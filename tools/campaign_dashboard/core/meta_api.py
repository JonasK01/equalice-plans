"""Thin wrappers over the existing tools/meta_*.py scripts.

The meta tools are flat scripts in tools/, so we add that dir to sys.path and
import their module-level functions instead of duplicating Graph API logic.
"""

from __future__ import annotations

import sys

import requests

from . import config

# Make tools/ importable (flat scripts: meta_account_spend.py, etc.)
if str(config.TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(config.TOOLS_DIR))

import meta_account_spend as _spend          # noqa: E402
import meta_list_ad_accounts as _accounts    # noqa: E402
import meta_set_campaign_budget as _budget   # noqa: E402

API_VERSION_DEFAULT = "v21.0"


def _creds() -> tuple[str, str]:
    env = _spend.load_env(config.ENV_PATH)
    token = env.get("META_LONG_TOKEN") or env.get("META_SHORT_TOKEN")
    ver = env.get("META_API_VERSION", API_VERSION_DEFAULT)
    if not token:
        raise RuntimeError("Kein META_LONG_TOKEN in .env gefunden.")
    return token, ver


# ---------------- read ----------------
def list_accounts() -> list[dict]:
    token, ver = _creds()
    return _accounts.fetch_ad_accounts(token, ver)


def insights(account_id: str, *, date_preset=None, since=None, until=None,
             level="account", time_increment=None, extra_fields=True) -> list[dict]:
    token, ver = _creds()
    return _spend.fetch_insights(token, ver, account_id, since, until,
                                 date_preset, level=level,
                                 time_increment=time_increment,
                                 extra_fields=extra_fields)


def campaigns(account_id: str) -> list[dict]:
    """List campaigns with budget + status (no dedicated tool fn — query here)."""
    token, ver = _creds()
    if not account_id.startswith("act_"):
        account_id = f"act_{account_id}"
    url = f"https://graph.facebook.com/{ver}/{account_id}/campaigns"
    params = {
        "access_token": token,
        "limit": 200,
        "fields": "id,name,status,effective_status,daily_budget,"
                  "lifetime_budget,bid_strategy,objective",
    }
    rows = []
    while url:
        d = requests.get(url, params=params, timeout=30).json()
        if "error" in d:
            raise RuntimeError(d["error"])
        rows.extend(d.get("data", []))
        url = d.get("paging", {}).get("next")
        params = None
    return rows


def get_campaign(cid: str) -> dict:
    token, ver = _creds()
    return _budget.get_campaign(token, ver, cid)


# ---------------- write (gated by caller) ----------------
def set_daily_budget(cid: str, dollars: float) -> dict:
    """Apply a new daily budget. Caller MUST confirm before invoking."""
    token, ver = _creds()
    cents = int(round(dollars * 100))
    _budget.set_budget(token, ver, cid, "daily_budget", cents)
    return _budget.get_campaign(token, ver, cid)


# ---------------- parsing helpers ----------------
def _num(x) -> float:
    try:
        return float(x)
    except (TypeError, ValueError):
        return 0.0


def _action_value(row: dict, keys: tuple[str, ...], value_field: bool) -> float:
    arr = row.get("action_values" if value_field else "actions", []) or []
    for a in arr:
        if a.get("action_type") in keys:
            return _num(a.get("value"))
    return 0.0


_PURCHASE_KEYS = (
    "purchase", "omni_purchase", "offsite_conversion.fb_pixel_purchase",
)


def summarise(row: dict) -> dict:
    """Flatten one insights row into spend/purchases/revenue/roas/etc."""
    spend = _num(row.get("spend"))
    imp = _num(row.get("impressions"))
    clk = _num(row.get("clicks"))
    purchases = _action_value(row, _PURCHASE_KEYS, False)
    revenue = _action_value(row, _PURCHASE_KEYS, True)
    roas_arr = row.get("purchase_roas") or []
    roas = _num(roas_arr[0].get("value")) if roas_arr else (
        revenue / spend if spend else 0.0)
    return {
        "name": row.get("campaign_name") or row.get("account_name") or "",
        "date_start": row.get("date_start", ""),
        "spend": round(spend, 2),
        "impressions": int(imp),
        "clicks": int(clk),
        "ctr": round(clk / imp * 100, 2) if imp else 0.0,
        "cpc": round(spend / clk, 2) if clk else 0.0,
        "purchases": int(purchases),
        "revenue": round(revenue, 2),
        "roas": round(roas, 2),
        "cpa": round(spend / purchases, 2) if purchases else 0.0,
        "currency": row.get("account_currency", "USD"),
    }
