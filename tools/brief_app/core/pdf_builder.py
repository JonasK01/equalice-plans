"""Unified, brand-parameterized Amazon listing brief PDF builder.

Takes a Customer config + a ParsedBrief, produces a Jotti/SeQR-style branded PDF
with embedded moodboard stock images and a 4-point argumentation block under
every copy element.

Architecture:
    - One BriefBuilder per (customer, brief) pair
    - Pages are built as ReportLab Flowables on a BaseDocTemplate
    - Brand color/font come from the Customer config
"""
from __future__ import annotations
import re as _re
from dataclasses import dataclass
from html import escape as _html_escape
from pathlib import Path
from typing import Optional

from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm, mm
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle,
    Image, PageBreak, KeepTogether, Flowable, NextPageTemplate,
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from .customers import Customer
from .excel_parser import ParsedBrief
from .argumentation import argument_for, Argumentation
from .unsplash import fetch_moodboard, has_unsplash_key, MoodImage
from .ai import BriefAI, AIImagePlanItem, AIModule, AIQA, AIArgumentation, AIComplianceFlag


# ---------- Localization for overlay text ----------

OVERLAY_PHRASES: dict[str, dict[str, str]] = {
    "en": {
        "cold_pressed": "COLD-PRESSED. NEVER REFINED.",
        "one_ingredient": "ONE INGREDIENT. NOTHING ELSE.",
        "seed_to_bottle": "SEED → PRESS → BOTTLE.",
        "head_to_toe": "ONE BOTTLE. HEAD TO TOE.",
        "built_for": "BUILT FOR DAILY USE.",
        "how_to_use": "HOW TO USE — A SIMPLE RITUAL.",
        "trust_stack": "PURE INSIDE. PROTECTED OUTSIDE.",
        "brand_close": "FAMILY-ROOTED. HONESTLY MADE.",
        "two_sizes": "TWO SIZES. ONE STANDARD.",
    },
    "de": {
        "cold_pressed": "KALTGEPRESST. NIE RAFFINIERT.",
        "one_ingredient": "EINE ZUTAT. SONST NICHTS.",
        "seed_to_bottle": "SAAT → PRESSE → FLASCHE.",
        "head_to_toe": "EINE FLASCHE. VON KOPF BIS FUSS.",
        "built_for": "GEMACHT FÜR DEN ALLTAG.",
        "how_to_use": "ANWENDUNG — EIN EINFACHES RITUAL.",
        "trust_stack": "INNEN REIN. AUSSEN GESCHÜTZT.",
        "brand_close": "FAMILIENGEFÜHRT. EHRLICH GEMACHT.",
        "two_sizes": "ZWEI GRÖSSEN. EIN STANDARD.",
    },
    "fr": {
        "cold_pressed": "PRESSÉ À FROID. JAMAIS RAFFINÉ.",
        "one_ingredient": "UN INGRÉDIENT. RIEN D'AUTRE.",
        "seed_to_bottle": "GRAINE → PRESSE → FLACON.",
        "head_to_toe": "UN FLACON. DE LA TÊTE AUX PIEDS.",
        "built_for": "CONÇU POUR UN USAGE QUOTIDIEN.",
        "how_to_use": "MODE D'EMPLOI — UN RITUEL SIMPLE.",
        "trust_stack": "PUR À L'INTÉRIEUR. PROTÉGÉ À L'EXTÉRIEUR.",
        "brand_close": "FAMILIAL. HONNÊTEMENT FABRIQUÉ.",
        "two_sizes": "DEUX TAILLES. UN SEUL STANDARD.",
    },
    "es": {
        "cold_pressed": "PRENSADO EN FRÍO. NUNCA REFINADO.",
        "one_ingredient": "UN INGREDIENTE. NADA MÁS.",
        "seed_to_bottle": "SEMILLA → PRENSA → BOTELLA.",
        "head_to_toe": "UNA BOTELLA. DE PIES A CABEZA.",
        "built_for": "DISEÑADO PARA EL DÍA A DÍA.",
        "how_to_use": "CÓMO USARLO — UN RITUAL SENCILLO.",
        "trust_stack": "PURO POR DENTRO. PROTEGIDO POR FUERA.",
        "brand_close": "DE FAMILIA. HECHO CON HONESTIDAD.",
        "two_sizes": "DOS TAMAÑOS. UN MISMO ESTÁNDAR.",
    },
    "it": {
        "cold_pressed": "SPREMUTO A FREDDO. MAI RAFFINATO.",
        "one_ingredient": "UN INGREDIENTE. NULL'ALTRO.",
        "seed_to_bottle": "SEME → PRESSA → FLACONE.",
        "head_to_toe": "UN FLACONE. DALLA TESTA AI PIEDI.",
        "built_for": "PENSATO PER L'USO QUOTIDIANO.",
        "how_to_use": "COME USARLO — UN RITUALE SEMPLICE.",
        "trust_stack": "PURO DENTRO. PROTETTO FUORI.",
        "brand_close": "DI FAMIGLIA. FATTO ONESTAMENTE.",
        "two_sizes": "DUE FORMATI. UNO STANDARD.",
    },
}


def overlay(key: str, lang: str, fallback: str = "") -> str:
    return OVERLAY_PHRASES.get(lang, {}).get(key) or OVERLAY_PHRASES["en"].get(key, fallback)


# ---------- Brand styling helpers ----------

def _hex(c: str) -> colors.Color:
    try:
        return HexColor(c)
    except Exception:
        return colors.black


@dataclass
class BrandStyle:
    primary: colors.Color
    accent: colors.Color
    text: colors.Color
    bg: colors.Color
    mood_bg: colors.Color
    fonts: list[str]

    @classmethod
    def from_customer(cls, c: Customer) -> "BrandStyle":
        return cls(
            primary=_hex(c.primary_color),
            accent=_hex(c.accent_color),
            text=_hex(c.text_color),
            bg=_hex(c.background_color),
            mood_bg=_hex(c.mood_background_color),
            fonts=c.fonts or ["Inter"],
        )

    @classmethod
    def equalice(cls) -> "BrandStyle":
        """EQUALICE (the agency) brand — drives the DELIVERABLE look & feel.
        The client brand is used separately for the brand sheet + image specs.
        Source: EQUALICE-Brand-Assets.html."""
        return cls(
            primary=_hex("#0F1115"),     # Ink — headings, top chrome
            accent=_hex("#FA7C04"),      # Orange — accents, labels, rules, bottom chrome
            text=_hex("#1F232B"),        # near-ink body
            bg=_hex("#FAF7F2"),          # Cream — cover background
            mood_bg=_hex("#FFF4E8"),     # Orange tint — highlight boxes
            fonts=["Geist"],
        )


# ---------- Flowables ----------

def _layout_hints() -> dict[str, str]:
    """One-line description per composition archetype, printed on the design card so the
    designer does not have to look the name up. Sourced from ai.LAYOUT_ARCHETYPES."""
    try:
        from .ai import LAYOUT_ARCHETYPES
        return dict(LAYOUT_ARCHETYPES)
    except Exception:
        return {}


_LAYOUT_HINTS = _layout_hints()


def _clip(s: object, limit: int) -> str:
    """Trim to `limit` characters on a word boundary, with an ellipsis if anything was cut."""
    t = " ".join(str(s or "").split())
    if len(t) <= limit:
        return t
    cut = t[:limit].rsplit(" ", 1)[0].rstrip(" ,;:.")
    return (cut or t[:limit]) + "…"


def _sentences(s: object, n: int) -> str:
    """Keep the first `n` sentences of a flowing description.

    The design cards were carrying full paragraphs of shot description. The AI is now asked
    for two sentences, but hand-written run.py plans predate that instruction and flow
    through the same renderer, so the trim happens here too.

    DELIBERATELY EXEMPT: text that is laid out in blocks (a blank line anywhere) is not
    prose, it is structure — above all the main image's Option A / B / C split test, which
    the team asked for by name. Trimming that to two sentences would silently throw away
    two of the three options. Structure is kept whole; only run-on prose is cut."""
    raw = str(s or "")
    if not raw.strip():
        return ""
    if "\n\n" in raw or _re.search(r"OPTION\s+[A-C]\b", raw):
        return raw.strip()
    t = " ".join(raw.split())
    parts = _re.split(r"(?<=[.!?])\s+", t)
    kept = " ".join(parts[:n]).strip()
    return kept if kept else _clip(t, 220)


def _esc(s: object) -> str:
    """HTML-escape user text before passing to a Paragraph.
    Normalise any already-escaped '&amp;' back to '&' first, so a field that was
    written with '&amp;' does NOT double-escape into a literal '&amp;' on the page.
    (These _esc'd fields — overlays, art-direction, module headlines — always want a
    real '&'; raw-HTML fields like bullets/module body are rendered without _esc.)"""
    return _html_escape(str(s or "").replace("&amp;", "&"), quote=False)


class ColorBlock(Flowable):
    def __init__(self, width, height, color):
        super().__init__()
        self.width = width
        self.height = height
        self.color = color

    def wrap(self, availWidth, availHeight):
        return self.width, self.height

    def draw(self):
        self.canv.setFillColor(self.color)
        self.canv.rect(0, 0, self.width, self.height, stroke=0, fill=1)


