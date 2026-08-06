"""Mountain Crest Gardens — Assorted Succulents BULK (choose 25/50/100) — Image Plan 04
Hand-written senior copy injected into the branded EQUALICE ReportLab pipeline.

Marketplace: amazon.com (US). Customer text + art direction both ENGLISH.

THIS PACK'S IDENTITY (the #1 job — make it crystal clear which pack this is):
  • ASSORTED SUCCULENTS BULK — the BIGGEST variety + SCALABLE quantity pack.
  • CHOOSE YOUR COUNT — 25, 50, or 100 live plants in one box.
  • 10 DIFFERENT VARIETIES, 5 OF EACH — a rich mix, not multiples of one type.
  • MIXED GENERA — Echeveria, Sedum, Sempervivum, Crassula and more
    (rosette, upright and trailing forms).
  • MIXED HARDINESS — bright indoor light or partial outdoor sun.
  • Fully rooted in individual 2-inch nursery pots.
  For: bulk projects, events, weddings, walls, favors, centerpieces, resale.

THE DISAMBIGUATION (client mandate): a dedicated "WHICH PACK IS RIGHT FOR YOU?"
comparison positions THIS pack vs the siblings. The single most important contrast:
this is the MOST-variety + PICK-YOUR-QUANTITY pack (10 kinds, choose 25/50/100,
mixed genera) — vs the single-type bulks (05 Sempervivum / 06 Echeveria / 07 Cactus)
which are ONE plant type only. Disambiguating badges live on the creative:
"PICK 25 50 100", "10 VARIETIES 5 EACH", "BIGGEST MIX".

ELEVATED COPY (4 levers): VoC from real reviews (healthy plants, great value,
loved the mixed assortment; defuse 'smaller than expected' + arrival condition by
stating 2-inch pot size honestly and foregrounding rooted, packed-for-live-arrival);
dream-outcome-first (one box covers a whole project / event with a rich mix);
plainspoken nursery power-words (no hype); weave KW naturally (bulk succulents,
assorted succulents, succulents for wedding favors, live succulents, 2 inch succulents).

LANGUAGE: all art-direction fields (purpose, background, visual, props, lighting,
why_it_works, ctr, cvr, module visual) are designer-facing English. All customer
text (title, bullets, overlays, module headline/body, Q&A) is English too (US).

OVERLAY RULE: sell the OUTCOME / identity, not the action. Each overlay distinct,
≤30 chars AND ≤5 words, SMOOTH (no "Word? Word." fragments, no "·" middots).
overlay_sub ≤90 · module headline ≤38 · bullet head ≤45.

Verified facts (from listing.xlsx USPs + brand_study matrix):
  - 25, 50 or 100 live succulent plants in one bulk pack (buyer chooses count)
  - 10 different varieties, 5 plants of each variety
  - each plant fully rooted in its own individual 2-inch nursery pot
  - assorted genera (Echeveria, Sedum, Sempervivum, Crassula and more);
    rosette, upright and trailing forms
  - mixed hardiness — bright indoor light or partial outdoor sun
  - low-maintenance; water deeply only when the soil is completely dry
  - made for DIY arrangements, wedding favors, gifts, centerpieces, home decor,
    event displays, container gardens, and resale
  - professionally packed; printed succulent care guide included

Review insight (VoC) used:
  praised  = healthy live plants, strong value for money, loved the mixed assortment,
             vibrant/attractive, well-rooted and growing, easy for beginners
  objection= "smaller than expected" (top complaint) + arrival condition (dry/moisture)
             → defuse: state 2-inch nursery-pot size honestly up front, foreground
             rooted/established plants, professional live-arrival packing + care guide

Compliance: no $/price, no URL/.com, no superlatives (best/#1/top/leading), no false
hardiness claims, no medical claims. Quantity stated only as the verified 25/50/100.
"""
from __future__ import annotations
import sys
from pathlib import Path

# Self-contained: this script lives at customers/<brand>/products/<product>/run.py
HERE = Path(__file__).resolve().parent          # the product folder
ROOT = HERE.parents[5]                            # project root (Claude_Code/)
sys.path.insert(0, str(ROOT))

from tools.brief_app.core.customers import load_customer
from tools.brief_app.core.excel_parser import parse_excel
from tools.brief_app.core.pdf_builder import BriefBuilder
from tools.brief_app.core.ai import AIImagePlanItem, AIModule, AIQA


