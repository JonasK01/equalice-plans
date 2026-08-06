"""RH Filters COMPLETE D13 OIL CHANGE KIT — Amazon image plan (image-led brief).
Hand-written, KW-led, fitment-verified senior copy injected into the branded ReportLab pipeline.

Brand: RH Filters by Royal Holding USA (aftermarket heavy-duty truck filtration).
Marketplace: amazon.com (US). Overlay language: ENGLISH.

Product: COMPLETE D13 OIL CHANGE KIT — a 4-filter service set, AFTERMARKET REPLACEMENT:
  • 2 × LF667  — full-flow spin-on oil filter (1 1/8-16 thread)
  • 1 × LF3654 — bypass spin-on oil filter (1 3/8-16 thread)
  • 1 × FF5507 — spin-on secondary fuel filter (M32 x 1.5 thread)
For Volvo D13 heavy-duty diesel service — always confirm by engine + OEM part number.
Listing cross-references OE# 20972293 · 21707133 · 21707132.
(See SOURCE_NOTES.md for the full verified fact set.)

LANGUAGE SPLIT (the standard):
  • ENGLISH (designer-facing) — art direction the designer reads:
    image purpose, background, visual, props, lighting, why_it_works, ctr, cvr, module visual.
  • ENGLISH (customer-facing, amazon.com) — text the shopper reads:
    TITLE, BULLETS, overlay, overlay_sub, module headline+body, QA, BACKEND.

OVERLAY RULE: sell the OUTCOME, not the action. Every on-image overlay leads with the result a
fleet/mechanic wants — one complete D13 service in one box, the RIGHT four filters, no missing
parts, no second trip to the parts counter, no wrong-filter surprise.
Hard limits (auto-linted on build):
  overlay ≤ 30 chars AND ≤ 5 words · overlay_sub ≤ 90 chars
  module headline ≤ 38 chars · bullet head <b>…</b> ≤ 45 chars · TITLE ≤ 200 real chars
  (no "·" middots in overlays — the linter counts them as words.)

ELEVATED COPY — 4 levers applied:
  1) VOICE-OF-CUSTOMER: praise = correct fit and function, filters work as expected, good quality,
     excellent price/value. The category's WORST reviews are "WRONG fuel filter supplied /
     compatibility mismatch / incorrect filter included." RH is the ANTIDOTE: a COMPLETE,
     correctly-matched D13 kit — the right 4 filters, every time, cross-referenced and verified.
  2) DREAM-OUTCOME-FIRST: hero + bullet 1 lead with the result — one box, a complete D13 oil-and-fuel
     service, the RIGHT filters, no missing parts, no second trip to the parts counter.
  3) POWER-WORDS + specificity: complete kit, full-flow + bypass + fuel, matched-and-verified,
     one-box service, no guesswork. Name the 4 filters (2× LF667, LF3654, FF5507).
  4) KEYWORD-WEAVING: oil change kit · oil and filter kit · bypass oil filter kit ·
     diesel bypass oil filter kit · volvo · truck oil.

COMPLIANCE (build auto-checks):
  - Aftermarket only — "aftermarket replacement, cross-references OE# …"; never imply it IS OEM.
  - NO "replaces" before a capitalized/part word (trips the competitor checker) — use "cross-references".
  - NO vague "universal fit" — state Volvo D13 + "confirm by engine / OEM part #".
  - No "best/#1/ultimate/guaranteed", no "$", no URL/".com" in customer copy.
"""
from __future__ import annotations
import sys
from pathlib import Path

# This script lives at customers/<brand>/products/<product>/run.py — self-contained.
HERE = Path(__file__).resolve().parent          # the product folder
ROOT = HERE.parents[5]                           # project root (Claude_Code/)
sys.path.insert(0, str(ROOT))

from tools.brief_app.core.customers import load_customer
from tools.brief_app.core.excel_parser import parse_excel
from tools.brief_app.core.pdf_builder import BriefBuilder
from tools.brief_app.core.ai import AIImagePlanItem, AIModule, AIQA


# Inputs/outputs live alongside this script — the product folder is self-contained.
EXCEL = HERE / "listing.xlsx"
PLAN_NO = "05"
ASIN = "B0CRVSPR1V"      # the parsed asin is a URL — use THIS exact ASIN


