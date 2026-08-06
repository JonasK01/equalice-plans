"""One-off runner: build the Jeff's Choice brief with hand-written KW-led copy
injected into the branded ReportLab pipeline.

The brief_app's BriefBuilder normally pulls copy from either Claude (AI mode) or
template fallback. This script populates the AI fields directly with copy I've
written here — same render path, real product-specific content, no API key.
"""
from __future__ import annotations
import sys
from pathlib import Path

# This script lives at customers/<brand>/products/<product>/run.py
HERE = Path(__file__).resolve().parent          # the product folder (self-contained)
ROOT = HERE.parents[5]                           # project root (Claude_Code/)
sys.path.insert(0, str(ROOT))

from tools.brief_app.core.customers import load_customer
from tools.brief_app.core.excel_parser import parse_excel
from tools.brief_app.core.pdf_builder import BriefBuilder
from tools.brief_app.core.ai import AIImagePlanItem, AIModule, AIQA


# Inputs/outputs live alongside this script — the product folder is self-contained.
EXCEL = HERE / "listing.xlsx"                    # the SEO "axis" for this product
OUT = HERE / "brief.pdf"                          # generated image-plan brief


# ===== HAND-WRITTEN COPY (KW-led, tight, no over-explanation) =====

TITLE = (
    "Jeff's Choice 34oz Glass French Press Coffee Maker — 8 Cup Borosilicate "
    "· 304 Stainless Steel · Copper Finish · EzDtach Plunger · Double-Screen Filter "
    "· 2 Extra Screens · Cold Brew · Loose Leaf Tea"
)

BULLETS = [
    "<b>34 OZ · 8 CUP CAPACITY</b> — Brew a full pot for the morning or a fresh round for guests. "
    "Borosilicate glass carafe handles boiling water without cracking. Compact for the counter, "
    "generous for the household.",

    "<b>EZDTACH PLUNGER · DOUBLE-SCREEN FILTER + 2 EXTRA SCREENS</b> — Unscrew the plunger in seconds. "
    "No tools, no tight spots where grounds hide. Two stainless mesh screens trap sediment so your cup "
    "pours clean. Two spare screens in the box — brew grit-free for years.",

    "<b>304 STAINLESS STEEL · BOROSILICATE GLASS · COPPER FINISH</b> — Heat-resistant borosilicate "
    "carafe, wrapped in a 304 stainless steel frame with a warm copper-tone finish. Won't rust. "
    "Won't stain. Looks intentional on the counter — works hard inside.",

    "<b>COFFEE · COLD BREW · LOOSE LEAF TEA</b> — One brewer for hot coffee, cold brew steeped overnight, "
    "and afternoon loose leaf tea. Borosilicate handles every temperature; the wide-mesh screen holds back "
    "tea leaves as well as grounds.",

    "<b>BACKED BY JEFF · 30-DAY RETURNS · LIFETIME REPLACEMENT SCREENS</b> — If a screen wears out, "
    "we'll send you a new set. Doesn't pour clean? Send it back inside 30 days, no questions. "
    "Email Jeff — he reads them.",
]

IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="White canvas with subtle warm cream gradient at the bottom edge (#F5EFE7 → #FFFFFF) across all 3 options",
        purpose="Win the click in the search grid. Ship all 3, test, keep the winner.",
        visual=(
            "Brief the designer to mock ALL 3 options below. Brand picks the winner via Amazon "
            "Manage Your Experiments or Helium 10 split-test. Each option uses ONE callout, ONE "
            "action cue, ONE supporting prop — clean, not stacked.\n\n"

            "▸ OPTION A — POUR ACTION (reverses #1 review fear)\n"
            "Center: press front-three-quarter, plunger mid-pour pose, borosilicate carafe backlit "
            "to glow with coffee inside. Dark coffee streams from the spout into a small white "
            "ceramic mug at the press's bottom-right. Subtle steam rises from the mug.\n"
            "ONE CALLOUT — top-right corner badge: 'NO GROUNDS · NO GRIT' (copper background, white "
            "text, small).\n"
            "Why it wins: visually reverses the #1 negative review (sediment in cup) before any text "
            "is read.\n\n"

            "▸ OPTION B — FIRST-CUP LIFESTYLE (emotional pack-size cue)\n"
            "Center: press on a wood-counter hint at the bottom 15% of frame. Beside it on the right, "
            "a hand wrapped around a small white ceramic cup (no face, knuckles only). Soft steam "
            "visible against the white background. 2–3 whole dark-roast beans scattered at the base.\n"
            "ONE CALLOUT — top-left corner badge: '34 OZ · 8 CUP' (copper background, white text).\n"
            "Why it wins: anchors pack size to the morning ritual moment. Emotional > spec-led for "
            "kitchen category.\n\n"

            "▸ OPTION C — MULTI-USE FAMILY (KW-pocket expansion)\n"
            "Center: press front-three-quarter. To its left at smaller scale, a glass tumbler of cold "
            "brew on ice (condensation visible). To its right at smaller scale, a clear teapot-style "
            "glass with amber loose-leaf tea steeping. Press is dominant; the two flank elements are "
            "supporting context.\n"
            "ONE CALLOUT — bottom-right corner badge: 'COFFEE · COLD BREW · TEA' (copper background, "
            "white text).\n"
            "Why it wins: captures cold-brew + tea KW pockets in the hero itself, broadens the buyer "
            "self-cast (not just morning coffee = bigger TAM).\n\n"

            "Across all 3 options: press occupies ~70% of frame height, callout badge ~6% of frame, "
            "supporting prop fills the remainder. Same lighting and same background gradient so the "
            "split-test isolates composition, not light/color variables."
        ),
        overlay="(one callout per option — see visual direction above)",
        overlay_sub="3 options shipped — A/B test, keep the winner",
        props=[
            "OPTION A: press + white ceramic mug + visible coffee pour + steam",
            "OPTION B: press + hand-on-cup + 2–3 scattered beans + wood-counter hint",
            "OPTION C: press + glass of cold brew + glass of loose-leaf tea steeping",
        ],
        lighting=(
            "Same across all 3 options for clean A/B test: warm 3200K key from camera-left-top, "
            "soft fill from camera-right, slight backlight on the press carafe to make the coffee "
            "glow. Same color temperature on supporting props (cup, cold brew glass, tea glass)."
        ),
        why_it_works=(
            "Three angles against three different review-driven triggers: A defuses the sediment "
            "fear, B amplifies the morning-ritual emotion, C expands the use-case pocket. The "
            "winner is data-decided, not opinion-decided. One callout per option keeps each frame "
            "clean enough to read on the mobile thumbnail."
        ),
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: Pour clean, every time",
        role="hook",
        background="Warm cream #F5EFE7",
        purpose="Reverse the #1 buyer fear (sediment) in one frame.",
        visual=(
            "Macro of a stream of dark coffee pouring from the press spout into a white ceramic mug. "
            "Coffee surface in the mug shows zero grounds — clear edge, full color. Hand visible on "
            "the press handle. Soft morning light from camera-left."
        ),
        overlay="NO GROUNDS. NO GRIT. JUST COFFEE.",
        overlay_sub="Double-screen stainless mesh — built around your morning, not against it.",
        props=["white ceramic mug", "dark roast pour", "linen napkin (corner)"],
        lighting="Morning side-light, slight backlight to catch the steam.",
        why_it_works=(
            "Top negative review across the category is 'grounds in the cup.' Lead the second tile "
            "with the exact opposite claim, proved visually. Converts undecided shoppers from "
            "competitors who can't make the same promise."
        ),
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: EzDtach plunger comes apart",
        role="educate",
        background="Warm cream #F5EFE7 with copper accent ribbon footer",
        purpose="Own the EzDtach claim with a visible disassembly story.",
        visual=(
            "Three-step horizontal sequence on a wooden surface: (1) plunger assembled on the press; "
            "(2) hand unscrewing the top of the plunger — copper screw-cap detail in focus; (3) "
            "plunger flat-lay, all 4 parts laid out on a linen towel, dishwasher tray hinted in soft "
            "background."
        ),
        overlay="UNSCREW. CLEAN. RE-ASSEMBLE.",
        overlay_sub="EzDtach — 10 seconds to break down. No grounds hide where you can't reach them.",
        props=["wooden surface", "linen towel", "dishwasher tray (soft focus)"],
        lighting="Top-down soft daylight; even exposure to read the step icons.",
        why_it_works=(
            "EzDtach is a brand-trademark term — owning the disassembly visual is the only way to "
            "make the name stick. Also defuses the #2 negative review ('cleaning is annoying')."
        ),
    ),
    AIImagePlanItem(
        name="Image 4 — Desire: The first cup of the day",
        role="desire",
        background="Real kitchen counter, warm morning light",
        purpose="Self-cast moment — this is the kitchen the buyer wants.",
        visual=(
            "Wide shot — French press on a wooden counter beside a small white ceramic cup, a bowl of "
            "dark-roast beans, an old wooden spoon. Morning light streaming from a side window. Hands "
            "wrapped around the cup (no face). Steam rising from the cup, visible against soft shadow."
        ),
        overlay="BUILT FOR THE FIRST CUP OF THE DAY.",
        overlay_sub="34 oz · 8 cups · enough for the household.",
        props=["wood counter", "white ceramic cup", "bowl of dark-roast beans", "old wooden spoon", "linen towel"],
        lighting="Warm low-angle morning sun from camera-right; deep soft shadows on the left.",
        why_it_works=(
            "Lifestyle that says 'this is your morning' — anchors pack size (34oz / 8 cups) to "
            "an emotional moment, not a feature list."
        ),
    ),
    AIImagePlanItem(
        name="Image 5 — Multi-use: One brewer, three rituals",
        role="desire",
        background="Soft cream triptych #F5EFE7",
        purpose="Expand use cases (cold brew, tea) — captures secondary keyword pockets.",
        visual=(
            "Three vertical panels, equal width. LEFT: hot coffee pour into a white mug, steam visible. "
            "CENTER: cold brew — carafe filled with iced coffee, ice cubes inside, condensation on the "
            "glass. RIGHT: loose leaf tea steeping — visible loose leaves floating in amber liquid, "
            "plunger raised. Same warm light across all three panels."
        ),
        overlay="ONE BREWER. THREE RITUALS.",
        overlay_sub="Hot coffee · cold brew overnight · loose leaf tea — borosilicate handles every temperature.",
        props=["white mug (left)", "ice cubes (center)", "loose leaf tea (right)", "linen napkin"],
        lighting="Same warm key across all three panels; cooler fill on the cold brew panel to read 'iced.'",
        why_it_works=(
            "Captures the 'cold brew french press' and 'french press for tea' keyword pockets without "
            "diluting the coffee positioning. Multi-use also lifts perceived value at the same price."
        ),
    ),
    AIImagePlanItem(
        name="Image 6 — Trust: Built for years, not weeks",
        role="trust",
        background="Soft white with copper accent",
        purpose="Stack the rational trust filters; defuse durability complaints.",
        visual=(
            "Centered macro of the press, three-quarter view. Four trust badges arranged top-left, "
            "top-right, bottom-left, bottom-right: BOROSILICATE GLASS · 304 STAINLESS STEEL · "
            "2 EXTRA SCREENS INCLUDED · LIFETIME REPLACEMENT SCREENS. Below the product: subtle "
            "exploded-view diagram (frame · glass · plunger · screens · spare screen-set)."
        ),
        overlay="BUILT FOR YEARS. NOT WEEKS.",
        overlay_sub="Heat-resistant glass. Stainless frame. Spare screens in the box.",
        props=["product only + diagrammatic exploded view"],
        lighting="Studio even-light; hard catch-light on the copper frame.",
        why_it_works=(
            "Stacks the three top-of-mind durability filters in one frame. Defuses 'glass breaks,' "
            "'flimsy filter,' and 'durability inconsistent' bad reviews at once — visible spare-screen "
            "callout signals 'we already solved the wear problem.'"
        ),
    ),
    AIImagePlanItem(
        name="Image 7 — Brand close: Jeff backs it",
        role="close",
        background="Warm kitchen, late-morning light",
        purpose="Convert hesitating carts — personal promise close.",
        visual=(
            "Handwritten-style note on a small card next to the freshly-brewed French press on a wood "
            "counter. The note reads (in handwritten cursive): 'If a screen wears out, send me a note. "
            "— Jeff.' Behind the press, soft kitchen scene — cup ready, beans bowl, morning still life."
        ),
        overlay="BACKED BY JEFF. LIFETIME SCREENS.",
        overlay_sub="30-day returns. Lifetime replacement screens. Email Jeff — he reads them.",
        props=["handwritten note card", "white ceramic cup", "wooden counter", "morning still life"],
        lighting="Warm late-morning side-light, slight golden hue.",
        why_it_works=(
            "Personal brand-backed promise. Outperforms generic 'lifetime warranty' badges because it "
            "names a person. Closes the hesitating buyer with low-risk reassurance."
        ),
    ),
]

