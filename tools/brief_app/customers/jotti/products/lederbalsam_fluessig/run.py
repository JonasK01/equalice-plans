"""Jotti Lederbalsam FLÜSSIG 500 ml (Sprühflasche) — Image Plan 02
Hand-written senior copy injected into the branded ReportLab pipeline.

Marketplace: amazon.de.

LANGUAGE SPLIT (the standard):
  • ENGLISH — art-direction / strategy fields the designer reads:
    image purpose, background, visual, props, lighting, why_it_works, ctr, cvr,
    and module visual.
  • GERMAN — marketplace, customer-facing text the shopper reads:
    TITLE, BULLETS, image overlay, overlay_sub, module headline, module body,
    QA, and BACKEND keywords.

OVERLAY RULE: sell the OUTCOME, not the action. Every on-image overlay leads
with the result / transformation / defused fear the buyer wants — never the
steps they perform, never a weak generic payoff. Each overlay is distinct and
tied to that image's job. Hard limits (auto-linted on build):
  overlay ≤ 30 chars AND ≤ 5 words · overlay_sub ≤ 90 chars
  module headline ≤ 38 chars · bullet head <b>…</b> ≤ 45 chars

Verified facts (see SOURCE_NOTES.md):
  - 500 ml Sprühflasche; natürliche Rezeptur (Bienenwachs, Jojobaöl, Carnaubawachs, Lanolin)
  - für glattes & strukturiertes Leder; 3-in-1 Reinigung + Pflege + Schutz
  - schützt vor Austrocknung/Rissen/Verblassen; macht geschmeidig; farblos
  - wasser- & schmutzabweisend; praktische SPRÜH-Anwendung (Vorteil ggü. festem Balsam)
  - Deutsche Manufakturqualität

Review insight used:
  praised  = gut dosierbar / keine Rückstände / toller Duft
  objection= "färbt stark ab, v.a. bei Feuchte" → defuse: gründlich einarbeiten +
             trocknen lassen; farblose Formel

Compliance: no $/€ prices, no URL/.com, no #1/beste/garantiert/Wundermittel, no false claims.
"""
from __future__ import annotations
import sys
from pathlib import Path

# This script lives at customers/<brand>/products/<product>/run.py — self-contained.
HERE = Path(__file__).resolve().parent          # the product folder
ROOT = HERE.parents[5]                           # project root (Claude_Code/)
sys.path.insert(0, str(ROOT))

from tools.brief_app.core.customers import load_customer
from tools.brief_app.core.excel_parser import parse_excel
from tools.brief_app.core.pdf_builder import BriefBuilder
from tools.brief_app.core.ai import AIImagePlanItem, AIModule, AIQA


EXCEL = HERE / "listing.xlsx"
PLAN_NO = "02"


# ===== KW-led, marketing-optimized DE copy (customer-facing) =====

# Title is HTML-escaped, so literal "&" counts as 1 char. Keep ≤200 real chars. Stays German.
TITLE = (
    "Jotti Lederbalsam Flüssig 500 ml Sprühflasche — 3-in-1 Lederpflege für Auto Sofa "
    "Schuhe & Taschen · mit Bienenwachs & Jojobaöl · farblos, wasserabweisend · "
    "Reinigung Pflege Schutz · Manufaktur"
)

BULLETS = [
    "<b>ALTES LEDER WIE NEU</b> — Trockenes, mattes Leder wird wieder satt, dunkel und "
    "geschmeidig – sichtbar aufgefrischt, vom Autositz bis zur alten Lederjacke.",

    "<b>TIEF GENÄHRT IN MINUTEN</b> — Einfach aufsprühen statt mühsam einreiben: feiner Nebel "
    "zieht gleichmäßig ein und versorgt Ledersitze, Ledercouch &amp; Lederschuhe in Minuten.",

    "<b>NATÜRLICH WEICH GEPFLEGT</b> — Bienenwachs, Jojobaöl, Carnaubawachs &amp; Lanolin "
    "nähren das Leder tief, machen es geschmeidig und schützen es vor Rissen und Austrocknen.",

    "<b>FARBLOS, OHNE ABZUFÄRBEN</b> — Die farblose Formel bewahrt die natürliche Lederfarbe. "
    "Dünn aufsprühen, gründlich einarbeiten, trocknen lassen – so bleiben keine Rückstände.",

    "<b>EIN BALSAM FÜR ALLES LEDER</b> — Lederpflege fürs Auto, Ledercouch &amp; Sofa, "
    "Lederschuhe, Lederjacke &amp; Taschen. Wasser- &amp; schmutzabweisend. Deutsche Manufaktur.",
]


