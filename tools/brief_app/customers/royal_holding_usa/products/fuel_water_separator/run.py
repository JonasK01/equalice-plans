"""RH Filters Heavy-Duty FUEL/WATER SEPARATOR — Amazon image plan (image-led brief).
Hand-written, KW-led, fitment-verified senior copy injected into the branded ReportLab pipeline.

Brand: RH Filters by Royal Holding USA (aftermarket heavy-duty truck filtration).
Marketplace: amazon.com (US). Overlay language: ENGLISH.

Product: RH32006 spin-on FUEL/WATER SEPARATOR with open bowl port — AFTERMARKET REPLACEMENT.
Fits Volvo VNL 780 with Cummins ISX, model years 2008–2017.
Cross-references OE# FS19799 · BF1355-O · 11-9982/119982 · LFF9982 · 33938 · 39123845.
9 micron nominal / 40 micron absolute · 1 1/4-12 mounting thread · M95×2.5 bowl thread.
(See SOURCE_NOTES.md for the full verified fact set.)

LANGUAGE SPLIT (the standard):
  • ENGLISH (designer-facing) — art direction the designer reads:
    image purpose, background, visual, props, lighting, why_it_works, ctr, cvr, module visual.
  • ENGLISH (customer-facing, amazon.com) — text the shopper reads:
    TITLE, BULLETS, overlay, overlay_sub, module headline+body, QA, BACKEND.

OVERLAY RULE: sell the OUTCOME, not the action. Every on-image overlay leads with the result a
trucker wants (clean fuel, water kept OUT of the injectors, exact fit, brand-new sealed unit).
Hard limits (auto-linted on build):
  overlay ≤ 30 chars AND ≤ 5 words · overlay_sub ≤ 90 chars
  module headline ≤ 38 chars · bullet head <b>…</b> ≤ 45 chars · TITLE ≤ 200 real chars

ELEVATED COPY — 4 levers applied:
  1) VOICE-OF-CUSTOMER: praise = good quality, competitive price, strong value, real fuel-and-water
     separation. The negatives are on a COMPETITOR unit (leaked, arrived used/dented, fuel smell) —
     so RH owns the opposite: brand-new, factory-sealed, exact-fit, strips water properly.
  2) DREAM-OUTCOME-FIRST: hero + bullet 1 lead with clean fuel and water kept out of the injectors,
     exact fit for the Volvo/Cummins, no guesswork.
  3) POWER-WORDS + specificity: water-stripping, injector-protecting, 9-micron, factory-sealed, dialed-in fit.
  4) KEYWORD-WEAVING: fuel water separator · water separator fuel filter · water separating fuel filter ·
     fuel/water separator filter.

COMPLIANCE (build auto-checks):
  - Aftermarket only — "aftermarket replacement, cross-references OE# …"; never imply it IS an OEM part.
  - NO "replaces" before a capitalized/part word (trips the competitor checker) — use "cross-references".
  - NO vague "universal fit" — state exact compatibility (Volvo VNL 780 · Cummins ISX · 2008–2017).
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
PLAN_NO = "04"
ASIN = "B0CS3X7ZS1"


# ===== KW-led, fitment-verified, aftermarket-compliant EN copy (customer-facing) =====
# Title is HTML-escaped by the builder, so a literal "&" counts as 1 real char. Keep <= 200.

TITLE = (
    "RH Filters Heavy-Duty Fuel Water Separator — Aftermarket Replacement for OE# FS19799 "
    "BF1355-O 119982 LFF9982 33938 39123845 — Fits Volvo VNL 780 Cummins ISX 2008-2017, 9 Micron"
)

BULLETS = [
    "<b>WATER OUT, INJECTORS PROTECTED</b> — This fuel water separator strips water and grit from "
    "the diesel before they reach your injectors, so the engine gets clean, dry fuel — exactly the "
    "fuel-and-water separation owner-operators count on, mile after mile.",

    "<b>FITS VOLVO VNL 780 · CUMMINS ISX 2008-2017</b> — Built as the exact spin-on water separator "
    "fuel filter for the Volvo VNL 780 with the Cummins ISX engine, model years 2008 through 2017. "
    "Dialed-in fit, no guesswork — confirm your year before ordering.",

    "<b>CROSS-REFERENCES 6 OE NUMBERS</b> — Aftermarket replacement that cross-references OE# FS19799, "
    "BF1355-O, 11-9982 / 119982, LFF9982, 33938 and 39123845. Match the number on your current "
    "fuel/water separator filter to confirm fitment. This is not an OEM-branded part.",

    "<b>9-MICRON SPIN-ON, OPEN BOWL PORT</b> — Spin-on separator rated 9 micron nominal / 40 micron "
    "absolute, with a 1 1/4-12 mounting thread and an open M95 x 2.5 bowl port for your compatible "
    "water-collecting bowl. Two gaskets included so the seal seats clean.",

    "<b>BRAND-NEW, FACTORY-SEALED QUALITY</b> — Every water separating fuel filter ships brand-new and "
    "factory-sealed — never used, never dented. RH Filters by Royal Holding USA: heavy-duty truck "
    "filtration built for real value, not a cut corner.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (pure white, fitment-spec read)",
        role="hero",
        background="Pure white #FFFFFF, Amazon main-image compliant. Separator fills >=85% of frame. NO overlay text, NO graphics, NO badges (policy).",
        purpose="Win the click in a diesel-parts grid by reading instantly as a real heavy-duty spin-on fuel/water separator with genuine build quality.",
        visual=(
            "Single RH Filters RH32006 fuel/water separator shot at a slightly elevated 3/4 angle so the "
            "buyer sees BOTH the spin-on threaded mounting end AND the open bowl port on the base. The "
            "printed RH Filters part label is rotated toward camera and legible (RH32006). Canister large, "
            "sharp, centered, occupying ~88% of the frame. Crisp focus edge to edge so the seal gasket and "
            "thread machining read as a real heavy-duty part, not a stock render. No props, no text — clean "
            "catalog hero. (Overlay intentionally empty per Amazon main-image policy.)"
        ),
        overlay="",
        overlay_sub="",
        props=["single spin-on fuel/water separator (3/4 angle showing threaded end + open bowl port)"],
        lighting="Soft even studio light, 5000K, large top key with twin side fill to kill harsh shadow. Gentle gradient shadow under the canister for grounding. Hard enough catch on the gasket to show real rubber.",
        why_it_works=(
            "Compliant white-background hero, but framed so the spin-on thread and the open bowl port are "
            "both visible — the two cues a diesel mechanic uses to recognize the correct separator at "
            "thumbnail size. Showing build quality pre-answers the 'is it quality?' doubt before the click."
        ),
        ctr="The 3/4 angle exposes the threaded mount and open bowl port, so the listing reads as a genuine heavy-duty separator against flat competitor renders in the grid.",
        cvr="A sharp, honest catalog shot signals an accurate listing — the top positive review driver — and counters the 'arrived used/dented' fear from competitor reviews before the gallery even opens.",
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: Fitment board (Volvo/Cummins + OE cross-reference)",
        role="hook",
        background="Mood blue #EAF1F8 with a clean technical grid texture — engineering data-sheet feel.",
        purpose="Answer the #1 buyer question instantly: WILL THIS FIT MY TRUCK? Lead with exact compatibility + the OE cross-reference list.",
        visual=(
            "LEFT 45%: the separator at a 3/4 angle, label toward camera. RIGHT 55%: a clean fitment panel "
            "in RH blue.\n"
            "  Top block — bold: 'FITS VOLVO VNL 780 · CUMMINS ISX · 2008-2017'.\n"
            "  Below it a 'CROSS-REFERENCES OE#' list, each on its own line in a monospace technical font:\n"
            "    FS19799 · BF1355-O · 11-9982 / 119982 · LFF9982 · 33938 · 39123845\n"
            "A thin RH-green callout strip reads: 'Match your current separator number before ordering.' "
            "Small 'AFTERMARKET REPLACEMENT' tag in the corner (RH blue) so there is zero OEM implication. "
            "One callout, one action cue (match-before-order), one prop (the separator)."
        ),
        overlay="FITS VOLVO VNL CUMMINS ISX",
        overlay_sub="Aftermarket fuel water separator · cross-references FS19799, BF1355-O and 4 more OE#.",
        props=["separator (3/4 angle)", "FITS Volvo/Cummins fitment panel", "OE cross-reference list", "AFTERMARKET REPLACEMENT corner tag"],
        lighting="Flat even technical light — this is a data frame, legibility beats mood. Slight rim on the separator to lift it off the blue field.",
        why_it_works=(
            "The single most decisive image for this category. Truckers shop separators by truck/engine and "
            "by OE number; surfacing the exact Volvo VNL 780 / Cummins ISX / 2008-2017 fit plus all six "
            "verified cross-references kills the top return driver (unclear fitment) and frames the part as aftermarket."
        ),
        ctr="An exact 'FITS VOLVO VNL · CUMMINS ISX' line plus a part number the buyer is actively searching is a direct match that stops the scroll.",
        cvr="Showing the precise truck/engine fit and six cross-reference numbers with a 'match before ordering' cue defuses the wrong-fitment fear that drives the worst reviews and returns.",
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: Cutaway showing water separation + 9-micron media",
        role="educate",
        background="White with a soft RH-blue panel behind the cutaway for separation.",
        purpose="Prove the part actually STRIPS WATER and filters to spec — defend it against thin commodity separators.",
        visual=(
            "Split frame. LEFT: a cutaway / sectioned view of the separator showing diesel flowing down "
            "through the pleated media while water droplets coalesce and drop into the open bowl port at the "
            "base — short arrows + labels 'CLEAN FUEL UP TO THE ENGINE' and 'WATER DROPS OUT TO THE BOWL.' "
            "RIGHT: an extreme macro of the pleated media labeled '9 MICRON NOMINAL — traps grit before the "
            "injectors.' Three RH-green spec chips along the bottom: '9 MICRON NOM / 40 ABS' · "
            "'SPIN-ON · OPEN BOWL PORT' · '1 1/4-12 THREAD.' Clean engineering-diagram styling, RH blue + green only."
        ),
        overlay="STRIPS WATER FROM FUEL",
        overlay_sub="Water coalesces and drops to the bowl · 9-micron media traps grit before the injectors.",
        props=["separator cutaway / section view", "media macro", "3 spec chips", "water-drop + clean-fuel arrows"],
        lighting="Clean studio key with a raking macro light on the pleats to reveal media texture and pleat depth.",
        why_it_works=(
            "Buyers reward real fuel-and-water separation and distrust low-information listings. Showing the "
            "water coalescing into the bowl plus the 9-micron media macro proves the separator does its core "
            "job — earning trust over an unbranded commodity unit, in the mechanic's own language."
        ),
        ctr="A water-separation cutaway is a pattern interrupt in a grid of plain product shots — it signals technical depth and pulls the detail-oriented diesel buyer in.",
        cvr="Visual proof of water dropping to the bowl and a tight 9-micron pleat pack converts buyers who were burned by separators that passed water through to the injectors.",
    ),
    AIImagePlanItem(
        name="Image 4 — Desire: Mounted on the fuel system",
        role="desire",
        background="Real engine-bay / fuel-filter-head context on a heavy-duty truck, neutral industrial tones.",
        purpose="Show the separator in its actual home so the buyer can picture the swap and confirm the spin-on + bowl interface matches their head.",
        visual=(
            "Three-quarter shot of the RH separator spun onto a heavy-duty fuel filter head, the clear/black "
            "water-collecting bowl threaded onto the open port at the base. A gloved hand (fingers only, no "
            "face) just finishing the spin-on, a clean shop rag as the single supporting prop. Small RH-blue "
            "callout: 'Spins on by hand · seat the gasket.' One action cue — the hand turning the canister home."
        ),
        overlay="SPINS ON IN MINUTES",
        overlay_sub="Spin-on separator threads onto your filter head; bowl ports onto the M95 base.",
        props=["fuel filter head", "water-collecting bowl on open port", "gloved hand (fingers only)", "shop rag"],
        lighting="Industrial garage light — cool overhead with a warm practical fill from the side. Honest shop atmosphere, not a sterile studio.",
        why_it_works=(
            "Places the part in the buyer's reality (the filter head + bowl) and answers 'how hard is the "
            "swap?' — echoing the 'easy to use' positive review theme and letting the buyer visually confirm "
            "the spin-on thread and bowl port match their setup before buying."
        ),
        ctr="An on-truck install shot reads as 'this is the exact application' and stands out from white-only competitor galleries.",
        cvr="Seeing the spin-on thread and bowl port engage a real head reassures buyers worried about the leak/fit failures called out in competitor reviews.",
    ),
    AIImagePlanItem(
        name="Image 5 — Trust: Spec & fitment card",
        role="trust",
        background="White with soft RH-blue spec panels for separation.",
        purpose="Stack the verification a fleet buyer scans for: type, rating, thread/bowl interface and how to confirm fitment — kills dimension/return risk.",
        visual=(
            "Centered separator (label to camera). Four spec tiles in the corners, RH-blue headers:\n"
            "  • TOP-LEFT — TYPE: Spin-on fuel/water separator, open bowl port\n"
            "  • TOP-RIGHT — RATING: 9 micron nominal / 40 micron absolute\n"
            "  • BOTTOM-LEFT — THREADS: 1 1/4-12 mount · M95 x 2.5 bowl\n"
            "  • BOTTOM-RIGHT — FITS: Volvo VNL 780 · Cummins ISX · 2008-2017\n"
            "Across the bottom, a single RH-green action strip: 'CONFIRM FITMENT — match the OE cross-reference "
            "number on your current separator before ordering.' Small corner tag: 'AFTERMARKET REPLACEMENT.' "
            "Clean, technical, fleet-friendly."
        ),
        overlay="SPECS AND FITMENT CLEAR",
        overlay_sub="Spin-on · 9-micron · 1 1/4-12 mount · M95 bowl — confirm by OE cross-reference number.",
        props=["separator (center)", "4 spec tiles", "green confirm-fitment strip", "AFTERMARKET REPLACEMENT tag"],
        lighting="Even studio light, tiles legible at thumbnail size, crisp catch on the canister.",
        why_it_works=(
            "Fleets and owner-operators buy on spec certainty. Listing type, micron rating, thread/bowl "
            "interface and exact truck fit — plus a match-the-cross-reference instruction — directly counters "
            "the dimension-mismatch and unclear-compatibility complaints that drive returns."
        ),
        ctr="A clean spec card signals a thorough, accurate listing and rewards the buyer who clicks through looking for technical detail.",
        cvr="Giving exact specs, the thread/bowl interface and a confirm-by-cross-reference instruction removes the last fit doubt for a fleet maintenance purchase.",
    ),
    AIImagePlanItem(
        name="Image 6 — Desire: Clean fuel, steady uptime (value framing)",
        role="desire",
        background="Heavy-duty Volvo-style semi on the highway, soft-focus; product inset on a clean lower band.",
        purpose="Tie clean, dry fuel to uptime and maintenance value — the owner-operator's real payoff — without unverified performance claims.",
        visual=(
            "Top 60%: a heavy-duty semi truck on the open highway, soft-focus, long-haul duty (NO competitor "
            "logos, NO readable fleet branding). Lower 40%: a clean RH-blue band holding the separator (sharp) "
            "on the left and three value chips on the right:\n"
            "  • CLEAN, DRY FUEL TO THE INJECTORS\n"
            "  • WATER KEPT OUT OF THE FUEL SYSTEM\n"
            "  • PROTECTS INJECTORS — FEWER UNPLANNED STOPS\n"
            "One supporting prop only (the separator). Copy stays a maintenance benefit — no numeric mpg or power claim."
        ),
        overlay="CLEAN FUEL, STEADY UPTIME",
        overlay_sub="Water kept out of the fuel system protects the injectors and supports steady uptime.",
        props=["heavy-duty truck (soft focus, unbranded)", "separator (inset)", "3 value chips"],
        lighting="Natural highway daylight up top; clean even studio light on the inset separator so it stays the sharp focal anchor.",
        why_it_works=(
            "Connects the part to the owner-operator's bottom line — uptime and cost-per-mile — the real value "
            "lever for this audience, while keeping every claim a maintenance benefit to stay clear of "
            "unverified-performance compliance limits."
        ),
        ctr="A truck-on-highway scene gives instant 'this is for my rig' context that a bare product shot can't, drawing the fleet buyer in.",
        cvr="Framing the separator as injector-protecting, water-stripping maintenance value converts the cost-conscious owner-operator who buys on total cost.",
    ),
    AIImagePlanItem(
        name="Image 7 — Close: RH Filters brand + brand-new, factory-sealed",
        role="close",
        background="Clean RH-blue brand panel with subtle technical grid.",
        purpose="Close on brand promise, the brand-new/factory-sealed edge, and a clear service-interval repurchase cue.",
        visual=(
            "Centered: the RH Filters separator, label to camera, with a subtle RH-green accent sweep behind "
            "it and a small 'FACTORY-SEALED · BRAND-NEW' seal badge. Below, the RH Filters brand mark and "
            "tagline 'Top quality. Fair price.' A clean lower strip with a service reminder: 'FUEL/WATER "
            "SEPARATOR — drain water regularly, replace at your service interval.' Small corner tag repeats "
            "'AFTERMARKET REPLACEMENT — cross-references OE# FS19799 / BF1355-O / 119982 / LFF9982 / 33938 / "
            "39123845.' Calm, confident, technical."
        ),
        overlay="NEW, SEALED, DIALED-IN FIT",
        overlay_sub="Brand-new, factory-sealed separator — drain the water, change at your service interval.",
        props=["separator (center)", "FACTORY-SEALED badge", "RH Filters brand mark + tagline", "service-interval strip", "OE cross-reference tag"],
        lighting="Clean even studio light, confident product-forward key, crisp catch on the canister.",
        why_it_works=(
            "Reinforces the value tagline and the brand-new/factory-sealed edge (the direct counter to "
            "competitors' 'arrived used/dented' reviews), gives a concrete repurchase trigger (service-interval "
            "replacement), and restates the OE cross-reference one last time so the buyer leaves certain of fit and brand value."
        ),
        ctr="A confident brand-close with the tagline and a factory-sealed badge builds the trust that turns a browse into a brand-loyal click.",
        cvr="The brand-new/sealed promise plus a drain-and-replace reminder and a final cross-reference recap seals fitment confidence and primes repeat fleet orders.",
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Brand banner: Heavy-duty filtration, fair price.",
        role="a+_banner",
        headline="WATER OUT. INJECTORS PROTECTED.",
        body=(
            "RH Filters by Royal Holding USA builds aftermarket replacement filters for the trucks that keep "
            "working. This heavy-duty fuel water separator strips water and grit from the diesel before they "
            "reach the injectors — an aftermarket replacement that cross-references OE# FS19799, BF1355-O, "
            "11-9982 / 119982, LFF9982, 33938 and 39123845, built for the Volvo VNL 780 with the Cummins ISX, "
            "model years 2008 through 2017."
        ),
        visual="Wide cinematic shot: heavy-duty truck in an industrial yard at golden hour (no readable competitor branding), the RH Filters fuel/water separator sharp in the foreground-right on a clean surface. RH blue logo upper-left, green accent rule along the bottom band, tagline 'Top quality. Fair price.'",
        alt="RH Filters heavy-duty spin-on fuel water separator in the foreground with a heavy-duty truck in an industrial yard behind it.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): Why this fuel/water separator",
        role="a+_carousel",
        headline="WHY THIS WATER SEPARATOR",
        body=(
            "Tile 1: <b>STRIPS WATER FROM FUEL</b> — Coalesces water and grit before they reach the injectors.<br/>"
            "Tile 2: <b>EXACT FIT</b> — Volvo VNL 780 · Cummins ISX · model years 2008-2017.<br/>"
            "Tile 3: <b>CROSS-REFERENCES 6 OE#</b> — FS19799 · BF1355-O · 119982 · LFF9982 · 33938 · 39123845.<br/>"
            "Tile 4: <b>9-MICRON SPIN-ON</b> — 9 micron nom / 40 abs · 1 1/4-12 mount · open M95 bowl port.<br/>"
            "Tile 5: <b>BRAND-NEW, SEALED</b> — Ships factory-sealed, never used. Aftermarket replacement."
        ),
        visual="5 square tiles, RH-blue accent corner on each, consistent composition. Small technical icons (water-drop into bowl · truck fit · cross-reference list · spin-on thread · sealed box). Separator photography consistent across tiles.",
        alt="Five-tile A+ carousel covering RH Filters fuel water separator differentiators: water separation, exact fit, OE cross-reference, 9-micron spin-on, brand-new sealed.",
    ),
    AIModule(
        name="Module 3 — Q&A: Fitment & application",
        role="a+_qa",
        headline="FITMENT QUESTIONS, ANSWERED",
        body=(
            "<b>Q.</b> How do I know this fits my truck?<br/>"
            "<b>A.</b> This is an aftermarket replacement fuel/water separator for the Volvo VNL 780 with the "
            "Cummins ISX engine, model years 2008 through 2017. Match the OE / cross-reference number on your "
            "current separator — FS19799, BF1355-O, 11-9982 / 119982, LFF9982, 33938 or 39123845 — and confirm "
            "your year before ordering.<br/><br/>"

            "<b>Q.</b> Is this an OEM part?<br/>"
            "<b>A.</b> No. It is an aftermarket replacement that cross-references the listed OE numbers. The OE "
            "numbers are shown for reference only.<br/><br/>"

            "<b>Q.</b> What does it actually do?<br/>"
            "<b>A.</b> It is a water separating fuel filter. As diesel passes through the 9-micron media, water "
            "and grit coalesce and drop into the bowl at the open port, so clean, dry fuel goes on to the injectors.<br/><br/>"

            "<b>Q.</b> What are the threads and rating?<br/>"
            "<b>A.</b> Spin-on with a 1 1/4-12 mounting thread and an open M95 x 2.5 bowl port for a compatible "
            "water-collecting bowl. Rated 9 micron nominal / 40 micron absolute. Two gaskets are included.<br/><br/>"

            "<b>Q.</b> How often should I service it?<br/>"
            "<b>A.</b> Drain the collected water regularly and fit a new separator at the interval in your "
            "maintenance schedule, or sooner if you see water carry-over. Keeping a fresh separator in service "
            "helps protect the injectors."
        ),
        visual="Vertical Q/A table, RH-green divider lines between questions, small RH-blue Q. and A. labels. Clean technical layout, plenty of whitespace.",
        alt="Premium A+ Q&A module answering fitment, OEM status, water separation, threads/rating and service interval for the RH Filters fuel water separator.",
    ),
    AIModule(
        name="Module 4 — Banner: How water separation protects the injectors",
        role="a+_banner",
        headline="WATER NEVER REACHES THE FUEL.",
        body=(
            "Water in diesel is what kills injectors and pumps. As fuel flows through this separator, the "
            "9-micron media drops water and grit out into the bowl at the base, so only clean, dry fuel "
            "continues up to the engine. Drain the bowl on schedule and the injectors stay protected — exactly "
            "the real fuel-and-water separation owner-operators count on."
        ),
        visual="Wide banner with a clean cutaway diagram: diesel flowing down through the pleated media, water droplets coalescing and falling into the bowl at the open port, an arrow showing clean dry fuel continuing up to the engine. RH blue + green only, engineering-diagram styling.",
        alt="A+ banner diagram showing how the RH Filters separator drops water out of the fuel into the bowl and sends clean dry fuel to the engine.",
    ),
    AIModule(
        name="Module 5 — Banner: Built for the working truck",
        role="a+_banner",
        headline="BUILT FOR THE WORKING TRUCK.",
        body=(
            "Long-haul, regional or off-road, the fuel system takes a beating. This spin-on separator threads "
            "onto your filter head, the open M95 bowl port carries a compatible water bowl, and the 9-micron "
            "media keeps water and grit out of the injectors. Ships brand-new and factory-sealed — never used, "
            "never dented — so it seats and seals the way it should the first time."
        ),
        visual="Triptych banner: LEFT — separator spun onto a fuel filter head with the bowl on the port (gloved hand, no face). CENTER — extreme macro of the pleated 9-micron media. RIGHT — heavy-duty truck on the highway, soft focus, unbranded. Cool industrial light with warm fill; RH blue + green accents.",
        alt="Triptych A+ banner showing the RH Filters separator mounted on a filter head, a media close-up, and a heavy-duty truck on the highway.",
    ),
    AIModule(
        name="Module 6 — Comparison: This separator vs an overdue / loose unit",
        role="a+_comparison",
        headline="FRESH SEALED SEPARATOR VS A WORN ONE",
        body=(
            "Compare across 3 columns: <b>RH Filters fuel/water separator (this product)</b> · "
            "An overdue / water-logged separator · A used or poorly-sealed unit.<br/><br/>"
            "Rows: Water separation (drops water to the bowl vs water carry-over) · Fuel to the injectors "
            "(clean and dry vs contaminated) · Condition on arrival (brand-new, factory-sealed vs used / dented) · "
            "Fit confirmation (OE cross-reference + exact truck/engine vs guesswork) · Effect on injectors "
            "(protected vs added wear) · Service (spins on by hand).<br/><br/>"
            "Highlight the RH Filters column with a soft RH-green tint. Competitor columns are condition "
            "descriptors only — no brand names."
        ),
        visual="Standard Amazon Premium Comparison Chart, 3 columns, RH-blue header row, RH-green tint on the RH Filters column. Small check / caution icons per cell. No brand names in the comparison columns.",
        alt="Premium comparison chart for the RH Filters fuel water separator versus a water-logged unit and a used/poorly-sealed unit across water separation, fuel quality, condition, fit and service.",
    ),
    AIModule(
        name="Module 7 — Carousel (5 tiles): The RH Filters range",
        role="a+_carousel",
        headline="THE RH FILTERS RANGE",
        body=(
            "Tile 1: <b>FUEL/WATER SEPARATORS (this product)</b> — Strip water from diesel before the injectors.<br/>"
            "Tile 2: <b>FUEL FILTERS</b> — Spin-on &amp; cartridge fuel filters for heavy-duty engines.<br/>"
            "Tile 3: <b>OIL FILTERS</b> — Spin-on &amp; cartridge oil filters for heavy-duty engines.<br/>"
            "Tile 4: <b>ENGINE &amp; CABIN AIR FILTERS</b> — Cleaner intake air and cleaner cab air.<br/>"
            "Tile 5: <b>AIR-DRYER FILTERS &amp; KITS</b> — Air-brake system filtration and complete service kits.<br/>"
            "<i>Confirm each SKU against your OE cross-reference number before ordering.</i>"
        ),
        visual="5 identical-composition product tiles, RH blue + green accent corner on each, consistent heavy-duty filter photography across the range. Category label on each tile.",
        alt="Five-tile A+ carousel of the RH Filters range: fuel/water separators, fuel filters, oil filters, engine and cabin air filters, and air-dryer filters and kits.",
    ),
]


QA = [
    AIQA(q="How do I confirm this fuel/water separator fits my truck?",
         a="It is an aftermarket replacement for the Volvo VNL 780 with the Cummins ISX engine, model years 2008 through 2017. Match the OE / cross-reference number on your current separator against this list: FS19799, BF1355-O, 11-9982 / 119982, LFF9982, 33938, 39123845. If your number is on the list and your year matches, it is designed to fit."),
    AIQA(q="Is this an OEM part?",
         a="No. This is an aftermarket replacement fuel/water separator that cross-references the listed OE numbers. The OE numbers are provided for reference only."),
    AIQA(q="What does the separator actually do?",
         a="It is a water separating fuel filter. As diesel passes through the 9-micron media, water and grit coalesce and drop into the bowl at the open port, so clean, dry fuel goes on to the injectors. Drain the collected water regularly."),
    AIQA(q="What are the threads and the filtration rating?",
         a="Spin-on with a 1 1/4-12 mounting thread and an open M95 x 2.5 bowl port for a compatible water-collecting bowl. It is rated 9 micron nominal / 40 micron absolute, and two gaskets are included so the seal seats clean."),
    AIQA(q="Does it come with the water bowl?",
         a="This listing is the spin-on separator element with an open bowl port. Use it with your compatible M95 x 2.5 water-collecting bowl. Confirm your existing bowl interface before ordering."),
    AIQA(q="What condition does it ship in?",
         a="Brand-new and factory-sealed — never used and never dented. Every unit ships sealed so it seats and seals correctly the first time."),
    AIQA(q="How often should I service it?",
         a="Drain the collected water regularly and fit a new separator at the interval in your maintenance schedule, or sooner if you see water carry-over. A fresh separator helps protect the injectors and the fuel system."),
]


# Backend KWs — stem-deduped, byte-packed. Avoid brand words already in the title and superlatives.
# Mix heavy-duty diesel terms + OE numbers + relevant generic separator search terms from the axis.
BACKEND = (
    "fuel water separator water separator fuel filter water separating fuel filter fuel oil separator "
    "diesel spin on heavy duty truck semi volvo vnl cummins isx injector protection 9 micron bowl "
    "filter head aftermarket replacement cross reference brand new sealed owner operator fleet "
    "maintenance fs19799 bf1355o 119982 lff9982 33938 39123845 filtro separador de agua combustible diesel"
)


def main() -> None:
    print("Loading Royal Holding USA customer + parsing RH Filters fuel/water-separator Excel…")
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
