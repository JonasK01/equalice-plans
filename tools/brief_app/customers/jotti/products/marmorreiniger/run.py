"""Jotti Marmor Reiniger 500 ml — Image Plan 13. FIRST PLAN BUILT IN THE NEW FORMAT.

Marketplace: amazon.de — GERMAN overlays + customer copy, ENGLISH art direction.

WHAT IS NEW HERE (this is the point of this plan):
Every image now declares a LAYOUT archetype and the GRAPHICS the designer must build, so a
tile is a designed composition instead of a headline on a photo. Across the seven: no two
layouts repeat, four of the four archetype families appear (before/after, icon-driven,
callout-driven, numbered-steps), and only two tiles are photography-only. Overlays contain
NO dashes and vary in construction.

LANGUAGE SPLIT (house standard):
  • GERMAN  — TITLE, BULLETS, overlay, overlay_sub, module headline + body, Q&A, backend.
  • ENGLISH — purpose, background, visual, props, lighting, why_it_works, ctr, cvr, graphics.

VERIFIED FACTS (from the SEO sheet only):
  - 500 ml Marmor- und Natursteinreiniger, für Innenbereich
  - mit natürlichem CARNAUBAWACHS; pflegend, schützend, FARBVERTIEFEND
  - für Marmor, Naturstein, Kunststein, hochglanzpolierte Flächen, Böden, Treppen, Fensterbänke
  - Anwendung: in Eimer mit warmem Wasser mischen, mit Aufnehmer gleichmäßig auftragen,
    trocknen lassen, optional auspolieren für zusätzlichen Glanz
  - Made in Germany, Schwarzwald, Jotti seit 1912

⚠ TWO SOURCE-DATA WARNINGS FOR WHOEVER PICKS THIS UP:
  1. The sheet's "USPs" block was copied from a COMPETITOR listing and names MELLERUD
     throughout. That brand must never appear in any copy, overlay or alt text. Only the
     SEO team's own title/bullets (which correctly say Jotti) were used here.
  2. ERGIEBIGKEIT (coverage) is a live review complaint, but the sheet gives no m² figure.
     Image 6 asks for it explicitly and marks it TO CONFIRM. Do not invent a number.

VoC — POSITIV: gute Reinigungsleistung auf Marmor und Granit, entfernt Dreckschichten und
Grünspan, schöner Glanz, Flächen wirken wie neu.
VoC — EINWÄNDE: Schlieren (uneinheitliche Meinungen zur Schlierenfreiheit), Ergiebigkeit,
unterschiedlich bewertete Glanzwirkung. Schlieren ist der wichtigste: er wird in Bild 2 und
in der Anwendung (Bild 6) direkt beantwortet.

Compliance (DE): keine Preise, keine URLs, kein "beste/#1/garantiert", keine Desinfektions-
oder Hygieneversprechen, keine Heilaussagen, kein Fremdmarkenname.

NOTE: the Jotti brand config is written for the LEATHER line (photo rules mention saddles,
boots, no synthetic leather). Those rules do not fit a stone cleaner. The art direction below
keeps the brand's heritage warmth and German-manufacture feel while staying truthful to the
product. Worth updating the brand config to cover the cleaning line.
"""
from __future__ import annotations
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent          # self-contained product folder
ROOT = HERE.parents[5]                           # project root (Claude_Code/)
sys.path.insert(0, str(ROOT))

from tools.brief_app.core.customers import load_customer
from tools.brief_app.core.excel_parser import parse_excel
from tools.brief_app.core.pdf_builder import BriefBuilder
from tools.brief_app.core.ai import AIImagePlanItem, AIModule, AIQA
from tools.brief_app.core.seo_loader import load_seo, as_bullets_html


EXCEL = HERE / "listing.xlsx"
PLAN_NO = "13"
ASIN = "TO_CONFIRM"      # the sheet's ASIN cell is empty — fill in before delivery


