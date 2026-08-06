"""Ultra PRO — Lucite Brik 1" Screwdown Trading Card Display  [Listing 66]
NEUES Format: Titel/Bullets/Backend kommen aus dem SEO-Sheet (listing.xlsx),
Q&A + Vergleich aus dem A+ Premium Sheet (aplus.xlsx). Bildregie handgeschrieben,
100% produktspezifisch, im Ultra-PRO-Katalogstil (schwarz/rot/weiss).

Marketplace: amazon.com (US). ASIN B000COO3SO.
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

PLAN_NO = "66"
ASIN = "B000COO3SO"
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
            "Mock ALL 3 options. Product exactly as real: the thick clear lucite screwdown brik "
            "holding a real standard-size trading card upright, crystal-clear through the acrylic, "
            "four corner screws visible. ONE callout each, product dominant.\n\n"
            "OPTION A — CLARITY: card face crisp and true-colour through the lucite, screws in focus. "
            "Badge (red): 'CRYSTAL-CLEAR LUCITE'.\n"
            "OPTION B — THICKNESS: side profile showing the chunky slab. Badge (red): '1\" THICK BRIK'.\n"
            "OPTION C — SECURITY: close on the four corner screws. Badge (red): 'FOUR-SCREW LOCK'.\n\n"
            "Across all 3: white background, red badge ~6% of frame, same lighting."
        ),
        overlay="(one callout per option)",
        overlay_sub="3 hero options shipped — A/B test, keep the winner.",
        props=["A: card upright inside the lucite brik", "B: side profile of the 1\" slab", "C: macro on the four corner screws"],
        lighting="Bright, even studio light; crisp catch-light so the clear lucite reads on white.",
        why_it_works=(
            "Three triggers: clarity (see the card), premium thickness (1\" brik), secure lock "
            "(four screws). One callout each — readable at thumbnail size."
        ),
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: crystal-clear lucite, card on full display",
        role="hook",
        background="Black with a thin red top-line and a bold white headline (Ultra PRO catalog)",
        purpose="Own the #1 reason collectors buy a brik: show the card, not hide it away.",
        visual=(
            "Large macro: a standard trading card sealed inside the thick lucite brik, the artwork "
            "sharp and true-colour through the slab, beveled edges catching the light. Thin red "
            "callout lines: 'thick lucite slabs', 'beveled edges', 'card stays fully visible'. "
            "White bold headline top: 'SHOW IT OFF.'"
        ),
        overlay="CRYSTAL-CLEAR LUCITE.",
        overlay_sub="Thick lucite slabs keep the full card face on display in true colour.",
        props=["card sealed in the brik (macro)", "red callout lines", "beveled edge highlight"],
        lighting="Dramatic catalog light on black; strong edge-light on the clear lucite.",
        why_it_works=(
            "Collectors buy a screwdown to display AND protect. A true-colour macro proves the "
            "lucite is genuinely crystal-clear — the strongest visual argument in the category."
        ),
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: four-screw closure holds it secure",
        role="educate",
        background="White with a black/red Ultra PRO footer band",
        purpose="Defend the build: how the corner screws secure the card yet allow easy access.",
        visual=(
            "Split card. LEFT: the brik with a card inside, a small shield icon 'SECURELY ENCLOSED'. "
            "RIGHT: three stacked feature rows with red check-icons — 'FOUR corner screws', 'Screw "
            "down to seal, unscrew for easy access', 'Stable, protective screwdown design'. Footer "
            "band: 'Reliable collector protection — trusted since 1952.'"
        ),
        overlay="FOUR-SCREW CLOSURE.",
        overlay_sub="Four corner screws seal the brik yet unscrew for easy card access.",
        props=["brik + card", "macro on a corner screw", "3 feature rows with red checks", "since-1952 footer band"],
        lighting="Flat, even catalog light; feature icons legible at thumbnail size.",
        why_it_works=(
            "The screwdown mechanism is the buying decision. Naming four screws plus a clear 'how "
            "it works' separates this from press-fit magnetic holders."
        ),
    ),
    AIImagePlanItem(
        name="Image 4 — Fit: sized for standard cards, sleeve-friendly",
        role="desire",
        background="White with a red dimension callout (Ultra PRO)",
        purpose="Remove the #1 buyer question — will my card (and sleeve) fit?",
        visual=(
            "A standard trading card centred in the brik with a clean dimension callout: 'Fits "
            "standard 2-1/2\" x 3-1/2\" cards (63.5 x 88.9 mm)'. Small ruler graphic along two "
            "edges. A short note: 'Non-recessed design works with protective sleeves.'"
        ),
        overlay="FITS STANDARD CARDS.",
        overlay_sub="Standard 2-1/2\" x 3-1/2\" cards — non-recessed, sleeve-friendly fit.",
        props=["card in brik", "dimension callout", "edge ruler graphic", "sleeve icon"],
        lighting="Bright, even; the dimension callout must read clearly.",
        why_it_works=(
            "Wrong-size or non-sleeve-fit holders are the top return reason. A precise fit callout "
            "plus the sleeve note sets honest expectations and prevents mis-buys."
        ),
    ),
    AIImagePlanItem(
        name="Image 5 — Display: stand it vertical or horizontal",
        role="desire",
        background="Black with red accents (Ultra PRO catalog)",
        purpose="Show the versatile premium presentation on any surface.",
        visual=(
            "The brik shown twice — once upright (portrait) and once laid horizontal — with a "
            "single card, styled on a tidy shelf and a desk. Icon-stats: 'Vertical or horizontal', "
            "'Shelf, desk & cabinet', 'Premium presentation', 'Non-recessed 1\" thick'. Clean, "
            "catalog-style layout."
        ),
        overlay="VERTICAL OR HORIZONTAL.",
        overlay_sub="Stand the brik upright or lay it flat on shelves, desks and cabinets.",
        props=["brik upright", "brik horizontal", "shelf and desk setting", "4 icon-stats"],
        lighting="Catalog light on black; product and stats clearly separated.",
        why_it_works=(
            "Flexible display is what turns a protector into a showcase — it speaks to collectors "
            "who want the card seen, not boxed away."
        ),
    ),
    AIImagePlanItem(
        name="Image 6 — Trust: Ultra PRO, trusted since 1952",
        role="trust",
        background="Black with red top-line, white headline (brand close)",
        purpose="Close on brand authority — the collector's default choice.",
        visual=(
            "Hero of the brik with a small lifestyle inset (a collector setting a prized card into "
            "the screwdown at a tidy desk). Brand line bottom: 'ULTRA PRO — protecting collections "
            "since 1952 · trusted by collectors worldwide'. Red badge: 'SINCE 1952'."
        ),
        overlay="TRUSTED SINCE 1952.",
        overlay_sub="Ultra PRO — protecting and displaying card collections worldwide.",
        props=["brik hero", "collector lifestyle inset", "since-1952 red badge"],
        lighting="Premium catalog light on black; warm inset for the lifestyle moment.",
        why_it_works=(
            "Against unbranded acrylic cases, heritage and trust are the deciding signals. 'Since "
            "1952' is Ultra PRO's honest, compliant authority claim."
        ),
    ),
    AIImagePlanItem(
        name="Image 7 — Range: the Ultra PRO display & storage system",
        role="close",
        background="White with black/red Ultra PRO chrome",
        purpose="Cross-sell the wider display and protection range.",
        visual=(
            "Clean line-up: the lucite screwdown brik (this product) alongside a graded card case, "
            "a 9-pocket PRO-Binder and toploaders — shown as a coordinated system. Small labels; "
            "the brik gently highlighted. Caption: 'Display it. Protect it. — the Ultra PRO way.'"
        ),
        overlay="DISPLAY IT. PROTECT IT.",
        overlay_sub="Pair the brik with Ultra PRO binders, graded cases and toploaders.",
        props=["lucite screwdown brik (highlighted)", "graded card case", "9-pocket PRO-Binder", "toploaders"],
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
        headline="SHOW IT OFF. SINCE 1952.",
        body=(
            "Thick crystal-clear lucite slabs and a four-screw corner closure put your standard "
            "trading card on premium display while keeping it securely enclosed. Beveled edges, a "
            "non-recessed 1\" thick design, sleeve-friendly — card protection and display trusted "
            "by collectors since 1952."
        ),
        visual="Wide black banner, red top-line, bold white headline left; a card sealed in the clear lucite brik right. Ultra PRO logo upper-left.",
        alt="Ultra PRO Lucite Brik screwdown banner: crystal-clear lucite, four-screw closure, since 1952.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): Why this screwdown",
        role="a+_carousel",
        headline="WHY THE LUCITE BRIK",
        body=(
            "Tile 1: <b>CRYSTAL-CLEAR LUCITE</b> — Thick slabs keep the full card on display.<br/>"
            "Tile 2: <b>FOUR-SCREW CLOSURE</b> — Corner screws seal it, unscrew for access.<br/>"
            "Tile 3: <b>STANDARD-CARD FIT</b> — 2-1/2\" x 3-1/2\", sleeve-friendly.<br/>"
            "Tile 4: <b>VERTICAL OR HORIZONTAL</b> — Display on shelves, desks &amp; cabinets.<br/>"
            "Tile 5: <b>SINCE 1952</b> — Trusted collector protection worldwide."
        ),
        visual="5 square tiles, red accent corner each, black/white icons (slab · screw · ruler · stand · badge).",
        alt="Five A+ tiles: crystal-clear lucite, four-screw closure, standard fit, vertical/horizontal, since 1952.",
    ),
    AIModule(
        name="Module 3 — Banner: Premium display",
        role="a+_banner",
        headline="PREMIUM DISPLAY. SECURE HOLD.",
        body=(
            "Built from thick lucite with beveled edges and a non-recessed 1\" profile, this "
            "screwdown brik showcases individual cards instead of hiding them away — while four "
            "corner screws keep each card securely enclosed on the shelf, desk or in the cabinet."
        ),
        visual="Banner split: macro of the clear lucite + corner-screw detail left; the brik on a display shelf right. Black/red Ultra PRO styling.",
        alt="A+ banner on premium lucite display with a secure four-screw closure.",
    ),
    AIModule(
        name="Module 4 — Carousel (4 tiles): The display & storage system",
        role="a+_carousel",
        headline="DISPLAY IT. PROTECT IT.",
        body=(
            "Tile 1: <b>LUCITE SCREWDOWN BRIK</b> — Premium single-card display (this product).<br/>"
            "Tile 2: <b>GRADED CARD CASE</b> — Hard-shell protection for graded slabs.<br/>"
            "Tile 3: <b>9-POCKET PRO-BINDER</b> — Organise and store full sets.<br/>"
            "Tile 4: <b>TOPLOADERS</b> — Rigid everyday protection for key cards."
        ),
        visual="4 coordinated product tiles, red accent corners, consistent catalog styling.",
        alt="Four A+ tiles showing the Ultra PRO display and storage system: brik, graded case, binder, toploaders.",
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
