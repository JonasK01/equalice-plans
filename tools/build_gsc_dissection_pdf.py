#!/usr/bin/env python3
"""GSC International — Dissection Kit 360-DS02-KT (B0F7MN3L5K)
Amazon.com Image Plan Brief — image-plan focused.
"""

import math
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, Color
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (
    Paragraph, Spacer, PageBreak, Table, TableStyle,
    KeepTogether, Frame, BaseDocTemplate, PageTemplate, NextPageTemplate,
)
from reportlab.platypus.flowables import Flowable

OUT = "/Users/jonask/Desktop/GSC_Dissection_Kit_Brief.pdf"

# ─── GSC palette ────────────────────────────────────────────────────
GSC_GREEN   = HexColor("#4A9B3F")
GSC_GREEN_D = HexColor("#2D6A28")
GSC_BLUE    = HexColor("#1D60AB")
GSC_BLUE_D  = HexColor("#0E3F75")
PAD_BLUE    = HexColor("#3060A0")     # dissection pad blue
PAN_SILVER  = HexColor("#C5C8CD")     # aluminum pan
STEEL       = HexColor("#A8B0BA")     # tool stainless steel
STEEL_D     = HexColor("#5A6678")
SPECIMEN_GR = HexColor("#7A9A5A")
WHITE       = HexColor("#FFFFFF")
OFFWHITE    = HexColor("#F7F9F4")
LIGHT_GRN   = HexColor("#E8F3E5")
LIGHT_BLU   = HexColor("#E5EEF8")
INK         = HexColor("#1A1A1A")
GREY        = HexColor("#6A6A6A")
GREY_L      = HexColor("#C0C0C0")
GREEN_OK    = HexColor("#3FA770")
RED_X       = HexColor("#D24545")
ACCENT_Y    = HexColor("#F5C518")

PAGE_W, PAGE_H = A4
ML, MR, MT, MB = 1.6*cm, 1.6*cm, 1.8*cm, 1.6*cm
CW = PAGE_W - ML - MR

styles = getSampleStyleSheet()
H1   = ParagraphStyle("H1", parent=styles["Title"],   fontName="Helvetica-Bold", fontSize=28, leading=32, textColor=GSC_GREEN_D, spaceAfter=4, alignment=TA_LEFT)
H2   = ParagraphStyle("H2", parent=styles["Heading2"],fontName="Helvetica-Bold", fontSize=18, leading=22, textColor=GSC_GREEN_D, spaceBefore=12, spaceAfter=6)
H3   = ParagraphStyle("H3", parent=styles["Heading3"],fontName="Helvetica-Bold", fontSize=11, leading=14, textColor=INK,         spaceBefore=10, spaceAfter=4)
BODY = ParagraphStyle("Body",parent=styles["Normal"], fontName="Helvetica",     fontSize=9.5, leading=13, textColor=INK,         spaceAfter=3)
SUB  = ParagraphStyle("SUB", parent=styles["Normal"], fontName="Helvetica",     fontSize=10, leading=13, textColor=GREY,         spaceAfter=10)
SMALL= ParagraphStyle("Small",parent=BODY, fontSize=8, leading=11, textColor=GREY)
QUOTE= ParagraphStyle("Quote",parent=BODY, fontName="Helvetica-Oblique", textColor=GREY)


# ─── Flowables ──────────────────────────────────────────────────────

class HRule(Flowable):
    def __init__(self, width=None, color=GSC_GREEN, thickness=1.4):
        self.width = width or CW; self.color = color; self.thickness = thickness
        Flowable.__init__(self)
    def wrap(self, *a): return (self.width, self.thickness + 6)
    def draw(self):
        self.canv.setStrokeColor(self.color); self.canv.setLineWidth(self.thickness)
        self.canv.line(0, 3, self.width, 3)


# ─── Drawing helpers ────────────────────────────────────────────────

def _draw_pan(c, cx, cy, w=4.0*cm, with_pad=True):
    """Aluminum dissection pan — top-down view + optional blue plastisol pad inside."""
    h = w * 0.75  # 10.5x7.75 proportions roughly
    # outer pan (aluminum rim)
    c.setFillColor(PAN_SILVER); c.setStrokeColor(STEEL_D); c.setLineWidth(0.4)
    c.roundRect(cx - w/2, cy - h/2, w, h, w*0.04, fill=1, stroke=1)
    # inner well shadow
    c.setFillColor(HexColor("#9AA0AA"))
    c.roundRect(cx - w/2 + w*0.05, cy - h/2 + h*0.06, w*0.90, h*0.88, w*0.02, fill=1, stroke=0)
    if with_pad:
        # blue plastisol pad
        c.setFillColor(PAD_BLUE); c.setStrokeColor(HexColor("#0A2840")); c.setLineWidth(0.3)
        c.rect(cx - w/2 + w*0.08, cy - h/2 + h*0.10, w*0.84, h*0.80, fill=1, stroke=1)
        # subtle texture on pad (tiny dots)
        c.setFillColor(Color(0,0,0,alpha=0.15))
        import random
        rng = random.Random(7)
        for _ in range(int(w*h/(cm*cm)*20)):
            c.circle(cx - w/2 + w*0.10 + rng.random()*w*0.80,
                     cy - h/2 + h*0.12 + rng.random()*h*0.76, 0.015*cm, fill=1, stroke=0)


def _draw_scalpel(c, cx, cy, length=2.2*cm, angle=0):
    """Stainless-steel scalpel — handle + blade."""
    c.saveState()
    c.translate(cx, cy)
    c.rotate(angle)
    # handle
    c.setFillColor(STEEL); c.setStrokeColor(STEEL_D); c.setLineWidth(0.3)
    c.roundRect(-length*0.5, -length*0.04, length*0.55, length*0.08, length*0.02, fill=1, stroke=1)
    # blade tip (small triangle)
    c.setFillColor(HexColor("#D0D5DC")); c.setStrokeColor(STEEL_D)
    p = c.beginPath()
    p.moveTo(length*0.05, length*0.04); p.lineTo(length*0.50, length*0.025)
    p.lineTo(length*0.50, -length*0.025); p.lineTo(length*0.05, -length*0.04); p.close()
    c.drawPath(p, fill=1, stroke=1)
    c.restoreState()


def _draw_scissors(c, cx, cy, length=2.4*cm, angle=0):
    """Stainless scissors."""
    c.saveState()
    c.translate(cx, cy)
    c.rotate(angle)
    # blades (crossed)
    c.setStrokeColor(STEEL_D); c.setLineWidth(1.2)
    c.line(-length*0.5, -length*0.05, length*0.2, length*0.10)
    c.line(-length*0.5, length*0.05, length*0.2, -length*0.10)
    # handles (rings)
    c.setStrokeColor(STEEL_D); c.setLineWidth(1.0); c.setFillColor(WHITE)
    c.circle(-length*0.50, -length*0.05, length*0.10, fill=1, stroke=1)
    c.circle(-length*0.50, length*0.05, length*0.10, fill=1, stroke=1)
    # pivot
    c.setFillColor(STEEL_D); c.circle(-length*0.10, 0, length*0.03, fill=1, stroke=0)
    c.restoreState()


