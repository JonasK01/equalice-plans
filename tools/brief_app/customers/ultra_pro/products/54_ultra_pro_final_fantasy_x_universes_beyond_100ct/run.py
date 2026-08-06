"""Ultra PRO — Magic: The Gathering x Final Fantasy 'The Crystal's Chosen'
Deck Protector Sleeves, 100 ct  [Listing 54]

LIZENZIERTES Produkt. Titel/Bullets/Backend kommen aus dem SEO-Sheet (listing.xlsx),
Q&A + Vergleich aus dem A+ Premium Sheet (aplus.xlsx). Bildregie handgeschrieben,
100% produktspezifisch. HERO = die lizenzierte 'Crystal's Chosen'-Artwork, die farbig
dominieren darf; drumherum Ultra-PRO-Katalogstil (schwarz/rot/weiss).

Marketplace: amazon.com (US). ASIN B0F5YHYPZ5.
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

PLAN_NO = "54"
ASIN = "B0F5YHYPZ5"
EXCEL = HERE / "listing.xlsx"
APLUS = HERE / "aplus.xlsx"


# ===== produktspezifische Bildregie (Ultra-PRO-Katalogstil, EN Overlays) =====

IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="Clean white for slot-1 compliance; the CTR versions add a black lower band with a thin red top-line (Ultra PRO catalog look). Same framing across all 3.",
        purpose="Win the click in a grid of plain-colour sleeves by leading with the licensed Final Fantasy artwork.",
        visual=(
            "Mock ALL 3 options. Product exactly as real: a Deck Protector sleeve carrying a real "
            "Magic card, the full-colour 'Crystal's Chosen' artwork printed across the sleeve back, "
            "plus the 100-count pack behind it. ONE callout each, product dominant.\n\n"
            "OPTION A — LICENSED ART: single sleeve, the Crystal's Chosen artwork facing camera, "
            "colours rich and true. Badge (red): 'OFFICIALLY LICENSED'.\n"
            "OPTION B — PACK VALUE: the 100-count pack with the art-back fanned. Badge (red): "
            "'100 SLEEVES'.\n"
            "OPTION C — MATTE FIT: sleeve at an angle showing the matte, no-glare surface + a real "
            "standard card loading in. Badge: 'MATTE · STANDARD SIZE'.\n\n"
            "Across all 3: white background, licensed art allowed to dominate in colour, red badge "
            "~6% of frame, same lighting."
        ),
        overlay="(one callout per option)",
        overlay_sub="3 hero options shipped — A/B test, keep the winner.",
        props=["A: single art-back sleeve with card", "B: 100-count pack fanned", "C: matte sleeve + standard card loading"],
        lighting="Bright, even studio light; soft catch-light so the matte finish reads without glare on white.",
        why_it_works=(
            "Three triggers: licensed artwork (fandom), pack value (100), matte + standard fit. "
            "One callout each — readable at thumbnail size."
        ),
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: the licensed Crystal's Chosen artwork",
        role="hook",
        background="Black with a thin red top-line and a bold white headline (Ultra PRO catalog)",
        purpose="Own the #1 reason to buy this over a plain sleeve: the exclusive licensed art.",
        visual=(
            "Large hero of one sleeve, the full-colour 'The Crystal's Chosen' artwork by Kotetsu "
            "Kinoshita filling the frame, a real standard card visible through the mouth. Thin red "
            "callout lines: 'Officially licensed', 'Magic: The Gathering x Final Fantasy', "
            "'exclusive full-colour art'. White bold headline top: 'SHOW YOUR FANDOM.' Small "
            "'Officially Licensed' lockup in a corner."
        ),
        overlay="THE CRYSTAL'S CHOSEN.",
        overlay_sub="Exclusive full-colour Magic x Final Fantasy artwork on every sleeve.",
        props=["single art-back sleeve (hero)", "real standard card in mouth", "red callout lines", "officially-licensed lockup"],
        lighting="Dramatic catalog light on black; even wash so the printed art stays true-colour and glare-free.",
        why_it_works=(
            "Fans buy licensed sleeves to display their fandom at the table. Leading with the "
            "artwork is the single strongest reason to pick this over a plain sleeve."
        ),
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: matte finish + ChromaFusion, art won't peel",
        role="educate",
        background="White with a black/red Ultra PRO footer band",
        purpose="Defend quality: why the matte, ChromaFusion-printed surface matters in real play.",
        visual=(
            "Split card. LEFT: a sleeve tilted under a light source showing the matte surface killing "
            "reflections, a small icon 'NO GLARE'. RIGHT: three stacked feature rows with red "
            "check-icons — 'MATTE finish reduces glare', 'ChromaFusion print resists peeling', "
            "'Archival-safe polypropylene'. Footer band: 'Built for shuffling, handling & storage.'"
        ),
        overlay="MATTE FINISH. NO GLARE.",
        overlay_sub="Matte surface cuts glare; ChromaFusion print resists peeling in play.",
        props=["tilted sleeve under light (matte, no reflection)", "3 feature rows with red checks", "footer band"],
        lighting="Flat, even catalog light plus one raking light to prove the matte no-glare surface.",
        why_it_works=(
            "Players filter on matte vs glossy and on durability. Naming matte + ChromaFusion + "
            "archival-safe with a clear 'why it matters' separates this from generic printed sleeves."
        ),
    ),
    AIImagePlanItem(
        name="Image 4 — Fit: sized for standard trading cards",
        role="desire",
        background="White with a red dimension callout (Ultra PRO)",
        purpose="Remove the #1 buyer question — will my cards fit?",
        visual=(
            "A real standard card centred, loading into the sleeve, with a clean dimension callout: "
            "'Fits standard size cards — 66mm x 91mm (2.5\" x 3.5\")'. Small ruler graphic along two "
            "edges. Short note: 'Smooth, easy-load fit for Magic and other standard TCGs.'"
        ),
        overlay="FITS STANDARD CARDS.",
        overlay_sub="Sized for 66mm x 91mm (2.5 x 3.5 in) standard trading cards.",
        props=["standard card loading into sleeve", "dimension callout 66x91mm", "edge ruler graphic"],
        lighting="Bright, even; the dimension callout must read clearly.",
        why_it_works=(
            "Wrong-size sleeves are the top return reason in this category. A precise standard-size "
            "callout sets honest expectations and prevents mis-buys."
        ),
    ),
    AIImagePlanItem(
        name="Image 5 — Pack: 100 sleeves, a full deck protected",
        role="desire",
        background="Black with red accents (Ultra PRO catalog)",
        purpose="Make the pack value and real use-cases obvious.",
        visual=(
            "The 100-count pack with a sleeved deck fanned so several art-backs show together. "
            "Icon-stats: '100 SLEEVES', 'A full standard deck', 'Casual & tournament play', "
            "'Camera-ready content'. Clean, catalog-style layout."
        ),
        overlay="100 SLEEVES PER PACK.",
        overlay_sub="Enough for a full standard deck — casual play, tournaments, content.",
        props=["100-count pack", "sleeved deck fanned (art-backs)", "4 icon-stats"],
        lighting="Catalog light on black; product and stats clearly separated.",
        why_it_works=(
            "Shows the quantity is a working tool — one pack sleeves a full deck — speaking to "
            "players, collectors and content creators alike."
        ),
    ),
    AIImagePlanItem(
        name="Image 6 — Trust: Ultra PRO, trusted since 1952",
        role="trust",
        background="Black with red top-line, white headline (brand close)",
        purpose="Close on brand authority — the player's default choice.",
        visual=(
            "Hero of the pack with a small lifestyle inset (a player sleeving a deck at a tidy game "
            "table). Brand line bottom: 'ULTRA PRO — protecting cards & collections since 1952 · "
            "trusted by players worldwide'. Red badge: 'SINCE 1952'."
        ),
        overlay="TRUSTED SINCE 1952.",
        overlay_sub="Ultra PRO — protecting cards and collections worldwide.",
        props=["pack hero", "player lifestyle inset", "since-1952 red badge"],
        lighting="Premium catalog light on black; warm inset for the lifestyle moment.",
        why_it_works=(
            "Against generic printed sleeves, licensed authority plus heritage are the deciding "
            "signals. 'Since 1952' is Ultra PRO's honest, compliant authority claim."
        ),
    ),
    AIImagePlanItem(
        name="Image 7 — Range: the Ultra PRO card protection system",
        role="close",
        background="White with black/red Ultra PRO chrome",
        purpose="Cross-sell the wider card-protection range.",
        visual=(
            "Clean line-up: these Final Fantasy Deck Protector sleeves (this product) alongside "
            "toploaders and a card storage organizer — shown as a coordinated system. Small labels; "
            "the licensed sleeves gently highlighted. Caption: 'Sleeve it. Protect it. Store it. — "
            "the Ultra PRO way.'"
        ),
        overlay="SLEEVE IT. STORE IT.",
        overlay_sub="Protect it — pair with Ultra PRO toploaders and storage organizers.",
        props=["licensed sleeves (highlighted)", "toploaders", "card storage organizer"],
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
        headline="SHOW YOUR FANDOM. SINCE 1952.",
        body=(
            "Officially licensed Magic: The Gathering x Final Fantasy Deck Protector sleeves featuring "
            "the exclusive full-colour 'The Crystal's Chosen' artwork by Kotetsu Kinoshita. A matte, "
            "no-glare finish and archival-safe polypropylene protect standard size cards through every "
            "shuffle &amp; store — card protection trusted by players since 1952."
        ),
        visual="Wide black banner, red top-line, bold white headline left; a single art-back sleeve with the Crystal's Chosen artwork right. Ultra PRO logo upper-left, small officially-licensed lockup.",
        alt="Ultra PRO Final Fantasy Crystal's Chosen deck protector sleeves banner: officially licensed, matte, since 1952.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): Why these sleeves",
        role="a+_carousel",
        headline="WHY THESE ULTRA PRO SLEEVES",
        body=(
            "Tile 1: <b>OFFICIALLY LICENSED</b> — Magic: The Gathering x Final Fantasy design.<br/>"
            "Tile 2: <b>CRYSTAL'S CHOSEN ART</b> — Exclusive full-colour artwork by Kotetsu Kinoshita.<br/>"
            "Tile 3: <b>MATTE &amp; NO-GLARE</b> — Comfortable viewing, camera-ready.<br/>"
            "Tile 4: <b>STANDARD SIZE FIT</b> — 66mm x 91mm (2.5\" x 3.5\"), easy load.<br/>"
            "Tile 5: <b>100-COUNT PACK</b> — A full deck of protection, since 1952."
        ),
        visual="5 square tiles, red accent corner each, black/white icons (licence badge · artwork · matte swatch · card · stack). The licensed art may show in colour.",
        alt="Five A+ tiles: officially licensed, Crystal's Chosen art, matte no-glare, standard fit, 100-count.",
    ),
    AIModule(
        name="Module 3 — Banner: Durable protection",
        role="a+_banner",
        headline="MATTE FINISH. DURABLE PROTECTION.",
        body=(
            "Made with archival-safe polypropylene and ChromaFusion Technology designed to help resist "
            "peeling, so the artwork stays crisp through regular shuffling &amp; handling. The matte "
            "surface reduces glare for comfortable play at home, at tournaments, or on camera."
        ),
        visual="Banner split: macro of the matte sleeve back under a raking light (no glare) + no-peel / archival-safe icons left; a sleeved deck right. Black/red Ultra PRO styling.",
        alt="A+ banner on matte, no-glare, archival-safe deck protector sleeves with ChromaFusion print.",
    ),
    AIModule(
        name="Module 4 — Carousel (4 tiles): The card protection system",
        role="a+_carousel",
        headline="SLEEVE IT. PROTECT IT. STORE IT.",
        body=(
            "Tile 1: <b>DECK PROTECTOR SLEEVES</b> — Licensed matte sleeves (this product).<br/>"
            "Tile 2: <b>ECLIPSE SLEEVES</b> — Solid-colour matte deck protection.<br/>"
            "Tile 3: <b>TOPLOADERS</b> — Rigid protection for key cards.<br/>"
            "Tile 4: <b>STORAGE ORGANIZERS</b> — Sort and archive full collections."
        ),
        visual="4 coordinated product tiles, red accent corners, consistent catalog styling.",
        alt="Four A+ tiles showing the Ultra PRO card protection system: sleeves, eclipse sleeves, toploaders, organizers.",
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
