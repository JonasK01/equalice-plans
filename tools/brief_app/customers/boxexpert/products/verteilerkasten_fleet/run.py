"""BOXEXPERT — Verteilerkasten aussen, Serie FLEET (ABS, IP65) 300x200x130 mm
Hand-written, KW-led, conversion-focused copy injected into the branded pipeline.

Marketplace: amazon.de (DE) — deutsche Overlays + Kunden-Copy.
ASIN: B093C38XCH · Produkt 01 · Marke: BOXEXPERT (Norderstedt).

Es gibt fuer dieses Produkt KEIN SEO-Listing-xlsx — der Brief wird aus recherchierten
Daten gebaut (Amazon-Listing-Screenshot inkl. 2.582 Bewertungen, boxexpert.de
Produktseite Serie Fleet, Ueber-uns-Seite, Startseite, Logo).

Positionierung: 'Das robuste Leichtgewicht' — rund 50 % leichter als Stahlblech,
aber IP65/IK08-hart. Doppelte Zielgruppe: B2B/Profi UND DIY/Prosumer.

Genauigkeits- und Compliance-Leitplanken:
  - 'wasserdicht' ist vom Kunden freigegeben (Haupt-Keyword) und wird bewusst gefuehrt,
    immer zusammen mit dem Beleg IP65. Untertauchen/Tauchwasser weiterhin nicht behaupten.
  - 'schuetzt vor' statt 'verhindert'. Keine Superlative (beste/Nr. 1/garantiert).
  - Nur echten Lieferumfang zeigen (verzinkte Montageplatte, Laschen, Schrauben).
"""
from __future__ import annotations
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent          # self-contained product folder
ROOT = HERE.parents[5]                           # project root (Claude_Code/)
sys.path.insert(0, str(ROOT))

from tools.brief_app.core.customers import load_customer
from tools.brief_app.core.excel_parser import ParsedBrief
from tools.brief_app.core.pdf_builder import BriefBuilder
from tools.brief_app.core.ai import AIImagePlanItem, AIModule, AIQA


PLAN_NO = "01"
ASIN = "B093C38XCH"


# ===== recherchierte Produkt-Achse (statt listing.xlsx) =====

