"""Jotti Lederreiniger 500 ml — Image Plan 08
Hand-written senior copy injected into the branded ReportLab pipeline.

Marketplace: amazon.de.

LANGUAGE SPLIT (the standard):
  • ENGLISH — art-direction / strategy fields the designer reads:
    image purpose, background, visual, props, lighting, why_it_works, ctr, cvr,
    and module visual.
  • GERMAN — marketplace, customer-facing text the shopper reads:
    TITLE, BULLETS, image overlay, overlay_sub, module headline, module body,
    QA, and BACKEND keywords.

OVERLAY RULE: sell the OUTCOME, not the action. Every on-image overlay leads with
the result the buyer wants — clean, fresh, ready-to-condition leather. Smooth
German, no gimmick punctuation, no middots. Hard limits (auto-linted on build):
  overlay ≤ 30 chars AND ≤ 5 words · overlay_sub ≤ 90 chars
  module headline ≤ 38 chars · bullet head <b>…</b> ≤ 45 chars · TITLE ≤ 200

KEY ANGLE — this is STEP 1 of leather care: "erst reinigen, dann pflegen".
Cross-sell the Jotti Lederbalsam as the pairing (clean → then condition). A
dedicated A+ module shows the 2-step routine (Reiniger → Balsam).

Verified facts:
  - 500 ml; schonender Reiniger für Glattleder & Kunstleder
  - entfernt Schmutz, Fett, Staub & leichte Flecken
  - für Auto(-sitze), Sofa, Schuhe, Taschen & Möbel
  - gründliche Reinigung ohne unnötige Materialbelastung
  - Deutsche Manufakturqualität; Schritt 1 vor der Pflege mit Lederbalsam

Compliance: no $/€ prices, no URL/.com/.de, no #1/beste/garantiert, no medical
claims (verhindert/heilt), no false claims.
"""
from __future__ import annotations
import sys
from pathlib import Path

# This script lives at customers/<brand>/products/<product>/run.py — self-contained.
HERE = Path(__file__).resolve().parent          # the product folder
ROOT = HERE.parents[5]                           # project root (Claude_Code/)
sys.path.insert(0, str(ROOT))

from tools.brief_app.core.customers import load_customer
from tools.brief_app.core.excel_parser import parse_excel
from tools.brief_app.core.pdf_builder import BriefBuilder
from tools.brief_app.core.ai import AIImagePlanItem, AIModule, AIQA


EXCEL = HERE / "listing.xlsx"
PLAN_NO = "08"


# ===== KW-led, marketing-optimized DE copy (customer-facing) =====

# Title is HTML-escaped, so literal "&" counts as 1 char. Keep ≤200 real chars. German.
TITLE = (
    "Jotti Lederreiniger 500 ml — schonende Lederreinigung für Auto Sofa Schuhe & Taschen "
    "· entfernt Schmutz, Fett & Staub · für Glattleder & Kunstleder · erst reinigen, dann "
    "pflegen · Deutsche Manufaktur"
)

BULLETS = [
    "<b>LEDER WIEDER SAUBER</b> — Löst Schmutz, Fett, Staub und leichte Flecken und macht "
    "Autositze, Ledercouch und Lederschuhe wieder sauber, matt-frisch und griffig.",

    "<b>ERST REINIGEN, DANN PFLEGEN</b> — Schritt 1 der Lederpflege: erst gründlich reinigen, "
    "dann mit dem Jotti Lederbalsam pflegen – so zieht die Pflege in sauberes Leder ein.",

    "<b>SCHONEND ZUM LEDER</b> — Reinigt gründlich ohne unnötige Materialbelastung: die "
    "milde Rezeptur säubert das Leder, statt es auszutrocknen oder anzugreifen.",

    "<b>FÜR GLATT- &amp; KUNSTLEDER</b> — Ein Lederreiniger für Auto-Ledersitze, Lenkrad, "
    "Ledersofa, Schuhe, Taschen und Möbel aus echtem Leder wie aus Kunstleder.",

    "<b>EINFACH AUFTRAGEN, ABWISCHEN</b> — Auf ein Tuch geben, sanft über das Leder führen, "
    "abnehmen – fertig. 500 ml für viele Anwendungen. Deutsche Manufaktur.",
]