EXCEL = HERE / "listing.xlsx"
PLAN_NO = "04"
ASIN = "B0FH5W3DB6"


# ===== KW-led, nursery-accurate US copy (customer-facing English) =====

# Title is HTML-escaped on render, so a literal "&" counts as 1 char. Keep ≤200 real chars.
TITLE = (
    "Mountain Crest Gardens Assorted Succulents Bulk Pack — Choose 25, 50 or 100 Live "
    "Succulent Plants, 10 Varieties, 5 of Each, Rooted in 2 Inch Pots — Mixed Succulents "
    "for Weddings, Favors and Projects"
)

BULLETS = [
    "<b>CHOOSE 25, 50 OR 100 PLANTS</b> — Pick the count your project needs and get live "
    "bulk succulents in one box. Scale up for events, walls, favors, centerpieces, or resale.",

    "<b>10 VARIETIES, 5 OF EACH</b> — A rich, balanced mix of ten different succulents, five "
    "plants of each. The biggest assortment in the Mountain Crest bulk lineup, not multiples of one.",

    "<b>A MIX OF GENERA AND FORMS</b> — Assorted Echeveria, Sedum, Sempervivum, Crassula and "
    "more — rosette, upright, and trailing shapes for varied, eye-catching arrangements.",

    "<b>ROOTED IN 2-INCH POTS</b> — Each plant arrives fully rooted and established in its own "
    "2-inch nursery pot, professionally packed with a printed care guide for live arrival.",

    "<b>EASY-CARE LIVE SUCCULENTS</b> — Mixed hardiness for bright indoor light or partial "
    "outdoor sun. Water deeply only when the soil is fully dry. Simple enough for beginners.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B test)",
        role="hero",
        background="Pure white #FFFFFF seamless (Amazon main-image policy — main hero shows no overlay text). For the badge-bearing alt options, a clean light backdrop #ECEFF4. True-to-life plant color, never oversaturated.",
        purpose="Win the click in the amazon.com bulk-succulent grid — instantly read as a BIG, mixed assortment you can size up (10 kinds, choose 25/50/100), not a single-type tray.",
        visual=(
            "Real, accurate assorted-succulent photography in true natural color. Designer mocks ALL 3 "
            "options; brand picks the winner via Amazon Manage Your Experiments. One callout, one "
            "idea, one clean layout each.\n\n"
            "▸ OPTION A — THE BIG MIXED GRID (wins on variety + volume)\n"
            "Clean overhead grid of many 2-inch pots showing the assorted genera — Echeveria rosettes, "
            "Sedum, Sempervivum, Crassula, a trailing strand — visibly diverse in color and form. "
            "Reads as a generous bulk mix. (Compliant alt: badge top-right '10 VARIETIES 5 EACH' in teal #345C64.)\n\n"
            "▸ OPTION B — CLEAN MAIN (Amazon-policy main image)\n"
            "Pure white background, a tight grouped cluster of several different rosettes plus one 2-inch "
            "pot turned to show the nursery pot, ~85% of frame, soft contact shadow. NO overlay text.\n\n"
            "▸ OPTION C — PICK YOUR COUNT (wins on the scalable quantity)\n"
            "Three pot-cluster sizes side by side labeled 25 / 50 / 100 to dramatize the choose-your-count "
            "promise. (Compliant alt: badge bottom-left 'PICK 25 50 100'.)\n\n"
            "All 3: plants dominant, honest color, real 2-inch nursery pots — never a staged stock look."
        ),
        overlay="10 VARIETIES 5 EACH",
        overlay_sub="A rich mixed box of assorted succulents, rooted in 2-inch nursery pots.",
        props=[
            "OPTION A: overhead grid of assorted genera in 2-inch pots",
            "OPTION B: pure-white cluster of mixed rosettes + one 2-inch nursery pot (no text)",
            "OPTION C: three pot clusters sized 25 / 50 / 100 for the count choice",
        ],
        lighting="Bright, even, daylight-balanced (5000-5500K) so mixed succulent colors stay true and accurate. No warm cast, no saturation push.",
        why_it_works=(
            "A visibly mixed grid of many pots makes the core promise — a big assortment of 10 kinds you "
            "can size up — readable on a mobile thumbnail and separates this pack from the single-type "
            "bulk packs (Sempervivum / Echeveria / Cactus) in the same grid."
        ),
        ctr="A generous, clearly-mixed grid telegraphs 'lots of plants, lots of variety' faster than a single-type shot, pulling project and event buyers out of the bulk-succulent grid.",
        cvr="Seeing the real mixed assortment and the 2-inch pots up front sets an honest expectation, matches the listing, and pre-answers 'how many and how big?' — cutting the 'smaller than expected' bounce and returns.",
    ),
    AIImagePlanItem(
        name="Image 2 — Spec / identity card (what's in the box)",
        role="educate",
        background="Light #ECEFF4 panel with a teal #345C64 footer band. Clean nursery-grade layout.",
        purpose="Pin down the exact identity and counts so buyers know precisely which pack this is before they scroll.",
        visual=(
            "Spec card. Center: the big mixed-grid thumbnail. Four labeled spec tiles with thin "
            "teal line icons:\n"
            "  • COUNT — choose 25, 50 or 100 plants\n"
            "  • MIX — 10 varieties, 5 of each\n"
            "  • TYPE — Echeveria, Sedum, Sempervivum, Crassula and more\n"
            "  • POTS — fully rooted, 2-inch nursery pots\n"
            "Footer band carries the disambiguation line. A coin or ruler cue for true pot scale."
        ),
        overlay="KNOW THIS PACK",
        overlay_sub="Choose 25, 50 or 100 plants, 10 varieties, 5 of each, in 2-inch pots.",
        props=["big mixed-grid thumbnail", "4 spec tiles with line icons", "teal footer band", "coin or ruler for 2-inch pot scale"],
        lighting="Flat, clean studio light — legibility over atmosphere.",
        why_it_works=(
            "Converts the listing's hard facts into a single scannable identity card, so a shopper "
            "comparing the seven Mountain Crest packs can confirm count choice, mix, genera and pot size "
            "at a glance — the heart of the client's disambiguation mandate, and an honest size cue."
        ),
        ctr="A clear spec card reassures project buyers who need to know exactly what arrives and earns the scroll into the gallery.",
        cvr="Stating the 2-inch pot size and the count options plainly removes the 'what and how big?' surprise that drives this listing's top complaint.",
    ),
    AIImagePlanItem(
        name="Image 3 — Hook: one box covers the whole project",
        role="hook",
        background="Clean light #ECEFF4 with the choose-your-count clusters as the focal point.",
        purpose="Make the dream outcome unmistakable — one bulk box covers a whole project or event with a rich mix.",
        visual=(
            "Three labeled pot clusters — 25, 50, 100 — flowing left to right, each a generous spread of "
            "assorted rosettes in 2-inch pots. Behind them, faint use-case cues (a wedding-favor pot with "
            "ribbon, a centerpiece bowl, a living-wall corner). Caption strip: 'one box, your whole project'."
        ),
        overlay="ONE BOX, WHOLE PROJECT",
        overlay_sub="Pick 25, 50 or 100 mixed succulents and cover favors, centerpieces, and walls.",
        props=["three pot clusters sized 25 / 50 / 100", "wedding-favor pot with ribbon", "centerpiece bowl", "living-wall corner cue"],
        lighting="Bright daylight-balanced, true color across every rosette.",
        why_it_works=(
            "Leads with the outcome buyers are really shopping for — enough plants in one order to finish "
            "a wedding, event, or wall — and ties the scalable count directly to real bulk use cases."
        ),
        ctr="'One box, whole project' speaks straight to event and DIY buyers scanning for quantity, and the 25/50/100 ladder proves it scales.",
        cvr="Matching the count to a concrete project helps buyers pick the right size the first time, raising fit and lowering re-orders.",
    ),
    AIImagePlanItem(
        name="Image 4 — Desire: the finished mixed arrangement",
        role="desire",
        background="A bright, real styled scene — wedding-favor table or decor shelf, natural daylight.",
        purpose="Sell the dream outcome — a beautiful, finished display built from the mixed assortment.",
        visual=(
            "Hero lifestyle shot: dozens of the assorted succulents styled into a finished result — a row "
            "of wedding-favor pots with kraft tags, a mixed centerpiece bowl, a small living-wall panel. "
            "Diverse rosette, upright and trailing forms create texture and color. Natural, honest color — "
            "never oversaturated. A real styled scene, not stock."
        ),
        overlay="BUILT FOR YOUR EVENT",
        overlay_sub="Favors, centerpieces and decor come together from one rich mixed box.",
        props=["row of wedding-favor pots with kraft tags", "mixed centerpiece bowl", "small living-wall panel", "trailing and rosette forms for texture"],
        lighting="Natural daylight, soft directional light for dimension, accurate plant color.",
        why_it_works=(
            "Shows the payoff buyers want — a finished, photogenic event or decor display — and the mixed "
            "forms justify why the assortment (not a single type) is the right choice for projects."
        ),
        ctr="A finished favors-and-centerpieces scene is aspirational for event and DIY buyers and stands out from plain pot shots in the grid.",
        cvr="Picturing the buyer's own finished project sets correct expectations and connects the mix directly to the result they're after.",
    ),
    AIImagePlanItem(
        name="Image 5 — Educate: easy care for a mixed pack",
        role="educate",
        background="White with a green accent band #78A848 in the footer.",
        purpose="Show the plants are low-maintenance and beginner-friendly, lowering the 'will they survive?' barrier.",
        visual=(
            "Headline at top, then a clean 4-step care row with line icons:\n"
            "  • LIGHT — bright indoor light or partial outdoor sun\n"
            "  • WATER — only when the soil is fully dry\n"
            "  • POTS — rooted in 2-inch nursery pots, repot anytime\n"
            "  • MIX — varied forms, all easy-care\n"
            "Footer band carries 'printed care guide included'. A rooted 2-inch pot anchors the side."
        ),
        overlay="EASY TO KEEP ALIVE",
        overlay_sub="Bright light or partial sun, water only when dry, with a care guide included.",
        props=["4 care-step icons", "rooted 2-inch nursery pot", "green footer band", "printed care guide"],
        lighting="Flat, clean studio light for legibility.",
        why_it_works=(
            "Turns the USP care facts into a confidence builder for first-time and bulk buyers, and the "
            "included care guide directly answers the arrival-and-survival worry seen in reviews."
        ),
        ctr="Low-maintenance, beginner-friendly care is a top reassurance for buyers ordering many live plants at once.",
        cvr="Simple, mixed-pack care and an included guide lower the perceived risk of a big live-plant order and support the purchase.",
    ),
    AIImagePlanItem(
        name="Image 6 — WHICH PACK IS RIGHT FOR YOU? (sibling comparison)",
        role="educate",
        background="Light #ECEFF4 with a teal #345C64 header bar. Clean comparison layout.",
        purpose="Disambiguate THIS pack from the single-type bulk packs so buyers pick the right one (the client's #1 ask).",
        visual=(
            "A 3-column compare card (this pack highlighted in teal). Columns and rows:\n"
            "  Row labels: PLANTS · ASSORTMENT · TYPE · HARDINESS · MADE FOR\n"
            "  COL 1 (highlighted) — THIS · Assorted Bulk: 'choose 25, 50 or 100' · '10 varieties, 5 of each' · "
            "'Mixed genera (Echeveria, Sedum, Sempervivum, Crassula)' · 'Mixed, indoor or partial sun' · 'Big projects, events, weddings, walls'\n"
            "  COL 2 — Sempervivum Bulk: '25 plants' · '5 varieties, 5 of each' · 'Sempervivum only' · "
            "'Cold-hardy, outdoor' · 'Outdoor projects, landscaping'\n"
            "  COL 3 — Echeveria Bulk: '25 plants' · '5 varieties, 5 of each' · 'Echeveria only' · "
            "'Tender, indoor or mild' · 'Colorful arrangements, decor'\n"
            "Caption under it: 'Want the biggest mix and your own count? This is your pack.'"
        ),
        overlay="WHICH PACK IS RIGHT",
        overlay_sub="Want the biggest mix and your own count? Choose this. Want one type? See a single bulk.",
        props=["3-column comparison card", "this-pack column highlighted teal", "row icons: count, assortment, type, hardiness, use"],
        lighting="Flat, clean studio light — table must be legible on a phone.",
        why_it_works=(
            "Directly fulfills the disambiguation mandate: it positions this most-variety, pick-your-count "
            "pack (10 kinds, mixed genera) against the single-type Sempervivum and Echeveria bulks, so "
            "buyers self-route to the right pack instead of guessing."
        ),
        ctr="Shoppers cross-shopping the Mountain Crest bulk packs stop here to settle which one fits, raising qualified clicks.",
        cvr="Pre-empting the 'is this all one type or a real mix?' confusion sharply cuts wrong-pack returns.",
    ),
    AIImagePlanItem(
        name="Image 7 — Trust / Close: real nursery, healthy arrival",
        role="trust",
        background="Clean nursery scene: trays of rooted 2-inch pots, soft daylight.",
        purpose="Build arrival confidence and close on the family-nursery promise; quietly defuse the size/condition objections.",
        visual=(
            "Two-part. LEFT: trays of healthy, established assorted succulents in 2-inch pots with visible "
            "new growth, plus the bulk live-plant box, upright-handling labels and the printed care guide. "
            "RIGHT: a small trust strip — 'rooted & established' · 'professionally packed' · "
            "'care guide included' · '2-inch nursery pots'. Hands (no face) lifting one pot for honest scale. "
            "Nursery-grade and real — a licensed family succulent nursery, not a kiosk."
        ),
        overlay="REAL NURSERY PLANTS",
        overlay_sub="Rooted and established in 2-inch pots, professionally packed with a care guide.",
        props=["trays of rooted 2-inch pots with new growth", "bulk live-plant box with handling labels", "printed care guide", "hands lifting a pot (no face)"],
        lighting="Soft natural daylight, accurate color, lived-in nursery feel — not staged stock.",
        why_it_works=(
            "Closes on the brand promise (real plants, real nursery, real help) and addresses the recurring "
            "negatives — 'smaller than expected' and arrival condition — by honestly showing the 2-inch pot "
            "size, rooted established plants, professional packing and the included care guide."
        ),
        ctr="The healthy-plants-and-care-guide trust strip reassures buyers wary of ordering many mail-order live plants.",
        cvr="Honest pot scale, visible plant health and professional packing answer the top size and arrival worries and seal the purchase.",
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Brand banner",
        role="a+_banner",
        headline="THE BIGGEST MIX, YOUR COUNT",
        body=(
            "Assorted live succulents in one bulk box — choose 25, 50, or 100 plants, with "
            "10 different varieties, 5 of each. A rich mix of Echeveria, Sedum, Sempervivum, "
            "Crassula and more, all rooted in 2-inch nursery pots. The variety and volume to "
            "cover weddings, events, walls, favors, and projects from a single order."
        ),
        visual="Wide cinematic overhead of the big mixed grid of assorted succulents in 2-inch pots, true natural color, teal #345C64 wordmark top-left. Clean light background.",
        alt="Overhead grid of assorted succulent varieties in 2-inch nursery pots, 10 kinds, 5 of each, bulk pack.",
    ),
    AIModule(
        name="Module 2 — Carousel (4 tiles): why this pack",
        role="a+_carousel",
        headline="WHY THIS PACK",
        body=(
            "Tile 1: <b>CHOOSE YOUR COUNT</b> — 25, 50, or 100 plants in one box.<br/>"
            "Tile 2: <b>10 VARIETIES, 5 EACH</b> — the biggest assortment, a balanced mix.<br/>"
            "Tile 3: <b>MIXED GENERA AND FORMS</b> — rosette, upright, and trailing shapes.<br/>"
            "Tile 4: <b>ROOTED IN 2-INCH POTS</b> — established and ready to arrange."
        ),
        visual="4 square tiles, green #78A848 accent corner per tile, line icons (count ladder · grid · mixed forms · pot). Real plant photography in each.",
        alt="Four-tile carousel: choose your count, 10 varieties five of each, mixed genera, rooted in 2-inch pots.",
    ),
    AIModule(
        name="Module 3 — Banner: one box covers the project",
        role="a+_banner",
        headline="ONE BOX, YOUR WHOLE PROJECT",
        body=(
            "Pick the count your project needs and let one box do the work. The mixed forms "
            "and colors come together as wedding favors, centerpieces, container gardens, "
            "living walls, and event displays — a finished result from a single bulk order, "
            "with plenty of plants to spare for resale or gifts."
        ),
        visual="Wide banner: assorted succulents styled into wedding favors, a centerpiece bowl, and a living-wall corner in natural daylight. Honest, true color — never oversaturated.",
        alt="A+ banner: assorted bulk succulents styled into wedding favors, centerpieces, and a living wall.",
    ),
    AIModule(
        name="Module 4 — Banner: easy care for a mixed pack",
        role="a+_banner",
        headline="EASY TO KEEP, BEGINNER READY",
        body=(
            "These mixed-hardiness succulents do well in bright indoor light or partial "
            "outdoor sun. Water deeply only when the soil is fully dry and otherwise leave "
            "them be. Each plant arrives rooted in its own 2-inch pot, professionally packed "
            "with a printed care guide so even first-time growers can keep them thriving."
        ),
        visual="Triptych: LEFT a rooted 2-inch pot, CENTER light/water/pot care icons, RIGHT the printed care guide. Clean daylight, green accents.",
        alt="A+ triptych: rooted 2-inch pot, simple light and water care, and the included printed care guide.",
    ),
    AIModule(
        name="Module 5 — Comparison: which pack is right for you",
        role="a+_comparison",
        headline="WHICH PACK IS RIGHT",
        body=(
            "Compare across three columns: <b>This Assorted Bulk</b> · Sempervivum Bulk · "
            "Echeveria Bulk.<br/><br/>"
            "Rows: Plant count · Assortment · Plant type · Hardiness · Made for.<br/><br/>"
            "<b>This Assorted Bulk:</b> choose 25, 50 or 100 plants · 10 varieties, 5 of each · "
            "mixed genera (Echeveria, Sedum, Sempervivum, Crassula and more) · mixed, indoor or "
            "partial sun · big projects, events, weddings, and walls.<br/>"
            "<b>Sempervivum Bulk:</b> 25 plants · 5 varieties, 5 of each · Sempervivum only · "
            "cold-hardy, outdoor · outdoor projects and landscaping.<br/>"
            "<b>Echeveria Bulk:</b> 25 plants · 5 varieties, 5 of each · Echeveria only · "
            "tender, indoor or mild · colorful arrangements and decor.<br/><br/>"
            "Want the biggest mix and your own count? This is your pack. Want a single plant "
            "type? Choose a single-type bulk instead. Highlight the This column."
        ),
        visual="Amazon Premium Comparison Chart, 3 product columns, this-pack column highlighted teal #345C64. Sibling packs named by their pack name only.",
        alt="Comparison chart: this Assorted Bulk (10 varieties, choose your count) vs Sempervivum Bulk vs Echeveria Bulk (single type).",
    ),
    AIModule(
        name="Module 6 — Carousel (4 tiles): where it shines",
        role="a+_carousel",
        headline="WHERE IT SHINES",
        body=(
            "Tile 1: <b>WEDDINGS AND FAVORS</b> — potted succulents as keepsakes.<br/>"
            "Tile 2: <b>EVENTS AND CENTERPIECES</b> — mixed bowls for the table.<br/>"
            "Tile 3: <b>LIVING WALLS</b> — fill a vertical panel with a rich mix.<br/>"
            "Tile 4: <b>RESALE AND GIFTS</b> — plenty of plants to share or sell."
        ),
        visual="4 identically composed use-case tiles, real styled succulent scenes, green accent corner per tile, consistent natural daylight.",
        alt="Four-tile carousel of uses: weddings and favors, events and centerpieces, living walls, resale and gifts.",
    ),
    AIModule(
        name="Module 7 — Premium Q&A",
        role="a+_qa",
        headline="COMMON QUESTIONS",
        body=(
            "<b>Q.</b> How many plants do I get?<br/>"
            "<b>A.</b> You choose the count — 25, 50, or 100 live succulents in one bulk pack, "
            "as 10 different varieties with 5 plants of each.<br/><br/>"
            "<b>Q.</b> What varieties are included?<br/>"
            "<b>A.</b> An assorted mix of genera such as Echeveria, Sedum, Sempervivum, Crassula "
            "and more, in rosette, upright, and trailing forms.<br/><br/>"
            "<b>Q.</b> What size are the plants?<br/>"
            "<b>A.</b> Each plant arrives fully rooted and established in its own 2-inch nursery "
            "pot, professionally packed with a printed care guide.<br/><br/>"
            "<b>Q.</b> Indoors or outdoors?<br/>"
            "<b>A.</b> The mix has mixed hardiness and does well in bright indoor light or partial "
            "outdoor sun. Water deeply only when the soil is fully dry.<br/><br/>"
            "<b>Q.</b> How is this different from the single-type bulk packs?<br/>"
            "<b>A.</b> This pack is the biggest mix with a count you choose — 10 varieties across "
            "several genera. The Sempervivum, Echeveria, and Cactus bulks are each one plant type only."
        ),
        visual="Vertical Q/A table, teal dividers between questions, small Q./A. labels in dark #414042.",
        alt="Premium Q&A module answering count, varieties, pot size, indoor vs outdoor, and single-type difference.",
    ),
]


