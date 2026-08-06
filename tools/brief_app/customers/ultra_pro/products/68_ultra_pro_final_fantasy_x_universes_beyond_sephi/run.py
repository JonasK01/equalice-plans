"""Ultra PRO — MTG Playmat, FINAL FANTASY x Universes Beyond (Double-Sided)  [Listing 68]
NEUES Format: Titel/Bullets/Backend kommen aus dem SEO-Sheet (listing.xlsx),
Q&A + Vergleich aus dem A+ Premium Sheet (aplus.xlsx). Bildregie handgeschrieben,
100% produktspezifisch, im Ultra-PRO-Katalogstil (schwarz/rot/weiss) — Lizenz-Art
darf farbig dominieren.

Produkt: LIZENZIERTE, BEIDSEITIGE Spielmatte (Playmat) für Magic: The Gathering.
Kein Sleeve/Bag. HERO = offiziell lizenzierte FINAL-FANTASY-Art (Clive, Ifrit's
Dominant / Ifrit, Warden of Inferno), beide Seiten, weiche Stoffoberfläche, 24 x 13.5 in.

Marketplace: amazon.com (US). ASIN B0F5YF2NXQ.
"""
from __future__ import annotations
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(HERE.parents[1]))   # customers/ultra_pro  (für seo_loader)

from tools.brief_app.core.customers import load_customer
from tools.brief_app.core.excel_parser import parse_excel
from tools.brief_app.core.pdf_builder import BriefBuilder
from tools.brief_app.core.ai import AIImagePlanItem, AIModule
import seo_loader as SEOL

PLAN_NO = "68"
ASIN = "B0F5YF2NXQ"
EXCEL = HERE / "listing.xlsx"
APLUS = HERE / "aplus.xlsx"


# ===== produktspezifische Bildregie (Ultra-PRO-Katalogstil, EN Overlays) =====

IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="Clean white for slot-1 compliance; the CTR versions add a thin red top-line and a slim black lower band (Ultra PRO catalog look). Same framing across all 3.",
        purpose="Win the click in a grid of look-alike playmats. Lead with the officially licensed FINAL FANTASY art — that is the reason to stop the scroll. Ship all 3, keep the winner.",
        visual=(
            "Mock ALL 3 options. Product exactly as real: a soft-fabric Magic: The Gathering "
            "playmat, laid flat, showing the full-colour licensed FINAL FANTASY artwork. ONE "
            "callout each, artwork dominant, mat filling the frame.\n\n"
            "OPTION A — LICENSED ART: the Clive, Ifrit's Dominant side laid flat, art crisp and "
            "full-colour edge to edge. Badge (red): 'OFFICIALLY LICENSED'.\n"
            "OPTION B — DOUBLE-SIDED: the two art sides shown as a subtle flip (Clive front, Ifrit "
            "back peeking). Badge (red): 'DOUBLE-SIDED'.\n"
            "OPTION C — SIZE: mat with a clean dimension callout. Badge (red): '24\" x 13.5\"'.\n\n"
            "Across all 3: white background, red badge ~6% of frame, same lighting; licensed art "
            "carries the colour, chrome stays black/red/white."
        ),
        overlay="(one callout per option)",
        overlay_sub="3 hero options shipped — A/B test, keep the winner.",
        props=["A: Clive, Ifrit's Dominant art side (flat)", "B: both art sides in a flip", "C: mat with 24 x 13.5 in dimension callout"],
        lighting="Bright, even studio light; soft catch-light so the fabric texture and full-colour art read on white.",
        why_it_works=(
            "Three triggers: the officially licensed art (the fan-buy reason), double-sided value, "
            "and clear size. One callout each — readable at thumbnail size."
        ),
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: officially licensed FINAL FANTASY art",
        role="hook",
        background="Black with a thin red top-line and a bold white headline (Ultra PRO catalog)",
        purpose="Own the #1 reason a fan buys this mat: the officially licensed Magic x FINAL FANTASY artwork.",
        visual=(
            "Large hero of the playmat laid flat, the Clive, Ifrit's Dominant artwork sharp and "
            "full-colour across the whole soft-fabric surface. Thin red callout lines: 'Officially "
            "Licensed', 'Magic: The Gathering — FINAL FANTASY', 'full-colour, edge to edge'. White "
            "bold headline top: 'PLAY THE ART.' A small official-licensing lockup sits bottom-right."
        ),
        overlay="OFFICIALLY LICENSED ART.",
        overlay_sub="Magic: The Gathering — FINAL FANTASY artwork, full-colour across the whole mat.",
        props=["playmat flat (hero)", "licensed FINAL FANTASY art edge to edge", "red callout lines", "official-licensing lockup"],
        lighting="Dramatic catalog light on black; strong edge-light so the fabric and colour art pop.",
        why_it_works=(
            "Licensed-art buyers choose with their eyes. A full-frame, true-colour hero of the "
            "actual artwork is the single strongest argument in the fan-mat category."
        ),
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: double-sided, two heroes",
        role="educate",
        background="White with a black/red Ultra PRO footer band",
        purpose="Explain the double-sided value — one mat, two full-colour art sides to display.",
        visual=(
            "Split card. LEFT: the Clive, Ifrit's Dominant side flat, small tag 'SIDE A'. RIGHT: the "
            "Ifrit, Warden of Inferno side flat, small tag 'SIDE B'. A red flip-arrow between them. "
            "Three feature rows with red check-icons: 'Full-colour artwork on both sides', 'Flip to "
            "switch the look', 'Two hero scenes, one mat'. Footer band: 'Officially licensed — "
            "trusted since 1952.'"
        ),
        overlay="TWO SIDES. TWO HEROES.",
        overlay_sub="Full-colour art on both sides — flip to switch between Clive and Ifrit.",
        props=["Side A: Clive, Ifrit's Dominant", "Side B: Ifrit, Warden of Inferno", "red flip-arrow", "3 feature rows with red checks"],
        lighting="Flat, even catalog light; both art sides equally lit so neither reads as the 'back'.",
        why_it_works=(
            "Double-sided is the hidden value most listings bury. Showing both hero scenes side by "
            "side doubles the perceived worth and answers 'what's on the other side?' instantly."
        ),
    ),
    AIImagePlanItem(
        name="Image 4 — Desire: soft fabric play surface protects cards",
        role="desire",
        background="White with a red macro callout (Ultra PRO)",
        purpose="Sell the play experience — a smooth soft-fabric surface that protects cards in play.",
        visual=(
            "Close macro of cards being played on the mat: a card sliding across the soft-fabric "
            "surface, easy to pick up. Red callout lines: 'soft fabric surface', 'smooth card "
            "handling', 'helps protect cards & sleeves in play'. A small texture inset shows the "
            "woven fabric top. Note: 'Lies flat for a clean, stable playing area.'"
        ),
        overlay="SOFT FABRIC PLAY SURFACE.",
        overlay_sub="Smooth soft-fabric top for easy card handling that helps protect cards in play.",
        props=["cards on the mat (macro)", "card sliding / easy pick-up", "woven fabric texture inset", "red callout lines"],
        lighting="Bright, even; raking light on the fabric so the soft texture is unmistakable.",
        why_it_works=(
            "Beyond the art, players want a mat that plays well. Showing smooth handling and card "
            "protection turns a display piece into a gameplay upgrade worth buying."
        ),
    ),
    AIImagePlanItem(
        name="Image 5 — Desire: gameplay-ready size, lies flat",
        role="desire",
        background="Black with red accents (Ultra PRO catalog)",
        purpose="Remove the size question and show the mat working on a real table.",
        visual=(
            "The mat on a tabletop set for play: cards, tokens and dice laid out with room to spare. "
            "Clean dimension callout: 'Approx. 24\" x 13.5\"'. Icon-stats: 'Room for board & hand', "
            "'Lies flat — no curl', 'Also great as an oversized desk mat / mousepad'. Catalog-style "
            "layout."
        ),
        overlay="GAMEPLAY-READY SIZE.",
        overlay_sub="Approx. 24 x 13.5 in — room for cards, tokens and accessories; lies flat.",
        props=["mat on tabletop", "cards, tokens, dice laid out", "24 x 13.5 in dimension callout", "3 icon-stats"],
        lighting="Catalog light on black; product and stats clearly separated, no clutter.",
        why_it_works=(
            "Size is the top pre-purchase question for mats. A real play scene plus a precise "
            "dimension callout sets honest expectations and shows day-one usefulness."
        ),
    ),
    AIImagePlanItem(
        name="Image 6 — Trust: Ultra PRO, trusted since 1952",
        role="trust",
        background="Black with red top-line, white headline (brand close)",
        purpose="Close on brand authority — the players' and collectors' default accessory brand.",
        visual=(
            "Hero of the rolled and flat mat together, with a small lifestyle inset (a player "
            "setting up the mat at a tidy game table). Brand line bottom: 'ULTRA PRO — reliable "
            "gaming accessories since 1952 · trusted by players & collectors worldwide'. Red badge: "
            "'SINCE 1952'."
        ),
        overlay="TRUSTED SINCE 1952.",
        overlay_sub="Ultra PRO — reliable gaming accessories for players and collectors worldwide.",
        props=["mat rolled + flat", "player lifestyle inset", "since-1952 red badge"],
        lighting="Premium catalog light on black; warm inset for the lifestyle moment.",
        why_it_works=(
            "Against generic third-party mats, heritage and trust are the deciding signals. 'Since "
            "1952' is Ultra PRO's honest, compliant authority claim."
        ),
    ),
    AIImagePlanItem(
        name="Image 7 — Close: build your Ultra PRO MTG setup",
        role="close",
        background="White with black/red Ultra PRO chrome",
        purpose="Cross-sell the wider Ultra PRO gameplay range.",
        visual=(
            "Clean line-up: this FINAL FANTASY playmat (highlighted) alongside matching deck "
            "protector sleeves, a deck box and a playmat tube/bag — shown as a coordinated setup. "
            "Small labels; the mat gently highlighted. Caption: 'Sleeve it. Store it. Play on it. — "
            "the Ultra PRO way.'"
        ),
        overlay="BUILD YOUR MTG SETUP.",
        overlay_sub="Pair the mat with Ultra PRO sleeves, deck boxes and playmat storage.",
        props=["FINAL FANTASY playmat (highlighted)", "deck protector sleeves", "deck box", "playmat tube/bag"],
        lighting="Bright, even; coordinated family shot.",
        why_it_works=(
            "Turns one purchase into a setup sale and reinforces Ultra PRO as the one-stop brand for "
            "Magic players."
        ),
    ),
]


