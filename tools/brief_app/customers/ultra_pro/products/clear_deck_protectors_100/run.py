"""Ultra PRO Clear Standard Deck Protectors (100 ct) — Image Plan + A+ (PLAN 45).

Hand-written senior copy in the Ultra PRO catalog format inside the EQUALICE
brief_app. Self-contained: reads listing.xlsx in this folder, writes the branded
PDF next to it. ASIN B005BFZAK4 — amazon.com / English.

PRODUCT (100% specific to THIS SKU): Ultra PRO CLEAR Standard-Size Deck
Protectors, 100 count — crystal-clear gloss sleeves that show the card face,
acid-free and made with NO PVC, standard size 66 x 91 mm, smooth and
shuffle-ready for Magic (MTG), Pokemon and other TCG / gaming cards.

CREATIVE LEAD (distinct from the pages SKU): CRYSTAL CLARITY (see the card face
sharply) + acid-free / no-PVC safety + shuffle-ready gameplay. Weave KW:
clear deck protectors, deck protector sleeves, mtg sleeves, card sleeves tcg.

ULTRA PRO STYLE (matched in the art direction of every image):
  black background, bold RED #C8102E top-line + big WHITE headline; feature
  callouts with thin arrows; icon-stat bars; a red circular clarity badge; REAL
  popular cards (Pokemon, MTG) inside the clear sleeves; real collector / player
  lifestyle; the product pack; a dimension callout (66 x 91 mm / 2.5" x 3.5");
  brand close 'Trusted since 1952 · Made in USA'. (Image 1 stays on clean white.)

GUARDRAILS (auto-checked on build):
  overlay ≤30 chars AND ≤5 words, smooth (no middots, no fragments) ·
  overlay_sub ≤90 · module headline ≤38 · bullet head <b>…</b> ≤45 · TITLE ≤200.
COMPLIANCE: no "#1", no "best", no "leading", no "guaranteed", no "prevent",
  no "$", no URL/.com. Heritage as "Trusted since 1952", clarity as "Crystal
  Clarity", protection as "guards / helps guard".

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
PLAN_NO = "45"
ASIN = "B005BFZAK4"


# ===== Customer-facing copy (ENGLISH — amazon.com) =====

# HTML-escaped "&" counts as 1 real char. Keep de-escaped length ≤ 200.
TITLE = (
    "Ultra PRO Clear Standard Deck Protectors (100 Count) — Crystal-Clear Card Sleeves "
    "for MTG, Pokemon &amp; TCG Gaming Cards · Acid-Free, No PVC · Fits Standard "
    "66 x 91 mm Cards · Made in USA"
)

BULLETS = [
    "<b>CRYSTAL-CLEAR CARD SLEEVES</b> — A high-clarity gloss finish shows off every "
    "Magic (MTG), Pokemon and TCG card in crystal detail, so the art stays sharp and true "
    "to color while these clear deck protectors keep it safe.",

    "<b>ACID-FREE, NO PVC MATERIAL</b> — Made from acid-free polypropylene with no PVC, "
    "these deck protector sleeves are archival-safe and will not yellow or harm your cards, "
    "guarding your collection against everyday wear.",

    "<b>SMOOTH, SHUFFLE-READY FIT</b> — A smooth gloss finish lets the sleeves slide and "
    "shuffle easily for fast, fair gameplay, while a snug standard fit keeps each card "
    "seated so your deck stays game-ready match after match.",

    "<b>FITS STANDARD-SIZE CARDS</b> — Sized 66 x 91 mm (2.5\" x 3.5\") to fit standard "
    "gaming and collectible cards, these mtg sleeves and tcg card sleeves suit Commander, "
    "Pokemon, sports and most standard-size decks.",

    "<b>TRUSTED BY COLLECTORS SINCE 1952</b> — 100 clear standard-size sleeves per pack from "
    "Ultra PRO, protecting collectibles since 1952. Archival, acid-free card sleeves for "
    "players and collectors — proudly Made in USA.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (sleeve pack + a sleeved card)",
        role="hero",
        background="Pure white #FFFFFF seamless — Amazon main-image policy (no overlay text, no graphics).",
        purpose="Win the click in the amazon.com card-sleeve grid — instantly read as crystal-clear, 100-count standard deck protectors.",
        visual=(
            "The 100-count Clear Deck Protectors pack standing three-quarter left, label fully legible. "
            "To its right, ONE clear-sleeved card held upright — a recognizable Pokemon or MTG card seen "
            "glass-clear through the sleeve so the art reads razor-sharp. A short fan of a few sleeved cards "
            "at the base. Tight crop, product ~85% of frame, subtle contact shadow, no overlay text."
        ),
        overlay="(no overlay — Amazon main image)",
        overlay_sub="",
        props=["100-count Clear Deck Protectors pack", "one clear-sleeved Pokemon / MTG card", "short fan of sleeved cards"],
        lighting="Bright, even studio light; soft rim on the sleeve edge so the crystal-clear plastic and card art pop against white.",
        why_it_works=(
            "The pack plus a glass-clear sleeved card communicates product type (clear deck protectors), count "
            "and clarity in one glance — the three things a player scans for in the sleeve grid."
        ),
        ctr="A recognizable card behind crystal-clear plastic out-signals generic empty-sleeve thumbnails and pulls the click.",
        cvr="Shows exactly what the buyer receives (pack + sleeves) and proves clarity up front, cutting hesitation.",
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: crystal clarity proof (macro)",
        role="hook",
        background="Black #111111. Bold RED #C8102E top-line 'CRYSTAL CLARITY', big WHITE headline below.",
        purpose="Prove the strongest promise — see every card in crystal detail through the clear gloss sleeve.",
        visual=(
            "Extreme macro of one sleeved holographic Pokemon / MTG card, edges razor-sharp through the "
            "glass-clear gloss film. A red circular badge top-right reads 'HIGH CLARITY'. A thin white arrow "
            "points to the clear front with a small 'gloss finish' tag. White headline lower-left."
        ),
        overlay="CRYSTAL-CLEAR PROTECTION.",
        overlay_sub="A high-clarity gloss front shows every card sharp and true to color.",
        props=["macro of a holo card in a clear sleeve", "red circular 'HIGH CLARITY' badge", "thin arrow to the clear front"],
        lighting="Hard raking side-light on black to make the clear film read as glass and reveal the crisp card art.",
        why_it_works=(
            "Answers the player's top question — 'will I still see my cards?' — with a proof macro, positioning "
            "these as the clear sleeve for showing off the collection."
        ),
        ctr="A giant, glass-clear holo card on black is a pattern interrupt in a grid full of flat sleeve packs.",
        cvr="Macro proof of clarity defuses the biggest fear (cloudy sleeves) before the click.",
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: acid-free / no-PVC material callouts",
        role="educate",
        background="Black #111111, RED top-line 'ARCHIVAL-SAFE MATERIAL', WHITE headline.",
        purpose="Stack the safety spec set that protects the collection — acid-free, no PVC, archival.",
        visual=(
            "One clear sleeve centered on black holding a card, thin white arrows radiating to labeled callouts: "
            "ACID-FREE · NO PVC · ARCHIVAL POLYPROPYLENE · WILL NOT YELLOW · HIGH-CLARITY GLOSS. "
            "Each callout with a small line icon. Red accent underlines under the two headline words."
        ),
        overlay="ACID-FREE, NO PVC.",
        overlay_sub="Archival polypropylene that will not yellow or harm your cards.",
        props=["clear sleeve holding a card (hero object)", "5 arrow callouts with line icons", "red accent underlines"],
        lighting="Even soft light on the sleeve, slightly brighter center so the product stays the focal point on black.",
        why_it_works=(
            "Turns spec words into a visual proof stack — acid-free / no-PVC / archival is exactly what a serious "
            "collector filters for and what a bargain sleeve cannot safely claim."
        ),
        ctr="A dense, well-organized safety-callout stack signals 'real protection' and earns the click from collectors.",
        cvr="Each callout removes a specific doubt (acid, PVC, yellowing), compounding trust toward purchase.",
    ),
    AIImagePlanItem(
        name="Image 4 — Desire: sleeving a deck (lifestyle)",
        role="desire",
        background="Warm gaming-table scene; product graphics kept to a slim black/red lower band.",
        purpose="Let the buyer self-cast into sleeving up a clean, protected deck they are proud to play.",
        visual=(
            "Over-the-shoulder lifestyle: a player's hands slide a card into a clear sleeve at a tidy gaming table, "
            "a sleeved MTG / Pokemon deck stacked nearby, cards reading crystal-clear. Warm, aspirational, real. "
            "Slim black lower band with red top-line 'SLEEVE YOUR DECK' and the white headline."
        ),
        overlay="SLEEVE YOUR WHOLE DECK.",
        overlay_sub="100 clear sleeves per pack — enough to protect a full standard deck.",
        props=["player's hands sleeving a card", "sleeved MTG / Pokemon deck", "clear sleeves", "tidy gaming table"],
        lighting="Warm natural table light from camera-left, soft and lived-in — hobbyist, not clinical.",
        why_it_works=(
            "Moves from features to the payoff — a clean, protected, game-ready deck — which is what turns a "
            "browsing player into a buyer."
        ),
        ctr="A relatable sleeve-up-your-deck moment stands out against sterile pack-only tiles and invites the click.",
        cvr="Buyers picture their own deck sleeved this way, and the 100-count line makes the buy feel sufficient.",
    ),
    AIImagePlanItem(
        name="Image 5 — Trust: smooth, shuffle-ready fit",
        role="trust",
        background="Black #111111, RED top-line 'SHUFFLE-READY', WHITE headline.",
        purpose="Defuse the gameplay fear that sleeves stick or bunch — these slide and shuffle smoothly.",
        visual=(
            "A fanned arc of sleeved cards mid-shuffle on black, motion cue showing them sliding cleanly. Thin white "
            "arrows call out 'smooth gloss finish' and 'snug standard fit'. A small red badge 'GAME-DAY READY'. "
            "One card shown seated snugly in its sleeve, not slipping."
        ),
        overlay="SHUFFLE-READY SLEEVES.",
        overlay_sub="A smooth gloss finish slides and shuffles cleanly for fast, fair gameplay.",
        props=["fanned arc of sleeved cards mid-shuffle", "arrow callouts to finish and fit", "red 'GAME-DAY READY' badge"],
        lighting="Focused key on the fanned arc so the smooth finish and clean slide read as playable, not sticky.",
        why_it_works=(
            "Targets a real gameplay objection (sleeves that stick or bunch when shuffling) with a concrete "
            "in-motion proof, not a promise."
        ),
        ctr="The mid-shuffle fan is a curiosity hook that stops the scroll for players.",
        cvr="Directly answers 'will these shuffle well?' with a visible slide cue, removing a purchase blocker.",
    ),
    AIImagePlanItem(
        name="Image 6 — Desire: precision fit & count (dimensions + icon stats)",
        role="desire",
        background="Black #111111, RED top-line 'SIZED TO FIT', WHITE headline; icon-stat bar along the bottom.",
        purpose="Prove exact size and count so the buyer knows it fits their cards and covers their deck.",
        visual=(
            "A single card ghosted inside a clear sleeve with a clean dimension callout '66 x 91 mm (2.5\" x 3.5\")' "
            "and arrows to the sleeve edges. Bottom icon-stat bar with two tiles: 'FITS STANDARD-SIZE CARDS' and "
            "'100 SLEEVES PER PACK'. Red accents on the stat icons."
        ),
        overlay="SIZED FOR STANDARD CARDS.",
        overlay_sub="Fits standard 66 x 91 mm (2.5 x 3.5 in) gaming and collectible cards.",
        props=["dimension callout 66 x 91 mm / 2.5\" x 3.5\"", "card ghosted inside a sleeve", "two icon-stat tiles"],
        lighting="Clean technical light — flat and legible so the dimensions and stat icons read instantly.",
        why_it_works=(
            "Removes the last practical doubts — 'will these fit my cards, and how many do I get?' — with exact "
            "numbers a spec-driven player trusts."
        ),
        ctr="Concrete numbers (66 x 91 mm, 100 count, standard size) signal precision and pull spec-checking buyers.",
        cvr="Exact fit and count data closes the sizing objection and justifies the buy.",
    ),
    AIImagePlanItem(
        name="Image 7 — Close: brand trust (since 1952 · Made in USA)",
        role="close",
        background="Black #111111 with the Ultra PRO logo; subtle red heritage line motif.",
        purpose="Close on brand identity and heritage — the protection players and collectors have trusted for decades.",
        visual=(
            "Centered Ultra PRO logo on black, a neat row of sleeved decks and packs softly behind. RED top-line "
            "'TRUSTED BY COLLECTORS WORLDWIDE', big WHITE headline, and a footer lockup: a small USA-flag mark with "
            "'Made in USA' beside 'Since 1952'."
        ),
        overlay="TRUSTED SINCE 1952.",
        overlay_sub="Protecting cards and collections with USA-made quality since 1952.",
        props=["Ultra PRO logo", "row of sleeved decks / packs", "USA-flag 'Made in USA' mark"],
        lighting="Premium low-key light, soft glow on the logo — authoritative, heritage, category-anchor feel.",
        why_it_works=(
            "Ends on heritage and provenance — the trust cue that converts a hesitating buyer who wants a brand "
            "that will still be here to protect the collection they are building."
        ),
        ctr="The heritage 'since 1952 / Made in USA' lockup signals category authority and reassures at a glance.",
        cvr="Provenance and longevity provide the final trust nudge that seals the purchase.",
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Brand banner (hero)",
        role="a+_banner",
        headline="CRYSTAL-CLEAR CARD PROTECTION",
        body=(
            "Clear Standard Deck Protectors deliver crystal-clear protection for Magic (MTG), Pokemon and "
            "other TCG cards — a high-clarity gloss finish, acid-free and made with no PVC. 100 clear "
            "standard-size sleeves per pack, ready for your deck."
        ),
        visual="Wide cinematic banner: the 100-count pack left, a fanned spread of clear-sleeved cards (Pokemon, MTG) right, on black with a red accent bar. Ultra PRO logo top-left.",
        alt="Ultra PRO Clear Deck Protectors pack beside a fan of clear-sleeved trading cards on a black background.",
    ),
    AIModule(
        name="Module 2 — Lifestyle banner",
        role="a+_banner",
        headline="PROTECT WHAT MATTERS MOST",
        body=(
            "From your first Pokemon pull to a Commander staple, keep every card safe in crystal-clear "
            "sleeves made for players and collectors. Acid-free and no PVC, so the cards you love stay "
            "sharp and true to color, match after match."
        ),
        visual="Warm lifestyle scene: a player sleeving a card at a gaming table, a sleeved deck stacked nearby, soft daylight. Slim black/red lower band with the headline.",
        alt="A player sleeving trading cards into clear deck protectors at a gaming table.",
    ),
    AIModule(
        name="Module 3 — Feature carousel (the clear set)",
        role="a+_carousel",
        headline="THE CLEAR DIFFERENCE",
        body=(
            "Tile 1: <b>CRYSTAL CLARITY</b> — a high-clarity gloss front shows every card.<br/>"
            "Tile 2: <b>ACID-FREE</b> — archival-safe, will not harm your cards.<br/>"
            "Tile 3: <b>NO PVC</b> — polypropylene material that will not yellow.<br/>"
            "Tile 4: <b>SHUFFLE-READY</b> — a smooth finish slides and shuffles cleanly.<br/>"
            "Tile 5: <b>STANDARD FIT</b> — sized 66 x 91 mm for standard cards.<br/>"
            "Tile 6: <b>100 PER PACK</b> — enough to sleeve a full standard deck."
        ),
        visual="6 square tiles on black, red accent corner and a line icon per tile (sparkle · shield · no-PVC · shuffle arrows · ruler · pack). Consistent Ultra PRO styling.",
        alt="Six-tile A+ carousel of Clear Deck Protector features: crystal clarity, acid-free, no PVC, shuffle-ready, standard fit, 100 per pack.",
    ),
    AIModule(
        name="Module 4 — Protection banner (material callouts)",
        role="a+_banner",
        headline="BUILT TO PROTECT YOUR CARDS",
        body=(
            "Acid-free, no-PVC polypropylene guards Magic (MTG), Pokemon, Commander and other TCG cards from "
            "dust, fingerprints and everyday wear, while the crystal-clear gloss front keeps the art sharp — "
            "archival-safe sleeves that will not yellow your collection."
        ),
        visual="Banner: one clear sleeve holding a card centered on black with thin white arrow callouts to the acid-free, no-PVC material, archival polypropylene and clear gloss front. Red top-line and white headline.",
        alt="A+ banner with callouts pointing to the acid-free, no-PVC, archival material and clear gloss front of a card sleeve.",
    ),
    AIModule(
        name="Module 5 — Fit & count banner (icon stats)",
        role="a+_banner",
        headline="SIZED AND READY TO PLAY",
        body=(
            "Sized 66 x 91 mm (2.5\" x 3.5\") to fit standard gaming and collectible cards, with 100 sleeves in "
            "every pack — enough to protect a full standard deck. A smooth gloss finish keeps them shuffle-ready "
            "for fast, fair gameplay."
        ),
        visual="Banner with two large icon-stat tiles on black: 'FITS STANDARD-SIZE CARDS (66 x 91 mm)' and '100 SLEEVES PER PACK', a sleeved deck alongside. Red stat icons.",
        alt="A+ banner with icon stats: fits standard-size 66 x 91 mm cards and 100 sleeves per pack.",
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
        visual="Closing banner: Ultra PRO logo centered on black, sleeved decks softly behind, footer lockup with a USA-flag 'Made in USA' mark and 'Since 1952', a five-star review quote below.",
        alt="Ultra PRO brand-close banner: trusted by collectors worldwide, Made in USA since 1952, with a five-star review quote.",
    ),
]


# ENGLISH backend search terms — stem-deduped, no title/brand duplicates, ≤ 249 bytes.
BACKEND = (
    "glossy gloss sleeve deck box binder toploader storage ccg commander edh yugioh "
    "one piece flesh blood lorcana digimon polypropylene colored matte outer inner "
    "bulk 100ct standard size protector collectible player game night"
)


def main() -> None:
    print("Loading Ultra PRO customer + parsing listing.xlsx (plan 45)…")
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
    builder._ai_qa = []          # client instruction: no Q&A module
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
