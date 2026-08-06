#!/usr/bin/env python3
"""
Pull spend (and basic delivery metrics) for a Meta ad account over a date range.
Reads META_LONG_TOKEN from .env. Uses the free Graph API insights endpoint.

Usage:
    python3 tools/meta_account_spend.py act_2088057028161457 --since 2026-06-13 --until 2026-06-13
    python3 tools/meta_account_spend.py act_2088057028161457 --date-preset yesterday
"""

import argparse
import os
import sys
from pathlib import Path

try:
    import requests
except ImportError:
    print("Missing dependency. Run: pip3 install requests")
    sys.exit(1)


PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENV_PATH = PROJECT_ROOT / ".env"
API_VERSION_DEFAULT = "v21.0"


def load_env(path: Path) -> dict:
    env = {}
    if not path.exists():
        return env
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        env[key.strip()] = value.strip()
    return env


def fetch_insights(token, api_version, account_id, since, until, date_preset,
                   level="account", time_increment=None, extra_fields=False):
    if not account_id.startswith("act_"):
        account_id = f"act_{account_id}"
    url = f"https://graph.facebook.com/{api_version}/{account_id}/insights"
    fields = "spend,impressions,clicks,cpc,cpm,ctr,account_currency,account_name"
    if level == "campaign":
        fields += ",campaign_name"
    if extra_fields:
        fields += ",actions,action_values,purchase_roas"
    params = {
        "access_token": token,
        "fields": fields,
        "level": level,
        "limit": 200,
    }
    if date_preset:
        params["date_preset"] = date_preset
    else:
        params["time_range"] = '{"since":"%s","until":"%s"}' % (since, until)
    if time_increment:
        params["time_increment"] = time_increment
    rows = []
    while url:
        resp = requests.get(url, params=params, timeout=30)
        data = resp.json()
        if "error" in data:
            raise RuntimeError(f"API error: {data['error']}")
        rows.extend(data.get("data", []))
        url = data.get("paging", {}).get("next")
        params = None
    return rows


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("account_id")
    p.add_argument("--since")
    p.add_argument("--until")
    p.add_argument("--date-preset", dest="date_preset")
    args = p.parse_args()

    if not args.date_preset and not (args.since and args.until):
        print("Provide either --date-preset or both --since and --until.")
        return 1

    env = load_env(ENV_PATH)
    token = env.get("META_LONG_TOKEN") or env.get("META_SHORT_TOKEN")
    api_version = env.get("META_API_VERSION", API_VERSION_DEFAULT)
    if not token:
        print("No META_LONG_TOKEN in .env.")
        return 1

    rows = fetch_insights(token, api_version, args.account_id,
                          args.since, args.until, args.date_preset)
    if not rows:
        print("No data (no spend in that window, or account had no active ads).")
        return 0

    for r in rows:
        cur = r.get("account_currency", "?")
        print(f"Account:     {r.get('account_name', '?')}")
        print(f"Spend:       {r.get('spend', '0')} {cur}")
        print(f"Impressions: {r.get('impressions', '0')}")
        print(f"Clicks:      {r.get('clicks', '0')}")
        print(f"CPC:         {r.get('cpc', '?')} {cur}")
        print(f"CPM:         {r.get('cpm', '?')} {cur}")
        print(f"CTR:         {r.get('ctr', '?')} %")
    return 0


if __name__ == "__main__":
    sys.exit(main())
