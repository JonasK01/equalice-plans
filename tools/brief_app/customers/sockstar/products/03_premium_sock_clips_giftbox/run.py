"""Sockstar — Premium Sock Clips Gift Box (Black & White Edition, 20 Stück)  [Produkt 03]
Titel/Bullets/Backend kommen aus dem gefüllten SEO-Sheet (listing.xlsx), Bildregie + Module
handgeschrieben (freundlich, clean, familienfreundlich), DE.

Marketplace: amazon.de. ASIN B000QGFBQG. Marke: Sockstar (new brand).

House rules aktiv (Config): new_brand=true -> 7 A+ Module, Modul 7 = 'From the Brand'
(kein Comparison); brand_statement -> die coole Marken-Aussage.

STIL (Kunden-Onboarding, strikt): hell, freundlich, aufgeräumt, hochwertig, leicht
verständlich, Premium 'Made in Germany'. KEINE dunklen/technischen/neon/überladenen Looks.
Einwände entkräften: Haltbarkeit (90 °C, hunderte Waschgänge), Preis/Value (nie Socken
verlieren, Zeit sparen), 'zusätzlicher Handgriff' -> als 1-Sekunden-Clip framen.
"""
from __future__ import annotations
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools/brief_app/customers/ultra_pro"))   # seo_loader (generisch)

from tools.brief_app.core.customers import load_customer
from tools.brief_app.core.excel_parser import parse_excel
from tools.brief_app.core.pdf_builder import BriefBuilder
from tools.brief_app.core.ai import AIImagePlanItem, AIModule, AIQA
import seo_loader as SEOL

PLAN_NO = "03"
ASIN = "B000QGFBQG"
EXCEL = HERE / "listing.xlsx"


