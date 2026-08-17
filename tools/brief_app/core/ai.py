"""AI-driven copywriting via Claude Sonnet 4.6.

One BriefAI instance per (customer, parsed brief). The brand identity + product
context are bundled into a single cached system prompt — the first call writes
the cache, the remaining ~9 calls per brief read it at ~10% cost.

Pattern:
    ai = BriefAI(customer, brief)
    if not ai.enabled:
        # fall back to template strings
    else:
        title = ai.generate_title()
        bullets = ai.generate_bullets()
        ...

All outputs are JSON-validated against a per-method schema via structured outputs.
Errors are logged and methods return None — callers fall back to template strings.
"""
from __future__ import annotations
import json
import logging
import os
from dataclasses import dataclass, field
from typing import Any, Optional

try:
    import anthropic
    _SDK_AVAILABLE = True
except ImportError:
    _SDK_AVAILABLE = False

from .customers import Customer
from .excel_parser import ParsedBrief


log = logging.getLogger(__name__)

MODEL = "claude-sonnet-4-6"
ANTHROPIC_KEY_ENV = "ANTHROPIC_API_KEY"

# Default per-call max_tokens. Sonnet 4.6 supports up to 64K with streaming;
# we stay non-streaming and well under the timeout limit for each task.
DEFAULT_MAX_TOKENS = 4096

LANGUAGE_NAMES = {
    "en": "English",
    "de": "German (Deutsch)",
    "fr": "French (Français)",
    "es": "Spanish (Español)",
    "it": "Italian (Italiano)",
}


# ---------- AI output dataclasses ----------

# ---------- layout archetypes ----------
# Team feedback (test phase): "oftmals nur Headline und Subheadline — bitte kreativer planen",
# "mal mehr Icons, mal davor/danach, mal smart in der Mitte Text und drumherum die Benefits",
# "mehr Vielfalt — muss zum Produkt passen".
# A tile is not a headline on a photo. Every tile now has to declare WHICH COMPOSITION it uses,
# picked from this catalogue, and no two tiles in a plan may use the same one.
LAYOUT_ARCHETYPES: dict[str, str] = {
    "clean_hero": "Product alone, dominant, no graphic furniture. Amazon main image only.",
    "before_after": "Split frame or slider: the problem state vs the result state, divider down the middle.",
    "hub_and_spokes": "Product centred; 4-6 benefits radiate around it with hairline leader lines to the exact part they describe.",
    "icon_row": "One clear product/lifestyle shot with a row of 3-5 icon+label tiles beneath it.",
    "numbered_steps": "2-4 numbered panels showing a sequence (how to use, how it is made, how a round is played).",
    "annotated_callouts": "Single hero shot with 3-5 callout labels pinned to specific features by thin lines.",
    "grid_of_uses": "2x2 or 1x4 grid of distinct use cases / variants, identical composition in every cell.",
    "scale_reference": "Product against a familiar reference (hand, coin, everyday object) to settle size honestly.",
    "contents_flatlay": "Overhead flat-lay of everything in the box, each component hairline-labelled.",
    "comparison_columns": "2-3 labelled columns comparing options, formats or category alternatives (never named competitors).",
    "stat_block": "One or two big numbers as the hero graphic, product supporting, proof line beneath.",
    "macro_detail": "Extreme macro on the one texture/material/finish that proves the quality claim.",
    "lifestyle_candid": "Real people mid-moment, product present but not posed. Emotion carries the frame.",
    "split_duo": "Two related frames side by side (two flavours, two audiences, two moments) under one idea.",
    "cutaway": "Cross-section or exploded view revealing what is inside or how it is built.",
    "brand_close": "Brand-forward closing frame: logo, tagline, the product in its world.",
    # --- second wave, added on team feedback "generell mehr kreative layouts" ---
    "timeline": "A horizontal time axis (day 1 / week 2 / month 3, or morning to night) with the product's effect plotted along it.",
    "exploded_kit": "Every component floating apart in ordered space, thin leader lines naming each piece.",
    "size_ladder": "The same product in all its sizes or strengths, lined up smallest to largest, each labelled.",
    "problem_grid": "3-4 problem states across the top, the single product beneath, arrows tying each problem to it.",
    "hand_in_frame": "A hand performing the exact gesture the product needs, shot so the scale and the ease both read.",
    "texture_swatch": "Large swatches of the actual finish/texture the product produces, labelled like a paint chart.",
    "quote_card": "A real customer sentence set large as the hero element, product small, attribution beneath.",
    "cross_section_room": "The product placed in a cutaway of its real environment, other use points marked around it.",
    "ingredient_origin": "The raw material beside the finished product, connected by a single line: where it comes from, what it becomes.",
    "myth_vs_fact": "Two stacked bands: the common wrong belief struck through on top, the correction beneath.",
    "pack_shot_open": "The packaging opened or cut away so the contents, the amount and the protection are all visible at once.",
}


