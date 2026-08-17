"""Deterministic final-QA helpers for every brief build.

Compliance: runs the project's amazon_compliance_checker over all customer-facing
copy and maps the result to AIComplianceFlag objects the PDF already knows how to
render. This runs automatically in BriefBuilder.build() for hand-written briefs
(ai=None) — no run.py has to remember to do it.
"""
from __future__ import annotations
import importlib.util
from pathlib import Path

from .ai import (
    AIComplianceFlag, QA_PAIRS, QA_Q_MAX, QA_A_MAX,
    MODULE_BODY_MAX as MAX_MODULE_BODY_CHARS,
    MODULE_VISUAL_MAX as MAX_MODULE_VISUAL_CHARS,
)

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


# Review-team standard (test phase): dashes were being used as a crutch to weld two
# half-thoughts into one headline. On-image text and A+ headlines must not contain them.
_DASHES = _re.compile(r"[—–]")

# NOTE: "all seven overlays are built the same way" is a real review complaint, but it is NOT
# lintable — at ≤5 words per overlay any fingerprint collapses and the check fires on every
# plan. A linter that cries wolf gets ignored, and it sits next to the dash rule that must be
# trusted. Construction variety is enforced in the generator prompt instead (ai.py).


def lint_copy(title: str, bullets, images, modules, qa=None) -> list[str]:
    """Return human-readable warnings for copy that is too long to read at a glance.
    On-image overlays are the strictest (they are headlines on the creative)."""
    warns: list[str] = []
    # A+ Q&A: five pairs, tightly capped. This block is scanned on a phone, so an
    # over-long answer is not a style nit — it is the reason the module gets skipped.
    qa = list(qa or [])
    if qa and len(qa) != QA_PAIRS:
        warns.append(f"A+ Q&A has {len(qa)} pairs (must be exactly {QA_PAIRS})")
    for i, pair in enumerate(qa, 1):
        q = _plain(getattr(pair, "q", "") or (pair.get("q") if isinstance(pair, dict) else ""))
        a = _plain(getattr(pair, "a", "") or (pair.get("a") if isinstance(pair, dict) else ""))
        if len(q) > QA_Q_MAX:
            warns.append(f'Q&A {i} question {len(q)}ch (max {QA_Q_MAX}): "{q}"')
        if len(a) > QA_A_MAX:
            warns.append(f'Q&A {i} answer {len(a)}ch (max {QA_A_MAX}): "{a}"')
    for i, im in enumerate(images or [], 1):
        ov = _plain(getattr(im, "overlay", ""))
        if ov and not ov.startswith("("):  # "(...)" = hero A/B placeholder, exempt
            if len(ov) > MAX_OVERLAY_CHARS or len(ov.split()) > MAX_OVERLAY_WORDS:
                warns.append(f'Image {i} overlay {len(ov)}ch/{len(ov.split())}w (max {MAX_OVERLAY_CHARS}ch/{MAX_OVERLAY_WORDS}w): "{ov}"')
            if _DASHES.search(ov):
                warns.append(f'Image {i} overlay uses a dash — rewrite without it: "{ov}"')
        sub = _plain(getattr(im, "overlay_sub", ""))
        if len(sub) > MAX_OVERLAY_SUB_CHARS:
            warns.append(f'Image {i} overlay_sub {len(sub)}ch (max {MAX_OVERLAY_SUB_CHARS})')
        if _DASHES.search(sub):
            warns.append(f'Image {i} overlay_sub uses a dash — rewrite without it')
    for i, mo in enumerate(modules or [], 1):
        h = _plain(getattr(mo, "headline", ""))
        if len(h) > MAX_MODULE_HEADLINE_CHARS:
            warns.append(f'Module {i} headline {len(h)}ch (max {MAX_MODULE_HEADLINE_CHARS}): "{h}"')
        if _DASHES.search(h):
            warns.append(f'Module {i} headline uses a dash — rewrite without it: "{h}"')
        # Body length applies to BANNERS only — they are the modules that turn into
        # paragraphs, and they are what the review team was reading when it said "way too
        # much copy". Two roles are structurally different and are excluded:
        #   - a+_carousel, whose body is a list of tile labels. Five scannable tiles are not
        #     a wall of text, and measuring them as one paragraph fails every carousel ever
        #     written.
        #   - a+_qa, whose body IS the question-and-answer block, already governed by the
        #     Q&A rules above. Measuring it here would report every plan twice for one text.
        # The bridge sentence is stripped as well: a house rule appends it after the copy is
        # written, so counting it would fail module 6 for a line its author never wrote.
        role = str(getattr(mo, "role", "") or "")
        body = _plain(_re.sub(r"<i>.*?</i>", "", str(getattr(mo, "body", "") or ""), flags=_re.S))
        if role == "a+_banner" and len(body) > MAX_MODULE_BODY_CHARS:
            warns.append(f'Module {i} body {len(body)}ch (max {MAX_MODULE_BODY_CHARS}) — '
                         f'A+ copy is support text, not a paragraph')
        vis = _plain(getattr(mo, "visual", ""))
        if len(vis) > MAX_MODULE_VISUAL_CHARS:
            warns.append(f'Module {i} layout spec {len(vis)}ch (max {MAX_MODULE_VISUAL_CHARS})')
    for i, b in enumerate(bullets or [], 1):
        m = _re.search(r"<b>(.*?)</b>", b or "")
        head = _plain(m.group(1)) if m else ""
        if len(head) > MAX_BULLET_HEAD_CHARS:
            warns.append(f'Bullet {i} head {len(head)}ch (max {MAX_BULLET_HEAD_CHARS})')
    t = _plain(title)
    if len(t) > 200:
        warns.append(f"TITLE {len(t)}ch (max 200)")
    return warns
