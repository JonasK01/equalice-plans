"""Freshly Preserved — Small Pansy & Orchid Freeze-Dried Edible Flowers
Hand-written, KW-led, conversion-focused copy injected into the branded pipeline.

Marketplace: amazon.com (USA) — English overlays + customer copy.
ASIN: B0GMRFZD2G · Product 01 · Brand: Freshly Preserved (edible-flowers line).

Positioning: REAL edible flowers, not artificial. Win the click on the promise
"real blooms that keep their color & shape, ready anytime" — and defuse the top
review objections (too small, arrived crumbled, duller than photos) right on-image.

Compliance guardrails (US):
  - No best / #1 / guaranteed · no health-cure claims · no prices or URLs on-image.
  - Keep color HONEST — reviewers already complain 'not as bright as pictures'.
  - Always show a SIZE reference — 'smaller than expected' is the #1 complaint.
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


EXCEL = HERE / "listing.xlsx"
PLAN_NO = "01"
ASIN_OVERRIDE = "B0GMRFZD2G"   # excel stores the parent ASIN; this file is the Pansy+Orchid variant


# ===== KW-led copy (US / English) =====

TITLE = ('Freshly Preserved Small Pansy & Orchid Freeze-Dried Edible Flowers — Real Blooms for '
         'Cake Decorating, Cupcakes, Cocktails & Charcuterie · Shelf-Stable · 100% Natural · '
         'No Preservatives · Made in USA')

BULLETS = [
    "<b>REAL EDIBLE FLOWERS — NOT ARTIFICIAL</b> — Genuine pansies and orchids, gently "
    "freeze-dried so they keep their true color and natural bloom shape. Food-grade and ready to "
    "place straight onto cakes, cupcakes, cookies, cocktails and plated desserts — the real, "
    "elegant detail that makes a dessert look professionally styled.",

    "<b>NEVER WILTS — READY THE MOMENT YOU ARE</b> — Fresh edible flowers brown, curl and spoil "
    "within days. These are shelf-stable, so you can stock them ahead of a wedding, birthday or "
    "dinner party and reach for a perfect bloom whenever inspiration strikes — no last-minute "
    "florist run, no waste.",

    "<b>MADE FOR SHOWPIECES — CAKES TO COCKTAILS</b> — Beautiful on wedding cake toppers, "
    "cupcakes and dessert boards; stunning as a cocktail or mocktail garnish; perfect for "
    "charcuterie and grazing boards, fine-dining plating, and even resin and DIY craft projects. "
    "One jar, endless presentation.",

    "<b>WHOLE BLOOMS + PETALS · SIZED FOR DETAIL</b> — A mix of small, delicate pansies and "
    "orchids — the right scale for cupcakes, cookies and drink garnishes where a full-size bloom "
    "would overwhelm. Lightweight and airy by nature, so handle gently and place with tweezers "
    "for flawless results.",

    "<b>100% NATURAL · MADE IN USA · RESEALABLE JAR</b> — No preservatives and no added sugar — "
    "just real flowers. Packed in a protective resealable jar that keeps the blooms intact and "
    "fresh between uses, so your last celebration looks as good as your first.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="Clean bright white with a whisper of soft lilac #F5F0F7 across the bottom 15% for grounding. Identical background across all 3 options so the split test isolates composition, not color.",
        purpose="Win the click in a grid of look-alike dried-flower listings. Ship all 3, keep the winner via Amazon Manage Your Experiments.",
        visual=(
            "Mock ALL 3 options — brand A/B tests and keeps the winner. Each: ONE callout, ONE "
            "supporting prop, product dominant. Colors stay TRUE to the real bloom (buyers "
            "complain 'not as bright as pictures' — do not over-saturate). Amazon slot-1 main "
            "must stay pure-white / product-only — these callout versions are the CTR mains you "
            "A/B test against a clean white main.\n\n"

            "OPTION A — REAL BLOOMS HERO (owns 'real, not artificial')\n"
            "An open resealable jar tipped slightly, small pansies and orchids spilling out onto "
            "white in a soft natural arc — a few blooms crisp and whole in the foreground so the "
            "petals read as REAL. Lower-right: a single cupcake topped with one bloom for scale + "
            "payoff.\n"
            "ONE CALLOUT (top-left badge, green bg / white text): 'REAL EDIBLE FLOWERS'.\n"
            "Why it wins: the category is full of plastic-looking 'decorations' — showing genuine, "
            "delicate, true-color blooms is the fastest trust signal.\n\n"

            "OPTION B — THE PAYOFF (owns the outcome)\n"
            "A beautifully finished cupcake or a stemmed cocktail, garnished with pansies and "
            "orchids, shot slightly above on bright white. The jar sits softly out of focus "
            "behind it.\n"
            "ONE CALLOUT (bottom-right badge, purple bg / white text): 'CAKES. COCKTAILS. BOARDS.'\n"
            "Why it wins: the buyer is really shopping for the RESULT — a showpiece dessert or "
            "drink. Selling the outcome beats selling a bag of petals.\n\n"

            "OPTION C — NEVER WILTS (defuses fresh-flower pain)\n"
            "Clean split: LEFT a fresh pansy visibly wilting/browning; RIGHT the Freshly Preserved "
            "bloom holding perfect color and shape. A thin arrow or divider between.\n"
            "ONE CALLOUT (top-right badge, green bg / white text): 'NEVER WILTS'.\n"
            "Why it wins: names the #1 frustration with fresh edible flowers and positions "
            "shelf-stable as the fix — in one glance.\n\n"

            "Across all 3: product dominant, callout ~6% of frame, same lighting + color temp."
        ),
        overlay="(one callout per option — see visual)",
        overlay_sub="3 hero options shipped — A/B test, keep the winner.",
        props=[
            "OPTION A: tipped resealable jar + spilling pansies & orchids + 1 cupcake for scale",
            "OPTION B: finished cupcake or cocktail garnished with blooms + jar soft-focus behind",
            "OPTION C: wilting fresh pansy (left) vs intact preserved bloom (right) + divider",
        ],
        lighting="Bright high-key daylight, soft shadows, airy. Same across all 3 for a clean split test.",
        why_it_works=(
            "Three triggers: A owns 'real, not artificial', B sells the finished showpiece "
            "(outcome), C defuses the fresh-flower pain (wilting). One idea, one prop, one badge "
            "each — readable at mobile thumbnail size, honest color."
        ),
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: Real edible flowers, not plastic decoration",
        role="hook",
        background="Soft lilac #F5F0F7 — fresh, elegant (not dark or moody)",
        purpose="Land the #1 differentiator in one frame: these are genuine, food-grade blooms.",
        visual=(
            "Extreme macro of a single pansy and a single orchid side by side, petals lit so the "
            "natural veining and true color read clearly — unmistakably REAL, not molded plastic. "
            "A small 'food-grade / edible' leaf check-mark badge sits beside them. Keep the color "
            "honest and natural — no candy over-saturation."
        ),
        overlay="REAL FLOWERS. NOT PLASTIC.",
        overlay_sub="Genuine, food-grade pansies & orchids — freeze-dried, edible, elegant.",
        props=["macro pansy + orchid", "food-grade / edible check-mark badge"],
        lighting="Soft directional daylight to reveal petal texture and veining. Clarity over drama.",
        why_it_works=(
            "Buyers can't tell real from fake in a thumbnail grid. A true-color macro that shows "
            "petal veining proves authenticity instantly and answers the quiet worry: 'are these "
            "actually real, edible flowers?'"
        ),
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: What's in the jar & how to use it",
        role="educate",
        background="White with a soft green ribbon footer",
        purpose="Show the varieties and the range of uses so the buyer pictures their own project.",
        visual=(
            "Left third: the open jar with a neat grouping of pansies + orchids, a small label "
            "'Whole blooms + petals'. Right two-thirds: a clean 4-tile 'WAYS TO USE' grid, each "
            "tile a small real photo —\n"
            "  • CAKES & CUPCAKES (bloom on buttercream)\n"
            "  • COCKTAILS & MOCKTAILS (bloom on a glass rim / frozen in an ice cube)\n"
            "  • CHARCUTERIE & GRAZING BOARDS (blooms scattered among cheese & fruit)\n"
            "  • PLATING & DIY / RESIN (bloom on a plated dessert / in clear resin)\n"
            "Thin green connectors tie the jar to the uses."
        ),
        overlay="ONE JAR. ENDLESS OCCASIONS.",
        overlay_sub="Cakes · cupcakes · cocktails · charcuterie · plating · DIY & resin crafts.",
        props=["open jar of pansies + orchids", "4 use-case tiles", "green connector lines"],
        lighting="Bright, even, editorial daylight. Educational clarity beats mood.",
        why_it_works=(
            "The product's value is versatility. Showing four concrete, aspirational uses lets "
            "bakers, mixologists and hosts all see themselves in the frame and justifies the "
            "purchase for more than a single occasion."
        ),
    ),
    AIImagePlanItem(
        name="Image 4 — Desire: The showpiece moment",
        role="desire",
        background="Styled bright celebration table, soft natural window light",
        purpose="Sell the dream outcome — an elegant, professional-looking centerpiece.",
        visual=(
            "Hero lifestyle shot: a beautifully finished celebration cake (or a tiered cupcake "
            "stand) crowned with pansies and orchids, on a styled bright table — soft linen, a "
            "couple of stemmed cocktails also garnished with blooms, a grazing board edge in "
            "frame. Everything light, fresh and aspirational, like a stylist's table. The jar "
            "sits naturally to the side. Freshly Preserved logo small, lower-corner."
        ),
        overlay="STEAL THE SHOW.",
        overlay_sub="Wedding cakes, cocktails & boards that look professionally styled.",
        props=["finished floral cake or cupcake tower", "2 garnished cocktails", "grazing board edge", "styled linen table", "jar to the side"],
        lighting="Soft natural window light, bright and airy. Aspirational editorial styling — never dark.",
        why_it_works=(
            "Sells the outcome, not the petals: the buyer is imagining the gasp at their event. "
            "The strongest CVR image — it shows exactly the 'showpiece' result they're paying "
            "for, with the product doing the work."
        ),
    ),
    AIImagePlanItem(
        name="Image 5 — Trust: Shelf-stable, natural, made in USA",
        role="trust",
        background="White with soft green panels behind each badge for separation",
        purpose="Stack the reassurances that defuse 'will they last / are they real food / are they safe?'",
        visual=(
            "Center: the resealable jar, clean and premium, a few intact blooms beside it. Four "
            "badges in the corners:\n\n"
            "  • TOP-LEFT — REAL EDIBLE FLOWERS (leaf icon — food-grade, not artificial)\n"
            "  • TOP-RIGHT — SHELF-STABLE (calendar icon — ready for months, no wilting)\n"
            "  • BOTTOM-LEFT — 100% NATURAL (no preservatives, no added sugar)\n"
            "  • BOTTOM-RIGHT — MADE IN USA (small US flag / outline)\n\n"
            "Thin strip below: 'Freeze-dried to lock in real color & natural shape · resealable "
            "jar keeps blooms protected between uses.'"
        ),
        overlay="SHELF-STABLE. STAYS PERFECT.",
        overlay_sub="Real · 100% natural · no preservatives · made in USA · resealable jar.",
        props=["resealable jar", "intact blooms", "4 corner badges", "thin supporting strip"],
        lighting="Bright studio-even light with a soft catch-light on the jar. Badges legible at thumbnail size.",
        why_it_works=(
            "The category's trust gaps are 'are they real & safe to eat?' and 'will they keep?'. "
            "Stacking real + shelf-stable + natural + made-in-USA answers every doubt in one "
            "frame before the buyer has to ask."
        ),
    ),
    AIImagePlanItem(
        name="Image 6 — Size & handling clarity (defuse #1 complaint)",
        role="desire",
        background="Soft lilac #F5F0F7 — same family as Image 2 for visual rhythm",
        purpose="Set honest size expectations and reassure on fragility — the top two review complaints.",
        visual=(
            "Split-frame.\n\n"
            "LEFT: a single pansy and a single orchid held on a fingertip (or beside a US quarter "
            "and resting on one cupcake) so the SMALL scale is unmistakable and honest. Caption: "
            "'Small blooms — sized for cupcakes, cookies & drinks.'\n\n"
            "RIGHT: a 'HANDLE WITH CARE' mini how-to — tweezers gently placing a bloom onto "
            "buttercream, with a soft note: 'Delicate by nature — place with tweezers or fingers, "
            "store sealed.' Show a couple of whole intact blooms plus a few loose petals so buyers "
            "know petals are usable too.\n\n"
            "Small footer: 'Airy & lightweight — a little goes a long way.'"
        ),
        overlay="SMALL BLOOMS, BIG DETAIL.",
        overlay_sub="Sized for cupcakes, cookies & drinks — delicate, so place with care.",
        props=["pansy + orchid on fingertip / by a coin", "one cupcake for scale", "tweezers placing a bloom", "few loose petals"],
        lighting="Bright, even, honest daylight — show the true size and true color.",
        why_it_works=(
            "Directly answers the two biggest 1-star themes — 'smaller than expected' and "
            "'fragile/crumbled'. Setting honest expectations up front lifts satisfaction and cuts "
            "returns, while framing the small size as the right scale for detailed work."
        ),
    ),
    AIImagePlanItem(
        name="Image 7 — Brand close: Real blooms, always ready",
        role="close",
        background="Bright, elegant styled surface — soft daylight",
        purpose="Close on the brand promise and identity before checkout.",
        visual=(
            "Clean brand-forward shot: the Freshly Preserved jar front and center with a graceful "
            "scatter of pansies and orchids around it on bright white, one finished cupcake or "
            "cocktail softly in frame. Lower band: Freshly Preserved logo + tagline. A short, "
            "honest reassurance line about real, shelf-stable edible flowers made in the USA."
        ),
        overlay="REAL BLOOMS. ALWAYS READY.",
        overlay_sub="Freshly Preserved — real edible flowers, ready the moment you are.",
        props=["Freshly Preserved jar", "scatter of pansies + orchids", "one finished cupcake or cocktail", "logo + tagline band"],
        lighting="Bright, airy, elegant daylight. Aspirational and brand-forward.",
        why_it_works=(
            "Closes on identity, not features: the buyer isn't buying dried petals, they're "
            "buying effortless, always-ready elegance. Ties the plan back to the brand promise "
            "the moment before add-to-cart."
        ),
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Brand banner: Real blooms. Ready when you are.",
        role="a+_banner",
        headline="REAL BLOOMS. READY WHEN YOU ARE.",
        body=(
            "Freshly Preserved freeze-dried edible flowers are real, food-grade pansies and "
            "orchids that keep their true color and natural shape — so you can create showpiece "
            "cakes, cocktails and boards without the wilting, browning and waste of fresh flowers. "
            "Made in the USA, 100% natural, ready the moment inspiration strikes."
        ),
        visual="Wide, bright editorial banner — a styled celebration table with a floral cake, a garnished cocktail and the resealable jar, soft natural window light. Freshly Preserved logo upper-left, tagline in the lower band.",
        alt="Freshly Preserved edible pansies and orchids styled on a bright celebration table with a floral cake and cocktail.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): Why Freshly Preserved",
        role="a+_carousel",
        headline="WHY FRESHLY PRESERVED",
        body=(
            "Tile 1: <b>REAL, NOT ARTIFICIAL</b> — Genuine food-grade pansies &amp; orchids.<br/>"
            "Tile 2: <b>NEVER WILTS</b> — Shelf-stable; ready weeks or months ahead.<br/>"
            "Tile 3: <b>TRUE COLOR &amp; SHAPE</b> — Freeze-dried to keep the natural bloom.<br/>"
            "Tile 4: <b>ENDLESSLY VERSATILE</b> — Cakes, cocktails, charcuterie, plating, DIY.<br/>"
            "Tile 5: <b>100% NATURAL · MADE IN USA</b> — No preservatives, no added sugar."
        ),
        visual="5 square tiles, purple accent corner on each, consistent bright styling. Small icons (pansy · calendar · color swatch · cupcake+glass · US leaf).",
        alt="Five-tile Premium A+ carousel covering Freshly Preserved differentiators: real not artificial, never wilts, true color, versatile, natural made in USA.",
    ),
    AIModule(
        name="Module 3 — Banner: Ways to use them",
        role="a+_banner",
        headline="ONE JAR. ENDLESS OCCASIONS.",
        body=(
            "Crown wedding cakes, cupcakes and dessert boards. Garnish cocktails and mocktails, "
            "or freeze a bloom into a clear ice cube. Scatter across charcuterie and grazing "
            "boards. Finish plated desserts like a pastry chef — and go beyond food into resin "
            "art and DIY crafts. Whole blooms for statement styling, petals for the fine detail."
        ),
        visual="Wide 4-panel banner: CAKE (bloom on buttercream) → COCKTAIL (bloom on a glass / in ice) → CHARCUTERIE (blooms among cheese & fruit) → PLATING / RESIN. Bright, editorial, thin purple dividers.",
        alt="Premium A+ banner showing four ways to use Freshly Preserved edible flowers: cakes, cocktails, charcuterie, and plating or resin.",
    ),
    AIModule(
        name="Module 4 — Banner: Fresh flowers wilt. These don't.",
        role="a+_banner",
        headline="FRESH FLOWERS WILT. THESE DON'T.",
        body=(
            "Fresh edible flowers are seasonal, fragile and spoil within days — they brown, curl "
            "and lose their shape right when you need them. Freshly Preserved blooms are "
            "freeze-dried and shelf-stable, so they hold their color and form until your event. "
            "Stock the jar ahead, skip the last-minute florist run, and waste nothing."
        ),
        visual="Wide banner split in two: LEFT — a fresh pansy visibly wilting and browning, muted. RIGHT — a Freshly Preserved bloom, bright and intact, beside the resealable jar. Clean divider, bright background.",
        alt="Premium A+ banner comparing a wilting fresh flower to a shelf-stable Freshly Preserved edible bloom.",
    ),
    AIModule(
        name="Module 5 — Carousel (5 tiles): The Freshly Preserved flower range",
        role="a+_carousel",
        headline="EXPLORE THE FLOWER RANGE",
        body=(
            "Tile 1: <b>PANSIES</b> — Bright, flat blooms — perfect on cupcakes &amp; cookies.<br/>"
            "Tile 2: <b>ORCHIDS</b> — Elegant, delicate — a refined cocktail &amp; cake garnish.<br/>"
            "Tile 3: <b>ROSES &amp; PETALS</b> — Romantic scatter for cakes &amp; grazing boards.<br/>"
            "Tile 4: <b>MARIGOLDS &amp; MORE</b> — Warm color for plating &amp; charcuterie.<br/>"
            "Tile 5: <b>MIXED &amp; SAMPLER BOXES</b> — Variety for every occasion.<br/>"
            "<i>This listing: Small Pansy &amp; Orchid mix. Explore the full Freshly Preserved range for more varieties.</i>"
        ),
        visual="5 identical-composition variety tiles (pansy · orchid · rose petals · marigold · mixed box), each a bright real bloom photo. Purple accent corner; consistent airy daylight.",
        alt="Five-tile A+ carousel of the Freshly Preserved edible flower range: pansies, orchids, roses and petals, marigolds, and mixed sampler boxes.",
    ),
    AIModule(
        name="Module 6 — Premium Q&A",
        role="a+_qa",
        headline="QUESTIONS BEFORE YOU BUY",
        body=(
            "<b>Q.</b> Are these real flowers, and are they edible?<br/>"
            "<b>A.</b> Yes. They are genuine, food-grade pansies and orchids that have been "
            "freeze-dried — real edible flowers, not artificial decoration.<br/><br/>"

            "<b>Q.</b> How big are the blooms?<br/>"
            "<b>A.</b> This is the small size — delicate pansies and orchids scaled for cupcakes, "
            "cookies and drink garnishes, where a large bloom would overwhelm. See the size image "
            "for a real-scale reference.<br/><br/>"

            "<b>Q.</b> How long do they last, and how should I store them?<br/>"
            "<b>A.</b> They are shelf-stable — no wilting like fresh flowers. Keep them in the "
            "resealable jar, away from moisture, and use them whenever you need a perfect "
            "bloom.<br/><br/>"

            "<b>Q.</b> Are they fragile? How do I handle them?<br/>"
            "<b>A.</b> Freeze-dried flowers are naturally light and delicate. Handle gently and "
            "place with tweezers or clean fingers for flawless results. Petals that separate are "
            "still perfect for scattering.<br/><br/>"

            "<b>Q.</b> Do they have a strong taste or smell?<br/>"
            "<b>A.</b> They are mild — used primarily for beautiful, natural presentation on cakes, "
            "drinks and boards rather than for strong flavor.<br/><br/>"

            "<b>Q.</b> What can I use them for?<br/>"
            "<b>A.</b> Cakes, cupcakes and wedding toppers; cocktails and mocktails; charcuterie "
            "and grazing boards; plated desserts; and craft projects like resin art. 100% "
            "natural, made in the USA."
        ),
        visual="Vertical Q/A table. Purple divider lines between each question. Small green Q. and purple A. labels.",
        alt="Premium Q&A module answering the six most-asked questions for Freshly Preserved edible pansies and orchids.",
    ),
    AIModule(
        name="Module 7 — Premium Comparison Chart",
        role="a+_comparison",
        headline="THE SMARTER WAY TO STYLE",
        body=(
            "Compare across 4 columns: <b>Freshly Preserved Freeze-Dried Flowers</b> · Fresh cut "
            "edible flowers · Artificial / plastic flower decorations · Generic dried petals.<br/><br/>"
            "Rows: Real &amp; edible (Yes) · Keeps true color &amp; shape · Shelf-stable (no wilting) · "
            "Whole blooms + petals · No preservatives / no added sugar · Ready to use anytime · "
            "Made in USA.<br/><br/>"
            "Highlight the Freshly Preserved column with a soft green tint and a 'REAL &amp; READY' "
            "ribbon at the top of the column."
        ),
        visual="Standard Amazon Premium Comparison Chart, 4 columns. Alternative columns use category descriptors only — no brand names. Green header row, purple highlight on the Freshly Preserved column.",
        alt="Premium comparison chart for Freshly Preserved vs. fresh cut edible flowers, artificial decorations, and generic dried petals.",
    ),
]


QA = [
    AIQA(q="Are these real flowers, and are they edible?",
         a="Yes. They are genuine, food-grade pansies and orchids that have been gently freeze-dried. Real edible flowers, not artificial decoration."),
    AIQA(q="How big are the blooms? They look small.",
         a="This is the small size — delicate pansies and orchids scaled for cupcakes, cookies and drink garnishes, where a full-size bloom would overwhelm the piece. Check the size-reference image for real scale so there are no surprises."),
    AIQA(q="How long do they last and how do I store them?",
         a="They are shelf-stable and will not wilt like fresh flowers. Keep them in the resealable jar away from moisture and use them whenever you need a perfect bloom — great for stocking ahead of an event."),
    AIQA(q="Are they fragile? Mine need to arrive intact.",
         a="Freeze-dried flowers are naturally light and delicate. They are packed in a protective resealable jar; handle gently and place with tweezers or clean fingers. Any petals that separate are still perfect for scattering on cakes and boards."),
    AIQA(q="Will the color match the photos?",
         a="We keep our images honest to the real bloom. Freeze-drying preserves the natural color and shape, though shades vary slightly from flower to flower because these are real botanicals, not printed decorations."),
    AIQA(q="Do they taste or smell strong?",
         a="They are mild. These flowers are used mainly for beautiful, natural presentation on cakes, drinks and boards rather than for strong flavor."),
    AIQA(q="What can I use them for?",
         a="Cakes, cupcakes and wedding cake toppers; cocktails and mocktails; charcuterie and grazing boards; plated desserts and fine-dining styling; and craft projects such as resin art. Whole blooms for statement styling, petals for fine detail."),
    AIQA(q="Are they natural and where are they made?",
         a="They are 100% natural with no preservatives and no added sugar, and they are made in the USA."),
]


# Backend KWs — stem-deduped, byte-packed. Avoid brand names already in the title and superlatives.
BACKEND = (
    "edible flowers freeze dried dried edible flowers pansies orchids cake decorating cupcake "
    "toppers wedding cake topper cocktail garnish mocktail charcuterie board grazing plating "
    "dessert decoration food grade real flowers petals resin craft shelf stable natural made in "
    "usa no preservatives baking pastry mixology event styling"
)


def main() -> None:
    print("Loading Freshly Preserved customer + parsing listing…")
    cust = load_customer("freshly_preserved")
    brief = parse_excel(EXCEL)
    asin = ASIN_OVERRIDE
    OUT = HERE / f"{PLAN_NO}_{asin}_Image Plan.pdf"
    print(f"  Product: {brief.product_name} (Small Pansy & Orchid variant)")
    print(f"  ASIN (file/variant): {asin}  Marketplace: {cust.marketplace}")
    print(f"  USPs={len(brief.usps)} KWs={len(brief.all_keywords)} Q&A={len(brief.rufus_qa)} reviews=+{len(brief.good_reviews)}/-{len(brief.bad_reviews)}")

    builder = BriefBuilder(cust, brief, OUT, ai=None)
    builder._ai_title = TITLE
    builder._ai_bullets = BULLETS
    builder._ai_images = IMAGES
    builder._ai_modules = MODULES
    builder._ai_qa = QA
    builder._ai_backend = BACKEND
    builder.copy_source_label = "Hand-written senior copy (KW-led, US/English)"

    print("Building branded PDF…")
    pdf_path = builder.build()
    size_kb = pdf_path.stat().st_size // 1024
    import re
    pages = len(re.findall(rb'/Type\s*/Page[^s]', pdf_path.read_bytes()))
    print(f"Built: {pdf_path}")
    print(f"  Pages: {pages}  Size: {size_kb} KB")


if __name__ == "__main__":
    main()
