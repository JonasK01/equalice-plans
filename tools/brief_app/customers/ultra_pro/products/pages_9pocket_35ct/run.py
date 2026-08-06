"""Ultra PRO 9-Pocket Pages — 35-Page VALUE PACK (ASIN B0D7WTZPKM) — Image Plan.

Plan #47. Hand-written senior copy in the Ultra PRO catalog format, built inside
the EQUALICE brief_app. Reads the product's own SEO axis from listing.xlsx and
constructs the ParsedBrief via parse_excel().

DIFFERENTIATION (per Jonas — every Ultra PRO listing is 100% its own):
  This SKU is the VALUE PACK — 35 nine-pocket pages that hold up to 315 standard
  trading cards, enough to build out a whole binder in one box. Lead on the value
  angle (35 pages = 315 cards) + clear, card-safe protection. Distinct from the
  100-page sample and from the Platinum SKU (#41): here the hook is quantity +
  binder build-out, not a premium/platinum grade.

ULTRA PRO STYLE (matched in the art direction of every image):
  BLACK background, bold RED #C8102E top-line + big WHITE headline; feature
  callouts with thin arrows; icon-stat bars (fits 3-ring binders · 315 cards);
  a red circular clarity badge; REAL popular cards (Pokemon, MTG, One Piece,
  sports) in the pages/binder; real collector lifestyle; the product pack shown;
  a dimension callout (2.5" x 3.5"); brand close 'Trusted since 1952 · Made in USA'.
  (Image 1 / main image stays on a clean white background per Amazon policy.)

GUARDRAILS (auto-checked on build):
  overlay ≤30 chars AND ≤5 words, smooth (no middots, no fragments) ·
  overlay_sub ≤90 · module headline ≤38 · bullet head <b>…</b> ≤45 · TITLE ≤200.
COMPLIANCE: no "#1", no "best", no "leading", no "guaranteed", no "prevent",
  no "$", no URL/.com. Heritage proof as "Trusted since 1952", clarity as
  "Crystal-Clear / High Clarity", strength as "Superior seal strength".

Client instruction (per Jonas, listings 35-50): do NOT build a Q&A module and do
NOT build a Comparison module. This brief ships 7 images + 6 A+ banners/carousels.
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
PLAN_NO = "47"
ASIN = "B0D7WTZPKM"


# ===== Customer-facing copy (ENGLISH — amazon.com) =====

# HTML-escaped "&" counts as 1 real char. Keep de-escaped length ≤ 200.
TITLE = (
    "Ultra PRO 9-Pocket Pages, 35-Page Value Pack — Clear Trading Card Pages for "
    "Pokemon, MTG, One Piece &amp; Sports · Holds Up to 315 Cards · No PVC / Acid-Free · "
    "Fits Standard 3-Ring Binders"
)

BULLETS = [
    "<b>35-PAGE VALUE PACK, 315 CARDS</b> — Build out a whole binder from one box: 35 clear "
    "9 pocket pages hold up to 315 standard trading cards, so you can sort your Pokemon, Magic "
    "(MTG), One Piece and sports cards in a single sitting instead of buying pack after pack.",

    "<b>HOLDS UP TO 315 CARDS</b> — Each 9-pocket page shows nine cards per side, and 35 trading "
    "card pages add up to 315 cards of organized storage — plenty of room to grow your collection "
    "and keep doubles, sets and singles all in one place.",

    "<b>FITS STANDARD 3-RING BINDERS</b> — Hole-punched to drop straight into any standard 3-ring "
    "binder or album, so your trading card pages and 9 pocket card sleeves stay neatly filed, easy "
    "to flip through and simple to rearrange as the collection grows.",

    "<b>CRYSTAL-CLEAR, CARD-SAFE PAGES</b> — Clear polypropylene pages let you read every card front "
    "and back without pulling it out, while acid-free, no-PVC material helps guard cards against "
    "yellowing, moisture and everyday handling.",

    "<b>TRUSTED BY COLLECTORS SINCE 1952</b> — Ultra PRO has protected collectibles since 1952. "
    "These clear trading card pages also store photos and memorabilia, so a single value pack keeps "
    "everything you care about safe — proudly Made in USA.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (value pack + loaded 9-pocket page)",
        role="hero",
        background="Pure white #FFFFFF seamless — Amazon main-image policy (no overlay text, no graphics).",
        purpose="Win the click in the amazon.com card-storage grid — instantly read as a high-count VALUE PACK of clear 9-pocket pages.",
        visual=(
            "The 35-page value pack (sealed pack / banded stack of pages) standing three-quarter left, count "
            "clearly legible. To its right, ONE 9-pocket page held upright and fully loaded with real popular "
            "cards (Pokemon, MTG, One Piece, a sports rookie), reading glass-clear so every face is sharp. A "
            "few more pages fanned lightly behind to signal quantity. Tight crop, product ~85% of frame, subtle "
            "contact shadow, no overlay text."
        ),
        overlay="(no overlay — Amazon main image)",
        overlay_sub="",
        props=["35-page value pack / banded stack of pages", "one 9-pocket page loaded with real cards", "Pokemon / MTG / One Piece / sports cards"],
        lighting="Bright, even studio light; soft rim on the page edge so the clear plastic and card art pop against white.",
        why_it_works=(
            "The visible page count plus a fully loaded, glass-clear page communicates product type (9-pocket "
            "pages), quantity (a lot of them) and clarity in one glance — the three things a collector scans for."
        ),
        ctr="A high-count value pack beside real recognizable cards out-signals single-page thumbnails and pulls the click.",
        cvr="Shows exactly what the buyer receives (35 pages + clear pockets) and proves clarity up front, cutting hesitation.",
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: the value-pack math (35 pages / 315 cards)",
        role="hook",
        background="Black #111111. Bold RED #C8102E top-line 'VALUE PACK', big WHITE headline below.",
        purpose="Land the single strongest reason to buy — one box fills a binder, up to 315 cards.",
        visual=(
            "A tall fanned stack of the 35 clear pages on black, several loaded with holo Pokemon / MTG cards. "
            "Two big red icon-stat tiles lower-third: '35 PAGES' and 'UP TO 315 CARDS'. A thin white arrow links "
            "the stack to an open binder filling up. White headline lower-left."
        ),
        overlay="35 PAGES, 315 CARDS.",
        overlay_sub="One value pack fills a whole binder with up to 315 cards.",
        props=["fanned stack of 35 pages", "two red icon-stat tiles (35 pages / 315 cards)", "open binder filling up"],
        lighting="Hard raking side-light on black so the stack reads deep and the clear film reads as glass.",
        why_it_works=(
            "Leads with the differentiator a shopper is comparing on — quantity and cost-per-card — and turns "
            "an abstract number into a visible 'this fills my binder' payoff."
        ),
        ctr="Big '35 PAGES / 315 CARDS' numbers on black are a pattern interrupt against single-page product shots.",
        cvr="Quantifies the value so the buyer sees one purchase covering the whole collection, justifying the buy.",
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: clear, card-safe construction",
        role="educate",
        background="Black #111111, RED top-line 'CLEAR 9-POCKET PAGES', WHITE headline.",
        purpose="Prove the pages are clear and card-safe as scannable arrow callouts.",
        visual=(
            "One 9-pocket page centered on black, thin white arrows radiating to labeled callouts: "
            "CLEAR POLYPROPYLENE · NO PVC / ACID-FREE · 9 POCKETS PER PAGE · READ FRONT & BACK · SMOOTH POCKET "
            "OPENINGS · FITS 3-RING BINDERS. Each callout with a small line icon. Red accent underlines under "
            "the headline words."
        ),
        overlay="CLEAR 9-POCKET PAGES.",
        overlay_sub="Clear, acid-free, no-PVC pages you can read front and back.",
        props=["9-pocket page (hero object)", "6 arrow callouts with line icons", "red accent underlines"],
        lighting="Even soft light on the page, slightly brighter center so the product stays the focal point on black.",
        why_it_works=(
            "Turns the spec sheet (clear, no-PVC, acid-free, 9 pockets) into a visual proof stack — exactly what "
            "a collector filters for when comparing card pages."
        ),
        ctr="A dense, organized feature stack signals 'safe storage' and earns the click from careful collectors.",
        cvr="Each callout removes a specific doubt (clarity, PVC, acid, fit), compounding trust toward purchase.",
    ),
    AIImagePlanItem(
        name="Image 4 — Desire: build out your binder (lifestyle)",
        role="desire",
        background="Warm collector desk scene; product graphics kept to a slim black/red lower band.",
        purpose="Let the buyer picture filling a fresh binder in one calm, satisfying session.",
        visual=(
            "Over-the-shoulder lifestyle: a collector's hands slide loaded 9-pocket pages into a 3-ring binder "
            "on a tidy desk, the open value pack and a fan of filled pages nearby showing Pokemon and sports "
            "cards. Warm, aspirational, real. Slim black lower band with red top-line 'BUILD OUT YOUR BINDER' "
            "and the white headline."
        ),
        overlay="BUILD OUT YOUR BINDER.",
        overlay_sub="Fill a fresh binder in one sitting with the whole value pack.",
        props=["collector's hands", "3-ring binder", "open value pack", "loaded 9-pocket pages", "Pokemon & sports cards"],
        lighting="Warm natural desk light from camera-left, soft and lived-in — hobbyist, not clinical.",
        why_it_works=(
            "Moves from features to the payoff unique to a value pack — finishing a whole binder at once — which "
            "is what turns a browsing collector into a buyer."
        ),
        ctr="A relatable 'binder night' scene stands out against sterile product-only tiles and invites the click.",
        cvr="Buyers picture the satisfying build-out, making the larger pack feel like the smarter single purchase.",
    ),
    AIImagePlanItem(
        name="Image 5 — Trust: cards stay protected in the pocket",
        role="trust",
        background="Black #111111, RED top-line 'CARD-SAFE POCKETS', WHITE headline.",
        purpose="Defuse the fear that cards slip or get damaged — the pockets hold and shield them.",
        visual=(
            "A page rotated to show a card held snugly in its pocket even tilted; thin white arrows call out "
            "'snug pocket fit' at the opening and 'acid-free, no PVC' along the film. A small red badge "
            "'PROTECTS YOUR CARDS'. Optional cue: a hand tilting the page, the card staying put."
        ),
        overlay="CARDS STAY PROTECTED.",
        overlay_sub="Snug pockets and acid-free, no-PVC film keep every card safe.",
        props=["page rotated / tilted", "arrow callouts to pocket fit and material", "red 'protects your cards' badge"],
        lighting="Focused key on the pocket mouth so the snug fit and clear film read as secure and precise.",
        why_it_works=(
            "Targets the top negative-review fear in card storage (cards slipping or getting damaged) with "
            "concrete visual proof rather than a promise."
        ),
        ctr="The tilted 'still held' visual is a curiosity hook that stops the scroll.",
        cvr="Directly answers 'will my cards fall out or get harmed?' with visible construction proof.",
    ),
    AIImagePlanItem(
        name="Image 6 — Desire: precision fit & capacity (dimensions + icon stats)",
        role="desire",
        background="Black #111111, RED top-line 'PRECISION STORAGE', WHITE headline; icon-stat bar along the bottom.",
        purpose="Prove exact fit and capacity so the buyer knows it works for their cards and binder.",
        visual=(
            "A single card ghosted inside a pocket with a clean dimension callout '2.5\" x 3.5\"' and arrows to "
            "the pocket edges. Above, the punched holes aligned to binder rings. Bottom icon-stat bar with two "
            "tiles: 'FITS STANDARD 3-RING BINDERS' and 'UP TO 315 CARDS'. Red accents on the stat icons."
        ),
        overlay="SIZED FOR YOUR CARDS.",
        overlay_sub="Fits standard 2.5 x 3.5 inch cards in any 3-ring binder.",
        props=["dimension callout 2.5\" x 3.5\"", "punched holes aligned to rings", "two icon-stat tiles"],
        lighting="Clean technical light — flat and legible so the dimensions and stat icons read instantly.",
        why_it_works=(
            "Removes the last practical doubts — 'will it fit my cards and my binder, and how much does it hold?' "
            "— with exact numbers a spec-driven collector trusts."
        ),
        ctr="Concrete numbers (2.5x3.5, 315 cards, 3-ring) signal precision and pull spec-checking buyers.",
        cvr="Exact fit and capacity data closes the sizing objection and justifies the buy.",
    ),
    AIImagePlanItem(
        name="Image 7 — Close: brand trust (since 1952 · Made in USA)",
        role="close",
        background="Black #111111 with the Ultra PRO logo; subtle red heritage line motif.",
        purpose="Close on brand identity and heritage — the protection collectors have trusted for decades.",
        visual=(
            "Centered Ultra PRO logo on black, a neat row of filled binders / loaded pages softly behind. RED "
            "top-line 'TRUSTED BY COLLECTORS WORLDWIDE', big WHITE headline, and a footer lockup: a small "
            "USA-flag mark with 'Made in USA' beside 'Since 1952'."
        ),
        overlay="TRUSTED SINCE 1952.",
        overlay_sub="Protecting collections with USA-made quality since 1952.",
        props=["Ultra PRO logo", "row of filled binders / loaded pages", "USA-flag 'Made in USA' mark"],
        lighting="Premium low-key light, soft glow on the logo — authoritative, heritage, category-anchor feel.",
        why_it_works=(
            "Ends on heritage and provenance — the trust cue that converts a hesitating collector who wants a "
            "brand that will still be here to protect the collection they are building."
        ),
        ctr="The heritage 'since 1952 · Made in USA' lockup signals category authority and reassures at a glance.",
        cvr="Provenance and longevity provide the final trust nudge that seals the purchase.",
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Brand banner (hero)",
        role="a+_banner",
        headline="VALUE-PACK CARD PROTECTION",
        body=(
            "The 35-page value pack of clear 9-pocket pages holds up to 315 standard trading cards — "
            "enough to build out a whole binder from one box. Clear, acid-free and no-PVC, ready for "
            "your Pokemon, MTG, One Piece and sports collection."
        ),
        visual="Wide cinematic banner: the value pack left, a tall fanned spread of loaded 9-pocket pages (Pokemon, MTG, One Piece, sports) right, on black with a red accent bar. Ultra PRO logo top-left.",
        alt="Ultra PRO 35-page value pack of 9-pocket pages beside loaded pages of trading cards on a black background.",
    ),
    AIModule(
        name="Module 2 — Feature carousel (what's in the value pack)",
        role="a+_carousel",
        headline="WHY THIS VALUE PACK",
        body=(
            "Tile 1: <b>35 PAGES</b> — a whole binder's worth in one box.<br/>"
            "Tile 2: <b>UP TO 315 CARDS</b> — nine pockets on every page.<br/>"
            "Tile 3: <b>CLEAR PAGES</b> — read every card front and back.<br/>"
            "Tile 4: <b>NO PVC / ACID-FREE</b> — card-safe polypropylene.<br/>"
            "Tile 5: <b>FITS 3-RING BINDERS</b> — drops into any standard album.<br/>"
            "Tile 6: <b>FOR EVERY TCG</b> — Pokemon, MTG, One Piece and sports."
        ),
        visual="6 square tiles on black, red accent corner and a line icon per tile (stack · grid · clear page · no-PVC · binder rings · cards). Consistent Ultra PRO styling.",
        alt="Six-tile A+ carousel: 35 pages, up to 315 cards, clear pages, no PVC/acid-free, fits 3-ring binders, for every TCG.",
    ),
    AIModule(
        name="Module 3 — Value banner (the pack math)",
        role="a+_banner",
        headline="35 PAGES, UP TO 315 CARDS",
        body=(
            "Each 9-pocket page stores nine cards per side, and 35 pages add up to 315 cards of organized "
            "storage. Sort doubles, sets and singles in one sitting, and keep room to grow — all from a "
            "single value pack instead of buying pages a few at a time."
        ),
        visual="Banner: a fanned stack of the 35 pages on black with two big red icon-stat tiles '35 PAGES' and 'UP TO 315 CARDS', an open binder filling up alongside. Red top-line and white headline.",
        alt="A+ banner with icon stats: 35 nine-pocket pages holding up to 315 trading cards, filling a binder.",
    ),
    AIModule(
        name="Module 4 — Build-out banner (lifestyle)",
        role="a+_banner",
        headline="BUILD OUT YOUR BINDER",
        body=(
            "From a first Pokemon pull to a graded sports rookie, drop each loaded page straight into a "
            "3-ring binder and watch the collection come together. Enough clear pages in one pack to fill "
            "a fresh binder and keep everything sorted and easy to browse."
        ),
        visual="Warm lifestyle scene: a collector sliding loaded pages into a binder at a tidy desk, the open value pack and cards visible, soft daylight. Slim black/red lower band with the headline.",
        alt="A collector building out a 3-ring binder with loaded 9-pocket pages from the value pack at a desk.",
    ),
    AIModule(
        name="Module 5 — Protection banner (clear & card-safe)",
        role="a+_banner",
        headline="CLEAR AND CARD-SAFE",
        body=(
            "Clear polypropylene lets you read every card front and back without pulling it out, while "
            "acid-free, no-PVC material helps guard Pokemon, Magic (MTG), One Piece, Yu-Gi-Oh and sports "
            "cards against yellowing, moisture and everyday handling."
        ),
        visual="Banner: one 9-pocket page centered on black with thin white arrow callouts to the clear film, snug pockets and acid-free / no-PVC material. Red top-line and white headline.",
        alt="A+ banner with callouts to the clear film, snug pockets and acid-free, no-PVC material of a 9-pocket page.",
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
        visual="Closing banner: Ultra PRO logo centered on black, filled binders softly behind, footer lockup with a USA-flag 'Made in USA' mark and 'Since 1952', a five-star review quote below.",
        alt="Ultra PRO brand-close banner: trusted by collectors worldwide, Made in USA since 1952, with a five-star review quote.",
    ),
]


# ENGLISH backend search terms — stem-deduped, no title/brand duplicates, ≤ 249 bytes.
BACKEND = (
    "binder card sleeves toploader album acid free storage tcg graded photo "
    "memorabilia holder collector display yugioh gathering ccg deck box "
    "page protectors sheets inserts baseball collection organizer"
)


def main() -> None:
    print("Loading Ultra PRO customer + parsing product 47 listing.xlsx…")
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
