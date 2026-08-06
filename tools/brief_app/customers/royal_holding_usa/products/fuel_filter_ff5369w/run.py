"""RH Filters FF5369W Diesel Fuel Filter / Water Separator — Amazon image plan.
Hand-written KW-led copy injected into the branded ReportLab pipeline.

Brand: Royal Holding USA / RH Filters (aftermarket heavy-duty truck filtration).
Marketplace: amazon.com (US). Overlay language: EN.

Compliance baseline (AFTERMARKET part):
  - Say "aftermarket replacement, replaces OE# …" — NEVER imply OEM-made.
  - NO "universal fit". NO "best / #1 / ultimate / guaranteed". No unverified mpg/performance claims.
  - Customer-facing copy: NO "$", NO URL / ".com" / external link.

Data note: the listing's ASIN field is corrupted ("amazon.com/dp/B0CS3V27TK").
DO NOT use brief.asin — the clean ASIN B0CS3V27TK is hard-coded below (internal only,
never printed into customer-facing copy).
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
PLAN_NO = "03"   # SEO listing no. -> output named 0X_<ASIN>_Image Plan.pdf
ASIN = "B0CS3V27TK"   # clean ASIN — do NOT use brief.asin (it is a URL in the listing)


# ===== KW-led copy — aftermarket-compliant, fitment-led =====

# Title is HTML-escaped on render, so "&" is a literal single char here (count "&" = 1).
TITLE = (
    "RH Filters FF5369W Diesel Fuel Filter & Water Separator, 20 Micron — Aftermarket "
    "Replacement for Freightliner & Kenworth Trucks, DD13 DD15 DD16 X15 ISX15 — OE# PF7620 "
    "P550414 33451 533651XE & More"
)

BULLETS = [
    "<b>EXACT FITMENT &amp; OE CROSS-REFERENCE</b> — Aftermarket replacement fuel filter / water separator "
    "cross-referenced to 11 OE numbers: PF7620, PF7621, PF7680, PF7744, P550414, P550463, P550757, P550969, "
    "33451, 33651 &amp; 533651XE. Match your current part number before ordering and you get a confident, drop-in fit — "
    "no guesswork, no returns.",

    "<b>BUILT FOR FREIGHTLINER &amp; KENWORTH DIESEL</b> — Designed for Freightliner &amp; Kenworth heavy-duty "
    "applications running Detroit DD13, DD15 &amp; DD16 or Cummins X15 &amp; ISX15 engines. Verify your vehicle "
    "and engine compatibility against the listed OE numbers above, then service with confidence.",

    "<b>20-MICRON FUEL &amp; WATER SEPARATION</b> — Rated to 20 microns to trap fine contaminants and separate "
    "water from diesel before it reaches your injectors and high-pressure fuel system. Cleaner fuel helps protect "
    "expensive downstream components over routine service intervals.",

    "<b>CARTRIDGE-STYLE, READY TO INSTALL</b> — Cartridge-style FF5369W with gasket / integrated sealing support, "
    "supplied for a straightforward, routine replacement. A standard maintenance-cycle part for owner-operators, "
    "fleets &amp; diesel mechanics who want the job done right the first time.",

    "<b>AFTERMARKET VALUE — TOP QUALITY, FAIR PRICE</b> — RH Filters by Royal Holding USA delivers dependable "
    "heavy-duty filtration at a fair aftermarket price versus OEM-counter cost. Keep one on the shelf so your "
    "truck is never down waiting on a fuel filter.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="Clean white canvas with a subtle blue (#14488F) tint along the bottom 12% for grounding. Same background across all 3 options so the split test isolates composition, not light/colour.",
        purpose="Win the click in a fuel-filter search grid full of look-alike cartridges. Answer the buyer's first question — 'WILL THIS FIT MY TRUCK?' — before they even open the listing.",
        visual=(
            "Brief the designer to mock ALL 3 options below. Brand picks the winner via Amazon Manage Your "
            "Experiments. Each option uses ONE callout, ONE action cue, ONE supporting prop — clean, not stacked.\n\n"

            "▸ OPTION A — FITMENT-PROOF HERO (owns the #1 buyer question)\n"
            "Center: the FF5369W cartridge filter, large and sharp, vertical, label readable, slight 3/4 turn. "
            "Filter occupies ~70% of frame.\n"
            "ONE CALLOUT — top-right corner badge (RH blue #14488F, white text): "
            "'REPLACES OE#: PF7620 · PF7621 · P550414 · P550463 · 33451 · 533651XE & MORE'.\n"
            "ONE PROP: a small green '20 MICRON' chip lower-left.\n"
            "Why it wins: owner-operators scan for their OE number first. Leading with the cross-reference badge "
            "answers 'will it fit?' on the thumbnail.\n\n"

            "▸ OPTION B — MAKE + ENGINE BADGE (owns the application)\n"
            "Center: FF5369W filter, label readable, slightly left of center.\n"
            "ONE CALLOUT — top-left badge (RH green #2E9E4B): 'FOR FREIGHTLINER & KENWORTH · DD13/DD15/DD16 · "
            "X15 / ISX15'.\n"
            "ONE ACTION CUE: a soft-focus Freightliner/Kenworth grille silhouette behind the filter.\n"
            "Why it wins: buyers who shop by truck make/engine instantly see their rig named — strong relevance "
            "signal in a generic grid.\n\n"

            "▸ OPTION C — 20-MICRON SPEC HERO (owns the filtration spec)\n"
            "Center: FF5369W filter. Floating to its right: a clean cutaway sliver showing pleated media + a "
            "water-droplet separating to the bottom of a bowl.\n"
            "ONE CALLOUT — bottom-right badge (RH blue): '20-MICRON FUEL & WATER SEPARATION'.\n"
            "Why it wins: after fitment, micron rating + water separation is the next decision filter. The cutaway "
            "proves function, not just form.\n\n"

            "Across all 3: filter dominant ~70%, callout ~6% of frame, one prop fills the remainder. Same lighting, "
            "same background gradient, same colour temperature so the A/B test stays clean. Aftermarket compliance: "
            "badges say 'REPLACES OE#…' — never 'OEM'."
        ),
        overlay="(one callout per option — see visual direction)",
        overlay_sub="3 hero options shipped — A/B test, keep the winner",
        props=[
            "OPTION A: FF5369W filter + OE cross-reference badge + 20-micron chip",
            "OPTION B: FF5369W filter + make/engine badge + soft truck-grille silhouette",
            "OPTION C: FF5369W filter + media/water cutaway sliver + micron badge",
        ],
        lighting="Hard technical product light: crisp top key (5000K) with fill from camera-right, a tight spec highlight down the can so the filter reads sharp and premium. Identical across all 3 options.",
        why_it_works=(
            "Diesel buyers decide on fitment first, spec second. Each hero attacks a different decision filter — OE "
            "cross-reference (A), truck make/engine (B), micron + water separation (C) — so the brand can measure "
            "which trigger converts and keep the winner. One callout, one prop, mobile-thumbnail legible."
        ),
        ctr="OE cross-reference badge on the thumbnail captures every buyer searching by their existing part number.",
        cvr="Naming the exact OE numbers, makes and engines on the hero removes fitment doubt before the click.",
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: Will this fit my truck? (fitment chart)",
        role="hook",
        background="RH mood blue #EAF1F8 — technical, clean, not consumer-glossy",
        purpose="Defuse the #1 return driver (wrong-part / fitment confusion) up front with a scannable fitment chart.",
        visual=(
            "Top headline (RH blue, sentence case): 'Check your fit in 10 seconds.'\n\n"
            "LEFT 35%: the FF5369W filter, upright, label readable.\n\n"
            "RIGHT 65%: a clean two-block fitment chart.\n"
            "  BLOCK 1 — 'COMPATIBLE MAKES': Freightliner · Kenworth.\n"
            "  BLOCK 2 — 'COMPATIBLE ENGINES': Detroit DD13 · DD15 · DD16 · Cummins X15 · ISX15.\n"
            "  BLOCK 3 — 'REPLACES OE#': PF7620 · PF7621 · PF7680 · PF7744 · P550414 · P550463 · P550757 · "
            "P550969 · 33451 · 33651 · 533651XE.\n\n"
            "Footer strip (RH green): 'Aftermarket replacement — match your OE number and engine before ordering.'"
        ),
        overlay="WILL IT FIT? CHECK YOUR OE NUMBER.",
        overlay_sub="Freightliner &amp; Kenworth · DD13/DD15/DD16 · X15 / ISX15 — replaces 11 OE numbers.",
        props=["FF5369W filter", "3-block fitment chart (makes / engines / OE numbers)", "green compliance footer strip"],
        lighting="Flat clean studio. This is an information tile — readability beats mood. Numbers legible at thumbnail size.",
        why_it_works=(
            "Reviews flag wrong-part/fitment confusion as the top friction. A full OE + make + engine chart in the "
            "second slot turns that anxiety into a fast self-check, cutting returns and building purchase confidence."
        ),
        ctr="'WILL IT FIT?' is the exact question in the buyer's head — it pulls the open.",
        cvr="A complete, verifiable fitment chart converts the hesitant buyer who needs to confirm before paying.",
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: 20-micron fuel & water separation (cutaway)",
        role="educate",
        background="White with a soft RH-blue ribbon footer",
        purpose="Prove the filter actually works — show media quality + water separation. Earn trust on filtration spec.",
        visual=(
            "Center: a clean technical CUTAWAY of the FF5369W. Show three labeled callouts:\n"
            "  1. 'PLEATED MEDIA — 20-MICRON RATING' (arrow to the folded filter media).\n"
            "  2. 'WATER SEPARATION' (arrow to water droplets coalescing and dropping to the bowl/base).\n"
            "  3. 'INTEGRATED GASKET / SEAL' (arrow to the sealing surface).\n\n"
            "Right side: a simple 2-step flow diagram — 'DIRTY DIESEL + WATER  →  [FF5369W]  →  CLEAN, "
            "WATER-SEPARATED FUEL' with a small droplet icon dropping out below the filter.\n\n"
            "Footer ribbon (RH blue): 'Cleaner fuel helps protect injectors and the high-pressure fuel system "
            "over routine service intervals.'"
        ),
        overlay="20 MICRONS. FUEL IN, WATER OUT.",
        overlay_sub="Pleated media traps fine contaminants &amp; separates water before it reaches your injectors.",
        props=["FF5369W cutaway with 3 labeled callouts", "2-step fuel-flow diagram", "water-droplet icon", "blue footer ribbon"],
        lighting="Flat clean studio with a slight macro highlight on the pleated media so the filtration surface reads as quality.",
        why_it_works=(
            "Quality and filtration spec are the second decision after fitment. A cutaway is the most credible way "
            "to show 20-micron media and water separation — it answers 'is it any good?' with proof, not adjectives. "
            "Claim is spec-bound (20 micron, water separation) — no unverified performance numbers."
        ),
        ctr="A cutaway stands out against flat product-on-white competitor tiles in the strip.",
        cvr="Showing media quality + water separation justifies choosing this filter over the cheapest look-alike.",
    ),
    AIImagePlanItem(
        name="Image 4 — In-context: engine-bay service moment",
        role="desire",
        background="Real heavy-duty diesel engine bay / service garage, cool industrial light",
        purpose="Place the part in the buyer's world — a mechanic mid-service on a Freightliner/Kenworth. Build install confidence.",
        visual=(
            "Three-quarter shot inside a semi engine bay. A mechanic's gloved hands (no face needed) seating the "
            "FF5369W fuel filter into the housing, wrench resting on the frame rail. The filter is the sharp "
            "focal point; the engine bay is softly de-focused behind it.\n\n"
            "FOREGROUND lower-right: the FF5369W in its packaging, label readable, next to the clean new filter.\n\n"
            "Small corner chip (RH green): 'ROUTINE SERVICE-INTERVAL PART'. Industrial, honest — diesel garage, "
            "not a studio.\n\n"
            "Model/asset note: use stock or brand-supplied engine-bay photography; avoid competitor brand logos "
            "and readable competitor part numbers in frame."
        ),
        overlay="DROP-IN SERVICE FOR YOUR DIESEL.",
        overlay_sub="Cartridge-style with integrated sealing — a straightforward routine replacement.",
        props=["FF5369W new filter", "FF5369W packaging", "mechanic gloved hands", "wrench", "diesel engine bay (soft focus)"],
        lighting="Cool industrial garage light with a directional highlight on the filter so it stays the hero. Honest service-bay feel, not staged glamour.",
        why_it_works=(
            "Owner-operators and mechanics want to picture the swap before buying. An engine-bay service moment "
            "answers 'can I install this easily?' and signals this is a real heavy-duty part, not a marine/consumer "
            "look-alike. Strongest in-context conversion image in the plan."
        ),
        ctr="A real engine-bay scene reads instantly as 'heavy-duty truck part' — the right-audience signal.",
        cvr="Seeing the actual install + 'routine service part' chip removes install hesitation before checkout.",
    ),
    AIImagePlanItem(
        name="Image 5 — Trust: aftermarket value + quality credentials",
        role="trust",
        background="White with soft RH-blue panels behind each badge for separation",
        purpose="Stack the filters diesel buyers scan for: correct fit, filtration spec, aftermarket value, RH brand. Defuse 'is this any good?'.",
        visual=(
            "Center: the FF5369W filter, label facing camera. Four trust badges in the corners:\n\n"
            "  • TOP-LEFT — 'EXACT-FIT CROSS-REFERENCE' (small checklist icon + 'Replaces 11 OE numbers').\n"
            "  • TOP-RIGHT — '20-MICRON FILTRATION' (small filter-media icon).\n"
            "  • BOTTOM-LEFT — 'FUEL / WATER SEPARATION' (small droplet icon).\n"
            "  • BOTTOM-RIGHT — 'AFTERMARKET VALUE' (small price-tag icon — NO currency symbol or number).\n\n"
            "Below the filter, a thin strip: 'RH Filters by Royal Holding USA — aftermarket heavy-duty truck "
            "filtration. Top quality. Fair price.'"
        ),
        overlay="EXACT FIT. PROVEN FILTRATION. FAIR VALUE.",
        overlay_sub="Aftermarket replacement — replaces 11 OE numbers · 20-micron · fuel/water separation.",
        props=["FF5369W filter (center)", "4 corner badge graphics", "RH brand strip"],
        lighting="Studio even light, hard catch-light on the filter, badges legible at thumbnail size.",
        why_it_works=(
            "Stacks the four filters that matter to a diesel buyer — fitment, micron spec, water separation, value — "
            "in one frame, anchored to the RH brand and tagline. 'Aftermarket value' badge carries no '$' or number, "
            "staying compliant while still owning the price-value motivator from the reviews."
        ),
        ctr="Four scannable proof badges read as 'serious technical brand' at a glance.",
        cvr="The credential stack closes the 'cheap-and-risky vs trustworthy' debate in the buyer's mind.",
    ),
    AIImagePlanItem(
        name="Image 6 — OE replacement checklist (full cross-reference)",
        role="desire",
        background="RH mood blue #EAF1F8 — same as Image 2 for visual rhythm",
        purpose="Remove every last fitment doubt with the complete OE replacement list as a checklist. The page buyers screenshot.",
        visual=(
            "Split-frame.\n\n"
            "LEFT 40%: the FF5369W filter, upright, label readable, with a green check-mark badge.\n\n"
            "RIGHT 60%: a two-column 'REPLACES OE# / REFERENCE #' checklist, each with a small green tick:\n"
            "  ✓ PF7620   ✓ PF7621   ✓ PF7680   ✓ PF7744\n"
            "  ✓ P550414  ✓ P550463  ✓ P550757  ✓ P550969\n"
            "  ✓ 33451    ✓ 33651    ✓ 533651XE\n\n"
            "Below: a caption — 'Find any of these numbers on your current filter? The FF5369W is your aftermarket "
            "replacement. Always confirm against your vehicle and engine.'"
        ),
        overlay="REPLACES 11 OE NUMBERS.",
        overlay_sub="PF7620 · PF7621 · PF7680 · PF7744 · P550414 · P550463 · P550757 · P550969 · 33451 · 33651 · 533651XE",
        props=["FF5369W filter + green check badge", "two-column OE checklist with ticks", "confirm-fitment caption"],
        lighting="Even soft front-light, clean infographic feel.",
        why_it_works=(
            "The complete, tick-marked OE list is the single most reassuring asset for a parts buyer — it lets them "
            "match their existing number in seconds and is the image they screenshot to confirm before ordering. "
            "Directly attacks the wrong-part return risk flagged in review analysis."
        ),
        ctr="'REPLACES 11 OE NUMBERS' is a hard, specific promise that out-specifies vague competitor tiles.",
        cvr="A full checklist lets the buyer self-verify fit — the last step before adding to cart.",
    ),
    AIImagePlanItem(
        name="Image 7 — Brand close: RH Filters fleet & shelf",
        role="close",
        background="Industrial — semi truck on the highway / shop shelf, RH blue + green accents",
        purpose="Close on brand identity and the 'keep one on the shelf' behaviour for fleets and owner-operators.",
        visual=(
            "Mid-range environmental shot. RIGHT side: the FF5369W in RH packaging on a clean shop shelf, label "
            "readable. LEFT / background: a soft-focus Freightliner or Kenworth semi on the highway through the "
            "open shop door (or a fleet lineup), conveying 'keeps your trucks running.'\n\n"
            "Lower band (RH blue): RH Filters logo + tagline 'Top quality. Fair price.' Small line: 'Aftermarket "
            "heavy-duty truck filtration — air, oil, fuel, cabin & water separators.'\n\n"
            "Industrial, trustworthy — semi-truck context, not consumer lifestyle. Avoid competitor logos."
        ),
        overlay="KEEP YOUR FLEET RUNNING.",
        overlay_sub="RH Filters by Royal Holding USA — aftermarket heavy-duty filtration. Top quality. Fair price.",
        props=["FF5369W in RH packaging", "shop shelf", "soft-focus Freightliner/Kenworth semi (highway)", "RH logo + tagline band"],
        lighting="Warm-cool industrial mix — directional light on the boxed filter, atmospheric haze on the highway truck behind. Honest, working-shop feel.",
        why_it_works=(
            "Closes on the brand promise a fleet buyer needs before checkout: dependable filtration that keeps "
            "trucks earning, at a fair aftermarket price, from a real US filtration supplier. The shelf framing "
            "nudges multi-unit / keep-a-spare purchases."
        ),
        ctr="The on-the-road semi signals 'this is the filter that keeps you driving' — emotional pull for operators.",
        cvr="Brand + tagline + range cross-sell builds the repeat-buyer relationship and stock-up purchase.",
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Brand banner: Aftermarket filtration that fits.",
        role="a+_banner",
        headline="AFTERMARKET FILTRATION THAT FITS.",
        body=(
            "RH Filters by Royal Holding USA builds dependable aftermarket replacement filters for heavy-duty "
            "diesel trucks. The FF5369W fuel filter / water separator is engineered for exact fitment, 20-micron "
            "filtration and a fair price — so your Freightliner or Kenworth stays on the road, not in the shop."
        ),
        visual="Wide cinematic banner: the FF5369W filter front-center on an industrial surface, a soft-focus Freightliner/Kenworth semi and engine bay behind it. RH blue logo upper-left, tagline 'Top quality. Fair price.' in the lower band.",
        alt="RH Filters FF5369W diesel fuel filter and water separator on an industrial bench with a heavy-duty truck in soft focus behind it.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): Why the FF5369W",
        role="a+_carousel",
        headline="WHY THE FF5369W",
        body=(
            "Tile 1: <b>EXACT FITMENT</b> — Replaces 11 OE numbers: PF7620 · P550414 · 33451 · 533651XE &amp; more.<br/>"
            "Tile 2: <b>FREIGHTLINER &amp; KENWORTH</b> — DD13 / DD15 / DD16 · X15 / ISX15 diesel applications.<br/>"
            "Tile 3: <b>20-MICRON RATING</b> — Traps fine contaminants &amp; separates water from diesel.<br/>"
            "Tile 4: <b>CARTRIDGE-STYLE</b> — Integrated gasket / sealing support, ready for routine service.<br/>"
            "Tile 5: <b>AFTERMARKET VALUE</b> — Top quality at a fair price versus OEM-counter cost."
        ),
        visual="5 square tiles, RH blue accent corner on each, consistent composition. Small icons (OE-checklist · truck · filter-media · cartridge · price-tag without currency).",
        alt="Five-tile A+ carousel of FF5369W differentiators: exact fitment, Freightliner and Kenworth fit, 20-micron rating, cartridge style, aftermarket value.",
    ),
    AIModule(
        name="Module 3 — Banner: How it protects your fuel system",
        role="a+_banner",
        headline="20 MICRONS BETWEEN YOUR FUEL AND YOUR INJECTORS.",
        body=(
            "Diesel fuel carries water and fine particulate that wear injectors and high-pressure pumps. The "
            "FF5369W uses pleated 20-micron media to trap contaminants and separate water before it reaches your "
            "fuel system, helping protect expensive downstream components over routine service intervals."
        ),
        visual="Wide banner: clean technical cutaway of the FF5369W with labeled callouts (pleated 20-micron media, water separation to the bowl, integrated seal) and a left-to-right 'dirty diesel + water → filter → clean fuel' flow. RH blue + green palette only.",
        alt="A+ banner showing the FF5369W cutaway: 20-micron pleated media and water separation protecting the diesel fuel system.",
    ),
    AIModule(
        name="Module 4 — Use cases triptych: shop, fleet, on the road",
        role="a+_banner",
        headline="FOR OWNER-OPERATORS, FLEETS & MECHANICS.",
        body=(
            "LEFT — the mechanic: a clean drop-in cartridge for fast, confident routine service. "
            "CENTER — the fleet: a fair-price part worth stocking so trucks are never down waiting on a fuel filter. "
            "RIGHT — the owner-operator: cleaner, water-separated fuel that helps keep you earning miles."
        ),
        visual="Triptych within one banner: LEFT — gloved hands seating the FF5369W in an engine bay. CENTER — a row of boxed FF5369W filters on a fleet shop shelf. RIGHT — a Freightliner/Kenworth semi on the highway. Cool industrial light across all three panels.",
        alt="Triptych A+ banner showing the FF5369W in engine-bay service, on a fleet shelf, and a heavy-duty truck on the highway.",
    ),
    AIModule(
        name="Module 5 — Carousel (5 tiles): The RH Filters range",
        role="a+_carousel",
        headline="THE RH FILTERS RANGE",
        body=(
            "Tile 1: <b>FUEL FILTER / WATER SEPARATOR (this product)</b> — FF5369W, 20-micron, Freightliner &amp; "
            "Kenworth diesel.<br/>"
            "Tile 2: <b>OIL FILTERS</b> — Heavy-duty engine oil filtration for diesel trucks.<br/>"
            "Tile 3: <b>ENGINE AIR FILTERS</b> — Protect intake against road dust and debris.<br/>"
            "Tile 4: <b>CABIN AIR FILTERS</b> — Cleaner cab air for long-haul comfort.<br/>"
            "Tile 5: <b>FILTER KITS &amp; WATER SEPARATORS</b> — Complete service kits to do the job in one stop.<br/>"
            "<i>Range confirmed on the Royal Holding USA brand site — pull current product photography from brand assets.</i>"
        ),
        visual="5 identical-composition product tiles, RH blue + green accent corner on each. Consistent filter / packaging photography across the range.",
        alt="Five-tile A+ carousel of the RH Filters range: fuel/water separator, oil filters, engine air filters, cabin air filters, and filter kits.",
    ),
    AIModule(
        name="Module 6 — Premium Q&A",
        role="a+_qa",
        headline="QUESTIONS DIESEL BUYERS ASK",
        body=(
            "<b>Q.</b> Will the FF5369W fit my truck?<br/>"
            "<b>A.</b> It is an aftermarket replacement for Freightliner &amp; Kenworth diesel applications running "
            "Detroit DD13/DD15/DD16 or Cummins X15/ISX15. It is cross-referenced to 11 OE numbers: PF7620, PF7621, PF7680, PF7744, "
            "P550414, P550463, P550757, P550969, 33451, 33651 &amp; 533651XE. Match your current part number and "
            "confirm your vehicle/engine before ordering.<br/><br/>"

            "<b>Q.</b> Is this an OEM part?<br/>"
            "<b>A.</b> No. It is an aftermarket replacement cross-referenced to the listed OE numbers. It is designed to "
            "fit the same applications at a fair aftermarket price.<br/><br/>"

            "<b>Q.</b> What is the micron rating?<br/>"
            "<b>A.</b> 20 microns. The pleated media traps fine contaminants and separates water from diesel before "
            "it reaches your injectors and high-pressure fuel system.<br/><br/>"

            "<b>Q.</b> Is it a fuel filter or a water separator?<br/>"
            "<b>A.</b> Both. The FF5369W is a diesel fuel filter with water-separation function in a single "
            "cartridge-style unit.<br/><br/>"

            "<b>Q.</b> Is it easy to install?<br/>"
            "<b>A.</b> It is a cartridge-style filter with integrated gasket / sealing support for a standard, "
            "routine replacement. Follow your engine manufacturer's service procedure and torque spec.<br/><br/>"

            "<b>Q.</b> How often should it be changed?<br/>"
            "<b>A.</b> Change it as part of your normal diesel fuel-filter service interval, or sooner if you "
            "notice reduced fuel flow or water in the fuel. Follow your maintenance schedule."
        ),
        visual="Vertical Q/A table. RH green divider lines between each Q. Small RH blue Q. and A. labels.",
        alt="Premium Q&A module answering the six most-asked diesel-buyer questions about the FF5369W fuel filter / water separator.",
    ),
    AIModule(
        name="Module 7 — Premium Comparison Chart",
        role="a+_comparison",
        headline="WHY CHOOSE RH FILTERS",
        body=(
            "Compare across 4 columns: <b>RH Filters FF5369W</b> · Unbranded economy fuel filter · "
            "Generic marine water separator · OEM-counter filter.<br/><br/>"
            "Rows: Exact OE cross-reference (11 numbers) · Freightliner &amp; Kenworth fitment listed · 20-micron "
            "rating · Fuel + water separation · Cartridge-style with integrated seal · Aftermarket value vs "
            "OEM-counter cost.<br/><br/>"
            "Highlight the RH Filters column with a soft RH-blue tint and an 'EXACT-FIT AFTERMARKET' ribbon at "
            "the top of the column. No currency symbols or prices in any cell."
        ),
        visual="Standard Amazon Premium Comparison Chart layout, 4 product columns. Competitor columns use category descriptors only — no brand names or logos. RH blue header row.",
        alt="Premium comparison chart for RH Filters FF5369W vs unbranded economy filter, generic marine separator, and OEM-counter filter.",
    ),
]


QA = [
    AIQA(q="Will the FF5369W fit my truck?",
         a="It is an aftermarket replacement for Freightliner and Kenworth diesel applications running Detroit DD13/DD15/DD16 or Cummins X15/ISX15. It is cross-referenced to 11 OE numbers: PF7620, PF7621, PF7680, PF7744, P550414, P550463, P550757, P550969, 33451, 33651 and 533651XE. Match your current part number and confirm your vehicle and engine before ordering."),
    AIQA(q="Is this an OEM part?",
         a="No. It is an aftermarket replacement cross-referenced to the listed OE numbers. It is designed to fit the same applications at a fair aftermarket price. It is not made by the original equipment manufacturer."),
    AIQA(q="What is the micron rating?",
         a="20 microns. The pleated media traps fine contaminants and separates water from diesel before it reaches your injectors and high-pressure fuel system."),
    AIQA(q="Is it a fuel filter or a water separator?",
         a="Both. The FF5369W is a diesel fuel filter with water-separation function in a single cartridge-style unit."),
    AIQA(q="Which OE / reference numbers does it replace?",
         a="PF7620, PF7621, PF7680, PF7744, P550414, P550463, P550757, P550969, 33451, 33651 and 533651XE. If your current filter shows any of these numbers, the FF5369W is your aftermarket replacement — always confirm against your vehicle and engine."),
    AIQA(q="Is it easy to install?",
         a="It is a cartridge-style filter with integrated gasket / sealing support for a standard, routine replacement. Follow your engine manufacturer's service procedure and torque specification."),
    AIQA(q="How often should it be changed?",
         a="Change it as part of your normal diesel fuel-filter service interval, or sooner if you notice reduced fuel flow or water in the fuel. Follow your vehicle's maintenance schedule."),
]


# Backend KWs — stem-deduped, byte-packed. Avoid: brand/terms already in title, superlatives.
# Long-tail cross-reference + category terms parsed from the listing SEO axis.
BACKEND = (
    "fuel water separator diesel fuel filter water separating heavy duty truck cartridge "
    "freightliner kenworth dd13 dd15 dd16 cummins x15 isx15 detroit 20 micron filtration "
    "pf7620 pf7621 pf7680 pf7744 p550414 p550463 p550757 p550969 33451 33651 533651xe "
    "ff5369w oe cross reference replacement aftermarket owner operator fleet mechanic service kit"
)


def main() -> None:
    print("Loading Royal Holding USA customer + parsing FF5369W Excel…")
    cust = load_customer("royal_holding_usa")
    brief = parse_excel(EXCEL)
    OUT = HERE / f"{PLAN_NO}_{ASIN}_Image Plan.pdf"
    title_len = len(TITLE)
    print(f"  Product: {brief.product_name}")
    print(f"  ASIN (clean, hard-coded): {ASIN}   (listing field was: {brief.asin})")
    print(f"  Marketplace: {cust.marketplace}")
    print(f"  USPs={len(brief.usps)} KWs={len(brief.all_keywords)} reviews=+{len(brief.good_reviews)}/-{len(brief.bad_reviews)}")
    print(f"  TITLE real chars: {title_len} (limit 200)")

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