class MoodTile(Flowable):
    """One moodboard tile: image (or placeholder) + caption."""

    def __init__(self, width, height, mood: MoodImage, caption: str, brand: BrandStyle):
        super().__init__()
        self.width = width
        self.height = height
        self.mood = mood
        self.caption = caption
        self.brand = brand

    def wrap(self, availWidth, availHeight):
        return self.width, self.height

    def draw(self):
        c = self.canv
        # With no Unsplash key the placeholder already prints the search prompt inside the tile,
        # so the caption underneath repeated the identical string. Drop the caption band in that
        # case: it was duplicated text AND wasted vertical space on every moodboard.
        has_image = bool(self.mood.file_path)
        cap_h = 1.3 * cm if has_image else 0.25 * cm
        img_h = self.height - cap_h
        # frame
        c.setStrokeColor(self.brand.accent)
        c.setLineWidth(0.5)
        c.rect(0, cap_h, self.width, img_h, stroke=1, fill=0)
        # image or placeholder
        if self.mood.file_path:
            try:
                c.drawImage(
                    str(self.mood.file_path),
                    1, cap_h + 1,
                    width=self.width - 2,
                    height=img_h - 2,
                    preserveAspectRatio=True,
                    anchor="c",
                    mask="auto",
                )
            except Exception:
                self._placeholder(c, img_h, cap_h)
        else:
            self._placeholder(c, img_h, cap_h)
        # caption — only when a real image is shown (the placeholder carries its own label)
        if has_image:
            c.setFillColor(self.brand.text)
            c.setFont("Helvetica-Bold", 8)
            c.drawString(0, 0.7 * cm, self._trunc(self.caption, 70))
        if has_image and self.mood.photographer:
            c.setFillColor(self.brand.accent)
            c.setFont("Helvetica", 6.5)
            c.drawString(0, 0.2 * cm, f"Photo: {self.mood.photographer} / Unsplash")

    def _placeholder(self, c, img_h, cap_h=None):
        cap_h = 1.3 * cm if cap_h is None else cap_h
        c.setFillColor(self.brand.mood_bg)
        c.rect(1, cap_h + 1, self.width - 2, img_h - 2, stroke=0, fill=1)
        c.setFillColor(self.brand.accent)
        c.setFont("Helvetica-Oblique", 8)
        # word-wrap the search prompt manually
        prompt = f'"{self.mood.query}"'
        words = prompt.split()
        line = ""
        y = cap_h + img_h / 2 + 1 * cm
        for w in words:
            test = (line + " " + w).strip()
            if c.stringWidth(test, "Helvetica-Oblique", 8) > self.width - 10:
                c.drawString(5, y, line)
                y -= 10
                line = w
            else:
                line = test
        if line:
            c.drawString(5, y, line)
        c.setFont("Helvetica", 6.5)
        c.setFillColor(self.brand.accent)
        c.drawCentredString(self.width / 2, 1.5 * cm + 10, "(Unsplash search prompt — add API key for real images)")

    def _trunc(self, s, n):
        return s if len(s) <= n else s[: n - 1] + "…"


# ---------- Builder ----------

