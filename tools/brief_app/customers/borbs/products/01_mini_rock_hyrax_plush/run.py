"""Borbs — Mini Rock Hyrax Plush  [Produkt 01]
Hand-written, KW-led, conversion-focused copy (playful, marketing-elevated).

Marketplace: amazon.com (US). Marke: Borbs (new brand).
Folder ASIN B0FDFLVGNH; listing.xlsx parses B0FHC82ZWG (mismatch flagged to Jonas).

House rules aktiv (Config): new_brand=true -> A+ Comparison-Modul wird automatisch
weggelassen; brand_statement -> 'From Borbs:'-Zeile wird automatisch ans Q&A-Modul gehängt.

Copywriting-Standard angewandt: dream-outcome-first, Voice-of-Customer, power words,
punchy-but-smooth. Die zwei Top-Review-Einwände (zu klein / zu wenig gestopft) werden
direkt auf den Bildern entkräftet (immer plump + ehrliche Größenreferenz).

COMPLIANCE: Sensory-Beads nur 'calming/soothing/sensory' — KEINE medizinischen Claims
(nicht 'treats anxiety/stress'). Keine Superlative. Ehrliche Größe. Ages 3+.
"""
from __future__ import annotations
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
sys.path.insert(0, str(ROOT))

from tools.brief_app.core.customers import load_customer
from tools.brief_app.core.excel_parser import parse_excel
from tools.brief_app.core.pdf_builder import BriefBuilder
from tools.brief_app.core.ai import AIImagePlanItem, AIModule, AIQA

PLAN_NO = "01"
ASIN = "B0FDFLVGNH"   # folder ASIN; listing content shows B0FHC82ZWG — bitte bestätigen
EXCEL = HERE / "listing.xlsx"


TITLE = ('Borbs Mini Rock Hyrax Plush — Adorable Dassie Stuffed Animal with Calming Sensory '
         'Fidget Beads · Super-Soft Cuddly Cotton · 12" Collectible Plushie for Kids, Teens & '
         'Animal Lovers · Ages 3+')

