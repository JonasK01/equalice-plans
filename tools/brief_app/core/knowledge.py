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


# ---------- the learning loop: team review corrections feed future plans ----------

def get_review_learnings(slug: str) -> str:
    f = TEAM_KNOWLEDGE_DIR / (slug or "") / "review_learnings.md"
    return _read(f, 6000) if f.exists() else ""


def add_review_learning(slug: str, text: str, author: str = "") -> None:
    """Persist a team correction so EVERY future plan for this brand applies it."""
    text = " ".join((text or "").split()).strip()
    if not text:
        return
    f = team_knowledge_dir(slug) / "review_learnings.md"
    head = "# Review learnings (team corrections — apply to every future plan)\n"
    prior = f.read_text(encoding="utf-8") if f.exists() else head
    who = f"  — {author}" if author else ""
    f.write_text(prior.rstrip() + f"\n- {text}{who}\n", encoding="utf-8")


# ---------- the brand's visual system: every plan must look like the last one ----------
#
# A brand is not just a voice and a palette, it is a recognisable way of building a tile —
# the same icon treatment, the same panel, the same place the badge sits. Brand memory
# already carried the words; it did not carry the design, so plan 6 could arrive looking
# nothing like plan 1 even though both were "on brand" by the config. This records the
# composition decisions each finished plan actually made and feeds them back, so the brand
# accumulates a house style instead of restarting every time.

def get_visual_system(slug: str) -> str:
    f = TEAM_KNOWLEDGE_DIR / (slug or "") / "visual_system.md"
    return _read(f, 4000) if f.exists() else ""


def record_plan_visuals(slug: str, product: str, images) -> None:
    """Append the composition decisions a finished plan made, for future plans to match.

    Deliberately terse: layouts plus the graphic devices actually specified. A long dump
    would crowd out the rest of brand memory and stop being read."""
    slug = (slug or "").strip()
    if not slug or not images:
        return
    layouts, devices = [], []
    for im in images:
        lay = (getattr(im, "layout", "") or "").strip()
        if lay:
            layouts.append(lay)
        for g in (getattr(im, "graphics", None) or [])[:2]:
            g = " ".join(str(g).split())
            if g:
                devices.append(g[:90])
    if not layouts:
        return
    line = f"- **{product or 'plan'}** — layouts: {', '.join(layouts)}"
    if devices:
        line += "\n  devices: " + " · ".join(devices[:6])
    f = team_knowledge_dir(slug) / "visual_system.md"
    head = ("# Visual system — how this brand's tiles are actually built\n"
            "Each entry is a plan already delivered for this brand.\n")
    prior = f.read_text(encoding="utf-8") if f.exists() else head
    if line.split("\n")[0] in prior:          # same product rebuilt: don't duplicate
        return
    f.write_text(prior.rstrip() + "\n" + line + "\n", encoding="utf-8")


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

    visual = get_visual_system(slug)
    if visual:
        parts.append(
            "## Visual system — HOW THIS BRAND'S TILES ARE BUILT. This is a house style, not a "
            "history: a shopper who has seen one of this brand's listings must recognise the next "
            "one. Reuse the same icon treatment, the same panel and badge placement, the same way "
            "text sits on the image. Vary the ARCHETYPE per tile as instructed, never the styling. "
            "Only depart from it if the product genuinely cannot carry it, and say so in "
            "why_it_works.\n" + visual)

    learnings = get_review_learnings(slug)
    if learnings:
        parts.append("## Review learnings — corrections the team made in past reviews. "
                     "APPLY THESE and never repeat these mistakes.\n" + learnings)

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
