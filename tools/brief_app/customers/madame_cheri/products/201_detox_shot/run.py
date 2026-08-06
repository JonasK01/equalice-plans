"""Madame Chéri — DETOX SHOT (50 ml, 10er-Box)
Hand-written, KW-led, conversion-focused copy im Feinkost-Look.

Marketplace: amazon.de (DE) — deutsche Overlays + Kunden-Copy.
Produkt 201 · Marke: Madame Chéri (Feinkost). Listing noch nicht live.

Positionierung: fruchtiges tägliches FRISCHE-RITUAL mit grünem Apfelessig.
Farbwelt: frisches Grün. Held: 50-ml-Flasche + 10er-Box, schwebende Zutaten-Bubbles.

COMPLIANCE (wichtig): 'Detox' nur als Produktname vom Etikett — KEIN Entgiftungs-,
Entschlackungs- oder Wirkversprechen. Für Detox gibt es KEINE zugelassenen EU-Health-Claims,
daher rein über Genuss, Frische, Zutaten, wenig Kalorien und Ritual kommunizieren.
Kein 'beste/Nr.1', keine Abnehm-/Heilbezüge, keine Preise/URLs.
"""
from __future__ import annotations
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
sys.path.insert(0, str(ROOT))

from tools.brief_app.core.customers import load_customer
from tools.brief_app.core.excel_parser import ParsedBrief
from tools.brief_app.core.pdf_builder import BriefBuilder
from tools.brief_app.core.ai import AIImagePlanItem, AIModule, AIQA

PLAN_NO = "201"
ASIN = ""   # noch nicht live


BRIEF = ParsedBrief(
    product_name="Madame Chéri Detox Shot · 10 x 50 ml",
    brand="Madame Chéri",
    marketplace="amazon.de",
    category="Lebensmittel & Getränke > Nahrungsergänzung > Functional Shots",
    main_keywords=["detox shot", "shots", "vitamin shot"],
    all_keywords=[
        "detox shot", "shots", "shots gesund", "vitamin shot", "apfelessig shot",
        "apfelessig trinken", "ingwer shot", "wellness shot", "functional shot",
        "detox kur", "frische shots", "shot flaschen", "daily shot", "grüner apfelessig",
        "shots set", "detox getränk", "kalorienarm getränk", "rosmarin zitrone honig",
    ],
    usps=[
        "Tägliches Frische-Ritual mit fruchtiger Rezeptur.",
        "5 natürliche Zutaten: grüner Apfelessig, Aprikose, Zitrone, Honig, Rosmarin.",
        "Nur rund 15 kcal pro 50-ml-Shot, nahezu fettfrei.",
        "Praktisches 50-ml-Format für unterwegs, Büro und Morgenroutine.",
        "10er-Box — der Vorrat für zwei Wochen tägliches Ritual.",
        "Premium-Feinkost von Madame Chéri, deutsches Traditionsunternehmen.",
    ],
    target_group=(
        "Wellness-, ernährungs- und lifestylebewusste Frauen und Männer, die ihren Alltag mit "
        "einem einfachen, fruchtigen Frische-Ritual bewusster gestalten möchten."
    ),
    target_problems=(
        "Selbst pressen ist aufwendig, große Saftflaschen sind unpraktisch und oft zuckrig. "
        "Gesucht wird ein schnelles, leckeres, kalorienarmes Ritual für jeden Tag."
    ),
    good_reviews=[
        "Schmeckt frisch und fruchtig, nicht so sauer wie befürchtet.",
        "Praktisch für unterwegs, kein Pressen mehr am Morgen.",
        "Angenehm leicht, schöner Start in den Tag.",
    ],
    bad_reviews=[
        "Apfelessig ist Geschmackssache — für manche zu säuerlich.",
    ],
)


# ===== Copy (Deutsch, Feinkost) — Detox: nur Genuss/Ritual, keine Health-Claims =====

TITLE = ('Madame Chéri Detox Shot · 10 x 50 ml — Fruchtiges Frische-Ritual mit grünem Apfelessig, '
         'Aprikose, Zitrone, Honig & Rosmarin · nur ca. 15 kcal pro Shot · praktisch für jeden Tag')

