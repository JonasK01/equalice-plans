"""Freshly Preserved — Product 03 · Freeze-Dried Small ROSES & MIXED 0.1 oz (about 12 rose blooms).

ASIN: B0H8ZDCP71 · Marketplace: amazon.com (USA) — English overlays + customer copy.
(The Overview tab also carries an older ASIN, B0GLR76YW1 — the SEO deliverable is filed under
B0H8ZDCP71, so that is the ASIN used here.)

WHAT MAKES THIS ONE DIFFERENT: it is the only variation that ships BOTH formats in one pack —
about 12 whole small rose blooms PLUS a mix of colourful loose petals. Roses are the romance
flower: weddings, anniversaries, engagement cakes, Valentine's. The creative leans into the
occasion, and the "blooms + petals in one pack" fact is the hook nothing else in the family has.

TITLE + BULLETS come 1:1 from the SEO tab (the keyword axis). Overlays / A+ / Q&A are
hand-written. Parent-child is built in at Image 7 and A+ Module 5.

Compliance guardrails (US): no best / #1 / guaranteed · no health-cure claims · no prices or
URLs on-image. Colour stays HONEST — reviewers already say "not as bright as pictures".
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
PLAN_NO = "03"
ASIN = "B0H8ZDCP71"

FAMILY = [
    "Small Roses & Mixed · about 12 rose blooms (this listing)",
    "Small Pansy · 12 whole blooms",
    "Small Orchid · 12 whole blooms",
    "Pansy & Orchids · 25 whole blooms",
    "Flower Petals · about 1.5 cups",
    "Squash Blossoms · 12 whole blooms",
    "Purple Orchids · 25 whole blooms",
    "Marigolds",
    "Small Mini Carnations & Bachelors",
    "Fall Cake Decorating Kit · 25+ flowers & leaves",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="Clean bright white with a whisper of soft lilac #F5F0F7 across the bottom 15%. "
                   "IDENTICAL across all 3 options so the split test isolates composition, not colour.",
        purpose="Win the click in a grid of look-alike dried-rose listings. The SEO team's CTR note is "
                "blunt: the current main image is not attractive. Ship all 3 and keep the winner.",
        visual=(
            "Mock ALL 3 options. Each: ONE callout, ONE supporting prop, product dominant. Colour stays "
            "TRUE to the real bloom — roses freeze-dry to a soft natural rose-pink, not a neon red, and "
            "over-saturating is exactly the complaint the reviews already make. Amazon's slot-1 main "
            "stays pure-white / product-only; these callout versions are the CTR mains you test.\n\n"

            "OPTION A — BLOOMS PLUS PETALS (owns what no sibling has)\n"
            "Clean overhead split on white: on the left, the 12 whole rose blooms arranged in a neat "
            "arc; on the right, a soft drift of the mixed petals. A hairline divider and two small "
            "labels: '12 whole roses' / 'mixed petals'. Open pack tipped in behind.\n"
            "ONE CALLOUT (top-left badge, green bg / white text): 'BLOOMS + PETALS'.\n"
            "Why it wins: it shows two products in one pack — the fastest value read in the category.\n\n"

            "OPTION B — THE ROMANCE PAYOFF (owns the occasion)\n"
            "A finished cake with whole roses set along one tier and petals drifting down onto the "
            "board, shot slightly above on bright white. Two coupes with a rose floating in each.\n"
            "ONE CALLOUT (top-right badge, purple bg / white text): 'WEDDING-CAKE READY'.\n"
            "Why it wins: roses are bought for an occasion, not an ingredient — sell the occasion.\n\n"

            "OPTION C — NEVER WILTS (defuses the fresh-flower pain)\n"
            "Clean split: LEFT a fresh rose visibly browning at the petal edges; RIGHT the Freshly "
            "Preserved rose holding perfect shape and colour. Thin divider between.\n"
            "ONE CALLOUT (top-right badge, green bg / white text): 'NEVER WILTS'.\n"
            "Why it wins: anyone who has ordered fresh roses for an event has watched them turn.\n\n"

            "Across all 3: product dominant, callout ~6% of frame, same lighting and colour temp."
        ),
        overlay="BLOOMS + PETALS",
        overlay_sub="About 12 whole rose blooms plus colourful mixed petals, in one pack.",
        props=["12 whole rose blooms in an arc", "drift of mixed petals", "tipped open pack",
               "finished rose cake", "wilting fresh rose vs preserved rose"],
        lighting="Bright high-key daylight, soft shadows, airy. Identical across all 3 for a clean split test.",
        why_it_works=(
            "Three triggers: A owns the two-formats-in-one-pack value, B owns the wedding occasion, C "
            "defuses the wilting pain. One idea, one prop, one badge each — legible at thumbnail size."
        ),
        ctr="'Blooms + petals' is a value claim no competing dried-rose thumbnail is making.",
        cvr="Option B pre-frames the occasion, so the listing page starts with the buyer's event in mind.",
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: real roses, not silk or potpourri",
        role="hook",
        background="Soft lilac #F5F0F7 — fresh and elegant, never dark or moody",
        purpose="Prove these are genuine, food-grade blooms — the category is full of silk roses and "
                "scented potpourri that look identical in a thumbnail.",
        visual=(
            "Extreme macro of one whole small rose bloom filling most of the frame, lit so the layered "
            "petals, natural veining and the slightly translucent edges read clearly — unmistakably a "
            "real flower, not fabric or moulded plastic. A single mixed petal rests beside it for "
            "contrast. Small 'FOOD-GRADE · EDIBLE' leaf check-mark badge. Keep the rose-pink honest and "
            "natural; no candy saturation."
        ),
        overlay="REAL ROSES. NOT SILK.",
        overlay_sub="Genuine food-grade rose blooms, freeze-dried whole. Edible, never artificial.",
        props=["macro whole rose bloom", "single mixed petal", "food-grade / edible check-mark badge"],
        lighting="Soft directional daylight to reveal layered petal texture and translucency.",
        why_it_works=(
            "Real and fake roses are indistinguishable at thumbnail size, and this category genuinely "
            "sells both. A true-colour macro showing layered petals settles it instantly."
        ),
        ctr="Macro texture stops the scroll where flat product shots do not.",
        cvr="Removes the 'is this decoration or food?' hesitation before it reaches the reviews.",
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: what's inside & every way to use it",
        role="educate",
        background="White with a soft green ribbon footer",
        purpose="Show exactly what arrives — blooms AND petals — and the range of uses. The CVR note "
                "asks for clear contents, usage and function.",
        visual=(
            "Left third: the open pack with the contents laid out honestly, small label 'About 12 whole "
            "rose blooms + mixed flower petals · 0.1 oz'. Right two-thirds: a clean 4-tile 'WAYS TO USE' "
            "grid, each tile a small real photo —\n"
            "  • CAKES & CUPCAKES (whole rose set on buttercream, petals scattered around it)\n"
            "  • COCKTAILS & CHAMPAGNE (rose floating in a coupe / petals frozen into clear ice)\n"
            "  • CHOCOLATES & PASTRY (petals pressed into tempered chocolate, rose on a tart)\n"
            "  • BOARDS & PLATING (petals drifted across charcuterie and a plated dessert)\n"
            "Thin green connectors tie the pack to the four uses."
        ),
        overlay="ONE PACK. TWO FORMATS.",
        overlay_sub="Whole roses to place, mixed petals to scatter. Cakes, drinks, boards.",
        props=["open pack with blooms and petals separated", "4 use-case tiles", "green connector lines"],
        lighting="Bright, even, editorial daylight. Educational clarity beats mood.",
        why_it_works=(
            "The two-format contents are the product's real advantage but are invisible in a standard "
            "product shot. Separating them and showing four uses turns one pack into four reasons to buy."
        ),
        ctr="Grid layouts read as informative at thumbnail size and win the browse-stage click.",
        cvr="Answers 'what exactly is in the pack, and what would I do with it?' in one frame.",
    ),
    AIImagePlanItem(
        name="Image 4 — Desire: the celebration cake moment",
        role="desire",
        background="Styled bright celebration table, soft natural window light",
        purpose="Sell the dream outcome — the wedding, engagement or anniversary centrepiece.",
        visual=(
            "Hero lifestyle shot: a finished celebration cake with whole roses set along the tier seam "
            "and petals drifting down the side onto the linen. Two champagne coupes nearby, each with a "
            "petal floating. The edge of a dessert table in frame, the pack sitting naturally to the "
            "side. Hands mid-placement are welcome — this is the 'action image' the CVR notes ask for. "
            "Light, fresh and aspirational; romantic without going dark or moody."
        ),
        overlay="A CAKE THEY REMEMBER.",
        overlay_sub="Whole roses on the tier, petals down the side. Styled, not sprinkled.",
        props=["tiered celebration cake with roses", "petals drifting onto linen", "2 champagne coupes",
               "styled dessert table", "pack to the side"],
        lighting="Soft natural window light, bright and airy. Aspirational editorial styling — never dark.",
        why_it_works=(
            "Roses are bought for a moment, not a recipe. Showing the moment — and how little effort it "
            "took — is the strongest CVR image in the set."
        ),
        ctr="Finished celebration food out-performs ingredient shots in the mobile carousel.",
        cvr="Transfers the result onto the buyer's own event — the emotional close.",
    ),
    AIImagePlanItem(
        name="Image 5 — Trust: real, shelf-stable, natural, made in USA",
        role="trust",
        background="White with soft green panels behind each badge for separation",
        purpose="Stack the reassurances: real food, nothing added, keeps, arrives protected.",
        visual=(
            "Centre: the resealable pack, clean and premium, two intact rose blooms and a few petals "
            "beside it. Four badges in the corners:\n\n"
            "  • TOP-LEFT — REAL EDIBLE FLOWERS (leaf icon — food-grade, not artificial)\n"
            "  • TOP-RIGHT — SHELF-STABLE (calendar icon — ready for months, no wilting)\n"
            "  • BOTTOM-LEFT — NO ADDED SUGAR, DYES OR PRESERVATIVES\n"
            "  • BOTTOM-RIGHT — MADE IN USA (small US outline)\n\n"
            "Thin strip below, aimed at the 'broken blooms' reviews: 'Delicate by nature — blooms travel "
            "cushioned in a protective resealable pack, and loose petals are part of the design.'"
        ),
        overlay="SHELF-STABLE. STAYS PERFECT.",
        overlay_sub="Real · no added sugar or dyes · made in USA · protective resealable pack.",
        props=["resealable pack", "2 intact roses", "few petals", "4 corner badges", "packaging strip"],
        lighting="Bright studio-even light with a soft catch-light on the pack. Badges legible at thumbnail size.",
        why_it_works=(
            "'Damaged petals or broken blooms' is a named review theme on this listing. Calling out the "
            "protective pack — and reframing loose petals as intended contents rather than damage — "
            "turns the objection into a feature."
        ),
        ctr="Badge clusters read as credentials even when the text is too small to parse.",
        cvr="Neutralises the top 1-star theme before the shopper scrolls to the reviews.",
    ),
    AIImagePlanItem(
        name="Image 6 — Honest size & count (about 12 rose blooms · 0.1 oz)",
        role="desire",
        background="Soft lilac #F5F0F7 — same family as Image 2 for visual rhythm",
        purpose="Set honest size and quantity expectations — 'smaller than expected from the images' is "
                "a named review theme on this listing.",
        visual=(
            "Split-frame.\n\n"
            "LEFT — SCALE, HONESTLY: one whole rose bloom held between finger and thumb, and the same "
            "bloom beside a US quarter and sitting on one cupcake. Caption: 'Small roses — about the "
            "width of a quarter, sized for cupcakes, cookies and drinks.'\n\n"
            "RIGHT — WHAT YOU GET: all 12 rose blooms laid out in a neat flat-lay grid with the mixed "
            "petals drifted alongside, pack beside them, label 'About 12 rose blooms + mixed petals · "
            "0.1 oz'. Do not art-direct this into looking like more than it is — an honest count picture "
            "is what stops the 'smaller than expected' return.\n\n"
            "Footer strip — HANDLING: tweezers placing a rose onto buttercream, note 'Place with tweezers "
            "or clean fingers, store sealed. Petals that separate are perfect for scattering.'"
        ),
        overlay="SMALL ROSES, BIG DETAIL",
        overlay_sub="About 12 blooms plus petals, scaled for cupcakes, cookies and drinks.",
        props=["rose bloom held in fingers", "rose beside a US quarter", "one cupcake for scale",
               "flat-lay of 12 blooms + petals", "tweezers placing a rose"],
        lighting="Bright, even, honest daylight — show the true size and the true colour.",
        why_it_works=(
            "Answers the two loudest 1-star themes head-on: 'smaller than expected' and 'broken petals'. "
            "Honest expectations lift satisfaction and cut returns, while the framing turns the small "
            "size into the right scale for detailed work."
        ),
        ctr="Coin-and-fingertip scale shots are unusual in this category and earn a curiosity click.",
        cvr="Closes the expectation gap that drives this listing's returns and 3-star reviews.",
    ),
    AIImagePlanItem(
        name="Image 7 — Close: find your flower (the variation family)",
        role="close",
        background="Bright white with a soft lilac band behind the family strip",
        purpose="Close on the brand and route the shopper to the right listing in the Freshly Preserved "
                "flower family.",
        visual=(
            "Top two-thirds: brand-forward shot — the Freshly Preserved pack front and centre with whole "
            "roses and a drift of petals around it on bright white, one finished cupcake softly in "
            "frame. Lower band: logo + tagline 'Real blooms. Ready when you are.'\n\n"
            "Bottom third — THE FAMILY STRIP (the variation navigator). One clean row of small "
            "identical-composition photos, each captioned with its name and count:\n"
            f"  {' · '.join(FAMILY[:6])}\n"
            "THIS listing — Small Roses & Mixed — is ringed in brand green with a small 'YOU ARE HERE' "
            "tag; the others sit un-ringed at 70% scale.\n"
            "Caption under the strip: 'Roses for romance, pansies for colour, orchids for elegance — "
            "same real bloom, different occasion.'\n"
            f"Small line at the very bottom: 'Also in the range: {' · '.join(FAMILY[6:])}.'"
        ),
        overlay="FIND YOUR FLOWER.",
        overlay_sub="One family, many blooms. Pick the flower your occasion calls for.",
        props=["Freshly Preserved pack", "whole roses + petals", "finished cupcake",
               "family strip with this listing ringed", "logo + tagline band"],
        lighting="Bright, airy, elegant daylight. Family strip evenly lit so the variations compare fairly.",
        why_it_works=(
            "A shopper who wanted pansies or orchids will otherwise bounce. The strip converts a mismatch "
            "into a sideways sale and closes on brand identity rather than a feature."
        ),
        ctr="Showing a range signals a real brand rather than a one-off seller.",
        cvr="Recovers the wrong-flower shopper inside the family, and seeds the second purchase.",
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Premium Full Image: brand banner",
        role="a+_banner",
        headline="REAL BLOOMS. READY WHEN YOU ARE.",
        body=(
            "Freshly Preserved Small Roses &amp; Mixed brings real rose blooms and colourful flower "
            "petals to cakes, desserts, drinks and boards — about 12 whole roses plus a mix of petals, "
            "freeze-dried so they keep their natural shape and colour. Made in the USA, with no added "
            "sugar, dyes or preservatives, and ready the moment inspiration strikes."
        ),
        visual=("Wide, bright editorial banner — a styled celebration table with a rose-topped cake, two "
                "coupes and the resealable pack, soft natural window light. Logo upper-left, tagline in "
                "the lower band. Desktop 1464x600, mobile 600x450 — keep cake and pack in the mobile "
                "safe area."),
        alt="Freshly Preserved freeze-dried edible rose blooms and petals on a bright celebration table.",
    ),
    AIModule(
        name="Module 2 — Premium Carousel (5 tiles): why Freshly Preserved",
        role="a+_carousel",
        headline="WHY FRESHLY PRESERVED",
        body=(
            "Tile 1: <b>REAL, NOT ARTIFICIAL</b> — Genuine food-grade roses, never silk or potpourri.<br/>"
            "Tile 2: <b>BLOOMS + PETALS</b> — Two formats in one pack: place them, or scatter them.<br/>"
            "Tile 3: <b>NEVER WILTS</b> — Shelf-stable; stock it weeks or months before the event.<br/>"
            "Tile 4: <b>TRUE COLOUR &amp; SHAPE</b> — Freeze-dried whole, so a rose still looks like a rose.<br/>"
            "Tile 5: <b>MADE IN USA · NOTHING ADDED</b> — No added sugar, dyes or preservatives."
        ),
        visual=("5 square tiles at 220x220, purple accent corner on each, consistent bright styling. "
                "Icons: rose · bloom+petal pair · calendar · colour swatch · US leaf. Alt text per tile."),
        alt="Five-tile A+ carousel: real roses, blooms plus petals, shelf-stable, true colour, made in USA.",
    ),
    AIModule(
        name="Module 3 — Premium Full Image: ways to use them",
        role="a+_banner",
        headline="ONE PACK. TWO FORMATS.",
        body=(
            "Set whole roses along a cake tier, on cupcakes, cookies and tarts. Float one in a coupe of "
            "champagne, or freeze petals into clear ice. Press petals into tempered chocolate and "
            "pastry. Drift them across charcuterie, grazing boards and plated desserts. Whole blooms are "
            "the focal point; the mixed petals fill everything around them — which is why one pack "
            "finishes a whole dessert table."
        ),
        visual=("Wide 4-panel banner: CAKE (rose on the tier, petals down the side) → CHAMPAGNE & ICE → "
                "CHOCOLATE & PASTRY → BOARDS & PLATING. Bright, editorial, thin purple dividers. Mobile "
                "keeps 2 panels stacked."),
        alt="A+ banner showing four ways to use Freshly Preserved edible rose blooms and petals.",
    ),
    AIModule(
        name="Module 4 — Premium Full Image: fresh flowers wilt, these don't",
        role="a+_banner",
        headline="FRESH ROSES WILT. THESE DON'T.",
        body=(
            "Fresh roses are seasonal, fragile and spoil within days — they brown at the edges, curl and "
            "drop right when the cake is due. These roses are freeze-dried whole and shelf-stable, so "
            "they hold their shape and natural colour until your event. Order weeks ahead, decorate on "
            "your own schedule, and waste nothing."
        ),
        visual=("Wide banner split in two: LEFT — a fresh rose visibly browning at the petal edges, "
                "muted. RIGHT — a Freshly Preserved rose, intact and natural, beside the resealable "
                "pack. Clean centre divider, bright background. Never a dark or moody treatment."),
        alt="A+ banner comparing a wilting fresh rose with a shelf-stable Freshly Preserved edible rose.",
    ),
    AIModule(
        name="Module 5 — Premium Carousel (5 tiles): choose your variation",
        role="a+_carousel",
        headline="FIND YOUR FLOWER",
        body=(
            "<b>You are viewing: Small Roses &amp; Mixed — about 12 rose blooms plus petals (0.1 oz).</b> "
            "Every variation is the same real, freeze-dried, food-grade flower — pick the bloom your "
            "occasion calls for.<br/><br/>"
            "Tile 1: <b>Small Roses &amp; Mixed</b> — Romance: weddings, anniversaries, engagements.<br/>"
            "Tile 2: <b>Small Pansy · 12 blooms</b> — Flat, bright faces for cupcakes and cookies.<br/>"
            "Tile 3: <b>Small Orchid · 12 blooms</b> — Sculptural blooms for drinks and cake tiers.<br/>"
            "Tile 4: <b>Pansy &amp; Orchids · 25 blooms</b> — Event quantity across two flowers.<br/>"
            "Tile 5: <b>Flower Petals · about 1.5 cups</b> — Pure coverage, no whole blooms.<br/><br/>"
            "Also in the Freshly Preserved range: Purple Orchids · Marigolds · Small Mini Carnations "
            "&amp; Bachelors · Squash Blossoms · Basil Blossoms · the Fall Cake Decorating Kit."
        ),
        visual=("5 identical-composition variation tiles at 220x220 — same white background, lighting "
                "and camera height, so the flowers compare honestly. THIS variation (Small Roses &amp; "
                "Mixed) carries a green ring and a small 'YOU ARE HERE' tag. Per-tile alt text names the "
                "variation and its count."),
        alt="Five-tile A+ carousel of the Freshly Preserved edible flower range with the rose pack marked.",
    ),
    AIModule(
        name="Module 6 — Premium Full Image: from the brand (benefits closer)",
        role="a+_banner",
        headline="FROM FRESHLY PRESERVED",
        body=(
            "We freeze-dry our flowers whole, in the USA, so the rose that leaves us is the rose that "
            "lands on your cake — same layered shape, same natural colour, months later. No added sugar, "
            "no dyes, no preservatives, and nothing artificial pretending to be a flower. This pack "
            "holds <b>about 12 whole rose blooms plus mixed flower petals (0.1 oz)</b> in a resealable "
            "pack that keeps them protected between projects. Small kitchens, big possibilities."
        ),
        visual=("Warm benefits/brand closer: soft-focus freeze-drying trays of roses on the left, the "
                "resealable pack and a rose-topped dessert on the right, brand-voice line across the "
                "middle. Bright and airy — never dark behind the logo."),
        alt="Freshly Preserved brand closing banner: freeze-dried whole in the USA, nothing added.",
    ),
    AIModule(
        name="Module 7 — Premium Q&A (finale)",
        role="a+_qa",
        headline="QUESTIONS BEFORE YOU BUY",
        body=(
            "<b>Q.</b> What exactly is in the pack?<br/>"
            "<b>A.</b> About 12 whole small rose blooms plus a mix of colourful flower petals, 0.1 oz "
            "in total. The whole roses are your focal points; the petals fill everything around "
            "them.<br/><br/>"

            "<b>Q.</b> Are these real flowers, and are they edible?<br/>"
            "<b>A.</b> Yes. Genuine, food-grade roses and petals, freeze-dried — real edible flowers, "
            "not silk, potpourri or artificial decoration.<br/><br/>"

            "<b>Q.</b> How big are the roses?<br/>"
            "<b>A.</b> These are small roses — roughly the width of a US quarter, scaled for cupcakes, "
            "cookies and drink garnishes. See the size image for a real-scale reference.<br/><br/>"

            "<b>Q.</b> How long do they last, and how should I store them?<br/>"
            "<b>A.</b> They are shelf-stable and will not wilt like fresh roses. Keep them sealed, away "
            "from moisture and humidity, and use them whenever you need them — ideal for ordering weeks "
            "before a wedding.<br/><br/>"

            "<b>Q.</b> Will they arrive intact?<br/>"
            "<b>A.</b> Freeze-dried blooms are naturally light and delicate, so they travel cushioned in "
            "a protective resealable pack. Handle gently and place with tweezers or clean fingers. Loose "
            "petals are part of what the pack contains, not a fault.<br/><br/>"

            "<b>Q.</b> Will the colour match the photos?<br/>"
            "<b>A.</b> We keep our images honest to the real bloom. Freeze-drying preserves the natural "
            "colour and shape, though shades vary between flowers because these are real botanicals.<br/><br/>"

            "<b>Q.</b> Do they taste or smell strong?<br/>"
            "<b>A.</b> They are mild, with no added sugar or dyes. Roses are used mainly for natural "
            "presentation on cakes, drinks and boards rather than for strong flavour."
        ),
        visual=("Vertical Q/A table, text only. Purple divider lines between questions, small green Q. "
                "and purple A. labels. Mobile-first line lengths."),
        alt="Premium Q&A module answering the most-asked questions about Freshly Preserved edible roses.",
    ),
]


QA = [
    AIQA(q="What exactly is in the pack?",
         a="About 12 whole small rose blooms plus a mix of colourful flower petals, 0.1 oz in total. The "
           "whole roses are your focal points; the petals fill everything around them."),
    AIQA(q="Are these real flowers, and are they edible?",
         a="Yes. Genuine, food-grade roses and petals, freeze-dried whole. Real edible flowers — not "
           "silk, not potpourri, not artificial decoration."),
    AIQA(q="How big are the roses? They look small.",
         a="They are small roses, roughly the width of a US quarter — scaled for cupcakes, cookies and "
           "drink garnishes where a full-size rose would overwhelm the piece. The size image shows one "
           "beside a coin and on a cupcake."),
    AIQA(q="How long do they last and how do I store them?",
         a="They are shelf-stable and will not wilt like fresh roses. Keep them sealed in the pack away "
           "from moisture and humidity, and use them whenever you need them — ideal for ordering weeks "
           "ahead of a wedding."),
    AIQA(q="Will they arrive intact? Mine are for a wedding.",
         a="Freeze-dried blooms are light and delicate by nature, so they ship cushioned in a protective "
           "resealable pack. Handle gently and place with tweezers or clean fingers. Loose petals are "
           "part of what the pack contains, not damage."),
    AIQA(q="Will the colour match the photos?",
         a="We keep our images honest to the real bloom. Freeze-drying preserves the natural rose colour "
           "and layered shape, though shades vary slightly between flowers because these are real "
           "botanicals."),
    AIQA(q="Do they taste or smell strong?",
         a="They are mild, with no added sugar or dyes. These roses are used mainly for natural "
           "presentation on cakes, drinks and boards rather than for strong flavour."),
    AIQA(q="What can I use them for?",
         a="Wedding and celebration cakes, cupcakes, cookies and tarts; chocolates and pastries; "
           "champagne, cocktails and clear ice cubes; charcuterie and grazing boards; plated desserts; "
           "and craft projects such as resin art."),
    AIQA(q="Roses or a mixed-flower pack — which should I choose?",
         a="Roses read as romance and suit weddings, anniversaries and engagements. Pansies bring bright "
           "multicolour, orchids bring elegance, and the loose petal mix is pure coverage. Every "
           "variation is the same real, freeze-dried bloom."),
]


def main() -> None:
    print("Loading Freshly Preserved customer + parsing listing…")
    cust = load_customer("freshly_preserved")
    brief = parse_excel(EXCEL)
    seo = load_seo(EXCEL)
    OUT = HERE / f"{PLAN_NO}_{ASIN}_Image Plan.pdf"
    print(f"  Product: {brief.product_name}  ASIN {ASIN}  Marketplace: {cust.marketplace}")
    print(f"  USPs={len(brief.usps)} KWs={len(brief.all_keywords)} Q&A={len(brief.rufus_qa)} "
          f"reviews=+{len(brief.good_reviews)}/-{len(brief.bad_reviews)}")

    builder = BriefBuilder(cust, brief, OUT, ai=None)
    builder._ai_title = seo.title
    builder._ai_bullets = as_bullets_html(seo)
    builder._ai_images = IMAGES
    builder._ai_modules = MODULES
    builder._ai_qa = QA
    builder._ai_backend = seo.backend
    builder.copy_source_label = ("SEO sheet (title/bullets/backend) + hand-written senior creative "
                                 "(overlays, A+, Q&A) — US/English")

    print("Building branded PDF…")
    pdf_path = builder.build()
    import re
    pages = len(re.findall(rb'/Type\s*/Page[^s]', pdf_path.read_bytes()))
    print(f"Built: {pdf_path}")
    print(f"  Pages: {pages}  Size: {pdf_path.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
