"""Ultra PRO Team Bags — Resealable Sleeves (100 Count) — Image Plan (PLAN 37).

Hand-written senior copy in the Ultra PRO catalog format inside the EQUALICE
brief_app. Reads the product's own SEO axis from listing.xlsx (parse_excel) and
builds a fully product-specific brief for ASIN B00095NR1K.

DISTINCT CREATIVE ANGLE (per product 37): lead on RESEALABLE + holds a whole
TEAM SET. The resealable strip opens and closes repeatedly; one bag holds a full
team set / multiple cards / photos. Weave the product's own keywords (team bags,
resealable team bags, team bags for trading cards).

LANGUAGE SPLIT (the standard):
  • ENGLISH — art-direction / strategy fields the designer reads.
  • ENGLISH customer copy (marketplace = amazon.com):
    TITLE, BULLETS, image overlay/overlay_sub, module headline/body, BACKEND.

ULTRA PRO STYLE (matched in the art direction of every image):
  black background, bold RED #C8102E top-line + big WHITE headline; feature
  callouts with thin arrows; icon-stat bars (100ct · resealable strip · acid-free);
  a red circular badge; REAL popular cards (Pokemon, MTG, One Piece, sports) in the
  bag; real collector lifestyle; the product box; brand close
  'Trusted since 1952 · Made in USA'. (Image 1 / main image stays on clean white.)

GUARDRAILS (auto-checked on build):
  overlay ≤30 chars AND ≤5 words, smooth (no middots, no fragments) ·
  overlay_sub ≤90 · module headline ≤38 · bullet head <b>…</b> ≤45 · TITLE ≤200.
COMPLIANCE: no "#1", no "best", no "leading", no "guaranteed", no "prevent",
  no "$", no URL/.com. Heritage proof expressed as "Trusted since 1952".

Client instruction (per Jonas, listings 35-50): NO Q&A module and NO Comparison
module. This brief ships 7 images + 6 A+ banners/carousels (a+_banner / a+_carousel).
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
PLAN_NO = "37"
ASIN = "B00095NR1K"


# ===== Customer-facing copy (ENGLISH — amazon.com) =====

# HTML-escaped "&" counts as 1 real char. Keep de-escaped length ≤ 200.
TITLE = (
    "Ultra PRO Team Bags Resealable Sleeves (100 Count) — Resealable Team Bags for "
    "Trading Cards, Sports Cards &amp; Top Loaders · Holds a Full Team Set · "
    "Acid-Free / No PVC · Made in USA"
)

BULLETS = [
    "<b>RESEAL, PROTECT, REPEAT</b> — A resealable strip lets each team bag open and close "
    "again and again, so you can add, swap or pull cards anytime and reseal to keep dust and "
    "moisture out — resealable team bags built for everyday collecting.",

    "<b>HOLDS A FULL TEAM SET</b> — Each roomy team bag holds a whole team set, multiple "
    "trading cards or photos in one place, so you can group a full roster together instead of "
    "storing loose cards one by one.",

    "<b>CRYSTAL-CLEAR VISIBILITY</b> — Clear polypropylene film shows off every Pokemon, "
    "Magic (MTG), One Piece and sports card in crystal detail, so you can read and sort a "
    "team set without opening the bag.",

    "<b>ACID-FREE, NO PVC MATERIAL</b> — Soft, flexible team bags for trading cards are "
    "archival, acid-free and made with no PVC, so your cards, top loaders and photos stay "
    "safe and true to color for years.",

    "<b>TRUSTED BY COLLECTORS SINCE 1952</b> — 100 resealable card sleeves per pack from a "
    "brand collectors have trusted since 1952. Store sports cards, TCG team sets, graded "
    "cards and photos — proudly Made in USA.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (product pack + resealable team bag with a team set)",
        role="hero",
        background="Pure white #FFFFFF seamless — Amazon main-image policy (no overlay text, no graphics).",
        purpose="Win the click in the amazon.com card-sleeve grid — instantly read as resealable team bags that hold a full team set.",
        visual=(
            "Product pack (Team Bags, 100 Count) standing three-quarter left, label fully legible. To its "
            "right, ONE clear team bag held upright and filled with a stacked TEAM SET of real popular cards "
            "(Pokemon, MTG, One Piece and a sports rookie) fanned so several faces show through the film. The "
            "resealable flap is visible at the top, half-open. Tight crop, product ~85% of frame, soft contact "
            "shadow, no overlay text."
        ),
        overlay="(no overlay — Amazon main image)",
        overlay_sub="",
        props=["Team Bags 100-count pack", "one clear team bag filled with a team set", "Pokemon / MTG / One Piece / sports cards", "resealable flap half-open"],
        lighting="Bright, even studio light; soft rim on the bag edge so the clear film and the stacked cards pop against white.",
        why_it_works=(
            "The pack plus a bag full of recognizable cards communicates product type (team bags), the "
            "resealable flap and the team-set capacity in one glance — exactly what a collector scans for."
        ),
        ctr="A single bag holding a whole fanned team set out-signals generic empty-sleeve thumbnails and pulls the click.",
        cvr="Shows exactly what the buyer receives (pack + resealable bags) and proves the team-set capacity up front.",
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: the resealable strip (macro)",
        role="hook",
        background="Black #111111. Bold RED #C8102E top-line 'RESEALABLE STRIP', big WHITE headline below.",
        purpose="Prove the single strongest promise — the strip opens and reseals again and again to keep a team set secure.",
        visual=(
            "Extreme macro of the top of a team bag: fingers peeling the resealable flap open, the adhesive "
            "strip clearly shown, a team set of cards visible inside. A thin white arrow points to the strip "
            "with a small 'reseals again and again' tag. A red circular badge top-right reads "
            "'OPEN &amp; RESEAL'. White headline lower-left."
        ),
        overlay="RESEAL, PROTECT, REPEAT.",
        overlay_sub="A resealable strip opens and closes again and again to keep your cards secure.",
        props=["macro of the resealable flap", "fingers peeling the strip open", "team set visible inside", "red 'open & reseal' badge"],
        lighting="Hard raking side-light on black so the clear film reads as glass and the strip edge catches a crisp highlight.",
        why_it_works=(
            "Answers the collector's top question — 'does it actually reseal?' — with a proof macro, and shows "
            "the strip in the act so the bag reads reusable, not disposable."
        ),
        ctr="A giant peel-open flap on black is a pattern interrupt in a grid full of flat sleeve shots.",
        cvr="Macro proof that the strip reseals defuses the biggest doubt about resealable bags before the click.",
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: feature callouts",
        role="educate",
        background="Black #111111, RED top-line 'BUILT FOR TEAM SETS', WHITE headline.",
        purpose="Stack the team-bag feature set as scannable arrow callouts a bargain bag can't match.",
        visual=(
            "One filled team bag centered on black, thin white arrows radiating to labeled callouts: "
            "RESEALABLE STRIP · ACID-FREE / NO PVC · CRYSTAL-CLEAR FILM · HOLDS A TEAM SET · SOFT &amp; FLEXIBLE "
            "· FITS TOP LOADERS. Each callout with a small line icon. Red accent underlines under the headline words."
        ),
        overlay="BUILT TO PROTECT CARDS",
        overlay_sub="Resealable, acid-free, no PVC and crystal-clear — sized for a full team set.",
        props=["filled team bag (hero object)", "6 arrow callouts with line icons", "red accent underlines"],
        lighting="Even soft light on the bag, slightly brighter center so the product stays the focal point on black.",
        why_it_works=(
            "Turns spec words into a visual proof stack — resealable / acid-free / no-PVC is exactly what a "
            "serious collector filters for and what a bargain bag cannot claim."
        ),
        ctr="A dense, well-organized feature stack signals 'serious protection' and earns the click.",
        cvr="Each callout removes a specific doubt (reseal, acid, PVC, fit), compounding trust toward purchase.",
    ),
    AIImagePlanItem(
        name="Image 4 — Desire: one bag holds a whole team set",
        role="desire",
        background="Black #111111, RED top-line 'ONE BAG, ONE TEAM', WHITE headline; product graphics in a slim lower band.",
        purpose="Show the core payoff — group a full roster in a single bag instead of loose, scattered cards.",
        visual=(
            "A single team bag laid flat and open, a full TEAM SET of ~15 sports cards fanned beside it ready to "
            "slide in together; the filled bag next to it shows the whole set grouped and readable through the "
            "film. Slim black lower band with red top-line and the white headline. Warm, aspirational, real."
        ),
        overlay="HOLDS A FULL TEAM SET.",
        overlay_sub="Group a whole team set or a stack of cards together in one roomy bag.",
        props=["team bag laid flat and open", "a fanned team set of ~15 cards", "the filled bag showing the grouped set"],
        lighting="Warm natural light from camera-left, soft and lived-in — hobbyist, not clinical.",
        why_it_works=(
            "Moves from features to the emotional payoff — a full roster kept together and easy to find — which "
            "is what turns a browsing collector into a buyer."
        ),
        ctr="A whole team set sliding into one bag is a relatable collector moment that invites the click.",
        cvr="Buyers picture their own sets grouped and tidy, making the purchase feel like the next step.",
    ),
    AIImagePlanItem(
        name="Image 5 — Trust: sealed shut, cards stay put",
        role="trust",
        background="Black #111111, RED top-line 'SEALED &amp; SECURE', WHITE headline.",
        purpose="Defuse the fear that cards slip out or dust gets in — the resealed strip holds a team set safely.",
        visual=(
            "A sealed, filled team bag rotated to show the cards held firmly even when tipped; thin white arrows "
            "call out 'resealable strip' at the top and 'soft, flexible film' along the side. A small red badge "
            "'KEEPS DUST OUT'. Optional cue: a hand tipping the bag, the team set staying together inside."
        ),
        overlay="OPEN AND RESEAL ANYTIME.",
        overlay_sub="Reseal the strip to hold your team set together and help keep dust and moisture out.",
        props=["sealed filled bag rotated", "arrow callouts to strip and film", "red 'keeps dust out' badge"],
        lighting="Focused key on the resealed strip so the closure reads as secure and precise.",
        why_it_works=(
            "Targets the top negative-review fear in card storage (cards slipping out or dust getting in). Showing "
            "the sealed strip and held set is concrete proof, not a promise."
        ),
        ctr="The tipped 'still held' bag is a curiosity hook that stops the scroll.",
        cvr="Directly answers 'will my cards fall out?' with a visible closure, removing a purchase blocker.",
    ),
    AIImagePlanItem(
        name="Image 6 — Desire: 100 count value + icon stats",
        role="desire",
        background="Black #111111, RED top-line 'READY BY THE BOX', WHITE headline; icon-stat bar along the bottom.",
        purpose="Prove the bulk value and the core specs so a stock-up buyer knows it fits their cards and volume.",
        visual=(
            "A neat stack / spread of many team bags with a big '100' number graphic, a few filled with team sets. "
            "Bottom icon-stat bar with three tiles: '100 BAGS PER PACK', 'RESEALABLE STRIP' and 'ACID-FREE / NO "
            "PVC'. Red accents on the stat icons. A card and a top loader ghosted beside a bag to show fit."
        ),
        overlay="ONE HUNDRED PER PACK.",
        overlay_sub="100 resealable team bags per pack — enough to sort a whole collection into sets.",
        props=["stack/spread of many bags", "big '100' number graphic", "three icon-stat tiles", "card + top loader for fit"],
        lighting="Clean technical light — flat and legible so the count and stat icons read instantly.",
        why_it_works=(
            "Removes the last practical doubts — 'how many do I get and what do they fit?' — with a concrete count "
            "and specs a stock-up collector trusts."
        ),
        ctr="Concrete numbers (100 count, resealable, acid-free) signal value and pull spec-checking buyers.",
        cvr="Bulk count and clear specs close the value objection and justify the buy.",
    ),
    AIImagePlanItem(
        name="Image 7 — Close: brand trust (since 1952 · Made in USA)",
        role="close",
        background="Black #111111 with the Ultra PRO logo; subtle red heritage line motif.",
        purpose="Close on brand identity and heritage — the protection collectors have trusted for decades.",
        visual=(
            "Centered Ultra PRO logo on black, a neat row of filled team bags and sorted card sets softly behind. "
            "RED top-line 'TRUSTED BY COLLECTORS WORLDWIDE', big WHITE headline, and a footer lockup: a small "
            "USA-flag mark with 'Made in USA' beside 'Since 1952'."
        ),
        overlay="TRUSTED SINCE 1952",
        overlay_sub="Protecting collections with USA-made quality since 1952.",
        props=["Ultra PRO logo", "row of filled team bags / sorted sets", "USA-flag 'Made in USA' mark"],
        lighting="Premium low-key light, soft glow on the logo — authoritative, heritage, category-anchor feel.",
        why_it_works=(
            "Ends on heritage and provenance — the trust cue that converts a hesitating collector who wants a "
            "brand that will still be here to protect the collection they are building."
        ),
        ctr="The heritage 'since 1952, Made in USA' lockup signals category authority and reassures at a glance.",
        cvr="Provenance and longevity provide the final trust nudge that seals the purchase.",
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Brand banner (hero)",
        role="a+_banner",
        headline="RESEALABLE PROTECTION FOR SETS",
        body=(
            "Team Bags are resealable sleeves that hold a full team set, a stack of trading cards or "
            "photos in one place — crystal-clear, acid-free and made with no PVC. 100 resealable bags per "
            "pack, ready to sort your whole collection into sets."
        ),
        visual="Wide cinematic banner: product pack left, a spread of filled team bags with fanned sets (Pokemon, MTG, One Piece, sports) right, on black with a red accent bar. Ultra PRO logo top-left.",
        alt="Ultra PRO Team Bags pack beside resealable bags filled with trading-card team sets on a black background.",
    ),
    AIModule(
        name="Module 2 — Resealable strip banner",
        role="a+_banner",
        headline="RESEAL, PROTECT, REPEAT",
        body=(
            "A resealable strip opens and closes again and again, so you can add, swap or pull cards "
            "anytime and reseal to keep dust and moisture out. No tape, no fuss — just peel, load your "
            "team set and press the strip closed."
        ),
        visual="Banner: macro of fingers peeling the resealable flap open on a filled bag, thin white arrow to the strip, red top-line and white headline on black.",
        alt="A+ banner showing the resealable strip of a team bag being peeled open with a team set inside.",
    ),
    AIModule(
        name="Module 3 — Feature carousel (the team-bag set)",
        role="a+_carousel",
        headline="WHY COLLECTORS PICK THESE",
        body=(
            "Tile 1: <b>RESEALABLE STRIP</b> — open and reseal again and again.<br/>"
            "Tile 2: <b>HOLDS A TEAM SET</b> — group a full roster in one bag.<br/>"
            "Tile 3: <b>CRYSTAL-CLEAR FILM</b> — read every card without opening.<br/>"
            "Tile 4: <b>ACID-FREE / NO PVC</b> — archival, will not yellow cards.<br/>"
            "Tile 5: <b>SOFT &amp; FLEXIBLE</b> — gentle on cards, easy to load.<br/>"
            "Tile 6: <b>100 PER PACK</b> — plenty to sort a whole collection."
        ),
        visual="6 square tiles on black, red accent corner and a line icon per tile (reseal strip · stacked set · sparkle · no-PVC · soft bag · '100'). Consistent Ultra PRO styling.",
        alt="Six-tile A+ carousel of Team Bags features: resealable strip, holds a team set, crystal-clear film, acid-free/no PVC, soft and flexible, 100 per pack.",
    ),
    AIModule(
        name="Module 4 — Protection banner (feature callouts)",
        role="a+_banner",
        headline="BUILT TO PROTECT YOUR CARDS",
        body=(
            "Soft, flexible, acid-free film made with no PVC protects Pokemon, Magic (MTG), One Piece, "
            "Yu-Gi-Oh and sports cards, top loaders and photos from dust, moisture and everyday handling — "
            "resealed shut to keep a whole team set safe."
        ),
        visual="Banner: one filled team bag centered on black with thin white arrow callouts to the resealable strip, the clear film and the acid-free material. Red top-line and white headline.",
        alt="A+ banner with feature callouts pointing to the resealable strip, clear film and acid-free material of a team bag.",
    ),
    AIModule(
        name="Module 5 — Capacity banner (icon stats)",
        role="a+_banner",
        headline="ONE HUNDRED PER PACK",
        body=(
            "Each pack holds 100 resealable team bags — enough to sort a whole collection into sets. Every "
            "bag fits a full team set, multiple trading cards or photos, and works with standard top "
            "loaders, so your cards stay grouped and easy to find."
        ),
        visual="Banner with three large icon-stat tiles on black: '100 BAGS PER PACK', 'RESEALABLE STRIP' and 'ACID-FREE / NO PVC', a spread of filled bags alongside. Red stat icons.",
        alt="A+ banner with icon stats: 100 bags per pack, resealable strip and acid-free/no PVC material.",
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
        visual="Closing banner: Ultra PRO logo centered on black, filled team bags and sorted sets softly behind, footer lockup with a USA-flag 'Made in USA' mark and 'Since 1952', a five-star review quote below.",
        alt="Ultra PRO brand-close banner: trusted by collectors worldwide, Made in USA since 1952, with a five-star review quote.",
    ),
]


# ENGLISH backend search terms — stem-deduped, no title/brand duplicates, ≤ 249 bytes.
BACKEND = (
    "team set bags resealable card sleeves sealable soft toploader storage tcg ccg "
    "sports baseball pokemon gathering yugioh one piece graded photo memorabilia "
    "protector holder bulk clear polypropylene collector organizer bcw"
)


def main() -> None:
    print("Loading Ultra PRO customer + parsing product 37 listing (team_bags_resealable)…")
    cust = load_customer("ultra_pro")
    brief = parse_excel(EXCEL)
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
    builder._ai_qa = []            # client instruction: no Q&A module
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