@dataclass
class AIImagePlanItem:
    name: str
    role: str
    background: str
    purpose: str
    visual: str
    overlay: str
    overlay_sub: str
    props: list[str]
    lighting: str
    why_it_works: str
    # Optional per-image conversion rationale. When set (hand-written senior copy),
    # they override the role-template CTR/CVR in the brief. Default "" = use template.
    ctr: str = ""
    cvr: str = ""
    # Composition archetype (key of LAYOUT_ARCHETYPES) + the graphic furniture the designer
    # must build. These exist so a tile is a DESIGNED LAYOUT, not a headline on a photo.
    layout: str = ""
    graphics: list[str] = field(default_factory=list)


@dataclass
class AIModule:
    name: str
    role: str
    headline: str
    body: str
    visual: str
    alt: str


@dataclass
class AIQA:
    q: str
    a: str


@dataclass
class AIArgumentation:
    ctr: str
    cvr: str
    keywords: list[str]
    reviews: str


@dataclass
class AIComplianceFlag:
    text: str
    issue: str
    severity: str  # "low" | "medium" | "high"
    suggestion: str


# ---------- system prompt builder ----------

def _list_or_dash(items: list[str], cap: int = 12) -> str:
    if not items:
        return "  (none provided)"
    out = []
    for i, it in enumerate(items[:cap]):
        out.append(f"  - {it}")
    if len(items) > cap:
        out.append(f"  - ... and {len(items) - cap} more")
    return "\n".join(out)


def _trim(s: str, n: int = 400) -> str:
    s = (s or "").strip()
    return s if len(s) <= n else s[: n - 1] + "…"


def _safe_brand_memory(customer: Customer) -> str:
    """Full brand history (study + every product's verified notes). Never breaks generation."""
    try:
        from .knowledge import build_brand_memory
        return build_brand_memory(getattr(customer, "slug", "") or "")
    except Exception:
        return ""


def build_system_prompt(customer: Customer, brief: ParsedBrief, feedback: str = "") -> str:
    overlay_lang = LANGUAGE_NAMES.get(customer.overlay_language, "English")
    brand_memory = _safe_brand_memory(customer)
    fb = (feedback or "").strip()
    fb_block = (
        "\n\n# REVISION — REVIEWER FEEDBACK YOU MUST APPLY (HIGHEST PRIORITY, overrides defaults)\n"
        "This is a new version of an existing plan. Concretely fix every point below:\n"
        f"{fb}\n"
        if fb else ""
    )
    return f"""You are a senior Amazon listing copywriter writing for the brand {customer.name}.{fb_block}

# BRAND DNA
- Brand: {customer.name}
- Tagline: {customer.tagline or '(none)'}
- Voice: {customer.voice or '(neutral, premium)'}
- Personality: {', '.join(customer.personality) or '(unspecified)'}
- Photography rules: {_trim(customer.photo_rules, 600)}
- No-gos (NEVER include in any visual or copy): {_trim(customer.no_gos, 600)}
- Creative freedom: {customer.creative_freedom}/5
- Website: {getattr(customer, 'website_url', '') or '(not supplied)'}

# ABOUT US — THE BRAND'S OWN STORY (in their words)
Use this for the brand banner, the "From the Brand" close and any heritage/credential claim.
If a founding story, a credential or a reason-for-existing is in here, USE IT — it is the one
thing a competitor cannot copy. NEVER invent a brand story that is not supported below.
{_trim(getattr(customer, 'about_us', '') or '', 1200) or '(No About Us on file — do NOT invent a founding story, credential or heritage claim. Stay with what the product facts support.)'}

# BRAND MEMORY — everything we have created and verified for this brand before
Use this to stay consistent with past work, reuse proven angles, respect the established
compliance wording (e.g. approved NPN/claim phrasing), and never repeat past mistakes.
Do NOT copy it verbatim — let it inform a fresh, product-specific plan.
{brand_memory or '(No prior brand history on file yet — this is an early plan for the brand.)'}

# PRODUCT BEING BRIEFED
- Product: {_trim(brief.product_name, 300)}
- ASIN: {brief.asin or '(missing)'}
- Marketplace: {customer.marketplace}
- Overlay language (for on-image text): {overlay_lang}
- Listing URL: {brief.listing_url or '(none)'}

# USPS (verbatim from client onboarding)
{_list_or_dash(brief.usps, cap=12)}

# EMOTIONAL BENEFITS
{_list_or_dash(brief.emotional_benefits, cap=10)}

# TARGET GROUP
{_trim(brief.target_group, 600) or '(not specified)'}

# TARGET PROBLEMS (defuse these in copy)
{_trim(brief.target_problems, 600) or '(not specified)'}

# POSITIVE REVIEW THEMES (echo these triggers)
{_list_or_dash(brief.good_reviews, cap=10)}

# NEGATIVE REVIEW THEMES (defuse these objections directly)
{_list_or_dash(brief.bad_reviews, cap=10)}

# MAIN KEYWORDS (must appear in title + first bullets when natural)
{_list_or_dash(brief.main_keywords, cap=8)}

# ADDITIONAL KEYWORDS (use in backend + sublines where natural)
{_list_or_dash(brief.all_keywords[:40], cap=40)}

# AMAZON COMPLIANCE — HARD CONSTRAINTS
- NEVER: medical/curative/regrowth claims ("cures", "heals", "regrows", "prevents", "FDA-approved", "clinically proven")
- NEVER: superlatives ("best", "#1", "ultimate", "miracle", "guaranteed")
- NEVER: competitor brand names
- NEVER: discount/price language ("$", "sale", "% off", "free shipping")
- Main image (Image 1): pure white background, ≥85% product, NO overlay text, NO graphics — Amazon policy
- Other images: overlay text MUST be in {overlay_lang} for marketplace {customer.marketplace}
- Body copy (visual direction, why-it-works, A+ body): always English
- Patch-test guidance required for topical/personal-care products
- Certifications ("Organic", "Non-GMO") only if proven

# YOUR JOB
You will receive specific generation requests. Always return JSON matching the schema you are given. Make every word:
1. Specific to THIS product (not generic templates)
2. Tied to a real USP, KW, or review insight
3. Brand-voice consistent
4. Compliance-safe
5. Conversion-optimized — every line should defuse a friction or amplify a trigger
"""


