"""Ultra PRO — Snorlax & Munchlax 9-Pocket PRO-Binder  [Listing 62]
NEUES Format: Titel/Bullets/Backend kommen aus dem SEO-Sheet (listing.xlsx),
Q&A + Vergleich aus dem A+ Premium Sheet (aplus.xlsx). Bildregie handgeschrieben,
100% produktspezifisch, im Ultra-PRO-Katalogstil (schwarz/rot/weiss) mit farbigem
Lizenz-Cover (Snorlax/Munchlax) als Hero.

Marketplace: amazon.com (US). ASIN B09TD2C2NL.
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

PLAN_NO = "62"
ASIN = "B09TD2C2NL"
EXCEL = HERE / "listing.xlsx"
APLUS = HERE / "aplus.xlsx"


# ===== produktspezifische Bildregie (Ultra-PRO-Katalogstil, EN Overlays) =====

IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="Clean white for slot-1 compliance; the CTR versions add a black lower band with a thin red top-line (Ultra PRO catalog look). Same framing across all 3.",
        purpose="Win the click in a grid of look-alike card binders — lead with the licensed Snorlax & Munchlax cover.",
        visual=(
            "Mock ALL 3 options. Product exactly as real: the closed 9-pocket PRO-Binder showing "
            "the full-colour, officially licensed Snorlax & Munchlax cover art, with the elastic "
            "strap closure visible. ONE callout each, product dominant.\n\n"
            "OPTION A — LICENSE COVER: front-on hero of the full-art Snorlax & Munchlax cover in "
            "full colour. Badge (red): 'OFFICIALLY LICENSED'.\n"
            "OPTION B — CAPACITY: binder open to a 9-pocket page with real Pokémon cards inside. "
            "Badge (red): 'HOLDS 360 CARDS'.\n"
            "OPTION C — FORMAT: binder with a small side-load pocket + strap icon. Badge (red): "
            "'9-POCKET · SIDE-LOAD'.\n\n"
            "Across all 3: white background, colourful licensed cover, red badge ~6% of frame, "
            "same lighting. Cards shown are real Pokémon cards."
        ),
        overlay="(one callout per option)",
        overlay_sub="3 hero options shipped — A/B test, keep the winner.",
        props=["A: licensed Snorlax & Munchlax cover hero", "B: open 9-pocket page with real cards", "C: binder + side-load/strap icon"],
        lighting="Bright, even studio light; crisp catch-light so the licensed cover art reads true-colour on white.",
        why_it_works=(
            "Three triggers: the licensed character cover (fan pull), 360-card capacity, and the "
            "9-pocket side-load format. One callout each — readable at thumbnail size."
        ),
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: Officially licensed Snorlax & Munchlax cover",
        role="hook",
        background="Black with a thin red top-line and a bold white headline (Ultra PRO catalog)",
        purpose="Own the #1 buy reason for a themed binder: the officially licensed full-art cover.",
        visual=(
            "Large hero: the closed binder showing the full-colour Snorlax & Munchlax full-art "
            "cover, edge-lit so the artwork pops. Thin red callout lines: 'Officially licensed "
            "Pokémon', 'full-art cover design', 'display-ready look'. White bold headline top: "
            "'BUILT FOR THE FANDOM.'"
        ),
        overlay="OFFICIALLY LICENSED.",
        overlay_sub="Full-art Snorlax and Munchlax cover — an officially licensed Pokémon binder.",
        props=["closed binder, licensed full-art cover", "red callout lines", "true-colour character art"],
        lighting="Dramatic catalog light on black; strong edge-light on the colourful cover.",
        why_it_works=(
            "For a themed portfolio the licensed character art is the emotional hook. A true-colour "
            "hero of the official Snorlax & Munchlax cover is the strongest single argument."
        ),
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: 9-pocket layout, side-loading pockets",
        role="educate",
        background="White with a black/red Ultra PRO footer band",
        purpose="Explain the format: 9 pockets per page, secure side-loading, easy access.",
        visual=(
            "Split card. LEFT: the binder open to a full 9-pocket page with real Pokémon cards, a "
            "small icon '9 PER PAGE'. RIGHT: three stacked feature rows with red check-icons — "
            "'SIDE-LOADING pockets keep cards positioned', 'LOW-FRICTION material for easy access', "
            "'Fits standard-size cards, including sleeved'. Footer band: 'Card protection trusted "
            "since 1952.'"
        ),
        overlay="SECURE SIDE LOADING.",
        overlay_sub="Side-loading pockets keep cards positioned during browsing and transport.",
        props=["open 9-pocket page with real cards", "3 feature rows with red checks", "since-1952 footer band"],
        lighting="Flat, even catalog light; feature icons legible at thumbnail size.",
        why_it_works=(
            "Side-loading vs top-loading is a real decision point for collectors. Showing the 9-per-"
            "page layout and side-load pockets answers the format question up front."
        ),
    ),
    AIImagePlanItem(
        name="Image 4 — Capacity: holds up to 360 cards",
        role="desire",
        background="White with a red capacity callout (Ultra PRO)",
        purpose="Make the 360-card capacity concrete and remove the 'how much fits' question.",
        visual=(
            "The binder fanned open across several 9-pocket pages, filled with real Pokémon cards, "
            "with a clean callout: 'Holds up to 360 standard-size cards'. A small note: 'Room for "
            "sets, duplicates and favourites — including sleeved cards.' Optional stack graphic "
            "showing the pages building up to 360."
        ),
        overlay="HOLDS 360 CARDS.",
        overlay_sub="Room for up to 360 standard-size cards, including cards stored in sleeves.",
        props=["binder fanned open, pages of real cards", "360-card capacity callout", "page-stack graphic"],
        lighting="Bright, even; the capacity callout must read clearly.",
        why_it_works=(
            "Capacity is the top spec buyers compare on portfolios. A concrete 360 number with the "
            "sleeved-card note sets honest expectations and prevents mis-buys."
        ),
    ),
    AIImagePlanItem(
        name="Image 5 — Archival-safe pages & elastic strap",
        role="desire",
        background="Black with red accents (Ultra PRO catalog)",
        purpose="Defend quality: acid-free, non-PVC pages plus the elastic strap closure.",
        visual=(
            "The binder standing with the elastic strap closure fastened, next to a macro of a "
            "page edge. Icon-stats: 'ACID-FREE', 'NON-PVC pages', 'ELASTIC STRAP closure', "
            "'Store & transport'. Clean, catalog-style layout."
        ),
        overlay="ACID-FREE. NON-PVC.",
        overlay_sub="Archival-safe acid-free, non-PVC pages with a secure elastic strap closure.",
        props=["binder with elastic strap fastened", "macro of page edge", "4 icon-stats"],
        lighting="Catalog light on black; product and stats clearly separated.",
        why_it_works=(
            "Serious collectors filter on archival safety. Naming acid-free + non-PVC and showing "
            "the strap closure signals long-term, travel-ready card care."
        ),
    ),
    AIImagePlanItem(
        name="Image 6 — Trust: Ultra PRO, trusted since 1952",
        role="trust",
        background="Black with red top-line, white headline (brand close)",
        purpose="Close on brand authority — the collector's default choice.",
        visual=(
            "Hero of the binder with a small lifestyle inset (a collector filing Pokémon cards at a "
            "tidy desk). Brand line bottom: 'ULTRA PRO — protecting collections since 1952 · trusted "
            "by collectors worldwide'. Red badge: 'SINCE 1952'."
        ),
        overlay="TRUSTED SINCE 1952.",
        overlay_sub="Ultra PRO — protecting trading card collections worldwide.",
        props=["binder hero", "collector lifestyle inset", "since-1952 red badge"],
        lighting="Premium catalog light on black; warm inset for the lifestyle moment.",
        why_it_works=(
            "Against unbranded binders, heritage and trust are the deciding signals. 'Since 1952' is "
            "Ultra PRO's honest, compliant authority claim."
        ),
    ),
    AIImagePlanItem(
        name="Image 7 — Range: the Ultra PRO card storage system",
        role="close",
        background="White with black/red Ultra PRO chrome",
        purpose="Cross-sell the wider card-protection range.",
        visual=(
            "Clean line-up: the 9-pocket PRO-Binder (this product) alongside deck protector sleeves, "
            "a graded card case and a 9-pocket portfolio — shown as a coordinated system. Small "
            "labels; the binder gently highlighted. Caption: 'Sleeve it. File it. Show it. — the "
            "Ultra PRO way.'"
        ),
        overlay="STORE IT. SHOW IT.",
        overlay_sub="Pair with Ultra PRO deck sleeves, graded card cases and portfolios.",
        props=["9-pocket binder (highlighted)", "deck protector sleeves", "graded card case", "9-pocket portfolio"],
        lighting="Bright, even; coordinated family shot.",
        why_it_works=(
            "Turns one purchase into a system sale and reinforces Ultra PRO as the one-stop collector "
            "brand for cards."
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
            "Officially licensed Pokémon 9-Pocket PRO-Binder featuring Snorlax &amp; Munchlax full-art "
            "cover design. Holds up to 360 standard-size cards on acid-free, non-PVC pages, with "
            "secure side-loading pockets and an elastic strap closure — collectible card storage "
            "trusted since 1952."
        ),
        visual="Wide black banner, red top-line, bold white headline left; the licensed Snorlax & Munchlax cover in full colour right. Ultra PRO logo upper-left.",
        alt="Ultra PRO Snorlax and Munchlax 9-pocket PRO-Binder banner: officially licensed, 360 cards, since 1952.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): Why this binder",
        role="a+_carousel",
        headline="WHY THIS ULTRA PRO BINDER",
        body=(
            "Tile 1: <b>LICENSED COVER</b> — Officially licensed Snorlax &amp; Munchlax full-art design.<br/>"
            "Tile 2: <b>360 CARDS</b> — Space for growing collections, including sleeved cards.<br/>"
            "Tile 3: <b>SIDE-LOADING</b> — Pockets keep cards positioned during handling.<br/>"
            "Tile 4: <b>ARCHIVAL-SAFE</b> — Acid-free, non-PVC pages plus elastic strap closure.<br/>"
            "Tile 5: <b>SINCE 1952</b> — Collectible card storage trusted worldwide."
        ),
        visual="5 square tiles, red accent corner each, black/white icons (character cover · stack · side-load pocket · shield · badge).",
        alt="Five A+ tiles: licensed cover, 360 cards, side-loading, acid-free/non-PVC, since 1952.",
    ),
    AIModule(
        name="Module 3 — Banner: Archival protection",
        role="a+_banner",
        headline="ARCHIVAL-SAFE. EVERY PAGE.",
        body=(
            "Built from acid-free, non-PVC pages so your cards stay protected for the long term. The "
            "elastic strap closure keeps the binder securely shut for storage and transport — file "
            "standard-size cards, including sleeved cards, and take your collection anywhere."
        ),
        visual="Banner split: macro of a page edge + acid-free / non-PVC shield icons left; the binder with elastic strap fastened right. Black/red Ultra PRO styling.",
        alt="A+ banner on archival-safe acid-free, non-PVC pages with elastic strap closure.",
    ),
    AIModule(
        name="Module 4 — Carousel (4 tiles): The card storage system",
        role="a+_carousel",
        headline="SLEEVE IT. FILE IT. SHOW IT.",
        body=(
            "Tile 1: <b>9-POCKET BINDER</b> — Licensed Snorlax &amp; Munchlax PRO-Binder (this product).<br/>"
            "Tile 2: <b>DECK SLEEVES</b> — Protect cards before you file them.<br/>"
            "Tile 3: <b>GRADED CARD CASES</b> — Hard-shell protection for key slabs.<br/>"
            "Tile 4: <b>9-POCKET PORTFOLIOS</b> — Grow the collection across more themes."
        ),
        visual="4 coordinated product tiles, red accent corners, consistent catalog styling.",
        alt="Four A+ tiles showing the Ultra PRO card storage system: binder, sleeves, graded cases, portfolios.",
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
