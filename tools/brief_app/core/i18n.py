"""Interface language for the app — English or German.

Two different languages live in this tool and they must not be confused:

  * the INTERFACE language (this module) — the labels, buttons and captions the team
    reads while working. Nothing here reaches a client.
  * the PLAN language (Customer.overlay_language) — the language of the on-image
    overlay text in the generated brief, which is a property of the brand and its
    marketplace, not of whoever happens to be operating the tool.

Keeping them separate means an English-speaking colleague can drive the tool for a
German amazon.de brand without silently turning that brand's overlays English.

The interface language is one app-wide setting rather than a per-user one: the team
works from a shared server and a shared screen share, and a per-session toggle would
mean two people describing different buttons to each other.

Default is English — the app was already almost entirely English, and English is the
common denominator across the team and the clients.
"""
from __future__ import annotations
import json
from pathlib import Path

from .config import DATA_ROOT

LANGUAGES = {"en": "English", "de": "Deutsch"}
DEFAULT_LANG = "en"

_SETTINGS_FILE = DATA_ROOT / "app_settings.json"


def get_ui_language() -> str:
    try:
        lang = json.loads(_SETTINGS_FILE.read_text(encoding="utf-8")).get("ui_language")
    except Exception:
        return DEFAULT_LANG                      # unreadable or absent: never break the UI
    return lang if lang in LANGUAGES else DEFAULT_LANG


def set_ui_language(lang: str) -> None:
    if lang not in LANGUAGES:
        return
    try:
        data = json.loads(_SETTINGS_FILE.read_text(encoding="utf-8"))
    except Exception:
        data = {}
    data["ui_language"] = lang
    _SETTINGS_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


