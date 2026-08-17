"""Freshly Preserved — WHOLE-BLOOM FAMILY (parent B0H8TR2WSB) · 6 child variations.

One SEO workbook, SIX SEO tabs = six child listings under one parent. This script builds
ONE image + A+ Premium plan PDF PER VARIATION (house rule: 2+ SEO tabs -> build them all).

  a  Small Pansy            0.1 oz · 12 whole blooms
  b  Small Orchid           0.1 oz · 12 whole blooms
  c  Small Pansy & Orchids  0.1 oz · 12 whole blooms   <- the parent's default child
  d  Pansy                  0.2 oz · 25 whole blooms
  e  Pansy & Orchids        0.2 oz · 25 whole blooms
  f  Purple Orchids         0.2 oz · 25 whole blooms

Marketplace: amazon.com (USA) — English overlays + customer copy.
TITLE + BULLETS come 1:1 from each variation's SEO tab (the keyword axis).
Overlays / A+ / Q&A are hand-written per variation.

PARENT-CHILD IS BUILT IN, on purpose, in three places:
  • Image 6  — honest size + THIS variation's count/weight vs its siblings.
  • Image 7  — "Find your flower": the family strip, this child ringed (close + cross-sell).
  • A+ Mod 5 — the family carousel, so the shopper lands on the right child instead of bouncing.

Compliance guardrails (US): no best / #1 / guaranteed · no health-cure claims · no prices
or URLs on-image. Keep color HONEST (reviewers: "not as bright as pictures"). ALWAYS show a
size reference — "smaller than expected" is the #1 complaint on this family.

CHILD ASINs: not in the workbook (Excel truncates tab names at 31 chars), so they were read
off the live Amazon listing's twister data for parent B0H8TR2WSB and mapped by (count, flower).
Two independent cross-checks confirm the mapping: the truncated tab 'SEO_Small Pansy
Freeze_B0GLR6GB' is B0GLR6GBWB (variant a), and the hidden hyperlink in Overview!D8 was
B0GLR1JC19, which Amazon reports as '12 Pieces / Mixed Pansy + Orchid' (variant c, the parent's
default child).
"""
from __future__ import annotations
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent          # self-contained product folder
ROOT = HERE.parents[5]                           # project root (Claude_Code/)
sys.path.insert(0, str(ROOT))

from tools.brief_app.core.customers import load_customer
from tools.brief_app.core.excel_parser import parse_excel
from tools.brief_app.core.pdf_builder import BriefBuilder
from tools.brief_app.core.ai import AIImagePlanItem, AIModule, AIQA
from tools.brief_app.core.seo_loader import load_seo, as_bullets_html


EXCEL = HERE / "listing.xlsx"
PLAN_NO = "02"
PARENT_ASIN = "B0H8TR2WSB"


# ===== The variation family (parent B0H8TR2WSB + the wider Freshly Preserved flower line) =====
# Used verbatim in Image 7 and A+ Module 5 so the shopper can self-select the right child.
FAMILY = [
    "Small Pansy · 12 blooms",
    "Small Orchid · 12 blooms",
    "Small Pansy & Orchids · 12 blooms",
    "Pansy · 25 blooms",
    "Pansy & Orchids · 25 blooms",
    "Purple Orchids · 25 blooms",
    "Marigolds",
    "Small Mini Carnations & Bachelors",
    "Small Roses & Mixed Flowers",
    "Squash Blossoms",
]


