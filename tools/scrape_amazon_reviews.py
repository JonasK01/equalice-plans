#!/usr/bin/env python3
"""
Scrape Amazon product reviews by ASIN.
Usage: python3 tools/scrape_amazon_reviews.py <ASIN> [marketplace] [pages]

Marketplace options: de, com, co.uk (default: de)
Pages: number of review pages to scrape (default: 3, max: 10)

Outputs JSON with individual reviews + analysis summary:
  - top praise themes, top complaint themes, emotional triggers, purchase drivers
"""

import sys
import json
import re
import time
import random
from collections import Counter

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Missing dependencies. Run: pip3 install requests beautifulsoup4 lxml")
    sys.exit(1)


MARKETPLACE_DOMAINS = {
    "de": "www.amazon.de",
    "com": "www.amazon.com",
    "co.uk": "www.amazon.co.uk",
    "uk": "www.amazon.co.uk",
}

USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.2 Safari/605.1.15",
]


def get_headers():
    return {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9,de;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "DNT": "1",
        "Connection": "keep-alive",
    }


def _parse_reviews_from_html(html):
    """Parse reviews from any Amazon HTML page (product detail or product-reviews)."""
    soup = BeautifulSoup(html, "lxml")
    reviews = []

    review_divs = soup.find_all("div", {"data-hook": "review"})

    for div in review_divs:
        review = {}

        # Title — current hook is "reviewTitle" (camelCase). Fallback to legacy hooks.
        title_el = (
            div.find(attrs={"data-hook": "reviewTitle"})
            or div.find("a", {"data-hook": "review-title"})
            or div.find("span", {"data-hook": "review-title"})
        )
        if title_el:
            spans = title_el.find_all("span")
            # Heuristic: last non-empty span is usually the title text
            cand = [s.get_text(strip=True) for s in spans if s.get_text(strip=True)]
            review["title"] = cand[-1] if cand else title_el.get_text(strip=True)

        # Rating
        rating_el = (
            div.find("i", {"data-hook": "review-star-rating"})
            or div.find("i", {"data-hook": "cmps-review-star-rating"})
            or div.find(attrs={"data-hook": "review-star-rating"})
        )
        if rating_el:
            text = rating_el.get_text(" ", strip=True)
            match = re.search(r"([\d.,]+)\s*out of", text) or re.search(r"([\d.,]+)", text)
            if match:
                try:
                    review["rating"] = float(match.group(1).replace(",", "."))
                except ValueError:
                    pass

        # Body — current hook is "reviewText". Fallback to "review-body".
        body_el = (
            div.find(attrs={"data-hook": "reviewText"})
            or div.find("span", {"data-hook": "review-body"})
        )
        if body_el:
            review["body"] = body_el.get_text(" ", strip=True)

        # Date
        date_el = div.find(attrs={"data-hook": "review-date"})
        if date_el:
            review["date"] = date_el.get_text(strip=True)

        # Variation (size/color)
        var_el = div.find(attrs={"data-hook": "product-variation-attributes"}) or div.find(attrs={"data-hook": "format-strip"})
        if var_el:
            review["variation"] = var_el.get_text(" ", strip=True)

        # Verified purchase
        verified_el = div.find(attrs={"data-hook": "avp-badge"})
        review["verified"] = verified_el is not None

        # Helpful count
        helpful_el = div.find(attrs={"data-hook": "helpful-vote-statement"})
        if helpful_el:
            text = helpful_el.get_text(strip=True)
            match = re.search(r"(\d+)", text)
            review["helpful_votes"] = int(match.group(1)) if match else 1
        else:
            review["helpful_votes"] = 0

        if review.get("body"):
            reviews.append(review)

    return reviews


def scrape_reviews_page(asin, marketplace, page=1, star_filter=None, session=None):
    """Scrape reviews. Tries /product-reviews/ first; falls back to product detail page (page 1 only).

    Note: Amazon's /product-reviews/ endpoint redirects unauthenticated traffic to login (302).
    The product detail page returns ~8 top reviews without login, so page 1 always falls back there.
    """
    domain = MARKETPLACE_DOMAINS.get(marketplace, MARKETPLACE_DOMAINS["de"])

    if session is None:
        session = requests.Session()
        session.headers.update(get_headers())

    # Try /product-reviews/ (will likely 302 to login for anon traffic)
    url = f"https://{domain}/product-reviews/{asin}"
    params = {"pageNumber": page, "sortBy": "recent"}
    if star_filter:
        params["filterByStar"] = f"{star_filter}_star"

    response = session.get(url, params=params, timeout=15, allow_redirects=False)
    if response.status_code == 200:
        reviews = _parse_reviews_from_html(response.text)
        if reviews:
            return reviews

    # Fallback: scrape the product detail page (only useful for page 1)
    if page == 1:
        dp_response = session.get(f"https://{domain}/dp/{asin}", timeout=15)
        if dp_response.status_code == 200:
            return _parse_reviews_from_html(dp_response.text)

    return []


