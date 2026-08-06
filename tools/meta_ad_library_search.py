#!/usr/bin/env python3
"""
Search the Meta Ad Library for ads matching a keyword or page.
Reads META_LONG_TOKEN from .env.

Usage:
    python3 tools/meta_ad_library_search.py <query> [--country DE] [--limit 10] [--active-only]

Examples:
    python3 tools/meta_ad_library_search.py "mosquito spray" --country US --limit 5
    python3 tools/meta_ad_library_search.py "Eggersmann" --country DE
"""

import sys
import json
import argparse
from pathlib import Path
from datetime import datetime

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


def search_ad_library(token: str, api_version: str, query: str, country: str,
                      limit: int, active_only: bool) -> list:
    url = f"https://graph.facebook.com/{api_version}/ads_archive"
    fields = [
        "id",
        "ad_creation_time",
        "ad_delivery_start_time",
        "ad_delivery_stop_time",
        "ad_snapshot_url",
        "page_id",
        "page_name",
        "publisher_platforms",
        "ad_creative_bodies",
        "ad_creative_link_titles",
        "ad_creative_link_descriptions",
        "ad_creative_link_captions",
        "languages",
        "target_locations",
    ]
    params = {
        "access_token": token,
        "search_terms": query,
        "ad_reached_countries": f"['{country}']",
        "ad_type": "ALL",
        "ad_active_status": "ACTIVE" if active_only else "ALL",
        "fields": ",".join(fields),
        "limit": min(limit, 100),
    }
    resp = requests.get(url, params=params, timeout=20)
    data = resp.json()
    if "error" in data:
        raise RuntimeError(f"API error: {data['error']}")
    return data.get("data", [])


def format_ad(ad: dict) -> str:
    lines = []
    page = ad.get("page_name", "?")
    page_id = ad.get("page_id", "?")
    ad_id = ad.get("id", "?")
    start = ad.get("ad_delivery_start_time", "?")
    stop = ad.get("ad_delivery_stop_time", "still running")
    platforms = ", ".join(ad.get("publisher_platforms", []))
    bodies = ad.get("ad_creative_bodies", [])
    titles = ad.get("ad_creative_link_titles", [])
    snapshot = ad.get("ad_snapshot_url", "")

    lines.append(f"  Page:       {page} (id: {page_id})")
    lines.append(f"  Ad ID:      {ad_id}")
    lines.append(f"  Running:    {start[:10] if start != '?' else '?'} → {stop[:10] if stop != 'still running' else 'still running'}")
    lines.append(f"  Platforms:  {platforms or '?'}")
    if titles:
        lines.append(f"  Headline:   {titles[0][:100]}")
    if bodies:
        body_preview = bodies[0][:200].replace("\n", " ")
        lines.append(f"  Copy:       {body_preview}{'...' if len(bodies[0]) > 200 else ''}")
    if snapshot:
        lines.append(f"  Snapshot:   {snapshot}")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Search Meta Ad Library")
    parser.add_argument("query", help="Search term (keyword or page name)")
    parser.add_argument("--country", default="DE", help="Country code (DE, US, GB, etc.)")
    parser.add_argument("--limit", type=int, default=10, help="Max results (default 10)")
    parser.add_argument("--active-only", action="store_true", help="Only active ads")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")
    args = parser.parse_args()

    env = load_env(ENV_PATH)
    token = env.get("META_LONG_TOKEN") or env.get("META_SHORT_TOKEN")
    api_version = env.get("META_API_VERSION", API_VERSION_DEFAULT)

    if not token:
        print("No META_LONG_TOKEN in .env. Run meta_token_exchange.py first.")
        return 1

    print(f"Searching Ad Library: query='{args.query}', country={args.country}, "
          f"limit={args.limit}, active_only={args.active_only}\n")

    ads = search_ad_library(token, api_version, args.query, args.country,
                            args.limit, args.active_only)

    if args.json:
        print(json.dumps(ads, indent=2, ensure_ascii=False))
        return 0

    if not ads:
        print("No ads found. Try:")
        print("  - Different keyword")
        print("  - Different country code")
        print("  - Drop --active-only flag")
        return 0

    print(f"Found {len(ads)} ad(s):\n")
    for i, ad in enumerate(ads, 1):
        print(f"[{i}] " + "-" * 60)
        print(format_ad(ad))
        print()

    return 0


if __name__ == "__main__":
    sys.exit(main())