BRIEF = ParsedBrief(
    product_name="Verteilerkasten außen · Serie Fleet · 300x200x130 mm",
    brand="BOXEXPERT",
    asin=ASIN,
    marketplace="amazon.de",
    listing_url="https://www.amazon.de/gp/product/B093C38XCH",
    category="Gewerbe, Industrie & Wissenschaft > Elektroinstallation > Elektrische Gehäuse",
    main_keywords=["verteilerkasten aussen wasserdicht", "schaltschrank aussen", "industriegehäuse"],
    all_keywords=[
        "verteilerkasten aussen wasserdicht", "verteilerkasten aussen", "schaltschrank aussen",
        "schaltschrank kunststoff", "industriegehäuse", "leergehäuse", "wandgehäuse", "wandschrank",
        "ip65 gehäuse", "verteilerkasten ip65", "kunststoffgehäuse elektro", "elektro gehäuse",
        "sicherungskasten aussen", "schaltkasten", "abzweigdose gross", "gehäuse abs",
        "verteilerkasten garten", "wallbox gehäuse", "pv gehäuse", "solar gehäuse",
        "verteilerkasten 300x200x130", "schaltschrank ip65 kunststoff", "elektrogehäuse aussen",
        "montageplatte schaltschrank", "verteilerkasten schwarz", "verteilerkasten grau",
    ],
    usps=[
        "ABS-Kunststoffgehäuse: rund 50 % leichter als ein Stahlblechschrank gleicher Größe.",
        "Schutzart IP65 — staubdicht und geschützt gegen Strahlwasser, für innen und außen.",
        "Schlagfestigkeit IK08 und eingeschäumte PUR-Dichtung, witterungs- und alterungsbeständig.",
        "Einsatzbereit von -35 °C bis +65 °C, halogenfrei und UV-beständig.",
        "Korrosionsbeständig ohne zusätzliche Beschichtung — kein Rost, beständig gegen Alkali, Öle und Salze.",
        "Verzinkte Montageplatte, 4 Befestigungslaschen und Schrauben im Lieferumfang.",
        "Wandmontage über außenliegende Laschen — ohne Bohren durch die Rückwand, Schutzart bleibt erhalten.",
        "Schwenkbare Tür mit Verriegelung serienmäßig; Sicherheitsschloss-Set als Zubehör, passt auf alle Fleet-Gehäuse.",
        "Sofort versandfertig, Lieferfrist 1-3 Tage; Sonderbearbeitung und Individualisierung auf Anfrage.",
        "12 Größen von 300x200x130 bis 800x600x260 mm, RAL 7035 Grau / RAL 9005 Schwarz, Deckel geschlossen oder transparent.",
        "Zulassungen CE und RoHS, Entflammbarkeit UL 94 HB.",
        "ABS ist funkdurchlässig — auch für Router, WLAN- und Netzwerktechnik geeignet.",
    ],
    technical_info=[
        "Außenmaß 300x200x130 mm, Innenmaß 258x151x116 mm, Gewicht 1,4 kg",
        "Material: Deckel ABS/PC, Unterteil ABS, halogenfrei, UV-beständig",
        "Schutzart IP65 · Schlagfestigkeit IK08 · UL 94 HB · CE, RoHS",
        "Temperaturbereich -35 °C bis +65 °C",
        "Serie Fleet gesamt: 240x180x130 bis 800x600x260 mm; RAL 7035, 9005, 3020, 5021",
    ],
    target_group=(
        "Doppelte Zielgruppe. PROFI/B2B: Elektroinstallateure, Schaltanlagen- und Maschinenbau, "
        "Industrie und Betreiber. DIY/PROSUMER: Werkstatt, Garten, Pool- und Pumpentechnik, "
        "PV/Solar, Wallbox und E-Auto-Laden, CNC-Steuerungen, IT- und Netzwerktechnik."
    ),
    target_problems=(
        "Stahlblechschränke sind teuer, schwer und rostanfällig; günstige Kunststoffkästen wirken "
        "unsicher bei Wetter, Schlag und Temperatur. Gesucht wird ein Gehäuse, das draußen dicht "
        "hält, sich leicht montieren lässt, die Elektronik sicher aufnimmt und lange hält."
    ),
    competitors=[
        {"asin": "EYPINS", "note": "günstige IP65/IP67-Kunststoffkästen, hohe Bewertungszahl"},
        {"asin": "CHENGPI", "note": "Anschlussdose/Abzweigdose transparent"},
        {"asin": "ELEKTRO-PLAST", "note": "Verteilerkasten Außen, abschließbar"},
        {"asin": "RSE", "note": "ABS Kunststoff-Gehäuse IP65, Wandschrank"},
        {"asin": "CAMWAY", "note": "IP67 Verteilerkasten mit Montagezubehör"},
    ],
    rufus_qa=[
        {"q": "Ist er wetterfest?", "a": "IP65 und PUR-Dichtung, einsetzbar von -35 °C bis +65 °C."},
        {"q": "Wie groß ist das Gehäuse?", "a": "Außen 300x200x130 mm, innen 258x151x116 mm."},
        {"q": "Ist es schwer?", "a": "1,4 kg — rund 50 % leichter als Stahlblech."},
        {"q": "Ist eine Montageplatte dabei?", "a": "Ja, verzinkte Stahl-Montageplatte im Lieferumfang."},
        {"q": "Ist es für den Außeneinsatz geeignet?", "a": "Ja, IP65 und UV-beständig für innen und außen."},
    ],
    good_reviews=[
        "Guter Verteilerkasten, auch noch formstabil bei der momentanen Hitze.",
        "Top Qualität (600x400x200 mm, Grau).",
        "Verteilerkasten für draußen — alles so wie es sein soll.",
        "Top Preis-Leistung.",
        "Passt exakt für NEMA-23-Schrittmotortreiber und CNC-Steuerung; Montageplatte ließ sich bohren und Gewinde schneiden.",
        "Gehäuse für ein Auto-Ladegerät genutzt.",
        "ABS ist funkdurchlässig und tief genug für IT-Technik, Router, WLAN und DECT.",
    ],
    bad_reviews=[
        "Mitgelieferte kleine Schrauben zu schwach — 2 von 8 beim Anziehen abgebrochen.",
        "Kratzer in der transparenten Tür bereits bei Lieferung.",
    ],
)


# ===== KW-geführte Copy (Deutsch) =====

TITLE = ('BOXEXPERT Verteilerkasten außen wasserdicht [ABS Kunststoff IP65 Gehäuse] schwarz '
         '(Serie Fleet) 300x200x130mm | Schaltschrank außen | Wandschrank | Industriegehäuse | '
         'Leergehäuse')