# ---------------------------------------------------------------- strings
# Only strings that actually differ between the two languages live here. The rest of
# the UI is English literal text in app.py and reads identically in both modes.
STRINGS: dict[str, dict[str, str]] = {
    # --- About Us prompt (Generate page) ---
    "about.missing_title": {
        "en": "📖 {brand} has no About-Us text yet",
        "de": "📖 Über-uns-Seite von {brand} fehlt",
    },
    "about.why": {
        "en": ("Paste it once and it applies to every future plan for this brand. Without it "
               "the AI may **not** invent a brand story, a founding year or a credential — "
               "which leaves the A+ modules paler than they need to be."),
        "de": ("Einmal einfügen, gilt für alle künftigen Pläne dieser Marke. Ohne diesen Text "
               "darf die KI **keine** Markengeschichte, kein Gründungsjahr und kein Credential "
               "erfinden — die A+ Module bleiben dann blasser als nötig."),
    },
    "about.field": {
        "en": "Paste the text from the About-Us page",
        "de": "Text von der Über-uns-Seite einfügen",
    },
    "about.placeholder": {
        "en": ("From {source} → About us.\n"
               "Who founded the brand, why, what it stands for, and which credentials exist "
               "(master workshop, since 1912, midwife, hospice social worker, family business …)."),
        "de": ("Von {source} → Über uns / About us.\n"
               "Wer hat die Marke gegründet, warum, wofür steht sie, welche Credentials gibt es "
               "(Meisterbetrieb, seit 1912, Hebamme, Hospiz-Sozialarbeiterin, Familienbetrieb …)."),
    },
    "about.website_fallback": {"en": "the website", "de": "der Website"},
    "about.save": {"en": "💾 Save", "de": "💾 Speichern"},
    "about.saved": {
        "en": "Saved. It now feeds into every plan for this brand.",
        "de": "Gespeichert. Fließt ab sofort in jeden Plan dieser Marke ein.",
    },
    "about.empty": {"en": "Paste the text first.", "de": "Erst Text einfügen."},
    "about.skip": {
        "en": "Or skip it — the plan still builds, just without the brand story.",
        "de": "Oder überspringen — der Plan wird trotzdem gebaut, nur ohne Markengeschichte.",
    },
    # --- Variants block (Generate page) ---
    "variants.found_title": {
        "en": "🧬 {n} variants found in this sheet",
        "de": "🧬 {n} Varianten in diesem Sheet gefunden",
    },
    "variants.each_tab": {
        "en": "Every SEO tab is its own child listing and gets its own plan. ",
        "de": "Jedes SEO-Tab ist ein eigenes Kind-Listing und bekommt einen eigenen Plan. ",
    },
    "variants.tab_help": {"en": "Excel tab: {tab}", "de": "Excel-Tab: {tab}"},
    "variants.unreadable": {
        "en": "SEO tab '{tab}' could not be read: {error}",
        "de": "SEO-Tab '{tab}' nicht lesbar: {error}",
    },
    "variants.done_where": {
        "en": "All of them under **Plans & Review** at {brand}.",
        "de": "Alle unter **Plans & Review** bei {brand}.",
    },
    "variants.pick": {
        "en": "Pick what to build — each variant costs a full run.",
        "de": "Auswählen, was gebaut werden soll — jede Variante kostet einen vollen Lauf.",
    },
    "variants.selected": {"en": "{n} of {total} selected.", "de": "{n} von {total} ausgewählt."},
    "variants.button": {"en": "🧬 Build {n} variant plans", "de": "🧬 {n} Varianten-Pläne bauen"},
    "variants.failed": {
        "en": "Build failed for '{label}': {error}",
        "de": "Bauen fehlgeschlagen für '{label}': {error}",
    },
    "variants.done": {
        "en": "✅ Built {n} variant plans. ",
        "de": "✅ {n} Varianten-Pläne gebaut. ",
    },
    # --- Version labels (Plans & Review) ---
    "version.latest": {"en": "  ·  🟢 current version", "de": "  ·  🟢 aktuellste Version"},
    "version.older": {"en": "  ·  ⚪️ older version", "de": "  ·  ⚪️ ältere Version"},
    "version.flag_latest": {"en": "🟢 CURRENT", "de": "🟢 AKTUELL"},
    "version.flag_old": {"en": "⚪️ old", "de": "⚪️ alt"},
    # --- Seeding + backup (Customers page) ---
    "seed.new": {
        "en": "🆕 Added by the latest deploy: ",
        "de": "🆕 Neu mit dem letzten Deploy dazugekommen: ",
    },
    "backup.title": {"en": "💾 Backup — download everything",
                     "de": "💾 Backup — alles herunterladen"},
    "backup.why": {
        "en": ("Brands, plans, brand memory and comments live only on the server. They are "
               "**not** in Git. Download everything as a ZIP here and keep it somewhere that "
               "is not this same server — otherwise losing the server loses all of it."),
        "de": ("Marken, Pläne, Brand Memory und Kommentare liegen nur auf dem Server. Sie sind "
               "**nicht** im Git. Lade hier alles als ZIP herunter und lege es irgendwo ab, das "
               "nicht derselbe Server ist — sonst ist bei einem Serververlust alles weg."),
    },
    "backup.make": {"en": "Create ZIP", "de": "ZIP erzeugen"},
    "backup.packing": {"en": "Packing…", "de": "Packe…"},
    # --- Plans & Review ---
    "version.not_latest": {
        "en": ("This is **not** the current version of this plan (v{v} of {total}). "
               "Comments belong on the newest one."),
        "de": ("Das ist **nicht** die aktuellste Version dieses Plans (v{v} von {total}). "
               "Kommentare gehören an die neueste."),
    },
    # --- Review statuses ---
    "status.open": {"en": "Freshly generated, nobody has looked at it yet.",
                    "de": "Neu generiert, noch niemand dran."},
    "status.changes requested": {"en": "Comments are in, the plan needs a revision.",
                                 "de": "Kommentare da, Plan muss überarbeitet werden."},
    "status.design done": {"en": "Design team is finished, waiting for sign-off.",
                           "de": "Design-Team ist fertig, wartet auf Freigabe."},
    "status.approved": {"en": "Signed off. Done.", "de": "Freigegeben. Fertig."},
    # --- Sidebar ---
    "sidebar.language": {"en": "Interface language", "de": "Sprache der Oberfläche"},
}


def t(key: str, lang: str | None = None, **kw) -> str:
    """Translate `key`, falling back to English and then to the key itself.

    A missing key returns the key rather than raising: a typo in a label must never
    take the page down mid-render."""
    if lang is None:
        lang = get_ui_language()
    entry = STRINGS.get(key)
    if not entry:
        return key
    text = entry.get(lang) or entry.get("en") or key
    try:
        return text.format(**kw) if kw else text
    except (KeyError, IndexError):
        return text