BULLETS = [
    "<b>MEET THE ROCK HYRAX — NATURE'S UNDERDOG</b> — This little dassie (the chubby "
    "\"rock rabbit\") is reborn as a round, squishy Borb you'll want to hug on sight. A genuinely "
    "unique plush for animal lovers who are tired of the same old bears and bunnies.",

    "<b>IRRESISTIBLY SOFT &amp; FULLY PLUMP</b> — Brushed cotton plush over extra-soft stuffing "
    "makes every Borb squishy, huggable and full — the kind of soft you don't want to put down. "
    "Made to stay plump and cuddly, cuddle after cuddle.",

    "<b>CALMING SENSORY FIDGET BEADS INSIDE</b> — Hidden within is a soft bead pocket to squish, "
    "press and fidget — a soothing, tactile little comfort for busy hands and cozy moments. Quiet "
    "sensory fun that travels everywhere you do.",

    "<b>JUST-RIGHT MINI SIZE · 12 INCHES</b> — At 12 x 5 x 5 in, your Borb cuddles in your arms, "
    "perches on a shelf or desk, and tucks straight into a bag. Small enough to take anywhere, big "
    "enough to hug — exactly the size a mini plush should be.",

    "<b>A GIFT THEY'LL ADORE · AGES 3+</b> — Wholesome, neatly stitched and endlessly cute — the "
    "perfect little surprise for kids, teens, animal lovers and plush collectors. Meet your first "
    "Borb… then start the whole collection.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="Bright white with a soft warm-cream #FFF4EC base and a cheerful teal/coral accent. Identical across all 3 for a clean split test.",
        purpose="Win the click with instant cuteness — and signal 'soft + plump + unique animal' at thumbnail size.",
        visual=(
            "Mock ALL 3 options. Product exactly as real: the brown Mini Rock Hyrax plush, shown "
            "FULLY STUFFED and round (never flat), soft texture visible. ONE cute callout each, "
            "plush dominant ~70%. Amazon slot-1 main = pure white / plush only.\n\n"
            "OPTION A — PURE CUTENESS: the hyrax front-on, big adorable eyes, plump and round, a "
            "tiny coral heart accent. Badge (teal): 'MEET YOUR NEW BORB'.\n"
            "OPTION B — SOFT & PLUMP: the plush gently squished in two hands to show softness and "
            "full stuffing. Badge (coral): 'SO SOFT. SO PLUMP.'\n"
            "OPTION C — SENSORY FEATURE: plush with a small cutaway/icon showing the internal "
            "fidget beads. Badge (teal): 'CALMING FIDGET BEADS'.\n\n"
            "Across all 3: plush ~70%, callout ~6%, same bright lighting + colour temperature."
        ),
        overlay="(one callout per option)",
        overlay_sub="3 hero options shipped — A/B test, keep the winner.",
        props=["A: plush front-on, plump, coral heart accent", "B: plush squished in two hands", "C: plush + fidget-bead cutaway/icon"],
        lighting="Bright, soft, cheerful high-key light; gentle shadow so the plush reads round and full.",
        why_it_works=(
            "Three triggers: pure cuteness (the click), soft+plump (defuses the 'flat/under-stuffed' "
            "worry up front), and the sensory bead feature (the differentiator). Cute and clear at "
            "thumbnail size."
        ),
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: an animal you've never hugged before",
        role="hook",
        background="Warm cream #FFF4EC with a playful teal headline shape",
        purpose="Own the uniqueness — the reason to pick a hyrax over another bear or bunny.",
        visual=(
            "The plush centre-stage, big friendly eyes to camera. A small, charming 'did you know?' "
            "flourish: a tiny illustrated real rock hyrax (dassie) beside the plush with a cute "
            "line — 'The rock hyrax: a chubby little \"rock rabbit\" — and secretly the elephant's "
            "closest cousin.' Keep it delightful and wholesome. Coral heart accents."
        ),
        overlay="THE CUTEST LITTLE HYRAX.",
        overlay_sub="A genuinely unique plush — for animal lovers over the same old bears.",
        props=["plush front-on", "tiny illustrated real hyrax", "cute fact flourish", "coral heart accents"],
        lighting="Bright, warm, storybook-friendly. Cute over dramatic.",
        why_it_works=(
            "Uniqueness is the whole pitch (top keyword: 'unique stuffed animals'). A charming fact "
            "makes the hyrax instantly lovable and gives gift-buyers a story to tell."
        ),
    ),
    AIImagePlanItem(
        name="Image 3 — Feature: calming sensory fidget beads",
        role="educate",
        background="Soft teal-tinted white, clean and friendly",
        purpose="Show the standout feature — the tactile, soothing fidget beads.",
        visual=(
            "A gentle cutaway or hands squishing the plush to reveal the internal soft bead pocket, "
            "with a small icon trio: 'Squish · Press · Fidget'. Short caption: 'A soft, soothing "
            "sensory feature for busy hands and calm-down moments.' Keep it a comforting lifestyle "
            "benefit — no medical wording."
        ),
        overlay="SQUISH THE FIDGET BEADS.",
        overlay_sub="A soft, soothing sensory feature for busy hands and cozy calm-down moments.",
        props=["hands squishing plush", "internal bead pocket cutaway", "Squish/Press/Fidget icons"],
        lighting="Bright, tactile, inviting — you can almost feel the squish.",
        why_it_works=(
            "The sensory beads are what separates this from every plain plush. Framing them as a "
            "calming, tactile joy (not a treatment) adds real value and stays fully compliant."
        ),
    ),
    AIImagePlanItem(
        name="Image 4 — Softness & full stuffing (defuse 'flat')",
        role="desire",
        background="Warm cream, cozy close-up",
        purpose="Directly answer the 'arrived under-stuffed / flat' complaint with proof of plumpness.",
        visual=(
            "Macro of the brushed cotton plush texture plus a shot of the plush hugged tight and "
            "springing back to full, round shape. Small callouts: 'Extra-soft stuffing', 'Brushed "
            "cotton plush', 'Stays plump &amp; huggable'. Cozy, tactile, reassuring."
        ),
        overlay="HUGGABLY SOFT & FULL.",
        overlay_sub="Extra-soft stuffing and brushed cotton plush — plump and cuddly, not flat.",
        props=["plush texture macro", "plush hugged + springing back full", "3 soft-feature callouts"],
        lighting="Warm, soft, close-up light that shows the fluffy texture.",
        why_it_works=(
            "'Under-stuffed / flat' is a top 1-star theme. Proving the plush is genuinely soft and "
            "stays full sets honest expectations and lifts satisfaction and reviews."
        ),
        cvr="Turns the biggest objection into a reason to buy.",
    ),
    AIImagePlanItem(
        name="Image 5 — Honest size: just-right 12 inches",
        role="desire",
        background="Clean white with a friendly teal ruler graphic",
        purpose="Set true size expectations — the #1 complaint is 'smaller than expected'.",
        visual=(
            "The plush shown IN A HAND and beside an everyday object (a mug and a ruler) with a "
            "clear callout: '12 x 5 x 5 in (30 cm) — mini size'. A tiny scene strip: on a shelf, "
            "in a backpack pocket, cuddled in arms. Honest and cheerful — 'small enough to take "
            "anywhere, big enough to hug'."
        ),
        overlay="JUST-RIGHT MINI SIZE.",
        overlay_sub="12 x 5 x 5 in — cuddles in your arms, perches on a shelf, tucks in a bag.",
        props=["plush in a hand", "plush beside a mug + ruler", "size callout 12x5x5 in", "shelf/bag/arms strip"],
        lighting="Bright, even, honest — true size, true colour.",
        why_it_works=(
            "Wrong-size expectations drive returns and bad reviews. An honest, cheerful size "
            "reference up front prevents disappointment and frames the mini size as a feature."
        ),
    ),
    AIImagePlanItem(
        name="Image 6 — Cuddle, decorate, collect, gift",
        role="desire",
        background="Bright playful lifestyle collage",
        purpose="Show the joyful ways to love a Borb — and open the door to collecting/gifting.",
        visual=(
            "A cheerful four-scene collage: 1) a child/teen cuddling the plush; 2) the hyrax "
            "perched on a shelf/desk as decor; 3) a little row of Borbs (hint at the collection); "
            "4) the plush with a simple gift ribbon. Warm, wholesome, joyful. Coral/teal accents."
        ),
        overlay="CUDDLE. DECORATE. COLLECT.",
        overlay_sub="A cuddle buddy, a cute shelf-mate, a collectible — and a gift they'll adore.",
        props=["cuddle scene", "shelf/desk decor scene", "row of Borbs (collection)", "gift-ribbon scene"],
        lighting="Bright, warm, happy lifestyle light across all four scenes.",
        why_it_works=(
            "Multiplies the reasons to buy (cuddle + decor + collect + gift) and plants the "
            "collection seed — turning one purchase into a series."
        ),
    ),
    AIImagePlanItem(
        name="Image 7 — Brand close: start your Borbs family",
        role="close",
        background="Bright, playful Borbs brand panel (teal + coral on cream)",
        purpose="Close on the brand world and the collectible hook.",
        visual=(
            "The hyrax plush front and centre with a few other 'coming soon' Borbs silhouettes/"
            "friends around it, the Borbs wordmark, and a cheerful line inviting buyers into the "
            "world of underrated-animal plushies. Warm, joyful, brand-forward."
        ),
        overlay="START YOUR BORBS FAMILY.",
        overlay_sub="Meet the hyrax — then collect the cutest underrated animals around.",
        props=["hyrax plush hero", "other Borbs friends (silhouettes)", "Borbs wordmark"],
        lighting="Bright, cheerful, brand-forward. Joyful and inviting.",
        why_it_works=(
            "Closes on identity and the collection: buyers aren't just buying a plush, they're "
            "joining the Borbs world — the hook that drives repeat purchases."
        ),
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Brand banner",
        role="a+_banner",
        headline="MEET YOUR NEW FAVOURITE BORB.",
        body=(
            "The Borbs Mini Rock Hyrax is a round, squishy plush of one of nature's most underrated "
            "cuties — the chubby little \"rock rabbit.\" Brushed cotton plush, extra-soft stuffing "
            "and hidden calming fidget beads make it huggable, soothing and impossible not to love."
        ),
        visual="Wide bright banner: the plump hyrax plush right, playful headline left on cream, teal/coral accents. Borbs wordmark upper-left.",
        alt="Borbs Mini Rock Hyrax plush banner: round, soft and huggable with calming fidget beads.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): Why you'll love it",
        role="a+_carousel",
        headline="WHY YOU'LL LOVE IT",
        body=(
            "Tile 1: <b>UNIQUELY CUTE</b> — A rock hyrax, not another bear or bunny.<br/>"
            "Tile 2: <b>SO SOFT &amp; PLUMP</b> — Brushed cotton plush, extra-soft stuffing.<br/>"
            "Tile 3: <b>CALMING FIDGET BEADS</b> — A soothing, tactile sensory feature.<br/>"
            "Tile 4: <b>JUST-RIGHT 12 IN</b> — Cuddle it, shelf it, take it anywhere.<br/>"
            "Tile 5: <b>A GIFT THEY'LL ADORE</b> — Ages 3+, for kids, teens &amp; collectors."
        ),
        visual="5 square tiles, coral accent corner each, cute rounded icons (hyrax · plush · beads · ruler · gift).",
        alt="Five A+ tiles: uniquely cute, soft and plump, calming fidget beads, 12 inch size, great gift.",
    ),
    AIModule(
        name="Module 3 — Banner: soft, plump & soothing",
        role="a+_banner",
        headline="HUGGABLY SOFT. SOOTHINGLY SQUISHY.",
        body=(
            "Brushed cotton plush over extra-soft stuffing keeps your Borb full, round and cuddly — "
            "not flat. Inside, a soft bead pocket to squish and fidget adds a calming, tactile "
            "little comfort for busy hands and cozy moments."
        ),
        visual="Banner split: soft-texture macro + plush springing back to full shape left; hands squishing the fidget beads right. Warm, tactile, bright.",
        alt="A+ banner showing the soft, full stuffing and calming internal fidget beads.",
    ),
    AIModule(
        name="Module 4 — Banner: just-right size, everywhere you go",
        role="a+_banner",
        headline="MINI SIZE. MAXIMUM CUDDLES.",
        body=(
            "At 12 x 5 x 5 inches, your Borb is small enough to tuck into a bag and big enough to "
            "hug all day. Cuddle it, perch it on a shelf or desk, take it on trips — then make room "
            "for the next one."
        ),
        visual="Banner: plush in a hand + beside a mug/ruler with a 12x5x5 in callout, and a strip of scenes (shelf · backpack · arms). Bright and honest.",
        alt="A+ banner showing the honest 12-inch size of the Borbs Mini Rock Hyrax plush in a hand, on a shelf and in a bag.",
    ),
    AIModule(
        name="Module 5 — Carousel (5 tiles): the Borbs world",
        role="a+_carousel",
        headline="WELCOME TO THE BORBS WORLD",
        body=(
            "Tile 1: <b>CUDDLE</b> — A soft companion for cozy moments.<br/>"
            "Tile 2: <b>DECORATE</b> — An adorable shelf- and desk-mate.<br/>"
            "Tile 3: <b>FIDGET</b> — Calming beads to squish anytime.<br/>"
            "Tile 4: <b>COLLECT</b> — Meet the underrated animals of Borbs.<br/>"
            "Tile 5: <b>GIFT</b> — The cutest little surprise, ages 3+."
        ),
        visual="5 lifestyle tiles (cuddle · shelf decor · fidget · a row of Borbs · gift ribbon), consistent bright cheerful styling.",
        alt="Five A+ tiles showing ways to enjoy Borbs: cuddle, decorate, fidget, collect, gift.",
    ),
    AIModule(
        name="Module 6 — Premium Q&A",
        role="a+_qa",
        headline="QUESTIONS BEFORE YOU CUDDLE",
        body=(
            "<b>Q.</b> What animal is it?<br/>"
            "<b>A.</b> A rock hyrax (a \"dassie\" or \"rock rabbit\") — a chubby, adorable little "
            "animal, here as a round, squishy Borb.<br/><br/>"
            "<b>Q.</b> How big is it?<br/>"
            "<b>A.</b> Mini size: 12 x 5 x 5 inches — cuddles in your arms, perches on a shelf and "
            "tucks into a bag.<br/><br/>"
            "<b>Q.</b> What are the fidget beads for?<br/>"
            "<b>A.</b> A soft internal bead pocket to squish, press and fidget — a soothing, "
            "tactile little comfort for busy hands.<br/><br/>"
            "<b>Q.</b> Is it soft and well-made?<br/>"
            "<b>A.</b> Yes — brushed cotton plush over extra-soft stuffing, neatly stitched to stay "
            "plump and huggable.<br/><br/>"
            "<b>Q.</b> Who is it for?<br/>"
            "<b>A.</b> Ages 3+ — a wonderful gift for kids, teens, animal lovers and plush "
            "collectors."
        ),
        visual="Vertical Q/A table, teal divider lines, small teal Q. and coral A. labels; friendly rounded type.",
        alt="Premium Q&A module for the Borbs Mini Rock Hyrax plush.",
    ),
]


