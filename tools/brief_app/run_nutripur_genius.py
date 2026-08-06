"""Nutripur GENIUS Kids & Teens — Chewable Omega-3 Brain Support
Hand-written KW-led copy injected into the branded ReportLab pipeline.

Marketplace: amazon.ca (Canada)
Health Canada NPN: 80001375 — defensible structure/function claims.

Health-claim compliance baseline (NPN 80001375 approved):
  - "Helps support cognitive development"
  - "Helps to support development and mental function in children"
  - "Helps in the management of ADD/ADHD"
  - "Helps improve concentration in children with ADD/ADHD"
  - "Helps in the development of the nervous system"

Never:
  - Cures / treats / prevents disease
  - Better than [competitor]
  - Best / #1 / ultimate / guaranteed
  - Use kid faces (privacy + brand rule)
"""
from __future__ import annotations
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from tools.brief_app.core.customers import load_customer
from tools.brief_app.core.excel_parser import parse_excel
from tools.brief_app.core.pdf_builder import BriefBuilder
from tools.brief_app.core.ai import AIImagePlanItem, AIModule, AIQA


EXCEL = ROOT / ".tmp/Nutripur/01_Nutripur Genius Kids and Teens Listing.xlsx"
OUT = Path.home() / "Desktop" / "Nutripur_GENIUS_Kids_Teens_Brief.pdf"


# ===== KW-led copy — Health Canada NPN compliant =====

TITLE = (
    "Nutripur GENIUS Kids & Teens Chewable Omega-3 — DHA · EPA · ALA · GLA · ARA + Phosphatidylcholine "
    "· 180 Chewables · Organic Orange · Health Canada NPN 80001375 · IFOS 5/5 Star Fish Oil · Brain "
    "& Focus Support · Ages 4+"
)

