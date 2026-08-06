"""TRU VIRTU — Karten-Portemonnaie Click & Slide Coin Pocket  [Produkt 03]
Titel/Bullets/Backend aus dem gefüllten SEO-Sheet (listing.xlsx); Bildregie + Module
handgeschrieben (DE), Premium/reduziert.

Marketplace: amazon.de. ASIN B08DD58MFX. Marke: TRU VIRTU (new brand).

Unterschied zur Strap Edition (01): dieses Modell hat ein praktisches MÜNZFACH (Coin Pocket)
— Karten UND Münzen in einem Slim Wallet, kaum größer als eine Kreditkarte.

REWORK (Kunden-Feedback, Telco-Vorbereitung):
- PREMIUM klarmachen & Preis rechtfertigen: Made in Germany + patentierter Mechanismus +
  echtes italienisches Leder + Schweizer Aluminium — Qualität, keine Massenware.
- PRESTIGE früh & prominent (Bild 2): an Bord von über 40 Airlines (Emirates, Singapore,
  Cathay Pacific, Lufthansa) + Travel-Retail-Award 2023–2025 — "hat kein anderer".
- SOCIAL PROOF: seit über 20 Jahren (Dolphin Innovations, gegr. 2003), hunderttausende
  zufriedene Kunden weltweit.
- WICHTIGSTER REVIEW-HEBEL: "Karten fallen raus". Ursache ist fast immer falsche Handhabung
  (nicht verschlossen / zu wenige Karten / Nicht-Bankkarten). LÖSUNG = EDUKATION, offensiv
  aber positiv: ein eigenes Bedien-Bild im Listing (Bild 4) + ein detailliertes Manual-Modul
  im A+ (analog secwal). Kernbotschaft: einmal richtig einlegen & VERSCHLIESSEN — dann sitzt
  alles bombenfest.
- A+ analog secwal: Marken-/Prestige-Banner, Kundenstimmen, detailliertes How-to.

House rules aktiv (Config): new_brand=true -> 7 Module, Q&A = Finale (Modul 7),
Modul 6 = Benefits/Info mit smartem Q&A-Bridge (kein Comparison).
COMPLIANCE: keine blanken Superlative (faktisch), RFID ehrlich, keine Konkurrenz-Vergleiche,
keine Preise/URLs.
"""
from __future__ import annotations
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools/brief_app/customers/ultra_pro"))   # seo_loader

from tools.brief_app.core.customers import load_customer
from tools.brief_app.core.excel_parser import parse_excel
from tools.brief_app.core.pdf_builder import BriefBuilder
from tools.brief_app.core.ai import AIImagePlanItem, AIModule, AIQA
import seo_loader as SEOL

PLAN_NO = "03"
ASIN = "B08DD58MFX"
EXCEL = HERE / "listing.xlsx"