IMAGES = [
    AIImagePlanItem(
        name="Bild 1 — Main Hero (3 Optionen für den A/B-Test)",
        role="hero",
        layout="clean_hero",
        graphics=[],
        background="Pure white #FFFFFF. Identical across all three options so the split test isolates "
                   "composition, not colour.",
        purpose="Win the click. The SEO team's CTR note is explicit: the current main image is not "
                "attractive. Ship all three and keep the winner via Manage Your Experiments.",
        visual=(
            "Amazon slot 1 stays pure white, product only, no overlay text and no graphics (policy). "
            "These three are the CTR mains you test against a clean white main.\n\n"

            "OPTION A — DAS ERGEBNIS AM STEIN\n"
            "The 500 ml bottle standing on a polished marble surface shot at a low three-quarter angle, "
            "so the stone's reflection carries under the bottle and the colour depth reads immediately. "
            "White background above and behind.\n"
            "Why it wins: the product is invisible in use, so the surface has to do the selling.\n\n"

            "OPTION B — MARMOR UND NATURSTEIN\n"
            "Bottle centred, with two clean stone samples laid flat in front of it: one light marble, one "
            "darker granite, both showing a treated half and an untreated half.\n"
            "Why it wins: it answers 'passt das auf meinen Stein?' before the click.\n\n"

            "OPTION C — DIE FLÄCHE, DIE GEMEINT IST\n"
            "Bottle in the lower third, with a marble floor and stair edge receding behind it, warm "
            "daylight raking across so the polish is visible.\n"
            "Why it wins: floors and stairs are the high-value use case and the reason for a 500 ml bottle.\n\n"

            "All three: product dominant, same lighting and colour temperature, honest stone colour."
        ),
        overlay="MARMOR WIE AM ERSTEN TAG.",
        overlay_sub="Reinigt, pflegt und vertieft die natürliche Farbe. Mit Carnaubawachs.",
        props=["500 ml Flasche", "polierte Marmorfläche", "Marmor- und Granitmuster", "Treppenkante"],
        lighting="Warm, raking daylight from camera-left so the polish and the colour depth are visible. "
                 "Soft fill right. No hard specular blowouts on the stone.",
        why_it_works=(
            "A cleaner is judged by the surface it leaves behind. All three options put the stone, not "
            "the bottle, in charge of the first impression."
        ),
        ctr="The category's mains are bottles on white. A visibly deepened, polished stone surface is a "
            "different silhouette in the search grid.",
        cvr="Option B pre-answers the compatibility question that otherwise stalls the purchase.",
    ),
    AIImagePlanItem(
        name="Bild 2 — Vorher / Nachher: Glanz und Farbtiefe",
        role="hook",
        layout="before_after",
        graphics=[
            "vertical divider down the exact centre, 3 px, Jotti brown #8B5A2B",
            "label chip top-left on the left half: 'VORHER', dark #2F2A26 on cream",
            "label chip top-right on the right half: 'NACHHER', white on Jotti brown",
            "thin arrow crossing the divider at mid-height, left to right",
            "small footer strip: 'Gleiche Fläche, gleiches Licht, gleicher Winkel.'",
        ],
        background="Cream #EFE6D9 outer frame, the stone surface fills the inner frame",
        purpose="Show the single result the buyer is paying for, and prove it honestly.",
        visual=(
            "One continuous marble or granite surface photographed ONCE from a fixed camera, split down "
            "the middle. LEFT: dull, greyed, with visible film and a faint streak pattern. RIGHT: the "
            "same surface cleaned and cared for, colour visibly deeper, an even satin sheen and NO "
            "streaks.\n\n"
            "The streak-free right half is doing specific work: 'Schlieren' is the most common complaint "
            "in the review data, so the frame must show an even finish with no wipe marks and no cloudy "
            "haze. Do not retouch the stone into a mirror. Honest satin beats fake gloss, and an "
            "over-polished fake will simply produce more streak complaints."
        ),
        overlay="SCHLIERENFREI TROCKNEN.",
        overlay_sub="Gleichmäßiger Glanz statt Wischspuren, wenn die Fläche trocknen darf.",
        props=["one continuous stone surface", "fixed camera position", "even satin finish on the right"],
        lighting="Single soft source, identical on both halves. Any lighting difference between the two "
                 "sides invalidates the comparison and reads as a trick.",
        why_it_works=(
            "The strongest positive review theme ('wirkt wie neu') and the strongest objection "
            "('Schlieren') are the same frame seen from two sides. Answering both at once is the most "
            "efficient image in the plan."
        ),
        ctr="A true before/after is the most clicked layout in the cleaning category.",
        cvr="Defuses the streak objection before the shopper reaches the reviews that raise it.",
    ),
    AIImagePlanItem(
        name="Bild 3 — Was drin ist und was es tut",
        role="educate",
        layout="annotated_callouts",
        graphics=[
            "bottle centred, upright, occupying the middle third",
            "4 callout labels pinned by 1 px lines to the bottle: upper-left 'CARNAUBAWACHS', "
            "upper-right 'FARBVERTIEFEND', lower-left 'FÜR NATUR- & KUNSTSTEIN', lower-right '500 ML'",
            "each callout is a cream chip with brown rule beneath and one short line of body text",
            "small carnauba-leaf line icon beside the wax callout",
        ],
        background="Cream #EFE6D9, clean and even",
        purpose="Explain the formula in one frame. The CVR note asks for images with clear ingredients "
                "and function.",
        visual=(
            "The bottle upright and centred, lit warm, with four callouts pinned to it by hairline "
            "leaders. Copy per callout, short:\n"
            "  • CARNAUBAWACHS — natürliches Wachs, pflegt und schützt die Oberfläche\n"
            "  • FARBVERTIEFEND — unterstützt die natürliche Farbwirkung des Steins\n"
            "  • FÜR NATUR- & KUNSTSTEIN — Marmor, Naturstein, hochglanzpolierte Flächen\n"
            "  • 500 ML — für Böden, Treppen und Fensterbänke im Innenbereich\n\n"
            "Keep every claim inside what the listing supports. No disinfection, no hygiene and no "
            "sealing claims."
        ),
        overlay="CARNAUBAWACHS PFLEGT MIT.",
        overlay_sub="Natürliches Wachs, das die Farbe vertieft und die Fläche schützt.",
        props=["500 ml bottle", "4 callout chips", "carnauba leaf icon"],
        lighting="Even, warm studio light. The label must be fully legible at thumbnail size.",
        why_it_works=(
            "Carnauba wax is the one concrete, ownable ingredient in the listing. Naming it and pinning "
            "it to the bottle turns a generic cleaner into a specific product."
        ),
        ctr="Callout layouts read as informative even before the text is legible.",
        cvr="Gives a rational reason to prefer this bottle over an unnamed supermarket cleaner.",
    ),
    AIImagePlanItem(
        name="Bild 4 — Die Flächen im Zuhause",
        role="desire",
        layout="lifestyle_candid",
        graphics=[
            "small cream caption strip along the bottom edge, 1 line",
            "no badges, no callouts: this is the one frame that stays purely photographic",
        ],
        background="Real interior, warm daylight through a window",
        purpose="Let the buyer place the product in their own home. This is the action image the CVR "
                "note asks for.",
        visual=(
            "A real interior moment: hands working a mop evenly across a marble floor in a hallway, with "
            "a marble stair edge and a windowsill visible in the same frame, all three surfaces the "
            "listing names. The bucket stands to one side, the bottle beside it, label readable.\n\n"
            "Warm afternoon daylight, lived-in but tidy. Heritage-warm in the Jotti manner: wood, brass "
            "and linen tones around the stone, nothing clinical and nothing showroom-sterile.\n"
            "Caption strip: 'Böden, Treppen und Fensterbänke im Innenbereich.'"
        ),
        overlay="GLANZ, DER BLEIBT.",
        overlay_sub="Für Böden, Treppen und Fensterbänke aus Marmor und Naturstein.",
        props=["mop and bucket", "500 ml bottle", "marble hallway floor", "stair edge", "windowsill"],
        lighting="Warm afternoon daylight from a window, raking low across the floor so the finish reads.",
        why_it_works=(
            "Naming three surfaces in one honest frame widens the use case from 'floor cleaner' to "
            "'stone care for the whole home', which is what justifies the bottle."
        ),
        ctr="A real interior stands out against the category's product-on-white sameness.",
        cvr="The buyer recognises their own hallway, which is the moment the purchase becomes concrete.",
    ),
    AIImagePlanItem(
        name="Bild 5 — Herkunft und Qualität",
        role="trust",
        layout="icon_row",
        graphics=[
            "bottle in the upper two thirds on cream",
            "row of 4 line icons across the base, evenly spaced, brown on cream, each with a short label",
            "icon 1 map/flag outline: 'MADE IN GERMANY'",
            "icon 2 fir tree: 'AUS DEM SCHWARZWALD'",
            "icon 3 date ribbon: 'SEIT 1912'",
            "icon 4 leaf: 'MIT CARNAUBAWACHS'",
            "hairline rule separating the icon row from the image above",
        ],
        background="Cream #EFE6D9 with a soft warm gradient behind the bottle",
        purpose="Convert heritage into a reason to trust the bottle over a cheaper alternative.",
        visual=(
            "The bottle standing on aged wood, warm side light, with a soft-focus hint of workshop "
            "behind it. Beneath, a clean row of four line icons with short labels. The icons carry the "
            "credentials; the photograph carries the feeling.\n\n"
            "Keep the icon set to exactly these four. Every one is supported by the listing, and a fifth "
            "invented badge would undo the credibility the other four buy."
        ),
        overlay="SEIT 1912 AUS DEM SCHWARZWALD.",
        overlay_sub="Deutsche Herstellung mit jahrzehntelanger Erfahrung und natürlichem Wachs.",
        props=["500 ml bottle", "aged wood surface", "4 line icons", "soft workshop background"],
        lighting="Warm side-light from camera-left, gentle falloff. Heritage, not moody.",
        why_it_works=(
            "'Made in Germany, seit 1912' is the brand's real asset and cannot be copied by a private "
            "label. Icons make it scannable in the half-second the shopper gives this tile."
        ),
        ctr="A row of clean credential icons reads as quality even at thumbnail size.",
        cvr="Answers the price objection in the SEO notes without ever mentioning price.",
    ),
    AIImagePlanItem(
        name="Bild 6 — Anwendung in vier Schritten",
        role="educate",
        layout="numbered_steps",
        graphics=[
            "4 equal panels left to right, thin cream dividers between",
            "large numeral 1 to 4 in Jotti brown, top-left of each panel",
            "one short German instruction line beneath each panel",
            "panel 4 carries a small 'OPTIONAL' chip",
            "footer strip in cream: 'Ergiebigkeit: ca. ___ m² je Flasche (TO CONFIRM mit Kunde)'",
        ],
        background="Cream #EFE6D9 panels, consistent across all four",
        purpose="Show how simple it is, and answer the two remaining objections: streaks and coverage.",
        visual=(
            "Four panels, identical composition and lighting, hands only:\n"
            "  1. Dosieren — Reiniger in einen Eimer mit warmem Wasser geben\n"
            "  2. Auftragen — mit dem Aufnehmer gleichmäßig auf der Fläche verteilen\n"
            "  3. Trocknen lassen — Fläche vollständig trocknen lassen\n"
            "  4. Auspolieren (optional) — für zusätzlichen Glanz nachpolieren\n\n"
            "Step 3 is the streak answer and must be unmistakable: show the surface drying evenly with "
            "no wipe marks. Most streak complaints in this category come from wiping a surface dry too "
            "early, so the plan gives that step its own panel rather than burying it.\n\n"
            "⚠ FOOTER — COVERAGE: 'Ergiebigkeit' is a live review complaint and the SEO sheet gives no "
            "m² figure. Ask the client for the real number and set it in the footer strip. Do NOT "
            "invent a coverage figure. If the client cannot supply one, delete the strip."
        ),
        overlay="EIMER, WISCHEN, FERTIG.",
        overlay_sub="Vier Schritte. Der vierte ist optional, wenn es besonders glänzen soll.",
        props=["bucket with warm water", "Aufnehmer / mop", "the bottle", "polishing cloth"],
        lighting="Bright, even and identical across all four panels so the sequence reads as one action.",
        why_it_works=(
            "The application is genuinely easy, and 'einfach' is a purchase trigger in this category. "
            "Giving the drying step its own panel converts the most common user error, and therefore the "
            "most common complaint, into an instruction."
        ),
        ctr="Numbered steps signal 'ich kann das selbst' at a glance.",
        cvr="Directly reduces the streak complaints that drive this listing's mixed reviews.",
    ),
    AIImagePlanItem(
        name="Bild 7 — Markenabschluss",
        role="close",
        layout="brand_close",
        graphics=[
            "Jotti logo centred in the lower band",
            "thin brown rule above the logo, full width",
            "tagline line beneath the logo",
            "no badges and no callouts: the close stays quiet",
        ],
        background="Warm, dark-wood workshop surface with soft daylight",
        purpose="Close on the brand rather than the feature, and make the buyer feel they chose well.",
        visual=(
            "The 500 ml bottle standing on aged wood beside a folded linen cloth and a polished marble "
            "offcut, warm daylight from the side. Quiet, made, unhurried. Lower band carries the Jotti "
            "logo and one line of brand copy about German manufacture since 1912.\n\n"
            "This is the second and last purely photographic tile in the plan. Keep it free of graphics "
            "so it reads as a pause after the information-dense tiles before it."
        ),
        overlay="TRADITION, DIE PFLEGT.",
        overlay_sub="Jotti aus dem Schwarzwald. Seit 1912 für Oberflächen, die bleiben sollen.",
        props=["500 ml bottle", "aged wood", "folded linen cloth", "polished marble offcut", "Jotti logo"],
        lighting="Warm daylight from camera-right, long soft shadow. Calm and premium.",
        why_it_works=(
            "After six working tiles the buyer needs one frame that simply feels like the brand. "
            "Heritage closes the sale that specifications opened."
        ),
        ctr="Brand-forward closes are rarely clicked first, but they hold the shopper who reached the end.",
        cvr="Turns a cleaning purchase into a considered choice, which supports the price position.",
    ),
]


