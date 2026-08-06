# Brand folder layout

Every brand lives in one folder under `customers/<slug>/`. This is the single
home for that brand — its identity AND all its product image plans.

```
customers/<slug>/
  config.json          # MACHINE brand study — the brief_app reads this. Source of truth.
  logo.<ext>           # brand logo (config.json -> logo_path points here)
  brand_study.md       # READABLE brand study — agent reads this FIRST. Auto-generated:
                       #   python tools/brief_app/make_brand_study.py <slug>
  source/              # raw client/SEO inputs: brand guide PDF, onboarding, product info
  products/
    <product_slug>/
      listing.xlsx     # the SEO "axis" for THIS product (keywords + listing copy)
      run.py           # the image-plan generator (hand-written copy + IMAGES list)
      brief.pdf        # generated branded image-plan brief (output)
      legacy/          # (optional) older manual briefs / scraped json, kept for reference
```

## Required at the top level (do not move into subfolders)
`config.json` and `logo.*` — the app globs `customers/*/config.json` and seeds
`logo.*`, so these two must stay at the brand root.

## Start a new brand
1. Copy this `_TEMPLATE/` folder to `customers/<slug>/`.
2. Fill in `config.json` (or create it via the Streamlit app). Drop the logo.
3. `python tools/brief_app/make_brand_study.py <slug>` to render `brand_study.md`.
4. Put raw inputs in `source/`.

## Start a new product image plan
1. Copy `products/_TEMPLATE/` to `products/<product_slug>/`.
2. Drop the SEO listing as `listing.xlsx`.
3. Copy an existing `run.py` (e.g. nutripur/products/genius_kids_teens/run.py) as
   your starting point and rewrite TITLE / BULLETS / IMAGES / MODULES for this product.
4. `python customers/<slug>/products/<product_slug>/run.py` -> writes `brief.pdf`.
