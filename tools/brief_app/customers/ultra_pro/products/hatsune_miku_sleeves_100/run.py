"""Ultra PRO 10th Anniversary HATSUNE MIKU Deck Protector Sleeves (100ct) — Image Plan #44.

A LICENSED collab collectible (ASIN B0DP23HSN4). The official Hatsune Miku
10th-anniversary sleeve ART is the hero — NOT generic sleeves. The plan leads on
the licensed design + collector appeal; protection (archival-safe polypropylene,
ChromaFusion film, standard fit for MTG / Pokemon) plays the support role.

Self-contained: listing.xlsx in → 44_B0DP23HSN4_Image Plan.pdf out, both in this folder.

LANGUAGE: amazon.com / English — TITLE, BULLETS, overlays, module copy, BACKEND all English.

ULTRA PRO STYLE (matched in every image's art direction): black background, bold RED
top-line + big WHITE headline; feature callouts with thin arrows; the licensed Miku art
shown on a sleeved deck; real TCG cards (MTG / Pokemon); the product pack; a dimension
callout (2.5" x 3.5"); brand close 'Trusted since 1952 · Made in USA'. (Image 1 / main
image stays on clean white per Amazon policy.)

GUARDRAILS (auto-checked on build):
  overlay ≤30 chars AND ≤5 words, smooth (no middots) · overlay_sub ≤90 ·
  module headline ≤38 · bullet head <b>…</b> ≤45 · TITLE ≤200.
COMPLIANCE: no "#1", no "best", no "leading", no "guaranteed", no "prevent",
  no "$", no URL/.com. "ChromaFusion helps resist peeling" (never 'prevent'),
  clarity/quality as concrete specs, brand proof as "Trusted since 1952".

Client instruction (listings 35-50): NO Q&A module, NO Comparison module.
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
PLAN_NO = "44"
ASIN = "B0DP23HSN4"


# ===== Customer-facing copy (ENGLISH — amazon.com) =====

# HTML-escaped "&amp;" counts as 1 real char. Keep de-escaped length ≤ 200.
TITLE = (
    "Ultra PRO 10th Anniversary Hatsune Miku Deck Protector Sleeves (100 Count) — "
    "Officially Licensed Anime Card Sleeves, Standard Size 2.5 x 3.5 in, Archival-Safe "
    "for MTG &amp; Pokemon TCG"
)

BULLETS = [
    "<b>OFFICIALLY LICENSED HATSUNE MIKU ART</b> — Full-color, officially licensed Hatsune Miku "
    "artwork wraps every sleeve, turning a protected deck into a display piece. These anime sleeves "
    "put the character front and center, not a plain solid back.",

    "<b>10TH ANNIVERSARY COLLECTOR EDITION</b> — Part of the 10th anniversary Hatsune Miku "
    "collection, these deck protector sleeves are made for collectors and fans who want licensed "
    "art on the cards they play and showcase.",

    "<b>ARCHIVAL-SAFE DECK PROTECTION</b> — Archival-safe polypropylene construction shields cards "
    "from dust, fingerprints and everyday wear, while ChromaFusion Technology helps resist peeling "
    "so the printed art stays crisp shuffle after shuffle.",

    "<b>STANDARD FIT FOR TCG PLAY</b> — Standard size sleeves fit trading cards measuring 2.5 x 3.5 "
    "inches, so they sleeve Magic (MTG), Pokemon and other standard TCG cards for casual games, "
    "commander decks and competitive play alike.",

    "<b>TRUSTED BY COLLECTORS SINCE 1952</b> — 100 sleeves per pack from Ultra PRO, protecting "
    "collectibles since 1952. Licensed anime sleeves that keep your deck safe on the table and "
    "sharp on the shelf — proudly Made in USA.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (pack + sleeved Miku deck)",
        role="hero",
        background="Pure white #FFFFFF seamless — Amazon main-image policy (no overlay text, no graphics).",
        purpose="Win the click in the amazon.com sleeve grid — instantly read as the OFFICIAL Hatsune Miku 10th-anniversary sleeve.",
        visual=(
            "The 100-count pack standing three-quarter left, label and Hatsune Miku art fully legible. "
            "To its right, a small fanned stack of sleeved cards showing the full-color Miku artwork on the "
            "sleeve backs, plus one sleeved card face-up so a standard TCG card reads clearly through the film. "
            "Tight crop, product ~85% of frame, subtle contact shadow, no overlay text."
        ),
        overlay="(no overlay — Amazon main image)",
        overlay_sub="",
        props=["100-count pack with Miku artwork", "fanned stack of sleeved cards (art backs)", "one sleeved standard TCG card"],
        lighting="Bright, even studio light; soft rim on the sleeve edges so the printed art and clear film pop against white.",
        why_it_works=(
            "The pack plus the sleeved deck shows the licensed art AND the product type (deck protector sleeves) "
            "in one glance — the two things a Miku collector scans for in the grid."
        ),
        ctr="The recognizable official Miku art on the sleeve backs out-signals plain solid-color sleeve thumbnails and pulls the click.",
        cvr="Shows exactly what the buyer receives (pack + art sleeves) and proves the artwork up front, cutting hesitation.",
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: the licensed art hero (macro)",
        role="hook",
        background="Black #111111. Bold RED #C8102E top-line 'OFFICIALLY LICENSED', big WHITE headline below.",
        purpose="Lead with the single strongest reason to buy — the official Hatsune Miku 10th-anniversary artwork.",
        visual=(
            "Hero macro of one sleeve back filling most of the frame, the full-color Hatsune Miku 10th-anniversary "
            "art razor-sharp under raking light. A small red circular badge top-right reads 'OFFICIALLY LICENSED'. "
            "Thin white arrow tags 'full-color themed artwork'. White headline lower-left."
        ),
        overlay="OFFICIAL HATSUNE MIKU.",
        overlay_sub="Full-color, officially licensed Hatsune Miku artwork on every sleeve.",
        props=["macro of the Miku sleeve-back art", "red 'officially licensed' badge", "thin arrow to the artwork"],
        lighting="Hard raking side-light on black so the printed art reads vivid and the sleeve edge catches a crisp rim.",
        why_it_works=(
            "Answers the fan's first question — 'is this the real, licensed Miku art?' — with a bold proof macro, "
            "making the licensed design (not generic protection) the hero."
        ),
        ctr="A giant official Miku illustration on black is a pattern interrupt in a grid of solid-color sleeve packs.",
        cvr="Macro proof of licensed, full-color art defuses the fan's biggest worry (bootleg / dull print) before the buy.",
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: the 10th anniversary collection",
        role="educate",
        background="Black #111111, RED top-line '10TH ANNIVERSARY', WHITE headline.",
        purpose="Frame the sleeve as a collectible anniversary piece, not a commodity accessory.",
        visual=(
            "The Miku sleeve art shown large beside the 100-count pack on black, thin white arrows to labeled "
            "callouts: OFFICIALLY LICENSED · FULL-COLOR ARTWORK · 10TH ANNIVERSARY · 100 SLEEVES · STANDARD SIZE. "
            "Small line icons per callout, red accent underlines under the two headline words."
        ),
        overlay="10TH ANNIVERSARY SLEEVES.",
        overlay_sub="Part of the 10th anniversary Hatsune Miku collection — 100 sleeves per pack.",
        props=["sleeve art hero", "100-count pack", "5 arrow callouts with line icons", "red accent underlines"],
        lighting="Even soft light, slightly brighter center so the art and pack stay the focal point on black.",
        why_it_works=(
            "Turns the SKU into a collectible moment — anniversary framing plus the licensed-art callouts is exactly "
            "what a Miku collector filters for and what a plain sleeve pack cannot claim."
        ),
        ctr="A well-organized anniversary feature stack signals 'collectible', earning the click from fans and collectors.",
        cvr="Each callout (licensed, full-color, anniversary, 100ct, standard) removes a specific doubt, compounding trust.",
    ),
    AIImagePlanItem(
        name="Image 4 — Desire: sleeved deck on the table (lifestyle)",
        role="desire",
        background="Warm game-table scene; product graphics kept to a slim black/red lower band.",
        purpose="Let the buyer picture their own deck sleeved in the Miku art during play and display.",
        visual=(
            "Over-the-shoulder lifestyle: a player's hands shuffle a deck fully sleeved in the Hatsune Miku art at a "
            "tidy game table, a few sleeved cards fanned face-up nearby (MTG / Pokemon). Warm, aspirational, real. "
            "Slim black lower band with red top-line 'DECK ART THAT STANDS OUT' and the white headline."
        ),
        overlay="DECK ART THAT STANDS OUT.",
        overlay_sub="Sleeve your whole deck in Miku art for game night and display.",
        props=["player's hands shuffling", "deck sleeved in Miku art", "fanned sleeved MTG / Pokemon cards", "tidy game table"],
        lighting="Warm natural table light from camera-left, soft and lived-in — hobbyist, not clinical.",
        why_it_works=(
            "Moves from the art to the emotional payoff — a deck that looks unmistakably yours at the table — which is "
            "what turns a browsing fan into a buyer."
        ),
        ctr="A relatable game-night moment with the Miku deck stands out against sterile product-only tiles.",
        cvr="Buyers picture their own deck sleeved this way, making the purchase feel like the obvious next step.",
    ),
    AIImagePlanItem(
        name="Image 5 — Trust: archival-safe protection & anti-peel film",
        role="trust",
        background="Black #111111, RED top-line 'ARCHIVAL-SAFE MATERIAL', WHITE headline.",
        purpose="Show that the licensed art is backed by real protection — archival PP and a peel-resistant print.",
        visual=(
            "A sleeved card held up on black with thin white arrows calling out 'archival-safe polypropylene' at the "
            "sleeve body and 'ChromaFusion film — resists peeling' at the printed edge. A small red badge "
            "'PROTECTS YOUR CARDS'. Optional cue: a fingertip gliding over the art, staying crisp."
        ),
        overlay="ARCHIVAL-SAFE PROTECTION.",
        overlay_sub="Archival-safe polypropylene with ChromaFusion film that helps resist peeling.",
        props=["sleeved card on black", "arrow callouts to PP body and ChromaFusion edge", "red 'protects your cards' badge"],
        lighting="Focused key on the sleeve edge so the film and the crisp printed art read as durable and premium.",
        why_it_works=(
            "Backs the collectible art with concrete protection specs — archival PP and peel-resistant printing — the "
            "reassurance a collector needs before sleeving a deck they care about."
        ),
        ctr="The 'archival-safe' callout plus the crisp art signals quality, not a flimsy novelty sleeve.",
        cvr="Directly answers 'will the art peel or the sleeve harm my cards?' with material proof, removing a blocker.",
    ),
    AIImagePlanItem(
        name="Image 6 — Desire: standard fit & capacity (dimensions + icon stats)",
        role="desire",
        background="Black #111111, RED top-line 'STANDARD SIZE FIT', WHITE headline; icon-stat bar along the bottom.",
        purpose="Prove exact fit and count so the buyer knows the sleeves suit their cards and deck.",
        visual=(
            "A standard card ghosted inside a sleeve with a clean dimension callout '2.5\" x 3.5\"' and arrows to the "
            "sleeve mouth. Bottom icon-stat bar with two tiles: 'FITS STANDARD TCG CARDS' and '100 SLEEVES PER PACK'. "
            "Red accents on the stat icons."
        ),
        overlay="STANDARD FIT FOR PLAY.",
        overlay_sub="Fits standard cards up to 2.5 x 3.5 inches — MTG, Pokemon and more.",
        props=["dimension callout 2.5\" x 3.5\"", "card ghosted inside a sleeve", "two icon-stat tiles"],
        lighting="Clean technical light — flat and legible so the dimensions and stat icons read instantly.",
        why_it_works=(
            "Removes the last practical doubts — 'will these fit my cards and how many do I get?' — with exact numbers "
            "a spec-driven player trusts."
        ),
        ctr="Concrete specs (2.5x3.5, 100 count, standard) signal precision and pull spec-checking buyers.",
        cvr="Exact fit and count data closes the sizing objection and justifies the buy.",
    ),
    AIImagePlanItem(
        name="Image 7 — Close: brand trust (since 1952 · Made in USA)",
        role="close",
        background="Black #111111 with the Ultra PRO logo; subtle red heritage line motif.",
        purpose="Close on Ultra PRO heritage — the protection collectors have trusted for decades, now with Miku art.",
        visual=(
            "Centered Ultra PRO logo on black, the sleeved Miku deck softly behind. RED top-line 'TRUSTED BY "
            "COLLECTORS WORLDWIDE', big WHITE headline, and a footer lockup: a small USA-flag mark with "
            "'Made in USA' beside 'Since 1952'."
        ),
        overlay="TRUSTED SINCE 1952.",
        overlay_sub="Protecting collections with USA-made quality since 1952.",
        props=["Ultra PRO logo", "sleeved Miku deck softly behind", "USA-flag 'Made in USA' mark"],
        lighting="Premium low-key light, soft glow on the logo — authoritative, heritage, category-anchor feel.",
        why_it_works=(
            "Ends on provenance — the trust cue that reassures a collector the licensed sleeve is backed by a brand "
            "that has protected collections for decades."
        ),
        ctr="The heritage 'since 1952 · Made in USA' lockup signals category authority and reassures at a glance.",
        cvr="Provenance and longevity provide the final trust nudge that seals the purchase.",
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Brand banner (licensed hero)",
        role="a+_banner",
        headline="OFFICIAL HATSUNE MIKU SLEEVES",
        body=(
            "Ultra PRO's 10th Anniversary Hatsune Miku Deck Protector Sleeves wrap every card in "
            "full-color, officially licensed artwork. 100 standard-size sleeves per pack, archival-safe "
            "and made to protect the deck you play and display."
        ),
        visual="Wide cinematic banner: the 100-count pack left, a fanned spread of Miku-art sleeves and a sleeved deck right, on black with a red accent bar. Ultra PRO logo top-left.",
        alt="Ultra PRO 10th Anniversary Hatsune Miku deck protector sleeves pack beside a sleeved deck on a black background.",
    ),
    AIModule(
        name="Module 2 — Lifestyle banner",
        role="a+_banner",
        headline="SLEEVE YOUR DECK IN STYLE",
        body=(
            "From commander night to a Pokemon showcase, keep every card protected in sleeves that show "
            "off official Hatsune Miku art. Archival-safe polypropylene guards your cards while the "
            "10th anniversary design makes your deck unmistakably yours."
        ),
        visual="Warm lifestyle scene: a player shuffling a Miku-sleeved deck at a game table, sleeved cards fanned nearby, soft daylight. Slim black/red lower band with the headline.",
        alt="A player shuffling a deck sleeved in Hatsune Miku art at a game table.",
    ),
    AIModule(
        name="Module 3 — Feature carousel (the anniversary set)",
        role="a+_carousel",
        headline="THE 10TH ANNIVERSARY DETAILS",
        body=(
            "Tile 1: <b>OFFICIALLY LICENSED</b> — genuine Hatsune Miku 10th anniversary artwork.<br/>"
            "Tile 2: <b>FULL-COLOR ART</b> — vivid printed design on every sleeve back.<br/>"
            "Tile 3: <b>ARCHIVAL-SAFE PP</b> — archival-safe polypropylene construction.<br/>"
            "Tile 4: <b>CHROMAFUSION FILM</b> — helps resist peeling, keeps art crisp.<br/>"
            "Tile 5: <b>STANDARD SIZE</b> — fits 2.5 x 3.5 in TCG cards.<br/>"
            "Tile 6: <b>100 PER PACK</b> — sleeves a full deck with spares."
        ),
        visual="6 square tiles on black, red accent corner and a line icon per tile (badge · art · shield · film layers · card size · stack). Consistent Ultra PRO styling.",
        alt="Six-tile A+ carousel: officially licensed, full-color art, archival-safe PP, ChromaFusion film, standard size, 100 per pack.",
    ),
    AIModule(
        name="Module 4 — Art showcase banner",
        role="a+_banner",
        headline="DECK ART THAT STANDS OUT",
        body=(
            "Every sleeve back carries the full-color Hatsune Miku 10th anniversary illustration, so a "
            "protected deck doubles as a display piece on the table and the shelf. Licensed anime sleeves "
            "made for fans who want their cards to look as good as they play."
        ),
        visual="Banner: a macro of the Miku sleeve art centered on black with thin white arrows to 'full-color artwork' and 'officially licensed'. Red top-line and white headline.",
        alt="A+ banner showcasing the full-color Hatsune Miku artwork printed on the sleeve backs.",
    ),
    AIModule(
        name="Module 5 — Protection banner (feature callouts)",
        role="a+_banner",
        headline="BUILT TO PROTECT YOUR CARDS",
        body=(
            "Archival-safe polypropylene shields Magic (MTG), Pokemon and other standard TCG cards from "
            "dust, fingerprints and everyday wear, while ChromaFusion Technology helps resist peeling so "
            "the printed art stays sharp through shuffle after shuffle of play."
        ),
        visual="Banner: one sleeved card centered on black with thin white arrow callouts to the archival-safe PP body and the ChromaFusion print edge. Red top-line and white headline.",
        alt="A+ banner with feature callouts pointing to the archival-safe polypropylene and ChromaFusion peel-resistant film of the sleeve.",
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
        visual="Closing banner: Ultra PRO logo centered on black, the sleeved Miku deck softly behind, footer lockup with a USA-flag 'Made in USA' mark and 'Since 1952', a five-star review quote below.",
        alt="Ultra PRO brand-close banner: trusted by collectors worldwide, Made in USA since 1952, with a five-star review quote.",
    ),
]


# ENGLISH backend search terms — stem-deduped, no title/brand duplicates, ≤ 249 bytes.
BACKEND = (
    "vocaloid anime deck sleeves matte glossy commander yugioh one piece "
    "chromafusion polypropylene tcg ccg deck box gaming accessories bulk pack "
    "art sleeves collectible fan gift shuffle protector color themed"
)


def main() -> None:
    print("Loading Ultra PRO customer + parsing Hatsune Miku listing…")
    cust = load_customer("ultra_pro")
    brief = parse_excel(EXCEL)
    OUT = HERE / f"{PLAN_NO}_{ASIN}_Image Plan.pdf"
    real_title_len = len(TITLE.replace("&amp;", "&"))
    print(f"  Product: {brief.product_name}")
    print(f"  Marketplace: {cust.marketplace}  Overlay lang: {cust.overlay_language}")
    print(f"  ASIN: {ASIN}  Plan #{PLAN_NO}")
    print(f"  TITLE real chars (de-escaped): {real_title_len}")

    builder = BriefBuilder(cust, brief, OUT, ai=None)
    builder._ai_title = TITLE
    builder._ai_bullets = BULLETS
    builder._ai_images = IMAGES
    builder._ai_modules = MODULES
    builder._ai_backend = BACKEND
    builder._ai_qa = []  # client instruction (35-50): no Q&A module
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
