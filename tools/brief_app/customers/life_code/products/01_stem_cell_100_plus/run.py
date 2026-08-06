"""Life Code — Stem Cell 100+ (60 veg. capsules)  [Produkt 01]
Hand-written, KW-led, COMPLIANCE-FIRST copy (US dietary supplement / Amazon).

Marketplace: amazon.com (US). ASIN B00OADCBUU. Marke: Life Code (Longevity-Science).

COMPLIANCE-LEITPLANKEN (oberste Priorität):
  - Nur STRUCTURE/FUNCTION-Sprache wie in den Live-Listings: 'designed to support',
    'formulated to support ... pathways', 'supports healthy aging / cellular health'.
  - NIEMALS: cure/treat/prevent/reverse, 'activates stem cells', 'lengthens telomeres',
    'regenerates', 'reverses aging', 'life extension', 'clinically proven', 'doctor-recommended'.
  - 'Anti-aging' nur als Kategorie-Deskriptor (steht in Amazon-Titeln), kein Wirkversprechen.
  - Keine Krankheits-/Medizin-Bilder, kein before/after, keine Preise/URLs (90-Tage-Garantie ok).
"""
from __future__ import annotations
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
sys.path.insert(0, str(ROOT))

from tools.brief_app.core.customers import load_customer
from tools.brief_app.core.excel_parser import parse_excel
from tools.brief_app.core.pdf_builder import BriefBuilder
from tools.brief_app.core.ai import AIImagePlanItem, AIModule, AIQA

PLAN_NO = "01"
ASIN = "B00OADCBUU"
EXCEL = HERE / "listing.xlsx"


TITLE = ('Life Code Stem Cell 100+ — Stem Cell & Telomere Pathway Support · Healthy Aging '
         'Supplement · Astragalus, Rhodiola, Pine Bark OPCs + D3, B12 & Folate · 60 Vegetarian '
         'Capsules · Made in USA')

