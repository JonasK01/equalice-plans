"""Waschii — Pocket-Sized Travel Clothes Washer (Portable Wash Bag)
Hand-written, KW-led, conversion-focused copy injected into the branded pipeline.

Marketplace: amazon.com (USA) — English overlays + customer copy.
ASIN: B0CQ71ZVJF · Product 01 · Brand: Waschii (client folder "Eric Williamson").

Positioning: Scrubba-style MANUAL portable wash bag. Win the click on the promise
"wash anywhere — no power, no sink, no laundromat", proven with the real specifics
(140 g, folds to palm, leakproof, solar-warm panel, gentle on delicates).

Compliance guardrails (US):
  - MANUAL device — never imply an electric/motorized machine.
  - Does NOT fully replace a washer/laundromat — it refreshes small essential loads.
  - Never name/knock the competitor "Scrubba".
  - No best / #1 / guaranteed / miracle · no prices or URLs on-image.
"""
from __future__ import annotations
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent          # self-contained product folder
ROOT = HERE.parents[5]                           # project root (Claude_Code/)
sys.path.insert(0, str(ROOT))

from tools.brief_app.core.customers import load_customer
from tools.brief_app.core.excel_parser import parse_excel
from tools.brief_app.core.pdf_builder import BriefBuilder
from tools.brief_app.core.ai import AIImagePlanItem, AIModule, AIQA


EXCEL = HERE / "listing.xlsx"
PLAN_NO = "01"


# ===== KW-led copy (US / English) =====

TITLE = ('Waschii Pocket-Sized Travel Clothes Washer — Portable Wash Bag for Camping, Hostels, '
         'Vanlife and RV · 6.7 L · Only 140 g · Leakproof · Solar-Warm Panel · '
         'Eco-Friendly · No Power or Sink Needed')

