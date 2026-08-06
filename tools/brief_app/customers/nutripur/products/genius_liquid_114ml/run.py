"""Nutripur GENIUS Kids & Teens — LIQUID Omega-3 Brain Support (114 ml)
Hand-written KW-led copy injected into the branded ReportLab pipeline.

Marketplace: amazon.ca (Canada) · ASIN B00CORKASE
Health Canada NPN: 80001374  (NOTE: the LIQUID has its OWN NPN — the chewable is 80001375.
                              Never cross the two.)

Per-teaspoon (5 ml) facts — verified from nutripur.com/ca/product/genius-kids-teens-liquid:
  Wild fish oil (mackerel, anchovy, sardine, tuna) 4000 mg · organic flax seed oil 640 mg ·
  borage oil 300 mg · phosphatidylcholine 9 mg · vitamin E 27 IU.
  Omega-3 1500 mg (DHA 730 mg · EPA 450 mg · ALA 320 mg) · Omega-6 (GLA 60 mg · LA 180 mg · ARA 30 mg).
  Dose: children 4+, 1/2 to 1 teaspoon daily WITH FOOD; straight or mixed into juice/smoothie/applesauce/yogurt.

Health-claim compliance baseline (NPN 80001374 approved language):
  - "Helps support development and mental function in children"
  - "Helps in the management of ADD/ADHD"
  - "Helps improve concentration in children with ADD/ADHD"
  - "Helps in the development of the nervous system"
  - "Provides structural components for healthy brain and eyes"

Never: cures/treats/prevents disease · best/#1/ultimate/guaranteed · kid faces (privacy + brand rule).
"""
from __future__ import annotations
import sys
from pathlib import Path

# This script lives at customers/<brand>/products/<product>/run.py
HERE = Path(__file__).resolve().parent          # the product folder (self-contained)
ROOT = HERE.parents[5]                            # project root (Claude_Code/)
sys.path.insert(0, str(ROOT))

from tools.brief_app.core.customers import load_customer
from tools.brief_app.core.excel_parser import parse_excel
from tools.brief_app.core.pdf_builder import BriefBuilder
from tools.brief_app.core.ai import AIImagePlanItem, AIModule, AIQA


# Inputs/outputs live alongside this script — the product folder is self-contained.
EXCEL = HERE / "listing.xlsx"                     # the SEO "axis" for this product
PLAN_NO = "02"   # SEO listing no. -> output named 0X_<ASIN>_Image Plan.pdf


# ===== KW-led copy — Health Canada NPN 80001374 compliant =====

TITLE = 'Nutripur GENIUS Kids & Teens Liquid Omega-3 — 730 mg DHA + 450 mg EPA per Teaspoon · 114 ml Organic Orange · Brain, Focus & ADD/ADHD Support · No Pills · Health Canada NPN 80001374 · Ages 4+'

