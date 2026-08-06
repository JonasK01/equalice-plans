"""EQUALICE Brief App — Streamlit front-end.

Run locally:
    streamlit run tools/brief_app/app.py

Writers select an existing customer (or create a new one), upload the SEO
analysis Excel for a single SKU, click "Generate Brief", preview the parsed
fields, and download the branded PDF.
"""
from __future__ import annotations
import os
import re
import sys
import time
import base64
from datetime import datetime
from pathlib import Path

# Make `tools.brief_app...` imports work when streamlit launches the file directly
ROOT_REPO = Path(__file__).resolve().parent.parent.parent
if str(ROOT_REPO) not in sys.path:
    sys.path.insert(0, str(ROOT_REPO))

import streamlit as st

from tools.brief_app.core.config import BRIEFS_DIR, MARKETPLACES, PERSONALITY_OPTIONS
from tools.brief_app.core.customers import (
    Customer, list_customers, load_customer, save_customer, delete_customer,
    save_logo, slugify,
)
from tools.brief_app.core.excel_parser import parse_excel
from tools.brief_app.core.pdf_builder import build_brief
from tools.brief_app.core import seo_loader as SEOL
from tools.brief_app.core.unsplash import has_unsplash_key, UNSPLASH_KEY_ENV
from tools.brief_app.core.ai import BriefAI, has_api_key, sdk_available, ANTHROPIC_KEY_ENV, MODEL as AI_MODEL
from tools.brief_app.core import comments as CM
from tools.brief_app.core import knowledge as KN


st.set_page_config(
    page_title="EQUALICE · Brief Generator",
    page_icon="📄",
    layout="wide",
)


# ---------- helpers ----------

def _customer_picker(customers: list[Customer]) -> Customer | None:
    """Slug-based picker — survives list reordering when new customers are added.

    The session_state stores the SLUG (stable id), not the list index (which shifts
    when a new customer is inserted into the alphabetically-sorted list).
    """
    if not customers:
        return None
    slugs = [c.slug for c in customers]
    labels = {c.slug: f"{c.name}  ({c.marketplace})" for c in customers}

    saved_slug = st.session_state.get("active_customer_slug")
    if saved_slug not in slugs:
        saved_slug = slugs[0]
    idx = slugs.index(saved_slug)

    pick_slug = st.selectbox(
        "Active customer",
        options=slugs,
        format_func=lambda s: labels[s],
        index=idx,
        key="customer_picker",
    )
    st.session_state["active_customer_slug"] = pick_slug
    return next(c for c in customers if c.slug == pick_slug)


