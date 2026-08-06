"""Ultra PRO Platinum Series 9-Pocket Pages (100 Pages) — SAMPLE Image Plan.

A hand-written DEMO brief that shows the Ultra PRO catalog format inside the
EQUALICE brief_app. There is NO listing.xlsx for this SKU — the ParsedBrief is
constructed manually in main() (only product_name is set; all other fields use
their dataclass defaults). Do NOT call parse_excel here.

LANGUAGE SPLIT (the standard):
  • ENGLISH — art-direction / strategy fields the designer reads:
    background, purpose, visual, props, lighting, why_it_works, ctr, cvr,
    and module visual/alt.
  • ENGLISH customer copy (marketplace = amazon.com):
    TITLE, BULLETS, image overlay/overlay_sub, module headline/body, BACKEND.

ULTRA PRO STYLE (matched in the art direction of every image):
  black background, bold RED top-line + big WHITE headline; feature callouts
  with thin arrows; icon-stat bars (fits 3-ring binders · stores up to 900
  cards); a red circular clarity badge; REAL popular cards (Pokemon, MTG, One
  Piece, sports) in the page/binder; real collector lifestyle; the product box;
  a dimension callout (2.5" x 3.5"); brand close 'Trusted since 1952 · Made in USA'.
  (Image 1 / main image stays on a clean white background per Amazon policy.)

GUARDRAILS (auto-checked on build):
  overlay ≤30 chars AND ≤5 words, smooth (no middots, no fragments) ·
  overlay_sub ≤90 · module headline ≤38 · bullet head <b>…</b> ≤45 · TITLE ≤200.
COMPLIANCE: no "#1", no "best", no "leading", no "guaranteed", no "prevent",
  no "$", no URL/.com. Brand-trust proof expressed as "Trusted since 1952",
  clarity as "Crystal Clarity / High Clarity", strength as "Superior".

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
from tools.brief_app.core.excel_parser import ParsedBrief
from tools.brief_app.core.pdf_builder import BriefBuilder
from tools.brief_app.core.ai import AIImagePlanItem, AIModule, AIQA


# ===== Customer-facing copy (ENGLISH — amazon.com) =====

# HTML-escaped "&" counts as 1 real char. Keep de-escaped length ≤ 200.
TITLE = (
    "Ultra PRO Platinum Series 9-Pocket Pages (100 Pages) — Archival Trading Card Pages "
    "for Pokemon, MTG, One Piece &amp; Sports · Holds 900 Cards · No PVC / Acid-Free · "
    "Fits 3-Ring Binders · Made in USA"
)

BULLETS = [
    "<b>CRYSTAL-CLEAR CARD PROTECTION</b> — Platinum-grade, high-clarity 9 pocket pages show off "
    "every Pokemon, Magic (MTG), One Piece and sports card in crystal detail — archival, acid-free "
    "and made with no PVC to keep your collection safe for years.",

    "<b>HOLDS UP TO 900 CARDS</b> — Each box packs 100 nine-pocket pages that hold up to 18 cards "
    "per page, front and back — so a single 100-page box stores an entire ~900-card collection in "
    "one binder.",

    "<b>FITS ALL STANDARD 3-RING BINDERS</b> — An 11-hole punch fits every standard 3-ring binder "
    "and album, so your trading card pages and card binder pages stay neatly organized and easy to "
    "flip through.",

    "<b>PLATINUM-GRADE DURABILITY</b> — Super-strong solid-bar welds and superior seal strength "
    "keep cards from slipping, while UV protection and a lay-flat design guard against fading, "
    "curling and everyday wear.",

    "<b>TRUSTED BY COLLECTORS SINCE 1952</b> — Ultra PRO has protected collectibles since 1952. "
    "Archival, acid-free pokemon card sleeves pages that also store photos and memorabilia — "
    "proudly Made in USA.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (product box + loaded 9-pocket page)",
        role="hero",
        background="Pure white #FFFFFF seamless — Amazon main-image policy (no overlay text, no graphics).",
        purpose="Win the click in the amazon.com card-storage grid — instantly read as a premium, crystal-clear 9-pocket page system.",
        visual=(
            "Product box (Platinum Series 9-Pocket Pages, 100 Pages) standing three-quarter left, label fully "
            "legible. To its right, ONE 9-pocket page held upright and fully loaded with real popular cards "
            "(Pokemon, MTG, One Piece, a sports rookie) — the page reads glass-clear so every card face is sharp. "
            "Tight crop, product ~85% of frame, subtle contact shadow, no overlay text."
        ),
        overlay="(no overlay — Amazon main image)",
        overlay_sub="",
        props=["Platinum Series product box", "one 9-pocket page loaded with real cards", "Pokemon / MTG / One Piece / sports cards"],
        lighting="Bright, even studio light; soft rim on the page edge so the crystal-clear plastic and card art pop against white.",
        why_it_works=(
            "The box plus a fully loaded, glass-clear page communicates product type (9-pocket pages), capacity "
            "and clarity in one glance — the three things a collector scans for in the storage grid."
        ),
        ctr="Real recognizable cards behind crystal-clear plastic out-signal generic empty-page thumbnails and pull the click.",
        cvr="Shows exactly what the buyer receives (box + pages) and proves clarity up front, cutting hesitation.",
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: crystal-clarity & durability proof (macro)",
        role="hook",
        background="Black #111111. Bold RED #C8102E top-line 'PLATINUM CLARITY', big WHITE headline below.",
        purpose="Prove the single strongest promise — see every card in crystal detail through archival, durable film.",
        visual=(
            "Extreme macro of one filled pocket: a holographic Pokemon / MTG card seen through the glass-clear "
            "pocket, edges razor-sharp. A red circular badge top-right reads 'CRYSTAL CLARITY & SUPER DURABLE'. "
            "Thin white arrow points to the weld line with a small 'super-strong welds' tag. White headline lower-left."
        ),
        overlay="SEE EVERY CARD CLEARLY",
        overlay_sub="High-clarity, archival pages keep every card sharp and true to color.",
        props=["macro of a holo card in a clear pocket", "red circular clarity badge", "thin arrow to weld line"],
        lighting="Hard raking side-light on black to make the clear film read as glass and reveal the crisp weld.",
        why_it_works=(
            "Answers the collector's top question — 'will I actually see my cards?' — with a proof macro, and pairs "
            "clarity with a durability cue so the page reads premium, not flimsy."
        ),
        ctr="A giant, glass-clear holo card on black is a pattern interrupt in a grid full of flat product shots.",
        cvr="Macro proof of clarity plus the durability badge defuses the two biggest fears before the click.",
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: feature callouts",
        role="educate",
        background="Black #111111, RED top-line 'PLATINUM-GRADE FEATURES', WHITE headline.",
        purpose="Stack the platinum feature set the cheap page can't match, as scannable arrow callouts.",
        visual=(
            "One 9-pocket page centered on black, thin white arrows radiating to labeled callouts: "
            "ARCHIVAL · NO PVC / ACID-FREE · UV PROTECTION · LAYS FLAT · SUPER-STRONG WELDS · CRYSTAL CLARITY. "
            "Each callout with a small line icon. Red accent underlines under the two headline words."
        ),
        overlay="BUILT TO PROTECT CARDS",
        overlay_sub="Archival, acid-free, no PVC, UV protection and super-strong welds.",
        props=["9-pocket page (hero object)", "6 arrow callouts with line icons", "red accent underlines"],
        lighting="Even soft light on the page, slightly brighter center so the product stays the focal point on black.",
        why_it_works=(
            "Turns spec words into a visual proof stack — the archival / no-PVC / UV set is exactly what a serious "
            "collector filters for and what a bargain page cannot claim."
        ),
        ctr="A dense, well-organized feature stack signals 'serious protection' and earns the click from graded-card buyers.",
        cvr="Each callout removes a specific doubt (acid, PVC, UV, welds), compounding trust toward purchase.",
    ),
    AIImagePlanItem(
        name="Image 4 — Desire: collector organizing a binder (lifestyle)",
        role="desire",
        background="Warm collector desk scene; product graphics kept to a slim black/red lower band.",
        purpose="Let the buyer self-cast into a calm, pro-organized collection they are proud of.",
        visual=(
            "Over-the-shoulder lifestyle: a collector's hands slide a loaded 9-pocket page into a 3-ring binder on "
            "a tidy desk, more filled pages fanned nearby showing Pokemon and sports cards. Warm, aspirational, real. "
            "Slim black lower band with red top-line 'ORGANIZE LIKE A PRO' and the white headline."
        ),
        overlay="ORGANIZE LIKE A PRO",
        overlay_sub="Sort your whole collection into one clean, pro-organized binder.",
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
        name="Image 5 — Trust: seal strength & super-strong welds",
        role="trust",
        background="Black #111111, RED top-line 'SUPERIOR SEAL STRENGTH', WHITE headline.",
        purpose="Defuse the fear that cards slip, fall out or get damaged — the page holds them securely.",
        visual=(
            "A page rotated to show a card held firmly in its pocket even upside-down; thin white arrows call out "
            "'solid-bar welds' along the seams and 'superior seal strength' at the pocket mouth. A small red badge "
            "'PROTECTS YOUR CARDS'. Optional stress-cue: a hand tugging a card gently, staying put."
        ),
        overlay="CARDS STAY SECURE",
        overlay_sub="Solid-bar welds and superior seal strength hold every card firmly in place.",
        props=["page rotated / inverted", "arrow callouts to welds and seal", "red 'protects your cards' badge"],
        lighting="Focused key on the weld seams so the solid-bar construction reads as strong and precise.",
        why_it_works=(
            "Targets the top negative-review fear in card storage (cards slipping out). Showing the weld and the "
            "held card is concrete proof, not a promise."
        ),
        ctr="The upside-down 'still held' visual is a curiosity hook that stops the scroll.",
        cvr="Directly answers 'will my cards fall out?' with visible construction proof, removing a purchase blocker.",
    ),
    AIImagePlanItem(
        name="Image 6 — Desire: precision fit & capacity (dimensions + icon stats)",
        role="desire",
        background="Black #111111, RED top-line 'PRECISION STORAGE', WHITE headline; icon-stat bar along the bottom.",
        purpose="Prove exact fit and capacity so the buyer knows it works for their cards and binder.",
        visual=(
            "A single card ghosted inside a pocket with a clean dimension callout '2.5\" x 3.5\"' and arrows to the "
            "pocket edges. Above, the 11-hole punch aligned to binder rings. Bottom icon-stat bar with two tiles: "
            "'FITS STANDARD 3-RING BINDERS' and 'STORES UP TO 900 CARDS'. Red accents on the stat icons."
        ),
        overlay="SIZED FOR YOUR CARDS",
        overlay_sub="Fits standard cards up to 2.5 x 3.5 inches in any 3-ring binder.",
        props=["dimension callout 2.5\" x 3.5\"", "11-hole punch aligned to rings", "two icon-stat tiles"],
        lighting="Clean technical light — flat and legible so the dimensions and stat icons read instantly.",
        why_it_works=(
            "Removes the last practical doubts — 'will it fit my cards and my binder, and how much does it hold?' — "
            "with exact numbers a spec-driven collector trusts."
        ),
        ctr="Concrete numbers (2.5x3.5, 900 cards, 3-ring) signal precision and pull spec-checking buyers.",
        cvr="Exact fit and capacity data closes the sizing objection and justifies the buy.",
    ),
    AIImagePlanItem(
        name="Image 7 — Close: brand trust (since 1952 · Made in USA)",
        role="close",
        background="Black #111111 with the Ultra PRO logo; subtle red heritage line motif.",
        purpose="Close on brand identity and heritage — the protection collectors have trusted for decades.",
        visual=(
            "Centered Ultra PRO logo on black, a neat row of filled binders / loaded pages softly behind. RED "
            "top-line 'TRUSTED BY COLLECTORS WORLDWIDE', big WHITE headline, and a footer lockup: a small USA-flag "
            "mark with 'Made in USA' beside 'Since 1952'."
        ),
        overlay="TRUSTED SINCE 1952",
        overlay_sub="Protecting collections with USA-made quality since 1952.",
        props=["Ultra PRO logo", "row of filled binders / loaded pages", "USA-flag 'Made in USA' mark"],
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
        headline="PREMIUM PROTECTION FOR CARDS",
        body=(
            "Platinum Series 9-Pocket Pages deliver premium protection for trading cards, photos and "
            "memorabilia — crystal-clear, archival, acid-free and built to last. 100 pages per box, "
            "9 pockets each, ready for your binder."
        ),
        visual="Wide cinematic banner: product box left, a fanned spread of loaded 9-pocket pages (Pokemon, MTG, One Piece, sports) right, on black with a red accent bar. Ultra PRO logo top-left.",
        alt="Ultra PRO Platinum Series 9-Pocket Pages box beside loaded pages of trading cards on a black background.",
    ),
    AIModule(
        name="Module 2 — Lifestyle banner",
        role="a+_banner",
        headline="PROTECT WHAT MATTERS MOST",
        body=(
            "From your first Pokemon pull to a graded sports rookie, keep every card safe in high-clarity "
            "pages made for serious collectors. Archival and acid-free, so the collection you love stays "
            "sharp for years."
        ),
        visual="Warm lifestyle scene: a collector placing a loaded page into a binder at a tidy desk, cards visible, soft daylight. Slim black/red lower band with the headline.",
        alt="A collector organizing loaded 9-pocket pages into a 3-ring binder at a desk.",
    ),
    AIModule(
        name="Module 3 — Feature carousel (the platinum set)",
        role="a+_carousel",
        headline="THE PLATINUM DIFFERENCE",
        body=(
            "Tile 1: <b>ARCHIVAL</b> — safe long-term storage for your cards.<br/>"
            "Tile 2: <b>NO PVC / ACID-FREE</b> — will not harm or yellow cards.<br/>"
            "Tile 3: <b>UV PROTECTION</b> — guards card art against fading.<br/>"
            "Tile 4: <b>LAYS FLAT</b> — no curl, clean display and easy flipping.<br/>"
            "Tile 5: <b>SUPER-STRONG WELDS</b> — solid-bar seams keep cards put.<br/>"
            "Tile 6: <b>CRYSTAL CLARITY</b> — see every detail, front and back."
        ),
        visual="6 square tiles on black, red accent corner and a line icon per tile (shield · no-PVC · sun · flat page · weld seam · sparkle). Consistent Ultra PRO styling.",
        alt="Six-tile A+ carousel of Platinum Series features: archival, no PVC/acid-free, UV protection, lays flat, super-strong welds, crystal clarity.",
    ),
    AIModule(
        name="Module 4 — Protection banner (feature callouts)",
        role="a+_banner",
        headline="BUILT TO PROTECT YOUR CARDS",
        body=(
            "Solid-bar welds, superior seal strength and archival, acid-free material protect Pokemon, "
            "Magic (MTG), One Piece, Yu-Gi-Oh and sports cards from dust, moisture and everyday wear — "
            "with UV protection to help guard against fading."
        ),
        visual="Banner: one 9-pocket page centered on black with thin white arrow callouts to welds, seal, material and UV. Red top-line and white headline.",
        alt="A+ banner with feature callouts pointing to the welds, seal, archival material and UV protection of a 9-pocket page.",
    ),
    AIModule(
        name="Module 5 — Organize banner (icon stats)",
        role="a+_banner",
        headline="ORGANIZE YOUR COLLECTION",
        body=(
            "The 11-hole punch fits standard 3-ring binders and albums, and one 100-page box stores up to "
            "900 cards — so your whole collection lives in one place, neatly sorted and easy to browse. "
            "Holds up to 18 cards per page, front and back."
        ),
        visual="Banner with two large icon-stat tiles on black: 'FITS STANDARD 3-RING BINDERS' and 'STORES UP TO 900 CARDS', a binder with pages alongside. Red stat icons.",
        alt="A+ banner with icon stats: fits standard 3-ring binders and stores up to 900 cards.",
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
    "trading card sleeves toploader binder album acid free archival uv storage tcg "
    "graded photo memorabilia holder collector display 18 pocket yugioh gathering "
    "11 hole page protectors ccg deck collection organizer"
)


def main() -> None:
    print("Loading Ultra PRO customer + building manual sample brief (no listing.xlsx)…")
    cust = load_customer("ultra_pro")
    brief = ParsedBrief(product_name="Ultra PRO Platinum Series 9-Pocket Pages (100 Pages)", asin="")
    OUT = HERE / "35_UltraPro_9-Pocket-Pages_SAMPLE_Image Plan.pdf"
    real_title_len = len(TITLE.replace("&amp;", "&"))
    print(f"  Product: {brief.product_name}")
    print(f"  Marketplace: {cust.marketplace}  Overlay lang: {cust.overlay_language}")
    print(f"  TITLE real chars (de-escaped): {real_title_len}")

    builder = BriefBuilder(cust, brief, OUT, ai=None)
    builder._ai_title = TITLE
    builder._ai_bullets = BULLETS
    builder._ai_images = IMAGES
    builder._ai_modules = MODULES
    builder._ai_qa = []  # client instruction: no Q&A module
    builder._ai_backend = BACKEND
    builder.copy_source_label = "Hand-written sample (Ultra PRO style)"

    print("Building branded PDF…")
    pdf_path = builder.build()
    size_kb = pdf_path.stat().st_size // 1024
    import re
    pages = len(re.findall(rb'/Type\s*/Page[^s]', pdf_path.read_bytes()))
    print(f"Built: {pdf_path}")
    print(f"  Pages: {pages}  Size: {size_kb} KB")


if __name__ == "__main__":
    main()
