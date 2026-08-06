#!/usr/bin/env python3
"""
CVR x CTR Booster — score a listing against the 20-point rubric and emit:
  - A scorecard JSON
  - A one-page Markdown punch list ranked by uplift potential

Usage:
    python3 tools/cvr_ctr_score.py <input_scores.json> [--out-json out.json] [--out-md out.md]

Input JSON format (see workflows/cvr_ctr_booster.md for the full rubric):
{
  "asin": "B0XXXXXXX",
  "marketplace": "com",
  "scores": {
    "main_image_clarity_at_200": {"score": 3, "note": "label hard to read at thumbnail"},
    "main_image_color_contrast": {"score": 4, "note": "..."},
    ...
  }
}

Lines whose score is missing are treated as 3 (median) with a note "[not scored]".
"""

import sys
import json
import argparse
from pathlib import Path

# Lever ID -> (label, group, weight, default_diagnostic)
RUBRIC = [
    # CTR — Search-Result Click-Through
    ("main_image_clarity_at_200",          "Main image clarity at 200 px",        "CTR", "High",   "Shrink to 200x200, look 2 sec — is the product unmistakable?"),
    ("main_image_color_contrast",          "Main image color contrast",           "CTR", "High",   "Does the tile pop against neighbors in the SERP?"),
    ("title_primary_kw_first_80",          "Title — primary keyword in first 80", "CTR", "High",   "Open on phone. Is the root keyword shown before '...'?"),
    ("title_variant_clarity",              "Title — variant clarity",             "CTR", "Medium", "Are size, count, and key feature unambiguous in the title?"),
    ("rating_visible_badge",               "Star rating >= 4.4",                  "CTR", "High",   "Below 4.3 hurts CTR; above 4.5 helps."),
    ("review_count_vs_median",             "Review count >= category median",     "CTR", "High",   "Compare to top-3 competitors."),
    ("coupon_promo_badge",                 "Coupon / Promo badge present",        "CTR", "Medium", "Missing badges leave CTR on the table in commodity categories."),
    # CVR — Page-to-Cart
    ("hero_image_2sec_confidence",         "Hero image — confidence in 2 sec",    "CVR", "High",   "Show image #1 for 2 sec; can a stranger describe what they get?"),
    ("image2_strongest_buying_reason",     "Image #2 — strongest single benefit", "CVR", "High",   "Buyer should think 'I want this because...' after image 2."),
    ("bullet1_emotional_plus_proof",       "Bullet #1 — emotion + proof",         "CVR", "High",   "Read aloud. Does it tell, or does it sell?"),
    ("bullets_5_distinct_benefits",        "Bullets — 5 non-overlapping",         "CVR", "Medium", "Bullets that repeat each other waste real estate."),
    ("aplus_module1_repositions_brand",    "A+ Module 1 — repositions brand",     "CVR", "Medium", "Should be a richer pitch, not a repeat of the bullets."),
    ("aplus_module6_qa_defuses",           "A+ Module 6 Q&A — defuses objections","CVR", "High",   "Cross-check vs. negative reviews — are top fears answered?"),
    ("aplus_module7_comparison_chart",     "A+ Module 7 — comparison chart",      "CVR", "High",   "Without one, sticker shock kills CVR."),
    ("variant_family_clarity",             "Variant family clarity",              "CVR", "Medium", "Wrong default variant is a silent CVR killer."),
    ("brand_story_strip",                  "Brand Story strip beneath bullets",   "CVR", "Low",    "Adds trust + discovery; many sellers skip it."),
    ("first_5_reviews_quality",            "First 5 reviews — helpful / mixed",   "CVR", "Medium", "All-5-star block reads as fake; some 4s and recent dates help."),
    ("subscribe_and_save",                 "Subscribe & Save offered",            "CVR", "Medium", "Materially boosts CVR + LTV in Grocery / Beauty."),
    ("qa_section_min_3_answered",          "Q&A section — at least 3 answered",   "CVR", "Low",    "Unanswered questions = friction."),
    ("mobile_above_fold_complete",         "Mobile above-the-fold complete",      "CVR", "High",   "First mobile scroll: image + headline + price + variant + S&S."),
]

WEIGHT_VALUE = {"High": 3, "Medium": 2, "Low": 1}


