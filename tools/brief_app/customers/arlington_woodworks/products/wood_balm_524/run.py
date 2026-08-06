"""Arlington Woodworks — Artisan Furniture Wood Balm No. 524 — Image Plan 01
Hand-written senior copy injected into the branded ReportLab pipeline.

Marketplace: amazon.com (US). Customer text: English. Art direction: English.

LANGUAGE / FIELD SPLIT (the standard):
  • CUSTOMER-FACING (shopper reads — auto-scanned for compliance):
    TITLE, BULLETS, image overlay + overlay_sub, module headline + body, QA.
  • ART-DIRECTION (designer reads — not customer copy):
    image purpose, background, visual, props, lighting, why_it_works, ctr, cvr,
    module visual, module alt.

OVERLAY RULE: sell the OUTCOME, not the action. Every on-image overlay leads with
the result / transformation / defused fear the buyer wants — never the steps.
Each overlay is distinct and tied to that image's job. Hard limits (auto-linted):
  overlay ≤ 30 chars AND ≤ 5 words · overlay_sub ≤ 90 chars
  module headline ≤ 38 chars · bullet head <b>…</b> ≤ 45 chars · TITLE ≤ 200 chars

ELEVATED COPY — 4 levers pulled:
  1. VoC as the dream outcome: 'like new' wood revival + easy buff, straight from reviews.
  2. Dream-outcome-first hero + bullet 1 (the revived, richer grain before the how).
  3. Warm artisan power-words: rich, deep grain, soft luster, nourished, revived — no hype.
  4. Keywords woven naturally: beeswax wood conditioner, furniture wax for wood,
     beeswax wood polish, wood conditioner for furniture, cutting board wax.

HONESTY (objections defused on-creative):
  • sticky/oily residue → 'a thin coat, a little goes a long way, buff well'.
  • soft NATURAL luster, NOT high gloss.
  • it CONDITIONS / REVIVES / PROTECTS — it is not a stain remover or damage repair.

Verified product facts (from listing.xlsx + brand_study.md):
  - Certified-organic 3-ingredient formula: flaxseed oil + beeswax + orange oil.
  - No petroleum, synthetic waxes or harsh chemicals.
  - Food-safe after proper application, absorption & buffing (cutting boards,
    butcher blocks, utensils, kitchen wood).
  - Restores warmth, depth, natural grain & soft luster to dry/dull/faded wood;
    hydrates + leaves a protective finish.
  - Wipe-on, absorb, buff-off — no sanding, no tools, no fumes, no prep.
  - Versatile: furniture, dining tables, cabinets, antiques, cutting boards,
    butcher blocks, kitchen tools, trays, décor.
  - Concentrated 8 oz paste; one jar cares for ~8-12 pieces.
  - Handmade small-batch in Connecticut, USA; veteran-owned; 10% of proceeds to
    cancer-related charities. 'No. 524' = heritage/apothecary craft feel.

COMPLIANCE NOTES: no $/price, no URL/.com, no superlatives (best/#1/ultimate),
no 'treat/prevent/cure' health verbs in customer copy, 'food-safe' stated as the
brand does (after proper application & buffing). 'organic' is a non-blocking WARNING.
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
PLAN_NO = "01"
ASIN = "B0F6GDG4T3"


# ===== KW-led, artisan customer-facing copy (English) =====

# Title HTML-escaped; literal "&" counts as 1 char. Keep ≤200 real chars.
TITLE = (
    "Arlington Woodworks Wood Balm No. 524 — Beeswax Wood Conditioner & Furniture Wax "
    "for Wood · Flaxseed Oil, Beeswax & Orange Oil · Revives Dry Wood to Rich Grain "
    "& Soft Luster · Food-Safe · 8 oz"
)

BULLETS = [
    "<b>DRY WOOD, REVIVED LIKE NEW</b> — Bring back the rich color, deep grain and soft "
    "natural luster of tired, dull wood. This beeswax wood conditioner nourishes furniture, "
    "dining tables and antiques so they look cared-for again, not coated or plasticky.",

    "<b>3 INGREDIENTS YOU CAN PRONOUNCE</b> — Just flaxseed oil, beeswax &amp; orange oil. "
    "No petroleum, no synthetic waxes, no harsh chemicals or fumes — a natural furniture wax "
    "for wood you'll feel good using around your home and family.",

    "<b>FOOD-SAFE FOR THE KITCHEN</b> — After it's applied, absorbed and buffed, No. 524 is "
    "food-safe — a cutting board wax and conditioner for butcher blocks, wooden utensils, "
    "spoons, bowls and trays. Family-safe wood care that belongs in the kitchen.",

    "<b>WIPE ON, BUFF OFF — NO SANDING</b> — Wipe on a thin coat, let it soak in, then buff "
    "off. A little goes a long way, so buff well and you're left with a soft luster and zero "
    "sticky residue. No sanding, no tools, no prep. It conditions and protects — a beeswax "
    "wood polish, not a stain remover.",

    "<b>HANDMADE IN CT · VETERAN-OWNED</b> — Small-batch wood care from Connecticut, made by "
    "hand the old apothecary way. One 8 oz jar cares for around 8 to 12 pieces, and 10% of "
    "proceeds support cancer-related charities. Wood conditioner for furniture, done right.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="Pure white #FFFFFF studio sweep — Amazon main-image policy: no overlay text, no graphics, ≥85% product fill. Same white across all 3 options for a clean split test.",
        purpose="Win the click in the beeswax-wood-care grid — read as a warm, natural, handmade balm, not a chemical spray polish.",
        visual=(
            "Designer mocks up ALL 3 options; brand picks the winner via Amazon Manage Your "
            "Experiments. Amazon MAIN image = pure white, product-only, NO overlay text / NO badges "
            "baked in (policy). The differences below are composition + prop only.\n\n"
            "▸ OPTION A — HERO JAR + INGREDIENT CUE (owns 'natural / 3 ingredients')\n"
            "The 8 oz No. 524 jar centered, lid off and resting against the base, label legible, slight "
            "3/4 turn, ~80% of frame. A small honest ingredient cue at the jar's foot: a few flax seeds, "
            "a raw beeswax chunk and a single orange half — real, not styled to excess. Amber balm "
            "visible in the open jar.\n\n"
            "▸ OPTION B — JAR + WOOD REVIVAL PROP (owns the result)\n"
            "Jar left-of-center, label legible. Beside it a small warm-walnut wood offcut showing rich "
            "revived grain and a soft (not glossy) sheen, a folded cotton buffing cloth resting on it. "
            "Jar + cloth + wood only, all on pure white.\n\n"
            "▸ OPTION C — JAR + APOTHECARY CRAFT CUE (owns 'handmade / heritage')\n"
            "Jar centered, ~80% of frame, kraft/parchment label and 'No. 524' fully readable, a small "
            "twine-tied tag hanging off the lid. Nothing else — clean apothecary presentation.\n\n"
            "All 3: pure white, jar dominant ~80%, label + amber balm readable, warm true-to-life wood/"
            "amber tones (NO oversaturation, NO high-gloss)."
        ),
        overlay="",
        overlay_sub="",
        props=[
            "OPTION A: 8 oz No. 524 jar (open) + flax seeds + raw beeswax chunk + orange half",
            "OPTION B: jar + revived walnut wood offcut (soft luster) + folded cotton buffing cloth",
            "OPTION C: jar with kraft 'No. 524' label + twine-tied tag on the lid",
        ],
        lighting="Soft window-style key from camera-left, gentle fill right (3200-3500K warm). Slight rim on the jar so the label and amber balm pop. Same light across all 3 options.",
        why_it_works=(
            "Three triggers against three buyer motives on pure-white (policy-safe): A wins on the "
            "'natural, 3 ingredients' promise, B proves the revived-grain result, C sells the handmade "
            "apothecary feel. Warm amber balm + true wood tones stand out beside cold chemical spray "
            "bottles in the grid."
        ),
        ctr="On the white amazon.com grid, a warm amber balm jar with visible natural ingredients (or a revived-grain wood offcut) reads instantly as artisan wood care and beats generic aerosol furniture-polish cans; the 'No. 524' apothecary label signals craft before the click.",
        cvr="Seeing the real 3 ingredients, the open amber balm and the soft-luster wood removes the 'is this another chemical polish?' doubt and sets an honest expectation of natural, cared-for wood — not plastic shine.",
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: Before/After wood revival",
        role="hook",
        background="Cream #F5ECDD backdrop with aged wood in the lower band, soft warm side-light — the mood shot.",
        purpose="Sell the dream outcome first: dry, dull, faded wood becomes rich, deep-grained and softly lustrous.",
        visual=(
            "One real piece — a walnut dining tabletop OR an antique cabinet door — split cleanly "
            "down the middle.\n"
            "LEFT (before): dry, dull, grey-faded, thirsty grain.\n"
            "RIGHT (after): the same wood nourished — warm, rich color, deep visible grain, a SOFT "
            "natural luster (NOT wet-look / high-gloss). A cotton cloth mid-buff at the dividing line, "
            "the open No. 524 jar in the foreground corner. Small caption strip at the bottom: "
            "'conditioned & revived — a soft natural luster, not high gloss.'"
        ),
        overlay="DRY WOOD, REVIVED",
        overlay_sub="Dull, tired wood comes back rich, deep-grained and softly lustrous.",
        props=["real walnut tabletop or antique door (split before/after)", "open No. 524 jar (foreground)", "cotton buffing cloth mid-buff", "caption strip"],
        lighting="Warm afternoon side-light from camera-right; rim on the revived half so the soft luster reads without looking glossy.",
        why_it_works=(
            "Leans on the strongest real-review verbatim — the 'like new' wood revival. The before/after "
            "is the single most persuasive proof in wood care, and the honest 'soft luster, not high gloss' "
            "caption pre-sets the right expectation so the finish never disappoints."
        ),
        ctr="The dry→rich transformation is universally wanted by anyone with a faded table, cabinet or antique; the split-frame is the strongest scroll-stopper in the wood-care grid.",
        cvr="Visible proof of the result instead of a promise — and the 'soft luster not gloss' line defuses the top shine-expectation complaint before it becomes a return.",
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: 3 natural ingredients vs chemical polish",
        role="educate",
        background="White with a walnut #4A3728 footer band; clean apothecary layout.",
        purpose="Make the natural formula concrete and defend it against petroleum/silicone spray polishes.",
        visual=(
            "Headline top. Three honest ingredient tiles with simple line icons + a real photo inset each:\n"
            "  • FLAXSEED OIL — nourishes deep into the grain\n"
            "  • BEESWAX — seals in a soft protective luster\n"
            "  • ORANGE OIL — light natural scent + gentle lift\n"
            "The 8 oz jar centered or right. A small honest contrast chip to the side: 'No petroleum · "
            "no synthetic waxes · no harsh chemicals' set against a faded generic 'spray polish' silhouette "
            "(no brand). Walnut footer band carries the supporting line."
        ),
        overlay="3 YOU CAN PRONOUNCE",
        overlay_sub="Flaxseed oil, beeswax, orange oil — no petroleum, no synthetic wax.",
        props=["3 ingredient tiles with icons + photo insets", "8 oz No. 524 jar", "flax seeds / beeswax chunk / orange half", "generic spray-polish silhouette (no brand)", "walnut footer band"],
        lighting="Flat, clean, warm studio light — legibility over drama; true amber and wood tones.",
        why_it_works=(
            "Buyers who filter on ingredients see three real, pronounceable actives instead of a chemical "
            "list — the exact 'natural / non-toxic' signal this category searches for, and the honest "
            "contrast justifies the artisan positioning without naming a competitor."
        ),
        ctr="'Ingredients you can pronounce' is a strong natural-wood-care search signal; the 3-tile layout communicates the whole formula at a glance.",
        cvr="Transparency builds trust and separates No. 524 from cheap petroleum/silicone sprays, earning the artisan price.",
    ),
    AIImagePlanItem(
        name="Image 4 — Desire: Food-safe for the kitchen",
        role="desire",
        background="Real warm kitchen scene: butcher block on a counter, soft window light, cream tones.",
        purpose="Own the food-safe kitchen use — cutting boards, butcher blocks, utensils — for family-safe homes.",
        visual=(
            "A rich, freshly conditioned butcher block or maple cutting board on a real kitchen counter, "
            "grain glowing warm. A hand (hands only, no face) buffing the last of the balm with a cloth; "
            "a wooden spoon, bowl and the open No. 524 jar alongside. Small honest note card: 'food-safe "
            "after it's applied, absorbed and buffed.' Warm, homey, NOT clinical."
        ),
        overlay="SAFE FOR THE KITCHEN",
        overlay_sub="Food-safe after buffing — cutting boards, butcher blocks, utensils.",
        props=["butcher block / maple cutting board (conditioned)", "hands buffing with cloth (no face)", "wooden spoon + bowl", "open No. 524 jar", "food-safe note card"],
        lighting="Soft warm window light from camera-left; honest kitchen ambiance, gentle rim on the conditioned board.",
        why_it_works=(
            "Food-safe is the category's biggest kitchen unlock and a top search intent (cutting board wax/"
            "oil). Showing it in a real kitchen with the honest 'after buffing' qualifier is both persuasive "
            "and compliant, and 'family-safe' widens the buyer set beyond furniture."
        ),
        ctr="Cutting-board and butcher-block buyers are a large, distinct search pool; the warm kitchen scene captures that intent the furniture shots miss.",
        cvr="The 'food-safe after buffing' note sets the honest condition up front, converting cautious kitchen buyers without over-claiming.",
    ),
    AIImagePlanItem(
        name="Image 5 — Trust: How it works + residue objection defused",
        role="trust",
        background="White with cream #F5ECDD step panels; clean instructional layout.",
        purpose="Show the 3-step ease AND defuse the #1 objection (sticky/oily residue) right on the image.",
        visual=(
            "3-step icon row, generous and legible:\n"
            "  1. WIPE ON — a thin coat with a cloth (a-little-goes-a-long-way cue)\n"
            "  2. LET IT ABSORB — soaks into the grain (clock / droplet icon)\n"
            "  3. BUFF OFF — buff to a soft luster, no residue (cloth / shine icon)\n"
            "Beside it an honest badge: 'A LITTLE GOES A LONG WAY — BUFF WELL, NO STICKY RESIDUE'. "
            "Small line: 'no sanding · no tools · no fumes'. Jar anchored on the right."
        ),
        overlay="BUFF TO A SOFT LUSTER",
        overlay_sub="A thin coat, buffed well — soft luster, no sticky residue, no sanding.",
        props=["3 step icons (wipe / absorb / buff)", "badge 'a little goes a long way'", "'no sanding / no tools / no fumes' line", "8 oz jar"],
        lighting="Clean even warm studio light — icons and the badge readable on a mobile thumbnail.",
        why_it_works=(
            "Proactively answers the one recurring negative — sticky/oily residue from over-application — "
            "with the exact fix (thin coat, buff well). Pre-defused objections lower returns and 1-stars, "
            "and the beginner-friendly 3 steps echo the 'easy to apply and buff' praise."
        ),
        ctr="The simple wipe/absorb/buff clarity attracts first-time wood-care buyers who fear a fussy, messy job.",
        cvr="Defuses the top residue objection on-creative and confirms the 'easy, no-sanding' promise reviewers reward — the strongest single objection-clearing frame in the plan.",
    ),
    AIImagePlanItem(
        name="Image 6 — Desire: Versatility grid (one jar, many pieces)",
        role="desire",
        background="Cream #F5ECDD, warm side-light, consistent across all tiles.",
        purpose="Show one jar covers the whole home — furniture, antiques, boards, cabinets, trays, décor.",
        visual=(
            "Clean 6-up grid of real warm-wood scenes, each with a small conditioned/buffed cue:\n"
            "  • DINING TABLE  • ANTIQUE DRESSER  • CUTTING BOARD\n"
            "  • CABINETS       • WOODEN TRAY      • CARVED DÉCOR\n"
            "Jar anchored center or bottom. Small caption: 'one 8 oz jar cares for around 8-12 pieces.' "
            "Consistent warm tones, true-to-life, no high-gloss."
        ),
        overlay="ONE JAR, WHOLE HOME",
        overlay_sub="Furniture, antiques, boards, cabinets, trays, décor — 8 oz cares for 8-12 pieces.",
        props=["6 use-case tiles (table/dresser/board/cabinets/tray/décor)", "8 oz No. 524 jar", "buffing-cloth cues", "caption strip"],
        lighting="Warm side-light, identical across all 6 tiles for a clean grid.",
        why_it_works=(
            "Expands perceived value — one jar covers many pieces — and hits the broad keyword spread "
            "(furniture wax, wood conditioner for furniture, cutting board wax, cabinets, antiques). "
            "The 8-12 pieces math makes the cost-per-use case."
        ),
        ctr="Speaks to several search intents at once (furniture, antiques, boards, cabinets), maximizing grid relevance.",
        cvr="More proven uses per jar = higher perceived value and an easier purchase to justify.",
    ),
    AIImagePlanItem(
        name="Image 7 — Close: The maker story (veteran-owned, CT, gives back)",
        role="close",
        background="Warm workshop scene: aged workbench, brass, linen, low golden side-light — apothecary mood.",
        purpose="Close on brand identity — handmade, veteran-owned, made in Connecticut, gives back.",
        visual=(
            "Mid-range workshop scene: a maker's hands (no face) hand-buffing balm into a beautiful piece "
            "of wood on an aged bench. On the bench: the No. 524 jar (label legible), a cotton cloth, a "
            "small batch of jars curing, a handwritten card. Soft-focused workshop (brass, linen, tools). "
            "Small trust strip: 'handmade small-batch in Connecticut · veteran-owned · 10% of proceeds "
            "support cancer-related charities.'"
        ),
        overlay="HANDMADE IN CONNECTICUT",
        overlay_sub="Small-batch, veteran-owned wood care — 10% of proceeds give back.",
        props=["maker's hands on wood (no face)", "No. 524 jar", "cotton cloth", "small batch of curing jars", "handwritten card", "aged workbench / brass / linen"],
        lighting="Low warm golden side-light from camera-right, lived-in workshop glow — not staged.",
        why_it_works=(
            "Closes on the brand promise that matters before checkout: an honest, handmade, veteran-owned "
            "maker who gives back. The hands-on-wood gesture is the visual metaphor for care, and the "
            "give-back line adds a values reason to choose No. 524 over an anonymous polish."
        ),
        ctr="The 'handmade in Connecticut, veteran-owned' signal differentiates from anonymous imported polishes and draws values-driven, quality-conscious buyers.",
        cvr="Provenance, craft and the give-back mission create the final trust that seals the purchase.",
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Brand banner: the maker's promise",
        role="a+_banner",
        headline="ARTISAN WOOD CARE, BY HAND.",
        body=(
            "Arlington Woodworks Wood Balm No. 524 is a handmade, small-batch beeswax wood conditioner "
            "made the old apothecary way in Connecticut. Three natural ingredients — flaxseed oil, beeswax "
            "and orange oil — revive dry, dull wood to a rich, deep grain and a soft, natural luster. "
            "Veteran-owned, and 10% of proceeds support cancer-related charities."
        ),
        visual="Wide cinematic workshop banner: aged workbench, warm golden side-light, the No. 524 jar front-center (label legible, amber balm visible), a beautifully conditioned wood surface and a folded cotton cloth soft-focused alongside. Logo upper-left in walnut #4A3728. Small heritage line in the lower band.",
        alt="Arlington Woodworks Wood Balm No. 524 jar on a warm workshop bench beside a richly conditioned wood surface, in golden apothecary light.",
    ),
    AIModule(
        name="Module 2 — Carousel (4 tiles): 3 ingredients vs chemical polish",
        role="a+_carousel",
        headline="3 INGREDIENTS YOU CAN SAY",
        body=(
            "Tile 1: <b>FLAXSEED OIL</b> — nourishes deep into thirsty, dry grain.<br/>"
            "Tile 2: <b>BEESWAX</b> — seals in a soft, protective natural luster.<br/>"
            "Tile 3: <b>ORANGE OIL</b> — a light natural scent and gentle lift.<br/>"
            "Tile 4: <b>NOTHING ELSE</b> — no petroleum, no synthetic waxes, no harsh chemicals or fumes, "
            "the way conventional spray polishes can carry."
        ),
        visual="4 square tiles, walnut #4A3728 accent corner each. Real macro photography: flax seeds, a raw beeswax chunk, a cut orange, then the No. 524 jar for tile 4. Beeswax-amber #C08A2E small icons. Same composition discipline across all 4.",
        alt="Four-tile A+ carousel of Wood Balm No. 524's three natural ingredients — flaxseed oil, beeswax, orange oil — versus conventional chemical polish.",
    ),
    AIModule(
        name="Module 3 — Banner: before/after wood revival",
        role="a+_banner",
        headline="DRY, DULL WOOD — REVIVED.",
        body=(
            "Tired, faded wood loses its warmth and grain. No. 524 nourishes the wood, draws the color "
            "and grain back to life, and leaves a soft, natural luster — not a plastic, high-gloss shine. "
            "It conditions, revives and protects the wood you already love; it is not a stain remover or "
            "a damage repair. Real wood, honestly renewed."
        ),
        visual="Wide before/after banner: one real walnut tabletop or antique cabinet door split down the middle — LEFT dry, grey-faded, thirsty grain; RIGHT the same wood revived, warm, deep-grained, soft-lustrous. A cotton cloth mid-buff and the open No. 524 jar at the seam. Warm afternoon light; true wood tones, no gloss.",
        alt="A+ before/after banner showing dry, faded wood on the left revived to rich, deep grain and soft luster on the right after Wood Balm No. 524.",
    ),
    AIModule(
        name="Module 4 — Banner: food-safe for the kitchen",
        role="a+_banner",
        headline="FOOD-SAFE FOR THE KITCHEN.",
        body=(
            "Once No. 524 is applied, absorbed and buffed, it is food-safe — a natural conditioner and "
            "cutting board wax for butcher blocks, wooden utensils, spoons, bowls and serving trays. "
            "Made from ingredients you can pronounce, it is family-safe wood care that belongs on the "
            "kitchen counter as much as in the dining room."
        ),
        visual="Wide warm-kitchen banner: a richly conditioned butcher block and maple cutting board on a real counter, hands (no face) buffing with a cloth, a wooden spoon and bowl and the open No. 524 jar alongside. Soft window light, cream tones, homey — not clinical. Small 'food-safe after buffing' note.",
        alt="A+ banner showing Wood Balm No. 524 conditioning a butcher block and cutting board in a warm kitchen, food-safe after buffing.",
    ),
    AIModule(
        name="Module 5 — Banner: how it works (wipe · absorb · buff)",
        role="a+_banner",
        headline="WIPE. ABSORB. BUFF. NO SANDING.",
        body=(
            "Wipe on a thin coat with a soft cloth, let it soak into the grain, then buff off to a soft "
            "luster. A little goes a long way, so buff well and you're left with warmth and depth — never "
            "a sticky, oily residue. No sanding, no tools, no fumes, no complicated prep. Beginner-friendly "
            "wood care that just works."
        ),
        visual="Wide 3-step banner: LEFT wipe on a thin coat (cloth, a-little-goes-a-long-way cue) · CENTER let it absorb into the grain (soft glow) · RIGHT buff to a soft luster (cloth, no residue). Warm light throughout, walnut #4A3728 step numbers, beeswax-amber #C08A2E accents. Small 'no sanding · no tools · no fumes' line.",
        alt="A+ three-step banner showing how to use Wood Balm No. 524 — wipe on a thin coat, let it absorb, buff off to a soft luster, no sanding.",
    ),
    AIModule(
        name="Module 6 — Premium Q&A",
        role="a+_qa",
        headline="COMMON QUESTIONS",
        body=(
            "<b>Q.</b> Will it leave a sticky or oily residue?<br/>"
            "<b>A.</b> Not when used correctly. A little goes a long way — wipe on a thin coat, let it "
            "absorb, then buff well. Buffing off the excess leaves a clean, soft luster with no sticky "
            "film.<br/><br/>"
            "<b>Q.</b> Is it really food-safe?<br/>"
            "<b>A.</b> Yes — after No. 524 is applied, absorbed and buffed, it is food-safe for cutting "
            "boards, butcher blocks, wooden utensils and serving pieces.<br/><br/>"
            "<b>Q.</b> Will it give a high-gloss shine?<br/>"
            "<b>A.</b> No. No. 524 brings back a soft, natural luster that lets the grain show — not a "
            "plastic, wet-look gloss. If you want warmth and depth rather than a mirror finish, this is it."
            "<br/><br/>"
            "<b>Q.</b> What wood does it work on?<br/>"
            "<b>A.</b> Bare, raw, oiled or dry/dull wood responds especially well — furniture, dining "
            "tables, cabinets, antiques, cutting boards, trays and décor. On sealed or painted surfaces, "
            "test a hidden area first.<br/><br/>"
            "<b>Q.</b> Is it a cleaner or a repair product?<br/>"
            "<b>A.</b> No. It conditions, revives and protects wood — it is not a stain remover, deep "
            "cleaner or damage-repair product. Wipe off surface dust before you apply.<br/><br/>"
            "<b>Q.</b> How far does one jar go?<br/>"
            "<b>A.</b> The 8 oz jar is concentrated — a little goes a long way, so one jar cares for around "
            "8 to 12 pieces depending on their size and dryness."
        ),
        visual="Vertical Q/A table, walnut #4A3728 divider lines between questions, small beeswax-amber Q. and A. labels. Cream #F5ECDD panel background.",
        alt="Premium Q&A module answering the most common buyer questions about Wood Balm No. 524 — residue, food-safe, luster, surfaces, use and coverage.",
    ),
    AIModule(
        name="Module 7 — Premium Comparison Chart",
        role="a+_comparison",
        headline="WHY NO. 524",
        body=(
            "Compare across 3 columns: <b>Arlington Wood Balm No. 524</b> · Synthetic spray polish · "
            "Plain oil.<br/><br/>"
            "Rows: Natural ingredients you can pronounce (flaxseed · beeswax · orange) · No petroleum or "
            "synthetic waxes · Food-safe after buffing · Revives grain + soft natural luster · Conditions "
            "&amp; protects (no sticky residue when buffed) · Wipe-on / buff-off, no sanding · Handmade "
            "small-batch, veteran-owned.<br/><br/>"
            "Highlight the Arlington column with a soft cream #F5ECDD tint and a small 'HANDMADE IN CT' "
            "ribbon at the top."
        ),
        visual="Standard Amazon Premium Comparison Chart, 3 product columns. Alternatives named by category only — no brand names. Walnut #4A3728 header row, beeswax-amber #C08A2E check marks, cream highlight on the Arlington column.",
        alt="Premium comparison chart: Arlington Wood Balm No. 524 vs a synthetic spray polish and plain oil across ingredients, food-safety, finish and application.",
    ),
]


QA = [
    AIQA(q="Will it leave a sticky or oily residue?",
         a="Not when used correctly. A little goes a long way — wipe on a thin coat, let it absorb, then buff well. Buffing off the excess leaves a clean, soft luster with no sticky film. The most common cause of residue is simply using too much."),
    AIQA(q="Is it really food-safe?",
         a="Yes. After No. 524 is applied, absorbed and buffed, it is food-safe. It's made from flaxseed oil, beeswax and orange oil, which makes it well suited to cutting boards, butcher blocks, wooden utensils, spoons, bowls and serving trays."),
    AIQA(q="Will it give a high-gloss shine?",
         a="No. No. 524 brings back a soft, natural luster that lets the wood grain show — not a plastic, wet-look gloss. If you want warmth, depth and richer grain rather than a mirror finish, this is what it does."),
    AIQA(q="What kind of wood does it work on?",
         a="Bare, raw, oiled or dry/dull wood responds especially well — furniture, dining tables, cabinets, antiques, cutting boards, butcher blocks, trays and décor. On sealed, painted or heavily used surfaces, test a small hidden area first, as absorption can vary."),
    AIQA(q="Is it a cleaner or a repair product?",
         a="No. It conditions, revives and protects wood — it is not a stain remover, deep cleaner or damage-repair product. Wipe off loose surface dust before applying so the balm can soak evenly into the grain."),
    AIQA(q="How do I use it?",
         a="Wipe a thin coat onto clean, dry wood with a soft cloth, let it soak in for a few minutes, then buff off with a clean cloth to a soft luster. No sanding, no tools and no fumes. For very dry wood, apply a second thin coat."),
    AIQA(q="How far does one jar go?",
         a="The 8 oz jar is concentrated, so a little goes a long way. One jar cares for around 8 to 12 pieces, depending on their size, how dry the wood is and how much you apply."),
    AIQA(q="Who makes it?",
         a="Arlington Woodworks — a veteran-owned maker crafting wood care by hand in small batches in Connecticut, the old apothecary way. 10% of proceeds support cancer-related charities."),
]


# Backend KWs — English, stem-deduped, byte-packed. Avoid brand/title duplicates & superlatives.
BACKEND = (
    "wood care beeswax furniture restoration wax paste polish sealer finish conditioner "
    "butcher block board oil cutting kitchen utensil spoon bowl tray antique dining table "
    "cabinet dresser dresser hardwood walnut oak maple teak revive nourish natural flaxseed "
    "orange non toxic chemical free handmade small batch veteran connecticut apothecary balm"
)


def main() -> None:
    print("Loading Arlington Woodworks customer + parsing Wood Balm No. 524 Excel…")
    cust = load_customer("arlington_woodworks")
    brief = parse_excel(EXCEL)
    OUT = HERE / f"{PLAN_NO}_{ASIN}_Image Plan.pdf"
    real_title_len = len(TITLE.replace("&amp;", "&"))
    print(f"  Product: {brief.product_name}")
    print(f"  ASIN: {brief.asin}  Marketplace: {cust.marketplace}")
    print(f"  USPs={len(brief.usps)} KWs={len(brief.all_keywords)} reviews=+{len(brief.good_reviews)}/-{len(brief.bad_reviews)}")
    print(f"  TITLE real chars (de-escaped): {real_title_len}")

    builder = BriefBuilder(cust, brief, OUT, ai=None)
    builder._ai_title = TITLE
    builder._ai_bullets = BULLETS
    builder._ai_images = IMAGES
    builder._ai_modules = MODULES
    builder._ai_qa = QA
    builder._ai_backend = BACKEND
    builder.copy_source_label = "Hand-written senior copy (KW-led, artisan)"

    print("Building branded PDF…")
    pdf_path = builder.build()
    size_kb = pdf_path.stat().st_size // 1024
    import re
    pages = len(re.findall(rb'/Type\s*/Page[^s]', pdf_path.read_bytes()))
    print(f"Built: {pdf_path}")
    print(f"  Pages: {pages}  Size: {size_kb} KB")


if __name__ == "__main__":
    main()