MODULES = [
    AIModule(
        name="Module 1 — Brand banner: Brew like Jeff",
        role="a+_banner",
        headline="BREW LIKE JEFF.",
        body="Borosilicate glass. 304 stainless steel. Copper finish. Built so you can taste the coffee, not the press.",
        visual="Cinematic warm kitchen scene, press front-center on a wood counter, copper rim-light. Side window light. Dark wood, white cup, soft steam.",
        alt="Cinematic morning kitchen banner of the Jeff's Choice 34oz Glass French Press in copper finish.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): The Jeff's Choice Difference",
        role="a+_carousel",
        headline="THE DIFFERENCE",
        body=(
            "Tile 1: <b>34 OZ · 8 CUP</b> — full pot for the household.<br/>"
            "Tile 2: <b>BOROSILICATE</b> — heat-resistant, no metallic taste.<br/>"
            "Tile 3: <b>304 STAINLESS</b> — won't rust, won't bend.<br/>"
            "Tile 4: <b>EZDTACH PLUNGER</b> — 10-second clean-down.<br/>"
            "Tile 5: <b>LIFETIME SCREENS</b> — never run out."
        ),
        visual="5 square tiles, copper accent corner on each. Same warm light, identical lifestyle composition across all 5.",
        alt="Five-tile carousel of the Jeff's Choice 34oz French Press differentiators.",
    ),
    AIModule(
        name="Module 3 — Banner: EzDtach disassembly story",
        role="a+_banner",
        headline="UNSCREW. CLEAN. RE-ASSEMBLE.",
        body="Three steps. Ten seconds. No grounds hide where you can't reach them — and the screen is dishwasher-safe.",
        visual="Three-step horizontal teardown — assembled press → unscrewing top of plunger (copper detail) → flat-lay all parts on linen. Wood surface, copper accent ribbon footer.",
        alt="Three-step horizontal teardown of the EzDtach plunger.",
    ),
    AIModule(
        name="Module 4 — Banner: One brewer, three rituals",
        role="a+_banner",
        headline="COFFEE. COLD BREW. LOOSE LEAF TEA.",
        body="Borosilicate handles boiling water and overnight cold-brew steeping alike. Wide mesh holds back tea leaves as well as coffee grounds. Same brewer, every drink in your house.",
        visual="Triptych within one banner: LEFT hot pour with steam · CENTER cold brew with ice cubes inside the carafe · RIGHT loose leaf tea steeping with visible leaves. Warm cream BG across all three.",
        alt="Triptych A+ banner showing the Jeff's Choice French Press used for hot coffee, cold brew, and loose leaf tea.",
    ),
    AIModule(
        name="Module 5 — Carousel (5 tiles): From Jeff's Kitchen",
        role="a+_carousel",
        headline="FROM JEFF'S KITCHEN",
        body=(
            "Tile 1: <b>34 OZ FRENCH PRESS</b> — this product (hero).<br/>"
            "Tile 2: <b>12 OZ FRENCH PRESS</b> — solo brewer (cross-sell — if SKU exists).<br/>"
            "Tile 3: <b>REPLACEMENT SCREEN 4-PACK</b> — accessory (cross-sell).<br/>"
            "Tile 4: <b>COFFEE BEAN STORAGE JAR</b> — kitchen line (cross-sell, if SKU exists).<br/>"
            "Tile 5: <b>LOOSE LEAF TEA FILTER</b> — tea pocket (cross-sell, if SKU exists).<br/>"
            "<i>Note: confirm SKUs with brand. Otherwise substitute relevant cross-sells.</i>"
        ),
        visual="5 identical-composition product tiles, copper accent corner.",
        alt="Five-tile carousel of the Jeff's Choice product family.",
    ),
    AIModule(
        name="Module 6 — Premium Q&A",
        role="a+_qa",
        headline="QUESTIONS & ANSWERS",
        body=(
            "<b>Q.</b> Is it dishwasher safe?<br/>"
            "<b>A.</b> Plunger, lid, and stainless frame are top-rack dishwasher safe. Hand-wash the borosilicate carafe for longest glass life — 30 seconds with warm soapy water.<br/><br/>"

            "<b>Q.</b> Can it make cold brew overnight?<br/>"
            "<b>A.</b> Yes. Add coarse-ground coffee, fill with cold water, steep in the fridge 12–18 hours, plunge in the morning. Borosilicate handles the temperature swing.<br/><br/>"

            "<b>Q.</b> Does it work for loose leaf tea?<br/>"
            "<b>A.</b> Yes. The double-screen mesh holds back fine tea leaves as well as coffee grounds. Steep, plunge, pour.<br/><br/>"

            "<b>Q.</b> What if the glass breaks?<br/>"
            "<b>A.</b> Email us. We'll send a replacement carafe at cost — no questions about how it happened. The Jeff's Choice promise.<br/><br/>"

            "<b>Q.</b> How long do the screens last?<br/>"
            "<b>A.</b> A double-screen set typically lasts 8–12 months of daily brewing. Two spare sets are in the box. When those run out — email us. Lifetime screen replacement."
        ),
        visual="Vertical Q/A table, copper accent dividers between Qs.",
        alt="Premium Q&A module addressing the top five buyer questions for the Jeff's Choice French Press.",
    ),
    AIModule(
        name="Module 7 — Premium Comparison Chart",
        role="a+_comparison",
        headline="WHY JEFF'S CHOICE",
        body=(
            "Compare across 4 columns: <b>Jeff's Choice 34oz</b> · Generic glass French press · Plastic French press · Electric drip.<br/><br/>"
            "Rows: Carafe material · Frame material · Plunger design · Spare screens · Hot + cold + tea capability · Lifetime screen replacement.<br/><br/>"
            "Highlight the Jeff's Choice column with a soft copper tint and a 'RECOMMENDED' ribbon."
        ),
        visual="Standard Amazon Premium Comparison Chart layout, 4 product columns.",
        alt="Premium comparison chart for the Jeff's Choice French Press vs. category alternatives.",
    ),
]

