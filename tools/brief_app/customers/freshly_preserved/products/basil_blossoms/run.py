"""Freshly Preserved — Product 05 · Freeze-Dried BASIL BLOSSOMS 0.2 oz (about 25 sprigs).

ASIN: B0H9ZFBXSF · Marketplace: amazon.com (USA) — English overlays + customer copy.
(The Overview tab also carries an older ASIN, B0CR6XHZG7 — the SEO deliverable is filed under
B0H9ZFBXSF, so that is the ASIN used here.)

WHAT MAKES THIS ONE DIFFERENT — and it is the biggest gap in the whole range:
this is the SAVOURY variation. Every other listing sells beauty on a cake; this one sells
FLAVOUR in a pan. Basil blossoms are an aromatic herb first and a garnish second — seasoning
blends, meat rubs, marinades, sauces, pasta, salads, tea infusions, gin and tomato-forward
cocktails. The buyer is a cook or a chef, not a cake decorator, and the creative has to reach
them: the hero belongs in a kitchen, not on a dessert table.

The second gap it fills: basil BOLTS. Once it flowers the leaves turn bitter and home
gardeners lose the plant — so fresh basil blossoms are a two-week window nobody can shop for.
Shelf-stable blossoms mean the flavour is available in February.

TITLE + BULLETS come 1:1 from the SEO tab (the keyword axis). Overlays / A+ / Q&A are
hand-written. Parent-child is built in at Image 7 and A+ Module 5.

Compliance guardrails (US): no best / #1 / guaranteed · NO health or wellness claims (this is
a herb — do not stray into "digestion", "immunity", "anti-inflammatory"; describe flavour,
aroma and use only) · no organic claim (the source sheet states it is NOT certified organic)
· no prices or URLs on-image.
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
PLAN_NO = "05"
ASIN = "B0H9ZFBXSF"

FAMILY = [
    "Basil Blossoms · about 25 sprigs (this listing)",
    "Squash Blossoms · 12 whole blooms",
    "Flower Petals · about 1.5 cups",
    "Small Roses & Mixed · about 12 rose blooms",
    "Small Pansy · 12 whole blooms",
    "Pansy & Orchids · 25 whole blooms",
    "Purple Orchids · 25 whole blooms",
    "Marigolds",
    "Small Mini Carnations & Bachelors",
    "Fall Cake Decorating Kit · 25+ flowers & leaves",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="Clean bright white with a whisper of soft sage-green across the bottom 15% — the "
                   "savoury member of the brand's light background family. IDENTICAL across all 3.",
        purpose="Win the click from a COOK, not a cake decorator. The SEO team's CTR note is blunt: the "
                "current main image is not attractive. Ship all 3 and keep the winner.",
        visual=(
            "Mock ALL 3 options. Each: ONE callout, ONE supporting prop, product dominant. Colour stays "
            "TRUE — basil blossoms freeze-dry to soft white-and-green sprigs, not vivid herb green, and "
            "over-saturating is exactly the complaint the reviews already make. Amazon's slot-1 main "
            "stays pure-white / product-only; these callout versions are the CTR mains you test.\n\n"

            "OPTION A — THE SPRIG COUNT (owns 'real herb, and this much')\n"
            "The basil blossom sprigs laid out on bright white in a loose fan, one sprig pulled forward "
            "in crisp macro so the tiny white florets and the square basil stem read clearly. Open pack "
            "tipped in behind, a small pinch bowl of crumbled blossom in front.\n"
            "ONE CALLOUT (top-left badge, green bg / white text): 'ABOUT 25 SPRIGS'.\n"
            "Why it wins: it reads immediately as a real culinary herb rather than a decorative flower.\n\n"

            "OPTION B — IN THE PAN (owns the savoury use — the option to beat)\n"
            "A finished savoury plate: blossoms scattered over burrata and tomato, or crumbled across a "
            "seared steak, with a bowl of the blossoms alongside. Bright kitchen surface, not a dessert "
            "table. This is the shot that tells a cook the product is for them.\n"
            "ONE CALLOUT (top-right badge, sage bg / white text): 'SEASON. RUB. GARNISH.'\n"
            "Why it wins: every competing edible-flower thumbnail shows a cake. A savoury plate owns a "
            "search intent nobody else is answering.\n\n"

            "OPTION C — BASIL, IN BLOOM (owns the rarity)\n"
            "Split: LEFT a fresh basil plant that has bolted, flowers open and leaves visibly past their "
            "best; RIGHT the preserved blossoms, intact and ready in the pack. Thin divider.\n"
            "ONE CALLOUT (top-right badge, green bg / white text): 'IN SEASON, ALL YEAR'.\n"
            "Why it wins: anyone who grows basil knows the two-week flowering window — and knows you "
            "cannot buy blossoms at the store.\n\n"

            "Across all 3: product dominant, callout ~6% of frame, same lighting and colour temp."
        ),
        overlay="ABOUT 25 SPRIGS",
        overlay_sub="Real freeze-dried basil blossoms. Aromatic, savoury, ready all year.",
        props=["fan of basil blossom sprigs", "macro of one sprig", "pinch bowl of crumbled blossom",
               "savoury plate with burrata and tomato", "bolted basil plant vs preserved sprigs"],
        lighting="Bright high-key daylight, soft shadows, airy. Identical across all 3 for a clean split test.",
        why_it_works=(
            "Three triggers: A owns quantity and authenticity, B claims the savoury cook nobody else in "
            "this category is talking to, C owns the seasonal rarity. One idea, one prop, one badge each."
        ),
        ctr="A savoury plate in a category of cakes is genuinely differentiated at thumbnail size.",
        cvr="Sets the right expectation from the first frame — this is a flavour ingredient, not decor.",
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: an aromatic herb, not just a garnish",
        role="hook",
        background="Soft sage wash on white — fresh and culinary, never dark or moody",
        purpose="Reposition the product in one frame: flavour and aroma first, beauty second.",
        visual=(
            "Split composition. LEFT: extreme macro of one basil blossom sprig, lit so the tiny white "
            "florets, the fine stem and the papery bracts read clearly — unmistakably a real herb. "
            "RIGHT: the same blossom crumbled between finger and thumb over a warm dish, with a soft "
            "hint of steam and a scattering of crumb already landed. A small 'FOOD-GRADE · EDIBLE' leaf "
            "check-mark badge sits between the two halves.\n"
            "The two halves together carry the whole positioning: whole for garnish, crumbled for "
            "flavour."
        ),
        overlay="WHOLE OR CRUMBLED.",
        overlay_sub="Garnish with the sprig or crumble it into the pan. Savoury basil either way.",
        props=["macro basil blossom sprig", "fingers crumbling a sprig over a warm dish",
               "food-grade / edible check-mark badge"],
        lighting="Soft directional daylight to reveal floret and stem texture; gentle warmth on the pan side.",
        why_it_works=(
            "The single biggest miss on this listing would be reading as decoration. Showing the "
            "crumble-into-the-pan gesture reframes it as a pantry herb, which doubles the occasions and "
            "justifies repurchase."
        ),
        ctr="The crumbling gesture is motion and intent — it stops the scroll where a flat sprig would not.",
        cvr="Answers 'is this actually food, or just pretty?' in the first two seconds.",
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: six ways a cook actually uses them",
        role="educate",
        background="White with a soft sage ribbon footer",
        purpose="Show the range of savoury uses — the CVR note asks for clear contents, usage and function.",
        visual=(
            "Left third: the open pack with the sprigs neatly grouped, small label 'About 25 basil "
            "blossom sprigs · 0.2 oz'. Right two-thirds: a clean 6-tile 'WAYS TO USE' grid, each tile a "
            "small real photo —\n"
            "  • SEASONING BLENDS (blossoms crumbled into a jar of dry mix)\n"
            "  • MEAT RUBS & MARINADES (pressed onto a steak or chicken before the pan)\n"
            "  • SAUCE & PASTA (scattered over tomato sauce and fresh pasta)\n"
            "  • SALAD & CHARCUTERIE (whole sprigs across burrata, tomato and a board)\n"
            "  • TEA & INFUSIONS (sprigs in a clear glass teapot)\n"
            "  • COCKTAILS (a sprig laid across a gin or tomato-forward drink)\n"
            "Thin sage connectors tie the pack to the six uses."
        ),
        overlay="ONE JAR. SIX USES.",
        overlay_sub="Rubs, marinades, sauces, salads, tea, cocktails. Savoury basil, ready.",
        props=["open pack of sprigs", "6 use-case tiles", "sage connector lines"],
        lighting="Bright, even, editorial daylight. Educational clarity beats mood.",
        why_it_works=(
            "A cook buys an ingredient when they can name three dishes for it. Six concrete uses — most "
            "of them savoury — turn a curiosity purchase into a pantry staple."
        ),
        ctr="A six-tile grid reads as substantial and informative at thumbnail size.",
        cvr="Multiplies the perceived occasions, which is what justifies the price on a small pack.",
    ),
    AIImagePlanItem(
        name="Image 4 — Desire: the plate that looks restaurant-made",
        role="desire",
        background="Bright kitchen or dining surface, soft natural window light",
        purpose="Sell the dream outcome — a home plate that looks like it came from a restaurant pass.",
        visual=(
            "Hero lifestyle shot, deliberately SAVOURY: a burrata, heirloom tomato and olive-oil plate "
            "finished with whole basil blossom sprigs, hands mid-placement with tweezers or fingers. In "
            "soft focus behind: a bowl of fresh pasta also finished with blossoms, and a gin cocktail "
            "with a sprig across the rim. Bright linen, a good knife, the pack sitting naturally to the "
            "side. This is the 'action image' the CVR notes ask for — and it must not look like a "
            "dessert table."
        ),
        overlay="PLATED LIKE A PRO.",
        overlay_sub="The finishing touch that makes a home plate look restaurant-made.",
        props=["burrata + heirloom tomato plate", "hands placing a sprig", "bowl of pasta",
               "gin cocktail with a sprig", "bright linen", "pack to the side"],
        lighting="Soft natural window light, bright and airy. Aspirational editorial food styling — never dark.",
        why_it_works=(
            "The emotional payoff for a home cook is the moment a plate looks professional. Showing the "
            "gesture and the result together makes that feel one sprig away."
        ),
        ctr="Restaurant-grade savoury plating is rare in this category's carousel and pulls the click.",
        cvr="Transfers the result onto the buyer's own cooking — the emotional close.",
    ),
    AIImagePlanItem(
        name="Image 5 — Trust: real, shelf-stable, natural, made in USA",
        role="trust",
        background="White with soft sage panels behind each badge for separation",
        purpose="Stack the reassurances: real food-grade herb, nothing added, keeps, arrives protected.",
        visual=(
            "Centre: the resealable pack, clean and premium, a few whole sprigs and a small pinch of "
            "crumbled blossom beside it. Four badges in the corners:\n\n"
            "  • TOP-LEFT — REAL EDIBLE BLOSSOMS (leaf icon — food-grade, not artificial)\n"
            "  • TOP-RIGHT — SHELF-STABLE (calendar icon — the flavour keeps, no refrigeration)\n"
            "  • BOTTOM-LEFT — NO ADDED SALT, SUGAR OR PRESERVATIVES\n"
            "  • BOTTOM-RIGHT — MADE IN USA (small US outline)\n\n"
            "Thin strip below: 'Freeze-dried to hold the aroma and colour of basil in bloom — store "
            "sealed and dry, no refrigeration needed.'\n"
            "IMPORTANT: no health, wellness or medicinal language anywhere on this frame. Flavour, aroma "
            "and use only. Do not imply organic certification."
        ),
        overlay="AROMA THAT KEEPS.",
        overlay_sub="Real · no added salt or sugar · made in USA · sealed, no refrigeration.",
        props=["resealable pack", "whole sprigs", "pinch of crumbled blossom", "4 corner badges"],
        lighting="Bright studio-even light with a soft catch-light on the pack. Badges legible at thumbnail size.",
        why_it_works=(
            "For a herb, the buying question is 'will it still taste of anything?' Leading the trust "
            "frame with aroma rather than looks answers the doubt that actually blocks this purchase."
        ),
        ctr="Badge clusters read as credentials even when the text is too small to parse.",
        cvr="Answers the flavour-retention doubt that is unique to the savoury listing.",
    ),
    AIImagePlanItem(
        name="Image 6 — Honest size & count (about 25 sprigs · 0.2 oz)",
        role="desire",
        background="Soft sage wash on white — same family as Image 2 for visual rhythm",
        purpose="Set honest size and quantity expectations — 'package size appears limited' is a named "
                "review theme on this listing.",
        visual=(
            "Split-frame.\n\n"
            "LEFT — SCALE, HONESTLY: one blossom sprig held between finger and thumb, and the same sprig "
            "beside a US quarter. Caption: 'Small, fine sprigs — a little carries a lot of aroma.'\n\n"
            "RIGHT — WHAT 25 LOOKS LIKE: all the sprigs laid out in a neat flat-lay grid beside the "
            "pack, plus a small teaspoon of crumbled blossom to show what one sprig yields when "
            "crumbled. Label: 'About 25 sprigs · 0.2 oz'. Do not art-direct this into looking like more "
            "than it is — an honest count picture is what stops the expectation-gap return.\n\n"
            "Footer strip — HANDLING: 'Delicate by nature — use whole as a garnish, or crumble between "
            "your fingers into the pan. Store sealed and dry.'"
        ),
        overlay="SMALL SPRIG, BIG AROMA",
        overlay_sub="About 25 sprigs. Use whole to garnish, crumble to season.",
        props=["sprig held in fingers", "sprig beside a US quarter", "flat-lay of all sprigs",
               "teaspoon of crumbled blossom"],
        lighting="Bright, even, honest daylight — show the true size and the true colour.",
        why_it_works=(
            "Freeze-dried herbs weigh almost nothing, so 0.2 oz reads as tiny until you see the count and "
            "what a single sprig yields crumbled. Showing both closes the expectation gap that drives "
            "this listing's 3-star reviews."
        ),
        ctr="Coin-scale and teaspoon-yield shots are concrete where the category is vague.",
        cvr="Reframes 'small pack' as 'concentrated', which is how cooks think about dried herbs.",
    ),
    AIImagePlanItem(
        name="Image 7 — Close: find your flower (the variation family)",
        role="close",
        background="Bright white with a soft sage band behind the family strip",
        purpose="Close on the brand and route the shopper across the family — this is the savoury door "
                "into a mostly sweet range.",
        visual=(
            "Top two-thirds: brand-forward shot — the Freshly Preserved pack front and centre with basil "
            "blossom sprigs scattered around it on bright white, the burrata plate softly in frame. "
            "Lower band: logo + tagline 'Real blooms. Ready when you are.'\n\n"
            "Bottom third — THE FAMILY STRIP (the variation navigator). One clean row of small "
            "identical-composition photos, each captioned with its name and count:\n"
            f"  {' · '.join(FAMILY[:6])}\n"
            "THIS listing — Basil Blossoms — is ringed in brand green with a small 'YOU ARE HERE' tag; "
            "the others sit un-ringed at 70% scale.\n"
            "Caption under the strip: 'Basil and squash blossoms cook. Pansies, orchids and roses "
            "decorate. Same freeze-drying, different job.'\n"
            f"Small line at the very bottom: 'Also in the range: {' · '.join(FAMILY[6:])}.'"
        ),
        overlay="FIND YOUR FLOWER.",
        overlay_sub="Savoury blossoms to cook with, sweet blooms to decorate. One family.",
        props=["Freshly Preserved pack", "basil blossom sprigs", "burrata plate",
               "family strip with this listing ringed", "logo + tagline band"],
        lighting="Bright, airy, elegant daylight. Family strip evenly lit so the variations compare fairly.",
        why_it_works=(
            "Basil brings in a cook who did not know the brand made anything else. Splitting the family "
            "into 'cook with' and 'decorate with' gives that shopper an instant second reason to return."
        ),
        ctr="Showing a range signals a real brand rather than a one-off seller.",
        cvr="Opens a whole second category to a buyer who arrived for one herb.",
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Premium Full Image: brand banner",
        role="a+_banner",
        headline="BASIL, CAUGHT IN BLOOM.",
        body=(
            "Basil only flowers for a couple of weeks, and you cannot buy the blossoms at a store. "
            "Freshly Preserved Freeze-Dried Basil Blossoms capture about 25 sprigs at exactly that "
            "moment — aromatic, savoury and shelf-stable, so the flavour is there in February as well "
            "as August. Use them whole as a garnish or crumble them into rubs, marinades, sauces and "
            "tea. Made in the USA, with no added salt, sugar or preservatives."
        ),
        visual=("Wide, bright editorial banner — a kitchen surface, not a dessert table: a burrata and "
                "tomato plate finished with blossoms, a bowl of pasta, the resealable pack, soft natural "
                "window light. Logo upper-left, tagline in the lower band. Desktop 1464x600, mobile "
                "600x450 — keep the plate and pack in the mobile safe area."),
        alt="Freshly Preserved freeze-dried basil blossoms on a savoury burrata and tomato plate.",
    ),
    AIModule(
        name="Module 2 — Premium Carousel (5 tiles): why basil blossoms",
        role="a+_carousel",
        headline="WHY BASIL BLOSSOMS",
        body=(
            "Tile 1: <b>SAVOURY, NOT SWEET</b> — A real culinary herb: rubs, sauces, salads, pasta.<br/>"
            "Tile 2: <b>WHOLE OR CRUMBLED</b> — Garnish with the sprig, crumble it in for flavour.<br/>"
            "Tile 3: <b>A TWO-WEEK WINDOW, KEPT</b> — Basil blossoms are seasonal; these are not.<br/>"
            "Tile 4: <b>AROMA HELD IN</b> — Freeze-dried to hold the colour and the basil aroma.<br/>"
            "Tile 5: <b>MADE IN USA · NOTHING ADDED</b> — No added salt, sugar or preservatives."
        ),
        visual=("5 square tiles at 220x220, sage accent corner on each, consistent bright styling. "
                "Icons: pan · sprig+pinch pair · calendar · aroma swirl · US leaf. Alt text per tile."),
        alt="Five-tile A+ carousel: savoury herb, whole or crumbled, seasonal window kept, aroma, USA made.",
    ),
    AIModule(
        name="Module 3 — Premium Full Image: ways to use them",
        role="a+_banner",
        headline="ONE JAR. SIX USES.",
        body=(
            "Crumble the blossoms into seasoning blends, meat rubs and marinades. Scatter them over "
            "tomato sauce, fresh pasta, pizza and roasted vegetables. Finish burrata, heirloom tomato "
            "salads and charcuterie boards with whole sprigs. Steep them for a herbal tea infusion. Lay "
            "one across a gin or tomato-forward cocktail. Whole for presentation, crumbled for flavour — "
            "one jar covers both."
        ),
        visual=("Wide 6-panel banner: RUBS & MARINADES → SAUCE & PASTA → SALAD & BURRATA → CHARCUTERIE "
                "→ TEA → COCKTAIL. Bright, editorial, thin sage dividers. Mobile version keeps 3 panels "
                "stacked with the two savoury-cooking panels first."),
        alt="A+ banner showing six ways to use Freshly Preserved freeze-dried basil blossoms.",
    ),
    AIModule(
        name="Module 4 — Premium Full Image: fresh basil bolts, these don't",
        role="a+_banner",
        headline="BASIL BOLTS. THESE DON'T.",
        body=(
            "Once a basil plant flowers, the window is short and the leaves turn — which is why fresh "
            "basil blossoms almost never reach a shop. Freeze-drying catches the blossoms at their peak "
            "and holds their colour and aroma, sealed and shelf-stable, with no refrigeration. Reach for "
            "them in the middle of winter and get the same savoury, floral basil note you would have "
            "picked in August."
        ),
        visual=("Wide banner split in two: LEFT — a bolted basil plant, flowers open, leaves visibly "
                "past their best. RIGHT — the preserved blossoms, intact and pale-green, beside the "
                "sealed pack with a small calendar graphic. Clean centre divider, bright background."),
        alt="A+ banner comparing a bolted fresh basil plant with shelf-stable freeze-dried basil blossoms.",
    ),
    AIModule(
        name="Module 5 — Premium Carousel (5 tiles): choose your variation",
        role="a+_carousel",
        headline="FIND YOUR FLOWER",
        body=(
            "<b>You are viewing: Basil Blossoms — about 25 sprigs (0.2 oz).</b> Some blooms in this "
            "family are for cooking, some are for decorating. Same freeze-drying, different job — pick "
            "the one your recipe needs.<br/><br/>"
            "Tile 1: <b>Basil Blossoms · about 25 sprigs</b> — Savoury herb: rubs, sauces, salads, tea.<br/>"
            "Tile 2: <b>Squash Blossoms · 12 whole blooms</b> — Large savoury blossoms for plating.<br/>"
            "Tile 3: <b>Flower Petals · about 1.5 cups</b> — Colour to scatter across cakes and boards.<br/>"
            "Tile 4: <b>Small Roses &amp; Mixed · about 12 blooms</b> — Romance for cakes and drinks.<br/>"
            "Tile 5: <b>Small Pansy · 12 whole blooms</b> — Bright, flat faces for cupcakes.<br/><br/>"
            "Also in the Freshly Preserved range: Small Orchid · Pansy &amp; Orchids · Purple Orchids · "
            "Marigolds · Small Mini Carnations &amp; Bachelors · the Fall Cake Decorating Kit."
        ),
        visual=("5 identical-composition variation tiles at 220x220 — same white background, lighting "
                "and camera height. THIS variation (Basil Blossoms) carries a green ring and a small "
                "'YOU ARE HERE' tag. Per-tile alt text names the variation and its use."),
        alt="Five-tile A+ carousel of the Freshly Preserved range with the basil blossoms marked.",
    ),
    AIModule(
        name="Module 6 — Premium Full Image: from the brand (benefits closer)",
        role="a+_banner",
        headline="FROM FRESHLY PRESERVED",
        body=(
            "We freeze-dry our blossoms whole, in the USA, at the moment the plant flowers — so the "
            "sprig that leaves us still carries the colour and the savoury basil aroma months later. No "
            "added salt, no sugar, no preservatives, no dyes. This pack holds <b>about 25 basil blossom "
            "sprigs (0.2 oz)</b> in a resealable pack that needs no refrigeration and keeps them "
            "protected between meals. Small kitchens, big possibilities."
        ),
        visual=("Warm benefits/brand closer: soft-focus basil field or freeze-drying trays on the left, "
                "the resealable pack and a finished savoury plate on the right, brand-voice line across "
                "the middle. Bright and airy — never dark behind the logo."),
        alt="Freshly Preserved brand closing banner: basil blossoms freeze-dried whole in the USA.",
    ),
    AIModule(
        name="Module 7 — Premium Q&A (finale)",
        role="a+_qa",
        headline="QUESTIONS BEFORE YOU BUY",
        body=(
            "<b>Q.</b> What do they taste like?<br/>"
            "<b>A.</b> Like basil, with a lighter, more floral edge than the leaf — savoury and "
            "aromatic. Whole sprigs are subtle as a garnish; crumbled, the flavour comes forward.<br/><br/>"

            "<b>Q.</b> What do I actually cook with them?<br/>"
            "<b>A.</b> Seasoning blends, meat rubs and marinades; tomato sauces, pasta, pizza and "
            "roasted vegetables; burrata and salads; charcuterie boards; herbal tea infusions; and gin "
            "or tomato-forward cocktails.<br/><br/>"

            "<b>Q.</b> How many sprigs do I get?<br/>"
            "<b>A.</b> About 25 sprigs, 0.2 oz. Freeze-dried herbs are extremely light, so the weight "
            "sounds small — the size image shows all the sprigs laid out and what one yields "
            "crumbled.<br/><br/>"

            "<b>Q.</b> Can I use them in tea?<br/>"
            "<b>A.</b> Yes. They are food-grade edible basil blossoms and can be steeped for a herbal "
            "infusion, used in cooking, or used as a garnish.<br/><br/>"

            "<b>Q.</b> Are they organic?<br/>"
            "<b>A.</b> They are food-grade, freeze-dried edible basil blossoms made in the USA. This "
            "listing does not carry an organic certification.<br/><br/>"

            "<b>Q.</b> How should I store them, and do they need refrigeration?<br/>"
            "<b>A.</b> No refrigeration needed. Keep them sealed in the pack, away from moisture, heat "
            "and direct sunlight, and they stay ready whenever you cook.<br/><br/>"

            "<b>Q.</b> Will they arrive intact?<br/>"
            "<b>A.</b> Freeze-dried blossoms are naturally light and delicate, so they travel cushioned "
            "in a resealable pack. Sprigs that break up are still perfect — much of the time you will be "
            "crumbling them anyway."
        ),
        visual=("Vertical Q/A table, text only. Sage divider lines between questions, small green Q. and "
                "sage A. labels. Mobile-first line lengths."),
        alt="Premium Q&A module answering the most-asked questions about freeze-dried basil blossoms.",
    ),
]


# House standard: exactly 5 pairs, question ≤80 chars, answer ≤120. Cut from nine to what
# actually blocks the cook: taste, quantity, why not just dried leaf, storage, and the
# organic question (answered honestly, since the listing carries no certification).
QA = [
    AIQA(q="What do they taste like?",
         a="Like basil, lighter and more floral than the leaf. Crumble them and the flavour "
           "comes forward."),
    AIQA(q="How many sprigs do I get?",
         a="About 25 sprigs, 0.2 oz. Freeze-dried herbs weigh almost nothing."),
    AIQA(q="Why not just use dried basil leaf?",
         a="The blossom is a different ingredient. Lighter, more floral, and recognisable "
           "whole on the plate."),
    AIQA(q="Are they organic?",
         a="They are food-grade and made in the USA. This listing does not carry an organic "
           "certification."),
    AIQA(q="Do they need refrigeration?",
         a="No. Keep them sealed, away from moisture, heat and direct sunlight."),
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
