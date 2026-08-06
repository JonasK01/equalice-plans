"""Plan review + comments — persisted in the writable /data volume so the whole team
sees the same threads. Each generated plan (a PDF under BRIEFS_DIR/<slug>/) can carry a
comment thread and a simple review status. Used by the app's 'Plans & Review' page and
the post-generation review box.
"""
from __future__ import annotations
import json
import re
import time
from pathlib import Path

from .config import DATA_ROOT, BRIEFS_DIR

COMMENTS_DIR = DATA_ROOT / "comments"

STATUSES = ["open", "approved", "changes requested"]


def _safe(name: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", name or "")


def _thread_file(slug: str, pdf_name: str) -> Path:
    d = COMMENTS_DIR / _safe(slug)
    d.mkdir(parents=True, exist_ok=True)
    return d / (_safe(pdf_name) + ".json")


def _load(slug: str, pdf_name: str) -> dict:
    f = _thread_file(slug, pdf_name)
    if f.exists():
        try:
            return json.loads(f.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"status": "open", "comments": []}


def _save(slug: str, pdf_name: str, data: dict) -> None:
    _thread_file(slug, pdf_name).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def list_comments(slug: str, pdf_name: str) -> list[dict]:
    return _load(slug, pdf_name).get("comments", [])


def get_status(slug: str, pdf_name: str) -> str:
    return _load(slug, pdf_name).get("status", "open")


def add_comment(slug: str, pdf_name: str, author: str, text: str) -> None:
    text = (text or "").strip()
    if not text:
        return
    data = _load(slug, pdf_name)
    data.setdefault("comments", []).append({
        "author": (author or "anon").strip()[:60],
        "text": text[:4000],
        "ts": int(time.time()),
    })
    _save(slug, pdf_name, data)


def set_status(slug: str, pdf_name: str, status: str) -> None:
    if status not in STATUSES:
        return
    data = _load(slug, pdf_name)
    data["status"] = status
    _save(slug, pdf_name, data)


def list_plans(slug: str) -> list[dict]:
    """All generated plan PDFs for a brand, newest first, with comment counts."""
    d = BRIEFS_DIR / slug
    if not d.exists():
        return []
    out = []
    for p in sorted(d.glob("*.pdf"), key=lambda x: x.stat().st_mtime, reverse=True):
        thread = _load(slug, p.name)
        out.append({
            "name": p.name,
            "path": str(p),
            "mtime": int(p.stat().st_mtime),
            "size_kb": p.stat().st_size // 1024,
            "comment_count": len(thread.get("comments", [])),
            "status": thread.get("status", "open"),
        })
    return out
