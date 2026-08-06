#!/usr/bin/env python3
"""
Set the daily (or lifetime) budget of a Meta campaign. WRITES to the live account.
Reads META_LONG_TOKEN from .env.

Usage:
    python3 tools/meta_set_campaign_budget.py <campaign_id> --daily 305
    python3 tools/meta_set_campaign_budget.py <campaign_id> --daily 305 --confirm

Without --confirm it does a DRY RUN (shows current vs. new, changes nothing).
Budget is given in account currency units (e.g. dollars), converted to cents.
"""

import argparse
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


def get_campaign(token, ver, cid):
    url = f"https://graph.facebook.com/{ver}/{cid}"
    params = {"access_token": token,
              "fields": "name,status,effective_status,daily_budget,lifetime_budget,bid_strategy"}
    r = requests.get(url, params=params, timeout=20).json()
    if "error" in r:
        raise RuntimeError(r["error"])
    return r


def set_budget(token, ver, cid, field, cents):
    url = f"https://graph.facebook.com/{ver}/{cid}"
    r = requests.post(url, data={"access_token": token, field: cents}, timeout=20).json()
    if isinstance(r, dict) and "error" in r:
        raise RuntimeError(r["error"])
    return r


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("campaign_id")
    p.add_argument("--daily", type=float, help="new daily budget in account currency")
    p.add_argument("--lifetime", type=float, help="new lifetime budget in account currency")
    p.add_argument("--confirm", action="store_true", help="actually apply (otherwise dry run)")
    args = p.parse_args()

    if not args.daily and not args.lifetime:
        print("Provide --daily or --lifetime.")
        return 1

    env = load_env(ENV_PATH)
    token = env.get("META_LONG_TOKEN") or env.get("META_SHORT_TOKEN")
    ver = env.get("META_API_VERSION", API_VERSION_DEFAULT)
    if not token:
        print("No META_LONG_TOKEN in .env.")
        return 1

    field = "daily_budget" if args.daily else "lifetime_budget"
    new_units = args.daily if args.daily else args.lifetime
    new_cents = int(round(new_units * 100))

    camp = get_campaign(token, ver, args.campaign_id)
    cur = camp.get(field)
    cur_units = f"{int(cur)/100:.2f}" if cur else "-"
    print(f"Campaign:  {camp.get('name')} ({camp.get('effective_status')})")
    print(f"{field}:  {cur_units}  ->  {new_units:.2f}")

    if not args.confirm:
        print("\nDRY RUN — nothing changed. Re-run with --confirm to apply.")
        return 0

    set_budget(token, ver, args.campaign_id, field, new_cents)
    after = get_campaign(token, ver, args.campaign_id)
    av = after.get(field)
    print(f"\nApplied. {field} now: {int(av)/100:.2f}" if av else "Applied.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
