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
from tools.brief_app.core.seo_loader import load_seo, as_bullets_html

PLAN_NO = "02"
ASIN = "B00IPR91P0"
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
        background="Clean white with a soft #EEF2F8 base. Identical across all 3 so the split test isolates composition.",
        purpose="Win the click in a grid where every rival says the same thing.",
        layout="clean_hero",
        graphics=[],
        visual=(
            "Mock ALL 3 options. Bottle exactly as real, label readable, dominant at ~70%. "
            "One callout each, navy anchor with a single red accent. Amazon slot-1 stays "
            "pure white and product only.\n\n"
            "OPTION A — THE STUDY (owns proof): bottle centred, a small '+123%' figure and "
            "'PLoS One 2015' set quietly beside it. Badge (navy): 'PEER REVIEWED'.\n"
            "OPTION B — THE BLEND (owns real ingredients): bottle with Astragalus root, pine "
            "bark and schisandra berries arranged beside it. Badge: '465 MG SC100 BLEND'.\n"
            "OPTION C — THE FORMULATOR (owns credibility): bottle with a small portrait chip "
            "and 'Dr. Bryant Villeponteau, Ph.D.'. Badge: 'FORMULATED BY A SCIENTIST'.\n\n"
            "Across all 3: bottle ~70%, callout ~6%, identical lighting and colour temperature."
        ),
        overlay="(one callout per option)",
        overlay_sub="Three hero options shipped. A/B test them and keep the winner.",
        props=["A: bottle + study figure", "B: bottle + botanicals", "C: bottle + founder chip"],
        lighting="Soft premium studio light 5000K, gentle reflection under the bottle. Same across all 3.",
        why_it_works=(
            "Each option tests a different reason to trust: published proof, real ingredients, "
            "a named formulator. All three are checkable, which is what this buyer responds to."
        ),
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: more stem cells is the wrong goal",
        role="hook",
        background="Split frame. Left half cool grey #E8EAED, right half brand navy #14294D.",
        purpose="Open with the argument only this brand makes, instead of a category platitude.",
        layout="myth_vs_fact",
        graphics=[
            "vertical divider down the exact centre, 2 px, white",
            "LEFT chip 'THE USUAL PITCH' grey #6B7280 caps, top-left of the left half",
            "left side: a row of stem-cell dots depleting to the right, the last three faded, "
            "one thin red #C8202F rule struck through the row",
            "RIGHT chip 'OUR APPROACH' white on navy, top-right",
            "right side: the same dots held steady inside a soft glowing ring labelled "
            "'the micro-environment', bottle standing beside it",
        ],
        visual=(
            "Wrong belief on the left struck through, correction on the right. Bottle sits on "
            "the navy half at one third height."
        ),
        overlay="MORE ISN'T THE GOAL.",
        overlay_sub="You have a limited number of stem cells. This supports the ones you have.",
        props=["bottle", "depleting stem-cell dot row", "glowing niche ring"],
        lighting="Even and editorial. The graphic carries the frame, not the light.",
        why_it_works=(
            "The client's own page argues that spending stem cells faster is not a win, because "
            "each divides a limited number of times. It is a checkable claim that reframes every "
            "'boosts your stem cells' rival as the naive option, and no competitor can copy it "
            "without abandoning their own headline."
        ),
        cvr="Turns the category's loudest promise into a reason to doubt the competitor.",
    ),
    AIImagePlanItem(
        name="Image 3 — The published lifespan study",
        role="educate",
        background="Clean white, thin navy rules top and bottom. Journal-page restraint.",
        purpose="Show the peer-reviewed research instead of claiming to be backed by science.",
        layout="stat_block",
        graphics=[
            "hero figure '+123%' very large in navy #14294D, centred in the top two thirds",
            "caption beneath in 30 px grey: 'median lifespan, Drosophila fruit flies'",
            "paired bar chart bottom-left: treated 89 days navy vs control 48 days grey",
            "citation line bottom-centre 30 px: 'PLoS One 2015, 10:e0119068'",
            "bottle small bottom-right, no badge on it",
        ],
        visual=(
            "One number carries the frame, the chart and citation support it. Restrained and "
            "journal-like, never infomercial."
        ),
        overlay="PUBLISHED IN PLOS ONE.",
        overlay_sub="A peer reviewed lifespan study in fruit flies. Not a human result.",
        props=["bottle", "paired bar chart", "citation line"],
        lighting="Flat, even, white. This tile is a document, not a product shot.",
        why_it_works=(
            "This is the formula the study was actually run on, which makes it the strongest "
            "tile in the plan. Naming the journal makes it checkable, and stating the species "
            "in the same breath as the number is both the compliant way to run it and the "
            "reason an informed buyer will trust everything else on the page."
        ),
        ctr="A real citation stands out in a grid of unsourced claims.",
    ),
    AIImagePlanItem(
        name="Image 4 — Inside the SC100 blend",
        role="desire",
        background="White, generous margins, one soft #EEF2F8 field behind the bottle.",
        purpose="Make the formula concrete and checkable against the label.",
        layout="hub_and_spokes",
        graphics=[
            "bottle centred, occupying the middle third",
            "eight labelled nodes evenly spaced around it, hairline navy leader lines to the bottle",
            "nodes: ASTRAGALUS root, VACCINIUM ULIGINOSUM fruit, PINE BARK OPCs, L-THEANINE, "
            "POLYGONUM MULTIFLORUM stem, SCHISANDRA CHINENSIS fruit, HE SHOU WU root, DRYNARIA rhizome",
            "a small navy chip above the bottle reading '465 mg SC100 blend per capsule'",
        ],
        visual=(
            "Eight named botanicals ringed around the bottle with leader lines. Real botanical "
            "photography in each node, not illustration."
        ),
        overlay="465 MG. EIGHT BOTANICALS.",
        overlay_sub="Astragalus, pine bark OPCs, schisandra, he shou wu and four more. Standardised.",
        props=["bottle", "eight botanical nodes", "465 mg chip"],
        lighting="Bright, clean, flat-lay quality on the botanicals; bottle lit as studio product.",
        why_it_works=(
            "A named count and a real milligram figure are checkable against the label, where "
            "'10+ botanicals' is not. Specificity is the whole trust argument for a proprietary "
            "blend, and shoppers in this category read supplement facts panels."
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
            "card 1: 'Dr. Bryant Villeponteau, Ph.D.' with 'decades of research in molecular "
            "biology and longevity science' beneath, portrait at 120 px (CLIENT TO SUPPLY)",
            "card 2: 'Formula published in a peer reviewed journal', PLoS One citation small beneath",
            "card 3: 'Tested twice: ingredients for purity and potency, then the finished bottle'",
            "bottle bottom-right at 25% height, no badge",
        ],
        visual=(
            "Three proof cards, not a badge wall. Each carries one checkable fact rather than "
            "an adjective."
        ),
        overlay="BUILT BY A SCIENTIST.",
        overlay_sub="Dr. Bryant Villeponteau, Ph.D. Decades in molecular biology and longevity.",
        props=["bottle", "three reason cards", "founder portrait (to be supplied)"],
        lighting="Even, calm, premium. Portrait lit softly, never corporate stock.",
        why_it_works=(
            "Almost nothing in this category can put a named researcher on the pack, and the "
            "listing already carries the credential. Three checkable facts beat four generic "
            "badges: every bottle in the grid says lab tested, none of them says who made it."
        ),
    ),
    AIImagePlanItem(
        name="Image 6 — The daily routine",
        role="desire",
        background="Warm, bright kitchen counter in morning light. Real, never clinical.",
        purpose="Set honest expectations and show how small the daily step is.",
        layout="hand_in_frame",
        graphics=[
            "two capsules held in an open palm in the lower left third, shot at true scale "
            "beside a water glass so capsule size reads honestly",
            "navy routine strip across the top third: '2 capsules daily · 60 per bottle'",
            "one grey honesty line beneath the strip: 'A long term routine, not an overnight change.'",
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
            "Reviewers dislike vague expectations and say effects build slowly. Saying so plainly "
            "on the creative costs nothing, protects the review average and lifts repeat purchase."
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
            "'Named botanicals', 'A named formulator', 'Published research'",
        ],
        visual=(
            "Calm, premium, disciplined. The three closing facts sit in equal cells so none "
            "shouts louder than the others."
        ),
        overlay="SCIENCE YOU CAN CHECK.",
        overlay_sub="Named botanicals, a named formulator, published research. Made in the USA.",
        props=["bottle + Life Code wordmark", "three-cell fact band"],
        lighting="Premium, even, navy and white. Calm and credible.",
        why_it_works=(
            "'Backed by science' is the emptiest phrase in this category and every rival uses it. "
            "Naming what can be checked is the opposite claim and the brand's actual position."
        ),
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Brand banner",
        role="a+_banner",
        headline="SUPPORT FOR HEALTHY AGING.",
        body=(
            "Stem Cell 100 supports stem cell and telomere related pathways. Made in the USA, "
            "GMP, tested for purity and potency."
        ),
        visual=("DESKTOP 1464x600, white. LEFT 55%: navy headline, one support line, Life Code "
                "wordmark above. RIGHT 45%: bottle on soft #EEF2F8 with an abstract cell motif "
                "behind. MOBILE 600x450: bottle top, headline beneath, inside the safe area."),
        alt="Life Code Stem Cell 100 brand banner: support for stem cell and telomere related pathways.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): Why Stem Cell 100",
        role="a+_carousel",
        headline="WHY STEM CELL 100",
        body=(
            "Tile 1: <b>PATHWAY SUPPORT</b> Stem cell and telomere related pathways.<br/>"
            "Tile 2: <b>THE NICHE</b> Supports the environment around your stem cells.<br/>"
            "Tile 3: <b>465 MG SC100</b> Eight standardised botanicals per capsule.<br/>"
            "Tile 4: <b>PEER REVIEWED</b> Formula published in PLoS One.<br/>"
            "Tile 5: <b>MADE IN USA</b> GMP facility, tested twice, vegetarian capsules."
        ),
        visual=("Five square tiles, navy accent corner on each, one red highlight on tile 4. "
                "Line icons only, no stock photography. MOBILE: one tile per swipe."),
        alt="Five A+ tiles: pathway support, the stem cell niche, the 465 mg blend, peer reviewed, made in USA.",
    ),
    AIModule(
        name="Module 3 — Banner: why not simply more stem cells",
        role="a+_banner",
        headline="MORE IS NOT THE GOAL.",
        body=(
            "Each stem cell divides a limited number of times. This formula supports the ones "
            "you have, and the environment around them."
        ),
        visual=("DESKTOP 1464x600. LEFT 50% grey #E8EAED: dot row depleting right, thin red "
                "strike-through, chip 'THE USUAL PITCH'. RIGHT 50% navy #14294D: same dots steady "
                "inside a glowing ring labelled 'micro-environment', bottle beside it. MOBILE "
                "600x450: stack left over right, chips inside the safe area."),
        alt="A+ banner contrasting the usual boost-your-count pitch with supporting the cells you have.",
    ),
    AIModule(
        name="Module 4 — Carousel (5 tiles): Inside the SC100 blend",
        role="a+_carousel",
        headline="INSIDE THE SC100 BLEND",
        body=(
            "Tile 1: <b>ASTRAGALUS</b> Root, standardised.<br/>"
            "Tile 2: <b>PINE BARK OPCs</b> Bark extract.<br/>"
            "Tile 3: <b>SCHISANDRA</b> Fruit, plus Vaccinium uliginosum.<br/>"
            "Tile 4: <b>HE SHOU WU</b> Root, plus Polygonum multiflorum stem.<br/>"
            "Tile 5: <b>L-THEANINE + DRYNARIA</b> Completing the 465 mg blend."
        ),
        visual=("Five tiles, real botanical photography on white, latin name small beneath each "
                "common name. MOBILE: one botanical per swipe."),
        alt="Five A+ tiles naming the eight standardised botanicals in the 465 mg SC100 blend.",
    ),
    AIModule(
        name="Module 5 — Banner: the published lifespan study",
        role="a+_banner",
        headline="PUBLISHED IN PLOS ONE.",
        body=(
            "Median lifespan more than doubled in a peer reviewed fruit fly study. That is an "
            "animal result, not a human one."
        ),
        visual=("DESKTOP 1464x600, white. CENTRE-LEFT: '+123%' very large navy #14294D, caption "
                "'median lifespan, Drosophila fruit flies'. RIGHT: paired bars, treated 89 days "
                "navy vs control 48 days grey. FOOT: 'PLoS One 2015, 10:e0119068'. MOBILE "
                "600x450: figure top, bars beneath, citation legible."),
        alt="A+ banner showing the peer-reviewed Drosophila lifespan result and its citation.",
    ),
    AIModule(
        name="Module 6 — Banner: who formulated this",
        role="a+_banner",
        headline="BUILT BY A SCIENTIST.",
        body=(
            "Life Code was co-founded by Dr. Bryant Villeponteau, Ph.D., with decades of research "
            "in molecular biology and longevity science."
        ),
        visual=("DESKTOP 1464x600, soft #EEF2F8. LEFT 40%: founder portrait in a white card, name "
                "and credential beneath (CLIENT TO SUPPLY). RIGHT 60%: two stacked white proof "
                "cards with navy left rules, 'peer reviewed formula' and 'tested twice, USA GMP', "
                "bottle small bottom-right. MOBILE 600x450: portrait card top, cards beneath."),
        alt="A+ banner introducing Life Code co-founder Dr. Bryant Villeponteau, Ph.D.",
    ),
    AIModule(
        name="Module 7 — Premium Q&A",
        role="a+_qa",
        headline="QUESTIONS BEFORE YOU BUY",
        body="",   # rendered from the QA list below
        visual="Vertical Q and A table, navy divider lines, small navy Q. and red A. labels.",
        alt="Premium Q&A module for Life Code Stem Cell 100.",
    ),
]


# House standard: exactly 5 pairs, question <=80 chars, answer <=120.
# Cut from seven. The "added vitamins" line in the 100 vs 100+ answer is gone: no supplied
# source confirms any vitamins in either formula. The difference that IS documented is the
# two extra botanicals in the Plus.
QA = [
    AIQA(q="What is Stem Cell 100 designed to do?",
         a="It supports stem cell and telomere related pathways as part of a healthy aging "
           "routine."),
    AIQA(q="What are the main ingredients?",
         a="A 465 mg SC100 blend: Astragalus, Pine Bark OPCs, Schisandra, He Shou Wu, "
           "L-Theanine and more."),
    AIQA(q="Has the formula been studied?",
         a="Yes. A peer reviewed fruit fly lifespan study, PLoS One 2015. An animal result, "
           "not a human one."),
    AIQA(q="How is Stem Cell 100 different from Stem Cell 100+?",
         a="Plus adds Rhodiola Rosea and Tulsi to this blend and is the faster acting "
           "version."),
    AIQA(q="How do I take it, and how long does a bottle last?",
         a="Two vegetarian capsules daily. 60 capsules per bottle, about a 30 day supply."),
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
