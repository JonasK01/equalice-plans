#!/usr/bin/env python3
"""
Analyze competitor listing images for visual patterns and gaps.
Usage: python3 tools/analyze_category_visuals.py <ASIN1,ASIN2,ASIN3> [marketplace]

Fetches listing images from competitor ASINs and saves them locally
for analysis. Outputs a JSON report with image URLs and metadata.

The agent (Claude) then analyzes these images visually.

Marketplace options: de, com, co.uk (default: de)
"""

import sys
import json
import os
import re
import time
import random

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
]

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".tmp", "competitor_images")


def get_headers():
    return {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9,de;q=0.8",
        "DNT": "1",
        "Connection": "keep-alive",
    }


def fetch_listing_images(asin, marketplace="de"):
    """Fetch all image URLs and product info from a listing."""
    domain = MARKETPLACE_DOMAINS.get(marketplace, MARKETPLACE_DOMAINS["de"])
    url = f"https://{domain}/dp/{asin}"

    session = requests.Session()
    session.headers.update(get_headers())
    response = session.get(url, timeout=15)

    if response.status_code != 200:
        return {"asin": asin, "error": f"HTTP {response.status_code}"}

    soup = BeautifulSoup(response.text, "lxml")

    # Get title
    title_el = soup.find("span", {"id": "productTitle"})
    title = title_el.get_text(strip=True) if title_el else "Unknown"

    # Get images from JavaScript
    images = []
    pattern = r'"hiRes"\s*:\s*"(https://[^"]+)"'
    matches = re.findall(pattern, response.text)
    if matches:
        images = list(dict.fromkeys(matches))[:9]

    # Fallback: get from image tags
    if not images:
        pattern2 = r'"large"\s*:\s*"(https://[^"]+)"'
        matches2 = re.findall(pattern2, response.text)
        if matches2:
            images = list(dict.fromkeys(matches2))[:9]

    return {
        "asin": asin,
        "title": title,
        "url": url,
        "image_count": len(images),
        "image_urls": images,
    }


def download_images(asin, image_urls, marketplace):
    """Download images to local .tmp directory for visual inspection."""
    asin_dir = os.path.join(OUTPUT_DIR, f"{asin}_{marketplace}")
    os.makedirs(asin_dir, exist_ok=True)

    downloaded = []
    session = requests.Session()
    session.headers.update(get_headers())

    for i, url in enumerate(image_urls):
        try:
            response = session.get(url, timeout=10)
            if response.status_code == 200:
                # Determine extension
                ext = ".jpg"
                content_type = response.headers.get("Content-Type", "")
                if "png" in content_type:
                    ext = ".png"
                elif "webp" in content_type:
                    ext = ".webp"

                filename = f"image_{i+1:02d}{ext}"
                filepath = os.path.join(asin_dir, filename)

                with open(filepath, "wb") as f:
                    f.write(response.content)

                downloaded.append({
                    "slot": i + 1,
                    "filename": filename,
                    "filepath": filepath,
                    "url": url,
                    "size_kb": round(len(response.content) / 1024, 1),
                })
            time.sleep(random.uniform(0.3, 0.8))
        except Exception as e:
            downloaded.append({
                "slot": i + 1,
                "error": str(e),
                "url": url,
            })

    return downloaded


def analyze_competitors(asins, marketplace="de", download=True):
    """Fetch and optionally download images for multiple competitor ASINs."""
    results = []

    for i, asin in enumerate(asins):
        asin = asin.strip()
        print(f"Fetching images for {asin} ({i+1}/{len(asins)})...")

        listing_data = fetch_listing_images(asin, marketplace)

        if "error" in listing_data:
            results.append(listing_data)
            continue

        if download and listing_data.get("image_urls"):
            print(f"  Downloading {len(listing_data['image_urls'])} images...")
            listing_data["downloaded_images"] = download_images(
                asin, listing_data["image_urls"], marketplace
            )

        results.append(listing_data)

        if i < len(asins) - 1:
            time.sleep(random.uniform(2, 4))

    report = {
        "marketplace": marketplace,
        "competitors_analyzed": len(results),
        "competitors": results,
        "summary": {
            "total_images": sum(r.get("image_count", 0) for r in results),
            "avg_images_per_listing": round(
                sum(r.get("image_count", 0) for r in results) / len(results), 1
            ) if results else 0,
        },
    }

    if download:
        report["images_saved_to"] = OUTPUT_DIR

    return report


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 tools/analyze_category_visuals.py <ASIN1,ASIN2,ASIN3> [marketplace] [--no-download]")
        print("Marketplaces: de, com, co.uk")
        sys.exit(1)

    asin_input = sys.argv[1]
    marketplace = "de"
    download = True

    for arg in sys.argv[2:]:
        if arg == "--no-download":
            download = False
        else:
            marketplace = arg

    asins = [a.strip() for a in asin_input.split(",")]

    result = analyze_competitors(asins, marketplace, download)
    print(json.dumps(result, indent=2, ensure_ascii=False))
