"""Ultra PRO — Pro-Fit Side-Load Standard Inner Sleeves (100 ct)  [Listing 69]
NEUES Format: Titel/Bullets/Backend kommen aus dem SEO-Sheet (listing.xlsx),
Q&A + Vergleich aus dem A+ Premium Sheet (aplus.xlsx). Bildregie handgeschrieben,
100% produktspezifisch, im Ultra-PRO-Katalogstil (schwarz/rot/weiss).

Produkt: klare, perfekt sitzende Innensleeves (Perfect-/Pro-Fit), seitlich
einsteckbar (side-load). Diese kommen ZUERST um die Karte, dann in eine normale
Deck-Protector-Sleeve — Double-Sleeving. Standardgröße (Magic-Size), 100er-Pack.

Marketplace: amazon.com (US). ASIN B0157RCVRK.
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

PLAN_NO = "69"
ASIN = "B0157RCVRK"
EXCEL = HERE / "listing.xlsx"
APLUS = HERE / "aplus.xlsx"


# ===== produktspezifische Bildregie (Ultra-PRO-Katalogstil, EN Overlays) =====

IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="Clean white for slot-1 compliance; the CTR versions add a black lower band with a thin red top-line (Ultra PRO catalog look). Same framing across all 3.",
        purpose="Win the click against look-alike inner-sleeve packs. Ship all 3, keep the winner.",
        visual=(
            "Mock ALL 3 options. Product exactly as real: an ultra-clear Pro-Fit inner sleeve "
            "hugging a generic (non-branded) standard-size gaming card, plus the 100-count pack "
            "behind it. ONE callout each, product dominant.\n\n"
            "OPTION A — PERFECT FIT: sleeve wrapped snug around the card, edges crisp and clear. "
            "Badge (red): 'PERFECT FIT'.\n"
            "OPTION B — DOUBLE SLEEVING: the inner-sleeved card sliding into a standard Deck "
            "Protector — two clear layers visible. Badge (red): 'DOUBLE SLEEVE'.\n"
            "OPTION C — PACK VALUE: the 100-count pack fanned. Badge (red): '100 SLEEVES'.\n\n"
            "Across all 3: white background, red badge ~6% of frame, same lighting."
        ),
        overlay="(one callout per option)",
        overlay_sub="3 hero options shipped — A/B test, keep the winner.",
        props=["A: card snug in inner sleeve", "B: inner-sleeved card into deck sleeve", "C: 100-count pack fanned"],
        lighting="Bright, even studio light; crisp catch-light so the ultra-clear film reads on white.",
        why_it_works=(
            "Three triggers: perfect fit, the double-sleeving payoff, and pack value (100). One "
            "callout each — readable at thumbnail size."
        ),
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: perfect fit, side-load format",
        role="hook",
        background="Black with a thin red top-line and a bold white headline (Ultra PRO catalog)",
        purpose="Own the core promise: a snug inner sleeve you load from the long edge.",
        visual=(
            "Large macro: a standard-size gaming card sliding into the ultra-clear inner sleeve "
            "through the LONG EDGE, a small red arrow showing the side-load direction. The film "
            "hugs the card, artwork sharp through it. Thin red callout lines: 'side-loading', "
            "'close, precise fit', 'clear polypropylene'. White bold headline top: 'PERFECT FIT. "
            "SIDE-LOAD.'"
        ),
        overlay="PERFECT FIT. SIDE-LOAD.",
        overlay_sub="Load from the long edge for a close, precise inner fit around standard cards.",
        props=["card side-loading into inner sleeve (macro)", "red direction arrow", "red callout lines"],
        lighting="Dramatic catalog light on black; strong edge-light on the clear film.",
        why_it_works=(
            "The side-load format and the snug fit are the two things buyers scan for. A single "
            "macro proves both at once — the strongest argument for an inner sleeve."
        ),
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: built for double sleeving",
        role="educate",
        background="White with a black/red Ultra PRO footer band",
        purpose="Explain the #1 use case — inner sleeve first, then a standard Deck Protector.",
        visual=(
            "Three-step illustration with real cards. STEP 1: bare card. STEP 2: card inside the "
            "clear Pro-Fit inner sleeve ('1 · INNER SLEEVE'). STEP 3: that inner-sleeved card "
            "sliding into a standard Deck Protector ('2 · DECK SLEEVE') — both clear layers "
            "visible, red check 'DOUBLE-SLEEVED'. Footer band: 'Card-care accessories — trusted "
            "since 1952.'"
        ),
        overlay="DOUBLE SLEEVE IT.",
        overlay_sub="Inner sleeve first, then a standard Deck Protector — two clear layers of care.",
        props=["3-step double-sleeving illustration", "clear inner + deck sleeve", "since-1952 footer band"],
        lighting="Flat, even catalog light; each step legible at thumbnail size.",
        why_it_works=(
            "Double sleeving is why players buy inner sleeves at all. A clear 3-step visual removes "
            "confusion and shows exactly how the two layers stack."
        ),
    ),
    AIImagePlanItem(
        name="Image 4 — Fit: sized for standard gaming cards",
        role="desire",
        background="White with a red dimension callout (Ultra PRO)",
        purpose="Remove the buyer question — will these fit my cards and my deck sleeves?",
        visual=(
            "A standard Magic-size gaming card centred in the inner sleeve with a clean callout: "
            "'Fits standard / Magic-size gaming cards'. A second small callout: 'Fits inside "
            "standard Deck Protector sleeves'. Short honest note: 'Not for sharp-angled sports "
            "cards — the tight fit may nick corners.'"
        ),
        overlay="STANDARD SIZE FIT.",
        overlay_sub="Sized for standard Magic-size cards and to fit inside standard deck sleeves.",
        props=["standard card in inner sleeve", "size callout", "fits-deck-sleeve callout"],
        lighting="Bright, even; the fit callouts must read clearly.",
        why_it_works=(
            "Wrong-size or wrong-use inner sleeves are the top return reason. A precise fit note, "
            "including the honest sports-card caveat, prevents mis-buys."
        ),
    ),
    AIImagePlanItem(
        name="Image 5 — Pack: 100 inner sleeves, clear & archival-safe",
        role="desire",
        background="Black with red accents (Ultra PRO catalog)",
        purpose="Make the pack value, clarity and archival material obvious.",
        visual=(
            "The 100-count pack with several inner-sleeved cards fanned. Icon-stats: '100 SLEEVES', "
            "'Ultra-clear', 'Acid-free', 'Archival-safe'. Small note: 'For deck building, sorting, "
            "storage and display.' Clean, catalog-style layout."
        ),
        overlay="100 INNER SLEEVES.",
        overlay_sub="Ultra-clear, acid-free, archival-safe polypropylene for everyday deck care.",
        props=["100-count pack", "inner-sleeved cards fanned", "4 icon-stats"],
        lighting="Catalog light on black; product and stats clearly separated.",
        why_it_works=(
            "Shows the quantity is a working supply for deck builders and collectors, and pins the "
            "clear, archival-safe material that separates it from bargain inner sleeves."
        ),
    ),
    AIImagePlanItem(
        name="Image 6 — Trust: Ultra PRO, trusted since 1952",
        role="trust",
        background="Black with red top-line, white headline (brand close)",
        purpose="Close on brand authority — the player's and collector's default choice.",
        visual=(
            "Hero of the pack with a small lifestyle inset (a player double-sleeving cards at a "
            "tidy desk). Brand line bottom: 'ULTRA PRO — card-care accessories since 1952 · trusted "
            "by players and collectors'. Red badge: 'SINCE 1952'."
        ),
        overlay="TRUSTED SINCE 1952.",
        overlay_sub="Ultra PRO — practical card-care accessories for players and collectors.",
        props=["pack hero", "double-sleeving lifestyle inset", "since-1952 red badge"],
        lighting="Premium catalog light on black; warm inset for the lifestyle moment.",
        why_it_works=(
            "Against unbranded inner sleeves, heritage and trust are the deciding signals. 'Since "
            "1952' is Ultra PRO's honest, compliant authority claim."
        ),
    ),
    AIImagePlanItem(
        name="Image 7 — Range: the Ultra PRO sleeving system",
        role="close",
        background="White with black/red Ultra PRO chrome",
        purpose="Cross-sell the wider protection range around double sleeving.",
        visual=(
            "Clean line-up: Pro-Fit inner sleeves (this product) alongside standard Deck Protector "
            "sleeves, a deck box and a 35pt ONE-TOUCH holder — shown as a coordinated system. "
            "Small labels; the inner sleeves gently highlighted. Caption: 'Inner sleeve. Deck "
            "sleeve. Protected. — the Ultra PRO way.'"
        ),
        overlay="SLEEVE IT. STORE IT.",
        overlay_sub="Pair with Ultra PRO deck sleeves, deck boxes and ONE-TOUCH holders.",
        props=["inner sleeves (highlighted)", "deck protector sleeves", "deck box", "35pt ONE-TOUCH holder"],
        lighting="Bright, even; coordinated family shot.",
        why_it_works=(
            "Turns one purchase into a system sale and reinforces Ultra PRO as the one-stop "
            "card-protection brand."
        ),
    ),
]


# ===== 4 kreative Module + Q&A/Vergleich aus dem A+ Sheet =====

CREATIVE_MODULES = [
    AIModule(
        name="Module 1 — Brand banner",
        role="a+_banner",
        headline="PERFECT FIT. DOUBLE SLEEVED.",
        body=(
            "Ultra-clear Pro-Fit inner sleeves wrap snugly around standard gaming cards and load "
            "from the long edge, then slide inside a standard Deck Protector for double sleeving. "
            "Acid-free, archival-safe polypropylene — card care trusted by players since 1952."
        ),
        visual="Wide black banner, red top-line, bold white headline left; an inner-sleeved card sliding into a deck sleeve right. Ultra PRO logo upper-left.",
        alt="Ultra PRO Pro-Fit side-load inner sleeves banner: perfect fit, double sleeving, since 1952.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): Why these inner sleeves",
        role="a+_carousel",
        headline="WHY ULTRA PRO PRO-FIT SLEEVES",
        body=(
            "Tile 1: <b>PERFECT FIT</b> — Wraps snugly around standard gaming cards.<br/>"
            "Tile 2: <b>SIDE-LOADING</b> — Load from the long edge for a secure fit.<br/>"
            "Tile 3: <b>DOUBLE SLEEVING</b> — Fits inside standard Deck Protector sleeves.<br/>"
            "Tile 4: <b>CLEAR &amp; ARCHIVAL-SAFE</b> — Acid-free polypropylene, artwork stays visible.<br/>"
            "Tile 5: <b>100-COUNT PACK</b> — For deck building, sorting and storage."
        ),
        visual="5 square tiles, red accent corner each, black/white icons (card · arrow · double-layer · film · stack).",
        alt="Five A+ tiles: perfect fit, side-loading, double sleeving, clear archival-safe, 100-count.",
    ),
    AIModule(
        name="Module 3 — Banner: Double sleeving",
        role="a+_banner",
        headline="INNER SLEEVE FIRST. THEN DECK SLEEVE.",
        body=(
            "Slip each card into a clear Pro-Fit inner sleeve, then into a standard Deck Protector "
            "for two clear layers of protection during gameplay and storage. Side-loading keeps "
            "cards snug &amp; secure; acid-free film keeps artwork and text fully visible."
        ),
        visual="Banner split: macro of an inner-sleeved card sliding into a deck sleeve left; the 100-count pack right. Black/red Ultra PRO styling.",
        alt="A+ banner on double sleeving with clear side-load inner sleeves inside standard deck sleeves.",
    ),
    AIModule(
        name="Module 4 — Carousel (4 tiles): The sleeving system",
        role="a+_carousel",
        headline="INNER. DECK. BOX. PROTECT.",
        body=(
            "Tile 1: <b>PRO-FIT INNER SLEEVES</b> — Clear side-load inner layer (this product).<br/>"
            "Tile 2: <b>DECK PROTECTOR SLEEVES</b> — Standard outer sleeves for double sleeving.<br/>"
            "Tile 3: <b>DECK BOXES</b> — Store and carry sleeved decks.<br/>"
            "Tile 4: <b>ONE-TOUCH HOLDERS</b> — 35pt rigid protection for standout cards."
        ),
        visual="4 coordinated product tiles, red accent corners, consistent catalog styling.",
        alt="Four A+ tiles showing the Ultra PRO sleeving system: inner sleeves, deck sleeves, deck boxes, ONE-TOUCH.",
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
