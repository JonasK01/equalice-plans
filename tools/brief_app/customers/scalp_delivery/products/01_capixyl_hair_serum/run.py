"""Scalp Delivery — 5% Capixyl Hair Growth Serum  [Produkt 01]
Hand-written, KW-led, COSMETIC-COMPLIANT, marketing-elevated copy.

Marketplace: amazon.com (US). ASIN B0D3BCFT4V. Marke: Scalp Delivery (new brand).

House rules aktiv (Config): new_brand=true -> 7 A+ Module, Modul 7 = 'From the Brand'
(kein Comparison); brand_statement -> die coole Marken-Aussage.

COMPLIANCE (kosmetisch, oberste Priorität):
  - NUR appearance-based Claims wie im Live-Listing: 'supports fuller, thicker-looking hair',
    'for the look of thinning hair', 'supports a healthy-looking scalp environment'.
  - VERBOTEN: regrows hair / cures/treats/reverses baldness or alopecia / stops-prevents hair
    loss / clinically proven to grow hair / FDA-approved / guaranteed results / medical DHT-block.
  - 'Hair Growth Serum' nur als Produktname/Kategorie. Keine dramatischen before/after,
    keine Medizin-Scalp-Bilder, keine Superlative, keine Preise/URLs.
  - Ergebnisse ehrlich als konsequente Routine über Wochen rahmen.
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
ASIN = "B0D3BCFT4V"
EXCEL = HERE / "listing.xlsx"


TITLE = ('Scalp Delivery 5% Capixyl Hair Growth Serum for Men & Women — Lightweight Leave-In '
         'Scalp Serum for Fuller, Thicker-Looking Hair · Vegan & Cruelty-Free · Non-Greasy Daily '
         'Dropper · 1 fl oz (30 mL)')

BULLETS = [
    "<b>5% CAPIXYL — TRANSPARENT BY DESIGN</b> — Know exactly what you're applying: the active "
    "Capixyl peptide complex is stated right on the label at a clear 5% — no mystery \"proprietary\" "
    "blends, no guessing. Just an honest, science-forward scalp serum.",

    "<b>FOR FULLER, THICKER-LOOKING HAIR</b> — Formulated to support the look of fuller, thicker "
    "hair and a healthy-looking scalp environment for men and women noticing the appearance of "
    "thinning. A lightweight leave-in that slots into any daily routine.",

    "<b>LIGHTWEIGHT, NON-GREASY, FAST-ABSORBING</b> — A water-based serum that absorbs quickly "
    "with no sticky, oily residue — no flat, weighed-down hair. A little goes a long way, so your "
    "bottle lasts.",

    "<b>PRECISE DROPPER · ONCE A DAY</b> — Apply directly to the scalp along the part line with "
    "the built-in dropper for clean, mess-free application. 1 fl oz (30 mL) for weeks of "
    "consistent daily use.",

    "<b>VEGAN & CRUELTY-FREE · MEN & WOMEN</b> — A clean, considered, water-based formula for "
    "everyone. Results build with consistent use — this is a daily routine, not an overnight fix, "
    "and we'd rather tell you the truth.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="Clean white with a soft mint #EAF4F2 base and deep-teal accent. Identical across all 3 for a clean split test.",
        purpose="Win the click in a sea of look-alike hair serums — signal transparency (5%) + clean science instantly.",
        visual=(
            "Mock ALL 3 options. Product exactly as real: the Scalp Delivery dropper bottle, label "
            "and '5% Capixyl' readable, crisp studio light. ONE callout each, bottle dominant ~70%. "
            "Deep-teal anchor, mint accent. Amazon slot-1 main = pure white / bottle only.\n\n"
            "OPTION A — TRANSPARENCY (owns the angle): bottle with the '5%' made a proud badge, a "
            "small 'active concentration, stated' tag. Badge (teal): '5% CAPIXYL, STATED'.\n"
            "OPTION B — THE OUTCOME (appearance-based): bottle beside healthy, full-looking hair "
            "(natural, realistic). Badge (mint): 'FULLER, THICKER-LOOKING HAIR'.\n"
            "OPTION C — TRUST STACK: bottle + small badge row (Vegan · Cruelty-Free · Non-Greasy · "
            "Men & Women). Badge (teal): 'VEGAN & CRUELTY-FREE'.\n\n"
            "Across all 3: bottle ~70%, callout ~6%, same lighting + colour temperature."
        ),
        overlay="(one callout per option)",
        overlay_sub="3 hero options shipped — A/B test, keep the winner.",
        props=["A: bottle + proud 5% badge", "B: bottle + realistic full-looking hair", "C: bottle + vegan/cruelty-free/non-greasy badges"],
        lighting="Clean, fresh studio light; a soft reflection under the bottle. Same across all 3.",
        why_it_works=(
            "Three triggers: transparency (the 5% angle no one else leads with), the appearance "
            "outcome, and clean-formula trust — each cosmetic-compliant and clear at thumbnail size."
        ),
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: know exactly what you apply",
        role="hook",
        background="Soft mint #EAF4F2 with a deep-teal headline (clean clinical look)",
        purpose="Own the transparency angle — the reason to pick this over vague 'proprietary' serums.",
        visual=(
            "The bottle centred with a clean split: LEFT a vague generic serum labelled 'Proprietary "
            "blend ??%' greyed out; RIGHT the Scalp Delivery bottle with a bright '5% CAPIXYL' "
            "call-out. A short line: 'The active is on the label — no mystery blends.' Keep it "
            "confident and honest, not a knock on a named competitor."
        ),
        overlay="KNOW WHAT YOU APPLY.",
        overlay_sub="A clearly-stated 5% Capixyl active — not a vague \"proprietary\" blend.",
        props=["bottle with bright 5% call-out", "greyed generic 'proprietary ??%' foil", "honest transparency line"],
        lighting="Even, clean, editorial. Clarity over drama.",
        why_it_works=(
            "In a category full of vague 'proprietary' promises, a clearly-stated 5% active is a "
            "genuine, defensible differentiator — and it builds trust with a skeptical buyer."
        ),
        cvr="Answers the 'what's actually in it / does it really contain enough?' doubt.",
    ),
    AIImagePlanItem(
        name="Image 3 — What is 5% Capixyl?",
        role="educate",
        background="White with a deep-teal footer band",
        purpose="Educate on the active — cosmetic, elegant, non-medical.",
        visual=(
            "Clean science-style graphic: Capixyl shown as its two parts — a biomimetic PEPTIDE + "
            "RED CLOVER extract — with an elegant, abstract 'scalp environment / root' motif (not a "
            "clinical scalp). Short, appearance-based captions only: 'A cosmetic complex to support "
            "the look of fuller, thicker hair and a healthy-looking scalp environment.' Footer band: "
            "'Active concentration: 5%.'"
        ),
        overlay="WHAT IS 5% CAPIXYL?",
        overlay_sub="A peptide + red-clover complex to support fuller, thicker-looking hair.",
        props=["Capixyl = peptide + red clover graphic", "abstract scalp/root motif", "5% footer band"],
        lighting="Bright, clean, science-editorial. Elegant, not clinical/scary.",
        why_it_works=(
            "Buyers want to understand the active before they invest weeks into a routine. A clean, "
            "honest explainer earns credibility and justifies the choice — while staying cosmetic."
        ),
    ),
    AIImagePlanItem(
        name="Image 4 — Lightweight, non-greasy texture",
        role="desire",
        background="Soft mint, fresh close-up",
        purpose="Show the feel — the thing daily users care about most.",
        visual=(
            "A clean droplet of the water-based serum on skin/fingertip, absorbing fast; a small "
            "'no residue' cue (a light, matte finish, not oily shine). Callouts: 'Water-based', "
            "'Absorbs fast', 'No sticky residue'. Fresh, clean, tactile."
        ),
        overlay="LIGHTWEIGHT. FAST-ABSORBING.",
        overlay_sub="A water-based serum that soaks in fast — no sticky, oily, weighed-down feel.",
        props=["serum droplet absorbing on fingertip", "'no residue' matte cue", "3 texture callouts"],
        lighting="Fresh, clean close-up light; the droplet looks light and watery, not oily.",
        why_it_works=(
            "'Lightweight & non-greasy' is the most-praised trait in reviews. Showing the fast-"
            "absorbing, residue-free feel reassures daily users it won't ruin their hair or routine."
        ),
    ),
    AIImagePlanItem(
        name="Image 5 — How to use: dropper, once a day",
        role="desire",
        background="Clean white with a friendly teal step strip",
        purpose="Make the routine effortless and clear — precise, mess-free.",
        visual=(
            "Three simple steps with the dropper: 1) Part the hair; 2) Apply a few drops directly "
            "to the scalp along the part line; 3) Massage in — leave-in, no rinse. Show a unisex "
            "hand (men and women). Small note: '1 fl oz (30 mL) · once daily · a little goes a long "
            "way.' Clean and precise."
        ),
        overlay="ONE DROPPER. ONCE DAILY.",
        overlay_sub="Part, apply to the scalp, massage in — a clean, leave-in daily step.",
        props=["3-step dropper application", "part-line scalp application", "unisex hands", "30 mL note"],
        lighting="Bright, even, instructional clarity.",
        why_it_works=(
            "Ease and precision drive daily compliance — and consistency is what this product needs "
            "to work. A clear, mess-free routine removes friction and sets the habit."
        ),
    ),
    AIImagePlanItem(
        name="Image 6 — For men & women · vegan & cruelty-free · honest results",
        role="desire",
        background="Soft mint, clean trust layout",
        purpose="Stack the trust signals and set honest expectations.",
        visual=(
            "The bottle with a clean badge row: 'FOR MEN & WOMEN', 'VEGAN', 'CRUELTY-FREE', "
            "'NON-GREASY'. Beside it, an honest 'what to expect' note framed as a routine: 'A daily "
            "serum — give it consistent use over several weeks. Not an overnight fix.' Calm, "
            "credible, honest."
        ),
        overlay="FOR MEN & WOMEN.",
        overlay_sub="Vegan, cruelty-free, non-greasy — and honest about consistent daily use.",
        props=["bottle + badge row (men&women/vegan/cruelty-free/non-greasy)", "honest 'what to expect' routine note"],
        lighting="Clean, even, trustworthy.",
        why_it_works=(
            "Reviews split on effectiveness because expectations aren't set. Being upfront that "
            "results build over weeks improves satisfaction, cuts returns, and — with the vegan / "
            "cruelty-free stack — makes the brand feel trustworthy."
        ),
        cvr="Turns the 'mixed results / takes time' objection into an honesty advantage.",
    ),
    AIImagePlanItem(
        name="Image 7 — Brand close: transparent by design",
        role="close",
        background="Clean deep-teal brand panel with white space",
        purpose="Close on the brand's transparency promise.",
        visual=(
            "The bottle with the Scalp Delivery wordmark and a calm, clean science motif. Lower "
            "band, three quiet trust points: 'Active stated on the label (5% Capixyl)', 'Lightweight, "
            "vegan & cruelty-free', 'An honest daily routine'. Tone: transparent, credible, premium."
        ),
        overlay="TRANSPARENT BY DESIGN.",
        overlay_sub="Scalp Delivery — a clearly-stated active and an honest routine.",
        props=["bottle + Scalp Delivery wordmark", "clean science motif", "3 trust points band"],
        lighting="Clean, premium, teal-and-white. Calm and credible.",
        why_it_works=(
            "Against vague 'proprietary' serums, a transparency-first brand close is the trust "
            "signal that converts a skeptical, research-minded buyer."
        ),
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Brand banner",
        role="a+_banner",
        headline="A CLEARLY-STATED 5% ACTIVE.",
        body=(
            "Scalp Delivery is a transparent, science-forward scalp serum: a clearly-stated 5% "
            "Capixyl peptide complex, formulated to support the look of fuller, thicker hair and a "
            "healthy-looking scalp environment for men and women. Lightweight, non-greasy, vegan "
            "and cruelty-free."
        ),
        visual="Wide clean banner: dropper bottle right, deep-teal headline left on white, an elegant abstract peptide/scalp motif. Scalp Delivery wordmark upper-left.",
        alt="Scalp Delivery 5% Capixyl serum banner: a clearly-stated active for fuller, thicker-looking hair.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): Why Scalp Delivery",
        role="a+_carousel",
        headline="WHY SCALP DELIVERY",
        body=(
            "Tile 1: <b>5% CAPIXYL, STATED</b> — The active is on the label — no mystery blends.<br/>"
            "Tile 2: <b>FULLER-LOOKING HAIR</b> — Supports the look of thicker, fuller hair.<br/>"
            "Tile 3: <b>LIGHTWEIGHT</b> — Water-based, non-greasy, fast-absorbing.<br/>"
            "Tile 4: <b>PRECISE DROPPER</b> — Clean, once-daily scalp application.<br/>"
            "Tile 5: <b>VEGAN &amp; CRUELTY-FREE</b> — For men &amp; women, 1 fl oz (30 mL)."
        ),
        visual="5 square tiles, mint accent corner each, clean icons (5% · hair · droplet · dropper · leaf).",
        alt="Five A+ tiles: 5% Capixyl stated, fuller-looking hair, lightweight, precise dropper, vegan and cruelty-free.",
    ),
    AIModule(
        name="Module 3 — Banner: What is Capixyl",
        role="a+_banner",
        headline="WHAT IS 5% CAPIXYL?",
        body=(
            "Capixyl pairs a biomimetic peptide with red-clover extract — a cosmetic complex "
            "formulated to support the look of fuller, thicker hair and a healthy-looking scalp "
            "environment. Scalp Delivery states the concentration plainly: 5%."
        ),
        visual="Banner: Capixyl shown as peptide + red-clover with an elegant abstract root/scalp motif, and a '5%' marker. Teal/white, one mint accent.",
        alt="A+ banner explaining 5% Capixyl as a peptide plus red-clover cosmetic complex.",
    ),
    AIModule(
        name="Module 4 — Banner: How to use",
        role="a+_banner",
        headline="ONE DROPPER. ONCE A DAY.",
        body=(
            "Part your hair, apply a few drops directly to the scalp along the part line, and "
            "massage in — a leave-in step, no rinse. Use once daily and give it consistent use over "
            "several weeks. A little goes a long way; 1 fl oz (30 mL) per bottle."
        ),
        visual="Banner with a 3-step dropper routine (part · apply to scalp · massage in), unisex hands, clean teal/white styling.",
        alt="A+ banner showing the once-daily dropper routine for the Scalp Delivery serum.",
    ),
    AIModule(
        name="Module 5 — Carousel (5 tiles): Clean & honest",
        role="a+_carousel",
        headline="CLEAN & HONEST",
        body=(
            "Tile 1: <b>VEGAN</b> — No animal-derived ingredients.<br/>"
            "Tile 2: <b>CRUELTY-FREE</b> — Never tested on animals.<br/>"
            "Tile 3: <b>NON-GREASY</b> — Water-based, absorbs fast.<br/>"
            "Tile 4: <b>FOR MEN &amp; WOMEN</b> — One serum, everyone.<br/>"
            "Tile 5: <b>HONEST ROUTINE</b> — Results build with consistent use."
        ),
        visual="5 tiles with clean check-style icons, mint accents; calm and credible.",
        alt="Five A+ tiles: vegan, cruelty-free, non-greasy, for men and women, honest routine.",
    ),
    AIModule(
        name="Module 6 — Premium Q&A",
        role="a+_qa",
        headline="QUESTIONS BEFORE YOU BUY",
        body=(
            "<b>Q.</b> What does the serum do?<br/>"
            "<b>A.</b> It's formulated to support the look of fuller, thicker hair and a healthy-"
            "looking scalp environment, using a clearly-stated 5% Capixyl complex.<br/><br/>"
            "<b>Q.</b> How do I use it?<br/>"
            "<b>A.</b> Once daily: part the hair, apply a few drops to the scalp with the dropper "
            "and massage in. It's a leave-in — no rinsing.<br/><br/>"
            "<b>Q.</b> Is it greasy?<br/>"
            "<b>A.</b> No. It's a lightweight, water-based serum that absorbs quickly with no "
            "sticky or oily residue.<br/><br/>"
            "<b>Q.</b> Is it for men or women?<br/>"
            "<b>A.</b> Both. It's a unisex, vegan and cruelty-free formula.<br/><br/>"
            "<b>Q.</b> How long until I notice a difference?<br/>"
            "<b>A.</b> It's a daily routine, not an overnight fix — give it consistent use over "
            "several weeks. Results vary from person to person."
        ),
        visual="Vertical Q/A table, teal divider lines, small teal Q. and mint A. labels.",
        alt="Premium Q&A module for the Scalp Delivery 5% Capixyl serum.",
    ),
]


QA = [
    AIQA(q="What is the serum designed to do?",
         a="It is formulated to support the look of fuller, thicker hair and a healthy-looking scalp environment, using a clearly-stated 5% Capixyl peptide complex. It supports the appearance of hair for men and women noticing thinning."),
    AIQA(q="What is Capixyl?",
         a="Capixyl is a cosmetic complex that pairs a biomimetic peptide with red-clover extract. Scalp Delivery states the concentration plainly at 5%, so you know exactly what you're applying."),
    AIQA(q="How do I use it, and how often?",
         a="Once daily. Part your hair, apply a few drops directly to the scalp along the part line with the dropper, and massage in. It's a leave-in serum — no rinsing."),
    AIQA(q="Is it greasy or heavy?",
         a="No. It's a lightweight, water-based serum that absorbs quickly and leaves no sticky or oily residue, so it won't weigh your hair down. A little goes a long way."),
    AIQA(q="Is it suitable for men and women?",
         a="Yes. It's a unisex formula, and it's vegan and cruelty-free. The bottle is 1 fl oz (30 mL)."),
    AIQA(q="How long until I see a difference?",
         a="This is a daily routine rather than an overnight fix. Give it consistent use over several weeks; results vary from person to person."),
    AIQA(q="Can I use it on color-treated hair?",
         a="It is a lightweight, water-based leave-in applied to the scalp. As with any new product, if you have specific concerns, patch test first and check with your stylist about your particular hair."),
]


BACKEND = (
    "capixyl hair growth serum scalp serum hair thickening serum hair density serum for men women "
    "lightweight non greasy vegan cruelty free dropper leave in thinning hair fuller thicker looking "
    "hair peptide red clover 5 percent daily routine scalp delivery"
)


def main() -> None:
    print("Lade Scalp Delivery + Capixyl-Serum Listing…")
    cust = load_customer("scalp_delivery")
    brief = parse_excel(EXCEL)
    OUT = HERE / f"{PLAN_NO}_{ASIN}_Image Plan.pdf"
    print(f"  Produkt: {brief.product_name}  ASIN: {ASIN}  Marktplatz: {cust.marketplace}")
    print(f"  new_brand={cust.new_brand} (Comparison weg, From-the-Brand als Modul 7)")

    builder = BriefBuilder(cust, brief, OUT, ai=None)
    builder._ai_title = TITLE
    builder._ai_bullets = BULLETS
    builder._ai_images = IMAGES
    builder._ai_modules = MODULES
    builder._ai_qa = QA
    builder._ai_backend = BACKEND
    builder.copy_source_label = "Hand-written senior copy (cosmetic-compliant, marketing-elevated)"

    print("Baue Branded PDF…")
    pdf_path = builder.build()
    size_kb = pdf_path.stat().st_size // 1024
    import re
    pages = len(re.findall(rb'/Type\s*/Page[^s]', pdf_path.read_bytes()))
    print(f"Gebaut: {pdf_path}")
    print(f"  Seiten: {pages}  Größe: {size_kb} KB")


if __name__ == "__main__":
    main()
