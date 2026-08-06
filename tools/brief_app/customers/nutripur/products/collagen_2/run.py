"""Nutripur COLLAGEN 2.0 — Bioactive Collagen Peptides® with Biotin
Hand-written KW-led copy injected into the branded ReportLab pipeline.

Marketplace: amazon.ca (Canada) · Overlay language: EN
Health Canada Licensed natural health product (NPN printed on pack — confirm before publishing).
  (See SOURCE_NOTES.md — brand to confirm printed NPN against the label/LNHPD
   before publishing; all NPN overlays carry this single number.)

Health-claim compliance baseline (NPN-approved, structure/function only):
  - "Helps reduce eye wrinkles within 4 weeks"
  - "Helps increase skin elasticity and skin density"
  - "Helps reduce wrinkles and fine facial lines"
  - "Helps promote healthy collagen and elastin production"
  - "Helps support healthy hair, skin and nails" (biotin / collagen cofactors)
  - "Helps in collagen formation to maintain healthy bones, cartilage, teeth and gums"
  - "Helps in connective tissue formation and wound healing"
  - "Helps relieve joint pain associated with osteoarthritis"

Never:
  - Cures / treats / prevents disease
  - Better than [competitor] / competitor names
  - Best / #1 / ultimate / guaranteed
  - "$" or any URL / ".com" in customer-facing copy (write "the Nutripur website")
  - Cartoon / candy / gummy aesthetic — this is a premium clinical-natural supplement
"""
from __future__ import annotations
import sys
from pathlib import Path

# This script lives at customers/<brand>/products/<product>/run.py
HERE = Path(__file__).resolve().parent          # the product folder (self-contained)
ROOT = HERE.parents[5]                           # project root (Claude_Code/)
sys.path.insert(0, str(ROOT))

from tools.brief_app.core.customers import load_customer
from tools.brief_app.core.excel_parser import parse_excel
from tools.brief_app.core.pdf_builder import BriefBuilder
from tools.brief_app.core.ai import AIImagePlanItem, AIModule, AIQA


# Inputs/outputs live alongside this script — the product folder is self-contained.
EXCEL = HERE / "listing.xlsx"                    # the SEO "axis" for this product
PLAN_NO = "06"   # SEO listing no. -> output named 0X_<ASIN>_Image Plan.pdf


# ===== KW-led copy — Health Canada NPN compliant =====

TITLE = 'Nutripur Collagen 2.0 — Hydrolyzed Collagen Peptides Type I & III 2,500 mg + Biotin, Vitamin C & Bamboo Silica · Unflavored · 60 Servings · Hair, Skin, Nails & Joints · Health Canada Licensed'

