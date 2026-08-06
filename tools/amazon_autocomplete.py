#!/usr/bin/env python3
"""
Fetch Amazon autocomplete suggestions for seed keywords.
Usage: python3 tools/amazon_autocomplete.py <keyword> [marketplace]

Marketplace options: de, com, co.uk (default: de)
Supports multiple keywords separated by comma.

Outputs JSON with autocomplete suggestions per keyword.

Endpoint note (2026-05): The legacy `https://{domain}/s/suggest` endpoint stopped
returning JSON; we now use `https://completion.amazon.com/api/2017/suggestions`
which requires the marketplace `mid` (merchant/marketplace ID), not a derived value.
"""

import sys
import json
import time
import random
from urllib.parse import quote

try:
    import requests
except ImportError:
    print("Missing dependencies. Run: pip3 install requests")
    sys.exit(1)


MARKETPLACE_CONFIG = {
    "de": {"domain": "www.amazon.de", "lang": "de_DE", "alias": "aps", "mid": "A1PA6795UKMFR9"},
    "com": {"domain": "www.amazon.com", "lang": "en_US", "alias": "aps", "mid": "ATVPDKIKX0DER"},
    "co.uk": {"domain": "www.amazon.co.uk", "lang": "en_GB", "alias": "aps", "mid": "A1F83G8C2ARO7P"},
    "uk": {"domain": "www.amazon.co.uk", "lang": "en_GB", "alias": "aps", "mid": "A1F83G8C2ARO7P"},
}

USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
]


def get_autocomplete(keyword, marketplace="de"):
    """Fetch autocomplete suggestions for a single keyword."""
    config = MARKETPLACE_CONFIG.get(marketplace, MARKETPLACE_CONFIG["de"])
    domain = config["domain"]
    lang = config["lang"]

    url = "https://completion.amazon.com/api/2017/suggestions"
    params = {
        "session-id": "000-0000000-0000000",
        "customer-id": "",
        "request-id": "",
        "page-type": "Gateway",
        "lop": lang,
        "site-variant": "desktop",
        "client-info": "amazon-search-ui",
        "mid": config["mid"],
        "alias": config["alias"],
        "b2b": 0,
        "fresh": 0,
        "ks": 83,
        "prefix": keyword,
        "event": "onkeypress",
        "limit": 11,
        "fb": 1,
        "suggestion-type": "KEYWORD",
    }

    headers = {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept": "application/json, text/javascript, */*",
        "Accept-Language": "en-US,en;q=0.9,de;q=0.8",
        "Referer": f"https://{domain}/",
    }

    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            suggestions = []
            if "suggestions" in data:
                for item in data["suggestions"]:
                    suggestion = {
                        "keyword": item.get("value", ""),
                    }
                    # Some responses include category info
                    if "nodes" in item:
                        suggestion["category"] = item["nodes"][0].get("name", "") if item["nodes"] else None
                    suggestions.append(suggestion)
            return suggestions
        else:
            return {"error": f"HTTP {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}


def expand_keyword(keyword, marketplace="de"):
    """Expand a keyword by appending a-z and getting suggestions for each."""
    print(f"  Expanding '{keyword}' with alphabet...")
    all_suggestions = set()

    # First get base suggestions
    base = get_autocomplete(keyword, marketplace)
    if isinstance(base, list):
        for s in base:
            all_suggestions.add(s["keyword"])

    # Expand with each letter
    for letter in "abcdefghijklmnopqrstuvwxyz":
        expanded = get_autocomplete(f"{keyword} {letter}", marketplace)
        if isinstance(expanded, list):
            for s in expanded:
                all_suggestions.add(s["keyword"])
        time.sleep(random.uniform(0.2, 0.5))

    return sorted(list(all_suggestions))


def get_suggestions(keywords, marketplace="de", expand=False):
    """Get autocomplete suggestions for multiple keywords."""
    results = {}

    for keyword in keywords:
        keyword = keyword.strip()
        print(f"Fetching suggestions for '{keyword}' on amazon.{marketplace}...")

        if expand:
            results[keyword] = expand_keyword(keyword, marketplace)
        else:
            suggestions = get_autocomplete(keyword, marketplace)
            if isinstance(suggestions, list):
                results[keyword] = [s["keyword"] for s in suggestions]
            else:
                results[keyword] = suggestions

        if len(keywords) > 1:
            time.sleep(random.uniform(0.5, 1.5))

    return results


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 tools/amazon_autocomplete.py <keyword> [marketplace] [--expand]")
        print("       python3 tools/amazon_autocomplete.py \"keyword1,keyword2\" [marketplace]")
        print("Marketplaces: de, com, co.uk")
        print("--expand: Also search keyword + a-z for deeper suggestions")
        sys.exit(1)

    keyword_input = sys.argv[1]
    marketplace = "de"
    expand = False

    for arg in sys.argv[2:]:
        if arg == "--expand":
            expand = True
        else:
            marketplace = arg

    keywords = [k.strip() for k in keyword_input.split(",")]

    results = get_suggestions(keywords, marketplace, expand)
    print(json.dumps(results, indent=2, ensure_ascii=False))