IMAGES = [
    AIImagePlanItem(
        name="Bild 1 — Main Hero (3 Varianten für A/B-Test)",
        role="hero",
        background="Reduziertes Premium-Weiss mit gebürstetem Alu-Silber-Akzent. Bei allen 3 Varianten identisch für einen sauberen Split-Test.",
        purpose="Klick gewinnen — Premium + der Differenzierer (Münzfach) + Made in Germany sofort lesbar.",
        visual=(
            "Alle 3 Varianten mocken. Produkt exakt wie real: das Click & Slide Coin-Pocket-Wallet "
            "(ital. Leder) mit herausgefächertem Alu-Karten-Case und sichtbarem Münzfach. Je EINE "
            "Aussage, Produkt dominant ~70%. Reduziert, edel. Amazon-Slot 1 bleibt produktfrei.\n\n"
            "VARIANTE A — DER DIFFERENZIERER: Wallet aufgeklappt, Karten fächern + Münzen im "
            "Münzfach sichtbar. Badge (Graphit): 'SLIM WALLET MIT MÜNZFACH'.\n"
            "VARIANTE B — PREMIUM/USP: Makro ital. Leder + Alu, dezente dt. Flagge. "
            "Badge: 'MADE IN GERMANY · PATENTIERT'.\n"
            "VARIANTE C — KAPAZITÄT: geschlossenes Wallet neben Kreditkarte als Grössenreferenz. "
            "Badge: 'FÜR 12 KARTEN + MÜNZEN'.\n\n"
            "Über alle 3: Produkt ~70%, Badge ~6%, gleiche Lichtstimmung."
        ),
        overlay="(eine Aussage je Variante)",
        overlay_sub="3 Hero-Varianten — A/B testen, Sieger behalten.",
        props=["A: aufgeklappt, Karten fächern + Münzfach", "B: Leder+Alu-Makro + dt. Flagge", "C: neben Kreditkarte + '12 Karten'"],
        lighting="Edles, klares Studiolicht; weiche Reflexe auf Alu und Leder. Bei allen 3 identisch.",
        why_it_works=(
            "Drei Kaufauslöser: A das Alleinstellungsmerkmal (Münzfach im Slim Wallet), B die "
            "Premium-Herkunft (Made in Germany, patentiert), C die Kapazität. Je eine Aussage."
        ),
    ),
    AIImagePlanItem(
        name="Bild 2 — Prestige: an Bord von über 40 Airlines + Awards",
        role="trust",
        background="Reduziertes Graphit/Weiss, dezente Reise-/Boarding-Anmutung. Premium, ruhig.",
        purpose="Das, was kein anderer hat, SOFORT zeigen — Airline-Prestige + Auszeichnungen rechtfertigen Marke & Preis.",
        visual=(
            "Starkes Prestige-Bild. Oben mittig das Wallet edel inszeniert. Darunter eine ruhige "
            "Logo-Reihe der PARTNER-AIRLINES (nur echte Partner: Emirates, Singapore Airlines, "
            "Cathay Pacific, Lufthansa) in dezentem Graphit/Grau, sauber gerastert. Daneben/darunter "
            "die AWARD-Siegel 'Travel-Retail-Award 2023 · 2024 · 2025'. Kleiner Vertrauensbalken: "
            "'~3.000 Stores in 30 Märkten'. Klar, edel, nicht überladen.\n"
            "HINWEIS an Design: nur real genutzte Partner-Logos verwenden (TRU VIRTU ist an Bord "
            "dieser Airlines) — keine erfundenen Logos, keine Preise."
        ),
        overlay="AN BORD VON 40+ AIRLINES.",
        overlay_sub="Emirates · Singapore · Cathay · Lufthansa — Travel-Retail-Award 2023–2025.",
        props=["Wallet edel inszeniert", "Logo-Reihe Partner-Airlines (real)", "Award-Siegel 2023–2025", "'~3.000 Stores in 30 Märkten'"],
        lighting="Edles, ruhiges Premium-Licht; Logos dezent, Produkt im Fokus.",
        why_it_works=(
            "Airline-Prestige + echte Awards sind der stärkste Vertrauens- und Premium-Beweis, den "
            "kein Billig-Etui vorweisen kann. Früh platziert positioniert es die Marke sofort oben."
        ),
        cvr="Rechtfertigt den Premium-Preis über unabhängige Beweise (Airlines, Awards, Reichweite).",
    ),
    AIImagePlanItem(
        name="Bild 3 — Hook: Karten auf Fingerdruck (patentiert)",
        role="hook",
        background="Helles Premium-Grau #F1F2F4 mit Graphit-Headline",
        purpose="Den patentierten Kern-Vorteil zeigen: automatischer Kartenaustritt, einhändig.",
        visual=(
            "Große, klare Sequenz einer Hand: ein leichter Fingerdruck auf den Knopf, die Karten "
            "fächern automatisch und gestaffelt aus dem Alu-Case. Feine Pfeile verdeutlichen die "
            "Bewegung. Kurzer Hinweis: 'Patentierte Click&Slide-Technik — einhändig, in Sekunden.' "
            "Smooth und präzise inszeniert (sichtbar reibungslos)."
        ),
        overlay="KARTEN AUF FINGERDRUCK.",
        overlay_sub="Patentierte Click&Slide-Technik — einhändig, in Sekunden die richtige Karte.",
        props=["Hand am Knopf", "automatisch auffächernde Karten (Sequenz)", "Bewegungs-Pfeile", "'patentiert'-Cue"],
        lighting="Klares Technik-Licht, weiche Reflexe. Bedienung sichtbar reibungslos.",
        why_it_works=(
            "Der patentierte Mechanismus ist der Kern-USP und muss erklärt werden. Die smoothe "
            "Bedienung sichtbar zu machen weckt Begehren und entkräftet den 'hakt'-Einwand vorab."
        ),
    ),
    AIImagePlanItem(
        name="Bild 4 — So sitzt alles sicher (Bedienung / gegen 'Karten fallen raus')",
        role="educate",
        background="Weiss, klares 3-Schritt-Layout, Graphit-Headline",
        purpose="Den #1-Negativ-Treiber offensiv & positiv entkräften: richtig eingelegt fällt nichts heraus.",
        visual=(
            "Freundliches, klares 3-Schritt-Schema (kein Warnton — Anleitung als Qualitätsmerkmal):\n"
            "SCHRITT 1 'Karten als Block einlegen' — alle Karten gemeinsam bis zum Klick eindrücken "
            "(nicht einzeln). Kleiner Zusatz: 'Original-Bankkarten (ISO-Standard)'.\n"
            "SCHRITT 2 'Verschließen' — den seitlichen Knopf nach oben schieben; Icon 'klick/lock'. "
            "Betont: 'Jetzt sitzt alles fest.'\n"
            "SCHRITT 3 'Zum Bezahlen' — Knopf herunterziehen, Karten fächern gestaffelt auf.\n"
            "Zentrale Aussage groß: 'Einmal richtig einlegen & verschließen — dann fällt nichts "
            "heraus.' Ruhig, hochwertig, hilfreich."
        ),
        overlay="EINLEGEN & VERSCHLIESSEN.",
        overlay_sub="Karten als Block einlegen, seitlich verschließen — dann sitzt alles fest.",
        props=["3-Schritt-Schema (Einlegen/Verschließen/Bezahlen)", "Lock-Icon", "'Original-Bankkarten (ISO)'-Zusatz"],
        lighting="Helles, gleichmässiges Info-Licht; jeder Schritt klar lesbar.",
        why_it_works=(
            "Die meisten 'fällt raus'-Rezensionen entstehen durch übersprungenes Verschließen. Wer "
            "es VOR dem Kauf sieht, bedient richtig — das schützt die Bewertung und macht die "
            "durchdachte Mechanik zum Qualitätsmerkmal statt zum Risiko."
        ),
        cvr="Beugt Fehlbedienung & Enttäuschung vor — richtige Handhabung = zufriedener Kunde.",
    ),
    AIImagePlanItem(
        name="Bild 5 — Karten UND Münzen: das Münzfach",
        role="desire",
        background="Weiss, Detail-Fokus auf das Münzfach",
        purpose="Den entscheidenden Mehrwert dieser Edition zeigen: integriertes Münzfach.",
        visual=(
            "Aufgeklapptes Wallet: LINKS das Alu-Case mit Karten, RECHTS das praktische Münzfach "
            "mit ein paar Münzen und Platz für Scheine/Belege. Callouts: 'Integriertes Münzfach', "
            "'Für 12 Karten + Münzen + Scheine', 'Kaum größer als eine Kreditkarte'. Zeigt, dass das "
            "Münzfach sicher schließt (Münzen fallen nicht heraus)."
        ),
        overlay="KARTEN, MÜNZEN & SCHEINE.",
        overlay_sub="Integriertes Münzfach — 12 Karten, Münzen & Scheine, kaum größer als eine Karte.",
        props=["Alu-Case mit Karten", "Münzfach mit Münzen", "Platz für Scheine", "Sicher-schließt-Callout"],
        lighting="Weiches, präzises Detail-Licht; das Münzfach klar sichtbar.",
        why_it_works=(
            "Das Münzfach ist der Grund, dieses Modell statt eines reinen Kartenetuis zu wählen. "
            "Sichtbar zu machen, dass Münzen sicher sitzen, entkräftet den 'fällt raus'-Zweifel."
        ),
        cvr="Zeigt den konkreten Mehrwert (Münzfach) und die sichere Aufbewahrung.",
    ),
    AIImagePlanItem(
        name="Bild 6 — Premium-Qualität, die den Preis rechtfertigt",
        role="trust",
        background="Warmes Premium-Grau, Material-Makros + Vertrauensband",
        purpose="Den Premium-Preis über Material, Herkunft, Technik & Garantie rechtfertigen — keine Massenware.",
        visual=(
            "Edle Material-Makros nebeneinander: das genarbte ITALIENISCHE Leder und das gebürstete "
            "SCHWEIZER Aluminium in Nahaufnahme. Badge-Reihe: 'Genuine Italian Leather' (Gold-Siegel), "
            "'Swiss Aluminium', 'Made in Germany' (dt. Flagge), 'RFID-Schutz · TÜV-geprüft', "
            "'2 Jahre Garantie + Repair-Kit'. Unteres, dezentes Vertrauensband: 'TRU VIRTU — seit "
            "über 20 Jahren · hunderttausende Kunden weltweit'. Ruhig, hochwertig, reduziert.\n"
            "Botschaft (ohne Konkurrenz zu nennen): echte Materialien & deutsche Technik statt "
            "Massenware."
        ),
        overlay="ITAL. LEDER, SCHWEIZER ALU.",
        overlay_sub="Echtes ital. Leder + Schweizer Aluminium, montiert in Deutschland, 2 J. Garantie.",
        props=["ital. Leder-Makro", "Schweizer Alu-Makro", "Badges: Leder/Alu/Made in Germany/RFID-TÜV/Garantie", "Vertrauensband '20+ Jahre · hunderttausende Kunden'"],
        lighting="Warmes, edles Licht auf den Materialien; Handwerk sichtbar.",
        why_it_works=(
            "Bei Premium-Preis entscheidet wahrgenommene Qualität. Echte Materialien, deutsche "
            "Fertigung, geprüfter RFID-Schutz, 2 Jahre Garantie und Langjährigkeit rechtfertigen den "
            "Preis und beruhigen Value-Zweifel."
        ),
        cvr="Bündelt alle Premium-Beweise → macht den höheren Preis nachvollziehbar.",
    ),
    AIImagePlanItem(
        name="Bild 7 — Markenabschluss: edle Geschenkidee",
        role="close",
        background="Reduzierte Premium-Szene, Graphit/Weiss, warme Reise-Anmutung",
        purpose="Emotional auf Marke, Prestige und Geschenk-Eignung abschliessen (bewusst anders als Bild 6).",
        visual=(
            "Warme, edle Lifestyle-Szene: das Wallet mit der exklusiven Geschenkbox auf einem "
            "Reise-Setting (Boarding-Pass, Lounge-Anmutung) — jemand greift entspannt einhändig "
            "zur Karte. Es geht ums GEFÜHL (angekommen, souverän, beschenkt), nicht um Badges. "
            "Unteres Markenband dezent: TRU-VIRTU-Logo · 'Hi-Tech Wallets. Reduced to the Max.'"
        ),
        overlay="EINE EDLE GESCHENKIDEE.",
        overlay_sub="TRU VIRTU — deutsches Hi-Tech-Wallet mit Münzfach, in edler Geschenkbox.",
        props=["Wallet + exklusive Geschenkbox", "Reise-/Lounge-Setting", "TRU-VIRTU-Markenband", "einhändiger Griff (Lifestyle)"],
        lighting="Warmes, ruhiges Licht. Premium, souverän, emotional.",
        why_it_works=(
            "Schliesst emotional auf Marke, Prestige und Geschenk-Eignung — der bewusst andere "
            "Ton nach dem faktischen Qualitäts-Bild 6 (kein zweites Badge-Bild)."
        ),
    ),
]


