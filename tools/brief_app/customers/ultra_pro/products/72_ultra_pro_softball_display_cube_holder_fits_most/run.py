"""Ultra PRO — Softball Display Cube Holder (fits most vinyl figures)  [Listing 72]
NEUES Format: Titel/Bullets/Backend kommen aus dem SEO-Sheet (listing.xlsx),
Q&A + Vergleich aus dem A+ Premium Sheet (aplus.xlsx). Bildregie handgeschrieben,
100% produktspezifisch, im Ultra-PRO-Katalogstil (schwarz/rot/weiss).

Klarer Display-Würfel: passt für regulation-size Softbälle UND die meisten
Vinyl-Figuren (z. B. Funko Pop!), Base-Ring, 3mm non-PVC, stapelbar, Finger-Notch-Deckel.
Funko Pop nur als Kompatibilität nennen — keine Funko-Markeninszenierung.

Marketplace: amazon.com (US). ASIN B06XGRZVHF.
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

PLAN_NO = "72"
ASIN = "B06XGRZVHF"
EXCEL = HERE / "listing.xlsx"
APLUS = HERE / "aplus.xlsx"


# ===== produktspezifische Bildregie (Ultra-PRO-Katalogstil, EN Overlays) =====

IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="Clean white for slot-1 compliance; the CTR versions add a black lower band with a thin red top-line (Ultra PRO catalog look). Same framing across all 3.",
        purpose="Win the click in a grid of look-alike display cubes and ball stands. Ship all 3, keep the winner.",
        visual=(
            "Mock ALL 3 options. Product exactly as real: a clear stackable display cube with a "
            "generic vinyl figure inside on the base ring, ultra-clear walls, finger-notch lid. ONE "
            "callout each, product dominant.\n\n"
            "OPTION A — DUAL USE: cube shown twice side by side — one holding a regulation softball, "
            "one holding a plain vinyl figure. Badge (red): 'SOFTBALL & FIGURES'.\n"
            "OPTION B — CLEAR VIEW: single cube, collectible crisp through the ultra-clear walls. "
            "Badge (red): 'CLEAR ALL-ROUND VIEW'.\n"
            "OPTION C — STACKABLE: two cubes stacked on a shelf. Badge: 'STACKABLE DISPLAY'.\n\n"
            "Across all 3: white background, red badge ~6% of frame, same lighting. Any figure is "
            "a plain non-branded vinyl figure — no Funko branding or trade dress."
        ),
        overlay="(one callout per option)",
        overlay_sub="3 hero options shipped — A/B test, keep the winner.",
        props=["A: cube with softball + cube with vinyl figure", "B: cube with collectible, clear walls", "C: two cubes stacked"],
        lighting="Bright, even studio light; crisp catch-light so the ultra-clear walls read on white.",
        why_it_works=(
            "Three triggers: dual use (softball or figure), clear all-round view, stackable "
            "display. One callout each — readable at thumbnail size."
        ),
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: clear all-round view",
        role="hook",
        background="Black with a thin red top-line and a bold white headline (Ultra PRO catalog)",
        purpose="Own the #1 reason collectors buy a display cube: see the piece from every angle.",
        visual=(
            "Large hero: the clear cube with a regulation softball inside, viewed at a three-quarter "
            "angle so all six clear walls read. Thin red callout lines: 'ultra-clear non-PVC', "
            "'view from every side', 'finger-notch lid'. White bold headline top: 'SEE EVERY SIDE.'"
        ),
        overlay="CLEAR VIEW FROM EVERY SIDE",
        overlay_sub="Ultra-clear non-PVC walls keep your softball or figure fully visible.",
        props=["cube with softball (three-quarter angle)", "red callout lines", "finger-notch lid detail"],
        lighting="Dramatic catalog light on black; strong edge-light on the clear walls.",
        why_it_works=(
            "Collectors buy a cube to display AND protect. A crisp all-round view proves the walls "
            "are genuinely clear — the strongest visual argument in the display-case category."
        ),
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: one cube, two uses",
        role="educate",
        background="White with a black/red Ultra PRO footer band",
        purpose="Show the dual use — a regulation softball OR most vinyl figures and small items.",
        visual=(
            "Split card. LEFT: the cube holding a regulation softball seated on the base ring, label "
            "'REGULATION SOFTBALL'. RIGHT: the same cube holding a plain vinyl figure, label 'FITS "
            "MOST VINYL FIGURES'. Below, a small icon row with red checks — 'figurines', 'toys', "
            "'tokens & dice', 'small collectibles'. Footer band: 'One clear cube, many collections "
            "— trusted since 1952.' Vinyl figure is generic, no Funko branding."
        ),
        overlay="SOFTBALL & VINYL FIGURES",
        overlay_sub="One cube for a regulation softball or most vinyl figures and small collectibles.",
        props=["cube with softball", "cube with plain vinyl figure", "icon row of small collectibles"],
        lighting="Flat, even catalog light; both use-cases legible at thumbnail size.",
        why_it_works=(
            "Dual use doubles the addressable buyer — sports collectors AND figure collectors see "
            "themselves in one image, widening the click base without a superlative claim."
        ),
    ),
    AIImagePlanItem(
        name="Image 4 — Fit: base ring & exact dimensions",
        role="desire",
        background="White with a red dimension callout (Ultra PRO)",
        purpose="Remove the #1 buyer question — will my ball or figure fit and stay put?",
        visual=(
            "The cube centred with a softball seated on the base ring, plus a clean dimension "
            "callout: 'Interior 4-1/8\" x 4-1/8\" x 4-1/4\" — Exterior 4-1/2\" x 4-1/2\" x 4-9/16\"'. "
            "Small arrow highlighting the base ring: 'holds round items securely'. Short note: "
            "'Seats a regulation softball, no roll.'"
        ),
        overlay="BASE RING HOLDS IT STEADY",
        overlay_sub="Base ring seats round items; interior 4-1/8\" x 4-1/8\" x 4-1/4\".",
        props=["cube with softball on base ring", "dimension callout", "base-ring arrow"],
        lighting="Bright, even; the dimension callout must read clearly.",
        why_it_works=(
            "Wrong-size or loose-fit is the top return reason for display cubes. A precise dimension "
            "callout plus the base ring sets honest expectations and prevents mis-buys."
        ),
    ),
    AIImagePlanItem(
        name="Image 5 — Build: 3mm non-PVC walls & finger-notch lid",
        role="desire",
        background="Black with red accents (Ultra PRO catalog)",
        purpose="Defend the build quality — durable, non-PVC, and an easy-access finger-notch lid.",
        visual=(
            "Macro of a cube corner showing wall thickness, with icon-stats: '3MM DURABLE WALLS', "
            "'NON-PVC PLASTIC', 'CLEAR ALL-ROUND VIEW', 'FINGER-NOTCH LID'. A small callout: 'Guards "
            "against dust and fading on the shelf.' Clean, catalog-style layout."
        ),
        overlay="CLEAR, NON-PVC BUILD.",
        overlay_sub="3mm non-PVC walls and a finger-notch lid keep pieces clean and easy to reach.",
        props=["cube corner macro (wall thickness)", "4 icon-stats", "dust/fading callout"],
        lighting="Catalog light on black; product and stats clearly separated.",
        why_it_works=(
            "Serious collectors filter on build and protection. Naming 3mm non-PVC walls and the base ring "
            "protection separates this from thin, unlabeled bargain cubes."
        ),
    ),
    AIImagePlanItem(
        name="Image 6 — Trust: Ultra PRO, trusted since 1952",
        role="trust",
        background="Black with red top-line, white headline (brand close)",
        purpose="Close on brand authority — the collector's default choice for display and storage.",
        visual=(
            "Hero of the cube with a small lifestyle inset (a collector arranging cubes on a tidy "
            "display shelf). Brand line bottom: 'ULTRA PRO — display and storage solutions since "
            "1952 · trusted by collectors worldwide'. Red badge: 'SINCE 1952'."
        ),
        overlay="TRUSTED SINCE 1952.",
        overlay_sub="Ultra PRO — display and storage solutions for collectors worldwide.",
        props=["cube hero", "collector display-shelf inset", "since-1952 red badge"],
        lighting="Premium catalog light on black; warm inset for the lifestyle moment.",
        why_it_works=(
            "Against unbranded bargain cubes, heritage and trust are the deciding signals. 'Since "
            "1952' is Ultra PRO's honest, compliant authority claim."
        ),
    ),
    AIImagePlanItem(
        name="Image 7 — Display: stack it, and the Ultra PRO range",
        role="close",
        background="White with black/red Ultra PRO chrome",
        purpose="Show the stackable display in action and cross-sell the wider Ultra PRO range.",
        visual=(
            "Clean line-up: several display cubes stacked into a tidy grid — some with softballs, "
            "some with figures — alongside a One-Touch holder and a storage box, shown as a "
            "coordinated display-and-storage system. Small labels; the display cubes gently "
            "highlighted. Caption: 'Stack it. Display it. Store it. — the Ultra PRO way.'"
        ),
        overlay="STACK IT. DISPLAY IT.",
        overlay_sub="Stackable cubes plus the wider Ultra PRO display and storage range.",
        props=["stacked display cubes (highlighted)", "One-Touch holder", "storage box"],
        lighting="Bright, even; coordinated family shot.",
        why_it_works=(
            "Turns one purchase into a system sale and reinforces Ultra PRO as the one-stop "
            "collector brand for display and storage."
        ),
    ),
]


# ===== 4 kreative Module + Q&A/Vergleich aus dem A+ Sheet =====

CREATIVE_MODULES = [
    AIModule(
        name="Module 1 — Brand banner",
        role="a+_banner",
        headline="SHOW IT OFF. CLEAR SINCE 1952.",
        body=(
            "An ultra-clear non-PVC display cube built for a regulation softball or most vinyl "
            "figures. Durable 3mm walls, a base ring that holds round items steady, non-PVC clarity "
            "and a stackable design with a finger-notch lid — display and storage trusted by "
            "collectors since 1952."
        ),
        visual="Wide black banner, red top-line, bold white headline left; a clear cube holding a softball with crisp all-round view right. Ultra PRO logo upper-left.",
        alt="Ultra PRO softball display cube banner: clear non-PVC, base ring, non-PVC clarity, since 1952.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): Why this display cube",
        role="a+_carousel",
        headline="WHY THE ULTRA PRO DISPLAY CUBE",
        body=(
            "Tile 1: <b>CLEAR ALL-ROUND VIEW</b> — Ultra-clear non-PVC walls, see every side.<br/>"
            "Tile 2: <b>SOFTBALL &amp; VINYL FIGURES</b> — One cube fits both, plus small items.<br/>"
            "Tile 3: <b>SECURE BASE RING</b> — Seats a regulation softball with no roll.<br/>"
            "Tile 4: <b>3MM NON-PVC WALLS</b> — Durable, crystal-clear build.<br/>"
            "Tile 5: <b>STACKABLE, SINCE 1952</b> — Finger-notch lid, trusted display and storage."
        ),
        visual="5 square tiles, red accent corner each, black/white icons (cube · softball+figure · ring · shield · stack).",
        alt="Five A+ tiles: clear view, softball and figures, base ring, 3mm walls, stackable since 1952.",
    ),
    AIModule(
        name="Module 3 — Banner: One cube, two uses",
        role="a+_banner",
        headline="FITS A SOFTBALL — OR YOUR FIGURES.",
        body=(
            "Interior 4-1/8\" x 4-1/8\" x 4-1/4\" and exterior 4-1/2\" x 4-1/2\" x 4-9/16\", with a "
            "base ring for round items. The clear cube holds a regulation softball or most vinyl "
            "figures &amp; small collectibles — figurines, toys, tokens and dice — on the shelf or "
            "the desk."
        ),
        visual="Banner split: cube with a softball on the base ring left; the same cube with a plain vinyl figure right. Black/red Ultra PRO styling.",
        alt="A+ banner showing the display cube holding a regulation softball or a vinyl figure.",
    ),
    AIModule(
        name="Module 4 — Carousel (4 tiles): The display & storage system",
        role="a+_carousel",
        headline="STACK IT. DISPLAY IT. STORE IT.",
        body=(
            "Tile 1: <b>DISPLAY CUBES</b> — Clear stackable cubes for balls and figures (this product).<br/>"
            "Tile 2: <b>ONE-TOUCH HOLDERS</b> — Magnetic rigid cases for graded and standard cards.<br/>"
            "Tile 3: <b>TOPLOADERS</b> — Rigid protection for cards, photos and posters.<br/>"
            "Tile 4: <b>STORAGE BOXES</b> — Organise and archive the wider collection."
        ),
        visual="4 coordinated product tiles, red accent corners, consistent catalog styling.",
        alt="Four A+ tiles showing the Ultra PRO display and storage system: cubes, holders, toploaders, boxes.",
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
