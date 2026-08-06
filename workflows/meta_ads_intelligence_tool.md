# Meta Ads Intelligence Tool

## Objective
Create a conversion-optimized creative plan for Meta ads (Facebook + Instagram) across all relevant placements and formats. The output is a structured creative brief that can be directly implemented in Figma and handed to media buyers.

---

## When to Use
- New product launch on Meta
- Scaling campaign with fresh creatives
- Creative refresh (ad fatigue)
- Funnel build-out (TOF / MOF / BOF)

---

## Relationship to Amazon Workflow

Meta reuses brand context that Amazon already produced — **but not Amazon tools**.

**Shared:** `.tmp/<brand>/` folder
- Amazon content brief → pull brand colors, fonts, voice, USPs, buyer psychology
- `moodboard/` → visual direction already validated
- `images/` → product renders / raw assets

**Not shared:** tools. Meta has its own toolset in `tools/` (prefixed `meta_*`). Do not call `scrape_amazon_*`, `amazon_compliance_checker`, or `export_brief_to_pdf` from this workflow — Meta has different platforms, policies, and export needs.

**How to start:**
1. Check `.tmp/<brand>/` — does a brand brief already exist from the Amazon workflow?
2. If yes → pull brandbook, buyer persona, moodboard, USPs directly. Skip re-researching brand basics.
3. If no → flag it. Meta creative without brand context is guesswork. Run the Amazon brand phase first OR collect brand info from the client.

---

## Tools (Meta-specific — to be built as needed)

| Tool | Script | Purpose |
|---|---|---|
| Ad Library Scraper | `tools/meta_ad_library_scraper.py` | Pull competitor ads from Meta Ad Library (images, copy, run duration) |
| Audience Research | `tools/meta_audience_research.py` | Demographics, interests, behaviors for target audience |
| Policy Checker | `tools/meta_policy_checker.py` | Check copy against Meta advertising policies (different from Amazon) |
| Hook Generator | `tools/meta_hook_generator.py` | Generate and rank scroll-stopping hooks based on angle + audience |
| Brief Export | `tools/meta_export_brief.py` | Export Meta creative brief to styled PDF for design team |

**Note:** Tools are built on demand. If a phase needs a tool that doesn't exist yet, stop and flag it — don't fall back to the Amazon equivalent.

---

## Required Inputs

### From `.tmp/<brand>/` (reuse)
- Brand colors, fonts, logo
- Brand voice / tone
- Buyer persona
- Product USPs
- Visual moodboard
- Product imagery

