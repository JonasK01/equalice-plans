"""Ultra PRO — 3" x 4" Ultra-Clear Toploaders, 210 ct  [Listing 52]
NEUES Format: Titel/Bullets/Backend kommen aus dem SEO-Sheet (listing.xlsx),
Q&A + Vergleich aus dem A+ Premium Sheet (aplus.xlsx). Bildregie handgeschrieben,
100% produktspezifisch, im Ultra-PRO-Katalogstil (schwarz/rot/weiss).

Produkt: rigide, ultra-klare 3" x 4" Toploader (rigid PVC) für Standard-Trading-
Cards 2,5" x 3,5" bis 35pt. Einzelkartenschutz für Lagerung, Display, Trading &
Versand. 210er-Pack für Sports-, Pokémon- & Magic-The-Gathering-Karten.

Marketplace: amazon.com (US). ASIN B08NB19NNP.
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

PLAN_NO = "52"
ASIN = "B08NB19NNP"
EXCEL = HERE / "listing.xlsx"
APLUS = HERE / "aplus.xlsx"


# ===== produktspezifische Bildregie (Ultra-PRO-Katalogstil, EN Overlays) =====

IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="Clean white for slot-1 compliance; the CTR versions add a black lower band with a thin red top-line (Ultra PRO catalog look). Same framing across all 3.",
        purpose="Win the click in a grid of look-alike toploaders. Ship all 3, keep the winner.",
        visual=(
            "Mock ALL 3 options. Product exactly as real: a rigid 3\" x 4\" ultra-clear toploader "
            "holding one generic (non-branded) trading card, plus the 210-count pack behind it. "
            "ONE callout each, product dominant.\n\n"
            "OPTION A — CLARITY: toploader with a colourful card inside, card face crisp through "
            "the rigid film. Badge (red): 'ULTRA CLEAR'.\n"
            "OPTION B — PACK VALUE: the 210-count pack fanned. Badge (red): '210 PACK'.\n"
            "OPTION C — RIGID FIT: single toploader edge-on to show stiffness. Badge: 'RIGID · 35PT'.\n\n"
            "Across all 3: white background, red badge ~6% of frame, same lighting."
        ),
        overlay="(one callout per option)",
        overlay_sub="3 hero options shipped — A/B test, keep the winner.",
        props=["A: card inside toploader", "B: 210-count pack fanned", "C: single toploader edge-on"],
        lighting="Bright, even studio light; crisp catch-light so the ultra-clear rigid film reads on white.",
        why_it_works=(
            "Three triggers: clarity (see your card), pack value (210), rigid fit (35pt). One "
            "callout each — readable at thumbnail size."
        ),
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: ultra-clear, card face stays visible",
        role="hook",
        background="Black with a thin red top-line and a bold white headline (Ultra PRO catalog)",
        purpose="Own the top reason collectors use toploaders: see the card, protect the card.",
        visual=(
            "Large macro: a standard trading card sliding into the ultra-clear rigid toploader, the "
            "card face sharp and true-colour through the transparent plastic. Thin red callout lines: "
            "'rigid PVC', 'crystal-clear', 'view without removing'. White bold headline top: 'SEE IT. "
            "PROTECT IT.'"
        ),
        overlay="ULTRA CLEAR VIEW",
        overlay_sub="Transparent rigid holder shows the card face without removing it.",
        props=["card sliding into toploader (macro)", "red callout lines", "true-colour card face"],
        lighting="Dramatic catalog light on black; strong edge-light on the clear rigid plastic.",
        why_it_works=(
            "Collectors buy toploaders to display AND protect. A true-colour macro proves the plastic "
            "is genuinely ultra-clear — the single strongest visual argument in the category."
        ),
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: rigid PVC structure prevents bending",
        role="educate",
        background="White with a black/red Ultra PRO footer band",
        purpose="Defend quality: why a rigid structure matters for single-card protection.",
        visual=(
            "Split card. LEFT: a card in the toploader with a small shield icon 'RIGID SUPPORT'. RIGHT: "
            "three stacked feature rows with red check-icons — 'RIGID PVC — sturdy, holds its shape', "
            "'Guards against bending and handling marks', 'Protects during everyday storage'. "
            "Footer band: 'Time-tested card protection — trusted since 1952.'"
        ),
        overlay="RIGID PROTECTION",
        overlay_sub="Rigid PVC guards against bending, handling marks and everyday wear.",
        props=["card in toploader", "3 feature rows with red checks", "since-1952 footer band"],
        lighting="Flat, even catalog light; feature icons legible at thumbnail size.",
        why_it_works=(
            "Serious collectors filter on protection strength. Naming the rigid structure with a "
            "clear 'why it matters' separates this from flimsy bargain holders."
        ),
    ),
    AIImagePlanItem(
        name="Image 4 — Fit: sized for standard trading cards",
        role="desire",
        background="White with a red dimension callout (Ultra PRO)",
        purpose="Remove the top buyer question — will my cards fit?",
        visual=(
            "A standard trading card centred in the 3\" x 4\" toploader with a clean dimension callout: "
            "'Fits standard 2.5\" x 3.5\" cards, up to 35pt'. Small ruler graphic along two edges. A "
            "short note: 'Snug, secure fit — sports, Pokemon and Magic cards.'"
        ),
        overlay="FITS STANDARD CARDS",
        overlay_sub="Sized for 2.5\" x 3.5\" cards up to 35pt — snug, secure fit.",
        props=["card in toploader", "dimension callout 3\" x 4\"", "edge ruler graphic"],
        lighting="Bright, even; the dimension callout must read clearly.",
        why_it_works=(
            "Wrong-size or too-thin holders are a top return reason in this category. A precise fit "
            "and 35pt callout set honest expectations and prevent mis-buys."
        ),
    ),
    AIImagePlanItem(
        name="Image 5 — Pack: 210 count for collection & shop",
        role="desire",
        background="Black with red accents (Ultra PRO catalog)",
        purpose="Make the pack value and use-cases obvious.",
        visual=(
            "The 210-count pack with several carded toploaders organised in a short row. Icon-stats: "
            "'210 TOPLOADERS', 'Store new pulls', 'Ship safely', 'Trade and display'. Clean, "
            "catalog-style layout."
        ),
        overlay="210 TOPLOADERS",
        overlay_sub="Sort, store, ship and trade sports and gaming cards with ease.",
        props=["210-count pack", "carded toploaders in a row", "4 icon-stats"],
        lighting="Catalog light on black; product and stats clearly separated.",
        why_it_works=(
            "Shows the quantity is a working tool, not just a number — speaks to collectors, "
            "hobbyists and card shops alike."
        ),
    ),
    AIImagePlanItem(
        name="Image 6 — Trust: Ultra PRO, trusted since 1952",
        role="trust",
        background="Black with red top-line, white headline (brand close)",
        purpose="Close on brand authority — the collector's default choice.",
        visual=(
            "Hero of the pack with a small lifestyle inset (a collector sleeving cards at a tidy "
            "desk). Brand line bottom: 'ULTRA PRO — protecting collections since 1952 · made in USA'. "
            "Red badge: 'SINCE 1952'."
        ),
        overlay="TRUSTED SINCE 1952",
        overlay_sub="Ultra PRO — protecting card collections, made in USA.",
        props=["pack hero", "collector lifestyle inset", "since-1952 red badge"],
        lighting="Premium catalog light on black; warm inset for the lifestyle moment.",
        why_it_works=(
            "Against unbranded bargain holders, heritage and trust are the deciding signals. 'Since "
            "1952' and 'made in USA' are Ultra PRO's honest, compliant authority claims."
        ),
    ),
    AIImagePlanItem(
        name="Image 7 — Range: the Ultra PRO card protection system",
        role="close",
        background="White with black/red Ultra PRO chrome",
        purpose="Cross-sell the wider card-protection range.",
        visual=(
            "Clean line-up: toploaders (this product) alongside card sleeves, 9-pocket binder pages "
            "and a storage organizer — shown as a coordinated system. Small labels; the toploaders "
            "gently highlighted. Caption: 'Sleeve it. Load it. Store it. — the Ultra PRO way.'"
        ),
        overlay="PROTECT EVERY CARD",
        overlay_sub="Pair toploaders with sleeves, binder pages and storage boxes.",
        props=["toploaders (highlighted)", "card sleeves", "9-pocket pages", "storage organizer"],
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
        headline="SEE IT. PROTECT IT. SINCE 1952.",
        body=(
            "Ultra-clear rigid 3\" x 4\" toploaders hold standard 2.5\" x 3.5\" cards up to 35pt, "
            "guarding against bending, handling marks and everyday wear. Rigid PVC card protection "
            "trusted by collectors since 1952."
        ),
        visual="Wide black banner, red top-line, bold white headline left; a carded toploader with a crisp card face right. Ultra PRO logo upper-left.",
        alt="Ultra PRO 3x4 toploaders banner: ultra-clear rigid card protection, since 1952.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): Why these toploaders",
        role="a+_carousel",
        headline="WHY ULTRA PRO TOPLOADERS",
        body=(
            "Tile 1: <b>ULTRA CLEAR</b> — Card face and art stay fully visible.<br/>"
            "Tile 2: <b>RIGID PVC</b> — Sturdy structure holds its shape.<br/>"
            "Tile 3: <b>STANDARD FIT</b> — 2.5\" x 3.5\" cards, up to 35pt.<br/>"
            "Tile 4: <b>210-COUNT PACK</b> — For larger card collections.<br/>"
            "Tile 5: <b>SINCE 1952</b> — Trusted card protection worldwide."
        ),
        visual="5 square tiles, red accent corner each, black/white icons (film · shield · ruler · stack · badge).",
        alt="Five A+ tiles: ultra-clear, rigid PVC, standard fit, 210-count, since 1952.",
    ),
    AIModule(
        name="Module 3 — Banner: Rigid protection, ship-ready",
        role="a+_banner",
        headline="RIGID. CLEAR. SHIP-READY.",
        body=(
            "Made from rigid PVC with a clear transparent design, these toploaders keep cards flat and "
            "protected during storage, display, trading and shipping. View sports &amp; gaming cards "
            "without removing them from the holder."
        ),
        visual="Banner split: macro of the rigid clear plastic + a card held flat left; a row of carded toploaders ready to ship right. Black/red Ultra PRO styling.",
        alt="A+ banner on rigid, ultra-clear card protection ready for storage and shipping.",
    ),
    AIModule(
        name="Module 4 — Carousel (4 tiles): The card protection system",
        role="a+_carousel",
        headline="SLEEVE IT. LOAD IT. STORE IT.",
        body=(
            "Tile 1: <b>TOPLOADERS</b> — Rigid ultra-clear card holders (this product).<br/>"
            "Tile 2: <b>CARD SLEEVES</b> — Soft first layer inside the toploader.<br/>"
            "Tile 3: <b>9-POCKET PAGES</b> — Display and organise sets in a binder.<br/>"
            "Tile 4: <b>STORAGE ORGANIZER</b> — Archive full collections."
        ),
        visual="4 coordinated product tiles, red accent corners, consistent catalog styling.",
        alt="Four A+ tiles showing the Ultra PRO card protection system: toploaders, sleeves, pages, organizer.",
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