VARIANTS = [
    dict(
        code="a", sheet="SEO_Small Pansy Freeze_B0GLR6GB", asin="B0GLR6GBWB",
        slug="Small-Pansy-12", label="Small Pansy · 12 whole blooms · 0.1 oz",
        flower="pansy", count="12", weight="0.1 oz",
        color="Vivid multicolor pansies — purple, yellow, blue and near-black faces, each with the "
              "pansy's signature dark centre marking.",
        shape="Flat, open, face-up blooms — they sit perfectly still on buttercream and read clearly "
              "from directly above, which is how cakes get photographed.",
        signature="cupcake towers, cookie tops and baby-shower dessert tables",
        hero_overlay="12 REAL PANSY BLOOMS",
        hero_sub="Whole freeze-dried pansies. Bright, flat-faced, ready to place.",
        hook_overlay="REAL PANSIES. NOT PLASTIC.",
        size_overlay="SMALL BLOOMS, BIG DETAIL",
        size_sub="12 small pansies, scaled for cupcakes, cookies and drink garnishes.",
        family_note="Need more coverage? The 25-bloom Pansy pack is the same flower, double the count.",
    ),
    dict(
        code="b", sheet="SEO_Mini Freeze-Dried Edible Or", asin="B0GLR3H7JM",
        slug="Small-Orchid-12", label="Small Orchid · 12 whole blooms · 0.1 oz",
        flower="orchid", count="12", weight="0.1 oz",
        color="Soft purple-and-white orchids with delicate throat markings — refined rather than loud.",
        shape="Sculptural, winged blooms with real dimension — they catch the light on a glass rim "
              "and photograph beautifully at an angle.",
        signature="craft cocktails, champagne coupes and wedding cake tiers",
        hero_overlay="12 REAL ORCHID BLOOMS",
        hero_sub="Whole freeze-dried orchids. The refined finish for drinks and cake.",
        hook_overlay="REAL ORCHIDS. NOT PLASTIC.",
        size_overlay="SMALL BLOOM, BIG PRESENCE",
        size_sub="12 small orchids. Refined detail without overwhelming the design.",
        family_note="Want a bolder purple statement? The 25-bloom Purple Orchid pack goes bigger.",
    ),
    dict(
        code="c", sheet="SEO_Freeze-Dried Edible Flowers", asin="B0GLR1JC19",
        slug="Small-Pansy-Orchid-12", label="Small Pansy & Orchids · 12 whole blooms · 0.1 oz",
        flower="pansy and orchid",
        count="12", weight="0.1 oz",
        color="Two flowers, one palette: multicolor pansies (purple, yellow, blue) beside soft "
              "purple-and-white orchids.",
        shape="Flat pansy faces for the top-down shot, sculptural orchids for height and angle — "
              "the mix is what makes an arrangement look designed rather than sprinkled.",
        signature="cakes and cocktails styled for the same event",
        hero_overlay="TWO FLOWERS. ONE SET.",
        hero_sub="12 whole blooms: pansies and orchids, ready to style together.",
        hook_overlay="REAL BLOOMS. NOT PLASTIC.",
        size_overlay="SMALL BLOOMS, BIG DETAIL",
        size_sub="12 whole blooms in the mix, sized for cupcakes, cookies and drinks.",
        family_note="Styling a whole event? The 25-bloom Pansy & Orchids pack covers more surface.",
    ),
    dict(
        code="d", sheet="SEO_Freeze-Dried Edible Pansies", asin="B0CNDYZLTH",
        slug="Pansy-25", label="Pansy · 25 whole blooms · 0.2 oz",
        flower="pansy", count="25", weight="0.2 oz",
        color="Vivid multicolor pansies — purple, yellow, blue and near-black faces, each with the "
              "pansy's signature dark centre marking.",
        shape="Flat, open, face-up blooms — enough of them to run a full floral cascade down the "
              "side of a tiered cake without rationing.",
        signature="tiered celebration cakes, dessert tables and 24-cupcake batches",
        hero_overlay="25 REAL PANSY BLOOMS",
        hero_sub="Enough whole pansies to style a full dessert table, not just one cake.",
        hook_overlay="REAL PANSIES. NOT PLASTIC.",
        size_overlay="25 BLOOMS. NO RATIONING.",
        size_sub="Small blooms, generous count. Style a whole table, not one slice.",
        family_note="Only decorating one cake? The 12-bloom Small Pansy pack is the smaller set.",
    ),
    dict(
        code="e", sheet="SEO_Pansy and Orchids Freeze_B0", asin="B0CN8M429Y",
        slug="Pansy-Orchid-25", label="Pansy & Orchids · 25 whole blooms · 0.2 oz",
        flower="pansy and orchid",
        count="25", weight="0.2 oz",
        color="Two flowers, one palette: multicolor pansies (purple, yellow, blue) beside soft "
              "purple-and-white orchids.",
        shape="Flat pansy faces plus sculptural orchids, in event quantity — the combination that "
              "lets one order cover the cake, the cupcakes AND the bar.",
        signature="weddings and events where the cake, the drinks and the board all match",
        hero_overlay="25 BLOOMS, TWO FLOWERS",
        hero_sub="Pansies and orchids together. Enough for cake, drinks and board.",
        hook_overlay="REAL BLOOMS. NOT PLASTIC.",
        size_overlay="ONE ORDER. WHOLE EVENT.",
        size_sub="25 whole blooms across two flowers. Cake, cupcakes and cocktails covered.",
        family_note="Just one dessert to finish? The 12-bloom Small Pansy & Orchids set is smaller.",
    ),
    dict(
        code="f", sheet="SEO_Freeze-Dried Edible Orchids", asin="B0CMP9D8MC",
        slug="Purple-Orchids-25", label="Purple Orchids · 25 whole blooms · 0.2 oz",
        flower="orchid", count="25", weight="0.2 oz",
        color="Rich, saturated purple orchids — the deepest colour in the family and the reason "
              "this variation gets picked for weddings.",
        shape="Sculptural, winged blooms with real dimension, in the count an event actually needs "
              "— a cascade down a wedding cake plus a garnish on every glass.",
        signature="wedding cakes, drink stations and catered menus",
        hero_overlay="25 PURPLE ORCHIDS",
        hero_sub="Deep purple whole blooms. The wedding-cake and cocktail-bar finish.",
        hook_overlay="REAL ORCHIDS. NOT PLASTIC.",
        size_overlay="PURPLE THAT CARRIES",
        size_sub="25 whole orchids. Rich natural purple, honest to the real bloom.",
        family_note="Testing the look first? The 12-bloom Small Orchid pack is the starter size.",
    ),
]


