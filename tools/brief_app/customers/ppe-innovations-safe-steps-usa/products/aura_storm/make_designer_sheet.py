"""Aura Storm — designer handoff sheet.

One page per tile. The on-image copy is set large in a tinted box because that is the
thing the designer typesets; everything else on the page is instruction, set small and
out of the way. Deliberately not the full brief format — this is the sheet that sits next
to the artboard.
"""
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, white
from reportlab.pdfgen import canvas as _canvas

OUT = Path(__file__).resolve().parent / "Aura_Storm_Image_Plan_Designer.pdf"

BLUE   = HexColor("#0A5BD3")
INK    = HexColor("#0B1520")
SOFT   = HexColor("#33475A")
MUTED  = HexColor("#7A8B9B")
PANEL  = HexColor("#EEF3F9")
LINE   = HexColor("#D3DDE7")
WIN    = HexColor("#0F7B5A")
WARN   = HexColor("#A8531B")

W, H = A4
M = 1.9 * cm

TILES = [
    dict(
        n="01", role="MAIN HERO", arch="clean_hero", status="KEEP",
        overlay=None,
        sub="No text on the image. Amazon main-image policy.",
        layout=[
            "Unit on pure white, 85% or more of the frame.",
            "Ship THREE variants for the A/B test, identical lighting:",
            "   A — plain unit, nothing else",
            "   B — badge: 2,775 SQ FT",
            "   C — badge: 99.99% THIRD-PARTY CERTIFIED",
        ],
        why="Let the test decide which promise wins the click. Keep the winner.",
    ),
    dict(
        n="02", role="WHAT IT REMOVES", arch="icon_halo", status="NEW",
        overlay="REDUCES 99.99% OF PATHOGENS.",
        sub="Bacteria, viruses, mold, fungus. Third-party certified, 4-log, under 60 minutes.",
        layout=[
            "Unit centred, large. The 99.99% mark set against it.",
            "The verb is REDUCES. Never kills, never eliminates. See WHY below.",
            "Ten icon badges ringed around the unit, in TWO ARCS:",
            "",
            "   UPPER ARC — accent blue, tied to the number",
            "   bacteria  ·  viruses  ·  mold  ·  fungus",
            "",
            "   ——— hairline separator between the arcs ———",
            "",
            "   LOWER ARC — neutral grey, NO percentage anywhere near it",
            "   VOCs  ·  gases  ·  odors  ·  dust  ·  pollen  ·  smoke",
        ],
        why=("Two rules hold this tile together. First the verb: it is REDUCES, never kills and "
             "never eliminates. A device that claims to kill microorganisms is making a pesticidal "
             "claim in the US and needs an EPA registration to carry it — and the certified result "
             "is a 4-log reduction, which is a reduction, not a kill. Second the scope: the "
             "certificate covers microbial reduction only, not VOCs, odors or dust. One ring with "
             "one percentage would claim 99.99% for all ten, which is not what was tested. Two arcs "
             "keep the strongest number in the category and stay exactly true."),
    ),
    dict(
        n="03", role="THE FILTER STACK", arch="exploded_kit", status="NEW",
        overlay="EIGHT STAGES. BOTH SIDES.",
        sub="H13+ HEPA, TiO2 cold catalyst, photocatalyst, UV-C lamp on each side.",
        layout=[
            "Exploded view of the unit, components floating apart in order.",
            "EVERY stage labelled by name with a thin leader line.",
            "Airflow arrows entering from BOTH sides — this is the dual-sided proof.",
            "Name at minimum: pre-filter · H13+ medical-grade HEPA ·",
            "TiO2 cold catalyst · photocatalyst · UV-C lamp (one each side).",
        ],
        why=("We print '8-STAGE' three times across the listing and never show a single stage. "
             "Austin shows a full cutaway, Winix explodes all four of theirs. A number without "
             "a picture is a claim; a labelled diagram is proof."),
    ),
    dict(
        n="04", role="THE PROOF", arch="stat_block", status="REVISED",
        overlay="99.99% REDUCTION, CERTIFIED.",
        sub="4-log against airborne pathogens, in under 60 minutes.",
        layout=[
            "99.99% set VERY large, in the top two thirds.",
            "DIRECTLY BENEATH IT, black, large enough to read as part of the headline:",
            "   REDUCTION, CERTIFIED.",
            "The number never stands without a noun AND a verb. See WHY below.",
            "",
            "One quiet line under the headline:",
            "   4-log reduction  ·  under 60 minutes  ·  third-party certified",
            "",
            "Data strip along the foot, right column:",
            "   0.01 microns  ·  CADR 320  ·  370 CFM",
            "Do NOT also write 0.01 microns in the subline. The strip carries it once.",
            "",
            "Unit large on the left. No badge on it.",
        ],
        why=("REVISED TWICE. The first version read '99.99% UNDER 60 MINUTES' and never said 99.99% "
             "of WHAT — a percentage with no object is decoration, not a claim, and it invites the "
             "wrong reading: 99.99% of the air, of all particles, of the whole room. The second "
             "version named pathogens but had no verb. A complete claim needs all three: how much, "
             "of what, and what happens to it. Tile 2 opens with the claim, this one proves it — "
             "certifier, log value, time window, particle size."),
    ),
    dict(
        n="05", role="SENSORS", arch="split_icon_panel", status="MERGED",
        overlay="IT MEASURES. IT ADJUSTS.",
        sub="Particulate and VOC sensors set the fan speed on their own.",
        layout=[
            "LEFT HALF — the unit in a real room, in use.",
            "RIGHT HALF — flat colour panel holding three icons with short labels:",
            "   particulate sensor  ·  VOC sensor  ·  automatic fan speed",
            "The panel gives the text a clean home instead of floating it over the photo.",
        ],
        why=("Replaces both 'YOUR AIR. REVEALED.' and 'SEE THE AIR. KNOW IT'S CLEAN.' — they "
             "are the same idea twice. Merging them frees the slot that pays for the filter "
             "diagram."),
    ),
    dict(
        n="06", role="QUIET", arch="comparison_columns", status="KEEP",
        overlay="QUIETER THAN A LIBRARY.",
        sub="29 dB on low. 370 CFM when the room needs it.",
        layout=[
            "Unchanged from the current tile — it already works.",
            "29 dB set large, with the comparison scale beside it:",
            "   40 library  ·  50 conversation  ·  65 busy street",
            "Occupied room, low light, unit present but not posed.",
        ],
        why=("The best tile in the current set. It turns an abstract number into something the "
             "buyer can hear. Every spec on this listing should be treated the way this one "
             "already is."),
    ),
    dict(
        n="07", role="BRAND CLOSE", arch="brand_close", status="KEEP",
        overlay="CLEANER AIR. SAFER SPACES.",
        sub="2,775 sq ft. Hospitals, schools, gyms, offices. U.S.-based manufacturer.",
        layout=[
            "Safe Steps wordmark in the top third.",
            "Unit centred beneath it.",
            "Lower band split into three equal cells by hairline rules:",
            "   environments  ·  2,775 sq ft  ·  independently lab tested",
        ],
        why="Close on the things no competitor on this page can match.",
    ),
]