def _draw_forceps(c, cx, cy, length=2.2*cm, angle=0):
    """Forceps / tweezers."""
    c.saveState()
    c.translate(cx, cy)
    c.rotate(angle)
    c.setStrokeColor(STEEL_D); c.setLineWidth(1.2)
    c.line(-length*0.5, length*0.04, length*0.4, length*0.0)
    c.line(-length*0.5, -length*0.04, length*0.4, -length*0.0)
    # connector
    c.setFillColor(STEEL); c.rect(-length*0.50, -length*0.05, length*0.10, length*0.10, fill=1, stroke=1)
    c.restoreState()


def _draw_probe(c, cx, cy, length=2.0*cm, angle=0):
    """Dissecting probe — long thin tool with a curved tip."""
    c.saveState()
    c.translate(cx, cy)
    c.rotate(angle)
    c.setFillColor(STEEL); c.setStrokeColor(STEEL_D); c.setLineWidth(0.3)
    c.rect(-length*0.5, -length*0.025, length*0.45, length*0.05, fill=1, stroke=1)
    # curved tip
    c.setStrokeColor(STEEL_D); c.setLineWidth(0.8)
    c.arc(length*0.0 - 0.05*cm, -length*0.08, length*0.20, length*0.08, startAng=180, extent=180)
    c.restoreState()


def _draw_tpin(c, cx, cy, length=0.7*cm, angle=0):
    """T-shaped pin for pinning specimens."""
    c.saveState()
    c.translate(cx, cy)
    c.rotate(angle)
    c.setStrokeColor(STEEL_D); c.setLineWidth(0.5)
    c.line(0, 0, 0, length)
    c.setFillColor(HexColor("#D9534F"))
    c.rect(-length*0.18, length - 0.03*cm, length*0.36, 0.08*cm, fill=1, stroke=0)
    c.restoreState()


def _draw_specimen(c, cx, cy, kind="frog", w=1.4*cm):
    """A small specimen icon."""
    if kind == "frog":
        c.setFillColor(SPECIMEN_GR); c.setStrokeColor(HexColor("#2A4A1A")); c.setLineWidth(0.3)
        c.ellipse(cx - w*0.45, cy - w*0.30, cx + w*0.45, cy + w*0.20, fill=1, stroke=1)
        # eyes
        c.setFillColor(SPECIMEN_GR); c.circle(cx - w*0.20, cy + w*0.22, w*0.10, fill=1, stroke=1)
        c.circle(cx + w*0.20, cy + w*0.22, w*0.10, fill=1, stroke=1)
        c.setFillColor(INK); c.circle(cx - w*0.20, cy + w*0.22, w*0.04, fill=1, stroke=0)
        c.circle(cx + w*0.20, cy + w*0.22, w*0.04, fill=1, stroke=0)
    elif kind == "flower":
        c.setFillColor(HexColor("#E08A45"))
        for i in range(6):
            a = math.radians(60*i)
            c.circle(cx + w*0.20*math.cos(a), cy + w*0.20*math.sin(a), w*0.12, fill=1, stroke=0)
        c.setFillColor(ACCENT_Y); c.circle(cx, cy, w*0.10, fill=1, stroke=0)
    elif kind == "worm":
        c.setFillColor(HexColor("#B07050")); c.setStrokeColor(HexColor("#5A2820")); c.setLineWidth(0.3)
        c.setLineWidth(1.5)
        c.bezier(cx - w*0.45, cy, cx - w*0.20, cy + w*0.20,
                 cx + w*0.20, cy - w*0.20, cx + w*0.45, cy)
    elif kind == "owl_pellet":
        c.setFillColor(HexColor("#8A6A4A")); c.setStrokeColor(HexColor("#4A2810")); c.setLineWidth(0.3)
        c.ellipse(cx - w*0.40, cy - w*0.25, cx + w*0.40, cy + w*0.25, fill=1, stroke=1)
        # tiny bones
        c.setStrokeColor(WHITE); c.setLineWidth(0.4)
        c.line(cx - w*0.20, cy - w*0.05, cx + w*0.15, cy + w*0.10)
        c.line(cx - w*0.10, cy + w*0.10, cx + w*0.20, cy - w*0.05)
    elif kind == "anatomy":
        # heart silhouette
        c.setFillColor(HexColor("#A02828")); c.setStrokeColor(HexColor("#400000")); c.setLineWidth(0.3)
        p = c.beginPath()
        p.moveTo(cx, cy - w*0.30)
        p.curveTo(cx + w*0.40, cy - w*0.10, cx + w*0.40, cy + w*0.30, cx, cy + w*0.05)
        p.curveTo(cx - w*0.40, cy + w*0.30, cx - w*0.40, cy - w*0.10, cx, cy - w*0.30)
        p.close()
        c.drawPath(p, fill=1, stroke=1)


def _draw_student(c, cx, cy, h=2.0*cm, shirt=GSC_BLUE):
    """Simple student silhouette."""
    c.setFillColor(HexColor("#E6B8A0")); c.setStrokeColor(HexColor("#8A5A3A")); c.setLineWidth(0.3)
    c.circle(cx, cy + h*0.30, h*0.15, fill=1, stroke=1)
    c.setFillColor(HexColor("#3A2818"))
    c.arc(cx - h*0.15, cy + h*0.16, cx + h*0.15, cy + h*0.46, startAng=0, extent=180)
    c.setFillColor(shirt); c.setStrokeColor(HexColor("#003366")); c.setLineWidth(0.3)
    p = c.beginPath()
    p.moveTo(cx - h*0.10, cy + h*0.18); p.lineTo(cx - h*0.28, cy - h*0.18)
    p.lineTo(cx - h*0.30, cy - h*0.42); p.lineTo(cx + h*0.30, cy - h*0.42)
    p.lineTo(cx + h*0.28, cy - h*0.18); p.lineTo(cx + h*0.10, cy + h*0.18); p.close()
    c.drawPath(p, fill=1, stroke=1)


def _draw_check(c, cx, cy, size=0.5*cm, color=GREEN_OK):
    c.setStrokeColor(color); c.setLineWidth(1.6)
    c.line(cx - size*0.3, cy, cx - size*0.05, cy - size*0.25)
    c.line(cx - size*0.05, cy - size*0.25, cx + size*0.3, cy + size*0.3)


def _draw_x(c, cx, cy, size=0.5*cm, color=RED_X):
    c.setStrokeColor(color); c.setLineWidth(1.6)
    c.line(cx - size*0.3, cy - size*0.3, cx + size*0.3, cy + size*0.3)
    c.line(cx - size*0.3, cy + size*0.3, cx + size*0.3, cy - size*0.3)


