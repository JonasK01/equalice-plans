"""Generate 4-point copy argumentation: CTR · CVR · Keywords · Reviews.

Every copy block (title, bullet, image headline, A+ headline, Q&A entry) gets
a small rationale derived from the parsed Excel data so the design team and
the brand can see WHY each line was written.
"""
from __future__ import annotations
import re
from dataclasses import dataclass
from typing import Iterable

from .excel_parser import ParsedBrief


@dataclass
class Argumentation:
    ctr: str
    cvr: str
    keywords: list[str]
    reviews: str


def _tokens(text: str) -> set[str]:
    """Loose token set for relevance matching."""
    return {t for t in re.findall(r"[a-zA-Z]{4,}", (text or "").lower())}


def _match_keywords(text: str, all_kws: Iterable[str], main_kws: Iterable[str], limit: int = 4) -> list[str]:
    text_tok = _tokens(text)
    if not text_tok:
        return []
    hits: list[tuple[int, str]] = []
    # Main keywords scored higher
    for kw in main_kws:
        score = len(_tokens(kw) & text_tok) * 3
        if score:
            hits.append((score, kw))
    for kw in all_kws:
        if kw in {k for _s, k in hits}:
            continue
        score = len(_tokens(kw) & text_tok)
        if score:
            hits.append((score, kw))
    hits.sort(key=lambda x: -x[0])
    out: list[str] = []
    seen: set[str] = set()
    for _s, kw in hits:
        if kw.lower() in seen:
            continue
        seen.add(kw.lower())
        out.append(kw)
        if len(out) >= limit:
            break
    return out


def _match_review_insight(text: str, brief: ParsedBrief) -> str:
    text_tok = _tokens(text)
    if not text_tok:
        return ""
    best = ""
    best_score = 0
    for r in brief.bad_reviews:
        score = len(_tokens(r) & text_tok)
        if score > best_score:
            best_score = score
            best = f"Defuses: {_trim(r)}"
    for r in brief.good_reviews:
        score = len(_tokens(r) & text_tok)
        if score > best_score + 1:  # prefer objection-defusers slightly
            best_score = score
            best = f"Echoes positive trigger: {_trim(r)}"
    if not best:
        return "No direct review match — line is positioning / brand voice."
    return best


def _trim(s: str, n: int = 180) -> str:
    s = (s or "").strip()
    return s if len(s) <= n else s[: n - 1] + "…"


# Role-based CTR/CVR rationale templates
_RATIONALES: dict[str, tuple[str, str]] = {
    "title": (
        "Title is the most-read text in search — front-loads main keyword + size + USP pattern for scannable click decision.",
        "Sets accurate expectation (no clickbait): pack size, product type, key benefit. Buyer arrives oriented.",
    ),
    "bullet": (
        "Bullet 1 is the first text under the image — has to confirm the click was correct in <2 seconds.",
        "Removes uncertainty: covers a buyer fear or filter directly (purity, use case, packaging, size).",
    ),
    "hero": (
        "Main image is the click trigger in the search grid — pure white, ~85% product, distinctive label glow.",
        "Sets premium expectation that the listing copy then earns. Reduces bounce.",
    ),
    "hook": (
        "Image 2 is the second-most-clicked tile — single visual + single line; reverses the buyer's biggest fear.",
        "Visualises the #1 trust trigger from reviews / brand DNA. First conversion lever.",
    ),
    "educate": (
        "Educational image stops the scroll for the curiosity-driven buyer.",
        "Owns the production / quality claim with a visual that no commodity competitor can mimic.",
    ),
    "desire": (
        "Lifestyle / desire image lets the buyer self-cast into the use case.",
        "Sells the experience, not the feature — the strongest in-grid conversion driver after price.",
    ),
    "trust": (
        "Stacks the filters (Non-GMO, hexane-free, cold-pressed) buyers scan for — high tile glance value.",
        "Defuses objections in one frame: removes review-driven friction visually.",
    ),
    "close": (
        "Brand-close image converts the buyer who's almost ready — identity over feature.",
        "Adds emotional commitment so the buyer chooses you over the cheaper competitor.",
    ),
    "a+_banner": (
        "A+ banner is the first thing seen below the bullets — sets brand mood + frames the rest of A+.",
        "Reinforces premium positioning to justify price vs. commodity competitors.",
    ),
    "a+_carousel": (
        "Carousel tiles are quick-scan reassurance — 5 reasons in 5 seconds.",
        "Defuses the top objections from the review pool in mobile-friendly tile format.",
    ),
    "a+_qa": (
        "Q&A captures objection-mode buyers (the ones who read further) — directly answers the question that would have driven a return or a 'too expensive' bounce.",
        "Each Q is a defused friction point from real review or category complaints.",
    ),
    "a+_comparison": (
        "Comparison table sits at the end of A+ — converts the comparison-shopper who'd otherwise leave to check competitors.",
        "Frames you as the rational choice on the buyer's checklist.",
    ),
    "overlay": (
        "On-image overlay text is the 'second headline' after the product — must be marketplace-language and large enough to read on the mobile thumbnail.",
        "Carries the single key claim that this tile is built around.",
    ),
}


def argument_for(
    role: str,
    text: str,
    brief: ParsedBrief,
) -> Argumentation:
    rationale = _RATIONALES.get(role, _RATIONALES["bullet"])
    return Argumentation(
        ctr=rationale[0],
        cvr=rationale[1],
        keywords=_match_keywords(text, brief.all_keywords, brief.main_keywords),
        reviews=_match_review_insight(text, brief),
    )