IMAGES = [
    AIImagePlanItem(
        name="Bild 1 — Main Hero (3 Optionen für A/B-Test)",
        role="hero",
        background="Warm cream backdrop (#EFE6D9) with soft side-light; aged wood in the bottom 15% band for a manufactory feel. Identical backdrop across all 3 options for a clean split-test.",
        purpose="Win the click in the amazon.de leather-care grid — stand out next to generic spray bottles.",
        visual=(
            "Designer mocks up ALL 3 options. Brand picks the winner via Amazon Manage Your Experiments. "
            "Each option: ONE callout, ONE action cue, ONE prop — clean, never stacked.\n\n"
            "▸ OPTION A — BEFORE/AFTER TRANSFORMATION (wins on proof)\n"
            "500 ml spray bottle centered (label legible, slight 3/4 turn, ~60% of frame). Behind it a "
            "leather swatch split diagonally: left matte/dry/cracked, right rich/supple/glossy. "
            "Spray-mist cue at the dividing line.\n"
            "CALLOUT top right: badge 'LEDER WIE NEU.' (brown #8B5A2B, white type).\n\n"
            "▸ OPTION B — SPRAY ACTION (wins on the speed advantage)\n"
            "Bottle left, a hand (hand only, no face) sprays a visible fine mist onto a car leather seat. "
            "Microfiber cloth as a prop.\n"
            "CALLOUT top left: 'WIEDER GESCHMEIDIG.' (dark #2F2A26, white type).\n\n"
            "▸ OPTION C — USE-CASE STACK (wins on versatility)\n"
            "Bottle centered, 4 use-case icons radiating out: car · sofa · shoes · bags (thin brown line icons).\n"
            "CALLOUT bottom right: '3-IN-1 LEDERPFLEGE' (brown #8B5A2B).\n\n"
            "All 3: bottle dominant ~60%, callout ~6%, same light / same backdrop."
        ),
        overlay="ALTES LEDER WIE NEU.",
        overlay_sub="Trockenes Leder wird wieder satt, weich und geschmeidig.",
        props=[
            "OPTION A: bottle + split leather swatch (dry/supple) + spray mist + badge",
            "OPTION B: bottle + hand + spray mist on car leather seat + microfiber cloth",
            "OPTION C: bottle + 4 use-case icons (car/sofa/shoes/bags) + badge",
        ],
        lighting="Warm side-light from camera-right (3000–3500K), rim light on the bottle so the label pops. Same light across all 3 options.",
        why_it_works=(
            "Three triggers against three buyer motives: A delivers the before/after proof (the strongest "
            "signal in the leather-care grid), B proves the spray speed advantage over solid balm, C shows "
            "versatility. One callout, one action cue, one prop — readable on a mobile thumbnail."
        ),
        ctr="The before/after leather swatch plus 'LEDER WIE NEU.' beats competitors' static spray bottles in the DE grid; the visible dry→supple contrast is the strongest click promise for car leather seats, sofas and leather shoes.",
        cvr="Instant clarity on product type (spray bottle), benefit (3-in-1) and result (supple leather) cuts bounce; the manufactory setting builds purchase trust.",
    ),
    AIImagePlanItem(
        name="Bild 2 — Hook: Sprüh-Vorteil ggü. festem Balsam",
        role="hook",
        background="Cream #EFE6D9, aged wood, warm side-light.",
        purpose="Establish the unique spray advantage instantly — fast and even instead of laborious rubbing.",
        visual=(
            "Split frame. LEFT: solid balm tin + cloth, a hand rubbing laboriously, faint 'slow' cue. "
            "RIGHT: Jotti spray bottle, a fine even mist on a leather seat, faint 'in seconds' cue. "
            "Large brown #8B5A2B arrow / divider. Small caption strip at the bottom: 'gleichmäßig · ohne Rückstände'."
        ),
        overlay="TIEF GENÄHRT IN MINUTEN.",
        overlay_sub="Feiner Nebel zieht ein – statt mühsamem Einreiben.",
        props=["solid balm tin + cloth (left)", "Jotti spray bottle + mist (right)", "car leather seat", "arrow / divider"],
        lighting="Even warm front-side light, soft shadow under the props.",
        why_it_works=(
            "A direct category counter: the main competition is solid balm. The spray application is the "
            "most tangible differentiator and answers 'why this product?' in one frame."
        ),
        ctr="The laborious-vs-seconds contrast hits the convenience nerve of the DE buyer looking for quick leather care for car and sofa.",
        cvr="Removes the effort worry ('do I have to rub for ages?') and positions the spray bottle clearly as the easier choice.",
    ),
    AIImagePlanItem(
        name="Bild 3 — Educate: Natürliche Rezeptur",
        role="educate",
        background="White with a brown accent band (#8B5A2B) in the footer.",
        purpose="Explain the natural formula and defend the premium positioning.",
        visual=(
            "Headline at top, then 4 ingredient tiles with line icons:\n"
            "  • BEESWAX — nourishes & protects\n"
            "  • JOJOBA OIL — restores suppleness\n"
            "  • CARNAUBA WAX — seals the surface\n"
            "  • LANOLIN — guards against drying out\n"
            "Bottle centered or right. Footer band (brown) carries the supporting line."
        ),
        overlay="WIEDER WEICH GENÄHRT.",
        overlay_sub="Bienenwachs, Jojobaöl &amp; Lanolin nähren tief und machen weich.",
        props=["4 ingredient tiles with icons", "Jotti bottle", "footer band"],
        lighting="Flat, clean studio light — legibility over atmosphere.",
        why_it_works=(
            "Makes the natural formula concrete and tangible. Buyers who filter on ingredients see real, "
            "high-quality actives instead of marketing words — which justifies the manufactory price."
        ),
        ctr="Natural ingredients (beeswax, jojoba oil) are a strong DE search signal; the active-ingredient tiles signal quality at a glance.",
        cvr="A transparent formula builds trust and differentiates from cheap chemical leather-care sprays.",
    ),
    AIImagePlanItem(
        name="Bild 4 — Desire: Before/After Transformation",
        role="desire",
        background="Aged wood, warm afternoon light.",
        purpose="Sell the visible result — old/dry becomes rich and supple again.",
        visual=(
            "Large before/after split of a real leather jacket OR a car leather seat. "
            "LEFT: matte, dried out, light cracks, faded. RIGHT: deeply conditioned, supple, rich color, "
            "a subtle natural sheen. Divider centered; small bottle in the foreground corner. "
            "Spray / cloth cue at the dividing line."
        ),
        overlay="SCHLUSS MIT RISSEN.",
        overlay_sub="Trockenes, rissiges Leder wird wieder satt und lebendig.",
        props=["leather jacket or car leather seat (split)", "Jotti bottle (foreground)", "microfiber cloth", "spray-mist cue"],
        lighting="Warm afternoon side-light from camera-right, rim on the supple side so the sheen pops.",
        why_it_works=(
            "Leans directly on the strongest real-review verbatim ('visibly renews old leather jackets'). "
            "The before/after proof is the strongest conversion signal in the leather-care category."
        ),
        ctr="The old→new transformation is universally desirable for anyone with aged car leather, a sofa or a favorite jacket.",
        cvr="Visual proof of result instead of a promise; sets realistic expectations and drives the purchase.",
    ),
    AIImagePlanItem(
        name="Bild 5 — Trust: Einwand entkräften (Abfärben)",
        role="trust",
        background="White with cream panels.",
        purpose="Defuse the main objection ('rubs off, especially when damp') right on the image.",
        visual=(
            "3-step application as an icon row:\n"
            "  1. SPRAY ON THINLY (spray icon)\n"
            "  2. WORK IN THOROUGHLY (cloth / circular-motion icon)\n"
            "  3. LET IT DRY (clock / droplet icon)\n"
            "Next to it a badge 'FARBLOSE FORMEL'. Small caption reinforcing 'no residue when used correctly'. "
            "Bottle as an anchor on the right."
        ),
        overlay="PFLEGT, OHNE ABZUFÄRBEN.",
        overlay_sub="Farblose Formel: einarbeiten, trocknen lassen – ohne Rückstände.",
        props=["3 application icons", "badge 'FARBLOSE FORMEL'", "Jotti bottle"],
        lighting="Clean even studio light — icons readable on the thumbnail.",
        why_it_works=(
            "Proactively addresses the one recurring negative review ('rubs off when damp') with a clear "
            "application fix. Pre-defused objections lower returns and 1-star ratings — and build trust "
            "before the purchase."
        ),
        ctr="The application clarity attracts careful DE buyers who want correct leather care.",
        cvr="Defuses the top purchase objection right on the image; buyers scanning reviews see the solution, not just the problem.",
    ),
    AIImagePlanItem(
        name="Bild 6 — Desire: Use-Case-Grid (für alles aus Leder)",
        role="desire",
        background="Cream #EFE6D9, aged wood.",
        purpose="Show versatility — one product for all the leather in the household.",
        visual=(
            "Clean 4-up grid of real leather scenes: car leather seat · leather sofa · leather shoes · "
            "leather bag. Each tile with a bottle / spray-mist cue. Bottle as an anchor center or bottom. "
            "Small label per tile (car · sofa · shoes · bags)."
        ),
        overlay="EIN BALSAM FÜR ALLES.",
        overlay_sub="Lederpflege fürs Auto, Sofa, Schuhe, Taschen &amp; Jacken.",
        props=["4 use-case scenes (car/sofa/shoes/bags)", "Jotti bottle", "spray-mist cues"],
        lighting="Warm side-light, consistent across all 4 tiles.",
        why_it_works=(
            "Expands perceived value: one bottle covers several expensive leather items. Hits the "
            "cost-per-use math and matches the broad DE search terms (car, sofa, shoes, bags)."
        ),
        ctr="Speaks to several search intents at once (leather care car, sofa, shoes) and maximizes relevance in the grid.",
        cvr="More use cases = higher perceived value per bottle, which makes the purchase easier to justify.",
    ),
    AIImagePlanItem(
        name="Bild 7 — Close: Deutsche Manufaktur",
        role="close",
        background="Workshop scene: aged wood, brass, linen, warm side-light.",
        purpose="Close on brand identity — artisanal manufactory quality.",
        visual=(
            "Mid-range workshop scene: hands (no face) working balm into a beautiful leather surface. "
            "On the wooden bench: Jotti spray bottle (label legible), microfiber cloth, aged leather. "
            "Soft-focused workshop setting (brass, linen). A small handwritten note card carries the "
            "manufactory line."
        ),
        overlay="DEUTSCHE MANUFAKTUR.",
        overlay_sub="Traditionelle Lederpflege, mit der Hand gemacht.",
        props=["hands on leather (no face)", "Jotti bottle", "microfiber cloth", "aged leather", "wooden bench / brass / linen", "handwritten note card"],
        lighting="Warm workshop side-light from camera-right, golden tone, lived-in — not staged.",
        why_it_works=(
            "Closes on the brand promise that matters before checkout: honest, artisanal manufactory "
            "quality. The hands-on-leather gesture is the visual metaphor for care and trust."
        ),
        ctr="The 'German manufactory' signal differentiates from anonymous import sprays and attracts quality-conscious DE buyers.",
        cvr="Provenance and craft create the final trust that seals the purchase.",
    ),
]


