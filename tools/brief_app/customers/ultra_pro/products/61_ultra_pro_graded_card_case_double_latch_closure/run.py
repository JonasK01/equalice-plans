"""Ultra PRO — Graded Card Case, Double Latch Closure  [Listing 61]
NEUES Format: Titel/Bullets/Backend kommen aus dem SEO-Sheet (listing.xlsx),
Q&A + Vergleich aus dem A+ Premium Sheet (aplus.xlsx). Bildregie handgeschrieben,
100% produktspezifisch, im Ultra-PRO-Katalogstil (schwarz/rot/weiss).

Produkt: extra-dicke ABS-Hartschalen-Transportbox für 100+ GEGRADETE Slabs
(PSA/BGS/CGC), IP67 wasser-/staubdicht, zwei Doppel-Latch-Verschlüsse, zwei
Schloss-Positionen, trackbare Seriennummer, Slot für Tracker, Griff + Schultergurt.

Marketplace: amazon.com (US). ASIN B0CVPF5QVW.
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

PLAN_NO = "61"
ASIN = "B0CVPF5QVW"
EXCEL = HERE / "listing.xlsx"
APLUS = HERE / "aplus.xlsx"


# ===== produktspezifische Bildregie (Ultra-PRO-Katalogstil, EN Overlays) =====

IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="Clean white for slot-1 compliance; the CTR versions add a black lower band with a thin red top-line (Ultra PRO catalog look). Same framing across all 3.",
        purpose="Win the click against generic slab boxes. Show a real hard-shell case full of graded slabs. Ship all 3, keep the winner.",
        visual=(
            "Mock ALL 3 options. Product exactly as real: the extra-thick ABS hard-shell case, "
            "lid open, rows of GENERIC (non-branded) graded slabs (PSA/BGS/CGC-style) standing "
            "inside. ONE callout each, product dominant.\n\n"
            "OPTION A — CAPACITY: case open, packed rows of graded slabs. Badge (red): 'HOLDS 100+ SLABS'.\n"
            "OPTION B — SECURITY: closed case, close-up of the two double latches + lock point. Badge (red): 'DOUBLE-LATCH LOCK'.\n"
            "OPTION C — TRAVEL: case with shoulder strap + handle, small water-drop / dust icons. Badge: 'IP67 · TRAVEL-READY'.\n\n"
            "Across all 3: white background, red badge ~6% of frame, same lighting."
        ),
        overlay="(one callout per option)",
        overlay_sub="3 hero options shipped — A/B test, keep the winner.",
        props=["A: open case packed with graded slabs", "B: closed case, double latches + lock", "C: case with strap + handle, water/dust icons"],
        lighting="Bright, even studio light; crisp catch-light so the ABS shell and slab edges read on white.",
        why_it_works=(
            "Three triggers: capacity (100+), security (locking latches), travel (IP67). One "
            "callout each — readable at thumbnail size."
        ),
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: extra-thick ABS hard shell",
        role="hook",
        background="Black with a thin red top-line and a bold white headline (Ultra PRO catalog)",
        purpose="Own the #1 reason collectors buy a case: rugged protection for expensive graded cards.",
        visual=(
            "Large hero of the closed case with a cutaway edge showing the extra-thick ABS wall "
            "thickness. Thin red callout lines: 'Extra-thick ABS shell', 'Rigid, impact-resistant', "
            "'Protects graded slabs in transit'. White bold headline top: 'BUILT TO PROTECT.'"
        ),
        overlay="EXTRA-THICK ABS SHELL.",
        overlay_sub="Rigid, impact-resistant hard shell guards graded slabs in storage and transit.",
        props=["closed case hero", "ABS wall-thickness cutaway", "red callout lines"],
        lighting="Dramatic catalog light on black; strong edge-light on the shell surface.",
        why_it_works=(
            "For four-figure graded cards, shell strength is the deciding feature. A wall-thickness "
            "cutaway proves the ABS is genuinely heavy-duty — the strongest visual argument here."
        ),
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: IP67 waterproof & dustproof",
        role="educate",
        background="White with a black/red Ultra PRO footer band",
        purpose="Defend quality: why an IP67 sealed case matters for long-term graded-card storage.",
        visual=(
            "Split card. LEFT: the closed case with a small shield icon 'IP67 SEALED'. RIGHT: three "
            "stacked feature rows with red check-icons — 'IP67 waterproof rating', 'Dustproof sealed "
            "gasket', 'Keeps humidity, dust & spills off your slabs'. Footer band: 'Reliable "
            "collectible storage — trusted since 1952.'"
        ),
        overlay="IP67 WATER & DUSTPROOF.",
        overlay_sub="IP67 sealed gasket keeps water, humidity and dust away from your graded slabs.",
        props=["closed case + IP67 shield", "3 feature rows with red checks", "since-1952 footer band"],
        lighting="Flat, even catalog light; feature icons legible at thumbnail size.",
        why_it_works=(
            "Water, humidity and dust ruin graded labels and cases. Naming the IP67 rating with a "
            "clear 'why it matters' separates this from unsealed bargain boxes."
        ),
    ),
    AIImagePlanItem(
        name="Image 4 — Capacity: holds 100+ graded slabs",
        role="desire",
        background="White with a red capacity callout (Ultra PRO)",
        purpose="Remove the #1 buyer question — how many of my slabs will it hold?",
        visual=(
            "Case open from above, graded slabs standing in tidy rows filling the interior with a "
            "clean callout: 'Holds 100+ graded slabs — PSA, BGS & CGC'. Small note: '14.6\" x 14\" x "
            "7\" — one case instead of many loose boxes.'"
        ),
        overlay="HOLDS 100+ GRADED SLABS.",
        overlay_sub="Fits 100+ PSA, BGS and CGC slabs in one 14.6\" x 14\" x 7\" case.",
        props=["top-down open case full of slabs", "capacity callout", "dimension note"],
        lighting="Bright, even; the capacity callout must read clearly.",
        why_it_works=(
            "Capacity is the top comparison point for slab cases. A precise, honest 100+ figure with "
            "real dimensions sets expectations and prevents mis-buys."
        ),
    ),
    AIImagePlanItem(
        name="Image 5 — Security: double latch, locks & serial",
        role="desire",
        background="Black with red accents (Ultra PRO catalog)",
        purpose="Make the theft-deterrent and tracking features obvious for high-value collections.",
        visual=(
            "The closed case with callout close-ups: the two double latches, two built-in lock "
            "locations (small padlock icon), the trackable serial-number plate, and the interior "
            "tracker slot (1.6\" x 1.6\" x 0.4\"). Icon-stats: 'Double latches', 'Two lock points', "
            "'Trackable serial No.', 'Tracker slot'."
        ),
        overlay="DOUBLE-LATCH. LOCKABLE.",
        overlay_sub="Two double latches, two lock points, trackable serial number and a tracker slot.",
        props=["double latches", "two lock locations", "serial-number plate", "interior tracker slot"],
        lighting="Catalog light on black; callout close-ups clearly separated.",
        why_it_works=(
            "Buyers of graded-card cases are protecting real money. Visible locks, a serial number "
            "and a tracker slot signal serious, theft-aware security."
        ),
    ),
    AIImagePlanItem(
        name="Image 6 — Trust: Ultra PRO, trusted since 1952",
        role="trust",
        background="Black with red top-line, white headline (brand close)",
        purpose="Close on brand authority — the collector's default choice.",
        visual=(
            "Hero of the case with a small lifestyle inset (a collector carrying it by the shoulder "
            "strap into a card show). Brand line bottom: 'ULTRA PRO — protecting collections since "
            "1952 · trusted by collectors worldwide'. Red badge: 'SINCE 1952'."
        ),
        overlay="TRUSTED SINCE 1952.",
        overlay_sub="Ultra PRO — protecting graded-card collections worldwide.",
        props=["case hero", "collector-at-show lifestyle inset", "since-1952 red badge"],
        lighting="Premium catalog light on black; warm inset for the lifestyle moment.",
        why_it_works=(
            "Against unbranded generic slab boxes, heritage and trust are the deciding signals. "
            "'Since 1952' is Ultra PRO's honest, compliant authority claim."
        ),
    ),
    AIImagePlanItem(
        name="Image 7 — Range: the Ultra PRO graded-card system",
        role="close",
        background="White with black/red Ultra PRO chrome",
        purpose="Cross-sell the wider graded-card protection range.",
        visual=(
            "Clean line-up: the graded card case (this product) alongside One Touch magnetic "
            "holders, toploaders and 9-pocket portfolios — shown as a coordinated system. Small "
            "labels; the case gently highlighted. Caption: 'Grade it. Case it. Carry it. — the "
            "Ultra PRO way.'"
        ),
        overlay="CASE IT. CARRY IT.",
        overlay_sub="Pair the case with Ultra PRO One Touch holders, toploaders and portfolios.",
        props=["graded card case (highlighted)", "One Touch magnetic holders", "toploaders", "9-pocket portfolio"],
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
        headline="CARRY IT. SECURE IT. SINCE 1952.",
        body=(
            "An extra-thick ABS hard-shell case that holds 100+ graded slabs and travels with an "
            "IP67 waterproof, dustproof rating. Two double latches, two lock locations, a trackable "
            "serial number and a handle plus shoulder strap &mdash; graded-card protection trusted "
            "by collectors since 1952."
        ),
        visual="Wide black banner, red top-line, bold white headline left; the open case full of graded slabs right. Ultra PRO logo upper-left.",
        alt="Ultra PRO graded card case banner: ABS hard shell, holds 100+ slabs, IP67, double latch, since 1952.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): Why this case",
        role="a+_carousel",
        headline="WHY ULTRA PRO GRADED CARD CASE",
        body=(
            "Tile 1: <b>EXTRA-THICK ABS SHELL</b> — Rigid, impact-resistant protection.<br/>"
            "Tile 2: <b>HOLDS 100+ SLABS</b> — Fits PSA, BGS &amp; CGC graded cards.<br/>"
            "Tile 3: <b>IP67 WATER &amp; DUSTPROOF</b> — Sealed against spills and dust.<br/>"
            "Tile 4: <b>DOUBLE-LATCH SECURITY</b> — Two lock points &amp; trackable serial No.<br/>"
            "Tile 5: <b>SINCE 1952</b> — Trusted collectible protection worldwide."
        ),
        visual="5 square tiles, red accent corner each, black/white icons (shell · slab stack · water-drop · padlock · badge).",
        alt="Five A+ tiles: ABS shell, holds 100+ slabs, IP67, double-latch security, since 1952.",
    ),
    AIModule(
        name="Module 3 — Banner: Travel-ready security",
        role="a+_banner",
        headline="TRAVEL-READY. LOCKED DOWN.",
        body=(
            "Take your collection to shows and meetups with confidence. The IP67 sealed shell shrugs "
            "off dust and moisture, while two double latches, two lock locations and a trackable "
            "serial number keep 100+ graded slabs secure &mdash; carried by the handle or shoulder "
            "strap."
        ),
        visual="Banner split: closed case with padlock + double-latch close-ups left; a collector carrying it by the strap right. Black/red Ultra PRO styling.",
        alt="A+ banner on travel-ready, lockable graded card case security.",
    ),
    AIModule(
        name="Module 4 — Carousel (4 tiles): The graded-card system",
        role="a+_carousel",
        headline="GRADE IT. CASE IT. CARRY IT.",
        body=(
            "Tile 1: <b>GRADED CARD CASE</b> — Hard-shell transport for 100+ slabs (this product).<br/>"
            "Tile 2: <b>ONE TOUCH HOLDERS</b> — Magnetic protection for single key cards.<br/>"
            "Tile 3: <b>TOPLOADERS</b> — Rigid protection for raw cards before grading.<br/>"
            "Tile 4: <b>9-POCKET PORTFOLIOS</b> — Organise and display your set."
        ),
        visual="4 coordinated product tiles, red accent corners, consistent catalog styling.",
        alt="Four A+ tiles showing the Ultra PRO graded-card system: case, One Touch holders, toploaders, portfolios.",
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