BULLETS = [
    "<b>DEIN TÄGLICHES FRISCHE-RITUAL</b> — Ein fruchtiger Shot, der in jede Morgenroutine passt. "
    "Weniger Ballast, mehr Frische: der leichte, bewusste Start in den Tag — ohne Pressen, ohne "
    "Aufwand, einfach aufdrehen und genießen.",

    "<b>5 NATÜRLICHE ZUTATEN, FEIN KOMPONIERT</b> — Grüner Apfelessig, Aprikose, Zitrone, Honig "
    "und Rosmarin ergeben eine fruchtig-frische Rezeptur mit Charakter. Sorgfältig abgestimmt von "
    "Madame Chéri — deutlich runder im Geschmack als purer Apfelessig.",

    "<b>NUR CA. 15 KCAL PRO SHOT</b> — Leichter Genuss statt schwerer Drink: nahezu fettfrei und "
    "kalorienarm, damit das Ritual sich jeden Tag gut anfühlt. Der frische Moment für zwischendurch, "
    "der nicht beschwert.",

    "<b>PRAKTISCH FÜR UNTERWEGS</b> — Das handliche 50-ml-Format passt in jede Tasche: für Büro, "
    "Sport, Reise oder direkt nach dem Aufstehen. Vor dem Trinken kurz schütteln — fertig ist dein "
    "Frische-Moment.",

    "<b>10ER-BOX VON MADAME CHÉRI FEINKOST</b> — Zehn Shots im edlen Display — dein Vorrat für "
    "zwei Wochen tägliches Ritual oder zum Ausprobieren und Teilen. Premium-Feinkost aus einem "
    "deutschen Traditionsunternehmen.",
]