class BriefBuilder:
    def __init__(
        self,
        customer: Customer,
        brief: ParsedBrief,
        output_path: Path,
        ai: Optional[BriefAI] = None,
        progress_cb=None,
    ):
        self.customer = customer
        self.brief = brief
        self.output_path = Path(output_path)
        # Two brands: EQUALICE styles the DELIVERABLE; the client brand is used for the
        # brand-sheet swatches and is referenced in the image specs.
        self.brand = BrandStyle.equalice()
        self.client_brand = BrandStyle.from_customer(customer)
        self.lang = customer.overlay_language or "en"
        self.styles = self._build_styles()
        self.story: list = []
        self._moodboard_cache: Optional[list[MoodImage]] = None
        self.ai = ai if (ai and ai.enabled) else None
        self.progress_cb = progress_cb or (lambda pct, msg: None)
        # Override-able label for the cover. None = auto (Sonnet 4.6 / template fallback).
        # Set to a custom string (e.g. "Hand-written senior copy") when the AI fields are
        # populated manually instead of via Claude.
        self.copy_source_label: Optional[str] = None
        # Optional per-product moodboard search terms, overriding the brand-level ones.
        # For multi-line brands whose brand terms only describe one product line.
        self.moodboard_terms: Optional[list[str]] = None
        # AI outputs are populated up-front in build() so each section can use them
        self._ai_title: Optional[str] = None
        self._ai_bullets: Optional[list[str]] = None
        self._ai_images: Optional[list[AIImagePlanItem]] = None
        self._ai_modules: Optional[list[AIModule]] = None
        self._ai_qa: Optional[list[AIQA]] = None
        self._ai_backend: Optional[str] = None
        self._ai_compliance: Optional[list[AIComplianceFlag]] = None
        self._compliance_blocking: bool = False
        self._copy_warnings: list[str] = []
        self._ai_arg_cache: dict[str, AIArgumentation] = {}

    # ----- styles -----
    def _build_styles(self) -> dict[str, ParagraphStyle]:
        base = getSampleStyleSheet()
        s: dict[str, ParagraphStyle] = {}
        s["title"] = ParagraphStyle(
            "title", parent=base["Title"], fontName="Helvetica-Bold",
            fontSize=32, leading=36, textColor=self.brand.primary, spaceAfter=10,
            alignment=1,  # center
        )
        s["subtitle"] = ParagraphStyle(
            "subtitle", parent=base["Heading2"], fontName="Helvetica",
            fontSize=13, leading=17, textColor=self.brand.text, spaceAfter=6,
            alignment=1,  # center
        )
        s["cover_product"] = ParagraphStyle(
            "cover_product", parent=base["Heading1"], fontName="Helvetica-Bold",
            fontSize=16, leading=20, textColor=self.brand.accent, spaceAfter=6,
            alignment=1,
        )
        s["cover_meta"] = ParagraphStyle(
            "cover_meta", parent=base["BodyText"], fontName="Helvetica",
            fontSize=10, leading=14, textColor=self.brand.text, spaceAfter=4,
            alignment=1,
        )
        s["h1"] = ParagraphStyle(
            "h1", parent=base["Heading1"], fontName="Helvetica-Bold",
            fontSize=18, leading=22, textColor=self.brand.primary, spaceBefore=10, spaceAfter=8,
        )
        s["h2"] = ParagraphStyle(
            "h2", parent=base["Heading2"], fontName="Helvetica-Bold",
            fontSize=13, leading=17, textColor=self.brand.accent, spaceBefore=8, spaceAfter=4,
        )
        s["h3"] = ParagraphStyle(
            "h3", parent=base["Heading3"], fontName="Helvetica-Bold",
            fontSize=11, leading=14, textColor=self.brand.text, spaceBefore=6, spaceAfter=3,
        )
        s["body"] = ParagraphStyle(
            "body", parent=base["BodyText"], fontName="Helvetica",
            fontSize=9.5, leading=13, textColor=self.brand.text, spaceAfter=4,
        )
        s["body_small"] = ParagraphStyle(
            "body_small", parent=base["BodyText"], fontName="Helvetica",
            fontSize=8.5, leading=11.5, textColor=self.brand.text, spaceAfter=2,
        )
        s["overlay"] = ParagraphStyle(
            "overlay", parent=base["BodyText"], fontName="Helvetica-Bold",
            fontSize=12, leading=14, textColor=self.brand.primary, spaceAfter=2,
        )
        s["overlay_sub"] = ParagraphStyle(
            "overlay_sub", parent=base["BodyText"], fontName="Helvetica-Oblique",
            fontSize=9, leading=12, textColor=self.brand.text, spaceAfter=4,
        )
        s["arg_label"] = ParagraphStyle(
            "arg_label", parent=base["BodyText"], fontName="Helvetica-Bold",
            fontSize=7.5, leading=10, textColor=self.brand.accent, spaceAfter=0,
        )
        s["arg_value"] = ParagraphStyle(
            "arg_value", parent=base["BodyText"], fontName="Helvetica",
            fontSize=7.5, leading=10, textColor=self.brand.text, spaceAfter=2,
        )
        s["caption"] = ParagraphStyle(
            "caption", parent=base["BodyText"], fontName="Helvetica-Oblique",
            fontSize=7.5, leading=10, textColor=self.brand.accent, spaceAfter=2,
        )
        s["mono"] = ParagraphStyle(
            "mono", parent=base["BodyText"], fontName="Courier",
            fontSize=8, leading=11, textColor=self.brand.text, spaceAfter=2,
        )
        # ---- section header (orange chip + ink title) ----
        s["sec_num"] = ParagraphStyle(
            "sec_num", parent=base["BodyText"], fontName="Helvetica-Bold",
            fontSize=15, leading=17, textColor=colors.white, alignment=1, spaceAfter=0,
        )
        s["sec_title"] = ParagraphStyle(
            "sec_title", parent=base["Heading1"], fontName="Helvetica-Bold",
            fontSize=17, leading=20, textColor=self.brand.primary, spaceBefore=0, spaceAfter=0,
        )
        # ---- EQUALICE deliverable identity ----
        s["eq_wordmark"] = ParagraphStyle(
            "eq_wordmark", parent=base["Title"], fontName="Helvetica-Bold",
            fontSize=30, leading=32, textColor=self.brand.primary, spaceAfter=4,
            alignment=1,
        )
        s["eq_kicker"] = ParagraphStyle(
            "eq_kicker", parent=base["BodyText"], fontName="Helvetica-Bold",
            fontSize=10, leading=13, textColor=self.brand.accent, spaceAfter=0,
            alignment=1,
        )
        # ---- design-team layout (storyboard + compact cards) ----
        s["card_head"] = ParagraphStyle(
            "card_head", parent=base["Heading2"], fontName="Helvetica-Bold",
            fontSize=13, leading=15, textColor=self.brand.primary, spaceAfter=0,
        )
        s["card_purpose"] = ParagraphStyle(
            "card_purpose", parent=base["BodyText"], fontName="Helvetica-Oblique",
            fontSize=8.5, leading=11, textColor=self.brand.accent, spaceAfter=0, alignment=2,  # right
        )
        s["zone_label"] = ParagraphStyle(
            "zone_label", parent=base["BodyText"], fontName="Helvetica-Bold",
            fontSize=7.5, leading=10, textColor=self.brand.accent, spaceBefore=4, spaceAfter=1,
        )
        s["onimg"] = ParagraphStyle(
            "onimg", parent=base["BodyText"], fontName="Helvetica-Bold",
            fontSize=12.5, leading=15, textColor=self.brand.primary, spaceAfter=1,
        )
        s["onimg_sub"] = ParagraphStyle(
            "onimg_sub", parent=base["BodyText"], fontName="Helvetica-Oblique",
            fontSize=9, leading=12, textColor=self.brand.text, spaceAfter=0,
        )
        s["why_line"] = ParagraphStyle(
            "why_line", parent=base["BodyText"], fontName="Helvetica-Oblique",
            fontSize=8, leading=11, textColor=colors.HexColor("#8A8A8A"), spaceBefore=3, spaceAfter=0,
        )
        s["sb_num"] = ParagraphStyle(
            "sb_num", parent=base["BodyText"], fontName="Helvetica-Bold",
            fontSize=15, leading=17, textColor=self.brand.primary, spaceAfter=0,
        )
        s["sb_role"] = ParagraphStyle(
            "sb_role", parent=base["BodyText"], fontName="Helvetica-Bold",
            fontSize=8, leading=10, textColor=self.brand.accent, spaceAfter=1,
        )
        s["sb_body"] = ParagraphStyle(
            "sb_body", parent=base["BodyText"], fontName="Helvetica",
            fontSize=8, leading=10.5, textColor=self.brand.text, spaceAfter=1,
        )
        s["sb_text"] = ParagraphStyle(
            "sb_text", parent=base["BodyText"], fontName="Helvetica-Bold",
            fontSize=8, leading=10.5, textColor=self.brand.primary, spaceAfter=0,
        )
        return s

    # ----- page templates -----
    def _make_doc(self) -> BaseDocTemplate:
        doc = BaseDocTemplate(
            str(self.output_path),
            pagesize=A4,
            leftMargin=1.7 * cm, rightMargin=1.7 * cm,
            topMargin=2.0 * cm, bottomMargin=2.0 * cm,
            title=f"{self.customer.name} — {self.brief.product_name or 'Listing Brief'}",
            author=f"{self.customer.name} Listing System",
        )
        frame = Frame(doc.leftMargin, doc.bottomMargin,
                      doc.width, doc.height, id="normal",
                      leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        cover_frame = Frame(0, 0, A4[0], A4[1], id="cover",
                            leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        doc.addPageTemplates([
            PageTemplate(id="cover", frames=[cover_frame], onPage=self._cover_bg),
            PageTemplate(id="normal", frames=[frame], onPage=self._page_chrome),
        ])
        return doc

    def _cover_bg(self, canvas, doc):
        canvas.setFillColor(self.brand.bg)
        canvas.rect(0, 0, A4[0], A4[1], stroke=0, fill=1)
        # accent stripe
        canvas.setFillColor(self.brand.primary)
        canvas.rect(0, 0, A4[0], 1.4 * cm, stroke=0, fill=1)
        canvas.setFillColor(self.brand.accent)
        canvas.rect(0, A4[1] - 1.4 * cm, A4[0], 1.4 * cm, stroke=0, fill=1)

    def _page_chrome(self, canvas, doc):
        canvas.setFillColor(self.brand.primary)
        canvas.rect(0, A4[1] - 0.45 * cm, A4[0], 0.45 * cm, stroke=0, fill=1)
        canvas.setFillColor(self.brand.accent)
        canvas.rect(0, 0, A4[0], 0.35 * cm, stroke=0, fill=1)
        # footer
        canvas.setFillColor(self.brand.text)
        canvas.setFont("Helvetica", 7.5)
        # Brand and product are often the same string (e.g. "The Death Deck"), which printed
        # the name twice in every footer. Only add the product when it says something new.
        prod = (self.brief.product_name or "")[:80].strip()
        brand = (self.customer.name or "").strip()
        parts = [brand] + ([prod] if prod and prod.lower() != brand.lower() else [])
        footer = " · ".join(p for p in parts if p) + f" · p.{doc.page - 1}"
        canvas.drawString(1.5 * cm, 0.55 * cm, footer)
        canvas.drawRightString(A4[0] - 1.5 * cm, 0.55 * cm, f"Marketplace: {self.customer.marketplace}")

    # ----- argumentation block -----
    def _arg_block(self, role: str, text: str, ctr_override: str = "", cvr_override: str = "") -> Flowable:
        # Prefer AI-generated argumentation; fall back to template if AI off/failed
        ai_arg = self._ai_arg(role, text) if self.ai else None
        if ai_arg:
            ctr, cvr, keywords, reviews = ai_arg.ctr, ai_arg.cvr, ai_arg.keywords, ai_arg.reviews
        else:
            template = argument_for(role, text, self.brief)
            ctr, cvr, keywords, reviews = template.ctr, template.cvr, template.keywords, template.reviews
        # Hand-written per-image CTR/CVR (from run.py) always wins over template/AI.
        if ctr_override:
            ctr = ctr_override
        if cvr_override:
            cvr = cvr_override
        rows = [
            [Paragraph("CTR", self.styles["arg_label"]), Paragraph(_esc(ctr), self.styles["arg_value"])],
            [Paragraph("CVR", self.styles["arg_label"]), Paragraph(_esc(cvr), self.styles["arg_value"])],
            [Paragraph("Keywords", self.styles["arg_label"]), Paragraph(_esc(", ".join(keywords) or "—"), self.styles["arg_value"])],
            [Paragraph("Reviews", self.styles["arg_label"]), Paragraph(_esc(reviews), self.styles["arg_value"])],
        ]
        t = Table(rows, colWidths=[2.0 * cm, 15.0 * cm])
        t.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), self.brand.mood_bg),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 5),
            ("RIGHTPADDING", (0, 0), (-1, -1), 5),
            ("TOPPADDING", (0, 0), (-1, -1), 3),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ("BOX", (0, 0), (-1, -1), 0.4, self.brand.accent),
        ]))
        return t

    # ----- sections -----
    def _run_ai_pipeline(self) -> None:
        """Run all AI generations up-front. Each method falls back to None on error
        and the render sections detect None and use template fallback."""
        if not self.ai:
            self.progress_cb(45, "Rendering PDF with template copy (AI disabled)…")
            return

        # SEO copy (title / bullets / backend) is the SEO team's job — if it was pre-set
        # (e.g. loaded from the SEO sheet), the AI must NOT overwrite it. The AI only writes
        # the CREATIVE Image plan + A+ modules + Q&A. Each step is skipped when already filled.
        def _set(attr, gen):
            if getattr(self, attr) is None:
                setattr(self, attr, gen())

        # Primer: run ONE generation first so it writes the prompt cache; every later call
        # then reads that cache at ~10% cost. The image plan is the anchor.
        self.progress_cb(20, "Designing 7 listing images…")
        _set("_ai_images", self.ai.generate_image_plan)

        # The remaining generations are independent of each other → run them CONCURRENTLY
        # (they all hit the warm cache). SEO-sourced fields (title/bullets/backend) are skipped
        # when already filled. Cuts wall-clock roughly in half without losing cache savings.
        import concurrent.futures as _cf
        parallel = {
            "_ai_title": self.ai.generate_title,
            "_ai_bullets": self.ai.generate_bullets,
            "_ai_modules": self.ai.generate_aplus_modules,
            "_ai_qa": self.ai.generate_qa,
            "_ai_backend": self.ai.generate_backend_keywords,
        }
        pending = {a: g for a, g in parallel.items() if getattr(self, a) is None}
        self.progress_cb(40, "Writing bullets · A+ modules · Q&A · backend (in parallel)…")
        if pending:
            with _cf.ThreadPoolExecutor(max_workers=len(pending)) as ex:
                futs = {ex.submit(g): a for a, g in pending.items()}
                for f in _cf.as_completed(futs):
                    attr = futs[f]
                    try:
                        setattr(self, attr, f.result())
                    except Exception:
                        pass  # leave None → render falls back to template for that section

        # Quality-over-speed: an elite second copywriting pass over the on-image overlays and
        # A+ headlines (the most visible marketing surface), informed by the full Brand Memory.
        self.progress_cb(68, "Elevating copy to top marketing quality…")
        try:
            self._ai_images, self._ai_modules = self.ai.elevate_copy(self._ai_images, self._ai_modules)
        except Exception:
            pass

        self.progress_cb(75, "Scanning copy for compliance issues…")
        scan_text = (self._ai_title or "") + "\n" + "\n".join(self._ai_bullets or [])
        self._ai_compliance = self.ai.compliance_scan(scan_text) if scan_text.strip() else []

    def build(self) -> Path:
        self.progress_cb(5, f"Applying brand: {self.customer.name}…")
        self._run_ai_pipeline()
        # Durable house rules (Jonas): new brands drop the Comparison module, and the Q&A
        # module closes with a "From the Brand" cool statement. Applied BEFORE the scans so
        # the brand line is compliance/copy-length checked too.
        self._apply_brand_module_rules()
        # Final QA — automatic for every build: deterministic compliance scan over ALL
        # customer-facing copy (title, bullets, image overlays, A+ modules, Q&A).
        from . import qa as _qa
        if not self.ai:
            self._ai_compliance = _qa.compliance_scan(self._gather_copy_texts())
            self._compliance_blocking = _qa.has_blocking(self._ai_compliance)
        # Copy-length lint — keep on-image overlays/headlines punchy (runs every build).
        self._copy_warnings = _qa.lint_copy(
            self._draft_title(), self._draft_bullets(), self._ai_images, self._ai_modules,
            qa=self._ai_qa)
        self.progress_cb(85, "Composing PDF…")

        self._cover()
        self._at_a_glance()
        self._brandbook()
        self._buyer_psychology()
        self._moodboard()
        self._image_plan()
        self._aplus_modules()
        self._master_copy()
        self._compliance_and_handoff()
        self._ctr_cvr_recap()

        self.progress_cb(95, "Rendering PDF…")
        doc = self._make_doc()
        doc.build(self.story)

        # Feed this plan's composition decisions back into the brand's visual system, so the
        # NEXT plan for this brand is built to look like this one. Only after a successful
        # render: a plan that failed to build is not a house style. Never fatal — a memory
        # write must not lose a finished PDF.
        try:
            from . import knowledge as _kn
            _kn.record_plan_visuals(self.customer.slug, self.brief.product_name, self._ai_images)
        except Exception:
            pass

        self.progress_cb(100, "Done")
        if self._compliance_blocking:
            n = len([f for f in (self._ai_compliance or []) if f.severity == "high"])
            print(f"  ⚠ COMPLIANCE: {n} blocking violation(s) — see section 7 of the brief. Fix before publishing.")
        else:
            print("  ✓ COMPLIANCE: passed (no blocking violations).")
        if self._copy_warnings:
            print(f"  ⚠ COPY LENGTH: {len(self._copy_warnings)} item(s) too long — keep on-image overlays ≤30ch/≤5 words:")
            for w in self._copy_warnings:
                print(f"      · {w}")
        else:
            print("  ✓ COPY LENGTHS: punchy (overlays ≤30ch/≤5 words, headlines short).")
        return self.output_path

    def build_line(self, line_title: str, variants: list, shared_modules: list) -> Path:
        """Build ONE document for a product LINE: cover + brand sheet + one
        product-SPECIFIC image-plan section per variant + ONE shared A+ Premium.
        variants: list of {"label": str, "images": list[AIImagePlanItem]}.
        shared_modules: list[AIModule] rendered once as the shared A+."""
        from . import qa as _qa
        self.brief.product_name = line_title
        self.brief.asin = ""
        # QA over EVERYTHING (all variants' overlays + the shared A+).
        all_images = [im for v in variants for im in v["images"]]
        texts: list[str] = []
        for im in all_images:
            texts += [getattr(im, "overlay", ""), getattr(im, "overlay_sub", "")]
        for m in shared_modules:
            texts += [getattr(m, "headline", ""), getattr(m, "body", "")]
        self._ai_compliance = _qa.compliance_scan([t for t in texts if t])
        self._compliance_blocking = _qa.has_blocking(self._ai_compliance)
        self._copy_warnings = _qa.lint_copy("", [], all_images, shared_modules)

        self._cover()
        self._brandbook()
        # one product-specific image plan per variant
        for v in variants:
            self._ai_images = v["images"]
            images = self._build_image_plan()
            self.story.append(Paragraph(_esc(v["label"]), self.styles["h1"]))
            self.story.append(Paragraph(
                f"Format: 2000 × 2000 px · sRGB · JPG · Overlay text in <b>{self.lang.upper()}</b> · marketplace <b>{_esc(self.customer.marketplace)}</b>",
                self.styles["caption"]))
            self.story.append(Spacer(1, 0.25 * cm))
            self._storyboard(images)
            for i, img in enumerate(images, 1):
                self._render_image_card(i, img)
            self.story.append(PageBreak())
        # ONE shared A+ Premium for the whole line
        self._ai_modules = shared_modules
        self._aplus_modules()
        self._compliance_and_handoff()

        doc = self._make_doc()
        doc.build(self.story)
        if self._compliance_blocking:
            n = len([f for f in (self._ai_compliance or []) if f.severity == "high"])
            print(f"  ⚠ COMPLIANCE: {n} blocking violation(s) — see the compliance section. Fix before publishing.")
        else:
            print("  ✓ COMPLIANCE: passed (no blocking violations).")
        if self._copy_warnings:
            print(f"  ⚠ COPY LENGTH: {len(self._copy_warnings)} item(s) too long — keep on-image overlays ≤30ch/≤5 words:")
            for w in self._copy_warnings:
                print(f"      · {w}")
        else:
            print("  ✓ COPY LENGTHS: punchy (overlays ≤30ch/≤5 words, headlines short).")
        return self.output_path

    def _ai_arg(self, role: str, text: str) -> Optional[AIArgumentation]:
        """Lazy AI argumentation with per-text caching (don't pay twice for same line)."""
        if not self.ai or not text:
            return None
        key = f"{role}::{text[:100]}"
        if key in self._ai_arg_cache:
            return self._ai_arg_cache[key]
        result = self.ai.generate_argumentation(role, text)
        if result:
            self._ai_arg_cache[key] = result
        return result

    # ---- cover ----
    def _cover(self) -> None:
        st = self.story
        st.append(Spacer(1, 3.2 * cm))
        # EQUALICE wordmark — this is an EQUALICE deliverable
        st.append(Paragraph("EQUALICE", self.styles["eq_wordmark"]))
        st.append(Paragraph("AMAZON IMAGE PLAN &amp; A+ BRIEF", self.styles["eq_kicker"]))
        st.append(Spacer(1, 2.0 * cm))
        # client logo if present
        logo = self.customer.logo_path
        if logo:
            if Path(logo).is_absolute():
                logo_path = Path(logo)
            else:
                # logo_path is stored relative to tools/brief_app (see customers.save_logo),
                # i.e. "customers/<slug>/logo.png" — resolve it against that same base.
                # Fall back to the project root for any legacy/hand-written path.
                from .config import CUSTOMERS_DIR
                candidates = [
                    (CUSTOMERS_DIR.parent / logo),
                    (Path(__file__).resolve().parent.parent.parent.parent / logo),
                ]
                logo_path = next((c.resolve() for c in candidates if c.exists()), candidates[0].resolve())
            if logo_path.exists():
                try:
                    st.append(Image(str(logo_path), width=3.2 * cm, height=3.2 * cm, kind="proportional"))
                    st.append(Spacer(1, 0.5 * cm))
                except Exception:
                    pass
        st.append(Paragraph(_esc(self.customer.name.upper()), self.styles["title"]))
        st.append(Paragraph(_esc(self.customer.tagline or "Amazon Listing Brief"), self.styles["subtitle"]))
        st.append(Spacer(1, 1.8 * cm))
        st.append(Paragraph(_esc(self.brief.product_name or "(product name missing)"), self.styles["cover_product"]))
        if self.brief.asin:
            st.append(Paragraph(_esc(f"ASIN: {self.brief.asin}  ·  {self.customer.marketplace}"), self.styles["cover_meta"]))
        st.append(Spacer(1, 5.5 * cm))
        src = self.copy_source_label or ("Claude" if self.ai else "Hand-written senior copy")
        st.append(Paragraph(
            f"Brand Sheet  ·  Image Plan  ·  A+ Premium  ·  Master Copy  ·  QA<br/>"
            f"Overlay language: <b>{_esc(self.lang.upper())}</b>  ·  Marketplace: <b>{_esc(self.customer.marketplace)}</b><br/>"
            f"Prepared by <b>EQUALICE</b> · Beyond Performance. Your Amazon Partner.",
            self.styles["cover_meta"],
        ))
        st.append(NextPageTemplate("normal"))
        st.append(PageBreak())

    # ---- at a glance ----
    def _at_a_glance(self) -> None:
        st = self.story
        self._section_header("", "At a Glance")
        # Brand / Product / ASIN / Marketplace / Overlay language are already on the cover, and
        # Voice / Personality are the first thing in the Brand Sheet. Repeating them here cost a
        # third of the page and taught the reader that this document repeats itself. Only the
        # rows that appear nowhere else survive.
        counts = (f"{len(self.brief.usps)} USPs · {len(self.brief.all_keywords)} keywords · "
                  f"{len(self.brief.rufus_qa)} Q&A · {len(self.brief.good_reviews)} good / "
                  f"{len(self.brief.bad_reviews)} bad reviews")
        rows = [
            ["Target group", Paragraph(_esc(self.brief.target_group[:400] or "—"), self.styles["body_small"])],
            ["Target problems", Paragraph(_esc(self.brief.target_problems[:400] or "—"), self.styles["body_small"])],
            ["Source data", Paragraph(_esc(counts), self.styles["body_small"])],
        ]
        if self.brief.listing_url:
            rows.append(["Listing", Paragraph(_esc(self.brief.listing_url), self.styles["body_small"])])
        t = Table(rows, colWidths=[3.4 * cm, 13.6 * cm])
        t.setStyle(self._kv_style())
        st.append(t)
        if self.brief.ctr_notes or self.brief.cvr_notes:
            st.append(Spacer(1, 0.35 * cm))
            st.append(Paragraph("Briefing notes from the SEO sheet", self.styles["h3"]))
            note_rows = []
            if self.brief.ctr_notes:
                note_rows.append(["CTR", Paragraph("<br/>".join("• " + _esc(n) for n in self.brief.ctr_notes[:5]),
                                                   self.styles["body_small"])])
            if self.brief.cvr_notes:
                note_rows.append(["CVR", Paragraph("<br/>".join("• " + _esc(n) for n in self.brief.cvr_notes[:5]),
                                                   self.styles["body_small"])])
            nt = Table(note_rows, colWidths=[3.4 * cm, 13.6 * cm])
            nt.setStyle(self._kv_style())
            st.append(nt)
        self._section_gap()

    def _section_header(self, num: str, title: str, subtitle: str = "") -> None:
        """EQUALICE section header: orange number chip + ink title + hairline rule.

        Sections used to open with a bare bold line, so every section looked like every
        paragraph and the document had no visible skeleton ("der Aufbau ist schwer zu lesen").
        One consistent header makes the structure scannable at a glance."""
        st = self.story
        full = A4[0] - 1.7 * cm * 2
        chip = ""
        if num:
            chip = Table([[Paragraph(_esc(num), self.styles["sec_num"])]],
                         colWidths=[0.95 * cm], rowHeights=[0.95 * cm])
            chip.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, -1), self.brand.accent),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]))
        head = Table([[chip, Paragraph(_esc(title), self.styles["sec_title"])]],
                     colWidths=[1.35 * cm if num else 0.01 * cm, full - (1.35 * cm if num else 0.01 * cm)])
        head.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ("LINEBELOW", (0, 0), (-1, -1), 1.2, self.brand.primary),
        ]))
        st.append(head)
        if subtitle:
            st.append(Spacer(1, 0.12 * cm))
            st.append(Paragraph(_esc(subtitle), self.styles["caption"]))
        st.append(Spacer(1, 0.28 * cm))

    def _section_gap(self) -> None:
        """Separator between two short sections that now SHARE a page.

        Team feedback (test phase): "zu viele Seiten". Roughly a quarter of the old 20 pages
        were spill — a section overflowing by a few centimetres onto an otherwise blank page,
        because every section ended in a hard PageBreak. Short sections now flow, separated by
        a rule instead of a break; only the big ones (image plan, A+) still start fresh."""
        self.story.append(Spacer(1, 0.45 * cm))
        rule = Table([[""]], colWidths=[A4[0] - 1.7 * cm * 2], rowHeights=[0.02 * cm])
        rule.setStyle(TableStyle([
            ("LINEBELOW", (0, 0), (-1, -1), 0.6, self.brand.accent),
            ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ]))
        self.story.append(rule)
        self.story.append(Spacer(1, 0.45 * cm))

    def _kv_style(self) -> TableStyle:
        return TableStyle([
            ("BACKGROUND", (0, 0), (0, -1), self.brand.mood_bg),
            ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 9),
            ("TEXTCOLOR", (0, 0), (-1, -1), self.brand.text),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 6),
            ("RIGHTPADDING", (0, 0), (-1, -1), 6),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ("BOX", (0, 0), (-1, -1), 0.4, self.brand.accent),
            ("INNERGRID", (0, 0), (-1, -1), 0.2, self.brand.accent),
        ])

    # ---- brandbook ----
    def _brandbook(self) -> None:
        st = self.story
        self._section_header("1", f"Brand Sheet — {self.customer.name}",
                            "Read this first. Everything below is the client's brand. "
                            "Use it for every image in this plan.")
        # Identity
        st.append(Paragraph("Identity", self.styles["h2"]))
        st.append(Paragraph(f"<b>Brand:</b> {_esc(self.customer.name)}", self.styles["body"]))
        if self.customer.tagline:
            st.append(Paragraph(f"<b>Tagline:</b> {_esc(self.customer.tagline)}", self.styles["body"]))
        if self.customer.voice:
            st.append(Paragraph(f"<b>Voice:</b> {_esc(self.customer.voice)}", self.styles["body"]))
        if self.customer.personality:
            st.append(Paragraph(f"<b>Personality:</b> {_esc(', '.join(self.customer.personality))}", self.styles["body"]))

        # Color swatches
        st.append(Paragraph("Color palette", self.styles["h2"]))
        swatches = [
            ("Primary", self.customer.primary_color, self.client_brand.primary),
            ("Accent", self.customer.accent_color, self.client_brand.accent),
            ("Text", self.customer.text_color, self.client_brand.text),
            ("Background", self.customer.background_color, self.client_brand.bg),
            ("Mood BG", self.customer.mood_background_color, self.client_brand.mood_bg),
        ]
        cells = []
        for role, hexv, col in swatches:
            block = ColorBlock(3.2 * cm, 1.2 * cm, col)
            cells.append([block, Paragraph(f"<b>{_esc(role)}</b><br/>{_esc(hexv)}", self.styles["body_small"])])
        tbl = Table(cells, colWidths=[3.3 * cm, 13.7 * cm], rowHeights=[1.4 * cm] * len(cells))
        tbl.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING", (0, 0), (-1, -1), 4),
            ("RIGHTPADDING", (0, 0), (-1, -1), 4),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ("BOX", (0, 0), (-1, -1), 0.4, self.brand.accent),
            ("INNERGRID", (0, 0), (-1, -1), 0.2, self.brand.accent),
        ]))
        st.append(tbl)

        st.append(Paragraph("Typography", self.styles["h2"]))
        st.append(Paragraph(_esc(", ".join(self.customer.fonts) or "Helvetica fallback"), self.styles["body"]))
        st.append(Paragraph("Image headlines 72–96 pt · A+ headlines 60–80 pt · Body 16–22 pt · Line-height 1.4–1.5", self.styles["body_small"]))

        st.append(Paragraph("Photography rules", self.styles["h2"]))
        st.append(Paragraph(_esc(self.customer.photo_rules or "—"), self.styles["body"]))

        st.append(Paragraph("No-gos", self.styles["h2"]))
        st.append(Paragraph(_esc(self.customer.no_gos or "—"), self.styles["body"]))

        # Creative directive — the EQUALICE house rule for every image.
        st.append(Paragraph("How we design (EQUALICE rule)", self.styles["h2"]))
        for line in [
            "<b>DO</b> — earn the click: add credential/quality badges, show the product's contents "
            "(e.g. capsules/pills), put short messaging on the product or on a badge. Every main/hero "
            "must visually answer “why click US?”",
            "<b>DO</b> — keep one callout, one action cue, one supporting prop per image (clean, mobile-legible).",
            "<b>DON'T</b> — never ship a bare product-on-white main with no hook. Whitespace-only is a miss.",
            f"<b>Creative freedom:</b> {self.customer.creative_freedom}/5 — push the design, stay anchored to the brand.",
        ]:
            st.append(Paragraph("• " + line, self.styles["body_small"]))

        self._section_gap()

    # ---- buyer psychology ----
    def _buyer_psychology(self) -> None:
        st = self.story
        self._section_header("2", "Buyer Psychology")
        st.append(Paragraph("Target group", self.styles["h2"]))
        st.append(Paragraph(_esc(self.brief.target_group or "—"), self.styles["body"]))
        st.append(Paragraph("Target problems", self.styles["h2"]))
        st.append(Paragraph(_esc(self.brief.target_problems or "—"), self.styles["body"]))

        # These four lists used to run down the full page width as one long column each, which
        # alone pushed this section onto a second page. Paired into two columns they carry the
        # same content in roughly half the height, and the pairing is meaningful:
        # what the product IS beside what it FEELS like; what buyers praise beside what they fault.
        full = A4[0] - 1.7 * cm * 2

        def bullet_col(title: str, items, marker: str = "•"):
            if not items:
                return ""
            inner = [Paragraph(title, self.styles["h3"])]
            inner += [Paragraph(f"{marker} {_esc(x)}", self.styles["body_small"]) for x in items]
            return inner

        def two_col(left, right):
            if not left and not right:
                return
            t = Table([[left or "", right or ""]], colWidths=[full / 2 - 0.2 * cm, full / 2 - 0.2 * cm])
            t.setStyle(TableStyle([
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (0, -1), 0), ("RIGHTPADDING", (0, 0), (0, -1), 10),
                ("LEFTPADDING", (1, 0), (1, -1), 10), ("RIGHTPADDING", (1, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
            ]))
            st.append(t)

        # Capped at 6 / 5. This is a brief, not an archive — the full lists stay in the SEO
        # sheet, and the sheet is the source of truth. Uncapped, these four lists alone ran to
        # a second page and pushed the moodboard grid (an unsplittable block) onto a third.
        two_col(bullet_col("USPs / technical", self.brief.usps[:6]),
                bullet_col("Emotional benefits", self.brief.emotional_benefits[:6]))
        st.append(Spacer(1, 0.2 * cm))
        two_col(bullet_col("Buyers praise", self.brief.good_reviews[:5], "+"),
                bullet_col("Objections to defuse", self.brief.bad_reviews[:5], "–"))

        self._section_gap()

    # ---- moodboard ----
    def _get_moodboard(self) -> list[MoodImage]:
        if self._moodboard_cache is not None:
            return self._moodboard_cache
        # Per-product override. Brands with more than one product line (Jotti sells leather care
        # AND stone/household cleaners) have brand-level moodboard terms that fit only one line —
        # a marble-cleaner brief was pulling saddles and riding boots. A run.py can set
        # builder.moodboard_terms = [...] to brief the right references for this product.
        override = [t for t in (getattr(self, "moodboard_terms", None) or []) if str(t).strip()]
        queries = override[:6] or self.customer.moodboard_search_terms[:6] or [
            f"{self.customer.name} brand moodboard premium",
            f"{self.brief.product_name[:40]} lifestyle warm light",
        ]
        self._moodboard_cache = fetch_moodboard(queries)
        return self._moodboard_cache

    def _moodboard(self) -> None:
        st = self.story
        self._section_header("3", "Moodboard")
        if not has_unsplash_key():
            st.append(Paragraph(
                "<i>No UNSPLASH_ACCESS_KEY set — embedded tiles below show the search prompt only. Set the env var to fetch real reference images automatically.</i>",
                self.styles["caption"],
            ))
            st.append(Spacer(1, 0.2 * cm))
        moods = self._get_moodboard()
        # 3-wide grid. Was 2x3 at 6.4 cm tall, which needed 19 cm of column and reliably spilled
        # onto a near-empty page. These are reference thumbnails, not artwork — 3 across at
        # 5.0 cm reads just as well and keeps the moodboard on one page.
        cols = 3
        gap = 0.35 * cm
        tile_w = (17 * cm - gap * (cols - 1)) / cols
        tile_h = 4.2 * cm
        rows = []
        row = []
        for i, m in enumerate(moods):
            caption = self.customer.moodboard_search_terms[i] if i < len(self.customer.moodboard_search_terms) else m.query
            row.append(MoodTile(tile_w, tile_h, m, caption, self.brand))
            if len(row) == cols:
                rows.append(row)
                row = []
        if row:
            while len(row) < cols:
                row.append(Spacer(tile_w, tile_h))
            rows.append(row)

        tbl = Table(rows, colWidths=[tile_w] * cols, rowHeights=[tile_h] * len(rows))
        tbl.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ]))
        # Keep the grid whole — a moodboard split across two pages reads as a layout accident.
        st.append(KeepTogether(tbl))
        self._section_gap()

    # ---- image plan ----
    def _image_plan(self) -> None:
        st = self.story
        images = self._build_image_plan()
        self._section_header(
            "4", f"{len(images)} Listing Images",
            f"2000 × 2000 px · sRGB · JPG · ≤ 5 MB · Overlay text in {self.lang.upper()} "
            f"for marketplace {self.customer.marketplace}")
        st.append(Spacer(1, 0.25 * cm))
        # 1) Storyboard — the whole plan on one page, at a glance.
        self._storyboard(images)
        # 2) One compact, design-team-friendly detail card per image.
        for i, img in enumerate(images, 1):
            self._render_image_card(i, img)
        st.append(PageBreak())

    # Friendly role names for the design team
    _ROLE_LABEL = {
        "hero": "HERO", "hook": "HOOK", "educate": "EDUCATE", "desire": "LIFESTYLE",
        "trust": "TRUST", "close": "CLOSE", "title": "TITLE", "bullet": "BULLET",
    }

    def _short_why(self, text: str) -> str:
        """First sentence of the rationale — one short grey context line for designers."""
        t = (text or "").strip()
        if not t:
            return ""
        cut = t.find(". ")
        return (t[: cut + 1] if cut != -1 else t).strip()

    def _storyboard(self, images: list[dict]) -> None:
        st = self.story
        st.append(Paragraph("Storyboard — the full sequence at a glance", self.styles["zone_label"]))
        st.append(Spacer(1, 0.1 * cm))

        def cell(i: int, img: dict):
            role = self._ROLE_LABEL.get(img.get("role", ""), (img.get("role", "") or "").upper())
            head = Table(
                [[Paragraph(str(i), self.styles["sb_num"]), Paragraph(role, self.styles["sb_role"])]],
                colWidths=[0.9 * cm, None],
            )
            head.setStyle(TableStyle([
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]))
            inner = [head, Paragraph(_esc(img.get("purpose", "")), self.styles["sb_body"])]
            lay = (img.get("layout") or "").strip()
            if lay:
                inner.append(Paragraph("LAYOUT: " + _esc(lay.replace("_", " ").upper()),
                                       self.styles["sb_text"]))
            ov = img.get("overlay") or ""
            if ov and not ov.startswith("("):
                inner.append(Paragraph("TEXT: " + _esc(ov), self.styles["sb_text"]))
            return inner

        rows, row = [], []
        for i, img in enumerate(images, 1):
            row.append(cell(i, img))
            if len(row) == 2:
                rows.append(row); row = []
        if row:
            row.append("")  # pad last cell
            rows.append(row)

        colw = (A4[0] - 1.7 * cm * 2) / 2.0
        t = Table(rows, colWidths=[colw, colw])
        t.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("BACKGROUND", (0, 0), (-1, -1), self.brand.mood_bg),
            ("BOX", (0, 0), (-1, -1), 0.5, self.brand.accent),
            ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.white),
            ("LEFTPADDING", (0, 0), (-1, -1), 7), ("RIGHTPADDING", (0, 0), (-1, -1), 7),
            ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ]))
        st.append(t)
        st.append(PageBreak())

    def _build_image_plan(self) -> list[dict]:
        # Prefer AI-designed plan
        if self._ai_images:
            return [
                {
                    "name": img.name,
                    "role": img.role,
                    "background": img.background,
                    "purpose": img.purpose,
                    "visual": img.visual,
                    "props": list(img.props or []),
                    "lighting": img.lighting,
                    "overlay": img.overlay,
                    "overlay_sub": img.overlay_sub,
                    "why_it_works": img.why_it_works,
                    "ctr": getattr(img, "ctr", ""),
                    "cvr": getattr(img, "cvr", ""),
                    "layout": getattr(img, "layout", "") or "",
                    "graphics": list(getattr(img, "graphics", []) or []),
                }
                for img in self._ai_images
            ]

        usps = self.brief.usps or ["Premium quality", "Designed for daily use"]
        main_kws = ", ".join(self.brief.main_keywords[:3]) or self.brief.product_name[:60]

        return [
            {
                "name": "Image 1 — Main Hero",
                "role": "hero",
                "background": "Pure white #FFFFFF",
                "purpose": "Click trigger in the search grid.",
                "visual": "Product centered, three-quarter elevated angle, label fully readable, subtle warm rim light. Tight crop, ~85% of frame height. Subtle contact shadow. No overlay text (Amazon main-image policy).",
                "overlay": "(no overlay — Amazon main image)",
                "overlay_sub": "",
            },
            {
                "name": "Image 2 — Hook",
                "role": "hook",
                "background": "Soft cream / brand mood background",
                "purpose": "Reverses the buyer's #1 fear in one visual.",
                "visual": f"Macro / lifestyle frame that visualises the strongest USP: '{usps[0][:120]}'. Hands only, brand-aligned props, no plastic, no clutter.",
                "overlay": overlay("cold_pressed", self.lang, "PURE & UNCOMPROMISED."),
                "overlay_sub": usps[0] if usps else "",
            },
            {
                "name": "Image 3 — Educate",
                "role": "educate",
                "background": "Mood background with brand accent ribbon",
                "purpose": "Owns the production / quality claim visually.",
                "visual": "Three illustrated steps in warm earthy line-illustration style with brand-color accents. Step-by-step production story justifies the price premium.",
                "overlay": overlay("seed_to_bottle", self.lang, "SOURCE → PROCESS → BOTTLE."),
                "overlay_sub": usps[1] if len(usps) > 1 else "",
            },
            {
                "name": "Image 4 — Desire (lifestyle)",
                "role": "desire",
                "background": "Real lifestyle / use-case scene",
                "purpose": "Buyer self-casts into the use case.",
                "visual": "Cinematic use-case shot. Place the product in the buyer's most realistic moment of use (the moment the review pool praised most strongly).",
                "overlay": overlay("built_for", self.lang, "BUILT FOR DAILY USE."),
                "overlay_sub": (self.brief.good_reviews[0][:120] + "…") if self.brief.good_reviews else (usps[2] if len(usps) > 2 else ""),
            },
            {
                "name": "Image 5 — How to Use / Multi-use",
                "role": "desire",
                "background": "Soft cream triptych or numbered step layout",
                "purpose": "Pre-empts hesitation; shows breadth of use.",
                "visual": "Either three vertical lifestyle panels (each showing a different use case) OR four numbered icons of the usage steps. Hands only, same warm lighting across panels.",
                "overlay": overlay("how_to_use", self.lang, "HOW TO USE — A SIMPLE RITUAL."),
                "overlay_sub": (usps[3] if len(usps) > 3 else "") or "",
            },
            {
                "name": "Image 6 — Trust",
                "role": "trust",
                "background": "Soft white with brand accent",
                "purpose": "Stacks the filters buyers scan for; defuses objections.",
                "visual": "Centered product surrounded by 4 trust badges drawn from your actual claims. Below: small fold-out / cross-section showing protection / construction.",
                "overlay": overlay("trust_stack", self.lang, "PURE INSIDE. PROTECTED OUTSIDE."),
                "overlay_sub": (self.brief.bad_reviews[0][:120] + "…") if self.brief.bad_reviews else "",
            },
            {
                "name": "Image 7 — Brand close",
                "role": "close",
                "background": "Warm environmental brand scene",
                "purpose": "Closes on identity; converts the hesitating buyer.",
                "visual": "Wide environmental shot anchoring the brand story. Soft light, brand-coded props, no overt product hero — the product becomes part of the buyer's life.",
                "overlay": overlay("brand_close", self.lang, "HONEST. HERITAGE-MADE."),
                "overlay_sub": self.customer.tagline or "",
            },
        ]

    def _render_image_card(self, idx: int, img: dict) -> None:
        """Compact, execution-first card for the design team:
        header → WHAT TO SHOW → ON-IMAGE TEXT (highlighted) → PROPS → LIGHT → 1 grey why-line.
        Strategy detail (CTR/CVR/keywords/reviews) is intentionally left off the design pages.
        """
        card: list = []
        full = A4[0] - 1.7 * cm * 2

        # Header: BILD n · ROLE   ........   purpose (right, grey-italic)
        role = self._ROLE_LABEL.get(img.get("role", ""), (img.get("role", "") or "").upper())
        title = f"Image {idx} · {role}"
        head = Table(
            [[Paragraph(_esc(title), self.styles["card_head"]),
              Paragraph(_esc(img.get("purpose", "")), self.styles["card_purpose"])]],
            colWidths=[full * 0.45, full * 0.55],
        )
        head.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "BOTTOM"),
            ("LINEBELOW", (0, 0), (-1, -1), 1.0, self.brand.primary),
            ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ]))
        card.append(head)

        # LAYOUT — the composition the designer builds. Named first, because the review team's
        # #1 complaint was tiles that were nothing but a headline over a photo. The archetype
        # description is clipped: it is a reminder of a shape the designer already knows, and
        # printing the full sentence on all seven cards was a page of repeated boilerplate.
        layout = (img.get("layout") or "").strip()
        graphics = [g for g in (img.get("graphics") or []) if str(g).strip()]
        if layout or graphics:
            bits = []
            if layout:
                pretty = layout.replace("_", " ").upper()
                desc = _clip(_LAYOUT_HINTS.get(layout, ""), 95)
                bits.append(f"<b>{_esc(pretty)}</b>"
                            + (f"  <font color='#6B7280'>{_esc(desc)}</font>" if desc else ""))
            for g in graphics:
                bits.append("• " + _esc(str(g)))
            card.append(Paragraph("LAYOUT", self.styles["zone_label"]))
            card.append(Paragraph("<br/>".join(bits), self.styles["body_small"]))

        # WHAT TO SHOW — direction, not a screenplay. Clipped to two sentences: the review
        # team asked for shorter shot descriptions, and hand-written run.py plans reach this
        # renderer too, so the limit is enforced here rather than only in the AI prompt.
        card.append(Paragraph("WHAT TO SHOW", self.styles["zone_label"]))
        visual_html = _esc(_sentences(img["visual"], 2)).replace("\n", "<br/>")
        if img.get("background"):
            visual_html = f"<b>BG:</b> {_esc(_clip(img['background'], 70))}  ·  " + visual_html
        card.append(Paragraph(visual_html, self.styles["body_small"]))

        # ON-IMAGE TEXT — the thing the designer actually typesets. Highlighted box.
        ov = img.get("overlay") or ""
        if ov and not ov.startswith("("):
            box_inner = [Paragraph(_esc(ov), self.styles["onimg"])]
            if img.get("overlay_sub"):
                box_inner.append(Paragraph(_esc(img["overlay_sub"]), self.styles["onimg_sub"]))
            box = Table([[box_inner]], colWidths=[full])
            box.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, -1), self.brand.mood_bg),
                ("LINEBEFORE", (0, 0), (-1, -1), 2.5, self.brand.primary),
                ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]))
            label = Table([[Paragraph(f"ON-IMAGE TEXT ({self.lang.upper()})", self.styles["zone_label"])]],
                          colWidths=[full])
            label.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0), ("TOPPADDING", (0, 0), (-1, -1), 4)]))
            card.append(label)
            card.append(box)
        elif ov:
            card.append(Paragraph("ON-IMAGE TEXT", self.styles["zone_label"]))
            card.append(Paragraph(_esc(ov), self.styles["onimg_sub"]))

        # PROPS + LIGHT on ONE line. They used to be two stacked rows with a bullet per prop,
        # which cost four or five lines per card for what is a short list — the single biggest
        # source of the "too much copy" the review team flagged on the design pages.
        props = [_esc(p) for p in (img.get("props") or []) if str(p).strip()]
        tail = []
        if props:
            tail.append("<b>PROPS</b>  " + ", ".join(props))
        if img.get("lighting"):
            tail.append("<b>LIGHT</b>  " + _esc(_clip(img["lighting"], 90)))
        if tail:
            card.append(Paragraph("<font color='#6B7280'>  ·  </font>".join(tail),
                                  self.styles["body_small"]))

        # One short grey strategy line (the only strategy kept on design pages).
        why = self._short_why(img.get("why_it_works", ""))
        if why:
            card.append(Paragraph("Why: " + _esc(why), self.styles["why_line"]))

        card.append(Spacer(1, 0.55 * cm))
        self.story.append(KeepTogether(card))

    # ---- A+ modules ----
    def _apply_brand_module_rules(self) -> None:
        """House rules applied to the A+ module list before scans + render (Jonas):
        NEW brands: (1) NO Premium Comparison. (2) The Q&A is the FINALE (last module).
        (3) The module right before the Q&A ends with a SMART line that bridges into it
        (brand-voice + a 'the answers are right below' teaser). Keeps 7 modules — if no
        benefits/brand closer was authored, a 'From the Brand' banner is inserted before
        the Q&A. Established brands are untouched."""
        from .ai import AIModule
        mods = self._ai_modules
        if not mods or not bool(getattr(self.customer, "new_brand", False)):
            return
        mods = [m for m in mods if m.role != "a+_comparison"]      # new brands don't compare yet
        qa = [m for m in mods if m.role == "a+_qa"]
        non_qa = [m for m in mods if m.role != "a+_qa"]
        statement = (getattr(self.customer, "brand_statement", "") or "").strip()
        lang = (self.customer.overlay_language or "en").lower()
        bridge = {
            "de": "Noch Fragen? Die wichtigsten Antworten findest du direkt darunter.",
            "en": "Still have questions? The most-asked answers are right below.",
        }.get(lang, "Still have questions? The most-asked answers are right below.")
        if not qa:
            self._ai_modules = non_qa
            return
        # keep 7 modules: if there is no dedicated benefits/brand closer before the Q&A, add one
        if statement and len(non_qa) < 6:
            non_qa.append(AIModule(
                name="Module — From the Brand",
                role="a+_banner",
                headline="FROM THE BRAND",
                body=_esc(statement),
                visual=(f"Warm benefits/brand closer in the {self.customer.name} look: a confident "
                        "brand-voice line and a small row of the brand's hero product / favourites."),
                alt=f"Brand closer for {self.customer.name} leading into the Q&A.",
            ))
        # append the smart Q&A bridge to the module immediately before the Q&A (idempotent)
        if non_qa:
            closer = non_qa[-1]
            btxt = _esc(bridge)
            if btxt not in (closer.body or ""):
                closer.body = (closer.body or "") + f"<br/><br/><i>{btxt}</i>"
        self._ai_modules = non_qa + qa    # Q&A is always the finale (Module 7)

    def _aplus_modules(self) -> None:
        st = self.story
        n = len(self._ai_modules or [])
        self._section_header("5", f"A+ Premium Content ({n} modules)")

        # Prefer AI-designed modules. Body may contain intentional HTML
        # (<b>, <br/>) — do NOT escape here. _render_module's Body cell uses
        # a Paragraph that interprets HTML; visual + alt are still escaped.
        if self._ai_modules:
            for m in self._ai_modules:
                self._render_module({
                    "name": m.name,
                    "role": m.role,
                    "headline": m.headline,
                    "body": m.body,
                    "visual": m.visual,
                    "alt": m.alt,
                })
            st.append(PageBreak())
            return

        usps = self.brief.usps or []
        modules = [
            {
                "name": "Module 1 — Premium Full Image: Brand banner",
                "role": "a+_banner",
                "headline": (self.customer.tagline.upper() if self.customer.tagline else "BRAND TAGLINE"),
                "body": f"{self.customer.voice or 'Set brand voice in the customer config.'}",
                "visual": "Cinematic brand-anchor scene with product in the foreground. Brand tagline in the left third.",
                "alt": f"Cinematic brand banner image for {self.customer.name} {self.brief.product_name[:60]}.",
            },
            {
                "name": "Module 2 — Premium Carousel (5 tiles): Brand Difference",
                "role": "a+_carousel",
                "headline": "THE DIFFERENCE",
                "body": " · ".join((u.split(",")[0] for u in usps[:5])) or "Top 5 USPs as scan-friendly tiles.",
                "visual": "5 square tiles, same lighting, color-coded label band.",
                "alt": f"Five-tile carousel listing the top five USPs of {self.customer.name} {self.brief.product_name[:60]}.",
            },
            {
                "name": "Module 3 — Premium Full Image: Process / Story",
                "role": "a+_banner",
                "headline": overlay("seed_to_bottle", self.lang),
                "body": "Three-step horizontal production story. Earthy palette. Zero shortcuts.",
                "visual": "Three illustrated steps along the banner; brand accent ribbon at the foot.",
                "alt": "Three-step illustration of production process from sourcing to packaging.",
            },
            {
                "name": "Module 4 — Premium Full Image: Use cases",
                "role": "a+_banner",
                "headline": overlay("built_for", self.lang),
                "body": "Triptych within one banner: each panel shows a different real use case.",
                "visual": "LEFT / CENTER / RIGHT lifestyle panels. Warm earth tones throughout. Body band underneath.",
                "alt": "Triptych lifestyle banner showing three real-world use cases.",
            },
            {
                "name": "Module 5 — Premium Carousel (5 tiles): Product Family",
                "role": "a+_carousel",
                "headline": "THE FAMILY",
                "body": "5 tiles — this SKU + 4 cross-sell SKUs. Same composition, color-coded label band.",
                "visual": "Identical 5-tile layout for every brand SKU.",
                "alt": f"Five-tile carousel of the {self.customer.name} product family.",
            },
            {
                "name": "Module 6 — Premium Q&A",
                "role": "a+_qa",
                "headline": "QUESTIONS & ANSWERS",
                "body": self._build_qa_block(),
                "visual": "Vertical Q/A table. Brand accent dividers between Qs.",
                "alt": f"Premium Q&A module addressing the top questions about {self.brief.product_name[:60]}.",
            },
            {
                "name": "Module 7 — Premium Comparison Chart",
                "role": "a+_comparison",
                "headline": "WHY CHOOSE THIS",
                "body": "Up to 4 product columns; highlight the brand column with subtle brand-color tint + accent 'RECOMMENDED' ribbon.",
                "visual": "Standard Amazon Premium Comparison Chart spec.",
                "alt": f"Premium comparison chart for {self.brief.product_name[:60]} vs. category alternatives.",
            },
        ]
        for m in modules:
            self._render_module(m)
        st.append(PageBreak())

    def _build_qa_block(self) -> str:
        # Prefer AI-drafted Q&A (brand-voice, friction-defusing) over raw RUFUS dump
        if self._ai_qa:
            items = [f"<b>Q.</b> {_esc(qa.q)}<br/><b>A.</b> {_esc(qa.a)}" for qa in self._ai_qa]
            return "<br/><br/>".join(items)
        if not self.brief.rufus_qa:
            return "Auto-Q&amp;A pool empty. Add at least 4 Q/A pairs in the RUFUS sheet of the Excel."
        items = []
        for qa in self.brief.rufus_qa[:6]:
            items.append(f"<b>Q.</b> {_esc(qa['q'])}<br/><b>A.</b> {_esc(qa['a'])}")
        return "<br/><br/>".join(items)

    def _render_module(self, m: dict) -> None:
        card: list = []
        card.append(Paragraph(_esc(m["name"]), self.styles["h2"]))
        rows = [
            ["Headline (overlay, " + _esc(self.lang.upper()) + ")", Paragraph(_esc(m["headline"]), self.styles["body_small"])],
            ["Body", Paragraph(m["body"], self.styles["body_small"])],  # body already HTML for QA module
            ["Visual direction", Paragraph(_esc(m["visual"]), self.styles["body_small"])],
            ["Alt text", Paragraph(_esc(m["alt"]), self.styles["body_small"])],
        ]
        t = Table(rows, colWidths=[3.5 * cm, 13.5 * cm])
        t.setStyle(self._kv_style())
        card.append(t)
        card.append(Spacer(1, 0.1 * cm))
        card.append(self._arg_block(m["role"], m["headline"] + " " + m["body"]))
        card.append(Spacer(1, 0.4 * cm))
        self.story.append(KeepTogether(card))

    # ---- master copy ----
    def _master_copy(self) -> None:
        st = self.story
        self._section_header("6", "Master Copy")

        title_text = self._draft_title()
        title_card = [
            Paragraph("Title (≤ 200 chars)", self.styles["h2"]),
            Paragraph(_esc(title_text), self.styles["body"]),
            self._arg_block("title", title_text),
            Spacer(1, 0.3 * cm),
        ]
        st.append(KeepTogether(title_card))

        st.append(Paragraph("Bullets", self.styles["h2"]))
        bullets = self._draft_bullets()
        for i, b in enumerate(bullets, 1):
            # bullets already contain <b>HEAD</b> markup — escape only the body part
            bullet_card = [
                Paragraph(f"<b>{i}.</b> {b}", self.styles["body"]),
                self._arg_block("bullet", b),
                Spacer(1, 0.2 * cm),
            ]
            st.append(KeepTogether(bullet_card))

        st.append(Paragraph("Backend search terms (≤ 250 bytes)", self.styles["h2"]))
        st.append(Paragraph(_esc(self._draft_backend()), self.styles["mono"]))
        self._section_gap()

    def _draft_title(self) -> str:
        if self._ai_title:
            return self._ai_title
        kws = self.brief.main_keywords[:3] or [self.brief.product_name[:50]]
        usp_short = (self.brief.usps[0][:40] if self.brief.usps else "premium").strip(" ,.;")
        return (
            f"{self.customer.name} {kws[0].title() if kws else ''} {self.brief.pack_size} — "
            f"{usp_short} · {' · '.join(k.title() for k in kws[1:3])}"
        ).strip(" -—·")[:200]

    def _draft_bullets(self) -> list[str]:
        if self._ai_bullets:
            return self._ai_bullets
        bullets: list[str] = []
        usps = self.brief.usps[:5] or ["Premium quality"]
        for u in usps:
            head = _esc(u.split(",")[0].strip().upper()[:60])
            bullets.append(f"<b>{head}</b> — {_esc(u)}")
        while len(bullets) < 5:
            bullets.append("<b>BUILT ON TRUST</b> — Backed by careful sourcing, designed for households who care about every ingredient.")
        return bullets[:5]

    def _draft_backend(self) -> str:
        if self._ai_backend:
            return self._ai_backend
        terms = self.brief.all_keywords[:60]
        s = " ".join(t for t in terms)
        return s.encode("utf-8")[:240].decode("utf-8", "ignore").strip()

    # ---- final QA helpers ----
    def _gather_copy_texts(self) -> list[str]:
        """All customer-facing copy that must pass the compliance scan."""
        texts: list[str] = [self._draft_title()]
        texts += self._draft_bullets()
        for img in (self._ai_images or []):
            texts += [getattr(img, "overlay", ""), getattr(img, "overlay_sub", "")]
        for m in (self._ai_modules or []):
            texts += [getattr(m, "headline", ""), getattr(m, "body", "")]
        for qa in (self._ai_qa or []):
            texts += [getattr(qa, "q", ""), getattr(qa, "a", "")]
        return [t for t in texts if t]

    def _ctr_cvr_recap(self) -> None:
        """Per-image CTR/CVR rationale — kept OFF the design pages, recapped here at the
        end for the strategy/account team (the 'check CTR & CVR at the end' step)."""
        imgs = [i for i in (self._ai_images or []) if getattr(i, "ctr", "") or getattr(i, "cvr", "")]
        if not imgs:
            return
        st = self.story
        self._section_header("8", "CTR / CVR Strategy (per image)",
                            "Why each image earns the click (CTR) and converts (CVR). "
                            "For the strategy and account team.")
        st.append(Spacer(1, 0.2 * cm))
        rows = [[Paragraph("<b>Image</b>", self.styles["body_small"]),
                 Paragraph("<b>CTR — why it earns the click</b>", self.styles["body_small"]),
                 Paragraph("<b>CVR — why it converts</b>", self.styles["body_small"])]]
        for i, img in enumerate(self._ai_images or [], 1):
            role = self._ROLE_LABEL.get(getattr(img, "role", ""), (getattr(img, "role", "") or "").upper())
            rows.append([
                Paragraph(f"<b>{i}</b><br/>{_esc(role)}", self.styles["body_small"]),
                Paragraph(_esc(getattr(img, "ctr", "") or "—"), self.styles["body_small"]),
                Paragraph(_esc(getattr(img, "cvr", "") or "—"), self.styles["body_small"]),
            ])
        t = Table(rows, colWidths=[2.0 * cm, 7.5 * cm, 7.5 * cm])
        t.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), self.brand.accent),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("BOX", (0, 0), (-1, -1), 0.4, self.brand.accent),
            ("INNERGRID", (0, 0), (-1, -1), 0.3, self.brand.mood_bg),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, self.brand.bg]),
            ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5),
            ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ]))
        st.append(t)
        st.append(PageBreak())

    # ---- compliance & designer handoff ----
    def _compliance_and_handoff(self) -> None:
        st = self.story
        self._section_header("7", "Compliance & Designer Handoff")

        # Status banner — blocking violations (high) vs warnings (low).
        flags = self._ai_compliance or []
        blocking = [f for f in flags if f.severity == "high"]
        warnings = [f for f in flags if f.severity != "high"]
        if blocking:
            status = f"⚠ {len(blocking)} BLOCKING VIOLATION(S) — fix before publishing."
            banner_col = _hex("#C0392B")
        else:
            status = "✓ COMPLIANCE PASSED — no blocking violations on any copy."
            banner_col = self.brand.accent
        banner = Table([[Paragraph(f"<b>{status}</b>", self.styles["onimg_sub"])]], colWidths=[A4[0] - 1.7 * cm * 2])
        banner.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), banner_col),
            ("TEXTCOLOR", (0, 0), (-1, -1), colors.white),
            ("LEFTPADDING", (0, 0), (-1, -1), 8), ("TOPPADDING", (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ]))
        st.append(banner)
        st.append(Paragraph(
            "Auto-scanned: title, bullets, all image overlays, A+ modules and Q&A against Amazon "
            "prohibited words, restricted claims and formatting rules.",
            self.styles["caption"],
        ))
        st.append(Spacer(1, 0.25 * cm))

        # AI compliance scan results (if any)
        if self._ai_compliance is not None:
            if self._ai_compliance:
                st.append(Paragraph("Compliance flags (review)", self.styles["h2"]))
                st.append(Paragraph(
                    f"<b>{len(blocking)}</b> blocking · <b>{len(warnings)}</b> warning(s).",
                    self.styles["body_small"],
                ))
                rows = [["Severity", "Phrase", "Issue", "Suggestion"]]
                for f in self._ai_compliance:
                    rows.append([
                        Paragraph(f"<b>{_esc(f.severity.upper())}</b>", self.styles["body_small"]),
                        Paragraph(f"<i>“{_esc(f.text)}”</i>", self.styles["body_small"]),
                        Paragraph(_esc(f.issue), self.styles["body_small"]),
                        Paragraph(_esc(f.suggestion), self.styles["body_small"]),
                    ])
                tbl = Table(rows, colWidths=[1.8 * cm, 4.0 * cm, 5.5 * cm, 5.7 * cm])
                tbl.setStyle(TableStyle([
                    ("BACKGROUND", (0, 0), (-1, 0), self.brand.accent),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                    ("FONTSIZE", (0, 0), (-1, -1), 8),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("BOX", (0, 0), (-1, -1), 0.4, self.brand.accent),
                    ("INNERGRID", (0, 0), (-1, -1), 0.2, self.brand.accent),
                    ("LEFTPADDING", (0, 0), (-1, -1), 4),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                    ("TOPPADDING", (0, 0), (-1, -1), 3),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                ]))
                st.append(tbl)
                st.append(Spacer(1, 0.3 * cm))
            else:
                st.append(Paragraph("AI compliance check", self.styles["h2"]))
                st.append(Paragraph(
                    "Title + bullets passed the AI compliance scan — no medical/curative claims, no superlatives, no competitor names detected.",
                    self.styles["body_small"],
                ))
                st.append(Spacer(1, 0.3 * cm))

        st.append(Paragraph("Compliance notes", self.styles["h2"]))
        compliance = [
            "Main image: pure white background, product ≥ 85% of frame, no overlay text or watermark.",
            "No medical / regrowth / curative claims unless explicitly approved.",
            "No competitor brand names anywhere in copy or alt text.",
            "Patch-test guidance required for all topical / personal-care SKUs.",
            "Certifications (Organic, Non-GMO, etc.) only with documented proof.",
            f"All on-image overlay text in {self.lang.upper()} for marketplace {self.customer.marketplace}.",
            "Avoid superlatives: 'best', '#1', 'ultimate', 'miracle'.",
        ]
        for c in compliance:
            st.append(Paragraph(f"• {c}", self.styles["body_small"]))

        st.append(Paragraph("Designer handoff checklist", self.styles["h2"]))
        for c in [
            "Brand colors locked to config above.",
            "Export sizes: 2000×2000 px main images · 1464×600 A+ banners · 220×220 A+ carousel · 150×300 comparison tiles.",
            "Mobile crop tested on every banner (text must remain legible).",
            f"Overlay text in {self.lang.upper()}; body copy stays English in the brief.",
            "Logo + label files received before design start.",
            "Photography brief signed off against the photography rules and no-gos.",
        ]:
            st.append(Paragraph(f"☐ {c}", self.styles["body_small"]))

        if self.brief.module_selection:
            st.append(Paragraph("Modules selected (from Excel)", self.styles["h2"]))
            for m in self.brief.module_selection:
                st.append(Paragraph(f"• {_esc(m)}", self.styles["body_small"]))


