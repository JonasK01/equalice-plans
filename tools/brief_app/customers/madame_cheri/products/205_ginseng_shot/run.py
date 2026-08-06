"""Madame Chéri — GINSENG SHOT (50 ml, 10er-Box)
Hand-written, KW-led, conversion-focused copy im Feinkost-Look.

Marketplace: amazon.de (DE) — deutsche Overlays + Kunden-Copy.
Produkt 205 · Marke: Madame Chéri (Feinkost). Listing noch nicht live.

Positionierung: edles tägliches FOKUS-RITUAL mit Ginseng. 'Tradition trifft Moderne.'
Farbwelt: warmes Bernstein/Gold, ruhig, fokussiert. Held: 50-ml-Flasche + 10er-Box.

COMPLIANCE (SEHR wichtig): Für Ginseng gibt es in der EU KAUM/KEINE zugelassenen
Health-Claims. Daher AUSSCHLIESSLICH über Lifestyle, Ritual, das Fokus-GEFÜHL,
Tradition, Genuss und Natürlichkeit kommunizieren — wie beim Detox-Muster.
KEINE Wirkaussagen (steigert Konzentration, mehr Energie/Leistung, stärkt, gegen
Müdigkeit, Immunsystem, Krankheits-/Heilbezug). 'Fokus' NUR als stimmungshaftes
Ritual-Wording ('dein Fokus-Moment'), NIE als versprochene Wirkung. Zucker/Kalorien
NICHT heroisieren. Kein 'beste/Nr.1/garantiert', keine Preise/URLs.
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

PLAN_NO = "205"
ASIN = ""   # noch nicht live


BRIEF = ParsedBrief(
    product_name="Madame Chéri Ginseng Shot · 10 x 50 ml",
    brand="Madame Chéri",
    marketplace="amazon.de",
    category="Lebensmittel & Getränke > Nahrungsergänzung > Functional Shots",
    main_keywords=["ginseng shot", "shots", "daily shot"],
    all_keywords=[
        "ginseng shot", "ginseng trinken", "ginseng flüssig", "fokus shot",
        "wellness shot", "ginseng extrakt", "roter ginseng", "shots", "daily shot",
        "ritual shot", "ginseng getränk", "functional shot", "ginseng ampullen",
        "shots set", "ginseng shot 50ml", "shot flaschen",
    ],
    usps=[
        "Edles tägliches Fokus-Ritual mit Ginseng.",
        "Tradition trifft Moderne — Ginseng, neu inszeniert für den Alltag.",
        "Natürliche Inspiration für jeden Tag, ruhig und fokussiert.",
        "Praktisches 50-ml-Format für Büro, unterwegs und Morgenroutine.",
        "10er-Box — der Vorrat für zwei Wochen tägliches Ritual.",
        "Premium-Feinkost von Madame Chéri, deutsches Traditionsunternehmen.",
    ],
    target_group=(
        "Wellness-, genuss- und lifestylebewusste Frauen und Männer, die bewusst in den Tag "
        "starten und moderne Routinen mit einem edlen, ruhigen Ritual gestalten möchten."
    ),
    target_problems=(
        "Klassische Ginseng-Kapseln oder -Tees wirken altmodisch und unpraktisch. Gesucht wird "
        "ein modernes, wohlschmeckendes 50-ml-Ritual, das sich schön in den Tag einfügt."
    ),
    good_reviews=[
        "Edler Geschmack und ein schönes, ruhiges Ritual am Morgen.",
        "Praktisch für unterwegs — angenehmer Start in den Tag.",
        "Wertige Aufmachung, schöne Bernstein-Farbe, wirkt hochwertig.",
    ],
    bad_reviews=[
        "Ginseng ist geschmacklich Typsache — für manche etwas herb.",
    ],
)


# ===== Copy (Deutsch, Feinkost) — Ginseng: nur Lifestyle/Ritual/Tradition, KEINE Health-Claims =====

TITLE = ('Madame Chéri Ginseng Shot · 10 x 50 ml — Dein tägliches Fokus-Ritual mit Ginseng · '
         'Tradition trifft Moderne · edler Genuss für bewusste Routinen, praktisch für jeden Tag')

BULLETS = [
    "<b>DEIN TÄGLICHES FOKUS-RITUAL</b> — Ein edler Ginseng Shot, der in jede moderne "
    "Routine passt. Der ruhige, bewusste Moment für dich — einfach aufdrehen, schütteln und "
    "genießen. Natürliche Inspiration für jeden Tag.",

    "<b>TRADITION TRIFFT MODERNE</b> — Ginseng wird seit Generationen geschätzt. Madame Chéri "
    "bringt ihn im praktischen 50-ml-Shot in deinen Alltag: traditionsreiche Wurzel, modern "
    "inszeniert für bewusste Routinen.",

    "<b>EDLER GENUSS, RUHIG &amp; FOKUSSIERT</b> — Warme Bernstein-Farbwelt, klarer Geschmack, "
    "wertige Aufmachung: der Shot als kleiner Genuss-Moment für zwischendurch, der sich schön "
    "in den Tag einfügt.",

    "<b>PRAKTISCH FÜR UNTERWEGS</b> — Das handliche 50-ml-Format passt in jede Tasche: für "
    "Büro, Reise oder direkt nach dem Aufstehen. Vor dem Trinken kurz schütteln — fertig ist "
    "dein Fokus-Moment.",

    "<b>10ER-BOX VON MADAME CHÉRI FEINKOST</b> — Zehn Shots im edlen Display — dein Vorrat für "
    "zwei Wochen tägliches Ritual oder zum Ausprobieren und Teilen. Premium-Feinkost aus einem "
    "deutschen Traditionsunternehmen.",
]


IMAGES = [
    AIImagePlanItem(
        name="Bild 1 — Main Hero (3 Varianten für A/B-Test)",
        role="hero",
        background="Warmes Bernstein/Gold mit weichem Verlauf (Ginseng-Farbwelt), edel und ruhig, passend zum Etikett. Bei allen 3 Varianten identisch für einen sauberen Split-Test.",
        purpose="Klick gewinnen im Shot-Raster — sofort erkennbar als edles, fokussiertes Ritual.",
        visual=(
            "Alle 3 Varianten mocken, Sieger behalten. Feinkost-Look: Madame-Chéri-Logo oben "
            "links, dunkler runder Badge 'Deutsches Traditionsunternehmen', Mengen-Schild "
            "'10 Stück' in Gold/Bernstein. Produkt exakt wie real (klare 50-ml-Flasche, weisser "
            "Deckel, bernstein-goldenes Etikett 'Ginseng Shot'). Amazon-Slot 1 bleibt produktfrei "
            "von Text — dies sind die CTR-Mains für den A/B-Test.\n\n"

            "VARIANTE A — FOKUS-EMOTION (Gefühl)\n"
            "Flasche mittig auf einem edlen Podest, warmes Bernstein-Licht, ruhige goldene "
            "Bokeh-Reflexe, eine frische Ginsengwurzel dezent daneben. Premium, fokussiert, "
            "aufgeräumt.\n"
            "BADGE (Serif, weiss auf dunklem Block): 'DEIN TÄGLICHES FOKUS-RITUAL'.\n"
            "Gewinnt, weil es Ruhe + Premium-Genuss in einem Blick zeigt.\n\n"

            "VARIANTE B — DIE 10ER-BOX (Wert)\n"
            "Die geöffnete 10er-Display-Box mit sichtbaren Fläschchen, zwei Shots davor, eine "
            "Ginsengwurzel daneben.\n"
            "BADGE: '10 SHOTS · 2 WOCHEN RITUAL'.\n"
            "Gewinnt, weil es Menge und Vorrat sofort klarmacht.\n\n"

            "VARIANTE C — TRADITION TRIFFT MODERNE (Marke)\n"
            "Flasche freigestellt, daneben eine ganze Ginsengwurzel und ein feiner "
            "Serif-Schriftzug 'Ginseng · Tradition trifft Moderne'.\n"
            "BADGE: 'TRADITION TRIFFT MODERNE'.\n"
            "Gewinnt, weil Herkunft + Premium der stärkste emotionale Hook für Ginseng ist.\n\n"

            "Über alle 3: Flasche dominant, Badge ca. 6 % der Fläche, gleiche warme Lichtstimmung. "
            "KEINE Wirkaussagen auf dem Bild."
        ),
        overlay="(eine Aussage je Variante)",
        overlay_sub="3 Hero-Varianten — A/B testen, Sieger behalten.",
        props=[
            "A: Flasche auf Podest + Ginsengwurzel + warme Bokeh-Reflexe",
            "B: geöffnete 10er-Box + 2 Shots + Ginsengwurzel",
            "C: freigestellte Flasche + ganze Ginsengwurzel + Serif-Schriftzug",
        ],
        lighting="Warm, edel, ruhig; weiche goldene Schatten. Bei allen 3 identisch für den Split-Test.",
        why_it_works=(
            "Drei Auslöser: A verkauft das Gefühl (edles Fokus-Ritual), B den Vorrat/Wert, C die "
            "Marken-Herkunft (Tradition trifft Moderne). Je eine Aussage — auf dem Thumbnail "
            "sofort lesbar, ganz ohne Wirkversprechen."
        ),
    ),
    AIImagePlanItem(
        name="Bild 2 — Ginseng: Tradition trifft Moderne",
        role="hook",
        background="Cremeweiss #F0EADD mit bernstein-goldenem Serif-Headline-Block oben rechts (Feinkost-Chrome)",
        purpose="Herkunft & Ritual edel inszenieren — Ginseng als traditionsreiche Wurzel, modern im Shot. KEINE Wirkclaims.",
        visual=(
            "Zweiteilige, ruhige Inszenierung. LINKS: eine ganze, schön ausgeleuchtete "
            "Ginsengwurzel auf edlem Untergrund, warme Bernstein-Töne. RECHTS: die Flasche, "
            "dazwischen ein feiner goldener Verbindungsstrich als 'von der Wurzel in den Shot'. "
            "Headline-Block oben: 'Tradition trifft Moderne'.\n\n"
            "Darunter dezent, rein beschreibend (KEINE Wirkung): 'Ginseng — seit Generationen "
            "geschätzt, heute im praktischen 50-ml-Shot.' Ruhig, premium, editorial."
        ),
        overlay="TRADITION TRIFFT MODERNE.",
        overlay_sub="Ginseng — traditionsreiche Wurzel, modern im 50-ml-Shot.",
        props=["ganze Ginsengwurzel", "Flasche", "goldener Verbindungsstrich", "Serif-Headline-Block"],
        lighting="Warmes, weiches Food-Licht mit Goldreflexen. Edel und ruhig.",
        why_it_works=(
            "Statt eines Wirkstoff-Fokus (der bei Ginseng rechtlich nicht bespielbar ist) "
            "verkauft dieses Bild Herkunft, Wertigkeit und Ritual. Die sichtbare Wurzel schafft "
            "Vertrauen und Premium-Anmutung — ganz ohne Health-Claim."
        ),
        cvr="Adressiert das Kaufmotiv 'echtes, traditionsreiches Ginseng' über Herkunft statt Wirkung.",
    ),
    AIImagePlanItem(
        name="Bild 3 — Warum kaufen: das Ritual & Format",
        role="educate",
        background="Warmes Bernstein/Gold, heller Verlauf",
        purpose="Den rationalen Kaufgrund verankern: edles Ritual, praktisches Format, natürlicher Genuss — statt Wirkung.",
        visual=(
            "Freigestellte Flasche links, rechts drei ruhige Fakt-Kacheln mit Outline-Icons:\n"
            "  • 50-ML-RITUAL für jeden Tag\n"
            "  • MIT GINSENG, natürlich inszeniert\n"
            "  • PRAKTISCH für Büro &amp; unterwegs\n\n"
            "Dezenter, neutraler Fuss: 'Nährwertangaben stehen auf dem Etikett.' Ehrlich und "
            "unaufgeregt — keine Wirkversprechen, nur Ritual, Genuss und Format."
        ),
        overlay="DEIN FOKUS-RITUAL.",
        overlay_sub="Ein 50-ml-Ritual mit Ginseng — edler Genuss für jeden Tag.",
        props=["freigestellte Flasche", "3 Fakt-Kacheln (Ritual, Ginseng, praktisch)", "dezenter Etikett-Hinweis"],
        lighting="Warm und klar, ruhiger Fokus auf der Flasche.",
        why_it_works=(
            "Ritual + Format + Genuss ist der stärkste rechtlich sichere Kaufgrund für Ginseng. "
            "Ehrliche Aussagen statt Wirkversprechen passen zur Premium-Positionierung und "
            "schaffen Vertrauen."
        ),
    ),
    AIImagePlanItem(
        name="Bild 4 — Der Fokus-Moment im Alltag",
        role="desire",
        background="Heller, moderner Schreibtisch / Küche am Morgen, warmes Tageslicht",
        purpose="Den Shot in den Alltag der Zielgruppe setzen — den ruhigen Fokus-Moment sichtbar machen.",
        visual=(
            "Lifestyle-Szene: eine Person (oder Hände, elegant, ohne Gesichtsfokus) hält den "
            "geöffneten Ginseng Shot am hellen Schreibtisch oder Küchentresen, daneben ein "
            "Notizbuch, eine Tasse, warmes Morgenlicht, im Hintergrund weich ein modernes "
            "Setting. Ruhig, premium, echt — kein Studio-Pharma-Look.\n\n"
            "Kleiner Hinweis-Chip: 'Vor dem Trinken kurz schütteln.'"
        ),
        overlay="DEIN FOKUS-MOMENT.",
        overlay_sub="Aufdrehen, schütteln, genießen — dein ruhiges Ritual für jeden Tag.",
        props=["Person/Hände mit Shot", "Notizbuch & Tasse", "warmes Morgen-Setting", "Schüttel-Hinweis"],
        lighting="Warmes, weiches Morgenlicht von der Seite. Aspirational, aber echt.",
        why_it_works=(
            "Verkauft das Gefühl, nicht die Wirkung: der bewusste, ruhige Start in den Tag. Das "
            "tägliche Ritual macht aus einem Einzelkauf eine Routine — und damit Wiederkäufe."
        ),
    ),
    AIImagePlanItem(
        name="Bild 5 — Die Shot-Familie von Madame Chéri",
        role="desire",
        background="Cremeweiss #F0EADD mit bernstein-goldenem Headline-Block",
        purpose="Cross-Sell: die ganze Daily-Shot-Linie zeigen, Wiedererkennung der Farbwelten.",
        visual=(
            "Sechs Flaschen der Linie in ihren Farbwelten nebeneinander, jede mit kleinem Label:\n"
            "  • GINSENG (bernstein, dieses Produkt) · DETOX (grün) · BROMELAIN (gelb) · KOLLAGEN "
            "(pink) · MAGNESIUM (blau) · GINGER (orange)\n\n"
            "Der Ginseng-Shot dezent hervorgehoben (leichter Rahmen/Podest). Darunter der "
            "Dachclaim 'Daily Shots. Daily Benefits.'"
        ),
        overlay="EIN RITUAL, SECHS SORTEN.",
        overlay_sub="Entdecke die Madame Chéri Daily Shots — für jeden Tag die passende.",
        props=["6 Flaschen in Farbwelten", "Ginseng hervorgehoben", "Dachclaim-Leiste"],
        lighting="Helles, gleichmässiges Studiolicht; jede Farbwelt klar erkennbar.",
        why_it_works=(
            "Zeigt Sortiments-Tiefe und Marken-System. Wer den Ginseng kauft, sieht sofort die "
            "nächsten Sorten für andere Momente — starker Cross-Sell-Hebel für die neue Linie."
        ),
    ),
    AIImagePlanItem(
        name="Bild 6 — Format & Handling",
        role="desire",
        background="Warmes Bernstein/Gold, hell",
        purpose="Menge, Grösse und Handling klarmachen — letzte Kaufhürde räumen.",
        visual=(
            "Zweiteilig. LINKS: die 10er-Box mit den Fläschchen, Label '10 x 50 ml'. RECHTS: eine "
            "Flasche in der Hand als Grössenreferenz (handlich, taschentauglich) mit drei kleinen "
            "Schritt-Icons: 'Schütteln → Aufdrehen → Genießen'.\n\n"
            "Kleiner Fuss: 'Ungeöffnet haltbar — praktisch für Vorrat und unterwegs.'"
        ),
        overlay="IMMER DABEI.",
        overlay_sub="10 x 50 ml, handlich für Büro & unterwegs — schütteln, aufdrehen, genießen.",
        props=["10er-Box", "Flasche in der Hand (Grössenreferenz)", "3 Schritt-Icons"],
        lighting="Warm und klar, ehrliche Grössen- und Farbwiedergabe.",
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
            "Ruhige, edle Aufnahme: die Ginseng-Flasche und die 10er-Box sauber arrangiert, eine "
            "Ginsengwurzel dezent, viel Weissraum. Madame-Chéri-Logo mittig, darunter der dunkle "
            "runde Badge 'Deutsches Traditionsunternehmen' und der Dachclaim 'Daily Shots. Daily "
            "Benefits.'\n\n"
            "Ton: premium, warm, ruhig — Feinkost, keine Superlative."
        ),
        overlay="FEINKOST FÜR JEDEN TAG.",
        overlay_sub="Madame Chéri — Daily Shots, Daily Benefits. Deutsches Traditionsunternehmen.",
        props=["Flasche + 10er-Box arrangiert", "Ginsengwurzel", "Logo", "Deutsches-Traditionsunternehmen-Badge", "Dachclaim"],
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
        headline="DEIN TÄGLICHER FOKUS-MOMENT.",
        body=(
            "Der Madame Chéri Ginseng Shot ist der edle, ruhige Start in den Tag: Ginseng, modern "
            "inszeniert für bewusste Routinen. Tradition trifft Moderne — praktisch im "
            "50-ml-Format. Natürliche Inspiration für jeden Tag."
        ),
        visual="Breites Banner: Ginseng-Flasche rechts vor warmem Bernstein/Gold mit dezenter Ginsengwurzel, links grosse Serif-Headline auf cremeweiss. Logo oben links.",
        alt="Madame Chéri Ginseng Shot vor warmem Bernstein-Hintergrund mit Ginsengwurzel als tägliches Fokus-Ritual.",
    ),
    AIModule(
        name="Modul 2 — Karussell (5 Kacheln): Warum Ginseng Shot",
        role="a+_carousel",
        headline="WARUM GINSENG SHOT",
        body=(
            "Kachel 1: <b>FOKUS-RITUAL</b> — Dein ruhiger Moment für jeden Tag.<br/>"
            "Kachel 2: <b>TRADITION &amp; MODERNE</b> — Ginseng, neu inszeniert.<br/>"
            "Kachel 3: <b>EDLER GENUSS</b> — Warme Bernstein-Farbwelt, wertig.<br/>"
            "Kachel 4: <b>PRAKTISCH</b> — 50-ml-Format für unterwegs.<br/>"
            "Kachel 5: <b>10ER-BOX</b> — Der Vorrat für zwei Wochen Ritual."
        ),
        visual="5 quadratische Kacheln, bernstein-goldene Akzentecke, weisse Outline-Icons, je eine Zeile Text.",
        alt="Fünf A+ Kacheln zum Ginseng Shot: Fokus-Ritual, Tradition & Moderne, edler Genuss, praktisch, 10er-Box.",
    ),
    AIModule(
        name="Modul 3 — Banner: Tradition trifft Moderne",
        role="a+_banner",
        headline="TRADITION TRIFFT MODERNE.",
        body=(
            "Ginseng wird seit Generationen geschätzt. Madame Chéri bringt die traditionsreiche "
            "Wurzel im praktischen 50-ml-Shot in deinen Alltag — modern inszeniert, edel im "
            "Geschmack. Natürliche Inspiration für jeden Tag."
        ),
        visual="Banner mit ganzer Ginsengwurzel links, Flasche rechts, goldener Verbindungsstrich 'von der Wurzel in den Shot', warme Bernstein-Töne.",
        alt="A+ Banner mit ganzer Ginsengwurzel und der Ginseng-Shot-Flasche, Tradition trifft Moderne.",
    ),
    AIModule(
        name="Modul 4 — Banner: Das Ritual",
        role="a+_banner",
        headline="DEIN RITUAL FÜR JEDEN TAG.",
        body=(
            "In jede Routine integrierbar: morgens nach dem Aufstehen, im Büro oder unterwegs. "
            "Vor dem Trinken kurz schütteln — fertig ist dein ruhiger Fokus-Moment. Ein edler "
            "Genuss, der sich schön in den Tag einfügt."
        ),
        visual="Banner mit drei ruhigen Alltagsszenen (Schreibtisch am Morgen, Küche, unterwegs), Flasche im Vordergrund, warmes Tageslicht.",
        alt="A+ Banner mit dem Ginseng Shot als tägliches Ritual am Schreibtisch, in der Küche und unterwegs.",
    ),
    AIModule(
        name="Modul 5 — Karussell (6 Kacheln): Die Daily-Shot-Linie",
        role="a+_carousel",
        headline="DIE MADAME CHÉRI DAILY SHOTS",
        body=(
            "Kachel 1: <b>GINSENG</b> — Fokus-Ritual, Tradition trifft Moderne (dieses Produkt).<br/>"
            "Kachel 2: <b>DETOX</b> — Fruchtiges Frische-Ritual mit Apfelessig.<br/>"
            "Kachel 3: <b>BROMELAIN</b> — Ananas &amp; Vitamin C, B2, B6.<br/>"
            "Kachel 4: <b>KOLLAGEN</b> — Beauty von innen, mit Zink &amp; Selen.<br/>"
            "Kachel 5: <b>MAGNESIUM</b> — Für Muskeln, Nerven &amp; Energie.<br/>"
            "Kachel 6: <b>GINGER</b> — Scharf, frisch, der Kick am Morgen."
        ),
        visual="6 Flaschen in ihren Farbwelten, einheitliche Komposition, Ginseng dezent hervorgehoben. Dachclaim 'Daily Shots. Daily Benefits.'",
        alt="A+ Karussell mit allen sechs Madame Chéri Daily Shots in ihren Farbwelten.",
    ),
    AIModule(
        name="Modul 6 — Premium Q&A",
        role="a+_qa",
        headline="HÄUFIGE FRAGEN",
        body=(
            "<b>F.</b> Was ist der Ginseng Shot?<br/>"
            "<b>A.</b> Ein edles 50-ml-Ritual mit Ginseng — traditionsreiche Wurzel, modern "
            "inszeniert für bewusste Routinen.<br/><br/>"
            "<b>F.</b> Wie schmeckt er?<br/>"
            "<b>A.</b> Edel und klar mit der typischen Ginseng-Note — ein ruhiger Genuss-Moment "
            "für zwischendurch.<br/><br/>"
            "<b>F.</b> Wie wird er getrunken?<br/>"
            "<b>A.</b> Vor dem Trinken kurz schütteln und pur genießen — jederzeit, ganz nach "
            "deiner Routine.<br/><br/>"
            "<b>F.</b> Wie viele sind enthalten?<br/>"
            "<b>A.</b> 10 Fläschchen à 50 ml — der Vorrat für zwei Wochen tägliches Ritual.<br/><br/>"
            "<b>F.</b> Von wem ist der Shot?<br/>"
            "<b>A.</b> Von Madame Chéri Feinkost, einem deutschen Traditionsunternehmen."
        ),
        visual="Vertikale Frage-/Antwort-Liste, bernstein-goldene Trennlinien, F. in Bernstein und A. in Gold. Kurze Antworten.",
        alt="Premium Q&A Modul mit fünf Kurzantworten zum Madame Chéri Ginseng Shot.",
    ),
    AIModule(
        name="Modul 7 — Premium Vergleichstabelle",
        role="a+_comparison",
        headline="DER EDLE WEG ZUM FOKUS-RITUAL",
        body=(
            "Vier Spalten: <b>Madame Chéri Ginseng Shot</b> · Kaffee · Energy-Drink · "
            "Ginseng-Kapseln.<br/><br/>"
            "Zeilen: Edles tägliches Ritual · Mit Ginseng · Praktisches 50-ml-Format · Kein "
            "Anrühren / kein Schlucken von Kapseln · Für unterwegs · Premium-Feinkost-Genuss.<br/><br/>"
            "Die Ginseng-Spalte bernstein hervorheben, Band 'DAILY SHOTS'. Vergleichsspalten nur "
            "als Kategorie, keine Fremdmarken und KEINE Wirkversprechen — nur Ritual, Format und "
            "Genuss."
        ),
        visual="Standard Amazon Premium Vergleichstabelle, 4 Spalten, Kopfzeile bernstein/gold, Ginseng-Spalte hell hinterlegt.",
        alt="Premium Vergleichstabelle Ginseng Shot gegenüber Kaffee, Energy-Drink und Ginseng-Kapseln.",
    ),
]


QA = [
    AIQA(q="Was ist der Madame Chéri Ginseng Shot?",
         a="Ein edles tägliches 50-ml-Ritual mit Ginseng. Die traditionsreiche Wurzel, modern inszeniert für bewusste Routinen — 'Tradition trifft Moderne.'"),
    AIQA(q="Wie schmeckt der Ginseng Shot?",
         a="Edel und klar mit der typischen Ginseng-Note. Ein ruhiger Genuss-Moment für zwischendurch — Ginseng ist geschmacklich Typsache, für viele angenehm."),
    AIQA(q="Wie trinke ich den Shot am besten?",
         a="Vor dem Trinken kurz schütteln und pur genießen. Ob morgens, im Büro oder unterwegs — ganz nach deiner Routine, als dein täglicher Fokus-Moment."),
    AIQA(q="Wie viele Shots sind in der Box?",
         a="Die Box enthält 10 Fläschchen à 50 ml — dein Vorrat für rund zwei Wochen tägliches Ritual."),
    AIQA(q="Welche Nährwerte hat der Shot?",
         a="Die genauen Nährwertangaben stehen auf dem Etikett. Der Shot ist als edles Genuss-Ritual gedacht, nicht als Wirkprodukt."),
    AIQA(q="Muss der Shot gekühlt werden?",
         a="Ungeöffnet ist er praktisch für Vorrat und unterwegs. Details zur Lagerung stehen auf dem Etikett; angebrochen kühl stellen und zeitnah genießen."),
    AIQA(q="Von wem ist der Ginseng Shot?",
         a="Von Madame Chéri, einem deutschen Feinkost-Traditionsunternehmen. Teil der Daily-Shot-Linie 'Daily Shots. Daily Benefits.'"),
]


BACKEND = (
    "ginseng shot ginseng trinken ginseng fluessig fokus shot wellness shot ginseng extrakt "
    "roter ginseng shots daily shot ritual shot ginseng getraenk functional shot ginseng "
    "ampullen shot flaschen 50ml 10er box tradition moderne madame cheri feinkost getraenk "
    "morgenroutine unterwegs buero"
)


def main() -> None:
    print("Lade Madame Chéri + Ginseng-Achse…")
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
