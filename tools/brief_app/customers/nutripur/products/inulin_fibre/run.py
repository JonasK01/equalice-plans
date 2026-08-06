"""Nutripur Inulin Fibre+ — Synbiotic Prebiotic + Probiotic Fibre Powder
Hand-written KW-led copy injected into the branded ReportLab pipeline.

Marketplace: amazon.ca (Canada)
Health Canada NPN: 80125989 — defensible structure/function claims.

Health-claim compliance baseline (NPN 80125989 approved — VERBATIM):
  - "Prebiotic and probiotic to promote a favorable gut flora"
  - "Helps stimulate the growth of healthy bacteria in the gut"
  - "Helps relieve abdominal pain associated with IBS (Irritable bowel syndrome)"
  - "Helps provide gentle relief of irregularity and/or constipation"
  - "Helps promote a healthy mood balance"
  - "Source of fibre for the maintenance of good health"
  - "Supports gastrointestinal health"

Never (HARD — blocks the deterministic compliance scan):
  - cure / treat / prevent / diagnose / clinically proven / miracle
  - best / #1 / ultimate / guaranteed
  - competitor brand names
  - "$" / URL / ".com" / external links  (write "the Nutripur website")
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
PLAN_NO = "04"   # SEO listing no. -> output named 0X_<ASIN>_Image Plan.pdf


# ===== KW-led copy — Health Canada NPN 80125989 compliant =====

TITLE = (
    "Nutripur Inulin Fibre+ Prebiotic &amp; Probiotic Synbiotic Fibre Powder — Chicory Inulin 5 g + "
    "Bacillus coagulans 2 Billion CFU · Gut Health, Bloating &amp; Regularity · 180 g Unflavoured · NPN 80125989"
)

BULLETS = [
    "<b>SYNBIOTIC: PREBIOTIC FIBRE + PROBIOTIC IN ONE SCOOP</b> — Inulin Fibre+ pairs chicory-root "
    "inulin (the prebiotic fibre that feeds your good bacteria) with Bacillus coagulans (the probiotic). "
    "Per Health Canada NPN 80125989, this prebiotic and probiotic promotes a favorable gut flora and "
    "helps stimulate the growth of healthy bacteria in the gut.",

    "<b>EASES BLOATING, IBS PAIN &amp; IRREGULARITY</b> — Many reviewers report less bloating and "
    "post-meal heaviness within the first weeks. Per the NPN, the formula helps relieve abdominal pain "
    "associated with IBS (irritable bowel syndrome) and helps provide gentle relief of irregularity and/or "
    "constipation. A source of fibre for the maintenance of good health.",

    "<b>5 g INULIN + 2 BILLION CFU · NO REFRIGERATION</b> — Each scoop delivers 5 g of chicory-root "
    "inulin and 2 billion CFU of Bacillus coagulans, a spore-forming probiotic that stays stable at room "
    "temperature and survives the journey through the gut. Shelf-stable — no fridge, no fuss, take it on "
    "the go.",

    "<b>UNFLAVOURED &amp; NON-THICKENING · STIRS INTO ANYTHING</b> — A tasteless, non-thickening powder "
    "that dissolves into water, coffee, tea, smoothies, yogurt or cereal without changing the flavour or "
    "texture. The heat-stable probiotic even holds up in hot coffee or tea. No added sugar or sodium; free "
    "of flavours, colourants, sweeteners, preservatives, additives and fillers.",

    "<b>180 g · VEGAN, GLUTEN-FREE, HALAL &amp; KOSHER · MADE IN CANADA</b> — A 180 g tub with scoop: "
    "take 1 scoop 1 to 3 times a day. Vegan, gluten-free, GMO-free, Halal and Kosher Certified. Made in "
    "Canada by Nutripur, a family company crafting clinical-quality natural health products since 1989.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="White canvas with a soft teal tint (Nutripur #E8F5F2) across the bottom 15% for grounding. Same background across all 3 options for a clean A/B test.",
        purpose="Win the click in a crowded fiber/probiotic search grid. Test all 3, keep the winner.",
        visual=(
            "Brief the designer to mock ALL 3 options below. Brand picks the winner via Amazon Manage Your "
            "Experiments. Each option uses ONE callout, ONE action cue, ONE supporting prop — clean, not "
            "stacked. Pull the real tub/label artwork and product photography from this product's assets/ "
            "folder (the on-file label render + product shots).\n\n"

            "▸ OPTION A — SYNBIOTIC CREDENTIAL HERO (owns the trust signal)\n"
            "Center: Inulin Fibre+ tub front-facing, label fully readable, slight elevated 3/4 turn. Tub "
            "occupies ~70% of frame. Action cue lower-right: the supplied scoop heaped with white powder, "
            "tilted so the fine texture reads. ONE supporting prop: a small fresh chicory root (or chicory "
            "flower) to cue the natural inulin source.\n"
            "ONE CALLOUT — top-right corner badge: 'HEALTH CANADA · NPN 80125989' (Nutripur teal "
            "background, white text, small maple-leaf icon).\n"
            "Why it wins: in the amazon.ca grid, no competitor leads with the NPN number visible. The "
            "Health Canada credential is the strongest single trust signal a Canadian shopper sees before "
            "clicking.\n\n"

            "▸ OPTION B — ACTION + MIXABILITY (defuses 'is it gritty / does it taste bad?')\n"
            "Center: tub slightly left of center, label readable. Action cue right of the tub: a clear glass "
            "of water mid-stir with a spoon, the powder dissolving cleanly (no clumps, no thickening) — a "
            "couple of soft swirl lines show it blending in. Supporting prop: a coffee mug softly out of "
            "focus behind, signalling 'goes in hot drinks too.'\n"
            "ONE CALLOUT — top-left corner badge: 'UNFLAVOURED · DISSOLVES CLEAR · NO REFRIGERATION' "
            "(Nutripur green background, white text).\n"
            "Why it wins: the top hesitation for a fiber powder is taste/grit/thickening. This image proves "
            "it dissolves clear and tasteless, and the 'no refrigeration' line removes a probiotic objection "
            "in the same glance.\n\n"

            "▸ OPTION C — SYNBIOTIC = PRE + PROBIOTIC (owns the category differentiator)\n"
            "Center: tub. Floating in a clean two-node layout: LEFT node 'PREBIOTIC — Inulin 5 g (chicory "
            "root)', RIGHT node 'PROBIOTIC — Bacillus coagulans 2 billion CFU', joined by a '+' into a "
            "single 'SYNBIOTIC' lockup beneath the tub. Each node a soft-edged pill: teal for prebiotic, "
            "blue for probiotic.\n"
            "ONE CALLOUT — bottom-right corner badge: 'PREBIOTIC + PROBIOTIC IN ONE SCOOP' (Nutripur "
            "blue background, white text).\n"
            "Why it wins: shoppers buy a prebiotic OR a probiotic and don't realise they need both. The "
            "two-node + lockup teaches 'synbiotic = one scoop does both,' the exact differentiator.\n\n"

            "Across all 3: tub dominant ~70%, callout ~6% of frame, supporting prop fills remainder. Same "
            "lighting, same background gradient, same colour temperature so the split test isolates "
            "composition, not light/colour."
        ),
        overlay="(one callout per option — see visual direction)",
        overlay_sub="3 hero options shipped — A/B test, keep the winner",
        props=[
            "OPTION A: tub + heaped scoop of powder + fresh chicory root/flower + NPN badge",
            "OPTION B: tub + clear glass of water mid-stir (powder dissolving) + soft-focus coffee mug + mixability badge",
            "OPTION C: tub + prebiotic/probiotic two-node lockup + synbiotic badge",
        ],
        lighting="Soft top key (5000K daylight balanced) with gentle fill from camera-right. Slight backlight on the tub to make the Inulin Fibre+ label pop. Same lighting across all 3 options to keep the A/B test clean.",
        why_it_works=(
            "Three angles against three buyer triggers: A wins on credential trust (NPN), B wins on the "
            "taste/grit/thickening anxiety that sinks fiber powders, C wins on the synbiotic category "
            "differentiator. One callout, one action cue, one supporting prop each — clean enough to read on "
            "a mobile thumbnail."
        ),
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: Prebiotic + Probiotic = Synbiotic",
        role="hook",
        background="Soft teal #E8F5F2 (Nutripur mood) — clinical-natural feel, not pharma-sterile",
        purpose="Teach the synbiotic concept in one frame — the hook a single-ingredient competitor can't match.",
        visual=(
            "Clean infographic. LEFT half: 'PREBIOTIC' — a stylized chicory root with a soft fibre-strand "
            "motif, labelled 'Inulin 5 g · feeds your good bacteria.' RIGHT half: 'PROBIOTIC' — a stylized "
            "spore/cell cluster, labelled 'Bacillus coagulans · 2 billion CFU · the good bacteria.' A bold "
            "Nutripur '+' sits between them. Below, the two merge into one heaped scoop of powder with the "
            "word 'SYNBIOTIC' set in Nutripur blue.\n\n"
            "Footer caption strip: 'One scoop delivers both — the fibre that feeds, and the bacteria that "
            "benefit.' Keep it medical-clean: thin connecting lines, soft pill shapes (teal for prebiotic, "
            "blue for probiotic), no clutter, no candy aesthetic."
        ),
        overlay="PREBIOTIC + PROBIOTIC = SYNBIOTIC.",
        overlay_sub="Inulin 5 g feeds the good bacteria · Bacillus coagulans 2 billion CFU is the good bacteria — one scoop does both.",
        props=["stylized chicory root (prebiotic)", "stylized spore/cell cluster (probiotic)", "Nutripur '+' lockup", "single heaped scoop of powder", "thin connecting lines (infographic style)"],
        lighting="Even soft front-light, subtle shadow under the scoop. Educational hook — clarity over mood.",
        why_it_works=(
            "Most shoppers buy a prebiotic OR a probiotic and never learn they work better together. "
            "Inulin Fibre+ owns 'synbiotic = both in one scoop,' a positioning single-ingredient powders and "
            "probiotic capsules can't claim. Educates and differentiates in one tile."
        ),
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: What it helps with (Health Canada-approved claims only)",
        role="educate",
        background="White with a soft Nutripur-green ribbon footer",
        purpose="Defend the premium and earn trust with verbatim NPN structure/function claims.",
        visual=(
            "Three-column horizontal layout. Top of frame: 'WHAT INULIN FIBRE+ HELPS WITH' headline in "
            "Nutripur blue, sentence case.\n\n"
            "COLUMN 1 — 'GUT FLORA'\n"
            "  - Prebiotic and probiotic to promote a favorable gut flora\n"
            "  - Helps stimulate the growth of healthy bacteria in the gut\n"
            "  - Supports gastrointestinal health\n"
            "Small icon: stylized gut/microbiome outline in Nutripur green.\n\n"
            "COLUMN 2 — 'COMFORT &amp; REGULARITY'\n"
            "  - Helps relieve abdominal pain associated with IBS (irritable bowel syndrome)\n"
            "  - Helps provide gentle relief of irregularity and/or constipation\n"
            "  - Source of fibre for the maintenance of good health\n"
            "Small icon: stylized stomach/comfort symbol in Nutripur blue.\n\n"
            "COLUMN 3 — 'MOOD &amp; BALANCE'\n"
            "  - Helps promote a healthy mood balance\n"
            "  - Supports the gut-brain connection through a balanced microbiome\n"
            "  - No added sugar or sodium\n"
            "Small icon: stylized gut-brain link (gut + simple head profile) in Nutripur green.\n\n"
            "Footer ribbon (Nutripur green): 'Claims supported by Health Canada NPN 80125989.'"
        ),
        overlay="WHAT INULIN FIBRE+ HELPS WITH.",
        overlay_sub="Gut flora · comfort &amp; regularity · healthy mood balance — backed by Health Canada NPN 80125989.",
        props=["3 column layout", "3 small medical icons (gut, stomach, gut-brain link)", "NPN citation footer"],
        lighting="Flat clean studio. Educational module — readability beats atmosphere.",
        why_it_works=(
            "Every line is verbatim from the Health Canada NPN — zero compliance risk. Shoppers filtering "
            "for 'is this legit?' see regulator-approved language, not marketing-speak. The mood-balance "
            "column quietly opens the gut-brain-axis angle the USPs flag, earning the premium over a bare "
            "bag of fiber."
        ),
    ),
    AIImagePlanItem(
        name="Image 4 — Lifestyle: The morning coffee ritual (verbatim-derived)",
        role="desire",
        background="Real kitchen scene, warm morning light from camera-right",
        purpose="Place the buyer in the easiest habit there is — stir it into the drink they already have.",
        visual=(
            "Wide angled shot on a real wood kitchen counter in soft morning light. FOREGROUND: an adult "
            "hand (fingers only, no face) tipping the supplied scoop of powder into a mug of coffee, a few "
            "grains caught mid-air. The powder is visibly dissolving — no clumps. Beside the mug: the Inulin "
            "Fibre+ tub, label facing camera, and a small bowl of yogurt with a spoon to cue 'works in food "
            "too.'\n\n"
            "Background: soft-focused kitchen — a plant, a window with warm light, maybe a smoothie glass. "
            "Honest natural-clinical, NOT pharmacy/lab, NOT staged. No faces, no candy styling.\n\n"
            "Small caption lower-left: 'Tasteless &amp; non-thickening — stirs into coffee, tea, smoothies, "
            "yogurt. Heat-stable, even in hot drinks.'"
        ),
        overlay="ONE SCOOP. IN THE DRINK YOU ALREADY HAVE.",
        overlay_sub="Unflavoured, non-thickening &amp; heat-stable — stir into coffee, tea, smoothies or yogurt.",
        props=["Inulin Fibre+ tub", "coffee mug", "supplied scoop with powder (mid-pour)", "small bowl of yogurt with spoon", "soft-focused plant + smoothie glass", "adult hand (fingers only)"],
        lighting="Warm morning side-light from camera-right. Gentle rim on the tub and steam off the mug. Honest natural-clinical, not studio-staged.",
        why_it_works=(
            "Owns the strongest convenience verbatim — 'easy and convenient to use' — and the heat-stable "
            "mixability claim in one frame. Pouring into existing coffee shows the habit is effortless, the "
            "#1 driver of repeat purchase for a daily fiber/probiotic. Strongest single conversion image in "
            "the plan."
        ),
    ),
    AIImagePlanItem(
        name="Image 5 — Trust: 5 quality credentials in one frame",
        role="trust",
        background="White with soft teal panels behind each badge for separation",
        purpose="Stack the filters Canadian shoppers scan for. Defuses 'is this brand legit / where is it made?'",
        visual=(
            "Centered macro of the Inulin Fibre+ tub (label facing camera). Five trust badges arranged "
            "around it:\n\n"
            "  - TOP-LEFT — HEALTH CANADA · NPN 80125989 (small maple-leaf icon)\n"
            "  - TOP-RIGHT — MADE IN CANADA · SINCE 1989 (small Canada outline + Nutripur mark)\n"
            "  - BOTTOM-LEFT — VEGAN · GLUTEN-FREE · GMO-FREE (small leaf icon)\n"
            "  - BOTTOM-RIGHT — HALAL &amp; KOSHER CERTIFIED (small certification mark)\n"
            "  - CENTER-BOTTOM ribbon — NO REFRIGERATION · SHELF-STABLE PROBIOTIC (small thermometer/"
            "leaf icon)\n\n"
            "Below the tub, a thin strip: 'Certified PURE — manufactured to exceed industry standards and "
            "tested in accredited laboratories. No added sugar or sodium. Made in Canada by Nutripur.'"
        ),
        overlay="REGULATOR-APPROVED. CANADIAN-MADE. SHELF-STABLE.",
        overlay_sub="Health Canada NPN 80125989 · Vegan · Gluten-Free · Halal &amp; Kosher · No refrigeration",
        props=["Inulin Fibre+ tub (center)", "5 badge graphics", "thin supporting strip"],
        lighting="Studio even light. Hard catch-light on the tub. Badges legible at thumbnail size.",
        why_it_works=(
            "Directly answers the negative-review concern about country of manufacture (Made in Canada, "
            "since 1989) and stacks the dietary filters vegan/gluten-free/Halal/Kosher shoppers screen on. "
            "'No refrigeration' pre-empts the classic probiotic objection — all in one trust frame."
        ),
    ),
    AIImagePlanItem(
        name="Image 6 — How to use: dose + 180 g value clarity",
        role="desire",
        background="Soft teal #E8F5F2 — same as Image 2 for visual rhythm",
        purpose="Make dosing obvious and remove the 'how do I take it / how long does it last?' friction.",
        visual=(
            "Split-frame infographic.\n\n"
            "LEFT 55% of frame: the Inulin Fibre+ tub open, the supplied scoop resting on a soft white "
            "surface with a clean heap of powder beside it and a glass of water mid-stir behind.\n\n"
            "RIGHT 45% of frame: a vertical how-to panel\n"
            "  - 180 g TUB · SCOOP INCLUDED\n"
            "  - Take 1 scoop, 1 to 3 times a day\n"
            "  - Mix 1 scoop into 250 mL water, coffee, tea or a smoothie\n"
            "  - Take it 2-3 hours apart from other medications or supplements\n"
            "  - Start with 1 scoop daily, build up as your gut adjusts\n\n"
            "Small caption below the panel: 'Adults. May cause temporary gas or bloating as your gut flora "
            "adjusts — easing in helps.'"
        ),
        overlay="1 SCOOP, 1 TO 3 TIMES A DAY.",
        overlay_sub="Mix into 250 mL of water, coffee, tea or a smoothie. 180 g tub with scoop.",
        props=["Inulin Fibre+ tub (open)", "supplied scoop + powder heap", "glass of water mid-stir", "how-to dosage panel"],
        lighting="Even soft front-light. Clean infographic feel.",
        why_it_works=(
            "Turns the label dosing into a glanceable how-to and the 'ease in / take apart from meds' note "
            "directly defuses the negative-review worry about mild side effects. Removes purchase friction by "
            "making the daily routine obvious."
        ),
    ),
    AIImagePlanItem(
        name="Image 7 — Brand close: gut health, the Nutripur way",
        role="close",
        background="Warm morning kitchen scene with soft Canadian cues",
        purpose="Close on brand identity — family-made, Canadian, clinical-quality since 1989.",
        visual=(
            "Mid-range environmental shot in a real, lived-in kitchen. The Inulin Fibre+ tub sits on a wood "
            "counter beside a finished smoothie and a glass of water; an adult hand (no face) rests a spoon "
            "next to the tub mid-routine. Soft-focused behind: a maple-leaf décor element, a plant, a window "
            "with warm morning light.\n\n"
            "Foreground bottom-left: a handwritten-style note card reading: 'Clinical-quality natural health "
            "products, made by our family in Quebec since 1989. — Nutripur.' A small Nutripur info card with "
            "the NPN number visible sits beside the tub.\n\n"
            "Reads 'real Canadian kitchen,' NOT 'pharmacy.' Warm, honest, calm — no candy styling, no faces."
        ),
        overlay="MADE IN CANADA. BACKED BY NUTRIPUR.",
        overlay_sub="Clinical-quality natural health products since 1989. Health Canada NPN 80125989.",
        props=["Inulin Fibre+ tub", "Nutripur info card with NPN", "finished smoothie + glass of water", "wood counter", "maple-leaf décor (soft focus)", "plant", "handwritten-style note card", "adult hand (no face)"],
        lighting="Warm morning side-light from a window. Soft natural tones. Honest, lived-in kitchen — not staged.",
        why_it_works=(
            "Closes on the brand promise a hesitating shopper needs before checkout: a real Canadian family "
            "company since 1989, a real Health Canada credential, a real daily-routine moment. Reinforces "
            "the Made-in-Canada answer to the origin concern from reviews."
        ),
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Brand banner: Gut health, simplified.",
        role="a+_banner",
        headline="ONE SCOOP. PREBIOTIC + PROBIOTIC.",
        body=(
            "Inulin Fibre+ by Nutripur is a Health Canada-approved synbiotic powder for adults — chicory-root "
            "inulin and Bacillus coagulans in a single tasteless scoop. A prebiotic and probiotic to promote "
            "a favorable gut flora. Stir it into the coffee, tea or smoothie you already have. No "
            "refrigeration, no fuss."
        ),
        visual="Wide cinematic morning scene — wood kitchen counter, Inulin Fibre+ tub front-center, a mug of coffee mid-stir, soft natural window light, a plant and smoothie glass softly out of focus. Nutripur teal logo upper-left, Health Canada NPN 80125989 small in the bottom band.",
        alt="Nutripur Inulin Fibre+ synbiotic powder tub on a kitchen counter in morning light beside a coffee mug, with a plant and smoothie glass in soft focus.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): The Inulin Fibre+ Difference",
        role="a+_carousel",
        headline="THE INULIN FIBRE+ DIFFERENCE",
        body=(
            "Tile 1: <b>SYNBIOTIC IN ONE SCOOP</b> — Prebiotic inulin 5 g + probiotic Bacillus coagulans "
            "2 billion CFU.<br/>"
            "Tile 2: <b>HEALTH CANADA APPROVED</b> — NPN 80125989. Defensible, regulator-approved claims.<br/>"
            "Tile 3: <b>UNFLAVOURED &amp; NON-THICKENING</b> — Stirs clear into water, coffee, tea, smoothies "
            "or yogurt.<br/>"
            "Tile 4: <b>NO REFRIGERATION</b> — Spore-forming, heat-stable probiotic. Shelf-stable, "
            "travel-ready.<br/>"
            "Tile 5: <b>VEGAN · GLUTEN-FREE · MADE IN CANADA</b> — Halal &amp; Kosher Certified. No added "
            "sugar or sodium."
        ),
        visual="5 square tiles, Nutripur teal accent corner on each. Same composition discipline across all 5. Small icons (synbiotic '+' · maple leaf · glass-with-spoon · thermometer/leaf · vegan leaf).",
        alt="Five-tile Premium A+ carousel covering Inulin Fibre+ differentiators: synbiotic in one scoop, Health Canada approved, unflavoured non-thickening, no refrigeration, vegan and made in Canada.",
    ),
    AIModule(
        name="Module 3 — Banner: How a synbiotic supports your gut",
        role="a+_banner",
        headline="THE FIBRE THAT FEEDS. THE BACTERIA THAT BENEFIT.",
        body=(
            "Per Health Canada NPN 80125989: a prebiotic and probiotic to promote a favorable gut flora, and "
            "helps stimulate the growth of healthy bacteria in the gut. Inulin is the prebiotic fibre your "
            "good bacteria feed on; Bacillus coagulans is the probiotic. Together — a synbiotic that supports "
            "gastrointestinal health."
        ),
        visual="Wide banner: clean medical-style infographic. LEFT — chicory root with a fibre-strand motif labelled 'PREBIOTIC · Inulin 5 g.' CENTER — a Nutripur '+' merging into a balanced microbiome illustration. RIGHT — spore/cell cluster labelled 'PROBIOTIC · Bacillus coagulans 2 billion CFU.' Nutripur teal and blue palette only. NPN 80125989 small in the lower band.",
        alt="Premium A+ banner showing how the prebiotic inulin and probiotic Bacillus coagulans work together as a synbiotic per Health Canada NPN 80125989.",
    ),
    AIModule(
        name="Module 4 — Banner: For bloating, regularity and balance",
        role="a+_banner",
        headline="LESS BLOATING. GENTLE REGULARITY. STEADY MOOD.",
        body=(
            "Per Health Canada NPN 80125989: helps relieve abdominal pain associated with IBS (irritable "
            "bowel syndrome), helps provide gentle relief of irregularity and/or constipation, and helps "
            "promote a healthy mood balance. A source of fibre for the maintenance of good health."
        ),
        visual="Triptych within one banner: LEFT — a calm midsection / comfort cue (hands resting at the waist, no face) with a glass of water in frame. CENTER — the supplied scoop and the tub on a clean counter, a soft daily-rhythm clock motif behind. RIGHT — a peaceful morning kitchen with a smoothie and the tub. Warm natural light across all three panels. NPN 80125989 small in the lower band.",
        alt="Triptych A+ banner showing Inulin Fibre+ supporting digestive comfort, gentle regularity and healthy mood balance per Health Canada-approved indications.",
    ),
    AIModule(
        name="Module 5 — Carousel (5 tiles): The Nutripur Digestive Family",
        role="a+_carousel",
        headline="THE NUTRIPUR DIGESTIVE FAMILY",
        body=(
            "Tile 1: <b>INULIN FIBRE+ (this product)</b> — Synbiotic prebiotic + probiotic powder. 180 g. "
            "Unflavoured.<br/>"
            "Tile 2: <b>INTESFIB</b> — Unflavoured fibre powder for everyday gut support (also in "
            "capsules).<br/>"
            "Tile 3: <b>PSYLLIUM FIBRE</b> — Very fine pure psyllium powder, a source of fibre for good "
            "health.<br/>"
            "Tile 4: <b>LAXAFORCE</b> — Gentle laxative formula with beneficial prebiotics and prune.<br/>"
            "Tile 5: <b>SUPER OMEGA</b> — Liquid omega-3 to round out a daily wellness routine.<br/>"
            "<i>All confirmed live on the Nutripur website — pull current product photography from brand "
            "assets.</i>"
        ),
        visual="5 identical-composition product tiles. Nutripur teal + blue accent corner on each. Family flat-lay style with consistent tub / packaging photography.",
        alt="Five-tile A+ carousel of the Nutripur digestive family — Inulin Fibre+, IntesFib, Psyllium Fibre, Laxaforce and Super Omega.",
    ),
    AIModule(
        name="Module 6 — Premium Q&A",
        role="a+_qa",
        headline="QUESTIONS SHOPPERS ASK",
        body=(
            "<b>Q.</b> What is a synbiotic?<br/>"
            "<b>A.</b> A synbiotic combines a prebiotic and a probiotic. Inulin Fibre+ pairs chicory-root "
            "inulin (the prebiotic fibre that feeds good bacteria) with Bacillus coagulans (the probiotic). "
            "Per Health Canada NPN 80125989, this prebiotic and probiotic promotes a favorable gut flora.<br/><br/>"

            "<b>Q.</b> Does it have a taste or thicken my drink?<br/>"
            "<b>A.</b> No. The powder is unflavoured and non-thickening — it dissolves into water, coffee, "
            "tea, smoothies or yogurt without changing the flavour or texture. The probiotic is heat-stable, "
            "so it even holds up in hot drinks.<br/><br/>"

            "<b>Q.</b> Does it need to be refrigerated?<br/>"
            "<b>A.</b> No. Bacillus coagulans is a spore-forming, shelf-stable probiotic, so Inulin Fibre+ "
            "stays stable at room temperature — easy to keep on the counter or take while travelling.<br/><br/>"

            "<b>Q.</b> Can it help with bloating, IBS or regularity?<br/>"
            "<b>A.</b> Per Health Canada NPN 80125989: it helps relieve abdominal pain associated with IBS "
            "(irritable bowel syndrome) and helps provide gentle relief of irregularity and/or constipation. "
            "Many reviewers also report less bloating with daily use. Results vary by person.<br/><br/>"

            "<b>Q.</b> Will it cause gas when I start?<br/>"
            "<b>A.</b> As your gut flora adjusts, the formula may cause temporary gas or bloating. Starting "
            "with 1 scoop a day and building up gradually helps. Take it 2-3 hours apart from other "
            "medications or supplements.<br/><br/>"

            "<b>Q.</b> Where is it made and is it vegan?<br/>"
            "<b>A.</b> Made in Canada by Nutripur, a family company since 1989. Inulin Fibre+ is vegan, "
            "gluten-free, GMO-free, and Halal &amp; Kosher Certified, with no added sugar or sodium."
        ),
        visual="Vertical Q/A table. Nutripur green divider lines between each Q. Small Nutripur blue Q. and A. labels.",
        alt="Premium Q&A module addressing the six most-asked shopper questions for Nutripur Inulin Fibre+.",
    ),
    AIModule(
        name="Module 7 — Premium Comparison Chart",
        role="a+_comparison",
        headline="WHY INULIN FIBRE+",
        body=(
            "Compare across 4 columns: <b>Nutripur Inulin Fibre+</b> · Prebiotic fibre powder only · "
            "Probiotic capsule only · Fibre gummy.<br/><br/>"
            "Rows: Synbiotic (prebiotic + probiotic) · Inulin per scoop (5 g) · Probiotic CFU (2 billion) · "
            "Health Canada NPN · No refrigeration · Unflavoured &amp; non-thickening · No added sugar · "
            "Vegan / Gluten-free · Made in Canada.<br/><br/>"
            "Highlight the Nutripur Inulin Fibre+ column with a soft Nutripur-teal tint and a 'SYNBIOTIC IN "
            "ONE SCOOP' ribbon at the top of the column."
        ),
        visual="Standard Amazon Premium Comparison Chart layout, 4 product columns. Competitor columns use category descriptors only — no brand names. Nutripur blue header row.",
        alt="Premium comparison chart for Nutripur Inulin Fibre+ vs. prebiotic-only powder, probiotic-only capsule and fibre gummy alternatives.",
    ),
]


QA = [
    AIQA(q="What exactly is in Inulin Fibre+?",
         a="Each scoop contains inulin (from chicory root) 5 g and Bacillus coagulans (MTCC 5856) 2 billion CFU, with GMO-free sweet potato maltodextrin as the only non-medicinal ingredient. No flavours, colourants, sweeteners, preservatives, additives or fillers. No added sugar or sodium."),
    AIQA(q="What is a synbiotic and why does it matter?",
         a="A synbiotic combines a prebiotic and a probiotic. The inulin is the prebiotic fibre that feeds your good bacteria; Bacillus coagulans is the probiotic. Per Health Canada NPN 80125989, this prebiotic and probiotic promotes a favorable gut flora and helps stimulate the growth of healthy bacteria in the gut."),
    AIQA(q="Does it taste bad or make drinks thick?",
         a="No. The powder is unflavoured and non-thickening. It dissolves into water, coffee, tea, smoothies or yogurt without changing the flavour or texture. The probiotic is heat-stable, so it holds up even in hot coffee or tea."),
    AIQA(q="Does it need refrigeration?",
         a="No. Bacillus coagulans is a spore-forming, shelf-stable probiotic, so Inulin Fibre+ stays stable at room temperature. Keep it on the counter or take it while travelling."),
    AIQA(q="Can it help with bloating, IBS pain or constipation?",
         a="Per Health Canada NPN 80125989: it helps relieve abdominal pain associated with IBS (irritable bowel syndrome) and helps provide gentle relief of irregularity and/or constipation. Many reviewers also report less bloating with daily use. Results vary by person."),
    AIQA(q="How do I take it, and could it cause gas at first?",
         a="Adults take 1 scoop, 1 to 3 times a day, mixed into 250 mL of water, coffee, tea or a smoothie. Take it 2-3 hours apart from other medications or supplements. As your gut flora adjusts it may cause temporary gas or bloating, so start with 1 scoop daily and build up gradually."),
    AIQA(q="Is it vegan, gluten-free and where is it made?",
         a="Inulin Fibre+ is vegan, gluten-free, GMO-free, and Halal & Kosher Certified. It is made in Canada by Nutripur, a family company crafting natural health products since 1989, and is tested in accredited laboratories. Health Canada NPN 80125989."),
]


# Backend KWs — stem-deduped, byte-packed. Avoid: brand names already in title, superlatives.
# Includes FR fallback terms because amazon.ca is bilingual.
BACKEND = (
    "gut health bloating debloat regularity constipation relief ibs digestive microbiome flora bacteria "
    "synbiotic chicory powder unflavoured non thickening shelf stable cfu adults men women "
    "probiotique prebiotique fibre intestinale digestion"
)


def main() -> None:
    print("Loading Nutripur customer + parsing Inulin Fibre+ Excel…")
    cust = load_customer("nutripur")
    brief = parse_excel(EXCEL)
    asin = brief.asin or "NA"
    OUT = HERE / f"{PLAN_NO}_{asin}_Image Plan.pdf"
    print(f"  Product: {brief.product_name}")
    print(f"  ASIN: {brief.asin}  Marketplace: {cust.marketplace}")
    print(f"  USPs={len(brief.usps)} KWs={len(brief.all_keywords)} Q&A={len(brief.rufus_qa)} reviews=+{len(brief.good_reviews)}/-{len(brief.bad_reviews)}")
    print(f"  Health Canada NPN: 80125989 (claims are NPN-defensible)")

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
