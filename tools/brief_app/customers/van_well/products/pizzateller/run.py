"""Van Well Pizzateller 6-teilig, XL Porzellan Ø 30,5 cm — Image Plan 04
Hand-written senior copy injected into the branded ReportLab pipeline.

Marketplace: amazon.de.

LANGUAGE SPLIT (the standard):
  • ENGLISH — art-direction / strategy fields the designer reads:
    image purpose, background, visual, props, lighting, why_it_works, ctr, cvr,
    and module visual.
  • GERMAN — marketplace, customer-facing text the shopper reads:
    TITLE, BULLETS, image overlay, overlay_sub, module headline, module body,
    QA, and BACKEND keywords.

VAN WELL STYLE MANDATE (art-direction, EN — must appear across the plan):
  navy-blue #1C2E4A overlay BARS with WHITE bold sans headlines; the VAN WELL
  crown wordmark top-right on lifestyle images; feature ICON BADGES in a navy bar
  (Spülmaschinengeeignet · Mikrowellenfest · Robustes Porzellan · Stapelbar);
  warm real GASTRO + FAMILY lifestyle (people enjoying pizza/pasta at a wood
  table, tiled kitchen) alongside clean white studio shots; a '60+ JAHRE
  QUALITÄT' trust badge. IMAGE 7 (role=close) = THE BRAND IMAGE: restaurant/chef
  scene, '10.000 Restaurants vertrauen auf VAN WELL' + '60+ Jahre' + crown.

OVERLAY RULE: sell the OUTCOME (Restaurant-/Italiener-Feeling zuhause), not the
action. Hard limits (auto-linted on build):
  overlay ≤ 30 chars AND ≤ 5 words · overlay_sub ≤ 90 chars
  module headline ≤ 38 chars · bullet head <b>…</b> ≤ 45 chars · TITLE ≤ 200 chars

Verified facts:
  - 6-teilig, XL Porzellan, Ø 30,5 cm (ideal für Pizzen bis 28 cm)
  - flacher breiter Rand 1,3 cm (hält Belag & Krümel sicher)
  - robust, STAPELBAR, SPÜLMASCHINENGEEIGNET, MIKROWELLENFEST, lebensmittelecht
  - für Pizza, Pasta & Antipasti; italienisches Charme-Design (Pizzabäcker),
    mehrere Design-Varianten
  - Van Well = Traditionsmarke seit über 60 Jahren

Review insight used:
  praised   = hochwertiges/edles Porzellan · schöne schlichte Optik · gute Größe · top Preis-Leistung
  objection = teils zerbrochen/zerkratzt angekommen → defuse: lead auf Qualität/
              robustes Porzellan UND bruchsichere Verpackung (kein Über-Versprechen).

Compliance: no $/€ prices, no URL/.com, no #1/beste/garantiert superlatives, no over-durability claim.
"""
from __future__ import annotations
import sys
from pathlib import Path

# This script lives at customers/<brand>/products/<product>/run.py — self-contained.
HERE = Path(__file__).resolve().parent          # the product folder
ROOT = HERE.parents[5]                           # project root
sys.path.insert(0, str(ROOT))

from tools.brief_app.core.customers import load_customer
from tools.brief_app.core.excel_parser import parse_excel
from tools.brief_app.core.pdf_builder import BriefBuilder
from tools.brief_app.core.ai import AIImagePlanItem, AIModule, AIQA


EXCEL = HERE / "listing.xlsx"
PLAN_NO = "04"


# ===== KW-led, marketing-optimized DE copy (customer-facing) =====

# Title is HTML-escaped, so literal "&" counts as 1 char. Keep ≤200 real chars. German.
TITLE = (
    "Van Well Pizzateller groß 6er Set — XL Porzellan Ø 30,5 cm für Pizza, Pasta & Antipasti "
    "· breiter Rand · stapelbar, spülmaschinengeeignet & mikrowellenfest · "
    "italienisches Design · Gastro & Zuhause"
)