def _customer_form(existing: Customer | None) -> Customer | None:
    """Customer create/edit form. Returns saved Customer on submit, else None."""
    is_new = existing is None
    prefix = "new" if is_new else f"edit_{existing.slug}"

    with st.form(f"customer_form_{prefix}", clear_on_submit=is_new):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Brand name *", value="" if is_new else existing.name)
            marketplace_keys = list(MARKETPLACES.keys())
            mp_index = marketplace_keys.index(existing.marketplace) if (existing and existing.marketplace in marketplace_keys) else 0
            marketplace = st.selectbox(
                "Marketplace",
                options=marketplace_keys,
                format_func=lambda k: MARKETPLACES[k]["label"],
                index=mp_index,
            )
            tagline = st.text_input("Tagline", value="" if is_new else existing.tagline)
            voice = st.text_area("Brand voice", value="" if is_new else existing.voice, height=80)

        with col2:
            primary = st.color_picker("Primary color", value="#222222" if is_new else existing.primary_color)
            accent = st.color_picker("Accent color", value="#888888" if is_new else existing.accent_color)
            text_color = st.color_picker("Text color", value="#000000" if is_new else existing.text_color)
            bg = st.color_picker("Background", value="#FFFFFF" if is_new else existing.background_color)
            mood_bg = st.color_picker("Moodboard background", value="#F5F1EA" if is_new else existing.mood_background_color)

        personality = st.multiselect(
            "Personality (pick up to 4)",
            options=sorted(set(PERSONALITY_OPTIONS + (existing.personality if existing else []))),
            default=[] if is_new else existing.personality,
            max_selections=4,
        )
        fonts_raw = st.text_input(
            "Font stack (comma-separated)",
            value="Inter" if is_new else ", ".join(existing.fonts),
        )
        photo_rules = st.text_area(
            "Photography rules",
            value="" if is_new else existing.photo_rules,
            height=80,
        )
        no_gos = st.text_area(
            "No-gos (what NEVER to show)",
            value="" if is_new else existing.no_gos,
            height=70,
        )
        mood_terms_raw = st.text_area(
            "Moodboard search prompts (one per line — used to fetch Unsplash references)",
            value="" if is_new else "\n".join(existing.moodboard_search_terms),
            height=110,
        )
        creative_freedom = st.slider(
            "Creative freedom (1 strict — 5 free)",
            min_value=1, max_value=5,
            value=4 if is_new else existing.creative_freedom,
        )
        st.markdown("**A+ house rules**")
        new_brand = st.checkbox(
            "New brand — no Comparison module (Module 7 becomes a 'From the Brand' banner instead)",
            value=True if is_new else existing.new_brand,
            help="Freshly onboarded brands don't compare yet. Keeps 7 modules; swaps Comparison for a brand-voice 'From the Brand' close.",
        )
        brand_statement = st.text_area(
            "'From the Brand' statement (the cool brand line for the A+ close)",
            value="" if is_new else existing.brand_statement,
            height=70,
            placeholder="From <Brand>: <one punchy, on-brand promise>.",
            help="Shown as the 'From the Brand' module (and only used when 'New brand' is on).",
        )
        notes = st.text_area(
            "Internal notes",
            value="" if is_new else existing.notes,
            height=60,
        )
        logo_upload = st.file_uploader("Brand logo (PNG / JPG)", type=["png", "jpg", "jpeg"])

        submit_label = "Create customer" if is_new else "Save changes"
        submitted = st.form_submit_button(submit_label, type="primary")

    if not submitted:
        return None

    if not name.strip():
        st.error("Brand name is required.")
        return None

    slug = existing.slug if existing else slugify(name)
    cust = Customer(
        slug=slug,
        name=name.strip(),
        marketplace=marketplace,
        overlay_language=MARKETPLACES[marketplace]["lang"],
        primary_color=primary,
        accent_color=accent,
        text_color=text_color,
        background_color=bg,
        mood_background_color=mood_bg,
        voice=voice.strip(),
        tagline=tagline.strip(),
        personality=personality,
        fonts=[f.strip() for f in fonts_raw.split(",") if f.strip()] or ["Inter"],
        photo_rules=photo_rules.strip(),
        no_gos=no_gos.strip(),
        moodboard_search_terms=[m.strip() for m in mood_terms_raw.splitlines() if m.strip()],
        creative_freedom=creative_freedom,
        logo_path=existing.logo_path if existing else None,
        notes=notes.strip(),
        new_brand=new_brand,
        brand_statement=brand_statement.strip(),
        created_at=existing.created_at if existing else "",
        updated_at="",
    )
    saved = save_customer(cust)

    if logo_upload:
        ext = logo_upload.name.split(".")[-1]
        rel = save_logo(saved.slug, logo_upload.read(), ext)
        saved.logo_path = rel
        save_customer(saved)

    st.success(f"Saved: {saved.name}")
    return saved


# ---------- shared UI helpers ----------

def _render_pdf_inline(pdf_path: Path, height: int = 900) -> None:
    """Embed the generated PDF in the page so reviewers see it without downloading."""
    try:
        data = Path(pdf_path).read_bytes()
    except Exception:
        st.info("PDF not available.")
        return
    b64 = base64.b64encode(data).decode()
    st.markdown(
        f'<iframe src="data:application/pdf;base64,{b64}" width="100%" height="{height}" '
        f'style="border:1px solid #ddd;border-radius:8px;"></iframe>',
        unsafe_allow_html=True,
    )