MODULES = [
    AIModule(
        name="Modul 1 — Premium Full Image: Markenbanner",
        role="a+_banner",
        headline="STEINPFLEGE SEIT 1912",
        body=(
            "Der Jotti Marmor Reiniger pflegt Marmor, Naturstein und Kunststein im Innenbereich. "
            "Mit natürlichem Carnaubawachs reinigt er schonend, schützt die Oberfläche und vertieft "
            "die natürliche Farbe des Steins. Hergestellt im Schwarzwald, mit der Erfahrung von über "
            "hundert Jahren."
        ),
        visual=("Wide banner. LEFT THIRD: the bottle on aged wood, warm side-light. RIGHT TWO THIRDS: a "
                "marble hallway floor receding into warm daylight. Jotti logo upper-left, headline set "
                "across the left third, body beneath it. Desktop 1464x600, mobile 600x450 — on mobile "
                "the bottle and the headline stay inside the safe area, the hallway crops away."),
        alt="Jotti Marmor Reiniger 500 ml auf Holz vor einem gepflegten Marmorboden.",
    ),
    AIModule(
        name="Modul 2 — Premium Carousel (5 Kacheln): Warum Jotti",
        role="a+_carousel",
        headline="WARUM JOTTI",
        body=(
            "Kachel 1: <b>MIT CARNAUBAWACHS</b> — Natürliches Wachs, das pflegt und schützt.<br/>"
            "Kachel 2: <b>FARBVERTIEFEND</b> — Unterstützt die natürliche Farbwirkung des Steins.<br/>"
            "Kachel 3: <b>FÜR NATUR- &amp; KUNSTSTEIN</b> — Marmor, Naturstein, polierte Flächen.<br/>"
            "Kachel 4: <b>EINFACH ANZUWENDEN</b> — Mischen, auftragen, trocknen lassen.<br/>"
            "Kachel 5: <b>MADE IN GERMANY</b> — Hergestellt im Schwarzwald, seit 1912."
        ),
        visual=("5 square tiles at 220x220. Identical white-on-cream treatment, one line icon per tile "
                "(leaf, colour swatch, stone sample, bucket, fir tree), label beneath. Brown accent rule "
                "under each icon. Alt text per tile."),
        alt="Fünf Kacheln mit den Kernmerkmalen des Jotti Marmor Reinigers.",
    ),
    AIModule(
        name="Modul 3 — Premium Full Image: Vorher / Nachher",
        role="a+_banner",
        headline="GLANZ OHNE SCHLIEREN",
        body=(
            "Stumpfe Flächen entstehen durch Schmutzfilm und Pflegerückstände. Der Jotti Marmor "
            "Reiniger löst diesen Film und pflegt die Fläche in einem Arbeitsgang. Wichtig ist der "
            "letzte Schritt: Die Fläche vollständig trocknen lassen, statt sie trocken zu wischen. "
            "So entsteht ein gleichmäßiger Glanz ohne Wischspuren."
        ),
        visual=("Wide banner split down the centre: LEFT the dull, filmed surface labelled VORHER; RIGHT "
                "the same surface, deeper in colour with an even satin sheen, labelled NACHHER. One "
                "continuous stone surface, one camera position, identical light on both halves. Mobile "
                "keeps the split but crops tighter."),
        alt="Vorher-Nachher-Vergleich einer Marmorfläche vor und nach der Anwendung.",
    ),
    AIModule(
        name="Modul 4 — Premium Full Image: Anwendung",
        role="a+_banner",
        headline="IN VIER SCHRITTEN ANGEWENDET",
        body=(
            "1. Den Reiniger in einem Eimer mit warmem Wasser mischen. 2. Mit dem Aufnehmer "
            "gleichmäßig auf der Fläche verteilen. 3. Die Fläche vollständig trocknen lassen. "
            "4. Wer mehr Glanz möchte, poliert anschließend nach. Geeignet für Böden, Treppen und "
            "Fensterbänke aus Marmor, Naturstein und Kunststein im Innenbereich."
        ),
        visual=("Wide 4-panel banner, hands only, identical composition and light per panel: DOSIEREN → "
                "AUFTRAGEN → TROCKNEN LASSEN → AUSPOLIEREN (optional). Large brown numerals top-left of "
                "each panel, one instruction line beneath. Mobile stacks into 2x2."),
        alt="Vier Schritte der Anwendung des Jotti Marmor Reinigers.",
    ),
    AIModule(
        name="Modul 5 — Premium Carousel (5 Kacheln): Geeignete Flächen",
        role="a+_carousel",
        headline="FÜR DIESE FLÄCHEN GEEIGNET",
        body=(
            "Kachel 1: <b>MARMORBÖDEN</b> — Flure, Wohnräume und Eingangsbereiche.<br/>"
            "Kachel 2: <b>TREPPEN</b> — Stufen und Podeste aus Naturstein.<br/>"
            "Kachel 3: <b>FENSTERBÄNKE</b> — Innenfensterbänke aus Marmor und Naturstein.<br/>"
            "Kachel 4: <b>HOCHGLANZPOLIERTE FLÄCHEN</b> — Polierte Steinoberflächen im Innenbereich.<br/>"
            "Kachel 5: <b>KUNSTSTEIN</b> — Geeignete Flächen aus Kunststein.<br/><br/>"
            "Im Zweifel an einer unauffälligen Stelle testen."
        ),
        visual=("5 square lifestyle tiles at 220x220, same camera height and warm daylight in each, one "
                "surface per tile. Label band beneath each. Alt text per tile names the surface."),
        alt="Fünf Kacheln mit den geeigneten Flächen für den Jotti Marmor Reiniger.",
    ),
    AIModule(
        name="Modul 6 — Premium Q&A",
        role="a+_qa",
        headline="HÄUFIGE FRAGEN",
        body=(
            "<b>F.</b> Hinterlässt der Reiniger Schlieren?<br/>"
            "<b>A.</b> Entscheidend ist der letzte Schritt. Die Fläche nach dem Auftragen vollständig "
            "trocknen lassen, statt sie trocken zu wischen. So trocknet sie gleichmäßig auf. Für "
            "zusätzlichen Glanz kann anschließend nachpoliert werden.<br/><br/>"

            "<b>F.</b> Für welche Flächen ist er geeignet?<br/>"
            "<b>A.</b> Für Marmor, Naturstein, Kunststein und hochglanzpolierte Steinflächen im "
            "Innenbereich, zum Beispiel Böden, Treppen und Fensterbänke. Im Zweifel an einer "
            "unauffälligen Stelle testen.<br/><br/>"

            "<b>F.</b> Wie wird er dosiert?<br/>"
            "<b>A.</b> Den Reiniger in einem Eimer mit warmem Wasser mischen und mit einem Aufnehmer "
            "gleichmäßig auf der Fläche verteilen.<br/><br/>"

            "<b>F.</b> Was bewirkt das Carnaubawachs?<br/>"
            "<b>A.</b> Carnaubawachs ist ein natürliches Wachs. Es pflegt die Oberfläche, unterstützt "
            "den Schutz der behandelten Fläche und vertieft die natürliche Farbwirkung des Steins.<br/><br/>"

            "<b>F.</b> Ist er auch für polierte Flächen geeignet?<br/>"
            "<b>A.</b> Ja, er kann auch zur Pflege entsprechender hochglanzpolierter Steinoberflächen "
            "eingesetzt werden.<br/><br/>"

            "<b>F.</b> Wo wird er hergestellt?<br/>"
            "<b>A.</b> In Deutschland. Jotti fertigt seit 1912 im Schwarzwald."
        ),
        visual="Vertical Q/A table, text only. Brown divider rules between questions, small brown F. and "
               "dark A. labels. Mobile-first line lengths.",
        alt="Häufige Fragen zum Jotti Marmor Reiniger.",
    ),
    AIModule(
        name="Modul 7 — Premium Comparison: die Jotti Steinpflege",
        role="a+_comparison",
        headline="DIE JOTTI PFLEGE IM ÜBERBLICK",
        body=(
            "Vergleich über die Jotti Reinigungslinie, nicht über Fremdmarken.<br/><br/>"
            "Spalten: <b>Marmor Reiniger 500 ml</b> · Putzstein · Polsterreiniger · Möbelwachs.<br/><br/>"
            "Zeilen: Geeignet für Marmor &amp; Naturstein · Mit Carnaubawachs · Farbvertiefend · "
            "Für Böden, Treppen &amp; Fensterbänke · Anwendung mit Wasser im Eimer · Made in Germany.<br/><br/>"
            "Die erste Spalte hervorheben. Nur Jotti-eigene Produkte, keine Fremdmarken."
        ),
        visual=("Standard Amazon Premium Comparison Chart, 4 columns, first column highlighted in Jotti "
                "brown with a small 'Seit 1912' ribbon. Cream header row, one product image per column."),
        alt="Vergleichstabelle der Jotti Pflegeprodukte mit dem Marmor Reiniger in der ersten Spalte.",
    ),
]