def _wrap(c, text, x, y, width, leading, font, size, colour):
    """Draw wrapped text, return the y after the last line."""
    c.setFont(font, size)
    c.setFillColor(colour)
    words, line = text.split(), ""
    for w in words:
        trial = (line + " " + w).strip()
        if c.stringWidth(trial, font, size) <= width:
            line = trial
        else:
            c.drawString(x, y, line)
            y -= leading
            line = w
    if line:
        c.drawString(x, y, line)
        y -= leading
    return y


def cover(c):
    c.setFillColor(INK)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    y = H - 5.2 * cm
    c.setFillColor(HexColor("#7FA9EE"))
    c.setFont("Helvetica-Bold", 9)
    c.drawString(M, y, "S A F E   S T E P S   ·   A M A Z O N   L I S T I N G   C R E A T I V E")

    y -= 1.5 * cm
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 40)
    c.drawString(M, y, "Aura Storm")
    y -= 1.25 * cm
    c.drawString(M, y, "Image Plan")

    y -= 1.6 * cm
    c.setFillColor(BLUE)
    c.rect(M, y, 4.2 * cm, 3, fill=1, stroke=0)

    y -= 1.5 * cm
    y = _wrap(c, "They filter. We filter, then inactivate — and we hold the certificate.",
              M, y, W - 2 * M - 3 * cm, 0.78 * cm, "Helvetica-Bold", 17, white)

    y -= 0.5 * cm
    y = _wrap(c, "Not one competitor states a certified kill rate. We have 99.99%, 4-log, in "
                 "under 60 minutes, verified by a third party. That single fact carries the "
                 "whole plan.",
              M, y, W - 2 * M - 2.5 * cm, 0.6 * cm, "Helvetica", 11.5, HexColor("#A8BACA"))

    # the seven overlays at a glance
    y -= 1.3 * cm
    c.setFillColor(HexColor("#7FA9EE"))
    c.setFont("Helvetica-Bold", 8.5)
    c.drawString(M, y, "T H E   S E V E N   T I L E S")
    y -= 0.85 * cm
    for t in TILES:
        c.setFillColor(HexColor("#5A6B7C"))
        c.setFont("Helvetica-Bold", 10)
        c.drawString(M, y, t["n"])
        c.setFillColor(white)
        c.setFont("Helvetica-Bold", 11)
        c.drawString(M + 1.15 * cm, y, t["overlay"] or "(no on-image text)")
        c.setFillColor(HexColor("#7A8B9B"))
        c.setFont("Helvetica", 8.5)
        c.drawRightString(W - M, y, t["status"])
        y -= 0.72 * cm

    c.setFillColor(HexColor("#5A6B7C"))
    c.setFont("Helvetica", 8)
    c.drawString(M, 1.6 * cm, "Prepared by EQUALICE   ·   Aura Storm, Safe Steps by PPE Innovations LLC")
    c.showPage()