# ===== KW-led, fitment-verified, aftermarket-compliant EN copy (customer-facing) =====
# Title is HTML-escaped by the builder, so a literal "&" counts as 1 real char. Keep <= 200.

TITLE = (
    "RH Filters Complete D13 Oil Change Kit — Aftermarket Replacement, Cross-References OE# "
    "20972293 21707133 21707132 — 2 x LF667 Full-Flow + LF3654 Bypass + FF5507 Fuel, Fits Volvo D13"
)

BULLETS = [
    "<b>ONE BOX, ONE COMPLETE D13 SERVICE</b> — Every filter your Volvo D13 oil-and-fuel change "
    "needs in a single matched-and-verified kit: 2 full-flow oil filters, 1 bypass oil filter and "
    "1 fuel filter. The right four filters, no missing parts, no second trip to the parts counter.",

    "<b>THE RIGHT 4 FILTERS, MATCHED</b> — 2 x LF667 full-flow spin-on oil filters, 1 x LF3654 "
    "bypass oil filter and 1 x FF5507 secondary fuel filter — combining full-flow oil, bypass oil "
    "and fuel filtration in one coordinated diesel bypass oil filter kit. No guesswork, no wrong filter.",

    "<b>CROSS-REFERENCES 3 OE NUMBERS</b> — Aftermarket replacement oil and filter kit that "
    "cross-references OE# 20972293, 21707133 and 21707132. Match these against your engine and "
    "current filters to verify fitment. This is not an OEM-branded part.",

    "<b>FITS VOLVO D13 DIESEL SERVICE</b> — Built for Volvo D13 heavy-duty diesel service. All four "
    "are spin-on filters for conventional workshop install. Always confirm fitment by your engine "
    "and OEM part number before ordering — no vague universal-fit guesswork here.",

    "<b>RIGHT FIT, FAIR PRICE, REAL VALUE</b> — RH Filters by Royal Holding USA: heavy-duty truck "
    "oil filtration built for value, not a cut corner. A complete bypass oil filter kit for the price "
    "of guessing part numbers one at a time — correct fit and function, kit after kit.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (pure white, complete-kit read)",
        role="hero",
        background="Pure white #FFFFFF, Amazon main-image compliant. The four filters fill >=85% of frame. NO overlay text, NO graphics, NO badges (policy).",
        purpose="Win the click in a diesel-parts grid by reading instantly as a COMPLETE, multi-filter D13 service kit — not a single lonely filter — with genuine heavy-duty build quality.",
        visual=(
            "All FOUR RH Filters canisters arranged as a confident group on pure white: the two LF667 "
            "full-flow oil filters together, the LF3654 bypass oil filter and the FF5507 fuel filter "
            "beside them, fanned at a slightly elevated 3/4 angle so each printed RH Filters part label "
            "is rotated toward camera and legible (LF667, LF3654, FF5507). The group occupies ~88% of "
            "the frame, tallest filter centered, crisp focus edge to edge so the spin-on threads and "
            "seal gaskets read as real heavy-duty parts, not a stock render. No props, no text — the "
            "completeness of the set IS the hero message. (Overlay intentionally empty per policy.)"
        ),
        overlay="",
        overlay_sub="",
        props=["all 4 kit filters grouped (2x LF667, LF3654, LF3654 bypass, FF5507) at 3/4 angle, labels to camera"],
        lighting="Soft even studio light, 5000K, large top key with twin side fill to kill harsh shadow. Gentle gradient shadow grounding the group. Hard enough catch on the gaskets to show real rubber.",
        why_it_works=(
            "Compliant white-background hero, but the four-filter group framing signals 'complete kit' at "
            "thumbnail size — the single thing this buyer is shopping for — instead of a one-filter shot "
            "that looks like every commodity listing. Showing four real, labeled canisters pre-answers "
            "'is everything in the box and is it quality?' before the click."
        ),
        ctr="A four-filter group reads as a COMPLETE D13 kit in a grid full of single-filter renders — the buyer searching an oil change kit sees their exact answer.",
        cvr="Four sharp, labeled canisters signal an accurate, complete listing — the top positive driver — and pre-empt the 'incorrect filter included / missing part' fear that drives the category's worst reviews.",
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: What's inside the box (kit laid out + labeled)",
        role="hook",
        background="Mood blue #EAF1F8 with a clean technical grid texture — engineering data-sheet feel.",
        purpose="Defuse the wrong-part fear instantly by laying the COMPLETE kit out and labeling exactly what's inside — the four correct filters, named.",
        visual=(
            "Flat-lay / knolling of the open kit on the blue field. The four canisters laid in a row, each "
            "with a clean RH-blue caller line to a label:\n"
            "  • 2 x LF667 — FULL-FLOW OIL\n"
            "  • 1 x LF3654 — BYPASS OIL\n"
            "  • 1 x FF5507 — SECONDARY FUEL\n"
            "A bold top strip: 'EVERYTHING FOR ONE D13 SERVICE — IN ONE BOX.' A thin RH-green callout "
            "reads: 'The right 4 filters, matched and verified.' Small 'AFTERMARKET REPLACEMENT' corner "
            "tag in RH blue so there is zero OEM implication. One callout, one action cue (what's inside), "
            "one hero prop (the laid-out kit)."
        ),
        overlay="THE RIGHT 4 FILTERS",
        overlay_sub="One complete D13 oil-and-fuel service in one box — 2 LF667, LF3654 and FF5507.",
        props=["kit flat-lay (4 canisters in a row)", "labeled caller lines per filter", "one box / what's inside strip", "AFTERMARKET REPLACEMENT corner tag"],
        lighting="Flat even technical light — this is a contents frame, legibility beats mood. Slight rim on the canisters to lift them off the blue field.",
        why_it_works=(
            "The single most decisive image for THIS product. The category's worst reviews are 'wrong / "
            "incorrect filter included.' Laying out all four correct filters by name, with a 'one box' "
            "message, kills the buyer's biggest fear before they ever read a review and frames the kit "
            "as complete and aftermarket."
        ),
        ctr="A labeled 'what's inside' layout of four named filters answers the buyer's exact question — is the whole D13 service here? — and stops the scroll.",
        cvr="Naming each correct filter (2x LF667, LF3654, FF5507) with a 'matched and verified' cue directly defuses the wrong-filter / missing-part fear that drives the category's returns.",
    ),
    AIImagePlanItem(
        name="Image 3 — Hook: Fitment board (Volvo D13 + OE cross-reference)",
        role="hook",
        background="Mood blue #EAF1F8 with a clean technical grid texture — engineering data-sheet feel.",
        purpose="Answer the #1 buyer question: WILL THIS FIT MY D13? Lead with exact application + the OE cross-reference list and a verify cue.",
        visual=(
            "LEFT 45%: the four-filter group at a 3/4 angle, labels to camera. RIGHT 55%: a clean fitment "
            "panel in RH blue.\n"
            "  Top block — bold: 'FITS VOLVO D13 HEAVY-DUTY DIESEL SERVICE'.\n"
            "  Below it a 'CROSS-REFERENCES OE#' list in a monospace technical font:\n"
            "    20972293   21707133   21707132\n"
            "A thin RH-green callout strip reads: 'Confirm by your engine and OEM part number before "
            "ordering.' Small 'AFTERMARKET REPLACEMENT' tag in the corner (RH blue). One callout, one "
            "action cue (verify-before-order), one prop (the kit group)."
        ),
        overlay="FITS VOLVO D13 SERVICE",
        overlay_sub="Aftermarket oil change kit — cross-references OE# 20972293, 21707133 and 21707132.",
        props=["four-filter group (3/4 angle)", "FITS Volvo D13 fitment panel", "OE cross-reference list", "AFTERMARKET REPLACEMENT corner tag"],
        lighting="Flat even technical light — this is a data frame, legibility beats mood. Slight rim on the filters to lift them off the blue field.",
        why_it_works=(
            "Diesel buyers shop by truck/engine and by OE number. Surfacing the exact Volvo D13 application "
            "plus all three verified cross-references, with a 'confirm by engine / OEM part #' cue, kills "
            "the top return driver (unclear fitment / compatibility mismatch) and frames the kit as aftermarket."
        ),
        ctr="An exact 'FITS VOLVO D13' line plus the OE numbers a buyer is actively searching is a direct match that stops the scroll.",
        cvr="Showing the precise application and three cross-reference numbers with a 'confirm before ordering' cue defuses the compatibility-mismatch fear behind the worst reviews and returns.",
    ),
    AIImagePlanItem(
        name="Image 4 — Educate: Three jobs, one kit (full-flow + bypass + fuel)",
        role="educate",
        background="White with a soft RH-blue panel behind the diagram for separation.",
        purpose="Prove the kit does THREE filtration jobs at once and that each named filter has a specific role — defend it against thin single-filter listings.",
        visual=(
            "A clean engineering diagram of the D13 oil-and-fuel circuit, three labeled nodes mapped to "
            "the kit's filters:\n"
            "  • FULL-FLOW OIL — 2 x LF667 (the main oil flow, cleaned)\n"
            "  • BYPASS OIL — 1 x LF3654 (extra-fine bypass polishing)\n"
            "  • SECONDARY FUEL — 1 x FF5507 (clean fuel to the injection)\n"
            "Each node has a short arrow and a thumbnail of that exact canister. Three RH-green spec chips "
            "along the bottom: 'FULL-FLOW + BYPASS OIL' · 'SECONDARY FUEL' · 'ALL SPIN-ON.' Clean "
            "engineering-diagram styling, RH blue + green only."
        ),
        overlay="THREE JOBS, ONE KIT",
        overlay_sub="Full-flow and bypass oil filtration plus secondary fuel — all four filters matched.",
        props=["oil-and-fuel circuit diagram", "3 labeled filter nodes with canister thumbnails", "3 spec chips", "flow arrows"],
        lighting="Clean studio key with a raking light on the canister thumbnails to reveal real part texture.",
        why_it_works=(
            "Buyers reward a kit that visibly covers the whole job and distrust low-information listings. "
            "Mapping each named filter to its role (full-flow, bypass, fuel) proves this is a coordinated "
            "complete service — not four random parts — in the mechanic's own language."
        ),
        ctr="A three-job circuit diagram is a pattern interrupt among plain product shots and signals technical depth to the detail-oriented diesel buyer.",
        cvr="Showing that the kit covers full-flow oil, bypass oil and fuel — each with the right named filter — converts buyers who need the COMPLETE service, not a partial one.",
    ),
    AIImagePlanItem(
        name="Image 5 — Desire: Service bay, kit on the bench",
        role="desire",
        background="Real heavy-duty service-bay / engine-bay context, neutral industrial tones.",
        purpose="Show the kit in its actual home so the buyer can picture a clean, one-pass D13 service with everything on the bench.",
        visual=(
            "Three-quarter shot of the four RH filters laid out on a clean shop bench beside a Volvo D13 "
            "engine, a gloved hand (fingers only, no face) lifting the LF3654 bypass filter toward the "
            "mount, a clean shop rag as the single supporting prop. The two LF667s and the FF5507 wait in "
            "order on the bench. Small RH-blue callout: 'Everything on the bench — spin them on.' One "
            "action cue — the hand reaching for the next filter."
        ),
        overlay="ONE-PASS D13 SERVICE",
        overlay_sub="All four filters on the bench, spin-on ready — no missing part, no second trip.",
        props=["four filters on a shop bench", "Volvo D13 engine context", "gloved hand (fingers only)", "shop rag"],
        lighting="Industrial garage light — cool overhead with a warm practical fill from the side. Honest shop atmosphere, not a sterile studio.",
        why_it_works=(
            "Places the kit in the buyer's reality (bench + engine) and answers 'is the whole job here?' — "
            "echoing the 'correct fit and function / convenient' positive themes and letting the buyer "
            "picture a clean one-pass service instead of a half-done job and a trip back to the counter."
        ),
        ctr="An on-bench service shot reads as 'this is the real D13 job, all in one box' and stands out from white-only competitor galleries.",
        cvr="Seeing all four filters staged for one service reassures buyers burned by missing or wrong parts — the kit is complete and ready.",
    ),
    AIImagePlanItem(
        name="Image 6 — Trust: Kit spec & fitment card",
        role="trust",
        background="White with soft RH-blue spec panels for separation.",
        purpose="Stack the verification a fleet buyer scans for: every filter, its role, thread, and how to confirm fitment — kills wrong-part / return risk.",
        visual=(
            "Centered: the four-filter group, labels to camera. Four spec tiles in the corners, RH-blue headers:\n"
            "  • TOP-LEFT — 2 x LF667: full-flow oil, 1 1/8-16 thread\n"
            "  • TOP-RIGHT — 1 x LF3654: bypass oil, 1 3/8-16 thread\n"
            "  • BOTTOM-LEFT — 1 x FF5507: secondary fuel, M32 x 1.5 thread\n"
            "  • BOTTOM-RIGHT — FITS: Volvo D13 heavy-duty diesel service\n"
            "Across the bottom, one RH-green action strip: 'CONFIRM FITMENT — verify by your engine and "
            "OEM part number, cross-references OE# 20972293 / 21707133 / 21707132.' Small corner tag: "
            "'AFTERMARKET REPLACEMENT.' Clean, technical, fleet-friendly."
        ),
        overlay="EVERY FILTER, SPELLED OUT",
        overlay_sub="2 LF667 full-flow, LF3654 bypass, FF5507 fuel — confirm by engine and OE part number.",
        props=["four-filter group (center)", "4 spec tiles", "green confirm-fitment strip", "AFTERMARKET REPLACEMENT tag"],
        lighting="Even studio light, tiles legible at thumbnail size, crisp catch on the canisters.",
        why_it_works=(
            "Fleets buy on spec certainty. Listing each filter, its thread and role, the exact application "
            "and a confirm-by-engine/OE instruction directly counters the compatibility-mismatch and "
            "'incorrect filter included' complaints that drive this category's returns."
        ),
        ctr="A clean per-filter spec card signals a thorough, accurate listing and rewards the buyer who clicks through for technical detail.",
        cvr="Spelling out every filter, thread and the confirm-by-OE instruction removes the last wrong-part doubt for a fleet maintenance purchase.",
    ),
    AIImagePlanItem(
        name="Image 7 — Close: RH Filters brand + complete-kit value",
        role="close",
        background="Clean RH-blue brand panel with subtle technical grid.",
        purpose="Close on the brand promise, the complete-kit value edge, and a clear service-interval repurchase cue.",
        visual=(
            "Centered: the four RH Filters canisters grouped, labels to camera, with a subtle RH-green accent "
            "sweep behind them and a small 'COMPLETE 4-FILTER KIT' seal badge. Below, the RH Filters brand "
            "mark and tagline 'Top quality. Fair price.' A clean lower strip with a service reminder: 'D13 "
            "OIL-AND-FUEL SERVICE — change all four at your service interval.' Small corner tag repeats "
            "'AFTERMARKET REPLACEMENT — cross-references OE# 20972293 / 21707133 / 21707132.' Calm, "
            "confident, technical."
        ),
        overlay="COMPLETE KIT, FAIR PRICE",
        overlay_sub="The right four D13 filters in one box — change them together at your service interval.",
        props=["four-filter group (center)", "COMPLETE 4-FILTER KIT badge", "RH Filters brand mark + tagline", "service-interval strip", "OE cross-reference tag"],
        lighting="Clean even studio light, confident product-forward key, crisp catch on the canisters.",
        why_it_works=(
            "Reinforces the value tagline and the complete-kit edge (the direct counter to the 'wrong / "
            "missing filter' reviews), gives a concrete repurchase trigger (change all four at the service "
            "interval), and restates the OE cross-reference one last time so the buyer leaves certain of "
            "fit and value."
        ),
        ctr="A confident brand-close with the tagline and a 'complete 4-filter kit' badge builds the trust that turns a browse into a brand-loyal click.",
        cvr="The complete-kit promise plus a change-together reminder and a final cross-reference recap seals fitment confidence and primes repeat fleet orders.",
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Brand banner: One box, one complete D13 service.",
        role="a+_banner",
        headline="ONE BOX. ONE D13 SERVICE.",
        body=(
            "RH Filters by Royal Holding USA builds aftermarket replacement filters for the trucks that keep "
            "working. This complete D13 oil change kit puts the right four filters in one box — 2 x LF667 "
            "full-flow oil filters, 1 x LF3654 bypass oil filter and 1 x FF5507 secondary fuel filter — an "
            "aftermarket replacement that cross-references OE# 20972293, 21707133 and 21707132, built for "
            "Volvo D13 heavy-duty diesel service. The right filters, matched and verified."
        ),
        visual="Wide cinematic shot: Volvo D13 truck in an industrial yard at golden hour (no readable competitor branding), the four RH Filters canisters grouped sharp in the foreground-right on a clean surface. RH blue logo upper-left, green accent rule along the bottom band, tagline 'Top quality. Fair price.'",
        alt="RH Filters complete D13 oil change kit — four filters grouped in the foreground with a heavy-duty truck in an industrial yard behind them.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): Why this D13 kit",
        role="a+_carousel",
        headline="WHY THIS D13 OIL CHANGE KIT",
        body=(
            "Tile 1: <b>COMPLETE 4-FILTER KIT</b> — Everything one D13 oil-and-fuel service needs, in one box.<br/>"
            "Tile 2: <b>THE RIGHT FILTERS</b> — 2 x LF667 full-flow, 1 x LF3654 bypass, 1 x FF5507 fuel.<br/>"
            "Tile 3: <b>CROSS-REFERENCES 3 OE#</b> — 20972293 · 21707133 · 21707132.<br/>"
            "Tile 4: <b>FITS VOLVO D13</b> — Heavy-duty diesel service; confirm by engine and OEM part number.<br/>"
            "Tile 5: <b>FAIR PRICE, REAL VALUE</b> — Aftermarket replacement built for value, not a cut corner."
        ),
        visual="5 square tiles, RH-blue accent corner on each, consistent composition. Small technical icons (4-filter box · named filters · cross-reference list · truck fit · value tag). Filter photography consistent across tiles.",
        alt="Five-tile A+ carousel covering the RH Filters D13 kit differentiators: complete 4-filter kit, the right named filters, OE cross-reference, Volvo D13 fit, value.",
    ),
    AIModule(
        name="Module 3 — Q&A: Fitment & contents",
        role="a+_qa",
        headline="FITMENT QUESTIONS, ANSWERED",
        body=(
            "<b>Q.</b> What exactly is in the kit?<br/>"
            "<b>A.</b> Four filters for one D13 service: 2 x LF667 full-flow spin-on oil filters, 1 x LF3654 "
            "bypass spin-on oil filter and 1 x FF5507 spin-on secondary fuel filter — combining full-flow "
            "oil, bypass oil and fuel filtration in one coordinated kit.<br/><br/>"

            "<b>Q.</b> How do I know this fits my truck?<br/>"
            "<b>A.</b> It is an aftermarket replacement for Volvo D13 heavy-duty diesel service. Confirm by "
            "your engine and OEM part number, and match the cross-references — OE# 20972293, 21707133 and "
            "21707132 — against your current filters before ordering.<br/><br/>"

            "<b>Q.</b> Is this an OEM part?<br/>"
            "<b>A.</b> No. It is an aftermarket replacement that cross-references the listed OE numbers. The "
            "OE numbers are shown for reference only.<br/><br/>"

            "<b>Q.</b> What are the threads on each filter?<br/>"
            "<b>A.</b> LF667 full-flow oil: 1 1/8-16 thread. LF3654 bypass oil: 1 3/8-16 thread. FF5507 "
            "secondary fuel: M32 x 1.5 thread. All four are spin-on for conventional workshop install.<br/><br/>"

            "<b>Q.</b> Will I be missing anything for the service?<br/>"
            "<b>A.</b> The kit supplies the four filters for a D13 oil-and-fuel change. Add your engine oil "
            "and any seals your procedure calls for, and change all four filters together at your interval."
        ),
        visual="Vertical Q/A table, RH-green divider lines between questions, small RH-blue Q. and A. labels. Clean technical layout, plenty of whitespace.",
        alt="Premium A+ Q&A module answering contents, fitment, OEM status, per-filter threads and service completeness for the RH Filters D13 oil change kit.",
    ),
    AIModule(
        name="Module 4 — Banner: The right filters, every time",
        role="a+_banner",
        headline="THE RIGHT FILTERS, MATCHED.",
        body=(
            "The most common complaint with diesel filters is a wrong or missing part — the compatibility "
            "mismatch that sends you back to the parts counter. This kit answers it directly: the four "
            "correct D13 filters, matched and verified, in one box. 2 x LF667 full-flow oil, 1 x LF3654 "
            "bypass oil and 1 x FF5507 fuel — an aftermarket replacement that cross-references OE# 20972293, "
            "21707133 and 21707132. Confirm by your engine and OEM part number, and the whole service is covered."
        ),
        visual="Wide banner: a clean knolling flat-lay of the four canisters, each with a caller line and label (2x LF667 FULL-FLOW · LF3654 BYPASS · FF5507 FUEL), an RH-green check beside each. RH blue + green only, engineering-data-sheet styling.",
        alt="A+ banner laying out the four matched RH Filters D13 filters with labels and OE cross-reference numbers.",
    ),
    AIModule(
        name="Module 5 — Banner: Built for the working truck",
        role="a+_banner",
        headline="BUILT FOR THE WORKING TRUCK.",
        body=(
            "Long-haul, regional or vocational, a D13 earns its keep — and its oil and fuel filters take the "
            "load. This kit spins all four on with conventional shop tools: full-flow and bypass oil "
            "filtration to keep the oil clean, plus a secondary fuel filter for clean fuel to the injection. "
            "One box, one pass, the right four filters — built for value, not a cut corner."
        ),
        visual="Triptych banner: LEFT — the four filters staged on a shop bench by a Volvo D13 engine (gloved hand, no face). CENTER — extreme macro of a spin-on filter's pleated media. RIGHT — heavy-duty truck on the highway, soft focus, unbranded. Cool industrial light with warm fill; RH blue + green accents.",
        alt="Triptych A+ banner showing the RH Filters D13 kit on a service bench, a filter-media close-up, and a heavy-duty truck on the highway.",
    ),
    AIModule(
        name="Module 6 — Comparison: Complete kit vs piecing it together",
        role="a+_comparison",
        headline="COMPLETE KIT VS PIECING IT TOGETHER",
        body=(
            "Compare across 3 columns: <b>RH Filters complete D13 kit (this product)</b> · "
            "Ordering filters one at a time · A mismatched or partial set.<br/><br/>"
            "Rows: Completeness (all four matched filters vs missing a part) · Wrong-part risk "
            "(cross-referenced and verified vs guesswork) · Coverage (full-flow + bypass oil + fuel vs "
            "partial) · Trips to the counter (one box vs a second trip) · Fit confirmation (OE cross-reference "
            "+ engine vs hope) · Value (one fair-price kit vs paying piecemeal).<br/><br/>"
            "Highlight the RH Filters column with a soft RH-green tint. Other columns are descriptors "
            "only — no brand names."
        ),
        visual="Standard Amazon Premium Comparison Chart, 3 columns, RH-blue header row, RH-green tint on the RH Filters column. Small check / caution icons per cell. No brand names in the comparison columns.",
        alt="Premium comparison chart for the RH Filters complete D13 kit versus ordering one at a time and a partial set across completeness, wrong-part risk, coverage, trips, fit and value.",
    ),
    AIModule(
        name="Module 7 — Carousel (5 tiles): The RH Filters range",
        role="a+_carousel",
        headline="THE RH FILTERS RANGE",
        body=(
            "Tile 1: <b>OIL CHANGE &amp; SERVICE KITS (this product)</b> — Complete matched filter sets for one service.<br/>"
            "Tile 2: <b>OIL FILTERS</b> — Full-flow &amp; bypass spin-on oil filters for heavy-duty engines.<br/>"
            "Tile 3: <b>FUEL FILTERS &amp; SEPARATORS</b> — Spin-on fuel filters and fuel/water separators.<br/>"
            "Tile 4: <b>ENGINE &amp; CABIN AIR FILTERS</b> — Cleaner intake air and cleaner cab air.<br/>"
            "Tile 5: <b>AIR-DRYER FILTERS &amp; KITS</b> — Air-brake system filtration and service kits.<br/>"
            "<i>Confirm each SKU against your OE cross-reference number before ordering.</i>"
        ),
        visual="5 identical-composition product tiles, RH blue + green accent corner on each, consistent heavy-duty filter photography across the range. Category label on each tile.",
        alt="Five-tile A+ carousel of the RH Filters range: oil change and service kits, oil filters, fuel filters and separators, engine and cabin air filters, and air-dryer filters and kits.",
    ),
]


