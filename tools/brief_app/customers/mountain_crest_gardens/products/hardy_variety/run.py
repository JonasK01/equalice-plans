"""Mountain Crest Gardens — HARDY VARIETY PACK (20 unique, mixed types) — Image Plan 03
Hand-written senior copy injected into the branded EQUALICE ReportLab pipeline.

Marketplace: amazon.com (US). Customer text + art direction both ENGLISH.

THIS PACK'S IDENTITY (the #1 job — make it crystal clear which pack this is):
  • A hand-picked MIX of hardy types — Sempervivum + Sedum + more.
    Rosette, stemmed AND trailing forms (not all one genus).
  • VARIETY PACK = 20 unique plants, no repeats — maximum diversity of FORMS.
  • Frost-tolerant to at least 0°F, USDA Zone 7-10, OUTDOOR.
  • Fully rooted & established in 2-inch nursery pots.
  For: frost-proof landscaping, rock gardens, outdoor variety, DIY arrangements.

THE DISAMBIGUATION (client mandate): a dedicated "WHICH PACK IS RIGHT FOR YOU?"
comparison module positions THIS pack vs the siblings. The two key contrasts:
  (a) vs 01 SEMPERVIVUM VARIETY — that pack is ONLY hens & chicks and even
      hardier (to -20°F). THIS 03 pack is a MIXED-type hardy assortment (more
      FORMS — rosette + stemmed + trailing) to 0°F.
  (b) vs the TENDER packs (Echeveria / Trailing & Strings) — those are NOT
      frost-proof. THIS pack survives winter outdoors in Zone 7-10.
Disambiguating badges live on the creative: "20 UNIQUE MIXED HARDY",
"FROST-TOLERANT TO 0F", "OUTDOOR ZONE 7-10".

LANGUAGE: all art-direction fields (purpose, background, visual, props, lighting,
why_it_works, ctr, cvr, module visual) are designer-facing English. All customer
text (title, bullets, overlays, module headline/body, Q&A) is English too (US).

OVERLAY RULE: sell the OUTCOME / identity, not the action. Each overlay distinct,
≤30 chars AND ≤5 words, SMOOTH (no "Word? Word." fragments, no "·" middots —
middots count as words). overlay_sub ≤90 · module headline ≤38 · bullet head ≤45.

Verified facts (from listing.xlsx USPs + brand_study matrix):
  - 20 unique live hardy succulents, no repeats; a MIX incl. Sempervivum + Sedum
  - hand-picked mix of rosette, stemmed and trailing forms; diverse colors/textures
  - cold- and frost-tolerant to at least 0°F; USDA Zones 7-10; year-round outdoor
  - each plant fully rooted in its own 2-inch nursery pot, ready to transplant
  - low maintenance, drought tolerant; water deeply only after soil dries fully
  - full sun or filtered/partial sun; containers or in-ground, gritty well-draining soil
  - printed care guide included; many varieties easy to propagate from offsets/cuttings
  - pet-safe; reusable nursery pots; grower states packaging is recyclable

Review insight (VoC) used:
  praised  = healthy beautiful plants, fast/new growth, matched photos, exceeds
             expectations, attractive color variety, gift-worthy, clear ship labels
  objection= occasional musty odor (shipping moisture); hard to contact seller
             → defuse: live-plant packing, rooted/established plants, care-guide recovery

Compliance: no $/price, no URL/.com, no superlatives (best/#1/top/leading),
no false hardiness claims, no medical claims. Hardiness stated only as the
verified 0°F / Zone 7-10 figures.
"""
from __future__ import annotations
import sys
from pathlib import Path

# Self-contained: this script lives at customers/<brand>/products/<product>/run.py
HERE = Path(__file__).resolve().parent          # the product folder
ROOT = HERE.parents[5]                           # project root (Claude_Code/)
sys.path.insert(0, str(ROOT))

from tools.brief_app.core.customers import load_customer
from tools.brief_app.core.excel_parser import parse_excel
from tools.brief_app.core.pdf_builder import BriefBuilder
from tools.brief_app.core.ai import AIImagePlanItem, AIModule, AIQA


