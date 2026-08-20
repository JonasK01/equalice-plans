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
from tools.brief_app.core.seo_loader import load_seo, as_bullets_html

PLAN_NO = "03"
ASIN = "B08BXBK77R"
EXCEL = HERE / "listing.xlsx"


# Title and bullets are NOT defined here. They come from listing.xlsx, which is the SEO
# axis for this plan and the only approved source for on-listing copy. They used to be
# hand-written constants at this spot and had drifted from the sheet, which is how
# unverified ingredients reached a live dietary-supplement listing. Deleted rather than
# kept as a fallback: a fallback is just a slower way to ship the same error.


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="Clean white with a soft #EEF2F8 base. Identical across all 3 for a clean split test.",
        purpose="Win the click against telomere products that all look and sound the same.",
        layout="clean_hero",
        graphics=[],
        visual=(
            "Mock ALL 3 options. Bottle exactly as real, label readable, dominant at ~70%. One "
            "callout each, navy anchor with a single red accent. Amazon slot-1 stays pure white "
            "and product only.\n\n"
            "OPTION A — THE BLEND (owns real ingredients): bottle with ashwagandha root, gotu "
            "kola leaf and milk thistle arranged beside it. Badge (navy): 'SIX BOTANICALS'.\n"
            "OPTION B — THE FORMULATOR (owns credibility): bottle with a small portrait chip and "
            "'Dr. Bryant Villeponteau, Ph.D.'. Badge: 'FORMULATED BY A SCIENTIST'.\n"
            "OPTION C — THE CATEGORY (owns the search): bottle centred with a clean abstract "
            "chromosome-cap motif behind it. Badge: 'TELOMERE SUPPORT'.\n\n"
            "Across all 3: bottle ~70%, callout ~6%, identical lighting and colour temperature."
        ),
        overlay="(one callout per option)",
        overlay_sub="Three hero options shipped. A/B test them and keep the winner.",
        props=["A: bottle + botanicals", "B: bottle + founder chip", "C: bottle + telomere motif"],
        lighting="Soft premium studio light 5000K, gentle reflection under the bottle. Same across all 3.",
        why_it_works=(
            "Three different reasons to click: real named ingredients, a named formulator, and "
            "plain category recognition for the shopper who searched 'telomere supplement'."
        ),
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: what a telomere actually is",
        role="hook",
        background="Deep navy #14294D, one clean illustration, generous negative space.",
        purpose="Teach the thing the shopper is buying. Most rivals assume it and lose them.",
        layout="cutaway",
        graphics=[
            "one chromosome drawn large and clean across the upper two thirds, its two caps "
            "picked out in red #C8202F",
            "leader line to the cap with the label 'telomere: the protective cap'",
            "beneath it a short three-step strip: 'cell divides' arrow 'cap shortens' arrow "
            "'this happens to everyone'",
            "bottle bottom-right at 20% height, small",
        ],
        visual=(
            "A single clean chromosome with its caps highlighted, one label, one three-step "
            "strip beneath. Elegant science illustration, never a medical diagram."
        ),
        overlay="TELOMERES SHORTEN WITH AGE.",
        overlay_sub="They are the caps on your chromosomes. TeloMax supports telomere health.",
        props=["chromosome illustration", "three-step strip", "bottle"],
        lighting="Flat vector illustration on navy. No photographic lighting in this tile.",
        why_it_works=(
            "Shoppers search 'telomere supplement' without being able to say what a telomere is, "
            "and every rival skips the explanation. Teaching it in one frame earns the authority "
            "that makes the rest of the page credible. The biology stated here is textbook and "
            "carries no claim; the product line stays strictly at 'supports telomere health'."
        ),
        cvr="Answers the question the shopper is too unsure to ask.",
    ),
    AIImagePlanItem(
        name="Image 3 — Inside the TX100 blend",
        role="educate",
        background="White, generous margins, one soft #EEF2F8 field behind the bottle.",
        purpose="Make the formula concrete and checkable against the label.",
        layout="hub_and_spokes",
        graphics=[
            "bottle centred, occupying the middle third",
            "six labelled nodes evenly spaced around it, hairline navy leader lines to the bottle",
            "nodes: WITHANIA SOMNIFERA (ashwagandha), GOTU KOLA, SILYBUM MARIANUM (milk thistle), "
            "SCUTELLARIA BAICALENSIS, GENISTEIN, UNCARIA TOMENTOSA (cat's claw)",
            "small navy chip above the bottle reading 'TX100 proprietary blend'",
        ],
        visual=(
            "Six named botanicals ringed around the bottle with leader lines. Real botanical "
            "photography in each node, common name large and latin name small."
        ),
        overlay="SIX BOTANICALS. ONE BLEND.",
        overlay_sub="Ashwagandha, gotu kola, milk thistle, scutellaria, genistein, cat's claw.",
        props=["bottle", "six botanical nodes", "TX100 chip"],
        lighting="Bright, clean, flat-lay quality on the botanicals; bottle lit as studio product.",
        why_it_works=(
            "A named count is checkable against the label where 'botanical blend' is not, and "
            "several of these are botanicals the shopper already recognises and trusts. "
            "Specificity is the entire trust argument for a proprietary blend."
        ),
    ),
    AIImagePlanItem(
        name="Image 4 — The daily routine",
        role="desire",
        background="Warm, bright kitchen counter in morning light. Real, never clinical.",
        purpose="Set honest expectations and show how small the daily step is.",
        layout="hand_in_frame",
        graphics=[
            "two capsules held in an open palm in the lower left third, at true scale beside a "
            "water glass so capsule size reads honestly",
            "navy routine strip across the top third: '2 capsules daily · 60 per bottle'",
            "one grey honesty line beneath: 'A long term routine, not an overnight change.'",
        ],
        visual=(
            "A real adult at a bright counter taking the two capsules with breakfast. Active and "
            "everyday, never medical."
        ),
        overlay="TWO CAPSULES A DAY.",
        overlay_sub="60 vegetarian capsules. One easy step in a long term routine.",
        props=["bottle", "two capsules in palm", "water glass", "routine strip"],
        lighting="Warm natural morning light. Aspirational and real.",
        why_it_works=(
            "Longevity buyers ask how long before anything happens. Saying plainly that it is a "
            "long term routine protects the review average and lifts repeat purchase."
        ),
    ),
    AIImagePlanItem(
        name="Image 5 — Who formulated this",
        role="trust",
        background="Soft #EEF2F8, one white card stack, generous margins.",
        purpose="Put a named scientist behind the bottle. The listing's biggest unused asset.",
        layout="why_us",
        graphics=[
            "three white reason cards stacked with 24 px gaps, each with a navy #14294D left rule",
            "card 1: 'Dr. Bryant Villeponteau, Ph.D.' with 'molecular biology and longevity "
            "science' beneath, portrait at 120 px (CLIENT TO SUPPLY)",
            "card 2: 'TX100: six named botanicals, no hidden filler list'",
            "card 3: 'Made in the USA in a GMP facility, tested for purity and potency'",
            "bottle bottom-right at 25% height, no badge",
        ],
        visual=(
            "Three proof cards, not a badge wall. Each carries one checkable fact rather than "
            "an adjective."
        ),
        overlay="BUILT BY A SCIENTIST.",
        overlay_sub="Dr. Bryant Villeponteau, Ph.D. Molecular biology and longevity science.",
        props=["bottle", "three reason cards", "founder portrait (to be supplied)"],
        lighting="Even, calm, premium. Portrait lit softly, never corporate stock.",
        why_it_works=(
            "Telomere supplements are a category thick with anonymous white-label bottles. A "
            "named researcher is the fastest way to separate this one, and the credential is "
            "already on the listing."
        ),
    ),
    AIImagePlanItem(
        name="Image 6 — TeloMax or Stem Cell 100?",
        role="desire",
        background="Soft #EEF2F8, two clean columns.",
        purpose="Help the shopper choose inside the range instead of bouncing to compare.",
        layout="comparison_columns",
        graphics=[
            "two equal columns, thin grey divider, a bottle standing at the top of each",
            "LEFT header 'TELOMAX', RIGHT header 'STEM CELL 100'",
            "three criterion rows down both: main focus, blend, take them together",
            "row 3 spans both columns with a single navy line: 'Many customers take both.'",
        ],
        visual=(
            "Two columns, the same criteria down both sides, the difference carried by the row "
            "labels rather than by extra copy."
        ),
        overlay="TELOMAX OR STEM CELL 100?",
        overlay_sub="TeloMax focuses on telomere health. SC100 works on the stem cell niche.",
        props=["TeloMax bottle", "Stem Cell 100 bottle", "three-row criteria table"],
        lighting="Even, clean; true label colours on both bottles.",
        why_it_works=(
            "A shopper deciding between two products from the same brand usually leaves to "
            "compare and does not come back. Answering it on the creative keeps the decision on "
            "the listing, and the 'many take both' line raises basket size honestly."
        ),
    ),
    AIImagePlanItem(
        name="Image 7 — Brand close",
        role="close",
        background="Navy #14294D panel with generous white space.",
        purpose="Close on the one thing this brand can say that rivals cannot.",
        layout="brand_close",
        graphics=[
            "Life Code wordmark centred in the top third",
            "bottle centred beneath it at 45% frame height",
            "lower band split into three equal cells by hairline white rules: "
            "'Named botanicals', 'A named formulator', 'Made in the USA'",
        ],
        visual=(
            "Calm, premium, disciplined. The three closing facts sit in equal cells so none "
            "shouts louder than the others."
        ),
        overlay="SCIENCE YOU CAN CHECK.",
        overlay_sub="Named botanicals, a named formulator, made in the USA in a GMP facility.",
        props=["bottle + Life Code wordmark", "three-cell fact band"],
        lighting="Premium, even, navy and white. Calm and credible.",
        why_it_works=(
            "'Backed by science' is the emptiest phrase in this category and every rival uses "
            "it. Naming what can be checked is the opposite claim and the brand's real position."
        ),
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Brand banner",
        role="a+_banner",
        headline="SUPPORT FOR TELOMERE HEALTH.",
        body=(
            "TeloMax supports telomere health and cellular wellness. Made in the USA in a GMP "
            "facility, tested for purity."
        ),
        visual=("DESKTOP 1464x600, white. LEFT 55%: navy headline, one support line, Life Code "
                "wordmark above. RIGHT 45%: bottle on soft #EEF2F8 with an abstract chromosome-cap "
                "motif behind. MOBILE 600x450: bottle top, headline beneath, inside the safe area."),
        alt="Life Code TeloMax brand banner: support for telomere health and cellular wellness.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): Why TeloMax",
        role="a+_carousel",
        headline="WHY TELOMAX",
        body=(
            "Tile 1: <b>TELOMERE SUPPORT</b> Supports telomere health and cellular wellness.<br/>"
            "Tile 2: <b>TX100 BLEND</b> Six named botanicals, nothing hidden.<br/>"
            "Tile 3: <b>A NAMED FORMULATOR</b> Dr. Bryant Villeponteau, Ph.D.<br/>"
            "Tile 4: <b>MADE IN USA</b> GMP facility, tested for purity and potency.<br/>"
            "Tile 5: <b>60 CAPSULES</b> Two a day, a 30 day supply."
        ),
        visual=("Five square tiles, navy accent corner on each, one red highlight on tile 3. "
                "Line icons only, no stock photography. MOBILE: one tile per swipe."),
        alt="Five A+ tiles: telomere support, the TX100 blend, the formulator, made in USA, 60 capsules.",
    ),
    AIModule(
        name="Module 3 — Banner: what a telomere is",
        role="a+_banner",
        headline="THE CAPS ON YOUR CHROMOSOMES.",
        body=(
            "Telomeres protect the ends of your chromosomes and shorten as cells divide. "
            "TeloMax supports telomere health."
        ),
        visual=("DESKTOP 1464x600, navy #14294D. LEFT 60%: one large clean chromosome, caps in "
                "red #C8202F, leader line labelled 'telomere'. RIGHT 40%: three-step strip 'cell "
                "divides / cap shortens / happens to everyone', bottle small beneath. MOBILE "
                "600x450: chromosome top, strip beneath, label inside the safe area."),
        alt="A+ banner explaining that telomeres are the protective caps on chromosomes.",
    ),
    AIModule(
        name="Module 4 — Carousel (5 tiles): Inside the TX100 blend",
        role="a+_carousel",
        headline="INSIDE THE TX100 BLEND",
        body=(
            "Tile 1: <b>ASHWAGANDHA</b> Withania somnifera.<br/>"
            "Tile 2: <b>GOTU KOLA</b> Centella asiatica.<br/>"
            "Tile 3: <b>MILK THISTLE</b> Silybum marianum.<br/>"
            "Tile 4: <b>SCUTELLARIA</b> Baicalensis, plus genistein.<br/>"
            "Tile 5: <b>CAT'S CLAW</b> Uncaria tomentosa."
        ),
        visual=("Five tiles, real botanical photography on white, latin name small beneath the "
                "common name. MOBILE: one botanical per swipe."),
        alt="Five A+ tiles naming the six botanicals in the TX100 blend.",
    ),
    AIModule(
        name="Module 5 — Banner: TeloMax or Stem Cell 100",
        role="a+_banner",
        headline="WHICH ONE IS FOR YOU?",
        body=(
            "TeloMax focuses on telomere health. Stem Cell 100 works on the stem cell niche. "
            "Many customers take both."
        ),
        visual=("DESKTOP 1464x600, soft #EEF2F8. Two equal columns, thin grey divider, a bottle "
                "at the top of each, headers 'TELOMAX' and 'STEM CELL 100', three criterion rows "
                "beneath, the last spanning both. MOBILE 600x450: columns stack, divider becomes "
                "a horizontal rule."),
        alt="A+ banner comparing TeloMax and Stem Cell 100 so the shopper can choose.",
    ),
    AIModule(
        name="Module 6 — Banner: who formulated this",
        role="a+_banner",
        headline="BUILT BY A SCIENTIST.",
        body=(
            "Life Code was co-founded by Dr. Bryant Villeponteau, Ph.D., whose background is in "
            "molecular biology and longevity science."
        ),
        visual=("DESKTOP 1464x600, white. LEFT 40%: founder portrait in a soft #EEF2F8 card, name "
                "and credential beneath (CLIENT TO SUPPLY). RIGHT 60%: two stacked proof cards "
                "with navy left rules, 'six named botanicals' and 'USA, GMP, tested for purity', "
                "bottle small bottom-right. MOBILE 600x450: portrait card top, cards beneath."),
        alt="A+ banner introducing Life Code co-founder Dr. Bryant Villeponteau, Ph.D.",
    ),
    AIModule(
        name="Module 7 — Premium Q&A",
        role="a+_qa",
        headline="QUESTIONS BEFORE YOU BUY",
        body="",   # rendered from the QA list below
        visual="Vertical Q and A table, navy divider lines, small navy Q. and red A. labels.",
        alt="Premium Q&A module for Life Code TeloMax.",
    ),
]


