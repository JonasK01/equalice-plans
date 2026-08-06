"""Mountain Crest Gardens — Sempervivum VARIETY PACK (20, no repeats) — Image Plan 01
Hand-written senior copy injected into the branded EQUALICE ReportLab pipeline.

Marketplace: amazon.com (US). Customer text + art direction both ENGLISH.

THIS PACK'S IDENTITY (the #1 job — make it crystal clear which pack this is):
  • Sempervivum ('hens & chicks') — rosette succulents.
  • VARIETY PACK = 20 plants, 20 DIFFERENT varieties, ONE of each, NO repeats.
    (A sampler / collector set — maximum diversity, not multiples.)
  • Cold-hardy to -20°F, USDA Zone 5-10, OUTDOOR (rock gardens, in-ground, containers).
  • Fully rooted & established in 2-inch nursery pots.
  For: collectors, rock gardens, diverse rosette displays.

THE DISAMBIGUATION (client mandate): a dedicated "WHICH PACK IS RIGHT FOR YOU?"
comparison module positions THIS pack vs the siblings. The single most important
contrast for buyers: this VARIETY pack (20 different, one of each — for COLLECTING /
diversity) vs the 05 SEMPERVIVUM BULK (25 = 5 of each — for PROJECTS / landscaping /
resale); also vs 03 Hardy Variety (a MIX of types, not all Sempervivum).
Disambiguating badges live on the creative: "20 VARIETIES NO REPEATS",
"COLD-HARDY TO -20F", "OUTDOOR ZONE 5-10".

LANGUAGE: all art-direction fields (purpose, background, visual, props, lighting,
why_it_works, ctr, cvr, module visual) are designer-facing English. All customer
text (title, bullets, overlays, module headline/body, Q&A) is English too (US).

OVERLAY RULE: sell the OUTCOME / identity, not the action. Each overlay distinct,
≤30 chars AND ≤5 words, SMOOTH (no "Word? Word." fragments, no "·" middots —
middots count as words). overlay_sub ≤90 · module headline ≤38 · bullet head ≤45.

Verified facts (from listing.xlsx USPs + brand_study matrix):
  - 20 live Sempervivum, 20 different varieties, one of each, no repeats
  - fully rooted & established in its own 2-inch nursery pot
  - cold-hardy USDA Zones 5-10, tolerant to at least -20°F once established
  - drought tolerant, low maintenance; water deeply only after soil is fully dry
  - rosette growth, diverse forms & seasonal colors; mature plants can send pink stalks
  - best in full sun to partial sun; containers, rock gardens, mini gardens, in-ground
  - produces offsets ("chicks") easy to separate & replant
  - pet-safe; printed care guide included; variety names on stakes / a legend

Review insight (VoC) used:
  praised  = healthy plants, visible new growth, attractive color variety, matched photos, great gift
  objection= rare arrival issue (white fungus / musty smell from shipping moisture)
             → defuse: live-plant packing, clear handling labels, easy care-guide recovery

Compliance: no $/price, no URL/.com, no superlatives (best/#1/top/leading),
no false hardiness claims, no medical claims. Hardiness stated only as the
verified -20°F / Zone 5-10 figures.
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
PLAN_NO = "01"
ASIN = "B0FK6C91NH"


# ===== KW-led, nursery-accurate US copy (customer-facing English) =====

# Title is HTML-escaped on render, so a literal "&" counts as 1 char. Keep ≤200 real chars.
TITLE = (
    "Mountain Crest Gardens Sempervivum Variety Pack — 20 Live Hens and Chicks Plants, "
    "20 Different Varieties, No Repeats, Rooted in 2 Inch Pots — Cold-Hardy Succulents "
    "for Outdoor Rock Gardens"
)

BULLETS = [
    "<b>20 VARIETIES, NO REPEATS</b> — Twenty live Sempervivum plants, twenty different "
    "varieties, one of each. A ready-made collection of hardy hens and chicks rosettes.",

    "<b>COLD-HARDY OUTDOORS TO -20F</b> — Thrives outside in USDA Zones 5 to 10 and takes at "
    "least -20°F once established. Built for rock gardens, in-ground beds, and containers.",

    "<b>ROOTED IN 2-INCH POTS</b> — Each plant arrives fully rooted and established in its own "
    "2-inch nursery pot, ready to display, repot, or plant straight into the garden.",

    "<b>LOW-CARE LIVE SUCCULENTS</b> — Drought tolerant and low maintenance. Full to partial "
    "sun, water deeply only after the soil dries out. They send out chicks you can replant.",

    "<b>A LIVING ROSETTE MOSAIC</b> — Diverse forms and seasonal colors make a collectible "
    "display for rock gardens and mini gardens. Pet-safe, with a printed care guide included.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B test)",
        role="hero",
        background="Pure white #FFFFFF seamless (Amazon main-image policy — main hero shows no overlay text). For the badge-bearing alt options, a clean light backdrop #ECEFF4. True-to-life plant color, never oversaturated.",
        purpose="Win the click in the amazon.com live-succulent grid — instantly read as a COLLECTOR set of 20 different hardy rosettes, not a tray of duplicates.",
        visual=(
            "Real, accurate Sempervivum photography in true natural color. Designer mocks ALL 3 "
            "options; brand picks the winner via Amazon Manage Your Experiments. One callout, one "
            "idea, one clean layout each.\n\n"
            "▸ OPTION A — THE GRID OF 20 (wins on the no-repeats promise)\n"
            "Clean overhead 4x5 grid of the actual 20 different varieties in their 2-inch nursery "
            "pots — every rosette visibly distinct (greens, reds, silvers, cobweb forms). Reads as "
            "a sampler at a glance. (Compliant alt: badge top-right 'NO REPEATS' in teal #345C64.)\n\n"
            "▸ OPTION B — CLEAN MAIN (Amazon-policy main image)\n"
            "Pure white background, a tight cluster of several distinct rosettes plus one 2-inch pot "
            "turned to show the nursery pot, ~85% of frame, soft contact shadow. NO overlay text.\n\n"
            "▸ OPTION C — IN THE ROCK GARDEN (wins on the outdoor use)\n"
            "The varieties nestled among stones in a sunlit rock garden, a hand placing one pot for "
            "scale. (Compliant alt: badge bottom-left 'COLD-HARDY TO -20F'.)\n\n"
            "All 3: plants dominant, honest color, nursery-grade and real — never a staged stock look."
        ),
        overlay="20 VARIETIES NO REPEATS",
        overlay_sub="Twenty different hardy hens and chicks, one of each, rooted in 2-inch pots.",
        props=[
            "OPTION A: overhead 4x5 grid of 20 distinct varieties in 2-inch pots",
            "OPTION B: pure-white cluster of rosettes + one 2-inch nursery pot (no text)",
            "OPTION C: varieties in a sunlit rock garden + a hand placing one pot for scale",
        ],
        lighting="Bright, even, daylight-balanced (5000-5500K) so rosette color stays true and accurate. No warm cast, no saturation push.",
        why_it_works=(
            "The grid of twenty visibly different rosettes makes the core promise — 20 varieties, no "
            "repeats — readable on a mobile thumbnail and separates this collector pack from the "
            "duplicate-heavy bulk packs in the same grid."
        ),
        ctr="A grid of twenty clearly different rosettes telegraphs 'collection / one of each' faster than any plain pot shot, pulling collectors and rock-garden buyers out of the live-succulent grid.",
        cvr="Seeing all 20 distinct varieties up front sets an honest expectation, matches the listing photos buyers praise, and pre-answers 'will I get repeats?' — cutting bounce and returns.",
    ),
    AIImagePlanItem(
        name="Image 2 — Spec / identity card (what's in the box)",
        role="educate",
        background="Light #ECEFF4 panel with a teal #345C64 footer band. Clean nursery-grade layout.",
        purpose="Pin down the exact identity and count so buyers know precisely which pack this is before they scroll.",
        visual=(
            "Spec card. Center: the 20-variety grid thumbnail. Four labeled spec tiles with thin "
            "teal line icons:\n"
            "  • COUNT — 20 plants, one of each\n"
            "  • TYPE — Sempervivum (hens & chicks)\n"
            "  • HARDINESS — Zone 5-10, to -20F, outdoor\n"
            "  • POTS — fully rooted, 2-inch nursery pots\n"
            "Footer band carries the disambiguation line. A small ruler/coin cue for pot scale."
        ),
        overlay="KNOW THIS PACK",
        overlay_sub="20 different Sempervivum, one of each, rooted in 2-inch pots, hardy outdoors.",
        props=["20-variety grid thumbnail", "4 spec tiles with line icons", "teal footer band", "coin or ruler for pot scale"],
        lighting="Flat, clean studio light — legibility over atmosphere.",
        why_it_works=(
            "Converts the listing's hard facts into a single scannable identity card, so a shopper "
            "comparing the seven Mountain Crest packs can confirm count, type, hardiness and pot size "
            "at a glance — the heart of the client's disambiguation mandate."
        ),
        ctr="A clear spec card reassures detail-driven plant buyers and earns the scroll into the gallery.",
        cvr="Removing every 'what exactly do I get?' question up front shortens the decision and reduces wrong-pack returns.",
    ),
    AIImagePlanItem(
        name="Image 3 — Hook: the collector promise (one of each)",
        role="hook",
        background="Clean light #ECEFF4 with the 20-grid as the focal point.",
        purpose="Make the no-repeats, one-of-each idea unmistakable — the reason to choose THIS pack.",
        visual=(
            "The full 4x5 grid of 20 distinct rosettes, each in its 2-inch pot, with a thin teal "
            "checkmark on every cell to dramatize 'all different'. A single highlighted cell pulled "
            "out slightly to show a named stake. Small caption strip: 'every plant a different variety'."
        ),
        overlay="ONE OF EACH",
        overlay_sub="Twenty different varieties, no duplicates — a sampler for collectors.",
        props=["4x5 grid of 20 distinct rosettes", "teal checkmarks per cell", "one named variety stake pulled forward"],
        lighting="Bright daylight-balanced, true color across every rosette.",
        why_it_works=(
            "Doubles down on the single strongest differentiator versus the bulk packs: this is "
            "twenty different plants, not multiples — exactly what collectors and diverse-display "
            "buyers are searching for."
        ),
        ctr="'One of each' is the promise collectors scan for; the all-different grid proves it instantly.",
        cvr="Buyers who specifically want diversity self-select here, raising fit and satisfaction.",
    ),
    AIImagePlanItem(
        name="Image 4 — Desire: the living rosette mosaic outdoors",
        role="desire",
        background="A real, sunlit rock garden — stones, gravel, natural daylight.",
        purpose="Sell the dream outcome — a thriving, collectible mosaic of rosettes growing outdoors.",
        visual=(
            "Hero lifestyle shot: many of the varieties planted together among rocks, forming a "
            "tapestry of different rosette forms and seasonal colors. A few mature rosettes sending "
            "up pink flower stalks. Natural, honest color — never oversaturated. Real outdoor scene."
        ),
        overlay="A LIVING ROSETTE MOSAIC",
        overlay_sub="Diverse rosettes thrive together in rock gardens, beds, and containers.",
        props=["mixed varieties planted among rocks", "pink flower stalks on mature rosettes", "natural gravel and stone"],
        lighting="Natural late-morning daylight, soft directional sun for rosette dimension, accurate color.",
        why_it_works=(
            "Shows the payoff buyers actually want — a diverse, living display thriving outdoors — "
            "and matches the cold-hardy, rock-garden use this Sempervivum pack is built for."
        ),
        ctr="The vivid-but-honest mosaic is aspirational for rock-garden and collector buyers and stands out in the grid.",
        cvr="A realistic in-garden result sets correct expectations and pictures the buyer's own future display.",
    ),
    AIImagePlanItem(
        name="Image 5 — Educate: easy outdoor care",
        role="educate",
        background="White with a green accent band #78A848 in the footer.",
        purpose="Show the plants are low-maintenance and hardy, lowering the 'will I keep them alive?' barrier.",
        visual=(
            "Headline at top, then a clean 4-step care row with line icons:\n"
            "  • SUN — full to partial sun\n"
            "  • WATER — only after soil is fully dry\n"
            "  • COLD — hardy to -20F, Zone 5-10\n"
            "  • CHICKS — separate offsets and replant\n"
            "Footer band carries 'printed care guide included'. A rooted 2-inch pot anchors the side."
        ),
        overlay="HARDY AND LOW CARE",
        overlay_sub="Full sun to part sun, water only when dry, hardy outdoors to -20F.",
        props=["4 care-step icons", "rooted 2-inch nursery pot", "green footer band", "offset 'chick' detail"],
        lighting="Flat, clean studio light for legibility.",
        why_it_works=(
            "Turns the USP care facts into a confidence builder for first-time succulent buyers, while "
            "the chicks/offsets note signals long-term value as the collection multiplies."
        ),
        ctr="Drought-tolerant, low-maintenance care is a top reassurance for live-plant shoppers scanning the gallery.",
        cvr="Clear, simple care lowers the perceived risk of keeping live plants and supports the purchase.",
    ),
    AIImagePlanItem(
        name="Image 6 — WHICH PACK IS RIGHT FOR YOU? (sibling comparison)",
        role="educate",
        background="Light #ECEFF4 with a teal #345C64 header bar. Clean comparison layout.",
        purpose="Disambiguate THIS pack from the sibling Mountain Crest packs so buyers pick the right one (the client's #1 ask).",
        visual=(
            "A 3-column compare card (this pack highlighted in teal). Columns and rows:\n"
            "  Row labels: PLANTS · ASSORTMENT · TYPE · HARDINESS · MADE FOR\n"
            "  COL 1 (highlighted) — THIS · Variety Pack: '20 plants' · '20 different, one of each' · "
            "'Sempervivum' · 'to -20F, Zone 5-10, outdoor' · 'Collecting, diverse displays'\n"
            "  COL 2 — Sempervivum Bulk: '25 plants' · '5 varieties, 5 of each' · 'Sempervivum' · "
            "'to -20F, outdoor' · 'Projects, landscaping, resale'\n"
            "  COL 3 — Hardy Variety: '20 plants' · 'mixed types, all different' · "
            "'Sempervivum + Sedum + more' · 'to 0F, Zone 7-10' · 'Frost-proof landscaping'\n"
            "Caption under it: 'Want one of each to collect? This is your pack.'"
        ),
        overlay="WHICH PACK IS RIGHT",
        overlay_sub="One of each to collect? Choose this. Need multiples for projects? See the bulk pack.",
        props=["3-column comparison card", "this-pack column highlighted teal", "row icons: count, assortment, type, hardiness, use"],
        lighting="Flat, clean studio light — table must be legible on a phone.",
        why_it_works=(
            "Directly fulfills the disambiguation mandate: it positions the variety pack (20 different, "
            "one of each — for collecting) against the Sempervivum bulk (25 = 5 of each — for projects "
            "and resale) and the mixed Hardy Variety, so buyers self-route to the right pack."
        ),
        ctr="Shoppers cross-shopping the Mountain Crest packs stop here to settle which one fits, raising qualified clicks.",
        cvr="Pre-empting the 'is this the one with multiples or one of each?' confusion sharply cuts wrong-pack returns.",
    ),
    AIImagePlanItem(
        name="Image 7 — Trust / Close: real nursery, healthy arrival",
        role="trust",
        background="Clean nursery scene: trays of rooted 2-inch pots, soft daylight.",
        purpose="Build arrival confidence and close on the family-nursery promise; quietly defuse the rare fungus/musty objection.",
        visual=(
            "Two-part. LEFT: a tray of healthy, established rosettes in 2-inch pots with visible new "
            "growth, plus the live-plant box with upright-handling labels and the printed care guide. "
            "RIGHT: a small trust strip — 'rooted & established' · 'packed for live arrival' · "
            "'care guide included' · 'pet-safe'. Hands (no face) lifting one pot for scale. "
            "Honest, nursery-grade — a real licensed succulent nursery, not a kiosk."
        ),
        overlay="REAL NURSERY PLANTS",
        overlay_sub="Rooted and established, packed for live arrival, with a care guide included.",
        props=["tray of rooted 2-inch pots with new growth", "live-plant box with handling labels", "printed care guide", "hands lifting a pot (no face)"],
        lighting="Soft natural daylight, accurate color, lived-in nursery feel — not staged stock.",
        why_it_works=(
            "Closes on the brand promise (real plants, real nursery, real help) and addresses the only "
            "recurring negative — occasional shipping-moisture issues — by foregrounding rooted, "
            "established plants, live-arrival packing and the included care guide."
        ),
        ctr="The healthy-plants-and-care-guide trust strip reassures buyers wary of mail-order live plants.",
        cvr="Visible plant health, live-arrival packing and an included care guide answer the top arrival worry and seal the purchase.",
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Brand banner",
        role="a+_banner",
        headline="20 VARIETIES, NO REPEATS",
        body=(
            "Twenty live Sempervivum plants — twenty different varieties, one of each. "
            "Hardy hens and chicks rooted in 2-inch nursery pots, cold-hardy outdoors to "
            "-20°F in USDA Zones 5 to 10. A ready-made collection for rock gardens and "
            "diverse rosette displays."
        ),
        visual="Wide cinematic overhead of the full 20-variety grid in 2-inch pots, true natural color, teal #345C64 wordmark top-left. Clean light background.",
        alt="Overhead grid of 20 different Sempervivum varieties in 2-inch nursery pots, one of each, no repeats.",
    ),
    AIModule(
        name="Module 2 — Carousel (4 tiles): why this pack",
        role="a+_carousel",
        headline="WHY THIS PACK",
        body=(
            "Tile 1: <b>ONE OF EACH</b> — 20 different varieties, no duplicates.<br/>"
            "Tile 2: <b>COLD-HARDY OUTDOORS</b> — to -20°F, USDA Zones 5 to 10.<br/>"
            "Tile 3: <b>ROOTED IN 2-INCH POTS</b> — established and ready to plant.<br/>"
            "Tile 4: <b>LOW-CARE ROSETTES</b> — drought tolerant, sends out chicks."
        ),
        visual="4 square tiles, green #78A848 accent corner per tile, line icons (grid · snowflake · pot · rosette). Real plant photography in each.",
        alt="Four-tile carousel: one of each, cold-hardy, rooted in 2-inch pots, low-care rosettes.",
    ),
    AIModule(
        name="Module 3 — Banner: the living rosette mosaic",
        role="a+_banner",
        headline="A LIVING ROSETTE MOSAIC",
        body=(
            "Planted together, the twenty varieties form a tapestry of different rosette "
            "forms and seasonal colors. Tuck them among stones in a rock garden, fill a "
            "container, or plant them in the ground — mature rosettes can even send up "
            "pink flower stalks."
        ),
        visual="Wide banner: the mixed varieties planted among rocks in natural daylight, a few pink flower stalks. Honest, true color — never oversaturated.",
        alt="A+ banner: mixed Sempervivum varieties forming a colorful rosette mosaic in a sunlit rock garden.",
    ),
    AIModule(
        name="Module 4 — Banner: easy outdoor care",
        role="a+_banner",
        headline="HARDY, AND EASY TO KEEP",
        body=(
            "Give them full to partial sun and water deeply only after the soil dries out. "
            "They shrug off cold to -20°F once established and need little else. Over time "
            "each plant sends out chicks you can separate and replant to grow your collection."
        ),
        visual="Triptych: LEFT a rooted 2-inch pot, CENTER sun/water/cold care icons, RIGHT an offset 'chick' being replanted. Clean daylight, green accents.",
        alt="A+ triptych: rooted 2-inch pot, simple sun and water care, and a chick offset being replanted.",
    ),
    AIModule(
        name="Module 5 — Comparison: which pack is right for you",
        role="a+_comparison",
        headline="WHICH PACK IS RIGHT",
        body=(
            "Compare across three columns: <b>This Variety Pack</b> · Sempervivum Bulk · "
            "Hardy Variety Pack.<br/><br/>"
            "Rows: Plant count · Assortment · Plant type · Hardiness · Made for.<br/><br/>"
            "<b>This Variety Pack:</b> 20 plants · 20 different, one of each · Sempervivum · "
            "to -20°F, Zones 5-10, outdoor · collecting and diverse displays.<br/>"
            "<b>Sempervivum Bulk:</b> 25 plants · 5 varieties, 5 of each · Sempervivum · "
            "to -20°F, outdoor · projects, landscaping, and resale.<br/>"
            "<b>Hardy Variety Pack:</b> 20 plants · mixed types, all different · Sempervivum, "
            "Sedum and more · to 0°F, Zones 7-10 · frost-proof landscaping.<br/><br/>"
            "Want one of each to collect? This is your pack. Need multiples for a project? "
            "Choose the bulk pack instead. Highlight the This column."
        ),
        visual="Amazon Premium Comparison Chart, 3 product columns, this-pack column highlighted teal #345C64. Sibling packs named by their pack name only.",
        alt="Comparison chart: this Variety Pack (one of each) vs Sempervivum Bulk (5 of each) vs Hardy Variety Pack (mixed types).",
    ),
    AIModule(
        name="Module 6 — Carousel (4 tiles): where they shine",
        role="a+_carousel",
        headline="WHERE THEY SHINE",
        body=(
            "Tile 1: <b>ROCK GARDENS</b> — rosettes tucked among stones.<br/>"
            "Tile 2: <b>CONTAINERS</b> — a mixed bowl of varieties.<br/>"
            "Tile 3: <b>MINI GARDENS</b> — small-scale diverse displays.<br/>"
            "Tile 4: <b>IN THE GROUND</b> — hardy outdoor groundcover."
        ),
        visual="4 identically composed use-case tiles, real outdoor plant scenes, green accent corner per tile, consistent natural daylight.",
        alt="Four-tile carousel of uses: rock gardens, containers, mini gardens, and in-ground planting.",
    ),
    AIModule(
        name="Module 7 — Premium Q&A",
        role="a+_qa",
        headline="COMMON QUESTIONS",
        body=(
            "<b>Q.</b> Will I get any duplicates?<br/>"
            "<b>A.</b> No. You receive 20 different Sempervivum varieties, one of each — a true "
            "collector assortment with no repeats.<br/><br/>"
            "<b>Q.</b> How cold-hardy are they?<br/>"
            "<b>A.</b> Sempervivum are cold-hardy outdoors in USDA Zones 5 to 10 and tolerate at "
            "least -20°F once established.<br/><br/>"
            "<b>Q.</b> What size are the plants?<br/>"
            "<b>A.</b> Each plant arrives fully rooted and established in its own 2-inch nursery pot.<br/><br/>"
            "<b>Q.</b> Indoors or outdoors?<br/>"
            "<b>A.</b> These thrive outdoors in full to partial sun — ideal for rock gardens, "
            "containers, and in-ground planting.<br/><br/>"
            "<b>Q.</b> How is this different from the bulk pack?<br/>"
            "<b>A.</b> This pack gives you 20 different varieties, one of each, for collecting. The "
            "Sempervivum Bulk gives 25 plants as 5 of each, for projects and resale."
        ),
        visual="Vertical Q/A table, teal dividers between questions, small Q./A. labels in dark #414042.",
        alt="Premium Q&A module answering duplicates, hardiness, pot size, indoor vs outdoor, and bulk difference.",
    ),
]


QA = [
    AIQA(q="Will I get any duplicate plants?",
         a="No. You receive 20 different Sempervivum varieties, one of each, with no repeats. It is a sampler-style collection chosen for diversity, not multiples of the same plant."),
    AIQA(q="How cold-hardy are these Sempervivum?",
         a="They are cold-hardy outdoors in USDA Zones 5 to 10 and tolerate at least -20°F once established. They are well suited to outdoor rock gardens and in-ground beds."),
    AIQA(q="What size are the plants and how do they ship?",
         a="Each plant arrives fully rooted and established in its own 2-inch nursery pot. Packs ship with upright-handling labels and a printed care guide so they travel and settle in well."),
    AIQA(q="Should I keep them indoors or outdoors?",
         a="These thrive outdoors in full to partial sun. Use them in rock gardens, containers, mini gardens, or planted directly in the ground."),
    AIQA(q="How do I care for them?",
         a="Give them full to partial sun and water deeply only after the soil is completely dry. They are drought tolerant and low maintenance, and they send out chicks you can separate and replant."),
    AIQA(q="How is this different from the Sempervivum Bulk pack?",
         a="This Variety Pack is 20 different varieties, one of each, for collecting and diverse displays. The Sempervivum Bulk pack is 25 plants as 5 of each variety, made for projects, landscaping, and resale."),
    AIQA(q="Are these pet-safe, and will the chicks spread?",
         a="Yes, the plants are pet-safe. Over time mature rosettes produce offsets, called chicks, that you can separate and replant, so a planting can expand and fill in."),
    AIQA(q="Can I tell the varieties apart when they arrive?",
         a="Yes. Variety names or temperature tolerances are supplied on plant stakes or a legend, and a printed care guide is included so you can identify and place each one."),
]


# Backend KWs — US English, stem-deduped, byte-packed. No brand/title duplicates, no superlatives.
BACKEND = (
    "sempervivum hens and chicks succulents live plants hardy rosette cold hardy outdoor "
    "rock garden groundcover perennial assorted variety collection sampler 2 inch pots "
    "rooted starter container mini garden fairy garden drought tolerant low maintenance "
    "sedum houseleek zone 5 winter hardy gift pet safe real plant set bulk assortment"
)


def main() -> None:
    print("Loading Mountain Crest Gardens customer + parsing Sempervivum Variety Excel…")
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
