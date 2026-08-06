"""Ultra PRO — Poké Ball Deck Protector Sleeves, 65 ct  [Listing 67]
NEUES Format: Titel/Bullets/Backend kommen aus dem SEO-Sheet (listing.xlsx),
Q&A + Vergleich aus dem A+ Premium Sheet (aplus.xlsx). Bildregie handgeschrieben,
100% produktspezifisch, im Ultra-PRO-Katalogstil (schwarz/rot/weiss).

Officially Licensed Pokémon Deck Protector sleeves — Poké Ball full-colour design,
standard size, 65 count. Marketplace: amazon.com (US). ASIN B01N9CJBJ0.
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

PLAN_NO = "67"
ASIN = "B01N9CJBJ0"
EXCEL = HERE / "listing.xlsx"
APLUS = HERE / "aplus.xlsx"


# ===== produktspezifische Bildregie (Ultra-PRO-Katalogstil, EN Overlays) =====

IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="Clean white for slot-1 compliance; the CTR versions add a black lower band with a thin red top-line (Ultra PRO catalog look). Same framing across all 3.",
        purpose="Win the click in a grid of look-alike card sleeves. The Poké Ball motif is the hero — its red/white split reads instantly at thumbnail size. Ship all 3, keep the winner.",
        visual=(
            "Mock ALL 3 options. Product exactly as real: standard-size sleeves with the iconic "
            "full-colour Poké Ball printed on the front, one sleeve holding a real Pokémon card, "
            "plus the 65-count pack behind it. ONE callout each, product dominant.\n\n"
            "OPTION A — LICENSE HERO: single sleeve straight-on, the red/white Poké Ball crisp and "
            "centred, a genuine Pokémon card inside. Badge (red): 'OFFICIALLY LICENSED'.\n"
            "OPTION B — PACK VALUE: the 65-count pack with a fanned stack of Poké Ball sleeves. "
            "Badge (red): '65 SLEEVES'.\n"
            "OPTION C — CLEAR FRONT: sleeve angled so the glossy clear front shows the card art "
            "through it. Badge: 'CLEAR GLOSSY FRONT'.\n\n"
            "Across all 3: white background, red badge ~6% of frame, same lighting."
        ),
        overlay="(one callout per option)",
        overlay_sub="3 hero options shipped — A/B test, keep the winner.",
        props=["A: single Poké Ball sleeve + Pokémon card", "B: 65-count pack fanned", "C: sleeve showing glossy clear front"],
        lighting="Bright, even studio light; crisp catch-light so the glossy front and Poké Ball red read on white.",
        why_it_works=(
            "Three triggers: the licensed Poké Ball design (recognisable in a split-second), pack "
            "value (65), and the clear glossy front. One callout each — readable at thumbnail size."
        ),
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: iconic Poké Ball design on every sleeve",
        role="hook",
        background="Black with a thin red top-line and a bold white headline (Ultra PRO catalog)",
        purpose="Own the #1 reason players buy these: the officially licensed Poké Ball look on their deck.",
        visual=(
            "Large macro: a standard Pokémon card sliding into the sleeve, the full-colour Poké Ball "
            "front sharp and true-colour, the card art visible through the glossy clear front. Thin "
            "red callout lines: 'full-colour Poké Ball print', 'clear glossy front', 'themed deck "
            "look'. White bold headline top: 'SLEEVE YOUR DECK.'"
        ),
        overlay="ICONIC POKE BALL DESIGN.",
        overlay_sub="Full-colour licensed Poke Ball front gives your deck a themed, unmistakable look.",
        props=["Pokémon card sliding into sleeve (macro)", "red callout lines", "full-colour Poké Ball front"],
        lighting="Dramatic catalog light on black; strong edge-light on the glossy sleeve front.",
        why_it_works=(
            "Players choose licensed sleeves to personalise their deck. A true-colour macro of the "
            "Poké Ball print is the single strongest visual argument in the category."
        ),
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: archival-safe, non-PVC material",
        role="educate",
        background="White with a black/red Ultra PRO footer band",
        purpose="Defend quality: why archival-safe, non-PVC polypropylene matters for storing cards.",
        visual=(
            "Split card. LEFT: a sleeved Pokémon card with a small shield icon 'ARCHIVAL-SAFE'. "
            "RIGHT: three stacked feature rows with red check-icons — 'ARCHIVAL-SAFE polypropylene', "
            "'NON-PVC film (safe for long-term storage)', 'Clear glossy front keeps card art "
            "visible'. Footer band: 'Time-tested card protection — trusted since 1952.'"
        ),
        overlay="ARCHIVAL-SAFE. NON-PVC.",
        overlay_sub="Archival-safe, non-PVC polypropylene for long-term Pokemon card storage.",
        props=["sleeved card", "3 feature rows with red checks", "since-1952 footer band"],
        lighting="Flat, even catalog light; feature icons legible at thumbnail size.",
        why_it_works=(
            "Serious collectors filter on archival safety. Naming archival-safe + non-PVC with a "
            "clear 'why it matters' separates this from unlabeled bargain sleeves."
        ),
    ),
    AIImagePlanItem(
        name="Image 4 — Fit: standard size for TCG cards",
        role="desire",
        background="White with a red dimension callout (Ultra PRO)",
        purpose="Remove the #1 buyer question — will my cards fit?",
        visual=(
            "A standard Pokémon card centred in the sleeve with a clean dimension callout: 'Fits "
            "standard-size cards 66mm x 91mm (2.5\" x 3.5\")'. Small ruler graphic along two edges. "
            "A short note: 'Proper fit for gameplay, trading and collection storage.'"
        ),
        overlay="FITS STANDARD CARDS.",
        overlay_sub="Sized for standard 66mm x 91mm (2.5 x 3.5 in) trading cards — a proper fit.",
        props=["standard card in sleeve", "dimension callout 66mm x 91mm", "edge ruler graphic"],
        lighting="Bright, even; the dimension callout must read clearly.",
        why_it_works=(
            "Wrong-size sleeves are the top return reason in this category. A precise standard-size "
            "callout sets honest expectations and prevents mis-buys."
        ),
    ),
    AIImagePlanItem(
        name="Image 5 — Pack: 65 sleeves ready a full deck",
        role="desire",
        background="Black with red accents (Ultra PRO catalog)",
        purpose="Make the 65-count value and use-cases obvious.",
        visual=(
            "The 65-count pack with a built standard deck of Poké Ball-sleeved cards fanned beside "
            "it. Icon-stats: '65 SLEEVES', 'Ready a full deck', 'Trade & sort', 'Personalise your "
            "setup'. Clean, catalog-style layout."
        ),
        overlay="65 SLEEVES. FULL DECK.",
        overlay_sub="65 sleeves ready a full standard deck for gameplay, trading and sorting.",
        props=["65-count pack", "built deck of sleeved cards fanned", "4 icon-stats"],
        lighting="Catalog light on black; product and stats clearly separated.",
        why_it_works=(
            "Shows the count is a working tool, not just a number — one pack sleeves a complete "
            "standard deck with cards to spare for trading and sorting."
        ),
    ),
    AIImagePlanItem(
        name="Image 6 — Trust: Ultra PRO, trusted since 1952",
        role="trust",
        background="Black with red top-line, white headline (brand close)",
        purpose="Close on brand authority — the collector's default choice, officially licensed.",
        visual=(
            "Hero of the pack with a small lifestyle inset (a player sleeving cards at a tidy game "
            "table). Brand line bottom: 'ULTRA PRO — Officially Licensed Pokémon accessories · "
            "protecting collections since 1952'. Red badge: 'SINCE 1952'."
        ),
        overlay="TRUSTED SINCE 1952.",
        overlay_sub="Ultra PRO — officially licensed Pokemon accessories, protecting cards worldwide.",
        props=["pack hero", "player lifestyle inset", "since-1952 red badge"],
        lighting="Premium catalog light on black; warm inset for the lifestyle moment.",
        why_it_works=(
            "Against unbranded bargain sleeves, an official license plus heritage are the deciding "
            "signals. 'Since 1952' is Ultra PRO's honest, compliant authority claim."
        ),
    ),
    AIImagePlanItem(
        name="Image 7 — Range: the Ultra PRO card protection system",
        role="close",
        background="White with black/red Ultra PRO chrome",
        purpose="Cross-sell the wider card-protection range.",
        visual=(
            "Clean line-up: Poké Ball deck sleeves (this product) alongside toploaders, a 9-pocket "
            "PRO-Binder and a deck box — shown as a coordinated system. Small labels; the sleeves "
            "gently highlighted. Caption: 'Sleeve it. Store it. Show it. — the Ultra PRO way.'"
        ),
        overlay="SLEEVE IT. STORE IT.",
        overlay_sub="Show it — pair with Ultra PRO binders, toploaders and deck boxes.",
        props=["Poké Ball sleeves (highlighted)", "toploaders", "9-pocket PRO-Binder", "deck box"],
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
        headline="SLEEVE YOUR DECK. SINCE 1952.",
        body=(
            "Officially licensed Poké Ball Deck Protector sleeves give your Pokémon deck a themed, "
            "full-colour look while a clear glossy front keeps card art visible. Archival-safe, "
            "non-PVC polypropylene — card protection trusted by collectors since 1952."
        ),
        visual="Wide black banner, red top-line, bold white headline left; a Poké Ball sleeve holding a Pokémon card right. Ultra PRO logo upper-left.",
        alt="Ultra PRO Poké Ball deck protector sleeves banner: licensed design, archival-safe, non-PVC, since 1952.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): Why these sleeves",
        role="a+_carousel",
        headline="WHY ULTRA PRO POKE BALL SLEEVES",
        body=(
            "Tile 1: <b>ICONIC POKE BALL DESIGN</b> — Full-colour licensed print on every front.<br/>"
            "Tile 2: <b>CLEAR GLOSSY FRONT</b> — Card art and details stay visible.<br/>"
            "Tile 3: <b>ARCHIVAL-SAFE &amp; NON-PVC</b> — Safe for long-term card storage.<br/>"
            "Tile 4: <b>STANDARD SIZE</b> — Fits 66mm x 91mm (2.5 x 3.5 in) cards.<br/>"
            "Tile 5: <b>65-COUNT PACK</b> — Ready a full standard deck, since 1952."
        ),
        visual="5 square tiles, red accent corner each, black/white icons (Poké Ball · glossy front · shield · ruler · stack).",
        alt="Five A+ tiles: Poké Ball design, clear glossy front, archival-safe/non-PVC, standard size, 65-count.",
    ),
    AIModule(
        name="Module 3 — Banner: Archival protection",
        role="a+_banner",
        headline="ARCHIVAL-SAFE. NON-PVC.",
        body=(
            "Made from archival-safe, non-PVC polypropylene film so it is a suitable storage option "
            "for cards you handle every day. Keep standard-size Pokémon cards clean and covered — "
            "in play, in the binder, or in the box."
        ),
        visual="Banner split: macro of the glossy sleeve front + archival-safe/non-PVC shield icons left; a fanned deck of sleeved cards right. Black/red Ultra PRO styling.",
        alt="A+ banner on archival-safe, non-PVC Pokémon card sleeve protection.",
    ),
    AIModule(
        name="Module 4 — Carousel (4 tiles): The card storage system",
        role="a+_carousel",
        headline="SLEEVE IT. STORE IT. SHOW IT.",
        body=(
            "Tile 1: <b>DECK SLEEVES</b> — Poké Ball standard-size protectors (this product).<br/>"
            "Tile 2: <b>TOPLOADERS</b> — Rigid protection for key single cards.<br/>"
            "Tile 3: <b>9-POCKET PRO-BINDER</b> — Store and show up to 360 cards.<br/>"
            "Tile 4: <b>DECK BOXES</b> — Carry and organise your sleeved deck."
        ),
        visual="4 coordinated product tiles, red accent corners, consistent catalog styling.",
        alt="Four A+ tiles showing the Ultra PRO card storage system: sleeves, toploaders, binder, deck box.",
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