IMAGES = [
    AIImagePlanItem(
        name="Bild 1 — Main Hero (3 Varianten für A/B-Test)",
        role="hero",
        background="Helles, aufgeräumtes Weiss mit frischem Sockstar-Blau-Akzent (#45BEDA/#0059A1). Bei allen 3 Varianten identisch für einen sauberen Split-Test.",
        purpose="Klick gewinnen — sofort das Alltagsproblem lösen und freundlich/hochwertig wirken.",
        visual=(
            "Alle 3 Varianten mocken. Produkt exakt wie real: die Sockstar-Clips (Black & White "
            "Edition) und ein sauber zusammengeclipptes Sockenpaar. Je EINE einfache Aussage, "
            "Produkt gut sichtbar. Hell, clean, freundlich — kein technischer/dunkler Look. "
            "Amazon-Slot 1 bleibt produktfrei von Text.\n\n"
            "VARIANTE A — DAS VERSPRECHEN: ein Clip hält ein Sockenpaar zusammen, daneben die "
            "Gift-Box. Badge (Blau): 'NIE WIEDER SOCKEN VERLIEREN'.\n"
            "VARIANTE B — DIE REISE: kleine Icon-Reihe Wäschekorb -> Waschmaschine -> Trockner -> "
            "Schublade, Paar bleibt zusammen. Badge: 'VOM KORB BIS ZUR SCHUBLADE'.\n"
            "VARIANTE C — QUALITÄT: Clip-Makro + dt. Flagge. Badge: 'MADE IN GERMANY'.\n\n"
            "Über alle 3: Produkt gut sichtbar, Badge ~6%, gleiche helle Lichtstimmung."
        ),
        overlay="(eine Aussage je Variante)",
        overlay_sub="3 Hero-Varianten — A/B testen, Sieger behalten.",
        props=["A: Clip mit Sockenpaar + Gift-Box", "B: Reise-Icons Korb→Maschine→Trockner→Schublade", "C: Clip-Makro + dt. Flagge"],
        lighting="Helles, weiches Tageslicht; freundlich und aufgeräumt. Bei allen 3 identisch.",
        why_it_works=(
            "Drei Auslöser: A das klare Versprechen, B die durchgängige Ordnung (die Reise), C die "
            "Qualität (Made in Germany). Eine einfache Aussage je Variante — sofort verständlich."
        ),
    ),
    AIImagePlanItem(
        name="Bild 2 — Hook: Schluss mit Einzelsocken",
        role="hook",
        background="Helles Sockstar-Blau #EAF6FB, freundlicher Vorher/Nachher",
        purpose="Das Alltagsproblem und die Lösung in einem Bild — freundlicher Kontrast.",
        visual=(
            "Freundlicher Vorher/Nachher-Split. LINKS: ein kleines, sympathisch dargestelltes "
            "Chaos aus einzelnen, nicht zusammenpassenden Socken ('vorher'). RECHTS: ordentliche, "
            "paarweise zusammengeclippte Socken mit Sockstar-Clip ('nachher'). Klar, hell, "
            "aufgeräumt — kein düsterer/überladener Look."
        ),
        overlay="SCHLUSS MIT EINZELSOCKEN.",
        overlay_sub="Ein Clip hält jedes Sockenpaar zusammen — vom Waschen bis zur Schublade.",
        props=["links: einzelne Socken (Chaos)", "rechts: geclippte Paare (Ordnung)", "Sockstar-Clip"],
        lighting="Hell, freundlich, klarer Kontrast vorher/nachher.",
        why_it_works=(
            "Jeder kennt die verlorene Einzelsocke. Der freundliche Vorher/Nachher-Kontrast macht "
            "den Nutzen in einer Sekunde emotional verständlich."
        ),
    ),
    AIImagePlanItem(
        name="Bild 3 — So einfach geht's",
        role="educate",
        background="Weiss, klares 3-Schritt-Layout",
        purpose="Zeigen, wie einfach es ist — entkräftet den 'zusätzlicher Handgriff'-Einwand.",
        visual=(
            "Drei einfache Schritte mit freundlichen Icons/Realfotos: 1) CLIPPEN — Sockenpaar in "
            "einer Sekunde in den Clip; 2) WASCHEN & TROCKNEN — Clip bleibt dran, in Maschine und "
            "Trockner; 3) VERSTAUEN — paarweise direkt in die Schublade. Kurze, leicht "
            "verständliche Texte. Hell und aufgeräumt."
        ),
        overlay="CLIPPEN. WASCHEN. FERTIG.",
        overlay_sub="In einer Sekunde geclippt — dann waschen, trocknen und paarweise verstauen.",
        props=["3 Schritte (clippen/waschen&trocknen/verstauen)", "freundliche Icons", "Sockenpaar im Clip"],
        lighting="Hell, gleichmässig, leicht verständlich.",
        why_it_works=(
            "Der einzige 'Aufwand' ist ein 1-Sekunden-Clip. Das sichtbar und einfach zu zeigen "
            "entkräftet den 'zusätzlicher Handgriff'-Einwand und senkt die Hürde."
        ),
        cvr="Adressiert den 'extra Schritt'-Einwand mit sichtbarer Einfachheit.",
    ),
    AIImagePlanItem(
        name="Bild 4 — Die Reise: Paare bleiben zusammen",
        role="desire",
        background="Helles Blau, freundliche Wäsche-Reise",
        purpose="Den Kernnutzen zeigen: durchgängige Ordnung von Anfang bis Ende.",
        visual=(
            "Freundliche, aufgeräumte Reise-Illustration/Realfoto-Strip: WÄSCHEKORB -> "
            "WASCHMASCHINE -> TROCKNER -> SCHUBLADE. In jeder Station bleibt das Sockenpaar dank "
            "Sockstar-Clip zusammen. Weiche Pfeile verbinden die Stationen. Hell, klar, "
            "verständlich."
        ),
        overlay="PAARE BLEIBEN ZUSAMMEN.",
        overlay_sub="Vom Wäschekorb über Maschine & Trockner bis in die Schublade — immer als Paar.",
        props=["4-Stationen-Reise (Korb/Maschine/Trockner/Schublade)", "Sockenpaar im Clip", "weiche Verbindungspfeile"],
        lighting="Helles, freundliches Tageslicht über alle Stationen.",
        why_it_works=(
            "Zeigt den vollen Nutzen über den gesamten Waschprozess — nicht nur einen Moment. Das "
            "macht die Zeitersparnis und Ordnung greifbar."
        ),
    ),
    AIImagePlanItem(
        name="Bild 5 — Robuste Qualität, Made in Germany",
        role="trust",
        background="Weiss mit dezenten hellblauen Panels",
        purpose="Haltbarkeit & Preis-Value beweisen — entkräftet 'zu teuer' / 'hält nicht lange'.",
        visual=(
            "Clip-Makro (hochwertiger Kunststoff) mit freundlichen Trust-Badges: 'MADE IN "
            "GERMANY' (dt. Flagge), 'HITZEBESTÄNDIG BIS 90 °C', 'FÜR HUNDERTE WASCHGÄNGE', "
            "'WIEDERVERWENDBAR / NACHHALTIG'. Kurzer Hinweis: 'Einmal kaufen, viele Jahre "
            "nutzen.' Hell, hochwertig, ruhig."
        ),
        overlay="ROBUST: BIS 90 °C.",
        overlay_sub="Made in Germany, für hunderte Waschgänge — einmal kaufen, lange nutzen.",
        props=["Clip-Makro", "4 Trust-Badges (Made in Germany / 90 °C / hunderte Waschgänge / nachhaltig)"],
        lighting="Hell, sauber; Material wirkt hochwertig.",
        why_it_works=(
            "'Zu teuer' und 'hält nicht' sind die Haupt-Einwände. Langlebigkeit (90 °C, hunderte "
            "Waschgänge, Made in Germany) macht den Preis zur Investition und beruhigt Zweifel."
        ),
    ),
    AIImagePlanItem(
        name="Bild 6 — Für die ganze Familie + Gift Box",
        role="desire",
        background="Helles Blau, warme Familien-Anmutung",
        purpose="Zielgruppe & Set-Wert zeigen: 20 Clips, Farben je Familienmitglied, als Geschenk.",
        visual=(
            "Freundliche Familien-Szene/Flatlay: die Gift-Box mit 20 Clips, verschiedene Farben "
            "kleinen Personen/Kategorien zugeordnet (Kinder-, Sport-, Alltagssocken). Kurzer "
            "Hinweis: 'Jedes Familienmitglied seine eigene Farbe.' Die edle Black & White Gift-Box "
            "auch als Geschenk-Anmutung. Hell, warm, aufgeräumt."
        ),
        overlay="FÜR DIE GANZE FAMILIE.",
        overlay_sub="20 Clips in der Gift Box — eigene Farben für jedes Familienmitglied.",
        props=["Gift-Box mit 20 Clips", "Farbzuordnung je Person", "Familien-/Geschenk-Anmutung"],
        lighting="Warmes, helles Wohnlicht; familiär und freundlich.",
        why_it_works=(
            "Klärt 'lohnt sich das für mich?': für Familien mit vielen Socken ist der Nutzen am "
            "grössten. Farben je Person + Gift-Box erhöhen Wert und Geschenk-Eignung."
        ),
    ),
    AIImagePlanItem(
        name="Bild 7 — Markenabschluss: Ordnung an jedem Waschtag",
        role="close",
        background="Helle, aufgeräumte Sockstar-Markenszene (Blau/Weiss)",
        purpose="Auf Marke & Alltagsnutzen abschliessen — freundlich, hochwertig.",
        visual=(
            "Ruhige, helle Aufnahme: geclippte Sockenpaare ordentlich in einer Schublade, die "
            "Gift-Box daneben, Sockstar-Logo. Unteres Band mit drei einfachen Punkten: 'Nie wieder "
            "Socken verlieren', 'Made in Germany, langlebig', 'Weniger Sortieren, mehr Zeit'. "
            "Freundlich, hochwertig, aufgeräumt."
        ),
        overlay="ORDNUNG AN JEDEM WASCHTAG.",
        overlay_sub="Sockstar — der waschbare Sockenclip für einen entspannten Alltag.",
        props=["geclippte Paare in der Schublade", "Gift-Box", "Sockstar-Logo", "3 Nutzen-Punkte"],
        lighting="Hell, ruhig, freundlich. Premium-Alltag.",
        why_it_works=(
            "Schliesst auf das Markenversprechen: mehr Ordnung, weniger Aufwand, hochwertig Made "
            "in Germany — genau das Gefühl, das den Kauf absichert."
        ),
    ),
]


