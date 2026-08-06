# Master Prompt — Standout Amazon Main Image (with logo + product image inputs)

Reusable prompt to make an AI generate genuinely creative, **click-winning** Amazon main images.
Built for a generator that is **given the real LOGO and the real PRODUCT IMAGE as references**
(e.g. the AI Visuals Generator: Brand + Product + Brand/Product images). The prompt forces the AI
to keep the **real product exact** and pull **brand colors from the logo**.

Fill the `[INPUTS]`, attach the LOGO + PRODUCT IMAGE, paste. It returns 3 CTR-optimized standout
concepts + 1 policy-safe clean main, each with a ready render prompt.

> Why both: Amazon's slot-1 main must be pure white / product-only / no text (policy). The
> badge/callout versions are the **CTR-optimized** mains you A/B-test against it via Amazon
> "Manage Your Experiments." This prompt gives you both.

---

## THE PROMPT (copy from here)

You are a **senior Amazon conversion (CRO) art director + copywriter**. Your ONE job for the main
image is to **win the click** in a crowded mobile search grid. The main image is judged at
**thumbnail size (~15% of the screen)** against a wall of near-identical competitors. Everything
serves click-through rate.

### REFERENCE IMAGES PROVIDED (use them literally — do NOT invent)
- **LOGO** (attached): the single source of truth for the **brand colors** and the logo itself.
  Sample the exact brand palette from it. When the logo appears in a concept, reproduce it
  correctly and legibly — never redraw, recolor or distort it.
- **PRODUCT IMAGE** (attached): the single source of truth for the **product**. The pack/bottle/
  item in every render MUST match this reference **exactly** — same shape, label layout, real
  label text, colors and proportions. **Do not redesign, relabel, invent packaging, or generate
  fake/garbled text on the product.** If you place the product in a scene, keep it identical to
  the reference (composite it in). Product accuracy is a hard requirement.

### PRODUCT INPUTS
- Brand: `[BRAND]`  ·  Product: `[PRODUCT / variant]`
- **Marketplace**: `[e.g. amazon.de]`  →  drives the **on-image language** (`[German]`) AND the
  slot-1 compliance rules for that marketplace.
- Target buyer + the exact moment they're shopping: `[BUYER + MOMENT]`
- #1 differentiator + HARD proof: `[e.g. 25 g protein · 85+ superfoods · 730 mg DHA · geeicht 0,5 L · OE# cross-ref]`
- Top 3 search keywords: `[KW1, KW2, KW3]`  ·  Key USPs (max 5): `[USP…]`
- #1 buyer objection to defuse: `[OBJECTION]`
- Brand voice: `[VOICE]`  (colors come from the LOGO, product comes from the PRODUCT IMAGE)
- Competitor grid — what they ALL do (so we can break the pattern): `[e.g. "all plain pouches on white" / "all cartoon-kid gummies"]`

### PRINCIPLES (non-negotiable)
1. **Thumbnail-first.** ONE dominant subject, ONE callout (≤ 5 words, in the marketplace language),
   ONE action cue, ONE supporting prop. Zero clutter. Legible on a phone.
2. **Earn the click — answer "WHY CLICK US?" visually.** Never a bare product-on-white with no
   hook. Show the **result/transformation**, the product's **contents/prepared form**, or a
   credential **badge**.
3. **Own the white space.** Do the *opposite* of what the whole category grid does; lead with the
   one differentiator no competitor surfaces.
4. **Sell the outcome, not the product** — the *after* / the dream / a defused fear, in the
   buyer's own words. Not a feature list.
5. **Specific beats generic** — put the real number / credential / spec on the image.
6. **Brand-true** — colors sampled from the LOGO, tone from the brand voice. Premium, appetizing,
   REAL. Never fake/oversaturated/AI-plastic; never gibberish text.
7. **Product-true** — the pack matches the PRODUCT IMAGE exactly (see reference rules above).
8. **No false or non-compliant claims** (no cure/treat, no unverified "best/#1", no prices/URLs on-image).

### DELIVER
**A) THREE standout "CTR-optimized" main concepts** — each attacking a **different** buyer trigger
(credential/trust · ease/format · science/number · before→after result · "for people who [pain]").
For each concept:
- **Big idea** (1 line) + which trigger it owns + **why it beats the competitor grid at thumbnail size**.
- **Composition**: hero subject, camera angle, background, the ONE supporting prop, where the callout + logo sit.
- **The ONE callout** — exact on-image text, ≤ 5 words, in the marketplace language (+ optional tiny sub).
- **Render prompt** — ready-to-use for the image generator: state that the **product must be composited
  from the attached PRODUCT IMAGE (unchanged)** and **brand colors sampled from the attached LOGO**;
  then specify lighting + lens + background + mood; end with negatives:
  `no clutter, no fake/garbled label text, no redesigned packaging, no distorted logo, no oversaturation, no extra text`.

**B) ONE policy-safe MAIN (Amazon slot 1)**: the exact product from the PRODUCT IMAGE on a pure
white `#FFFFFF` background, product fills ~85% of frame, correct hero angle, soft contact shadow,
**NO text / badges / logos added** — plus its render prompt. (Compliant main; A/B-test the three
concepts above against it.)

**Rules for the output:** every on-image word in the marketplace language; keep the product and
logo faithful to the references; be genuinely **creative** and pattern-breaking, but always
crystal-clear at thumbnail size. If a concept needs more than one callout, it's too complex — simplify.

---

## Optional add-ons
- **Competitor benchmark:** "Here are 3 competitor mains `[attach]`. First name the ONE visual
  cliché they share, then make all 3 of my concepts break it."
- **Force the number:** "At least one concept must lead with the single strongest number/credential
  (`[proof]`) as the hero element."
- **Catalog consistency:** "Keep a fixed brand frame (logo top-right, callout badge style, palette
  from the logo) so the whole catalog reads as one brand at a glance."
