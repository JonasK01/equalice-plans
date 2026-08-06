#!/usr/bin/env python3
"""
Amazon listing copy compliance checker.
Usage: python3 tools/amazon_compliance_checker.py <input_file>
       echo "your copy text" | python3 tools/amazon_compliance_checker.py --stdin

Checks copy against Amazon's prohibited words, restricted claims,
and formatting rules for listing images and A+ content.

Supports: All marketplaces (DE, US, UK rules combined)

Outputs JSON with violations, warnings, and pass/fail per rule.
"""

import sys
import json
import re
import os


# ═══════════════════════════════════════════════════════════════════
# RULE DEFINITIONS
# ═══════════════════════════════════════════════════════════════════

PROHIBITED_WORDS = {
    "superlatives_without_proof": {
        "description": "Superlative claims require substantiation",
        "severity": "violation",
        "patterns": [
            r"\b(best|bester|beste|bestes)\b",
            r"\b(#\s*1|nr\.\s*1|number\s*one|nummer\s*eins)\b",
            r"\b(top\s*rated|top\s*seller|top-rated|top-seller)\b",
            r"\b(best[\s-]?sell(er|ing))\b",
            r"\b(leading|market\s*leader|marktführer)\b",
            r"\b(most\s+popular|beliebteste[rs]?)\b",
            r"\b(world'?s?\s*(best|finest|greatest|leading))\b",
            r"\b(unmatched|unrivaled|unübertroffen)\b",
            r"\b(superior\s+to\s+all)\b",
        ],
        "note": "Allowed only with verifiable third-party substantiation (e.g., award, certified test)"
    },

    "guarantee_language": {
        "description": "Guarantee/warranty claims not backed by Amazon policy",
        "severity": "warning",
        "patterns": [
            r"\b(money[\s-]?back\s*guarantee|geld[\s-]?zurück[\s-]?garantie)\b",
            r"\b(satisfaction\s*guarant|zufriedenheitsgarantie)\b",
            r"\b(100\s*%\s*(guarantee|garantie|satisfaction|zufriedenheit))\b",
            r"\b(risk[\s-]?free|risikofrei)\b",
            r"\b(lifetime\s*(guarantee|warranty)|lebenslange\s*garantie)\b",
        ],
        "note": "Guarantees must be backed by actual policy. Amazon return policy is separate."
    },

    "health_medical_claims": {
        "description": "Medical/health claims not allowed without certification",
        "severity": "violation",
        "patterns": [
            r"\b(cure[sd]?|heilt|heilung|cures)\b",
            r"\b(treat(s|ment)?|behandlung|behandelt)\b",
            r"\b(prevent(?:s|ion|ing)?|verhindert|vorbeugung)\b",
            r"\b(diagnos(e|is|tic)|diagnose)\b",
            r"\b(clinically\s*proven|klinisch\s*(erwiesen|getestet|bewiesen))\b",
            r"\b(FDA[\s-]?approved|medizinisch\s*zugelassen)\b",
            r"\b(doctor[\s-]?recommended|ärztlich\s*empfohlen)\b",
            r"\b(miracle|wunder(mittel)?)\b",
            r"\b(anti[\s-]?aging|anti[\s-]?falten)\b",
        ],
        "note": "Health claims require regulatory approval. Use 'supports', 'helps with', 'designed for' instead."
    },

    "urgency_pressure": {
        "description": "False urgency or pressure tactics",
        "severity": "violation",
        "patterns": [
            r"\b(buy\s*now|jetzt\s*kaufen|act\s*now|sofort\s*handeln)\b",
            r"\b(limited\s*(time|stock|offer|edition)|begrenzt(e[rs]?)?\s*(angebot|zeit|stückzahl))\b",
            r"\b(hurry|beeilen\s*sie\s*sich|don'?t\s*miss\s*out|nicht\s*verpassen)\b",
            r"\b(while\s*supplies\s*last|solange\s*der\s*vorrat\s*reicht)\b",
            r"\b(order\s*(now|today)|bestellen\s*sie\s*(jetzt|heute))\b",
            r"\b(last\s*chance|letzte\s*chance)\b",
            r"\b(selling\s*fast|schnell\s*ausverkauft)\b",
        ],
        "note": "Amazon prohibits false urgency. Time-limited offers must be actual promotions managed through Seller Central."
    },

    "competitor_references": {
        "description": "Direct competitor brand mentions",
        "severity": "violation",
        "patterns": [
            r"\b(better\s*than|besser\s*als)\s+[A-Z][a-zA-Z]+\b",
            r"\b(unlike|im\s*gegensatz\s*zu)\s+[A-Z][a-zA-Z]+\b",
            r"\b(replaces?|ersetzt)\s+[A-Z][a-zA-Z]+\b",
            r"\b(compared?\s*to|verglichen\s*mit)\s+[A-Z][a-zA-Z]+\b",
        ],
        "note": "Never reference competitor brands by name. Use generic terms like 'conventional products' or 'other brands'."
    },

    "pricing_references": {
        "description": "Price references not allowed in listing content",
        "severity": "violation",
        "patterns": [
            r"\b(cheap(est|er)?|billig(ste[rs]?)?|günstig(ste[rs]?)?)\b",
            r"\b(affordable|erschwinglich|preiswert)\b",
            r"(\$|€|£)\s*\d+",
            r"\b\d+\s*(dollar|euro|pound|EUR|USD|GBP)\b",
            r"\b(save\s*\d+\s*%|sparen\s*sie\s*\d+\s*%)\b",
            r"\b(discount|rabatt|sale\s*price|angebotspreis)\b",
            r"\b(free\s*shipping|kostenloser\s*versand)\b",
        ],
        "note": "Pricing and shipping info is managed by Amazon. Do not reference prices in images or A+ content."
    },

    "subjective_unverifiable": {
        "description": "Subjective claims that can't be verified",
        "severity": "warning",
        "patterns": [
            r"\b(amazing|erstaunlich|incredible|unglaublich)\b",
            r"\b(perfect|perfekt(e[rs]?)?)\b",
            r"\b(revolutionary|revolutionär)\b",
            r"\b(game[\s-]?chang(er|ing)|bahnbrechend)\b",
            r"\b(unique|einzigartig)\b",
            r"\b(innovative|innovativ)\b",
        ],
        "note": "These words are overused and lack specificity. Replace with concrete, measurable benefits."
    },

    "environmental_claims": {
        "description": "Environmental claims require certification",
        "severity": "warning",
        "patterns": [
            r"\b(eco[\s-]?friendly|umweltfreundlich)\b",
            r"\b(sustainable|nachhaltig)\b",
            r"\b(biodegradable|biologisch\s*abbaubar)\b",
            r"\b(carbon[\s-]?neutral|klimaneutral|CO2[\s-]?neutral)\b",
            r"\b(organic|bio|ökologisch)\b",
            r"\b(green\s*product|grünes\s*produkt)\b",
            r"\b(recyclable|recycelbar|recyclingfähig)\b",
        ],
        "note": "Environmental claims need certification (e.g., FSC, GOTS, EU Ecolabel). Add the specific certification."
    },

    "contact_external_links": {
        "description": "External contact info or links not allowed",
        "severity": "violation",
        "patterns": [
            r"\b(www\.|http|\.com|\.de|\.co\.uk)\b",
            r"\b(call\s*us|rufen\s*sie\s*uns\s*an|contact\s*us|kontaktieren\s*sie)\b",
            r"\b(email|e-mail)\s*:?\s*\S+@\S+",
            r"\b(phone|telefon|tel\.?)\s*:?\s*[\d\s\-\+]+\b",
            r"\b(visit\s*our\s*(website|shop|store)|besuchen\s*sie\s*unsere)\b",
            r"\b(follow\s*us|folgen\s*sie\s*uns)\b",
            r"\b(facebook|instagram|twitter|tiktok|youtube|pinterest)\b",
        ],
        "note": "Amazon prohibits external links, contact info, and social media references in listing content."
    },

    "condition_claims": {
        "description": "Condition claims must be accurate",
        "severity": "warning",
        "patterns": [
            r"\b(brand\s*new|brandneu|nagelneu)\b",
            r"\b(original|authentic|authentisch)\b",
            r"\b(genuine|echt(e[rs]?)?)\b",
        ],
        "note": "Condition is set at listing level. Avoid redundant condition claims in copy."
    },

    "shipping_fulfillment": {
        "description": "Shipping/fulfillment promises not allowed in copy",
        "severity": "violation",
        "patterns": [
            r"\b(fast\s*(shipping|delivery)|schnelle(r)?\s*(versand|lieferung))\b",
            r"\b(free\s*(shipping|delivery|returns?)|kostenlose[rs]?\s*(versand|lieferung|rückgabe))\b",
            r"\b(next[\s-]?day|same[\s-]?day|overnight)\s*(delivery|shipping)\b",
            r"\b(prime\s*(eligible|shipping|delivery))\b",
        ],
        "note": "Shipping and fulfillment info is managed by Amazon. Never promise delivery terms in copy."
    },
}