BULLETS = [
    "<b>RUND 50 % LEICHTER ALS STAHLBLECH</b> — Das ABS-Gehäuse der Serie Fleet bringt bei "
    "gleicher Gehäusegröße nur rund die Hälfte auf die Waage: dieses Modell wiegt 1,4 kg. Das "
    "spart Aufwand bei Transport, Handling und Wandmontage. Zusätzlich bleibt das Gehäuse ganz "
    "ohne weitere Beschichtung korrosionsbeständig — kein Rost, auch nach Jahren im Freien.",

    "<b>WASSERDICHT NACH IP65 — IK08 SCHLAGFEST</b> — Wasserdicht nach Schutzart IP65: "
    "staubdicht und geschützt gegen Strahlwasser aus jeder Richtung, dazu schlagfest nach IK08. "
    "Für die Dichtheit sorgt eine eingeschäumte "
    "PUR-Dichtung, die verschleißarm bleibt und auch bei häufigem Öffnen der Tür elastisch und "
    "witterungsbeständig ist.",

    "<b>MONTIERT, OHNE DIE DICHTHEIT ZU ÖFFNEN</b> — Vier außenliegende Befestigungslaschen und "
    "die passenden Schrauben liegen bei: Sie montieren an der Wand, ohne durch die Gehäuserückwand "
    "zu bohren — die Schutzart und damit der Schutz der innenliegenden Komponenten bleibt "
    "erhalten. Dazu eine verzinkte Stahl-Montageplatte für Ihre Elektronik. Auspacken, "
    "aufbauen, montieren — ohne Zusatzkauf.",

    "<b>VON -35 °C BIS +65 °C EINSATZBEREIT</b> — Halogenfrei, UV-beständig und formstabil auch "
    "bei sommerlicher Hitze, dazu beständig gegen Alkali, Öle und Salze. Die schwenkbare Tür ist "
    "serienmäßig mit Dreikant-Schlüsselverriegelung ausgestattet und schützt vor unbefugtem "
    "Zugriff; ein Sicherheitsschloss ist optional erhältlich.",

    "<b>12 GRÖSSEN, PASSEND FÜR IHR PROJEKT</b> — Erhältlich von 300x200x130 bis 800x600x260 mm, "
    "in RAL 7035 Grau und RAL 9005 Schwarz, mit geschlossenem oder transparentem Deckel. Bewährt "
    "in Maschinenbau, Werkstatt und Außenbereich — und dank funkdurchlässigem ABS auch für "
    "Router-, WLAN- und Netzwerktechnik geeignet. Gehäusetechnik von BOXEXPERT aus Norderstedt.",
]