EXCEL = HERE / "listing.xlsx"
PLAN_NO = "03"
ASIN = "B0FH7LHZTQ"


# ===== KW-led, nursery-accurate US copy (customer-facing English) =====

# Title is HTML-escaped on render, so a literal "&" counts as 1 char. Keep ≤200 real chars.
TITLE = (
    "Mountain Crest Gardens Hardy Succulent Variety Pack — 20 Unique Live Outdoor Plants, "
    "a Mix of Sedum, Sempervivum and More, Rooted in 2 Inch Pots — Frost Hardy Succulents "
    "for Rock Gardens"
)

BULLETS = [
    "<b>20 UNIQUE HARDY SUCCULENTS</b> — Twenty live outdoor succulents, all different, no "
    "repeats. A hand-picked mix of Sempervivum, Sedum and more in rosette, stemmed and trailing forms.",

    "<b>FROST HARDY TO 0F, OUTDOORS</b> — These frost-tolerant succulents take at least 0°F and "
    "thrive year-round outdoors in USDA Zones 7 to 10 — built for rock gardens, beds, and containers.",

    "<b>ROOTED IN 2-INCH POTS</b> — Each plant arrives fully rooted and established in its own "
    "2-inch nursery pot, ready to display, transplant, or plant straight into the garden.",

    "<b>LOW-CARE OUTDOOR SUCCULENTS</b> — Drought tolerant and low maintenance. Full or partial "
    "sun, gritty well-draining soil, water deeply only after the soil dries out completely.",

    "<b>A FROST-PROOF LIVING TAPESTRY</b> — Mixed forms, colors and textures make a hardy outdoor "
    "display for landscaping and DIY arrangements. Pet-safe, with a printed care guide included.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B test)",
        role="hero",
        background="Pure white #FFFFFF seamless (Amazon main-image policy — main hero shows no overlay text). For the badge-bearing alt options, a clean light backdrop #ECEFF4. True-to-life plant color, never oversaturated.",
        purpose="Win the click in the amazon.com live-succulent grid — instantly read as a MIXED hardy outdoor assortment of 20 different forms, not duplicates and not tender indoor plants.",
        visual=(
            "Real, accurate succulent photography in true natural color. Designer mocks ALL 3 "
            "options; brand picks the winner via Amazon Manage Your Experiments. One callout, one "
            "idea, one clean layout each.\n\n"
            "▸ OPTION A — THE MIXED GRID OF 20 (wins on the diversity-of-forms promise)\n"
            "Clean overhead 4x5 grid of the actual 20 different plants in their 2-inch nursery "
            "pots — visibly MIXED types: tight rosettes (Sempervivum), fleshy mats and spreaders "
            "(Sedum), plus a stemmed and a trailing form. Reads as a hardy assortment at a glance. "
            "(Compliant alt: badge top-right 'FROST HARDY TO 0F' in teal #345C64.)\n\n"
            "▸ OPTION B — CLEAN MAIN (Amazon-policy main image)\n"
            "Pure white background, a tight cluster of several distinct hardy forms plus one 2-inch "
            "pot turned to show the nursery pot, ~85% of frame, soft contact shadow. NO overlay text.\n\n"
            "▸ OPTION C — IN THE ROCK GARDEN (wins on frost-proof outdoor use)\n"
            "The mixed varieties nestled among stones in a sunlit rock garden, a hand placing one pot "
            "for scale. (Compliant alt: badge bottom-left '20 UNIQUE MIXED HARDY'.)\n\n"
            "All 3: plants dominant, honest color, nursery-grade and real — never a staged stock look."
        ),
        overlay="20 UNIQUE HARDY TYPES",
        overlay_sub="Twenty different frost-hardy succulents, a mix of forms, rooted in 2-inch pots.",
        props=[
            "OPTION A: overhead 4x5 grid of 20 distinct mixed-type plants in 2-inch pots",
            "OPTION B: pure-white cluster of mixed hardy forms + one 2-inch nursery pot (no text)",
            "OPTION C: mixed varieties in a sunlit rock garden + a hand placing one pot for scale",
        ],
        lighting="Bright, even, daylight-balanced (5000-5500K) so plant color stays true and accurate. No warm cast, no saturation push.",
        why_it_works=(
            "A grid of twenty visibly different FORMS — rosettes, mats, a trailer — telegraphs a "
            "hardy MIXED assortment on a mobile thumbnail, separating this pack from the single-genus "
            "Sempervivum packs and the tender indoor packs in the same grid."
        ),
        ctr="A mixed grid of rosette, stemmed and trailing hardy plants reads as 'variety + outdoor' faster than a plain pot, pulling landscaping and rock-garden buyers out of the grid.",
        cvr="Seeing all 20 distinct hardy forms up front sets an honest expectation, matches the listing photos buyers praise, and pre-answers 'is this really a mix, and is it frost-proof?' — cutting bounce and returns.",
    ),
    AIImagePlanItem(
        name="Image 2 — Spec / identity card (what's in the box)",
        role="educate",
        background="Light #ECEFF4 panel with a teal #345C64 footer band. Clean nursery-grade layout.",
        purpose="Pin down the exact identity, mix and hardiness so buyers know precisely which pack this is before they scroll.",
        visual=(
            "Spec card. Center: the 20-plant mixed grid thumbnail. Four labeled spec tiles with thin "
            "teal line icons:\n"
            "  • COUNT — 20 unique plants, all different\n"
            "  • MIX — Sempervivum, Sedum and more\n"
            "  • HARDINESS — Zone 7-10, to 0F, outdoor\n"
            "  • POTS — fully rooted, 2-inch nursery pots\n"
            "Footer band carries the disambiguation line. A small ruler/coin cue for pot scale."
        ),
        overlay="KNOW THIS PACK",
        overlay_sub="20 unique hardy succulents, a mix of forms, rooted in 2-inch pots, frost-hardy.",
        props=["20-plant mixed grid thumbnail", "4 spec tiles with line icons", "teal footer band", "coin or ruler for pot scale"],
        lighting="Flat, clean studio light — legibility over atmosphere.",
        why_it_works=(
            "Converts the listing's hard facts into a single scannable identity card, so a shopper "
            "comparing the seven Mountain Crest packs can confirm count, mix, hardiness and pot size "
            "at a glance — the heart of the client's disambiguation mandate."
        ),
        ctr="A clear spec card reassures detail-driven plant buyers and earns the scroll into the gallery.",
        cvr="Removing every 'what exactly do I get?' question up front shortens the decision and reduces wrong-pack returns.",
    ),
    AIImagePlanItem(
        name="Image 3 — Hook: the hardy mix (many forms)",
        role="hook",
        background="Clean light #ECEFF4 with the 20-grid as the focal point.",
        purpose="Make the mixed-forms, all-hardy idea unmistakable — the reason to choose THIS pack over a single-genus one.",
        visual=(
            "The full 4x5 grid of 20 distinct plants, each in its 2-inch pot, grouped by FORM with "
            "thin teal labels: ROSETTE · STEMMED · TRAILING. One highlighted cell pulled out slightly "
            "to show a named stake. Small caption strip: 'every plant different, every plant hardy'."
        ),
        overlay="ONE OF EACH HARDY",
        overlay_sub="Twenty different hardy succulents, mixed forms, no duplicates.",
        props=["4x5 grid of 20 distinct plants", "form labels: rosette, stemmed, trailing", "one named variety stake pulled forward"],
        lighting="Bright daylight-balanced, true color across every plant.",
        why_it_works=(
            "Doubles down on the strongest differentiator versus the single-genus packs: this is "
            "twenty different plants across multiple FORMS, all frost-hardy — exactly what outdoor "
            "and landscaping buyers searching for variety want."
        ),
        ctr="'One of each hardy' plus the rosette/stemmed/trailing split is the variety promise outdoor buyers scan for, proven instantly by the grid.",
        cvr="Buyers who specifically want a hardy MIX (not all hens & chicks) self-select here, raising fit and satisfaction.",
    ),
    AIImagePlanItem(
        name="Image 4 — Desire: the frost-proof tapestry outdoors",
        role="desire",
        background="A real, sunlit rock garden — stones, gravel, natural daylight in cool-season light.",
        purpose="Sell the dream outcome — a thriving, frost-proof outdoor tapestry that survives winter.",
        visual=(
            "Hero lifestyle shot: many of the mixed varieties planted together among rocks, forming a "
            "tapestry of rosettes, spreading Sedum mats and a trailing edge — different forms, colors "
            "and textures. A light dusting of frost on a few leaf tips to signal cold-hardy. Natural, "
            "honest color — never oversaturated. Real outdoor scene."
        ),
        overlay="A FROST-PROOF TAPESTRY",
        overlay_sub="Mixed hardy succulents thrive together outdoors through the seasons.",
        props=["mixed forms planted among rocks", "light frost on a few leaf tips", "natural gravel and stone", "trailing form spilling over an edge"],
        lighting="Natural cool-season daylight, soft directional sun for dimension, accurate color.",
        why_it_works=(
            "Shows the payoff outdoor buyers want — a diverse, living display that survives winter — "
            "and matches the frost-hardy, Zone 7-10 landscaping use this mixed pack is built for."
        ),
        ctr="The frosted-but-thriving outdoor tapestry is aspirational for rock-garden and landscaping buyers and stands out in the grid.",
        cvr="A realistic frost-proof in-garden result sets correct expectations and pictures the buyer's own winter-hardy display.",
    ),
    AIImagePlanItem(
        name="Image 5 — Educate: easy outdoor care",
        role="educate",
        background="White with a green accent band #78A848 in the footer.",
        purpose="Show the plants are low-maintenance and frost-hardy, lowering the 'will I keep them alive?' barrier.",
        visual=(
            "Headline at top, then a clean 4-step care row with line icons:\n"
            "  • SUN — full or partial sun\n"
            "  • WATER — only after soil is fully dry\n"
            "  • SOIL — gritty, well-draining mix\n"
            "  • COLD — frost-hardy to 0F, Zone 7-10\n"
            "Footer band carries 'printed care guide included'. A rooted 2-inch pot anchors the side."
        ),
        overlay="HARDY AND LOW CARE",
        overlay_sub="Full or partial sun, gritty soil, water only when dry, frost-hardy to 0F.",
        props=["4 care-step icons", "rooted 2-inch nursery pot", "green footer band", "offset/cutting propagation detail"],
        lighting="Flat, clean studio light for legibility.",
        why_it_works=(
            "Turns the USP care facts into a confidence builder for first-time outdoor succulent "
            "buyers, while the propagation note signals long-term value as the planting fills in."
        ),
        ctr="Drought-tolerant, frost-hardy, low-maintenance care is a top reassurance for outdoor live-plant shoppers scanning the gallery.",
        cvr="Clear, simple care plus the well-draining-soil cue lowers the perceived risk of keeping live plants and supports the purchase.",
    ),
    AIImagePlanItem(
        name="Image 6 — WHICH PACK IS RIGHT FOR YOU? (sibling comparison)",
        role="educate",
        background="Light #ECEFF4 with a teal #345C64 header bar. Clean comparison layout.",
        purpose="Disambiguate THIS pack from the sibling Mountain Crest packs so buyers pick the right one (the client's #1 ask).",
        visual=(
            "A 3-column compare card (this pack highlighted in teal). Columns and rows:\n"
            "  Row labels: PLANTS · ASSORTMENT · TYPE · HARDINESS · MADE FOR\n"
            "  COL 1 (highlighted) — THIS · Hardy Variety: '20 unique' · 'all different, mixed forms' · "
            "'Sempervivum + Sedum + more' · 'to 0F, Zone 7-10, outdoor' · 'Frost-proof landscaping'\n"
            "  COL 2 — Sempervivum Variety: '20 unique' · 'all different, one genus' · "
            "'Sempervivum only' · 'to -20F, Zone 5-10' · 'Hens and chicks collecting'\n"
            "  COL 3 — Trailing and Strings: '12 plants' · '6 varieties, 2 of each' · "
            "'Trailing, tender' · 'indoor or mild outdoor' · 'Hanging planters'\n"
            "Caption under it: 'Want a hardy outdoor mix that survives winter? This is your pack.'"
        ),
        overlay="WHICH PACK IS RIGHT",
        overlay_sub="Want a hardy outdoor mix? Choose this. All hens and chicks? See the Sempervivum pack.",
        props=["3-column comparison card", "this-pack column highlighted teal", "row icons: count, assortment, type, hardiness, use"],
        lighting="Flat, clean studio light — table must be legible on a phone.",
        why_it_works=(
            "Directly fulfills the disambiguation mandate: it positions the hardy MIXED pack against "
            "the single-genus Sempervivum Variety (only hens & chicks, even hardier to -20F) and the "
            "tender Trailing pack (indoor, not frost-proof), so buyers self-route to the right pack."
        ),
        ctr="Shoppers cross-shopping the Mountain Crest packs stop here to settle which one fits, raising qualified clicks.",
        cvr="Pre-empting the 'is this all one type or a mix, and is it really frost-proof?' confusion sharply cuts wrong-pack returns.",
    ),
    AIImagePlanItem(
        name="Image 7 — Trust / Close: real nursery, healthy arrival",
        role="trust",
        background="Clean nursery scene: trays of rooted 2-inch pots, soft daylight.",
        purpose="Build arrival confidence and close on the family-nursery promise; quietly defuse the rare musty-odor objection.",
        visual=(
            "Two-part. LEFT: a tray of healthy, established mixed succulents in 2-inch pots with "
            "visible new growth, plus the live-plant box with upright-handling labels and the printed "
            "care guide. RIGHT: a small trust strip — 'rooted & established' · 'packed for live arrival' "
            "· 'care guide included' · 'pet-safe'. Hands (no face) lifting one pot for scale. "
            "Honest, nursery-grade — a real licensed succulent nursery, not a kiosk."
        ),
        overlay="REAL NURSERY PLANTS",
        overlay_sub="Rooted and established, packed for live arrival, with a care guide included.",
        props=["tray of rooted 2-inch pots with new growth", "live-plant box with handling labels", "printed care guide", "hands lifting a pot (no face)"],
        lighting="Soft natural daylight, accurate color, lived-in nursery feel — not staged stock.",
        why_it_works=(
            "Closes on the brand promise (real plants, real nursery, real help) and addresses the "
            "recurring negatives — occasional shipping-moisture musty odor and hard-to-reach contact — "
            "by foregrounding rooted, established plants, live-arrival packing and the included care guide."
        ),
        ctr="The healthy-plants-and-care-guide trust strip reassures buyers wary of mail-order live plants.",
        cvr="Visible plant health, live-arrival packing and an included care guide answer the top arrival worry and seal the purchase.",
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Brand banner",
        role="a+_banner",
        headline="20 UNIQUE HARDY SUCCULENTS",
        body=(
            "Twenty live outdoor succulents — all different, no repeats. A hand-picked "
            "mix of Sempervivum, Sedum and more in rosette, stemmed and trailing forms, "
            "rooted in 2-inch nursery pots. Frost-tolerant to 0°F in USDA Zones 7 to 10 — "
            "a ready-made assortment for frost-proof rock gardens and landscaping."
        ),
        visual="Wide cinematic overhead of the full 20-plant mixed grid in 2-inch pots, true natural color, teal #345C64 wordmark top-left. Clean light background.",
        alt="Overhead grid of 20 different hardy succulents in 2-inch nursery pots, a mix of forms, no repeats.",
    ),
    AIModule(
        name="Module 2 — Carousel (4 tiles): why this pack",
        role="a+_carousel",
        headline="WHY THIS PACK",
        body=(
            "Tile 1: <b>UNIQUE MIX OF FORMS</b> — 20 different plants, rosette to trailing.<br/>"
            "Tile 2: <b>FROST HARDY OUTDOORS</b> — to 0°F, USDA Zones 7 to 10.<br/>"
            "Tile 3: <b>ROOTED IN 2-INCH POTS</b> — established and ready to plant.<br/>"
            "Tile 4: <b>LOW-CARE SUCCULENTS</b> — drought tolerant, easy to propagate."
        ),
        visual="4 square tiles, green #78A848 accent corner per tile, line icons (grid · snowflake · pot · leaf). Real plant photography in each.",
        alt="Four-tile carousel: unique mix of forms, frost hardy, rooted in 2-inch pots, low-care succulents.",
    ),
    AIModule(
        name="Module 3 — Banner: the frost-proof tapestry",
        role="a+_banner",
        headline="A FROST-PROOF TAPESTRY",
        body=(
            "Planted together, the twenty mixed varieties form a tapestry of rosettes, "
            "spreading Sedum mats and a trailing edge — different forms, colors and "
            "textures. Tuck them among stones in a rock garden, fill a container, or "
            "plant them in the ground for a hardy display that holds through winter."
        ),
        visual="Wide banner: the mixed varieties planted among rocks in cool-season daylight, a light frost on a few tips. Honest, true color — never oversaturated.",
        alt="A+ banner: mixed hardy succulents forming a frost-proof tapestry in a sunlit rock garden.",
    ),
    AIModule(
        name="Module 4 — Banner: easy outdoor care",
        role="a+_banner",
        headline="HARDY, AND EASY TO KEEP",
        body=(
            "Give them full or partial sun in gritty, well-draining soil, and water deeply "
            "only after the soil dries out. They shrug off cold to 0°F once established and "
            "need little else. Many varieties are easy to propagate from offsets or stem "
            "cuttings, so a planting fills in over time."
        ),
        visual="Triptych: LEFT a rooted 2-inch pot, CENTER sun/water/soil/cold care icons, RIGHT an offset or cutting being replanted. Clean daylight, green accents.",
        alt="A+ triptych: rooted 2-inch pot, simple sun, soil and water care, and a cutting being replanted.",
    ),
    AIModule(
        name="Module 5 — Comparison: which pack is right for you",
        role="a+_comparison",
        headline="WHICH PACK IS RIGHT",
        body=(
            "Compare across three columns: <b>This Hardy Variety Pack</b> · Sempervivum "
            "Variety Pack · Trailing and Strings Pack.<br/><br/>"
            "Rows: Plant count · Assortment · Plant type · Hardiness · Made for.<br/><br/>"
            "<b>This Hardy Variety Pack:</b> 20 unique · all different, mixed forms · "
            "Sempervivum, Sedum and more · frost hardy to 0°F, Zones 7-10, outdoor · "
            "frost-proof landscaping and rock gardens.<br/>"
            "<b>Sempervivum Variety Pack:</b> 20 unique · all different, one genus · "
            "Sempervivum hens and chicks · cold-hardy to -20°F, Zones 5-10, outdoor · "
            "collecting and rosette displays.<br/>"
            "<b>Trailing and Strings Pack:</b> 12 plants · 6 varieties, 2 of each · "
            "trailing and tender · indoor or mild outdoor · hanging planters and cascading decor.<br/><br/>"
            "Want a hardy outdoor mix that survives winter? This is your pack. Want only "
            "hens and chicks? Choose the Sempervivum pack. Highlight the This column."
        ),
        visual="Amazon Premium Comparison Chart, 3 product columns, this-pack column highlighted teal #345C64. Sibling packs named by their pack name only.",
        alt="Comparison chart: this Hardy Variety Pack (mixed forms, to 0F) vs Sempervivum Variety (one genus, to -20F) vs Trailing and Strings (tender, indoor).",
    ),
    AIModule(
        name="Module 6 — Carousel (4 tiles): where they shine",
        role="a+_carousel",
        headline="WHERE THEY SHINE",
        body=(
            "Tile 1: <b>ROCK GARDENS</b> — mixed forms tucked among stones.<br/>"
            "Tile 2: <b>LANDSCAPING</b> — hardy groundcover and borders.<br/>"
            "Tile 3: <b>CONTAINERS</b> — a mixed bowl of hardy succulents.<br/>"
            "Tile 4: <b>DIY ARRANGEMENTS</b> — build your own outdoor planters."
        ),
        visual="4 identically composed use-case tiles, real outdoor plant scenes, green accent corner per tile, consistent natural daylight.",
        alt="Four-tile carousel of uses: rock gardens, landscaping, containers, and DIY arrangements.",
    ),
    AIModule(
        name="Module 7 — Premium Q&A",
        role="a+_qa",
        headline="COMMON QUESTIONS",
        body=(
            "<b>Q.</b> Will I get any duplicates?<br/>"
            "<b>A.</b> No. You receive 20 unique plants, all different — a hand-picked mix of "
            "hardy succulents with no repeats.<br/><br/>"
            "<b>Q.</b> How cold-hardy are they?<br/>"
            "<b>A.</b> This mix is frost-tolerant to at least 0°F and grows year-round outdoors "
            "in USDA Zones 7 to 10.<br/><br/>"
            "<b>Q.</b> What kinds of succulents are included?<br/>"
            "<b>A.</b> A hand-picked mix of hardy types, including Sempervivum and Sedum, in "
            "rosette, stemmed and trailing forms.<br/><br/>"
            "<b>Q.</b> Indoors or outdoors?<br/>"
            "<b>A.</b> These are built for outdoors in full or partial sun — ideal for rock "
            "gardens, landscaping, and containers.<br/><br/>"
            "<b>Q.</b> How is this different from the Sempervivum pack?<br/>"
            "<b>A.</b> This pack is a hardy MIX of types and forms, frost-hardy to 0°F. The "
            "Sempervivum Variety Pack is only hens and chicks and hardy to -20°F."
        ),
        visual="Vertical Q/A table, teal dividers between questions, small Q./A. labels in dark #414042.",
        alt="Premium Q&A module answering duplicates, hardiness, plant types, indoor vs outdoor, and Sempervivum difference.",
    ),
]