# ===== 4 kreative Module + Q&A/Vergleich aus dem A+ Sheet =====

CREATIVE_MODULES = [
    AIModule(
        name="Module 1 — Brand banner",
        role="a+_banner",
        headline="PLAY THE ART. SINCE 1952.",
        body=(
            "An officially licensed Magic: The Gathering — FINAL FANTASY playmat with "
            "full-colour artwork on both sides — Clive, Ifrit’s Dominant on one, Ifrit, "
            "Warden of Inferno on the other. A soft-fabric surface gives smooth card handling and "
            "helps protect cards in play. Reliable gaming accessories, trusted since 1952."
        ),
        visual="Wide black banner, red top-line, bold white headline left; the flat playmat showing full-colour licensed art right. Ultra PRO logo upper-left, official-licensing lockup lower-right.",
        alt="Ultra PRO MTG FINAL FANTASY playmat banner: officially licensed, double-sided, soft fabric, since 1952.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): Why this playmat",
        role="a+_carousel",
        headline="WHY THIS ULTRA PRO PLAYMAT",
        body=(
            "Tile 1: <b>OFFICIALLY LICENSED</b> — Magic: The Gathering — FINAL FANTASY artwork.<br/>"
            "Tile 2: <b>DOUBLE-SIDED</b> — Full-colour art on both sides, flip to switch.<br/>"
            "Tile 3: <b>SOFT FABRIC SURFACE</b> — Smooth handling that helps protect cards.<br/>"
            "Tile 4: <b>24\" x 13.5\" SIZE</b> — Room for board, hand and accessories.<br/>"
            "Tile 5: <b>SINCE 1952</b> — Reliable gaming accessories worldwide."
        ),
        visual="5 square tiles, red accent corner each, black/white icons (license lockup · flip · fabric · ruler · badge); licensed art carries the colour.",
        alt="Five A+ tiles: officially licensed, double-sided, soft fabric, 24 x 13.5 in, since 1952.",
    ),
    AIModule(
        name="Module 3 — Banner: double-sided artwork",
        role="a+_banner",
        headline="TWO SIDES. TWO HEROES.",
        body=(
            "One mat, two full-colour scenes. Display Clive, Ifrit’s Dominant for one look, "
            "then flip to Ifrit, Warden of Inferno for another. Officially licensed artwork on a "
            "soft-fabric surface that lies flat for a clean, stable playing area."
        ),
        visual="Banner split: Clive side flat left, Ifrit side flat right, a red flip-arrow between; small 'SIDE A / SIDE B' tags. Black/red Ultra PRO styling.",
        alt="A+ banner showing the double-sided FINAL FANTASY playmat: Clive on one side, Ifrit on the other.",
    ),
    AIModule(
        name="Module 4 — Carousel (4 tiles): Build your Ultra PRO setup",
        role="a+_carousel",
        headline="SLEEVE IT. STORE IT. PLAY ON IT.",
        body=(
            "Tile 1: <b>PLAYMAT</b> — This double-sided FINAL FANTASY mat (this product).<br/>"
            "Tile 2: <b>DECK PROTECTOR SLEEVES</b> — Keep your cards clean in play.<br/>"
            "Tile 3: <b>DECK BOXES</b> — Carry and protect your deck.<br/>"
            "Tile 4: <b>PLAYMAT STORAGE</b> — Roll, tube and travel with your mat."
        ),
        visual="4 coordinated product tiles, red accent corners, consistent Ultra PRO catalog styling.",
        alt="Four A+ tiles showing the Ultra PRO Magic setup: playmat, sleeves, deck boxes, playmat storage.",
    ),
]