QA = [
    AIQA(q="What animal is the plush?",
         a="It's a rock hyrax — also called a dassie or \"rock rabbit\" — a chubby, adorable little animal, reimagined as a round, squishy Borb."),
    AIQA(q="How big is it?",
         a="Mini size: 12 x 5 x 5 inches (about 30 cm). Small enough to tuck into a bag, big enough to hug — it cuddles in your arms or perches on a shelf or desk."),
    AIQA(q="Is it soft, and does it stay full?",
         a="Yes. It's brushed cotton plush over extra-soft stuffing, neatly stitched to stay plump, round and huggable rather than flat."),
    AIQA(q="What are the sensory fidget beads?",
         a="A soft internal bead pocket you can squish, press and fidget with — a soothing, tactile little comfort for busy hands and cozy moments."),
    AIQA(q="What age is it suitable for?",
         a="Ages 3 and up. It makes a lovely gift for kids, teens, animal lovers and plush collectors."),
    AIQA(q="Can I use it as decoration?",
         a="Absolutely. Plenty of fans perch their hyrax on a shelf or desk as a cute display piece as well as a cuddle buddy."),
    AIQA(q="Are there other Borbs to collect?",
         a="The hyrax is your gateway Borb — Borbs celebrates the world's most underrated animals, so keep an eye out for more cute characters to collect."),
]


