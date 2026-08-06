"""RH Filters Heavy-Duty Engine Air Filter — Amazon image plan (image-led brief).
Hand-written KW-led, fitment-verified copy injected into the branded ReportLab pipeline.

Brand: RH Filters by Royal Holding USA (aftermarket heavy-duty truck filtration).
Marketplace: amazon.com (US). Overlay language: EN.

Product: radial-seal PRIMARY engine air filter — AFTERMARKET REPLACEMENT.
Replaces OE / cross-reference #: DA8137, P614556, P625128, RS5287, AF4197, LAF4556, WA10149.

Compliance baseline (build auto-checks):
  - Aftermarket replacement only — "replaces OE# …", never imply it IS an OEM/genuine part.
  - No vague "universal fit" — always specify compatibility (radial-seal primary air filter,
    match by OE cross-reference + air-intake housing).
  - No "best / #1 / ultimate / guaranteed" superlatives.
  - No unverified performance / mpg claims — fuel efficiency framed as a maintenance benefit only.
  - No "$", no URL / ".com" / external links in any customer-facing copy.

NOTE: the Excel-parsed ASIN (B0DM4H93466) is malformed — use the literal ASIN below.
"""
from __future__ import annotations
import sys
from pathlib import Path

# This script lives at customers/<brand>/products/<product>/run.py
HERE = Path(__file__).resolve().parent          # the product folder (self-contained)
ROOT = HERE.parents[5]                           # project root (Claude_Code/)
sys.path.insert(0, str(ROOT))

from tools.brief_app.core.customers import load_customer
from tools.brief_app.core.excel_parser import parse_excel
from tools.brief_app.core.pdf_builder import BriefBuilder
from tools.brief_app.core.ai import AIImagePlanItem, AIModule, AIQA


# Inputs/outputs live alongside this script — the product folder is self-contained.
EXCEL = HERE / "listing.xlsx"                    # the SEO "axis" for this product
PLAN_NO = "01"   # SEO listing no. -> output named 0X_<ASIN>_Image Plan.pdf
ASIN = "B0DM4H9346"   # use THIS exact ASIN (the parsed brief.asin is malformed — do NOT use it)


# ===== KW-led copy — fitment-verified, aftermarket-compliant =====
# Title is HTML-escaped by the builder, so use a literal "&" (counts as 1 real char). Keep <= 200.

TITLE = ('RH Filters Heavy-Duty Engine Air Filter — Aftermarket Replacement for OE# DA8137 '
         'P614556 P625128 RS5287 AF4197 LAF4556 WA10149 — Radial-Seal Primary Truck Filter')