QA = [
    AIQA(q="How many plants do I get, and can I choose?",
         a="You choose the count — 25, 50, or 100 live succulents in one bulk pack. Each option is 10 different varieties with 5 plants of each, so the mix stays balanced at any size."),
    AIQA(q="What varieties and types of succulents are included?",
         a="An assorted mix of genera such as Echeveria, Sedum, Sempervivum, Crassula and more, in rosette, upright, and trailing forms. It is the biggest assortment in the Mountain Crest bulk lineup."),
    AIQA(q="What size are the plants and how do they ship?",
         a="Each plant arrives fully rooted and established in its own individual 2-inch nursery pot. Packs are professionally packed for live arrival with a printed succulent care guide included."),
    AIQA(q="Should I keep them indoors or outdoors?",
         a="The mix has mixed hardiness and does well in bright indoor light or partial outdoor sun. Water deeply only when the soil is completely dry."),
    AIQA(q="Are these good for weddings, events, and projects?",
         a="Yes. The variety and volume suit DIY arrangements, wedding favors, gifts, centerpieces, home decor, event displays, container gardens, living walls, and resale — one box can cover a whole project."),
    AIQA(q="How is this different from the single-type bulk packs?",
         a="This pack is the biggest mix with a count you choose — 10 varieties across several genera. The Sempervivum, Echeveria, and Cactus bulks are each a single plant type only, with 5 varieties of that one type."),
    AIQA(q="Are the plants easy to care for?",
         a="Yes. They are low-maintenance and beginner-friendly. Give them bright light or partial sun, water deeply only when the soil is fully dry, and follow the included care guide."),
    AIQA(q="Will the assortment match what is shown?",
         a="You receive a hand-picked mix of 10 varieties, 5 of each, chosen for diversity of color and form. Each plant is rooted in a 2-inch nursery pot, so it is sized for small pots on arrival."),
]


