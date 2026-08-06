"""Ultra PRO — Platinum Series 3-Pocket Binder Sleeves (100 pack)  [Listing 73]

WICHTIG (Datenlage): Der Ordner/ASIN sagte ursprünglich B000ETN37E (1-Pocket 8x10),
die im Ordner liegende SEO/A+-Datei gehört aber zum Produkt B00156X6BI —
'Platinum Series 3-Pocket Binder Sleeves, 100 Pack, 3-1/2" x 7-1/2" Pockets'.
Entscheidung (mit Freigabe von Jonas): Plan an der REALEN SEO-Datei ausrichten und
nach der passenden ASIN B00156X6BI benennen. Bildregie ist auf das 3-Pocket-Produkt
umgeschrieben; Titel/Bullets/Backend/Q&A/Vergleich kommen 1:1 aus den Sheets.

Marketplace: amazon.com (US). Ultra-PRO-Katalogstil (schwarz/rot/weiss).
"""
from __future__ import annotations
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(HERE.parents[1]))

from tools.brief_app.core.customers import load_customer
from tools.brief_app.core.excel_parser import parse_excel
from tools.brief_app.core.pdf_builder import BriefBuilder
from tools.brief_app.core.ai import AIImagePlanItem, AIModule
import seo_loader as SEOL

PLAN_NO = "73"
ASIN = "B00156X6BI"   # entspricht dem Inhalt der SEO/A+-Datei (nicht B000ETN37E)
EXCEL = HERE / "listing.xlsx"
APLUS = HERE / "aplus.xlsx"


