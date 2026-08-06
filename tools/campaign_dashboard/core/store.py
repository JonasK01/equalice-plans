"""File-based JSON persistence. One file per entity, no database.

Mirrors tools/brief_app/core/customers.py: load/list/save/delete over a
DATA_ROOT directory, with ISO timestamps stamped on save.
"""

from __future__ import annotations

import json
import re
import time
from pathlib import Path
from typing import Optional

from . import config
from .models import Influencer, CreativeItem, CalendarEvent


def _now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%S")


def slugify(name: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return s or "item"


def _read_json(path: Path, default):
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text())
    except (json.JSONDecodeError, OSError):
        return default


def _write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False))


# ---------------- Influencers ----------------
def list_influencers() -> list[Influencer]:
    config.ensure_dirs()
    out = []
    for f in sorted(config.INFLUENCERS_DIR.glob("*.json")):
        d = _read_json(f, None)
        if d:
            out.append(Influencer.from_dict(d))
    return out


def load_influencer(slug: str) -> Optional[Influencer]:
    d = _read_json(config.INFLUENCERS_DIR / f"{slug}.json", None)
    return Influencer.from_dict(d) if d else None


def save_influencer(inf: Influencer) -> Influencer:
    config.ensure_dirs()
    if not inf.created_at:
        inf.created_at = _now()
    inf.updated_at = _now()
    _write_json(config.INFLUENCERS_DIR / f"{inf.slug}.json", inf.to_dict())
    return inf


def delete_influencer(slug: str) -> None:
    p = config.INFLUENCERS_DIR / f"{slug}.json"
    if p.exists():
        p.unlink()


# ---------------- Creatives ----------------
def list_creatives() -> list[CreativeItem]:
    config.ensure_dirs()
    out = []
    for f in sorted(config.CREATIVES_DIR.glob("*.json")):
        d = _read_json(f, None)
        if d:
            out.append(CreativeItem.from_dict(d))
    return out


def load_creative(cid: str) -> Optional[CreativeItem]:
    d = _read_json(config.CREATIVES_DIR / f"{cid}.json", None)
    return CreativeItem.from_dict(d) if d else None


def save_creative(item: CreativeItem) -> CreativeItem:
    config.ensure_dirs()
    if not item.created_at:
        item.created_at = _now()
    item.updated_at = _now()
    _write_json(config.CREATIVES_DIR / f"{item.id}.json", item.to_dict())
    return item


def delete_creative(cid: str) -> None:
    p = config.CREATIVES_DIR / f"{cid}.json"
    if p.exists():
        p.unlink()


# ---------------- Calendar (single file list) ----------------
def _events_path() -> Path:
    return config.CALENDAR_DIR / "events.json"


def list_events() -> list[CalendarEvent]:
    config.ensure_dirs()
    raw = _read_json(_events_path(), [])
    return [CalendarEvent.from_dict(d) for d in raw]


def save_events(events: list[CalendarEvent]) -> None:
    _write_json(_events_path(), [e.to_dict() for e in events])


def upsert_event(event: CalendarEvent) -> None:
    events = list_events()
    events = [e for e in events if e.id != event.id]
    events.append(event)
    save_events(events)


def delete_event(event_id: str) -> None:
    save_events([e for e in list_events() if e.id != event_id])


# ---------------- Settings ----------------
DEFAULT_SETTINGS = {
    "account_id": config.DEFAULT_ACCOUNT_ID,
    "monthly_video_target": 12,
    "videos_per_influencer_per_month": 3,
    "managed_per_person": 8,            # influencers one manager can handle
    "budget_targets": {},               # {campaign_id: monthly_target_usd}
}


def load_settings() -> dict:
    s = dict(DEFAULT_SETTINGS)
    s.update(_read_json(config.SETTINGS_PATH, {}))
    return s


def save_settings(settings: dict) -> None:
    config.ensure_dirs()
    _write_json(config.SETTINGS_PATH, settings)


# ---------------- Budget audit log ----------------
def append_audit(entry: dict) -> None:
    config.ensure_dirs()
    log = _read_json(config.AUDIT_LOG_PATH, [])
    entry["ts"] = _now()
    log.append(entry)
    _write_json(config.AUDIT_LOG_PATH, log)


def list_audit() -> list[dict]:
    return _read_json(config.AUDIT_LOG_PATH, [])