IMAGES = [
    AIImagePlanItem(
        name="Bild 1 — Main Hero (3 Varianten für A/B-Test)",
        role="hero",
        background="Frisches, sattes Grün mit hellem Verlauf (Detox-Farbwelt), passend zum Etikett. Bei allen 3 Varianten identisch für einen sauberen Split-Test.",
        purpose="Klick gewinnen im Shot-Raster — sofort erkennbar als frisches, premium Ritual.",
        visual=(
            "Alle 3 Varianten mocken, Sieger behalten. Feinkost-Look: Madame-Chéri-Logo oben "
            "links, dunkelgrüner runder Badge 'Deutsches Traditionsunternehmen', Mengen-Schild "
            "'10 Stück' in Grün. Produkt exakt wie real (klare 50-ml-Flasche, weisser Deckel, "
            "grün-graues Etikett 'Detox Shot'). Amazon-Slot 1 bleibt produktfrei von Text — dies "
            "sind die CTR-Mains für den A/B-Test.\n\n"

            "VARIANTE A — FRISCHE-RITUAL (Emotion)\n"
            "Flasche mittig auf einem grünen Podest, ringsum schwebende Wasser-Bubbles mit je "
            "einer Zutat (grüner Apfel, Zitrone, Aprikose, Honigwabe, Rosmarin) — exakt der Look "
            "des vorhandenen Detox-Keyvisuals, nur premiumisiert. Frische Blätter im Flug.\n"
            "BADGE (Serif, weiss auf grünem Block): 'TÄGLICHES FRISCHE-RITUAL'.\n"
            "Gewinnt, weil es Genuss + Natürlichkeit in einem Blick zeigt.\n\n"

            "VARIANTE B — DIE 10ER-BOX (Wert)\n"
            "Die geöffnete 10er-Display-Box mit sichtbaren Fläschchen, zwei Shots davor, frische "
            "Zutaten daneben.\n"
            "BADGE: '10 SHOTS · 2 WOCHEN RITUAL'.\n"
            "Gewinnt, weil es Menge und Vorrat sofort klarmacht.\n\n"

            "VARIANTE C — LEICHT & EHRLICH (Fakt)\n"
            "Flasche freigestellt, daneben ein sauberer Zutaten-Fächer (Apfelessig, Aprikose, "
            "Zitrone, Honig, Rosmarin) und ein kleiner Kalorien-Chip.\n"
            "BADGE: 'NUR CA. 15 KCAL'.\n"
            "Gewinnt, weil kalorienarm + natürliche Zutaten der stärkste rationale Hook ist.\n\n"

            "Über alle 3: Flasche dominant, Badge ca. 6 % der Fläche, gleiche Lichtstimmung."
        ),
        overlay="(eine Aussage je Variante)",
        overlay_sub="3 Hero-Varianten — A/B testen, Sieger behalten.",
        props=[
            "A: Flasche + schwebende Zutaten-Bubbles + Frische-Blätter",
            "B: geöffnete 10er-Box + 2 Shots + frische Zutaten",
            "C: freigestellte Flasche + Zutaten-Fächer + Kalorien-Chip",
        ],
        lighting="Hell, frisch, appetitlich; weiche Schatten. Bei allen 3 identisch für den Split-Test.",
        why_it_works=(
            "Drei Auslöser: A verkauft das Gefühl (frisches Ritual), B den Vorrat/Wert, C den "
            "rationalen Hook (kalorienarm, natürliche Zutaten). Je eine Aussage — auf dem "
            "Thumbnail sofort lesbar."
        ),
    ),
    AIImagePlanItem(
        name="Bild 2 — Was drin ist: 5 natürliche Zutaten",
        role="hook",
        background="Cremeweiss #F0EADD mit dunkelgrünem Serif-Headline-Block oben rechts (Feinkost-Chrome)",
        purpose="In einem Bild zeigen, woraus der Shot besteht — und dass er fein komponiert ist.",
        visual=(
            "Flasche mittig, darum in fünf weissen Outline-Kreis-Icons (Feinkost-Callout-Stil) die "
            "Zutaten mit echten Frisch-Fotos und Label:\n"
            "  • Grüner Apfelessig\n  • Aprikose\n  • Zitrone\n  • Honig\n  • Rosmarin\n\n"
            "Verbindende feine Linien von den Zutaten zur Flasche. Frische Fruchtscheiben und ein "
            "Rosmarinzweig locker gestreut. Headline-Block oben: 'Fein komponiert, nicht nur "
            "sauer'."
        ),
        overlay="5 NATÜRLICHE ZUTATEN.",
        overlay_sub="Grüner Apfelessig, Aprikose, Zitrone, Honig & Rosmarin — fruchtig-fein.",
        props=["Flasche", "5 Zutaten-Icon-Kreise mit Frisch-Fotos", "Fruchtscheiben", "Rosmarinzweig"],
        lighting="Helles, gleichmässiges Food-Licht. Appetitlich und klar.",
        why_it_works=(
            "Bei einem Apfelessig-Shot ist die grösste Hürde 'schmeckt das nur sauer?'. Die fünf "
            "fein abgestimmten Zutaten sichtbar zu machen, verkauft Genuss statt Medizin und hebt "
            "den Shot von puren Apfelessig-Produkten ab."
        ),
        cvr="Adressiert direkt die häufigste Geschmacks-Sorge (zu sauer).",
    ),
    AIImagePlanItem(
        name="Bild 3 — Warum kaufen: leicht & ehrlich",
        role="educate",
        background="Frisches Grün, heller Verlauf",
        purpose="Den rationalen Kaufgrund verankern: kalorienarm, nahezu fettfrei, natürlicher Genuss.",
        visual=(
            "Freigestellte Flasche links, rechts drei ruhige Fakt-Kacheln mit Outline-Icons:\n"
            "  • NUR CA. 15 KCAL pro 50-ml-Shot\n"
            "  • NAHEZU FETTFREI\n"
            "  • FRUCHTIGE, NATÜRLICHE REZEPTUR\n\n"
            "Kleiner Nährwert-Hinweis dezent am Fuss (pro 100 ml: 30 kcal). Ehrlich und "
            "unaufgeregt — keine Wirkversprechen, nur klare Fakten und Genuss."
        ),
        overlay="LEICHT GENIESSEN.",
        overlay_sub="Rund 15 kcal pro Shot, nahezu fettfrei — fruchtig-frisch statt schwer.",
        props=["freigestellte Flasche", "3 Fakt-Kacheln", "dezenter Nährwert-Hinweis"],
        lighting="Hell und frisch, klarer Fokus auf der Flasche.",
        why_it_works=(
            "Kalorienarm + natürlich ist der stärkste rechtlich sichere Kaufgrund. Ehrliche "
            "Fakten statt Heilversprechen passen zur Premium-Positionierung und schaffen Vertrauen."
        ),
    ),
    AIImagePlanItem(
        name="Bild 4 — Das Ritual im Alltag",
        role="desire",
        background="Helle, moderne Küche / Schreibtisch am Morgen, warmes Tageslicht",
        purpose="Den Shot in den Alltag der Zielgruppe setzen — das tägliche Ritual sichtbar machen.",
        visual=(
            "Lifestyle-Szene: eine Frau (oder Hände, elegant, ohne Gesichtsfokus) hält den "
            "geöffneten Detox Shot am hellen Küchentresen oder Schreibtisch, daneben ein Glas "
            "Wasser, frische Zitrone und Rosmarin, im Hintergrund weich ein Morgen-Setting. "
            "Ruhig, premium, echt — kein Studio-Pharma-Look.\n\n"
            "Kleiner Hinweis-Chip: 'Vor dem Trinken kurz schütteln.'"
        ),
        overlay="DEIN MOMENT AM MORGEN.",
        overlay_sub="Aufdrehen, schütteln, genießen — dein frisches Ritual für jeden Tag.",
        props=["Person/Hände mit Shot", "Glas Wasser", "frische Zitrone & Rosmarin", "helles Morgen-Setting", "Schüttel-Hinweis"],
        lighting="Warmes, weiches Morgenlicht von der Seite. Aspirational, aber echt.",
        why_it_works=(
            "Verkauft das Gefühl, nicht nur die Flasche: der bewusste, leichte Start in den Tag. "
            "Das tägliche Ritual macht aus einem Einzelkauf eine Routine — und damit "
            "Wiederkäufe."
        ),
    ),
    AIImagePlanItem(
        name="Bild 5 — Die Shot-Familie von Madame Chéri",
        role="desire",
        background="Cremeweiss #F0EADD mit dunkelgrünem Headline-Block",
        purpose="Cross-Sell: die ganze Daily-Shot-Linie zeigen, Wiedererkennung der Farbwelten.",
        visual=(
            "Sechs Flaschen der Linie in ihren Farbwelten nebeneinander, jede mit kleinem Label:\n"
            "  • DETOX (grün, dieses Produkt) · BROMELAIN (gelb) · KOLLAGEN (pink) · MAGNESIUM "
            "(blau) · GINSENG (bernstein) · GINGER (orange)\n\n"
            "Der Detox-Shot dezent hervorgehoben (leichter Rahmen/Podest). Darunter der Dachclaim "
            "'Daily Shots. Daily Benefits.'"
        ),
        overlay="EIN RITUAL, SECHS SORTEN.",
        overlay_sub="Entdecke die Madame Chéri Daily Shots — für jeden Tag die passende.",
        props=["6 Flaschen in Farbwelten", "Detox hervorgehoben", "Dachclaim-Leiste"],
        lighting="Helles, gleichmässiges Studiolicht; jede Farbwelt klar erkennbar.",
        why_it_works=(
            "Zeigt Sortiments-Tiefe und Marken-System. Wer den Detox kauft, sieht sofort die "
            "nächsten Sorten für andere Momente — starker Cross-Sell-Hebel für die neue Linie."
        ),
    ),
    AIImagePlanItem(
        name="Bild 6 — Format & Handling",
        role="desire",
        background="Frisches Grün, hell",
        purpose="Menge, Grösse und Handling klarmachen — letzte Kaufhürde räumen.",
        visual=(
            "Zweiteilig. LINKS: die 10er-Box mit den Fläschchen, Label '10 x 50 ml'. RECHTS: eine "
            "Flasche in der Hand als Grössenreferenz (handlich, taschentauglich) mit drei kleinen "
            "Schritt-Icons: 'Schütteln → Aufdrehen → Genießen'.\n\n"
            "Kleiner Fuss: 'Ungeöffnet haltbar — praktisch für Vorrat und unterwegs.'"
        ),
        overlay="IMMER DABEI.",
        overlay_sub="10 x 50 ml, handlich für Büro, Sport & unterwegs — schütteln, aufdrehen, genießen.",
        props=["10er-Box", "Flasche in der Hand (Grössenreferenz)", "3 Schritt-Icons"],
        lighting="Hell und klar, ehrliche Grössen- und Farbwiedergabe.",
        why_it_works=(
            "Beantwortet 'wie viel, wie gross, wie benutze ich das?' in einem Bild und macht den "
            "Vorrats-Vorteil der 10er-Box greifbar."
        ),
    ),
    AIImagePlanItem(
        name="Bild 7 — Markenabschluss: Madame Chéri Feinkost",
        role="close",
        background="Cremeweiss #F0EADD, edel, mit goldenen Akzenten",
        purpose="Mit der Premium-Marke abschliessen — Vertrauen vor dem Kauf.",
        visual=(
            "Ruhige, edle Aufnahme: die Detox-Flasche und die 10er-Box sauber arrangiert, frische "
            "Zutaten dezent, viel Weissraum. Madame-Chéri-Logo mittig, darunter der dunkle runde "
            "Badge 'Deutsches Traditionsunternehmen' und der Dachclaim 'Daily Shots. Daily "
            "Benefits.'\n\n"
            "Ton: premium, warm, ruhig — Feinkost, keine Superlative."
        ),
        overlay="FEINKOST FÜR JEDEN TAG.",
        overlay_sub="Madame Chéri — Daily Shots, Daily Benefits. Deutsches Traditionsunternehmen.",
        props=["Flasche + 10er-Box arrangiert", "frische Zutaten", "Logo", "Deutsches-Traditionsunternehmen-Badge", "Dachclaim"],
        lighting="Weiches, edles Licht mit warmen Goldreflexen. Premium und ruhig.",
        why_it_works=(
            "Schliesst auf Marke und Vertrauen: deutsches Feinkost-Traditionsunternehmen statt "
            "namenloser Shot. Genau das Signal, das bei einem neuen Produkt den Kauf absichert."
        ),
    ),
]