CREATIVE_MODULES = [
    AIModule(
        name="Modul 1 — Markenbanner",
        role="a+_banner",
        headline="REDUCED TO THE MAX.",
        body=(
            "Das TRU VIRTU Click & Slide Coin Pocket vereint patentierte One-Touch-Technik, "
            "RFID-Schutz, ein praktisches Münzfach und echtes italienisches Leder in einem Slim "
            "Wallet — kaum größer als eine Kreditkarte. Made in Germany, an Bord von über 40 "
            "Airlines weltweit."
        ),
        visual="Breites Premium-Banner: aufgeklapptes Wallet mit auffächernden Karten + Münzfach rechts, reduzierte Headline links auf Weiss, Alu-Silber-Akzent. TRU-VIRTU-Logo oben links.",
        alt="TRU VIRTU Click & Slide Coin Pocket Banner: Karten, Münzfach, RFID-Schutz, Made in Germany.",
    ),
    AIModule(
        name="Modul 2 — Karussell (5 Kacheln): Warum dieses Wallet",
        role="a+_carousel",
        headline="WARUM DIESES WALLET",
        body=(
            "Kachel 1: <b>CLICK&amp;SLIDE</b> — Karten per Fingerdruck, patentiert, einhändig.<br/>"
            "Kachel 2: <b>MIT MÜNZFACH</b> — 12 Karten, Münzen &amp; Scheine in einem.<br/>"
            "Kachel 3: <b>RFID-SCHUTZ</b> — Alu-Hülle gegen unbefugtes Auslesen, TÜV-geprüft.<br/>"
            "Kachel 4: <b>ITAL. LEDER + SWISS ALU</b> — edle Optik, hochwertige Haptik.<br/>"
            "Kachel 5: <b>MADE IN GERMANY</b> — 2 Jahre Garantie, edle Geschenkbox."
        ),
        visual="5 quadratische Kacheln, Alu-Silber-Akzentecke, reduzierte Icons (Knopf/Fächer · Münze · RFID-Schild · Leder/Alu · dt. Flagge).",
        alt="Fünf A+ Kacheln: Click&Slide, Münzfach, RFID-Schutz, italienisches Leder & Swiss Aluminium, Made in Germany.",
    ),
    AIModule(
        name="Modul 3 — Banner: Prestige & Auszeichnungen (analog secwal)",
        role="a+_banner",
        headline="AN BORD VON ÜBER 40 AIRLINES",
        body=(
            "TRU VIRTU Wallets finden Sie an Bord von über 40 führenden Airlines weltweit — u. a. "
            "Emirates, Singapore Airlines, Cathay Pacific und Lufthansa — sowie in rund 3.000 "
            "Stores in 30 Märkten. Ausgezeichnet mit dem Travel-Retail-Award 2023, 2024 und 2025. "
            "Prestige, das kein Etui von der Stange bietet."
        ),
        visual="Premium-Banner: dezente Logo-Reihe der echten Partner-Airlines (Emirates, Singapore, Cathay, Lufthansa) + Award-Siegel 2023/24/25. Produkt edel daneben. HINWEIS: nur real genutzte Partner-Logos.",
        alt="A+ Banner: TRU VIRTU an Bord von über 40 Airlines, Travel-Retail-Award 2023–2025.",
    ),
    AIModule(
        name="Modul 4 — Banner: So bedienst du es richtig (detailliertes How-to)",
        role="a+_banner",
        headline="SO SITZT ALLES SICHER",
        body=(
            "Einmal richtig einlegen — dann fällt nichts heraus. In vier Schritten:<br/><br/>"
            "<b>1. Aktivieren</b> — 3–5 Karten zur Hälfte einschieben und einige Male gegen den "
            "Gummi-Stopfen hin- und herbewegen (nur beim ersten Mal).<br/>"
            "<b>2. Karten einlegen</b> — alle Karten gemeinsam als Block bis zum Klick eindrücken "
            "(nicht einzeln). Max. 5 im Alu-Case (max. 4 geprägte + 1 flache), nur "
            "Original-Bankkarten nach ISO-Standard.<br/>"
            "<b>3. Verschließen</b> — den seitlichen Knopf nach oben schieben. Jetzt sitzt alles "
            "fest.<br/>"
            "<b>4. Bezahlen</b> — den Knopf herunterziehen, die Karten fächern gestaffelt auf.<br/><br/>"
            "<i>Tipp: nicht über Kopf schütteln — das gehört nicht zur normalen Anwendung.</i>"
        ),
        visual="Klares 4-Schritt-How-to (Icons: einschieben · Block/Klick · Lock nach oben · herunterziehen). Ruhig, hochwertig, hilfreich — analog secwal-Bedienmodul. Kein Warnton.",
        alt="A+ How-to: Click & Slide richtig einlegen, verschließen und bedienen — dann fällt nichts heraus.",
    ),
    AIModule(
        name="Modul 5 — Banner: Premium-Qualität, die den Preis rechtfertigt",
        role="a+_banner",
        headline="QUALITÄT, DIE MAN SPÜRT",
        body=(
            "Echtes italienisches Leder, Schweizer Aluminium und der patentierte Click&Slide-"
            "Mechanismus — montiert in Deutschland. Dazu TÜV-geprüfter RFID-Schutz und 2 Jahre "
            "Herstellergarantie inklusive Repair-Kit. Keine Massenware, sondern deutsche "
            "Ingenieurskunst zum täglichen Gebrauch."
        ),
        visual="Banner mit drei Detail-Makros: italienisches Leder, Schweizer Aluminium, RFID-Schild am Alu-Case. Badges: 'Made in Germany' (dt. Flagge), 'TÜV-geprüft', '2 Jahre Garantie'.",
        alt="A+ Banner: italienisches Leder, Schweizer Aluminium, Made in Germany, RFID-Schutz, 2 Jahre Garantie.",
    ),
    AIModule(
        name="Modul 6 — Banner: Darum vertrauen Kunden TRU VIRTU (Benefits + Q&A-Bridge)",
        role="a+_banner",
        headline="DARUM VERTRAUEN KUNDEN",
        body=(
            "Seit über 20 Jahren und mit hunderttausenden zufriedenen Kunden weltweit steht "
            "TRU VIRTU für durchdachte Hi-Tech-Wallets. Was Kunden immer wieder schätzen:<br/><br/>"
            "• <b>Souveräner Alltag</b> — Karten per Fingerdruck, immer die richtige zur Hand.<br/>"
            "• <b>Sicheres Gefühl</b> — RFID-Schutz und eine Mechanik, die hält, was sie verspricht.<br/>"
            "• <b>Bleibende Qualität</b> — edle Materialien, deutsche Fertigung, 2 Jahre Garantie."
        ),
        visual="Warmes Premium-Banner mit Reise-/Alltags-Anmutung, dezentes Vertrauensband 'seit über 20 Jahren · hunderttausende Kunden weltweit'. Drei kurze Benefit-Zeilen, reduziert.",
        alt="A+ Banner: seit über 20 Jahren, hunderttausende zufriedene Kunden — warum sie TRU VIRTU vertrauen.",
    ),
    AIModule(
        name="Modul 7 — Premium Q&A",
        role="a+_qa",
        headline="HÄUFIGE FRAGEN",
        body=(
            "<b>F.</b> Fallen die Karten heraus?<br/>"
            "<b>A.</b> Nein — wenn Sie die Karten als Block einlegen und den seitlichen Knopf nach "
            "oben schieben (verschließen), sitzt alles fest. Bitte Original-Bankkarten (ISO-Standard) "
            "verwenden und das Wallet nicht über Kopf schütteln.<br/><br/>"
            "<b>F.</b> Wie viele Karten und passen Münzen mit hinein?<br/>"
            "<b>A.</b> Bis zu 12 Karten plus Münzfach: max. 5 Karten im Alu-Case (max. 4 geprägte + "
            "1 flache), weitere Karten, Münzen und Scheine im integrierten Leder-Münzfach.<br/><br/>"
            "<b>F.</b> Wie funktioniert die Click&amp;Slide-Technik, und was, wenn sie hakt?<br/>"
            "<b>A.</b> Ein leichter Fingerdruck fächert die Karten automatisch auf. Beim ersten Mal "
            "das Case kurz aktivieren (siehe Anleitung). Sollte einmal etwas klemmen, hilft die "
            "2-Jahres-Garantie inkl. Repair-Kit.<br/><br/>"
            "<b>F.</b> Schützt es vor RFID-Auslesen?<br/>"
            "<b>A.</b> Ja. Die Aluminiumhülle schützt vor unbefugtem Auslesen (RFID/NFC) und vor "
            "Entmagnetisierung — TÜV-geprüft.<br/><br/>"
            "<b>F.</b> Woraus besteht es und wo wird es gefertigt?<br/>"
            "<b>A.</b> Aus echtem italienischem Leder und Schweizer Aluminium, montiert in "
            "Deutschland (Made in Germany), inklusive 2 Jahren Garantie."
        ),
        visual="Vertikale Frage-/Antwort-Liste, Alu-Silber-Trennlinien, F. in Graphit und A. dezent. Kurze Antworten. Erste Frage bewusst offensiv (Karten fallen raus).",
        alt="Premium Q&A Modul zum TRU VIRTU Click & Slide Coin Pocket.",
    ),
]


