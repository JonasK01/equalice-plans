"""Van Well Willibecher 0,5 L — 12er-SET — Image Plan 05
Hand-written senior copy injected into the branded ReportLab pipeline.

Marketplace: amazon.de.

LANGUAGE SPLIT (the standard):
  • ENGLISH — art-direction / strategy the designer reads:
    image purpose, background, visual, props, lighting, why_it_works, ctr, cvr,
    and module visual.
  • GERMAN — marketplace, customer-facing text the shopper reads:
    TITLE, BULLETS, image overlay, overlay_sub, module headline, module body,
    QA, and BACKEND keywords.

VAN WELL STYLE MANDATE (art-direction, English):
  navy-blue #1C2E4A overlay BARS with WHITE bold sans headlines; the VAN WELL
  crown wordmark top-right on lifestyle images; feature ICON BADGES in a navy bar
  (0,5 L mit Eichstrich · verstärkter Boden · dickwandig · spülmaschinengeeignet ·
  12er-Set); warm real GASTRO + SOCIAL lifestyle (friends toasting beer, biergarten,
  pub) plus clean white studio shots (a single glass showing the Eichstrich + fill
  line). '60+ JAHRE QUALITÄT' trust badge. IMAGE 7 (close) = THE BRAND IMAGE:
  restaurant/pub scene, 'Mehr als 10.000 Restaurants vertrauen auf VAN WELL' +
  '60+ Jahre' + crown logo — the same brand-trust close as the catalog.

Verified facts:
  - 12 klassische Willibecher-Biergläser, 0,5 L Fassungsvermögen
  - deutlich sichtbarer EICHSTRICH (geeicht — fairer/exakter Ausschank, Gastro-relevant)
  - DICKWANDIGES, robustes Glas; VERSTÄRKTER Glasboden
  - spülmaschinengeeignet; stapelbar
  - Van Well Traditionsmarke seit über 60 Jahren; Gastro + Zuhause

Angle: der Gastro-Klassiker — robust, geeicht, 12er-Vorteilsset, für Kneipe & Zuhause.
No review VoC in the listing — lean on the facts + gastro-classic angle.

OVERLAY RULE: sell the OUTCOME/identity, not the action. ≤30 chars AND ≤5 words,
smooth (no fragments, no '·' middots). overlay_sub ≤90. module headline ≤38.
bullet head <b>…</b> ≤45. TITLE ≤200 real chars.

Compliance: German copy; no $/€ prices, no URL/.com/.de, no beste/#1/garantiert,
honest (Klassiker, robust, geeicht — no over-durability claim).
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
PLAN_NO = "05"


# ===== KW-led, marketing-optimized DE copy (customer-facing) =====

# Title is HTML-escaped, so literal "&" counts as 1 char. Keep ≤200 real chars. German.
TITLE = (
    "Van Well Willibecher 0,5 L 12er-Set — 12 klassische Biergläser 0,5 mit Eichstrich · "
    "dickwandiges Bierglas mit verstärktem Boden · spülmaschinengeeignet · "
    "Gläser-Set für Gastronomie & Zuhause"
)

BULLETS = [
    "<b>DER GASTRO-KLASSIKER FÜRS BIER</b> — Der klassische Willibecher, der in jede Kneipe, "
    "jeden Biergarten und an jeden Tisch zuhause gehört. 12 Biergläser 0,5 für den perfekten "
    "Bier-Moment mit Freunden.",

    "<b>GEEICHT MIT EICHSTRICH FÜR 0,5 L</b> — Der deutlich sichtbare Eichstrich sorgt für einen "
    "fairen, exakten Ausschank – 0,5 Liter, jedes Mal genau. In der Gastronomie Pflicht, zuhause "
    "einfach ehrlich eingeschenkt.",

    "<b>DICKWANDIG &amp; ROBUST GEBAUT</b> — Dickwandiges Glas mit verstärktem Boden, gemacht für den "
    "täglichen Einsatz. Diese Willibecher stecken Spülgänge, volle Tabletts und lange Abende weg – "
    "Tag für Tag.",

    "<b>SPÜLMASCHINENFEST &amp; STAPELBAR</b> — Alle 12 Gläser wandern einfach in die Spülmaschine "
    "und lassen sich platzsparend stapeln. Schnell sauber, schnell verstaut – ideal für Theke, "
    "Küche und Party.",

    "<b>12ER-SET MIT SYSTEM</b> — Das 12er-Vorteilsset für Gastronomie, Feste und Zuhause: "
    "genug Biergläser 0,5 für Freunde, Familie und Gäste. Van Well steht seit über 60 Jahren "
    "für Glas und Porzellan.",
]


IMAGES = [
    AIImagePlanItem(
        name="Bild 1 — Main Hero (3 Optionen für A/B-Test)",
        role="hero",
        background="Clean white studio (#FFFFFF) with a soft cool key light. Same backdrop across all 3 options for a clean split-test. Van Well crown wordmark top-right on any lifestyle-tinted option.",
        purpose="Win the click in the amazon.de beer-glass grid — read instantly as THE classic Willibecher set, not a generic glass.",
        visual=(
            "Designer mocks up ALL 3 options; brand picks the winner via Amazon Manage Your "
            "Experiments. Each option: ONE navy #1C2E4A overlay bar, ONE hero subject, ONE cue — "
            "clean, never stacked.\n\n"
            "▸ OPTION A — THE 12er-SET LAID OUT (wins on value/quantity)\n"
            "All 12 Willibecher arranged in a clean 4×3 (or 6×2) formation on white, one glass "
            "front-center filled with golden beer showing a crisp head. ~70% of frame.\n"
            "NAVY BAR top: white bold sans headline 'DER GASTRO-KLASSIKER'.\n"
            "NAVY ICON-BADGE ROW bottom: 0,5 L mit Eichstrich · verstärkter Boden · dickwandig · "
            "spülmaschinengeeignet · 12er-Set. Crown wordmark top-right.\n\n"
            "▸ OPTION B — EICHSTRICH MACRO (wins on the trust differentiator)\n"
            "One glass, 3/4 turn, filled to the fill line, a sharp macro call-out ring around the "
            "visible EICHSTRICH with the '0,5 L' mark. Faint remaining glasses stacked soft-focus behind.\n"
            "NAVY BAR top-left: 'GEEICHT AUF 0,5 LITER'. Crown wordmark top-right.\n\n"
            "▸ OPTION C — SOCIAL TOAST (wins on the beer-moment identity)\n"
            "Warm biergarten table, several hands toasting the Willibecher full of beer (hands only, "
            "no faces), condensation on the glass. Van Well crown wordmark top-right.\n"
            "NAVY BAR bottom: 'FÜR DEN PERFEKTEN BIER-MOMENT'.\n\n"
            "All 3: hero subject dominant ~70%, navy bar ~8%, same light / same white base so the "
            "split test isolates composition, not light."
        ),
        overlay="(one navy bar per option — see visual direction)",
        overlay_sub="3 Hero-Optionen geliefert — A/B-Test, Sieger behalten.",
        props=[
            "OPTION A: all 12 Willibecher in formation + 1 filled front glass + navy icon-badge row",
            "OPTION B: single glass, Eichstrich macro call-out ring, 0,5 L mark",
            "OPTION C: biergarten table, hands toasting (no faces), condensation",
        ],
        lighting="Cool clean studio key from top-left (5000K) for A/B; warm biergarten side-light for option C. Rim light so the beer glows and the Eichstrich reads.",
        why_it_works=(
            "Three triggers against three buyer motives: A sells the 12-set value and reads as THE "
            "classic at a glance, B owns the Eichstrich trust differentiator no generic glass shows, "
            "C sells the beer-moment identity. One navy bar, one subject — readable on a mobile thumbnail."
        ),
        ctr="The instantly recognizable Willibecher shape plus the navy 'GASTRO-KLASSIKER' bar beats anonymous glass listings in the DE grid; the 12-set and the Eichstrich are the two strongest click promises for 'biergläser 0,5' and 'willibecher 0,5l'.",
        cvr="Instant clarity on format (0,5 L Willibecher), quantity (12er-Set) and the geeicht/robust angle cuts bounce; the crown wordmark signals an established brand, not a no-name import.",
    ),
    AIImagePlanItem(
        name="Bild 2 — Hook: Der Eichstrich (geeicht auf 0,5 L)",
        role="hook",
        background="Clean white studio, cool key light. Navy #1C2E4A overlay bar, crown wordmark top-right.",
        purpose="Establish the Eichstrich differentiator instantly — the fair, exact 0,5 L pour that generic glasses can't prove.",
        visual=(
            "Single Willibecher, 3/4 turn, filled with golden beer exactly to the fill line. A crisp "
            "macro call-out ring highlights the engraved EICHSTRICH and the '0,5 L' calibration mark. "
            "Thin navy leader line labels it 'Eichstrich — geeicht'. Small caption strip bottom: "
            "'fairer, exakter Ausschank'. Navy bar carries the headline; crown wordmark top-right."
        ),
        overlay="GEEICHT AUF 0,5 LITER.",
        overlay_sub="Der Eichstrich sorgt für fairen, exakten Ausschank – jedes Mal genau.",
        props=["single filled Willibecher", "Eichstrich macro call-out ring", "0,5 L mark", "navy leader line", "caption strip"],
        lighting="Cool clean studio key from top-left, rim light on the glass so the engraved Eichstrich and the beer read sharply.",
        why_it_works=(
            "The Eichstrich is the one visible, credible differentiator in a sea of look-alike beer "
            "glasses. It answers 'why this glass?' in one frame and speaks directly to gastro buyers "
            "who need a calibrated pour."
        ),
        ctr="'Geeicht auf 0,5 Liter' is a concrete, honest trust hook that separates this set from generic 'biergläser 0,5' listings and pulls the Gastronomie searcher.",
        cvr="Proves the fair-pour claim visually, so the buyer trusts the volume — removing the top doubt behind a beer-glass purchase.",
    ),
    AIImagePlanItem(
        name="Bild 3 — Educate: Maße & Aufbau (0,5 L · dickwandig · verstärkter Boden)",
        role="educate",
        background="White studio with a navy #1C2E4A footer band. Crown wordmark top-right.",
        purpose="Make the build and spec concrete — the robust, dishwasher-safe classic worth buying by the dozen.",
        visual=(
            "Single Willibecher center with clean navy call-out lines to labeled specs:\n"
            "  • 0,5 L FASSUNGSVERMÖGEN — mit sichtbarem Eichstrich\n"
            "  • DICKWANDIGES GLAS — robust für den Alltag\n"
            "  • VERSTÄRKTER BODEN — standsicher, stabil\n"
            "  • SPÜLMASCHINENGEEIGNET — schnell wieder sauber\n"
            "Navy footer band carries the icon-badge row (Eichstrich · verstärkter Boden · dickwandig · "
            "spülmaschinengeeignet · stapelbar) in white."
        ),
        overlay="ROBUST GEBAUT FÜR DEN ALLTAG.",
        overlay_sub="Dickwandiges Glas, verstärkter Boden, 0,5 L mit Eichstrich.",
        props=["single glass", "4 navy spec call-out lines", "navy footer icon-badge row"],
        lighting="Flat clean studio light — legibility over atmosphere; a light rim so the glass edge reads.",
        why_it_works=(
            "Turns the facts into a scannable spec card. Buyers filtering on size and durability see "
            "the 0,5 L Eichstrich, the thick wall and the reinforced base at a glance — justifying the "
            "set over a cheaper thin glass, without overclaiming."
        ),
        ctr="The spec card answers the size and robustness questions DE buyers scan for, lifting relevance for 'bierglas 0,5' and 'gläser 0,5 liter'.",
        cvr="Concrete build details (dickwandig, verstärkter Boden) set honest, confident expectations and pre-empt 'is it flimsy?' doubts.",
    ),
    AIImagePlanItem(
        name="Bild 4 — Desire: Der perfekte Bier-Moment (Social/Biergarten)",
        role="desire",
        background="Warm biergarten / pub scene, golden late-afternoon side-light. Van Well crown wordmark top-right.",
        purpose="Place the buyer in the moment — friends toasting cold beer in these glasses at a table.",
        visual=(
            "Warm biergarten or pub table: several Willibecher full of golden beer with fresh heads, "
            "hands toasting (hands only, no faces), condensation on the glass, a pretzel and coasters "
            "as props, wood table. Navy #1C2E4A bar carries the headline; crown wordmark top-right. "
            "Small navy tag: 'Kneipe · Biergarten · Zuhause'."
        ),
        overlay="FÜR DEN PERFEKTEN BIER-MOMENT.",
        overlay_sub="Anstoßen mit Freunden – in der Kneipe, im Biergarten und zuhause.",
        props=["several filled Willibecher", "hands toasting (no faces)", "condensation", "pretzel", "coasters", "wood table"],
        lighting="Warm golden side-light from camera-right, rim on the glasses so the beer glows; lived-in, appetizing, not staged.",
        why_it_works=(
            "Sells the emotional outcome behind the purchase — the shared beer moment. The classic "
            "Willibecher in a real biergarten scene is the aspirational payoff that a plain studio "
            "shot can't deliver."
        ),
        ctr="The warm toast scene is universally desirable for anyone hosting, running a pub or setting up a biergarten table, widening appeal beyond a spec search.",
        cvr="Shows the glasses in the exact context of use, so buyers picture their own gatherings and justify the 12-set.",
    ),
    AIImagePlanItem(
        name="Bild 5 — Trust: Spülmaschinenfest & stapelbar (Alltagstauglich)",
        role="trust",
        background="Clean kitchen / gastro back-of-house, white with cool tones. Navy #1C2E4A bar, crown wordmark top-right.",
        purpose="Defuse the practicality worry — 12 glasses that are effortless to clean and store.",
        visual=(
            "Two-panel icon story:\n"
            "  LEFT — the 12 Willibecher neatly stacked, compact, saving shelf space (stapelbar cue).\n"
            "  RIGHT — a glass going into an open dishwasher rack (spülmaschinengeeignet cue).\n"
            "Navy icon-badge strip: spülmaschinengeeignet · stapelbar · 12er-Set. Navy bar headline; "
            "crown wordmark top-right."
        ),
        overlay="SCHNELL SAUBER, PLATZSPAREND.",
        overlay_sub="Spülmaschinenfest und stapelbar – ideal für Theke, Küche und Party.",
        props=["12 stacked glasses", "open dishwasher rack + glass", "navy icon-badge strip"],
        lighting="Clean even light — icons and stacking readable on the thumbnail.",
        why_it_works=(
            "Answers the practical objection behind buying a dozen glasses: cleanup and storage. "
            "Dishwasher-safe and stackable is exactly what a busy pub or a host wants to see before "
            "committing to a 12-set."
        ),
        ctr="The dishwasher + stacking cues attract practical DE buyers outfitting a kitchen, party or gastro setting.",
        cvr="Removes the 'too much to wash and store' hesitation, making the 12-set feel effortless rather than a burden.",
    ),
    AIImagePlanItem(
        name="Bild 6 — Desire: 12er-Set (Vorteil & Einsatzorte)",
        role="desire",
        background="White studio with warm accent, navy #1C2E4A footer band. Crown wordmark top-right.",
        purpose="Show the value of the dozen — enough glasses for every occasion, from pub to party to resale.",
        visual=(
            "Hero of all 12 Willibecher laid out in a clean formation, a few filled with beer for warmth. "
            "Navy footer icon-badge row of use-cases: Kneipe · Biergarten · Party · Zuhause. "
            "Small navy tag: '12 Gläser 0,5 L'. Navy bar headline; crown wordmark top-right."
        ),
        overlay="12 GLÄSER FÜR JEDEN ANLASS.",
        overlay_sub="Genug Biergläser 0,5 für Kneipe, Biergarten, Party und Zuhause.",
        props=["all 12 Willibecher laid out", "a few filled with beer", "navy use-case icon-badge row"],
        lighting="Warm, even studio light so the full set reads as a generous, appetizing lineup.",
        why_it_works=(
            "Expands perceived value: one purchase covers a whole table, a party or a gastro service. "
            "Hits the cost-per-glass math and matches broad DE search terms (gläser set, gläser set 12 "
            "teilig, pint gläser)."
        ),
        ctr="The full dozen laid out signals value-per-glass and speaks to several intents at once (party, gastro, home), maximizing grid relevance.",
        cvr="More glasses for more occasions = higher perceived value, making the 12-set easy to justify over a smaller pack.",
    ),
    AIImagePlanItem(
        name="Bild 7 — Close: Marken-Vertrauen (THE BRAND IMAGE)",
        role="close",
        background="Warm restaurant / pub interior, golden evening light — the same brand-trust close as the catalog. Van Well crown wordmark prominent top-right.",
        purpose="Close on brand identity — the established gastro brand thousands of restaurants trust.",
        visual=(
            "Mid-range restaurant / pub scene: Willibecher full of beer on a set table or a polished bar, "
            "warm interior soft-focused behind (guests as ambience, no faces in focus). VAN WELL crown "
            "wordmark prominent top-right. Navy #1C2E4A bar carries the trust line; a small "
            "'60+ JAHRE QUALITÄT' badge sits in the navy bar. Consistent with the brand-trust close "
            "across the Van Well catalog."
        ),
        overlay="10.000 RESTAURANTS VERTRAUEN.",
        overlay_sub="Mehr als 10.000 Restaurants vertrauen auf Van Well – seit über 60 Jahren.",
        props=["Willibecher full of beer on set table / bar", "warm restaurant interior (soft focus)", "VAN WELL crown wordmark", "navy bar", "'60+ JAHRE QUALITÄT' badge"],
        lighting="Warm golden evening restaurant light, inviting and premium — not cold, not sterile.",
        why_it_works=(
            "Closes on the brand promise that matters before checkout: an established German brand that "
            "professional kitchens rely on. The '10.000 Restaurants' + '60+ Jahre' + crown is the "
            "consistent trust signature that ties the whole Van Well catalog together."
        ),
        ctr="The 'trusted by restaurants' signal differentiates from anonymous import glassware and reassures quality-conscious DE buyers.",
        cvr="Gastro trust and 60+ years of heritage create the final confidence that seals the purchase.",
    ),
]


MODULES = [
    AIModule(
        name="Modul 1 — Brand-Banner",
        role="a+_banner",
        headline="DER GASTRO-KLASSIKER.",
        body=(
            "Der klassische Willibecher von Van Well: 12 robuste Biergläser mit 0,5 L und deutlich "
            "sichtbarem Eichstrich. Für Kneipe, Biergarten und Zuhause – der perfekte Bier-Moment, "
            "Abend für Abend. Van Well, seit über 60 Jahren."
        ),
        visual="Wide cinematic biergarten / pub scene: Willibecher full of golden beer front-center, warm side-light, wood table and soft-focused guests behind. VAN WELL crown wordmark top-right; small '60+ Jahre Qualität' badge in a navy #1C2E4A band.",
        alt="Van Well Willibecher 0,5 L voll Bier auf einem Biergartentisch in warmem Licht, klassischer Gastro-Look.",
    ),
    AIModule(
        name="Modul 2 — Größe & Aufbau (Specs mit Icons)",
        role="a+_banner",
        headline="0,5 L MIT EICHSTRICH.",
        body=(
            "Klassischer Willibecher mit 0,5 Liter Fassungsvermögen und deutlich sichtbarem Eichstrich "
            "für einen fairen, exakten Ausschank. Dickwandiges, robustes Glas mit verstärktem Boden – "
            "gemacht für den täglichen Einsatz. Spülmaschinengeeignet und stapelbar."
        ),
        visual="Wide spec banner: single Willibecher center with navy #1C2E4A call-out lines to 0,5 L, Eichstrich, dickwandiges Glas, verstärkter Boden. Navy icon-badge row along the bottom (Eichstrich · verstärkter Boden · dickwandig · spülmaschinengeeignet · stapelbar) in white. Crown wordmark top-right.",
        alt="A+ Banner: Willibecher mit Maßen 0,5 L, Eichstrich, dickwandiges Glas und verstärkter Boden, mit Icon-Badges.",
    ),
    AIModule(
        name="Modul 3 — Carousel (4 Kacheln): Warum dieser Willibecher",
        role="a+_carousel",
        headline="WARUM DIESER WILLIBECHER",
        body=(
            "Kachel 1: <b>GEEICHT · 0,5 L</b> — sichtbarer Eichstrich für fairen Ausschank.<br/>"
            "Kachel 2: <b>DICKWANDIG</b> — robustes Glas mit verstärktem Boden.<br/>"
            "Kachel 3: <b>SPÜLMASCHINENFEST</b> — schnell sauber, stapelbar verstaut.<br/>"
            "Kachel 4: <b>12ER-SET</b> — genug Gläser für Gäste, Feste und Gastro."
        ),
        visual="4 square tiles, navy #1C2E4A accent corner per tile, small white line icons (Eichstrich mark · thick-wall glass · dishwasher · 12-set grid). Consistent studio look.",
        alt="Vier-Kachel A+ Carousel: geeicht 0,5 L, dickwandig, spülmaschinenfest, 12er-Set.",
    ),
    AIModule(
        name="Modul 4 — Perfekt für … (Einsatzorte mit Icon-Badge-Reihe)",
        role="a+_banner",
        headline="PERFEKT FÜR JEDEN ANLASS.",
        body=(
            "Ob Kneipe, Biergarten, Party oder gemütlicher Abend zuhause – der Willibecher passt "
            "überall. Das 12er-Set liefert genug Biergläser 0,5 für Freunde, Familie und Gäste, "
            "in der Gastronomie wie beim Feiern daheim."
        ),
        visual="Wide use-case banner: 4 warm scenes in a row (pub · biergarten · party table · home), each with a filled Willibecher. Navy #1C2E4A icon-badge row across the bottom: Kneipe · Biergarten · Party · Zuhause. Crown wordmark top-right.",
        alt="A+ Banner Perfekt für: Kneipe, Biergarten, Party und Zuhause, mit Willibecher-Gläsern und Icon-Badge-Reihe.",
    ),
    AIModule(
        name="Modul 5 — Carousel (4 Kacheln): Alltagstauglich & 12er-Set",
        role="a+_carousel",
        headline="GEMACHT FÜR DEN EINSATZ",
        body=(
            "Kachel 1: <b>SPÜLMASCHINENGEEIGNET</b> — alle 12 Gläser einfach reinstellen.<br/>"
            "Kachel 2: <b>STAPELBAR</b> — platzsparend verstaut in Küche und Theke.<br/>"
            "Kachel 3: <b>VERSTÄRKTER BODEN</b> — standsicher und stabil im Alltag.<br/>"
            "Kachel 4: <b>12 GLÄSER 0,5 L</b> — das Vorteilsset für jeden Anlass."
        ),
        visual="4 identically composed tiles, navy accent corner per tile: stacked glasses · dishwasher rack · reinforced base macro · the 12 glasses laid out. Consistent light.",
        alt="Vier-Kachel A+ Carousel: spülmaschinengeeignet, stapelbar, verstärkter Boden, 12 Gläser 0,5 L.",
    ),
    AIModule(
        name="Modul 6 — Premium Q&A",
        role="a+_qa",
        headline="HÄUFIGE FRAGEN",
        body=(
            "<b>F.</b> Sind die Gläser geeicht?<br/>"
            "<b>A.</b> Ja. Jeder Willibecher hat einen deutlich sichtbaren Eichstrich bei 0,5 Litern – "
            "für einen fairen, exakten Ausschank in der Gastronomie und zuhause.<br/><br/>"
            "<b>F.</b> Wie viele Gläser sind im Set?<br/>"
            "<b>A.</b> Das Set enthält 12 klassische Willibecher mit je 0,5 L – genug für Gäste, "
            "Feste und den täglichen Gastro-Einsatz.<br/><br/>"
            "<b>F.</b> Sind die Gläser spülmaschinengeeignet?<br/>"
            "<b>A.</b> Ja. Alle 12 Gläser sind spülmaschinengeeignet und lassen sich zudem "
            "platzsparend stapeln.<br/><br/>"
            "<b>F.</b> Wie robust sind die Willibecher?<br/>"
            "<b>A.</b> Es ist dickwandiges Glas mit verstärktem Boden, gemacht für den täglichen "
            "Einsatz in Kneipe, Biergarten und zuhause.<br/><br/>"
            "<b>F.</b> Wofür eignet sich das Set?<br/>"
            "<b>A.</b> Für Gastronomie, Biergarten, Partys und Zuhause – überall dort, wo klassische "
            "Biergläser 0,5 gebraucht werden."
        ),
        visual="Vertical Q/A table, navy #1C2E4A divider lines between questions, small navy F./A. labels.",
        alt="Premium Q&A Modul mit den häufigsten Fragen zum Van Well Willibecher 0,5 L 12er-Set.",
    ),
    AIModule(
        name="Modul 7 — Marken-Vertrauen (Brand-Trust Close)",
        role="a+_banner",
        headline="RESTAURANTS VERTRAUEN VAN WELL.",
        body=(
            "Mehr als 10.000 Restaurants vertrauen auf Van Well. Seit über 60 Jahren stehen wir für "
            "hochwertiges Glas und Porzellan mit einem starken Preis-Leistungs-Verhältnis – für "
            "Gastronomen und qualitätsbewusste Privatkunden."
        ),
        visual="Wide brand-trust banner: warm restaurant / pub interior, Willibecher full of beer on a set table or bar, guests soft-focused behind. VAN WELL crown wordmark prominent top-right; '60+ Jahre Qualität' badge in a navy #1C2E4A band. Same brand-trust close as the catalog.",
        alt="A+ Brand-Trust Banner: Van Well Willibecher in einem Restaurant, mehr als 10.000 Restaurants vertrauen auf Van Well, 60+ Jahre.",
    ),
]


QA = [
    AIQA(q="Sind die Willibecher geeicht?",
         a="Ja. Jedes Glas hat einen deutlich sichtbaren Eichstrich bei 0,5 Litern. Das sorgt für einen fairen, exakten Ausschank – in der Gastronomie Pflicht, zuhause einfach ehrlich eingeschenkt."),
    AIQA(q="Wie viele Gläser enthält das Set?",
         a="Das Set enthält 12 klassische Willibecher mit je 0,5 L Fassungsvermögen – genug für Freunde, Familie, Gäste und den täglichen Gastro-Einsatz."),
    AIQA(q="Sind die Gläser spülmaschinengeeignet?",
         a="Ja. Alle 12 Willibecher sind spülmaschinengeeignet. Nach dem Einsatz einfach in die Spülmaschine – schnell wieder sauber."),
    AIQA(q="Lassen sich die Gläser stapeln?",
         a="Ja. Die Willibecher sind stapelbar und lassen sich platzsparend in Küche, Theke oder Schrank verstauen."),
    AIQA(q="Wie robust sind die Gläser?",
         a="Es ist dickwandiges, robustes Glas mit verstärktem Boden, gemacht für den täglichen Einsatz in Kneipe, Biergarten und zuhause. Ein Klassiker, der viel mitmacht – für langlebige Nutzung bitte trotzdem sorgsam behandeln."),
    AIQA(q="Wofür eignet sich der Willibecher?",
         a="Für Gastronomie, Biergarten, Oktoberfest, Partys und Zuhause – überall dort, wo klassische Biergläser mit 0,5 L gebraucht werden."),
    AIQA(q="Wer ist Van Well?",
         a="Van Well ist eine Traditionsmarke für Glas und Porzellan seit über 60 Jahren. Mehr als 10.000 Restaurants vertrauen auf Van Well – für Gastronomen und qualitätsbewusste Privatkunden."),
]


# Backend KWs — German, stem-deduped, byte-packed. Avoid brand/title duplicates & superlatives.
BACKEND = (
    "willy becher willibecher biergläser bierglas trinkglas trinkgläser gläserset gläser "
    "500ml 0 5 liter pint pils weizenbiergläser schoppenglas bierkrug bierkrüge stapelbar "
    "geeicht eichstrich dickwandig gastronomie kneipe biergarten oktoberfest party feiern "
    "wiederverkauf spülmaschinenfest robust bar theke set 12 teilig trinkgeschirr bier"
)


def main() -> None:
    print("Loading Van Well customer + parsing Willibecher Excel…")
    cust = load_customer("van_well")
    brief = parse_excel(EXCEL)
    OUT = HERE / f"{PLAN_NO}_VanWell_Willibecher_Image Plan.pdf"
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
