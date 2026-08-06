"""Unsplash search + cached download for moodboard images.

If no Unsplash access key is set (env UNSPLASH_ACCESS_KEY), the module returns
empty results and the PDF builder falls back to placeholder boxes with the
search-prompt printed inside. The app surfaces a banner asking the user to
add a key.
"""
from __future__ import annotations
import hashlib
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import requests

from .config import CACHE_DIR


UNSPLASH_KEY_ENV = "UNSPLASH_ACCESS_KEY"


@dataclass
class MoodImage:
    query: str
    file_path: Optional[Path]  # None => fallback placeholder
    photographer: str = ""
    photographer_url: str = ""
    unsplash_url: str = ""


def has_unsplash_key() -> bool:
    return bool(os.environ.get(UNSPLASH_KEY_ENV))


def _cache_key(query: str) -> str:
    return hashlib.sha256(query.lower().encode()).hexdigest()[:16]


def search_image(query: str, orientation: str = "landscape") -> MoodImage:
    """Return a MoodImage. If no key or API fails, file_path is None (placeholder)."""
    key = os.environ.get(UNSPLASH_KEY_ENV)
    cache_id = _cache_key(query + ":" + orientation)
    cached_jpg = CACHE_DIR / f"{cache_id}.jpg"
    cached_meta = CACHE_DIR / f"{cache_id}.meta"

    if cached_jpg.exists() and cached_meta.exists():
        meta = cached_meta.read_text().split("|")
        return MoodImage(
            query=query,
            file_path=cached_jpg,
            photographer=meta[0] if len(meta) > 0 else "",
            photographer_url=meta[1] if len(meta) > 1 else "",
            unsplash_url=meta[2] if len(meta) > 2 else "",
        )

    if not key:
        return MoodImage(query=query, file_path=None)

    try:
        r = requests.get(
            "https://api.unsplash.com/search/photos",
            params={"query": query, "orientation": orientation, "per_page": 3, "content_filter": "high"},
            headers={"Authorization": f"Client-ID {key}"},
            timeout=10,
        )
        r.raise_for_status()
        data = r.json()
        results = data.get("results", [])
        if not results:
            return MoodImage(query=query, file_path=None)
        pick = results[0]
        img_url = pick["urls"]["regular"]
        photog = pick["user"]["name"]
        photog_url = pick["user"]["links"]["html"]
        page_url = pick["links"]["html"]

        img = requests.get(img_url, timeout=15)
        img.raise_for_status()
        cached_jpg.write_bytes(img.content)
        cached_meta.write_text(f"{photog}|{photog_url}|{page_url}")
        return MoodImage(
            query=query,
            file_path=cached_jpg,
            photographer=photog,
            photographer_url=photog_url,
            unsplash_url=page_url,
        )
    except Exception:
        return MoodImage(query=query, file_path=None)


def fetch_moodboard(queries: list[str]) -> list[MoodImage]:
    return [search_image(q) for q in queries]
