"""Jotti Imprägnierspray-Serie (06) — ONE document, 6 product-specific image plans + ONE shared A+.
Marketplace amazon.de. Same premium formula (silikonfrei, farbneutral, atmungsaktiv, Langzeit,
wasser- & schmutzabweisend, 500 ml), positioned per target surface.

LANGUAGE SPLIT: art-direction fields ENGLISH (designer-facing); customer text (overlay,
overlay_sub, module headline/body, QA) GERMAN. Overlays: outcome-led, ≤30 chars & ≤5 words, smooth.
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

EXCEL = HERE / "listing.xlsx"   # base (universal) — for brand context
OUT = HERE / "06_Jotti_Impraegnierspray_Serie_Image Plan.pdf"

# Shared overlays (identical across surfaces) — German, outcome-led, within limits.
OV_HOOK = "WASSER PERLT AB."
OV_EDU = "FARBNEUTRAL & ATMUNGSAKTIV."
OV_TRUST = "SILIKONFREI. LANGZEITSCHUTZ."
OV_CLOSE = "DEUTSCHE MANUFAKTUR."

# Per-surface positioning. label=section title; the rest feed the 7-image template.
SURFACES = [
    {
        "key": "universal", "label": "Image-Plan — Imprägnierspray Universal",
        "hero_ov": "ALLES BLEIBT TROCKEN.",
        "hero_sub": "Silikonfreier Langzeitschutz für Textil, Leder, Schuhe &amp; mehr.",
        "surface_en": "a mixed group — a textile jacket, a leather shoe and an outdoor fabric",
        "use_ov": "EIN SPRAY FÜR ALLES.",
        "use_sub": "Universeller Nässeschutz für fast jede Oberfläche.",
        "use_scene_en": "a hallway drop-zone: jackets on hooks, shoes on a rack, a bag — one bottle protects them all",
        "vers_ov": "TEXTIL, LEDER & SCHUHE.",
        "vers_list_en": "Textilien, Glattleder, Schuhe, Taschen, Outdoor-Stoffe",
        "kw": "imprägnierspray, imprägnierspray universal, imprägnierspray textil, imprägnierspray leder",
    },
    {
        "key": "textilien", "label": "Image-Plan — Imprägnierspray Textilien",
        "hero_ov": "REGEN PERLT EINFACH AB.",
        "hero_sub": "Silikonfreier Nässeschutz für Jacken, Markisen &amp; Outdoor-Textilien.",
        "surface_en": "a technical rain jacket / outdoor textile",
        "use_ov": "TROCKEN DURCH JEDES WETTER.",
        "use_sub": "Für Regenjacke, Markise, Rucksack &amp; Outdoor-Kleidung.",
        "use_scene_en": "a person in a rain jacket in light rain, water beading and rolling off the shoulders",
        "vers_ov": "JACKEN, MARKISEN, OUTDOOR.",
        "vers_list_en": "Regenjacken, Markisen, Rucksäcke, Zelte, Outdoor-Kleidung",
        "kw": "imprägnierspray textil, imprägnierspray outdoor, imprägnierspray jacke",
    },
    {
        "key": "wildleder", "label": "Image-Plan — Imprägnierspray Wildleder",
        "hero_ov": "WILDLEDER BLEIBT SCHÖN.",
        "hero_sub": "Silikonfreier, farbneutraler Schutz für Wildleder, Nubuk &amp; Velours.",
        "surface_en": "a pair of suede/nubuck boots (soft matte nap clearly visible)",
        "use_ov": "KEIN FLECK AUF WILDLEDER.",
        "use_sub": "Schützt empfindliches Wildleder vor Nässe &amp; Flecken.",
        "use_scene_en": "a water droplet beading on a suede boot's nap; a hand brushing suede, matte texture intact",
        "vers_ov": "WILDLEDER, NUBUK, VELOURS.",
        "vers_list_en": "Wildleder, Nubuk, Veloursleder — Schuhe, Taschen, Jacken",
        "kw": "imprägnierspray wildleder, wildleder imprägnierspray, nubuk imprägnierspray",
    },
    {
        "key": "schuhe", "label": "Image-Plan — Imprägnierspray Schuhe",
        "hero_ov": "SCHUHE BLEIBEN TROCKEN.",
        "hero_sub": "Silikonfreier Nässeschutz für Sneaker, Leder- &amp; Textilschuhe.",
        "surface_en": "a clean pair of sneakers + a leather shoe beside them",
        "use_ov": "TROCKENE FÜSSE, JEDER TAG.",
        "use_sub": "Für Sneaker, Lederschuhe, Textilschuhe &amp; Stiefel.",
        "use_scene_en": "sneakers stepping through a puddle on a rainy street, water beading off the toe",
        "vers_ov": "SNEAKER, LEDER, TEXTIL.",
        "vers_list_en": "Sneaker, Glattleder, Textilschuhe, Stiefel",
        "kw": "imprägnierspray schuhe, schuhe imprägnieren, sneaker imprägnierspray",
    },
    {
        "key": "zelt", "label": "Image-Plan — Imprägnierspray Zelt",
        "hero_ov": "DAS ZELT HÄLT DICHT.",
        "hero_sub": "Silikonfreier Nässeschutz für Zelt, Plane &amp; Outdoor-Ausrüstung.",
        "surface_en": "a pitched camping tent (technical outdoor fabric)",
        "use_ov": "TROCKEN CAMPEN BEI REGEN.",
        "use_sub": "Frischt den Nässeschutz von Zelt &amp; Plane wieder auf.",
        "use_scene_en": "rain on a tent at a campsite, water beading and running off the flysheet, dry inside",
        "vers_ov": "ZELT, PLANE, AUSRÜSTUNG.",
        "vers_list_en": "Zelte, Planen, Tarps, Outdoor-Ausrüstung",
        "kw": "imprägnierspray zelt, zelt imprägnieren, imprägnierspray outdoor",
    },
    {
        "key": "cabrio", "label": "Image-Plan — Imprägnierspray Cabrio-Verdeck",
        "hero_ov": "VERDECK BLEIBT DICHT.",
        "hero_sub": "Silikonfreier, farbneutraler Nässeschutz fürs Cabrio-Stoffverdeck.",
        "surface_en": "a convertible car's fabric soft-top (textured cloth roof)",
        "use_ov": "CABRIO-VERDECK GESCHÜTZT.",
        "use_sub": "Schützt das Stoffverdeck vor Nässe, Schmutz &amp; Verblassen.",
        "use_scene_en": "rain beading on a convertible fabric top; the car parked, roof up, water rolling off",
        "vers_ov": "STOFF- & TEXTILVERDECKE.",
        "vers_list_en": "Cabrio-Stoffverdecke, Textilverdecke",
        "kw": "imprägnierspray cabrio, cabrio verdeck imprägnieren, verdeck imprägnierspray",
    },
]


def make_images(s: dict) -> list:
    """The shared 7-image template, surface-swapped. Art-direction English, overlays German."""
    br = "Jotti brand: warm, honest, craftsman; brown #8B5A2B + dark #2F2A26 accents; the 500 ml Jotti spray bottle as the anchor."
    return [
        AIImagePlanItem(
            name="Bild 1 — Main Hero (3 A/B-Optionen)",
            role="hero",
            background="Clean, bright studio with a soft cool grey backdrop; same across all 3 options for a clean split-test.",
            purpose=f"Win the click in the amazon.de Imprägnierspray grid for {s['key']} — instantly signal WHAT surface this protects.",
            visual=(
                f"Mock ALL 3 options; brand picks the winner. Each: ONE callout, ONE action cue, ONE prop.\n"
                f"▸ OPTION A — RESULT: the 500 ml Jotti bottle beside {s['surface_en']}, with visible water beads sitting on the surface (protected). Callout top-right badge (brown #8B5A2B): the German hero line.\n"
                f"▸ OPTION B — ACTION: a hand sprays a fine even mist onto {s['surface_en']}; light catches the mist. Callout: 'SILIKONFREI'.\n"
                f"▸ OPTION C — BEFORE/AFTER: {s['surface_en']} split — left absorbs a dark water stain, right beads the water off. Callout: 'WASSER PERLT AB'.\n"
                f"All 3: bottle + surface dominant ~65%, callout ~6%, identical light. {br}"
            ),
            overlay=s["hero_ov"], overlay_sub=s["hero_sub"],
            props=[f"Jotti 500 ml bottle", s["surface_en"], "visible water beads", "brown callout badge"],
            lighting="Bright, clean side-light; small speculars on the water beads so 'beading' reads instantly.",
            why_it_works=f"Leads with the exact outcome the {s['key']} buyer wants (stays dry/protected) and names the surface, so the right shopper self-selects in the grid.",
            ctr=f"The water-beading proof on {s['key']} plus the surface-specific German line out-reads generic 'Imprägnierspray' bottles in the DE grid.",
            cvr=f"Instant clarity on surface fit + the silikonfrei/farbneutral reassurance cuts the 'is this right for my {s['key']}?' hesitation.",
        ),
        AIImagePlanItem(
            name="Bild 2 — Hook: Abperl-Effekt",
            role="hook",
            background="Macro studio, cool grey.",
            purpose="Prove the effect in one glance — water beads and rolls off, it doesn't soak in.",
            visual=f"Extreme macro of water droplets beading on {s['surface_en']} after treatment; one droplet mid-roll. Small caption strip: 'wasser- & schmutzabweisend'.",
            overlay=OV_HOOK, overlay_sub="Nässe &amp; Schmutz perlen ab, statt einzuziehen.",
            props=["macro water droplets", s["surface_en"], "caption strip"],
            lighting="Hard raking light for crisp droplet speculars.",
            why_it_works="The beading macro is the single most persuasive proof for any impregnation spray.",
            ctr="A crisp beading macro is a scroll-stopper on mobile.", cvr="Visually guarantees the core benefit before the buyer reads a word.",
        ),
        AIImagePlanItem(
            name="Bild 3 — Educate: silikonfrei, farbneutral, atmungsaktiv",
            role="educate",
            background="White with a soft brown ribbon footer.",
            purpose="Defend the premium: it protects WITHOUT changing look or breathability.",
            visual="Three clean icon columns: (1) SILIKONFREI — no silicone build-up; (2) FARBNEUTRAL — colour & look unchanged; (3) ATMUNGSAKTIV — material still breathes. Small footer: 'Langzeit-Imprägnierschutz'.",
            overlay=OV_EDU, overlay_sub="Schützt, ohne Farbe, Optik oder Atmungsaktivität zu verändern.",
            props=["3 icon columns", "brown footer ribbon"],
            lighting="Flat clean studio — readability first.",
            why_it_works="Silicone-free + colour-neutral + breathable is exactly what quality-conscious DE buyers filter for (silicone dulls and clogs).",
            ctr="Lower-funnel; holds the comparison shopper.", cvr="Removes the two big fears — discolouration and clogging — that kill sprays.",
        ),
        AIImagePlanItem(
            name="Bild 4 — Lifestyle: der Einsatz",
            role="desire",
            background=f"Real {s['key']} use-case scene, natural light.",
            purpose="Put the buyer in the moment the protection pays off.",
            visual=f"{s['use_scene_en']}. Warm, real, believable — not staged. Small brand mark bottom corner.",
            overlay=s["use_ov"], overlay_sub=s["use_sub"],
            props=[s["surface_en"], "rain / water in action"],
            lighting="Natural outdoor/daylight; visible water for the beading story.",
            why_it_works=f"Owns the {s['key']} buyer's real rainy-day scenario — the emotional reason to buy.",
            ctr="Human, weather-in-action scene stands out against product-only competitor tiles.",
            cvr=f"The buyer pictures their own {s['key']} staying dry — the decisive conversion beat.",
        ),
        AIImagePlanItem(
            name="Bild 5 — Trust: silikonfrei & Langzeit",
            role="trust",
            background="White with soft brown panels.",
            purpose="Stack the reasons to trust: silicone-free, colour-neutral, long-lasting, 500 ml.",
            visual="Centered Jotti 500 ml bottle with 4 badges: SILIKONFREI · FARBNEUTRAL · LANGZEIT-SCHUTZ · 500 ML ERGIEBIG. Thin strip: 'wasser- & schmutzabweisend'.",
            overlay=OV_TRUST, overlay_sub="Silikonfreie Premium-Rezeptur mit langanhaltendem Schutz.",
            props=["Jotti 500 ml bottle", "4 badges", "supporting strip"],
            lighting="Studio even light, catch-light on the bottle.",
            why_it_works="Bundles the credentials a careful DE buyer scans for before committing.",
            ctr="Badge frame earns the secondary click from a comparing buyer.", cvr="Closes the legitimacy gap right before add-to-cart.",
        ),
        AIImagePlanItem(
            name="Bild 6 — Vielseitigkeit (innerhalb der Oberfläche)",
            role="desire",
            background="Soft grey, flat-lay.",
            purpose="Show the range this specific spray covers within its surface family.",
            visual=f"Flat-lay showing the items this variant is for: {s['vers_list_en']} — each with a small water-bead cue. Clean grid.",
            overlay=s["vers_ov"], overlay_sub=f"Geeignet für: {s['vers_list_en']}.",
            props=[s["vers_list_en"]],
            lighting="Even soft top light.",
            why_it_works=f"Widens perceived value within the {s['key']} use-case without confusing it with the other variants.",
            ctr="Not a click-driver; deepens the scroll.", cvr="Answers 'can I also use it on…?' within this surface family.",
        ),
        AIImagePlanItem(
            name="Bild 7 — Marken-Close",
            role="close",
            background="Warm workshop / brand scene.",
            purpose="Close on the Jotti brand promise — honest, handcrafted care.",
            visual="Warm brand scene: the Jotti spray bottle on a workbench, soft daylight, a subtle handwritten-style note. Brand mark clear. Consistent with the other Jotti plans' close.",
            overlay=OV_CLOSE, overlay_sub="Silikonfreier Premium-Schutz – handwerklich gemacht.",
            props=["Jotti bottle", "workbench", "brand mark"],
            lighting="Warm daylight, honest and lived-in.",
            why_it_works="Ends on brand trust — the reassurance that converts the hesitating buyer.",
            ctr="Final-position brand recall.", cvr="Turns brand trust into the purchase.",
        ),
    ]


# ONE shared A+ Premium for the whole line (same formula) — incl. the RANGE clarity module.
SHARED_MODULES = [
    AIModule(
        name="Modul 1 — Marken-Banner",
        role="a+_banner",
        headline="SILIKONFREIER PREMIUM-SCHUTZ.",
        body=("Die Jotti Imprägnierspray-Serie schützt Ihre Lieblingsstücke zuverlässig vor Nässe und "
              "Schmutz – silikonfrei, farbneutral und atmungsaktiv. Eine Premium-Rezeptur, sechs "
              "Varianten für genau Ihre Oberfläche. Handwerkliche Qualität aus deutscher Manufaktur."),
        visual="Wide brand banner: the Jotti spray bottles lined up, water beading on a textile in the foreground, warm daylight, brown accent ribbon.",
        alt="Marken-Banner der Jotti Imprägnierspray-Serie mit Abperl-Effekt.",
    ),
    AIModule(
        name="Modul 2 — Carousel: Der Unterschied",
        role="a+_carousel",
        headline="DER JOTTI-UNTERSCHIED",
        body=("Kachel 1: <b>SILIKONFREI</b> – kein Verkleben, keine Rückstände.<br/>"
              "Kachel 2: <b>FARBNEUTRAL</b> – Farbe und Optik bleiben unverändert.<br/>"
              "Kachel 3: <b>ATMUNGSAKTIV</b> – das Material atmet weiter.<br/>"
              "Kachel 4: <b>LANGZEIT-SCHUTZ</b> – wasser- &amp; schmutzabweisend.<br/>"
              "Kachel 5: <b>500 ML ERGIEBIG</b> – reicht für viele Anwendungen."),
        visual="5 square tiles, brown accent corner each, small icons (Tropfen, Farbpalette, Atmung, Uhr, Sprühdose).",
        alt="Fünf-Kachel-Carousel: silikonfrei, farbneutral, atmungsaktiv, Langzeitschutz, ergiebig.",
    ),
    AIModule(
        name="Modul 3 — Banner: So einfach geht's",
        role="a+_banner",
        headline="SPRÜHEN. TROCKNEN. GESCHÜTZT.",
        body=("Gleichmäßig aufsprühen, trocknen lassen – fertig. Der unsichtbare Schutzfilm lässt Nässe "
              "und Schmutz einfach abperlen, ohne die Optik zu verändern. Bei Bedarf einfach wieder auffrischen."),
        visual="Three-step horizontal banner: 1 spray mist onto a surface, 2 drying (clock), 3 water beading off. Brown accent ribbon at the foot.",
        alt="Drei-Schritt-Anleitung: aufsprühen, trocknen, geschützt.",
    ),
    AIModule(
        name="Modul 4 — Banner: Schützt, ohne zu verändern",
        role="a+_banner",
        headline="SCHUTZ, DER NICHTS VERÄNDERT.",
        body=("Silikonhaltige Sprays können Materialien verkleben, abdunkeln und die Atmungsaktivität "
              "verschließen. Jotti ist bewusst silikonfrei: Der Schutz bleibt unsichtbar, die Farbe echt "
              "und das Material atmungsaktiv – gerade bei empfindlichem Wildleder, Textilien und Outdoor-Ausrüstung."),
        visual="Split banner: LEFT a silicone-clogged, darkened swatch; RIGHT the Jotti-treated swatch, matte and true-colour with beading. Clear labels.",
        alt="Vergleich: silikonfrei geschützt vs. silikonhaltig verklebt.",
    ),
    AIModule(
        name="Modul 5 — Range: Welches Jotti-Spray für was?",
        role="a+_carousel",
        headline="WELCHES SPRAY FÜR WAS?",
        body=("<b>UNIVERSAL</b> – der Allrounder für Textil, Leder, Schuhe &amp; mehr.<br/>"
              "<b>TEXTILIEN</b> – für Jacken, Markisen &amp; Outdoor-Textilien.<br/>"
              "<b>WILDLEDER</b> – farbneutral für Wildleder, Nubuk &amp; Velours.<br/>"
              "<b>SCHUHE</b> – für Sneaker, Leder- &amp; Textilschuhe.<br/>"
              "<b>ZELT</b> – für Zelt, Plane &amp; Outdoor-Ausrüstung.<br/>"
              "<b>CABRIO-VERDECK</b> – für Stoff- &amp; Textilverdecke."),
        visual="6-tile carousel: one tile per variant, each showing the bottle + its surface (jacket, suede boot, sneaker, tent, cabrio top, mixed). Consistent brown-accent layout so the buyer picks the right one.",
        alt="Übersicht der 6 Jotti Imprägnierspray-Varianten nach Oberfläche.",
    ),
    AIModule(
        name="Modul 6 — Premium Q&A",
        role="a+_qa",
        headline="HÄUFIGE FRAGEN",
        body=("<b>F.</b> Verändert das Spray die Farbe?<br/><b>A.</b> Nein. Die Rezeptur ist farbneutral – "
              "Farbe und Optik bleiben unverändert.<br/><br/>"
              "<b>F.</b> Ist es wirklich silikonfrei?<br/><b>A.</b> Ja. Bewusst silikonfrei, damit das "
              "Material atmungsaktiv bleibt und nichts verklebt.<br/><br/>"
              "<b>F.</b> Für welche Oberfläche nehme ich welche Variante?<br/><b>A.</b> Universal für fast "
              "alles; sonst die passende Variante (Textilien, Wildleder, Schuhe, Zelt, Cabrio-Verdeck) – siehe Übersicht.<br/><br/>"
              "<b>F.</b> Wie oft muss ich nachbehandeln?<br/><b>A.</b> Der Schutz hält lange; bei "
              "nachlassendem Abperl-Effekt einfach wieder auffrischen.<br/><br/>"
              "<b>F.</b> Wie wende ich es an?<br/><b>A.</b> Gleichmäßig aufsprühen, trocknen lassen – fertig. "
              "Vorher an verdeckter Stelle testen."),
        visual="Vertical Q/A table, brown divider lines, small brown F./A. labels.",
        alt="Premium-Q&A zur Jotti Imprägnierspray-Serie.",
    ),
    AIModule(
        name="Modul 7 — Vergleich",
        role="a+_comparison",
        headline="WARUM JOTTI",
        body=("Vergleich über 4 Spalten: <b>Jotti Imprägnierspray</b> · silikonhaltiges Spray · einfaches "
              "Nässeschutz-Spray · unbehandelt.<br/><br/>"
              "Zeilen: Silikonfrei · Farbneutral · Atmungsaktiv · Langzeit wasser- &amp; schmutzabweisend · "
              "für empfindliche Materialien · Deutsche Manufaktur.<br/><br/>"
              "Die Jotti-Spalte mit brauner Tönung und Ribbon 'Deutsche Manufaktur' hervorheben."),
        visual="Standard Amazon comparison chart, 4 columns; competitor columns as category names only; brown header row.",
        alt="Vergleichstabelle: Jotti silikonfrei vs. silikonhaltige und einfache Sprays.",
    ),
]


def main() -> None:
    print("Lade Jotti + baue Imprägnierspray-Serie (6 Varianten, 1 Dokument)…")
    cust = load_customer("jotti")
    brief = parse_excel(EXCEL)
    variants = [{"label": s["label"], "images": make_images(s)} for s in SURFACES]
    builder = BriefBuilder(cust, brief, OUT, ai=None)
    builder.copy_source_label = "Hand-written senior copy (DE, Serie: 6 spezifische Image-Pläne + 1 A+)"
    pdf = builder.build_line("Jotti Imprägnierspray-Serie — 6 Varianten", variants, SHARED_MODULES)
    size_kb = pdf.stat().st_size // 1024
    print(f"Built: {pdf}  ({size_kb} KB)")


if __name__ == "__main__":
    main()