IMAGES = [
    AIImagePlanItem(
        name="Bild 1 — Main Hero (3 Optionen für A/B-Test)",
        role="hero",
        background="Warm cream backdrop (#EFE6D9) with soft side-light; aged wood in the bottom 15% band for a manufactory feel. Identical backdrop across all 3 options for a clean split-test.",
        purpose="Win the click in the amazon.de leather-CLEANER grid — signal clean+fresh result and stand out next to generic cleaner bottles.",
        visual=(
            "Designer mocks up ALL 3 options. Brand picks the winner via Amazon Manage Your Experiments. "
            "Each option: ONE callout, ONE action cue, ONE prop — clean, never stacked.\n\n"
            "▸ OPTION A — BEFORE/AFTER (wins on proof)\n"
            "500 ml bottle centered (label legible, slight 3/4 turn, ~55% of frame). Behind it a car "
            "leather seat split diagonally: left grimy/matte/dull with a dirt film, right clean/fresh/even. "
            "A microfiber cloth lifting a visible grey dirt smudge at the dividing line.\n"
            "CALLOUT top right: badge 'LEDER WIEDER SAUBER.' (brown #8B5A2B, white type).\n\n"
            "▸ OPTION B — CLOTH LIFTS DIRT (wins on the satisfying result)\n"
            "Bottle left; a hand (hand only, no face) wipes a leather sofa with a cloth, a clean streak "
            "appearing behind the wipe, a grey soiled edge on the cloth.\n"
            "CALLOUT top left: 'SCHMUTZ LÖST SICH.' (dark #2F2A26, white type).\n\n"
            "▸ OPTION C — USE-CASE STACK (wins on versatility)\n"
            "Bottle centered, 4 use-case icons radiating out: car · sofa · shoes · bags (thin brown line icons).\n"
            "CALLOUT bottom right: 'AUTO, SOFA, SCHUHE.' (brown #8B5A2B).\n\n"
            "All 3: bottle dominant ~55%, callout ~6%, same light / same backdrop."
        ),
        overlay="LEDER WIEDER SAUBER.",
        overlay_sub="Schmutz, Fett und Staub lösen sich – Leder wieder sauber und frisch.",
        props=[
            "OPTION A: bottle + split car-leather seat (grimy/clean) + cloth lifting dirt + badge",
            "OPTION B: bottle + hand + cloth wiping leather sofa + clean streak + soiled cloth edge",
            "OPTION C: bottle + 4 use-case icons (car/sofa/shoes/bags) + badge",
        ],
        lighting="Warm side-light from camera-right (3000–3500K), rim light on the bottle so the label pops. Same light across all 3 options.",
        why_it_works=(
            "Three triggers against three buyer motives: A delivers the grimy→clean before/after proof "
            "(the strongest signal in the leather-cleaner grid), B shows the satisfying dirt-lift moment, "
            "C shows versatility. One callout, one action cue, one prop — readable on a mobile thumbnail."
        ),
        ctr="The grimy→clean car-seat split plus 'LEDER WIEDER SAUBER.' beats competitors' static bottles in the DE grid; visible dirt-lift is the strongest click promise for Lederreiniger Auto, Sofa and Schuhe.",
        cvr="Instant clarity on product type (cleaner, not conditioner), job (removes dirt) and result (clean, fresh leather) cuts bounce; the manufactory setting builds purchase trust.",
    ),
    AIImagePlanItem(
        name="Bild 2 — Hook: Der Schmutz löst sich (Cloth lifts dirt)",
        role="hook",
        background="Cream #EFE6D9, aged wood, warm side-light.",
        purpose="Prove the core job in one satisfying frame — dirt visibly lifts off the leather onto the cloth.",
        visual=(
            "Tight macro: a hand (no face) wipes a soiled leather surface with a folded microfiber cloth. "
            "A CLEAN, brighter streak appears behind the cloth; the cloth carries a clear grey soiled edge. "
            "Bottle standing to the right as an anchor. Small caption strip at the bottom: "
            "'Schmutz · Fett · Staub'."
        ),
        overlay="SCHMUTZ LÖST SICH.",
        overlay_sub="Der Schmutz löst sich sichtbar und lässt sich mühelos abnehmen.",
        props=["hand + microfiber cloth", "soiled leather surface", "clean streak behind wipe", "grey soiled cloth edge", "Jotti bottle"],
        lighting="Even warm front-side light, soft shadow under the cloth so the clean streak reads.",
        why_it_works=(
            "The dirt-lift is the single most persuasive proof for a cleaner. Showing the grey on the cloth "
            "makes the result tangible and answers 'does it actually work?' in one frame."
        ),
        ctr="The visible clean streak hooks DE buyers searching 'lederreiniger stark' who want real cleaning power, not a mild wipe.",
        cvr="Concrete proof of the result lowers doubt and sets a realistic, believable expectation before purchase.",
    ),
    AIImagePlanItem(
        name="Bild 3 — Educate: Schonend / ohne Materialbelastung",
        role="educate",
        background="White with a brown accent band (#8B5A2B) in the footer.",
        purpose="Reassure that strong cleaning does NOT mean an aggressive product — schonend to the leather.",
        visual=(
            "Headline at top, then 3 reassurance tiles with line icons:\n"
            "  • GENTLE FORMULA — cleans without drying the leather\n"
            "  • NO HARSH ATTACK — protects the surface & grain\n"
            "  • GLATT + KUNSTLEDER — right for both leather types\n"
            "Bottle centered or right. Footer band (brown) carries the supporting line "
            "'gründliche Reinigung ohne unnötige Materialbelastung'."
        ),
        overlay="SCHONEND ZUM LEDER.",
        overlay_sub="Reinigt gründlich, ohne das Leder unnötig zu belasten.",
        props=["3 reassurance tiles with icons", "Jotti bottle", "brown footer band"],
        lighting="Flat, clean studio light — legibility over atmosphere.",
        why_it_works=(
            "Defuses the classic cleaner fear ('will a strong cleaner ruin my leather?'). Pairing 'gründlich' "
            "with 'schonend' resolves the tension and justifies the manufactory positioning."
        ),
        ctr="'Schonend' plus 'Glatt- & Kunstleder' widens relevance and reassures careful DE buyers scanning for a safe Lederreiniger.",
        cvr="Removes the damage worry — the top objection for a cleaner — so buyers feel safe using it on expensive leather.",
    ),
    AIImagePlanItem(
        name="Bild 4 — Desire: Before/After (verschmutzte → saubere Sitze)",
        role="desire",
        background="Aged wood, warm afternoon light.",
        purpose="Sell the visible transformation — grimy, matte seats/sofa become clean and fresh.",
        visual=(
            "Large before/after split of a real car leather seat OR a leather sofa. "
            "LEFT: grimy, dull, dusty, a visible dirt film and scuffed sheen. RIGHT: clean, even, "
            "matt-fresh, restored uniform surface. Divider centered; small bottle in the foreground corner. "
            "Cloth cue at the dividing line."
        ),
        overlay="WIEDER SAUBER & FRISCH.",
        overlay_sub="Matte, verschmutzte Sitze werden wieder sauber und frisch.",
        props=["car leather seat or leather sofa (split before/after)", "Jotti bottle (foreground)", "microfiber cloth", "dirt-film cue"],
        lighting="Warm afternoon side-light from camera-right, even so the clean side reads fresh and uniform.",
        why_it_works=(
            "The grimy→clean before/after is the strongest conversion signal in the cleaner category and is "
            "universally desirable for anyone with worn, dirty car leather or a used sofa."
        ),
        ctr="The dirty→clean seat transformation is instantly desirable for the huge 'lederpflege auto' / 'ledercouch' audience.",
        cvr="Visual proof of the outcome instead of a promise; sets a realistic expectation and drives the purchase.",
    ),
    AIImagePlanItem(
        name="Bild 5 — Trust/Cross-sell: 2-Schritt-Routine (Reiniger → Balsam)",
        role="trust",
        background="White with cream panels.",
        purpose="Anchor the product as STEP 1 of a routine and cross-sell the Jotti Lederbalsam as STEP 2.",
        visual=(
            "Two-step routine laid out left→right with a brown #8B5A2B arrow between:\n"
            "  SCHRITT 1 — REINIGEN: Jotti Lederreiniger bottle + cloth wiping a leather surface clean.\n"
            "  → ARROW →\n"
            "  SCHRITT 2 — PFLEGEN: Jotti Lederbalsam (companion product) being worked into the now-clean "
            "leather, restoring a supple sheen.\n"
            "Small caption under step 2: 'Pflege zieht in sauberes Leder besser ein'. "
            "Keep both products clearly Jotti-branded so the pairing reads as one system."
        ),
        overlay="ERST REINIGEN, DANN PFLEGEN.",
        overlay_sub="Erst reinigen, dann pflegen – so hält Ihr Leder länger schön.",
        props=["Jotti Lederreiniger bottle + cloth (step 1)", "brown arrow divider", "Jotti Lederbalsam (step 2)", "clean supple leather"],
        lighting="Clean even studio light — both steps equally readable on the thumbnail.",
        why_it_works=(
            "Frames the cleaner inside a repeatable routine, raising perceived value and seeding the "
            "Lederbalsam cross-sell. 'Clean first, then condition' is honest care advice that builds trust "
            "and lifts basket size."
        ),
        ctr="The 2-step visual signals a complete care system, attracting buyers who want to do leather care properly, not just spot-clean.",
        cvr="Cross-sells the Lederbalsam and reframes the purchase as the first step of a routine, increasing both conversion and add-on sales.",
    ),
    AIImagePlanItem(
        name="Bild 6 — Desire: Use-Case-Grid (Auto · Sofa · Schuhe · Taschen)",
        role="desire",
        background="Cream #EFE6D9, aged wood.",
        purpose="Show versatility — one cleaner for all the leather in the home and car.",
        visual=(
            "Clean 4-up grid of real leather scenes being wiped clean: car leather seat / lenkrad · "
            "leather sofa · leather shoes · leather bag. Each tile with a bottle / cloth cue. Bottle as an "
            "anchor center or bottom. Small label per tile (Auto · Sofa · Schuhe · Taschen)."
        ),
        overlay="AUTO, SOFA, SCHUHE.",
        overlay_sub="Für Auto, Sofa, Schuhe, Taschen und Möbel aus Leder.",
        props=["4 use-case scenes (car/sofa/shoes/bags)", "Jotti bottle", "cloth cues per tile"],
        lighting="Warm side-light, consistent across all 4 tiles.",
        why_it_works=(
            "Expands perceived value: one bottle cleans several expensive leather items, and it maps directly "
            "onto the broad DE search terms (Lederreiniger Auto, Sofa, Schuhe, Taschen)."
        ),
        ctr="Speaks to several search intents at once (lederreiniger auto, lederreiniger sofa, ledercouch), maximizing relevance in the grid.",
        cvr="More use cases = higher perceived value per bottle, which makes the purchase easier to justify.",
    ),
    AIImagePlanItem(
        name="Bild 7 — Close: Deutsche Manufaktur",
        role="close",
        background="Workshop scene: aged wood, brass, linen, warm side-light.",
        purpose="Close on brand identity — honest, artisanal manufactory quality.",
        visual=(
            "Mid-range workshop scene: hands (no face) wiping a beautiful leather surface clean with a cloth. "
            "On the wooden bench: Jotti Lederreiniger bottle (label legible), microfiber cloth, aged leather. "
            "Soft-focused workshop setting (brass, linen). A small handwritten note card carries the "
            "manufactory line."
        ),
        overlay="DEUTSCHE MANUFAKTUR.",
        overlay_sub="Traditionelle Lederpflege, mit der Hand gemacht.",
        props=["hands cleaning leather (no face)", "Jotti bottle", "microfiber cloth", "aged leather", "wooden bench / brass / linen", "handwritten note card"],
        lighting="Warm workshop side-light from camera-right, golden tone, lived-in — not staged.",
        why_it_works=(
            "Closes on the brand promise that matters before checkout: honest, artisanal manufactory quality. "
            "The hands-on-leather gesture is the visual metaphor for care and trust."
        ),
        ctr="The 'German manufactory' signal differentiates from anonymous import cleaners and attracts quality-conscious DE buyers.",
        cvr="Provenance and craft create the final trust that seals the purchase.",
    ),
]