CREATIVE_MODULES = [
    AIModule(
        name="Modul 1 — Markenbanner",
        role="a+_banner",
        headline="NIE WIEDER SOCKEN VERLIEREN.",
        body=(
            "Sockstar ist der waschbare Sockenclip, der deine Sockenpaare vom Wäschekorb über "
            "Waschmaschine und Trockner bis in die Schublade zuverlässig zusammenhält. Robust, "
            "hitzebeständig bis 90 °C und Made in Germany — für weniger Sortieren und mehr Zeit."
        ),
        visual="Breites, helles Banner: Sockstar-Clips mit geclipptem Sockenpaar rechts, freundliche Headline links auf Weiss, Sockstar-Blau-Akzent. Logo oben links.",
        alt="Sockstar Sockenclip Banner: hält Sockenpaare beim Waschen zusammen, Made in Germany.",
    ),
    AIModule(
        name="Modul 2 — Karussell (5 Kacheln): Deine Vorteile",
        role="a+_carousel",
        headline="DEINE VORTEILE",
        body=(
            "Kachel 1: <b>NIE WIEDER EINZELSOCKEN</b> — Jedes Paar bleibt zusammen.<br/>"
            "Kachel 2: <b>SPART ZEIT &amp; NERVEN</b> — Kein Sortieren nach der Wäsche.<br/>"
            "Kachel 3: <b>BIS 90 °C</b> — Waschmaschinen- &amp; trocknergeeignet.<br/>"
            "Kachel 4: <b>FÜR DIE FAMILIE</b> — Eigene Farbe je Familienmitglied.<br/>"
            "Kachel 5: <b>MADE IN GERMANY</b> — Robust, langlebig &amp; wiederverwendbar."
        ),
        visual="5 helle Kacheln, Sockstar-Blau-Akzentecke, freundliche einfache Icons (Sockenpaar · Uhr · Waschmaschine · Familie · dt. Flagge).",
        alt="Fünf A+ Kacheln: nie wieder Einzelsocken, spart Zeit, bis 90 °C, für die Familie, Made in Germany.",
    ),
    AIModule(
        name="Modul 3 — Banner: So einfach geht's",
        role="a+_banner",
        headline="CLIPPEN. WASCHEN. VERSTAUEN.",
        body=(
            "In einer Sekunde geclippt: Sockenpaar in den Sockstar-Clip, ab in Waschmaschine und "
            "Trockner — der Clip bleibt dran — und danach paarweise direkt in die Schublade. Kein "
            "Suchen, kein Sortieren, kein Aufwand."
        ),
        visual="Banner mit 3 freundlichen Schritten (clippen · waschen & trocknen · verstauen), helle Icons/Realfotos, weiche Pfeile.",
        alt="A+ Banner mit den drei einfachen Schritten: clippen, waschen und trocknen, verstauen.",
    ),
    AIModule(
        name="Modul 4 — Banner: Robuste Qualität",
        role="a+_banner",
        headline="ROBUST & LANGLEBIG. MADE IN GERMANY.",
        body=(
            "Gefertigt aus hochwertigem Premium-Kunststoff in Deutschland — hitzebeständig bis "
            "90 °C und gemacht für hunderte Waschgänge. Wiederverwendbar und nachhaltig: einmal "
            "kaufen, viele Jahre nutzen."
        ),
        visual="Banner: Clip-Makro links, Trust-Badges rechts (Made in Germany, 90 °C, hunderte Waschgänge, wiederverwendbar). Hell, hochwertig.",
        alt="A+ Banner zur robusten, langlebigen Qualität Made in Germany, hitzebeständig bis 90 °C.",
    ),
    AIModule(
        name="Modul 5 — Karussell (5 Kacheln): Für wen",
        role="a+_carousel",
        headline="IDEAL FÜR",
        body=(
            "Kachel 1: <b>FAMILIEN</b> — Viele Socken, eigene Farbe pro Person.<br/>"
            "Kachel 2: <b>PAARE &amp; SINGLES</b> — Schluss mit dem Sockensuchen.<br/>"
            "Kachel 3: <b>SPORT</b> — Sportsocken bleiben als Paar zusammen.<br/>"
            "Kachel 4: <b>BUSINESS</b> — Feine Business-Socken ordentlich gepaart.<br/>"
            "Kachel 5: <b>ALS GESCHENK</b> — Edle Gift Box mit 20 Clips."
        ),
        visual="5 helle, freundliche Kacheln (Familie · Paar · Sport · Business · Geschenk), Sockstar-Blau-Akzent.",
        alt="Fünf A+ Kacheln: ideal für Familien, Paare & Singles, Sport, Business und als Geschenk.",
    ),
    AIModule(
        name="Modul 6 — Premium Q&A",
        role="a+_qa",
        headline="HÄUFIGE FRAGEN",
        body=(
            "<b>F.</b> Halten die Clips in Waschmaschine und Trockner?<br/>"
            "<b>A.</b> Ja. Die Sockstar-Clips sind hitzebeständig bis 90 °C und für Waschmaschine "
            "und Trockner geeignet — dein Sockenpaar bleibt die ganze Zeit zusammen.<br/><br/>"
            "<b>F.</b> Ist das nicht ein zusätzlicher Aufwand?<br/>"
            "<b>A.</b> Kaum: Das Sockenpaar ist in einer Sekunde eingeclippt. Dafür entfällt das "
            "lästige Sortieren nach der Wäsche komplett.<br/><br/>"
            "<b>F.</b> Wie langlebig sind sie?<br/>"
            "<b>A.</b> Sehr. Sie sind aus robustem Premium-Kunststoff Made in Germany gefertigt und "
            "für hunderte Waschgänge gemacht — wiederverwendbar und nachhaltig.<br/><br/>"
            "<b>F.</b> Wie viele Clips sind enthalten?<br/>"
            "<b>A.</b> Die Gift Box (Black &amp; White Edition) enthält 20 Clips — genug für die "
            "ganze Familie, mit eigener Farbe je Person.<br/><br/>"
            "<b>F.</b> Für wen lohnt es sich?<br/>"
            "<b>A.</b> Für alle, die regelmäßig Socken waschen — besonders Familien, Sportler und "
            "alle, die Ordnung und Zeitersparnis schätzen."
        ),
        visual="Vertikale Frage-/Antwort-Liste, hellblaue Trennlinien, freundliche, gut lesbare Typo.",
        alt="Premium Q&A Modul zu den Sockstar Sockenclips.",
    ),
]


