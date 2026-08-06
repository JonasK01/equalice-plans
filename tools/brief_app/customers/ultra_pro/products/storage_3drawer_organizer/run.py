"""Ultra PRO 3-Drawer Storage Organizer (ASIN B09PGT4C3T) — Image Plan #50.

Hand-written senior copy in the Ultra PRO catalog format inside the EQUALICE
brief_app. Reads this product's own SEO axis from listing.xlsx (parse_excel).

CREATIVE POSITIONING (distinct from the pages/sleeves/toploaders SKUs):
  this is STORAGE FURNITURE, not a protector — a 3-drawer desk/shelf organizer.
  Lead on ORGANIZATION + BIG CAPACITY (1,000+ standard cards / 500+ double-
  sleeved) + THREE REMOVABLE DRAWERS + matching dividers + front display slots +
  stackable design. Weave the SEO keywords (card storage, tcg storage, trading
  card organizer, pokemon card storage box, mtg storage box).

LANGUAGE SPLIT (the standard):
  • ENGLISH — art-direction / strategy fields the designer reads:
    background, purpose, visual, props, lighting, why_it_works, ctr, cvr,
    and module visual/alt.
  • ENGLISH customer copy (marketplace = amazon.com):
    TITLE, BULLETS, image overlay/overlay_sub, module headline/body, BACKEND.

ULTRA PRO STYLE (matched in the art direction of every image):
  black background, bold RED #C8102E top-line + big WHITE headline; feature
  callouts with thin arrows; icon-stat bars; a red circular badge; REAL popular
  cards (Pokemon, MTG, One Piece, sports) inside the drawers; real collector
  desk/shelf lifestyle; the product; dimension/capacity callouts; brand close
  'Trusted since 1952 · Made in USA'. (Image 1 / main image stays on a clean
  white background per Amazon policy.)

GUARDRAILS (auto-checked on build):
  overlay ≤30 chars AND ≤5 words, smooth (no middots, no fragments) ·
  overlay_sub ≤90 · module headline ≤38 · bullet head <b>…</b> ≤45 · TITLE ≤200.
COMPLIANCE: no "#1", no "best", no "leading", no "guaranteed", no "prevent",
  no "$", no URL/.com. Brand-trust proof expressed as "Trusted since 1952".

Client instruction (per Jonas, listings 35-50): do NOT build a Q&A module and
do NOT build a Comparison module. This brief ships 7 images + 6 A+ banners/carousels.
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
PLAN_NO = "50"
ASIN = "B09PGT4C3T"


# ===== Customer-facing copy (ENGLISH — amazon.com) =====

# HTML-escaped "&" counts as 1 real char. Keep de-escaped length ≤ 200.
TITLE = (
    "Ultra PRO 3-Drawer Storage Organizer — Trading Card Storage Box for Pokemon, MTG "
    "&amp; One Piece · Holds 1,000+ Cards · 3 Removable Drawers &amp; 9 Dividers · "
    "Acid-Free / No PVC · Stackable"
)

BULLETS = [
    "<b>ORGANIZE 1,000+ CARDS IN ONE BOX</b> — This trading card organizer holds over 1,000 standard "
    "cards, or 500+ double-sleeved, so your whole Pokemon, Magic (MTG) and One Piece collection lives "
    "in one place — sorted, protected and easy to reach.",

    "<b>THREE REMOVABLE DRAWERS</b> — Three full-width drawers pull all the way out and snap back in, "
    "so you can sort by game, set or rarity and carry a single drawer to the table without disturbing "
    "the rest of your card collection storage.",

    "<b>9 MATCHING DIVIDERS INCLUDED</b> — Nine card dividers let you split each drawer into tidy "
    "sections, while a front display slot on every drawer holds a standard card face-out so you can "
    "label and find any set at a glance.",

    "<b>STACKABLE, BUILT-TO-LAST DESIGN</b> — Rigid polypropylene with a recessed base lets you stack "
    "multiple organizers on a desk or shelf, and acid-free, no-PVC materials keep cards safe as your "
    "tcg storage grows.",

    "<b>TRUSTED BY COLLECTORS SINCE 1952</b> — Ultra PRO has protected collectibles since 1952. Fits "
    "standard 2.5 x 3.5 inch cards and various deck boxes — a Made in USA trading card storage box "
    "built for serious collectors.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (organizer with drawers, loaded)",
        role="hero",
        background="Pure white #FFFFFF seamless — Amazon main-image policy (no overlay text, no graphics).",
        purpose="Win the click in the amazon.com card-storage grid — instantly read as a premium 3-drawer card organizer with big capacity.",
        visual=(
            "The 3-drawer storage organizer shown three-quarter front, top drawer pulled open to reveal rows of "
            "real popular cards standing on edge (Pokemon, MTG, One Piece, a sports rookie), a matching divider and "
            "a card face-out in the front display slot. Ultra PRO branding legible. Tight crop, product ~85% of "
            "frame, subtle contact shadow, no overlay text."
        ),
        overlay="(no overlay — Amazon main image)",
        overlay_sub="",
        props=["3-drawer organizer", "one drawer open with real cards", "matching divider", "front display slot card"],
        lighting="Bright, even studio light; soft rim on the drawer edge so the structure and card rows pop against white.",
        why_it_works=(
            "Product type (3-drawer organizer), capacity and premium build read in one glance — the three things a "
            "collector scans for when choosing card storage over a plain box."
        ),
        ctr="An open drawer full of recognizable cards out-signals flat closed-box thumbnails and pulls the click.",
        cvr="Shows exactly what the buyer receives and how much it holds up front, cutting hesitation.",
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: big capacity, one organizer",
        role="hook",
        background="Black #111111. Bold RED #C8102E top-line 'MASSIVE CAPACITY', big WHITE headline below.",
        purpose="Prove the single strongest promise — one organizer swallows a whole collection.",
        visual=(
            "The organizer centered with all three drawers open like a staircase, each packed with rows of real "
            "cards. A red circular badge top-right reads 'HOLDS 1,000+ CARDS'. Thin white arrow tags each drawer "
            "'~340 cards'. White headline lower-left."
        ),
        overlay="1,000+ CARDS ORGANIZED",
        overlay_sub="One organizer holds over 1,000 standard cards, or 500+ double-sleeved.",
        props=["organizer with 3 drawers open", "rows of real cards", "red capacity badge", "per-drawer arrow tags"],
        lighting="Hard raking side-light on black so the loaded drawers and their depth read as serious capacity.",
        why_it_works=(
            "Answers the collector's top question — 'how much does it hold?' — with a proof visual, and frames the "
            "organizer as the one place a growing collection belongs."
        ),
        ctr="Three open drawers stacked full of cards on black is a pattern interrupt in a grid of closed boxes.",
        cvr="Visible capacity plus the double-sleeved number defuses the biggest sizing question before the click.",
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: three removable drawers",
        role="educate",
        background="Black #111111, RED top-line 'REMOVABLE DRAWERS', WHITE headline.",
        purpose="Show the removable-drawer system — sort by game or set, carry one drawer to the table.",
        visual=(
            "The organizer with the middle drawer lifted fully OUT and floating beside the body, cards still neatly "
            "in rows inside it. Thin white arrows call out 'pulls all the way out', 'snap-fit back in' and 'sort by "
            "game or set'. Red accent underline under the two headline words."
        ),
        overlay="DRAWERS THAT LIFT OUT",
        overlay_sub="Pull a full drawer out to sort or carry, then snap it back in place.",
        props=["organizer body", "one drawer removed and floating", "cards in rows", "3 arrow callouts"],
        lighting="Even soft light with a brighter center so the removed drawer stays the focal point on black.",
        why_it_works=(
            "Turns the headline feature into a visual — removable drawers are the reason a collector picks this over "
            "a fixed box, letting them grab one set and go."
        ),
        ctr="A drawer lifted out and floating is an unusual, curiosity-driving frame that stops the scroll.",
        cvr="Seeing the drawer come out proves the sort-and-carry workflow buyers want, removing a doubt.",
    ),
    AIImagePlanItem(
        name="Image 4 — Desire: collector organizing at the desk (lifestyle)",
        role="desire",
        background="Warm collector desk scene; product graphics kept to a slim black/red lower band.",
        purpose="Let the buyer self-cast into a calm, pro-organized collection on their own desk.",
        visual=(
            "Over-the-shoulder lifestyle: a collector's hands file cards into an open drawer of the organizer on a "
            "tidy desk, a second organizer stacked on top, more cards and a deck box nearby. Warm, aspirational, "
            "real. Slim black lower band with red top-line 'ORGANIZE LIKE A PRO' and the white headline."
        ),
        overlay="YOUR COLLECTION, SORTED",
        overlay_sub="Keep your whole collection sorted and within reach on your desk or shelf.",
        props=["collector's hands filing cards", "open drawer", "second organizer stacked", "deck box", "tidy desk"],
        lighting="Warm natural desk light from camera-left, soft and lived-in — hobbyist, not clinical.",
        why_it_works=(
            "Moves from features to the emotional payoff — a proud, sorted collection on display — which turns a "
            "browsing collector into a buyer."
        ),
        ctr="A relatable collector-desk moment stands out against sterile product-only tiles and invites the click.",
        cvr="Buyers picture their own collection organized this way, making the purchase feel like the next step.",
    ),
    AIImagePlanItem(
        name="Image 5 — Educate: dividers & front display slot",
        role="educate",
        background="Black #111111, RED top-line 'SORT & LABEL WITH EASE', WHITE headline.",
        purpose="Show how the 9 dividers and front display slots keep every set findable.",
        visual=(
            "One drawer shown top-down, split into sections by matching dividers, each section a different game "
            "(Pokemon, MTG, One Piece). A thin arrow points to the front display slot holding a card face-out as a "
            "label. Small red badge '9 DIVIDERS INCLUDED'. White headline lower-left."
        ),
        overlay="FIND ANY SET FAST",
        overlay_sub="Nine dividers section each drawer and a front slot labels it with a card.",
        props=["drawer top-down", "matching dividers", "sections by game", "front display slot card", "red badge"],
        lighting="Clean, slightly top-down key light so the divider sections and labels read instantly.",
        why_it_works=(
            "Answers 'how do I actually find a card in here?' — dividers plus a face-out label turn a big box into a "
            "browsable, indexed system collectors love."
        ),
        ctr="A neatly sectioned, labeled drawer signals real organization and earns the click from serious collectors.",
        cvr="Showing the indexing system removes the 'it'll just be a jumble' fear, nudging the purchase.",
    ),
    AIImagePlanItem(
        name="Image 6 — Trust: stackable, protective build (specs)",
        role="trust",
        background="Black #111111, RED top-line 'BUILT TO STACK & LAST', WHITE headline; icon-stat bar along the bottom.",
        purpose="Prove durable, stackable, card-safe construction so the buyer trusts it for a growing collection.",
        visual=(
            "Two organizers stacked, a thin arrow to the recessed base showing how they lock together, another to "
            "the rigid wall with 'acid-free · no PVC'. Bottom icon-stat bar with two tiles: 'STACKABLE DESIGN' and "
            "'FITS 2.5 x 3.5in CARDS'. Red accents on the stat icons."
        ),
        overlay="STACK AND EXPAND",
        overlay_sub="Rigid, acid-free build stacks on a recessed base as your collection grows.",
        props=["two organizers stacked", "arrow to recessed base", "arrow to rigid acid-free wall", "two icon-stat tiles"],
        lighting="Clean technical light — flat and legible so the stacking detail and stat icons read at a glance.",
        why_it_works=(
            "Removes the last practical doubts — 'will it last, is it card-safe, can I add more?' — with construction "
            "proof a spec-driven collector trusts."
        ),
        ctr="Concrete cues (stackable, acid-free, 2.5x3.5in) signal precision and pull spec-checking buyers.",
        cvr="Durable, stackable, acid-free proof closes the longevity objection and justifies the buy.",
    ),
    AIImagePlanItem(
        name="Image 7 — Close: brand trust (since 1952 · Made in USA)",
        role="close",
        background="Black #111111 with the Ultra PRO logo; subtle red heritage line motif.",
        purpose="Close on brand identity and heritage — the storage collectors have trusted for decades.",
        visual=(
            "Centered Ultra PRO logo on black, a neat row of stacked organizers and loaded drawers softly behind. "
            "RED top-line 'TRUSTED BY COLLECTORS WORLDWIDE', big WHITE headline, and a footer lockup: a small "
            "USA-flag mark with 'Made in USA' beside 'Since 1952'."
        ),
        overlay="TRUSTED SINCE 1952",
        overlay_sub="Protecting and organizing collections with USA-made quality since 1952.",
        props=["Ultra PRO logo", "row of stacked organizers / loaded drawers", "USA-flag 'Made in USA' mark"],
        lighting="Premium low-key light, soft glow on the logo — authoritative, heritage, category-anchor feel.",
        why_it_works=(
            "Ends on heritage and provenance — the trust cue that converts a hesitating collector who wants a brand "
            "that will still be here to protect the collection they are building."
        ),
        ctr="The heritage 'since 1952 · Made in USA' lockup signals category authority and reassures at a glance.",
        cvr="Provenance and longevity provide the final trust nudge that seals the purchase.",
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Brand banner (hero)",
        role="a+_banner",
        headline="STORAGE BUILT FOR COLLECTORS",
        body=(
            "The Ultra PRO 3-Drawer Storage Organizer keeps your trading cards sorted and protected in "
            "one place — three removable drawers, nine matching dividers and room for over 1,000 standard "
            "cards. Acid-free, no PVC, and built to stack as your collection grows."
        ),
        visual="Wide cinematic banner: the organizer left with drawers open and loaded (Pokemon, MTG, One Piece, sports) on black with a red accent bar. Ultra PRO logo top-left.",
        alt="Ultra PRO 3-Drawer Storage Organizer with drawers open and full of trading cards on a black background.",
    ),
    AIModule(
        name="Module 2 — Capacity banner",
        role="a+_banner",
        headline="ONE HOME FOR 1,000+ CARDS",
        body=(
            "From your first Pokemon pull to a graded sports rookie, one organizer holds over 1,000 "
            "standard cards, or 500+ double-sleeved — so your whole collection lives together, sorted by "
            "game, set or rarity across three deep drawers."
        ),
        visual="Banner: the organizer with all three drawers open and packed with rows of cards, a red circular '1,000+ CARDS' badge, on black. Slim red top-line with the headline.",
        alt="A+ banner showing the organizer with three open drawers packed with cards and a 1,000-plus capacity badge.",
    ),
    AIModule(
        name="Module 3 — Feature carousel (the organizer set)",
        role="a+_carousel",
        headline="WHY COLLECTORS SORT HERE",
        body=(
            "Tile 1: <b>3 REMOVABLE DRAWERS</b> — pull one out to sort or carry to the table.<br/>"
            "Tile 2: <b>HOLDS 1,000+ CARDS</b> — a whole collection in one organizer.<br/>"
            "Tile 3: <b>9 DIVIDERS INCLUDED</b> — split each drawer into tidy sections.<br/>"
            "Tile 4: <b>FRONT DISPLAY SLOT</b> — a card labels each drawer face-out.<br/>"
            "Tile 5: <b>ACID-FREE / NO PVC</b> — safe materials for long-term storage.<br/>"
            "Tile 6: <b>STACKABLE DESIGN</b> — recessed base stacks as you grow."
        ),
        visual="6 square tiles on black, red accent corner and a line icon per tile (drawer · stacked cards · divider · display slot · shield · stack). Consistent Ultra PRO styling.",
        alt="Six-tile A+ carousel: three removable drawers, holds 1,000-plus cards, nine dividers, front display slot, acid-free/no PVC, stackable design.",
    ),
    AIModule(
        name="Module 4 — Removable-drawer banner (feature callouts)",
        role="a+_banner",
        headline="SORT, PULL OUT, AND CARRY",
        body=(
            "Three full-width drawers pull all the way out and snap back in, so you can sort Pokemon, "
            "Magic (MTG), One Piece and sports cards by set, then carry a single drawer to the table "
            "without disturbing the rest of your collection."
        ),
        visual="Banner: the organizer with one drawer lifted out and floating, thin white arrow callouts to 'pulls all the way out', 'snap-fit back in' and 'sort by set'. Red top-line and white headline.",
        alt="A+ banner with callouts on the removable drawer system of the 3-drawer card organizer.",
    ),
    AIModule(
        name="Module 5 — Fit & build banner (icon stats)",
        role="a+_banner",
        headline="FITS YOUR CARDS AND SHELF",
        body=(
            "Sized for standard 2.5 x 3.5 inch cards and compatible with various deck boxes, the rigid "
            "polypropylene build stacks on a recessed base so multiple organizers sit neatly on a desk "
            "or shelf as your card storage grows."
        ),
        visual="Banner with two large icon-stat tiles on black: 'FITS 2.5 x 3.5in CARDS' and 'STACKABLE DESIGN', two organizers stacked alongside. Red stat icons.",
        alt="A+ banner with icon stats: fits standard 2.5 by 3.5 inch cards and stackable design.",
    ),
    AIModule(
        name="Module 6 — Brand close (heritage + review)",
        role="a+_banner",
        headline="TRUSTED SINCE 1952",
        body=(
            "Collectors worldwide trust Ultra PRO for collectible storage and protection — proudly Made "
            "in USA since 1952. <br/><br/>“I trust Ultra Pro for all my collectible card needs, great "
            "quality.” &#9733;&#9733;&#9733;&#9733;&#9733;"
        ),
        visual="Closing banner: Ultra PRO logo centered on black, stacked organizers softly behind, footer lockup with a USA-flag 'Made in USA' mark and 'Since 1952', a five-star review quote below.",
        alt="Ultra PRO brand-close banner: trusted by collectors worldwide, Made in USA since 1952, with a five-star review quote.",
    ),
]


# ENGLISH backend search terms — stem-deduped, no title/brand duplicates, ≤ 249 bytes.
BACKEND = (
    "collector card box tcg deck ccg yugioh gathering baseball sports memorabilia "
    "bulk large capacity holder case bin desk shelf sorted dividers display drawer "
    "acid free polypropylene stackable double sleeved collection"
)


def main() -> None:
    print("Loading Ultra PRO customer + parsing listing.xlsx (product 50)…")
    cust = load_customer("ultra_pro")
    brief = parse_excel(EXCEL)
    OUT = HERE / f"{PLAN_NO}_{ASIN}_Image Plan.pdf"
    real_title_len = len(TITLE.replace("&amp;", "&"))
    print(f"  Product: {brief.product_name}  ASIN: {ASIN}")
    print(f"  Marketplace: {cust.marketplace}  Overlay lang: {cust.overlay_language}")
    print(f"  TITLE real chars (de-escaped): {real_title_len}")

    builder = BriefBuilder(cust, brief, OUT, ai=None)
    builder._ai_title = TITLE
    builder._ai_bullets = BULLETS
    builder._ai_images = IMAGES
    builder._ai_modules = MODULES
    builder._ai_qa = []       # client instruction: no Q&A module
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