IMAGES = [
    AIImagePlanItem(
        name="Image 1 — Main Hero (3 options for A/B testing)",
        role="hero",
        background="Clean white for slot-1; the CTR versions add a black lower band with a thin red top-line (Ultra PRO catalog). Same framing across all 3.",
        purpose="Win the click among look-alike binder pages. Ship all 3, keep the winner.",
        visual=(
            "Mock ALL 3 options. Product exactly as real: a clear 3-pocket binder page (three "
            "vertical 3-1/2\" x 7-1/2\" pockets) holding collectibles — a ticket, a banknote, a "
            "photo — plus the 100-pack behind it. ONE callout each.\n\n"
            "OPTION A — POCKET LAYOUT: page with three filled pockets. Badge (red): '3 POCKETS PER PAGE'.\n"
            "OPTION B — PACK VALUE: the 100-pack stack. Badge (red): '100 PAGES'.\n"
            "OPTION C — ARCHIVAL: page + acid-free / no-PVC icons. Badge: 'ARCHIVAL · NON-PVC'.\n\n"
            "Across all 3: white background, red badge ~6% of frame, same lighting."
        ),
        overlay="(one callout per option)",
        overlay_sub="3 hero options shipped — A/B test, keep the winner.",
        props=["A: 3-pocket page with ticket/banknote/photo", "B: 100-pack stack", "C: page + acid-free/no-PVC icons"],
        lighting="Bright, even studio light; crisp catch-light so the clear film reads on white.",
        why_it_works=(
            "Three triggers: the useful 3-pocket layout, pack value (100), archival safety. One "
            "callout each — readable at thumbnail size."
        ),
    ),
    AIImagePlanItem(
        name="Image 2 — Hook: three 3-1/2\" x 7-1/2\" pockets per page",
        role="hook",
        background="Black with a thin red top-line and bold white headline (Ultra PRO catalog)",
        purpose="Show the pocket format and what it is really made to hold.",
        visual=(
            "Large macro of one page: three vertical pockets, each holding a different keepsake — "
            "a concert ticket, a banknote, a trading card. Thin red callout lines: '3 pockets per "
            "page', '3-1/2\" x 7-1/2\" each', 'both-sides viewing'. White bold headline: 'A PLACE "
            "FOR EVERY KEEPSAKE.'"
        ),
        overlay="3 POCKETS PER PAGE.",
        overlay_sub="Three 3-1/2\" x 7-1/2\" pockets for tickets, currency, photos & cards.",
        props=["3-pocket page macro", "ticket / banknote / card in pockets", "red callout lines"],
        lighting="Dramatic catalog light on black; strong edge-light on the clear film.",
        why_it_works=(
            "The 3-pocket, tall-pocket format is the differentiator — showing real tickets and "
            "currency communicates the use-case instantly, beyond just trading cards."
        ),
    ),
    AIImagePlanItem(
        name="Image 3 — Educate: archival-safe, non-PVC & acid-free",
        role="educate",
        background="White with a black/red Ultra PRO footer band",
        purpose="Defend quality: safe long-term storage for valuables and memorabilia.",
        visual=(
            "Split card. LEFT: a filled page, shield icon 'ARCHIVAL-SAFE'. RIGHT: three feature "
            "rows with red check-icons — 'NON-PVC polypropylene', 'ACID-FREE film', 'Clear "
            "both-sides viewing'. Footer band: 'Protecting collections since 1952.'"
        ),
        overlay="ARCHIVAL. NON-PVC.",
        overlay_sub="Acid-free, non-PVC polypropylene for safe long-term storage.",
        props=["filled page", "3 feature rows with red checks", "since-1952 footer band"],
        lighting="Flat, even catalog light; feature icons legible at thumbnail size.",
        why_it_works=(
            "Collectors of currency, tickets and photos care about archival safety. Naming "
            "non-PVC + acid-free with a clear benefit separates this from bargain pages."
        ),
    ),
    AIImagePlanItem(
        name="Image 4 — Fit: 3-ring album compatible",
        role="desire",
        background="White with a red callout (Ultra PRO)",
        purpose="Remove the fit question — does it go in my binder?",
        visual=(
            "A page being placed into an open 3-ring album, the 3-hole punched spine highlighted. "
            "Callout: 'Fits standard 3-ring albums & binders'. Note: 'Add pages as your collection "
            "grows.'"
        ),
        overlay="FITS 3-RING ALBUMS.",
        overlay_sub="3-hole punched spine drops into any standard 3-ring binder system.",
        props=["page into 3-ring album", "3-hole spine highlight", "red callout"],
        lighting="Bright, even; the spine detail must read clearly.",
        why_it_works=(
            "Binder compatibility is the top pre-purchase question for pages. Showing the 3-hole "
            "spine in a real album sets honest expectations."
        ),
    ),
    AIImagePlanItem(
        name="Image 5 — Use: what fits inside",
        role="desire",
        background="Black with red accents (Ultra PRO catalog)",
        purpose="Make the versatility and 100-count value obvious.",
        visual=(
            "A binder open to several filled pages, with icon-stats: '100 PAGES', 'Tickets & "
            "stubs', 'Currency & notes', 'Photos & documents', 'Cards & memorabilia'. Clean "
            "catalog layout."
        ),
        overlay="TICKETS. CURRENCY. PHOTOS.",
        overlay_sub="Organize keepsakes, memorabilia and documents — 100 pages per box.",
        props=["binder with filled pages", "5 icon-stats", "assorted keepsakes"],
        lighting="Catalog light on black; product and stats clearly separated.",
        why_it_works=(
            "Shows the pages are a flexible keepsake system, not just card storage — widening the "
            "buyer base to collectors of tickets, currency and photos."
        ),
    ),
    AIImagePlanItem(
        name="Image 6 — Trust: Ultra PRO, trusted since 1952",
        role="trust",
        background="Black with red top-line, white headline (brand close)",
        purpose="Close on brand authority — the collector's default choice.",
        visual=(
            "Hero of the pack with a small lifestyle inset (a collector filing pages into an album "
            "at a tidy desk). Brand line: 'ULTRA PRO — protecting collections since 1952 · trusted "
            "by collectors worldwide'. Red badge: 'SINCE 1952'."
        ),
        overlay="TRUSTED SINCE 1952.",
        overlay_sub="Ultra PRO — protecting collections and keepsakes worldwide.",
        props=["pack hero", "collector lifestyle inset", "since-1952 red badge"],
        lighting="Premium catalog light on black; warm inset for the lifestyle moment.",
        why_it_works=(
            "Against unbranded pages, heritage and trust are the deciding signals. 'Since 1952' is "
            "Ultra PRO's honest, compliant authority claim."
        ),
    ),
    AIImagePlanItem(
        name="Image 7 — Range: the Ultra PRO Platinum storage system",
        role="close",
        background="White with black/red Ultra PRO chrome",
        purpose="Cross-sell the wider Platinum page & album range.",
        visual=(
            "Clean line-up: the 3-pocket page (this product) alongside other Platinum pocket "
            "configurations and a 3-ring album — a coordinated system. Small labels; this page "
            "gently highlighted. Caption: 'Build your collection — the Ultra PRO way.'"
        ),
        overlay="BUILD YOUR COLLECTION.",
        overlay_sub="Pair with Ultra PRO Platinum pages and 3-ring albums.",
        props=["3-pocket page (highlighted)", "other Platinum pages", "3-ring album"],
        lighting="Bright, even; coordinated family shot.",
        why_it_works=(
            "Turns one purchase into a system sale and reinforces Ultra PRO as the one-stop "
            "collector brand."
        ),
    ),
]