def main() -> None:
    print("Lade Sockstar + SEO-Sheet…")
    cust = load_customer("sockstar")
    brief = parse_excel(EXCEL)
    seo = SEOL.load_seo(EXCEL)
    OUT = HERE / f"{PLAN_NO}_{ASIN}_Image Plan.pdf"
    print(f"  Produkt: {brief.product_name}  ASIN: {ASIN}  Marktplatz: {cust.marketplace}")
    print(f"  SEO-Titel({len(seo.title)}) + Bullets={len(seo.bullets)} | new_brand={cust.new_brand}")

    builder = BriefBuilder(cust, brief, OUT, ai=None)
    builder._ai_title = seo.title
    builder._ai_bullets = SEOL.as_bullets_html(seo)
    builder._ai_images = IMAGES
    builder._ai_modules = list(CREATIVE_MODULES)
    builder._ai_qa = [
        AIQA(q="Halten die Clips in Waschmaschine und Trockner?",
             a="Ja. Die Sockstar-Clips sind hitzebeständig bis 90 °C und für Waschmaschine und Trockner geeignet. Dein Sockenpaar bleibt die ganze Zeit zusammen."),
        AIQA(q="Ist das nicht ein zusätzlicher Aufwand?",
             a="Kaum. Das Sockenpaar ist in einer Sekunde eingeclippt — dafür entfällt das lästige Sortieren nach der Wäsche komplett."),
        AIQA(q="Wie langlebig sind die Sockenclips?",
             a="Sehr langlebig. Sie sind aus robustem Premium-Kunststoff Made in Germany gefertigt und für hunderte Waschgänge gemacht; wiederverwendbar und nachhaltig."),
        AIQA(q="Wie viele Clips sind enthalten?",
             a="Die Gift Box (Black & White Edition) enthält 20 Clips — genug für die ganze Familie, mit einer eigenen Farbe je Person."),
        AIQA(q="Für wen lohnt sich Sockstar?",
             a="Für alle, die regelmäßig Socken waschen — besonders Familien, Sportler, Paare und alle, die Ordnung und Zeitersparnis schätzen."),
        AIQA(q="Beschädigen die Clips meine Socken?",
             a="Nein. Die Clips sind so gestaltet, dass sie die Socken sicher halten, ohne sie zu beschädigen — vom feinen Business- bis zum robusten Sportsocken."),
    ]
    builder._ai_backend = seo.backend
    builder.copy_source_label = "SEO-Sheet (Titel/Bullets/Backend) + hand-written Bildregie (DE)"

    print("Baue Branded PDF…")
    pdf_path = builder.build()
    size_kb = pdf_path.stat().st_size // 1024
    import re
    pages = len(re.findall(rb'/Type\s*/Page[^s]', pdf_path.read_bytes()))
    print(f"Gebaut: {pdf_path}")
    print(f"  Seiten: {pages}  Größe: {size_kb} KB")


if __name__ == "__main__":
    main()
