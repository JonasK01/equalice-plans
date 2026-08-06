"""Brand Memory — the 'mind' layer.

config.json = brand IDENTITY (voice, colours, no-gos). Brand Memory = brand HISTORY:
the readable brand study + every product's verified SOURCE_NOTES (NPN numbers, approved
claim wording, ingredients, formats, directions) + the catalogue of products done so far.

It is injected into every generation's system prompt so each new plan is informed by ALL
prior work for that brand: consistent voice, reused proven angles, established compliance
wording, and no repeated mistakes. This is what makes the tool get smarter as it does more.

Read from the shipped customers dir (image copy), size-capped so it stays cache-friendly.
"""
from __future__ import annotations
import re
from pathlib import Path

from .config import SEED_CUSTOMERS_DIR, DATA_ROOT

# Team-contributed knowledge lives on the writable volume so it survives redeploys AND
# feeds straight back into every future generation (the start of the learning loop):
# extra product info + reference images the team uploads in the app.
TEAM_KNOWLEDGE_DIR = DATA_ROOT / "knowledge"
_IMG_EXT = {".png", ".jpg", ".jpeg", ".webp", ".gif"}

_TOTAL_CAP = 26000          # chars of memory injected (~6-7k tokens, cached in the system block)
_STUDY_CAP = 5000
_NOTES_CAP = 1600
_TEAM_CAP = 5000


def _read(p: Path, limit: int) -> str:
    try:
        t = p.read_text(encoding="utf-8", errors="ignore").strip()
    except Exception:
        return ""
    return t if len(t) <= limit else t[:limit].rstrip() + " …"


def list_brand_products(slug: str) -> list[str]:
    """Product folder names for a brand (its catalogue), scaffolding folders excluded."""
    d = SEED_CUSTOMERS_DIR / slug / "products"
    if not d.exists():
        return []
    return sorted(p.name for p in d.iterdir() if p.is_dir() and not p.name.startswith("_"))


# ---------- team-contributed knowledge (writable /data volume) ----------

def team_knowledge_dir(slug: str) -> Path:
    d = TEAM_KNOWLEDGE_DIR / (slug or "")
    d.mkdir(parents=True, exist_ok=True)
    return d


def get_team_info(slug: str) -> str:
    f = TEAM_KNOWLEDGE_DIR / (slug or "") / "extra_info.md"
    return _read(f, 100000) if f.exists() else ""


def save_team_info(slug: str, text: str) -> None:
    (team_knowledge_dir(slug) / "extra_info.md").write_text((text or "").strip(), encoding="utf-8")


def list_team_images(slug: str) -> list[str]:
    d = TEAM_KNOWLEDGE_DIR / (slug or "")
    if not d.exists():
        return []
    return sorted(p.name for p in d.iterdir() if p.suffix.lower() in _IMG_EXT)


def save_team_image(slug: str, filename: str, data: bytes) -> str:
    safe = re.sub(r"[^A-Za-z0-9._-]+", "_", filename or "image.png")
    (team_knowledge_dir(slug) / safe).write_bytes(data)
    return safe


def _team_knowledge(slug: str) -> str:
    parts = []
    info = get_team_info(slug)
    if info:
        parts.append(info if len(info) <= _TEAM_CAP else info[:_TEAM_CAP].rstrip() + " …")
    imgs = list_team_images(slug)
    if imgs:
        parts.append("Reference images the team uploaded for this brand/product: " + ", ".join(imgs))
    return "\n\n".join(parts).strip()


def build_brand_memory(slug: str) -> str:
    """Aggregate everything known for a brand into one markdown pack (size-capped):
    the shipped brand study + product source notes, PLUS team-added knowledge from /data."""
    slug = (slug or "").strip()
    if not slug:
        return ""
    base = SEED_CUSTOMERS_DIR / slug

    parts: list[str] = []
    study = base / "brand_study.md"
    if study.exists():
        parts.append("## Brand study\n" + _read(study, _STUDY_CAP))

    prods = list_brand_products(slug)
    if prods:
        parts.append(f"## Catalogue — products created for this brand so far ({len(prods)})\n"
                     + ", ".join(prods))
        for name in prods:
            notes = base / "products" / name / "SOURCE_NOTES.md"
            if notes.exists():
                parts.append(f"### {name} — verified source notes\n" + _read(notes, _NOTES_CAP))

    team = _team_knowledge(slug)
    if team:
        parts.append("## Team-added knowledge (latest info + notes the team uploaded — treat as current)\n" + team)

    if not parts:
        return ""
    pack = "\n\n".join(parts).strip()
    if len(pack) > _TOTAL_CAP:
        pack = pack[:_TOTAL_CAP].rstrip() + "\n\n… (brand memory truncated for length)"
    return pack


def brand_memory_summary(slug: str) -> dict:
    """Lightweight overview for the app UI (what the tool knows about this brand)."""
    prods = list_brand_products(slug)
    base = SEED_CUSTOMERS_DIR / slug
    notes = 0
    for name in prods:
        if (base / "products" / name / "SOURCE_NOTES.md").exists():
            notes += 1
    return {
        "products": prods,
        "product_count": len(prods),
        "source_notes_count": notes,
        "has_brand_study": (base / "brand_study.md").exists(),
        "memory_chars": len(build_brand_memory(slug)),
    }
