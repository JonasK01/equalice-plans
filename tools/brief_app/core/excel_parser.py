"""Generalized SEO Excel parser.

Reads a Chekko/Norb-style SEO analysis Excel and produces a normalized ParsedBrief
dict that the PDF builder can consume.

Sheet name matching is fuzzy (case-insensitive substring) so different naming
conventions across customers still parse correctly.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import openpyxl


# ---------- helpers ----------

def _norm(s: str) -> str:
    return (s or "").strip().lower()


def _find_sheet(wb, *patterns: str) -> Optional[str]:
    pats = [p.lower() for p in patterns]
    for name in wb.sheetnames:
        n = _norm(name)
        if any(p in n for p in pats):
            return name
    return None


def _iter_rows(ws, max_rows: int | None = None):
    last = ws.max_row if max_rows is None else min(ws.max_row, max_rows)
    for r in range(1, last + 1):
        yield r, [ws.cell(r, c).value for c in range(1, ws.max_column + 1)]


def _coerce_str(v) -> str:
    if v is None:
        return ""
    return str(v).strip()


def _split_usps(text: str) -> list[str]:
    """Split USP cells that come as comma- or semicolon-separated text."""
    if not text:
        return []
    out = []
    for raw in text.replace(";", "\n").replace(" , ", "\n").split("\n"):
        s = raw.strip(" ,-•·").strip()
        if s and len(s) > 3:
            out.append(s)
    return out


# ---------- data model ----------

@dataclass
class ParsedBrief:
    product_name: str = ""
    brand: str = ""
    asin: str = ""
    marketplace: str = ""
    listing_url: str = ""
    pack_size: str = ""
    category: str = ""
    main_keywords: list[str] = field(default_factory=list)
    all_keywords: list[str] = field(default_factory=list)
    usps: list[str] = field(default_factory=list)
    technical_info: list[str] = field(default_factory=list)
    emotional_benefits: list[str] = field(default_factory=list)
    target_group: str = ""
    target_problems: str = ""
    competitors: list[dict] = field(default_factory=list)
    rufus_qa: list[dict] = field(default_factory=list)
    good_reviews: list[str] = field(default_factory=list)
    bad_reviews: list[str] = field(default_factory=list)
    ctr_notes: list[str] = field(default_factory=list)
    cvr_notes: list[str] = field(default_factory=list)
    module_selection: list[str] = field(default_factory=list)
    raw_excel_path: str = ""

    def has_minimum_data(self) -> tuple[bool, list[str]]:
        missing = []
        if not self.product_name:
            missing.append("product name")
        if not self.usps:
            missing.append("USPs")
        if not self.all_keywords:
            missing.append("keywords")
        return (len(missing) == 0, missing)


# ---------- main parser ----------

def parse_excel(path: str | Path) -> ParsedBrief:
    path = Path(path)
    wb = openpyxl.load_workbook(path, data_only=True)
    pb = ParsedBrief(raw_excel_path=str(path))

    _parse_overview(wb, pb)
    _parse_rufus(wb, pb)
    _parse_reviews(wb, pb)
    _parse_keywords(wb, pb)
    _parse_improvement(wb, pb)
    _parse_modules(wb, pb)

    return pb


def _parse_overview(wb, pb: ParsedBrief) -> None:
    sheet = _find_sheet(wb, "overview product", "overview", "übersicht")
    if not sheet:
        return
    ws = wb[sheet]

    rows = list(_iter_rows(ws, max_rows=120))

    # Header-key → value scan (Field in col C, value in col D)
    KEY_MAP = {
        "exact name": "product_name",
        "produktname": "product_name",
        "amazon asin": "asin",
        "asin": "asin",
        "brand name": "brand",
        "marke": "brand",
        "marketplace": "marketplace",
        "link": "listing_url",
        "perceived main keyword 1": "_kw1",
        "perceived main keyword 2": "_kw2",
        "perceived main keyword 3": "_kw3",
    }
    main_kws: list[str] = []

    for _r, row in rows:
        if len(row) < 4:
            continue
        label = _coerce_str(row[2]).lower()
        value = _coerce_str(row[3])
        if not label or not value:
            continue
        for key, attr in KEY_MAP.items():
            if label.startswith(key):
                if attr.startswith("_kw"):
                    if value and value not in main_kws:
                        main_kws.append(value)
                else:
                    setattr(pb, attr, value)
                break

    pb.main_keywords = main_kws

    # USPs are in col 8 (H), starting near row 9; emotional benefit col 10 (J)
    # Skip header rows: rows 6-8 contain column labels ("Technical Information",
    # "Emotional Benefit", "How can this product help our target group?",
    # "USPs/Properties/Benefits Allgemein") not actual USP content.
    HEADER_BLOCKLIST = {
        "technical information", "emotional benefit", "emotional benefits",
        "how can this product help our target group?", "how can this product help our target group",
        "usps/properties/benefits allgemein", "usps", "properties", "benefits",
        "target group", "problems of target group", "zielgruppe",
    }
    usps_seen = set()
    for _r, row in rows:
        if len(row) < 10:
            continue
        usp = _coerce_str(row[7]) if len(row) >= 8 else ""
        emo = _coerce_str(row[9]) if len(row) >= 10 else ""
        if usp and len(usp) > 8 and usp not in usps_seen and usp.lower() not in HEADER_BLOCKLIST:
            usps_seen.add(usp)
            pb.usps.append(usp)
            pb.technical_info.append(usp)
        if emo and len(emo) > 4 and emo.lower() not in HEADER_BLOCKLIST:
            pb.emotional_benefits.append(emo)

    # Target group & problems live in col 9 (I) near rows 25-28
    for _r, row in rows:
        if len(row) < 9:
            continue
        cell6 = _coerce_str(row[5]).lower() if len(row) >= 6 else ""
        cell9 = _coerce_str(row[8]) if len(row) >= 9 else ""
        if not cell9:
            continue
        if "target group" in cell6 or "zielgruppe" in cell6:
            if "problem" in cell6:
                pb.target_problems = cell9
            else:
                pb.target_group = cell9

    # Competitors are in col D rows 20+ following "Competitor X"
    for _r, row in rows:
        if len(row) < 4:
            continue
        label = _coerce_str(row[2]).lower()
        value = _coerce_str(row[3])
        if label.startswith("competitor ") and value:
            pb.competitors.append({"slot": label, "asin": value})


def _parse_rufus(wb, pb: ParsedBrief) -> None:
    sheet = _find_sheet(wb, "rufus", "qna", "q&a")
    if not sheet:
        return
    ws = wb[sheet]
    for _r, row in _iter_rows(ws, max_rows=60):
        if len(row) < 2:
            continue
        q = _coerce_str(row[0])
        a = _coerce_str(row[2] if len(row) >= 3 and row[2] else (row[1] if len(row) >= 2 else ""))
        if not q or q.lower().startswith("rufus question"):
            continue
        if q and a:
            pb.rufus_qa.append({"q": q, "a": a})


def _parse_reviews(wb, pb: ParsedBrief) -> None:
    sheet = _find_sheet(wb, "review analysis", "reviews")
    if not sheet:
        return
    ws = wb[sheet]
    for _r, row in _iter_rows(ws, max_rows=40):
        if not row:
            continue
        good = _coerce_str(row[0]) if len(row) >= 1 else ""
        bad = _coerce_str(row[2]) if len(row) >= 3 else ""
        if good and not good.lower().startswith("good reviews"):
            pb.good_reviews.append(good)
        if bad and not bad.lower().startswith("bad reviews"):
            pb.bad_reviews.append(bad)


def _parse_keywords(wb, pb: ParsedBrief) -> None:
    """Pull keywords from H10 sheet (col 2 or 3 typically) or from Overview KWS list."""
    h10 = _find_sheet(wb, "h10", "keywords", "kw")
    found: list[str] = []
    if h10:
        ws = wb[h10]
        for r in range(2, min(ws.max_row + 1, 5000)):
            for c in (2, 3, 1):
                v = ws.cell(r, c).value
                if isinstance(v, str) and 3 <= len(v) <= 80 and v.strip() and not v.startswith("="):
                    s = v.strip()
                    if s.lower() not in {"keyword", "phrase", "kw", "search term"} and s not in found:
                        found.append(s)
                        break
            if len(found) >= 200:
                break

    # Also harvest KWS section in Overview (col 3, rows 57+)
    sheet = _find_sheet(wb, "overview")
    if sheet:
        ws = wb[sheet]
        for r in range(55, min(ws.max_row + 1, 200)):
            v = ws.cell(r, 3).value
            if isinstance(v, str) and 3 <= len(v) <= 80 and v.lower() not in {"kws:", "keywords"}:
                if v not in found and not v.lower().startswith("modul"):
                    found.append(v.strip())

    pb.all_keywords = found


def _parse_improvement(wb, pb: ParsedBrief) -> None:
    sheet = _find_sheet(wb, "improvement", "ctr", "cvr")
    if not sheet:
        return
    ws = wb[sheet]
    for _r, row in _iter_rows(ws, max_rows=30):
        if len(row) < 11:
            continue
        ctr = _coerce_str(row[1]) if len(row) >= 2 else ""
        cvr = _coerce_str(row[10]) if len(row) >= 11 else ""
        if ctr and not ctr.lower().startswith("how to improve"):
            pb.ctr_notes.append(ctr)
        if cvr and not cvr.lower().startswith("how to improve"):
            pb.cvr_notes.append(cvr)


def _parse_modules(wb, pb: ParsedBrief) -> None:
    sheet = _find_sheet(wb, "overview")
    if not sheet:
        return
    ws = wb[sheet]
    for r in range(35, min(ws.max_row + 1, 60)):
        label = _coerce_str(ws.cell(r, 3).value)
        choice = _coerce_str(ws.cell(r, 4).value)
        if label.lower().startswith("modul") and choice:
            pb.module_selection.append(f"{label}: {choice}")
        elif label.lower().startswith("modul") and not choice:
            pb.module_selection.append(label)


if __name__ == "__main__":
    import sys
    p = sys.argv[1] if len(sys.argv) > 1 else "/Users/jonask/Desktop/Claude_Code/.tmp/Chekko Oil/02_B09HCSZLP1 - Chekko Castor Oil SEO.xlsx"
    pb = parse_excel(p)
    print("Product:", pb.product_name)
    print("ASIN:", pb.asin)
    print("Brand:", pb.brand)
    print("USPs:", len(pb.usps))
    print("Keywords:", len(pb.all_keywords))
    print("Main KWs:", pb.main_keywords)
    print("RUFUS Q&A:", len(pb.rufus_qa))
    print("Good reviews:", len(pb.good_reviews))
    print("Bad reviews:", len(pb.bad_reviews))
    print("CTR notes:", len(pb.ctr_notes))
    print("CVR notes:", len(pb.cvr_notes))
    print("Modules:", pb.module_selection)
    print("Target group:", pb.target_group[:200] if pb.target_group else "(none)")
    print("Target problems:", pb.target_problems[:200] if pb.target_problems else "(none)")