def tile_page(c, t):
    # header band
    c.setFillColor(PANEL)
    c.rect(0, H - 3.6 * cm, W, 3.6 * cm, fill=1, stroke=0)
    c.setFillColor(BLUE)
    c.rect(0, H - 3.6 * cm, 0.32 * cm, 3.6 * cm, fill=1, stroke=0)

    c.setFillColor(BLUE)
    c.setFont("Helvetica-Bold", 30)
    c.drawString(M, H - 2.5 * cm, t["n"])

    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 15)
    c.drawString(M + 1.85 * cm, H - 2.35 * cm, t["role"])
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 9)
    c.drawString(M + 1.85 * cm, H - 3.0 * cm, f"layout: {t['arch']}")

    badge = t["status"]
    bw = c.stringWidth(badge, "Helvetica-Bold", 8.5) + 0.7 * cm
    c.setFillColor(WIN if badge == "KEEP" else BLUE)
    c.roundRect(W - M - bw, H - 2.55 * cm, bw, 0.62 * cm, 2, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 8.5)
    c.drawCentredString(W - M - bw / 2, H - 2.36 * cm, badge)

    y = H - 5.0 * cm

    # ---- ON-IMAGE TEXT — the thing the designer sets ----
    c.setFillColor(MUTED)
    c.setFont("Helvetica-Bold", 8.5)
    c.drawString(M, y, "O N - I M A G E   T E X T")
    y -= 0.35 * cm

    box_top = y
    inner_w = W - 2 * M - 1.6 * cm
    # measure
    tmp_y = box_top - 1.15 * cm
    if t["overlay"]:
        tmp_y = _wrap(c, t["overlay"], M + 0.8 * cm, tmp_y, inner_w, 0.85 * cm, "Helvetica-Bold", 20, white)
        tmp_y -= 0.15 * cm
    tmp_y = _wrap(c, t["sub"], M + 0.8 * cm, tmp_y, inner_w, 0.52 * cm, "Helvetica", 11,
                  white if t["overlay"] else MUTED)
    box_h = box_top - tmp_y + 0.8 * cm

    # draw box then text on top
    c.setFillColor(INK if t["overlay"] else PANEL)
    c.rect(M, box_top - box_h, W - 2 * M, box_h, fill=1, stroke=0)
    c.setFillColor(BLUE)
    c.rect(M, box_top - box_h, 0.22 * cm, box_h, fill=1, stroke=0)

    yy = box_top - 1.15 * cm
    if t["overlay"]:
        yy = _wrap(c, t["overlay"], M + 0.8 * cm, yy, inner_w, 0.85 * cm, "Helvetica-Bold", 20, white)
        yy -= 0.15 * cm
        _wrap(c, t["sub"], M + 0.8 * cm, yy, inner_w, 0.52 * cm, "Helvetica", 11, HexColor("#A8BACA"))
    else:
        _wrap(c, t["sub"], M + 0.8 * cm, yy, inner_w, 0.52 * cm, "Helvetica-Oblique", 11, SOFT)

    y = box_top - box_h - 1.15 * cm

    # ---- LAYOUT ----
    c.setFillColor(MUTED)
    c.setFont("Helvetica-Bold", 8.5)
    c.drawString(M, y, "L A Y O U T")
    y -= 0.6 * cm
    for line in t["layout"]:
        if not line.strip():
            y -= 0.28 * cm
            continue
        indented = line.startswith("   ")
        txt = line.strip()
        if indented:
            y = _wrap(c, txt, M + 0.9 * cm, y, W - 2 * M - 0.9 * cm, 0.52 * cm,
                      "Helvetica-Bold", 10.5, BLUE)
        else:
            c.setFillColor(LINE)
            c.circle(M + 0.12 * cm, y + 0.12 * cm, 0.07 * cm, fill=1, stroke=0)
            y = _wrap(c, txt, M + 0.55 * cm, y, W - 2 * M - 0.55 * cm, 0.52 * cm,
                      "Helvetica", 10.5, SOFT)
        y -= 0.08 * cm

    # ---- WHY ----
    y -= 0.7 * cm
    c.setStrokeColor(LINE)
    c.setLineWidth(0.6)
    c.line(M, y, W - M, y)
    y -= 0.75 * cm
    c.setFillColor(MUTED)
    c.setFont("Helvetica-Bold", 8.5)
    c.drawString(M, y, "W H Y")
    y -= 0.55 * cm
    _wrap(c, t["why"], M, y, W - 2 * M, 0.5 * cm, "Helvetica", 10, MUTED)

    c.setFillColor(LINE)
    c.setFont("Helvetica", 8)
    c.drawRightString(W - M, 1.4 * cm, f"Aura Storm image plan  ·  tile {t['n']} of 07")
    c.showPage()


