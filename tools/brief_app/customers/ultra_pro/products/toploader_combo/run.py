"""Ultra PRO Toploader + Card-Sleeve COMBO (Clear Storage Box) — Image Plan #38.

Hand-written senior copy in the Ultra PRO catalog format inside the EQUALICE
brief_app. Product 38 / ASIN B07YGDP2KY: a COMBO starter kit — 25 standard card
sleeves + 25 regular 3" x 4" toploaders in a clear polypropylene storage box.
The distinct creative angle: the 2-STEP protection of a valuable SINGLE card
(sleeve first, then toploader) and the "complete combo" convenience.

LANGUAGE SPLIT (the standard):
  • ENGLISH — art-direction / strategy fields the designer reads:
    background, purpose, visual, props, lighting, why_it_works, ctr, cvr,
    and module visual/alt.
  • ENGLISH customer copy (marketplace = amazon.com):
    TITLE, BULLETS, image overlay/overlay_sub, module headline/body, BACKEND.

ULTRA PRO STYLE (matched in the art direction of every image):
  black background, bold RED #C8102E top-line + big WHITE headline; thin-arrow
  feature callouts; icon-stat bars; a red circular badge; REAL popular cards
  (Pokemon, MTG, One Piece, sports) shown sleeved-then-toploaded; real collector
  lifestyle; the clear storage box; a dimension callout (3" x 4"); brand close
  'Trusted since 1952 · Made in USA'. (Image 1 stays clean white per Amazon policy.)

GUARDRAILS (auto-checked on build):
  overlay ≤30 chars AND ≤5 words, smooth (no middots, no fragments) ·
  overlay_sub ≤90 · module headline ≤38 · bullet head <b>…</b> ≤45 · TITLE ≤200.
COMPLIANCE: no "#1", no "best", no "leading", no "guaranteed", no "prevent",
  no "$", no URL/.com. Heritage proof as "Trusted since 1952", protection as
  "Protect", strength as "Superior", clarity as "Crystal/High Clarity".

Client instruction (per Jonas, listings 35-50): NO Q&A module and NO Comparison
module. This brief ships 7 images + 6 A+ banners/carousels.
"""
from __future__ import annotations
import sys
from pathlib import Path

# customers/<brand>/products/<product>/run.py — self-contained.
HERE = Path(__file__).resolve().parent          # the product folder
ROOT = HERE.parents[5]                           # project root (Claude_Code/)
sys.path.insert(0, str(ROOT))

from tools.brief_app.core.customers import load_customer
from tools.brief_app.core.excel_parser import parse_excel
from tools.brief_app.core.pdf_builder import BriefBuilder
from tools.brief_app.core.ai import AIImagePlanItem, AIModule

EXCEL = HERE / "listing.xlsx"
PLAN_NO = "38"
ASIN = "B07YGDP2KY"


# ===== Customer-facing copy (ENGLISH — amazon.com) =====

# HTML-escaped "&" counts as 1 real char. Keep de-escaped length ≤ 200.
TITLE = (
    "Ultra PRO Toploader &amp; Card Sleeve Combo — 25 Card Sleeves + 25 Regular 3\" x 4\" "
    "Toploaders in a Clear Storage Box · 2-Step Protection for Single Cards · Fits 35pt to "
    "360pt · Made in USA"
)