BULLETS = [
    "<b>ITALIENER-FEELING ZUHAUSE</b> — Servieren wie beim Lieblings-Italiener: XL Pizzateller "
    "groß aus edlem Porzellan bringen Pizza, Pasta &amp; Antipasti stilvoll auf den Tisch.",

    "<b>XL Ø 30,5 CM — ENDLICH PLATZ</b> — Der große Pizzateller 30 cm fasst Pizzen bis 28 cm. "
    "Der flache, breite Rand von 1,3 cm hält Belag und Krümel sicher auf dem Teller.",

    "<b>ROBUSTES, EDLES PORZELLAN</b> — Schweres, hochwertiges Teller Porzellan mit schöner, "
    "schlichter Optik. Bruchsicher verpackt, damit Ihr 6er Set heil und komplett ankommt.",

    "<b>STAPELBAR &amp; PFLEGELEICHT</b> — Spülmaschinengeeignet und mikrowellenfest für den "
    "Alltag. Platzsparend stapelbar – 6 große Teller, aufgeräumt verstaut im Schrank.",

    "<b>VIELSEITIG: PIZZA, PASTA, MEHR</b> — Als Pizzateller, tiefer Pastateller, Servierteller "
    "groß oder Platzteller. Charmantes italienisches Design – Traditionsmarke seit über 60 Jahren.",
]