IMAGES = [
    AIImagePlanItem(
        name="Bild 1 — Main Hero (3 Varianten für A/B-Test)",
        role="hero",
        background="Reines Weiss mit angeschnittenem BOXEXPERT-blauem Flächenblock #1E6FC4. Bei allen 3 Varianten identisch, damit der Split-Test nur die Komposition misst.",
        purpose="Klick gewinnen in einem Raster austauschbarer schwarzer Kunststoffkästen.",
        visual=(
            "Alle 3 Varianten mocken, Sieger behalten. Je Variante EINE Aussage, Produkt dominant, "
            "Gehäuse exakt wie real (Serie Fleet, schwenkbare Tür, Verriegelung), 3/4-Iso-Ansicht "
            "mit sauberem Schlagschatten. Amazon-Slot 1 bleibt textfrei — dies sind die CTR-Mains "
            "für den A/B-Test dagegen.\n\n"

            "VARIANTE A — DAS LEICHTGEWICHT\n"
            "Fleet-Gehäuse geschlossen, daneben die Silhouette eines klobigen Stahlschranks. "
            "Gewichts-Chip am Gehäuse: '1,4 kg'.\n"
            "BADGE oben links (Blau/weiss): '50 % LEICHTER'.\n"
            "Gewinnt, weil kein Wettbewerber im Raster den einzigen echten Grund gegen Stahlblech nennt.\n\n"

            "VARIANTE B — DAS INNENLEBEN\n"
            "Gehäuse offen, Tür aufgeschwenkt, innen eine saubere Installation auf der verzinkten "
            "Montageplatte (Reihenklemmen, Automaten, farbige Adern).\n"
            "BADGE unten rechts (Navy/weiss): 'MONTAGEPLATTE INKLUSIVE'.\n"
            "Gewinnt, weil gekauft wird, was hineinkommt — fast alle zeigen nur den zu Kasten.\n\n"

            "VARIANTE C — WETTERBEWEIS\n"
            "Gehäuse an der Aussenwand, Wassertropfen perlen ab, dahinter unscharf Fassade oder "
            "PV-Anlage. Realistisch Regen/Strahlwasser, kein Untertauchen, kein Ozean.\n"
            "BADGE oben rechts (Blau/weiss): 'WASSERDICHT · IP65'.\n"
            "Gewinnt, weil 'hält das draussen dicht?' die Frage Nr. 1 ist.\n\n"

            "Über alle 3: Produkt dominant, Badge ca. 6 % der Fläche, gleiche Lichtstimmung."
        ),
        overlay="(eine Aussage je Variante)",
        overlay_sub="3 Hero-Varianten — A/B testen, Sieger behalten.",
        props=[
            "A: Fleet-Gehäuse + Stahlschrank-Silhouette + Chip '1,4 kg'",
            "B: Gehäuse offen mit Installation auf der Montageplatte",
            "C: wandmontiertes Gehäuse mit abperlenden Tropfen + PV unscharf",
        ],
        lighting="Helles Studiolicht 5000 K, weiche Kante auf der Kontur, damit Schwarz auf Weiss nicht absäuft. Bei allen 3 identisch.",
        why_it_works=(
            "Drei Kaufauslöser: A die harte Zahl gegen Stahlblech, B der fertige Einbau samt "
            "Lieferumfang, C der Wetterzweifel. Je eine Aussage — auf dem Thumbnail sofort lesbar."
        ),
        ctr="Variante A und C zielen auf den Klick im Raster, B auf Qualifizierung des Traffics.",
    ),
    AIImagePlanItem(
        name="Bild 2 — Was es ist: der Schaltschrank im Detail",
        role="hook",
        background="Weiss, freigestelltes Gehäuse halb geöffnet, dezenter blauer Rahmen",
        purpose="In einem Bild beantworten: Was ist das, woraus besteht es, was bekomme ich?",
        visual=(
            "Grosse, freigestellte 3/4-Ansicht des Gehäuses mit geöffneter Tür, ringsum schlanke "
            "Callout-Linien in Blau auf die Bauteile:\n"
            "  • Schwenkbare Tür mit Verriegelung — schützt vor unbefugtem Zugriff\n"
            "  • Eingeschäumte PUR-Dichtung — hält dicht nach IP65\n"
            "  • Verzinkte Montageplatte — für Ihre Elektronik, liegt bei\n"
            "  • Domen im Gehäuse — Platte einfach aufschrauben\n"
            "  • 4 Befestigungslaschen + Schrauben — liegen bei\n"
            "  • ABS-Gehäuse, Deckel ABS/PC — halogenfrei, UV-beständig\n\n"
            "Unten eine schmale Masszeile: 'Aussen 300 x 200 x 130 mm · Innen 258 x 151 x 116 mm "
            "· 1,4 kg'.\n\n"
            "Sachlich und aufgeräumt — dieses Bild muss den Zoom aushalten."
        ),
        overlay="WAS SIE BEKOMMEN.",
        overlay_sub="Gehäuse, verzinkte Montageplatte, 4 Befestigungslaschen und Schrauben.",
        props=["Gehäuse offen freigestellt", "6 Bauteil-Callouts", "Masszeile aussen/innen/Gewicht"],
        lighting="Flaches, gleichmässiges Studiolicht ohne harte Schatten. Technische Klarheit vor Stimmung.",
        why_it_works=(
            "Der Käufer sieht auf einen Blick, was ein Leergehäuse überhaupt ist und was im Karton "
            "liegt. Das nimmt die Unsicherheit 'muss ich noch Zubehör dazukaufen?' und macht den "
            "Wert gegenüber namenlosen Billigkästen sofort sichtbar."
        ),
        cvr="Stärkstes Bild gegen Kaufabbruch durch Unklarheit über den Lieferumfang.",
    ),
    AIImagePlanItem(
        name="Bild 3 — Warum kaufen 1: rund 50 % leichter als Stahlblech",
        role="educate",
        background="Helles Blaugrau #EEF4FA mit angeschnittenem blauem Flächenblock",
        purpose="Den Kern-Kaufgrund beweisen: halbes Gewicht, volle Belastbarkeit.",
        visual=(
            "Klarer Split. LINKS ein Stahlblech-Schaltschrank, grau und massiv, mit kleinen "
            "Chips 'schwer', 'rostanfällig'. RECHTS das Fleet-Gehäuse, einhändig getragen, mit "
            "Chips '1,4 kg', 'kein Rost'.\n\n"
            "Dazwischen eine schlanke Waagegrafik in Blau mit der Kernzahl: 'rund 50 % weniger "
            "Gewicht bei gleicher Gehäusegröße'.\n\n"
            "Fair bleiben, kein Spott über Stahl."
        ),
        overlay="50 % LEICHTER ALS STAHL.",
        overlay_sub="Gleiche Gehäusegröße, halbes Gewicht — und ganz ohne Rost.",
        props=["Stahlschrank mit Nachteils-Chips", "Fleet einhändig getragen", "Waagegrafik in Blau"],
        lighting="Gleichmässiges Technik-Licht, leichte Aufhellung von rechts. Sachlich statt dramatisch.",
        why_it_works=(
            "Logistik, Handling und Korrosion sind die realen Schmerzen bei Stahlblech. "
            "'Rund 50 %' ist die Zahl, die hängen bleibt — und der faire Ton erzeugt "
            "Ingenieurs-Vertrauen statt Werbe-Reflex."
        ),
    ),
    AIImagePlanItem(
        name="Bild 4 — Warum kaufen 2: wasserdicht nach IP65 und schlagfest",
        role="trust",
        background="Weiss mit schmalem blauem Fussbalken",
        purpose="Alle Schutzwerte auf einen Blick — die Spec-Wand für Profis, die Beruhigung für DIY.",
        visual=(
            "Freigestelltes geschlossenes Gehäuse mittig, Wassertropfen perlen ab. Darum ein "
            "sauberes Icon-Raster, Wert in Navy, Icon in Blau:\n"
            "  • IP65 — wasserdicht, staubdicht, gegen Strahlwasser geschützt\n"
            "  • IK08 — schlagfest\n"
            "  • -35 °C bis +65 °C\n"
            "  • UL 94 HB — Entflammbarkeit\n"
            "  • CE / RoHS\n"
            "  • halogenfrei + UV-beständig\n\n"
            "Rechts angeschnitten ein Makro der eingeschäumten PUR-Dichtung im Deckelfalz als "
            "Beweis, woher die Dichtheit kommt."
        ),
        overlay="WASSERDICHT. IP65. IK08.",
        overlay_sub="Staubdicht, strahlwassergeschützt, schlagfest — geprüft nach CE und RoHS.",
        props=["geschlossenes Gehäuse mit Tropfen", "6 Spec-Icons", "Makro PUR-Dichtung"],
        lighting="Flaches, gleichmässiges Licht auf dem Raster, gerichtetes Licht auf dem Dichtungs-Makro.",
        why_it_works=(
            "Im Elektro-Umfeld entscheiden Kennwerte. Sechs Normwerte plus der sichtbare Beweis "
            "der PUR-Dichtung machen Qualität prüfbar statt behauptet — genau der Unterschied zu "
            "den namenlosen Kästen im Raster."
        ),
    ),
    AIImagePlanItem(
        name="Bild 5 — Warum kaufen 3: montiert, ohne die Dichtheit zu öffnen",
        role="educate",
        background="Weiss, Flatlay oben, Montageszene unten",
        purpose="Den Lieferumfang zeigen und den unterschätzten Vorteil: Wandmontage ohne Schutzartverlust.",
        visual=(
            "OBEN — LIEFERUMFANG als beschriftetes Flatlay: Gehäuse, verzinkte Montageplatte, "
            "4 Befestigungslaschen, Schrauben, Schlüssel.\n\n"
            "UNTEN — DER ENTSCHEIDENDE PUNKT in zwei Bildern nebeneinander:\n"
            "  LINKS: die Laschen werden AUSSEN am Gehäuse eingehängt und an die Wand geschraubt. "
            "Grüner Haken, Text: 'Gehäusewand bleibt geschlossen — IP65 bleibt erhalten.'\n"
            "  RECHTS (als Kontrast, neutral gezeichnet): eine durch die Rückwand gebohrte "
            "Befestigung mit Wassereintritt-Pfeil. Grauer Hinweis: 'Bohren durch die Rückwand "
            "beeinträchtigt die Schutzart.'\n\n"
            "Hinweis fürs Design: Schrauben realistisch zeigen, nicht als Schwerlast-Set "
            "inszenieren — in Rezensionen wurden die kleinen Schrauben kritisiert."
        ),
        overlay="MONTIERT, OHNE ZU BOHREN.",
        overlay_sub="4 außenliegende Laschen inklusive — die Gehäusewand bleibt dicht.",
        props=["Flatlay Lieferumfang", "verzinkte Montageplatte", "4 Laschen + Schrauben", "Montage aussen vs. Bohrung durch die Rückwand"],
        lighting="Weiches, schattenarmes Flatlay-Licht oben, klares Werkstattlicht in der Montageszene.",
        why_it_works=(
            "Dieser Vorteil steht auf der Herstellerseite, aber in keinem Wettbewerbs-Listing: "
            "Wer durch die Rückwand bohrt, zerstört die Schutzart. Die mitgelieferten "
            "Aussenlaschen lösen das — ein echtes Profi-Argument, das auch Heimwerker sofort "
            "verstehen."
        ),
        cvr="Adressiert zugleich die häufigste Frage 'Ist eine Montageplatte dabei?'.",
    ),
    AIImagePlanItem(
        name="Bild 6 — Für wen: Anwendungen von Industrie bis Heimwerker",
        role="desire",
        background="Sechs Realfoto-Kacheln mit blauen Label-Balken (Website-Bildsprache)",
        purpose="Beide Zielgruppen gleichzeitig abholen — Profi sieht Industrie, DIY das eigene Projekt.",
        visual=(
            "Raster aus sechs Anwendungskacheln, je mit angeschnittenem blauem Label-Balken:\n"
            "  • MASCHINENBAU — Steuerung im Schaltanlagenbau\n"
            "  • WERKSTATT — Unterverteilung an der Wand\n"
            "  • AUSSENBEREICH — Gehäuse an der Hauswand im Regen\n"
            "  • PV UND WALLBOX — neben Solarmodulen bzw. Ladepunkt\n"
            "  • GARTEN UND PUMPE — Pool- und Bewässerungstechnik\n"
            "  • IT UND NETZWERK — Router im Gehäuse, Hinweis 'ABS ist funkdurchlässig'\n\n"
            "Echte Szenen, keine Symbolbilder. Menschen nur als Hände oder Arbeitssituation."
        ),
        overlay="WERKSTATT. INDUSTRIE. OUTDOOR.",
        overlay_sub="Vom Schaltanlagenbau bis zur Wallbox — dank ABS auch für WLAN-Technik.",
        props=["6 Anwendungskacheln", "blaue Label-Balken", "Hände beim Verdrahten", "PV-Modul / Wallbox", "Router im Gehäuse"],
        lighting="Realistisches Tageslicht je Szene, einheitliche Farbtemperatur über alle sechs Kacheln.",
        why_it_works=(
            "Das Produkt hat eine ungewöhnlich breite Zielgruppe. Sechs konkrete Szenen lassen "
            "Profi und Heimwerker sich gleichzeitig wiederfinden. Die Netzwerk-Kachel greift ein "
            "echtes Rezensions-Argument auf, das kein Wettbewerber bewirbt."
        ),
    ),
    AIImagePlanItem(
        name="Bild 7 — Welche Variante — und warum BOXEXPERT",
        role="close",
        background="Helles Blaugrau #EEF4FA oben, blaues Markenband unten",
        purpose="Die richtige Größe wählen lassen und mit Herkunft und Service abschliessen.",
        visual=(
            "OBEN — GRÖSSEN UND VARIANTEN: mehrere Fleet-Gehäuse nach Größe gestaffelt, "
            "Massangaben von 300x200x130 bis 800x600x260 mm, beim beworbenen Modell zusätzlich "
            "das Innenmass. Daneben vier kleine Kacheln: RAL 7035 Grau und RAL 9005 Schwarz, "
            "jeweils mit geschlossenem und transparentem Deckel. Kurzer Hinweis: 'Transparenter "
            "Deckel — Anzeigen im Blick, ohne die Tür zu öffnen.'\n\n"
            "UNTEN — MARKENBAND in BOXEXPERT-Blau mit Logo und drei ruhigen Punkten:\n"
            "  • Gehäusetechnik aus Norderstedt bei Hamburg\n"
            "  • Zulassungen CE und RoHS\n"
            "  • Beratung, Zubehör und Sonderlösungen direkt vom Hersteller\n\n"
            "Ton: hanseatisch nüchtern, keine Superlative."
        ),
        overlay="12 GRÖSSEN. 4 FARBEN.",
        overlay_sub="Von 300x200x130 bis 800x600x260 mm — Deckel geschlossen oder transparent.",
        props=["Größenstaffel mit Massangaben", "4 Farb- und Deckel-Kacheln", "blaues Markenband mit Logo"],
        lighting="Gleichmässiges helles Licht, echte RAL-Töne ohne Farbverfälschung.",
        why_it_works=(
            "Bei einem Varianten-Listing entscheidet die richtige Größe über Kauf und Retoure. "
            "Der Markenabschluss liefert danach den Grund, zum Markenprodukt statt zum "
            "namenlosen Kasten zu greifen."
        ),
    ),
]