BULLETS = [
    "<b>WASH ANYWHERE — NO POWER OR PLUMBING</b> — Waschii turns any spot into your "
    "laundry room. Add detergent, pour in water, roll the top closed and agitate by hand for a "
    "couple of minutes — you become the washing machine. Perfect for campsites, hostels, cabins, "
    "boats, sleeper trains, cruises, RVs and off-grid stays where a real washer just isn't there.",

    "<b>POCKET-SIZED — ONLY 140 g (4.9 oz)</b> — Folds down to palm size and "
    "weighs about the same as a phone, so it disappears into a carry-on, backpack or van drawer. "
    "One-bag travelers, backpackers and digital nomads pack fewer clothes and simply refresh the "
    "essentials on the road.",

    "<b>LEAKPROOF — WASH WITHOUT THE MESS</b> — A valve-free silicone gasket seal plus "
    "triple-welded seams keep water where it belongs. Hold it upside down — no drips on the tent "
    "floor, hostel bunk or hotel carpet. Flexible food-grade TPU with a glassy interior that "
    "rinses clean and a textured exterior that grips while you wash.",

    "<b>SOLAR-WARM PANEL — ECO-FRIENDLY CLEAN</b> — The dark rear panel soaks up "
    "sunlight to gently warm the wash water — no electricity required. The smart water-flow "
    "agitation loosens everyday dirt without a harsh scrub board, so it stays kind to merino, "
    "activewear, underwear, socks and baby clothes.",

    "<b>6.7 L THAT FITS YOUR MUST-WASH LOAD</b> — Room for roughly two shirts plus a few days of "
    "underwear and socks in one go. A simple wash → rinse → hang routine keeps your core garments "
    "fresh between laundromat visits — so you travel lighter and skip the dirty-laundry buildup.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="Clean white canvas with a soft aqua #EAF4F2 tint across the bottom 15% for grounding. Identical background across all 3 options so the split test isolates composition, not color.",
        purpose="Win the click in a grid of near-identical wash bags. Ship all 3, keep the winner via Amazon Manage Your Experiments.",
        visual=(
            "Mock ALL 3 options below — brand A/B tests and keeps the winner. Each option: ONE "
            "callout, ONE supporting prop, product dominant ~70%. Product must match the real "
            "Waschii bag exactly (roll-top TPU body, dark rear solar panel, sandy-textured "
            "exterior). Note: Amazon slot-1 main must stay pure-white / product-only — these "
            "callout versions are the CTR mains you A/B test against a clean white main.\n\n"

            "OPTION A — FREEDOM / 'WASH ANYWHERE' (owns the core promise)\n"
            "Waschii rolled-and-sealed, standing 3/4 turn, a few soft water droplets on the "
            "textured surface. Lower-right: a small folded fresh tee. Top-right corner: three "
            "tiny 'crossed-out' glyphs — power plug, faucet, laundromat — in muted grey.\n"
            "ONE CALLOUT (top-left badge, charcoal bg / white text): 'WASH ANYWHERE'.\n"
            "Why it wins: no competitor thumbnail states the whole promise — clean clothes with "
            "no power, no sink, no laundromat — in two words.\n\n"

            "OPTION B — PACKS TO YOUR PALM (owns 'travel lighter')\n"
            "Waschii folded down to palm size, resting in an open hand (fingers only, no face), "
            "beside a packed carry-on corner. A luggage scale reading '140 g' hooked to the bag.\n"
            "ONE CALLOUT (bottom-right badge, aqua bg / charcoal text): 'POCKET-SIZED · 140 g'.\n"
            "Why it wins: the one-bag traveler's first question is 'how much room does it steal?' "
            "— this answers it before the click.\n\n"

            "OPTION C — LEAKPROOF PROOF (defuses the #1 fear)\n"
            "Waschii filled with water, held UPSIDE DOWN by the roll-top, zero drips — a dry "
            "surface below. A subtle aqua seal-line highlights the gasket + welded seam.\n"
            "ONE CALLOUT (top-right badge, charcoal bg / white text): 'LEAKPROOF. NO SPILLS.'\n"
            "Why it wins: 'leaky wash bag' is the top complaint in the category — showing zero "
            "drip upside-down is the most persuasive single proof.\n\n"

            "Across all 3: product ~70%, callout ~6% of frame, same lighting + color temperature."
        ),
        overlay="(one callout per option — see visual)",
        overlay_sub="3 hero options shipped — A/B test, keep the winner.",
        props=[
            "OPTION A: sealed Waschii + folded fresh tee + 3 crossed-out icons (plug/faucet/laundromat)",
            "OPTION B: folded Waschii in palm + packed carry-on corner + luggage scale '140 g'",
            "OPTION C: water-filled Waschii held upside-down, no drip + gasket/seam highlight",
        ],
        lighting="Soft top key (5000K daylight) with gentle camera-right fill, slight backlight to separate the bag from white. Same across all 3 for a clean split test.",
        why_it_works=(
            "Three different triggers: A owns the promise (wash anywhere), B owns pack-light "
            "(140 g / pocket), C defuses the category's #1 fear (leaks). One callout, one prop, "
            "one idea each — readable at mobile thumbnail size."
        ),
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: No power. No sink. No laundromat.",
        role="hook",
        background="Soft aqua #EAF4F2 — fresh, clean, travel feel (not sterile studio)",
        purpose="State the whole promise in one frame — the hook no plain-product competitor lands.",
        visual=(
            "Center: Waschii in a hand mid-agitation (hands gripping the textured body, water and "
            "a few suds visible through a subtle window of motion). Across the top, three greyed "
            "icons struck through — a power plug, a faucet/sink, a laundromat storefront — each "
            "with a thin diagonal line. Below the bag, a single aqua check-mark badge: the bag "
            "itself is the answer.\n\n"
            "Keep it MANUAL and honest: this is hand-powered washing, not a motor."
        ),
        overlay="NO POWER. NO SINK.",
        overlay_sub="No laundromat either — just add water, roll, and wash anywhere.",
        props=["Waschii in-hand mid-agitation", "3 crossed-out icons (plug / faucet / laundromat)", "aqua check-mark badge"],
        lighting="Even soft front-light, gentle 3D shadow under the bag. Clarity over drama — this is the promise, it must read instantly.",
        why_it_works=(
            "Every competitor main shows a bag on white. Waschii's hook reframes the whole "
            "category around independence: clean clothes with none of the things you don't have "
            "on the road. Answers 'why click us?' in one glance."
        ),
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: Wash in 3 simple steps",
        role="educate",
        background="White with a soft aqua ribbon footer",
        purpose="Kill the 'is it complicated / does it actually clean?' hesitation. Show the effortless routine.",
        visual=(
            "Three-panel horizontal how-it-works strip. Headline top: 'CLEAN CLOTHES IN 3 STEPS'.\n\n"
            "STEP 1 — FILL: hands pouring water and a small measure of detergent into the open "
            "roll-top Waschii, a couple of garments inside. Caption: 'Add clothes, water and "
            "detergent.'\n"
            "STEP 2 — WASH: hands rolling the top closed and squeezing/agitating the bag on a van "
            "bench or camp table. Caption: 'Roll, seal, and agitate 2-3 minutes.'\n"
            "STEP 3 — HANG: a fresh tee clipped to a paracord line by a van door in soft sun. "
            "Caption: 'Rinse and hang — done.'\n\n"
            "Thin aqua arrows connect the three steps. Simple, real, sunlit."
        ),
        overlay="WASH IN 3 SIMPLE STEPS.",
        overlay_sub="Fill · Roll and wash · Rinse and hang — no machine, no laundromat.",
        props=["3-panel step strip", "roll-top fill shot", "hand-agitation shot", "fresh tee on a paracord line", "aqua connector arrows"],
        lighting="Bright natural daylight, consistent across all three panels. Educational clarity beats mood.",
        why_it_works=(
            "Manual washing sounds like effort until you see it's three easy steps. Showing the "
            "full wash → rinse → hang routine removes the 'too fiddly' objection and makes the "
            "value obvious for someone standing in a sink-less hostel room."
        ),
    ),
    AIImagePlanItem(
        name="Image 4 — Desire: Fresh clothes on the road (vanlife / hostel)",
        role="desire",
        background="Real travel scene — open campervan door or hostel bunk, warm afternoon light",
        purpose="Place the buyer in the moment. Owns the feeling: fresh essentials, freedom to travel light.",
        visual=(
            "Wide, aspirational lifestyle shot. A campervan side door open to a sunlit view "
            "(mountains / coast). On a paracord line strung across the doorway: two fresh tees "
            "and a pair of socks drying in the breeze. On the van bench in the foreground: the "
            "Waschii bag (sealed, a little wet), next to a folded merino tee and a compact "
            "travel-detergent bottle.\n\n"
            "A traveler (hands / lower-arm only, or seen from behind — no face-forward portrait) "
            "clipping the last garment to the line. Golden-hour warmth, wanderlust mood, real "
            "not staged. Waschii logo small, lower-corner."
        ),
        overlay="FRESH CLOTHES ON THE ROAD.",
        overlay_sub="Pack fewer clothes — refresh your essentials wherever the day ends.",
        props=["campervan door + paracord line", "2 fresh tees + socks drying", "sealed Waschii on bench", "folded merino tee", "compact detergent bottle", "traveler (hands / from behind)"],
        lighting="Warm golden-hour side-light from the van doorway. Soft rim on the drying clothes. Honest, lived-in — not a studio set.",
        why_it_works=(
            "Sells the outcome, not the object: the dream of one-bag travel where clean clothes "
            "are never a problem. The strongest CVR image in the plan — the buyer sees their own "
            "trip, with Waschii quietly making it work."
        ),
    ),
    AIImagePlanItem(
        name="Image 5 — Trust: Built leakproof, food-grade, made to last",
        role="trust",
        background="White with soft aqua panels behind each badge for separation",
        purpose="Stack the build-quality proofs that defuse 'will it leak / is it safe / will it last?'",
        visual=(
            "Centered macro of the Waschii bag (roll-top + dark solar panel visible). Four trust "
            "badges in the corners:\n\n"
            "  • TOP-LEFT — VALVE-FREE LEAKPROOF (silicone-gasket icon)\n"
            "  • TOP-RIGHT — TRIPLE-WELDED SEAMS (welded-seam icon)\n"
            "  • BOTTOM-LEFT — FOOD-GRADE TPU (droplet icon — glassy interior, rinses clean)\n"
            "  • BOTTOM-RIGHT — SOLAR-WARM PANEL (sun icon — no power needed)\n\n"
            "A thin supporting strip below: 'Flexible waterproof TPU · smooth interior rinses "
            "clean · textured exterior grips while you wash · gentle on delicates.'"
        ),
        overlay="LEAKPROOF. BUILT TO LAST.",
        overlay_sub="Silicone gasket · triple-welded seams · waterproof TPU · solar-warm panel.",
        props=["Waschii macro (roll-top + solar panel)", "4 corner badges", "thin spec strip"],
        lighting="Studio-even light with a crisp catch-light on the TPU. Badges legible at thumbnail size.",
        why_it_works=(
            "The category's trust gap is durability and leaks. Stacking gasket + welded seams + "
            "food-grade TPU + solar panel in one frame answers every build-quality doubt before "
            "the buyer has to ask it."
        ),
    ),
    AIImagePlanItem(
        name="Image 6 — Desire: How light, how small, how much it holds",
        role="desire",
        background="Soft aqua #EAF4F2 — same family as Image 2 for visual rhythm",
        purpose="Make the pack-light value and capacity concrete. Removes 'how big / how much does it hold?' friction.",
        visual=(
            "Split-frame spec infographic.\n\n"
            "LEFT 55%: Waschii folded to palm size in an open hand, a luggage scale beside it "
            "reading '140 g / 4.9 oz'. A faint 'ghost' of the unfolded bag behind it shows the "
            "6.7 L size, so both the packed and the in-use size read at once.\n\n"
            "RIGHT 45%: a clean 'WHAT FITS' laid-out flat — 2 shirts + 3 pairs of underwear + "
            "socks arranged neatly, with a small caption: '6.7 L — your must-wash essentials, in "
            "one wash.'\n\n"
            "Small footer: 'Folds to pocket size · weighs about as much as a phone.'"
        ),
        overlay="140 g. FOLDS TO PALM.",
        overlay_sub="6.7 L holds ~2 shirts plus underwear and socks — packs down to pocket size.",
        props=["folded Waschii in palm", "luggage scale '140 g / 4.9 oz'", "ghosted full-size bag", "'what fits' flat-lay (2 shirts + underwear + socks)"],
        lighting="Even soft front-light, clean infographic feel.",
        why_it_works=(
            "Two purchase questions — 'how much space does it steal?' and 'will my load actually "
            "fit?' — answered in one frame with real numbers. Turns abstract specs (140 g, 6.7 L) "
            "into a decision the buyer can picture."
        ),
    ),
    AIImagePlanItem(
        name="Image 7 — Brand close: Wash anywhere. Travel lighter.",
        role="close",
        background="Wide wanderlust travel scene — trailhead / coastline at golden hour",
        purpose="Close on the brand promise and identity before checkout.",
        visual=(
            "Mid-range aspirational shot: a backpacker's pack resting at a scenic overlook "
            "(mountain ridge or coast) at golden hour, the Waschii bag clipped to the outside of "
            "the pack, a fresh tee just dried. The whole frame says 'go further, carry less.'\n\n"
            "Lower band: Waschii logo + tagline. A small honest line of reassurance about what "
            "Waschii is — the pocket-sized washer that goes wherever you do."
        ),
        overlay="WASH ANYWHERE. TRAVEL LIGHTER.",
        overlay_sub="Waschii — the pocket-sized travel washer that goes wherever you do.",
        props=["backpack at scenic overlook", "Waschii clipped to pack", "freshly dried tee", "Waschii logo + tagline band"],
        lighting="Golden-hour warmth, wide and airy. Aspirational, honest, brand-forward.",
        why_it_works=(
            "Closes on identity, not features: the buyer isn't buying a bag, they're buying the "
            "freedom to travel light and stay fresh. Ties the whole plan back to the brand "
            "promise the moment before they add to cart."
        ),
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Brand banner: Wash anywhere. Travel lighter.",
        role="a+_banner",
        headline="WASH ANYWHERE. TRAVEL LIGHTER.",
        body=(
            "Waschii is a pocket-sized, manual travel clothes washer for people who refuse to "
            "carry a week of dirty laundry. No power, no plumbing, no laundromat — just add water, "
            "roll it closed, and wash your essentials wherever the day ends: campsites, hostels, "
            "vans, boats, sleeper trains and off-grid stays."
        ),
        visual="Wide cinematic travel scene — open campervan door at golden hour, Waschii bag on the bench front-center, a fresh tee drying on a line in soft focus. Waschii logo upper-left, tagline in the lower band.",
        alt="Waschii pocket-sized travel clothes washer on a campervan bench at golden hour with fresh laundry drying on a line.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): Why Waschii",
        role="a+_carousel",
        headline="WHY WASCHII",
        body=(
            "Tile 1: <b>WASH ANYWHERE</b> — No power, no plumbing, no sink required.<br/>"
            "Tile 2: <b>ONLY 140 g (4.9 oz)</b> — Folds to palm size, packs to pocket.<br/>"
            "Tile 3: <b>VALVE-FREE LEAKPROOF</b> — Silicone gasket &amp; triple-welded seams.<br/>"
            "Tile 4: <b>SOLAR-WARM PANEL</b> — Dark panel gently warms water in the sun.<br/>"
            "Tile 5: <b>GENTLE ON DELICATES</b> — Kind to merino, activewear &amp; baby clothes."
        ),
        visual="5 square tiles, aqua accent corner on each. Consistent composition. Small icons (globe/pin · folded bag on scale · gasket seal · sun · soft sweater).",
        alt="Five-tile Premium A+ carousel covering Waschii differentiators: wash anywhere, 140 g, leakproof, solar-warm panel, gentle on delicates.",
    ),
    AIModule(
        name="Module 3 — Banner: How Waschii works (3 steps)",
        role="a+_banner",
        headline="CLEAN CLOTHES IN 3 STEPS.",
        body=(
            "1. FILL — add your clothes, water and a little detergent to the roll-top body. "
            "2. WASH — roll the top closed and agitate by hand for 2-3 minutes; the smart "
            "water-flow action loosens everyday dirt without a harsh scrub board. 3. RINSE and "
            "HANG — wring, hang, and you're done. You become the washing machine — no electricity "
            "and no sink needed."
        ),
        visual="Wide 3-panel banner: FILL (pouring water into the open bag) → WASH (hands rolling and agitating) → HANG (fresh tee on a paracord line). Thin aqua arrows between panels, consistent daylight.",
        alt="Premium A+ banner showing the Waschii three-step wash routine: fill, wash by hand, rinse and hang.",
    ),
    AIModule(
        name="Module 4 — Banner: Leakproof, food-grade, solar-warm",
        role="a+_banner",
        headline="BUILT LEAKPROOF. WARMED BY THE SUN.",
        body=(
            "A valve-free body with a silicone gasket seal and triple-welded seams keeps water "
            "in — hold it upside down with no drips. The flexible, fully waterproof food-grade TPU "
            "has a glassy interior that rinses clean and a textured exterior that grips while you "
            "wash. The dark rear panel soaks up sunlight to gently warm the wash water, so you get "
            "a comfortable, eco-friendly clean with no power at all."
        ),
        visual="Wide banner split in two: LEFT — macro of the roll-top closure, gasket and welded seam, bag held upside-down with zero drip. RIGHT — the dark solar panel in warm sunlight with a subtle heat glow. Aqua + charcoal palette.",
        alt="Premium A+ banner showing Waschii's leakproof valve-free construction and dark solar-warming panel.",
    ),
    AIModule(
        name="Module 5 — Carousel (5 tiles): Made for the way you travel",
        role="a+_carousel",
        headline="MADE FOR THE WAY YOU TRAVEL",
        body=(
            "Tile 1: <b>VANLIFE &amp; RV</b> — Fresh clothes off-grid, no hookup required.<br/>"
            "Tile 2: <b>BACKPACKING &amp; HOSTELS</b> — Wash in a sink-less room, hang overnight.<br/>"
            "Tile 3: <b>CRUISES, TRAINS &amp; BOATS</b> — Refresh essentials in a tiny cabin.<br/>"
            "Tile 4: <b>ONE-BAG TRAVEL</b> — Pack fewer clothes; re-wear less, wash more.<br/>"
            "Tile 5: <b>BABY ESSENTIALS &amp; EMERGENCY KITS</b> — Gentle, always-ready backup."
        ),
        visual="5 identical-composition lifestyle tiles (van · hostel bunk · cruise cabin · packed carry-on · folded baby clothes). Aqua accent corner on each; consistent warm daylight photography.",
        alt="Five-tile A+ carousel of Waschii use cases: vanlife and RV, backpacking and hostels, cruises and trains, one-bag travel, baby essentials and emergency kits.",
    ),
    AIModule(
        name="Module 6 — Premium Q&A",
        role="a+_qa",
        headline="QUESTIONS TRAVELERS ASK",
        body=(
            "<b>Q.</b> Do I need electricity or a sink?<br/>"
            "<b>A.</b> No. Waschii is completely manual — add water and detergent, roll it closed, "
            "and agitate by hand. It works anywhere: campsites, hostels, boats, trains, RVs and "
            "off-grid stays.<br/><br/>"

            "<b>Q.</b> Will it leak in my bag or hotel room?<br/>"
            "<b>A.</b> The valve-free body uses a silicone gasket seal and triple-welded seams to "
            "keep water inside — you can hold it upside down without drips. Roll the top closed as "
            "directed before you agitate.<br/><br/>"

            "<b>Q.</b> How much can it wash at once?<br/>"
            "<b>A.</b> The 6.7 L body fits a small must-wash load — roughly two shirts plus a few "
            "days of underwear and socks. It is made to refresh your essentials between full "
            "washes, so you can pack lighter.<br/><br/>"

            "<b>Q.</b> How does the solar warming work?<br/>"
            "<b>A.</b> The dark rear panel absorbs sunlight to gently warm the wash water. Leave "
            "the filled bag in the sun for an hour or two when warmer water helps — no power "
            "needed.<br/><br/>"

            "<b>Q.</b> Is it gentle enough for delicates?<br/>"
            "<b>A.</b> Yes. The smart water-flow agitation cleans without a rigid scrub board, so "
            "it stays kind to merino, activewear, underwear and baby clothes.<br/><br/>"

            "<b>Q.</b> How small and light is it?<br/>"
            "<b>A.</b> It weighs only 140 g (4.9 oz) and folds down to palm size, so it slips into "
            "a carry-on, backpack or van drawer without stealing space."
        ),
        visual="Vertical Q/A table. Aqua divider lines between each question. Small charcoal Q. and aqua A. labels.",
        alt="Premium Q&A module answering the six most-asked traveler questions for the Waschii travel clothes washer.",
    ),
    AIModule(
        name="Module 7 — Premium Comparison Chart",
        role="a+_comparison",
        headline="WASCHII VS. THE ALTERNATIVES",
        body=(
            "Compare across 4 columns: <b>Waschii Travel Clothes Washer</b> · Electric mini travel "
            "washer · Basic wash bag · Hand-washing in a sink.<br/><br/>"
            "Rows: Needs power (No) · Needs a sink/plumbing (No) · Weight (140 g) · Folds to pocket "
            "size · Valve-free leakproof seal · Solar-warm panel · Gentle on delicates · Works "
            "off-grid.<br/><br/>"
            "Highlight the Waschii column with a soft aqua tint and a 'TRAVELS ANYWHERE' ribbon at "
            "the top of the column."
        ),
        visual="Standard Amazon Premium Comparison Chart, 4 columns. Alternative columns use category descriptors only — no brand names. Charcoal header row, aqua highlight on the Waschii column.",
        alt="Premium comparison chart for Waschii vs. an electric mini travel washer, a basic wash bag, and hand-washing in a sink.",
    ),
]