IMAGES = [
    AIImagePlanItem(
        name="Bild 1 — Main Hero (3 Optionen für A/B-Test)",
        role="hero",
        background="Clean white studio (#FFFFFF) with a soft warm gradient in the bottom 15% for grounding. Identical backdrop across all 3 options for a clean split-test.",
        purpose="Win the click in the amazon.de plate grid — stand out next to generic white plates with the italian-charme design + XL size.",
        visual=(
            "Designer mocks up ALL 3 options. Brand picks the winner via Amazon Manage Your Experiments. "
            "Each option: ONE navy callout bar, ONE hero cue, clean — never stacked. VAN WELL crown "
            "wordmark top-right on every option.\n\n"
            "▸ OPTION A — XL SIZE PROOF (wins on the 'endlich groß genug' promise)\n"
            "One Pizzateller centered, front 3/4, the pizzabäcker illustration legible (~60% of frame). "
            "A whole pizza (to ~28 cm) sits on it, showing the flat wide rim still framing the crust. "
            "NAVY CALLOUT BAR bottom-left (#1C2E4A, white bold sans): 'XL Ø 30,5 CM'.\n\n"
            "▸ OPTION B — SET + STACK VALUE (wins on the 6er value + storage)\n"
            "The 6-piece set as a clean stack of plates, top plate fanned forward so the design shows. "
            "Small navy ICON BADGE ROW under the stack: Spülmaschinengeeignet · Mikrowellenfest · "
            "Robustes Porzellan · Stapelbar (icons only in a single navy bar). NAVY CALLOUT top-left: "
            "'6er SET XL PORZELLAN'.\n\n"
            "▸ OPTION C — ITALIAN LIFESTYLE (wins on desire / Italiener-Feeling)\n"
            "Warm wood table, a served pizza + a glass of red on the plate, italian-tiled kitchen soft "
            "behind. NAVY CALLOUT bottom-right: 'WIE BEIM ITALIENER'. Crown wordmark top-right.\n\n"
            "All 3: plate/set dominant ~60%, navy callout ~7%, crown top-right, same light / same backdrop."
        ),
        overlay="WIE BEIM ITALIENER.",
        overlay_sub="XL Porzellanteller Ø 30,5 cm – Pizza, Pasta &amp; Antipasti stilvoll serviert.",
        props=[
            "OPTION A: single plate + whole pizza (~28 cm) + navy 'XL Ø 30,5 CM' bar + crown",
            "OPTION B: 6-piece stack + navy icon-badge row + navy '6er SET' bar + crown",
            "OPTION C: served pizza + red wine + warm wood table + tiled kitchen + navy bar + crown",
        ],
        lighting="Soft warm top key (~4000K) with gentle fill from camera-right, subtle rim on the plate rim so the porcelain and glaze read premium. Same light across all 3 options.",
        why_it_works=(
            "Three triggers against three motives: A proves the XL size (the top search intent 'pizzateller "
            "groß'), B proves the 6er value + stackable storage, C sells the Italiener-Feeling desire. The "
            "navy bar + crown identity keeps it instantly recognizable as VAN WELL in the grid."
        ),
        ctr="The XL pizza-on-plate proof plus the navy 'XL Ø 30,5 CM' bar beats generic white-plate thumbnails and matches the 'pizzateller groß / 30 cm' search intent.",
        cvr="Instant clarity on size, set count and italian design cuts bounce; the crown + navy identity signals an established brand, not a no-name plate.",
    ),
    AIImagePlanItem(
        name="Bild 2 — Hook: XL Ø 30,5 cm mit breitem Rand",
        role="hook",
        background="White studio with a light navy dimension line for the size call-out.",
        purpose="Establish the XL size + wide rim advantage instantly — the reason to buy this over a standard 26 cm plate.",
        visual=(
            "Top-down macro of one plate with a clean navy dimension arrow across it labeled 'Ø 30,5 cm', "
            "and a second short arrow on the rim labeled '1,3 cm Rand'. A pizza outline (to 28 cm) ghosted "
            "onto the plate shows the fit. Side navy caption bar: 'Rand hält Belag & Krümel sicher'. "
            "Crown wordmark top-right."
        ),
        overlay="ENDLICH GROSS GENUG.",
        overlay_sub="Ø 30,5 cm fasst Pizzen bis 28 cm – der breite Rand hält den Belag.",
        props=["single plate (top-down)", "navy Ø 30,5 cm dimension arrow", "1,3 cm rim arrow", "ghosted 28 cm pizza outline", "navy caption bar", "crown wordmark"],
        lighting="Even soft front-light, slight 3D shadow under the plate. Clarity over mood — this is the educational hook.",
        why_it_works=(
            "A direct answer to the top search query 'pizzateller groß / 30 cm': the XL diameter plus the "
            "belag-holding rim is the most tangible differentiator versus a standard dinner plate."
        ),
        ctr="The Ø 30,5 cm dimension call-out hits the size nerve of the DE buyer explicitly searching for a large pizza plate.",
        cvr="Removes the 'is it actually big enough?' doubt with a measured, honest size proof — sets correct expectations.",
    ),
    AIImagePlanItem(
        name="Bild 3 — Educate: Robustes Porzellan + Pflege-Icons",
        role="educate",
        background="White with a navy (#1C2E4A) accent band in the footer.",
        purpose="Explain the material quality and everyday practicality — defend the price-quality positioning.",
        visual=(
            "Headline at top, then a navy ICON BADGE ROW of 4 tiles (icon over label):\n"
            "  • SPÜLMASCHINENGEEIGNET (dishwasher icon)\n"
            "  • MIKROWELLENFEST (microwave icon)\n"
            "  • ROBUSTES PORZELLAN (shield / plate icon)\n"
            "  • STAPELBAR (stacked-plates icon)\n"
            "One plate anchored right, edge-on to show the material thickness. Navy footer band carries the "
            "supporting line. Crown wordmark top-right."
        ),
        overlay="STARK IM ALLTAG.",
        overlay_sub="Robustes Porzellan – spülmaschinengeeignet, mikrowellenfest &amp; stapelbar.",
        props=["navy 4-icon badge row", "single plate edge-on (thickness)", "navy footer band", "crown wordmark"],
        lighting="Flat, clean studio light — legibility over atmosphere; slight edge highlight to read the porcelain thickness.",
        why_it_works=(
            "Makes 'robustes Porzellan' concrete with the exact everyday filters DE buyers scan for. The "
            "navy icon-badge row is the established VAN WELL catalog language, so it reads as brand-consistent."
        ),
        ctr="The dishwasher/microwave/stackable icon row answers the practical everyday questions at a glance.",
        cvr="Concrete material + care facts build trust and separate this from a fragile, purely decorative plate.",
    ),
    AIImagePlanItem(
        name="Bild 4 — Desire: Gedeckter Tisch (Pizza, Pasta & Antipasti)",
        role="desire",
        background="Warm wood table, italian-tiled kitchen soft-focus, warm afternoon light.",
        purpose="Sell the served result — a beautiful italian table the buyer wants to recreate at home.",
        visual=(
            "Overhead / 3/4 table scene: three of the plates in use — one with a whole pizza, one with pasta, "
            "one with antipasti (tomato-mozzarella, parma & melon). A glass of red wine, linen napkin, "
            "warm wood. The italian-charme design shows between the food. Crown wordmark top-right; small "
            "navy caption bar: 'Pizza · Pasta · Antipasti'."
        ),
        overlay="DER ITALIENER-TISCH.",
        overlay_sub="Pizza, Pasta &amp; Antipasti – so schön angerichtet wie im Restaurant.",
        props=["3 plates in use (pizza / pasta / antipasti)", "red wine glass", "linen napkin", "warm wood table", "tiled kitchen (soft focus)", "navy caption bar", "crown wordmark"],
        lighting="Warm afternoon side-light from camera-right, appetizing golden tone, soft shadows — lived-in, not sterile.",
        why_it_works=(
            "Leans on the strongest VoC verbatim (schöne Optik, gute Größe) and shows the plates doing their "
            "real job across all three use cases. The served italian table is the strongest desire signal in "
            "the category."
        ),
        ctr="A warm, appetizing italian table is universally desirable for anyone who loves pizza and pasta nights at home.",
        cvr="Shows the real served result across pizza, pasta and antipasti — buyers see the plates in their own dinner, not on a shelf.",
    ),
    AIImagePlanItem(
        name="Bild 5 — Trust: Bruchsicher & komplett angekommen",
        role="trust",
        background="White with soft navy panels for separation.",
        purpose="Defuse the main objection ('arrived broken/scratched') honestly — lead on quality + secure packaging.",
        visual=(
            "Left: one plate front-on with a navy '60+ JAHRE QUALITÄT' trust badge. Right: a clean cutaway of "
            "the packaging — 6 plates individually cushioned in a sturdy box with foam/cardboard dividers, a "
            "small navy badge 'BRUCHSICHER VERPACKT'. Between them a short navy caption bar: 'Robustes "
            "Porzellan, sicher verpackt – vollständig geliefert'. Crown wordmark top-right. Honest, no "
            "'unzerbrechlich' claim."
        ),
        overlay="SICHER VERPACKT.",
        overlay_sub="Robustes Porzellan, bruchsicher verpackt – Ihr 6er Set kommt komplett an.",
        props=["single plate + navy '60+ JAHRE QUALITÄT' badge", "packaging cutaway with dividers", "navy 'BRUCHSICHER VERPACKT' badge", "navy caption bar", "crown wordmark"],
        lighting="Clean even studio light — badges and packaging legible on the thumbnail.",
        why_it_works=(
            "Proactively addresses the one recurring negative ('arrived broken') without over-claiming "
            "indestructibility: it leads on quality porcelain and shows the secure packaging that gets the "
            "set delivered complete. Pre-defused objections lower returns and 1-star ratings."
        ),
        ctr="The '60+ Jahre' + secure-packaging cue reassures buyers who scanned reviews mentioning breakage.",
        cvr="Defuses the top purchase objection honestly on the image — buyers see the fix (secure packing) rather than only the risk.",
    ),
    AIImagePlanItem(
        name="Bild 6 — Desire: Design-Varianten (Wählen Sie Ihr Lieblingsdesign)",
        role="desire",
        background="White studio, warm neutral, consistent across tiles.",
        purpose="Show the design choice — the italian-charme variants let the buyer pick their favorite look.",
        visual=(
            "Clean grid of the available design variants, each plate front-on so the pizzabäcker / italian "
            "illustrations read clearly. Small label under each variant. A soft navy caption bar across the "
            "top: 'Mehrere Designs – ein Lieblingsstück'. Crown wordmark top-right. Keep it premium and "
            "uncluttered — real product photography, no cheap look."
        ),
        overlay="IHR LIEBLINGSDESIGN.",
        overlay_sub="Mehrere italienische Design-Varianten – wählen Sie Ihren Favoriten.",
        props=["grid of design variants (plates front-on)", "per-variant labels", "navy caption bar", "crown wordmark"],
        lighting="Even warm studio light, consistent across all tiles so the designs compare fairly.",
        why_it_works=(
            "Turns the multi-variant catalog into a desire lever: choice raises engagement and lets the buyer "
            "self-select the design that fits their kitchen, matching the established VAN WELL A+ selector."
        ),
        ctr="A visible choice of italian designs invites the buyer to find 'their' plate and keeps them on the listing.",
        cvr="Letting buyers pick a favorite design increases fit-to-taste and reduces post-purchase design regret.",
    ),
    AIImagePlanItem(
        name="Bild 7 — Close: DIE MARKENBILD — 10.000 Restaurants vertrauen VAN WELL",
        role="close",
        background="Warm restaurant / pizzeria scene: chef by the wood-fired oven, wood counter, soft ambient light.",
        purpose="Close on brand identity — the VAN WELL brand-trust image, consistent across the whole catalog.",
        visual=(
            "Mid-range restaurant scene: a chef / pizzaiolo (hands and torso, face soft or turned) plating a "
            "fresh pizza onto a VAN WELL Pizzateller by the wood-fired oven. On the wood counter: a small "
            "stack of the plates, legible. NAVY OVERLAY BAR (#1C2E4A, white bold sans) carries the trust "
            "line; a navy '60+ JAHRE QUALITÄT' badge sits alongside. VAN WELL crown wordmark top-right. "
            "Warm, appetizing, premium gastro atmosphere — the established brand-close image."
        ),
        overlay="RESTAURANTS VERTRAUEN UNS.",
        overlay_sub="Über 10.000 Restaurants vertrauen VAN WELL – Qualität seit über 60 Jahren.",
        props=["chef / pizzaiolo (hands + torso, no face-forward)", "wood-fired oven", "VAN WELL plates (stack + in use)", "navy overlay bar", "navy '60+ JAHRE QUALITÄT' badge", "crown wordmark", "wood counter"],
        lighting="Warm restaurant side-light, golden appetizing tone, lived-in gastro feel — not staged, not sterile.",
        why_it_works=(
            "Closes on the brand promise that matters before checkout: real restaurants and 60+ years of "
            "VAN WELL trust. Consistent with the catalog brand-image, it transfers pro-kitchen credibility "
            "to the home buyer — the gastro-to-home trust handoff."
        ),
        ctr="The '10.000 Restaurants' + crown signal differentiates from anonymous no-name plates and attracts quality-conscious DE buyers.",
        cvr="Gastro provenance and 60+ years of heritage create the final trust that seals the purchase.",
    ),
]


