"""Jotti Putzstein 600 ml — universeller Reinigungsstein / Putzpaste — Image Plan 07
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
with the result the buyer wants — never the steps. Smooth German, no gimmicks,
no "·" middots in overlays. Hard limits (auto-linted on build):
  overlay ≤ 30 chars AND ≤ 5 words · overlay_sub ≤ 90 chars
  module headline ≤ 38 chars · bullet head <b>…</b> ≤ 45 chars · TITLE ≤ 200

Verified facts:
  - 600 ml universeller Putzstein / Reinigungsstein (auch als 200 ml erhältlich)
  - entfernt Kalk, Fett & eingetrocknete Flecken
  - für Spüle, Armaturen, Fliesen, Edelstahl, Keramik & abwaschbare Flächen
  - kraftvolle Reinigung OHNE aggressives Schrubben; schonend, keine Kratzer auf
    geeigneten Flächen; frischer Duft; deutsche Manufakturqualität

CRITICAL CORRECTION (listing USP is WRONG): KEIN Schwamm im Lieferumfang.
  Never claim an included sponge anywhere in this brief.

Compliance: no $/€ prices, no URL/.com, no beste/#1/garantiert, no medical/
prevention claims, no false claims (no sponge, no disinfect/antibacterial claim).
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
PLAN_NO = "07"


# ===== KW-led, marketing-optimized DE copy (customer-facing) =====

# Title is HTML-escaped, so literal "&" counts as 1 char. Keep ≤200 real chars. Stays German.
TITLE = (
    "Jotti Putzstein 600 ml — Universal-Reinigungsstein für Küche & Bad · entfernt Kalk, "
    "Fett & eingetrocknete Flecken · für Spüle, Armaturen, Fliesen, Edelstahl & Keramik · "
    "kraftvoll & schonend"
)

BULLETS = [
    "<b>ALLES BLITZT WIEDER</b> — Verkalkte Armaturen, matte Spülen und eingetrocknete "
    "Flecken verschwinden: Der Jotti Putzstein bringt Oberflächen im ganzen Haushalt "
    "sichtbar wieder zum Glänzen.",

    "<b>KALK, FETT &amp; FLECKEN – GELÖST</b> — Der Reinigungsstein löst hartnäckige "
    "Kalkrückstände, Fett und eingetrocknete Verschmutzungen zuverlässig – als kraftvoller "
    "Universalstein für Küche und Bad.",

    "<b>EIN STEIN FÜR ALLE FLÄCHEN</b> — Geeignet für Spüle, Armaturen, Fliesen, Edelstahl, "
    "Keramik und abwaschbare Flächen. Ein Allzweckreiniger als Stein – erhältlich als 600 ml "
    "und als praktische 200 ml.",

    "<b>KRAFTVOLL, ABER SCHONEND</b> — Kraftvolle Reinigung ohne aggressives Schrubben: Der "
    "Putzstein arbeitet den Schmutz heraus, ohne geeignete Oberflächen zu zerkratzen – so "
    "bleibt der Glanz erhalten.",

    "<b>FRISCHER DUFT, DEUTSCHE MANUFAKTUR</b> — Hinterlässt ein sauberes Ergebnis und einen "
    "frischen Duft. Als vielseitiger Schmutzradierer für den Haushalt – in deutscher "
    "Manufakturqualität.",
]


IMAGES = [
    AIImagePlanItem(
        name="Bild 1 — Main Hero (3 Optionen für A/B-Test)",
        role="hero",
        background="Clean, bright kitchen/bath backdrop in cream #EFE6D9 with soft side-light; a thin brushed-steel or aged-wood band in the bottom 15% for a manufactory feel. Identical backdrop across all 3 options for a clean split-test.",
        purpose="Win the click in the amazon.de cleaning-stone grid — stand out next to generic tubs of paste.",
        visual=(
            "Designer mocks up ALL 3 options. Brand picks the winner via Amazon Manage Your Experiments. "
            "Each option: ONE callout, ONE result cue, ONE prop — clean, never stacked. "
            "DO NOT show a sponge anywhere (not included with the product).\n\n"
            "▸ OPTION A — BEFORE/AFTER TRANSFORMATION (wins on proof)\n"
            "600 ml Putzstein tub centered (label legible, slight 3/4 turn, ~55% of frame). Behind it a "
            "chrome mixer tap split diagonally: left limescaled/matte, right mirror-bright. Sparkle cue on "
            "the clean side.\n"
            "CALLOUT top right: badge 'ALLES BLITZT WIEDER.' (brown #8B5A2B, white type).\n\n"
            "▸ OPTION B — POWER LIFT (wins on the cleaning-power promise)\n"
            "Tub left, the stone/paste visibly lifting limescale + grease off a stainless sink edge, a clean "
            "swipe track revealing shine.\n"
            "CALLOUT top left: 'KALK HAT KEINE CHANCE.' (dark #2F2A26, white type).\n\n"
            "▸ OPTION C — MULTI-SURFACE STACK (wins on versatility)\n"
            "Tub centered, 5 thin brown line icons radiating: sink · tap · tiles · stainless · ceramic.\n"
            "CALLOUT bottom right: 'EIN STEIN FÜR ALLES.' (brown #8B5A2B).\n\n"
            "All 3: tub dominant ~55%, callout ~6%, same light / same backdrop. No sponge in frame."
        ),
        overlay="ALLES BLITZT WIEDER.",
        overlay_sub="Kalk, Fett und eingetrocknete Flecken verschwinden – ein Stein für alles.",
        props=[
            "OPTION A: tub + split chrome tap (limescaled/mirror-bright) + sparkle cue + badge",
            "OPTION B: tub + stone lifting limescale & grease off a stainless sink + clean swipe track",
            "OPTION C: tub + 5 surface icons (sink/tap/tiles/stainless/ceramic) + badge",
        ],
        lighting="Bright, clean daylight from camera-right (4500–5000K), a crisp rim on the clean surfaces so the shine reads instantly. Same light across all 3 options.",
        why_it_works=(
            "Three triggers against three buyer motives: A delivers the before/after proof (limescale is the "
            "#1 pain), B proves raw cleaning power, C shows versatility. One callout, one result cue, one prop "
            "— readable on a mobile thumbnail. No sponge shown — the product does not include one."
        ),
        ctr="The limescaled→mirror-bright tap plus 'ALLES BLITZT WIEDER.' beats competitors' plain paste tubs in the DE grid; the visible shine is the strongest click promise for sinks, taps and tiles.",
        cvr="Instant clarity on product type (Putzstein/paste), job (removes limescale, grease, stains) and result (surfaces shine) cuts bounce; the manufactory band builds purchase trust.",
    ),
    AIImagePlanItem(
        name="Bild 2 — Hook: Kalk & Fett lösen sich",
        role="hook",
        background="Cream #EFE6D9, brushed steel accent, bright even side-light.",
        purpose="Show the raw lifting power on the hardest soils — limescale and grease — in one frame.",
        visual=(
            "Tight macro of a limescaled chrome tap / stainless sink edge. A single clean swipe track cuts "
            "across the frame, revealing mirror shine underneath; the lifted limescale + grease film visible "
            "at the edge of the track. Putzstein tub anchored bottom-left corner. NO sponge — show only the "
            "clean result and the stone/paste. Small caption strip at the bottom: 'löst Kalk & Fett'."
        ),
        overlay="KALK HAT KEINE CHANCE.",
        overlay_sub="Der Putzstein löst Kalkrückstände und Fett – ohne aggressives Schrubben.",
        props=["limescaled chrome tap / stainless sink", "clean swipe track revealing shine", "Jotti Putzstein tub", "caption strip"],
        lighting="Bright directional daylight, crisp specular highlight on the revealed shine.",
        why_it_works=(
            "Limescale and grease are the category's defining problems. A single reveal swipe proves the "
            "product does the hard part, answering 'does it actually work?' in one glance — without implying "
            "any bundled sponge."
        ),
        ctr="The dramatic dirty→mirror-bright reveal hits the exact frustration of the DE buyer fighting limescale on taps and sinks.",
        cvr="Removes the effort worry ('do I have to scrub forever?') and proves the stone lifts limescale and grease on its own.",
    ),
    AIImagePlanItem(
        name="Bild 3 — Educate: Ein Stein für alle Flächen",
        role="educate",
        background="White with a brown accent band (#8B5A2B) in the footer.",
        purpose="Explain the multi-surface versatility that makes it a true universal cleaner.",
        visual=(
            "Headline at top, then a clean 5-tile surface grid with line icons + one real micro-scene each:\n"
            "  • SPÜLE — sink basin\n"
            "  • ARMATUREN — chrome tap\n"
            "  • FLIESEN — bathroom tiles\n"
            "  • EDELSTAHL — stainless hob/surface\n"
            "  • KERAMIK — ceramic wash-basin\n"
            "Putzstein tub anchored center or right. Footer band (brown) carries the supporting line: "
            "'auch für abwaschbare Flächen im Haushalt'. No sponge in any tile."
        ),
        overlay="EIN STEIN FÜR ALLES.",
        overlay_sub="Spüle, Armaturen, Fliesen, Edelstahl und Keramik – ein Universalstein.",
        props=["5 surface tiles with icons (sink/tap/tiles/stainless/ceramic)", "Jotti Putzstein tub", "footer band"],
        lighting="Flat, clean studio light — legibility over atmosphere.",
        why_it_works=(
            "Makes 'universal' concrete: buyers filtering for a specific surface (Edelstahl, Fliesen, Keramik) "
            "see their exact use case, which widens relevance and justifies one purchase for the whole home."
        ),
        ctr="Surface names (Edelstahl, Fliesen, Keramik) are strong DE search signals; the grid captures several intents at once.",
        cvr="One product for every hard surface raises perceived value and removes the 'will it work on mine?' doubt.",
    ),
    AIImagePlanItem(
        name="Bild 4 — Desire: Before/After Armatur & Spüle",
        role="desire",
        background="Bright modern kitchen/bath, clean daylight.",
        purpose="Sell the visible result — dull, limescaled fittings become mirror-bright again.",
        visual=(
            "Large before/after split of a real chrome mixer tap and sink corner. "
            "LEFT: limescaled, matte, water-spotted, dull. RIGHT: streak-free, mirror-bright, reflective. "
            "Divider centered; Putzstein tub small in the foreground corner. A subtle sparkle accent on the "
            "clean side. No sponge — result-only staging."
        ),
        overlay="SPIEGELBLANK IN MINUTEN.",
        overlay_sub="Verkalkte, matte Armaturen und Spülen werden wieder streifenfrei glänzend.",
        props=["chrome tap + sink corner (before/after split)", "Jotti Putzstein tub (foreground)", "sparkle accent"],
        lighting="Bright daylight from camera-right, crisp rim on the mirror-bright side so the shine pops.",
        why_it_works=(
            "The dull→mirror-bright transformation is the most desirable, universally understood proof in the "
            "cleaning category — and it is honest to the product's real job."
        ),
        ctr="The streak-free shine result is instantly desirable to anyone battling limescale on taps and sinks.",
        cvr="Visual proof instead of a promise; sets a realistic, achievable expectation and drives the purchase.",
    ),
    AIImagePlanItem(
        name="Bild 5 — Trust: Kraftvoll, aber schonend (keine Kratzer)",
        role="trust",
        background="White with cream panels.",
        purpose="Defuse the key objection — 'is it abrasive / will it scratch my surfaces?'",
        visual=(
            "Two-part reassurance. LEFT: a macro of a cleaned stainless surface with NO scratch marks, a "
            "small loupe/zoom callout on the flawless finish. RIGHT: 3-step application as an icon row:\n"
            "  1. AUFTRAGEN (stone/paste + a little water)\n"
            "  2. EINARBEITEN (light circular motion, soft-cloth icon)\n"
            "  3. ABSPÜLEN / NACHWISCHEN (rinse / wipe icon)\n"
            "Badge 'SCHONEND ZUR FLÄCHE'. Putzstein tub anchored right. Note the cloth is the USER's own — "
            "do NOT depict or label an included sponge."
        ),
        overlay="KRAFTVOLL, ABER SCHONEND.",
        overlay_sub="Kraftvoll gegen Schmutz, schonend zur Fläche – keine Kratzer auf geeignetem Material.",
        props=["macro of scratch-free stainless finish", "loupe/zoom callout", "3 application icons", "badge 'SCHONEND ZUR FLÄCHE'", "Jotti Putzstein tub"],
        lighting="Clean even studio light — icons and the flawless finish readable on the thumbnail.",
        why_it_works=(
            "The single biggest hesitation with any cleaning stone is scratching. Showing a scratch-free "
            "finish plus a gentle 3-step method pre-defuses the objection and lowers returns — while a "
            "surface-suitability caveat keeps the claim honest."
        ),
        ctr="The 'powerful yet gentle' promise attracts careful DE buyers who fear abrasives on chrome and stainless.",
        cvr="Defuses the top purchase objection (scratching) right on the image, before the buyer even scans reviews.",
    ),
    AIImagePlanItem(
        name="Bild 6 — Desire: Multi-Surface-Grid (Küche & Bad)",
        role="desire",
        background="Cream #EFE6D9, bright side-light.",
        purpose="Show real household use across the whole home — one stone, many rooms.",
        visual=(
            "Clean 4-up grid of real scenes: kitchen sink & tap · bathroom tiles · stainless hob/surface · "
            "ceramic wash-basin. Each tile with a subtle sparkle/clean cue. Putzstein tub anchored center or "
            "bottom. Small label per tile (Spüle · Bad · Edelstahl · Keramik). No sponge in any scene."
        ),
        overlay="SPÜLE, BAD, EDELSTAHL.",
        overlay_sub="Ein Schmutzradierer für Küche, Bad und abwaschbare Flächen im ganzen Haushalt.",
        props=["4 use scenes (sink/tiles/stainless/ceramic)", "Jotti Putzstein tub", "sparkle/clean cues"],
        lighting="Bright side-light, consistent across all 4 tiles.",
        why_it_works=(
            "Expands perceived value: one tub covers kitchen and bath. Hits the cost-per-use math and matches "
            "broad DE search terms (Küche, Bad, Edelstahl, Keramik)."
        ),
        ctr="Speaks to several search intents at once (Küchenreiniger, Badreiniger, Edelstahlreiniger) and maximizes grid relevance.",
        cvr="More rooms and surfaces = higher perceived value per tub, which makes the purchase easier to justify.",
    ),
    AIImagePlanItem(
        name="Bild 7 — Close: Deutsche Manufaktur",
        role="close",
        background="Warm, tidy workspace: clean surfaces, aged wood, brass, linen, soft side-light.",
        purpose="Close on brand identity — honest, artisanal manufactory quality with a fresh finish.",
        visual=(
            "Mid-range hero of the Putzstein tub (label legible) on a clean surface, a freshly polished tap "
            "and a small linen cloth beside it, a subtle fresh/citrus scent cue (a sprig or soft haze). "
            "Soft-focused manufactory setting (brass, linen). A small handwritten note card carries the "
            "manufactory line. No sponge on set."
        ),
        overlay="DEUTSCHE MANUFAKTUR.",
        overlay_sub="Frischer Duft, kraftvolle Reinigung – Haushaltspflege aus deutscher Manufaktur.",
        props=["Jotti Putzstein tub", "freshly polished tap", "linen cloth (user's own)", "fresh-scent cue", "aged wood / brass / linen", "handwritten note card"],
        lighting="Warm workshop side-light from camera-right, golden and lived-in — not staged.",
        why_it_works=(
            "Closes on the brand promise that matters before checkout: honest, artisanal manufactory quality "
            "and a fresh, clean finish — differentiating from anonymous supermarket paste."
        ),
        ctr="The 'German manufactory' signal separates Jotti from generic import cleaners and attracts quality-conscious DE buyers.",
        cvr="Provenance, craft and a fresh finish create the final trust that seals the purchase.",
    ),
]


MODULES = [
    AIModule(
        name="Modul 1 — Brand-Banner",
        role="a+_banner",
        headline="ALLES BLITZT WIEDER.",
        body=(
            "Der Jotti Putzstein entfernt Kalk, Fett und eingetrocknete Flecken und bringt Spüle, "
            "Armaturen und Fliesen wieder zum Glänzen – kraftvoll, aber schonend, aus deutscher "
            "Manufaktur."
        ),
        visual="Wide bright banner: clean kitchen/bath surfaces, a mirror-bright tap, Jotti Putzstein tub front-center. Logo top left in brown #8B5A2B. No sponge in frame.",
        alt="Jotti Putzstein 600 ml vor blitzsauberer Spüle und glänzender Armatur in hellem Licht.",
    ),
    AIModule(
        name="Modul 2 — Carousel (4 Kacheln): Der Jotti-Vorteil",
        role="a+_carousel",
        headline="DER JOTTI-VORTEIL",
        body=(
            "Kachel 1: <b>KALK &amp; FETT WEG</b> — löst Kalkrückstände, Fett &amp; eingetrocknete Flecken.<br/>"
            "Kachel 2: <b>UNIVERSAL</b> — Spüle, Armaturen, Fliesen, Edelstahl &amp; Keramik.<br/>"
            "Kachel 3: <b>SCHONEND</b> — kraftvoll ohne aggressives Schrubben, keine Kratzer auf geeigneten Flächen.<br/>"
            "Kachel 4: <b>FRISCHER DUFT</b> — sauberes Ergebnis, frischer Duft, deutsche Manufaktur."
        ),
        visual="4 square tiles, brown accent corner per tile, small line icons (droplet+sparkle · surface grid · shield · fresh sprig). No sponge shown.",
        alt="Vier-Kachel A+ Carousel mit den Jotti-Vorteilen: Kalk & Fett weg, universal, schonend, frischer Duft.",
    ),
    AIModule(
        name="Modul 3 — Banner: Reinigungskraft",
        role="a+_banner",
        headline="KALK HAT KEINE CHANCE.",
        body=(
            "Der Putzstein löst hartnäckige Kalkrückstände, Fett und eingetrocknete Verschmutzungen "
            "zuverlässig – auch dort, wo normale Reiniger aufgeben. Einfach anfeuchten, auftragen, "
            "einarbeiten und nachwischen."
        ),
        visual="Wide banner: macro reveal swipe on a limescaled tap turning mirror-bright, tub alongside. Bright daylight. No sponge — the swipe track and clean shine tell the story.",
        alt="A+ Banner: verkalkte Armatur wird mit dem Jotti Putzstein wieder spiegelblank.",
    ),
    AIModule(
        name="Modul 4 — Banner: Kraftvoll, aber schonend",
        role="a+_banner",
        headline="KRAFTVOLL, ABER SCHONEND.",
        body=(
            "Kraftvolle Reinigung ohne aggressives Schrubben: Der Putzstein arbeitet den Schmutz heraus "
            "und ist dabei schonend zur Oberfläche – keine Kratzer auf geeigneten Flächen wie Edelstahl, "
            "Fliesen und Keramik. Auf empfindlichen Materialien vorab an unauffälliger Stelle testen."
        ),
        visual="Triptych: LEFT dirty/limescaled surface (before), CENTER application moment (stone/paste + light circular motion), RIGHT scratch-free mirror-bright finish (after). Bright light throughout. No sponge.",
        alt="A+ Triptychon-Banner: Fläche vorher verschmutzt, Anwendung, nachher glänzend und kratzerfrei.",
    ),
    AIModule(
        name="Modul 5 — Carousel (4 Kacheln): Für Küche & Bad",
        role="a+_carousel",
        headline="EIN STEIN FÜR ALLES.",
        body=(
            "Kachel 1: <b>SPÜLE &amp; ARMATUREN</b> — löst Kalk und bringt Chrom zum Glänzen.<br/>"
            "Kachel 2: <b>FLIESEN &amp; BAD</b> — entfernt Schmutzränder und Ablagerungen.<br/>"
            "Kachel 3: <b>EDELSTAHL</b> — Kochfeld, Töpfe &amp; Flächen streifenfrei sauber.<br/>"
            "Kachel 4: <b>KERAMIK &amp; MEHR</b> — für viele abwaschbare Flächen im Haushalt."
        ),
        visual="4 identically composed real-surface tiles (sink/tap · tiles · stainless · ceramic), brown accent corner per tile, consistent bright light. No sponge in any tile.",
        alt="Vier-Kachel A+ Carousel der Flächen: Spüle & Armaturen, Fliesen & Bad, Edelstahl, Keramik.",
    ),
    AIModule(
        name="Modul 6 — Premium Q&A",
        role="a+_qa",
        headline="HÄUFIGE FRAGEN",
        body=(
            "<b>F.</b> Zerkratzt der Putzstein die Oberfläche?<br/>"
            "<b>A.</b> Bei richtiger Anwendung reinigt er kraftvoll, aber schonend – ohne Kratzer auf "
            "geeigneten Flächen. Empfindliche Materialien vorab an unauffälliger Stelle testen.<br/><br/>"
            "<b>F.</b> Für welche Flächen ist er geeignet?<br/>"
            "<b>A.</b> Für Spüle, Armaturen, Fliesen, Edelstahl, Keramik und viele abwaschbare Flächen "
            "in Küche und Bad.<br/><br/>"
            "<b>F.</b> Ist ein Schwamm enthalten?<br/>"
            "<b>A.</b> Geliefert wird der Putzstein selbst. Zum Auftragen genügen ein feuchtes Tuch oder "
            "ein Schwamm aus dem Haushalt.<br/><br/>"
            "<b>F.</b> Wie wende ich ihn an?<br/>"
            "<b>A.</b> Stein bzw. Paste anfeuchten, dünn auftragen, einarbeiten und mit klarem Wasser "
            "nachwischen. Bei hartnäckigen Stellen wiederholen.<br/><br/>"
            "<b>F.</b> Welche Größen gibt es?<br/>"
            "<b>A.</b> Erhältlich als 600 ml und als praktische 200 ml – aus deutscher Manufakturqualität."
        ),
        visual="Vertical Q/A table, brown dividers between questions, small F./A. labels in dark #2F2A26.",
        alt="Premium Q&A Modul mit den häufigsten Fragen zum Jotti Putzstein.",
    ),
    AIModule(
        name="Modul 7 — Premium Comparison Chart",
        role="a+_comparison",
        headline="WARUM JOTTI",
        body=(
            "Vergleich über 4 Spalten: <b>Jotti Putzstein</b> · Scheuermilch · Kalkentferner-Spray · "
            "Allzweckreiniger (flüssig).<br/><br/>"
            "Zeilen: entfernt Kalk · löst Fett &amp; eingetrocknete Flecken · für viele Flächen "
            "(Spüle/Armaturen/Fliesen/Edelstahl/Keramik) · ohne aggressives Schrubben · schonend "
            "(keine Kratzer auf geeigneten Flächen) · frischer Duft · deutsche Manufaktur.<br/><br/>"
            "Jotti-Spalte mit dezentem Braun-Ton hervorheben."
        ),
        visual="Standard Amazon Premium Comparison Chart, 4 product columns. Competitors named by category only, no brand names. Brown header row.",
        alt="Premium Vergleichstabelle: Jotti Putzstein vs. Scheuermilch, Kalkentferner-Spray und flüssiger Allzweckreiniger.",
    ),
]


QA = [
    AIQA(q="Zerkratzt der Putzstein die Oberfläche?",
         a="Bei richtiger Anwendung reinigt der Putzstein kraftvoll, aber schonend und hinterlässt keine Kratzer auf geeigneten Flächen wie Edelstahl, Fliesen oder Keramik. Empfindliche oder hochglänzende Materialien vorab an einer unauffälligen Stelle testen."),
    AIQA(q="Für welche Flächen ist der Putzstein geeignet?",
         a="Für Spüle, Armaturen, Fliesen, Edelstahl, Keramik und viele weitere abwaschbare Flächen in Küche und Bad. Als Universalstein ist er vielseitig im ganzen Haushalt einsetzbar."),
    AIQA(q="Ist ein Schwamm im Lieferumfang enthalten?",
         a="Geliefert wird der Jotti Putzstein selbst. Zum Auftragen genügen ein feuchtes Tuch oder ein Schwamm aus Ihrem Haushalt – so haben Sie die Anwendung ganz in der Hand."),
    AIQA(q="Wie wird der Putzstein angewendet?",
         a="Den Stein bzw. die Paste anfeuchten, dünn auf die Fläche auftragen, mit Tuch oder Schwamm einarbeiten und anschließend mit klarem Wasser nachwischen. Bei hartnäckigen Verschmutzungen den Vorgang wiederholen."),
    AIQA(q="Entfernt der Putzstein wirklich Kalk und Fett?",
         a="Ja. Der Reinigungsstein löst Kalkrückstände, Fett und eingetrocknete Flecken und bringt matte, verkalkte Oberflächen wie Armaturen und Spülen wieder zum Glänzen – ohne aggressives Schrubben."),
    AIQA(q="Riecht der Putzstein unangenehm?",
         a="Nein. Der Putzstein hat einen frischen Duft und hinterlässt nach dem Nachwischen ein sauberes, angenehmes Ergebnis."),
    AIQA(q="Welche Größen gibt es und wo wird Jotti hergestellt?",
         a="Der Putzstein ist als 600 ml und als praktische 200 ml erhältlich. Jotti steht für Haushaltspflege in deutscher Manufakturqualität."),
]


# Backend KWs — German, stem-deduped. Avoid title duplicates, superlatives, and 'schwamm'
# (no sponge is included — do not bid the product into sponge searches).
BACKEND = (
    "universalstein schmutzradierer allzweckreiniger universalreiniger putzpaste "
    "reinigungspaste haushaltsreiniger badreiniger kuechenreiniger kalkentferner fettloeser "
    "waschbecken spuelbecken oberflaechen streifenfrei glaenzend abwaschbar milder "
    "putzmittel scheuermilch alternative frischer duft chrom sanitaer"
)


def main() -> None:
    print("Loading Jotti customer + parsing Putzstein Excel…")
    cust = load_customer("jotti")
    brief = parse_excel(EXCEL)
    OUT = HERE / f"{PLAN_NO}_Jotti_Putzstein_Image Plan.pdf"
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
    builder.copy_source_label = "Hand-written senior copy (DE, conversion)"

    print("Building branded PDF…")
    pdf_path = builder.build()
    size_kb = pdf_path.stat().st_size // 1024
    import re
    pages = len(re.findall(rb'/Type\s*/Page[^s]', pdf_path.read_bytes()))
    print(f"Built: {pdf_path}")
    print(f"  Pages: {pages}  Size: {size_kb} KB")


if __name__ == "__main__":
    main()