MODULES = [
    AIModule(
        name="Modul 1 — Markenbanner",
        role="a+_banner",
        headline="DAS ROBUSTE LEICHTGEWICHT.",
        body=(
            "Kunststoff-Schaltschrank statt Stahlblech: rund 50 % leichter, wasserdicht nach "
            "IP65, schlagfest nach IK08. Gehäusetechnik aus Norderstedt."
        ),
        visual="Breites Banner im Website-Look: freigestelltes Fleet-Gehäuse rechts, grosse Headline links auf weiss, angeschnittener blauer Flächenblock, Logo oben links.",
        alt="BOXEXPERT Serie Fleet Kunststoff-Schaltschrank, wasserdicht nach IP65 und schlagfest nach IK08.",
    ),
    AIModule(
        name="Modul 2 — Karussell (5 Kacheln): Warum Fleet",
        role="a+_carousel",
        headline="WARUM FLEET",
        body=(
            "Kachel 1: <b>50 % LEICHTER</b> — als Stahlblech, bei gleicher Größe.<br/>"
            "Kachel 2: <b>WASSERDICHT</b> — IP65, staubdicht &amp; strahlwassergeschützt.<br/>"
            "Kachel 3: <b>SCHLAGFEST</b> — IK08, eingeschäumte PUR-Dichtung.<br/>"
            "Kachel 4: <b>KEIN ROST</b> — korrosionsbeständig ohne Beschichtung.<br/>"
            "Kachel 5: <b>KOMPLETT</b> — Montageplatte, 4 Laschen &amp; Schrauben dabei."
        ),
        visual="5 quadratische Kacheln, blaue Akzentecke, schlanke Linien-Icons (Waage · Tropfen · Schild · Rost-durchgestrichen · Karton). Je Kachel maximal eine Zeile Text.",
        alt="Fünf A+ Kacheln: 50 Prozent leichter, wasserdicht nach IP65, schlagfest, rostfrei, kompletter Lieferumfang.",
    ),
    AIModule(
        name="Modul 3 — Banner: Fleet gegen Stahlblech",
        role="a+_banner",
        headline="50 % LEICHTER. VOLL BELASTBAR.",
        body=(
            "Stahlblech ist teuer und schwer. Fleet spart bei gleicher Gehäusegröße rund die "
            "Hälfte des Gewichts — und rostet nicht. Nur bei EMV-kritischen Anwendungen bleibt "
            "Metall die erste Wahl."
        ),
        visual="Vergleichsbanner: links Stahlschrank mit Chips (schwer, rostanfällig), rechts Fleet einhändig getragen mit Chips (1,4 kg, kein Rost), mittig eine Waagegrafik in Blau.",
        alt="A+ Banner mit dem Gewichtsvergleich zwischen Stahlblechschrank und dem ABS-Gehäuse der Serie Fleet.",
    ),
    AIModule(
        name="Modul 4 — Banner: Dichtheit und Türverriegelung",
        role="a+_banner",
        headline="WASSERDICHT. FEST. WETTERFEST.",
        body=(
            "Eine eingeschäumte PUR-Dichtung hält das Gehäuse wasserdicht nach IP65 — auch nach "
            "häufigem Öffnen. Einsatzbereit von -35 °C bis +65 °C. Die Tür ist serienmäßig "
            "verriegelt, ein Sicherheitsschloss gibt es als Zubehör."
        ),
        visual="Drei Detail-Makros nebeneinander: eingeschäumte PUR-Dichtung im Deckelfalz, Türverriegelung mit Schlüssel, abperlende Tropfen auf dem geschlossenen Gehäuse. Blaue Trennlinien.",
        alt="A+ Banner mit Makros der PUR-Dichtung, der Türverriegelung und des Strahlwasserschutzes.",
    ),
    AIModule(
        name="Modul 5 — Banner: Wandmontage ohne Schutzverlust",
        role="a+_banner",
        headline="MONTIERT, OHNE ZU BOHREN.",
        body=(
            "Vier außenliegende Befestigungslaschen und die passenden Schrauben liegen bei. Sie "
            "werden außen montiert — die Gehäusewand bleibt geschlossen und die Schutzart IP65 "
            "erhalten. Die verzinkte Montageplatte für Ihre Elektronik ist ebenfalls dabei."
        ),
        visual="Banner zweigeteilt: links Flatlay des Lieferumfangs (Gehäuse, Montageplatte, 4 Laschen, Schrauben, Schlüssel), rechts Montageszene mit aussen eingehängter Lasche an der Wand.",
        alt="A+ Banner zur Wandmontage über außenliegende Befestigungslaschen bei erhaltener Schutzart IP65.",
    ),
    AIModule(
        name="Modul 6 — Premium Q&A",
        role="a+_qa",
        headline="HÄUFIGE FRAGEN",
        body=(
            "<b>F.</b> Für den Außenbereich geeignet?<br/>"
            "<b>A.</b> Ja — wasserdicht nach IP65, UV-beständig, -35 °C bis +65 °C.<br/><br/>"
            "<b>F.</b> Welche Maße?<br/>"
            "<b>A.</b> Außen 300x200x130 mm, innen 258x151x116 mm, 1,4 kg.<br/><br/>"
            "<b>F.</b> Ist eine Montageplatte dabei?<br/>"
            "<b>A.</b> Ja, verzinkt — plus 4 Befestigungslaschen und Schrauben.<br/><br/>"
            "<b>F.</b> Lässt es sich abschließen?<br/>"
            "<b>A.</b> Türverriegelung serienmäßig, Sicherheitsschloss als Zubehör.<br/><br/>"
            "<b>F.</b> Auch für Router und WLAN?<br/>"
            "<b>A.</b> Ja — ABS ist funkdurchlässig, anders als ein Metallgehäuse."
        ),
        visual="Vertikale Frage-/Antwort-Liste, blaue Trennlinien, F. in Navy und A. in Blau. Bewusst kurze Antworten — je eine Zeile.",
        alt="Premium Q&A Modul mit fünf Kurzantworten zum BOXEXPERT Verteilerkasten der Serie Fleet.",
    ),
    AIModule(
        name="Modul 7 — Premium Vergleichstabelle",
        role="a+_comparison",
        headline="FLEET IM VERGLEICH",
        body=(
            "Vier Spalten: <b>BOXEXPERT Serie Fleet</b> · Stahlblech-Schaltschrank · Einfacher "
            "Kunststoffkasten · Abzweigdose.<br/><br/>"
            "Zeilen: Wasserdicht nach IP65 · Schlagfest IK08 · PUR-Dichtung · Gewicht · Rostfrei "
            "ohne Beschichtung · Montageplatte im Lieferumfang · Montage ohne Schutzverlust · "
            "Größen bis 800x600x260 mm · CE und RoHS.<br/><br/>"
            "Fleet-Spalte hellblau hinterlegen, Band 'GEHÄUSETECHNIK AUS DEM NORDEN'. "
            "Vergleichsspalten nur als Kategorie, keine Fremdmarken."
        ),
        visual="Standard Amazon Premium Vergleichstabelle, 4 Spalten, Kopfzeile Navy, Fleet-Spalte hellblau hinterlegt.",
        alt="Premium Vergleichstabelle der Serie Fleet gegenüber Stahlblechschrank, einfachem Kunststoffkasten und Abzweigdose.",
    ),
]


