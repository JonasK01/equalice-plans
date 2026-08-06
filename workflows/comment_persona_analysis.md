# Workflow: Kommentar-basierte Buyer-Persona

## Objective
Aus Social-Media-Kommentaren auf Ads (und ggf. organischen Posts) einer Marke eine
datenbasierte Buyer-Persona ableiten: Wünsche, Pain-Points, Einwände, Sprache/O-Töne,
Kaufmotive, FAQ und Content-/Ad-Angles.

## Required Inputs
- **Ad-Account-ID** (z.B. `act_2088057028161457`)
- Gültiger Meta-Token in `.env` (`META_LONG_TOKEN`)
- `slug` + `brand` für die Output-Dateien
- Optional: `ANTHROPIC_API_KEY` in `.env` für automatische Analyse

## Tool
`tools/meta_comments.py` — siehe Aufrufe unten.

## Vorgehen
1. **Erreichbarkeit prüfen:** Token-Scopes mit `tools/meta_list_ad_accounts.py` / Graph-API
   checken. Für Kommentare gilt:
   - **IG-Ad-Kommentare** funktionieren mit Standard-Scopes (`pages_show_list`,
     `pages_read_engagement`) über `effective_instagram_media_id`.
   - **FB-Kommentare** (Ad-Posts + organisch) brauchen `pages_read_user_content`
     **+ App Review** — sonst Fehler `#10`.
   - **Organisches IG-Media-Listing** (`/{ig_id}/media`) braucht effektive
     Instagram-Permissions (App Review) — sonst Fehler `#10`.
2. **Kommentare ziehen (Export-only):**
   ```
   .venv/bin/python tools/meta_comments.py \
     --account <ACT_ID> --slug <slug> --brand "<Brand>" \
     --ad-status all --no-facebook --no-organic --no-analyze
   ```
   `--ad-status all` = alle Ads inkl. pausiert (mehr IG-Reichweite).
   `--no-facebook` = überspringt die #10-gesperrten FB-Calls (kein Rauschen).
   Output: `.tmp/<slug>_comments.{json,csv}`.
3. **Analyse:**
   - Mit `ANTHROPIC_API_KEY`: Flag `--no-analyze` weglassen → Tool erzeugt
     `.tmp/<slug>_persona.md` (Modell `claude-opus-4-8`, strukturierter Output).
   - Ohne Key: Kommentare exportieren, Agent wertet `.tmp/<slug>_comments.json` manuell aus.
4. **Deliverable:** Persona in Cloud (Google Doc/Sheet) ablegen oder direkt an den User.

## Gelernte Stolpersteine
- **Page-Token nötig:** Kommentare brauchen einen Page-Access-Token (User-Token →
  Fehler „Page access token is required"). Tool holt ihn automatisch via `/me/accounts`.
- **Verschluckte Fehler vermeiden:** Permission-Fehler `#10` NICHT als „0 Kommentare"
  interpretieren — das Tool zählt fehlerhafte Quellen separat.
- **IG-Usernames** kommen aktuell leer zurück (Feld `username` ohne
  `instagram_manage_comments` nicht befüllt) — Texte sind davon nicht betroffen.
- **Ad-Kommentare sind fan-lastig:** für ein vollständiges Bild (Preis-/Lieferkritik,
  breitere Skepsis) sind die **Facebook-Kommentare** wichtig → App Review priorisieren.

## Token-Schutz
`MAX_COMMENTS_FOR_ANALYSIS` in `tools/meta_comments.py` begrenzt die an Claude
gesendete Menge (Default 1500); bei Überschreitung meldet das Tool, wie viele
nicht ausgewertet wurden.