# House standard: exactly 5 pairs, question <=80 chars, answer <=120.
#
# Cut from seven. Two answers described Lithium Orotate at 2 mg per serving. No source the
# client has supplied confirms it for this product, and lithium is not an ingredient to name
# on a listing from memory, so it is out of the copy and into the open questions in
# SOURCE_NOTES.md until the client sends the label. The "Multipath Regeneration (MuR)"
# answer is gone too: it explained an internal name rather than answering a buyer.
QA = [
    AIQA(q="What is TeloMax designed to do?",
         a="It supports telomere health and cellular wellness as part of a healthy aging "
           "routine."),
    AIQA(q="What are the main ingredients?",
         a="The TX100 blend: ashwagandha, gotu kola, milk thistle, scutellaria, genistein and "
           "cat's claw."),
    AIQA(q="What is a telomere?",
         a="The protective cap on the end of a chromosome. Telomeres shorten as your cells "
           "divide."),
    AIQA(q="How is TeloMax different from Stem Cell 100?",
         a="TeloMax focuses on telomere health. Stem Cell 100 works on the stem cell "
           "micro-environment."),
    AIQA(q="How do I take it, and how long does a bottle last?",
         a="Two capsules daily. 60 capsules per bottle, about a 30 day supply."),
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
    # Title and bullets come 1:1 from the SEO sheet, which is the axis for this plan.
    seo = load_seo(EXCEL)
    builder._ai_title = seo.title
    builder._ai_bullets = as_bullets_html(seo)
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