QA = [
    AIQA(q="Fallen die Karten heraus?",
         a="Nein — wenn Sie die Karten als Block einlegen und den seitlichen Knopf nach oben schieben (verschließen), sitzt alles fest. Bitte Original-Bankkarten nach ISO-Standard verwenden und das Wallet nicht über Kopf schütteln; dann funktioniert die Mechanik zuverlässig."),
    AIQA(q="Wie viele Karten passen hinein, und passen Münzen mit dazu?",
         a="Bis zu 12 Karten plus Münzfach: max. 5 Karten im Aluminium-Case (max. 4 geprägte + 1 flache), weitere Karten, Münzen und Scheine im integrierten Leder-Münzfach — alles kaum größer als eine Kreditkarte."),
    AIQA(q="Wie funktioniert die Click&Slide-Technik, und was, wenn sie hakt?",
         a="Ein leichter Fingerdruck auf den Knopf fächert die Karten automatisch auf. Beim ersten Gebrauch das Case kurz aktivieren (3–5 Karten einschieben und einige Male gegen den Gummi-Stopfen bewegen). Sollte einmal etwas klemmen, greift die 2-Jahres-Garantie inklusive Repair-Kit."),
    AIQA(q="Schützt das Wallet meine Karten vor Datendiebstahl?",
         a="Die Aluminiumhülle schützt vor unbefugtem Auslesen per RFID/NFC-Scanning und vor Entmagnetisierung — TÜV-geprüft."),
    AIQA(q="Aus welchen Materialien besteht es und wo wird es gefertigt?",
         a="Aus echtem italienischem Leder und Schweizer Aluminium, montiert in Deutschland (Made in Germany), inklusive 2 Jahren Herstellergarantie."),
    AIQA(q="Eignet es sich als Geschenk?",
         a="Ja. Das Wallet ist in einer exklusiven Geschenkbox verpackt und damit eine edle Geschenkidee. TRU VIRTU Wallets sind zudem an Bord von über 40 Airlines weltweit erhältlich."),
]


def main() -> None:
    print("Lade TRU VIRTU + SEO-Sheet (Coin Pocket)…")
    cust = load_customer("tru_virtu")
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
    builder._ai_qa = QA
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
