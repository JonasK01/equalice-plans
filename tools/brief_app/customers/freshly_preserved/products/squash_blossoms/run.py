"""Freshly Preserved — Product 06 · Freeze-Dried SQUASH BLOSSOMS 0.2 oz (12 whole blooms).

ASIN: B0CN47WW2D · Marketplace: amazon.com (USA) — English overlays + customer copy.
(This is the one product where the folder ASIN and the Overview tab agree.)

WHAT MAKES THIS ONE DIFFERENT — it is the chef's flower, and it breaks two family rules:
  1. SIZE INVERTS. Every other listing has to apologise for small blooms. Squash blossoms are
     the LARGE ones — big enough to stuff, fry, plate whole. "Smaller than expected" is not
     the objection here; the objection is the opposite, so lead with the full open trumpet
     shape and give the size reference as a boast, not a defence.
  2. IT IS SAVOURY AND SCARCE. Fresh squash blossoms are a farmers-market-only, 24-hour
     ingredient — fiori di zucca, quesadillas de flor de calabaza, chef's tasting menus. Most
     home cooks have eaten them once, in a restaurant, and have never found them to buy. That
     scarcity is the strongest hook in the entire range.

TITLE + BULLETS come 1:1 from the SEO tab (the keyword axis). Overlays / A+ / Q&A are
hand-written. Parent-child is built in at Image 7 and A+ Module 5.

Compliance guardrails (US): no best / #1 / guaranteed · no health-cure claims · no prices or
URLs on-image. Colour stays HONEST — reviewers note natural colour variation between blossoms,
so say so rather than retouching it away. Frying and rehydration are described as customer
practice, not as a promise about how the product performs.
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
PLAN_NO = "06"
ASIN = "B0CN47WW2D"

FAMILY = [
    "Squash Blossoms · 12 whole blooms (this listing)",
    "Basil Blossoms · about 25 sprigs",
    "Flower Petals · about 1.5 cups",
    "Small Roses & Mixed · about 12 rose blooms",
    "Small Pansy · 12 whole blooms",
    "Pansy & Orchids · 25 whole blooms",
    "Purple Orchids · 25 whole blooms",
    "Marigolds",
    "Small Mini Carnations & Bachelors",
    "Fall Cake Decorating Kit · 25+ flowers & leaves",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="Clean bright white with a whisper of warm cream #FAF7F2 across the bottom 15% — warm "
                   "enough for a savoury product, still unmistakably the brand's bright world. "
                   "IDENTICAL across all 3.",
        purpose="Win the click from a COOK. The SEO team's CTR note is blunt: the current main image is "
                "not attractive. Ship all 3 and keep the winner.",
        visual=(
            "Mock ALL 3 options. Each: ONE callout, ONE supporting prop, product dominant. Colour stays "
            "TRUE — squash blossoms freeze-dry to a warm golden-orange with green at the base, and they "
            "vary blossom to blossom. Reviewers already note that variation, so show it honestly rather "
            "than matching them all. Amazon's slot-1 main stays pure-white / product-only; these callout "
            "versions are the CTR mains you test.\n\n"

            "OPTION A — THE OPEN TRUMPET (owns the size — the option to beat)\n"
            "One whole blossom shot three-quarter on bright white, fully open so the trumpet shape and "
            "the golden ruffled petals fill the frame, with the remaining blossoms fanned behind and the "
            "open pack tipped in. The whole point is scale: these are big, and every competitor's "
            "edible flower is tiny.\n"
            "ONE CALLOUT (top-left badge, terracotta bg / white text): '12 WHOLE BLOSSOMS'.\n"
            "Why it wins: in a grid of confetti-sized petals, one large open blossom is a completely "
            "different silhouette.\n\n"

            "OPTION B — THE CHEF'S PLATE (owns the outcome)\n"
            "A restaurant-style plate: blossoms on a burrata or ricotta dish, one laid across a "
            "quesadilla, a bowl alongside. Bright kitchen surface, real cooking, not a dessert table.\n"
            "ONE CALLOUT (top-right badge, green bg / white text): 'STUFF. PLATE. GARNISH.'\n"
            "Why it wins: it tells a cook in one glance that this is an ingredient, not decor.\n\n"

            "OPTION C — OUT OF SEASON, IN YOUR PANTRY (owns the scarcity)\n"
            "Split: LEFT a farmers-market crate of fresh squash blossoms, visibly wilting and collapsing "
            "at the edges; RIGHT the preserved blossoms, intact and open, in the sealed pack. Thin "
            "divider.\n"
            "ONE CALLOUT (top-right badge, terracotta bg / white text): 'IN SEASON, ALL YEAR'.\n"
            "Why it wins: anyone who has looked for squash blossoms knows they last a day and vanish "
            "after summer.\n\n"

            "Across all 3: product dominant, callout ~6% of frame, same lighting and colour temp."
        ),
        overlay="12 WHOLE BLOSSOMS",
        overlay_sub="Large, open squash blossoms, freeze-dried whole. Ready any month.",
        props=["one fully open blossom, three-quarter view", "fan of remaining blossoms", "tipped pack",
               "chef's plate with blossoms", "wilting market crate vs sealed pack"],
        lighting="Bright high-key daylight with a slightly warm cast, soft shadows. Identical across all 3.",
        why_it_works=(
            "Three triggers: A owns the unusual size and silhouette, B claims the savoury cook, C owns "
            "the scarcity that makes this ingredient worth stocking. One idea, one prop, one badge each."
        ),
        ctr="A large open blossom is a different shape from everything else in the search grid — the "
            "single cheapest way to break the pattern.",
        cvr="Sets the right expectation from frame one: a cooking ingredient, not a cake sprinkle.",
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: the flower most people can't buy fresh",
        role="hook",
        background="Warm cream #FAF7F2 on white — savoury but still bright and airy",
        purpose="Land the scarcity hook: this is a restaurant ingredient that home cooks can rarely source.",
        visual=(
            "Macro three-quarter of one whole blossom, lit so the fine ribbing of the petals, the "
            "translucent golden edges and the green base read clearly — a real flower with real "
            "structure, not a flat dried petal. Beside it, a small honest note: 'Fresh squash blossoms "
            "last about a day and appear for a few summer weeks.' Small 'FOOD-GRADE · EDIBLE' leaf "
            "check-mark badge.\n"
            "Do NOT retouch the blossoms to identical colour — natural variation is real, and pretending "
            "otherwise is the review complaint waiting to happen."
        ),
        overlay="THE CHEF'S FLOWER.",
        overlay_sub="Fresh squash blossoms last a day. These wait in your pantry.",
        props=["macro whole blossom", "scarcity note", "food-grade / edible check-mark badge"],
        lighting="Soft directional daylight to reveal petal ribbing and the translucent edge.",
        why_it_works=(
            "Most buyers have eaten squash blossoms once, in a restaurant, and never found them to buy. "
            "Naming that scarcity turns an unfamiliar product into an opportunity they did not know "
            "they had."
        ),
        ctr="A large golden blossom in macro is visually unusual and stops the scroll.",
        cvr="Converts curiosity into urgency without any urgency language.",
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: what a cook does with twelve blossoms",
        role="educate",
        background="White with a soft green ribbon footer",
        purpose="Show the savoury range — the CVR note asks for clear contents, usage and function.",
        visual=(
            "Left third: the open pack with the 12 whole blossoms neatly grouped, small label '12 whole "
            "squash blossoms · 0.2 oz'. Right two-thirds: a clean 4-tile 'WAYS TO USE' grid, each tile a "
            "small real photo —\n"
            "  • PLATE THEM WHOLE (blossoms on burrata, ricotta or a soup)\n"
            "  • STUFF THEM (a blossom being filled with soft cheese — the classic fiori di zucca)\n"
            "  • BOARDS & APPETISERS (blossoms across charcuterie, tostadas, quesadillas)\n"
            "  • DRINKS & DESSERT STYLING (a blossom on a cocktail rim, one on a pastry)\n"
            "Thin green connectors tie the pack to the four uses. Under the stuffing tile, a small "
            "honest note: 'Many cooks rehydrate briefly before stuffing or frying.'"
        ),
        overlay="PLATE, STUFF, GARNISH.",
        overlay_sub="Twelve whole blossoms. Big enough to fill, elegant enough to plate.",
        props=["open pack of 12 blossoms", "4 use-case tiles", "green connector lines"],
        lighting="Bright, even, editorial daylight. Educational clarity beats mood.",
        why_it_works=(
            "Squash blossoms are unfamiliar to most Amazon shoppers, so the plan has to teach before it "
            "sells. Four concrete uses — with the classic stuffed preparation named — give a hesitant "
            "buyer permission to try."
        ),
        ctr="Grid layouts read as informative at thumbnail size and win the browse-stage click.",
        cvr="Removes the 'I wouldn't know what to do with them' objection, which is the real blocker here.",
    ),
    AIImagePlanItem(
        name="Image 4 — Desire: the restaurant plate at home",
        role="desire",
        background="Bright kitchen or dining surface, soft natural window light",
        purpose="Sell the dream outcome — a plate that looks like a tasting menu course.",
        visual=(
            "Hero lifestyle shot, deliberately SAVOURY: a ricotta and honey crostini or a burrata plate "
            "finished with two open squash blossoms, hands mid-placement. In soft focus behind: a "
            "quesadilla with a blossom laid across it and a bowl of soup with one floating. Bright "
            "linen, a good knife, the pack sitting naturally to the side. This is the 'action image' the "
            "CVR notes ask for — and it must read as dinner, not dessert."
        ),
        overlay="A TASTING-MENU FINISH.",
        overlay_sub="The blossom that makes a home plate look like a restaurant course.",
        props=["burrata or ricotta plate with 2 blossoms", "hands placing a blossom", "quesadilla",
               "bowl of soup with a floating blossom", "bright linen", "pack to the side"],
        lighting="Soft natural window light, bright and airy with a warm cast. Aspirational food styling.",
        why_it_works=(
            "The payoff for this buyer is status at their own table. Showing the gesture and the result "
            "together makes a restaurant-grade plate feel one blossom away."
        ),
        ctr="Restaurant-grade savoury plating is rare in this category's carousel and pulls the click.",
        cvr="Transfers the result onto the buyer's own cooking — the emotional close.",
    ),
    AIImagePlanItem(
        name="Image 5 — Trust: real, shelf-stable, natural, made in USA",
        role="trust",
        background="White with soft green panels behind each badge for separation",
        purpose="Stack the reassurances: real food-grade blossoms, nothing added, keeps, arrives protected.",
        visual=(
            "Centre: the resealable pack, clean and premium, two intact open blossoms beside it. Four "
            "badges in the corners:\n\n"
            "  • TOP-LEFT — REAL EDIBLE BLOSSOMS (leaf icon — food-grade, not artificial)\n"
            "  • TOP-RIGHT — SHELF-STABLE (calendar icon — no refrigeration, ready out of season)\n"
            "  • BOTTOM-LEFT — 12 WHOLE BLOOMS (the count, repeated where it reassures)\n"
            "  • BOTTOM-RIGHT — MADE IN USA (small US outline)\n\n"
            "Thin strip below, aimed at the 'crushed blossoms' reviews: 'Large and delicate by nature — "
            "blossoms travel cushioned in a protective resealable pack, and colour varies naturally from "
            "blossom to blossom.'"
        ),
        overlay="OUT OF SEASON. IN STOCK.",
        overlay_sub="Real · 12 whole blooms · shelf-stable, no refrigeration · made in USA.",
        props=["resealable pack", "2 intact open blossoms", "4 corner badges", "packaging strip"],
        lighting="Bright studio-even light with a soft catch-light on the pack. Badges legible at thumbnail size.",
        why_it_works=(
            "Two named review themes get answered in one frame: 'crushed on arrival' by the protective "
            "pack line, and 'colours differ from expectations' by saying plainly that natural variation "
            "is what real blossoms do."
        ),
        ctr="Badge clusters read as credentials even when the text is too small to parse.",
        cvr="Pre-empts both of this listing's recurring complaints before the shopper reaches the reviews.",
    ),
    AIImagePlanItem(
        name="Image 6 — Size & count, as a boast (12 whole blooms · 0.2 oz)",
        role="desire",
        background="Warm cream #FAF7F2 — same family as Image 2 for visual rhythm",
        purpose="Show the scale. Uniquely in this range the size is a selling point, so present it as "
                "one — while still being honest about count and weight.",
        visual=(
            "Split-frame.\n\n"
            "LEFT — HOW BIG: one open blossom held in a flat palm, filling most of it, and the same "
            "blossom beside a US quarter — the coin should look small next to it. Caption: 'Large, open "
            "blossoms — big enough to stuff, plate or fill.'\n\n"
            "RIGHT — WHAT YOU GET: all 12 blossoms laid out in a neat flat-lay grid beside the pack, "
            "label '12 whole blossoms · 0.2 oz', with visible natural colour variation left in. A small "
            "honest note: 'Freeze-dried blossoms are feather-light — 0.2 oz is twelve full blooms.'\n\n"
            "Footer strip — HANDLING: 'Delicate by nature — handle gently, and many cooks rehydrate "
            "briefly before stuffing or frying. Store sealed and dry.'"
        ),
        overlay="BIG ENOUGH TO STUFF.",
        overlay_sub="12 large, open blooms. Not petals, not confetti.",
        props=["blossom in a flat palm", "blossom beside a US quarter", "flat-lay of all 12 blossoms",
               "pack for scale"],
        lighting="Bright, even, honest daylight — show the true size and the true colour variation.",
        why_it_works=(
            "The rest of the family fights 'smaller than expected'; this product wins on the opposite "
            "fact. Showing a blossom dwarfing a coin turns the family's weakest slot into this "
            "listing's strongest one, while the honest count still protects against returns."
        ),
        ctr="A flower that makes a US quarter look small is an unusual, memorable frame.",
        cvr="Confirms the ingredient is substantial enough for real cooking, which justifies the price.",
    ),
    AIImagePlanItem(
        name="Image 7 — Close: find your flower (the variation family)",
        role="close",
        background="Bright white with a warm cream band behind the family strip",
        purpose="Close on the brand and route the shopper across the family — squash and basil are the "
                "savoury door into a mostly sweet range.",
        visual=(
            "Top two-thirds: brand-forward shot — the Freshly Preserved pack front and centre with open "
            "blossoms arranged around it on bright white, the burrata plate softly in frame. Lower band: "
            "logo + tagline 'Real blooms. Ready when you are.'\n\n"
            "Bottom third — THE FAMILY STRIP (the variation navigator). One clean row of small "
            "identical-composition photos, each captioned with its name and count:\n"
            f"  {' · '.join(FAMILY[:6])}\n"
            "THIS listing — Squash Blossoms — is ringed in brand green with a small 'YOU ARE HERE' tag; "
            "the others sit un-ringed at 70% scale.\n"
            "Caption under the strip: 'Squash and basil blossoms cook. Pansies, orchids and roses "
            "decorate. Same freeze-drying, different job.'\n"
            f"Small line at the very bottom: 'Also in the range: {' · '.join(FAMILY[6:])}.'"
        ),
        overlay="FIND YOUR FLOWER.",
        overlay_sub="Savoury blossoms to cook with, sweet blooms to decorate. One family.",
        props=["Freshly Preserved pack", "open squash blossoms", "burrata plate",
               "family strip with this listing ringed", "logo + tagline band"],
        lighting="Bright, airy, elegant daylight. Family strip evenly lit so the variations compare fairly.",
        why_it_works=(
            "Squash blossoms bring in an adventurous cook who did not know the brand existed. Splitting "
            "the family into 'cook with' and 'decorate with' gives that shopper an immediate second reason "
            "to come back."
        ),
        ctr="Showing a range signals a real brand rather than a one-off seasonal seller.",
        cvr="Opens a whole second category to a buyer who arrived for one ingredient.",
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Premium Full Image: brand banner",
        role="a+_banner",
        headline="THE CHEF'S FLOWER, IN STOCK.",
        body=(
            "Fresh squash blossoms appear for a few summer weeks, last about a day, and rarely make it "
            "to a shop at all. Freshly Preserved Freeze-Dried Squash Blossoms give you twelve whole, "
            "open blooms that keep their shape, delicate texture and mild squash flavour — ready to "
            "plate, stuff or garnish in any month. Food-grade, made in the USA, and shelf-stable with no "
            "refrigeration."
        ),
        visual=("Wide, bright editorial banner — a kitchen surface, not a dessert table: a burrata plate "
                "finished with open blossoms, a quesadilla, the resealable pack, soft natural window "
                "light with a warm cast. Logo upper-left, tagline in the lower band. Desktop 1464x600, "
                "mobile 600x450 — keep the plate and pack in the mobile safe area."),
        alt="Freshly Preserved freeze-dried squash blossoms on a savoury burrata plate in a bright kitchen.",
    ),
    AIModule(
        name="Module 2 — Premium Carousel (5 tiles): why squash blossoms",
        role="a+_carousel",
        headline="WHY SQUASH BLOSSOMS",
        body=(
            "Tile 1: <b>LARGE, WHOLE BLOOMS</b> — Big enough to stuff, plate or fill — not petals.<br/>"
            "Tile 2: <b>SAVOURY, NOT SWEET</b> — A mild squash flavour that suits real cooking.<br/>"
            "Tile 3: <b>A ONE-DAY INGREDIENT, KEPT</b> — Fresh blossoms wilt overnight; these do not.<br/>"
            "Tile 4: <b>SHELF-STABLE</b> — No refrigeration; ready in February as well as July.<br/>"
            "Tile 5: <b>MADE IN USA · FOOD-GRADE</b> — Real blossoms, nothing artificial added."
        ),
        visual=("5 square tiles at 220x220, terracotta accent corner on each, consistent bright styling. "
                "Icons: open blossom · pan · clock · calendar · US leaf. Alt text per tile."),
        alt="Five-tile A+ carousel: large whole blooms, savoury, seasonal ingredient kept, shelf-stable, USA made.",
    ),
    AIModule(
        name="Module 3 — Premium Full Image: ways to use them",
        role="a+_banner",
        headline="PLATE, STUFF, GARNISH.",
        body=(
            "Lay a whole blossom over burrata, ricotta, soup or risotto and the plate changes character. "
            "Fill them with soft cheese for the classic fiori di zucca. Set one across a quesadilla, a "
            "tostada or a charcuterie board. Float one on a cocktail, or use one to finish a pastry. "
            "Twelve blossoms go further than they look, because each one is a centrepiece rather than a "
            "sprinkle. Many cooks rehydrate them briefly before stuffing or frying."
        ),
        visual=("Wide 4-panel banner: PLATE WHOLE → STUFF (blossom being filled with soft cheese) → "
                "BOARDS & APPETISERS → DRINKS & PASTRY. Bright, editorial, thin terracotta dividers. "
                "Mobile keeps 2 panels stacked, savoury first."),
        alt="A+ banner showing four ways to use Freshly Preserved freeze-dried squash blossoms.",
    ),
    AIModule(
        name="Module 4 — Premium Full Image: a one-day ingredient, kept",
        role="a+_banner",
        headline="FRESH ONES LAST A DAY.",
        body=(
            "Squash blossoms are picked at dawn and collapse by evening, which is why they live at "
            "farmers' markets for a few summer weeks and almost never on a shelf. Freeze-drying catches "
            "them fully open and holds the shape, the delicate texture and the mild squash flavour — "
            "sealed, shelf-stable, no refrigeration. Cook the summer ingredient in the middle of winter, "
            "on a Tuesday, without planning ahead."
        ),
        visual=("Wide banner split in two: LEFT — a market crate of fresh blossoms visibly wilting and "
                "collapsing, muted. RIGHT — the preserved blossoms, open and golden, beside the sealed "
                "pack with a small calendar graphic. Clean centre divider, bright background. Never dark."),
        alt="A+ banner comparing wilting fresh squash blossoms with shelf-stable freeze-dried blossoms.",
    ),
    AIModule(
        name="Module 5 — Premium Carousel (5 tiles): choose your variation",
        role="a+_carousel",
        headline="FIND YOUR FLOWER",
        body=(
            "<b>You are viewing: Squash Blossoms — 12 whole blooms (0.2 oz).</b> Some blooms in this "
            "family are for cooking, some are for decorating. Same freeze-drying, different job — pick "
            "the one your recipe needs.<br/><br/>"
            "Tile 1: <b>Squash Blossoms · 12 whole blooms</b> — Large savoury blooms: plate, stuff, fill.<br/>"
            "Tile 2: <b>Basil Blossoms · about 25 sprigs</b> — Savoury herb: rubs, sauces, salads, tea.<br/>"
            "Tile 3: <b>Flower Petals · about 1.5 cups</b> — Colour to scatter across cakes and boards.<br/>"
            "Tile 4: <b>Small Roses &amp; Mixed · about 12 blooms</b> — Romance for cakes and drinks.<br/>"
            "Tile 5: <b>Small Pansy · 12 whole blooms</b> — Bright, flat faces for cupcakes.<br/><br/>"
            "Also in the Freshly Preserved range: Small Orchid · Pansy &amp; Orchids · Purple Orchids · "
            "Marigolds · Small Mini Carnations &amp; Bachelors · the Fall Cake Decorating Kit."
        ),
        visual=("5 identical-composition variation tiles at 220x220 — same white background, lighting "
                "and camera height, so the sizes compare honestly (the squash blossom will visibly be "
                "the largest, which is the point). THIS variation carries a green ring and a small 'YOU "
                "ARE HERE' tag. Per-tile alt text names the variation and its use."),
        alt="Five-tile A+ carousel of the Freshly Preserved range with the squash blossoms marked.",
    ),
    AIModule(
        name="Module 6 — Premium Full Image: from the brand (benefits closer)",
        role="a+_banner",
        headline="FROM FRESHLY PRESERVED",
        body=(
            "We freeze-dry our blossoms whole, in the USA, while they are fully open — so the blossom "
            "that leaves us still has its trumpet shape, its delicate texture and its mild squash "
            "flavour months later. Nothing artificial, nothing pretending to be a flower, and natural "
            "colour variation left exactly as it comes. This pack holds <b>12 whole squash blossoms "
            "(0.2 oz)</b> in a resealable pack that needs no refrigeration. Small kitchens, big "
            "possibilities."
        ),
        visual=("Warm benefits/brand closer: soft-focus growing field or freeze-drying trays on the "
                "left, the resealable pack and a finished savoury plate on the right, brand-voice line "
                "across the middle. Bright and airy — never dark behind the logo."),
        alt="Freshly Preserved brand closing banner: squash blossoms freeze-dried whole in the USA.",
    ),
    AIModule(
        name="Module 7 — Premium Q&A (finale)",
        role="a+_qa",
        headline="QUESTIONS BEFORE YOU BUY",
        body=(
            "<b>Q.</b> How big are they?<br/>"
            "<b>A.</b> These are large, open blossoms — a single one fills a palm and dwarfs a US "
            "quarter. Big enough to stuff, plate whole or lay across a dish, which is what separates "
            "them from petals and small blooms.<br/><br/>"

            "<b>Q.</b> What do they taste like?<br/>"
            "<b>A.</b> Mild and lightly squash-like — subtle enough to complement a dish rather than "
            "take it over, which is why they work on burrata, soup, quesadillas and cocktails.<br/><br/>"

            "<b>Q.</b> Can I stuff or fry them like fresh ones?<br/>"
            "<b>A.</b> Many cooks rehydrate them briefly first, then handle them as they would fresh "
            "blossoms. Used dry, they are excellent laid whole over a finished plate or a board.<br/><br/>"

            "<b>Q.</b> Can I use them in cocktails?<br/>"
            "<b>A.</b> Yes. Place a blossom on the rim, float it on top, or use it as a garnish — the "
            "mild flavour complements a drink without overpowering it.<br/><br/>"

            "<b>Q.</b> How do I store them? Do they need refrigeration?<br/>"
            "<b>A.</b> No refrigeration. Keep them sealed in their pack at room temperature, "
            "out of direct sunlight and away from extreme heat, and they stay ready whenever you "
            "cook.<br/><br/>"

            "<b>Q.</b> Why do the blossoms look slightly different from each other?<br/>"
            "<b>A.</b> Because they are real flowers. Colour and size vary naturally from blossom to "
            "blossom, and we keep our photography honest to that rather than matching them "
            "artificially.<br/><br/>"

            "<b>Q.</b> Will they arrive intact?<br/>"
            "<b>A.</b> Freeze-dried blossoms are large and delicate, so they travel cushioned in a "
            "protective resealable pack. Handle gently — a blossom that splits is still perfect laid "
            "over a plate or torn across a board."
        ),
        visual=("Vertical Q/A table, text only. Terracotta divider lines between questions, small green "
                "Q. and terracotta A. labels. Mobile-first line lengths."),
        alt="Premium Q&A module answering the most-asked questions about freeze-dried squash blossoms.",
    ),
]


QA = [
    AIQA(q="How big are they?",
         a="Large, open blossoms — one fills a palm and makes a US quarter look small. Big enough to "
           "stuff, plate whole or lay across a dish, which is what separates them from petals and the "
           "small decorative blooms."),
    AIQA(q="What do they taste like?",
         a="Mild and lightly squash-like — subtle enough to complement a dish rather than take it over, "
           "which is why they suit burrata, soup, quesadillas, boards and cocktails."),
    AIQA(q="Can I stuff or fry them like fresh blossoms?",
         a="Many cooks rehydrate them briefly first and then handle them as they would fresh blossoms. "
           "Used dry, they are excellent laid whole over a finished plate, a board or a bowl of soup."),
    AIQA(q="Can I use them in cocktails?",
         a="Yes. Place one on the rim, float it on top, or use it as a garnish — the mild flavour "
           "complements a drink without overpowering it."),
    AIQA(q="How do I store them? Do they need refrigeration?",
         a="No refrigeration needed. Keep them sealed in their pack at room temperature, out "
           "of direct sunlight and away from extreme heat, and they are ready whenever you cook."),
    AIQA(q="Why do the blossoms look slightly different from each other?",
         a="Because they are real flowers. Colour and size vary naturally from blossom to blossom, and "
           "we keep our photography honest to that rather than matching them artificially."),
    AIQA(q="Will they arrive intact?",
         a="Freeze-dried blossoms are large and delicate, so they ship cushioned in a protective "
           "resealable pack. Handle gently — a blossom that splits is still perfect laid over a plate or "
           "torn across a board."),
    AIQA(q="What can I use them for?",
         a="Plating burrata, ricotta, soups and risotto; stuffing with soft cheese; quesadillas, tostadas "
           "and appetisers; charcuterie and grazing boards; cocktail garnish; and pastry or cake "
           "styling where a large bloom is wanted."),
    AIQA(q="Are these the same as your decorative flowers?",
         a="Same freeze-drying, different job. Squash and basil blossoms are for cooking; pansies, "
           "orchids, roses and the petal mix are for decorating cakes, desserts and drinks."),
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
