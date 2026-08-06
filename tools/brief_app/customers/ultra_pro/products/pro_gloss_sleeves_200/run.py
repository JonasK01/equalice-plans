"""Ultra PRO PRO-Gloss Standard Deck Protector Sleeves — 200ct, BLACK — Image Plan (PLAN 46).

Hand-written senior copy in the Ultra PRO catalog format, built with the EQUALICE
brief_app. Self-contained: listing.xlsx in (SEO axis), branded PDF out — both live in
this product folder. Parses the SEO listing for product_name/USPs/keywords, then the
title / bullets / 7 images / 6 A+ modules / backend are all hand-written below.

DISTINCT CREATIVE ANGLE (vs. the other Ultra PRO SKUs): this is a SLEEVE, not a page.
Lead on the three things that make PRO-Gloss different — a GLOSSY, crystal-clear front
that shows the card, an OPAQUE BLACK back (no peeking, no marking during play), and the
big 200-count value pack for deck-builders and double-sleevers. Woven KW: gloss sleeves,
deck protector sleeves, black sleeves, commander sleeves, standard size card sleeves.

ULTRA PRO STYLE (art direction of every image): black background, bold RED #C8102E
top-line + big WHITE headline; thin-arrow feature callouts; icon-stat bars; a red
circular badge; REAL cards (MTG/Commander, Pokemon, One Piece, sports); real collector /
gameplay lifestyle; the product box; a size callout (2.5" x 3.5" / 66 x 91 mm); brand
close 'Trusted since 1952 · Made in USA'. Image 1 stays on clean white per Amazon policy.

GUARDRAILS (auto-checked on build):
  overlay ≤30 chars AND ≤5 words, smooth (no middots) · overlay_sub ≤90 ·
  module headline ≤38 · bullet head <b>…</b> ≤45 · TITLE ≤200.
COMPLIANCE: no "#1", no "best", no "leading", no "guaranteed", no "prevent", no "$",
  no URL/.com. Heritage as "Trusted since 1952", clarity as "Crystal / High Clarity".

Client instruction (listings 35-50): NO Q&A module and NO Comparison module.
Ships 7 images + 6 A+ banners/carousels.
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
PLAN_NO = "46"
ASIN = "B0CNJ85YDC"


# ===== Customer-facing copy (ENGLISH — amazon.com) =====

# HTML-escaped "&" counts as 1 real char. Keep de-escaped length ≤ 200.
TITLE = (
    "Ultra PRO PRO-Gloss Standard Deck Protector Sleeves (200 Count, Black) — Glossy Clear "
    "Front, Opaque Black Back for MTG Commander, Pokemon &amp; TCG · Acid-Free, No PVC · "
    "Made in USA"
)

BULLETS = [
    "<b>GLOSSY CLEAR FRONT, OPAQUE BACK</b> — PRO-Gloss deck protector sleeves pair a high-gloss, "
    "crystal-clear front that shows off every card with a solid opaque black back — so your MTG, "
    "Commander, Pokemon and TCG cards read sharp on the table while the back stays private.",

    "<b>OPAQUE BLACK BACK — NO PEEKING</b> — The fully opaque black back hides your cards from "
    "across the table and keeps every sleeve looking identical, so there is no marking and no "
    "reading your hand during commander and competitive play.",

    "<b>200-COUNT VALUE PACK</b> — A generous 200 sleeves per box gives you enough black card "
    "sleeves to protect a full deck or double-sleeve your favorites, with plenty of spares — great "
    "value for deck-builders who sleeve more than one commander deck.",

    "<b>STANDARD SIZE, SNUG FIT</b> — Sized for standard cards up to 66 x 91 mm (2.5\" x 3.5\"), "
    "these standard size card sleeves fit MTG, Pokemon, One Piece and most TCG cards snugly, with "
    "smooth gloss faces that shuffle easily and slide clean in and out of the deck.",

    "<b>TRUSTED BY COLLECTORS SINCE 1952</b> — Made from acid-free, non-PVC polypropylene to keep "
    "cards safe over the long haul. Ultra PRO has protected collections since 1952 — proudly "
    "Made in USA.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (product box + fanned sleeves)",
        role="hero",
        background="Pure white #FFFFFF seamless — Amazon main-image policy (no overlay text, no graphics).",
        purpose="Win the click in the amazon.com sleeve grid — instantly read as glossy-front, black-back, 200-count sleeves.",
        visual=(
            "Product box (PRO-Gloss Standard Deck Protector Sleeves, 200ct, Black) standing three-quarter left, "
            "label fully legible with the '200' count clear. To its right, a small fan of sleeves: two front-facing "
            "sleeves showing real cards (MTG/Commander, a Pokemon) glass-clear through the glossy front, and two "
            "flipped to show the solid opaque BLACK back. Tight crop, product ~85% of frame, soft contact shadow, "
            "no overlay text."
        ),
        overlay="(no overlay — Amazon main image)",
        overlay_sub="",
        props=["PRO-Gloss product box (200ct)", "two front sleeves with real cards", "two flipped black-back sleeves"],
        lighting="Bright, even studio light; soft rim on the sleeve edges so the glossy front reads as glass and the black back reads deep and solid.",
        why_it_works=(
            "The box plus front-and-back sleeves shows product type, the glossy-clear-front / opaque-black-back "
            "combo and the 200 count in one glance — the three things a deck-builder scans for in the grid."
        ),
        ctr="Real cards behind glossy plastic beside a solid black back out-signal flat, empty-sleeve thumbnails and pull the click.",
        cvr="Shows exactly what the buyer receives and proves both the clear front and the opaque back up front, cutting hesitation.",
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: glossy front, black back (macro)",
        role="hook",
        background="Black #111111. Bold RED #C8102E top-line 'PRO-GLOSS FINISH', big WHITE headline below.",
        purpose="Prove the signature combo — a glossy crystal-clear front and a fully opaque black back — in one macro.",
        visual=(
            "Split macro: LEFT, a sleeved holo card seen through the glossy clear front, edges razor-sharp and the "
            "gloss catching a clean highlight; RIGHT, the same sleeve flipped to a solid, even opaque black back. A "
            "thin white arrow labels 'glossy clear front' on the left and 'opaque black back' on the right. White "
            "headline lower-left."
        ),
        overlay="GLOSSY FRONT, BLACK BACK.",
        overlay_sub="A crystal-clear glossy front and a solid opaque black back in one sleeve.",
        props=["macro of a holo card through a glossy front", "flipped solid black back", "two thin arrow labels"],
        lighting="Hard raking side-light on black so the gloss front reads as glass and the black back stays deep and matte-solid.",
        why_it_works=(
            "Answers the buyer's core question — 'will my cards show clearly, and is the back truly opaque?' — with "
            "a single side-by-side proof macro that no generic sleeve thumbnail matches."
        ),
        ctr="A glossy holo card beside a pure-black back is a pattern interrupt in a grid full of flat sleeve shots.",
        cvr="Side-by-side proof of the clear front and opaque back defuses the two biggest sleeve fears before the click.",
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: feature callouts",
        role="educate",
        background="Black #111111, RED top-line 'BUILT FOR PROTECTION', WHITE headline.",
        purpose="Stack the PRO-Gloss feature set as scannable arrow callouts a bargain sleeve can't claim.",
        visual=(
            "One sleeve centered on black, thin white arrows radiating to labeled callouts: "
            "GLOSSY CLEAR FRONT · OPAQUE BLACK BACK · ACID-FREE · NO PVC · SNUG STANDARD FIT · SHUFFLE-SMOOTH. "
            "Each callout with a small line icon. Red accent underlines under the two headline words."
        ),
        overlay="BUILT TO PROTECT DECKS",
        overlay_sub="Glossy clear front, opaque back, acid-free and non-PVC material.",
        props=["single sleeve (hero object)", "6 arrow callouts with line icons", "red accent underlines"],
        lighting="Even soft light on the sleeve, slightly brighter center so the product stays the focal point on black.",
        why_it_works=(
            "Turns spec words into a visual proof stack — acid-free / non-PVC plus the glossy-front / opaque-back "
            "combo is exactly what a serious player filters for and what a cheap sleeve cannot claim."
        ),
        ctr="A dense, organized feature stack signals 'serious deck protection' and earns the click from competitive players.",
        cvr="Each callout removes a specific doubt (material, clarity, opacity, fit), compounding trust toward purchase.",
    ),
    AIImagePlanItem(
        name="Image 4 — Desire: sleeved deck on the table (lifestyle)",
        role="desire",
        background="Warm gameplay scene; product graphics kept to a slim black/red lower band.",
        purpose="Let the buyer self-cast into a clean, protected, tournament-ready deck at the table.",
        visual=(
            "Over-the-shoulder lifestyle: a player shuffles a sleeved MTG/Commander deck on a play mat, the glossy "
            "fronts catching light and the uniform black backs facing up in a neat stack. A few Pokemon and One Piece "
            "cards fanned nearby, all sleeved. Warm, real hobby scene. Slim black lower band with red top-line "
            "'SHUFFLE-READY' and the white headline."
        ),
        overlay="SHUFFLE-READY EVERY GAME",
        overlay_sub="Smooth glossy faces shuffle easily and slide clean in and out of the deck.",
        props=["player's hands shuffling", "sleeved commander deck", "black-back stack", "play mat", "sleeved TCG cards"],
        lighting="Warm natural table light from camera-left, soft and lived-in — game-night, not clinical.",
        why_it_works=(
            "Moves from features to the payoff — a clean, tournament-ready deck the player is proud to bring — which "
            "turns a browsing deck-builder into a buyer."
        ),
        ctr="A relatable game-night moment stands out against sterile product-only tiles and invites the click.",
        cvr="Buyers picture their own deck sleeved and uniform, making the purchase feel like the next step.",
    ),
    AIImagePlanItem(
        name="Image 5 — Trust: opaque back, no peeking",
        role="trust",
        background="Black #111111, RED top-line 'FULLY OPAQUE BACK', WHITE headline.",
        purpose="Defuse the fear that a thin back lets opponents read the deck or that sleeves get marked.",
        visual=(
            "A back-lit test: a bright light source BEHIND a fan of the opaque black sleeves shows zero card "
            "silhouettes bleeding through — the backs read solid and identical. A thin white arrow calls out "
            "'no see-through' and a small red badge reads 'UNIFORM BACKS'. Beside it, one sleeve front stays "
            "glass-clear for contrast."
        ),
        overlay="OPAQUE, NO PEEKING.",
        overlay_sub="A solid opaque black back hides your cards and keeps every sleeve identical.",
        props=["back-lit fan of black sleeves (no bleed-through)", "arrow 'no see-through'", "red 'uniform backs' badge"],
        lighting="Strong backlight to prove opacity, keeping the fronts on black moody and premium.",
        why_it_works=(
            "Targets the top competitive-play fear (thin or inconsistent backs that reveal or mark cards). A "
            "back-lit opacity test is concrete proof, not a promise."
        ),
        ctr="The back-lit 'nothing shows through' visual is a curiosity hook that stops the scroll.",
        cvr="Directly answers 'can opponents read my cards?' with a visible opacity test, removing a purchase blocker.",
    ),
    AIImagePlanItem(
        name="Image 6 — Desire: 200-count value & standard fit (icon stats)",
        role="desire",
        background="Black #111111, RED top-line 'BIG 200-COUNT PACK', WHITE headline; icon-stat bar along the bottom.",
        purpose="Prove the pack size and exact fit so the buyer knows it covers their deck and their cards.",
        visual=(
            "A tall stack / spread of sleeves labeled '200 SLEEVES' with a single card ghosted inside one sleeve and "
            "a clean size callout '2.5\" x 3.5\"  ·  66 x 91 mm' with arrows to the edges. Bottom icon-stat bar with "
            "two tiles: 'STANDARD SIZE FIT' and 'SLEEVE A FULL DECK'. Red accents on the stat icons."
        ),
        overlay="200 SLEEVES, GREAT VALUE.",
        overlay_sub="Enough sleeves to protect a full deck or double-sleeve your favorites.",
        props=["stack of 200 sleeves", "size callout 2.5\" x 3.5\" / 66 x 91 mm", "two icon-stat tiles"],
        lighting="Clean technical light — flat and legible so the count and dimensions read instantly.",
        why_it_works=(
            "Removes the last practical doubts — 'will it fit my cards, and is 200 enough?' — with exact numbers a "
            "spec-driven deck-builder trusts."
        ),
        ctr="Concrete numbers (200 count, 2.5x3.5, standard size) signal precision and pull spec-checking buyers.",
        cvr="Exact count and fit data closes the sizing and quantity objections and justifies the buy.",
    ),
    AIImagePlanItem(
        name="Image 7 — Close: brand trust (since 1952 · Made in USA)",
        role="close",
        background="Black #111111 with the Ultra PRO logo; subtle red heritage line motif.",
        purpose="Close on brand identity and heritage — the protection players and collectors have trusted for decades.",
        visual=(
            "Centered Ultra PRO logo on black, a neat row of sleeved decks and deck boxes softly behind. RED top-line "
            "'TRUSTED BY COLLECTORS WORLDWIDE', big WHITE headline, and a footer lockup: a small USA-flag mark with "
            "'Made in USA' beside 'Since 1952'."
        ),
        overlay="TRUSTED SINCE 1952",
        overlay_sub="Protecting cards and collections with USA-made quality since 1952.",
        props=["Ultra PRO logo", "row of sleeved decks / deck boxes", "USA-flag 'Made in USA' mark"],
        lighting="Premium low-key light, soft glow on the logo — authoritative, heritage, category-anchor feel.",
        why_it_works=(
            "Ends on heritage and provenance — the trust cue that converts a hesitating buyer who wants a brand that "
            "stands behind the cards they play and collect."
        ),
        ctr="The heritage 'since 1952 · Made in USA' lockup signals category authority and reassures at a glance.",
        cvr="Provenance and longevity provide the final trust nudge that seals the purchase.",
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Brand banner (hero)",
        role="a+_banner",
        headline="GLOSSY FRONT. OPAQUE BLACK BACK.",
        body=(
            "PRO-Gloss Standard Deck Protector Sleeves pair a high-gloss, crystal-clear front with a solid "
            "opaque black back — so your cards read sharp on the table while the back stays private. 200 "
            "sleeves per box, sized for standard cards, acid-free and non-PVC."
        ),
        visual="Wide cinematic banner: product box left, a fan of sleeves right — half front-facing with real cards (MTG/Commander, Pokemon, One Piece), half flipped to solid black backs, on black with a red accent bar. Ultra PRO logo top-left.",
        alt="Ultra PRO PRO-Gloss deck protector sleeves box beside a fan of glossy-front and opaque black-back sleeves on a black background.",
    ),
    AIModule(
        name="Module 2 — Gameplay banner",
        role="a+_banner",
        headline="SLEEVE UP. PROTECT YOUR DECK.",
        body=(
            "From your Commander pod to a competitive TCG event, keep every card safe behind a smooth glossy "
            "front and a uniform opaque back. Shuffle-friendly faces slide clean in and out of the deck, and "
            "acid-free, non-PVC material keeps cards safe game after game."
        ),
        visual="Warm gameplay scene: a player shuffling a sleeved deck on a play mat, glossy fronts catching light, uniform black backs stacked. Slim black/red lower band with the headline.",
        alt="A player shuffling a black-backed sleeved deck on a play mat at game night.",
    ),
    AIModule(
        name="Module 3 — Feature carousel (the PRO-Gloss set)",
        role="a+_carousel",
        headline="THE PRO-GLOSS DIFFERENCE",
        body=(
            "Tile 1: <b>GLOSSY CLEAR FRONT</b> — high-gloss face shows every card sharp.<br/>"
            "Tile 2: <b>OPAQUE BLACK BACK</b> — solid back, no peeking, no marking.<br/>"
            "Tile 3: <b>ACID-FREE, NO PVC</b> — archival polypropylene keeps cards safe.<br/>"
            "Tile 4: <b>STANDARD SIZE FIT</b> — snug fit for cards up to 66 x 91 mm.<br/>"
            "Tile 5: <b>SHUFFLE-SMOOTH</b> — smooth faces shuffle easily and deal clean.<br/>"
            "Tile 6: <b>200-COUNT PACK</b> — enough to sleeve or double-sleeve a deck."
        ),
        visual="6 square tiles on black, red accent corner and a line icon per tile (gloss card · solid black back · leaf/no-PVC · ruler fit · shuffle arrows · stacked 200). Consistent Ultra PRO styling.",
        alt="Six-tile A+ carousel of PRO-Gloss features: glossy clear front, opaque black back, acid-free no PVC, standard size fit, shuffle-smooth, 200-count pack.",
    ),
    AIModule(
        name="Module 4 — Opacity banner (no peeking)",
        role="a+_banner",
        headline="A FULLY OPAQUE BLACK BACK",
        body=(
            "The solid opaque black back hides your cards from across the table and keeps every sleeve looking "
            "identical — so there is no reading your hand and no marked cards during Commander and competitive "
            "play. Front stays crystal-clear so you still see every card you play."
        ),
        visual="Banner: a back-lit fan of black sleeves showing no card silhouettes bleeding through, one clear front beside for contrast, thin white arrow callout 'no see-through'. Red top-line and white headline.",
        alt="A+ banner with a back-lit opacity test showing the solid black sleeve backs with no card bleed-through.",
    ),
    AIModule(
        name="Module 5 — Fit & value banner (icon stats)",
        role="a+_banner",
        headline="200 SLEEVES, STANDARD FIT",
        body=(
            "Sized for standard cards up to 66 x 91 mm (2.5\" x 3.5\"), PRO-Gloss sleeves fit MTG, Pokemon, "
            "One Piece and most TCG cards snugly. With 200 sleeves per box, you get enough black card sleeves "
            "to protect a full deck or double-sleeve your favorites, with spares to keep on hand."
        ),
        visual="Banner with two large icon-stat tiles on black: 'STANDARD SIZE FIT (66 x 91 mm)' and 'SLEEVE A FULL DECK', a stack of sleeves and a sleeved card alongside. Red stat icons.",
        alt="A+ banner with icon stats: standard size fit up to 66 x 91 mm and 200 sleeves to protect a full deck.",
    ),
    AIModule(
        name="Module 6 — Brand close (heritage + review)",
        role="a+_banner",
        headline="TRUSTED SINCE 1952",
        body=(
            "Players and collectors worldwide trust Ultra PRO for card protection — proudly Made in USA since "
            "1952. <br/><br/>“Crystal clear and durable, my cards are well-protected.” "
            "&#9733;&#9733;&#9733;&#9733;&#9733;"
        ),
        visual="Closing banner: Ultra PRO logo centered on black, sleeved decks and deck boxes softly behind, footer lockup with a USA-flag 'Made in USA' mark and 'Since 1952', a five-star review quote below.",
        alt="Ultra PRO brand-close banner: trusted by collectors worldwide, Made in USA since 1952, with a five-star review quote.",
    ),
]


# ENGLISH backend search terms — stem-deduped, no title/brand duplicates, ≤ 249 bytes.
BACKEND = (
    "gloss card sleeves deck protectors black matte polypropylene tcg ccg toploader "
    "double sleeve inner shuffle yugioh gathering one piece lorcana digimon standard "
    "66x91 66 91 mm collector gaming bulk 200ct"
)


def main() -> None:
    print("Loading Ultra PRO customer + parsing PRO-Gloss 200ct listing…")
    cust = load_customer("ultra_pro")
    brief = parse_excel(EXCEL)
    OUT = HERE / f"{PLAN_NO}_{ASIN}_Image Plan.pdf"
    real_title_len = len(TITLE.replace("&amp;", "&"))
    print(f"  Product: {brief.product_name}")
    print(f"  ASIN: {ASIN}  Marketplace: {cust.marketplace}  Overlay lang: {cust.overlay_language}")
    print(f"  TITLE real chars (de-escaped): {real_title_len}")

    builder = BriefBuilder(cust, brief, OUT, ai=None)
    builder._ai_title = TITLE
    builder._ai_bullets = BULLETS
    builder._ai_images = IMAGES
    builder._ai_modules = MODULES
    builder._ai_backend = BACKEND
    builder._ai_qa = []  # client instruction (listings 35-50): no Q&A module
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