MODULES = [
    AIModule(
        name="Modul 1 — Markenbanner",
        role="a+_banner",
        headline="DEIN TÄGLICHES FRISCHE-RITUAL.",
        body=(
            "Der Madame Chéri Detox Shot ist der leichte, fruchtige Start in den Tag: grüner "
            "Apfelessig, Aprikose, Zitrone, Honig und Rosmarin, fein komponiert. Weniger Ballast, "
            "mehr Frische — praktisch im 50-ml-Format."
        ),
        visual="Breites Banner: Detox-Flasche rechts vor frischem Grün mit schwebenden Zutaten-Bubbles, links grosse Serif-Headline auf cremeweiss. Logo oben links.",
        alt="Madame Chéri Detox Shot vor frischem Grün mit schwebenden Zutaten als tägliches Frische-Ritual.",
    ),
    AIModule(
        name="Modul 2 — Karussell (5 Kacheln): Warum Detox Shot",
        role="a+_carousel",
        headline="WARUM DETOX SHOT",
        body=(
            "Kachel 1: <b>FRUCHTIG-FRISCH</b> — Fein komponiert, nicht nur sauer.<br/>"
            "Kachel 2: <b>5 NATÜRLICHE ZUTATEN</b> — Apfelessig, Aprikose, Zitrone, Honig &amp; Rosmarin.<br/>"
            "Kachel 3: <b>CA. 15 KCAL</b> — Leichter Genuss, nahezu fettfrei.<br/>"
            "Kachel 4: <b>PRAKTISCH</b> — 50-ml-Format für unterwegs, kein Pressen.<br/>"
            "Kachel 5: <b>10ER-BOX</b> — Der Vorrat für zwei Wochen Ritual."
        ),
        visual="5 quadratische Kacheln, dunkelgrüne Akzentecke, weisse Outline-Icons, je eine Zeile Text.",
        alt="Fünf A+ Kacheln zum Detox Shot: fruchtig-frisch, natürliche Zutaten, kalorienarm, praktisch, 10er-Box.",
    ),
    AIModule(
        name="Modul 3 — Banner: Die Zutaten",
        role="a+_banner",
        headline="FEIN KOMPONIERT, NICHT NUR SAUER.",
        body=(
            "Grüner Apfelessig trifft auf Aprikose, Zitrone, Honig und Rosmarin — eine "
            "fruchtig-frische Rezeptur mit Charakter, sorgfältig abgestimmt von Madame Chéri. "
            "Deutlich runder im Geschmack als purer Apfelessig."
        ),
        visual="Banner mit fünf Zutaten in weissen Outline-Kreisen (Apfelessig, Aprikose, Zitrone, Honig, Rosmarin), Flasche rechts, frische Fruchtscheiben gestreut.",
        alt="A+ Banner mit den fünf natürlichen Zutaten des Detox Shots rund um die Flasche.",
    ),
    AIModule(
        name="Modul 4 — Banner: Das Ritual",
        role="a+_banner",
        headline="AUFDREHEN. SCHÜTTELN. GENIESSEN.",
        body=(
            "In jede Routine integrierbar: morgens nach dem Aufstehen, im Büro oder vor dem "
            "Sport. Vor dem Trinken kurz schütteln — fertig ist dein frischer Moment. Nur rund "
            "15 kcal pro Shot."
        ),
        visual="Banner mit drei ruhigen Alltagsszenen (Küche morgens, Schreibtisch, Sporttasche), Flasche im Vordergrund, warmes Tageslicht.",
        alt="A+ Banner mit dem Detox Shot als tägliches Ritual in Küche, Büro und beim Sport.",
    ),
    AIModule(
        name="Modul 5 — Karussell (6 Kacheln): Die Daily-Shot-Linie",
        role="a+_carousel",
        headline="DIE MADAME CHÉRI DAILY SHOTS",
        body=(
            "Kachel 1: <b>DETOX</b> — Fruchtiges Frische-Ritual (dieses Produkt).<br/>"
            "Kachel 2: <b>BROMELAIN</b> — Ananas &amp; Vitamin C, B2, B6.<br/>"
            "Kachel 3: <b>KOLLAGEN</b> — Beauty von innen, mit Zink &amp; Selen.<br/>"
            "Kachel 4: <b>MAGNESIUM</b> — Für Muskeln, Nerven &amp; Energie.<br/>"
            "Kachel 5: <b>GINSENG</b> — Fokus-Ritual, Tradition trifft Moderne.<br/>"
            "Kachel 6: <b>GINGER</b> — Scharf, frisch, der Kick am Morgen."
        ),
        visual="6 Flaschen in ihren Farbwelten, einheitliche Komposition, Detox dezent hervorgehoben. Dachclaim 'Daily Shots. Daily Benefits.'",
        alt="A+ Karussell mit allen sechs Madame Chéri Daily Shots in ihren Farbwelten.",
    ),
    AIModule(
        name="Modul 6 — Premium Q&A",
        role="a+_qa",
        headline="HÄUFIGE FRAGEN",
        body=(
            "<b>F.</b> Wie schmeckt der Shot?<br/>"
            "<b>A.</b> Fruchtig-frisch: grüner Apfelessig mit Aprikose, Zitrone, Honig und "
            "Rosmarin — runder als purer Apfelessig.<br/><br/>"
            "<b>F.</b> Wie viele Kalorien?<br/>"
            "<b>A.</b> Rund 15 kcal pro 50-ml-Shot, nahezu fettfrei.<br/><br/>"
            "<b>F.</b> Wie wird er getrunken?<br/>"
            "<b>A.</b> Vor dem Trinken kurz schütteln und pur genießen — jederzeit, ganz nach "
            "deiner Routine.<br/><br/>"
            "<b>F.</b> Wie viele sind enthalten?<br/>"
            "<b>A.</b> 10 Fläschchen à 50 ml — der Vorrat für zwei Wochen tägliches Ritual.<br/><br/>"
            "<b>F.</b> Von wem ist der Shot?<br/>"
            "<b>A.</b> Von Madame Chéri Feinkost, einem deutschen Traditionsunternehmen."
        ),
        visual="Vertikale Frage-/Antwort-Liste, dunkelgrüne Trennlinien, F. in Grün und A. in Gold. Kurze Antworten.",
        alt="Premium Q&A Modul mit fünf Kurzantworten zum Madame Chéri Detox Shot.",
    ),
    AIModule(
        name="Modul 7 — Premium Vergleichstabelle",
        role="a+_comparison",
        headline="DER SMARTE WEG ZUM FRISCHE-RITUAL",
        body=(
            "Vier Spalten: <b>Madame Chéri Detox Shot</b> · Selbst pressen · Große Saftflasche · "
            "Softdrink.<br/><br/>"
            "Zeilen: Fruchtig-frisch · Nur ca. 15 kcal pro Portion · Natürliche Zutaten · Kein "
            "Aufwand / kein Pressen · Praktisch für unterwegs · Fein komponierte Rezeptur.<br/><br/>"
            "Die Detox-Spalte grün hervorheben, Band 'DAILY SHOTS'. Vergleichsspalten nur als "
            "Kategorie, keine Fremdmarken."
        ),
        visual="Standard Amazon Premium Vergleichstabelle, 4 Spalten, Kopfzeile dunkelgrün, Detox-Spalte hellgrün hinterlegt.",
        alt="Premium Vergleichstabelle Detox Shot gegenüber selbst pressen, Saftflasche und Softdrink.",
    ),
]