def _reviewer_name() -> str:
    return (st.session_state.get("reviewer") or "").strip() or "anon"


def _comment_thread_ui(slug: str, pdf_name: str, key_prefix: str) -> None:
    """Review status + comment thread for a plan (persisted in /data, shared across the team)."""
    status = CM.get_status(slug, pdf_name)
    new_status = st.selectbox(
        "Review status", CM.STATUSES,
        index=CM.STATUSES.index(status) if status in CM.STATUSES else 0,
        key=f"{key_prefix}_status",
    )
    if new_status != status:
        CM.set_status(slug, pdf_name, new_status)
        st.rerun()

    for c in CM.list_comments(slug, pdf_name):
        when = datetime.fromtimestamp(c.get("ts", 0)).strftime("%Y-%m-%d %H:%M")
        st.markdown(f"**{c.get('author','anon')}** · _{when}_")
        st.markdown(f"> {c.get('text','')}")
    else:
        pass

    txt = st.text_area("Add a comment", key=f"{key_prefix}_new",
                       placeholder="e.g. Overlay 3 too long; make image 5 warmer; add the award badge…")
    learn = st.checkbox(
        "📚 Also save as a brand learning — the AI applies it to every future plan for this brand",
        key=f"{key_prefix}_learn",
    )
    if st.button("Post comment", key=f"{key_prefix}_post"):
        if txt.strip():
            CM.add_comment(slug, pdf_name, _reviewer_name(), txt)
            if learn:
                KN.add_review_learning(slug, txt, _reviewer_name())
            st.rerun()
        else:
            st.warning("Write something first.")
    _lc = KN.get_review_learnings(slug)
    if _lc:
        n = _lc.count("\n- ")
        st.caption(f"🧠 {n} brand learning(s) from past reviews are being applied to new plans.")


# ---------- pages ----------