QA = [
    AIQA(q="What exactly comes in this D13 oil change kit?",
         a="Four filters for one Volvo D13 service: 2 x LF667 full-flow spin-on oil filters, 1 x LF3654 bypass spin-on oil filter, and 1 x FF5507 spin-on secondary fuel filter. Together they cover full-flow oil, bypass oil and fuel filtration in one coordinated kit."),
    AIQA(q="How do I confirm this kit fits my truck?",
         a="It is an aftermarket replacement for Volvo D13 heavy-duty diesel service. Confirm by your engine and OEM part number, and match the cross-references — OE# 20972293, 21707133 and 21707132 — against your current filters before ordering."),
    AIQA(q="Is this an OEM part?",
         a="No. This is an aftermarket replacement oil change kit that cross-references the listed OE numbers. The OE numbers are provided for reference only."),
    AIQA(q="What are the threads and sizes on each filter?",
         a="LF667 full-flow oil: about 263.9 mm high, 107.7 mm outside diameter, 1 1/8-16 thread (quantity 2). LF3654 bypass oil: similar size, 1 3/8-16 thread. FF5507 secondary fuel: about 263.9 mm high, ~108 mm outside diameter, M32 x 1.5 thread. All four are spin-on."),
    AIQA(q="Why buy the kit instead of ordering filters one at a time?",
         a="The kit gives you the four matched, cross-referenced filters for one D13 service in a single box — no missing part, no wrong filter and no second trip to the parts counter. It is built for fair-price value over buying piecemeal."),
    AIQA(q="Will I need anything else for the service?",
         a="The kit supplies the four filters. Add your engine oil and any seals your service procedure calls for. Change all four filters together at the interval in your maintenance schedule."),
]


