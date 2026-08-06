"""Ultra PRO — 24" x 36" Toploader (Rigid Poster Protector)  [Listing 70]
NEUES Format: Titel/Bullets/Backend kommen aus dem SEO-Sheet (listing.xlsx),
Q&A + Vergleich aus dem A+ Premium Sheet (aplus.xlsx). Bildregie handgeschrieben,
100% produktspezifisch, im Ultra-PRO-Katalogstil (schwarz/rot/weiss).

Grosser starrer Toploader fuer uebergrosse Poster, Prints, Fotos & Dokumente —
Fokus auf MASSSTAB (24x36) und STARREN Schutz. KEIN Trading-Card-Fokus.

Marketplace: amazon.com (US). ASIN B004L17318.
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

PLAN_NO = "70"
ASIN = "B004L17318"
EXCEL = HERE / "listing.xlsx"
APLUS = HERE / "aplus.xlsx"


# ===== produktspezifische Bildregie (Ultra-PRO-Katalogstil, EN Overlays) =====

IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="Clean white for slot-1 compliance; the CTR versions add a black lower band with a thin red top-line (Ultra PRO catalog look). Same framing across all 3.",
        purpose="Win the click in a grid of small card holders by showing true poster scale. Ship all 3, keep the winner.",
        visual=(
            "Mock ALL 3 options. Product exactly as real: the rigid 24\" x 36\" toploader holding a "
            "real full-size poster (generic, non-branded artwork), ultra-clear front. ONE callout "
            "each, product dominant, poster fully readable through the front.\n\n"
            "OPTION A — SCALE: the loader shown at true 24x36 scale, a hand or standard object for "
            "size reference. Badge (red): '24\" X 36\"'.\n"
            "OPTION B — RIGID: edge-on angle showing the thick rigid panels. Badge (red): 'RIGID "
            "PLASTIC'.\n"
            "OPTION C — MULTI-USE: poster + a print and a document fanned beside it. Badge: "
            "'POSTERS · PRINTS · DOCS'.\n\n"
            "Across all 3: white background, red badge ~6% of frame, same lighting."
        ),
        overlay="(one callout per option)",
        overlay_sub="3 hero options shipped — A/B test, keep the winner.",
        props=["A: 24x36 loader with size reference", "B: edge-on rigid panels", "C: loader + print + document"],
        lighting="Bright, even studio light; crisp catch-light so the ultra-clear front reads on white.",
        why_it_works=(
            "Three triggers: true 24x36 scale, rigid protection and multi-purpose use. One callout "
            "each — readable at thumbnail size against small card-holder look-alikes."
        ),
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: oversized 24 x 36 format",
        role="hook",
        background="Black with a thin red top-line and a bold white headline (Ultra PRO catalog)",
        purpose="Lead with the one thing card holders can't do — hold a full 24x36 poster.",
        visual=(
            "Large hero: the toploader holding a full-size 24\" x 36\" poster, standing upright with "
            "a subtle scale reference (a standard shelf or a person's forearm at the edge). Thin red "
            "callout lines: 'fits full 24 x 36 in posters', 'oversized rigid holder', 'no folding, "
            "no rolling'. White bold headline top: 'BIG FORMAT. FULLY PROTECTED.'"
        ),
        overlay="BIG 24 X 36 INCHES.",
        overlay_sub="Oversized rigid toploader sized for full 24 x 36 in posters and prints.",
        props=["24x36 loader with poster upright", "scale reference", "red callout lines"],
        lighting="Dramatic catalog light on black; strong edge-light to show the loader's size.",
        why_it_works=(
            "Size is the category's buying trigger — most 'toploaders' are card-size. Showing a real "
            "24x36 poster at scale instantly signals this is the oversized one."
        ),
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: rigid plastic protection",
        role="educate",
        background="White with a black/red Ultra PRO footer band",
        purpose="Defend the core benefit — rigid structure that stops bends, creases and corner damage.",
        visual=(
            "Split card. LEFT: an edge-on macro of the thick rigid panels, a small shield icon "
            "'RIGID STRUCTURE'. RIGHT: three stacked feature rows with red check-icons — 'DURABLE "
            "RIGID PLASTIC (holds its shape)', 'ADDED STRUCTURE (no bends or creases)', 'GUARDS "
            "CORNERS &amp; EDGES during handling'. Footer band: 'Time-tested collectible protection "
            "— trusted since 1952.'"
        ),
        overlay="RIGID PLASTIC HOLDER.",
        overlay_sub="Durable rigid plastic adds structure and guards against bends and creases.",
        props=["edge-on rigid panels macro", "3 feature rows with red checks", "since-1952 footer band"],
        lighting="Flat, even catalog light; feature icons legible at thumbnail size.",
        why_it_works=(
            "Buyers of large-format holders fear bent posters. Naming the rigid construction with a "
            "clear 'why it matters' separates this from flimsy soft sleeves."
        ),
    ),
    AIImagePlanItem(
        name="Image 4 — Desire: ultra-clear display",
        role="desire",
        background="White with a red accent callout (Ultra PRO)",
        purpose="Show items stay fully visible — store and display without taking them out.",
        visual=(
            "The toploader with a colourful poster, cover art crisp and true-colour through the clear "
            "front. Thin red callout: 'ultra-clear plastic — view without removing'. A small note: "
            "'See titles, artwork and detail at a glance.'"
        ),
        overlay="ULTRA-CLEAR DISPLAY.",
        overlay_sub="Clear plastic shows artwork and titles while items stay fully protected.",
        props=["toploader with colourful poster", "true-colour front", "red clarity callout"],
        lighting="Bright, even; strong edge-light so the ultra-clear front reads true-colour.",
        why_it_works=(
            "Collectors and artists want to display AND protect. Proving the front is genuinely "
            "clear is the strongest desire trigger for a display holder."
        ),
    ),
    AIImagePlanItem(
        name="Image 5 — Desire: multi-purpose storage",
        role="desire",
        background="Black with red accents (Ultra PRO catalog)",
        purpose="Widen the use-cases beyond posters to lift perceived value.",
        visual=(
            "The loader alongside the flat items it fits: a poster, a magazine, a large print, a "
            "sheet and a document, laid out clean and catalog-style. Icon-stats: 'POSTERS', "
            "'MAGAZINES', 'PRINTS &amp; PHOTOS', 'DOCUMENTS &amp; SHEETS'."
        ),
        overlay="POSTERS. PRINTS. DOCS.",
        overlay_sub="Store posters, magazines, photos, sheets and documents in one rigid holder.",
        props=["loader + poster + magazine + print + document", "4 icon-stats"],
        lighting="Catalog light on black; product and stats clearly separated.",
        why_it_works=(
            "One holder that protects many flat collectibles reads as more value — speaks to "
            "collectors, artists, photographers and home offices alike."
        ),
    ),
    AIImagePlanItem(
        name="Image 6 — Trust: Ultra PRO, trusted since 1952",
        role="trust",
        background="Black with red top-line, white headline (brand close)",
        purpose="Close on brand authority — the collector's default choice.",
        visual=(
            "Hero of the toploader with a small lifestyle inset (a collector or artist sliding a "
            "poster into the loader at a tidy desk). Brand line bottom: 'ULTRA PRO — protecting "
            "collections since 1952 · trusted by collectors worldwide'. Red badge: 'SINCE 1952'."
        ),
        overlay="TRUSTED SINCE 1952.",
        overlay_sub="Ultra PRO — protecting posters, prints and collectibles worldwide.",
        props=["toploader hero", "collector lifestyle inset", "since-1952 red badge"],
        lighting="Premium catalog light on black; warm inset for the lifestyle moment.",
        why_it_works=(
            "Against unbranded oversized sleeves, heritage and trust are the deciding signals. "
            "'Since 1952' is Ultra PRO's honest, compliant authority claim."
        ),
    ),
    AIImagePlanItem(
        name="Image 7 — Range: the Ultra PRO storage system",
        role="close",
        background="White with black/red Ultra PRO chrome",
        purpose="Cross-sell the wider protection range for every size.",
        visual=(
            "Clean line-up: the 24x36 toploader (this product) alongside smaller toploaders, sleeves "
            "and a storage solution — shown as a coordinated system from card-size to poster-size. "
            "Small labels; the 24x36 loader gently highlighted. Caption: 'Protect every size — the "
            "Ultra PRO way.'"
        ),
        overlay="STORE IT. DISPLAY IT.",
        overlay_sub="Pair with Ultra PRO sleeves, toploaders and storage for every collectible.",
        props=["24x36 toploader (highlighted)", "smaller toploaders", "sleeves", "storage solution"],
        lighting="Bright, even; coordinated family shot.",
        why_it_works=(
            "Turns one purchase into a system sale and reinforces Ultra PRO as the one-stop "
            "collector brand across every size."
        ),
    ),
]


# ===== 4 kreative Module + Q&A/Vergleich aus dem A+ Sheet =====

CREATIVE_MODULES = [
    AIModule(
        name="Module 1 — Brand banner",
        role="a+_banner",
        headline="STORE IT. DISPLAY IT. SINCE 1952.",
        body=(
            "The Ultra PRO 24 x 36 in toploader keeps full-size posters, prints, photos and "
            "documents flat, rigid and fully visible. Durable rigid plastic adds structure and guards "
            "against bends, creases and corner damage — oversized collectible protection trusted "
            "by collectors since 1952."
        ),
        visual="Wide black banner, red top-line, bold white headline left; the 24x36 loader holding a crisp poster right. Ultra PRO logo upper-left.",
        alt="Ultra PRO 24 x 36 toploader banner: oversized, rigid, ultra-clear, since 1952.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): Why this toploader",
        role="a+_carousel",
        headline="WHY ULTRA PRO 24 x 36",
        body=(
            "Tile 1: <b>BIG 24 x 36 SIZE</b> — Sized for full oversized posters and prints.<br/>"
            "Tile 2: <b>RIGID PLASTIC</b> — Added structure, no bends or creases.<br/>"
            "Tile 3: <b>ULTRA-CLEAR FRONT</b> — View artwork without removing it.<br/>"
            "Tile 4: <b>MULTI-PURPOSE</b> — Posters, magazines, prints, sheets &amp; documents.<br/>"
            "Tile 5: <b>SINCE 1952</b> — Trusted collectible protection worldwide."
        ),
        visual="5 square tiles, red accent corner each, black/white icons (ruler · panel · eye · stack · badge).",
        alt="Five A+ tiles: big 24x36 size, rigid plastic, ultra-clear, multi-purpose, since 1952.",
    ),
    AIModule(
        name="Module 3 — Banner: Rigid oversized protection",
        role="a+_banner",
        headline="OVERSIZED. RIGID. WORRY-FREE.",
        body=(
            "Made from durable rigid plastic with an ultra-clear front, this oversized toploader holds "
            "its shape so large posters and prints stay flat and protected — during storage, "
            "handling and display. See every detail without ever taking the item out."
        ),
        visual="Banner split: edge-on macro of the rigid panels left; the loader holding a full poster upright right. Black/red Ultra PRO styling.",
        alt="A+ banner on oversized rigid plastic protection for 24 x 36 posters and prints.",
    ),
    AIModule(
        name="Module 4 — Carousel (4 tiles): What it protects",
        role="a+_carousel",
        headline="ONE HOLDER, MANY USES",
        body=(
            "Tile 1: <b>POSTERS</b> — Keep full-size posters flat and rigid.<br/>"
            "Tile 2: <b>PRINTS &amp; PHOTOS</b> — Protect artwork and large photos.<br/>"
            "Tile 3: <b>MAGAZINES &amp; SHEETS</b> — Store oversized flat collectibles.<br/>"
            "Tile 4: <b>DOCUMENTS</b> — Preserve important papers, clean and covered."
        ),
        visual="4 coordinated use-case tiles, red accent corners, consistent catalog styling.",
        alt="Four A+ tiles showing what the Ultra PRO 24x36 toploader protects: posters, prints, magazines, documents.",
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
