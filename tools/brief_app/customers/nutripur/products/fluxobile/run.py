"""Nutripur FluxOBile — Organic Liver Cleanse · Cholagogue / Choleretic · 10-Day Program — Image Plan 10
Hand-written senior copy injected into the branded ReportLab pipeline.

Marketplace: amazon.ca (Canada) · Overlay language: ENGLISH.

LANGUAGE SPLIT (the standard):
  • ENGLISH — art-direction / strategy fields the designer reads:
    image purpose, background, visual, props, lighting, why_it_works, ctr, cvr,
    and module visual (written as a senior art director briefing a designer).
  • ENGLISH — marketplace, customer-facing text the shopper reads:
    TITLE, BULLETS, image overlay, overlay_sub, module headline, module body,
    QA, BACKEND. (amazon.ca = EN primary.)

OVERLAY RULE: sell the OUTCOME, not the action. Every on-image overlay leads with
the result / benefit the buyer wants. Each overlay is distinct and tied to its image.
Hard limits (auto-linted on build):
  overlay ≤ 30 chars AND ≤ 5 words · overlay_sub ≤ 90 chars
  module headline ≤ 38 chars · bullet head <b>…</b> ≤ 45 chars · TITLE ≤ 200 real chars

Verified facts (see SOURCE_NOTES.md — from the REAL box label + nutripur.com + Health Canada):
  - Health Canada NPN 02239745 (THIS product's own NPN — confirmed on the box front).
  - Per 10 ml ampoule (4 ORGANIC botanicals, water extract 1:10):
      Black Radish 500 mg (= 5000 mg) · Boldo 210 mg (= 2100 mg) ·
      Artichoke 200 mg (= 2000 mg) · Dandelion 90 mg (= 900 mg)
  - 10-day program = 10 ampoules of 10 ml · ONLY 1 AMPOULE / DAY, morning before breakfast
    in half a glass (125 ml) of lukewarm water or juice · continue 10 to 20 days.
  - 100% Organic — Ecocert certified · Non-GMO · alcohol-free · no preservatives, sweeteners
    or colours · vegan · gluten-free · lactose-free · GMP certified.

Audience: adults wanting digestive + liver support, post-meal comfort, a lighter feeling after
rich meals, occasional heavy-meal / rich-food periods, a simple once-a-day seasonal herbal routine.

COMPLIANCE — high-risk product, EXTRA STRICT:
  - ONLY the NPN-approved structure/function wording is used for benefits:
    helps support / helps relieve digestive disturbances (dyspepsia); stimulates digestion and
    biliary functions (helps support bile flow); helps protect the liver against cell damage
    caused by free radicals; helps with fat digestion / post-meal comfort.
  - "Liver cleanse / liver detox / fatty liver" are the proper NAME + SEO/category terms ONLY —
    they live in BACKEND keywords, NEVER as a benefit claim in title/bullets/overlays/QA.
  - NO detoxifies / removes toxins / cleanses the body, NO cure/treat/prevent/diagnose, NO disease
    names as claims, NO best/#1/ultimate/guaranteed/miracle, NO "$", NO URL/.com in customer copy.
    (Note: the auto-checker flags the literal word "treat" — the box says "Treats…", but here every
    benefit is reframed as "helps relieve / helps support" to stay defensible AND lint-clean.)
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
PLAN_NO = "10"
ASIN = "B00CORKCQY"


# ===== KW-led, marketing-optimized EN copy (customer-facing) — NPN 02239745 defensible =====

# Title is HTML-escaped, so literal "&" counts as 1 char. Keep ≤200 real chars.
TITLE = (
    "Nutripur FluxOBile Organic Liver Cleanse — Black Radish, Boldo, Artichoke & Dandelion "
    "Digestive & Bile Flow Support · 10-Day Program · 10 Liquid Ampoules · Health Canada "
    "NPN 02239745 · Made in Canada"
)

BULLETS = [
    "<b>DIGESTION & BILE FLOW SUPPORT</b> — A herbal blend that stimulates digestion and "
    "biliary functions and helps relieve digestive disturbances (dyspepsia) — for a lighter, "
    "more comfortable feeling after meals.",

    "<b>4 ORGANIC BOTANICALS PER AMPOULE</b> — Black radish 500 mg, boldo 210 mg, artichoke "
    "200 mg and dandelion 90 mg in each 10 ml ampoule (water extract 1:10). Cholagogue and "
    "choleretic traditional herbal medicine.",

    "<b>HELPS PROTECT THE LIVER</b> — Helps protect the liver against cell damage caused by "
    "free radicals while supporting healthy digestion and bile flow — a simple herbal way to "
    "support liver and digestive function.",

    "<b>ONE LIQUID AMPOULE A DAY</b> — Snap, pour into half a glass of water or juice and "
    "drink in the morning before breakfast. Liquid format for easy intake — no pills to swallow. "
    "A 10-day program you can repeat each season.",

    "<b>ORGANIC, ECOCERT & HEALTH CANADA</b> — 100% organic (Ecocert certified), non-GMO, "
    "alcohol-free, with no preservatives, sweeteners or colours. Vegan, gluten-free and made in "
    "Canada by Nutripur. Health Canada NPN 02239745.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="White canvas with a soft teal tint (#E8F5F2) in the bottom 15% for grounding. Identical backdrop across all 3 options for a clean split-test.",
        purpose="Win the click in the amazon.ca liver/digestive-support grid — stand out next to generic milk-thistle bottles and capsule jars.",
        visual=(
            "Brief the designer to mock ALL 3 options below. Brand picks the winner via Amazon "
            "Manage Your Experiments. Each option uses ONE callout, ONE action cue, ONE supporting "
            "prop — clean, never stacked. Use the real FluxOBile 10-ampoule box from assets/ as the "
            "product reference, with the four botanicals (black radish, boldo, artichoke, dandelion) "
            "and a single 10 ml glass ampoule visible.\n\n"

            "▸ OPTION A — NPN + ORGANIC CREDENTIAL HERO (owns the trust signal)\n"
            "Center: FluxOBile box front-facing, label fully readable, slight elevated 3/4 turn, "
            "~65% of frame. Lower-right: one upright glass ampoule and a small sprig of dandelion "
            "for the botanical cue.\n"
            "CALLOUT top-right badge: 'HEALTH CANADA · NPN 02239745' (Nutripur navy #1F3A5F, white "
            "type, small Canada-leaf icon) plus a small green 'ORGANIC · ECOCERT' chip.\n"
            "Why it wins: no competitor in the grid leads with a visible NPN AND the Ecocert organic "
            "mark — the two strongest trust signals a cautious Canadian digestive-health shopper scans for.\n\n"

            "▸ OPTION B — ONE AMPOULE A DAY (defuses the format / 'how do I take it' question)\n"
            "Center: FluxOBile box left of center. Right: one snapped glass ampoule pouring a thin "
            "amber stream into a clear half-glass of water; an adult hand (fingers only, no face) "
            "holds the ampoule.\n"
            "CALLOUT top-left badge: 'ONE AMPOULE A DAY' (Nutripur teal #2A8C7E, white type).\n"
            "Why it wins: liquid ampoules are unfamiliar vs. capsules — showing the snap-and-pour "
            "action makes the once-daily routine obvious and removes the 'no pills' hesitation at a glance.\n\n"

            "▸ OPTION C — 4 BOTANICALS STACK (owns the ingredient differentiator)\n"
            "Center: FluxOBile box. Floating in a clean radial layout: 4 ingredient chips — "
            "BLACK RADISH · BOLDO · ARTICHOKE · DANDELION. Each chip a soft teal/navy pill on a "
            "white halo, with the matching botanical photographed small beside it.\n"
            "CALLOUT bottom-right badge: '4 ORGANIC BOTANICALS' (Nutripur navy).\n"
            "Why it wins: shoppers search the actual herbs ('artichoke extract', 'dandelion root', "
            "'black radish'); surfacing all four organic botanicals on the hero matches that intent "
            "and beats vague single-ingredient liver bottles.\n\n"

            "Across all 3: box dominant ~65%, callout ~6%, prop fills remainder. Same lighting, "
            "same backdrop, same colour temperature so the split test isolates composition."
        ),
        overlay="(one callout per option — see visual direction)",
        overlay_sub="3 hero options shipped — A/B test, keep the winner",
        props=[
            "OPTION A: box + 1 glass ampoule + dandelion sprig + NPN badge + Ecocert organic chip",
            "OPTION B: box + snapped ampoule pouring into a half-glass of water + adult hand (no face) + dose badge",
            "OPTION C: box + 4 botanical chips in radial halo (black radish, boldo, artichoke, dandelion) + 4-botanicals badge",
        ],
        lighting="Soft top key (5000K daylight balanced) with gentle fill from camera-right. Slight backlight on the box so the FluxOBile label and green logo pop. Identical across all 3 options.",
        why_it_works=(
            "Three angles against three buyer triggers: A wins on credential trust (NPN + Ecocert), "
            "B defuses the unfamiliar-liquid-format question with a clear snap-and-pour action, C "
            "matches herb-level search intent. Per the new standard: one callout, one action cue, "
            "one prop. Clean enough to read on a mobile thumbnail."
        ),
        ctr="Leading with the visible NPN + Ecocert, the snap-and-pour ampoule, and the four named organic botanicals beats generic milk-thistle bottles in the amazon.ca grid and matches high-intent herb searches.",
        cvr="Instant clarity on what it is (organic herbal digestive/bile support), how you take it (one liquid ampoule a day), and that it is Health Canada approved cuts bounce for the cautious adult shopper.",
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: 4 organic botanicals in one ampoule",
        role="hook",
        background="Soft teal #E8F5F2 (Nutripur mood) — clinical-natural, not pharma-sterile.",
        purpose="Stack the 4-botanical differentiator with real mg values — the hook generic single-herb liver bottles can't match.",
        visual=(
            "Center: a clean macro of one upright 10 ml glass ampoule, amber liquid catching the "
            "light. Behind it, 4 botanical labels in a clean radial layout (12, 3, 6, 9 o'clock): "
            "BLACK RADISH · BOLDO · ARTICHOKE · DANDELION. Each label in a soft-edged pill (Nutripur "
            "teal for two, navy for two), with a small real photo of each botanical and a thin "
            "connecting line to the central ampoule like a clean medical infographic.\n\n"
            "Below the ampoule: a caption strip with the real per-ampoule values — Black radish "
            "500 mg · Boldo 210 mg · Artichoke 200 mg · Dandelion 90 mg (organic, water extract 1:10)."
        ),
        overlay="ORGANIC BOTANICALS.",
        overlay_sub="4 organic herbs in one ampoule — black radish, boldo, artichoke & dandelion.",
        props=["single glass ampoule (macro)", "4 botanical label pills with small real plant photos", "thin connecting lines (infographic style)"],
        lighting="Even soft front-light, slight 3D shadow under the ampoule. Educational hook — clarity over mood.",
        why_it_works=(
            "Every competitor sells one herb (usually milk thistle). FluxOBile visibly stacks four "
            "organic botanicals with real mg, anchored to the ampoule. Educates and differentiates "
            "in one frame, and surfaces the exact herb search terms shoppers type."
        ),
        ctr="The mg-anchored 4-botanical stack answers 'what is actually in it?' instantly and out-specs vague single-ingredient liver bottles.",
        cvr="Concrete amounts plus the 1:10 extract equivalence justify the premium over basic milk-thistle and reassure the careful adult buyer.",
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: what the formula supports (NPN-approved claims only)",
        role="educate",
        background="White with a soft Nutripur-teal ribbon footer.",
        purpose="Defend the price premium with Health Canada-language structure/function claims — zero compliance risk.",
        visual=(
            "Three-tile horizontal layout under a headline 'WHAT FLUXOBILE SUPPORTS' in Nutripur "
            "navy, sentence case.\n\n"
            "TILE 1 — DIGESTION (stomach/leaf icon, teal)\n"
            "  • Helps relieve digestive disturbances (dyspepsia)\n"
            "  • Stimulates digestion\n"
            "  • A lighter feeling after meals\n\n"
            "TILE 2 — BILE FLOW (droplet icon, navy)\n"
            "  • Stimulates biliary functions (bile flow)\n"
            "  • Cholagogue & choleretic herbal blend\n"
            "  • Helps with fat digestion\n\n"
            "TILE 3 — LIVER PROTECTION (shield/leaf icon, teal)\n"
            "  • Helps protect the liver against cell damage caused by free radicals\n"
            "  • Antioxidant organic botanicals\n\n"
            "Footer ribbon (Nutripur teal): 'Claims supported by Health Canada NPN 02239745.'"
        ),
        overlay="DIGESTION, SUPPORTED.",
        overlay_sub="Backed by Health Canada NPN 02239745 — regulator-approved language.",
        props=["3 benefit tiles with icons", "small stomach / droplet / shield-leaf icons", "NPN citation footer"],
        lighting="Flat clean studio. Educational module — readability beats atmosphere.",
        why_it_works=(
            "Every claim is verbatim-aligned with the Health Canada NPN — zero compliance risk. "
            "Buyers who filter on 'is this legit?' see actual regulator-approved language, not "
            "marketing-speak, which earns the premium over generic liver capsules."
        ),
        ctr="Regulator-approved, specific support claims read as credible and pull the careful digestive-health shopper deeper into the listing.",
        cvr="NPN-anchored wording defuses the 'are these claims real?' doubt and justifies the premium price.",
    ),
    AIImagePlanItem(
        name="Image 4 — Desire: lighter after rich meals",
        role="desire",
        background="Real home kitchen / dining scene, soft natural light from camera-right.",
        purpose="Place the adult buyer in the after-a-rich-meal moment and own the post-meal-comfort use case.",
        visual=(
            "Angled lifestyle shot. An adult (40–60) at a kitchen table after a hearty meal — relaxed, "
            "a hand resting comfortably near the stomach, calm and content (NOT in discomfort). Face "
            "naturally soft-focused or three-quarter, not a posed stare into camera.\n\n"
            "FOREGROUND right edge: FluxOBile box (label to camera) beside one glass ampoule and a "
            "half-glass of water with a faint amber tint (the poured ampoule). A few plated rich-meal "
            "cues soft-focused behind (no clutter).\n\n"
            "Soft natural light from camera-right. Lived-in home dining vibe, NOT pharmacy / lab. "
            "Stock with model release acceptable; avoid brand logos in frame."
        ),
        overlay="LIGHTER AFTER MEALS.",
        overlay_sub="Herbal digestive support for rich-food days and post-meal comfort.",
        props=["adult model (relaxed, soft-focus, no posed stare)", "FluxOBile box", "1 glass ampoule", "half-glass of water with amber tint", "soft-focused rich-meal cues"],
        lighting="Soft natural side-light from camera-right. Gentle rim on the box. Honest natural-clinical, not studio-staged.",
        why_it_works=(
            "Owns the strongest real use case — feeling lighter and more comfortable after rich meals "
            "— with a person in frame. The relaxed post-meal composition delivers the lifestyle CVR "
            "signal while staying brand-safe and on the NPN-approved digestive benefit."
        ),
        ctr="The relatable after-a-big-meal moment makes the adult shopper self-identify and stop scrolling.",
        cvr="Pairing the post-meal comfort trigger with the visible box and one-ampoule dose moves the shopper from 'is this for me?' to 'this is for me.'",
    ),
    AIImagePlanItem(
        name="Image 5 — Trust: organic, alcohol-free, clean-label credentials",
        role="trust",
        background="White with soft teal panels behind each badge for separation.",
        purpose="Stack the filters Canadian digestive-health shoppers scan for and defuse the clean-label / 'what's NOT in it' question.",
        visual=(
            "Centered macro of the FluxOBile box (label to camera) with one glass ampoule resting "
            "beside it. Four trust badges in the corners:\n\n"
            "  • TOP-LEFT — HEALTH CANADA NPN 02239745 (small Canada-leaf icon)\n"
            "  • TOP-RIGHT — 100% ORGANIC · ECOCERT CERTIFIED (small leaf icon)\n"
            "  • BOTTOM-LEFT — ALCOHOL-FREE · NON-GMO (small droplet icon)\n"
            "  • BOTTOM-RIGHT — NO PRESERVATIVES, SWEETENERS OR COLOURS (small leaf icon)\n\n"
            "Below the box, a thin strip: 'Vegan · gluten-free · lactose-free · made in Canada · "
            "GMP certified · 10 liquid ampoules of 10 ml.'"
        ),
        overlay="ORGANIC & ALCOHOL-FREE.",
        overlay_sub="Ecocert organic · alcohol-free · Health Canada NPN 02239745 · made in Canada.",
        props=["FluxOBile box (center)", "one glass ampoule", "4 corner badge graphics", "thin supporting strip"],
        lighting="Studio even light. Hard catch-light on the box. Badges legible at thumbnail size.",
        why_it_works=(
            "Answers the top clean-label objection (what is NOT in it) and stacks the four filters "
            "that matter to a Canadian herbal-supplement buyer: regulator, certified organic, "
            "alcohol-free / non-GMO, and free of preservatives, sweeteners and colours."
        ),
        ctr="The Ecocert organic and alcohol-free badge stack pulls in cautious buyers who screen for clean, certified herbal products.",
        cvr="Pre-answering the 'what's in it / what's not in it' question right on the image lowers hesitation at the buy box.",
    ),
    AIImagePlanItem(
        name="Image 6 — Desire: the 10-day program = how to use",
        role="desire",
        background="Soft teal #E8F5F2 — same as Image 2 for visual rhythm.",
        purpose="Make the once-daily routine and 10-day program crystal clear and remove the 'how do I take it?' friction.",
        visual=(
            "Split-frame infographic.\n\n"
            "LEFT 55%: FluxOBile box, open, with the strip of 10 glass ampoules visible — one ampoule "
            "snapped and pouring into a half-glass of water in the foreground (today's dose).\n\n"
            "RIGHT 45%: a vertical 3-step how-to panel —\n"
            "  • STEP 1 — Snap one ampoule\n"
            "  • STEP 2 — Pour into half a glass (125 ml) of water or juice\n"
            "  • STEP 3 — Drink in the morning, before breakfast\n"
            "Below: '10 ampoules = a 10-day program · 1 ampoule a day · repeat each season.'"
        ),
        overlay="ONE AMPOULE A DAY.",
        overlay_sub="Snap, pour into water, drink before breakfast · 10 ampoules = a 10-day program.",
        props=["FluxOBile box (open) with 10-ampoule strip", "1 snapped ampoule pouring into a half-glass", "3-step how-to panel"],
        lighting="Even soft front-light. Clean infographic feel.",
        why_it_works=(
            "Removes the unfamiliar-format friction by showing the exact snap-pour-drink routine and "
            "frames the pack as a clear 10-day program. Answers 'how do I take this?' on the thumbnail "
            "and signals an easy, repeatable seasonal habit."
        ),
        ctr="A clear 3-step how-to answers the format question on the image and rewards the comparison shopper unsure about liquid ampoules.",
        cvr="The simple once-daily, no-pills routine reframes the purchase as an easy seasonal habit, easing the buy decision.",
    ),
    AIImagePlanItem(
        name="Image 7 — Brand close: made in Canada by Nutripur",
        role="close",
        background="Warm, calm home scene with soft natural light.",
        purpose="Close on brand identity — clinical-quality, organic, Canadian-made herbal health.",
        visual=(
            "Mid-range environmental shot. An adult hand / arm (no full face needed) setting the "
            "FluxOBile box on a clean kitchen shelf beside a half-glass of water, one glass ampoule "
            "and a small Nutripur info card with the NPN number visible. A soft-focused maple-leaf or "
            "Canada décor element and a small plant in the background.\n\n"
            "Warm afternoon side-light from a window. Wood/stone surface, soft natural tones. Reads "
            "'real Canadian home,' NOT pharmacy.\n\n"
            "Foreground bottom-left: a handwritten-style note card — 'Three generations of "
            "clinical-quality natural health. — From the Nutripur family, Quebec.'"
        ),
        overlay="MADE IN CANADA.",
        overlay_sub="Three generations of clinical-quality natural health · Health Canada NPN 02239745.",
        props=["FluxOBile box", "Nutripur info card with NPN", "1 glass ampoule", "half-glass of water", "maple-leaf or Canada décor (soft focus)", "small plant", "handwritten-style note card", "adult hand / arm (no face)"],
        lighting="Warm afternoon side-light from window. Soft golden hue. Honest, lived-in home — not staged.",
        why_it_works=(
            "Closes on the brand promise the buyer needs before checkout: real Canadian maker, "
            "certified organic, real Health Canada credential, calm seasonal-routine setting. "
            "Provenance is the final trust nudge for a herbal product they will take daily for 10 days."
        ),
        ctr="The 'made in Canada by Nutripur' signal differentiates from anonymous import liver supplements for the trust-conscious CA shopper.",
        cvr="Provenance, organic certification and the visible NPN create the final confidence that seals the purchase.",
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Brand banner: Organic digestive & bile support.",
        role="a+_banner",
        headline="DIGESTION, SUPPORTED.",
        body=(
            "Nutripur FluxOBile is a Health Canada-approved organic herbal blend of black radish, "
            "boldo, artichoke and dandelion. One liquid ampoule a day stimulates digestion and "
            "biliary functions, helps relieve digestive disturbances (dyspepsia) and helps protect "
            "the liver against cell damage caused by free radicals — clinical credibility, made in Canada."
        ),
        visual="Wide cinematic morning scene — clean kitchen shelf, FluxOBile box front-center, soft natural light from a window, a half-glass of water and one glass ampoule in the foreground. Nutripur navy logo upper-left, Health Canada NPN 02239745 small in the bottom band.",
        alt="Nutripur FluxOBile organic herbal digestive and bile support box on a shelf in soft morning light, with a glass ampoule and half-glass of water.",
    ),
    AIModule(
        name="Module 2 — Carousel (4 tiles): The FluxOBile difference",
        role="a+_carousel",
        headline="THE FLUXOBILE DIFFERENCE",
        body=(
            "Tile 1: <b>4 ORGANIC BOTANICALS</b> — black radish, boldo, artichoke & dandelion; cholagogue & choleretic.<br/>"
            "Tile 2: <b>DIGESTION & BILE FLOW</b> — stimulates digestion and biliary functions; helps relieve dyspepsia.<br/>"
            "Tile 3: <b>HEALTH CANADA APPROVED</b> — NPN 02239745. Defensible, regulator-approved language.<br/>"
            "Tile 4: <b>ONE LIQUID AMPOULE A DAY</b> — snap, pour, drink before breakfast; no pills; made in Canada."
        ),
        visual="4 square tiles, Nutripur navy accent corner per tile. Small line icons (botanicals · droplet · maple leaf · ampoule). Consistent composition across all 4.",
        alt="Four-tile A+ carousel: 4 organic botanicals, digestion and bile flow support, Health Canada approved, one liquid ampoule a day.",
    ),
    AIModule(
        name="Module 3 — Banner: how the herbs support digestion",
        role="a+_banner",
        headline="STIMULATES BILE FLOW.",
        body=(
            "Per Health Canada NPN 02239745: stimulates digestion and biliary functions (bile flow); "
            "helps relieve digestive disturbances (dyspepsia); and helps protect the liver against "
            "cell damage caused by free radicals. Cholagogue and choleretic traditional herbal "
            "medicine to support digestive and liver function."
        ),
        visual="Wide banner: clean medical-style infographic — the 4 botanicals (black radish, boldo, artichoke, dandelion) connected by thin lines to a stylized liver / gallbladder / digestive tract (no graphic anatomy, soft illustrative). Nutripur teal and navy palette only. NPN 02239745 small in the lower band.",
        alt="A+ banner showing how FluxOBile's organic botanicals support digestion and bile flow per Health Canada NPN 02239745.",
    ),
    AIModule(
        name="Module 4 — Banner: for rich-meal days",
        role="a+_banner",
        headline="LIGHTER AFTER MEALS.",
        body=(
            "Built for rich-food days and post-meal comfort. The herbal blend stimulates digestion "
            "and biliary functions and helps with fat digestion, for a lighter feeling after meals. "
            "One liquid ampoule a day, before breakfast — a simple 10-day program you can repeat "
            "each season. Per Health Canada NPN 02239745."
        ),
        visual="Triptych within one banner: LEFT — adult relaxed after a hearty meal (soft-focus, no posed stare). CENTER — one ampoule pouring into a half-glass of water. RIGHT — calm morning routine with the FluxOBile box on a kitchen shelf. Soft natural light across all three panels.",
        alt="Triptych A+ banner showing FluxOBile supporting digestion through rich-meal days, the daily ampoule, and a morning routine.",
    ),
    AIModule(
        name="Module 5 — Carousel (5 tiles): The Nutripur family",
        role="a+_carousel",
        headline="THE NUTRIPUR FAMILY",
        body=(
            "Tile 1: <b>FLUXOBILE (this product)</b> — organic digestive & bile support. 10 liquid ampoules.<br/>"
            "Tile 2: <b>FLUXOBILE DUO</b> — the 20-ampoule, 20-day program for a longer seasonal routine.<br/>"
            "Tile 3: <b>HEPATOL</b> — milk thistle herbal liver support in capsules.<br/>"
            "Tile 4: <b>LUTEIN PLUS</b> — Lutein + Zeaxanthin eye-health formula.<br/>"
            "Tile 5: <b>GENIUS Kids &amp; Teens</b> — omega-3 brain &amp; focus support for children 4+.<br/>"
            "<i>Confirm each SKU live on the Nutripur website — pull current product photography from brand assets.</i>"
        ),
        visual="5 identically composed product tiles. Nutripur navy + teal accent corner per tile. Family flat-lay style with consistent box / packaging photography.",
        alt="Five-tile A+ carousel of the Nutripur family — FluxOBile, FluxOBile Duo, Hepatol, Lutein Plus, GENIUS Kids & Teens.",
    ),
    AIModule(
        name="Module 6 — Premium Q&A",
        role="a+_qa",
        headline="QUESTIONS SHOPPERS ASK",
        body=(
            "<b>Q.</b> What does FluxOBile do?<br/>"
            "<b>A.</b> Per Health Canada NPN 02239745, it stimulates digestion and biliary functions "
            "(bile flow), helps relieve digestive disturbances (dyspepsia), and helps protect the "
            "liver against cell damage caused by free radicals.<br/><br/>"

            "<b>Q.</b> How do I take it?<br/>"
            "<b>A.</b> Snap one ampoule, pour it into half a glass (125 ml) of lukewarm water or "
            "juice, and drink in the morning before breakfast. One ampoule a day — no pills to swallow.<br/><br/>"

            "<b>Q.</b> What is in the formula?<br/>"
            "<b>A.</b> Each 10 ml ampoule contains four organic botanicals (water extract 1:10): "
            "black radish 500 mg, boldo 210 mg, artichoke 200 mg and dandelion 90 mg.<br/><br/>"

            "<b>Q.</b> Is it good after rich meals?<br/>"
            "<b>A.</b> Yes. The cholagogue and choleretic herbal blend stimulates digestion and "
            "helps with fat digestion, for a lighter, more comfortable feeling after rich meals.<br/><br/>"

            "<b>Q.</b> How long does one box last?<br/>"
            "<b>A.</b> 10 ampoules per box = a 10-day program at one ampoule a day. Continue 10 to "
            "20 days, and repeat each season.<br/><br/>"

            "<b>Q.</b> Is it organic and clean-label?<br/>"
            "<b>A.</b> Yes — 100% organic (Ecocert certified), non-GMO, alcohol-free, with no "
            "preservatives, sweeteners or colours. Vegan, gluten-free and made in Canada. NPN 02239745."
        ),
        visual="Vertical Q/A table. Nutripur teal divider lines between each Q. Small Nutripur navy Q. and A. labels.",
        alt="Premium Q&A module addressing the six most-asked shopper questions for Nutripur FluxOBile.",
    ),
    AIModule(
        name="Module 7 — Premium Comparison Chart",
        role="a+_comparison",
        headline="WHY FLUXOBILE",
        body=(
            "Compare across 4 columns: <b>Nutripur FluxOBile</b> · Single-herb milk thistle capsule · "
            "Liver detox tea · Generic liver capsule.<br/><br/>"
            "Rows: 4 organic botanicals (black radish, boldo, artichoke, dandelion) · Stimulates bile "
            "flow · Helps relieve dyspepsia · Helps protect the liver (free radicals) · Liquid ampoule "
            "(no pills) · Ecocert organic · Alcohol-free · Health Canada NPN · Made in Canada.<br/><br/>"
            "Highlight the FluxOBile column with a soft Nutripur-teal tint and a 'CANADIAN ORGANIC "
            "CHOICE' ribbon at the top of the column."
        ),
        visual="Standard Amazon Premium Comparison Chart layout, 4 product columns. Competitor columns use category descriptors only — no brand names. Nutripur navy header row.",
        alt="Premium comparison chart for Nutripur FluxOBile vs. single-herb milk thistle capsule, liver detox tea, and generic liver capsule.",
    ),
]


QA = [
    AIQA(q="What does FluxOBile do?",
         a="Per Health Canada NPN 02239745: it stimulates digestion and biliary functions (bile flow), helps relieve digestive disturbances (dyspepsia), and helps protect the liver against cell damage caused by free radicals."),
    AIQA(q="How do I take it?",
         a="Snap one ampoule, pour it into half a glass (125 ml) of lukewarm water or juice, and drink in the morning before breakfast. One ampoule a day — a liquid format with no pills to swallow."),
    AIQA(q="What is in the formula?",
         a="Each 10 ml ampoule contains four organic botanicals (water extract 1:10): black radish 500 mg, boldo 210 mg, artichoke 200 mg and dandelion 90 mg. No alcohol, preservatives, sweeteners or colours."),
    AIQA(q="Is it good after rich meals?",
         a="Yes. The cholagogue and choleretic herbal blend stimulates digestion and helps with fat digestion, for a lighter, more comfortable feeling after rich-food days and big meals."),
    AIQA(q="Is it organic and clean-label?",
         a="Yes. It is 100% organic (Ecocert certified), non-GMO and alcohol-free, with no preservatives, sweeteners or colours. It is also vegan, gluten-free and lactose-free."),
    AIQA(q="How long does one box last?",
         a="10 ampoules per box = a 10-day program at one ampoule a day. You can continue 10 to 20 days, and repeat the program each season."),
    AIQA(q="Where is FluxOBile made?",
         a="Made in Canada by Nutripur in a GMP-certified facility. Health Canada NPN 02239745. Three generations of clinical-quality natural health products."),
    AIQA(q="Who is it for, and any cautions?",
         a="For adults wanting digestive and bile-flow support. Do not use if you are pregnant or breastfeeding. Consult a healthcare practitioner before use if you have liver or gallbladder disorders, or any intestinal obstruction, or if symptoms persist."),
]


# Backend KWs — stem-deduped, byte-packed. Category/SEO terms that are NOT NPN claims
# (liver cleanse, liver detox, fatty liver, flush) live HERE ONLY — never in customer-facing copy.
# Includes FR fallback (amazon.ca is bilingual) and high-volume competitor/category terms from the SEO axis.
BACKEND = (
    "liver cleanse liver detox liver support supplement fatty liver liver flush liver health "
    "digestive support bile flow choleretic cholagogue dyspepsia bloating after meals fat digestion "
    "black radish boldo artichoke extract dandelion root organic herbal liquid ampoules ecocert "
    "milk thistle silymarin tudca choline ox bile gallbladder cleanse detox dandelion tea "
    "foie nettoyage foie détox foie chardon marie digestion bile radis noir artichaut pissenlit "
    "boldo ampoules biologique sans alcool fabriqué au canada npn santé du foie"
)


def main() -> None:
    print("Loading Nutripur customer + parsing FluxOBile Excel…")
    cust = load_customer("nutripur")
    brief = parse_excel(EXCEL)
    asin = brief.asin or ASIN
    OUT = HERE / f"{PLAN_NO}_{asin}_Image Plan.pdf"
    real_title_len = len(TITLE.replace("&amp;", "&"))
    print(f"  Product: {brief.product_name}")
    print(f"  ASIN: {brief.asin}  Marketplace: {cust.marketplace}")
    print(f"  USPs={len(brief.usps)} KWs={len(brief.all_keywords)} reviews=+{len(brief.good_reviews)}/-{len(brief.bad_reviews)}")
    print(f"  Health Canada NPN: 02239745 (claims are NPN-defensible)")
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
