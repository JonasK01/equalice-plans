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
import json
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

# ---------- EQUALICE brand skin ----------
EQ_LOGO_SVG = """
<svg width="176" height="50" viewBox="0 0 700 200" xmlns="http://www.w3.org/2000/svg">
  <g transform="translate(20, 30)">
    <circle cx="65" cy="65" r="56" fill="none" stroke="#0F1115" stroke-width="5"/>
    <path d="M 9 65 A 56 17 0 0 1 121 65" fill="none" stroke="#0F1115" stroke-width="5"/>
    <rect x="41" y="29" width="12" height="56" rx="1.5" fill="#FA7C04"/>
    <rect x="59" y="14" width="12" height="72" rx="1.5" fill="#FA7C04"/>
    <rect x="77" y="22" width="12" height="64" rx="1.5" fill="#FA7C04"/>
    <path d="M 9 65 A 56 17 0 0 0 121 65" fill="none" stroke="#0F1115" stroke-width="5"/>
  </g>
  <line x1="155" y1="65" x2="155" y2="140" stroke="#0F1115" stroke-width="3"/>
  <text x="170" y="125" font-family="Geist, system-ui, sans-serif" font-size="64" font-weight="600" letter-spacing="-2" fill="#0F1115">EQUALICE</text>
</svg>
"""

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500;600;700;800;900&family=Geist+Mono:wght@400;500&display=swap');
:root{
  --orange:#FA7C04; --orange-dark:#D85F00; --orange-light:#FFF4E8;
  --ink:#0F1115; --cream:#FAF7F2; --g700:#3F4651; --g500:#6B7280; --border:rgba(15,17,21,0.08);
}
/* Geist on TEXT elements only — never on icon glyphs (bare span/* would break Material icons) */
.stApp, .stApp p, .stApp li, .stApp label, .stApp a,
.stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6,
.stApp button, .stApp input, .stApp textarea, .stApp select,
.stApp [data-testid="stMarkdownContainer"], .stApp [data-baseweb="tab"],
.stApp [data-testid="stWidgetLabel"] {
  font-family:'Geist',-apple-system,BlinkMacSystemFont,system-ui,sans-serif !important;
}
/* protect Material icon glyphs (expander chevrons, radios, checks…) */
.stApp [data-testid="stIconMaterial"],
.stApp span.material-icons, .stApp span[class*="material-symbols"],
.stApp .material-symbols-rounded, .stApp .material-symbols-outlined {
  font-family:'Material Symbols Rounded','Material Symbols Outlined','Material Icons' !important;
}
.stApp { background:var(--cream); color:var(--ink); }
/* inputs stay light + legible */
.stTextInput input, .stTextArea textarea, [data-baseweb="input"] input {
  background:#fff !important; color:var(--ink) !important; border:1px solid var(--border) !important;
}
[data-testid="stHeader"] { background:transparent; }
.block-container { padding-top:2.5rem; max-width:1180px; }
h1,h2,h3,h4 { color:var(--ink) !important; font-weight:700 !important; letter-spacing:-0.03em !important; }
h1 { letter-spacing:-0.045em !important; }
a, a:visited { color:var(--orange); }
/* buttons */
.stButton>button, .stDownloadButton>button, [data-testid="stBaseButton-secondary"] {
  border-radius:6px; font-weight:600; border:1px solid var(--border); letter-spacing:-0.01em;
}
.stButton>button[kind="primary"], .stDownloadButton>button[kind="primary"],
[data-testid="stBaseButton-primary"] {
  background:var(--orange) !important; color:#fff !important; border-color:var(--orange) !important;
}
.stButton>button[kind="primary"]:hover, [data-testid="stBaseButton-primary"]:hover {
  background:var(--orange-dark) !important; border-color:var(--orange-dark) !important;
}
/* sidebar */
[data-testid="stSidebar"] { background:#fff; border-right:1px solid var(--border); }
[data-testid="stSidebar"] .block-container { padding-top:1.5rem; }
/* inputs, expanders, cards */
[data-testid="stExpander"] { border:1px solid var(--border) !important; border-radius:8px; background:#fff; }
.stTextInput input, .stTextArea textarea, [data-baseweb="select"]>div { border-radius:6px !important; }
[data-testid="stFileUploaderDropzone"] { border-radius:8px; border:1px dashed var(--border); }
/* progress + accents */
.stProgress > div > div > div > div { background:var(--orange) !important; }
[data-testid="stMetricValue"] { color:var(--ink); font-weight:700; }
code, [data-testid="stCaptionContainer"] { font-family:'Geist Mono',monospace !important; }
/* alert tints on brand */
[data-testid="stNotificationContentSuccess"] { }
hr { border-color:var(--border); }
</style>
""", unsafe_allow_html=True)


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


def _meta_path(slug: str, pdf_name: str) -> Path:
    return BRIEFS_DIR / slug / (pdf_name + ".meta.json")


def _save_plan_meta(slug: str, pdf_name: str, data: dict) -> None:
    try:
        _meta_path(slug, pdf_name).write_text(json.dumps(data), encoding="utf-8")
    except Exception:
        pass


def _load_plan_meta(slug: str, pdf_name: str) -> dict:
    p = _meta_path(slug, pdf_name)
    if p.exists():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def _build_and_report(cust, brief, out_path: Path, seo, feedback: str = "", source_upload: str = "") -> Path:
    """Build a plan (optionally applying reviewer feedback), show progress + QA, persist the
    source-sheet path so the plan can later be regenerated with feedback. Returns the PDF path."""
    ai_ready = has_api_key() and sdk_available()
    try:
        brief.all_keywords = SEOL.scrub_keywords(brief.all_keywords)
        brief.main_keywords = SEOL.scrub_keywords(brief.main_keywords)
    except Exception:
        pass

    progress = st.progress(0, text="Starting…")

    def _progress(pct: int, msg: str) -> None:
        try:
            progress.progress(min(max(pct, 0), 100), text=msg)
        except Exception:
            pass

    ai_instance = BriefAI(cust, brief, feedback=feedback) if ai_ready else None
    if ai_instance and not ai_instance.enabled:
        st.error(f"AI init failed: {ai_instance.status_message}. Falling back to templates.")
        ai_instance = None

    seo_title, seo_bullets, seo_backend = seo
    _res: dict = {}
    try:
        t0 = time.perf_counter()
        pdf_path = build_brief(
            cust, brief, out_path, ai=ai_instance, progress_cb=_progress,
            seo_title=seo_title, seo_bullets=seo_bullets, seo_backend=seo_backend, result_out=_res,
        )
        elapsed = time.perf_counter() - t0
    except Exception as exc:
        progress.empty()
        st.error(f"PDF build failed: {exc}")
        raise
    progress.empty()

    kb = pdf_path.stat().st_size // 1024
    if ai_instance:
        u = ai_instance.last_usage
        cost = (u["input"] / 1e6) * 3.0 + (u["cached"] / 1e6) * 0.30 + (u["output"] / 1e6) * 15.0
        st.success(f"✅ Built `{pdf_path.name}` · {kb} KB · {elapsed:.0f}s · ${cost:.2f}"
                   + (" · feedback applied" if feedback else ""))
        if ai_instance.errors:
            with st.expander(f"⚠️ {len(ai_instance.errors)} AI call(s) used template fallback", expanded=False):
                for e in ai_instance.errors:
                    st.code(e)
    else:
        st.success(f"✅ Built `{pdf_path.name}` · {kb} KB · {elapsed:.0f}s (template mode)")

    comp = _res.get("compliance") or []
    blocking = _res.get("compliance_blocking")
    copy_warn = _res.get("copy_warnings") or []
    c1, c2 = st.columns(2)
    with c1:
        if blocking:
            st.error(f"⛔ Compliance: {sum(1 for c in comp if getattr(c,'severity','')=='high')} blocking — fix before publishing.")
        elif comp:
            st.warning(f"⚠️ Compliance: {len(comp)} note(s), none blocking.")
        else:
            st.success("✅ Compliance passed.")
        for c in comp:
            st.caption(f"• [{getattr(c,'severity','?')}] {getattr(c,'issue','')}")
    with c2:
        if copy_warn:
            st.warning(f"⚠️ Copy length: {len(copy_warn)} over limit.")
            for w in copy_warn[:8]:
                st.caption(f"• {w}")
        else:
            st.success("✅ Copy lengths punchy.")

    _save_plan_meta(cust.slug, pdf_path.name, {"upload": str(source_upload), "product": brief.product_name or ""})
    return pdf_path


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

    # Work the feedback in — build a new version of THIS plan that applies the comments.
    _cs = CM.list_comments(slug, pdf_name)
    _up = _load_plan_meta(slug, pdf_name).get("upload", "")
    if _cs and _up and Path(_up).exists():
        st.markdown("---")
        st.caption("Apply the comments above to a fresh version of this plan (~4–5 min).")
        if st.button("🔄 New version applying the comments", key=f"{key_prefix}_regen", type="primary"):
            cust = load_customer(slug)
            brief = parse_excel(_up)
            seo_t = seo_b = seo_bk = None
            try:
                _s = SEOL.load_seo(_up)
                if _s.title:
                    seo_t, seo_b, seo_bk = _s.title, (SEOL.as_bullets_html(_s) or None), (_s.backend or None)
            except Exception:
                pass
            fb = "Apply these reviewer corrections to this new version:\n" + "\n".join(f"- {c['text']}" for c in _cs)
            stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            base = pdf_name[:-4] if pdf_name.endswith(".pdf") else pdf_name
            out_path = BRIEFS_DIR / slug / f"{base}__rev-{stamp}.pdf"
            newpdf = _build_and_report(cust, brief, out_path, (seo_t, seo_b, seo_bk), feedback=fb, source_upload=_up)
            st.session_state["last_plan"] = {"slug": slug, "name": newpdf.name}
            st.success("New version created — open it under **Plans & Review**.")
    elif _cs:
        st.caption("🔄 Tip: plans generated from the **Generate** page can be regenerated with the comments in one click.")


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

    # Slim active-brand strip — calm, one line, still prevents wrong-brand mistakes.
    _tag = f" · {cust.tagline}" if cust.tagline else ""
    st.markdown(
        f"""
        <div style="display:flex;align-items:center;gap:14px;background:#fff;
             border:1px solid rgba(15,17,21,0.08);border-left:4px solid {cust.primary_color};
             padding:11px 16px;border-radius:8px;margin:6px 0 20px 0;">
          <span style="font-size:18px;font-weight:700;color:#0F1115;letter-spacing:-0.02em;">{cust.name}</span>
          <span style="font-family:'Geist Mono',monospace;font-size:11px;color:#6B7280;letter-spacing:0.03em;">
            {cust.marketplace} · overlay {cust.overlay_language.upper()}{_tag}
          </span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.expander("Brand details & Brand Memory", expanded=False):
        tab_a, tab_b = st.tabs(["Brand details", "➕ Add to Brand Memory"])
        with tab_a:
            st.write(f"**Voice:** {cust.voice or '—'}")
            st.write(f"**Personality:** {', '.join(cust.personality) or '—'} · **Fonts:** {', '.join(cust.fonts) or '—'}")
            st.markdown(
                f"**Colours:** <span style='background:{cust.primary_color};color:#fff;padding:2px 8px;border-radius:3px;'>{cust.primary_color}</span> "
                f"<span style='background:{cust.accent_color};color:#fff;padding:2px 8px;border-radius:3px;'>{cust.accent_color}</span>",
                unsafe_allow_html=True,
            )
            st.caption(f"Photo rules — {cust.photo_rules[:220] or '—'}")
            st.caption(f"No-gos — {cust.no_gos[:220] or '—'}")
        with tab_b:
            st.caption("Saved to this brand's memory — informs every future plan (new info, positioning, corrections, reference images).")
            existing = KN.get_team_info(cust.slug)
            info = st.text_area("Extra product info / notes", value=existing, height=110, key="kn_info",
                                placeholder="e.g. new 500 ml size; hero colour teal; certified organic since 2025; avoid 'detox'…")
            kn_imgs = st.file_uploader("Reference images (optional)", type=["png", "jpg", "jpeg", "webp"],
                                       accept_multiple_files=True, key="kn_imgs")
            if st.button("💾 Save to Brand Memory", key="kn_save"):
                KN.save_team_info(cust.slug, info)
                n = 0
                for f in (kn_imgs or []):
                    KN.save_team_image(cust.slug, f.name, f.read()); n += 1
                st.success(f"Saved to {cust.name}'s memory" + (f" (+{n} image(s))" if n else "") + ".")
            cur = KN.list_team_images(cust.slug)
            if cur:
                st.caption("Images on file: " + ", ".join(cur))

    st.divider()
    st.markdown("#### 1 · Upload the SEO sheet")
    upload = st.file_uploader("Drop the product's SEO analysis .xlsx", type=["xlsx"], key="seo_up")
    if not upload:
        st.caption("SEO title + bullets come from the sheet — the tool writes the creative Image + A+ plan.")
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

    # SEO copy comes from the sheet (not AI); the tool only writes the creative plan.
    seo_title = seo_bullets = seo_backend = None
    try:
        _seo = SEOL.load_seo(upload_path)
        if _seo.title:
            seo_title = _seo.title
            seo_bullets = SEOL.as_bullets_html(_seo) or None
            seo_backend = _seo.backend or None
    except Exception:
        pass
    st.session_state["_seo"] = (seo_title, seo_bullets, seo_backend)

    # Brand mismatch is the one real risk → loud. Everything else stays a calm caption.
    excel_brand = (brief.brand or "").strip().lower()
    cust_brand = (cust.name or "").strip().lower()
    if excel_brand and cust_brand and excel_brand not in cust_brand and cust_brand not in excel_brand:
        st.error(f"⚠️ Brand mismatch — the sheet says **{brief.brand}**, active brand is **{cust.name}**. "
                 f"The plan will be styled as {cust.name}. Switch the brand above if this is wrong.")

    ok, missing = brief.has_minimum_data()
    _notes = []
    if seo_title:
        _notes.append(f"SEO copy from sheet ✓ ({len(seo_bullets or [])} bullets)")
    if not ok:
        _notes.append(f"missing: {', '.join(missing)} (placeholders used)")
    st.caption(" · ".join(_notes) if _notes else "Sheet read.")

    st.markdown("#### 2 · Review")
    m1, m2, m3 = st.columns(3)
    m1.metric("USPs", len(brief.usps))
    m2.metric("Keywords", len(brief.all_keywords))
    m3.metric("Q&A", len(brief.rufus_qa))
    with st.expander(f"Parsed data — {brief.product_name or 'product'}", expanded=False):
        st.write(f"**Product:** {brief.product_name or '—'}  ·  **ASIN:** {brief.asin or '—'}")
        if brief.listing_url:
            st.write(f"**Listing:** {brief.listing_url}")
        if brief.main_keywords:
            st.write(f"**Main keywords:** {', '.join(brief.main_keywords)}")
        if brief.usps:
            st.markdown("**USPs**")
            for u in brief.usps:
                st.markdown(f"- {u}")
        if brief.good_reviews or brief.bad_reviews:
            st.markdown(f"**Reviews** — {len(brief.good_reviews)} good / {len(brief.bad_reviews)} bad")
            for r in brief.good_reviews:
                st.markdown(f"+ {r}")
            for r in brief.bad_reviews:
                st.markdown(f"– {r}")
        if brief.rufus_qa:
            st.markdown("**Q&A**")
            for qa in brief.rufus_qa:
                st.markdown(f"**Q.** {qa['q']}  \n**A.** {qa['a']}")
        if brief.all_keywords:
            st.caption("Keywords: " + ", ".join(brief.all_keywords))

    st.divider()
    st.markdown("#### 3 · Generate")
    ai_ready = has_api_key() and sdk_available()
    if ai_ready:
        st.caption(f"AI writes the 7-image plan + 7 A+ modules + Q&A for {cust.name}, then an elite copywriting "
                   f"pass. ~4–5 min · SEO copy stays from the sheet · every plan is compliance-scanned.")
    else:
        st.warning("AI is disabled (no API key) — the plan will use template copy.")

    if st.button("Generate PDF", type="primary"):
        out_dir = BRIEFS_DIR / cust.slug
        out_dir.mkdir(parents=True, exist_ok=True)
        slug_name = slugify(brief.product_name or upload.name.replace(".xlsx", ""))[:80]
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        out_path = out_dir / f"{cust.slug}__{slug_name}__{stamp}.pdf"

        _seo = st.session_state.get("_seo", (None, None, None))
        pdf_path = _build_and_report(cust, brief, out_path, _seo, source_upload=str(upload_path))

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
    st.markdown(EQ_LOGO_SVG, unsafe_allow_html=True)
    st.markdown("### Image + A+ Plan Generator")
    st.caption("Team access — enter the password to continue.")
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
    st.markdown(EQ_LOGO_SVG, unsafe_allow_html=True)
    st.markdown(
        "<div style='font-family:Geist Mono,monospace;font-size:10px;letter-spacing:0.16em;"
        "text-transform:uppercase;color:#6B7280;margin:6px 0 2px 2px;'>Image + A+ Plan Generator</div>",
        unsafe_allow_html=True,
    )
    page = st.radio("Section", options=list(PAGES.keys()), label_visibility="collapsed")
    st.divider()
    st.text_input("Your name (for comments)", key="reviewer", placeholder="e.g. Jonas")
    st.divider()
    st.caption(f"AI ({AI_MODEL}): {'✓ ready' if (has_api_key() and sdk_available()) else '✗ disabled — set ' + ANTHROPIC_KEY_ENV}")
    st.caption(f"Unsplash key: {'✓ set' if has_unsplash_key() else '✗ missing'}")
    st.caption("Customers + briefs stored under `tools/brief_app/`")

PAGES[page]()