QA = [
    AIQA(q="Ist das Gehäuse wirklich für draußen geeignet?",
         a="Ja. Das Gehäuse ist wasserdicht nach Schutzart IP65 — staubdicht und geschützt gegen Strahlwasser aus jeder Richtung. Zusammen mit der eingeschäumten PUR-Dichtung, der UV-Beständigkeit und dem Temperaturbereich von -35 °C bis +65 °C ist es für den dauerhaften Außeneinsatz ausgelegt. Für dauerhaftes Untertauchen ist es nicht vorgesehen."),
    AIQA(q="Wie groß ist der Verteilerkasten innen und außen?",
         a="Außen 300x200x130 mm, nutzbares Innenmaß 258x151x116 mm, Gewicht 1,4 kg. Die Serie Fleet reicht von 300x200x130 bis 800x600x260 mm."),
    AIQA(q="Wie schwer ist das Gehäuse im Vergleich zu Stahlblech?",
         a="Dieses Modell wiegt 1,4 kg. Da das Unterteil aus ABS und der Deckel aus ABS/PC besteht, ergibt sich bei gleicher Gehäusegröße rund 50 % Gewichtsersparnis — spürbar bei Transport, Handling und Wandmontage."),
    AIQA(q="Was ist im Lieferumfang enthalten?",
         a="Das Gehäuse, eine Montageplatte aus verzinktem Stahl, vier Befestigungslaschen für die Wandmontage sowie die zugehörigen Schrauben und der Schlüssel für die Türverriegelung."),
    AIQA(q="Muss ich zur Wandmontage durch das Gehäuse bohren?",
         a="Nein. Die vier mitgelieferten Befestigungslaschen werden außen am Gehäuse eingehängt und an die Wand geschraubt. Die Gehäusewand bleibt geschlossen, sodass die Schutzart und damit der Schutz der innenliegenden Komponenten erhalten bleibt."),
    AIQA(q="Kann ich das Gehäuse abschließen?",
         a="Die schwenkbare Tür ist serienmäßig mit einer Türverriegelung inklusive Schlüssel ausgestattet und schützt vor unbefugtem Zugriff. Als Zubehör ist ein Sicherheitsschloss mit Griff und zwei Schlüsseln erhältlich, das auf alle Gehäuse der Serie Fleet passt."),
    AIQA(q="Rostet das Gehäuse im Außenbereich?",
         a="Nein. Das ABS-Gehäuse ist auch ohne zusätzliche Beschichtung resistent gegen korrosive Belastungen und zusätzlich beständig gegen Alkali, Öle und Salze — ein Vorteil gegenüber unbeschichteten Metallgehäusen im Außenbereich."),
    AIQA(q="Eignet sich das Gehäuse für Router, WLAN oder Netzwerktechnik?",
         a="Ja. ABS ist funkdurchlässig, anders als ein Metallgehäuse. Router, WLAN-Komponenten oder DECT-Technik lassen sich damit geschützt unterbringen, ohne den Funkempfang abzuschirmen."),
    AIQA(q="Welche Farben und Deckel-Varianten gibt es?",
         a="Unter anderem RAL 7035 Lichtgrau und RAL 9005 Schwarz, wahlweise mit geschlossenem oder transparentem Deckel. Ein transparenter Deckel hält Anzeigen und Automaten im Blick, ohne die Tür zu öffnen."),
]