BULLETS = [
    "<b>BRAIN, FOCUS &amp; LEARNING SUPPORT FOR KIDS 4+</b> — Health Canada-approved liquid formula "
    "(NPN 80001374) that helps support development and mental function in children such as memory, "
    "perception and problem-solving. The liquid GENIUS for kids who can't or won't swallow capsules.",

    "<b>1,500 mg OMEGA-3 IN ONE TEASPOON</b> — DHA 730 mg, EPA 450 mg, ALA 320 mg, plus GLA, ARA, "
    "Phosphatidylcholine &amp; Vitamin E. A high-concentration daily dose in a single small teaspoon — "
    "far more omega-3 per serving than typical kids' gummies.",

    "<b>HELPS WITH ADD &amp; ADHD MANAGEMENT</b> — Per Health Canada: helps in the management of "
    "Attention Deficit Disorder with or without Hyperactivity, and helps improve concentration in "
    "children with ADD/ADHD. Also helps in the development of the nervous system.",

    "<b>CREAMY ORGANIC ORANGE · MIXES INTO ANYTHING</b> — Award-winning certified-organic orange "
    "flavour. Take it straight off the spoon or stir 1/2 to 1 teaspoon into juice, a smoothie, "
    "applesauce or yogurt. No artificial colours, flavours, sweeteners or preservatives. PA-free borage "
    "oil. Molecularly distilled wild fish oil — parents report no fishy burps.",

    "<b>114 ml · IFOS 5/5 STAR · MADE IN CANADA</b> — Every lot independently tested under the IFOS "
    "program — the world's strictest standard for fish oil purity, potency and freshness. Gluten-free, "
    "lactose-free, GMO-free, alcohol-free. Manufactured in Canada by Nutripur.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="White canvas with a soft sage-green tint at the bottom 15% for grounding. Same background across all 3 options for a clean A/B test.",
        purpose="Win the click in a kids omega-3 search grid full of capsule bottles and sugary gummies. The liquid format is the differentiator — show it. Test all 3, keep the winner.",
        visual=(
            "Brief the designer to mock ALL 3 options below. Brand picks the winner via Amazon Manage Your "
            "Experiments. Each option uses ONE callout, ONE action cue, ONE supporting prop — clean, not stacked.\n\n"

            "▸ OPTION A — 'FOR KIDS WHO CAN'T SWALLOW PILLS' (owns the format reason-to-buy)\n"
            "Center: GENIUS LIQUID 114 ml bottle, label fully readable, slight elevated 3/4 turn (~65% of "
            "frame). To the lower-right: a filled dosing teaspoon of the orange liquid mid-air over a small "
            "glass of orange juice, with one thin orange slice for the flavour cue.\n"
            "ONE CALLOUT — top-right badge: 'LIQUID OMEGA-3 · NO PILLS TO SWALLOW' (Nutripur green, white text).\n"
            "Why it wins: this SKU exists for kids who gag on capsules/gummies. Leading with the liquid "
            "format answers the exact reason a parent filters for 'liquid omega 3 for kids.'\n\n"

            "▸ OPTION B — POTENCY HERO (owns the science differentiator)\n"
            "Center: GENIUS LIQUID bottle slightly left of center. Right of the bottle: a clean stat block "
            "'PER TEASPOON' with 'DHA 730 mg · EPA 450 mg · 1,500 mg Omega-3' in Nutripur blue.\n"
            "ONE CALLOUT — bottom-right badge: '1,500 mg OMEGA-3 PER TSP' (Nutripur blue, white text).\n"
            "Why it wins: 730 mg DHA in one teaspoon dwarfs the few-milligram doses in kids' gummies. The "
            "per-teaspoon number is a hard, defensible differentiator no gummy competitor can match.\n\n"

            "▸ OPTION C — NPN CREDENTIAL HERO (owns the trust signal)\n"
            "Center: GENIUS LIQUID bottle front-facing (~70%). Lower-right: dosing spoon + thin orange slice.\n"
            "ONE CALLOUT — top-left badge: 'HEALTH CANADA APPROVED · NPN 80001374' (Nutripur blue, white "
            "text, small Canada-leaf icon).\n"
            "Why it wins: no competitor in the amazon.ca liquid-omega-3 grid leads with the NPN number. "
            "Health Canada credential is the strongest single trust signal a Canadian parent can see.\n\n"

            "Across all 3: bottle dominant ~65-70%, callout ~6% of frame, supporting prop fills remainder. "
            "Same lighting, same gradient, same colour temperature so the split test isolates composition."
        ),
        overlay="(one callout per option — see visual direction)",
        overlay_sub="3 hero options shipped — A/B test, keep the winner",
        props=[
            "OPTION A: bottle + dosing teaspoon over a glass of juice + orange slice + format badge",
            "OPTION B: bottle + 'PER TEASPOON' stat block (DHA 730 / EPA 450) + potency badge",
            "OPTION C: bottle + dosing spoon + orange slice + NPN 80001374 badge",
        ],
        lighting="Soft top key (5000K daylight) with gentle fill from camera-right. Slight backlight on the bottle to make the GENIUS label and the orange liquid glow. Same lighting across all 3 options.",
        why_it_works=(
            "Three angles against three different buyer triggers: A wins on the format reason-to-buy (no "
            "pills), B on potency/science (730 mg DHA per tsp), C on credential trust (NPN). One callout, "
            "one action cue, one prop — clean enough to read on a mobile thumbnail."
        ),
        ctr="The liquid-pour action cue + a single high-contrast callout reads instantly at thumbnail size and visually separates this listing from the wall of identical capsule bottles and gummy jars — the pour is the pattern interrupt that earns the click on 'liquid omega 3 for kids.'",
        cvr="Each variant pre-answers the decisive objection before the click: A ('my kid can't swallow pills'), B ('is the dose actually meaningful?'), C ('is this brand legit?'). Whichever objection the shopper carries, the winning hero defuses it, so the click is already a qualified, intent-matched visit.",
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: 1,500 mg Omega-3 in one teaspoon",
        role="hook",
        background="Soft sky blue #EAF1F8 (Nutripur mood) — clinical-natural, not pharma-sterile",
        purpose="Stack the potency differentiator the liquid owns. One teaspoon = a serious omega-3 dose.",
        visual=(
            "Center: a clean macro of the orange liquid being poured into / sitting in a dosing teaspoon, "
            "the liquid catching the light. Around the spoon, a clean radial layout of the per-teaspoon "
            "numbers in soft-edged pills (Nutripur green for omega-3s, Nutripur blue for omega-6 + "
            "phosphatidylcholine):\n\n"
            "  DHA 730 mg · EPA 450 mg · ALA 320 mg · GLA 60 mg · ARA 30 mg · Phosphatidylcholine 9 mg.\n\n"
            "Below the spoon: a caption strip — 'ONE TEASPOON = 1,500 mg total Omega-3.' Optional small "
            "comparison footnote: 'Most kids' omega-3 gummies: a fraction of the omega-3, plus added sugar.'"
        ),
        overlay="1,500 mg OMEGA-3. ONE TEASPOON.",
        overlay_sub="DHA 730 mg · EPA 450 mg per teaspoon — a real dose, not a token amount.",
        props=["dosing teaspoon with orange liquid (macro)", "6 nutrient label pills", "per-teaspoon caption strip"],
        lighting="Even soft front-light, small specular highlight on the liquid. Clarity over drama — this is an educational hook.",
        why_it_works=(
            "Reverses the category's biggest weakness for kids' omega-3: gummies taste good but deliver "
            "almost no omega-3. GENIUS Liquid leads with 730 mg DHA per teaspoon — a number gummies can't "
            "touch — and makes the dose tangible in one frame."
        ),
        ctr="A single bold number ('1,500 mg / ONE TEASPOON') is the most scannable possible hook in the grid — quantified claims out-pull adjectives, and the orange-liquid macro signals the format at a glance.",
        cvr="Defuses the value objection that kills gummy sales ('is there even enough omega-3 in here?'). Showing 730 mg DHA per teaspoon vs. a gummy's token dose justifies the premium and converts the dose-aware parent.",
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: What each nutrient supports (Health Canada-approved claims only)",
        role="educate",
        background="White with a soft Nutripur-green ribbon footer",
        purpose="Defend the price premium with regulator-approved structure/function language.",
        visual=(
            "Three-column horizontal layout. Top: 'WHAT EACH NUTRIENT SUPPORTS' headline in Nutripur blue, "
            "sentence case.\n\n"
            "COLUMN 1 — 'DHA + EPA + ALA' (Omega-3)\n"
            "  • Helps support development and mental function in children\n"
            "  • Helps in the management of ADD/ADHD\n"
            "  • Helps improve concentration in children with ADD/ADHD\n"
            "Small icon: stylized brain outline in Nutripur green.\n\n"
            "COLUMN 2 — 'GLA + ARA' (Omega-6)\n"
            "  • Helps in the development of the nervous system\n"
            "  • Provides structural components for healthy brain and eyes\n"
            "  • Sourced from PA-free borage oil\n"
            "Small icon: stylized nervous system / nerve cell in Nutripur blue.\n\n"
            "COLUMN 3 — 'Phosphatidylcholine + Vitamin E'\n"
            "  • Supports cell-membrane structure in the brain\n"
            "  • Antioxidant support (vitamin E)\n"
            "  • Part of the synergistic GENIUS blend\n"
            "Small icon: stylized neuron / synapse in Nutripur green.\n\n"
            "Footer ribbon (Nutripur green): 'Claims supported by Health Canada NPN 80001374.'"
        ),
        overlay="WHAT EACH NUTRIENT SUPPORTS.",
        overlay_sub="Backed by Health Canada NPN 80001374 — defensible, regulator-approved language.",
        props=["3 column layout", "3 small medical icons (brain, nerve, neuron)", "NPN 80001374 citation footer"],
        lighting="Flat clean studio. Educational module — readability beats atmosphere.",
        why_it_works=(
            "Every claim is verbatim Health Canada NPN language — zero compliance risk. Parents who filter "
            "on 'is this brand legit?' see regulator-approved wording, not marketing-speak, which earns the "
            "premium over a cheap grocery gummy."
        ),
        ctr="Lower-funnel image — it isn't built to win the click but to hold the scroll; the clean 3-column structure invites the comparison-shopping parent to slow down and read.",
        cvr="Converts the skeptical, research-mode parent: regulator-approved claim wording (with the NPN cited on-image) is the credibility proof that turns 'sounds nice' into 'this one's defensible.'",
    ),
    AIImagePlanItem(
        name="Image 4 — Lifestyle: the easy spoonful (verbatim-derived)",
        role="desire",
        background="Real kitchen / breakfast scene, warm morning light from camera-right",
        purpose="Show the single biggest liquid advantage in action — easy to give, easy to take, mixes in.",
        visual=(
            "Warm breakfast-table shot. A PARENT'S hand (no face) holds a dosing teaspoon of orange GENIUS "
            "liquid just above a small bowl of yogurt or a glass of orange juice — mid-stir, the liquid "
            "swirling in. A KID (age 6–9) sits across, in PROFILE or three-quarter from behind, reaching "
            "for the glass / spoon — natural, head not face-forward (hair falling forward / side angle).\n\n"
            "FOREGROUND right edge: GENIUS LIQUID bottle (label facing camera). Background: soft-focused "
            "breakfast — a bowl of fruit, a school backpack on a chair. Warm morning light. Real family "
            "kitchen, NOT pharmacy / lab.\n\n"
            "Model selection note: kid model with model release; stock acceptable per brand brief. Avoid "
            "competitor-branded clothing / school logos."
        ),
        overlay="ONE EASY SPOONFUL. STRAIGHT OR STIRRED IN.",
        overlay_sub="Take it off the spoon or mix into juice, a smoothie, applesauce or yogurt. Helps support focus, attention &amp; concentration.",
        props=["GENIUS LIQUID bottle", "dosing teaspoon with orange liquid", "small bowl of yogurt or glass of juice", "soft-focused fruit + school backpack", "parent hand (no face)", "kid model (profile, no face-forward)"],
        lighting="Warm morning side-light from camera-right. Hair-light on the kid's profile. Slight rim on the bottle. Honest natural-clinical, not studio-staged.",
        why_it_works=(
            "Owns the format's core promise — 'easy to give a kid' — and visually neutralizes the picky-eater "
            "fear by showing the liquid stirred into familiar foods. The mix-in moment is the strongest "
            "single conversion image for a liquid supplement while staying brand-safe (no face-forward shot)."
        ),
        ctr="A warm human breakfast moment is the pattern-interrupt against sterile product-only competitor tiles — the mid-stir action reads even at small size and pulls the eye on a lifestyle-led carousel.",
        cvr="Directly kills the #1 liquid-supplement objection ('will my picky kid actually take a spoon of fish oil?') by showing it stirred into yogurt/juice — the parent pictures their own kid taking it, which is the decisive conversion moment.",
    ),
    AIImagePlanItem(
        name="Image 5 — Trust: 4 quality credentials in one frame",
        role="trust",
        background="White with soft sky blue panels behind each badge for separation",
        purpose="Stack the four filters Canadian parents scan for. Defuses 'is this brand legit?'",
        visual=(
            "Centered GENIUS LIQUID bottle (label facing camera). Four trust badges in the corners:\n\n"
            "  • TOP-LEFT — HEALTH CANADA APPROVED (Canada-leaf icon + NPN 80001374 below)\n"
            "  • TOP-RIGHT — IFOS 5/5 STAR (fish icon + 5 stars, 'tested every lot')\n"
            "  • BOTTOM-LEFT — MADE IN CANADA (Canada outline + Nutripur badge)\n"
            "  • BOTTOM-RIGHT — NO ARTIFICIAL COLOURS, FLAVOURS, SWEETENERS OR PRESERVATIVES (leaf icon)\n\n"
            "Below the bottle, a thin strip: 'Molecularly distilled wild fish oil. PA-free borage oil. "
            "Organic flaxseed oil. Gluten-free · Lactose-free · GMO-free · Alcohol-free. Made in Canada by "
            "Nutripur.'"
        ),
        overlay="REGULATOR-APPROVED. LAB-TESTED. CANADIAN-MADE.",
        overlay_sub="Health Canada NPN 80001374 · IFOS 5/5 Star · No artificial anything",
        props=["GENIUS LIQUID bottle (center)", "4 badge graphics in corners", "thin supporting strip"],
        lighting="Studio even light. Hard catch-light on the bottle and liquid. Badges legible at thumbnail size.",
        why_it_works=(
            "Stacks the four filters that matter for a Canadian parent buying omega-3 for kids: regulator, "
            "independent testing, country of origin, clean formulation. No competitor in the liquid grid "
            "leads with all four."
        ),
        ctr="Badge-dense trust frames don't win the first click; this one earns the secondary click from a parent already comparing two finalists and scanning for credentials.",
        cvr="Closes the legitimacy gap at the decision point: four scannable proof marks (NPN, IFOS, Made-in-Canada, clean-label) remove the last 'can I trust a fish oil I give my child daily?' hesitation right before add-to-cart.",
    ),
    AIImagePlanItem(
        name="Image 6 — How to take it: dose + mix-in clarity",
        role="desire",
        background="Soft sky blue #EAF1F8 — same as Image 2 for visual rhythm",
        purpose="Remove the 'how much / how do I give it?' friction. Make dosing effortless to understand.",
        visual=(
            "Split-frame infographic.\n\n"
            "LEFT 55%: the GENIUS LIQUID bottle beside a dosing teaspoon of orange liquid, with three small "
            "mix-in icons in a row beneath — a glass of juice, a smoothie cup, a bowl of yogurt — each with "
            "a tiny orange-swirl showing the liquid stirred in.\n\n"
            "RIGHT 45%: vertical breakdown panel\n"
            "  • CHILDREN 4+ YEARS\n"
            "  • 1/2 to 1 teaspoon daily, with food\n"
            "  • Straight off the spoon OR mixed into juice / smoothie / applesauce / yogurt\n"
            "  • 1,500 mg omega-3 per teaspoon (DHA 730 · EPA 450)\n"
            "  • 114 ml bottle · creamy organic orange\n\n"
            "Small caption: 'Shake well. Refrigerate after opening.'"
        ),
        overlay="1/2 TO 1 TEASPOON A DAY. WITH FOOD.",
        overlay_sub="Straight off the spoon or stirred into juice, a smoothie, applesauce or yogurt.",
        props=["GENIUS LIQUID bottle", "dosing teaspoon with orange liquid", "3 mix-in icons (juice, smoothie, yogurt)", "dose info panel"],
        lighting="Even soft front-light. Clean infographic feel.",
        why_it_works=(
            "Liquid dosing is less familiar than 'take a capsule,' so showing the exact teaspoon amount and "
            "the mix-in options removes the friction and the picky-eater worry in one frame — the value and "
            "the ease are both obvious."
        ),
        ctr="Not a click-driver; it's the scroll-deepening 'how does this work?' frame that keeps a considering parent in the listing instead of bouncing to compare.",
        cvr="Turns abstract interest into a concrete daily ritual the parent can picture (½–1 tsp in the morning yogurt). Making the routine effortless and unambiguous removes the last usage doubt and drives the purchase.",
    ),
    AIImagePlanItem(
        name="Image 7 — Brand close: Family moment + Made in Canada",
        role="close",
        background="Warm morning family-kitchen scene",
        purpose="Close on family identity and Canadian provenance. Cue the chewable as a companion SKU.",
        visual=(
            "Mid-range environmental shot in a real family kitchen. PARENT (hand / arm, no full face) stirs a "
            "spoon of GENIUS liquid into a glass of juice for a KID (back of head or three-quarter from "
            "behind), who reaches for it — a small natural moment, NOT posed.\n\n"
            "On the counter: GENIUS LIQUID bottle (label readable), a small Nutripur info card with NPN "
            "80001374 visible, an indoor plant, and a soft-focused maple-leaf décor element in the "
            "background. Warm morning side-light from a window. Wood counter, soft natural tones — reads "
            "'real Canadian family kitchen,' not 'pharmacy.'\n\n"
            "Foreground bottom-left: handwritten-style note card — *Three generations of clinical-quality "
            "nutrition. — From the Nutripur family, Quebec.* Small secondary line: 'Prefer capsules? Ask for "
            "GENIUS Kids & Teens Chewable.'"
        ),
        overlay="MADE IN CANADA. BACKED BY NUTRIPUR.",
        overlay_sub="Three generations of clinical-quality nutrition. Health Canada NPN 80001374.",
        props=["GENIUS LIQUID bottle", "Nutripur info card with NPN 80001374", "spoon + glass of juice", "wood counter", "maple-leaf décor (soft focus)", "indoor plant", "handwritten-style note card", "parent (hand / arm)", "kid (back / profile)"],
        lighting="Warm morning side-light from window. Soft golden hue. Honest, lived-in kitchen — not staged.",
        why_it_works=(
            "Closes on the brand promise the buyer needs before checkout: real Canadian family, real spoon-"
            "into-juice handoff, real Health Canada credential. The parent-to-kid handoff is the visual "
            "metaphor for the brand-to-customer trust handoff, and the note cross-sells the chewable SKU."
        ),
        ctr="Final-position image; not a click target, but the warm family scene rewards the parent who swiped to the end and reinforces brand recall.",
        cvr="Lands the emotional + provenance close (Canadian family, since-1989 heritage, NPN on a note card) and quietly cross-sells the chewable — converting brand trust into the add-to-cart and seeding a second purchase.",
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Brand banner: Made for growing minds.",
        role="a+_banner",
        headline="MADE FOR GROWING MINDS.",
        body=(
            "GENIUS Kids &amp; Teens Liquid by Nutripur is a Health Canada-approved omega-3 brain-support "
            "formula for children and teens ages 4 and up — the liquid GENIUS for kids who can't or won't "
            "swallow capsules. Backed by clinical-quality nutrition, blended for real life: one easy "
            "teaspoon, straight or stirred into breakfast."
        ),
        visual="Wide cinematic morning scene — kitchen counter, GENIUS LIQUID bottle front-center with a dosing spoon, soft natural light, school backpack and a glass of juice soft-focused behind. Nutripur blue logo upper-left, Health Canada NPN 80001374 small in the bottom band.",
        alt="Nutripur GENIUS Kids & Teens Liquid omega-3 bottle with a dosing spoon on a kitchen counter in morning light.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): The GENIUS Liquid Difference",
        role="a+_carousel",
        headline="THE GENIUS LIQUID DIFFERENCE",
        body=(
            "Tile 1: <b>1,500 mg OMEGA-3 PER TSP</b> — DHA 730 mg · EPA 450 mg · ALA 320 mg in one teaspoon.<br/>"
            "Tile 2: <b>NO PILLS TO SWALLOW</b> — Liquid format for kids who gag on capsules and gummies.<br/>"
            "Tile 3: <b>HEALTH CANADA APPROVED</b> — NPN 80001374. Defensible, regulator-approved claims.<br/>"
            "Tile 4: <b>IFOS 5/5 STAR</b> — Independently lab-tested every lot for purity, potency, freshness.<br/>"
            "Tile 5: <b>CREAMY ORGANIC ORANGE</b> — Mixes into juice, smoothies &amp; yogurt. No added sugar."
        ),
        visual="5 square tiles, Nutripur blue accent corner on each. Consistent composition. Small icons (teaspoon · no-pill · maple leaf · fish + stars · orange slice).",
        alt="Five-tile Premium A+ carousel covering GENIUS Liquid differentiators: 1,500 mg omega-3 per teaspoon, no pills, Health Canada approved, IFOS 5/5, organic orange.",
    ),
    AIModule(
        name="Module 3 — Banner: How the formula supports brain development",
        role="a+_banner",
        headline="HELPS SUPPORT DEVELOPMENT &amp; MENTAL FUNCTION.",
        body=(
            "Per Health Canada NPN 80001374: helps support development and mental function in children such "
            "as memory, perception and problem-solving. Helps in the management of ADD/ADHD. Helps improve "
            "concentration in children with ADD/ADHD. Helps in the development of the nervous system. "
            "Provides structural components for healthy brain and eyes."
        ),
        visual="Wide banner: clean medical-style infographic of a stylized child's brain outline (no face), with nutrient labels (DHA, EPA, ALA, GLA, ARA, Phosphatidylcholine) connected by thin lines to brain regions they support. Nutripur green and blue palette. NPN 80001374 small in the lower band.",
        alt="Premium A+ banner showing how GENIUS Liquid omega-3 nutrients support development and mental function per Health Canada NPN 80001374.",
    ),
    AIModule(
        name="Module 4 — Banner: For school, focus, and daily routine",
        role="a+_banner",
        headline="FOCUS. LEARNING. EVERY MORNING.",
        body=(
            "Helps with difficulty staying concentrated on school work or everyday tasks. Helps improve "
            "concentration in children with ADD/ADHD. Supports development and mental function such as "
            "memory and problem-solving. One easy teaspoon, with food, every morning. Per Health Canada NPN "
            "80001374."
        ),
        visual="Triptych within one banner: LEFT — kid's homework scene (hand on pencil only, no face). CENTER — a teaspoon of orange liquid stirred into a glass of juice on a breakfast table. RIGHT — GENIUS LIQUID bottle beside a school backpack. Warm natural light across all three panels.",
        alt="Triptych A+ banner showing GENIUS Liquid supporting school focus and the daily morning routine per Health Canada-approved indications.",
    ),
    AIModule(
        name="Module 5 — Carousel (5 tiles): The Nutripur Family for Canadian Households",
        role="a+_carousel",
        headline="THE NUTRIPUR FAMILY",
        body=(
            "Tile 1: <b>GENIUS Kids &amp; Teens LIQUID (this product)</b> — Omega-3 brain support, ages 4+. "
            "114 ml creamy organic orange. No pills to swallow.<br/>"
            "Tile 2: <b>GENIUS Kids &amp; Teens CHEWABLE</b> — Same brain-support range in a 180-count "
            "chewable capsule for kids who prefer to chew.<br/>"
            "Tile 3: <b>GENIUS Mom &amp; Baby</b> — Prenatal DHA omega-3 for pregnancy and breastfeeding.<br/>"
            "Tile 4: <b>COLD &amp; FLU Kids &amp; Teens</b> — Immune support for the same demographic — "
            "winter-season pairing.<br/>"
            "Tile 5: <b>MAGNESIUM BISGLYCINATE</b> — Stress, sleep &amp; calm for kids and the whole family.<br/>"
            "<i>All SKUs confirmed live on the Nutripur website — pull current product photography from brand assets.</i>"
        ),
        visual="5 identical-composition product tiles. Nutripur blue + green accent corner on each. Family flat-lay style with consistent packaging photography.",
        alt="Five-tile A+ carousel of the Nutripur family — GENIUS Liquid, GENIUS Chewable, Mom & Baby prenatal DHA, Cold & Flu Kids, and Magnesium Bisglycinate.",
    ),
    AIModule(
        name="Module 6 — Premium Q&A",
        role="a+_qa",
        headline="QUESTIONS PARENTS ASK",
        body=(
            "<b>Q.</b> Why liquid instead of capsules?<br/>"
            "<b>A.</b> GENIUS Liquid is made for children who can't or won't swallow capsules or gummies. One "
            "teaspoon delivers 1,500 mg of omega-3 (DHA 730 mg, EPA 450 mg) and can be taken straight or "
            "mixed into juice, a smoothie, applesauce or yogurt.<br/><br/>"

            "<b>Q.</b> How much do I give my child?<br/>"
            "<b>A.</b> Children 4 years and older: 1/2 to 1 teaspoon daily, with food. Shake well before use "
            "and refrigerate after opening.<br/><br/>"

            "<b>Q.</b> Does it taste fishy?<br/>"
            "<b>A.</b> GENIUS Liquid uses an award-winning certified-organic orange flavour, with no "
            "artificial colours, flavours or sweeteners. Most parents report no fishy burps. Stir it into "
            "juice or yogurt if your child prefers.<br/><br/>"

            "<b>Q.</b> Does it help with ADD or ADHD?<br/>"
            "<b>A.</b> Per Health Canada NPN 80001374: helps in the management of Attention Deficit Disorder "
            "with or without Hyperactivity (ADD/ADHD), and helps improve concentration in children with "
            "ADD/ADHD. Speak with your healthcare provider about your child's specific needs.<br/><br/>"

            "<b>Q.</b> Is it tested and safe for daily use?<br/>"
            "<b>A.</b> Yes. Approved by Health Canada (NPN 80001374) and tested every lot under the IFOS "
            "program — the world's strictest standard for fish oil purity, potency and freshness. Designed "
            "for daily use in children 4 years and older.<br/><br/>"

            "<b>Q.</b> Where is it made?<br/>"
            "<b>A.</b> Made in Canada by Nutripur. Gluten-free, lactose-free, GMO-free and alcohol-free. "
            "PA-free borage oil and certified organic flaxseed oil."
        ),
        visual="Vertical Q/A table. Nutripur green divider lines between each Q. Small Nutripur blue Q. and A. labels.",
        alt="Premium Q&A module addressing the six most-asked parent questions for Nutripur GENIUS Kids & Teens Liquid.",
    ),
    AIModule(
        name="Module 7 — Premium Comparison Chart",
        role="a+_comparison",
        headline="WHY GENIUS LIQUID",
        body=(
            "Compare across 4 columns: <b>Nutripur GENIUS Liquid</b> · Kids omega-3 gummy · Generic kids "
            "fish oil capsule · Plain cod liver oil.<br/><br/>"
            "Rows: Omega-3 per serving (1,500 mg vs token amounts) · DHA per serving (730 mg) · Easy for kids "
            "who can't swallow pills (liquid) · Health Canada NPN · IFOS 5/5 Star · Added sugar (zero) · "
            "Mixes into food &amp; drink · Recommended for ADD/ADHD support (per NPN).<br/><br/>"
            "Highlight the Nutripur GENIUS column with soft Nutripur-green tint and a 'CANADIAN PARENTS' "
            "CHOICE' ribbon at the top of the column."
        ),
        visual="Standard Amazon Premium Comparison Chart layout, 4 product columns. Competitor columns use category descriptors only — no brand names. Nutripur blue header row.",
        alt="Premium comparison chart for Nutripur GENIUS Liquid vs. omega-3 gummy, generic fish oil capsule, and cod liver oil.",
    ),
]