MODULES = [
    AIModule(
        name="Modul 1 — Lifestyle-Hero-Banner",
        role="a+_banner",
        headline="ITALIENER-FEELING ZUHAUSE.",
        body=(
            "Van Well XL Pizzateller aus edlem Porzellan bringen Pizza, Pasta &amp; Antipasti stilvoll "
            "auf den Tisch. Ø 30,5 cm, robust, stapelbar – Qualität seit über 60 Jahren."
        ),
        visual="Wide cinematic lifestyle banner: warm wood table with a served pizza on the plate, tiled italian kitchen soft-focused, warm side-light. VAN WELL crown wordmark top-right, small navy '60+ JAHRE QUALITÄT' badge in the lower band.",
        alt="Van Well Pizzateller mit servierter Pizza auf einem warmen Holztisch, italienische Küche im Hintergrund.",
    ),
    AIModule(
        name="Modul 2 — Size / Design Specs",
        role="a+_banner",
        headline="XL Ø 30,5 CM · 1,3 CM RAND.",
        body=(
            "Ø 30,5 cm XL Porzellan fasst Pizzen bis 28 cm; der flache, breite Rand von 1,3 cm hält Belag "
            "und Krümel sicher. Robustes Porzellan, platzsparend stapelbar. 6-teiliges Set."
        ),
        visual="Wide spec banner: one plate top-down with a navy dimension line 'Ø 30,5 cm' and a rim call-out '1,3 cm Rand', a plate edge-on beside it showing thickness and stackability. Navy accents, white studio. Crown wordmark top-right.",
        alt="A+ Banner mit den Maßen des Van Well Pizzatellers: Ø 30,5 cm und 1,3 cm breiter Rand, stapelbar.",
    ),
    AIModule(
        name="Modul 3 — Carousel (4 Kacheln): Perfekt für Pizza, Pasta & Antipasti",
        role="a+_carousel",
        headline="PIZZA, PASTA & ANTIPASTI",
        body=(
            "Kachel 1: <b>PIZZA</b> — XL Ø 30,5 cm, Platz für Pizzen bis 28 cm.<br/>"
            "Kachel 2: <b>PASTA</b> — als tiefer Pastateller für Spaghetti &amp; Nudelgerichte.<br/>"
            "Kachel 3: <b>ANTIPASTI</b> — Tomate-Mozzarella, Melone &amp; Parma stilvoll anrichten.<br/>"
            "Kachel 4: <b>SERVIEREN</b> — als Servierteller groß oder Platzteller vielseitig einsetzbar."
        ),
        visual="4 square lifestyle tiles (pizza · pasta · antipasti · serving), each with a navy icon-badge corner (Spülmaschinengeeignet · Mikrowellenfest · Robustes Porzellan · Stapelbar cycled across tiles). Warm consistent light. Crown wordmark top-right.",
        alt="Vier-Kachel A+ Carousel: Van Well Pizzateller für Pizza, Pasta, Antipasti und zum Servieren.",
    ),
    AIModule(
        name="Modul 4 — Design-Selector (Wählen Sie Ihr Lieblingsdesign)",
        role="a+_carousel",
        headline="IHR LIEBLINGSDESIGN",
        body=(
            "Kachel 1: <b>PIZZABÄCKER-DESIGN</b> — charmante italienische Illustration.<br/>"
            "Kachel 2: <b>ITALIA-MOTIV</b> — klassisch mediterraner Look für den Tisch.<br/>"
            "Kachel 3: <b>SCHLICHT &amp; ELEGANT</b> — dezentes Dekor, passt zu allem.<br/>"
            "Kachel 4: <b>WEITERE VARIANTEN</b> — wählen Sie das Design, das zu Ihnen passt."
        ),
        visual="4 identically composed design-variant tiles, each plate front-on so the illustration reads clearly, per-variant label beneath. Navy accent corner, warm neutral studio. Crown wordmark top-right. Premium, no cheap look.",
        alt="Vier-Kachel A+ Design-Selector der Van Well Pizzateller-Varianten zum Auswählen des Lieblingsdesigns.",
    ),
    AIModule(
        name="Modul 5 — Marken-Trust-Close",
        role="a+_banner",
        headline="10.000 RESTAURANTS VERTRAUEN.",
        body=(
            "Über 10.000 Restaurants vertrauen auf Van Well. Die Traditionsmarke steht seit über 60 Jahren "
            "für hochwertige, stilvolle Porzellan- und Glasprodukte mit ausgezeichnetem Preis-Leistungs-Verhältnis."
        ),
        visual="Wide brand-trust banner: warm restaurant / pizzeria scene, a chef plating a pizza onto a Van Well plate by the wood-fired oven, a stack of plates on the counter. Navy overlay bar carries the trust line, navy '60+ JAHRE QUALITÄT' badge, crown wordmark top-right.",
        alt="A+ Marken-Banner: Küchenchef richtet Pizza auf einem Van Well Teller an – über 10.000 Restaurants vertrauen Van Well.",
    ),
    AIModule(
        name="Modul 6 — Premium Q&A",
        role="a+_qa",
        headline="HÄUFIGE FRAGEN",
        body=(
            "<b>F.</b> Wie groß sind die Teller?<br/>"
            "<b>A.</b> Ø 30,5 cm XL Porzellan – ideal für Pizzen bis 28 cm. Der flache, breite Rand von "
            "1,3 cm hält Belag und Krümel sicher auf dem Teller.<br/><br/>"
            "<b>F.</b> Sind sie spülmaschinengeeignet und mikrowellenfest?<br/>"
            "<b>A.</b> Ja. Die Teller sind spülmaschinengeeignet und mikrowellenfest, lebensmittelecht und "
            "platzsparend stapelbar – praktisch für den Alltag.<br/><br/>"
            "<b>F.</b> Kommen die Teller heil an?<br/>"
            "<b>A.</b> Die Teller bestehen aus robustem Porzellan und werden bruchsicher verpackt, damit Ihr "
            "6er Set vollständig und unbeschädigt bei Ihnen ankommt.<br/><br/>"
            "<b>F.</b> Wofür kann ich die Teller nutzen?<br/>"
            "<b>A.</b> Für Pizza, Pasta &amp; Antipasti – ebenso als tiefer Pastateller, Servierteller groß "
            "oder Platzteller. Vielseitig für Gastronomie und Zuhause.<br/><br/>"
            "<b>F.</b> Gibt es verschiedene Designs?<br/>"
            "<b>A.</b> Ja. Die Serie gibt es in mehreren italienischen Design-Varianten – wählen Sie Ihr "
            "Lieblingsdesign."
        ),
        visual="Vertical Q/A table, navy dividers between questions, small navy F./A. labels. Crown wordmark top-right.",
        alt="Premium Q&A Modul mit den häufigsten Fragen zum Van Well Pizzateller.",
    ),
    AIModule(
        name="Modul 7 — Premium Comparison Chart",
        role="a+_comparison",
        headline="WARUM VAN WELL",
        body=(
            "Vergleich über 4 Spalten: <b>Van Well Pizzateller XL</b> · Standard-Speiseteller · "
            "Pizzateller ohne Rand · No-Name Porzellanteller.<br/><br/>"
            "Zeilen: XL Ø 30,5 cm · breiter Rand 1,3 cm (hält Belag) · robustes Porzellan · stapelbar · "
            "spülmaschinengeeignet &amp; mikrowellenfest · italienisches Design · Traditionsmarke 60+ Jahre.<br/><br/>"
            "Van-Well-Spalte mit dezentem Navy-Ton hervorheben."
        ),
        visual="Standard Amazon Premium Comparison Chart, 4 product columns. Competitors named by category only, no brand names. Navy header row, crown wordmark top-right.",
        alt="Premium Vergleichstabelle: Van Well Pizzateller XL vs. Standard-Speiseteller, Pizzateller ohne Rand und No-Name Porzellanteller.",
    ),
]


