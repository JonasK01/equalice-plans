"""Ultra PRO VIVID 12-Pocket Zippered PRO-Binder (B09P21NPN3) — Image Plan #43.

Hand-written senior copy in the Ultra PRO catalog format inside the EQUALICE
brief_app. Self-contained: listing.xlsx in (SEO axis), branded PDF out.

DISTINCT CREATIVE ANGLE for this SKU (vs. the pages/sleeves/toploader briefs):
  lead on BIG CAPACITY (stores up to 480 cards) + 12 POCKETS PER PAGE +
  ZIPPERED, travel-safe security + the VIVID color padded-leatherette cover.
  This is a no-rings, side-loading, zip-around binder — differentiation is
  "carry your whole collection, zipped shut and safe."

ULTRA PRO STYLE (matched in every image's art direction):
  black background, bold RED #C8102E top-line + big WHITE headline; thin-arrow
  feature callouts; icon-stat bars (stores up to 480 cards · 12 pockets · 20
  pages); a red circular badge; REAL popular cards (Pokemon, MTG, One Piece,
  sports) shown in the pockets; real collector lifestyle; the vivid binder shut
  and zipped; brand close 'Trusted since 1952 · Made in USA'.
  (Image 1 / main image stays on a clean white background per Amazon policy.)

GUARDRAILS (auto-checked on build):
  overlay ≤30 chars AND ≤5 words, smooth (no middots) · overlay_sub ≤90 ·
  module headline ≤38 · bullet head <b>…</b> ≤45 · TITLE ≤200.
COMPLIANCE: no "#1"/"best"/"leading"/"guaranteed", no "prevent", no "$",
  no URL/.com. Strength as "superior seal strength", heritage as "since 1952".

Client instruction (listings 35-50): NO Q&A module, NO Comparison module.
Ships 7 images + 6 A+ banners/carousels only.
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
PLAN_NO = "43"
ASIN = "B09P21NPN3"


# ===== Customer-facing copy (ENGLISH — amazon.com) =====

# HTML-escaped "&" counts as 1 real char. Keep de-escaped length ≤ 200.
TITLE = (
    "Ultra PRO Vivid 12-Pocket Zippered PRO-Binder — Trading Card Binder with Zipper "
    "for Pokemon, MTG &amp; One Piece · Holds 480 Cards · 20 Side-Loading Pages · "
    "Acid-Free, No PVC · Padded Leatherette"
)

BULLETS = [
    "<b>STORES UP TO 480 CARDS</b> — This 12 pocket zippered binder packs 20 side-loading pages "
    "with 12 pockets each, so a single trading card binder holds up to 480 standard-size cards — "
    "your whole Pokemon, MTG or One Piece collection organized in one place.",

    "<b>12 POCKETS, 20 PAGES</b> — Each page runs 12 pockets across, and every row holds a full "
    "4-card playset, so this tcg binder 12 pocket layout keeps decks, sets and duplicates sorted "
    "the way collectors actually build them.",

    "<b>ZIPPERED, TRAVEL-SAFE</b> — A zipper closure with a matching pull tab seals the trading "
    "card binder zipper shut on all sides, so cards stay put in your bag — no rings to snag, and "
    "side-loading pockets keep every card secure on the move.",

    "<b>VIVID PADDED COVER</b> — A padded leatherette cover in a vivid color guards against knocks "
    "and scuffs, while low-friction black backing between the pockets protects card faces and lets "
    "each card slide in and out clean.",

    "<b>TRUSTED BY COLLECTORS SINCE 1952</b> — Ultra PRO has protected collectibles since 1952. "
    "Acid-free, non-PVC card binder with zipper that also stores photos and memorabilia — built "
    "to the standard serious collectors rely on.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (zipped vivid binder + loaded 12-pocket page)",
        role="hero",
        background="Pure white #FFFFFF seamless — Amazon main-image policy (no overlay text, no graphics).",
        purpose="Win the click in the amazon.com card-binder grid — instantly read as a premium, high-capacity zippered 12-pocket binder.",
        visual=(
            "The vivid-color zippered PRO-Binder standing three-quarter left, zipper and pull tab clearly "
            "visible along the edge, padded leatherette cover catching soft light. Beside it, the binder opened "
            "to ONE 12-pocket page fully loaded with real popular cards (Pokemon, MTG, One Piece, a sports rookie) "
            "so the 12-across pocket layout reads at a glance. Tight crop, product ~85% of frame, subtle contact "
            "shadow, no overlay text."
        ),
        overlay="(no overlay — Amazon main image)",
        overlay_sub="",
        props=["vivid zippered PRO-Binder (closed, zipper visible)", "binder opened to one loaded 12-pocket page", "Pokemon / MTG / One Piece / sports cards"],
        lighting="Bright, even studio light; soft rim on the cover and zipper so the vivid color and 12-pocket page both pop against white.",
        why_it_works=(
            "The closed zippered cover plus an open, fully loaded 12-pocket page communicates the three things a "
            "collector scans for — big capacity, zip security and pocket count — in one glance."
        ),
        ctr="A vivid zippered binder shown both shut and loaded out-signals flat, empty-binder thumbnails and pulls the click.",
        cvr="Shows exactly what the buyer receives and proves the 12-pocket capacity up front, cutting hesitation.",
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: 480-card capacity, zipped safe",
        role="hook",
        background="Black #111111. Bold RED #C8102E top-line 'BIG CAPACITY', big WHITE headline below.",
        purpose="Prove the single strongest promise — a whole 480-card collection carried in one zipped binder.",
        visual=(
            "The vivid binder open to a fanned spread of loaded 12-pocket pages, real cards visible, with a bold "
            "'480' stat callout and a red circular badge reading 'STORES UP TO 480 CARDS'. A thin white arrow points "
            "to the closed zipper with a small 'zipped safe' tag. White headline lower-left."
        ),
        overlay="480 CARDS, ZIPPED SAFE.",
        overlay_sub="20 pages of 12 pockets hold up to 480 cards, sealed in one binder.",
        props=["binder fanned open with loaded pages", "big '480' stat callout", "red circular capacity badge", "arrow to closed zipper"],
        lighting="Hard raking side-light on black so the loaded pages and the zipper line read sharp and premium.",
        why_it_works=(
            "Answers the binder buyer's top question — 'how much does it actually hold?' — with a big concrete number, "
            "and pairs it with the zip-security cue that sets this SKU apart from ring binders."
        ),
        ctr="A giant '480' on black is a pattern interrupt in a grid full of vague 'high capacity' claims.",
        cvr="A concrete capacity number plus the zipped-safe cue defuses the two biggest doubts before the click.",
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: 12 pockets per page + 4-card playset rows",
        role="educate",
        background="Black #111111, RED top-line 'SORTED LIKE A COLLECTOR', WHITE headline.",
        purpose="Show the 12-pocket layout and how each row holds a full 4-card playset — the way collectors build sets.",
        visual=(
            "One 12-pocket page centered on black, loaded with cards. Thin white arrows call out the 12-across pocket "
            "grid and bracket one row of 4 with a 'holds a 4-card playset' tag. Small line icons for 'side-loading' and "
            "'low-friction backing'. Red accent underline under the headline."
        ),
        overlay="12 POCKETS PER PAGE.",
        overlay_sub="Each row holds a 4-card playset, so sets and decks stay together.",
        props=["12-pocket page (hero object)", "arrow callouts to the 12 pockets", "bracket over a 4-card row", "side-loading + backing icons"],
        lighting="Even soft light on the page, slightly brighter center so the pocket grid stays the focal point on black.",
        why_it_works=(
            "Turns the spec (12 pockets, 4-card rows) into a visual that maps to how TCG players actually organize "
            "playsets — exactly what a 12-pocket buyer is searching for."
        ),
        ctr="A clean 12-across grid reads instantly as 'more per page' and earns the click from set-builders.",
        cvr="Showing playset-friendly rows proves the layout fits the buyer's real sorting habit, driving the buy.",
    ),
    AIImagePlanItem(
        name="Image 4 — Desire: vivid zippered protection (cover + travel)",
        role="desire",
        background="Black #111111, RED top-line 'PROTECT WHAT MATTERS MOST', WHITE headline.",
        purpose="Sell the vivid padded cover and the zipped-all-around protection as the reason to pick this binder.",
        visual=(
            "Hero shot of the closed vivid binder at a three-quarter angle, hand drawing the zipper around the edge, "
            "padded leatherette cover catching light. Thin arrows to 'padded leatherette cover' and 'zip closure with "
            "pull tab'. A slim lower band carries the red top-line and white headline."
        ),
        overlay="VIVID, ZIPPERED PROTECTION.",
        overlay_sub="A padded leatherette cover and zip closure guard cards on every side.",
        props=["closed vivid binder", "hand drawing the zipper", "arrow to padded cover", "arrow to zip pull tab"],
        lighting="Warm key from camera-left with a crisp rim on the zipper — premium, tactile, aspirational.",
        why_it_works=(
            "Moves from capacity to the emotional payoff — a good-looking, fully sealed binder the collector is proud "
            "to carry — which is what turns a browser into a buyer in the zippered-binder segment."
        ),
        ctr="The vivid cover mid-zip is a tactile, colorful moment that stands out against sterile binder-only tiles.",
        cvr="Buyers picture their collection zipped safely inside a cover they like, making the purchase feel worth it.",
    ),
    AIImagePlanItem(
        name="Image 5 — Trust: side-loading pockets + secure zip",
        role="trust",
        background="Black #111111, RED top-line 'SECURE ON THE MOVE', WHITE headline.",
        purpose="Defuse the fear that cards slip out or fall — side-loading pockets plus the zip hold everything in place.",
        visual=(
            "A page rotated to show cards held firmly in side-loading pockets even when tilted; thin white arrows call "
            "out 'side-loading pockets' and 'low-friction black backing'. Beside it the whole binder shown upside-down "
            "and zipped shut with a red badge 'ZIPPED SHUT, NOTHING FALLS OUT'."
        ),
        overlay="ZIP SHUT, TRAVEL SAFE.",
        overlay_sub="Side-loading pockets and an all-around zip keep every card in place.",
        props=["page tilted to show held cards", "arrows to side-loading pockets and backing", "binder inverted and zipped", "red security badge"],
        lighting="Focused key on the pocket mouths and the zipper line so the side-load design and seal read as secure.",
        why_it_works=(
            "Targets the top negative-review fear in card binders (cards sliding out or ring dents). Side-loading plus "
            "a full zip is concrete proof the cards stay put, not a promise."
        ),
        ctr="The upside-down, zipped 'still holds' visual is a curiosity hook that stops the scroll.",
        cvr="Directly answers 'will my cards fall out?' with visible side-load and zip proof, removing a purchase blocker.",
    ),
    AIImagePlanItem(
        name="Image 6 — Desire: no rings, standard-size fit (icon stats)",
        role="desire",
        background="Black #111111, RED top-line 'BUILT FOR YOUR CARDS', WHITE headline; icon-stat bar along the bottom.",
        purpose="Prove practical fit — no rings to dent cards, sized for standard cards, and the full capacity in numbers.",
        visual=(
            "A single standard card ghosted into a side-loading pocket with a clean dimension cue and arrows to the "
            "pocket edges; a small 'NO RINGS' callout where ring binders would dent cards. Bottom icon-stat bar with "
            "three tiles: 'STORES UP TO 480 CARDS', '12 POCKETS PER PAGE', '20 PAGES'. Red accents on the stat icons."
        ),
        overlay="SIDE-LOAD, NO RINGS.",
        overlay_sub="Ring-free, side-loading pockets sized for standard trading cards.",
        props=["standard card in a side-loading pocket", "'NO RINGS' callout", "three icon-stat tiles (480 / 12 / 20)"],
        lighting="Clean technical light — flat and legible so the fit cue and stat icons read instantly.",
        why_it_works=(
            "Removes the last practical doubts — 'will it dent my cards, do they fit, how much does it hold?' — with the "
            "no-rings advantage and exact numbers a spec-driven collector trusts."
        ),
        ctr="Concrete numbers (480 / 12 / 20) plus 'NO RINGS' signal precision and pull spec-checking buyers.",
        cvr="Exact capacity data and the ring-free reassurance close the sizing and safety objections at once.",
    ),
    AIImagePlanItem(
        name="Image 7 — Close: brand trust (since 1952 · Made in USA)",
        role="close",
        background="Black #111111 with the Ultra PRO logo; subtle red heritage line motif.",
        purpose="Close on brand identity and heritage — the protection collectors have trusted for decades.",
        visual=(
            "Centered Ultra PRO logo on black, a neat row of zipped vivid binders softly behind. RED top-line "
            "'TRUSTED BY COLLECTORS WORLDWIDE', big WHITE headline, and a footer lockup: a small USA-flag mark with "
            "'Made in USA' beside 'Since 1952'."
        ),
        overlay="TRUSTED SINCE 1952.",
        overlay_sub="Protecting collections with USA-made quality since 1952.",
        props=["Ultra PRO logo", "row of zipped vivid binders", "USA-flag 'Made in USA' mark"],
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
        headline="PROTECT WHAT MATTERS MOST",
        body=(
            "The Vivid 12-Pocket Zippered PRO-Binder carries your whole collection in one place — "
            "20 side-loading pages, 12 pockets each, holding up to 480 trading cards behind a padded "
            "leatherette cover that zips shut on every side."
        ),
        visual="Wide cinematic banner: the closed vivid binder left, an open loaded 12-pocket spread (Pokemon, MTG, One Piece, sports) right, on black with a red accent bar. Ultra PRO logo top-left.",
        alt="Ultra PRO Vivid 12-pocket zippered binder closed beside an open page loaded with trading cards on a black background.",
    ),
    AIModule(
        name="Module 2 — Feature carousel (the vivid set)",
        role="a+_carousel",
        headline="THE VIVID DIFFERENCE",
        body=(
            "Tile 1: <b>HOLDS 480 CARDS</b> — 20 pages, 12 pockets each, one binder.<br/>"
            "Tile 2: <b>ZIP CLOSURE</b> — sealed on all sides with a matching pull tab.<br/>"
            "Tile 3: <b>SIDE-LOADING</b> — cards slide in secure and stay put.<br/>"
            "Tile 4: <b>NO PVC / ACID-FREE</b> — safe long-term storage for cards.<br/>"
            "Tile 5: <b>PADDED COVER</b> — vivid leatherette guards against knocks.<br/>"
            "Tile 6: <b>4-CARD ROWS</b> — every row holds a full playset."
        ),
        visual="6 square tiles on black, red accent corner and a line icon per tile (stack · zipper · side-arrow · no-PVC · padded cover · playset row). Consistent Ultra PRO styling.",
        alt="Six-tile A+ carousel: holds 480 cards, zip closure, side-loading, no PVC/acid-free, padded cover, 4-card rows.",
    ),
    AIModule(
        name="Module 3 — Capacity banner (480 cards)",
        role="a+_banner",
        headline="480 CARDS, ONE ZIPPED BINDER",
        body=(
            "Twenty 12-pocket pages hold up to 480 standard-size cards, and each row fits a full 4-card "
            "playset — so decks, sets and duplicates from Pokemon, Magic (MTG), One Piece and Yu-Gi-Oh "
            "stay sorted the way you build them, all in one binder."
        ),
        visual="Banner: the binder fanned open showing loaded 12-pocket pages, a big '480' stat and icon tiles for 12 pockets and 20 pages on black. Red top-line and white headline.",
        alt="A+ banner showing the fanned-open binder with a 480-card capacity stat and 12-pocket, 20-page icon tiles.",
    ),
    AIModule(
        name="Module 4 — Zipper security banner",
        role="a+_banner",
        headline="ZIP IT SHUT, TAKE IT ANYWHERE",
        body=(
            "A zipper closure with a matching pull tab seals the binder on all sides, so cards stay put "
            "in a backpack or on the move. Side-loading pockets and low-friction black backing keep every "
            "card secure, with no rings to dent or snag your cards."
        ),
        visual="Banner: hand drawing the zipper around the closed vivid binder, thin arrows to the zip pull tab and side-loading pockets. Red top-line, white headline on black.",
        alt="A+ banner of a hand zipping the vivid binder shut, with callouts to the pull tab and side-loading pockets.",
    ),
    AIModule(
        name="Module 5 — Organize banner (12 pockets, playsets)",
        role="a+_banner",
        headline="12 POCKETS, EVERY PLAYSET",
        body=(
            "The 12-across pocket layout puts more cards on every page and gives each row a full 4-card "
            "playset, so your whole collection lives in one place, neatly sorted and easy to browse. "
            "Side-loading pockets are sized for standard trading cards."
        ),
        visual="Banner with a loaded 12-pocket page on black, one row bracketed as a 4-card playset, plus two icon-stat tiles: '12 POCKETS PER PAGE' and 'STORES UP TO 480 CARDS'. Red stat icons.",
        alt="A+ banner showing a 12-pocket page with a bracketed 4-card playset row and icon stats for pockets and capacity.",
    ),
    AIModule(
        name="Module 6 — Brand close (heritage + review)",
        role="a+_banner",
        headline="TRUSTED SINCE 1952",
        body=(
            "Collectors worldwide trust Ultra PRO for collectible protection — proudly Made in USA since "
            "1952. <br/><br/>“Crystal clear and durable, my cards are well-protected.” "
            "&#9733;&#9733;&#9733;&#9733;&#9733;"
        ),
        visual="Closing banner: Ultra PRO logo centered on black, zipped vivid binders softly behind, footer lockup with a USA-flag 'Made in USA' mark and 'Since 1952', a five-star review quote below.",
        alt="Ultra PRO brand-close banner: trusted by collectors worldwide, Made in USA since 1952, with a five-star review quote.",
    ),
]


# ENGLISH backend search terms — stem-deduped, no title/brand duplicates, ≤ 249 bytes.
BACKEND = (
    "zip up card binder no rings 720 card album sleeves toploader graded storage "
    "organizer holder display case leatherette playset deck yugioh gathering ccg "
    "collection memorabilia photo protector standard size 4 pocket 9 pocket"
)


def main() -> None:
    print("Loading Ultra PRO customer + parsing listing.xlsx…")
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
    builder._ai_qa = []       # client instruction (listings 35-50): no Q&A module
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
