"""Ultra PRO — 9" x 11-1/4" Thick Magazine Toploader (10 ct)  [Listing 63]
Titel/Bullets/Backend kommen aus dem SEO-Sheet (listing.xlsx), Q&A + Vergleich
aus dem A+ Premium Sheet (aplus.xlsx). Bildregie handgeschrieben, 100%
produktspezifisch, im Ultra-PRO-Katalogstil (schwarz/rot/weiss).

WICHTIG (Compliance): Dieses Produkt ist aus HIGH-IMPACT RIGID PVC. KEINE
'acid-free' / 'PVC-free'-Claims verwenden — es IST PVC. Stärke = starrer,
biegefester Schutz, ultra-klare Sicht, Magazingröße 9x11-1/4, bis 7mm dick.

Marketplace: amazon.com (US). ASIN B001IKHSR4.
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

PLAN_NO = "63"
ASIN = "B001IKHSR4"
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
            "Mock ALL 3 options. Product exactly as real: a rigid 9\" x 11-1/4\" magazine "
            "toploader holding a real magazine, ultra-clear front, plus the 10-count pack "
            "behind it. ONE callout each, product dominant.\n\n"
            "OPTION A — CLARITY: toploader with a magazine inside, cover crisp through the "
            "clear front. Badge (red): 'ULTRA-CLEAR'.\n"
            "OPTION B — RIGID: toploader held at a corner showing the stiff, bend-resistant "
            "body. Badge (red): 'RIGID PVC'.\n"
            "OPTION C — PACK VALUE: the 10-count stack fanned. Badge (red): '10 PACK'.\n\n"
            "Across all 3: white background, red badge ~6% of frame, same lighting."
        ),
        overlay="(one callout per option)",
        overlay_sub="3 hero options shipped — A/B test, keep the winner.",
        props=["A: toploader with magazine inside", "B: rigid toploader at a corner", "C: 10-count pack fanned"],
        lighting="Bright, even studio light; crisp catch-light so the ultra-clear front reads on white.",
        why_it_works=(
            "Three triggers: clarity (see your cover), rigidity (real protection), pack "
            "value (10). One callout each — readable at thumbnail size."
        ),
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: rigid PVC, ultra-clear front",
        role="hook",
        background="Black with a thin red top-line and a bold white headline (Ultra PRO catalog)",
        purpose="Own the #1 reason collectors sleeve magazines: rigid, see-through protection.",
        visual=(
            "Large macro: a magazine sliding into the rigid toploader, the cover art sharp "
            "and true-colour through the ultra-clear front. Thin red callout lines: "
            "'high-impact rigid PVC', 'ultra-clear front', 'cover stays visible'. White bold "
            "headline top: 'SEE IT. SHIELD IT.'"
        ),
        overlay="RIGID. ULTRA-CLEAR.",
        overlay_sub="High-impact rigid PVC with an ultra-clear front — see every cover.",
        props=["magazine sliding into toploader (macro)", "red callout lines", "true-colour cover art"],
        lighting="Dramatic catalog light on black; strong edge-light on the rigid clear front.",
        why_it_works=(
            "Collectors buy toploaders to display AND shield. A true-colour macro proves the "
            "front is genuinely ultra-clear while the body stays rigid — the category's "
            "strongest visual argument."
        ),
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: rigid protection for magazines & documents",
        role="educate",
        background="White with a black/red Ultra PRO footer band",
        purpose="Defend quality: why rigid PVC and a 7mm capacity matter for magazine storage.",
        visual=(
            "Split card. LEFT: the toploader holding a magazine, a small shield icon "
            "'RIGID PROTECTION'. RIGHT: three stacked feature rows with red check-icons — "
            "'HIGH-IMPACT RIGID PVC', 'HOLDS ITEMS UP TO 7MM THICK', 'Guards against bending, "
            "dust & handling wear'. Footer band: 'Time-tested collectible protection — "
            "trusted since 1952.'"
        ),
        overlay="HOLDS UP TO 7MM THICK",
        overlay_sub="Rigid PVC guards magazines, programs and documents up to 7mm — no bending.",
        props=["toploader + magazine", "3 feature rows with red checks", "since-1952 footer band"],
        lighting="Flat, even catalog light; feature icons legible at thumbnail size.",
        why_it_works=(
            "Serious collectors filter on rigidity and capacity. Naming high-impact PVC and "
            "the 7mm thickness limit separates this from flimsy bargain sleeves."
        ),
    ),
    AIImagePlanItem(
        name="Image 4 — Fit: sized for 9 x 11-1/4 magazines",
        role="desire",
        background="White with a red dimension callout (Ultra PRO)",
        purpose="Remove the #1 buyer question — will my magazine fit?",
        visual=(
            "A magazine centred in the toploader with a clean dimension callout: 'Fits items "
            "9\" x 11-1/4\" (228.6mm x 279.4mm), up to 7mm thick'. Small ruler graphic along "
            "two edges. A short note: 'Large-format top-load — easy in and out, no bent "
            "covers.'"
        ),
        overlay="FITS 9\" X 11-1/4\"",
        overlay_sub="Large-format fit for 9\" x 11-1/4\" magazines, programs and documents.",
        props=["magazine in toploader", "dimension callout", "edge ruler graphic"],
        lighting="Bright, even; the dimension callout must read clearly.",
        why_it_works=(
            "Wrong-size holders are the top return reason in this category. A precise fit "
            "callout sets honest expectations and prevents mis-buys."
        ),
    ),
    AIImagePlanItem(
        name="Image 5 — Pack: 10 count to store, display & ship",
        role="desire",
        background="Black with red accents (Ultra PRO catalog)",
        purpose="Make the pack value and use-cases obvious.",
        visual=(
            "The 10-count pack with several loaded toploaders standing on a shelf and a flat "
            "stack ready to ship. Icon-stats: '10 TOPLOADERS', 'Store magazines', 'Display "
            "upright', 'Ship flat & safe'. Clean, catalog-style layout."
        ),
        overlay="10 PACK. STAY ORGANIZED.",
        overlay_sub="Ten rigid toploaders to store, display and ship your collection.",
        props=["10-count pack", "loaded toploaders on a shelf", "flat stack ready to ship", "4 icon-stats"],
        lighting="Catalog light on black; product and stats clearly separated.",
        why_it_works=(
            "Shows the quantity is a working tool, not just a number — speaks to collectors, "
            "dealers and anyone shipping printed collectibles."
        ),
    ),
    AIImagePlanItem(
        name="Image 6 — Trust: Ultra PRO, trusted since 1952",
        role="trust",
        background="Black with red top-line, white headline (brand close)",
        purpose="Close on brand authority — the collector's default choice.",
        visual=(
            "Hero of the pack with a small lifestyle inset (a collector loading magazines "
            "into toploaders at a tidy desk). Brand line bottom: 'ULTRA PRO — protecting "
            "collections since 1952 · trusted by collectors worldwide'. Red badge: "
            "'SINCE 1952'."
        ),
        overlay="TRUSTED SINCE 1952.",
        overlay_sub="Ultra PRO — protecting magazine and card collections worldwide.",
        props=["pack hero", "collector lifestyle inset", "since-1952 red badge"],
        lighting="Premium catalog light on black; warm inset for the lifestyle moment.",
        why_it_works=(
            "Against unbranded bargain holders, heritage and trust are the deciding signals. "
            "'Since 1952' is Ultra PRO's honest, compliant authority claim."
        ),
    ),
    AIImagePlanItem(
        name="Image 7 — Range: the Ultra PRO storage system",
        role="close",
        background="White with black/red Ultra PRO chrome",
        purpose="Cross-sell the wider protection range.",
        visual=(
            "Clean line-up: magazine toploaders (this product) alongside card toploaders, "
            "sleeves, pocket pages and a storage box — shown as a coordinated system. Small "
            "labels; the magazine toploaders gently highlighted. Caption: 'Protect it. Store "
            "it. — the Ultra PRO way.'"
        ),
        overlay="PROTECT IT. STORE IT.",
        overlay_sub="Pair with Ultra PRO toploaders, sleeves, pages and storage boxes.",
        props=["magazine toploaders (highlighted)", "card toploaders", "sleeves", "pocket pages", "storage box"],
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
        headline="SEE IT. SHIELD IT. SINCE 1952.",
        body=(
            "High-impact rigid PVC magazine toploaders keep covers fully visible through an "
            "ultra-clear front while guarding large-format items against bending, dust and "
            "handling wear. Sized for 9\" x 11-1/4\" magazines, programs and documents up to "
            "7mm thick — protection trusted by collectors since 1952."
        ),
        visual="Wide black banner, red top-line, bold white headline left; a loaded magazine toploader with a crisp cover right. Ultra PRO logo upper-left.",
        alt="Ultra PRO 9x11-1/4 magazine toploader banner: rigid PVC, ultra-clear, up to 7mm, since 1952.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): Why these toploaders",
        role="a+_carousel",
        headline="WHY ULTRA PRO MAGAZINE TOPLOADERS",
        body=(
            "Tile 1: <b>HIGH-IMPACT RIGID PVC</b> — Sturdy, bend-resistant protection.<br/>"
            "Tile 2: <b>ULTRA-CLEAR FRONT</b> — Covers &amp; artwork stay fully visible.<br/>"
            "Tile 3: <b>LARGE 9\" x 11-1/4\" FIT</b> — For magazines, programs &amp; documents.<br/>"
            "Tile 4: <b>HOLDS UP TO 7MM</b> — Fits thick publications with room to spare.<br/>"
            "Tile 5: <b>10-PACK · SINCE 1952</b> — Trusted collectible protection worldwide."
        ),
        visual="5 square tiles, red accent corner each, black/white icons (shield · film · ruler · caliper · badge).",
        alt="Five A+ tiles: rigid PVC, ultra-clear, 9x11-1/4 fit, up to 7mm, 10-pack since 1952.",
    ),
    AIModule(
        name="Module 3 — Banner: Store, display & ship",
        role="a+_banner",
        headline="STORE IT. DISPLAY IT. SHIP IT.",
        body=(
            "Rigid top-loading design makes it easy to slide magazines and documents in and "
            "out while the stiff PVC body keeps them flat and protected — on the shelf, "
            "standing on display, or boxed for shipping. Ten toploaders per pack for "
            "collectors &amp; dealers alike."
        ),
        visual="Banner split: loaded toploaders standing on a shelf left; a flat stack ready to ship right. Black/red Ultra PRO styling.",
        alt="A+ banner on storing, displaying and shipping magazines in rigid Ultra PRO toploaders.",
    ),
    AIModule(
        name="Module 4 — Carousel (4 tiles): The Ultra PRO storage system",
        role="a+_carousel",
        headline="PROTECT IT. STORE IT. ULTRA PRO WAY.",
        body=(
            "Tile 1: <b>MAGAZINE TOPLOADERS</b> — Rigid 9\" x 11-1/4\" holders (this product).<br/>"
            "Tile 2: <b>CARD TOPLOADERS</b> — Rigid protection for key cards.<br/>"
            "Tile 3: <b>SLEEVES &amp; PAGES</b> — Everyday protection &amp; organization.<br/>"
            "Tile 4: <b>STORAGE BOXES</b> — Organise and archive full collections."
        ),
        visual="4 coordinated product tiles, red accent corners, consistent catalog styling.",
        alt="Four A+ tiles showing the Ultra PRO storage system: magazine toploaders, card toploaders, sleeves, boxes.",
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