# Backend-Keywords — stammreduziert, bytesparend. Keine Markennamen aus dem Titel, keine Superlative.
BACKEND = (
    "verteilerkasten aussen schaltschrank kunststoff ip65 gehaeuse industriegehaeuse leergehaeuse "
    "wandgehaeuse wandschrank abzweigdose sicherungskasten elektrogehaeuse abs schlagfest ik08 "
    "montageplatte verzinkt tuerverriegelung pur dichtung uv bestaendig halogenfrei wallbox "
    "photovoltaik solar garten pumpe werkstatt maschinenbau router wlan netzwerk 300x200x130"
)


def main() -> None:
    print("Lade BOXEXPERT + recherchierte Produkt-Achse…")
    cust = load_customer("boxexpert")
    brief = BRIEF
    OUT = HERE / f"{PLAN_NO}_{ASIN}_Image Plan.pdf"
    print(f"  Produkt: {brief.product_name}")
    print(f"  ASIN: {brief.asin}  Marktplatz: {cust.marketplace}")
    print(f"  USPs={len(brief.usps)} KWs={len(brief.all_keywords)} Q&A={len(brief.rufus_qa)} "
          f"Reviews=+{len(brief.good_reviews)}/-{len(brief.bad_reviews)}")

    builder = BriefBuilder(cust, brief, OUT, ai=None)
    builder._ai_title = TITLE
    builder._ai_bullets = BULLETS
    builder._ai_images = IMAGES
    builder._ai_modules = MODULES
    builder._ai_qa = QA
    builder._ai_backend = BACKEND
    builder.copy_source_label = "Hand-written senior copy (recherchiert, DE)"

    print("Baue Branded PDF…")
    pdf_path = builder.build()
    size_kb = pdf_path.stat().st_size // 1024
    import re
    pages = len(re.findall(rb'/Type\s*/Page[^s]', pdf_path.read_bytes()))
    print(f"Gebaut: {pdf_path}")
    print(f"  Seiten: {pages}  Größe: {size_kb} KB")


if __name__ == "__main__":
    main()
