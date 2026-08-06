"""Ultra PRO — Current Size Comic UV One-Touch Magnetic Holder  [Listing 56]
NEUES Format: Titel/Bullets/Backend kommen aus dem SEO-Sheet (listing.xlsx),
Q&A + Vergleich aus dem A+ Premium Sheet (aplus.xlsx). Bildregie handgeschrieben,
100% produktspezifisch, im Ultra-PRO-Katalogstil (schwarz/rot/weiss).

Marketplace: amazon.com (US). ASIN B01EK6OXFM.
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

PLAN_NO = "56"
ASIN = "B01EK6OXFM"
EXCEL = HERE / "listing.xlsx"
APLUS = HERE / "aplus.xlsx"


# ===== produktspezifische Bildregie (Ultra-PRO-Katalogstil, EN Overlays) =====

IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="Clean white for slot-1 compliance; the CTR versions add a black lower band with a thin red top-line (Ultra PRO catalog look). Same framing across all 3.",
        purpose="Win the click against flat sleeves and toploaders — show a rigid, display-ready magnetic case.",
        visual=(
            "Mock ALL 3 options. Product exactly as real: a rigid two-piece clear magnetic holder "
            "with a real current-size comic inside, diamond corners and frosted borders visible. "
            "ONE callout each, product dominant.\n\n"
            "OPTION A — MAGNET: holder held upright, top piece just closing. Badge (red): "
            "'ONE-TOUCH MAGNET'.\n"
            "OPTION B — UV SHIELD: holder with a subtle UV shield icon over the comic. Badge "
            "(red): 'UV PROTECTION'.\n"
            "OPTION C — DISPLAY: holder standing on a shelf, sawtooth hanger hinted. Badge: "
            "'DISPLAY OR WALL-MOUNT'.\n\n"
            "Across all 3: white background, red badge ~6% of frame, same lighting."
        ),
        overlay="(one callout per option)",
        overlay_sub="3 hero options shipped — A/B test, keep the winner.",
        props=["A: holder closing, magnet edge", "B: holder + UV shield icon", "C: holder standing, hanger hinted"],
        lighting="Bright, even studio light; crisp catch-light so the clear rigid case reads on white.",
        why_it_works=(
            "Three triggers: one-touch magnet, UV protection, display-ready. One callout each — "
            "readable at thumbnail size and clearly a premium case, not a bag."
        ),
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: One-touch magnetic closure",
        role="hook",
        background="Black with a thin red top-line and a bold white headline (Ultra PRO catalog)",
        purpose="Own the standout feature: slide the comic in, the magnet snaps it shut.",
        visual=(
            "Large macro: a current-size comic sliding into the two-piece holder along the slide-in "
            "hinge, the magnetic edge snapping closed. Thin red callout lines: 'two-piece holder', "
            "'slide-in hinge', 'magnetic closure'. White bold headline top: 'SNAP. SECURE. DONE.'"
        ),
        overlay="ONE-TOUCH MAGNETIC CLOSE.",
        overlay_sub="Two-piece holder with slide-in hinge and magnetic closure for easy, secure access.",
        props=["comic sliding into holder (macro)", "magnetic edge closing", "red callout lines"],
        lighting="Dramatic catalog light on black; strong edge-light on the clear rigid case.",
        why_it_works=(
            "The magnetic one-touch action is the single feature no flat sleeve offers. A macro of "
            "the snap-close proves it is effortless yet secure."
        ),
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: UV protection keeps colours true",
        role="educate",
        background="White with a black/red Ultra PRO footer band",
        purpose="Defend value: why UV-blocking matters for displayed comics that face light.",
        visual=(
            "Split card. LEFT: the holder with a comic, a small sun icon 'UV-BLOCKING'. RIGHT: "
            "three stacked feature rows with red check-icons — 'UV-blocking additives', 'Guards "
            "cover colours from fading', 'Ultra-clear viewing surface'. Footer band: 'Time-tested "
            "comic protection — trusted since 1952.'"
        ),
        overlay="UV PROTECTION BUILT IN.",
        overlay_sub="UV-blocking additives help guard cover colours while on display.",
        props=["holder + comic", "3 feature rows with red checks", "since-1952 footer band"],
        lighting="Flat, even catalog light; feature icons legible at thumbnail size.",
        why_it_works=(
            "Displayed comics fade under light. Naming UV-blocking additives with a clear 'why it "
            "matters' separates this from plain clear cases."
        ),
    ),
    AIImagePlanItem(
        name="Image 4 — Desire: premium display details",
        role="desire",
        background="White with a red detail callout (Ultra PRO)",
        purpose="Sell the premium look — diamond corners, frosted borders, ultra-clear front.",
        visual=(
            "Close crop on the holder's corners and edges: red callouts to 'diamond corners', "
            "'frosted borders', 'ultra-clear viewing surface'. A short note: 'Hard plastic "
            "construction — a display piece, not just storage.'"
        ),
        overlay="DIAMOND CORNERS. CLEAR VIEW.",
        overlay_sub="Hard plastic case with diamond corners, frosted borders and ultra-clear front.",
        props=["corner + edge close crop", "diamond-corner callout", "frosted-border callout"],
        lighting="Bright, even; the detail callouts must read clearly.",
        why_it_works=(
            "The finish details justify the premium over a bag or toploader — collectors pay for a "
            "case that looks as good as the book inside."
        ),
    ),
    AIImagePlanItem(
        name="Image 5 — Desire: display it or mount it",
        role="desire",
        background="Black with red accents (Ultra PRO catalog)",
        purpose="Show the two display modes — shelf stand and wall mount.",
        visual=(
            "The holder shown two ways: standing on a shelf, and wall-mounted via the sawtooth "
            "hanger. Icon-stats: 'SHELF STAND', 'WALL MOUNT', 'SAWTOOTH HANGER', 'CURRENT-SIZE "
            "FIT'. Clean, catalog-style layout."
        ),
        overlay="DISPLAY OR WALL-MOUNT.",
        overlay_sub="Sawtooth hanger plus stand — display current-size comics on shelf or wall.",
        props=["holder standing on shelf", "holder wall-mounted", "sawtooth hanger detail", "4 icon-stats"],
        lighting="Catalog light on black; both display modes clearly separated.",
        why_it_works=(
            "Two use-cases in one image widens the appeal — desk display or a wall gallery of key "
            "issues, both ready out of the box."
        ),
    ),
    AIImagePlanItem(
        name="Image 6 — Trust: Ultra PRO, trusted since 1952",
        role="trust",
        background="Black with red top-line, white headline (brand close)",
        purpose="Close on brand authority — the collector's default choice.",
        visual=(
            "Hero of the holder with a small lifestyle inset (a collector mounting a comic on a "
            "tidy wall display). Brand line bottom: 'ULTRA PRO — protecting collections since 1952 "
            "· trusted by collectors worldwide'. Red badge: 'SINCE 1952'."
        ),
        overlay="TRUSTED SINCE 1952.",
        overlay_sub="Ultra PRO — protecting and displaying comic collections worldwide.",
        props=["holder hero", "collector wall-display inset", "since-1952 red badge"],
        lighting="Premium catalog light on black; warm inset for the lifestyle moment.",
        why_it_works=(
            "Against unbranded cases, heritage and trust are the deciding signals. 'Since 1952' is "
            "Ultra PRO's honest, compliant authority claim."
        ),
    ),
    AIImagePlanItem(
        name="Image 7 — Range: the Ultra PRO comic display system",
        role="close",
        background="White with black/red Ultra PRO chrome",
        purpose="Cross-sell the wider comic-protection and display range.",
        visual=(
            "Clean line-up: the UV magnetic holder (this product) alongside comic bags, boards and "
            "a comic storage box — shown as a coordinated protect-and-display system. Small labels; "
            "the magnetic holder gently highlighted. Caption: 'Protect it. Display it. — the Ultra "
            "PRO way.'"
        ),
        overlay="PROTECT IT. DISPLAY IT.",
        overlay_sub="Pair the UV magnetic holder with Ultra PRO bags, boards and storage boxes.",
        props=["UV magnetic holder (highlighted)", "comic bags", "boards", "comic storage box"],
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
        headline="PROTECT IT. DISPLAY IT. SINCE 1952.",
        body=(
            "The Ultra PRO Current Size Comic UV One-Touch Magnetic Holder pairs a rigid, "
            "ultra-clear hard-plastic case with UV-blocking protection and a one-touch magnetic "
            "closure. Slide your comic in, snap it shut, and stand it or wall-mount it &mdash; "
            "premium comic display trusted by collectors since 1952."
        ),
        visual="Wide black banner, red top-line, bold white headline left; the magnetic holder with a comic and diamond corners right. Ultra PRO logo upper-left.",
        alt="Ultra PRO UV one-touch magnetic comic holder banner: UV protection, magnetic close, display, since 1952.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): Why this holder",
        role="a+_carousel",
        headline="WHY ULTRA PRO MAGNETIC HOLDER",
        body=(
            "Tile 1: <b>ONE-TOUCH MAGNET</b> &mdash; Slide-in hinge and magnetic closure.<br/>"
            "Tile 2: <b>UV PROTECTION</b> &mdash; UV-blocking additives guard cover colours.<br/>"
            "Tile 3: <b>ULTRA-CLEAR HARD PLASTIC</b> &mdash; Diamond corners, frosted borders.<br/>"
            "Tile 4: <b>DISPLAY OR WALL-MOUNT</b> &mdash; Sawtooth hanger plus stand.<br/>"
            "Tile 5: <b>SINCE 1952</b> &mdash; Trusted comic protection worldwide."
        ),
        visual="5 square tiles, red accent corner each, black/white icons (magnet · sun/UV · case · hanger · badge).",
        alt="Five A+ tiles: one-touch magnet, UV protection, hard plastic, display/wall-mount, since 1952.",
    ),
    AIModule(
        name="Module 3 — Banner: UV protection & premium finish",
        role="a+_banner",
        headline="UV PROTECTION. PREMIUM FINISH.",
        body=(
            "Built with hard plastic and UV-blocking additives, this holder helps shield cover "
            "colours from fading while keeping an ultra-clear view. Diamond corners and frosted "
            "borders finish a case made to be seen &mdash; on the shelf or on the wall."
        ),
        visual="Banner split: macro of the ultra-clear front + UV sun and diamond-corner icons left; the holder wall-mounted right. Black/red Ultra PRO styling.",
        alt="A+ banner on UV protection and premium hard-plastic finish of the magnetic comic holder.",
    ),
    AIModule(
        name="Module 4 — Carousel (4 tiles): The comic display system",
        role="a+_carousel",
        headline="PROTECT IT. DISPLAY IT.",
        body=(
            "Tile 1: <b>UV MAGNETIC HOLDER</b> &mdash; Rigid current-size display case (this product).<br/>"
            "Tile 2: <b>COMIC BAGS</b> &mdash; Ultra-clear sleeves for everyday storage.<br/>"
            "Tile 3: <b>BACKING BOARDS</b> &mdash; Keep comics flat and supported.<br/>"
            "Tile 4: <b>STORAGE BOXES</b> &mdash; Organise and archive full runs."
        ),
        visual="4 coordinated product tiles, red accent corners, consistent catalog styling.",
        alt="Four A+ tiles showing the Ultra PRO comic system: UV magnetic holder, bags, boards, boxes.",
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