def main() -> None:
    print(f"Lade Ultra PRO + SEO/A+ Sheets für Listing {PLAN_NO}…")
    cust = load_customer("ultra_pro")
    brief = parse_excel(EXCEL)
    seo = SEOL.load_seo(EXCEL)
    ap = SEOL.load_aplus(APLUS)
    OUT = HERE / f"{PLAN_NO}_{ASIN}_Image Plan.pdf"
    print(f"  SEO-Titel ({len(seo.title)} chars): {seo.title[:70]}…")
    print(f"  Bullets={len(seo.bullets)}  Q&A={len(ap.qa)}  Vergleich-Zeilen={len(ap.comp_rows)}")

    modules = list(CREATIVE_MODULES)
    if ap.qa:
        modules.append(SEOL.qa_module(ap, headline="PLAYER Q&A"))
    if ap.comp_rows:
        modules.append(SEOL.comparison_module(ap))

    builder = BriefBuilder(cust, brief, OUT, ai=None)
    builder._ai_title = seo.title                       # SEO-Titel 1:1 (wird ge-esc't)
    builder._ai_bullets = SEOL.as_bullets_html(seo)     # SEO-Bullets -> Haus-Stil
    builder._ai_images = IMAGES
    builder._ai_modules = modules
    builder._ai_qa = SEOL.as_qa(ap)
    builder._ai_backend = seo.backend
    builder.copy_source_label = "SEO-Sheet (Titel/Bullets/Backend) + A+ Sheet (Q&A/Vergleich); Bildregie hand-written"

    print("Baue Branded PDF…")
    pdf_path = builder.build()
    size_kb = pdf_path.stat().st_size // 1024
    import re
    pages = len(re.findall(rb'/Type\s*/Page[^s]', pdf_path.read_bytes()))
    print(f"Gebaut: {pdf_path}")
    print(f"  Seiten: {pages}  Größe: {size_kb} KB")


if __name__ == "__main__":
    main()
