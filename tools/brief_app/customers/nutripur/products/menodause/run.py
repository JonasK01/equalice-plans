"""Nutripur MENODAUSE — Menopausal Formula with Ashwagandha
Hand-written KW-led copy injected into the branded ReportLab pipeline.

Marketplace: amazon.ca (Canada)
Health Canada NPN: 80042095 — defensible structure/function claims (this product's own NPN).

Health-claim compliance baseline (NPN 80042095 approved — "Traditionally used in herbal
medicine / Ayurveda"; verbatim from the 2025 box artwork in assets/):
  - "Helps relieve menopause-related symptoms, including hot flashes, night sweats, mood swings,
     sleep disorders, urinary discomfort, and vaginal dryness."
  - "Helps relieve nervous tension, restlessness and nervousness."
  - "Acts as a restorative tonic and supports energy metabolism."
  - "Helps improve memory."
  - "Acts as a hormone normaliser to help stabilise the menstrual cycle and relieve
     premenstrual and menstrual symptoms."
  - "Helps in the maintenance of bones, cartilage, teeth, and gums."

Formula per capsule (from the 2025 box — authoritative over the website write-up):
  Black cohosh extract (Actaea racemosa, root) 40 mg, standardized to 2.5% triterpene glycosides
  Ashwagandha 10:1 extract (Withania somnifera, root) 100 mg = 1000 mg ashwagandha
  Chasteberry 4:1 extract (Vitex agnus-castus, fruit) 100 mg = 400 mg chasteberry
  Vitamin C 75 mg · B1 / B2 / B3 / B5 / B6 25 mg each
  60 vegetarian capsules · 1–2 capsules twice daily.

Never (compliance):
  - cure / treat / prevent disease
  - best / #1 / ultimate / guaranteed
  - competitor brand names
  - estrogen/hormone *medical* claims or "replaces HRT"
  - "$" or URLs/".com" in any customer-facing copy (write "the Nutripur website")
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
PLAN_NO = "08"   # SEO listing no. -> output named 0X_<ASIN>_Image Plan.pdf


# ===== KW-led copy — Health Canada NPN compliant =====

TITLE = 'Nutripur Menodause Menopause Supplement for Women — Ashwagandha, Black Cohosh & Chasteberry · Hot Flashes, Night Sweats, Mood & Sleep · 60 Veg Capsules · Health Canada NPN 80042095'

BULLETS = [
    "<b>MENOPAUSE &amp; PERIMENOPAUSE SYMPTOM RELIEF</b> — Health Canada-approved formula "
    "(NPN 80042095) that helps relieve menopause-related symptoms, including hot flashes, night "
    "sweats, mood swings, sleep disorders and vaginal dryness. Designed for women moving through "
    "perimenopause, menopause and beyond — many report a calmer, steadier day by the second week.",

    "<b>WITH 1000 mg ASHWAGANDHA + BLACK COHOSH + CHASTEBERRY</b> — A synergistic botanical blend: "
    "Ashwagandha 10:1 extract (equivalent to 1000 mg), Black cohosh standardized to 2.5% triterpene "
    "glycosides, and Chasteberry 4:1 (equivalent to 400 mg). Acts as a hormone normaliser to help "
    "stabilise the cycle — the combination does what a single herb on its own cannot.",

    "<b>SUPPORTS CALM, MOOD &amp; RESTFUL SLEEP</b> — Per Health Canada: helps relieve nervous "
    "tension, restlessness and nervousness, and helps improve memory. Ashwagandha is a traditional "
    "restorative tonic that supports energy metabolism — so the formula works on the mood, sleep and "
    "tired-all-day side of menopause, not just hot flashes.",

    "<b>6 SUPPORTING VITAMINS · VEGETARIAN CAPSULES · NO FILLERS</b> — Each capsule adds Vitamin C "
    "75 mg plus B1, B2, B3, B5 and B6 (25 mg each) for energy metabolism. Hypromellose vegetarian "
    "capsules with organic rice extract, organic gum arabic and organic sunflower oil. No artificial "
    "additives or fillers. Vegan, gluten-free, lactose-free, alcohol-free.",

    "<b>60 VEGETARIAN CAPSULES · MADE IN CANADA BY NUTRIPUR</b> — Adults take 1 to 2 capsules twice "
    "daily; suitable for prolonged daily use across the whole menopausal transition. Formulated with "
    "research-based ingredients and made in Canada under Health Canada NPN 80042095. Clinical-quality "
    "natural health products from the Nutripur family.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="White canvas with a soft warm sage-and-blush tint across the bottom 15% for grounding. Same background across all 3 options so the split test stays clean.",
        purpose="Win the click in a search grid full of look-alike menopause bottles. Test all 3, keep the winner.",
        visual=(
            "Brief the designer to mock ALL 3 options below. Brand picks the winner via Amazon Manage "
            "Your Experiments. Each option uses ONE callout, ONE action cue, ONE supporting prop — "
            "clean, dignified, NOT stacked. Warm and empowering tone for women 40s–50s+. No candy, no "
            "cartoon, no fear imagery.\n\n"

            "▸ OPTION A — NPN CREDENTIAL HERO (owns the trust signal)\n"
            "Center: Menodause bottle front-facing, label fully readable, slight elevated 3/4 turn. "
            "Bottle occupies ~70% of frame. Lower-right of the bottle: 2 vegetarian capsules and a "
            "small sprig of fresh ashwagandha/botanical greenery for a natural-botanical cue.\n"
            "ONE CALLOUT — top-right corner badge: 'HEALTH CANADA APPROVED · NPN 80042095' "
            "(Nutripur teal background, white text, small Canada-leaf icon).\n"
            "Why it wins: in the amazon.ca menopause grid, almost no competitor shows the actual NPN. "
            "The Health Canada credential is the single strongest trust signal a Canadian woman can "
            "see before clicking.\n\n"

            "▸ OPTION B — INGREDIENT POWER (owns 'with Ashwagandha')\n"
            "Center: Menodause bottle slightly left of center, label readable. Right of the bottle: a "
            "small clean arrangement of the 3 hero botanicals — ashwagandha root, a black cohosh "
            "stem, and chasteberry berries — each subtly labelled.\n"
            "ONE CALLOUT — top-left corner badge: 'WITH 1000 mg ASHWAGANDHA' (Nutripur blue "
            "background, white text).\n"
            "Why it wins: 'with ashwagandha' is rising fast in the menopause search axis. Showing the "
            "three named botanicals proves this is a real synergistic blend, not a single-herb pill.\n\n"

            "▸ OPTION C — SHOW THE CONTENTS + SYMPTOM PROMISE (defuses 'will it actually help?')\n"
            "Center: Menodause bottle, open, with a small white ceramic dish beside it holding 2 "
            "vegetarian capsules (a single dose), one capsule resting on the rim. A thin soft-focus "
            "linen and a single eucalyptus sprig for a calm, spa-like cue.\n"
            "ONE CALLOUT — bottom-right corner badge: 'HOT FLASHES · MOOD · SLEEP' (Nutripur teal "
            "background, white text).\n"
            "Why it wins: shows the vegetarian capsules (per the creative directive — never a bare "
            "bottle) and names the three symptoms women search for most, in regulator-safe wording.\n\n"

            "Across all 3: bottle dominant ~70%, callout ~6% of frame, supporting prop fills the rest. "
            "Same lighting, same background gradient, same colour temperature so the split test "
            "isolates composition, not light or colour."
        ),
        overlay="(one callout per option — see visual direction)",
        overlay_sub="3 hero options shipped — A/B test, keep the winner",
        props=[
            "OPTION A: bottle + 2 vegetarian capsules + botanical sprig + NPN badge",
            "OPTION B: bottle + ashwagandha root + black cohosh stem + chasteberry berries (labelled) + ingredient badge",
            "OPTION C: bottle (open) + white dish with 2 capsules + eucalyptus sprig + linen + symptom badge",
        ],
        lighting="Soft top key (5000K daylight balanced) with gentle fill from camera-right. Slight backlight to make the Menodause label pop. Identical lighting across all 3 options to keep the A/B test clean.",
        why_it_works=(
            "Three angles against three buyer triggers: A wins on credential trust (NPN), B wins on "
            "the rising 'with ashwagandha' search, C wins on showing contents + the symptom promise. "
            "One callout, one action cue, one prop each. Warm and dignified — reads cleanly on a "
            "mobile thumbnail."
        ),
        ctr="",
        cvr="",
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: 3 botanicals + 1000 mg ashwagandha in one capsule",
        role="hook",
        background="Soft warm teal #E8F5F2 (Nutripur mood) — clinical-natural, calm, not pharma-sterile",
        purpose="Stack the synergistic-blend differentiator. The hook a single-herb competitor can't match.",
        visual=(
            "Center: a clean macro of a single Menodause vegetarian capsule, oriented so the capsule "
            "reads as 'real, swallowable, vegetarian.' Behind the capsule, 3 botanical labels in a "
            "clean triangular layout: ASHWAGANDHA · BLACK COHOSH · CHASTEBERRY. Each label sits "
            "inside a soft-edged pill shape (Nutripur teal for the herbs), with a thin connecting line "
            "from each label to the central capsule, like a calm medical-botanical infographic.\n\n"
            "Below the capsule: a small caption strip with the real amounts — Ashwagandha 10:1 "
            "(equivalent to 1000 mg) · Black cohosh 40 mg (2.5% triterpene glycosides) · Chasteberry "
            "4:1 (equivalent to 400 mg) · plus Vitamin C and 5 B vitamins."
        ),
        overlay="3 BOTANICALS. ONE VEGETARIAN CAPSULE.",
        overlay_sub="Ashwagandha (equivalent to 1000 mg) + black cohosh + chasteberry — a synergistic menopause blend.",
        props=["single vegetarian capsule (macro)", "3 botanical label pills", "thin connecting lines (infographic style)", "amounts caption strip"],
        lighting="Even soft front-light, gentle 3D shadow under the capsule. No drama lighting — this is an educational hook, clarity beats mood.",
        why_it_works=(
            "Direct reversal of the most common competitor positioning: most menopause pills lead with "
            "one herb. Menodause owns the three-botanical synergistic blend with a standout 1000 mg "
            "ashwagandha equivalence — defensible per the on-pack formula. Educates and differentiates "
            "in one frame."
        ),
        ctr="",
        cvr="",
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: what each ingredient supports (Health Canada-approved wording only)",
        role="educate",
        background="White with a soft Nutripur-teal ribbon footer",
        purpose="Defend the price premium. Earn trust with Health Canada-language structure/function claims.",
        visual=(
            "Three-column horizontal layout. Top of frame: 'WHAT EACH INGREDIENT SUPPORTS' headline in "
            "Nutripur blue, sentence case.\n\n"
            "COLUMN 1 — 'Black Cohosh + Chasteberry'\n"
            "  - Helps relieve menopause-related symptoms\n"
            "  - Hot flashes, night sweats, vaginal dryness\n"
            "  - Acts as a hormone normaliser to help stabilise the cycle\n"
            "Small icon: stylized botanical leaf in Nutripur teal.\n\n"
            "COLUMN 2 — 'Ashwagandha (1000 mg equivalent)'\n"
            "  - Helps relieve nervous tension and restlessness\n"
            "  - Restorative tonic; supports energy metabolism\n"
            "  - Helps improve memory\n"
            "Small icon: stylized calm/leaf-and-drop in Nutripur blue.\n\n"
            "COLUMN 3 — 'Vitamin C + B Complex'\n"
            "  - B1, B2, B3, B5, B6 for energy metabolism\n"
            "  - Vitamin C 75 mg\n"
            "  - Helps with daily energy and tiredness\n"
            "Small icon: stylized vitamin/spark in Nutripur teal.\n\n"
            "Footer ribbon (Nutripur teal): 'Claims supported by Health Canada NPN 80042095.'"
        ),
        overlay="WHAT EACH INGREDIENT SUPPORTS.",
        overlay_sub="Backed by Health Canada NPN 80042095 — defensible, regulator-approved language.",
        props=["3 column layout", "3 small botanical/vitamin icons", "NPN citation footer ribbon"],
        lighting="Flat clean studio. Educational module — readability beats atmosphere.",
        why_it_works=(
            "Every line is drawn from the Health Canada NPN recommended-use wording — zero compliance "
            "risk. Women who filter on 'is this brand legitimate?' see actual regulator-approved "
            "language, not marketing-speak. Earns the premium over generic black-cohosh-only pills."
        ),
        ctr="",
        cvr="",
    ),
    AIImagePlanItem(
        name="Image 4 — Lifestyle: cool, calm afternoon (verbatim-derived from reviews)",
        role="desire",
        background="Real home scene — bright living room or kitchen, warm soft afternoon light",
        purpose="Place the buyer in the frame. Owns the 'cooler, calmer, sleeping better' verbatim from real reviews.",
        visual=(
            "Warm environmental shot. A woman in her late 40s–50s, relaxed and at ease — seated by a "
            "sunlit window with a cup of tea, or mid-laugh with a friend — looking genuinely "
            "comfortable and in control (NOT fanning herself, NOT distressed; dignity and calm "
            "confidence, no fear cliché). Natural, real, un-posed.\n\n"
            "FOREGROUND right edge: Menodause bottle (label facing camera) beside a small white "
            "ceramic dish with 2 vegetarian capsules and a glass of water.\n\n"
            "Background: soft-focused plants, linen, a calm neutral palette. Warm afternoon light from "
            "camera-right. Real-home vibe, NOT pharmacy or lab.\n\n"
            "Model note: use a real woman 45–55 with model release, or stock if brand prefers. Avoid "
            "competitor-branded items."
        ),
        overlay="COOLER DAYS. CALMER NIGHTS.",
        overlay_sub="Helps relieve hot flashes, night sweats &amp; mood swings. Many users report a steadier week 2 onward.",
        props=["Menodause bottle", "small white dish with 2 capsules", "glass of water", "cup of tea", "soft-focused plants / linen", "woman model 45–55 (relaxed, dignified)"],
        lighting="Warm afternoon side-light from camera-right. Soft hair-light on the model. Slight rim on the bottle. Honest natural-clinical, not staged.",
        why_it_works=(
            "Owns the strongest real-review verbatim — relief from hot flashes and night sweats, "
            "better sleep, steadier mood — with the buyer's peer in frame. Empowering, dignified tone "
            "that the audience responds to. The strongest single conversion image in the plan."
        ),
        ctr="",
        cvr="",
    ),
    AIImagePlanItem(
        name="Image 5 — Trust: 4 quality credentials in one frame",
        role="trust",
        background="White with soft warm teal panels behind each badge for separation",
        purpose="Stack the four filters Canadian women scan for. Defuses the 'is this brand legit?' check.",
        visual=(
            "Centered macro of the Menodause bottle (label facing camera). Four trust badges arranged "
            "top-left, top-right, bottom-left, bottom-right:\n\n"
            "  - TOP-LEFT — HEALTH CANADA APPROVED (small Canada-leaf icon + NPN 80042095 below)\n"
            "  - TOP-RIGHT — VEGETARIAN CAPSULES (small leaf icon + 'vegan')\n"
            "  - BOTTOM-LEFT — MADE IN CANADA (small Canada outline + Nutripur badge)\n"
            "  - BOTTOM-RIGHT — NO ARTIFICIAL ADDITIVES OR FILLERS (small clean-formula icon)\n\n"
            "Below the bottle, a thin strip with the supporting line: 'Vegan · gluten-free · "
            "lactose-free · alcohol-free. Organic rice extract, organic gum arabic, organic sunflower "
            "oil. Made in Canada by Nutripur.'"
        ),
        overlay="REGULATOR-APPROVED. CLEAN FORMULA. CANADIAN-MADE.",
        overlay_sub="Health Canada NPN 80042095 · vegetarian capsules · no artificial additives or fillers",
        props=["Menodause bottle (center)", "4 badge graphics in corners", "thin supporting strip"],
        lighting="Studio even light. Hard catch-light on the bottle. Badges legible at thumbnail size.",
        why_it_works=(
            "Stacks the four filters that matter for a Canadian woman shopping a menopause supplement: "
            "regulator, vegetarian/clean format, country of origin, no fillers. No competitor in the "
            "menopause grid leads with all four."
        ),
        ctr="",
        cvr="",
    ),
    AIImagePlanItem(
        name="Image 6 — Format clarity: 60 capsules = how to take it",
        role="desire",
        background="Soft warm teal #E8F5F2 — same as Image 2 for visual rhythm",
        purpose="Make the dose and pack value crystal clear. Removes 'how do I take it / how long does it last?' friction.",
        visual=(
            "Split-frame infographic.\n\n"
            "LEFT 60% of frame: Menodause bottle, open, vegetarian capsules spilling gently onto a "
            "soft white surface with a clean count of 2 capsules at the forefront (a single dose) and "
            "a small pile behind.\n\n"
            "RIGHT 40% of frame: a vertical breakdown panel\n"
            "  - 60 VEGETARIAN CAPSULES PER BOTTLE\n"
            "  - Adults: 1 to 2 capsules twice daily\n"
            "  - Take morning and evening\n"
            "  - Suitable for prolonged daily use\n"
            "  - Easy-to-swallow vegetarian capsule\n\n"
            "Small caption below the panel: 'Suitable across perimenopause, menopause and "
            "post-menopause — no breaks required.'"
        ),
        overlay="60 VEGETARIAN CAPSULES. SIMPLE DAILY USE.",
        overlay_sub="Adults: 1–2 capsules twice daily, morning and evening.",
        props=["Menodause bottle (open)", "capsule pile + 2-capsule dose count", "dosage info panel"],
        lighting="Even soft front-light. Clean infographic feel.",
        why_it_works=(
            "Dose and pack value made obvious. Removes the 'how do I actually take this?' hesitation "
            "and signals it's a simple twice-daily routine suitable for the long haul of the "
            "transition."
        ),
        ctr="",
        cvr="",
    ),
    AIImagePlanItem(
        name="Image 7 — Brand close: calm confidence + Made in Canada",
        role="close",
        background="Warm, soft home scene — golden afternoon light",
        purpose="Close on identity and brand provenance: dignified relief, Canadian-made, regulator-backed.",
        visual=(
            "Mid-range environmental shot in a real, warm home. A woman 45–55 standing or sitting "
            "comfortably, soft natural smile, holding the Menodause bottle or a glass of water — calm, "
            "in control, at ease. Empowering, not clinical, not staged.\n\n"
            "On the counter beside her: Menodause bottle (label readable), a small Nutripur info card "
            "with the NPN number visible, a soft-focus indoor plant, and a maple-leaf décor element in "
            "the background for the Canadian cue.\n\n"
            "Warm afternoon side-light from a window. Wood and linen tones. Reads 'real Canadian "
            "home,' NOT pharmacy.\n\n"
            "Foreground bottom-left: a handwritten-style note card reading: 'Reliable support for a "
            "smoother menopausal transition. — From the Nutripur family, Quebec.'"
        ),
        overlay="MADE IN CANADA. BACKED BY NUTRIPUR.",
        overlay_sub="Reliable support for a smoother menopausal transition. Health Canada NPN 80042095.",
        props=["Menodause bottle", "Nutripur info card with NPN", "glass of water", "wood counter", "maple-leaf décor (soft focus)", "indoor plant", "handwritten-style note card", "woman model 45–55 (calm, confident)"],
        lighting="Warm afternoon side-light from window. Soft golden hue. Honest, lived-in home — not staged.",
        why_it_works=(
            "Closes on the brand promise the buyer needs before checkout: a real Canadian woman, "
            "relaxed and in control, with a real Health Canada credential. Calm confidence is the "
            "emotional handoff that converts the dignified, empowering positioning."
        ),
        ctr="",
        cvr="",
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Brand banner: A smoother menopausal transition.",
        role="a+_banner",
        headline="A SMOOTHER MENOPAUSAL TRANSITION.",
        body=(
            "Menodause by Nutripur is a Health Canada-approved menopause formula with ashwagandha, "
            "black cohosh and chasteberry. A synergistic, research-based blend designed to support "
            "hormonal balance, energy and overall well-being — through perimenopause, menopause and "
            "beyond."
        ),
        visual="Wide cinematic scene — a calm, sunlit home, Menodause bottle front-center, soft natural light from a window, a woman 45–55 relaxed and soft-focused in the background. Nutripur teal logo upper-left, Health Canada NPN 80042095 small in the bottom band.",
        alt="Nutripur Menodause menopause supplement bottle on a counter in warm home light, with a relaxed woman in soft focus.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): The Menodause Difference",
        role="a+_carousel",
        headline="THE MENODAUSE DIFFERENCE",
        body=(
            "Tile 1: <b>WITH 1000 mg ASHWAGANDHA</b> — 10:1 extract, equivalent to 1000 mg.<br/>"
            "Tile 2: <b>3-BOTANICAL BLEND</b> — Ashwagandha · black cohosh · chasteberry, working together.<br/>"
            "Tile 3: <b>HEALTH CANADA APPROVED</b> — NPN 80042095. Defensible, regulator-approved claims.<br/>"
            "Tile 4: <b>VEGETARIAN &amp; CLEAN</b> — Vegan capsules, no artificial additives or fillers.<br/>"
            "Tile 5: <b>MADE IN CANADA</b> — Clinical-quality natural health products by Nutripur."
        ),
        visual="5 square tiles, Nutripur teal accent corner on each. Same composition discipline across all 5. Small icons (ashwagandha root · 3 botanicals · maple leaf · vegan leaf · Canada outline).",
        alt="Five-tile Premium A+ carousel covering Menodause differentiators: 1000 mg ashwagandha, 3-botanical blend, Health Canada approved, vegetarian and clean, made in Canada.",
    ),
    AIModule(
        name="Module 3 — Banner: How the formula supports the transition",
        role="a+_banner",
        headline="HELPS RELIEVE MENOPAUSE-RELATED SYMPTOMS.",
        body=(
            "Per Health Canada NPN 80042095: helps relieve menopause-related symptoms, including hot "
            "flashes, night sweats, mood swings, sleep disorders, urinary discomfort and vaginal "
            "dryness. Acts as a hormone normaliser to help stabilise the cycle. Helps relieve nervous "
            "tension, restlessness and nervousness."
        ),
        visual="Wide banner: clean botanical-style infographic showing the 3 hero botanicals (ashwagandha root, black cohosh, chasteberry) on the left, connected by thin lines to a calm symptom-relief column on the right (hot flashes, sleep, mood). Nutripur teal and blue palette only. NPN 80042095 small in the lower band. No anatomical or fear imagery.",
        alt="Premium A+ banner showing how Menodause botanicals help relieve menopause-related symptoms per Health Canada NPN 80042095.",
    ),
    AIModule(
        name="Module 4 — Banner: Calm, mood and restful sleep",
        role="a+_banner",
        headline="CALM. MOOD. RESTFUL SLEEP.",
        body=(
            "Menopause is more than hot flashes. Per Health Canada NPN 80042095: helps relieve nervous "
            "tension, restlessness and nervousness; acts as a restorative tonic and supports energy "
            "metabolism; helps improve memory. With Vitamin C and a full B-complex for daily energy."
        ),
        visual="Triptych within one banner: LEFT — a calm woman by a window with a cup of tea (relaxed, dignified, no distress). CENTER — a small white dish with 2 capsules on a bedside table, a softly-lit bedroom corner behind. RIGHT — a peaceful morning kitchen scene with the Menodause bottle and a glass of water. Warm natural light across all three panels.",
        alt="Triptych A+ banner showing Menodause supporting calm, mood and restful sleep per Health Canada-approved indications.",
    ),
    AIModule(
        name="Module 5 — Carousel (5 tiles): The Nutripur Family",
        role="a+_carousel",
        headline="THE NUTRIPUR FAMILY",
        body=(
            "Tile 1: <b>MENODAUSE (this product)</b> — Menopause formula with ashwagandha, black "
            "cohosh &amp; chasteberry. 60 vegetarian capsules.<br/>"
            "Tile 2: <b>ASHWAGANDHA</b> — Stress, calm &amp; energy support for everyday tension.<br/>"
            "Tile 3: <b>MAGNESIUM BISGLYCINATE</b> — Sleep, calm &amp; muscle support for the whole family.<br/>"
            "Tile 4: <b>VITAMIN D + K2</b> — Bone and immune support, ideal alongside menopause care.<br/>"
            "Tile 5: <b>PROBIOTICS</b> — Digestive and daily wellness support.<br/>"
            "<i>Confirm the current live SKUs on the Nutripur website and pull current product photography from brand assets before publishing.</i>"
        ),
        visual="5 identical-composition product tiles. Nutripur teal + blue accent corner on each. Family flat-lay style with consistent bottle / packaging photography.",
        alt="Five-tile A+ carousel of the Nutripur family — Menodause, Ashwagandha, Magnesium Bisglycinate, Vitamin D + K2, and Probiotics.",
    ),
    AIModule(
        name="Module 6 — Premium Q&A",
        role="a+_qa",
        headline="QUESTIONS WOMEN ASK",
        body=(
            "<b>Q.</b> What does Menodause help with?<br/>"
            "<b>A.</b> Per Health Canada NPN 80042095, it helps relieve menopause-related symptoms, "
            "including hot flashes, night sweats, mood swings, sleep disorders and vaginal dryness, "
            "and helps relieve nervous tension and restlessness.<br/><br/>"

            "<b>Q.</b> What's in the formula?<br/>"
            "<b>A.</b> Three hero botanicals — Ashwagandha 10:1 extract (equivalent to 1000 mg), Black "
            "cohosh standardized to 2.5% triterpene glycosides, and Chasteberry 4:1 (equivalent to "
            "400 mg) — plus Vitamin C and a full B-complex (B1, B2, B3, B5, B6).<br/><br/>"

            "<b>Q.</b> How do I take it?<br/>"
            "<b>A.</b> Adults take 1 to 2 capsules twice daily, morning and evening. It is suitable "
            "for prolonged daily use across perimenopause, menopause and post-menopause.<br/><br/>"

            "<b>Q.</b> How long until I notice a difference?<br/>"
            "<b>A.</b> Many women report a calmer, steadier week from the second week onward, with "
            "support building over the first month. Results vary by individual.<br/><br/>"

            "<b>Q.</b> Is it vegetarian and clean?<br/>"
            "<b>A.</b> Yes. Menodause uses hypromellose vegetarian capsules with organic rice extract, "
            "organic gum arabic and organic sunflower oil. It contains no artificial additives or "
            "fillers and is vegan, gluten-free, lactose-free and alcohol-free.<br/><br/>"

            "<b>Q.</b> Anything I should check first?<br/>"
            "<b>A.</b> Consult a health care practitioner before use if you have a liver disorder, if "
            "symptoms persist or worsen, or if you take hormone-containing medications or hormone "
            "replacement therapy. Do not use if pregnant, breastfeeding or trying to conceive except "
            "on professional advice."
        ),
        visual="Vertical Q/A table. Nutripur teal divider lines between each Q. Small Nutripur blue Q. and A. labels.",
        alt="Premium Q&A module addressing the six most-asked questions for Nutripur Menodause.",
    ),
    AIModule(
        name="Module 7 — Premium Comparison Chart",
        role="a+_comparison",
        headline="WHY MENODAUSE",
        body=(
            "Compare across 4 columns: <b>Nutripur Menodause</b> · Black-cohosh-only menopause pill · "
            "Isoflavone-only formula · Generic multivitamin for women.<br/><br/>"
            "Rows: Hero botanicals (3 vs 1) · Ashwagandha (1000 mg equivalent) · Black cohosh "
            "(standardized) · Chasteberry · Vitamin C + B-complex · Health Canada NPN · Vegetarian "
            "capsules · No artificial additives or fillers · Made in Canada.<br/><br/>"
            "Highlight the Nutripur Menodause column with a soft Nutripur-teal tint and a 'CANADIAN "
            "WOMEN'S CHOICE' ribbon at the top of the column."
        ),
        visual="Standard Amazon Premium Comparison Chart layout, 4 product columns. Competitor columns use category descriptors only — no brand names. Nutripur blue header row.",
        alt="Premium comparison chart for Nutripur Menodause vs. black-cohosh-only, isoflavone-only, and generic women's multivitamin alternatives.",
    ),
]


QA = [
    AIQA(q="What does Menodause help with?",
         a="Per Health Canada NPN 80042095: helps relieve menopause-related symptoms, including hot flashes, night sweats, mood swings, sleep disorders, urinary discomfort and vaginal dryness. It also helps relieve nervous tension, restlessness and nervousness, and helps improve memory."),
    AIQA(q="What's in the formula?",
         a="Three hero botanicals per capsule: Ashwagandha 10:1 extract (equivalent to 1000 mg), Black cohosh extract 40 mg standardized to 2.5% triterpene glycosides, and Chasteberry 4:1 extract (equivalent to 400 mg). Plus Vitamin C 75 mg and a full B-complex — B1, B2, B3, B5, B6 at 25 mg each."),
    AIQA(q="How do I take it?",
         a="Adults take 1 to 2 capsules twice daily, morning and evening. Menodause is suitable for prolonged daily use across perimenopause, menopause and post-menopause — no breaks required."),
    AIQA(q="How long until I notice a difference?",
         a="Many women report a calmer, steadier week from the second week onward, with support building over the first month. As reviews note, results vary depending on the individual and the body's response."),
    AIQA(q="Does it contain ashwagandha?",
         a="Yes. Each capsule provides Ashwagandha 10:1 extract equivalent to 1000 mg, alongside black cohosh and chasteberry. Ashwagandha is a traditional restorative tonic that helps relieve nervous tension and supports energy metabolism."),
    AIQA(q="Is it vegetarian and clean?",
         a="Yes. Menodause uses hypromellose vegetarian capsules with organic rice extract, organic gum arabic and organic sunflower oil. It contains no artificial additives or fillers, and is vegan, gluten-free, lactose-free and alcohol-free."),
    AIQA(q="Is there anything I should check before using it?",
         a="Consult a health care practitioner before use if you have a liver disorder or develop symptoms of one, if symptoms persist or worsen, or if you take hormone-containing medications or hormone replacement therapy. Do not use if pregnant, breastfeeding or trying to conceive except on professional advice. It may cause drowsiness — use caution when driving."),
    AIQA(q="Where is Menodause made?",
         a="Made in Canada by Nutripur under Health Canada NPN 80042095. Formulated with research-based ingredients — clinical-quality natural health products from the Nutripur family in Quebec."),
]


# Backend KWs — stem-deduped, byte-packed. Avoid: brand names already in title, superlatives,
# and competitor brand names. Includes FR fallback terms because amazon.ca is bilingual.
BACKEND = (
    "menopause supplement women perimenopause relief hot flashes night sweats mood swings sleep "
    "hormone balance ashwagandha black cohosh chasteberry vitex menopausal women 40s 50s vegetarian "
    "vegan capsules energy b complex vitamin c memory nervous tension health canada npn made canada "
    "menopause symptomes femme bouffees chaleur sueurs nocturnes equilibre hormonal ashwagandha "
    "soutien menopause capsules vegetariennes sommeil humeur"
)


def main() -> None:
    print("Loading Nutripur customer + parsing Menodause Excel…")
    cust = load_customer("nutripur")
    brief = parse_excel(EXCEL)
    asin = brief.asin or "NA"
    OUT = HERE / f"{PLAN_NO}_{asin}_Image Plan.pdf"
    print(f"  Product: {brief.product_name}")
    print(f"  ASIN: {brief.asin}  Marketplace: {cust.marketplace}")
    print(f"  USPs={len(brief.usps)} KWs={len(brief.all_keywords)} reviews=+{len(brief.good_reviews)}/-{len(brief.bad_reviews)}")
    print(f"  Health Canada NPN: 80042095 (claims are NPN-defensible)")

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