BACKEND = (
    "hyrax stuffed animal plush toy cute stuffies unique stuffed animals small plushie kids teens "
    "animal lover gift sensory fidget beads soft cuddly collectible dassie rock rabbit brown plush "
    "12 inch mini stuffed animal decoration cozy squishy borbs"
)


def main() -> None:
    print("Lade Borbs + Mini Rock Hyrax Listing…")
    cust = load_customer("borbs")
    brief = parse_excel(EXCEL)
    OUT = HERE / f"{PLAN_NO}_{ASIN}_Image Plan.pdf"
    print(f"  Produkt: {brief.product_name}  ASIN: {ASIN}  Marktplatz: {cust.marketplace}")
    print(f"  new_brand={cust.new_brand} (Comparison wird weggelassen)  brand_statement gesetzt={bool(cust.brand_statement)}")

    builder = BriefBuilder(cust, brief, OUT, ai=None)
    builder._ai_title = TITLE
    builder._ai_bullets = BULLETS
    builder._ai_images = IMAGES
    builder._ai_modules = MODULES
    builder._ai_qa = QA
    builder._ai_backend = BACKEND
    builder.copy_source_label = "Hand-written senior copy (playful, marketing-elevated)"

    print("Baue Branded PDF…")
    pdf_path = builder.build()
    size_kb = pdf_path.stat().st_size // 1024
    import re
    pages = len(re.findall(rb'/Type\s*/Page[^s]', pdf_path.read_bytes()))
    print(f"Gebaut: {pdf_path}")
    print(f"  Seiten: {pages}  Größe: {size_kb} KB")


if __name__ == "__main__":
    main()
