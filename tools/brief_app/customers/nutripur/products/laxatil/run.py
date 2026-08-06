"""Nutripur LAXATIL — Natural Herbal Laxative with Aloe (60 vegetarian capsules)
Hand-written KW-led copy injected into the branded ReportLab pipeline.

Marketplace: amazon.ca (Canada)
Health Canada NPN: 02241124 — defensible traditional-use structure/function claims.

Health-claim compliance baseline (NPN 02241124 approved):
  - "Traditional herbal medicine (laxative) for the gentle relief of occasional constipation"
  - Onset of effect: within 6 to 12 hours (take at bedtime)
  - For occasional use only; not for more than 7 consecutive days without advice

Never (Amazon + Health Canada):
  - cure / treat / prevent disease  (these are blocking-violation words)
  - best / #1 / ultimate / guaranteed / miracle
  - competitor brand names
  - "$" / price language / URLs / ".com" in customer-facing copy
  - crude or undignified imagery (sensitive category — keep tasteful)
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
PLAN_NO = "05"   # SEO listing no. -> output named 0X_<ASIN>_Image Plan.pdf


# ===== KW-led copy — Health Canada NPN compliant =====

TITLE = (
    "Nutripur LAXATIL Natural Laxative for Constipation Relief — Herbal Aloe, Mallow &amp; Buckthorn · "
    "Gentle Relief of Occasional Constipation · 60 Vegetarian Capsules · Health Canada NPN 02241124 · Vegan"
)

BULLETS = [
    "<b>GENTLE RELIEF OF OCCASIONAL CONSTIPATION</b> — A traditional herbal laxative formula approved by "
    "Health Canada (NPN 02241124). Used in traditional herbal medicine for the gentle relief of occasional "
    "constipation and the bloating that can come with it. Designed to work with your body, not against it.",

    "<b>WORKS OVERNIGHT — RELIEF IN 6 TO 12 HOURS</b> — Take one capsule at bedtime with a full glass of "
    "water and let it work while you sleep. Most people feel comfortable relief by morning, on their own "
    "schedule and in the privacy of home. One capsule a day is all it takes.",

    "<b>FOUR SOOTHING HERBS · ALOE, MALLOW, BUCKTHORN &amp; RHUBARB</b> — Each vegetarian capsule delivers "
    "aloe leaf 105 mg, mallow leaf 90 mg, buckthorn bark 75 mg and rhubarb root 30 mg. Mallow and aloe are "
    "traditionally chosen to keep the formula gentle, so relief feels comfortable, not harsh.",

    "<b>CLEAN, PLANT-BASED &amp; VEGAN</b> — Vegetarian (hypromellose) capsules with no artificial fillers. "
    "Gluten-free, lactose-free, alcohol-free, GMO-free and free of preservatives. Easy-to-swallow capsule "
    "format with no chalky powders, no laxative tea to brew and no unpleasant aftertaste.",

    "<b>60 CAPSULES · MADE IN CANADA BY NUTRIPUR</b> — A 60-capsule bottle for occasional use as you need it. "
    "Manufactured in Canada in a GMP-certified facility. For occasional use only; do not use for more than 7 "
    "consecutive days without talking to a health care practitioner.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="White canvas with a soft teal (#E8F5F2) tint across the bottom 15% for grounding. Same background across all 3 options for a clean A/B test.",
        purpose="Win the click in a constipation-relief grid crowded with harsh-looking pharma laxatives. Test all 3, keep the winner.",
        visual=(
            "Brief the designer to mock ALL 3 options below. Brand picks the winner via Amazon Manage Your "
            "Experiments. Each option uses ONE callout, ONE action cue, ONE supporting prop — clean, not stacked. "
            "Dignified and calm throughout — this is a sensitive category, keep it tasteful and reassuring.\n\n"

            "▸ OPTION A — NPN CREDENTIAL HERO (owns the trust signal)\n"
            "Center: LAXATIL bottle front-facing, label fully readable, slight elevated 3/4 turn. Bottle "
            "occupies ~70% of frame. To the bottle's lower-right: 2 vegetarian capsules and a small, fresh "
            "aloe-leaf cross-section for the natural-ingredient cue.\n"
            "ONE CALLOUT — top-right corner badge: 'HEALTH CANADA NPN 02241124' (Nutripur blue background, "
            "white text, small Canada-leaf icon).\n"
            "ONE ACTION CUE: the two capsules placed as if just tipped from the bottle.\n"
            "Why it wins: in the amazon.ca grid, no herbal competitor leads with the NPN number visible. The "
            "Health Canada credential is the strongest single trust signal a Canadian shopper can see before "
            "clicking on a sensitive purchase.\n\n"

            "▸ OPTION B — GENTLE + OVERNIGHT (defuses the 'will it be harsh?' fear)\n"
            "Center: LAXATIL bottle, label readable, slightly left of center. Right of the bottle: a small "
            "moon / pre-dawn window motif and a single capsule beside a glass of water, signalling the "
            "bedtime ritual. Soft fresh mallow flower or aloe slice as the natural prop.\n"
            "ONE CALLOUT — top-left corner badge: 'GENTLE RELIEF · WORKS IN 6–12 HOURS' (Nutripur green "
            "background, white text).\n"
            "Why it wins: the #1 hesitation in this category is 'will it cramp / will it be harsh?' This image "
            "promises gentle, overnight, take-one-and-sleep relief — exactly the calm reassurance the buyer "
            "is scanning for.\n\n"

            "▸ OPTION C — 4 SOOTHING HERBS (owns the natural differentiator)\n"
            "Center: LAXATIL bottle. Floating around the bottle in a clean radial layout: 4 small botanical "
            "icons labeled ALOE · MALLOW · BUCKTHORN · RHUBARB, each a simple leaf/root line "
            "illustration in Nutripur green on a soft white halo.\n"
            "ONE CALLOUT — bottom-right corner badge: '4 HERBS · VEGAN · GLUTEN-FREE' (Nutripur blue "
            "background, white text).\n"
            "Why it wins: most laxatives in the grid look like single-ingredient pharma pills. Only LAXATIL "
            "visibly stacks four traditional soothing herbs — the natural, plant-based story at a glance.\n\n"

            "Across all 3: bottle dominant ~70%, callout ~6% of frame, supporting prop fills remainder. Same "
            "lighting, same background gradient, same colour temperature so the split test isolates "
            "composition, not light/colour."
        ),
        overlay="",  # Amazon main-image policy bans overlay text — keep empty for Image 1
        overlay_sub="",
        props=[
            "OPTION A: bottle + 2 vegetarian capsules + aloe-leaf cross-section + NPN badge",
            "OPTION B: bottle + single capsule + glass of water + moon/pre-dawn motif + mallow/aloe prop + gentle/overnight badge",
            "OPTION C: bottle + 4 botanical icons in radial halo + natural/vegan badge",
        ],
        lighting="Soft top key (5000K daylight balanced) with gentle fill from camera-right. Slight backlight on the bottle to make the LAXATIL label pop. Same lighting across all 3 options to keep the A/B test clean.",
        why_it_works=(
            "Three angles against three different buyer triggers: A wins on credential trust (NPN), B wins on "
            "the harshness fear (gentle, overnight), C wins on the natural / plant-based differentiation. One "
            "callout, one action cue, one supporting prop each. Clean enough to read on a mobile thumbnail."
        ),
        ctr=(
            "Bottle-dominant with a single high-contrast Nutripur-blue/green badge reads instantly at "
            "thumbnail size against a grid of identical white pharma-laxative boxes. The NPN number (Option A) "
            "and 'gentle / 6–12 hours' (Option B) are pattern interrupts no commodity competitor shows."
        ),
        cvr=(
            "Each option pre-answers the purchase fear before the click: legitimacy (Health Canada), comfort "
            "(gentle / overnight), and clean formulation (4 herbs / vegan). The calm, dignified styling lowers "
            "the embarrassment friction unique to this sensitive category."
        ),
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: Gentle relief while you sleep",
        role="hook",
        background="Soft teal #E8F5F2 (Nutripur mood) — calm, clinical-natural, never pharma-sterile",
        purpose="Reverse the #1 buyer fear (harsh, urgent, cramping laxatives) with a calm overnight ritual.",
        visual=(
            "Center-left: LAXATIL bottle beside a single vegetarian capsule and a tall glass of water on a "
            "calm bedside surface. Soft pre-dawn light through a blurred window in the background. To the right, "
            "a simple, elegant timeline graphic: a crescent-moon icon labelled 'BEDTIME · 1 capsule + water' "
            "flowing along a thin Nutripur-green line to a sunrise icon labelled 'MORNING · comfortable relief'. "
            "Small caption between them: 'works in 6 to 12 hours'.\n\n"
            "Keep it serene and dignified — a quiet bedside scene, not a bathroom. The promise is calm, "
            "private, overnight relief on your own schedule."
        ),
        overlay="GENTLE RELIEF WHILE YOU SLEEP.",
        overlay_sub="One capsule at bedtime &mdash; comfortable relief of occasional constipation by morning, in 6 to 12 hours.",
        props=["LAXATIL bottle", "single vegetarian capsule", "tall glass of water", "moon-to-sunrise timeline graphic", "soft blurred window"],
        lighting="Soft pre-dawn ambient light, cool-to-warm gradient (window light). Gentle shadow under the bottle. Calm, restful mood — clarity over drama.",
        why_it_works=(
            "Directly defuses the category's top objection from the reviews and the buyer's mind: that "
            "laxatives are harsh, urgent and unpredictable. The bedtime-to-morning timeline reframes the "
            "product as gentle, scheduled and private — the exact reassurance this shopper needs."
        ),
        ctr=(
            "The moon-to-sunrise timeline is an instantly legible visual metaphor that stops the scroll — it "
            "answers 'when and how does this work?' in one glance, which a plain pill bottle cannot."
        ),
        cvr=(
            "Converts the hesitant shopper by removing the fear of harsh, unpredictable timing: take it, sleep, "
            "wake up comfortable. Privacy and control are the emotional triggers that close a sensitive-category sale."
        ),
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: 4 soothing herbs and what's in every capsule",
        role="educate",
        background="White with a soft Nutripur-green ribbon footer",
        purpose="Earn trust and justify the natural premium by showing the real, regulator-listed formula.",
        visual=(
            "Top of frame: 'WHAT'S IN EVERY CAPSULE' headline in Nutripur blue, sentence case. Below, a clean "
            "four-row table or four soft-edged ingredient cards, each with a simple botanical line icon:\n\n"
            "ROW 1 — Aloe (Aloe capensis) leaf — 105 mg\n"
            "ROW 2 — Mallow (Malva sylvestris) leaf — 90 mg\n"
            "ROW 3 — Buckthorn (Rhamnus frangula) bark — 75 mg\n"
            "ROW 4 — Rhubarb (Rheum palmatum) root — 30 mg\n\n"
            "Short tag beside the group: 'Mallow &amp; aloe are traditionally chosen to keep the formula "
            "gentle.' Small strip below: 'Vegetarian capsule · organic rice extract blend · organic gum "
            "arabic · organic sunflower oil. No artificial fillers.'\n\n"
            "Footer ribbon (Nutripur green): 'Traditional herbal medicine — Health Canada NPN 02241124.'"
        ),
        overlay="FOUR SOOTHING HERBS. ONE GENTLE FORMULA.",
        overlay_sub="Aloe &middot; Mallow &middot; Buckthorn &middot; Rhubarb &mdash; the full formula, listed honestly.",
        props=["4 ingredient cards", "4 botanical line icons (aloe, mallow, buckthorn, rhubarb)", "non-medicinal strip", "NPN citation footer"],
        lighting="Flat clean studio. Educational module — readability beats atmosphere.",
        why_it_works=(
            "Showing the real milligram amounts and the exact botanical names signals an honest, regulated "
            "product, not a mystery blend. Naming mallow and aloe as the 'gentle' herbs pre-answers the "
            "harshness fear with the formula itself."
        ),
        ctr=(
            "A transparent ingredient table is a recognised 'legit brand' pattern shoppers open to verify a "
            "supplement, pulling secondary clicks from the gallery."
        ),
        cvr=(
            "Real amounts plus the 'gentle herbs' framing justify choosing a natural formula over a cheap "
            "single-ingredient stimulant, defusing the review concern that gentleness isn't universal."
        ),
    ),
    AIImagePlanItem(
        name="Image 4 — Lifestyle: Comfortable mornings, back to your day",
        role="desire",
        background="Bright, airy kitchen / living space, warm morning light from camera-right",
        purpose="Let the buyer self-cast into the relief — calm, comfortable, dignified, back to normal life.",
        visual=(
            "Warm, relaxed morning scene. An adult (35–60, in PROFILE or from behind, face not the focus) "
            "in comfortable home clothes, relaxed and at ease — holding a mug of tea by a sunny window, or "
            "stretching gently — body language reads 'comfortable and light again', NOT in distress.\n\n"
            "FOREGROUND right edge: LAXATIL bottle (label facing camera) beside a single capsule and a glass "
            "of water on the counter, signalling last night's routine. A small bowl of fruit or a plant nearby "
            "for a fresh, healthy cue.\n\n"
            "Keep it tasteful and dignified — the feeling is relief and comfort, never the problem itself. "
            "Soft natural morning light, airy and clean. Use a stock model with release; avoid logos."
        ),
        overlay="COMFORTABLE AGAIN. BACK TO YOUR MORNING.",
        overlay_sub="Gentle, overnight relief of occasional constipation &mdash; so you can get on with your day.",
        props=["LAXATIL bottle", "single capsule + glass of water", "mug of tea", "bowl of fruit or plant", "adult model (profile / from behind)"],
        lighting="Warm morning side-light from camera-right. Soft, airy, lived-in. Honest natural-clinical, not staged.",
        why_it_works=(
            "Owns the emotional payoff the reviews describe — relief and comfort — without depicting the "
            "problem. A relaxed adult in a bright home is the aspirational 'after' state the buyer is paying "
            "for, kept brand-safe with no face-forward portrait."
        ),
        ctr=(
            "A calm human lifestyle frame stands out against competitors' clinical pill-and-box galleries and "
            "invites the emotional 'that could be me' click."
        ),
        cvr=(
            "Sells the outcome — feeling light and back to normal — which is what closes the sale. The "
            "dignified, relief-focused framing lowers the embarrassment barrier specific to this category."
        ),
    ),
    AIImagePlanItem(
        name="Image 5 — Trust: 4 quality credentials in one frame",
        role="trust",
        background="White with soft teal panels behind each badge for separation",
        purpose="Stack the strongest filters a Canadian shopper scans for and defuse 'is this brand legit?'.",
        visual=(
            "Centered macro of the LAXATIL bottle (label facing camera). Four trust badges in the corners:\n\n"
            "  • TOP-LEFT — HEALTH CANADA NPN 02241124 (small Canada-leaf icon)\n"
            "  • TOP-RIGHT — VEGAN · PLANT-BASED (small leaf icon)\n"
            "  • BOTTOM-LEFT — MADE IN CANADA · GMP CERTIFIED (small Canada outline)\n"
            "  • BOTTOM-RIGHT — GLUTEN-FREE · LACTOSE-FREE · NO PRESERVATIVES (small check icon)\n\n"
            "Below the bottle, a thin strip: 'Vegetarian capsule. No artificial fillers. Alcohol-free. GMO-free. "
            "Manufactured in Canada by Nutripur.'"
        ),
        overlay="HEALTH CANADA APPROVED. CLEAN. CANADIAN-MADE.",
        overlay_sub="NPN 02241124 &middot; Vegan &middot; Gluten-Free &middot; GMP Certified &middot; No preservatives",
        props=["LAXATIL bottle (center)", "4 badge graphics in corners", "thin supporting strip"],
        lighting="Studio even light. Hard catch-light on the bottle. Badges legible at thumbnail size.",
        why_it_works=(
            "Stacks the four filters that matter for a Canadian shopper buying a natural laxative: regulator "
            "(NPN), plant-based formulation, country of origin / GMP, and clean / allergen-free. Few commodity "
            "competitors lead with all four."
        ),
        ctr=(
            "Four crisp badges around the bottle create a high-information, high-trust thumbnail that earns the "
            "verification click from cautious shoppers."
        ),
        cvr=(
            "Directly answers 'can I trust this?' for an ingested product, removing the legitimacy objection "
            "that stalls supplement purchases."
        ),
    ),
    AIImagePlanItem(
        name="Image 6 — How to use: One capsule, one glass of water, at bedtime",
        role="desire",
        background="Soft teal #E8F5F2 — same as Image 2 for visual rhythm",
        purpose="Remove dosing friction and reinforce the simple, gentle, occasional-use ritual.",
        visual=(
            "Split-frame infographic.\n\n"
            "LEFT 55%: a calm bedside flat-lay — LAXATIL bottle (open), one vegetarian capsule and a glass "
            "of water, with a soft moon icon in the corner for the bedtime cue.\n\n"
            "RIGHT 45%: a clean vertical step panel\n"
            "  • TAKE 1 capsule at bedtime\n"
            "  • WITH a full glass of water\n"
            "  • RELIEF in 6 to 12 hours — by morning\n"
            "  • FOR occasional use as needed\n"
            "  • 60 capsules per bottle\n\n"
            "Small caption: 'Adults. For occasional use only — do not use for more than 7 consecutive days "
            "without talking to a health care practitioner.'"
        ),
        overlay="ONE CAPSULE. ONE GLASS OF WATER. AT BEDTIME.",
        overlay_sub="Simple occasional-use routine &mdash; 60 vegetarian capsules per bottle.",
        props=["LAXATIL bottle (open)", "single capsule", "glass of water", "moon icon", "numbered step panel"],
        lighting="Even soft front-light. Clean infographic feel.",
        why_it_works=(
            "Makes the routine effortless and unintimidating: one capsule, one glass of water, sleep. Including "
            "the 7-day occasional-use caution sets honest expectations and builds trust rather than over-promising."
        ),
        ctr=(
            "A numbered how-to-use panel is a recognised gallery format shoppers open to check 'is this easy "
            "and safe to take?', earning a secondary click."
        ),
        cvr=(
            "Eliminates dosing uncertainty and signals an honest, gentle product, defusing the review concern "
            "about unpredictable timing and harshness."
        ),
    ),
    AIImagePlanItem(
        name="Image 7 — Brand close: Made in Canada by Nutripur",
        role="close",
        background="Warm, soft natural setting with subtle Canadian cue",
        purpose="Close on brand identity and provenance — gentle, natural, trustworthy, Canadian.",
        visual=(
            "Mid-range hero of the LAXATIL bottle on a warm wood surface, label readable. Beside it: a small "
            "Nutripur info card with the NPN number visible, fresh aloe and mallow sprigs, and a soft-focused "
            "maple-leaf or Canada-flag motif in the background. An indoor plant adds a calm, natural note.\n\n"
            "Warm afternoon side-light. The mood reads 'trusted natural Canadian brand', calm and dignified — "
            "never a pharmacy aisle.\n\n"
            "Foreground bottom-left: a small handwritten-style note card: 'Gentle, natural relief — made in "
            "Canada by Nutripur.'"
        ),
        overlay="MADE IN CANADA. BACKED BY NUTRIPUR.",
        overlay_sub="Gentle, natural relief of occasional constipation. Health Canada NPN 02241124.",
        props=["LAXATIL bottle", "Nutripur info card with NPN", "aloe + mallow sprigs", "wood surface", "maple-leaf / Canada-flag motif (soft focus)", "indoor plant", "handwritten-style note card"],
        lighting="Warm afternoon side-light. Soft natural tones. Honest, calm, not staged.",
        why_it_works=(
            "Closes on the reassurance the buyer needs before checkout for an ingested, sensitive product: a "
            "real Canadian brand, a visible Health Canada credential, and natural ingredients on show. Brand "
            "provenance is the final trust handoff."
        ),
        ctr=(
            "A warm, branded close frame gives the gallery a confident finish and reinforces recall of the "
            "Nutripur name and NPN."
        ),
        cvr=(
            "Provenance plus the visible NPN converts the last hesitation: this is a legitimate, gentle, "
            "Canadian-made natural product worth trusting."
        ),
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Brand banner: Gentle, natural relief.",
        role="a+_banner",
        headline="GENTLE, NATURAL RELIEF.",
        body=(
            "LAXATIL by Nutripur is a traditional herbal laxative for the gentle relief of occasional "
            "constipation. Four soothing herbs in a vegetarian capsule, taken once at bedtime to help you "
            "wake up comfortable. Approved by Health Canada, NPN 02241124."
        ),
        visual="Wide calm banner — LAXATIL bottle front-center on a soft wood surface, fresh aloe and mallow sprigs beside it, soft natural morning light from a window, glass of water in the frame. Nutripur logo upper-left, NPN 02241124 small in the bottom band.",
        alt="Nutripur LAXATIL natural herbal laxative bottle with aloe and mallow on a wood surface in soft morning light.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): The LAXATIL Difference",
        role="a+_carousel",
        headline="THE LAXATIL DIFFERENCE",
        body=(
            "Tile 1: <b>GENTLE RELIEF</b> &mdash; Traditional herbal laxative for the gentle relief of occasional constipation.<br/>"
            "Tile 2: <b>WORKS OVERNIGHT</b> &mdash; One capsule at bedtime; comfortable relief in 6 to 12 hours.<br/>"
            "Tile 3: <b>4 SOOTHING HERBS</b> &mdash; Aloe, mallow, buckthorn and rhubarb in every capsule.<br/>"
            "Tile 4: <b>CLEAN &amp; VEGAN</b> &mdash; Vegetarian capsule, gluten-free, no preservatives, no fillers.<br/>"
            "Tile 5: <b>HEALTH CANADA APPROVED</b> &mdash; NPN 02241124. Made in Canada by Nutripur."
        ),
        visual="5 square tiles, Nutripur blue/green accent corner on each. Same composition discipline across all 5. Small icons (leaf · moon · 4 botanicals · vegan leaf · maple leaf).",
        alt="Five-tile A+ carousel covering LAXATIL differentiators: gentle relief, works overnight, four herbs, clean and vegan, Health Canada approved.",
    ),
    AIModule(
        name="Module 3 — Banner: How the formula stays gentle",
        role="a+_banner",
        headline="FOUR HERBS, CHOSEN TO STAY GENTLE.",
        body=(
            "Each vegetarian capsule delivers aloe leaf 105 mg, mallow leaf 90 mg, buckthorn bark 75 mg and "
            "rhubarb root 30 mg. Mallow and aloe are traditionally chosen to soothe, so relief feels "
            "comfortable rather than harsh. No artificial fillers. Health Canada NPN 02241124."
        ),
        visual="Wide banner: clean botanical-style infographic showing the four herbs (aloe leaf, mallow flower, buckthorn bark, rhubarb root) as soft line illustrations, each with its milligram amount on a label. Nutripur green and blue palette only. NPN 02241124 small in the lower band.",
        alt="A+ banner showing the four LAXATIL herbs with milligram amounts per capsule, per Health Canada NPN 02241124.",
    ),
    AIModule(
        name="Module 4 — Banner: The simple bedtime routine",
        role="a+_banner",
        headline="ONE CAPSULE. AT BEDTIME. RELIEF BY MORNING.",
        body=(
            "Take one capsule with a full glass of water at bedtime and let it work while you sleep. Most "
            "people feel comfortable relief within 6 to 12 hours. For occasional use only — do not use for "
            "more than 7 consecutive days without talking to a health care practitioner."
        ),
        visual="Triptych within one banner: LEFT — capsule and glass of water on a bedside table, soft evening light, moon motif. CENTER — calm dark window, bottle in soft focus, signalling overnight. RIGHT — bright morning kitchen, person (profile, no face focus) relaxed with a mug of tea. Warm-to-cool natural light across the three panels.",
        alt="Triptych A+ banner showing the LAXATIL bedtime-to-morning routine: take at night, works overnight, comfortable in the morning.",
    ),
    AIModule(
        name="Module 5 — Carousel (5 tiles): The Nutripur Family for Canadian Households",
        role="a+_carousel",
        headline="THE NUTRIPUR FAMILY",
        body=(
            "Tile 1: <b>LAXATIL (this product)</b> &mdash; Natural herbal laxative with aloe for the gentle "
            "relief of occasional constipation. 60 vegetarian capsules.<br/>"
            "Tile 2: <b>DIGESTIVE &amp; GUT SUPPORT</b> &mdash; Everyday digestive comfort to pair with occasional relief.<br/>"
            "Tile 3: <b>PROBIOTICS</b> &mdash; Daily support for a balanced gut and regular routine.<br/>"
            "Tile 4: <b>MAGNESIUM BISGLYCINATE</b> &mdash; Calm, sleep and everyday muscle comfort for the whole family.<br/>"
            "Tile 5: <b>GENIUS Kids &amp; Teens</b> &mdash; Omega-3 brain support for the younger members of the household.<br/>"
            "<i>Confirm the current companion SKUs on the Nutripur website and pull product photography from brand assets.</i>"
        ),
        visual="5 identical-composition product tiles. Nutripur blue + green accent corner on each. Family flat-lay style with consistent bottle / packaging photography.",
        alt="Five-tile A+ carousel of the Nutripur family — LAXATIL, digestive support, probiotics, magnesium bisglycinate, and GENIUS Kids & Teens.",
    ),
    AIModule(
        name="Module 6 — Premium Q&A",
        role="a+_qa",
        headline="QUESTIONS CUSTOMERS ASK",
        body=(
            "<b>Q.</b> Is LAXATIL gentle?<br/>"
            "<b>A.</b> LAXATIL is used in traditional herbal medicine for the gentle relief of occasional "
            "constipation. Mallow and aloe are traditionally chosen to keep the formula soothing. Sensitivity "
            "varies from person to person, so start with the recommended single capsule.<br/><br/>"

            "<b>Q.</b> How fast does it work?<br/>"
            "<b>A.</b> Take one capsule at bedtime with a full glass of water; most people feel comfortable "
            "relief within 6 to 12 hours — typically by the next morning.<br/><br/>"

            "<b>Q.</b> How often can I take it?<br/>"
            "<b>A.</b> LAXATIL is for occasional use. Do not use for more than 7 consecutive days without "
            "talking to a health care practitioner.<br/><br/>"

            "<b>Q.</b> What's in it?<br/>"
            "<b>A.</b> Four herbs per vegetarian capsule: aloe leaf 105 mg, mallow leaf 90 mg, buckthorn bark "
            "75 mg and rhubarb root 30 mg. No artificial fillers, gluten, lactose, alcohol or preservatives.<br/><br/>"

            "<b>Q.</b> Is it vegan and gluten-free?<br/>"
            "<b>A.</b> Yes. LAXATIL uses a vegetarian (hypromellose) capsule and is vegan, gluten-free, "
            "lactose-free and GMO-free.<br/><br/>"

            "<b>Q.</b> Can I take it while pregnant or breastfeeding?<br/>"
            "<b>A.</b> Pregnant and breastfeeding women should talk to a health care practitioner before use."
        ),
        visual="Vertical Q/A table. Nutripur green divider lines between each Q. Small Nutripur blue Q. and A. labels.",
        alt="Premium Q&A module addressing the six most-asked customer questions for Nutripur LAXATIL.",
    ),
    AIModule(
        name="Module 7 — Premium Comparison Chart",
        role="a+_comparison",
        headline="WHY LAXATIL",
        body=(
            "Compare across 4 columns: <b>Nutripur LAXATIL</b> &middot; Conventional stimulant laxative tablet "
            "&middot; Osmotic laxative powder &middot; Laxative tea.<br/><br/>"
            "Rows: Herbal blend (4 soothing herbs) &middot; Positioned for gentle relief &middot; Works overnight "
            "(6–12 hours) &middot; Vegetarian capsule format &middot; Vegan / gluten-free &middot; No "
            "preservatives or fillers &middot; Health Canada NPN &middot; Made in Canada.<br/><br/>"
            "Highlight the Nutripur LAXATIL column with a soft Nutripur-green tint and a 'GENTLE &amp; NATURAL' "
            "ribbon at the top of the column."
        ),
        visual="Standard Amazon Premium Comparison Chart layout, 4 product columns. Competitor columns use category descriptors only — no brand names. Nutripur blue header row.",
        alt="Premium comparison chart for Nutripur LAXATIL vs. conventional stimulant tablet, osmotic powder, and laxative tea alternatives.",
    ),
]


QA = [
    AIQA(q="Is LAXATIL gentle?",
         a="LAXATIL is used in traditional herbal medicine for the gentle relief of occasional constipation, and mallow and aloe are traditionally chosen to keep the formula soothing. Sensitivity varies from person to person, so start with the recommended single capsule at bedtime."),
    AIQA(q="How fast does it work?",
         a="Take one capsule at bedtime with a full glass of water. Most people feel comfortable relief within 6 to 12 hours, typically by the next morning. Timing can vary from person to person."),
    AIQA(q="How often can I take it?",
         a="LAXATIL is intended for occasional use as needed. Do not use it for more than 7 consecutive days without talking to a health care practitioner."),
    AIQA(q="What is in the formula?",
         a="Each vegetarian capsule contains aloe (Aloe capensis) leaf 105 mg, mallow (Malva sylvestris) leaf 90 mg, buckthorn (Rhamnus frangula) bark 75 mg and rhubarb (Rheum palmatum) root 30 mg. Non-medicinal ingredients: hypromellose vegetarian capsule, organic rice extract blend, organic gum arabic and organic sunflower oil. No artificial fillers."),
    AIQA(q="Is LAXATIL vegan and gluten-free?",
         a="Yes. LAXATIL uses a vegetarian (hypromellose) capsule and is vegan, gluten-free, lactose-free, alcohol-free and GMO-free, with no preservatives."),
    AIQA(q="How many capsules are in a bottle and how long does it last?",
         a="There are 60 vegetarian capsules per bottle. At the recommended one capsule per occasion, a bottle covers many separate occasions. LAXATIL is for occasional use, not daily long-term use."),
    AIQA(q="Can I take it while pregnant or breastfeeding?",
         a="Pregnant and breastfeeding women should talk to a health care practitioner before using LAXATIL."),
]


# Backend KWs — stem-deduped, byte-packed. Avoid: brand names already in title, superlatives.
# Includes FR fallback terms because amazon.ca is bilingual.
BACKEND = (
    "constipation relief adults laxative herbal natural gentle occasional bloating gas digestive aloe "
    "mallow buckthorn rhubarb vegetarian capsule vegan plant based stool regularity bedtime overnight "
    "laxatif constipation soulagement doux naturel intestinal digestion canada"
)


def main() -> None:
    print("Loading Nutripur customer + parsing LAXATIL Excel…")
    cust = load_customer("nutripur")
    brief = parse_excel(EXCEL)
    asin = brief.asin or "NA"
    OUT = HERE / f"{PLAN_NO}_{asin}_Image Plan.pdf"
    print(f"  Product: {brief.product_name}")
    print(f"  ASIN: {brief.asin}  Marketplace: {cust.marketplace}")
    print(f"  USPs={len(brief.usps)} KWs={len(brief.all_keywords)} reviews=+{len(brief.good_reviews)}/-{len(brief.bad_reviews)}")
    print(f"  Health Canada NPN: 02241124 (traditional-use claims are NPN-defensible)")

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
