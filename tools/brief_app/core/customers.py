"""Customer config CRUD. Each customer = one folder under customers/<slug>/ with config.json + optional logo."""
from __future__ import annotations
import json
import re
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path
from typing import Optional

from .config import CUSTOMERS_DIR


def slugify(name: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "-", name).strip("-").lower()
    return s or "customer"


@dataclass
class Customer:
    slug: str
    name: str
    marketplace: str = "amazon.com"
    overlay_language: str = "en"
    primary_color: str = "#222222"
    accent_color: str = "#888888"
    text_color: str = "#000000"
    background_color: str = "#FFFFFF"
    mood_background_color: str = "#F5F1EA"
    voice: str = ""
    tagline: str = ""
    personality: list[str] = field(default_factory=list)
    fonts: list[str] = field(default_factory=lambda: ["Inter"])
    photo_rules: str = ""
    no_gos: str = ""
    moodboard_search_terms: list[str] = field(default_factory=list)
    creative_freedom: int = 4
    logo_path: Optional[str] = None
    notes: str = ""
    new_brand: bool = False          # True -> builder drops the A+ Comparison module (house rule)
    brand_statement: str = ""        # "From the Brand" cool statement appended to the A+ Q&A module
    created_at: str = ""
    updated_at: str = ""

    def folder(self) -> Path:
        return CUSTOMERS_DIR / self.slug

    def to_json(self) -> dict:
        return asdict(self)


def list_customers() -> list[Customer]:
    customers: list[Customer] = []
    for cfg in sorted(CUSTOMERS_DIR.glob("*/config.json")):
        if cfg.parent.name.startswith("_"):
            continue  # skip scaffolding folders like _TEMPLATE
        try:
            customers.append(load_customer(cfg.parent.name))
        except Exception:
            continue
    return customers


def load_customer(slug: str) -> Customer:
    cfg = CUSTOMERS_DIR / slug / "config.json"
    with cfg.open() as f:
        data = json.load(f)
    return Customer(**data)


def save_customer(c: Customer) -> Customer:
    now = datetime.utcnow().isoformat(timespec="seconds")
    if not c.created_at:
        c.created_at = now
    c.updated_at = now
    folder = c.folder()
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "config.json").write_text(json.dumps(c.to_json(), indent=2, ensure_ascii=False))
    return c


def delete_customer(slug: str) -> None:
    import shutil
    folder = CUSTOMERS_DIR / slug
    if folder.exists():
        shutil.rmtree(folder)


def save_logo(slug: str, file_bytes: bytes, extension: str) -> str:
    ext = (extension or "png").lower().lstrip(".")
    folder = CUSTOMERS_DIR / slug
    folder.mkdir(parents=True, exist_ok=True)
    rel = f"logo.{ext}"
    (folder / rel).write_bytes(file_bytes)
    return str((folder / rel).relative_to(CUSTOMERS_DIR.parent))
