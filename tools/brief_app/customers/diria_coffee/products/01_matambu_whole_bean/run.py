"""CAFÉ DIRIÁ — Proceso Matambú, WHOLE BEAN  [Variant 01]
SEO title/bullets/backend 1:1 from the 'SEO_Costa Rica Coffee Diria Pro' tab; bildregie +
A+ shared via _diria_common (fmt='whole_bean'). Marketplace amazon.com (EN). new_brand=true.
ASIN not supplied yet -> filename placeholder 'WHOLE-BEAN'.
"""
from __future__ import annotations
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools/brief_app/customers/ultra_pro"))   # seo_loader
sys.path.insert(0, str(HERE.parent))                                    # _diria_common

from tools.brief_app.core.customers import load_customer
from tools.brief_app.core.excel_parser import parse_excel
from tools.brief_app.core.pdf_builder import BriefBuilder
import seo_loader as SEOL
import _diria_common as DIRIA

PLAN_NO = "01"
ASIN = "WHOLE-BEAN"
SEO_SHEET = "SEO_Costa Rica Coffee Diria Pro"
FORMAT = "whole_bean"
PRODUCT_NAME = "Diriá Proceso Matambú — Whole Bean (340 g)"
EXCEL = HERE / "listing.xlsx"


def main() -> None:
    print("Lade CAFÉ DIRIÁ + SEO-Sheet (Whole Bean)…")
    cust = load_customer("diria_coffee")
    brief = parse_excel(EXCEL)
    brief.product_name = PRODUCT_NAME
    brief.all_keywords = SEOL.scrub_keywords(brief.all_keywords)
    brief.main_keywords = SEOL.scrub_keywords(brief.main_keywords)
    seo = SEOL.load_seo(EXCEL, sheet=SEO_SHEET)
    images, modules, qa = DIRIA.build(FORMAT)
    OUT = HERE / f"{PLAN_NO}_{ASIN}_Image Plan.pdf"
    print(f"  Produkt: {brief.product_name}  ASIN: {ASIN}  Marktplatz: {cust.marketplace}")
    print(f"  SEO-Titel({len(seo.title)}) + Bullets={len(seo.bullets)} | new_brand={cust.new_brand}")

    builder = BriefBuilder(cust, brief, OUT, ai=None)
    builder._ai_title = seo.title
    builder._ai_bullets = SEOL.as_bullets_html(seo)
    builder._ai_images = images
    builder._ai_modules = list(modules)
    builder._ai_qa = qa
    builder._ai_backend = seo.backend
    builder.copy_source_label = "SEO sheet (title/bullets/backend) + hand-written bildregie (EN)"

    print("Baue Branded PDF…")
    pdf_path = builder.build()
    size_kb = pdf_path.stat().st_size // 1024
    import re
    pages = len(re.findall(rb'/Type\s*/Page[^s]', pdf_path.read_bytes()))
    print(f"Gebaut: {pdf_path}")
    print(f"  Seiten: {pages}  Größe: {size_kb} KB")


if __name__ == "__main__":
    main()