### From the Agent (new for this campaign)
- **Campaign objective** (Awareness / Traffic / Engagement / Leads / Sales / App Installs)
- **Funnel stage** (TOF — cold / MOF — warm / BOF — retargeting)
- **Target audience** (cold interest targeting, lookalikes, custom audiences)
- **Landing destination** (Amazon listing, Shopify, landing page, WhatsApp, lead form)
- **Budget & scale** (test budget vs. scale budget — affects how many variations to plan)
- **Market & language** (DE / US / UK / other)
- **Offer / hook** (discount, bundle, free shipping, new product, seasonal)
- **Creative constraints** (any formats the client wants/doesn't want — e.g. "no video, no UGC")

---

## Process

### Phase 1: Brand & Context Pull

**Goal:** Load brand context from `.tmp/<brand>/` without re-doing the work.

1. Locate brand folder in `.tmp/`
2. Read the Amazon content brief (if present) — extract:
   - Brand identity (name, message, personality)
   - Color palette & typography
   - Buyer persona
   - Top 3 emotional triggers
   - Top 3 purchase objections
   - Product USPs
3. Note what's missing. Meta needs some things Amazon doesn't:
   - Thumb-stopping visual language
   - Short-form video thinking (Reels / Stories)
   - Social proof formats (UGC-style, testimonial overlays)

---

### Phase 2: Campaign Strategy

**Goal:** Translate campaign objective into creative requirements.

#### Funnel Stage → Creative Role

| Stage | Goal | Creative Focus |
|---|---|---|
| **TOF (Cold)** | Stop the scroll, introduce brand | Hook-heavy, curiosity, bold visuals, pattern interrupt |
| **MOF (Warm)** | Educate, overcome objections | Social proof, demos, comparisons, UGC |
| **BOF (Retargeting)** | Close the sale | Offer-driven, urgency, testimonials, FAQ handling |

#### Define per Campaign:
- **Primary objective** (what Meta optimizes for)
- **Core message** (one sentence)
- **Hero USP** (if they had to remember ONE thing)
- **Angle** (problem-solution / aspiration / comparison / story / contrarian)
- **Proof elements** (reviews, stats, certifications, before-afters)

---

### Phase 3: Competitive Research

**Goal:** See what's already working in the category on Meta.

**Tool sequence:**
1. `python3 tools/meta_ad_library_scraper.py <competitor_brand_name> --market <DE|US|UK>` — Pull competitor ads that have been running 30+ days (signal they're profitable)
2. `python3 tools/meta_audience_research.py "<target_audience>" --market <marketplace>` — Interest & demographic signals

#### Analyze competitor ads for:
- **Hook patterns** (first 3 seconds / headline / opening frame)
- **Format mix** (are they running more image, carousel, or video?)
- **Copy length** (short punchy vs. long-form story)
- **Visual style** (UGC vs. studio vs. graphic-heavy)
- **Offers used** (discounts, bundles, free shipping)
- **Gaps** — what nobody in the category is doing that we could

---

### Phase 4: Format Plan

**Goal:** Decide which Meta formats to produce and how many variations.

#### Meta Ad Formats & Specs

| Format | Aspect Ratio | Dimensions | Placement | Best For |
|---|---|---|---|---|
| **Feed — Single Image** | 1:1 | 1080 x 1080 px | FB/IG Feed | Simple, fast test |
| **Feed — Portrait Image** | 4:5 | 1080 x 1350 px | FB/IG Feed | Max feed real estate |
| **Carousel** | 1:1 | 1080 x 1080 px (2–10 cards) | FB/IG Feed | Multi-USP, storytelling, product ranges |
| **Story / Reel** | 9:16 | 1080 x 1920 px | Stories + Reels | Mobile-first, video or static |
| **Video Feed** | 1:1 or 4:5 | 1080 x 1080 / 1080 x 1350 | Feed | Demos, UGC, testimonials |

**Safe zones:**
- Stories/Reels: keep headline in middle ~60% (top 14% + bottom 20% get covered by UI)
- Feed 4:5: text can go anywhere but bottom 20% gets cropped on some placements

#### Text Overlay Rule (updated policy)
Meta no longer hard-rejects >20% text, but ads with heavy text still underperform. Keep text overlays minimal — hook headline + optional sub-line max.

#### Variations per Campaign (recommendation)
- **Test phase:** 3–5 hooks × 2–3 visual treatments = 6–15 creatives
- **Scale phase:** double down on 1–2 winning angles, refresh weekly

---

### Phase 5: Creative Plan Per Ad

**Goal:** Spec every individual creative so design can execute directly.

#### For Each Creative, Define:

```
## Ad [#] — [Working Title]
**Format:** [Feed 1:1 / Feed 4:5 / Carousel / Story-Reel 9:16 / Video]
**Funnel Stage:** [TOF / MOF / BOF]
**Angle:** [Problem-Solution / Aspiration / Comparison / Story / Contrarian]
**Dimensions:** [exact px]

### Hook (first 3 seconds / top of frame)
[The thumb-stopper. One sentence or visual moment that stops the scroll.]

### Visual Description
[What the image/video shows — composition, product placement, setting, human element, lighting, text overlay position]

### Text Overlay (if any)
- **Headline:** [max 5-7 words]
- **Sub:** [optional 1 line]

### Ad Copy (the text above/below the creative)
- **Primary Text:** [the main body — 125 chars shows before "See more" on mobile]
- **Headline (below creative):** [max 40 chars]
- **Description (optional):** [max 30 chars]
- **CTA Button:** [Shop Now / Learn More / Sign Up / Order Now / etc.]

### Design Notes
- [Font from brandbook]
- [Color treatment]
- [Layout direction]
- [Brand no-gos to respect]

### Why This Works
[1-2 sentences: the psychology — why this hook, why this visual, why this angle for this audience]
```

#### For Carousels — Per Card:
```
| Card | Visual | Headline | Description |
|---|---|---|---|
| 1 | [hook card] | [...] | [...] |
| 2 | [USP 1] | [...] | [...] |
| 3 | [USP 2] | [...] | [...] |
| 4 | [social proof] | [...] | [...] |
| 5 | [CTA card] | [...] | [...] |
```

#### For Video / Reels — Per Scene:
```
| Time | Visual | On-screen Text | Voiceover / Audio |
|---|---|---|---|
| 0-3s | [hook shot] | [hook text] | [VO or trending audio] |
| 3-8s | [problem] | [...] | [...] |
| 8-15s | [solution/demo] | [...] | [...] |
| 15-25s | [proof] | [...] | [...] |
| 25-30s | [CTA] | [...] | [...] |
```

---

### Phase 6: Copywriting

**Goal:** Write all primary text, headlines, and CTAs per creative.

#### Meta Copy Rules (different from Amazon!)
1. **First line is everything** — mobile truncates after ~125 chars. Hook has to land before "See more"
2. **Conversational tone** — Meta is social, not a product page. Sound like a person, not a catalog
3. **Pattern interrupt** — emojis, line breaks, questions, numbers. Anything to break the scroll rhythm
4. **Clear CTA** — tell people exactly what to do ("Tap to shop", "Link in bio", "Get yours today")
5. **Social proof weaves in naturally** — "Over 10,000 reviews" works better than "Premium quality"
6. **No hard claims without proof** — Meta flags medical, financial, weight-loss claims fast

#### Per Creative Deliver:
- Primary text (long version + short version)
- Headline (40 char limit)
- Description (30 char limit)
- CTA button choice
- Landing URL

---

### Phase 7: Policy Check

**Goal:** Catch Meta ad policy violations before submission.

**Run:** `python3 tools/meta_policy_checker.py <brief_file.md>`

Meta's most common rejections:
- **Personal attributes** — implying you know the user's age, health, weight, race, religion ("Are you over 40?" → rejected. "Designed for 40+" → OK)
- **Before/after images** — heavily restricted in health/beauty
- **Unrealistic claims** — "Lose 10 lbs in a week", "Cure your acne"
- **Sensational content** — shock, clickbait, "You won't believe..."
- **Body positivity violations** — zoomed-in body parts, shame-based framing
- **Prohibited products** — tobacco, weapons, adult, supplements with banned ingredients
- **Trademark issues** — using "Meta", "Facebook", "Instagram" in copy

Fix all violations. Review warnings.

---

### Phase 8: Export

**Goal:** Package the brief for the design team and media buyer.

**Run:** `python3 tools/meta_export_brief.py .tmp/<brief_file>.md .tmp/<brief_file>.pdf`

Output goes to the same brand folder as Amazon work: `.tmp/<brand>/meta_creative_brief_<date>.pdf`

---

## Output Format

### Deliverable: Meta Creative Brief

```
# [Brand Name] — Meta Creative Brief
## Date: [YYYY-MM-DD]
## Market: [DE/US/UK]
## Campaign Objective: [Sales / Leads / Traffic / etc.]
## Funnel Stage: [TOF / MOF / BOF]

---

## 1. Brand Context
[Pulled from .tmp/<brand>/ — short summary of colors, fonts, voice, USPs]

## 2. Campaign Strategy
[Objective, core message, angle, hero USP]

## 3. Competitive Insights
[What's working for competitors, gaps to exploit]

## 4. Format Mix
[Which formats, how many variations, why]

## 5. Creative Specs
[Full spec per ad as defined above]

## 6. Master Copy Sheet
[All primary text, headlines, descriptions, CTAs in one place]

## 7. Launch Plan
[Which creatives test first, budget split, success metrics]
```

---

## Clarifying Questions to Ask

1. **Does a brand brief already exist in `.tmp/<brand>/`?** (If yes, reuse. If no, pull brand first.)
2. **What's the campaign objective in Meta Ads Manager?** (Sales / Leads / Traffic — shapes creative)
3. **Funnel stage?** (TOF creative ≠ BOF creative)
4. **Where does the ad send people?** (Amazon link / Shopify / landing page / WhatsApp / lead form)
5. **What offer are we running?** (Discount, bundle, free shipping, new launch, seasonal)
6. **How many variations?** (Test batch vs. scale batch)
7. **Any format constraints?** (Client may not want video, UGC, or certain imagery)
8. **Is there existing UGC or testimonials we can use?**
9. **What's the hero claim?** (And can we prove it without getting flagged?)
10. **Any previous Meta ads we can learn from?** (Winners to scale, losers to avoid)

---

## Edge Cases & Notes

- **No brand data in `.tmp/`:** Do not guess. Either run the Amazon brand phase first or collect brand info from the client before proceeding.
- **Regulated categories** (supplements, skincare with claims, finance, dating, children's products): policy check is non-negotiable. Flag every claim.
- **Small test budget (<€500):** 3-5 creatives max. Don't over-produce.
- **Scale phase:** focus on variations of the proven winner, not net-new concepts.
- **Client already has Amazon listing:** reuse the hero image angle, but adapt — Amazon's white-background main image rarely works on Meta. Needs lifestyle or text-overlay treatment.
- **Video without video assets:** static "video-style" creatives (Ken Burns pan on still image + text) can substitute for real video in early tests.

---

## Quality Checklist

- [ ] Brand context pulled from `.tmp/<brand>/` (not re-researched)
- [ ] Campaign objective and funnel stage match the creative direction
- [ ] Every ad has a distinct hook — no duplicates
- [ ] Hooks work in the first 3 seconds / first 125 chars
- [ ] Formats cover the required placements (Feed + Stories/Reels minimum)
- [ ] Text overlays are minimal and mobile-legible
- [ ] Copy is in the target market language
- [ ] CTAs match the landing destination
- [ ] No Meta policy violations
- [ ] Visual style references brandbook (fonts, colors, no-gos)
- [ ] Safe zones respected for Stories/Reels
- [ ] Brief exports cleanly to PDF
