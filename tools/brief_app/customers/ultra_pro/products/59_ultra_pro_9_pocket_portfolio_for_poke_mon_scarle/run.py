"""Ultra PRO — 9-Pocket Portfolio for Pokémon Scarlet & Violet  [Listing 59]
NEUES Format: Titel/Bullets/Backend kommen aus dem SEO-Sheet (listing.xlsx),
Q&A + Vergleich aus dem A+ Premium Sheet (aplus.xlsx). Bildregie handgeschrieben,
100% produktspezifisch, im Ultra-PRO-Katalogstil (schwarz/rot/weiss, Lizenz-Cover farbig).

Marketplace: amazon.com (US). ASIN B0CTMRMJJM.
"""
from __future__ import annotations
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(HERE.parents[1]))   # customers/ultra_pro  (für seo_loader)

from tools.brief_app.core.customers import load_customer
from tools.brief_app.core.excel_parser import parse_excel
from tools.brief_app.core.pdf_builder import BriefBuilder
from tools.brief_app.core.ai import AIImagePlanItem, AIModule
import seo_loader as SEOL

PLAN_NO = "59"
ASIN = "B0CTMRMJJM"
EXCEL = HERE / "listing.xlsx"
APLUS = HERE / "aplus.xlsx"


# ===== produktspezifische Bildregie (Ultra-PRO-Katalogstil, EN Overlays) =====

IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="Clean white for slot-1 compliance; the CTR versions add a black lower band with a thin red top-line (Ultra PRO catalog look). Same framing across all 3.",
        purpose="Win the click in a grid of look-alike card binders. Ship all 3, keep the winner.",
        visual=(
            "Mock ALL 3 options. Product exactly as real: the 9-pocket Pokémon Scarlet & Violet "
            "portfolio, closed, showing the officially licensed full-art cover (Shiny Pikachu, "
            "Shiny Dondozo, Shiny Curly Form Tatsugiri). ONE callout each, product dominant.\n\n"
            "OPTION A — LICENSE: closed binder, colourful full-art cover front and centre. Badge "
            "(red): 'OFFICIALLY LICENSED'.\n"
            "OPTION B — CAPACITY: binder open one page, real Pokémon cards in the 9 pockets. Badge "
            "(red): 'HOLDS 252 CARDS'.\n"
            "OPTION C — PAGES: fanned high-clarity pages visible. Badge: '14 HIGH-CLARITY PAGES'.\n\n"
            "Across all 3: white background, red badge ~6% of frame, same lighting."
        ),
        overlay="(one callout per option)",
        overlay_sub="3 hero options shipped — A/B test, keep the winner.",
        props=["A: closed binder, full-art cover", "B: open page with real Pokémon cards", "C: fanned high-clarity pages"],
        lighting="Bright, even studio light; crisp catch-light so the licensed cover art reads true-colour on white.",
        why_it_works=(
            "Three triggers: the licensed cover collectors recognise, capacity (252), and the "
            "high-clarity pages. One callout each — readable at thumbnail size."
        ),
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: officially licensed Scarlet & Violet cover",
        role="hook",
        background="Black with a thin red top-line and a bold white headline (Ultra PRO catalog)",
        purpose="Own the #1 reason collectors pick this binder: the officially licensed full-art cover.",
        visual=(
            "Large hero of the closed binder, the full-art Scarlet & Violet cover crisp and "
            "true-colour — Shiny Pikachu, Shiny Dondozo and Shiny Curly Form Tatsugiri clearly "
            "recognisable. Thin red callout lines: 'officially licensed', 'full-art cover', "
            "'Scarlet & Violet'. White bold headline top: 'BUILT FOR THE FANDOM.'"
        ),
        overlay="OFFICIALLY LICENSED.",
        overlay_sub="Full-art Scarlet & Violet cover with Shiny Pikachu, Dondozo and Tatsugiri.",
        props=["closed binder hero", "full-art licensed cover", "red callout lines"],
        lighting="Dramatic catalog light on black; strong edge-light so the colourful cover pops.",
        why_it_works=(
            "In a grid of plain binders, an officially licensed full-art cover is the strongest "
            "recognition and desire signal for Pokémon collectors."
        ),
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: 9 pockets, up to 252 cards",
        role="educate",
        background="White with a black/red Ultra PRO footer band",
        purpose="Make the capacity concrete — the #1 practical question for a portfolio.",
        visual=(
            "Split card. LEFT: an open 9-pocket page filled with real Pokémon cards, a small red "
            "badge '9 POCKETS'. RIGHT: three stacked feature rows with red check-icons — "
            "'126 cards single-loaded', '252 cards double-loaded', '14 high-clarity pages'. "
            "Footer band: 'Organise a growing collection — trusted since 1952.'"
        ),
        overlay="HOLDS UP TO 252 CARDS.",
        overlay_sub="126 single-loaded or 252 double-loaded standard cards across 14 pages.",
        props=["open 9-pocket page with cards", "3 feature rows with red checks", "since-1952 footer band"],
        lighting="Flat, even catalog light; feature icons legible at thumbnail size.",
        why_it_works=(
            "Capacity drives the buy decision for binders. Showing both single- and double-load "
            "numbers on real cards sets honest, high-value expectations."
        ),
    ),
    AIImagePlanItem(
        name="Image 4 — Fit: high-clarity pages, secure side-loading pockets",
        role="desire",
        background="White with a red callout (Ultra PRO)",
        purpose="Sell the everyday experience: see every card, keep every card secure.",
        visual=(
            "Macro of a single high-clarity pocket with a Pokémon card fully visible through the "
            "film, plus an inset arrow showing a card entering from the side into a side-loading "
            "pocket. Callouts: 'high-clarity view', 'side-loading pockets', 'view without removing "
            "cards'. Short note: 'Secure side-load keeps cards seated.'"
        ),
        overlay="SEE EVERY CARD.",
        overlay_sub="High-clarity pages and side-loading pockets — view cards without removing them.",
        props=["macro of card in high-clarity pocket", "side-load entry arrow inset", "callout lines"],
        lighting="Bright, even; strong edge-light so the clear film and card detail read.",
        why_it_works=(
            "Collectors want to display and browse without handling cards. Proving clarity plus "
            "secure side-loading answers the two things that make a portfolio feel premium."
        ),
    ),
    AIImagePlanItem(
        name="Image 5 — Educate: archival-safe, acid-free & non-PVC",
        role="desire",
        background="Black with red accents (Ultra PRO catalog)",
        purpose="Defend quality: why acid-free + non-PVC pages matter for long-term card storage.",
        visual=(
            "The binder open beside icon-stats on black: 'ARCHIVAL-SAFE polypropylene', 'ACID-FREE', "
            "'NON-PVC (no plasticiser migration)', 'MADE IN CALIFORNIA, U.S.A.'. A small shield icon "
            "ties the row together. Clean, catalog-style layout."
        ),
        overlay="ACID-FREE. NON-PVC.",
        overlay_sub="Archival-safe polypropylene pages for long-term Pokémon card storage.",
        props=["open binder", "4 icon-stats", "archival shield icon"],
        lighting="Catalog light on black; product and stats clearly separated.",
        why_it_works=(
            "Serious collectors filter on archival safety. Naming acid-free + non-PVC with a clear "
            "'why it matters' separates this from unlabeled bargain binders."
        ),
    ),
    AIImagePlanItem(
        name="Image 6 — Trust: Ultra PRO, trusted since 1952",
        role="trust",
        background="Black with red top-line, white headline (brand close)",
        purpose="Close on brand authority — the collector's default choice.",
        visual=(
            "Hero of the binder with a small lifestyle inset (a collector sliding cards into the "
            "portfolio at a tidy desk). Brand line bottom: 'ULTRA PRO — protecting collections since "
            "1952 · made in California, U.S.A.'. Red badge: 'SINCE 1952'."
        ),
        overlay="TRUSTED SINCE 1952.",
        overlay_sub="Ultra PRO — made in California, U.S.A., protecting collectors since 1952.",
        props=["binder hero", "collector lifestyle inset", "since-1952 red badge"],
        lighting="Premium catalog light on black; warm inset for the lifestyle moment.",
        why_it_works=(
            "Against unbranded bargain binders, heritage and trust are the deciding signals. 'Since "
            "1952' and 'made in the U.S.A.' are Ultra PRO's honest, compliant authority claims."
        ),
    ),
    AIImagePlanItem(
        name="Image 7 — Range: the Ultra PRO Pokémon storage system",
        role="close",
        background="White with black/red Ultra PRO chrome",
        purpose="Cross-sell the wider card-protection range.",
        visual=(
            "Clean line-up: the 9-pocket portfolio (this product) alongside deck-protector sleeves, "
            "toploaders and a card storage box — shown as a coordinated system. Small labels; the "
            "portfolio gently highlighted. Caption: 'Sleeve it. Store it. Show it. — the Ultra PRO way.'"
        ),
        overlay="BINDER. SLEEVES. MORE.",
        overlay_sub="Pair with Ultra PRO deck sleeves, toploaders and card storage boxes.",
        props=["9-pocket portfolio (highlighted)", "deck-protector sleeves", "toploaders", "card storage box"],
        lighting="Bright, even; coordinated family shot.",
        why_it_works=(
            "Turns one purchase into a system sale and reinforces Ultra PRO as the one-stop "
            "collector brand."
        ),
    ),
]


# ===== 4 kreative Module + Q&A/Vergleich aus dem A+ Sheet =====