# Five pairs, question ≤80 chars, answer ≤120 (house standard — the A+ Q&A is scanned on a
# phone). Cut from seven: "hochglanzpoliert" duplicated the surfaces answer, and dosage volume
# is a value question rather than one that blocks a purchase.
QA = [
    AIQA(q="Hinterlässt der Reiniger Schlieren?",
         a="Nicht, wenn die Fläche nach dem Auftragen trocknen darf statt trocken gewischt zu "
           "werden. Danach nachpolieren."),
    AIQA(q="Für welche Flächen ist er geeignet?",
         a="Marmor, Naturstein, Kunststein und hochglanzpolierte Steinflächen im Innenbereich. "
           "Im Zweifel unauffällig testen."),
    AIQA(q="Wie wird er dosiert und angewendet?",
         a="Mit warmem Wasser im Eimer mischen, gleichmäßig auftragen, trocknen lassen. Für mehr "
           "Glanz danach nachpolieren."),
    AIQA(q="Was bewirkt das Carnaubawachs?",
         a="Ein natürliches Wachs. Es pflegt die Oberfläche und vertieft die natürliche "
           "Farbwirkung des Steins."),
    AIQA(q="Wo wird der Marmor Reiniger hergestellt?",
         a="In Deutschland. Jotti fertigt seit 1912 im Schwarzwald."),
]


