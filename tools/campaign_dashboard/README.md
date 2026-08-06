# Campaign-Ops Dashboard

Streamlit operations cockpit for the Dr. Denese / HYDROSHIELD Meta-ads account.
Four modules in one app:

1. **Performance & Budget** — live Meta insights (spend / ROAS / purchases) by
   account and campaign, daily trend, and **gated** daily-budget editing
   (confirm checkbox + audit log) reusing `tools/meta_set_campaign_budget.py`.
2. **Creative-Pipeline** — board of creatives by status (Idea → Brief →
   Production → Ready → Live → Result), seeded from the 5 HYDROSHIELD briefs,
   linked to influencers and to live campaigns.
3. **Influencer-CRM** — roster + contract / fee / script / product-seeding
   tracking, deliverables per influencer, and a capacity planner
   (videos-target → influencers needed → management load).
4. **Kalender & Pacing** — content calendar (shoots/posts/launches) and
   cumulative spend vs. monthly budget target.

## Run locally

```bash
bash tools/campaign_dashboard/run.sh      # → http://localhost:8501
```

Needs `META_LONG_TOKEN` in the repo-root `.env` (already present). Live data is
pulled on demand and cached briefly with `st.cache_data`.

## Data

Persisted as plain JSON under `tools/campaign_dashboard/data/` (gitignored),
one file per entity — same file-based pattern as `tools/brief_app`. Override the
location with `CAMPAIGN_DASH_DATA=/path` (e.g. a Railway volume).

```
data/
├── influencers/<slug>.json
├── creatives/<id>.json
├── calendar/events.json
├── settings.json
└── budget_audit_log.json
```

## Architecture

- `core/config.py` — paths + `CAMPAIGN_DASH_DATA` env (mirrors brief_app).
- `core/models.py` — dataclasses + controlled vocabularies.
- `core/store.py` — JSON CRUD.
- `core/meta_api.py` — thin wrappers importing `tools/meta_*.py` functions.
- `core/seed.py` — first-boot creative seed from the briefs.
- `pages_impl/*.py` — one `render()` per module, dispatched by `app.py`.

## Deploy (later)

Railway-ready via the same pattern as `brief_app` (Dockerfile + persistent
volume at `/data`, `CAMPAIGN_DASH_DATA=/data`). Not set up yet — local first.