# ===================== per-variation image plan (7 images) =====================

def build_images(v: dict) -> list[AIImagePlanItem]:
    flower = v["flower"]
    count, weight = v["count"], v["weight"]
    Flower = flower.capitalize()
    return [
        AIImagePlanItem(
            name="Image 1 — Main Hero (3 options for A/B testing)",
            role="hero",
            background="Clean bright white with a whisper of soft lilac #F5F0F7 across the bottom 15% "
                       "for grounding. IDENTICAL background across all 3 options so the split test "
                       "isolates composition, not colour.",
            purpose=(f"Win the click against a grid of look-alike dried-flower listings. The SEO team's "
                     f"CTR note is blunt: the current main image is not attractive. Ship all 3, keep the "
                     f"winner via Amazon Manage Your Experiments."),
            visual=(
                "Mock ALL 3 options — the brand A/B tests and keeps the winner. Each: ONE callout, ONE "
                "supporting prop, product dominant. Colour stays TRUE to the real bloom (reviewers "
                "complain 'not as bright as pictures' — do NOT over-saturate). Amazon's slot-1 main must "
                "stay pure-white / product-only; these callout versions are the CTR mains you test "
                f"against a clean white main.\n\n"

                f"THIS VARIATION: {v['label']}. {v['color']}\n\n"

                "OPTION A — THE REAL-BLOOM COUNT (owns 'real, and this much')\n"
                f"The {count} whole {flower} blooms laid out on bright white in a loose, natural arc, "
                "one bloom pulled forward in crisp macro so petal veining reads as unmistakably REAL. "
                "Open resealable pack tipped in behind. Lower-right: one cupcake wearing a single bloom, "
                "for scale and payoff.\n"
                f"ONE CALLOUT (top-left badge, green bg / white text): '{count} WHOLE BLOOMS'.\n"
                "Why it wins: answers the two questions every shopper in this category has — are they "
                "real, and how many do I actually get — before they open the listing.\n\n"

                "OPTION B — THE PAYOFF (owns the outcome)\n"
                f"The finished result: {v['signature']}, styled with these blooms, shot slightly above on "
                "bright white. The pack sits softly out of focus behind it.\n"
                "ONE CALLOUT (top-right badge, purple bg / white text): 'CAKES. COCKTAILS. BOARDS.'\n"
                "Why it wins: nobody wants a bag of petals — they want the showpiece. Selling the "
                "finished dessert beats selling the ingredient.\n\n"

                "OPTION C — NEVER WILTS (defuses the fresh-flower pain)\n"
                f"Clean split: LEFT a fresh {flower} visibly wilting and browning at the edges; RIGHT the "
                "Freshly Preserved bloom holding perfect colour and shape. Thin divider between.\n"
                "ONE CALLOUT (top-right badge, green bg / white text): 'NEVER WILTS'.\n"
                "Why it wins: names the #1 frustration with fresh edible flowers and positions "
                "shelf-stable as the fix, in one glance.\n\n"

                "Across all 3: product dominant, callout ~6% of frame, same lighting and colour temp."
            ),
            overlay=v["hero_overlay"],
            overlay_sub=v["hero_sub"],
            props=[
                f"OPTION A: {count} whole {flower} blooms + tipped resealable pack + 1 cupcake for scale",
                f"OPTION B: finished {v['signature'].split(',')[0]} + pack soft-focus behind",
                f"OPTION C: wilting fresh {flower} (left) vs intact preserved bloom (right)",
            ],
            lighting="Bright high-key daylight, soft shadows, airy. Identical across all 3 for a clean split test.",
            why_it_works=(
                "Three different triggers: A owns 'real, and here's the count', B sells the finished "
                "showpiece, C defuses the wilting pain. One idea, one prop, one badge each — legible at "
                "mobile thumbnail size, with honest colour."
            ),
            ctr=(f"Callout + visible bloom count beat the category's bare product-on-white mains; the "
                 f"{count}-bloom badge pre-answers the quantity question that stops the click."),
            cvr="Option B doubles as the desire cue — the shopper arrives already picturing the result.",
        ),
        AIImagePlanItem(
            name=f"Image 2 — Hook: real {flower} blooms, not artificial decoration",
            role="hook",
            background="Soft lilac #F5F0F7 — fresh and elegant, never dark or moody",
            purpose="Land the #1 differentiator in one frame: these are genuine, food-grade blooms.",
            visual=(
                f"Extreme macro of a single whole {flower} bloom filling most of the frame, lit so the "
                f"natural veining, petal edges and the tiny imperfections read clearly — unmistakably "
                f"REAL, not moulded plastic. {v['shape']}\n\n"
                "A small 'FOOD-GRADE · EDIBLE' leaf check-mark badge sits beside it. Keep the colour "
                "honest and natural — no candy over-saturation, because that is exactly the complaint "
                "the reviews already make."
            ),
            overlay=v["hook_overlay"],
            overlay_sub=f"Genuine food-grade {flower} blooms, freeze-dried whole. Never artificial.",
            props=[f"macro {flower} bloom", "food-grade / edible check-mark badge"],
            lighting="Soft directional daylight to reveal petal texture and veining. Clarity over drama.",
            why_it_works=(
                "In a thumbnail grid, real and fake look identical. A true-colour macro showing petal "
                "veining proves authenticity instantly and answers the quiet worry: 'are these actually "
                "real, edible flowers?'"
            ),
            ctr="Macro texture stops the scroll in a category of flat, samey product shots.",
            cvr="Removes the 'is this plastic decoration?' hesitation that kills the add-to-cart.",
        ),
        AIImagePlanItem(
            name="Image 3 — Educate: what's inside & every way to use it",
            role="educate",
            background="White with a soft green ribbon footer",
            purpose="Show exactly what arrives and the range of uses, so the buyer pictures their own project.",
            visual=(
                f"Left third: the open pack with the {count} whole {flower} blooms neatly grouped, small "
                f"label '{count} whole blooms · {weight}'. Right two-thirds: a clean 4-tile 'WAYS TO USE' "
                "grid, each tile a small real photo —\n"
                "  • CAKES & CUPCAKES (bloom set into buttercream)\n"
                "  • COCKTAILS & MOCKTAILS (bloom on a glass rim / frozen into a clear ice cube)\n"
                "  • CHARCUTERIE & GRAZING BOARDS (blooms scattered among cheese and fruit)\n"
                "  • PLATING & DIY / RESIN (bloom on a plated dessert / set in clear resin)\n"
                "Thin green connectors tie the pack to the four uses."
            ),
            overlay="ONE PACK. EVERY OCCASION.",
            overlay_sub="Cakes · cupcakes · cocktails · charcuterie · plating · resin and DIY crafts.",
            props=[f"open pack of {count} {flower} blooms", "4 use-case tiles", "green connector lines"],
            lighting="Bright, even, editorial daylight. Educational clarity beats mood.",
            why_it_works=(
                "The SEO team's CVR note asks for images with clear contents, usage and function. Four "
                "concrete uses let bakers, mixologists and hosts all see themselves in the frame and "
                "justify the purchase beyond a single occasion."
            ),
            ctr="Grid layouts read as informative at thumbnail size and pull the browse-stage click.",
            cvr="Directly answers 'what do I actually get, and what would I do with it?'",
        ),
        AIImagePlanItem(
            name="Image 4 — Desire: the showpiece moment",
            role="desire",
            background="Styled bright celebration table, soft natural window light",
            purpose="Sell the dream outcome — an elegant, professionally-styled centrepiece.",
            visual=(
                f"Hero lifestyle shot built around {v['signature']}: the finished piece crowned with these "
                f"{flower} blooms, on a styled bright table — soft linen, two stemmed cocktails also "
                "garnished, the edge of a grazing board in frame. Light, fresh and aspirational, like a "
                "food stylist's table. The pack sits naturally to the side. Freshly Preserved logo small, "
                "lower corner. This is the 'action image' the CVR notes ask for — hands mid-placement are "
                "welcome."
            ),
            overlay="STEAL THE SHOW.",
            overlay_sub="Cakes, cocktails and boards that look professionally styled.",
            props=[f"finished {v['signature'].split(',')[0]}", "2 garnished cocktails",
                   "grazing board edge", "styled linen table", "pack to the side"],
            lighting="Soft natural window light, bright and airy. Aspirational editorial styling — never dark.",
            why_it_works=(
                "Sells the outcome, not the petals: the buyer is imagining the reaction at their event. "
                "The strongest CVR image in the set — it shows exactly the result they are paying for."
            ),
            ctr="Beautiful finished food out-performs ingredient shots in the mobile carousel.",
            cvr="Transfers the result onto the buyer's own occasion — the emotional close.",
        ),
        AIImagePlanItem(
            name="Image 5 — Trust: real, shelf-stable, natural, made in USA",
            role="trust",
            background="White with soft green panels behind each badge for separation",
            purpose="Stack the reassurances that defuse 'are they real food, will they last, will they arrive intact?'",
            visual=(
                "Centre: the resealable pack, clean and premium, a few intact blooms beside it. Four "
                "badges in the corners:\n\n"
                "  • TOP-LEFT — REAL EDIBLE FLOWERS (leaf icon — food-grade, not artificial)\n"
                "  • TOP-RIGHT — SHELF-STABLE (calendar icon — ready for months, no wilting)\n"
                "  • BOTTOM-LEFT — 100% NATURAL (no preservatives, no added sugar)\n"
                "  • BOTTOM-RIGHT — USA GROWN & FREEZE-DRIED (small US outline)\n\n"
                "Thin strip below, aimed straight at the 'arrived smashed' reviews: 'Protective resealable "
                "pack — blooms travel cushioned and stay protected between uses.'"
            ),
            overlay="SHELF-STABLE. STAYS PERFECT.",
            overlay_sub="Real · 100% natural · no preservatives · USA grown · resealable pack.",
            props=["resealable pack", "intact blooms", "4 corner badges", "protective-packaging strip"],
            lighting="Bright studio-even light with a soft catch-light on the pack. Badges legible at thumbnail size.",
            why_it_works=(
                "The category's trust gaps are 'real and safe to eat?' and 'will they survive shipping?'. "
                "Stacking real + shelf-stable + natural + USA-grown, with the protective pack called out, "
                "answers every doubt before it becomes a question."
            ),
            ctr="Badge clusters read as credentials even when the text is too small to parse.",
            cvr="Neutralises the top two 1-star themes (fragile, arrived damaged) pre-emptively.",
        ),
        AIImagePlanItem(
            name=f"Image 6 — Honest size & count ({count} blooms · {weight})",
            role="desire",
            background="Soft lilac #F5F0F7 — same family as Image 2 for visual rhythm",
            purpose="Set honest size and quantity expectations — the #1 and #2 review complaints on this family.",
            visual=(
                "Split-frame.\n\n"
                f"LEFT — SCALE, HONESTLY: a single {flower} bloom held on a fingertip, and the same bloom "
                "beside a US quarter and resting on one cupcake. Caption: 'Small blooms — scaled for "
                f"cupcakes, cookies and drinks.'\n\n"
                f"RIGHT — WHAT {count} LOOKS LIKE: all {count} blooms laid out in a neat grid, photographed "
                f"flat, with the pack beside them and the label '{count} whole blooms · {weight}'. Do not "
                "art-direct this into looking like more than it is — an honest count picture is what stops "
                "the 'smaller than expected' return.\n\n"
                "Footer strip — HANDLING: tweezers gently placing a bloom onto buttercream, with the note "
                "'Delicate by nature — place with tweezers or clean fingers, store sealed. Petals that "
                "separate are perfect for scattering.'"
            ),
            overlay=v["size_overlay"],
            overlay_sub=v["size_sub"],
            props=[f"{flower} bloom on a fingertip", "bloom beside a US quarter", "one cupcake for scale",
                   f"flat-lay grid of all {count} blooms", "tweezers placing a bloom"],
            lighting="Bright, even, honest daylight — show the true size and the true colour.",
            why_it_works=(
                "Answers the two loudest 1-star themes head-on: 'smaller than expected' and 'fragile'. "
                "Honest expectations lift satisfaction and cut returns, while the framing turns the small "
                "size into the right scale for detailed work."
            ),
            ctr="Coin-and-fingertip scale shots are unusual in this category and earn a curiosity click.",
            cvr="Removes the expectation gap that drives this family's returns and 3-star reviews.",
        ),
        AIImagePlanItem(
            name="Image 7 — Close: find your flower (the variation family)",
            role="close",
            background="Bright white with a soft lilac band behind the family strip",
            purpose=("Close on the brand AND route the shopper to the right child listing — this parent has "
                     "six whole-bloom variations plus the wider flower range."),
            visual=(
                "Top two-thirds: brand-forward shot — the Freshly Preserved pack front and centre with a "
                f"graceful scatter of {flower} blooms around it on bright white, one finished cupcake or "
                "cocktail softly in frame. Lower band: logo + tagline 'Real blooms. Ready when you are.'\n\n"
                "Bottom third — THE FAMILY STRIP (this is the variation navigator). A single clean row of "
                "small identical-composition bloom photos, each captioned with its variation name and "
                f"count:\n  {' · '.join(FAMILY[:6])}\n"
                f"THIS listing — {v['label']} — is ringed in brand green with a small 'YOU ARE HERE' tag; "
                "the others stay un-ringed at 70% scale.\n"
                f"Caption under the strip: '{v['family_note']}'\n"
                f"Small line at the very bottom: 'Also in the Freshly Preserved range: "
                f"{' · '.join(FAMILY[6:])}.'"
            ),
            overlay="FIND YOUR FLOWER.",
            overlay_sub="One family, many blooms. Pick the flower and the count your project needs.",
            props=["Freshly Preserved pack", f"scatter of {flower} blooms", "finished cupcake or cocktail",
                   "family strip of 6 variations with this one ringed", "logo + tagline band"],
            lighting="Bright, airy, elegant daylight. Family strip evenly lit so the variations compare fairly.",
            why_it_works=(
                "A parent-child family loses sales when the shopper lands on the wrong child and bounces. "
                "Showing the whole family with this child ringed converts a mismatch into a sideways sale "
                "and closes on brand identity rather than a feature."
            ),
            ctr="'Find your flower' reads as a range, which signals a real brand rather than a one-off seller.",
            cvr="Recovers the shopper who wanted a different flower or a bigger count — inside the family.",
        ),
    ]


