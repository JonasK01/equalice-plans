"""RH Filters — Detroit Diesel Fuel Filter Insert Kit (replaces OE# DDE A9360900651)
Hand-written, KW-led, fitment-verified copy injected into the branded ReportLab pipeline.

Marketplace: amazon.com (US)
Brand: RH Filters by Royal Holding USA — aftermarket heavy-duty truck filtration.

AFTERMARKET COMPLIANCE (auto-checked on build):
  - Frame as "aftermarket replacement, replaces OE# DDE A9360900651" — NEVER imply OEM-made.
  - NO "universal fit" — always state exact compatibility (Detroit Diesel DD13/DD15/DD16).
  - NO "best / #1 / ultimate / guaranteed". No unverified performance / mpg claims.
  - In ANY customer-facing copy: NO "$", NO URL / ".com" / external link.

CREATIVE SPINE — buyer questions, in order:
  1. "WILL THIS FIT MY DETROIT DIESEL?"  -> lead with OE# badge + DD13/DD15/DD16 fitment proof
  2. "Is the KIT complete?"             -> show full kit laid out (strain insert + main filter + O-rings)
  3. "Is the quality good?"             -> cutaway / media macro + leak-free / long-mile review proof
Audience = owner-operators, fleets, diesel mechanics. One callout + one action cue + one prop per image.
"""
from __future__ import annotations
import sys
from pathlib import Path

# This script lives at customers/<brand>/products/<product>/run.py
HERE = Path(__file__).resolve().parent          # the product folder (self-contained)
ROOT = HERE.parents[5]                           # project root
sys.path.insert(0, str(ROOT))

from tools.brief_app.core.customers import load_customer
from tools.brief_app.core.excel_parser import parse_excel
from tools.brief_app.core.pdf_builder import BriefBuilder
from tools.brief_app.core.ai import AIImagePlanItem, AIModule, AIQA


# Inputs/outputs live alongside this script — the product folder is self-contained.
EXCEL = HERE / "listing.xlsx"                    # the SEO "axis" for this product
PLAN_NO = "02"   # SEO listing no. -> output named 0X_<ASIN>_Image Plan.pdf
ASIN = "B0CTKSBYYN"


# ===== KW-led, fitment-verified copy — aftermarket compliant =====
# Title is HTML-escaped downstream, so a literal "&" is safe and counts as 1 real char.
TITLE = (
    "RH Filters Detroit Diesel Fuel Filter Insert Kit — Aftermarket Replacement for DDE A9360900651 — "
    "Complete Kit: Strain Filter Insert, Main Filter & O-Rings — Fits Detroit Diesel DD13 DD15 DD16 Trucks"
)