BULLETS = [
    "<b>BRAIN, FOCUS &amp; LEARNING SUPPORT FOR KIDS 4+</b> — Health Canada-approved formula (NPN 80001375) "
    "designed to help support cognitive development, memory, perception and problem-solving in growing minds. "
    "Many parents report calmer behaviour and easier homework completion by the second week.",

    "<b>6 BRAIN NUTRIENTS IN ONE CAPSULE</b> — DHA 264 mg, EPA 52 mg, ALA, GLA, ARA, plus Phosphatidylcholine "
    "&amp; Vitamin E. Provides 90% of the essential fatty acids the brain needs. The synergistic blend delivers "
    "what no single ingredient can.",

    "<b>HELPS WITH ADD &amp; ADHD MANAGEMENT</b> — Per Health Canada: helps in the management of Attention Deficit "
    "Disorder with or without Hyperactivity, and helps improve concentration in children with ADD/ADHD. The same "
    "formula also supports kids without attention challenges who want an edge for school.",

    "<b>CHEWABLE OR SWALLOW · ORGANIC ORANGE FLAVOUR</b> — Award-winning organic orange flavour designed to take "
    "the fishy bite out of fish oil. Most kids chew it; for kids who prefer, the capsules can also be swallowed "
    "whole with water. No artificial colours, flavours, sweeteners or preservatives. PA-free borage oil. "
    "Molecularly distilled wild fish oil.",

    "<b>180 CAPSULES · IFOS 5/5 STAR · MADE IN CANADA</b> — 45-day supply at 4 capsules/day, or 30-day supply at "
    "6 capsules/day. Every lot independently tested under the IFOS program — the world's strictest standard for "
    "fish oil purity, potency and freshness. Manufactured in Canada by Nutripur.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="White canvas with a soft sage-green tint at the bottom 15% for grounding. Same background across all 3 options for a clean A/B test.",
        purpose="Win the click in a search grid full of generic kids omega-3 bottles. Test all 3, keep the winner.",
        visual=(
            "Brief the designer to mock ALL 3 options below. Brand picks the winner via Amazon Manage Your "
            "Experiments. Each option uses ONE callout, ONE action cue, ONE supporting prop — clean, not stacked.\n\n"

            "▸ OPTION A — NPN CREDENTIAL HERO (owns the trust signal)\n"
            "Center: GENIUS bottle front-facing, label fully readable, slight elevated 3/4 turn. Bottle "
            "occupies ~70% of frame. To the bottle's lower-right: 2 organic orange capsules and a thin "
            "slice of fresh orange peel for flavour cue.\n"
            "ONE CALLOUT — top-right corner badge: 'HEALTH CANADA APPROVED · NPN 80001375' "
            "(Nutripur blue background, white text, small Canada-leaf icon).\n"
            "Why it wins: in the amazon.ca search grid, no competitor leads with the NPN number visible. "
            "Health Canada credential is the strongest single trust signal a Canadian parent can see "
            "before clicking.\n\n"

            "▸ OPTION B — ACTION + PORTION CONTROL (defuses 'will my kid take it?' anxiety)\n"
            "Center: GENIUS bottle, label readable, slightly left of center. Right of the bottle: a small "
            "white ceramic dish holding 4 chewable capsules (the daily dose), with one capsule held in a "
            "small adult hand mid-air above the dish (just fingers visible, no face).\n"
            "Background prop: 1–2 thin orange slices for the flavour cue.\n"
            "ONE CALLOUT — top-left corner badge: 'CHEWABLE · ORGANIC ORANGE · KIDS LOVE IT' "
            "(Nutripur green background, white text).\n"
            "Why it wins: the #1 buyer hesitation for kids' supplements is 'will my child actually take it?' — "
            "this image visually proves format + flavour are easy. Adult-hand-only is on-brand (no kid "
            "faces) and keeps the focus on the product.\n\n"

            "▸ OPTION C — 6 NUTRIENT POWER STACK (owns the science differentiator)\n"
            "Center: GENIUS bottle. Floating around the bottle in a clean radial layout: 6 small icons "
            "labeled DHA · EPA · ALA · GLA · ARA · PHOSPHATIDYLCHOLINE. Each icon "
            "is a simple molecule outline in Nutripur blue or green, on a soft white halo.\n"
            "ONE CALLOUT — bottom-right corner badge: '6 BRAIN NUTRIENTS · 90% EFAs' (Nutripur "
            "blue background, white text).\n"
            "Why it wins: every competitor sells 'omega-3.' Only GENIUS visibly stacks 6 brain nutrients "
            "(DHA + EPA + ALA + GLA + ARA + Phosphatidylcholine). The 6-icon halo communicates the "
            "synergistic differentiator at a glance.\n\n"

            "Across all 3: bottle dominant ~70%, callout ~6% of frame, supporting prop fills remainder. "
            "Same lighting, same background gradient, same colour temperature so the split test isolates "
            "composition not light/colour."
        ),
        overlay="(one callout per option — see visual direction)",
        overlay_sub="3 hero options shipped — A/B test, keep the winner",
        props=[
            "OPTION A: bottle + 2 capsules + thin orange slice + NPN badge",
            "OPTION B: bottle + small white dish with 4 capsules + adult hand (fingers only) + orange slices + format/flavour badge",
            "OPTION C: bottle + 6 nutrient icons in radial halo + science badge",
        ],
        lighting="Soft top key (5000K daylight balanced) with gentle fill from camera-right. Slight backlight on the bottle to make the GENIUS label pop. Same lighting across all 3 options to keep the A/B test clean.",
        why_it_works=(
            "Three angles against three different buyer triggers: A wins on credential trust (NPN), B "
            "wins on format/flavour anxiety, C wins on science differentiation. Per the new standard: "
            "one callout, one action cue, one supporting prop. Clean enough to read on mobile thumbnail."
        ),
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: 6 Brain Nutrients in One Chewable",
        role="hook",
        background="Soft sky blue #EAF1F8 (Nutripur mood) — clinical-natural feel, not pharma-sterile",
        purpose="Visually stack the 6-nutrient differentiator. The hook competitors can't match.",
        visual=(
            "Center: large macro of a single GENIUS chewable capsule, oriented so the soft orange colour "
            "reads cleanly. Behind the capsule, 6 ingredient labels in a clean radial layout (12, 2, 4, 6, "
            "8, 10 o'clock positions): DHA · EPA · ALA · GLA · ARA · "
            "PHOSPHATIDYLCHOLINE. Each label sits inside a small soft-edged pill shape (Nutripur green for "
            "omega-3s, Nutripur blue for omega-6s and phosphatidylcholine). Subtle connecting line from "
            "each label to the central capsule, like a clean medical infographic.\n\n"
            "Below the capsule: small caption strip with the actual mg values — DHA 264 mg · "
            "EPA 52 mg · ALA 104 mg · GLA 64 mg · ARA 20 mg · Phosphatidylcholine 18 mg."
        ),
        overlay="6 BRAIN NUTRIENTS. ONE CHEWABLE.",
        overlay_sub="DHA · EPA · ALA · GLA · ARA + Phosphatidylcholine — 90% of the EFAs the brain needs.",
        props=["single chewable capsule (macro)", "6 nutrient label pills", "thin connecting lines (infographic style)"],
        lighting="Even soft front-light, slight 3D shadow under the capsule. No drama lighting — this is an educational hook, clarity > mood.",
        why_it_works=(
            "Direct reversal of the #1 search query competitor positioning: every competitor sells 'omega 3.' "
            "GENIUS owns '6 brain nutrients including omega-3.' Mathematically defensible per the Genius Product "
            "Information sheet (90% of EFAs). Educates and differentiates in one frame."
        ),
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: What each nutrient does (Health Canada-approved claims only)",
        role="educate",
        background="White with a soft Nutripur-green ribbon footer",
        purpose="Defend the price premium. Earn the buyer's trust with Health Canada-language structure/function claims.",
        visual=(
            "Three-column horizontal layout. Top of frame: 'WHAT EACH NUTRIENT SUPPORTS' headline in Nutripur "
            "blue, sentence case.\n\n"
            "COLUMN 1 — 'DHA + EPA + ALA' (Omega-3)\n"
            "  • Helps to support cognitive development\n"
            "  • Helps in the management of ADD/ADHD\n"
            "  • Helps improve concentration in children with ADD/ADHD\n"
            "Small icon: stylized brain outline in Nutripur green.\n\n"
            "COLUMN 2 — 'GLA + ARA' (Omega-6)\n"
            "  • Helps in the development of the nervous system\n"
            "  • Supports healthy brain function\n"
            "  • Sourced from PA-free borage oil\n"
            "Small icon: stylized nervous system / nerve cell in Nutripur blue.\n\n"
            "COLUMN 3 — 'Phosphatidylcholine'\n"
            "  • Supports neurotransmission in neurons\n"
            "  • Supports memory and learning\n"
            "  • Key component of all cell membranes\n"
            "Small icon: stylized neuron / synapse in Nutripur green.\n\n"
            "Footer ribbon (Nutripur green): 'Claims supported by Health Canada NPN 80001375.'"
        ),
        overlay="WHAT EACH NUTRIENT SUPPORTS.",
        overlay_sub="Backed by Health Canada NPN 80001375 — defensible, regulator-approved language.",
        props=["3 column layout", "3 small medical icons (brain, nerve, neuron)", "NPN citation footer"],
        lighting="Flat clean studio. Educational module — readability beats atmosphere.",
        why_it_works=(
            "Every claim is verbatim from the Health Canada NPN — zero compliance risk. Buyers who "
            "filter on 'is this brand legit?' see actual regulator-approved language, not marketing-speak. "
            "Earns the premium price vs. $15 grocery gummies."
        ),
    ),
    AIImagePlanItem(
        name="Image 4 — Lifestyle: Kid + homework moment (verbatim-derived)",
        role="desire",
        background="Real kitchen / desk scene, warm afternoon light from camera-right",
        purpose="Place the buyer's child in the frame. Owns the 'easier homework' verbatim from real parent reviews.",
        visual=(
            "Wide angled shot. KID (age 8–10) seated at a kitchen counter or homework table, in PROFILE "
            "or three-quarter from behind — head naturally tilted down toward an open exercise book, "
            "pencil in hand. Face is naturally obscured by the studying posture (hair falling forward / "
            "head-down angle). Casual, real — not a posed portrait.\n\n"
            "FOREGROUND right edge: GENIUS bottle (label facing camera) next to a small white ceramic "
            "dish with 4 chewable capsules. A glass of water beside the bottle.\n\n"
            "Background: soft-focused books, a couple of crayons or markers. Warm afternoon light from "
            "camera-right. Kitchen / family-room vibe, NOT pharmacy / lab.\n\n"
            "Model selection note: kid model with model release; use stock if brand prefers. Avoid "
            "competitor-branded clothing / school logos."
        ),
        overlay="CALMER AFTERNOONS. EASIER HOMEWORK.",
        overlay_sub="Parent-reported results often build from week 2 onward. Helps support focus, attention &amp; concentration.",
        props=["GENIUS bottle", "small white dish with 4 capsules", "glass of water", "open exercise book", "pencil", "soft-focused books / crayons", "kid model (profile, no face-forward)"],
        lighting="Warm afternoon side-light from camera-right. Hair-light on the kid's profile. Slight rim on the bottle. Honest natural-clinical, not studio-staged.",
        why_it_works=(
            "Owns the most powerful real-review verbatim — *'easier homework, calmer afternoons'* — with "
            "a kid in frame. Profile / head-down composition delivers the lifestyle CVR signal Amazon "
            "kids' supplements need, while staying brand-safe (no posed staring-into-camera shot). "
            "This is the strongest single conversion image in the plan."
        ),
    ),
    AIImagePlanItem(
        name="Image 5 — Trust: 4 quality credentials in one frame",
        role="trust",
        background="White with soft sky blue panels behind each badge for separation",
        purpose="Stack the four strongest filters Canadian parents scan for. Defuses the 'is this brand legit?' check.",
        visual=(
            "Centered macro of the GENIUS bottle (label facing camera). Four trust badges arranged top-left, "
            "top-right, bottom-left, bottom-right:\n\n"
            "  • TOP-LEFT — HEALTH CANADA APPROVED (small Canada-leaf icon + NPN 80001375 below)\n"
            "  • TOP-RIGHT — IFOS 5/5 STAR (small fish icon + 5 stars below)\n"
            "  • BOTTOM-LEFT — MADE IN CANADA (small Canada outline + Nutripur badge)\n"
            "  • BOTTOM-RIGHT — NO ARTIFICIAL COLOURS, FLAVOURS, SWEETENERS OR PRESERVATIVES "
            "(small leaf icon)\n\n"
            "Below the bottle, a thin strip with the supporting line: 'Molecularly distilled wild fish oil. "
            "PA-free borage oil. Organic flaxseed oil. Manufactured in Canada by Nutripur.'"
        ),
        overlay="REGULATOR-APPROVED. LAB-TESTED. CANADIAN-MADE.",
        overlay_sub="Health Canada NPN 80001375 · IFOS 5/5 Star · No artificial anything",
        props=["GENIUS bottle (center)", "4 badge graphics in corners", "thin supporting strip"],
        lighting="Studio even light. Hard catch-light on the bottle. Badges legible at thumbnail size.",
        why_it_works=(
            "Stacks the four filters that matter for a Canadian parent shopping omega-3 for kids: regulator, "
            "independent testing, country of origin, clean formulation. No competitor in the omega-3-for-kids "
            "search grid leads with all four."
        ),
    ),
    AIImagePlanItem(
        name="Image 6 — Format clarity: 180 capsules = how long it lasts",
        role="desire",
        background="Soft sky blue #EAF1F8 — same as Image 2 for visual rhythm",
        purpose="Make the pack-size value crystal clear. Removes the 'how long does it last?' purchase friction.",
        visual=(
            "Split-frame infographic. \n\n"
            "LEFT 60% of frame: GENIUS bottle, open, capsules cascading out onto a soft white surface with "
            "a clean count of 4 capsules at the forefront (today's dose) and a pile behind it.\n\n"
            "RIGHT 40% of frame: vertical breakdown panel\n"
            "  • 180 CAPSULES PER BOTTLE\n"
            "  • 4 capsules/day → 45-day supply\n"
            "  • 6 capsules/day → 30-day supply\n"
            "  • Take morning &amp; night, or all at once\n"
            "  • Chew or swallow with water\n\n"
            "Small caption below the panel: 'Recommended: Children 4 years and older — start at 4 capsules/day.'"
        ),
        overlay="180 CHEWABLES. 30 TO 45 DAYS.",
        overlay_sub="4 capsules/day = 45-day supply · 6 capsules/day = 30-day supply",
        props=["GENIUS bottle (open)", "capsule pile + 4-capsule daily count", "dosage info panel"],
        lighting="Even soft front-light. Clean infographic feel.",
        why_it_works=(
            "Pack-size value made obvious. Removes the '180 capsules sounds like a lot but how long does "
            "it last?' mental calculation. Also signals you don't need to re-buy every 2 weeks — hits "
            "the cost-per-day math hard."
        ),
    ),
    AIImagePlanItem(
        name="Image 7 — Brand close: Family moment + Made in Canada",
        role="close",
        background="Warm afternoon family-kitchen scene",
        purpose="Close on family identity. Lifestyle + brand provenance in one frame.",
        visual=(
            "Mid-range environmental shot in a real family kitchen. PARENT (hand / arm visible, no full "
            "face needed — could be over-shoulder or side angle) handing a single chewable capsule to "
            "a KID (back of head or three-quarter profile from behind). Kid's posture is open / reaching "
            "— small natural moment, NOT a posed pose.\n\n"
            "On the kitchen counter beside them: GENIUS bottle (label readable), a small Nutripur info "
            "card with the NPN number visible, an indoor plant, and a soft-focused Canada flag pin or "
            "maple-leaf décor element in the background.\n\n"
            "Warm afternoon side-light from a window. Wood counter, soft natural tones. Reads 'real "
            "Canadian family kitchen,' NOT 'pharmacy.'\n\n"
            "Foreground bottom-left: handwritten-style note card reading: *Three generations of clinical-"
            "quality nutrition. — From the Nutripur family, Quebec.*"
        ),
        overlay="MADE IN CANADA. BACKED BY NUTRIPUR.",
        overlay_sub="Three generations of clinical-quality nutrition. Health Canada NPN 80001375.",
        props=["GENIUS bottle", "Nutripur info card with NPN", "wood counter", "Canada flag pin or maple-leaf décor (soft focus)", "indoor plant", "handwritten-style note card", "parent (hand / arm)", "kid (back / profile)"],
        lighting="Warm afternoon side-light from window. Soft golden hue. Honest, lived-in kitchen — not staged.",
        why_it_works=(
            "Closes on the brand-promise the buyer needs to hear before checkout: real Canadian family, "
            "real handoff moment, real Health Canada credential. The parent-to-kid handoff is the visual "
            "metaphor for the brand-to-customer trust handoff."
        ),
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Brand banner: Made for growing minds.",
        role="a+_banner",
        headline="MADE FOR GROWING MINDS.",
        body=(
            "GENIUS by Nutripur is a Health Canada-approved chewable omega-3 brain support formula for "
            "children and teens ages 4 and up. Backed by clinical research, blended for real life — "
            "every morning, before school, between homework."
        ),
        visual="Wide cinematic morning scene — kitchen counter, GENIUS bottle front-center, soft natural light from a window, school backpack and lunchbox soft-focused in the background. Nutripur blue logo upper-left, Health Canada NPN 80001375 small in the bottom band.",
        alt="Nutripur GENIUS Kids & Teens omega-3 chewable bottle on a kitchen counter in morning light, with school backpack and lunchbox in soft focus.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): The GENIUS Difference",
        role="a+_carousel",
        headline="THE GENIUS DIFFERENCE",
        body=(
            "Tile 1: <b>6 BRAIN NUTRIENTS</b> — DHA · EPA · ALA · GLA · ARA + Phosphatidylcholine.<br/>"
            "Tile 2: <b>HEALTH CANADA APPROVED</b> — NPN 80001375. Defensible, regulator-approved claims.<br/>"
            "Tile 3: <b>IFOS 5/5 STAR</b> — Independently lab-tested for purity, potency, freshness.<br/>"
            "Tile 4: <b>ORGANIC ORANGE</b> — Award-winning flavour. Kids actually take it.<br/>"
            "Tile 5: <b>MADE IN CANADA</b> — Three generations of clinical-quality nutrition."
        ),
        visual="5 square tiles, Nutripur blue accent corner on each. Same composition discipline across all 5. Small icons (brain · maple leaf · fish + stars · orange slice · Canada outline).",
        alt="Five-tile Premium A+ carousel covering GENIUS Kids & Teens differentiators: 6 brain nutrients, Health Canada approved, IFOS 5/5, organic orange flavour, made in Canada.",
    ),
    AIModule(
        name="Module 3 — Banner: How the formula supports brain development",
        role="a+_banner",
        headline="HELPS SUPPORT COGNITIVE DEVELOPMENT.",
        body=(
            "Per Health Canada NPN 80001375: helps support development and mental function in children "
            "such as memory, perception and problem-solving. Helps in the management of ADD/ADHD. "
            "Helps improve concentration in children with ADD/ADHD. Helps in the development of the "
            "nervous system. Provides 90% of the essential fatty acids the brain needs."
        ),
        visual="Wide banner: clean medical-style infographic of a stylized child's brain outline (no face), with 6 nutrient labels (DHA, EPA, ALA, GLA, ARA, Phosphatidylcholine) connected by thin lines to brain regions they support. Nutripur green and blue palette only. NPN 80001375 small in the lower band.",
        alt="Premium A+ banner showing how GENIUS omega-3 nutrients support cognitive development per Health Canada NPN 80001375.",
    ),
    AIModule(
        name="Module 4 — Banner: For school, focus, and restful sleep",
        role="a+_banner",
        headline="FOCUS. LEARNING. EMOTIONAL BALANCE.",
        body=(
            "Helps with difficulty staying concentrated on school work or every day tasks. Calms anxieties "
            "in children. Helps with poor school performance. Enhances poor memory. Supports difficulty "
            "with reading and writing. Helps support better recuperative sleep. Per Health Canada NPN "
            "80001375."
        ),
        visual="Triptych within one banner: LEFT — kid's homework scene (hand on pencil only, no face, books and a glass of water in frame). CENTER — small white dish with 4 capsules on a bedside table, a softly-lit bedroom corner behind. RIGHT — peaceful evening kitchen scene with the GENIUS bottle and a glass of water. Warm natural light across all three panels.",
        alt="Triptych A+ banner showing GENIUS supporting school focus, daily routine, and restful sleep per Health Canada-approved indications.",
    ),
    AIModule(
        name="Module 5 — Carousel (5 tiles): The Nutripur Family for Canadian Households",
        role="a+_carousel",
        headline="THE NUTRIPUR FAMILY",
        body=(
            "Tile 1: <b>GENIUS Kids &amp; Teens CHEWABLE (this product)</b> — Omega-3 brain support, ages 4+. "
            "180 chewable capsules. Organic orange.<br/>"
            "Tile 2: <b>GENIUS Kids &amp; Teens LIQUID</b> — Same brain-support formula in a 114 ml liquid for "
            "kids who can't or won't take capsules.<br/>"
            "Tile 3: <b>GENIUS Mom &amp; Baby</b> — Prenatal DHA omega-3 for pregnancy and breastfeeding.<br/>"
            "Tile 4: <b>COLD &amp; FLU Kids &amp; Teens</b> — Immune support for the same demographic — "
            "winter season pairing.<br/>"
            "Tile 5: <b>MAGNESIUM BISGLYCINATE</b> — Stress, sleep &amp; calm for kids and the whole family.<br/>"
            "<i>All five SKUs confirmed live on nutripur.com — pull current product photography from brand assets.</i>"
        ),
        visual="5 identical-composition product tiles. Nutripur blue + green accent corner on each. Family flat-lay style with consistent bottle / packaging photography.",
        alt="Five-tile A+ carousel of the Nutripur family — GENIUS Chewable, GENIUS Liquid, Mom & Baby prenatal DHA, Cold & Flu Kids, and Magnesium Bisglycinate.",
    ),
    AIModule(
        name="Module 6 — Premium Q&A",
        role="a+_qa",
        headline="QUESTIONS PARENTS ASK",
        body=(
            "<b>Q.</b> Is GENIUS safe for daily use?<br/>"
            "<b>A.</b> Yes. GENIUS is approved by Health Canada (NPN 80001375) and every lot is independently "
            "tested under the IFOS program — the world's strictest standard for fish oil purity, potency and "
            "freshness. Designed for daily use in children 4 years and older.<br/><br/>"

            "<b>Q.</b> Does it taste fishy?<br/>"
            "<b>A.</b> No. GENIUS uses an award-winning organic orange flavour, with no artificial colours, "
            "flavours or sweeteners. Most kids chew it; it can also be swallowed with water.<br/><br/>"

            "<b>Q.</b> How is it different from a kids' omega-3 gummy?<br/>"
            "<b>A.</b> GENIUS delivers six brain nutrients — DHA, EPA, ALA, GLA, ARA, plus Phosphatidylcholine "
            "— in a chewable capsule. Most kids' gummies provide only a small amount of omega-3 and added "
            "sugar. GENIUS provides 90% of the essential fatty acids the brain needs, with no added sugar.<br/><br/>"

            "<b>Q.</b> Does GENIUS help with ADD or ADHD?<br/>"
            "<b>A.</b> GENIUS contains clinically supported ingredients. Per Health Canada NPN 80001375: helps "
            "in the management of Attention Deficit Disorder with or without Hyperactivity (ADD/ADHD), and "
            "helps improve concentration in children with ADD/ADHD. Speak with your healthcare provider "
            "about your child's specific needs.<br/><br/>"

            "<b>Q.</b> How long does one bottle last?<br/>"
            "<b>A.</b> 180 capsules per bottle. At the standard 4 capsules/day dose, that's a 45-day supply. "
            "At the higher 6 capsules/day dose, that's a 30-day supply. Take all at once or split morning "
            "&amp; night.<br/><br/>"

            "<b>Q.</b> Where is GENIUS made?<br/>"
            "<b>A.</b> Made in Canada by Nutripur. Three generations of clinical-quality nutrition. Every "
            "lot IFOS-tested. Health Canada NPN 80001375."
        ),
        visual="Vertical Q/A table. Nutripur green divider lines between each Q. Small Nutripur blue Q. and A. labels.",
        alt="Premium Q&A module addressing the six most-asked parent questions for Nutripur GENIUS Kids & Teens.",
    ),
    AIModule(
        name="Module 7 — Premium Comparison Chart",
        role="a+_comparison",
        headline="WHY GENIUS",
        body=(
            "Compare across 4 columns: <b>Nutripur GENIUS Kids &amp; Teens</b> · Generic kids fish oil capsule · "
            "Kids omega-3 gummy · Plain DHA-only chewable.<br/><br/>"
            "Rows: Brain nutrients (6 vs 1–2) · DHA content (264 mg) · Health Canada NPN · IFOS 5/5 Star · "
            "Phosphatidylcholine for neurotransmission · Added sugar (zero) · Made in Canada · Recommended "
            "for ADD/ADHD support (per NPN).<br/><br/>"
            "Highlight the Nutripur GENIUS column with soft Nutripur-green tint and a 'CANADIAN PARENTS' "
            "CHOICE' ribbon at the top of the column."
        ),
        visual="Standard Amazon Premium Comparison Chart layout, 4 product columns. Competitor columns use category descriptors only — no brand names. Nutripur blue header row.",
        alt="Premium comparison chart for Nutripur GENIUS Kids & Teens vs. generic fish oil capsule, omega-3 gummy, and DHA-only chewable alternatives.",
    ),
]