QA = [
    AIQA(q="Do I need electricity, plumbing or a sink to use Waschii?",
         a="No. Waschii is completely manual. Add your clothes, water and a little detergent, roll the top closed, and agitate by hand for 2-3 minutes. It works at campsites, hostels, cabins, boats, sleeper trains, cruises, RVs and other off-grid places."),
    AIQA(q="Will it leak in my luggage or hotel room?",
         a="The valve-free body uses a silicone gasket seal plus triple-welded seams to keep water inside, so you can hold it upside down without drips. Just roll the top closure as directed before you agitate."),
    AIQA(q="How much laundry can it hold?",
         a="The 6.7 L body fits a small must-wash load, roughly two shirts plus a few days of underwear and socks. It is designed to refresh your essentials between full washes so you can pack fewer clothes."),
    AIQA(q="How does the solar warming work?",
         a="The dark rear panel absorbs sunlight to gently warm the wash water. Leave the filled bag in the sun for an hour or two when you want warmer water. No electricity is required at any point."),
    AIQA(q="Is Waschii gentle on delicate fabrics?",
         a="Yes. The smart water-flow agitation cleans without a rigid scrub board, so it stays gentle on merino, activewear, underwear, socks and baby clothes."),
    AIQA(q="How small and light is it?",
         a="Waschii weighs only 140 g (4.9 oz) and folds down to palm size, so it slips into a carry-on, backpack or van drawer without taking up meaningful space."),
    AIQA(q="What is it made of, and is it easy to clean?",
         a="It is made from flexible, fully waterproof food-grade TPU. The interior is smooth and glassy so it rinses clean easily, while the textured exterior gives you grip during hand agitation."),
    AIQA(q="Does it replace a washing machine?",
         a="Waschii is built to refresh small essential loads on the road, not to replace a full home washer or laundromat for bedding and large loads. For travel, camping and off-grid days it keeps your core garments fresh wherever you are."),
]