# Backend KWs — stem-deduped, byte-packed. Avoid brand words already in the title and superlatives.
# Mix heavy-duty diesel terms + OE numbers + relevant generic search terms from the axis.
BACKEND = (
    "oil change kit oil and filter kit bypass oil filter kit diesel bypass oil filter kit volvo d13 "
    "oil filter kit truck oil filter fuel oil filter full flow oil filter secondary fuel filter "
    "spin on heavy duty diesel semi volvo vnl service kit complete kit aftermarket replacement cross "
    "reference lf667 lf3654 ff5507 owner operator fleet maintenance 20972293 21707133 21707132 "
    "kit de cambio de aceite filtro de aceite diesel"
)


def main() -> None:
    print("Loading Royal Holding USA customer + parsing RH Filters D13 oil-change-kit Excel…")
    cust = load_customer("royal_holding_usa")
    brief = parse_excel(EXCEL)
    OUT = HERE / f"{PLAN_NO}_{ASIN}_Image Plan.pdf"
    print(f"  Product: {brief.product_name}")
    print(f"  ASIN: {ASIN}  Marketplace: {cust.marketplace}")
    print(f"  USPs={len(brief.usps)} KWs={len(brief.all_keywords)} reviews=+{len(brief.good_reviews)}/-{len(brief.bad_reviews)}")
    real_len = len(TITLE.replace('&amp;', '&'))
    print(f"  TITLE real length: {real_len} chars (limit 200)")

    builder = BriefBuilder(cust, brief, OUT, ai=None)
    builder._ai_title = TITLE
    builder._ai_bullets = BULLETS
    builder._ai_images = IMAGES
    builder._ai_modules = MODULES
    builder._ai_qa = QA
    builder._ai_backend = BACKEND
    builder.copy_source_label = "Hand-written senior copy (KW-led, fitment-verified)"

    print("Building branded PDF…")
    pdf_path = builder.build()
    size_kb = pdf_path.stat().st_size // 1024
    import re
    pages = len(re.findall(rb'/Type\s*/Page[^s]', pdf_path.read_bytes()))
    print(f"Built: {pdf_path}")
    print(f"  Pages: {pages}  Size: {size_kb} KB")


if __name__ == "__main__":
    main()
