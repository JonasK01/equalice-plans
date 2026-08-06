"""Madame Chéri — KOLLAGEN SHOT (50 ml, 10er-Box)
Hand-written, KW-led, conversion-focused copy im Feinkost-Look.

Marketplace: amazon.de (DE) — deutsche Overlays + Kunden-Copy.
Produkt 203 · Marke: Madame Chéri (Feinkost). Listing noch nicht live.

Positionierung: kommerzielles Flaggschiff — der Beauty-Shot, ein tägliches
Beauty-Ritual von innen. Tonalität etwas mutiger: starke Beauty-Lifestyle-Sprache
('Glow', 'Beauty von innen', 'strahlend') erlaubt.
Farbwelt: Beere/Pink/Magenta. Held: 50-ml-Flasche + 10er-Box, tropische Früchte
(Kiwi, Mango, Erdbeere, Ananas), Beauty-Editorial, hell & premium.

COMPLIANCE (wichtig): Kollagen selbst hat KEINEN zugelassenen EU-Health-Claim.
Über Kollagen NUR Fakten (Typ 1 & 3, 500 Da Tripeptid, 10 g pro Portion, Geschmack) —
KEINE Wirkaussage (kein 'straff', 'gegen Falten', 'Anti-Aging'). Der Haut/Haare/Nägel-
Benefit MUSS an ZINK bzw. SELEN gebunden sein, wörtlich mit den zugelassenen Claims:
  Zink -> 'Zink trägt zur Erhaltung normaler Haut, Haare und Nägel bei.'
  Selen -> 'Selen trägt zur Erhaltung normaler Haare und Nägel bei.'
  Folsäure -> 'Folsäure hat eine Funktion bei der Zellteilung.'
  Vitamin B6 -> 'Vitamin B6 trägt zu einem normalen Energiestoffwechsel bei.'
Kein 'beste/Nr.1', keine Anti-Aging-/Faltenversprechen, keine Preise/URLs.
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

PLAN_NO = "203"
ASIN = ""   # noch nicht live


BRIEF = ParsedBrief(
    product_name="Madame Chéri Kollagen Shot · 10 x 50 ml",
    brand="Madame Chéri",
    marketplace="amazon.de",
    category="Lebensmittel & Getränke > Nahrungsergänzung > Functional Shots",
    main_keywords=["kollagen shot", "collagen shot", "beauty shot"],
    all_keywords=[
        "kollagen shot", "collagen shot", "kollagen trinken", "kollagen hochdosiert",
        "beauty shot", "kollagen tripeptid", "zink selen shot", "kollagen typ 1 3",
        "collagen drink", "hautpflege von innen", "kollagen flüssig", "shots",
        "folsäure shot", "kollagen 10g",
    ],
    usps=[
        "Tägliches Beauty-Ritual von innen im 50-ml-Format.",
        "10 g Kollagen pro Portion — Typ 1 & 3, 500 Da Kollagen-Tripeptid.",
        "Mit Zink: trägt zur Erhaltung normaler Haut, Haare und Nägel bei.",
        "Mit Selen & Folsäure: Haare/Nägel und Funktion bei der Zellteilung.",
        "Geschmack Tropische Früchte (Kiwi, Mango, Erdbeere, Ananas), 0 g Zucker.",
        "10er-Box Premium-Feinkost von Madame Chéri, deutsches Traditionsunternehmen.",
    ],
    target_group=(
        "Beauty-, wellness- und lifestylebewusste Frauen (und Männer), die ihre Routine mit "
        "einem einfachen, wohlschmeckenden Beauty-Ritual von innen ergänzen möchten — "
        "praktisch für Morgenroutine, Büro und unterwegs."
    ),
    target_problems=(
        "Kollagen-Pulver muss angerührt und dosiert werden, Kapseln sind unpraktisch, viele "
        "Beauty-Drinks sind zuckrig. Gesucht wird ein trinkfertiger, leckerer Shot mit klar "
        "deklarierten Nährstoffen für jeden Tag."
    ),
    good_reviews=[
        "Schmeckt fruchtig-tropisch, gar nicht künstlich.",
        "Trinkfertig — kein Anrühren wie beim Pulver.",
        "Praktisches Format, passt in meine Morgenroutine.",
    ],
    bad_reviews=[
        "Vor dem Trinken gut schütteln, sonst setzt sich etwas ab.",
    ],
)


# ===== Copy (Deutsch, Feinkost) — Kollagen: Fakten + zugelassene Nährstoff-Claims =====

TITLE = ('Madame Chéri Kollagen Shot · 10 x 50 ml — Typ 1 & 3, 10 g Kollagen pro Portion · '
         'mit Zink, Selen, Folsäure & B6 · Tropische Früchte · 0 g Zucker · Dein Beauty-Ritual von innen')

BULLETS = [
    "<b>DEIN TÄGLICHES BEAUTY-RITUAL VON INNEN</b> — Beauty beginnt von innen: ein "
    "trinkfertiger Shot, der in jede Morgenroutine passt. Aufdrehen, gut schütteln, "
    "genießen — dein täglicher Beauty-Moment, strahlend durch den Tag, ganz ohne Anrühren "
    "oder Dosieren.",

    "<b>10 G KOLLAGEN, TYP 1 &amp; 3 · 500 DA TRIPEPTID</b> — Pro Portion stecken 10 g "
    "Kollagen in deinem Shot: Kollagen Typ 1 &amp; 3 als niedermolekulares 500 Da "
    "Kollagen-Tripeptid. Klar deklariert, hochdosiert und trinkfertig statt Pulver-Anrühren.",

    "<b>ZINK FÜR HAUT, HAARE &amp; NÄGEL</b> — Mit 25 mg Zink pro Portion: Zink trägt zur "
    "Erhaltung normaler Haut, Haare und Nägel bei. Der clevere Beauty-Nährstoff, fest in "
    "dein tägliches Ritual eingebaut.",

    "<b>SELEN &amp; FOLSÄURE CLEVER KOMBINIERT</b> — Selen trägt zur Erhaltung normaler "
    "Haare und Nägel bei, Folsäure hat eine Funktion bei der Zellteilung und Vitamin B6 "
    "trägt zu einem normalen Energiestoffwechsel bei — ein durchdachtes Nährstoff-Bündel.",

    "<b>TROPISCHE FRÜCHTE, 0 G ZUCKER</b> — Geschmack Tropische Früchte mit Kiwi, Mango, "
    "Erdbeere &amp; Ananas: fruchtig-frisch und mit 0 g Zucker. Zehn Shots im edlen Display "
    "— Premium-Feinkost von Madame Chéri, deutsches Traditionsunternehmen.",
]


IMAGES = [
    AIImagePlanItem(
        name="Bild 1 — Main Hero (3 Varianten für A/B-Test)",
        role="hero",
        background="Beere/Pink-Verlauf, hell & premium (Kollagen-Farbwelt), passend zum Etikett. Bei allen 3 Varianten identisch für einen sauberen Split-Test.",
        purpose="Klick gewinnen im Shot-Raster — sofort erkennbar als premium Beauty-Ritual.",
        visual=(
            "Alle 3 Varianten mocken, Sieger behalten. Feinkost-Look: Madame-Chéri-Logo oben "
            "links, dunkelgrüner runder Badge 'Deutsches Traditionsunternehmen', Mengen-Schild "
            "'10 Stück' in Beere/Pink. Produkt exakt wie real (50-ml-Flasche, weisser Deckel, "
            "pink-magenta Etikett 'Kollagen Shot'). Amazon-Slot 1 bleibt produktfrei von "
            "Overlay-Text — dies sind die CTR-Mains für den A/B-Test.\n\n"

            "VARIANTE A — BEAUTY-EMOTION\n"
            "Flasche mittig auf einem Beere-Podest, ringsum schwebende Wasser-Bubbles mit "
            "tropischen Früchten (Kiwi, Mango, Erdbeere, Ananas) im Beauty-Editorial-Look, "
            "weiche rosa Spritzer. Premium und feminin-elegant.\n"
            "BADGE (Serif, weiss auf Beere-Block): 'BEAUTY VON INNEN'.\n"
            "Gewinnt, weil es Glow + Genuss in einem Blick verkauft.\n\n"

            "VARIANTE B — DIE 10ER-BOX (Wert)\n"
            "Die geöffnete 10er-Display-Box mit sichtbaren Fläschchen, zwei Shots davor, "
            "tropische Früchte daneben.\n"
            "BADGE: '10 SHOTS · 2 WOCHEN RITUAL'.\n"
            "Gewinnt, weil es Menge und Vorrat sofort klarmacht.\n\n"

            "VARIANTE C — DER FAKT (rational)\n"
            "Flasche freigestellt, daneben ein sauberer Fakt-Chip '10 G KOLLAGEN' und zwei "
            "kleine Nährstoff-Kreise 'ZINK' + 'SELEN'.\n"
            "BADGE: '10 G KOLLAGEN · TYP 1 & 3'.\n"
            "Gewinnt, weil hochdosiertes Kollagen + Beauty-Nährstoffe der stärkste rationale "
            "Hook sind.\n\n"

            "Über alle 3: Flasche dominant, Badge ca. 6 % der Fläche, gleiche Lichtstimmung."
        ),
        overlay="(eine Aussage je Variante)",
        overlay_sub="3 Hero-Varianten — A/B testen, Sieger behalten.",
        props=[
            "A: Flasche + schwebende Frucht-Bubbles + rosa Spritzer",
            "B: geöffnete 10er-Box + 2 Shots + tropische Früchte",
            "C: freigestellte Flasche + '10 g Kollagen'-Chip + Zink & Selen-Kreise",
        ],
        lighting="Hell, premium, appetitlich; weiche Schatten. Bei allen 3 identisch für den Split-Test.",
        why_it_works=(
            "Drei Auslöser: A verkauft das Gefühl (Beauty von innen), B den Vorrat/Wert, C den "
            "rationalen Hook (10 g Kollagen + Zink & Selen). Je eine Aussage — auf dem "
            "Thumbnail sofort lesbar."
        ),
    ),
    AIImagePlanItem(
        name="Bild 2 — Was drin ist: 10 g Kollagen + Nährstoffe",
        role="hook",
        background="Cremeweiss #F0EADD mit dunkelgrünem Serif-Headline-Block oben rechts (Feinkost-Chrome), Beere-Akzente",
        purpose="In einem Bild zeigen, was der Shot liefert — Kollagen als Fakt, Nährstoffe als Claim-Icons.",
        visual=(
            "Flasche mittig. Grosser Fakt-Chip zentral: '10 G KOLLAGEN PRO PORTION · TYP 1 & 3 · "
            "500 DA KOLLAGEN-TRIPEPTID' (reiner Fakt, KEINE Wirkaussage). Darum in vier weissen "
            "Outline-Kreis-Icons (Feinkost-Callout-Stil) die Nährstoffe mit Menge + zugelassenem "
            "Claim:\n"
            "  • ZINK 25 mg — 'trägt zur Erhaltung normaler Haut, Haare und Nägel bei'\n"
            "  • SELEN 275 µg — 'trägt zur Erhaltung normaler Haare und Nägel bei'\n"
            "  • FOLSÄURE 1000 µg — 'hat eine Funktion bei der Zellteilung'\n"
            "  • VITAMIN B6 7 mg — 'trägt zu einem normalen Energiestoffwechsel bei'\n\n"
            "Verbindende feine Linien von den Icons zur Flasche. Headline-Block oben: "
            "'Beauty Nutrition, klar deklariert'."
        ),
        overlay="10 G KOLLAGEN PRO SHOT.",
        overlay_sub="Typ 1 & 3, 500 Da Kollagen-Tripeptid — plus Zink, Selen, Folsäure & B6.",
        props=["Flasche", "'10 g Kollagen'-Fakt-Chip", "4 Nährstoff-Icon-Kreise mit Menge & Claim"],
        lighting="Helles, gleichmässiges Studiolicht. Klar und premium.",
        why_it_works=(
            "Trennt sauber: Kollagen wird als Fakt (Typ, Tripeptid, 10 g) gezeigt, der "
            "Beauty-Benefit ausschliesslich über die zugelassenen Zink-/Selen-Claims. Genau "
            "das macht den Shot glaubwürdig UND rechtssicher."
        ),
        cvr="Beantwortet 'was bringt mir das?' mit Menge + zugelassenem Nährstoff-Claim.",
    ),
    AIImagePlanItem(
        name="Bild 3 — Beauty von innen: die zugelassenen Claims",
        role="educate",
        background="Beere/Pink, heller Verlauf",
        purpose="Den Beauty-Kaufgrund rechtssicher verankern — jeder Benefit an seinen Nährstoff gebunden.",
        visual=(
            "Freigestellte Flasche links, rechts drei ruhige Claim-Kacheln mit Outline-Icons "
            "(jede Aussage wörtlich, an den Nährstoff gebunden):\n"
            "  • ZINK — trägt zur Erhaltung normaler Haut, Haare und Nägel bei\n"
            "  • SELEN — trägt zur Erhaltung normaler Haare und Nägel bei\n"
            "  • FOLSÄURE — hat eine Funktion bei der Zellteilung\n\n"
            "Kleiner Fuss dezent: 'Vitamin B6 trägt zu einem normalen Energiestoffwechsel bei.' "
            "Kollagen erscheint nur als Fakt-Zeile ('10 g Kollagen, Typ 1 & 3') — ohne "
            "Wirkversprechen. Ton: ehrlich, premium, kein Pharma-Look."
        ),
        overlay="BEAUTY BEGINNT VON INNEN.",
        overlay_sub="Zink trägt zur Erhaltung normaler Haut, Haare und Nägel bei.",
        props=["freigestellte Flasche", "3 Claim-Kacheln (Zink/Selen/Folsäure)", "dezenter B6-Hinweis", "Kollagen-Fakt-Zeile"],
        lighting="Hell und frisch, klarer Fokus auf der Flasche.",
        why_it_works=(
            "Bindet den emotionalen Beauty-Anspruch an die einzig zulässigen Aussagen — die "
            "Nährstoff-Claims. Starker, glaubwürdiger Kaufgrund ohne rechtliches Risiko."
        ),
    ),
    AIImagePlanItem(
        name="Bild 4 — Geschmack & Ritual im Alltag",
        role="desire",
        background="Helles, modernes Beauty-Setting / Waschtisch am Morgen, warmes Tageslicht, Beere-Akzente",
        purpose="Geschmack und tägliches Ritual sichtbar machen — Genuss statt Medizin.",
        visual=(
            "Lifestyle-Szene: eine Frau (oder elegante Hände, ohne Gesichtsfokus) hält den "
            "geöffneten Kollagen Shot am hellen Waschtisch oder Küchentresen, tropische Früchte "
            "(Kiwi, Mango, Erdbeere, Ananas) dekorativ, weich im Hintergrund ein Morgen-Setting. "
            "Ruhig, premium, echt — kein Studio-Pharma-Look.\n\n"
            "Deutlicher Hinweis-Chip: 'Vor dem Trinken gut schütteln.' Kleiner Geschmacks-Chip: "
            "'Tropische Früchte · 0 g Zucker'."
        ),
        overlay="DEIN TÄGLICHER BEAUTY-MOMENT.",
        overlay_sub="Tropische Früchte (Kiwi, Mango, Erdbeere, Ananas) — 0 g Zucker. Gut schütteln.",
        props=["Person/Hände mit Shot", "tropische Früchte", "helles Morgen-Setting", "Schüttel-Hinweis", "Geschmacks-Chip"],
        lighting="Warmes, weiches Morgenlicht von der Seite. Aspirational, aber echt.",
        why_it_works=(
            "Verkauft das Gefühl und den Geschmack: der wohlschmeckende, tägliche Beauty-Moment. "
            "Das Ritual macht aus einem Einzelkauf eine Routine — und damit Wiederkäufe."
        ),
    ),
    AIImagePlanItem(
        name="Bild 5 — Die Shot-Familie von Madame Chéri",
        role="desire",
        background="Cremeweiss #F0EADD mit dunkelgrünem Headline-Block",
        purpose="Cross-Sell: die ganze Daily-Shot-Linie zeigen, Kollagen hervorgehoben.",
        visual=(
            "Sechs Flaschen der Linie in ihren Farbwelten nebeneinander, jede mit kleinem Label:\n"
            "  • DETOX (grün) · BROMELAIN (gelb) · KOLLAGEN (pink, dieses Produkt) · MAGNESIUM "
            "(blau) · GINSENG (bernstein) · GINGER (orange)\n\n"
            "Der Kollagen-Shot deutlich hervorgehoben (Beere-Rahmen/Podest, leicht grösser). "
            "Darunter der Dachclaim 'Daily Shots. Daily Benefits.'"
        ),
        overlay="EIN RITUAL, SECHS SORTEN.",
        overlay_sub="Entdecke die Madame Chéri Daily Shots — für jeden Tag die passende.",
        props=["6 Flaschen in Farbwelten", "Kollagen hervorgehoben", "Dachclaim-Leiste"],
        lighting="Helles, gleichmässiges Studiolicht; jede Farbwelt klar erkennbar.",
        why_it_works=(
            "Zeigt Sortiments-Tiefe und Marken-System. Wer den Kollagen-Shot kauft, sieht sofort "
            "die nächsten Sorten für andere Momente — starker Cross-Sell-Hebel für die Linie."
        ),
    ),
    AIImagePlanItem(
        name="Bild 6 — Format & Handling",
        role="desire",
        background="Beere/Pink, hell",
        purpose="Menge, Grösse und Handling klarmachen — letzte Kaufhürde räumen.",
        visual=(
            "Zweiteilig. LINKS: die 10er-Box mit den Fläschchen, Label '10 x 50 ml'. RECHTS: eine "
            "Flasche in der Hand als Grössenreferenz (handlich, taschentauglich) mit drei kleinen "
            "Schritt-Icons: 'Schütteln → Aufdrehen → Genießen'.\n\n"
            "Kleiner Fuss: 'Vor dem Trinken gut schütteln — praktisch für Vorrat und unterwegs.'"
        ),
        overlay="IMMER DABEI, TÄGLICH GLOW.",
        overlay_sub="10 x 50 ml — handlich für Büro, Sport & unterwegs. Vor dem Trinken gut schütteln.",
        props=["10er-Box", "Flasche in der Hand (Grössenreferenz)", "3 Schritt-Icons", "Schüttel-Hinweis"],
        lighting="Hell und klar, ehrliche Grössen- und Farbwiedergabe.",
        why_it_works=(
            "Beantwortet 'wie viel, wie gross, wie benutze ich das?' in einem Bild und macht den "
            "Vorrats-Vorteil der 10er-Box greifbar."
        ),
    ),
    AIImagePlanItem(
        name="Bild 7 — Markenabschluss: Madame Chéri Feinkost",
        role="close",
        background="Cremeweiss #F0EADD, edel, mit goldenen Akzenten und Beere-Detail",
        purpose="Mit der Premium-Marke abschliessen — Vertrauen vor dem Kauf.",
        visual=(
            "Ruhige, edle Aufnahme: die Kollagen-Flasche und die 10er-Box sauber arrangiert, "
            "tropische Früchte dezent, viel Weissraum. Madame-Chéri-Logo mittig, darunter der "
            "dunkle runde Badge 'Deutsches Traditionsunternehmen' und der Dachclaim 'Daily Shots. "
            "Daily Benefits.'\n\n"
            "Ton: premium, warm, ruhig — Feinkost, keine Superlative."
        ),
        overlay="FEINKOST FÜR DEINEN GLOW.",
        overlay_sub="Madame Chéri — Daily Shots, Daily Benefits. Deutsches Traditionsunternehmen.",
        props=["Flasche + 10er-Box arrangiert", "tropische Früchte", "Logo", "Deutsches-Traditionsunternehmen-Badge", "Dachclaim"],
        lighting="Weiches, edles Licht mit warmen Goldreflexen. Premium und ruhig.",
        why_it_works=(
            "Schliesst auf Marke und Vertrauen: deutsches Feinkost-Traditionsunternehmen statt "
            "namenloser Beauty-Drink. Genau das Signal, das bei einem neuen Produkt den Kauf "
            "absichert."
        ),
    ),
]


MODULES = [
    AIModule(
        name="Modul 1 — Markenbanner",
        role="a+_banner",
        headline="BEAUTY BEGINNT VON INNEN.",
        body=(
            "Der Madame Chéri Kollagen Shot ist dein tägliches Beauty-Ritual von innen: 10 g "
            "Kollagen (Typ 1 &amp; 3) pro Portion, mit Zink, Selen, Folsäure &amp; B6. "
            "Trinkfertig im 50-ml-Format, Geschmack Tropische Früchte."
        ),
        visual="Breites Banner: Kollagen-Flasche rechts vor Beere/Pink mit schwebenden tropischen Frucht-Bubbles, links grosse Serif-Headline auf cremeweiss. Logo oben links.",
        alt="Madame Chéri Kollagen Shot vor Beere-Hintergrund mit tropischen Früchten als tägliches Beauty-Ritual von innen.",
    ),
    AIModule(
        name="Modul 2 — Karussell (5 Kacheln): Warum Kollagen Shot",
        role="a+_carousel",
        headline="WARUM KOLLAGEN SHOT",
        body=(
            "Kachel 1: <b>10 G KOLLAGEN</b> — Typ 1 &amp; 3, 500 Da Kollagen-Tripeptid.<br/>"
            "Kachel 2: <b>ZINK</b> — trägt zur Erhaltung normaler Haut, Haare &amp; Nägel bei.<br/>"
            "Kachel 3: <b>SELEN</b> — trägt zur Erhaltung normaler Haare &amp; Nägel bei.<br/>"
            "Kachel 4: <b>FOLSÄURE &amp; B6</b> — Zellteilung &amp; normaler Energiestoffwechsel.<br/>"
            "Kachel 5: <b>TROPISCHE FRÜCHTE</b> — Kiwi, Mango, Erdbeere &amp; Ananas, 0 g Zucker."
        ),
        visual="5 quadratische Kacheln, dunkelgrüne Akzentecke, weisse Outline-Icons, je eine Zeile Text.",
        alt="Fünf A+ Kacheln zum Kollagen Shot: 10 g Kollagen, Zink, Selen, Folsäure & B6, tropische Früchte.",
    ),
    AIModule(
        name="Modul 3 — Banner: Der Kollagen-Fakt",
        role="a+_banner",
        headline="10 G KOLLAGEN, TYP 1 & 3.",
        body=(
            "Pro Portion 10 g Kollagen: Typ 1 &amp; 3 als niedermolekulares 500 Da "
            "Kollagen-Tripeptid — klar deklariert und trinkfertig statt Pulver-Anrühren. "
            "Reine Fakten, kein Kleingedrucktes."
        ),
        visual="Banner mit grossem Fakt-Chip '10 g Kollagen · Typ 1 & 3 · 500 Da Tripeptid', Flasche rechts, tropische Früchte gestreut.",
        alt="A+ Banner mit dem Kollagen-Fakt: 10 g Kollagen, Typ 1 & 3, 500 Da Tripeptid pro Portion.",
    ),
    AIModule(
        name="Modul 4 — Banner: Das Ritual",
        role="a+_banner",
        headline="DEIN TÄGLICHER BEAUTY-MOMENT.",
        body=(
            "In jede Routine integrierbar: morgens, im Büro oder unterwegs. Vor dem Trinken "
            "gut schütteln und pur genießen — Geschmack Tropische Früchte, 0 g Zucker. "
            "Strahlend durch den Tag."
        ),
        visual="Banner mit ruhigen Alltagsszenen (Waschtisch morgens, Schreibtisch, unterwegs), Flasche im Vordergrund, tropische Früchte, warmes Tageslicht.",
        alt="A+ Banner mit dem Kollagen Shot als tägliches Beauty-Ritual mit Geschmack Tropische Früchte.",
    ),
    AIModule(
        name="Modul 5 — Karussell (6 Kacheln): Die Daily-Shot-Linie",
        role="a+_carousel",
        headline="DIE MADAME CHÉRI DAILY SHOTS",
        body=(
            "Kachel 1: <b>KOLLAGEN</b> — Beauty von innen, 10 g Kollagen (dieses Produkt).<br/>"
            "Kachel 2: <b>DETOX</b> — Fruchtiges Frische-Ritual mit grünem Apfelessig.<br/>"
            "Kachel 3: <b>BROMELAIN</b> — Ananas &amp; Vitamin C, B2, B6.<br/>"
            "Kachel 4: <b>MAGNESIUM</b> — Für Muskeln, Nerven &amp; Energie.<br/>"
            "Kachel 5: <b>GINSENG</b> — Fokus-Ritual, Tradition trifft Moderne.<br/>"
            "Kachel 6: <b>GINGER</b> — Scharf, frisch, der Kick am Morgen."
        ),
        visual="6 Flaschen in ihren Farbwelten, einheitliche Komposition, Kollagen deutlich hervorgehoben. Dachclaim 'Daily Shots. Daily Benefits.'",
        alt="A+ Karussell mit allen sechs Madame Chéri Daily Shots in ihren Farbwelten, Kollagen hervorgehoben.",
    ),
    AIModule(
        name="Modul 6 — Premium Q&A",
        role="a+_qa",
        headline="HÄUFIGE FRAGEN",
        body=(
            "<b>F.</b> Wie viel Kollagen ist enthalten?<br/>"
            "<b>A.</b> 10 g pro Portion — Kollagen Typ 1 &amp; 3 als 500 Da "
            "Kollagen-Tripeptid.<br/><br/>"
            "<b>F.</b> Was bewirken Zink und Selen?<br/>"
            "<b>A.</b> Zink trägt zur Erhaltung normaler Haut, Haare und Nägel bei; Selen zur "
            "Erhaltung normaler Haare und Nägel.<br/><br/>"
            "<b>F.</b> Wie schmeckt der Shot?<br/>"
            "<b>A.</b> Nach Tropischen Früchten (Kiwi, Mango, Erdbeere &amp; Ananas) — "
            "fruchtig-frisch, mit 0 g Zucker.<br/><br/>"
            "<b>F.</b> Wie wird er getrunken?<br/>"
            "<b>A.</b> Vor dem Trinken gut schütteln und pur genießen — ganz nach deiner "
            "Routine.<br/><br/>"
            "<b>F.</b> Wie viele sind enthalten?<br/>"
            "<b>A.</b> 10 Fläschchen à 50 ml — dein Vorrat für zwei Wochen tägliches Ritual."
        ),
        visual="Vertikale Frage-/Antwort-Liste, dunkelgrüne Trennlinien, F. in Grün und A. in Gold. Kurze Antworten.",
        alt="Premium Q&A Modul mit fünf Kurzantworten zum Madame Chéri Kollagen Shot.",
    ),
    AIModule(
        name="Modul 7 — Premium Vergleichstabelle",
        role="a+_comparison",
        headline="DER SMARTE WEG ZUM GLOW",
        body=(
            "Vier Spalten: <b>Madame Chéri Kollagen Shot</b> · Kollagen-Pulver · Kollagen-Kapseln "
            "· Creme von außen.<br/><br/>"
            "Zeilen: Trinkfertig in 50 ml · 10 g Kollagen pro Portion (Typ 1 &amp; 3) · "
            "Zusätzlich Zink, Selen, Folsäure &amp; B6 · Geschmack Tropische Früchte · Kein "
            "Anrühren oder Dosieren · Praktisch für unterwegs.<br/><br/>"
            "Die Kollagen-Shot-Spalte in Beere/Pink hervorheben, Band 'DAILY SHOTS'. "
            "Vergleichsspalten nur als Kategorie, keine Fremdmarken."
        ),
        visual="Standard Amazon Premium Vergleichstabelle, 4 Spalten, Kopfzeile dunkelgrün, Kollagen-Shot-Spalte in Beere/Pink hinterlegt.",
        alt="Premium Vergleichstabelle Kollagen Shot gegenüber Kollagen-Pulver, Kapseln und Creme von außen.",
    ),
]


QA = [
    AIQA(q="Wie viel Kollagen steckt in einem Shot?",
         a="10 g Kollagen pro Portion — Kollagen Typ 1 und 3 als niedermolekulares 500 Da Kollagen-Tripeptid, klar deklariert und trinkfertig."),
    AIQA(q="Was bewirken Zink und Selen im Shot?",
         a="Zink trägt zur Erhaltung normaler Haut, Haare und Nägel bei. Selen trägt zur Erhaltung normaler Haare und Nägel bei."),
    AIQA(q="Wofür sind Folsäure und Vitamin B6 enthalten?",
         a="Folsäure hat eine Funktion bei der Zellteilung. Vitamin B6 trägt zu einem normalen Energiestoffwechsel bei."),
    AIQA(q="Wie schmeckt der Kollagen Shot?",
         a="Nach Tropischen Früchten mit Kiwi, Mango, Erdbeere und Ananas — fruchtig-frisch und mit 0 g Zucker."),
    AIQA(q="Wie trinke ich den Shot am besten?",
         a="Vor dem Trinken gut schütteln und pur genießen. Ob morgens, im Büro oder unterwegs — ganz nach deiner Routine."),
    AIQA(q="Wie viele Shots sind in der Box?",
         a="Die Box enthält 10 Fläschchen à 50 ml — dein Vorrat für rund zwei Wochen tägliches Beauty-Ritual."),
    AIQA(q="Von wem ist der Kollagen Shot?",
         a="Von Madame Chéri, einem deutschen Feinkost-Traditionsunternehmen. Teil der Daily-Shot-Linie 'Daily Shots. Daily Benefits.'"),
]


BACKEND = (
    "kollagen shot collagen shot kollagen trinken kollagen hochdosiert beauty shot kollagen "
    "tripeptid zink selen shot kollagen typ 1 3 collagen drink hautpflege von innen kollagen "
    "fluessig folsaeure shot kollagen 10g tropische fruechte kiwi mango erdbeere ananas b6 "
    "50ml 10er box madame cheri feinkost beauty ritual"
)


def main() -> None:
    print("Lade Madame Chéri + Kollagen-Achse…")
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