# ---------- BriefAI class ----------

class BriefAI:
    def __init__(self, customer: Customer, brief: ParsedBrief, model: str = MODEL, feedback: str = ""):
        self.customer = customer
        self.brief = brief
        self.model = model
        self.feedback = (feedback or "").strip()
        self.lang = customer.overlay_language or "en"
        self.api_key = os.environ.get(ANTHROPIC_KEY_ENV, "").strip()
        self.client: Optional["anthropic.Anthropic"] = None
        self.last_usage: dict[str, int] = {"input": 0, "cached": 0, "output": 0}
        self.errors: list[str] = []
        import threading
        self._usage_lock = threading.Lock()

        if _SDK_AVAILABLE and self.api_key:
            try:
                self.client = anthropic.Anthropic(api_key=self.api_key)
            except Exception as exc:
                log.warning("AI client init failed: %s", exc)
                self.client = None

        self._system_prompt = build_system_prompt(customer, brief, self.feedback)

    @property
    def enabled(self) -> bool:
        return self.client is not None

    @property
    def status_message(self) -> str:
        if not _SDK_AVAILABLE:
            return "anthropic SDK not installed"
        if not self.api_key:
            return f"{ANTHROPIC_KEY_ENV} not set"
        if not self.client:
            return "client init failed"
        return f"ready ({self.model})"

    # ----- low-level call helpers -----

    def _system_blocks(self) -> list[dict]:
        """System prompt as a list with cache_control on the last block.
        Caches the brand + product context so the remaining ~9 calls per
        brief hit cache at ~10% cost."""
        return [
            {
                "type": "text",
                "text": self._system_prompt,
                "cache_control": {"type": "ephemeral"},
            }
        ]

    def _structured_call(self, task: str, schema: dict, max_tokens: int = DEFAULT_MAX_TOKENS) -> Optional[dict]:
        """Make one structured-output call. Returns parsed JSON or None on error."""
        if not self.client:
            return None
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=max_tokens,
                system=self._system_blocks(),
                messages=[{"role": "user", "content": task}],
                output_config={"format": {"type": "json_schema", "schema": schema}},
            )
            # Tally usage (thread-safe — the pipeline runs generations in parallel)
            u = response.usage
            with self._usage_lock:
                self.last_usage["input"] += u.input_tokens
                self.last_usage["cached"] += u.cache_read_input_tokens or 0
                self.last_usage["output"] += u.output_tokens
            # Structured outputs guarantee first content block is text containing JSON
            text = next((b.text for b in response.content if b.type == "text"), "")
            return json.loads(text)
        except anthropic.APIStatusError as exc:
            msg = f"AI call failed ({task[:40]}): {exc.status_code} {exc.message}"
            log.error(msg)
            self.errors.append(msg)
            return None
        except Exception as exc:
            msg = f"AI call failed ({task[:40]}): {exc}"
            log.error(msg)
            self.errors.append(msg)
            return None

    # ----- generation methods -----

    def generate_title(self) -> Optional[str]:
        schema = {
            "type": "object",
            "properties": {
                "title": {"type": "string", "description": "Amazon listing title, MAX 200 characters, separated by ' · ' or ' — '. Front-load main keyword, include pack size, include 1-2 differentiating USPs. Must read naturally."},
                "char_count": {"type": "integer"},
            },
            "required": ["title", "char_count"],
            "additionalProperties": False,
        }
        task = (
            "Write the Amazon listing title for this product. "
            "Max 200 characters. Front-load the strongest main keyword. "
            "Include pack size/quantity. Include 1-2 differentiating USPs. "
            "Use ' · ' or ' — ' as separators. Must read like a human wrote it, not a string concatenation. "
            "Return JSON."
        )
        result = self._structured_call(task, schema, max_tokens=512)
        return result["title"] if result else None

    def generate_bullets(self) -> Optional[list[str]]:
        schema = {
            "type": "object",
            "properties": {
                "bullets": {
                    "type": "array",
                    "minItems": 1,
                    "items": {
                        "type": "object",
                        "properties": {
                            "head": {"type": "string", "description": "ALL CAPS hook, max 50 chars, no superlatives"},
                            "body": {"type": "string", "description": "Conversion-focused sentence(s), 180-260 chars, defuses a friction OR amplifies a trigger"},
                        },
                        "required": ["head", "body"],
                        "additionalProperties": False,
                    },
                },
            },
            "required": ["bullets"],
            "additionalProperties": False,
        }
        task = (
            "Write 5 Amazon bullet points for this product. Each MUST:\n"
            "- Start with an ALL-CAPS hook (max 50 chars), then ' — ', then 180-260 chars of body copy\n"
            "- Defuse a specific friction from the negative reviews OR amplify a specific trigger from the positive reviews\n"
            "- Use a different USP than the other bullets\n"
            "- Include keywords naturally (don't stuff)\n"
            "- Stay in brand voice\n"
            "- Be compliance-safe (no medical claims, no superlatives, no competitor names)\n"
            "Bullet 1 = strongest single USP. Bullet 5 = brand trust + heritage. Return JSON."
        )
        result = self._structured_call(task, schema, max_tokens=2048)
        if not result:
            return None
        return [f"<b>{b['head']}</b> — {b['body']}" for b in result["bullets"]]

    def generate_image_plan(self) -> Optional[list[AIImagePlanItem]]:
        schema = {
            "type": "object",
            "properties": {
                "images": {
                    "type": "array",
                    "minItems": 1,
                    "items": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string", "description": "e.g. 'Image 2 — Cold-press hook'"},
                            "role": {
                                "type": "string",
                                "enum": ["hero", "hook", "educate", "desire", "trust", "close"],
                                "description": "Conversion role of this tile",
                            },
                            "background": {"type": "string", "description": "Specific background — for Image 1 MUST be 'Pure white #FFFFFF'"},
                            "purpose": {"type": "string", "description": "What this tile does for the buyer in 1 sentence"},
                            "visual": {"type": "string", "description": "Specific shot direction — composition, framing, angle. For Image 1: pure white BG, ≥85% product, no overlay text"},
                            "overlay": {"type": "string", "description": f"On-image headline in {LANGUAGE_NAMES.get(self.lang, 'English')}. EMPTY STRING for Image 1 (Amazon policy bans overlay on main image)."},
                            "overlay_sub": {"type": "string", "description": f"On-image subline in {LANGUAGE_NAMES.get(self.lang, 'English')}. EMPTY STRING for Image 1."},
                            "props": {"type": "array", "items": {"type": "string"}, "description": "Specific props on set (e.g. 'wooden brow brush, glass dropper, linen towel')"},
                            "lighting": {"type": "string", "description": "Specific lighting note (e.g. 'Warm side-light from camera-left, 45° rim, soft fill right')"},
                            "why_it_works": {"type": "string", "description": "1-2 sentence rationale tied to a specific USP, keyword, or review insight"},
                            "layout": {
                                "type": "string",
                                "enum": list(LAYOUT_ARCHETYPES.keys()),
                                "description": "The COMPOSITION this tile uses. Image 1 must be 'clean_hero'. No two tiles may share the same layout.",
                            },
                            "graphics": {
                                "type": "array",
                                "items": {"type": "string"},
                                "description": (
                                    "The graphic furniture the designer must actually build for this layout — icons, "
                                    "badges, callout lines, numbers, dividers, arrows, panel labels. Be concrete and "
                                    "name each element and where it sits (e.g. '5 line icons across the base: leaf, "
                                    "clock, shield, drop, USA outline', 'thin arrow from the split divider pointing "
                                    "right', 'big 112 set in brand navy, cards fanned behind it'). EMPTY ARRAY for "
                                    "Image 1 only — Amazon bans graphics on the main image."
                                ),
                            },
                        },
                        "required": ["name", "role", "background", "purpose", "visual", "overlay", "overlay_sub", "props", "lighting", "why_it_works", "layout", "graphics"],
                        "additionalProperties": False,
                    },
                },
            },
            "required": ["images"],
            "additionalProperties": False,
        }
        task = (
            "Design the 7-image Amazon listing plan for this product. The 7 tiles must follow these roles in order:\n"
            "1. hero — Amazon main image: pure white BG, ≥85% product fill, NO overlay text, NO graphics (policy)\n"
            "2. hook — visualises the #1 buyer fear reversed (from negative reviews)\n"
            "3. educate — production / quality story (the claim the cheap competitor can't make)\n"
            "4. desire — lifestyle / in-use moment the buyer self-casts into\n"
            "5. trust — badges + objection-defusing (sourced from the actual review concerns)\n"
            "6. desire — second lifestyle or how-to-use ritual (different from #4)\n"
            "7. close — brand identity tile that turns hesitating buyers into loyal ones\n\n"
            "Each tile must be SPECIFIC to THIS product — not generic templates. Visual direction must read like a photographer's brief: "
            "composition, angle, framing, distance, props list, lighting note. "
            f"Overlay text (where allowed) MUST be in {LANGUAGE_NAMES.get(self.lang, 'English')} for marketplace {self.customer.marketplace}. "
            "Body fields (visual, why_it_works) stay English. "
            "For Image 1, overlay/overlay_sub MUST be empty strings (Amazon main-image policy bans overlay text). "
            "In Image 1's 'visual' field, propose 2-3 distinct MAIN-IMAGE OPTIONS to A/B test — label them "
            "Option A / Option B / Option C — each a different composition/props/angle that could win the click. "
            "Every overlay (Images 2-7) MUST be PUNCHY (≤30 chars AND ≤5 words, one idea) AND marketing-strong: "
            "lead with the dream outcome, use power words and specifics, never generic (e.g. 'GENTLE, NO CRAMPING.'). "
            "overlay_sub ≤90 chars.\n\n"

            "# DESIGN THE LAYOUT, NOT JUST THE HEADLINE (hard requirement)\n"
            "A tile is a COMPOSITION, not a caption on a photo. Reviewers rejected plans where every tile was "
            "just headline + subheadline over an image. For every tile you must choose a 'layout' archetype and "
            "specify the 'graphics' the designer builds. Available archetypes:\n"
            + "\n".join(f"  - {k}: {v}" for k, v in LAYOUT_ARCHETYPES.items()) + "\n\n"
            "RULES:\n"
            "- Image 1 = 'clean_hero' with an EMPTY graphics array (Amazon policy).\n"
            "- Images 2-7 must each use a DIFFERENT archetype. Never repeat one inside a plan.\n"
            "- Across the 7 tiles include at least THREE of these four: a before/after or comparison, an "
            "icon-driven tile, a hub_and_spokes or annotated_callouts tile, and a numbered_steps or "
            "contents_flatlay tile. Photography-only tiles may never be more than two of the seven.\n"
            "- PUSH PAST THE OBVIOUS. At least ONE tile must use an archetype from the second half of "
            "the list above (timeline, exploded_kit, size_ladder, problem_grid, hand_in_frame, "
            "texture_swatch, quote_card, cross_section_room, ingredient_origin, myth_vs_fact, "
            "pack_shot_open). A plan built only from clean_hero / icon_row / lifestyle_candid / "
            "numbered_steps is the safe, boring plan the review team already rejected. Pick the "
            "unexpected archetype that this product can genuinely carry, and say in why_it_works why "
            "that composition beats the obvious one.\n"
            "- Pick archetypes that FIT THIS PRODUCT. A cross-section suits hardware, not a card game; a "
            "scale_reference suits anything reviewers call 'smaller than expected'; contents_flatlay suits "
            "multi-part products; before_after suits anything that fixes a visible problem. Choosing an "
            "archetype the product cannot support is worse than a plain shot.\n"
            "- 'graphics' must name real elements and their position. 'Some icons' is a failure; "
            "'row of 4 line icons under the product: leaf, clock, shield, USA outline' is correct.\n\n"

            "# MOBILE LEGIBILITY (over 70% of Amazon traffic is mobile — these are hard specs)\n"
            "- THE TOP TWO THIRDS RULE: the bottom 15-20% of a listing image is de-emphasised or partly "
            "covered by Amazon's own mobile UI. Put the headline, the key callout and any badge in the "
            "TOP TWO THIRDS. Never place the single most important callout bottom-left or bottom-right.\n"
            "- THE THUMBNAIL TEST: state in the visual how the tile survives at 100x100 px. A shopper must "
            "identify the product category in under one second at that size. If the idea only reads at full "
            "size, it is the wrong idea for that slot.\n"
            "- Minimum on-image body text 30 px in a 2000x2000 file (headlines much larger). Sans-serif for "
            "overlays — it stays legible where a display serif breaks up. Text-to-background contrast at "
            "least 4.5:1; on a busy photo, put the text on a solid or semi-transparent panel rather than "
            "shrinking it.\n"
            "- ONE IDEA PER TILE. Four features, three specs and a comparison in one graphic means none of "
            "them gets read.\n\n"

            "# OVERLAYS DOUBLE AS KEYWORD REINFORCEMENT\n"
            "Where it can be done without bending the language, echo the buyer's ACTUAL search wording from "
            "the keyword list above in the overlay or subline. The shopper arrived on a search term; seeing "
            "their own words on the image confirms they are in the right place. Never keyword-stuff, and "
            "never let a keyword make a line clumsy — a natural line beats a keyword-shaped one.\n\n"

            "# WRITING STYLE FOR ON-IMAGE TEXT\n"
            "- NO em-dashes or en-dashes (— –) in overlay or overlay_sub. Reviewers flagged dash overuse "
            "explicitly. Use a full stop, a comma, or restructure the line. A colon is fine, sparingly.\n"
            "- A CONCRETE NUMBER BEATS AN ADJECTIVE. Counts, sizes, minutes, years, temperatures and "
            "quantities measurably out-perform vague quality words in headlines. Use a real figure from the "
            "product data whenever one exists; never invent one.\n"
            "- Vary the sentence SHAPE across the seven overlays. Do not ship seven lines built the same way "
            "(e.g. all 'ADJECTIVE NOUN. ADJECTIVE NOUN.'). Mix a command, a number-led claim, a question a "
            "buyer actually asks, a plain statement of the result.\n"
            "- Punchy is not choppy: each line must still read smoothly out loud.\n"
            "Return JSON."
        )
        result = self._structured_call(task, schema, max_tokens=6000)
        if not result:
            return None
        return [AIImagePlanItem(**img) for img in result["images"]]

    def generate_aplus_modules(self) -> Optional[list[AIModule]]:
        schema = {
            "type": "object",
            "properties": {
                "modules": {
                    "type": "array",
                    "minItems": 1,
                    "items": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string", "description": "e.g. 'Module 1 — Brand banner'"},
                            "role": {
                                "type": "string",
                                "enum": ["a+_banner", "a+_carousel", "a+_qa", "a+_comparison"],
                            },
                            "headline": {"type": "string", "description": f"Module headline in {LANGUAGE_NAMES.get(self.lang, 'English')}"},
                            "body": {"type": "string", "description": "Module body / supporting copy (English, brand-voice, 2-4 sentences)"},
                            "visual": {"type": "string", "description": "Visual direction for designer"},
                            "alt": {"type": "string", "description": "Accessibility alt text"},
                        },
                        "required": ["name", "role", "headline", "body", "visual", "alt"],
                        "additionalProperties": False,
                    },
                },
            },
            "required": ["modules"],
            "additionalProperties": False,
        }
        task = (
            "Design the 7 A+ Premium modules for this product. Fixed Amazon sequence:\n"
            "1. a+_banner — Brand hero banner (tagline + lifestyle scene)\n"
            "2. a+_carousel — 5-tile 'Brand Difference' (the 5 strongest USPs as scan-friendly tiles)\n"
            "3. a+_banner — Production / story banner (heritage, process, traceability)\n"
            "4. a+_banner — Use cases triptych (LEFT/CENTER/RIGHT real-world scenes)\n"
            "5. a+_carousel — Product family carousel (this SKU + 4 cross-sell tiles)\n"
            "6. a+_qa — 4-6 Q&A pairs (each defuses a specific review-driven friction)\n"
            "7. a+_comparison — Comparison vs commodity / vs cheap alternative\n\n"
            "Each module must be SPECIFIC to this product. Headlines in "
            f"{LANGUAGE_NAMES.get(self.lang, 'English')}. Body in English.\n\n"

            "# THE 'visual' FIELD IS A LAYOUT SPEC, NOT A MOOD NOTE\n"
            "Reviewers rejected A+ banners that were just a headline over a photo. For every module, the "
            "'visual' field must state the actual composition: how the frame is divided, what sits left / "
            "centre / right, what graphic furniture the designer builds (icons, numbers, dividers, callout "
            "lines, badges, panel labels), and how it reflows for mobile. Name the elements and their "
            "positions. Vary the construction across the seven modules — never ship three banners built the "
            "same way. Always give BOTH sizes: desktop 1464x600, mobile 600x450, and say what stays inside "
            "the mobile safe area.\n\n"

            "# WRITING STYLE\n"
            "- NO em-dashes or en-dashes (— –) in any headline. Reviewers flagged dash overuse explicitly.\n"
            "- Vary headline construction across the seven modules.\n"
            "- Body copy: 2-4 sentences, no filler, every sentence carries a fact, a benefit or a reason to "
            "trust. Cut anything a competitor could paste onto their own product unchanged.\n"
            "- The strongest A+ pages run roughly 70% image, 30% text. If a module needs a long paragraph to "
            "work, the visual is not carrying its share — redesign the visual instead of writing more.\n"
            "Return JSON."
        )
        result = self._structured_call(task, schema, max_tokens=6000)
        if not result:
            return None
        return [AIModule(**m) for m in result["modules"]]

    def generate_qa(self) -> Optional[list[AIQA]]:
        schema = {
            "type": "object",
            "properties": {
                "qa": {
                    "type": "array",
                    "minItems": 1,
                    "items": {
                        "type": "object",
                        "properties": {
                            "q": {"type": "string", "description": "The exact question a hesitating buyer would ask"},
                            "a": {"type": "string", "description": "Brand-voice answer that defuses the objection. Honest. Compliance-safe."},
                        },
                        "required": ["q", "a"],
                        "additionalProperties": False,
                    },
                },
            },
            "required": ["qa"],
            "additionalProperties": False,
        }
        task = (
            "Write 5-8 Q&A pairs for this product. Each Q MUST be a real hesitation a buyer would have, drawn from:\n"
            "- The negative reviews (defuse those objections)\n"
            "- Common category questions (e.g. how to use, what's the difference, is it safe for X)\n"
            "- Compliance edge cases (patch test, allergies, regulatory expectations)\n"
            "Each A: brand voice, honest, never over-claims. If existing RUFUS Q&A is in the product context, rewrite it in brand voice — "
            "don't copy verbatim. Return JSON."
        )
        result = self._structured_call(task, schema, max_tokens=3000)
        if not result:
            return None
        return [AIQA(**qa) for qa in result["qa"]]

    def elevate_copy(self, images, modules):
        """Second-pass ELITE copywriting refinement (quality over speed).

        Rewrites the highest-visibility marketing surface — on-image overlays + sublines and
        A+ module headlines — to the top bar: dream-outcome-first, voice-of-customer language,
        power words + specifics, punchy and on-brand, informed by the full Brand Memory in the
        cached system prompt. Stays compliant (the build still runs the compliance + copy-length
        scans afterwards as the safety net). Returns (images, modules); unchanged on any failure.
        """
        if not self.client or not (images or modules):
            return images, modules

        img_in = [
            {"i": i, "role": im.role, "overlay": im.overlay or "", "overlay_sub": im.overlay_sub or ""}
            for i, im in enumerate(images or [])
            if (im.role or "") != "hero"          # never add overlay text to the Amazon main image
        ]
        mod_in = [
            {"i": i, "role": m.role, "headline": m.headline or ""}
            for i, m in enumerate(modules or [])
        ]
        if not img_in and not mod_in:
            return images, modules

        schema = {
            "type": "object",
            "properties": {
                "images": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "i": {"type": "integer"},
                            "overlay": {"type": "string", "description": "Refined on-image headline. ≤30 chars AND ≤5 words."},
                            "overlay_sub": {"type": "string", "description": "Refined subline. ≤90 chars."},
                        },
                        "required": ["i", "overlay", "overlay_sub"],
                        "additionalProperties": False,
                    },
                },
                "modules": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "i": {"type": "integer"},
                            "headline": {"type": "string", "description": "Refined A+ headline. ≤38 chars."},
                        },
                        "required": ["i", "headline"],
                        "additionalProperties": False,
                    },
                },
            },
            "required": ["images", "modules"],
            "additionalProperties": False,
        }

        import json as _json
        lang = LANGUAGE_NAMES.get(self.lang, "English")
        task = (
            "You are an ELITE Amazon conversion copywriter and brand voice specialist. Below is a "
            "drafted image + A+ plan. Rewrite ONLY the marketing copy to the highest possible bar — "
            "this is the quality pass, take the care it deserves:\n"
            "- Lead with the buyer's dream outcome; use real voice-of-customer language.\n"
            "- Power words + concrete specifics, not vague fluff. Punchy and smooth, varied rhythm.\n"
            "- Stay 100% in this brand's voice and honour every no-go and the Brand Memory context.\n"
            "- Keep it fully Amazon-compliant (no medical/curative claims, no superlatives like "
            "'best/#1', no competitor names, no prices/URLs).\n"
            f"- Overlays + sublines MUST be in {lang}. Overlay ≤30 chars AND ≤5 words; subline ≤90 chars; "
            "A+ headline ≤38 chars.\n"

            "\nNON-NEGOTIABLES — the review team rejected the previous output on exactly these points:\n"
            "1. NO em-dashes or en-dashes (— –) anywhere in an overlay, subline or A+ headline. They were "
            "used as a crutch to bolt two half-thoughts together. Use a full stop, a comma, or rewrite the "
            "line so it does not need one.\n"
            "2. NO two lines in the set may share the same construction. If you have written three lines as "
            "'NOUN PHRASE. NOUN PHRASE.', rewrite two of them. Across the set, deliberately mix: a command, "
            "a number-led claim, a real buyer question, a flat statement of the result, a short line with a "
            "twist in the second half.\n"
            "3. NO stock marketing filler: 'premium quality', 'perfect for', 'take it anywhere', 'elevate "
            "your', 'game changer', 'say goodbye to'. If a competitor could paste the line onto their own "
            "product unchanged, it is not finished.\n"
            "4. Every line must be sayable out loud without stumbling. Read each one back before you keep it.\n"

            "\n# THE BAR: THIS COPY EXISTS TO CONVERT, NOT TO DESCRIBE\n"
            "Judge every line by one question: does it move somebody closer to buying? A line that is "
            "merely accurate is a wasted line. Specifically:\n"
            "- OWN A JOB PER TILE. Across the seven overlays, the set must cover: the dream outcome, "
            "the objection that loses the sale, the proof, and the reason to buy THIS one. If two "
            "overlays do the same job, rewrite one.\n"
            "- LEAD WITH THE AFTER. Not what it is, not what it does — what the buyer's life looks "
            "like once it worked. 'Marmor wie am ersten Tag' beats 'Reinigt Naturstein'.\n"
            "- USE THEIR NUMBERS. A concrete figure from the product data (count, size, minutes, "
            "years, temperature) out-converts any adjective. Never invent one; if the data has none, "
            "use a sensory specific instead.\n"
            "- TURN THE TOP COMPLAINT INTO A PROMISE. Take the loudest negative review theme and write "
            "the overlay that answers it head-on. That single line usually carries the whole plan.\n"
            "- SOUND LIKE THE BUYER, NOT THE SELLER. Reuse the exact words from the review data. If "
            "customers say 'wie neu', say 'wie neu' — do not upgrade it to 'revitalisiert'.\n"
            "- EARN THE SECOND GLANCE. At thumbnail size the shopper reads three words. Front-load "
            "the ones that matter and let the subline carry the rest.\n"
            "- Return the SAME items by their 'i' index (do not add, drop, or reorder). Improve the text; "
            "if a line is already excellent, you may keep it.\n\n"
            "IMAGES (overlays to elevate):\n" + _json.dumps(img_in, ensure_ascii=False) + "\n\n"
            "A+ MODULE HEADLINES to elevate:\n" + _json.dumps(mod_in, ensure_ascii=False) + "\n\n"
            "Return JSON matching the schema."
        )
        result = self._structured_call(task, schema, max_tokens=3000)
        if not result:
            return images, modules

        for r in result.get("images", []) or []:
            i = r.get("i")
            if isinstance(i, int) and 0 <= i < len(images) and (images[i].role or "") != "hero":
                ov = (r.get("overlay") or "").strip()
                sub = (r.get("overlay_sub") or "").strip()
                if ov:
                    images[i].overlay = ov
                if sub:
                    images[i].overlay_sub = sub
        for r in result.get("modules", []) or []:
            i = r.get("i")
            if isinstance(i, int) and 0 <= i < len(modules):
                hl = (r.get("headline") or "").strip()
                if hl:
                    modules[i].headline = hl
        return images, modules

    def generate_argumentation(self, role: str, text: str) -> Optional[AIArgumentation]:
        """Generate CTR/CVR/Keywords/Reviews rationale for one specific copy element."""
        schema = {
            "type": "object",
            "properties": {
                "ctr": {"type": "string", "description": "Why this copy drives CLICKS specifically — 1-2 sentences referencing the visual hook, search-grid legibility, pattern interrupt, or main keyword presence"},
                "cvr": {"type": "string", "description": "Why this copy CONVERTS — 1-2 sentences referencing a specific objection defused or trigger amplified"},
                "keywords": {"type": "array", "items": {"type": "string"}, "description": "Up to 5 keywords from the product's KW universe that this line covers, in priority order"},
                "reviews": {"type": "string", "description": "Quote or paraphrase the EXACT review verbatim that this line addresses. If no direct match, say so."},
            },
            "required": ["ctr", "cvr", "keywords", "reviews"],
            "additionalProperties": False,
        }
        task = (
            f"For this copy element (role: {role}):\n"
            f"COPY: {text}\n\n"
            "Generate a 4-point argumentation:\n"
            "- CTR: specifically why THIS line gets the click\n"
            "- CVR: specifically what objection it defuses or trigger it amplifies\n"
            "- Keywords: which product KWs this line covers\n"
            "- Reviews: which review insight this line responds to (quote/paraphrase)\n"
            "Be specific to this line — not generic theory. Return JSON."
        )
        result = self._structured_call(task, schema, max_tokens=800)
        if not result:
            return None
        return AIArgumentation(**result)

    def compliance_scan(self, text: str) -> Optional[list[AIComplianceFlag]]:
        """Scan a copy block for compliance issues; return flagged spans + safe replacements."""
        schema = {
            "type": "object",
            "properties": {
                "flags": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "text": {"type": "string", "description": "The exact problematic phrase"},
                            "issue": {"type": "string", "description": "Why it's a problem (Amazon policy / FTC / brand voice)"},
                            "severity": {"type": "string", "enum": ["low", "medium", "high"]},
                            "suggestion": {"type": "string", "description": "Specific replacement phrasing that keeps the intent"},
                        },
                        "required": ["text", "issue", "severity", "suggestion"],
                        "additionalProperties": False,
                    },
                },
            },
            "required": ["flags"],
            "additionalProperties": False,
        }
        task = (
            f"Scan this copy block for compliance issues:\n\n{text}\n\n"
            "Flag any of:\n"
            "- Medical/curative claims (cures, regrows, heals, prevents)\n"
            "- Superlatives (best, #1, ultimate, miracle, guaranteed)\n"
            "- Unproven certifications (organic/non-GMO if not certified)\n"
            "- Competitor brand names\n"
            "- Discount/price language ($, sale, free shipping)\n"
            "- Drug-Facts-style language for cosmetics\n"
            "For each flag: provide a safe replacement that preserves the intent. "
            "If no issues, return an empty flags array. Return JSON."
        )
        result = self._structured_call(task, schema, max_tokens=1500)
        if not result:
            return None
        return [AIComplianceFlag(**f) for f in result["flags"]]

    def generate_backend_keywords(self) -> Optional[str]:
        """Stem-deduplicated, byte-budget-aware backend search terms ≤ 249 bytes."""
        schema = {
            "type": "object",
            "properties": {
                "backend": {"type": "string", "description": "Space-separated keyword string. Lowercase. No commas, no brand names, no superlatives. Stem-deduplicated. ≤ 249 bytes."},
                "byte_count": {"type": "integer"},
            },
            "required": ["backend", "byte_count"],
            "additionalProperties": False,
        }
        task = (
            "Build the Amazon backend search-terms field for this product. Rules:\n"
            "- Lowercase, space-separated, NO commas\n"
            "- Stem-deduplicate (don't include both 'oil' and 'oils' — just the root)\n"
            "- No words already in the title (those get full credit there)\n"
            "- No competitor brands, no superlatives, no '$/sale/free'\n"
            "- Cover related/misspelled/long-tail variants the title can't fit\n"
            "- Hard limit: 249 bytes (Amazon's actual cap is 250; leave 1 for safety)\n"
            "Return JSON with the string and its byte count."
        )
        result = self._structured_call(task, schema, max_tokens=1024)
        return result["backend"] if result else None


# ---------- module-level helper ----------

def has_api_key() -> bool:
    return bool(os.environ.get(ANTHROPIC_KEY_ENV, "").strip())


def sdk_available() -> bool:
    return _SDK_AVAILABLE