BULLETS = [
    "<b>COLLAGEN PEPTIDES FOR HAIR, SKIN, NAILS &amp; JOINTS</b> — Health Canada-licensed formula "
    "(Health Canada licensed) delivering 2,500 mg of hydrolyzed Bioactive Collagen Peptides (Type I &amp; III) per "
    "scoop. Helps reduce eye wrinkles within 4 weeks and helps increase skin elasticity and skin density. "
    "Beauty-from-within, built for adults and women.",

    "<b>4 ACTIVES IN ONE SCOOP — COLLAGEN + BIOTIN + VITAMIN C + SILICA</b> — Collagen peptides paired "
    "with Biotin 500 mcg, Vitamin C 185 mg, and 15 mg silicon from bamboo (Bambusa Vulgaris). Vitamin C "
    "helps promote healthy collagen and elastin production; biotin and the cofactor blend help support "
    "healthy hair, skin and nails. The cofactors do what collagen alone cannot.",

    "<b>UNFLAVORED · TASTELESS · MIXES CLEAR</b> — Dissolves clean in water, coffee, tea or a smoothie "
    "without changing the taste of your drink. Hydrolyzed to an average molecular weight near 2.0 kD (the "
    "\"2.0\") for easy mixing. No artificial colours, flavours, sweeteners, preservatives or fillers. "
    "No added sugar or sodium.",

    "<b>SUPPORTS JOINTS, BONES &amp; CONNECTIVE TISSUE</b> — Beyond beauty: helps relieve joint pain "
    "associated with osteoarthritis, and helps in collagen formation to maintain healthy bones, cartilage, "
    "teeth and gums, plus connective tissue formation and wound healing. One daily scoop covers skin and "
    "joints together.",

    "<b>60 SERVINGS · BOVINE GRASS-FED · MADE BY NUTRIPUR</b> — 60 daily scoops per container, sourced "
    "from grass-fed, pasture-raised bovine collagen (Halal &amp; Kosher certified), produced in a "
    "GMP-certified facility. Use for at least 5 months to see beneficial effects. Health Canada Licensed.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="White canvas with a soft teal #E8F5F2 wash across the bottom 15% for grounding. Same background across all 3 options for a clean A/B test.",
        purpose="Win the click in a collagen-powder search grid full of look-alike tubs. Test all 3, keep the winner.",
        visual=(
            "Brief the designer to mock ALL 3 options below. Brand picks the winner via Amazon Manage Your "
            "Experiments. Each option uses ONE callout, ONE action cue, ONE supporting prop — premium, clean, "
            "never bare product-on-white.\n\n"

            "▸ OPTION A — NPN CREDENTIAL HERO (owns the trust signal)\n"
            "Center: Collagen 2.0 container front-facing, label fully readable, slight elevated 3/4 turn. "
            "Container occupies ~65% of frame. ACTION CUE: the supplied scoop rests against the base with a "
            "small mound of fine collagen powder spilled cleanly onto the white surface (shows it IS a powder).\n"
            "ONE CALLOUT — top-right corner badge: 'HEALTH CANADA LICENSED' "
            "(Nutripur teal background, white text, small Canada-leaf icon).\n"
            "Why it wins: in the amazon.ca collagen grid, almost no competitor surfaces a Canadian NPN. The "
            "Health Canada credential is the single strongest trust signal a Canadian shopper sees pre-click.\n\n"

            "▸ OPTION B — DISSOLVES CLEAR IN COFFEE (defuses the top hesitation: 'will it clump / taste?')\n"
            "Center-left: Collagen 2.0 container, label readable. Center-right: a clear glass mug of coffee on "
            "a saucer with a thin swirl of collagen powder dissolving INTO it, leaving the coffee clear (no "
            "clumps). ACTION CUE: scoop tipping powder toward the mug, mid-pour. Prop: a few coffee beans.\n"
            "ONE CALLOUT — top-left corner badge: 'UNFLAVORED · MIXES CLEAR · NO CLUMPS' "
            "(Nutripur teal background, white text).\n"
            "Why it wins: reviews flag clumping/taste worries — this image proves solubility and the tasteless "
            "promise in one glance, the strongest objection-killer for a daily collagen.\n\n"

            "▸ OPTION C — 4-ACTIVE POWER STACK (owns the formula differentiator)\n"
            "Center: Collagen 2.0 container. Floating around it in a clean radial layout: 4 minimal icons "
            "labeled COLLAGEN 2,500 mg · BIOTIN 500 mcg · VITAMIN C 185 mg · BAMBOO SILICA 15 mg. Each icon "
            "a simple line glyph in Nutripur teal or navy on a soft white halo.\n"
            "ONE CALLOUT — bottom-right corner badge: '4 ACTIVES · 1 SCOOP' (Nutripur navy background, "
            "white text).\n"
            "Why it wins: most competitors sell collagen alone. Only Collagen 2.0 visibly stacks collagen + "
            "biotin + vitamin C + bamboo silica — the 4-icon halo communicates the cofactor advantage instantly.\n\n"

            "Across all 3: container dominant ~65%, callout ~6% of frame, supporting prop fills the remainder. "
            "Same lighting, same background wash, same colour temperature so the split test isolates "
            "composition, not light/colour."
        ),
        overlay="(one callout per option — see visual direction)",
        overlay_sub="3 hero options shipped — A/B test, keep the winner",
        props=[
            "OPTION A: container + scoop + clean powder mound + NPN badge",
            "OPTION B: container + clear glass mug of coffee with powder dissolving clear + scoop mid-pour + coffee beans + mixes-clear badge",
            "OPTION C: container + 4 active icons in radial halo + '4 actives 1 scoop' badge",
        ],
        lighting="Soft top key (5000K daylight balanced) with gentle fill from camera-right. Slight backlight on the container to make the label and the powder texture pop. Same lighting across all 3 options to keep the A/B test clean.",
        why_it_works=(
            "Three angles against three buyer triggers: A wins on credential trust (NPN), B wins on the "
            "clump/taste objection, C wins on the cofactor differentiator. One callout, one action cue, one "
            "prop each — clean enough to read on a mobile thumbnail. Premium clinical-natural, never candy."
        ),
        ctr="Option B (dissolves-clear-in-coffee) is the predicted CTR leader — it answers the daily-collagen buyer's first fear (clumping/taste) inside the thumbnail; Option A (NPN) is the trust-shopper variant.",
        cvr="Option C (4-active stack) is the CVR anchor on the PDP — once clicked, the cofactor differentiation (collagen + biotin + vitamin C + silica) justifies the premium over collagen-only tubs.",
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: 4 actives in one scoop",
        role="hook",
        background="Soft teal #E8F5F2 (Nutripur mood) — clinical-natural, premium, not pharma-sterile",
        purpose="Visually stack the 4-active differentiator. The hook collagen-only competitors can't match.",
        visual=(
            "Center: a clean macro of the supplied scoop heaped with fine, near-white collagen powder, set on "
            "the teal surface. Around the scoop, 4 labels in a clean radial layout (roughly 12, 3, 6, 9 o'clock): "
            "COLLAGEN PEPTIDES · BIOTIN · VITAMIN C · BAMBOO SILICA. Each label sits inside a soft-edged pill "
            "shape (Nutripur teal for collagen + silica, Nutripur navy for biotin + vitamin C). A subtle thin "
            "connecting line runs from each label to the scoop, like a clean medical infographic.\n\n"
            "Below the scoop: a small caption strip with the actual amounts — Collagen Type I &amp; III "
            "2,500 mg · Biotin 500 mcg · Vitamin C 185 mg · Bamboo Silica (15 mg silicon)."
        ),
        overlay="4 ACTIVES. ONE SCOOP.",
        overlay_sub="Collagen peptides + biotin + vitamin C + bamboo silica — the cofactors collagen alone cannot give.",
        props=["supplied scoop heaped with collagen powder (macro)", "4 active label pills", "thin connecting lines (infographic style)"],
        lighting="Even soft front-light, slight 3D shadow under the scoop. No drama lighting — educational hook, clarity beats mood.",
        why_it_works=(
            "Direct reversal of the category default: competitors sell 'collagen.' Collagen 2.0 owns 'collagen "
            "PLUS the cofactors that build it' (vitamin C for collagen/elastin synthesis, biotin + silica for "
            "hair/skin/nails). Educates and differentiates in one frame."
        ),
        ctr="Not a thumbnail driver — this is PDP slot 2 reinforcement; the mg caption strip is what holds the scrolling eye.",
        cvr="Strong CVR lift: it reframes the price gap as 4-in-1 value, the moment shoppers compare cost-per-serving against collagen-only powders.",
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: what each active supports (NPN-approved claims only)",
        role="educate",
        background="White with a soft Nutripur-teal ribbon footer",
        purpose="Defend the premium. Earn trust with Health Canada-language structure/function claims, nothing more.",
        visual=(
            "Three-column horizontal layout. Top of frame: 'WHAT EACH ACTIVE SUPPORTS' headline in Nutripur "
            "navy, sentence case.\n\n"
            "COLUMN 1 — 'Collagen Peptides (Type I &amp; III) 2,500 mg'\n"
            "  • Helps reduce eye wrinkles within 4 weeks\n"
            "  • Helps increase skin elasticity and skin density\n"
            "  • Helps in collagen formation for healthy bones, cartilage, teeth and gums\n"
            "Small icon: stylized skin / smooth-line glyph in Nutripur teal.\n\n"
            "COLUMN 2 — 'Vitamin C 185 mg + Biotin 500 mcg'\n"
            "  • Vitamin C helps promote healthy collagen and elastin production\n"
            "  • Helps support healthy hair, skin and nails\n"
            "  • A factor in the maintenance of good health\n"
            "Small icon: stylized hair-strand / nail glyph in Nutripur navy.\n\n"
            "COLUMN 3 — 'Bamboo Silica (15 mg silicon)'\n"
            "  • Supports connective tissue formation\n"
            "  • Helps relieve joint pain associated with osteoarthritis\n"
            "  • Plant-sourced from Bambusa Vulgaris shoot\n"
            "Small icon: stylized joint / bamboo glyph in Nutripur teal.\n\n"
            "Footer ribbon (Nutripur teal): 'Claims supported by Health Canada Licensed.'"
        ),
        overlay="WHAT EACH ACTIVE SUPPORTS.",
        overlay_sub="Backed by Health Canada Licensed — defensible, regulator-approved language.",
        props=["3 column layout", "3 small clinical icons (skin, hair/nail, joint/bamboo)", "NPN citation footer"],
        lighting="Flat clean studio. Educational module — readability beats atmosphere.",
        why_it_works=(
            "Every claim mirrors the NPN-approved recommended-use language — low compliance risk. Shoppers who "
            "filter on 'is this legit?' see regulator-aligned wording, not marketing-speak, which earns the "
            "premium over commodity collagen."
        ),
        ctr="N/A for click — this is the trust/educate slot deeper in the carousel.",
        cvr="High CVR for skeptical/40+ buyers comparing brands: the NPN citation footer is the proof that converts the careful researcher.",
    ),
    AIImagePlanItem(
        name="Image 4 — Lifestyle: morning coffee ritual (solubility proof, verbatim-derived)",
        role="desire",
        background="Real kitchen / café-corner scene, warm morning light from camera-right",
        purpose="Place the buyer in the daily ritual. Owns the 'mixes clear, tasteless, easy' verbatim from real reviews.",
        visual=(
            "Wide angled shot. An adult WOMAN (hands / forearm visible, no face-forward portrait) stirring a "
            "scoop of Collagen 2.0 into a clear glass mug of coffee at a sunlit kitchen counter. The powder is "
            "shown dissolving CLEAR — no clumps, no film — the action cue that defuses the clumping reviews.\n\n"
            "FOREGROUND right edge: Collagen 2.0 container (label facing camera) with the scoop resting beside "
            "it. A small linen napkin and a sprig of greenery for an elegant premium feel.\n\n"
            "Background: soft-focused bright kitchen, a plant, a folded newspaper or open laptop edge — a calm "
            "self-care morning, not a gym or a lab. Warm natural light from camera-right.\n\n"
            "Model selection note: adult woman, beauty-from-within target; use stock with model release if the "
            "brand prefers. Keep the look elegant and premium, never staged-clinical."
        ),
        overlay="ONE SCOOP. ONE COFFEE. ZERO CLUMPS.",
        overlay_sub="Unflavored, mixes clear — folds into your morning routine. Skin results often build from week 4.",
        props=["Collagen 2.0 container", "scoop", "clear glass mug of coffee with powder dissolving clear", "linen napkin", "sprig of greenery", "soft-focused plant / laptop edge", "adult woman (hands only, no face-forward)"],
        lighting="Warm morning side-light from camera-right. Soft highlight on the coffee mug. Slight rim on the container. Honest natural-clinical, elegant, not studio-staged.",
        why_it_works=(
            "Owns the strongest positive verbatim — *'tasteless, mixes well in coffee, easy daily habit'* — "
            "while visually answering the top negative (clumping). The morning-coffee ritual is the highest-"
            "intent CVR moment for a daily collagen and stays on-brand (hands-only, premium, no candy)."
        ),
        ctr="Could be tested as a secondary hero — the relatable coffee ritual reads instantly at thumbnail size for the lifestyle-led shopper.",
        cvr="The single strongest conversion image in the plan: it proves the daily habit is effortless and the powder behaves, removing the last hesitation before add-to-cart.",
    ),
    AIImagePlanItem(
        name="Image 5 — Trust: 4 quality credentials in one frame",
        role="trust",
        background="White with soft teal panels behind each badge for separation",
        purpose="Stack the filters a careful Canadian shopper scans for. Defuses the 'is this brand legit?' check.",
        visual=(
            "Centered macro of the Collagen 2.0 container (label facing camera). Four trust badges arranged "
            "top-left, top-right, bottom-left, bottom-right:\n\n"
            "  • TOP-LEFT — HEALTH CANADA LICENSED (small Canada-leaf icon + the Health Canada licence on pack below)\n"
            "  • TOP-RIGHT — GRASS-FED · PASTURE-RAISED BOVINE (small leaf icon + Halal &amp; Kosher note)\n"
            "  • BOTTOM-LEFT — GMP CERTIFIED (small shield icon)\n"
            "  • BOTTOM-RIGHT — NO FLAVOURS, COLOURS, SWEETENERS OR FILLERS (small clean-leaf icon)\n\n"
            "Below the container, a thin strip with the supporting line: 'Hydrolyzed Type I &amp; III collagen "
            "peptides, average molecular weight near 2.0 kD. Bamboo-sourced silica. No added sugar or sodium. "
            "Made by Nutripur.'"
        ),
        overlay="HEALTH-CANADA LICENSED. GRASS-FED. CLEAN.",
        overlay_sub="Health Canada Licensed · Grass-fed pasture-raised bovine · GMP certified · No fillers",
        props=["Collagen 2.0 container (center)", "4 badge graphics in corners", "thin supporting strip"],
        lighting="Studio even light. Hard catch-light on the container. Badges legible at thumbnail size.",
        why_it_works=(
            "Stacks the four filters that matter for a premium-collagen shopper: regulator, source quality, "
            "manufacturing, clean formulation. The 2.0 kD molecular-weight detail signals real formulation "
            "literacy that commodity tubs cannot claim."
        ),
        ctr="N/A — trust slot, not a click driver.",
        cvr="Closes the trust gap for the comparison shopper: four credentials in one glance is what tips a careful buyer toward the premium SKU.",
    ),
    AIImagePlanItem(
        name="Image 6 — Format clarity: 60 servings + how to use",
        role="desire",
        background="Soft teal #E8F5F2 — same as Image 2 for visual rhythm",
        purpose="Make the value and the routine crystal clear. Removes 'how much, how long, how do I take it?' friction.",
        visual=(
            "Split-frame infographic.\n\n"
            "LEFT 60% of frame: Collagen 2.0 container, open, with the scoop lifting a clean heap of powder; "
            "a clear glass of water and a clear glass of coffee beside it to show the mixing options.\n\n"
            "RIGHT 40% of frame: vertical breakdown panel\n"
            "  • 60 SERVINGS PER CONTAINER\n"
            "  • 1 SCOOP / DAY (2,500 mg collagen)\n"
            "  • Mix in 250 mL water, coffee, tea or a smoothie\n"
            "  • Unflavored — mixes clear, no clumps\n"
            "  • Use for at least 5 months to see full results\n\n"
            "Small caption below the panel: 'Suggested use: 1 scoop daily, any time of day. Consistency is key.'"
        ),
        overlay="60 SERVINGS. ONE SIMPLE SCOOP A DAY.",
        overlay_sub="Mix in water, coffee, tea or a smoothie — unflavored, mixes clear. Use 5 months for full results.",
        props=["Collagen 2.0 container (open)", "scoop with powder heap", "clear glass of water", "clear glass of coffee", "usage info panel"],
        lighting="Even soft front-light. Clean infographic feel.",
        why_it_works=(
            "Pack-size value made obvious and the realistic timeline set up front (4-week skin / 5-month full "
            "results) so expectations match the reviews — which reduces the 'didn't work for me' returns the "
            "negative verbatim warns about."
        ),
        ctr="N/A — PDP clarity slot.",
        cvr="Lifts CVR by pre-answering the dosing and 'how long' questions; the explicit timeline manages expectations and protects review quality post-purchase.",
    ),
    AIImagePlanItem(
        name="Image 7 — Brand close: beauty-from-within + Made by Nutripur",
        role="close",
        background="Warm, elegant vanity / kitchen-corner scene, soft morning light",
        purpose="Close on identity. Premium beauty-from-within ritual + brand provenance in one frame.",
        visual=(
            "Mid-range environmental shot. An adult WOMAN's hand (no face-forward portrait — over-shoulder or "
            "side angle) setting down a clear glass mug after stirring in Collagen 2.0, calm and unhurried — a "
            "small self-care moment, not a posed shot.\n\n"
            "On the counter beside her: the Collagen 2.0 container (label readable), a small Nutripur info card "
            "with the NPN number visible, a sprig of eucalyptus or a single stem in a slim vase, and soft "
            "natural skincare-adjacent décor (a linen towel, a ceramic dish). Elegant, premium, uncluttered.\n\n"
            "Warm morning side-light from a window. Light wood / stone counter, soft neutral tones. Reads "
            "'premium daily ritual,' NOT 'pharmacy' and NOT 'gym.'\n\n"
            "Foreground bottom-left: a handwritten-style note card reading: *Beauty, supported from within. "
            "— From the Nutripur family, Quebec.*"
        ),
        overlay="BEAUTY, SUPPORTED FROM WITHIN.",
        overlay_sub="Hair, skin, nails &amp; joints — one daily scoop. Made by Nutripur · Health Canada Licensed.",
        props=["Collagen 2.0 container", "Nutripur info card with NPN", "clear glass mug", "single stem in a slim vase", "linen towel / ceramic dish", "light wood or stone counter", "adult woman (hand only, no face-forward)", "handwritten-style note card"],
        lighting="Warm morning side-light from window. Soft, flattering glow. Honest, elegant, lived-in — not staged.",
        why_it_works=(
            "Closes on the brand promise the beauty-from-within buyer needs before checkout: a real, premium "
            "daily ritual plus the Canadian regulatory credential. The calm self-care moment is the visual "
            "metaphor for the long-term results the formula is designed to deliver."
        ),
        ctr="N/A — final close slot.",
        cvr="Seals CVR on identity and provenance: the premium ritual plus the NPN and 'from the Nutripur family' line gives the brand-driven buyer the emotional + trust push to convert.",
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Brand banner: Beauty, supported from within.",
        role="a+_banner",
        headline="BEAUTY, SUPPORTED FROM WITHIN.",
        body=(
            "Collagen 2.0 by Nutripur is a Health Canada-licensed bioactive collagen peptide powder (Health Canada licensed) for adults who want healthy hair, skin, nails and joints. Hydrolyzed Type I &amp; III "
            "collagen plus the cofactors that help build it — biotin, vitamin C and bamboo silica. Unflavored, "
            "mixes clear, one scoop a day."
        ),
        visual="Wide cinematic morning scene — light stone counter, Collagen 2.0 container front-center, a clear glass mug of coffee with powder dissolving clear, soft natural window light, a single eucalyptus stem soft-focused. Nutripur navy logo upper-left, Health Canada the Health Canada licence small in the bottom band.",
        alt="Nutripur Collagen 2.0 bioactive collagen peptide powder container on a sunlit counter beside a clear glass of coffee, with a eucalyptus stem in soft focus.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): The Collagen 2.0 Difference",
        role="a+_carousel",
        headline="THE COLLAGEN 2.0 DIFFERENCE",
        body=(
            "Tile 1: <b>2,500 mg COLLAGEN PEPTIDES</b> — Hydrolyzed Type I &amp; III, near 2.0 kD molecular weight.<br/>"
            "Tile 2: <b>4 ACTIVES IN 1 SCOOP</b> — Collagen + biotin + vitamin C + bamboo silica.<br/>"
            "Tile 3: <b>HEALTH CANADA LICENSED</b> — Health Canada licensed. Defensible, regulator-approved claims.<br/>"
            "Tile 4: <b>UNFLAVORED · MIXES CLEAR</b> — No clumps, no taste, no added sugar or fillers.<br/>"
            "Tile 5: <b>GRASS-FED · MADE BY NUTRIPUR</b> — Pasture-raised bovine, Halal &amp; Kosher, GMP certified."
        ),
        visual="5 square tiles, Nutripur navy accent corner on each. Same composition discipline across all 5. Small icons (collagen helix · 4-active stack · maple leaf · clear mug · grass-fed leaf).",
        alt="Five-tile Premium A+ carousel covering Collagen 2.0 differentiators: 2,500 mg peptides, 4 actives, Health Canada licensed, unflavored mixes clear, grass-fed made by Nutripur.",
    ),
    AIModule(
        name="Module 3 — Banner: How the formula supports hair, skin and nails",
        role="a+_banner",
        headline="HELPS REDUCE WRINKLES. SUPPORTS HAIR, SKIN &amp; NAILS.",
        body=(
            "Per its Health Canada licence: helps reduce eye wrinkles within 4 weeks, helps increase skin "
            "elasticity and skin density, and helps reduce wrinkles and fine facial lines. Vitamin C helps "
            "promote healthy collagen and elastin production, while biotin helps support healthy hair, skin "
            "and nails. The cofactors do what collagen alone cannot."
        ),
        visual="Wide banner: clean clinical-style infographic of a stylized skin cross-section (no faces), with 4 active labels (Collagen, Biotin, Vitamin C, Bamboo Silica) connected by thin lines to what each supports. Nutripur teal and navy palette only. the Health Canada licence small in the lower band.",
        alt="Premium A+ banner showing how Collagen 2.0 actives support skin elasticity, wrinkle reduction and healthy hair and nails per Health Canada Licensed.",
    ),
    AIModule(
        name="Module 4 — Banner: Beyond beauty — joints, bones and connective tissue",
        role="a+_banner",
        headline="JOINTS. BONES. CONNECTIVE TISSUE.",
        body=(
            "More than skin-deep. Helps relieve joint pain associated with osteoarthritis, helps in collagen "
            "formation to maintain healthy bones, cartilage, teeth and gums, and helps in connective tissue "
            "formation and wound healing. One daily scoop covers skin and joints together. Per Health Canada "
            "Health Canada licensed."
        ),
        visual="Triptych within one banner: LEFT — a clear glass of water with collagen powder dissolving clear, scoop beside it. CENTER — stylized clinical joint / cartilage glyph in Nutripur teal (no medical diagram of disease). RIGHT — an active adult moment, hands-only (e.g. lacing a walking shoe, gardening) showing easy movement. Warm natural light across all three panels.",
        alt="Triptych A+ banner showing Collagen 2.0 supporting joint comfort, bone and connective tissue alongside its daily mix-in routine, per Health Canada-approved indications.",
    ),
    AIModule(
        name="Module 5 — Carousel (5 tiles): The Nutripur Hair, Skin & Nails Family",
        role="a+_carousel",
        headline="THE NUTRIPUR FAMILY",
        body=(
            "Tile 1: <b>COLLAGEN 2.0 (this product)</b> — Bioactive collagen peptides + biotin, vitamin C &amp; "
            "bamboo silica. Unflavored powder, 60 servings.<br/>"
            "Tile 2: <b>COLLAGEN BEAUTY BLENDS</b> — Companion collagen formats from the Hair, Skin &amp; Nails "
            "line for variety in routine.<br/>"
            "Tile 3: <b>BIOTIN &amp; HAIR SUPPORT</b> — Targeted hair, skin and nails support.<br/>"
            "Tile 4: <b>VITAMIN C &amp; ANTIOXIDANTS</b> — Cofactor support for everyday collagen production.<br/>"
            "Tile 5: <b>JOINT &amp; MOBILITY SUPPORT</b> — For active adults pairing beauty with movement.<br/>"
            "<i>Confirm current Hair, Skin &amp; Nails SKUs on the Nutripur website and pull current product "
            "photography from brand assets before publishing.</i>"
        ),
        visual="5 identical-composition product tiles. Nutripur navy + teal accent corner on each. Family flat-lay style with consistent container / packaging photography.",
        alt="Five-tile A+ carousel of the Nutripur Hair, Skin & Nails family anchored by Collagen 2.0, with companion collagen, biotin, vitamin C and joint-support products.",
    ),
    AIModule(
        name="Module 6 — Premium Q&A",
        role="a+_qa",
        headline="QUESTIONS CUSTOMERS ASK",
        body=(
            "<b>Q.</b> Will it clump or change the taste of my coffee?<br/>"
            "<b>A.</b> No. Collagen 2.0 is unflavored and hydrolyzed to a small peptide size (near 2.0 kD) so it "
            "mixes clear in water, coffee, tea or a smoothie. Stir into liquid as you pour for the smoothest "
            "result.<br/><br/>"

            "<b>Q.</b> What is actually in each scoop?<br/>"
            "<b>A.</b> 2,500 mg of hydrolyzed Bioactive Collagen Peptides (Type I &amp; III) from grass-fed, "
            "pasture-raised bovine, plus Vitamin C 185 mg, Biotin 500 mcg and 15 mg silicon from bamboo silica. "
            "No artificial colours, flavours, sweeteners, preservatives or fillers; no added sugar or sodium.<br/><br/>"

            "<b>Q.</b> What does it help with?<br/>"
            "<b>A.</b> Per its Health Canada licence: helps reduce eye wrinkles within 4 weeks, helps increase "
            "skin elasticity and skin density, helps support healthy hair, skin and nails, helps in collagen "
            "formation for healthy bones, cartilage, teeth and gums, and helps relieve joint pain associated "
            "with osteoarthritis.<br/><br/>"

            "<b>Q.</b> How long until I see results?<br/>"
            "<b>A.</b> Skin benefits such as reduced eye wrinkles can begin within 4 weeks. For full beneficial "
            "effects, use one scoop daily for at least 5 months. Consistency is key — results vary by person.<br/><br/>"

            "<b>Q.</b> How many servings are in a container?<br/>"
            "<b>A.</b> 60 daily servings per container — one scoop a day, any time of day.<br/><br/>"

            "<b>Q.</b> Where is it made and is it certified?<br/>"
            "<b>A.</b> Made by Nutripur in a GMP-certified facility, licensed by Health Canada. "
            "The collagen is grass-fed, pasture-raised bovine, Halal &amp; Kosher certified."
        ),
        visual="Vertical Q/A table. Nutripur teal divider lines between each Q. Small Nutripur navy Q. and A. labels.",
        alt="Premium Q&A module addressing the six most-asked questions for Nutripur Collagen 2.0.",
    ),
    AIModule(
        name="Module 7 — Premium Comparison Chart",
        role="a+_comparison",
        headline="WHY COLLAGEN 2.0",
        body=(
            "Compare across 4 columns: <b>Nutripur Collagen 2.0</b> · Plain collagen peptides powder · "
            "Flavoured collagen drink mix · Biotin-only beauty capsule.<br/><br/>"
            "Rows: Collagen peptides per scoop (2,500 mg) · Type I &amp; III · Biotin included · Vitamin C "
            "cofactor · Bamboo silica · Health Canada NPN · Unflavored / mixes clear · No added sugar or "
            "fillers · Joint support claim (per NPN) · Grass-fed pasture-raised source.<br/><br/>"
            "Highlight the Nutripur Collagen 2.0 column with a soft Nutripur-teal tint and a 'BEAUTY + JOINTS "
            "IN ONE' ribbon at the top of the column."
        ),
        visual="Standard Amazon Premium Comparison Chart layout, 4 product columns. Competitor columns use category descriptors only — no brand names. Nutripur navy header row.",
        alt="Premium comparison chart for Nutripur Collagen 2.0 vs. plain collagen powder, flavoured collagen drink mix, and biotin-only capsule alternatives.",
    ),
]


