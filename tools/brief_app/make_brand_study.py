"""Render a human-readable brand_study.md from a customer's config.json.

config.json is the machine source of truth (the brief_app reads it).
brand_study.md is the readable "branding" the agent reads FIRST before any
image-plan job for that brand. Regenerate it whenever config.json changes so
the two never drift.

Usage:
    python tools/brief_app/make_brand_study.py <slug>      # one brand
    python tools/brief_app/make_brand_study.py --all       # every brand
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

CUSTOMERS = Path(__file__).resolve().parent / "customers"


def _section(title: str, body: str) -> str:
    body = (body or "").strip()
    if not body:
        return ""
    return f"## {title}\n\n{body}\n\n"


def _bullets(title: str, items) -> str:
    items = [str(i).strip() for i in (items or []) if str(i).strip()]
    if not items:
        return ""
    lines = "\n".join(f"- {i}" for i in items)
    return f"## {title}\n\n{lines}\n\n"


def render(cfg: dict) -> str:
    name = cfg.get("name", cfg.get("slug", "Brand"))
    md = f"# {name} — Brand Study\n\n"
    md += (
        "> Auto-generated from `config.json` by `make_brand_study.py`. "
        "Edit `config.json`, then regenerate — do not hand-edit this file.\n"
        "> **Read this before starting any image-plan or A+ job for this brand.**\n\n"
    )

    facts = [
        ("Slug", cfg.get("slug")),
        ("Marketplace", cfg.get("marketplace")),
        ("Overlay language", cfg.get("overlay_language")),
        ("Tagline", cfg.get("tagline")),
        ("Creative freedom (1-5)", cfg.get("creative_freedom")),
    ]
    md += "## At a glance\n\n"
    md += "| Field | Value |\n|---|---|\n"
    for k, v in facts:
        if v not in (None, "", []):
            md += f"| {k} | {v} |\n"
    md += "\n"

    colors = [
        ("Primary", cfg.get("primary_color")),
        ("Accent", cfg.get("accent_color")),
        ("Text", cfg.get("text_color")),
        ("Background", cfg.get("background_color")),
        ("Mood background", cfg.get("mood_background_color")),
    ]
    color_rows = "".join(f"| {k} | `{v}` |\n" for k, v in colors if v)
    if color_rows:
        md += "## Colors\n\n| Role | HEX |\n|---|---|\n" + color_rows + "\n"

    md += _bullets("Fonts", cfg.get("fonts"))
    md += _bullets("Personality", cfg.get("personality"))
    md += _section("Voice", cfg.get("voice"))
    md += _section("Photo rules", cfg.get("photo_rules"))
    md += _section("No-gos (hard don'ts)", cfg.get("no_gos"))
    md += _bullets("Moodboard search terms", cfg.get("moodboard_search_terms"))
    md += _section("Notes (product context, keywords, compliance)", cfg.get("notes"))
    return md.rstrip() + "\n"


def write_one(slug: str) -> Path:
    cfg_path = CUSTOMERS / slug / "config.json"
    cfg = json.loads(cfg_path.read_text())
    out = CUSTOMERS / slug / "brand_study.md"
    out.write_text(render(cfg))
    return out


def main(argv: list[str]) -> None:
    if not argv:
        print(__doc__)
        return
    if argv[0] == "--all":
        for cfg in sorted(CUSTOMERS.glob("*/config.json")):
            out = write_one(cfg.parent.name)
            print(f"wrote {out.relative_to(CUSTOMERS.parent)}")
        return
    out = write_one(argv[0])
    print(f"wrote {out.relative_to(CUSTOMERS.parent)}")


if __name__ == "__main__":
    main(sys.argv[1:])
