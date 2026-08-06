"""Ultra PRO — Eclipse Gloss Standard Deck Protector Sleeves, 100 ct  [Listing 53]
NEUES Format: Titel/Bullets/Backend kommen aus dem SEO-Sheet (listing.xlsx),
Q&A + Vergleich aus dem A+ Premium Sheet (aplus.xlsx). Bildregie handgeschrieben,
100% produktspezifisch, im Ultra-PRO-Katalogstil (schwarz/rot/weiss + Apple-Red-Akzent).

Produkt: Ultra Pro ECLIPSE Gloss "Apple Red" Standard Deck Protector Sleeves, 100 Pack,
66 mm x 91 mm, High-Clarity Gloss Front, fully opaque ChromaFusion Backing, smooth shuffle feel.

Marketplace: amazon.com (US). ASIN B09BK5PTSH.
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

PLAN_NO = "53"
ASIN = "B09BK5PTSH"
EXCEL = HERE / "listing.xlsx"
APLUS = HERE / "aplus.xlsx"


# ===== produktspezifische Bildregie (Ultra-PRO-Katalogstil, EN Overlays) =====

IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="Clean white for slot-1 compliance; the CTR versions add a black lower band with a thin red top-line (Ultra PRO catalog look). Same framing across all 3.",
        purpose="Win the click among look-alike deck sleeves. Ship all 3, keep the winner.",
        visual=(
            "Mock ALL 3 options. Product exactly as real: Ultra PRO Eclipse sleeves in Apple Red, "
            "a real standard trading card in the gloss front, plus the 100-count pack. ONE callout "
            "each, product dominant.\n\n"
            "OPTION A — GLOSS FRONT: a foil/holo card seen crisp through the high-clarity gloss "
            "face. Badge (red): 'HIGH-CLARITY GLOSS'.\n"
            "OPTION B — PACK VALUE: the 100-count Apple Red pack, a short fan of sleeves in front. "
            "Badge (red): '100 SLEEVES'.\n"
            "OPTION C — OPAQUE BACK: the Apple Red ChromaFusion back of a face-down deck, fully "
            "opaque & even. Badge (red): 'FULLY OPAQUE BACK'.\n\n"
            "Across all 3: white background, red badge ~6% of frame, same lighting; Apple Red is "
            "the one accent colour."
        ),
        overlay="(one callout per option)",
        overlay_sub="3 hero options shipped — A/B test, keep the winner.",
        props=["A: foil card in gloss front", "B: 100-count Apple Red pack fanned", "C: opaque Apple Red ChromaFusion back"],
        lighting="Bright, even studio light; crisp catch-light so the gloss front and rich Apple Red read on white.",
        why_it_works=(
            "Three triggers: gloss clarity (see foil), pack value (100), opaque back (fair play). "
            "One callout each — readable at thumbnail size."
        ),
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: high-clarity gloss front shows the foil",
        role="hook",
        background="Black with a thin red top-line and a bold white headline (Ultra PRO catalog)",
        purpose="Own the reason players pick gloss: foil and holo detail stay bright and visible.",
        visual=(
            "Large macro: a holographic/foil trading card sliding into the Eclipse gloss front, the "
            "art and foil shimmer sharp and true-colour through the glossy film. Thin red callout "
            "lines: 'high-clarity gloss face', 'foil & holo pop', 'covered during play'. White bold "
            "headline top: 'SEE THE FOIL.'"
        ),
        overlay="HIGH-CLARITY GLOSS FRONT.",
        overlay_sub="A glossy front face keeps foil and holo detail bright and fully visible.",
        props=["foil card sliding into gloss front (macro)", "red callout lines", "true-colour foil shimmer"],
        lighting="Dramatic catalog light on black; strong edge-light so the gloss finish and foil catch the light.",
        why_it_works=(
            "Gloss vs matte is the first choice players make. A true-colour foil macro proves the "
            "gloss front genuinely shows the card — the strongest visual argument in the category."
        ),
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: ChromaFusion opaque back & smooth shuffle",
        role="educate",
        background="White with a black/red Ultra PRO footer band",
        purpose="Explain ChromaFusion: a fully opaque back for fair play plus a smooth shuffle feel.",
        visual=(
            "Split card. LEFT: a face-down Apple Red deck, uniform and fully opaque, small icon "
            "'CHROMAFUSION BACK'. RIGHT: three stacked feature rows with red check-icons — "
            "'FULLY OPAQUE — no card show-through', 'CONSISTENT DECK LOOK in matches', 'SMOOTH "
            "SHUFFLE FEEL for repeated play'. Footer band: 'Time-tested card protection — trusted "
            "since 1952.'"
        ),
        overlay="FULLY OPAQUE BACK.",
        overlay_sub="ChromaFusion backing hides card faces and gives a smooth, consistent shuffle.",
        props=["face-down Apple Red opaque deck", "3 feature rows with red checks", "since-1952 footer band"],
        lighting="Flat, even catalog light; feature icons legible at thumbnail size.",
        why_it_works=(
            "Tournament players need a back that can't be read and shuffles cleanly. Naming "
            "ChromaFusion with a clear 'why it matters' separates this from thin bargain sleeves."
        ),
    ),
    AIImagePlanItem(
        name="Image 4 — Fit: standard size 66 x 91 mm",
        role="desire",
        background="White with a red dimension callout (Ultra PRO)",
        purpose="Remove the top buyer question — will my cards fit?",
        visual=(
            "A standard trading card centred in the sleeve with a clean dimension callout: 'Fits "
            "standard-size cards — 66 mm x 91 mm'. Small ruler graphic along two edges. A short "
            "note: 'Precise, easy-load fit for TCG play, sorting & storage.'"
        ),
        overlay="FITS 66 X 91 MM.",
        overlay_sub="Sized for standard trading cards — a precise, easy-load fit for TCG play.",
        props=["standard card in sleeve", "66 x 91 mm dimension callout", "edge ruler graphic"],
        lighting="Bright, even; the dimension callout must read clearly.",
        why_it_works=(
            "Wrong-size sleeves are the top return reason. A precise 66 x 91 mm fit callout sets "
            "honest expectations and avoids mis-buys for MTG, Pokemon and other TCGs."
        ),
    ),
    AIImagePlanItem(
        name="Image 5 — Pack: 100 sleeves for decks & gameplay",
        role="desire",
        background="Black with red accents (Ultra PRO catalog)",
        purpose="Make the 100-count value and use-cases obvious.",
        visual=(
            "The 100-count Apple Red pack with several sleeved cards fanned as a ready deck. "
            "Icon-stats: '100 SLEEVES', 'Sleeve a full deck', 'Swap worn sleeves', 'Sort & store "
            "collections'. Clean, catalog-style layout."
        ),
        overlay="100 SLEEVES PER PACK.",
        overlay_sub="Sleeve a full deck, swap worn sleeves, and sort or store your collection.",
        props=["100-count Apple Red pack", "fanned sleeved deck", "4 icon-stats"],
        lighting="Catalog light on black; product and stats clearly separated.",
        why_it_works=(
            "Shows 100 count as a working tool, not just a number — speaks to competitive players, "
            "collectors and hobby shops alike."
        ),
    ),
    AIImagePlanItem(
        name="Image 6 — Trust: archival-safe, trusted since 1952",
        role="trust",
        background="Black with red top-line, white headline (brand close)",
        purpose="Close on brand authority — the player's and collector's default choice.",
        visual=(
            "Hero of the Apple Red pack with a small lifestyle inset (a player sleeving a deck at a "
            "tidy game table). Brand line bottom: 'ULTRA PRO — protecting cards since 1952 · "
            "archival-safe polypropylene'. Red badge: 'SINCE 1952'."
        ),
        overlay="TRUSTED SINCE 1952.",
        overlay_sub="Ultra PRO — archival-safe polypropylene protecting cards worldwide.",
        props=["Apple Red pack hero", "player lifestyle inset", "since-1952 red badge"],
        lighting="Premium catalog light on black; warm inset for the lifestyle moment.",
        why_it_works=(
            "Against unbranded bargain sleeves, heritage and archival safety are the deciding "
            "signals. 'Since 1952' is Ultra PRO's honest, compliant authority claim."
        ),
    ),
    AIImagePlanItem(
        name="Image 7 — Range: the Eclipse colour system",
        role="close",
        background="White with black/red Ultra PRO chrome",
        purpose="Cross-sell the wider Eclipse colour range and deck-building system.",
        visual=(
            "Clean line-up: Eclipse gloss sleeves in a row of colours (Apple Red highlighted, this "
            "product) alongside a matte Eclipse pack and a deck box — shown as a coordinated "
            "system. Small labels; the Apple Red pack gently highlighted. Caption: 'Match your "
            "deck. Build your set. — the Ultra PRO Eclipse way.'"
        ),
        overlay="MATCH YOUR DECK.",
        overlay_sub="Build a set — pair Eclipse gloss sleeves with matte packs and deck boxes.",
        props=["Eclipse colour line-up (Apple Red highlighted)", "matte Eclipse pack", "deck box"],
        lighting="Bright, even; coordinated family shot.",
        why_it_works=(
            "Turns one purchase into a colour-matched system sale and reinforces Ultra PRO Eclipse "
            "as the go-to deck-protection line."
        ),
    ),
]


# ===== 4 kreative Module + Q&A/Vergleich aus dem A+ Sheet =====

CREATIVE_MODULES = [
    AIModule(
        name="Module 1 — Brand banner",
        role="a+_banner",
        headline="SEE THE FOIL. GUARD THE DECK.",
        body=(
            "Ultra PRO Eclipse gloss deck protector sleeves pair a high-clarity gloss front that "
            "shows off foil and holo detail with a fully opaque ChromaFusion back for fair play and "
            "a smooth shuffle. Archival-safe polypropylene, standard 66 mm x 91 mm size — card "
            "protection trusted by players since 1952."
        ),
        visual="Wide black banner, red top-line, bold white headline left; an Apple Red sleeve with a foil card front and opaque back right. Ultra PRO logo upper-left.",
        alt="Ultra PRO Eclipse gloss deck sleeves banner: high-clarity gloss front, opaque ChromaFusion back, since 1952.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): Why Eclipse gloss",
        role="a+_carousel",
        headline="WHY ULTRA PRO ECLIPSE GLOSS",
        body=(
            "Tile 1: <b>HIGH-CLARITY GLOSS FRONT</b> — Foil &amp; holo detail stays bright and visible.<br/>"
            "Tile 2: <b>CHROMAFUSION OPAQUE BACK</b> — Fully opaque back for a consistent deck look.<br/>"
            "Tile 3: <b>SMOOTH SHUFFLE FEEL</b> — Slick handling for repeated gameplay.<br/>"
            "Tile 4: <b>STANDARD 66 x 91 MM</b> — Precise fit for standard TCG cards.<br/>"
            "Tile 5: <b>100 SLEEVES · SINCE 1952</b> — Archival-safe, trusted card protection."
        ),
        visual="5 square tiles, red accent corner each, black/white icons (gloss card · opaque back · shuffle · ruler · badge); Apple Red as the one accent.",
        alt="Five A+ tiles: gloss front, opaque ChromaFusion back, smooth shuffle, standard 66x91mm fit, 100-count since 1952.",
    ),
    AIModule(
        name="Module 3 — Banner: Fair play & smooth shuffle",
        role="a+_banner",
        headline="FULLY OPAQUE. SMOOTH SHUFFLE.",
        body=(
            "ChromaFusion technology gives a fully opaque back so no card shows through and every "
            "deck looks the same face-down. The polypropylene film keeps a smooth shuffle feel "
            "through long sessions &amp; regular handling — clean play, match after match."
        ),
        visual="Banner split: a face-down Apple Red opaque deck + shuffle-motion icon left; a sleeved foil card front right. Black/red Ultra PRO styling.",
        alt="A+ banner on ChromaFusion fully opaque back and smooth shuffle feel for fair, consistent play.",
    ),
    AIModule(
        name="Module 4 — Carousel (4 tiles): The Eclipse deck system",
        role="a+_carousel",
        headline="MATCH YOUR DECK. BUILD YOUR SET.",
        body=(
            "Tile 1: <b>ECLIPSE GLOSS SLEEVES</b> — High-clarity gloss front, opaque back (this product).<br/>"
            "Tile 2: <b>ECLIPSE MATTE SLEEVES</b> — Matte gloss-free finish, same opaque back.<br/>"
            "Tile 3: <b>ECLIPSE DECK BOXES</b> — Colour-matched storage for a sleeved deck.<br/>"
            "Tile 4: <b>PLAYMATS &amp; STORAGE</b> — Round out the table and archive the collection."
        ),
        visual="4 coordinated product tiles, red accent corners, consistent catalog styling, Apple Red colour-match thread.",
        alt="Four A+ tiles showing the Ultra PRO Eclipse system: gloss sleeves, matte sleeves, deck boxes, playmats and storage.",
    ),
]


def main() -> None:
    print(f"Lade Ultra PRO + SEO/A+ Sheets für Listing {PLAN_NO}…")
    cust = load_customer("ultra_pro")
    brief = parse_excel(EXCEL)
    seo = SEOL.load_seo(EXCEL)
    ap = SEOL.load_aplus(APLUS)
    # Compliance: the source A+ Q&A contains the restricted claim word "prevent"
    # ("helps prevent card visibility"). Swap it for a compliant verb before it flows
    # into the Q&A module + Q&A list. SEO/A+ content otherwise passes through untouched.
    import re as _re
    ap.qa = [(_re.sub(r"prevent", "reduce", q, flags=_re.I),
              _re.sub(r"prevent", "reduce", a, flags=_re.I)) for q, a in ap.qa]
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
