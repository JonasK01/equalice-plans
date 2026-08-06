# Product image-plan folder

Drop here:
- `listing.xlsx` — the SEO listing export for this product (the "axis").
- `run.py` — copy a working one (e.g. `customers/nutripur/products/genius_kids_teens/run.py`)
  and rewrite TITLE / BULLETS / IMAGES / MODULES / QA for this product.

Set `PLAN_NO = "0X"` in run.py to the product's SEO listing number.
Then: `python <this folder>/run.py` → writes `0X_<ASIN>_Image Plan.pdf` next to it
(named like the SEO listing: number + ASIN; ASIN comes from `listing.xlsx`).

`run.py` is self-contained: it reads `listing.xlsx`, resolves the brand via
`load_customer("<slug>")`, and writes `<PLAN_NO>_<ASIN>_Image Plan.pdf` in its own folder.

## Keep copy punchy (auto-linted on every build)
On-image text is a HEADLINE, not a sentence. The build prints `⚠ COPY LENGTH` if you exceed:
- `overlay` (on-image headline): **≤ 30 chars AND ≤ 5 words**
- `overlay_sub`: ≤ 90 chars · A+ module `headline`: ≤ 38 chars · bullet head `<b>…</b>`: ≤ 45 chars
Detail belongs in `visual` / `why_it_works` (designer-facing), not in the overlay.