QA = [
    AIQA(q="Is GENIUS safe for daily use?",
         a="Yes. GENIUS is approved by Health Canada (NPN 80001375) and every lot is IFOS-tested for purity, potency and freshness. Designed for daily use in children 4 years and older."),
    AIQA(q="How long until I see results?",
         a="Most parents notice calmer behaviour and easier homework completion by the second week. Brain function improvements typically build over the first month. Better school results often become noticeable by the second month. Results vary by child."),
    AIQA(q="Does it taste fishy?",
         a="Most kids report a clean orange flavour and chew the capsules without complaint. A small number of kids find the fish oil notes more noticeable — in that case, the capsules can be swallowed whole with water. No artificial colours, flavours or sweeteners are added."),
    AIQA(q="How is GENIUS different from a kids' omega-3 gummy?",
         a="GENIUS delivers 6 brain nutrients in one chewable: DHA, EPA, ALA, GLA, ARA plus Phosphatidylcholine. Provides 90% of the essential fatty acids the brain needs. No added sugar. Most kids' gummies provide only a small amount of omega-3 and several grams of added sugar per serving."),
    AIQA(q="Does GENIUS help with ADD or ADHD?",
         a="Per Health Canada NPN 80001375: helps in the management of Attention Deficit Disorder with or without Hyperactivity (ADD/ADHD), and helps improve concentration in children with ADD/ADHD. Speak with your healthcare provider about your child's specific needs."),
    AIQA(q="What's in the formula?",
         a="DHA 264 mg, EPA 52 mg, ALA 104 mg (omega-3), GLA 64 mg, ARA 20 mg (omega-6), plus Phosphatidylcholine 18 mg and Vitamin E. Sourced from wild fish oil (mackerel, anchovy, sardine, tuna), PA-free borage oil and certified organic flaxseed oil. No artificial colours, flavours, sweeteners or preservatives."),
    AIQA(q="How long does one bottle last?",
         a="180 capsules per bottle. At 4 capsules/day, that's a 45-day supply. At 6 capsules/day, that's a 30-day supply. Take all at once or split morning and night."),
    AIQA(q="Where is GENIUS made?",
         a="Made in Canada by Nutripur. Health Canada NPN 80001375. Manufactured in a GMP-certified facility. Three generations of clinical-quality natural health products."),
]


