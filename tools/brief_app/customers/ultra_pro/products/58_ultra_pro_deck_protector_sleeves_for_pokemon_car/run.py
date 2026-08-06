"""Ultra PRO — Pokémon Deck Protector Sleeves feat. Ceruledge (65 ct)  [Listing 58]
NEUES Format: Titel/Bullets/Backend kommen aus dem SEO-Sheet (listing.xlsx),
Q&A + Vergleich aus dem A+ Premium Sheet (aplus.xlsx). Bildregie handgeschrieben,
100% produktspezifisch, im Ultra-PRO-Katalogstil (schwarz/rot/weiss). Das offiziell
lizenzierte Ceruledge-Motiv darf farbig sein.

Marketplace: amazon.com (US). ASIN B0DFDYZY25.
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

PLAN_NO = "58"
ASIN = "B0DFDYZY25"
EXCEL = HERE / "listing.xlsx"
APLUS = HERE / "aplus.xlsx"


# ===== produktspezifische Bildregie (Ultra-PRO-Katalogstil, EN Overlays) =====

IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="Clean white for slot-1 compliance; the CTR versions add a black lower band with a thin red top-line (Ultra PRO catalog look). Same framing across all 3.",
        purpose="Win the click in a grid of look-alike Pokémon sleeves. Ship all 3, keep the winner.",
        visual=(
            "Mock ALL 3 options. Product exactly as real: standard-size deck protector sleeves with "
            "the full-colour Ceruledge art-back, plus the 65-count pack behind them. Real Pokémon "
            "cards, ONE callout each, product dominant. The Ceruledge motif stays vibrant/colourful; "
            "all chrome around it is Ultra PRO black/red/white.\n\n"
            "OPTION A — LICENSE: fanned sleeves showing the vivid Ceruledge art-back. Badge (red): "
            "'OFFICIAL POKÉMON'.\n"
            "OPTION B — PACK VALUE: the 65-count pack front and centre. Badge (red): '65 SLEEVES'.\n"
            "OPTION C — TECH: a card sliding into a sleeve, edge crisp. Badge: 'CHROMAFUSION'.\n\n"
            "Across all 3: white background, red badge ~6% of frame, same lighting."
        ),
        overlay="(one callout per option)",
        overlay_sub="3 hero options shipped — A/B test, keep the winner.",
        props=["A: fanned Ceruledge art-back sleeves", "B: 65-count pack", "C: card sliding into sleeve"],
        lighting="Bright, even studio light; crisp catch-light so the glossy art-back reads on white.",
        why_it_works=(
            "Three triggers: official licence (Ceruledge), pack value (65) and ChromaFusion tech. "
            "One callout each — readable at thumbnail size."
        ),
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: official Ceruledge full-colour art-back",
        role="hook",
        background="Black with a thin red top-line and a bold white headline (Ultra PRO catalog)",
        purpose="Own the #1 reason fans buy these: the officially licensed Ceruledge look.",
        visual=(
            "Large hero of a single sleeve, the vibrant full-colour Ceruledge character art-back "
            "sharp and saturated. Thin red callout lines: 'Officially licensed Pokémon TCG', "
            "'full-colour artwork', 'themed deck & collection'. White bold headline top: "
            "'SHOW YOUR DECK.' The Ceruledge art stays colourful against the black chrome."
        ),
        overlay="OFFICIAL CERULEDGE ART.",
        overlay_sub="Officially licensed Pokémon TCG sleeves with vibrant full-colour Ceruledge artwork.",
        props=["single sleeve hero (Ceruledge art-back)", "red callout lines", "official-licence line"],
        lighting="Dramatic catalog light on black; strong edge-light so the glossy art-back pops.",
        why_it_works=(
            "Themed players buy the character first. A saturated, true-colour art-back hero is the "
            "single strongest visual argument in the licensed-sleeve category."
        ),
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: standard size, fits your TCG cards",
        role="educate",
        background="White with a black/red Ultra PRO footer band",
        purpose="Remove the #1 buyer question — will these fit my Pokémon cards?",
        visual=(
            "A standard-size Pokémon card centred in a sleeve with a clean dimension callout: "
            "'Fits standard-size cards — 66mm x 91mm (2.5\" x 3.5\")'. Small ruler graphic along two "
            "edges. Short note: 'Proper fit — smooth load, easy handling.' Footer band: "
            "'Time-tested card protection — trusted since 1952.'"
        ),
        overlay="FITS STANDARD CARDS.",
        overlay_sub="Sized for standard TCG cards — 66mm x 91mm (2.5\" x 3.5\"), smooth easy load.",
        props=["card in sleeve", "dimension callout 66x91mm", "edge ruler graphic", "since-1952 footer band"],
        lighting="Bright, even catalog light; the dimension callout must read clearly.",
        why_it_works=(
            "Wrong-size sleeves are the top return reason in this category. A precise fit callout "
            "sets honest expectations and reduces mis-buys."
        ),
    ),
    AIImagePlanItem(
        name="Image 4 — Desire: ChromaFusion, archival-safe & non-PVC",
        role="desire",
        background="Black with red accents (Ultra PRO catalog)",
        purpose="Defend quality: ChromaFusion anti-peel plus archival-safe, non-PVC material.",
        visual=(
            "Split card. LEFT: a macro of the sleeve edge, small shield icon 'ARCHIVAL-SAFE'. "
            "RIGHT: three stacked feature rows with red check-icons — 'CHROMAFUSION helps prevent "
            "peeling', 'NON-PVC polypropylene', 'Built for repeated shuffling & sorting'. Clean, "
            "catalog-style layout."
        ),
        overlay="CHROMAFUSION. NO PEEL.",
        overlay_sub="ChromaFusion helps resist peeling; archival-safe, non-PVC polypropylene.",
        props=["sleeve edge macro", "3 feature rows with red checks", "archival-safe shield icon"],
        lighting="Catalog light on black; feature icons legible at thumbnail size.",
        why_it_works=(
            "Serious players filter on durability. Naming ChromaFusion + non-PVC with a clear 'why "
            "it matters' separates this from unlabeled bargain sleeves."
        ),
    ),
    AIImagePlanItem(
        name="Image 5 — Desire: 65 sleeves for a complete deck",
        role="desire",
        background="Black with red accents (Ultra PRO catalog)",
        purpose="Make the 65-count pack value and use-cases obvious.",
        visual=(
            "The 65-count pack with several Ceruledge-sleeved cards fanned into a deck. Icon-stats: "
            "'65 SLEEVES', 'Complete deck setup', 'Games & events', 'Sort & store collection'. "
            "Clean, catalog-style layout."
        ),
        overlay="65 SLEEVES PER PACK.",
        overlay_sub="65 standard-size sleeves — a complete deck setup for games, events and storage.",
        props=["65-count pack", "fanned deck of sleeved cards", "4 icon-stats"],
        lighting="Catalog light on black; product and stats clearly separated.",
        why_it_works=(
            "Shows 65 is a working deck count, not just a number — speaks to players, event-goers "
            "and collectors alike."
        ),
    ),
    AIImagePlanItem(
        name="Image 6 — Trust: Ultra PRO, trusted since 1952",
        role="trust",
        background="Black with red top-line, white headline (brand close)",
        purpose="Close on brand authority — the collector's default choice.",
        visual=(
            "Hero of the pack with a small lifestyle inset (a player sleeving a deck at a tidy "
            "table). Brand line bottom: 'ULTRA PRO — protecting cards & collections since 1952 · "
            "trusted by players worldwide'. Red badge: 'SINCE 1952'."
        ),
        overlay="TRUSTED SINCE 1952.",
        overlay_sub="Ultra PRO — protecting Pokémon cards and collections worldwide.",
        props=["pack hero", "player lifestyle inset", "since-1952 red badge"],
        lighting="Premium catalog light on black; warm inset for the lifestyle moment.",
        why_it_works=(
            "Against unbranded bargain sleeves, heritage and trust are the deciding signals. 'Since "
            "1952' is Ultra PRO's honest, compliant authority claim."
        ),
    ),
    AIImagePlanItem(
        name="Image 7 — Range: the Ultra PRO card protection system",
        role="close",
        background="White with black/red Ultra PRO chrome",
        purpose="Cross-sell the wider card-protection range.",
        visual=(
            "Clean line-up: the Ceruledge deck protector sleeves (this product) alongside a deck "
            "box, toploaders and a binder — shown as a coordinated system. Small labels; the "
            "sleeves gently highlighted. Caption: 'Sleeve it. Box it. Store it. — the Ultra PRO way.'"
        ),
        overlay="SLEEVE IT. STORE IT.",
        overlay_sub="Box it — pair with Ultra PRO deck boxes, toploaders and binders.",
        props=["Ceruledge sleeves (highlighted)", "deck box", "toploaders", "binder"],
        lighting="Bright, even; coordinated family shot.",
        why_it_works=(
            "Turns one purchase into a system sale and reinforces Ultra PRO as the one-stop "
            "collector brand."
        ),
    ),
]


# ===== 4 kreative Module + Q&A/Vergleich aus dem A+ Sheet =====

CREATIVE_MODULES = [
    AIModule(
        name="Module 1 — Brand banner",
        role="a+_banner",
        headline="SHOW YOUR DECK. SINCE 1952.",
        body=(
            "Officially licensed Pokémon TCG deck protector sleeves featuring vibrant full-colour "
            "Ceruledge artwork. Archival-safe, non-PVC polypropylene with ChromaFusion Technology "
            "that helps resist peeling — standard-size card protection trusted by players since 1952."
        ),
        visual="Wide black banner, red top-line, bold white headline left; a fanned set of Ceruledge art-back sleeves right (colourful). Ultra PRO logo upper-left.",
        alt="Ultra PRO Ceruledge Pokémon deck protector sleeves banner: officially licensed, ChromaFusion, since 1952.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): Why these sleeves",
        role="a+_carousel",
        headline="WHY ULTRA PRO SLEEVES",
        body=(
            "Tile 1: <b>OFFICIAL CERULEDGE ART</b> — Vibrant full-colour Pokémon artwork.<br/>"
            "Tile 2: <b>STANDARD-SIZE FIT</b> — 66mm x 91mm (2.5\" x 3.5\"), smooth load.<br/>"
            "Tile 3: <b>CHROMAFUSION TECH</b> — Helps resist peeling on repeated handling.<br/>"
            "Tile 4: <b>ARCHIVAL-SAFE &amp; NON-PVC</b> — Polypropylene material for storage.<br/>"
            "Tile 5: <b>65 SLEEVES · SINCE 1952</b> — A complete deck, trusted worldwide."
        ),
        visual="5 square tiles, red accent corner each, black/white icons (art-back · ruler · shield · leaf · badge); the Ceruledge tile stays colourful.",
        alt="Five A+ tiles: Ceruledge art, standard fit, ChromaFusion, archival-safe non-PVC, 65 pack since 1952.",
    ),
    AIModule(
        name="Module 3 — Banner: Built to be handled",
        role="a+_banner",
        headline="SHUFFLE-READY. ARCHIVAL-SAFE.",
        body=(
            "Made from archival-safe, non-PVC polypropylene with ChromaFusion Technology to help "
            "resist peeling through games, sorting and storage. Keep standard-size Pokémon cards "
            "protected during play and on the shelf."
        ),
        visual="Banner split: macro of the sleeve edge + archival-safe / non-PVC shield icons left; a fanned Ceruledge deck right. Black/red Ultra PRO styling.",
        alt="A+ banner on ChromaFusion, archival-safe, non-PVC Pokémon card sleeves built for repeated handling.",
    ),
    AIModule(
        name="Module 4 — Carousel (4 tiles): The card storage system",
        role="a+_carousel",
        headline="SLEEVE IT. BOX IT. STORE IT.",
        body=(
            "Tile 1: <b>DECK PROTECTOR SLEEVES</b> — Ceruledge standard-size sleeves (this product).<br/>"
            "Tile 2: <b>DECK BOXES</b> — Carry and protect a sleeved deck.<br/>"
            "Tile 3: <b>TOPLOADERS</b> — Rigid protection for key cards.<br/>"
            "Tile 4: <b>BINDERS &amp; BOXES</b> — Organise and archive full collections."
        ),
        visual="4 coordinated product tiles, red accent corners, consistent catalog styling.",
        alt="Four A+ tiles showing the Ultra PRO card storage system: sleeves, deck boxes, toploaders, binders.",
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
