"""Mountain Crest Gardens — Sempervivum BULK PACK (25 = 5 of each) — Image Plan 05
Hand-written senior copy injected into the branded EQUALICE ReportLab pipeline.

Marketplace: amazon.com (US). Customer text + art direction both ENGLISH.

THIS PACK'S IDENTITY (the #1 job — make it crystal clear which pack this is):
  • Sempervivum ('hens & chicks') — rosette succulents.
  • BULK PACK = 25 plants, 5 cold-hardy varieties, 5 of EACH (MULTIPLES, not one of each).
    (Quantity of matching plants — to fill space, repeat a pattern, or resell.)
  • Cold-hardy to about -20°F, USDA Zone 5 and warmer, OUTDOOR (rock gardens, beds,
    living walls/roofs, containers, landscaping).
  • Fully rooted & established in 2-inch nursery pots.
  For: outdoor PROJECTS, landscaping, ground cover, and RESALE.

THE DISAMBIGUATION (client mandate): a dedicated "WHICH PACK IS RIGHT FOR YOU?"
comparison module positions THIS pack vs the siblings. The single most important
contrast buyers confuse: this BULK is 5 OF EACH (multiples to fill space / resell)
vs the 01 SEMPERVIVUM VARIETY (20 different, ONE of each — for collecting/diversity).
Same plant, opposite purpose. Also vs 03 Hardy Variety (a MIX of types, less hardy).
Disambiguating badges on the creative: "5 OF EACH x5",
"COLD-HARDY TO -20F", "FOR PROJECTS RESALE".

LANGUAGE: all art-direction fields (purpose, background, visual, props, lighting,
why_it_works, ctr, cvr, module visual) are designer-facing English. All customer
text (title, bullets, overlays, module headline/body, Q&A) is English too (US).

OVERLAY RULE: sell the OUTCOME / identity, not the action. Each overlay distinct,
≤30 chars AND ≤5 words, SMOOTH (no "Word? Word." fragments, no "·" middots —
middots count as words). overlay_sub ≤90 · module headline ≤38 · bullet head ≤45.

Verified facts (from listing.xlsx USPs + brand_study matrix):
  - 25 live Sempervivum, 5 cold-hardy varieties, 5 of each (multiples)
  - each plant fully rooted in its own 2-inch nursery pot
  - cold-hardy to about -20°F, USDA Zone 5 and warmer, outdoor
  - drought tolerant, low maintenance; water deeply only after soil fully dries
  - full sun or filtered/partial sun, gradual acclimation after delivery
  - classic rosette forms, seasonal mix of colors, textures, species, cultivars
  - well-established roots — ready to transplant or resell; can stay in pots temporarily
  - for rock gardens, containers, living walls/roofs, mini gardens, favors,
    landscaping and other outdoor projects; care guidance included

Review insight (VoC) used:
  praised  = healthy/gorgeous good-quality plants, careful live-plant packing,
             matched/exceeded listing photos, strong color variety, visible new growth,
             good for propagation (chicks), giftable, recommended seller / good value
  objection= rare arrival issue (white-fungus look / musty smell from shipping moisture),
             unclear seller contact, occasional single off plant in an order
             → defuse: rooted/established plants, ventilated live-arrival packing,
               handling labels, included care guide, easy acclimation steps

Compliance: no $/price, no URL/.com, no superlatives (best/#1/top/leading),
no false hardiness claims, no medical claims. Hardiness stated only as the
verified about -20°F / Zone 5 and warmer figures.
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
PLAN_NO = "05"
ASIN = "B0FK6V3ZKC"


# ===== KW-led, nursery-accurate US copy (customer-facing English) =====

# Title is HTML-escaped on render, so a literal "&" counts as 1 char. Keep ≤200 real chars.
TITLE = (
    "Mountain Crest Gardens Sempervivum Bulk Pack — 25 Live Hens and Chicks Plants, "
    "5 Varieties, 5 of Each, Rooted in 2 Inch Pots — Cold-Hardy Succulents for "
    "Outdoor Projects, Landscaping and Resale"
)

BULLETS = [
    "<b>25 PLANTS, 5 OF EACH</b> — Twenty-five live Sempervivum, five cold-hardy varieties "
    "with five of each. Matching multiples to fill a bed, repeat a pattern, or resell.",

    "<b>COLD-HARDY OUTDOORS TO -20F</b> — Thrives outside in USDA Zone 5 and warmer and "
    "takes about -20°F once established. Built for rock gardens, beds, and landscaping.",

    "<b>ROOTED IN 2-INCH POTS</b> — Each plant arrives fully rooted in its own 2-inch nursery "
    "pot, established and ready to transplant, plant out, or resell with margin.",

    "<b>LOW-CARE LIVE SUCCULENTS</b> — Drought tolerant and low maintenance. Full or partial "
    "sun, water deeply only after the soil dries out. They send out chicks you can replant.",

    "<b>MADE FOR OUTDOOR PROJECTS</b> — Hens and chicks rosettes for ground cover, living "
    "walls and roofs, containers, favors, and resale. Care guidance included with every pack.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B test)",
        role="hero",
        background="Pure white #FFFFFF seamless (Amazon main-image policy — main hero shows no overlay text). For the badge-bearing alt options, a clean light backdrop #ECEFF4. True-to-life plant color, never oversaturated.",
        purpose="Win the click in the amazon.com live-succulent grid — instantly read as a BULK quantity of matching hardy rosettes (5 of each), not a one-of-each sampler.",
        visual=(
            "Real, accurate Sempervivum photography in true natural color. Designer mocks ALL 3 "
            "options; brand picks the winner via Amazon Manage Your Experiments. One callout, one "
            "idea, one clean layout each.\n\n"
            "▸ OPTION A — THE QUANTITY GRID (wins on the 5-of-each promise)\n"
            "Clean overhead 5x5 grid of the 25 plants in their 2-inch nursery pots, grouped so each "
            "of the 5 varieties shows as a row of 5 identical rosettes — the eye instantly reads "
            "'multiples, 5 of each'. (Compliant alt: badge top-right '5 OF EACH x5' in teal #345C64.)\n\n"
            "▸ OPTION B — CLEAN MAIN (Amazon-policy main image)\n"
            "Pure white background, a full tray of 25 rooted 2-inch pots stacked into frame, ~85% of "
            "frame, soft contact shadow, one pot turned to show the nursery pot. NO overlay text.\n\n"
            "▸ OPTION C — FILLING THE BED (wins on the project use)\n"
            "The matching rosettes planted in repeating drifts across a sunlit rock-garden bed, hands "
            "setting one pot into a gap for scale. (Compliant alt: badge bottom-left 'COLD-HARDY TO -20F'.)\n\n"
            "All 3: plants dominant, honest color, nursery-grade and real — never a staged stock look."
        ),
        overlay="25 PLANTS 5 OF EACH",
        overlay_sub="Five cold-hardy varieties, five of each — matching multiples for outdoor projects.",
        props=[
            "OPTION A: overhead 5x5 grid grouped as 5 varieties x 5 in 2-inch pots",
            "OPTION B: pure-white full tray of 25 rooted 2-inch pots (no text)",
            "OPTION C: matching rosettes planted in drifts across a rock-garden bed, hand for scale",
        ],
        lighting="Bright, even, daylight-balanced (5000-5500K) so rosette color stays true and accurate. No warm cast, no saturation push.",
        why_it_works=(
            "Rows of five identical rosettes make the core promise — 5 of each — readable on a mobile "
            "thumbnail and separate this bulk project pack from the one-of-each variety sampler in the "
            "same grid."
        ),
        ctr="Grouped multiples telegraph 'quantity / 5 of each' faster than any single pot shot, pulling landscapers and resellers out of the live-succulent grid.",
        cvr="Seeing 5 of each variety up front sets an honest expectation, matches the photos buyers praise, and pre-answers 'is this multiples or one of each?' — cutting bounce and wrong-pack returns.",
    ),
    AIImagePlanItem(
        name="Image 2 — Spec / identity card (what's in the box)",
        role="educate",
        background="Light #ECEFF4 panel with a teal #345C64 footer band. Clean nursery-grade layout.",
        purpose="Pin down the exact identity and count so buyers know precisely which pack this is before they scroll.",
        visual=(
            "Spec card. Center: the 5-variety x5 quantity-grid thumbnail. Four labeled spec tiles "
            "with thin teal line icons:\n"
            "  • COUNT — 25 plants, 5 of each\n"
            "  • TYPE — Sempervivum (hens & chicks)\n"
            "  • HARDINESS — Zone 5 and warmer, to -20F, outdoor\n"
            "  • POTS — fully rooted, 2-inch nursery pots\n"
            "Footer band carries the disambiguation line. A small ruler/coin cue for pot scale."
        ),
        overlay="KNOW THIS PACK",
        overlay_sub="25 Sempervivum, 5 of each variety, rooted in 2-inch pots, hardy outdoors.",
        props=["5-variety x5 quantity-grid thumbnail", "4 spec tiles with line icons", "teal footer band", "coin or ruler for pot scale"],
        lighting="Flat, clean studio light — legibility over atmosphere.",
        why_it_works=(
            "Converts the listing's hard facts into a single scannable identity card, so a shopper "
            "comparing the seven Mountain Crest packs can confirm count, type, hardiness and pot size "
            "at a glance — the heart of the client's disambiguation mandate."
        ),
        ctr="A clear spec card reassures detail-driven project and reseller buyers and earns the scroll into the gallery.",
        cvr="Removing every 'what exactly do I get?' question up front shortens the decision and reduces wrong-pack returns.",
    ),
    AIImagePlanItem(
        name="Image 3 — Hook: multiples to fill space (5 of each)",
        role="hook",
        background="Clean light #ECEFF4 with the grouped quantity grid as the focal point.",
        purpose="Make the 5-of-each, multiples idea unmistakable — the reason to choose THIS pack over the sampler.",
        visual=(
            "The grid grouped into 5 labeled rows, each row showing 5 identical rosettes of one "
            "variety in 2-inch pots — so '5 of each' reads instantly. A thin teal bracket spans one "
            "row marked 'x5'. Small caption strip: 'five of each variety, ready to repeat'."
        ),
        overlay="FIVE OF EACH",
        overlay_sub="Five matching plants per variety — multiples to fill space and resell.",
        props=["5 labeled rows of 5 identical rosettes", "teal 'x5' bracket over one row", "2-inch pots throughout"],
        lighting="Bright daylight-balanced, true color across every rosette.",
        why_it_works=(
            "Doubles down on the single strongest differentiator versus the variety pack: this is "
            "multiples of each plant, not one of each — exactly what landscapers, project buyers and "
            "resellers are searching for."
        ),
        ctr="'Five of each' is the promise project buyers scan for; the grouped rows prove it at a glance.",
        cvr="Buyers who specifically want matching quantity self-select here, raising fit and satisfaction.",
    ),
    AIImagePlanItem(
        name="Image 4 — Desire: a filled, planted outdoor scene",
        role="desire",
        background="A real, sunlit rock garden or planted bed — stones, gravel, natural daylight.",
        purpose="Sell the dream outcome — enough matching hardy rosettes to fill a bed or wall and finish a project.",
        visual=(
            "Hero lifestyle shot: the matching rosettes planted in repeating drifts across a rock "
            "garden or a vertical living wall, filling the space with a cohesive carpet of rosettes "
            "and seasonal color. A few mature rosettes sending up pink flower stalks. Natural, honest "
            "color — never oversaturated. Real outdoor scene."
        ),
        overlay="FILL THE SPACE",
        overlay_sub="Enough matching rosettes to carpet a bed, wall, or roof with hardy color.",
        props=["matching rosettes planted in repeating drifts", "living wall or rock-garden bed", "pink flower stalks on mature rosettes"],
        lighting="Natural late-morning daylight, soft directional sun for rosette dimension, accurate color.",
        why_it_works=(
            "Shows the payoff buyers actually want — a fully covered, cohesive outdoor planting — and "
            "matches the cold-hardy, project-scale use this bulk Sempervivum pack is built for."
        ),
        ctr="A filled, finished bed is aspirational for landscapers and project buyers and stands out in the grid.",
        cvr="A realistic, covered result sets correct expectations and pictures the buyer's own finished project.",
    ),
    AIImagePlanItem(
        name="Image 5 — Educate: easy outdoor care",
        role="educate",
        background="White with a green accent band #78A848 in the footer.",
        purpose="Show the plants are low-maintenance and hardy, lowering the 'will they survive the project?' barrier.",
        visual=(
            "Headline at top, then a clean 4-step care row with line icons:\n"
            "  • SUN — full or partial sun\n"
            "  • WATER — only after soil is fully dry\n"
            "  • COLD — hardy to -20F, Zone 5 and up\n"
            "  • CHICKS — separate offsets and replant\n"
            "Footer band carries 'care guidance included'. A rooted 2-inch pot anchors the side, plus "
            "a small 'acclimate gradually after delivery' note."
        ),
        overlay="HARDY AND LOW CARE",
        overlay_sub="Full or partial sun, water only when dry, hardy outdoors to about -20F.",
        props=["4 care-step icons", "rooted 2-inch nursery pot", "green footer band", "offset 'chick' detail", "acclimation note"],
        lighting="Flat, clean studio light for legibility.",
        why_it_works=(
            "Turns the USP care facts into a confidence builder for project buyers, while the "
            "chicks/offsets note signals the plants multiply over time — useful for landscaping and resale."
        ),
        ctr="Drought-tolerant, low-maintenance care is a top reassurance for live-plant and project shoppers scanning the gallery.",
        cvr="Clear, simple care plus acclimation steps lower the perceived risk of a bulk live-plant order and support the purchase.",
    ),
    AIImagePlanItem(
        name="Image 6 — WHICH PACK IS RIGHT FOR YOU? (sibling comparison)",
        role="educate",
        background="Light #ECEFF4 with a teal #345C64 header bar. Clean comparison layout.",
        purpose="Disambiguate THIS bulk pack from the sibling Mountain Crest packs so buyers pick the right one (the client's #1 ask).",
        visual=(
            "A 3-column compare card (this pack highlighted in teal). Columns and rows:\n"
            "  Row labels: PLANTS · ASSORTMENT · TYPE · HARDINESS · MADE FOR\n"
            "  COL 1 (highlighted) — THIS · Sempervivum Bulk: '25 plants' · '5 varieties, 5 of each' · "
            "'Sempervivum' · 'to -20F, Zone 5 and up, outdoor' · 'Projects, landscaping, resale'\n"
            "  COL 2 — Sempervivum Variety: '20 plants' · '20 different, one of each' · 'Sempervivum' · "
            "'to -20F, Zone 5-10' · 'Collecting, diverse displays'\n"
            "  COL 3 — Hardy Variety: '20 plants' · 'mixed types, all different' · "
            "'Sempervivum + Sedum + more' · 'to 0F, Zone 7-10' · 'Frost-tolerant landscaping'\n"
            "Caption under it: 'Need multiples to fill space or resell? This is your pack.'"
        ),
        overlay="WHICH PACK IS RIGHT",
        overlay_sub="Need multiples to fill space? Choose this. Want one of each? See the variety pack.",
        props=["3-column comparison card", "this-pack column highlighted teal", "row icons: count, assortment, type, hardiness, use"],
        lighting="Flat, clean studio light — table must be legible on a phone.",
        why_it_works=(
            "Directly fulfills the disambiguation mandate: it positions this bulk pack (25 = 5 of each "
            "— for projects and resale) against the variety pack (20 different, one of each — for "
            "collecting) and the mixed Hardy Variety, so buyers self-route to the right pack."
        ),
        ctr="Shoppers cross-shopping the Mountain Crest packs stop here to settle which one fits, raising qualified clicks.",
        cvr="Pre-empting the 'is this multiples or one of each?' confusion sharply cuts wrong-pack returns.",
    ),
    AIImagePlanItem(
        name="Image 7 — Trust / Close: real nursery, healthy arrival",
        role="trust",
        background="Clean nursery scene: trays of rooted 2-inch pots, soft daylight.",
        purpose="Build arrival confidence and close on the family-nursery promise; quietly defuse the rare fungus/musty objection.",
        visual=(
            "Two-part. LEFT: trays of healthy, established rosettes in 2-inch pots with visible new "
            "growth, plus the ventilated live-plant box with upright-handling labels and the care "
            "guide. RIGHT: a small trust strip — 'rooted & established' · 'packed for live arrival' · "
            "'care guidance included' · 'ready to transplant or resell'. Hands (no face) lifting one "
            "pot for scale. Honest, nursery-grade — a real licensed succulent nursery, not a kiosk."
        ),
        overlay="REAL NURSERY PLANTS",
        overlay_sub="Rooted and established, packed for live arrival, with care guidance included.",
        props=["trays of rooted 2-inch pots with new growth", "ventilated live-plant box with handling labels", "printed care guide", "hands lifting a pot (no face)"],
        lighting="Soft natural daylight, accurate color, lived-in nursery feel — not staged stock.",
        why_it_works=(
            "Closes on the brand promise (real plants, real nursery, real help) and addresses the only "
            "recurring negatives — occasional shipping-moisture issues — by foregrounding rooted, "
            "established plants, ventilated live-arrival packing and the included care guidance."
        ),
        ctr="The healthy-plants-and-care-guide trust strip reassures buyers wary of a bulk mail-order live-plant order.",
        cvr="Visible plant health, ventilated live-arrival packing and included care guidance answer the top arrival worry and seal the purchase.",
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Brand banner",
        role="a+_banner",
        headline="25 PLANTS, 5 OF EACH",
        body=(
            "Twenty-five live Sempervivum plants — five cold-hardy varieties, five of each. "
            "Hardy hens and chicks rooted in 2-inch nursery pots, cold-hardy outdoors to "
            "about -20°F in USDA Zone 5 and warmer. Matching multiples for outdoor projects, "
            "landscaping, ground cover, and resale."
        ),
        visual="Wide cinematic overhead of the 25 pots grouped as 5 varieties x 5 in 2-inch pots, true natural color, teal #345C64 wordmark top-left. Clean light background.",
        alt="Overhead grid of 25 Sempervivum in 2-inch nursery pots, five varieties with five of each.",
    ),
    AIModule(
        name="Module 2 — Carousel (4 tiles): why this pack",
        role="a+_carousel",
        headline="WHY THIS PACK",
        body=(
            "Tile 1: <b>FIVE OF EACH</b> — 5 varieties, 5 matching plants of each.<br/>"
            "Tile 2: <b>COLD-HARDY OUTDOORS</b> — to about -20°F, Zone 5 and up.<br/>"
            "Tile 3: <b>ROOTED IN 2-INCH POTS</b> — established and ready to plant.<br/>"
            "Tile 4: <b>BUILT FOR PROJECTS</b> — landscaping, ground cover, resale."
        ),
        visual="4 square tiles, green #78A848 accent corner per tile, line icons (multiples · snowflake · pot · trowel). Real plant photography in each.",
        alt="Four-tile carousel: five of each, cold-hardy, rooted in 2-inch pots, built for projects.",
    ),
    AIModule(
        name="Module 3 — Banner: fill the space",
        role="a+_banner",
        headline="ENOUGH TO FILL THE SPACE",
        body=(
            "With five of each variety, you have enough matching rosettes to carpet a bed, "
            "edge a path, cover a living wall or roof, or repeat a pattern. Planted together "
            "they form a cohesive tapestry of rosette forms and seasonal color — and mature "
            "rosettes can even send up pink flower stalks."
        ),
        visual="Wide banner: matching rosettes planted in repeating drifts across a sunlit rock garden or living wall, a few pink flower stalks. Honest, true color — never oversaturated.",
        alt="A+ banner: matching Sempervivum rosettes filling a rock-garden bed and living wall.",
    ),
    AIModule(
        name="Module 4 — Banner: easy outdoor care",
        role="a+_banner",
        headline="HARDY, AND EASY TO KEEP",
        body=(
            "Give them full or partial sun and water deeply only after the soil dries out. "
            "They shrug off cold to about -20°F once established and need little else. Acclimate "
            "them gradually after delivery, and over time each plant sends out chicks you can "
            "separate and replant to expand a planting."
        ),
        visual="Triptych: LEFT a rooted 2-inch pot, CENTER sun/water/cold care icons, RIGHT an offset 'chick' being replanted. Clean daylight, green accents.",
        alt="A+ triptych: rooted 2-inch pot, simple sun and water care, and a chick offset being replanted.",
    ),
    AIModule(
        name="Module 5 — Comparison: which pack is right for you",
        role="a+_comparison",
        headline="WHICH PACK IS RIGHT",
        body=(
            "Compare across three columns: <b>This Sempervivum Bulk</b> · Sempervivum Variety "
            "Pack · Hardy Variety Pack.<br/><br/>"
            "Rows: Plant count · Assortment · Plant type · Hardiness · Made for.<br/><br/>"
            "<b>This Sempervivum Bulk:</b> 25 plants · 5 varieties, 5 of each · Sempervivum · "
            "to about -20°F, Zone 5 and up, outdoor · projects, landscaping, and resale.<br/>"
            "<b>Sempervivum Variety Pack:</b> 20 plants · 20 different, one of each · Sempervivum · "
            "to -20°F, Zones 5-10 · collecting and diverse displays.<br/>"
            "<b>Hardy Variety Pack:</b> 20 plants · mixed types, all different · Sempervivum, "
            "Sedum and more · to 0°F, Zones 7-10 · frost-tolerant landscaping.<br/><br/>"
            "Need multiples to fill space or resell? This is your pack. Want one of each to "
            "collect? Choose the variety pack instead. Highlight the This column."
        ),
        visual="Amazon Premium Comparison Chart, 3 product columns, this-pack column highlighted teal #345C64. Sibling packs named by their pack name only.",
        alt="Comparison chart: this Sempervivum Bulk (5 of each) vs Variety Pack (one of each) vs Hardy Variety Pack (mixed types).",
    ),
    AIModule(
        name="Module 6 — Carousel (4 tiles): where they shine",
        role="a+_carousel",
        headline="WHERE THEY SHINE",
        body=(
            "Tile 1: <b>GROUND COVER</b> — matching rosettes carpet a bed.<br/>"
            "Tile 2: <b>LIVING WALLS AND ROOFS</b> — fill vertical plantings.<br/>"
            "Tile 3: <b>LANDSCAPING</b> — edge paths and rock gardens.<br/>"
            "Tile 4: <b>RESALE AND FAVORS</b> — rooted pots ready to move."
        ),
        visual="4 identically composed use-case tiles, real outdoor plant scenes, green accent corner per tile, consistent natural daylight.",
        alt="Four-tile carousel of uses: ground cover, living walls and roofs, landscaping, and resale or favors.",
    ),
    AIModule(
        name="Module 7 — Premium Q&A",
        role="a+_qa",
        headline="COMMON QUESTIONS",
        body=(
            "<b>Q.</b> How many of each variety do I get?<br/>"
            "<b>A.</b> You receive 25 plants as five cold-hardy varieties with five of each — "
            "matching multiples, not one of each.<br/><br/>"
            "<b>Q.</b> How cold-hardy are they?<br/>"
            "<b>A.</b> Sempervivum are cold-hardy outdoors in USDA Zone 5 and warmer and tolerate "
            "about -20°F once established.<br/><br/>"
            "<b>Q.</b> What size are the plants?<br/>"
            "<b>A.</b> Each plant arrives fully rooted in its own 2-inch nursery pot, established "
            "and ready to transplant or resell.<br/><br/>"
            "<b>Q.</b> Can I resell them or hold them in the pots?<br/>"
            "<b>A.</b> Yes. The roots are well established, so plants can be transplanted, resold, "
            "or kept in their original pots temporarily with proper care.<br/><br/>"
            "<b>Q.</b> How is this different from the variety pack?<br/>"
            "<b>A.</b> This bulk pack gives 5 of each variety for projects and resale. The "
            "Sempervivum Variety Pack gives 20 different varieties, one of each, for collecting."
        ),
        visual="Vertical Q/A table, teal dividers between questions, small Q./A. labels in dark #414042.",
        alt="Premium Q&A module answering quantity per variety, hardiness, pot size, resale, and variety-pack difference.",
    ),
]


QA = [
    AIQA(q="How many of each variety do I get?",
         a="You receive 25 plants supplied as five cold-hardy varieties with five plants of each. They are matching multiples, made for filling space and resale, not one of each."),
    AIQA(q="How cold-hardy are these Sempervivum?",
         a="They are cold-hardy outdoors in USDA Zone 5 and warmer and tolerate about -20°F once established. They are well suited to outdoor rock gardens, beds, and landscaping."),
    AIQA(q="What size are the plants and how do they ship?",
         a="Each plant arrives fully rooted in its own 2-inch nursery pot. Packs ship in ventilated live-plant packaging with upright-handling labels and care guidance, so they travel and settle in well."),
    AIQA(q="Can I resell these or keep them in the pots for a while?",
         a="Yes. The roots are well established, so the plants are ready to transplant or resell, and they can stay in their original 2-inch pots temporarily with proper care."),
    AIQA(q="Indoors or outdoors, and how do I care for them?",
         a="These thrive outdoors in full or partial sun. Acclimate them gradually after delivery, and water deeply only after the soil is completely dry. They are drought tolerant and low maintenance."),
    AIQA(q="How is this different from the Sempervivum Variety Pack?",
         a="This Bulk pack is five varieties with five of each, made for projects, landscaping, and resale. The Sempervivum Variety Pack is 20 different varieties, one of each, made for collecting and diverse displays."),
    AIQA(q="What can I use this bulk pack for?",
         a="It suits ground cover, living walls and roofs, container plantings, mini gardens, favors, landscaping, and resale, anywhere you want a quantity of matching hardy rosettes."),
    AIQA(q="Will the plants multiply over time?",
         a="Yes. Mature rosettes produce offsets, called chicks, that you can separate and replant, so a planting can expand and fill in over time."),
]


# Backend KWs — US English, stem-deduped, byte-packed. No brand/title duplicates, no superlatives.
BACKEND = (
    "sempervivum hens and chicks succulents live plants hardy rosette cold hardy outdoor "
    "rock garden groundcover ground cover perennial bulk wholesale assortment multiples "
    "2 inch pots rooted starter container living wall roof landscaping resale project "
    "drought tolerant low maintenance sedum houseleek zone 5 winter hardy favors pet safe"
)


def main() -> None:
    print("Loading Mountain Crest Gardens customer + parsing Sempervivum Bulk Excel…")
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