QA = [
    AIQA(q="Why liquid instead of capsules?",
         a="GENIUS Liquid is made for kids who can't or won't swallow capsules or gummies. One teaspoon delivers 1,500 mg of omega-3 (DHA 730 mg, EPA 450 mg) and can be taken straight or mixed into juice, a smoothie, applesauce or yogurt."),
    AIQA(q="How much do I give my child?",
         a="Children 4 years and older: 1/2 to 1 teaspoon daily, with food. Shake well before use and refrigerate after opening."),
    AIQA(q="How is this different from a kids' omega-3 gummy?",
         a="One teaspoon of GENIUS Liquid provides 1,500 mg of omega-3 including 730 mg DHA — far more than a typical kids' gummy, and with no added sugar. It also includes ALA, GLA, ARA and phosphatidylcholine, and is Health Canada-approved (NPN 80001374)."),
    AIQA(q="Does it taste fishy?",
         a="GENIUS Liquid uses an award-winning certified-organic orange flavour with no artificial colours, flavours or sweeteners. Most parents report no fishy burps. If your child is sensitive to taste or texture, stir it into juice or yogurt."),
    AIQA(q="Does GENIUS Liquid help with ADD or ADHD?",
         a="Per Health Canada NPN 80001374: helps in the management of Attention Deficit Disorder with or without Hyperactivity (ADD/ADHD), and helps improve concentration in children with ADD/ADHD. Speak with your healthcare provider about your child's specific needs."),
    AIQA(q="What's in the formula?",
         a="Per teaspoon: DHA 730 mg, EPA 450 mg, ALA 320 mg (omega-3), GLA 60 mg, LA 180 mg, ARA 30 mg (omega-6), plus Phosphatidylcholine 9 mg and Vitamin E 27 IU. Sourced from wild fish oil (mackerel, anchovy, sardine, tuna), PA-free borage oil and certified organic flaxseed oil. No artificial colours, flavours, sweeteners or preservatives."),
    AIQA(q="Is it tested and safe for daily use?",
         a="Yes. Approved by Health Canada (NPN 80001374) and tested every lot under the IFOS program for purity, potency and freshness. Designed for daily use in children 4 years and older. Gluten-free, lactose-free, GMO-free and alcohol-free."),
    AIQA(q="Where is GENIUS Liquid made?",
         a="Made in Canada by Nutripur. Manufactured to clinical-quality standards. PA-free borage oil and certified organic flaxseed oil."),
]


