"""Ultra PRO Premium Series 4-Pocket SECURE Pages (100 Pages) — Image Plan (PLAN 36).

Hand-written senior copy in the established Ultra PRO catalog format, built with
the EQUALICE brief_app. Reads the product's own listing.xlsx (SEO axis) and emits
a branded PDF image plan + A+ script.

WHAT MAKES THIS SKU DISTINCT (do NOT reuse 9-pocket page creative):
  These are 4-POCKET pages engineered to HOLD TOPLOADERS inside a standard 3-ring
  binder — one card, in its toploader, per pocket, secured by an individual
  protective flap. They fit toploaders up to 130pt, so thick / valuable / graded-
  style cards live in the binder instead of a shoebox. The hero is a toploader
  sliding into a 4-pocket page and the secure flap holding it in place.

LANGUAGE SPLIT (the standard):
  • ENGLISH — art-direction / strategy fields the designer reads:
    background, purpose, visual, props, lighting, why_it_works, ctr, cvr,
    and module visual/alt.
  • ENGLISH customer copy (marketplace = amazon.com):
    TITLE, BULLETS, image overlay/overlay_sub, module headline/body, BACKEND.

ULTRA PRO STYLE (matched in the art direction of every image):
  black background, bold RED #C8102E top-line + big WHITE headline; feature
  callouts with thin arrows; icon-stat bars (fits 3-ring binders · holds up to
  400 toploaders); a red circular clarity badge; REAL popular cards (Pokemon,
  MTG, One Piece, sports) in toploaders in the page/binder; real collector
  lifestyle; the product box; brand close 'Trusted since 1952 · Made in USA'.
  (Image 1 / main image stays on a clean white background per Amazon policy.)

GUARDRAILS (auto-checked on build):
  overlay ≤30 chars AND ≤5 words, smooth (no middots, no fragments) ·
  overlay_sub ≤90 · module headline ≤38 · bullet head <b>…</b> ≤45 · TITLE ≤200.
COMPLIANCE: no "#1", no "best", no "leading", no "guaranteed", no "$", no URL/.com.
  Brand-trust proof expressed as "Trusted since 1952"; clarity as "clear /
  high-clarity"; strength as "secure / superior".

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
PLAN_NO = "36"
ASIN = "B09P9SK3Q4"


# ===== Customer-facing copy (ENGLISH — amazon.com) =====

# HTML-escaped "&" counts as 1 real char. Keep de-escaped length ≤ 200.
TITLE = (
    "Ultra PRO Premium Series 4-Pocket SECURE Pages (100 Pages) — Toploader Pages for Binder "
    "that Hold Toploaders up to 130pt · For Pokemon, MTG &amp; Sports Cards · Acid-Free / No PVC "
    "· Fits 3-Ring Binders"
)

BULLETS = [
    "<b>HOLDS TOPLOADERS IN YOUR BINDER</b> — These secure 4 pocket pages are built to hold your "
    "cards in their toploaders, so thick, valuable and graded-style cards finally live in a standard "
    "3-ring binder instead of a box — one toploader per pocket, four per page.",

    "<b>FITS THICK CARDS UP TO 130PT</b> — Each pocket is sized for toploaders up to 130pt thickness, "
    "so chunky rookies, holos and slabs slide right in. The perfect toploader pages for binder storage "
    "when regular sleeves are simply too thin to hold the card.",

    "<b>A PROTECTIVE FLAP ON EVERY POCKET</b> — An individual flap folds over each of the four pockets "
    "to keep every toploader from sliding out and to help keep dust and debris away — secure pages that "
    "hold cards firmly, even when you flip the binder.",

    "<b>FITS STANDARD 3-RING BINDERS</b> — A standard 3-hole punched design drops straight into any "
    "3-ring binder or album, so your toploaders stay sorted, upright and easy to browse. Clear pages "
    "let you read every card, front and back, without pulling it out.",

    "<b>TRUSTED BY COLLECTORS SINCE 1952</b> — Ultra PRO has protected collectibles since 1952. "
    "Acid-free, non-PVC 4 pocket card binder sleeves that guard Pokemon, Magic (MTG), One Piece and "
    "sports cards — 100 pages per pack, proudly Made in USA.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (product box + loaded 4-pocket secure page)",
        role="hero",
        background="Pure white #FFFFFF seamless — Amazon main-image policy (no overlay text, no graphics).",
        purpose="Win the click in the amazon.com card-storage grid — instantly read as pages that hold cards in toploaders inside a binder.",
        visual=(
            "Product box (Premium Series 4-Pocket SECURE Pages, 100 Pages) standing three-quarter left, "
            "label fully legible. To its right, ONE 4-pocket page held upright with all four pockets loaded "
            "with real popular cards INSIDE clear toploaders (Pokemon holo, MTG, One Piece, a sports rookie) "
            "— the protective flaps visible over each pocket. Tight crop, product ~85% of frame, subtle "
            "contact shadow, no overlay text."
        ),
        overlay="(no overlay — Amazon main image)",
        overlay_sub="",
        props=["Premium Series 4-Pocket SECURE Pages box", "one 4-pocket page loaded with cards in toploaders", "clear toploaders", "Pokemon / MTG / One Piece / sports cards"],
        lighting="Bright, even studio light; soft rim on the page and toploader edges so the clear plastic and card art pop against white.",
        why_it_works=(
            "The box plus a page holding four carded toploaders communicates product type (4-pocket secure "
            "pages), what it does (holds toploaders) and capacity in one glance — exactly what a collector "
            "with thick cards scans for."
        ),
        ctr="Toploaders visibly held inside binder pages is an instant pattern interrupt against generic empty-page thumbnails.",
        cvr="Shows precisely what the buyer receives and proves the core promise — cards stay in their toploaders — up front.",
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: a toploader sliding into the secure pocket (macro)",
        role="hook",
        background="Black #111111. Bold RED #C8102E top-line 'SECURE STORAGE', big WHITE headline below.",
        purpose="Prove the single strongest promise in one shot — a full toploader slides in and the flap holds it.",
        visual=(
            "Extreme macro: a hand slides a clear toploader (holding a holo Pokemon / MTG card) into one "
            "4-pocket page pocket; the individual protective flap is mid-fold over the top. Thin white arrow "
            "tags 'protective flap' and 'holds toploaders up to 130pt'. A red circular badge top-right reads "
            "'HOLDS THICK CARDS'. White headline lower-left."
        ),
        overlay="TOPLOADERS IN YOUR BINDER",
        overlay_sub="Slide a full toploader into every pocket and let the flap hold it secure.",
        props=["macro of a toploader entering a pocket", "protective flap mid-fold", "red circular 'holds thick cards' badge", "thin arrow tags"],
        lighting="Hard raking side-light on black so the clear toploader reads as glass and the flap edge is crisp.",
        why_it_works=(
            "Answers the collector's first question — 'will my toploaders actually fit and stay in?' — with a "
            "proof macro, and shows the flap mechanism that sets this SKU apart from thin sleeve pages."
        ),
        ctr="A giant toploader sliding into a binder pocket on black stops the scroll in a grid of flat product shots.",
        cvr="Macro proof of the toploader fitting plus the flap defuses the two biggest fears before the click.",
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: feature callouts",
        role="educate",
        background="Black #111111, RED top-line 'PREMIUM SECURE FEATURES', WHITE headline.",
        purpose="Stack the secure-page feature set thin sleeve pages can't match, as scannable arrow callouts.",
        visual=(
            "One 4-pocket page centered on black, a carded toploader in each pocket, thin white arrows "
            "radiating to labeled callouts: HOLDS TOPLOADERS · FITS UP TO 130PT · PROTECTIVE FLAP PER POCKET "
            "· ACID-FREE / NO PVC · CLEAR BOTH SIDES · FITS 3-RING BINDERS. Each callout with a small line "
            "icon. Red accent underlines under the two headline words."
        ),
        overlay="BUILT TO HOLD TOPLOADERS",
        overlay_sub="Holds toploaders up to 130pt, one secure flap over every pocket.",
        props=["4-pocket page loaded with toploaders", "6 arrow callouts with line icons", "red accent underlines"],
        lighting="Even soft light on the page, slightly brighter center so the product stays the focal point on black.",
        why_it_works=(
            "Turns spec words into a visual proof stack — 130pt fit, per-pocket flap, acid-free/no-PVC — the "
            "exact things a collector with thick, valuable cards filters for and a thin sleeve page cannot claim."
        ),
        ctr="A dense, well-organized feature stack signals serious protection and earns the click from graded-card buyers.",
        cvr="Each callout removes a specific doubt (thickness, slipping, acid, PVC), compounding trust toward purchase.",
    ),
    AIImagePlanItem(
        name="Image 4 — Desire: collector filing toploaders into a binder (lifestyle)",
        role="desire",
        background="Warm collector desk scene; product graphics kept to a slim black/red lower band.",
        purpose="Let the buyer self-cast into a binder where their thick, valuable cards live safely in toploaders.",
        visual=(
            "Over-the-shoulder lifestyle: a collector's hands slide a toploaded card into a 4-pocket page in "
            "an open 3-ring binder on a tidy desk, more filled pages of carded toploaders fanned nearby "
            "(Pokemon, sports). Warm, aspirational, real. Slim black lower band with red top-line 'YOUR THICK "
            "CARDS, ORGANIZED' and the white headline."
        ),
        overlay="THICK CARDS ORGANIZED",
        overlay_sub="Keep your toploaders sorted upright in one clean binder you are proud of.",
        props=["collector's hands", "open 3-ring binder", "4-pocket pages loaded with toploaders", "Pokemon & sports cards", "tidy desk"],
        lighting="Warm natural desk light from camera-left, soft and lived-in — hobbyist, not clinical.",
        why_it_works=(
            "Moves from features to the emotional payoff — the valuable cards that used to sit loose in a box "
            "now organized and visible in a binder — which is what turns a browsing collector into a buyer."
        ),
        ctr="A relatable collector-desk moment with toploaders in a binder stands out against sterile product-only tiles.",
        cvr="Buyers picture their own thick cards finally in the binder, making the purchase feel like the next step.",
    ),
    AIImagePlanItem(
        name="Image 5 — Trust: the flap holds every toploader secure",
        role="trust",
        background="Black #111111, RED top-line 'SECURE 4-POCKET DESIGN', WHITE headline.",
        purpose="Defuse the fear that a heavy toploader slips out — the protective flap holds it, even flipped.",
        visual=(
            "A page rotated / held upside-down to show carded toploaders staying firmly in their pockets under "
            "the closed flaps. Thin white arrows call out 'individual protective flap' and 'keeps dust out'. A "
            "small red badge 'CARDS STAY PUT'. Optional stress-cue: a gentle tug on a toploader, staying seated."
        ),
        overlay="TOPLOADERS STAY SECURE",
        overlay_sub="An individual flap over each pocket holds every toploader firmly in place.",
        props=["page rotated / inverted with toploaders held", "arrow callouts to flaps", "red 'cards stay put' badge"],
        lighting="Focused key on the flap edges so the secure closure reads as strong and precise.",
        why_it_works=(
            "Targets the top fear for toploader-in-binder storage (a heavy card falling out). Showing the flap "
            "and the held toploaders upside-down is concrete proof, not a promise."
        ),
        ctr="The upside-down 'still held' visual is a curiosity hook that stops the scroll.",
        cvr="Directly answers 'will my toploaders fall out?' with visible flap proof, removing a purchase blocker.",
    ),
    AIImagePlanItem(
        name="Image 6 — Desire: fit & capacity (toploader spec + icon stats)",
        role="desire",
        background="Black #111111, RED top-line 'SIZED FOR TOPLOADERS', WHITE headline; icon-stat bar along the bottom.",
        purpose="Prove exact toploader fit and total capacity so the buyer knows it works for their cards and binder.",
        visual=(
            "A single toploader ghosted inside a pocket with a clean thickness callout 'UP TO 130PT' and arrows "
            "to the pocket walls and flap. Above, the standard 3-hole punch aligned to binder rings. Bottom "
            "icon-stat bar with two tiles: 'FITS STANDARD 3-RING BINDERS' and 'HOLDS UP TO 400 TOPLOADERS'. "
            "Red accents on the stat icons."
        ),
        overlay="FITS UP TO 130PT",
        overlay_sub="Pockets sized for toploaders up to 130pt, four per page, 100 pages per pack.",
        props=["thickness callout 'up to 130pt'", "3-hole punch aligned to rings", "two icon-stat tiles"],
        lighting="Clean technical light — flat and legible so the thickness spec and stat icons read instantly.",
        why_it_works=(
            "Removes the last practical doubts — 'will my toploader fit, and how many does a pack hold?' — with "
            "exact numbers (130pt, 4 per page, up to 400) a spec-driven collector trusts."
        ),
        ctr="Concrete numbers (130pt, 400 toploaders, 3-ring) signal precision and pull spec-checking buyers.",
        cvr="Exact fit and capacity data closes the sizing objection and justifies the buy.",
    ),
    AIImagePlanItem(
        name="Image 7 — Close: brand trust (since 1952 · Made in USA)",
        role="close",
        background="Black #111111 with the Ultra PRO logo; subtle red heritage line motif.",
        purpose="Close on brand identity and heritage — the protection collectors have trusted for decades.",
        visual=(
            "Centered Ultra PRO logo on black, a neat row of filled binders / pages of carded toploaders softly "
            "behind. RED top-line 'TRUSTED BY COLLECTORS WORLDWIDE', big WHITE headline, and a footer lockup: a "
            "small USA-flag mark with 'Made in USA' beside 'Since 1952'."
        ),
        overlay="TRUSTED SINCE 1952",
        overlay_sub="Protecting collections with USA-made quality since 1952.",
        props=["Ultra PRO logo", "row of filled binders / toploader pages", "USA-flag 'Made in USA' mark"],
        lighting="Premium low-key light, soft glow on the logo — authoritative, heritage, category-anchor feel.",
        why_it_works=(
            "Ends on heritage and provenance — the trust cue that converts a hesitating collector who wants a "
            "brand that will still be here to protect the valuable cards they are storing."
        ),
        ctr="The heritage 'since 1952 · Made in USA' lockup signals category authority and reassures at a glance.",
        cvr="Provenance and longevity provide the final trust nudge that seals the purchase.",
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Brand banner (hero)",
        role="a+_banner",
        headline="TOPLOADERS IN YOUR BINDER",
        body=(
            "Premium Series 4-Pocket SECURE Pages hold your cards in their toploaders inside a standard "
            "3-ring binder — four pockets per page, an individual protective flap over each one, and clear "
            "sides so you see every card. 100 pages per pack, ready for your collection."
        ),
        visual="Wide cinematic banner: product box left, a fanned spread of 4-pocket pages loaded with carded toploaders (Pokemon, MTG, One Piece, sports) right, on black with a red accent bar. Ultra PRO logo top-left.",
        alt="Ultra PRO 4-Pocket SECURE Pages box beside pages holding trading cards in toploaders on a black background.",
    ),
    AIModule(
        name="Module 2 — Lifestyle banner",
        role="a+_banner",
        headline="PROTECT WHAT MATTERS MOST",
        body=(
            "From a graded-style rookie to your favorite holo, the cards worth a toploader deserve to live in "
            "your binder — not a shoebox. Secure 4-pocket pages keep thick, valuable cards sorted, upright and "
            "easy to browse, acid-free and non-PVC so the collection you love stays safe for years."
        ),
        visual="Warm lifestyle scene: a collector sliding a toploaded card into a 4-pocket page in an open binder at a tidy desk, more toploaders visible, soft daylight. Slim black/red lower band with the headline.",
        alt="A collector filing toploaders into 4-pocket pages in a 3-ring binder at a desk.",
    ),
    AIModule(
        name="Module 3 — Feature carousel (the secure set)",
        role="a+_carousel",
        headline="THE SECURE DIFFERENCE",
        body=(
            "Tile 1: <b>HOLDS TOPLOADERS</b> — one full toploader in every pocket.<br/>"
            "Tile 2: <b>FITS UP TO 130PT</b> — sized for thick, valuable cards.<br/>"
            "Tile 3: <b>PROTECTIVE FLAP</b> — a flap per pocket keeps cards in.<br/>"
            "Tile 4: <b>NO PVC / ACID-FREE</b> — safe long-term storage.<br/>"
            "Tile 5: <b>CLEAR BOTH SIDES</b> — read every card without pulling it.<br/>"
            "Tile 6: <b>FITS 3-RING BINDERS</b> — standard 3-hole punched design."
        ),
        visual="6 square tiles on black, red accent corner and a line icon per tile (toploader · caliper · flap · no-PVC · clear page · 3-ring). Consistent Ultra PRO styling.",
        alt="Six-tile A+ carousel of 4-Pocket SECURE Pages features: holds toploaders, fits 130pt, protective flap, no PVC/acid-free, clear both sides, fits 3-ring binders.",
    ),
    AIModule(
        name="Module 4 — Protection banner (feature callouts)",
        role="a+_banner",
        headline="BUILT TO HOLD THICK CARDS",
        body=(
            "Pockets sized for toploaders up to 130pt, an individual protective flap over each one, and "
            "acid-free, non-PVC material protect Pokemon, Magic (MTG), One Piece, Yu-Gi-Oh and sports cards "
            "from dust, moisture and everyday wear — so the cards you kept in a box finally live in the binder."
        ),
        visual="Banner: one 4-pocket page loaded with toploaders centered on black with thin white arrow callouts to the flaps, the 130pt pocket, the material and the clear sides. Red top-line and white headline.",
        alt="A+ banner with feature callouts pointing to the flaps, 130pt pockets, acid-free material and clear sides of a 4-pocket secure page.",
    ),
    AIModule(
        name="Module 5 — Organize banner (icon stats)",
        role="a+_banner",
        headline="ORGANIZE YOUR TOPLOADERS",
        body=(
            "The standard 3-hole punched design fits standard 3-ring binders and albums, and one 100-page pack "
            "holds up to 400 toploaders — four per page — so your whole toploader collection lives in one place, "
            "neatly sorted and easy to browse. Clear pages let you read every card at a glance."
        ),
        visual="Banner with two large icon-stat tiles on black: 'FITS STANDARD 3-RING BINDERS' and 'HOLDS UP TO 400 TOPLOADERS', a binder with loaded pages alongside. Red stat icons.",
        alt="A+ banner with icon stats: fits standard 3-ring binders and holds up to 400 toploaders.",
    ),
    AIModule(
        name="Module 6 — Brand close (heritage + review)",
        role="a+_banner",
        headline="TRUSTED SINCE 1952",
        body=(
            "Collectors worldwide trust Ultra PRO for collectible protection — proudly Made in USA since "
            "1952. <br/><br/>“They fit perfectly in my binder and my cards are well-protected.” "
            "&#9733;&#9733;&#9733;&#9733;&#9733;"
        ),
        visual="Closing banner: Ultra PRO logo centered on black, filled binders of toploader pages softly behind, footer lockup with a USA-flag 'Made in USA' mark and 'Since 1952', a five-star review quote below.",
        alt="Ultra PRO brand-close banner: trusted by collectors worldwide, Made in USA since 1952, with a five-star review quote.",
    ),
]


# ENGLISH backend search terms — stem-deduped, no title/brand duplicates, ≤ 249 bytes.
BACKEND = (
    "top loader binder sleeves side loader card pages toploader sheets 3 hole "
    "protectors graded slab thick card holder yugioh one piece baseball tcg ccg "
    "album organizer flap dust proof collection display 130pt"
)


def main() -> None:
    print("Loading Ultra PRO customer + parsing listing.xlsx…")
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
    builder._ai_qa = []  # client instruction: no Q&A module
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