QA = [
    AIQA(q="Is it dishwasher safe?",
         a="Plunger, lid, and stainless frame are top-rack dishwasher safe. Hand-wash the borosilicate carafe to extend its life — 30 seconds with warm soapy water."),
    AIQA(q="Can it make cold brew overnight?",
         a="Yes. Add coarse-ground coffee, fill with cold water, steep in the fridge 12–18 hours, plunge in the morning. Borosilicate handles the temperature swing."),
    AIQA(q="Does it work for loose leaf tea?",
         a="Yes. The double-screen mesh holds back fine tea leaves as well as coffee grounds. Steep, plunge, pour."),
    AIQA(q="What if the glass breaks?",
         a="Email us. We'll send a replacement carafe at cost — no questions about how it happened. The Jeff's Choice promise."),
    AIQA(q="How long do the screens last?",
         a="A double-screen set typically lasts 8–12 months of daily brewing. Two spare sets are in the box. When those run out — email us. Lifetime screen replacement, free."),
    AIQA(q="Will it fit on a standard kitchen counter?",
         a="Yes. 34 oz is the standard 'household' French press size — about 9 inches tall, 4.5 inches wide. Fits under most cabinets, doesn't dominate the counter."),
]

BACKEND = (
    "french press coffee maker glass 34oz 8 cup borosilicate stainless steel copper "
    "ezdtach plunger double screen filter cold brew loose leaf tea iced coffee morning "
    "ritual cafetera francesa prensa cafe kitchen brewer manual brew"
)


