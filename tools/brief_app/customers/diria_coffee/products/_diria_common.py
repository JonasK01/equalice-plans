"""CAFÉ DIRIÁ — shared image/A+ regie for the 'Proceso Matambú' listing.

One creative source of truth for BOTH Amazon variants (client rule: the SEO sheet has
multiple variant tabs -> plan for all). The only differences between variants are the
FORMAT (Whole Bean vs Ground): one hero badge, image 5, one A+ line and one Q&A answer.
Everything else (origin, Matambú process, flavor, sustainability, brand close) is shared.

SEO title/bullets/backend come 1:1 from the per-variant SEO sheet (seo_loader); the
bildregie/overlays are hand-written (EN), warm/artisanal/specialty. new_brand=true ->
7 A+ modules, NO Comparison, Q&A = finale, Module 6 = values banner + smart Q&A bridge.
COMPLIANCE: 'Blue Zone' only as ORIGIN (no health/longevity claim), no blank superlatives,
no organic-cert claim, barrel/alcoholic fermentation = process only, no prices/URLs.
"""
from __future__ import annotations
from tools.brief_app.core.ai import AIImagePlanItem, AIModule, AIQA

# per-variant strings
FMT = {
    "whole_bean": {
        "label": "Whole Bean",
        "hero_badge": "WHOLE BEAN · 12 OZ",
        "b5_overlay": "GRIND FRESH, YOUR WAY.",
        "b5_sub": "Whole bean — grind only what you need, for a fresher cup every time.",
        "b5_purpose": "Show the whole-bean benefit: freshness and control over the grind.",
        "b5_visual": (
            "Whole roasted beans spilling warmly from the open 12 oz bag next to a grinder and a "
            "fresh brew. Callouts: 'Grind only what you need', 'Freshness in every cup', "
            "'Adjust the grind to your brew method'. Warm, tactile, appetising."
        ),
        "b5_props": ["open bag + whole beans", "grinder", "fresh brewed cup", "'grind what you need' callout"],
        "brew_line": "Whole bean: grind only what you need and dial in your brew — pour-over, drip or espresso.",
        "qa_format": ("Is this whole bean or ground?",
                      "This listing is the WHOLE BEAN format, so you control the grind for any brew "
                      "method. The same coffee is also offered pre-ground if you prefer convenience."),
    },
    "ground": {
        "label": "Ground",
        "hero_badge": "GROUND · 12 OZ",
        "b5_overlay": "READY FOR YOUR ROUTINE.",
        "b5_sub": "Pre-ground — measure, brew, enjoy. Fresh flavor, everyday convenience.",
        "b5_purpose": "Show the ground benefit: convenient, ready for the daily routine.",
        "b5_visual": (
            "Fresh grounds tumbling from the open 12 oz bag into a scoop, next to a brewed cup and "
            "a filter/drip setup. Callouts: 'Ready to brew', 'Measure & go', 'Fresh flavor, "
            "everyday convenience'. Warm, tactile, appetising."
        ),
        "b5_props": ["open bag + ground coffee", "scoop", "drip/filter + brewed cup", "'ready to brew' callout"],
        "brew_line": "Ground: measure what you need and brew — ideal for drip and filter, ready in minutes.",
        "qa_format": ("Is this ground or whole bean?",
                      "This listing is the GROUND format — measure, brew and enjoy, no grinder needed. "
                      "The same coffee is also offered as whole bean if you prefer to grind fresh."),
    },
}


