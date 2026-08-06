"""Life Code — TeloMax (60 capsules)  [Produkt 03]
Hand-written, KW-led, COMPLIANCE-FIRST copy (US dietary supplement / Amazon).

Marketplace: amazon.com (US). ASIN B08BXBK77R. Marke: Life Code (Longevity-Science).

COMPLIANCE-LEITPLANKEN (oberste Priorität):
  - Nur STRUCTURE/FUNCTION-Sprache wie in den Live-Listings: 'designed to support',
    'supports telomere maintenance and cellular function', 'supports healthy aging'.
  - 'Multipath Regeneration (MuR)' ist ein PRODUKT-/ENTWICKLUNGSANSATZ (Eigenname) —
    daraus NIEMALS ein 'regenerates cells'-Wirkversprechen ableiten.
  - NIEMALS: cure/treat/prevent/reverse, 'lengthens telomeres', 'activates/increases
    telomerase', 'regenerates cells', 'reverses aging', 'life extension',
    'clinically proven', 'doctor-recommended', 'guaranteed results'.
  - KEINE Superlative (best/#1/leading; auch nicht 'best used' -> 'designed for
    consistent use'). 'Anti-aging' nur als Kategorie-Deskriptor.
  - Lithium Orotate nur als niedrig dosierte ZUTAT (2 mg) nennen — KEINE Wirk-,
    Stimmungs- oder mentale-Gesundheits-Claims.
  - Keine Krankheits-/Medizin-Bilder, kein before/after, keine Preise/URLs
    (90-Tage-Garantie ok).
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

PLAN_NO = "03"
ASIN = "B08BXBK77R"
EXCEL = HERE / "listing.xlsx"


TITLE = ('Life Code TeloMax — Telomere &amp; Cellular Function Support · Healthy Aging '
         'Supplement · Ashwagandha, Gotu Kola, Milk Thistle, Scutellaria &amp; Genistein '
         'Botanical Blend · 60 Capsules · Made in USA')

BULLETS = [
    "<b>TELOMERE &amp; CELLULAR FUNCTION SUPPORT</b> — TeloMax is designed to support "
    "telomere maintenance and cellular function as part of a healthy-aging routine. A "
    "telomere-focused daily formula for informed adults investing in longevity.",

    "<b>MULTIPATH BOTANICAL BLEND</b> — A proprietary blend of standardized herbal "
    "extracts including Ashwagandha, Gotu Kola, Silybum Marianum (Milk Thistle), "
    "Scutellaria Baicalensis, Genistein and Uncaria Tomentosa — developed using Life "
    "Code's Multipath Regeneration (MuR) approach.",

    "<b>STANDARDIZED HERBAL EXTRACTS</b> — Made with standardized botanical extracts for "
    "consistent quality, plus Lithium Orotate at a low supplemental amount (2 mg per "
    "serving). A considered, transparent formula — no hidden proprietary fillers.",

    "<b>60 CAPSULES · SIMPLE DAILY USE</b> — Suggested use is just 2 capsules daily, so "
    "one bottle is about a 30-day supply. Designed for consistent, long-term daily use as "
    "an easy addition to your longevity routine.",

    "<b>MADE IN THE USA · cGMP FACILITY</b> — Manufactured in the USA in a cGMP-certified "
    "facility for quality you can trust. Backed by Life Code's longevity-science approach "
    "and a 90-day money-back guarantee.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="Clean white with a soft navy-to-light-blue #EEF2F8 base. Identical across all 3 for a clean split test.",
        purpose="Win the click in a crowded telomere/longevity grid — signal premium science + trust instantly.",
        visual=(
            "Mock ALL 3 options. Product exactly as real: the TeloMax bottle, label "
            "readable, crisp studio light. ONE callout each, bottle dominant ~70%. Navy "
            "anchor, a single disciplined red accent. Amazon slot-1 main = pure white / "
            "bottle only.\n\n"
            "OPTION A — TELOMERE SUPPORT (owns the category): bottle centred, a clean "
            "stylised telomere/chromosome motif behind it (abstract, elegant, non-medical). "
            "Badge (navy): 'TELOMERE & CELL SUPPORT'.\n"
            "OPTION B — BOTANICAL BLEND (owns 'real ingredients'): bottle with Ashwagandha "
            "root, Gotu Kola and Milk Thistle arranged beside it. Badge: 'MULTIPATH "
            "BOTANICAL BLEND'.\n"
            "OPTION C — TRUST STACK (defuses 'is it legit?'): bottle + small badge row "
            "(Made in USA · cGMP · Lab-Tested · 90-Day Guarantee). Badge: 'MADE IN USA · "
            "cGMP'.\n\n"
            "Across all 3: bottle ~70%, callout ~6%, same lighting + colour temperature."
        ),
        overlay="(one callout per option)",
        overlay_sub="3 hero options shipped — A/B test, keep the winner.",
        props=["A: bottle + abstract telomere/chromosome motif", "B: bottle + Ashwagandha/Gotu Kola/Milk Thistle", "C: bottle + trust-badge row"],
        lighting="Soft, premium studio light (5000K), gentle reflection under the bottle. Same across all 3.",
        why_it_works=(
            "Three triggers: category ownership (telomere support), real botanicals, and "
            "trust — each compliant and readable at thumbnail size. No disease, reversal or "
            "telomere-lengthening claims."
        ),
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: designed to support telomere maintenance & cellular function",
        role="hook",
        background="Soft light-blue #EEF2F8 with navy headline (clean science look)",
        purpose="State the compliant core promise in one frame — telomere & cellular support.",
        visual=(
            "Centre: the bottle. Around it, four clean stylised icons on soft navy discs, "
            "each a supported area (verbatim-safe from the listing): 'Telomere "
            "maintenance', 'Cellular function', 'Healthy aging', 'Everyday vitality'. Thin "
            "connecting lines from each to the bottle, like an elegant science infographic. "
            "Small caption: 'Designed to support telomere maintenance & cellular "
            "function.'"
        ),
        overlay="TELOMERE & CELL SUPPORT.",
        overlay_sub="Designed to support telomere maintenance & cellular function every day.",
        props=["bottle", "4 support-area icons on navy discs", "thin connector lines"],
        lighting="Even, clean, editorial. Clarity over drama.",
        why_it_works=(
            "Telomere shoppers want to know what the product actually supports. Naming the "
            "supported areas in the listing's own hedged language educates and "
            "differentiates while staying fully compliant."
        ),
        cvr="Directly answers the 'what does this actually support?' hesitation.",
    ),
    AIImagePlanItem(
        name="Image 3 — Inside the TeloMax blend",
        role="educate",
        background="White with a navy footer band",
        purpose="Defend the premium: show the standardized botanical blend and what it supports.",
        visual=(
            "Clean ingredient grid. Real photos of the key botanicals with short, honest "
            "labels:\n"
            "  • ASHWAGANDHA — traditional adaptogen\n"
            "  • GOTU KOLA — traditional longevity botanical\n"
            "  • MILK THISTLE (SILYBUM MARIANUM) — traditional botanical\n"
            "  • SCUTELLARIA BAICALENSIS — traditional botanical\n"
            "  • GENISTEIN · UNCARIA TOMENTOSA — plant extracts\n\n"
            "Footer band: 'Plus Lithium Orotate at a low supplemental amount (2 mg per "
            "serving).' Keep claims to 'support' language only — no ingredient effect "
            "claims."
        ),
        overlay="MULTIPATH BOTANICAL BLEND.",
        overlay_sub="Ashwagandha, Gotu Kola, Milk Thistle, Scutellaria & Genistein — standardized extracts.",
        props=["botanical ingredient grid (real photos)", "Lithium Orotate 2 mg footer band"],
        lighting="Bright, clean flat-lay light; ingredients appetising and premium.",
        why_it_works=(
            "Buyers value standardized, named ingredients. Making the blend transparent "
            "justifies the price and separates this from vague telomere products with "
            "hidden formulas."
        ),
    ),
    AIImagePlanItem(
        name="Image 4 — The Multipath (MuR) approach",
        role="desire",
        background="Soft light-blue #EEF2F8, clean science layout",
        purpose="Explain the brand's development approach without over-claiming.",
        visual=(
            "Elegant, honest infographic: the bottle with several thin lines fanning out "
            "to the botanical extracts in the blend, converging on two calm labels — "
            "'Telomere maintenance' and 'Cellular function'. A small note: 'Developed "
            "using Life Code's Multipath Regeneration (MuR) approach — a multi-botanical "
            "formula designed to support healthy-aging pathways.' Abstract and premium — "
            "NOT medical, no cell-division animation, no 'regenerates' language."
        ),
        overlay="MULTIPATH SUPPORT APPROACH.",
        overlay_sub="A multi-botanical formula designed to support healthy-aging pathways.",
        props=["bottle", "fan-out lines to botanicals", "two calm support-area labels"],
        lighting="Even, clean; true label colours on the bottle.",
        why_it_works=(
            "Informed longevity buyers want to understand the thinking behind a formula. "
            "Framing the MuR approach as a multi-botanical design — not an outcome — "
            "educates and differentiates while staying compliant."
        ),
    ),
    AIImagePlanItem(
        name="Image 5 — Trust: made in USA, cGMP, lab-tested",
        role="trust",
        background="White with soft navy panels behind each badge",
        purpose="Stack the quality signals that make a supplement buyer click 'add to cart'.",
        visual=(
            "Centre bottle, four trust badges in the corners:\n"
            "  • MADE IN THE USA (small flag)\n"
            "  • cGMP-CERTIFIED FACILITY (facility icon)\n"
            "  • LABORATORY TESTED (flask/check icon)\n"
            "  • 90-DAY GUARANTEE (seal icon)\n\n"
            "Thin strip: 'Manufactured in the USA in a cGMP-certified facility · 90-day "
            "money-back guarantee.'"
        ),
        overlay="MADE IN USA. cGMP.",
        overlay_sub="cGMP-certified facility · laboratory tested · 90-day money-back guarantee.",
        props=["bottle", "4 trust badges", "90-day guarantee strip"],
        lighting="Studio-even; badges legible at thumbnail size.",
        why_it_works=(
            "Supplement trust gaps are quality and legitimacy. Stacking USA + cGMP + "
            "lab-tested + guarantee answers every doubt before purchase."
        ),
    ),
    AIImagePlanItem(
        name="Image 6 — Simple daily routine",
        role="desire",
        background="Warm, bright lifestyle — an active, healthy mature adult's morning",
        purpose="Set honest expectations (consistency) and show the easy daily habit.",
        visual=(
            "Lifestyle: a vibrant, healthy adult in their 60s at a bright kitchen counter, "
            "taking their 2 capsules with water alongside breakfast — active, happy, "
            "everyday (NOT medical). Small routine panel: '2 capsules daily · 60 capsules "
            "per bottle · designed for consistent use'. Honest note: 'A long-term routine, "
            "not an overnight fix.'"
        ),
        overlay="2 CAPSULES A DAY.",
        overlay_sub="60 capsules — an easy daily step in your longevity routine.",
        props=["healthy 60s adult at kitchen counter", "bottle + 2 capsules + water", "routine panel"],
        lighting="Warm natural morning light. Aspirational, real, vibrant — never clinical.",
        why_it_works=(
            "Reviewers note effects build over time and dislike vague expectations. "
            "Framing it honestly as a consistent daily routine improves satisfaction and "
            "repeat purchase — and shows the aspirational healthy-aging lifestyle."
        ),
    ),
    AIImagePlanItem(
        name="Image 7 — Brand close: Life Code longevity science",
        role="close",
        background="Clean navy brand panel with white space",
        purpose="Close on credibility — a science-led longevity brand.",
        visual=(
            "Bottle with the Life Code wordmark and a calm, premium science motif. Lower "
            "band, three quiet trust points: 'Longevity-science formulas', 'Made in the "
            "USA · cGMP · lab-tested', '90-day money-back guarantee'. Tone: credible, "
            "disciplined, premium — no hype."
        ),
        overlay="LONGEVITY, BACKED BY SCIENCE.",
        overlay_sub="Life Code — researched longevity formulas, made in the USA.",
        props=["bottle + Life Code wordmark", "science motif", "3 trust points band"],
        lighting="Premium, even, navy-and-white. Calm and credible.",
        why_it_works=(
            "Against unbranded telomere supplements, a disciplined science-led brand close "
            "is the trust signal that converts an informed longevity buyer."
        ),
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Brand banner",
        role="a+_banner",
        headline="SUPPORT FOR HEALTHY AGING.",
        body=(
            "Life Code TeloMax is designed to support telomere maintenance and cellular "
            "function, with a proprietary blend of standardized botanical extracts. Made "
            "in the USA in a cGMP-certified facility."
        ),
        visual="Wide clean banner: bottle right, navy headline left on white, an elegant abstract telomere/chromosome motif. Life Code wordmark upper-left.",
        alt="Life Code TeloMax banner: designed to support telomere maintenance and cellular function, made in the USA.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): Why TeloMax",
        role="a+_carousel",
        headline="WHY TELOMAX",
        body=(
            "Tile 1: <b>TELOMERE SUPPORT</b> — Designed to support telomere maintenance &amp; cellular function.<br/>"
            "Tile 2: <b>MULTIPATH BLEND</b> — Ashwagandha, Gotu Kola, Milk Thistle &amp; more.<br/>"
            "Tile 3: <b>STANDARDIZED EXTRACTS</b> — Standardized herbal extracts for consistent quality.<br/>"
            "Tile 4: <b>2 CAPSULES A DAY</b> — 60 capsules, designed for consistent daily use.<br/>"
            "Tile 5: <b>MADE IN USA</b> — cGMP-certified facility, laboratory tested."
        ),
        visual="5 square tiles, navy accent corner each, one disciplined red highlight. Clean science icons.",
        alt="Five A+ tiles: telomere support, multipath blend, standardized extracts, daily use, made in USA.",
    ),
    AIModule(
        name="Module 3 — Banner: Inside the TeloMax blend",
        role="a+_banner",
        headline="A MULTIPATH BOTANICAL BLEND.",
        body=(
            "The TeloMax blend brings together standardized extracts of Ashwagandha, Gotu "
            "Kola, Milk Thistle, Scutellaria Baicalensis, Genistein and Uncaria Tomentosa "
            "— plus Lithium Orotate (2 mg per serving). Developed using Life Code's "
            "Multipath Regeneration (MuR) approach."
        ),
        visual="Banner with a clean botanical ingredient row (real photos + labels) and the Lithium Orotate 2 mg note. Navy/white, one red accent.",
        alt="A+ banner showing the TeloMax botanical blend plus Lithium Orotate at a low supplemental amount.",
    ),
    AIModule(
        name="Module 4 — Banner: Quality & trust",
        role="a+_banner",
        headline="MADE IN THE USA. cGMP TESTED.",
        body=(
            "Manufactured in the USA in a cGMP-certified facility and laboratory tested for "
            "quality. Backed by Life Code's longevity-science approach and a 90-day "
            "money-back guarantee."
        ),
        visual="Banner with four trust badges (Made in USA · cGMP · Lab-Tested · 90-Day Guarantee) around the bottle. Navy/white.",
        alt="A+ banner with Life Code quality badges: made in USA, cGMP, lab-tested, 90-day guarantee.",
    ),
    AIModule(
        name="Module 5 — Carousel (5 tiles): The Life Code longevity range",
        role="a+_carousel",
        headline="THE LIFE CODE RANGE",
        body=(
            "Tile 1: <b>TELOMAX</b> — Telomere-focused botanical support (this product).<br/>"
            "Tile 2: <b>STEM CELL 100+</b> — Upgraded stem cell &amp; telomere pathway support.<br/>"
            "Tile 3: <b>STEM CELL 100</b> — The original stem cell &amp; telomere support formula.<br/>"
            "Tile 4: <b>LONGEVITY COMBO</b> — Stem Cell 100+ paired with TeloMax.<br/>"
            "Tile 5: <b>90-DAY GUARANTEE</b> — Try the Life Code approach with confidence."
        ),
        visual="5 tiles: bottles of the range in consistent navy/white styling. TeloMax gently highlighted.",
        alt="Five A+ tiles of the Life Code longevity range: TeloMax, Stem Cell 100+, Stem Cell 100, Longevity Combo, guarantee.",
    ),
    AIModule(
        name="Module 6 — Premium Q&A",
        role="a+_qa",
        headline="QUESTIONS BEFORE YOU BUY",
        body=(
            "<b>Q.</b> What does TeloMax do?<br/>"
            "<b>A.</b> It is designed to support telomere maintenance and cellular function "
            "as part of a healthy-aging routine.<br/><br/>"
            "<b>Q.</b> What's inside?<br/>"
            "<b>A.</b> A proprietary blend of standardized herbal extracts — Ashwagandha, "
            "Gotu Kola, Milk Thistle, Scutellaria Baicalensis, Genistein and Uncaria "
            "Tomentosa — plus Lithium Orotate (2 mg per serving).<br/><br/>"
            "<b>Q.</b> How do I take it?<br/>"
            "<b>A.</b> 2 capsules daily. One bottle contains 60 capsules — about a 30-day "
            "supply, designed for consistent daily use.<br/><br/>"
            "<b>Q.</b> What is the Multipath Regeneration (MuR) approach?<br/>"
            "<b>A.</b> Life Code's development approach — a multi-botanical formula designed "
            "to support healthy-aging pathways.<br/><br/>"
            "<b>Q.</b> Where is it made?<br/>"
            "<b>A.</b> Made in the USA in a cGMP-certified facility and laboratory tested, "
            "with a 90-day money-back guarantee."
        ),
        visual="Vertical Q/A table, navy divider lines, small navy Q. and red A. labels.",
        alt="Premium Q&A module for Life Code TeloMax.",
    ),
    AIModule(
        name="Module 7 — Premium Comparison Chart",
        role="a+_comparison",
        headline="CHOOSE YOUR LONGEVITY SUPPORT",
        body=(
            "Four columns: <b>Life Code TeloMax</b> · Stem Cell 100+ · Single-herb "
            "supplement · Basic multivitamin.<br/><br/>"
            "Rows: Supports telomere maintenance &amp; cellular function · Multipath "
            "botanical blend · Standardized herbal extracts · Lithium Orotate (2 mg) · "
            "2 capsules daily · Made in USA / cGMP / lab-tested · 90-day guarantee.<br/><br/>"
            "Highlight the TeloMax column with a soft navy tint and a 'TELOMERE-FOCUSED' "
            "ribbon. Comparison columns use category descriptors only — no competitor "
            "brands."
        ),
        visual="Standard Amazon Premium Comparison Chart, 4 columns, navy header, TeloMax column highlighted.",
        alt="Premium comparison chart for Life Code TeloMax vs Stem Cell 100+, single-herb supplement and basic multivitamin.",
    ),
]


QA = [
    AIQA(q="What is TeloMax designed to do?",
         a="It is designed to support telomere maintenance and cellular function as part of a healthy-aging routine."),
    AIQA(q="What are the main ingredients?",
         a="A proprietary blend of standardized botanical extracts including Ashwagandha, Gotu Kola, Silybum Marianum (Milk Thistle), Scutellaria Baicalensis, Genistein and Uncaria Tomentosa, plus Lithium Orotate at a low supplemental amount (2 mg per serving)."),
    AIQA(q="How do I take it, and how long does a bottle last?",
         a="Suggested use is 2 capsules daily. Each bottle contains 60 capsules, about a 30-day supply. It is designed for consistent, long-term daily use."),
    AIQA(q="What is the Multipath Regeneration (MuR) approach?",
         a="It is Life Code's development approach for TeloMax — a multi-botanical formula designed to support healthy-aging pathways. It names the approach, not a promised outcome."),
    AIQA(q="How much Lithium Orotate is in it?",
         a="TeloMax includes Lithium Orotate at a low supplemental amount of 2 mg per serving, as one ingredient within the blend."),
    AIQA(q="Where is it made and is it tested?",
         a="It is manufactured in the USA in a cGMP-certified facility and laboratory tested for quality. Life Code also offers a 90-day money-back guarantee."),
    AIQA(q="When will I notice a difference?",
         a="TeloMax is a daily longevity-support routine rather than an overnight product. Results vary from person to person, and consistent long-term use is recommended."),
]


BACKEND = (
    "telomere supplement telomere support healthy aging longevity supplement cellular "
    "function ashwagandha gotu kola milk thistle silybum marianum scutellaria baicalensis "
    "genistein uncaria tomentosa cats claw lithium orotate standardized herbal extract "
    "botanical blend adaptogen anti aging support made in usa cgmp lab tested capsules "
    "life code telomax multipath"
)


def main() -> None:
    print("Lade Life Code + TeloMax Listing…")
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