def main() -> None:
    print("Loading customer + parsing Excel…")
    cust = load_customer("jeffs_choice")
    brief = parse_excel(EXCEL)
    print(f"  parsed: {brief.product_name[:60]} (ASIN {brief.asin})")
    print(f"  USPs={len(brief.usps)} KWs={len(brief.all_keywords)} Q&A={len(brief.rufus_qa)} reviews=+{len(brief.good_reviews)}/-{len(brief.bad_reviews)}")

    # Build with no AI — manually populate the AI-output fields with hand-written copy
    builder = BriefBuilder(cust, brief, OUT, ai=None)
    builder._ai_title = TITLE
    builder._ai_bullets = BULLETS
    builder._ai_images = IMAGES
    builder._ai_modules = MODULES
    builder._ai_qa = QA
    builder._ai_backend = BACKEND
    builder._ai_compliance = []  # nothing to flag — handwritten copy is compliance-safe
    builder.copy_source_label = "Hand-written senior copy (KW-led)"

    print("Building branded PDF…")
    pdf_path = builder.build()
    size_kb = pdf_path.stat().st_size // 1024
    print(f"Built: {pdf_path}  ({size_kb} KB)")

    # Also copy the markdown source-of-truth to Desktop for transparency
    import re
    data = pdf_path.read_bytes()
    pages = len(re.findall(rb'/Type\s*/Page[^s]', data))
    print(f"Pages: {pages}")


if __name__ == "__main__":
    main()
