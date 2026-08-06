"""Ultra PRO — 8x10 Photo Pages / Refill Pages (25 ct)  [Listing 60]
NEUES Format: Titel/Bullets/Backend kommen aus dem SEO-Sheet (listing.xlsx),
Q&A + Vergleich aus dem A+ Premium Sheet (aplus.xlsx). Bildregie handgeschrieben,
100% produktspezifisch, im Ultra-PRO-Katalogstil (schwarz/rot/weiss).

Kein Trading-Card-Fokus — hier Foto / Print / Album / Memorabilia.
Marketplace: amazon.com (US). ASIN B01MS1KGY8.
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

PLAN_NO = "60"
ASIN = "B01MS1KGY8"
EXCEL = HERE / "listing.xlsx"
APLUS = HERE / "aplus.xlsx"


# ===== produktspezifische Bildregie (Ultra-PRO-Katalogstil, EN Overlays) =====

IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="Clean white for slot-1 compliance; the CTR versions add a black lower band with a thin red top-line (Ultra PRO catalog look). Same framing across all 3.",
        purpose="Win the click in a grid of look-alike photo sleeves. Ship all 3, keep the winner.",
        visual=(
            "Mock ALL 3 options. Product exactly as real: a clear 8x10 photo page holding real "
            "family/print photos, plus the 25-page pack behind it. ONE callout each, product "
            "dominant.\n\n"
            "OPTION A — CLARITY: a single page with a crisp 8x10 photo, image sharp through the "
            "sleeve. Badge (red): 'HIGH-CLARITY'.\n"
            "OPTION B — PACK VALUE: the 25-page pack fanned, several pages visible. Badge (red): "
            "'25 PAGES · 50 PHOTOS'.\n"
            "OPTION C — ARCHIVAL: page + small acid-free / no-PVC / UV icons. Badge: 'ACID-FREE · "
            "NO PVC'.\n\n"
            "Across all 3: white background, red badge ~6% of frame, same lighting."
        ),
        overlay="(one callout per option)",
        overlay_sub="3 hero options shipped — A/B test, keep the winner.",
        props=["A: page with 8x10 photo inside", "B: 25-page pack fanned", "C: page + acid-free/no-PVC/UV icons"],
        lighting="Bright, even studio light; crisp catch-light so the high-clarity film reads on white.",
        why_it_works=(
            "Three triggers: clarity (see your photo), pack value (25 pages / 50 photos), archival "
            "safety. One callout each — readable at thumbnail size."
        ),
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: High-clarity, photos stay visible both sides",
        role="hook",
        background="Black with a thin red top-line and a bold white headline (Ultra PRO catalog)",
        purpose="Own the #1 reason people sleeve photos: see the image, protect the image.",
        visual=(
            "Large macro: an 8x10 photo sliding into the clear page, the image sharp and true-colour "
            "through the film, a second photo visible on the reverse pocket. Thin red callout lines: "
            "'high-clarity polypropylene', 'front &amp; back pockets', 'view both sides — no removal'. "
            "White bold headline top: 'SEE IT. PROTECT IT.'"
        ),
        overlay="HIGH-CLARITY PAGES.",
        overlay_sub="Clear polypropylene keeps photos and prints fully visible on both sides.",
        props=["8x10 photo sliding into page (macro)", "reverse pocket with second photo", "red callout lines"],
        lighting="Dramatic catalog light on black; strong edge-light on the clear film.",
        why_it_works=(
            "Buyers sleeve photos to display AND protect. A true-colour macro proves the film is "
            "genuinely high-clarity — the single strongest visual argument in the category."
        ),
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: Archival-safe, acid-free, PVC-free & UV",
        role="educate",
        background="White with a black/red Ultra PRO footer band",
        purpose="Defend quality: why acid-free + PVC-free + UV matters for long-term photo storage.",
        visual=(
            "Split card. LEFT: a page holding a photo, a small shield icon 'ARCHIVAL-SAFE'. RIGHT: "
            "three stacked feature rows with red check-icons — 'ACID-FREE polypropylene', 'PVC-FREE "
            "(no plasticiser migration)', 'UV protection against fading, dust &amp; fingerprints'. "
            "Footer band: 'Time-tested photo protection — trusted since 1952.'"
        ),
        overlay="ACID-FREE. PVC-FREE.",
        overlay_sub="Archival-safe, UV-protected pages for long-term, worry-free photo storage.",
        props=["page + photo", "3 feature rows with red checks", "since-1952 footer band"],
        lighting="Flat, even catalog light; feature icons legible at thumbnail size.",
        why_it_works=(
            "People preserving family photos and prints filter on archival safety. Naming acid-free "
            "+ PVC-free + UV with a clear 'why it matters' separates this from unlabeled bargain pages."
        ),
    ),
    AIImagePlanItem(
        name="Image 4 — Fit: sized for 8x10 photos, fits 8.5\"x11\" albums",
        role="desire",
        background="White with a red dimension callout (Ultra PRO)",
        purpose="Remove the #1 buyer question — will my photos and my binder fit?",
        visual=(
            "An 8x10 photo centred in the page with a clean dimension callout: 'Holds 8x10 photos "
            "&amp; prints'. The 3-hole punched spine highlighted against a standard 3-ring binder: "
            "'Fits 8.5\" x 11\" albums &amp; 3-ring binders'. Small ruler graphic along two edges."
        ),
        overlay="FITS 8x10 PHOTOS.",
        overlay_sub="Holds 8x10 prints; 3-hole spine fits 8.5\"x11\" albums and 3-ring binders.",
        props=["8x10 photo in page", "3-hole spine + binder rings", "dimension + ruler graphic"],
        lighting="Bright, even; the dimension and 3-hole callouts must read clearly.",
        why_it_works=(
            "Wrong size or wrong hole-spacing is the top return reason for refill pages. Precise "
            "photo-size and binder-fit callouts set honest expectations and prevent mis-buys."
        ),
    ),
    AIImagePlanItem(
        name="Image 5 — Pack: 25 pages hold up to 50 photos",
        role="desire",
        background="Black with red accents (Ultra PRO catalog)",
        purpose="Make the pack value and use-cases obvious.",
        visual=(
            "The 25-page pack loaded into a binder with photos on front and back pockets. Icon-stats: "
            "'25 PAGES', 'UP TO 50 PHOTOS', 'Front &amp; back pockets', 'Family, travel &amp; event "
            "prints'. Clean, catalog-style layout."
        ),
        overlay="25 PAGES. 50 PHOTOS.",
        overlay_sub="Front and back pockets organize family, travel and event prints in one album.",
        props=["25-page pack in binder", "photos front &amp; back", "4 icon-stats"],
        lighting="Catalog light on black; product and stats clearly separated.",
        why_it_works=(
            "Shows the quantity is a working album system, not just a number — speaks to families, "
            "hobbyists and print collectors alike."
        ),
    ),
    AIImagePlanItem(
        name="Image 6 — Trust: Ultra PRO, trusted since 1952",
        role="trust",
        background="Black with red top-line, white headline (brand close)",
        purpose="Close on brand authority — the collector's and family's default choice.",
        visual=(
            "Hero of the pack with a small lifestyle inset (someone filing photos into an album at a "
            "tidy desk). Brand line bottom: 'ULTRA PRO — protecting photos and collections since 1952 "
            "· made in the USA with imported materials'. Red badge: 'SINCE 1952'."
        ),
        overlay="TRUSTED SINCE 1952.",
        overlay_sub="Ultra PRO — protecting photos, prints and collections worldwide.",
        props=["pack hero", "photo-filing lifestyle inset", "since-1952 red badge"],
        lighting="Premium catalog light on black; warm inset for the lifestyle moment.",
        why_it_works=(
            "Against unbranded bargain pages, heritage and trust are the deciding signals. 'Since "
            "1952' is Ultra PRO's honest, compliant authority claim."
        ),
    ),
    AIImagePlanItem(
        name="Image 7 — Range: the Ultra PRO photo storage system",
        role="close",
        background="White with black/red Ultra PRO chrome",
        purpose="Cross-sell the wider photo/album protection range.",
        visual=(
            "Clean line-up: 8x10 photo pages (this product) alongside 4x6 and 5x7 photo pages, an "
            "album/binder and a photo storage box — shown as a coordinated system. Small labels; the "
            "8x10 pages gently highlighted. Caption: 'Sleeve it. Album it. Store it. — the Ultra PRO "
            "way.'"
        ),
        overlay="SLEEVE IT. STORE IT.",
        overlay_sub="Pair 8x10 pages with 4x6 and 5x7 pages, albums and photo storage boxes.",
        props=["8x10 photo pages (highlighted)", "4x6 &amp; 5x7 pages", "album/binder", "photo storage box"],
        lighting="Bright, even; coordinated family shot.",
        why_it_works=(
            "Turns one purchase into a system sale and reinforces Ultra PRO as the one-stop photo "
            "and collection brand."
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
            "High-clarity 8x10 photo pages keep your prints fully visible on both sides while "
            "guarding against fading, dust and fingerprints. Acid-free, PVC-free, UV-protected and "
            "archival-safe — photo protection trusted by collectors since 1952."
        ),
        visual="Wide black banner, red top-line, bold white headline left; a clear page with a crisp 8x10 photo right. Ultra PRO logo upper-left.",
        alt="Ultra PRO 8x10 photo pages banner: high-clarity, acid-free, PVC-free, UV, since 1952.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): Why these pages",
        role="a+_carousel",
        headline="WHY ULTRA PRO PHOTO PAGES",
        body=(
            "Tile 1: <b>HIGH-CLARITY</b> — Photos and prints stay fully visible, both sides.<br/>"
            "Tile 2: <b>ACID-FREE &amp; PVC-FREE</b> — Archival-safe, UV-protected storage.<br/>"
            "Tile 3: <b>8x10 FIT</b> — 3-hole spine fits 8.5\" x 11\" albums &amp; binders.<br/>"
            "Tile 4: <b>25-PAGE PACK</b> — Holds up to 50 photos front &amp; back.<br/>"
            "Tile 5: <b>SINCE 1952</b> — Trusted photo protection worldwide."
        ),
        visual="5 square tiles, red accent corner each, black/white icons (film · shield · binder · stack · badge).",
        alt="Five A+ tiles: high-clarity, acid-free/PVC-free, 8x10 fit, 25-page pack, since 1952.",
    ),
    AIModule(
        name="Module 3 — Banner: Archival protection",
        role="a+_banner",
        headline="ARCHIVAL-SAFE. WORRY-FREE.",
        body=(
            "Made from acid-free, PVC-free polypropylene with UV protection, so there is no "
            "plasticiser migration and no fading onto your prints. Keep 8x10 photos clean and "
            "covered — in the album, in the box, or on the shelf."
        ),
        visual="Banner split: macro of the clear film + acid-free/PVC-free/UV shield icons left; a binder of photo pages right. Black/red Ultra PRO styling.",
        alt="A+ banner on archival-safe acid-free, PVC-free, UV-protected photo storage.",
    ),
    AIModule(
        name="Module 4 — Carousel (4 tiles): The photo storage system",
        role="a+_carousel",
        headline="SLEEVE IT. ALBUM IT. STORE IT.",
        body=(
            "Tile 1: <b>8x10 PHOTO PAGES</b> — High-clarity refill sleeves (this product).<br/>"
            "Tile 2: <b>4x6 &amp; 5x7 PAGES</b> — Match every print size in one binder.<br/>"
            "Tile 3: <b>ALBUMS &amp; BINDERS</b> — 8.5\" x 11\" 3-ring, ready for refills.<br/>"
            "Tile 4: <b>STORAGE BOXES</b> — Organise and archive full photo collections."
        ),
        visual="4 coordinated product tiles, red accent corners, consistent catalog styling.",
        alt="Four A+ tiles showing the Ultra PRO photo storage system: 8x10 pages, other sizes, albums, boxes.",
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