BULLETS = [
    "<b>AFTERMARKET REPLACEMENT FOR OE# DDE A9360900651</b> — Direct-fit diesel fuel filter "
    "insert kit engineered as an aftermarket replacement for OE# DDE A9360900651. Confirm this OE number "
    "against your unit before ordering and you get an exact match — no guesswork, no returns.",

    "<b>FITS DETROIT DIESEL DD13, DD15 &amp; DD16</b> — Built for Detroit Diesel heavy-duty truck "
    "applications, including Freightliner Cascadia chassis. This is a vehicle-specific replacement part, "
    "not a vague one-size-fits-all filter — exact fitment is how you avoid leaks and downtime.",

    "<b>COMPLETE KIT — NOTHING ELSE TO BUY</b> — Every service comes ready: strain filter insert, main "
    "filter, and all required O-rings in one box. No hunting for seals at the parts counter — open the kit, "
    "swap the old set, torque, and you&#39;re back on the road.",

    "<b>CLEAN FUEL, SMOOTHER RUN</b> — Supports reliable diesel fuel filtration to help separate water and "
    "debris before they reach your injectors. Drivers report smoother fuel flow with no more sputtering and "
    "quieter operation after a fresh service — exactly what routine fuel filter maintenance should deliver.",

    "<b>BUILT TO LAST — FAIR PRICE</b> — Machined exterior and durable construction stand up to real "
    "heavy-duty miles, with leak-free installs and long-haul confidence reported well past 25,000 miles. "
    "Top quality at a fair price versus dealer and truck-stop options — stock up and service on schedule.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="Clean white canvas with a soft blue (#EAF1F8) tint across the bottom 15% for grounding. Same background across all 3 options for a clean A/B test.",
        purpose="Win the click in a fuel-filter search grid where every result looks like a generic black canister. Answer the #1 buyer question — 'will this fit my Detroit Diesel?' — before the click.",
        visual=(
            "Brief the designer to mock ALL 3 options below. Brand picks the winner via Amazon Manage Your "
            "Experiments. Each option uses ONE callout, ONE action cue, ONE supporting prop — technical, not stacked.\n\n"

            "▸ OPTION A — FITMENT-PROOF HERO (owns the #1 buyer question)\n"
            "Center: the main filter standing upright, sharp and large (~65% of frame), front-facing so the RH "
            "Filters label reads. Lower-right: the strain filter insert + 2 O-rings staged so the kit reads as "
            "complete.\n"
            "ONE CALLOUT — top-right badge: 'REPLACES OE# DDE A9360900651' (RH blue #14488F background, white "
            "Arial, small green check icon). Thin sub-line under badge: 'Aftermarket replacement'.\n"
            "Why it wins: no competitor puts the exact OE cross-reference number on the thumbnail. A mechanic "
            "scanning the grid for 'A9360900651' sees an instant match.\n\n"

            "▸ OPTION B — COMPLETE-KIT LAYOUT (defuses 'is the kit complete?')\n"
            "Center: full kit laid out flat in a clean technical row on a soft graphite surface — strain filter "
            "insert | main filter | O-ring set — each component lightly labeled in RH blue.\n"
            "ONE CALLOUT — top-left badge: 'COMPLETE KIT · INSERT + FILTER + O-RINGS' (RH green #2E9E4B "
            "background, white Arial).\n"
            "Why it wins: the second buyer hesitation is 'will I be missing a seal mid-service?' This image "
            "proves completeness at a glance — open box, full service.\n\n"

            "▸ OPTION C — ENGINE FITMENT BADGE (owns the application)\n"
            "Center: main filter upright (~60%). Right side: 3 clean engine chips stacked — 'DD13' · 'DD15' · "
            "'DD16' — RH blue outline pills on a white halo. Soft-focus diesel engine bay behind.\n"
            "ONE CALLOUT — bottom-right badge: 'FITS DETROIT DIESEL DD13 / DD15 / DD16' (RH blue, white Arial).\n"
            "Why it wins: owner-operators shop by engine. Naming the exact Detroit Diesel platforms on the "
            "thumbnail captures the 'dd15 fuel filter kit' searcher instantly.\n\n"

            "Across all 3: product dominant ~60-65%, callout ~6% of frame, supporting prop fills remainder. "
            "Same lighting, same background gradient, same color temperature so the split test isolates "
            "composition, not light/color."
        ),
        overlay="(one callout per option — see visual direction)",
        overlay_sub="3 hero options shipped — A/B test, keep the winner",
        props=[
            "OPTION A: main filter + strain insert + 2 O-rings + OE# badge",
            "OPTION B: full kit flat-lay (insert + main filter + O-ring set) + complete-kit badge",
            "OPTION C: main filter + DD13/DD15/DD16 engine chips + soft engine-bay backdrop + fitment badge",
        ],
        lighting="Hard technical key light (5000K) from upper-left with crisp fill to read machined edges and label text. Slight rim on the filter body. Identical lighting across all 3 options to keep the A/B test clean.",
        why_it_works=(
            "Three angles against the three buyer triggers for an aftermarket fuel filter: A wins on the exact "
            "OE cross-reference (fitment), B wins on kit completeness, C wins on engine application. One callout, "
            "one action cue, one prop each — legible on a mobile thumbnail in a crowded filter grid."
        ),
        ctr="Lead with the OE# badge (Option A) — exact-number match is the strongest scroll-stopper for a mechanic searching DDE A9360900651.",
        cvr="Backs the click with completeness + fitment proof so the buyer trusts the match before opening the detail page.",
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: Exact OE Cross-Reference",
        role="hook",
        background="RH mood blue #EAF1F8 — clean technical, not consumer-glossy.",
        purpose="Hammer the single most-searched purchase trigger: the OE number. This is the hook competitors bury in fine print.",
        visual=(
            "Center: macro of the main filter, three-quarter turn, sharp. To its right, a clean 'cross-reference' "
            "panel styled like a parts catalog row:\n\n"
            "  OE# (replaces):  DDE A9360900651\n"
            "  Type:            Diesel fuel filter insert kit\n"
            "  Application:     Detroit Diesel DD13 / DD15 / DD16\n\n"
            "A bold RH-green check sits beside the OE# line. Small disclaimer strip along the bottom in RH blue: "
            "'Aftermarket replacement. Confirm OE# against your unit before ordering.'"
        ),
        overlay="AFTERMARKET REPLACEMENT FOR OE# DDE A9360900651.",
        overlay_sub="Aftermarket diesel fuel filter insert kit for Detroit Diesel DD13 / DD15 / DD16.",
        props=["main filter (macro)", "cross-reference catalog panel", "RH-green check icon", "aftermarket disclaimer strip"],
        lighting="Even technical front-light, slight drop shadow under the filter. Clarity over mood — this is the fitment hook.",
        why_it_works=(
            "Owner-operators and fleet buyers search by part number first. Surfacing 'DDE A9360900651' as the "
            "hook — framed as an aftermarket replacement — answers the make-or-break question and is fully "
            "compliant (no OEM implication, no universal-fit language)."
        ),
        ctr="The OE number as a headline is the exact string the buyer typed into search — instant relevance.",
        cvr="Removes the #1 listing risk (wrong fitment) up front, so the buyer reads on with confidence.",
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: What's in the complete kit",
        role="educate",
        background="White with a soft RH-green ribbon footer.",
        purpose="Prove the kit is complete so the buyer never wonders 'will I be short a seal mid-service?' Defuses the second buyer hesitation.",
        visual=(
            "Three-column exploded layout. Headline top, RH blue, sentence case: 'Everything one service needs.'\n\n"
            "COLUMN 1 — STRAIN FILTER INSERT\n"
            "  • First-stage strainer element\n"
            "  • Catches larger debris before the main filter\n"
            "Small icon: stylized mesh strainer in RH green.\n\n"
            "COLUMN 2 — MAIN FILTER\n"
            "  • Primary diesel fuel filtration media\n"
            "  • Helps separate water and fine debris from fuel\n"
            "Small icon: stylized pleated filter media in RH blue.\n\n"
            "COLUMN 3 — O-RING SET\n"
            "  • All required seals included\n"
            "  • Helps deliver a clean, leak-free install\n"
            "Small icon: stylized O-ring in RH green.\n\n"
            "Footer ribbon (RH green): 'Complete kit — replaces OE# DDE A9360900651. Aftermarket replacement.'"
        ),
        overlay="EVERYTHING ONE SERVICE NEEDS.",
        overlay_sub="Strain filter insert + main filter + all required O-rings — in one box.",
        props=["3-column exploded layout", "3 technical icons (strainer, filter media, O-ring)", "complete-kit footer ribbon"],
        lighting="Flat clean studio. Educational module — readability beats atmosphere.",
        why_it_works=(
            "Spells out exactly what arrives so the mechanic can plan the job and never gets stranded hunting "
            "for a seal. Mirrors the verified kit contents from the listing axis and reinforces the aftermarket "
            "OE-replacement framing."
        ),
        ctr="The word 'complete' plus the component breakdown answers a hesitation many filter listings ignore.",
        cvr="A buyer who can see every part included is far more likely to add to cart without messaging the seller.",
    ),
    AIImagePlanItem(
        name="Image 4 — Quality: Filter-media cutaway macro",
        role="trust",
        background="Dark technical graphite gradient — makes the cut media glow, reads 'engineering'.",
        purpose="Answer 'is the quality good?' with a look inside. Cutaway is the most persuasive quality proof for filtration.",
        visual=(
            "Hero cutaway: the main filter sliced to reveal the pleated filtration media in sharp macro, pleats "
            "fanning cleanly. A single thin RH-blue leader line points to the media with a small label: 'Multi-"
            "pleat diesel fuel media — more surface area for water + debris capture.' Second leader to the "
            "machined housing edge: 'Machined exterior, durable construction.'\n\n"
            "Foreground prop: one O-ring resting at the base to keep the kit context. ONE action cue: a faint "
            "directional fuel-flow arrow through the media."
        ),
        overlay="SEE THE FILTRATION INSIDE.",
        overlay_sub="Multi-pleat media + machined, durable housing — built for heavy-duty diesel miles.",
        props=["cutaway main filter (macro)", "single O-ring", "media + housing leader labels", "subtle fuel-flow arrow"],
        lighting="Dramatic single key from upper-right raking across the pleats to show media depth; soft fill so the housing edge stays sharp.",
        why_it_works=(
            "A cutaway is the single strongest quality signal in filtration — it shows the media a buyer is "
            "actually paying for. Pairs with the verified review theme ('quality vs truck-stop options', 'no "
            "sputtering') without making any unverified performance claim."
        ),
        ctr="A glowing cutaway stands out hard against rows of closed black-canister thumbnails.",
        cvr="Visible media quality justifies the choice over the cheapest option and converts the quality-skeptic.",
    ),
    AIImagePlanItem(
        name="Image 5 — Trust: Verified-fit + leak-free, long-mile proof",
        role="trust",
        background="White with soft RH mood-blue panels behind each badge for separation.",
        purpose="Stack the trust filters a fleet buyer scans for: verified fit, leak-free, long-mile, fair price. Defuses 'is this seller legit?'",
        visual=(
            "Centered macro of the main filter (label facing camera). Four trust badges in the corners:\n\n"
            "  • TOP-LEFT — VERIFIED FITMENT (small check icon + 'Replaces OE# DDE A9360900651')\n"
            "  • TOP-RIGHT — LEAK-FREE INSTALL (small O-ring/seal icon + 'All seals included')\n"
            "  • BOTTOM-LEFT — DETROIT DIESEL DD13 / DD15 / DD16 (small engine icon)\n"
            "  • BOTTOM-RIGHT — TOP QUALITY · FAIR PRICE (small RH shield)\n\n"
            "Below the filter, a thin strip with the supporting line: 'Drivers report smooth fuel flow, no "
            "sputtering, quieter operation and leak-free installs. Aftermarket replacement by RH Filters.'"
        ),
        overlay="VERIFIED FIT. LEAK-FREE. HEAVY-DUTY VALUE.",
        overlay_sub="Aftermarket replacement for OE# DDE A9360900651 · Fits Detroit Diesel DD13 / DD15 / DD16 · All seals included",
        props=["main filter (center)", "4 badge graphics in corners", "thin supporting review strip"],
        lighting="Studio even light, hard catch-light on the filter body. Badges legible at thumbnail size.",
        why_it_works=(
            "Stacks the four filters a fleet or owner-operator checks before buying aftermarket: confirmed fit, "
            "leak-free install, exact engine application, value. Every line is anchored to verified review "
            "themes and the OE cross-reference — no superlatives, no unverified claims."
        ),
        ctr="A four-badge trust grid signals a vetted seller in a category full of unbranded listings.",
        cvr="Leak-free + long-mile proof is exactly the reassurance that closes a cautious diesel-service buyer.",
    ),
    AIImagePlanItem(
        name="Image 6 — In-context: Engine-bay service moment",
        role="desire",
        background="Real heavy-duty diesel engine bay, garage work light from camera-right.",
        purpose="Put the kit where it lives. Make the buyer picture the easy, leak-free service the reviews describe.",
        visual=(
            "Wide angled shot inside a Detroit Diesel engine bay. A mechanic's gloved hands (no face) seating "
            "the new main filter into the fuel filter housing — mid-action, clearly a clean swap. The rest of "
            "the kit (strain insert + O-rings) staged on a shop towel on the fender, ready.\n\n"
            "FOREGROUND right edge: the RH Filters box / main filter, label readable. Soft-focus engine, hoses "
            "and the DD valve cover behind. Honest garage light, not studio gloss.\n\n"
            "ONE action cue: hands seating the filter. ONE prop: the staged kit on the towel."
        ),
        overlay="A CLEAN SWAP IN THE BAY.",
        overlay_sub="Open the kit, seat the filter, fit the seals — back on the road. Aftermarket replacement for OE# DDE A9360900651.",
        props=["gloved mechanic hands (no face)", "main filter going into housing", "strain insert + O-rings on shop towel", "RH Filters box", "soft-focus Detroit Diesel engine bay"],
        lighting="Directional garage work-light from camera-right, slight rim on the filter, honest industrial tone — engine-bay real, not staged.",
        why_it_works=(
            "Owner-operators and mechanics convert on 'this is exactly the job I'm about to do.' The in-bay swap "
            "with the full kit staged reinforces completeness and the verified 'easy install / leak-free' review "
            "theme, with the OE# kept in frame for fitment."
        ),
        ctr="A real engine-bay swap reads instantly as the buyer's own maintenance task.",
        cvr="Showing the easy, complete service lowers install anxiety and pushes the add-to-cart.",
    ),
    AIImagePlanItem(
        name="Image 7 — Brand close: RH Filters, top quality fair price",
        role="close",
        background="Clean white-to-blue (#EAF1F8) gradient, semi-truck-on-highway soft-focus upper band.",
        purpose="Close on brand value and stock-up logic — fleets and owner-operators service on schedule.",
        visual=(
            "Mid-range product portrait: the complete kit grouped cleanly — main filter front, strain insert "
            "and O-rings beside it — on a white surface, RH Filters label sharp. Upper band: a soft-focus "
            "Freightliner-style semi on the highway (no competitor logos), grounding the heavy-duty fleet use.\n\n"
            "Lower-left: a small RH Filters shield lockup with the tagline 'Top quality. Fair price.' Thin "
            "strip: 'Aftermarket replacement — replaces OE# DDE A9360900651 — RH Filters by Royal Holding USA, "
            "Bensenville, IL.'\n\n"
            "ONE callout: the tagline lockup. ONE prop: the complete kit. ONE cue: highway context for fleet use."
        ),
        overlay="TOP QUALITY. FAIR PRICE.",
        overlay_sub="RH Filters aftermarket diesel fuel filter kit — aftermarket replacement for OE# DDE A9360900651. Service on schedule, keep the truck running.",
        props=["complete kit grouped (main filter + strain insert + O-rings)", "RH Filters shield + tagline lockup", "soft-focus semi-truck highway band", "aftermarket / OE# strip"],
        lighting="Clean even product light on the kit; airy soft-focus highway band above. Trustworthy, technical, value-forward.",
        why_it_works=(
            "Closes on the brand promise a value-driven fleet buyer needs before checkout: top quality, fair "
            "price, exact aftermarket fitment, and a service-on-schedule cue that nudges multi-unit / repeat "
            "purchase. No URL, no price symbol, no OEM implication — fully compliant."
        ),
        ctr="The tagline + highway context frames the kit as the smart fleet maintenance buy.",
        cvr="Reinforces value and repeat-service logic at the decision point, lifting both conversion and units-per-order.",
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Brand banner: Heavy-duty filtration, fair price.",
        role="a+_banner",
        headline="HEAVY-DUTY DIESEL FILTRATION. FAIR PRICE.",
        body=(
            "RH Filters by Royal Holding USA builds aftermarket filtration for the trucks that keep America "
            "moving. This diesel fuel filter insert kit is an aftermarket replacement for OE# DDE A9360900651, "
            "engineered for Detroit Diesel DD13, DD15 and DD16 applications. Top quality, fair price, exact fitment."
        ),
        visual="Wide cinematic engine-bay scene — the complete kit front-center on a clean shop surface, soft-focus Detroit Diesel engine behind, garage work-light from the side. RH blue logo upper-left; 'Replaces OE# DDE A9360900651' in a small badge in the lower band.",
        alt="RH Filters Detroit Diesel fuel filter insert kit on a shop surface in an engine bay, badged as an aftermarket replacement for OE# DDE A9360900651.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): The RH Filters Difference",
        role="a+_carousel",
        headline="THE RH FILTERS DIFFERENCE",
        body=(
            "Tile 1: <b>EXACT OE CROSS-REFERENCE</b> — Aftermarket replacement for OE# DDE A9360900651.<br/>"
            "Tile 2: <b>FITS DD13 / DD15 / DD16</b> — Engineered for Detroit Diesel heavy-duty applications.<br/>"
            "Tile 3: <b>COMPLETE KIT</b> — Strain filter insert, main filter &amp; all required O-rings.<br/>"
            "Tile 4: <b>CLEAN FUEL FLOW</b> — Helps separate water &amp; debris before your injectors.<br/>"
            "Tile 5: <b>TOP QUALITY · FAIR PRICE</b> — Machined, durable build for real heavy-duty miles."
        ),
        visual="5 square tiles, RH blue accent corner on each, consistent composition. Small technical icons (cross-reference tag, engine, exploded kit, fuel-flow arrow, RH shield).",
        alt="Five-tile Premium A+ carousel covering RH Filters fuel kit differentiators: OE cross-reference, Detroit Diesel fit, complete kit, clean fuel flow, quality and value.",
    ),
    AIModule(
        name="Module 3 — Banner: Confirm your fitment",
        role="a+_banner",
        headline="CONFIRM YOUR FITMENT — AFTERMARKET REPLACEMENT FOR OE# DDE A9360900651.",
        body=(
            "This is a vehicle-specific aftermarket replacement, not a one-size-fits-all filter. It is built for "
            "OE# DDE A9360900651 and fits Detroit Diesel DD13, DD15 and DD16 applications, including Freightliner "
            "Cascadia chassis. Check the OE number on your current unit against the listing before ordering for "
            "an exact match — the surest way to avoid leaks, returns and downtime."
        ),
        visual="Wide banner: clean parts-catalog cross-reference panel on the left (OE# DDE A9360900651, Type: diesel fuel filter insert kit, Application: DD13/DD15/DD16) with a large RH-green check; the main filter sharp on the right. RH blue and green palette only.",
        alt="Premium A+ banner showing the RH Filters fuel kit cross-reference for OE# DDE A9360900651 and Detroit Diesel DD13/DD15/DD16 fitment.",
    ),
    AIModule(
        name="Module 4 — Banner: What's in the box",
        role="a+_banner",
        headline="A COMPLETE SERVICE IN ONE BOX.",
        body=(
            "Every kit includes the strain filter insert, the main filter and all required O-rings — everything "
            "one diesel fuel filter service needs. No second trip to the parts counter, no missing seals. Open "
            "the kit, swap the old set, fit the seals and you are back on the road with clean, well-filtered fuel."
        ),
        visual="Triptych within one banner: LEFT — strain filter insert macro. CENTER — main filter macro. RIGHT — O-ring set macro. Each lightly labeled in RH blue, even technical light across all three panels, soft graphite surface.",
        alt="Triptych A+ banner showing the three components of the RH Filters Detroit Diesel fuel kit: strain filter insert, main filter and O-rings.",
    ),
    AIModule(
        name="Module 5 — Carousel (5 tiles): RH Filters for Your Fleet",
        role="a+_carousel",
        headline="RH FILTERS FOR YOUR FLEET",
        body=(
            "Tile 1: <b>DIESEL FUEL FILTER KIT (this product)</b> — Aftermarket replacement for OE# DDE "
            "A9360900651. Strain insert + main filter + O-rings.<br/>"
            "Tile 2: <b>OIL FILTERS &amp; KITS</b> — Heavy-duty oil filtration for Detroit Diesel &amp; Cummins "
            "service intervals.<br/>"
            "Tile 3: <b>FUEL-WATER SEPARATORS</b> — Keep water out of the fuel system on long hauls.<br/>"
            "Tile 4: <b>ENGINE &amp; CABIN AIR FILTERS</b> — Clean intake air and a fresher cab.<br/>"
            "Tile 5: <b>FILTER SERVICE KITS</b> — Bundled aftermarket kits for Freightliner, Volvo, Peterbilt, "
            "Kenworth &amp; International.<br/>"
            "<i>Pull current product photography from RH Filters brand assets — confirm exact cross-reference "
            "numbers per SKU before publishing.</i>"
        ),
        visual="5 identical-composition product tiles. RH blue + green accent corner on each. Consistent filter / kit packaging photography, flat-lay style.",
        alt="Five-tile A+ carousel of the RH Filters range — fuel filter kit, oil filters, fuel-water separators, air filters and filter service kits for heavy-duty trucks.",
    ),
    AIModule(
        name="Module 6 — Premium Q&A",
        role="a+_qa",
        headline="QUESTIONS MECHANICS ASK",
        body=(
            "<b>Q.</b> Will this fit my truck?<br/>"
            "<b>A.</b> This is an aftermarket replacement for OE# DDE A9360900651, fitting Detroit Diesel DD13, "
            "DD15 and DD16 applications including Freightliner Cascadia. Check the OE number on your current unit "
            "against this listing before ordering for an exact match.<br/><br/>"

            "<b>Q.</b> Is the kit complete, or do I need extra seals?<br/>"
            "<b>A.</b> The kit is complete: strain filter insert, main filter and all required O-rings are "
            "included. No extra seals to source — open the box and service.<br/><br/>"

            "<b>Q.</b> Is this an OEM part?<br/>"
            "<b>A.</b> No. This is an aftermarket replacement for OE# DDE A9360900651. It is "
            "engineered to fit and perform as a direct service replacement at a fair price.<br/><br/>"

            "<b>Q.</b> What does the kit do?<br/>"
            "<b>A.</b> It supports diesel fuel filtration — the strain insert and main filter help separate "
            "water and debris from your fuel before it reaches the injectors. Drivers report smoother fuel "
            "flow and quieter operation after a fresh service.<br/><br/>"

            "<b>Q.</b> How is the quality?<br/>"
            "<b>A.</b> The kit uses multi-pleat fuel media in a machined, durable housing. Buyers report "
            "leak-free installs and long-haul confidence well past 25,000 miles, with quality that holds up "
            "against truck-stop options.<br/><br/>"

            "<b>Q.</b> Who makes it?<br/>"
            "<b>A.</b> RH Filters by Royal Holding USA — aftermarket heavy-duty truck filtration based in "
            "Bensenville, Illinois. Top quality, fair price."
        ),
        visual="Vertical Q/A table. RH green divider lines between each Q. Small RH blue Q. and A. labels.",
        alt="Premium Q&A module answering the six most-asked mechanic questions for the RH Filters Detroit Diesel fuel filter insert kit.",
    ),
    AIModule(
        name="Module 7 — Premium Comparison Chart",
        role="a+_comparison",
        headline="WHY RH FILTERS",
        body=(
            "Compare across 4 columns: <b>RH Filters Fuel Kit</b> · Generic single fuel filter · Truck-stop "
            "filter · Dealer OE part.<br/><br/>"
            "Rows: Aftermarket replacement for OE# DDE A9360900651 · Fits Detroit Diesel DD13/DD15/DD16 · Complete kit (insert + "
            "filter + O-rings) · All seals included · Multi-pleat fuel media · Machined, durable build · "
            "Aftermarket value pricing.<br/><br/>"
            "Highlight the RH Filters column with a soft RH-green tint and a 'FLEET CHOICE' ribbon at the top "
            "of the column. Competitor columns use category descriptors only — no brand names, no OEM implication."
        ),
        visual="Standard Amazon Premium Comparison Chart layout, 4 product columns. Competitor columns use category descriptors only — no brand names. RH blue header row.",
        alt="Premium comparison chart for the RH Filters Detroit Diesel fuel kit vs. a generic single fuel filter, a truck-stop filter and a dealer OE part.",
    ),
]


