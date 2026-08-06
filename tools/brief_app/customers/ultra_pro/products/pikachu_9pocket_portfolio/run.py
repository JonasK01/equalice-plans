"""Ultra PRO OFFICIAL Pokemon Pikachu 9-Pocket Portfolio — Image Plan (PLAN 40).

Hand-written senior copy for a LICENSED collectible. The hero of every creative is
the OFFICIAL Pikachu portfolio cover art + real Pokemon cards displayed in the pages
— this is a licensed Pokemon collectible, NOT a generic binder. Protection specs
(acid-free, archival, non-PVC, high-clarity) are the SUPPORT, not the lead.

PRODUCT: Pikachu 9-Pocket Portfolio (fixed-page portfolio, NOT a 3-ring binder).
Holds up to 180 standard-size cards when double-loaded. High-clarity pages, acid-free
/ archival / non-PVC materials, full-art Pikachu cover. Made in California, U.S.A.
ASIN B0DTQ9CJPP · amazon.com · English.

ULTRA PRO STYLE (matched in the art direction of every image):
  black background, bold RED #C8102E top-line + big WHITE headline; feature callouts
  with thin arrows; icon-stat bars; a red circular badge; REAL Pokemon cards in the
  portfolio pages; real collector lifestyle; the product itself with the Pikachu cover;
  brand close 'Trusted since 1952 · Made in USA'. (Image 1 stays clean white per policy.)

GUARDRAILS (auto-checked on build):
  overlay ≤30 chars AND ≤5 words, smooth (no middots, no fragments) ·
  overlay_sub ≤90 · module headline ≤38 · bullet head <b>…</b> ≤45 · TITLE ≤200.
COMPLIANCE: no "#1", no "best", no "leading", no "guaranteed", no "prevent". Heritage
  proof as "Trusted since 1952", clarity as "High-Clarity / Crystal-Clear".

Client instruction (Ultra PRO listings 35-50): NO Q&A module, NO Comparison module.
This brief ships 7 images + 6 A+ banners/carousels (a+_banner / a+_carousel only).
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
PLAN_NO = "40"
ASIN = "B0DTQ9CJPP"


# ===== Customer-facing copy (ENGLISH — amazon.com) =====

# HTML-escaped "&" counts as 1 real char. Keep de-escaped length ≤ 200.
TITLE = (
    "Ultra PRO Official Pokemon Pikachu 9-Pocket Portfolio — Trading Card Binder Holds "
    "180 Cards Double-Loaded · High-Clarity Acid-Free &amp; Archival Non-PVC Pages · "
    "Full-Art Pikachu Cover · Made in USA"
)

BULLETS = [
    "<b>OFFICIAL POKEMON PIKACHU DESIGN</b> — This is a licensed Pokemon collectible with "
    "full-art Pikachu cover artwork, not a plain binder. Show off the character you love while "
    "you store and display your deck, making it the pikachu binder every fan wants on the shelf.",

    "<b>HOLDS UP TO 180 CARDS</b> — The fixed-page 9-pocket portfolio stores up to 90 cards "
    "single-loaded and up to 180 standard-size cards double-loaded, so your growing Pokemon "
    "collection lives in one 9 pocket portfolio you can flip through card by card.",

    "<b>HIGH-CLARITY, ACID-FREE PAGES</b> — See every card in crystal-clear detail through "
    "high-clarity pockets made from acid-free, archival, non-PVC material — so your cards stay "
    "sharp, true to color and safe from dust and everyday handling for years.",

    "<b>BUILT TO PROTECT YOUR COLLECTION</b> — Snug 9-pocket pages and a sturdy bound cover "
    "keep cards secure and guard against curling, moisture and scuffs, making this pokemon card "
    "binder a display and storage solution serious collectors trust.",

    "<b>MADE IN THE USA SINCE 1952</b> — Ultra PRO has protected collectibles since 1952 and "
    "builds this Pikachu portfolio in California, U.S.A. — a trading card binder that pairs "
    "official Pokemon style with the quality collectors count on.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (Pikachu portfolio, cover + a loaded page)",
        role="hero",
        background="Pure white #FFFFFF seamless — Amazon main-image policy (no overlay text, no graphics).",
        purpose="Win the click in the amazon.com card-storage grid — instantly read as the OFFICIAL Pikachu portfolio, not a generic binder.",
        visual=(
            "The closed Pikachu 9-Pocket Portfolio standing three-quarter left so the full-art Pikachu "
            "cover reads big and legible. Beside it, the portfolio opened to ONE 9-pocket page fully "
            "loaded with real Pokemon cards behind glass-clear pockets. Tight crop, product ~85% of frame, "
            "subtle contact shadow, no overlay text."
        ),
        overlay="(no overlay — Amazon main image)",
        overlay_sub="",
        props=["closed Pikachu portfolio (full-art cover)", "portfolio open to one loaded 9-pocket page", "real Pokemon cards"],
        lighting="Bright, even studio light; soft rim on the page edge so the Pikachu art and card faces pop against white.",
        why_it_works=(
            "The recognizable Pikachu cover plus a loaded glass-clear page signals licensed collectible, "
            "product type (9-pocket portfolio) and clarity in one glance — what a fan scans for in the grid."
        ),
        ctr="The official Pikachu cover art is an instant character hook that out-signals generic black binders in the storage grid.",
        cvr="Showing the cover plus a loaded page proves it is the real licensed portfolio and exactly what the buyer receives, cutting hesitation.",
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: official Pikachu design (the licensed hero)",
        role="hook",
        background="Black #111111. Bold RED #C8102E top-line 'OFFICIAL POKEMON', big WHITE headline below.",
        purpose="Lead with the licensed Pikachu artwork — the single reason a fan chooses this over a plain binder.",
        visual=(
            "The Pikachu portfolio cover fills most of the frame on black, full-art Pikachu glowing under a "
            "soft key light, a small red circular badge top-right reads 'OFFICIAL DESIGN'. A thin white arrow "
            "tags the cover 'full-art Pikachu'. White headline lower-left."
        ),
        overlay="OFFICIAL PIKACHU PORTFOLIO.",
        overlay_sub="A licensed Pokemon portfolio with full-art Pikachu cover artwork.",
        props=["full-art Pikachu cover close-up", "red 'official design' badge", "thin arrow to the cover art"],
        lighting="Soft hero key on the cover against black so the Pikachu artwork reads premium and true to color.",
        why_it_works=(
            "For a licensed collectible the character IS the product. Making Pikachu the hero answers 'is this "
            "the real official one?' immediately and separates it from commodity binders."
        ),
        ctr="A giant, glowing official Pikachu on black is a pure pattern interrupt in a grid of plain storage tiles.",
        cvr="The official-design badge confirms the license up front, defusing the fake/unofficial fear before the click.",
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: capacity (holds up to 180 cards)",
        role="educate",
        background="Black #111111, RED top-line 'BUILT-IN CAPACITY', WHITE headline.",
        purpose="Prove how much of a Pokemon collection fits — up to 180 cards double-loaded.",
        visual=(
            "The portfolio fanned open on black to show several loaded 9-pocket pages of Pokemon cards. Two "
            "icon-stat tiles along the bottom: '90 CARDS SINGLE-LOADED' and '180 CARDS DOUBLE-LOADED'. A thin "
            "arrow shows two cards sliding back-to-back into one pocket. Red accents on the stat icons."
        ),
        overlay="HOLDS UP TO 180 CARDS.",
        overlay_sub="Store up to 90 cards single-loaded or 180 double-loaded in one portfolio.",
        props=["portfolio fanned open with loaded pages", "two icon-stat tiles (90 / 180)", "arrow: double-loading a pocket"],
        lighting="Even soft light on the pages, slightly brighter center so the loaded product stays the focal point on black.",
        why_it_works=(
            "Capacity is the top spec a growing collector filters for. Showing single vs double-loaded with real "
            "numbers answers 'will my whole collection fit?' concretely."
        ),
        ctr="The concrete 180-card number signals a serious-capacity portfolio and pulls collectors with growing decks.",
        cvr="Single vs double-loaded numbers remove the capacity doubt and justify the buy for a large collection.",
    ),
    AIImagePlanItem(
        name="Image 4 — Desire: show off your Pokemon (lifestyle)",
        role="desire",
        background="Warm collector desk scene; product graphics kept to a slim black/red lower band.",
        purpose="Let a fan self-cast into proudly browsing and showing off their Pikachu collection.",
        visual=(
            "Over-the-shoulder lifestyle: a collector flips through the open Pikachu portfolio on a tidy desk, "
            "pages full of Pokemon cards catching the light, the Pikachu cover visible. Warm, aspirational, real. "
            "Slim black lower band with red top-line 'SHOW IT OFF' and the white headline."
        ),
        overlay="SHOW OFF YOUR POKEMON.",
        overlay_sub="Browse and display your favorite Pokemon cards page by page.",
        props=["collector's hands flipping the portfolio", "pages full of Pokemon cards", "Pikachu cover visible", "tidy desk"],
        lighting="Warm natural desk light from camera-left, soft and lived-in — hobbyist, not clinical.",
        why_it_works=(
            "Moves from spec to emotional payoff — pride in a collection you can flip through and show friends — "
            "which is what turns a browsing fan into a buyer."
        ),
        ctr="A relatable collector-desk moment with recognizable Pokemon cards stands out against sterile product-only tiles.",
        cvr="Buyers picture showing off their own collection this way, making the purchase feel like the next step.",
    ),
    AIImagePlanItem(
        name="Image 5 — Trust: high-clarity & protective pages",
        role="trust",
        background="Black #111111, RED top-line 'HIGH-CLARITY PROTECTION', WHITE headline.",
        purpose="Defuse the fear that cards look dull or get damaged — clear, archival, acid-free pockets.",
        visual=(
            "Extreme macro of one filled pocket: a Pokemon card seen through the glass-clear pocket, edges "
            "razor-sharp. Thin white arrows to labeled callouts: HIGH-CLARITY · ACID-FREE · ARCHIVAL · NON-PVC. "
            "A small red badge 'KEEPS CARDS SAFE'. White headline lower-left."
        ),
        overlay="KEEP YOUR CARDS SAFE.",
        overlay_sub="High-clarity, acid-free, archival non-PVC pockets keep cards sharp and protected.",
        props=["macro of a Pokemon card in a clear pocket", "4 arrow callouts", "red 'keeps cards safe' badge"],
        lighting="Hard raking side-light on black to make the clear film read as glass and reveal crisp card detail.",
        why_it_works=(
            "Answers the collector's two fears — 'will my cards look dull?' and 'will they get damaged?' — with a "
            "proof macro plus the archival / acid-free / non-PVC stack a fan filters for."
        ),
        ctr="A giant, glass-clear Pokemon card on black is a proof-driven pattern interrupt that stops the scroll.",
        cvr="Macro clarity plus the material callouts defuse the dull-look and damage fears before purchase.",
    ),
    AIImagePlanItem(
        name="Image 6 — Desire: organize your whole collection",
        role="desire",
        background="Black #111111, RED top-line 'ONE HOME FOR YOUR CARDS', WHITE headline.",
        purpose="Show the portfolio as the single, tidy home a collector keeps and grows their set in.",
        visual=(
            "The Pikachu portfolio closed on black beside a neat row of its loaded pages laid out, Pokemon cards "
            "sorted by set. Thin arrows note 'fixed 9-pocket pages' and 'flip-through storage'. A red top-line and "
            "white headline; the Pikachu cover stays visible as the anchor."
        ),
        overlay="ORGANIZE YOUR COLLECTION.",
        overlay_sub="Keep your whole Pokemon collection sorted in one portfolio you can flip through.",
        props=["closed Pikachu portfolio", "row of loaded pages sorted by set", "arrow callouts to pages"],
        lighting="Clean, slightly warm light so the sorted cards and Pikachu cover read organized and inviting.",
        why_it_works=(
            "Reinforces the practical payoff — one tidy, portable home for the collection — for buyers who hate "
            "loose cards scattered in boxes."
        ),
        ctr="A neatly sorted, one-portfolio setup signals effortless organization and draws collectors tired of loose cards.",
        cvr="Showing the whole collection sorted in one place closes the 'where do I keep them all' objection.",
    ),
    AIImagePlanItem(
        name="Image 7 — Close: brand trust (since 1952 · Made in USA)",
        role="close",
        background="Black #111111 with the Ultra PRO logo; subtle red heritage line motif.",
        purpose="Close on brand identity and heritage — the protection collectors have trusted for decades.",
        visual=(
            "Centered Ultra PRO logo on black, the Pikachu portfolio and a few loaded pages softly behind. RED "
            "top-line 'TRUSTED BY COLLECTORS WORLDWIDE', big WHITE headline, and a footer lockup: a small USA-flag "
            "mark with 'Made in USA' beside 'Since 1952'."
        ),
        overlay="TRUSTED SINCE 1952.",
        overlay_sub="Protecting collections with USA-made quality since 1952.",
        props=["Ultra PRO logo", "Pikachu portfolio + loaded pages behind", "USA-flag 'Made in USA' mark"],
        lighting="Premium low-key light, soft glow on the logo — authoritative, heritage, category-anchor feel.",
        why_it_works=(
            "Ends on heritage and provenance — the trust cue that converts a hesitating fan who wants the official "
            "product from a brand that stands behind it."
        ),
        ctr="The heritage 'since 1952 · Made in USA' lockup signals category authority and reassures at a glance.",
        cvr="Provenance and longevity give the final trust nudge that seals the purchase of a licensed collectible.",
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Brand banner (hero)",
        role="a+_banner",
        headline="OFFICIAL PIKACHU PORTFOLIO",
        body=(
            "The Ultra PRO Pikachu 9-Pocket Portfolio is a licensed Pokemon collectible with full-art "
            "Pikachu cover artwork — a place to store, display and show off your cards. High-clarity, "
            "acid-free, archival non-PVC pages hold up to 180 standard-size cards double-loaded."
        ),
        visual="Wide cinematic banner: the Pikachu portfolio cover left, an open loaded 9-pocket page of Pokemon cards right, on black with a red accent bar. Ultra PRO logo top-left.",
        alt="Ultra PRO Pikachu 9-Pocket Portfolio with full-art cover beside an open page of Pokemon cards on a black background.",
    ),
    AIModule(
        name="Module 2 — Capacity banner",
        role="a+_banner",
        headline="HOLDS UP TO 180 CARDS",
        body=(
            "The fixed-page 9-pocket portfolio stores up to 90 cards single-loaded or up to 180 standard-size "
            "cards double-loaded — so your growing Pokemon collection lives in one portfolio you can flip "
            "through, page by page, whenever you want."
        ),
        visual="Banner: the portfolio fanned open on black showing loaded pages, two large icon-stat tiles '90 SINGLE-LOADED' and '180 DOUBLE-LOADED'. Red stat icons.",
        alt="A+ banner with icon stats: holds up to 90 cards single-loaded or 180 cards double-loaded.",
    ),
    AIModule(
        name="Module 3 — Feature carousel (the protection set)",
        role="a+_carousel",
        headline="THE PIKACHU DIFFERENCE",
        body=(
            "Tile 1: <b>OFFICIAL DESIGN</b> — licensed Pokemon full-art Pikachu cover.<br/>"
            "Tile 2: <b>HIGH-CLARITY</b> — see every card sharp and true to color.<br/>"
            "Tile 3: <b>ACID-FREE</b> — safe, non-yellowing storage for your cards.<br/>"
            "Tile 4: <b>ARCHIVAL / NON-PVC</b> — built to protect for the long term.<br/>"
            "Tile 5: <b>9-POCKET PAGES</b> — up to 180 cards double-loaded.<br/>"
            "Tile 6: <b>MADE IN USA</b> — built in California since 1952."
        ),
        visual="6 square tiles on black, red accent corner and a line icon per tile (Pikachu · sparkle · shield · archival · 9-pocket grid · USA flag). Consistent Ultra PRO styling.",
        alt="Six-tile A+ carousel: official design, high-clarity, acid-free, archival non-PVC, 9-pocket pages, made in USA.",
    ),
    AIModule(
        name="Module 4 — Protection banner (feature callouts)",
        role="a+_banner",
        headline="BUILT TO PROTECT YOUR CARDS",
        body=(
            "High-clarity pockets made from acid-free, archival, non-PVC material keep Pokemon cards sharp, "
            "true to color and safe from dust, moisture and everyday handling. Snug 9-pocket pages and a sturdy "
            "bound cover help guard against curling, scuffs and wear."
        ),
        visual="Banner: one loaded 9-pocket page centered on black with thin white arrow callouts to high-clarity, acid-free, archival and non-PVC. Red top-line and white headline.",
        alt="A+ banner with feature callouts pointing to the high-clarity, acid-free, archival and non-PVC pages of the Pikachu portfolio.",
    ),
    AIModule(
        name="Module 5 — Lifestyle banner (show it off)",
        role="a+_banner",
        headline="SHOW OFF YOUR COLLECTION",
        body=(
            "From your first Pikachu pull to your rarest holo, keep every card in one portfolio you are proud "
            "to open. Flip through page by page, browse your favorites and show off your Pokemon collection to "
            "friends — organized, protected and ready to display."
        ),
        visual="Warm lifestyle scene: a collector flipping through the open Pikachu portfolio at a tidy desk, pages of Pokemon cards visible, soft daylight. Slim black/red lower band with the headline.",
        alt="A collector flipping through the open Pikachu 9-pocket portfolio full of Pokemon cards at a desk.",
    ),
    AIModule(
        name="Module 6 — Brand close (heritage + review)",
        role="a+_banner",
        headline="TRUSTED SINCE 1952",
        body=(
            "Collectors worldwide trust Ultra PRO for collectible protection — this Pikachu portfolio is proudly "
            "Made in USA, built in California since 1952. <br/><br/>“Sturdy, holds a ton of cards and the pages "
            "are crystal clear.” &#9733;&#9733;&#9733;&#9733;&#9733;"
        ),
        visual="Closing banner: Ultra PRO logo centered on black, the Pikachu portfolio and loaded pages softly behind, footer lockup with a USA-flag 'Made in USA' mark and 'Since 1952', a five-star review quote below.",
        alt="Ultra PRO brand-close banner: trusted by collectors worldwide, Made in USA since 1952, with a five-star review quote.",
    ),
]


# ENGLISH backend search terms — stem-deduped, no title/brand duplicates, ≤ 249 bytes.
BACKEND = (
    "card binder pokemon 9 pocket collection holder folder sleeve album display case "
    "tcg trading cards storage organizer fan gift kids collector standard size zipper "
    "side loader deck box protector"
)


def main() -> None:
    print("Loading Ultra PRO customer + parsing listing.xlsx…")
    cust = load_customer("ultra_pro")
    brief = parse_excel(EXCEL)
    OUT = HERE / f"{PLAN_NO}_{ASIN}_Image Plan.pdf"
    real_title_len = len(TITLE.replace("&amp;", "&"))
    print(f"  Product: {brief.product_name}")
    print(f"  ASIN: {ASIN}  Plan: {PLAN_NO}")
    print(f"  Marketplace: {cust.marketplace}  Overlay lang: {cust.overlay_language}")
    print(f"  TITLE real chars (de-escaped): {real_title_len}")

    builder = BriefBuilder(cust, brief, OUT, ai=None)
    builder._ai_title = TITLE
    builder._ai_bullets = BULLETS
    builder._ai_images = IMAGES
    builder._ai_modules = MODULES
    builder._ai_qa = []       # client instruction: NO Q&A module
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
