"""Mountain Crest Gardens — TRAILING & STRINGS PACK (12, 6 varieties x2) — Image Plan 02
Hand-written senior copy injected into the branded EQUALICE ReportLab pipeline.

Marketplace: amazon.com (US). Customer text + art direction both ENGLISH.

THIS PACK'S IDENTITY (the #1 job — make it crystal clear which pack this is):
  • TRAILING / STRING succulents — cascading habit (string-of-pearls, burro's tail,
    etc.). Stems can spill up to about 3 feet as they mature.
  • 12 live plants = 6 different varieties, 2 of each. A starter set built for
    hanging planters and cascading decor.
  • TENDER — bright INDOOR light or filtered / partial outdoor shade (not frost-hardy).
  • Fully rooted & established in 2-inch nursery pots.
  For: hanging baskets, shelves, cascading arrangements, indoor greenery.

THE DISAMBIGUATION (client mandate): a dedicated "WHICH PACK IS RIGHT FOR YOU?"
comparison module positions THIS pack vs the siblings. The single most important
contrast for buyers: this is the ONLY TRAILING / hanging pack — every other Mountain
Crest pack is UPRIGHT rosettes (Sempervivum / Echeveria) or spiny cacti that do NOT
cascade. So if you want greenery that spills down from a basket or shelf, this is the
one. Disambiguating badges live on the creative: "TRAILING FOR HANGING",
"CASCADES TO 3 FT", "12 PLANTS 6 KINDS", "BRIGHT INDOOR LIGHT".

LANGUAGE: all art-direction fields (purpose, background, visual, props, lighting,
why_it_works, ctr, cvr, module visual) are designer-facing English. All customer
text (title, bullets, overlays, module headline/body, Q&A) is English too (US).

OVERLAY RULE: sell the OUTCOME / identity, not the action. Each overlay distinct,
≤30 chars AND ≤5 words, SMOOTH (no "Word? Word." fragments, no "·" middots —
middots count as words). overlay_sub ≤90 · module headline ≤38 · bullet head ≤45.

Verified facts (from listing.xlsx USPs + brand_study matrix):
  - 12 live trailing succulents, 6 different varieties, 2 of each
  - fully rooted & established in its own 2-inch nursery pot, ready to display/transplant
  - trailing/cascading habit; stems can spill up to about 3 feet as they mature
  - tender: bright indoor light or filtered/partial outdoor sun (NOT frost-hardy)
  - low-water: water deeply only after the soil dries completely
  - grown in a fast-draining cactus/succulent medium; use pots with drainage
  - easy to propagate from offsets, cuttings, or leaves (varies by variety)
  - care guide included; hand-picked, seasonal colors/varieties may differ slightly

Review insight (VoC) used:
  praised  = healthy, vigorous plants that keep growing; attractive sculptural color;
             good value vs garden centers; easy-care for beginners; secure packaging
  objection= DOMINANT complaint is plants smaller / less full than photos, and
             "doesn't match the listing photos"; also dry/dehydrated arrival, broken
             strands, fungus gnats.
             → defuse with HONESTY: show true starter size in 2-inch pots, state the
               3-ft cascade is a MATURE / over-time result (sets correct expectation),
               foreground rooted live-arrival packing + care guide, note fast-draining
               medium (gnat mitigation).

Compliance: no $/price, no URL/.com, no superlatives (best/#1/top/leading),
no false hardiness claims (this pack is TENDER — never call it frost-hardy),
no medical claims.
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
PLAN_NO = "02"
ASIN = "B0FK6MXSS6"


# ===== KW-led, nursery-accurate US copy (customer-facing English) =====

# Title is HTML-escaped on render, so a literal "&" counts as 1 char. Keep ≤200 real chars.
TITLE = (
    "Mountain Crest Gardens Trailing & Strings Succulent Pack — 12 Live Plants, "
    "6 Trailing Varieties, 2 of Each, Rooted in 2 Inch Pots — Hanging Succulents "
    "for Indoor Planters and Cascading Decor"
)

BULLETS = [
    "<b>12 TRAILING PLANTS, 6 KINDS</b> — Twelve live trailing succulents, six different "
    "varieties, two of each. A starter set of cascading strings made for hanging planters.",

    "<b>CASCADES UP TO 3 FEET</b> — Trailing varieties like string of pearls and burro's tail "
    "spill longer as they grow, dropping curtains of greenery from a shelf, basket, or rail.",

    "<b>ROOTED IN 2-INCH POTS</b> — Each plant arrives fully rooted and established in its own "
    "2-inch nursery pot, ready to display in a hanging planter or transplant into your own.",

    "<b>BRIGHT INDOOR LIGHT</b> — These are tender succulents for bright indoor light or filtered "
    "outdoor shade. Water deeply only after the soil dries out; use pots with drainage.",

    "<b>HAND-PICKED LIVE GREENERY</b> — Easy-care plants you can propagate from cuttings and "
    "offsets. Hand-picked, so seasonal colors may vary, and a printed care guide is included.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B test)",
        role="hero",
        background="Pure white #FFFFFF seamless (Amazon main-image policy — main hero shows no overlay text). For the badge-bearing alt options, a clean light backdrop #ECEFF4. True-to-life plant color, never oversaturated.",
        purpose="Win the click in the amazon.com live-plant grid — instantly read as a TRAILING / hanging set of cascading strings, not upright rosettes or cacti.",
        visual=(
            "Real, accurate trailing-succulent photography in true natural color. Designer mocks ALL 3 "
            "options; brand picks the winner via Amazon Manage Your Experiments. One callout, one idea, "
            "one clean layout each.\n\n"
            "▸ OPTION A — THE CASCADE (wins on the trailing identity)\n"
            "A hanging planter with the varieties spilling strands downward — string of pearls and "
            "burro's tail visibly cascading. Reads as 'hanging plant' at a thumbnail glance. (Compliant "
            "alt: badge top-right 'TRAILING FOR HANGING' in teal #345C64.)\n\n"
            "▸ OPTION B — CLEAN MAIN (Amazon-policy main image)\n"
            "Pure white background, a tight group of the 6 trailing varieties in their 2-inch pots with "
            "strands draped forward over the pot rims, ~85% of frame, soft contact shadow. NO overlay text.\n\n"
            "▸ OPTION C — ON THE SHELF (wins on the decor use)\n"
            "A bright, styled shelf with one trailing pot spilling down past a stack of books, a hand "
            "placing a 2-inch pot for honest scale. (Compliant alt: badge bottom-left '12 PLANTS 6 KINDS'.)\n\n"
            "All 3: plants dominant, honest color, true starter size shown in real 2-inch pots — never an "
            "oversized or staged stock look (the listing must match what arrives)."
        ),
        overlay="TRAILING FOR HANGING",
        overlay_sub="Twelve cascading succulents, six varieties, rooted in 2-inch pots for hanging.",
        props=[
            "OPTION A: hanging planter with string of pearls and burro's tail cascading",
            "OPTION B: pure-white group of 6 trailing varieties in 2-inch pots, strands over rims (no text)",
            "OPTION C: bright styled shelf, one trailing pot spilling down + a hand placing a 2-inch pot",
        ],
        lighting="Bright, even, daylight-balanced (5000-5500K) so plant color stays true and accurate. No warm cast, no saturation push.",
        why_it_works=(
            "A visible cascade of strands instantly signals 'trailing / hanging plant' on a mobile "
            "thumbnail and separates this pack from every upright-rosette and cactus pack in the same "
            "Mountain Crest grid — the core disambiguation."
        ),
        ctr="A hanging cascade of strands telegraphs 'trailing plant for my basket or shelf' faster than any upright pot shot, pulling hanging-plant and string-of-pearls buyers out of the grid.",
        cvr="Showing true starter size in real 2-inch pots up front sets an honest expectation and matches what arrives — directly defusing the dominant 'smaller than the photos' complaint.",
    ),
    AIImagePlanItem(
        name="Image 2 — Spec / identity card (what's in the box)",
        role="educate",
        background="Light #ECEFF4 panel with a teal #345C64 footer band. Clean nursery-grade layout.",
        purpose="Pin down the exact identity and count so buyers know precisely which pack this is before they scroll.",
        visual=(
            "Spec card. Center: a clean group photo of the 6 trailing varieties in 2-inch pots, strands "
            "draped. Four labeled spec tiles with thin teal line icons:\n"
            "  • COUNT — 12 plants, 6 varieties, 2 of each\n"
            "  • HABIT — trailing, cascades up to ~3 ft over time\n"
            "  • LIGHT — bright indoor or partial shade (tender)\n"
            "  • POTS — fully rooted, 2-inch nursery pots\n"
            "Footer band carries the disambiguation line. A coin or ruler cue for honest pot scale."
        ),
        overlay="KNOW THIS PACK",
        overlay_sub="12 trailing succulents, 6 kinds, rooted in 2-inch pots, bright indoor light.",
        props=["group photo of 6 trailing varieties in 2-inch pots", "4 spec tiles with line icons", "teal footer band", "coin or ruler for pot scale"],
        lighting="Flat, clean studio light — legibility over atmosphere.",
        why_it_works=(
            "Converts the listing's hard facts into a single scannable identity card, so a shopper "
            "comparing the seven Mountain Crest packs can confirm count, habit, light needs and pot size "
            "at a glance — the heart of the client's disambiguation mandate."
        ),
        ctr="A clear spec card reassures detail-driven plant buyers and earns the scroll into the gallery.",
        cvr="Stating the true starter pot size and that 3 ft is an over-time result removes the 'what exactly do I get?' gap that drives wrong-size returns.",
    ),
    AIImagePlanItem(
        name="Image 3 — Hook: built to cascade",
        role="hook",
        background="Clean light #ECEFF4 with one hanging planter as the focal point.",
        purpose="Make the trailing / hanging identity unmistakable — the reason to choose THIS pack over the upright ones.",
        visual=(
            "One hanging planter shown small-now and long-later: LEFT the freshly potted strands just "
            "spilling over the rim (true starter size); RIGHT the same plant matured with strands "
            "cascading well below. A thin teal arrow and caption strip: 'short now, longer as it grows'. "
            "Names of two flagship varieties (string of pearls, burro's tail) on small stakes."
        ),
        overlay="MADE TO CASCADE",
        overlay_sub="Strands start short and spill longer over time, up to about 3 feet.",
        props=["starter strands over pot rim", "matured long-cascade version", "teal growth arrow", "variety name stakes"],
        lighting="Bright daylight-balanced, true color, honest scale across both states.",
        why_it_works=(
            "Doubles down on the single strongest differentiator versus the rosette and cactus packs — "
            "these trail and hang — while the short-now/long-later framing pre-empts the dominant "
            "'arrived smaller / less full than the photo' objection."
        ),
        ctr="'Made to cascade' is exactly what hanging-plant buyers scan for, and the trailing strands prove it instantly.",
        cvr="Honestly showing starter length and the over-time cascade sets correct expectations, raising fit and cutting size-mismatch returns.",
    ),
    AIImagePlanItem(
        name="Image 4 — Desire: curtains of greenery at home",
        role="desire",
        background="A bright, real interior — a sunlit window shelf or macramé hanger, soft daylight.",
        purpose="Sell the dream outcome — lush curtains of greenery cascading from a shelf or basket in the buyer's own home.",
        visual=(
            "Hero lifestyle shot: the trailing varieties grown in, strands of string of pearls and "
            "burro's tail spilling down from a hanging basket and a high shelf, forming soft curtains of "
            "green. Styled but real interior. Natural, honest color — never oversaturated."
        ),
        overlay="CURTAINS OF GREENERY",
        overlay_sub="Trailing strands spill from shelves and baskets to soften any bright room.",
        props=["hanging basket with cascading strands", "high shelf with trailing pot", "bright styled interior", "macramé hanger"],
        lighting="Natural window daylight, soft directional light for strand dimension, accurate color.",
        why_it_works=(
            "Shows the payoff buyers actually want — living curtains of greenery indoors — and matches "
            "the bright-indoor, decor use this tender trailing pack is built for."
        ),
        ctr="The aspirational cascade-in-the-home scene stands out in the grid and speaks straight to decor and houseplant buyers.",
        cvr="A realistic in-home result helps the buyer picture their own future display while keeping color and scale honest.",
    ),
    AIImagePlanItem(
        name="Image 5 — Educate: easy indoor care",
        role="educate",
        background="White with a green accent band #78A848 in the footer.",
        purpose="Show the plants are low-maintenance and tender-friendly, lowering the 'will I keep them alive?' barrier and addressing gnats/dehydration.",
        visual=(
            "Headline at top, then a clean 4-step care row with line icons:\n"
            "  • LIGHT — bright indoor or partial shade\n"
            "  • WATER — only after soil is fully dry\n"
            "  • SOIL — fast-draining mix, pots with drainage\n"
            "  • GROW — propagate from cuttings and offsets\n"
            "Footer band carries 'printed care guide included'. A rooted 2-inch pot anchors the side."
        ),
        overlay="EASY INDOOR CARE",
        overlay_sub="Bright light, water only when dry, fast-draining soil with good drainage.",
        props=["4 care-step icons", "rooted 2-inch nursery pot", "green footer band", "cutting being propagated"],
        lighting="Flat, clean studio light for legibility.",
        why_it_works=(
            "Turns the USP care facts into a confidence builder for first-time succulent buyers; the "
            "fast-draining-soil and water-when-dry notes quietly address the fungus-gnat and dehydration "
            "concerns seen in reviews, while propagation signals long-term value."
        ),
        ctr="Low-maintenance, easy-care messaging is a top reassurance for live-plant shoppers scanning the gallery.",
        cvr="Clear, simple care plus drainage guidance lowers the perceived risk of keeping live trailing plants and supports the purchase.",
    ),
    AIImagePlanItem(
        name="Image 6 — WHICH PACK IS RIGHT FOR YOU? (sibling comparison)",
        role="educate",
        background="Light #ECEFF4 with a teal #345C64 header bar. Clean comparison layout.",
        purpose="Disambiguate THIS pack from the sibling Mountain Crest packs so buyers pick the right one (the client's #1 ask).",
        visual=(
            "A 3-column compare card (this pack highlighted in teal). Columns and rows:\n"
            "  Row labels: HABIT · PLANTS · TYPE · LIGHT · MADE FOR\n"
            "  COL 1 (highlighted) — THIS · Trailing & Strings: 'trailing, cascades to ~3 ft' · "
            "'12 plants, 6 kinds' · 'String succulents' · 'bright indoor, tender' · 'Hanging planters, decor'\n"
            "  COL 2 — Echeveria Bulk: 'upright rosettes' · '25 plants, 5 of each' · 'Echeveria' · "
            "'bright indoor, tender' · 'Colorful arrangements, gifts'\n"
            "  COL 3 — Sempervivum Variety: 'upright rosettes' · '20 plants, all different' · "
            "'Sempervivum' · 'full sun, cold-hardy outdoor' · 'Rock gardens, collecting'\n"
            "Caption under it: 'Want greenery that hangs and spills? This is your pack.'"
        ),
        overlay="WHICH PACK IS RIGHT",
        overlay_sub="Want plants that hang and cascade? Choose this. Want upright rosettes? See the others.",
        props=["3-column comparison card", "this-pack column highlighted teal", "row icons: habit, count, type, light, use"],
        lighting="Flat, clean studio light — table must be legible on a phone.",
        why_it_works=(
            "Directly fulfills the disambiguation mandate: it shows this is the ONLY trailing / hanging "
            "pack, set against the upright-rosette Echeveria and Sempervivum packs, so buyers who want "
            "cascading greenery self-route here and the rest route away."
        ),
        ctr="Shoppers cross-shopping the Mountain Crest packs stop here to settle which one hangs, raising qualified clicks.",
        cvr="Pre-empting the 'do these trail or stand upright?' confusion sharply cuts wrong-pack returns.",
    ),
    AIImagePlanItem(
        name="Image 7 — Trust / Close: real nursery, healthy arrival",
        role="trust",
        background="Clean nursery scene: trays of rooted 2-inch trailing pots, soft daylight.",
        purpose="Build arrival confidence and close on the family-nursery promise; quietly defuse the dry-arrival, broken-strand, and mismatch objections.",
        visual=(
            "Two-part. LEFT: a tray of healthy, established trailing plants in 2-inch pots with full "
            "strands, plus the live-plant box with upright-handling labels and the printed care guide. "
            "RIGHT: a small trust strip — 'rooted & established' · 'packed for live arrival' · "
            "'care guide included' · 'hand-picked'. Hands (no face) lifting one pot for honest scale. "
            "Honest, nursery-grade — a real licensed succulent nursery, not a kiosk."
        ),
        overlay="REAL NURSERY PLANTS",
        overlay_sub="Rooted and established, packed for live arrival, with a care guide included.",
        props=["tray of rooted 2-inch trailing pots with full strands", "live-plant box with handling labels", "printed care guide", "hands lifting a pot (no face)"],
        lighting="Soft natural daylight, accurate color, lived-in nursery feel — not staged stock.",
        why_it_works=(
            "Closes on the brand promise (real plants, real nursery, real help) and addresses the "
            "recurring negatives — dry arrival, broken strands, photo mismatch — by foregrounding rooted, "
            "established plants in honest 2-inch pots, live-arrival packing and the included care guide."
        ),
        ctr="The healthy-plants-and-care-guide trust strip reassures buyers wary of mail-order live trailing plants.",
        cvr="Visible plant health, live-arrival packing and an included care guide answer the top arrival worries and seal the purchase.",
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Brand banner",
        role="a+_banner",
        headline="12 TRAILING PLANTS, 6 KINDS",
        body=(
            "Twelve live trailing succulents — six different varieties, two of each. "
            "Cascading strings like string of pearls and burro's tail, rooted in 2-inch "
            "nursery pots and ready for hanging planters. Bright indoor light or partial "
            "outdoor shade. A starter set of greenery made to spill and grow."
        ),
        visual="Wide cinematic shot of a hanging planter with the trailing varieties cascading, true natural color, teal #345C64 wordmark top-left. Clean light background.",
        alt="Hanging planter of 12 trailing succulents, 6 varieties, cascading strands, rooted in 2-inch pots.",
    ),
    AIModule(
        name="Module 2 — Carousel (4 tiles): why this pack",
        role="a+_carousel",
        headline="WHY THIS PACK",
        body=(
            "Tile 1: <b>TRAILING HABIT</b> — strands spill from shelves and baskets.<br/>"
            "Tile 2: <b>CASCADES TO 3 FEET</b> — longer as the plants mature.<br/>"
            "Tile 3: <b>ROOTED IN 2-INCH POTS</b> — established and ready to hang.<br/>"
            "Tile 4: <b>BRIGHT INDOOR LIGHT</b> — tender, easy-care greenery."
        ),
        visual="4 square tiles, green #78A848 accent corner per tile, line icons (cascade · ruler · pot · sun). Real trailing-plant photography in each.",
        alt="Four-tile carousel: trailing habit, cascades to 3 feet, rooted in 2-inch pots, bright indoor light.",
    ),
    AIModule(
        name="Module 3 — Banner: curtains of greenery",
        role="a+_banner",
        headline="CURTAINS OF GREENERY",
        body=(
            "Grown in, the trailing strands spill down from shelves and baskets to form "
            "soft curtains of green. String of pearls, burro's tail and more drape over "
            "rims and rails, softening a bright window, desk, or corner with living "
            "cascading decor."
        ),
        visual="Wide banner: trailing varieties cascading from a hanging basket and shelf in a bright interior, natural daylight. Honest, true color — never oversaturated.",
        alt="A+ banner: trailing succulents cascading from a basket and shelf as curtains of greenery indoors.",
    ),
    AIModule(
        name="Module 4 — Banner: easy indoor care",
        role="a+_banner",
        headline="EASY TO KEEP, EASY TO GROW",
        body=(
            "Give them bright indoor light or filtered outdoor shade and water deeply only "
            "after the soil dries out. Plant in a fast-draining mix in pots with drainage. "
            "Over time the strands lengthen, and you can propagate new plants from cuttings "
            "and offsets to fill more baskets."
        ),
        visual="Triptych: LEFT a rooted 2-inch pot with strands, CENTER light/water/drainage care icons, RIGHT a cutting being propagated. Clean daylight, green accents.",
        alt="A+ triptych: rooted 2-inch trailing pot, simple light and water care, and a cutting being propagated.",
    ),
    AIModule(
        name="Module 5 — Comparison: which pack is right for you",
        role="a+_comparison",
        headline="WHICH PACK IS RIGHT",
        body=(
            "Compare across three columns: <b>This Trailing &amp; Strings Pack</b> · Echeveria "
            "Bulk · Sempervivum Variety Pack.<br/><br/>"
            "Rows: Habit · Plant count · Plant type · Light · Made for.<br/><br/>"
            "<b>This Trailing &amp; Strings Pack:</b> trailing, cascades to ~3 ft · 12 plants, "
            "6 kinds, 2 of each · string succulents · bright indoor, tender · hanging planters "
            "and cascading decor.<br/>"
            "<b>Echeveria Bulk:</b> upright rosettes · 25 plants, 5 of each · Echeveria · "
            "bright indoor, tender · colorful arrangements and gifts.<br/>"
            "<b>Sempervivum Variety Pack:</b> upright rosettes · 20 plants, all different · "
            "Sempervivum · full sun, cold-hardy outdoor · rock gardens and collecting.<br/><br/>"
            "Want greenery that hangs and spills? This is your pack. Want upright rosettes? "
            "Choose one of the others. Highlight the This column."
        ),
        visual="Amazon Premium Comparison Chart, 3 product columns, this-pack column highlighted teal #345C64. Sibling packs named by their pack name only.",
        alt="Comparison chart: this Trailing & Strings Pack (cascading) vs Echeveria Bulk and Sempervivum Variety (upright rosettes).",
    ),
    AIModule(
        name="Module 6 — Carousel (4 tiles): where they shine",
        role="a+_carousel",
        headline="WHERE THEY SHINE",
        body=(
            "Tile 1: <b>HANGING BASKETS</b> — strands spilling over the rim.<br/>"
            "Tile 2: <b>HIGH SHELVES</b> — greenery cascading downward.<br/>"
            "Tile 3: <b>DIY ARRANGEMENTS</b> — mixed trailing bowls.<br/>"
            "Tile 4: <b>BRIGHT WINDOWS</b> — living indoor decor."
        ),
        visual="4 identically composed use-case tiles, real trailing-plant scenes, green accent corner per tile, consistent natural daylight.",
        alt="Four-tile carousel of uses: hanging baskets, high shelves, DIY arrangements, and bright windows.",
    ),
    AIModule(
        name="Module 7 — Premium Q&A",
        role="a+_qa",
        headline="COMMON QUESTIONS",
        body=(
            "<b>Q.</b> What exactly do I get?<br/>"
            "<b>A.</b> Twelve live trailing succulents: six different varieties, two of each, "
            "all rooted in their own 2-inch nursery pots.<br/><br/>"
            "<b>Q.</b> How long do they trail?<br/>"
            "<b>A.</b> Strands start short and lengthen as the plants mature; over time many "
            "trailing varieties can cascade up to about 3 feet.<br/><br/>"
            "<b>Q.</b> What size do they arrive?<br/>"
            "<b>A.</b> They arrive at starter size in 2-inch pots, fully rooted and established, "
            "ready to display in a hanging planter or transplant.<br/><br/>"
            "<b>Q.</b> Indoors or outdoors?<br/>"
            "<b>A.</b> These are tender. Keep them in bright indoor light or filtered outdoor "
            "shade — they are not frost-hardy.<br/><br/>"
            "<b>Q.</b> How is this different from the rosette packs?<br/>"
            "<b>A.</b> This is the trailing pack: the plants cascade and hang. The Echeveria "
            "and Sempervivum packs are upright rosettes that do not trail."
        ),
        visual="Vertical Q/A table, teal dividers between questions, small Q./A. labels in dark #414042.",
        alt="Premium Q&A module answering what's included, trailing length, arrival size, indoor vs outdoor, and rosette difference.",
    ),
]


QA = [
    AIQA(q="What exactly do I get in this pack?",
         a="You receive 12 live trailing succulents: six different varieties with two plants of each. Every plant is fully rooted and established in its own 2-inch nursery pot."),
    AIQA(q="How long do the strands trail?",
         a="Strands start short and lengthen as the plants grow. Over time many trailing varieties, such as string of pearls and burro's tail, can cascade up to about 3 feet."),
    AIQA(q="What size are the plants when they arrive?",
         a="They arrive at starter size in 2-inch pots, fully rooted and ready to display in a hanging planter or transplant. They fill out and trail longer as they mature in your care."),
    AIQA(q="Should I keep them indoors or outdoors?",
         a="These are tender trailing succulents. Keep them in bright indoor light or filtered, partial outdoor shade. They are not frost-hardy, so protect them from cold."),
    AIQA(q="How do I care for them?",
         a="Give them bright light and water deeply only after the soil is completely dry. Use a fast-draining mix in pots with drainage, and a printed care guide is included to help."),
    AIQA(q="How is this different from the rosette packs?",
         a="This is the trailing pack, made for hanging planters and cascading decor. The Echeveria Bulk and Sempervivum Variety packs are upright rosettes that do not trail or hang."),
    AIQA(q="Can I propagate more plants from these?",
         a="Yes. Depending on the variety you can propagate from offsets, cuttings, or leaves, so over time you can grow new plants to fill more baskets and pots."),
    AIQA(q="Will the plants match the photos and varieties shown?",
         a="Plants are hand-picked from a working nursery, so seasonal colors and variety selection may differ slightly. They ship at honest starter size, rooted and packed for live arrival."),
]


# Backend KWs — US English, stem-deduped, byte-packed. No brand/title duplicates, no superlatives.
BACKEND = (
    "trailing succulents live plants hanging plant string of pearls burro tail string of "
    "hearts cascading vine indoor houseplant succulent 2 inch pots rooted starter assorted "
    "variety pack 6 kinds drought tolerant low maintenance bright light tender shelf basket "
    "macrame planter decor gift propagate cuttings real plant set fast draining greenery"
)


def main() -> None:
    print("Loading Mountain Crest Gardens customer + parsing Trailing & Strings Excel…")
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