def page_generate() -> None:
    st.title("Generate Image + A+ Premium Plan")
    customers = list_customers()
    if not customers:
        st.info("No customers yet. Create one in the **Customers** page first.")
        return

    cust = _customer_picker(customers)
    if not cust:
        return

    # Big, unmistakable active-customer banner so writers cannot accidentally
    # ship a brief styled with the wrong brand.
    st.markdown(
        f"""
        <div style="
            background: linear-gradient(90deg, {cust.primary_color}25 0%, {cust.accent_color}10 100%);
            border-left: 6px solid {cust.primary_color};
            padding: 14px 18px; border-radius: 6px; margin: 10px 0 18px 0;
        ">
          <div style="font-size: 12px; color: #555; letter-spacing: 1px;">ACTIVE BRAND</div>
          <div style="font-size: 22px; font-weight: 700; color: {cust.accent_color};">{cust.name}</div>
          <div style="font-size: 13px; color: #444; margin-top: 4px;">
            Marketplace <b>{cust.marketplace}</b> &nbsp;·&nbsp; Overlay language <b>{cust.overlay_language.upper()}</b>
            &nbsp;·&nbsp; Tagline <i>{cust.tagline or '—'}</i>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.expander("Brand details (colors, voice, photo rules)", expanded=False):
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Voice:** {cust.voice or '—'}")
            st.write(f"**Personality:** {', '.join(cust.personality) or '—'}")
            st.write(f"**Fonts:** {', '.join(cust.fonts) or '—'}")
        with col2:
            st.markdown(
                f"**Colors:** <span style='background:{cust.primary_color};color:white;padding:2px 8px;border-radius:3px;'>{cust.primary_color}</span> "
                f"<span style='background:{cust.accent_color};color:white;padding:2px 8px;border-radius:3px;'>{cust.accent_color}</span>",
                unsafe_allow_html=True,
            )
            st.write(f"**Photo rules:** {cust.photo_rules[:200] or '—'}")
            st.write(f"**No-gos:** {cust.no_gos[:200] or '—'}")

    with st.expander("➕ Add product info / reference images to Brand Memory (feeds every future plan)", expanded=False):
        st.caption(
            "Anything you add here is saved to this brand's memory and informs EVERY future "
            "generation — new product details, positioning, corrections, reference images."
        )
        existing = KN.get_team_info(cust.slug)
        info = st.text_area("Extra product info / notes", value=existing, height=120,
                            placeholder="e.g. New 500 ml size launching; hero color teal; certified organic since 2025; avoid the word 'detox'…",
                            key="kn_info")
        kn_imgs = st.file_uploader("Reference images (optional)", type=["png", "jpg", "jpeg", "webp"],
                                   accept_multiple_files=True, key="kn_imgs")
        if st.button("💾 Save to Brand Memory", key="kn_save"):
            KN.save_team_info(cust.slug, info)
            n = 0
            for f in (kn_imgs or []):
                KN.save_team_image(cust.slug, f.name, f.read()); n += 1
            st.success(f"Saved — now part of {cust.name}'s memory for every future plan"
                       + (f" (+{n} image(s))" if n else "") + ".")
        cur = KN.list_team_images(cust.slug)
        if cur:
            st.caption("Reference images on file: " + ", ".join(cur))

    st.divider()
    st.subheader("Step 1 — Upload SEO Excel")
    if not has_unsplash_key():
        st.warning(
            f"No `{UNSPLASH_KEY_ENV}` set. Moodboard tiles will fall back to placeholder boxes with the search prompt. "
            "Get a free key at https://unsplash.com/developers and set the environment variable before launching Streamlit."
        )

    upload = st.file_uploader("Drop the customer's SEO analysis .xlsx here", type=["xlsx"])
    if not upload:
        return

    # Save upload to a tmp working path so the parser (file-based) can read it
    work_dir = BRIEFS_DIR / cust.slug / "_uploads"
    work_dir.mkdir(parents=True, exist_ok=True)
    safe_name = re.sub(r"[^A-Za-z0-9._-]+", "_", upload.name)
    upload_path = work_dir / f"{int(time.time())}__{safe_name}"
    upload_path.write_bytes(upload.read())

    with st.spinner("Parsing Excel…"):
        try:
            brief = parse_excel(upload_path)
        except Exception as exc:
            st.error(f"Excel parse failed: {exc}")
            return

    ok, missing = brief.has_minimum_data()
    if not ok:
        st.warning(f"Missing recommended fields: {', '.join(missing)}. The brief will still build with placeholders.")

    # SEO copy is the SEO team's job — take TITLE + BULLETS + BACKEND from the sheet (not AI).
    # The app only generates the CREATIVE Image + A+ Premium plan.
    seo_title = seo_bullets = seo_backend = None
    try:
        _seo = SEOL.load_seo(upload_path)
        if _seo.title:
            seo_title = _seo.title
            seo_bullets = SEOL.as_bullets_html(_seo) or None
            seo_backend = _seo.backend or None
    except Exception:
        pass  # no filled SEO sheet -> AI will draft copy as a fallback
    st.session_state["_seo"] = (seo_title, seo_bullets, seo_backend)
    if seo_title:
        st.info(
            f"📋 **SEO copy taken from the sheet** (not AI-written): title + "
            f"{len(seo_bullets or [])} bullets + backend. The app generates only the "
            f"Image plan + A+ Premium modules."
        )

    # Brand-mismatch check: warn loud if the Excel mentions a different brand than
    # the active customer. This is the #1 way writers ship the wrong-branded PDF.
    excel_brand = (brief.brand or "").strip().lower()
    cust_brand = (cust.name or "").strip().lower()
    if excel_brand and cust_brand and excel_brand not in cust_brand and cust_brand not in excel_brand:
        st.error(
            f"⚠️ **Brand mismatch.** The Excel says brand **“{brief.brand}”**, "
            f"but the active customer is **“{cust.name}”**. "
            f"The brief will be styled with {cust.name}'s colors, voice, photo rules — "
            f"but the product copy + ASIN will be for {brief.brand}. "
            f"This is almost always a mistake. Switch the customer above, or upload the correct Excel."
        )
    elif excel_brand and cust_brand:
        st.success(f"Brand match: Excel brand “{brief.brand}” aligns with active customer “{cust.name}”.")

    st.subheader("Step 2 — Review parsed data")
    col1, col2, col3 = st.columns(3)
    col1.metric("USPs", len(brief.usps))
    col2.metric("Keywords", len(brief.all_keywords))
    col3.metric("Q&A pairs", len(brief.rufus_qa))

    with st.expander("Product info"):
        st.write(f"**Product:** {brief.product_name or '—'}")
        st.write(f"**ASIN:** {brief.asin or '—'}")
        st.write(f"**Brand from Excel:** {brief.brand or '—'}")
        st.write(f"**Listing URL:** {brief.listing_url or '—'}")
        st.write(f"**Main keywords:** {', '.join(brief.main_keywords) or '—'}")
    with st.expander(f"USPs ({len(brief.usps)})"):
        for u in brief.usps:
            st.markdown(f"- {u}")
    with st.expander(f"Reviews ({len(brief.good_reviews)} good / {len(brief.bad_reviews)} bad)"):
        if brief.good_reviews:
            st.markdown("**Good:**")
            for r in brief.good_reviews:
                st.markdown(f"+ {r}")
        if brief.bad_reviews:
            st.markdown("**Bad:**")
            for r in brief.bad_reviews:
                st.markdown(f"– {r}")
    with st.expander(f"RUFUS Q&A ({len(brief.rufus_qa)})"):
        for qa in brief.rufus_qa:
            st.markdown(f"**Q.** {qa['q']}")
            st.markdown(f"**A.** {qa['a']}")
            st.markdown("---")
    with st.expander(f"Keywords ({len(brief.all_keywords)})"):
        st.write(", ".join(brief.all_keywords))

    st.divider()
    st.subheader("Step 3 — Generate the brief")
    st.caption(
        f"This will build a branded PDF for **{cust.name}** "
        f"({cust.marketplace}, overlay {cust.overlay_language.upper()}) using the data parsed above."
    )

    # AI status note before generate
    ai_ready = has_api_key() and sdk_available()
    if ai_ready:
        st.success(
            f"🧠 **AI creative enabled** — Claude writes the 7-image plan, 7 A+ modules, Q&A "
            f"and argumentation (the CREATIVE). SEO title + bullets come from the sheet, not AI. "
            f"~10 API calls per brief, ~$0.10 with prompt caching. Build takes ~1–3 minutes."
        )
    else:
        st.warning(
            f"⚠️ **AI copywriting disabled** — falling back to template strings. "
            f"Set `{ANTHROPIC_KEY_ENV}=sk-ant-...` in your environment and restart Streamlit to enable "
            f"Sonnet 4.6 copywriting."
        )

    if st.button("Generate PDF", type="primary"):
        out_dir = BRIEFS_DIR / cust.slug
        out_dir.mkdir(parents=True, exist_ok=True)
        slug_name = slugify(brief.product_name or upload.name.replace(".xlsx", ""))[:80]
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        out_path = out_dir / f"{cust.slug}__{slug_name}__{stamp}.pdf"

        progress = st.progress(0, text="Starting…")

        def _progress(pct: int, msg: str) -> None:
            try:
                progress.progress(min(max(pct, 0), 100), text=msg)
            except Exception:
                pass

        ai_instance = BriefAI(cust, brief) if ai_ready else None
        if ai_instance and not ai_instance.enabled:
            st.error(f"AI init failed: {ai_instance.status_message}. Falling back to templates.")
            ai_instance = None

        _seo_title, _seo_bullets, _seo_backend = st.session_state.get("_seo", (None, None, None))
        _res: dict = {}
        try:
            t0 = time.perf_counter()
            pdf_path = build_brief(
                cust, brief, out_path, ai=ai_instance, progress_cb=_progress,
                seo_title=_seo_title, seo_bullets=_seo_bullets, seo_backend=_seo_backend,
                result_out=_res,
            )
            elapsed = time.perf_counter() - t0
        except Exception as exc:
            progress.empty()
            st.error(f"PDF build failed: {exc}")
            raise

        # Surface AI usage stats if applicable
        if ai_instance:
            usage = ai_instance.last_usage
            cache_hit_pct = (
                round(100 * usage["cached"] / max(1, usage["input"] + usage["cached"]))
                if (usage["input"] + usage["cached"]) > 0 else 0
            )
            cost_input = (usage["input"] / 1_000_000) * 3.0 + (usage["cached"] / 1_000_000) * 0.30
            cost_output = (usage["output"] / 1_000_000) * 15.0
            st.success(
                f"✅ Brief built for **{cust.name}** — `{pdf_path.name}` "
                f"({pdf_path.stat().st_size // 1024} KB)"
            )
            cols = st.columns(4)
            cols[0].metric("Time", f"{elapsed:.1f} s")
            cols[1].metric("Input tokens", f"{usage['input'] + usage['cached']:,}", f"{cache_hit_pct}% cached")
            cols[2].metric("Output tokens", f"{usage['output']:,}")
            cols[3].metric("Cost", f"${cost_input + cost_output:.3f}")

            if ai_instance.errors:
                with st.expander(f"⚠️ {len(ai_instance.errors)} AI call(s) fell back to template", expanded=False):
                    for err in ai_instance.errors:
                        st.code(err)
        else:
            st.success(
                f"✅ Brief built for **{cust.name}** — `{pdf_path.name}` "
                f"({pdf_path.stat().st_size // 1024} KB) in {elapsed:.1f}s (template mode)"
            )

        # Auto-QA results (run on every build): compliance + on-image copy lengths.
        comp = _res.get("compliance") or []
        blocking = _res.get("compliance_blocking")
        copy_warn = _res.get("copy_warnings") or []
        cc1, cc2 = st.columns(2)
        with cc1:
            if blocking:
                st.error(f"⛔ COMPLIANCE: {len([c for c in comp if getattr(c,'severity','')=='high'])} blocking issue(s) — fix before publishing.")
            elif comp:
                st.warning(f"⚠️ COMPLIANCE: {len(comp)} low note(s), none blocking.")
            else:
                st.success("✅ COMPLIANCE: passed — no issues.")
            for c in comp:
                st.caption(f"• [{getattr(c,'severity','?')}] {getattr(c,'issue','')}")
        with cc2:
            if copy_warn:
                st.warning(f"⚠️ COPY LENGTHS: {len(copy_warn)} item(s) over the punchy limit.")
                for w in copy_warn[:8]:
                    st.caption(f"• {w}")
            else:
                st.success("✅ COPY LENGTHS: punchy (overlays ≤30ch/≤5 words).")

        # Persist as the "last plan" so the preview + comment thread survive Streamlit reruns.
        st.session_state["last_plan"] = {"slug": cust.slug, "name": pdf_path.name}

    # Persistent review area — renders on every rerun (e.g. after posting a comment).
    last = st.session_state.get("last_plan")
    if last and last.get("slug") == cust.slug:
        p = BRIEFS_DIR / last["slug"] / last["name"]
        if p.exists():
            st.divider()
            st.subheader("📄 Generated plan — preview & review")
            st.caption(f"`{last['name']}`  ·  status: **{CM.get_status(last['slug'], last['name'])}**")
            _render_pdf_inline(p)
            with p.open("rb") as f:
                st.download_button("⬇️  Download PDF", data=f.read(), file_name=p.name,
                                   mime="application/pdf", type="primary", key="dl_last")
            st.markdown("#### 💬 Comments")
            _comment_thread_ui(last["slug"], last["name"], key_prefix="gen")


def page_customers() -> None:
    st.title("Customers")
    customers = list_customers()

    tabs = st.tabs(["Existing", "+ New customer"])

    with tabs[0]:
        if not customers:
            st.info("No customers yet — create one in the next tab.")
        else:
            for c in customers:
                with st.expander(f"{c.name} · {c.marketplace}"):
                    st.json(c.to_json(), expanded=False)
                    edit_col, delete_col = st.columns([1, 1])
                    if edit_col.button(f"Edit {c.name}", key=f"edit_{c.slug}"):
                        st.session_state["editing"] = c.slug
                    if delete_col.button(f"Delete {c.name}", key=f"del_{c.slug}"):
                        delete_customer(c.slug)
                        st.success(f"Deleted {c.name}")
                        st.rerun()

            editing_slug = st.session_state.get("editing")
            if editing_slug:
                try:
                    cust = load_customer(editing_slug)
                    st.subheader(f"Editing {cust.name}")
                    saved = _customer_form(cust)
                    if saved:
                        st.session_state.pop("editing", None)
                        st.rerun()
                except FileNotFoundError:
                    st.session_state.pop("editing", None)

    with tabs[1]:
        st.subheader("Create new customer")
        saved = _customer_form(None)
        if saved:
            st.rerun()


_STATUS_ICON = {"open": "🟡", "approved": "🟢", "changes requested": "🔴"}


def page_archive() -> None:
    st.title("Plans & Review")
    customers = list_customers()
    if not customers:
        st.info("No customers yet.")
        return

    with_plans = [(c, CM.list_plans(c.slug)) for c in customers]
    with_plans = [(c, pl) for c, pl in with_plans if pl]
    if not with_plans:
        st.info("No plans generated yet. Create one on the **Generate** page.")
        return

    labels = {c.slug: f"{c.name}  ({len(pl)} plan{'s' if len(pl) != 1 else ''})" for c, pl in with_plans}
    pick = st.selectbox("Brand", [c.slug for c, _ in with_plans],
                        format_func=lambda s: labels.get(s, s), key="arch_brand")
    cust, plans = next((c, pl) for c, pl in with_plans if c.slug == pick)

    for plan in plans:
        icon = _STATUS_ICON.get(plan["status"], "🟡")
        when = datetime.fromtimestamp(plan["mtime"]).strftime("%Y-%m-%d %H:%M")
        header = (f"{icon}  {plan['name']}   ·   {when}   ·   {plan['size_kb']} KB"
                  f"   ·   💬 {plan['comment_count']}")
        with st.expander(header, expanded=False):
            p = Path(plan["path"])
            _render_pdf_inline(p, height=800)
            with p.open("rb") as f:
                st.download_button("⬇️  Download PDF", data=f.read(), file_name=p.name,
                                   mime="application/pdf", key=f"dl_{plan['name']}")
            st.markdown("#### 💬 Comments")
            _comment_thread_ui(cust.slug, plan["name"], key_prefix=f"arch_{plan['name']}")


# ---------- access gate (for hosted deployments) ----------

def _password_gate() -> bool:
    """If APP_PASSWORD is set (hosted URL), require it once per session.
    If unset (local use), the app is open. Keeps the hosted tool team-only."""
    required = os.environ.get("APP_PASSWORD", "").strip()
    if not required:
        return True
    if st.session_state.get("_authed"):
        return True
    st.title("EQUALICE · Image + A+ Plan Generator")
    pw = st.text_input("Team password", type="password")
    if st.button("Enter", type="primary"):
        if pw == required:
            st.session_state["_authed"] = True
            st.rerun()
        else:
            st.error("Wrong password.")
    return False


# ---------- main ----------

PAGES = {
    "Generate Image + A+ plan": page_generate,
    "Plans & Review": page_archive,
    "Customers": page_customers,
}

if not _password_gate():
    st.stop()

with st.sidebar:
    st.markdown("## EQUALICE\n### Brief Generator")
    page = st.radio("Section", options=list(PAGES.keys()), label_visibility="collapsed")
    st.divider()
    st.text_input("Your name (for comments)", key="reviewer", placeholder="e.g. Jonas")
    st.divider()
    st.caption(f"AI ({AI_MODEL}): {'✓ ready' if (has_api_key() and sdk_available()) else '✗ disabled — set ' + ANTHROPIC_KEY_ENV}")
    st.caption(f"Unsplash key: {'✓ set' if has_unsplash_key() else '✗ missing'}")
    st.caption("Customers + briefs stored under `tools/brief_app/`")

PAGES[page]()
