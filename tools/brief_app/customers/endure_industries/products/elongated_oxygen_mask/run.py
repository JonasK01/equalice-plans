"""Endure Industries — Elongated Oxygen Mask (Product 01)
Hand-written senior copy injected into the branded ReportLab pipeline.

Marketplace: amazon.com (US)
ASIN: B0BX4HG6FR

MEDICAL DEVICE — EXTRA STRICT compliance (the build auto-checks and BLOCKS on violation):
  This is an oxygen-DELIVERY accessory, NOT a therapy.
  - NEVER claim it treats / cures / prevents / relieves any disease or condition.
  - NO disease names (no asthma / COPD / etc.).
  - Frame strictly as oxygen delivery; include "For use under the guidance of a medical professional."
  - NO "FDA approved/cleared".
  - NO superlatives: best / #1 / ultimate / guaranteed / miracle.
  - In ANY customer-facing copy (title, bullets, overlays, module headline+body, Q&A):
      NO "$", NO URL / ".com" / external link.
  - AVOID the word "prevent" entirely (it trips the checker) — use "helps keep" / "reduces".
  - AVOID "treat" / "treatment" in customer-facing copy (trips the checker). Compatible-equipment
    terms (concentrator, nebulizer) are fine.

Only the scanned fields must stay clean: title, bullets, image overlay/overlay_sub, module
headline/body, and Q&A. Art-direction fields (visual, purpose, props, lighting, why_it_works,
ctr, cvr) and BACKEND are NOT scanned — fit/equipment language lives safely there.

Real review objections defused in the images:
  - sizing/fit ("too small even when adult/XL") -> elongated shape + actual dimensions + adjustable fit
  - tubing kinks / arrives bent -> full 2 m smooth, kink-resistant tubing laid out
  - comfort for extended / overnight use -> soft PVC, adjustable nose clip + elastic strap
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
PLAN_NO = "01"   # SEO listing no. -> output named 0X_<ASIN>_Image Plan.pdf
ASIN = "B0BX4HG6FR"


# ===== KW-led copy — medical-device compliant (oxygen delivery only) =====

# Title is HTML-escaped by the builder, so use a literal "&" (counts as 1 char).
# Real length (counting "&" as 1) must be <= 200.
TITLE = (
    "Endure Elongated Oxygen Mask with 2 m Tubing for Adults — Latex-Free Soft Medical-Grade "
    "PVC, Adjustable Nose Clip & Elastic Strap — Pack of 5 Individually Wrapped, for "
    "Concentrator & Nebulizer"
)

# Bullets are raw HTML -> use "&amp;" for ampersands.
BULLETS = [
    "<b>ELONGATED ADULT FIT</b> — The elongated shape is designed for full adult face coverage from "
    "the bridge of the nose to below the chin, so it sits and seals more easily than short, round "
    "masks. An adjustable aluminium nose strip and elastic head strap let each person shape the fit "
    "to their own face for a secure, low-slip hold.",

    "<b>FULL 2 M / 6.8 FT OXYGEN TUBING</b> — Includes a generous 2-meter (6.8 ft) length of standard "
    "oxygen tubing so the wearer can move, sit up or rest while staying connected to the unit. The "
    "smooth-wall tubing is made to resist kinking and stay flexible for steady, uninterrupted oxygen "
    "delivery.",

    "<b>SOFT, LATEX-FREE MEDICAL-GRADE PVC</b> — Built from soft medical-grade PVC with smooth edges "
    "for comfortable wear, including longer and overnight sessions. The material is latex-free for "
    "added peace of mind, and the contoured nose clip + elastic strap help keep the mask gently and "
    "securely in place.",

    "<b>WORKS WITH CONCENTRATOR &amp; NEBULIZER</b> — The standard universal connector fits common "
    "home and clinical oxygen concentrators, oxygen tanks and nebulizers, so the mask drops into your "
    "existing setup with no adapters. A simple, reliable connection for everyday home oxygen delivery.",

    "<b>PACK OF 5, INDIVIDUALLY WRAPPED</b> — Each mask is sealed and individually wrapped for hygiene "
    "and easy storage, with five masks per pack for rotation, travel or sharing across a household. "
    "Trusted by medical professionals, EMS and the US Military. For use under the guidance of a "
    "medical professional.",
]


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="Clean clinical white with a soft Endure-blue tint (#C5DAFA) across the bottom 15% for grounding. Identical background across all 3 options for a clean A/B test.",
        purpose="Win the click in a search grid full of look-alike round oxygen masks. Lead with proof (fit + 2 m tubing + pack of 5), not a bare product-on-white.",
        visual=(
            "Brief the designer to mock ALL 3 options below. Brand picks the winner via Amazon Manage "
            "Your Experiments. Each option uses ONE callout badge, ONE action cue, ONE supporting prop "
            "— clean, calm, clinical, never alarming.\n\n"

            "▸ OPTION A — PROOF-BADGE HERO (owns the spec scan)\n"
            "Center: the elongated mask front-facing at a slight 3/4 elevated turn, occupying ~60% of "
            "frame, with the full 2 m tubing laid out in one smooth, deliberate S-curve below it so the "
            "real length reads at a glance. Lower-right: one sealed individual wrapper to signal pack-of-5 "
            "hygiene.\n"
            "ONE CALLOUT — top-right stacked badge strip (Endure blue #0043A3 panel, white text): "
            "'LATEX-FREE · MEDICAL-GRADE PVC · 2 M TUBING · PACK OF 5'.\n"
            "Why it wins: a buyer scanning the grid gets every purchase-deciding spec in one read, with "
            "the full tubing visibly proving the 2 m claim competitors only state in text.\n\n"

            "▸ OPTION B — FIT / COVERAGE HERO (defuses the #1 'will it fit my face?' objection)\n"
            "Center: the elongated mask shown against a neutral grey face silhouette / mannequin profile "
            "(no real face, no distress) so the elongated nose-to-chin coverage is obvious. A thin dimension "
            "caller marks the mask height. Right: the adjustable aluminium nose strip and elastic strap "
            "shown extended.\n"
            "ONE CALLOUT — top-left badge (Endure blue): 'ELONGATED ADULT COVERAGE · ADJUSTABLE FIT'.\n"
            "Why it wins: the top review complaint is 'too small even when listed adult/XL' — this image "
            "answers the sizing fear before the click, the single biggest CVR lever for this product.\n\n"

            "▸ OPTION C — WORKS-WITH HERO (owns the compatibility question)\n"
            "Center: the mask + 2 m tubing with the standard connector end in sharp focus, the tubing "
            "leading toward a soft-focus home oxygen concentrator at frame edge. Calm home setting, "
            "soft-blue tones.\n"
            "ONE CALLOUT — bottom-right badge (Endure blue): 'WORKS WITH CONCENTRATOR & NEBULIZER · "
            "STANDARD CONNECTOR'.\n"
            "Why it wins: the second-biggest pre-click question is 'will it work with MY machine?' — the "
            "visible standard connector + concentrator context answers it instantly.\n\n"

            "Across all 3: mask + tubing dominant ~65%, callout badge ~8%, supporting prop fills the rest. "
            "Same lighting, same gradient, same colour temperature so the split test isolates composition."
        ),
        overlay="(one callout per option — see visual direction)",
        overlay_sub="3 hero options shipped — A/B test, keep the winner",
        props=[
            "OPTION A: elongated mask + full 2 m tubing in an S-curve + one sealed individual wrapper + spec badge strip",
            "OPTION B: mask on neutral grey face silhouette / mannequin profile + dimension caller + extended nose clip & elastic + fit badge",
            "OPTION C: mask + 2 m tubing with standard connector in focus + soft-focus home concentrator + works-with badge",
        ],
        lighting="Soft top key (5000K daylight balanced) with gentle fill from camera-right. Light backlight to separate the white mask from the white ground. Same lighting across all 3 options to keep the A/B test clean.",
        why_it_works=(
            "Three hero angles against the three pre-click questions for this category: A wins on the spec "
            "scan (and proves the 2 m tubing visually), B wins on the dominant sizing/fit fear, C wins on "
            "machine compatibility. One callout, one action cue, one prop each — readable on a mobile "
            "thumbnail, calm and clinical, never alarming."
        ),
        ctr="Leads with the buyer's exact spec questions (fit, 2 m tubing, pack of 5, works-with) as a badge on a white grid full of bare round masks — the proof-first thumbnail earns the click.",
        cvr="Each option pre-answers a purchase blocker (specs / sizing / compatibility), so the click arrives already reassured — the strongest lever is Option B defusing the 'too small' review fear.",
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: The full 2 m tubing, laid out",
        role="hook",
        background="Clinical white with a faint Endure-blue gridline floor for a measured, technical feel",
        purpose="Prove the 2 m / 6.8 ft reach visually and kill the 'tubing kinks / arrives bent' objection up front.",
        visual=(
            "Hero macro-to-wide of the full 2 m tubing laid out edge-to-edge in one smooth, deliberate "
            "curve, mask at one end, standard connector at the other. A clean dimension line runs the "
            "length labelled '2 m / 6.8 ft'. Add one small inset macro circle showing the smooth tubing "
            "wall flexing around a gentle bend WITHOUT pinching, to communicate kink resistance.\n\n"
            "Keep it calm and technical — no clutter, soft-blue accents only. The visual story is "
            "'long enough to move, smooth enough to stay open.'"
        ),
        overlay="2 M OF SMOOTH, KINK-RESISTANT TUBING",
        overlay_sub="6.8 ft of reach — move, sit up or rest while staying connected.",
        props=["full 2 m tubing in one smooth curve", "mask at one end", "standard connector at the other end", "dimension line '2 m / 6.8 ft'", "inset macro of tubing flexing without pinching"],
        lighting="Even soft front-light with a low raking light to catch the smooth tubing wall. Clarity over drama — this is an educational hook.",
        why_it_works=(
            "Turns the most common negative review (kinked / bent tubing) into the lead selling point. "
            "Showing the full length laid flat proves the 2 m claim that competitors only assert in text, "
            "and the inset flex macro directly answers the kink fear before it becomes a return."
        ),
        ctr="A single clean line of tubing with a 2 m dimension callout is unusual in this grid — it reads as a spec proof and pulls the spec-driven shopper in.",
        cvr="Directly neutralises the top tubing objection (kinks / bent on arrival), removing the main reason buyers hesitate or return.",
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: Elongated coverage + real dimensions (defuse sizing)",
        role="educate",
        background="White with a soft Endure-blue ribbon footer",
        purpose="Answer 'will it fit my face?' with the elongated shape and actual dimensions, side by side with a short round mask.",
        visual=(
            "Headline top: 'ELONGATED COVERAGE, BUILT FOR ADULT FACES' in Endure blue, sentence case.\n\n"
            "LEFT 55%: the elongated mask overlaid on a neutral grey adult face profile (no real face), "
            "showing coverage from the nose bridge to below the chin. Clean dimension callers mark mask "
            "height and width (designer to fill the verified measured values). A small arrow highlights "
            "the adjustable aluminium nose strip conforming over the nose.\n\n"
            "RIGHT 45%: a small, faded silhouette of a typical SHORT ROUND mask for scale contrast "
            "(generic, unbranded) so the elongated advantage is obvious. Caption: 'Elongated shape = "
            "more adult-face coverage than short round masks.'\n\n"
            "Footer ribbon (Endure blue): 'Adjustable nose strip + elastic strap let you fine-tune the fit.'"
        ),
        overlay="BUILT FOR ADULT FACES",
        overlay_sub="Elongated nose-to-chin coverage, plus an adjustable nose strip and elastic strap to fine-tune the fit.",
        props=["elongated mask on neutral grey adult face profile", "dimension callers (height + width)", "faded short-round mask silhouette for scale", "arrow on adjustable nose strip"],
        lighting="Flat clean studio. Educational module — readability beats atmosphere.",
        why_it_works=(
            "Sizing/fit is the #1 negative review theme ('too small even when adult/XL'). This frame puts "
            "the elongated coverage and real dimensions on a face silhouette so the buyer self-confirms it "
            "will fit before purchase — the highest-leverage CVR move in the plan."
        ),
        ctr="The face-profile coverage diagram signals 'this brand answers the fit question,' which differentiates from spec-only thumbnails.",
        cvr="Lets the buyer measure the fit against their own face up front, removing the sizing uncertainty that drives this category's returns.",
    ),
    AIImagePlanItem(
        name="Image 4 — Desire: Comfort for extended & overnight wear",
        role="desire",
        background="Calm home setting, soft warm-neutral light, soft-blue accents — restful, not clinical-cold",
        purpose="Show soft medical-grade PVC + padded edges + adjustable fit as comfortable for long and overnight sessions.",
        visual=(
            "Calm bedside or armchair scene at soft evening light. The elongated mask rests on a clean "
            "neutral surface beside a glass of water, tubing trailing softly toward a soft-focus "
            "concentrator. Macro inset (top-right): the smooth, soft PVC edge and the elastic strap, "
            "highlighting the gentle contact surface. A small hand (fingers only, no face) lightly "
            "adjusts the aluminium nose strip.\n\n"
            "Mood: restful, dignified, comfortable — a person could wear this through the night. No "
            "distress, no clinical sterility."
        ),
        overlay="COMFORTABLE FOR LONGER, OVERNIGHT WEAR",
        overlay_sub="Soft medical-grade PVC with smooth edges and an adjustable strap for a gentle, secure hold.",
        props=["elongated mask on neutral bedside surface", "glass of water", "tubing toward soft-focus concentrator", "macro inset of soft PVC edge + elastic strap", "hand (fingers only) adjusting nose strip"],
        lighting="Soft warm evening side-light with a gentle fill. Hair-light glint on the PVC edge in the macro inset. Honest, restful, never alarming.",
        why_it_works=(
            "Edge comfort during extended / sleep use is a recurring complaint. Pairing the restful "
            "overnight scene with a macro of the soft PVC edge and adjustable strap makes comfort "
            "tangible, supporting the 'oxygen mask for sleeping' search intent in the data."
        ),
        ctr="The calm overnight scene signals comfort, standing out from cold product-only thumbnails for the 'mask for sleeping' searcher.",
        cvr="The soft-edge macro plus adjustable strap answers the extended-wear comfort objection that otherwise blocks repeat and overnight buyers.",
    ),
    AIImagePlanItem(
        name="Image 5 — Trust: 4 quality credentials in one frame",
        role="trust",
        background="White with soft Endure-blue panels behind each badge for separation",
        purpose="Stack the proof points caregivers scan for and signal who already relies on Endure.",
        visual=(
            "Centered macro of the elongated mask + connector. Four trust badges in the corners:\n\n"
            "  • TOP-LEFT — LATEX-FREE (small shield / drop icon)\n"
            "  • TOP-RIGHT — SOFT MEDICAL-GRADE PVC (small material icon)\n"
            "  • BOTTOM-LEFT — INDIVIDUALLY WRAPPED · PACK OF 5 (small sealed-pouch icon)\n"
            "  • BOTTOM-RIGHT — STANDARD UNIVERSAL CONNECTOR (small connector icon)\n\n"
            "Below the mask, a thin Endure-blue strip: 'Trusted by medical professionals, EMS and the "
            "US Military. For use under the guidance of a medical professional.'"
        ),
        overlay="CLINICAL-GRADE, LATEX-FREE",
        overlay_sub="Soft medical-grade PVC · Individually wrapped, pack of 5 · Trusted by EMS and the US Military.",
        props=["elongated mask + connector (center)", "4 corner badge graphics", "thin supporting strip with provenance + medical-guidance line"],
        lighting="Studio even light. Clean catch-light on the connector. Badges legible at thumbnail size.",
        why_it_works=(
            "Stacks the four reassurance filters a caregiver scans (latex-free, material quality, hygienic "
            "packaging, compatibility) and adds credible provenance (EMS / US Military) — the strongest "
            "single trust signal for a medical-supply purchase, with the required medical-guidance line."
        ),
        ctr="Four credible badges plus EMS / US Military provenance read as 'legitimate medical supply,' lifting click confidence over unbranded look-alikes.",
        cvr="Bundles the trust filters that decide a medical-accessory purchase, closing the 'is this brand legit?' gap right before checkout.",
    ),
    AIImagePlanItem(
        name="Image 6 — Desire: Pack of 5, individually wrapped",
        role="desire",
        background="Clinical white with a soft Endure-blue floor tint — same family as Image 2 for rhythm",
        purpose="Make the pack-of-5 value and hygiene obvious, and quietly clear the reusable-vs-single confusion.",
        visual=(
            "Clean flat-lay: five sealed, individually wrapped masks fanned in a neat row, with one mask "
            "unwrapped in front showing it ready to use, tubing coiled neatly beside it. A small label "
            "strip: '5 INDIVIDUALLY WRAPPED MASKS — rotate, travel, or keep spares on hand.'\n\n"
            "Add a small, calm note panel: 'Each mask is sealed for hygiene — open one when you need it.' "
            "Keep it tidy and reassuring — communicate value and cleanliness, not clutter."
        ),
        overlay="5 SEALED MASKS, READY WHEN YOU NEED THEM",
        overlay_sub="Individually wrapped for hygiene — rotate, travel, or keep spares on hand.",
        props=["five sealed individually wrapped masks fanned in a row", "one unwrapped mask ready to use", "neatly coiled tubing", "hygiene note panel"],
        lighting="Even soft front-light, clean flat-lay shadows. Hygienic, organised feel.",
        why_it_works=(
            "Multi-pack value and individual wrapping are both praised in reviews. Showing the sealed five "
            "plus one ready-to-use mask makes the value tangible and quietly answers the reusable-vs-single "
            "and 'how many do I get?' confusion that surfaces in feedback."
        ),
        ctr="A neat fan of five sealed masks signals stock-up value and hygiene at a glance, attractive to caregivers buying for ongoing use.",
        cvr="Clarifies exactly what arrives (5 sealed masks) and reinforces hygiene, removing the pack-count and reusable-vs-single confusion before purchase.",
    ),
    AIImagePlanItem(
        name="Image 7 — Close: Works with your existing setup",
        role="close",
        background="Calm home-oxygen scene, soft daylight, soft-blue tones",
        purpose="Close on 'it just works with what you already have' and leave the buyer reassured.",
        visual=(
            "Mid-range home scene: the elongated mask + 2 m tubing connected to a home oxygen "
            "concentrator on a side table, a nebulizer beside it to signal dual compatibility. Tubing "
            "runs neatly toward a comfortable armchair (empty or with a hand/arm only — no face in "
            "distress). Calm, dignified, lived-in home, not a hospital.\n\n"
            "Foreground: a small Endure info card reading 'Standard universal connector — drops into your "
            "concentrator, tank or nebulizer. For use under the guidance of a medical professional.'"
        ),
        overlay="FITS YOUR CONCENTRATOR & NEBULIZER",
        overlay_sub="Standard universal connector — no adapters. For use under the guidance of a medical professional.",
        props=["elongated mask + 2 m tubing connected to a home concentrator", "nebulizer beside it", "comfortable armchair (empty / hand only)", "Endure info card with medical-guidance line"],
        lighting="Soft natural daylight from a window, gentle and warm. Honest home setting — calm, never alarming.",
        why_it_works=(
            "Closes on the compatibility reassurance the buyer needs before checkout — the mask drops into "
            "the equipment they already own with no adapters — while the required medical-guidance line "
            "keeps the close compliant and trustworthy."
        ),
        ctr="The home-setup scene with both a concentrator and a nebulizer signals 'this works with my machine,' a strong final pull for the compatibility searcher.",
        cvr="Confirms zero-adapter compatibility with the buyer's existing equipment and adds the medical-guidance reassurance, removing the last hesitation at checkout.",
    ),
]


MODULES = [
    AIModule(
        name="Module 1 — Brand banner: Medical-grade oxygen delivery.",
        role="a+_banner",
        headline="MEDICAL-GRADE OXYGEN DELIVERY",
        body=(
            "Endure Industries builds clinical-quality oxygen-delivery accessories trusted by medical "
            "professionals, EMS and the US Military. The Elongated Oxygen Mask pairs an adult-coverage "
            "shape with a full 2 m of standard tubing for calm, reliable home oxygen delivery. For use "
            "under the guidance of a medical professional."
        ),
        visual="Wide cinematic clinical-home scene — the elongated mask + full 2 m tubing laid clean across a soft-blue surface, an Endure-blue logo upper-left, a soft-focus home concentrator at the right edge. Calm, professional, never alarming.",
        alt="Endure Industries Elongated Oxygen Mask with 2 m tubing laid out on a clean clinical surface beside a home oxygen concentrator.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): The Endure Difference",
        role="a+_carousel",
        headline="THE ENDURE DIFFERENCE",
        body=(
            "Tile 1: <b>ELONGATED ADULT FIT</b> — Nose-to-chin coverage with an adjustable nose strip "
            "&amp; elastic strap.<br/>"
            "Tile 2: <b>2 M / 6.8 FT TUBING</b> — Smooth, kink-resistant length for room to move.<br/>"
            "Tile 3: <b>LATEX-FREE PVC</b> — Soft, medical-grade material, gentle for longer wear.<br/>"
            "Tile 4: <b>WORKS WITH YOUR MACHINE</b> — Standard universal connector for concentrators, "
            "tanks &amp; nebulizers.<br/>"
            "Tile 5: <b>PACK OF 5</b> — Individually wrapped for hygiene and spares on hand."
        ),
        visual="5 square tiles, Endure-blue accent corner on each, consistent composition. Small icons (face-coverage outline · tubing coil · material drop · connector · sealed pouch).",
        alt="Five-tile A+ carousel covering Endure Elongated Oxygen Mask differentiators: elongated adult fit, 2 m tubing, latex-free PVC, universal connector, pack of 5.",
    ),
    AIModule(
        name="Module 3 — Banner: Built to fit adult faces",
        role="a+_banner",
        headline="BUILT TO FIT ADULT FACES",
        body=(
            "The elongated shape covers from the bridge of the nose to below the chin for fuller adult "
            "coverage than short, round masks. An adjustable aluminium nose strip conforms over the nose "
            "and an elastic head strap fine-tunes the hold, so the mask sits securely with less slipping "
            "during everyday home oxygen delivery."
        ),
        visual="Wide banner: the elongated mask overlaid on a neutral grey adult face profile (no real face) with clean dimension callers for height and width, an arrow on the adjustable nose strip, and a faded short-round mask silhouette for scale contrast. Endure-blue palette only.",
        alt="A+ banner showing the elongated oxygen mask coverage on a neutral adult face profile with dimension callouts and an adjustable nose strip.",
    ),
    AIModule(
        name="Module 4 — Banner: 2 m tubing, smooth and kink-resistant",
        role="a+_banner",
        headline="2 M OF SMOOTH, KINK-RESISTANT TUBING",
        body=(
            "The included 2-meter (6.8 ft) standard oxygen tubing gives room to sit up, move or rest while "
            "staying connected. Smooth-wall tubing is made to resist kinking and stay flexible so oxygen "
            "delivery stays steady and uninterrupted. The standard connector links to common "
            "concentrators, tanks and nebulizers."
        ),
        visual="Wide banner: the full 2 m tubing laid out in one smooth curve with a '2 m / 6.8 ft' dimension line, plus an inset macro of the tubing flexing around a bend without pinching. Soft-blue technical background.",
        alt="A+ banner showing the full 2 m oxygen tubing laid out with a dimension line and a macro inset of kink-resistant flexing.",
    ),
    AIModule(
        name="Module 5 — Premium Q&A",
        role="a+_qa",
        headline="QUESTIONS BUYERS ASK",
        body=(
            "<b>Q.</b> Will it fit an adult face?<br/>"
            "<b>A.</b> Yes. The elongated shape is designed for adult coverage from the nose bridge to "
            "below the chin, and the adjustable aluminium nose strip plus elastic head strap let you "
            "fine-tune the fit to your own face.<br/><br/>"

            "<b>Q.</b> How long is the tubing?<br/>"
            "<b>A.</b> Each mask includes a full 2 m (6.8 ft) of standard oxygen tubing — smooth-wall and "
            "made to resist kinking — so you have room to move or rest while staying connected.<br/><br/>"

            "<b>Q.</b> Does it work with my concentrator or nebulizer?<br/>"
            "<b>A.</b> The standard universal connector fits common home and clinical oxygen "
            "concentrators, oxygen tanks and nebulizers, so it drops into your existing setup with no "
            "adapters.<br/><br/>"

            "<b>Q.</b> Is it comfortable for longer or overnight use?<br/>"
            "<b>A.</b> The mask is made from soft, medical-grade PVC with smooth edges, and the adjustable "
            "strap helps keep a gentle, secure hold for extended wear.<br/><br/>"

            "<b>Q.</b> Is it latex-free?<br/>"
            "<b>A.</b> Yes. The mask is made from latex-free, soft medical-grade PVC.<br/><br/>"

            "<b>Q.</b> How many masks come in the pack?<br/>"
            "<b>A.</b> Five masks per pack, each individually wrapped for hygiene — handy for rotation, "
            "travel or keeping spares on hand. For use under the guidance of a medical professional."
        ),
        visual="Vertical Q/A table. Endure-blue divider lines between each Q. Small Endure-blue Q. and A. labels.",
        alt="Premium Q&A module addressing the most-asked buyer questions for the Endure Elongated Oxygen Mask.",
    ),
    AIModule(
        name="Module 6 — Premium Comparison Chart",
        role="a+_comparison",
        headline="WHY ENDURE",
        body=(
            "Compare across 4 columns: <b>Endure Elongated Oxygen Mask</b> · Short round oxygen mask · "
            "Single-mask pack · Mask without tubing.<br/><br/>"
            "Rows: Mask shape (elongated adult coverage) · Tubing included (2 m / 6.8 ft) · "
            "Kink-resistant smooth-wall tubing · Adjustable nose strip &amp; elastic strap · Latex-free "
            "medical-grade PVC · Standard universal connector · Individually wrapped · Masks per pack (5).<br/><br/>"
            "Highlight the Endure column with a soft Endure-blue tint and a 'CLINICAL-GRADE' ribbon at "
            "the top of the column."
        ),
        visual="Standard Amazon Premium Comparison Chart layout, 4 product columns. Competitor columns use category descriptors only — no brand names. Endure-blue header row.",
        alt="Premium comparison chart for the Endure Elongated Oxygen Mask vs. a short round mask, a single-mask pack, and a mask without tubing.",
    ),
    AIModule(
        name="Module 7 — Banner: Trusted clinical supply",
        role="a+_banner",
        headline="TRUSTED BY PROFESSIONALS",
        body=(
            "Endure Industries supplies medical professionals, EMS, clinics and the US Military. Every "
            "Elongated Oxygen Mask is built from latex-free, soft medical-grade PVC and individually "
            "wrapped for hygiene, in a pack of 5. For use under the guidance of a medical professional."
        ),
        visual="Wide banner: the elongated mask + connector centered on clean white with four small trust badges (latex-free · medical-grade PVC · individually wrapped · standard connector) and a soft Endure-blue provenance strip. Calm, professional.",
        alt="A+ banner showing Endure trust credentials: latex-free, medical-grade PVC, individually wrapped, standard connector, trusted by EMS and the US Military.",
    ),
]


QA = [
    AIQA(q="Will it fit an adult face?",
         a="Yes. The elongated shape is designed for adult coverage from the nose bridge to below the chin, and the adjustable aluminium nose strip plus elastic head strap let you fine-tune the fit to your own face for a secure, low-slip hold."),
    AIQA(q="How long is the tubing?",
         a="Each mask includes a full 2 m (6.8 ft) of standard oxygen tubing. The smooth-wall tubing is made to resist kinking and stay flexible, so you have room to move, sit up or rest while staying connected."),
    AIQA(q="Does it work with my oxygen concentrator or nebulizer?",
         a="Yes. The standard universal connector fits common home and clinical oxygen concentrators, oxygen tanks and nebulizers, so the mask drops into your existing setup with no adapters."),
    AIQA(q="Is it comfortable for longer or overnight use?",
         a="The mask is made from soft, medical-grade PVC with smooth edges for comfortable wear, and the adjustable strap helps keep a gentle, secure hold during extended or overnight sessions."),
    AIQA(q="Is the mask latex-free?",
         a="Yes. The mask is made from latex-free, soft medical-grade PVC for added peace of mind."),
    AIQA(q="What does the tubing connect to?",
         a="The tubing ends in a standard universal connector that links to common oxygen concentrators, oxygen tanks and nebulizers — no adapters needed."),
    AIQA(q="How many masks are in the pack?",
         a="Five masks per pack, each individually wrapped for hygiene — handy for rotation, travel or keeping spares on hand. For use under the guidance of a medical professional."),
]


# Backend KWs — stem-deduped, byte-packed. Avoid: brand name already in title, superlatives.
# Includes a couple of Spanish terms because the listing shows ES search demand.
# NOTE: backend is NOT scanned for compliance, so equipment/category terms are safe here.
BACKEND = (
    "oxygen mask tubing adult face concentrator nebulizer o2 medical grade pvc latex free elongated "
    "adjustable nose clip elastic strap pack of 5 individually wrapped standard connector 6.8 ft 2 meter "
    "breathing respiratory home tank sleeping replacement kit "
    "mascara de oxigeno adultos mascarilla para nebulizador"
)


def main() -> None:
    print("Loading Endure Industries customer + parsing Elongated Oxygen Mask Excel…")
    cust = load_customer("endure_industries")
    brief = parse_excel(EXCEL)
    asin = brief.asin or ASIN
    OUT = HERE / f"{PLAN_NO}_{ASIN}_Image Plan.pdf"
    print(f"  Product: {brief.product_name}")
    print(f"  ASIN: {brief.asin}  Marketplace: {cust.marketplace}")
    print(f"  USPs={len(brief.usps)} KWs={len(brief.all_keywords)} reviews=+{len(brief.good_reviews)}/-{len(brief.bad_reviews)}")
    real_title_len = len(TITLE.replace('&amp;', '&'))
    print(f"  TITLE real length: {real_title_len} (<=200 required)")

    builder = BriefBuilder(cust, brief, OUT, ai=None)
    builder._ai_title = TITLE
    builder._ai_bullets = BULLETS
    builder._ai_images = IMAGES
    builder._ai_modules = MODULES
    builder._ai_qa = QA
    builder._ai_backend = BACKEND
    builder.copy_source_label = "Hand-written senior copy (KW-led, medical-compliant)"

    print("Building branded PDF…")
    pdf_path = builder.build()
    size_kb = pdf_path.stat().st_size // 1024
    import re
    pages = len(re.findall(rb'/Type\s*/Page[^s]', pdf_path.read_bytes()))
    print(f"Built: {pdf_path}")
    print(f"  Pages: {pages}  Size: {size_kb} KB")


if __name__ == "__main__":
    main()