# Backend KWs — stem-deduped, byte-packed. Avoid brand names already in the title and superlatives.
BACKEND = (
    "portable washing bag travel wash bag camping clothes washer manual laundry bag portable "
    "washer travel laundry bag off grid hostel vanlife rv backpacking one bag travel leakproof "
    "tpu solar heated eco friendly hand wash underwear socks delicates cruise sleeper train "
    "camping essentials packable compact 140g digital nomad"
)


def main() -> None:
    print("Loading Waschii customer + parsing listing…")
    cust = load_customer("waschii")
    brief = parse_excel(EXCEL)
    import re as _re
    _raw_asin = brief.asin or ""
    _m = _re.search(r"B0[A-Z0-9]{8}", _raw_asin)   # excel stores ASIN as a full amazon URL
    asin = _m.group(0) if _m else (_raw_asin or "NA")
    OUT = HERE / f"{PLAN_NO}_{asin}_Image Plan.pdf"
    print(f"  Product: {brief.product_name}")
    print(f"  ASIN: {brief.asin}  Marketplace: {cust.marketplace}")
    print(f"  USPs={len(brief.usps)} KWs={len(brief.all_keywords)} Q&A={len(brief.rufus_qa)} reviews=+{len(brief.good_reviews)}/-{len(brief.bad_reviews)}")

    builder = BriefBuilder(cust, brief, OUT, ai=None)
    builder._ai_title = TITLE
    builder._ai_bullets = BULLETS
    builder._ai_images = IMAGES
    builder._ai_modules = MODULES
    builder._ai_qa = QA
    builder._ai_backend = BACKEND
    builder.copy_source_label = "Hand-written senior copy (KW-led, US/English)"

    print("Building branded PDF…")
    pdf_path = builder.build()
    size_kb = pdf_path.stat().st_size // 1024
    import re
    pages = len(re.findall(rb'/Type\s*/Page[^s]', pdf_path.read_bytes()))
    print(f"Built: {pdf_path}")
    print(f"  Pages: {pages}  Size: {size_kb} KB")


if __name__ == "__main__":
    main()