def score_listing(input_data):
    asin = input_data.get("asin", "UNKNOWN")
    marketplace = input_data.get("marketplace", "com")
    scores = input_data.get("scores", {}) or {}

    rows = []
    total_uplift = 0
    total_max_uplift = 0
    health_sum = 0

    for lever_id, label, group, weight, diagnostic in RUBRIC:
        entry = scores.get(lever_id, {}) or {}
        raw = entry.get("score")
        note = entry.get("note", "")
        if raw is None:
            score = 3
            note = (note + " [not scored — defaulted to 3]").strip()
        else:
            score = max(1, min(5, int(raw)))
        weight_val = WEIGHT_VALUE[weight]
        uplift = (5 - score) * weight_val
        max_uplift = 4 * weight_val
        rows.append({
            "lever_id": lever_id,
            "label": label,
            "group": group,
            "weight": weight,
            "score": score,
            "note": note,
            "uplift_points": uplift,
            "max_uplift_points": max_uplift,
            "diagnostic": diagnostic,
        })
        total_uplift += uplift
        total_max_uplift += max_uplift
        health_sum += score

    health_score = round(health_sum / len(RUBRIC), 2)
    return {
        "asin": asin,
        "marketplace": marketplace,
        "health_score_avg": health_score,
        "total_uplift_points": total_uplift,
        "max_uplift_points": total_max_uplift,
        "uplift_percent": round(100 * total_uplift / total_max_uplift, 1) if total_max_uplift else 0,
        "rows": rows,
    }


def to_markdown(result):
    lines = []
    lines.append(f"# Listing Uplift Punch List — {result['asin']} ({result['marketplace']})")
    lines.append("")
    lines.append(f"- **Health Score (avg 1-5):** {result['health_score_avg']}  *(higher = healthier)*")
    lines.append(f"- **Uplift potential:** {result['total_uplift_points']} of {result['max_uplift_points']} points  ({result['uplift_percent']}%)")
    lines.append("")

    # Top 5 priority fixes
    sorted_rows = sorted(result["rows"], key=lambda r: r["uplift_points"], reverse=True)
    top5 = [r for r in sorted_rows if r["uplift_points"] > 0][:5]
    lines.append("## Priority fixes — top 5 by uplift")
    lines.append("")
    lines.append("| # | Lever | Group | Weight | Current Score | Uplift | Note |")
    lines.append("|---|---|---|---|---|---|---|")
    for i, r in enumerate(top5, 1):
        lines.append(f"| {i} | {r['label']} | {r['group']} | {r['weight']} | {r['score']}/5 | +{r['uplift_points']} | {r['note'] or '—'} |")
    lines.append("")

    # Full table
    lines.append("## Full scorecard")
    lines.append("")
    lines.append("| Lever | Group | Weight | Score | Uplift | Diagnostic |")
    lines.append("|---|---|---|---|---|---|")
    for r in result["rows"]:
        lines.append(f"| {r['label']} | {r['group']} | {r['weight']} | {r['score']}/5 | +{r['uplift_points']} | {r['diagnostic']} |")
    lines.append("")
    lines.append("---")
    lines.append("Scoring rubric: 1 = critical gap · 2 = below average · 3 = acceptable · 4 = strong · 5 = best-in-class")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Score an Amazon listing against the CTR x CVR Booster rubric.")
    parser.add_argument("input", help="Path to input scores JSON (see workflow doc).")
    parser.add_argument("--out-json", default=None, help="Where to write the scorecard JSON. Default: alongside input.")
    parser.add_argument("--out-md", default=None, help="Where to write the punch-list markdown. Default: alongside input.")
    args = parser.parse_args()

    in_path = Path(args.input)
    data = json.loads(in_path.read_text())
    result = score_listing(data)

    out_json = Path(args.out_json) if args.out_json else in_path.with_name(in_path.stem + "_scorecard.json")
    out_md = Path(args.out_md) if args.out_md else in_path.with_name(in_path.stem + "_punchlist.md")

    out_json.write_text(json.dumps(result, indent=2))
    out_md.write_text(to_markdown(result))

    print(f"Health score (avg 1-5): {result['health_score_avg']}")
    print(f"Uplift potential: {result['total_uplift_points']} / {result['max_uplift_points']} ({result['uplift_percent']}%)")
    print(f"Scorecard JSON: {out_json}")
    print(f"Punch list MD : {out_md}")


if __name__ == "__main__":
    main()
