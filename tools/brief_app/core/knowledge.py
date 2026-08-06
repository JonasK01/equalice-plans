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
from pathlib import Path

from .config import SEED_CUSTOMERS_DIR

_TOTAL_CAP = 22000          # chars of memory injected (~5-6k tokens, cached in the system block)
_STUDY_CAP = 5000
_NOTES_CAP = 1600


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


def build_brand_memory(slug: str) -> str:
    """Aggregate everything known for a brand into one markdown pack (size-capped)."""
    slug = (slug or "").strip()
    if not slug:
        return ""
    base = SEED_CUSTOMERS_DIR / slug
    if not base.exists():
        return ""

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