QA = [
    AIQA(q="Wie schmeckt der Detox Shot?",
         a="Fruchtig-frisch. Grüner Apfelessig wird mit Aprikose, Zitrone, Honig und Rosmarin zu einer runden, fein abgestimmten Rezeptur kombiniert — deutlich angenehmer als purer Apfelessig."),
    AIQA(q="Wie viele Kalorien hat ein Shot?",
         a="Rund 15 kcal pro 50-ml-Shot (30 kcal pro 100 ml) und nahezu fettfrei — ein leichter Genuss für jeden Tag."),
    AIQA(q="Welche Zutaten sind enthalten?",
         a="Grüner Apfelessig, Aprikose, Zitrone, Honig und Rosmarin — eine fruchtig-frische Rezeptur von Madame Chéri."),
    AIQA(q="Wie trinke ich den Shot am besten?",
         a="Vor dem Trinken kurz schütteln und pur genießen. Ob morgens, im Büro oder vor dem Sport — ganz nach deiner Routine."),
    AIQA(q="Wie viele Shots sind in der Box?",
         a="Die Box enthält 10 Fläschchen à 50 ml — dein Vorrat für rund zwei Wochen tägliches Frische-Ritual."),
    AIQA(q="Muss der Shot gekühlt werden?",
         a="Ungeöffnet ist er praktisch für Vorrat und unterwegs. Details zur Lagerung stehen auf dem Etikett; angebrochen kühl stellen und zeitnah genießen."),
    AIQA(q="Von wem ist der Detox Shot?",
         a="Von Madame Chéri, einem deutschen Feinkost-Traditionsunternehmen. Teil der Daily-Shot-Linie 'Daily Shots. Daily Benefits.'"),
]


