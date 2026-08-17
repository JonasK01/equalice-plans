"""Freshly Preserved — Product 04 · FALL CAKE DECORATING KIT 4 oz (25+ mixed flowers & leaves).

ASIN: B0H9532666 · Marketplace: amazon.com (USA) — English overlays + customer copy.
(The Overview tab also carries an older ASIN, B0DH2XBFY3 — the SEO deliverable is filed under
B0H9532666, so that is the ASIN used here.)

WHAT MAKES THIS ONE DIFFERENT — three things, and all three drive the creative:
  1. It is a KIT, not an ingredient. Roses, amaranth (firesticks), oregano flowers, ferns and
     geranium leaves — flowers AND greenery, which is what makes a cake look arranged rather
     than sprinkled. Sell the finished autumn cake, then show the kit that built it.
  2. It is 4 oz — TWENTY TIMES the weight of the 0.2 oz packs. The family's "smaller than
     expected" objection inverts here: abundance is the story, so show the pile.
  3. It is SEASONAL. Fall weddings, Thanksgiving, autumn birthdays, holiday dessert tables —
     and a genuine gift purchase for the baker in the family.
The skill promise from the SEO bullets is the real hook: "no piping tips or advanced frosting
techniques required" — a bakery-looking cake from someone who cannot pipe.

TITLE + BULLETS come 1:1 from the SEO tab (the keyword axis). Overlays / A+ / Q&A are
hand-written. Parent-child is built in at Image 7 and A+ Module 5.

Compliance guardrails (US): no best / #1 / guaranteed · no health-cure claims · no prices or
URLs on-image. Colour stays HONEST — reviewers already say "not as bright as pictures".
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
PLAN_NO = "04"
ASIN = "B0H9532666"

CONTENTS = "roses · amaranth (firesticks) · oregano flowers · ferns · geranium leaves"

FAMILY = [
    "Fall Cake Decorating Kit · 4 oz, 25+ pieces (this listing)",
    "Small Roses & Mixed · about 12 rose blooms",
    "Small Pansy · 12 whole blooms",
    "Pansy & Orchids · 25 whole blooms",
    "Flower Petals · about 1.5 cups",
    "Squash Blossoms · 12 whole blooms",
    "Purple Orchids · 25 whole blooms",
    "Marigolds",
    "Small Mini Carnations & Bachelors",
    "Basil Blossoms · about 25 sprigs",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="Clean bright white with a warm cream #FAF7F2 wash across the bottom 15% — the one "
                   "place the autumn palette is allowed to warm the background. IDENTICAL across all 3.",
        purpose="Win the click on a seasonal search. The SEO team's CTR note is blunt: the current main "
                "image is not attractive. Ship all 3 and keep the winner.",
        visual=(
            "Mock ALL 3 options. Each: ONE callout, ONE supporting prop, product dominant. Autumn palette "
            "comes from the FLOWERS — rust roses, deep-red amaranth, green ferns and geranium leaves — "
            "never from a dark or moody background, which the brand does not do. Amazon's slot-1 main "
            "stays pure-white / product-only; these callout versions are the CTR mains you test.\n\n"

            "OPTION A — THE FINISHED CAKE (owns the outcome)\n"
            "A naked or buttercream cake, autumn-styled: a crescent of roses, amaranth sprays and fern "
            "fronds arranged across the top-right and cascading down one side. Shot slightly above on "
            "bright white, the open kit tipped in behind so the shopper connects the two.\n"
            "ONE CALLOUT (top-left badge, rust bg / white text): 'NO PIPING NEEDED'.\n"
            "Why it wins: it sells the bakery result AND the skill promise in one glance — and the "
            "skill promise is what this kit is really selling.\n\n"

            "OPTION B — THE ABUNDANCE FLAT-LAY (owns quantity)\n"
            "Overhead flat-lay of the whole kit emptied onto white and grouped by type: roses, amaranth "
            "firesticks, oregano flowers, ferns, geranium leaves — each cluster hairline-labelled. It "
            "should read as generous, because at 4 oz it genuinely is.\n"
            "ONE CALLOUT (top-right badge, green bg / white text): '25+ FLOWERS & LEAVES'.\n"
            "Why it wins: everything else in the category is a small 0.1-0.2 oz pack. Showing the pile "
            "is a value claim the competition cannot copy.\n\n"

            "OPTION C — FLOWERS *AND* GREENERY (owns the arrangement)\n"
            "Tight three-quarter shot of one rose, one amaranth spray and one fern frond being arranged "
            "together by hand on a cake edge — the moment where a scatter becomes an arrangement.\n"
            "ONE CALLOUT (top-right badge, rust bg / white text): 'FLOWERS + GREENERY'.\n"
            "Why it wins: greenery is what separates a designed cake from a sprinkled one, and no "
            "competing kit is saying it.\n\n"

            "Across all 3: product dominant, callout ~6% of frame, same lighting and colour temp."
        ),
        overlay="25+ FLOWERS & LEAVES",
        overlay_sub="A full 4 oz autumn kit: roses, amaranth, oregano flowers, ferns, geranium.",
        props=["autumn-styled cake with floral crescent", "open kit tipped behind",
               "flat-lay of the full kit grouped by type", "hand arranging rose + amaranth + fern"],
        lighting="Bright high-key daylight with a slightly warm cast, soft shadows. Identical across all 3.",
        why_it_works=(
            "Three triggers: A owns the finished cake and the no-skill promise, B owns quantity, C owns "
            "the flowers-plus-greenery arrangement idea. One idea, one prop, one badge each."
        ),
        ctr="'25+' and '4 oz' are the only real quantity claims in a category of tiny packs — and the "
            "no-piping badge speaks straight to the home baker who thinks this is beyond them.",
        cvr="Option A pre-frames the result, so the listing page opens with the cake already imagined.",
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: everything in the kit, laid out",
        role="hook",
        background="Bright white with a warm cream #FAF7F2 base band",
        purpose="Show the five components by name — the kit's contents ARE its differentiator.",
        visual=(
            f"Overhead hero flat-lay of the full kit on white, grouped into five labelled clusters: "
            f"{CONTENTS}. Each cluster gets a hairline callout with the botanical name, and one piece "
            "from each is pulled into near-macro so the real texture reads — the layered rose, the "
            "beaded amaranth spray, the tiny oregano florets, the fine fern frond, the veined geranium "
            "leaf. Keep the autumn colours HONEST: rust, wine, terracotta, moss and cream as they "
            "actually freeze-dry, never boosted."
        ),
        overlay="FIVE BOTANICALS. ONE KIT.",
        overlay_sub="Roses, amaranth, oregano flowers, ferns and geranium leaves. All edible.",
        props=["5 labelled botanical clusters", "near-macro of one piece per cluster",
               "food-grade / edible check-mark badge"],
        lighting="Soft directional daylight to reveal petal, frond and leaf texture. Clarity over drama.",
        why_it_works=(
            "'What's actually in it?' is the first question on any kit listing, and naming five real "
            "botanicals proves this is a curated set rather than a bag of assorted offcuts."
        ),
        ctr="A labelled botanical flat-lay reads as expert and stops the scroll.",
        cvr="Converts an abstract 'mixed kit' into five specific things the buyer can picture using.",
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: three cakes, three arrangements, no piping",
        role="educate",
        background="White with a soft green ribbon footer",
        purpose="Teach the buyer that they can do this — the skill objection is the real barrier here.",
        visual=(
            "A clean 3-step strip across the frame, each step a real photo of the SAME plain "
            "buttercream cake:\n"
            "  1. PLACE THE GREENERY — two fern fronds and a geranium leaf set as the base line.\n"
            "  2. ADD THE BLOOMS — three roses set along that line, largest in the middle.\n"
            "  3. FINISH WITH TEXTURE — amaranth sprays and oregano florets filling the gaps.\n"
            "Under the strip, a short note: 'No piping tips, no frosting skills — place, don't pipe.' "
            "Right edge: a small inset of the finished cake at full beauty. Keep every step visibly "
            "achievable — a shaky home-baked cake is more persuasive here than a perfect bakery one."
        ),
        overlay="PLACE, DON'T PIPE.",
        overlay_sub="Greenery first, blooms next, texture last. A styled cake in three steps.",
        props=["plain buttercream cake x3 stages", "fern + geranium base", "3 roses", "amaranth + oregano",
               "finished cake inset"],
        lighting="Bright, even, editorial daylight. Educational clarity beats mood.",
        why_it_works=(
            "The SEO bullets promise 'no piping tips or advanced frosting techniques required', and the "
            "reviews confirm buyers value exactly that. Showing the three steps turns the promise into "
            "proof and removes the 'I couldn't pull that off' objection."
        ),
        ctr="Step strips are unusually informative for this category and win the browse-stage click.",
        cvr="Removes the skill barrier — the single biggest reason a hesitant baker does not buy.",
    ),
    AIImagePlanItem(
        name="Image 4 — Desire: the autumn table",
        role="desire",
        background="Styled bright autumn table, soft natural window light",
        purpose="Sell the dream outcome — the Thanksgiving or fall-wedding dessert table.",
        visual=(
            "Hero lifestyle shot: the finished autumn cake as the centrepiece of a styled table — warm "
            "linen, a few cupcakes each wearing a rose and a fern tip, two amber cocktails garnished "
            "with oregano florets, the kit sitting open to the side. Autumn colour comes from the "
            "flowers and the linen, NOT from a dark background: the room stays bright and airy. Hands "
            "in frame setting the last bloom — this is the 'action image' the CVR notes ask for."
        ),
        overlay="AN AUTUMN SHOWSTOPPER.",
        overlay_sub="One kit styles the cake, the cupcakes and the drinks on your table.",
        props=["finished autumn cake", "cupcakes with rose + fern", "2 amber cocktails", "warm linen",
               "open kit to the side", "hands placing a bloom"],
        lighting="Soft natural window light, bright and airy with a warm cast. Never dark or moody.",
        why_it_works=(
            "Seasonal purchases are emotional and occasion-led. Showing the whole table — not just the "
            "cake — also justifies the 4 oz size: this is enough for the event, not for one dessert."
        ),
        ctr="Finished seasonal food out-performs ingredient shots in the mobile carousel.",
        cvr="Transfers the result onto the buyer's own Thanksgiving or fall event.",
    ),
    AIImagePlanItem(
        name="Image 5 — Trust: real, shelf-stable, natural, made in USA",
        role="trust",
        background="White with soft green panels behind each badge for separation",
        purpose="Stack the reassurances: real edible botanicals, nothing added, keeps, arrives protected.",
        visual=(
            "Centre: the kit packaging, clean and premium, with a small arrangement of roses, amaranth "
            "and fern beside it. Four badges in the corners:\n\n"
            "  • TOP-LEFT — REAL EDIBLE FLOWERS & LEAVES (leaf icon — food-grade, not artificial)\n"
            "  • TOP-RIGHT — SHELF-STABLE (calendar icon — order early, decorate later)\n"
            "  • BOTTOM-LEFT — 25+ PIECES · 4 OZ (scale icon — the quantity claim, repeated)\n"
            "  • BOTTOM-RIGHT — MADE IN USA (small US outline)\n\n"
            "Thin strip below, aimed at the 'broken petals' reviews: 'Delicate by nature — the kit "
            "travels cushioned, and pieces that separate still arrange beautifully.'"
        ),
        overlay="ORDER EARLY. DECORATE LATER.",
        overlay_sub="Real · 25+ pieces · shelf-stable · made in USA · nothing artificial.",
        props=["kit packaging", "small arrangement beside it", "4 corner badges", "packaging strip"],
        lighting="Bright studio-even light with a soft catch-light on the pack. Badges legible at thumbnail size.",
        why_it_works=(
            "For a seasonal kit, 'shelf-stable' is a purchase-timing argument as much as a quality one: "
            "it makes buying in September for November feel safe. The packaging line defuses the "
            "'broken flowers' review theme at the same time."
        ),
        ctr="Badge clusters read as credentials even when the text is too small to parse.",
        cvr="Removes the 'should I wait until closer to the date?' hesitation that stalls seasonal carts.",
    ),
    AIImagePlanItem(
        name="Image 6 — Honest size & coverage (4 oz · 25+ pieces)",
        role="desire",
        background="Warm cream #FAF7F2 — the autumn member of the brand's light background family",
        purpose="Show how far the kit goes. Here the size story is abundance, not apology — but it still "
                "has to be honest, because 'package size does not match expectations' is a named review "
                "theme across this brand.",
        visual=(
            "Split-frame.\n\n"
            "LEFT — HOW MUCH: the full 4 oz kit emptied into a clear glass bowl beside one 0.2 oz pack "
            "from the range, so the difference is undeniable. A single rose is shown on a fingertip and "
            "beside a US quarter for piece-scale. Caption: '4 oz · 25+ pieces — freeze-dried botanicals "
            "are feather-light, so this fills a bowl.'\n\n"
            "RIGHT — HOW FAR IT GOES: three coverage examples photographed identically — one 8-inch "
            "cake, twelve cupcakes, one dessert board — each with a small honest note on roughly how "
            "much of the kit it uses.\n\n"
            "Footer strip — HANDLING: 'Place with clean fingers or tweezers. Store sealed and dry; "
            "leftovers keep for the next occasion.'"
        ),
        overlay="4 OZ. FILLS A BOWL.",
        overlay_sub="25+ pieces. Enough for a cake, a dozen cupcakes and the drinks.",
        props=["4 oz kit in a glass bowl", "0.2 oz pack for comparison", "rose on a fingertip",
               "rose beside a US quarter", "3 coverage examples"],
        lighting="Bright, even, honest daylight — show the true volume and the true colour.",
        why_it_works=(
            "Freeze-dried botanicals weigh almost nothing, so '4 oz' means little until you see it "
            "filling a bowl next to a standard pack. Showing coverage per project makes the value "
            "concrete and pre-empts the expectation gap."
        ),
        ctr="A side-by-side against a normal-size pack is a value claim shown, not stated.",
        cvr="Justifies the kit price by making the quantity and the reach visible.",
    ),
    AIImagePlanItem(
        name="Image 7 — Close: find your flower (the variation family)",
        role="close",
        background="Bright white with a warm cream band behind the family strip",
        purpose="Close on the brand, position the kit as the seasonal entry point, and route the shopper "
                "to the single-flower listings in the family.",
        visual=(
            "Top two-thirds: brand-forward shot — the kit front and centre with roses, amaranth and fern "
            "arranged around it on bright white, the finished autumn cake softly in frame. Lower band: "
            "logo + tagline 'Real blooms. Ready when you are.'\n\n"
            "Bottom third — THE FAMILY STRIP (the variation navigator). One clean row of small "
            "identical-composition photos, each captioned with its name and count:\n"
            f"  {' · '.join(FAMILY[:6])}\n"
            "THIS listing — the Fall Cake Decorating Kit — is ringed in brand green with a small 'YOU "
            "ARE HERE' tag; the others sit un-ringed at 70% scale.\n"
            "Caption under the strip: 'The kit is the seasonal set. Single-flower packs let you restock "
            "exactly the bloom you use most.'\n"
            f"Small line at the very bottom: 'Also in the range: {' · '.join(FAMILY[6:])}.'"
        ),
        overlay="FIND YOUR FLOWER.",
        overlay_sub="Seasonal kits to start with, single-flower packs to restock.",
        props=["kit packaging", "autumn arrangement", "finished cake",
               "family strip with this listing ringed", "logo + tagline band"],
        lighting="Bright, airy, elegant daylight. Family strip evenly lit so the options compare fairly.",
        why_it_works=(
            "A kit buyer is the family's strongest repeat customer: they discover which bloom they actually "
            "reach for, then restock it single. Showing the family closes on brand and opens the second "
            "purchase in the same frame."
        ),
        ctr="Showing a range signals a real brand rather than a one-off seasonal seller.",
        cvr="Recovers the shopper who wanted one specific flower, and seeds the restock.",
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Premium Full Image: brand banner",
        role="a+_banner",
        headline="AN AUTUMN CAKE, NO PIPING.",
        body=(
            "The Freshly Preserved Fall Cake Decorating Kit brings a full 4 oz of real, freeze-dried "
            f"edible botanicals — {CONTENTS} — in rich autumn colours. Flowers and greenery together, so "
            "your cake looks arranged rather than sprinkled, with no piping tips and no advanced "
            "frosting skills. Made in the USA and shelf-stable, so you can order early and decorate on the day."
        ),
        visual=("Wide, bright editorial banner — a styled autumn table with the finished floral cake, "
                "cupcakes and the open kit, soft natural window light with a warm cast. Logo upper-left, "
                "tagline in the lower band. Desktop 1464x600, mobile 600x450 — keep cake and kit in the "
                "mobile safe area."),
        alt="Freshly Preserved Fall Cake Decorating Kit styled with an autumn floral cake on a bright table.",
    ),
    AIModule(
        name="Module 2 — Premium Carousel (5 tiles): what's in the kit",
        role="a+_carousel",
        headline="WHAT'S IN THE KIT",
        body=(
            "Tile 1: <b>ROSES</b> — The focal blooms: set them along the tier or the cake top.<br/>"
            "Tile 2: <b>AMARANTH (FIRESTICKS)</b> — Deep-red beaded sprays that add height and texture.<br/>"
            "Tile 3: <b>OREGANO FLOWERS</b> — Tiny florets that fill the gaps between the blooms.<br/>"
            "Tile 4: <b>FERNS</b> — Fine green fronds that give an arrangement its shape.<br/>"
            "Tile 5: <b>GERANIUM LEAVES</b> — Broad, veined leaves that anchor the whole design."
        ),
        visual=("5 square tiles at 220x220, same white background and lighting, one botanical per tile "
                "photographed at the same scale. Warm rust accent corner on each. Alt text per tile "
                "names the botanical and its role."),
        alt="Five-tile A+ carousel naming each botanical in the Fall Cake Decorating Kit and its role.",
    ),
    AIModule(
        name="Module 3 — Premium Full Image: place, don't pipe",
        role="a+_banner",
        headline="PLACE, DON'T PIPE.",
        body=(
            "Start with the greenery — two fern fronds and a geranium leaf set as your base line. Add "
            "the roses along that line, largest in the middle. Fill the gaps with amaranth sprays and "
            "oregano florets. That is the whole technique: no piping bag, no tips, no practice cake. "
            "The same three steps work on cupcakes, tarts, cheesecakes and dessert boards."
        ),
        visual=("Wide 3-panel how-to banner on the SAME plain buttercream cake: GREENERY → BLOOMS → "
                "TEXTURE, with the finished cake as a fourth inset at the right edge. Bright, editorial, "
                "thin rust dividers. Mobile version stacks the three steps."),
        alt="A+ banner showing the three-step method for decorating a cake with the Fall kit — no piping needed.",
    ),
    AIModule(
        name="Module 4 — Premium Full Image: fresh flowers wilt, these don't",
        role="a+_banner",
        headline="ORDER EARLY. DECORATE LATER.",
        body=(
            "Fresh flowers for an autumn event are seasonal, fragile and spoil within days — they brown "
            "and curl before the cake is even iced, and a florist run the morning of is the last thing "
            "anyone needs. These botanicals are freeze-dried and shelf-stable, so the kit can sit in "
            "your cupboard from September to Thanksgiving and still hold its colour and shape. Order "
            "early, decorate calmly, waste nothing."
        ),
        visual=("Wide banner split in two: LEFT — fresh flowers visibly browning and curling, muted. "
                "RIGHT — the kit's botanicals, intact and warm-toned, beside the sealed pack with a "
                "small calendar graphic. Clean centre divider, bright background. Never dark or moody."),
        alt="A+ banner comparing wilting fresh flowers with the shelf-stable Freshly Preserved fall kit.",
    ),
    AIModule(
        name="Module 5 — Premium Carousel (5 tiles): choose your variation",
        role="a+_carousel",
        headline="FIND YOUR FLOWER",
        body=(
            "<b>You are viewing: the Fall Cake Decorating Kit — 4 oz, 25+ flowers and leaves.</b> The kit "
            "is the seasonal set; the single-flower packs let you restock exactly the bloom you reach "
            "for most. Same real, freeze-dried, food-grade botanicals throughout.<br/><br/>"
            "Tile 1: <b>Fall Cake Decorating Kit · 4 oz</b> — Flowers and greenery, autumn palette.<br/>"
            "Tile 2: <b>Small Roses &amp; Mixed · about 12 blooms</b> — Restock the focal roses.<br/>"
            "Tile 3: <b>Small Pansy · 12 whole blooms</b> — Bright, flat faces for cupcakes.<br/>"
            "Tile 4: <b>Pansy &amp; Orchids · 25 whole blooms</b> — Event quantity, two flowers.<br/>"
            "Tile 5: <b>Flower Petals · about 1.5 cups</b> — Pure scatter and coverage.<br/><br/>"
            "Also in the Freshly Preserved range: Purple Orchids · Marigolds · Small Mini Carnations "
            "&amp; Bachelors · Squash Blossoms · Basil Blossoms."
        ),
        visual=("5 identical-composition variation tiles at 220x220 — same white background, lighting "
                "and camera height. THIS variation (Fall Cake Decorating Kit) carries a green ring and a "
                "small 'YOU ARE HERE' tag. Per-tile alt text names the variation and its count."),
        alt="Five-tile A+ carousel of the Freshly Preserved range with the Fall Cake Decorating Kit marked.",
    ),
    AIModule(
        name="Module 6 — Premium Full Image: from the brand (benefits closer)",
        role="a+_banner",
        headline="FROM FRESHLY PRESERVED",
        body=(
            "We freeze-dry our flowers and greenery whole, in the USA, so the rose that leaves us is the "
            "rose that lands on your cake — same shape, same natural autumn colour, months later. No "
            "added sugar, no dyes, no preservatives, and nothing artificial pretending to be a flower. "
            f"This kit holds <b>4 oz — 25+ pieces of {CONTENTS}</b>, enough to style a cake, a dozen "
            "cupcakes and the drinks beside them. Small kitchens, big possibilities."
        ),
        visual=("Warm benefits/brand closer: soft-focus freeze-drying trays on the left, the kit and the "
                "finished autumn cake on the right, brand-voice line across the middle. Bright and airy "
                "with a warm cast — never dark behind the logo."),
        alt="Freshly Preserved brand closing banner: freeze-dried in the USA, 25+ pieces, nothing added.",
    ),
    AIModule(
        name="Module 7 — Premium Q&A (finale)",
        role="a+_qa",
        headline="QUESTIONS BEFORE YOU BUY",
        body=(
            "<b>Q.</b> What is actually in the kit?<br/>"
            f"<b>A.</b> 4 oz, 25+ pieces: {CONTENTS}. Flowers and greenery together, which is what makes "
            "a cake look arranged rather than sprinkled.<br/><br/>"

            "<b>Q.</b> Do I need piping skills?<br/>"
            "<b>A.</b> No. There are no piping tips and no frosting techniques involved — you place the "
            "greenery first, set the blooms along it, then fill the gaps with amaranth and oregano "
            "florets. The A+ banner above shows all three steps.<br/><br/>"

            "<b>Q.</b> Are the flowers and leaves safe to eat?<br/>"
            "<b>A.</b> Yes. They are real, food-grade edible flowers and leaves, freeze-dried for use on "
            "cakes, cupcakes, desserts and drinks.<br/><br/>"

            "<b>Q.</b> How far does one kit go?<br/>"
            "<b>A.</b> Comfortably an 8-inch cake plus around a dozen cupcakes, or a cake and a dessert "
            "board. The size image shows three real coverage examples.<br/><br/>"

            "<b>Q.</b> Can I order it in September and use it in November?<br/>"
            "<b>A.</b> Yes — that is the point of freeze-drying. Kept sealed, dry and out of direct "
            "sunlight, the kit holds its colour and shape for months, so you can order early and "
            "decorate on the day.<br/><br/>"

            "<b>Q.</b> Will everything arrive intact?<br/>"
            "<b>A.</b> Freeze-dried botanicals are naturally light and delicate, so the kit travels "
            "cushioned. Handle gently; pieces that separate still arrange beautifully, and smaller "
            "florets are ideal for filling gaps.<br/><br/>"

            "<b>Q.</b> Can I use it on things other than cake?<br/>"
            "<b>A.</b> Yes — cupcakes, tarts, cheesecakes, cookies and pastries; cocktails, mocktails "
            "and warm drinks; charcuterie and grazing boards; and craft projects such as resin art."
        ),
        visual=("Vertical Q/A table, text only. Rust divider lines between questions, small green Q. and "
                "rust A. labels. Mobile-first line lengths."),
        alt="Premium Q&A module answering the most-asked questions about the Fall Cake Decorating Kit.",
    ),
]


QA = [
    AIQA(q="What is actually in the kit?",
         a=f"4 oz and 25+ pieces: {CONTENTS}. Flowers and greenery together — the greenery is what makes "
           f"a cake look arranged rather than sprinkled."),
    AIQA(q="Do I need piping skills or special tools?",
         a="No. No piping tips and no frosting techniques: place the greenery as your base line, set the "
           "roses along it, then fill the gaps with amaranth sprays and oregano florets. Clean fingers or "
           "tweezers are all you need."),
    AIQA(q="Are the flowers and leaves safe to eat?",
         a="Yes. They are real, food-grade edible flowers and leaves, freeze-dried for use on cakes, "
           "cupcakes, desserts, cocktails and plated dishes."),
    AIQA(q="How far does one kit go?",
         a="Comfortably an 8-inch cake plus around a dozen cupcakes, or a cake and a dessert board. The "
           "size image shows three real coverage examples so you can plan your table."),
    AIQA(q="Can I order early and decorate in November?",
         a="Yes — that is exactly what freeze-drying is for. Kept sealed, dry and out of direct sunlight, "
           "the kit holds its colour and shape for months."),
    AIQA(q="Will everything arrive intact?",
         a="Freeze-dried botanicals are light and delicate by nature, so the kit ships cushioned. Handle "
           "gently — pieces that separate still arrange beautifully, and the smaller florets are ideal "
           "for filling gaps between blooms."),
    AIQA(q="Will the autumn colours match the photos?",
         a="We keep our images honest to the real botanicals. Freeze-drying preserves the natural rust, "
           "wine and moss tones, though shades vary between pieces because these are real flowers and "
           "leaves rather than printed decorations."),
    AIQA(q="Do the flowers taste of anything?",
         a="They are mild. The oregano flowers carry a light herbal note; the rest are used mainly for "
           "natural colour and presentation, with no added sugar or dyes."),
    AIQA(q="Can I use it on things other than cake?",
         a="Yes — cupcakes, tarts, cheesecakes, cookies and pastries; cocktails, mocktails and warm "
           "drinks; charcuterie and grazing boards; and craft projects such as resin art."),
    AIQA(q="Would this work as a gift?",
         a="It is a natural gift for anyone who bakes: a complete seasonal set that needs no skill and "
           "no extra tools, and it keeps until they are ready to use it."),
]


def main() -> None:
    print("Loading Freshly Preserved customer + parsing listing…")
    cust = load_customer("freshly_preserved")
    brief = parse_excel(EXCEL)
    seo = load_seo(EXCEL)
    OUT = HERE / f"{PLAN_NO}_{ASIN}_Image Plan.pdf"
    print(f"  Product: {brief.product_name}  ASIN {ASIN}  Marketplace: {cust.marketplace}")
    print(f"  USPs={len(brief.usps)} KWs={len(brief.all_keywords)} Q&A={len(brief.rufus_qa)} "
          f"reviews=+{len(brief.good_reviews)}/-{len(brief.bad_reviews)}")

    builder = BriefBuilder(cust, brief, OUT, ai=None)
    builder._ai_title = seo.title
    builder._ai_bullets = as_bullets_html(seo)
    builder._ai_images = IMAGES
    builder._ai_modules = MODULES
    builder._ai_qa = QA
    builder._ai_backend = seo.backend
    builder.copy_source_label = ("SEO sheet (title/bullets/backend) + hand-written senior creative "
                                 "(overlays, A+, Q&A) — US/English")

    print("Building branded PDF…")
    pdf_path = builder.build()
    import re
    pages = len(re.findall(rb'/Type\s*/Page[^s]', pdf_path.read_bytes()))
    print(f"Built: {pdf_path}")
    print(f"  Pages: {pages}  Size: {pdf_path.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
