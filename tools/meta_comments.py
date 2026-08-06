#!/usr/bin/env python3
"""
Meta Comment Analyzer — Buyer-Persona aus Ad-/Post-Kommentaren.

Zieht Kommentare von:
  - allen AKTIVEN Ads eines Ad-Accounts (Facebook Dark-Posts + Instagram-Media)
  - den organischen Posts der verknüpften Facebook-Page und des Instagram-Accounts

und lässt sie von Claude zu einer Buyer-Persona auswerten
(Wünsche, Pain-Points, Einwände, Sprache, FAQ, Content-Angles).

Rohdaten landen in .tmp/<slug>_comments.{json,csv},
der Persona-Report in .tmp/<slug>_persona.md.

.env-Variablen:
  META_LONG_TOKEN (oder META_SHORT_TOKEN)   – Meta User-Token
  META_API_VERSION                          – z.B. v21.0 (Default)
  ANTHROPIC_API_KEY                         – für die Persona-Analyse

 NÖTIGE META-BERECHTIGUNGEN (sonst gibt die Graph API Fehler #10/#200):
  pages_read_engagement, pages_read_user_content,
  instagram_basic, instagram_manage_comments

Usage:
  python3 tools/meta_comments.py --account act_2088057028161457 --slug dr_denese
  python3 tools/meta_comments.py --account act_2088057028161457 --no-organic
  python3 tools/meta_comments.py --account act_2088057028161457 --no-analyze   # nur Export
"""

import argparse
import csv
import json
import sys
import time
from pathlib import Path

try:
    import requests
except ImportError:
    print("Missing dependency. Run: pip3 install requests")
    sys.exit(1)


PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENV_PATH = PROJECT_ROOT / ".env"
TMP_DIR = PROJECT_ROOT / ".tmp"
API_VERSION_DEFAULT = "v21.0"
GRAPH = "https://graph.facebook.com"

# Wie viele Kommentare maximal an Claude gehen (Token-Schutz). 0 = alle.
MAX_COMMENTS_FOR_ANALYSIS = 1500
MAX_COMMENTS_PER_POST = 500   # Schutz vor Riesen-Posts (Timeout/Runaway)
ANALYSIS_MODEL = "claude-opus-4-8"


# --------------------------------------------------------------------------- #
# .env
# --------------------------------------------------------------------------- #
def load_env(path: Path) -> dict:
    env = {}
    if not path.exists():
        return env
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        env[key.strip()] = value.strip()
    return env


# --------------------------------------------------------------------------- #
# Graph-API Helpers
# --------------------------------------------------------------------------- #
def graph_get(path: str, token: str, version: str, **params) -> dict:
    url = f"{GRAPH}/{version}/{path}"
    params["access_token"] = token
    resp = requests.get(url, params=params, timeout=30)
    return resp.json()


def _get_with_retry(url: str, params, timeout: int = 45, retries: int = 2) -> dict:
    """GET mit Retry bei Netzwerk-/Timeout-Fehlern. Wirft RuntimeError bei Aufgabe."""
    last = None
    for attempt in range(retries + 1):
        try:
            resp = requests.get(url, params=params, timeout=timeout)
            return resp.json()
        except requests.exceptions.RequestException as e:
            last = e
    raise RuntimeError(f"network error after {retries + 1} tries: {last}")


def paginate(path: str, token: str, version: str, max_items: int = 0, **params) -> list:
    """Holt Seiten einer Edge. max_items>0 begrenzt (Schutz vor Riesen-Posts)."""
    out = []
    params["access_token"] = token
    url = f"{GRAPH}/{version}/{path}"
    pages = 0
    while url and pages < 200:
        data = _get_with_retry(url, params)
        pages += 1
        if "error" in data:
            err = data["error"]
            raise RuntimeError(
                f"Graph API error (code {err.get('code')}): {err.get('message')}"
            )
        out.extend(data.get("data", []))
        if max_items and len(out) >= max_items:
            return out[:max_items]
        url = data.get("paging", {}).get("next")
        params = None  # 'next' enthält schon alle Query-Params
    return out