BACKEND = (
    "detox shot apfelessig shot vitamin shot wellness shot functional shot daily shot frische "
    "shots shot flaschen kalorienarm rosmarin zitrone honig aprikose gruener apfelessig ritual "
    "morgenroutine unterwegs 50ml 10er box madame cheri feinkost getraenk"
)


def main() -> None:
    print("Lade Madame Chéri + Detox-Achse…")
    cust = load_customer("madame_cheri")
    brief = BRIEF
    _asin = ASIN or "NA"
    OUT = HERE / f"{PLAN_NO}_{_asin}_Image Plan.pdf"
    print(f"  Produkt: {brief.product_name}  Marktplatz: {cust.marketplace}")

    builder = BriefBuilder(cust, brief, OUT, ai=None)
    builder._ai_title = TITLE
    builder._ai_bullets = BULLETS
    builder._ai_images = IMAGES
    builder._ai_modules = MODULES
    builder._ai_qa = QA
    builder._ai_backend = BACKEND
    builder.copy_source_label = "Hand-written senior copy (Feinkost, DE)"

    print("Baue Branded PDF…")
    pdf_path = builder.build()
    size_kb = pdf_path.stat().st_size // 1024
    import re
    pages = len(re.findall(rb'/Type\s*/Page[^s]', pdf_path.read_bytes()))
    print(f"Gebaut: {pdf_path}")
    print(f"  Seiten: {pages}  Größe: {size_kb} KB")


if __name__ == "__main__":
    main()
