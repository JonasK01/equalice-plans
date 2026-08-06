# EQUALICE Brief Generator

Internal Streamlit app for the SEO content writers. Pick a customer → upload the SEO-analysis Excel → download a branded Amazon listing brief PDF.

## What you get in every brief

- Cover + at-a-glance summary (auto-pulled from the Excel)
- Brandbook page (colors, fonts, voice, photo rules, no-gos — from the customer config)
- Buyer psychology page (target group, USPs, emotional benefits, review verbatims)
- **Moodboard with 5–6 real Unsplash reference images** (configure search prompts per customer)
- 7-image listing plan — each tile with role, visual direction, **overlay text in the marketplace language**, and a 4-point argumentation block (CTR · CVR · Keywords · Reviews)
- 7 A+ Premium modules (Banner → Carousel → Banner → Banner → Carousel → Q&A → Comparison)
- Master Copy sheet (title, 5 bullets, backend search terms) — each with argumentation block
- Compliance + designer handoff checklist

## Run it

```bash
# from repo root
streamlit run tools/brief_app/app.py
```

If `streamlit` isn't on PATH (Python user-install on macOS):

```bash
~/Library/Python/3.9/bin/streamlit run tools/brief_app/app.py
```

App opens at <http://localhost:8501>. Stop with Ctrl-C.

### Enable real moodboard images

The app uses the Unsplash API. Without a key, moodboard tiles render as placeholder boxes with the search prompt printed inside.

1. Create a free Unsplash developer account at <https://unsplash.com/developers>
2. Create an application → copy the "Access Key"
3. Export before launching Streamlit:

```bash
export UNSPLASH_ACCESS_KEY=your_key_here
streamlit run tools/brief_app/app.py
```

Images get cached locally under `assets/cache/` so the same prompt only hits the API once.

## Workflow

1. **Customers tab**: create the customer once with brand colors, voice, fonts, photo rules, no-gos, and 5–6 moodboard search prompts. Upload a logo (optional).
2. **Generate brief tab**: pick the customer, drop the SEO Excel, review the parsed fields (USPs, keywords, reviews, Q&A), click "Generate PDF", download.
3. **Brief archive tab**: re-download any previously built brief, organized per customer.

## Expected Excel structure

The parser is forgiving — it does fuzzy sheet-name matching (case-insensitive substring). Standard tabs the workflow expects:

| Sheet                    | What it reads                                                          |
|--------------------------|-----------------------------------------------------------------------|
| `Overview Product`       | Product name, ASIN, brand, marketplace, main keywords, USPs, emotional benefits, target group, target problems, competitors |
| `H10 KW - Phase 1` (or any `keywords`/`kw` sheet) | Full keyword list                                              |
| `RUFUS QNA (US only)`    | Q&A pairs                                                              |
| `Review Analysis`        | Good + bad review themes                                               |
| `Improvement`            | CTR + CVR briefing notes                                               |

Missing sheets are skipped gracefully — the brief still builds, but some sections will be sparse.

## File layout

```
tools/brief_app/
  app.py                          Streamlit entry point
  requirements.txt
  README.md
  core/
    config.py                     Paths + marketplace catalog
    customers.py                  Customer CRUD (JSON-backed)
    excel_parser.py               SEO Excel → ParsedBrief
    argumentation.py              CTR/CVR/Keywords/Reviews rationale per copy block
    unsplash.py                   Image search + cached download
    pdf_builder.py                Unified ReportLab branded PDF generator
  customers/<slug>/
    config.json                   Brand config (colors, voice, fonts, search prompts, …)
    logo.png                      Optional brand logo
  briefs/<slug>/
    <slug>__<product>__<stamp>.pdf  Generated briefs
    _uploads/                     Source Excels (kept for debugging)
  assets/cache/                   Unsplash image cache
```

## Adding a marketplace

Edit `MARKETPLACES` in `core/config.py`. Each entry needs a label, language code (`en` / `de` / `fr` / `es` / `it`), and currency. The language code is auto-applied as the overlay language — and `core/pdf_builder.OVERLAY_PHRASES` ships standard hook translations for those five languages. Add a new language block there to expand.

## Deploy to Railway (always-on, paid ~$5–10/mo)

Railway runs the app 24/7 with a persistent volume so customer configs + generated briefs survive deploys. Setup is one-time, takes ~10 min.

### 1. Push the repo to GitHub

Railway pulls from GitHub. Create a (private if you want) repo, then:

```bash
cd /Users/jonask/Desktop/Claude_Code
git init && git add . && git commit -m "Initial brief app"
gh repo create equalice-briefs --private --source=. --push
```

The deployment-relevant files (already in this repo):

```
/.dockerignore                          repo-root
/railway.toml                           repo-root, tells Railway which Dockerfile to use
/tools/brief_app/Dockerfile             build recipe
/tools/brief_app/...                    app code
```

### 2. Create the Railway service

1. Sign up at <https://railway.app>
2. **New Project → Deploy from GitHub repo** → pick the repo you just pushed
3. Railway auto-detects `railway.toml` and the Dockerfile

### 3. Add the persistent volume (CRITICAL)

Without this, all customer configs + briefs get wiped on every deploy.

1. In the service, go to **Settings → Volumes → New Volume**
2. Mount path: `/data`
3. Size: 1 GB is plenty for thousands of briefs

### 4. Set environment variables

In **Variables**, add:

| Variable | Value | Required |
|---|---|---|
| `BRIEF_APP_DATA` | `/data` | yes — points the app at the persistent volume |
| `UNSPLASH_ACCESS_KEY` | your Unsplash key | recommended (real moodboard images) |

### 5. Expose the service

1. **Settings → Networking → Generate Domain** → Railway gives you a URL like `equalice-briefs.up.railway.app`
2. Share that URL with the writers — no installation needed on their side, only a browser

### 6. First-boot

On first start, the app sees an empty `/data/customers` folder and auto-seeds the 5 brands shipped with the code (Chekko, Norb, Jotti, SeQR, GSC) into the volume. Writers can edit / extend from there.

### Updating the deployed app

```bash
git add -A && git commit -m "..." && git push
```

Railway auto-redeploys. Customer data on the volume is untouched.

### Cost expectation

Railway has a small free credit each month. After that:

- Smallest instance (~512 MB RAM) is enough — Streamlit + ReportLab is lightweight
- 1 GB persistent volume
- Realistic: **$5–10 / month** for an internal app at this scale.

## Limits / known constraints

- Overlay translations: only standard hooks are localized. Product-specific phrasing (USP-derived sublines) stays English in the brief — flagged for the copywriter to localize before final design.
- Moodboard: 6 tiles max (2×3 grid). More requires layout work.
- The PDF builder uses Helvetica as fallback (ReportLab default). Custom brand fonts (Public Play, Minion etc.) are referenced in the brandbook page but not rendered into the PDF body — the designer applies them in Figma.