def main() -> None:
    print("Loading Jotti customer + parsing listing…")
    cust = load_customer("jotti")
    brief = parse_excel(EXCEL)
    seo = load_seo(EXCEL)
    OUT = HERE / f"{PLAN_NO}_{ASIN}_Image Plan.pdf"
    print(f"  Product: {brief.product_name}  ASIN {ASIN}  Marketplace: {cust.marketplace}")
    print(f"  USPs={len(brief.usps)} KWs={len(brief.all_keywords)} "
          f"reviews=+{len(brief.good_reviews)}/-{len(brief.bad_reviews)}")

    builder = BriefBuilder(cust, brief, OUT, ai=None)
    builder._ai_title = seo.title
    builder._ai_bullets = as_bullets_html(seo)
    builder._ai_images = IMAGES
    builder._ai_modules = MODULES
    builder._ai_qa = QA
    builder._ai_backend = seo.backend
    builder.copy_source_label = ("SEO-Sheet (Titel/Bullets/Backend) + hand-written senior creative "
                                 "(Overlays, A+, Q&A) — DE")
    # Jotti's brand-level moodboard terms describe the LEATHER line (saddles, boots, balm), which
    # briefs the wrong references entirely for a stone cleaner. Override for this product.
    builder.moodboard_terms = [
        "marble floor hallway polished warm daylight interior",
        "natural stone staircase interior clean bright",
        "marble windowsill detail sunlight home",
        "granite surface texture macro polished",
        "mop bucket cleaning stone floor hands",
        "black forest workshop german manufacture heritage",
    ]

    print("Building branded PDF…")
    pdf_path = builder.build()
    import re
    pages = len(re.findall(rb'/Type\s*/Page[^s]', pdf_path.read_bytes()))
    print(f"Built: {pdf_path}")
    print(f"  Pages: {pages}  Size: {pdf_path.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
