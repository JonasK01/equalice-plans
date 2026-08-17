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


def _seed_customers() -> list[str]:
    """Copy brands that ship with the code onto the data volume — ADDITIVELY.

    The old version only ran when the volume was completely empty, i.e. once, on the
    very first boot. That meant a brand added to the repo later never reached a running
    server: the volume already had brands, so seeding returned immediately and the new
    folder was silently skipped forever.

    Now every seed brand is checked individually. A brand the volume does not have yet
    is copied in full (config, logo, brand study, products). A brand it already has is
    left completely alone — the team edits brands through the UI and those edits live
    only on the volume, so overwriting them would destroy work that exists nowhere else.
    Never make this function overwrite; 'missing' is the only condition it may act on."""
    if DATA_ROOT == CODE_ROOT:
        return []                      # dev: code and data are the same folder
    if not SEED_CUSTOMERS_DIR.exists():
        return []
    import shutil
    added: list[str] = []
    for cfg in sorted(SEED_CUSTOMERS_DIR.glob("*/config.json")):
        slug = cfg.parent.name
        if slug.startswith("_"):
            continue                   # scaffolding folders like _TEMPLATE
        target = CUSTOMERS_DIR / slug
        if (target / "config.json").exists():
            continue                   # already on the volume — hands off
        try:
            # copy the whole brand, not just config + logo: brand_study.md and the
            # products folder are what make the brand usable, and the old partial
            # copy left seeded brands looking empty in the UI.
            shutil.copytree(cfg.parent, target, dirs_exist_ok=True)
            added.append(slug)
        except Exception:
            continue                   # a bad seed folder must never break boot
    return added


SEEDED_ON_BOOT = _seed_customers()

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