def get_page_for_account(account_id: str, user_token: str, version: str) -> dict:
    """Promoted-Object/Page hinter dem Ad-Account finden + Page-Token holen."""
    # Pages, auf die der User Zugriff hat (inkl. Page-Token + IG-Account)
    me_accounts = paginate(
        "me/accounts", user_token, version,
        fields="name,id,access_token,instagram_business_account{id,username}",
    )
    return me_accounts


def page_token_for(page_id: str, user_token: str, version: str) -> str:
    data = graph_get(page_id, user_token, version, fields="access_token")
    return data.get("access_token", "")


# --------------------------------------------------------------------------- #
# Kommentar-Quellen sammeln
# --------------------------------------------------------------------------- #
def ad_posts(account_id: str, user_token: str, version: str, status: str = "active") -> dict:
    """Liefert {fb_post_ids:set, ig_media_ids:set} der Ads.

    status="active" → nur laufende Ads; status="all" → alle (inkl. pausiert).
    """
    params = dict(
        fields="name,creative{effective_object_story_id,effective_instagram_media_id}",
        limit=100,
    )
    if status == "active":
        params["effective_status"] = json.dumps(["ACTIVE"])
    ads = paginate(f"{account_id}/ads", user_token, version, **params)
    fb_posts, ig_media = set(), set()
    for ad in ads:
        creative = ad.get("creative", {})
        if creative.get("effective_object_story_id"):
            fb_posts.add(creative["effective_object_story_id"])
        if creative.get("effective_instagram_media_id"):
            ig_media.add(creative["effective_instagram_media_id"])
    return {"fb_posts": fb_posts, "ig_media": ig_media, "n_ads": len(ads)}


def organic_fb_posts(page_id: str, page_token: str, version: str, limit: int = 50) -> set:
    posts = paginate(f"{page_id}/posts", page_token, version,
                     fields="id", limit=limit)
    return {p["id"] for p in posts}


def organic_ig_media(ig_id: str, user_token: str, version: str, limit: int = 50) -> set:
    media = paginate(f"{ig_id}/media", user_token, version,
                     fields="id", limit=limit)
    return {m["id"] for m in media}


def fetch_fb_comments(post_id: str, page_token: str, version: str) -> list:
    rows = paginate(
        f"{post_id}/comments", page_token, version,
        max_items=MAX_COMMENTS_PER_POST,
        filter="stream", order="reverse_chronological",
        fields="from{name},message,created_time,like_count",
        limit=100,
    )
    out = []
    for c in rows:
        msg = (c.get("message") or "").strip()
        if not msg:
            continue
        out.append({
            "source": "facebook",
            "post_id": post_id,
            "author": (c.get("from") or {}).get("name", ""),
            "text": msg,
            "created_time": c.get("created_time", ""),
            "likes": c.get("like_count", 0),
        })
    return out


def fetch_ig_comments(media_id: str, user_token: str, version: str) -> list:
    rows = paginate(
        f"{media_id}/comments", user_token, version,
        max_items=MAX_COMMENTS_PER_POST,
        fields="username,text,timestamp,like_count",
        limit=100,
    )
    out = []
    for c in rows:
        msg = (c.get("text") or "").strip()
        if not msg:
            continue
        out.append({
            "source": "instagram",
            "post_id": media_id,
            "author": c.get("username", ""),
            "text": msg,
            "created_time": c.get("timestamp", ""),
            "likes": c.get("like_count", 0),
        })
    return out