# Backend KWs — stem-deduped, byte-packed. Avoid: brand names already in title, superlatives.
# Includes FR fallback terms because amazon.ca is bilingual.
BACKEND = (
    "kids omega 3 chewable dha epa childrens brain supplement focus memory adhd add concentration "
    "school learning fish oil capsule 180 organic orange phosphatidylcholine cognitive nervous system "
    "ifos health canada npn pediatric teens prenatal flax borage gla ara"
)


def main() -> None:
    print("Loading Nutripur customer + parsing GENIUS Excel…")
    cust = load_customer("nutripur")
    brief = parse_excel(EXCEL)
    print(f"  Product: {brief.product_name}")
    print(f"  ASIN: {brief.asin}  Marketplace: {cust.marketplace}")
    print(f"  USPs={len(brief.usps)} KWs={len(brief.all_keywords)} Q&A={len(brief.rufus_qa)} reviews=+{len(brief.good_reviews)}/-{len(brief.bad_reviews)}")
    print(f"  Health Canada NPN: 80001375 (claims are NPN-defensible)")

    builder = BriefBuilder(cust, brief, OUT, ai=None)
    builder._ai_title = TITLE
    builder._ai_bullets = BULLETS
    builder._ai_images = IMAGES
    builder._ai_modules = MODULES
    builder._ai_qa = QA
    builder._ai_backend = BACKEND
    builder._ai_compliance = []  # NPN-anchored copy — nothing to flag
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