def scrape_all_reviews(asin, marketplace="de", max_pages=3):
    """Scrape multiple pages of reviews."""
    session = requests.Session()
    session.headers.update(get_headers())

    all_reviews = []

    for page in range(1, max_pages + 1):
        print(f"  Scraping review page {page}/{max_pages}...", file=sys.stderr)
        reviews = scrape_reviews_page(asin, marketplace, page, session=session)

        if not reviews:
            print(f"  No reviews found on page {page}, stopping.", file=sys.stderr)
            break

        all_reviews.extend(reviews)

        if page < max_pages:
            time.sleep(random.uniform(1.5, 3.5))

    return all_reviews


def analyze_reviews(reviews):
    """Analyze reviews and extract key insights."""
    if not reviews:
        return {"error": "No reviews to analyze"}

    analysis = {
        "total_reviews_scraped": len(reviews),
        "average_rating": 0,
        "rating_distribution": {5: 0, 4: 0, 3: 0, 2: 0, 1: 0},
        "positive_reviews": [],     # 4-5 stars
        "negative_reviews": [],     # 1-2 stars
        "neutral_reviews": [],      # 3 stars
        "most_helpful": [],
        "verified_percentage": 0,
    }

    ratings = []
    verified_count = 0

    for review in reviews:
        rating = review.get("rating")
        if rating:
            ratings.append(rating)
            rounded = round(rating)
            if rounded in analysis["rating_distribution"]:
                analysis["rating_distribution"][rounded] += 1

            if rating >= 4:
                analysis["positive_reviews"].append({
                    "title": review.get("title", ""),
                    "body": review.get("body", "")[:500],
                    "rating": rating,
                })
            elif rating <= 2:
                analysis["negative_reviews"].append({
                    "title": review.get("title", ""),
                    "body": review.get("body", "")[:500],
                    "rating": rating,
                })
            else:
                analysis["neutral_reviews"].append({
                    "title": review.get("title", ""),
                    "body": review.get("body", "")[:500],
                    "rating": rating,
                })

        if review.get("verified"):
            verified_count += 1

    if ratings:
        analysis["average_rating"] = round(sum(ratings) / len(ratings), 2)

    analysis["verified_percentage"] = round(
        (verified_count / len(reviews)) * 100, 1
    ) if reviews else 0

    # Most helpful reviews
    sorted_by_helpful = sorted(reviews, key=lambda r: r.get("helpful_votes", 0), reverse=True)
    analysis["most_helpful"] = [
        {
            "title": r.get("title", ""),
            "body": r.get("body", "")[:500],
            "rating": r.get("rating"),
            "helpful_votes": r.get("helpful_votes", 0),
        }
        for r in sorted_by_helpful[:5]
    ]

    # Trim lists for readability
    analysis["positive_reviews"] = analysis["positive_reviews"][:10]
    analysis["negative_reviews"] = analysis["negative_reviews"][:10]
    analysis["neutral_reviews"] = analysis["neutral_reviews"][:5]

    return analysis


def scrape_and_analyze(asin, marketplace="de", max_pages=3):
    """Full pipeline: scrape reviews and analyze."""
    print(f"Scraping reviews for {asin} on amazon.{marketplace}...", file=sys.stderr)
    reviews = scrape_all_reviews(asin, marketplace, max_pages)

    print(f"Analyzing {len(reviews)} reviews...", file=sys.stderr)
    analysis = analyze_reviews(reviews)

    return {
        "asin": asin,
        "marketplace": marketplace,
        "reviews": reviews,
        "analysis": analysis,
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 tools/scrape_amazon_reviews.py <ASIN> [marketplace] [pages]")
        print("Marketplaces: de, com, co.uk")
        print("Pages: 1-10 (default: 3)")
        sys.exit(1)

    asin = sys.argv[1]
    marketplace = sys.argv[2] if len(sys.argv) > 2 else "de"
    max_pages = int(sys.argv[3]) if len(sys.argv) > 3 else 3

    max_pages = min(max_pages, 10)

    result = scrape_and_analyze(asin, marketplace, max_pages)
    print(json.dumps(result, indent=2, ensure_ascii=False))
