"""Ultra PRO Penny Sleeves (1,000 Count) — Image Plan + A+ (Plan 39).

ASIN B08B9GVG36 · amazon.com · English. Hand-written senior copy in the Ultra PRO
catalog format, built through the EQUALICE brief_app. Self-contained: listing.xlsx
in (parsed for product context), branded PDF out — both live in this product folder.

CREATIVE ANGLE (distinct from the other Ultra PRO SKUs):
  Lead on FIRST-LAYER protection + the huge 1,000-count BULK value. A penny sleeve is
  the everyday first layer for a standard 2.5" x 3.5" card — slide it on, then drop the
  sleeved card into a toploader or deck sleeve. Weave the KW cluster (penny sleeves,
  1000 penny sleeves, penny sleeves for trading cards, pokemon / sports / mtg).

ULTRA PRO STYLE (matched in the art direction of every image):
  black background, bold RED #C8102E top-line + big WHITE headline; thin-arrow feature
  callouts; icon-stat bars; a red circular badge; REAL popular cards (Pokemon, MTG, One
  Piece, sports) shown sleeved; real collector lifestyle; the product box; a dimension
  callout (2.5" x 3.5"); brand close 'Trusted since 1952 · Made in USA'.
  (Image 1 / main image stays on clean white per Amazon policy — no overlay text.)

GUARDRAILS (auto-checked on build, ai=None):
  overlay ≤30 chars AND ≤5 words, smooth (no middots) · overlay_sub ≤90 ·
  module headline ≤38 · bullet head <b>…</b> ≤45 · TITLE ≤200.
COMPLIANCE (deterministic scan): no "#1", no "best", no "leading", no "guaranteed",
  no "prevent", no "$", no URL/.com. Heritage proof as "Trusted since 1952",
  clarity as "clear / crystal-clear", strength as "superior seal / super-strong".

Client instruction (per Jonas, listings 35-50): NO Q&A module, NO Comparison module.
This brief ships 7 images + 6 A+ banners/carousels.
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
PLAN_NO = "39"
ASIN = "B08B9GVG36"


# ===== Customer-facing copy (ENGLISH — amazon.com) =====

# HTML-escaped "&" counts as 1 real char. Keep de-escaped length ≤ 200.
TITLE = (
    "Ultra PRO Penny Sleeves (1,000 Count) — Clear Soft Penny Sleeves for Trading Cards, "
    "Pokemon, MTG &amp; Sports · Standard 2.5\" x 3.5\" · No PVC / Acid-Free · "
    "The First Layer of Card Protection"
)

BULLETS = [
    "<b>THE FIRST LAYER OF PROTECTION</b> — Slide every card into a soft penny sleeve before it "
    "goes into a toploader or deck sleeve. This clear first layer shields the card surface from "
    "dust, dirt and the natural oils from handling, so corners and edges stay clean.",

    "<b>1,000 SLEEVES, BULK VALUE</b> — Each box packs 1,000 penny sleeves, so you can sleeve a "
    "huge bulk collection in one go. Ideal penny sleeves for trading cards — organizing new pulls, "
    "sorting doubles and protecting sports cards, Pokemon and TCG cards in bulk.",

    "<b>STANDARD 2.5\" X 3.5\" FIT</b> — Sized for standard trading cards measuring 2.5 x 3.5 "
    "inches and built to hold cards up to 35 points thick, these soft sleeves slide on smoothly "
    "and fit Pokemon, Magic (MTG), One Piece, Yu-Gi-Oh and sports cards.",

    "<b>ARCHIVAL, ACID-FREE, NO PVC</b> — Made from clear polypropylene film with no PVC, these "
    "acid-free, archival-safe penny sleeves will not yellow or harm your cards — keeping them "
    "safe for long-term storage and everyday handling.",

    "<b>TRUSTED BY COLLECTORS SINCE 1952</b> — Ultra PRO has protected collectibles since 1952. "
    "Clear penny sleeves for trading cards that also work as the first layer for photos and "
    "memorabilia — proudly Made in USA.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (box + sleeves + one sleeved card)",
        role="hero",
        background="Pure white #FFFFFF seamless — Amazon main-image policy (no overlay text, no graphics).",
        purpose="Win the click in the amazon card-supply grid — instantly read as a huge 1,000-count box of clear soft penny sleeves.",
        visual=(
            "Product box (Penny Sleeves, 1,000 Count) standing three-quarter left, label fully legible. "
            "To its right, a small fan of empty clear penny sleeves plus ONE real popular card (a Pokemon "
            "or sports rookie) already inside a sleeve so the soft, glass-clear film reads instantly. "
            "Tight crop, product ~85% of frame, subtle contact shadow, no overlay text."
        ),
        overlay="(no overlay — Amazon main image)",
        overlay_sub="",
        props=["Penny Sleeves 1,000-count box", "fan of empty clear penny sleeves", "one real card sleeved (Pokemon / sports)"],
        lighting="Bright, even studio light; soft rim on the sleeve edge so the clear film and card art pop against white.",
        why_it_works=(
            "The box plus a card already sleeved communicates product type (soft penny sleeves), the big 1,000 "
            "count and clarity in one glance — the three things a collector scans for in the supplies grid."
        ),
        ctr="A recognizable card behind clear film beside a bulk 1,000 box out-signals generic empty-sleeve thumbnails.",
        cvr="Shows exactly what the buyer receives and proves the soft-sleeve fit up front, cutting hesitation.",
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: the first layer (layering concept)",
        role="hook",
        background="Black #111111. Bold RED #C8102E top-line 'START WITH THE FIRST LAYER', big WHITE headline below.",
        purpose="Teach the core role — a penny sleeve is the everyday first layer that goes on before a toploader.",
        visual=(
            "A single standard card shown mid-slide into a clear penny sleeve, then a second frame (thin white "
            "arrow) showing that sleeved card dropping into a toploader. A small red circular badge reads "
            "'EVERYDAY FIRST LAYER'. White headline lower-left; the clear film reads glass-smooth."
        ),
        overlay="THE FIRST LAYER",
        overlay_sub="Sleeve every card first, then add a toploader or deck sleeve.",
        props=["card sliding into a clear penny sleeve", "arrow to sleeved card entering a toploader", "red 'first layer' badge"],
        lighting="Hard raking side-light on black so the clear soft film reads as a smooth protective skin.",
        why_it_works=(
            "Answers the beginner's core question — 'what is a penny sleeve for?' — and positions this box as the "
            "essential base layer every card needs before any harder shell."
        ),
        ctr="The two-step 'sleeve then toploader' visual is a clear pattern interrupt in a grid of flat product shots.",
        cvr="Framing the sleeve as the required first layer makes the 1,000-count box feel like a staple, not an extra.",
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: material feature callouts",
        role="educate",
        background="Black #111111, RED top-line 'MADE TO PROTECT', WHITE headline.",
        purpose="Stack the material feature set as scannable arrow callouts so the buyer trusts the sleeve on their cards.",
        visual=(
            "One clear penny sleeve centered on black holding a card, thin white arrows radiating to labeled "
            "callouts: CLEAR POLYPROPYLENE · NO PVC · ACID-FREE · ARCHIVAL-SAFE · SOFT SLEEVE · HOLDS UP TO 35PT. "
            "Each callout with a small line icon. Red accent underlines under the two headline words."
        ),
        overlay="CLEAR, ACID-FREE, NO PVC",
        overlay_sub="Clear polypropylene, acid-free and archival-safe — will not yellow or harm cards.",
        props=["clear penny sleeve holding a card (hero object)", "6 arrow callouts with line icons", "red accent underlines"],
        lighting="Even soft light on the sleeve, slightly brighter center so the product stays the focal point on black.",
        why_it_works=(
            "Turns spec words into a visual proof stack — no-PVC / acid-free / archival is exactly what a serious "
            "collector filters for and what a bargain sleeve often cannot claim."
        ),
        ctr="A dense, well-organized material callout signals 'safe on my cards' and earns the click from careful buyers.",
        cvr="Each callout removes a specific doubt (PVC, acid, yellowing), compounding trust toward purchase.",
    ),
    AIImagePlanItem(
        name="Image 4 — Desire: sleeve the whole collection (bulk value)",
        role="desire",
        background="Warm collector desk scene; product graphics kept to a slim black/red lower band.",
        purpose="Let the buyer self-cast into sleeving a big bulk collection quickly and calmly with 1,000 on hand.",
        visual=(
            "Over-the-shoulder lifestyle: a collector's hands sleeving a stack of cards at a tidy desk, with an "
            "open 1,000-count box and neat rows of already-sleeved Pokemon and sports cards fanned nearby. Warm, "
            "aspirational, real. Slim black lower band with red top-line 'SLEEVE THEM ALL' and the white headline."
        ),
        overlay="1,000 SLEEVES, BULK VALUE",
        overlay_sub="One box sleeves a huge bulk collection — new pulls, doubles and more.",
        props=["collector's hands sleeving cards", "open 1,000-count box", "rows of sleeved Pokemon & sports cards", "tidy desk"],
        lighting="Warm natural desk light from camera-left, soft and lived-in — hobbyist, not clinical.",
        why_it_works=(
            "Moves from features to the payoff — a whole collection protected in one quick pass — the emotional "
            "reason a collector reaches for a big 1,000-count box."
        ),
        ctr="A relatable bulk-sleeving desk moment stands out against sterile product-only tiles and invites the click.",
        cvr="Buyers picture their own backlog finally sleeved, making the large-count box feel like the smart buy.",
    ),
    AIImagePlanItem(
        name="Image 5 — Trust: soft, snug protection (no scratches, held)",
        role="trust",
        background="Black #111111, RED top-line 'GENTLE ON YOUR CARDS', WHITE headline.",
        purpose="Defuse the fear that a flimsy sleeve scratches, sticks or lets cards slip — this one is soft and snug.",
        visual=(
            "Macro of a card seated in a clear penny sleeve, thin white arrows calling out 'soft, non-abrasive film' "
            "on the surface and 'snug open-top fit' at the mouth. A small red badge 'PROTECTS EVERY CARD'. Optional "
            "cue: a fingertip resting on the sleeve, no marks on the card beneath."
        ),
        overlay="PROTECT EVERY CARD",
        overlay_sub="Soft, non-abrasive film with a snug fit guards surfaces, corners and edges.",
        props=["macro of a card in a clear sleeve", "arrows to soft film and snug open-top fit", "red 'protects every card' badge"],
        lighting="Focused key on the sleeve surface so the smooth, soft film reads as gentle and scratch-free.",
        why_it_works=(
            "Targets the top penny-sleeve review fears (scratching, cloudy film, loose fit). Showing the soft film and "
            "snug seat is concrete proof, not a promise."
        ),
        ctr="The 'gentle on your cards' macro is a reassurance hook that stops careful collectors mid-scroll.",
        cvr="Directly answers 'will it scratch or let my card slip?' with a visible soft-fit proof, removing a blocker.",
    ),
    AIImagePlanItem(
        name="Image 6 — Desire: exact fit + how to layer (dimensions)",
        role="desire",
        background="Black #111111, RED top-line 'A PERFECT STANDARD FIT', WHITE headline; icon-stat bar along the bottom.",
        purpose="Prove exact fit and show the layering ritual so the buyer knows it works for their cards and shells.",
        visual=(
            "A single card ghosted inside a clear penny sleeve with a clean dimension callout '2.5\" x 3.5\"' and "
            "arrows to the sleeve edges, plus a small 'up to 35pt' tag. Beside it, a three-step strip: card → penny "
            "sleeve → toploader. Bottom icon-stat bar: 'STANDARD 2.5\" x 3.5\" CARDS' and '1,000 SLEEVES PER BOX'. "
            "Red accents on the stat icons."
        ),
        overlay="USE UNDER A TOPLOADER",
        overlay_sub="Fits standard 2.5 x 3.5 inch cards, then slides into any toploader.",
        props=["dimension callout 2.5\" x 3.5\"", "card → sleeve → toploader step strip", "two icon-stat tiles"],
        lighting="Clean technical light — flat and legible so the dimensions and stat icons read instantly.",
        why_it_works=(
            "Removes the last practical doubts — 'will it fit my cards and my toploaders?' — with exact numbers and a "
            "clear layering diagram a spec-driven collector trusts."
        ),
        ctr="Concrete numbers (2.5x3.5, up to 35pt, 1,000 per box) signal precision and pull spec-checking buyers.",
        cvr="Exact fit plus the layering strip closes the sizing and compatibility objection and justifies the buy.",
    ),
    AIImagePlanItem(
        name="Image 7 — Close: brand trust (since 1952 · Made in USA)",
        role="close",
        background="Black #111111 with the Ultra PRO logo; subtle red heritage line motif.",
        purpose="Close on brand identity and heritage — the protection collectors have trusted for decades.",
        visual=(
            "Centered Ultra PRO logo on black, a neat spread of sleeved cards and the 1,000-count box softly behind. "
            "RED top-line 'TRUSTED BY COLLECTORS WORLDWIDE', big WHITE headline, and a footer lockup: a small USA-flag "
            "mark with 'Made in USA' beside 'Since 1952'."
        ),
        overlay="TRUSTED SINCE 1952",
        overlay_sub="Protecting collections with USA-made quality since 1952.",
        props=["Ultra PRO logo", "spread of sleeved cards + 1,000-count box", "USA-flag 'Made in USA' mark"],
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
        headline="THE FIRST LAYER OF PROTECTION",
        body=(
            "Penny Sleeves are the everyday first layer for standard trading cards — slide every card in "
            "before it goes into a toploader or deck sleeve. Clear, soft, acid-free and made with no PVC, "
            "with 1,000 sleeves per box so your whole collection gets covered."
        ),
        visual="Wide cinematic banner: 1,000-count box left, a fanned spread of sleeved cards (Pokemon, MTG, One Piece, sports) right, on black with a red accent bar. Ultra PRO logo top-left.",
        alt="Ultra PRO Penny Sleeves 1,000-count box beside a spread of sleeved trading cards on a black background.",
    ),
    AIModule(
        name="Module 2 — Lifestyle banner",
        role="a+_banner",
        headline="PROTECT WHAT MATTERS MOST",
        body=(
            "From your first Pokemon pull to a graded sports rookie, give every card a soft clear first layer "
            "that guards the surface from dust, dirt and the natural oils from handling. Simple, everyday "
            "protection serious collectors reach for every day."
        ),
        visual="Warm lifestyle scene: a collector sleeving cards at a tidy desk, sleeved cards and the open box visible, soft daylight. Slim black/red lower band with the headline.",
        alt="A collector sleeving trading cards into clear penny sleeves at a desk.",
    ),
    AIModule(
        name="Module 3 — Feature carousel (why penny sleeves)",
        role="a+_carousel",
        headline="THE PENNY SLEEVE DIFFERENCE",
        body=(
            "Tile 1: <b>CLEAR POLYPROPYLENE</b> — see every card sharp and true to color.<br/>"
            "Tile 2: <b>NO PVC / ACID-FREE</b> — will not harm or yellow cards.<br/>"
            "Tile 3: <b>ARCHIVAL-SAFE</b> — built for safe long-term storage.<br/>"
            "Tile 4: <b>SOFT SLEEVE</b> — gentle, non-abrasive film that will not scratch.<br/>"
            "Tile 5: <b>HOLDS UP TO 35PT</b> — fits standard cards, even thicker stock.<br/>"
            "Tile 6: <b>1,000 PER BOX</b> — bulk value to sleeve a whole collection."
        ),
        visual="6 square tiles on black, red accent corner and a line icon per tile (sparkle · no-PVC · shield · soft film · caliper · stacked box). Consistent Ultra PRO styling.",
        alt="Six-tile A+ carousel of penny-sleeve features: clear polypropylene, no PVC/acid-free, archival-safe, soft sleeve, holds up to 35pt, 1,000 per box.",
    ),
    AIModule(
        name="Module 4 — How-to banner (layering)",
        role="a+_banner",
        headline="BUILD YOUR PROTECTION IN LAYERS",
        body=(
            "Start with the penny sleeve as your first layer, then add a toploader or deck sleeve for cards you "
            "play, trade, store or ship. The soft clear sleeve keeps the surface clean and lets any harder shell "
            "slide on without scuffing your Pokemon, Magic (MTG), One Piece or sports cards."
        ),
        visual="Banner: a clean three-step strip on black — card → clear penny sleeve → toploader — with thin white arrows and a red top-line. White headline right.",
        alt="A+ banner showing the layering steps: a card into a penny sleeve, then into a toploader.",
    ),
    AIModule(
        name="Module 5 — Bulk / organize banner (icon stats)",
        role="a+_banner",
        headline="SLEEVE YOUR WHOLE COLLECTION",
        body=(
            "One box holds 1,000 penny sleeves sized for standard 2.5 x 3.5 inch cards — enough to sleeve new "
            "pulls, sort your doubles and protect a big bulk collection in a single pass. Keep a stack on the "
            "desk so every card gets its first layer the moment it comes out of the pack."
        ),
        visual="Banner with two large icon-stat tiles on black: 'STANDARD 2.5\" x 3.5\" CARDS' and '1,000 SLEEVES PER BOX', the open box with sleeved cards alongside. Red stat icons.",
        alt="A+ banner with icon stats: fits standard 2.5 x 3.5 inch cards and 1,000 sleeves per box.",
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
        visual="Closing banner: Ultra PRO logo centered on black, sleeved cards and the 1,000-count box softly behind, footer lockup with a USA-flag 'Made in USA' mark and 'Since 1952', a five-star review quote below.",
        alt="Ultra PRO brand-close banner: trusted by collectors worldwide, Made in USA since 1952, with a five-star review quote.",
    ),
]


# ENGLISH backend search terms — stem-deduped, no title/brand duplicates, ≤ 249 bytes.
BACKEND = (
    "toploader deck box protector holder collectible tcg ccg yugioh one piece gathering "
    "baseball football basketball rookie graded lot dust oil scratch storage organizer "
    "sleaves sleves polypropylene 35pt thick perfect fit"
)


def main() -> None:
    print("Loading Ultra PRO customer + parsing penny-sleeves listing…")
    cust = load_customer("ultra_pro")
    brief = parse_excel(EXCEL)
    OUT = HERE / f"{PLAN_NO}_{ASIN}_Image Plan.pdf"
    real_title_len = len(TITLE.replace("&amp;", "&"))
    print(f"  Product: {brief.product_name}  ASIN: {ASIN}  Plan: {PLAN_NO}")
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