BULLETS = [
    "<b>COMPLETE 2-STEP COMBO</b> — Everything you need to protect a valuable single in one kit: "
    "25 standard card sleeves plus 25 regular 3\" x 4\" toploaders. Sleeve the card first, slide it "
    "into a toploader second — soft-then-hard protection your prized cards deserve.",

    "<b>SLEEVE PLUS TOPLOADER PROTECTION</b> — The card sleeves cushion the surface against scratches "
    "and dust, while the rigid toploaders shield corners and edges from bends and dings — a two-layer "
    "system for Pokemon, Magic (MTG), One Piece and sports card singles.",

    "<b>CLEAR STORAGE BOX INCLUDED</b> — A see-through polypropylene box with a self-locking header lid "
    "keeps your sleeves and top loaders together and organized. A write-on strip on top lets you label "
    "the set, the player or the game at a glance.",

    "<b>FITS 35PT TO 360PT CARDS</b> — The regular 3\" x 4\" toploaders and ONE-TOUCH-compatible box "
    "handle standard cards and thicker relics alike, from 35pt up to 360pt — one combo for base cards, "
    "rookies and chunky memorabilia singles.",

    "<b>TRUSTED BY COLLECTORS SINCE 1952</b> — Ultra PRO has protected collectibles since 1952. "
    "Crystal-clear card sleeves and toploaders that keep your singles safe to store, trade and show "
    "off — proudly Made in USA.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (clear box + sleeves + toploaders)",
        role="hero",
        background="Pure white #FFFFFF seamless — Amazon main-image policy (no overlay text, no graphics).",
        purpose="Win the click in the amazon.com card-protection grid — instantly read as a complete sleeve + toploader combo kit.",
        visual=(
            "The clear storage box standing three-quarter left with its self-locking header lid visible. In front, a "
            "small fanned stack of card sleeves on the left and a short stack of regular 3\" x 4\" toploaders on the "
            "right, ONE toploader holding a sleeved real card (a Pokemon or sports rookie) so the 2-step combo reads "
            "at a glance. Tight crop, product ~85% of frame, subtle contact shadow, no overlay text."
        ),
        overlay="(no overlay — Amazon main image)",
        overlay_sub="",
        props=["clear storage box with header lid", "stack of card sleeves", "stack of 3x4 toploaders", "one sleeved real card in a toploader"],
        lighting="Bright, even studio light; soft rim on the clear box and toploader so the plastic reads glass-clear against white.",
        why_it_works=(
            "Shows all three parts of the kit — box, sleeves, toploaders — plus the sleeved-card-in-a-toploader, so a "
            "collector instantly sees a complete combo, not a single item, and grasps the 2-step method in one glance."
        ),
        ctr="A combo bundle (box + sleeves + toploaders) out-signals single-item thumbnails and pulls value-seeking collectors.",
        cvr="Shows exactly what the buyer receives and demonstrates the 2-step method up front, cutting hesitation.",
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: protect your valuable single",
        role="hook",
        background="Black #111111. Bold RED #C8102E top-line 'PROTECT WHAT MATTERS', big WHITE headline below.",
        purpose="Trigger the collector's core fear — a valuable single getting scratched or bent — and reverse it.",
        visual=(
            "Hero macro of one prized card (a holo Pokemon or a graded-look sports rookie) first slid into a crystal "
            "card sleeve, then dropped into a rigid 3\" x 4\" toploader. A thin white arrow labels 'SLEEVE' on the soft "
            "layer and 'TOPLOADER' on the hard shell. A red circular badge top-right reads 'PROTECT YOUR SINGLES'. "
            "White headline lower-left."
        ),
        overlay="PROTECT YOUR SINGLES.",
        overlay_sub="Sleeve the card, then a rigid toploader guards every corner and edge.",
        props=["one prized single card", "crystal card sleeve", "rigid 3x4 toploader", "red circular badge", "SLEEVE / TOPLOADER arrows"],
        lighting="Hard raking side-light on black so the clear sleeve and toploader read as glass and the card art pops.",
        why_it_works=(
            "Answers the collector's top worry — 'will my best card get damaged?' — by showing the exact two-layer "
            "defense the combo delivers, on a real recognizable card."
        ),
        ctr="A giant, protected holo single on black is a pattern interrupt against flat product-only tiles.",
        cvr="Naming and showing both layers proves the card is fully protected, defusing the fear before the click.",
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: the 2-step method",
        role="educate",
        background="Black #111111, RED top-line 'HOW THE COMBO WORKS', WHITE headline.",
        purpose="Teach the simple 2-step routine so the buyer knows exactly how to use the kit.",
        visual=(
            "A clean left-to-right sequence on black: STEP 1 a card sliding into a crystal sleeve, STEP 2 the sleeved "
            "card sliding into a 3\" x 4\" toploader, STEP 3 the finished sleeved-and-loaded card standing upright. Thin "
            "white arrows connect the steps; small numbered tags 1-2-3. Red accent underlines under the two headline words."
        ),
        overlay="SLEEVE PLUS TOPLOADER.",
        overlay_sub="A simple two-step routine: soft sleeve inside, rigid toploader outside.",
        props=["3-step sequence graphic", "card + crystal sleeve", "sleeved card + 3x4 toploader", "numbered 1-2-3 tags"],
        lighting="Even soft light on each step, slightly brighter center so the finished card stays the focal point on black.",
        why_it_works=(
            "New and returning collectors both want the 'right way' to protect a single — a clear 1-2-3 removes doubt "
            "and positions the combo as the complete, foolproof method."
        ),
        ctr="A tidy numbered how-to signals 'complete kit' and earns the click from buyers unsure what they need.",
        cvr="Showing the exact routine removes the 'do I have everything?' friction and makes the combo the obvious buy.",
    ),
    AIImagePlanItem(
        name="Image 4 — Desire: the complete combo (what's in the box)",
        role="desire",
        background="Black #111111, RED top-line 'THE COMPLETE COMBO', WHITE headline; icon-stat bar along the bottom.",
        purpose="Show the full value of the kit so the buyer sees one purchase covers everything.",
        visual=(
            "The clear storage box open with the header lid up, 25 card sleeves and 25 toploaders neatly laid beside it, "
            "a few real cards sleeved-and-loaded. Bottom icon-stat bar with two tiles: '25 SLEEVES + 25 TOPLOADERS' and "
            "'HOLDS UP TO 30 TOPLOADERS'. Red accents on the stat icons; the write-on strip highlighted with a thin arrow."
        ),
        overlay="THE COMPLETE COMBO.",
        overlay_sub="25 card sleeves, 25 toploaders and a clear storage box in one starter kit.",
        props=["open clear storage box", "25 card sleeves", "25 toploaders", "two icon-stat tiles", "write-on strip callout"],
        lighting="Clean product light, slightly brighter on the box so the count and contents read instantly on black.",
        why_it_works=(
            "Spelling out the exact contents (25 + 25 + box) and capacity turns an abstract 'combo' into concrete value, "
            "which is what converts a shopper comparing bundles."
        ),
        ctr="Concrete counts (25 + 25, holds up to 30) signal real value and pull collectors comparing kits.",
        cvr="Seeing everything included answers 'is this a complete kit?' and justifies choosing the combo over separates.",
    ),
    AIImagePlanItem(
        name="Image 5 — Trust: rigid protection, stays organized",
        role="trust",
        background="Black #111111, RED top-line 'STAYS LOCKED IN', WHITE headline.",
        purpose="Defuse the fear that cards slip out or get crushed — the rigid toploader and locking box hold firm.",
        visual=(
            "A loaded toploader held upright and tilted to show the card sitting firmly inside, thin white arrows calling "
            "out 'RIGID SHELL' at the edges and 'SNUG FIT' at the mouth. Beside it, the storage box closed with a small "
            "arrow to the 'SELF-LOCKING LID'. A red badge reads 'CARDS STAY SECURE'."
        ),
        overlay="CARDS STAY LOCKED IN.",
        overlay_sub="Rigid toploaders and a self-locking box keep every single snug and secure.",
        props=["loaded toploader tilted upright", "RIGID SHELL / SNUG FIT arrows", "closed box with self-locking lid arrow", "red 'stay secure' badge"],
        lighting="Focused key on the toploader edge so the rigid shell reads as strong and protective.",
        why_it_works=(
            "Targets the top negative-review fear in card storage (cards slipping or corners bending). Showing the snug "
            "toploader and the locking box is concrete proof, not a promise."
        ),
        ctr="The 'held firm' toploader visual is a curiosity hook that stops the scroll.",
        cvr="Directly answers 'will my card slip or get bent?' with visible rigid protection, removing a purchase blocker.",
    ),
    AIImagePlanItem(
        name="Image 6 — Desire: sized for your singles (dimensions + fit)",
        role="desire",
        background="Black #111111, RED top-line 'SIZED TO FIT', WHITE headline; icon-stat bar along the bottom.",
        purpose="Prove exact fit so the buyer knows the combo works for their cards, from base cards to thick relics.",
        visual=(
            "A single card ghosted inside a toploader with a clean dimension callout '3\" x 4\"' and arrows to the "
            "toploader edges. A small thickness gauge shows '35pt' to '360pt' with a card silhouette growing thicker. "
            "Bottom icon-stat bar with two tiles: 'REGULAR 3\" x 4\" TOPLOADERS' and 'ONE-TOUCH COMPATIBLE BOX'."
        ),
        overlay="SIZED FOR YOUR CARDS.",
        overlay_sub="Regular 3 x 4 toploaders fit standard cards from 35pt up to 360pt.",
        props=["dimension callout 3\" x 4\"", "35pt to 360pt thickness gauge", "two icon-stat tiles"],
        lighting="Clean technical light — flat and legible so the dimensions and thickness gauge read instantly.",
        why_it_works=(
            "Removes the last practical doubt — 'will it fit my card and my thicker relics?' — with exact numbers a "
            "spec-driven collector trusts."
        ),
        ctr="Concrete specs (3x4, 35pt-360pt, ONE-TOUCH) signal precision and pull spec-checking buyers.",
        cvr="Exact fit and thickness range close the sizing objection and justify the buy.",
    ),
    AIImagePlanItem(
        name="Image 7 — Close: brand trust (since 1952 · Made in USA)",
        role="close",
        background="Black #111111 with the Ultra PRO logo; subtle red heritage line motif.",
        purpose="Close on brand identity and heritage — the protection collectors have trusted for decades.",
        visual=(
            "Centered Ultra PRO logo on black, the clear storage box and a few sleeved-and-loaded cards softly behind. "
            "RED top-line 'TRUSTED BY COLLECTORS WORLDWIDE', big WHITE headline, and a footer lockup: a small USA-flag "
            "mark with 'Made in USA' beside 'Since 1952'."
        ),
        overlay="TRUSTED SINCE 1952.",
        overlay_sub="Protecting collections with USA-made quality since 1952.",
        props=["Ultra PRO logo", "clear storage box behind", "sleeved-and-loaded cards", "USA-flag 'Made in USA' mark"],
        lighting="Premium low-key light, soft glow on the logo — authoritative, heritage, category-anchor feel.",
        why_it_works=(
            "Ends on heritage and provenance — the trust cue that converts a hesitating collector who wants a brand "
            "that will still be here to protect the singles they are building."
        ),
        ctr="The heritage 'since 1952 · Made in USA' lockup signals category authority and reassures at a glance.",
        cvr="Provenance and longevity provide the final trust nudge that seals the purchase.",
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Brand banner (hero)",
        role="a+_banner",
        headline="COMPLETE COMBO FOR SINGLES",
        body=(
            "The Ultra PRO Toploader and Card Sleeve Combo gives you everything to protect a valuable "
            "single: 25 standard card sleeves, 25 regular 3\" x 4\" toploaders and a clear storage box. "
            "Sleeve first, toploader second — soft-then-hard protection for the cards you care about."
        ),
        visual="Wide cinematic banner: clear storage box left, fanned sleeves and toploaders center, a sleeved-and-loaded holo card right, on black with a red accent bar. Ultra PRO logo top-left.",
        alt="Ultra PRO combo: clear storage box with card sleeves and 3x4 toploaders and a sleeved card, on a black background.",
    ),
    AIModule(
        name="Module 2 — Feature carousel (what's inside)",
        role="a+_carousel",
        headline="EVERYTHING IN ONE KIT",
        body=(
            "Tile 1: <b>25 CARD SLEEVES</b> — soft crystal sleeves cushion the card surface.<br/>"
            "Tile 2: <b>25 TOPLOADERS</b> — rigid 3\" x 4\" shells guard corners and edges.<br/>"
            "Tile 3: <b>CLEAR STORAGE BOX</b> — see-through box keeps the set together.<br/>"
            "Tile 4: <b>SELF-LOCKING LID</b> — header lid snaps shut so nothing spills.<br/>"
            "Tile 5: <b>WRITE-ON STRIP</b> — label the player, set or game on top.<br/>"
            "Tile 6: <b>FITS 35PT TO 360PT</b> — base cards to thick relic singles."
        ),
        visual="6 square tiles on black, red accent corner and a line icon per tile (sleeve · toploader · box · lock · marker · thickness gauge). Consistent Ultra PRO styling.",
        alt="Six-tile A+ carousel: 25 card sleeves, 25 toploaders, clear storage box, self-locking lid, write-on strip, fits 35pt to 360pt.",
    ),
    AIModule(
        name="Module 3 — How it works banner (2-step)",
        role="a+_banner",
        headline="THE SIMPLE 2-STEP METHOD",
        body=(
            "Protecting a single is easy with the combo. Step one: slide the card into a crystal card "
            "sleeve to guard the surface from scratches and dust. Step two: drop the sleeved card into a "
            "rigid 3\" x 4\" toploader to shield the corners and edges. Store it in the clear box, done."
        ),
        visual="Banner with a left-to-right 1-2-3 sequence on black: card into sleeve, sleeved card into toploader, finished card standing in the box. Thin white arrows, red top-line and white headline.",
        alt="A+ banner showing the two-step method: sleeve the card, then insert it into a toploader.",
    ),
    AIModule(
        name="Module 4 — Protection banner (why two layers)",
        role="a+_banner",
        headline="TWO LAYERS OF PROTECTION",
        body=(
            "The soft card sleeve cushions the surface against scratches, fingerprints and dust, while the "
            "rigid toploader shields corners and edges from bends and dings. Together they protect Pokemon, "
            "Magic (MTG), One Piece, Yu-Gi-Oh and sports card singles at home, in trades and on the go."
        ),
        visual="Banner: one sleeved-and-loaded card centered on black with thin white arrow callouts to the soft sleeve layer and the rigid toploader shell. Red top-line and white headline.",
        alt="A+ banner with callouts to the soft sleeve layer and the rigid toploader shell of a protected single card.",
    ),
    AIModule(
        name="Module 5 — Organize banner (box + capacity)",
        role="a+_banner",
        headline="STORE AND STAY ORGANIZED",
        body=(
            "The clear polypropylene storage box holds up to 30 standard 3\" x 4\" toploaders, with a "
            "self-locking header lid so nothing spills and a write-on strip to label the set. See your "
            "protected singles through the box wall and keep the whole kit in one tidy place."
        ),
        visual="Banner with the clear box and two large icon-stat tiles on black: 'HOLDS UP TO 30 TOPLOADERS' and 'WRITE-ON STRIP + LOCKING LID', loaded toploaders alongside. Red stat icons.",
        alt="A+ banner with icon stats: clear box holds up to 30 toploaders, self-locking lid and write-on strip.",
    ),
    AIModule(
        name="Module 6 — Brand close (heritage + review)",
        role="a+_banner",
        headline="TRUSTED SINCE 1952",
        body=(
            "Collectors worldwide trust Ultra PRO for collectible protection — proudly Made in USA since "
            "1952. <br/><br/>“I trust Ultra Pro for all my collectible card needs, great quality.” "
            "&#9733;&#9733;&#9733;&#9733;&#9733;"
        ),
        visual="Closing banner: Ultra PRO logo centered on black, the clear box and sleeved-and-loaded cards softly behind, footer lockup with a USA-flag 'Made in USA' mark and 'Since 1952', a five-star review quote below.",
        alt="Ultra PRO brand-close banner: trusted by collectors worldwide, Made in USA since 1952, with a five-star review quote.",
    ),
]


