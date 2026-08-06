"""Dataclasses for the dashboard's persisted entities.

Everything is plain JSON-serialisable so store.py can round-trip via
dataclasses.asdict / from-dict without a database.
"""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Optional

# --- controlled vocabularies (kept here so UI + validation share one source) ---
INFLUENCER_STATUS = [
    "prospect", "contacted", "negotiating", "contracted",
    "active", "completed", "dropped",
]
INFLUENCER_TIERS = ["nano", "micro", "mid", "macro"]
FEE_MODELS = ["flat", "per_video", "affiliate", "gifted", "hybrid"]
SCRIPT_STATUS = ["needed", "drafted", "approved", "sent"]
PRODUCT_STATUS = ["needed", "requested", "shipped", "delivered"]
DELIVERABLE_STATUS = ["planned", "in_progress", "submitted", "approved", "live"]

CREATIVE_STATUS = ["Idea", "Brief", "Production", "Ready", "Live", "Result"]
FUNNEL_STAGES = ["TOF", "MOF", "BOF", "Retargeting"]

EVENT_TYPES = ["shoot", "post", "launch", "budget_change", "other"]
EVENT_STATUS = ["planned", "confirmed", "done", "cancelled"]


@dataclass
class Deliverable:
    type: str = "Reel"            # Reel / Story / UGC raw / Static / Carousel
    count: int = 1
    due_date: str = ""            # ISO date
    status: str = "planned"
    brief_ref: str = ""           # links to a CreativeItem id or brief section


@dataclass
class Influencer:
    slug: str
    name: str
    tier: str = "micro"
    status: str = "prospect"
    handles: dict = field(default_factory=dict)        # {"instagram": url, "tiktok": url}
    fee: float = 0.0
    fee_model: str = "flat"
    contract_start: str = ""
    contract_end: str = ""
    contract_link: str = ""
    deliverables: list = field(default_factory=list)   # list[Deliverable as dict]
    script_status: str = "needed"
    product_status: str = "needed"
    product_tracking: str = ""
    linked_creative_ids: list = field(default_factory=list)
    contact: str = ""                                  # email / phone / agent
    notes: str = ""
    created_at: str = ""
    updated_at: str = ""

    def to_dict(self) -> dict:
        return asdict(self)

    @staticmethod
    def from_dict(d: dict) -> "Influencer":
        known = {f for f in Influencer.__dataclass_fields__}
        return Influencer(**{k: v for k, v in d.items() if k in known})


@dataclass
class CreativeItem:
    id: str
    title: str
    angle: str = ""
    funnel_stage: str = "TOF"
    format: str = "9:16 Reel"
    status: str = "Brief"
    brief_ref: str = ""
    assigned_influencer_slug: str = ""
    live_campaign_id: str = ""
    live_ad_id: str = ""
    result: dict = field(default_factory=dict)         # {"roas":, "spend":, "purchases":}
    compliance_flag: bool = False
    compliance_notes: str = ""
    notes: str = ""
    created_at: str = ""
    updated_at: str = ""

    def to_dict(self) -> dict:
        return asdict(self)

    @staticmethod
    def from_dict(d: dict) -> "CreativeItem":
        known = {f for f in CreativeItem.__dataclass_fields__}
        return CreativeItem(**{k: v for k, v in d.items() if k in known})


@dataclass
class CalendarEvent:
    id: str
    date: str                                          # ISO date
    title: str
    type: str = "post"
    status: str = "planned"
    creative_id: str = ""
    influencer_slug: str = ""
    notes: str = ""

    def to_dict(self) -> dict:
        return asdict(self)

    @staticmethod
    def from_dict(d: dict) -> "CalendarEvent":
        known = {f for f in CalendarEvent.__dataclass_fields__}
        return CalendarEvent(**{k: v for k, v in d.items() if k in known})