def plan_to_dict(builder: "BriefBuilder") -> dict:
    """Everything the team can edit, as plain JSON. Saved beside each PDF so a plan can be
    corrected and re-rendered WITHOUT paying for another AI generation."""
    from dataclasses import asdict, is_dataclass

    def dump(x):
        return asdict(x) if is_dataclass(x) else dict(x or {})

    return {
        "title": builder._ai_title or "",
        "bullets": list(builder._ai_bullets or []),
        "backend": builder._ai_backend or "",
        "images": [dump(i) for i in (builder._ai_images or [])],
        "modules": [dump(m) for m in (builder._ai_modules or [])],
        "qa": [dump(q) for q in (builder._ai_qa or [])],
    }


def plan_from_dict(data: dict) -> dict:
    """Inverse of plan_to_dict — rebuild the dataclasses, ignoring unknown/missing keys so an
    older sidecar (written before a field existed) still loads."""
    from .ai import AIImagePlanItem, AIModule, AIQA
    import inspect

    def make(cls, d):
        allowed = set(inspect.signature(cls).parameters)
        return cls(**{k: v for k, v in (d or {}).items() if k in allowed})

    return {
        "title": data.get("title") or "",
        "bullets": list(data.get("bullets") or []),
        "backend": data.get("backend") or "",
        "images": [make(AIImagePlanItem, i) for i in (data.get("images") or [])],
        "modules": [make(AIModule, m) for m in (data.get("modules") or [])],
        "qa": [make(AIQA, q) for q in (data.get("qa") or [])],
    }


