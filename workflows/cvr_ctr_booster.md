# CVR × CTR Booster — Listing Diagnostic Workflow

## Objective
Run a structured diagnostic on any Amazon listing (live or pre-launch draft) and produce a **prioritised punch-list of fixes ranked by expected uplift to CTR (search-result click-through) and CVR (page-to-cart conversion)**.

Output is an Excel scorecard + a 1-page punch list, ready for the design / copy team.

---

## When to Use
- Before launching a new listing — sanity check the brief against the same scoring rubric.
- 30 days after launch — diagnose where CTR or CVR is underperforming the niche median.
- Quarterly health-check on the brand's top 5 SKUs.
- After a competitor moves (price change, image refresh) — re-score and recommend response.

---

## Required Inputs
- ASIN
- Marketplace (de / com / co.uk)
- Top 3 competitor ASINs (from search-result top 1, top 3, top 10 — diverse positions)
- Optional: Brand Analytics or Helium 10 keyword export for the niche

---

## Tool Sequence
```
1. python3 tools/scrape_amazon_listing.py <ASIN> <market>
2. python3 tools/scrape_amazon_listing.py <COMP1>,<COMP2>,<COMP3> <market>
3. python3 tools/scrape_amazon_reviews.py <ASIN> <market> 2
4. python3 tools/amazon_autocomplete.py "<root_kw1>,<root_kw2>" <market>
5. python3 tools/cvr_ctr_score.py .tmp/<asin>_score.json   # produces the scorecard
6. python3 tools/export_brief_to_pdf.py .tmp/<asin>_punchlist.md ~/Desktop/<asin>_uplift.pdf
```

---

## The 20-Point Scorecard

Every line is scored 1–5 (1 = critical gap, 5 = best-in-class). Multiply by **weight** (High=3, Medium=2, Low=1). The product of `(5 − score) × weight` is the **uplift potential** for that line. Sum, sort, ship.

### CTR — Search-Result Click-Through

| # | Lever | Diagnostic question | How to test | Weight |
|---|---|---|---|---|
| 1 | Main image clarity at 200 px | Is the product unmistakable at thumbnail size? | Shrink to 200×200, look 2 sec, can you tell what it is and which variant? | High |
| 2 | Main image color contrast | Does the tile pop against neighbours in the SERP? | Screenshot the SERP. Does it blend in or stand out? | High |
| 3 | Title — primary keyword in first 80 chars | Is the most-searched root keyword above the mobile fold? | Open on phone. What's shown before "..."? | High |
| 4 | Title — variant clarity | Are size, count, and key feature unambiguous? | "1 L (33 Fl Oz)" should be visible without opening the variant picker. | Medium |
| 5 | Star rating ≥ 4.4 visible badge | Is the rating high enough to clear the click filter? | Below 4.3 hurts CTR materially. Above 4.5 helps. | High |
| 6 | Review count ≥ category median | Does the listing have enough reviews to feel credible? | Compare to top-3 competitors. | High |
| 7 | Coupon / Promo badge present | Is there an attention-grabbing badge (% off, S&S)? | Missing badges leave CTR on the table in commodity categories. | Medium |

### CVR — Page-to-Cart Conversion

| # | Lever | Diagnostic question | How to test | Weight |
|---|---|---|---|---|
| 8 | Hero image confidence in 2 seconds | Within 2 sec, can a buyer tell exactly what they're getting? | Show image #1 to someone for 2 sec, ask them to describe it. | High |
| 9 | Image #2 — strongest single buying reason | Does it lead with the #1 benefit (not feature)? | A buyer should think "I want this because…" after image 2. | High |
| 10 | Bullet #1 — emotional + concrete proof | Does the first bullet pair an emotional hook with a hard fact? | Read aloud. Does it tell, or does it sell? | High |
| 11 | Bullets — 5 distinct benefits | Are all 5 bullets non-overlapping? | Bullets that repeat each other waste real estate. | Medium |
| 12 | A+ Module 1 banner — repositions brand | Does the A+ banner reframe the product beyond bullets? | It should feel like a richer pitch, not a repeat. | Medium |
| 13 | A+ Module 6 Q&A — defuses top objections | Does it answer the questions that show up in negative reviews? | Cross-check against the negative reviews. | High |
| 14 | A+ Module 7 comparison chart | Does it justify the price vs cheaper alternatives? | Without one, sticker shock kills CVR. | High |
| 15 | Variant family clarity | Is the right size pre-selected and others visible? | Wrong default variant is a silent CVR killer. | Medium |
| 16 | Brand Story strip | Is there a Brand Story block beneath the bullets? | Adds trust and discovery — many sellers skip it. | Low |
| 17 | First 5 reviews shown | Are top reviews helpful, recent, and not all 5★? | A 5★-only block reads as fake. | Medium |
| 18 | Subscribe & Save offered | For consumables: is S&S enabled? | Materially boosts CVR + LTV in Grocery / Beauty. | Medium |
| 19 | Q&A section — at least 3 answered | Are buyer questions answered (by brand or owner)? | Unanswered questions = friction. | Low |
| 20 | Mobile-fold above-the-fold | Does the mobile-visible portion close the sale (image + headline + price + variant + S&S)? | Open on phone. Is anything missing in the first scroll? | High |

---

## Scoring Rubric (1–5)

- **1 — Critical gap:** Visibly worse than category median. Costs sales today.
- **2 — Below average:** Noticeably weaker than top-3 competitors.
- **3 — Acceptable:** Median for the category. Not winning, not losing.
- **4 — Strong:** Better than median; competitive on this lever.
- **5 — Best-in-class:** Among the top in the category.

---

## Uplift Math

For each line:
```
uplift_points = (5 - score) × weight_value
weight_value: High = 3, Medium = 2, Low = 1
```

The lines with the **highest uplift_points** are the priority fixes. A line scoring 5 contributes 0 (no room to grow). A line scoring 1 with High weight contributes 12 (highest possible single-line uplift).

The sum across all 20 lines gives a **Listing Health Score** (lower number = healthier listing). Track this number over time per SKU.

---

## Output Format

**A. Excel scorecard** — one sheet per SKU, banded for readability, with a totals row at the bottom and a sorted "Priority Fixes" block.

**B. One-page punch list** — markdown / PDF. Top 5 fixes, each with:
- The lever
- Current state (what's wrong)
- Recommended fix (specific, do-it-this-week instruction)
- Expected uplift (qualitative: "small / medium / large")
- Owner (designer / copy / ops / Brand Analytics)

---

## Edge Cases & Notes
- **New listings (< 30 days):** Skip lines 5 (rating) and 6 (review count). Re-score after 30 days.
- **B2B listings:** Lines 7 (coupon) and 18 (Subscribe & Save) are not applicable. Drop them.
- **Restricted categories (Beauty, Supplements, Baby):** Add a 21st line for compliance / claim language risk.
- **No A+:** If A+ is not yet published, score lines 12–14 as 1 (critical gap) — A+ is one of the highest single uplifts available.
- **Subscribe & Save eligibility:** Confirm with the seller before flagging — not all categories support it.

---

## Self-Improvement Loop
Every quarter, review the priority fixes that were actually shipped vs. the ones that drove measurable uplift. Update the **weights** in this workflow so they reflect what really moves the numbers in your category. The rubric should grow more accurate over time.