def _draw_callout_line(c, x1, y1, x2, y2, color=GSC_BLUE):
    c.setStrokeColor(color); c.setLineWidth(0.6)
    c.line(x1, y1, x2, y2)
    c.setFillColor(color); c.circle(x2, y2, 0.06*cm, fill=1, stroke=0)


# ─── Mockup container ──────────────────────────────────────────────

class ListingMockup(Flowable):
    def __init__(self, slot, role, draw_fn, bg=WHITE):
        self.slot = slot; self.role = role; self.draw_fn = draw_fn; self.bg = bg
        self.size = 7.0*cm
        Flowable.__init__(self)
    def wrap(self, *a): return (self.size, self.size + 0.5*cm)
    def draw(self):
        c = self.canv; s = self.size
        c.setFillColor(self.bg); c.setStrokeColor(HexColor("#CCCCCC")); c.setLineWidth(0.4)
        c.rect(0, 0, s, s, fill=1, stroke=1)
        c.setFillColor(GSC_GREEN_D); c.rect(0, s - 0.75*cm, 1.5*cm, 0.75*cm, fill=1, stroke=0)
        c.setFillColor(WHITE); c.setFont("Helvetica-Bold", 12)
        c.drawCentredString(0.75*cm, s - 0.52*cm, f"#{self.slot}")
        self.draw_fn(c, s/2, s/2 - 0.2*cm)
        c.setFillColor(GSC_BLUE)
        tw = c.stringWidth(self.role.upper(), "Helvetica-Bold", 7.5) + 0.5*cm
        c.rect(s - tw, 0, tw, 0.6*cm, fill=1, stroke=0)
        c.setFillColor(WHITE); c.setFont("Helvetica-Bold", 7.5)
        c.drawString(s - tw + 0.25*cm, 0.22*cm, self.role.upper())
        c.setFillColor(GREY); c.setFont("Helvetica", 6.5)
        c.drawCentredString(s/2, 0.20*cm, "2000 × 2000 px")


# ─── Concept drawings — 7 listing images ────────────────────────────

def cpt_main_hero(c, cx, cy):
    """#1 Hero — pan with pad + tools arranged inside, top-down."""
    _draw_pan(c, cx, cy + 0.2*cm, w=5.0*cm, with_pad=True)
    # tools arranged inside
    _draw_scalpel(c, cx - 1.5*cm, cy + 0.7*cm, length=2.0*cm, angle=-15)
    _draw_scissors(c, cx + 1.0*cm, cy + 0.7*cm, length=2.0*cm, angle=20)
    _draw_forceps(c, cx - 0.8*cm, cy - 0.1*cm, length=1.9*cm, angle=10)
    _draw_probe(c, cx + 1.2*cm, cy - 0.2*cm, length=1.9*cm, angle=-25)
    _draw_scalpel(c, cx - 0.2*cm, cy - 0.7*cm, length=1.8*cm, angle=5)
    # 4 t-pins in corners
    for dx, dy in [(-1.8*cm, 1.0*cm), (1.8*cm, 1.0*cm), (-1.8*cm, -1.0*cm), (1.8*cm, -1.0*cm)]:
        _draw_tpin(c, cx + dx, cy + dy, length=0.4*cm, angle=45)


def cpt_whats_included(c, cx, cy):
    """#2 — exploded view with labeled callouts."""
    c.setFillColor(GSC_GREEN_D); c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(cx, cy + 2.6*cm, "EVERYTHING.")
    c.drawCentredString(cx, cy + 2.25*cm, "IN ONE BOX.")
    # central tool laid-out grid
    _draw_pan(c, cx, cy - 0.4*cm, w=2.6*cm, with_pad=True)
    # tool list with check marks on the right
    items = [
        "Aluminum dissection pan",
        "Self-healing plastisol pad",
        "Stainless scalpel",
        "Stainless scissors",
        "Forceps / tweezers",
        "Dissecting probe",
        "T-pins (for pinning)",
    ]
    for i, item in enumerate(items):
        y = cy + 1.6*cm - i*0.30*cm
        _draw_check(c, cx + 1.7*cm, y, size=0.3*cm)
        c.setFillColor(INK); c.setFont("Helvetica", 7)
        c.drawString(cx + 1.9*cm, y - 0.08*cm, item)
    # bottom strap
    c.setFillColor(GREY); c.setFont("Helvetica-Oblique", 6.0)
    c.drawCentredString(cx, cy - 2.5*cm, "Nothing to source separately. Open and start dissecting.")


def cpt_pad(c, cx, cy):
    """#3 — self-healing pad: macro + before/after pinhole."""
    c.setFillColor(GSC_GREEN_D); c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(cx, cy + 2.6*cm, "SELF-HEALING PAD.")
    c.drawCentredString(cx, cy + 2.25*cm, "BUILT FOR REPEATED LABS.")
    # large pad close-up
    c.setFillColor(PAD_BLUE); c.setStrokeColor(HexColor("#0A2840")); c.setLineWidth(0.3)
    c.rect(cx - 2.4*cm, cy - 1.2*cm, 4.8*cm, 2.4*cm, fill=1, stroke=1)
    # texture dots
    import random
    rng = random.Random(11)
    c.setFillColor(Color(0,0,0,alpha=0.18))
    for _ in range(80):
        c.circle(cx - 2.3*cm + rng.random()*4.6*cm, cy - 1.1*cm + rng.random()*2.2*cm, 0.02*cm, fill=1, stroke=0)
    # T-pins stuck in
    for x, y in [(cx - 1.5*cm, cy + 0.5*cm), (cx + 1.2*cm, cy + 0.3*cm), (cx - 0.5*cm, cy - 0.5*cm), (cx + 1.6*cm, cy - 0.7*cm)]:
        _draw_tpin(c, x, y, length=0.5*cm, angle=0)
    # zoom callout — "self-heals" with arrow
    c.setFillColor(LIGHT_GRN); c.setStrokeColor(GSC_GREEN); c.setLineWidth(0.6)
    c.roundRect(cx - 1.6*cm, cy - 2.3*cm, 3.2*cm, 0.7*cm, 0.10*cm, fill=1, stroke=1)
    c.setFillColor(GSC_GREEN_D); c.setFont("Helvetica-Bold", 8)
    c.drawCentredString(cx, cy - 1.95*cm, "Pinholes close on their own")
    c.setFillColor(GREY); c.setFont("Helvetica", 6.5)
    c.drawCentredString(cx, cy - 2.15*cm, "Use the pad 30+ times. Surface stays flat.")


