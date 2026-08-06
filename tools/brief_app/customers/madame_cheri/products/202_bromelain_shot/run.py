"""Madame Chéri — BROMELAIN SHOT (50 ml, 10er-Box)
Hand-written, KW-led, conversion-focused copy im Feinkost-Look.

Marketplace: amazon.de (DE) — deutsche Overlays + Kunden-Copy.
Produkt 202 · Marke: Madame Chéri (Feinkost). Listing noch nicht live.

Positionierung: tropischer täglicher VITAMIN-MOMENT mit Ananas (Bromelain) + Vitaminen.
Farbwelt: sonniges Ananas-Gelb/Gold. Held: 50-ml-Flasche + 10er-Box, frische Ananas,
tropische Frische, Wasser-Spritzer.

COMPLIANCE (wichtig): Tonalität etwas mutiger = starke Lifestyle-/Benefit-Sprache erlaubt
(tropisch, Power, Vitalität), ABER jede echte Wirkaussage MUSS eine der drei zugelassenen
EU-Health-Claims sein, wörtlich und an den Nährstoff gebunden:
  · 'Vitamin C trägt zu einer normalen Funktion des Immunsystems bei.'
  · 'Vitamin B6 trägt zur Verringerung von Müdigkeit und Ermüdung bei.'
  · 'Vitamin B2 trägt zu einem normalen Energiestoffwechsel bei.'
NICHT erlaubt: 'stärkt das Immunsystem', 'gegen Erkältung', Heil-/Krankheitsbezug,
'beste/Nr.1/garantiert', Abnehmversprechen, Preise/URLs.
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

PLAN_NO = "202"
ASIN = ""   # noch nicht live


BRIEF = ParsedBrief(
    product_name="Madame Chéri Bromelain Shot · 10 x 50 ml",
    brand="Madame Chéri",
    marketplace="amazon.de",
    category="Lebensmittel & Getränke > Nahrungsergänzung > Functional Shots",
    main_keywords=["bromelain shot", "ananas shot", "vitamin c shot"],
    all_keywords=[
        "bromelain shot", "ananas shot", "vitamin c shot", "vitamin c hochdosiert",
        "immun shot", "vitamin shot", "shots", "vitamin b6 shot", "energie shot",
        "tropical shot", "ananas enzym", "shot flaschen", "daily shot", "funktionaler shot",
    ],
    usps=[
        "Tropischer Vitamin-Moment: Ananas-Power für jeden Tag.",
        "Hochdosiertes Vitamin C (ca. 266 mg pro 50-ml-Shot) plus Vitamin B2 und B6.",
        "0 g Zucker — voller tropischer Geschmack ganz ohne Zuckerzusatz.",
        "Praktisches 50-ml-Format für unterwegs, Büro und Morgenroutine.",
        "10er-Box — der Vorrat für zwei Wochen tägliches Ritual.",
        "Premium-Feinkost von Madame Chéri, deutsches Traditionsunternehmen.",
    ],
    target_group=(
        "Wellness-, ernährungs- und lifestylebewusste Frauen und Männer, die ihren Alltag mit "
        "einem einfachen, tropischen Vitamin-Ritual bewusster gestalten möchten."
    ),
    target_problems=(
        "Vitaminpräparate schmecken oft künstlich, sind zuckrig oder umständlich. Gesucht wird "
        "ein schneller, leckerer Vitamin-Moment für jeden Tag — tropisch statt medizinisch."
    ),
    good_reviews=[
        "Schmeckt frisch nach Ananas, gar nicht künstlich.",
        "Praktisch für unterwegs, mein Vitamin-Moment am Morgen.",
        "Angenehm tropisch und dabei ohne Zucker — top.",
    ],
    bad_reviews=[
        "Ananas ist Geschmackssache — für manche etwas zu intensiv.",
    ],
)


# ===== Copy (Deutsch, Feinkost) — Bromelain: mutige Lifestyle-Sprache, Wirkaussagen nur EU-Claims =====

TITLE = ('Madame Chéri Bromelain Shot · 10 x 50 ml — Ananas mit hochdosiertem Vitamin C, '
         'Vitamin B2 & B6 · 0 g Zucker · tropischer Vitamin-Moment für jeden Tag im '
         'praktischen 50-ml-Format')

BULLETS = [
    "<b>DEIN TÄGLICHER VITAMIN-MOMENT</b> — Tropische Ananas-Power in einem Shot: exotischer "
    "Genuss mit wertvollen Vitaminen. Der frische Kick für deine Morgenroutine — einfach "
    "aufdrehen, schütteln und den sonnigen Ananas-Moment genießen.",

    "<b>VITAMIN C FÜR DEIN IMMUNSYSTEM</b> — Mit hochdosiertem Vitamin C (ca. 266 mg pro "
    "50-ml-Shot): Vitamin C trägt zu einer normalen Funktion des Immunsystems bei. Tropische "
    "Kraft, clever kombiniert für deinen Tag.",

    "<b>VITAMIN B6 &amp; B2 FÜR DEINEN TAG</b> — Vitamin B6 trägt zur Verringerung von "
    "Müdigkeit und Ermüdung bei, und Vitamin B2 trägt zu einem normalen Energiestoffwechsel "
    "bei. Vitalität, die schmeckt.",

    "<b>0 G ZUCKER, VOLLE FRISCHE</b> — Voller tropischer Ananas-Geschmack ganz ohne "
    "Zuckerzusatz: 0 g Zucker pro 100 ml. Leichter Genuss statt süßer Softdrink — der "
    "Vitamin-Moment, der sich jeden Tag gut anfühlt.",

    "<b>10ER-BOX VON MADAME CHÉRI FEINKOST</b> — Zehn Shots im edlen Display — dein Vorrat für "
    "zwei Wochen tägliches Ritual oder zum Ausprobieren und Teilen. Premium-Feinkost aus einem "
    "deutschen Traditionsunternehmen.",
]


IMAGES = [
    AIImagePlanItem(
        name="Bild 1 — Main Hero (3 Varianten für A/B-Test)",
        role="hero",
        background="Sonniges Ananas-Gelb mit hellem Verlauf (Bromelain-Farbwelt), passend zum Etikett. Bei allen 3 Varianten identisch für einen sauberen Split-Test.",
        purpose="Klick gewinnen im Shot-Raster — sofort erkennbar als tropischer, premium Vitamin-Shot.",
        visual=(
            "Alle 3 Varianten mocken, Sieger behalten. Feinkost-Look: Madame-Chéri-Logo oben "
            "links, dunkelgrüner runder Badge 'Deutsches Traditionsunternehmen', Mengen-Schild "
            "'10 Stück' in Gelb/Gold. Produkt exakt wie real (klare 50-ml-Flasche, weisser "
            "Deckel, gelbes Etikett 'Bromelain Shot'). Amazon-Slot 1 bleibt produktfrei von "
            "Text — dies sind die CTR-Mains für den A/B-Test.\n\n"

            "VARIANTE A — TROPISCHE FRISCHE (Emotion)\n"
            "Flasche mittig auf einem goldenen Podest, ringsum frische Ananasscheiben, ein "
            "Ananasblatt-Schopf und dynamische Wasser-Spritzer — sonnig, tropisch, appetitlich. "
            "Frische Tropfen im Flug.\n"
            "BADGE (Serif, weiss auf grünem Block): 'TROPISCHER VITAMIN-MOMENT'.\n"
            "Gewinnt, weil es Genuss + Frische in einem Blick zeigt.\n\n"

            "VARIANTE B — DIE 10ER-BOX (Wert)\n"
            "Die geöffnete 10er-Display-Box mit sichtbaren Fläschchen, zwei Shots davor, frische "
            "Ananas daneben.\n"
            "BADGE: '10 SHOTS · 2 WOCHEN RITUAL'.\n"
            "Gewinnt, weil es Menge und Vorrat sofort klarmacht.\n\n"

            "VARIANTE C — VITAMIN C + 0 G ZUCKER (Fakt)\n"
            "Flasche freigestellt, daneben ein sauberer Ananas-Fächer, ein Vitamin-C-Chip und "
            "ein '0 g Zucker'-Chip.\n"
            "BADGE: 'VITAMIN C · 0 G ZUCKER'.\n"
            "Gewinnt, weil hochdosiertes Vitamin C + 0 g Zucker der stärkste rationale Hook ist.\n\n"

            "Über alle 3: Flasche dominant, Badge ca. 6 % der Fläche, gleiche Lichtstimmung."
        ),
        overlay="(eine Aussage je Variante)",
        overlay_sub="3 Hero-Varianten — A/B testen, Sieger behalten.",
        props=[
            "A: Flasche + frische Ananasscheiben + Wasser-Spritzer",
            "B: geöffnete 10er-Box + 2 Shots + frische Ananas",
            "C: freigestellte Flasche + Ananas-Fächer + Vitamin-C- & 0-g-Zucker-Chip",
        ],
        lighting="Hell, sonnig, appetitlich; weiche Schatten. Bei allen 3 identisch für den Split-Test.",
        why_it_works=(
            "Drei Auslöser: A verkauft das Gefühl (tropische Frische), B den Vorrat/Wert, C den "
            "rationalen Hook (hochdosiertes Vitamin C, 0 g Zucker). Je eine Aussage — auf dem "
            "Thumbnail sofort lesbar."
        ),
    ),
    AIImagePlanItem(
        name="Bild 2 — Vitamine im Fokus: C, B2 & B6",
        role="hook",
        background="Cremeweiss #F0EADD mit dunkelgrünem Serif-Headline-Block oben rechts (Feinkost-Chrome), goldene Akzente",
        purpose="In einem Bild zeigen, welche Vitamine drin sind — und wofür sie zugelassen sind.",
        visual=(
            "Flasche mittig, darum drei weisse Outline-Icon-Kreise (Feinkost-Callout-Stil), je "
            "Vitamin einer, mit kurzem zugelassenem Claim als Untertext:\n"
            "  • VITAMIN C — 'trägt zu einer normalen Funktion des Immunsystems bei'\n"
            "  • VITAMIN B6 — 'trägt zur Verringerung von Müdigkeit und Ermüdung bei'\n"
            "  • VITAMIN B2 — 'trägt zu einem normalen Energiestoffwechsel bei'\n\n"
            "Verbindende feine Linien von den Icons zur Flasche. Frische Ananasscheiben locker "
            "gestreut. Headline-Block oben: 'Vitalität trifft Geschmack'. Claim-Texte wörtlich "
            "und an den Nährstoff gebunden."
        ),
        overlay="VITAMINE IM FOKUS.",
        overlay_sub="Vitamin C, B2 & B6 — clever kombiniert für deinen Tag.",
        props=["Flasche", "3 Vitamin-Icon-Kreise (C, B6, B2) mit Claim-Untertext", "Ananasscheiben"],
        lighting="Helles, gleichmässiges Food-Licht. Appetitlich und klar.",
        why_it_works=(
            "Macht die drei Vitamine und ihre EU-zugelassenen Benefits in einem Blick greifbar. "
            "Konkrete, rechtssichere Claims schaffen Vertrauen und heben den Shot von vagen "
            "Vitamin-Produkten ab."
        ),
        cvr="Übersetzt 'Vitamine drin' in konkrete, zugelassene Benefits — der rationale Kaufgrund.",
    ),
    AIImagePlanItem(
        name="Bild 3 — Warum kaufen: hochdosiert & 0 g Zucker",
        role="educate",
        background="Sonniges Ananas-Gelb, heller Verlauf",
        purpose="Den rationalen Kaufgrund verankern: viel Vitamin C, 0 g Zucker, tropischer Geschmack.",
        visual=(
            "Freigestellte Flasche links, rechts drei ruhige Fakt-Kacheln mit Outline-Icons:\n"
            "  • VITAMIN C HOCHDOSIERT — ca. 266 mg pro 50-ml-Shot\n"
            "  • 0 G ZUCKER — voller Geschmack ohne Zuckerzusatz\n"
            "  • ANANAS-BASIS — tropisch, natürlich, frisch\n\n"
            "Kleiner Nährwert-Hinweis dezent am Fuss (pro 100 ml: 533 mg Vitamin C, Zucker 0 g). "
            "Ehrlich und unaufgeregt — Wirkaussagen nur als zugelassene Claims, sonst klare Fakten."
        ),
        overlay="0 G ZUCKER.",
        overlay_sub="Hochdosiertes Vitamin C, tropischer Ananas-Geschmack — ganz ohne Zuckerzusatz.",
        props=["freigestellte Flasche", "3 Fakt-Kacheln", "dezenter Nährwert-Hinweis"],
        lighting="Hell und sonnig, klarer Fokus auf der Flasche.",
        why_it_works=(
            "Hochdosiertes Vitamin C + 0 g Zucker ist der stärkste, rechtlich sichere "
            "Doppel-Hook: Benefit und Guilt-free in einem. Ehrliche Zahlen statt Heilversprechen "
            "passen zur Premium-Positionierung."
        ),
    ),
    AIImagePlanItem(
        name="Bild 4 — Der Vitamin-Moment im Alltag",
        role="desire",
        background="Helle, moderne Küche / Schreibtisch am Morgen, warmes Tageslicht",
        purpose="Den Shot in den Alltag der Zielgruppe setzen — das tägliche Vitamin-Ritual sichtbar machen.",
        visual=(
            "Lifestyle-Szene: eine Frau (oder Hände, elegant, ohne Gesichtsfokus) hält den "
            "geöffneten Bromelain Shot am hellen Küchentresen oder Schreibtisch, daneben frische "
            "Ananas und ein Glas Wasser, im Hintergrund weich ein sonniges Morgen-Setting. Ruhig, "
            "premium, echt — kein Studio-Pharma-Look.\n\n"
            "Kleiner Hinweis-Chip: 'Vor dem Trinken kurz schütteln.'"
        ),
        overlay="ANANAS-POWER FÜR DEN TAG.",
        overlay_sub="Aufdrehen, schütteln, genießen — dein tropischer Vitamin-Moment für jeden Tag.",
        props=["Person/Hände mit Shot", "frische Ananas", "Glas Wasser", "sonniges Morgen-Setting", "Schüttel-Hinweis"],
        lighting="Warmes, weiches Morgenlicht von der Seite. Aspirational, aber echt.",
        why_it_works=(
            "Verkauft das Gefühl, nicht nur die Flasche: der tropische, leichte Vitamin-Moment. "
            "Das tägliche Ritual macht aus einem Einzelkauf eine Routine — und damit Wiederkäufe."
        ),
    ),
    AIImagePlanItem(
        name="Bild 5 — Die Shot-Familie von Madame Chéri",
        role="desire",
        background="Cremeweiss #F0EADD mit dunkelgrünem Headline-Block",
        purpose="Cross-Sell: die ganze Daily-Shot-Linie zeigen, Wiedererkennung der Farbwelten.",
        visual=(
            "Sechs Flaschen der Linie in ihren Farbwelten nebeneinander, jede mit kleinem Label:\n"
            "  • DETOX (grün) · BROMELAIN (gelb, dieses Produkt) · KOLLAGEN (pink) · MAGNESIUM "
            "(blau) · GINSENG (bernstein) · GINGER (orange)\n\n"
            "Der Bromelain-Shot dezent hervorgehoben (leichter Rahmen/Podest). Darunter der "
            "Dachclaim 'Daily Shots. Daily Benefits.'"
        ),
        overlay="SECHS SORTEN, EIN RITUAL.",
        overlay_sub="Entdecke die Madame Chéri Daily Shots — für jeden Tag die passende.",
        props=["6 Flaschen in Farbwelten", "Bromelain hervorgehoben", "Dachclaim-Leiste"],
        lighting="Helles, gleichmässiges Studiolicht; jede Farbwelt klar erkennbar.",
        why_it_works=(
            "Zeigt Sortiments-Tiefe und Marken-System. Wer den Bromelain kauft, sieht sofort die "
            "nächsten Sorten für andere Momente — starker Cross-Sell-Hebel für die neue Linie."
        ),
    ),
    AIImagePlanItem(
        name="Bild 6 — Format & Handling",
        role="desire",
        background="Sonniges Ananas-Gelb, hell",
        purpose="Menge, Grösse und Handling klarmachen — letzte Kaufhürde räumen.",
        visual=(
            "Zweiteilig. LINKS: die 10er-Box mit den Fläschchen, Label '10 x 50 ml'. RECHTS: eine "
            "Flasche in der Hand als Grössenreferenz (handlich, taschentauglich) mit drei kleinen "
            "Schritt-Icons: 'Schütteln → Aufdrehen → Genießen'.\n\n"
            "Kleiner Fuss: 'Ungeöffnet praktisch für Vorrat und unterwegs.'"
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
            "Ruhige, edle Aufnahme: die Bromelain-Flasche und die 10er-Box sauber arrangiert, "
            "frische Ananas dezent, viel Weissraum. Madame-Chéri-Logo mittig, darunter der dunkle "
            "runde Badge 'Deutsches Traditionsunternehmen' und der Dachclaim 'Daily Shots. Daily "
            "Benefits.'\n\n"
            "Ton: premium, warm, ruhig — Feinkost, keine Superlative."
        ),
        overlay="FEINKOST FÜR JEDEN TAG.",
        overlay_sub="Madame Chéri — Daily Shots, Daily Benefits. Deutsches Traditionsunternehmen.",
        props=["Flasche + 10er-Box arrangiert", "frische Ananas", "Logo", "Deutsches-Traditionsunternehmen-Badge", "Dachclaim"],
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
        headline="TROPISCHE KRAFT. CLEVER KOMBINIERT.",
        body=(
            "Der Madame Chéri Bromelain Shot ist dein tropischer Vitamin-Moment: Ananas-Power "
            "mit hochdosiertem Vitamin C sowie Vitamin B2 und B6 — 0 g Zucker, voller "
            "Geschmack. Praktisch im 50-ml-Format."
        ),
        visual="Breites Banner: Bromelain-Flasche rechts vor sonnigem Ananas-Gelb mit frischen Ananasscheiben und Wasser-Spritzern, links grosse Serif-Headline auf cremeweiss. Logo oben links.",
        alt="Madame Chéri Bromelain Shot vor sonnigem Ananas-Gelb mit frischer Ananas als tropischer Vitamin-Moment.",
    ),
    AIModule(
        name="Modul 2 — Karussell (5 Kacheln): Warum Bromelain Shot",
        role="a+_carousel",
        headline="WARUM BROMELAIN SHOT",
        body=(
            "Kachel 1: <b>TROPISCH FRISCH</b> — Ananas-Power für deinen Tag.<br/>"
            "Kachel 2: <b>VITAMIN C</b> — Trägt zu einer normalen Funktion des Immunsystems bei.<br/>"
            "Kachel 3: <b>VITAMIN B6 &amp; B2</b> — Weniger Müdigkeit, normaler Energiestoffwechsel.<br/>"
            "Kachel 4: <b>0 G ZUCKER</b> — Voller Geschmack, kein Zuckerzusatz.<br/>"
            "Kachel 5: <b>10ER-BOX</b> — Der Vorrat für zwei Wochen Ritual."
        ),
        visual="5 quadratische Kacheln, dunkelgrüne Akzentecke, weisse Outline-Icons, je eine Zeile Text.",
        alt="Fünf A+ Kacheln zum Bromelain Shot: tropisch frisch, Vitamin C, B6 & B2, 0 g Zucker, 10er-Box.",
    ),
    AIModule(
        name="Modul 3 — Banner: Die Vitamine",
        role="a+_banner",
        headline="VITALITÄT TRIFFT GESCHMACK.",
        body=(
            "Vitamin C trägt zu einer normalen Funktion des Immunsystems bei. Vitamin B6 trägt "
            "zur Verringerung von Müdigkeit und Ermüdung bei. Vitamin B2 trägt zu einem normalen "
            "Energiestoffwechsel bei."
        ),
        visual="Banner mit drei Vitaminen in weissen Outline-Kreisen (Vitamin C, B6, B2, je mit zugelassenem Claim), Flasche rechts, frische Ananasscheiben gestreut.",
        alt="A+ Banner mit Vitamin C, B6 und B2 des Bromelain Shots und ihren zugelassenen EU-Claims.",
    ),
    AIModule(
        name="Modul 4 — Banner: Das Ritual",
        role="a+_banner",
        headline="AUFDREHEN. SCHÜTTELN. GENIESSEN.",
        body=(
            "In jede Routine integrierbar: morgens nach dem Aufstehen, im Büro oder vor dem "
            "Sport. Vor dem Trinken kurz schütteln — fertig ist dein tropischer Vitamin-Moment. "
            "0 g Zucker."
        ),
        visual="Banner mit drei ruhigen Alltagsszenen (Küche morgens, Schreibtisch, Sporttasche), Flasche im Vordergrund, warmes Tageslicht.",
        alt="A+ Banner mit dem Bromelain Shot als tägliches Ritual in Küche, Büro und beim Sport.",
    ),
    AIModule(
        name="Modul 5 — Karussell (6 Kacheln): Die Daily-Shot-Linie",
        role="a+_carousel",
        headline="DIE MADAME CHÉRI DAILY SHOTS",
        body=(
            "Kachel 1: <b>DETOX</b> — Fruchtiges Frische-Ritual mit grünem Apfelessig.<br/>"
            "Kachel 2: <b>BROMELAIN</b> — Ananas &amp; Vitamin C, B2, B6 (dieses Produkt).<br/>"
            "Kachel 3: <b>KOLLAGEN</b> — Beauty von innen, mit Zink &amp; Selen.<br/>"
            "Kachel 4: <b>MAGNESIUM</b> — Für Muskeln, Nerven &amp; Energie.<br/>"
            "Kachel 5: <b>GINSENG</b> — Fokus-Ritual, Tradition trifft Moderne.<br/>"
            "Kachel 6: <b>GINGER</b> — Scharf, frisch, der Kick am Morgen."
        ),
        visual="6 Flaschen in ihren Farbwelten, einheitliche Komposition, Bromelain dezent hervorgehoben. Dachclaim 'Daily Shots. Daily Benefits.'",
        alt="A+ Karussell mit allen sechs Madame Chéri Daily Shots in ihren Farbwelten.",
    ),
    AIModule(
        name="Modul 6 — Premium Q&A",
        role="a+_qa",
        headline="HÄUFIGE FRAGEN",
        body=(
            "<b>F.</b> Wie schmeckt der Shot?<br/>"
            "<b>A.</b> Tropisch-frisch nach Ananas — voller Geschmack, ganz ohne Zuckerzusatz.<br/><br/>"
            "<b>F.</b> Welche Vitamine sind drin?<br/>"
            "<b>A.</b> Hochdosiertes Vitamin C sowie Vitamin B2 und B6.<br/><br/>"
            "<b>F.</b> Wie viel Zucker?<br/>"
            "<b>A.</b> 0 g Zucker pro 100 ml — leichter Genuss statt süßer Softdrink.<br/><br/>"
            "<b>F.</b> Wie wird er getrunken?<br/>"
            "<b>A.</b> Vor dem Trinken kurz schütteln und pur genießen — ganz nach deiner Routine.<br/><br/>"
            "<b>F.</b> Wie viele sind enthalten?<br/>"
            "<b>A.</b> 10 Fläschchen à 50 ml — der Vorrat für zwei Wochen tägliches Ritual."
        ),
        visual="Vertikale Frage-/Antwort-Liste, dunkelgrüne Trennlinien, F. in Grün und A. in Gold. Kurze Antworten.",
        alt="Premium Q&A Modul mit fünf Kurzantworten zum Madame Chéri Bromelain Shot.",
    ),
    AIModule(
        name="Modul 7 — Premium Vergleichstabelle",
        role="a+_comparison",
        headline="DER SMARTE VITAMIN-MOMENT",
        body=(
            "Vier Spalten: <b>Madame Chéri Bromelain Shot</b> · Frische Ananas pressen · "
            "Vitamin-Brausetabletten · Softdrink.<br/><br/>"
            "Zeilen: Tropisch frisch · Hochdosiertes Vitamin C · 0 g Zucker · Kein Aufwand / "
            "kein Pressen · Praktisch für unterwegs · Vitamin B6 &amp; B2.<br/><br/>"
            "Die Bromelain-Spalte gelb hervorheben, Band 'DAILY SHOTS'. Vergleichsspalten nur "
            "als Kategorie, keine Fremdmarken."
        ),
        visual="Standard Amazon Premium Vergleichstabelle, 4 Spalten, Kopfzeile dunkelgrün, Bromelain-Spalte hellgelb hinterlegt.",
        alt="Premium Vergleichstabelle Bromelain Shot gegenüber Ananas pressen, Brausetabletten und Softdrink.",
    ),
]


QA = [
    AIQA(q="Wie schmeckt der Bromelain Shot?",
         a="Tropisch-frisch nach Ananas — exotischer Genuss mit vollem Geschmack, ganz ohne Zuckerzusatz."),
    AIQA(q="Welche Vitamine sind enthalten?",
         a="Hochdosiertes Vitamin C (ca. 266 mg pro 50-ml-Shot) sowie Vitamin B2 und B6. Vitamin C trägt zu einer normalen Funktion des Immunsystems bei."),
    AIQA(q="Wie viel Zucker hat ein Shot?",
         a="0 g Zucker pro 100 ml — voller tropischer Ananas-Geschmack ganz ohne Zuckerzusatz."),
    AIQA(q="Wobei helfen die B-Vitamine?",
         a="Vitamin B6 trägt zur Verringerung von Müdigkeit und Ermüdung bei, und Vitamin B2 trägt zu einem normalen Energiestoffwechsel bei."),
    AIQA(q="Wie trinke ich den Shot am besten?",
         a="Vor dem Trinken kurz schütteln und pur genießen. Ob morgens, im Büro oder vor dem Sport — ganz nach deiner Routine."),
    AIQA(q="Wie viele Shots sind in der Box?",
         a="Die Box enthält 10 Fläschchen à 50 ml — dein Vorrat für rund zwei Wochen täglichen Vitamin-Moment."),
    AIQA(q="Von wem ist der Bromelain Shot?",
         a="Von Madame Chéri, einem deutschen Feinkost-Traditionsunternehmen. Teil der Daily-Shot-Linie 'Daily Shots. Daily Benefits.'"),
]


BACKEND = (
    "bromelain shot ananas vitamin c hochdosiert immun vitamin b6 b2 energie shot tropical "
    "funktionaler shot flaschen daily wellness 0 zucker ritual morgenroutine unterwegs 50ml "
    "10er box madame cheri feinkost getraenk vitalitaet"
)


def main() -> None:
    print("Lade Madame Chéri + Bromelain-Achse…")
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