BULLETS = [
    "<b>STEM CELL &amp; TELOMERE PATHWAY SUPPORT</b> — Stem Cell 100+ is formulated to support "
    "stem cell and telomere-related pathways as part of a healthy-aging routine. Our upgraded "
    "SC100+ proprietary blend is designed to be more comprehensive than the original Stem Cell 100.",

    "<b>MULTI-PATHWAY BOTANICAL BLEND</b> — A researched, plant-based blend including Astragalus "
    "Membranaceus, Rhodiola Rosea, Pine Bark OPCs, L-Theanine, He Shou Wu, Genistein, Rubus "
    "Chingii and Drynaria — designed to support multiple aging-related pathways: cellular health, "
    "vascular circulation, neural function and autophagy.",

    "<b>PLUS D3, B12 &amp; FOLATE</b> — Includes Vitamin D3, Vitamin B12 and active Folate "
    "(5-MTHF) as additional nutritional ingredients that support everyday wellness and normal "
    "cellular function — a thoughtful, complete daily formula.",

    "<b>60 VEGETARIAN CAPSULES · SIMPLE DAILY USE</b> — 100% vegetarian capsules with no "
    "animal-based capsule ingredients. Suggested use is just 2 capsules daily — an easy addition "
    "to your longevity routine.",

    "<b>MADE IN THE USA · GMP · LAB-TESTED</b> — Manufactured in the USA to GMP standards and "
    "laboratory tested for quality you can trust. Backed by Life Code's longevity-science approach "
    "and a 90-day money-back guarantee.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="Clean white with a soft navy-to-light-blue #EEF2F8 base. Identical across all 3 for a clean split test.",
        purpose="Win the click in a crowded longevity-supplement grid — signal premium science + trust instantly.",
        visual=(
            "Mock ALL 3 options. Product exactly as real: the Stem Cell 100+ bottle, label "
            "readable, crisp studio light. ONE callout each, bottle dominant ~70%. Navy anchor, "
            "a single disciplined red accent. Amazon slot-1 main = pure white / bottle only.\n\n"
            "OPTION A — PATHWAY SUPPORT (owns the category): bottle centred, a clean stylised "
            "cell + telomere/chromosome motif behind it (abstract, elegant, non-medical). Badge "
            "(navy): 'STEM CELL & TELOMERE SUPPORT'.\n"
            "OPTION B — BOTANICAL BLEND (owns 'real ingredients'): bottle with Astragalus root, "
            "Rhodiola and pine bark arranged beside it. Badge: '10+ RESEARCHED BOTANICALS'.\n"
            "OPTION C — TRUST STACK (defuses 'is it legit?'): bottle + small badge row (Made in "
            "USA · GMP · Vegetarian · Lab-Tested). Badge: 'MADE IN USA · GMP'.\n\n"
            "Across all 3: bottle ~70%, callout ~6%, same lighting + colour temperature."
        ),
        overlay="(one callout per option)",
        overlay_sub="3 hero options shipped — A/B test, keep the winner.",
        props=["A: bottle + abstract cell/telomere motif", "B: bottle + Astragalus/Rhodiola/pine bark", "C: bottle + trust-badge row"],
        lighting="Soft, premium studio light (5000K), gentle reflection under the bottle. Same across all 3.",
        why_it_works=(
            "Three triggers: category ownership (pathway support), real botanicals, and trust — "
            "each compliant and readable at thumbnail size. No disease or reversal claims."
        ),
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: designed to support the pathways of healthy aging",
        role="hook",
        background="Soft light-blue #EEF2F8 with navy headline (clean science look)",
        purpose="State the compliant core promise in one frame — multi-pathway support.",
        visual=(
            "Centre: the bottle. Around it, four clean stylised icons on soft navy discs, each a "
            "supported pathway (verbatim-safe from the listing): 'Cellular health', 'Vascular "
            "circulation', 'Neural function', 'Autophagy'. Thin connecting lines from each to the "
            "bottle, like an elegant science infographic. Small caption: 'Formulated to support "
            "stem cell & telomere-related pathways.'"
        ),
        overlay="SUPPORT FOR HEALTHY AGING.",
        overlay_sub="Designed to support cellular health, circulation, neural function & autophagy.",
        props=["bottle", "4 pathway icons on navy discs", "thin connector lines"],
        lighting="Even, clean, editorial. Clarity over drama.",
        why_it_works=(
            "Reviewers say it's hard to connect ingredients to benefits. Naming the four supported "
            "pathways — in the listing's own hedged language — educates and differentiates while "
            "staying fully compliant."
        ),
        cvr="Directly answers the 'how does this actually help me?' hesitation.",
    ),
    AIImagePlanItem(
        name="Image 3 — Inside the SC100+ blend",
        role="educate",
        background="White with a navy footer band",
        purpose="Defend the premium: show the researched botanical blend and what each area supports.",
        visual=(
            "Clean ingredient grid. Real photos of the key botanicals with short, honest labels:\n"
            "  • ASTRAGALUS MEMBRANACEUS — traditional longevity botanical\n"
            "  • RHODIOLA ROSEA — adaptogen\n"
            "  • PINE BARK OPCs — antioxidant support\n"
            "  • L-THEANINE — calm focus\n"
            "  • HE SHOU WU · GENISTEIN · RUBUS CHINGII · DRYNARIA — traditional botanicals\n\n"
            "Footer band: 'Plus Vitamin D3, B12 & active Folate (5-MTHF).' Keep claims to "
            "'support' language only."
        ),
        overlay="10+ RESEARCHED BOTANICALS.",
        overlay_sub="Astragalus, Rhodiola, Pine Bark OPCs, He Shou Wu & more — plus D3, B12 & Folate.",
        props=["botanical ingredient grid (real photos)", "D3/B12/Folate footer band"],
        lighting="Bright, clean flat-lay light; ingredients appetising and premium.",
        why_it_works=(
            "Buyers value researched, named ingredients. Making the blend transparent justifies "
            "the price and separates this from vague 'stem cell' products with hidden formulas."
        ),
    ),
    AIImagePlanItem(
        name="Image 4 — 100+ vs 100: the upgraded formula",
        role="desire",
        background="Soft light-blue #EEF2F8, clean comparison",
        purpose="Position 100+ as the more comprehensive choice within the range.",
        visual=(
            "Side-by-side of the two bottles (Stem Cell 100 and Stem Cell 100+), with a clean "
            "'what's added' panel for 100+: more botanicals in the blend, added D3/B12/Folate, "
            "designed to be more comprehensive. A soft red '+' accent marks the upgraded pick. "
            "Honest framing — both are good; 100+ is the fuller formula."
        ),
        overlay="THE UPGRADED FORMULA.",
        overlay_sub="Stem Cell 100+ builds on Stem Cell 100 with a broader blend plus D3, B12 & Folate.",
        props=["Stem Cell 100 + 100+ bottles side by side", "'what's added' panel", "red + accent"],
        lighting="Even, clean; true label colours on both bottles.",
        why_it_works=(
            "Shoppers comparing the two need a clear reason to choose 100+. Showing the delta "
            "(broader blend + added vitamins) makes the premium choice obvious and lifts AOV."
        ),
    ),
    AIImagePlanItem(
        name="Image 5 — Trust: made in USA, GMP, lab-tested, vegetarian",
        role="trust",
        background="White with soft navy panels behind each badge",
        purpose="Stack the quality signals that make a supplement buyer click 'add to cart'.",
        visual=(
            "Centre bottle, four trust badges in the corners:\n"
            "  • MADE IN THE USA (small flag)\n"
            "  • GMP MANUFACTURED (facility icon)\n"
            "  • LABORATORY TESTED (flask/check icon)\n"
            "  • 100% VEGETARIAN CAPSULES (leaf icon)\n\n"
            "Thin strip: '90-day money-back guarantee · no animal-based capsule ingredients.'"
        ),
        overlay="MADE IN USA. LAB-TESTED.",
        overlay_sub="GMP manufactured · 100% vegetarian capsules · 90-day money-back guarantee.",
        props=["bottle", "4 trust badges", "90-day guarantee strip"],
        lighting="Studio-even; badges legible at thumbnail size.",
        why_it_works=(
            "Supplement trust gaps are quality and legitimacy. Stacking USA + GMP + lab-tested + "
            "vegetarian + guarantee answers every doubt before purchase."
        ),
    ),
    AIImagePlanItem(
        name="Image 6 — Simple daily routine",
        role="desire",
        background="Warm, bright lifestyle — an active, healthy mature adult's morning",
        purpose="Set honest expectations (consistency) and show the easy daily habit.",
        visual=(
            "Lifestyle: a vibrant, healthy adult in their 60s at a bright kitchen counter, taking "
            "their 2 capsules with water alongside breakfast — active, happy, everyday (NOT "
            "medical). Small routine panel: '2 capsules daily · 60 capsules per bottle · best with "
            "a consistent routine'. Honest note: 'A long-term routine, not an overnight fix.'"
        ),
        overlay="2 CAPSULES A DAY.",
        overlay_sub="60 vegetarian capsules — an easy daily step in your longevity routine.",
        props=["healthy 60s adult at kitchen counter", "bottle + 2 capsules + water", "routine panel"],
        lighting="Warm natural morning light. Aspirational, real, vibrant — never clinical.",
        why_it_works=(
            "Reviewers note effects build over time and dislike vague expectations. Framing it "
            "honestly as a consistent daily routine improves satisfaction and repeat purchase — "
            "and shows the aspirational healthy-aging lifestyle."
        ),
    ),
    AIImagePlanItem(
        name="Image 7 — Brand close: Life Code longevity science",
        role="close",
        background="Clean navy brand panel with white space",
        purpose="Close on credibility — a science-led longevity brand.",
        visual=(
            "Bottle with the Life Code wordmark and a calm, premium science motif. Lower band, "
            "three quiet trust points: 'Longevity-science formulas', 'Made in the USA · GMP · "
            "lab-tested', '90-day money-back guarantee'. Tone: credible, disciplined, premium — "
            "no hype."
        ),
        overlay="LONGEVITY, BACKED BY SCIENCE.",
        overlay_sub="Life Code — researched longevity formulas, made in the USA.",
        props=["bottle + Life Code wordmark", "science motif", "3 trust points band"],
        lighting="Premium, even, navy-and-white. Calm and credible.",
        why_it_works=(
            "Against unbranded 'stem cell' supplements, a disciplined science-led brand close is "
            "the trust signal that converts an informed longevity buyer."
        ),
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Brand banner",
        role="a+_banner",
        headline="SUPPORT FOR HEALTHY-AGING PATHWAYS.",
        body=(
            "Life Code Stem Cell 100+ is formulated to support stem cell and telomere-related "
            "pathways, with a researched botanical blend designed to support cellular health, "
            "circulation, neural function and autophagy. Made in the USA, GMP, laboratory tested."
        ),
        visual="Wide clean banner: bottle right, navy headline left on white, an elegant abstract cell/telomere motif. Life Code wordmark upper-left.",
        alt="Life Code Stem Cell 100+ banner: formulated to support stem cell and telomere-related pathways, made in the USA.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): Why Stem Cell 100+",
        role="a+_carousel",
        headline="WHY STEM CELL 100+",
        body=(
            "Tile 1: <b>PATHWAY SUPPORT</b> — Supports stem cell &amp; telomere-related pathways.<br/>"
            "Tile 2: <b>MULTI-PATHWAY BLEND</b> — Cellular health, circulation, neural, autophagy.<br/>"
            "Tile 3: <b>10+ BOTANICALS</b> — Astragalus, Rhodiola, Pine Bark OPCs &amp; more.<br/>"
            "Tile 4: <b>PLUS D3, B12 &amp; FOLATE</b> — Added nutritional support.<br/>"
            "Tile 5: <b>MADE IN USA</b> — GMP, lab-tested, 100% vegetarian capsules."
        ),
        visual="5 square tiles, navy accent corner each, one disciplined red highlight. Clean science icons.",
        alt="Five A+ tiles: pathway support, multi-pathway blend, botanicals, added vitamins, made in USA.",
    ),
    AIModule(
        name="Module 3 — Banner: Inside the SC100+ blend",
        role="a+_banner",
        headline="A RESEARCHED, MULTI-PATHWAY BLEND.",
        body=(
            "The SC100+ proprietary blend brings together Astragalus Membranaceus, Rhodiola Rosea, "
            "Pine Bark OPCs, L-Theanine, He Shou Wu, Genistein and more — plus Vitamin D3, B12 and "
            "active Folate. Designed to support multiple aging-related pathways as part of a daily "
            "healthy-aging routine."
        ),
        visual="Banner with a clean botanical ingredient row (real photos + labels) and the D3/B12/Folate add-ons. Navy/white, one red accent.",
        alt="A+ banner showing the SC100+ botanical blend plus D3, B12 and Folate.",
    ),
    AIModule(
        name="Module 4 — Banner: Quality & trust",
        role="a+_banner",
        headline="MADE IN THE USA. TESTED FOR QUALITY.",
        body=(
            "Manufactured in the USA to GMP standards and laboratory tested. 100% vegetarian "
            "capsules with no animal-based capsule ingredients. Backed by Life Code's "
            "longevity-science approach and a 90-day money-back guarantee."
        ),
        visual="Banner with four trust badges (Made in USA · GMP · Lab-Tested · Vegetarian) around the bottle, and a 90-day guarantee seal. Navy/white.",
        alt="A+ banner with Life Code quality badges: made in USA, GMP, lab-tested, vegetarian, 90-day guarantee.",
    ),
    AIModule(
        name="Module 5 — Carousel (5 tiles): The Life Code longevity range",
        role="a+_carousel",
        headline="THE LIFE CODE RANGE",
        body=(
            "Tile 1: <b>STEM CELL 100+</b> — Upgraded stem cell &amp; telomere pathway support (this product).<br/>"
            "Tile 2: <b>STEM CELL 100</b> — The original stem cell &amp; telomere support formula.<br/>"
            "Tile 3: <b>TELOMAX</b> — Telomere-focused botanical support.<br/>"
            "Tile 4: <b>LONGEVITY COMBO</b> — Stem Cell 100+ paired with TeloMax.<br/>"
            "Tile 5: <b>90-DAY GUARANTEE</b> — Try the Life Code approach with confidence."
        ),
        visual="5 tiles: bottles of the range in consistent navy/white styling. This product gently highlighted.",
        alt="Five A+ tiles of the Life Code longevity range: Stem Cell 100+, Stem Cell 100, TeloMax, Longevity Combo, guarantee.",
    ),
    AIModule(
        name="Module 6 — Premium Q&A",
        role="a+_qa",
        headline="QUESTIONS BEFORE YOU BUY",
        body=(
            "<b>Q.</b> What does Stem Cell 100+ do?<br/>"
            "<b>A.</b> It is formulated to support stem cell and telomere-related pathways and to "
            "support multiple aging-related pathways — cellular health, circulation, neural "
            "function and autophagy — as part of a healthy-aging routine.<br/><br/>"
            "<b>Q.</b> What's inside?<br/>"
            "<b>A.</b> A researched botanical blend (Astragalus, Rhodiola, Pine Bark OPCs, "
            "L-Theanine, He Shou Wu and more) plus Vitamin D3, B12 and active Folate.<br/><br/>"
            "<b>Q.</b> How do I take it?<br/>"
            "<b>A.</b> 2 vegetarian capsules daily. One bottle contains 60 capsules — about a "
            "30-day supply. Designed for consistent, long-term daily use.<br/><br/>"
            "<b>Q.</b> How is 100+ different from Stem Cell 100?<br/>"
            "<b>A.</b> Stem Cell 100+ is the upgraded formula — a broader botanical blend with "
            "added Vitamin D3, B12 and Folate.<br/><br/>"
            "<b>Q.</b> Where is it made?<br/>"
            "<b>A.</b> Made in the USA to GMP standards and laboratory tested. Backed by a 90-day "
            "money-back guarantee."
        ),
        visual="Vertical Q/A table, navy divider lines, small navy Q. and red A. labels.",
        alt="Premium Q&A module for Life Code Stem Cell 100+.",
    ),
    AIModule(
        name="Module 7 — Premium Comparison Chart",
        role="a+_comparison",
        headline="CHOOSE YOUR LONGEVITY SUPPORT",
        body=(
            "Four columns: <b>Life Code Stem Cell 100+</b> · Stem Cell 100 · Single-herb "
            "supplement · Basic multivitamin.<br/><br/>"
            "Rows: Supports stem cell &amp; telomere-related pathways · Multi-pathway botanical "
            "blend · 10+ researched botanicals · Added D3, B12 &amp; Folate · 100% vegetarian "
            "capsules · Made in USA / GMP / lab-tested · 90-day guarantee.<br/><br/>"
            "Highlight the Stem Cell 100+ column with a soft navy tint and a 'MOST COMPREHENSIVE' "
            "ribbon. Comparison columns use category descriptors only — no competitor brands."
        ),
        visual="Standard Amazon Premium Comparison Chart, 4 columns, navy header, Stem Cell 100+ column highlighted.",
        alt="Premium comparison chart for Life Code Stem Cell 100+ vs Stem Cell 100, single-herb supplement and basic multivitamin.",
    ),
]