def build(fmt: str):
    f = FMT[fmt]

    IMAGES = [
        AIImagePlanItem(
            name="Image 1 — Main Hero (3 variants to A/B test)",
            role="hero",
            background="Warm cream #F4ECE0 with soft daylight and a subtle shadow. Identical across all 3 variants for a clean split-test.",
            purpose="Win the click — an appetising, premium main that also signals single-origin specialty (fixes the weak main-image / CTR issue).",
            visual=(
                "Mock all 3. Product exactly as real: the 12 oz (340 g) Diriá 'Proceso Matambú' bag, "
                f"front label readable, styled with real {f['label'].lower()} coffee and a warm brewed "
                "cup. One statement each, product dominant ~70%. Warm, artisanal, appetising. Amazon "
                "slot 1 stays product-only.\n\n"
                "VARIANT A — MAIN WITH SHADOW: the bag hero, a few beans/grounds + a cup, soft shadow. "
                "Badge cluster (small): 'SINGLE ORIGIN' · 'NICOYA BLUE ZONE'.\n"
                "VARIANT B — CTR / WITH TASTING NOTES: the bag surrounded by its flavor cues — cocoa, "
                "cherry, blueberry, a drizzle of honey. Badge: 'COCOA · CHERRY · BLUEBERRY'.\n"
                f"VARIANT C — FORMAT: bag with {f['label'].lower()} coffee + cup. Badge: '{f['hero_badge']}'.\n\n"
                "Across all 3: product ~70%, badge ~6%, same warm light."
            ),
            overlay="(one statement per variant)",
            overlay_sub="3 hero variants — A/B test, keep the winner.",
            props=["A: bag + beans/grounds + cup, soft shadow", "B: bag + cocoa/cherry/blueberry/honey cues", f"C: bag + cup + '{f['hero_badge']}'"],
            lighting="Warm natural daylight, gentle shadow, rich but appetising. Identical across all 3.",
            why_it_works=(
                "Three click triggers: A specialty provenance (single origin, Blue Zone), B the "
                "craveable flavor, C the exact format — one clear idea each, instantly readable, and a "
                "more appetising main than a plain pack shot."
            ),
        ),
        AIImagePlanItem(
            name="Image 2 — Origin: grown in a Costa Rican Blue Zone",
            role="hook",
            background="Warm Guanacaste landscape / highland coffee farm, cream framing",
            purpose="Lead with the strongest premium hook: single origin from the Nicoya Blue Zone, cooperative since 1962.",
            visual=(
                "A warm origin scene: highland shade-coffee in the Nicoya Peninsula, the bag resting in "
                "the foreground. A small, tasteful map pin marks Nicoya, Costa Rica. Callouts: "
                "'Nicoya Peninsula, Costa Rica — a recognized Blue Zone', '700–1,000 m, 100% Arábica', "
                "'Grown by the Coopepilangosta cooperative since 1962'. HINT: Blue Zone as ORIGIN only "
                "(no health promise)."
            ),
            overlay="GROWN IN A BLUE ZONE.",
            overlay_sub="Single origin from Costa Rica's Nicoya Peninsula — cooperative-grown since 1962.",
            props=["highland shade-coffee scene", "Costa Rica / Nicoya map pin", "bag in foreground", "'since 1962' cue"],
            lighting="Warm, golden natural light; authentic, rooted, premium.",
            why_it_works=(
                "Provenance is the #1 reason to pay a specialty price. A real, recognized origin plus a "
                "60-year cooperative story justify the premium and set the brand apart from generic coffee."
            ),
            cvr="Anchors the premium in a verifiable, distinctive origin story.",
        ),
        AIImagePlanItem(
            name="Image 3 — The Matambú Process (the signature)",
            role="educate",
            background="Clean cream, warm step-by-step layout",
            purpose="Explain the rare process that creates the complex cup — the craft that justifies the price.",
            visual=(
                "A warm 4-step visual of the signature MATAMBÚ process (inspired by the Chorotega/"
                "Matambú Indigenous traditions):\n"
                "1. ANAEROBIC PRE-FERMENT — cherries ferment while still whole.\n"
                "2. FIRST SUN-DRYING — dried on raised beds in the sun.\n"
                "3. BARREL FERMENTATION — an alcoholic fermentation in barrels.\n"
                "4. SECOND SUN-DRYING — dried again to lock in character.\n"
                "Small note: 'A rare, hands-on process — the reason for the complex flavor.' Authentic, "
                "artisanal icons; process only (not 'boozy')."
            ),
            overlay="THE MATAMBÚ PROCESS.",
            overlay_sub="Anaerobic ferment · sun-dry · barrel ferment · sun-dry — the craft behind the cup.",
            props=["4-step process icons", "coffee cherries", "raised drying beds", "fermentation barrels"],
            lighting="Warm, documentary-style daylight; craft and hands visible.",
            why_it_works=(
                "Buyers pay more when they understand the craft. Showing the rare four-step process makes "
                "the complexity believable and the price make sense."
            ),
            cvr="Turns an abstract 'specialty' claim into visible, ownable craft.",
        ),
        AIImagePlanItem(
            name="Image 4 — A bold, layered cup (flavor profile)",
            role="desire",
            background="Warm cream flat-lay, tasting-note styling",
            purpose="Make the complex flavor vivid — directly answers the 'too mild / notes hard to detect' objections.",
            visual=(
                "Appetising flavor flat-lay around a brewed cup: cocoa, cherry, blueberry, a drizzle of "
                "Carao honey, a hint of cardamom. Simple sensory meters shown honestly from the catalog: "
                "'Body 5/5 · Aroma 4/5 · Acidity 3/5' with a small 'Bold, not mild' cue. Callout of the "
                "tasting notes: 'Cardamom liqueur · Cocoa · Cherry · Blueberry · Carao honey'."
            ),
            overlay="A BOLD, LAYERED CUP.",
            overlay_sub="Cocoa, cherry, blueberry & Carao honey — full-bodied, layered, distinctive.",
            props=["brewed cup", "cocoa/cherry/blueberry/honey styling", "body-aroma-acidity meters", "tasting-note callout"],
            lighting="Warm, appetising light; deep coffee tones, fresh fruit accents.",
            why_it_works=(
                "The most common category complaint is 'weak/ordinary'. Showing a full-bodied (5/5), "
                "clearly layered profile pre-empts that doubt and makes the cup feel worth it."
            ),
            cvr="Sets accurate, appetising flavor expectations → fewer 'too mild' letdowns.",
        ),
        AIImagePlanItem(
            name=f"Image 5 — {f['label']}: {f['b5_overlay'].rstrip('.')}",
            role="desire",
            background="Warm cream, product-in-use",
            purpose=f['b5_purpose'],
            visual=f['b5_visual'],
            overlay=f['b5_overlay'],
            overlay_sub=f['b5_sub'],
            props=f['b5_props'],
            lighting="Warm, tactile light; texture of beans/grounds and a fresh cup.",
            why_it_works=(
                "The format is why this exact variant is chosen. Showing it in use (and hinting at "
                "freshness) answers the 'stale/old roast' worry and makes the daily use obvious."
            ),
            cvr="Confirms the format benefit and freshness — reassures on the everyday experience.",
        ),
        AIImagePlanItem(
            name="Image 6 — Grown the right way (people & planet)",
            role="trust",
            background="Warm highland farm, cream framing + trust band",
            purpose="Justify the premium through values: shade-grown, cooperative, 192 families, sustainability.",
            visual=(
                "Warm, real scene of cooperative farmers / shade-grown agroforestry. Icon row: "
                "'Shade-grown in agroforestry', 'Supports biodiversity, soil & water', "
                "'192 producer families', 'Cooperative since 1962'. Small trust band: "
                "'Café Diriá · Coopepilangosta · Nicoya, Costa Rica'. Honest, dignified, no clichés."
            ),
            overlay="SHADE-GROWN SINCE 1962.",
            overlay_sub="Agroforestry that protects the land — and 192 cooperative families behind every bag.",
            props=["cooperative farmers / shade coffee", "sustainability icon row", "'192 families' cue", "trust band"],
            lighting="Warm, honest daylight; community and nature visible.",
            why_it_works=(
                "Values are a real premium driver for specialty buyers. Shade-grown farming and a "
                "60-year cooperative give the price meaning beyond the cup."
            ),
            cvr="Adds ethical/quality value that supports the premium and builds trust.",
        ),
        AIImagePlanItem(
            name="Image 7 — Your new daily ritual (brand close)",
            role="close",
            background="Cozy warm home moment, soft daylight",
            purpose="Close emotionally on the ritual and the brand — deliberately different from image 6 (values).",
            visual=(
                "A calm, inviting home moment: warm hands around a fresh cup, the Diriá bag nearby, "
                "morning light. It's about the FEELING — slow down, savour something distinctive. "
                "Subtle brand line at the base: 'Café Diriá — single-origin Costa Rican coffee, "
                "with you since 1962.'"
            ),
            overlay="SLOW DOWN. SIP BETTER.",
            overlay_sub="Café Diriá — a more distinctive daily coffee ritual, from the Nicoya Blue Zone.",
            props=["hands around a warm cup", "Diriá bag nearby", "morning light", "brand line"],
            lighting="Warm, soft, emotional home light; premium and calm.",
            why_it_works=(
                "Ends on the emotional reward and the brand — the deliberately warmer, human close after "
                "the factual values image (no second badge shot)."
            ),
        ),
    ]

    MODULES = [
        AIModule(
            name="Module 1 — Brand banner (LOGO start)",
            role="a+_banner",
            headline="SINGLE-ORIGIN COSTA RICAN COFFEE",
            body=(
                "Café Diriá 'Proceso Matambú' is a single-origin Costa Rican coffee grown by our "
                "cooperative in the Nicoya Peninsula — a recognized Blue Zone — at 700–1,000 m, "
                "shade-grown and crafted with the ancestral Matambú traditions. Slow down for a more "
                "distinctive daily cup."
            ),
            visual="Wide warm banner (970:600): Diriá bag + brewed cup on cream, headline left, Café Diriá logo top-left. Espresso brown + ochre accents.",
            alt="Café Diriá Proceso Matambú banner: single-origin Costa Rican coffee from the Nicoya Blue Zone.",
        ),
        AIModule(
            name="Module 2 — Carousel (5 tiles): Why this coffee",
            role="a+_carousel",
            headline="WHY THIS COFFEE",
            body=(
                "Tile 1: <b>SINGLE ORIGIN</b> — one origin, Nicoya Peninsula, Costa Rica.<br/>"
                "Tile 2: <b>BLUE ZONE</b> — grown in a recognized Blue Zone region.<br/>"
                "Tile 3: <b>MATAMBÚ PROCESS</b> — a rare barrel-fermented, sun-dried craft.<br/>"
                "Tile 4: <b>BOLD &amp; LAYERED</b> — cocoa, cherry, blueberry, Carao honey.<br/>"
                "Tile 5: <b>SHADE-GROWN</b> — agroforestry, cooperative since 1962."
            ),
            visual="5 square tiles on cream, ochre accent corner, warm line icons (origin pin · landscape · barrel · cup with notes · leaf).",
            alt="Five A+ tiles: single origin, Blue Zone, Matambú process, bold layered flavor, shade-grown.",
        ),
        AIModule(
            name="Module 3 — Banner: From the Nicoya Blue Zone",
            role="a+_banner",
            headline="FROM THE NICOYA BLUE ZONE",
            body=(
                "Every bean is grown in Costa Rica's Nicoya Peninsula — one of the world's five Blue "
                "Zones — between 700 and 1,000 metres, under natural shade. It is produced by "
                "Coopepilangosta, a cooperative supporting 192 local producer families, growing coffee "
                "here since 1962."
            ),
            visual="Warm 3-image split (300x300): highland shade farm · Costa Rica/Nicoya map · cooperative hands with cherries. Ochre captions.",
            alt="A+ banner: Café Diriá origin — Nicoya Peninsula Blue Zone, cooperative since 1962, 192 families.",
        ),
        AIModule(
            name="Module 4 — Banner: The Matambú Process (detailed)",
            role="a+_banner",
            headline="THE MATAMBÚ PROCESS",
            body=(
                "Named for the Matambú Indigenous heritage of Guanacaste, our signature process gives "
                "the cup its complexity — in four hands-on steps:<br/><br/>"
                "<b>1. Anaerobic pre-ferment</b> — the cherries ferment while still whole.<br/>"
                "<b>2. First sun-drying</b> — slowly dried on raised beds in the sun.<br/>"
                "<b>3. Barrel fermentation</b> — an alcoholic fermentation in barrels.<br/>"
                "<b>4. Second sun-drying</b> — dried again to lock in the character.<br/><br/>"
                "<i>A rare, careful process — the reason for the layered flavor in your cup.</i>"
            ),
            visual="Clean 4-step how-it's-made (icons: sealed cherries · drying beds · barrel · sun). Warm, artisanal, documentary feel.",
            alt="A+ how-it's-made: the Matambú process — anaerobic ferment, sun-dry, barrel ferment, sun-dry.",
        ),
        AIModule(
            name="Module 5 — Banner: Taste & brew",
            role="a+_banner",
            headline="TASTE & BREW",
            body=(
                "Expect a bold, layered cup — notes of cardamom liqueur, cocoa, cherry, blueberry and "
                "Carao honey, with citric acidity and a creamy body (full-bodied, not mild). "
                f"{f['brew_line']}"
            ),
            visual="Warm banner: brewed cup with cocoa/cherry/blueberry/honey styling on the left, simple body/aroma/acidity meters and a brew cue on the right.",
            alt="A+ banner: Café Diriá tasting notes and brewing guidance for a bold, layered cup.",
        ),
        AIModule(
            name="Module 6 — Banner: Grown the right way (values + Q&A bridge)",
            role="a+_banner",
            headline="GROWN THE RIGHT WAY",
            body=(
                "Café Diriá is shade-grown in agroforestry systems that protect biodiversity, soil and "
                "water, and produced through a cooperative that has supported local families in the "
                "Nicoya highlands since 1962. Buying this coffee supports 192 producer families and a "
                "more responsible way to farm — quality you can feel good about, cup after cup."
            ),
            visual="Warm banner: cooperative farmers / shade-grown agroforestry, sustainability icon row, small 'since 1962 · 192 families' trust band. Cream + ochre.",
            alt="A+ banner: shade-grown agroforestry, Coopepilangosta cooperative since 1962, 192 producer families.",
        ),
        AIModule(
            name="Module 7 — Premium Q&A",
            role="a+_qa",
            headline="FREQUENTLY ASKED",
            body=(
                f"<b>Q.</b> {f['qa_format'][0]}<br/>"
                f"<b>A.</b> {f['qa_format'][1]}<br/><br/>"
                "<b>Q.</b> What does it taste like — is it strong?<br/>"
                "<b>A.</b> A bold, full-bodied cup (body 5/5), not a mild one. Expect cardamom liqueur, "
                "cocoa, cherry, blueberry and Carao honey, with citric acidity and a creamy body.<br/><br/>"
                "<b>Q.</b> How is it processed?<br/>"
                "<b>A.</b> With the Matambú process: an anaerobic pre-fermentation in the cherry, first "
                "sun-drying, an alcoholic fermentation in barrels, then a second sun-drying.<br/><br/>"
                "<b>Q.</b> Where is it from and who grows it?<br/>"
                "<b>A.</b> Costa Rica's Nicoya Peninsula (a recognized Blue Zone), 700–1,000 m, 100% "
                "Arábica — grown by the Coopepilangosta cooperative (192 producer families) since 1962.<br/><br/>"
                "<b>Q.</b> How much coffee is in the bag?<br/>"
                "<b>A.</b> 12 oz (340 g). Keep the bag sealed between uses and check the pack for the "
                "roast or expiry date so you enjoy it at its freshest."
            ),
            visual="Vertical Q/A list on cream, ochre divider lines, small brown Q. and A. labels. Short answers; first Q addresses the format directly.",
            alt="Premium Q&A module for Café Diriá Proceso Matambú.",
        ),
    ]

    QA = [
        AIQA(q=f['qa_format'][0], a=f['qa_format'][1]),
        AIQA(q="What does it taste like — is it strong or mild?",
             a="It is a bold, full-bodied cup (body 5/5), not a mild one. Expect notes of cardamom liqueur, cocoa, cherry, blueberry and Carao honey, balanced by citric acidity, a creamy body and a fruity aroma."),
        AIQA(q="What is the Matambú process?",
             a="A rare four-step craft: an anaerobic pre-fermentation while the coffee is still in the cherry, a first sun-drying, an alcoholic fermentation in barrels, and a second sun-drying — the reason for the layered flavor."),
        AIQA(q="Where is the coffee from and who grows it?",
             a="From Costa Rica's Nicoya Peninsula — a recognized Blue Zone region — at 700–1,000 m, 100% Arábica, grown under natural shade by the Coopepilangosta cooperative, which supports 192 local producer families and has grown coffee here since 1962."),
        AIQA(q="How much is in the bag, and how do I keep it fresh?",
             a="Each bag holds 12 oz (340 g). Keep it sealed between uses and check the pack for the roast or expiry date so you can enjoy it at its freshest."),
    ]

    return IMAGES, MODULES, QA