# --------------------------------------------------------------------------- #
# Persona-Analyse via Claude
# --------------------------------------------------------------------------- #
def analyze_persona(comments: list, brand: str, api_key: str) -> str:
    try:
        import anthropic
        from pydantic import BaseModel
    except ImportError:
        print("Missing dependency for analysis. Run: pip3 install anthropic pydantic")
        return ""

    class Persona(BaseModel):
        audience_summary: str
        demographics_signals: list[str]
        core_desires: list[str]
        pain_points: list[str]
        objections: list[str]
        emotional_triggers: list[str]
        customer_vocabulary: list[str]      # O-Töne / Formulierungen der Zielgruppe
        buying_motivations: list[str]
        frequent_questions: list[str]
        content_angles: list[str]           # Ad-/Content-Ideen abgeleitet aus den Kommentaren
        representative_quotes: list[str]

    customer = [c for c in comments if not c.get("is_brand")]
    sample = customer[:MAX_COMMENTS_FOR_ANALYSIS] if MAX_COMMENTS_FOR_ANALYSIS else customer
    dropped = len(customer) - len(sample)
    blob = "\n".join(
        f"[{c['source']}|{c['likes']}❤] {c['author']}: {c['text']}" for c in sample
    )

    client = anthropic.Anthropic(api_key=api_key)
    prompt = (
        f"Du bist Performance-Marketing-Stratege. Unten stehen echte Social-Media-"
        f"Kommentare auf Ads und Posts der Marke '{brand}'. Leite daraus eine "
        f"datenbasierte Buyer-Persona ab. Stütze JEDE Aussage auf das, was in den "
        f"Kommentaren tatsächlich steht — erfinde nichts. Für customer_vocabulary und "
        f"representative_quotes nutze möglichst wörtliche Original-Formulierungen.\n\n"
        f"=== KOMMENTARE ({len(sample)}) ===\n{blob}"
    )

    response = client.messages.parse(
        model=ANALYSIS_MODEL,
        max_tokens=16000,
        thinking={"type": "adaptive"},
        messages=[{"role": "user", "content": prompt}],
        output_format=Persona,
    )
    p = response.parsed_output

    def block(title, items):
        body = "\n".join(f"- {i}" for i in items) if isinstance(items, list) else items
        return f"## {title}\n{body}\n"

    md = [f"# Buyer-Persona — {brand}\n",
          f"_Basis: {len(sample)} Kommentare"
          + (f" (von {len(comments)}, {dropped} nicht ausgewertet)" if dropped else "")
          + f" · Modell: {ANALYSIS_MODEL}_\n",
          block("Zusammenfassung", p.audience_summary),
          block("Demografische Signale", p.demographics_signals),
          block("Kern-Wünsche", p.core_desires),
          block("Pain-Points", p.pain_points),
          block("Einwände", p.objections),
          block("Emotionale Trigger", p.emotional_triggers),
          block("Sprache der Zielgruppe (O-Töne)", p.customer_vocabulary),
          block("Kaufmotive", p.buying_motivations),
          block("Häufige Fragen", p.frequent_questions),
          block("Content-/Ad-Angles", p.content_angles),
          block("Repräsentative Zitate", p.representative_quotes)]
    return "\n".join(md)


# --------------------------------------------------------------------------- #
# Account-Pipeline (für Single- und All-Accounts-Modus)
# --------------------------------------------------------------------------- #
import re


def slugify(name: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "_", (name or "").lower()).strip("_")
    return s or "account"


def list_ad_accounts(user_token: str, version: str) -> list:
    return paginate("me/adaccounts", user_token, version,
                    fields="account_id,name,currency,account_status", limit=200)


def pages_map(user_token: str, version: str) -> dict:
    """{page_id: page_meta} aller Pages, auf die der User Zugriff hat."""
    accounts = paginate(
        "me/accounts", user_token, version,
        fields="name,id,access_token,instagram_business_account{id,username}",
    )
    return {a["id"]: a for a in accounts}


