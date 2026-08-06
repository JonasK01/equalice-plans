"""Jotti Polsterreiniger 500 ml (Sprühflasche) — Image Plan 05
Hand-written senior copy injected into the branded ReportLab pipeline.

Marketplace: amazon.de
LANGUAGE SPLIT (the new standard):
  • ENGLISH = art-direction / strategy (designer-facing): image purpose, background,
    visual, props, lighting, why_it_works, ctr, cvr, and module `visual`.
    Written as a senior art director briefing a photographer/designer.
  • GERMAN  = marketplace / customer-facing: TITLE, BULLETS, image overlay + overlay_sub,
    module headline + body, QA, BACKEND.

OVERLAY STANDARD: sell the OUTCOME, not the action. Every overlay leads with the
result / transformation / defused fear — never a process triad. (The old
"SPRÜHEN. EINARBEITEN. SAUBER." is retired; the method now lives in art-direction.)
Hard limits (auto-linted on build): overlay ≤30ch & ≤5 words; overlay_sub ≤90;
module headline ≤38; bullet head <b>…</b> ≤45.

Verified facts (see SOURCE_NOTES.md):
  - 500 ml Sprühflasche; kraftvolle, tiefenwirksame Reinigung für Textilien & Polster
  - für viele Materialien; einfache Sprüh-Anwendung; präziser Sprühkopf (review-praised)
  - für Haushalt & Auto in einem; schonend für empfindliche Textilien
  - bei Bedarf wiederholbare Intensivreinigung; keine Ränder; Deutsche Manufakturqualität

Review insight used:
  praised  = präziser Sprühkopf / keine Ränder / leicht einzuarbeiten / angenehmer Geruch
  objection= "Reinigungskraft nicht immer überzeugend" → defuse HONEST: bei hartnäckigen
             Flecken einwirken lassen + wiederholen; ehrliches Before/After (kein Wunder).

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
PLAN_NO = "05"


# ===== KW-led, marketing-optimized DE copy (customer-facing) =====

# Title is HTML-escaped, so literal "&" counts as 1 char. Keep ≤200 real chars.
TITLE = (
    "Jotti Polsterreiniger 500 ml Sprüh — tiefenwirksam für Polster & Textil · "
    "Sofa Auto Matratze Teppich · Fleckentferner für Haushalt & Auto · präziser "
    "Sprühkopf, keine Ränder · Manufaktur"
)

BULLETS = [
    "<b>SOFA &amp; AUTOSITZE WIEDER WIE FRISCH</b> — Müde, fleckige Polster sehen sichtbar "
    "frisch und sauber aus: Dieser Polsterreiniger löst Schmutz tief aus der Faser, statt "
    "ihn nur an der Oberfläche zu verwischen – Sofa, Couch und Autositze wie neu.",

    "<b>PRÄZISER SPRÜHKOPF, KEIN RAND</b> — Aufsprühen, kurz einwirken, abnehmen: Der "
    "Sprühkopf dosiert sehr präzise und lässt sich super leicht einarbeiten – das "
    "Fleckenspray hinterlässt keine unschönen Ränder auf dem Polster.",

    "<b>EIN COUCH REINIGER FÜR HAUS &amp; AUTO</b> — Sofa, Couch, Autositze, Matratze, "
    "Teppich und Polsterstühle mit nur einer Flasche: Sofa Reiniger, Matratzenreiniger und "
    "Teppichreiniger in einem – im ganzen Haushalt und im Auto einsatzbereit.",

    "<b>ANGENEHM IM GERUCH, SCHONEND ZUR FASER</b> — Der Duft ist angenehm und nicht zu "
    "chemisch, kein beißender Chemiegeruch. Für viele Materialien geeignet und schonend – "
    "an einer verdeckten Stelle kurz vortesten.",

    "<b>AUCH HARTNÄCKIGES WIRD SICHTBAR SAUBER</b> — Tiefenwirksam gegen tiefsitzenden "
    "Schmutz: Bei hartnäckigen Flecken einfach einwirken lassen und wiederholen. Ehrliche, "
    "wiederholbare Intensivreinigung aus deutscher Manufaktur.",
]


IMAGES = [
    AIImagePlanItem(
        name="Bild 1 — Main Hero (3 Optionen für A/B-Test)",
        role="hero",
        background=(
            "Light, clean set, warm off-white (#EFE6D9) seamless with soft side-shadow; "
            "hint of living-room / car-interior texture in the lower 15% band. Identical "
            "background across all 3 options so the split-test isolates the message, not the set."
        ),
        purpose=(
            "Win the click in the amazon.de upholstery-cleaner grid — stand apart from the "
            "generic spray bottles by leading with visible proof, not packaging."
        ),
        visual=(
            "Mock up ALL 3 options; brand picks the winner via Amazon Manage Your Experiments. "
            "Each option: ONE callout, ONE action cue, ONE prop — clean, never stacked.\n\n"
            "▸ OPTION A — BEFORE/AFTER STAIN (wins on proof)\n"
            "Center the 500 ml spray bottle (label readable, slight 3/4 turn, ~55% of frame). "
            "Behind it a sofa/upholstery panel split diagonally: left side visibly stained/dull, "
            "right side clean/fresh — keep it HONEST, allow faint residual texture, no flawless "
            "miracle. Fine spray-mist cue along the split line.\n"
            "CALLOUT top-right: badge with the German overlay (brown #8B5A2B, white type).\n\n"
            "▸ OPTION B — SPRAY ACTION (wins on method)\n"
            "Bottle left; a hand (hand only, no face) mists a fine spray onto a car seat, "
            "microfiber cloth staged as a prop.\n"
            "CALLOUT top-left: short outcome line (dark #2F2A26, white type).\n\n"
            "▸ OPTION C — USE-CASE STACK (wins on versatility)\n"
            "Bottle centered, four thin line-icons radiating: sofa · car · mattress · carpet (brown).\n"
            "CALLOUT bottom-right: short German overlay (brown #8B5A2B).\n\n"
            "All three: bottle dominant ~55%, callout ~6%, identical light and background."
        ),
        overlay="POLSTER WIE FRISCH.",
        overlay_sub="Tief in der Faser sauber – Sofa, Auto &amp; Matratze.",
        props=[
            "OPTION A: bottle + split upholstery panel (stained/clean) + spray mist + badge",
            "OPTION B: bottle + hand + spray mist on car seat + microfiber cloth",
            "OPTION C: bottle + 4 use-case line-icons (sofa/car/mattress/carpet) + badge",
        ],
        lighting=(
            "Bright, clean side-light from camera-right (4000–4500K), rim light on the bottle so "
            "the label pops. Keep the exact same lighting across all 3 options."
        ),
        why_it_works=(
            "Three triggers against three buyer motives: A delivers the honest stain proof (the "
            "strongest signal in the cleaner grid), B proves the easy spray method, C shows the "
            "versatility. One callout, one action cue, one prop — legible on a mobile thumbnail."
        ),
        ctr=(
            "A visible stain-to-clean contrast on sofa and car seat beats the static competitor "
            "bottles in the DE grid — the before/after is the single strongest click promise here."
        ),
        cvr=(
            "Instant clarity on format (spray bottle), benefit (deep-cleaning) and surfaces (sofa, "
            "car, mattress, carpet) cuts bounce; the precise nozzle and Manufaktur cue build the "
            "trust needed to commit to the purchase."
        ),
    ),
    AIImagePlanItem(
        name="Bild 2 — Hook: Tiefenwirksam statt nur Oberfläche",
        role="hook",
        background="Cream #EFE6D9 seamless, warm side-light, subtle fabric weave texture.",
        purpose=(
            "Establish the core benefit in one glance — the clean reaches into the fibre, not just "
            "the surface; answer 'does this really clean properly?' immediately."
        ),
        visual=(
            "Upholstery cross-section cue: fibre surface on top, a soiled layer beneath. An arrow "
            "shows the spray mist drawing down into the depth and lifting the dirt. LEFT a small "
            "'surface only' cue struck through; RIGHT 'down into the fibre'. Bottle anchors the "
            "right edge. Bottom caption strip with the three-step micro-cue (spray · dwell · wipe)."
        ),
        overlay="TIEF IN DER FASER.",
        overlay_sub="Löst Schmutz tief aus dem Gewebe – nicht nur an der Oberfläche.",
        props=["upholstery cross-section cue", "spray-mist depth arrow", "Jotti spray bottle", "caption strip"],
        lighting="Even warm front-side light, light contact shadow under the props.",
        why_it_works=(
            "Makes 'deep-cleaning' visually tangible rather than just a word on the label. The fibre "
            "cross-section answers 'does this actually clean?' in a single frame and backs the core USP."
        ),
        ctr=(
            "The 'surface only vs. into the fibre' contrast hits the DE buyer hunting for real deep "
            "cleaning on sofa, mattress and car seats — not a surface freshener."
        ),
        cvr="Proves cleaning depth and positions the spray as a serious cleaner, not a mere refresher.",
    ),
    AIImagePlanItem(
        name="Bild 3 — Educate: 3 Schritte zur sauberen Faser",
        role="educate",
        background="White with a brown accent band (#8B5A2B) in the footer.",
        purpose=(
            "Explain the simple application and establish the correct method at the same time, so the "
            "buyer feels 'I can do this'."
        ),
        visual=(
            "Top headline area, then 3 numbered step tiles with line-icons:\n"
            "  1. SPRAY ON — precise nozzle, even coverage\n"
            "  2. LET IT DWELL — short dwell; longer for stubborn stains\n"
            "  3. WIPE OFF — lift with a clean cloth, no rings\n"
            "Bottle anchored center or right. Brown footer band carries the 'für viele Materialien' line. "
            "Keep it flat and legible — this is the instructional tile."
        ),
        overlay="IN MINUTEN WIE NEU.",
        overlay_sub="Präziser Sprühkopf, leicht einzuarbeiten – ganz ohne Rand.",
        props=["3 numbered step tiles with icons", "Jotti bottle", "microfiber cloth", "footer band"],
        lighting="Flat clean studio light — readability over atmosphere.",
        why_it_works=(
            "Makes the application concrete and lowers the effort barrier. The precise nozzle and "
            "'no rings' are genuine real-review strengths — shown here as a foolproof 3-step flow."
        ),
        ctr=(
            "A simple 3-step flow signals 'this is effortless' and pulls DE buyers who want fast, clean "
            "results without hassle."
        ),
        cvr=(
            "A clear method lowers pre-purchase uncertainty; the precise nozzle and 'no rings' directly "
            "calm the fear of leaving stain rings behind."
        ),
    ),
    AIImagePlanItem(
        name="Bild 4 — Desire: Before/After Fleck (ehrlich)",
        role="desire",
        background="Bright living scene, warm daylight.",
        purpose=(
            "Sell the visible result — a real stain is visibly reduced. Keep it honest: a believable "
            "improvement, not a flawless miracle."
        ),
        visual=(
            "Large before/after split of a real sofa armrest OR a car seat with a genuine stain. "
            "LEFT: clear stain/soiling. RIGHT: visibly cleaner, fresh — honest, faint residual texture "
            "allowed (no flawless miracle). Center split line; small bottle in a foreground corner. "
            "Spray/cloth cue on the split line. Small honesty caption near the seam reinforcing the "
            "dwell-and-repeat method (kept in German on the creative)."
        ),
        overlay="SICHTBAR FRISCHER FLECK.",
        overlay_sub="Bei hartnäckigen Flecken: einwirken lassen &amp; wiederholen.",
        props=["sofa armrest or car seat (split, real stain)", "Jotti bottle (foreground)", "microfiber cloth", "spray-mist cue"],
        lighting=(
            "Warm daylight from camera-right, neutral enough that the stain contrast reads honest and "
            "credible rather than retouched."
        ),
        why_it_works=(
            "Uses the before/after proof — the strongest conversion signal in the cleaner category — but "
            "HONESTLY. The 'dwell & repeat' caption proactively disarms the 'cleaning power not always "
            "convincing' objection and sets realistic expectations."
        ),
        ctr=(
            "A real stain that disappears is universally desirable for anyone with a sofa, car seat or "
            "mattress; the honest contrast reads more credible than a too-perfect before/after."
        ),
        cvr=(
            "Visual, realistic result proof instead of exaggeration; the honest expectation lowers "
            "disappointment, returns and 1-star reviews."
        ),
    ),
    AIImagePlanItem(
        name="Bild 5 — Trust: Einwand entkräften (Reinigungskraft)",
        role="trust",
        background="White with cream panels.",
        purpose=(
            "Disarm the main objection ('cleaning power not always convincing') directly on the image by "
            "showing the honest method for tough stains."
        ),
        visual=(
            "Two-column 'for stubborn stains' layout:\n"
            "  Step 1: LET IT DWELL (clock icon) — give the cleaner time to work\n"
            "  Step 2: REPEAT (circular-arrow icon) — intensive clean on demand\n"
            "Beside it a reassurance badge for 'repeatable intensive clean'. Small caption: deep stains "
            "need a second pass. Bottle anchors the right edge."
        ),
        overlay="HARTNÄCKIGES WIRD SAUBER.",
        overlay_sub="Einwirken lassen &amp; wiederholen – wiederholbare Intensivreinigung.",
        props=["2 method icons (clock, circular arrow)", "'repeatable intensive clean' badge", "Jotti bottle"],
        lighting="Clean flat studio light — icons must read on a thumbnail.",
        why_it_works=(
            "Proactively addresses the one recurring negative review ('cleaning power not always "
            "convincing') with the honest fix: dwell + repeat. Pre-disarmed objections lower returns and "
            "1-star reviews and build pre-purchase trust."
        ),
        ctr=(
            "Method clarity attracts DE buyers who know deep stains take time and want exactly that "
            "confirmed on the image."
        ),
        cvr=(
            "Defuses the top purchase objection right on the image; buyers who scan critical reviews see "
            "the solution instead of just the problem."
        ),
    ),
    AIImagePlanItem(
        name="Bild 6 — Desire: Use-Case-Grid (Haushalt & Auto)",
        role="desire",
        background="Cream #EFE6D9, bright living-room light.",
        purpose=(
            "Show the versatility — one cleaner covers every upholstered surface in the home and the car, "
            "lifting perceived value per bottle."
        ),
        visual=(
            "Clean 4-up grid of real upholstery scenes: sofa/couch · car seat · mattress · "
            "carpet/upholstered chair. Each tile carries a bottle or spray-mist cue. Bottle anchored "
            "center or bottom. Small label per tile (sofa · car · mattress · carpet)."
        ),
        overlay="EINE FLASCHE, ALLE POLSTER.",
        overlay_sub="Sofa, Autositze, Matratze, Teppich &amp; Polsterstühle.",
        props=["4 use-case scenes (sofa/car/mattress/carpet)", "Jotti bottle", "spray-mist cues"],
        lighting="Warm, bright side-light, consistent across all 4 tiles.",
        why_it_works=(
            "Expands perceived value: one bottle covers several upholstered surfaces in the home AND the "
            "car. Hits the cost-per-use math and matches the broad DE search terms (sofa, car, mattress, carpet)."
        ),
        ctr=(
            "Speaks to several search intents at once (Polsterreiniger Sofa, Autoinnenreiniger, "
            "Matratzenreiniger, Teppichreiniger) and maximizes grid relevance."
        ),
        cvr="More use cases = higher perceived value per bottle, which makes the purchase easier to justify.",
    ),
    AIImagePlanItem(
        name="Bild 7 — Close: Deutsche Manufaktur",
        role="close",
        background="Workshop/living scene: aged wood, linen, warm side-light.",
        purpose=(
            "Close on brand identity — honest, craft-made Manufaktur quality — the promise that matters "
            "right before checkout."
        ),
        visual=(
            "Mid-range scene: hands (no face) spray and work the cleaner into a beautiful piece of "
            "upholstery. On the wooden table: Jotti spray bottle (label readable), microfiber cloth, a "
            "clean upholstery swatch. Soft-focus warm setting (wood, linen). Small handwritten note card "
            "carrying the German close line ('Ehrliche Tiefenreinigung. — Aus deutscher Manufaktur.')."
        ),
        overlay="DEUTSCHE MANUFAKTUR.",
        overlay_sub="Ehrliche Tiefenreinigung, tief in der Faser – handwerklich gemacht.",
        props=["hands on upholstery (no face)", "Jotti bottle", "microfiber cloth", "clean upholstery swatch", "wooden table/linen", "handwritten note card"],
        lighting="Warm side-light from camera-right, golden tone, lived-in — not staged.",
        why_it_works=(
            "Closes on the brand promise that counts before checkout: honest, craft-made Manufaktur "
            "quality. The hands-on-upholstery gesture is the visual metaphor for care and trust."
        ),
        ctr="The 'German Manufaktur' signal differentiates from anonymous import sprays and attracts quality-conscious DE buyers.",
        cvr="Provenance and craft create the final trust that seals the purchase.",
    ),
]


MODULES = [
    AIModule(
        name="Modul 1 — Brand-Banner",
        role="a+_banner",
        headline="POLSTER WIE FRISCH.",
        body=(
            "Müde, fleckige Polster sehen wieder sichtbar frisch und sauber aus. Der Jotti "
            "Polsterreiniger löst Schmutz und Flecken tief aus der Faser – nicht nur an der "
            "Oberfläche. Einfach aufsprühen, einwirken lassen, abnehmen: für Sofa, Autositze, "
            "Matratze und Teppich. Ehrliche Tiefenreinigung aus deutscher Manufaktur."
        ),
        visual=(
            "Wide cinematic living-room scene: warm side-light, Jotti spray bottle front-center, clean "
            "sofa and car seat in soft focus. Logo top-left in brown #8B5A2B."
        ),
        alt="Jotti Polsterreiniger Sprühflasche auf einem Holztisch in warmem Licht, mit sauberem Polster im Hintergrund.",
    ),
    AIModule(
        name="Modul 2 — Carousel (4 Kacheln): Der Jotti-Vorteil",
        role="a+_carousel",
        headline="DER JOTTI-VORTEIL",
        body=(
            "Kachel 1: <b>TIEF IN DER FASER</b> — löst Schmutz aus dem Gewebe, nicht nur oben.<br/>"
            "Kachel 2: <b>PRÄZISER SPRÜHKOPF</b> — dosiert genau, leicht einzuarbeiten, kein Rand.<br/>"
            "Kachel 3: <b>HAUS &amp; AUTO</b> — Sofa, Autositze, Matratze &amp; Teppich in einem.<br/>"
            "Kachel 4: <b>ANGENEHMER DUFT</b> — frisch statt chemisch, schonend zur Faser."
        ),
        visual=(
            "Four square tiles, brown accent corner on each, small line-icons (fibre · nozzle · "
            "sofa+car · textile). Consistent flat studio light, generous whitespace for scanability."
        ),
        alt="Vier-Kachel A+ Carousel mit den Jotti-Vorteilen: tiefenwirksam, einfach sprühen, Haushalt & Auto, für viele Materialien.",
    ),
    AIModule(
        name="Modul 3 — Banner: In Minuten wie neu",
        role="a+_banner",
        headline="IN MINUTEN WIE NEU.",
        body=(
            "Aufsprühen, kurz einwirken lassen, mit einem sauberen Tuch abnehmen. Der präzise Sprühkopf "
            "dosiert genau, lässt sich super leicht einarbeiten und hinterlässt keinen Rand. Bei "
            "hartnäckigen Flecken einfach länger einwirken lassen und wiederholen – sichtbar frisch."
        ),
        visual=(
            "Wide banner with 3 step panels: spray on → dwell → wipe off. A hand mists a fine spray onto "
            "a car seat, cloth alongside. Warm light, brown/dark palette."
        ),
        alt="A+ Banner: 3-Schritt-Anwendung des Jotti Polsterreinigers – aufsprühen, einwirken, abnehmen.",
    ),
    AIModule(
        name="Modul 4 — Banner: Before/After Fleck",
        role="a+_banner",
        headline="FLECK RAUS, POLSTER FRISCH.",
        body=(
            "Ob Sofa, Autositz oder Matratze: Jotti löst Schmutz und Flecken tief aus dem Gewebe – das "
            "Polster wirkt sichtbar frischer. Ehrlich gesagt: Bei hartnäckigen Flecken einwirken "
            "lassen und den Vorgang wiederholen – wiederholbare Intensivreinigung."
        ),
        visual=(
            "Triptych: LEFT upholstery with a visible stain (before), CENTER the spray/work-in moment, "
            "RIGHT visibly cleaner upholstery (after, honest). Continuous warm light across all three."
        ),
        alt="A+ Triptychon-Banner: Polster vorher mit Fleck, Anwendung, nachher sichtbar sauberer.",
    ),
    AIModule(
        name="Modul 5 — Carousel (4 Kacheln): Für alle Polster",
        role="a+_carousel",
        headline="FÜR ALLE POLSTER",
        body=(
            "Kachel 1: <b>SOFA &amp; COUCH</b> — frischt müde Polstermöbel sichtbar auf.<br/>"
            "Kachel 2: <b>AUTOSITZE</b> — reinigt den Innenraum tief aus der Faser.<br/>"
            "Kachel 3: <b>MATRATZE</b> — löst Flecken tief aus dem Gewebe.<br/>"
            "Kachel 4: <b>TEPPICH &amp; STÜHLE</b> — für Teppiche und Polsterstühle."
        ),
        visual=(
            "Four identically composed use-case tiles, real upholstery scenes, brown accent corner per "
            "tile, consistent warm light."
        ),
        alt="Vier-Kachel A+ Carousel der Anwendungsfälle: Sofa, Autositze, Matratze, Teppich & Polsterstühle.",
    ),
    AIModule(
        name="Modul 6 — Premium Q&A",
        role="a+_qa",
        headline="HÄUFIGE FRAGEN",
        body=(
            "<b>F.</b> Wofür kann ich den Reiniger verwenden?<br/>"
            "<b>A.</b> Für Polster und Textilien im Haushalt und Auto: Sofa, Couch, Autositze, Matratze, "
            "Teppich und Polsterstühle. Für viele Materialien geeignet.<br/><br/>"
            "<b>F.</b> Wie wende ich ihn an?<br/>"
            "<b>A.</b> Aufsprühen, kurz einwirken lassen und mit einem sauberen Tuch abnehmen. Der präzise "
            "Sprühkopf dosiert genau und hinterlässt keine Ränder.<br/><br/>"
            "<b>F.</b> Was tun bei hartnäckigen Flecken?<br/>"
            "<b>A.</b> Länger einwirken lassen und den Vorgang bei Bedarf wiederholen – eine wiederholbare "
            "Intensivreinigung für tiefsitzenden Schmutz.<br/><br/>"
            "<b>F.</b> Ist er schonend zu empfindlichen Textilien?<br/>"
            "<b>A.</b> Ja, er reinigt schonend. Testen Sie ihn vorab an einer verdeckten Stelle.<br/><br/>"
            "<b>F.</b> Wo wird Jotti hergestellt?<br/>"
            "<b>A.</b> In deutscher Manufakturqualität – ehrliche Reinigung, handwerklich gemacht."
        ),
        visual=(
            "Vertical Q/A table, brown divider lines between questions, small F./A. labels in dark #2F2A26."
        ),
        alt="Premium Q&A Modul mit den häufigsten Fragen zu Jotti Polsterreiniger.",
    ),
    AIModule(
        name="Modul 7 — Premium Comparison Chart",
        role="a+_comparison",
        headline="WARUM JOTTI",
        body=(
            "Vergleich über 4 Spalten: <b>Jotti Polsterreiniger</b> · Standard-Polsterspray · "
            "Schaumreiniger · Fleckenspray.<br/><br/>"
            "Zeilen: Tiefenwirksame Reinigung · Präziser Sprühkopf (keine Ränder) · Für Haushalt &amp; Auto · "
            "Für viele Materialien · Schonend zu empfindlichen Textilien · Wiederholbare Intensivreinigung · "
            "Deutsche Manufaktur.<br/><br/>"
            "Jotti-Spalte mit dezentem Braun-Ton hervorheben."
        ),
        visual=(
            "Standard Amazon Premium Comparison Chart, 4 product columns. Competitors named only as "
            "category labels, no brand names. Brown header row, Jotti column subtly highlighted."
        ),
        alt="Premium Vergleichstabelle: Jotti Polsterreiniger vs. Standard-Polsterspray, Schaumreiniger und Fleckenspray.",
    ),
]


QA = [
    AIQA(q="Für welche Polster und Materialien ist der Reiniger geeignet?",
         a="Für Textilien und Polster im Haushalt und Auto: Sofa, Couch, Autositze, Matratze, Teppich und Polsterstühle. Als Sofa Reiniger, Matratzenreiniger und Teppichreiniger in einem ist er für viele Materialien geeignet. Bitte vorab an einer verdeckten Stelle testen."),
    AIQA(q="Wie wende ich den Polsterreiniger an?",
         a="Gleichmäßig aufsprühen, kurz einwirken lassen und mit einem sauberen, leicht feuchten Tuch abnehmen. Der präzise Sprühkopf dosiert genau, lässt sich leicht einarbeiten und hinterlässt keinen Rand – das Polster wirkt danach sichtbar frisch."),
    AIQA(q="Was mache ich bei hartnäckigen Flecken?",
         a="Ehrlich gesagt: Tiefsitzender Schmutz braucht oft einen zweiten Durchgang. Den Reiniger einfach länger einwirken lassen und den Vorgang wiederholen – die Intensivreinigung ist wiederholbar und arbeitet tief in der Faser."),
    AIQA(q="Reinigt das Spray nur an der Oberfläche?",
         a="Nein. Die Reinigung wirkt tiefenwirksam und löst Schmutz tief aus der Faser, nicht nur an der Oberfläche – kein bloßer Textilerfrischer."),
    AIQA(q="Hinterlässt der Reiniger Ränder?",
         a="Richtig angewendet hinterlässt er keinen Rand – das bestätigen viele Kunden. Gleichmäßig aufsprühen, einarbeiten und überschüssige Feuchtigkeit mit einem sauberen Tuch abnehmen."),
    AIQA(q="Riecht das Fleckenspray stark nach Chemie?",
         a="Nein. Der Geruch ist angenehm und nicht zu chemisch – kein beißender Chemiegeruch, der im Raum oder im Auto hängen bleibt."),
    AIQA(q="Ist er für empfindliche Textilien schonend?",
         a="Ja, er reinigt schonend empfindliche Textilien. Testen Sie ihn dennoch vorab an einer verdeckten Stelle, um die Materialverträglichkeit zu prüfen."),
    AIQA(q="Wo wird Jotti hergestellt?",
         a="In deutscher Manufakturqualität. Jotti steht für ehrliche, handwerklich gemachte Reinigung und Pflege."),
]


# Backend KWs — stem-deduped, DE, byte-packed. Avoid brand/title duplicates & superlatives.
BACKEND = (
    "polsterreiniger spray fleckenspray fleckenentferner sofareiniger couchreiniger "
    "ledersofa stoffsofa autositz autoinnenreiniger autopflege innenraum textilreiniger "
    "matratzenreiniger teppichreiniger teppichschaum polsterschaum schaumreiniger "
    "polsterstuhl polstermoebel textilerfrischer geruchsentferner flecken einarbeiten "
    "tiefenreinigung intensivreinigung spruehkopf rueckstandsfrei schonend haushalt "
    "auto reinigen frischen manufaktur deutsche"
)


def main() -> None:
    print("Loading Jotti customer + parsing Polsterreiniger Excel…")
    cust = load_customer("jotti")
    brief = parse_excel(EXCEL)
    OUT = HERE / f"{PLAN_NO}_Jotti_Polsterreiniger_Image Plan.pdf"
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
    builder.copy_source_label = "Hand-written senior copy (DE customer-facing, EN art-direction)"

    print("Building branded PDF…")
    pdf_path = builder.build()
    size_kb = pdf_path.stat().st_size // 1024
    import re
    pages = len(re.findall(rb'/Type\s*/Page[^s]', pdf_path.read_bytes()))
    print(f"Built: {pdf_path}")
    print(f"  Pages: {pages}  Size: {size_kb} KB")


if __name__ == "__main__":
    main()
