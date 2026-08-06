"""Life Code — Stem Cell 100 (60 veg. capsules)  [Produkt 02]
Hand-written, KW-led, COMPLIANCE-FIRST copy (US dietary supplement / Amazon).

Marketplace: amazon.com (US). ASIN B00IPR91P0. Marke: Life Code (Longevity-Science).
Dies ist das ORIGINAL Stem-Cell-&-Telomere-Support-Formula (SC100 blend). Stem Cell 100+
ist die stärkere/erweiterte Version — hier positionieren wir 100 als das Original.

COMPLIANCE-LEITPLANKEN (oberste Priorität):
  - Nur STRUCTURE/FUNCTION-Sprache wie in den Live-Listings: 'designed to support',
    'formulated to support ... pathways', 'supports healthy aging / cellular health'.
  - NIEMALS: cure/treat/prevent/reverse, 'activates stem cells', 'lengthens telomeres',
    'regenerates', 'reverses aging', 'life extension', 'clinically proven', 'doctor-recommended'.
  - KEINE Superlative (best/#1/leading, auch nicht 'best used').
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

PLAN_NO = "02"
ASIN = "B00IPR91P0"
EXCEL = HERE / "listing.xlsx"


TITLE = ('Life Code Stem Cell 100 — Stem Cell & Telomere Support Formula · Healthy Aging '
         'Supplement · Astragalus, Pine Bark OPCs, L-Theanine, Schisandra & He Shou Wu · '
         '60 Vegetarian Capsules · Made in USA')

BULLETS = [
    "<b>STEM CELL &amp; TELOMERE PATHWAY SUPPORT</b> — Stem Cell 100 is the original "
    "stem cell &amp; telomere support formula, formulated to support stem cell and "
    "telomere-related pathways as part of a healthy-aging routine. The SC100 proprietary "
    "blend brings together researched botanicals for daily longevity support.",

    "<b>PROPRIETARY SC100 BOTANICAL BLEND</b> — A researched, plant-based blend of "
    "Astragalus, Pine Bark OPCs, L-Theanine, Schisandra and He Shou Wu — designed to "
    "support multiple aging-related pathways as part of your everyday longevity routine.",

    "<b>ANTIOXIDANT &amp; ADAPTOGEN SUPPORT</b> — Pine Bark OPCs provide antioxidant "
    "support, Astragalus and Schisandra are traditional longevity botanicals, and "
    "L-Theanine supports calm focus — a thoughtfully balanced daily formula.",

    "<b>60 VEGETARIAN CAPSULES · SIMPLE DAILY USE</b> — 100% vegetarian capsules with no "
    "animal-based capsule ingredients. Suggested use is just 2 capsules daily — an easy "
    "addition to your longevity routine.",

    "<b>MADE IN THE USA · GMP · LAB-TESTED</b> — Manufactured in the USA to GMP standards "
    "and laboratory tested for quality you can trust. Backed by Life Code's "
    "longevity-science approach and a 90-day money-back guarantee.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="Clean white with a soft navy-to-light-blue #EEF2F8 base. Identical across all 3 for a clean split test.",
        purpose="Win the click in a crowded longevity-supplement grid — signal premium science + trust instantly.",
        visual=(
            "Mock ALL 3 options. Product exactly as real: the Stem Cell 100 bottle, label "
            "readable, crisp studio light. ONE callout each, bottle dominant ~70%. Navy anchor, "
            "a single disciplined red accent. Amazon slot-1 main = pure white / bottle only.\n\n"
            "OPTION A — PATHWAY SUPPORT (owns the category): bottle centred, a clean stylised "
            "cell + telomere/chromosome motif behind it (abstract, elegant, non-medical). Badge "
            "(navy): 'STEM CELL & TELOMERE SUPPORT'.\n"
            "OPTION B — THE ORIGINAL FORMULA (owns 'proven original'): bottle with a quiet "
            "'ORIGINAL SC100 BLEND' ribbon; Astragalus root, pine bark and Schisandra berries "
            "arranged beside it. Badge: 'THE ORIGINAL FORMULA'.\n"
            "OPTION C — TRUST STACK (defuses 'is it legit?'): bottle + small badge row (Made in "
            "USA · GMP · Vegetarian · Lab-Tested). Badge: 'MADE IN USA · GMP'.\n\n"
            "Across all 3: bottle ~70%, callout ~6%, same lighting + colour temperature."
        ),
        overlay="(one callout per option)",
        overlay_sub="3 hero options shipped — A/B test, keep the winner.",
        props=["A: bottle + abstract cell/telomere motif", "B: bottle + Astragalus/pine bark/Schisandra", "C: bottle + trust-badge row"],
        lighting="Soft, premium studio light (5000K), gentle reflection under the bottle. Same across all 3.",
        why_it_works=(
            "Three triggers: category ownership (pathway support), the proven original formula, "
            "and trust — each compliant and readable at thumbnail size. No disease or reversal claims."
        ),
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: designed to support the pathways of healthy aging",
        role="hook",
        background="Soft light-blue #EEF2F8 with navy headline (clean science look)",
        purpose="State the compliant core promise in one frame — multi-pathway support.",
        visual=(
            "Centre: the bottle. Around it, four clean stylised icons on soft navy discs, each a "
            "supported area drawn from the SC100 blend: 'Cellular health', 'Antioxidant support', "
            "'Calm focus', 'Longevity pathways'. Thin connecting lines from each to the bottle, "
            "like an elegant science infographic. Small caption: 'Formulated to support stem cell "
            "& telomere-related pathways.'"
        ),
        overlay="SUPPORT FOR HEALTHY AGING.",
        overlay_sub="Formulated to support stem cell & telomere-related pathways.",
        props=["bottle", "4 support-area icons on navy discs", "thin connector lines"],
        lighting="Even, clean, editorial. Clarity over drama.",
        why_it_works=(
            "Reviewers say it's hard to connect ingredients to benefits. Naming what the SC100 "
            "blend supports — in the listing's own hedged language — educates and differentiates "
            "while staying fully compliant."
        ),
        cvr="Directly answers the 'how does this actually help me?' hesitation.",
    ),
    AIImagePlanItem(
        name="Image 3 — Inside the SC100 blend",
        role="educate",
        background="White with a navy footer band",
        purpose="Defend the premium: show the researched botanical blend and what each area supports.",
        visual=(
            "Clean ingredient grid. Real photos of the SC100 botanicals with short, honest labels:\n"
            "  • ASTRAGALUS — traditional longevity botanical\n"
            "  • PINE BARK OPCs — antioxidant support\n"
            "  • L-THEANINE — calm focus\n"
            "  • SCHISANDRA — traditional adaptogen botanical\n"
            "  • HE SHOU WU — traditional longevity botanical\n\n"
            "Footer band: 'The original SC100 proprietary blend.' Keep claims to "
            "'support' language only."
        ),
        overlay="5 RESEARCHED INGREDIENTS.",
        overlay_sub="Astragalus, Pine Bark OPCs, L-Theanine, Schisandra & He Shou Wu.",
        props=["botanical ingredient grid (real photos)", "SC100 footer band"],
        lighting="Bright, clean flat-lay light; ingredients appetising and premium.",
        why_it_works=(
            "Buyers value researched, named ingredients. Making the SC100 blend transparent "
            "justifies the price and separates this from vague 'stem cell' products with hidden formulas."
        ),
    ),
    AIImagePlanItem(
        name="Image 4 — 100 vs 100+: the original and the upgrade",
        role="desire",
        background="Soft light-blue #EEF2F8, clean comparison",
        purpose="Position Stem Cell 100 as the established original within the range.",
        visual=(
            "Side-by-side of the two bottles (Stem Cell 100 and Stem Cell 100+), with a clean "
            "'the range' panel: Stem Cell 100 is the original, focused SC100 formula; Stem Cell "
            "100+ is the upgraded, broader formula. A soft navy accent marks Stem Cell 100 as the "
            "original pick. Honest framing — both are good; 100 is the established starting point."
        ),
        overlay="THE ORIGINAL FORMULA.",
        overlay_sub="Stem Cell 100 is the original stem cell & telomere support formula.",
        props=["Stem Cell 100 + 100+ bottles side by side", "'the range' panel", "navy original accent"],
        lighting="Even, clean; true label colours on both bottles.",
        why_it_works=(
            "Shoppers comparing the two need clarity. Showing that 100 is the original, focused "
            "formula (and 100+ the broader upgrade) helps buyers choose confidently and reduces returns."
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
            "medical). Small routine panel: '2 capsules daily · 60 capsules per bottle · designed "
            "for a consistent routine'. Honest note: 'A long-term routine, not an overnight fix.'"
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
            "Life Code Stem Cell 100 is the original formula, formulated to support stem cell "
            "and telomere-related pathways, with a researched SC100 botanical blend designed to "
            "support your everyday healthy-aging routine. Made in the USA, GMP, laboratory tested."
        ),
        visual="Wide clean banner: bottle right, navy headline left on white, an elegant abstract cell/telomere motif. Life Code wordmark upper-left.",
        alt="Life Code Stem Cell 100 banner: formulated to support stem cell and telomere-related pathways, made in the USA.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): Why Stem Cell 100",
        role="a+_carousel",
        headline="WHY STEM CELL 100",
        body=(
            "Tile 1: <b>PATHWAY SUPPORT</b> — Supports stem cell &amp; telomere-related pathways.<br/>"
            "Tile 2: <b>THE ORIGINAL FORMULA</b> — The original SC100 proprietary blend.<br/>"
            "Tile 3: <b>5 RESEARCHED INGREDIENTS</b> — Astragalus, Pine Bark OPCs, L-Theanine &amp; more.<br/>"
            "Tile 4: <b>ANTIOXIDANT &amp; ADAPTOGEN</b> — Pine Bark OPCs, Schisandra &amp; calm focus.<br/>"
            "Tile 5: <b>MADE IN USA</b> — GMP, lab-tested, 100% vegetarian capsules."
        ),
        visual="5 square tiles, navy accent corner each, one disciplined red highlight. Clean science icons.",
        alt="Five A+ tiles: pathway support, original formula, ingredients, antioxidant and adaptogen, made in USA.",
    ),
    AIModule(
        name="Module 3 — Banner: Inside the SC100 blend",
        role="a+_banner",
        headline="THE ORIGINAL SC100 BLEND.",
        body=(
            "The SC100 proprietary blend brings together Astragalus, Pine Bark OPCs, L-Theanine, "
            "Schisandra and He Shou Wu — researched botanicals designed to support multiple "
            "aging-related pathways as part of a daily healthy-aging routine."
        ),
        visual="Banner with a clean botanical ingredient row (real photos + labels): Astragalus, pine bark, Schisandra, He Shou Wu. Navy/white, one red accent.",
        alt="A+ banner showing the original SC100 botanical blend: Astragalus, Pine Bark OPCs, L-Theanine, Schisandra and He Shou Wu.",
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
            "Tile 1: <b>STEM CELL 100</b> — The original stem cell &amp; telomere support formula (this product).<br/>"
            "Tile 2: <b>STEM CELL 100+</b> — The upgraded, broader formula with added vitamins.<br/>"
            "Tile 3: <b>TELOMAX</b> — Telomere-focused botanical support.<br/>"
            "Tile 4: <b>LONGEVITY COMBO</b> — Stem Cell 100+ paired with TeloMax.<br/>"
            "Tile 5: <b>90-DAY GUARANTEE</b> — Try the Life Code approach with confidence."
        ),
        visual="5 tiles: bottles of the range in consistent navy/white styling. This product (Stem Cell 100) gently highlighted.",
        alt="Five A+ tiles of the Life Code longevity range: Stem Cell 100, Stem Cell 100+, TeloMax, Longevity Combo, guarantee.",
    ),
    AIModule(
        name="Module 6 — Premium Q&A",
        role="a+_qa",
        headline="QUESTIONS BEFORE YOU BUY",
        body=(
            "<b>Q.</b> What does Stem Cell 100 do?<br/>"
            "<b>A.</b> It is formulated to support stem cell and telomere-related pathways and to "
            "support aging-related pathways as part of a healthy-aging routine.<br/><br/>"
            "<b>Q.</b> What's inside?<br/>"
            "<b>A.</b> The original SC100 proprietary blend — Astragalus, Pine Bark OPCs, "
            "L-Theanine, Schisandra and He Shou Wu.<br/><br/>"
            "<b>Q.</b> How do I take it?<br/>"
            "<b>A.</b> 2 vegetarian capsules daily. One bottle contains 60 capsules — about a "
            "30-day supply. Designed for consistent, long-term daily use.<br/><br/>"
            "<b>Q.</b> How is Stem Cell 100 different from Stem Cell 100+?<br/>"
            "<b>A.</b> Stem Cell 100 is the original, focused formula. Stem Cell 100+ is the "
            "upgraded version with a broader blend and added vitamins.<br/><br/>"
            "<b>Q.</b> Where is it made?<br/>"
            "<b>A.</b> Made in the USA to GMP standards and laboratory tested. Backed by a 90-day "
            "money-back guarantee."
        ),
        visual="Vertical Q/A table, navy divider lines, small navy Q. and red A. labels.",
        alt="Premium Q&A module for Life Code Stem Cell 100.",
    ),
    AIModule(
        name="Module 7 — Premium Comparison Chart",
        role="a+_comparison",
        headline="CHOOSE YOUR LONGEVITY SUPPORT",
        body=(
            "Four columns: <b>Life Code Stem Cell 100</b> · Stem Cell 100+ · Single-herb "
            "supplement · Basic multivitamin.<br/><br/>"
            "Rows: Supports stem cell &amp; telomere-related pathways · Proprietary SC100 "
            "botanical blend · 5 researched ingredients · Antioxidant &amp; adaptogen support · "
            "100% vegetarian capsules · Made in USA / GMP / lab-tested · 90-day guarantee.<br/><br/>"
            "Highlight the Stem Cell 100 column with a soft navy tint and a 'THE ORIGINAL FORMULA' "
            "ribbon. Comparison columns use category descriptors only — no competitor brands."
        ),
        visual="Standard Amazon Premium Comparison Chart, 4 columns, navy header, Stem Cell 100 column highlighted.",
        alt="Premium comparison chart for Life Code Stem Cell 100 vs Stem Cell 100+, single-herb supplement and basic multivitamin.",
    ),
]


QA = [
    AIQA(q="What is Stem Cell 100 designed to do?",
         a="It is formulated to support stem cell and telomere-related pathways, and designed to support aging-related pathways as part of a healthy-aging routine."),
    AIQA(q="What are the main ingredients?",
         a="The original SC100 proprietary botanical blend: Astragalus, Pine Bark OPCs, L-Theanine, Schisandra and He Shou Wu."),
    AIQA(q="How do I take it, and how long does a bottle last?",
         a="Suggested use is 2 vegetarian capsules daily. Each bottle contains 60 capsules, about a 30-day supply. It is designed for consistent, long-term daily use."),
    AIQA(q="How is Stem Cell 100 different from Stem Cell 100+?",
         a="Stem Cell 100 is the original, focused formula. Stem Cell 100+ is the upgraded, more comprehensive version with a broader botanical blend and added vitamins."),
    AIQA(q="Is it vegetarian?",
         a="Yes. Stem Cell 100 uses 100% vegetarian capsules with no animal-based capsule ingredients."),
    AIQA(q="Where is it made and is it tested?",
         a="It is manufactured in the USA to GMP standards and laboratory tested for quality. Life Code also offers a 90-day money-back guarantee."),
    AIQA(q="When will I notice a difference?",
         a="Stem Cell 100 is a daily longevity-support routine rather than an overnight product. Results vary from person to person, and consistent long-term use is recommended."),
]


BACKEND = (
    "stem cell supplement telomere support longevity healthy aging astragalus pine bark opc "
    "l theanine schisandra he shou wu vegetarian capsules cellular health adaptogen antioxidant "
    "anti aging support made in usa gmp lab tested life code sc100 original formula"
)


def main() -> None:
    print("Lade Life Code + Stem Cell 100 Listing…")
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