CREATIVE_MODULES = [
    AIModule(
        name="Module 1 — Brand banner",
        role="a+_banner",
        headline="OFFICIALLY LICENSED. SINCE 1952.",
        body=(
            "An officially licensed Pokémon Scarlet &amp; Violet 9-pocket portfolio with a full-art "
            "cover of Shiny Pikachu, Shiny Dondozo and Shiny Curly Form Tatsugiri. Holds up to 252 "
            "cards across 14 high-clarity, acid-free, non-PVC pages — card storage trusted by "
            "collectors since 1952."
        ),
        visual="Wide black banner, red top-line, bold white headline left; the closed binder with its colourful full-art cover right. Ultra PRO logo upper-left.",
        alt="Ultra PRO 9-pocket Pokémon Scarlet and Violet portfolio banner: officially licensed, 252 cards, since 1952.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): Why this portfolio",
        role="a+_carousel",
        headline="WHY THIS ULTRA PRO PORTFOLIO",
        body=(
            "Tile 1: <b>OFFICIALLY LICENSED</b> — Full-art Scarlet &amp; Violet cover.<br/>"
            "Tile 2: <b>UP TO 252 CARDS</b> — 126 single- or 252 double-loaded.<br/>"
            "Tile 3: <b>14 HIGH-CLARITY PAGES</b> — View cards without removing them.<br/>"
            "Tile 4: <b>ACID-FREE &amp; NON-PVC</b> — Archival-safe polypropylene pages.<br/>"
            "Tile 5: <b>SINCE 1952</b> — Trusted card protection, made in the U.S.A."
        ),
        visual="5 square tiles, red accent corner each, black/white icons (badge · pockets · page · shield · seal).",
        alt="Five A+ tiles: officially licensed, 252 cards, 14 high-clarity pages, acid-free non-PVC, since 1952.",
    ),
    AIModule(
        name="Module 3 — Banner: Archival card protection",
        role="a+_banner",
        headline="SEE EVERY CARD. KEEP EVERY CARD.",
        body=(
            "High-clarity pages let collectors view artwork and details without removing cards, "
            "while side-loading pockets keep them securely seated. Made from acid-free, non-PVC "
            "polypropylene so there is no plasticiser migration onto your cards."
        ),
        visual="Banner split: macro of a card in a high-clarity pocket + side-load arrow left; the open 9-pocket page filled with cards right. Black/red Ultra PRO styling.",
        alt="A+ banner on high-clarity, side-loading, acid-free non-PVC Pokémon card protection.",
    ),
    AIModule(
        name="Module 4 — Carousel (4 tiles): The card storage system",
        role="a+_carousel",
        headline="SLEEVE IT. STORE IT. SHOW IT.",
        body=(
            "Tile 1: <b>9-POCKET PORTFOLIO</b> — Officially licensed binder (this product).<br/>"
            "Tile 2: <b>DECK SLEEVES</b> — Protect single cards before they go in.<br/>"
            "Tile 3: <b>TOPLOADERS</b> — Rigid protection for key cards.<br/>"
            "Tile 4: <b>STORAGE BOXES</b> — Organise and archive full collections."
        ),
        visual="4 coordinated product tiles, red accent corners, consistent catalog styling.",
        alt="Four A+ tiles showing the Ultra PRO card storage system: portfolio, sleeves, toploaders, boxes.",
    ),
]


def main() -> None:
    print(f"Lade Ultra PRO + SEO/A+ Sheets für Listing {PLAN_NO}…")
    cust = load_customer("ultra_pro")
    brief = parse_excel(EXCEL)
    seo = SEOL.load_seo(EXCEL)
    ap = SEOL.load_aplus(APLUS)
    OUT = HERE / f"{PLAN_NO}_{ASIN}_Image Plan.pdf"
    print(f"  SEO-Titel ({len(seo.title)} chars): {seo.title[:70]}…")
    print(f"  Bullets={len(seo.bullets)}  Q&A={len(ap.qa)}  Vergleich-Zeilen={len(ap.comp_rows)}")

    modules = list(CREATIVE_MODULES)
    if ap.qa:
        modules.append(SEOL.qa_module(ap, headline="COLLECTOR Q&A"))
    if ap.comp_rows:
        modules.append(SEOL.comparison_module(ap))

    builder = BriefBuilder(cust, brief, OUT, ai=None)
    builder._ai_title = seo.title                       # SEO-Titel 1:1 (wird ge-esc't)
    builder._ai_bullets = SEOL.as_bullets_html(seo)     # SEO-Bullets -> Haus-Stil
    builder._ai_images = IMAGES
    builder._ai_modules = modules
    builder._ai_qa = SEOL.as_qa(ap)
    builder._ai_backend = seo.backend
    builder.copy_source_label = "SEO-Sheet (Titel/Bullets/Backend) + A+ Sheet (Q&A/Vergleich); Bildregie hand-written"

    print("Baue Branded PDF…")
    pdf_path = builder.build()
    size_kb = pdf_path.stat().st_size // 1024
    import re
    pages = len(re.findall(rb'/Type\s*/Page[^s]', pdf_path.read_bytes()))
    print(f"Gebaut: {pdf_path}")
    print(f"  Seiten: {pages}  Größe: {size_kb} KB")


if __name__ == "__main__":
    main()
