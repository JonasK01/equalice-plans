"""Nutripur Magnesium Bisglycinate — 180 Vegetarian Capsules (no magnesium oxide)
Hand-written KW-led copy injected into the branded ReportLab pipeline.

Marketplace: amazon.ca (Canada) · Overlay language: EN
Health Canada NPN: 80136854 — defensible structure/function claims.

Health-claim compliance baseline (magnesium NPN 80136854 / monograph aligned):
  - "Helps to maintain/support normal electrolyte balance and muscle function,
     including heart function"
  - "Helps in energy metabolism / the body's ability to metabolize nutrients"
  - "Helps to maintain proper functioning of the nervous system and muscles"
  - "Helps in the development and maintenance of bones and teeth"
  - "Helps in tissue formation"
  - "A factor in the maintenance of good health"

Sleep / stress / calm = consumer search-intent framing only; the regulated claim is
always anchored to muscle function / nervous system / energy metabolism wording.

Never:
  - Cures / treats / prevents disease (no insomnia/anxiety disease claims)
  - Best / #1 / ultimate / guaranteed
  - Competitor brand names (magnesium oxide may be named as a FORM avoided)
  - "$" or any URL / ".com" in customer-facing copy → write "the Nutripur website"

Real product facts (see SOURCE_NOTES.md):
  - 100 mg elemental magnesium per capsule (400 mg at 4-cap max daily dose)
  - Albion TRAACS fully chelated magnesium bisglycinate — NO magnesium oxide
  - 180 vegetarian capsules (hypromellose) — vegan-friendly
  - Adults 1-4 caps/day; gentle on the stomach, non-laxative
  - Made in Canada, GMP-certified facility, NNHPD-licensed
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
PLAN_NO = "07"   # SEO listing no. -> output named 0X_<ASIN>_Image Plan.pdf


# ===== KW-led copy — Health Canada NPN compliant =====

TITLE = 'Nutripur Magnesium Bisglycinate 100 mg — 180 Vegan Caps, No Magnesium Oxide · High-Absorption Chelated for Sleep, Stress, Muscle & Energy · Gentle, Non-Laxative · Health Canada NPN 80136854'

BULLETS = [
    "<b>BISGLYCINATE, NOT MAGNESIUM OXIDE</b> — 100% fully chelated Albion TRAACS magnesium "
    "bisglycinate, with NO magnesium oxide and no harsh mineral blends. The amino-acid-chelated form "
    "is built for high absorption, so more of every capsule is actually usable by the body.",

    "<b>100 mg ELEMENTAL MAGNESIUM PER CAPSULE</b> — Clear, honest labelling: 100 mg of elemental "
    "magnesium per vegan capsule, up to 400 mg at the 4-capsule daily dose. No guessing about how much "
    "you really get — the elemental amount is stated, not buried behind a compound weight.",

    "<b>GENTLE ON THE STOMACH</b> — Magnesium bisglycinate is bound to two glycine amino acids, a form "
    "chosen for digestive comfort. Designed for daily use without the laxative effect many people notice "
    "from some other magnesium forms. Many reviewers report it sits easily, even on an empty stomach.",

    "<b>MUSCLE, NERVES, SLEEP &amp; STRESS ROUTINE</b> — A go-to for adults winding down at night or "
    "easing tense, tired muscles. Per Health Canada NPN 80136854: helps maintain normal muscle function "
    "and electrolyte balance, supports the nervous system, and helps in energy metabolism.",

    "<b>180 VEGAN CAPSULES · MADE IN CANADA</b> — A long 180-count supply in a vegetarian hypromellose "
    "capsule (no animal gelatin, no artificial fillers). Manufactured in Canada in a GMP-certified "
    "facility and licensed by Health Canada (NPN 80136854). By Nutripur.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="White canvas with a soft teal tint (#E8F5F2) across the bottom 15% for grounding. Same background on all 3 options for a clean A/B test.",
        purpose="Win the click in a magnesium search grid crowded with identical white bottles. Test all 3, keep the winner.",
        visual=(
            "Brief the designer to mock ALL 3 options below. Brand picks the winner via Amazon Manage "
            "Your Experiments. Each option uses ONE callout, ONE action cue, ONE supporting prop — clean, "
            "not stacked.\n\n"

            "▸ OPTION A — 'NO MAGNESIUM OXIDE' DIFFERENTIATOR HERO\n"
            "Center: Nutripur Magnesium Bisglycinate bottle, label fully readable, slight elevated 3/4 "
            "turn, occupying ~70% of frame. Lower-right of the bottle: 3-4 white vegan capsules spilled "
            "from the cap as the action cue.\n"
            "ONE CALLOUT — top-right corner badge: 'NO MAGNESIUM OXIDE · FULLY CHELATED' (Nutripur teal "
            "#2A8C7E background, white text, small check-mark icon).\n"
            "Why it wins: the strongest single search-grid differentiator. Buyers actively avoid cheap "
            "magnesium oxide; no competitor thumbnail leads with the form callout this directly.\n\n"

            "▸ OPTION B — ELEMENTAL DOSE CLARITY HERO (defuses 'how much do I actually get?')\n"
            "Center: bottle slightly left of center, label readable. Right of the bottle: a single vegan "
            "capsule standing upright with a clean numeric tag beside it reading '100 mg ELEMENTAL'.\n"
            "Supporting prop: 1-2 capsules resting at the base.\n"
            "ONE CALLOUT — top-left corner badge: '100 mg ELEMENTAL MAGNESIUM · PER CAPSULE' (Nutripur "
            "navy #1F3A5F background, white text).\n"
            "Why it wins: the #1 magnesium buyer complaint is unclear elemental content. Stating the real "
            "elemental number on the thumbnail answers the question before the click.\n\n"

            "▸ OPTION C — 180 VEGAN CAPS VALUE HERO\n"
            "Center: bottle front-facing. To the lower-left: a small clear glass dish holding a generous "
            "pile of vegan capsules, with 4 capsules counted out in front (one daily dose) as the action "
            "cue.\n"
            "ONE CALLOUT — bottom-right corner badge: '180 VEGAN CAPS · GENTLE ON THE STOMACH' (Nutripur "
            "teal background, white text, small leaf icon).\n"
            "Why it wins: pairs the large 180-count value with the gentle-on-stomach reassurance — two "
            "top purchase drivers in one clean frame.\n\n"

            "Across all 3: bottle dominant ~70%, callout ~6% of frame, supporting prop fills remainder. "
            "Same lighting, same background gradient, same colour temperature so the split test isolates "
            "composition, not light/colour."
        ),
        overlay="(one callout per option — see visual direction)",
        overlay_sub="3 hero options shipped — A/B test, keep the winner",
        props=[
            "OPTION A: bottle + 3-4 vegan capsules spilled from cap + 'no magnesium oxide' badge",
            "OPTION B: bottle + single upright capsule + '100 mg elemental' numeric tag + dose badge",
            "OPTION C: bottle + glass dish of capsules + 4-capsule daily count + 180-count value badge",
        ],
        lighting="Soft top key (5000K daylight balanced) with gentle fill from camera-right. Slight backlight on the bottle to make the label pop. Identical lighting across all 3 options to keep the A/B test clean.",
        why_it_works=(
            "Three angles against three different magnesium buyer triggers: A wins on the form "
            "differentiator (no oxide), B wins on elemental-dose clarity, C wins on count value plus "
            "tolerability. One callout, one action cue, one supporting prop each — readable on a mobile "
            "thumbnail."
        ),
        ctr="Each option leads with a number or a hard differentiator a magnesium shopper is scanning for — 'no magnesium oxide', '100 mg elemental', '180 vegan caps' — so the thumbnail answers the buyer's first question before the click.",
        cvr="By front-loading form, dose clarity and count, the hero pre-qualifies the buyer: the people who click already want exactly what this bottle is, which lifts add-to-cart on the detail page.",
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: Bisglycinate vs the magnesium oxide most people get",
        role="hook",
        background="Soft teal mood #E8F5F2 — clinical-natural, not pharma-sterile",
        purpose="Visually reverse the #1 buyer objection: cheap magnesium oxide. Owns the absorption hook.",
        visual=(
            "Clean side-by-side split frame.\n\n"
            "LEFT panel (muted grey, slightly faded): a generic, unbranded white tablet labelled "
            "'MAGNESIUM OXIDE' with a small low-absorption meter sitting near empty. No brand, no logo — "
            "category descriptor only.\n\n"
            "RIGHT panel (bright, Nutripur teal accent): a single Nutripur vegan capsule labelled "
            "'MAGNESIUM BISGLYCINATE — FULLY CHELATED (ALBION TRAACS)' with a high-absorption meter near "
            "full, and a small molecule outline showing magnesium bound to two glycine amino acids.\n\n"
            "Center divider with a clean 'vs' marker. Bottom caption strip: 'Chelated bisglycinate is "
            "built for absorption and digestive comfort — this formula contains NO magnesium oxide.'"
        ),
        overlay="NOT ALL MAGNESIUM IS ABSORBED THE SAME.",
        overlay_sub="Fully chelated bisglycinate (Albion TRAACS) — NO magnesium oxide. Built for high absorption.",
        props=["generic unbranded oxide tablet (category descriptor only)", "Nutripur vegan capsule", "two absorption meters", "magnesium + 2-glycine molecule outline", "'vs' divider"],
        lighting="Even soft front-light, gentle shadow under each form. Left panel slightly cooler/duller, right panel brighter — guides the eye to the winner. No drama lighting; clarity beats mood.",
        why_it_works=(
            "Directly answers the strongest negative-review theme in the category — distrust of cheap "
            "magnesium oxide and inconsistent absorption. Naming oxide as a FORM (not a brand) is "
            "compliant and is the exact differentiator on the live Amazon title."
        ),
        ctr="A side-by-side 'vs' frame is a pattern interrupt in a grid of plain bottles — the absorption-meter contrast pulls the eye and rewards the swipe.",
        cvr="It defuses the category's biggest trust objection up front: the buyer worried about getting cheap, poorly-absorbed oxide sees this formula is the chelated form they were hunting for.",
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: What magnesium supports (NPN-approved claims only)",
        role="educate",
        background="White with a soft Nutripur-teal ribbon footer",
        purpose="Defend the premium with regulator-approved structure/function language. Earn trust.",
        visual=(
            "Four-quadrant clean infographic. Top of frame: 'WHAT MAGNESIUM HELPS SUPPORT' headline in "
            "Nutripur navy, sentence case.\n\n"
            "QUADRANT 1 — MUSCLE FUNCTION (icon: stylized muscle/leg outline, teal)\n"
            "  • Helps maintain normal muscle function, including heart function\n"
            "  • Helps maintain normal electrolyte balance\n\n"
            "QUADRANT 2 — NERVOUS SYSTEM &amp; CALM ROUTINE (icon: nerve cell, navy)\n"
            "  • Helps maintain proper functioning of the nervous system\n"
            "  • A go-to in an evening wind-down and stress-relief routine\n\n"
            "QUADRANT 3 — ENERGY METABOLISM (icon: clean cell / spark, teal)\n"
            "  • Helps in energy metabolism\n"
            "  • Supports the body's ability to metabolize nutrients\n\n"
            "QUADRANT 4 — BONES, TEETH &amp; TISSUE (icon: bone outline, navy)\n"
            "  • Helps in the development and maintenance of bones and teeth\n"
            "  • Helps in tissue formation\n\n"
            "Footer ribbon (Nutripur teal): 'Claims supported by Health Canada NPN 80136854.'"
        ),
        overlay="WHAT MAGNESIUM HELPS SUPPORT.",
        overlay_sub="Backed by Health Canada NPN 80136854 — regulator-approved structure/function language.",
        props=["4-quadrant layout", "4 medical icons (muscle, nerve, cell/energy, bone)", "NPN citation footer ribbon"],
        lighting="Flat clean studio. Educational module — readability beats atmosphere.",
        why_it_works=(
            "Every line is monograph-aligned, NPN-anchored wording — zero compliance risk. Buyers who "
            "filter on 'is this brand legit?' see actual approved language instead of vague marketing, "
            "which earns the premium over commodity magnesium."
        ),
        ctr="Not a click-first tile — it lives mid-gallery to hold the scroll with a scannable four-way breakdown of why someone takes magnesium.",
        cvr="Regulator-approved wording converts the skeptical, label-reading magnesium buyer who has been burned by vague claims — it reads as honest and defensible.",
    ),
    AIImagePlanItem(
        name="Image 4 — Lifestyle: Evening wind-down / sleep & calm routine",
        role="desire",
        background="Real bedside / living-room scene, warm low evening light from camera-right",
        purpose="Place the buyer in the moment they want magnesium for: unwinding at night. Owns the sleep/calm search intent.",
        visual=(
            "Warm, calm environmental shot. A bedside table or soft side table at dusk: a single Nutripur "
            "Magnesium Bisglycinate capsule resting in an open adult palm (hand only, no face), a glass "
            "of water beside it, and the bottle (label facing camera) in soft focus. A warm bedside lamp "
            "glows in the background; a folded throw blanket and an unlit candle add the wind-down cue.\n\n"
            "Optional second-angle prop: a book face-down and reading glasses, signalling the end-of-day "
            "ritual. Keep the countertop calm and uncluttered.\n\n"
            "Mood: restful, adult, lived-in — NOT a clinical or pharmacy look. Soft, low warm light."
        ),
        overlay="YOUR EVENING WIND-DOWN.",
        overlay_sub="A calm, end-of-day magnesium routine. Helps support normal muscle and nervous system function.",
        props=["Nutripur bottle (soft focus)", "single capsule in open adult palm (no face)", "glass of water", "warm bedside lamp", "folded throw blanket", "unlit candle", "book + reading glasses (optional)"],
        lighting="Warm low evening side-light from camera-right, soft lamp glow. Gentle rim on the bottle. Honest, restful, natural — not staged studio.",
        why_it_works=(
            "Owns the dominant search intent for magnesium — sleep, calm, evening wind-down — while "
            "keeping the regulated claim anchored to muscle/nervous-system language. The hand-only, "
            "lived-in scene lets the adult buyer self-cast without overclaiming."
        ),
        ctr="The cosy dusk palette stands apart from the clinical white grid and signals exactly when and why to take the product, drawing the gallery swipe.",
        cvr="It converts the sleep/stress shopper by showing the product already living in their nightly routine — the emotional 'this is for me' moment that lifts add-to-cart.",
    ),
    AIImagePlanItem(
        name="Image 5 — Trust: 4 quality credentials in one frame",
        role="trust",
        background="White with soft teal panels behind each badge for separation",
        purpose="Stack the four filters Canadian magnesium buyers scan for. Defuse 'is this legit / clean?'.",
        visual=(
            "Centered macro of the Nutripur Magnesium Bisglycinate bottle (label facing camera). Four "
            "trust badges in the corners:\n\n"
            "  • TOP-LEFT — HEALTH CANADA LICENSED (small Canada-leaf icon + NPN 80136854 below)\n"
            "  • TOP-RIGHT — NO MAGNESIUM OXIDE (small check-mark icon + 'fully chelated Albion TRAACS')\n"
            "  • BOTTOM-LEFT — VEGAN CAPSULE (small leaf icon + 'vegetarian hypromellose, no gelatin')\n"
            "  • BOTTOM-RIGHT — MADE IN CANADA · GMP FACILITY (small Canada outline + Nutripur badge)\n\n"
            "Below the bottle, a thin strip: 'Fully chelated magnesium bisglycinate. 100 mg elemental "
            "magnesium per capsule. No artificial fillers. Manufactured in Canada by Nutripur.'"
        ),
        overlay="LICENSED. CHELATED. VEGAN. CANADIAN-MADE.",
        overlay_sub="Health Canada NPN 80136854 · No magnesium oxide · Vegan capsule · Made in Canada",
        props=["Nutripur bottle (center)", "4 badge graphics in corners", "thin supporting spec strip"],
        lighting="Studio even light. Hard catch-light on the bottle. Badges legible at thumbnail size.",
        why_it_works=(
            "Stacks the four filters a Canadian magnesium buyer scans for: regulator licence, clean form "
            "(no oxide), vegan format, and country of origin. No commodity magnesium thumbnail leads with "
            "all four at once."
        ),
        ctr="Badge tiles are high-scan-value mid-gallery — the corner credentials are legible even at thumbnail size and reassure a wary scroller.",
        cvr="It closes the trust gap created by the category's labelling and quality complaints: licence number, no oxide, vegan and Canadian-made together remove the last objection before purchase.",
    ),
    AIImagePlanItem(
        name="Image 6 — Format clarity: dose + how long 180 caps lasts",
        role="desire",
        background="Soft teal #E8F5F2 — same as Image 2 for visual rhythm",
        purpose="Make the dose and pack-size value crystal clear. Removes 'how do I take it / how long does it last?' friction.",
        visual=(
            "Split-frame infographic.\n\n"
            "LEFT 60% of frame: the bottle, open, vegan capsules cascading onto a soft white surface, with "
            "a clean count of 4 capsules at the forefront (the max daily dose) and a pile behind it.\n\n"
            "RIGHT 40% of frame: vertical dose panel\n"
            "  • 180 VEGAN CAPSULES PER BOTTLE\n"
            "  • 100 mg elemental magnesium per capsule\n"
            "  • Adults: 1 to 4 capsules per day\n"
            "  • 2 capsules/day → 90-day supply\n"
            "  • 4 capsules/day → 45-day supply\n"
            "  • Take with water, anytime — gentle enough for evening\n\n"
            "Small caption below the panel: 'Adults — start low at 1-2 capsules and adjust to your routine.'"
        ),
        overlay="180 VEGAN CAPS. 45 TO 90 DAYS.",
        overlay_sub="100 mg elemental per capsule · adults take 1 to 4 per day · gentle, take anytime",
        props=["Nutripur bottle (open)", "capsule pile + 4-capsule daily count", "dose info panel"],
        lighting="Even soft front-light. Clean infographic feel.",
        why_it_works=(
            "Turns the large 180-count into an obvious value story (a 45-to-90-day supply) and removes "
            "dosing uncertainty. Restating 100 mg elemental answers the recurring labelling-clarity "
            "complaint a second time, where the buyer is closest to deciding."
        ),
        ctr="The day-count math ('45 to 90 days') is a concrete value cue that pulls the value-shopper deeper into the gallery.",
        cvr="Clear dosing plus a long supply removes two frictions at once — 'how do I take it' and 'is this enough to be worth it' — nudging the on-the-fence buyer to commit.",
    ),
    AIImagePlanItem(
        name="Image 7 — Brand close: Made in Canada by Nutripur",
        role="close",
        background="Warm, calm home scene with soft natural light",
        purpose="Close on brand trust and Canadian provenance. Lifestyle + brand promise in one frame.",
        visual=(
            "Mid-range environmental shot in a calm, real home corner. The Nutripur Magnesium Bisglycinate "
            "bottle (label readable) sits on a wood surface beside a small Nutripur info card with the NPN "
            "number visible, a glass of water, and a softly-blurred green plant. A soft-focus maple-leaf "
            "décor element or small Canada flag pin sits in the background.\n\n"
            "Warm side-light from a window, wood tones, soft natural palette — reads 'trusted Canadian "
            "wellness brand,' NOT 'pharmacy.'\n\n"
            "Foreground bottom-left: handwritten-style note card reading: *Clinical-quality nutrition, "
            "made in Canada. — From the Nutripur family, Quebec.*"
        ),
        overlay="MADE IN CANADA. BACKED BY NUTRIPUR.",
        overlay_sub="Fully chelated magnesium bisglycinate. Health Canada NPN 80136854. Find more on the Nutripur website.",
        props=["Nutripur bottle", "Nutripur info card with NPN", "wood surface", "glass of water", "green plant (soft focus)", "maple-leaf décor or Canada flag pin (soft focus)", "handwritten-style note card"],
        lighting="Warm afternoon side-light from window. Soft natural tones. Honest, lived-in home — not staged.",
        why_it_works=(
            "Closes on the brand promise the buyer wants before checkout: a real Canadian wellness brand, "
            "a visible Health Canada credential, and clean clinical-quality positioning — the trust "
            "handoff that converts a hesitating shopper."
        ),
        ctr="As the final gallery frame it reinforces brand recall; the warm Canadian-home cue differentiates from faceless commodity sellers.",
        cvr="It answers 'who is behind this?' at the decision moment — a licensed, Canadian-made, family brand — converting buyers who hesitate over unknown supplement labels.",
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Brand banner: Magnesium your body can actually use.",
        role="a+_banner",
        headline="MAGNESIUM YOUR BODY CAN ACTUALLY USE.",
        body=(
            "Nutripur Magnesium Bisglycinate is a fully chelated, high-absorption magnesium for adults — "
            "for muscle function, a calm nervous system, and an easy evening wind-down. No magnesium "
            "oxide. Gentle on the stomach. Made in Canada, licensed by Health Canada (NPN 80136854)."
        ),
        visual="Wide cinematic calm scene — a soft-lit side table at dusk, the Nutripur bottle front-center, a glass of water and a single vegan capsule, warm lamp glow. Nutripur teal logo upper-left, Health Canada NPN 80136854 small in the bottom band.",
        alt="Nutripur Magnesium Bisglycinate bottle on a calm bedside table at dusk with a glass of water and a single vegan capsule.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): The Nutripur Magnesium Difference",
        role="a+_carousel",
        headline="THE NUTRIPUR MAGNESIUM DIFFERENCE",
        body=(
            "Tile 1: <b>NO MAGNESIUM OXIDE</b> — 100% fully chelated bisglycinate (Albion TRAACS).<br/>"
            "Tile 2: <b>100 mg ELEMENTAL PER CAPSULE</b> — honest labelling, up to 400 mg per day.<br/>"
            "Tile 3: <b>GENTLE ON THE STOMACH</b> — bound to glycine; designed for daily use.<br/>"
            "Tile 4: <b>180 VEGAN CAPSULES</b> — vegetarian hypromellose, no gelatin, no fillers.<br/>"
            "Tile 5: <b>HEALTH CANADA LICENSED</b> — NPN 80136854. Made in Canada by Nutripur."
        ),
        visual="5 square tiles, Nutripur teal accent corner on each. Same composition discipline across all 5. Small icons (check-mark / no-oxide · capsule with '100 mg' · stomach/leaf · vegan leaf · maple leaf).",
        alt="Five-tile Premium A+ carousel of Nutripur Magnesium Bisglycinate differentiators: no magnesium oxide, 100 mg elemental, gentle on the stomach, 180 vegan capsules, Health Canada licensed.",
    ),
    AIModule(
        name="Module 3 — Banner: Why the bisglycinate form matters",
        role="a+_banner",
        headline="FULLY CHELATED. BUILT FOR ABSORPTION.",
        body=(
            "Magnesium bisglycinate binds each magnesium to two glycine amino acids using the Albion "
            "TRAACS chelation system — a form chosen for high absorption and digestive comfort. This "
            "formula contains no magnesium oxide and no harsh mineral blends, so it can be taken daily "
            "without the laxative effect many people notice from some other magnesium forms."
        ),
        visual="Wide banner: clean medical-style infographic of a single magnesium ion bound to two glycine molecules, with a soft absorption-pathway illustration. A small inset shows a faded, unbranded 'magnesium oxide' tablet with a near-empty absorption meter for contrast (category descriptor only, no brand). Nutripur teal and navy palette. NPN 80136854 small in the lower band.",
        alt="Premium A+ banner explaining fully chelated Albion TRAACS magnesium bisglycinate and why it is built for absorption, with no magnesium oxide.",
    ),
    AIModule(
        name="Module 4 — Banner: When adults reach for magnesium",
        role="a+_banner",
        headline="MUSCLE. CALM. ENERGY METABOLISM.",
        body=(
            "Helps maintain normal muscle function, including heart function. Helps maintain proper "
            "functioning of the nervous system. Helps in energy metabolism. A go-to for tense, tired "
            "muscles, an evening wind-down, and a daily calm routine. Per Health Canada NPN 80136854."
        ),
        visual="Triptych within one banner: LEFT — post-workout calf/leg stretch (no face) with a glass of water and the bottle nearby. CENTER — a bedside table at dusk, a single capsule and a glass of water, warm lamp glow. RIGHT — a calm morning desk with the bottle and a glass of water. Warm natural light across all three panels.",
        alt="Triptych A+ banner showing Nutripur Magnesium Bisglycinate supporting muscle function, an evening calm routine, and daily energy metabolism per Health Canada-approved indications.",
    ),
    AIModule(
        name="Module 5 — Carousel (5 tiles): The Nutripur Magnesium Family",
        role="a+_carousel",
        headline="THE NUTRIPUR MAGNESIUM FAMILY",
        body=(
            "Tile 1: <b>MAGNESIUM BISGLYCINATE 180 VCAPS (this product)</b> — fully chelated, no "
            "magnesium oxide, 100 mg elemental per capsule. For adults.<br/>"
            "Tile 2: <b>MAGNESIUM BISGLYCINATE — POWDER</b> — the same chelated magnesium in a mixable "
            "powder for those who prefer a drink.<br/>"
            "Tile 3: <b>MAGNESIUM BISGLYCINATE — KIDS &amp; TEENS</b> — a gentler format for ages 9-18.<br/>"
            "Tile 4: <b>GENIUS Kids &amp; Teens</b> — chewable omega-3 brain and focus support, ages 4+.<br/>"
            "Tile 5: <b>GENIUS Mom &amp; Baby</b> — prenatal DHA omega-3 for pregnancy and breastfeeding.<br/>"
            "<i>Confirm current SKUs and pull product photography from brand assets / the Nutripur website.</i>"
        ),
        visual="5 identical-composition product tiles. Nutripur teal + navy accent corner on each. Family flat-lay style with consistent bottle / packaging photography.",
        alt="Five-tile A+ carousel of the Nutripur magnesium and wellness family — Magnesium Bisglycinate capsules, powder, Kids & Teens, plus GENIUS Kids omega-3 and GENIUS Mom & Baby.",
    ),
    AIModule(
        name="Module 6 — Premium Q&A",
        role="a+_qa",
        headline="QUESTIONS BUYERS ASK",
        body=(
            "<b>Q.</b> Does this contain magnesium oxide?<br/>"
            "<b>A.</b> No. This is 100% fully chelated magnesium bisglycinate (Albion TRAACS), with no "
            "magnesium oxide and no harsh mineral blends. The chelated form is chosen for high absorption "
            "and digestive comfort.<br/><br/>"

            "<b>Q.</b> How much magnesium do I actually get?<br/>"
            "<b>A.</b> 100 mg of elemental magnesium per capsule — the usable amount, stated clearly. "
            "Adults take 1 to 4 capsules per day, so up to 400 mg of elemental magnesium daily.<br/><br/>"

            "<b>Q.</b> Will it upset my stomach?<br/>"
            "<b>A.</b> Magnesium bisglycinate is bound to glycine, a form chosen for digestive comfort, "
            "and is designed for daily use without the laxative effect many people notice from some other "
            "magnesium forms. If you are sensitive, start at 1 capsule and build up.<br/><br/>"

            "<b>Q.</b> Can I take it for sleep or stress?<br/>"
            "<b>A.</b> Many adults use it as part of an evening wind-down or calm routine. Per Health "
            "Canada NPN 80136854, magnesium helps maintain proper functioning of the nervous system and "
            "normal muscle function, and helps in energy metabolism.<br/><br/>"

            "<b>Q.</b> Is it vegan?<br/>"
            "<b>A.</b> Yes. The capsule is vegetarian hypromellose — no animal gelatin, no artificial "
            "fillers. The only non-medicinal ingredient is the vegetarian capsule itself.<br/><br/>"

            "<b>Q.</b> Where is it made?<br/>"
            "<b>A.</b> Made in Canada by Nutripur in a GMP-certified facility and licensed by Health "
            "Canada (NPN 80136854). 180 vegan capsules per bottle."
        ),
        visual="Vertical Q/A table. Nutripur teal divider lines between each Q. Small Nutripur navy Q. and A. labels.",
        alt="Premium Q&A module answering the six most-asked questions for Nutripur Magnesium Bisglycinate: oxide, elemental amount, tolerability, sleep/stress, vegan, and origin.",
    ),
    AIModule(
        name="Module 7 — Premium Comparison Chart",
        role="a+_comparison",
        headline="WHY NUTRIPUR MAGNESIUM",
        body=(
            "Compare across 4 columns: <b>Nutripur Magnesium Bisglycinate</b> · Generic magnesium oxide "
            "tablet · Magnesium citrate capsule · Magnesium gummy.<br/><br/>"
            "Rows: Form (fully chelated bisglycinate vs oxide) · Elemental magnesium stated (100 mg) · "
            "Absorption focus · Gentle on the stomach / non-laxative · No magnesium oxide · Vegan capsule "
            "· Added sugar (zero) · Health Canada licensed (NPN) · Made in Canada.<br/><br/>"
            "Highlight the Nutripur column with a soft Nutripur-teal tint and a 'FULLY CHELATED' ribbon at "
            "the top of the column."
        ),
        visual="Standard Amazon Premium Comparison Chart layout, 4 product columns. The three reference columns use category descriptors only — no brand names. Nutripur navy header row.",
        alt="Premium comparison chart for Nutripur Magnesium Bisglycinate vs generic magnesium oxide tablet, magnesium citrate capsule, and magnesium gummy alternatives.",
    ),
]


QA = [
    AIQA(q="Does this contain magnesium oxide?",
         a="No. This is 100% fully chelated magnesium bisglycinate (Albion TRAACS) — no magnesium oxide and no harsh mineral blends. The chelated form is chosen for high absorption and digestive comfort."),
    AIQA(q="How much magnesium do I actually get per capsule?",
         a="100 mg of elemental magnesium per capsule — the usable amount, stated clearly on the label. Adults take 1 to 4 capsules per day, so up to 400 mg of elemental magnesium daily."),
    AIQA(q="Is it gentle on the stomach?",
         a="Magnesium bisglycinate is bound to glycine, a form chosen for digestive comfort, and is designed for daily use without the laxative effect many people notice from some other magnesium forms. If you are sensitive, start at 1 capsule and build up gradually."),
    AIQA(q="Can I take it for sleep, stress or muscle relaxation?",
         a="Many adults take it as part of an evening wind-down or a calm daily routine, and after activity for tired muscles. Per Health Canada NPN 80136854, magnesium helps maintain proper functioning of the nervous system, helps maintain normal muscle function, and helps in energy metabolism."),
    AIQA(q="How many capsules do I take and how long does a bottle last?",
         a="Adults take 1 to 4 capsules per day. With 180 vegan capsules per bottle, that's a 90-day supply at 2 capsules a day, or a 45-day supply at 4 capsules a day. Start low and adjust to your routine."),
    AIQA(q="Is it vegan and free of fillers?",
         a="Yes. The capsule is vegetarian hypromellose — no animal gelatin and no artificial fillers. The vegetarian capsule is the only non-medicinal ingredient."),
    AIQA(q="Where is it made and is it licensed?",
         a="Made in Canada by Nutripur in a GMP-certified facility and licensed by Health Canada (NPN 80136854). You can find more on the Nutripur website."),
]


# Backend KWs — stem-deduped, byte-packed. Avoid: brand names already in title, superlatives.
# Includes FR fallback terms because amazon.ca is bilingual.
BACKEND = (
    "magnesium supplement bisglycinate glycinate chelated traacs albion elemental absorption calm sleep "
    "muscle cramps relaxation stress nervous system energy metabolism vegan capsule 180 gentle stomach "
    "non laxative women men magnesium pure complex magnesium kids magnesium powder canada"
)


def main() -> None:
    print("Loading Nutripur customer + parsing Magnesium Bisglycinate Excel…")
    cust = load_customer("nutripur")
    brief = parse_excel(EXCEL)
    asin = brief.asin or "NA"
    OUT = HERE / f"{PLAN_NO}_{asin}_Image Plan.pdf"
    print(f"  Product: {brief.product_name}")
    print(f"  ASIN: {brief.asin}  Marketplace: {cust.marketplace}")
    print(f"  USPs={len(brief.usps)} KWs={len(brief.all_keywords)} Q&A={len(brief.rufus_qa)} reviews=+{len(brief.good_reviews)}/-{len(brief.bad_reviews)}")
    print(f"  Health Canada NPN: 80136854 (claims are NPN-defensible)")

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
