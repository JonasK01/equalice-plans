"""Ultra PRO — MTG Playmat, Final Fantasy x Universes Beyond 'Lightning, Army of One'  [Listing 65]
NEUES Format: Titel/Bullets/Backend kommen aus dem SEO-Sheet (listing.xlsx),
Q&A + Vergleich aus dem A+ Premium Sheet (aplus.xlsx). Bildregie handgeschrieben,
100% produktspezifisch, im Ultra-PRO-Katalogstil (schwarz/rot/weiss). Die
lizenzierte Lightning-Artwork darf farbig dominieren.

Marketplace: amazon.com (US). ASIN B0F5YJCQKJ.
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

PLAN_NO = "65"
ASIN = "B0F5YJCQKJ"
EXCEL = HERE / "listing.xlsx"
APLUS = HERE / "aplus.xlsx"


# ===== produktspezifische Bildregie (Ultra-PRO-Katalogstil, EN Overlays) =====

IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="Clean white for slot-1 compliance; the CTR versions add a thin black band with a red top-line (Ultra PRO catalog look). Same framing across all 3.",
        purpose="Win the click in a grid of look-alike playmats. Lead with the licensed Lightning artwork, ship all 3, keep the winner.",
        visual=(
            "Mock ALL 3 options. Product exactly as real: the full 24 x 13.5 in playmat laid flat, "
            "top-down, the licensed 'Lightning, Army of One' artwork filling the mat in full colour, "
            "black stitched edges crisp all around. ONE callout each, artwork dominant.\n\n"
            "OPTION A — LICENSED ART: pure top-down of the full mat, artwork edge-to-edge. Badge "
            "(red): 'OFFICIALLY LICENSED'.\n"
            "OPTION B — SIZE: same mat with a slim dimension callout '24\" x 13.5\"' along two edges. "
            "Badge (red): '24 x 13.5 IN'.\n"
            "OPTION C — STITCHED EDGE: three-quarter angle with a tight macro inset of the black "
            "stitched border. Badge (red): 'STITCHED EDGES'.\n\n"
            "Across all 3: white background, red badge ~6% of frame, Lightning artwork in full colour, same lighting."
        ),
        overlay="(one callout per option)",
        overlay_sub="3 hero options shipped — A/B test, keep the winner.",
        props=["A: full mat, licensed artwork edge-to-edge", "B: mat with 24x13.5 in dimension callout", "C: angle + stitched-edge macro inset"],
        lighting="Bright, even studio light; soft catch-light so the fabric weave and stitched edge read on white.",
        why_it_works=(
            "Three triggers: the licensed Lightning art (the reason to buy), the size, and the "
            "stitched-edge quality. One callout each — readable at thumbnail size."
        ),
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: Officially licensed Lightning artwork",
        role="hook",
        background="Black with a thin red top-line and a bold white headline (Ultra PRO catalog)",
        purpose="Own the #1 reason collectors buy this mat: the licensed Final Fantasy x MTG Lightning art.",
        visual=(
            "Large hero of the full mat at a slight three-quarter angle, the 'Lightning, Army of One' "
            "artwork by Isamu Kamikokuryo rich and true-colour across the fabric surface. Thin red "
            "callout lines: 'Magic: The Gathering x FINAL FANTASY', 'Lightning, Army of One', "
            "'art by Isamu Kamikokuryo'. White bold headline top: 'PLAY ON THE ART.'"
        ),
        overlay="OFFICIALLY LICENSED ART.",
        overlay_sub="Magic: The Gathering x FINAL FANTASY Lightning, Army of One artwork.",
        props=["full mat at three-quarter angle", "red callout lines", "true-colour Lightning artwork"],
        lighting="Dramatic catalog light on black; the artwork colours pop against the dark frame.",
        why_it_works=(
            "Licensed crossover art is the whole purchase decision here. A true-colour hero of the "
            "Lightning artwork is the single strongest visual argument in the category."
        ),
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: Soft fabric top protects cards",
        role="educate",
        background="White with a black/red Ultra PRO footer band",
        purpose="Defend quality: why the soft fabric surface matters for shuffling and card care.",
        visual=(
            "Split card. LEFT: a macro of the fabric surface with a card mid-slide and a small shield "
            "icon 'CARD-SAFE'. RIGHT: three stacked feature rows with red check-icons — 'SOFT FABRIC "
            "TOP (smooth handling)', 'CUSHIONS &amp; PICK-UP (easy to lift cards)', 'HELPS REDUCE WEAR "
            "during play'. Footer band: 'Time-tested gaming accessories — trusted since 1952.'"
        ),
        overlay="SOFT FABRIC TOP.",
        overlay_sub="Smooth surface for card handling and shuffling — helps reduce card wear.",
        props=["macro of fabric top + card mid-slide", "3 feature rows with red checks", "since-1952 footer band"],
        lighting="Flat, even catalog light; the fabric weave and icons legible at thumbnail size.",
        why_it_works=(
            "Players filter on surface feel. Showing the fabric top with a clear 'why it matters' "
            "separates this from thin, slick bargain mats."
        ),
    ),
    AIImagePlanItem(
        name="Image 4 — Trust: Black stitched edges",
        role="desire",
        background="White with a red macro callout (Ultra PRO)",
        purpose="Show the premium build detail buyers look for — sewn edges that will not fray.",
        visual=(
            "Tight macro of one corner: the black stitched edge framing the artwork, thread and hem "
            "sharp. Clean callout: 'Black stitched edges frame the art and resist fraying'. A small "
            "note: 'Refined, premium feel — built to last through match after match.'"
        ),
        overlay="BLACK STITCHED EDGES.",
        overlay_sub="Sewn edges frame the artwork, resist fraying and add a premium feel.",
        props=["corner macro of stitched edge", "thread/hem detail", "red callout line"],
        lighting="Bright, even; strong macro light so individual stitches read clearly.",
        why_it_works=(
            "Frayed, glued edges are the top complaint on cheap mats. A macro of real stitching "
            "proves durable construction and justifies the price."
        ),
    ),
    AIImagePlanItem(
        name="Image 5 — Desire: Non-slip rubber backing + size",
        role="desire",
        background="Black with red accents (Ultra PRO catalog)",
        purpose="Prove the mat stays put and lies flat at true tabletop size.",
        visual=(
            "The mat flipped to show the natural-rubber underside, plus a small top-down inset of the "
            "full playing area with cards in play. Icon-stats: 'NON-SLIP RUBBER BACK', 'LIES FLAT', "
            "'24 x 13.5 IN', 'STABLE DURING PLAY'. Clean, catalog-style layout."
        ),
        overlay="NON-SLIP. LIES FLAT.",
        overlay_sub="Rubber backing keeps the 24 x 13.5 in mat stable while you draw and tap.",
        props=["mat flipped to rubber underside", "top-down inset with cards in play", "4 icon-stats"],
        lighting="Catalog light on black; product and stats clearly separated.",
        why_it_works=(
            "A mat that slides ruins a game. Showing the rubber back plus the flat playing area "
            "answers the two questions every buyer has: does it grip, and is it big enough."
        ),
    ),
    AIImagePlanItem(
        name="Image 6 — Trust: Ultra PRO, trusted since 1952",
        role="trust",
        background="Black with red top-line, white headline (brand close)",
        purpose="Close on brand authority — the player's and collector's default choice.",
        visual=(
            "Hero of the mat with a small lifestyle inset (a player using the mat at a tidy table, "
            "cards mid-game). Brand line bottom: 'ULTRA PRO — supporting players and collectors since "
            "1952 · trusted worldwide'. Red badge: 'SINCE 1952'."
        ),
        overlay="TRUSTED SINCE 1952.",
        overlay_sub="Ultra PRO — reliable gaming accessories for players and collectors.",
        props=["mat hero", "player lifestyle inset", "since-1952 red badge"],
        lighting="Premium catalog light on black; warm inset for the lifestyle moment.",
        why_it_works=(
            "Against generic mats, heritage and trust are deciding signals. 'Since 1952' is Ultra "
            "PRO's honest, compliant authority claim."
        ),
    ),
    AIImagePlanItem(
        name="Image 7 — Use: play surface, display & desk",
        role="close",
        background="White with black/red Ultra PRO chrome",
        purpose="Broaden the use-cases and turn one mat into an everyday want.",
        visual=(
            "Clean three-panel line-up of the same mat in use: PANEL 1 'GAME' — cards in a match; "
            "PANEL 2 'DISPLAY' — mat framed/hung as licensed art; PANEL 3 'DESK' — mat as an "
            "oversized desk mat / mousepad. Small labels; caption: 'Game on it. Display it. Live "
            "with the art — the Ultra PRO way.'"
        ),
        overlay="GAME. DISPLAY. DESK.",
        overlay_sub="Use it for TCG play, collectible display, or as an oversized desk mat.",
        props=["panel: cards in play", "panel: mat displayed as art", "panel: mat as desk mat/mousepad"],
        lighting="Bright, even; coordinated three-panel family shot.",
        why_it_works=(
            "Multiple honest use-cases widen the audience beyond match play and justify the mat as "
            "an everyday piece — reinforcing perceived value."
        ),
    ),
]


# ===== 4 kreative Module + Q&A/Vergleich aus dem A+ Sheet =====

CREATIVE_MODULES = [
    AIModule(
        name="Module 1 — Brand banner",
        role="a+_banner",
        headline="PLAY ON THE ART. SINCE 1952.",
        body=(
            "The Ultra PRO Magic: The Gathering x FINAL FANTASY playmat features officially licensed "
            "Lightning, Army of One artwork on a soft fabric top, framed by black stitched edges over "
            "a non-slip rubber backing. Approximately 24 x 13.5 inches of gaming accessory trusted by "
            "players and collectors since 1952."
        ),
        visual="Wide black banner, red top-line, bold white headline left; the full playmat with the Lightning artwork right. Ultra PRO logo upper-left.",
        alt="Ultra PRO MTG Final Fantasy Lightning playmat banner: licensed art, stitched edges, non-slip, since 1952.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): Why this playmat",
        role="a+_carousel",
        headline="WHY THIS ULTRA PRO PLAYMAT",
        body=(
            "Tile 1: <b>OFFICIALLY LICENSED ART</b> — MTG x FINAL FANTASY Lightning, Army of One.<br/>"
            "Tile 2: <b>SOFT FABRIC TOP</b> — Smooth card handling, helps reduce wear.<br/>"
            "Tile 3: <b>BLACK STITCHED EDGES</b> — Framed, premium, resist fraying.<br/>"
            "Tile 4: <b>NON-SLIP RUBBER BACK</b> — Stays put and lies flat at 24 x 13.5 in.<br/>"
            "Tile 5: <b>SINCE 1952</b> — Trusted gaming accessories worldwide."
        ),
        visual="5 square tiles, red accent corner each, black/white icons (art frame · fabric weave · stitch · grip · badge).",
        alt="Five A+ tiles: licensed art, soft fabric top, stitched edges, non-slip backing, since 1952.",
    ),
    AIModule(
        name="Module 3 — Banner: Built for play & display",
        role="a+_banner",
        headline="BUILT FOR PLAY. MADE TO DISPLAY.",
        body=(
            "The soft fabric surface makes shuffling and card pick-up easy while helping protect your "
            "cards, and the non-slip rubber backing keeps the mat flat and stable. Approximately 24 x "
            "13.5 inches — use it for matches, sorting, collectible display, or as an oversized desk mat."
        ),
        visual="Banner split: macro of the fabric top and stitched corner left; top-down of the full Lightning artwork with cards in play right. Black/red Ultra PRO styling.",
        alt="A+ banner on the soft fabric, stitched, non-slip Ultra PRO Final Fantasy playmat.",
    ),
    AIModule(
        name="Module 4 — Carousel (4 tiles): One mat, many uses",
        role="a+_carousel",
        headline="GAME IT. DISPLAY IT. LIVE WITH IT.",
        body=(
            "Tile 1: <b>TCG PLAY</b> — A dedicated surface for Magic and other card games.<br/>"
            "Tile 2: <b>SORT &amp; ORGANIZE</b> — Lay out and manage your collection.<br/>"
            "Tile 3: <b>COLLECTIBLE DISPLAY</b> — Show the licensed Lightning artwork.<br/>"
            "Tile 4: <b>OVERSIZED DESK MAT</b> — Doubles as a desk mat or mousepad."
        ),
        visual="4 coordinated use-case tiles, red accent corners, consistent catalog styling.",
        alt="Four A+ tiles showing the Ultra PRO playmat used for play, sorting, display and desk.",
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
        modules.append(SEOL.qa_module(ap, headline="COLLECTOR Q&A"))
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