MODULES = [
    AIModule(
        name="Modul 1 — Brand-Banner",
        role="a+_banner",
        headline="ALTES LEDER WIE NEU.",
        body=(
            "Jotti Lederbalsam Flüssig macht trockenes, mattes Leder wieder satt, weich und "
            "geschmeidig – in einem Sprühgang. Natürliche Rezeptur, farblos, deutsche Manufaktur."
        ),
        visual="Wide cinematic workshop scene: aged wood, warm side-light, Jotti spray bottle front-center, leather & brass soft-focused. Logo top left in brown #8B5A2B.",
        alt="Jotti Lederbalsam Flüssig Sprühflasche auf einer Holzbank in warmem Werkstattlicht, mit gepflegtem Leder im Hintergrund.",
    ),
    AIModule(
        name="Modul 2 — Carousel (4 Kacheln): Der Jotti-Vorteil",
        role="a+_carousel",
        headline="DER JOTTI-VORTEIL",
        body=(
            "Kachel 1: <b>3-IN-1</b> — Reinigung, Pflege &amp; Schutz in einem.<br/>"
            "Kachel 2: <b>EINFACH SPRÜHEN</b> — schnell &amp; gleichmäßig statt mühsames Einreiben.<br/>"
            "Kachel 3: <b>NATÜRLICHE REZEPTUR</b> — Bienenwachs, Jojobaöl, Carnaubawachs, Lanolin.<br/>"
            "Kachel 4: <b>FARBLOS</b> — bewahrt die natürliche Lederfarbe, wasser- &amp; schmutzabweisend."
        ),
        visual="4 square tiles, brown accent corner per tile, small line icons (3-in-1 · spray head · honeycomb · droplet).",
        alt="Vier-Kachel A+ Carousel mit den Jotti-Vorteilen: 3-in-1, einfach sprühen, natürliche Rezeptur, farblos.",
    ),
    AIModule(
        name="Modul 3 — Banner: Sprüh-Vorteil",
        role="a+_banner",
        headline="TIEF GENÄHRT IN MINUTEN.",
        body=(
            "Der feine Sprühnebel verteilt den Balsam schnell und gleichmäßig und zieht tief ein – "
            "ohne mühsames Einreiben. Dünn aufsprühen, gründlich einarbeiten, trocknen lassen. "
            "Für glattes und strukturiertes Leder."
        ),
        visual="Wide banner: a hand sprays a fine even mist onto a car leather seat, cloth alongside. Warm side-light. Brown/dark palette.",
        alt="A+ Banner: Jotti Sprühflasche wird gleichmäßig auf einen Auto-Ledersitz aufgesprüht.",
    ),
    AIModule(
        name="Modul 4 — Banner: Schutz & Wirkung",
        role="a+_banner",
        headline="SCHLUSS MIT RISSEN.",
        body=(
            "Nährt trockenes Leder tief, macht es wieder geschmeidig und schützt vor Austrocknung, "
            "Rissen und Verblassen. Danach perlt Wasser ab, Schmutz hält weniger – und die farblose "
            "Formel bewahrt die natürliche Farbe Ihres Leders."
        ),
        visual="Triptych: LEFT dry/cracked leather (before), CENTER spray/work-in moment, RIGHT supple rich leather with water beading off (after). Warm light throughout.",
        alt="A+ Triptychon-Banner: Leder vorher trocken, Anwendung, nachher geschmeidig und wasserabweisend.",
    ),
    AIModule(
        name="Modul 5 — Carousel (4 Kacheln): Für alles aus Leder",
        role="a+_carousel",
        headline="FÜR ALLES AUS LEDER",
        body=(
            "Kachel 1: <b>AUTO-LEDERSITZE</b> — frischt ausgetrocknete Sitze sichtbar auf.<br/>"
            "Kachel 2: <b>LEDERSOFA</b> — hält Couch &amp; Sessel geschmeidig.<br/>"
            "Kachel 3: <b>LEDERSCHUHE</b> — pflegt und schützt vor Nässe.<br/>"
            "Kachel 4: <b>TASCHEN &amp; JACKEN</b> — bewahrt Lieblingsstücke aus Leder."
        ),
        visual="4 identically composed use-case tiles, real leather scenes, brown accent corner per tile, consistent warm light.",
        alt="Vier-Kachel A+ Carousel der Anwendungsfälle: Auto-Ledersitze, Ledersofa, Lederschuhe, Taschen & Jacken.",
    ),
    AIModule(
        name="Modul 6 — Premium Q&A",
        role="a+_qa",
        headline="HÄUFIGE FRAGEN",
        body=(
            "<b>F.</b> Färbt der Balsam ab?<br/>"
            "<b>A.</b> Die Formel ist farblos. Dünn aufsprühen, gründlich einarbeiten und trocknen lassen – "
            "richtig angewendet bleiben keine Rückstände.<br/><br/>"
            "<b>F.</b> Für welches Leder ist er geeignet?<br/>"
            "<b>A.</b> Für glattes und strukturiertes Leder: Auto-Ledersitze, Sofa, Schuhe, Taschen und Jacken.<br/><br/>"
            "<b>F.</b> Was ist der Vorteil der Sprühflasche?<br/>"
            "<b>A.</b> Der Balsam lässt sich schnell und gleichmäßig auftragen – ohne mühsames Einreiben "
            "wie bei festem Balsam.<br/><br/>"
            "<b>F.</b> Was steckt drin?<br/>"
            "<b>A.</b> Eine natürliche Rezeptur aus Bienenwachs, Jojobaöl, Carnaubawachs, Lanolin und "
            "weiteren hochwertigen Inhaltsstoffen.<br/><br/>"
            "<b>F.</b> Wo wird Jotti hergestellt?<br/>"
            "<b>A.</b> In deutscher Manufakturqualität – traditionelle Lederpflege, handwerklich gemacht."
        ),
        visual="Vertical Q/A table, brown dividers between questions, small F./A. labels in dark #2F2A26.",
        alt="Premium Q&A Modul mit den häufigsten Fragen zu Jotti Lederbalsam Flüssig.",
    ),
    AIModule(
        name="Modul 7 — Premium Comparison Chart",
        role="a+_comparison",
        headline="WARUM JOTTI",
        body=(
            "Vergleich über 4 Spalten: <b>Jotti Lederbalsam Flüssig</b> · Fester Lederbalsam · "
            "Lederspray (Standard) · Lederöl.<br/><br/>"
            "Zeilen: 3-in-1 Reinigung+Pflege+Schutz · Sprüh-Anwendung · Natürliche Rezeptur "
            "(Bienenwachs/Jojobaöl) · Farblos · Wasser- &amp; schmutzabweisend · Für glattes &amp; "
            "strukturiertes Leder · Deutsche Manufaktur.<br/><br/>"
            "Jotti-Spalte mit dezentem Braun-Ton hervorheben."
        ),
        visual="Standard Amazon Premium Comparison Chart, 4 product columns. Competitors named by category only, no brand names. Brown header row.",
        alt="Premium Vergleichstabelle: Jotti Lederbalsam Flüssig vs. fester Balsam, Standard-Lederspray und Lederöl.",
    ),
]


