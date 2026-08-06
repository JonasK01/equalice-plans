import os
from pathlib import Path

# CODE_ROOT — where the app code lives (does not need to be writable in prod).
CODE_ROOT = Path(__file__).resolve().parent.parent

# DATA_ROOT — where customer configs, generated briefs, and the image cache live.
# In dev: defaults to the same folder as the code so the app works out of the box.
# In Railway / production: set BRIEF_APP_DATA=/data and mount a persistent volume there
# so customer JSONs and PDFs survive deploys.
DATA_ROOT = Path(os.environ.get("BRIEF_APP_DATA", str(CODE_ROOT)))

CUSTOMERS_DIR = DATA_ROOT / "customers"
BRIEFS_DIR = DATA_ROOT / "briefs"
CACHE_DIR = DATA_ROOT / "assets" / "cache"

# Seed customer configs that ship with the code — copied to DATA_ROOT on first boot.
SEED_CUSTOMERS_DIR = CODE_ROOT / "customers"

for p in (CUSTOMERS_DIR, BRIEFS_DIR, CACHE_DIR):
    p.mkdir(parents=True, exist_ok=True)


def _seed_customers_if_empty() -> None:
    """First-boot seeding: if the DATA_ROOT customers folder is empty (fresh deploy
    with a new volume), copy the seed customers shipped with the code into it."""
    if DATA_ROOT == CODE_ROOT:
        return
    if any(CUSTOMERS_DIR.glob("*/config.json")):
        return
    if not SEED_CUSTOMERS_DIR.exists():
        return
    import shutil
    for cfg in SEED_CUSTOMERS_DIR.glob("*/config.json"):
        if cfg.parent.name.startswith("_"):
            continue  # skip scaffolding folders like _TEMPLATE
        target = CUSTOMERS_DIR / cfg.parent.name
        target.mkdir(parents=True, exist_ok=True)
        shutil.copy2(cfg, target / "config.json")
        for extra in cfg.parent.glob("logo.*"):
            shutil.copy2(extra, target / extra.name)


_seed_customers_if_empty()

MARKETPLACES = {
    "amazon.com": {"label": "amazon.com (US)", "lang": "en", "currency": "USD"},
    "amazon.de": {"label": "amazon.de (DE)", "lang": "de", "currency": "EUR"},
    "amazon.co.uk": {"label": "amazon.co.uk (UK)", "lang": "en", "currency": "GBP"},
    "amazon.fr": {"label": "amazon.fr (FR)", "lang": "fr", "currency": "EUR"},
    "amazon.es": {"label": "amazon.es (ES)", "lang": "es", "currency": "EUR"},
    "amazon.it": {"label": "amazon.it (IT)", "lang": "it", "currency": "EUR"},
}

PERSONALITY_OPTIONS = [
    "Modern", "Luxurious", "Heritage", "Playful", "Bold",
    "Calm", "Scientific", "Creative/Original", "Friendly", "Premium",
    "Minimalist", "Warm",
]
