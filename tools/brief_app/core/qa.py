"""Deterministic final-QA helpers for every brief build.

Compliance: runs the project's amazon_compliance_checker over all customer-facing
copy and maps the result to AIComplianceFlag objects the PDF already knows how to
render. This runs automatically in BriefBuilder.build() for hand-written briefs
(ai=None) — no run.py has to remember to do it.
"""
from __future__ import annotations
import importlib.util
from pathlib import Path

from .ai import AIComplianceFlag

# tools/amazon_compliance_checker.py lives at the project root /tools.
_CHECKER = Path(__file__).resolve().parents[3] / "tools" / "amazon_compliance_checker.py"


def _load_checker():
    spec = importlib.util.spec_from_file_location("amazon_compliance_checker", _CHECKER)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def compliance_scan(texts: list[str]) -> list[AIComplianceFlag]:
    """Scan all copy lines, return flags (violations = high, warnings = low)."""
    try:
        checker = _load_checker()
    except Exception:
        return []  # checker unavailable — don't block the build
    blob = "\n".join(t for t in texts if t)
    if not blob.strip():
        return []
    res = checker.check_text(blob)
    flags: list[AIComplianceFlag] = []
    for v in res.get("violations", []):
        flags.append(AIComplianceFlag(
            text=", ".join(str(m) for m in v.get("matches", [])) or v.get("rule", ""),
            issue=v.get("description", ""),
            severity="high",
            suggestion=v.get("note", ""),
        ))
    for w in res.get("warnings", []):
        flags.append(AIComplianceFlag(
            text=", ".join(str(m) for m in w.get("matches", [])) or w.get("rule", ""),
            issue=w.get("description", ""),
            severity="low",
            suggestion=w.get("note", ""),
        ))
    return flags


def has_blocking(flags: list[AIComplianceFlag]) -> bool:
    return any(f.severity == "high" for f in (flags or []))


# ---- copy-length lint: keep on-image text punchy, headlines short ----
import re as _re

# Punchy standard for image-plan copy. On-image overlays must be glanceable.
MAX_OVERLAY_CHARS = 30
MAX_OVERLAY_WORDS = 5
MAX_OVERLAY_SUB_CHARS = 90
MAX_MODULE_HEADLINE_CHARS = 38
MAX_BULLET_HEAD_CHARS = 45


def _plain(s: object) -> str:
    return _re.sub(r"<[^>]+>", "", str(s or "").replace("&amp;", "&")).strip()


def lint_copy(title: str, bullets, images, modules) -> list[str]:
    """Return human-readable warnings for copy that is too long to read at a glance.
    On-image overlays are the strictest (they are headlines on the creative)."""
    warns: list[str] = []
    for i, im in enumerate(images or [], 1):
        ov = _plain(getattr(im, "overlay", ""))
        if ov and not ov.startswith("("):  # "(...)" = hero A/B placeholder, exempt
            if len(ov) > MAX_OVERLAY_CHARS or len(ov.split()) > MAX_OVERLAY_WORDS:
                warns.append(f'Image {i} overlay {len(ov)}ch/{len(ov.split())}w (max {MAX_OVERLAY_CHARS}ch/{MAX_OVERLAY_WORDS}w): "{ov}"')
        sub = _plain(getattr(im, "overlay_sub", ""))
        if len(sub) > MAX_OVERLAY_SUB_CHARS:
            warns.append(f'Image {i} overlay_sub {len(sub)}ch (max {MAX_OVERLAY_SUB_CHARS})')
    for i, mo in enumerate(modules or [], 1):
        h = _plain(getattr(mo, "headline", ""))
        if len(h) > MAX_MODULE_HEADLINE_CHARS:
            warns.append(f'Module {i} headline {len(h)}ch (max {MAX_MODULE_HEADLINE_CHARS}): "{h}"')
    for i, b in enumerate(bullets or [], 1):
        m = _re.search(r"<b>(.*?)</b>", b or "")
        head = _plain(m.group(1)) if m else ""
        if len(head) > MAX_BULLET_HEAD_CHARS:
            warns.append(f'Bullet {i} head {len(head)}ch (max {MAX_BULLET_HEAD_CHARS})')
    t = _plain(title)
    if len(t) > 200:
        warns.append(f"TITLE {len(t)}ch (max 200)")
    return warns
