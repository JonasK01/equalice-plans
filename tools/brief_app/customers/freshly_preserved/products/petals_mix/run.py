"""Freshly Preserved — Product 01 · Freeze-Dried Edible FLOWER PETALS 0.2 oz (about 1.5 cups).

ASIN: B0H8FDVXFJ · Marketplace: amazon.com (USA) — English overlays + customer copy.
(The Overview tab also carries an older ASIN, B0CV9435JM — the SEO deliverable is filed
under B0H8FDVXFJ, so that is the ASIN used here.)

WHAT MAKES THIS ONE DIFFERENT: this is the PETAL variation, not a whole-bloom pack. Loose
petals from roses, carnations, pansies and orchids, about 1.5 CUPS of them. Whole blooms are
focal points; petals are COVERAGE — confetti across a cake, a scatter down a grazing board,
a drift over a plated dessert. Volume is the hero fact, and it is also the answer to the
"package looks smaller than expected" review theme: show the 1.5 cups, measured.

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
PLAN_NO = "01"
ASIN = "B0H8FDVXFJ"

FAMILY = [
    "Flower Petals · about 1.5 cups (this listing)",
    "Small Pansy · 12 whole blooms",
    "Small Orchid · 12 whole blooms",
    "Pansy & Orchids · 25 whole blooms",
    "Small Roses & Mixed · about 12 rose blooms",
    "Squash Blossoms · 12 whole blooms",
    "Basil Blossoms · about 25 sprigs",
    "Fall Cake Decorating Kit · 25+ flowers & leaves",
    "Marigolds",
    "Small Mini Carnations & Bachelors",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="Clean bright white with a whisper of soft lilac #F5F0F7 across the bottom 15%. "
                   "IDENTICAL across all 3 options so the split test isolates composition, not colour.",
        purpose="Win the click. The SEO team's CTR note is blunt: the current main image is not "
                "attractive. Ship all 3, keep the winner via Amazon Manage Your Experiments.",
        visual=(
            "Mock ALL 3 options. Each: ONE callout, ONE supporting prop, product dominant. Colour stays "
            "TRUE to the real petals — do NOT over-saturate. Amazon's slot-1 main stays pure-white / "
            "product-only; these callout versions are the CTR mains you test against it.\n\n"

            "OPTION A — THE VOLUME SHOT (owns 'you get a lot')\n"
            "A clear glass measuring cup filled to the 1.5-cup line with the petal mix — rose, "
            "carnation, pansy and orchid petals visible as distinct colours — tipped so petals spill "
            "onto bright white. The pack stands behind. This is the single most useful image we can "
            "make, because 'package looks smaller than expected' is a live review theme and this "
            "answers it before the click.\n"
            "ONE CALLOUT (top-left badge, green bg / white text): 'ABOUT 1.5 CUPS'.\n\n"

            "OPTION B — THE PAYOFF (owns the outcome)\n"
            "A finished celebration cake with petals scattered across the top and drifting down one "
            "side onto the board — the confetti effect only loose petals can make. Shot slightly above "
            "on bright white, pack soft-focus behind.\n"
            "ONE CALLOUT (top-right badge, purple bg / white text): 'SCATTER. STYLE. DONE.'\n\n"

            "OPTION C — REAL PETALS, FOUR FLOWERS (owns 'real, not sprinkles')\n"
            "Overhead macro of the mix separated into four soft clusters — roses, carnations, pansies, "
            "orchids — each labelled with a hairline callout, petal veining clearly visible. Reads as "
            "botanical, not as a bag of craft confetti.\n"
            "ONE CALLOUT (top-right badge, green bg / white text): 'REAL EDIBLE PETALS'.\n\n"

            "Across all 3: product dominant, callout ~6% of frame, same lighting and colour temp."
        ),
        overlay="ABOUT 1.5 CUPS",
        overlay_sub="Real freeze-dried petals: rose, carnation, pansy and orchid. USA grown.",
        props=["glass measuring cup filled to 1.5 cups", "spilling petal mix", "finished petal-scattered cake",
               "four labelled petal clusters"],
        lighting="Bright high-key daylight, soft shadows, airy. Identical across all 3 for a clean split test.",
        why_it_works=(
            "Three triggers: A owns quantity (the category's biggest expectation gap), B owns the "
            "finished look, C owns authenticity. One idea, one prop, one badge each — legible at mobile "
            "thumbnail size, honest colour."
        ),
        ctr="A measured 1.5-cup shot is unique in a category of vague little bags — it earns the click "
            "on value before the shopper even reads the price.",
        cvr="Pre-answers the quantity objection, so the listing page starts from trust.",
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: real petals from four real flowers",
        role="hook",
        background="Soft lilac #F5F0F7 — fresh and elegant, never dark or moody",
        purpose="Prove these are genuine botanicals, not dyed craft confetti or sugar sprinkles.",
        visual=(
            "Extreme macro across a shallow drift of the mix, one rose petal and one pansy petal pulled "
            "into sharp focus so natural veining, translucency and the soft ruffled edge read clearly. "
            "Small 'FOOD-GRADE · EDIBLE' leaf check-mark badge beside them. Keep colour honest — the "
            "petals are naturally soft-toned, and over-saturating them is exactly the complaint the "
            "reviews already make."
        ),
        overlay="REAL PETALS. NOT SPRINKLES.",
        overlay_sub="Rose, carnation, pansy and orchid petals. Freeze-dried, food-grade, edible.",
        props=["macro petal drift", "food-grade / edible check-mark badge"],
        lighting="Soft directional daylight to reveal petal texture, veining and translucency.",
        why_it_works=(
            "In a thumbnail grid this product can be mistaken for dyed craft confetti or edible glitter. "
            "A true-colour macro showing veining settles the authenticity question instantly."
        ),
        ctr="Macro texture stops the scroll where flat product shots do not.",
        cvr="Removes the 'is this actually food?' hesitation before it reaches the reviews.",
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: four flowers in, every way to use them out",
        role="educate",
        background="White with a soft green ribbon footer",
        purpose="Show exactly what is in the mix and the range of uses — the CVR note asks for clear "
                "contents, usage and function.",
        visual=(
            "Left third: the open pack with petals spilling, small label 'Rose · Carnation · Pansy · "
            "Orchid petals — about 1.5 cups (0.2 oz)'. Right two-thirds: a clean 4-tile 'WAYS TO USE' "
            "grid, each tile a small real photo —\n"
            "  • SCATTER ON CAKES (petal confetti across buttercream and down one side)\n"
            "  • DRINKS & ICE (petals floating in a coupe / frozen into clear ice cubes)\n"
            "  • BOARDS & PLATING (petals drifted across charcuterie and a plated dessert)\n"
            "  • CHOCOLATE, COOKIES & RESIN (petals pressed into tempered chocolate and set in resin)\n"
            "Thin green connectors tie the pack to the four uses."
        ),
        overlay="ONE PACK. FOUR FLOWERS.",
        overlay_sub="Scatter on cakes · float in drinks · drift across boards · set into chocolate.",
        props=["open pack with spilling petals", "4 use-case tiles", "green connector lines"],
        lighting="Bright, even, editorial daylight. Educational clarity beats mood.",
        why_it_works=(
            "Loose petals are the most versatile format in the range but the least obvious to a first-time "
            "buyer. Four concrete uses turn 'pretty petals' into four reasons to buy."
        ),
        ctr="Grid layouts read as informative at thumbnail size and win the browse-stage click.",
        cvr="Answers 'what would I actually do with a cup and a half of petals?'",
    ),
    AIImagePlanItem(
        name="Image 4 — Desire: the scatter that finishes the table",
        role="desire",
        background="Styled bright celebration table, soft natural window light",
        purpose="Sell the dream outcome — a table that looks professionally styled.",
        visual=(
            "Hero lifestyle shot: hands mid-scatter, petals falling across a finished celebration cake, a "
            "few already landed on the linen and the board below. Two garnished coupes nearby, the edge "
            "of a grazing board in frame, the pack sitting naturally to the side. Light, fresh and "
            "aspirational — a food stylist's table. This is the 'action image' the CVR notes ask for: "
            "the motion of scattering is the product's entire promise."
        ),
        overlay="SCATTER. STYLE. DONE.",
        overlay_sub="A handful of petals turns a plain cake into the centrepiece.",
        props=["hands scattering petals", "finished cake", "2 garnished coupes", "grazing board edge",
               "styled linen table", "pack to the side"],
        lighting="Soft natural window light, bright and airy. Aspirational editorial styling — never dark.",
        why_it_works=(
            "Sells the outcome and the ease at once: no piping skill, no florist, one motion. The "
            "strongest CVR image in the set."
        ),
        ctr="Motion and finished food out-perform static ingredient shots in the mobile carousel.",
        cvr="Shows the effort level as well as the result — the buyer believes they can do this.",
    ),
    AIImagePlanItem(
        name="Image 5 — Trust: real, shelf-stable, natural, USA grown",
        role="trust",
        background="White with soft green panels behind each badge for separation",
        purpose="Stack the reassurances: real food, no additives, keeps, arrives protected.",
        visual=(
            "Centre: the resealable pack, clean and premium, a soft drift of petals beside it. Four "
            "badges in the corners:\n\n"
            "  • TOP-LEFT — REAL EDIBLE PETALS (leaf icon — food-grade, not artificial)\n"
            "  • TOP-RIGHT — SHELF-STABLE (calendar icon — ready for months, no wilting)\n"
            "  • BOTTOM-LEFT — NO ADDED SUGAR, SALT OR PRESERVATIVES\n"
            "  • BOTTOM-RIGHT — USA GROWN & FREEZE-DRIED (small US outline)\n\n"
            "Thin strip below, aimed at the 'damaged in shipping' reviews: 'Petals are light and "
            "delicate by nature — they travel cushioned in a resealable pack and stay protected between "
            "uses.'"
        ),
        overlay="SHELF-STABLE. STAYS PERFECT.",
        overlay_sub="Real · no added sugar, salt or preservatives · USA grown · resealable pack.",
        props=["resealable pack", "petal drift", "4 corner badges", "protective-packaging strip"],
        lighting="Bright studio-even light with a soft catch-light on the pack. Badges legible at thumbnail size.",
        why_it_works=(
            "The trust gaps here are 'is it real food?' and 'will it survive shipping?'. Stacking real + "
            "no additives + shelf-stable + USA-grown answers both before they become questions."
        ),
        ctr="Badge clusters read as credentials even when the text is too small to parse.",
        cvr="Neutralises the recurring 'arrived damaged' review theme pre-emptively.",
    ),
    AIImagePlanItem(
        name="Image 6 — Honest volume & coverage (about 1.5 cups)",
        role="desire",
        background="Soft lilac #F5F0F7 — same family as Image 2 for visual rhythm",
        purpose="Set honest quantity expectations — 'package looks smaller than expected' is a live "
                "review theme, and volume is this product's strongest answer.",
        visual=(
            "Split-frame.\n\n"
            "LEFT — HOW MUCH: the petals poured into a clear glass measuring cup, filled to the 1.5-cup "
            "line, shot straight on so the marking is readable. Beside it, the pack and a US quarter for "
            "petal scale. Caption: 'About 1.5 cups · 0.2 oz — petals are light, so weight looks small "
            "and volume looks generous.' That sentence defuses the whole complaint.\n\n"
            "RIGHT — HOW FAR IT GOES: three coverage examples photographed identically — one 8-inch cake "
            "top, six cupcakes, one grazing board — each showing the petals actually placed, with a small "
            "note on roughly how much of the pack each uses. Honest, not exaggerated.\n\n"
            "Footer strip — HANDLING: 'Delicate by nature — sprinkle by hand or place with tweezers, "
            "store sealed and dry.'"
        ),
        overlay="LIGHT PACK, GENEROUS CUP",
        overlay_sub="About 1.5 cups of petals. Light by weight, generous by volume.",
        props=["glass measuring cup at 1.5 cups", "pack + US quarter", "3 coverage examples", "tweezers"],
        lighting="Bright, even, honest daylight — show the true volume and the true colour.",
        why_it_works=(
            "Freeze-dried petals weigh almost nothing, so 0.2 oz sounds tiny while 1.5 cups looks "
            "generous. Showing both, measured, converts the listing's weakest number into its strongest "
            "picture and cuts the expectation-gap returns."
        ),
        ctr="A measuring cup is an unexpected, concrete image in a category of styled abstractions.",
        cvr="Directly closes the #1 expectation gap on this listing.",
    ),
    AIImagePlanItem(
        name="Image 7 — Close: find your flower (the variation family)",
        role="close",
        background="Bright white with a soft lilac band behind the family strip",
        purpose="Close on the brand and route the shopper to the right listing in the Freshly Preserved "
                "flower family — petals for coverage, whole blooms for focal points.",
        visual=(
            "Top two-thirds: brand-forward shot — the Freshly Preserved pack front and centre with a "
            "graceful drift of petals around it on bright white, one finished cupcake softly in frame. "
            "Lower band: logo + tagline 'Real blooms. Ready when you are.'\n\n"
            "Bottom third — THE FAMILY STRIP (the variation navigator). One clean row of small "
            "identical-composition photos, each captioned with its name and count:\n"
            f"  {' · '.join(FAMILY[:6])}\n"
            "THIS listing — Flower Petals, about 1.5 cups — is ringed in brand green with a small 'YOU "
            "ARE HERE' tag; the others sit un-ringed at 70% scale.\n"
            "Caption under the strip: 'Petals cover. Whole blooms are the focal point. Most people end "
            "up using both.'\n"
            f"Small line at the very bottom: 'Also in the range: {' · '.join(FAMILY[6:])}.'"
        ),
        overlay="FIND YOUR FLOWER.",
        overlay_sub="Petals to scatter, whole blooms to place. One family, every project.",
        props=["Freshly Preserved pack", "petal drift", "finished cupcake",
               "family strip with this listing ringed", "logo + tagline band"],
        lighting="Bright, airy, elegant daylight. Family strip evenly lit so the options compare fairly.",
        why_it_works=(
            "Petals and whole blooms solve different problems, and a shopper who wanted blooms will "
            "otherwise bounce. The strip converts a mismatch into a sideways sale and closes on brand "
            "identity rather than a feature."
        ),
        ctr="Showing a range signals a real brand rather than a one-off seller.",
        cvr="Recovers the wrong-format shopper inside the family, and seeds the second purchase.",
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Premium Full Image: brand banner",
        role="a+_banner",
        headline="REAL BLOOMS. READY WHEN YOU ARE.",
        body=(
            "Freshly Preserved Freeze-Dried Edible Flower Petals bring real botanical colour to cakes, "
            "desserts, drinks and boards — about 1.5 cups of rose, carnation, pansy and orchid petals, "
            "freeze-dried so they keep their natural colour and delicate texture. Grown and freeze-dried "
            "in the USA, with no added sugar, salt or preservatives, and ready the moment inspiration "
            "strikes."
        ),
        visual=("Wide, bright editorial banner — a styled table with a petal-scattered cake, a garnished "
                "coupe and the resealable pack, soft natural window light. Logo upper-left, tagline in "
                "the lower band. Desktop 1464x600, mobile 600x450 — keep cake and pack in the mobile "
                "safe area."),
        alt="Freshly Preserved freeze-dried edible flower petals scattered across a styled celebration table.",
    ),
    AIModule(
        name="Module 2 — Premium Carousel (5 tiles): why Freshly Preserved",
        role="a+_carousel",
        headline="WHY FRESHLY PRESERVED",
        body=(
            "Tile 1: <b>REAL, NOT ARTIFICIAL</b> — Genuine food-grade petals, never craft confetti.<br/>"
            "Tile 2: <b>ABOUT 1.5 CUPS</b> — Generous volume; light by weight, wide in coverage.<br/>"
            "Tile 3: <b>FOUR FLOWERS IN ONE</b> — Rose, carnation, pansy and orchid petals.<br/>"
            "Tile 4: <b>NEVER WILTS</b> — Shelf-stable; stock it weeks or months ahead.<br/>"
            "Tile 5: <b>USA GROWN · NOTHING ADDED</b> — No added sugar, salt or preservatives."
        ),
        visual=("5 square tiles at 220x220, purple accent corner on each, consistent bright styling. "
                "Icons: petal · measuring cup · four-flower cluster · calendar · US leaf. Alt text per tile."),
        alt="Five-tile A+ carousel: real petals, about 1.5 cups, four flowers, shelf-stable, USA grown.",
    ),
    AIModule(
        name="Module 3 — Premium Full Image: ways to use them",
        role="a+_banner",
        headline="ONE PACK. EVERY OCCASION.",
        body=(
            "Scatter across cakes, cupcakes and cookies for a confetti finish no piping bag can make. "
            "Float petals in cocktails and mocktails, or freeze them into clear ice. Drift them over "
            "charcuterie and grazing boards, plated desserts and salads. Press them into tempered "
            "chocolate, fold them through sugar, or set them in resin for craft projects. Loose petals "
            "are the format that covers ground — a handful finishes a whole table."
        ),
        visual=("Wide 4-panel banner: CAKE SCATTER → DRINKS & ICE → BOARDS & PLATING → CHOCOLATE & "
                "RESIN. Bright, editorial, thin purple dividers. Mobile keeps 2 panels stacked."),
        alt="A+ banner showing four ways to use Freshly Preserved edible flower petals.",
    ),
    AIModule(
        name="Module 4 — Premium Full Image: fresh flowers wilt, these don't",
        role="a+_banner",
        headline="FRESH FLOWERS WILT. THESE DON'T.",
        body=(
            "Fresh edible flowers are seasonal, fragile and spoil within days — they brown, curl and "
            "lose their colour right when you need them. These petals are freeze-dried and shelf-stable, "
            "so they hold their natural colour and delicate texture until your event. Stock the pack "
            "ahead, skip the last-minute florist run, and waste nothing."
        ),
        visual=("Wide banner split in two: LEFT — fresh petals visibly browning and curling, muted. "
                "RIGHT — Freshly Preserved petals, bright and intact, beside the resealable pack. Clean "
                "centre divider, bright background. Never a dark or moody treatment."),
        alt="A+ banner comparing wilting fresh petals with shelf-stable Freshly Preserved edible petals.",
    ),
    AIModule(
        name="Module 5 — Premium Carousel (5 tiles): choose your variation",
        role="a+_carousel",
        headline="FIND YOUR FLOWER",
        body=(
            "<b>You are viewing: Flower Petals — about 1.5 cups (0.2 oz).</b> Petals cover ground; whole "
            "blooms are the focal point. Same real, freeze-dried, food-grade flowers in every "
            "variation — pick the format your project needs.<br/><br/>"
            "Tile 1: <b>Flower Petals · about 1.5 cups</b> — Scatter, confetti, full-surface coverage.<br/>"
            "Tile 2: <b>Small Pansy · 12 whole blooms</b> — Flat, bright faces for cupcakes and cookies.<br/>"
            "Tile 3: <b>Small Orchid · 12 whole blooms</b> — Sculptural blooms for drinks and cake tiers.<br/>"
            "Tile 4: <b>Small Roses &amp; Mixed · about 12 rose blooms</b> — Romantic blooms plus petals.<br/>"
            "Tile 5: <b>Squash Blossoms · 12 whole blooms</b> — Large blossoms for savoury plating.<br/><br/>"
            "Also in the Freshly Preserved range: Pansy and Pansy &amp; Orchid 25-bloom packs · Purple "
            "Orchids · Marigolds · Small Mini Carnations &amp; Bachelors · Basil Blossoms · the Fall Cake "
            "Decorating Kit."
        ),
        visual=("5 identical-composition variation tiles at 220x220 — same white background, same "
                "lighting, same camera height, so formats compare honestly. THIS variation (Flower "
                "Petals) carries a green ring and a small 'YOU ARE HERE' tag. Per-tile alt text names "
                "the variation and its count."),
        alt="Five-tile A+ carousel of the Freshly Preserved edible flower range with the petal mix marked.",
    ),
    AIModule(
        name="Module 6 — Premium Full Image: from the brand (benefits closer)",
        role="a+_banner",
        headline="FROM FRESHLY PRESERVED",
        body=(
            "We grow and freeze-dry our flowers in the USA, so the petal that leaves us is the petal "
            "that lands on your cake — natural colour, delicate texture, months later. No added sugar, "
            "no salt, no preservatives, no dyes, and nothing artificial pretending to be a flower. This "
            "pack holds <b>about 1.5 cups of rose, carnation, pansy and orchid petals (0.2 oz)</b> in a "
            "resealable pack that keeps them protected between projects. Small kitchens, big possibilities."
        ),
        visual=("Warm benefits/brand closer: soft-focus USA growing field or freeze-drying trays on the "
                "left, the resealable pack and a petal-scattered dessert on the right, brand-voice line "
                "across the middle. Bright and airy — never dark behind the logo."),
        alt="Freshly Preserved brand closing banner: USA grown, freeze-dried, nothing added.",
    ),
    AIModule(
        name="Module 7 — Premium Q&A (finale)",
        role="a+_qa",
        headline="QUESTIONS BEFORE YOU BUY",
        body=(
            "<b>Q.</b> How much do I actually get?<br/>"
            "<b>A.</b> About 1.5 cups of petals, which is 0.2 oz by weight. Freeze-dried petals are "
            "extremely light, so the weight sounds small while the volume is generous — the size image "
            "shows the petals measured in a glass cup.<br/><br/>"

            "<b>Q.</b> Are these real flowers, and are they edible?<br/>"
            "<b>A.</b> Yes. Real, food-grade petals from roses, carnations, pansies and orchids, "
            "freeze-dried — not craft confetti, not artificial decoration.<br/><br/>"

            "<b>Q.</b> Whole blooms or petals — which should I choose?<br/>"
            "<b>A.</b> Petals cover ground: scatter them across a cake top, a board or a plate. Whole "
            "blooms are focal points you place one at a time. Many customers keep both.<br/><br/>"

            "<b>Q.</b> How long do they last, and how should I store them?<br/>"
            "<b>A.</b> They are shelf-stable and will not wilt like fresh flowers. Keep them sealed, "
            "away from moisture and direct sunlight, and use them whenever you need them.<br/><br/>"

            "<b>Q.</b> Will the colour match the photos?<br/>"
            "<b>A.</b> We keep our images honest to the real petal. Freeze-drying preserves the natural "
            "colour, though shades vary between flowers because these are real botanicals.<br/><br/>"

            "<b>Q.</b> Do they taste of anything?<br/>"
            "<b>A.</b> They are mild. Petals are used mainly for natural colour and presentation rather "
            "than for strong flavour, with no added sugar or salt.<br/><br/>"

            "<b>Q.</b> Can I use them for resin and craft projects?<br/>"
            "<b>A.</b> Yes. The petals keep their shape and colour when set in clear resin, which makes "
            "them popular for coasters, jewellery and DIY projects as well as food."
        ),
        visual=("Vertical Q/A table, text only. Purple divider lines between questions, small green Q. "
                "and purple A. labels. Mobile-first line lengths."),
        alt="Premium Q&A module answering the most-asked questions about Freshly Preserved edible flower petals.",
    ),
]


# House standard: exactly 5 pairs, question ≤80 chars, answer ≤120. Cut from nine — the
# five kept are the ones that actually block the purchase (quantity, authenticity, damage
# in transit, colour honesty, origin). Taste and use-cases are already covered in bullets.
QA = [
    AIQA(q="How much do I actually get?",
         a="About 1.5 cups of petals, 0.2 oz. They weigh almost nothing, so the volume is "
           "generous."),
    AIQA(q="Are these real flowers, and are they edible?",
         a="Yes. Food-grade petals from roses, carnations, pansies and orchids. Not craft "
           "confetti."),
    AIQA(q="Will they arrive damaged?",
         a="They travel cushioned in a resealable pack. Some settling is normal and does not "
           "affect loose petals."),
    AIQA(q="Will the colour match the photos?",
         a="Our images stay honest to the real petal. Shades vary slightly because these are "
           "real botanicals."),
    AIQA(q="Where are they grown?",
         a="USA-grown flowers, freeze-dried in the USA. No added sugar, salt or "
           "preservatives."),
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