QA = [
    AIQA(q="Will it clump or change the taste of my drink?",
         a="No. Collagen 2.0 is unflavored and hydrolyzed to a small peptide size (near 2.0 kD) so it mixes clear in water, coffee, tea or a smoothie. Stir it in as you pour for the smoothest result."),
    AIQA(q="How long until I see results?",
         a="Skin benefits such as reduced eye wrinkles can begin within 4 weeks. For full beneficial effects, use one scoop daily for at least 5 months. Consistency matters and results vary by person."),
    AIQA(q="What's in each scoop?",
         a="2,500 mg of hydrolyzed Bioactive Collagen Peptides (Type I & III) from grass-fed, pasture-raised bovine, plus Vitamin C 185 mg, Biotin 500 mcg and 15 mg silicon from bamboo silica. No artificial colours, flavours, sweeteners, preservatives or fillers; no added sugar or sodium."),
    AIQA(q="What does Collagen 2.0 help with?",
         a="Per its Health Canada licence: helps reduce eye wrinkles within 4 weeks, helps increase skin elasticity and skin density, helps support healthy hair, skin and nails, helps in collagen formation for healthy bones, cartilage, teeth and gums, and helps relieve joint pain associated with osteoarthritis."),
    AIQA(q="How is it different from a plain collagen powder?",
         a="Collagen 2.0 pairs 2,500 mg of Type I & III peptides with the cofactors that help build collagen: vitamin C for collagen and elastin production, plus biotin and bamboo silica for hair, skin and nails. Most powders give you collagen alone."),
    AIQA(q="Is it good for women over 50 / for joints too?",
         a="Yes. It is formulated for adults wanting beauty-from-within support and also helps relieve joint pain associated with osteoarthritis and supports connective tissue, so one daily scoop covers skin and joints together."),
    AIQA(q="How many servings are in a container and how do I take it?",
         a="60 daily servings per container. Mix one scoop in 250 mL of water, coffee, tea or a smoothie, once a day, any time of day."),
    AIQA(q="Where is it made and is it certified?",
         a="Made by Nutripur in a GMP-certified facility and licensed by Health Canada. The collagen is grass-fed, pasture-raised bovine, Halal and Kosher certified."),
]


