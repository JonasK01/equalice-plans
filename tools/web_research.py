#!/usr/bin/env python3
"""
Web research tool for product trends, lifestyle context, and buyer insights.
Usage: python3 tools/web_research.py <query> [--market de|com|uk]

Searches the web for product-related information useful for creating
Amazon listing content: trends, use cases, buyer demographics, lifestyle context.

Outputs JSON with search results and extracted content.
"""

import sys
import json
import re
import random
import time
from urllib.parse import quote_plus, urljoin

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Missing dependencies. Run: pip3 install requests beautifulsoup4 lxml")
    sys.exit(1)


USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
]

SEARCH_CONFIGS = {
    "de": {"domain": "www.google.de", "lang": "de", "country": "DE"},
    "com": {"domain": "www.google.com", "lang": "en", "country": "US"},
    "uk": {"domain": "www.google.co.uk", "lang": "en", "country": "GB"},
    "co.uk": {"domain": "www.google.co.uk", "lang": "en", "country": "GB"},
}


def google_search(query, market="com", num_results=10):
    """Search Google and return results."""
    config = SEARCH_CONFIGS.get(market, SEARCH_CONFIGS["com"])

    url = f"https://{config['domain']}/search"
    params = {
        "q": query,
        "num": num_results,
        "hl": config["lang"],
        "gl": config["country"],
    }

    headers = {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": f"{config['lang']},en;q=0.9",
    }

    try:
        response = requests.get(url, params=params, headers=headers, timeout=15)
        if response.status_code != 200:
            return {"error": f"HTTP {response.status_code}"}

        soup = BeautifulSoup(response.text, "lxml")
        results = []

        for div in soup.find_all("div", class_="g"):
            title_el = div.find("h3")
            link_el = div.find("a", href=True)
            snippet_el = div.find("div", class_="VwiC3b") or div.find("span", class_="aCOpRe")

            if title_el and link_el:
                href = link_el["href"]
                if href.startswith("/url?q="):
                    href = href.split("/url?q=")[1].split("&")[0]

                results.append({
                    "title": title_el.get_text(strip=True),
                    "url": href,
                    "snippet": snippet_el.get_text(strip=True) if snippet_el else "",
                })

        return results

    except Exception as e:
        return {"error": str(e)}


def fetch_page_content(url, max_chars=3000):
    """Fetch and extract main text content from a URL."""
    headers = {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            return None

        soup = BeautifulSoup(response.text, "lxml")

        # Remove noise
        for tag in soup.find_all(["script", "style", "nav", "footer", "header", "aside"]):
            tag.decompose()

        # Try main content containers
        main = (
            soup.find("main") or
            soup.find("article") or
            soup.find("div", class_=re.compile(r"(content|article|post|entry)", re.I)) or
            soup.find("body")
        )

        if main:
            text = main.get_text(separator=" ", strip=True)
            # Clean up whitespace
            text = re.sub(r"\s+", " ", text)
            return text[:max_chars]

        return None

    except Exception:
        return None


def research_product(query, market="com", deep=False):
    """
    Research a product topic across multiple search angles.

    Searches for:
    1. Product trends and market context
    2. Buyer demographics and use cases
    3. Lifestyle and usage scenarios
    4. Common problems and solutions
    """
    search_angles = [
        f"{query} trends 2025 2026",
        f"{query} buyer demographics who buys",
        f"{query} use cases lifestyle",
        f"{query} common problems complaints",
        f"{query} buying guide what to look for",
    ]

    all_results = {}

    for i, search_query in enumerate(search_angles):
        angle_name = ["trends", "demographics", "lifestyle", "problems", "buying_guide"][i]
        print(f"  Searching: {search_query}...")

        results = google_search(search_query, market)

        if isinstance(results, list):
            all_results[angle_name] = results

            # Optionally fetch page content for top results
            if deep and results:
                for j, result in enumerate(results[:2]):
                    print(f"    Fetching content from: {result['title'][:50]}...")
                    content = fetch_page_content(result["url"])
                    if content:
                        results[j]["content_extract"] = content
                    time.sleep(random.uniform(1, 2))

        time.sleep(random.uniform(1.5, 3))

    return {
        "query": query,
        "market": market,
        "research": all_results,
        "total_results": sum(
            len(v) for v in all_results.values() if isinstance(v, list)
        ),
    }


def research_competitors(product_name, competitor_brands, market="com"):
    """Research specific competitor brands and their positioning."""
    results = {}

    for brand in competitor_brands:
        query = f"{brand} {product_name} review"
        print(f"  Researching competitor: {brand}...")
        search_results = google_search(query, market, num_results=5)
        if isinstance(search_results, list):
            results[brand] = search_results
        time.sleep(random.uniform(2, 4))

    return {
        "product": product_name,
        "competitors": results,
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 tools/web_research.py <query> [--market de|com|uk] [--deep]")
        print("       python3 tools/web_research.py <query> --competitors \"Brand1,Brand2\"")
        print("")
        print("Options:")
        print("  --market    Target market (de, com, uk). Default: com")
        print("  --deep      Also fetch page content from top results")
        print("  --competitors  Research specific competitor brands")
        sys.exit(1)

    query = sys.argv[1]
    market = "com"
    deep = False
    competitors = None

    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == "--market" and i + 1 < len(sys.argv):
            market = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == "--deep":
            deep = True
            i += 1
        elif sys.argv[i] == "--competitors" and i + 1 < len(sys.argv):
            competitors = [c.strip() for c in sys.argv[i + 1].split(",")]
            i += 2
        else:
            market = sys.argv[i]
            i += 1

    if competitors:
        result = research_competitors(query, competitors, market)
    else:
        print(f"Researching '{query}' for market: {market}...")
        result = research_product(query, market, deep)

    print(json.dumps(result, indent=2, ensure_ascii=False))