def cpt_stainless(c, cx, cy):
    """#4 — stainless steel quality close-up with material callouts."""
    c.setFillColor(GSC_GREEN_D); c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(cx, cy + 2.6*cm, "STAINLESS STEEL.")
    c.drawCentredString(cx, cy + 2.25*cm, "NOT THE CHEAP STUFF.")
    # 3 tools large + spec callouts
    _draw_scalpel(c, cx - 1.5*cm, cy + 0.7*cm, length=3.0*cm, angle=10)
    _draw_scissors(c, cx + 1.4*cm, cy + 0.7*cm, length=3.0*cm, angle=-5)
    _draw_forceps(c, cx, cy - 0.8*cm, length=2.8*cm, angle=0)
    # spec strip
    specs = [
        ("CORROSION-RESISTANT",  "Won't rust between labs"),
        ("PRECISION-GROUND BLADES", "Clean cuts on day 1 and day 30"),
        ("BALANCED HANDLES",     "Comfortable for teen hands"),
    ]
    for i, (a, b) in enumerate(specs):
        y = cy - 1.7*cm - i*0.30*cm
        c.setFillColor(GSC_BLUE); c.circle(cx - 2.4*cm, y, 0.08*cm, fill=1, stroke=0)
        c.setFillColor(GSC_BLUE_D); c.setFont("Helvetica-Bold", 6.5)
        c.drawString(cx - 2.2*cm, y - 0.06*cm, a)
        c.setFillColor(GREY); c.setFont("Helvetica", 6)
        c.drawString(cx + 0.3*cm, y - 0.06*cm, b)


def cpt_use_cases(c, cx, cy):
    """#5 — what you can dissect: 5 specimen types."""
    c.setFillColor(GSC_GREEN_D); c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(cx, cy + 2.6*cm, "FROG · FLOWER · WORM · OWL PELLET · ANATOMY.")
    cases = [
        ("FROG",       cx - 2.4*cm, "frog"),
        ("FLOWER",     cx - 1.2*cm, "flower"),
        ("EARTHWORM",  cx,          "worm"),
        ("OWL PELLET", cx + 1.2*cm, "owl_pellet"),
        ("HEART",      cx + 2.4*cm, "anatomy"),
    ]
    for label, x, kind in cases:
        c.setFillColor(OFFWHITE); c.setStrokeColor(GSC_GREEN); c.setLineWidth(0.5)
        c.roundRect(x - 0.55*cm, cy - 0.5*cm, 1.1*cm, 1.4*cm, 0.08*cm, fill=1, stroke=1)
        _draw_specimen(c, x, cy + 0.3*cm, kind=kind, w=0.9*cm)
        c.setFillColor(GSC_GREEN_D); c.setFont("Helvetica-Bold", 5.5)
        c.drawCentredString(x, cy - 1.05*cm, label)
    # bottom strap
    c.setFillColor(GREY); c.setFont("Helvetica-Oblique", 6.5)
    c.drawCentredString(cx, cy - 2.0*cm, "One kit covers middle-school through college-level biology.")


def cpt_classroom(c, cx, cy):
    """#6 — student doing dissection in a classroom lab."""
    c.setFillColor(GSC_GREEN_D); c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(cx, cy + 2.6*cm, "BIOLOGY YOU CAN TOUCH.")
    # lab bench
    c.setFillColor(HexColor("#D9C9B0")); c.setStrokeColor(HexColor("#7A5A30")); c.setLineWidth(0.3)
    c.rect(cx - 3.0*cm, cy - 1.6*cm, 6.0*cm, 0.4*cm, fill=1, stroke=1)
    # student
    _draw_student(c, cx - 1.6*cm, cy + 0.4*cm, h=2.0*cm, shirt=GSC_BLUE)
    # pan + tools on bench
    _draw_pan(c, cx + 0.6*cm, cy - 1.0*cm, w=2.4*cm, with_pad=True)
    _draw_scalpel(c, cx + 0.0*cm, cy - 0.9*cm, length=1.4*cm, angle=15)
    _draw_specimen(c, cx + 0.8*cm, cy - 1.0*cm, kind="frog", w=0.8*cm)
    # bottom strap
    c.setFillColor(GREY); c.setFont("Helvetica-Oblique", 6.5)
    c.drawCentredString(cx, cy - 2.4*cm, "From textbook diagram to hands-on lab in five minutes.")


def cpt_specs_brand(c, cx, cy):
    """#7 — spec sheet + brand close."""
    c.setFillColor(GSC_GREEN_D); c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(cx, cy + 2.6*cm, "WHAT'S IN THE BOX")
    # pan + tools on left
    _draw_pan(c, cx - 1.8*cm, cy + 0.4*cm, w=2.6*cm, with_pad=True)
    # spec list on the right
    specs = [
        ("10.5\" × 7.75\" × 1.5\"",   "Aluminum pan, fits standard lab bench"),
        ("Self-healing pad",            "Plastisol surface · pinholes close"),
        ("Stainless steel tools",       "Scalpel · scissors · forceps · probe"),
        ("T-pins",                      "For pinning specimens to the pad"),
        ("Easy cleanup",                "Wipe, sterilize, store"),
    ]
    for i, (a, b) in enumerate(specs):
        y = cy + 1.4*cm - i*0.55*cm
        c.setFillColor(GSC_GREEN); c.circle(cx + 0.5*cm, y, 0.08*cm, fill=1, stroke=0)
        c.setFillColor(INK); c.setFont("Helvetica-Bold", 7.5)
        c.drawString(cx + 0.7*cm, y - 0.06*cm, a)
        c.setFillColor(GREY); c.setFont("Helvetica", 6.5)
        c.drawString(cx + 0.7*cm, y - 0.28*cm, b)
    # GSC brand close
    c.setFillColor(GSC_GREEN); c.rect(cx - 3.0*cm, cy - 2.4*cm, 6.0*cm, 0.8*cm, fill=1, stroke=0)
    c.setFillColor(WHITE); c.setFont("Helvetica-Bold", 13)
    c.drawCentredString(cx, cy - 2.10*cm, "GO SCIENCE CRAZY")
    c.setFillColor(WHITE); c.setFont("Helvetica", 7.5)
    c.drawCentredString(cx, cy - 2.32*cm, "Hands-on tools for the classroom · since 2003")


# ─── Page chrome ────────────────────────────────────────────────────

