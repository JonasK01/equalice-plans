"""NUMOTIZINE — Pain Relief Ointment (8 oz)  [Produkt 01]
Titel/Bullets/Backend aus dem gefüllten SEO-Sheet (listing.xlsx); Bildregie + Module
hand-written (professional, warm, educational, heritage). EN / amazon.com.

ASIN B000GCPX7M. Marke: NUMOTIZINE (Hobart Laboratories, seit 1905). New brand.

House rules aktiv (Config): new_brand=true -> 7 Module, Modul 7 = 'From the Brand' (kein
Comparison); brand_statement -> die Heritage-Aussage. Echtes Logo geseedet.

OTC-COMPLIANCE (oberste Priorität, FDA topical analgesic): nur zugelassene Menthol-Claims
('temporarily relieves minor aches and pains of muscles and joints'); ages 12+; NIE
cure/heal/permanent/best/#1/guaranteed/prevents-arthritis. Logo NIE auf schwarzem Grund,
nicht verzerren/umfärben, ® behalten. Kein cluttered/clinical/neon/cartoon/gimmicky Look.
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
from tools.brief_app.core import seo_loader as SEOL
from tools.brief_app.core.ai import AIImagePlanItem, AIModule, AIQA

PLAN_NO = "01"
ASIN = "B000GCPX7M"
EXCEL = HERE / "listing.xlsx"


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="Clean white with a calm navy #283778 base band and a warm yellow #FFED39 accent. Identical across all 3 for a clean split test. Never a black background.",
        purpose="Win the click and signal trusted heritage + clear function at thumbnail size.",
        visual=(
            "Mock ALL 3 options. Product exactly as real: the 8 oz NUMOTIZINE jar — per brand "
            "rule ALWAYS show the front label (® intact), the lid, and a glimpse of the thick "
            "ointment texture. ONE callout each, jar dominant ~70%, calm and professional (never "
            "clinical or cluttered). Amazon slot-1 main = pure white / jar only.\n\n"
            "OPTION A — HERITAGE (trust): jar with a subtle 'Since 1905' seal. Badge (navy): "
            "'TRUSTED SINCE 1905'.\n"
            "OPTION B — FUNCTION: jar with an open lid + thick ointment + a cool-menthol cue. "
            "Badge (yellow/navy): '1.25% MENTHOL MUSCLE RUB'.\n"
            "OPTION C — ORIGIN: jar + US flag + 'FDA-registered facility' cue. Badge: "
            "'MADE IN THE USA'.\n\n"
            "Across all 3: jar ~70%, callout ~6%, same calm lighting."
        ),
        overlay="(one callout per option)",
        overlay_sub="3 hero options shipped — A/B test, keep the winner.",
        props=["A: jar + 'Since 1905' seal", "B: open jar + thick ointment + menthol cue", "C: jar + US flag + FDA-registered cue"],
        lighting="Soft, warm, professional studio light; the jar and ointment texture read clearly.",
        why_it_works=(
            "Three trust-first triggers: 100+ year heritage, the clear menthol muscle-rub "
            "function, and Made-in-USA origin — professional and glanceable, no hype."
        ),
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: the classic cooling menthol muscle rub",
        role="hook",
        background="Soft navy-tinted white with a warm yellow accent",
        purpose="Land the core, honest promise: temporary cooling relief for minor muscle & joint aches.",
        visual=(
            "The jar with a clean, calm cooling motif (subtle cool-blue vapor/cooling waves — not "
            "flashy). A short educational line: 'A 1.25% menthol topical analgesic for the "
            "temporary relief of minor aches and pains of muscles and joints.' Professional, "
            "reassuring, not clinical."
        ),
        overlay="COOLING MENTHOL RELIEF.",
        overlay_sub="1.25% menthol for the temporary relief of minor muscle & joint aches.",
        props=["jar", "subtle cooling-menthol motif", "educational one-liner"],
        lighting="Calm, clean; a gentle cool highlight to suggest the menthol cooling.",
        why_it_works=(
            "States exactly what it does in honest OTC language — reassuring and compliant, which "
            "matters most for a pain-relief buyer choosing a trusted classic."
        ),
    ),
    AIImagePlanItem(
        name="Image 3 — What it's for",
        role="educate",
        background="White with a warm yellow footer band",
        purpose="Educate on the honest use cases — where and when to use it.",
        visual=(
            "A clean body diagram or a small grid of relatable adults, with calm markers on the "
            "areas: 'Shoulders', 'Back', 'Arms & legs', 'Sore muscles', 'Joints'. Small note: "
            "'Also a traditional menthol chest rub.' Honest, educational, warm — real people, not "
            "clinical stock."
        ),
        overlay="FOR MUSCLES & JOINTS.",
        overlay_sub="Shoulders, back, arms, legs & joints — plus a traditional menthol chest rub.",
        props=["body/area markers", "relatable adults", "chest-rub note"],
        lighting="Bright, warm, editorial. Educational clarity.",
        why_it_works=(
            "Buyers want to know 'is this for my kind of ache?'. Showing the areas plainly makes "
            "the fit obvious and covers the traditional chest-rub use as a bonus."
        ),
    ),
    AIImagePlanItem(
        name="Image 4 — The thick, traditional paste",
        role="desire",
        background="Warm neutral, close-up texture",
        purpose="Own the format and defuse 'greasy / doesn't stay' — the paste stays where applied.",
        visual=(
            "A macro of the thick, traditional ointment on a fingertip / spread on skin, showing "
            "it holds its place. Callouts: 'Thick paste-like formula', 'Spreads smoothly, stays "
            "where applied', 'Removes easily with water'. Tactile, honest, clean."
        ),
        overlay="THICK PASTE, STAYS PUT.",
        overlay_sub="A traditional thick ointment that spreads smoothly and rinses off with water.",
        props=["ointment texture macro", "spread-on-skin shot", "3 texture callouts"],
        lighting="Warm close-up light that shows the thick, traditional texture.",
        why_it_works=(
            "Reviews mention greasy/sticky feel. Showing the thick paste stays targeted and rinses "
            "with water sets honest expectations and highlights the classic format."
        ),
        cvr="Turns the 'feel' objection into the traditional-format selling point.",
    ),
    AIImagePlanItem(
        name="Image 5 — How to use it",
        role="educate",
        background="White with a calm navy step strip",
        purpose="Make correct use clear — apply to the targeted area, ages 12+.",
        visual=(
            "Three simple steps: 1) Apply a thin layer to the affected area; 2) Massage gently "
            "until absorbed; 3) Rinse hands (and area, when done) with water. Small note: "
            "'Adults & children 12+. Use as directed on the label.' Calm, instructional, "
            "trustworthy."
        ),
        overlay="APPLY. MASSAGE. RELIEVE.",
        overlay_sub="Apply to the affected area, massage gently — adults & children 12+.",
        props=["3-step application", "targeted-area cue", "ages 12+ note"],
        lighting="Bright, even, instructional.",
        why_it_works=(
            "Clear directions build trust and set correct expectations (temporary, targeted "
            "relief), reducing disappointment and reflecting the brand's educational voice."
        ),
    ),
    AIImagePlanItem(
        name="Image 6 — 100+ years of trust",
        role="trust",
        background="Warm navy/white heritage panel",
        purpose="Stack the trust signals — the heart of this brand.",
        visual=(
            "A warm, dignified heritage layout: the jar with four trust badges — 'TRUSTED SINCE "
            "1905', 'MADE IN THE USA', 'OWN FDA-REGISTERED FACILITY', 'FIVE-GENERATION "
            "FAMILY-OWNED'. A subtle nod to Bemidji, Minnesota. Professional, reassuring, warm — "
            "never clinical."
        ),
        overlay="100+ YEARS OF TRUST.",
        overlay_sub="Made in the USA in our own FDA-registered facility, family-owned since 1905.",
        props=["jar", "4 heritage/trust badges", "subtle Minnesota nod"],
        lighting="Warm, premium, trustworthy.",
        why_it_works=(
            "For a pain-relief purchase, trust is decisive. A 100+ year, family-owned, "
            "US-made, FDA-registered heritage is the strongest, most honest reason to choose "
            "NUMOTIZINE over a nameless rub."
        ),
    ),
    AIImagePlanItem(
        name="Image 7 — Lifestyle close: back to what you love",
        role="close",
        background="Warm, bright real-life scene (not clinical, not a badge board)",
        purpose="Close on the EMOTIONAL payoff — relief that lets you get back to daily life. (Distinct from Image 6's heritage/trust angle.)",
        visual=(
            "A warm, real lifestyle moment: a relatable adult back to something they enjoy after "
            "easing a minor ache — gardening, a walk with grandkids, golf, light DIY. Natural, "
            "genuine, dignified — NOT clinical, NO badge stack (that's Image 6). The 8 oz jar sits "
            "naturally on a side table or in a bag in the scene. Small, quiet NUMOTIZINE logo "
            "(on light, never black). The feeling: comfort, ease, getting on with your day."
        ),
        overlay="BACK TO WHAT YOU LOVE.",
        overlay_sub="Ease minor muscle & joint aches and get on with your day — the NUMOTIZINE way.",
        props=["real adult enjoying an activity (garden/walk/golf/DIY)", "jar resting naturally in the scene", "quiet NUMOTIZINE logo on light"],
        lighting="Warm, natural daylight; genuine and inviting — the opposite of clinical.",
        why_it_works=(
            "Image 6 owns the heritage/trust proof; Image 7 owns the EMOTIONAL outcome — the life "
            "the buyer wants back. Two distinct closers instead of two trust images, so the plan "
            "ends on feeling, not repetition."
        ),
    ),
]


CREATIVE_MODULES = [
    AIModule(
        name="Module 1 — Brand banner",
        role="a+_banner",
        headline="TRUSTED PAIN RELIEF SINCE 1905.",
        body=(
            "NUMOTIZINE is a 1.25% menthol topical analgesic for the temporary relief of minor "
            "aches and pains of muscles and joints. A thick, traditional muscle rub, made in the "
            "USA in our own FDA-registered facility — trusted by families for over 100 years."
        ),
        visual="Wide, calm banner: the 8 oz jar (front + lid) right, navy headline left on white, warm yellow accent. NUMOTIZINE logo upper-left on light (never black).",
        alt="NUMOTIZINE Pain Relief Ointment banner: 1.25% menthol muscle rub, made in the USA, trusted since 1905.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): Why NUMOTIZINE",
        role="a+_carousel",
        headline="WHY NUMOTIZINE",
        body=(
            "Tile 1: <b>1.25% MENTHOL</b> — Temporary relief of minor muscle &amp; joint aches.<br/>"
            "Tile 2: <b>COOLING MUSCLE RUB</b> — The classic cooling menthol sensation.<br/>"
            "Tile 3: <b>THICK PASTE</b> — Spreads smoothly, stays where applied.<br/>"
            "Tile 4: <b>EASY TO RINSE</b> — Removes with water; 8 oz jar.<br/>"
            "Tile 5: <b>SINCE 1905</b> — Made in the USA, family-owned, FDA-registered facility."
        ),
        visual="5 clean tiles, navy/yellow accents, simple professional icons (menthol leaf · cooling wave · jar · water drop · heritage seal). Not cluttered.",
        alt="Five A+ tiles: 1.25% menthol, cooling muscle rub, thick paste, easy to rinse, since 1905.",
    ),
    AIModule(
        name="Module 3 — Banner: How to use",
        role="a+_banner",
        headline="APPLY. MASSAGE. RELIEVE.",
        body=(
            "Apply a thin layer to the affected area and massage gently until absorbed. The thick, "
            "traditional formula stays where applied and rinses off with water. For adults and "
            "children 12 and older — use as directed on the label."
        ),
        visual="Banner with a calm 3-step application (apply · massage · rinse), warm relatable hands, navy/white styling. Educational, not clinical.",
        alt="A+ banner showing how to use NUMOTIZINE: apply, massage, relieve; ages 12+.",
    ),
    AIModule(
        name="Module 4 — Banner: 100+ years of trust",
        role="a+_banner",
        headline="MADE IN THE USA. TRUSTED SINCE 1905.",
        body=(
            "NUMOTIZINE is made in the USA in our own FDA-registered facility by Hobart "
            "Laboratories — a five-generation, family-owned company in Bemidji, Minnesota. Over "
            "100 years of dependable, high-quality relief."
        ),
        visual="Banner with warm heritage badges (Since 1905 · Made in USA · FDA-registered facility · Family-owned) around the jar. Dignified, warm, professional.",
        alt="A+ banner: NUMOTIZINE made in the USA in an FDA-registered facility, family-owned since 1905.",
    ),
    AIModule(
        name="Module 5 — Carousel (5 tiles): When to reach for it",
        role="a+_carousel",
        headline="WHEN TO REACH FOR IT",
        body=(
            "Tile 1: <b>AFTER ACTIVITY</b> — Sore muscles after exercise or physical work.<br/>"
            "Tile 2: <b>EVERYDAY ACHES</b> — Minor muscle stiffness and discomfort.<br/>"
            "Tile 3: <b>JOINTS</b> — Temporary relief of minor joint aches.<br/>"
            "Tile 4: <b>BACK, SHOULDERS &amp; LEGS</b> — Targeted areas, big and small.<br/>"
            "Tile 5: <b>CHEST RUB</b> — The traditional menthol-vapor use."
        ),
        visual="5 warm, relatable lifestyle tiles (after activity · everyday · joints · back/shoulders · chest rub), consistent calm styling.",
        alt="Five A+ tiles: when to use NUMOTIZINE — after activity, everyday aches, joints, back/shoulders/legs, chest rub.",
    ),
    AIModule(
        name="Module 6 — Benefits recap (bridges into the Q&A)",
        role="a+_banner",
        headline="KEEP A CLASSIC IN THE CABINET.",
        body=(
            "One traditional jar, many everyday moments: cooling 1.25% menthol relief for minor "
            "muscle and joint aches, a thick paste that stays where you put it and rinses off with "
            "water, and a chest-rub tradition — trusted, made in the USA, since 1905."
            # A smart line bridging into the Q&A is appended automatically (house rule).
        ),
        visual="Warm benefits-recap banner: the 8 oz jar centre, 4 quiet benefit icons (cooling menthol · thick paste · rinses off · since 1905), navy/yellow on white. Calm, not cluttered.",
        alt="A+ benefits recap banner for NUMOTIZINE: cooling menthol, thick paste, rinses off, since 1905.",
    ),
    AIModule(
        name="Module 7 — Premium Q&A",
        role="a+_qa",
        headline="QUESTIONS BEFORE YOU BUY",
        body=(
            "<b>Q.</b> What is NUMOTIZINE for?<br/>"
            "<b>A.</b> It's a 1.25% menthol topical analgesic for the temporary relief of minor "
            "aches and pains of muscles and joints.<br/><br/>"
            "<b>Q.</b> How do I use it?<br/>"
            "<b>A.</b> Apply a thin layer to the affected area and massage gently until absorbed. "
            "For adults and children 12 and older — use as directed on the label.<br/><br/>"
            "<b>Q.</b> Is it greasy?<br/>"
            "<b>A.</b> It's a thick, traditional paste that spreads smoothly, stays where applied, "
            "and rinses off with water.<br/><br/>"
            "<b>Q.</b> Can I use it as a chest rub?<br/>"
            "<b>A.</b> Yes — NUMOTIZINE releases a traditional menthol vapor and has long been "
            "used as a classic chest rub.<br/><br/>"
            "<b>Q.</b> Who makes it?<br/>"
            "<b>A.</b> Hobart Laboratories — a five-generation, family-owned company, made in the "
            "USA in our own FDA-registered facility since 1905."
        ),
        visual="Vertical Q/A table, navy divider lines, small navy Q. and warm yellow A. labels. Clean, easy to read.",
        alt="Premium Q&A module for NUMOTIZINE Pain Relief Ointment.",
    ),
]


def main() -> None:
    print("Lade NUMOTIZINE + SEO-Sheet…")
    cust = load_customer("numotizine")
    brief = parse_excel(EXCEL)
    seo = SEOL.load_seo(EXCEL)
    OUT = HERE / f"{PLAN_NO}_{ASIN}_Image Plan.pdf"
    print(f"  Produkt: {brief.product_name}  ASIN: {ASIN}  Marktplatz: {cust.marketplace}")
    print(f"  SEO-Titel({len(seo.title)}) + Bullets={len(seo.bullets)} | new_brand={cust.new_brand} | logo={cust.logo_path}")

    builder = BriefBuilder(cust, brief, OUT, ai=None)
    builder._ai_title = seo.title
    builder._ai_bullets = SEOL.as_bullets_html(seo)
    builder._ai_images = IMAGES
    builder._ai_modules = list(CREATIVE_MODULES)
    builder._ai_qa = [
        AIQA(q="What is NUMOTIZINE Pain Relief Ointment used for?",
             a="It is a 1.25% menthol topical analgesic for the temporary relief of minor aches and pains of muscles and joints — associated with sore muscles, muscle stiffness, minor arthritis discomfort, backache, strains and sprains."),
        AIQA(q="How do I apply it?",
             a="Apply a thin layer to the affected area and massage gently until absorbed, up to as directed on the label. It is for adults and children 12 years and older."),
        AIQA(q="Is it greasy or hard to remove?",
             a="No. It is a thick, traditional paste that spreads smoothly and stays where applied, and it rinses off easily with water."),
        AIQA(q="Can it be used as a chest rub?",
             a="Yes. NUMOTIZINE releases a traditional menthol vapor and has long been used as a classic menthol chest rub, in addition to a muscle and joint rub."),
        AIQA(q="How big is the jar?",
             a="It comes in a generous 8 oz jar."),
        AIQA(q="Who makes NUMOTIZINE and where?",
             a="It is made by Hobart Laboratories, Inc. — a five-generation, family-owned company in Bemidji, Minnesota — in the USA in our own FDA-registered facility, trusted since 1905."),
    ]
    builder._ai_backend = seo.backend
    builder.copy_source_label = "SEO-Sheet (Titel/Bullets/Backend) + hand-written creative (OTC-compliant, EN)"

    print("Baue Branded PDF…")
    pdf_path = builder.build()
    size_kb = pdf_path.stat().st_size // 1024
    import re
    pages = len(re.findall(rb'/Type\s*/Page[^s]', pdf_path.read_bytes()))
    print(f"Gebaut: {pdf_path}")
    print(f"  Seiten: {pages}  Größe: {size_kb} KB")


if __name__ == "__main__":
    main()