QA = [
    AIQA(q="Wie groß sind die Pizzateller?",
         a="Ø 30,5 cm XL Porzellan – ideal für Pizzen bis 28 cm. Der flache, breite Rand von 1,3 cm hält Belag und Krümel sicher auf dem Teller. Höhe ca. 2 cm."),
    AIQA(q="Sind die Teller spülmaschinengeeignet und mikrowellenfest?",
         a="Ja. Die Teller sind spülmaschinengeeignet und mikrowellenfest sowie lebensmittelecht. Das macht die tägliche Reinigung und Nutzung besonders einfach."),
    AIQA(q="Kommen die Teller unbeschädigt an?",
         a="Die Teller bestehen aus robustem, schwerem Porzellan und werden bruchsicher verpackt, damit Ihr 6-teiliges Set vollständig und unbeschädigt bei Ihnen ankommt. Sollte doch einmal etwas beschädigt sein, wenden Sie sich bitte an uns."),
    AIQA(q="Sind die Teller stapelbar?",
         a="Ja. Die Teller sind stapelbar und lassen sich dadurch platzsparend im Schrank verstauen – praktisch für ein 6er Set."),
    AIQA(q="Wofür eignen sich die Teller?",
         a="Für Pizza, Pasta und Antipasti – ebenso als tiefer Pastateller, Servierteller groß, Platzteller oder Speiseteller. Vielseitig einsetzbar für Gastronomie und Zuhause."),
    AIQA(q="Gibt es verschiedene Designs?",
         a="Ja. Die Pizzateller-Serie gibt es in mehreren charmanten italienischen Design-Varianten. So finden Sie das Design, das am besten zu Ihrer Küche und Ihrem Geschmack passt."),
    AIQA(q="Wer steckt hinter Van Well?",
         a="Van Well ist eine Traditionsmarke und steht seit über 60 Jahren für hochwertige, stilvolle Porzellan- und Glasprodukte mit einem sehr guten Preis-Leistungs-Verhältnis – für Gastronomen wie für qualitätsbewusste Privatkunden."),
]


