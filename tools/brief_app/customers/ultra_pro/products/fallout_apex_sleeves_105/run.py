"""Ultra PRO FALLOUT 'APEX' Deck Protector Sleeves (105 ct) — Image Plan #49.

Plan 49 · ASIN B0CXJZ4GM4 · amazon.com (English).

A hand-written senior brief for a LICENSED collab SKU. This is the premium APEX
line dressed in OFFICIALLY LICENSED Fallout artwork — so the creative leads on
two things at once: the official Fallout design (the hero collectors buy) and
APEX-grade durability, with archival-safe protection as the support beat.

LANGUAGE SPLIT (the standard):
  • ENGLISH — art-direction / strategy fields the designer reads:
    background, purpose, visual, props, lighting, why_it_works, ctr, cvr,
    and module visual/alt.
  • ENGLISH customer copy (marketplace = amazon.com):
    TITLE, BULLETS, image overlay/overlay_sub, module headline/body, BACKEND.

ULTRA PRO STYLE (matched in the art direction of every image):
  black background, bold RED #C8102E top-line + big WHITE headline; feature
  callouts with thin arrows; icon-stat bars; a red circular badge; REAL cards
  (MTG / Commander decks) sleeved in the product; the pack shown; dimension
  callout (2.5" x 3.5"); brand close 'Trusted since 1952 · Made in USA'. Here the
  official Fallout key art is the visual hero. (Image 1 stays on clean white per
  Amazon policy.)

GUARDRAILS (auto-checked on build):
  overlay ≤30 chars AND ≤5 words, smooth (no middots, no fragments) ·
  overlay_sub ≤90 · module headline ≤38 · bullet head <b>…</b> ≤45 · TITLE ≤200.
COMPLIANCE: no "#1", no "best", no "leading", no "guaranteed", no "prevent",
  no "$", no URL/.com. Strength expressed as "APEX-grade / superior", clarity as
  "crystal-clear", heritage as "Trusted since 1952".

Client instruction (per Jonas, listings 35-50): NO Q&A module and NO Comparison
module. This brief ships 7 images + 6 A+ banners/carousels (a+_banner / a+_carousel only).
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
PLAN_NO = "49"
ASIN = "B0CXJZ4GM4"


# ===== Customer-facing copy (ENGLISH — amazon.com) =====

# HTML-escaped "&" counts as 1 real char. Keep de-escaped length ≤ 200.
TITLE = (
    "Ultra PRO FALLOUT APEX Deck Protector Sleeves (105 Count) — Officially Licensed Fallout "
    "Card Sleeves for MTG &amp; TCG · Standard Size 2.5 x 3.5 in · Archival-Safe · Smooth "
    "Shuffle · Matte or Gloss Finish"
)

BULLETS = [
    "<b>OFFICIALLY LICENSED FALLOUT ARTWORK</b> — Gear up your deck with genuine, officially "
    "licensed Fallout key art printed edge to edge on every sleeve. These fallout sleeves turn "
    "a standard 105-count pack into a themed deck your whole playgroup will notice.",

    "<b>APEX-GRADE DECK PROTECTION</b> — Built on Ultra PRO's premium APEX line, these deck "
    "protector sleeves use a resilient, extra-durable film with a crystal-clear front, so your "
    "cards stay sharp, snug and shielded from dust, scuffs and everyday table wear.",

    "<b>ARCHIVAL-SAFE, NO-PVC MATERIAL</b> — Made with archival-safe polypropylene and no PVC, "
    "these mtg card sleeves are safe for long-term storage — your Commander staples and rare "
    "cards stay protected in the deck box, binder or on the battlefield.",

    "<b>SMOOTH SHUFFLE FORMULATION</b> — A new sleeve formulation is designed for smooth, "
    "consistent shuffling and easy dealing, with a snug fit on standard-size cards (2.5 x 3.5 "
    "inches) so your deck feels great in hand, game after game.",

    "<b>TRUSTED BY COLLECTORS SINCE 1952</b> — 105 sleeves per pack, available in matte or gloss "
    "finish. Ultra PRO has protected cards and collectibles since 1952 — proudly Made in USA and "
    "trusted by TCG players and collectors worldwide.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (pack + fanned Fallout sleeves)",
        role="hero",
        background="Pure white #FFFFFF seamless — Amazon main-image policy (no overlay text, no graphics).",
        purpose="Win the click in the amazon.com card-sleeve grid — instantly read as OFFICIAL Fallout art on premium APEX sleeves.",
        visual=(
            "The 105-count Fallout APEX pack standing three-quarter left, label and Fallout branding fully "
            "legible. To its right, a clean fan of 4-5 loose sleeves showing the official Fallout key art, plus "
            "ONE sleeve holding a real MTG card so the crystal-clear front reads glass-sharp. Tight crop, product "
            "~85% of frame, subtle contact shadow, no overlay text."
        ),
        overlay="(no overlay — Amazon main image)",
        overlay_sub="",
        props=["Fallout APEX 105-count pack", "fanned sleeves showing Fallout art", "one sleeve on a real MTG card"],
        lighting="Bright, even studio light; soft rim on the sleeve edges so the clear film and Fallout art pop against white.",
        why_it_works=(
            "The pack plus fanned official artwork plus a sleeved card communicate the three things a collector "
            "scans for — licensed design, sleeve type and clarity — in a single glance."
        ),
        ctr="Recognizable official Fallout art on the sleeves out-signals generic solid-color sleeve thumbnails and pulls the click.",
        cvr="Shows exactly what the buyer receives (pack + themed sleeves) and proves clarity up front, cutting hesitation.",
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: the official Fallout collab (hero art)",
        role="hook",
        background="Black #111111. Bold RED #C8102E top-line 'OFFICIAL COLLAB', big WHITE headline below.",
        purpose="Lead with the reason collectors buy this SKU — the officially licensed Fallout design, front and center.",
        visual=(
            "Bold beauty shot: three or four sleeves overlapping on black so the Fallout key art fills the frame, "
            "one sleeve carrying a real MTG card behind the glass-clear front. A red circular badge top-right reads "
            "'OFFICIALLY LICENSED'. Thin white arrow tags the crisp printed art edge. White headline lower-left."
        ),
        overlay="OFFICIAL FALLOUT SLEEVES.",
        overlay_sub="Officially licensed Fallout key art printed on every deck protector sleeve.",
        props=["overlapping Fallout-art sleeves", "one sleeve on a real MTG card", "red 'officially licensed' badge"],
        lighting="Hard raking side-light on black to make the printed art rich and the clear front read as glass.",
        why_it_works=(
            "Answers the collector's first question — 'is this the real, official Fallout design?' — with a "
            "bold licensed hero shot that also proves the front stays crystal-clear over a card."
        ),
        ctr="A full-frame official Fallout artwork on black is a pattern interrupt in a grid of plain sleeve packs.",
        cvr="Confirming the licensed design and the clear front up front removes the two biggest doubts before the click.",
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: APEX-grade durability + archival material",
        role="educate",
        background="Black #111111, RED top-line 'THE APEX LINE', WHITE headline.",
        purpose="Stack the premium APEX build the cheap themed sleeve can't match, as scannable arrow callouts.",
        visual=(
            "One Fallout sleeve centered on black, thin white arrows radiating to labeled callouts: "
            "EXTRA-DURABLE FILM · CRYSTAL-CLEAR FRONT · ARCHIVAL-SAFE · NO PVC · SNUG FIT · SMOOTH SHUFFLE. "
            "Each callout with a small line icon. Red accent underline under the headline."
        ),
        overlay="APEX-GRADE PROTECTION.",
        overlay_sub="Premium APEX film: extra-durable, archival-safe, no PVC and crystal-clear.",
        props=["single Fallout sleeve (hero object)", "6 arrow callouts with line icons", "red accent underline"],
        lighting="Even soft light on the sleeve, slightly brighter center so the product stays the focal point on black.",
        why_it_works=(
            "Turns spec words into a visual proof stack — extra-durable + archival + no-PVC is exactly what a "
            "serious deck-builder filters for and what a bargain themed sleeve cannot claim."
        ),
        ctr="A dense, well-organized feature stack signals 'premium protection' and earns the click from competitive players.",
        cvr="Each callout removes a specific doubt (durability, PVC, fit, shuffle), compounding trust toward purchase.",
    ),
    AIImagePlanItem(
        name="Image 4 — Desire: game night with a fully sleeved deck (lifestyle)",
        role="desire",
        background="Warm game-table scene; product graphics kept to a slim black/red lower band.",
        purpose="Let the buyer self-cast into a proud, table-ready Fallout deck at their next Commander night.",
        visual=(
            "Over-the-shoulder lifestyle: a player's hands shuffle a fully sleeved MTG Commander deck at a warm, "
            "lived-in game table, more Fallout-art sleeves and a deck box nearby. Aspirational and real. Slim black "
            "lower band with red top-line 'GAME READY' and the white headline."
        ),
        overlay="GEAR UP YOUR DECK.",
        overlay_sub="Bring an officially licensed Fallout deck to your next game night.",
        props=["player's hands shuffling", "fully sleeved Commander deck", "Fallout-art sleeves", "deck box", "game table"],
        lighting="Warm natural table light from camera-left, soft and lived-in — hobbyist, not clinical.",
        why_it_works=(
            "Moves from features to the emotional payoff — a themed deck the whole playgroup notices — which is "
            "what turns a browsing player into a buyer."
        ),
        ctr="A relatable game-night moment stands out against sterile product-only tiles and invites the click.",
        cvr="Buyers picture their own deck sleeved in Fallout art, making the purchase feel like the next step.",
    ),
    AIImagePlanItem(
        name="Image 5 — Trust: smooth shuffle & snug fit (macro)",
        role="trust",
        background="Black #111111, RED top-line 'NEW FORMULATION', WHITE headline.",
        purpose="Defuse the top sleeve fears — poor shuffle feel and loose fit — with a construction proof macro.",
        visual=(
            "Macro of a card sliding cleanly into a sleeve, the mouth snug on a standard card. Thin white arrows call "
            "out 'smooth-shuffle finish' along the face and 'snug 2.5\" x 3.5\" fit' at the opening. A small red badge "
            "'SMOOTH SHUFFLE'. A soft riffle of a few sleeves cues easy dealing."
        ),
        overlay="SMOOTH, SOLID SHUFFLE.",
        overlay_sub="New formulation shuffles smoothly with a snug fit on standard cards.",
        props=["macro of card entering sleeve", "arrows to finish and snug mouth", "red 'smooth shuffle' badge"],
        lighting="Focused key on the sleeve face and mouth so the finish and snug fit read clearly on black.",
        why_it_works=(
            "Targets the two most common sleeve complaints (clumpy shuffle, loose or tight fit) with a concrete "
            "macro rather than a promise — reassuring competitive players who shuffle every turn."
        ),
        ctr="The clean card-into-sleeve macro is a satisfying curiosity hook that stops the scroll.",
        cvr="Directly answers 'will it shuffle well and fit right?' with visible proof, removing a purchase blocker.",
    ),
    AIImagePlanItem(
        name="Image 6 — Desire: matte or gloss finish & 105-count (specs)",
        role="desire",
        background="Black #111111, RED top-line 'YOUR FINISH', WHITE headline; icon-stat bar along the bottom.",
        purpose="Prove finish choice and pack size so the buyer knows it fits their deck and their preference.",
        visual=(
            "Split beauty shot: the same Fallout sleeve shown MATTE on the left (soft, glare-free) and GLOSS on the "
            "right (bright, reflective), a card ghosted behind each. Clean dimension callout '2.5\" x 3.5\"'. Bottom "
            "icon-stat bar with two tiles: '105 SLEEVES PER PACK' and 'FITS STANDARD SIZE CARDS'. Red stat icons."
        ),
        overlay="MATTE OR GLOSS FINISH.",
        overlay_sub="Choose matte or gloss — 105 sleeves per pack for standard-size cards.",
        props=["matte vs gloss split of the sleeve", "dimension callout 2.5\" x 3.5\"", "two icon-stat tiles"],
        lighting="Clean technical light — a soft, glare-free key on the matte half and a brighter reflective key on the gloss half.",
        why_it_works=(
            "Removes the last practical doubts — 'which finish, what size, how many?' — with an at-a-glance "
            "matte-vs-gloss comparison and exact numbers a spec-driven player trusts."
        ),
        ctr="Concrete choices (matte vs gloss, 105 count, standard size) signal precision and pull spec-checking buyers.",
        cvr="Finish choice plus exact count and fit close the last objections and justify the buy.",
    ),
    AIImagePlanItem(
        name="Image 7 — Close: brand trust (since 1952 · Made in USA)",
        role="close",
        background="Black #111111 with the Ultra PRO logo; subtle red heritage line motif.",
        purpose="Close on brand identity and heritage — the protection collectors and players have trusted for decades.",
        visual=(
            "Centered Ultra PRO logo on black, a neat row of Fallout-sleeved decks and a deck box softly behind. RED "
            "top-line 'TRUSTED BY COLLECTORS WORLDWIDE', big WHITE headline, and a footer lockup: a small USA-flag "
            "mark with 'Made in USA' beside 'Since 1952'."
        ),
        overlay="PROTECTED SINCE 1952.",
        overlay_sub="Ultra PRO has protected cards with USA-made quality since 1952.",
        props=["Ultra PRO logo", "row of Fallout-sleeved decks", "deck box", "USA-flag 'Made in USA' mark"],
        lighting="Premium low-key light, soft glow on the logo — authoritative, heritage, category-anchor feel.",
        why_it_works=(
            "Ends on heritage and provenance — the trust cue that converts a hesitating buyer who wants a brand "
            "that will still be here to protect the collection and decks they are building."
        ),
        ctr="The heritage 'since 1952 · Made in USA' lockup signals category authority and reassures at a glance.",
        cvr="Provenance and longevity provide the final trust nudge that seals the purchase.",
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Brand banner (Fallout collab hero)",
        role="a+_banner",
        headline="OFFICIAL FALLOUT DECK SLEEVES",
        body=(
            "The premium Ultra PRO APEX line, dressed in officially licensed Fallout key art. 105 deck "
            "protector sleeves with a crystal-clear front and extra-durable, archival-safe film — gear up "
            "your MTG and TCG decks with a design collectors and players instantly recognize."
        ),
        visual="Wide cinematic banner: the 105-count Fallout pack left, a fanned spread of Fallout-art sleeves right (one on a real MTG card), on black with a red accent bar. Ultra PRO logo top-left.",
        alt="Ultra PRO Fallout APEX pack beside a fan of officially licensed Fallout deck protector sleeves on a black background.",
    ),
    AIModule(
        name="Module 2 — Feature carousel (the APEX set)",
        role="a+_carousel",
        headline="THE APEX DIFFERENCE",
        body=(
            "Tile 1: <b>OFFICIAL FALLOUT ART</b> — officially licensed key art on every sleeve.<br/>"
            "Tile 2: <b>EXTRA-DURABLE FILM</b> — premium APEX build shields cards from wear.<br/>"
            "Tile 3: <b>CRYSTAL-CLEAR FRONT</b> — see your card sharp and true through the front.<br/>"
            "Tile 4: <b>ARCHIVAL-SAFE, NO PVC</b> — safe polypropylene for long-term storage.<br/>"
            "Tile 5: <b>SMOOTH SHUFFLE</b> — new formulation shuffles and deals smoothly.<br/>"
            "Tile 6: <b>SNUG STANDARD FIT</b> — sized for 2.5 x 3.5 in standard cards."
        ),
        visual="6 square tiles on black, red accent corner and a line icon per tile (Fallout art · shield · sparkle · no-PVC · shuffle swirl · card fit). Consistent Ultra PRO styling.",
        alt="Six-tile A+ carousel of Fallout APEX features: official art, durable film, clear front, archival no-PVC, smooth shuffle, snug standard fit.",
    ),
    AIModule(
        name="Module 3 — Licensed-art banner",
        role="a+_banner",
        headline="OFFICIALLY LICENSED ARTWORK",
        body=(
            "Every sleeve carries genuine, officially licensed Fallout key art printed edge to edge — no "
            "generic prints, no fakes. Turn a standard 105-count pack into a fully themed deck that stands "
            "out on the table and in your collection."
        ),
        visual="Banner: three or four Fallout-art sleeves overlapping to fill the frame on black, one on a real MTG card, a red 'officially licensed' badge, red top-line and white headline.",
        alt="A+ banner showing officially licensed Fallout key art across overlapping Ultra PRO APEX sleeves.",
    ),
    AIModule(
        name="Module 4 — Protection banner (feature callouts)",
        role="a+_banner",
        headline="BUILT TO PROTECT YOUR DECK",
        body=(
            "Extra-durable APEX film, a crystal-clear front and archival-safe, no-PVC material protect your "
            "MTG, Commander and TCG cards from dust, moisture, scuffs and everyday table wear — while the snug "
            "standard fit keeps every card secure edge to edge."
        ),
        visual="Banner: one Fallout sleeve centered on black with thin white arrow callouts to the durable film, clear front, archival material and snug mouth. Red top-line and white headline.",
        alt="A+ banner with feature callouts pointing to the durable film, clear front, archival material and snug fit of a Fallout APEX sleeve.",
    ),
    AIModule(
        name="Module 5 — Game-ready banner (icon stats)",
        role="a+_banner",
        headline="MADE FOR YOUR GAME",
        body=(
            "105 sleeves per pack, sized for standard 2.5 x 3.5 in cards and available in matte or gloss "
            "finish — enough to sleeve a full Commander deck with spares, so your whole deck is protected and "
            "ready for game night, tournaments and everyday play."
        ),
        visual="Banner with two large icon-stat tiles on black: '105 SLEEVES PER PACK' and 'FITS STANDARD SIZE CARDS', a sleeved Commander deck and deck box alongside. Red stat icons.",
        alt="A+ banner with icon stats: 105 sleeves per pack and fits standard-size cards, beside a sleeved deck.",
    ),
    AIModule(
        name="Module 6 — Brand close (heritage + review)",
        role="a+_banner",
        headline="TRUSTED SINCE 1952",
        body=(
            "Collectors and players worldwide trust Ultra PRO for card protection — proudly Made in USA since "
            "1952. <br/><br/>“Crystal clear and durable, my cards are well-protected.” "
            "&#9733;&#9733;&#9733;&#9733;&#9733;"
        ),
        visual="Closing banner: Ultra PRO logo centered on black, Fallout-sleeved decks softly behind, footer lockup with a USA-flag 'Made in USA' mark and 'Since 1952', a five-star review quote below.",
        alt="Ultra PRO brand-close banner: trusted by collectors worldwide, Made in USA since 1952, with a five-star review quote.",
    ),
]


# ENGLISH backend search terms — stem-deduped, no title/brand duplicates, ≤ 249 bytes.
BACKEND = (
    "commander deck sleeves matte gloss polypropylene tcg ccg gaming yugioh pokemon "
    "colored black bulk 105 count katana outer inner deckbox protectors themed collab "
    "licensed collectible shuffle snug fit game night tournament"
)


def main() -> None:
    print("Loading Ultra PRO customer + parsing Fallout APEX listing…")
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
    builder._ai_qa = []       # client instruction (35-50): no Q&A module
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
