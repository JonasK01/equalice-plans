"""Loader für die NEUEN Ultra-PRO-Listings (51-73).

Diese Listings kommen mit zwei Excel-Dateien pro Produkt:
  • <listing>.xlsx  — enthält ein Sheet 'SEO_...' mit fertigem Titel, 5 Bullets,
    Item-Highlights und Backend-Search-Terms (vom SEO-Team, Spalte E, Labels in Spalte H).
  • A+ Premium ...xlsx — Sheet1 mit Q&A (6th Module) und Vergleichstabelle (7th Module).

Dieser Loader zieht diese Inhalte 1:1 heraus, damit die Image-Pläne produktspezifisch
und SEO-treu sind. Bildregie/Overlays bleiben handgeschrieben pro Produkt.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path
import openpyxl


@dataclass
class SeoListing:
    title: str = ""
    short_title: str = ""
    highlights: str = ""
    backend: str = ""
    bullets: list[str] = field(default_factory=list)
    description: str = ""


@dataclass
class AplusData:
    qa: list[tuple[str, str]] = field(default_factory=list)
    comp_headline: str = ""
    comp_columns: list[str] = field(default_factory=list)   # inkl. Spalte 0 = dieses Produkt
    comp_rows: list[tuple[str, list[str]]] = field(default_factory=list)


def _norm(v) -> str:
    return "" if v is None else str(v).strip()


def list_seo_sheets(listing_xlsx: str | Path) -> list[str]:
    """Alle Sheets, die wie ein SEO-Variantenblatt aussehen (Header-Label 'New Title' in
    Spalte H). So findet der Agent auch Varianten, deren Sheet NICHT mit 'seo' beginnt
    (z. B. 'Tabellenblatt10' = Ground-Variante). Reihenfolge = Sheet-Reihenfolge."""
    wb = openpyxl.load_workbook(str(listing_xlsx), data_only=True)
    out = []
    for s in wb.sheetnames:
        ws = wb[s]
        labels = " ".join(_norm(ws.cell(r, 8).value).lower()
                           for r in range(1, min(ws.max_row, 40) + 1))
        if "new title" in labels and "bullets point" in labels:
            out.append(s)
    return out


def load_seo(listing_xlsx: str | Path, sheet: str | None = None) -> SeoListing:
    wb = openpyxl.load_workbook(str(listing_xlsx), data_only=True)
    if sheet:
        if sheet not in wb.sheetnames:
            raise ValueError(f"Sheet '{sheet}' nicht in {listing_xlsx} ({wb.sheetnames})")
        seo_name = sheet
    else:
        seo_name = next((s for s in wb.sheetnames if s.lower().startswith("seo")), None)
        if not seo_name:
            raise ValueError(f"kein SEO-Sheet in {listing_xlsx}")
    ws = wb[seo_name]
    out = SeoListing()
    # Header-Labels stehen in Spalte H (8), zugehörige Werte in Spalte E (5), i.d.R. eine Zeile tiefer.
    for r in range(1, ws.max_row + 1):
        label = _norm(ws.cell(r, 8).value)
        if not label:
            continue
        low = label.lower()
        val = _norm(ws.cell(r + 1, 5).value)
        if low.startswith("new title"):
            out.title = val
        elif low.startswith("short title"):
            out.short_title = val
        elif low.startswith("item highlights"):
            out.highlights = val
        elif low.startswith("backend search"):
            out.backend = val
        elif low.startswith("bullets point"):
            bl = []
            for rr in range(r + 1, r + 9):
                cv = _norm(ws.cell(rr, 5).value)
                if cv and not cv.startswith("="):
                    bl.append(cv)
                if len(bl) >= 5:
                    break
            out.bullets = bl
        elif low.startswith("description"):
            out.description = val
    return out


def _comply(s: str) -> str:
    """Neutralise Amazon-blocking claim words in raw SEO/A+ source copy while keeping the
    meaning intact. Some source sheets say 'prevent peeling' (ChromaFusion); Amazon flags
    'prevent(s)' as a restricted claim. The approved Ultra PRO wording is 'resist' (see
    hatsune_miku run.py: "ChromaFusion helps resist peeling — never 'prevent'"). This runs
    on every emitted copy line so loader-sourced bullets and Q&A pass compliance."""
    import re as _re

    def _r(m):
        w = m.group(0)
        base = "resists" if w.lower().endswith("s") else "resist"
        return base.capitalize() if w[0].isupper() else base

    return _re.sub(r"(?i)\bprevents?\b", _r, s or "")


_KW_BLOCKERS = __import__("re").compile(
    r"(?i)\b(best|#\s*1|no\.?\s*1|number\s*one|world'?s\s*(best|finest)|finest|"
    r"ultimate|miracle|guaranteed|leading)\b"
)


def scrub_keywords(kws) -> list[str]:
    """Drop keyword-research terms that contain Amazon-restricted superlatives ('best costa
    rica coffee', '#1 …', 'ultimate …'). These come from KW-research tabs via parse_excel and
    are rendered in the brief's keyword appendix — a single 'best' trips the compliance scan
    (and would get a live listing suppressed anyway). Real listing copy is never touched."""
    out = []
    for k in kws or []:
        s = str(k).strip()
        if s and not _KW_BLOCKERS.search(s):
            out.append(s)
    return out


def _esc_html(s: str) -> str:
    """Roh-Text für ein raw-HTML-Paragraph-Feld absichern (&, <, > -> Entities).
    Läuft zuerst durch _comply, damit Amazon-Sperrwörter aus dem Sheet neutralisiert werden."""
    return _comply(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def as_bullets_html(seo: "SeoListing") -> list[str]:
    """SEO-Bullets ('HEAD: body') -> Haus-Stil '<b>HEAD</b> — body' (raw HTML, escaped)."""
    out = []
    for b in seo.bullets:
        esc = _esc_html(b.strip())
        if ": " in esc:
            head, body = esc.split(": ", 1)
            out.append(f"<b>{head.strip()}</b> — {body.strip()}")
        else:
            out.append(esc)
    return out


def as_qa(ap: "AplusData"):
    """A+ Q&A -> Liste von AIQA (für builder._ai_qa)."""
    from tools.brief_app.core.ai import AIQA
    return [AIQA(q=_comply(q), a=_comply(a)) for q, a in ap.qa if q and a]


def qa_module(ap: "AplusData", headline: str = "QUESTIONS COLLECTORS ASK"):
    """A+ Q&A -> AIModule role a+_qa (kurze, saubere Q/A-Tabelle)."""
    from tools.brief_app.core.ai import AIModule
    parts = []
    for q, a in ap.qa:
        parts.append(f"<b>Q.</b> {_esc_html(q)}<br/><b>A.</b> {_esc_html(a)}")
    body = "<br/><br/>".join(parts)
    return AIModule(
        name="Module — Premium Q&A (aus SEO/A+ Sheet)",
        role="a+_qa",
        headline=headline,
        body=body,
        visual="Vertical Q/A table, Ultra PRO black header with red divider lines; small red Q. and black A. labels.",
        alt="Premium Q&A module answering the most-asked collector questions for this product.",
    )


def comparison_module(ap: "AplusData"):
    """A+ Vergleich -> AIModule role a+_comparison. Spalten sind Ultra-PRO-eigene Produkte
    (Cross-Sell-Familie), daher dürfen die Namen genannt werden; ASINs werden entfernt."""
    from tools.brief_app.core.ai import AIModule
    import re as _re
    cols = [_re.sub(r"\s*\(B0[A-Z0-9]{8}\)", "", c).strip() for c in ap.comp_columns]
    this_col = cols[0] if cols else "This product"
    header_line = " · ".join(f"<b>{c}</b>" if i == 0 else c for i, c in enumerate(cols))
    row_lines = []
    for label, vals in ap.comp_rows:
        # 'Best For' ist eine Standard-Amazon-Vergleichszeile, triggert aber die Superlativ-Regel
        label = label.replace("Best For", "Ideal For")
        cells = " · ".join(vals)
        row_lines.append(f"<b>{_esc_html(label)}:</b> {_esc_html(cells)}")
    body = (
        f"Vergleich über {len(cols)} Ultra-PRO-Produkte (Cross-Sell-Familie): "
        f"{_esc_html(header_line) if False else header_line}.<br/><br/>"
        + "<br/>".join(row_lines)
        + f"<br/><br/>Spalte 1 (<b>{_esc_html(this_col)}</b>) hervorheben (roter Rahmen, "
          f"'Trusted since 1952'-Band). Nur Ultra-PRO-eigene Produkte, keine Fremdmarken."
    )
    return AIModule(
        name="Module — Premium Comparison (aus A+ Sheet)",
        role="a+_comparison",
        headline="COMPARE THE ULTRA PRO RANGE",
        body=body,
        visual="Standard Amazon Premium Comparison Chart. First column = this product, highlighted red. Ultra PRO black/red/white styling. Columns are Ultra PRO's own products.",
        alt="Premium comparison chart across Ultra PRO storage and protection products.",
    )


def load_aplus(aplus_xlsx: str | Path) -> AplusData:
    wb = openpyxl.load_workbook(str(aplus_xlsx), data_only=True)
    ws = wb[wb.sheetnames[0]]
    out = AplusData()
    # --- Q&A: Frage-Zeile ('Q1:' oder 'Question 1:') gefolgt von Antwort ('A:' oder 'Answer:') ---
    import re as _re
    q_re = _re.compile(r"^(q\d*|question\s*\d*)\s*:", _re.I)
    a_re = _re.compile(r"^(a|answer)\s*:", _re.I)
    rows = [_norm(ws.cell(r, 1).value) for r in range(1, ws.max_row + 1)]
    i = 0
    while i < len(rows):
        cell = rows[i]
        if q_re.match(cell):
            q = cell.split(":", 1)[1].strip()
            a = ""
            if i + 1 < len(rows) and a_re.match(rows[i + 1]):
                a = rows[i + 1].split(":", 1)[1].strip()
                i += 1
            if q:
                out.qa.append((q, a))
        i += 1
    # --- Vergleich: ab Zeile mit A == '7th Module' ---
    for r in range(1, ws.max_row + 1):
        if _norm(ws.cell(r, 1).value).lower().startswith("7th module"):
            cols = [_norm(ws.cell(r, c).value) for c in range(2, ws.max_column + 1)]
            out.comp_columns = [c for c in cols if c]
            for rr in range(r + 1, ws.max_row + 1):
                label = _norm(ws.cell(rr, 1).value)
                if not label:
                    continue
                vals = [_norm(ws.cell(rr, c).value) for c in range(2, 2 + len(out.comp_columns))]
                out.comp_rows.append((label, vals))
            break
    return out