# Backend KWs — German, stem-deduped, byte-packed. Avoid brand/title duplicates & superlatives.
BACKEND = (
    "pizzateller groß pizza teller gross 30 cm 33 cm xl porzellanteller pastateller tief "
    "spaghetti teller servierteller platzteller speiseteller große teller geschirr porzellan "
    "geschirrset kombiservice italienisch pizzabäcker design set 6er sechs stück stapelbar "
    "spülmaschinenfest mikrowellengeeignet robust gastro restaurant buffet antipasti nudeln pasta"
)


def main() -> None:
    print("Loading Van Well customer + parsing Pizzateller Excel…")
    cust = load_customer("van_well")
    brief = parse_excel(EXCEL)
    OUT = HERE / f"{PLAN_NO}_VanWell_Pizzateller_Image Plan.pdf"
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
    builder.copy_source_label = "Hand-written senior copy (DE, VAN WELL style)"

    print("Building branded PDF…")
    pdf_path = builder.build()
    size_kb = pdf_path.stat().st_size // 1024
    import re
    pages = len(re.findall(rb'/Type\s*/Page[^s]', pdf_path.read_bytes()))
    print(f"Built: {pdf_path}")
    print(f"  Pages: {pages}  Size: {size_kb} KB")


if __name__ == "__main__":
    main()