MODULES = [
    AIModule(
        name="Modul 1 — Brand-Banner",
        role="a+_banner",
        headline="LEDER WIEDER SAUBER.",
        body=(
            "Jotti Lederreiniger löst Schmutz, Fett und Staub und macht Autositze, Ledercouch und "
            "Schuhe wieder sauber und frisch – schonend zum Leder. Schritt 1 vor der Pflege. "
            "Deutsche Manufaktur."
        ),
        visual="Wide cinematic workshop scene: aged wood, warm side-light, Jotti Lederreiniger bottle front-center, cloth wiping clean leather, brass soft-focused. Logo top left in brown #8B5A2B.",
        alt="Jotti Lederreiniger Flasche auf einer Holzbank in warmem Werkstattlicht, daneben sauber gewischtes Leder.",
    ),
    AIModule(
        name="Modul 2 — Banner: Die 2-Schritt-Routine (Reiniger → Balsam)",
        role="a+_banner",
        headline="ERST REINIGEN, DANN PFLEGEN.",
        body=(
            "Gepflegtes Leder beginnt mit sauberem Leder. <b>Schritt 1:</b> Mit dem Jotti Lederreiniger "
            "Schmutz, Fett und Staub gründlich entfernen. <b>Schritt 2:</b> Mit dem Jotti Lederbalsam "
            "nähren und schützen. So zieht die Pflege in sauberes Leder besser ein und das Leder bleibt "
            "länger schön."
        ),
        visual="Wide banner split in two: LEFT 'SCHRITT 1 REINIGEN' with the Lederreiniger + cloth wiping a car seat clean; brown arrow; RIGHT 'SCHRITT 2 PFLEGEN' with the Jotti Lederbalsam being worked into the clean leather. Warm side-light, both products clearly Jotti-branded.",
        alt="A+ Banner der 2-Schritt-Routine: erst mit Jotti Lederreiniger reinigen, dann mit Jotti Lederbalsam pflegen.",
    ),
    AIModule(
        name="Modul 3 — Carousel (4 Kacheln): Der Jotti-Vorteil",
        role="a+_carousel",
        headline="DER JOTTI-VORTEIL",
        body=(
            "Kachel 1: <b>LÖST SCHMUTZ &amp; FETT</b> — entfernt Schmutz, Fett, Staub und leichte Flecken.<br/>"
            "Kachel 2: <b>SCHONEND</b> — gründliche Reinigung ohne unnötige Materialbelastung.<br/>"
            "Kachel 3: <b>GLATT- &amp; KUNSTLEDER</b> — der richtige Reiniger für beide Ledertypen.<br/>"
            "Kachel 4: <b>SCHRITT 1</b> — erst reinigen, dann mit dem Jotti Lederbalsam pflegen."
        ),
        visual="4 square tiles, brown accent corner per tile, small line icons (cloth+dirt · shield · leather swatch · 1-2 steps).",
        alt="Vier-Kachel A+ Carousel mit den Jotti-Vorteilen: löst Schmutz und Fett, schonend, Glatt- und Kunstleder, Schritt 1.",
    ),
    AIModule(
        name="Modul 4 — Banner: Vorher / Nachher",
        role="a+_banner",
        headline="WIEDER SAUBER & FRISCH.",
        body=(
            "Matte, verschmutzte Ledersitze und Sofas werden wieder sauber, gleichmäßig und frisch. "
            "Der Jotti Lederreiniger nimmt den Schmutzfilm ab und bringt die natürliche Oberfläche zurück "
            "– schonend, ohne das Leder auszutrocknen."
        ),
        visual="Triptych: LEFT grimy dull leather seat (before), CENTER cloth wiping mid-clean, RIGHT clean fresh even leather (after). Warm light throughout.",
        alt="A+ Triptychon-Banner: Ledersitz vorher verschmutzt, beim Reinigen, nachher sauber und frisch.",
    ),
    AIModule(
        name="Modul 5 — Carousel (4 Kacheln): Für alles aus Leder",
        role="a+_carousel",
        headline="FÜR ALLES AUS LEDER",
        body=(
            "Kachel 1: <b>AUTO-LEDERSITZE</b> — reinigt Sitze und Lenkrad von Schmutz und Fett.<br/>"
            "Kachel 2: <b>LEDERSOFA</b> — nimmt den Alltagsschmutz von Couch &amp; Sessel.<br/>"
            "Kachel 3: <b>LEDERSCHUHE</b> — befreit Glatt- und Kunstlederschuhe von Staub.<br/>"
            "Kachel 4: <b>TASCHEN &amp; MÖBEL</b> — säubert Lieblingsstücke aus Leder."
        ),
        visual="4 identically composed use-case tiles, real leather scenes being wiped clean, brown accent corner per tile, consistent warm light.",
        alt="Vier-Kachel A+ Carousel der Anwendungsfälle: Auto-Ledersitze, Ledersofa, Lederschuhe, Taschen und Möbel.",
    ),
    AIModule(
        name="Modul 6 — Premium Q&A",
        role="a+_qa",
        headline="HÄUFIGE FRAGEN",
        body=(
            "<b>F.</b> Für welches Leder ist der Reiniger geeignet?<br/>"
            "<b>A.</b> Für Glattleder und Kunstleder: Auto-Ledersitze, Lenkrad, Sofa, Schuhe, Taschen "
            "und Möbel. Nicht für Wildleder/Veloursleder.<br/><br/>"
            "<b>F.</b> Trocknet der Reiniger das Leder aus?<br/>"
            "<b>A.</b> Nein. Er reinigt gründlich, aber schonend – ohne unnötige Materialbelastung.<br/><br/>"
            "<b>F.</b> Muss ich nach dem Reinigen pflegen?<br/>"
            "<b>A.</b> Wir empfehlen die 2-Schritt-Routine: erst mit dem Jotti Lederreiniger reinigen, "
            "dann mit dem Jotti Lederbalsam pflegen. So bleibt das Leder länger schön.<br/><br/>"
            "<b>F.</b> Wie wird der Reiniger angewendet?<br/>"
            "<b>A.</b> Auf ein weiches Tuch geben, sanft über das Leder führen und den gelösten Schmutz "
            "abnehmen. Bei stärkerer Verschmutzung wiederholen.<br/><br/>"
            "<b>F.</b> Wo wird Jotti hergestellt?<br/>"
            "<b>A.</b> In deutscher Manufakturqualität – traditionelle Lederpflege, handwerklich gemacht."
        ),
        visual="Vertical Q/A table, brown dividers between questions, small F./A. labels in dark #2F2A26.",
        alt="Premium Q&A Modul mit den häufigsten Fragen zum Jotti Lederreiniger.",
    ),
    AIModule(
        name="Modul 7 — Premium Comparison Chart",
        role="a+_comparison",
        headline="WARUM JOTTI",
        body=(
            "Vergleich über 4 Spalten: <b>Jotti Lederreiniger</b> · Standard-Lederreiniger · "
            "Allzweckreiniger · feuchtes Tuch.<br/><br/>"
            "Zeilen: Löst Schmutz, Fett &amp; Staub · Schonend (ohne Materialbelastung) · Für Glatt- "
            "&amp; Kunstleder · Teil einer Pflege-Routine (mit Balsam) · Deutsche Manufaktur.<br/><br/>"
            "Jotti-Spalte mit dezentem Braun-Ton hervorheben."
        ),
        visual="Standard Amazon Premium Comparison Chart, 4 product columns. Competitors named by category only, no brand names. Brown header row.",
        alt="Premium Vergleichstabelle: Jotti Lederreiniger vs. Standard-Lederreiniger, Allzweckreiniger und feuchtes Tuch.",
    ),
]