# ═══════════════════════════════════════════════════════════════════
# FORMATTING RULES
# ═══════════════════════════════════════════════════════════════════

FORMATTING_RULES = {
    "all_caps_words": {
        "description": "Excessive use of ALL CAPS (more than 2 consecutive caps words)",
        "severity": "warning",
        "check": lambda text: bool(re.search(r"\b[A-ZÄÖÜ]{3,}\s+[A-ZÄÖÜ]{3,}\s+[A-ZÄÖÜ]{3,}\b", text)),
        "note": "ALL CAPS is aggressive. Use sparingly — max 1-2 words for emphasis."
    },
    "excessive_punctuation": {
        "description": "Excessive punctuation (!!!, ???, ...)",
        "severity": "warning",
        "check": lambda text: bool(re.search(r"[!]{2,}|[?]{2,}|\.{4,}", text)),
        "note": "Multiple exclamation/question marks look unprofessional."
    },
    "emoji_in_copy": {
        "description": "Emojis in listing copy",
        "severity": "warning",
        "check": lambda text: bool(re.search(
            r"[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF"
            r"\U00002702-\U000027B0\U0001f900-\U0001f9FF\U00002600-\U000026FF]",
            text
        )),
        "note": "Emojis are not allowed in A+ content. In listing images, use with caution."
    },
}