QA = [
    AIQA(q="What is Stem Cell 100+ designed to do?",
         a="It is formulated to support stem cell and telomere-related pathways, and designed to support multiple aging-related pathways including cellular health, vascular circulation, neural function and autophagy, as part of a healthy-aging routine."),
    AIQA(q="What are the main ingredients?",
         a="An SC100+ proprietary botanical blend including Astragalus Membranaceus, Rhodiola Rosea, Pine Bark OPCs, L-Theanine, He Shou Wu, Genistein, Rubus Chingii and Drynaria, plus Vitamin D3, Vitamin B12 and active Folate (5-MTHF)."),
    AIQA(q="How do I take it, and how long does a bottle last?",
         a="Suggested use is 2 vegetarian capsules daily. Each bottle contains 60 capsules, about a 30-day supply. It is designed for consistent, long-term daily use."),
    AIQA(q="How is Stem Cell 100+ different from Stem Cell 100?",
         a="Stem Cell 100+ is the upgraded, more comprehensive formula, with a broader botanical blend and added Vitamin D3, B12 and Folate compared with the original Stem Cell 100."),
    AIQA(q="Is it vegetarian?",
         a="Yes. Stem Cell 100+ uses 100% vegetarian capsules with no animal-based capsule ingredients."),
    AIQA(q="Where is it made and is it tested?",
         a="It is manufactured in the USA to GMP standards and laboratory tested for quality. Life Code also offers a 90-day money-back guarantee."),
    AIQA(q="When will I notice a difference?",
         a="Stem Cell 100+ is a daily longevity-support routine rather than an overnight product. Results vary from person to person, and consistent long-term use is recommended."),
]