QA = [
    AIQA(q="Will this fit my truck?",
         a="This is an aftermarket replacement for OE# DDE A9360900651, fitting Detroit Diesel DD13, DD15 and DD16 applications including Freightliner Cascadia. Check the OE number on your current unit against this listing before ordering for an exact match."),
    AIQA(q="Is the kit complete or do I need to buy seals separately?",
         a="The kit is complete: strain filter insert, main filter and all required O-rings are included. No extra seals to source — open the box and service."),
    AIQA(q="Is this an OEM part?",
         a="No. This is an aftermarket replacement for OE# DDE A9360900651. It is engineered to fit and perform as a direct service replacement at a fair price."),
    AIQA(q="What does the kit actually do?",
         a="It supports diesel fuel filtration. The strain insert and main filter help separate water and debris from your fuel before it reaches the injectors. Drivers report smoother fuel flow with no sputtering and quieter operation after a fresh service."),
    AIQA(q="How is the build quality?",
         a="The kit uses multi-pleat fuel media in a machined, durable housing built for heavy-duty miles. Buyers report leak-free installs and long-haul confidence well past 25,000 miles, with quality that holds up against truck-stop options."),
    AIQA(q="Will it fit a DD15 specifically?",
         a="Yes — it fits Detroit Diesel DD15 along with DD13 and DD16 applications, as an aftermarket replacement for OE# DDE A9360900651. As always, confirm the OE number on your unit before ordering."),
    AIQA(q="How often should I service the fuel filter?",
         a="Change your diesel fuel filter kit at the interval in your truck's maintenance schedule, or sooner if you notice fuel sputtering, hard starts or reduced flow. Keeping a kit on hand lets you service on schedule and avoid downtime."),
    AIQA(q="Who makes it and where?",
         a="RH Filters by Royal Holding USA — aftermarket heavy-duty truck filtration based in Bensenville, Illinois. Top quality, fair price."),
]


