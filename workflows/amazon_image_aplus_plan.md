# Amazon Listing Image & A+ Premium Content Plan

## Objective
Create a comprehensive, conversion-optimized image plan and A+ Premium content plan for an Amazon product listing. The output is a structured content brief that can be directly implemented in Figma.

---

## Where everything lives (READ FIRST)

This workflow is implemented by the **`tools/brief_app/`** engine. Each brand is one
persistent folder: `tools/brief_app/customers/<brand_slug>/`. See the
"Brands & Image Plans" section in `CLAUDE.md` for the full layout.

**Before any image-plan job, in this order:**
1. **Read `customers/<slug>/brand_study.md`** — the brand's voice, colors, fonts, photo
   rules, and no-gos. This is the canonical brandbook (auto-generated from `config.json`).
   It replaces the old "create a Google Doc brandbook" step in Phase 1 below — only build
   a fresh brandbook for a brand that has no `config.json` yet.
2. Put the SEO listing export as `customers/<slug>/products/<product>/listing.xlsx` (the "axis").
3. Build the plan in that product's `run.py` and generate `brief.pdf` (see CLAUDE.md steps).

> Note: the old per-product folders in `.tmp 2/` are retired. Do not author new plans there.

---

## Two brands per job (never confuse them)
- **EQUALICE** = our agency → the **deliverable's** look & feel (Orange #FA7C04 / Ink #0F1115 /
  Cream #FAF7F2 / Geist). The brief is an EQUALICE document. Handled automatically by the builder.
- **The client** (e.g. Nutripur) → shown as the **Brand Sheet** (Section 1, for the design team)
  and used for the **colors/fonts in the actual image specs**. Comes from `config.json`/`brand_study.md`.

## Creative directive (house rule — every image)
NEVER a bare product-on-white main with no hook. We are the experts: add **credential/quality
badges**, **show the product's contents** (e.g. capsules/pills), put **short messaging on the
product or on a badge**. Every main/hero must visually answer **"why click US?"** One callout,
one action cue, one supporting prop per image. (This rule is printed into every Brand Sheet.)

**Keep copy punchy — on-image text is a HEADLINE, not a sentence.** Hard limits (the builder
auto-lints every build and prints `⚠ COPY LENGTH` on a miss):
- `overlay` (on-image headline): **≤ 30 characters AND ≤ 5 words.** Strong words, glanceable.
- `overlay_sub`: ≤ 90 characters (one short supporting line).
- A+ module `headline`: ≤ 38 characters. Bullet head (`<b>…</b>`): ≤ 45 characters.
Put detail in the `visual`/`why_it_works` fields (designer-facing), NOT in the on-image text.

**Sell the outcome, not the action.** Lead the on-image copy with the RESULT the buyer wants
(the after / transformation / emotion / a defused fear) — not the steps they perform. Avoid
weak generic payoffs ("clean", "good"). Process-listing ("Spray. Rub. Clean.") is weak; the
result ("Like new — in minutes.") sells. Be specific; add a little tension→resolution.

**Short ≠ choppy — it must still read smoothly.** A punchy overlay is a polished micro-phrase,
NOT a telegraphic fragment. Avoid gimmicky "Word? Word." constructions and over-clipped 2-word
stubs that sound abrupt (DE example: "Risse? Vorbei." reads choppy → "Schluss mit Rissen."
reads round). Keep within the char limits, but make every overlay sound natural when read aloud.

**Language split (per job):**
- **English** = all designer/strategy fields: `purpose`, `background`, `visual` (art direction),
  `props`, `lighting`, `why_it_works`, `ctr`, `cvr`, and module `visual`. The design/strategy
  team reads these.
- **Marketplace language** (e.g. German for amazon.de) = all customer-facing TEXT that ships on
  the listing/creative: `TITLE`, `BULLETS`, `overlay`, `overlay_sub`, module `headline`, module
  `body`, and `QA`. This is what the shopper reads.

## Operating procedure (the steps, in order)
1. **Brand ready?** Ensure `customers/<slug>/` has `config.json` + `brand_study.md` + logo.
   New brand → onboard brand info first (fill config, run `make_brand_study.py <slug>`).
