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
from tools.brief_app.core.seo_loader import load_seo, as_bullets_html

PLAN_NO = "01"
ASIN = "B00OADCBUU"
EXCEL = HERE / "listing.xlsx"


# Title and bullets are NOT defined here. They come from listing.xlsx, which is the SEO
# axis for this plan and the only approved source for on-listing copy.
#
# They used to be hand-written constants at this spot, and had drifted from the sheet: that
# version put Vitamin D3, B12, active Folate (5-MTHF), Genistein, Rubus Chingii and Drynaria
# into the title and bullets. None of them appear in the SEO sheet or in anything the client
# has supplied. On a dietary supplement listing that is not a wording difference, it is an
# ingredient claim, so the constants are deleted rather than kept as a fallback — a fallback
# is just a slower way to ship the same error.


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
            "Rhodiola and pine bark arranged beside it. Badge: 'STANDARDISED BOTANICALS'.\n"
            "OPTION C — TRUST STACK (defuses 'is it legit?'): bottle + small badge row (Made in "
            "USA · GMP · Vegetarian · Lab-Tested). Badge: 'MADE IN USA · GMP'.\n\n"
            "Across all 3: bottle ~70%, callout ~6%, same lighting + colour temperature."
        ),
        overlay="(one callout per option)",
        overlay_sub="Three hero options shipped. A/B test them and keep the winner.",
        props=["A: bottle + abstract cell/telomere motif", "B: bottle + Astragalus/Rhodiola/pine bark", "C: bottle + trust-badge row"],
        lighting="Soft, premium studio light (5000K), gentle reflection under the bottle. Same across all 3.",
        why_it_works=(
            "Three triggers: category ownership (pathway support), real botanicals, and trust — "
            "each compliant and readable at thumbnail size. No disease or reversal claims."
        ),
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: more stem cells is the wrong goal",
        role="hook",
        background="Split frame. Left half cool grey #E8EAED, right half brand navy #14294D.",
        purpose="Lead with the argument only this brand can make, instead of a category platitude.",
        layout="myth_vs_fact",
        graphics=[
            "vertical divider down the exact centre, 2 px, white",
            "LEFT band label chip 'THE USUAL PITCH' in grey #6B7280 caps 12 px, top-left",
            "left side: a row of stem-cell dots depleting left to right, last three faded out, "
            "struck through with a single thin red #C8202F rule",
            "RIGHT band label chip 'OUR APPROACH' in white on navy, top-right",
            "right side: the same dots held steady inside a softly glowing ring labelled "
            "'the micro-environment', bottle standing beside it",
        ],
        visual=(
            "Two stacked bands, the wrong belief on the left struck through, the correction on the "
            "right. Bottle sits on the navy half at one third height."
        ),
        overlay="MORE ISN'T THE GOAL.",
        overlay_sub="You have a limited number of stem cells. This formula supports the ones you have.",
        props=["bottle", "depleting stem-cell dot row", "glowing niche ring"],
        lighting="Even, editorial, no drama. The graphic carries the frame, not the light.",
        why_it_works=(
            "The client's own page makes a contrarian argument no competitor makes: spending stem "
            "cells faster is not a win, because each divides a limited number of times. That is a "
            "checkable claim a shopper can weigh, and it reframes every 'boosts stem cells' rival "
            "as the naive option. It is the strongest asset on the page and the first plan omitted it."
        ),
        cvr="Turns the category's loudest claim into a reason to doubt the competitor instead.",
    ),
    AIImagePlanItem(
        name="Image 3 — The published lifespan study",
        role="educate",
        background="Clean white, thin navy rule top and bottom. Journal-page restraint.",
        purpose="Show the peer-reviewed research rather than saying 'backed by science'.",
        layout="stat_block",
        graphics=[
            "hero figure '+123%' set very large in navy #14294D, centred in the top two thirds",
            "caption directly beneath in 30 px grey: 'median lifespan, Drosophila fruit flies'",
            "paired bar chart bottom-left comparing the OLDEST 5% of each group, treated navy vs control grey, labelled '+77% in the oldest 5%'",
            "citation line bottom-centre in 30 px: 'PLoS One 2015, 10:e0119068'",
            "a one-line note under the chart in 30 px grey: 'group comparison, not a single longest-lived individual'",
            "method strip along the bottom edge in 30 px grey: '3 treated cages vs 3 controls, 500 flies per cage, 250 male and 250 female'",
            "bottle small at bottom-right, no badge on it",
        ],
        visual=(
            "One number carries the frame, the chart and the citation support it underneath. "
            "Restrained and journal-like, never infomercial."
        ),
        overlay="PUBLISHED IN PLOS ONE.",
        overlay_sub="A peer reviewed lifespan study in fruit flies. Not a human result.",
        props=["bottle", "paired bar chart", "citation line"],
        lighting="Flat, even, white. This tile is a document, not a product shot.",
        why_it_works=(
            "A peer-reviewed lifespan study is close to unheard of in this category, and naming the "
            "journal makes it checkable. The subline states the species and the limit in the same "
            "breath as the number, which is both the compliant way to run it and the reason an "
            "informed longevity buyer will trust the rest of the page."
        ),
        ctr="A real citation stands out in a grid of unsourced claims.",
    ),
    AIImagePlanItem(
        name="Image 4 — 100+ vs 100: the upgraded formula",
        role="desire",
        background="Soft light-blue #EEF2F8, clean comparison",
        purpose="Position 100+ as the more comprehensive choice within the range.",
        layout="comparison_columns",
        graphics=[
            "two equal columns, thin grey divider, bottle standing at the top of each",
            "LEFT header 'STEM CELL 100', RIGHT header 'STEM CELL 100+' with a red #C8202F plus mark",
            "four criterion rows down both columns: SC100 blend, Rhodiola Rosea, Tulsi, pace",
            "shared botanicals shown as grey ticks on both sides, the two Plus-only rows as "
            "red ticks on the right and grey dashes on the left",
        ],
        visual=(
            "Two columns, same criteria down both sides, the difference carried by the tick colour "
            "rather than by any extra copy."
        ),
        overlay="TWO FORMULAS. ONE CHOICE.",
        overlay_sub="Plus adds Rhodiola Rosea and Tulsi to the SC100 blend.",
        props=["Stem Cell 100 + 100+ bottles side by side", "four-row criteria table", "red + accent"],
        lighting="Even, clean; true label colours on both bottles.",
        why_it_works=(
            "Shoppers comparing the two need one clear reason to choose Plus. Naming the two "
            "botanicals that actually differ is checkable against the label, which is worth more "
            "to this buyer than a vague 'more comprehensive'."
        ),
    ),
    AIImagePlanItem(
        name="Image 5 — Who formulated this",
        role="trust",
        background="Soft light-blue #EEF2F8, one white card stack, generous margins.",
        purpose="Put a named scientist behind the bottle. The listing's biggest unused asset.",
        layout="why_us",
        graphics=[
            "three white reason cards stacked with 24 px gaps, each with a navy #14294D left rule",
            "card 1: 'Co-founded by Dr. Bryant Villeponteau, Ph.D.' with a small portrait at 120 px "
            "(CLIENT TO SUPPLY, see SOURCE_NOTES)",
            "card 2: 'A study of this formula was published in a peer reviewed journal', PLoS One citation beneath",
            "card 3: 'Made in the USA, GMP facility, laboratory tested' with three 40 px line icons in a row",
            "bottle bottom-right at 25% height, no badge",
        ],
        visual=(
            "A stack of three proof cards, not a badge wall. Each card carries one checkable fact "
            "rather than an adjective."
        ),
        overlay="BUILT BY A SCIENTIST.",
        overlay_sub="Co-founded by Dr. Bryant Villeponteau, Ph.D.",
        props=["bottle", "three reason cards", "founder portrait (to be supplied)"],
        lighting="Even, calm, premium. Portrait lit softly, never corporate-stock.",
        why_it_works=(
            "Almost nothing in this category can put a named researcher on the pack, and the "
            "listing already carries the credential. Three checkable facts beat four generic "
            "badges: 'lab-tested' is on every bottle in the grid, a named scientist is not."
        ),
    ),
    AIImagePlanItem(
        name="Image 6 — Every claim has a reference",
        role="desire",
        background="White, thin navy grid rules. Reads like a table in a paper, not an advert.",
        purpose="Show the evidence base itself. This is what 'backed by science' should mean.",
        layout="grid_of_uses",
        graphics=[
            "3x3 grid, nine equal cells, hairline navy #14294D rules between them",
            "each cell: the supported area in navy semi-bold, its reference numbers beneath in "
            "grey 30 px, e.g. 'Adult stem cell rejuvenation' / '[1-4]'",
            "the nine cells: adult stem cell rejuvenation [1-4]; healthy cardiovascular system "
            "[5-8]; healthy blood glucose, for those already in the normal range [9-13]; healthy "
            "blood pressure, for those already in the normal range [14-15]; healthy cholesterol, "
            "for those already in the normal range [9, 16-17]; more youthful looking skin [18-24]; "
            "learning and focus [25-30]; endurance with vigorous exercise [31-35]; healthy immune "
            "system [31-32, 36-39]",
            "footer rule with 'References 1 to 39, published and listed by Life Code' in 30 px grey",
            "FDA disclaimer set small beneath the footer, full sentence, never abbreviated",
            "bottle small bottom-right outside the grid",
        ],
        visual=(
            "Nine cells, identical construction, each pairing one supported area with its "
            "citation numbers. Restrained typography, no icons, no colour beyond the navy rules."
        ),
        overlay="EVERY CLAIM HAS A NUMBER.",
        overlay_sub="Nine supported areas, each tied to published references.",
        props=["3x3 citation grid", "footer reference line", "FDA disclaimer", "bottle"],
        lighting="Flat and even. This tile is a document; treat it as typography, not photography.",
        why_it_works=(
            "Every rival in this category writes 'backed by science' and shows nothing. Printing "
            "the reference numbers next to each supported area is the opposite move: it invites "
            "the shopper to check, which only a brand with real citations can afford to do. The "
            "'already in the normal range' qualifiers are part of the claim and stay on the cells. "
            "References 40 to 46 are deliberately excluded from the grid."
        ),
        cvr="Converts the informed sceptic, who is exactly this brand's buyer.",
    ),
    AIImagePlanItem(
        name="Image 7 — Brand close: Life Code longevity science",
        role="close",
        background="Clean navy brand panel with white space",
        purpose="Close on credibility — a science-led longevity brand.",
        layout="brand_close",
        graphics=[
            "Life Code wordmark centred in the top third on navy #14294D",
            "bottle centred beneath it at 45% frame height",
            "lower band split into three equal cells by hairline white rules, one quiet fact each",
        ],
        visual=(
            "Bottle with the Life Code wordmark and a calm, premium science motif. Lower band, "
            "three quiet trust points: 'Longevity-science formulas', 'Made in the USA · GMP · "
            "lab-tested', '90-day money-back guarantee'. Tone: credible, disciplined, premium — "
            "no hype."
        ),
        overlay="SCIENCE YOU CAN CHECK.",
        overlay_sub="Named botanicals, a named formulator, published research. Made in the USA.",
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
        headline="SUPPORT FOR HEALTHY AGING.",
        body=(
            "Stem Cell 100+ supports stem cell and telomere related pathways. Made in the USA, "
            "GMP, laboratory tested."
        ),
        visual=("DESKTOP 1464x600, white. LEFT 55%: navy headline, one support line, Life Code "
                "wordmark above. RIGHT 45%: bottle on a soft #EEF2F8 field with an abstract cell "
                "and telomere motif behind it. MOBILE 600x450: bottle top, headline beneath."),
        alt="Life Code Stem Cell 100+ brand banner: support for stem cell and telomere related pathways.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): Why Stem Cell 100+",
        role="a+_carousel",
        headline="WHY STEM CELL 100+",
        body=(
            "Tile 1: <b>PATHWAY SUPPORT</b> Stem cell and telomere related pathways.<br/>"
            "Tile 2: <b>THE NICHE</b> Supports the environment around your stem cells.<br/>"
            "Tile 3: <b>SC100+ BLEND</b> Astragalus, Rhodiola Rosea, Tulsi, Pine Bark OPCs.<br/>"
            "Tile 4: <b>PEER REVIEWED</b> A study of the formula, published in PLoS One.<br/>"
            "Tile 5: <b>MADE IN USA</b> GMP, lab tested, vegetarian capsules."
        ),
        visual=("Five square tiles, navy accent corner on each, one disciplined red highlight on "
                "tile 4. Line icons only, no stock photography. MOBILE: same five, one per swipe."),
        alt="Five A+ tiles: pathway support, the stem cell niche, the SC100+ blend, peer reviewed, made in USA.",
    ),
    AIModule(
        name="Module 3 — Banner: why not simply more stem cells",
        role="a+_banner",
        headline="MORE IS NOT THE GOAL.",
        body=(
            "Each stem cell divides a limited number of times, and the niche around it becomes "
            "less nurturing with age. This formula supports the cells you have and that niche, "
            "rather than spending them faster."
        ),
        visual=("DESKTOP 1464x600. LEFT 50% grey #E8EAED: dot row depleting to the right, thin red "
                "strike-through, chip 'THE USUAL PITCH'. RIGHT 50% navy #14294D: same dots steady "
                "inside a glowing ring labelled 'micro-environment', bottle beside it. MOBILE "
                "600x450: stack left over right, chips stay inside the safe area."),
        alt="A+ banner contrasting the usual boost-your-stem-cell-count pitch with supporting the cells you have.",
    ),
    AIModule(
        name="Module 4 — Carousel (5 tiles): The Life Code longevity range",
        role="a+_carousel",
        headline="THE LIFE CODE RANGE",
        body=(
            "Tile 1: <b>STEM CELL 100+</b> The SC100 blend plus Rhodiola and Tulsi (this product).<br/>"
            "Tile 2: <b>STEM CELL 100</b> The original SC100 formula.<br/>"
            "Tile 3: <b>TELOMAX</b> Telomere focused botanical support.<br/>"
            "Tile 4: <b>LONGEVITY COMBO</b> Stem Cell 100+ paired with TeloMax.<br/>"
            "Tile 5: <b>90 DAY GUARANTEE</b> Try the Life Code approach with confidence."
        ),
        visual=("Five tiles, the range shot in one consistent navy and white style, this product "
                "gently highlighted with a red rule. MOBILE: one bottle per swipe, name beneath."),
        alt="Five A+ tiles of the Life Code range: Stem Cell 100+, Stem Cell 100, TeloMax, the combo, the guarantee.",
    ),
    AIModule(
        name="Module 5 — Banner: the published lifespan study",
        role="a+_banner",
        headline="PUBLISHED IN PLOS ONE.",
        body=(
            "Median lifespan rose 123% in a peer reviewed Drosophila study: three treated "
            "cages against three controls, 500 flies each. An animal result, not a human one."
        ),
        visual=("DESKTOP 1464x600, white. CENTRE-LEFT: '+123%' very large navy #14294D, caption "
                "beneath 'median lifespan, Drosophila fruit flies'. RIGHT: paired bars comparing the "
                "oldest 5% of each group, +77%, navy vs grey. FOOT: 'PLoS One 2015, 10:e0119068 · 3 treated cages vs 3 controls, 500 flies each'. MOBILE "
                "600x450: figure on top, bars beneath, citation stays legible."),
        alt="A+ banner showing the peer-reviewed Drosophila lifespan result and its citation.",
    ),
    AIModule(
        name="Module 6 — Banner: who formulated this",
        role="a+_banner",
        headline="BUILT BY A SCIENTIST.",
        body=(
            "Life Code was co-founded by Dr. Bryant Villeponteau, Ph.D., whose background is in "
            "molecular biology and longevity science. Made in the USA, GMP, laboratory tested."
        ),
        visual=("DESKTOP 1464x600, soft #EEF2F8. LEFT 40%: founder portrait in a white card, name "
                "and Ph.D. beneath (CLIENT TO SUPPLY). RIGHT 60%: two stacked white proof cards "
                "with navy left rules, 'peer reviewed formula' and 'USA, GMP, lab tested', bottle "
                "small bottom-right. MOBILE 600x450: portrait card on top, cards beneath."),
        alt="A+ banner introducing Life Code co-founder Dr. Bryant Villeponteau, Ph.D.",
    ),
    AIModule(
        name="Module 7 — Premium Q&A",
        role="a+_qa",
        headline="QUESTIONS BEFORE YOU BUY",
        body="",   # rendered from the QA list below
        visual="Vertical Q and A table, navy divider lines, small navy Q. and red A. labels.",
        alt="Premium Q&A module for Life Code Stem Cell 100+.",
    ),
]


