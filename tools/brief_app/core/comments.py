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

# The plan's journey through the team. "SEO check" was added on team feedback: after the
# design team has worked a plan, SEO looks at it once more before it ships, so keyword and
# listing-copy problems are caught before the creative is produced, not after.
STATUSES = ["open", "changes requested", "design done", "SEO check", "approved"]

# Shown in the UI so nobody has to guess what a status means.
STATUS_HELP = {
    "open": "Neu generiert, noch niemand dran.",
    "changes requested": "Kommentare da, Plan muss überarbeitet werden.",
    "design done": "Design-Team ist fertig, wartet auf den SEO-Check.",
    "SEO check": "Liegt bei SEO zur finalen Prüfung (Keywords, Titel, Bullets).",
    "approved": "Freigegeben. Fertig.",
}

# Legacy threads may carry a status that no longer exists — map it forward instead of
# silently resetting someone's review state to "open".
_LEGACY = {"in review": "SEO check", "done": "approved"}


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
    s = _load(slug, pdf_name).get("status", "open")
    s = _LEGACY.get(s, s)
    return s if s in STATUSES else "open"


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


def plan_family(pdf_name: str) -> str:
    """The plan this file is a version OF.

    A plan accumulates versions: the original, '__rev-<stamp>' from working in the review
    comments, and '__edit-<stamp>' from the in-app editor. Stripping those suffixes groups
    every version of the same plan together, so the team can see which one is current
    instead of scanning a flat list of near-identical filenames (team feedback: "welches
    ist jetzt die aktuellste Version, aktuell sehr unübersichtlich")."""
    base = pdf_name[:-4] if pdf_name.lower().endswith(".pdf") else pdf_name
    return re.sub(r"(__(rev|edit)-\d{8}_\d{6})+$", "", base)


def list_plans(slug: str) -> list[dict]:
    """All generated plan PDFs for a brand, newest first, with comment counts.

    Each entry also carries its version family, its position in that family, and whether it
    is the current version — so the UI can label it instead of leaving the team guessing."""
    d = BRIEFS_DIR / slug
    if not d.exists():
        return []
    files = sorted(d.glob("*.pdf"), key=lambda x: x.stat().st_mtime, reverse=True)

    # newest file per family wins the "current" flag
    fam_files: dict[str, list] = {}
    for p in files:
        fam_files.setdefault(plan_family(p.name), []).append(p)

    out = []
    for p in files:
        fam = plan_family(p.name)
        siblings = fam_files[fam]                       # already newest-first
        idx = siblings.index(p)
        thread = _load(slug, p.name)
        st = thread.get("status", "open")
        st = _LEGACY.get(st, st)
        out.append({
            "name": p.name,
            "path": str(p),
            "mtime": int(p.stat().st_mtime),
            "size_kb": p.stat().st_size // 1024,
            "comment_count": len(thread.get("comments", [])),
            "status": st if st in STATUSES else "open",
            "family": fam,
            "version": len(siblings) - idx,             # v1 = oldest
            "versions_total": len(siblings),
            "is_latest": idx == 0,
        })
    return out