# Backend KWs — stem-deduped, byte-packed. Avoid: brand names already in title, superlatives.
# Includes FR fallback terms because amazon.ca is bilingual.
BACKEND = (
    "collagen peptides powder hydrolyzed type 1 3 bioactive biotin vitamin c bamboo silica unflavored "
    "mixes clear coffee smoothie hair skin nails joints wrinkles elasticity beauty from within women "
    "over 50 grass fed bovine halal kosher gmp health canada npn collagene hydrolyse peptides poudre "
    "cheveux peau ongles articulations biotine"
)


def main() -> None:
    print("Loading Nutripur customer + parsing Collagen 2.0 Excel…")
    cust = load_customer("nutripur")
    brief = parse_excel(EXCEL)
    asin = brief.asin or "NA"
    OUT = HERE / f"{PLAN_NO}_{asin}_Image Plan.pdf"
    print(f"  Product: {brief.product_name}")
    print(f"  ASIN: {brief.asin}  Marketplace: {cust.marketplace}")
    print(f"  USPs={len(brief.usps)} KWs={len(brief.all_keywords)} Q&A={len(brief.rufus_qa)} reviews=+{len(brief.good_reviews)}/-{len(brief.bad_reviews)}")
    print(f"  Health Canada Licensed (NPN on pack — confirm before publishing)")

    builder = BriefBuilder(cust, brief, OUT, ai=None)
    builder._ai_title = TITLE
    builder._ai_bullets = BULLETS
    builder._ai_images = IMAGES
    builder._ai_modules = MODULES
    builder._ai_qa = QA
    builder._ai_backend = BACKEND
    builder.copy_source_label = "Hand-written senior copy (KW-led, NPN-defensible)"

    print("Building branded PDF…")
    pdf_path = builder.build()
    size_kb = pdf_path.stat().st_size // 1024
    import re
    pages = len(re.findall(rb'/Type\s*/Page[^s]', pdf_path.read_bytes()))
    print(f"Built: {pdf_path}")
    print(f"  Pages: {pages}  Size: {size_kb} KB")


if __name__ == "__main__":
    main()
