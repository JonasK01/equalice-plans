#!/usr/bin/env python3
"""
Exchange a short-lived Meta user access token for a long-lived one (~60 days).
Reads META_APP_ID, META_APP_SECRET, META_SHORT_TOKEN from .env.
Writes the result back into .env as META_LONG_TOKEN.

Usage: python3 tools/meta_token_exchange.py
"""

import os
import sys
import re
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


def upsert_env_key(path: Path, key: str, value: str) -> None:
    text = path.read_text() if path.exists() else ""
    pattern = re.compile(rf"^{re.escape(key)}=.*$", re.MULTILINE)
    if pattern.search(text):
        text = pattern.sub(f"{key}={value}", text)
    else:
        text = text.rstrip() + f"\n{key}={value}\n"
    path.write_text(text)


def exchange_token(app_id: str, app_secret: str, short_token: str, api_version: str) -> dict:
    url = f"https://graph.facebook.com/{api_version}/oauth/access_token"
    params = {
        "grant_type": "fb_exchange_token",
        "client_id": app_id,
        "client_secret": app_secret,
        "fb_exchange_token": short_token,
    }
    resp = requests.get(url, params=params, timeout=15)
    data = resp.json()
    if resp.status_code != 200 or "access_token" not in data:
        raise RuntimeError(f"Token exchange failed: {data}")
    return data


def debug_token(token: str, app_id: str, app_secret: str, api_version: str) -> dict:
    url = f"https://graph.facebook.com/{api_version}/debug_token"
    params = {
        "input_token": token,
        "access_token": f"{app_id}|{app_secret}",
    }
    resp = requests.get(url, params=params, timeout=15)
    return resp.json().get("data", {})


def main() -> int:
    env = load_env(ENV_PATH)
    app_id = env.get("META_APP_ID")
    app_secret = env.get("META_APP_SECRET")
    short_token = env.get("META_SHORT_TOKEN")
    api_version = env.get("META_API_VERSION", API_VERSION_DEFAULT)

    missing = [k for k, v in {
        "META_APP_ID": app_id,
        "META_APP_SECRET": app_secret,
        "META_SHORT_TOKEN": short_token,
    }.items() if not v]
    if missing:
        print(f"Missing in .env: {', '.join(missing)}")
        return 1

    print("Exchanging short-lived token for long-lived token...")
    result = exchange_token(app_id, app_secret, short_token, api_version)
    long_token = result["access_token"]
    expires_in = result.get("expires_in")

    upsert_env_key(ENV_PATH, "META_LONG_TOKEN", long_token)
    print("Long-lived token written to .env as META_LONG_TOKEN")

    if expires_in:
        days = expires_in // 86400
        print(f"Token lifetime: ~{days} days ({expires_in} seconds)")
    else:
        print("Token lifetime: not specified (typically long-lived ~60 days)")

    info = debug_token(long_token, app_id, app_secret, api_version)
    if info:
        scopes = info.get("scopes", [])
        user_id = info.get("user_id", "?")
        is_valid = info.get("is_valid", False)
        print(f"\nToken info:")
        print(f"  Valid: {is_valid}")
        print(f"  User ID: {user_id}")
        print(f"  Scopes: {', '.join(scopes) if scopes else '(none)'}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
