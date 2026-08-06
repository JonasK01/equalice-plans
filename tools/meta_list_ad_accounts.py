#!/usr/bin/env python3
"""
List all Meta Ad Accounts accessible with the current long-lived token.
Reads META_LONG_TOKEN from .env.

Usage: python3 tools/meta_list_ad_accounts.py
"""

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

ACCOUNT_STATUS = {
    1: "ACTIVE",
    2: "DISABLED",
    3: "UNSETTLED",
    7: "PENDING_RISK_REVIEW",
    8: "PENDING_SETTLEMENT",
    9: "IN_GRACE_PERIOD",
    100: "PENDING_CLOSURE",
    101: "CLOSED",
    201: "ANY_ACTIVE",
    202: "ANY_CLOSED",
}


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


def fetch_ad_accounts(token: str, api_version: str) -> list:
    """Fetch ad accounts accessible by the token's user (personal + business)."""
    url = f"https://graph.facebook.com/{api_version}/me/adaccounts"
    params = {
        "access_token": token,
        "fields": "id,account_id,name,account_status,currency,business_name,timezone_name,amount_spent",
        "limit": 100,
    }
    accounts = []
    while url:
        resp = requests.get(url, params=params, timeout=15)
        data = resp.json()
        if "error" in data:
            raise RuntimeError(f"API error: {data['error']}")
        accounts.extend(data.get("data", []))
        paging = data.get("paging", {})
        url = paging.get("next")
        params = None
    return accounts


def fetch_businesses(token: str, api_version: str) -> list:
    url = f"https://graph.facebook.com/{api_version}/me/businesses"
    params = {
        "access_token": token,
        "fields": "id,name,verification_status",
        "limit": 100,
    }
    resp = requests.get(url, params=params, timeout=15)
    data = resp.json()
    if "error" in data:
        return []
    return data.get("data", [])


def main() -> int:
    env = load_env(ENV_PATH)
    token = env.get("META_LONG_TOKEN") or env.get("META_SHORT_TOKEN")
    api_version = env.get("META_API_VERSION", API_VERSION_DEFAULT)

    if not token:
        print("No META_LONG_TOKEN in .env. Run meta_token_exchange.py first.")
        return 1

    print("Fetching businesses...")
    businesses = fetch_businesses(token, api_version)
    if businesses:
        print(f"\nBusiness Portfolios ({len(businesses)}):")
        for b in businesses:
            status = b.get("verification_status", "?")
            print(f"  - {b['name']} (id: {b['id']}, verification: {status})")
    else:
        print("No business portfolios accessible.")

    print("\nFetching ad accounts...")
    accounts = fetch_ad_accounts(token, api_version)

    if not accounts:
        print("\nNo ad accounts accessible with this token.")
        print("Likely causes:")
        print("  - App in Dev Mode + no Business Portfolio linked")
        print("  - Token user has no ad account permissions")
        print("  - Accounts are under Business Managers that haven't granted app access")
        return 0

    print(f"\nAd Accounts ({len(accounts)}):\n")
    for acc in accounts:
        status_code = acc.get("account_status")
        status = ACCOUNT_STATUS.get(status_code, f"UNKNOWN({status_code})")
        name = acc.get("name", "(no name)")
        acc_id = acc.get("id", "?")
        currency = acc.get("currency", "?")
        biz = acc.get("business_name", "(personal)")
        spent = acc.get("amount_spent", "0")
        print(f"  {acc_id}")
        print(f"    Name:     {name}")
        print(f"    Business: {biz}")
        print(f"    Status:   {status}")
        print(f"    Currency: {currency}")
        print(f"    Spent:    {spent} (lifetime, in cents)")
        print()

    return 0


if __name__ == "__main__":
    sys.exit(main())