CREATIVE_MODULES = [
    AIModule(
        name="Module 1 — Brand banner",
        role="a+_banner",
        headline="A PLACE FOR EVERY KEEPSAKE.",
        body=(
            "Ultra PRO Platinum 3-pocket binder sleeves keep tickets, currency, photos, documents "
            "and cards clearly organised in three 3-1/2\" x 7-1/2\" pockets per page. Non-PVC, "
            "acid-free and archival-safe — collectible storage trusted since 1952."
        ),
        visual="Wide black banner, red top-line, bold white headline left; a filled 3-pocket page right. Ultra PRO logo upper-left.",
        alt="Ultra PRO Platinum 3-pocket binder sleeves banner: three pockets per page, non-PVC, since 1952.",
    ),
    AIModule(
        name="Module 2 — Carousel (5 tiles): Why these pages",
        role="a+_carousel",
        headline="WHY ULTRA PRO PLATINUM PAGES",
        body=(
            "Tile 1: <b>3 POCKETS PER PAGE</b> — Three 3-1/2\" x 7-1/2\" pockets.<br/>"
            "Tile 2: <b>NON-PVC &amp; ACID-FREE</b> — Archival-safe for the long term.<br/>"
            "Tile 3: <b>BOTH-SIDES VIEWING</b> — Clear polypropylene film.<br/>"
            "Tile 4: <b>3-RING COMPATIBLE</b> — 3-hole spine fits standard albums.<br/>"
            "Tile 5: <b>100 PAGES</b> — For growing collections."
        ),
        visual="5 square tiles, red accent corner each, black/white icons (3-pocket grid · shield · eye · 3-ring · stack).",
        alt="Five A+ tiles: 3 pockets, non-PVC/acid-free, both-sides viewing, 3-ring compatible, 100 pages.",
    ),
    AIModule(
        name="Module 3 — Banner: What fits inside",
        role="a+_banner",
        headline="TICKETS. CURRENCY. PHOTOS. CARDS.",
        body=(
            "The tall 3-1/2\" x 7-1/2\" pockets are made for more than cards — organise concert "
            "tickets and stubs, banknotes and currency, photos, documents and memorabilia, all "
            "clearly visible from both sides and safely stored in your binder."
        ),
        visual="Banner split: a filled page (ticket / banknote / photo) left; a binder of pages right. Black/red Ultra PRO styling.",
        alt="A+ banner showing tickets, currency, photos and cards stored in the 3-pocket pages.",
    ),
    AIModule(
        name="Module 4 — Carousel (4 tiles): The Platinum storage system",
        role="a+_carousel",
        headline="BUILD YOUR COLLECTION",
        body=(
            "Tile 1: <b>3-POCKET PAGES</b> — Tall pockets for keepsakes (this product).<br/>"
            "Tile 2: <b>POCKET PAGES</b> — More Platinum configurations for cards.<br/>"
            "Tile 3: <b>3-RING ALBUMS</b> — Store and display full collections.<br/>"
            "Tile 4: <b>PROTECTIVE SLEEVES</b> — Add a layer for valuable items."
        ),
        visual="4 coordinated product tiles, red accent corners, consistent catalog styling.",
        alt="Four A+ tiles showing the Ultra PRO Platinum storage system: pages, albums, sleeves.",
    ),
]


def main() -> None:
    print(f"Lade Ultra PRO + SEO/A+ Sheets für Listing {PLAN_NO} (korrigiert auf {ASIN})…")
    cust = load_customer("ultra_pro")
    brief = parse_excel(EXCEL)
    seo = SEOL.load_seo(EXCEL)
    ap = SEOL.load_aplus(APLUS)
    OUT = HERE / f"{PLAN_NO}_{ASIN}_Image Plan.pdf"
    print(f"  SEO-Titel ({len(seo.title)} chars): {seo.title[:70]}…")
    print(f"  Bullets={len(seo.bullets)}  Q&A={len(ap.qa)}  Vergleich-Zeilen={len(ap.comp_rows)}")

    modules = list(CREATIVE_MODULES)
    if ap.qa:
        modules.append(SEOL.qa_module(ap, headline="COLLECTOR Q&A"))
    if ap.comp_rows:
        modules.append(SEOL.comparison_module(ap))

    builder = BriefBuilder(cust, brief, OUT, ai=None)
    builder._ai_title = seo.title
    builder._ai_bullets = SEOL.as_bullets_html(seo)
    builder._ai_images = IMAGES
    builder._ai_modules = modules
    builder._ai_qa = SEOL.as_qa(ap)
    builder._ai_backend = seo.backend
    builder.copy_source_label = "SEO-Sheet (Titel/Bullets/Backend) + A+ Sheet (Q&A/Vergleich); Bildregie hand-written"

    print("Baue Branded PDF…")
    pdf_path = builder.build()
    size_kb = pdf_path.stat().st_size // 1024
    import re
    pages = len(re.findall(rb'/Type\s*/Page[^s]', pdf_path.read_bytes()))
    print(f"Gebaut: {pdf_path}")
    print(f"  Seiten: {pages}  Größe: {size_kb} KB")


if __name__ == "__main__":
    main()