def closing(c):
    y = H - M - 0.5 * cm
    c.setFillColor(BLUE)
    c.setFont("Helvetica-Bold", 8.5)
    c.drawString(M, y, "A +   P R E M I U M")
    y -= 1.0 * cm

    aplus = [
        ("01", "BANNER", "Brand hero. Cleaner air, safer spaces."),
        ("02", "SLIDER", "Five strongest specs as scan tiles."),
        ("03", "BANNER", "The eight stages, dual-sided. The diagram, full width."),
        ("04", "SLIDER", "Environments: clinic, school, gym, office, senior care."),
        ("05", "BANNER", "The proof: 99.99%, 4-log, under 60 minutes, certified."),
        ("06", "BANNER", "Safe Steps close, handing the reader into the Q&A."),
        ("07", "Q&A", "Five pairs. Question max 80 characters, answer max 120."),
    ]
    for n, kind, txt in aplus:
        c.setFillColor(MUTED); c.setFont("Helvetica", 9); c.drawString(M, y, n)
        c.setFillColor(BLUE); c.setFont("Helvetica-Bold", 8.5); c.drawString(M + 1.0 * cm, y, kind)
        c.setFillColor(SOFT); c.setFont("Helvetica", 10.5); c.drawString(M + 3.4 * cm, y, txt)
        y -= 0.52 * cm
        c.setStrokeColor(LINE); c.setLineWidth(0.5); c.line(M, y + 0.2 * cm, W - M, y + 0.2 * cm)
        y -= 0.28 * cm

    y -= 1.1 * cm
    c.setFillColor(WARN)
    c.setFont("Helvetica-Bold", 8.5)
    c.drawString(M, y, "B E F O R E   Y O U   B U I L D")
    y -= 0.9 * cm

    flags = [
        ("Do not write \"sterilization\" against the 4-log result",
         "Sterilization means complete destruction; the accepted standard is 6-log. A 4-log "
         "result is 99.99% — a reduction, which is disinfection. Every tile says reduction and "
         "pairs it with third-party certified. Product and partner names stay as they are."),
        ("No SARS-CoV-2 or COVID-19 anywhere",
         "Nothing about either goes on a tile until the registration behind that claim is "
         "confirmed. Virus-kill claims for devices sit in EPA territory in the US, and Amazon "
         "removes listings in this category aggressively."),
    ]
    for title, body in flags:
        c.setFillColor(PANEL)
        c.rect(M, y - 2.5 * cm, W - 2 * M, 2.75 * cm, fill=1, stroke=0)
        c.setFillColor(WARN)
        c.rect(M, y - 2.5 * cm, 0.22 * cm, 2.75 * cm, fill=1, stroke=0)
        yy = y - 0.15 * cm
        yy = _wrap(c, title, M + 0.8 * cm, yy, W - 2 * M - 1.6 * cm, 0.55 * cm,
                   "Helvetica-Bold", 11.5, INK)
        yy -= 0.1 * cm
        _wrap(c, body, M + 0.8 * cm, yy, W - 2 * M - 1.6 * cm, 0.45 * cm, "Helvetica", 9.5, SOFT)
        y -= 3.3 * cm

    c.setFillColor(MUTED)
    c.setFont("Helvetica", 8)
    c.drawString(M, 1.4 * cm, "Prepared by EQUALICE   ·   questions: jk@equalice-academy.com")
    c.showPage()


def main():
    c = _canvas.Canvas(str(OUT), pagesize=A4)
    c.setTitle("Aura Storm — Image Plan (Designer Sheet)")
    cover(c)
    for t in TILES:
        tile_page(c, t)
    closing(c)
    c.save()
    print("Built:", OUT)


if __name__ == "__main__":
    main()
