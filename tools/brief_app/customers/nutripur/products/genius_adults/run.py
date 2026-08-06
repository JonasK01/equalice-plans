"""Nutripur GENIUS Cognitive Health Formula (Adult) — Liquid Omega-3 Brain Support
Hand-written KW-led copy injected into the branded ReportLab pipeline.

Marketplace: amazon.ca (Canada)
Health Canada NPN: 80070546 — THIS adult product's own NPN (kids chewable = 80001375,
kids liquid = 80001374 — never reused here).

Health-claim compliance baseline (NPN 80070546 approved, VERBATIM):
  - "Helps to support and maintain brain functions such as memory, perception and problem solving"
  - "Helps improve concentration in people suffering from ADD/ADHD"
  - "Helps support and maintain eye function and eye health"
  - "Helps maintain cardiovascular health"

Never:
  - Cure / treat / prevent disease
  - Better than [competitor]
  - Best / #1 / ultimate / guaranteed
  - "$", prices, URLs / ".com" / external links (write "the Nutripur website")
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


# ===== KW-led copy — Health Canada NPN 80070546 compliant =====

TITLE = (
    "Nutripur GENIUS Liquid Omega-3 Fish Oil for Adults — 1500 mg Omega-3 per tsp · DHA 730 · EPA 450 "
    "· Memory Focus Eye &amp; Heart · 114 ml Orange · Health Canada NPN 80070546 · IFOS 5/5 · Made in Canada"
)

BULLETS = [
    "<b>1500 MG OMEGA-3 PER TEASPOON — ADULT BRAIN SUPPORT</b> — Health Canada-approved liquid formula "
    "(NPN 80070546) that helps to support and maintain brain functions such as memory, perception and "
    "problem solving. Each teaspoon delivers DHA 730 mg, EPA 450 mg and ALA 320 mg from wild fish oil.",

    "<b>HELPS WITH FOCUS &amp; CONCENTRATION (ADD/ADHD)</b> — Per Health Canada NPN 80070546: helps improve "
    "concentration in people suffering from ADD/ADHD. A high-DHA omega-3 designed for adults who want steady "
    "focus through long workdays, study sessions and demanding routines.",

    "<b>FOUR BENEFITS IN ONE LIQUID — BRAIN, EYES &amp; HEART</b> — One formula helps support and maintain "
    "eye function and eye health, and helps maintain cardiovascular health, alongside its brain-support "
    "claims. The synergistic blend pairs wild fish oil with organic flaxseed and borage oils plus "
    "phosphatidylcholine.",

    "<b>CREAMY ORANGE LIQUID — NO FISHY AFTERTASTE, NO PILLS</b> — A liquid means flexible dosing and no "
    "large capsules to swallow. Natural creamy organic orange flavour with certified organic stevia. "
    "Alcohol-free, lactose-free, gluten-free, GMO-free, with no artificial colours or preservatives.",

    "<b>114 ML · IFOS 5/5 STAR · MADE IN CANADA</b> — Adults take 1 to 3 teaspoons daily with food. Every lot "
    "is independently tested under the IFOS program — the world-class standard for fish oil purity, potency "
    "and freshness — and earns the highest 5/5 star rating. Manufactured in Canada by Nutripur.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="White canvas with a soft teal tint (Nutripur #E8F5F2) at the bottom 15% for grounding. Same background across all 3 options for a clean A/B test.",
        purpose="Win the click in a search grid full of look-alike omega-3 bottles. Test all 3, keep the winner.",
        visual=(
            "Brief the designer to mock ALL 3 options below. Brand picks the winner via Amazon Manage Your "
            "Experiments. Each option uses ONE callout, ONE action cue, ONE supporting prop — clean, not stacked.\n\n"

            "▸ OPTION A — NPN CREDENTIAL HERO (owns the trust signal)\n"
            "Center: GENIUS adult 114 ml bottle front-facing, label fully readable, slight elevated 3/4 turn. "
            "Bottle occupies ~70% of frame. Lower-right: a filled teaspoon of the golden-orange liquid resting "
            "on a small white dish, with a thin slice of fresh orange peel for the flavour cue.\n"
            "ONE CALLOUT — top-right corner badge: 'HEALTH CANADA APPROVED · NPN 80070546' "
            "(Nutripur teal background, white text, small Canada-leaf icon).\n"
            "Why it wins: no competitor in the amazon.ca omega-3 grid leads with the NPN number visible. The "
            "Health Canada credential is the strongest single trust signal a Canadian shopper can read before "
            "clicking.\n\n"

            "▸ OPTION B — POTENCY HERO (defuses 'is this strong enough?' confusion)\n"
            "Center: GENIUS bottle, label readable, slightly left of center. Right of the bottle: one full "
            "teaspoon of liquid mid-pour catching the light, a single drop falling. Soft orange slice behind.\n"
            "ONE CALLOUT — top-left corner badge: '1500 MG OMEGA-3 · DHA 730 · EPA 450 PER TSP' "
            "(Nutripur deep-blue background, white text).\n"
            "Why it wins: reviews show confusion about 'strength' / concentration. Putting the per-teaspoon "
            "mg on the hero answers the #1 numeric question before the click and out-specs vague rivals.\n\n"

            "▸ OPTION C — 4-BENEFIT POWER STACK (owns the multi-benefit differentiator)\n"
            "Center: GENIUS bottle. In a clean radial layout around it, 4 simple line-icons labelled "
            "BRAIN · FOCUS · EYES · HEART, each in a soft white halo, Nutripur teal or blue.\n"
            "ONE CALLOUT — bottom-right corner badge: '4 BENEFITS · 1 LIQUID' (Nutripur teal "
            "background, white text).\n"
            "Why it wins: most omega-3s sell a single benefit. GENIUS visibly stacks four NPN-supported "
            "benefits, reframing 'good but similar to others' into a clear reason to pick this one.\n\n"

            "Across all 3: bottle dominant ~70%, callout ~6% of frame, supporting prop fills the remainder. "
            "Same lighting, background gradient and colour temperature so the split test isolates "
            "composition, not light or colour."
        ),
        overlay="(one callout per option — see visual direction)",
        overlay_sub="3 hero options shipped — A/B test, keep the winner",
        props=[
            "OPTION A: bottle + filled teaspoon on white dish + orange peel + NPN badge",
            "OPTION B: bottle + teaspoon mid-pour with falling drop + orange slice + potency badge",
            "OPTION C: bottle + 4 benefit icons in radial halo + multi-benefit badge",
        ],
        lighting="Soft top key (5000K daylight balanced) with gentle fill from camera-right. Slight backlight to make the golden-orange liquid glow and the GENIUS label pop. Same lighting across all 3 options to keep the A/B test clean.",
        why_it_works=(
            "Three angles against three different buyer triggers: A wins on credential trust (NPN), B wins on "
            "strength/concentration confusion, C wins on multi-benefit differentiation. One callout, one action "
            "cue, one prop each — clean enough to read on a mobile thumbnail."
        ),
        ctr=(
            "Three thumbnail-legible angles against three different click triggers: A leads with the Health "
            "Canada NPN number (no rival shows it), B leads with the per-teaspoon mg potency that answers the "
            "'strong enough?' question, C leads with the 4-benefit stack. One callout, one action cue, one prop "
            "each — reads cleanly at mobile size."
        ),
        cvr=(
            "Each hero pre-answers a documented buyer hesitation: credential trust (A), strength/concentration "
            "confusion from reviews (B), and 'good but similar to others' low-differentiation (C). The winning "
            "frame carries that reassurance straight into the detail page."
        ),
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: 1500 mg Omega-3 in one teaspoon",
        role="hook",
        background="Soft teal #E8F5F2 (Nutripur mood) — clinical-natural, not pharma-sterile",
        purpose="Make the per-teaspoon potency impossible to miss. The numeric hook vague rivals can't match.",
        visual=(
            "Center: a clean macro of a single brimming teaspoon of the golden-orange GENIUS liquid, a soft "
            "highlight running across the surface. Behind the spoon, a tidy infographic stack of the "
            "per-teaspoon numbers in Nutripur teal/blue pills: DHA 730 mg · EPA 450 mg · ALA 320 mg · GLA 60 mg. "
            "Thin connector lines from each pill toward the spoon, like a clean medical diagram.\n\n"
            "Bottom caption strip: 'Per teaspoon — 1500 mg total Omega-3 from wild fish oil, organic flaxseed "
            "oil and borage oil.' The 114 ml bottle sits small, lower-left, label readable."
        ),
        overlay="1500 MG OMEGA-3. ONE TEASPOON.",
        overlay_sub="DHA 730 mg · EPA 450 mg · ALA 320 mg per teaspoon — high-DHA liquid for adults.",
        props=["brimming teaspoon of liquid (macro)", "4 nutrient mg pills", "thin connector lines (infographic style)", "114 ml bottle (small, lower-left)"],
        lighting="Even soft front-light with a single specular highlight on the liquid. Clarity over drama — this is an educational hook.",
        why_it_works=(
            "Reverses the category default: rivals sell vague 'omega-3', GENIUS owns the exact per-teaspoon "
            "potency (1500 mg, DHA 730 / EPA 450). Educates and differentiates in one defensible frame."
        ),
        ctr=(
            "Leads with the exact number a shopper scans for — 1500 mg per teaspoon — instead of a vague "
            "'omega-3' label. The macro spoon is a pattern-interrupt against rows of identical capsule bottles."
        ),
        cvr=(
            "Directly defuses the review-documented 'unclear strength / concentration' objection by showing "
            "the real per-teaspoon DHA/EPA breakdown, turning a doubt into a reason to buy."
        ),
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: what the formula supports (NPN-approved claims only)",
        role="educate",
        background="White with a soft Nutripur-teal ribbon footer",
        purpose="Earn the premium. Show four regulator-approved benefits in plain, defensible language.",
        visual=(
            "Four-quadrant layout. Top headline in Nutripur deep-blue, sentence case: 'What this formula "
            "helps support'.\n\n"
            "QUADRANT 1 — BRAIN (stylized brain line-icon, teal)\n"
            "  Helps to support and maintain brain functions such as memory, perception and problem solving.\n\n"
            "QUADRANT 2 — FOCUS (stylized focus / target line-icon, blue)\n"
            "  Helps improve concentration in people suffering from ADD/ADHD.\n\n"
            "QUADRANT 3 — EYES (stylized eye line-icon, teal)\n"
            "  Helps support and maintain eye function and eye health.\n\n"
            "QUADRANT 4 — HEART (stylized heart line-icon, blue)\n"
            "  Helps maintain cardiovascular health.\n\n"
            "Footer ribbon (Nutripur teal): 'Claims supported by Health Canada NPN 80070546.'"
        ),
        overlay="FOUR BENEFITS. ONE DAILY LIQUID.",
        overlay_sub="Brain · Focus · Eyes · Heart — backed by Health Canada NPN 80070546.",
        props=["4-quadrant layout", "4 line-icons (brain, focus, eye, heart)", "NPN citation footer ribbon"],
        lighting="Flat clean studio. Educational module — readability beats atmosphere.",
        why_it_works=(
            "Every line is verbatim Health Canada NPN-approved wording — zero compliance risk — and the "
            "four-benefit breadth (brain, focus, eyes, heart) justifies the premium over single-benefit oils."
        ),
        ctr=(
            "A scannable four-benefit grid reads instantly in the carousel and signals 'more than just fish "
            "oil', pulling the click toward the differentiated value."
        ),
        cvr=(
            "Every line is verbatim NPN-approved wording — zero compliance risk and credible to shoppers who "
            "filter for 'is this brand legit?'. The four-benefit breadth justifies the premium over a "
            "single-benefit commodity oil."
        ),
    ),
    AIImagePlanItem(
        name="Image 4 — Lifestyle: adult morning focus moment",
        role="desire",
        background="Real kitchen scene, soft natural morning light from camera-right",
        purpose="Let the adult buyer self-cast. Owns the 'easy daily routine' and 'steady focus' triggers.",
        visual=(
            "Three-quarter lifestyle shot. An adult (35–55, natural, relaxed — face allowed, looking down at "
            "the spoon, NOT staring into the camera) at a bright kitchen counter, taking a teaspoon of the "
            "GENIUS liquid as part of a calm morning routine. A glass of water and a small bowl of fruit "
            "nearby.\n\n"
            "FOREGROUND right edge: the GENIUS 114 ml bottle, label facing camera, beside a clean teaspoon and "
            "a couple of fresh orange slices for the flavour cue.\n\n"
            "Background: softly out-of-focus open laptop / notebook and reading glasses, signalling a "
            "focused workday ahead. Warm natural light. Real home kitchen, NOT a lab or pharmacy.\n\n"
            "Model note: adult model with model release, or licensed stock. Avoid competitor-branded items."
        ),
        overlay="ONE TEASPOON. STEADY DAILY FOCUS.",
        overlay_sub="A simple morning ritual — helps support memory, perception and concentration.",
        props=["GENIUS 114 ml bottle", "teaspoon", "glass of water", "fresh orange slices", "soft-focused laptop / notebook + reading glasses", "bowl of fruit", "adult model (natural, looking down)"],
        lighting="Soft natural morning side-light from camera-right. Gentle rim on the bottle and a highlight on the liquid in the spoon. Honest, lived-in, not studio-staged.",
        why_it_works=(
            "An adult-in-use morning moment lets the buyer self-cast and proves the no-pills liquid ritual is "
            "effortless — the strongest conversion image for this category and audience."
        ),
        ctr=(
            "A real adult-in-use moment stands out among sterile bottle-on-white tiles and signals 'this fits "
            "my morning', earning the curiosity click."
        ),
        cvr=(
            "Visually proves the no-pills, liquid teaspoon ritual is effortless — defusing the format / "
            "pill-size objection from reviews — while the workday cues amplify the focus benefit the buyer wants."
        ),
    ),
    AIImagePlanItem(
        name="Image 5 — Trust: 4 quality credentials in one frame",
        role="trust",
        background="White with soft teal panels behind each badge for separation",
        purpose="Stack the filters Canadian shoppers scan for. Defuses the 'is this brand legit?' check.",
        visual=(
            "Centered macro of the GENIUS 114 ml bottle (label facing camera). Four trust badges in the "
            "corners:\n\n"
            "  • TOP-LEFT — HEALTH CANADA APPROVED (Canada-leaf icon + NPN 80070546 below)\n"
            "  • TOP-RIGHT — IFOS 5/5 STAR (fish icon + 5 stars below)\n"
            "  • BOTTOM-LEFT — MADE IN CANADA (Canada outline + Nutripur badge)\n"
            "  • BOTTOM-RIGHT — NO ARTIFICIAL COLOURS OR PRESERVATIVES · GMO-FREE · GLUTEN-FREE "
            "(leaf icon)\n\n"
            "Below the bottle, a thin strip: 'Wild fish oil (mackerel, anchovy, sardine, tuna). Certified "
            "organic flaxseed and borage oils. Alcohol-free, lactose-free. Manufactured in Canada by Nutripur.'"
        ),
        overlay="REGULATOR-APPROVED. LAB-TESTED. CANADIAN-MADE.",
        overlay_sub="Health Canada NPN 80070546 · IFOS 5/5 Star · No artificial colours or preservatives",
        props=["GENIUS 114 ml bottle (center)", "4 badge graphics in corners", "thin supporting ingredient strip"],
        lighting="Studio even light. Hard catch-light on the bottle. Badges legible at thumbnail size.",
        why_it_works=(
            "Stacks the four filters a Canadian omega-3 shopper checks — regulator, independent testing, "
            "country of origin and clean formulation — in one frame no commodity rival leads with."
        ),
        ctr=(
            "Four recognisable credential badges around one bottle read as 'verified quality' at a glance and "
            "lift click-confidence in a low-trust category."
        ),
        cvr=(
            "Stacks the four filters a Canadian omega-3 shopper checks — regulator, independent testing, "
            "country of origin, clean formulation — answering 'is this legit?' before checkout."
        ),
    ),
    AIImagePlanItem(
        name="Image 6 — Dosing clarity: 114 ml = how to use it",
        role="desire",
        background="Soft teal #E8F5F2 — same as Image 2 for visual rhythm",
        purpose="Make the dose and value obvious. Removes 'how much do I take / how long does it last?' friction.",
        visual=(
            "Split-frame infographic.\n\n"
            "LEFT 60%: the open GENIUS 114 ml bottle with a teaspoon of liquid being poured, golden-orange "
            "catching the light, a soft orange slice beside it.\n\n"
            "RIGHT 40%: vertical how-to-use panel\n"
            "  • 114 ML LIQUID — flexible dosing, no pills\n"
            "  • Adults: 1 to 3 teaspoons daily with food\n"
            "  • 1 teaspoon = 1500 mg Omega-3 (DHA 730 · EPA 450)\n"
            "  • Take straight, or stir into juice or a smoothie\n"
            "  • Keep refrigerated after opening for freshness\n\n"
            "Small caption below the panel: 'Start at 1 teaspoon daily and adjust within the 1–3 teaspoon range.'"
        ),
        overlay="114 ML. 1 TO 3 TEASPOONS DAILY.",
        overlay_sub="Flexible liquid dosing — take it straight or stir into juice or a smoothie.",
        props=["GENIUS 114 ml bottle (open)", "teaspoon mid-pour", "orange slice", "how-to-use panel"],
        lighting="Even soft front-light. Clean infographic feel with one highlight on the liquid.",
        why_it_works=(
            "Spells out the simple 1–3 teaspoon dose and mixing options, removing usage uncertainty and "
            "reinforcing the no-pills convenience liquid buyers want."
        ),
        ctr=(
            "A clear how-to-use panel signals an easy, no-guesswork product and invites the click from "
            "first-time liquid-omega-3 buyers."
        ),
        cvr=(
            "Spells out the simple 1–3 teaspoon dose and mixing options, removing usage uncertainty and "
            "reinforcing the no-pills convenience that liquid buyers want."
        ),
    ),
    AIImagePlanItem(
        name="Image 7 — Brand close: Made in Canada by Nutripur",
        role="close",
        background="Warm, soft natural-light home scene",
        purpose="Close on brand trust and provenance. Lifestyle + Canadian credibility in one frame.",
        visual=(
            "Mid-range environmental shot in a bright, calm home. The GENIUS 114 ml bottle front and centre on "
            "a wood counter, label readable, beside a teaspoon, a glass of water and a small Nutripur info card "
            "showing the NPN number. A soft-focused maple-leaf décor element and an indoor plant in the "
            "background signal Canadian-made, natural-clinical — NOT pharmacy.\n\n"
            "Warm afternoon side-light from a window. Wood tones, soft natural palette.\n\n"
            "Foreground bottom-left: a handwritten-style note card reading: 'Three generations of "
            "clinical-quality nutrition. — From the Nutripur family, Quebec.'"
        ),
        overlay="MADE IN CANADA. BACKED BY NUTRIPUR.",
        overlay_sub="Three generations of clinical-quality nutrition. Health Canada NPN 80070546.",
        props=["GENIUS 114 ml bottle", "teaspoon", "glass of water", "Nutripur info card with NPN", "wood counter", "maple-leaf décor (soft focus)", "indoor plant", "handwritten-style note card"],
        lighting="Warm afternoon side-light from window. Soft golden hue. Honest, lived-in home — not staged.",
        why_it_works=(
            "Closes on brand identity: a real Canadian-home moment plus the Health Canada NPN and Made-in-Canada "
            "provenance — the final trust nudge that converts a comparison shopper."
        ),
        ctr=(
            "A warm Canadian-home brand frame closes the carousel on identity, giving hesitating shoppers a "
            "final 'this is a real, trusted brand' nudge."
        ),
        cvr=(
            "Pairs the Made-in-Canada provenance and Health Canada NPN with a human brand promise — the last "
            "reassurance that converts a comparison shopper into a buyer."
        ),
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Brand banner: Clarity, focus, every day.",
        role="a+_banner",
        headline="CLARITY AND FOCUS, EVERY DAY.",
        body=(
            "GENIUS Cognitive Health Formula by Nutripur is a Health Canada-approved liquid omega-3 for "
            "adults (NPN 80070546). One creamy orange teaspoon delivers 1500 mg of omega-3 — and helps to "
            "support and maintain brain functions such as memory, perception and problem solving."
        ),
        visual="Wide cinematic morning scene — a bright kitchen counter, GENIUS 114 ml bottle front-centre with a teaspoon and a glass of water, soft natural light from a window, a softly-focused laptop and reading glasses in the background. Nutripur logo upper-left, Health Canada NPN 80070546 small in the bottom band.",
        alt="Nutripur GENIUS Cognitive Health Formula liquid omega-3 bottle on a kitchen counter in morning light with a teaspoon and glass of water.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): The GENIUS Difference",
        role="a+_carousel",
        headline="THE GENIUS DIFFERENCE",
        body=(
            "Tile 1: <b>1500 MG OMEGA-3 PER TEASPOON</b> — DHA 730 mg · EPA 450 mg · ALA 320 mg.<br/>"
            "Tile 2: <b>FOUR BENEFITS, ONE LIQUID</b> — Brain · Focus · Eyes · Heart, per NPN 80070546.<br/>"
            "Tile 3: <b>HEALTH CANADA APPROVED</b> — NPN 80070546. Defensible, regulator-approved claims.<br/>"
            "Tile 4: <b>IFOS 5/5 STAR</b> — Independently lab-tested for purity, potency and freshness.<br/>"
            "Tile 5: <b>CREAMY ORANGE LIQUID</b> — No pills, no fishy aftertaste. Made in Canada."
        ),
        visual="5 square tiles, Nutripur teal accent corner on each. Same composition discipline across all 5. Small icons (teaspoon · 4-benefit cluster · maple leaf · fish + stars · orange slice).",
        alt="Five-tile Premium A+ carousel covering GENIUS adult differentiators: 1500 mg omega-3 per teaspoon, four benefits, Health Canada approved, IFOS 5/5, creamy orange liquid.",
    ),
    AIModule(
        name="Module 3 — Banner: Inside the formula",
        role="a+_banner",
        headline="INSIDE EVERY TEASPOON.",
        body=(
            "Per teaspoon: wild fish oil 4000 mg (mackerel, anchovy, sardine, tuna), certified organic "
            "flaxseed oil 640 mg, borage oil 300 mg, phosphatidylcholine 9 mg and vitamin E 27 IU. Total "
            "omega-3 1500 mg — DHA 730 mg, EPA 450 mg, ALA 320 mg — plus omega-6 GLA 60 mg. A synergistic "
            "blend, per Health Canada NPN 80070546."
        ),
        visual="Wide banner: a clean medical-style infographic of the liquid teaspoon with thin lines connecting to labelled mg values for each ingredient. A small soft-focus photo of orange slices and flax seeds at one edge for the natural-source cue. Nutripur teal and blue palette only. NPN 80070546 small in the lower band.",
        alt="Premium A+ banner showing the per-teaspoon ingredient and omega-3 breakdown of GENIUS Cognitive Health Formula per Health Canada NPN 80070546.",
    ),
    AIModule(
        name="Module 4 — Banner: For work, study, and daily wellness",
        role="a+_banner",
        headline="FOCUS. EYE COMFORT. HEART HEALTH.",
        body=(
            "Helps to support and maintain brain functions such as memory, perception and problem solving. "
            "Helps improve concentration in people suffering from ADD/ADHD. Helps support and maintain eye "
            "function and eye health. Helps maintain cardiovascular health. Per Health Canada NPN 80070546."
        ),
        visual="Triptych within one banner: LEFT — an adult focused at a desk (laptop, notebook, glass of water; natural, looking down). CENTER — a teaspoon of liquid being taken at a bright kitchen counter. RIGHT — a calm evening moment with the GENIUS bottle and a glass of water. Warm natural light across all three panels.",
        alt="Triptych A+ banner showing GENIUS supporting focus, eye health and cardiovascular health per Health Canada-approved indications.",
    ),
    AIModule(
        name="Module 5 — Carousel (5 tiles): The Nutripur Family",
        role="a+_carousel",
        headline="THE NUTRIPUR FAMILY",
        body=(
            "Tile 1: <b>GENIUS Cognitive Health Formula (this product)</b> — Adult liquid omega-3 brain "
            "support, 114 ml, creamy orange.<br/>"
            "Tile 2: <b>GENIUS Kids &amp; Teens CHEWABLE</b> — Omega-3 brain support for ages 4+, organic "
            "orange.<br/>"
            "Tile 3: <b>GENIUS Kids &amp; Teens LIQUID</b> — The same brain-support idea in a liquid for "
            "younger kids.<br/>"
            "Tile 4: <b>SUPER OMEGA Liquid</b> — Everyday omega-3 fish oil for whole-family wellness.<br/>"
            "Tile 5: <b>MAGNESIUM BISGLYCINATE</b> — Stress, sleep and calm for the whole family.<br/>"
            "<i>Confirm current SKUs and pull product photography from brand assets and the Nutripur website.</i>"
        ),
        visual="5 identical-composition product tiles. Nutripur teal + blue accent corner on each. Family flat-lay style with consistent bottle / packaging photography.",
        alt="Five-tile A+ carousel of the Nutripur family — GENIUS adult liquid, GENIUS Kids chewable and liquid, Super Omega liquid, and Magnesium Bisglycinate.",
    ),
    AIModule(
        name="Module 6 — Premium Q&A",
        role="a+_qa",
        headline="QUESTIONS ADULTS ASK",
        body=(
            "<b>Q.</b> How much omega-3 do I get per dose?<br/>"
            "<b>A.</b> Each teaspoon delivers 1500 mg of omega-3, including DHA 730 mg, EPA 450 mg and ALA "
            "320 mg, from wild fish oil, organic flaxseed oil and borage oil. Adults take 1 to 3 teaspoons "
            "daily with food.<br/><br/>"

            "<b>Q.</b> Does it taste fishy?<br/>"
            "<b>A.</b> Most people describe a clean, creamy organic orange flavour and report no fishy "
            "aftertaste. There are no artificial colours or preservatives, and it is sweetened with certified "
            "organic stevia. Take it straight or stir it into juice or a smoothie.<br/><br/>"

            "<b>Q.</b> Why a liquid instead of capsules?<br/>"
            "<b>A.</b> A liquid means flexible dosing and no large pills to swallow. One teaspoon already "
            "provides a high-DHA 1500 mg omega-3 dose — difficult to match without taking several capsules.<br/><br/>"

            "<b>Q.</b> Does it help with focus, ADD or ADHD?<br/>"
            "<b>A.</b> Per Health Canada NPN 80070546: helps improve concentration in people suffering from "
            "ADD/ADHD, and helps to support and maintain brain functions such as memory, perception and "
            "problem solving. Speak with your healthcare provider about your specific needs.<br/><br/>"

            "<b>Q.</b> Is it tested for purity?<br/>"
            "<b>A.</b> Yes. Every lot is independently tested under the IFOS program — a world-class standard "
            "for fish oil purity, potency and freshness — and earns the highest 5/5 star rating.<br/><br/>"

            "<b>Q.</b> Where is it made?<br/>"
            "<b>A.</b> Made in Canada by Nutripur. Health Canada NPN 80070546. Alcohol-free, lactose-free, "
            "gluten-free and GMO-free."
        ),
        visual="Vertical Q/A table. Nutripur teal divider lines between each Q. Small Nutripur blue Q. and A. labels.",
        alt="Premium Q&A module addressing the six most-asked adult questions for Nutripur GENIUS Cognitive Health Formula.",
    ),
    AIModule(
        name="Module 7 — Premium Comparison Chart",
        role="a+_comparison",
        headline="WHY GENIUS",
        body=(
            "Compare across 4 columns: <b>Nutripur GENIUS Cognitive Health Formula</b> · Standard fish oil "
            "capsule · Plain omega-3 liquid · DHA-only softgel.<br/><br/>"
            "Rows: Omega-3 per dose (1500 mg per teaspoon) · DHA content (730 mg) · Format (no-pill liquid) · "
            "Benefits supported (brain, focus, eyes, heart) · Health Canada NPN · IFOS 5/5 Star · Flavour "
            "(creamy organic orange) · Made in Canada.<br/><br/>"
            "Highlight the Nutripur GENIUS column with a soft Nutripur-teal tint and a 'CANADIAN ADULTS' "
            "CHOICE' ribbon at the top of the column."
        ),
        visual="Standard Amazon Premium Comparison Chart layout, 4 product columns. Competitor columns use category descriptors only — no brand names. Nutripur blue header row.",
        alt="Premium comparison chart for Nutripur GENIUS Cognitive Health Formula vs. standard fish oil capsule, plain omega-3 liquid and DHA-only softgel alternatives.",
    ),
]


QA = [
    AIQA(q="How much omega-3 do I get per dose?",
         a="Each teaspoon delivers 1500 mg of omega-3, including DHA 730 mg, EPA 450 mg and ALA 320 mg, from wild fish oil, organic flaxseed oil and borage oil. Adults take 1 to 3 teaspoons daily with food."),
    AIQA(q="Does it taste fishy?",
         a="Most people describe a clean, creamy organic orange flavour and report no fishy aftertaste or burping. It contains no artificial colours or preservatives and is sweetened with certified organic stevia. Take it straight or stir it into juice or a smoothie."),
    AIQA(q="Why choose a liquid instead of capsules?",
         a="A liquid means flexible dosing and no large pills to swallow. One teaspoon already provides a high-DHA 1500 mg omega-3 dose that would take several standard capsules to match."),
    AIQA(q="What benefits does it help support?",
         a="Per Health Canada NPN 80070546: helps to support and maintain brain functions such as memory, perception and problem solving; helps improve concentration in people suffering from ADD/ADHD; helps support and maintain eye function and eye health; and helps maintain cardiovascular health."),
    AIQA(q="What is in the formula?",
         a="Per teaspoon: wild fish oil 4000 mg (mackerel, anchovy, sardine, tuna), certified organic flaxseed oil 640 mg, borage oil 300 mg, phosphatidylcholine 9 mg and vitamin E 27 IU — providing 1500 mg total omega-3 (DHA 730 mg, EPA 450 mg, ALA 320 mg) plus omega-6 GLA 60 mg."),
    AIQA(q="Is it tested for purity and freshness?",
         a="Yes. Every lot is independently tested under the IFOS program — a world-class standard for fish oil purity, potency and freshness — and earns the highest 5/5 star rating."),
    AIQA(q="How long does one bottle last?",
         a="The bottle holds 114 ml. At 1 teaspoon (5 ml) daily that is roughly a three-week supply; at 3 teaspoons daily it lasts about one week. Keep refrigerated after opening for freshness."),
    AIQA(q="Where is it made?",
         a="Made in Canada by Nutripur. Health Canada NPN 80070546. Alcohol-free, lactose-free, gluten-free and GMO-free, manufactured to clinical-quality standards."),
]


# Backend KWs — stem-deduped, byte-packed. Avoid words already in the title, and superlatives.
# Includes FR fallback terms because amazon.ca is bilingual.
BACKEND = (
    "omega 3 supplements fish oil liquid adults high concentration memory brain cognitive "
    "eye dry vision heart cardiovascular adhd add flaxseed borage gla phosphatidylcholine "
    "triglyceride creamy orange ifos npn omega3 oméga huile poisson cerveau"
)


def main() -> None:
    print("Loading Nutripur customer + parsing GENIUS adult Excel…")
    cust = load_customer("nutripur")
    brief = parse_excel(EXCEL)
    asin = brief.asin or "NA"
    OUT = HERE / f"{PLAN_NO}_{asin}_Image Plan.pdf"
    print(f"  Product: {brief.product_name}")
    print(f"  ASIN: {brief.asin}  Marketplace: {cust.marketplace}")
    print(f"  USPs={len(brief.usps)} KWs={len(brief.all_keywords)} reviews=+{len(brief.good_reviews)}/-{len(brief.bad_reviews)}")
    print(f"  Health Canada NPN: 80070546 (claims are NPN-defensible)")

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
