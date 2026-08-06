"""Ultra PRO — Ultra Clear Toploaders 3" x 4" (420 Count)  [Listing 55]
NEUES Format: Titel/Bullets/Backend kommen aus dem SEO-Sheet (listing.xlsx),
Q&A + Vergleich aus dem A+ Premium Sheet (aplus.xlsx). Bildregie handgeschrieben,
100% produktspezifisch, im Ultra-PRO-Katalogstil (schwarz/rot/weiss).

Marketplace: amazon.com (US). ASIN B08Q66KXXH.
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

PLAN_NO = "55"
ASIN = "B08Q66KXXH"
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
            "holding a generic (non-branded) standard trading card, plus the 420-count bulk pack "
            "behind it. ONE callout each, product dominant.\n\n"
            "OPTION A — CLARITY: single toploader with a colourful card inside, artwork crisp "
            "through the rigid film. Badge (red): 'ULTRA-CLEAR RIGID'.\n"
            "OPTION B — BULK VALUE: the 420-count pack shown as 12 sealed 35-count sleeves fanned. "
            "Badge (red): '420 COUNT PACK'.\n"
            "OPTION C — PROTECTION: toploader + small rigid / no-bend icons. Badge: 'FITS UP TO "
            "35PT'.\n\n"
            "Across all 3: white background, red badge ~6% of frame, same lighting."
        ),
        overlay="(one callout per option)",
        overlay_sub="3 hero options shipped — A/B test, keep the winner.",
        props=["A: toploader with card inside", "B: 420-count bulk pack fanned (12x 35ct)", "C: toploader + rigid/no-bend icons"],
        lighting="Bright, even studio light; crisp catch-light so the ultra-clear rigid film reads on white.",
        why_it_works=(
            "Three triggers: clarity (see your card), bulk value (420), rigid protection. One "
            "callout each — readable at thumbnail size."
        ),
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: Rigid & ultra-clear, card art stays visible",
        role="hook",
        background="Black with a thin red top-line and a bold white headline (Ultra PRO catalog)",
        purpose="Own the #1 reason collectors use toploaders: display the card, protect the card.",
        visual=(
            "Large macro: a standard 2.5\" x 3.5\" card sliding into the rigid 3\" x 4\" ultra-clear "
            "toploader, the artwork sharp and true-colour through the film. Thin red callout lines: "
            "'rigid PVC', 'ultra-clear', 'card art stays visible'. White bold headline top: 'SEE "
            "IT. PROTECT IT.'"
        ),
        overlay="ULTRA-CLEAR RIGID.",
        overlay_sub="Rigid ultra-clear PVC keeps card artwork and details fully visible.",
        props=["card sliding into toploader (macro)", "red callout lines", "true-colour card art"],
        lighting="Dramatic catalog light on black; strong edge-light on the rigid clear film.",
        why_it_works=(
            "Collectors buy toploaders to display AND protect. A true-colour macro proves the film "
            "is genuinely ultra-clear — the single strongest visual argument in the category."
        ),
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: Rigid structure, reduces bending damage",
        role="educate",
        background="White with a black/red Ultra PRO footer band",
        purpose="Defend quality: why rigid PVC matters for handling, storage and shipping.",
        visual=(
            "Split card. LEFT: the toploader with a card, a small shield icon 'RIGID STRUCTURE'. "
            "RIGHT: three stacked feature rows with red check-icons — 'RIGID PVC plastic', 'Reduces "
            "bending &amp; handling damage', 'Protects against dust, edge &amp; corner wear'. "
            "Footer band: 'Time-tested card protection — trusted since 1952.'"
        ),
        overlay="RIGID PVC PROTECTION.",
        overlay_sub="Sturdy rigid PVC reduces bending and handling damage during storage.",
        props=["toploader + card", "3 feature rows with red checks", "since-1952 footer band"],
        lighting="Flat, even catalog light; feature icons legible at thumbnail size.",
        why_it_works=(
            "Serious collectors filter on rigidity. Naming rigid PVC with a clear 'why it matters' "
            "separates this from flimsy unlabeled bargain holders."
        ),
    ),
    AIImagePlanItem(
        name="Image 4 — Fit: standard cards up to 35pt",
        role="desire",
        background="White with a red dimension callout (Ultra PRO)",
        purpose="Remove the #1 buyer question — will my cards fit?",
        visual=(
            "A standard trading card centred in the 3\" x 4\" toploader with a clean dimension "
            "callout: 'Fits standard 2.5\" x 3.5\" cards up to 35pt'. Small ruler graphic along two "
            "edges. A short note: 'Easy-load fit — sports, Pokemon, Magic and more.'"
        ),
        overlay="FITS STANDARD CARDS.",
        overlay_sub="Sized for 2.5\" x 3.5\" cards up to 35pt — sports, Pokemon and Magic.",
        props=["card in toploader", "dimension callout", "edge ruler graphic"],
        lighting="Bright, even; the dimension callout must read clearly.",
        why_it_works=(
            "Wrong-size or wrong-thickness holders are the top return reason in this category. A "
            "precise fit callout sets honest expectations and prevents mis-buys."
        ),
    ),
    AIImagePlanItem(
        name="Image 5 — Pack: 420 count for collectors, shops & resellers",
        role="desire",
        background="Black with red accents (Ultra PRO catalog)",
        purpose="Make the bulk value and use-cases obvious.",
        visual=(
            "The 420-count pack broken out as 12 sealed 35-count sleeves, with several carded "
            "toploaders organised in a row. Icon-stats: '420 COUNT', '12 x 35 packs', 'Sort new "
            "pulls', 'Shop &amp; reseller inventory'. Clean, catalog-style layout."
        ),
        overlay="420 PACK. STOCK UP.",
        overlay_sub="420 holders as 12 x 35 packs — collectors, shops and reseller inventory.",
        props=["420-count pack (12x 35ct sleeves)", "carded toploaders in a row", "4 icon-stats"],
        lighting="Catalog light on black; product and stats clearly separated.",
        why_it_works=(
            "Shows the quantity is a working stock, not just a number — speaks to collectors, "
            "hobbyists, card shops and resellers alike."
        ),
    ),
    AIImagePlanItem(
        name="Image 6 — Trust: Ultra PRO, trusted since 1952",
        role="trust",
        background="Black with red top-line, white headline (brand close)",
        purpose="Close on brand authority — the collector's default choice.",
        visual=(
            "Hero of the pack with a small lifestyle inset (a collector loading cards into "
            "toploaders at a tidy desk). Brand line bottom: 'ULTRA PRO — protecting collections "
            "since 1952 · trusted by collectors worldwide'. Red badge: 'SINCE 1952'."
        ),
        overlay="TRUSTED SINCE 1952.",
        overlay_sub="Ultra PRO — protecting trading card collections worldwide.",
        props=["pack hero", "collector lifestyle inset", "since-1952 red badge"],
        lighting="Premium catalog light on black; warm inset for the lifestyle moment.",
        why_it_works=(
            "Against unbranded bargain holders, heritage and trust are the deciding signals. 'Since "
            "1952' is Ultra PRO's honest, compliant authority claim."
        ),
    ),
    AIImagePlanItem(
        name="Image 7 — Range: the Ultra PRO card storage system",
        role="close",
        background="White with black/red Ultra PRO chrome",
        purpose="Cross-sell the wider card-protection range.",
        visual=(
            "Clean line-up: ultra-clear toploaders (this product) alongside penny sleeves, deck "
            "protectors and a storage box — shown as a coordinated system. Small labels; the "
            "toploaders gently highlighted. Caption: 'Sleeve it. Load it. Store it. — the Ultra "
            "PRO way.'"
        ),
        overlay="LOAD IT. STORE IT.",
        overlay_sub="Pair with Ultra PRO penny sleeves, deck protectors and storage boxes.",
        props=["toploaders (highlighted)", "penny sleeves", "deck protectors", "card storage box"],
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
            "Rigid 3\" x 4\" ultra-clear toploaders keep card artwork fully visible while "
            "guarding against bending, dust and edge wear. Made from rigid PVC and sized for "
            "standard 2.5\" x 3.5\" cards up to 35pt — card protection trusted by "
            "collectors since 1952."
        ),
        visual="Wide black banner, red top-line, bold white headline left; a carded ultra-clear toploader with crisp artwork right. Ultra PRO logo upper-left.",
        alt="Ultra PRO ultra-clear toploaders banner: rigid, standard-size fit, since 1952.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): Why these toploaders",
        role="a+_carousel",
        headline="WHY ULTRA PRO TOPLOADERS",
        body=(
            "Tile 1: <b>ULTRA-CLEAR RIGID</b> — Card art and details stay fully visible.<br/>"
            "Tile 2: <b>RIGID PVC STRUCTURE</b> — Reduces bending &amp; handling damage.<br/>"
            "Tile 3: <b>STANDARD-SIZE FIT</b> — 2.5\" x 3.5\" cards up to 35pt.<br/>"
            "Tile 4: <b>420-COUNT PACK</b> — 12 x 35 for collections and shops.<br/>"
            "Tile 5: <b>SINCE 1952</b> — Trusted card protection worldwide."
        ),
        visual="5 square tiles, red accent corner each, black/white icons (film · shield · ruler · stack · badge).",
        alt="Five A+ tiles: ultra-clear, rigid PVC, standard-size fit, 420-count, since 1952.",
    ),
    AIModule(
        name="Module 3 — Banner: Rigid protection",
        role="a+_banner",
        headline="RIGID PROTECTION. STORE &amp; SHIP.",
        body=(
            "Made from rigid PVC so cards stay supported and flat — reducing bending and handling "
            "damage during storage, display and shipping. Keep standard cards clean and covered, "
            "in the box or on show."
        ),
        visual="Banner split: macro of the rigid clear film + no-bend / support icons left; a row of carded toploaders right. Black/red Ultra PRO styling.",
        alt="A+ banner on rigid ultra-clear toploader protection for storage and shipping.",
    ),
    AIModule(
        name="Module 4 — Carousel (4 tiles): The card storage system",
        role="a+_carousel",
        headline="SLEEVE IT. LOAD IT. STORE IT.",
        body=(
            "Tile 1: <b>TOPLOADERS</b> — Rigid ultra-clear card holders (this product).<br/>"
            "Tile 2: <b>PENNY SLEEVES</b> — First-layer protection before the toploader.<br/>"
            "Tile 3: <b>DECK PROTECTORS</b> — Shuffle-ready sleeves for play.<br/>"
            "Tile 4: <b>STORAGE BOXES</b> — Organise and archive full collections."
        ),
        visual="4 coordinated product tiles, red accent corners, consistent catalog styling.",
        alt="Four A+ tiles showing the Ultra PRO card storage system: toploaders, sleeves, deck protectors, boxes.",
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
