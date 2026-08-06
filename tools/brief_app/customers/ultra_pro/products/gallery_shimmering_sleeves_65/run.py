"""Ultra PRO GALLERY SERIES 'Shimmering Skyline' Deck Protector Sleeves (65 ct)
— Image Plan #48 (ASIN B08WYG1PK9, amazon.com / English).

A hand-written senior brief for an ARTISTIC designer sleeve. Unlike the standard
Ultra PRO protection SKUs, THE ARTWORK IS THE HERO here: the shimmering skyline
design and standing out at the table lead; archival protection plays support.

NOTE ON THE FOLDER NAME: the folder is 'gallery_shimmering_sleeves_65' and an old
label called this 'Eclipse Pacific Blue' — both are WRONG for the customer copy.
We TRUST listing.xlsx, which parses the product as the Gallery Series 'Shimmering
Skyline' Deck Protector Sleeves. All copy below is for the Shimmering Skyline art.

LANGUAGE: amazon.com — all customer copy (TITLE, BULLETS, overlays, modules,
backend) in English. Art-direction fields are English too.

ULTRA PRO STYLE (matched in the art direction): black background, bold RED
#C8102E top-line + big WHITE headline; feature callouts with thin arrows; the
product box; a red circular badge; real popular cards (Pokemon, MTG, One Piece)
sleeved to show the art; brand close 'Trusted since 1952'. Image 1 stays on a
clean white background per Amazon main-image policy. For THIS art SKU the black
canvas doubles as a gallery wall so the shimmering skyline artwork pops.

GUARDRAILS (auto-checked on build):
  overlay ≤30 chars AND ≤5 words, smooth (no middots) · overlay_sub ≤90 ·
  module headline ≤38 · bullet head <b>…</b> ≤45 · TITLE ≤200.
COMPLIANCE: no "#1", no "best", no "leading", no "guaranteed", no "prevent",
  no "$", no URL/.com. (The USP's "help prevent peeling" is reworded to
  "resist peeling".) 6 A+ modules, a+_banner / a+_carousel ONLY — NO Q&A,
  NO Comparison (client instruction for listings 35-50).
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
PLAN_NO = "48"
ASIN = "B08WYG1PK9"


# ===== Customer-facing copy (ENGLISH — amazon.com) =====

# HTML-escaped "&amp;" counts as 1 real char. Keep de-escaped length ≤ 200.
TITLE = (
    "Ultra PRO Gallery Series Shimmering Skyline Deck Protector Sleeves (65 Count) "
    "— Art Trading Card Deck Sleeves for Pokemon, MTG &amp; TCG · Standard 2.5 x 3.5 in "
    "· Archival, No PVC · Since 1952"
)

BULLETS = [
    "<b>SHIMMERING SKYLINE ARTWORK</b> — Full-color Gallery Series artwork turns every card sleeve "
    "into a piece of art, so your deck reads as a curated collection and your Pokemon, Magic (MTG) "
    "and TCG cards stand out the moment they hit the table.",

    "<b>PROTECTION THAT KEEPS UP</b> — Behind the art, these are true deck protector sleeves: a snug "
    "standard fit and DECK PROTECTOR technology engineered to resist peeling and lifting keep every "
    "card guarded through shuffle after shuffle.",

    "<b>ARCHIVAL, NO-PVC MATERIAL</b> — Made from archival-safe, acid-free polypropylene with no PVC, "
    "so these art sleeves stay clear and true to color and keep your cards safe for the long haul, "
    "on the table or in storage.",

    "<b>SIZED FOR STANDARD CARDS</b> — Each pack holds 65 sleeves cut for standard 2.5 x 3.5 inch "
    "cards, an easy fit for Pokemon, Magic the Gathering, One Piece and most trading card games — "
    "lightweight art sleeves ready for deck or display.",

    "<b>TRUSTED BY COLLECTORS SINCE 1952</b> — Ultra PRO has protected collectibles since 1952. "
    "The Gallery Series pairs that heritage with designer card sleeves, so you protect what matters "
    "most while showing off your style.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (pack + fanned art sleeves)",
        role="hero",
        background="Pure white #FFFFFF seamless — Amazon main-image policy (no overlay text, no graphics).",
        purpose="Win the click in the amazon.com sleeve grid — instantly read as a premium designer art sleeve, not a plain sleeve.",
        visual=(
            "Gallery Series 'Shimmering Skyline' pack standing three-quarter left, label and artwork fully legible. "
            "To its right, a clean fan of 4-5 sleeves showing the shimmering skyline art, one sleeving a real card so "
            "the fit is obvious. Tight crop, product ~85% of frame, subtle contact shadow, no overlay text."
        ),
        overlay="(no overlay — Amazon main image)",
        overlay_sub="",
        props=["Gallery Series Shimmering Skyline pack", "fan of 4-5 art sleeves", "one real card sleeved"],
        lighting="Bright, even studio light with a soft rim so the shimmering skyline art catches highlights and pops against white.",
        why_it_works=(
            "The pack plus a fan of the shimmering art communicates product type (designer deck protector sleeves), "
            "count and the artwork in one glance — exactly what an art-sleeve buyer scans for."
        ),
        ctr="A shimmering illustrated sleeve out-signals the sea of plain matte-black sleeve thumbnails and pulls the click.",
        cvr="Shows the actual artwork and a real card in a sleeve up front, proving both the look and the fit.",
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: the shimmering skyline artwork (macro)",
        role="hook",
        background="Black #111111 gallery wall. Bold RED #C8102E top-line 'GALLERY SERIES', big WHITE headline below.",
        purpose="Lead on the single strongest reason to buy — the artwork — shown large enough to fall for.",
        visual=(
            "Extreme macro of one sleeve so the shimmering skyline artwork fills the frame, highlights catching the "
            "light like a real gallery print. A small red circular badge top-right reads 'GALLERY SERIES ART'. White "
            "headline lower-left. The black canvas reads as a museum wall so the art is the hero."
        ),
        overlay="SHIMMERING SKYLINE ART.",
        overlay_sub="Full-color Gallery Series artwork made to be seen across the table.",
        props=["macro of the shimmering skyline sleeve", "red circular 'gallery series art' badge"],
        lighting="Raking side-light on black so the shimmer in the skyline artwork glints and the design reads as premium.",
        why_it_works=(
            "For a designer sleeve the art IS the product — showing it big on a gallery-black wall is the pattern "
            "interrupt that stops an art-sleeve shopper mid-scroll."
        ),
        ctr="A large shimmering illustration on black is unmissable next to flat solid-color sleeve tiles.",
        cvr="Seeing the artwork full-size lets the buyer fall for the design before they even read a spec.",
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: what's in the pack (art + count)",
        role="educate",
        background="Black #111111, RED top-line 'GALLERY SERIES SLEEVES', WHITE headline.",
        purpose="Make the offer concrete — designer art sleeves, 65 per pack, standard size.",
        visual=(
            "A clean fan of the shimmering skyline sleeves centered on black with thin white arrow callouts: "
            "'65 SLEEVES PER PACK', 'STANDARD 2.5 x 3.5 in', 'FULL-COLOR ART', 'ARCHIVAL, NO PVC'. A single sleeve "
            "pulled forward shows a card sliding in. Red accent underline under the headline."
        ),
        overlay="GALLERY SERIES SLEEVES.",
        overlay_sub="65 designer art sleeves, cut for standard 2.5 x 3.5 inch cards.",
        props=["fan of art sleeves", "4 arrow callouts", "one sleeve with a card sliding in"],
        lighting="Even soft light, slightly brighter center so the fanned artwork stays the focal point on black.",
        why_it_works=(
            "Answers 'what exactly do I get?' — count, size and the art — so the designer sleeve feels like a "
            "confident, spec-backed buy, not a mystery."
        ),
        ctr="Concrete callouts (65, 2.5 x 3.5, full-color) signal a real product and pull spec-checking buyers.",
        cvr="Count and size remove the sizing and quantity doubts that stall sleeve purchases.",
    ),
    AIImagePlanItem(
        name="Image 4 — Desire: stand out at the table (lifestyle)",
        role="desire",
        background="Warm game-table scene; product graphics kept to a slim black/red lower band.",
        purpose="Let the buyer self-cast into the moment their deck turns heads at the table.",
        visual=(
            "Over-the-shoulder game-night moment: a player lays down a hand of shimmering skyline sleeved cards on a "
            "gaming mat, friends leaning in, the art catching the light. Real, warm, aspirational. Slim black lower "
            "band with red top-line 'STAND OUT AT THE TABLE' and the white headline."
        ),
        overlay="STAND OUT AT THE TABLE.",
        overlay_sub="Sleeve your deck in art that turns heads on game night.",
        props=["player's hand of sleeved cards", "gaming mat", "friends at the table", "warm cafe/game-night light"],
        lighting="Warm natural light from camera-left, soft and lived-in — social game night, not clinical studio.",
        why_it_works=(
            "For a designer sleeve the emotional payoff is identity and status at the table — that self-image is "
            "what turns a browsing player into a buyer."
        ),
        ctr="A relatable game-night moment stands out against sterile product-only tiles and invites the click.",
        cvr="Buyers picture their own deck standing out this way, making the purchase feel like the next step.",
    ),
    AIImagePlanItem(
        name="Image 5 — Trust: protection behind the art",
        role="trust",
        background="Black #111111, RED top-line 'BUILT TO PROTECT', WHITE headline.",
        purpose="Reassure that the pretty sleeve is still a real deck protector — snug fit, resists peeling.",
        visual=(
            "One shimmering sleeve with a card inside, rotated to show a snug fit; thin white arrows call out "
            "'DECK PROTECTOR technology', 'RESISTS PEELING' at the seam and 'ARCHIVAL, NO PVC' on the film. A small "
            "red badge 'PROTECT WITH STYLE'. Optional cue: a thumb shuffling the sleeved card, staying crisp."
        ),
        overlay="PROTECT WITH STYLE.",
        overlay_sub="Archival, no-PVC sleeves built to resist peeling shuffle after shuffle.",
        props=["sleeve with card, snug fit", "arrow callouts to seam and film", "red 'protect with style' badge"],
        lighting="Focused key on the seam and film so the construction reads as strong and precise.",
        why_it_works=(
            "The top worry with art sleeves is that looks come at the cost of durability — showing the snug fit and "
            "peel-resistance is concrete proof it protects as well as it looks."
        ),
        ctr="Pairing the artwork with visible protection cues signals 'style AND substance' and earns the click.",
        cvr="Directly answers 'will a designer sleeve actually protect my cards?' and removes a purchase blocker.",
    ),
    AIImagePlanItem(
        name="Image 6 — Desire: match your favorites (compatibility)",
        role="desire",
        background="Black #111111, RED top-line 'FITS YOUR GAMES', WHITE headline; icon row along the bottom.",
        purpose="Show the art sleeves fit the cards the buyer already loves, so it's an easy yes.",
        visual=(
            "Three shimmering sleeved cards fanned — a Pokemon, a Magic (MTG) and a One Piece card — each fully "
            "protected and framed by the skyline art. Dimension callout '2.5\" x 3.5\"' on one. Bottom icon row: "
            "'POKEMON', 'MAGIC (MTG)', 'ONE PIECE', 'TCG'. Red accents on the icons."
        ),
        overlay="65 ART SLEEVES PER PACK.",
        overlay_sub="Fits standard 2.5 x 3.5 inch cards across your favorite games.",
        props=["three sleeved cards (Pokemon/MTG/One Piece)", "dimension callout 2.5\" x 3.5\"", "game icon row"],
        lighting="Clean technical light — flat and legible so the dimension and game icons read instantly.",
        why_it_works=(
            "Removes the last practical doubt — 'will these fit MY cards?' — by showing the exact games and size the "
            "buyer already plays."
        ),
        ctr="Recognizable game names and a clear size signal easy compatibility and pull the click.",
        cvr="Concrete fit across the buyer's own games closes the compatibility objection and justifies the buy.",
    ),
    AIImagePlanItem(
        name="Image 7 — Close: Gallery Series heritage (since 1952)",
        role="close",
        background="Black #111111 with the Ultra PRO logo; subtle red heritage line motif.",
        purpose="Close on brand identity — designer art backed by the protection collectors have trusted for decades.",
        visual=(
            "Centered Ultra PRO logo on black, a soft row of shimmering skyline sleeves behind. RED top-line "
            "'THE GALLERY SERIES', big WHITE headline, footer lockup reading 'Trusted since 1952'. Premium, "
            "gallery-quiet composition."
        ),
        overlay="ULTRA PRO GALLERY SERIES.",
        overlay_sub="Designer art sleeves backed by protection trusted since 1952.",
        props=["Ultra PRO logo", "row of shimmering skyline sleeves", "'since 1952' heritage lockup"],
        lighting="Premium low-key light, soft glow on the logo — authoritative, heritage, gallery feel.",
        why_it_works=(
            "Ends on heritage plus design — the trust cue that reassures a buyer choosing a designer sleeve they "
            "want to both show off and rely on."
        ),
        ctr="The 'Gallery Series · since 1952' lockup signals a real, established art line and reassures at a glance.",
        cvr="Heritage and brand authority provide the final trust nudge that seals the purchase.",
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Gallery banner (hero)",
        role="a+_banner",
        headline="ART YOU CAN PLAY WITH",
        body=(
            "The Gallery Series 'Shimmering Skyline' sleeves turn your deck into a display piece — full-color "
            "artwork on every sleeve, backed by archival, no-PVC protection. 65 sleeves per pack, cut for "
            "standard 2.5 x 3.5 inch cards."
        ),
        visual="Wide cinematic banner: the pack left, a fanned spread of shimmering skyline sleeves right, on a gallery-black wall with a red accent bar. Ultra PRO logo top-left.",
        alt="Ultra PRO Gallery Series Shimmering Skyline sleeve pack beside a fan of shimmering art sleeves on black.",
    ),
    AIModule(
        name="Module 2 — Stand-out banner (lifestyle)",
        role="a+_banner",
        headline="STAND OUT AT THE TABLE",
        body=(
            "From casual game night to a Commander pod, a shimmering skyline deck reads as a curated collection. "
            "Sleeve your Pokemon, Magic (MTG) and One Piece cards in art that turns heads while it keeps every "
            "card protected."
        ),
        visual="Warm game-table scene: a player laying down shimmering sleeved cards on a mat, friends leaning in, art catching the light. Slim black/red lower band with the headline.",
        alt="A player laying shimmering skyline sleeved cards on a gaming mat at game night.",
    ),
    AIModule(
        name="Module 3 — Feature carousel (the Gallery difference)",
        role="a+_carousel",
        headline="THE GALLERY DIFFERENCE",
        body=(
            "Tile 1: <b>SHIMMERING ART</b> — full-color skyline artwork on every sleeve.<br/>"
            "Tile 2: <b>65 PER PACK</b> — enough to sleeve a full standard deck.<br/>"
            "Tile 3: <b>ARCHIVAL, NO PVC</b> — acid-free film that stays true to color.<br/>"
            "Tile 4: <b>DECK PROTECTOR</b> — engineered to resist peeling and lifting.<br/>"
            "Tile 5: <b>STANDARD FIT</b> — cut for 2.5 x 3.5 inch trading cards.<br/>"
            "Tile 6: <b>PLAY OR DISPLAY</b> — as good on the table as on the shelf."
        ),
        visual="6 square tiles on black, red accent corner and a line icon per tile (art frame · stack of 65 · shield · seam · card size · easel). Consistent Ultra PRO styling.",
        alt="Six-tile A+ carousel: shimmering art, 65 per pack, archival no-PVC, deck protector, standard fit, play or display.",
    ),
    AIModule(
        name="Module 4 — Protection banner (callouts)",
        role="a+_banner",
        headline="BEAUTIFUL AND BUILT TO LAST",
        body=(
            "Behind the artwork, these are true deck protector sleeves: DECK PROTECTOR technology engineered to "
            "resist peeling, a snug standard fit, and archival, acid-free, no-PVC film that guards Pokemon, Magic "
            "(MTG), One Piece and TCG cards through shuffle after shuffle."
        ),
        visual="Banner: one shimmering sleeve with a card centered on black, thin white arrow callouts to the seam, the snug fit and the archival film. Red top-line and white headline.",
        alt="A+ banner with callouts pointing to the seam, snug fit and archival film of a shimmering skyline sleeve.",
    ),
    AIModule(
        name="Module 5 — Compatibility banner (fits your games)",
        role="a+_banner",
        headline="FITS YOUR FAVORITE GAMES",
        body=(
            "Sized for standard 2.5 x 3.5 inch cards, the Shimmering Skyline sleeves fit Pokemon, Magic the "
            "Gathering, One Piece and most trading card games — 65 art sleeves per pack, ready for deck or "
            "display straight out of the box."
        ),
        visual="Banner with three shimmering sleeved cards (Pokemon, MTG, One Piece) and a game icon row on black; a '2.5 x 3.5 in' dimension callout. Red stat icons.",
        alt="A+ banner showing shimmering skyline sleeves fitting Pokemon, Magic and One Piece standard-size cards.",
    ),
    AIModule(
        name="Module 6 — Brand close (heritage + review)",
        role="a+_banner",
        headline="THE GALLERY SERIES",
        body=(
            "Collectors have trusted Ultra PRO for collectible protection since 1952. The Gallery Series pairs "
            "that heritage with designer artwork, so you protect what matters most in style. <br/><br/>"
            "“Crystal clear and durable, my cards are well-protected.” &#9733;&#9733;&#9733;&#9733;&#9733;"
        ),
        visual="Closing banner: Ultra PRO logo centered on black, a soft row of shimmering skyline sleeves behind, a 'since 1952' heritage lockup and a five-star review quote below.",
        alt="Ultra PRO Gallery Series brand-close banner: trusted since 1952, with a five-star review quote.",
    ),
]


# ENGLISH backend search terms — stem-deduped, no title/brand duplicates, ≤ 249 bytes.
BACKEND = (
    "commander deck sleeves matte glossy colored art sleeve tcg ccg yugioh one piece "
    "bulk 65 count game night display shuffle protector holder gaming collection "
    "outer inner illustrated designer skyline"
)


def main() -> None:
    print("Loading Ultra PRO customer + parsing Shimmering Skyline listing…")
    cust = load_customer("ultra_pro")
    brief = parse_excel(EXCEL)
    OUT = HERE / f"{PLAN_NO}_{ASIN}_Image Plan.pdf"
    real_title_len = len(TITLE.replace("&amp;", "&"))
    print(f"  Product: {brief.product_name}")
    print(f"  Plan #{PLAN_NO}  ASIN(task): {ASIN}  ASIN(xlsx): {brief.asin}")
    print(f"  Marketplace: {cust.marketplace}  Overlay lang: {cust.overlay_language}")
    print(f"  TITLE real chars (de-escaped): {real_title_len}")

    builder = BriefBuilder(cust, brief, OUT, ai=None)
    builder._ai_title = TITLE
    builder._ai_bullets = BULLETS
    builder._ai_images = IMAGES
    builder._ai_modules = MODULES
    builder._ai_qa = []      # client instruction (listings 35-50): no Q&A module
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
