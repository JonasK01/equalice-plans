"""Jotti Pfotenbalsam 100 ml (Tiegel, zuhause) — Image Plan 11
Hand-written senior copy injected into the branded ReportLab pipeline.

Marketplace: amazon.de.

LANGUAGE SPLIT (the standard):
  • ENGLISH — art-direction / strategy fields the designer reads:
    background, purpose, visual, props, lighting, why_it_works, ctr, cvr,
    and module visual.
  • GERMAN — marketplace, customer-facing text the shopper reads:
    TITLE, BULLETS, image overlay, overlay_sub, module headline, module body,
    QA, and BACKEND keywords.

OVERLAY RULE: sell the OUTCOME, not the action. Every on-image overlay leads
with the result the buyer wants — geschützte, weiche, gesunde Pfoten. Smooth
German, no "Wort? Wort." gimmicks, no "·" middots on-image. Hard limits
(auto-linted on build):
  overlay ≤ 30 chars AND ≤ 5 words · overlay_sub ≤ 90 chars
  module headline ≤ 38 chars · bullet head <b>…</b> ≤ 45 chars · TITLE ≤ 200

Verified facts (from listing.xlsx + brief):
  - Pfotenbalsam 100 ml TIEGEL — Pfotenpflege für HUNDE & KATZEN, für zuhause (ergiebig)
  - pflegt trockene, raue & rissige Ballen; bildet einen schützenden Pflegefilm
  - SCHUTZ bei HITZE & heißem Asphalt (Sommer) UND bei Kälte, Schnee & Streusalz (Winter)
  - natürliche Rezeptur (Bienenwachs & pflegende Öle); zieht schnell ein
  - Deutsche Manufakturqualität

FORMAT DIFFERENTIATION: this is the 100 ml JAR (home use). Sibling = 40 ml STICK
(on-the-go, product 12). Cross-reference so buyers pick the right format.

Review insight used:
  praised   = "Pfoten weich & gepflegt" / "zieht schnell ein, macht Pfoten schnell weich"
  objection = one reviewer disliked the SCENT → do NOT over-promise scent;
              lead on care/protection, say "natürliche Rezeptur" (not "toller Duft")

Compliance (pet care): NO Heilversprechen — "pflegt rissige Ballen", NOT "heilt".
  Frame everything as Pflege & Schutz. No $/€ prices, no URL/.com, no
  #1/beste/garantiert, no "verhindert/behandelt/heilt".
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
PLAN_NO = "11"


# ===== KW-led, marketing-optimized DE copy (customer-facing) =====

# Title is HTML-escaped, so literal "&" counts as 1 char. Keep ≤200 real chars. Stays German.
TITLE = (
    "Jotti Pfotenbalsam Hund & Katze 100 ml — Pfotenpflege & Pfotenschutz bei Hitze, "
    "heißem Asphalt, Kälte & Streusalz · pflegt trockene, rissige Ballen · "
    "natürliche Rezeptur · Deutsche Manufaktur"
)

BULLETS = [
    "<b>SCHUTZ BEI HITZE & KÄLTE</b> — Ein Pfotenbalsam für jedes Wetter: schützt die "
    "Ballen im Sommer vor heißem Asphalt und im Winter vor Kälte, Schnee &amp; Streusalz. "
    "Pfotenschutz für Hunde bei Hitze wie bei Frost.",

    "<b>WEICHE, GEPFLEGTE BALLEN</b> — Pflegt trockene, raue und rissige Ballen wieder "
    "geschmeidig. Die Pfotenpflege für Hunde und Katzen macht raue Pfoten spürbar weich "
    "und gepflegt – Tag für Tag.",

    "<b>SCHÜTZENDER PFLEGEFILM</b> — Bildet einen dünnen, schützenden Pflegefilm auf den "
    "Ballen, der vor Asphalt, Streusalz und rauem Untergrund abschirmt und die Pfoten vor "
    "dem Austrocknen bewahrt.",

    "<b>ZIEHT SCHNELL EIN</b> — Der Balsam zieht schnell ein und macht die Pfoten rasch "
    "weich, ohne stark zu fetten. Natürliche Rezeptur mit Bienenwachs &amp; pflegenden "
    "Ölen – einfach in die Ballen einmassieren.",

    "<b>100 ML FÜR ZUHAUSE — DEUTSCHE MANUFAKTUR</b> — Der ergiebige 100-ml-Tiegel für "
    "die tägliche Pfotenpflege zuhause. Für unterwegs gibt es Jotti Pfotenbalsam als "
    "40-ml-Stift. Handwerklich gemacht in deutscher Manufaktur.",
]


IMAGES = [
    AIImagePlanItem(
        name="Bild 1 — Main Hero (3 Optionen für A/B-Test)",
        role="hero",
        background="Pure white #FFFFFF, Amazon main-image policy. Warm rim light so the amber balm tint reads. Identical setup across all 3 options for a clean split-test.",
        purpose="Win the click in the amazon.de dog-paw-care grid — read instantly as a caring paw balm, not a generic tin.",
        visual=(
            "Designer mocks up ALL 3 options. Brand picks the winner via Amazon Manage Your Experiments. "
            "Each option: ONE callout, ONE cue, ONE prop — clean, never stacked. Pure white BG, jar ~85% of frame, "
            "label fully legible.\n\n"
            "▸ OPTION A — HERO JAR + PAW (wins on category clarity)\n"
            "100 ml jar, lid off, three-quarter angle. Beside it a soft dog paw resting in frame. Subtle contact shadow.\n"
            "CALLOUT top right: badge 'HUND & KATZE' (brown #8B5A2B, white type).\n\n"
            "▸ OPTION B — DUAL-SEASON SPLIT (wins on the core benefit)\n"
            "Jar centered; behind it a soft diagonal split — warm summer asphalt on one side, icy salted winter path "
            "on the other. One balm protecting both.\n"
            "CALLOUT top left: 'HITZE & KÄLTE' (dark #2F2A26, white type).\n\n"
            "▸ OPTION C — BEFORE/AFTER PAW (wins on proof)\n"
            "Jar left; a paw-pad close-up split: left dry/rough/cracked, right soft/supple.\n"
            "CALLOUT bottom right: 'WEICHE BALLEN' (brown #8B5A2B).\n\n"
            "All 3: jar dominant ~85%, callout ~6%, same light, pure white BG, NO overlay sentence (policy)."
        ),
        overlay="(no overlay — Amazon main image)",
        overlay_sub="",
        props=[
            "OPTION A: 100 ml jar (lid off) + soft dog paw",
            "OPTION B: jar + dual-season split (hot asphalt / salted snow)",
            "OPTION C: jar + paw-pad before/after split",
        ],
        lighting="Bright even studio light with a warm rim from camera-right so the balm's amber tone and the jar label pop. Same light across all 3 options.",
        why_it_works=(
            "Three triggers against three motives: A nails category clarity (paw balm for dogs AND cats), B leads on "
            "the unique dual-season protection, C shows the before/after proof. One callout, one prop — readable on a "
            "mobile thumbnail in the DE paw-care grid."
        ),
        ctr="A caring paw plus a clear callout beats competitors' bare tins in the amazon.de grid; the dual-season and before/after angles are the strongest click promises for pfotenschutz hund sommer and winter.",
        cvr="Instant clarity on product type (paw balm), audience (Hund & Katze) and benefit (soft, protected pads) cuts bounce before the buyer even scrolls.",
    ),
    AIImagePlanItem(
        name="Bild 2 — Hook: Ein Balsam für jedes Wetter (Hitze & Kälte)",
        role="hook",
        background="Soft cream #EFE6D9 with a subtle diagonal split; warm side-light.",
        purpose="Land the core promise in one frame — one balm protects paws in summer heat AND winter salt.",
        visual=(
            "Split hero. LEFT: a dog walking on hot sunlit asphalt, heat-shimmer cue, warm tones. "
            "RIGHT: the same dog on an icy, salted winter path, cool tones, grit of Streusalz visible. "
            "Jar sits centered on the dividing line as the single solution bridging both worlds. "
            "Small caption strip under the jar: 'Sommer & Winter'."
        ),
        overlay="SCHUTZ BEI HITZE & KÄLTE.",
        overlay_sub="Ein Pfotenbalsam für heißen Asphalt im Sommer und Streusalz im Winter.",
        props=["dog on hot asphalt (left)", "dog on salted snow (right)", "100 ml jar on the divide", "heat-shimmer + grit cues"],
        lighting="Warm sunlit key on the summer side, cool blue fill on the winter side, jar lit neutral so it reads as the constant.",
        why_it_works=(
            "The dual-season use is the single strongest differentiator and matches the top DE search intents "
            "(pfotenschutz hund sommer AND hunde pfotenschutz hitze plus winter salt). One frame, one promise."
        ),
        ctr="The hot-vs-icy contrast is an instant pattern interrupt in the grid and covers both peak-season search waves at once.",
        cvr="Answers 'do I need a summer and a winter product?' with a single jar — raising perceived value and removing choice friction.",
    ),
    AIImagePlanItem(
        name="Bild 3 — Educate: Schützender Pflegefilm",
        role="educate",
        background="White with a brown accent band (#8B5A2B) in the footer.",
        purpose="Explain HOW it protects — a thin care film that shields the pads and locks in suppleness.",
        visual=(
            "Macro of a healthy paw pad with a subtle translucent film sheen. A simple cross-section callout shows "
            "3 layers: PAD → CARE FILM → shielded from asphalt heat / road salt / rough ground (thin brown line icons). "
            "Jar anchored right. Footer band carries the supporting line."
        ),
        overlay="GEGEN STREUSALZ & ASPHALT.",
        overlay_sub="Ein dünner Pflegefilm schirmt die Ballen ab und bewahrt sie vor dem Austrocknen.",
        props=["paw-pad macro with film sheen", "3-layer cross-section diagram", "line icons (heat/salt/rough ground)", "100 ml jar"],
        lighting="Flat, clean studio light — legibility over atmosphere so the film and diagram read on a thumbnail.",
        why_it_works=(
            "Makes the 'schützender Pflegefilm' USP concrete and visual. Buyers understand the mechanism, which "
            "separates Jotti from vague 'paw cream' listings and justifies the manufactory positioning."
        ),
        ctr="The visible protective-film mechanic signals a real, engineered benefit — stronger than a plain tin shot.",
        cvr="Explaining how the barrier works builds trust that the protection is real, not just a lotion.",
    ),
    AIImagePlanItem(
        name="Bild 4 — Desire: Before/After Ballen (rissig → weich)",
        role="desire",
        background="Warm cream #EFE6D9, aged wood, soft afternoon light.",
        purpose="Sell the visible result — dry, rough, cracked pads become soft and supple again.",
        visual=(
            "Large before/after split of a real paw pad. LEFT: dry, rough, fine cracks, dull. "
            "RIGHT: soft, supple, healthy sheen, well cared for. Divider centered; the 100 ml jar in the foreground "
            "corner with a fingertip-of-balm cue. Keep it honest and natural — no exaggerated gloss."
        ),
        overlay="WEICHE, GESUNDE BALLEN.",
        overlay_sub="Pflegt trockene, raue und rissige Ballen wieder geschmeidig und weich.",
        props=["paw pad before/after (split)", "100 ml jar (foreground)", "fingertip of balm cue", "aged wood surface"],
        lighting="Warm afternoon side-light from camera-right, gentle rim on the cared-for side so the healthy sheen shows.",
        why_it_works=(
            "Leans on the real review verbatim ('Pfoten weich & gepflegt'). Before/after is the strongest conversion "
            "signal in personal/pet care — it shows the outcome instead of claiming it. Care framing, no medical claim."
        ),
        ctr="The rough→soft pad transformation is universally desirable for any owner whose dog has dry or cracked pads.",
        cvr="Visual proof of the care result sets realistic expectations and drives the add-to-cart.",
    ),
    AIImagePlanItem(
        name="Bild 5 — Trust: Zieht schnell ein & natürliche Rezeptur",
        role="trust",
        background="White with cream panels.",
        purpose="Defuse friction (greasy/slow?) and reassure on the natural formula without over-promising scent.",
        visual=(
            "Left: a calm owner's hand massaging balm into a relaxed dog's paw, the dog settled — a moment of care. "
            "Right: a small 3-step icon row: 1. AUFTRAGEN (fingertip) · 2. EINMASSIEREN (circular-motion) · "
            "3. EINZIEHEN LASSEN (clock). Badge 'NATÜRLICHE REZEPTUR' with a honeycomb + oil-drop icon. "
            "Jar anchored right."
        ),
        overlay="ZIEHT SCHNELL EIN.",
        overlay_sub="Natürliche Rezeptur mit Bienenwachs & pflegenden Ölen – einmassieren, fertig.",
        props=["hand massaging dog paw", "3-step application icons", "badge 'NATÜRLICHE REZEPTUR' (honeycomb + oil drop)", "100 ml jar"],
        lighting="Clean even studio light — icons and badge readable on the thumbnail; warm tone on the care moment.",
        why_it_works=(
            "Echoes the positive verbatim ('zieht schnell ein, macht Pfoten schnell weich') and quietly answers the "
            "one scent objection by leading on 'natürliche Rezeptur' — care and formula, never an over-claimed fragrance."
        ),
        ctr="The fast-absorbing, no-fuss promise reassures buyers worried about greasy paws tracking through the house.",
        cvr="Pre-empts the effort and formula worries; the care moment builds the emotional trust that seals the purchase.",
    ),
    AIImagePlanItem(
        name="Bild 6 — Desire: Hund & Katze + Format (Tiegel vs. Stift)",
        role="desire",
        background="Cream #EFE6D9, aged wood.",
        purpose="Show breadth (dogs AND cats) and help buyers pick the right format — jar for home, stick for on-the-go.",
        visual=(
            "Two-up scene. LEFT: a dog's paw being cared for at home; RIGHT: a cat's paw — same balm, both audiences. "
            "Bottom strip = a simple format chooser: '100 ml TIEGEL — für zuhause, ergiebig' next to a small "
            "'40 ml STIFT — für unterwegs' silhouette, with a checkmark on the jar (this product). "
            "Brown line icons, calm and clear."
        ),
        overlay="FÜR HUND & KATZE.",
        overlay_sub="100-ml-Tiegel für zuhause – der 40-ml-Stift ist ideal für unterwegs.",
        props=["dog paw (left)", "cat paw (right)", "100 ml jar (checked)", "40 ml stick silhouette", "format-chooser strip"],
        lighting="Warm side-light, consistent across both tiles.",
        why_it_works=(
            "Widens the audience (Hund UND Katze = broader search relevance) and cross-sells the sibling format so the "
            "buyer self-selects the jar for home use instead of bouncing to compare — reduces wrong-format returns."
        ),
        ctr="Speaks to both dog and cat owners at once and answers the 'jar or stick?' question inside the grid.",
        cvr="Clear format guidance means the buyer picks the right size with confidence — fewer returns, higher satisfaction.",
    ),
    AIImagePlanItem(
        name="Bild 7 — Close: Deutsche Manufaktur",
        role="close",
        background="Workshop feel: aged wood, brass, linen, warm side-light.",
        purpose="Close on brand identity — honest, artisanal manufactory quality.",
        visual=(
            "Mid-range warm scene: hands (no face) finishing a jar of Jotti Pfotenbalsam on a wooden bench, "
            "surrounded by natural ingredient cues (honeycomb, small oil bottle). Jar label legible. "
            "A small handwritten note card carries the manufactory line. Lived-in, not staged."
        ),
        overlay="DEUTSCHE MANUFAKTUR.",
        overlay_sub="Handwerklich gemachte Pfotenpflege – mit natürlichen Pflegestoffen.",
        props=["hands finishing jar (no face)", "100 ml jar", "honeycomb + small oil bottle", "wooden bench / brass / linen", "handwritten note card"],
        lighting="Warm workshop side-light from camera-right, golden tone, lived-in — not staged.",
        why_it_works=(
            "Closes on the brand promise before checkout: honest, handmade manufactory quality with natural care "
            "ingredients. The hands-on-the-jar gesture is the visual metaphor for care and trust."
        ),
        ctr="The 'Deutsche Manufaktur' signal differentiates from anonymous import paw creams and attracts quality-conscious DE buyers.",
        cvr="Provenance and craft create the final trust that turns a hesitating buyer into a purchase.",
    ),
]


MODULES = [
    AIModule(
        name="Modul 1 — Brand-Banner",
        role="a+_banner",
        headline="PFOTENPFLEGE, DIE SCHÜTZT.",
        body=(
            "Jotti Pfotenbalsam pflegt trockene, raue und rissige Ballen wieder geschmeidig "
            "und legt einen schützenden Pflegefilm um die Pfoten – bei Hitze und heißem Asphalt "
            "genauso wie bei Kälte, Schnee und Streusalz. Natürliche Rezeptur, deutsche Manufaktur."
        ),
        visual="Wide cinematic scene: a dog on a warm path in golden side-light, the 100 ml jar front-center on aged wood. Logo top left in brown #8B5A2B.",
        alt="Jotti Pfotenbalsam 100 ml Tiegel auf Holz in warmem Licht, mit einem Hund im Hintergrund.",
    ),
    AIModule(
        name="Modul 2 — Carousel (4 Kacheln): Der Jotti-Vorteil",
        role="a+_carousel",
        headline="DER JOTTI-VORTEIL",
        body=(
            "Kachel 1: <b>HITZE &amp; KÄLTE</b> — ein Balsam für Sommer und Winter.<br/>"
            "Kachel 2: <b>WEICHE BALLEN</b> — pflegt trockene, raue &amp; rissige Ballen.<br/>"
            "Kachel 3: <b>PFLEGEFILM</b> — schirmt vor Asphalt, Streusalz &amp; rauem Grund ab.<br/>"
            "Kachel 4: <b>ZIEHT SCHNELL EIN</b> — natürliche Rezeptur, ohne stark zu fetten."
        ),
        visual="4 square tiles, brown accent corner per tile, small line icons (sun+snowflake · paw · shield-film · oil drop).",
        alt="Vier-Kachel A+ Carousel mit den Jotti-Vorteilen: Hitze & Kälte, weiche Ballen, Pflegefilm, zieht schnell ein.",
    ),
    AIModule(
        name="Modul 3 — Banner: Schutz bei jedem Wetter",
        role="a+_banner",
        headline="EIN BALSAM FÜR JEDES WETTER.",
        body=(
            "Im Sommer schützt der Pflegefilm die Ballen vor heißem Asphalt, im Winter vor Kälte, "
            "Schnee und Streusalz. So bleiben die Pfoten Ihres Hundes oder Ihrer Katze das ganze "
            "Jahr über weich, gepflegt und geschützt."
        ),
        visual="Wide banner split: left a dog on hot asphalt (heat shimmer), right the same dog on salted snow. Jar centered on the divide. Warm/cool palette.",
        alt="A+ Banner: ein Hund auf heißem Asphalt und auf verschneitem, gestreutem Weg – der Pfotenbalsam schützt in beiden Jahreszeiten.",
    ),
    AIModule(
        name="Modul 4 — Banner: Sichtbar gepflegte Ballen",
        role="a+_banner",
        headline="WEICHE, GESUNDE BALLEN.",
        body=(
            "Trockene, raue und rissige Ballen werden wieder geschmeidig und weich. Der Balsam zieht "
            "schnell ein und macht die Pfoten spürbar gepflegt – mit einer natürlichen Rezeptur aus "
            "Bienenwachs und pflegenden Ölen."
        ),
        visual="Triptych: LEFT dry/cracked pad (before), CENTER a caring hand massaging in the balm, RIGHT soft supple pad (after). Warm light throughout.",
        alt="A+ Triptychon: Ballen vorher trocken und rissig, Anwendung, nachher weich und geschmeidig.",
    ),
    AIModule(
        name="Modul 5 — Carousel (4 Kacheln): Für Hund, Katze & jeden Weg",
        role="a+_carousel",
        headline="FÜR HUND & KATZE",
        body=(
            "Kachel 1: <b>HUNDE</b> — Pfotenpflege &amp; Pfotenschutz bei jedem Wetter.<br/>"
            "Kachel 2: <b>KATZEN</b> — pflegt raue Ballen sanft und weich.<br/>"
            "Kachel 3: <b>SOMMER</b> — Schutz vor heißem Asphalt.<br/>"
            "Kachel 4: <b>WINTER</b> — Schutz vor Kälte, Schnee &amp; Streusalz."
        ),
        visual="4 identically composed tiles, real paw scenes, brown accent corner per tile, consistent warm light.",
        alt="Vier-Kachel A+ Carousel: Anwendung bei Hunden, Katzen, im Sommer und im Winter.",
    ),
    AIModule(
        name="Modul 6 — Premium Q&A",
        role="a+_qa",
        headline="HÄUFIGE FRAGEN",
        body=(
            "<b>F.</b> Ist der Balsam für Hunde und Katzen geeignet?<br/>"
            "<b>A.</b> Ja. Jotti Pfotenbalsam pflegt die Ballen von Hunden und Katzen und lässt sich "
            "einfach in die Pfoten einmassieren.<br/><br/>"
            "<b>F.</b> Hilft er im Sommer und im Winter?<br/>"
            "<b>A.</b> Ja. Der schützende Pflegefilm schirmt die Ballen im Sommer vor heißem Asphalt "
            "und im Winter vor Kälte, Schnee und Streusalz ab.<br/><br/>"
            "<b>F.</b> Zieht der Balsam schnell ein?<br/>"
            "<b>A.</b> Ja. Der Balsam zieht schnell ein und macht die Pfoten rasch weich, ohne stark "
            "zu fetten.<br/><br/>"
            "<b>F.</b> Was ist drin?<br/>"
            "<b>A.</b> Eine natürliche Rezeptur mit Bienenwachs und pflegenden Ölen, die trockene, raue "
            "und rissige Ballen geschmeidig pflegt.<br/><br/>"
            "<b>F.</b> Tiegel oder Stift – was passt zu mir?<br/>"
            "<b>A.</b> Der 100-ml-Tiegel ist ergiebig für die tägliche Pflege zuhause. Für unterwegs gibt "
            "es Jotti Pfotenbalsam als handlichen 40-ml-Stift."
        ),
        visual="Vertical Q/A table, brown dividers between questions, small F./A. labels in dark #2F2A26.",
        alt="Premium Q&A Modul mit den häufigsten Fragen zu Jotti Pfotenbalsam.",
    ),
    AIModule(
        name="Modul 7 — Premium Comparison Chart",
        role="a+_comparison",
        headline="WARUM JOTTI",
        body=(
            "Vergleich über 4 Spalten: <b>Jotti Pfotenbalsam 100 ml</b> · Einfache Pfotencreme · "
            "Vaseline / Melkfett · Hundeschuhe.<br/><br/>"
            "Zeilen: Schutz bei Hitze &amp; heißem Asphalt · Schutz bei Kälte &amp; Streusalz · "
            "schützender Pflegefilm · zieht schnell ein · natürliche Rezeptur · für Hund &amp; Katze · "
            "Deutsche Manufaktur.<br/><br/>"
            "Jotti-Spalte mit dezentem Braun-Ton hervorheben."
        ),
        visual="Standard Amazon Premium Comparison Chart, 4 columns. Alternatives named by category only, no brand names. Brown header row.",
        alt="Premium Vergleichstabelle: Jotti Pfotenbalsam vs. einfache Pfotencreme, Vaseline/Melkfett und Hundeschuhe.",
    ),
]


QA = [
    AIQA(q="Ist der Pfotenbalsam für Hunde und Katzen geeignet?",
         a="Ja. Jotti Pfotenbalsam pflegt die Ballen von Hunden und Katzen. Er lässt sich einfach in die Pfoten einmassieren und zieht schnell ein."),
    AIQA(q="Schützt der Balsam im Sommer bei Hitze und heißem Asphalt?",
         a="Ja. Der schützende Pflegefilm schirmt die Ballen vor heißem Asphalt und rauem, sonnenwarmem Untergrund ab – ideal für die Gassirunde an heißen Tagen."),
    AIQA(q="Und im Winter bei Kälte, Schnee und Streusalz?",
         a="Ja. Derselbe Pflegefilm schützt die Ballen auch im Winter vor Kälte, Schnee und Streusalz und pflegt raue, strapazierte Pfoten wieder geschmeidig."),
    AIQA(q="Pflegt er trockene und rissige Ballen?",
         a="Ja. Die natürlichen Pflegestoffe versorgen trockene, raue und rissige Ballen und machen sie wieder weich und geschmeidig. Bei stark beanspruchten Pfoten den Balsam mehrmals täglich auftragen."),
    AIQA(q="Zieht der Balsam schnell ein oder fettet er stark?",
         a="Der Balsam zieht schnell ein und macht die Pfoten rasch weich, ohne stark zu fetten. Dünn auftragen und in die Ballen einmassieren – so bleibt kein Fettfilm auf dem Boden."),
    AIQA(q="Was ist in der Rezeptur enthalten?",
         a="Eine natürliche Rezeptur mit Bienenwachs und pflegenden Ölen. Wir setzen auf die Pflege- und Schutzwirkung, nicht auf einen aufdringlichen Duft."),
    AIQA(q="Wie oft und wie wird der Balsam angewendet?",
         a="Pfoten grob säubern, eine kleine Menge Balsam auf die Ballen geben und sanft einmassieren. Nach Bedarf wiederholen, zum Beispiel vor und nach dem Spaziergang."),
    AIQA(q="Tiegel oder Stift – welches Format passt zu mir?",
         a="Der ergiebige 100-ml-Tiegel eignet sich für die tägliche Pfotenpflege zuhause. Für unterwegs gibt es Jotti Pfotenbalsam als handlichen 40-ml-Stift – so haben Sie den Schutz immer dabei."),
    AIQA(q="Wo wird Jotti hergestellt?",
         a="In deutscher Manufakturqualität. Jotti steht für handwerklich gemachte, ehrliche Pflege."),
]


# Backend KWs — German, stem-deduped, byte-packed. Avoid brand/title duplicates & superlatives.
BACKEND = (
    "hundepfoten pfoetchen ballenpflege pfotencreme pfotensalbe hundepfote paw wax "
    "hitzeschutz pfoten sommer strassenhitze hundeschuhe pfotenschuhe winter frost "
    "schneeschutz melkfett vaseline ersatz bienenwachs pflegeoel trockene ballen "
    "rissige pfoten gassi spaziergang welpen senior katzenpfoten samtpfoten "
    "manufaktur tiegel ergiebig pfoetchenschutz tierpflege"
)


def main() -> None:
    print("Loading Jotti customer + parsing Pfotenbalsam Excel…")
    cust = load_customer("jotti")
    brief = parse_excel(EXCEL)
    OUT = HERE / f"{PLAN_NO}_Jotti_Pfotenbalsam_Image Plan.pdf"
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