2. **Inputs**: SEO listing → `products/<product>/listing.xlsx`; get the **client website URL**.
3. **Research** (this is the value): fetch the website + parse the listing. Pull real product
   facts — formula, claims, regulatory IDs (e.g. NPN), dosing, differentiators, taglines.
   For the **main image**, also analyse **competitor main images** (scrapers in `tools/`,
   needs competitor ASINs) to find the white space we can own. Save verified facts to
   `products/<product>/SOURCE_NOTES.md`.
4. **Brand Sheet first** — the brief opens with the client brand for the design team
   (auto-rendered as Section 1 from `config.json`, incl. the creative directive).
5. **Image plan** — write `run.py`: TITLE · 5 bullets · 7 images
   (hero / hook / educate / lifestyle / trust / format / close, each with `ctr`/`cvr`) ·
   7 A+ modules · Q&A · backend KW. Apply the creative directive. Overlays in marketplace language.
6. **Final QA (automatic on every build)** — the builder runs a **compliance scan** over ALL
   copy (title, bullets, overlays, A+, Q&A); a red banner + loud console line appear on any
   **blocking** violation (fix before publishing). A **CTR/CVR strategy recap** (Section 8) is
   generated from the per-image `ctr`/`cvr` for the strategy team.
7. **Build** → `python customers/<slug>/products/<product>/run.py` → EQUALICE-branded PDF,
   named like the SEO listing: **`0X_<ASIN>_Image Plan.pdf`** (set `PLAN_NO="0X"` in run.py;
   ASIN is read from `listing.xlsx`).

Canonical example to copy = **image plan #1**, `customers/nutripur/products/genius_kids_teens/run.py`.

---

## When to Use
- New product listing launch
- Listing redesign / optimization
- Brand onboarding with new product line

---

## Tools

| Tool | Script | Purpose |
|---|---|---|
| Listing Scraper | `tools/scrape_amazon_listing.py` | Pull competitor listing data (title, bullets, price, images) by ASIN |
| Review Scraper | `tools/scrape_amazon_reviews.py` | Pull & analyze competitor reviews — praise, complaints, emotional triggers |
| Autocomplete | `tools/amazon_autocomplete.py` | Fetch Amazon search autocomplete suggestions for keywords |
| Visual Analysis | `tools/analyze_category_visuals.py` | Download competitor listing images for visual pattern analysis |
| Web Research | `tools/web_research.py` | Search web for product trends, buyer demographics, lifestyle context |
| Compliance Checker | `tools/amazon_compliance_checker.py` | Check all copy against Amazon prohibited words & rules |
| PDF Export | `tools/export_brief_to_pdf.py` | Export final markdown brief to styled PDF |

**Supported marketplaces:** `de`, `com`, `co.uk`

---

## Required Inputs