# Backend KWs — stem-deduped, byte-packed. Avoid: brand terms already in title, superlatives.
BACKEND = (
    "detroit diesel fuel filter kit insert dde a9360900651 dd13 dd15 dd16 diesel fuel filter kit "
    "fuel water separator main filter strain filter o ring seal heavy duty truck filtration "
    "freightliner cascadia diesel mechanic fleet aftermarket replacement oe cross reference "
    "fuel filter service kit diesel engine fuel system multi pleat media owner operator semi truck"
)


def main() -> None:
    print("Loading Royal Holding USA customer + parsing RH Filters Excel…")
    cust = load_customer("royal_holding_usa")
    brief = parse_excel(EXCEL)
    OUT = HERE / f"{PLAN_NO}_{ASIN}_Image Plan.pdf"
    print(f"  Product: {brief.product_name}")
    print(f"  ASIN: {ASIN}  Marketplace: {cust.marketplace}")
    print(f"  USPs={len(brief.usps)} KWs={len(brief.all_keywords)} reviews=+{len(brief.good_reviews)}/-{len(brief.bad_reviews)}")
    print(f"  Replaces OE#: DDE A9360900651 (aftermarket replacement — fitment-verified copy)")
    print(f"  TITLE real chars: {len(TITLE)}")

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
