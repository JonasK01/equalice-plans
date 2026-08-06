"""Teacher Planner Company — A4 Teacher Planner 2026-2027 (Flex Union, leatherette)
Hand-written, KW-led, conversion-focused copy injected into the branded pipeline.

Marketplace: amazon.co.uk (UK) — UK English overlays + customer copy.
Product 01 · PARENT listing (colour variants) · Brand: Teacher Planner Company.

Positioning: 'Designed especially for teachers by teachers.' In this category the
INTERIOR sells the planner — the six-period daily layout is the core differentiator,
so the plan leads with real page spreads, not a closed cover.

Compliance / accuracy guardrails (UK):
  - Academic year 2026-2027 must be unmistakable (a real review complaint).
  - Prove substance: 200 pages, hardboard cover, wiro coil ('feels thinner than expected').
  - UK spelling throughout (organiser, colour, timetable).
  - No best / #1 / guaranteed · no prices or URLs on-image.
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


EXCEL = HERE / "listing.xlsx"
PLAN_NO = "01"
ASIN_OVERRIDE = "B0FCJ71NXF"   # confirmed by client (source filename said B00ZIGV046 — superseded)


# ===== KW-led copy (UK English) =====

TITLE = ('Teacher Planner Company A4 Teacher Planner 2026-2027 — Improved Six-Period Daily Layout '
         '· 200 Pages · Tabbed Dividers · 2 Storage Wallets · Luxury Leatherette Cover · Academic '
         'Diary and Organiser')

BULLETS = [
    "<b>SIX PERIODS A DAY — ROOM TO PLAN PROPERLY</b> — The improved six-period layout gives you "
    "dedicated space for lesson content, homework, activities, reminders and extra notes across up "
    "to six teaching periods. At A4 (approx. 300 x 250 mm) there is finally enough room to write "
    "what you actually need, instead of squeezing a lesson into one narrow box.",

    "<b>YOUR WHOLE SCHOOL YEAR IN ONE ORGANISER</b> — 200 planning pages covering the 2026-2027 "
    "academic year, with yearly calendars, monthly planning tables, term dates, meeting pages, "
    "timetables and notes sections. Every date, deadline and lesson lives in one place, so nothing "
    "gets forgotten across separate notebooks.",

    "<b>EVERY WORKSHEET IN ITS PLACE</b> — Laminated tabbed pocket dividers let you jump straight "
    "to the section you need mid-lesson, and two built-in plastic storage wallets — including an "
    "extra V-shaped wallet — keep worksheets, meeting documents and loose papers safely with your "
    "planner instead of loose in your bag.",

    "<b>BUILT TO SURVIVE A FULL SCHOOL YEAR</b> — A reinforced sturdy coil with wiro binding "
    "handles constant opening and page-turning, while the durable hardboard cover and premium "
    "paper give you a comfortable writing surface that still looks smart in July.",

    "<b>LUXURY-FEEL LEATHERETTE, SOFT-TOUCH FINISH</b> — A soft-touch leatherette cover with an "
    "elasticated closure cord keeps your pages and documents protected, and looks polished in "
    "classrooms, meetings and staffrooms. Designed especially for teachers, by teachers — and a "
    "genuinely useful gift for one.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="Clean white with a soft lilac-grey #F4F2F8 band across the bottom 15%. Identical background across all 3 options so the split test isolates composition, not colour.",
        purpose="Win the click in a grid of look-alike academic diaries. Ship all 3, keep the winner via Amazon Manage Your Experiments.",
        visual=(
            "Mock ALL 3 options — brand A/B tests and keeps the winner. Each: ONE callout, product "
            "dominant, and the academic year UNMISTAKABLE. Amazon slot-1 main must stay pure-white "
            "/ product-only — these callout versions are the CTR mains you A/B test against a "
            "clean white main.\n\n"

            "OPTION A — YEAR CLARITY (defuses the #1 complaint)\n"
            "The closed purple leatherette planner at a slight 3/4 angle, elasticated cord "
            "visible, soft-touch texture catching the light. Large, clean '2026-2027' lockup "
            "beside it, with a small 'A4' size chip.\n"
            "ONE CALLOUT (top-left badge, purple bg / white text): 'A4 · 2026-2027'.\n"
            "Why it wins: buyers scanning the grid are checking one thing first — is this the "
            "right academic year and the right size? Answering it in the thumbnail removes the "
            "biggest reason they scroll past (and the biggest source of returns).\n\n"

            "OPTION B — THE INTERIOR SELLS IT (owns the differentiator)\n"
            "The planner lying OPEN on white, showing a real, legible six-period daily spread "
            "with light handwriting in a couple of period boxes. The closed cover stands softly "
            "behind it so the buyer still sees the product.\n"
            "ONE CALLOUT (bottom-right badge, blue bg / white text): 'SIX PERIODS A DAY'.\n"
            "Why it wins: almost every competitor thumbnail shows a closed cover. Showing the "
            "actual layout answers the real question — 'will it fit how I teach?' — before the "
            "click.\n\n"

            "OPTION C — EVERYTHING YOU GET (owns value)\n"
            "Neat overhead flat-lay: the planner, the laminated tabbed dividers fanned out, both "
            "plastic wallets (including the V-shaped one) with a worksheet peeking out, and a pen.\n"
            "ONE CALLOUT (top-right badge, purple bg / white text): '200 PAGES · 2 WALLETS'.\n"
            "Why it wins: makes the value visible at a glance and separates this from a plain "
            "diary — you are buying a whole organising system.\n\n"

            "Across all 3: product dominant, callout ~6% of frame, same lighting + colour temp. "
            "UK spelling throughout."
        ),
        overlay="(one callout per option — see visual)",
        overlay_sub="3 hero options shipped — A/B test, keep the winner.",
        props=[
            "OPTION A: closed purple leatherette planner + '2026-2027' lockup + A4 chip",
            "OPTION B: open six-period spread + closed cover behind",
            "OPTION C: flat-lay — planner, fanned tabbed dividers, 2 wallets incl. V-shaped, pen",
        ],
        lighting="Bright, soft daylight with gentle shadow to show the leatherette texture. Same across all 3 for a clean split test.",
        why_it_works=(
            "Three triggers: A removes the year/size doubt that kills clicks and causes returns, "
            "B shows the six-period layout no competitor surfaces in a thumbnail, C makes the "
            "full value visible. One idea per option, readable on mobile."
        ),
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: The improved six-period daily layout",
        role="hook",
        background="Soft lilac-grey #F4F2F8 — calm, professional",
        purpose="Land the core differentiator: a full teaching day genuinely fits on one page.",
        visual=(
            "Large, straight-on hero of one open daily spread, shot clean and legible. Thin blue "
            "callout lines label the anatomy of the page: 'Period 1-6 planning boxes', 'Lesson "
            "content, homework and activities', 'Reminders', 'Additional notes'. Light, realistic "
            "teacher handwriting in two of the period boxes so it feels used, not sterile.\n\n"
            "Small chip in a corner: 'A4 — approx. 300 x 250 mm'. Keep the page fully readable — "
            "this image must survive a zoom."
        ),
        overlay="SIX PERIODS. ONE PAGE.",
        overlay_sub="Lesson content, homework, activities, reminders and notes — all with room to write.",
        props=["open daily spread", "callout lines labelling the six period boxes", "realistic handwriting", "A4 size chip"],
        lighting="Even, bright, shadow-free document lighting — legibility beats mood here.",
        why_it_works=(
            "The single biggest question a teacher has is 'does the layout match how I actually "
            "teach?'. Showing a labelled, legible six-period spread answers it instantly and is "
            "the clearest advantage over standard academic diaries."
        ),
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: Everything inside the 200 pages",
        role="educate",
        background="White with a soft purple ribbon footer",
        purpose="Show the full contents so the buyer sees a complete system, not just a diary.",
        visual=(
            "Clean 6-tile contents grid, each tile a small real photo of that section:\n"
            "  • YEARLY CALENDARS — see the whole year at a glance\n"
            "  • MONTHLY PLANNING TABLES — map out each month\n"
            "  • TERM DATES — every term logged in one place\n"
            "  • MEETING PAGES — staff meetings, notes and actions\n"
            "  • TIMETABLES — your weekly teaching schedule\n"
            "  • NOTES SECTIONS — space for everything else\n\n"
            "Centre or footer strip: '200 planning pages · 2026-2027 academic year'. Thin purple "
            "dividers between tiles."
        ),
        overlay="YOUR WHOLE YEAR INSIDE.",
        overlay_sub="Yearly calendars, monthly tables, term dates, meetings, timetables and notes.",
        props=["6 contents tiles (real page photos)", "200 pages / 2026-2027 footer strip", "purple dividers"],
        lighting="Bright, even, editorial daylight. Clarity over atmosphere.",
        why_it_works=(
            "Turns an abstract '200 pages' into six concrete sections the buyer can picture using. "
            "Also reinforces the correct academic year, directly addressing the review complaint "
            "that year and contents did not match expectations."
        ),
    ),
    AIImagePlanItem(
        name="Image 4 — Organisation: Tabbed dividers and two storage wallets",
        role="desire",
        background="Tidy teacher desk, bright natural daylight",
        purpose="Own the 'loose paperwork' pain — the everyday frustration this planner solves.",
        visual=(
            "Three-quarter desk shot of the planner open, with the laminated tabbed pocket "
            "dividers clearly fanned so each tab reads. In the foreground, the two built-in "
            "plastic wallets are shown in use: one holding marked worksheets, the V-shaped wallet "
            "holding a folded meeting document and a few loose notes.\n\n"
            "Small labels: 'Laminated tabbed dividers — find any section fast', 'Two built-in "
            "wallets, including an extra V-shaped wallet'. A pen and a mug complete the real desk "
            "feel."
        ),
        overlay="EVERY PAPER IN ITS PLACE.",
        overlay_sub="Laminated tabbed dividers plus two built-in wallets, including a V-shaped one.",
        props=["open planner", "fanned laminated tabbed dividers", "wallet with worksheets", "V-shaped wallet with documents", "pen", "mug"],
        lighting="Natural daylight from a window, soft shadows. Real staffroom or classroom desk — tidy, not staged-sterile.",
        why_it_works=(
            "Loose worksheets and lost paperwork are the daily frustration behind the purchase. "
            "Showing the dividers and both wallets actually holding real documents proves the "
            "planner replaces the folder-and-diary juggle."
        ),
    ),
    AIImagePlanItem(
        name="Image 5 — Trust: Built to last (and it is not thin)",
        role="trust",
        background="White with soft lilac panels behind each badge for separation",
        purpose="Prove build quality and directly defuse the 'feels thinner than expected' review.",
        visual=(
            "Centre: a clear SIDE-ON shot of the closed planner so the full 200-page thickness and "
            "the reinforced wiro coil are unmistakable — this is the key frame. Four badges in the "
            "corners:\n\n"
            "  • TOP-LEFT — 200 PLANNING PAGES (page-stack icon)\n"
            "  • TOP-RIGHT — REINFORCED WIRO COIL (coil icon)\n"
            "  • BOTTOM-LEFT — DURABLE HARDBOARD COVER (shield icon)\n"
            "  • BOTTOM-RIGHT — PREMIUM PAPER (pen-nib icon)\n\n"
            "Thin strip below: 'Soft-touch leatherette cover with elasticated closure cord — "
            "protects your pages and documents all year.'"
        ),
        overlay="BUILT TO LAST THE YEAR.",
        overlay_sub="200 pages · reinforced wiro coil · hardboard cover · premium paper.",
        props=["side-on thickness shot", "wiro coil close-up", "4 corner badges", "supporting strip"],
        lighting="Bright studio-even light with a crisp edge-light on the page block so the thickness reads clearly.",
        why_it_works=(
            "Answers the one recurring criticism head-on. A side-on thickness shot is the most "
            "honest, most persuasive proof of substance, and pairs the reassurance with the "
            "binding, cover and paper quality that reviewers already praise."
        ),
    ),
    AIImagePlanItem(
        name="Image 6 — Size and colour options",
        role="desire",
        background="Soft lilac-grey #F4F2F8 — same family as Image 2 for visual rhythm",
        purpose="Set honest size expectations and show the colour choice.",
        visual=(
            "Split frame.\n\n"
            "LEFT: an A4 scale reference — the planner on a desk beside a standard pen and an A4 "
            "worksheet, with a clean dimension callout 'approx. 300 mm x 250 mm'. The open spread "
            "shows how much writing space that really gives.\n\n"
            "RIGHT: the colour variants — the purple and the blue leatherette planners side by "
            "side at a slight angle, soft-touch texture and elasticated cord visible on both, "
            "with small labels 'Leatherette Purple' and 'Leatherette Blue'.\n\n"
            "Footer: 'Luxury-feel leatherette · soft-touch finish · elasticated closure cord.'"
        ),
        overlay="A4 SPACE. TWO COLOURS.",
        overlay_sub="Approx. 300 x 250 mm — in leatherette purple or leatherette blue.",
        props=["planner beside pen and A4 worksheet", "dimension callout", "purple and blue variants side by side"],
        lighting="Bright, even, honest daylight — true colour, true scale.",
        why_it_works=(
            "Size and colour are the last two decisions before add-to-cart on a parent listing "
            "with variants. Showing real A4 scale and both leatherette finishes removes the final "
            "hesitation and reduces wrong-variant returns."
        ),
    ),
    AIImagePlanItem(
        name="Image 7 — Brand close: By teachers, for teachers",
        role="close",
        background="Warm, calm classroom or staffroom at the end of the day, soft natural light",
        purpose="Close on the brand promise — less admin chaos, more time for teaching.",
        visual=(
            "Mid-range environmental shot: a teacher's desk at the end of the school day, the "
            "planner closed with its elasticated cord fastened, a pen resting on top, a mug and a "
            "small stack of marked books beside it. Calm, tidy, warm — the feeling of a day that "
            "is genuinely under control.\n\n"
            "Lower band: Teacher Planner Company logo + tagline, with a short reassurance line "
            "about a planner designed with real teaching days in mind."
        ),
        overlay="BY TEACHERS, FOR TEACHERS.",
        overlay_sub="Streamline the admin — and keep your time for what really matters.",
        props=["closed planner with cord fastened", "pen", "mug", "small stack of marked books", "logo + tagline band"],
        lighting="Warm end-of-day daylight, soft and calm. Reassuring, not clinical.",
        why_it_works=(
            "Closes on identity and outcome rather than features: teachers are not buying paper, "
            "they are buying a calmer, more controlled school year. The teacher-designed promise "
            "is the trust signal that lands the purchase."
        ),
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Brand banner: Designed especially for teachers, by teachers.",
        role="a+_banner",
        headline="DESIGNED BY TEACHERS, FOR TEACHERS.",
        body=(
            "The Teacher Planner Company A4 planner is built around the real demands of a school "
            "day. An improved six-period layout, 200 planning pages and dedicated space for term "
            "dates, meetings and timetables help you streamline the admin of the 2026-2027 "
            "academic year — so more of your time goes to the teaching that actually matters."
        ),
        visual="Wide, calm banner: a tidy teacher's desk in soft daylight, the purple leatherette planner open on a six-period spread, pen and mug beside it. Logo upper-left, tagline in the lower band.",
        alt="Teacher Planner Company A4 planner open on a tidy teacher desk showing the six-period daily layout.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): Why this planner",
        role="a+_carousel",
        headline="WHY THIS PLANNER",
        body=(
            "Tile 1: <b>SIX PERIODS A DAY</b> — Improved layout with room to plan properly.<br/>"
            "Tile 2: <b>200 PLANNING PAGES</b> — The full 2026-2027 academic year in one book.<br/>"
            "Tile 3: <b>TABBED DIVIDERS</b> — Laminated tabs to find any section fast.<br/>"
            "Tile 4: <b>TWO STORAGE WALLETS</b> — Including an extra V-shaped wallet.<br/>"
            "Tile 5: <b>LUXURY LEATHERETTE</b> — Soft-touch cover &amp; elasticated closure cord."
        ),
        visual="5 square tiles, purple accent corner on each, consistent bright product photography. Small icons (grid of six boxes · page stack · tab · wallet · leatherette swatch).",
        alt="Five-tile Premium A+ carousel covering the six-period layout, 200 pages, tabbed dividers, storage wallets and leatherette cover.",
    ),
    AIModule(
        name="Module 3 — Banner: The six-period daily layout",
        role="a+_banner",
        headline="A FULL TEACHING DAY, ON ONE PAGE.",
        body=(
            "The improved six-period format gives you dedicated planning space for up to six "
            "lessons, with room for lesson content, homework, activities, reminders and additional "
            "notes. At A4 — approximately 300 mm x 250 mm — you get generous writing space instead "
            "of cramped boxes, so a busy timetable finally fits the way you actually teach."
        ),
        visual="Wide banner: a large, legible open daily spread with thin callout lines labelling the six period boxes, the notes column and the reminders area. Light realistic handwriting in two boxes. A4 dimension chip in the corner.",
        alt="Premium A+ banner showing the improved six-period daily layout of the A4 teacher planner with labelled sections.",
    ),
    AIModule(
        name="Module 4 — Banner: Everything in one organiser",
        role="a+_banner",
        headline="YOUR WHOLE YEAR IN ONE PLACE.",
        body=(
            "Yearly calendars and monthly planning tables to see the term ahead. Term dates, "
            "meeting pages, timetables and notes sections for everything else a school year "
            "throws at you. Laminated tabbed pocket dividers keep each area easy to find, while "
            "two built-in plastic wallets — including an extra V-shaped wallet — hold worksheets, "
            "meeting documents and loose papers safely with the planner."
        ),
        visual="Wide banner split into a contents strip: YEARLY CALENDAR → MONTHLY TABLES → TERM DATES → MEETINGS → TIMETABLE → NOTES, each a small real page photo, with the tabbed dividers and both wallets shown at the right-hand end.",
        alt="Premium A+ banner showing the planner contents: yearly calendars, monthly tables, term dates, meetings, timetables, notes, dividers and wallets.",
    ),
    AIModule(
        name="Module 5 — Carousel (5 tiles): Made to last, made to look good",
        role="a+_carousel",
        headline="MADE TO LAST, MADE TO LOOK GOOD",
        body=(
            "Tile 1: <b>REINFORCED WIRO COIL</b> — Handles daily opening &amp; page-turning.<br/>"
            "Tile 2: <b>DURABLE HARDBOARD COVER</b> — Protects pages at school or on the move.<br/>"
            "Tile 3: <b>PREMIUM PAPER</b> — A comfortable, smooth writing surface.<br/>"
            "Tile 4: <b>ELASTICATED CLOSURE CORD</b> — Keeps documents secure in your bag.<br/>"
            "Tile 5: <b>PURPLE OR BLUE</b> — Luxury-feel leatherette in two colours."
        ),
        visual="5 identical-composition detail tiles (coil close-up · cover edge · paper with pen stroke · elastic cord fastened · purple and blue covers). Purple accent corner; bright consistent daylight.",
        alt="Five-tile A+ carousel of build quality details: wiro coil, hardboard cover, premium paper, elasticated cord, and the purple and blue leatherette colours.",
    ),
    AIModule(
        name="Module 6 — Premium Q&A",
        role="a+_qa",
        headline="QUESTIONS TEACHERS ASK",
        body=(
            "<b>Q.</b> Which academic year does this planner cover?<br/>"
            "<b>A.</b> This edition is designed for the 2026-2027 academic year, with yearly "
            "calendars, monthly planning tables and dedicated term-date pages for the "
            "year.<br/><br/>"

            "<b>Q.</b> What size is it, and is there enough writing space?<br/>"
            "<b>A.</b> It is A4, measuring approximately 300 mm long by 250 mm wide. The improved "
            "six-period layout uses that space for lesson content, homework, activities, reminders "
            "and additional notes.<br/><br/>"

            "<b>Q.</b> How many teaching periods can I plan each day?<br/>"
            "<b>A.</b> Up to six. The six-period daily layout gives each lesson its own dedicated "
            "planning space, with further room for notes and lesson details.<br/><br/>"

            "<b>Q.</b> How many pages are included?<br/>"
            "<b>A.</b> 200 planning pages, so the whole academic year fits in one organiser "
            "instead of several separate notebooks.<br/><br/>"

            "<b>Q.</b> Where do I keep worksheets and loose papers?<br/>"
            "<b>A.</b> The planner includes laminated tabbed pocket dividers and two built-in "
            "plastic wallets, including an extra V-shaped wallet, for worksheets, meeting "
            "documents and loose notes.<br/><br/>"

            "<b>Q.</b> Is it sturdy enough for daily classroom use?<br/>"
            "<b>A.</b> Yes. It is built with a reinforced sturdy coil and wiro binding, a durable "
            "hardboard cover, premium paper and a soft-touch leatherette covering with an "
            "elasticated closure cord."
        ),
        visual="Vertical Q/A table. Purple divider lines between each question. Small purple Q. and blue A. labels.",
        alt="Premium Q&A module answering the six most-asked teacher questions about the A4 teacher planner.",
    ),
    AIModule(
        name="Module 7 — Premium Comparison Chart",
        role="a+_comparison",
        headline="MORE THAN AN ACADEMIC DIARY",
        body=(
            "Compare across 4 columns: <b>Teacher Planner Company A4 Planner</b> · Standard "
            "academic diary · Plain notebook · Digital planning app.<br/><br/>"
            "Rows: Six-period daily teaching layout · A4 writing space (approx. 300 x 250 mm) · "
            "200 planning pages · Term dates &amp; meeting pages · Timetable pages · Laminated "
            "tabbed dividers · Two built-in storage wallets · Works with no battery or "
            "signal.<br/><br/>"
            "Highlight the Teacher Planner Company column with a soft purple tint and a "
            "'DESIGNED BY TEACHERS' ribbon at the top of the column."
        ),
        visual="Standard Amazon Premium Comparison Chart, 4 columns. Alternative columns use category descriptors only — no brand names. Purple header row, blue highlight on the Teacher Planner Company column.",
        alt="Premium comparison chart for the Teacher Planner Company A4 planner vs a standard academic diary, a plain notebook and a digital planning app.",
    ),
]


QA = [
    AIQA(q="Which academic year does this planner cover?",
         a="This edition is designed for the 2026-2027 academic year. It includes yearly calendars, monthly planning tables and dedicated term-date pages for that year."),
    AIQA(q="What size is the planner?",
         a="It is A4, measuring approximately 300 mm long by 250 mm wide, which gives generous writing space for lesson planning and notes."),
    AIQA(q="How many teaching periods can I plan for each day?",
         a="Up to six. The improved six-period layout provides dedicated planning space for up to six lessons or teaching periods, with additional room for lesson content, homework, activities, reminders and notes."),
    AIQA(q="How many planning pages are included?",
         a="There are 200 planning pages, giving you enough space for the full academic year without needing several separate notebooks."),
    AIQA(q="What sections does it include?",
         a="Yearly calendars, monthly planning tables, term dates, meeting pages, timetables and notes sections, so school dates, staff meetings, deadlines and lesson planning all sit in one organiser."),
    AIQA(q="Where can I keep worksheets and loose documents?",
         a="It includes laminated tabbed pocket dividers plus two built-in plastic storage wallets, including an extra V-shaped wallet, for worksheets, meeting documents and loose notes."),
    AIQA(q="Is it sturdy enough for everyday classroom use?",
         a="Yes. It uses a reinforced sturdy coil with wiro binding for constant opening and page-turning, a durable hardboard cover and premium paper, finished with a soft-touch leatherette covering and an elasticated closure cord."),
    AIQA(q="What colours are available, and would it make a good gift?",
         a="The leatherette collection comes in purple and blue. With its luxury-feel soft-touch cover and elasticated cord it presents well, making it a practical gift for a teacher, teaching assistant or trainee teacher."),
]


# Backend KWs — stem-deduped, byte-packed. UK spelling. Avoid brand names already in the title.
BACKEND = (
    "teacher planner 2026 2027 a4 teachers organiser academic diary lesson planning six period "
    "timetable term dates meeting pages notes wiro bound leatherette hardback tabbed dividers "
    "storage wallet teaching assistant trainee supply teacher department head school year "
    "work diary organiser notebook teacher gift"
)


def main() -> None:
    print("Loading Teacher Planner Company customer + parsing listing…")
    cust = load_customer("teacher_planner_company")
    brief = parse_excel(EXCEL)
    asin = ASIN_OVERRIDE
    OUT = HERE / f"{PLAN_NO}_{asin}_Image Plan.pdf"
    print(f"  Product: {brief.product_name}")
    print(f"  ASIN (file): {asin}  Marketplace: {cust.marketplace}")
    print(f"  USPs={len(brief.usps)} KWs={len(brief.all_keywords)} Q&A={len(brief.rufus_qa)} reviews=+{len(brief.good_reviews)}/-{len(brief.bad_reviews)}")

    builder = BriefBuilder(cust, brief, OUT, ai=None)
    builder._ai_title = TITLE
    builder._ai_bullets = BULLETS
    builder._ai_images = IMAGES
    builder._ai_modules = MODULES
    builder._ai_qa = QA
    builder._ai_backend = BACKEND
    builder.copy_source_label = "Hand-written senior copy (KW-led, UK English)"

    print("Building branded PDF…")
    pdf_path = builder.build()
    size_kb = pdf_path.stat().st_size // 1024
    import re
    pages = len(re.findall(rb'/Type\s*/Page[^s]', pdf_path.read_bytes()))
    print(f"Built: {pdf_path}")
    print(f"  Pages: {pages}  Size: {size_kb} KB")


if __name__ == "__main__":
    main()
