"""Ultra PRO — Current Size Comic Bags (100 ct)  [Listing 51]
NEUES Format: Titel/Bullets/Backend kommen aus dem SEO-Sheet (listing.xlsx),
Q&A + Vergleich aus dem A+ Premium Sheet (aplus.xlsx). Bildregie handgeschrieben,
100% produktspezifisch, im Ultra-PRO-Katalogstil (schwarz/rot/weiss).

Marketplace: amazon.com (US). ASIN B09TVBW43D.
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

PLAN_NO = "51"
ASIN = "B09TVBW43D"
EXCEL = HERE / "listing.xlsx"
APLUS = HERE / "aplus.xlsx"


# ===== produktspezifische Bildregie (Ultra-PRO-Katalogstil, EN Overlays) =====

IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="Clean white for slot-1 compliance; the CTR versions add a black lower band with a thin red top-line (Ultra PRO catalog look). Same framing across all 3.",
        purpose="Win the click in a grid of look-alike comic sleeves. Ship all 3, keep the winner.",
        visual=(
            "Mock ALL 3 options. Product exactly as real: a current-size comic bag holding a "
            "generic (non-branded) comic, ultra-clear, plus the 100-count pack behind it. ONE "
            "callout each, product dominant.\n\n"
            "OPTION A — CLARITY: bag with a colourful comic inside, cover art crisp through the "
            "sleeve. Badge (red): 'ULTRA-CLEAR 2 MIL'.\n"
            "OPTION B — PACK VALUE: the 100-count stack fanned. Badge (red): '100 BAGS'.\n"
            "OPTION C — ARCHIVAL: bag + small acid-free / no-PVC icons. Badge: 'ACID-FREE · NO PVC'.\n\n"
            "Across all 3: white background, red badge ~6% of frame, same lighting."
        ),
        overlay="(one callout per option)",
        overlay_sub="3 hero options shipped — A/B test, keep the winner.",
        props=["A: comic bag with comic inside", "B: 100-count pack fanned", "C: bag + acid-free/no-PVC icons"],
        lighting="Bright, even studio light; crisp catch-light so the ultra-clear film reads on white.",
        why_it_works=(
            "Three triggers: clarity (see your art), pack value (100), archival safety. One "
            "callout each — readable at thumbnail size."
        ),
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: Ultra-clear 2 mil, art stays visible",
        role="hook",
        background="Black with a thin red top-line and a bold white headline (Ultra PRO catalog)",
        purpose="Own the #1 reason collectors sleeve comics: see the cover, protect the cover.",
        visual=(
            "Large macro: a current-size comic sliding into the ultra-clear bag, the cover art "
            "sharp and true-colour through the film. Thin red callout lines: '2 mil polypropylene', "
            "'crystal-clear', 'cover art stays visible'. White bold headline top: 'SEE IT. "
            "PROTECT IT.'"
        ),
        overlay="ULTRA-CLEAR 2 MIL.",
        overlay_sub="Crystal-clear polypropylene keeps cover art and titles fully visible.",
        props=["comic sliding into bag (macro)", "red callout lines", "true-colour cover art"],
        lighting="Dramatic catalog light on black; strong edge-light on the clear film.",
        why_it_works=(
            "Collectors buy sleeves to display AND protect. A true-colour macro proves the film "
            "is genuinely ultra-clear — the single strongest visual argument in the category."
        ),
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: Archival-safe, acid-free & PVC-free",
        role="educate",
        background="White with a black/red Ultra PRO footer band",
        purpose="Defend quality: why acid-free + PVC-free matters for long-term comic storage.",
        visual=(
            "Split card. LEFT: the bag with a comic, a small shield icon 'ARCHIVAL-SAFE'. RIGHT: "
            "three stacked feature rows with red check-icons — 'ACID-FREE polypropylene', 'PVC-FREE "
            "(no plasticiser migration)', 'Protects against dust, fingerprints & shelf wear'. "
            "Footer band: 'Time-tested comic protection — trusted since 1952.'"
        ),
        overlay="ACID-FREE. PVC-FREE.",
        overlay_sub="Archival-safe polypropylene for long-term, worry-free comic storage.",
        props=["bag + comic", "3 feature rows with red checks", "since-1952 footer band"],
        lighting="Flat, even catalog light; feature icons legible at thumbnail size.",
        why_it_works=(
            "Serious collectors filter on archival safety. Naming acid-free + PVC-free with a "
            "clear 'why it matters' separates this from unlabeled bargain bags."
        ),
    ),
    AIImagePlanItem(
        name="Image 4 — Fit: sized for current-size comics",
        role="desire",
        background="White with a red dimension callout (Ultra PRO)",
        purpose="Remove the #1 buyer question — will my comics fit?",
        visual=(
            "A current-size comic centred in the bag with a clean dimension callout: 'Fits current-"
            "size comics up to 6-7/8\" x 10-1/2\"'. Small ruler graphic along two edges. A short "
            "note: 'Snug, easy-load fit — in and out without bending covers.'"
        ),
        overlay="FITS CURRENT-SIZE COMICS.",
        overlay_sub="Sized for issues up to 6-7/8\" x 10-1/2\" — easy load, no bent covers.",
        props=["comic in bag", "dimension callout", "edge ruler graphic"],
        lighting="Bright, even; the dimension callout must read clearly.",
        why_it_works=(
            "Wrong-size sleeves are the top return reason in this category. A precise fit callout "
            "sets honest expectations and prevents mis-buys."
        ),
    ),
    AIImagePlanItem(
        name="Image 5 — Pack: 100 count for collection & shop",
        role="desire",
        background="Black with red accents (Ultra PRO catalog)",
        purpose="Make the pack value and use-cases obvious.",
        visual=(
            "The 100-count pack with several bagged comics organised in a short box. Icon-stats: "
            "'100 BAGS', 'Sort new pulls', 'Refresh old sleeves', 'Shop & reseller inventory'. "
            "Clean, catalog-style layout."
        ),
        overlay="100 BAGS. STAY ORGANIZED.",
        overlay_sub="Sort new pulls, refresh old sleeves, manage shop and reseller inventory.",
        props=["100-count pack", "bagged comics in a short box", "4 icon-stats"],
        lighting="Catalog light on black; product and stats clearly separated.",
        why_it_works=(
            "Shows the quantity is a working tool, not just a number — speaks to collectors, "
            "hobbyists and comic shops alike."
        ),
    ),
    AIImagePlanItem(
        name="Image 6 — Trust: Ultra PRO, trusted since 1952",
        role="trust",
        background="Black with red top-line, white headline (brand close)",
        purpose="Close on brand authority — the collector's default choice.",
        visual=(
            "Hero of the pack with a small lifestyle inset (a collector bagging comics at a tidy "
            "desk). Brand line bottom: 'ULTRA PRO — protecting collections since 1952 · trusted by "
            "collectors worldwide'. Red badge: 'SINCE 1952'."
        ),
        overlay="TRUSTED SINCE 1952.",
        overlay_sub="Ultra PRO — protecting comic and card collections worldwide.",
        props=["pack hero", "collector lifestyle inset", "since-1952 red badge"],
        lighting="Premium catalog light on black; warm inset for the lifestyle moment.",
        why_it_works=(
            "Against unbranded bargain bags, heritage and trust are the deciding signals. 'Since "
            "1952' is Ultra PRO's honest, compliant authority claim."
        ),
    ),
    AIImagePlanItem(
        name="Image 7 — Range: the Ultra PRO comic storage system",
        role="close",
        background="White with black/red Ultra PRO chrome",
        purpose="Cross-sell the wider comic-protection range.",
        visual=(
            "Clean line-up: current-size comic bags (this product) alongside boards, toploaders "
            "and a comic storage box — shown as a coordinated system. Small labels; the comic "
            "bags gently highlighted. Caption: 'Bag it. Board it. Store it. — the Ultra PRO way.'"
        ),
        overlay="BAG IT. BOARD IT.",
        overlay_sub="Store it — pair with Ultra PRO boards, toploaders and storage boxes.",
        props=["comic bags (highlighted)", "boards", "toploaders", "comic storage box"],
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
            "Ultra-clear 2 mil polypropylene comic bags keep cover art fully visible while guarding "
            "against dust, fingerprints and shelf wear. Acid-free, PVC-free and archival-safe — "
            "comic protection trusted by collectors since 1952."
        ),
        visual="Wide black banner, red top-line, bold white headline left; a bagged comic with crisp cover art right. Ultra PRO logo upper-left.",
        alt="Ultra PRO current-size comic bags banner: ultra-clear, acid-free, PVC-free, since 1952.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): Why these bags",
        role="a+_carousel",
        headline="WHY ULTRA PRO COMIC BAGS",
        body=(
            "Tile 1: <b>ULTRA-CLEAR 2 MIL</b> — Cover art and titles stay fully visible.<br/>"
            "Tile 2: <b>ACID-FREE &amp; PVC-FREE</b> — Archival-safe for long-term storage.<br/>"
            "Tile 3: <b>CURRENT-SIZE FIT</b> — Up to 6-7/8\" x 10-1/2\", easy load.<br/>"
            "Tile 4: <b>100-COUNT PACK</b> — For collections and shop inventory.<br/>"
            "Tile 5: <b>SINCE 1952</b> — Trusted comic protection worldwide."
        ),
        visual="5 square tiles, red accent corner each, black/white icons (film · shield · ruler · stack · badge).",
        alt="Five A+ tiles: ultra-clear, acid-free/PVC-free, current-size fit, 100-count, since 1952.",
    ),
    AIModule(
        name="Module 3 — Banner: Archival protection",
        role="a+_banner",
        headline="ARCHIVAL-SAFE. WORRY-FREE.",
        body=(
            "Made from acid-free, PVC-free polypropylene so there is no plasticiser migration onto "
            "your books. Keep current-size comics clean and covered — on the shelf, in the box, or "
            "on display."
        ),
        visual="Banner split: macro of the clear film + acid-free/PVC-free shield icons left; a short box of bagged comics right. Black/red Ultra PRO styling.",
        alt="A+ banner on archival-safe acid-free, PVC-free comic protection.",
    ),
    AIModule(
        name="Module 4 — Carousel (4 tiles): The comic storage system",
        role="a+_carousel",
        headline="BAG IT. BOARD IT. STORE IT.",
        body=(
            "Tile 1: <b>COMIC BAGS</b> — Ultra-clear current-size sleeves (this product).<br/>"
            "Tile 2: <b>BACKING BOARDS</b> — Keep comics flat and supported.<br/>"
            "Tile 3: <b>COMIC TOPLOADERS</b> — Rigid protection for key issues.<br/>"
            "Tile 4: <b>STORAGE BOXES</b> — Organise and archive full runs."
        ),
        visual="4 coordinated product tiles, red accent corners, consistent catalog styling.",
        alt="Four A+ tiles showing the Ultra PRO comic storage system: bags, boards, toploaders, boxes.",
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
