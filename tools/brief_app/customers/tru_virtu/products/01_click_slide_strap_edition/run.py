"""TRU VIRTU — Wallet Click & Slide Strap Edition  [Produkt 01]
Hand-written, recherchierte, marketing-elevated Copy (DE). Quelle: Brand-Deck
(Tru_Virtu.pdf) + Web, da das SEO-Sheet noch ein leeres Template ist.

Marketplace: amazon.de (DE). ASIN B076PJ51BV. Marke: TRU VIRTU (new brand).

House rules aktiv (Config): new_brand=true -> 7 A+ Module, Modul 7 = 'From the Brand'
(kein Comparison); brand_statement -> die coole Marken-Aussage.

STRATEGIE (Kunde): Airline-/Premium-Prestige HERVORHEBEN + Top-Qualität; und weil die
Reviews durchwachsen sind, die echten Einwände aktiv ENTKRÄFTEN:
  - 'Karten fallen raus'      -> Strap-Verschluss + tiefe Lederfächer, alles sitzt sicher
  - 'Slide-Mechanismus hakt'  -> smoothe patentierte One-Touch-Bedienung + korrekte Nutzung
                                 + 2 Jahre Garantie & Repair-Kit als Sicherheit
  - Preis/Value              -> Made in Germany, ital. Leder, Alu, TÜV, Airlines, Awards

COMPLIANCE: keine blanken Superlative (faktisch statt 'führend/meistverkauft');
RFID-Schutz ehrlich (Scanning/Entmagnetisierung), kein '100% sicher'. Keine Preise/URLs.
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

PLAN_NO = "01"
ASIN = "B076PJ51BV"


BRIEF = ParsedBrief(
    product_name="TRU VIRTU Wallet Click & Slide Strap Edition",
    brand="TRU VIRTU",
    asin=ASIN,
    marketplace="amazon.de",
    category="Koffer, Rucksäcke & Taschen > Accessoires > Geldbörsen & Kartenetuis",
    main_keywords=["slim wallet rfid", "kartenetui click slide", "geldbörse herren slim"],
    all_keywords=[
        "slim wallet", "kartenetui rfid schutz", "geldbörse slim herren", "click slide wallet",
        "aluminium kartenetui", "rfid geldbörse", "mini wallet karten", "kartenhalter metall",
        "smart wallet", "geldbörse leder slim", "kreditkartenetui rfid", "portemonnaie slim",
        "kartenetui herren", "reise wallet", "tru virtu", "kartenetui aufklappbar",
    ],
    usps=[
        "Patentierte CLICK&SLIDE-Technik: Karten fächern per One-Touch einhändig auf.",
        "STRAP EDITION: elastisches Band statt Druckknopf hält alles sicher zusammen.",
        "Alu-Karten-Case mit RFID-Schutz (TÜV-geprüft) gegen Auslesen & Entmagnetisierung.",
        "Für 12 Karten: 5 im Alu-Case (max. 4 geprägt + 1 flach) + 7 im Leder-Envelope, plus Scheine.",
        "Echtes italienisches Nappa-Leder + Swiss-Made-Aluminium (50% recycelt).",
        "Made in Germany, 2 Jahre Herstellergarantie + Repair-Kit.",
        "An Bord von über 40 Airlines weltweit (u.a. Emirates, Singapore Airlines, Lufthansa).",
        "Mehrfacher Travel-Retail-Award-Gewinner 2023-2025.",
    ],
    technical_info=[
        "Alu-Case: 5 Karten (max. 4 geprägt + 1 flach); Leder-Envelope: 7 Karten + Scheine",
        "Materialien: ital. Nappa-Rindsleder, Aluminium (Swiss Made, 50% recycelt)",
        "RFID/NFC-Schutz + Entmagnetisierung, TÜV-geprüft",
        "Verschluss: elastischer Strap (Strap Cross / Strap Edge Edition)",
        "Made in Germany · 2 Jahre Garantie · patentierte Click&Slide-Technik",
    ],
    target_group=(
        "Anspruchsvolle, design- und sicherheitsbewusste Vielreisende (35-65), die Wert auf "
        "Qualität, Datenschutz und reduziertes Premium-Design legen und für echte Qualität mehr "
        "zahlen."
    ),
    target_problems=(
        "Klassische Geldbörsen sind dick, unsicher gegen RFID-Auslesen und unpraktisch beim "
        "schnellen Kartenzugriff auf Reisen. Gesucht wird ein schlankes, sicheres, hochwertiges "
        "Wallet, das Karten schützt und blitzschnell griffbereit macht."
    ),
    good_reviews=[
        "Hochwertige Verarbeitung, edles Leder und Alu — fühlt sich premium an.",
        "Karten sind mit einem Klick da — genial am Flughafen und im Alltag.",
        "Endlich schlank in der Hosentasche, trotzdem viel Platz.",
    ],
    bad_reviews=[
        "Manche berichten, dass Karten herausrutschen können.",
        "Vereinzelt hakt der Slide-Mechanismus bei falscher Bedienung.",
        "Für manche ist der Preis hoch.",
    ],
)


# ===== KW-geführte Copy (Deutsch) =====

TITLE = ('TRU VIRTU Wallet Click & Slide Strap Edition — Slim Wallet mit RFID-Schutz & '
         'patentierter Click&Slide-Technik · Alu-Kartenetui + echtes italienisches Leder · '
         'für 12 Karten · Made in Germany')

BULLETS = [
    "<b>PATENTIERTE CLICK&amp;SLIDE-TECHNIK</b> — Ein leichter Druck auf den seitlichen Knopf und "
    "deine Karten fächern sich einhändig auf — griffbereit in Sekunden. Die durchdachte "
    "One-Touch-Mechanik von TRU VIRTU, entwickelt und patentiert in Deutschland.",

    "<b>STRAP EDITION — ALLES SITZT SICHER</b> — Statt Druckknopf hält ein elastisches Band das "
    "Wallet fest zusammen: Karten und Scheine bleiben sicher an ihrem Platz, auch unterwegs. "
    "Symbiose aus Tradition und Moderne — mit vertikalem oder horizontalem Strap.",

    "<b>RFID-SCHUTZ, TÜV-GEPRÜFT</b> — Das Aluminium-Case schützt deine Karten zuverlässig vor "
    "unbefugtem Auslesen (RFID/NFC-Scanning) und vor Entmagnetisierung — geprüfte Sicherheit für "
    "deine persönlichen Daten.",

    "<b>FÜR 12 KARTEN + SCHEINE</b> — 5 Karten im Alu-Case (max. 4 geprägt + 1 flach) plus 7 im "
    "echten italienischen Leder-Envelope, dazu Platz für Scheine und Belege. Viel Stauraum in "
    "einem bewusst schlanken Format.",

    "<b>MADE IN GERMANY · 2 JAHRE GARANTIE</b> — Echtes italienisches Nappa-Leder trifft "
    "Swiss-Made-Aluminium, gefertigt in Deutschland. Inklusive 2 Jahren Herstellergarantie und "
    "Repair-Kit. Ein Hi-Tech-Wallet, wie man es an Bord von über 40 Airlines weltweit findet.",
]


IMAGES = [
    AIImagePlanItem(
        name="Bild 1 — Main Hero (3 Varianten für A/B-Test)",
        role="hero",
        background="Reduziertes Premium-Weiss mit gebürstetem Alu-Silber-Akzent. Bei allen 3 Varianten identisch für einen sauberen Split-Test.",
        purpose="Klick gewinnen im Geldbörsen-Raster — sofort premium + reise-affin + funktional wirken.",
        visual=(
            "Alle 3 Varianten mocken. Produkt exakt wie real: das Strap-Edition-Wallet (schwarzes "
            "Nappa-Leder) mit herausgefächertem Alu-Karten-Case und dem elastischen Strap. Je EINE "
            "Aussage, Produkt dominant ~70%. Reduziert, edel. Amazon-Slot 1 bleibt produktfrei von "
            "Text.\n\n"
            "VARIANTE A — AIRLINE-PRESTIGE (der Wow-Hebel): Wallet elegant in Szene, dezente "
            "Airline-/Boarding-Anmutung (Boarding-Pass, Lounge unscharf), kleine Airline-Logos "
            "nur angedeutet. Badge (Graphit): 'AN BORD VON 40+ AIRLINES'.\n"
            "VARIANTE B — FUNKTION: Karten fächern aus dem Alu-Case, RFID-Wellen-Icon. "
            "Badge: '12 KARTEN · RFID-SCHUTZ'.\n"
            "VARIANTE C — QUALITÄT: Makro Leder + Alu, dt. Flagge. Badge: 'MADE IN GERMANY'.\n\n"
            "Über alle 3: Produkt ~70%, Badge ~6%, gleiche Lichtstimmung."
        ),
        overlay="(eine Aussage je Variante)",
        overlay_sub="3 Hero-Varianten — A/B testen, Sieger behalten.",
        props=["A: Wallet + Boarding/Lounge-Anmutung", "B: Karten fächern + RFID-Icon", "C: Leder+Alu-Makro + dt. Flagge"],
        lighting="Edles, klares Studiolicht; weiche Reflexe auf Alu und Leder. Bei allen 3 identisch.",
        why_it_works=(
            "Drei Kaufauslöser: A verkauft Prestige/Vertrauen (an Bord führender Airlines), B die "
            "Funktion (12 Karten + RFID), C die Qualität (Made in Germany). Je eine Aussage — auf "
            "dem Thumbnail sofort lesbar."
        ),
    ),
    AIImagePlanItem(
        name="Bild 2 — Hook: Karten auf Knopfdruck",
        role="hook",
        background="Helles Premium-Grau #F1F2F4 mit Graphit-Headline",
        purpose="Den patentierten Kern-Vorteil zeigen: One-Touch, einhändig.",
        visual=(
            "Große, klare Sequenz (2-3 Phasen) einer Hand, die mit dem Daumen den seitlichen Knopf "
            "drückt — die Karten fächern sich fächerförmig aus dem Alu-Case. Feine Pfeile "
            "verdeutlichen die Bewegung. Kurzer Hinweis: 'Einhändig, in Sekunden.' Smooth und "
            "präzise inszeniert (zeigt bewusst die reibungslose Bedienung)."
        ),
        overlay="KARTEN AUF KNOPFDRUCK.",
        overlay_sub="Patentierte Click&Slide-Technik — einhändig, in Sekunden griffbereit.",
        props=["Hand mit Daumen am Knopf", "auffächernde Karten (Sequenz)", "Bewegungs-Pfeile"],
        lighting="Klares Technik-Licht, weiche Reflexe. Bedienung sichtbar reibungslos.",
        why_it_works=(
            "Die patentierte One-Touch-Mechanik ist der Kern-USP. Die smoothe Bedienung sichtbar "
            "zu zeigen weckt Begehren — und entkräftet zugleich vorab den 'hakt'-Einwand."
        ),
    ),
    AIImagePlanItem(
        name="Bild 3 — Klarstellung: Strap hält alles sicher",
        role="educate",
        background="Weiss, Detail-Fokus auf den Strap-Verschluss",
        purpose="Den Haupt-Review-Einwand ('Karten fallen raus') aktiv entkräften.",
        visual=(
            "Makro des geschlossenen Wallets mit dem elastischen STRAP, der fest um das Etui "
            "spannt; daneben das geöffnete Leder-Envelope mit Karten und Scheinen, die tief und "
            "sicher in den Fächern sitzen. Kleine Callouts: 'Elastischer Strap statt Druckknopf', "
            "'Tiefe Lederfächer', 'Alles sitzt sicher'. Ehrlich und beruhigend — kein "
            "Überversprechen."
        ),
        overlay="NICHTS FÄLLT RAUS.",
        overlay_sub="Elastischer Strap + tiefe Lederfächer halten Karten & Scheine sicher.",
        props=["Makro Strap-Verschluss", "geöffnetes Envelope mit Karten & Scheinen", "3 Sicherheits-Callouts"],
        lighting="Weiches, präzises Detail-Licht; Material und Spannung des Straps klar sichtbar.",
        why_it_works=(
            "'Karten fallen raus' ist der häufigste Kritikpunkt. Die Strap Edition löst genau das "
            "— das sichtbar zu machen verwandelt den Einwand in ein Kaufargument."
        ),
        cvr="Adressiert direkt den Top-Review-Einwand und beugt Retouren vor.",
    ),
    AIImagePlanItem(
        name="Bild 4 — RFID-Schutz, TÜV-geprüft",
        role="trust",
        background="Graphit/Weiss, technisch-clean",
        purpose="Den Datenschutz-Nutzen beweisen — sachlich, geprüft.",
        visual=(
            "Das Alu-Case mit stilisiertem RFID-Wellen-Schild: ein Scan-Versuch prallt am "
            "Aluminium ab. Icon-Reihe: 'Schutz vor RFID/NFC-Auslesen', 'Schutz vor "
            "Entmagnetisierung', 'TÜV-geprüft'. Ehrliche Formulierung (schützt vor Auslesen, kein "
            "'100% gegen alles')."
        ),
        overlay="RFID-SCHUTZ, TÜV-GEPRÜFT.",
        overlay_sub="Alu-Case schützt vor unbefugtem Auslesen (RFID/NFC) & Entmagnetisierung.",
        props=["Alu-Case + RFID-Schild", "abprallender Scan", "3 Schutz-Icons"],
        lighting="Klares, technisches Licht; Aluminium wirkt hochwertig und massiv.",
        why_it_works=(
            "Datenschutz ist ein zentrales Kaufmotiv der Zielgruppe. Ein geprüfter (TÜV) "
            "RFID-Schutz macht den Nutzen glaubwürdig statt behauptet."
        ),
    ),
    AIImagePlanItem(
        name="Bild 5 — Qualität: Alu trifft italienisches Leder",
        role="desire",
        background="Warmes Premium-Grau, Material-Makros",
        purpose="Den Premium-Preis rechtfertigen — Materialien & Herkunft.",
        visual=(
            "Edle Material-Makros: das gebürstete Aluminium-Case und das genarbte italienische "
            "Nappa-Leder in Nahaufnahme, dazu das Gold-Siegel 'Genuine Italian Leather', die "
            "dt. Flagge 'Made in Germany' und 'Swiss Made Aluminium / 50% recycelt'. Ruhig, "
            "hochwertig, reduziert."
        ),
        overlay="ALU TRIFFT ITAL. LEDER.",
        overlay_sub="Echtes italienisches Nappa-Leder + Swiss-Made-Aluminium, Made in Germany.",
        props=["Alu-Makro", "ital. Leder-Makro", "Gold-Siegel + dt. Flagge + Alu-Badge"],
        lighting="Warmes, edles Licht auf den Materialien; Handwerk sichtbar.",
        why_it_works=(
            "Bei einem Premium-Preis entscheidet die wahrgenommene Qualität. Echte Materialien und "
            "Herkunft sichtbar zu machen rechtfertigt den Preis und beruhigt Value-Zweifel."
        ),
    ),
    AIImagePlanItem(
        name="Bild 6 — Kapazität & einhändige Bedienung",
        role="desire",
        background="Weiss, sauberes Info-Layout",
        purpose="Kapazität klar machen und die korrekte, mühelose Nutzung zeigen.",
        visual=(
            "Zweiteilig. LINKS: aufgeklapptes Wallet mit klarer Zählung — '5 Karten im Alu-Case "
            "(max. 4 geprägt + 1 flach)' + '7 Karten im Leder-Envelope' + 'Scheine & Belege' = "
            "'für 12 Karten'. RECHTS: 3 Schritte der einhändigen Bedienung (Knopf drücken -> "
            "Karten auffächern -> gewünschte Karte ziehen), damit die Handhabung von Anfang an "
            "reibungslos gelingt."
        ),
        overlay="12 KARTEN, EINHÄNDIG.",
        overlay_sub="5 im Alu-Case + 7 im Leder-Envelope + Scheine — mühelos in Sekunden.",
        props=["aufgeklapptes Wallet mit Kapazitäts-Zählung", "3 Schritte einhändige Bedienung"],
        lighting="Helles, gleichmässiges Info-Licht; alles klar lesbar.",
        why_it_works=(
            "Zeigt Kapazität und korrekte Nutzung in einem Bild — beantwortet 'wie viel passt "
            "rein?' und beugt dem 'hakt/Bedienung'-Einwand vor, indem die richtige Handhabung "
            "sichtbar wird."
        ),
    ),
    AIImagePlanItem(
        name="Bild 7 — Markenabschluss: Reduced to the Max",
        role="close",
        background="Reduzierte Premium-Szene, Graphit/Weiss",
        purpose="Auf Marke, Prestige und Auszeichnungen abschliessen.",
        visual=(
            "Ruhige, edle Aufnahme: das Wallet in einer premium Reise-Anmutung (Boarding-Pass, "
            "Lounge unscharf). Unteres Markenband mit TRU-VIRTU-Logo und drei ruhigen Punkten: "
            "'Made in Germany · patentierte Click&Slide-Technik', 'An Bord von über 40 Airlines "
            "weltweit', 'Travel-Retail-Award-Gewinner 2023-2025'. Ton: premium, reduziert."
        ),
        overlay="REDUCED TO THE MAX.",
        overlay_sub="TRU VIRTU — deutsche Hi-Tech-Wallets, an Bord der Welt zuhause.",
        props=["Wallet in Reise-Anmutung", "TRU-VIRTU-Markenband", "3 Prestige-Punkte (Made in Germany / Airlines / Awards)"],
        lighting="Edles, ruhiges Licht. Premium und selbstbewusst-reduziert.",
        why_it_works=(
            "Schliesst auf Marke und Prestige: an Bord führender Airlines, ausgezeichnet, Made in "
            "Germany. Genau die Signale, die den Premium-Kauf absichern."
        ),
    ),
]


MODULES = [
    AIModule(
        name="Modul 1 — Markenbanner",
        role="a+_banner",
        headline="KARTEN AUF KNOPFDRUCK.",
        body=(
            "Die TRU VIRTU Click & Slide Strap Edition vereint patentierte One-Touch-Technik, "
            "RFID-Schutz und echtes italienisches Leder in einem bewusst schlanken Wallet. "
            "Made in Germany — und an Bord von über 40 Airlines weltweit zuhause."
        ),
        visual="Breites Premium-Banner: Wallet mit auffächernden Karten rechts, reduzierte Headline links auf Weiss, Alu-Silber-Akzent. TRU-VIRTU-Logo oben links.",
        alt="TRU VIRTU Click & Slide Strap Edition Banner: One-Touch, RFID-Schutz, Made in Germany.",
    ),
    AIModule(
        name="Modul 2 — Karussell (5 Kacheln): Warum TRU VIRTU",
        role="a+_carousel",
        headline="WARUM TRU VIRTU",
        body=(
            "Kachel 1: <b>CLICK&amp;SLIDE</b> — Karten per One-Touch, einhändig.<br/>"
            "Kachel 2: <b>STRAP-VERSCHLUSS</b> — Elastisches Band, alles sitzt sicher.<br/>"
            "Kachel 3: <b>RFID-SCHUTZ</b> — TÜV-geprüft gegen Auslesen &amp; Entmagnetisierung.<br/>"
            "Kachel 4: <b>FÜR 12 KARTEN</b> — Alu-Case + ital. Leder-Envelope.<br/>"
            "Kachel 5: <b>MADE IN GERMANY</b> — 2 Jahre Garantie + Repair-Kit."
        ),
        visual="5 quadratische Kacheln, Alu-Silber-Akzentecke, reduzierte Icons (Knopf/Fächer · Strap · RFID-Schild · Karten · dt. Flagge).",
        alt="Fünf A+ Kacheln: Click&Slide, Strap-Verschluss, RFID-Schutz, 12 Karten, Made in Germany.",
    ),
    AIModule(
        name="Modul 3 — Banner: Sicher verschlossen (Strap)",
        role="a+_banner",
        headline="ELASTISCHER STRAP. ALLES SITZT SICHER.",
        body=(
            "Die Strap Edition setzt auf ein elastisches Band statt Druckknopf: Es hält das Wallet "
            "fest zusammen, sodass Karten und Scheine sicher an ihrem Platz bleiben — auch in der "
            "Tasche und unterwegs. Symbiose aus Tradition und Moderne, mit vertikalem oder "
            "horizontalem Strap."
        ),
        visual="Banner: Makro des gespannten Straps um das geschlossene Wallet links, geöffnetes Leder-Envelope mit sicher sitzenden Karten & Scheinen rechts. Reduziert, premium.",
        alt="A+ Banner zur Strap Edition: elastisches Band hält Karten und Scheine sicher.",
    ),
    AIModule(
        name="Modul 4 — Banner: Datenschutz & Qualität",
        role="a+_banner",
        headline="RFID-SCHUTZ. MADE IN GERMANY.",
        body=(
            "Das Aluminium-Case schützt deine Karten vor unbefugtem Auslesen (RFID/NFC) und vor "
            "Entmagnetisierung — TÜV-geprüft. Kombiniert mit echtem italienischem Nappa-Leder und "
            "Swiss-Made-Aluminium, gefertigt in Deutschland und mit 2 Jahren Herstellergarantie."
        ),
        visual="Banner mit drei Detail-Makros: RFID-Schild am Alu-Case, italienisches Nappa-Leder, dt. Flagge 'Made in Germany' + '2 Jahre Garantie'-Siegel.",
        alt="A+ Banner: RFID-Schutz, italienisches Leder, Made in Germany, 2 Jahre Garantie.",
    ),
    AIModule(
        name="Modul 5 — Karussell (5 Kacheln): Für Reise & Alltag",
        role="a+_carousel",
        headline="FÜR REISE & ALLTAG",
        body=(
            "Kachel 1: <b>FLUGHAFEN</b> — Boarding-Pass &amp; Karten in Sekunden griffbereit.<br/>"
            "Kachel 2: <b>BUSINESS</b> — Schlank im Sakko, Karten sicher geschützt.<br/>"
            "Kachel 3: <b>DUTY FREE</b> — Tap &amp; Go, ohne alles auszupacken.<br/>"
            "Kachel 4: <b>ALLTAG</b> — Weniger Ballast, mehr Überblick.<br/>"
            "Kachel 5: <b>GESCHENK</b> — Premium-Wallet, edel verpackt."
        ),
        visual="5 Lifestyle-Kacheln (Flughafen · Business · Duty Free · Alltag · Geschenk), einheitlich premium-reduziert.",
        alt="Fünf A+ Kacheln: TRU VIRTU Wallet für Flughafen, Business, Duty Free, Alltag und als Geschenk.",
    ),
    AIModule(
        name="Modul 6 — Premium Q&A",
        role="a+_qa",
        headline="HÄUFIGE FRAGEN",
        body=(
            "<b>F.</b> Wie viele Karten passen hinein?<br/>"
            "<b>A.</b> Für 12 Karten: 5 im Alu-Case (max. 4 geprägt + 1 flach) und 7 im "
            "Leder-Envelope, dazu Scheine und Belege.<br/><br/>"
            "<b>F.</b> Fallen Karten heraus?<br/>"
            "<b>A.</b> Nein — der elastische Strap hält das Wallet fest zusammen und die tiefen "
            "Lederfächer halten Karten und Scheine sicher an ihrem Platz.<br/><br/>"
            "<b>F.</b> Wie funktioniert die Click&amp;Slide-Technik?<br/>"
            "<b>A.</b> Ein leichter Druck auf den seitlichen Knopf, und die Karten fächern sich "
            "einhändig auf. Patentiert und in Deutschland entwickelt.<br/><br/>"
            "<b>F.</b> Schützt es vor RFID-Auslesen?<br/>"
            "<b>A.</b> Ja. Das Aluminium-Case schützt vor unbefugtem Auslesen (RFID/NFC) und vor "
            "Entmagnetisierung — TÜV-geprüft.<br/><br/>"
            "<b>F.</b> Gibt es eine Garantie?<br/>"
            "<b>A.</b> Ja, 2 Jahre Herstellergarantie. Viele Reparaturen lassen sich zudem mit dem "
            "beiliegenden Repair-Kit selbst erledigen."
        ),
        visual="Vertikale Frage-/Antwort-Liste, Alu-Silber-Trennlinien, F. in Graphit und A. dezent. Kurze Antworten.",
        alt="Premium Q&A Modul zur TRU VIRTU Click & Slide Strap Edition.",
    ),
]


QA = [
    AIQA(q="Wie viele Karten passen in das Wallet?",
         a="Für 12 Karten: 5 im Aluminium-Case (max. 4 geprägte + 1 flache Karte) und 7 im italienischen Leder-Envelope, dazu Platz für Scheine und Belege."),
    AIQA(q="Fallen die Karten heraus?",
         a="Nein. Die Strap Edition nutzt ein elastisches Band statt Druckknopf, das das Wallet fest zusammenhält; die tiefen Lederfächer halten Karten und Scheine sicher an ihrem Platz — auch unterwegs."),
    AIQA(q="Wie funktioniert die Click&Slide-Technik, und was, wenn sie hakt?",
         a="Ein leichter Druck auf den seitlichen Knopf fächert die Karten einhändig auf. Die Mechanik ist auf reibungslose Bedienung ausgelegt; bitte wie in der beiliegenden Anleitung bedienen. Sollte einmal etwas klemmen, hilft das Repair-Kit oder die 2-Jahres-Garantie."),
    AIQA(q="Schützt das Wallet meine Karten vor Datendiebstahl?",
         a="Das Aluminium-Case schützt vor unbefugtem Auslesen per RFID/NFC-Scanning und vor Entmagnetisierung. Der Schutz ist TÜV-geprüft."),
    AIQA(q="Aus welchen Materialien besteht es und wo wird es gefertigt?",
         a="Aus echtem italienischem Nappa-Leder und Swiss-Made-Aluminium (50% recycelt). Gefertigt in Deutschland (Made in Germany), inklusive 2 Jahren Herstellergarantie."),
    AIQA(q="Ist es für Reisen geeignet?",
         a="Ja. Das schlanke Format, der schnelle Kartenzugriff und der RFID-Schutz machen es ideal für unterwegs. TRU VIRTU Wallets sind an Bord von über 40 Airlines weltweit erhältlich."),
    AIQA(q="Kann ich damit kontaktlos bezahlen?",
         a="Ja, per Tap & Go lässt sich eine Karte nutzen, während die übrigen Karten im Alu-Case geschützt bleiben."),
]


BACKEND = (
    "slim wallet rfid kartenetui click slide aluminium leder geldboerse herren damen mini wallet "
    "kartenhalter metall smart wallet reise portemonnaie kreditkartenetui rfid schutz tuev italienisches "
    "leder made in germany strap edition tru virtu 12 karten einhaendig"
)


def main() -> None:
    print("Lade TRU VIRTU + recherchierte Produkt-Achse…")
    cust = load_customer("tru_virtu")
    brief = BRIEF
    OUT = HERE / f"{PLAN_NO}_{ASIN}_Image Plan.pdf"
    print(f"  Produkt: {brief.product_name}  ASIN: {ASIN}  Marktplatz: {cust.marketplace}")
    print(f"  new_brand={cust.new_brand} (Comparison weg, From-the-Brand als Modul 7)")

    builder = BriefBuilder(cust, brief, OUT, ai=None)
    builder._ai_title = TITLE
    builder._ai_bullets = BULLETS
    builder._ai_images = IMAGES
    builder._ai_modules = MODULES
    builder._ai_qa = QA
    builder._ai_backend = BACKEND
    builder.copy_source_label = "Hand-written senior copy (recherchiert aus Brand-Deck, DE)"

    print("Baue Branded PDF…")
    pdf_path = builder.build()
    size_kb = pdf_path.stat().st_size // 1024
    import re
    pages = len(re.findall(rb'/Type\s*/Page[^s]', pdf_path.read_bytes()))
    print(f"Gebaut: {pdf_path}")
    print(f"  Seiten: {pages}  Größe: {size_kb} KB")


if __name__ == "__main__":
    main()