def collect_account(account_id, slug, brand, user_token, version, pmap,
                    ad_status="all", include_fb=True, include_organic=False,
                    organic_limit=50) -> dict:
    """Sammelt + exportiert Kommentare eines Accounts. Gibt Summary-Dict zurück."""
    posts = ad_posts(account_id, user_token, version, ad_status)

    page_id = next(iter(posts["fb_posts"])).split("_")[0] if posts["fb_posts"] else None
    page_meta = pmap.get(page_id) if page_id else None
    page_token = ""
    if page_meta:
        page_token = page_meta.get("access_token", "")
    elif page_id:
        page_token = page_token_for(page_id, user_token, version)
    ig_id = ((page_meta or {}).get("instagram_business_account") or {}).get("id")

    fb_posts = set(posts["fb_posts"]) if include_fb else set()
    if include_fb and not page_token:
        fb_posts = set()  # ohne Page-Token keine FB-Kommentare
    ig_media = set(posts["ig_media"])

    if include_organic:
        if page_id and page_token:
            try:
                fb_posts |= organic_fb_posts(page_id, page_token, version, organic_limit)
            except RuntimeError:
                pass
        if ig_id:
            try:
                ig_media |= organic_ig_media(ig_id, user_token, version, organic_limit)
            except RuntimeError:
                pass

    comments, errors = [], 0
    for pid in fb_posts:
        try:
            comments += fetch_fb_comments(pid, page_token, version)
        except Exception:
            errors += 1
    for mid in ig_media:
        try:
            comments += fetch_ig_comments(mid, user_token, version)
        except Exception:
            errors += 1

    # Marken-eigene Antworten markieren (Autor == Page-Name) → nicht Kundenstimme
    page_name = (page_meta or {}).get("name", "")
    for c in comments:
        c["is_brand"] = bool(page_name) and c["author"] == page_name

    seen, unique = set(), []
    for c in comments:
        k = (c["author"], c["text"])
        if k not in seen:
            seen.add(k)
            unique.append(c)
    comments = unique

    json_path = csv_path = None
    if comments:
        json_path = TMP_DIR / f"{slug}_comments.json"
        csv_path = TMP_DIR / f"{slug}_comments.csv"
        json_path.write_text(json.dumps(comments, ensure_ascii=False, indent=2))
        with csv_path.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=["source", "post_id", "author", "text",
                                              "created_time", "likes", "is_brand"])
            w.writeheader()
            w.writerows(comments)

    fb_n = sum(1 for c in comments if c["source"] == "facebook")
    ig_n = sum(1 for c in comments if c["source"] == "instagram")
    brand_n = sum(1 for c in comments if c.get("is_brand"))
    return {
        "account_id": account_id, "slug": slug, "brand": brand,
        "n_ads": posts["n_ads"], "fb_sources": len(fb_posts), "ig_sources": len(ig_media),
        "comments": comments, "n": len(comments), "fb": fb_n, "ig": ig_n,
        "brand_replies": brand_n,
        "errors": errors, "page_id": page_id,
        "json": json_path, "csv": csv_path,
    }


