"""Madame Chéri — MAGNESIUM SHOT (50 ml, 10er-Box)
Hand-written, KW-led, conversion-focused copy im Feinkost-Look.

Marketplace: amazon.de (DE) — deutsche Overlays + Kunden-Copy.
Produkt 204 · Marke: Madame Chéri (Feinkost). Listing noch nicht live.

Positionierung: aktives, sportliches tägliches RITUAL für Muskeln, Nerven & Energie.
Farbwelt: klares Blau. Held: 50-ml-Flasche + 10er-Box, aktiver Lifestyle, Wasser-Spritzer.

COMPLIANCE (wichtig): Tonalität 'etwas mutiger' = starke aktive Lifestyle-Sprache erlaubt
(stark, Fokus, Balance, Bewegung, aktiv), ABER echte Wirkaussagen NUR als die zugelassenen
EU-Health-Claims, wörtlich und an den Nährstoff gebunden:
  · 'Magnesium trägt zu einer normalen Muskelfunktion bei.'
  · 'Magnesium trägt zur Verringerung von Müdigkeit und Ermüdung bei.'
  · 'Magnesium trägt zu einer normalen Funktion des Nervensystems bei.'
  · 'Vitamin D trägt zur Erhaltung normaler Knochen bei.'
  · 'Vitamin B6 trägt zu einem normalen Energiestoffwechsel bei.'
Kein 'beste/Nr.1', kein Krankheits-/Heilbezug (z.B. keine 'gegen Krämpfe'-Aussage),
keine Vorbeuge-/Behandlungs-Sprache, keine Preise/URLs.
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

PLAN_NO = "204"
ASIN = ""   # noch nicht live


BRIEF = ParsedBrief(
    product_name="Madame Chéri Magnesium Shot · 10 x 50 ml",
    brand="Madame Chéri",
    marketplace="amazon.de",
    category="Lebensmittel & Getränke > Nahrungsergänzung > Functional Shots",
    main_keywords=["magnesium shot", "magnesium flüssig", "magnesium sport"],
    all_keywords=[
        "magnesium shot", "magnesium flüssig", "magnesium sport", "magnesium 200mg",
        "muskel shot", "magnesium vitamin d", "magnesium trinkampullen", "magnesium b6",
        "energie shot", "magnesium hochdosiert", "shots", "vitamin d shot", "sport shot",
        "regeneration",
    ],
    usps=[
        "Aktives tägliches Ritual für Muskeln, Nerven & Energie.",
        "200 mg Magnesium plus Vitamin D3 (50 µg) und Vitamin B6 (10 mg).",
        "Magnesium trägt zu einer normalen Muskelfunktion bei.",
        "Magnesium trägt zur Verringerung von Müdigkeit und Ermüdung bei.",
        "Praktisches 50-ml-Format für Sport, Büro und unterwegs.",
        "10er-Box — der Vorrat für zwei Wochen aktives Ritual, Feinkost von Madame Chéri.",
    ],
    target_group=(
        "Aktive, bewegungs- und gesundheitsbewusste Frauen und Männer, die Sport, Alltag und "
        "Routine mit einem einfachen, praktischen Magnesium-Ritual unterstützen möchten."
    ),
    target_problems=(
        "Magnesium-Tabletten sind trocken, Pulver muss angerührt werden und Kapseln fühlen sich "
        "nach Medizin an. Gesucht wird eine schnelle, trinkfertige und angenehme Magnesium-Quelle "
        "für jeden Tag."
    ),
    good_reviews=[
        "Schnell getrunken, kein Anrühren, schmeckt frisch.",
        "Praktisch nach dem Sport und für unterwegs.",
        "Angenehmes Format, gut in die Tagesroutine integrierbar.",
    ],
    bad_reviews=[
        "Magnesium hat einen Eigengeschmack — nicht jedermanns Sache.",
    ],
)


# ===== Copy (Deutsch, Feinkost) — Magnesium: aktive Sprache, Wirkaussagen NUR als zugelassene Claims =====

TITLE = ('Madame Chéri Magnesium Shot · 10 x 50 ml — 200 mg Magnesium mit Vitamin D3 & B6 · '
         'für Muskeln, Nerven & Energie · flüssig & praktisch dosiert · aktives Ritual für jeden Tag')

BULLETS = [
    "<b>STARK DURCH DEN TAG</b> — Dein aktiver Shot für Sport, Alltag und Routine: einfach "
    "aufdrehen, schütteln und trinken. 200 mg Magnesium, flüssig und trinkfertig — kein Anrühren, "
    "kein Tablettengefühl, einfach dein Ritual für Bewegung und Balance.",

    "<b>MAGNESIUM FÜR DIE MUSKELFUNKTION</b> — 200 mg Magnesium pro Shot, sinnvoll dosiert. "
    "Magnesium trägt zu einer normalen Muskelfunktion bei. Der praktische Begleiter, der zu einem "
    "aktiven, bewegten Alltag passt.",

    "<b>MAGNESIUM FÜR NERVEN &amp; WENIGER MÜDIGKEIT</b> — Magnesium trägt zur Verringerung von "
    "Müdigkeit und Ermüdung bei und trägt zu einer normalen Funktion des Nervensystems bei. Fokus "
    "und Balance für Tage, an denen viel zusammenkommt.",

    "<b>VITAMIN D3 &amp; B6 IM SHOT</b> — Clever kombiniert mit 50 µg Vitamin D3 und 10 mg "
    "Vitamin B6. Vitamin D trägt zur Erhaltung normaler Knochen bei, Vitamin B6 trägt zu einem "
    "normalen Energiestoffwechsel bei.",

    "<b>200 MG DOSIERT · 10ER-BOX FEINKOST</b> — Zehn trinkfertige 50-ml-Shots im edlen Display: "
    "dein Vorrat für zwei Wochen aktives Ritual oder zum Ausprobieren und Teilen. Premium-Feinkost "
    "aus einem deutschen Traditionsunternehmen.",
]


IMAGES = [
    AIImagePlanItem(
        name="Bild 1 — Main Hero (3 Varianten für A/B-Test)",
        role="hero",
        background="Klares, frisches Blau mit hellem Verlauf (Magnesium-Farbwelt), passend zum Etikett. Bei allen 3 Varianten identisch für einen sauberen Split-Test.",
        purpose="Klick gewinnen im Shot-Raster — sofort erkennbar als aktiver, premium Magnesium-Shot.",
        visual=(
            "Alle 3 Varianten mocken, Sieger behalten. Feinkost-Look: Madame-Chéri-Logo oben "
            "links, dunkelblauer runder Badge 'Deutsches Traditionsunternehmen', Mengen-Schild "
            "'10 Stück' in Blau. Produkt exakt wie real (klare 50-ml-Flasche, weisser Deckel, "
            "blaues Etikett 'Magnesium Shot'). Amazon-Slot 1 bleibt produktfrei von Text — dies "
            "sind die CTR-Mains für den A/B-Test.\n\n"

            "VARIANTE A — AKTIV & DYNAMISCH (Emotion)\n"
            "Flasche mittig, dynamische Wasser-Spritzer und frische Blau-Akzente ringsum, "
            "Bewegungsgefühl. Ein Hauch Sport-/Aktiv-Stimmung ohne Gesichtsfokus.\n"
            "BADGE (Serif, weiss auf blauem Block): 'STARK DURCH DEN TAG'.\n"
            "Gewinnt, weil es Aktivität und Energie in einem Blick zeigt.\n\n"

            "VARIANTE B — DIE 10ER-BOX (Wert)\n"
            "Die geöffnete 10er-Display-Box mit sichtbaren Fläschchen, zwei Shots davor, "
            "Wasser-Spritzer daneben.\n"
            "BADGE: '10 SHOTS · 2 WOCHEN RITUAL'.\n"
            "Gewinnt, weil es Menge und Vorrat sofort klarmacht.\n\n"

            "VARIANTE C — 200 MG FAKT (rational)\n"
            "Flasche freigestellt, daneben ein klarer Wirkstoff-Chip '200 mg Magnesium' und "
            "kleine D3- und B6-Marker.\n"
            "BADGE: '200 MG MAGNESIUM'.\n"
            "Gewinnt, weil die Dosis der stärkste rationale Hook in der Magnesium-Suche ist.\n\n"

            "Über alle 3: Flasche dominant, Badge ca. 6 % der Fläche, gleiche Lichtstimmung."
        ),
        overlay="(eine Aussage je Variante)",
        overlay_sub="3 Hero-Varianten — A/B testen, Sieger behalten.",
        props=[
            "A: Flasche + dynamische Wasser-Spritzer + Blau-Akzente",
            "B: geöffnete 10er-Box + 2 Shots + Wasser-Spritzer",
            "C: freigestellte Flasche + 200-mg-Chip + D3/B6-Marker",
        ],
        lighting="Hell, frisch, dynamisch; weiche Schatten. Bei allen 3 identisch für den Split-Test.",
        why_it_works=(
            "Drei Auslöser: A verkauft das Gefühl (aktiv, stark), B den Vorrat/Wert, C den "
            "rationalen Hook (200 mg Dosis). Je eine Aussage — auf dem Thumbnail sofort lesbar."
        ),
        ctr="Blaue Farbwelt + '200 mg' heben den Shot im Magnesium-Raster hervor.",
    ),
    AIImagePlanItem(
        name="Bild 2 — Was drin ist: Magnesium, D3 & B6",
        role="hook",
        background="Cremeweiss #F0EADD mit dunkelblauem Serif-Headline-Block oben rechts (Feinkost-Chrome)",
        purpose="In einem Bild zeigen, was wirkt — Wirkstoffe mit dem zugelassenen Muskel-Claim.",
        visual=(
            "Flasche mittig, darum in drei weissen Outline-Kreis-Icons (Feinkost-Callout-Stil) die "
            "Wirkstoffe mit Menge und Label:\n"
            "  • Magnesium 200 mg\n  • Vitamin D3 50 µg\n  • Vitamin B6 10 mg\n\n"
            "Verbindende feine Linien von den Icons zur Flasche, dezente Wasser-Spritzer. "
            "Headline-Block oben: 'Wirkstoffe, klar dosiert'. Kleiner konformer Claim-Fuss: "
            "'Magnesium trägt zu einer normalen Muskelfunktion bei.'"
        ),
        overlay="200 MG MAGNESIUM.",
        overlay_sub="Magnesium trägt zu einer normalen Muskelfunktion bei. Plus Vitamin D3 & B6.",
        props=["Flasche", "3 Wirkstoff-Icon-Kreise (Magnesium, D3, B6)", "Mengen-Label", "Wasser-Spritzer"],
        lighting="Helles, gleichmässiges Food-Licht. Klar und premium.",
        why_it_works=(
            "Bei einem Magnesium-Shot ist die Dosis das erste Kaufkriterium. 200 mg Magnesium plus "
            "D3 und B6 sichtbar zu machen, verankert den Wirkstoff-Wert und rahmt ihn mit dem einzig "
            "zugelassenen Muskel-Claim — mutig im Ton, sauber in der Aussage."
        ),
        cvr="Beantwortet 'wie viel Magnesium?' sofort — das wichtigste CVR-Kriterium.",
    ),
    AIImagePlanItem(
        name="Bild 3 — Warum kaufen: stark & fokussiert",
        role="educate",
        background="Klares Blau, heller Verlauf",
        purpose="Den rationalen Kaufgrund verankern — die zugelassenen Magnesium-Claims greifbar machen.",
        visual=(
            "Freigestellte Flasche links, rechts drei ruhige Fakt-Kacheln mit Outline-Icons, jede "
            "an einen zugelassenen Claim gebunden:\n"
            "  • MUSKELN — normale Muskelfunktion (Magnesium)\n"
            "  • WENIGER MÜDIGKEIT — Verringerung von Müdigkeit und Ermüdung (Magnesium)\n"
            "  • NERVEN — normale Funktion des Nervensystems (Magnesium)\n\n"
            "Kleiner Nährwert-Hinweis dezent am Fuss (pro 100 ml: 46 kcal, Zucker 3,6 g). Klar und "
            "aktiv — starke Sprache, aber jede Wirkaussage exakt als zugelassener Claim."
        ),
        overlay="STARK DURCH DEN TAG.",
        overlay_sub="Magnesium für normale Muskelfunktion & zur Verringerung von Müdigkeit.",
        props=["freigestellte Flasche", "3 Claim-Kacheln (Muskeln, Müdigkeit, Nerven)", "dezenter Nährwert-Hinweis"],
        lighting="Hell und frisch, klarer Fokus auf der Flasche.",
        why_it_works=(
            "Magnesium für Muskeln, weniger Müdigkeit und Nerven sind die stärksten rechtlich "
            "sicheren Kaufgründe. An den Nährstoff gebundene Claims wirken mutig und bleiben doch "
            "sauber — genau die Tonalität, die der Kunde freigegeben hat."
        ),
    ),
    AIImagePlanItem(
        name="Bild 4 — Das Ritual im aktiven Alltag",
        role="desire",
        background="Heller, aktiver Moment (nach dem Sport / Küche am Morgen), frisches Tageslicht",
        purpose="Den Shot in den aktiven Alltag der Zielgruppe setzen — das tägliche Ritual sichtbar machen.",
        visual=(
            "Lifestyle-Szene: eine Person (oder Hände, sportlich-elegant, ohne Gesichtsfokus) hält "
            "den geöffneten Magnesium Shot nach dem Training oder am hellen Küchentresen, daneben "
            "ein Handtuch/Trinkflasche, frische Blau-Akzente und ein Glas Wasser. Dynamisch, "
            "premium, echt — kein Studio-Pharma-Look.\n\n"
            "Kleiner Hinweis-Chip: 'Vor dem Trinken kurz schütteln.'"
        ),
        overlay="FÜR BEWEGUNG GEMACHT.",
        overlay_sub="Aufdrehen, schütteln, trinken — dein Magnesium-Ritual für jeden aktiven Tag.",
        props=["Person/Hände mit Shot", "Handtuch/Trinkflasche", "Glas Wasser", "aktives Setting", "Schüttel-Hinweis"],
        lighting="Frisches, dynamisches Tageslicht von der Seite. Aktiv und aspirational, aber echt.",
        why_it_works=(
            "Verkauft das Gefühl, nicht nur die Flasche: der aktive, starke Moment im Alltag. "
            "Das tägliche Ritual macht aus einem Einzelkauf eine Routine — und damit Wiederkäufe."
        ),
    ),
    AIImagePlanItem(
        name="Bild 5 — Die Shot-Familie von Madame Chéri",
        role="desire",
        background="Cremeweiss #F0EADD mit dunkelblauem Headline-Block",
        purpose="Cross-Sell: die ganze Daily-Shot-Linie zeigen, Magnesium hervorheben.",
        visual=(
            "Sechs Flaschen der Linie in ihren Farbwelten nebeneinander, jede mit kleinem Label:\n"
            "  • MAGNESIUM (blau, dieses Produkt) · DETOX (grün) · BROMELAIN (gelb) · KOLLAGEN "
            "(pink) · GINSENG (bernstein) · GINGER (orange)\n\n"
            "Der Magnesium-Shot dezent hervorgehoben (leichter Rahmen/Podest). Darunter der "
            "Dachclaim 'Daily Shots. Daily Benefits.'"
        ),
        overlay="EIN RITUAL, SECHS SORTEN.",
        overlay_sub="Entdecke die Madame Chéri Daily Shots — für jeden Tag die passende.",
        props=["6 Flaschen in Farbwelten", "Magnesium hervorgehoben", "Dachclaim-Leiste"],
        lighting="Helles, gleichmässiges Studiolicht; jede Farbwelt klar erkennbar.",
        why_it_works=(
            "Zeigt Sortiments-Tiefe und Marken-System. Wer den Magnesium-Shot kauft, sieht sofort "
            "die nächsten Sorten für andere Momente — starker Cross-Sell-Hebel für die neue Linie."
        ),
    ),
    AIImagePlanItem(
        name="Bild 6 — Format & Handling",
        role="desire",
        background="Klares Blau, hell",
        purpose="Menge, Grösse und Handling klarmachen — letzte Kaufhürde räumen.",
        visual=(
            "Zweiteilig. LINKS: die 10er-Box mit den Fläschchen, Label '10 x 50 ml'. RECHTS: eine "
            "Flasche in der Hand als Grössenreferenz (handlich, taschentauglich) mit drei kleinen "
            "Schritt-Icons: 'Schütteln → Aufdrehen → Trinken'.\n\n"
            "Kleiner Fuss: 'Trinkfertig — kein Anrühren, praktisch für Sport und unterwegs.'"
        ),
        overlay="IMMER DABEI.",
        overlay_sub="10 x 50 ml, handlich für Sport, Büro & unterwegs — schütteln, aufdrehen, trinken.",
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
            "Ruhige, edle Aufnahme: die Magnesium-Flasche und die 10er-Box sauber arrangiert, "
            "dezente Wasser-Spritzer, viel Weissraum. Madame-Chéri-Logo mittig, darunter der dunkle "
            "runde Badge 'Deutsches Traditionsunternehmen' und der Dachclaim 'Daily Shots. Daily "
            "Benefits.'\n\n"
            "Ton: premium, warm, ruhig — Feinkost, keine Superlative."
        ),
        overlay="FEINKOST FÜR JEDEN TAG.",
        overlay_sub="Madame Chéri — Daily Shots, Daily Benefits. Deutsches Traditionsunternehmen.",
        props=["Flasche + 10er-Box arrangiert", "dezente Wasser-Spritzer", "Logo", "Deutsches-Traditionsunternehmen-Badge", "Dachclaim"],
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
        headline="STARK DURCH DEN TAG.",
        body=(
            "Der Madame Chéri Magnesium Shot ist dein aktiver Begleiter für Sport, Alltag und "
            "Routine: 200 mg Magnesium plus Vitamin D3 &amp; B6, flüssig und trinkfertig. "
            "Fokus, Balance und Bewegung — praktisch im 50-ml-Format."
        ),
        visual="Breites Banner: Magnesium-Flasche rechts vor klarem Blau mit dynamischen Wasser-Spritzern, links grosse Serif-Headline auf cremeweiss. Logo oben links.",
        alt="Madame Chéri Magnesium Shot vor klarem Blau mit Wasser-Spritzern als aktives Ritual für jeden Tag.",
    ),
    AIModule(
        name="Modul 2 — Karussell (5 Kacheln): Warum Magnesium Shot",
        role="a+_carousel",
        headline="WARUM MAGNESIUM SHOT",
        body=(
            "Kachel 1: <b>200 MG MAGNESIUM</b> — Sinnvoll dosiert, flüssig &amp; trinkfertig.<br/>"
            "Kachel 2: <b>MUSKELFUNKTION</b> — Magnesium trägt zu einer normalen Muskelfunktion bei.<br/>"
            "Kachel 3: <b>WENIGER MÜDIGKEIT</b> — Magnesium trägt zur Verringerung von Müdigkeit und Ermüdung bei.<br/>"
            "Kachel 4: <b>D3 &amp; B6</b> — Vitamin B6 trägt zu einem normalen Energiestoffwechsel bei.<br/>"
            "Kachel 5: <b>10ER-BOX</b> — Der Vorrat für zwei Wochen aktives Ritual."
        ),
        visual="5 quadratische Kacheln, dunkelblaue Akzentecke, weisse Outline-Icons, je eine Zeile Text.",
        alt="Fünf A+ Kacheln zum Magnesium Shot: 200 mg, Muskelfunktion, weniger Müdigkeit, D3 & B6, 10er-Box.",
    ),
    AIModule(
        name="Modul 3 — Banner: Die Wirkstoffe",
        role="a+_banner",
        headline="200 MG MAGNESIUM, KLAR DOSIERT.",
        body=(
            "200 mg Magnesium treffen auf 50 µg Vitamin D3 und 10 mg Vitamin B6 — clever "
            "kombiniert und flüssig trinkfertig. Magnesium trägt zu einer normalen Muskelfunktion "
            "bei, Vitamin D trägt zur Erhaltung normaler Knochen bei."
        ),
        visual="Banner mit drei Wirkstoffen in weissen Outline-Kreisen (Magnesium 200 mg, Vitamin D3 50 µg, Vitamin B6 10 mg), Flasche rechts, dezente Wasser-Spritzer.",
        alt="A+ Banner mit den Wirkstoffen Magnesium, Vitamin D3 und Vitamin B6 rund um die Flasche.",
    ),
    AIModule(
        name="Modul 4 — Banner: Das aktive Ritual",
        role="a+_banner",
        headline="FÜR BEWEGUNG GEMACHT.",
        body=(
            "In jede Routine integrierbar: morgens, im Büro oder nach dem Sport. Vor dem Trinken "
            "kurz schütteln — fertig ist dein Magnesium-Moment. Magnesium trägt zu einer normalen "
            "Funktion des Nervensystems bei."
        ),
        visual="Banner mit drei aktiven Alltagsszenen (Morgen, Schreibtisch, nach dem Sport), Flasche im Vordergrund, frisches Tageslicht.",
        alt="A+ Banner mit dem Magnesium Shot als aktives Ritual in Alltag, Büro und Sport.",
    ),
    AIModule(
        name="Modul 5 — Karussell (6 Kacheln): Die Daily-Shot-Linie",
        role="a+_carousel",
        headline="DIE MADAME CHÉRI DAILY SHOTS",
        body=(
            "Kachel 1: <b>MAGNESIUM</b> — Für Muskeln, Nerven &amp; Energie (dieses Produkt).<br/>"
            "Kachel 2: <b>DETOX</b> — Fruchtiges Frische-Ritual mit grünem Apfelessig.<br/>"
            "Kachel 3: <b>BROMELAIN</b> — Ananas &amp; Vitamin C, B2, B6.<br/>"
            "Kachel 4: <b>KOLLAGEN</b> — Beauty von innen, mit Zink &amp; Selen.<br/>"
            "Kachel 5: <b>GINSENG</b> — Fokus-Ritual, Tradition trifft Moderne.<br/>"
            "Kachel 6: <b>GINGER</b> — Scharf, frisch, der Kick am Morgen."
        ),
        visual="6 Flaschen in ihren Farbwelten, einheitliche Komposition, Magnesium dezent hervorgehoben. Dachclaim 'Daily Shots. Daily Benefits.'",
        alt="A+ Karussell mit allen sechs Madame Chéri Daily Shots in ihren Farbwelten.",
    ),
    AIModule(
        name="Modul 6 — Premium Q&A",
        role="a+_qa",
        headline="HÄUFIGE FRAGEN",
        body=(
            "<b>F.</b> Wie viel Magnesium ist enthalten?<br/>"
            "<b>A.</b> 200 mg Magnesium pro 50-ml-Shot, dazu 50 µg Vitamin D3 und 10 mg "
            "Vitamin B6.<br/><br/>"
            "<b>F.</b> Wofür ist Magnesium gut?<br/>"
            "<b>A.</b> Magnesium trägt zu einer normalen Muskelfunktion und zur Verringerung von "
            "Müdigkeit und Ermüdung bei.<br/><br/>"
            "<b>F.</b> Wie wird der Shot getrunken?<br/>"
            "<b>A.</b> Vor dem Trinken kurz schütteln und pur trinken — trinkfertig, ganz nach "
            "deiner Routine.<br/><br/>"
            "<b>F.</b> Wie viele sind enthalten?<br/>"
            "<b>A.</b> 10 Fläschchen à 50 ml — der Vorrat für zwei Wochen aktives Ritual.<br/><br/>"
            "<b>F.</b> Von wem ist der Shot?<br/>"
            "<b>A.</b> Von Madame Chéri Feinkost, einem deutschen Traditionsunternehmen."
        ),
        visual="Vertikale Frage-/Antwort-Liste, dunkelblaue Trennlinien, F. in Blau und A. in Gold. Kurze Antworten.",
        alt="Premium Q&A Modul mit fünf Kurzantworten zum Madame Chéri Magnesium Shot.",
    ),
    AIModule(
        name="Modul 7 — Premium Vergleichstabelle",
        role="a+_comparison",
        headline="DER SMARTE WEG ZU MAGNESIUM",
        body=(
            "Vier Spalten: <b>Madame Chéri Magnesium Shot</b> · Brausetabletten · Kapseln · "
            "Pulver.<br/><br/>"
            "Zeilen: 200 mg Magnesium pro Portion · Flüssig &amp; trinkfertig · Kein Anrühren · "
            "Plus Vitamin D3 &amp; B6 · Praktisch für unterwegs · Feinkost-Rezeptur.<br/><br/>"
            "Die Magnesium-Spalte blau hervorheben, Band 'DAILY SHOTS'. Vergleichsspalten nur als "
            "Kategorie, keine Fremdmarken."
        ),
        visual="Standard Amazon Premium Vergleichstabelle, 4 Spalten, Kopfzeile dunkelblau, Magnesium-Spalte hellblau hinterlegt.",
        alt="Premium Vergleichstabelle Magnesium Shot gegenüber Brausetabletten, Kapseln und Pulver.",
    ),
]


QA = [
    AIQA(q="Wie viel Magnesium steckt in einem Shot?",
         a="200 mg Magnesium pro 50-ml-Shot, ergänzt um 50 µg Vitamin D3 und 10 mg Vitamin B6 — flüssig und trinkfertig."),
    AIQA(q="Wofür ist der Magnesium Shot gut?",
         a="Magnesium trägt zu einer normalen Muskelfunktion, zur Verringerung von Müdigkeit und Ermüdung und zu einer normalen Funktion des Nervensystems bei."),
    AIQA(q="Welche Rolle spielen Vitamin D3 und B6?",
         a="Vitamin D trägt zur Erhaltung normaler Knochen bei, Vitamin B6 trägt zu einem normalen Energiestoffwechsel bei."),
    AIQA(q="Wie trinke ich den Shot am besten?",
         a="Vor dem Trinken kurz schütteln und pur trinken. Ob morgens, im Büro oder nach dem Sport — ganz nach deiner Routine."),
    AIQA(q="Wie viele Shots sind in der Box?",
         a="Die Box enthält 10 Fläschchen à 50 ml — dein Vorrat für rund zwei Wochen aktives Ritual."),
    AIQA(q="Muss der Shot gekühlt werden?",
         a="Ungeöffnet ist er praktisch für Vorrat und unterwegs. Details zur Lagerung stehen auf dem Etikett; angebrochen kühl stellen und zeitnah trinken."),
    AIQA(q="Von wem ist der Magnesium Shot?",
         a="Von Madame Chéri, einem deutschen Feinkost-Traditionsunternehmen. Teil der Daily-Shot-Linie 'Daily Shots. Daily Benefits.'"),
]


BACKEND = (
    "magnesium shot magnesium fluessig magnesium sport magnesium 200mg muskel shot magnesium "
    "vitamin d magnesium trinkampullen magnesium b6 energie shot magnesium hochdosiert shots "
    "vitamin d shot sport shot regeneration vitamin d3 vitamin b6 trinkfertig fokus balance "
    "bewegung aktiv 50ml 10er box madame cheri feinkost getraenk"
)


def main() -> None:
    print("Lade Madame Chéri + Magnesium-Achse…")
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