def check_text(text, context="general"):
    """
    Check text against all compliance rules.

    Args:
        text: The copy text to check
        context: 'listing_image', 'aplus', 'alt_text', or 'general'

    Returns dict with violations, warnings, and summary.
    """
    results = {
        "text_checked": text[:200] + "..." if len(text) > 200 else text,
        "context": context,
        "violations": [],
        "warnings": [],
        "passed": True,
    }

    # Check prohibited words/patterns
    for rule_id, rule in PROHIBITED_WORDS.items():
        for pattern in rule["patterns"]:
            matches = re.findall(pattern, text, re.IGNORECASE)
            if matches:
                finding = {
                    "rule": rule_id,
                    "description": rule["description"],
                    "matches": list(set(m if isinstance(m, str) else m[0] for m in matches))[:5],
                    "severity": rule["severity"],
                    "note": rule["note"],
                }

                if rule["severity"] == "violation":
                    results["violations"].append(finding)
                    results["passed"] = False
                else:
                    results["warnings"].append(finding)

    # Check formatting rules
    for rule_id, rule in FORMATTING_RULES.items():
        if rule["check"](text):
            finding = {
                "rule": rule_id,
                "description": rule["description"],
                "severity": rule["severity"],
                "note": rule["note"],
            }
            results["warnings"].append(finding)

    return results


def check_file(filepath):
    """Check an entire content brief file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Split into sections and check each
    sections = re.split(r"^##\s+", content, flags=re.MULTILINE)

    all_results = {
        "file": filepath,
        "sections": [],
        "summary": {
            "total_violations": 0,
            "total_warnings": 0,
            "passed": True,
        }
    }

    for section in sections:
        if not section.strip():
            continue

        # Get section title
        lines = section.strip().split("\n")
        title = lines[0].strip()
        text = "\n".join(lines[1:])

        if not text.strip():
            continue

        # Determine context from section title
        context = "general"
        title_lower = title.lower()
        if "image" in title_lower or "listing" in title_lower:
            context = "listing_image"
        elif "a+" in title_lower or "premium" in title_lower or "module" in title_lower:
            context = "aplus"
        elif "alt" in title_lower:
            context = "alt_text"

        result = check_text(text, context)
        result["section"] = title

        all_results["sections"].append(result)
        all_results["summary"]["total_violations"] += len(result["violations"])
        all_results["summary"]["total_warnings"] += len(result["warnings"])

        if not result["passed"]:
            all_results["summary"]["passed"] = False

    return all_results


def check_copy_list(copy_items):
    """
    Check a list of copy items.
    Each item should be a dict with 'text' and optionally 'context' and 'label'.
    """
    results = []
    total_violations = 0
    total_warnings = 0

    for item in copy_items:
        text = item.get("text", "")
        context = item.get("context", "general")
        label = item.get("label", "")

        result = check_text(text, context)
        result["label"] = label
        results.append(result)

        total_violations += len(result["violations"])
        total_warnings += len(result["warnings"])

    return {
        "items_checked": len(results),
        "results": results,
        "summary": {
            "total_violations": total_violations,
            "total_warnings": total_warnings,
            "passed": total_violations == 0,
        }
    }


if __name__ == "__main__":
    if len(sys.argv) < 2 and not sys.stdin.isatty():
        # Read from stdin
        text = sys.stdin.read()
        result = check_text(text)
        print(json.dumps(result, indent=2, ensure_ascii=False))
    elif len(sys.argv) >= 2:
        if sys.argv[1] == "--stdin":
            text = sys.stdin.read()
            result = check_text(text)
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            filepath = sys.argv[1]
            if os.path.isfile(filepath):
                result = check_file(filepath)
                print(json.dumps(result, indent=2, ensure_ascii=False))
            else:
                # Treat argument as text
                result = check_text(sys.argv[1])
                print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print("Usage: python3 tools/amazon_compliance_checker.py <input_file>")
        print("       python3 tools/amazon_compliance_checker.py \"your copy text\"")
        print("       echo \"your copy text\" | python3 tools/amazon_compliance_checker.py --stdin")
        sys.exit(1)