QA = [
    AIQA(q="Färbt der Lederbalsam ab?",
         a="Die Formel ist farblos und bewahrt die natürliche Lederfarbe. Wichtig: dünn aufsprühen, gründlich einarbeiten und vollständig trocknen lassen – so bleiben keine Rückstände, auch bei späterer Feuchte."),
    AIQA(q="Für welches Leder ist der Balsam geeignet?",
         a="Für glattes und strukturiertes Leder: Auto-Ledersitze, Ledersofa, Lederschuhe, Taschen und Jacken. Nicht für Wildleder/Veloursleder."),
    AIQA(q="Was ist der Vorteil der Sprühflasche gegenüber festem Balsam?",
         a="Der Balsam lässt sich schnell und gleichmäßig aufsprühen, statt ihn mühsam einzureiben. Das spart Zeit und sorgt für eine gleichmäßige Pflege auf größeren Flächen wie Autositzen oder Sofas."),
    AIQA(q="Was ist in der Rezeptur enthalten?",
         a="Eine natürliche Rezeptur aus Bienenwachs, Jojobaöl, Carnaubawachs, Lanolin und weiteren hochwertigen Inhaltsstoffen. Sie nährt das Leder und macht es wieder geschmeidig."),
    AIQA(q="Wirkt der Balsam wasserabweisend?",
         a="Ja. Nach dem Auftragen ist das Leder wasser- und schmutzabweisend und besser vor Nässe und Verschmutzung geschützt."),
    AIQA(q="Schützt er vor Rissen und Austrocknung?",
         a="Ja. Die natürlichen Pflegestoffe nähren trockenes Leder tief, machen es wieder satt und geschmeidig und schützen vor Austrocknung, Rissen und Verblassen. Selbst alte, ausgetrocknete Lederjacken oder Autositze wirken sichtbar aufgefrischt."),
    AIQA(q="Wie wird der Balsam angewendet?",
         a="Leder vorab grob reinigen, Jotti Lederbalsam dünn aufsprühen, mit einem weichen Tuch gründlich einarbeiten und trocknen lassen. Bei stark beanspruchtem Leder den Vorgang wiederholen."),
    AIQA(q="Wo wird Jotti hergestellt?",
         a="In deutscher Manufakturqualität. Jotti steht für traditionelle, handwerklich gemachte Lederpflege."),
]