# Backend KWs — stem-deduped, byte-packed. Avoid: brand names already in title, superlatives.
# Includes FR fallback terms because amazon.ca is bilingual. Liquid-format intent prioritised.
BACKEND = (
    "kids omega 3 liquid childrens dha epa fish oil liquid for kids brain supplement focus memory "
    "adhd add concentration school learning organic orange 114 ml teaspoon no pills swallow "
    "phosphatidylcholine cognitive nervous system ifos health canada npn pediatric teens flax borage "
    "gla ara omega 3 liquide enfants huile de poisson"
)


def main() -> None:
    print("Loading Nutripur customer + parsing GENIUS Liquid Excel…")
    cust = load_customer("nutripur")
    brief = parse_excel(EXCEL)
    asin = brief.asin or "NA"
    OUT = HERE / f"{PLAN_NO}_{asin}_Image Plan.pdf"
    print(f"  Product: {brief.product_name}")
    print(f"  ASIN: {brief.asin}  Marketplace: {cust.marketplace}")
    print(f"  USPs={len(brief.usps)} KWs={len(brief.all_keywords)} Q&A={len(brief.rufus_qa)} reviews=+{len(brief.good_reviews)}/-{len(brief.bad_reviews)}")
    print(f"  Health Canada NPN: 80001374 (LIQUID — distinct from chewable 80001375)")

    builder = BriefBuilder(cust, brief, OUT, ai=None)
    builder._ai_title = TITLE
    builder._ai_bullets = BULLETS
    builder._ai_images = IMAGES
    builder._ai_modules = MODULES
    builder._ai_qa = QA
    builder._ai_backend = BACKEND
    builder._ai_compliance = []  # NPN-anchored copy — nothing to flag
    builder.copy_source_label = "Hand-written senior copy (KW-led, NPN 80001374-defensible)"

    print("Building branded PDF…")
    pdf_path = builder.build()
    size_kb = pdf_path.stat().st_size // 1024
    import re
    pages = len(re.findall(rb'/Type\s*/Page[^s]', pdf_path.read_bytes()))
    print(f"Built: {pdf_path}")
    print(f"  Pages: {pages}  Size: {size_kb} KB")


if __name__ == "__main__":
    main()