QA = [
    AIQA(q="Für welches Leder ist der Reiniger geeignet?",
         a="Für Glattleder und Kunstleder: Auto-Ledersitze, Lenkrad, Ledersofa, Lederschuhe, Taschen und Möbel. Nicht geeignet für Wildleder oder Veloursleder."),
    AIQA(q="Trocknet der Lederreiniger das Leder aus?",
         a="Nein. Der Reiniger säubert gründlich, aber schonend – gründliche Reinigung ohne unnötige Materialbelastung. Für den vollen Pflegeeffekt danach den Jotti Lederbalsam auftragen."),
    AIQA(q="Was entfernt der Reiniger?",
         a="Schmutz, Fett, Staub und leichte Flecken. Er nimmt den Alltagsschmutzfilm ab und bringt die natürliche, saubere Lederoberfläche zurück."),
    AIQA(q="Muss ich nach dem Reinigen pflegen?",
         a="Wir empfehlen die 2-Schritt-Routine: erst reinigen, dann pflegen. Nach dem Jotti Lederreiniger den Jotti Lederbalsam auftragen – die Pflege zieht in sauberes Leder besser ein und das Leder bleibt länger geschmeidig."),
    AIQA(q="Wie wird der Lederreiniger angewendet?",
         a="Den Reiniger auf ein weiches, sauberes Tuch geben, sanft über das Leder führen und den gelösten Schmutz abnehmen. Bei stärkerer Verschmutzung den Vorgang wiederholen. Vorher an einer unauffälligen Stelle testen."),
    AIQA(q="Kann ich den Reiniger für Autositze und Lenkrad verwenden?",
         a="Ja. Der Reiniger ist ideal für Auto-Ledersitze und das Lederlenkrad sowie für Ledersofa, Schuhe, Taschen und Möbel aus Glatt- und Kunstleder."),
    AIQA(q="Wie ergiebig sind die 500 ml?",
         a="Die 500 ml reichen für viele Anwendungen, da pro Reinigung nur wenig Produkt auf das Tuch nötig ist."),
    AIQA(q="Wo wird Jotti hergestellt?",
         a="In deutscher Manufakturqualität. Jotti steht für traditionelle, handwerklich gemachte Lederpflege."),
]


