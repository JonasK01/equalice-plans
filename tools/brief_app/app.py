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

from tools.brief_app.core.config import (
    BRIEFS_DIR, MARKETPLACES, OVERLAY_LANGUAGES, PERSONALITY_OPTIONS,
)
from tools.brief_app.core.customers import (
    Customer, list_customers, load_customer, save_customer, delete_customer,
    save_logo, slugify,
)
from tools.brief_app.core.excel_parser import parse_excel
from tools.brief_app.core.pdf_builder import build_brief
from tools.brief_app.core import pdf_builder as PB
from tools.brief_app.core import seo_loader as SEOL
from tools.brief_app.core.unsplash import has_unsplash_key, UNSPLASH_KEY_ENV
from tools.brief_app.core.ai import BriefAI, has_api_key, sdk_available, ANTHROPIC_KEY_ENV, MODEL as AI_MODEL
from tools.brief_app.core import comments as CM
from tools.brief_app.core import knowledge as KN
from tools.brief_app.core.i18n import LANGUAGES, get_ui_language, set_ui_language, t as T


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
            # The marketplace language is only the default. It used to be forced, which made
            # English overlays impossible on a non-.com marketplace — wrong for brands whose
            # packaging and creative are English even when they sell on amazon.de.
            _ov_keys = list(OVERLAY_LANGUAGES.keys())
            _ov_default = (existing.overlay_language if existing
                           else MARKETPLACES[marketplace]["lang"])
            overlay_language = st.selectbox(
                "Overlay language (on-image text)",
                options=_ov_keys,
                format_func=lambda c: OVERLAY_LANGUAGES[c],
                index=_ov_keys.index(_ov_default) if _ov_default in _ov_keys else 0,
                help="The language of the text ON the images. Brief body copy is always "
                     "English. Defaults to the marketplace language.",
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
        st.markdown("**Website & About Us**")
        st.caption("The brand's own words. Used for voice, the founding story and real claims — "
                   "so a plan never has to invent a brand story.")
        website_url = st.text_input(
            "Website URL",
            value="" if is_new else existing.website_url,
            placeholder="https://brand.com",
        )
        about_us = st.text_area(
            "About Us / brand story (paste from their About page)",
            value="" if is_new else existing.about_us,
            height=110,
            placeholder="Paste the brand's About Us text here — who founded it, why, what they "
                        "stand for, any credentials worth using (e.g. 'created by a hospice "
                        "social worker', 'family farm since 1978').",
            help="Ask the client for this during onboarding. It is the single best source for the "
                 "A+ brand banner and the 'From the Brand' close.",
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
        overlay_language=overlay_language,
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
        website_url=website_url.strip(),
        about_us=about_us.strip(),
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


def _when(ts: int) -> str:
    """Local wall-clock time for a plan. The archive used to show a bare timestamp with no
    sense of recency, so nobody could tell which version was current at a glance."""
    dt = datetime.fromtimestamp(ts)
    today = datetime.now().date()
    delta = (today - dt.date()).days
    day = {0: "heute", 1: "gestern"}.get(delta) or dt.strftime("%d.%m.%Y")
    return f"{day}, {dt.strftime('%H:%M')}"


def _download_name(slug: str, pdf_name: str) -> str:
    """A filename that means something on the designer's desktop.

    Generated files are named `<brand>__<product>__<stamp>.pdf`, which downloads as an
    unreadable slug blob. This rebuilds it as
    `EQUALICE_<Brand>_<Product>_Image-Plan_v<n>_<YYYY-MM-DD>.pdf` (team feedback:
    "richtige Benennung nach Herunterladen")."""
    meta = _load_plan_meta(slug, pdf_name)
    try:
        cust_name = load_customer(slug).name
    except Exception:
        cust_name = slug
    product = (meta.get("product") or "").strip()
    if not product:
        base = CM.plan_family(pdf_name)
        product = re.sub(r"^%s__" % re.escape(slug), "", base).split("__")[0].replace("-", " ")
    version = ""
    for pl in CM.list_plans(slug):
        if pl["name"] == pdf_name:
            if pl["versions_total"] > 1:
                version = f"_v{pl['version']}"
            break
    stamp = ""
    p = BRIEFS_DIR / slug / pdf_name
    if p.exists():
        stamp = "_" + datetime.fromtimestamp(p.stat().st_mtime).strftime("%Y-%m-%d")

    def clean(s: str) -> str:
        return re.sub(r"[^A-Za-z0-9]+", "-", (s or "")).strip("-")[:45] or "Plan"

    return f"EQUALICE_{clean(cust_name)}_{clean(product)}_Image-Plan{version}{stamp}.pdf"


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


_AI_BLOCK_FILE = BRIEFS_DIR.parent / "ai_block.json"


def _read_ai_block() -> str:
    """The last account-level refusal, shared by everyone using the tool.

    Kept on the data volume rather than in session state so the whole team is warned by
    the first person who hits it. Without this every colleague burns one build discovering
    the same outage for themselves."""
    try:
        import json as _j
        d = _j.loads(_AI_BLOCK_FILE.read_text(encoding="utf-8"))
        return str(d.get("reason") or "")
    except Exception:
        return ""


def _write_ai_block(reason: str) -> None:
    try:
        import json as _j
        if reason:
            _AI_BLOCK_FILE.write_text(
                _j.dumps({"reason": reason, "at": datetime.now().isoformat(timespec="seconds")}),
                encoding="utf-8")
        elif _AI_BLOCK_FILE.exists():
            _AI_BLOCK_FILE.unlink()          # a successful run clears it for everyone
    except Exception:
        pass


def _ai_blocked_reason() -> str:
    """Why generating right now would produce template boilerplate, or "" if it is fine.

    Two sources: the obvious one (no key, no SDK) and the one that only shows up mid-build
    (the account refused the work). The second is remembered for the rest of the session so
    the next click is warned BEFORE spending four minutes on a plan nobody can use."""
    if not sdk_available():
        return "The Anthropic SDK is not installed in this container."
    if not has_api_key():
        return f"No API key is set. Add {ANTHROPIC_KEY_ENV} to the server's .env and restart."
    return st.session_state.get("_ai_blocked", "") or _read_ai_block()


def _ai_preflight() -> bool:
    """Show a blocking banner when AI is unavailable. Returns True when it is safe to build."""
    reason = _ai_blocked_reason()
    if not reason:
        return True
    st.error(
        "⛔ **AI copywriting is unavailable — do not generate plans right now.**\n\n"
        + reason
        + "\n\nAnything generated in this state is generic template text that looks the same "
          "for every brand and cannot be edited afterwards."
    )
    return False


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

    # Did the AI actually write anything? A plan with no AI images is boilerplate wearing the
    # brand's colours: the built-in template overlays are identical for every product, which
    # is why a run of failed generations reads to the team as "the tool is mixing up brands".
    # It has to be impossible to mistake that for a finished plan.
    _content = _res.get("content") or {}
    _ai_wrote_nothing = bool(ai_instance) and not (_content.get("images") or [])
    _blocked = ai_instance.hard_failure() if ai_instance else ""
    if _blocked:
        st.session_state["_ai_blocked"] = _blocked      # warn before the next build, not after
        _write_ai_block(_blocked)                        # ...and warn everyone else too
    elif ai_instance and (_content.get("images") or []):
        st.session_state.pop("_ai_blocked", None)        # it works again
        _write_ai_block("")

    if _blocked:
        st.error(
            "⛔ **No AI copy was written. This plan is template boilerplate — do not send it.**\n\n"
            + _blocked
            + "\n\nEvery plan generated until this is fixed will have generic copy that looks "
              "the same for every brand."
        )
    elif _ai_wrote_nothing:
        st.error(
            "⛔ **No AI copy was written. This plan is template boilerplate — do not send it.**\n\n"
            "The AI calls failed for another reason. Open the detail below and send it on."
        )

    if ai_instance:
        u = ai_instance.last_usage
        cost = (u["input"] / 1e6) * 3.0 + (u["cached"] / 1e6) * 0.30 + (u["output"] / 1e6) * 15.0
        _msg = f"Built `{pdf_path.name}` · {kb} KB · {elapsed:.0f}s · ${cost:.2f}" + (
            " · feedback applied" if feedback else "")
        if _blocked or _ai_wrote_nothing:
            st.warning("⚠️ " + _msg + " — TEMPLATE MODE")
        else:
            st.success("✅ " + _msg)
        if ai_instance.errors:
            _exp = bool(_blocked or _ai_wrote_nothing)
            with st.expander(f"⚠️ {len(ai_instance.errors)} AI call(s) failed", expanded=_exp):
                for e in ai_instance.errors[:12]:
                    st.code(e)
    else:
        st.warning(f"⚠️ Built `{pdf_path.name}` · {kb} KB · {elapsed:.0f}s — TEMPLATE MODE, no API key set.")

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
    # Sidecar with the editable plan content, so the team can correct a plan and re-render it
    # without paying for another AI generation.
    #
    # Only save content the editor can actually work with. A run where the AI produced
    # nothing writes a sidecar with empty images, modules and Q&A — which the editor then
    # opens as a plan with nothing in it. That is what "we cannot edit it anymore" was:
    # not a broken editor, an empty file it had been handed.
    if _content.get("images"):
        _save_plan_content(cust.slug, pdf_path.name, _content)
    return pdf_path


def _plan_content_path(slug: str, pdf_name: str) -> Path:
    return BRIEFS_DIR / slug / (pdf_name + ".plan.json")


def _save_plan_content(slug: str, pdf_name: str, content: dict) -> None:
    try:
        _plan_content_path(slug, pdf_name).write_text(
            json.dumps(content, ensure_ascii=False, indent=1), encoding="utf-8")
    except Exception:
        pass


def _load_plan_content(slug: str, pdf_name: str) -> dict:
    p = _plan_content_path(slug, pdf_name)
    if p.exists():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def _plan_editor_ui(slug: str, pdf_name: str, key_prefix: str) -> None:
    """Edit the generated plan — image plan AND A+ Premium — then re-render the PDF.

    No AI call: this re-renders exactly what you typed, then re-runs the compliance and
    copy-length scans so an edit cannot quietly introduce a banned claim or a 40-character
    overlay. Requested by the team: "the full pdf plan image and A+ Premium if possible"."""
    data = _load_plan_content(slug, pdf_name)
    if not data:
        st.caption("✏️ This plan was generated before in-app editing existed — regenerate it once to unlock editing.")
        return
    # A sidecar with no images means the plan was built while the AI was unavailable: the
    # PDF is template boilerplate and there is nothing here worth editing. Say so, rather
    # than opening an editor with three empty tabs — that silence is what the team read as
    # "we cannot edit it anymore".
    if not (data.get("images") or []):
        st.error(
            "⛔ **This plan has no AI content.** It was generated while the AI was "
            "unavailable, so the PDF contains generic template copy and there is nothing to "
            "edit. Generate it again once the AI is working."
        )
        return
    meta = _load_plan_meta(slug, pdf_name)
    upload = meta.get("upload", "")
    if not upload or not Path(upload).exists():
        st.caption("✏️ Editing needs the original SEO sheet, which is no longer on disk for this plan.")
        return

    edited = {"title": data.get("title", ""), "backend": data.get("backend", ""),
              "bullets": list(data.get("bullets") or []),
              "images": [dict(i) for i in (data.get("images") or [])],
              "modules": [dict(m) for m in (data.get("modules") or [])],
              "qa": [dict(q) for q in (data.get("qa") or [])]}

    t_img, t_apl, t_qa = st.tabs(
        [f"🖼️ Images ({len(edited['images'])})",
         f"📄 A+ Premium ({len(edited['modules'])})",
         f"❓ Q&A ({len(edited['qa'])})"])

    with t_img:
        for i, im in enumerate(edited["images"]):
            role = (im.get("role") or "").upper()
            with st.expander(f"Image {i + 1} · {role} — {(im.get('overlay') or '(no overlay)')[:40]}",
                             expanded=False):
                k = f"{key_prefix}_i{i}"
                im["overlay"] = st.text_input("On-image headline (≤30 chars, ≤5 words, no dashes)",
                                              value=im.get("overlay", ""), key=f"{k}_ov")
                im["overlay_sub"] = st.text_input("On-image subline (≤90 chars)",
                                                  value=im.get("overlay_sub", ""), key=f"{k}_sub")
                im["purpose"] = st.text_input("Purpose", value=im.get("purpose", ""), key=f"{k}_pur")
                im["visual"] = st.text_area("What to show (art direction)",
                                            value=im.get("visual", ""), height=150, key=f"{k}_vis")
                c1, c2 = st.columns(2)
                with c1:
                    im["background"] = st.text_input("Background", value=im.get("background", ""), key=f"{k}_bg")
                    im["props"] = [p.strip() for p in st.text_area(
                        "Props (one per line)", value="\n".join(im.get("props") or []),
                        height=90, key=f"{k}_props").splitlines() if p.strip()]
                with c2:
                    im["lighting"] = st.text_input("Lighting", value=im.get("lighting", ""), key=f"{k}_lig")
                    im["graphics"] = [g.strip() for g in st.text_area(
                        "Graphics / icons to build (one per line)",
                        value="\n".join(im.get("graphics") or []), height=90, key=f"{k}_gfx").splitlines() if g.strip()]

    with t_apl:
        for i, mo in enumerate(edited["modules"]):
            with st.expander(f"Module {i + 1} — {(mo.get('headline') or mo.get('name') or '')[:50]}",
                             expanded=False):
                k = f"{key_prefix}_m{i}"
                mo["headline"] = st.text_input("Headline (≤38 chars, no dashes)",
                                               value=mo.get("headline", ""), key=f"{k}_h")
                mo["body"] = st.text_area("Body (HTML allowed: <b>, <br/>)",
                                          value=mo.get("body", ""), height=180, key=f"{k}_b")
                mo["visual"] = st.text_area("Layout / visual direction",
                                            value=mo.get("visual", ""), height=110, key=f"{k}_v")
                mo["alt"] = st.text_input("Alt text", value=mo.get("alt", ""), key=f"{k}_a")

    with t_qa:
        for i, q in enumerate(edited["qa"]):
            k = f"{key_prefix}_q{i}"
            q["q"] = st.text_input(f"Q{i + 1}", value=q.get("q", ""), key=f"{k}_q")
            q["a"] = st.text_area(f"A{i + 1}", value=q.get("a", ""), height=80, key=f"{k}_a")

    st.caption("Re-renders the PDF from exactly what you typed. No AI call, no cost, a few seconds. "
               "Compliance and copy-length are re-checked on the edited text.")
    if st.button("💾 Save edits & re-render PDF", key=f"{key_prefix}_apply", type="primary"):
        try:
            cust = load_customer(slug)
            brief = parse_excel(upload)
            content = PB.plan_from_dict(edited)
            stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            base = pdf_name[:-4] if pdf_name.endswith(".pdf") else pdf_name
            base = re.sub(r"__edit-\d{8}_\d{6}$", "", base)
            out_path = BRIEFS_DIR / slug / f"{base}__edit-{stamp}.pdf"
            _res: dict = {}
            PB.build_brief(cust, brief, out_path, ai=None, result_out=_res,
                           plan_content=content)
            if _res.get("content"):
                _save_plan_content(slug, out_path.name, _res["content"])
            _save_plan_meta(slug, out_path.name, {"upload": upload, "product": brief.product_name or ""})
            warn = _res.get("copy_warnings") or []
            if _res.get("compliance_blocking"):
                st.error("⛔ Your edit introduced a blocking compliance issue — see section 7 of the new PDF.")
            if warn:
                st.warning("⚠️ Copy-length / dash issues in the edit:\n" + "\n".join(f"- {w}" for w in warn[:8]))
            st.session_state["last_plan"] = {"slug": slug, "name": out_path.name}
            st.success(f"Saved as `{out_path.name}` — open it under **Plans & Review**.")
        except Exception as exc:
            st.error(f"Re-render failed: {exc}")


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
        _fb_ok = _ai_preflight()
        if st.button("🔄 New version applying the comments", key=f"{key_prefix}_regen",
                     type="primary", disabled=not _fb_ok):
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
            info = st.text_area("Extra product info / notes", value=existing, height=110, key=f"kn_info_{cust.slug}",
                                placeholder="e.g. new 500 ml size; hero colour teal; certified organic since 2025; avoid 'detox'…")
            kn_imgs = st.file_uploader("Reference images (optional)", type=["png", "jpg", "jpeg", "webp"],
                                       accept_multiple_files=True, key=f"kn_imgs_{cust.slug}")
            if st.button("💾 Save to Brand Memory", key=f"kn_save_{cust.slug}"):
                KN.save_team_info(cust.slug, info)
                n = 0
                for f in (kn_imgs or []):
                    KN.save_team_image(cust.slug, f.name, f.read()); n += 1
                st.success(f"Saved to {cust.name}'s memory" + (f" (+{n} image(s))" if n else "") + ".")
            cur = KN.list_team_images(cust.slug)
            if cur:
                st.caption("Images on file: " + ", ".join(cur))

    # ---- About Us: ask once per brand, then never again ----
    # Without this text the AI would invent a brand story. With it, it gets the real one
    # (e.g. "created by a hospice social worker") — the strongest trust asset there is.
    if not (cust.about_us or "").strip():
        with st.container(border=True):
            st.markdown("##### " + T("about.missing_title", brand=cust.name))
            st.caption(T("about.why"))
            _au = st.text_area(
                T("about.field"),
                height=120, key=f"about_quick_{cust.slug}",
                placeholder=T("about.placeholder",
                              source=cust.website_url or T("about.website_fallback")),
            )
            _c1, _c2 = st.columns([1, 3])
            if _c1.button(T("about.save"), key=f"about_quick_save_{cust.slug}", type="primary"):
                if _au.strip():
                    cust.about_us = _au.strip()
                    save_customer(cust)
                    st.success(T("about.saved"))
                    st.rerun()
                else:
                    st.warning(T("about.empty"))
            _c2.caption(T("about.skip"))

    st.divider()
    st.markdown("#### 1 · Upload the product inputs")
    up_c1, up_c2 = st.columns([1, 1])
    with up_c1:
        upload = st.file_uploader("SEO analysis sheet (.xlsx) *", type=["xlsx"], key=f"seo_up_{cust.slug}")
    with up_c2:
        prod_imgs = st.file_uploader(
            "Product images (optional, several)",
            type=["png", "jpg", "jpeg", "webp"],
            accept_multiple_files=True,
            key=f"prod_imgs_{cust.slug}",
            help="Packshots, existing listing images, lifestyle shots, the packaging. The plan "
                 "references what actually exists instead of describing shots you cannot produce.",
        )
    if not upload:
        st.caption("SEO title + bullets come from the sheet — the tool writes the creative Image + A+ plan. "
                   "Product images are optional but make the plan far more concrete.")
        return

    # Save upload to a tmp working path so the parser (file-based) can read it
    work_dir = BRIEFS_DIR / cust.slug / "_uploads"
    work_dir.mkdir(parents=True, exist_ok=True)
    safe_name = re.sub(r"[^A-Za-z0-9._-]+", "_", upload.name)
    upload_path = work_dir / f"{int(time.time())}__{safe_name}"
    upload_path.write_bytes(upload.read())

    # Product images live beside the sheet they were uploaded with, so a regenerated version
    # picks up the same set. Saved under the plan's own folder, not brand-wide Brand Memory.
    img_dir = work_dir / (upload_path.stem + "__images")
    saved_imgs: list[str] = []
    for f in (prod_imgs or []):
        try:
            img_dir.mkdir(parents=True, exist_ok=True)
            safe = re.sub(r"[^A-Za-z0-9._-]+", "_", f.name)
            (img_dir / safe).write_bytes(f.read())
            saved_imgs.append(safe)
        except Exception as exc:
            st.warning(f"Could not save {f.name}: {exc}")
    if saved_imgs:
        st.caption(f"🖼️ {len(saved_imgs)} product image(s) attached: " + ", ".join(saved_imgs))
        with st.expander("Preview attached images", expanded=False):
            st.image([str(img_dir / n) for n in saved_imgs], width=150)

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

    # ---- Build Variants: mehrere SEO-Tabs = Kind-Varianten unter einem Parent ----
    _tabs = []
    try:
        _tabs = SEOL.list_seo_sheets(upload_path)
    except Exception:
        pass
    if len(_tabs) > 1:
        with st.container(border=True):
            st.markdown("##### " + T("variants.found_title", n=len(_tabs)))
            st.caption(T("variants.each_tab") + T("variants.pick"))
            _picked = []
            for _i, _t in enumerate(_tabs):
                _label = SEOL.variation_label(_t) or _t
                if st.checkbox(f"**{_label}**", value=True, key=f"var_{cust.slug}_{_i}",
                               help=T("variants.tab_help", tab=_t)):
                    _picked.append(_t)
            st.caption(T("variants.selected", n=len(_picked), total=len(_tabs)))
            _ok = _ai_preflight()
            if st.button(T("variants.button", n=len(_picked)), key=f"build_variants_{cust.slug}",
                         type="primary", disabled=(not _picked) or (not _ok)):
                out_dir = BRIEFS_DIR / cust.slug
                out_dir.mkdir(parents=True, exist_ok=True)
                built = []
                for _n, _t in enumerate(_picked, 1):
                    _lab = SEOL.variation_label(_t) or _t
                    st.markdown(f"**{_n}/{len(_picked)} · {_lab}**")
                    try:
                        _s = SEOL.load_seo(upload_path, sheet=_t)
                        _seo_v = (_s.title or None, SEOL.as_bullets_html(_s) or None, _s.backend or None)
                    except Exception as exc:
                        st.error(T("variants.unreadable", tab=_t, error=exc))
                        continue
                    _stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    _slugname = slugify(f"{brief.product_name or 'plan'} {_lab}")[:80]
                    _out = out_dir / f"{cust.slug}__{_slugname}__{_stamp}.pdf"
                    try:
                        _pdf = _build_and_report(cust, brief, _out, _seo_v,
                                                 source_upload=str(upload_path))
                        built.append(_pdf.name)
                    except Exception as exc:
                        st.error(T("variants.failed", label=_lab, error=exc))
                if built:
                    # Keep the whole set, not just the last one. Previously only built[-1]
                    # was handed to the preview, so a five-variant run showed one plan and
                    # the team reported the other four as "not generated".
                    st.session_state["last_plan"] = {"slug": cust.slug, "name": built[-1]}
                    st.session_state["last_variants"] = {"slug": cust.slug, "names": built}
                    st.success(T("variants.done", n=len(built))
                               + T("variants.done_where", brand=cust.name))
                    for _b in built:
                        _bp = out_dir / _b
                        if not _bp.exists():
                            continue
                        with st.expander(f"📄 {_b}  ·  {_bp.stat().st_size // 1024} KB", expanded=False):
                            with _bp.open("rb") as _fh:
                                st.download_button("⬇️ Download", data=_fh.read(),
                                                   file_name=_download_name(cust.slug, _b),
                                                   mime="application/pdf",
                                                   key=f"dl_var_{cust.slug}_{_b}")
        st.divider()

    _gen_ok = _ai_preflight()
    if st.button("Generate PDF", type="primary", disabled=not _gen_ok):
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
            _v = next((x for x in CM.list_plans(last["slug"]) if x["name"] == last["name"]), None)
            _vtxt = (f"  ·  **v{_v['version']}/{_v['versions_total']}**"
                     + T("version.latest" if _v["is_latest"] else "version.older")) if _v else ""
            st.caption(f"`{last['name']}`  ·  {_when(int(p.stat().st_mtime))}{_vtxt}  ·  "
                       f"Status: **{CM.get_status(last['slug'], last['name'])}**")
            _render_pdf_inline(p)
            with p.open("rb") as f:
                st.download_button("⬇️  Download PDF", data=f.read(),
                                   file_name=_download_name(last["slug"], last["name"]),
                                   mime="application/pdf", type="primary", key="dl_last")
            st.markdown("#### ✏️ Edit this plan")
            _plan_editor_ui(last["slug"], last["name"], key_prefix=f"gen_edit_{last['slug']}_{last['name']}")
            st.markdown("#### 💬 Comments")
            _comment_thread_ui(last["slug"], last["name"], key_prefix="gen")


def _backup_zip() -> bytes:
    """Everything the team created, as one ZIP.

    Brands added through the UI and every generated plan live ONLY on the server's data
    volume — they are not in git and nothing else copies them. If that volume is lost,
    so is the work. This is the escape hatch: download it, commit it, keep it somewhere
    that is not the same machine."""
    import io, zipfile
    from tools.brief_app.core.config import DATA_ROOT
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        for folder in ("customers", "briefs", "knowledge", "comments"):
            root = DATA_ROOT / folder
            if not root.exists():
                continue
            for f in root.rglob("*"):
                if f.is_file() and not f.name.startswith("."):
                    try:
                        z.write(f, str(f.relative_to(DATA_ROOT)))
                    except Exception:
                        continue
    return buf.getvalue()


def page_customers() -> None:
    st.title("Customers")
    customers = list_customers()

    # Brands seeded from the repo on this boot — so it is visible that a new brand
    # arrived with a deploy rather than being created by someone in the UI.
    try:
        from tools.brief_app.core.config import SEEDED_ON_BOOT
        if SEEDED_ON_BOOT:
            st.info(T("seed.new") + "**" + "**, **".join(SEEDED_ON_BOOT) + "**")
    except Exception:
        pass

    # Brands whose shipped config differs from the live one. Shown, never applied on its
    # own: most shipped configs carry no timestamp, so "the repo is newer" and "someone
    # edited this in the app" are indistinguishable, and guessing wrong destroys work that
    # exists nowhere else. A person picks, one brand at a time.
    try:
        from tools.brief_app.core.config import repo_config_drift, sync_brand_from_repo
        _drift = repo_config_drift()
    except Exception:
        _drift = []
    if _drift:
        with st.expander(T("drift.title", n=len(_drift)), expanded=False):
            st.caption(T("drift.why"))
            _pick = st.selectbox(T("drift.brand"), _drift, key="drift_pick")
            if st.button(T("drift.apply"), key="drift_apply"):
                if sync_brand_from_repo(_pick):
                    st.success(T("drift.applied", brand=_pick))
                    st.rerun()
                else:
                    st.error(T("drift.failed", brand=_pick))

    with st.expander(T("backup.title"), expanded=False):
        st.caption(T("backup.why"))
        if st.button(T("backup.make"), key="mk_backup"):
            with st.spinner(T("backup.packing")):
                data = _backup_zip()
            st.download_button(
                f"⬇️  equalice-backup ({len(data) // 1024} KB)",
                data=data,
                file_name=f"equalice-plans-backup_{datetime.now():%Y-%m-%d}.zip",
                mime="application/zip",
                type="primary",
                key="dl_backup",
            )

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


_STATUS_ICON = {"open": "🟡", "changes requested": "🔴", "design done": "🎨",
                "approved": "🟢"}


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
        ver = (f"v{plan['version']}/{plan['versions_total']}"
               if plan["versions_total"] > 1 else "v1")
        flag = T("version.flag_latest") if plan["is_latest"] else T("version.flag_old")
        header = (f"{icon}  {flag}  ·  {ver}  ·  {_when(plan['mtime'])}  ·  "
                  f"{plan['name']}  ·  {plan['size_kb']} KB  ·  💬 {plan['comment_count']}")
        with st.expander(header, expanded=False):
            p = Path(plan["path"])
            if not plan["is_latest"]:
                st.warning(T("version.not_latest", v=plan["version"],
                             total=plan["versions_total"]))
            st.caption(f"Status: **{plan['status']}** — {CM.status_help(plan['status'])}")
            _render_pdf_inline(p, height=800)
            with p.open("rb") as f:
                st.download_button("⬇️  Download PDF", data=f.read(),
                                   file_name=_download_name(cust.slug, plan["name"]),
                                   mime="application/pdf", key=f"dl_{plan['name']}")
            st.markdown("#### ✏️ Edit this plan")
            _plan_editor_ui(cust.slug, plan["name"], key_prefix=f"archedit_{plan['name']}")
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

    # Interface language only — the language of a brand's on-image overlays is set per
    # brand on the Customers page, so switching this never changes a client deliverable.
    _codes = list(LANGUAGES.keys())
    _cur = get_ui_language()
    _pick = st.selectbox(
        "🌐 " + T("sidebar.language"), _codes, index=_codes.index(_cur),
        format_func=lambda c: LANGUAGES[c],
    )
    if _pick != _cur:
        set_ui_language(_pick)
        st.rerun()
    st.divider()
    st.caption(f"AI ({AI_MODEL}): {'✓ ready' if (has_api_key() and sdk_available()) else '✗ disabled — set ' + ANTHROPIC_KEY_ENV}")
    st.caption(f"Unsplash key: {'✓ set' if has_unsplash_key() else '✗ missing'}")
    st.caption("Customers + briefs stored under `tools/brief_app/`")

PAGES[page]()
