"""Ultra PRO — 11" x 14" Toploader (20 ct)  [Listing 64]
NEUES Format: Titel/Bullets/Backend kommen aus dem SEO-Sheet (listing.xlsx),
Q&A + Vergleich aus dem A+ Premium Sheet (aplus.xlsx). Bildregie handgeschrieben,
100% produktspezifisch, im Ultra-PRO-Katalogstil (schwarz/rot/weiss).

Grosse starre 11x14-Toploader fuer Fotos, Prints, Artwork, Poster, Dokumente
und Zertifikate — KEIN Trading-Card-Fokus.

Marketplace: amazon.com (US). ASIN B0019TSI4Q.
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

PLAN_NO = "64"
ASIN = "B0019TSI4Q"
EXCEL = HERE / "listing.xlsx"
APLUS = HERE / "aplus.xlsx"


# ===== produktspezifische Bildregie (Ultra-PRO-Katalogstil, EN Overlays) =====

IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="Clean white for slot-1 compliance; the CTR versions add a black lower band with a thin red top-line (Ultra PRO catalog look). Same framing across all 3.",
        purpose="Win the click in a grid of look-alike rigid photo protectors. Ship all 3, keep the winner.",
        visual=(
            "Mock ALL 3 options. Product exactly as real: a rigid 11x14 toploader holding a real "
            "photo/print, super clear, plus the 20-count pack behind it. ONE callout each, product "
            "dominant.\n\n"
            "OPTION A — CLARITY: toploader with a colourful 11x14 photo inside, detail crisp through "
            "the rigid front. Badge (red): 'SUPER CLEAR'.\n"
            "OPTION B — PACK VALUE: the 20 toploaders fanned. Badge (red): '20 TOPLOADERS'.\n"
            "OPTION C — RIGID: toploader flexed flat with a print inside, no bending. Badge (red): "
            "'RIGID PVC 11x14'.\n\n"
            "Across all 3: white background, red badge ~6% of frame, same lighting."
        ),
        overlay="(one callout per option)",
        overlay_sub="3 hero options shipped — A/B test, keep the winner.",
        props=["A: 11x14 toploader with photo inside", "B: 20-count pack fanned", "C: rigid toploader flexed flat"],
        lighting="Bright, even studio light; crisp catch-light so the rigid clear front reads on white.",
        why_it_works=(
            "Three triggers: clarity (see your print), pack value (20), rigid protection. One "
            "callout each — readable at thumbnail size."
        ),
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: rigid PVC, keeps large prints flat",
        role="hook",
        background="Black with a thin red top-line and a bold white headline (Ultra PRO catalog)",
        purpose="Own the #1 reason buyers pick a toploader over a soft sleeve: rigid, no bending.",
        visual=(
            "Large macro: an 11x14 photo inside the rigid toploader held horizontally, staying "
            "perfectly flat with no sag. Thin red callout lines: 'high-impact rigid PVC', 'holds "
            "large prints flat', 'guards against bending'. White bold headline top: 'RIGID. FLAT. "
            "PROTECTED.'"
        ),
        overlay="RIGID PVC PROTECTION.",
        overlay_sub="High-impact rigid PVC holds 11x14 photos and prints flat, reducing bending.",
        props=["11x14 photo held flat in rigid toploader (macro)", "red callout lines", "no-sag edge detail"],
        lighting="Dramatic catalog light on black; strong edge-light on the rigid clear front.",
        why_it_works=(
            "Large prints and photos curl and crease in soft sleeves. A macro of a flat, supported "
            "11x14 print proves the rigid PVC does the one job buyers want most."
        ),
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: super-clear viewing, no removal",
        role="educate",
        background="White with a black/red Ultra PRO footer band",
        purpose="Defend quality: see and identify contents without handling the print.",
        visual=(
            "Split card. LEFT: the toploader with a photo, a small eye icon 'SUPER CLEAR'. RIGHT: "
            "three stacked feature rows with red check-icons — 'View photos & prints without "
            "removing', 'Guards against dust, dirt & handling', 'Clean presentation for display & "
            "storage'. Footer band: 'Time-tested protection — trusted since 1952.'"
        ),
        overlay="SEE IT. PROTECT IT.",
        overlay_sub="Super-clear front keeps photos, prints and document details fully visible.",
        props=["toploader + photo", "3 feature rows with red checks", "since-1952 footer band"],
        lighting="Flat, even catalog light; feature icons legible at thumbnail size.",
        why_it_works=(
            "Buyers protecting photos and documents want to identify contents at a glance. Showing "
            "crisp viewing without removal separates this from cloudy bargain sleeves."
        ),
    ),
    AIImagePlanItem(
        name="Image 4 — Fit: sized for 11x14 flat media",
        role="desire",
        background="White with a red dimension callout (Ultra PRO)",
        purpose="Remove the #1 buyer question — will my photos and prints fit?",
        visual=(
            "An 11x14 print centred in the toploader with a clean dimension callout: 'Holds flat "
            "items up to 11\" x 14\"'. Small ruler graphic along two edges. A short note: 'Photos · "
            "prints · artwork · posters · certificates · documents.'"
        ),
        overlay="FITS UP TO 11X14.",
        overlay_sub="Sized for photos, prints, posters and documents up to 11 x 14 inches.",
        props=["11x14 print in toploader", "dimension callout", "edge ruler graphic"],
        lighting="Bright, even; the dimension callout must read clearly.",
        why_it_works=(
            "Wrong-size protectors are the top return reason in this category. A precise 11x14 fit "
            "callout sets honest expectations and prevents mis-buys."
        ),
    ),
    AIImagePlanItem(
        name="Image 5 — Pack: 20 count for collections, studios & offices",
        role="desire",
        background="Black with red accents (Ultra PRO catalog)",
        purpose="Make the pack value and use-cases obvious.",
        visual=(
            "The 20-count set with several loaded toploaders organised upright. Icon-stats: '20 "
            "TOPLOADERS', 'Home collections', 'Studios & offices', 'Display & transport'. Clean, "
            "catalog-style layout."
        ),
        overlay="20 RIGID TOPLOADERS.",
        overlay_sub="Protect multiple photos, prints and documents at home, studio or office.",
        props=["20-count set", "loaded toploaders upright", "4 icon-stats"],
        lighting="Catalog light on black; product and stats clearly separated.",
        why_it_works=(
            "Shows the quantity is a working tool for real use-cases — collectors, artists, "
            "photographers and offices alike."
        ),
    ),
    AIImagePlanItem(
        name="Image 6 — Trust: Ultra PRO, trusted since 1952",
        role="trust",
        background="Black with red top-line, white headline (brand close)",
        purpose="Close on brand authority — the practical default for flat-media protection.",
        visual=(
            "Hero of the pack with a small lifestyle inset (a person sliding a framed-size print "
            "into a toploader at a tidy desk). Brand line bottom: 'ULTRA PRO — protecting photos, "
            "prints and collections since 1952'. Red badge: 'SINCE 1952'."
        ),
        overlay="TRUSTED SINCE 1952.",
        overlay_sub="Ultra PRO — practical protection and storage for photos, prints and documents.",
        props=["pack hero", "print-loading lifestyle inset", "since-1952 red badge"],
        lighting="Premium catalog light on black; warm inset for the lifestyle moment.",
        why_it_works=(
            "Against unbranded bargain protectors, heritage and trust are the deciding signals. "
            "'Since 1952' is Ultra PRO's honest, compliant authority claim."
        ),
    ),
    AIImagePlanItem(
        name="Image 7 — Range: the Ultra PRO storage & display system",
        role="close",
        background="White with black/red Ultra PRO chrome",
        purpose="Cross-sell the wider flat-media protection range.",
        visual=(
            "Clean line-up: 11x14 toploaders (this product) alongside photo pages, rigid photo/art "
            "holders and a storage box — shown as a coordinated system. Small labels; the 11x14 "
            "toploaders gently highlighted. Caption: 'Protect it. Store it. Display it. — the Ultra "
            "PRO way.'"
        ),
        overlay="PROTECT IT. STORE IT.",
        overlay_sub="Display it — pair with Ultra PRO photo pages, holders and storage boxes.",
        props=["11x14 toploaders (highlighted)", "photo pages", "rigid holders", "storage box"],
        lighting="Bright, even; coordinated family shot.",
        why_it_works=(
            "Turns one purchase into a system sale and reinforces Ultra PRO as the one-stop brand "
            "for protecting photos, prints and documents."
        ),
    ),
]


# ===== 4 kreative Module + Q&A/Vergleich aus dem A+ Sheet =====

CREATIVE_MODULES = [
    AIModule(
        name="Module 1 — Brand banner",
        role="a+_banner",
        headline="RIGID. CLEAR. SINCE 1952.",
        body=(
            "High-impact rigid PVC 11x14 toploaders hold photos, prints, artwork, posters and "
            "documents flat while keeping details fully visible. Guards against dust, dirt and "
            "everyday handling — practical protection trusted by collectors since 1952."
        ),
        visual="Wide black banner, red top-line, bold white headline left; a rigid 11x14 toploader with a crisp photo right. Ultra PRO logo upper-left.",
        alt="Ultra PRO 11x14 toploader banner: rigid PVC, super clear, for photos and prints, since 1952.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): Why these toploaders",
        role="a+_carousel",
        headline="WHY ULTRA PRO 11X14 TOPLOADERS",
        body=(
            "Tile 1: <b>RIGID PVC</b> — High-impact support holds large prints flat.<br/>"
            "Tile 2: <b>SUPER CLEAR</b> — View photos &amp; documents without removing.<br/>"
            "Tile 3: <b>11X14 FIT</b> — Sized for photos, prints, posters &amp; certificates.<br/>"
            "Tile 4: <b>20-COUNT PACK</b> — For collections, studios and offices.<br/>"
            "Tile 5: <b>SINCE 1952</b> — Trusted protection worldwide."
        ),
        visual="5 square tiles, red accent corner each, black/white icons (shield · eye · ruler · stack · badge).",
        alt="Five A+ tiles: rigid PVC, super clear, 11x14 fit, 20-count, since 1952.",
    ),
    AIModule(
        name="Module 3 — Banner: Flat-media protection",
        role="a+_banner",
        headline="HOLD LARGE PRINTS FLAT.",
        body=(
            "Made from durable, high-impact rigid PVC so 11x14 photos, prints and documents stay "
            "flat and supported — reducing bending and shielding contents from dust, dirt and "
            "handling. Store, display or transport with confidence."
        ),
        visual="Banner split: macro of an 11x14 print held flat in the rigid toploader left; loaded toploaders in a storage box right. Black/red Ultra PRO styling.",
        alt="A+ banner on rigid PVC protection that keeps large photos and prints flat.",
    ),
    AIModule(
        name="Module 4 — Carousel (4 tiles): The storage & display system",
        role="a+_carousel",
        headline="PROTECT IT. STORE IT. DISPLAY IT.",
        body=(
            "Tile 1: <b>11X14 TOPLOADERS</b> — Rigid clear protectors (this product).<br/>"
            "Tile 2: <b>PHOTO PAGES</b> — Organise smaller photos in binders.<br/>"
            "Tile 3: <b>RIGID HOLDERS</b> — Firm support for prints &amp; art.<br/>"
            "Tile 4: <b>STORAGE BOXES</b> — Archive and transport flat media."
        ),
        visual="4 coordinated product tiles, red accent corners, consistent catalog styling.",
        alt="Four A+ tiles showing the Ultra PRO storage system: toploaders, photo pages, holders, boxes.",
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
