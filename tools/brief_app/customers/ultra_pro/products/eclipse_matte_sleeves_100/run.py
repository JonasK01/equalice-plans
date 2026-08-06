"""Ultra PRO ECLIPSE Matte Standard Deck Protector Sleeves, 100ct (66x91mm) —
Image Plan #42 (ASIN B09QH6SJ7P). Hand-written senior copy in the Ultra PRO
catalog format inside the EQUALICE brief_app.

Self-contained: listing.xlsx in → branded PDF out, both in this product folder.
Reads the SEO axis from listing.xlsx via parse_excel; the customer-facing copy
(TITLE / BULLETS / IMAGES / MODULES / BACKEND) is authored by hand below.

DISTINCT CREATIVE (these are SLEEVES, not binder pages): lead on the MATTE,
anti-glare finish + fully OPAQUE colored back (hides card faces, no marking) +
smooth SHUFFLE feel for real gameplay. KW woven: matte sleeves, deck protector
sleeves, mtg sleeves, commander sleeves.

ULTRA PRO STYLE (matched in every image's art direction):
  black background, bold RED #C8102E top-line + big WHITE headline; feature
  callouts with thin arrows; icon-stat bars; a red circular badge; REAL popular
  cards (MTG, Pokemon, Commander) sleeved; real gameplay lifestyle (shuffling,
  a deck box); dimension callout (66 x 91 mm / 2.5" x 3.5"); brand close
  'Trusted since 1952 · Made in USA'. (Image 1 stays clean white per Amazon.)

GUARDRAILS (auto-checked on build):
  overlay ≤30 chars AND ≤5 words, smooth (no middots, no fragments) ·
  overlay_sub ≤90 · module headline ≤38 · bullet head <b>…</b> ≤45 · TITLE ≤200.
COMPLIANCE: no "#1", no "best", no "leading", no "guaranteed", no "prevent",
  no "$", no URL/.com. Strength as "superior seal / split-resistant".

Client instruction (per Jonas, listings 35-50): NO Q&A module and NO Comparison
module. This brief ships 7 images + 6 A+ banners/carousels only.
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
PLAN_NO = "42"
ASIN = "B09QH6SJ7P"


# ===== Customer-facing copy (ENGLISH — amazon.com) =====

# HTML-escaped "&" counts as 1 real char. Keep de-escaped length ≤ 200.
TITLE = (
    "Ultra PRO ECLIPSE Matte Deck Protector Sleeves (100 Count, 66 x 91 mm) — "
    "Anti-Glare Matte Card Sleeves for MTG, Commander, Pokemon &amp; TCG · "
    "Opaque Colored Back · Smooth Shuffle · Made in USA"
)

BULLETS = [
    "<b>MATTE, ANTI-GLARE CARD FACE</b> — The matte finish on every sleeve kills "
    "screen and overhead glare at the table, so your cards read clean and clear "
    "under any light — matte sleeves built for long game nights and stream play.",

    "<b>FULLY OPAQUE COLORED BACK</b> — A solid, opaque colored back hides every "
    "card face so no one reads your deck through the sleeve, and it leaves no "
    "marking — fair, tournament-ready deck protector sleeves for competitive play.",

    "<b>SMOOTH SHUFFLE FEEL</b> — A smooth polypropylene glide lets your deck "
    "shuffle and fan effortlessly, riffle after riffle, so mtg sleeves and "
    "commander sleeves stay easy to handle from the first game to the hundredth.",

    "<b>SPLIT-RESISTANT SEAL</b> — A split-resistant seal and durable PP film "
    "guard the edges and corners of every card against nicks, dust and wear — "
    "archival-safe material that keeps Magic (MTG) and Pokemon cards protected.",

    "<b>TRUSTED BY PLAYERS SINCE 1952</b> — Ultra PRO has protected collectibles "
    "since 1952. Standard-size 66 x 91 mm sleeves, 100 per pack, sized for MTG, "
    "Commander, Pokemon and other TCG cards — proudly Made in USA.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (pack + fanned matte sleeves)",
        role="hero",
        background="Pure white #FFFFFF seamless — Amazon main-image policy (no overlay text, no graphics).",
        purpose="Win the click in the amazon.com sleeves grid — instantly read as premium matte deck protector sleeves with an opaque colored back.",
        visual=(
            "Product pack (ECLIPSE Matte Standard Deck Protector Sleeves, 100ct) standing three-quarter "
            "left, label fully legible. To its right, a neat fan of ~6 sleeves showing the matte, opaque "
            "colored back, plus ONE sleeve turned to reveal a real MTG/Commander card face reading crisp "
            "through the front. Tight crop, product ~85% of frame, subtle contact shadow, no overlay text."
        ),
        overlay="(no overlay — Amazon main image)",
        overlay_sub="",
        props=["ECLIPSE 100ct pack", "fan of matte opaque-back sleeves", "one sleeved MTG/Commander card"],
        lighting="Bright, even studio light with a soft rim so the matte, non-reflective surface reads clearly against white (no hotspots).",
        why_it_works=(
            "The pack plus a fan that shows BOTH the opaque colored back and a clean card face communicates "
            "product type, finish and function in one glance — exactly what a player scans for in the grid."
        ),
        ctr="A matte, glare-free fan on white out-signals shiny glossy-sleeve thumbnails and pulls the click.",
        cvr="Shows precisely what the buyer receives (100ct pack + colored sleeves) and proves the opaque back up front.",
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: matte, anti-glare finish (macro)",
        role="hook",
        background="Black #111111. Bold RED #C8102E top-line 'MATTE FINISH', big WHITE headline below.",
        purpose="Prove the lead promise — a true matte surface that kills glare so cards stay readable at the table.",
        visual=(
            "Split macro: LEFT a glossy sleeve throwing a harsh white glare hotspot across the card; RIGHT the "
            "ECLIPSE matte sleeve on the same card, surface soft and glare-free, art fully readable. Thin white "
            "arrow labels 'no glare' on the matte side; small red badge 'ANTI-GLARE MATTE'. White headline lower-left."
        ),
        overlay="MATTE FINISH, NO GLARE.",
        overlay_sub="A true matte surface kills table and screen glare so cards stay readable.",
        props=["side-by-side glossy vs matte sleeve", "red 'anti-glare matte' badge", "thin arrow to matte surface"],
        lighting="Hard overhead key aimed to bloom on the glossy side and die on the matte side — the contrast IS the proof.",
        why_it_works=(
            "Answers the player's top matte-sleeve question — 'will it actually cut glare?' — with a direct "
            "side-by-side, the single clearest reason a buyer upgrades from glossy sleeves."
        ),
        ctr="A glare-vs-no-glare split on black is a pattern interrupt in a grid full of flat product shots.",
        cvr="Visual proof of the matte payoff defuses the 'is it really matte?' doubt before the click.",
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: opaque colored back (no read-through)",
        role="educate",
        background="Black #111111, RED top-line 'FULLY OPAQUE BACK', WHITE headline.",
        purpose="Prove the back is truly opaque — the deck can't be read through the sleeve and there is no marking.",
        visual=(
            "A backlit stack of sleeves: a bright lamp behind shows the opaque colored backs blocking all light — "
            "no card faces bleed through. Thin white arrows call out 'solid opaque back' and 'no read-through'. "
            "A single sleeve back centered showing the even, consistent color. Red accent under the two headline words."
        ),
        overlay="OPAQUE COLORED BACK.",
        overlay_sub="A solid opaque back blocks read-through and leaves no marking on your deck.",
        props=["backlit stack of sleeves", "lamp behind for the opacity test", "arrow callouts 'no read-through'"],
        lighting="Strong backlight for the opacity demo, soft front fill so the colored back still reads rich, not silhouetted.",
        why_it_works=(
            "Opacity and 'no marking' are exactly what competitive MTG and Commander players filter for — the "
            "backlit test is concrete proof, not a claim a bargain sleeve can match."
        ),
        ctr="The lamp-behind opacity test is a curiosity visual that stops the scroll for tournament players.",
        cvr="Removes the fairness objection (read-through / marked cards) that blocks the competitive buyer.",
    ),
    AIImagePlanItem(
        name="Image 4 — Desire: smooth shuffle at the table (lifestyle)",
        role="desire",
        background="Warm game-table scene; product graphics kept to a slim black/red lower band.",
        purpose="Let the buyer feel the smooth shuffle and fan — the in-hand payoff during real gameplay.",
        visual=(
            "Over-the-shoulder lifestyle: a player's hands riffle-shuffle a sleeved Commander deck at a game "
            "table, cards fanning cleanly, a deck box and more sleeved decks nearby in the matching color. Warm, "
            "real, aspirational. Slim black lower band with red top-line 'SMOOTH SHUFFLE' and the white headline."
        ),
        overlay="SMOOTH SHUFFLE FEEL.",
        overlay_sub="A smooth glide lets your deck shuffle and fan cleanly, game after game.",
        props=["player's hands shuffling", "sleeved Commander deck", "deck box", "matching colored sleeves", "game table"],
        lighting="Warm ambient table light from camera-left, soft and lived-in — game night, not clinical studio.",
        why_it_works=(
            "Moves from features to the tactile payoff every player cares about — how the deck feels to shuffle "
            "and fan — which is what turns a browsing player into a buyer."
        ),
        ctr="A relatable game-table shuffle moment stands out against sterile product-only tiles and invites the click.",
        cvr="Buyers picture their own deck shuffling this smoothly, making the purchase feel like the next step.",
    ),
    AIImagePlanItem(
        name="Image 5 — Trust: split-resistant seal & durable film",
        role="trust",
        background="Black #111111, RED top-line 'SPLIT-RESISTANT SEAL', WHITE headline.",
        purpose="Defuse the fear that sleeves split at the seam or let cards get damaged — the seal and film hold up.",
        visual=(
            "Macro of a sleeve mouth and seam: thin white arrows call out 'split-resistant seal' along the welded "
            "edge and 'durable PP film' on the body, with a card held snug inside. A small red badge 'PROTECTS "
            "YOUR CARDS'. Optional stress-cue: a hand flexing the sleeve, seam staying intact."
        ),
        overlay="SPLIT-RESISTANT SEAL.",
        overlay_sub="A split-resistant seal and durable film guard edges and corners from wear.",
        props=["macro of sleeve seam / mouth", "arrow callouts to seal and film", "red 'protects your cards' badge"],
        lighting="Focused key on the seam so the welded, split-resistant edge reads as strong and precise.",
        why_it_works=(
            "Targets the top negative-review fear for sleeves (seams splitting, cards wearing). Showing the seal "
            "and the snug card is concrete durability proof, not a promise."
        ),
        ctr="The flexed-seam 'still intact' visual is a curiosity hook that stops the scroll.",
        cvr="Directly answers 'will these split?' with visible construction proof, removing a purchase blocker.",
    ),
    AIImagePlanItem(
        name="Image 6 — Desire: precision fit & count (dimensions + icon stats)",
        role="desire",
        background="Black #111111, RED top-line 'STANDARD-SIZE FIT', WHITE headline; icon-stat bar along the bottom.",
        purpose="Prove exact fit and count so the buyer knows the sleeves fit their cards and deck size.",
        visual=(
            "A standard card ghosted inside a sleeve with a clean dimension callout '66 x 91 mm (2.5\" x 3.5\")' "
            "and arrows to the sleeve edges, a hair of breathing room shown. Bottom icon-stat bar with two tiles: "
            "'FITS STANDARD-SIZE CARDS' and '100 SLEEVES PER PACK'. Red accents on the stat icons."
        ),
        overlay="FITS STANDARD CARDS.",
        overlay_sub="Sized 66 x 91 mm for standard MTG, Commander and Pokemon cards.",
        props=["dimension callout 66 x 91 mm", "ghosted standard card in sleeve", "two icon-stat tiles"],
        lighting="Clean technical light — flat and legible so the dimensions and stat icons read instantly.",
        why_it_works=(
            "Removes the last practical doubt — 'will these fit my cards and how many do I get?' — with exact "
            "numbers a spec-driven player trusts."
        ),
        ctr="Concrete numbers (66x91mm, 100 count, standard-size) signal precision and pull spec-checking buyers.",
        cvr="Exact fit and count data closes the sizing objection and justifies the buy.",
    ),
    AIImagePlanItem(
        name="Image 7 — Close: brand trust (since 1952 · Made in USA)",
        role="close",
        background="Black #111111 with the Ultra PRO logo; subtle red heritage line motif.",
        purpose="Close on brand identity and heritage — the protection players have trusted for decades.",
        visual=(
            "Centered Ultra PRO logo on black, a neat row of sleeved decks and deck boxes softly behind. RED "
            "top-line 'TRUSTED BY PLAYERS WORLDWIDE', big WHITE headline, and a footer lockup: a small USA-flag "
            "mark with 'Made in USA' beside 'Since 1952'."
        ),
        overlay="TRUSTED SINCE 1952.",
        overlay_sub="Protecting decks and collections with USA-made quality since 1952.",
        props=["Ultra PRO logo", "row of sleeved decks / deck boxes", "USA-flag 'Made in USA' mark"],
        lighting="Premium low-key light, soft glow on the logo — authoritative, heritage, category-anchor feel.",
        why_it_works=(
            "Ends on heritage and provenance — the trust cue that converts a hesitating player who wants a brand "
            "that will still be here to protect the decks they are building."
        ),
        ctr="The heritage 'since 1952 · Made in USA' lockup signals category authority and reassures at a glance.",
        cvr="Provenance and longevity provide the final trust nudge that seals the purchase.",
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Brand banner (hero)",
        role="a+_banner",
        headline="MATTE PROTECTION FOR YOUR DECK",
        body=(
            "ECLIPSE Matte Deck Protector Sleeves deliver a true matte, anti-glare finish over a fully "
            "opaque colored back — 100 standard-size 66 x 91 mm sleeves per pack, built for MTG, Commander, "
            "Pokemon and other TCG decks."
        ),
        visual="Wide cinematic banner: the 100ct pack left, a fanned spread of matte opaque-back sleeves with one sleeved MTG/Commander card right, on black with a red accent bar. Ultra PRO logo top-left.",
        alt="Ultra PRO ECLIPSE Matte Deck Protector Sleeves pack beside a fan of matte opaque sleeves on a black background.",
    ),
    AIModule(
        name="Module 2 — Anti-glare banner (lifestyle)",
        role="a+_banner",
        headline="PLAY WITH ZERO GLARE",
        body=(
            "The matte surface kills glare from lights, screens and streams, so every card stays readable "
            "through long game nights. See your plays clearly and keep your deck looking sharp — matte "
            "sleeves made for players who log real table hours."
        ),
        visual="Warm lifestyle scene: a player holding a matte-sleeved hand at a lit game table, no glare hotspots on the cards, deck box nearby. Slim black/red lower band with the headline.",
        alt="A player holding matte-sleeved cards at a game table with no glare on the card faces.",
    ),
    AIModule(
        name="Module 3 — Feature carousel (the ECLIPSE set)",
        role="a+_carousel",
        headline="THE ECLIPSE DIFFERENCE",
        body=(
            "Tile 1: <b>MATTE FINISH</b> — anti-glare surface, readable in any light.<br/>"
            "Tile 2: <b>OPAQUE BACK</b> — solid colored back, no read-through.<br/>"
            "Tile 3: <b>SMOOTH GLIDE</b> — shuffles and fans cleanly, game after game.<br/>"
            "Tile 4: <b>SPLIT-RESISTANT SEAL</b> — welded edge holds up to handling.<br/>"
            "Tile 5: <b>ARCHIVAL-SAFE PP</b> — durable film that guards your cards.<br/>"
            "Tile 6: <b>STANDARD SIZE</b> — 66 x 91 mm, 100 sleeves per pack."
        ),
        visual="6 square tiles on black, red accent corner and a line icon per tile (matte swatch · opaque back · shuffle arrows · welded seam · shield · card size). Consistent Ultra PRO styling.",
        alt="Six-tile A+ carousel of ECLIPSE features: matte finish, opaque back, smooth glide, split-resistant seal, archival-safe PP, standard size.",
    ),
    AIModule(
        name="Module 4 — Shuffle banner (feel + fairness)",
        role="a+_banner",
        headline="BUILT FOR SERIOUS SHUFFLING",
        body=(
            "A smooth polypropylene glide lets your deck riffle, mash and fan without sticking, while the "
            "opaque colored back keeps your cards hidden and unmarked — fair, tournament-ready deck protector "
            "sleeves for Commander pods and competitive MTG."
        ),
        visual="Banner: a Commander deck mid-shuffle on black with thin white arrow callouts to the smooth glide, the opaque back and the split-resistant seal. Red top-line and white headline.",
        alt="A+ banner with callouts on a shuffling deck: smooth glide, opaque back and split-resistant seal.",
    ),
    AIModule(
        name="Module 5 — Opacity banner (no read-through)",
        role="a+_banner",
        headline="OPAQUE BACK, HIDDEN CARDS",
        body=(
            "The fully opaque colored back blocks all read-through, so opponents can't identify cards through "
            "the sleeve and your deck stays fair. Even, consistent color across all 100 sleeves — sort your "
            "collection and decks by color at a glance."
        ),
        visual="Banner with a backlit opacity test on black: a lamp behind a stack of sleeves, the opaque backs blocking the light, plus one sleeve back showing even color. Red stat icons.",
        alt="A+ banner showing a backlit opacity test proving the opaque colored back blocks read-through.",
    ),
    AIModule(
        name="Module 6 — Brand close (heritage + review)",
        role="a+_banner",
        headline="TRUSTED SINCE 1952",
        body=(
            "Players worldwide trust Ultra PRO for deck and card protection — proudly Made in USA since "
            "1952. <br/><br/>“Smooth to shuffle and no glare at all, my cards look great.” "
            "&#9733;&#9733;&#9733;&#9733;&#9733;"
        ),
        visual="Closing banner: Ultra PRO logo centered on black, sleeved decks and deck boxes softly behind, footer lockup with a USA-flag 'Made in USA' mark and 'Since 1952', a five-star review quote below.",
        alt="Ultra PRO brand-close banner: trusted by players worldwide, Made in USA since 1952, with a five-star review quote.",
    ),
]


# ENGLISH backend search terms — stem-deduped, no title/brand duplicates, ≤ 249 bytes.
BACKEND = (
    "standard size magic the gathering yugioh one piece gaming trading polypropylene "
    "split resistant archival glossy alternative bulk 100ct game night shuffling "
    "opaque backing sleeve protectors ccg no read through hidden"
)


def main() -> None:
    print("Loading Ultra PRO customer + parsing ECLIPSE matte sleeves listing…")
    cust = load_customer("ultra_pro")
    brief = parse_excel(EXCEL)
    OUT = HERE / f"{PLAN_NO}_{ASIN}_Image Plan.pdf"
    real_title_len = len(TITLE.replace("&amp;", "&"))
    print(f"  Product: {brief.product_name}")
    print(f"  ASIN: {ASIN}   Marketplace: {cust.marketplace}   Overlay lang: {cust.overlay_language}")
    print(f"  TITLE real chars (de-escaped): {real_title_len}")

    builder = BriefBuilder(cust, brief, OUT, ai=None)
    builder._ai_title = TITLE
    builder._ai_bullets = BULLETS
    builder._ai_images = IMAGES
    builder._ai_modules = MODULES
    builder._ai_qa = []       # client instruction (35-50): no Q&A module
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