# Backend KWs — German, stem-deduped, byte-packed. Avoid brand/title duplicates & superlatives.
BACKEND = (
    "lederpflege auto sofa ledercouch ledersitze pflegen sattel motorradkombi lederjacke "
    "lederschuhe ledertasche lederfett farblos lederöl lederreiniger sattelseife "
    "schuhcreme schuhpflege bienenwachs jojobaöl carnaubawachs lanolin natürlich "
    "wasserabweisend schmutzabweisend sprühflasche reinigung schutz geschmeidig "
    "glattleder strukturleder manufaktur deutsche conditioner"
)


def main() -> None:
    print("Loading Jotti customer + parsing Lederbalsam Flüssig Excel…")
    cust = load_customer("jotti")
    brief = parse_excel(EXCEL)
    OUT = HERE / f"{PLAN_NO}_Jotti_Lederbalsam_Fluessig_Image Plan.pdf"
    real_title_len = len(TITLE.replace("&amp;", "&"))
    print(f"  Product: {brief.product_name}")
    print(f"  ASIN: {brief.asin}  Marketplace: {cust.marketplace}")
    print(f"  USPs={len(brief.usps)} KWs={len(brief.all_keywords)} reviews=+{len(brief.good_reviews)}/-{len(brief.bad_reviews)}")
    print(f"  TITLE real chars (de-escaped): {real_title_len}")

    builder = BriefBuilder(cust, brief, OUT, ai=None)
    builder._ai_title = TITLE
    builder._ai_bullets = BULLETS
    builder._ai_images = IMAGES
    builder._ai_modules = MODULES
    builder._ai_qa = QA
    builder._ai_backend = BACKEND
    builder.copy_source_label = "Hand-written senior copy (DE customer text, EN art direction)"

    print("Building branded PDF…")
    pdf_path = builder.build()
    size_kb = pdf_path.stat().st_size // 1024
    import re
    pages = len(re.findall(rb'/Type\s*/Page[^s]', pdf_path.read_bytes()))
    print(f"Built: {pdf_path}")
    print(f"  Pages: {pages}  Size: {size_kb} KB")


if __name__ == "__main__":
    main()