# ENGLISH backend search terms — stem-deduped, no title/brand duplicates, ≤ 249 bytes.
BACKEND = (
    "card protector storage tcg pokemon graded sports single deck hard plastic penny "
    "sleeve one touch pt case organize collection mtg yugioh onepiece rigid holder "
    "trading standard rookie relic display trade holder box"
)


def main() -> None:
    print("Loading Ultra PRO customer + parsing listing.xlsx…")
    cust = load_customer("ultra_pro")
    brief = parse_excel(EXCEL)
    brief.asin = ASIN
    OUT = HERE / f"{PLAN_NO}_{ASIN}_Image Plan.pdf"
    real_title_len = len(TITLE.replace("&amp;", "&"))
    print(f"  Product: {brief.product_name}")
    print(f"  Marketplace: {cust.marketplace}  Overlay lang: {cust.overlay_language}")
    print(f"  TITLE real chars (de-escaped): {real_title_len}")

    builder = BriefBuilder(cust, brief, OUT, ai=None)
    builder._ai_title = TITLE
    builder._ai_bullets = BULLETS
    builder._ai_images = IMAGES
    builder._ai_modules = MODULES
    builder._ai_qa = []  # client instruction (listings 35-50): no Q&A module
    builder._ai_backend = BACKEND
    builder.copy_source_label = "Hand-written senior copy (Ultra PRO)"

    print("Building branded PDF…")
    pdf_path = builder.build()
    size_kb = pdf_path.stat().st_size // 1024
    import re
    pages = len(re.findall(rb'/Type\s*/Page[^s]', pdf_path.read_bytes()))
    print(f"Built: {pdf_path}")
    print(f"  Pages: {pages}  Size: {size_kb} KB")


if __name__ == "__main__":
    main()