# ===================== per-variation A+ Premium plan (7 modules, Q&A finale) =====================

def build_modules(v: dict) -> list[AIModule]:
    flower = v["flower"]
    count, weight = v["count"], v["weight"]
    fam_tiles = FAMILY[:5]
    return [
        AIModule(
            name="Module 1 — Premium Full Image: brand banner",
            role="a+_banner",
            headline="REAL BLOOMS. READY WHEN YOU ARE.",
            body=(
                f"Freshly Preserved freeze-dried edible flowers are real, food-grade blooms that keep "
                f"their true colour and natural shape — so you can create showpiece cakes, cocktails and "
                f"boards without the wilting, browning and waste of fresh flowers. This variation: "
                f"<b>{v['label']}</b>. Grown and freeze-dried in the USA, 100% natural, ready the moment "
                f"inspiration strikes."
            ),
            visual=("Wide, bright editorial banner — a styled celebration table with a floral cake, a "
                    "garnished cocktail and the resealable pack, soft natural window light. Freshly "
                    "Preserved logo upper-left, tagline in the lower band. Desktop 1464x600, mobile "
                    "600x450 — keep the cake and the pack inside the mobile safe area."),
            alt=f"Freshly Preserved freeze-dried edible {flower} blooms styled on a bright celebration table.",
        ),
        AIModule(
            name="Module 2 — Premium Carousel (5 tiles): why Freshly Preserved",
            role="a+_carousel",
            headline="WHY FRESHLY PRESERVED",
            body=(
                "Tile 1: <b>REAL, NOT ARTIFICIAL</b> — Genuine food-grade blooms, never plastic decor.<br/>"
                "Tile 2: <b>NEVER WILTS</b> — Shelf-stable; stock it weeks or months ahead.<br/>"
                "Tile 3: <b>TRUE COLOUR &amp; SHAPE</b> — Freeze-dried whole, so the bloom stays a bloom.<br/>"
                "Tile 4: <b>ENDLESSLY VERSATILE</b> — Cakes, cocktails, charcuterie, plating, resin art.<br/>"
                "Tile 5: <b>USA GROWN · 100% NATURAL</b> — No preservatives, no added sugar, no dyes."
            ),
            visual=("5 square tiles at 220x220, purple accent corner on each, consistent bright styling. "
                    "Small icons: bloom · calendar · colour swatch · cupcake+glass · US leaf. Alt text per tile."),
            alt="Five-tile A+ carousel: real not artificial, never wilts, true colour, versatile, USA grown and natural.",
        ),
        AIModule(
            name="Module 3 — Premium Full Image: ways to use them",
            role="a+_banner",
            headline="ONE PACK. EVERY OCCASION.",
            body=(
                "Crown wedding cakes, cupcakes and dessert boards. Garnish cocktails and mocktails, or "
                "freeze a whole bloom into a clear ice cube. Scatter across charcuterie and grazing "
                "boards. Finish plated desserts like a pastry chef — and go beyond food into resin art "
                f"and DIY crafts. {v['shape']}"
            ),
            visual=("Wide 4-panel banner: CAKE (bloom set in buttercream) → COCKTAIL (bloom on a rim / in "
                    "clear ice) → CHARCUTERIE (blooms among cheese and fruit) → PLATING / RESIN. Bright, "
                    "editorial, thin purple dividers. Mobile version keeps 2 panels stacked."),
            alt=f"A+ banner showing four ways to use Freshly Preserved edible {flower} blooms.",
        ),
        AIModule(
            name="Module 4 — Premium Full Image: fresh flowers wilt, these don't",
            role="a+_banner",
            headline="FRESH FLOWERS WILT. THESE DON'T.",
            body=(
                "Fresh edible flowers are seasonal, fragile and spoil within days — they brown, curl and "
                "lose their shape right when you need them. Freshly Preserved blooms are freeze-dried "
                "whole and shelf-stable, so they hold their colour and form until your event. Stock the "
                "pack ahead, skip the last-minute florist run, and waste nothing."
            ),
            visual=(f"Wide banner split in two: LEFT — a fresh {flower} visibly wilting and browning, "
                    "muted. RIGHT — a Freshly Preserved bloom, bright and intact, beside the resealable "
                    "pack. Clean centre divider, bright background. Never a dark or moody treatment."),
            alt=f"A+ banner comparing a wilting fresh {flower} with a shelf-stable Freshly Preserved bloom.",
        ),
        AIModule(
            name="Module 5 — Premium Carousel (5 tiles): choose your variation",
            role="a+_carousel",
            headline="FIND YOUR FLOWER",
            body=(
                f"<b>You are viewing: {v['label']}.</b> Every variation in this family is the same real, "
                f"freeze-dried, food-grade bloom — pick the flower and the count your project needs.<br/><br/>"
                f"Tile 1: <b>{fam_tiles[0]}</b> — Flat, bright faces for cupcakes and cookies.<br/>"
                f"Tile 2: <b>{fam_tiles[1]}</b> — Sculptural blooms for drinks and cake tiers.<br/>"
                f"Tile 3: <b>{fam_tiles[2]}</b> — Both flowers, for cake and bar in one order.<br/>"
                f"Tile 4: <b>{fam_tiles[3]}</b> — Double the count for tables and tiered cakes.<br/>"
                f"Tile 5: <b>{fam_tiles[4]}</b> — Event quantity across two flowers.<br/><br/>"
                f"Also in the Freshly Preserved range: {' · '.join(FAMILY[5:])}. "
                f"{v['family_note']}"
            ),
            visual=("5 identical-composition variation tiles at 220x220 — same white background, same "
                    "lighting, same camera height, so the flowers and counts compare honestly. THIS "
                    f"variation ({v['label']}) carries a green ring and a small 'YOU ARE HERE' tag. "
                    "Per-tile alt text names the variation and its count."),
            alt="Five-tile A+ carousel of the Freshly Preserved whole-bloom variations with the current one marked.",
        ),
        AIModule(
            name="Module 6 — Premium Full Image: from the brand (benefits closer)",
            role="a+_banner",
            headline="FROM FRESHLY PRESERVED",
            body=(
                "We grow and freeze-dry our flowers in the USA, whole, so the bloom that leaves us is the "
                "bloom that lands on your cake — same shape, same natural colour, months later. No "
                "preservatives, no added sugar, no dyes, and nothing artificial pretending to be a "
                f"flower. This pack holds <b>{count} whole {flower} blooms ({weight})</b> in a resealable "
                "pack that keeps them protected between projects. Small kitchens, big possibilities."
            ),
            visual=("Warm benefits/brand closer: soft-focus USA growing field or the freeze-drying trays "
                    "on the left, the resealable pack and a finished dessert on the right, brand-voice "
                    "line across the middle. Bright and airy — never dark behind the logo."),
            alt="Freshly Preserved brand closing banner: USA grown, freeze-dried whole, nothing artificial.",
        ),
        AIModule(
            name="Module 7 — Premium Q&A (finale)",
            role="a+_qa",
            headline="QUESTIONS BEFORE YOU BUY",
            body=(
                "<b>Q.</b> Are these real flowers, and are they edible?<br/>"
                f"<b>A.</b> Yes. They are genuine, food-grade {flower} blooms that have been freeze-dried "
                "whole — real edible flowers, not artificial decoration.<br/><br/>"

                f"<b>Q.</b> How many blooms do I get, and how big are they?<br/>"
                f"<b>A.</b> This variation is {v['label']} — {count} whole blooms, {weight}. They are "
                "small by design, scaled for cupcakes, cookies and drink garnishes where a full-size "
                "bloom would overwhelm the piece. See the size image for a real-scale reference.<br/><br/>"

                "<b>Q.</b> How long do they last, and how should I store them?<br/>"
                "<b>A.</b> They are shelf-stable and will not wilt like fresh flowers. Keep them in the "
                "resealable pack, away from moisture and direct sunlight, and use them whenever you need "
                "a perfect bloom.<br/><br/>"

                "<b>Q.</b> Are they fragile? Will they arrive intact?<br/>"
                "<b>A.</b> Freeze-dried flowers are naturally light and delicate, so they travel "
                "cushioned in a protective resealable pack. Handle gently and place with tweezers or "
                "clean fingers. Any petals that separate are still perfect for scattering.<br/><br/>"

                "<b>Q.</b> Will the colour match the photos?<br/>"
                "<b>A.</b> We keep our images honest to the real bloom. Freeze-drying preserves the "
                "natural colour and shape, though shades vary slightly from flower to flower — these are "
                "real botanicals, not printed decorations.<br/><br/>"

                "<b>Q.</b> Do they have a strong taste or smell?<br/>"
                "<b>A.</b> They are mild. These blooms are used mainly for beautiful, natural "
                "presentation on cakes, drinks and boards rather than for strong flavour.<br/><br/>"

                "<b>Q.</b> Which variation should I choose?<br/>"
                f"<b>A.</b> Same real bloom in every one — choose by flower and by count. "
                f"{v['family_note']} See the family carousel above for the full range."
            ),
            visual=("Vertical Q/A table, text only. Purple divider lines between questions, small green "
                    "Q. and purple A. labels. Mobile-first line lengths."),
            alt="Premium Q&A module answering the most-asked questions about Freshly Preserved edible flowers.",
        ),
    ]


