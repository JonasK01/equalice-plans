"""Madame Chéri — GINGER SHOT (50 ml, 10er-Box)
Hand-written, KW-led, conversion-focused copy im Feinkost-Look.

Marketplace: amazon.de (DE) — deutsche Overlays + Kunden-Copy.
Produkt 206 · Marke: Madame Chéri (Feinkost). Listing noch nicht live.

Positionierung: intensiver Ingwer-Shot — der würzig-frische KICK am Morgen.
Farbwelt: kräftiges Orange, frisch & energiegeladen. Held: 50-ml-Flasche + 10er-Box,
frische Ingwerknollen, Zitrone, Spritzer.

COMPLIANCE (wichtig): Ingwer-Shot OHNE zugesetzte Vitamine — es gibt KEINE zugelassenen
Nährstoff-Health-Claims. Daher rein über GESCHMACK, Schärfe, Intensität, Ritual und das
'Kick'-GEFÜHL kommunizieren (wie viele Ingwer-Shot-Wettbewerber), aber OHNE konkrete
Wirk-/Heilaussage. VERBOTEN: 'stärkt Immunsystem', 'gegen Erkältung', 'hilft bei Übelkeit',
Verdauungs-/Heilaussagen, 'entzündungshemmend', 'beste/Nr.1/garantiert', Abnehmversprechen,
Preise/URLs. 'Kick'/'kraftvoll' nur als Geschmacks-/Stimmungsbild, nie als versprochene Wirkung.
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

PLAN_NO = "206"
ASIN = ""   # noch nicht live


BRIEF = ParsedBrief(
    product_name="Madame Chéri Ginger Shot · 10 x 50 ml",
    brand="Madame Chéri",
    marketplace="amazon.de",
    category="Lebensmittel & Getränke > Nahrungsergänzung > Functional Shots",
    main_keywords=["ingwer shot", "ginger shot", "ingwershot"],
    all_keywords=[
        "ingwer shot", "ginger shot", "ingwershot", "ingwer scharf", "ingwer pur",
        "morgen shot", "ingwer getränk", "shots", "daily shot", "ingwer intensiv",
        "ginger shot ohne zusatz", "wellness shot", "ingwer kick", "shot flaschen",
        "ingwer shot ohne zusatz", "shots set", "ingwer shot scharf", "functional shot",
    ],
    usps=[
        "Intensiver Ingwergeschmack — scharf, frisch, unverwechselbar.",
        "Wenige Zutaten, viel Charakter: Ingwer in seiner stärksten Form.",
        "Der würzig-frische Kick für einen kraftvollen Start in den Tag.",
        "Praktisches 50-ml-Format für unterwegs, Büro und Morgenroutine.",
        "10er-Box — der Vorrat für zwei Wochen tägliches Ingwer-Ritual.",
        "Premium-Feinkost von Madame Chéri, deutsches Traditionsunternehmen.",
    ],
    target_group=(
        "Wellness-, ernährungs- und lifestylebewusste Frauen und Männer, die es authentisch "
        "mögen und ihren Tag mit einem würzig-frischen Ingwer-Ritual kraftvoll starten wollen."
    ),
    target_problems=(
        "Ingwer selbst schälen und pressen ist aufwendig und scharf an den Händen, Ingwertee "
        "dauert. Gesucht wird ein sofort trinkfertiger, intensiver Ingwer-Shot für jeden Tag."
    ),
    good_reviews=[
        "Schön scharf und intensiv — schmeckt nach echtem Ingwer, nicht verdünnt.",
        "Praktisch für morgens, kein Schälen und Pressen mehr.",
        "Angenehmer Kick am Morgen, würzig-frisch.",
    ],
    bad_reviews=[
        "Ingwer ist Geschmackssache — für empfindliche Zungen wirklich scharf.",
    ],
)


# ===== Copy (Deutsch, Feinkost) — Ginger: nur Geschmack/Schärfe/Ritual, KEINE Health-Claims =====

TITLE = ('Madame Chéri Ginger Shot · 10 x 50 ml — Intensiver Ingwer Shot, scharf & frisch · '
         'wenige Zutaten, viel Charakter · der würzig-frische Kick für deine Morgenroutine, '
         'praktisch für jeden Tag')

BULLETS = [
    "<b>DEIN INTENSIVER INGWER-KICK AM MORGEN</b> — Ein würzig-frischer Shot, der wach "
    "schmeckt: kräftiger Ingwer, sofort trinkfertig. Der kraftvolle Start in den Tag — ohne "
    "Schälen, ohne Pressen, einfach aufdrehen und den Kick genießen.",

    "<b>SCHARF, FRISCH, UNVERWECHSELBAR</b> — Ingwer in seiner stärksten Form: intensiv, "
    "würzig und ehrlich scharf. Für alle, die es authentisch mögen und echten Ingwergeschmack "
    "einem verdünnten Getränk vorziehen.",

    "<b>WENIGE ZUTATEN, VIEL CHARAKTER</b> — Der Klassiker mit Charakter: puristisch "
    "komponiert, damit der Ingwer im Mittelpunkt steht. Pure Schärfe, echter Geschmack — "
    "unaufgeregt und geradlinig.",

    "<b>IMMER DABEI, KICK FÜR UNTERWEGS</b> — Das handliche 50-ml-Format passt in jede Tasche: "
    "für Büro, Sport, Reise oder direkt nach dem Aufstehen. Vor dem Trinken kurz schütteln — "
    "fertig ist dein würziger Moment.",

    "<b>10ER-BOX VON MADAME CHÉRI FEINKOST</b> — Zehn Shots im edlen Display — dein Vorrat für "
    "zwei Wochen tägliches Ingwer-Ritual oder zum Ausprobieren und Teilen. Premium-Feinkost aus "
    "einem deutschen Traditionsunternehmen.",
]


IMAGES = [
    AIImagePlanItem(
        name="Bild 1 — Main Hero (3 Varianten für A/B-Test)",
        role="hero",
        background="Kräftiges, frisches Orange mit hellem Verlauf (Ginger-Farbwelt), passend zum Etikett. Bei allen 3 Varianten identisch für einen sauberen Split-Test.",
        purpose="Klick gewinnen im Shot-Raster — sofort erkennbar als intensiver, premium Ingwer-Shot.",
        visual=(
            "Alle 3 Varianten mocken, Sieger behalten. Feinkost-Look: Madame-Chéri-Logo oben "
            "links, dunkelgrüner runder Badge 'Deutsches Traditionsunternehmen', Mengen-Schild "
            "'10 Stück' in Orange. Produkt exakt wie real (klare 50-ml-Flasche, weisser Deckel, "
            "orange-graues Etikett 'Ginger Shot'). Amazon-Slot 1 bleibt produktfrei von Text — "
            "dies sind die CTR-Mains für den A/B-Test.\n\n"

            "VARIANTE A — DER KICK (Emotion)\n"
            "Flasche mittig auf einem orangen Podest, ringsum ein frischer Spritzer, fliegende "
            "Ingwer-Scheiben und ein Zitronenschnitz, energiegeladene Bewegung — der würzig-"
            "frische Moment eingefroren.\n"
            "BADGE (Serif, weiss auf orangem Block): 'DER KICK AM MORGEN'.\n"
            "Gewinnt, weil es Energie + Frische in einem Blick zeigt.\n\n"

            "VARIANTE B — DIE 10ER-BOX (Wert)\n"
            "Die geöffnete 10er-Display-Box mit sichtbaren Fläschchen, zwei Shots davor, frische "
            "Ingwerknollen daneben.\n"
            "BADGE: '10 SHOTS · 2 WOCHEN RITUAL'.\n"
            "Gewinnt, weil es Menge und Vorrat sofort klarmacht.\n\n"

            "VARIANTE C — INTENSIVER INGWER, PUR (Fakt)\n"
            "Flasche freigestellt, daneben frische Ingwerknolle im Anschnitt und ein Zitronen-"
            "schnitz — puristisch, ehrlich, intensiv.\n"
            "BADGE: 'INTENSIVER INGWER · PUR'.\n"
            "Gewinnt, weil purer, authentischer Ingwer der stärkste rationale Hook ist.\n\n"

            "Über alle 3: Flasche dominant, Badge ca. 6 % der Fläche, gleiche Lichtstimmung."
        ),
        overlay="(eine Aussage je Variante)",
        overlay_sub="3 Hero-Varianten — A/B testen, Sieger behalten.",
        props=[
            "A: Flasche + Spritzer + fliegende Ingwer-Scheiben + Zitrone",
            "B: geöffnete 10er-Box + 2 Shots + frische Ingwerknollen",
            "C: freigestellte Flasche + Ingwerknolle im Anschnitt + Zitrone",
        ],
        lighting="Hell, frisch, appetitlich; weiche Schatten. Bei allen 3 identisch für den Split-Test.",
        why_it_works=(
            "Drei Auslöser: A verkauft das Gefühl (der Kick am Morgen), B den Vorrat/Wert, C den "
            "rationalen Hook (intensiver, purer Ingwer). Je eine Aussage — auf dem Thumbnail "
            "sofort lesbar."
        ),
    ),
    AIImagePlanItem(
        name="Bild 2 — Geschmack & Intensität",
        role="hook",
        background="Cremeweiss #F0EADD mit dunkelgrünem Serif-Headline-Block oben rechts (Feinkost-Chrome)",
        purpose="In einem Bild zeigen, wie intensiv und scharf-frisch der Shot schmeckt.",
        visual=(
            "Flasche mittig, umgeben von frisch inszeniertem Ingwer: Ingwerknolle im Anschnitt, "
            "dünne Ingwer-Scheiben, ein Zitronenschnitz und ein feiner Spritzer. Rechts eine "
            "dezente Schärfe-Skala als STIMMUNGSBILD (drei kleine Ingwer-Symbole gefüllt, "
            "'intensiv') — rein illustrativ für den Geschmack, KEINE Wirkaussage.\n\n"
            "Headline-Block oben: 'Scharf. Frisch. Intensiv.' Feine Verbindungslinien vom "
            "frischen Ingwer zur Flasche."
        ),
        overlay="SCHARF. FRISCH. INTENSIV.",
        overlay_sub="Kräftiger Ingwergeschmack mit echter Schärfe — authentisch und frisch.",
        props=["Flasche", "Ingwerknolle im Anschnitt", "Ingwer-Scheiben", "Zitronenschnitz", "Schärfe-Skala (Stimmungsbild)", "Spritzer"],
        lighting="Helles, gleichmässiges Food-Licht. Appetitlich und klar.",
        why_it_works=(
            "Bei einem Ingwer-Shot ist Intensität das Kaufargument. Frischen Ingwer und eine "
            "geschmackliche Schärfe-Skala sichtbar zu machen, kommuniziert genau die Erwartung "
            "'schmeckt kräftig und echt' — ohne jede Wirkaussage."
        ),
        cvr="Adressiert die zentrale Frage beim Ingwer-Shot: 'ist der schön intensiv?'",
    ),
    AIImagePlanItem(
        name="Bild 3 — Warum kaufen: wenige Zutaten, viel Charakter",
        role="educate",
        background="Kräftiges Orange, heller Verlauf",
        purpose="Den rationalen Kaufgrund verankern: puristisch, authentisch, echter Ingwergeschmack.",
        visual=(
            "Freigestellte Flasche links, rechts drei ruhige Fakt-Kacheln mit Outline-Icons:\n"
            "  • WENIGE ZUTATEN — Ingwer im Mittelpunkt\n"
            "  • PUR & AUTHENTISCH — echter Ingwergeschmack\n"
            "  • SOFORT TRINKFERTIG — kein Schälen, kein Pressen\n\n"
            "Kleiner Nährwert-Hinweis dezent am Fuss (pro 100 ml: 46 kcal, Zucker 6,42 g). "
            "Ehrlich und unaufgeregt — keine Wirkversprechen, nur klare Fakten und Geschmack."
        ),
        overlay="PUR UND AUTHENTISCH.",
        overlay_sub="Wenige Zutaten, viel Charakter — intensiver Ingwer, ehrlich und pur.",
        props=["freigestellte Flasche", "3 Fakt-Kacheln", "dezenter Nährwert-Hinweis"],
        lighting="Hell und frisch, klarer Fokus auf der Flasche.",
        why_it_works=(
            "Purer, authentischer Ingwer ist der stärkste rechtlich sichere Kaufgrund. Ehrliche "
            "Fakten statt Heilversprechen passen zur Premium-Positionierung und schaffen Vertrauen."
        ),
    ),
    AIImagePlanItem(
        name="Bild 4 — Das Ritual im Alltag",
        role="desire",
        background="Helle, moderne Küche / Schreibtisch am Morgen, warmes Tageslicht",
        purpose="Den Shot in den Alltag der Zielgruppe setzen — den Kick am Morgen sichtbar machen.",
        visual=(
            "Lifestyle-Szene: eine Frau (oder Hände, elegant, ohne Gesichtsfokus) hält den "
            "geöffneten Ginger Shot am hellen Küchentresen oder Schreibtisch, daneben ein Glas "
            "Wasser, frische Ingwerknolle und ein Zitronenschnitz, im Hintergrund weich ein "
            "Morgen-Setting. Ruhig, premium, echt — kein Studio-Pharma-Look.\n\n"
            "Kleiner Hinweis-Chip: 'Vor dem Trinken kurz schütteln.'"
        ),
        overlay="DER KICK AM MORGEN.",
        overlay_sub="Aufdrehen, schütteln, genießen — dein würzig-frischer Start in den Tag.",
        props=["Person/Hände mit Shot", "Glas Wasser", "frische Ingwerknolle & Zitrone", "helles Morgen-Setting", "Schüttel-Hinweis"],
        lighting="Warmes, weiches Morgenlicht von der Seite. Aspirational, aber echt.",
        why_it_works=(
            "Verkauft das Gefühl, nicht nur die Flasche: der würzig-frische, wache Start in den "
            "Tag. Das tägliche Ritual macht aus einem Einzelkauf eine Routine — und damit "
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
            "  • GINGER (orange, dieses Produkt) · DETOX (grün) · BROMELAIN (gelb) · KOLLAGEN "
            "(pink) · MAGNESIUM (blau) · GINSENG (bernstein)\n\n"
            "Der Ginger-Shot dezent hervorgehoben (leichter Rahmen/Podest). Darunter der "
            "Dachclaim 'Daily Shots. Daily Benefits.'"
        ),
        overlay="EIN RITUAL, SECHS SORTEN.",
        overlay_sub="Entdecke die Madame Chéri Daily Shots — für jeden Tag die passende.",
        props=["6 Flaschen in Farbwelten", "Ginger hervorgehoben", "Dachclaim-Leiste"],
        lighting="Helles, gleichmässiges Studiolicht; jede Farbwelt klar erkennbar.",
        why_it_works=(
            "Zeigt Sortiments-Tiefe und Marken-System. Wer den Ginger kauft, sieht sofort die "
            "nächsten Sorten für andere Momente — starker Cross-Sell-Hebel für die neue Linie."
        ),
    ),
    AIImagePlanItem(
        name="Bild 6 — Format & Handling",
        role="desire",
        background="Kräftiges Orange, hell",
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
            "Ruhige, edle Aufnahme: die Ginger-Flasche und die 10er-Box sauber arrangiert, frische "
            "Ingwerknolle und ein Zitronenschnitz dezent, viel Weissraum. Madame-Chéri-Logo "
            "mittig, darunter der dunkle runde Badge 'Deutsches Traditionsunternehmen' und der "
            "Dachclaim 'Daily Shots. Daily Benefits.'\n\n"
            "Ton: premium, warm, ruhig — Feinkost, keine Superlative."
        ),
        overlay="FEINKOST FÜR JEDEN TAG.",
        overlay_sub="Madame Chéri — Daily Shots, Daily Benefits. Deutsches Traditionsunternehmen.",
        props=["Flasche + 10er-Box arrangiert", "frische Ingwerknolle & Zitrone", "Logo", "Deutsches-Traditionsunternehmen-Badge", "Dachclaim"],
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
        headline="DER KLASSIKER MIT CHARAKTER.",
        body=(
            "Der Madame Chéri Ginger Shot ist der würzig-frische Start in den Tag: intensiver "
            "Ingwer, scharf und ehrlich, sofort trinkfertig. Wenige Zutaten, viel Charakter — "
            "praktisch im 50-ml-Format."
        ),
        visual="Breites Banner: Ginger-Flasche rechts vor kräftigem Orange mit frischem Spritzer und fliegenden Ingwer-Scheiben, links grosse Serif-Headline auf cremeweiss. Logo oben links.",
        alt="Madame Chéri Ginger Shot vor kräftigem Orange mit frischem Ingwer als würziges Morgen-Ritual.",
    ),
    AIModule(
        name="Modul 2 — Karussell (5 Kacheln): Warum Ginger Shot",
        role="a+_carousel",
        headline="WARUM GINGER SHOT",
        body=(
            "Kachel 1: <b>SCHARF &amp; FRISCH</b> — Intensiver Ingwer, ehrlich würzig.<br/>"
            "Kachel 2: <b>WENIGE ZUTATEN</b> — Viel Charakter, Ingwer im Mittelpunkt.<br/>"
            "Kachel 3: <b>DER KICK AM MORGEN</b> — Würzig-frischer Start in den Tag.<br/>"
            "Kachel 4: <b>SOFORT TRINKFERTIG</b> — Kein Schälen, kein Pressen.<br/>"
            "Kachel 5: <b>10ER-BOX</b> — Der Vorrat für zwei Wochen Ritual."
        ),
        visual="5 quadratische Kacheln, dunkelgrüne Akzentecke, weisse Outline-Icons, je eine Zeile Text.",
        alt="Fünf A+ Kacheln zum Ginger Shot: scharf & frisch, wenige Zutaten, Kick am Morgen, sofort trinkfertig, 10er-Box.",
    ),
    AIModule(
        name="Modul 3 — Banner: Pure Schärfe",
        role="a+_banner",
        headline="PURE SCHÄRFE. ECHTER GESCHMACK.",
        body=(
            "Ingwer in seiner stärksten Form: intensiv, würzig und unverwechselbar. Puristisch "
            "komponiert, damit der Ingwer im Mittelpunkt steht — authentischer Geschmack für "
            "alle, die es echt mögen."
        ),
        visual="Banner mit frischer Ingwerknolle im Anschnitt, Ingwer-Scheiben und Zitronenschnitz rund um die Flasche rechts, feiner Spritzer, kräftiges Orange.",
        alt="A+ Banner mit purem, intensivem Ingwer rund um den Ginger Shot.",
    ),
    AIModule(
        name="Modul 4 — Banner: Das Ritual",
        role="a+_banner",
        headline="DER KICK AM MORGEN.",
        body=(
            "In jede Routine integrierbar: morgens nach dem Aufstehen, im Büro oder vor dem "
            "Sport. Vor dem Trinken kurz schütteln — fertig ist dein würzig-frischer Moment. "
            "Sofort trinkfertig, ganz ohne Schälen und Pressen."
        ),
        visual="Banner mit drei ruhigen Alltagsszenen (Küche morgens, Schreibtisch, Sporttasche), Ginger-Flasche im Vordergrund, warmes Tageslicht.",
        alt="A+ Banner mit dem Ginger Shot als würziges Ritual in Küche, Büro und beim Sport.",
    ),
    AIModule(
        name="Modul 5 — Karussell (6 Kacheln): Die Daily-Shot-Linie",
        role="a+_carousel",
        headline="DIE MADAME CHÉRI DAILY SHOTS",
        body=(
            "Kachel 1: <b>GINGER</b> — Scharf, frisch, der Kick am Morgen (dieses Produkt).<br/>"
            "Kachel 2: <b>DETOX</b> — Fruchtiges Frische-Ritual mit Apfelessig.<br/>"
            "Kachel 3: <b>BROMELAIN</b> — Ananas &amp; Vitamin C, B2, B6.<br/>"
            "Kachel 4: <b>KOLLAGEN</b> — Beauty von innen, mit Zink &amp; Selen.<br/>"
            "Kachel 5: <b>MAGNESIUM</b> — Für Muskeln, Nerven &amp; Energie.<br/>"
            "Kachel 6: <b>GINSENG</b> — Fokus-Ritual, Tradition trifft Moderne."
        ),
        visual="6 Flaschen in ihren Farbwelten, einheitliche Komposition, Ginger dezent hervorgehoben. Dachclaim 'Daily Shots. Daily Benefits.'",
        alt="A+ Karussell mit allen sechs Madame Chéri Daily Shots in ihren Farbwelten.",
    ),
    AIModule(
        name="Modul 6 — Premium Q&A",
        role="a+_qa",
        headline="HÄUFIGE FRAGEN",
        body=(
            "<b>F.</b> Wie schmeckt der Shot?<br/>"
            "<b>A.</b> Intensiv und scharf-frisch: kräftiger, echter Ingwer — puristisch, ohne "
            "verdünnten Beigeschmack.<br/><br/>"
            "<b>F.</b> Wie scharf ist der Ingwer?<br/>"
            "<b>A.</b> Deutlich würzig — Ingwer in seiner stärksten Form. Für alle, die "
            "authentischen Ingwergeschmack mögen.<br/><br/>"
            "<b>F.</b> Wie wird er getrunken?<br/>"
            "<b>A.</b> Vor dem Trinken kurz schütteln und pur genießen — jederzeit, ganz nach "
            "deiner Routine.<br/><br/>"
            "<b>F.</b> Wie viele sind enthalten?<br/>"
            "<b>A.</b> 10 Fläschchen à 50 ml — der Vorrat für zwei Wochen tägliches Ritual.<br/><br/>"
            "<b>F.</b> Von wem ist der Shot?<br/>"
            "<b>A.</b> Von Madame Chéri Feinkost, einem deutschen Traditionsunternehmen."
        ),
        visual="Vertikale Frage-/Antwort-Liste, dunkelgrüne Trennlinien, F. in Grün und A. in Gold. Kurze Antworten.",
        alt="Premium Q&A Modul mit fünf Kurzantworten zum Madame Chéri Ginger Shot.",
    ),
    AIModule(
        name="Modul 7 — Premium Vergleichstabelle",
        role="a+_comparison",
        headline="DER SMARTE WEG ZUM INGWER-RITUAL",
        body=(
            "Vier Spalten: <b>Madame Chéri Ginger Shot</b> · Ingwer selbst pressen · Ingwertee · "
            "Ingwerkapseln.<br/><br/>"
            "Zeilen: Intensiver Ingwergeschmack · Sofort trinkfertig · Kein Schälen / kein "
            "Pressen · Praktisch für unterwegs · Wenige Zutaten · Scharf-frisches Ritual.<br/><br/>"
            "Die Ginger-Spalte orange hervorheben, Band 'DAILY SHOTS'. Vergleichsspalten nur als "
            "Kategorie/Format, keine Fremdmarken, keine Wirkversprechen — nur Geschmack, Ritual, "
            "Format und Aufwand."
        ),
        visual="Standard Amazon Premium Vergleichstabelle, 4 Spalten, Kopfzeile dunkelgrün, Ginger-Spalte hellorange hinterlegt.",
        alt="Premium Vergleichstabelle Ginger Shot gegenüber selbst pressen, Ingwertee und Ingwerkapseln.",
    ),
]


QA = [
    AIQA(q="Wie schmeckt der Ginger Shot?",
         a="Intensiv und scharf-frisch. Kräftiger, echter Ingwer, puristisch komponiert — würzig und unverwechselbar, ohne verdünnten Beigeschmack."),
    AIQA(q="Wie scharf ist der Shot?",
         a="Deutlich würzig-scharf — Ingwer in seiner stärksten Form. Genau richtig für alle, die authentischen, kräftigen Ingwergeschmack mögen."),
    AIQA(q="Welche Zutaten sind enthalten?",
         a="Wenige Zutaten, viel Charakter: intensiver Ingwer steht im Mittelpunkt. Pro 100 ml rund 46 kcal, Zucker 6,42 g. Details stehen auf dem Etikett."),
    AIQA(q="Wie trinke ich den Shot am besten?",
         a="Vor dem Trinken kurz schütteln und pur genießen. Ob morgens, im Büro oder vor dem Sport — ganz nach deiner Routine."),
    AIQA(q="Wie viele Shots sind in der Box?",
         a="Die Box enthält 10 Fläschchen à 50 ml — dein Vorrat für rund zwei Wochen tägliches Ingwer-Ritual."),
    AIQA(q="Muss der Shot gekühlt werden?",
         a="Ungeöffnet ist er praktisch für Vorrat und unterwegs. Details zur Lagerung stehen auf dem Etikett; angebrochen kühl stellen und zeitnah genießen."),
    AIQA(q="Von wem ist der Ginger Shot?",
         a="Von Madame Chéri, einem deutschen Feinkost-Traditionsunternehmen. Teil der Daily-Shot-Linie 'Daily Shots. Daily Benefits.'"),
]


BACKEND = (
    "ingwer shot ginger shot ingwershot ingwer scharf ingwer pur ingwer intensiv morgen shot "
    "daily shot wellness shot functional shot ingwer getraenk shots shot flaschen ingwer kick "
    "ingwer shot ohne zusatz ritual morgenroutine unterwegs 50ml 10er box madame cheri feinkost"
)


def main() -> None:
    print("Lade Madame Chéri + Ginger-Achse…")
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