QA = [
    AIQA(q="Will I get any duplicate plants?",
         a="No. You receive 20 unique plants, all different, with no repeats. It is a hand-picked mix of hardy succulents chosen for diversity of types and forms, not multiples of the same plant."),
    AIQA(q="How cold-hardy are these succulents?",
         a="This mix is cold- and frost-tolerant to at least 0°F and grows year-round outdoors in USDA Zones 7 to 10. It is well suited to outdoor rock gardens, beds, and containers."),
    AIQA(q="What kinds of succulents are included?",
         a="A hand-picked mix of hardy types, including Sempervivum and Sedum and more, in rosette, stemmed and trailing forms with diverse colors, textures, and seasonal color changes."),
    AIQA(q="What size are the plants and how do they ship?",
         a="Each plant arrives fully rooted and established in its own 2-inch nursery pot. Packs ship with upright-handling labels and a printed care guide so they travel and settle in well."),
    AIQA(q="Should I keep them indoors or outdoors?",
         a="These are built for outdoors in full or partial sun. Use them in rock gardens, landscaping, containers, or DIY arrangements, in gritty, well-draining soil."),
    AIQA(q="How do I care for them?",
         a="Give them full or partial sun and gritty, well-draining soil, and water deeply only after the soil is completely dry. They are drought tolerant and low maintenance."),
    AIQA(q="How is this different from the Sempervivum Variety pack?",
         a="This Hardy Variety Pack is a mix of hardy types and forms, frost-tolerant to 0°F in Zones 7 to 10. The Sempervivum Variety Pack is only hens and chicks and cold-hardy to -20°F in Zones 5 to 10."),
    AIQA(q="Are these pet-safe, and can I propagate them?",
         a="Yes, the plants are pet-safe. Many of the varieties are easy to propagate from offsets or stem cuttings, so a planting can expand and fill in over time."),
    AIQA(q="Can I tell the varieties apart when they arrive?",
         a="Variety details or temperature tolerances are supplied on plant stakes or a legend, and a printed care guide is included so you can identify and place each one."),
]


# Backend KWs — US English, stem-deduped, byte-packed. No brand/title duplicates, no superlatives.
BACKEND = (
    "hardy succulents outdoor frost tolerant cold hardy sedum sempervivum hens chicks "
    "live plants assorted mix collection sampler rosette trailing groundcover perennial "
    "rock garden landscaping 2 inch pots rooted starter container drought tolerant low "
    "maintenance zone 7 winter pet safe real plant set arrangement diy recyclable"
)


def main() -> None:
    print("Loading Mountain Crest Gardens customer + parsing Hardy Variety Excel…")
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