# Backend KWs — German, stem-deduped, byte-packed. Avoid brand/title duplicates & superlatives.
BACKEND = (
    "lederreiniger auto sofa ledercouch ledersitze reinigen lenkrad lederlenkrad "
    "innenraumreiniger autositze polsterreiniger kunstleder glattleder reiniger "
    "lederschuhe ledertasche lederpflege pflegen fleckentferner schmutz fett staub "
    "schonend materialschonend leather cleaner autopflege innenraum couch sessel "
    "möbel manufaktur deutsche routine balsam nachher sauber frisch"
)


def main() -> None:
    print("Loading Jotti customer + parsing Lederreiniger Excel…")
    cust = load_customer("jotti")
    brief = parse_excel(EXCEL)
    OUT = HERE / f"{PLAN_NO}_Jotti_Lederreiniger_Image Plan.pdf"
    real_title_len = len(TITLE.replace("&amp;", "&"))
    print(f"  Product: {brief.product_name}")
    print(f"  ASIN: {brief.asin}  Marketplace: {cust.marketplace}")
    print(f"  USPs={len(brief.usps)} KWs={len(brief.all_keywords)} reviews=+{len(brief.good_reviews)}/-{len(brief.bad_reviews)}")
    print(f"  TITLE real chars (de-escaped): {real_title_len}")

    builder = BriefBuilder(cust, brief, OUT, ai=None)
    builder._ai_title = TITLE
    builder._ai_bullets = BULLETS
    builder._ai_images = IMAGES
    builder._ai_modules = MODULES
    builder._ai_qa = QA
    builder._ai_backend = BACKEND
    builder.copy_source_label = "Hand-written senior copy (DE, conversion)"

    print("Building branded PDF…")
    pdf_path = builder.build()
    size_kb = pdf_path.stat().st_size // 1024
    import re
    pages = len(re.findall(rb'/Type\s*/Page[^s]', pdf_path.read_bytes()))
    print(f"Built: {pdf_path}")
    print(f"  Pages: {pages}  Size: {size_kb} KB")


if __name__ == "__main__":
    main()
