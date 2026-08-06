"""Ultra PRO 4-Pocket TOPLOADER Zippered Premium PRO-Binder — Image Plan 35.

Hand-written senior copy injected into the branded EQUALICE ReportLab pipeline.
Marketplace: amazon.com (English). ASIN B0CSHLGYN6.

WHAT MAKES THIS SKU DIFFERENT (do NOT reuse the generic 9-pocket pages plan):
  This is a BINDER built to store TOPLOADERS — thick, graded or valuable single
  cards in rigid plastic. The two hero angles are (1) it holds toploaders (most
  binders can't) and (2) the ZIPPERED closure makes it travel-safe so nothing
  falls out. Every image leads on ZIPPER + TOPLOADER, not on plain pages.

Verified specs (parsed from listing.xlsx):
  • 4-pocket toploader binder format · 20 clear archival-safe pages
  • Holds up to 80 standard-size cards in standard toploaders
  • Four side-loading pockets per page · secure zippered closure with pull tab
  • Padded leatherette cover · black solid rectangular design
  • Size: 11.41 x 8 x 1.59 inches

ULTRA PRO STYLE (matched in the art direction of every image):
  black background, bold RED #C8102E top-line + big WHITE bold headline; feature
  callouts with thin arrows; icon-stat bars (holds 80 toploaders · zippered ·
  padded cover); a red circular clarity/trust badge; REAL popular cards (Pokemon,
  MTG, One Piece, sports) in graded slabs / toploaders; real collector lifestyle;
  the padded binder; a dimension callout; brand close 'Trusted since 1952 · Made
  in USA'. (Image 1 / main image stays on clean white per Amazon policy.)

LANGUAGE SPLIT (the standard):
  • ENGLISH — art-direction / strategy fields the designer reads:
    background, purpose, visual, props, lighting, why_it_works, ctr, cvr, module visual/alt.
  • ENGLISH customer copy (amazon.com):
    TITLE, BULLETS, overlay/overlay_sub, module headline/body, BACKEND.

GUARDRAILS (auto-checked on build):
  overlay ≤30 chars AND ≤5 words, smooth (no fragments, no middots) ·
  overlay_sub ≤90 · module headline ≤38 · bullet head <b>…</b> ≤45 · TITLE ≤200.
COMPLIANCE: no "#1", no "best", no "leading", no "guaranteed", no "prevent",
  no "$", no URL/.com. Trust proof = "Trusted since 1952", clarity = "Crystal
  Clarity", strength = "Superior". NO Q&A module, NO Comparison module (client
  instruction, listings 35-50).
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
PLAN_NO = "35"
ASIN = "B0CSHLGYN6"


# ===== KW-led, marketing-optimized EN copy (customer-facing, amazon.com) =====

# Title is HTML-escaped, so literal "&" (as &amp;) counts as 1 real char. Keep ≤200.
TITLE = (
    "Ultra PRO 4-Pocket Toploader Binder with Zipper — Premium Zippered PRO-Binder "
    "for Pokemon, MTG, One Piece &amp; Sports Toploaders · Holds 80 Toploaders · "
    "Padded Cover · Made in USA"
)

BULLETS = [
    "<b>BUILT FOR TOPLOADERS</b> — A 4 pocket toploader binder made for thick, graded and "
    "valuable single cards. Four side-loading pockets per page hold standard toploaders snugly, "
    "so your slabbed Pokemon, MTG, One Piece and sports cards store flat and protected.",

    "<b>HOLDS UP TO 80 TOPLOADERS</b> — 20 clear archival-safe pages with four pockets each store "
    "up to 80 standard-size cards in standard toploaders — a whole showcase of your heaviest hits "
    "in one padded binder built to display, not just to stash.",

    "<b>TRAVEL-SAFE ZIPPER</b> — A secure zippered closure with an easy pull tab seals the binder "
    "shut, so toploaders stay put in your bag, at the shop or at a tournament. Nothing slides out, "
    "nothing falls loose — this zippered card binder travels with you.",

    "<b>PADDED PREMIUM COVER</b> — A padded leatherette cover in classic black cushions every knock "
    "and gives the toploader binder a premium, collector-grade feel that protects the cards inside "
    "from bumps, dust and everyday wear.",

    "<b>TRUSTED SINCE 1952</b> — Ultra PRO has protected collectibles since 1952. Crystal-clear, "
    "archival-safe pages keep every card visible and secure — a top loader binder proudly Made in "
    "USA for serious collectors.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (padded zippered binder + toploaders inside)",
        role="hero",
        background="Pure white #FFFFFF seamless — Amazon main-image policy (no overlay text, no graphics).",
        purpose="Win the click in the amazon.com toploader-binder grid — instantly read as a premium zippered binder that holds thick, graded cards.",
        visual=(
            "The black padded leatherette 4-pocket PRO-Binder shown three-quarter, zipper and pull tab "
            "clearly visible, opened just enough to reveal ONE inner page loaded with real toploaders — a "
            "graded Pokemon slab, an MTG and a sports rookie in rigid toploaders, side-loading pockets crisp. "
            "Product ~85% of frame, subtle contact shadow, no overlay text."
        ),
        overlay="(no overlay — Amazon main image)",
        overlay_sub="",
        props=["black padded zippered PRO-Binder", "one inner page loaded with toploaders", "graded Pokemon / MTG / sports cards in toploaders"],
        lighting="Bright even studio light; soft rim on the padded cover and zipper so the premium texture and the pull tab pop against white.",
        why_it_works=(
            "The zipper plus visible toploaders inside signal the two things this buyer scans for — travel-safe "
            "closure and real toploader capacity — separating it from ordinary empty-page binders in one glance."
        ),
        ctr="A zippered padded binder cracked open on real graded slabs out-signals generic empty binder thumbnails.",
        cvr="Shows exactly what the buyer receives and proves it truly holds toploaders, cutting sizing hesitation.",
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: travel-safe zipper (nothing falls out)",
        role="hook",
        background="Black #111111. Bold RED #C8102E top-line 'SECURE ZIPPERED CLOSURE', big WHITE headline below.",
        purpose="Prove the single strongest promise — the zipper seals thick cards in so nothing slides out on the move.",
        visual=(
            "The closed binder tilted and even held upside-down by the pull tab; the zipper tracked all the way "
            "around glows under a red accent line. A thin white arrow points to the pull tab tag 'seals shut'. "
            "A red circular badge top-right reads 'TRAVEL-SAFE'. White headline lower-left."
        ),
        overlay="TOPLOADERS, ZIPPED SAFE.",
        overlay_sub="A secure zippered closure seals thick toploaders in — nothing slides out.",
        props=["closed binder held upside-down by pull tab", "red circular 'TRAVEL-SAFE' badge", "arrow to zipper pull tab"],
        lighting="Hard raking side-light on black so the zipper teeth and the padded edge read premium and sealed.",
        why_it_works=(
            "Answers the collector's top fear when carrying valuable cards — 'will they fall out?' — with the "
            "upside-down sealed binder as concrete proof, not a promise."
        ),
        ctr="An upside-down binder that stays sealed is a curiosity pattern-interrupt in a grid of flat product shots.",
        cvr="The visible sealed zipper defuses the biggest objection for anyone transporting graded or valuable cards.",
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: feature callouts (why it fits toploaders)",
        role="educate",
        background="Black #111111, RED top-line 'BUILT FOR THICK CARDS', WHITE headline.",
        purpose="Stack the toploader-specific feature set as scannable arrow callouts a spec-driven buyer trusts.",
        visual=(
            "The open binder centered on black, thin white arrows radiating to labeled callouts: "
            "FOUR SIDE-LOADING POCKETS · FITS STANDARD TOPLOADERS · 20 ARCHIVAL-SAFE PAGES · SECURE ZIPPER · "
            "PADDED LEATHERETTE COVER · CRYSTAL CLARITY. Each callout with a small line icon. Red accent "
            "underlines under the two headline words."
        ),
        overlay="BUILT FOR THICK CARDS.",
        overlay_sub="Four side-loading pockets sized for standard toploaders, in archival-safe pages.",
        props=["open binder (hero object)", "6 arrow callouts with line icons", "red accent underlines"],
        lighting="Even soft light on the binder, slightly brighter center so the product stays the focal point on black.",
        why_it_works=(
            "Turns specs into a visual proof stack — side-loading pockets sized for toploaders is exactly what a "
            "graded-card collector filters for and what an ordinary page binder cannot claim."
        ),
        ctr="A dense, organized toploader-fit feature stack signals 'serious protection' and earns the click.",
        cvr="Each callout removes a specific doubt (fit, page count, zipper, padding), compounding trust to purchase.",
    ),
    AIImagePlanItem(
        name="Image 4 — Desire: collector on the move (lifestyle)",
        role="desire",
        background="Warm collector / hobby-shop scene; product graphics kept to a slim black/red lower band.",
        purpose="Let the buyer self-cast into carrying their best cards safely to a shop, meetup or tournament.",
        visual=(
            "Lifestyle: a collector slides the zipped black PRO-Binder into a backpack or sets it on a game-store "
            "counter, thumb on the pull tab, a couple of toploaders visible through a half-open page. Warm, "
            "aspirational, real. Slim black lower band with red top-line 'TAKE IT ANYWHERE' and the white headline."
        ),
        overlay="CARRY YOUR HITS SAFELY.",
        overlay_sub="Zip it shut and take your toploaders to the shop, meetup or table.",
        props=["collector's hands on the pull tab", "zipped PRO-Binder", "backpack or game-store counter", "toploaders visible in a page"],
        lighting="Warm natural light from camera-left, soft and lived-in — hobbyist, not clinical.",
        why_it_works=(
            "Moves from features to the emotional payoff — confidently carrying valuable cards — which is what turns "
            "a browsing collector into a buyer of a zippered binder over an open one."
        ),
        ctr="A relatable take-it-anywhere moment stands out against sterile product-only tiles and invites the click.",
        cvr="Buyers picture safely transporting their own graded cards, making the zipper feel worth paying for.",
    ),
    AIImagePlanItem(
        name="Image 5 — Trust: side-loading pockets hold toploaders secure",
        role="trust",
        background="Black #111111, RED top-line 'SIDE-LOADING POCKETS', WHITE headline.",
        purpose="Defuse the fear that a heavy toploader slips out of its pocket — the side-load design holds it firm.",
        visual=(
            "Macro of one page rotated to show a toploader held firmly in a side-loading pocket even when tilted; "
            "a thin white arrow calls out the side-load opening 'loads from the side, holds firm'. A small red "
            "badge 'HOLDS TOPLOADERS'. A finger easing a graded slab into the pocket shows the snug fit."
        ),
        overlay="TOPLOADERS HELD FIRM.",
        overlay_sub="Four side-loading pockets grip standard toploaders so heavy cards stay put.",
        props=["page tilted with toploader held in pocket", "arrow to side-load opening", "red 'HOLDS TOPLOADERS' badge", "finger easing in a graded slab"],
        lighting="Focused key on the pocket mouth so the snug side-load grip reads as secure and precise.",
        why_it_works=(
            "Targets the specific worry with thick cards in binders — heavy toploaders sagging or slipping — and "
            "shows the side-load pocket gripping the slab as visible construction proof."
        ),
        ctr="The tilted 'still held' toploader is a curiosity hook that stops the scroll for graded-card buyers.",
        cvr="Directly answers 'will my toploaders fall out of the pockets?' with a visible fit, removing a blocker.",
    ),
    AIImagePlanItem(
        name="Image 6 — Desire: capacity & fit (icon stats + dimensions)",
        role="desire",
        background="Black #111111, RED top-line 'ORGANIZE LIKE A PRO', WHITE headline; icon-stat bar along the bottom.",
        purpose="Prove exact capacity and size so the buyer knows how much it holds and that it fits their setup.",
        visual=(
            "The binder shown flat-open with pages fanned, a clean dimension callout '11.41\" x 8\" x 1.59\"' and an "
            "arrow to the spine depth. Bottom icon-stat bar with three tiles: 'HOLDS 80 TOPLOADERS', "
            "'4 POCKETS PER PAGE' and 'SECURE ZIPPER'. Red accents on the stat icons."
        ),
        overlay="EIGHTY TOPLOADERS, ONE BINDER.",
        overlay_sub="Twenty archival-safe pages, four pockets each — up to 80 toploaders in one place.",
        props=["dimension callout 11.41 x 8 x 1.59 in", "fanned pages", "three icon-stat tiles"],
        lighting="Clean technical light — flat and legible so the dimensions and stat icons read instantly.",
        why_it_works=(
            "Removes the last practical doubts — 'how many toploaders does it hold and how big is it?' — with exact "
            "numbers a spec-driven collector trusts before buying."
        ),
        ctr="Concrete numbers (80 toploaders, 4 pockets, zipper) signal precision and pull spec-checking buyers.",
        cvr="Exact capacity and size data closes the sizing objection and justifies the buy.",
    ),
    AIImagePlanItem(
        name="Image 7 — Close: brand trust (since 1952 · Made in USA)",
        role="close",
        background="Black #111111 with the Ultra PRO logo; subtle red heritage line motif.",
        purpose="Close on brand identity and heritage — the protection collectors have trusted for decades.",
        visual=(
            "Centered Ultra PRO logo on black, the zipped black PRO-Binder softly behind with a few toploaders "
            "beside it. RED top-line 'TRUSTED BY COLLECTORS WORLDWIDE', big WHITE headline, and a footer lockup: "
            "a small USA-flag mark with 'Made in USA' beside 'Since 1952'."
        ),
        overlay="TRUSTED SINCE 1952.",
        overlay_sub="Protecting collections with USA-made quality since 1952.",
        props=["Ultra PRO logo", "zipped black PRO-Binder", "toploaders", "USA-flag 'Made in USA' mark"],
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
        headline="A ZIPPERED HOME FOR TOPLOADERS",
        body=(
            "The Ultra PRO 4-Pocket PRO-Binder is built to store toploaders — thick, graded and valuable "
            "single cards. Twenty archival-safe pages, four side-loading pockets each, a padded leatherette "
            "cover and a secure zippered closure that keeps up to 80 toploaders travel-safe."
        ),
        visual="Wide cinematic banner: the zipped black padded binder left, a fanned spread of pages loaded with graded Pokemon, MTG, One Piece and sports toploaders right, on black with a red accent bar. Ultra PRO logo top-left.",
        alt="Ultra PRO black zippered 4-pocket PRO-Binder beside pages loaded with graded cards in toploaders on a black background.",
    ),
    AIModule(
        name="Module 2 — Hook banner (travel-safe zipper)",
        role="a+_banner",
        headline="ZIP IT SHUT, TAKE IT ANYWHERE",
        body=(
            "A secure zippered closure with an easy pull tab seals the binder all the way around, so your "
            "toploaders stay put in a bag, at the shop or at a tournament. Carry your graded Pokemon, MTG and "
            "sports hits with confidence — nothing slides out, nothing falls loose."
        ),
        visual="Banner: the closed binder held by the pull tab, red accent line tracing the zipper all the way around, a thin arrow to the pull tab. Red top-line and white headline on black.",
        alt="A+ banner of the closed zippered PRO-Binder held by its pull tab, zipper highlighted as travel-safe.",
    ),
    AIModule(
        name="Module 3 — Feature carousel (built for toploaders)",
        role="a+_carousel",
        headline="BUILT FOR TOPLOADERS",
        body=(
            "Tile 1: <b>4 SIDE-LOADING POCKETS</b> — sized to hold standard toploaders snugly.<br/>"
            "Tile 2: <b>HOLDS 80 TOPLOADERS</b> — 20 archival-safe pages, four pockets each.<br/>"
            "Tile 3: <b>SECURE ZIPPER</b> — pull-tab closure seals cards in, travel-safe.<br/>"
            "Tile 4: <b>PADDED COVER</b> — black leatherette cushions every knock.<br/>"
            "Tile 5: <b>CRYSTAL CLARITY</b> — archival-safe pages keep every card visible.<br/>"
            "Tile 6: <b>MADE IN USA</b> — Ultra PRO quality, trusted since 1952."
        ),
        visual="6 square tiles on black, red accent corner and a line icon per tile (four-pocket page · stack · zipper · padded cover · sparkle · USA flag). Consistent Ultra PRO styling.",
        alt="Six-tile A+ carousel: four side-loading pockets, holds 80 toploaders, secure zipper, padded cover, crystal clarity, Made in USA.",
    ),
    AIModule(
        name="Module 4 — Protection banner (side-loading pockets)",
        role="a+_banner",
        headline="TOPLOADERS THAT STAY PUT",
        body=(
            "Four side-loading pockets per page grip standard toploaders so even heavy graded slabs load "
            "easily and stay firmly in place. Clear, archival-safe pages keep every Pokemon, MTG, One Piece "
            "and sports card visible while the padded cover guards against bumps, dust and everyday wear."
        ),
        visual="Banner: one page centered on black with thin white arrow callouts to the side-load opening, the gripped toploader, the archival page and the padded edge. Red top-line and white headline.",
        alt="A+ banner with callouts pointing to the side-loading pocket, a gripped toploader, the archival page and padded cover.",
    ),
    AIModule(
        name="Module 5 — Capacity carousel (organize like a pro)",
        role="a+_carousel",
        headline="ORGANIZE LIKE A PRO",
        body=(
            "Tile 1: <b>UP TO 80 TOPLOADERS</b> — a whole showcase of your heaviest hits.<br/>"
            "Tile 2: <b>20 ARCHIVAL PAGES</b> — clear, archival-safe, four pockets each.<br/>"
            "Tile 3: <b>SLIM PADDED PROFILE</b> — 11.41 x 8 x 1.59 inches, easy to shelve.<br/>"
            "Tile 4: <b>DISPLAY &amp; PROTECT</b> — flip through graded cards without pulling them out."
        ),
        visual="4 identically composed tiles on black: capacity, page count, dimensions, display — real toploaders shown, red accent corner per tile, consistent light.",
        alt="Four-tile A+ carousel: up to 80 toploaders, 20 archival pages, slim padded profile, display and protect.",
    ),
    AIModule(
        name="Module 6 — Brand close (heritage + review)",
        role="a+_banner",
        headline="TRUSTED SINCE 1952",
        body=(
            "Collectors worldwide trust Ultra PRO to protect what matters — proudly Made in USA since 1952. "
            "<br/><br/>“Crystal clear and durable, my cards are well-protected.” "
            "&#9733;&#9733;&#9733;&#9733;&#9733;"
        ),
        visual="Closing banner: Ultra PRO logo centered on black, the zipped black PRO-Binder softly behind, footer lockup with a USA-flag 'Made in USA' mark and 'Since 1952', a five-star review quote below.",
        alt="Ultra PRO brand-close banner: trusted by collectors worldwide, Made in USA since 1952, with a five-star review quote.",
    ),
]


# ENGLISH backend search terms — stem-deduped, no title/brand duplicates, ≤ 249 bytes.
BACKEND = (
    "top loader binder 4 pocket toploader zippered card mini tcg trading graded slab "
    "pokemon mtg magic one piece sports storage archival page protectors album holder "
    "collector display side loading pockets padded travel case deck"
)


def main() -> None:
    print("Loading Ultra PRO customer + parsing 4-Pocket Toploader Zippered Binder Excel…")
    cust = load_customer("ultra_pro")
    brief = parse_excel(EXCEL)
    OUT = HERE / f"{PLAN_NO}_{ASIN}_Image Plan.pdf"
    real_title_len = len(TITLE.replace("&amp;", "&"))
    print(f"  Product: {brief.product_name}")
    print(f"  ASIN: {brief.asin}  Marketplace: {cust.marketplace}  Overlay lang: {cust.overlay_language}")
    print(f"  USPs={len(brief.usps)} KWs={len(brief.all_keywords)}")
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
