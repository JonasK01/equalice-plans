"""Ultra PRO — ONE-Touch 55pt Magnetic Card Holder (25-Pack Box)  [Listing 71]
NEUES Format: Titel/Bullets/Backend kommen aus dem SEO-Sheet (listing.xlsx),
Q&A + Vergleich aus dem A+ Premium Sheet (aplus.xlsx). Bildregie handgeschrieben,
100% produktspezifisch, im Ultra-PRO-Katalogstil (schwarz/rot/weiss).

Marketplace: amazon.com (US). ASIN B00N5KSKUO.
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

PLAN_NO = "71"
ASIN = "B00N5KSKUO"
EXCEL = HERE / "listing.xlsx"
APLUS = HERE / "aplus.xlsx"


# ===== produktspezifische Bildregie (Ultra-PRO-Katalogstil, EN Overlays) =====

IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="Clean white for slot-1 compliance; the CTR versions add a black lower band with a thin red top-line (Ultra PRO catalog look). Same framing across all 3.",
        purpose="Win the click in a grid of look-alike card holders. Ship all 3, keep the winner.",
        visual=(
            "Mock ALL 3 options. Product exactly as real: a rigid two-piece ONE-Touch magnetic "
            "holder with a real standard trading card sealed inside, ultra-clear front, plus the "
            "25-count box behind it. ONE callout each, product dominant.\n\n"
            "OPTION A — DISPLAY: holder face-on, card art crisp through the clear window with the "
            "frosted border framing it. Badge (red): 'ULTRA-CLEAR DISPLAY'.\n"
            "OPTION B — MAGNET: three-quarter angle showing the magnetic lid closing on the hinge. "
            "Badge (red): 'ONE-TOUCH MAGNET'.\n"
            "OPTION C — PACK VALUE: the 25-count box with several loaded holders fanned. Badge "
            "(red): '25-PACK BOX'.\n\n"
            "Across all 3: white background, red badge ~6% of frame, same lighting."
        ),
        overlay="(one callout per option)",
        overlay_sub="3 hero options shipped — A/B test, keep the winner.",
        props=["A: holder face-on with card", "B: magnetic lid closing on hinge", "C: 25-count box with loaded holders"],
        lighting="Bright, even studio light; crisp catch-light so the ultra-clear window and frosted border read on white.",
        why_it_works=(
            "Three triggers: display (see your card), the one-touch magnet mechanism, and 25-pack "
            "value. One callout each — readable at thumbnail size."
        ),
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: One-touch magnetic closure, no screws",
        role="hook",
        background="Black with a thin red top-line and a bold white headline (Ultra PRO catalog)",
        purpose="Own the #1 upgrade reason: a secure magnetic close instead of fiddly screws.",
        visual=(
            "Large macro: a thumb closing the magnetic lid onto the slide-in hinge, card already "
            "seated inside. Thin red callout lines: 'slide-in hinge', 'magnetic closure', 'no "
            "screws or tools'. White bold headline top: 'SNAP IT SHUT.'"
        ),
        overlay="ONE-TOUCH. NO SCREWS.",
        overlay_sub="Slide-in hinges and a magnetic closure open and close without screws or tools.",
        props=["thumb closing magnetic lid (macro)", "slide-in hinge detail", "red callout lines"],
        lighting="Dramatic catalog light on black; strong edge-light on the clear case and hinge.",
        why_it_works=(
            "Collectors trading up from screw-down holders want speed and security. Showing the "
            "one-touch magnet in action is the single strongest visual argument in the category."
        ),
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: UV-blocking, acid-free, non-PVC",
        role="educate",
        background="White with a black/red Ultra PRO footer band",
        purpose="Defend quality: why UV-blocking + acid-free + non-PVC matters for long-term storage.",
        visual=(
            "Split card. LEFT: the loaded holder with a small sun/shield icon 'UV-BLOCKING'. RIGHT: "
            "three stacked feature rows with red check-icons — 'UV-BLOCKING additives (guards "
            "color)', 'ACID-FREE, non-PVC polypropylene', 'Front & back visibility'. Footer band: "
            "'Time-tested card protection — trusted since 1952.'"
        ),
        overlay="UV-BLOCKING. ACID-FREE.",
        overlay_sub="Non-PVC, acid-free polypropylene with UV-blocking additives guards color and card.",
        props=["loaded holder + UV shield icon", "3 feature rows with red checks", "since-1952 footer band"],
        lighting="Flat, even catalog light; feature icons legible at thumbnail size.",
        why_it_works=(
            "Serious collectors filter on archival safety and UV protection. Naming each benefit "
            "with a clear 'why it matters' separates this from unlabeled bargain holders."
        ),
    ),
    AIImagePlanItem(
        name="Image 4 — Fit: standard cards up to 55pt",
        role="desire",
        background="White with a red dimension callout (Ultra PRO)",
        purpose="Remove the #1 buyer question — will my card fit?",
        visual=(
            "A standard trading card centred in the open holder with a clean callout: 'Fits "
            "standard 2.5\" x 3.5\" cards up to 55pt'. Small thickness gauge along one edge and a "
            "note: 'For sports, trading and gaming cards.'"
        ),
        overlay="FITS 55PT STANDARD CARDS.",
        overlay_sub="Sized for standard 2.5\" x 3.5\" cards up to 55pt — sports, trading and gaming.",
        props=["card seated in open holder", "55pt thickness gauge", "dimension callout"],
        lighting="Bright, even; the dimension and 55pt callouts must read clearly.",
        why_it_works=(
            "Wrong-thickness holders are a top return reason. A precise 55pt / standard-size "
            "callout sets honest expectations and prevents mis-buys."
        ),
    ),
    AIImagePlanItem(
        name="Image 5 — Display & pack: 25 holders, showcase-ready",
        role="desire",
        background="Black with red accents (Ultra PRO catalog)",
        purpose="Make the display value and 25-pack use-cases obvious.",
        visual=(
            "Several loaded holders standing upright on a shelf like a mini display, frosted borders "
            "and diamond corners catching the light, with the 25-count box beside them. Icon-stats: "
            "'25 HOLDERS', 'Front & back view', 'Stands for display', 'Frosted border · diamond "
            "corners'. Clean, catalog-style layout."
        ),
        overlay="25 HOLDERS. DISPLAY READY.",
        overlay_sub="A 25-pack box to protect and showcase sports, trading and gaming cards.",
        props=["upright holders on a shelf", "25-count box", "4 icon-stats"],
        lighting="Catalog light on black; product and stats clearly separated.",
        why_it_works=(
            "Shows the holders both protect AND display, and that 25 is a working set — speaks to "
            "collectors building and showing a collection."
        ),
    ),
    AIImagePlanItem(
        name="Image 6 — Trust: Ultra PRO, trusted since 1952",
        role="trust",
        background="Black with red top-line, white headline (brand close)",
        purpose="Close on brand authority — the collector's default choice.",
        visual=(
            "Hero of the box with a small lifestyle inset (a collector snapping a card into a holder "
            "at a tidy desk). Brand line bottom: 'ULTRA PRO — protecting collections since 1952 · "
            "trusted by collectors worldwide'. Red badge: 'SINCE 1952'."
        ),
        overlay="TRUSTED SINCE 1952.",
        overlay_sub="Ultra PRO — protecting card collections worldwide.",
        props=["box hero", "collector lifestyle inset", "since-1952 red badge"],
        lighting="Premium catalog light on black; warm inset for the lifestyle moment.",
        why_it_works=(
            "Against unbranded bargain holders, heritage and trust are the deciding signals. "
            "'Since 1952' is Ultra PRO's honest, compliant authority claim."
        ),
    ),
    AIImagePlanItem(
        name="Image 7 — Range: the Ultra PRO card protection system",
        role="close",
        background="White with black/red Ultra PRO chrome",
        purpose="Cross-sell the wider card-protection range.",
        visual=(
            "Clean line-up: the ONE-Touch magnetic holders (this product) alongside toploaders, "
            "inner sleeves and a storage box — shown as a coordinated system. Small labels; the "
            "magnetic holders gently highlighted. Caption: 'Sleeve it. Hold it. Store it. — the "
            "Ultra PRO way.'"
        ),
        overlay="THE ULTRA PRO SYSTEM.",
        overlay_sub="Pair the holders with Ultra PRO sleeves, toploaders and storage boxes.",
        props=["magnetic holders (highlighted)", "toploaders", "inner sleeves", "storage box"],
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
        headline="ONE-TOUCH. UV-CLEAR. SINCE 1952.",
        body=(
            "The ONE-Touch 55pt magnetic holder seals standard cards in a rigid, ultra-clear case "
            "with a secure one-touch magnetic closure. UV-blocking, acid-free and non-PVC "
            "polypropylene keeps color and card protected &amp; on display — trusted by collectors "
            "since 1952."
        ),
        visual="Wide black banner, red top-line, bold white headline left; a loaded magnetic holder with a crisp card right. Ultra PRO logo upper-left.",
        alt="Ultra PRO ONE-Touch 55pt magnetic card holder banner: one-touch magnet, UV-clear, since 1952.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): Why these holders",
        role="a+_carousel",
        headline="WHY ONE-TOUCH MAGNETIC HOLDERS",
        body=(
            "Tile 1: <b>ONE-TOUCH MAGNET</b> — Slide-in hinge, no screws or tools.<br/>"
            "Tile 2: <b>UV-BLOCKING &amp; ACID-FREE</b> — Non-PVC, guards color long-term.<br/>"
            "Tile 3: <b>FITS 55PT STANDARD</b> — For 2.5\" x 3.5\" cards up to 55pt.<br/>"
            "Tile 4: <b>25-PACK BOX</b> — Protect &amp; display a whole collection.<br/>"
            "Tile 5: <b>SINCE 1952</b> — Trusted card protection worldwide."
        ),
        visual="5 square tiles, red accent corner each, black/white icons (magnet · shield · ruler · box · badge).",
        alt="Five A+ tiles: one-touch magnet, UV-blocking/acid-free, 55pt fit, 25-pack, since 1952.",
    ),
    AIModule(
        name="Module 3 — Banner: Clear display & UV protection",
        role="a+_banner",
        headline="CLEAR DISPLAY. UV PROTECTION.",
        body=(
            "Made from clear, non-PVC, acid-free polypropylene with UV-blocking additives, so cards "
            "stay visible front &amp; back while guarding against fading. Frosted borders and diamond "
            "corners frame every card — on the shelf, in the box, or on display."
        ),
        visual="Banner split: macro of the clear window + UV/acid-free shield icons left; upright loaded holders on a shelf right. Black/red Ultra PRO styling.",
        alt="A+ banner on clear display and UV-blocking, acid-free card protection.",
    ),
    AIModule(
        name="Module 4 — Carousel (4 tiles): The card protection system",
        role="a+_carousel",
        headline="PROTECT YOUR WHOLE COLLECTION",
        body=(
            "Tile 1: <b>MAGNETIC HOLDERS</b> — One-touch 55pt display cases (this product).<br/>"
            "Tile 2: <b>TOPLOADERS</b> — Rigid protection for everyday cards.<br/>"
            "Tile 3: <b>INNER SLEEVES</b> — First layer against dust &amp; scratches.<br/>"
            "Tile 4: <b>STORAGE BOXES</b> — Organize and archive full collections."
        ),
        visual="4 coordinated product tiles, red accent corners, consistent catalog styling.",
        alt="Four A+ tiles showing the Ultra PRO card protection system: magnetic holders, toploaders, sleeves, boxes.",
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
