"""Jotti Pfotenbalsam STIFT 40 ml (Stick) — Image Plan 12
Hand-written senior copy injected into the branded ReportLab pipeline.

Marketplace: amazon.de.

LANGUAGE SPLIT (the standard):
  • ENGLISH — art-direction / strategy fields the designer reads:
    image purpose, background, visual, props, lighting, why_it_works, ctr, cvr,
    and module visual.
  • GERMAN — marketplace, customer-facing text the shopper reads:
    TITLE, BULLETS, image overlay, overlay_sub, module headline, module body,
    QA, and BACKEND keywords.

THE FORMAT IS THE HERO ANGLE:
  Same balm as the 100 ml JAR (product 11), but in a STICK. The stick = clean,
  hands-free application (keine schmierigen Finger), handlich, passt in jede
  (Gassi-)Tasche, unterwegs auftragen. Sibling = 100 ml Glas for home use.

Verified facts / VoC (from listing.xlsx):
  - Pfotenpflege für Hunde & Katzen; pflegt trockene, raue & rissige Ballen
  - Schutz bei Hitze & heißem Asphalt (Sommer) UND Kälte, Schnee & Streusalz (Winter)
  - bildet einen schützenden Pflegefilm; kompakte Stick-Form für unterwegs
  - praised: "Stick ist handlich und ideal für unterwegs", "zieht schnell ein,
    macht Pfoten schnell weich"
  - objection: stick wird bei sehr kalter Temperatur fester → defuse: "kurz in
    der Hand anwärmen"; one reviewer disliked the SCENT → do NOT over-promise
    scent, focus on care/protection + "natürliche Rezeptur"

Compliance (pet care): NO Heilversprechen — "pflegt rissige Ballen" NOT "heilt".
No $/€ prices, no URL/.com, no #1/beste/garantiert. Overlays: smooth outcome-led
German, ≤30 chars & ≤5 words. Art direction English; customer text German.
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
PLAN_NO = "12"


# ===== KW-led, marketing-optimized DE copy (customer-facing) =====

# Title is HTML-escaped, so literal "&" counts as 1 char. Keep ≤200 real chars. German.
TITLE = (
    "Jotti Pfotenbalsam Stift 40 ml — Pfotenpflege für Hunde & Katzen · Pfotenschutz "
    "bei Hitze & heißem Asphalt, Kälte, Schnee & Streusalz · pflegt trockene, rissige "
    "Ballen · für unterwegs · Manufaktur"
)

BULLETS = [
    "<b>PFOTENSCHUTZ FÜR UNTERWEGS</b> — Der handliche Stift schützt die Pfoten Ihres "
    "Hundes oder Ihrer Katze direkt auf dem Spaziergang: einfach aufdrehen, auftragen, "
    "weiter geht&#39;s. Passt in jede Gassi- &amp; Jackentasche.",

    "<b>AUFTRAGEN OHNE SCHMIERFINGER</b> — Die Stick-Form gleitet sauber direkt auf die "
    "Ballen – kein Eincremen mit den Fingern, kein Fett an den Händen. Ideal, wenn der "
    "Hund unruhig ist oder es unterwegs schnell gehen muss.",

    "<b>SCHUTZ BEI HITZE &amp; KÄLTE</b> — Ein schützender Pflegefilm für das ganze Jahr: "
    "schützt die Ballen im Sommer bei heißem Asphalt und Hitze und im Winter bei Kälte, "
    "Schnee und Streusalz.",

    "<b>ZIEHT SCHNELL EIN &amp; PFLEGT TIEF</b> — Die natürliche Rezeptur zieht schnell "
    "ein und macht trockene, raue und rissige Ballen wieder weich und geschmeidig – ohne "
    "langes Warten, bevor es weitergeht.",

    "<b>HANDLICH &amp; DEUTSCHE MANUFAKTUR</b> — Kompaktes Stift-Format für unterwegs, das "
    "große Glas (100 ml) für die Pflege zuhause. Pfotenpflege für Hunde &amp; Katzen aus "
    "deutscher Manufaktur.",
]


IMAGES = [
    AIImagePlanItem(
        name="Bild 1 — Main Hero (3 Optionen für A/B-Test)",
        role="hero",
        background="Warm cream backdrop (#EFE6D9) with soft side-light; a hint of aged wood in the bottom 15% band for the manufactory feel. Identical backdrop across all 3 options for a clean split-test.",
        purpose="Win the click in the amazon.de paw-care grid — stand out next to generic tins and tubes by leading with the STICK format.",
        visual=(
            "Designer mocks up ALL 3 options. Brand picks the winner via Amazon Manage Your Experiments. "
            "Each option: ONE callout, ONE action cue, ONE prop — clean, never stacked.\n\n"
            "▸ OPTION A — STICK-ON-PAW (wins on the hands-free format)\n"
            "The open Jotti stick (cap off, balm nub visible) glides directly onto a dog's paw pad outdoors; "
            "hand only (no face), clean fingers, no mess. Stick label legible, ~55% of frame.\n"
            "CALLOUT top right: badge 'OHNE SCHMIERFINGER' (brown #8B5A2B, white type).\n\n"
            "▸ OPTION B — STICK + JAR SYSTEM (wins on the range logic)\n"
            "Jotti stick standing upright front-left (cap off), the 100 ml jar soft-focused behind right. "
            "Thin brown labels: 'STIFT — UNTERWEGS' · 'GLAS — ZUHAUSE'.\n"
            "CALLOUT top left: 'FÜR UNTERWEGS & ZUHAUSE' (dark #2F2A26, white type).\n\n"
            "▸ OPTION C — POCKET / ON-THE-GO (wins on convenience)\n"
            "Stick tucked into a jacket / treat-bag pocket beside a leash, showing how small it is. Bright, "
            "clean, outdoor light.\n"
            "CALLOUT bottom right: 'PASST IN JEDE TASCHE' (brown #8B5A2B).\n\n"
            "All 3: stick dominant ~55–60%, callout ~6%, same light / same backdrop."
        ),
        overlay="(eine Callout je Option — siehe Bildregie)",
        overlay_sub="3 Hero-Optionen geliefert — A/B testen, Sieger behalten.",
        props=[
            "OPTION A: open stick + dog paw + clean hand (no face) + outdoor cue + badge",
            "OPTION B: stick (front) + 100 ml jar (soft focus) + range labels",
            "OPTION C: stick in jacket/treat-bag pocket + leash + outdoor light",
        ],
        lighting="Warm side-light from camera-right (3000–3500K), gentle rim on the stick so the label pops. Same light across all 3 options.",
        why_it_works=(
            "Three triggers against three motives: A owns the hands-free STICK format (the differentiator "
            "vs. tins you dig into with your fingers), B frames the stick-plus-jar range, C proves pocket "
            "portability. One callout, one action cue, one prop — readable on a mobile thumbnail."
        ),
        ctr="The stick-on-paw shot plus 'OHNE SCHMIERFINGER' is a pattern-interrupt next to competitors' generic paw-balm tins; the format is the click promise for 'pfotenbalsam hund' and 'pfotenschutz hund sommer'.",
        cvr="Instant clarity on format (stick), user (Hund & Katze) and payoff (clean, hands-free paw protection) cuts bounce; the manufactory cue builds trust.",
    ),
    AIImagePlanItem(
        name="Bild 2 — Hook: Der Stift-Vorteil (ohne Schmierfinger)",
        role="hook",
        background="Cream #EFE6D9, hint of aged wood, warm side-light.",
        purpose="Establish the unique stick advantage instantly — clean, hands-free application vs. greasy fingers from a tin.",
        visual=(
            "Split frame. LEFT: an open balm tin + a greasy fingertip digging in, faint 'schmierig' cue, dog "
            "pulling away. RIGHT: the Jotti stick gliding cleanly straight onto the paw pad, clean hand (no "
            "face), calm dog. Large brown #8B5A2B arrow / divider. Small caption strip at the bottom: "
            "'aufdrehen · auftragen · fertig'."
        ),
        overlay="AUFTRAGEN OHNE SCHMIERFINGER.",
        overlay_sub="Der Stift gleitet direkt auf die Pfote – ganz ohne fettige Finger.",
        props=["open balm tin + greasy finger (left)", "Jotti stick gliding on paw (right)", "dog paw", "arrow / divider"],
        lighting="Even warm front-side light, soft shadow under the props.",
        why_it_works=(
            "A direct category counter: paw balms usually come in tins you scoop with your fingers. The "
            "clean stick application is the most tangible differentiator and answers 'why this product?' "
            "in one frame — straight from the review verbatim 'handlich und ideal für unterwegs'."
        ),
        ctr="The messy-tin-vs-clean-stick contrast hits the convenience nerve of the DE dog owner who wants quick paw care on the walk.",
        cvr="Removes the 'greasy fingers / fussy application' worry and positions the stick clearly as the easier, cleaner choice.",
    ),
    AIImagePlanItem(
        name="Bild 3 — Educate: Schützender Pflegefilm, natürliche Rezeptur",
        role="educate",
        background="White with a brown accent band (#8B5A2B) in the footer.",
        purpose="Explain how the balm works — a protective care film from a natural formula — and defend the premium positioning.",
        visual=(
            "Headline at top, then a clean cross-section illustration of a paw pad with a thin translucent "
            "'Pflegefilm' layer highlighted on the surface. Beside it 3 benefit tiles with line icons:\n"
            "  • NATÜRLICHE ÖLE & WACHSE — pflegen tief\n"
            "  • SCHÜTZENDER FILM — auf rauen Ballen\n"
            "  • ZIEHT SCHNELL EIN — weich & geschmeidig\n"
            "Stick standing upright right. Footer band (brown) carries the supporting line."
        ),
        overlay="SCHÜTZENDER PFLEGEFILM.",
        overlay_sub="Natürliche Öle & Wachse legen einen schützenden Film auf raue Ballen.",
        props=["paw-pad cross-section with film layer", "3 benefit tiles with icons", "Jotti stick", "footer band"],
        lighting="Flat, clean studio light — legibility over atmosphere.",
        why_it_works=(
            "Makes the mechanism concrete: buyers see the protective film on the pad instead of a vague "
            "promise. The natural-formula framing (without over-claiming scent) justifies the manufactory "
            "price and stays compliant — care, not cure."
        ),
        ctr="'Natürliche Rezeptur' and 'Pflegefilm' are strong DE trust signals for paw care; the cross-section reads as real substance at a glance.",
        cvr="A transparent, natural formula builds trust and separates Jotti from generic paw waxes — and it sidesteps the scent objection by leading with care and protection.",
    ),
    AIImagePlanItem(
        name="Bild 4 — Desire: Schutz durch alle Jahreszeiten",
        role="desire",
        background="Split seasonal scene — warm summer asphalt vs. cold winter snow. Consistent warm key light.",
        purpose="Sell the year-round protection promise — the two moments the buyer worries about most.",
        visual=(
            "Large seasonal split. LEFT (SOMMER): a dog walking on sun-baked asphalt / pavement, faint heat "
            "shimmer, small sun icon. RIGHT (WINTER): the same dog on snow with grit / road salt, small "
            "snowflake icon. Stick anchored in the foreground center (label legible), a small paw print on "
            "each side. Divider centered."
        ),
        overlay="SCHUTZ BEI HITZE & KÄLTE.",
        overlay_sub="Schützt die Ballen bei heißem Asphalt im Sommer und Streusalz im Winter.",
        props=["dog on hot asphalt (summer)", "dog on snow / road salt (winter)", "Jotti stick (foreground)", "sun & snowflake icons", "paw prints"],
        lighting="Warm key light kept consistent across both seasons so the split reads as one product, two jobs.",
        why_it_works=(
            "Doubles the buying occasions: the same stick answers the summer 'hot asphalt burns paws' fear "
            "AND the winter 'salt and snow crack paws' fear. Matches high-intent KWs 'pfotenschutz hund "
            "sommer', 'hunde pfotenschutz hitze' and the winter Streusalz search."
        ),
        ctr="Hot-asphalt-and-winter-salt is the single most-searched paw worry in DE; showing both seasons in one frame maximizes grid relevance year-round.",
        cvr="Two seasons = two reasons to buy now instead of later; the buyer sees their exact walk in the frame.",
    ),
    AIImagePlanItem(
        name="Bild 5 — Trust: VoC-Beweis + Einwand entkräften (Kälte)",
        role="trust",
        background="White with cream panels.",
        purpose="Prove the 'zieht schnell ein, macht Pfoten weich' review and defuse the one objection (stick firms up in hard cold).",
        visual=(
            "LEFT: a before/after of a single paw pad — 'RAU & TROCKEN' vs. 'WEICH & GEPFLEGT' with a small "
            "clock icon and a caption 'zieht schnell ein'. RIGHT: a simple 3-step icon row:\n"
            "  1. AUFDREHEN (twist-up icon)\n"
            "  2. AUFTRAGEN (stick-on-paw icon)\n"
            "  3. BEI KÄLTE KURZ ANWÄRMEN (hand-warming icon)\n"
            "Small badge 'NATÜRLICHE REZEPTUR'. Stick as an anchor bottom-right."
        ),
        overlay="ZIEHT SCHNELL EIN.",
        overlay_sub="Macht raue Ballen schnell weich. Bei Kälte kurz in der Hand anwärmen.",
        props=["before/after paw pad (rau → weich)", "3 application icons", "badge 'NATÜRLICHE REZEPTUR'", "Jotti stick"],
        lighting="Clean even studio light — icons and before/after readable on the thumbnail.",
        why_it_works=(
            "Turns the strongest positive verbatim ('zieht schnell ein, macht Pfoten schnell weich') into "
            "on-image proof, and pre-empts the single recurring negative ('stick wird bei Kälte fester') "
            "with the honest fix — warm it briefly in your hand. Pre-defused objections lower returns and "
            "1-star ratings."
        ),
        ctr="The rau→weich before/after is the proof careful DE buyers scan for; the honest cold-weather tip signals a trustworthy seller.",
        cvr="Defuses the top review objection right on the image — the shopper reading reviews sees the solution, not just the problem, before buying.",
    ),
    AIImagePlanItem(
        name="Bild 6 — Desire: Passt in jede Tasche (unterwegs)",
        role="desire",
        background="Cream #EFE6D9, outdoor-walk cue, warm side-light.",
        purpose="Show the portability payoff — always with you on the walk, the moment the paw needs it.",
        visual=(
            "Lifestyle: the small Jotti stick shown next to everyday carry — a leash, a treat pouch, a "
            "jacket pocket — with the stick clearly tiny (compare-to-lip-balm scale). A hand slips it into "
            "the treat bag (no face). Soft-focused park path in the background. Small label 'immer dabei'."
        ),
        overlay="PASST IN JEDE TASCHE.",
        overlay_sub="So klein wie ein Lippenpflegestift – passt in jede Gassi- oder Jackentasche.",
        props=["Jotti stick (small-scale reference)", "leash", "treat pouch / jacket pocket", "hand (no face)", "soft-focused park path"],
        lighting="Warm natural outdoor side-light, lived-in and real — not studio-staged.",
        why_it_works=(
            "Expands perceived value by owning the on-the-go moment: the stick is small enough to always "
            "be in the bag, so protection happens exactly when the paw meets hot asphalt or salt. Hits the "
            "'unterwegs' verbatim and the pocketable format that the 100 ml jar can't."
        ),
        ctr="Portability speaks to the walking dog owner's exact scenario and separates the stick from bulky tins and jars in the grid.",
        cvr="'Always in my bag' lowers the mental barrier — the buyer pictures using it daily, which raises perceived value per stick.",
    ),
    AIImagePlanItem(
        name="Bild 7 — Close: Deutsche Manufaktur (Stift & Glas)",
        role="close",
        background="Workshop-adjacent scene: aged wood, warm side-light, clean and calm.",
        purpose="Close on brand identity and the range — artisanal manufactory quality, stick for on-the-go, jar for home.",
        visual=(
            "Mid-range scene on a wooden surface: the Jotti stick front-center (label legible) with the "
            "100 ml jar beside it, a happy dog soft-focused in the background. Small labels: 'STIFT — "
            "UNTERWEGS' and 'GLAS — ZUHAUSE'. A small handwritten note card carries the manufactory line. "
            "Warm, honest, lived-in styling."
        ),
        overlay="DEUTSCHE MANUFAKTUR.",
        overlay_sub="Stift für unterwegs, Glas für zuhause – deutsche Manufakturqualität.",
        props=["Jotti stick (front)", "100 ml jar", "dog (soft focus)", "wooden surface", "handwritten note card", "range labels"],
        lighting="Warm side-light from camera-right, golden tone, lived-in — not staged.",
        why_it_works=(
            "Closes on the brand promise that matters before checkout — honest, artisanal manufactory "
            "quality — and cross-sells the 100 ml jar for home use, lifting basket size while positioning "
            "the stick as the on-the-go companion."
        ),
        ctr="The 'deutsche Manufaktur' signal differentiates from anonymous import paw waxes and attracts quality-conscious DE pet owners.",
        cvr="Provenance plus the stick-and-jar range creates the final trust and an easy cross-sell that seals the purchase.",
    ),
]


MODULES = [
    AIModule(
        name="Modul 1 — Brand-Banner",
        role="a+_banner",
        headline="PFOTENSCHUTZ FÜR UNTERWEGS.",
        body=(
            "Jotti Pfotenbalsam als handlicher Stift: sauber und ohne Schmierfinger direkt auf die "
            "Pfote – für Hunde und Katzen. Pflegt trockene, raue und rissige Ballen und legt einen "
            "schützenden Pflegefilm bei Hitze und Kälte. Natürliche Rezeptur, deutsche Manufaktur."
        ),
        visual="Wide cinematic outdoor scene: a park path in warm side-light, Jotti stick front-center (cap off), a dog soft-focused mid-walk. Logo top left in brown #8B5A2B.",
        alt="Jotti Pfotenbalsam Stift im Vordergrund auf einem Spazierweg in warmem Licht, mit einem Hund im weichen Hintergrund.",
    ),
    AIModule(
        name="Modul 2 — Carousel (4 Kacheln): Der Jotti-Vorteil",
        role="a+_carousel",
        headline="DER JOTTI-VORTEIL",
        body=(
            "Kachel 1: <b>OHNE SCHMIERFINGER</b> — Stick-Form, sauber direkt auf die Pfote.<br/>"
            "Kachel 2: <b>FÜR UNTERWEGS</b> — handlich, passt in jede Gassi- &amp; Jackentasche.<br/>"
            "Kachel 3: <b>HITZE &amp; KÄLTE</b> — schützt bei heißem Asphalt, Schnee &amp; Streusalz.<br/>"
            "Kachel 4: <b>NATÜRLICHE REZEPTUR</b> — pflegt raue, rissige Ballen, zieht schnell ein."
        ),
        visual="4 square tiles, brown accent corner per tile, small line icons (stick head · pocket · sun+snowflake · droplet).",
        alt="Vier-Kachel A+ Carousel mit den Jotti-Vorteilen: ohne Schmierfinger, für unterwegs, Hitze & Kälte, natürliche Rezeptur.",
    ),
    AIModule(
        name="Modul 3 — Banner: Der Stift-Vorteil",
        role="a+_banner",
        headline="AUFTRAGEN OHNE SCHMIERFINGER.",
        body=(
            "Aufdrehen, direkt auf die Ballen auftragen, fertig – der Stift gleitet sauber auf die "
            "Pfote, ohne fettige Finger und ohne Eincremen aus der Dose. Ideal, wenn der Hund "
            "unruhig ist oder es unterwegs schnell gehen muss."
        ),
        visual="Wide banner: split — messy tin with a greasy finger (left) vs. clean Jotti stick gliding on a paw (right). Brown #8B5A2B divider. Warm side-light.",
        alt="A+ Banner: Vergleich zwischen fettiger Dosen-Anwendung und dem sauberen Jotti Stift direkt auf der Pfote.",
    ),
    AIModule(
        name="Modul 4 — Banner: Schutz durch alle Jahreszeiten",
        role="a+_banner",
        headline="SCHUTZ BEI HITZE & KÄLTE.",
        body=(
            "Ein Pflegefilm für das ganze Jahr: schützt die Ballen im Sommer bei heißem Asphalt und "
            "Hitze und im Winter bei Kälte, Schnee und Streusalz. Trockene, raue Ballen werden wieder "
            "weich und geschmeidig – und ziehen schnell ein."
        ),
        visual="Triptych: LEFT summer dog on hot asphalt (sun icon), CENTER stick applied to a paw, RIGHT winter dog on snow/road salt (snowflake icon). Consistent warm light.",
        alt="A+ Triptychon-Banner: Pfotenschutz im Sommer bei Hitze, Anwendung des Stifts, Schutz im Winter bei Schnee und Streusalz.",
    ),
    AIModule(
        name="Modul 5 — Carousel (2 Kacheln): Stift & Glas",
        role="a+_carousel",
        headline="STIFT & GLAS IM ÜBERBLICK",
        body=(
            "Kachel 1: <b>PFOTENBALSAM STIFT 40 ML (dieses Produkt)</b> — handlich für unterwegs, "
            "sauber ohne Schmierfinger, passt in jede Gassi-Tasche.<br/>"
            "Kachel 2: <b>PFOTENBALSAM GLAS 100 ML</b> — dieselbe Pflege im großen Format für die "
            "regelmäßige Pfotenpflege zuhause.<br/>"
            "<i>Beide für Hunde &amp; Katzen – Stift für unterwegs, Glas für zuhause.</i>"
        ),
        visual="2 identically composed product tiles, brown accent corner per tile: stick (left), 100 ml jar (right). Consistent warm light, real paw-care styling.",
        alt="Zwei-Kachel A+ Carousel: Jotti Pfotenbalsam Stift 40 ml für unterwegs und Glas 100 ml für zuhause.",
    ),
    AIModule(
        name="Modul 6 — Premium Q&A",
        role="a+_qa",
        headline="HÄUFIGE FRAGEN",
        body=(
            "<b>F.</b> Für welche Tiere ist der Stift geeignet?<br/>"
            "<b>A.</b> Für Hunde und Katzen. Er pflegt trockene, raue und rissige Ballen und legt einen "
            "schützenden Pflegefilm.<br/><br/>"
            "<b>F.</b> Was ist der Vorteil der Stick-Form?<br/>"
            "<b>A.</b> Man trägt den Balsam sauber und direkt auf die Pfote auf – ohne schmierige Finger. "
            "Der Stift ist handlich und passt in jede Gassi- oder Jackentasche.<br/><br/>"
            "<b>F.</b> Schützt er bei Hitze und Kälte?<br/>"
            "<b>A.</b> Ja. Der Pflegefilm schützt die Ballen im Sommer bei heißem Asphalt und im Winter "
            "bei Kälte, Schnee und Streusalz.<br/><br/>"
            "<b>F.</b> Der Stift ist bei Kälte fester geworden – was tun?<br/>"
            "<b>A.</b> Das ist normal bei sehr niedrigen Temperaturen. Den Stift kurz in der Hand anwärmen, "
            "dann gleitet er wieder leicht auf.<br/><br/>"
            "<b>F.</b> Was ist der Unterschied zum 100-ml-Glas?<br/>"
            "<b>A.</b> Dieselbe Pflege in zwei Formaten: der Stift für unterwegs, das Glas für die "
            "regelmäßige Pflege zuhause."
        ),
        visual="Vertical Q/A table, brown dividers between questions, small F./A. labels in dark #2F2A26.",
        alt="Premium Q&A Modul mit den häufigsten Fragen zum Jotti Pfotenbalsam Stift.",
    ),
    AIModule(
        name="Modul 7 — Premium Comparison Chart",
        role="a+_comparison",
        headline="WARUM JOTTI",
        body=(
            "Vergleich über 4 Spalten: <b>Jotti Pfotenbalsam Stift</b> · Pfotenbalsam in der Dose · "
            "Pfotenwachs (Standard) · Pfotenschuhe.<br/><br/>"
            "Zeilen: Auftragen ohne Schmierfinger · Handlich für unterwegs · Schutz bei Hitze &amp; heißem "
            "Asphalt · Schutz bei Kälte, Schnee &amp; Streusalz · Natürliche Rezeptur · Für Hunde &amp; "
            "Katzen · Deutsche Manufaktur.<br/><br/>"
            "Jotti-Spalte mit dezentem Braun-Ton hervorheben."
        ),
        visual="Standard Amazon Premium Comparison Chart, 4 product columns. Competitors named by category only, no brand names. Brown header row.",
        alt="Premium Vergleichstabelle: Jotti Pfotenbalsam Stift vs. Balsam in der Dose, Standard-Pfotenwachs und Pfotenschuhe.",
    ),
]


QA = [
    AIQA(q="Für welche Tiere ist der Pfotenbalsam Stift geeignet?",
         a="Für Hunde und Katzen. Der Stift pflegt trockene, raue und rissige Ballen und legt einen schützenden Pflegefilm auf die Pfoten."),
    AIQA(q="Was ist der Vorteil der Stick-Form gegenüber der Dose?",
         a="Man trägt den Balsam sauber und direkt auf die Pfote auf, ohne schmierige Finger und ohne Eincremen aus der Dose. Der Stift ist handlich und passt in jede Gassi- oder Jackentasche – ideal für unterwegs."),
    AIQA(q="Schützt der Balsam bei Hitze und heißem Asphalt?",
         a="Ja. Der Pflegefilm schützt die Ballen im Sommer bei Hitze und heißem Asphalt. Vor dem Spaziergang auf die Pfoten auftragen."),
    AIQA(q="Schützt er auch im Winter bei Schnee und Streusalz?",
         a="Ja. Im Winter schützt der Pflegefilm die Ballen bei Kälte, Schnee und Streusalz und hält trockene, raue Ballen weich und geschmeidig."),
    AIQA(q="Zieht der Balsam schnell ein?",
         a="Ja. Die natürliche Rezeptur zieht schnell ein und macht raue Ballen zügig weich – so geht es ohne langes Warten weiter."),
    AIQA(q="Der Stift ist bei Kälte fester geworden – was kann ich tun?",
         a="Das ist bei sehr niedrigen Temperaturen normal. Den Stift einfach kurz in der Hand anwärmen, dann lässt er sich wieder leicht auftragen."),
    AIQA(q="Was ist der Unterschied zum 100-ml-Glas?",
         a="Es ist dieselbe Pflege in zwei Formaten: der Stift für unterwegs, das große Glas (100 ml) für die regelmäßige Pfotenpflege zuhause."),
]


# Backend KWs — German, stem-deduped, byte-packed. Avoid brand/title duplicates & superlatives.
BACKEND = (
    "hunde pfotenpflege pfotenbalsam katze hundepfoten balsam paw wax pfotencreme pfotenwachs "
    "hitzeschutz pfoten asphalt sommer winter schnee streusalz kaelte ballenpflege rissige "
    "pfoten trockene raue ballen bienenwachs natuerlich pflegestick unterwegs gassi wandern "
    "hundezubehoer katzenpflege pflegefilm geschmeidig weich"
)


def main() -> None:
    print("Loading Jotti customer + parsing Pfotenbalsam Stift Excel…")
    cust = load_customer("jotti")
    brief = parse_excel(EXCEL)
    OUT = HERE / f"{PLAN_NO}_Jotti_Pfotenbalsam_Stift_Image Plan.pdf"
    real_title_len = len(TITLE.replace("&amp;", "&").replace("&#39;", "'"))
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
