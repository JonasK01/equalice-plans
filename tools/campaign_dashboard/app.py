"""Campaign-Ops Dashboard — Streamlit entry point.

Run: streamlit run tools/campaign_dashboard/app.py
A sidebar switches between the four modules; each lives in pages_impl/.
"""

import sys
from pathlib import Path

import streamlit as st

# Allow `from core...` and `from pages_impl...` when run via `streamlit run`
APP_DIR = Path(__file__).resolve().parent
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from core import config, store, seed          # noqa: E402
from pages_impl import (                       # noqa: E402
    performance, pipeline, influencers, calendar_budget,
)

st.set_page_config(page_title="Dr. Denese — Campaign Ops",
                   page_icon="📊", layout="wide")

# First-boot: ensure dirs + seed creative pipeline from the briefs
config.ensure_dirs()
seed.seed_if_empty()

PAGES = {
    "📈 Performance & Budget": performance.render,
    "🎬 Creative-Pipeline": pipeline.render,
    "🤝 Influencer-CRM": influencers.render,
    "🗓️ Kalender & Pacing": calendar_budget.render,
}

st.sidebar.title("📊 Campaign Ops")
st.sidebar.caption("Dr. Denese · HYDROSHIELD")
choice = st.sidebar.radio("Modul", list(PAGES.keys()), label_visibility="collapsed")

settings = store.load_settings()
st.sidebar.divider()
st.sidebar.caption(f"Account: `{settings['account_id']}`")
st.sidebar.caption(f"Influencer: {len(store.list_influencers())} · "
                   f"Creatives: {len(store.list_creatives())}")

PAGES[choice]()