def build_brief(
    customer: Customer,
    brief: ParsedBrief,
    output_path: Path,
    ai: Optional[BriefAI] = None,
    progress_cb=None,
    seo_title: Optional[str] = None,
    seo_bullets: Optional[list[str]] = None,
    seo_backend: Optional[str] = None,
    result_out: Optional[dict] = None,
    plan_content: Optional[dict] = None,
) -> Path:
    """Build a branded Image + A+ Premium plan PDF.

    SEO copy is INPUT, not generated: pass seo_title / seo_bullets / seo_backend (from the
    SEO team's sheet) and they are used verbatim; the AI then writes only the creative
    Image plan + A+ modules + Q&A. Leave them None to let the AI draft copy too (fallback).

    plan_content: an edited plan (from plan_from_dict). When given, NO AI runs — the plan is
    re-rendered exactly as edited, then re-scanned for compliance and copy length."""
    builder = BriefBuilder(customer, brief, output_path,
                           ai=None if plan_content else ai, progress_cb=progress_cb)
    if seo_title:
        builder._ai_title = seo_title
    if seo_bullets:
        builder._ai_bullets = seo_bullets
    if seo_backend:
        builder._ai_backend = seo_backend
    if plan_content:
        builder._ai_title = plan_content.get("title") or builder._ai_title
        builder._ai_bullets = plan_content.get("bullets") or builder._ai_bullets
        builder._ai_backend = plan_content.get("backend") or builder._ai_backend
        builder._ai_images = plan_content.get("images") or None
        builder._ai_modules = plan_content.get("modules") or None
        builder._ai_qa = plan_content.get("qa") or None
        builder.copy_source_label = "Edited in the tool by the team"
    path = builder.build()
    if result_out is not None:
        from . import qa as _qa
        comp = builder._ai_compliance or []
        result_out["compliance"] = comp
        result_out["compliance_blocking"] = _qa.has_blocking(comp)
        result_out["copy_warnings"] = builder._copy_warnings or []
        result_out["content"] = plan_to_dict(builder)
    return path


if __name__ == "__main__":
    import sys
    from .customers import load_customer
    from .excel_parser import parse_excel

    excel = sys.argv[1] if len(sys.argv) > 1 else "/Users/jonask/Desktop/Claude_Code/.tmp/Chekko Oil/02_B09HCSZLP1 - Chekko Castor Oil SEO.xlsx"
    slug = sys.argv[2] if len(sys.argv) > 2 else "chekko"
    out = sys.argv[3] if len(sys.argv) > 3 else "/tmp/test_brief.pdf"
    c = load_customer(slug)
    b = parse_excel(excel)
    path = build_brief(c, b, Path(out))
    print(f"Built: {path}")