### From the Client (via Design Onboarding)
Source: [Design Onboarding Spreadsheet](https://docs.google.com/spreadsheets/d/1kPAooxMzpQCju-VLmASyz4xHoVssAddRzUl9oBxiOIU/edit)

The onboarding form collects:
| Field | Purpose |
|---|---|
| Brand Guide / Style Guide (PDF) | Visual identity reference |
| Font (Headline) | Typography for headlines |
| Font (Sub-Headline) | Typography for subheadlines |
| Font (Body Text) | Typography for body copy |
| Brand Colors | HEX codes for primary/secondary colors |
| Design Style | Modern, Minimalist, Playful, Luxurious, Sustainable, Warm, Technical, Creative, Clean |
| Stock Photo Policy | Yes with product insertion / Yes without / No |
| Design No-Gos | Absolute don'ts for the brand |
| Brand Message | Core message the brand wants to convey |
| Creative Freedom (1-5) | How much room to push boundaries |
| Logo Files | Logo uploads |
| Brand Name | Correct spelling/formatting |

### From the Agent (you provide at project start)
- **Product name & ASIN** (if existing)
- **Target market** (e.g. DE, US, UK)
- **Product category**
- **Relevant keywords** (main + long-tail)
- **USPs** (what makes this product different)
- **Key features** (specs, materials, dimensions, etc.)
- **Competitor reviews** (paste or link — what do buyers love/hate about alternatives?)
- **Product images/renders** available (what raw material do we have to work with?)
- **Target audience** (demographics, psychographics if known)

---

## Process

### Phase 1: Brand Understanding (Brandbook Creation)

**Goal:** Translate the raw onboarding data into a clean, usable brandbook document.

1. Pull the client's row from the onboarding spreadsheet
2. If a brand guide PDF was provided, review it and extract key visual rules
3. Create a **Client Brandbook** (Google Doc) with these sections:

```
# [Brand Name] — Brandbook

## Brand Identity
- **Brand Name:** [exact name]
- **Brand Message:** [translated & polished version of their answer]
- **Brand Personality:** [derived from design style + message]

## Typography
- **Headlines:** [Font name]
- **Subheadlines:** [Font name]
- **Body Text:** [Font name]

## Color Palette
- **Primary:** [HEX + color name]
- **Secondary:** [HEX + color name]
- **Accent:** [HEX + color name]
- **Background options:** [light/dark based on brand style]

## Visual Style
- **Style Direction:** [e.g. "Modern & Sustainable with warm tones"]
- **Photography Style:** [lifestyle/studio/graphic based on brand]
- **Stock Photos:** [policy]
- **Design No-Gos:** [what to avoid]

## Creative Freedom
- **Level:** [1-5] — [interpretation: 1=strict brand compliance, 5=full creative freedom]

## Logo Usage
- [Logo file references]
```

4. Write everything in clean, professional language. Translate German answers to English where needed for international teams.

---

### Phase 2: Buyer Psychology & Market Research

**Goal:** Understand WHY someone buys this product and what convinces them.

This is the creative intelligence phase. Go deep. Use the research tools to gather real data.

**Tool sequence:**
1. `python3 tools/scrape_amazon_listing.py <COMPETITOR_ASIN1,ASIN2,ASIN3> <marketplace>` — Pull competitor listings
2. `python3 tools/scrape_amazon_reviews.py <COMPETITOR_ASIN> <marketplace> 5` — Pull reviews for top 2-3 competitors
3. `python3 tools/amazon_autocomplete.py "<seed_keyword1,seed_keyword2>" <marketplace>` — Find what buyers search for
4. `python3 tools/analyze_category_visuals.py <ASIN1,ASIN2,ASIN3> <marketplace>` — Download competitor images for analysis
5. `python3 tools/web_research.py "<product category>" --market <marketplace> --deep` — Research trends & lifestyle context

#### 2a. Competitor Review Analysis
Run `scrape_amazon_reviews.py` on top 2-3 competitor ASINs, then extract:
- **Top 3 reasons people BUY** (what do 5-star reviews praise?)
- **Top 3 reasons people DON'T BUY** (what do 1-3 star reviews complain about?)
- **Unmet needs** (what do buyers wish existed?)
- **Emotional triggers** (what language do buyers use? What feelings drive the purchase?)
- **Purchase objections** (what makes people hesitate?)

#### 2b. Buyer Persona Construction
Based on reviews + product category, build:
- **Who is the buyer?** (age range, lifestyle, situation)
- **What triggered the search?** (pain point, event, need)
- **What are they comparing?** (price, quality, features, reviews, brand trust)
- **What would make them click "Add to Cart" in 3 seconds?**
- **What lifestyle does this product represent?**

#### 2c. Competitive Visual Analysis
Run `analyze_category_visuals.py` to download competitor images to `.tmp/competitor_images/`, then analyze and think about:
- What do competitors show in their main images?
- What are competitors NOT showing that we could?
- What visual clichés exist in this category that we should avoid or subvert?
- What would make our listing visually stand out in search results?

#### 2d. Moodboard & Visual Direction
Create a written moodboard with:
- **Overall visual mood** (e.g. "Bright, airy, Scandinavian-inspired lifestyle with warm wood tones and natural light")
- **Color mood** (how brand colors interact with product and lifestyle setting)
- **Lifestyle scenarios** (3-5 specific scenes that show the product in aspirational use)
- **Props & styling direction** (what belongs in the frame with the product)
- **Lighting direction** (natural, studio, dramatic, soft)
- **Human element** (hands, full body, face, no people?)
- **Texture & material emphasis** (what physical qualities to highlight)
- **Reference image descriptions** (describe 5-10 specific reference images you'd search for)

---

### Phase 3: Listing Image Plan (7 Images)

**Goal:** Plan all 7 listing images with conversion-optimized sequencing.

**Format:** 2000 x 2000px (square, optimized for mobile viewing)

#### Image Sequencing Strategy

| Slot | Purpose | Conversion Role |
|---|---|---|
| 1. Main Image | Hero product shot — must win the click in search | **CLICK TRIGGER** |
| 2. Image 2 | #1 USP or key benefit — instant value proposition | **HOOK** |
| 3. Image 3 | Features/specs or how-it-works | **EDUCATE** |
| 4. Image 4 | Lifestyle / in-use shot | **DESIRE** |
| 5. Image 5 | Social proof / trust / certifications | **TRUST** |
| 6. Image 6 | What's in the box / size / comparison | **CLARIFY** |
| 7. Image 7 | Brand story or secondary lifestyle | **CLOSE** |

#### For Each Image, Define:

```
## Image [#] — [Title]
**Type:** [Hero / Infographic / Lifestyle / Comparison / Brand Story]
**Conversion Role:** [Click Trigger / Hook / Educate / Desire / Trust / Clarify / Close]
**Dimensions:** 2000 x 2000 px

### Visual Description
[Detailed description of what the image shows — product angle, setting, props, lighting, human elements]

### Copy Overlay
- **Headline:** [max 5-7 words, benefit-driven]
- **Subline:** [supporting detail, 1 short sentence]
- **Call-outs / Labels:** [if infographic-style, list each label]

### Design Notes
- [Font to use]
- [Color treatment]
- [Layout direction — where product sits, where text sits]
- [Any specific brand guidelines to apply]

### Why This Works
[1-2 sentences on the psychology: why this image at this position converts]
```

---

### Phase 4: A+ Premium Content Plan

**Goal:** Plan the full A+ Premium layout with module-by-module content.

#### Module Structure (Fixed Sequence)

| # | Module Type | Desktop | Mobile | Notes |
|---|---|---|---|---|
| 1 | Premium Full Image | 1464 x 600 px | 600 x 450 px | Alt text required |
| 2 | Premium Simple Image Carousel | 220 x 220 px per tile (5 tiles) | — | Alt text per tile |
| 3 | Premium Full Image | 1464 x 600 px | 600 x 450 px | Alt text required |
| 4 | Premium Full Image | 1464 x 600 px | 600 x 450 px | Alt text required |
| 5 | Premium Simple Image Carousel | 220 x 220 px per tile (5 tiles) | — | Alt text per tile |
| 6 | **Benefits / info banner** (ends with a smart line bridging into the Q&A) | 1464 x 600 px | 600 x 450 px | Alt text required |
| 7 | **Premium Q&A** (the finale) — established brands may use Comparison instead | Text only | Text only | — |

**Important:** Premium Full Image modules require BOTH a desktop and mobile version. Design mobile-first — ensure key messaging and visuals remain clear at 600x450.

#### House rules for the A+ sequence (durable — apply to every plan)

**Always keep 7 modules.** New brands do NOT lose a module — they swap the Comparison for a
"From the Brand" module.

1. **New brands → NO Comparison Chart. Q&A is the FINALE (Module 7).** For a brand's first plans
   (freshly onboarded), do **not** build the `a+_comparison` module, and make the **Q&A the last
   module**. **Module 6 is a benefits/info banner** whose copy **ends with a smart line that
   bridges into the Q&A** (e.g. *"Still have questions? The answers are right below."*).
   Automated when `config.json` has `"new_brand": true`: the builder drops any comparison module,
   moves the `a+_qa` module to LAST, appends the language-matched Q&A bridge to the module before
   it, and — if you didn't author a benefits/brand closer — inserts a "From the Brand" banner
   (from `brand_statement`) as Module 6 to keep 7. Established brands with real comparison data
   (e.g. Ultra PRO's A+ sheets) keep the Comparison.

2. **`brand_statement` powers Module 6's closer.** Set it in `config.json` — a confident,
   on-brand line (*"From <Brand>: <short promise>."*). It fills the auto-inserted benefits/brand
   closer, right before the smart Q&A bridge. **Don't end on two near-identical images:** if
   Image 6 is heritage/trust, make Image 7 the emotional/lifestyle close, not a second trust image.

3. **Always run a Copywriting-Agent pass.** Before finalizing, elevate the marketing copy with a
   dedicated copywriting step (a sub-agent or a focused self-pass) so every plan is
   marketing-technically top-tier — see "Copywriting standard" below. Never ship first-draft copy.

#### Copywriting standard (the bar every plan must clear)

Run a **dedicated copywriting pass** (own sub-agent on rollouts; focused self-pass on singles)
whose only job is to make the marketing copy *sell*. It rewrites overlays, overlay_subs, bullet
heads, A+ headlines and the Q&A brand line to this bar:

- **Dream-outcome first.** Lead with the *after* / the transformation, not the feature. Sell the
  result the buyer wants, then justify it with the spec. ("Sell the outcome, not the action.")
- **Voice-of-Customer.** Mine the review language (good + bad) and speak the buyer's exact words;
  turn the top objection into a benefit.
- **Power words + specifics.** Concrete numbers, credentials and sensory verbs beat vague
  adjectives. One strong idea per line — glanceable at thumbnail size.
- **Punchy ≠ choppy.** Short, but it must still read smoothly and on-brand (no robotic fragments).
- **Rhythm & distinctiveness.** Vary structure across the 7 images; avoid repeating the same
  sentence shape. Each overlay should be a line a competitor could not have written.
- **On-brand voice.** Match the brand_study voice; the "From the Brand" Q&A close carries the
  strongest brand personality.
- **Stay compliant.** Elevation never adds banned claims — respect the brand's no-gos and the
  auto compliance scan (marketplace language, structure/function for supplements, no superlatives).

The copywriting pass runs **after** the product-specific draft is built and **before** the final
build/verify, so its output still passes the compliance + copy-length linters.

#### For Each Module, Define:

```
## Module [#] — [Module Type]: [Title/Theme]

### Content Strategy
[What this module communicates and why it's placed here in the flow]

### Visual Description
[Detailed description of the image(s) — layout, product placement, background, graphical elements]

### Copy
- **Headline:** [...]
- **Body:** [...]
- **Alt Text:** [SEO-optimized alt text for the image]

### For Carousels — Per Tile:
| Tile | Icon/Image | Headline | Body |
|---|---|---|---|
| 1 | [description] | [...] | [...] |
| 2 | [description] | [...] | [...] |
| 3 | [description] | [...] | [...] |
| 4 | [description] | [...] | [...] |
| 5 | [description] | [...] | [...] |

### For Q&A:
| Question | Answer |
|---|---|
| [Customer question] | [Brand answer — keyword-rich] |

### For Comparison Chart:
| Feature | Our Product | Competitor A | Competitor B |
|---|---|---|---|
| [Feature 1] | [checkmark/value] | [...] | [...] |

### Design Notes
- [Layout guidance for Figma implementation]
- [Brand-specific styling to apply]
```

---

### Phase 5: Copywriting

**Goal:** Write all copy that appears in listing images and A+ modules.

#### Copywriting Rules
1. **Benefit-first, feature-second** — lead with what the customer gains, not what the product has
2. **Mobile-optimized** — short headlines, scannable text, large enough to read on phone
3. **Keyword integration** — weave target keywords naturally into headlines and body copy
4. **Emotional + rational** — pair an emotional hook with a concrete proof point
5. **Brand voice** — match the tone defined in the brandbook
6. **Language** — write in the target market language (translate as needed)
7. **No fluff** — every word must earn its place. No "premium quality" without proof.

#### Copy Deliverables
- All listing image headlines & sublines
- All A+ module headlines & body text
- All carousel tile text
- All Q&A pairs (min 3, keyword-optimized)
- All comparison chart content
- All image alt texts (SEO-optimized)

---

### Phase 6: Compliance Check

**Goal:** Verify all copy passes Amazon's content policies before delivery.

**Run:** `python3 tools/amazon_compliance_checker.py <brief_file.md>`

The checker flags:
- **Violations** (must fix): prohibited superlatives, health claims, competitor mentions, urgency language, pricing references, external links, shipping promises
- **Warnings** (review): guarantee language, subjective claims, environmental claims without certification, excessive formatting

Fix all violations. Review all warnings and adjust where needed.

---

### Phase 7: Export

**Goal:** Package the final brief for delivery.

**Run:** `python3 tools/export_brief_to_pdf.py .tmp/<brief_file>.md .tmp/<brief_file>.pdf`

The PDF is styled and formatted for direct use by the design team in Figma.

---

## Output Format

### Deliverable: Content Brief Document (Google Doc or Markdown)

Structure:
```
# [Brand Name] — [Product Name] Content Brief
## Date: [YYYY-MM-DD]
## Market: [DE/US/UK]

---

## 1. Brandbook Summary
[Condensed version — fonts, colors, style, no-gos]

## 2. Buyer Psychology
[Persona, purchase triggers, objections, emotional drivers]

## 3. Visual Direction & Moodboard
[Written moodboard with reference descriptions]

## 4. Listing Images (7 Images)
[Full plan per image as defined above]

## 5. A+ Premium Content (7 Modules)
[Full plan per module as defined above]

## 6. Master Copy Sheet
[All copy in one place for easy review]
```

This format is designed to be **directly transferable to Figma**:
- Every frame has exact dimensions
- Every text element is written out
- Visual descriptions are detailed enough for a designer to execute
- Layout guidance is included per frame

---

## Clarifying Questions to Ask

Before starting, always verify:

1. **Do we have product photos/renders?** What raw visual assets exist?
2. **Are there existing listings to reference?** (Current listing we're improving?)
3. **Who are the top 3 competitors?** (ASINs if possible)
4. **Are there any claims we CAN'T make?** (Regulatory — especially health, food, kids products)
5. **Is there a price positioning?** (Premium, mid-range, budget — affects visual language)
6. **Any seasonal or trend angle?** (Launch timing, seasonal relevance)
7. **What's the hero USP?** (If they had to pick ONE thing, what is it?)
8. **Lifestyle context?** (Where/when/how is this product actually used?)
9. **Bundle or single product?** (Affects main image composition)
10. **Any specific competitor images they admire or want to beat?**

---

## Edge Cases & Notes

- **No brand guide provided:** Build the brandbook purely from onboarding answers + any existing Amazon presence. Lean into creative freedom level.
- **Low creative freedom (1-2):** Stick very close to existing brand materials. Minimal experimentation.
- **High creative freedom (4-5):** Push boundaries. Propose bold visual concepts. Test unconventional layouts.
- **Multiple products from same brand:** Reuse brandbook, create separate content briefs per product.
- **Regulated categories (supplements, children, food):** Flag any claims that need legal review. Note this in the brief.

---

## Quality Checklist

Before delivering the content brief:

- [ ] Brandbook covers all onboarding fields
- [ ] Buyer psychology section has real insights (not generic marketing speak)
- [ ] Every listing image has a clear conversion role
- [ ] Main image follows Amazon compliance (white background, product focus)
- [ ] All A+ modules follow the specified sequence
- [ ] Copy is in the correct target language
- [ ] Keywords are naturally integrated
- [ ] All dimensions are specified
- [ ] Design notes reference the brandbook (fonts, colors, no-gos)
- [ ] Moodboard has specific, actionable visual descriptions
- [ ] Alt texts are written for all A+ images
- [ ] No brand no-gos are violated