def build_qa(v: dict) -> list[AIQA]:
    """House standard: exactly 5 pairs, question ≤80 chars, answer ≤120.

    Cut from ten. Because this runs for every child variation, the count and the
    which-variation answer stay — they are the two that differ per child and are exactly
    what a shopper on a variation listing is trying to resolve."""
    flower, count, weight = v["flower"], v["count"], v["weight"]
    return [
        AIQA(q="Are these real flowers, and are they edible?",
             a=f"Yes. Food-grade {flower} blooms, freeze-dried whole. Not artificial "
               f"decoration."),
        AIQA(q="How many blooms do I get?",
             a=f"This variation is {count} whole blooms at {weight}. The size image shows all "
               f"{count} laid out flat."),
        AIQA(q="How big are the blooms? They look small.",
             a="Small by design. Scaled for cupcakes, cookies and drink garnishes."),
        AIQA(q="Are they fragile? Mine need to arrive intact.",
             a="They ship cushioned in a resealable pack. Petals that separate are still "
               "perfect for scattering."),
        AIQA(q="Which variation should I choose?",
             a="Every variation is the same real, freeze-dried bloom. Choose by flower and by "
               "count."),
    ]


def main() -> None:
    print("Loading Freshly Preserved customer + parsing listing…")
    cust = load_customer("freshly_preserved")
    brief = parse_excel(EXCEL)
    print(f"  Parent: {brief.product_name}  ASIN {PARENT_ASIN}  Marketplace: {cust.marketplace}")
    print(f"  USPs={len(brief.usps)} KWs={len(brief.all_keywords)} Q&A={len(brief.rufus_qa)} "
          f"reviews=+{len(brief.good_reviews)}/-{len(brief.bad_reviews)}")
    print(f"  Building {len(VARIANTS)} child variations…\n")

    for v in VARIANTS:
        seo = load_seo(EXCEL, v["sheet"])
        out = HERE / f"{PLAN_NO}{v['code']}_{v['asin']}_{v['slug']}_Image Plan.pdf"
        print(f"— {v['label']}")
        print(f"    sheet: {v['sheet']}")

        builder = BriefBuilder(cust, brief, out, ai=None)
        builder._ai_title = seo.title
        builder._ai_bullets = as_bullets_html(seo)
        builder._ai_images = build_images(v)
        builder._ai_modules = build_modules(v)
        builder._ai_qa = build_qa(v)
        builder._ai_backend = seo.backend
        builder.copy_source_label = (
            f"SEO sheet '{v['sheet']}' (title/bullets/backend) + hand-written senior creative "
            f"(overlays, A+, Q&A) — US/English"
        )
        pdf_path = builder.build()
        import re
        pages = len(re.findall(rb'/Type\s*/Page[^s]', pdf_path.read_bytes()))
        print(f"    → {pdf_path.name}  ({pages} pages, {pdf_path.stat().st_size // 1024} KB)\n")

    print(f"Done — {len(VARIANTS)} variation plans in {HERE}")


if __name__ == "__main__":
    main()
