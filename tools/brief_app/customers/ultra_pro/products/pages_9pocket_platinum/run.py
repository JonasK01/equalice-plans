"""Ultra PRO PLATINUM Series 9-Pocket Pages (25-Pack) — Image Plan (PLAN 41).

Product 41 · ASIN B07T9JMHTQ · amazon.com (English).
Standard-size cards (2.5" x 3.5"), 9-pocket pages, 25-page pack, 3-hole punched
spine for 3-ring binders, ultra-clear non-PVC / acid-free polypropylene film,
solid-bar seals, lays flat. Reads the SEO axis from listing.xlsx (parse_excel).

DISTINCT FROM THE SAMPLE 9-pocket plan: this brief leads specifically on the
PLATINUM grade + solid-bar welds + crystal clarity + hologram authenticity, and
uses this SKU's real spec (25-pack, ~450 cards, 3-ring / 3-hole). Overlays are
all new (not cloned from the sample).

LANGUAGE SPLIT (the standard):
  • ENGLISH — art-direction fields the designer reads (background, purpose,
    visual, props, lighting, why_it_works, ctr, cvr, module visual/alt).
  • ENGLISH customer copy (marketplace = amazon.com):
    TITLE, BULLETS, overlay/overlay_sub, module headline/body, BACKEND.

ULTRA PRO STYLE (in the art direction of every image):
  black background, bold RED #C8102E top-line + big WHITE headline; feature
  callouts with thin arrows; icon-stat bars (fits 3-ring binders · stores up to
  450 cards); a red circular clarity badge; REAL popular cards (Pokemon, MTG,
  One Piece, sports) in the page/binder; real collector lifestyle; the product
  box; a dimension callout (2.5" x 3.5"); brand close 'Trusted since 1952 ·
  Made in USA'. (Image 1 / main image stays on clean white per Amazon policy.)

GUARDRAILS (auto-checked on build):
  overlay ≤30 chars AND ≤5 words, smooth (no middots) · overlay_sub ≤90 ·
  module headline ≤38 · bullet head <b>…</b> ≤45 · TITLE ≤200.
COMPLIANCE: no "#1", no "best", no "leading", no "guaranteed", no "prevent",
  no "$", no URL/.com. Heritage proof as "Trusted since 1952", clarity as
  "Crystal Clarity", strength as "Superior seal strength / solid-bar welds".

Client instruction (per Jonas, listings 35-50): NO Q&A module, NO Comparison
module. Ships 7 images + 6 A+ banners/carousels.
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
PLAN_NO = "41"
ASIN = "B07T9JMHTQ"


# ===== Customer-facing copy (ENGLISH — amazon.com) =====

# HTML-escaped "&" counts as 1 real char. Keep de-escaped length ≤ 200.
TITLE = (
    "Ultra PRO Platinum Series 9-Pocket Pages (25-Pack) — Trading Card Pages for "
    "Pokemon, MTG, One Piece &amp; Sports · Holds 450 Cards · No PVC / Acid-Free · "
    "Fits 3-Ring Binders · Made in USA"
)

BULLETS = [
    "<b>PLATINUM-GRADE CARD PROTECTION</b> — Platinum Series pages are built from ultra-clear, "
    "archival, acid-free polypropylene with no PVC, so your Pokemon, Magic (MTG), One Piece and "
    "sports cards stay safe, flat and true-to-color for years in one binder.",

    "<b>SOLID-BAR WELDS HOLD CARDS TIGHT</b> — Solid-bar seals and superior seal strength keep "
    "every card firmly in its pocket instead of slipping or falling out, while the lay-flat build "
    "resists curling so these 9 pocket pages display cleanly, front and back.",

    "<b>CRYSTAL-CLEAR, TRUE-COLOR VIEWING</b> — High-clarity film shows off every card in crystal "
    "detail with no haze or glare, so graded rookies, holos and chase cards read sharp and true "
    "through these platinum series pages without ever taking a card out.",

    "<b>FITS 3-RING BINDERS, HOLDS 450 CARDS</b> — A 3-hole punched spine fits standard 3-ring "
    "binders and albums, and 25 nine-pocket trading card pages store up to 450 cards, front and "
    "back — an easy way to sort and expand a growing collection.",

    "<b>GENUINE ULTRA PRO, TRUSTED SINCE 1952</b> — Look for the Ultra PRO hologram for genuine "
    "Platinum Series quality. Ultra PRO has protected collectibles since 1952 — archival, acid-free "
    "pages that also store photos and memorabilia, proudly Made in USA.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (product pack + loaded 9-pocket page)",
        role="hero",
        background="Pure white #FFFFFF seamless — Amazon main-image policy (no overlay text, no graphics).",
        purpose="Win the click in the amazon.com card-storage grid — instantly read as a premium, crystal-clear Platinum 9-pocket page system.",
        visual=(
            "The Platinum Series 9-Pocket Pages pack (25 pages) standing three-quarter left, label fully "
            "legible. To its right, ONE 9-pocket page held upright and fully loaded with real popular cards "
            "(Pokemon, MTG, One Piece, a sports rookie) — the film reads glass-clear so every card face is "
            "sharp. Tight crop, product ~85% of frame, subtle contact shadow, no overlay text."
        ),
        overlay="(no overlay — Amazon main image)",
        overlay_sub="",
        props=["Platinum Series 25-page pack", "one loaded 9-pocket page", "Pokemon / MTG / One Piece / sports cards"],
        lighting="Bright, even studio light; soft rim on the page edge so the crystal-clear film and card art pop against white.",
        why_it_works=(
            "The pack plus a fully loaded, glass-clear page communicates product type (9-pocket pages), "
            "capacity and clarity in one glance — the three things a collector scans for in the storage grid."
        ),
        ctr="Real recognizable cards behind crystal-clear film out-signal generic empty-page thumbnails and pull the click.",
        cvr="Shows exactly what the buyer receives (pack + pages) and proves clarity up front, cutting hesitation.",
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: crystal clarity proof (macro)",
        role="hook",
        background="Black #111111. Bold RED #C8102E top-line 'PLATINUM CLARITY', big WHITE headline below.",
        purpose="Prove the single strongest promise — see every card in crystal, true-color detail through the film.",
        visual=(
            "Extreme macro of one filled pocket: a holographic Pokemon / MTG card seen through the glass-clear "
            "film, edges razor-sharp, colors true. A red circular badge top-right reads 'CRYSTAL CLARITY'. Thin "
            "white arrow points to 'ultra-clear archival film'. White headline lower-left."
        ),
        overlay="SEE CARDS IN CRYSTAL CLARITY.",
        overlay_sub="High-clarity, archival film keeps every card sharp and true to color.",
        props=["macro of a holo card in a clear pocket", "red circular 'crystal clarity' badge", "thin arrow to film"],
        lighting="Hard raking side-light on black to make the clear film read as glass and reveal true card color.",
        why_it_works=(
            "Answers the collector's top question — 'will I actually see my cards?' — with a proof macro, the "
            "defining Platinum-grade advantage over hazy budget pages."
        ),
        ctr="A giant, glass-clear holo card on black is a pattern interrupt in a grid full of flat product shots.",
        cvr="Macro proof of true-color clarity defuses the biggest fear before the click.",
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: platinum-grade feature callouts",
        role="educate",
        background="Black #111111, RED top-line 'PLATINUM-GRADE FEATURES', WHITE headline.",
        purpose="Stack the Platinum feature set a budget page can't match, as scannable arrow callouts.",
        visual=(
            "One 9-pocket page centered on black, thin white arrows radiating to labeled callouts: "
            "ARCHIVAL · NO PVC / ACID-FREE · ULTRA-CLEAR FILM · LAYS FLAT · SOLID-BAR WELDS · SUPERIOR SEAL. "
            "Each callout with a small line icon. Red accent underlines under the headline."
        ),
        overlay="PLATINUM-GRADE PROTECTION.",
        overlay_sub="Archival, acid-free, no PVC, ultra-clear film with solid-bar welds.",
        props=["9-pocket page (hero object)", "6 arrow callouts with line icons", "red accent underlines"],
        lighting="Even soft light on the page, slightly brighter center so the product stays the focal point on black.",
        why_it_works=(
            "Turns spec words into a visual proof stack — the archival / no-PVC / ultra-clear set is exactly "
            "what a serious collector filters for and what a bargain page cannot claim."
        ),
        ctr="A dense, well-organized feature stack signals 'serious protection' and earns the click from graded-card buyers.",
        cvr="Each callout removes a specific doubt (acid, PVC, haze, welds), compounding trust toward purchase.",
    ),
    AIImagePlanItem(
        name="Image 4 — Desire: collector organizing a binder (lifestyle)",
        role="desire",
        background="Warm collector desk scene; product graphics kept to a slim black/red lower band.",
        purpose="Let the buyer self-cast into a calm, pro-organized collection they are proud of.",
        visual=(
            "Over-the-shoulder lifestyle: a collector's hands slide a loaded 9-pocket page into a 3-ring binder "
            "on a tidy desk, more filled pages fanned nearby showing Pokemon and sports cards. Warm, aspirational, "
            "real. Slim black lower band with red top-line 'ORGANIZE LIKE A PRO' and the white headline."
        ),
        overlay="SORT YOUR WHOLE COLLECTION.",
        overlay_sub="Slide loaded pages into one clean, pro-organized 3-ring binder.",
        props=["collector's hands", "3-ring binder", "loaded 9-pocket pages", "Pokemon & sports cards", "tidy desk"],
        lighting="Warm natural desk light from camera-left, soft and lived-in — hobbyist, not clinical.",
        why_it_works=(
            "Moves from features to the emotional payoff — a proud, organized collection — which is what turns a "
            "browsing collector into a buyer."
        ),
        ctr="A relatable collector-desk moment stands out against sterile product-only tiles and invites the click.",
        cvr="Buyers picture their own collection organized this way, making the purchase feel like the next step.",
    ),
    AIImagePlanItem(
        name="Image 5 — Trust: solid-bar welds & seal strength",
        role="trust",
        background="Black #111111, RED top-line 'SOLID-BAR WELDS', WHITE headline.",
        purpose="Defuse the fear that cards slip or fall out — the solid-bar welds hold them securely.",
        visual=(
            "A page rotated to show a card held firmly in its pocket even upside-down; thin white arrows call out "
            "'solid-bar welds' along the seams and 'superior seal strength' at the pocket mouth. A small red badge "
            "'HOLDS CARDS TIGHT'. Optional stress-cue: a hand tilting the page, the card staying put."
        ),
        overlay="SOLID-BAR WELDS HOLD TIGHT.",
        overlay_sub="Solid-bar welds and superior seal strength hold every card firmly in place.",
        props=["page rotated / inverted", "arrow callouts to welds and seal", "red 'holds cards tight' badge"],
        lighting="Focused key on the weld seams so the solid-bar construction reads as strong and precise.",
        why_it_works=(
            "Targets the top negative-review fear in card storage (cards slipping out). Showing the weld and the "
            "held card is concrete proof, not a promise."
        ),
        ctr="The upside-down 'still held' visual is a curiosity hook that stops the scroll.",
        cvr="Directly answers 'will my cards fall out?' with visible solid-bar construction, removing a purchase blocker.",
    ),
    AIImagePlanItem(
        name="Image 6 — Desire: precision fit & capacity (dimensions + icon stats)",
        role="desire",
        background="Black #111111, RED top-line 'PRECISION STORAGE', WHITE headline; icon-stat bar along the bottom.",
        purpose="Prove exact fit and capacity so the buyer knows it works for their cards and binder.",
        visual=(
            "A single card ghosted inside a pocket with a clean dimension callout '2.5\" x 3.5\"' and arrows to the "
            "pocket edges. Above, the 3-hole punched spine aligned to binder rings. Bottom icon-stat bar with two "
            "tiles: 'FITS STANDARD 3-RING BINDERS' and 'STORES UP TO 450 CARDS'. Red accents on the stat icons."
        ),
        overlay="FITS BINDERS, HOLDS 450 CARDS.",
        overlay_sub="Fits standard cards up to 2.5 x 3.5 inches in any 3-ring binder.",
        props=["dimension callout 2.5\" x 3.5\"", "3-hole spine aligned to rings", "two icon-stat tiles"],
        lighting="Clean technical light — flat and legible so the dimensions and stat icons read instantly.",
        why_it_works=(
            "Removes the last practical doubts — 'will it fit my cards and my binder, and how much does it hold?' — "
            "with exact numbers a spec-driven collector trusts."
        ),
        ctr="Concrete numbers (2.5x3.5, 450 cards, 3-ring) signal precision and pull spec-checking buyers.",
        cvr="Exact fit and capacity data closes the sizing objection and justifies the buy.",
    ),
    AIImagePlanItem(
        name="Image 7 — Close: hologram authenticity + heritage (since 1952 · Made in USA)",
        role="close",
        background="Black #111111 with the Ultra PRO logo; subtle red heritage line motif.",
        purpose="Close on genuine-article proof and heritage — the hologram-sealed protection collectors trust.",
        visual=(
            "Centered Ultra PRO logo on black, a macro of the Ultra PRO authenticity hologram on the pack in the "
            "foreground, a neat row of filled binders / loaded pages softly behind. RED top-line 'GENUINE ULTRA "
            "PRO', big WHITE headline, footer lockup: a small USA-flag 'Made in USA' mark beside 'Since 1952'."
        ),
        overlay="HOLOGRAM-SEALED AUTHENTICITY.",
        overlay_sub="Look for the Ultra PRO hologram — genuine quality, trusted since 1952.",
        props=["Ultra PRO logo", "authenticity hologram macro", "row of filled binders", "USA-flag 'Made in USA' mark"],
        lighting="Premium low-key light, soft glow on the logo and a bright refractive glint on the hologram.",
        why_it_works=(
            "Ends on provenance — the hologram proves the genuine article and heritage since 1952 reassures the "
            "collector that this brand will still be here to protect a growing collection."
        ),
        ctr="The hologram glint plus 'since 1952 · Made in USA' lockup signals authenticity and reassures at a glance.",
        cvr="Genuine-article proof and longevity provide the final trust nudge that seals the purchase.",
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Brand banner (hero)",
        role="a+_banner",
        headline="PLATINUM-GRADE CARD PROTECTION",
        body=(
            "Platinum Series 9-Pocket Pages deliver premium protection for trading cards, photos and "
            "memorabilia — ultra-clear, archival, acid-free and built with solid-bar welds. 25 pages per "
            "pack, 9 pockets each, ready for your 3-ring binder."
        ),
        visual="Wide cinematic banner: the 25-page pack left, a fanned spread of loaded 9-pocket pages (Pokemon, MTG, One Piece, sports) right, on black with a red accent bar. Ultra PRO logo top-left.",
        alt="Ultra PRO Platinum Series 9-Pocket Pages pack beside loaded pages of trading cards on a black background.",
    ),
    AIModule(
        name="Module 2 — Feature carousel (the platinum set)",
        role="a+_carousel",
        headline="THE PLATINUM DIFFERENCE",
        body=(
            "Tile 1: <b>ARCHIVAL</b> — safe long-term storage for your cards.<br/>"
            "Tile 2: <b>NO PVC / ACID-FREE</b> — will not harm or yellow cards.<br/>"
            "Tile 3: <b>ULTRA-CLEAR FILM</b> — crystal clarity, front and back.<br/>"
            "Tile 4: <b>LAYS FLAT</b> — no curl, clean display and easy flipping.<br/>"
            "Tile 5: <b>SOLID-BAR WELDS</b> — solid-bar seams keep cards put.<br/>"
            "Tile 6: <b>SUPERIOR SEAL</b> — strong pocket mouth holds cards in."
        ),
        visual="6 square tiles on black, red accent corner and a line icon per tile (shield · no-PVC · sparkle · flat page · weld seam · seal). Consistent Ultra PRO styling.",
        alt="Six-tile A+ carousel of Platinum Series features: archival, no PVC/acid-free, ultra-clear film, lays flat, solid-bar welds, superior seal.",
    ),
    AIModule(
        name="Module 3 — Clarity banner",
        role="a+_banner",
        headline="SEE EVERY CARD IN CLARITY",
        body=(
            "High-clarity, ultra-clear film shows off every Pokemon, Magic (MTG), One Piece and sports card "
            "in crystal, true-to-color detail — no haze, no glare. Read grades, holos and chase cards sharp "
            "without ever taking a card out of the page."
        ),
        visual="Banner: macro of a holo card seen through the glass-clear film on black, a red 'CRYSTAL CLARITY' badge, thin arrow to the ultra-clear film. Red top-line and white headline.",
        alt="A+ banner showing a holographic card in crystal clarity through the ultra-clear film of a 9-pocket page.",
    ),
    AIModule(
        name="Module 4 — Protection banner (welds + seal)",
        role="a+_banner",
        headline="SOLID-BAR WELDS HOLD TIGHT",
        body=(
            "Solid-bar welds, superior seal strength and archival, acid-free material hold Pokemon, Magic "
            "(MTG), One Piece, Yu-Gi-Oh and sports cards firmly in place and guard them from dust, moisture "
            "and everyday wear — while the lay-flat build resists curling."
        ),
        visual="Banner: one 9-pocket page centered on black with thin white arrow callouts to the solid-bar welds, seal, material and lay-flat edge. Red top-line and white headline.",
        alt="A+ banner with callouts pointing to the solid-bar welds, seal and archival material of a 9-pocket page.",
    ),
    AIModule(
        name="Module 5 — Organize banner (icon stats)",
        role="a+_banner",
        headline="ORGANIZE YOUR COLLECTION",
        body=(
            "The 3-hole punched spine fits standard 3-ring binders and albums, and 25 nine-pocket pages store "
            "up to 450 cards — so your whole collection lives in one place, neatly sorted and easy to browse. "
            "Holds up to 18 cards per page, front and back."
        ),
        visual="Banner with two large icon-stat tiles on black: 'FITS STANDARD 3-RING BINDERS' and 'STORES UP TO 450 CARDS', a binder with pages alongside. Red stat icons.",
        alt="A+ banner with icon stats: fits standard 3-ring binders and stores up to 450 cards.",
    ),
    AIModule(
        name="Module 6 — Brand close (hologram authenticity + heritage)",
        role="a+_banner",
        headline="GENUINE ULTRA PRO, SINCE 1952",
        body=(
            "Look for the Ultra PRO hologram for genuine Platinum Series quality. Collectors worldwide trust "
            "Ultra PRO for collectible protection — proudly Made in USA since 1952. <br/><br/>"
            "“Crystal clear and durable, my cards are well-protected.” &#9733;&#9733;&#9733;&#9733;&#9733;"
        ),
        visual="Closing banner: Ultra PRO logo centered on black, an authenticity-hologram macro and filled binders softly behind, footer lockup with a USA-flag 'Made in USA' mark and 'Since 1952', a five-star review quote below.",
        alt="Ultra PRO brand-close banner: genuine hologram, Made in USA since 1952, with a five-star review quote.",
    ),
]


# ENGLISH backend search terms — stem-deduped, no title/brand duplicates, ≤ 249 bytes.
BACKEND = (
    "binder sleeves toploader album archival uv storage tcg graded photo memorabilia "
    "holder collector display 18 pocket yugioh gathering ccg deck collection organizer "
    "page protectors sheets inserts baseball rookie chase holo"
)


def main() -> None:
    print("Loading Ultra PRO customer + parsing listing.xlsx…")
    cust = load_customer("ultra_pro")
    brief = parse_excel(EXCEL)
    OUT = HERE / f"{PLAN_NO}_{ASIN}_Image Plan.pdf"
    real_title_len = len(TITLE.replace("&amp;", "&"))
    print(f"  Product: {brief.product_name}  (ASIN {ASIN})")
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