BULLETS = [
    "<b>AFTERMARKET REPLACEMENT FOR OE# DA8137 P614556 P625128 RS5287 AF4197 LAF4556 WA10149</b> "
    "— Cross-reference primary air filter. Check your existing filter number and air-intake "
    "housing against this list before ordering to confirm exact fitment — this is not an OEM-branded part.",

    "<b>RADIAL-SEAL PRIMARY AIR FILTER</b> — The radial-seal design seats firmly inside the "
    "housing and helps seal out air leaks and stop dust bypass, so the engine pulls only filtered air. "
    "No clamps or wing-nuts to over-torque &amp; no gasket to mis-seat.",

    "<b>HIGH-EFFICIENCY CELLULOSE MEDIA</b> — Pleated paper / cellulose filter media traps dust, "
    "dirt and airborne contaminants before they reach the engine, protecting the turbo, cylinders "
    "&amp; mass-airflow sensor across long-haul and off-road duty cycles.",

    "<b>HEAVY-DUTY FOR TRUCK &amp; EQUIPMENT INTAKE</b> — Built for compatible heavy-duty truck and "
    "off-highway equipment air-intake systems. Rubber gasket and rigid end caps hold the pleats "
    "square under high airflow &amp; vibration. Match by OE cross-reference, not by guesswork.",

    "<b>EASY SERVICE · MAINTENANCE VALUE</b> — Drops in as a routine-maintenance replacement; swap "
    "it at your scheduled interval with hand tools. Keeping a clean air filter in service supports "
    "fuel efficiency, lower maintenance and engine longevity over the life of the truck.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (pure white, fitment-spec read)",
        role="hero",
        background="Pure white #FFFFFF, Amazon main-image compliant. Filter fills >=85% of frame. NO overlay text, NO graphics, NO badges (policy).",
        purpose="Win the click in a parts search grid by reading instantly as a real heavy-duty radial-seal air filter, shot to show its scale and build quality.",
        visual=(
            "Single RH Filters primary air filter, shot at a slightly elevated 3/4 angle so the "
            "buyer sees BOTH the pleated outer media wall AND the open radial-seal end with its "
            "rubber gasket. Filter is large, sharp, centered, occupying ~88% of the frame. The "
            "printed RH Filters part label is rotated toward camera and legible. Crisp focus edge "
            "to edge so the pleat count and media texture are visible — this reads 'real heavy-duty "
            "part,' not a stock render. No props, no text, no shadow gimmicks — clean catalog hero. "
            "(Overlay text intentionally empty per Amazon main-image policy.)"
        ),
        overlay="",
        overlay_sub="",
        props=["single radial-seal primary air filter (3/4 angle showing media + gasketed end)"],
        lighting="Soft even studio light, 5000K, large top key with twin side fill to kill harsh shadow. Gentle gradient shadow under the filter for grounding. Hard enough catch on the gasket to show it is real rubber.",
        why_it_works=(
            "Compliant white-background hero, but framed so the radial-seal end + pleated media are "
            "both visible — the two cues a diesel mechanic uses to recognize the correct filter type "
            "at thumbnail size. Showing build quality on the main image pre-answers the 'is it quality?' "
            "doubt before the click."
        ),
        ctr="3/4 angle exposes the gasketed radial-seal end and deep pleats, so the listing reads as a genuine heavy-duty part against flat competitor renders in the grid.",
        cvr="Sharp, honest catalog shot signals an accurate listing — the #1 positive review driver ('exactly as pictured') — lowering fit-anxiety before the buyer even opens the gallery.",
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: Replaces OE# cross-reference board",
        role="hook",
        background="Mood blue #EAF1F8 with a clean technical grid texture — engineering data-sheet feel.",
        purpose="Answer the #1 buyer question instantly: WILL THIS FIT? Put the full OE cross-reference list front and center.",
        visual=(
            "LEFT 45%: the air filter at a 3/4 angle, media wall toward camera. RIGHT 55%: a clean "
            "'REPLACES OE# / CROSS-REFERENCE' panel in RH blue, each number on its own line in a "
            "monospace technical font for scannability:\n"
            "  DA8137 · P614556 · P625128 · RS5287 · AF4197 · LAF4556 · WA10149\n"
            "A thin RH-green callout strip under the list reads: 'Match your existing filter number "
            "before ordering.' Small 'AFTERMARKET REPLACEMENT' tag in the corner (RH blue) so there "
            "is zero OEM implication. One callout, one action cue (match-before-order), one prop (filter)."
        ),
        overlay="AFTERMARKET REPLACEMENT FOR OE# DA8137 · P614556 · P625128 · RS5287 · AF4197 · LAF4556 · WA10149",
        overlay_sub="Aftermarket replacement primary air filter — match your existing number before ordering.",
        props=["air filter (3/4 angle)", "OE cross-reference panel", "AFTERMARKET REPLACEMENT corner tag"],
        lighting="Flat even technical light — this is a data frame, legibility beats mood. Slight rim on the filter to separate it from the blue field.",
        why_it_works=(
            "The single most decisive image for this category. Buyers shop air filters by OE / "
            "cross-reference number; surfacing all seven verified numbers in a scannable board kills "
            "the top return driver (unclear compatibility) and frames the part correctly as aftermarket."
        ),
        ctr="The literal 'REPLACES OE#' headline plus a part number the buyer is actively searching is a direct keyword match that stops the scroll.",
        cvr="Showing the exact seven cross-reference numbers and an explicit 'match before ordering' cue defuses the wrong-fitment fear that drives the worst reviews and returns.",
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: Radial-seal cutaway + media close-up",
        role="educate",
        background="White with a soft RH-blue panel behind the cutaway for separation.",
        purpose="Prove filtration QUALITY and explain why the radial-seal design seats cleanly — defends the part against cheap commodity filters.",
        visual=(
            "Split frame. LEFT: a cutaway / sectioned view of the filter showing the pleated cellulose "
            "media depth and the rubber radial-seal gasket pressed against a stylized housing wall, "
            "with a short arrow + label 'RADIAL SEAL — seats inside the housing, helps stop dust bypass.' "
            "RIGHT: an extreme macro of the pleated media surface showing the tight, even pleat pack, "
            "labeled 'HIGH-EFFICIENCY CELLULOSE MEDIA — traps dust before it reaches the engine.' "
            "Three small spec chips along the bottom in RH green: 'PLEATED CELLULOSE MEDIA' · "
            "'RUBBER RADIAL-SEAL GASKET' · 'PRIMARY AIR FILTER.' Clean engineering-diagram styling, "
            "RH blue + green only."
        ),
        overlay="HOW IT PROTECTS YOUR ENGINE",
        overlay_sub="Radial-seal gasket helps stop dust bypass · pleated cellulose media filters the air intake.",
        props=["filter cutaway / section view", "media macro", "3 spec chips", "arrow callouts"],
        lighting="Clean studio key with a raking macro light on the pleats to reveal media texture and pleat depth.",
        why_it_works=(
            "Buyers reward 'good filtration / clean air' and distrust low-information listings. Showing "
            "the cutaway and media macro proves construction quality and explains the radial-seal benefit "
            "in the mechanic's own language — earning trust over an unbranded commodity filter."
        ),
        ctr="A cutaway is a pattern interrupt in a grid of plain product shots — it signals technical depth and pulls the detail-oriented mechanic in.",
        cvr="Visual proof of pleat density and a real rubber gasket converts buyers who were burned by thin, poorly-sealing budget filters.",
    ),
    AIImagePlanItem(
        name="Image 4 — Desire: Installed in the air-intake housing",
        role="desire",
        background="Real engine-bay / air-cleaner housing context, neutral industrial tones.",
        purpose="Show the part in its actual home so the buyer can picture the swap and confirm it is the right shape/seal for their housing.",
        visual=(
            "Three-quarter shot of the air filter seated inside an open heavy-duty air-cleaner housing "
            "(or canister) on a truck, the housing lid lifted to one side, a gloved hand just finishing "
            "seating the filter (fingers only, no face). The radial-seal end is shown engaging the "
            "housing bore. Foreground: a clean shop rag and the lifted housing lid as the single "
            "supporting prop. Small RH-blue callout: 'Seats by hand — no special tools.' One action cue: "
            "the hand pressing the filter home."
        ),
        overlay="DROPS IN AT YOUR SERVICE INTERVAL",
        overlay_sub="Radial-seal filter seats by hand inside the air-cleaner housing — routine maintenance, hand tools only.",
        props=["air-cleaner housing (open)", "gloved hand (fingers only)", "housing lid", "shop rag"],
        lighting="Industrial garage light — cool overhead with a warm practical fill from the side. Honest shop atmosphere, not a sterile studio.",
        why_it_works=(
            "Places the part in the buyer's reality (the housing) and answers 'how hard is the swap?' — "
            "echoing the 'easy installation' positive review theme and letting the buyer visually confirm "
            "the seal style matches their housing before buying."
        ),
        ctr="An in-housing install shot reads as 'this is the exact application' and stands out from white-only competitor galleries.",
        cvr="Seeing the radial seal engage a real housing reassures buyers worried about the housing-fit failures called out in negative competitor reviews.",
    ),
    AIImagePlanItem(
        name="Image 5 — Trust: Spec & fitment card",
        role="trust",
        background="White with soft RH-blue spec panels for separation.",
        purpose="Stack the verification a fleet buyer scans for: filter type, construction, and how to confirm fitment — kills dimension/return risk.",
        visual=(
            "Centered filter (label to camera). Four spec tiles in the corners, RH blue headers:\n"
            "  • TOP-LEFT — FILTER TYPE: Radial-seal PRIMARY air filter\n"
            "  • TOP-RIGHT — MEDIA: High-efficiency pleated cellulose\n"
            "  • BOTTOM-LEFT — SEAL: Molded rubber radial gasket\n"
            "  • BOTTOM-RIGHT — APPLICATION: Heavy-duty truck & equipment air intake\n"
            "Across the bottom, a single RH-green action strip: 'CONFIRM FITMENT — measure your old "
            "filter and match the OE cross-reference numbers before ordering.' Small corner tag: "
            "'AFTERMARKET REPLACEMENT.' Clean, technical, fleet-friendly."
        ),
        overlay="SPECS &amp; FITMENT AT A GLANCE",
        overlay_sub="Radial-seal primary filter · pleated cellulose media · rubber gasket — confirm by OE cross-reference.",
        props=["filter (center)", "4 spec tiles", "green confirm-fitment strip", "AFTERMARKET REPLACEMENT tag"],
        lighting="Even studio light, tiles legible at thumbnail size, crisp catch on the filter.",
        why_it_works=(
            "Fleets and owner-operators buy on spec certainty. Listing filter type, media, seal and "
            "application — plus an explicit measure-and-cross-reference instruction — directly counters "
            "the dimension-mismatch and unclear-compatibility complaints that drive returns."
        ),
        ctr="A clean spec card signals a thorough, accurate listing and rewards the buyer who clicks through looking for technical detail.",
        cvr="Giving exact specs and a measure-before-order instruction removes the last fit doubt for a buyer about to commit a fleet maintenance purchase.",
    ),
    AIImagePlanItem(
        name="Image 6 — Desire: Fleet uptime / value framing",
        role="desire",
        background="Heavy-duty truck on the highway, soft-focus; product inset on a clean lower band.",
        purpose="Tie clean intake to uptime and maintenance value — the owner-operator's real-world payoff — without making unverified mpg claims.",
        visual=(
            "Top 60%: a heavy-duty semi truck on the open highway, soft-focus, conveying long-haul "
            "duty (NO competitor logos, NO readable fleet branding). Lower 40%: a clean RH-blue band "
            "holding the air filter (sharp) on the left and three value chips on the right:\n"
            "  • CLEANER AIR INTAKE\n"
            "  • SUPPORTS FUEL EFFICIENCY WHEN REPLACED ON SCHEDULE\n"
            "  • PROTECTS THE ENGINE — FEWER UNPLANNED STOPS\n"
            "One supporting prop only (the filter). Copy stays a maintenance benefit — no numeric mpg "
            "or horsepower claim."
        ),
        overlay="CLEAN INTAKE. STEADY UPTIME.",
        overlay_sub="A fresh air filter on schedule supports fuel efficiency, lower maintenance and engine longevity.",
        props=["heavy-duty truck (soft focus, unbranded)", "air filter (inset)", "3 value chips"],
        lighting="Natural highway daylight up top; clean even studio light on the inset filter so it stays the sharp focal anchor.",
        why_it_works=(
            "Connects the part to the owner-operator's bottom line — uptime and cost-per-mile — which is "
            "the real value lever for this audience, while keeping every claim a maintenance benefit to "
            "stay clear of unverified-performance compliance limits."
        ),
        ctr="A truck-on-highway scene gives instant 'this is for my rig' context that a bare product shot can't, drawing the fleet buyer in.",
        cvr="Framing the filter as scheduled-maintenance value (uptime, longevity) converts the cost-conscious owner-operator who buys on total cost, not sticker.",
    ),
    AIImagePlanItem(
        name="Image 7 — Close: RH Filters brand + replace-on-schedule",
        role="close",
        background="Clean RH-blue brand panel with subtle technical grid.",
        purpose="Close on brand promise and a clear repurchase / service-interval cue.",
        visual=(
            "Centered: the RH Filters air filter, label to camera, with a subtle RH-green accent sweep "
            "behind it. Below, the RH Filters brand mark and tagline 'Top quality. Fair price.' A clean "
            "lower strip with a service reminder: 'PRIMARY AIR FILTER — inspect at every service, replace "
            "at your scheduled interval.' Small corner tag repeats 'AFTERMARKET REPLACEMENT — replaces OE# "
            "DA8137 / P614556 / P625128 / RS5287 / AF4197 / LAF4556 / WA10149.' Calm, confident, technical."
        ),
        overlay="RH FILTERS — TOP QUALITY. FAIR PRICE.",
        overlay_sub="Aftermarket replacement primary air filter — inspect at every service, change on schedule.",
        props=["air filter (center)", "RH Filters brand mark + tagline", "service-interval strip", "OE cross-reference tag"],
        lighting="Clean even studio light, confident product-forward key, crisp catch on the media.",
        why_it_works=(
            "Reinforces the value tagline and gives a concrete repurchase trigger (service-interval "
            "replacement), while restating the OE cross-reference one last time so the buyer leaves the "
            "gallery certain of both fitment and brand value."
        ),
        ctr="A confident brand-close frame with the tagline builds the trust that turns a browse into a brand-loyal click.",
        cvr="The replace-on-schedule reminder plus a final cross-reference recap seals fitment confidence and primes repeat fleet orders.",
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Brand banner: Heavy-duty filtration, fair price.",
        role="a+_banner",
        headline="HEAVY-DUTY FILTRATION. FAIR PRICE.",
        body=(
            "RH Filters by Royal Holding USA builds aftermarket replacement filters for the trucks and "
            "equipment that keep working. This radial-seal primary air filter is an aftermarket replacement "
            "for OE# DA8137, P614556, P625128, RS5287, AF4197, LAF4556 and WA10149 — high-efficiency "
            "cellulose media engineered to keep dust out of the engine, mile after mile."
        ),
        visual="Wide cinematic shot: heavy-duty truck in an industrial yard at golden hour (no readable competitor branding), the RH Filters air filter sharp in the foreground-right on a clean surface. RH blue logo upper-left, green accent rule along the bottom band, tagline 'Top quality. Fair price.'",
        alt="RH Filters heavy-duty radial-seal engine air filter in the foreground with a heavy-duty truck in an industrial yard behind it.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): Why this air filter",
        role="a+_carousel",
        headline="WHY THIS AIR FILTER",
        body=(
            "Tile 1: <b>CROSS-REFERENCES 7 OE#</b> — DA8137 · P614556 · P625128 · RS5287 · AF4197 · LAF4556 · WA10149.<br/>"
            "Tile 2: <b>RADIAL-SEAL DESIGN</b> — Seats firmly in the housing, helps stop dust bypass.<br/>"
            "Tile 3: <b>HIGH-EFFICIENCY MEDIA</b> — Pleated cellulose traps dust, dirt &amp; contaminants.<br/>"
            "Tile 4: <b>HEAVY-DUTY BUILD</b> — Rubber gasket &amp; rigid end caps for truck &amp; equipment intake.<br/>"
            "Tile 5: <b>EASY SERVICE</b> — Drops in at your interval with hand tools. Aftermarket replacement."
        ),
        visual="5 square tiles, RH-blue accent corner on each, consistent composition. Small technical icons (cross-reference list · radial seal ring · pleated media · gasket + end cap · wrench). Filter photography consistent across tiles.",
        alt="Five-tile A+ carousel covering RH Filters air filter differentiators: OE cross-reference, radial seal, high-efficiency media, heavy-duty build, easy service.",
    ),
    AIModule(
        name="Module 3 — Q&A: Fitment & application",
        role="a+_qa",
        headline="FITMENT QUESTIONS, ANSWERED",
        body=(
            "<b>Q.</b> How do I know this fits my truck?<br/>"
            "<b>A.</b> This is an aftermarket replacement primary air filter. Match the OE / cross-reference "
            "number on your current filter — DA8137, P614556, P625128, RS5287, AF4197, LAF4556 or WA10149 — "
            "and confirm it suits your air-cleaner housing before ordering. If your number is on the list, "
            "it is designed to fit.<br/><br/>"

            "<b>Q.</b> Is this an OEM part?<br/>"
            "<b>A.</b> No. It is an aftermarket replacement that cross-references the listed OE numbers. The OE "
            "numbers are shown for reference only.<br/><br/>"

            "<b>Q.</b> What is a radial-seal filter?<br/>"
            "<b>A.</b> The seal is a rubber gasket that presses against the inside of the air-cleaner housing "
            "as the filter slides in, helping stop unfiltered air from bypassing the media — no clamps or "
            "wing-nuts required.<br/><br/>"

            "<b>Q.</b> What is it made of?<br/>"
            "<b>A.</b> Pleated paper / cellulose filter media with a molded rubber gasket and rigid end caps, "
            "built for heavy-duty truck and equipment air intake.<br/><br/>"

            "<b>Q.</b> How often should I change it?<br/>"
            "<b>A.</b> Inspect at every service and fit a new one at the interval in your maintenance schedule, "
            "or sooner in dusty or off-road conditions. A clean air filter helps protect the engine and "
            "supports fuel efficiency."
        ),
        visual="Vertical Q/A table, RH-green divider lines between questions, small RH-blue Q. and A. labels. Clean technical layout, plenty of whitespace.",
        alt="Premium A+ Q&A module answering fitment, OEM status, radial-seal design, materials and replacement interval for the RH Filters air filter.",
    ),
    AIModule(
        name="Module 4 — Banner: Radial seal vs loose fit",
        role="a+_banner",
        headline="A SEAL THAT HELPS KEEP DUST OUT.",
        body=(
            "Dust that bypasses a poorly-sealed filter goes straight into the engine. The radial-seal gasket "
            "on this filter presses against the inside of the air-cleaner housing as it seats, helping stop "
            "unfiltered air from sneaking around the media — so the pleated cellulose can do its job and the "
            "turbo and cylinders stay protected."
        ),
        visual="Wide banner with a clean cutaway diagram: the radial-seal gasket pressing against a stylized housing wall, an arrow showing filtered air flowing through the media and a blocked path showing dust stopped at the seal. RH blue + green only, engineering-diagram styling.",
        alt="A+ banner diagram showing how the RH Filters radial-seal gasket helps prevent dust bypass in the air-cleaner housing.",
    ),
    AIModule(
        name="Module 5 — Banner: Built for the working truck",
        role="a+_banner",
        headline="BUILT FOR THE WORKING TRUCK.",
        body=(
            "Long-haul, regional or off-road, the air intake takes a beating. Rigid end caps hold the pleats "
            "square under high airflow and vibration, and the high-efficiency cellulose media keeps dust, dirt "
            "and airborne grit out of the engine. Change it on schedule and it supports cleaner running, lower "
            "maintenance and engine longevity over the life of the truck."
        ),
        visual="Triptych banner: LEFT — engine-bay air-cleaner housing with the filter seated (gloved hand, no face). CENTER — extreme macro of the pleated media. RIGHT — heavy-duty truck on the highway, soft focus, unbranded. Cool industrial light with warm fill; RH blue + green accents.",
        alt="Triptych A+ banner showing the RH Filters air filter installed in a housing, a media close-up, and a heavy-duty truck on the highway.",
    ),
    AIModule(
        name="Module 6 — Comparison: This filter vs a worn / unsealed filter",
        role="a+_comparison",
        headline="FRESH RADIAL-SEAL FILTER VS A WORN ONE",
        body=(
            "Compare across 3 columns: <b>RH Filters radial-seal air filter (this product)</b> · "
            "A clogged / overdue air filter · A loose or poorly-sealed filter.<br/><br/>"
            "Rows: Airflow to the engine (full vs restricted) · Dust bypass risk (low — radial seal vs high) · "
            "Media condition (clean pleated cellulose vs loaded) · Fit confirmation (OE cross-reference vs "
            "guesswork) · Effect on maintenance (supports longevity vs added engine wear) · Service effort "
            "(drops in by hand).<br/><br/>"
            "Highlight the RH Filters column with a soft RH-green tint. Competitor columns are condition "
            "descriptors only — no brand names."
        ),
        visual="Standard Amazon Premium Comparison Chart, 3 columns, RH-blue header row, RH-green tint on the RH Filters column. Small check / caution icons per cell. No brand names in the comparison columns.",
        alt="Premium comparison chart for the RH Filters radial-seal air filter versus a clogged filter and a poorly-sealed filter across airflow, dust bypass, fit and maintenance.",
    ),
    AIModule(
        name="Module 7 — Carousel (5 tiles): The RH Filters range",
        role="a+_carousel",
        headline="THE RH FILTERS RANGE",
        body=(
            "Tile 1: <b>ENGINE AIR FILTER (this product)</b> — Radial-seal primary air filter for heavy-duty intake.<br/>"
            "Tile 2: <b>OIL FILTERS</b> — Spin-on &amp; cartridge oil filters for heavy-duty engines.<br/>"
            "Tile 3: <b>FUEL FILTERS &amp; WATER SEPARATORS</b> — Keep water and grit out of the fuel system.<br/>"
            "Tile 4: <b>CABIN AIR FILTERS</b> — Cleaner air in the cab for the driver.<br/>"
            "Tile 5: <b>AIR-DRYER FILTERS &amp; KITS</b> — Air-brake system filtration and complete service kits.<br/>"
            "<i>Confirm each SKU against your OE cross-reference number before ordering.</i>"
        ),
        visual="5 identical-composition product tiles, RH blue + green accent corner on each, consistent heavy-duty filter photography across the range. Category label on each tile.",
        alt="Five-tile A+ carousel of the RH Filters range: engine air filters, oil filters, fuel filters and water separators, cabin air filters, and air-dryer filters and kits.",
    ),
]


