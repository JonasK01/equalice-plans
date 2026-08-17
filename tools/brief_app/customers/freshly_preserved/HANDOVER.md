# Freshly Preserved — Image + A+ Premium plans · handover

**Built 2026-08-09** from the SEO drop of 08.08.26 · marketplace **amazon.com (US)** ·
**6 products → 11 plans**, all compliance-clean and copy-length clean.

Each PDF is a single EQUALICE-branded brief containing **both** deliverables:
the **7-image listing plan** (Section 4) and the **7-module A+ Premium plan** (Section 5),
plus brand sheet, Q&A, backend keywords and a CTR/CVR strategy recap. 20 pages each.

---

## The 11 plans

| # | Product | ASIN | PDF |
|---|---|---|---|
| 01 | Flower Petals · 0.2 oz, about 1.5 cups | B0H8FDVXFJ | `products/petals_mix/01_B0H8FDVXFJ_Image Plan.pdf` |
| 02a | Small Pansy · 12 blooms, 0.1 oz | *parent B0H8TR2WSB* | `products/bloom_family/02a_…_Small-Pansy-12_Image Plan.pdf` |
| 02b | Small Orchid · 12 blooms, 0.1 oz | *parent B0H8TR2WSB* | `products/bloom_family/02b_…_Small-Orchid-12_Image Plan.pdf` |
| 02c | Small Pansy & Orchids · 12 blooms, 0.1 oz | *parent B0H8TR2WSB* | `products/bloom_family/02c_…_Small-Pansy-Orchid-12_Image Plan.pdf` |
| 02d | Pansy · 25 blooms, 0.2 oz | *parent B0H8TR2WSB* | `products/bloom_family/02d_…_Pansy-25_Image Plan.pdf` |
| 02e | Pansy & Orchids · 25 blooms, 0.2 oz | *parent B0H8TR2WSB* | `products/bloom_family/02e_…_Pansy-Orchid-25_Image Plan.pdf` |
| 02f | Purple Orchids · 25 blooms, 0.2 oz | *parent B0H8TR2WSB* | `products/bloom_family/02f_…_Purple-Orchids-25_Image Plan.pdf` |
| 03 | Small Roses & Mixed · ~12 rose blooms + petals | B0H8ZDCP71 | `products/small_roses_mixed/03_B0H8ZDCP71_Image Plan.pdf` |
| 04 | Fall Cake Decorating Kit · 4 oz, 25+ pieces | B0H9532666 | `products/fall_cake_kit/04_B0H9532666_Image Plan.pdf` |
| 05 | Basil Blossoms · ~25 sprigs, 0.2 oz | B0H9ZFBXSF | `products/basil_blossoms/05_B0H9ZFBXSF_Image Plan.pdf` |
| 06 | Squash Blossoms · 12 whole, 0.2 oz | B0CN47WW2D | `products/squash_blossoms/06_B0CN47WW2D_Image Plan.pdf` |

Rebuild any of them with `python products/<folder>/run.py`.
`bloom_family/run.py` emits all six variation PDFs in one run.

---

## How the plans are structured

**Images (2000×2000):** hero (shipped as **3 A/B options** — the SEO team's CTR note says the
current main image is not attractive, so every plan gives Manage-Your-Experiments something to
test) → hook → educate → desire/lifestyle → trust badges → honest size & count → family close.

**A+ Premium (desktop 1464×600 / mobile 600×450, alt text throughout):** brand banner →
"why Freshly Preserved" carousel → ways to use → fresh-flowers-wilt banner → **variation family
carousel** → From the Brand closer → **Premium Q&A finale**.

No Comparison chart anywhere: Freshly Preserved is flagged `new_brand: true`, and the house rule
for new brands is Comparison out, Q&A last, with the module before it bridging into the Q&A.

## Parent-child, built into every plan

A shopper who lands on the wrong child normally bounces. Three places stop that:

- **Image 7 — "Find your flower"**: family strip, THIS child ringed in brand green with a
  "YOU ARE HERE" tag, siblings at 70% scale.
- **A+ Module 5 — family carousel**: "You are viewing: X" plus 5 sibling tiles, remainder named
  in text.
- **Image 6**: this child's count and weight shown against its siblings.

## Copy sourcing

TITLE, the 5 bullets and the backend keyword string come **1:1 from each product's SEO tab** —
that is the keyword axis and it is not rewritten. Everything creative (on-image overlays, all A+
copy, the Q&A) is hand-written per product against `brand_study.md` and the review analysis.

## What each product leads on

- **01 Petals** — coverage, not focal points. Hero is the petals measured to the 1.5-cup line in a
  glass cup: that single frame answers the "package looks smaller than expected" reviews.
- **02 Whole blooms** — real bloom + visible count. Size shown honestly on a fingertip and beside
  a US quarter, because "smaller than expected" is the family's #1 complaint.
- **03 Roses** — the only pack with **blooms AND petals**, and the romance occasion (weddings,
  anniversaries). Loose petals reframed as intended contents, not shipping damage.
- **04 Fall Kit** — "place, don't pipe": flowers *and* greenery, a 3-step method, and 4 oz of
  abundance shown against a standard 0.2 oz pack. Seasonal — see below.
- **05 Basil** — **savoury**. A cook's herb, not a cake decoration: rubs, sauces, salads, tea,
  cocktails. Basil only flowers for ~2 weeks, so shelf-stable blossoms are otherwise unbuyable.
- **06 Squash** — **savoury and large**. The one product where size is a boast: big enough to
  stuff and plate whole, and a farmers-market-only ingredient made available year-round.

---

## Open items

1. **Child ASINs for parent B0H8TR2WSB — blocking correct filing.** Excel truncates sheet names
   at 31 characters, so the ASINs encoded in the tab names are cut off
   (`SEO_Small Pansy Freeze_B0GLR6GB`) and appear nowhere else in the workbook. All six variation
   PDFs are filed under the **parent** ASIN with a variant suffix. Send the six child ASINs and
   set `VARIANTS[...]["asin"]` in `products/bloom_family/run.py`, then re-run it.

2. **ASIN mismatch on 01 / 03 / 04 / 05.** The SEO folder name and the workbook's
   "Overview Product" tab disagree. The plans use the **folder** ASIN, since that is how the SEO
   team named the deliverable. Unconfirmed.

   | # | Folder (used) | Overview tab |
   |---|---|---|
   | 01 | B0H8FDVXFJ | B0CV9435JM |
   | 03 | B0H8ZDCP71 | B0GLR76YW1 |
   | 04 | B0H9532666 | B0DH2XBFY3 |
   | 05 | B0H9ZFBXSF | B0CR6XHZG7 |

3. **Brand assets still missing.** No logo file in this folder — onboarding referenced a
   `fp_veggie logo` (the snack line), never supplied; we need the **flowers** logo (PNG/SVG).
   Colours and fonts in `config.json` are **derived**, not client-confirmed: the client said
   "fresh green, purple, red, orange, white" with no HEX and no font. Design is building against
   derived values until this lands.

4. **Timing flag — 04 Fall Cake Decorating Kit is seasonal.** If it is meant to be live for this
   autumn it should jump the design queue; the other ten are evergreen.

5. **Family or range?** Every plan currently presents the whole line as one selectable family. If
   Amazon's actual parent-child only links the whole-bloom flowers (02a–02f), the strip still
   works as cross-sell on the standalone listings, but the wording there should shift from
   "pick your variation" to "also in the range". Needs confirmation.

## Retired

`products/bloom_family/legacy/pansy_orchids_2026-07/` — the original 11 Jul plan
(ASIN B0GMRFZD2G), superseded by **02c**. Reference only; see the README there.
