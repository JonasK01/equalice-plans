"""The Death Deck — Product 01 · Conversation Card Game, 112 question cards.

ASIN: B07GSRDL6H · Marketplace: amazon.com (USA) — English overlays + customer copy.
Brand onboarded 08.08.26. First plan for this client.

THE CENTRAL CREATIVE PROBLEM — everything below is built around it:
The word "Death" in the title is the best hook in the category AND the biggest objection.
It stops the scroll, then instantly triggers "this will be morbid / depressing / for people
who are dying". The client named the fix themselves: modern, warm, optimistic, inviting —
never dark or clinical — and the reaction they want is "I could actually do this with my
family." So the plan leads with LAUGHTER and PEOPLE. The topic is the surprise, never the
threat. The skull is a friendly graphic mark, never a horror cue.

THE MOAT: created by a HOSPICE SOCIAL WORKER. No competing conversation-card game has a
credential like it, and it is what turns a novelty deck into a tool. It carries Image 5 and
A+ Module 4.

THE EXPECTATION TRAP: reviews split BOTH ways — some say "not as deep as I expected", others
find it more intense than they wanted. One fix answers both: show REAL sample cards, a funny
one and a searching one, so buyers self-calibrate before they buy (Image 6).

TITLE + BULLETS come 1:1 from the SEO tab (the keyword axis). Overlays / A+ / Q&A are
hand-written.

Compliance guardrails (US): no best / #1 / guaranteed · NO medical, grief-therapy or
end-of-life-advice claims — this is a conversation game, never treatment or counselling ·
no prices or URLs on-image · age rating 13+ stated honestly, never softened.
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
PLAN_NO = "01"
ASIN = "B07GSRDL6H"

# The spec badges buyers scan for. Same set, same order, every time they appear.
SPECS = "112 CARDS · 2-10 PLAYERS · AGES 13+ · 30-90 MIN"


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="Clean bright white with a soft periwinkle #EFF1F7 wash across the bottom 15% for "
                   "grounding. IDENTICAL across all 3 options so the split test isolates composition.",
        purpose=("Win the click AND survive the word 'Death'. The SEO team's CTR note is blunt: the "
                 "current main image is not attractive. Ship all 3 and keep the winner via Amazon "
                 "Manage Your Experiments."),
        visual=(
            "Mock ALL 3 options. Each: ONE callout, ONE supporting prop, product dominant. NOTHING dark, "
            "gothic, clinical or funereal in any of them — that is the brand's hard no-go and also the "
            "commercial risk. Amazon's slot-1 main stays pure-white / product-only; these callout "
            "versions are the CTR mains you A/B test against a clean white main.\n\n"

            "OPTION A — THE LAUGH (owns the reframe — the option to beat)\n"
            "Three or four friends around a bright kitchen table, mid-laugh, cards in hand, one person "
            "reading aloud. Warm daylight, white space above them for the callout. The box sits in the "
            "foreground, clearly readable. The whole frame has to say 'good night in' before the shopper "
            "has finished reading the word Death.\n"
            "ONE CALLOUT (top-left badge, magenta #A650A2 bg / white text): '112 QUESTIONS. REAL LAUGHS.'\n"
            "Why it wins: it contradicts the expectation the title creates, in the half-second before "
            "the shopper decides this is not for them.\n\n"

            "OPTION B — THE DECK, FANNED (owns the substance)\n"
            "The box standing, with the 112 cards fanned in a wide arc beside it on bright white — two "
            "cards pulled forward and fully readable, one light-hearted and one searching. Clean spec "
            f"strip along the bottom: {SPECS}.\n"
            "ONE CALLOUT (top-right badge, periwinkle #6470A5 bg / white text): '112 CARDS'.\n"
            "Why it wins: 'not worth the price' is a live review theme. Showing the actual card count "
            "and real questions makes the box read as substantial before anyone checks the price.\n\n"

            "OPTION C — THE CREDENTIAL (owns the trust)\n"
            "The box centred on bright white, cards fanned behind it, with a single clean line of type "
            "beside it: 'Created by a hospice social worker.' One warm portrait-style illustration or a "
            "small real photo of the creator, playful not solemn.\n"
            "ONE CALLOUT (top-right badge, navy #272C3F bg / white text): 'BY A HOSPICE SOCIAL WORKER'.\n"
            "Why it wins: it answers 'is this tasteful or is it a gimmick?' instantly, and no competitor "
            "in the conversation-card category can make the same claim.\n\n"

            "Across all 3: product dominant, callout ~6% of frame, same lighting and colour temp."
        ),
        overlay="112 QUESTIONS. REAL LAUGHS.",
        overlay_sub="The conversation everyone avoids, turned into a genuinely good evening.",
        props=["OPTION A: friends laughing around a bright table, cards in hand, box in foreground",
               "OPTION B: box + 112 cards fanned, 2 cards readable, spec strip",
               "OPTION C: box + cards + 'created by a hospice social worker' line"],
        lighting="Bright, warm natural daylight. Soft shadows, airy, optimistic. Never moody or low-key.",
        why_it_works=(
            "Three different jobs: A reframes the topic before it repels, B proves the box is worth the "
            "money, C establishes authority. One idea, one prop, one badge each — legible at mobile "
            "thumbnail size."
        ),
        ctr=("The category's thumbnails are all boxes on white. A frame full of people mid-laugh is a "
             "different silhouette, and it neutralises the flinch the brand name causes."),
        cvr="Option A pre-frames the whole listing as warm, so every image after it is read that way.",
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: not the evening you're expecting",
        role="hook",
        background="Soft periwinkle #EFF1F7 — bright, friendly, never sombre",
        purpose="Kill the morbid assumption outright, in one frame, before it costs the sale.",
        visual=(
            "A tight, candid two-shot: two people leaning toward each other over a table, one holding a "
            "card, both genuinely laughing — the kind of laugh that happens right after someone says "
            "something unexpectedly honest. Cards scattered loosely between them. Warm daylight, lots of "
            "white space to the left for the overlay.\n\n"
            "Small playful illustrated accents in the brand palette — magenta circles, apricot dots, "
            "periwinkle plus signs — scattered at low opacity, exactly as the brand uses them. The "
            "friendly skull mark may appear small and graphic; never rendered realistically.\n\n"
            "NOTHING dark, no candles, no black, no memorial cues anywhere in frame."
        ),
        overlay="NOT THE EVENING YOU EXPECT",
        overlay_sub="It's about death. It's also the most fun you've had talking about anything.",
        props=["two people mid-laugh over cards", "loose scattered cards", "playful brand-palette accents"],
        lighting="Warm natural daylight, high-key. Candid rather than posed.",
        why_it_works=(
            "The single biggest reason someone does not buy this game is that they assume how it will "
            "feel. A real laugh is the fastest possible rebuttal, and it costs the shopper nothing to "
            "believe."
        ),
        ctr="Genuine human emotion out-performs product shots in the carousel at every stage.",
        cvr="Removes the 'this will be depressing' objection before the shopper reaches the reviews.",
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: everything in the box",
        role="educate",
        background="White with a soft periwinkle ribbon footer",
        purpose="Show the contents and the specs — the CVR note asks for clear contents, usage and function.",
        visual=(
            "Clean overhead flat-lay of the complete contents on white, each element hairline-labelled:\n"
            "  • The 112 cards, fanned in two clear groups — MULTIPLE-CHOICE and OPEN-ENDED — so the "
            "two question formats are visible as a feature, not buried in the copy\n"
            "  • The instruction booklet, open to the ways-to-play page\n"
            "  • The sample scorecard\n"
            "  • The box itself, closed, showing the front\n\n"
            f"Spec badge row across the bottom in the brand palette: {SPECS}. Use the client's own icon "
            "roles — periwinkle plus signs and age icon, apricot dots for the 30-minute mark, magenta "
            "circles as the side graphics."
        ),
        overlay="112 CARDS, TWO QUESTION TYPES",
        overlay_sub="Multiple-choice and open-ended, plus the booklet and a sample scorecard.",
        props=["112 cards fanned in 2 labelled groups", "instruction booklet open", "sample scorecard",
               "closed box", "spec badge row"],
        lighting="Bright, even, editorial daylight. Educational clarity beats mood.",
        why_it_works=(
            "'Not worth the price' is a named review theme. Laying out every component with the card "
            "count, both question formats, the booklet and the scorecard makes the value visible instead "
            "of asserted."
        ),
        ctr="Flat-lays of full contents read as informative at thumbnail size.",
        cvr="Directly answers 'what do I actually get for my money?' — the top objection on this listing.",
    ),
    AIImagePlanItem(
        name="Image 4 — Desire: the night that runs long",
        role="desire",
        background="Warm home setting, soft natural window light",
        purpose="Sell the outcome the buyer actually wants — connection, not a card game.",
        visual=(
            "The action image the CVR notes ask for. Three generations around a table after dinner — a "
            "grandparent mid-story, an adult child listening properly, a teenager who has stopped "
            "looking at their phone. Plates pushed aside, cards in the middle, someone holding one up. "
            "Warm and bright, lived-in, genuinely happy.\n\n"
            "Small caption strip, low in frame: 'Works for 2 to 10 — couples, friends, family, or the "
            "whole table.'\n\n"
            "Shoot or source an ALTERNATE of this same scene with a couple on a sofa, so the design team "
            "has both the family and the date-night version. Bright and warm in both. No grief, no "
            "tears, no soft-focus sentimentality — that is an explicit brand no-go."
        ),
        overlay="DINNER RUNS LATE.",
        overlay_sub="The questions people never get around to asking each other. Finally asked.",
        props=["three generations at a table", "plates pushed aside", "cards in the middle",
               "someone reading a card aloud", "alt version: couple on a sofa"],
        lighting="Warm natural window light, bright and optimistic. Candid, never staged-solemn.",
        why_it_works=(
            "Nobody buys a card game; they buy the evening it creates. Showing three generations also "
            "quietly answers 'who is this even for?' and makes the gift use-case obvious."
        ),
        ctr="Multigenerational warmth is rare in the party-game category and stands out in the strip.",
        cvr="Transfers the outcome onto the buyer's own family — the emotional close.",
    ),
    AIImagePlanItem(
        name="Image 5 — Trust: created by a hospice social worker",
        role="trust",
        background="White with soft periwinkle panels behind each supporting element",
        purpose="Establish authority. This is the brand's strongest asset and no competitor has it.",
        visual=(
            "Centre-left: a warm, human portrait of the creator — or a friendly illustrated stand-in if "
            "no photo is licensed — with a short line of type: 'Created by a hospice social worker who "
            "watched too many families have this conversation too late.'\n\n"
            "Centre-right: the box and a small fan of cards.\n\n"
            "Three supporting badges beneath, in the brand palette:\n"
            "  • WRITTEN FROM REAL EXPERIENCE (navy)\n"
            "  • QUESTIONS THAT GO SOMEWHERE (magenta)\n"
            "  • AGES 13+ · ANSWER AT YOUR OWN LEVEL (periwinkle)\n\n"
            "That third badge is doing quiet, important work: it tells a nervous buyer that nobody gets "
            "forced into a topic they are not ready for. Keep the whole frame bright and optimistic — a "
            "credential, not a memorial."
        ),
        overlay="BY A HOSPICE SOCIAL WORKER",
        overlay_sub="Written by someone who has sat with families for the conversation that came too late.",
        props=["creator portrait or friendly illustrated stand-in", "box + small card fan",
               "3 brand-palette badges"],
        lighting="Bright, warm, human. Studio-even on the product side, natural on the portrait side.",
        why_it_works=(
            "It converts the product from a novelty deck into a tool with a reason to exist. It also "
            "answers the unspoken question behind every hesitation here — 'is this tasteful, or is "
            "someone making a joke out of dying?'"
        ),
        ctr="A human face plus a real credential reads as legitimate at a glance.",
        cvr="The strongest single trust lever on the listing, and completely un-copyable by competitors.",
    ),
    AIImagePlanItem(
        name="Image 6 — Read the actual cards (calibrate expectations)",
        role="desire",
        background="Soft periwinkle #EFF1F7 — same family as Image 2 for visual rhythm",
        purpose=("Fix BOTH halves of the expectation gap: reviewers who wanted more depth and reviewers "
                 "who found it more intense than they bargained for."),
        visual=(
            "Six real cards from the deck, shown large and fully readable, arranged in two clearly "
            "labelled rows:\n\n"
            "  ROW 1 — MULTIPLE-CHOICE (the easy way in): three cards with lighter, funnier prompts. "
            "These prove the game is playable at a party and that nobody has to make a speech.\n\n"
            "  ROW 2 — OPEN-ENDED (the ones people remember): three cards with genuinely searching "
            "prompts about how you want to be remembered, what you would want at the end, what you have "
            "never said.\n\n"
            "Small line beneath: 'Both kinds are in the box. Play the level your table is ready for.'\n\n"
            "IMPORTANT: use REAL card text supplied by the client — do not invent prompts. Ask the "
            "client to pick the six; they know which land best."
        ),
        overlay="READ THE ACTUAL CARDS.",
        overlay_sub="Funny ones and searching ones. You choose how deep the table goes.",
        props=["3 multiple-choice cards, readable", "3 open-ended cards, readable", "row labels"],
        lighting="Bright, even, honest daylight — card text must be crisply legible at thumbnail size.",
        why_it_works=(
            "The two loudest complaints on this listing point in opposite directions: not deep enough, "
            "and too intense. Both are expectation gaps, and both are solved by simply letting people "
            "read the cards before they buy. It also demonstrates replay range, which answers a third "
            "objection."
        ),
        ctr="Readable real questions are inherently curiosity-driving — people stop to read them.",
        cvr="Self-selects the right buyer, which lifts satisfaction and cuts the 'not what I expected' returns.",
    ),
    AIImagePlanItem(
        name="Image 7 — Close: the gift people actually remember",
        role="close",
        background="Bright white with a warm periwinkle band at the base",
        purpose="Close on the gift occasion and the brand promise — reviews already call it a thoughtful gift.",
        visual=(
            "The box presented as a gift: held in two hands, or sitting with a simple ribbon on a bright "
            "table, a few cards fanned beside it. Behind, softly out of focus, a small warm gathering — "
            "the evening the gift turns into.\n\n"
            "Lower band: The Death Deck logo + tagline 'A lively game of surprising conversations.'\n"
            f"Thin spec strip: {SPECS}.\n"
            "A short closing line: 'For the friend who says the real thing. For the family that never "
            "quite gets around to it.'"
        ),
        overlay="THE GIFT THEY REMEMBER.",
        overlay_sub="For the family that never quite gets around to the conversation that matters.",
        props=["boxed as a gift with ribbon", "cards fanned beside it", "warm gathering soft-focus behind",
               "logo + tagline band", "spec strip"],
        lighting="Bright, warm, celebratory daylight. Optimistic and inviting.",
        why_it_works=(
            "Gifting is already a named strength in the reviews and it removes the buyer's own hesitation "
            "entirely — they do not have to want the conversation themselves to justify the purchase. "
            "Closing on identity beats closing on a feature."
        ),
        ctr="Gift framing widens the audience well beyond people already shopping for conversation games.",
        cvr="Gives the undecided buyer a second, easier reason to say yes.",
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Premium Full Image: brand banner",
        role="a+_banner",
        headline="THE TALK NOBODY REGRETS HAVING",
        body=(
            "The Death Deck turns the one conversation most families keep postponing into an evening "
            "people actually enjoy. 112 question cards, a mix of multiple-choice and open-ended prompts, "
            "for 2 to 10 players aged 13 and up. Expect laughter, a few long pauses, and the strange "
            "relief of finally saying something out loud."
        ),
        visual=("Wide, bright editorial banner — friends and family around a warm table mid-laugh, cards "
                "in hand, the box clearly in frame. Generous white space, playful brand-palette accents. "
                "Logo upper-left, tagline in the lower band. Desktop 1464x600, mobile 600x450 — keep the "
                "faces and the box inside the mobile safe area. Nothing dark, clinical or funereal."),
        alt="Friends and family laughing around a table while playing The Death Deck conversation card game.",
    ),
    AIModule(
        name="Module 2 — Premium Carousel (5 tiles): what's in the box",
        role="a+_carousel",
        headline="WHAT'S IN THE BOX",
        body=(
            "Tile 1: <b>112 QUESTION CARDS</b> — Enough for many nights, and no two the same.<br/>"
            "Tile 2: <b>TWO WAYS TO ASK</b> — Multiple-choice to warm up, open-ended to go deeper.<br/>"
            "Tile 3: <b>2-10 PLAYERS</b> — A couple on the sofa or the whole table after dinner.<br/>"
            "Tile 4: <b>30-90 MINUTES · AGES 13+</b> — Fits an evening; answer at your own level.<br/>"
            "Tile 5: <b>BOOKLET + SCORECARD</b> — Several ways to play, explained in one page."
        ),
        visual=("5 square tiles at 220x220, same white background and lighting. Client's icon roles: "
                "periwinkle plus signs and age icon, apricot dots for the 30-minute mark, magenta "
                "circles as side graphics, navy typography. Alt text per tile."),
        alt="Five-tile A+ carousel: 112 cards, two question types, 2-10 players, 30-90 minutes, booklet and scorecard.",
    ),
    AIModule(
        name="Module 3 — Premium Full Image: how a round actually goes",
        role="a+_banner",
        headline="HOW A ROUND ACTUALLY GOES",
        body=(
            "Someone draws a card and reads it out. If it is multiple-choice, everyone guesses how that "
            "person answered — which is where most of the laughing happens. If it is open-ended, you "
            "just talk, for as long as it deserves. There is a scoring version in the booklet if your "
            "group likes a game with a winner, and a no-scoring version if you would rather it just be "
            "a conversation. Both are correct."
        ),
        visual=("Wide 3-panel banner: DRAW (a hand pulling a card) → GUESS (a table laughing, pointing) "
                "→ TALK (two people leaning in, listening). Bright, editorial, thin magenta dividers. "
                "Mobile version stacks the three panels."),
        alt="A+ banner showing the three steps of a round: draw a card, guess the answer, then talk.",
    ),
    AIModule(
        name="Module 4 — Premium Full Image: why it exists",
        role="a+_banner",
        headline="MADE BY A HOSPICE SOCIAL WORKER",
        body=(
            "The Death Deck was created by a hospice social worker who spent years watching families "
            "have this conversation for the first time in a hospital corridor, under the worst possible "
            "conditions. The questions in this box are the ones she wished those families had asked each "
            "other years earlier, over dinner, while everyone was still laughing. That is the whole "
            "idea: have it early, have it easily, and have it with the people it concerns."
        ),
        visual=("Wide banner: warm human portrait of the creator on the left (or a friendly illustrated "
                "stand-in), the box and a small card fan on the right, the story line across the middle. "
                "Bright and optimistic — a credential, not a memorial. Absolutely no clinical or funeral "
                "imagery."),
        alt="A+ banner introducing the hospice social worker who created The Death Deck and why.",
    ),
    AIModule(
        name="Module 5 — Premium Carousel (5 tiles): who it's for",
        role="a+_carousel",
        headline="WHO IT'S FOR",
        body=(
            "Tile 1: <b>COUPLES</b> — Two players is plenty. You will still learn something new.<br/>"
            "Tile 2: <b>FRIENDS &amp; GAME NIGHTS</b> — Funnier than expected, and it beats small talk.<br/>"
            "Tile 3: <b>FAMILIES</b> — Three generations at one table, saying the things out loud.<br/>"
            "Tile 4: <b>A GIFT</b> — For the person who likes a real conversation, not a gadget.<br/>"
            "Tile 5: <b>GROUPS &amp; FACILITATORS</b> — Used by educators, doulas and care teams too."
        ),
        visual=("5 identical-composition lifestyle tiles at 220x220 — same warm daylight, same camera "
                "height, one setting per tile. Magenta accent corner on each. Alt text per tile names "
                "the audience."),
        alt="Five-tile A+ carousel showing who The Death Deck is for: couples, friends, families, gifting, groups.",
    ),
    AIModule(
        name="Module 6 — Premium Full Image: from the brand (benefits closer)",
        role="a+_banner",
        headline="FROM THE DEATH DECK",
        body=(
            "We are not trying to make anyone sad. We are trying to make one specific conversation "
            "ordinary — so that when it matters, your family already knows what you would have wanted, "
            "and you already know what they would have wanted. 112 cards, a lot of laughing, and "
            "questions that stay with people long after the box goes back on the shelf. Play it early. "
            "Play it with the people it concerns."
        ),
        visual=("Warm brand closer: the box and fanned cards on the left, a bright multigenerational "
                "table softly out of focus on the right, brand-voice line across the middle. Generous "
                "white space, playful accents. Never dark behind the logo."),
        alt="The Death Deck closing brand banner: play it early, play it with the people it concerns.",
    ),
    AIModule(
        name="Module 7 — Premium Q&A (finale)",
        role="a+_qa",
        headline="QUESTIONS BEFORE YOU BUY",
        body=(
            "<b>Q.</b> Is this depressing?<br/>"
            "<b>A.</b> It is the most common thing people expect, and the most common thing they say "
            "afterwards is how much they laughed. The multiple-choice cards are genuinely funny; the "
            "open-ended ones go deeper when your table wants them to.<br/><br/>"

            "<b>Q.</b> What is actually in the box?<br/>"
            "<b>A.</b> 112 question cards for 2 to 10 players, ages 13+, running about 30 to 90 "
            "minutes — plus an instruction booklet and a sample scorecard, with more scorecards "
            "available to download from our website.<br/><br/>"

            "<b>Q.</b> What kind of questions are they?<br/>"
            "<b>A.</b> They cover end-of-life preferences, beliefs about what comes after, how you want "
            "to be remembered, and funeral or burial wishes — approached from many angles, in two "
            "formats: multiple-choice and open-ended.<br/><br/>"

            "<b>Q.</b> Can teenagers play?<br/>"
            "<b>A.</b> It is rated 13 and up, so it is not made for younger children. The mix of humour "
            "and thoughtful questions works well with mature teens, and families often find it is the "
            "teenagers who ask the sharpest follow-ups.<br/><br/>"

            "<b>Q.</b> How many people do we need?<br/>"
            "<b>A.</b> Two to ten. Two works for couples or a one-on-one with a friend or parent; "
            "smaller groups suit dinner parties; larger groups suit game nights.<br/><br/>"

            "<b>Q.</b> What if someone does not want to answer?<br/>"
            "<b>A.</b> Then they do not. Everyone answers at their own comfort level, and the booklet "
            "includes ways to play that keep things light if that is what the group needs.<br/><br/>"

            "<b>Q.</b> Does it work as a gift?<br/>"
            "<b>A.</b> It is one of the most common reasons people buy it — for a partner, a parent, or "
            "the friend who would rather have a real conversation than another gadget."
        ),
        visual=("Vertical Q/A table, text only. Magenta divider lines between questions, small "
                "periwinkle Q. and navy A. labels. Mobile-first line lengths."),
        alt="Premium Q&A module answering the most-asked questions about The Death Deck card game.",
    ),
]


QA = [
    AIQA(q="Is this depressing?",
         a="It is what almost everyone expects, and it is almost never what people report afterwards. "
           "The multiple-choice cards are genuinely funny and the open-ended ones go deeper only when "
           "your table wants them to. Most groups describe the evening as warm and surprisingly light."),
    AIQA(q="What exactly do I get?",
         a="112 question cards in a portable box, plus an instruction booklet and a sample scorecard. "
           "The cards come in two formats — multiple-choice and open-ended — and more scorecards can be "
           "downloaded from our website."),
    AIQA(q="What kind of questions are on the cards?",
         a="They cover end-of-life preferences, beliefs about what comes after, how you want to be "
           "remembered, and funeral or burial wishes — approached from many different angles, some "
           "light-hearted and some searching."),
    AIQA(q="Can kids play this?",
         a="It is rated 13 and up, so it is not recommended for younger children. The mix of humour and "
           "thoughtful questions works well with mature teens, often in a family setting."),
    AIQA(q="How many players does it work for?",
         a="Two to ten. Two works well for couples or a one-on-one conversation with a friend or parent; "
           "small groups suit dinner parties and family gatherings; larger groups suit game nights."),
    AIQA(q="How long does a game take?",
         a="Roughly 30 to 90 minutes, depending on how many players you have and how long the "
           "conversations run. There is no wrong length — some tables finish a round, some talk all night."),
    AIQA(q="What if someone does not want to answer a question?",
         a="Then they pass. Everyone answers at their own comfort level, and the booklet includes ways to "
           "play that keep things lighter if that is what the group prefers."),
    AIQA(q="Is it a real game or just a stack of questions?",
         a="Both, depending on your group. The booklet includes a scoring version where players guess how "
           "someone answered, and a no-scoring version where you simply talk. The guessing version is "
           "where most of the laughing happens."),
    AIQA(q="Who made it?",
         a="A hospice social worker, after years of watching families have this conversation for the "
           "first time in a hospital corridor. The questions are the ones she wished those families had "
           "asked each other years earlier."),
    AIQA(q="Would this work as a gift?",
         a="It is one of the most common reasons people buy it — for a partner, a parent, or a friend who "
           "would rather have a real conversation than another gadget."),
]


def main() -> None:
    print("Loading The Death Deck customer + parsing listing…")
    cust = load_customer("the_death_deck")
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
