#!/usr/bin/env python3
"""
Scrape an Amazon product listing by ASIN.
Usage: python3 tools/scrape_amazon_listing.py <ASIN> [marketplace]

Marketplace options: de, com, co.uk (default: de)

Outputs JSON with: title, bullets, description, price, rating, review_count,
                   image_urls, brand, category, availability
"""

import sys
import json
import re
import time
import random
import os
from urllib.parse import quote

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
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
]


def get_headers():
    return {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9,de;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "DNT": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
    }


def scrape_listing(asin, marketplace="de"):
    """Scrape a single Amazon product listing."""
    domain = MARKETPLACE_DOMAINS.get(marketplace, MARKETPLACE_DOMAINS["de"])
    url = f"https://{domain}/dp/{asin}"

    session = requests.Session()
    session.headers.update(get_headers())

    # Initial request
    response = session.get(url, timeout=15)

    if response.status_code != 200:
        return {"error": f"HTTP {response.status_code}", "url": url}

    soup = BeautifulSoup(response.text, "lxml")

    data = {
        "asin": asin,
        "marketplace": marketplace,
        "url": url,
        "title": _get_title(soup),
        "brand": _get_brand(soup),
        "price": _get_price(soup),
        "rating": _get_rating(soup),
        "review_count": _get_review_count(soup),
        "bullets": _get_bullets(soup),
        "description": _get_description(soup),
        "image_urls": _get_images(soup, response.text),
        "categories": _get_categories(soup),
        "availability": _get_availability(soup),
        "bestseller_rank": _get_bsr(soup),
    }

    return data


def _get_title(soup):
    el = soup.find("span", {"id": "productTitle"})
    if el:
        return el.get_text(strip=True)
    el = soup.find("h1", {"id": "title"})
    return el.get_text(strip=True) if el else None


def _get_brand(soup):
    el = soup.find("a", {"id": "bylineInfo"})
    if el:
        text = el.get_text(strip=True)
        # Remove "Visit the X Store" or "Brand: X" patterns
        text = re.sub(r"(Visit the |Brand:\s*|Marke:\s*|Besuche den |-Store$| Store$)", "", text)
        return text.strip()
    return None


def _get_price(soup):
    # Try multiple price selectors
    selectors = [
        ("span", {"class": "a-price-whole"}),
        ("span", {"id": "priceblock_ourprice"}),
        ("span", {"id": "priceblock_dealprice"}),
        ("span", {"class": "a-offscreen"}),
    ]
    for tag, attrs in selectors:
        el = soup.find(tag, attrs)
        if el:
            text = el.get_text(strip=True)
            # Clean price string
            price_match = re.search(r"[\d.,]+", text)
            if price_match:
                return text
    return None


def _get_rating(soup):
    el = soup.find("span", {"class": "a-icon-alt"})
    if el:
        text = el.get_text(strip=True)
        match = re.search(r"([\d.,]+)", text)
        if match:
            return match.group(1)
    return None


def _get_review_count(soup):
    el = soup.find("span", {"id": "acrCustomerReviewCount"})
    if el:
        text = el.get_text(strip=True)
        match = re.search(r"([\d.,]+)", text)
        if match:
            return match.group(1).replace(".", "").replace(",", "")
    return None


def _get_bullets(soup):
    bullets = []
    feature_div = soup.find("div", {"id": "feature-bullets"})
    if feature_div:
        items = feature_div.find_all("span", {"class": "a-list-item"})
        for item in items:
            text = item.get_text(strip=True)
            if text and len(text) > 5:
                bullets.append(text)
    return bullets


def _get_description(soup):
    # Product description
    desc_div = soup.find("div", {"id": "productDescription"})
    if desc_div:
        return desc_div.get_text(strip=True)
    return None


def _get_images(soup, html_text):
    """Extract high-res image URLs from the page."""
    images = []

    # Method 1: Parse from JavaScript data
    pattern = r'"hiRes"\s*:\s*"(https://[^"]+)"'
    matches = re.findall(pattern, html_text)
    if matches:
        images = list(dict.fromkeys(matches))  # deduplicate preserving order

    # Method 2: Fallback to image tags
    if not images:
        img_container = soup.find("div", {"id": "altImages"})
        if img_container:
            for img in img_container.find_all("img"):
                src = img.get("src", "")
                if "images/I/" in src:
                    # Convert thumbnail to large
                    large = re.sub(r"\._[A-Z0-9_,]+_\.", ".", src)
                    images.append(large)

    return images[:9]  # Max 9 images


def _get_categories(soup):
    breadcrumbs = soup.find("div", {"id": "wayfinding-breadcrumbs_container"})
    if breadcrumbs:
        items = breadcrumbs.find_all("a", {"class": "a-link-normal"})
        return [item.get_text(strip=True) for item in items]
    return []


def _get_availability(soup):
    el = soup.find("div", {"id": "availability"})
    if el:
        return el.get_text(strip=True)
    return None


def _get_bsr(soup):
    """Extract Best Seller Rank."""
    ranks = []
    # Try product details table
    rows = soup.find_all("tr")
    for row in rows:
        text = row.get_text()
        if "Best Sellers Rank" in text or "Bestseller-Rang" in text or "Amazon Bestseller-Rang" in text:
            rank_matches = re.findall(r"Nr\.\s*([\d.]+)\s*in\s*(.+?)(?:\(|$)", text)
            if not rank_matches:
                rank_matches = re.findall(r"#([\d,]+)\s*in\s*(.+?)(?:\(|$)", text)
            for rank, category in rank_matches:
                ranks.append({
                    "rank": rank.strip().replace(".", "").replace(",", ""),
                    "category": category.strip()
                })

    # Try detail bullets
    if not ranks:
        bullets = soup.find_all("li")
        for li in bullets:
            text = li.get_text()
            if "Best Sellers Rank" in text or "Bestseller-Rang" in text:
                rank_matches = re.findall(r"Nr\.\s*([\d.]+)\s*in\s*(.+?)(?:\(|$)", text)
                if not rank_matches:
                    rank_matches = re.findall(r"#([\d,]+)\s*in\s*(.+?)(?:\(|$)", text)
                for rank, category in rank_matches:
                    ranks.append({
                        "rank": rank.strip().replace(".", "").replace(",", ""),
                        "category": category.strip()
                    })

    return ranks if ranks else None


def scrape_multiple(asins, marketplace="de", delay_range=(2, 5)):
    """Scrape multiple ASINs with random delays."""
    results = []
    for i, asin in enumerate(asins):
        print(f"Scraping {asin} ({i+1}/{len(asins)})...")
        result = scrape_listing(asin, marketplace)
        results.append(result)

        if i < len(asins) - 1:
            delay = random.uniform(*delay_range)
            print(f"  Waiting {delay:.1f}s...")
            time.sleep(delay)

    return results


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 tools/scrape_amazon_listing.py <ASIN> [marketplace]")
        print("       python3 tools/scrape_amazon_listing.py <ASIN1,ASIN2,ASIN3> [marketplace]")
        print("Marketplaces: de, com, co.uk")
        sys.exit(1)

    asin_input = sys.argv[1]
    marketplace = sys.argv[2] if len(sys.argv) > 2 else "de"

    asins = [a.strip() for a in asin_input.split(",")]

    if len(asins) == 1:
        result = scrape_listing(asins[0], marketplace)
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        results = scrape_multiple(asins, marketplace)
        print(json.dumps(results, indent=2, ensure_ascii=False))