BACKEND = (
    "stem cell supplement telomere support longevity healthy aging astragalus rhodiola pine bark "
    "opc he shou wu l theanine genistein folate 5-mthf vitamin d3 b12 vegetarian capsules cellular "
    "health autophagy adaptogen anti aging support made in usa gmp lab tested life code sc100"
)


def main() -> None:
    print("Lade Life Code + Stem Cell 100+ Listing…")
    cust = load_customer("life_code")
    brief = parse_excel(EXCEL)
    OUT = HERE / f"{PLAN_NO}_{ASIN}_Image Plan.pdf"
    print(f"  Produkt: {brief.product_name}  ASIN: {ASIN}  Marktplatz: {cust.marketplace}")

    builder = BriefBuilder(cust, brief, OUT, ai=None)
    builder._ai_title = TITLE
    builder._ai_bullets = BULLETS
    builder._ai_images = IMAGES
    builder._ai_modules = MODULES
    builder._ai_qa = QA
    builder._ai_backend = BACKEND
    builder.copy_source_label = "Hand-written senior copy (compliance-first, structure/function)"

    print("Baue Branded PDF…")
    pdf_path = builder.build()
    size_kb = pdf_path.stat().st_size // 1024
    import re
    pages = len(re.findall(rb'/Type\s*/Page[^s]', pdf_path.read_bytes()))
    print(f"Gebaut: {pdf_path}")
    print(f"  Seiten: {pages}  Größe: {size_kb} KB")


if __name__ == "__main__":
    main()