def cover_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(GSC_GREEN); canvas.rect(0, PAGE_H - 5*cm, PAGE_W, 5*cm, fill=1, stroke=0)
    canvas.setFillColor(GSC_BLUE); canvas.rect(0, PAGE_H - 5.3*cm, PAGE_W, 0.3*cm, fill=1, stroke=0)
    canvas.setFillColor(WHITE); canvas.setFont("Helvetica-Bold", 38)
    canvas.drawString(ML, PAGE_H - 2.6*cm, "GSC")
    canvas.setFont("Helvetica-Bold", 14)
    canvas.drawString(ML + 3.0*cm, PAGE_H - 2.2*cm, "inc.")
    canvas.setFillColor(WHITE); canvas.setFont("Helvetica", 14)
    canvas.drawString(ML, PAGE_H - 3.4*cm, "Go Science Crazy")

    canvas.setFillColor(GSC_GREEN_D); canvas.setFont("Helvetica-Bold", 30)
    canvas.drawString(ML, PAGE_H - 7.5*cm, "Dissection Kit")
    canvas.setFillColor(INK); canvas.setFont("Helvetica", 14)
    canvas.drawString(ML, PAGE_H - 8.2*cm, "Pan · Pad · Stainless tools — for biology labs · 360-DS02-KT")
    canvas.setStrokeColor(GSC_GREEN); canvas.setLineWidth(0.5)
    canvas.line(ML, PAGE_H - 8.7*cm, ML + 8*cm, PAGE_H - 8.7*cm)
    canvas.setFillColor(GSC_BLUE); canvas.setFont("Helvetica-Bold", 14)
    canvas.drawString(ML, PAGE_H - 9.5*cm, "Amazon.com — Image Plan Brief")
    canvas.setFillColor(GREY); canvas.setFont("Helvetica", 11)
    canvas.drawString(ML, PAGE_H - 10.1*cm, "Buyer psychology · 7 listing images · A+ outline · Master copy")

    y = 3.4*cm
    fields = [("BRAND", "GSC International"), ("MARKET", "Amazon.com"), ("ASIN", "B0F7MN3L5K"), ("DATE", "2026-05-25")]
    for i, (k, v) in enumerate(fields):
        x = ML + i * 4.4*cm
        canvas.setFillColor(GSC_GREEN_D); canvas.setFont("Helvetica-Bold", 8)
        canvas.drawString(x, y, k)
        canvas.setFillColor(INK); canvas.setFont("Helvetica", 11)
        canvas.drawString(x, y - 0.55*cm, v)

    # hero kit drawing on the right side
    _draw_pan(canvas, PAGE_W - MR - 4.5*cm, PAGE_H - 13*cm, w=6.5*cm, with_pad=True)
    _draw_scalpel(canvas, PAGE_W - MR - 6.0*cm, PAGE_H - 12.2*cm, length=2.5*cm, angle=-15)
    _draw_scissors(canvas, PAGE_W - MR - 3.0*cm, PAGE_H - 12.2*cm, length=2.5*cm, angle=20)
    _draw_forceps(canvas, PAGE_W - MR - 5.0*cm, PAGE_H - 13.5*cm, length=2.3*cm, angle=10)
    _draw_probe(canvas, PAGE_W - MR - 3.5*cm, PAGE_H - 13.8*cm, length=2.3*cm, angle=-25)
    canvas.setFillColor(GSC_GREEN_D); canvas.setFont("Helvetica-Oblique", 10)
    canvas.drawString(ML, PAGE_H - 14.5*cm, "Open the kit. Start the lab. Everything you need, in one box.")

    canvas.setFillColor(GSC_GREEN); canvas.rect(0, 0, PAGE_W, 1.3*cm, fill=1, stroke=0)
    canvas.setFillColor(WHITE); canvas.setFont("Helvetica-Bold", 9)
    canvas.drawString(ML, 0.5*cm, "HANDS-ON SCIENCE. EVERY LAB. EVERY STUDENT.")
    canvas.setFillColor(WHITE); canvas.setFont("Helvetica", 9)
    canvas.drawRightString(PAGE_W - MR, 0.5*cm, "Prepared by EQUALICE")
    canvas.restoreState()


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(GSC_GREEN); canvas.setLineWidth(2.0)
    canvas.line(ML, PAGE_H - 1.0*cm, PAGE_W - MR, PAGE_H - 1.0*cm)
    canvas.setFillColor(GSC_GREEN_D); canvas.setFont("Helvetica-Bold", 11)
    canvas.drawString(ML, PAGE_H - 0.7*cm, "GSC")
    canvas.setFillColor(GREY); canvas.setFont("Helvetica", 8)
    canvas.drawString(ML + 1.2*cm, PAGE_H - 0.7*cm, "Dissection Kit 360-DS02-KT — Amazon.com Image Plan")
    canvas.drawRightString(PAGE_W - MR, PAGE_H - 0.7*cm, f"Page {doc.page}")
    canvas.setStrokeColor(HexColor("#E0DCC8")); canvas.setLineWidth(0.4)
    canvas.line(ML, MB - 0.4*cm, PAGE_W - MR, MB - 0.4*cm)
    canvas.setFillColor(GREY); canvas.setFont("Helvetica", 7.5)
    canvas.drawString(ML, MB - 0.7*cm, "Prepared by EQUALICE — 2026-05-25 · Go Science Crazy")
    canvas.restoreState()


