"""Paths and environment for the campaign dashboard.

Mirrors the pattern in tools/brief_app/core/config.py: a single env var
(CAMPAIGN_DASH_DATA) controls where mutable data lives, defaulting to a local
./data folder next to the app so it works instantly in dev.
"""

import os
from pathlib import Path

CODE_ROOT = Path(__file__).resolve().parent.parent          # tools/campaign_dashboard
PROJECT_ROOT = CODE_ROOT.parent.parent                       # repo root
TOOLS_DIR = CODE_ROOT.parent                                 # tools/
ENV_PATH = PROJECT_ROOT / ".env"
TMP_DIR = PROJECT_ROOT / ".tmp"

DATA_ROOT = Path(os.environ.get("CAMPAIGN_DASH_DATA", str(CODE_ROOT / "data")))
INFLUENCERS_DIR = DATA_ROOT / "influencers"
CREATIVES_DIR = DATA_ROOT / "creatives"
CALENDAR_DIR = DATA_ROOT / "calendar"
SETTINGS_PATH = DATA_ROOT / "settings.json"
AUDIT_LOG_PATH = DATA_ROOT / "budget_audit_log.json"

# Default account = Dr. Denese (SkinScience Labs main ad account)
DEFAULT_ACCOUNT_ID = "act_2088057028161457"

# Read-only context panels surfaced in the dashboard
PERSONA_MD = TMP_DIR / "dr_denese_persona.md"
LEARNINGS_MD = TMP_DIR / "dr_denese_meta_learnings.md"
BRIEFS_MD = TMP_DIR / "dr_denese_hydroshield_creative_briefs.md"


def ensure_dirs() -> None:
    for d in (DATA_ROOT, INFLUENCERS_DIR, CREATIVES_DIR, CALENDAR_DIR):
        d.mkdir(parents=True, exist_ok=True)