def maybe_analyze(summary, api_key):
    if not api_key or not summary["comments"]:
        return
    print(f"   → Persona-Analyse ({summary['n']} Kommentare) …")
    report = analyze_persona(summary["comments"], summary["brand"], api_key)
    if report:
        out = TMP_DIR / f"{summary['slug']}_persona.md"
        out.write_text(report)
        print(f"     → {out.relative_to(PROJECT_ROOT)}")


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def main() -> int:
    ap = argparse.ArgumentParser(description="Meta Comment Analyzer → Buyer-Persona")
    ap.add_argument("--account", help="Ad-Account-ID, z.B. act_2088057028161457")
    ap.add_argument("--all-accounts", action="store_true",
                    help="ALLE erreichbaren Ad-Accounts durchlaufen (eine Persona je Account)")
    ap.add_argument("--page", help="Page-ID überschreiben (sonst automatisch ermittelt)")
    ap.add_argument("--slug", default="brand", help="Dateiname-Slug für Outputs")
    ap.add_argument("--brand", default=None, help="Markenname für den Report")
    ap.add_argument("--ad-status", choices=["active", "all"], default="active",
                    help="active = nur laufende Ads; all = alle (inkl. pausiert)")
    ap.add_argument("--no-facebook", action="store_true",
                    help="FB-Comment-Calls überspringen (sind ohne pages_read_user_content #10-gesperrt)")
    ap.add_argument("--no-organic", action="store_true", help="nur Ad-Posts, keine organischen")
    ap.add_argument("--no-analyze", action="store_true", help="nur Kommentare exportieren")
    ap.add_argument("--analyze-only", action="store_true",
                    help="nichts neu ziehen — bereits exportierte .tmp/*_comments.json auswerten")
    ap.add_argument("--organic-limit", type=int, default=50)
    args = ap.parse_args()

    if not args.account and not args.all_accounts:
        print("Entweder --account <ID> oder --all-accounts angeben.")
        return 1

    env = load_env(ENV_PATH)
    user_token = env.get("META_LONG_TOKEN") or env.get("META_SHORT_TOKEN")
    version = env.get("META_API_VERSION", API_VERSION_DEFAULT)
    if not user_token:
        print("Kein META_LONG_TOKEN/META_SHORT_TOKEN in .env.")
        return 1
    api_key = None if args.no_analyze else env.get("ANTHROPIC_API_KEY")

    TMP_DIR.mkdir(exist_ok=True)

    # Analyze-only: bereits exportierte Kommentar-Dateien auswerten (kein Fetch)
    if args.analyze_only:
        if not api_key:
            print("Kein ANTHROPIC_API_KEY in .env → keine Analyse möglich.")
            return 1
        # slug → Markenname aus der Übersicht (falls vorhanden)
        names = {}
        ov = TMP_DIR / "all_accounts_overview.json"
        if ov.exists():
            for o in json.loads(ov.read_text()):
                if o.get("slug"):
                    names[o["slug"]] = o.get("name", o["slug"])
        files = sorted(TMP_DIR.glob("*_comments.json"))
        print(f"→ {len(files)} Kommentar-Dateien gefunden\n")
        for fp in files:
            slug = fp.name[:-len("_comments.json")]
            comments = json.loads(fp.read_text())
            brand = names.get(slug, slug)
            n_cust = sum(1 for c in comments if not c.get("is_brand"))
            print(f"=== {brand} ({n_cust} Kunden-Kommentare) ===")
            maybe_analyze({"comments": comments, "brand": brand, "slug": slug,
                           "n": len(comments)}, api_key)
        return 0

    include_fb = not args.no_facebook
    include_organic = not args.no_organic
    pmap = pages_map(user_token, version)

    # Account-Liste bestimmen
    if args.all_accounts:
        accounts = list_ad_accounts(user_token, version)
        targets = [(a["id"], slugify(a["name"]), a["name"]) for a in accounts]
        print(f"→ {len(targets)} Ad-Accounts gefunden\n")
    else:
        slug = args.slug if args.slug != "brand" else slugify(args.account)
        targets = [(args.account, slug, args.brand or slug)]

    overview = []
    for acc_id, slug, name in targets:
        print(f"=== {name} ({acc_id}) ===")
        try:
            s = collect_account(acc_id, slug, name, user_token, version, pmap,
                                ad_status=args.ad_status, include_fb=include_fb,
                                include_organic=include_organic,
                                organic_limit=args.organic_limit)
        except RuntimeError as e:
            print(f"   übersprungen: {e}\n")
            overview.append({"name": name, "n": 0, "note": str(e)[:60]})
            continue
        print(f"   {s['n_ads']} Ads · {s['fb_sources']} FB / {s['ig_sources']} IG Quellen "
              f"→ {s['n']} Kommentare ({s['fb']} FB / {s['ig']} IG)"
              + (f" · {s['errors']} Quellen-Fehler" if s['errors'] else ""))
        if s["json"]:
            print(f"   → {s['json'].relative_to(PROJECT_ROOT)}")
        maybe_analyze(s, api_key)
        overview.append({"name": name, "n": s["n"], "fb": s["fb"], "ig": s["ig"],
                         "slug": slug})
        print()

    # Übersicht über alle Accounts
    if args.all_accounts:
        print("=== Übersicht ===")
        for o in sorted(overview, key=lambda x: x.get("n", 0), reverse=True):
            line = f"   {o['name'][:30]:30} {o.get('n', 0):>4} Kommentare"
            if o.get("n"):
                line += f" ({o.get('fb', 0)} FB / {o.get('ig', 0)} IG)"
            print(line)
        ov_path = TMP_DIR / "all_accounts_overview.json"
        ov_path.write_text(json.dumps(overview, ensure_ascii=False, indent=2))
        print(f"\n→ {ov_path.relative_to(PROJECT_ROOT)}")

    if not api_key and not args.no_analyze:
        print("\nHinweis: Kein ANTHROPIC_API_KEY in .env → Analyse übersprungen "
              "(Kommentare sind exportiert).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