# House standard: exactly 5 pairs, question ≤80 chars, answer ≤120.
#
# Rewritten from seven. Two answers previously listed Genistein, Rubus Chingii, Drynaria,
# Vitamin D3, B12 and Folate as being in this product. No source the client supplied confirms
# any of them for the Plus formula, so they are out until the client sends the full label.
# On a supplement listing an unverified ingredient is not a copy problem, it is a liability.
QA = [
    AIQA(q="What is Stem Cell 100+ designed to do?",
         a="It supports stem cell and telomere related pathways as part of a healthy aging "
           "routine."),
    AIQA(q="What are the main ingredients?",
         a="The SC100+ botanical blend: Astragalus, Rhodiola Rosea, Tulsi, Pine Bark OPCs, "
           "He Shou Wu, L-Theanine."),
    AIQA(q="How do I take it, and how long does a bottle last?",
         a="Two vegetarian capsules daily. 60 capsules per bottle, about a 30 day supply."),
    AIQA(q="How is Stem Cell 100+ different from Stem Cell 100?",
         a="Plus adds Rhodiola Rosea and Tulsi to the SC100 blend."),
    AIQA(q="When will I notice a difference?",
         a="It is a long term daily routine, not an overnight product. Results vary from "
           "person to person."),
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

    # Title and bullets come 1:1 from the SEO sheet, which is the axis for this plan.
    # They used to be hand-written constants in this file, and had drifted: that version
    # claimed Vitamin D3, B12, Folate, Genistein, Rubus Chingii and Drynaria for this
    # product. None of those appear in the SEO sheet or in any source the client supplied.
    # On a supplement listing that is not a copy difference, it is an ingredient claim.
    seo = load_seo(EXCEL)
    builder = BriefBuilder(cust, brief, OUT, ai=None)
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