# Backend KWs — US English, stem-deduped, byte-packed. No brand/title duplicates, no superlatives.
BACKEND = (
    "assorted succulents bulk live plants succulent variety pack mixed echeveria sedum "
    "crassula sempervivum rosette trailing 2 inch pots rooted starter wedding favors "
    "event centerpiece living wall arrangement decor container garden gift indoor outdoor "
    "drought tolerant low maintenance beginner real plant set assortment 25 50 100 resale"
)


def main() -> None:
    print("Loading Mountain Crest Gardens customer + parsing Assorted Bulk Excel…")
    cust = load_customer("mountain_crest_gardens")
    brief = parse_excel(EXCEL)
    OUT = HERE / f"{PLAN_NO}_{ASIN}_Image Plan.pdf"
    real_title_len = len(TITLE.replace("&amp;", "&"))
    print(f"  Product: {brief.product_name}")
    print(f"  ASIN: {ASIN}  Marketplace: {cust.marketplace}")
    print(f"  USPs={len(brief.usps)} KWs={len(brief.all_keywords)} reviews=+{len(brief.good_reviews)}/-{len(brief.bad_reviews)}")
    print(f"  TITLE real chars (de-escaped): {real_title_len}")

    builder = BriefBuilder(cust, brief, OUT, ai=None)
    builder._ai_title = TITLE
    builder._ai_bullets = BULLETS
    builder._ai_images = IMAGES
    builder._ai_modules = MODULES
    builder._ai_qa = QA
    builder._ai_backend = BACKEND
    builder.copy_source_label = "Hand-written senior copy (KW-led, nursery-accurate)"

    print("Building branded PDF…")
    pdf_path = builder.build()
    size_kb = pdf_path.stat().st_size // 1024
    import re
    pages = len(re.findall(rb'/Type\s*/Page[^s]', pdf_path.read_bytes()))
    print(f"Built: {pdf_path}")
    print(f"  Pages: {pages}  Size: {size_kb} KB")


if __name__ == "__main__":
    main()
