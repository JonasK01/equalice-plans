"""Jotti Möbelwachs 200 ml (fest, Wachs) — Image Plan 03
Hand-written senior copy injected into the branded ReportLab pipeline.

Marketplace: amazon.de.

LANGUAGE SPLIT (house standard):
  • ENGLISH  → art-direction / strategy fields a designer reads:
       image purpose, background, visual, props, lighting, why_it_works, ctr, cvr,
       and module `visual`. Written as a senior art director briefing a designer.
  • GERMAN   → everything the marketplace/customer sees:
       TITLE, BULLETS, image overlay + overlay_sub, module headline + body, QA, BACKEND.

OVERLAY DOCTRINE — sell the OUTCOME, not the action.
  Every overlay leads with the RESULT / transformation / defused fear, never the steps.
  Hard limits (auto-linted on build): overlay ≤30 chars AND ≤5 words; overlay_sub ≤90;
  module headline ≤38; bullet head <b>…</b> ≤45.

Verified facts (see SOURCE_NOTES.md):
  - 200 ml festes Möbelwachs; natürliche Rezeptur (Bienenwachs & Jojobaöl)
  - universell für viele Holzarten; 3-in-1 Reinigung + Pflege + Schutz
  - schützt vor Austrocknung/Rissen/Verblassen; ANTISTATISCH (weniger Staub)
  - FARBAUFFRISCHEND mit seidenmattem Glanz; wasser- & schmutzabweisend
  - einfache Tuch-Anwendung, für innen & außen; Deutsche Manufakturqualität
  - Farbtöne: DUNKLE EICHE / HELLE EICHE / FARBLOS (200 ml)

Review insight used:
  praised  = leicht aufzutragen / zieht schnell ein / "Alleskönner"
  objection= "riecht danach noch ein paar Tage" → defuse: natürlicher Bienenwachs-Duft,
             verfliegt; gut lüften.

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
PLAN_NO = "03"


# ===== CUSTOMER-FACING DE COPY (title + bullets) =====

# Title is HTML-escaped, so literal "&" counts as 1 char. Keep ≤200 real chars.
TITLE = (
    "Jotti Möbelwachs 200 ml — Holzpflege mit Bienenwachs & Jojobaöl · 3-in-1 Reinigung "
    "Pflege Schutz · farbauffrischend, antistatisch · Dunkle Eiche, Helle Eiche & Farblos · "
    "innen & außen · Manufaktur"
)

BULLETS = [
    "<b>AUFFRISCHEN OHNE ABSCHLEIFEN</b> — Mattes, vergrautes Holz bekommt mit einem Tuch seine "
    "satte Farbe, Tiefe und einen seidenmatten Glanz zurück – kein Schleifen, kein Lackieren.",

    "<b>NATUR PUR: BIENENWACHS &amp; JOJOBAÖL</b> — Diese natürliche Holzpflege nährt durstiges, "
    "ausgetrocknetes Holz tief und schützt es spürbar vor Rissen, Austrocknung &amp; Verblassen.",

    "<b>EIN ALLESKÖNNER FÜRS HOLZ</b> — Reinigt, pflegt und schützt in einem Arbeitsgang. "
    "Antistatisch, daher zieht die Oberfläche weniger Staub an und bleibt länger sauber.",

    "<b>KINDERLEICHT MIT DEM TUCH</b> — Dünn auftragen, einarbeiten, nachpolieren: zieht schnell "
    "ein, ist ergiebig und leicht zu verarbeiten. Danach wasser- &amp; schmutzabweisend.",

    "<b>EHRLICHE MANUFAKTURQUALITÄT</b> — Festes Möbelwachs in Dunkle Eiche, Helle Eiche &amp; "
    "Farblos für viele Holzarten, innen &amp; außen. Natürlicher Duft, der bald verfliegt.",
]


# ===== IMAGE PLAN =====
# Art-direction fields (purpose/background/visual/props/lighting/why_it_works/ctr/cvr) = ENGLISH.
# overlay + overlay_sub = GERMAN, outcome-led.

IMAGES = [
    AIImagePlanItem(
        name="Bild 1 — Main Hero (3 A/B options)",
        role="hero",
        background=(
            "Warm cream seamless (#EFE6D9) with soft side-light; a 15% band of aged timber "
            "across the bottom for an artisan-manufaktur cue. Hold the EXACT same background and "
            "key across all 3 options so the only variable is the message — clean split-test."
        ),
        purpose=(
            "Win the click in the amazon.de wood-care grid: out-cut the generic wood oils and "
            "polish tins it sits beside on a mobile thumbnail."
        ),
        visual=(
            "Mock ALL 3 options; brand picks the winner via Amazon Manage Your Experiments. "
            "Each option: ONE callout, ONE action cue, ONE prop — clean, never stacked.\n\n"
            "▸ OPTION A — BEFORE/AFTER WOOD REVIVAL (wins on proof)\n"
            "Tin centred ('Dunkle Eiche' label legible, slight 3/4 turn, ~55% of frame). Behind it a "
            "solid-wood dining table split on the diagonal: left matte/grey/dry, right rich/revived/"
            "satin. A cloth cue sits on the dividing line.\n"
            "CALLOUT top-right: badge 'FARBE KEHRT ZURÜCK.' (brown #8B5A2B, white type).\n\n"
            "▸ OPTION B — CLOTH ACTION (wins on simplicity)\n"
            "Tin left; a hand (hand only, no face) rubs wax into a cabinet front with a cloth, a "
            "visible satin sheen streak trailing behind. Second tin as a prop.\n"
            "CALLOUT top-left: 'REINIGT. PFLEGT. SCHÜTZT.' (dark #2F2A26, white type).\n\n"
            "▸ OPTION C — 3-SHADE STACK (wins on choice)\n"
            "Three tins side by side (Dunkle Eiche · Helle Eiche · Farblos), each above a matching "
            "wood swatch in its shade.\n"
            "CALLOUT bottom-right: '3 FARBTÖNE' (brown #8B5A2B).\n\n"
            "All 3: tin(s) dominant, callout ~6% of frame, identical light + background."
        ),
        overlay="HOLZ AUFFRISCHEN.",
        overlay_sub="Satte Farbe & seidenmatter Glanz – ganz ohne Schleifen.",
        props=[
            "OPTION A: 'Dunkle Eiche' tin + split solid-wood dining table (grey vs revived) + cloth cue + badge",
            "OPTION B: tin + hand + cloth + satin-sheen streak on a cabinet front",
            "OPTION C: 3 tins (Dunkle Eiche/Helle Eiche/Farblos) + 3 wood swatches + badge",
        ],
        lighting=(
            "Warm side-light from camera-right (3000–3500K) with a rim on the tin so the label pops. "
            "Identical lighting across all 3 options."
        ),
        why_it_works=(
            "Three triggers against three buyer motives: A delivers the before/after revival proof "
            "(the strongest signal in the wood-care grid), B proves the effortless cloth application, "
            "C surfaces the 3 shades for the variant searcher. One callout, one action cue, one prop — "
            "legible on a mobile thumbnail."
        ),
        ctr=(
            "The greyed-to-revived solid-wood table reading 'FARBE KEHRT ZURÜCK.' beats the static "
            "polish tins in the DE grid; the visible revival contrast is the strongest click promise "
            "for dining tables, cabinets and antique furniture."
        ),
        cvr=(
            "Instant clarity on format (solid wax), benefit (3-in-1) and result (revived, satin wood) "
            "cuts bounce; the manufaktur set and the 3 shades build purchase confidence."
        ),
    ),
    AIImagePlanItem(
        name="Bild 2 — Hook: grey wood goes rich again",
        role="hook",
        background="Cream #EFE6D9, aged timber, warm side-light.",
        purpose="Land the core promise instantly — dull, greyed wood gets its colour and sheen back.",
        visual=(
            "Split frame of a solid-wood dining table. LEFT: matte, greyed, dry, small text cue "
            "'vorher'. RIGHT: rich colour, satin sheen, text cue 'nachher'. Bold divider in brown "
            "#8B5A2B; 'Dunkle Eiche' tin + cloth in the foreground corner. Small caption strip below: "
            "'farbauffrischend · seidenmatter Glanz'."
        ),
        overlay="FARBE KEHRT ZURÜCK.",
        overlay_sub="Aus grauem Holz wird wieder warmes, lebendiges Holz.",
        props=["Solid-wood dining table (split: greyed vs revived)", "'Dunkle Eiche' tin", "Cloth", "Divider"],
        lighting="Even warm front-side light, rim on the revived side so the sheen pops.",
        why_it_works=(
            "Hits the category's strongest buyer motive head-on: make tired, dry wood beautiful again. "
            "The before/after proof answers 'what's in it for me?' in a single frame."
        ),
        ctr=(
            "The grey→rich contrast speaks to anyone with an ageing dining table, cabinet or antique "
            "and promises a visible result."
        ),
        cvr="Visual result-proof instead of a claim sets realistic expectations and lowers bounce.",
    ),
    AIImagePlanItem(
        name="Bild 3 — Educate: natural formula & 3-in-1",
        role="educate",
        background="White with a brown accent band (#8B5A2B) in the footer.",
        purpose="Explain the formula and the 3-in-1 action; defend the premium positioning.",
        visual=(
            "Headline top: 'REINIGT. PFLEGT. SCHÜTZT.'. Left, 2 ingredient tiles with line icons:\n"
            "  • BIENENWACHS — nourishes & seals\n"
            "  • JOJOBAÖL — keeps wood supple\n"
            "Right, 3 action tiles: REINIGT (cloth) · PFLEGT (drop) · SCHÜTZT (shield). "
            "Tin centred. Footer band (brown): 'Universell für viele Holzarten.'"
        ),
        overlay="TIEF GENÄHRT.",
        overlay_sub="Bienenwachs & Jojobaöl nähren das Holz von innen.",
        props=["2 ingredient tiles", "3 action tiles", "Jotti tin", "Footer band"],
        lighting="Flat, clean studio light — legibility over atmosphere.",
        why_it_works=(
            "Makes the natural formula and the 3-in-1 action concrete. Ingredient-conscious buyers see "
            "real actives (beeswax, jojoba) instead of marketing words — which earns the manufaktur claim."
        ),
        ctr=(
            "Beeswax & jojoba are strong DE wood-care search signals; the active-ingredient tiles "
            "telegraph quality at a glance."
        ),
        cvr="A transparent formula builds trust and separates it from cheap chemical polish sprays.",
    ),
    AIImagePlanItem(
        name="Bild 4 — Desire: antistatic = less dust",
        role="desire",
        background="Aged timber, warm afternoon light.",
        purpose="Sell the everyday win — an antistatic surface attracts less dust.",
        visual=(
            "Split of a cared-for cabinet front. LEFT: untreated, visible dust film, text cue "
            "'zieht Staub an'. RIGHT: waxed, clean and glossy, text cue 'bleibt länger sauber'. "
            "Small tin in the foreground, cloth cue. Badge 'ANTISTATISCH'."
        ),
        overlay="LÄNGER SAUBER.",
        overlay_sub="Antistatisch – die Oberfläche zieht spürbar weniger Staub an.",
        props=["Cabinet front (split: dusty vs clean)", "Tin", "Cloth", "Badge 'ANTISTATISCH'"],
        lighting="Warm afternoon side-light, rim on the waxed side so the sheen pops.",
        why_it_works=(
            "Surfaces a concrete everyday benefit competitors rarely show: less dusting. Antistatic is a "
            "tangible, desirable win for cabinets and shelves."
        ),
        ctr="'Less dust' is a universal everyday promise that earns relevance beyond pure wood care.",
        cvr="An extra concrete benefit raises perceived value and makes the purchase easier to justify.",
    ),
    AIImagePlanItem(
        name="Bild 5 — Trust: defuse the scent objection",
        role="trust",
        background="White with cream panels.",
        purpose="Defuse the main objection on-image — 'still smells for a few days'.",
        visual=(
            "3-step application guide as an icon row:\n"
            "  1. DÜNN AUFTRAGEN (cloth icon)\n"
            "  2. EINARBEITEN & NACHPOLIEREN (circular-motion icon)\n"
            "  3. GUT LÜFTEN (window/air icon)\n"
            "Alongside, badge 'NATÜRLICHER BIENENWACHS-DUFT'. Small caption: 'Der natürliche Duft "
            "verfliegt – einfach gut lüften.' Tin as an anchor on the right."
        ),
        overlay="DER DUFT VERFLIEGT.",
        overlay_sub="Natürlicher Bienenwachs-Duft – einfach gut lüften, dann ist er weg.",
        props=["3 application icons", "Badge 'NATÜRLICHER BIENENWACHS-DUFT'", "Jotti tin"],
        lighting="Clean even studio light — icons legible on a thumbnail.",
        why_it_works=(
            "Pre-empts the only recurring negative review ('still smells for a few days') with an honest "
            "explanation (natural beeswax scent) and a simple fix (ventilate). Pre-defused objections cut "
            "returns and 1-star reviews."
        ),
        ctr="The honest framing of the natural scent attracts careful DE buyers who value natural products.",
        cvr=(
            "Defuses the top purchase objection right in the image; buyers scanning reviews see the "
            "explanation instead of just the problem."
        ),
    ),
    AIImagePlanItem(
        name="Bild 6 — Desire: use-case grid (many woods)",
        role="desire",
        background="Cream #EFE6D9, aged timber.",
        purpose="Show the versatility — one wax for many pieces, indoors and out.",
        visual=(
            "Clean 4-up grid of real wood scenes: solid-wood dining table · cabinet/dresser · antique "
            "furniture · garden furniture (teak/wood bench outdoors). Each tile carries a cloth cue. "
            "Tin centred or bottom as the anchor. Small label per tile (Tisch · Schrank · Antik · "
            "Garten). Small: 'innen & außen'."
        ),
        overlay="EIN ALLESKÖNNER.",
        overlay_sub="Ein Wachs für Esstisch, Schrank, Antik- & Gartenmöbel.",
        props=["4 use-case scenes (table/cabinet/antique/garden)", "Jotti tin", "Cloth cues"],
        lighting="Warm side-light, consistent across all 4 tiles.",
        why_it_works=(
            "Expands perceived value: one tin cares for many woods, indoors and out. Hits the cost-per-use "
            "maths and matches the broad DE search terms (dining table, cabinet, antique, garden furniture)."
        ),
        ctr=(
            "Addresses several search intents at once (wood care dining table, antique wax, garden "
            "furniture) and maximises grid relevance."
        ),
        cvr=(
            "More use-cases indoors and out = higher perceived value per tin, which makes the purchase "
            "easier to justify."
        ),
    ),
    AIImagePlanItem(
        name="Bild 7 — Close: German manufaktur",
        role="close",
        background="Workshop scene: aged wood, brass, linen, warm side-light.",
        purpose="Close on brand identity — artisan manufaktur quality.",
        visual=(
            "Mid-range workshop scene: hands (no face) rub wax into a beautiful wood surface with a "
            "cloth. On the bench: 3 Jotti tins (Dunkle Eiche · Helle Eiche · Farblos, labels legible), "
            "a cloth, wood swatches. Soft-focus workshop set (brass, linen). Small handwritten note "
            "card: 'Traditionelle Holzpflege. — Aus deutscher Manufaktur.'"
        ),
        overlay="DEUTSCHE MANUFAKTUR.",
        overlay_sub="Traditionelle Holzpflege, ehrlich von Hand gemacht.",
        props=["Hands at the wood (no face)", "3 Jotti tins (Dunkle Eiche/Helle Eiche/Farblos)", "Cloth", "Wood swatches", "Bench/brass/linen", "Handwritten note card"],
        lighting="Warm workshop side-light from camera-right, golden tone, lived-in — not staged.",
        why_it_works=(
            "Closes on the brand promise that matters right before checkout: honest, artisan manufaktur "
            "quality. The 3 tins anchor the shade choice; the hands-at-the-wood gesture is the visual "
            "metaphor for care and trust."
        ),
        ctr="The 'German manufaktur' signal differentiates from anonymous import polish sprays and draws quality-minded DE buyers.",
        cvr="Provenance, craft and the visible 3 shades create the final confidence that seals the purchase.",
    ),
]


# ===== A+ MODULES =====
# module `visual` = ENGLISH (designer brief). headline + body = GERMAN (customer-facing).

MODULES = [
    AIModule(
        name="Modul 1 — Brand-Banner",
        role="a+_banner",
        headline="HOLZ AUFFRISCHEN, NICHT SCHLEIFEN.",
        body=(
            "Müdes, vergrautes Holz wieder satt und lebendig – ohne abzuschleifen. Jotti Möbelwachs "
            "reinigt, pflegt und schützt in einem Arbeitsgang. Natürliche Rezeptur mit Bienenwachs "
            "&amp; Jojobaöl, farbauffrischend, aus deutscher Manufaktur."
        ),
        visual=(
            "Wide cinematic workshop scene: aged wood, warm side-light, 3 Jotti tins "
            "(Dunkle Eiche/Helle Eiche/Farblos) front-and-centre, wood swatches and brass soft-focus. "
            "Logo top-left in brown #8B5A2B."
        ),
        alt="Jotti Möbelwachs Dosen auf einer Holzbank in warmem Werkstattlicht, mit gepflegtem Holz im Hintergrund.",
    ),
    AIModule(
        name="Modul 2 — Carousel (4 Kacheln): Der Jotti-Vorteil",
        role="a+_carousel",
        headline="DER JOTTI-VORTEIL",
        body=(
            "Kachel 1: <b>OHNE SCHLEIFEN</b> — frischt Holz direkt auf, kein Abschleifen.<br/>"
            "Kachel 2: <b>FARBE &amp; GLANZ ZURÜCK</b> — satte Farbe, seidenmatter Glanz.<br/>"
            "Kachel 3: <b>NATÜRLICHE REZEPTUR</b> — Bienenwachs &amp; Jojobaöl, nährt tief.<br/>"
            "Kachel 4: <b>ANTISTATISCH</b> — zieht weniger Staub an, wasser- &amp; schmutzabweisend."
        ),
        visual=(
            "4 square tiles, brown accent corner per tile, small line icons "
            "(3-in-1 · brush/colour · honeycomb · dust-free)."
        ),
        alt="Vier-Kachel A+ Carousel mit den Jotti-Vorteilen: 3-in-1, farbauffrischend, natürliche Rezeptur, antistatisch.",
    ),
    AIModule(
        name="Modul 3 — Banner: Farbe kehrt zurück",
        role="a+_banner",
        headline="FARBE ZURÜCK. GLANZ ZURÜCK.",
        body=(
            "Dieses feste Holzwachs holt die natürliche Farbe ins Holz zurück und legt einen warmen, "
            "seidenmatten Glanz darüber. Einfach dünn mit dem Tuch auftragen, einarbeiten, "
            "nachpolieren – es zieht schnell ein und ist erstaunlich ergiebig. Für viele Holzarten, "
            "innen und außen."
        ),
        visual=(
            "Wide banner: a hand rubs wax into a solid-wood dining table with a cloth — greyed half "
            "left, rich revived half right. Warm side-light. Brown/dark palette."
        ),
        alt="A+ Banner: Jotti Möbelwachs wird mit Tuch in einen Massivholz-Esstisch eingearbeitet, Farbe kehrt zurück.",
    ),
    AIModule(
        name="Modul 4 — Banner: Schutz & Wirkung",
        role="a+_banner",
        headline="TIEF GENÄHRT. GUT GESCHÜTZT.",
        body=(
            "Die natürliche Rezeptur nährt das Holz tief und macht es wieder lebendig – und schützt "
            "es zugleich vor Austrocknung, Rissen und Verblassen. Danach ist die Oberfläche wasser- "
            "und schmutzabweisend und antistatisch, zieht also weniger Staub an."
        ),
        visual=(
            "Triptych: LEFT dry/grey wood (before), CENTRE the cloth-in moment, RIGHT rich wood with "
            "water beading off (after). Warm light throughout."
        ),
        alt="A+ Triptychon-Banner: Holz vorher grau, Anwendung mit Tuch, nachher satt und wasserabweisend.",
    ),
    AIModule(
        name="Modul 5 — Carousel (4 Kacheln): Für viele Hölzer",
        role="a+_carousel",
        headline="FÜR VIELE HÖLZER",
        body=(
            "Kachel 1: <b>MASSIVHOLZ-ESSTISCH</b> — frischt vergraute Tischplatten sichtbar auf.<br/>"
            "Kachel 2: <b>SCHRÄNKE &amp; KOMMODEN</b> — hält Möbel geschmeidig und sauber.<br/>"
            "Kachel 3: <b>ANTIKMÖBEL</b> — pflegt wertvolle Stücke schonend.<br/>"
            "Kachel 4: <b>GARTENMÖBEL</b> — schützt Holz auch außen vor Witterung."
        ),
        visual=(
            "4 identically composed use-case tiles, real wood scenes, brown accent corner per tile, "
            "consistent warm light."
        ),
        alt="Vier-Kachel A+ Carousel der Anwendungsfälle: Esstisch, Schränke, Antikmöbel, Gartenmöbel.",
    ),
    AIModule(
        name="Modul 6 — Premium Q&A",
        role="a+_qa",
        headline="HÄUFIGE FRAGEN",
        body=(
            "<b>F.</b> Riecht das Wachs nach dem Auftragen?<br/>"
            "<b>A.</b> Es hat einen natürlichen Bienenwachs-Duft, der nach kurzer Zeit verfliegt. "
            "Einfach nach dem Auftragen gut lüften.<br/><br/>"
            "<b>F.</b> Für welche Hölzer ist es geeignet?<br/>"
            "<b>A.</b> Universell für viele Holzarten: Massivholz-Esstische, Schränke, Antikmöbel und "
            "Gartenmöbel – innen und außen.<br/><br/>"
            "<b>F.</b> Frischt es die Holzfarbe wirklich auf?<br/>"
            "<b>A.</b> Ja, das Wachs hat einen farbauffrischenden Effekt und bringt einen seidenmatten "
            "Glanz zurück. In Dunkle Eiche, Helle Eiche und Farblos erhältlich.<br/><br/>"
            "<b>F.</b> Wie wird es aufgetragen?<br/>"
            "<b>A.</b> Dünn mit einem weichen Tuch auftragen, einarbeiten und nachpolieren. Zieht "
            "schnell ein und ist leicht zu verarbeiten.<br/><br/>"
            "<b>F.</b> Wo wird Jotti hergestellt?<br/>"
            "<b>A.</b> In deutscher Manufakturqualität – traditionelle Holzpflege, handwerklich gemacht."
        ),
        visual=(
            "Vertical Q/A table, brown dividers between questions, small F./A. labels in dark #2F2A26."
        ),
        alt="Premium Q&A Modul mit den häufigsten Fragen zu Jotti Möbelwachs.",
    ),
    AIModule(
        name="Modul 7 — Premium Comparison Chart",
        role="a+_comparison",
        headline="WARUM JOTTI",
        body=(
            "Vergleich über 4 Spalten: <b>Jotti Möbelwachs</b> · Standard-Möbelpolitur · "
            "Holzöl · Hartwachsöl.<br/><br/>"
            "Zeilen: 3-in-1 Reinigung+Pflege+Schutz · Farbauffrischend · Natürliche Rezeptur "
            "(Bienenwachs/Jojobaöl) · Antistatisch · Wasser- &amp; schmutzabweisend · Für viele "
            "Holzarten innen &amp; außen · Deutsche Manufaktur.<br/><br/>"
            "Jotti-Spalte mit dezentem Braun-Ton hervorheben."
        ),
        visual=(
            "Standard Amazon Premium Comparison Chart, 4 product columns. Competitors named only as "
            "category descriptors, no brand names. Brown header row."
        ),
        alt="Premium Vergleichstabelle: Jotti Möbelwachs vs. Standard-Politur, Holzöl und Hartwachsöl.",
    ),
]


# ===== Q&A (customer-facing, DE) =====

QA = [
    AIQA(q="Muss ich das Holz vorher abschleifen?",
         a="Nein. Das ist der Vorteil: Das Wachs frischt mattes, vergrautes Holz direkt auf – ohne Abschleifen und ohne Lackieren. Einfach reinigen und mit dem Tuch auftragen."),
    AIQA(q="Riecht das Möbelwachs nach dem Auftragen?",
         a="Es hat einen natürlichen Bienenwachs-Duft, der die ersten Tage leicht wahrnehmbar ist und dann verfliegt. Einfach gut lüften – danach riecht der Raum wieder frisch."),
    AIQA(q="Für welche Holzarten ist das Wachs geeignet?",
         a="Ein echter Alleskönner für viele Holzarten: Massivholz-Esstische, Schränke und Kommoden, Antikmöbel sowie Gartenmöbel. Geeignet für innen und außen."),
    AIQA(q="Frischt das Wachs die Holzfarbe wirklich auf?",
         a="Ja. Jotti Möbelwachs holt die Farbe ins Holz zurück und gibt vergrautem, mattem Holz wieder eine satte, warme Tiefe mit seidenmattem Glanz."),
    AIQA(q="Welche Farbtöne gibt es?",
         a="Das Möbelwachs gibt es in drei Tönen: Dunkle Eiche, Helle Eiche und Farblos. So finden Sie den passenden Ton für Ihre jeweilige Holzart."),
    AIQA(q="Was bedeutet antistatisch?",
         a="Die behandelte Oberfläche lädt sich weniger elektrostatisch auf und zieht dadurch weniger Staub an – Schränke und Regale bleiben spürbar länger sauber."),
    AIQA(q="Ist das Holz danach wasserabweisend?",
         a="Ja. Nach dem Wachsen perlt Wasser besser ab, und die Oberfläche ist wasser- und schmutzabweisend – also besser vor Feuchtigkeit und Flecken geschützt."),
    AIQA(q="Wie wird das Möbelwachs angewendet?",
         a="Holz reinigen, das Wachs dünn mit einem weichen Tuch auftragen, einarbeiten und nachpolieren. Es zieht schnell ein, ist ergiebig und leicht zu verarbeiten. Bei Bedarf wiederholen."),
]


# Backend KWs — stem-deduped, DE, byte-packed. Avoid brand/title duplicates & superlatives.
BACKEND = (
    "holzpflege holzwachs holzpolitur möbelpolitur antikwachs möbelöl holzöl innen außen "
    "holzpflegeöl esstisch massivholz schrank kommode antikmöbel gartenmöbel teak "
    "bienenwachs jojobaöl natürlich farbauffrischend seidenmatt antistatisch staub "
    "wasserabweisend schmutzabweisend reinigung pflege schutz tuch politur holzbutter "
    "hartwachsöl möbelpflege wachsen dunkle helle eiche farblos manufaktur deutsche"
)


def main() -> None:
    print("Loading Jotti customer + parsing Möbelwachs Excel…")
    cust = load_customer("jotti")
    brief = parse_excel(EXCEL)
    OUT = HERE / f"{PLAN_NO}_Jotti_Moebelwachs_Image Plan.pdf"
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
    builder.copy_source_label = "Hand-written senior copy (EN art-direction / DE marketplace)"

    print("Building branded PDF…")
    pdf_path = builder.build()
    size_kb = pdf_path.stat().st_size // 1024
    import re
    pages = len(re.findall(rb'/Type\s*/Page[^s]', pdf_path.read_bytes()))
    print(f"Built: {pdf_path}")
    print(f"  Pages: {pages}  Size: {size_kb} KB")


if __name__ == "__main__":
    main()