QA = [
    AIQA(q="How do I confirm this air filter fits my truck?",
         a="Match the OE / cross-reference number on your current filter against this list: DA8137, P614556, P625128, RS5287, AF4197, LAF4556, WA10149. Also confirm it suits your air-cleaner housing. If your number is on the list, this aftermarket replacement is designed to fit."),
    AIQA(q="Is this an OEM part?",
         a="No. This is an aftermarket replacement primary air filter that cross-references the listed OE numbers. The OE numbers are provided for reference only."),
    AIQA(q="What does radial-seal mean and why does it matter?",
         a="A radial seal uses a rubber gasket that presses against the inside of the air-cleaner housing as the filter slides in. It helps stop unfiltered air from bypassing the media, and it installs without clamps or wing-nuts."),
    AIQA(q="What is the filter made of?",
         a="Pleated paper / cellulose filter media with a molded rubber gasket and rigid end caps, built for heavy-duty truck and equipment air-intake systems."),
    AIQA(q="Will this fit my specific engine or housing?",
         a="Fitment is determined by the OE cross-reference number and the air-cleaner housing, not by the engine alone. Measure your existing filter and confirm the cross-reference number before ordering to avoid a size or housing mismatch."),
    AIQA(q="How often should I change the air filter?",
         a="Inspect it at every service and fit a new one at the interval in your maintenance schedule, or sooner in dusty or off-road conditions. A clean air filter helps protect the engine and supports fuel efficiency."),
    AIQA(q="Is it easy to install?",
         a="Yes. As a radial-seal filter it seats by hand inside the air-cleaner housing — no special tools and no clamps to over-torque. It drops in as a routine-maintenance replacement."),
]


# Backend KWs — stem-deduped, byte-packed. Avoid brand words already in the title and superlatives.
# Mix heavy-duty truck terms + OE numbers + relevant generic air-filter search terms from the axis.
BACKEND = (
    "heavy duty engine air filter truck primary radial seal cross reference replacement aftermarket "
    "diesel semi air intake cleaner housing pleated cellulose media gasket high efficiency dust "
    "owner operator fleet maintenance da8137 p614556 p625128 rs5287 af4197 laf4556 wa10149 "
    "equipment off road filtro de aire camion motor"
)


def main() -> None:
    print("Loading Royal Holding USA customer + parsing RH Filters air-filter Excel…")
    cust = load_customer("royal_holding_usa")
    brief = parse_excel(EXCEL)
    OUT = HERE / f"{PLAN_NO}_{ASIN}_Image Plan.pdf"
    print(f"  Product: {brief.product_name}")
    print(f"  ASIN (forced): {ASIN}  (parsed brief.asin={brief.asin!r} — malformed, ignored)")
    print(f"  Marketplace: {cust.marketplace}")
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
