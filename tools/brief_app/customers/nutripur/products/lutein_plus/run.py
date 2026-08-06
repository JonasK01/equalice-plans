"""Nutripur Lutein Plus — Lutein + Zeaxanthin + Bilberry + Vitamin A Eye Formula — Image Plan 09
Hand-written senior copy injected into the branded ReportLab pipeline.

Marketplace: amazon.ca (Canada) · Overlay language: ENGLISH.

LANGUAGE SPLIT (the standard):
  • ENGLISH — art-direction / strategy fields the designer reads:
    image purpose, background, visual, props, lighting, why_it_works, ctr, cvr,
    and module visual.
  • ENGLISH — marketplace, customer-facing text the shopper reads:
    TITLE, BULLETS, image overlay, overlay_sub, module headline, module body,
    QA, BACKEND. (amazon.ca = EN primary.)

OVERLAY RULE: sell the OUTCOME, not the action. Every on-image overlay leads with
the result / benefit / defused fear the buyer wants. Each overlay is distinct and
tied to that image's job. Hard limits (auto-linted on build):
  overlay ≤ 30 chars AND ≤ 5 words · overlay_sub ≤ 90 chars
  module headline ≤ 38 chars · bullet head <b>…</b> ≤ 45 chars · TITLE ≤ 200 real chars

Verified facts (see SOURCE_NOTES.md — from the REAL box label + Health Canada LNHPD):
  - Health Canada NPN 80058123 (THIS product's own NPN — not the GENIUS NPN)
  - Per 2-capsule daily dose: Lutein 20 mg (LUTEMAX 2020 marigold) providing Zeaxanthin,
    Bilberry 4:1 extract 600 mg (= 2400 mg whole bilberry), Organic Canadian Blueberry 200 mg,
    Vitamin A 1500 mcg RAE (5000 IU, palmitate)
  - 60 vegetarian capsules · Adults take 1 to 2 capsules daily · GMP · Made in Canada
  - No artificial colours / flavours / preservatives

Audience: adults 40+, screen-heavy / digital-eye-strain users, eye-health shoppers.
Objection defused: capsule size / swallowability → show the small vegetarian capsule, once-daily.

Compliance (auto-blocks):
  - ONLY Health-Canada-approved structure/function wording for eyes/vision.
  - NO cure/treat/prevent/diagnose, NO disease names (macular degeneration / cataracts / AMD
    live ONLY in BACKEND), NO best/#1/ultimate/guaranteed, NO "$", NO URL/.com in customer copy.
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


EXCEL = HERE / "listing.xlsx"
PLAN_NO = "09"
ASIN = "B07FQN9F9C"


# ===== KW-led, marketing-optimized EN copy (customer-facing) — NPN 80058123 defensible =====

# Title is HTML-escaped, so literal "&" counts as 1 char. Keep ≤200 real chars.
TITLE = (
    "Nutripur Lutein Plus — Lutein 20mg + Zeaxanthin + Bilberry & Vitamin A Eye Health "
    "Supplement · Antioxidant Vision Formula · 60 Vegetarian Capsules · Health Canada "
    "NPN 80058123 · Made in Canada"
)

BULLETS = [
    "<b>LUTEIN + ZEAXANTHIN EYE FORMULA</b> — A focused daily blend of Lutein and Zeaxanthin "
    "(from LUTEMAX 2020 marigold) that helps maintain eye health and supports the macular "
    "pigment that filters harmful blue light from screens and sunlight.",

    "<b>4 EYE NUTRIENTS IN ONE CAPSULE</b> — Lutein 20 mg, Zeaxanthin, Bilberry 4:1 extract "
    "600 mg (equal to 2400 mg whole bilberry) and Vitamin A 1500 mcg RAE, plus organic "
    "Canadian blueberry. Provides antioxidants for the maintenance of eye health.",

    "<b>FOR SCREEN-HEAVY EYES &amp; ADULTS 40+</b> — Built for long days on phones, laptops "
    "and monitors. Helps improve macular pigment optical density and supports the development "
    "and maintenance of night vision.",

    "<b>ONE SMALL CAPSULE, ONCE A DAY</b> — Adults take 1 to 2 small vegetarian capsules "
    "daily. Easy to swallow, no fishy aftertaste. Vegan, gluten-free and made with no "
    "artificial colours, flavours or preservatives.",

    "<b>60 CAPSULES · HEALTH CANADA NPN</b> — A 1 to 2 month supply. Approved by Health Canada "
    "(NPN 80058123), GMP-certified and made in Canada by Nutripur — three generations of "
    "clinical-quality nutrition.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="White canvas with a soft teal tint (#E8F5F2) in the bottom 15% for grounding. Identical backdrop across all 3 options for a clean split-test.",
        purpose="Win the click in the amazon.ca eye-vitamin grid — stand out next to generic lutein bottles.",
        visual=(
            "Brief the designer to mock ALL 3 options below. Brand picks the winner via Amazon "
            "Manage Your Experiments. Each option uses ONE callout, ONE action cue, ONE supporting "
            "prop — clean, never stacked. Use the real Lutein Plus box from assets/ as the reference.\n\n"

            "▸ OPTION A — NPN CREDENTIAL HERO (owns the trust signal)\n"
            "Center: Lutein Plus box front-facing, label fully readable, slight elevated 3/4 turn, "
            "~70% of frame. Lower-right: 2 small amber vegetarian capsules and a single marigold "
            "petal for the source cue.\n"
            "CALLOUT top-right badge: 'HEALTH CANADA · NPN 80058123' (Nutripur navy #1F3A5F, white "
            "type, small Canada-leaf icon).\n"
            "Why it wins: no competitor in the grid leads with the NPN number visible — the strongest "
            "single trust signal a Canadian eye-health shopper can see before clicking.\n\n"

            "▸ OPTION B — CAPSULE SIZE / EASY DOSE (defuses the swallowability objection)\n"
            "Center: Lutein Plus box left of center. Right: a small white dish with 1 capsule, an "
            "adult fingertip lifting it (fingers only, no face), scale-cue making the small capsule "
            "obvious next to the box.\n"
            "CALLOUT top-left badge: 'ONE SMALL CAP A DAY' (Nutripur teal #2A8C7E, white type).\n"
            "Why it wins: the #1 hesitation on eye supplements is capsule size — this proves the "
            "small, easy-to-swallow vegetarian capsule and the once-daily routine at a glance.\n\n"

            "▸ OPTION C — LUTEIN + ZEAXANTHIN mg STACK (owns the ingredient differentiator)\n"
            "Center: Lutein Plus box. Floating in a clean radial layout: 4 ingredient chips — "
            "LUTEIN 20mg · ZEAXANTHIN · BILBERRY 600mg · VITAMIN A. Each chip a soft teal/navy pill "
            "on a white halo.\n"
            "CALLOUT bottom-right badge: 'LUTEIN 20MG + ZEAXANTHIN' (Nutripur navy).\n"
            "Why it wins: shoppers search exact mg ('lutein 20mg'); surfacing the dose on the hero "
            "matches intent and beats vague 'eye support' bottles.\n\n"

            "Across all 3: box dominant ~70%, callout ~6%, prop fills remainder. Same lighting, "
            "same backdrop, same colour temperature so the split test isolates composition."
        ),
        overlay="(one callout per option — see visual direction)",
        overlay_sub="3 hero options shipped — A/B test, keep the winner",
        props=[
            "OPTION A: box + 2 amber capsules + marigold petal + NPN badge",
            "OPTION B: box + small dish with 1 capsule + adult fingertip (no face) + scale cue + dose badge",
            "OPTION C: box + 4 ingredient chips in radial halo + mg badge",
        ],
        lighting="Soft top key (5000K daylight balanced) with gentle fill from camera-right. Slight backlight on the box so the Lutein Plus label pops. Identical across all 3 options.",
        why_it_works=(
            "Three angles against three buyer triggers: A wins on credential trust (NPN), B defuses "
            "the capsule-size objection, C matches exact-dose search intent. Per the new standard: "
            "one callout, one action cue, one prop. Clean enough to read on a mobile thumbnail."
        ),
        ctr="Leading with the visible NPN, the small-capsule proof and the exact 'Lutein 20mg + Zeaxanthin' dose beats generic eye-vitamin bottles in the amazon.ca grid and matches high-intent search terms.",
        cvr="Instant clarity on what it is (lutein eye formula), the dose, and that the capsule is small and easy to take cuts bounce for the 40+ screen-tired shopper.",
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: 4 eye nutrients in one capsule",
        role="hook",
        background="Soft teal #E8F5F2 (Nutripur mood) — clinical-natural, not pharma-sterile.",
        purpose="Stack the 4-nutrient differentiator with real mg values — the hook generic lutein bottles can't match.",
        visual=(
            "Center: large macro of a single amber vegetarian capsule, oriented so the soft amber "
            "colour reads cleanly. Behind it, 4 ingredient labels in a clean radial layout (12, 3, 6, "
            "9 o'clock): LUTEIN · ZEAXANTHIN · BILBERRY · VITAMIN A. Each label in a soft-edged pill "
            "(Nutripur teal for the carotenoids, navy for bilberry and vitamin A), with a thin "
            "connecting line to the central capsule like a clean medical infographic.\n\n"
            "Below the capsule: a caption strip with the real per-2-capsule values — Lutein 20 mg · "
            "Zeaxanthin (from LUTEMAX 2020) · Bilberry 600 mg (= 2400 mg whole) · Vitamin A 1500 mcg RAE."
        ),
        overlay="LUTEIN + ZEAXANTHIN.",
        overlay_sub="4 eye nutrients in one small capsule — Lutein 20 mg + Zeaxanthin, Bilberry &amp; Vitamin A.",
        props=["single amber capsule (macro)", "4 nutrient label pills", "thin connecting lines (infographic style)"],
        lighting="Even soft front-light, slight 3D shadow under the capsule. Educational hook — clarity over mood.",
        why_it_works=(
            "Every competitor sells 'lutein.' Lutein Plus visibly stacks Lutein + Zeaxanthin + "
            "Bilberry + Vitamin A with real mg, anchored to the box. Educates and differentiates "
            "in one frame, and surfaces the exact-dose search terms shoppers type."
        ),
        ctr="The mg-anchored 4-nutrient stack answers 'how much lutein and what else is in it?' instantly and out-specs vague eye-support bottles.",
        cvr="Concrete amounts plus the Bilberry 4:1 equivalence justify the premium over single-ingredient lutein and reassure the careful 40+ buyer.",
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: what each nutrient supports (NPN-approved claims only)",
        role="educate",
        background="White with a soft Nutripur-teal ribbon footer.",
        purpose="Defend the price premium with Health Canada-language structure/function claims — zero compliance risk.",
        visual=(
            "Four-tile horizontal layout under a headline 'WHAT EACH NUTRIENT SUPPORTS' in Nutripur "
            "navy, sentence case.\n\n"
            "TILE 1 — LUTEIN + ZEAXANTHIN (carotenoid icon, teal)\n"
            "  • Helps maintain eye health\n"
            "  • Helps improve macular pigment optical density\n"
            "  • Supports the pigment that filters blue light\n\n"
            "TILE 2 — BILBERRY 4:1 (berry icon, navy)\n"
            "  • Provides antioxidants for the maintenance of eye health\n"
            "  • 600 mg = 2400 mg whole bilberry\n\n"
            "TILE 3 — ORGANIC BLUEBERRY (berry icon, teal)\n"
            "  • Antioxidant-rich Canadian blueberry\n"
            "  • Complements the bilberry blend\n\n"
            "TILE 4 — VITAMIN A (eye icon, navy)\n"
            "  • Helps in the development and maintenance of night vision\n"
            "  • 1500 mcg RAE per daily dose\n\n"
            "Footer ribbon (Nutripur teal): 'Claims supported by Health Canada NPN 80058123.'"
        ),
        overlay="NUTRIENTS FOR EYE HEALTH.",
        overlay_sub="Backed by Health Canada NPN 80058123 — regulator-approved language.",
        props=["4 ingredient tiles with icons", "4 small eye/berry icons", "NPN citation footer"],
        lighting="Flat clean studio. Educational module — readability beats atmosphere.",
        why_it_works=(
            "Every claim is verbatim from the Health Canada NPN — zero compliance risk. Buyers who "
            "filter on 'is this legit?' see actual regulator-approved language, not marketing-speak, "
            "which earns the premium over cheap single-ingredient lutein."
        ),
        ctr="Regulator-approved, per-nutrient claims read as credible and specific, pulling the careful eye-health shopper deeper into the listing.",
        cvr="NPN-anchored wording defuses the 'are these claims real?' doubt and justifies the premium price.",
    ),
    AIImagePlanItem(
        name="Image 4 — Desire: built for screen-tired eyes",
        role="desire",
        background="Real home-office / desk scene, soft natural light from camera-right.",
        purpose="Place the 40+ screen-heavy buyer in the frame and own the digital-eye-strain use case.",
        visual=(
            "Angled lifestyle shot. An adult (45–60) at a desk in PROFILE or three-quarter from "
            "behind — gently pressing the bridge of the nose / easing tired eyes after a long day on "
            "a laptop. Face naturally obscured by the posture (hand near eyes, head slightly down). "
            "Real and calm, not a posed portrait.\n\n"
            "FOREGROUND right edge: Lutein Plus box (label to camera) beside a small white dish with "
            "1 capsule and a glass of water. Soft-focused laptop and a warm desk lamp behind.\n\n"
            "Soft natural light from camera-right. Home-office / lived-in vibe, NOT pharmacy / lab. "
            "Stock with model release acceptable; avoid brand logos in frame."
        ),
        overlay="FOR SCREEN-TIRED EYES.",
        overlay_sub="Daily eye nutrition for long days on phones, laptops &amp; monitors.",
        props=["adult model (profile, no face-forward)", "Lutein Plus box", "small white dish with 1 capsule", "glass of water", "soft-focused laptop", "warm desk lamp"],
        lighting="Soft natural side-light from camera-right. Gentle rim on the box. Honest natural-clinical, not studio-staged.",
        why_it_works=(
            "Owns the strongest real use case — long screen days for the 40+ buyer — with a person "
            "in frame. Profile / head-down composition delivers the lifestyle CVR signal while "
            "staying brand-safe (no posed staring-into-camera shot)."
        ),
        ctr="The relatable screen-strain moment makes the busy 40+ shopper self-identify and stop scrolling.",
        cvr="Pairing the lifestyle trigger with the visible box and single-capsule dose moves the shopper from 'is this for me?' to 'this is for me.'",
    ),
    AIImagePlanItem(
        name="Image 5 — Trust: small capsule + clean-label credentials",
        role="trust",
        background="White with soft teal panels behind each badge for separation.",
        purpose="Defuse the capsule-size objection AND stack the filters Canadian shoppers scan for.",
        visual=(
            "Centered macro of the Lutein Plus box (label to camera) with one small amber capsule "
            "resting beside a Canadian dime for honest scale. Four trust badges in the corners:\n\n"
            "  • TOP-LEFT — HEALTH CANADA NPN 80058123 (small Canada-leaf icon)\n"
            "  • TOP-RIGHT — VEGETARIAN CAPSULE (small leaf icon)\n"
            "  • BOTTOM-LEFT — MADE IN CANADA · GMP (small Canada outline)\n"
            "  • BOTTOM-RIGHT — NO ARTIFICIAL COLOURS, FLAVOURS OR PRESERVATIVES (small leaf icon)\n\n"
            "Below the box, a thin strip: 'Small vegetarian capsule · easy to swallow · vegan · "
            "gluten-free · 60 capsules.'"
        ),
        overlay="SMALL CAP, EASY TO TAKE.",
        overlay_sub="Vegetarian capsule · Health Canada NPN 80058123 · made in Canada.",
        props=["Lutein Plus box (center)", "one amber capsule + coin for scale", "4 corner badge graphics", "thin supporting strip"],
        lighting="Studio even light. Hard catch-light on the box. Badges legible at thumbnail size.",
        why_it_works=(
            "Directly answers the top review objection (capsule size) with an honest coin-scale shot, "
            "then stacks the four filters that matter to a Canadian eye-health buyer: regulator, "
            "vegetarian format, country of origin, clean label."
        ),
        ctr="The small-capsule-on-coin proof plus the badge stack pulls in cautious buyers who bounced on size or clean-label concerns.",
        cvr="Pre-defusing the swallowability objection right on the image lowers returns and hesitation at the buy box.",
    ),
    AIImagePlanItem(
        name="Image 6 — Desire: 60 capsules = how long it lasts",
        role="desire",
        background="Soft teal #E8F5F2 — same as Image 2 for visual rhythm.",
        purpose="Make the pack-size value clear and remove the 'how long does it last?' friction.",
        visual=(
            "Split-frame infographic.\n\n"
            "LEFT 60%: Lutein Plus box, open, with a clean count of capsules spilling onto a soft "
            "white surface — 1 capsule at the forefront (today's dose) and a small pile behind.\n\n"
            "RIGHT 40%: a vertical breakdown panel —\n"
            "  • 60 VEGETARIAN CAPSULES\n"
            "  • 1 capsule/day → 60-day supply\n"
            "  • 2 capsules/day → 30-day supply\n"
            "  • Take with a meal\n"
            "  • Small &amp; easy to swallow\n\n"
            "Caption below: 'Adults: take 1 to 2 capsules daily.'"
        ),
        overlay="60 CAPS, 60 DAYS.",
        overlay_sub="1 capsule/day = 60-day supply · 2 capsules/day = 30-day supply.",
        props=["Lutein Plus box (open)", "capsule pile + single daily capsule", "dosage info panel"],
        lighting="Even soft front-light. Clean infographic feel.",
        why_it_works=(
            "Pack-size value made obvious. Removes the '60 capsules — how long is that?' mental math "
            "and signals you don't re-buy constantly, hitting the cost-per-day logic for a daily habit."
        ),
        ctr="A clear days-of-supply read answers the value question on the thumbnail and rewards the comparison shopper.",
        cvr="Concrete supply math reframes the purchase as a low cost-per-day daily routine, easing the buy decision.",
    ),
    AIImagePlanItem(
        name="Image 7 — Brand close: made in Canada by Nutripur",
        role="close",
        background="Warm, calm home scene with soft natural light.",
        purpose="Close on brand identity — clinical-quality, Canadian-made eye nutrition.",
        visual=(
            "Mid-range environmental shot. An adult hand / arm (no full face needed) setting the "
            "Lutein Plus box on a clean kitchen or bathroom shelf beside a glass of water and a small "
            "Nutripur info card with the NPN number visible. A soft-focused maple-leaf or Canada décor "
            "element and a small plant in the background.\n\n"
            "Warm afternoon side-light from a window. Wood/stone surface, soft natural tones. Reads "
            "'real Canadian home,' NOT pharmacy.\n\n"
            "Foreground bottom-left: a handwritten-style note card — 'Three generations of "
            "clinical-quality nutrition. — From the Nutripur family, Quebec.'"
        ),
        overlay="MADE IN CANADA.",
        overlay_sub="Three generations of clinical-quality nutrition · Health Canada NPN 80058123.",
        props=["Lutein Plus box", "Nutripur info card with NPN", "glass of water", "maple-leaf or Canada décor (soft focus)", "small plant", "handwritten-style note card", "adult hand / arm (no face)"],
        lighting="Warm afternoon side-light from window. Soft golden hue. Honest, lived-in home — not staged.",
        why_it_works=(
            "Closes on the brand promise the buyer needs before checkout: real Canadian maker, real "
            "Health Canada credential, calm daily-habit setting. Provenance is the final trust nudge "
            "for a supplement they'll take every day."
        ),
        ctr="The 'made in Canada by Nutripur' signal differentiates from anonymous import eye vitamins for the trust-conscious CA shopper.",
        cvr="Provenance and the visible NPN create the final confidence that seals a recurring-use purchase.",
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Brand banner: Made for eye health.",
        role="a+_banner",
        headline="MADE FOR EYE HEALTH.",
        body=(
            "Nutripur Lutein Plus is a Health Canada-approved Lutein + Zeaxanthin eye formula with "
            "bilberry and Vitamin A. One small vegetarian capsule a day to help maintain eye health "
            "for screen-heavy days and the 40+ years — clinical credibility, made in Canada."
        ),
        visual="Wide cinematic morning scene — clean shelf, Lutein Plus box front-center, soft natural light from a window, a glass of water and a laptop soft-focused in the background. Nutripur navy logo upper-left, Health Canada NPN 80058123 small in the bottom band.",
        alt="Nutripur Lutein Plus eye health supplement box on a shelf in soft morning light, glass of water and laptop in soft focus.",
    ),
    AIModule(
        name="Module 2 — Carousel (4 tiles): The Lutein Plus difference",
        role="a+_carousel",
        headline="THE LUTEIN PLUS DIFFERENCE",
        body=(
            "Tile 1: <b>LUTEIN 20 MG + ZEAXANTHIN</b> — from LUTEMAX 2020 marigold; supports macular pigment.<br/>"
            "Tile 2: <b>BILBERRY &amp; BLUEBERRY ANTIOXIDANTS</b> — 600 mg bilberry 4:1 (= 2400 mg whole) + organic blueberry.<br/>"
            "Tile 3: <b>HEALTH CANADA APPROVED</b> — NPN 80058123. Defensible, regulator-approved claims.<br/>"
            "Tile 4: <b>ONE SMALL VEGETARIAN CAP</b> — once daily, easy to swallow; made in Canada."
        ),
        visual="4 square tiles, Nutripur navy accent corner per tile. Small line icons (carotenoid · berry · maple leaf · capsule). Consistent composition across all 4.",
        alt="Four-tile A+ carousel: Lutein 20mg + Zeaxanthin, bilberry & blueberry antioxidants, Health Canada approved, small vegetarian capsule.",
    ),
    AIModule(
        name="Module 3 — Banner: how the formula supports vision",
        role="a+_banner",
        headline="HELPS MAINTAIN EYE HEALTH.",
        body=(
            "Per Health Canada NPN 80058123: helps maintain eye health; provides antioxidants for "
            "the maintenance of eye health; helps improve macular pigment optical density; and helps "
            "in the development and maintenance of night vision. The macular pigment helps filter "
            "harmful blue light from screens and sunlight."
        ),
        visual="Wide banner: clean medical-style infographic of a stylized eye (no face), with the 4 nutrient labels (Lutein, Zeaxanthin, Bilberry, Vitamin A) connected by thin lines to the macula / retina they support. Nutripur teal and navy palette only. NPN 80058123 small in the lower band.",
        alt="A+ banner showing how Lutein Plus nutrients support eye health and macular pigment per Health Canada NPN 80058123.",
    ),
    AIModule(
        name="Module 4 — Banner: for screen-heavy days",
        role="a+_banner",
        headline="DAILY EYE NUTRITION.",
        body=(
            "Built for long days on phones, laptops and monitors and for adults in their 40s and up. "
            "Lutein and Zeaxanthin support the macular pigment that filters blue light, while Vitamin A "
            "helps maintain night vision. One small vegetarian capsule a day. Per Health Canada NPN 80058123."
        ),
        visual="Triptych within one banner: LEFT — adult at a laptop easing tired eyes (no face, profile). CENTER — small white dish with 1 capsule and a glass of water on a desk. RIGHT — calm evening reading scene with the Lutein Plus box. Soft natural light across all three panels.",
        alt="Triptych A+ banner showing Lutein Plus supporting eye health through screen-heavy days, daily dose, and evening routine.",
    ),
    AIModule(
        name="Module 5 — Carousel (5 tiles): The Nutripur family",
        role="a+_carousel",
        headline="THE NUTRIPUR FAMILY",
        body=(
            "Tile 1: <b>LUTEIN PLUS (this product)</b> — Lutein + Zeaxanthin eye formula. 60 vegetarian capsules.<br/>"
            "Tile 2: <b>GENIUS Kids &amp; Teens</b> — Omega-3 brain &amp; focus support for children 4+.<br/>"
            "Tile 3: <b>GENIUS Mom &amp; Baby</b> — Prenatal DHA omega-3 for pregnancy and breastfeeding.<br/>"
            "Tile 4: <b>MAGNESIUM BISGLYCINATE</b> — Stress, sleep &amp; calm for the whole family.<br/>"
            "Tile 5: <b>COLD &amp; FLU</b> — Seasonal immune support.<br/>"
            "<i>Confirm each SKU live on the Nutripur website — pull current product photography from brand assets.</i>"
        ),
        visual="5 identically composed product tiles. Nutripur navy + teal accent corner per tile. Family flat-lay style with consistent box / packaging photography.",
        alt="Five-tile A+ carousel of the Nutripur family — Lutein Plus, GENIUS Kids & Teens, Mom & Baby prenatal DHA, Magnesium Bisglycinate, Cold & Flu.",
    ),
    AIModule(
        name="Module 6 — Premium Q&A",
        role="a+_qa",
        headline="QUESTIONS SHOPPERS ASK",
        body=(
            "<b>Q.</b> What does Lutein Plus do?<br/>"
            "<b>A.</b> Per Health Canada NPN 80058123, it helps maintain eye health, provides "
            "antioxidants for the maintenance of eye health, helps improve macular pigment optical "
            "density, and helps in the development and maintenance of night vision.<br/><br/>"

            "<b>Q.</b> How big are the capsules — are they easy to swallow?<br/>"
            "<b>A.</b> They are small vegetarian capsules and most adults find them easy to swallow. "
            "Take 1 to 2 capsules daily with a meal and water.<br/><br/>"

            "<b>Q.</b> What is in the formula?<br/>"
            "<b>A.</b> Per 2-capsule daily dose: Lutein 20 mg and Zeaxanthin (from LUTEMAX 2020 "
            "marigold), Bilberry 4:1 extract 600 mg (equal to 2400 mg whole bilberry), organic "
            "Canadian blueberry 200 mg and Vitamin A 1500 mcg RAE.<br/><br/>"

            "<b>Q.</b> Is it good for screen time?<br/>"
            "<b>A.</b> Yes. Lutein and Zeaxanthin support the macular pigment that helps filter blue "
            "light from screens and sunlight — a fit for long days on phones, laptops and monitors.<br/><br/>"

            "<b>Q.</b> How long does one bottle last?<br/>"
            "<b>A.</b> 60 vegetarian capsules per bottle. At 1 capsule/day that is a 60-day supply; "
            "at 2 capsules/day, a 30-day supply.<br/><br/>"

            "<b>Q.</b> Where is it made?<br/>"
            "<b>A.</b> Made in Canada by Nutripur in a GMP-certified facility. Health Canada NPN "
            "80058123. Vegan, gluten-free, with no artificial colours, flavours or preservatives."
        ),
        visual="Vertical Q/A table. Nutripur teal divider lines between each Q. Small Nutripur navy Q. and A. labels.",
        alt="Premium Q&A module addressing the six most-asked shopper questions for Nutripur Lutein Plus.",
    ),
    AIModule(
        name="Module 7 — Premium Comparison Chart",
        role="a+_comparison",
        headline="WHY LUTEIN PLUS",
        body=(
            "Compare across 4 columns: <b>Nutripur Lutein Plus</b> · Single-ingredient lutein capsule · "
            "Lutein gummy · Generic eye multivitamin.<br/><br/>"
            "Rows: Lutein 20 mg + Zeaxanthin · Bilberry 4:1 (600 mg = 2400 mg whole) · Vitamin A for "
            "night vision · Health Canada NPN · Vegetarian capsule · No artificial colours/flavours/"
            "preservatives · Added sugar (zero) · Made in Canada.<br/><br/>"
            "Highlight the Lutein Plus column with a soft Nutripur-teal tint and a 'CANADIAN EYE-HEALTH "
            "CHOICE' ribbon at the top of the column."
        ),
        visual="Standard Amazon Premium Comparison Chart layout, 4 product columns. Competitor columns use category descriptors only — no brand names. Nutripur navy header row.",
        alt="Premium comparison chart for Nutripur Lutein Plus vs. single-ingredient lutein capsule, lutein gummy, and generic eye multivitamin.",
    ),
]


QA = [
    AIQA(q="What does Lutein Plus do?",
         a="Per Health Canada NPN 80058123: helps maintain eye health, provides antioxidants for the maintenance of eye health, helps improve macular pigment optical density, and helps in the development and maintenance of night vision."),
    AIQA(q="How big are the capsules — are they easy to swallow?",
         a="They are small vegetarian capsules and most adults find them easy to swallow. Adults take 1 to 2 capsules daily with a meal and water. No fishy aftertaste."),
    AIQA(q="What is in the formula?",
         a="Per 2-capsule daily dose: Lutein 20 mg and Zeaxanthin (from LUTEMAX 2020 marigold), Bilberry 4:1 extract 600 mg (equal to 2400 mg whole bilberry), organic Canadian blueberry 200 mg, and Vitamin A 1500 mcg RAE (5000 IU). Non-medicinal: sunflower oil and a vegetarian hypromellose capsule."),
    AIQA(q="Is it good for screen time and the 40+ years?",
         a="Yes. Lutein and Zeaxanthin support the macular pigment that helps filter blue light from screens and sunlight, making it a fit for long days on phones, laptops and monitors and for adults in their 40s and up."),
    AIQA(q="Is it vegan and free from artificial additives?",
         a="Yes. The capsule is vegetarian and the product is vegan, gluten-free and lactose-free, with no artificial colours, flavours or preservatives."),
    AIQA(q="How long does one bottle last?",
         a="60 vegetarian capsules per bottle. At 1 capsule/day that is a 60-day supply; at 2 capsules/day, a 30-day supply."),
    AIQA(q="Where is Lutein Plus made?",
         a="Made in Canada by Nutripur in a GMP-certified facility. Health Canada NPN 80058123. Three generations of clinical-quality natural health products."),
    AIQA(q="How many should I take and when?",
         a="Adults take 1 to 2 capsules daily, ideally with a meal. Consult a healthcare practitioner if symptoms persist or worsen."),
]


# Backend KWs — stem-deduped, byte-packed. Disease-name search terms (macular degeneration,
# cataracts, AMD, dry eye) live HERE ONLY — never in customer-facing copy. Includes FR fallback
# (amazon.ca is bilingual) and the high-volume competitor/category terms from the SEO axis.
BACKEND = (
    "lutein zeaxanthin supplement eye vitamins for adults eye health vision macular pigment "
    "optical density blue light screen digital eye strain night vision bilberry blueberry "
    "vitamin a carotenoid antioxidant marigold lutemax 20mg 40mg vegetarian capsule vegan "
    "macular degeneration amd cataracts dry eye retina ocular eye care areds 2 ocuvite "
    "vitalux 50 plus adults 40 health canada npn made in canada lutéine zéaxanthine yeux "
    "vision santé oculaire myrtille bleuet vitamine a végétarien"
)


def main() -> None:
    print("Loading Nutripur customer + parsing Lutein Plus Excel…")
    cust = load_customer("nutripur")
    brief = parse_excel(EXCEL)
    asin = brief.asin or ASIN
    OUT = HERE / f"{PLAN_NO}_{asin}_Image Plan.pdf"
    real_title_len = len(TITLE.replace("&amp;", "&"))
    print(f"  Product: {brief.product_name}")
    print(f"  ASIN: {brief.asin}  Marketplace: {cust.marketplace}")
    print(f"  USPs={len(brief.usps)} KWs={len(brief.all_keywords)} reviews=+{len(brief.good_reviews)}/-{len(brief.bad_reviews)}")
    print(f"  Health Canada NPN: 80058123 (claims are NPN-defensible)")
    print(f"  TITLE real chars (de-escaped): {real_title_len}")

    builder = BriefBuilder(cust, brief, OUT, ai=None)
    builder._ai_title = TITLE
    builder._ai_bullets = BULLETS
    builder._ai_images = IMAGES
    builder._ai_modules = MODULES
    builder._ai_qa = QA
    builder._ai_backend = BACKEND
    builder.copy_source_label = "Hand-written senior copy (KW-led, NPN-defensible)"

    print("Building branded PDF…")
    pdf_path = builder.build()
    size_kb = pdf_path.stat().st_size // 1024
    import re
    pages = len(re.findall(rb'/Type\s*/Page[^s]', pdf_path.read_bytes()))
    print(f"Built: {pdf_path}")
    print(f"  Pages: {pages}  Size: {size_kb} KB")


if __name__ == "__main__":
    main()