def build():
    doc = BaseDocTemplate(OUT, pagesize=A4,
                          leftMargin=ML, rightMargin=MR,
                          topMargin=MT, bottomMargin=MB,
                          title="GSC Dissection Kit 360-DS02-KT — Amazon.com Image Plan",
                          author="EQUALICE")
    cf = Frame(ML, MB, CW, PAGE_H - MT - MB, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    bf = Frame(ML, MB, CW, PAGE_H - MT - MB, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([
        PageTemplate(id="Cover", frames=[cf], onPage=cover_page),
        PageTemplate(id="Body", frames=[bf], onPage=header_footer),
    ])

    s = []
    s.append(Spacer(1, PAGE_H - MT - MB - 2))
    s.append(NextPageTemplate("Body")); s.append(PageBreak())

    # ───── At a Glance ─────
    s.append(Paragraph("At a Glance", H2)); s.append(HRule())
    glance = [
        ["Product",        "Dissection Kit 360-DS02-KT — aluminum pan + self-healing plastisol pad + stainless tools"],
        ["Brand",          "GSC International · Go Science Crazy"],
        ["ASIN",           "B0F7MN3L5K · Amazon.com"],
        ["Pan size",       "10.5 in × 7.75 in × 1.5 in · fits standard lab bench"],
        ["Use cases",      "Frog · flower · earthworm · owl pellet · heart/anatomy · veterinary training · medical-school prep"],
        ["Target group",   "Biology students (middle school → college) · teachers · homeschool · vet / med-school prep"],
        ["Buyer = User?",  "Often NO. Teacher / school buys; student uses. Frame must satisfy both."],
        ["Hero USP",       "Complete kit — pan + pad + tools in one box. No sourcing pads + scalpels + scissors separately."],
        ["Top KWs (SV)",   "dissection kit (2,549) · dissection kits (1,170) · dissection kit anatomy lab (489) · lab dissection kits (477) · scalpel kit (462) · biology dissection kit (386)"],
        ["Pos. reviews",   "Sharp & precise · durable stainless steel · good tool variety · easy clean · sturdy build"],
        ["Neg. reviews",   "Blades dull quickly · missing tools · blades don't fit handle · scissors break · rust over time · flimsy cases · no instructions"],
        ["Brand brief notes", "Engaging for students 15+ · creative freedom 5/5 · school-appropriate · NOT childish toys · sharp-tool safety mandatory"],
    ]
    t = Table([[Paragraph(f"<b>{k}</b>", BODY), Paragraph(v, BODY)] for k, v in glance],
              colWidths=[3.6*cm, CW - 3.6*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,-1), LIGHT_GRN),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LINEBELOW", (0,0), (-1,-1), 0.3, HexColor("#E0DCC8")),
        ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 6), ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ]))
    s.append(t)

    s.append(Spacer(1, 0.4*cm))
    strat = Table([[Paragraph(
        "<b>Strategic read.</b> Buyer fear #1 in this category is <i>\"kit will arrive incomplete / tools will break / blades will rust\"</i> — every negative "
        "review confirms it. The image plan has to <b>show every tool that's in the box</b> (frame #2) and <b>prove the steel quality</b> (frame #4) before the "
        "buyer ever sees the price. Frame #3 (self-healing pad) defends the durability claim. Frame #5 (5 specimen types) sells the breadth that justifies cost. "
        "Together these defuse the four most common 1-star themes <i>before purchase</i>.", BODY)]],
        colWidths=[CW])
    strat.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), GSC_GREEN_D),
        ("TEXTCOLOR", (0,0), (-1,-1), WHITE),
        ("LEFTPADDING", (0,0), (-1,-1), 14), ("RIGHTPADDING", (0,0), (-1,-1), 14),
        ("TOPPADDING", (0,0), (-1,-1), 10), ("BOTTOMPADDING", (0,0), (-1,-1), 10),
    ]))
    s.append(strat)

    # ───── Buyer + Review Map ─────
    s.append(PageBreak())
    s.append(Paragraph("Who buys this — and what makes them nervous", H2)); s.append(HRule())
    persona = [
        ("Biology teacher (high school)",
         "Buys 15–30 kits at a time for a class set. Has been burned by cheap kits where the scissors snap mid-lab. Cares most about <b>predictable kit completeness</b> and <b>tool reusability across years</b>. Will write a furious 1-star if a kit arrives missing the forceps."),
        ("Lab coordinator (college)",
         "Equips intro biology labs. Buys in bulk. Reads the spec carefully — wants the pan dimensions and pad material in writing. Pad longevity is a key cost metric: a pad that lasts 30 sessions is worth 3× one that lasts 10."),
        ("Homeschool parent / pre-med student",
         "Single-kit buyer. Anatomy or pre-med prep. Cares about the tool quality more than the pan. Wants steel that <b>feels real</b>, not toy-store stamped-metal."),
    ]
    p_tbl = Table([[Paragraph(f"<b>{k}</b>", BODY), Paragraph(v, BODY)] for k, v in persona],
                  colWidths=[5.2*cm, CW - 5.2*cm])
    p_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,-1), GSC_BLUE),
        ("TEXTCOLOR", (0,0), (0,-1), WHITE),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LINEBELOW", (0,0), (-1,-1), 0.3, HexColor("#E0DCC8")),
        ("LEFTPADDING", (0,0), (-1,-1), 10), ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 8), ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ]))
    s.append(p_tbl)

    s.append(Spacer(1, 0.4*cm))
    s.append(Paragraph("Review themes → Image responses", H3))
    rev = [
        ["Theme (verbatim)",                                  "Sentiment",  "How the image plan answers it"],
        ["\"Sharp and precise tools\"",                        "POS",        "Frame #4 — close-up of stainless tools + spec strip"],
        ["\"Stainless steel feels durable and resistant\"",    "POS",        "Frame #4 — material callout: corrosion-resistant"],
        ["\"Carrying cases keep instruments organized\"",      "POS",        "Frame #7 — \"What's in the box\" spec sheet"],
        ["\"Tools easy to clean and sterilize\"",              "POS",        "Frame #7 — \"Easy cleanup\" spec line"],
        ["\"Blades dull quickly with repeated use\"",          "NEG",        "Frame #4 — \"Precision-ground · Clean cuts day 1 AND day 30\""],
        ["\"Missing tools / incomplete kit on arrival\"",      "NEG",        "Frame #2 — every tool shown + checkmarked individually"],
        ["\"Blades don't fit the handle properly\"",           "NEG",        "Frame #2 — show scalpel + handle as one labeled unit"],
        ["\"Scissors or probes bend / break\"",                "NEG",        "Frame #4 — \"Balanced handles · daily-lab tested\""],
        ["\"Rust or corrosion over time\"",                    "NEG",        "Frame #4 — \"Corrosion-resistant\" badge front-and-center"],
        ["\"Carrying case feels flimsy\"",                     "NEG",        "Frame #7 — show pan as primary storage (sturdy aluminum)"],
        ["\"Lack of instructions\"",                           "NEG",        "A+ Module 6 Q&A — include 'how to clean / store / replace blades'"],
    ]
    rt = Table([[Paragraph(c, SMALL if i > 0 else BODY) for c in r] for i, r in enumerate(rev)],
               colWidths=[6.6*cm, 1.6*cm, CW - 8.2*cm])
    rt.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), GSC_GREEN_D),
        ("TEXTCOLOR", (0,0), (-1,0), WHITE),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 6), ("RIGHTPADDING", (0,0), (-1,-1), 6),
        ("TOPPADDING", (0,0), (-1,-1), 5), ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("GRID", (0,0), (-1,-1), 0.3, HexColor("#DDDDDD")),
        ("ROWBACKGROUNDS", (0,1), (-1,4), [WHITE, LIGHT_GRN]),
        ("ROWBACKGROUNDS", (0,5), (-1,-1), [HexColor("#FBE5E8"), HexColor("#FFF4E5")]),
    ]))
    s.append(rt)

    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("Top KWs → where they live in the listing", H3))
    kws = [
        ["KW",                                "SV",       "Used in"],
        ["dissection kit",                    "2,549",    "Title (first 80 chars) · Bullet 1 · A+ Module 1"],
        ["dissection kits",                   "1,170",    "Backend · variant cap"],
        ["dissection kit anatomy lab",        "489",      "Title · Bullet 3 · Image #5 (anatomy specimen)"],
        ["lab dissection kits",               "477",      "Title · Bullet 4 (lab use)"],
        ["scalpel kit",                       "462",      "Bullet 2 · Image #2 callout"],
        ["biology dissection kit",            "386",      "Title · Bullet 1 · Image #5"],
        ["dissecting kit",                    "354",      "Backend · A+"],
        ["dissection kit biology lab",        "233",      "Title · Bullet 4"],
        ["basic dissection kit",              "226",      "Backend (target intent: 'first-time buyer')"],
        ["anatomy dissection kit",            "107",      "Image #5 + A+"],
    ]
    kw_tbl = Table([[Paragraph(c, SMALL if i > 0 else BODY) for c in r] for i, r in enumerate(kws)],
                   colWidths=[5.5*cm, 1.8*cm, CW - 7.3*cm])
    kw_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), GSC_BLUE_D),
        ("TEXTCOLOR", (0,0), (-1,0), WHITE),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 6), ("RIGHTPADDING", (0,0), (-1,-1), 6),
        ("TOPPADDING", (0,0), (-1,-1), 4), ("BOTTOMPADDING", (0,0), (-1,-1), 4),
        ("GRID", (0,0), (-1,-1), 0.3, HexColor("#DDDDDD")),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, LIGHT_BLU]),
    ]))
    s.append(kw_tbl)

    # ───── Image Plan ─────
    s.append(PageBreak())
    s.append(Paragraph("Image Plan — 7 Listing Frames", H2)); s.append(HRule())
    s.append(Paragraph(
        "2000 × 2000 px · sRGB · JPG · ≤ 5 MB. Mockup left, concept + headline + benefit + product proof right.", SUB))

    listing = [
        (1, "HERO",
         "(no overlay — Amazon main-image rule. White BG.)",
         "Top-down hero shot of the open pan with the blue pad inside, and every tool laid out neatly: scalpel, scissors, forceps, probe, T-pins. Top-down so the buyer immediately sees the FULL inventory.",
         "Every negative review starts with \"kit was missing X\". Showing the complete contents in image #1 pre-empts that worry at the SERP level.",
         cpt_main_hero, WHITE),
        (2, "HOOK · WHAT'S INCLUDED",
         "EVERYTHING. IN ONE BOX.",
         "Same pan in the center but smaller. To the right: a 7-line checklist with green checks: Aluminum pan · Self-healing pad · Scalpel · Scissors · Forceps · Probe · T-pins. Each line is a separate green check — visually obvious that nothing's missing.",
         "Direct response to the #1 negative review theme. The buyer needs the checklist visible BEFORE they buy, not after the kit arrives.",
         cpt_whats_included, OFFWHITE),
        (3, "PROOF · SELF-HEALING PAD",
         "SELF-HEALING PAD. BUILT FOR REPEATED LABS.",
         "Macro shot of the blue plastisol pad with several T-pins stuck in. Below: green callout box: \"Pinholes close on their own · Use the pad 30+ times · Surface stays flat\".",
         "The lab coordinator's #1 question is pad lifespan. This frame answers it with a concrete number (30+ sessions) and the mechanism (self-healing material).",
         cpt_pad, WHITE),
        (4, "PROOF · STAINLESS STEEL QUALITY",
         "STAINLESS STEEL. NOT THE CHEAP STUFF.",
         "Close-up of scalpel + scissors + forceps. Three blue dots with spec callouts: CORROSION-RESISTANT · PRECISION-GROUND BLADES · BALANCED HANDLES. Each with a 1-line benefit.",
         "Defuses the entire bottom block of negative reviews: dull blades, rust, scissors break, blade fit. Show the quality in image, not just claim it in copy.",
         cpt_stainless, OFFWHITE),
        (5, "USE CASES · 5 SPECIMENS",
         "FROG · FLOWER · WORM · OWL PELLET · ANATOMY.",
         "Five icon tiles in a row — each specimen type with a tiny illustration. Tells the buyer: middle-school through college, plus vet / med-school prep.",
         "Sells the breadth that justifies the kit price. Hits the long-tail \"anatomy dissection kit\" / \"biology dissection kit\" KWs.",
         cpt_use_cases, WHITE),
        (6, "LIFESTYLE · CLASSROOM",
         "BIOLOGY YOU CAN TOUCH.",
         "Student at a lab bench with the pan open, scalpel in hand, frog specimen pinned. Bench is organized — sells the controlled, focused work the kit enables.",
         "The brand brief explicitly asks for student engagement. This frame is the emotional pay-off — sells the teacher-buyer on what they'll see in the classroom.",
         cpt_classroom, OFFWHITE),
        (7, "WHAT'S IN THE BOX + BRAND",
         "Spec sheet for procurement + GSC brand close.",
         "5-line spec sheet with green dots: pan dimensions · self-healing pad · stainless tools · T-pins · easy cleanup. GSC green brand bar at bottom: \"GO SCIENCE CRAZY · Hands-on tools for the classroom.\"",
         "Lab coordinators forward the spec image to procurement. This frame is screenshot-ready. Brand bar closes the trust loop and sells cross-buy (BeeSpi, etc.).",
         cpt_specs_brand, WHITE),
    ]
    for slot, role, headline, concept, why, fn, bg in listing:
        s.append(Paragraph(f"Image {slot} — {role}", H3))
        m = ListingMockup(slot, role, fn, bg=bg)
        side_rows = [
            Paragraph(f"<b>Headline:</b> {headline}", BODY),
            Spacer(1, 0.1*cm),
            Paragraph(f"<b>Concept:</b> {concept}", BODY),
            Spacer(1, 0.1*cm),
            Paragraph(f"<i>Why it works:</i> {why}", QUOTE),
        ]
        side = Table([[r] for r in side_rows], colWidths=[CW - m.size - 0.4*cm])
        side.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),
                                  ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0),
                                  ("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),2)]))
        row = Table([[m, side]], colWidths=[m.size + 0.4*cm, CW - m.size - 0.4*cm])
        row.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),
                                 ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0)]))
        s.append(KeepTogether([row])); s.append(Spacer(1, 0.35*cm))

    # ───── A+ outline ─────
    s.append(PageBreak())
    s.append(Paragraph("A+ Premium Content — 7 Modules", H2)); s.append(HRule())
    modules = [
        ("Module 1 · Premium Full Image",
         "OPEN THE BOX. START THE LAB.",
         "Wide hero banner. Open pan with all tools laid out, GSC wordmark top-left, student hands reaching in from the side."),
        ("Module 2 · Carousel (5 tiles)",
         "WHAT'S IN EVERY KIT.",
         "Five carousel tiles, one per category: PAN · PAD · TOOLS · T-PINS · STORAGE. Each tile: tiny image + 1-line benefit."),
        ("Module 3 · Premium Full Image",
         "BUILT FOR REPEATED USE.",
         "Macro of the self-healing pad with multiple T-pins stuck in. \"Use it 30+ times. The surface heals between sessions.\""),
        ("Module 4 · Premium Full Image",
         "TOOLS THAT WON'T QUIT MID-DISSECTION.",
         "Beauty close-up of stainless tools side-by-side. Spec callouts: corrosion-resistant · precision-ground · balanced grip."),
        ("Module 5 · Carousel (5 tiles)",
         "WHAT YOU CAN DISSECT.",
         "Frog · flower · earthworm · owl pellet · sheep heart. Each tile: tiny illustration + 1-line educational use."),
        ("Module 6 · Q&A",
         "TEACHER QUESTIONS, ANSWERED.",
         "5–6 Q&A pairs: Is the pad reusable? · How to clean tools? · Replacement blades? · Pan dimensions? · Suitable for which grades? · Sharp-tool safety?"),
        ("Module 7 · Comparison Chart",
         "GSC DISSECTION KIT vs. CHEAPER BLISTER-PACK KITS.",
         "Four columns: GSC (highlighted) · Generic Amazon kit · Carolina Biological · Frey Scientific. Rows: pan material · pad type · tool steel grade · cost per kit · pad lifespan."),
    ]
    for hd, head, desc in modules:
        s.append(Paragraph(hd, H3))
        s.append(Paragraph(f"<b>Headline:</b> {head}", BODY))
        s.append(Paragraph(f"<b>Concept:</b> {desc}", BODY))
        s.append(Spacer(1, 0.15*cm))

    # ───── Master Copy ─────
    s.append(PageBreak())
    s.append(Paragraph("Master Copy — paste-ready", H2)); s.append(HRule())

    s.append(Paragraph("Title (≤ 200 chars)", H3))
    tbox = Table([[Paragraph(
        "<b>GSC International Dissection Kit 360-DS02-KT — Complete Biology Dissection Kit with Aluminum Pan, Self-Healing Pad, "
        "Stainless Steel Scalpel · Scissors · Forceps · Probe · T-Pins · For Anatomy &amp; Lab Use · 10.5\" Pan</b>", BODY)]],
        colWidths=[CW])
    tbox.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), GSC_GREEN_D),
        ("TEXTCOLOR", (0,0), (-1,-1), WHITE),
        ("LEFTPADDING", (0,0), (-1,-1), 12), ("RIGHTPADDING", (0,0), (-1,-1), 12),
        ("TOPPADDING", (0,0), (-1,-1), 8), ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ]))
    s.append(tbox)

    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("Bullets (5 × ~240 chars)", H3))
    bullets = [
        ("COMPLETE DISSECTION KIT IN ONE BOX",
         "Everything a biology lab needs: a 10.5 × 7.75 × 1.5 in aluminum pan, a self-healing plastisol pad, a stainless-steel scalpel, "
         "scissors, forceps, probe, and T-pins. Open the kit and start the lab — no sourcing parts separately."),
        ("SELF-HEALING PAD · REUSABLE FOR 30+ SESSIONS",
         "The plastisol pad surface closes around pin holes between labs, so the surface stays flat through repeated specimen pinning. "
         "Designed for daily classroom use across a full school year of labs."),
        ("STAINLESS-STEEL TOOLS · BUILT FOR REAL LAB WORK",
         "Corrosion-resistant stainless tools that survive specimen contact, cleaning, and sterilization between sessions. "
         "Precision-ground blades stay sharp, balanced handles fit teen and adult hands."),
        ("FROM FROG TO ANATOMY · GRADES 7 THROUGH COLLEGE",
         "Suitable for biology, anatomy, veterinary, and medical-prep dissections: frog, earthworm, flower, owl pellet, fetal pig, sheep heart, "
         "and more. One kit covers a multi-year science curriculum."),
        ("HANDS-ON SCIENCE FROM GO SCIENCE CRAZY",
         "GSC International designs dependable, classroom-ready science equipment. Hands-on biology becomes the kind students remember. "
         "NOT A TOY: educational/scientific use only. Sharp instruments included — adult supervision required, ages 15+."),
    ]
    bt = Table([[Paragraph(f"<b>{i+1}. {h}</b>", BODY), Paragraph(b, BODY)] for i, (h, b) in enumerate(bullets)],
               colWidths=[6.0*cm, CW - 6.0*cm])
    bt.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,-1), LIGHT_GRN),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LINEBELOW", (0,0), (-1,-1), 0.3, HexColor("#E0DCC8")),
        ("LEFTPADDING", (0,0), (-1,-1), 10), ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 6), ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ]))
    s.append(bt)

    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("Backend search terms (≤ 250 bytes)", H3))
    be = Table([[Paragraph(
        '<font face="Courier" size="8">dissection kit biology anatomy lab pan dissecting tools scalpel scissors forceps probe '
        't-pins stainless steel self healing pad frog earthworm flower owl pellet fetal pig classroom science teacher homeschool '
        'veterinary medical school prep stem ngss</font>', BODY)]],
        colWidths=[CW])
    be.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), HexColor("#F5F5F5")),
        ("LEFTPADDING", (0,0), (-1,-1), 10), ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 8), ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ]))
    s.append(be)

    # ───── Priority actions ─────
    s.append(PageBreak())
    s.append(Paragraph("Priority actions — order of work", H2)); s.append(HRule())
    pri = [
        ("1", "Image #2 — \"What's included\" checklist",
         "Highest single CVR lift. Directly defuses the #1 negative-review theme (incomplete kit). Buyer must SEE the full inventory before they click Add to Cart."),
        ("2", "Image #4 — Stainless-steel close-up + spec strip",
         "Defuses the bottom 4 negative-review themes (rust · dull blades · broken scissors · blade fit). Single biggest \"quality reassurance\" frame."),
        ("3", "Image #1 hero — pan + tools top-down, every tool visible",
         "Makes the kit look complete BEFORE the click. Beats every competitor that shows only the pan in image #1."),
        ("4", "Title rewrite — lead with 'Dissection Kit' + 'Biology'",
         "Two top KWs (2,549 + 386 SV) in the first 80 chars. Current title buries them."),
        ("5", "A+ Module 6 (Q&A) — replacement blades + cleaning + safety",
         "Pre-empts the \"lack of instructions\" review. Teacher procurement reads every Q&A."),
        ("6", "Replacement blades as a cross-sell / FBT bundle",
         "Negative review \"blades dull quickly\" is partially a fact-of-life. Solving it via a cheap replacement pack converts a complaint into AOV."),
    ]
    pt = Table([[Paragraph(f"<b>{n}</b>", BODY), Paragraph(f"<b>{t}</b>", BODY), Paragraph(d, BODY)] for n, t, d in pri],
               colWidths=[0.8*cm, 7.0*cm, CW - 7.8*cm])
    pt.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,-1), GSC_GREEN_D),
        ("TEXTCOLOR", (0,0), (0,-1), WHITE),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LINEBELOW", (0,0), (-1,-1), 0.3, HexColor("#E0DCC8")),
        ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 7), ("BOTTOMPADDING", (0,0), (-1,-1), 7),
        ("ROWBACKGROUNDS", (1,0), (-1,-1), [WHITE, LIGHT_GRN]),
    ]))
    s.append(pt)

    s.append(Spacer(1, 0.4*cm))
    s.append(Paragraph("Open questions for the brand", H3))
    for line in [
        "Exact tool count — confirm the inventory (how many T-pins, how many scalpel blades, scissor type) so the \"What's included\" frame is accurate.",
        "Pad lifespan claim — can we say \"30+ sessions\" with confidence? If yes, that goes in image #3 + bullet 2.",
        "Steel grade — 304 or 410 stainless? If specifiable, it goes in image #4 + bullet 3.",
        "Replacement-blade SKU available? If yes, list as cross-sell.",
        "Safety / certifications — any classroom-safe certifications (ISO, school-approved)? Use as trust badge.",
    ]:
        s.append(Paragraph("· " + line, BODY))

    doc.build(s)
    print(f"PDF: {OUT}")


if __name__ == "__main__":
    build()
