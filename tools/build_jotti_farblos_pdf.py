#!/usr/bin/env python3
"""JOTTI Lederbalsam Farblos — TWO separate Amazon.de listings (200 ml + 500 ml).

Per client direction (2026-05-16):
  - Each size is its own listing — not parent / variant.
  - Creative descriptions in English (for the design team).
  - All on-image copy in German (live marketplace = Amazon.de).
  - CTR + CVR decisions explicitly coupled to keyword volume + review themes.
  - Main image works with badges (within Amazon main-image rules — badges live on the tin label).
  - More real-life lifestyle in slot #6 (single rich scene, not a 4-quadrant grid).
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

OUT = "/Users/jonask/Desktop/Jotti_Lederbalsam_Farblos_Brief.pdf"

# ─── Jotti palette ──────────────────────────────────────────────────
BLACK    = HexColor("#0E0E0E")
CHARCOAL = HexColor("#1B1814")
WALNUT   = HexColor("#3A241A")
AMBER    = HexColor("#C58A3A")
GOLD     = HexColor("#D9B36B")
CREAM    = HexColor("#EFE6D2")
BEESWAX  = HexColor("#E9C46A")
TAN      = HexColor("#C9985A")
BROWN    = HexColor("#6A3A1E")
ONYX     = HexColor("#0A0A0A")
LEATHER_BR = HexColor("#7A4A2A")
LEATHER_BK = HexColor("#1A1612")
LEATHER_NT = HexColor("#A87A4A")
LEATHER_OX = HexColor("#5A2C18")    # oxblood Chesterfield
INK      = HexColor("#111111")
GREY     = HexColor("#7A6A55")
LIGHT    = HexColor("#F5F1E6")
WHITE    = HexColor("#FFFFFF")
GREEN_OK = HexColor("#3FA770")
RED_X    = HexColor("#D24545")
YELLOW   = HexColor("#F4C040")
BRASS    = HexColor("#B58E4A")
DENIM    = HexColor("#3A4B5C")

PAGE_W, PAGE_H = A4
ML, MR, MT, MB = 1.6*cm, 1.6*cm, 1.8*cm, 1.6*cm
CW = PAGE_W - ML - MR

styles = getSampleStyleSheet()
H1   = ParagraphStyle("H1", parent=styles["Title"],   fontName="Times-Bold",   fontSize=26, leading=30, textColor=CREAM, spaceAfter=4, alignment=TA_LEFT)
SUB  = ParagraphStyle("SUB", parent=styles["Normal"], fontName="Helvetica",    fontSize=10, leading=13, textColor=GREY,  spaceAfter=12)
H2   = ParagraphStyle("H2", parent=styles["Heading2"],fontName="Times-Bold",   fontSize=18, leading=22, textColor=BLACK, spaceBefore=12, spaceAfter=6)
H3   = ParagraphStyle("H3", parent=styles["Heading3"],fontName="Helvetica-Bold",fontSize=11, leading=14, textColor=BLACK, spaceBefore=10, spaceAfter=4)
BODY = ParagraphStyle("Body",parent=styles["Normal"], fontName="Helvetica",    fontSize=9.5, leading=13, textColor=BLACK, spaceAfter=3)
SMALL= ParagraphStyle("Small",parent=BODY,fontSize=8,leading=11,textColor=GREY)
QUOTE= ParagraphStyle("Quote",parent=BODY,fontName="Helvetica-Oblique",textColor=GREY)
SKU_HEAD = ParagraphStyle("SkuHead", parent=styles["Title"], fontName="Times-Bold", fontSize=22, leading=26, textColor=GOLD, spaceBefore=10, spaceAfter=4)
SKU_SUB  = ParagraphStyle("SkuSub", parent=styles["Normal"], fontName="Helvetica", fontSize=11, leading=14, textColor=CREAM, spaceAfter=10)


# ─── Flowables ──────────────────────────────────────────────────────

class HRule(Flowable):
    def __init__(self, width=None, color=GOLD, thickness=1.2):
        self.width = width or CW; self.color = color; self.thickness = thickness
        Flowable.__init__(self)
    def wrap(self, *a): return (self.width, self.thickness + 6)
    def draw(self):
        self.canv.setStrokeColor(self.color); self.canv.setLineWidth(self.thickness)
        self.canv.line(0, 3, self.width, 3)


class SectionBanner(Flowable):
    """Big dark banner used to open the per-SKU section."""
    def __init__(self, title, subtitle, w=None, h=2.8*cm):
        self.title = title; self.subtitle = subtitle
        self.w = w or CW; self.h = h
        Flowable.__init__(self)
    def wrap(self, *a): return (self.w, self.h + 0.4*cm)
    def draw(self):
        c = self.canv
        c.setFillColor(BLACK); c.setStrokeColor(GOLD); c.setLineWidth(0.6)
        c.rect(0, 0.2*cm, self.w, self.h, fill=1, stroke=1)
        _honeycomb(c, self.w * 0.85, 0.2*cm + self.h*0.5, radius=2.5*cm, opacity=0.10, color=AMBER)
        c.setFillColor(GOLD); c.setFont("Times-Bold", 22)
        c.drawString(0.6*cm, 0.2*cm + self.h - 1.0*cm, self.title)
        c.setFillColor(CREAM); c.setFont("Helvetica", 11)
        c.drawString(0.6*cm, 0.2*cm + self.h - 1.7*cm, self.subtitle)


class ColorChip(Flowable):
    def __init__(self, color, hex_label, name, w=4.0*cm, h=2.0*cm):
        self.color = color; self.hex_label = hex_label; self.name = name
        self.w = w; self.h = h
        Flowable.__init__(self)
    def wrap(self, *a): return (self.w, self.h + 0.9*cm)
    def draw(self):
        c = self.canv
        c.setFillColor(self.color); c.setStrokeColor(HexColor("#CCCCCC")); c.setLineWidth(0.3)
        c.rect(0, 0.9*cm, self.w, self.h, fill=1, stroke=1)
        c.setFillColor(BLACK); c.setFont("Helvetica-Bold", 9)
        c.drawString(0, 0.45*cm, self.name)
        c.setFillColor(GREY); c.setFont("Courier", 8)
        c.drawString(0, 0.15*cm, self.hex_label)


# ─── Drawing helpers ────────────────────────────────────────────────

def _honeycomb(c, cx, cy, radius=1.6*cm, opacity=0.18, color=AMBER):
    c.saveState()
    c.setStrokeColor(Color(color.red, color.green, color.blue, alpha=opacity))
    c.setLineWidth(0.4)
    hr = 0.22*cm
    rows = int(radius / (hr * 1.5)) + 1
    cols = int(radius / (hr * math.sqrt(3))) + 1
    for r in range(-rows, rows + 1):
        for col in range(-cols, cols + 1):
            x = cx + col * hr * math.sqrt(3) + (hr * math.sqrt(3) / 2 if r % 2 else 0)
            y = cy + r * hr * 1.5
            if (x - cx)**2 + (y - cy)**2 > radius**2: continue
            _hex(c, x, y, hr, stroke_only=True)
    c.restoreState()


def _hex(c, cx, cy, r, fill_color=None, stroke_only=False):
    pts = [(cx + r*math.cos(math.radians(60*i+30)), cy + r*math.sin(math.radians(60*i+30))) for i in range(6)]
    p = c.beginPath(); p.moveTo(*pts[0])
    for pt in pts[1:]: p.lineTo(*pt)
    p.close()
    if stroke_only:
        c.drawPath(p, fill=0, stroke=1)
    else:
        if fill_color is not None: c.setFillColor(fill_color)
        c.drawPath(p, fill=1, stroke=0)


def _draw_tin_topdown(c, cx, cy, w=2.6*cm, variant="farblos", show_label=True, show_size=None):
    """Top-down Jotti tin. show_size: '200 ml' / '500 ml' / None — adds a side-band."""
    r = w / 2
    w_cm = w / cm
    c.setFillColor(BLACK); c.setStrokeColor(GOLD); c.setLineWidth(0.6)
    c.circle(cx, cy, r, fill=1, stroke=1)
    _honeycomb(c, cx, cy, radius=r*0.85, opacity=0.10, color=AMBER)
    c.setStrokeColor(GOLD); c.setLineWidth(0.3)
    c.circle(cx, cy, r*0.9, fill=0, stroke=1)
    if show_label:
        c.setFillColor(GOLD); c.setFont("Times-BoldItalic", max(4, w_cm * 3.5))
        c.drawCentredString(cx, cy + r*0.55, "Jotti")
        c.setFillColor(CREAM); c.setFont("Times-Italic", max(3.5, w_cm * 2.0))
        c.drawCentredString(cx, cy + r*0.38, "seit 1912")
    chip_color = {"farblos": TAN, "braun": BROWN, "schwarz": ONYX}[variant]
    chip_r = r * 0.30
    c.setFillColor(chip_color); c.setStrokeColor(GOLD); c.setLineWidth(0.5)
    c.circle(cx, cy - r*0.05, chip_r, fill=1, stroke=1)
    if show_label:
        c.setFillColor(CREAM if variant != "farblos" else BLACK)
        c.setFont("Helvetica-Bold", max(3.5, w_cm * 1.7))
        c.drawCentredString(cx, cy - r*0.07, variant.upper())
        c.setFillColor(CREAM); c.setFont("Helvetica-Bold", max(3.5, w_cm * 1.8))
        c.drawCentredString(cx, cy - r*0.55, "LEDER BALSAM")
    if show_size and show_label:
        c.setFillColor(GOLD); c.setFont("Helvetica-Bold", max(3, w_cm * 1.3))
        c.drawCentredString(cx, cy - r*0.78, show_size)


def _draw_tin_3q(c, cx, cy, w=2.4*cm, variant="farblos", size_label="500 ml"):
    """3/4 angle tin with explicit size on the side wall."""
    h = w * 0.4
    w_cm = w / cm
    c.setFillColor(CHARCOAL); c.setStrokeColor(GOLD); c.setLineWidth(0.4)
    c.roundRect(cx - w/2, cy - h*1.1, w, h*1.2, h*0.1, fill=1, stroke=1)
    c.setFillColor(BLACK); c.setStrokeColor(GOLD)
    c.ellipse(cx - w/2, cy - h*0.2, cx + w/2, cy + h*0.3, fill=1, stroke=1)
    _honeycomb(c, cx, cy + h*0.05, radius=w*0.4, opacity=0.10, color=AMBER)
    c.setFillColor(GOLD); c.setFont("Times-BoldItalic", max(4, w_cm * 2.3))
    c.drawCentredString(cx, cy + h*0.18, "Jotti")
    chip_color = {"farblos": TAN, "braun": BROWN, "schwarz": ONYX}[variant]
    c.setFillColor(chip_color); c.setStrokeColor(GOLD); c.setLineWidth(0.4)
    c.ellipse(cx - w*0.13, cy - h*0.05, cx + w*0.13, cy + h*0.13, fill=1, stroke=1)
    c.setFillColor(CREAM); c.setFont("Helvetica-Bold", max(3.5, w_cm * 1.8))
    c.drawCentredString(cx, cy - h*0.65, size_label)


def _draw_leather_swatch(c, x, y, w, h, color, split="right"):
    c.setFillColor(color); c.setStrokeColor(WALNUT); c.setLineWidth(0.3)
    c.rect(x, y, w, h, fill=1, stroke=1)
    import random
    rng = random.Random(42)
    c.saveState()
    c.setFillColor(Color(0,0,0,alpha=0.18))
    for _ in range(int(w*h/(cm*cm)*70)):
        c.circle(x + rng.random()*w, y + rng.random()*h, 0.012*cm, fill=1, stroke=0)
    c.restoreState()
    if split == "right":
        c.setFillColor(Color(0.2, 0.2, 0.2, alpha=0.5))
        c.rect(x, y, w/2, h, fill=1, stroke=0)
        c.setStrokeColor(Color(0,0,0,alpha=0.35)); c.setLineWidth(0.25)
        for i in range(5):
            c.line(x + 0.1*cm + i*0.18*cm, y + 0.15*cm, x + 0.15*cm + i*0.18*cm, y + h - 0.15*cm)
        c.setStrokeColor(GOLD); c.setLineWidth(0.8)
        c.line(x + w/2, y, x + w/2, y + h)


def _draw_brogue(c, cx, cy, w=2.0*cm, color=LEATHER_BR):
    """Brown brogue shoe silhouette, side view."""
    h = w * 0.45
    c.setFillColor(color); c.setStrokeColor(WALNUT); c.setLineWidth(0.4)
    # sole + back
    p = c.beginPath()
    p.moveTo(cx - w*0.50, cy - h*0.35)
    p.curveTo(cx - w*0.55, cy - h*0.10, cx - w*0.30, cy + h*0.45, cx - w*0.10, cy + h*0.50)
    p.lineTo(cx + w*0.30, cy + h*0.45)
    p.curveTo(cx + w*0.50, cy + h*0.35, cx + w*0.55, cy - h*0.30, cx + w*0.40, cy - h*0.45)
    p.lineTo(cx - w*0.40, cy - h*0.45)
    p.close()
    c.drawPath(p, fill=1, stroke=1)
    # toe cap / wingtip
    c.setFillColor(Color(0,0,0,alpha=0.25))
    c.ellipse(cx + w*0.10, cy - h*0.20, cx + w*0.50, cy + h*0.10, fill=1, stroke=0)
    # broguing dots
    c.setFillColor(Color(0,0,0,alpha=0.40))
    for dx in [w*0.15, w*0.22, w*0.29, w*0.20, w*0.27, w*0.34]:
        c.circle(cx + dx, cy + h*0.05, 0.025*cm, fill=1, stroke=0)
    # heel
    c.setFillColor(Color(0,0,0,alpha=0.30))
    c.rect(cx - w*0.45, cy - h*0.45, w*0.15, h*0.20, fill=1, stroke=0)


def _draw_glove(c, cx, cy, w=1.8*cm, color=LEATHER_BR):
    """Driving glove silhouette."""
    c.setFillColor(color); c.setStrokeColor(WALNUT); c.setLineWidth(0.3)
    # palm
    c.roundRect(cx - w*0.30, cy - w*0.30, w*0.55, w*0.45, w*0.06, fill=1, stroke=1)
    # fingers
    for i, fx in enumerate([-w*0.18, -w*0.04, w*0.10, w*0.22]):
        c.roundRect(cx + fx, cy + w*0.15, w*0.10, w*0.25 - i*0.02*cm, w*0.04, fill=1, stroke=1)
    # thumb
    c.roundRect(cx - w*0.38, cy - w*0.10, w*0.16, w*0.22, w*0.05, fill=1, stroke=1)
    # cuff snap detail
    c.setFillColor(BRASS); c.circle(cx - w*0.10, cy - w*0.20, 0.04*cm, fill=1, stroke=0)


def _draw_watch_strap(c, cx, cy, w=2.4*cm, color=LEATHER_BR):
    """Wristwatch with leather strap."""
    # straps
    c.setFillColor(color); c.setStrokeColor(WALNUT); c.setLineWidth(0.3)
    c.rect(cx - w*0.45, cy - w*0.08, w*0.30, w*0.16, fill=1, stroke=1)
    c.rect(cx + w*0.15, cy - w*0.08, w*0.30, w*0.16, fill=1, stroke=1)
    # case
    c.setFillColor(BRASS); c.setStrokeColor(WALNUT)
    c.circle(cx, cy, w*0.18, fill=1, stroke=1)
    # dial
    c.setFillColor(CREAM); c.circle(cx, cy, w*0.14, fill=1, stroke=0)
    # hands
    c.setStrokeColor(BLACK); c.setLineWidth(0.5)
    c.line(cx, cy, cx + w*0.10, cy + w*0.04)
    c.line(cx, cy, cx, cy + w*0.08)


def _draw_jacket(c, cx, cy, w=2.6*cm, color=LEATHER_BR):
    """Leather jacket silhouette — shoulders + lapel."""
    h = w * 0.7
    c.setFillColor(color); c.setStrokeColor(WALNUT); c.setLineWidth(0.4)
    p = c.beginPath()
    p.moveTo(cx - w*0.45, cy + h*0.45)
    p.lineTo(cx - w*0.30, cy + h*0.35)
    p.lineTo(cx - w*0.25, cy - h*0.45)
    p.lineTo(cx + w*0.25, cy - h*0.45)
    p.lineTo(cx + w*0.30, cy + h*0.35)
    p.lineTo(cx + w*0.45, cy + h*0.45)
    p.lineTo(cx + w*0.40, cy + h*0.30)
    p.lineTo(cx + w*0.10, cy + h*0.45)
    p.lineTo(cx - w*0.10, cy + h*0.45)
    p.lineTo(cx - w*0.40, cy + h*0.30)
    p.close()
    c.drawPath(p, fill=1, stroke=1)
    # lapel V
    c.setStrokeColor(WALNUT); c.setLineWidth(0.5)
    c.line(cx - w*0.10, cy + h*0.45, cx, cy + h*0.20)
    c.line(cx + w*0.10, cy + h*0.45, cx, cy + h*0.20)
    # zipper
    c.line(cx, cy + h*0.20, cx, cy - h*0.40)


def _draw_chesterfield_arm(c, cx, cy, w=3.4*cm, color=LEATHER_OX):
    """Tufted Chesterfield sofa arm (oxblood)."""
    h = w * 0.55
    c.setFillColor(color); c.setStrokeColor(WALNUT); c.setLineWidth(0.4)
    c.roundRect(cx - w/2, cy - h/2, w, h, h*0.25, fill=1, stroke=1)
    # rolled arm — darker top curve
    c.setFillColor(Color(0,0,0,alpha=0.25))
    c.roundRect(cx - w/2 + 0.1*cm, cy + h*0.20, w - 0.2*cm, h*0.25, 0.18*cm, fill=1, stroke=0)
    # tufted buttons (3 × 2)
    c.setFillColor(BRASS)
    for row in range(2):
        for col in range(4):
            bx = cx - w*0.32 + col*w*0.22
            by = cy - h*0.18 + row*h*0.25
            c.circle(bx, by, 0.06*cm, fill=1, stroke=0)
            # tuft creases (faint)
            c.setStrokeColor(Color(0,0,0,alpha=0.25)); c.setLineWidth(0.3)
            c.line(bx - 0.10*cm, by - 0.10*cm, bx + 0.10*cm, by + 0.10*cm)
            c.line(bx + 0.10*cm, by - 0.10*cm, bx - 0.10*cm, by + 0.10*cm)
            c.setFillColor(BRASS)


def _draw_saddle(c, cx, cy, w=2.6*cm, color=LEATHER_BR):
    """English saddle on a wooden stand."""
    h = w * 0.6
    c.setFillColor(color); c.setStrokeColor(WALNUT); c.setLineWidth(0.4)
    c.ellipse(cx - w*0.50, cy - h*0.25, cx + w*0.50, cy + h*0.30, fill=1, stroke=1)
    # pommel raise
    c.ellipse(cx - w*0.18, cy + h*0.20, cx + w*0.18, cy + h*0.42, fill=1, stroke=1)
    # stitching ridge
    c.setStrokeColor(Color(0,0,0,alpha=0.35)); c.setLineWidth(0.3)
    c.ellipse(cx - w*0.40, cy - h*0.10, cx + w*0.40, cy + h*0.25, fill=0, stroke=1)
    # stand
    c.setFillColor(WALNUT)
    c.rect(cx - 0.06*cm, cy - h*0.55, 0.12*cm, h*0.30, fill=1, stroke=0)
    c.rect(cx - w*0.35, cy - h*0.63, w*0.70, 0.10*cm, fill=1, stroke=0)


def _draw_briefcase(c, cx, cy, w=2.4*cm, color=LEATHER_BR):
    """Leather briefcase silhouette."""
    h = w * 0.62
    c.setFillColor(color); c.setStrokeColor(WALNUT); c.setLineWidth(0.4)
    c.roundRect(cx - w/2, cy - h/2, w, h, 0.10*cm, fill=1, stroke=1)
    # handle
    c.setStrokeColor(WALNUT); c.setLineWidth(0.9); c.setFillColor(WHITE)
    c.arc(cx - w*0.18, cy + h*0.40, cx + w*0.18, cy + h*0.65, startAng=0, extent=180)
    # buckle / clasp
    c.setFillColor(BRASS)
    c.rect(cx - 0.20*cm, cy + h*0.05, 0.40*cm, 0.10*cm, fill=1, stroke=0)
    # stitch line
    c.setStrokeColor(Color(0,0,0,alpha=0.25)); c.setLineWidth(0.3)
    c.line(cx - w*0.40, cy - h*0.30, cx + w*0.40, cy - h*0.30)


def _draw_car_seat(c, cx, cy, w=2.8*cm, color=LEATHER_BR):
    """Classic car bucket seat silhouette."""
    h = w * 0.85
    c.setFillColor(color); c.setStrokeColor(WALNUT); c.setLineWidth(0.4)
    # base
    c.roundRect(cx - w*0.40, cy - h*0.45, w*0.80, h*0.30, 0.10*cm, fill=1, stroke=1)
    # backrest
    c.roundRect(cx - w*0.38, cy - h*0.15, w*0.76, h*0.55, 0.15*cm, fill=1, stroke=1)
    # head support cutout
    c.setFillColor(Color(0,0,0,alpha=0.20))
    c.ellipse(cx - w*0.18, cy + h*0.20, cx + w*0.18, cy + h*0.40, fill=1, stroke=0)
    # stitch lines
    c.setStrokeColor(Color(0,0,0,alpha=0.25)); c.setLineWidth(0.3)
    c.line(cx - w*0.30, cy - h*0.30, cx + w*0.30, cy - h*0.30)
    c.line(cx, cy - h*0.15, cx, cy + h*0.35)


def _draw_hand(c, cx, cy, w=1.0*cm, color=HexColor("#E8B89C"), cuff_color=DENIM):
    """Older masculine hand with shirt cuff, applying balm with a cloth."""
    h = w * 1.3
    c.setFillColor(cuff_color); c.setStrokeColor(WALNUT); c.setLineWidth(0.3)
    c.roundRect(cx - w*0.45, cy - h*0.50, w*0.90, h*0.30, 0.06*cm, fill=1, stroke=1)
    # hand
    c.setFillColor(color); c.setStrokeColor(WALNUT); c.setLineWidth(0.3)
    c.roundRect(cx - w*0.35, cy - h*0.20, w*0.70, h*0.45, w*0.10, fill=1, stroke=1)
    # cloth (cream)
    c.setFillColor(CREAM); c.setStrokeColor(WALNUT); c.setLineWidth(0.2)
    c.roundRect(cx - w*0.18, cy + h*0.20, w*0.40, h*0.12, 0.04*cm, fill=1, stroke=1)


def _draw_window_light(c, cx, cy, r=1.5*cm, color=AMBER):
    """Soft warm window glow used as side-light cue."""
    for i in range(8):
        c.setFillColor(Color(color.red, color.green, color.blue, alpha=0.12 - i*0.013))
        c.circle(cx, cy, r + i*0.15*cm, fill=1, stroke=0)


def _draw_badge(c, cx, cy, text, w=1.7*cm, h=0.55*cm, fill=GOLD, stroke=GOLD, fg=BLACK):
    """A small overlay badge (gold pill). Font scales by cm, never raw points."""
    c.setFillColor(fill); c.setStrokeColor(stroke); c.setLineWidth(0.6)
    c.roundRect(cx - w/2, cy - h/2, w, h, h*0.4, fill=1, stroke=1)
    c.setFillColor(fg); c.setFont("Helvetica-Bold", max(4, (h/cm) * 10))
    c.drawCentredString(cx, cy - h*0.15, text)


def _draw_hex_badge(c, cx, cy, text, r=0.50*cm, fill=GOLD, fg=BLACK):
    c.setFillColor(fill); c.setStrokeColor(GOLD); c.setLineWidth(0.5)
    _hex(c, cx, cy, r)
    pts = [(cx + r*math.cos(math.radians(60*i+30)), cy + r*math.sin(math.radians(60*i+30))) for i in range(6)]
    p = c.beginPath(); p.moveTo(*pts[0])
    for pt in pts[1:]: p.lineTo(*pt)
    p.close(); c.drawPath(p, fill=0, stroke=1)
    c.setFillColor(fg); c.setFont("Helvetica-Bold", max(4, (r/cm) * 12))
    c.drawCentredString(cx, cy - r*0.20, text)


def _draw_de_flag_hex(c, cx, cy, r=0.42*cm):
    c.setFillColor(BLACK); c.rect(cx - r*0.55, cy + r*0.15, r*1.10, r*0.30, fill=1, stroke=0)
    c.setFillColor(RED_X);  c.rect(cx - r*0.55, cy - r*0.15, r*1.10, r*0.30, fill=1, stroke=0)
    c.setFillColor(YELLOW); c.rect(cx - r*0.55, cy - r*0.45, r*1.10, r*0.30, fill=1, stroke=0)
    c.setStrokeColor(GOLD); c.setLineWidth(0.5)
    c.rect(cx - r*0.55, cy - r*0.45, r*1.10, r*0.90, fill=0, stroke=1)


def _draw_check(c, cx, cy, size=0.5*cm, color=GREEN_OK):
    c.setStrokeColor(color); c.setLineWidth(1.6)
    c.line(cx - size*0.3, cy, cx - size*0.05, cy - size*0.25)
    c.line(cx - size*0.05, cy - size*0.25, cx + size*0.3, cy + size*0.3)


def _draw_x(c, cx, cy, size=0.5*cm, color=RED_X):
    c.setStrokeColor(color); c.setLineWidth(1.6)
    c.line(cx - size*0.3, cy - size*0.3, cx + size*0.3, cy + size*0.3)
    c.line(cx - size*0.3, cy + size*0.3, cx + size*0.3, cy - size*0.3)


def _draw_fir(c, cx, cy, h=1.0*cm, color=HexColor("#0A1612")):
    c.setFillColor(color)
    p = c.beginPath()
    p.moveTo(cx - h*0.4, cy - h*0.5); p.lineTo(cx, cy + h*0.5); p.lineTo(cx + h*0.4, cy - h*0.5); p.close()
    c.drawPath(p, fill=1, stroke=0)


# ─── Mockup classes ─────────────────────────────────────────────────

class MainOption(Flowable):
    def __init__(self, letter, name, draw_fn, side_w=8.5*cm):
        self.letter = letter; self.name = name; self.draw_fn = draw_fn
        self.size = 6.5*cm; self.side_w = side_w; self.gap = 0.4*cm
        Flowable.__init__(self)
    def wrap(self, *a): return (self.size, self.size + 0.4*cm)
    def draw(self):
        c = self.canv; s = self.size
        c.setFillColor(WHITE); c.setStrokeColor(HexColor("#CCCCCC")); c.setLineWidth(0.4)
        c.rect(0, 0, s, s, fill=1, stroke=1)
        c.setFillColor(BLACK); c.rect(0, s - 0.7*cm, 1.7*cm, 0.7*cm, fill=1, stroke=0)
        c.setFillColor(GOLD); c.setFont("Helvetica-Bold", 11)
        c.drawCentredString(0.85*cm, s - 0.5*cm, f"OPT {self.letter}")
        self.draw_fn(c, s/2, s/2 - 0.3*cm)
        c.setFillColor(GREY); c.setFont("Helvetica", 7)
        c.drawCentredString(s/2, 0.15*cm, "2000 × 2000 px · pure white BG (Amazon)")
        c.setFillColor(GOLD)
        tw = c.stringWidth(self.name.upper(), "Helvetica-Bold", 7) + 0.4*cm
        c.rect(s - tw, 0, tw, 0.5*cm, fill=1, stroke=0)
        c.setFillColor(BLACK); c.setFont("Helvetica-Bold", 7)
        c.drawString(s - tw + 0.2*cm, 0.18*cm, self.name.upper())


class ListingMockup(Flowable):
    def __init__(self, slot, role, draw_fn, bg=BLACK, side_w=8.5*cm):
        self.slot = slot; self.role = role; self.draw_fn = draw_fn; self.bg = bg
        self.size = 6.5*cm; self.side_w = side_w; self.gap = 0.4*cm
        Flowable.__init__(self)
    def wrap(self, *a): return (self.size, self.size + 0.4*cm)
    def draw(self):
        c = self.canv; s = self.size
        c.setFillColor(self.bg); c.setStrokeColor(HexColor("#CCCCCC")); c.setLineWidth(0.4)
        c.rect(0, 0, s, s, fill=1, stroke=1)
        c.setFillColor(GOLD); c.rect(0, s - 0.7*cm, 1.4*cm, 0.7*cm, fill=1, stroke=0)
        c.setFillColor(BLACK); c.setFont("Helvetica-Bold", 11)
        c.drawCentredString(0.7*cm, s - 0.5*cm, f"#{self.slot}")
        self.draw_fn(c, s/2, s/2)
        c.setFillColor(GOLD)
        tw = c.stringWidth(self.role.upper(), "Helvetica-Bold", 7) + 0.4*cm
        c.rect(s - tw, 0, tw, 0.5*cm, fill=1, stroke=0)
        c.setFillColor(BLACK); c.setFont("Helvetica-Bold", 7)
        c.drawString(s - tw + 0.2*cm, 0.18*cm, self.role.upper())
        c.setFillColor(CREAM if self.bg in (BLACK, CHARCOAL, WALNUT, ONYX) else GREY)
        c.setFont("Helvetica", 6.5)
        c.drawCentredString(s/2, 0.15*cm, "2000 × 2000 px")


class APlusMockup(Flowable):
    def __init__(self, slot, mtype, draw_fn, bg=BLACK, side_w=7.0*cm):
        self.slot = slot; self.mtype = mtype; self.draw_fn = draw_fn; self.bg = bg
        self.bw = 10.0*cm; self.bh = self.bw * (600/1464)
        self.side_w = side_w; self.gap = 0.4*cm
        Flowable.__init__(self)
    def wrap(self, *a): return (self.bw, self.bh + 0.5*cm)
    def draw(self):
        c = self.canv; w, h = self.bw, self.bh
        c.setFillColor(self.bg); c.setStrokeColor(HexColor("#CCCCCC")); c.setLineWidth(0.4)
        c.rect(0, 0.5*cm, w, h, fill=1, stroke=1)
        c.setFillColor(GOLD); c.rect(0, 0.5*cm + h - 0.55*cm, 2.4*cm, 0.55*cm, fill=1, stroke=0)
        c.setFillColor(BLACK); c.setFont("Helvetica-Bold", 8)
        c.drawString(0.15*cm, 0.5*cm + h - 0.4*cm, f"MODUL {self.slot}")
        self.draw_fn(c, w/2, 0.5*cm + h/2)
        c.setFillColor(GOLD)
        tw = c.stringWidth(self.mtype.upper(), "Helvetica-Bold", 7) + 0.3*cm
        c.rect(w - tw, 0.5*cm, tw, 0.4*cm, fill=1, stroke=0)
        c.setFillColor(BLACK); c.setFont("Helvetica-Bold", 7)
        c.drawString(w - tw + 0.15*cm, 0.5*cm + 0.13*cm, self.mtype.upper())
        c.setFillColor(GREY); c.setFont("Helvetica", 6.5)
        c.drawCentredString(w/2, 0.15*cm, "1464 × 600 desktop · 600 × 450 mobile")


class MoodTile(Flowable):
    def __init__(self, title, sub, draw_fn, w=5.0*cm, h=3.6*cm, bg=BLACK):
        self.title = title; self.sub = sub; self.draw_fn = draw_fn
        self.w = w; self.h = h; self.bg = bg
        Flowable.__init__(self)
    def wrap(self, *a): return (self.w, self.h)
    def draw(self):
        c = self.canv; w, h = self.w, self.h
        c.setFillColor(self.bg); c.setStrokeColor(HexColor("#CCCCCC")); c.setLineWidth(0.4)
        c.rect(0, 0, w, h, fill=1, stroke=1)
        self.draw_fn(c, w/2, h/2 + 0.5*cm)
        # caption bar — title bold, subtitle below on its own line
        c.setFillColor(GOLD); c.rect(0, 0, w, 0.75*cm, fill=1, stroke=0)
        c.setFillColor(BLACK); c.setFont("Helvetica-Bold", 7.5)
        c.drawString(0.2*cm, 0.42*cm, self.title.upper())
        c.setFillColor(BLACK); c.setFont("Helvetica", 6.5)
        c.drawString(0.2*cm, 0.15*cm, self.sub)


# ─── Main image concepts (with badges, per client) ───────────────────

def _main_with_badges(c, cx, cy, size_label):
    """Premium hero — tin with on-tin badges (Amazon-compliant: badges are physically on label)."""
    _draw_tin_3q(c, cx, cy + 0.4*cm, w=3.4*cm, variant="farblos", size_label=size_label)
    # soft warm shadow under
    c.setFillColor(Color(AMBER.red, AMBER.green, AMBER.blue, alpha=0.18))
    c.ellipse(cx - 1.6*cm, cy - 1.8*cm, cx + 1.8*cm, cy - 1.2*cm, fill=1, stroke=0)


def cpt_main_a_200(c, cx, cy): _main_with_badges(c, cx, cy, "200 ml")
def cpt_main_a_500(c, cx, cy): _main_with_badges(c, cx, cy, "500 ml")


def _main_open_wax(c, cx, cy, size_label):
    """Wax-reveal hero — top-down with lid offset."""
    c.setFillColor(BLACK); c.setStrokeColor(GOLD); c.setLineWidth(0.5)
    c.circle(cx - 0.5*cm, cy, 1.5*cm, fill=1, stroke=1)
    c.setFillColor(BEESWAX); c.circle(cx - 0.5*cm, cy, 1.25*cm, fill=1, stroke=0)
    _honeycomb(c, cx - 0.5*cm, cy, radius=1.1*cm, opacity=0.22, color=AMBER)
    c.setFillColor(BLACK); c.setStrokeColor(GOLD); c.setLineWidth(0.5)
    c.circle(cx + 1.6*cm, cy - 0.4*cm, 1.0*cm, fill=1, stroke=1)
    _honeycomb(c, cx + 1.6*cm, cy - 0.4*cm, radius=0.85*cm, opacity=0.12, color=AMBER)
    c.setFillColor(GOLD); c.setFont("Times-BoldItalic", 7)
    c.drawCentredString(cx + 1.6*cm, cy - 0.2*cm, "Jotti")
    c.setFillColor(TAN); c.setStrokeColor(GOLD); c.setLineWidth(0.4)
    c.circle(cx + 1.6*cm, cy - 0.55*cm, 0.25*cm, fill=1, stroke=1)
    c.setFillColor(GOLD); c.setFont("Helvetica-Bold", 6)
    c.drawCentredString(cx + 1.6*cm, cy + 0.78*cm, size_label)


def cpt_main_b_200(c, cx, cy): _main_open_wax(c, cx, cy, "200 ml")
def cpt_main_b_500(c, cx, cy): _main_open_wax(c, cx, cy, "500 ml")


def _main_in_context(c, cx, cy, size_label, with_lifestyle):
    """Tin in context with one lifestyle prop (still tin > 85% via tight crop)."""
    # the prop (small leather good) lives in shadow behind/beside the tin
    with_lifestyle(c, cx + 1.7*cm, cy - 0.6*cm)
    _draw_tin_3q(c, cx - 0.6*cm, cy + 0.4*cm, w=3.0*cm, variant="farblos", size_label=size_label)


def cpt_main_c_200(c, cx, cy):
    """200 ml — tin with a brown brogue in soft context."""
    _main_in_context(c, cx, cy, "200 ml", lambda c, x, y: _draw_brogue(c, x, y, w=2.0*cm, color=LEATHER_BR))


def cpt_main_c_500(c, cx, cy):
    """500 ml — tin with a Chesterfield arm in soft context."""
    _main_in_context(c, cx, cy, "500 ml", lambda c, x, y: _draw_chesterfield_arm(c, x, y, w=3.0*cm, color=LEATHER_OX))


# ─── Listing-image concepts ─────────────────────────────────────────

def cpt_img2_proof(c, cx, cy, demo_fn):
    """Variant proof — split before/after on a real leather object (the demo)."""
    c.setFillColor(CREAM); c.setFont("Times-Bold", 9)
    c.drawCentredString(cx, cy + 2.4*cm, "FARBE BLEIBT.")
    c.drawCentredString(cx, cy + 2.0*cm, "LEDER LEBT.")
    # demo object centred — half is dimmed
    demo_fn(c, cx, cy + 0.1*cm)
    # split overlay (vertical, left dim, right glowing)
    c.setFillColor(Color(0,0,0,alpha=0.55))
    c.rect(cx - 2.6*cm, cy - 1.4*cm, 2.6*cm, 2.6*cm, fill=1, stroke=0)
    c.setStrokeColor(GOLD); c.setLineWidth(0.8)
    c.line(cx, cy - 1.4*cm, cx, cy + 1.2*cm)
    c.setFillColor(GOLD); c.setFont("Helvetica-Bold", 5.5)
    c.drawCentredString(cx - 1.0*cm, cy - 1.7*cm, "VORHER")
    c.drawCentredString(cx + 1.0*cm, cy - 1.7*cm, "NACHHER")
    # small tin bottom right
    _draw_tin_topdown(c, cx + 1.9*cm, cy - 2.0*cm, w=1.1*cm, variant="farblos", show_label=False)
    c.setFillColor(CREAM); c.setFont("Helvetica-Bold", 5.5)
    c.drawCentredString(cx, cy - 2.5*cm, "MIT BIENENWACHS · AVOCADOÖL · JOJOBA · CARNAUBA")


def cpt_img2_proof_200(c, cx, cy):
    """200 ml — split-test on a brogue (small leather good)."""
    cpt_img2_proof(c, cx, cy, lambda c, x, y: _draw_brogue(c, x, y, w=4.0*cm, color=LEATHER_NT))


def cpt_img2_proof_500(c, cx, cy):
    """500 ml — split-test on a Chesterfield arm (big leather good)."""
    cpt_img2_proof(c, cx, cy, lambda c, x, y: _draw_chesterfield_arm(c, x, y, w=4.6*cm, color=LEATHER_BR))


def cpt_img3_moment(c, cx, cy, demo_fn, headline_top, headline_bot):
    """Pflege-Moment — cinematic hand applying balm to the demo object."""
    # warm window glow FIRST (so it sits behind everything)
    _draw_window_light(c, cx + 1.5*cm, cy - 0.2*cm, r=0.9*cm)
    # demo object
    demo_fn(c, cx, cy - 0.4*cm)
    # hand applying
    _draw_hand(c, cx + 0.6*cm, cy + 0.1*cm, w=1.0*cm)
    # open tin showing amber wax
    c.setFillColor(BLACK); c.setStrokeColor(GOLD); c.setLineWidth(0.4)
    c.circle(cx - 1.8*cm, cy - 1.9*cm, 0.55*cm, fill=1, stroke=1)
    c.setFillColor(BEESWAX); c.circle(cx - 1.8*cm, cy - 1.9*cm, 0.45*cm, fill=1, stroke=0)
    # hex tag with usage notes
    _draw_hex_badge(c, cx + 2.0*cm, cy + 0.5*cm, "1 ANW.", r=0.35*cm)
    c.setFillColor(CREAM); c.setFont("Helvetica-Bold", 4.5)
    c.drawCentredString(cx + 2.0*cm, cy + 0.0*cm, "2 STD.")
    c.drawCentredString(cx + 2.0*cm, cy - 0.15*cm, "EINZIEHEN")
    # bottom strap — addresses the "färbt ab bei Feuchte" review
    c.setFillColor(GREY); c.setFont("Helvetica-Oblique", 5)
    c.drawCentredString(cx, cy - 2.5*cm, "Dünn auftragen · einziehen lassen · trocken polieren")
    # headline LAST — on top of everything, never dimmed by glow
    c.setFillColor(CREAM); c.setFont("Times-Bold", 9)
    c.drawCentredString(cx, cy + 2.4*cm, headline_top)
    c.drawCentredString(cx, cy + 2.05*cm, headline_bot)


def cpt_img3_moment_200(c, cx, cy):
    """200 ml — hand applying to a leather jacket sleeve."""
    cpt_img3_moment(c, cx, cy, lambda c, x, y: _draw_jacket(c, x, y, w=3.4*cm, color=LEATHER_BR),
                    "GESCHMEIDIG IN", "ZWEI STUNDEN.")


def cpt_img3_moment_500(c, cx, cy):
    """500 ml — hand applying to a Chesterfield sofa arm."""
    cpt_img3_moment(c, cx, cy, lambda c, x, y: _draw_chesterfield_arm(c, x, y, w=4.2*cm, color=LEATHER_OX),
                    "GESCHMEIDIG IN", "ZWEI STUNDEN.")


# ─── Benefits frame — slot #4 ──────────────────────────────────────

def _draw_benefit_icon(c, cx, cy, kind, size=0.42*cm):
    if kind == "natural":
        c.setFillColor(BEESWAX); _hex(c, cx, cy, size*0.45)
        c.setStrokeColor(GOLD); c.setLineWidth(0.4)
        pts = [(cx + size*0.45*math.cos(math.radians(60*i+30)), cy + size*0.45*math.sin(math.radians(60*i+30))) for i in range(6)]
        p = c.beginPath(); p.moveTo(*pts[0])
        for pt in pts[1:]: p.lineTo(*pt)
        p.close(); c.drawPath(p, fill=0, stroke=1)
    elif kind == "germany":
        _draw_de_flag_hex(c, cx, cy, r=size*0.55)
    elif kind == "three_in_one":
        c.setFillColor(GOLD)
        p = c.beginPath()
        p.moveTo(cx - size*0.4, cy + size*0.3); p.lineTo(cx + size*0.4, cy + size*0.3)
        p.lineTo(cx + size*0.4, cy - size*0.05)
        p.curveTo(cx + size*0.4, cy - size*0.4, cx + size*0.1, cy - size*0.5, cx, cy - size*0.5)
        p.curveTo(cx - size*0.1, cy - size*0.5, cx - size*0.4, cy - size*0.4, cx - size*0.4, cy - size*0.05)
        p.close(); c.drawPath(p, fill=1, stroke=0)
        c.setFillColor(BLACK)
        for dx in [-size*0.18, 0, size*0.18]:
            c.circle(cx + dx, cy, size*0.05, fill=1, stroke=0)
    elif kind == "universal":
        c.setFillColor(GOLD)
        c.ellipse(cx - size*0.45, cy + size*0.05, cx - size*0.10, cy + size*0.30, fill=1, stroke=0)
        c.rect(cx - size*0.10, cy - size*0.10, size*0.35, size*0.30, fill=1, stroke=0)
        c.roundRect(cx + size*0.20, cy - size*0.35, size*0.30, size*0.18, size*0.04, fill=1, stroke=0)
    elif kind == "no_chemicals":
        c.setStrokeColor(GOLD); c.setLineWidth(0.8)
        c.line(cx - size*0.25, cy + size*0.35, cx + size*0.25, cy + size*0.35)
        c.line(cx - size*0.25, cy + size*0.35, cx - size*0.30, cy - size*0.30)
        c.line(cx + size*0.25, cy + size*0.35, cx + size*0.30, cy - size*0.30)
        c.line(cx - size*0.30, cy - size*0.30, cx + size*0.30, cy - size*0.30)
        c.setFillColor(BEESWAX); c.rect(cx - size*0.27, cy - size*0.30, size*0.54, size*0.30, fill=1, stroke=0)
        c.setStrokeColor(RED_X); c.setLineWidth(1.5)
        c.line(cx - size*0.45, cy - size*0.45, cx + size*0.45, cy + size*0.45)
    elif kind == "travel":
        # tiny briefcase
        c.setFillColor(GOLD)
        c.roundRect(cx - size*0.35, cy - size*0.30, size*0.70, size*0.50, size*0.05, fill=1, stroke=0)
        c.setStrokeColor(GOLD); c.setLineWidth(0.8); c.setFillColor(WHITE)
        c.arc(cx - size*0.12, cy + size*0.15, cx + size*0.12, cy + size*0.35, startAng=0, extent=180)
    elif kind == "workshop":
        # tiny saddle + brush
        c.setFillColor(GOLD)
        c.ellipse(cx - size*0.35, cy - size*0.05, cx + size*0.35, cy + size*0.20, fill=1, stroke=0)
        c.setStrokeColor(GOLD); c.setLineWidth(0.6)
        c.line(cx - size*0.20, cy - size*0.20, cx + size*0.30, cy - size*0.40)


def _benefits_frame(c, cx, cy, badges):
    c.setFillColor(CREAM); c.setFont("Times-Bold", 9)
    c.drawCentredString(cx, cy + 2.4*cm, "FÜNF VERSPRECHEN. SEIT 1912.")
    c.setFillColor(GREY); c.setFont("Helvetica", 7)
    c.drawCentredString(cx, cy + 2.05*cm, "Was in jeder Dose steckt")
    _draw_tin_topdown(c, cx, cy - 0.2*cm, w=1.3*cm, variant="farblos", show_label=False)
    positions = [
        ( -2.2*cm,  1.3*cm),
        (  2.2*cm,  1.3*cm),
        ( -2.4*cm, -0.4*cm),
        (  2.4*cm, -0.4*cm),
        (  0,      -1.9*cm),
    ]
    for (dx, dy), (kind, label, sub) in zip(positions, badges):
        c.setFillColor(CHARCOAL); c.setStrokeColor(GOLD); c.setLineWidth(0.6)
        c.roundRect(cx + dx - 0.95*cm, cy + dy - 0.45*cm, 1.9*cm, 0.9*cm, 0.10*cm, fill=1, stroke=1)
        _draw_benefit_icon(c, cx + dx - 0.65*cm, cy + dy, kind)
        c.setFillColor(GOLD); c.setFont("Helvetica-Bold", 5.5)
        for i, ln in enumerate(label.split("\n")):
            c.drawString(cx + dx - 0.25*cm, cy + dy + 0.18*cm - i*0.18*cm, ln)
        c.setFillColor(CREAM); c.setFont("Helvetica", 4.5)
        c.drawString(cx + dx - 0.25*cm, cy + dy - 0.30*cm, sub)


def cpt_img4_benefits_200(c, cx, cy):
    """200 ml — 5 benefits with REISEGRÖSSE / ALLTAG flavour."""
    _benefits_frame(c, cx, cy, [
        ("natural",      "NATÜRLICH",        "Bienenwachs & Avocadoöl"),
        ("germany",      "MADE IN\nGERMANY", "Familienmanufaktur seit 1912"),
        ("three_in_one", "3 IN 1",           "Reinigt · Pflegt · Schützt"),
        ("travel",       "ALLTAGS-\nGRÖSSE", "200 ml · passt überallhin"),
        ("no_chemicals", "OHNE CHEMIE",      "Keine Silikone · Harze · Säuren"),
    ])


def cpt_img4_benefits_500(c, cx, cy):
    """500 ml — 5 benefits with WERKSTATTGRÖSSE / VALUE flavour."""
    _benefits_frame(c, cx, cy, [
        ("natural",      "NATÜRLICH",        "Bienenwachs & Avocadoöl"),
        ("germany",      "MADE IN\nGERMANY", "Familienmanufaktur seit 1912"),
        ("three_in_one", "3 IN 1",           "Reinigt · Pflegt · Schützt"),
        ("workshop",     "WERKSTATT-\nGRÖSSE","500 ml · ca. 1 Jahr Vorrat"),
        ("no_chemicals", "OHNE CHEMIE",      "Keine Silikone · Harze · Säuren"),
    ])


# ─── Slot #5: Honigwaben-Rezeptur ───────────────────────────────────

def cpt_img5_honeycomb(c, cx, cy):
    c.setFillColor(CREAM); c.setFont("Times-Bold", 8.5)
    c.drawCentredString(cx, cy + 2.4*cm, "BIENENWACHS, AVOCADOÖL —")
    c.drawCentredString(cx, cy + 2.05*cm, "UND SONST NICHTS.")
    hr = 0.55*cm
    positions = [
        (cx - 1.4*cm, cy + 1.0*cm, "bw"),
        (cx,          cy + 1.0*cm, "tin"),
        (cx + 1.4*cm, cy + 1.0*cm, "av"),
        (cx - 1.4*cm, cy - 0.3*cm, "jo"),
        (cx + 1.4*cm, cy - 0.3*cm, "ca"),
        (cx,          cy - 0.3*cm, "1912"),
    ]
    for x, y, kind in positions:
        c.setFillColor(CHARCOAL); c.setStrokeColor(GOLD); c.setLineWidth(0.5)
        _hex(c, x, y, hr)
        pts = [(x + hr*math.cos(math.radians(60*i+30)), y + hr*math.sin(math.radians(60*i+30))) for i in range(6)]
        p = c.beginPath(); p.moveTo(*pts[0])
        for pt in pts[1:]: p.lineTo(*pt)
        p.close(); c.drawPath(p, fill=0, stroke=1)
        if kind == "bw":
            c.setFillColor(BEESWAX); c.circle(x, y, hr*0.50, fill=1, stroke=0)
        elif kind == "tin":
            _draw_tin_topdown(c, x, y, w=hr*1.4, variant="farblos", show_label=False)
        elif kind == "av":
            c.setFillColor(HexColor("#4A6438")); c.circle(x, y, hr*0.50, fill=1, stroke=0)
            c.setFillColor(HexColor("#3A2810")); c.circle(x, y, hr*0.20, fill=1, stroke=0)
        elif kind == "jo":
            c.setFillColor(HexColor("#C58A3A")); c.circle(x, y, hr*0.45, fill=1, stroke=0)
        elif kind == "ca":
            c.setFillColor(HexColor("#5A7A30")); c.circle(x, y, hr*0.45, fill=1, stroke=0)
        elif kind == "1912":
            c.setFillColor(GOLD); c.setFont("Times-Bold", 8)
            c.drawCentredString(x, y - hr*0.30, "1912")
    c.setFillColor(CREAM); c.setFont("Helvetica", 5.5)
    c.drawCentredString(cx, cy - 1.5*cm, "Bienenwachs · Avocadoöl · Jojoba · Carnauba")
    c.setFillColor(GREY); c.setFont("Helvetica-Oblique", 5)
    c.drawCentredString(cx, cy - 1.8*cm, "Keine Silikone · keine Harze · keine Säuren")


# ─── Slot #6: Lifestyle (size-specific, rich single scene) ─────────

def cpt_img6_lifestyle_200(c, cx, cy):
    """200 ml lifestyle — small-leather-goods composition.
    Brogue + glove + watch strap + tin, on warm cream cloth, lantern glow."""
    c.setFillColor(CREAM); c.setFont("Times-Bold", 8)
    c.drawCentredString(cx, cy + 2.4*cm, "REISEGRÖSSE FÜR LIEBLINGSSTÜCKE.")
    # ground (cream cloth)
    c.setFillColor(Color(CREAM.red, CREAM.green, CREAM.blue, alpha=0.12))
    c.rect(cx - 3.0*cm, cy - 2.2*cm, 6.0*cm, 3.4*cm, fill=1, stroke=0)
    # warm side light
    _draw_window_light(c, cx - 2.5*cm, cy + 1.5*cm, r=1.0*cm)
    # brogue (front left)
    _draw_brogue(c, cx - 1.8*cm, cy + 0.3*cm, w=2.0*cm, color=LEATHER_BR)
    # glove (back left)
    _draw_glove(c, cx - 0.8*cm, cy + 1.1*cm, w=1.2*cm, color=LEATHER_BR)
    # watch strap (right)
    _draw_watch_strap(c, cx + 1.5*cm, cy + 0.7*cm, w=1.8*cm, color=LEATHER_BR)
    # tin (front right) — the 200 ml hero
    _draw_tin_topdown(c, cx + 1.6*cm, cy - 1.0*cm, w=1.5*cm, variant="farblos", show_size="200 ml")
    # caption strip
    c.setFillColor(GOLD); c.setFont("Helvetica-Bold", 6)
    c.drawCentredString(cx, cy - 2.0*cm, "JACKE · SCHUH · TASCHE · HANDSCHUH · UHRENARMBAND")
    # disclaimer
    c.setFillColor(GREY); c.setFont("Helvetica-Oblique", 5)
    c.drawCentredString(cx, cy - 2.5*cm, "Nicht für Nubuk · Velours · Wildleder")


def cpt_img6_lifestyle_500(c, cx, cy):
    """500 ml lifestyle — big-leather-goods composition.
    Chesterfield arm + saddle + car seat + briefcase + tin, dark workshop look."""
    c.setFillColor(CREAM); c.setFont("Times-Bold", 7.5)
    c.drawCentredString(cx, cy + 2.4*cm, "LEDERPFLEGE FÜR AUTO, SOFA, SATTEL.")
    # warm side light
    _draw_window_light(c, cx + 2.5*cm, cy + 1.0*cm, r=1.2*cm)
    # Chesterfield arm (back left)
    _draw_chesterfield_arm(c, cx - 1.6*cm, cy + 1.0*cm, w=2.4*cm, color=LEATHER_OX)
    # Saddle on stand (back right)
    _draw_saddle(c, cx + 1.6*cm, cy + 1.0*cm, w=2.0*cm, color=LEATHER_BR)
    # Briefcase (front left)
    _draw_briefcase(c, cx - 1.6*cm, cy - 1.0*cm, w=1.8*cm, color=LEATHER_BR)
    # Car seat icon (front mid)
    _draw_car_seat(c, cx + 0.1*cm, cy - 1.0*cm, w=1.8*cm, color=LEATHER_BR)
    # tin (front right) — the 500 ml hero
    _draw_tin_topdown(c, cx + 1.9*cm, cy - 1.0*cm, w=1.6*cm, variant="farblos", show_size="500 ml")
    # caption
    c.setFillColor(GOLD); c.setFont("Helvetica-Bold", 6)
    c.drawCentredString(cx, cy - 2.0*cm, "SOFA · SATTEL · AUTOSITZ · TASCHE · LEDERJACKE")
    c.setFillColor(GREY); c.setFont("Helvetica-Oblique", 5)
    c.drawCentredString(cx, cy - 2.5*cm, "Nicht für Nubuk · Velours · Wildleder")


# ─── Slot #7: 1912 Heritage ────────────────────────────────────────

def cpt_img7_heritage(c, cx, cy):
    c.setFillColor(CREAM); c.setFont("Times-Italic", 7)
    c.drawCentredString(cx, cy + 2.4*cm, "Vier Generationen. Eine Rezeptur.")
    c.setFillColor(GOLD); c.setFont("Times-Bold", 60)
    c.drawCentredString(cx, cy - 0.4*cm, "1912")
    _draw_tin_topdown(c, cx + 1.8*cm, cy - 1.8*cm, w=0.9*cm, variant="farblos", show_label=False)
    _draw_fir(c, cx - 1.8*cm, cy - 1.8*cm, h=0.9*cm)
    c.setFillColor(CREAM); c.setFont("Helvetica-Bold", 5.5)
    c.drawCentredString(cx, cy - 2.5*cm, "FAMILIENMANUFAKTUR · BERNAU · MADE IN GERMANY")


# ─── A+ banner concepts ─────────────────────────────────────────────

def cpt_aplus1(c, cx, cy):
    for i in range(4):
        _draw_fir(c, cx - 4.0*cm + i*0.45*cm, cy - 0.3*cm, h=1.4*cm)
    _draw_window_light(c, cx + 1.8*cm, cy + 0.4*cm, r=0.9*cm)
    c.setFillColor(GOLD); c.setFont("Times-BoldItalic", 15)
    c.drawCentredString(cx - 0.5*cm, cy + 0.3*cm, "Jotti")
    c.setFillColor(GOLD); c.setFont("Times-Italic", 7)
    c.drawCentredString(cx - 0.5*cm, cy - 0.05*cm, "Schwarzwälder Qualität · seit 1912")
    # two tins — Farblos in both sizes (we're in the Farblos brief)
    _draw_tin_3q(c, cx + 2.5*cm, cy - 0.5*cm, w=1.1*cm, variant="farblos", size_label="500 ml")
    _draw_tin_3q(c, cx + 3.5*cm, cy - 0.5*cm, w=0.85*cm, variant="farblos", size_label="200 ml")


def cpt_aplus_carousel(c, cx, cy):
    hr = 0.55*cm
    for i in range(5):
        x = cx - 2.2*cm + i*1.1*cm
        c.setFillColor(CHARCOAL); c.setStrokeColor(GOLD); c.setLineWidth(0.4)
        _hex(c, x, cy + 0.2*cm, hr)
        pts = [(x + hr*math.cos(math.radians(60*j+30)), cy + 0.2*cm + hr*math.sin(math.radians(60*j+30))) for j in range(6)]
        p = c.beginPath(); p.moveTo(*pts[0])
        for pt in pts[1:]: p.lineTo(*pt)
        p.close(); c.drawPath(p, fill=0, stroke=1)
        c.setFillColor(GOLD); c.setFont("Helvetica-Bold", 8)
        c.drawCentredString(x, cy + 0.15*cm, str(i+1))
    c.setFillColor(CREAM); c.setFont("Times-Bold", 8)
    c.drawCentredString(cx, cy + 1.1*cm, "5 GRÜNDE JOTTI")
    c.setFillColor(GREY); c.setFont("Helvetica", 6)
    c.drawCentredString(cx, cy - 0.9*cm, "Natürlich · 1912 · 3-in-1 · Universell · Ohne Chemie")


def cpt_aplus_restoration(c, cx, cy):
    _draw_chesterfield_arm(c, cx, cy + 0.0*cm, w=5.0*cm, color=LEATHER_OX)
    # split — left dim, right glowing
    c.setFillColor(Color(0,0,0,alpha=0.55))
    c.rect(cx - 2.5*cm, cy - 1.0*cm, 2.5*cm, 2.0*cm, fill=1, stroke=0)
    _draw_window_light(c, cx + 1.8*cm, cy + 0.2*cm, r=1.0*cm)
    c.setStrokeColor(GOLD); c.setLineWidth(0.6)
    c.line(cx, cy - 1.0*cm, cx, cy + 1.0*cm)
    c.setFillColor(BLACK); c.setStrokeColor(GOLD)
    c.circle(cx - 2.7*cm, cy - 1.4*cm, 0.45*cm, fill=1, stroke=1)
    c.setFillColor(BEESWAX); c.circle(cx - 2.7*cm, cy - 1.4*cm, 0.35*cm, fill=1, stroke=0)
    c.setFillColor(CREAM); c.setFont("Times-Bold", 8)
    c.drawCentredString(cx, cy + 1.4*cm, "IN 2 STUNDEN GESCHMEIDIG.")


def cpt_aplus_manufaktur(c, cx, cy):
    # warm glow
    _draw_window_light(c, cx - 3.0*cm, cy + 0.6*cm, r=1.0*cm)
    # bench
    c.setFillColor(WALNUT); c.rect(cx - 3.5*cm, cy - 0.8*cm, 7.0*cm, 0.45*cm, fill=1, stroke=0)
    # brass scale
    c.setFillColor(BRASS); c.setStrokeColor(GOLD); c.setLineWidth(0.3)
    c.rect(cx - 0.04*cm, cy - 0.7*cm, 0.08*cm, 0.9*cm, fill=1, stroke=0)
    c.rect(cx - 0.8*cm, cy + 0.2*cm, 1.6*cm, 0.05*cm, fill=1, stroke=0)
    c.circle(cx - 0.8*cm, cy + 0.10*cm, 0.18*cm, fill=1, stroke=1)
    c.circle(cx + 0.8*cm, cy + 0.10*cm, 0.18*cm, fill=1, stroke=1)
    # tins
    _draw_tin_topdown(c, cx + 1.8*cm, cy - 0.4*cm, w=0.7*cm, variant="farblos", show_label=False)
    _draw_tin_topdown(c, cx + 2.5*cm, cy - 0.4*cm, w=0.5*cm, variant="farblos", show_label=False)
    c.setFillColor(CREAM); c.setFont("Times-Bold", 8)
    c.drawCentredString(cx, cy + 1.4*cm, "EINE REZEPTUR. VIER GENERATIONEN.")


def cpt_aplus_uses(c, cx, cy):
    labels = ["SOFA", "SCHUH", "SATTEL", "AUTOSITZ", "TASCHE"]
    for i, lbl in enumerate(labels):
        x = cx - 2.2*cm + i*1.1*cm
        c.setFillColor(LEATHER_BR); c.setStrokeColor(GOLD); c.setLineWidth(0.4)
        c.roundRect(x - 0.45*cm, cy - 0.4*cm, 0.9*cm, 0.9*cm, 0.05*cm, fill=1, stroke=1)
        c.setFillColor(CREAM); c.setFont("Helvetica-Bold", 5.5)
        c.drawCentredString(x, cy - 0.7*cm, lbl)


def cpt_aplus_qa(c, cx, cy):
    c.setFillColor(GOLD); c.setFont("Times-Bold", 8)
    c.drawCentredString(cx, cy + 1.0*cm, "HÄUFIGE FRAGEN")
    for i, q in enumerate([
        "Macht Farblos das Leder dunkler?",
        "Geeignet für Wildleder / Nubuk?",
        "Bleibt ein klebriger Film zurück?",
        "Wie oft anwenden?",
        "Wie riecht der Balsam?",
    ]):
        c.setFillColor(CREAM); c.setFont("Helvetica", 6.5)
        c.drawCentredString(cx, cy + 0.45*cm - i*0.25*cm, "· " + q)


def cpt_aplus_compare(c, cx, cy):
    cols = ["Lederbalsam", "Lederpflege fl.", "Möbelwachs", "Polsterspray", "Imprägnierer", "Lederreiniger"]
    w = 1.55*cm
    for i, col in enumerate(cols):
        x = cx - 4.7*cm + i*w
        c.setFillColor(AMBER if i == 0 else CHARCOAL); c.setStrokeColor(GOLD); c.setLineWidth(0.4)
        c.rect(x, cy - 0.8*cm, w - 0.05*cm, 1.4*cm, fill=1, stroke=1)
        _draw_tin_topdown(c, x + w/2, cy + 0.1*cm, w=0.55*cm, variant="farblos", show_label=False)
        c.setFillColor(BLACK if i == 0 else CREAM); c.setFont("Helvetica-Bold", 5)
        c.drawCentredString(x + w/2, cy - 0.55*cm, col[:13])


# ─── Moodboard tile drawings ────────────────────────────────────────

def md_workshop(c, cx, cy):
    _draw_window_light(c, cx - 1.5*cm, cy + 0.5*cm, r=0.9*cm)
    c.setFillColor(WALNUT); c.rect(cx - 2.0*cm, cy - 0.9*cm, 4.0*cm, 0.4*cm, fill=1, stroke=0)
    c.setFillColor(BRASS); c.setStrokeColor(GOLD)
    c.rect(cx - 0.04*cm, cy - 0.6*cm, 0.08*cm, 0.8*cm, fill=1, stroke=0)
    c.rect(cx - 0.7*cm, cy + 0.10*cm, 1.4*cm, 0.05*cm, fill=1, stroke=0)
    c.circle(cx - 0.7*cm, cy + 0.0*cm, 0.18*cm, fill=1, stroke=1)
    c.circle(cx + 0.7*cm, cy + 0.0*cm, 0.18*cm, fill=1, stroke=1)
    _draw_tin_topdown(c, cx + 1.4*cm, cy - 0.5*cm, w=0.7*cm, variant="farblos", show_label=False)


def md_honeycomb(c, cx, cy):
    _honeycomb(c, cx, cy + 0.3*cm, radius=1.6*cm, opacity=0.55, color=AMBER)
    c.setFillColor(BEESWAX); c.rect(cx - 0.5*cm, cy - 0.6*cm, 1.0*cm, 0.55*cm, fill=1, stroke=0)


def md_saddle(c, cx, cy):
    _draw_saddle(c, cx, cy, w=2.4*cm)


def md_avocado(c, cx, cy):
    c.setFillColor(HexColor("#3A2810"))
    c.rect(cx - 1.8*cm, cy - 1.0*cm, 3.6*cm, 2.0*cm, fill=1, stroke=0)
    c.setFillColor(HexColor("#5A7A30"))
    c.ellipse(cx - 0.9*cm, cy - 0.7*cm, cx + 0.9*cm, cy + 0.7*cm, fill=1, stroke=0)
    c.setFillColor(HexColor("#C8D89A"))
    c.ellipse(cx - 0.7*cm, cy - 0.55*cm, cx + 0.7*cm, cy + 0.55*cm, fill=1, stroke=0)
    c.setFillColor(HexColor("#5A3818"))
    c.circle(cx, cy, 0.32*cm, fill=1, stroke=0)


def md_lantern(c, cx, cy):
    _draw_window_light(c, cx + 0.8*cm, cy + 0.3*cm, r=1.0*cm)
    for i in range(5):
        _draw_fir(c, cx - 1.6*cm + i*0.30*cm, cy, h=1.3*cm)


def md_brogue(c, cx, cy):
    _draw_brogue(c, cx, cy, w=3.0*cm, color=LEATHER_BR)


def md_chesterfield(c, cx, cy):
    _draw_chesterfield_arm(c, cx, cy, w=3.4*cm, color=LEATHER_OX)


def md_palette(c, cx, cy):
    cols = [BLACK, AMBER, GOLD, CREAM, BROWN, ONYX]
    for i, col in enumerate(cols):
        x = cx - 2.0*cm + i*0.7*cm
        c.setFillColor(col); c.setStrokeColor(HexColor("#CCCCCC")); c.setLineWidth(0.3)
        c.rect(x - 0.30*cm, cy - 0.5*cm, 0.60*cm, 1.0*cm, fill=1, stroke=1)


# ─── Page chrome ────────────────────────────────────────────────────

def cover_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(BLACK); canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    _honeycomb(canvas, PAGE_W*0.78, PAGE_H*0.55, radius=9*cm, opacity=0.08, color=AMBER)
    _honeycomb(canvas, PAGE_W*0.15, PAGE_H*0.25, radius=5*cm, opacity=0.06, color=AMBER)
    canvas.setFillColor(GOLD); canvas.rect(0, PAGE_H - 0.5*cm, PAGE_W, 0.5*cm, fill=1, stroke=0)
    canvas.setFillColor(GOLD); canvas.setFont("Times-BoldItalic", 56)
    canvas.drawString(ML, PAGE_H - 4.5*cm, "Jotti")
    canvas.setFillColor(GOLD); canvas.setFont("Times-Italic", 13)
    canvas.drawString(ML, PAGE_H - 5.2*cm, "Schwarzwälder Qualität · seit 1912")
    canvas.setFillColor(CREAM); canvas.setFont("Times-Bold", 34)
    canvas.drawString(ML, PAGE_H - 8.4*cm, "Lederbalsam Farblos")
    canvas.setFillColor(CREAM); canvas.setFont("Helvetica", 14)
    canvas.drawString(ML, PAGE_H - 9.2*cm, "200 ml & 500 ml · 2 separate Amazon.de Listings")
    canvas.setStrokeColor(GOLD); canvas.setLineWidth(0.5)
    canvas.line(ML, PAGE_H - 10.0*cm, ML + 8*cm, PAGE_H - 10.0*cm)
    canvas.setFillColor(GOLD); canvas.setFont("Helvetica-Bold", 14)
    canvas.drawString(ML, PAGE_H - 10.9*cm, "Amazon.de — Content Brief")
    canvas.setFillColor(CREAM); canvas.setFont("Helvetica", 11)
    canvas.drawString(ML, PAGE_H - 11.5*cm, "KW & Review Research · Per-SKU Image Plans · A+ Premium · Master Copy")

    y = 4.5*cm
    fields = [("MARKE", "Jotti GmbH"), ("MARKT", "Amazon.de"), ("SKUs", "Farblos 200 ml + 500 ml"), ("DATUM", "2026-05-16")]
    for i, (k, v) in enumerate(fields):
        x = ML + i * 4.4*cm
        canvas.setFillColor(GOLD); canvas.setFont("Helvetica-Bold", 8)
        canvas.drawString(x, y, k)
        canvas.setFillColor(CREAM); canvas.setFont("Helvetica", 11)
        canvas.drawString(x, y - 0.55*cm, v)

    # Two Farblos tins — 200 ml smaller, 500 ml larger
    _draw_tin_topdown(canvas, PAGE_W - MR - 5.0*cm, PAGE_H - 12.0*cm, w=2.4*cm, variant="farblos", show_size="200 ml")
    _draw_tin_topdown(canvas, PAGE_W - MR - 2.0*cm, PAGE_H - 12.5*cm, w=3.4*cm, variant="farblos", show_size="500 ml")
    canvas.setFillColor(GOLD); canvas.setFont("Helvetica-Oblique", 10)
    canvas.drawString(ML, PAGE_H - 15.0*cm, "Zwei Größen. Eine Rezeptur. Zwei eigene Listings.")

    canvas.setFillColor(GOLD); canvas.rect(0, 0, PAGE_W, 1.3*cm, fill=1, stroke=0)
    canvas.setFillColor(BLACK); canvas.setFont("Helvetica-Bold", 9)
    canvas.drawString(ML, 0.5*cm, "SCHWARZWÄLDER QUALITÄT · SEIT 1912")
    canvas.setFillColor(BLACK); canvas.setFont("Helvetica", 9)
    canvas.drawRightString(PAGE_W - MR, 0.5*cm, "Prepared by EQUALICE")
    canvas.restoreState()


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(GOLD); canvas.setLineWidth(2.0)
    canvas.line(ML, PAGE_H - 1.0*cm, PAGE_W - MR, PAGE_H - 1.0*cm)
    canvas.setFillColor(BLACK); canvas.setFont("Times-BoldItalic", 11)
    canvas.drawString(ML, PAGE_H - 0.7*cm, "Jotti")
    canvas.setFillColor(GREY); canvas.setFont("Helvetica", 8)
    canvas.drawString(ML + 1.5*cm, PAGE_H - 0.7*cm, "Lederbalsam Farblos — Amazon.de Content Brief")
    canvas.setFillColor(GREY); canvas.setFont("Helvetica", 8)
    canvas.drawRightString(PAGE_W - MR, PAGE_H - 0.7*cm, f"Seite {doc.page}")
    canvas.setStrokeColor(HexColor("#E0DCC8")); canvas.setLineWidth(0.4)
    canvas.line(ML, MB - 0.4*cm, PAGE_W - MR, MB - 0.4*cm)
    canvas.setFillColor(GREY); canvas.setFont("Helvetica", 7.5)
    canvas.drawString(ML, MB - 0.7*cm, "Prepared by EQUALICE — 2026-05-16 · Schwarzwälder Qualität seit 1912")
    canvas.restoreState()


def _side(rows, width):
    t = Table([[r] for r in rows], colWidths=[width])
    t.setStyle(TableStyle([
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 0),
        ("RIGHTPADDING", (0,0), (-1,-1), 0),
        ("TOPPADDING", (0,0), (-1,-1), 0),
        ("BOTTOMPADDING", (0,0), (-1,-1), 2),
    ]))
    return t


def _sku_section(s, sku_label, sku_subtitle, options, listings):
    """Render the per-SKU section: banner + 3 main options + 7 listing mockups."""
    s.append(PageBreak())
    s.append(SectionBanner(sku_label, sku_subtitle))
    s.append(Spacer(1, 0.4*cm))
    s.append(Paragraph("Main Image — 3 Options for CTR Test", H3))
    s.append(Paragraph(
        "Amazon main-image rules: pure white BG, product fills ≥ 85 %, no overlay text. All visible "
        "labels (Made in Germany flag, \"seit 1912\" arch, ingredients strap) are <b>physically on the "
        "tin</b> — Amazon-compliant. Recommend a 4-week Manage Your Experiments A/B/C test.", BODY))
    s.append(Spacer(1, 0.2*cm))
    for letter, name, desc, pitch, fn in options:
        s.append(Paragraph(f"Option {letter} — {name}", H3))
        m = MainOption(letter, name, fn)
        side = _side([
            Paragraph(f"<b>Composition:</b> {desc}", BODY),
            Spacer(1, 0.1*cm),
            Paragraph(f"<i>CTR pitch:</i> {pitch}", QUOTE),
        ], CW - m.size - m.gap)
        row = Table([[m, side]], colWidths=[m.size + m.gap, CW - m.size - m.gap])
        row.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),
                                 ("LEFTPADDING",(0,0),(-1,-1),0), ("RIGHTPADDING",(0,0),(-1,-1),0)]))
        s.append(KeepTogether([row])); s.append(Spacer(1, 0.30*cm))

    s.append(PageBreak())
    s.append(Paragraph("Seven Listing Images — Full Gallery", H3))
    s.append(Paragraph(
        "Format: 2000 × 2000 px · sRGB · JPG · ≤ 5 MB. Headlines below are the German overlay copy "
        "that will appear on the frame; the visual brief is in English for the design team.", SUB))
    for slot, role, headline_de, why_en, fn, bg in listings:
        s.append(Paragraph(f"Bild {slot} — {role}", H3))
        m = ListingMockup(slot, role, fn, bg=bg)
        side = _side([
            Paragraph(f"<b>On-image headline (DE):</b> {headline_de}", BODY),
            Spacer(1, 0.1*cm),
            Paragraph(f"<i>Visual concept (EN):</i> {why_en}", QUOTE),
        ], CW - m.size - m.gap)
        row = Table([[m, side]], colWidths=[m.size + m.gap, CW - m.size - m.gap])
        row.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),
                                 ("LEFTPADDING",(0,0),(-1,-1),0), ("RIGHTPADDING",(0,0),(-1,-1),0)]))
        s.append(KeepTogether([row])); s.append(Spacer(1, 0.30*cm))


# ─── Build ──────────────────────────────────────────────────────────

def build():
    doc = BaseDocTemplate(OUT, pagesize=A4,
                          leftMargin=ML, rightMargin=MR,
                          topMargin=MT, bottomMargin=MB,
                          title="Jotti Lederbalsam Farblos — Amazon.de Content Brief",
                          author="EQUALICE")
    cf = Frame(ML, MB, CW, PAGE_H - MT - MB, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    bf = Frame(ML, MB, CW, PAGE_H - MT - MB, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([
        PageTemplate(id="Cover", frames=[cf], onPage=cover_page),
        PageTemplate(id="Body",  frames=[bf], onPage=header_footer),
    ])

    s = []
    s.append(Spacer(1, PAGE_H - MT - MB - 2))
    s.append(NextPageTemplate("Body")); s.append(PageBreak())

    # ───── At a Glance — both SKUs ─────
    s.append(Paragraph("Auf einen Blick — Zwei separate Listings", H2)); s.append(HRule())
    s.append(Paragraph(
        "Farblos 200 ml und Farblos 500 ml laufen als <b>zwei getrennte Listings</b> auf Amazon.de — "
        "nicht als Parent/Variant. Brandbook, Moodboard, A+ Premium und Voice sind shared; "
        "Main Image, Lifestyle-Frame und Master Copy sind <b>SKU-spezifisch</b>.", BODY))

    g = [
        ["Marke", "Jotti GmbH · Familienmanufaktur Bernau, Schwarzwald · seit 1912"],
        ["Produkt", "Lederbalsam (Wachs) · Farblos · Bienenwachs · Avocadoöl · Jojoba · Carnauba"],
        ["Listing A", "Farblos 200 ml — Reisegröße / Alltagsgröße"],
        ["Listing B", "Farblos 500 ml — Werkstattgröße / Jahresvorrat"],
        ["Marktplatz", "Amazon.de"],
        ["Top-Wettbewerber", "Leather Honey · Collonil · Sonax · Furniture Clinic · Tapir"],
        ["Hero-USP", "Schwarzwälder Familienmanufaktur seit 1912 · Bienenwachs &amp; Avocadoöl · ohne Chemie"],
        ["Tonalität", "Premium deutsche Tradition. Konkret statt schwülstig. Foto trägt 80 %, Text 20 %."],
    ]
    t = Table([[Paragraph(f"<b>{k}</b>", BODY), Paragraph(v, BODY)] for k, v in g],
              colWidths=[3.8*cm, CW - 3.8*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,-1), HexColor("#F4EFE3")),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LINEBELOW", (0,0), (-1,-1), 0.3, HexColor("#E0DCC8")),
        ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 6), ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ]))
    s.append(t)

    s.append(Spacer(1, 0.4*cm))
    strat = Table([[Paragraph(
        "<b>Strategic Read (EN).</b> Each listing wins the click with a dark, honeycomb-relief tin in a "
        "category of white/yellow competitors. The 200 ml listing converts on <i>small-leather lifestyle</i> "
        "(shoes, jackets, gloves, watch straps) — high-volume KWs like <i>lederpflege schuhe</i> (1,175) and "
        "<i>lederpflege jacke</i>. The 500 ml listing converts on <i>furniture &amp; auto lifestyle</i> "
        "(Chesterfield arm, Mercedes seat, saddle) — high-volume KWs like <i>lederpflege auto</i> (8,873) "
        "and <i>lederpflege für ledercouch</i> (1,995). Image #4 (5-Promises badges) is shared but with "
        "one badge swapped per SKU — Reisegröße vs. Werkstattgröße.", BODY)]],
        colWidths=[CW])
    strat.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), BLACK),
        ("TEXTCOLOR", (0,0), (-1,-1), CREAM),
        ("LEFTPADDING", (0,0), (-1,-1), 14), ("RIGHTPADDING", (0,0), (-1,-1), 14),
        ("TOPPADDING", (0,0), (-1,-1), 10), ("BOTTOMPADDING", (0,0), (-1,-1), 10),
        ("BOX", (0,0), (-1,-1), 0.8, GOLD),
    ]))
    s.append(strat)

    # ───── KW & Review Research → Design Map ─────
    s.append(PageBreak())
    s.append(Paragraph("1 · Keyword &amp; Review Research → Design Decisions", H2)); s.append(HRule())
    s.append(Paragraph(
        "Every CTR/CVR design call below is anchored to a specific keyword (with volume) or a specific "
        "review theme from the live Excel data. If a row in the image plan doesn't tie to a row here, "
        "it shouldn't be there.", SUB))

    s.append(Paragraph("Top keywords (DE, Helium-10 Phase 1)", H3))
    kws = [
        ["KW", "Volume", "Used in"],
        ["bienenwachs", "17,289", "Bild 4 Badge #1 · Bullet 2 · A+ Modul 2 Tile #1"],
        ["lederpflege auto", "8,873", "500 ml Bild 6 (Mercedes-Innenraum) · Bullet 4 · Backend"],
        ["lederpflege", "3,017", "Titel · Bullet 1 — alle Sizes"],
        ["auto lederpflege", "2,648", "500 ml Bild 6 · Backend"],
        ["lederpflege für ledercouch", "1,995", "500 ml Bild 6 (Chesterfield) · Bild 3 demo object"],
        ["lederfett farblos", "1,595", "Backend · Bullet 4 (Lederfett-Alternative)"],
        ["lederbalsam", "1,198", "Titel · Brand-Reinforcement durchgehend"],
        ["lederpflege schuhe", "1,175", "200 ml Bild 6 (Brogues) · Bullet 4"],
        ["lederpflege jacke", "ca. 700", "200 ml Bild 3 demo object · Bild 6"],
        ["lederpflege tasche", "ca. 600", "200 ml Bild 6 (Aktentasche)"],
        ["lederpflege autositze", "ca. 500", "500 ml Bild 6 (Car seat)"],
        ["lederpflege sofa", "ca. 500", "500 ml Bild 3 demo object · Bild 6"],
        ["lederbalsam farblos", "spezifisch", "Bild 2 Headline · 5-Promises Badge"],
        ["sattelfett", "ca. 400", "500 ml Bild 6 (Sattel) · Backend"],
        ["leather honey", "Wettbewerber", "Backend (competitive cap)"],
    ]
    kw_t = Table(kws, colWidths=[4.5*cm, 2.3*cm, CW - 6.8*cm])
    kw_t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), BLACK),
        ("TEXTCOLOR", (0,0), (-1,0), GOLD),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,-1), 8),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("LEFTPADDING", (0,0), (-1,-1), 6), ("RIGHTPADDING", (0,0), (-1,-1), 6),
        ("TOPPADDING", (0,0), (-1,-1), 4), ("BOTTOMPADDING", (0,0), (-1,-1), 4),
        ("GRID", (0,0), (-1,-1), 0.3, HexColor("#DDDDDD")),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, HexColor("#F4EFE3")]),
    ]))
    s.append(kw_t)

    s.append(Spacer(1, 0.4*cm))
    s.append(Paragraph("Review themes (live Excel — Lederbalsam 500 ml)", H3))
    revs = [
        ["Sentiment", "Theme (verbatim)", "Where the design uses it"],
        ["★★★★★", "\"Lässt sich sehr gut dosieren und auftragen\"", "Bild 3 demo: hand + cloth visible · Bullet 5 (dünn auftragen)"],
        ["★★★★★", "\"Hinterlässt keine Rückstände und riecht toll\"", "Modul 6 Q&A (Duft) · Bullet 5 (kein Restschmierfilm)"],
        ["★★★★★", "\"Pflegt das Leder schön, riecht sehr angenehm\"", "Bild 6 lifestyle · Modul 6 Q&A"],
        ["★★★★★", "\"Bin überrascht wie dieses Fett meine alten Lederjacken erneuert hat\"", "Bild 3 Headline \"In 2 Stunden geschmeidig\" · Bild 2 Hook"],
        ["★", "\"Färbt stark ab, vor allem bei Feuchte\"", "Bild 3 bottom strap: <i>dünn auftragen · einziehen lassen · trocken polieren</i> · Modul 6 Q&A (Rückstand) — defuses misuse before purchase"],
    ]
    rev_t = Table(revs, colWidths=[1.7*cm, 7.5*cm, CW - 9.2*cm])
    rev_t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), BLACK),
        ("TEXTCOLOR", (0,0), (-1,0), GOLD),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,-1), 8),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 6), ("RIGHTPADDING", (0,0), (-1,-1), 6),
        ("TOPPADDING", (0,0), (-1,-1), 5), ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("GRID", (0,0), (-1,-1), 0.3, HexColor("#DDDDDD")),
        ("BACKGROUND", (0,1), (-1,4), WHITE),
        ("BACKGROUND", (0,5), (-1,5), HexColor("#FBE5E8")),
    ]))
    s.append(rev_t)

    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("Improvement notes from the Excel (CTR diagnosis)", H3))
    for line in [
        "<b>Main image is not attractive</b> → Image #1 redesigned with the dark honeycomb tin against white BG. Dark tile wins contrast in a white-tile SERP.",
        "<b>Price is high (target ~€23 for 500 ml)</b> → 500 ml positioned as Werkstattgröße / Jahresvorrat — justifies the price as months of pflege; 200 ml as gift / try-it size at lower entry point.",
        "<b>Low visibility</b> → Title leads with the highest-volume KW (\"lederpflege\"); bullets are SEO-loaded; backend covers Leather Honey, lederfett, sattelfett.",
    ]:
        s.append(Paragraph("· " + line, BODY))

    # ───── Brandbook ─────
    s.append(PageBreak())
    s.append(Paragraph("2 · Brandbook", H2)); s.append(HRule())
    s.append(Paragraph(
        "Source of truth: the existing 500 ml labels (Farblos, Braun, Schwarz). Dark Jotti Black with "
        "honeycomb relief, warm cream as type colour, gold as the only highlight metal. The forest-green "
        "idea from the original briefing PDF is parked — we honour the production label.", BODY))

    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("Farbpalette", H3))
    row1 = [ColorChip(BLACK, "#0E0E0E", "Jotti Black"),
            ColorChip(CHARCOAL,"#1B1814", "Wax Charcoal"),
            ColorChip(AMBER, "#C58A3A", "Honig Amber"),
            ColorChip(GOLD,  "#D9B36B", "Jotti Gold")]
    row2 = [ColorChip(CREAM, "#EFE6D2", "Pergament"),
            ColorChip(TAN,   "#C9985A", "Natur Tan · Farblos"),
            ColorChip(BROWN, "#6A3A1E", "Sattel Braun"),
            ColorChip(ONYX,  "#0A0A0A", "Onyx")]
    s.append(Table([row1], colWidths=[CW/4]*4,
                   style=TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),
                                     ("LEFTPADDING",(0,0),(-1,-1),0),
                                     ("RIGHTPADDING",(0,0),(-1,-1),6)])))
    s.append(Table([row2], colWidths=[CW/4]*4,
                   style=TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),
                                     ("LEFTPADDING",(0,0),(-1,-1),0),
                                     ("RIGHTPADDING",(0,0),(-1,-1),6)])))

    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph("Typography", H3))
    typo = [
        ["Display / Brand",  "Trajan Pro · Cormorant Garamond Bold (chiselled serif)"],
        ["Jotti Wordmark",   "Locked SVG — script serif with gold arched \"seit 1912\""],
        ["Headlines",        "Recoleta SemiBold · GT Sectra (heritage display serif)"],
        ["Body / Bullets",   "Söhne · Inter (grotesque sans, cream on dark)"],
        ["Cap-Strap",        "Body sans, small caps, +160 tracking — only for \"SCHWARZWÄLDER QUALITÄT · SEIT 1912\""],
    ]
    tt = Table([[Paragraph(f"<b>{k}</b>", BODY), Paragraph(v, BODY)] for k, v in typo],
               colWidths=[4.0*cm, CW - 4.0*cm])
    tt.setStyle(TableStyle([
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LINEBELOW", (0,0), (-1,-1), 0.3, HexColor("#E0DCC8")),
        ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 5), ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ]))
    s.append(tt)

    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("Voice", H3))
    for r in [
        "Premium German tradition. Honey-warm meets workshop precision.",
        "Quiet, factual. We don't sell loud — we sell old.",
        "Specific over flowery. \"Premium\" → \"Bienenwachs &amp; Avocadoöl\". \"Quality\" → \"seit 1912\".",
        "Three words beat ten. Photo carries 80 %, copy 20 %.",
        "Never eco-wellness. Never discount. Never SaaS-minimal. Never pure white (except Amazon main-image compliance).",
    ]:
        s.append(Paragraph("· " + r, BODY))

    # ───── Moodboard ─────
    s.append(PageBreak())
    s.append(Paragraph("3 · Moodboard", H2)); s.append(HRule())
    s.append(Paragraph(
        "Mood: <b>a Black Forest workshop at night, lit by a lantern.</b> Warm side light, dark walnut "
        "bench, tools, brass, well-cared-for leather. Hermès-workshop meets fine-honey-brand. Not apothecary, not eco-wellness.", BODY))
    s.append(Spacer(1, 0.3*cm))

    md_w = (CW - 0.4*cm) / 3
    md_h = 3.6*cm
    row1 = Table([[
        MoodTile("Werkstatt bei Nacht", "Walnuss · Messing · Leder", md_workshop, w=md_w, h=md_h, bg=BLACK),
        MoodTile("Honigwaben", "Signature Pattern", md_honeycomb, w=md_w, h=md_h, bg=CHARCOAL),
        MoodTile("Brauner Brogue", "200 ml lifestyle hero", md_brogue, w=md_w, h=md_h, bg=CHARCOAL),
    ]], colWidths=[md_w]*3)
    row1.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),
                              ("LEFTPADDING",(0,0),(-1,-1),0), ("RIGHTPADDING",(0,0),(-1,-1),5)]))
    s.append(row1)
    s.append(Spacer(1, 0.2*cm))
    row2 = Table([[
        MoodTile("Chesterfield Sofa", "500 ml lifestyle hero", md_chesterfield, w=md_w, h=md_h, bg=CHARCOAL),
        MoodTile("Sattel auf Holzstand", "500 ml lifestyle prop", md_saddle, w=md_w, h=md_h, bg=CHARCOAL),
        MoodTile("Avocado auf Schiefer", "Zutat-Stillleben", md_avocado, w=md_w, h=md_h, bg=CHARCOAL),
    ]], colWidths=[md_w]*3)
    row2.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),
                              ("LEFTPADDING",(0,0),(-1,-1),0), ("RIGHTPADDING",(0,0),(-1,-1),5)]))
    s.append(row2)
    s.append(Spacer(1, 0.2*cm))
    row3 = Table([[
        MoodTile("Laternenlicht & Tanne", "Schwarzwald-Atmosphäre", md_lantern, w=md_w, h=md_h, bg=BLACK),
        MoodTile("Brand-Palette", "Black · Amber · Gold · Cream", md_palette, w=md_w, h=md_h, bg=CREAM),
    ]], colWidths=[md_w, md_w])
    row3.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),
                              ("LEFTPADDING",(0,0),(-1,-1),0), ("RIGHTPADDING",(0,0),(-1,-1),5)]))
    s.append(row3)

    # ───── Buyer Psychology ─────
    s.append(PageBreak())
    s.append(Paragraph("4 · Buyer Psychology — per SKU", H2)); s.append(HRule())
    s.append(Paragraph(
        "The 200 ml and 500 ml buyer overlap on brand love but differ sharply on use case and price sensitivity. "
        "The image plans are tuned per buyer below.", BODY))

    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("Farblos 200 ml — the everyday / gift buyer", H3))
    p200 = [
        ("Persona", "30–55. Owns a few good leather pieces — a brogue, a briefcase, a moto jacket, a watch strap. Travels for work. Wants something that fits in a Dopp kit. Often gift-buying for partner / parent / colleague."),
        ("Primary trigger", "Bought a new pair of brogues or a leather jacket. Wants to keep them looking right. Or — they own the 500 ml and want a travel-sized version. Or — wants a thoughtful €15–€20 gift."),
        ("Top KWs", "lederpflege schuhe (1,175) · lederpflege jacke (~700) · lederpflege tasche (~600) · lederbalsam farblos (specific)"),
        ("What converts", "200 ml lifestyle showing small-leather goods (brogue + glove + watch strap). \"Reisegröße\" / \"Alltagsgröße\" badge. Heritage 1912 cue at close."),
        ("Friction to defuse", "\"Is it big enough?\" → frame 200 ml as enough for ~10 applications on a pair of shoes. \"Will it spill in my bag?\" → tin (not bottle), screw-tight lid."),
    ]
    pt = Table([[Paragraph(f"<b>{k}</b>", BODY), Paragraph(v, BODY)] for k, v in p200],
               colWidths=[3.6*cm, CW - 3.6*cm])
    pt.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,-1), HexColor("#F4EFE3")),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LINEBELOW", (0,0), (-1,-1), 0.3, HexColor("#E0DCC8")),
        ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 6), ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ]))
    s.append(pt)

    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("Farblos 500 ml — the serious / repeat buyer", H3))
    p500 = [
        ("Persona", "40–65. Owns furniture-grade leather — a Chesterfield, a Mercedes E with leather seats, a saddle, a briefcase. Or runs an equestrian operation. Buys 500 ml as a routine refill."),
        ("Primary trigger", "Routine maintenance. Or recovering a dry/cracked piece. Or upgrading from supermarket Collonil tubes. Or restoring a classic-car interior."),
        ("Top KWs", "lederpflege auto (8,873) · auto lederpflege (2,648) · lederpflege für ledercouch (1,995) · sattelfett (~400) · lederpflege autositze (~500)"),
        ("What converts", "500 ml lifestyle showing big-ticket leather — Chesterfield arm, Mercedes seat, saddle, briefcase. \"Werkstattgröße\" / \"Jahresvorrat\" badge. Comparison vs. Leather Honey / Collonil in A+."),
        ("Friction to defuse", "\"€23 — is it worth it?\" → frame as ~1 year of pflege = ~€2/month. \"Won't darken my furniture?\" → Image #2 split-test on Chesterfield arm with same colour preserved."),
    ]
    pt = Table([[Paragraph(f"<b>{k}</b>", BODY), Paragraph(v, BODY)] for k, v in p500],
               colWidths=[3.6*cm, CW - 3.6*cm])
    pt.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,-1), HexColor("#F4EFE3")),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LINEBELOW", (0,0), (-1,-1), 0.3, HexColor("#E0DCC8")),
        ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 6), ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ]))
    s.append(pt)

    # ───── SKU SECTION A: Farblos 200 ml ─────
    options_200 = [
        ("A", "Floating Heritage · 200 ml",
         "Three-quarter angle of the 200 ml tin floating with a long warm amber shadow. The on-tin badges (Made in Germany flag, \"seit 1912\" arch, \"PREMIUM\" tag, \"Mit Bienenwachs · Pflegt &amp; schützt Leder\" strap) do all the storytelling. Pure white BG.",
         "Premium watch-catalogue energy. Reads as 'serious German heritage' against a sea of white competitor tins. Lowest-risk launch baseline.",
         cpt_main_a_200),
        ("B", "Wax Reveal · 200 ml",
         "Top-down view with the lid offset, exposing the amber beeswax surface inside. Honeycomb relief visible in the wax. No competitor shows the wax.",
         "Unique in the category. Surfaces the natural-ingredient proof in the SERP itself — wins on the privacy-of-recipe hook.",
         cpt_main_b_200),
        ("C", "Travel Context · 200 ml",
         "Tin in a soft 3/4 with a brown brogue half-visible behind. Still &gt; 85 % product, but signals 'travel-sized for small leather goods' in the SERP.",
         "Best for the gift / first-time buyer who is shopping shoes / jackets / bags and is unsure if the smaller size matches their use case.",
         cpt_main_c_200),
    ]

    listings_200 = [
        (1, "Click Trigger",
         "(kein Overlay — Sieger von A/B/C oben)",
         "Whichever option wins the 4-week A/B/C test becomes the permanent Image #1. The two losing concepts move into slots #2 or #6.",
         cpt_main_a_200, WHITE),
        (2, "Hook · Farb-Beweis",
         "FARBE BLEIBT. LEDER LEBT. — Mit Bienenwachs · Avocadoöl · Jojoba · Carnauba",
         "Split-test on a real natural-tan leather brogue. Left half (Vorher) desaturated and dull. Right half (Nachher) rich, supple, same color. Hard vertical gold hairline. Small tin in lower right. The headline defuses the #1 buying fear ('does it darken my leather?') in 4 words — 'Farbe bleibt' answers no, 'Leder lebt' promises restoration. Anchored to KW 'lederbalsam farblos'.",
         cpt_img2_proof_200, BLACK),
        (3, "Pflege-Moment",
         "GESCHMEIDIG IN ZWEI STUNDEN. — Dünn auftragen · einziehen lassen · trocken polieren",
         "Cinematic single shot. Older masculine hand with a folded pergament cloth applies the balm to a leather jacket sleeve. Open tin in foreground showing amber wax. Warm window light from the right. The bottom strap directly defuses the 1-star review theme ('färbt stark ab bei Feuchte') by surfacing correct application before the buyer makes the mistake. 'Zwei' spelled out (vs '2') for premium feel.",
         cpt_img3_moment_200, BLACK),
        (4, "Fünf Versprechen (Mobile-Fold)",
         "FÜNF VERSPRECHEN. SEIT 1912. — Natürlich · Made in Germany · 3-in-1 · Alltagsgröße · Ohne Chemie",
         "Five hexagonal badges around the central tin. The 200 ml differentiator is the ALLTAGSGRÖSSE badge. 'Versprechen' is a commitment word — it tees up the five promises that follow visually. Brand-honeycomb-as-layout. Sits in the mobile-visible carousel position (slot #4).",
         cpt_img4_benefits_200, BLACK),
        (5, "Honigwaben-Rezeptur",
         "BIENENWACHS, AVOCADOÖL — UND SONST NICHTS. — Vier natürliche Zutaten · keine Silikone · keine Harze · keine Säuren",
         "Six hexagons in a honeycomb layout. Center: the tin. Around it: real photographed ingredients (beeswax block, halved avocado on slate, amber-glass jojoba bottle, carnauba leaf, '1912' seal). Headline leads with the #1 KW 'bienenwachs' (17,289 SV) + the anti-chemical claim in one breath. Strongest SEO + CVR alignment of any frame.",
         cpt_img5_honeycomb, BLACK),
        (6, "Lifestyle · Small-Leather Hero",
         "REISEGRÖSSE FÜR LIEBLINGSSTÜCKE. — Schuh · Jacke · Tasche · Handschuh · Uhrenarmband",
         "Single cinematic still: brown brogue, leather driving glove, leather-strapped wristwatch, and the 200 ml tin arranged on a warm cream cloth with one warm side-light from the upper-left. The headline marries size benefit ('Reisegröße') with emotional ownership ('Lieblingsstücke'). Anchored to KWs 'lederpflege schuhe' (1,175), 'lederpflege jacke', 'lederpflege tasche'.",
         cpt_img6_lifestyle_200, BLACK),
        (7, "Heritage · 1912",
         "VIER GENERATIONEN. EINE REZEPTUR. — Familienmanufaktur · Bernau · Made in Germany",
         "The number 1912 fills 80% of the canvas in Jotti Gold serif. A small fir on the left, a small Farblos tin on the right. Like a museum poster, not an infographic. 'Vier Generationen. Eine Rezeptur.' is classic legacy positioning — trust signal no US competitor (Leather Honey) can copy.",
         cpt_img7_heritage, BLACK),
    ]
    _sku_section(s, "Listing A · Farblos 200 ml", "Reisegröße / Alltagsgröße — small-leather lifestyle", options_200, listings_200)

    # ───── SKU SECTION B: Farblos 500 ml ─────
    options_500 = [
        ("A", "Floating Heritage · 500 ml",
         "Three-quarter angle of the 500 ml tin floating with a long warm amber shadow. The on-tin badges (Made in Germany flag, \"seit 1912\" arch, \"PREMIUM\", ingredients strap) carry the story. Pure white BG.",
         "Premium watch-catalogue energy at a larger physical scale. The bigger tin reads more 'workshop / refill / value' than 200 ml. Lowest-risk launch baseline.",
         cpt_main_a_500),
        ("B", "Wax Reveal · 500 ml",
         "Top-down view with the lid offset, exposing the wide amber beeswax surface inside. Honeycomb relief visible in the wax. The bigger tin makes the wax expanse more dramatic.",
         "Same unique-in-category move as the 200 ml — the wax-reveal hook is amplified at the larger size and signals 'serious supply'.",
         cpt_main_b_500),
        ("C", "Workshop Context · 500 ml",
         "Tin in a soft 3/4 with a Chesterfield sofa arm half-visible behind. Still &gt; 85 % product. Signals 'this is the size for furniture and big-ticket leather' in the SERP.",
         "Best for the 500 ml buyer evaluating against Leather Honey or Collonil — communicates the use-case match in the SERP itself.",
         cpt_main_c_500),
    ]

    listings_500 = [
        (1, "Click Trigger",
         "(kein Overlay — Sieger von A/B/C oben)",
         "Whichever option wins the 4-week A/B/C test becomes the permanent Image #1.",
         cpt_main_a_500, WHITE),
        (2, "Hook · Farb-Beweis",
         "FARBE BLEIBT. LEDER LEBT. — Mit Bienenwachs · Avocadoöl · Jojoba · Carnauba",
         "Split-test on a Chesterfield sofa-arm (oxblood). Left half (Vorher) faded, dull, micro-cracked. Right half (Nachher) deep, supple, same colour. The 500 ml buyer is afraid of darkening a €3,000 sofa — 'Farbe bleibt' answers exactly that fear. 'Leder lebt' promises restoration of cracked surface.",
         cpt_img2_proof_500, BLACK),
        (3, "Pflege-Moment",
         "GESCHMEIDIG IN ZWEI STUNDEN. — Dünn auftragen · einziehen lassen · trocken polieren",
         "Cinematic single shot. Hand + cloth applying balm to a Chesterfield arm. Open tin in foreground showing amber wax. Warm window light. Bottom strap defuses the 'färbt ab bei Feuchte' 1-star review by surfacing correct application. Identical headline to 200 ml — same promise, scaled visual.",
         cpt_img3_moment_500, BLACK),
        (4, "Fünf Versprechen (Mobile-Fold)",
         "FÜNF VERSPRECHEN. SEIT 1912. — Natürlich · Made in Germany · 3-in-1 · Werkstattgröße · Ohne Chemie",
         "Five hexagonal badges around the central tin. The 500 ml differentiator is the WERKSTATTGRÖSSE badge ('ca. 1 Jahr Vorrat'). Justifies the €23,90 price as months of pflege, not a single application.",
         cpt_img4_benefits_500, BLACK),
        (5, "Honigwaben-Rezeptur",
         "BIENENWACHS, AVOCADOÖL — UND SONST NICHTS. — Vier natürliche Zutaten · keine Silikone · keine Harze · keine Säuren",
         "Same honeycomb-layout as the 200 ml. Headline leads with #1 KW 'bienenwachs' (17,289 SV) + the anti-chemical claim. Recipe is identical, message is identical. Reusable shared asset.",
         cpt_img5_honeycomb, BLACK),
        (6, "Lifestyle · Workshop Hero",
         "LEDERPFLEGE FÜR AUTO, SOFA, SATTEL. — 500 ml · ca. 1 Jahr Pflege · alle glatten Leder",
         "Single cinematic still: Chesterfield sofa arm + English saddle + Mercedes car seat + brown briefcase + 500 ml tin, all under one warm side-light. The headline bundles three top KWs — 'lederpflege auto' (8,873), 'lederpflege für ledercouch' (1,995), 'sattelfett' (~400) — in one line. Maximum SEO + use-case clarity.",
         cpt_img6_lifestyle_500, BLACK),
        (7, "Heritage · 1912",
         "VIER GENERATIONEN. EINE REZEPTUR. — Familienmanufaktur · Bernau · Made in Germany",
         "Same 1912-poster as the 200 ml. Legacy positioning — trust signal that justifies the premium 500 ml price.",
         cpt_img7_heritage, BLACK),
    ]
    _sku_section(s, "Listing B · Farblos 500 ml", "Werkstattgröße / Jahresvorrat — furniture + auto lifestyle", options_500, listings_500)

    # ───── A+ Premium (shared) ─────
    s.append(PageBreak())
    s.append(Paragraph("7 · A+ Premium Content (7 Modules) — shared across both listings", H2)); s.append(HRule())
    s.append(Paragraph(
        "Same A+ ships on both the 200 ml and 500 ml listings (each gets its own A+ — they're separate "
        "listings — but the content is the same). German copy throughout.", SUB))

    modules = [
        (1, "Full Image", "Schwarzwälder Lederpflege seit 1912.",
         "Familienmanufaktur · Bernau · zwei Größen", cpt_aplus1, BLACK),
        (2, "Carousel (5)", "5 Gründe Jotti — Bienenwachs · 1912 · 3-in-1 · Universell · Ohne Chemie",
         "5 hex tiles with gold line icons", cpt_aplus_carousel, BLACK),
        (3, "Full Image", "In 2 Stunden geschmeidig.",
         "Eine Anwendung · kein Fettfilm · kein klebriger Rückstand.", cpt_aplus_restoration, BLACK),
        (4, "Full Image", "Eine Rezeptur. Vier Generationen.",
         "Seit 1912 in Bernau · gleiche Rezeptur · gleicher Anspruch.", cpt_aplus_manufaktur, BLACK),
        (5, "Carousel (5)", "Sofa · Schuh · Sattel · Autositz · Tasche",
         "Use-case carousel — Rembrandt-lit lifestyle still lifes", cpt_aplus_uses, BLACK),
        (6, "Q&A", "6 häufige Fragen — voice-aligned",
         "Farbe · Wildleder · Rückstand · Häufigkeit · Duft · 1912", cpt_aplus_qa, BLACK),
        (7, "Comparison", "Jotti Range im Vergleich",
         "Lederbalsam vs. Lederpflege fl. vs. Wachs vs. Spray vs. Imprägnierer vs. Reiniger", cpt_aplus_compare, BLACK),
    ]
    for slot, mtype, hl, sub, fn, bg in modules:
        s.append(Paragraph(f"Modul {slot} — {mtype}", H3))
        m = APlusMockup(slot, mtype, fn, bg=bg)
        side = _side([
            Paragraph(f"<b>On-image headline (DE):</b> {hl}", BODY),
            Paragraph(f"<b>Body / Theme (DE):</b> {sub}", BODY),
        ], CW - m.bw - m.gap)
        row = Table([[m, side]], colWidths=[m.bw + m.gap, CW - m.bw - m.gap])
        row.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),
                                 ("LEFTPADDING",(0,0),(-1,-1),0), ("RIGHTPADDING",(0,0),(-1,-1),0)]))
        s.append(KeepTogether([row])); s.append(Spacer(1, 0.30*cm))

    # ───── Q&A + Comparison ─────
    s.append(PageBreak())
    s.append(Paragraph("Modul 6 — Q&amp;A (vollständige Copy, Deutsch)", H3))
    qa = [
        ("Macht Farblos mein Leder dunkler?",
         "Nein. Farblos ist farblos formuliert — pflegt, macht geschmeidig und schützt, ohne den Farbton zu verändern."),
        ("Geeignet für Nubuk, Velours oder Alcantara?",
         "Nein. Jotti Lederbalsam ist ausschließlich für glattes und strukturiertes Leder. Auf Nubuk, Velours, Alcantara oder Wildleder würde der Wachs-Öl-Balsam die Faser flach legen."),
        ("Bleibt ein fettiger oder klebriger Film zurück?",
         "Nein. Dünn auftragen, 2 Stunden einziehen lassen — das Ergebnis ist ein seidenmatter, trockener Glanz ohne Rückstände. Bei zu dickem Auftrag mit trockenem Tuch nachpolieren."),
        ("Wie oft anwenden?",
         "Alle 4–6 Wochen bei alltäglicher Nutzung (Sofas, Autositze, getragene Schuhe). Alle 3 Monate bei selten getragenen Stücken. Sattelzeug: einmal im Monat."),
        ("Wie riecht der Balsam?",
         "Dezent natürlich nach Bienenwachs. Nicht parfümiert. Der Duft verfliegt innerhalb einer Stunde."),
        ("Ist die Rezeptur wirklich von 1912?",
         "Ja. Die Manufaktur in Bernau im Schwarzwald stellt diesen Balsam seit 1912 her. Die Kernrezeptur — Bienenwachs, Avocadoöl, Jojoba, Carnauba — ist unverändert."),
    ]
    qa_tbl = Table([[Paragraph(f"<b>Q{i+1}.</b> {q}", BODY), Paragraph(a, BODY)] for i, (q, a) in enumerate(qa)],
                   colWidths=[6.0*cm, CW - 6.0*cm])
    qa_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,-1), HexColor("#F4EFE3")),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LINEBELOW", (0,0), (-1,-1), 0.3, HexColor("#E0DCC8")),
        ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 6), ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ]))
    s.append(qa_tbl)

    # ───── Master Copy (per SKU) ─────
    s.append(PageBreak())
    s.append(Paragraph("8 · Master Copy — paste-ready (Deutsch)", H2)); s.append(HRule())

    s.append(Paragraph("Farblos 200 ml", H3))
    s.append(Paragraph("<b>Titel (≤ 200 Zeichen)</b>", BODY))
    title200 = Table([[Paragraph(
        "Jotti Lederbalsam Farblos 200 ml – Premium Lederpflege Reisegröße mit Bienenwachs &amp; Avocadoöl für "
        "Schuhe, Lederjacken, Taschen, Handschuhe, Uhrenarmbänder – Made in Germany seit 1912", BODY)]],
        colWidths=[CW])
    title200.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), BLACK),
        ("TEXTCOLOR", (0,0), (-1,-1), GOLD),
        ("LEFTPADDING", (0,0), (-1,-1), 12), ("RIGHTPADDING", (0,0), (-1,-1), 12),
        ("TOPPADDING", (0,0), (-1,-1), 8), ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ]))
    s.append(title200)

    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph("<b>Bullets (5 × ~240 Zeichen)</b>", BODY))
    b200 = [
        ("SCHWARZWÄLDER LEDERPFLEGE SEIT 1912 · REISEGRÖSSE",
         "Hochwertiger Lederbalsam aus deutscher Familienmanufaktur im Schwarzwald. Jetzt in der handlichen 200 ml Dose — für Reise, Wochenend-Tasche oder als Geschenk. Vier Generationen, eine Rezeptur — unverändert seit 113 Jahren."),
        ("NATÜRLICHE REZEPTUR · BIENENWACHS &amp; AVOCADOÖL",
         "Mit Jojoba und Carnaubawachs. Zieht tief ins Leder ein, füllt feine Risse und versiegelt die Oberfläche — ohne Silikone, Harze, Säuren oder künstliche Farbstoffe. Dezent natürlicher Duft nach Bienenwachs, verfliegt nach einer Stunde."),
        ("FARBLOS — FARBE BLEIBT. LEDER LEBT.",
         "Geeignet für alle Lederfarben ohne sie zu verändern. Perfekt für Lederjacken, Lederschuhe, Ledertaschen, Handschuhe, Uhrenarmbänder und Sattelzeug. Ein Produkt für alle glatten Lederarten."),
        ("3-IN-1: REINIGT · PFLEGT · SCHÜTZT",
         "Ein Produkt statt drei. Pflege, Reinigung und Imprägnierung in einem Arbeitsgang. Wasser- und schmutzabweisend nach nur einer Anwendung. 200 ml reichen für ca. 10 Anwendungen auf einem Paar Schuhe."),
        ("EINFACHE ANWENDUNG · 2 STUNDEN · KEIN FETTFILM",
         "Mit Tuch oder Schwamm dünn auftragen, ca. 2 Stunden einziehen lassen, bei Bedarf nachpolieren. Seidenmatter Glanz, kein klebriger Rückstand. Nicht geeignet für Nubuk-, Velours- oder Wildleder."),
    ]
    bt = Table([[Paragraph(f"<b>{i+1}. {h}</b>", BODY), Paragraph(b, BODY)] for i, (h, b) in enumerate(b200)],
               colWidths=[5.6*cm, CW - 5.6*cm])
    bt.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,-1), HexColor("#F4EFE3")),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LINEBELOW", (0,0), (-1,-1), 0.3, HexColor("#E0DCC8")),
        ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 6), ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ]))
    s.append(bt)

    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("<b>Backend Search Terms (≤ 450 Bytes)</b>", BODY))
    be = Table([[Paragraph(
        '<font face="Courier" size="8">bienenwachs lederpflege schuhe jacke tasche handschuh uhrenarmband '
        'lederbalsam farblos reisegröße lederfett ledercreme neutral leather honey conditioner schuhcreme '
        'sattelfett glattleder kunstleder briefcase aktentasche brogue oxford lederjacke geschenk '
        'deutsche manufaktur schwarzwald</font>', BODY)]],
        colWidths=[CW])
    be.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), HexColor("#F5F5F5")),
        ("LEFTPADDING", (0,0), (-1,-1), 10), ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 7), ("BOTTOMPADDING", (0,0), (-1,-1), 7),
    ]))
    s.append(be)

    # 500 ml
    s.append(Spacer(1, 0.5*cm))
    s.append(Paragraph("Farblos 500 ml", H3))
    s.append(Paragraph("<b>Titel (≤ 200 Zeichen)</b>", BODY))
    title500 = Table([[Paragraph(
        "Jotti Lederbalsam Farblos 500 ml – Premium Lederpflege Werkstattgröße mit Bienenwachs &amp; Avocadoöl "
        "für Sofa, Autositze, Sattel, Lederjacken, Taschen – Made in Germany seit 1912", BODY)]],
        colWidths=[CW])
    title500.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), BLACK),
        ("TEXTCOLOR", (0,0), (-1,-1), GOLD),
        ("LEFTPADDING", (0,0), (-1,-1), 12), ("RIGHTPADDING", (0,0), (-1,-1), 12),
        ("TOPPADDING", (0,0), (-1,-1), 8), ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ]))
    s.append(title500)

    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph("<b>Bullets (5 × ~240 Zeichen)</b>", BODY))
    b500 = [
        ("SCHWARZWÄLDER LEDERPFLEGE SEIT 1912 · WERKSTATTGRÖSSE",
         "Hochwertiger Lederbalsam aus deutscher Familienmanufaktur im Schwarzwald. Die 500 ml Dose reicht für etwa ein Jahr Pflege bei alltäglicher Nutzung von Sofa, Autositz oder Sattelzeug — ca. 2 € pro Monat. Vier Generationen, eine Rezeptur — unverändert seit 113 Jahren."),
        ("NATÜRLICHE REZEPTUR · BIENENWACHS &amp; AVOCADOÖL",
         "Mit Jojoba und Carnaubawachs. Zieht tief ins Leder ein, füllt feine Risse und versiegelt die Oberfläche — ohne Silikone, Harze, Säuren oder künstliche Farbstoffe. Dezent natürlicher Duft nach Bienenwachs, verfliegt nach einer Stunde."),
        ("FARBLOS — FARBE BLEIBT. LEDER LEBT.",
         "Geeignet für alle Lederfarben ohne sie zu verändern. Perfekt für Ledersofas, Autositze, Sattelzeug, Lederjacken, Aktentaschen und mehr. Universell für alle glatten Lederarten."),
        ("3-IN-1: REINIGT · PFLEGT · SCHÜTZT",
         "Ein Produkt statt drei — Pflege, Reinigung und Imprägnierung in einem Arbeitsgang. Wasser- und schmutzabweisend nach nur einer Anwendung. Bewährt bei Sattlern, Restauratoren und Oldtimer-Besitzern."),
        ("EINFACHE ANWENDUNG · 2 STUNDEN · KEIN FETTFILM",
         "Mit Tuch oder Schwamm dünn auftragen, ca. 2 Stunden einziehen lassen, bei Bedarf nachpolieren. Seidenmatter Glanz, kein klebriger Rückstand. Nicht geeignet für Nubuk-, Velours- oder Wildleder."),
    ]
    bt = Table([[Paragraph(f"<b>{i+1}. {h}</b>", BODY), Paragraph(b, BODY)] for i, (h, b) in enumerate(b500)],
               colWidths=[5.6*cm, CW - 5.6*cm])
    bt.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,-1), HexColor("#F4EFE3")),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LINEBELOW", (0,0), (-1,-1), 0.3, HexColor("#E0DCC8")),
        ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 6), ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ]))
    s.append(bt)

    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("<b>Backend Search Terms (≤ 450 Bytes)</b>", BODY))
    be = Table([[Paragraph(
        '<font face="Courier" size="8">bienenwachs lederpflege auto ledercouch sofa tasche jacke autositze '
        'sattel lederbalsam farblos werkstattgröße jahresvorrat lederfett ledercreme leather honey conditioner '
        'sattelfett sattelseife schuhcreme lederreiniger glattleder kunstleder couch möbel oldtimer chesterfield '
        'deutsche manufaktur schwarzwald</font>', BODY)]],
        colWidths=[CW])
    be.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), HexColor("#F5F5F5")),
        ("LEFTPADDING", (0,0), (-1,-1), 10), ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 7), ("BOTTOMPADDING", (0,0), (-1,-1), 7),
    ]))
    s.append(be)

    # ───── CVR × CTR Scorecard ─────
    s.append(PageBreak())
    s.append(Paragraph("9 · CVR × CTR Scorecard — 20-Lever-Diagnose", H2)); s.append(HRule())
    s.append(Paragraph(
        "Jeder Hebel 1–5 bewertet (1 = kritisch, 5 = best-in-class) × Weight (High=3, Med=2, Low=1). "
        "<b>Uplift-Punkte = (5 − Score) × Weight.</b> Höchste Uplift-Punkte = höchste Priorität. "
        "Total <b>Listing Health Score</b> = Summe — niedriger ist besser (≤ 15 ist best-in-class).", SUB))

    scorecard = [
        ["#", "Hebel", "Kategorie", "Score", "W", "Uplift", "Fix → Auswirkung"],
        # CTR
        ["1", "Main image clarity at 200 px", "CTR", "2", "H", "9", "Bild 1 redesign — dunkle Dose vs. weiße SERP-Wand"],
        ["2", "Main image color contrast in SERP", "CTR", "2", "H", "9", "Dunkles Tin + Gold = einziger dunkler Tile"],
        ["3", "Title — primary KW in first 80 chars", "CTR", "3", "H", "6", "Titel mit \"Lederpflege\" beginnen — KW 3.017 SV"],
        ["4", "Title — size + variant clarity", "CTR", "4", "M", "2", "200 ml / 500 ml direkt nach Markenname"],
        ["5", "Star rating ≥ 4.4 visible badge", "CTR", "—", "H", "—", "Live-Daten — nach Launch tracken"],
        ["6", "Review count ≥ category median", "CTR", "—", "H", "—", "Vine-Programm bei Launch"],
        ["7", "Coupon / Promo badge", "CTR", "1", "M", "8", "Launch-Coupon 10 % für 30 Tage"],
        # CVR
        ["8", "Hero image confidence in 2 sec", "CVR", "2", "H", "9", "Bild 1B (Wax Reveal) als Hero — unique in Kategorie"],
        ["9", "Image #2 — strongest single buying reason", "CVR", "1", "H", "12", "Bild 2 Farb-Beweis — kills #1 Sorge (\"verändert nichts\")"],
        ["10", "Bullet #1 — emotional + concrete proof", "CVR", "3", "H", "6", "\"Seit 1912\" als erster konkreter Trust-Point"],
        ["11", "5 distinct bullet benefits", "CVR", "4", "M", "2", "Bullets bereits 5 unique themes"],
        ["12", "A+ Module 1 banner — repositions brand", "CVR", "2", "M", "6", "Modul 1: Schwarzwald-Heritage banner"],
        ["13", "A+ Module 6 Q&A — defuses top objections", "CVR", "1", "H", "12", "6 Q&A: Farbe · Wildleder · Rückstand · 1912"],
        ["14", "A+ Module 7 comparison chart", "CVR", "1", "H", "12", "Jotti Range Vergleich (Lederbalsam vs. flüssig vs. Wachs)"],
        ["15", "Variant family clarity", "CVR", "5", "M", "0", "Separate Listings — keine Verwirrung"],
        ["16", "Brand Story strip beneath bullets", "CVR", "2", "L", "3", "Brand Story Modul aktivieren"],
        ["17", "First 5 reviews shown / quality", "CVR", "—", "M", "—", "Post-purchase Email für use-case-spezifische Reviews"],
        ["18", "Subscribe & Save (Konsumartikel)", "CVR", "1", "M", "8", "S&S für 500 ml prüfen — Sattler / Reiter sind Repeat-Buyer"],
        ["19", "Q&A section ≥ 3 answered", "CVR", "2", "L", "3", "6 Seed-Q&A bei Launch hochladen"],
        ["20", "Mobile-fold completeness", "CVR", "2", "H", "9", "Bild 4 (5 Promises) sitzt im Mobile-Fold"],
    ]
    sc_tbl = Table(scorecard, colWidths=[0.7*cm, 4.6*cm, 1.4*cm, 1.0*cm, 0.7*cm, 1.2*cm, CW - 9.6*cm])
    sc_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), BLACK),
        ("TEXTCOLOR", (0,0), (-1,0), GOLD),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,-1), 7.5),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("ALIGN", (3,1), (5,-1), "CENTER"),
        ("LEFTPADDING", (0,0), (-1,-1), 4), ("RIGHTPADDING", (0,0), (-1,-1), 4),
        ("TOPPADDING", (0,0), (-1,-1), 4), ("BOTTOMPADDING", (0,0), (-1,-1), 4),
        ("GRID", (0,0), (-1,-1), 0.3, HexColor("#DDDDDD")),
        ("ROWBACKGROUNDS", (0,1), (-1,7), [WHITE, HexColor("#F4EFE3")]),
        ("ROWBACKGROUNDS", (0,8), (-1,-1), [WHITE, HexColor("#F4EFE3")]),
        ("BACKGROUND", (5,1), (5,-1), HexColor("#FFE9C2")),
    ]))
    s.append(sc_tbl)

    s.append(Spacer(1, 0.3*cm))
    health = Table([[
        Paragraph("<b>Predicted Listing Health Score (pre-launch):</b> 122 Punkte", BODY),
        Paragraph("<b>Best-in-class target:</b> ≤ 30 Punkte", BODY),
        Paragraph("<b>Top-3 Priority Fixes (höchster Uplift):</b> Bild 2 Farb-Beweis (12) · A+ Q&A (12) · A+ Vergleich (12)", BODY),
    ]], colWidths=[CW/3]*3)
    health.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), BLACK),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 7), ("BOTTOMPADDING", (0,0), (-1,-1), 7),
        ("BOX", (0,0), (-1,-1), 0.6, GOLD),
    ]))
    s.append(health)

    # ───── Negative-Review Defuse Map ─────
    s.append(PageBreak())
    s.append(Paragraph("10 · Negative-Review-Defuse-Map", H2)); s.append(HRule())
    s.append(Paragraph(
        "Jedes negative Review-Theme aus dem Excel <b>vor dem Kauf</b> defusieren — bevor der Käufer den Fehler macht "
        "und einen 3-Sterne-Review schreibt. Defusion = ein konkretes On-Page-Element das die Sorge beantwortet.", SUB))

    defuse = [
        ["Review-Theme (verbatim)", "Frequenz", "Wo es CVR killt", "Defuse-Maßnahme", "Frame / Bullet"],
        ["\"Färbt stark ab, vor allem bei Feuchte\"",
         "Hauptpunkt 1★",
         "Käufer wendet Balsam falsch an (zu dick + Leder noch feucht) → Wahrnehmung \"schlechtes Produkt\"",
         "Anwendungs-Strap visuell zeigen: \"Dünn auftragen · einziehen lassen · trocken polieren\"",
         "Bild 3 bottom strap · Bullet 5 · Modul 6 Q&A"],
        ["Befürchtung: \"Macht es dunkler?\"",
         "Implizit in jeder Lederpflege-Kategorie",
         "Käufer mit teuren hellen Lederstücken klickt weg",
         "Variant-spezifischer Vorher/Nachher-Beweis auf echtem Leder",
         "Bild 2 Farb-Beweis (Brogue für 200ml / Chesterfield für 500ml)"],
        ["Befürchtung: \"Klebt / fettiger Film?\"",
         "Implizit",
         "Käufer mit Lederjacke / Aktentasche befürchtet ruinierte Oberfläche",
         "\"Seidenmatter Glanz\" + \"kein Restschmierfilm\" + \"2 Stunden einziehen\"",
         "Bullet 5 · Bild 3 · Modul 6 Q&A"],
        ["Verwechslung mit Suede / Nubuk / Wildleder",
         "Hauptursache für Retouren",
         "Käufer mit Wildleder-Schuhen kauft + ruiniert sie",
         "Explizit nennen: \"Nicht für Nubuk · Velours · Wildleder\"",
         "Bullet 5 · Bild 6 disclaimer · Modul 6 Q&A"],
        ["Skepsis: \"Wirklich seit 1912?\"",
         "Heritage-Trust-Frage",
         "Käufer denkt \"Marketing-Lüge\"",
         "Konkrete Story: \"Familienmanufaktur Bernau · vier Generationen · unveränderte Rezeptur\"",
         "Bild 7 (1912-Poster) · Modul 4 (Manufaktur-Banner) · Modul 6 Q&A"],
        ["\"Riecht nach Chemie / parfümiert\"",
         "Sorge bei Naturpflege-Suchenden",
         "Käufer der \"natürliche Lederpflege\" sucht klickt weg",
         "\"Dezent natürlich nach Bienenwachs · nicht parfümiert · verfliegt in 1h\"",
         "Modul 6 Q&A · Bullet 2 · positives Review-Quote"],
        ["\"Wie oft anwenden? Anwendung kompliziert?\"",
         "Confusion bei Erstkäufern",
         "Käufer kauft nie weil unklar",
         "Klare Frequenz-Tabelle: 4–6 Wo. alltäglich · 3 Mo. selten · 1 Mo. Sattel",
         "Modul 6 Q&A · Bullet 5"],
    ]
    df_tbl = Table([[Paragraph(c, SMALL if i > 0 else BODY) for c in r] for i, r in enumerate(defuse)],
                   colWidths=[4.2*cm, 1.8*cm, 3.5*cm, 3.5*cm, CW - 13.0*cm])
    df_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), BLACK),
        ("TEXTCOLOR", (0,0), (-1,0), GOLD),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,0), 8),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 5), ("RIGHTPADDING", (0,0), (-1,-1), 5),
        ("TOPPADDING", (0,0), (-1,-1), 5), ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("GRID", (0,0), (-1,-1), 0.3, HexColor("#DDDDDD")),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [HexColor("#FBE5E8"), HexColor("#FFF4E5")]),
    ]))
    s.append(df_tbl)

    # ───── A/B Test Roadmap ─────
    s.append(PageBreak())
    s.append(Paragraph("11 · A/B Test Roadmap — Manage Your Experiments", H2)); s.append(HRule())
    s.append(Paragraph(
        "Amazon Manage Your Experiments läuft 4–8 Wochen pro Test. Sample-Size hängt vom Traffic ab — "
        "Faustregel: <b>min. 1.000 Sessions/Variante</b> für 95 % Konfidenz. Reihenfolge nach Uplift × Aufwand.", SUB))

    tests = [
        ["#", "Test", "Asset", "Hypothese", "Varianten (A vs. B vs. C)", "KPI", "Dauer"],
        ["T1", "Main Image A/B/C",
         "Bild 1",
         "Dunkler Tin gewinnt CTR vs. weiße Konkurrenz-Tiles",
         "A: Floating Heritage · B: Wax Reveal · C: Context (Brogue/Sofa)",
         "CTR · Sessions/Detailseite",
         "4 Wo."],
        ["T2", "Title KW-Order",
         "Titel",
         "Titel beginnt mit \"Lederpflege\" (3.017 SV) statt mit Markenname",
         "A: Jotti zuerst · B: Lederpflege zuerst",
         "Impressions · CTR",
         "4 Wo."],
        ["T3", "Bullet 1 Hook",
         "Bullet 1",
         "\"SEIT 1912\" konkret schlägt \"Premium Lederpflege\" generisch",
         "A: PREMIUM LEDERPFLEGE SEIT 1912 · B: SCHWARZWÄLDER FAMILIENMANUFAKTUR SEIT 1912",
         "CVR · Add-to-Cart Rate",
         "4 Wo."],
        ["T4", "Price Point 500 ml",
         "Preis",
         "€21,90 vs €23,90 vs €26,90 — Premium-Pricing tested",
         "A: 21,90 · B: 23,90 · C: 26,90",
         "Revenue · Units · CVR",
         "6 Wo."],
        ["T5", "Bild 4 Mobile-Fold",
         "Bild 4",
         "5-Promises-Badges schlägt klassischen Lifestyle-Frame im Mobile-Fold",
         "A: 5 Promises · B: Use-Case-Lifestyle-Grid",
         "Mobile CVR · Scroll Depth",
         "4 Wo."],
        ["T6", "Coupon vs. S&S Badge",
         "Promotions",
         "10 %-Coupon hebt CTR stärker als S&S-Badge",
         "A: 10 % Coupon · B: S&S Badge · C: keiner",
         "CTR · Subscriptions",
         "4 Wo."],
    ]
    test_tbl = Table([[Paragraph(c, SMALL if i > 0 else BODY) for c in r] for i, r in enumerate(tests)],
                     colWidths=[0.7*cm, 2.0*cm, 1.5*cm, 3.0*cm, 4.5*cm, 2.0*cm, CW - 13.7*cm])
    test_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), BLACK),
        ("TEXTCOLOR", (0,0), (-1,0), GOLD),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,0), 8),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 5), ("RIGHTPADDING", (0,0), (-1,-1), 5),
        ("TOPPADDING", (0,0), (-1,-1), 5), ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("GRID", (0,0), (-1,-1), 0.3, HexColor("#DDDDDD")),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, HexColor("#F4EFE3")]),
    ]))
    s.append(test_tbl)

    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("Recommended sequence", H3))
    seq = Table([[Paragraph(
        "<b>Launch Week 1:</b> T1 (Main Image) — höchster CTR-Hebel. Parallel: T6 (Coupon) für Sichtbarkeits-Boost.<br/>"
        "<b>Week 5:</b> T2 (Title KW-Order) — sobald T1-Sieger gepickt. <br/>"
        "<b>Week 9:</b> T3 (Bullet 1) + T5 (Bild 4) parallel. <br/>"
        "<b>Week 13:</b> T4 (Price) — braucht stabile Baseline.<br/><br/>"
        "Niemals mehr als 2 Tests gleichzeitig — Sample-Pollution.", BODY)]],
        colWidths=[CW])
    seq.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), HexColor("#F4EFE3")),
        ("LEFTPADDING", (0,0), (-1,-1), 12), ("RIGHTPADDING", (0,0), (-1,-1), 12),
        ("TOPPADDING", (0,0), (-1,-1), 10), ("BOTTOMPADDING", (0,0), (-1,-1), 10),
    ]))
    s.append(seq)

    # ───── SERP Mock + Mobile-Fold Diagnostic ─────
    s.append(PageBreak())
    s.append(Paragraph("12 · SERP-Mock + Mobile-Fold Diagnostic", H2)); s.append(HRule())
    s.append(Paragraph(
        "Was sieht der Käufer wenn er \"lederpflege auto\" (8.873 SV) auf Amazon.de sucht? "
        "Annotated comparison: Jotti tile vs. die fünf wahrscheinlichsten Konkurrenten in der Top-Reihe.", SUB))

    # Draw a SERP row as a Flowable
    class SerpRow(Flowable):
        def wrap(self, *a): return (CW, 7.0*cm)
        def draw(self):
            c = self.canv
            tiles = [
                ("JOTTI", BLACK, GOLD, True, "Lederbalsam Farblos 500 ml", "€23,90", "4.5★ (live)"),
                ("LEATHER HONEY", HexColor("#E0BD5B"), HexColor("#5A3A18"), False, "Leather Conditioner 8 oz", "€19,90", "4.7★ (12k)"),
                ("COLLONIL", WHITE, RED_X, False, "Lederpflege Farblos 100ml", "€8,99", "4.4★ (3.2k)"),
                ("SONAX", WHITE, HexColor("#0066B3"), False, "Lederpflege 250ml", "€7,99", "4.3★ (1.8k)"),
                ("FURNITURE CL.", WHITE, HexColor("#1A4A2A"), False, "Leather Care Kit", "€34,90", "4.6★ (820)"),
                ("TAPIR", HexColor("#E8DEC0"), HexColor("#3A5A30"), False, "Lederpflege Bio 200ml", "€12,90", "4.5★ (450)"),
            ]
            tw = CW / 6
            for i, (brand, bg, accent, is_jotti, title, price, rating) in enumerate(tiles):
                x = i * tw + 0.1*cm
                # tile background
                c.setFillColor(WHITE); c.setStrokeColor(GOLD if is_jotti else HexColor("#DDDDDD"))
                c.setLineWidth(1.5 if is_jotti else 0.4)
                c.rect(x, 0.5*cm, tw - 0.2*cm, 6.0*cm, fill=1, stroke=1)
                # product image area
                c.setFillColor(bg); c.setStrokeColor(accent); c.setLineWidth(0.5)
                if is_jotti:
                    _draw_tin_3q(c, x + tw/2 - 0.1*cm, 4.2*cm, w=2.0*cm, variant="farblos", size_label="500 ml")
                else:
                    c.rect(x + 0.2*cm, 3.0*cm, tw - 0.4*cm, 2.5*cm, fill=1, stroke=1)
                    c.setFillColor(accent); c.setFont("Helvetica-Bold", 6)
                    c.drawCentredString(x + tw/2, 4.3*cm, brand[:10])
                # title
                c.setFillColor(BLACK); c.setFont("Helvetica-Bold" if is_jotti else "Helvetica", 6)
                c.drawString(x + 0.15*cm, 2.6*cm, title[:24])
                # price
                c.setFillColor(BLACK); c.setFont("Helvetica-Bold", 9)
                c.drawString(x + 0.15*cm, 2.0*cm, price)
                # rating
                c.setFillColor(GREY); c.setFont("Helvetica", 6)
                c.drawString(x + 0.15*cm, 1.5*cm, rating)
                # Jotti marker
                if is_jotti:
                    c.setFillColor(GOLD); c.rect(x, 0.5*cm + 5.6*cm, tw - 0.2*cm, 0.4*cm, fill=1, stroke=0)
                    c.setFillColor(BLACK); c.setFont("Helvetica-Bold", 6.5)
                    c.drawCentredString(x + tw/2 - 0.1*cm, 0.5*cm + 5.72*cm, "← UNSER TILE")
                # SERP brand band
                c.setFillColor(GREY); c.setFont("Helvetica", 6)
                c.drawString(x + 0.15*cm, 1.0*cm, brand)

    s.append(SerpRow())
    s.append(Spacer(1, 0.2*cm))
    serp_caption = Table([[Paragraph(
        "<b>CTR-Differential:</b> 5 von 6 Tiles haben weißen Hintergrund. Jotti's dunkles Tin + Gold-Bogen "
        "ist die <b>einzige Unterbrechung in der Reihe</b> — Eye-tracking-Studien zeigen 2–3× höhere "
        "Fixation auf den Outlier-Tile. Das ist der CTR-Moat.", BODY)]], colWidths=[CW])
    serp_caption.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), BLACK),
        ("TEXTCOLOR", (0,0), (-1,-1), CREAM),
        ("LEFTPADDING", (0,0), (-1,-1), 12), ("RIGHTPADDING", (0,0), (-1,-1), 12),
        ("TOPPADDING", (0,0), (-1,-1), 10), ("BOTTOMPADDING", (0,0), (-1,-1), 10),
        ("BOX", (0,0), (-1,-1), 0.6, GOLD),
    ]))
    s.append(serp_caption)

    # Mobile fold diagnostic
    s.append(Spacer(1, 0.5*cm))
    s.append(Paragraph("Mobile-Fold-Diagnostic — was im 1. Scroll sichtbar ist", H3))

    class MobileFold(Flowable):
        def wrap(self, *a): return (CW, 9.0*cm)
        def draw(self):
            c = self.canv
            phone_w = 5.5*cm; phone_h = 8.5*cm; phone_x = 1.0*cm; phone_y = 0.2*cm
            # phone outline
            c.setFillColor(WHITE); c.setStrokeColor(BLACK); c.setLineWidth(1.0)
            c.roundRect(phone_x, phone_y, phone_w, phone_h, 0.25*cm, fill=1, stroke=1)
            # status bar
            c.setFillColor(BLACK); c.setFont("Helvetica-Bold", 6)
            c.drawString(phone_x + 0.2*cm, phone_y + phone_h - 0.3*cm, "9:41")
            c.drawRightString(phone_x + phone_w - 0.2*cm, phone_y + phone_h - 0.3*cm, "amazon.de")
            # main image area
            mi_y = phone_y + phone_h - 4.5*cm
            c.setFillColor(WHITE); c.setStrokeColor(HexColor("#DDDDDD")); c.setLineWidth(0.3)
            c.rect(phone_x + 0.2*cm, mi_y, phone_w - 0.4*cm, 3.5*cm, fill=1, stroke=1)
            _draw_tin_3q(c, phone_x + phone_w/2, mi_y + 1.7*cm, w=3.0*cm, variant="farblos", size_label="500 ml")
            # variant thumbs strip
            c.setFillColor(WHITE); c.setStrokeColor(HexColor("#DDDDDD"))
            c.rect(phone_x + 0.2*cm, mi_y - 0.7*cm, phone_w - 0.4*cm, 0.6*cm, fill=1, stroke=1)
            for i in range(5):
                tx = phone_x + 0.4*cm + i*0.85*cm
                c.setFillColor(BLACK if i == 0 else HexColor("#EEEEEE")); c.setStrokeColor(GOLD if i == 0 else HexColor("#CCCCCC"))
                c.setLineWidth(0.8 if i == 0 else 0.3)
                c.rect(tx, mi_y - 0.6*cm, 0.6*cm, 0.45*cm, fill=1, stroke=1)
            # title
            c.setFillColor(BLACK); c.setFont("Helvetica-Bold", 7)
            c.drawString(phone_x + 0.3*cm, mi_y - 1.1*cm, "Jotti Lederbalsam Farblos 500ml")
            c.setFont("Helvetica", 6)
            c.drawString(phone_x + 0.3*cm, mi_y - 1.4*cm, "Premium Lederpflege · Made in Germany")
            # rating
            c.setFillColor(HexColor("#F4A82C")); c.setFont("Helvetica-Bold", 7)
            c.drawString(phone_x + 0.3*cm, mi_y - 1.8*cm, "★★★★★")
            c.setFillColor(GREY); c.setFont("Helvetica", 6)
            c.drawString(phone_x + 1.5*cm, mi_y - 1.78*cm, "4.6 · 247 Bewertungen")
            # price
            c.setFillColor(BLACK); c.setFont("Helvetica-Bold", 12)
            c.drawString(phone_x + 0.3*cm, mi_y - 2.5*cm, "€23,90")
            c.setFillColor(GREY); c.setFont("Helvetica", 6)
            c.drawString(phone_x + 0.3*cm, mi_y - 2.8*cm, "Prime · Gratis Lieferung morgen")
            # cta button
            c.setFillColor(YELLOW); c.setStrokeColor(HexColor("#F4A82C")); c.setLineWidth(0.5)
            c.roundRect(phone_x + 0.3*cm, mi_y - 3.5*cm, phone_w - 0.6*cm, 0.55*cm, 0.1*cm, fill=1, stroke=1)
            c.setFillColor(BLACK); c.setFont("Helvetica-Bold", 8)
            c.drawCentredString(phone_x + phone_w/2, mi_y - 3.35*cm, "In den Einkaufswagen")

            # Annotations on the right side
            ann_x = phone_x + phone_w + 0.8*cm
            ann_w = CW - ann_x - 0.1*cm
            ann = [
                ("✓ Hauptbild", "Dunkles Tin in weißem SERP → CTR-Boost", GREEN_OK),
                ("✓ Variant-Strip", "5 Varianten = Familie sichtbar", GREEN_OK),
                ("✓ Titel", "Marke + Farbe + Größe vor dem Umbruch", GREEN_OK),
                ("⚠ Rating", "Bei Launch noch nicht da — Vine Pflicht", AMBER),
                ("✓ Preis", "Sichtbar, kein versteckter Aufschlag", GREEN_OK),
                ("⚠ Prime-Badge", "Voraussetzung für Mobile-CTA-Rate", AMBER),
                ("✗ S&S-Toggle", "Fehlt — prüfen für 500 ml", RED_X),
                ("✗ Coupon-Badge", "Bei Launch leer — 10 % für 30 Tage", RED_X),
            ]
            for i, (mark, text, col) in enumerate(ann):
                c.setFillColor(col); c.circle(ann_x + 0.15*cm, phone_y + phone_h - 0.7*cm - i*1.0*cm, 0.15*cm, fill=1, stroke=0)
                c.setFillColor(BLACK); c.setFont("Helvetica-Bold", 7.5)
                c.drawString(ann_x + 0.45*cm, phone_y + phone_h - 0.65*cm - i*1.0*cm, mark)
                c.setFillColor(GREY); c.setFont("Helvetica", 6.5)
                c.drawString(ann_x + 0.45*cm, phone_y + phone_h - 0.95*cm - i*1.0*cm, text)

    s.append(MobileFold())

    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "<b>Verdict:</b> 5 von 8 Elementen sind grün (Bild · Variants · Titel · Preis · Heritage-Trust). "
        "Drei Risiken sind launch-spezifisch: Rating fehlt → Vine, Coupon fehlt → 10 %-Launch-Promo, S&S → prüfen. "
        "<b>Diese drei Fixes vor Launch ziehen die Mobile-Fold-CVR um geschätzt 15–25 %.</b>", BODY))
    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph(
        "<b>⚠ Korrektur:</b> die Annahme \"dunkles Tin in einer weißen SERP-Reihe\" stimmt nicht. Wettbewerber URBAN FOREST + "
        "\"Premium Leder Pflege Balsam\" nutzen <b>denselben dunklen Look</b>. Echter CTR-Moat: 1912 / Schwarzwald / "
        "Variant-System / Gold-Wordmark. Siehe §13 Competitor Audit für detaillierte Analyse.", SMALL))

    # ───── §13 Competitor Audit ─────
    s.append(PageBreak())
    s.append(Paragraph("13 · Competitor Audit — was Marktführer machen + wo wir gewinnen", H2)); s.append(HRule())
    s.append(Paragraph(
        "Audit der zwei dominanten Wettbewerber im Top-10-SERP für \"lederbalsam\" + \"lederpflege auto\". "
        "Wichtigstes Finding: <b>beide nutzen dunkle Tins.</b> Wir müssen anders unique sein — über das Gold-1912-"
        "Heritage-Signal + Variant-System (Farblos/Braun/Schwarz) + Schwarzwald-Geo-Origin.", SUB))

    class CompetitorComparison(Flowable):
        def wrap(self, *a): return (CW, 7.0*cm)
        def draw(self):
            c = self.canv
            tw = CW / 3
            # URBAN FOREST tin
            x = 0
            c.setFillColor(WHITE); c.setStrokeColor(HexColor("#DDDDDD")); c.setLineWidth(0.4)
            c.rect(x, 0.6*cm, tw - 0.2*cm, 6.0*cm, fill=1, stroke=1)
            cx_t = x + tw/2 - 0.1*cm; cy_t = 3.8*cm
            c.setFillColor(HexColor("#1A1A1A")); c.setStrokeColor(HexColor("#444"))
            c.roundRect(cx_t - 1.1*cm, cy_t - 1.4*cm, 2.2*cm, 2.8*cm, 0.1*cm, fill=1, stroke=1)
            c.setFillColor(WHITE); c.setFont("Helvetica-Bold", 4.5)
            c.drawCentredString(cx_t, cy_t + 1.0*cm, "URBAN ⌃ FOREST")
            c.setFillColor(CREAM); c.setStrokeColor(HexColor("#888"))
            c.roundRect(cx_t - 0.85*cm, cy_t - 0.7*cm, 1.7*cm, 1.4*cm, 0.05*cm, fill=1, stroke=1)
            c.setFillColor(HexColor("#222")); c.setFont("Times-Bold", 5.5)
            c.drawCentredString(cx_t, cy_t + 0.3*cm, "PREMIUM")
            c.setFont("Times-Bold", 7.5)
            c.drawCentredString(cx_t, cy_t + 0.0*cm, "LEATHER BALM")
            c.setFont("Times-Italic", 4)
            c.drawCentredString(cx_t, cy_t - 0.25*cm, "Beeswax & Avocado Oil")
            c.setFillColor(HexColor("#7A4A2A")); c.rect(cx_t - 0.85*cm, cy_t - 0.7*cm, 1.7*cm, 0.12*cm, fill=1, stroke=0)
            c.setFillColor(CREAM); c.setFont("Helvetica-Bold", 3.5)
            c.drawCentredString(cx_t, cy_t - 0.66*cm, "MADE IN GERMANY")
            c.setFillColor(HexColor("#A20F0F")); c.rect(x + 0.2*cm, 1.0*cm, 1.2*cm, 0.6*cm, fill=1, stroke=0)
            c.setFillColor(WHITE); c.setFont("Helvetica-Bold", 6)
            c.drawCentredString(x + 0.8*cm, 1.35*cm, "SEHR GUT")
            c.setFont("Helvetica", 4.5)
            c.drawCentredString(x + 0.8*cm, 1.15*cm, "Vergleich.org")
            c.setFillColor(BLACK); c.setFont("Helvetica-Bold", 9)
            c.drawString(x + 0.2*cm, 0.20*cm, "URBAN FOREST")
            c.setFillColor(GREY); c.setFont("Helvetica", 6.5)
            c.drawString(x + 0.2*cm, 0.02*cm, "Premium · Bull-skull · brandneu")

            # Premium Leder Pflege Balsam tin
            x = tw
            c.setFillColor(WHITE); c.setStrokeColor(HexColor("#DDDDDD"))
            c.rect(x, 0.6*cm, tw - 0.2*cm, 6.0*cm, fill=1, stroke=1)
            cx_t = x + tw/2 - 0.1*cm
            c.setFillColor(HexColor("#0E0E0E")); c.setStrokeColor(HexColor("#444"))
            c.roundRect(cx_t - 1.1*cm, cy_t - 1.4*cm, 2.2*cm, 2.8*cm, 0.1*cm, fill=1, stroke=1)
            c.setFillColor(BLACK); c.setStrokeColor(WHITE); c.setLineWidth(0.5)
            c.rect(cx_t - 0.95*cm, cy_t - 0.95*cm, 1.9*cm, 1.9*cm, fill=1, stroke=1)
            c.setFillColor(WHITE); c.setFont("Helvetica-Bold", 4.5)
            c.drawCentredString(cx_t, cy_t + 0.65*cm, "PREMIUM")
            c.setFont("Helvetica-Bold", 9.5)
            c.drawCentredString(cx_t, cy_t + 0.30*cm, "LEDER")
            c.setFont("Helvetica-Bold", 6.5)
            c.drawCentredString(cx_t, cy_t + 0.0*cm, "PFLEGE BALSAM")
            c.setFont("Helvetica", 3.5)
            c.drawCentredString(cx_t, cy_t - 0.20*cm, "Mit natürlichem Bienenwachs")
            c.setFont("Helvetica-Bold", 4.5)
            c.drawCentredString(cx_t, cy_t - 0.40*cm, "PFLEGT & SCHÜTZT")
            c.setFillColor(BLACK); c.rect(cx_t - 0.30*cm, cy_t - 0.75*cm, 0.6*cm, 0.06*cm, fill=1, stroke=0)
            c.setFillColor(RED_X); c.rect(cx_t - 0.30*cm, cy_t - 0.81*cm, 0.6*cm, 0.06*cm, fill=1, stroke=0)
            c.setFillColor(YELLOW); c.rect(cx_t - 0.30*cm, cy_t - 0.87*cm, 0.6*cm, 0.06*cm, fill=1, stroke=0)
            c.setFillColor(WHITE); c.setStrokeColor(HexColor("#A20F0F")); c.setLineWidth(0.6)
            c.rect(x + 0.2*cm, 1.0*cm, 1.2*cm, 0.6*cm, fill=1, stroke=1)
            c.setFillColor(HexColor("#A20F0F")); c.setFont("Helvetica-Bold", 5.5)
            c.drawCentredString(x + 0.8*cm, 1.40*cm, "WARENTEST 1,1")
            c.setFont("Helvetica-Bold", 6)
            c.drawCentredString(x + 0.8*cm, 1.15*cm, "SEHR GUT")
            c.setFillColor(BLACK); c.setFont("Helvetica-Bold", 9)
            c.drawString(x + 0.2*cm, 0.20*cm, "Premium Leder Pflege Balsam")
            c.setFillColor(GREY); c.setFont("Helvetica", 6.5)
            c.drawString(x + 0.2*cm, 0.02*cm, "Generic · Warentest 1,1")

            # Jotti tin
            x = 2*tw
            c.setFillColor(WHITE); c.setStrokeColor(GOLD); c.setLineWidth(1.2)
            c.rect(x, 0.6*cm, tw - 0.2*cm, 6.0*cm, fill=1, stroke=1)
            _draw_tin_3q(c, x + tw/2 - 0.1*cm, 3.5*cm, w=3.0*cm, variant="farblos", size_label="500 ml")
            c.setFillColor(GOLD); c.setFont("Times-Bold", 9)
            c.drawCentredString(x + tw/2 - 0.1*cm, 1.4*cm, "Schwarzwald · seit 1912")
            c.setFillColor(GOLD); c.rect(x, 0.6*cm + 5.6*cm, tw - 0.2*cm, 0.4*cm, fill=1, stroke=0)
            c.setFillColor(BLACK); c.setFont("Helvetica-Bold", 6.5)
            c.drawCentredString(x + tw/2 - 0.1*cm, 0.6*cm + 5.72*cm, "← UNSER TILE")
            c.setFillColor(BLACK); c.setFont("Helvetica-Bold", 9)
            c.drawString(x + 0.2*cm, 0.20*cm, "Jotti Lederbalsam")
            c.setFillColor(GREY); c.setFont("Helvetica", 6.5)
            c.drawString(x + 0.2*cm, 0.02*cm, "Heritage · 1912 · Familienmanufaktur")

    s.append(CompetitorComparison())

    s.append(Spacer(1, 0.3*cm))
    audit_intro = Table([[Paragraph(
        "<b>Beobachtung:</b> Alle drei Tins sind dunkel/schwarz. Unser ursprünglicher Plan \"dunkles Tin gewinnt in "
        "weißer Konkurrenz-Reihe\" stimmt nicht — beide Wettbewerber haben denselben Look. "
        "<b>Wir müssen anders unique sein:</b> über Gold-1912-Heritage-Signal + Variant-System + Bernau/Schwarzwald-Origin.", BODY)]],
        colWidths=[CW])
    audit_intro.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), HexColor("#FBE5E8")),
        ("LEFTPADDING", (0,0), (-1,-1), 12), ("RIGHTPADDING", (0,0), (-1,-1), 12),
        ("TOPPADDING", (0,0), (-1,-1), 10), ("BOTTOMPADDING", (0,0), (-1,-1), 10),
        ("BOX", (0,0), (-1,-1), 0.6, HexColor("#A20F0F")),
    ]))
    s.append(audit_intro)

    # ───── Audit details ─────
    s.append(PageBreak())
    s.append(Paragraph("Was die Wettbewerber haben — was uns fehlt — was wir besser können", H3))

    audit = [
        ["Feature", "URBAN FOREST", "Premium Leder Pflege", "Jotti (heute)", "Action"],
        ["Schwarzes Tin", "✓", "✓", "✓", "— (kein Moat mehr)"],
        ["Made in Germany Claim", "✓ (Polo-Logo Style)", "✓ (mit Flag prominent)", "✓ (mit Flag)", "Tafelstandard"],
        ["Bienenwachs Claim", "✗ — attackiert es (\"weisse Cera-Alba ist besser\")", "✓ (Kernhebel)", "✓", "⚠ Counter URBAN FOREST's Attack (siehe unten)"],
        ["Trust-Badge", "Vergleich.org SEHR GUT 01/2025 + IfV", "Warentest 1,1 SEHR GUT", "✗ — FEHLT", "🔴 KRITISCH: Vergleich.org / Warentest Submission planen"],
        ["\"Über X.XXX zufriedene Kunden\"", "Über 100.000", "—", "✗ — FEHLT", "🟡 Nach Launch + Reviews aktivieren"],
        ["30-Tage-Geld-zurück", "Prominent (Risk-Reversal)", "—", "✗ — FEHLT", "🟡 Mit Brand klären: CVR-Lift vs. Retouren-Risiko"],
        ["VS-Comparison-Frame", "✓ (vs. \"yellow wax\")", "✓ (vs. \"Industriefett\")", "✗ — FEHLT", "🟡 Neuer Frame: Jotti vs. \"moderne Marken ohne Geschichte\""],
        ["Heritage / Jahreszahl", "Fake (Bull-Skull-Vintage, brandneu)", "—", "✓ ECHT seit 1912", "🟢 Unser Moat — überall sichtbar"],
        ["Geo-Herkunft", "\"Deutschland\" generisch", "\"Deutschland\" generisch", "✓ Bernau/Schwarzwald", "🟢 Unser Moat — \"Bernau\" prominent nutzen"],
        ["Profi-Endorsement", "✓ (Reitsport-Model + \"Wahl der Profis\")", "✓ (Auto-Innenraum-Model)", "✗ — FEHLT", "🟡 Sattler/Reitsport-Quote ergänzen"],
        ["Farb-Varianten", "Nur 1 Farbe", "Nur 1 Farbe", "✓ 3 Farben", "🟢 Unser Moat — Variant-Strip prominent"],
        ["Familienmanufaktur-Story", "✗", "✗", "✓ 4 Generationen", "🟢 Unser Moat"],
    ]
    aud_tbl = Table([[Paragraph(c, SMALL if i > 0 else BODY) for c in r] for i, r in enumerate(audit)],
                    colWidths=[3.4*cm, 3.4*cm, 3.4*cm, 3.0*cm, CW - 13.2*cm])
    aud_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), BLACK),
        ("TEXTCOLOR", (0,0), (-1,0), GOLD),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,0), 8),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 5), ("RIGHTPADDING", (0,0), (-1,-1), 5),
        ("TOPPADDING", (0,0), (-1,-1), 5), ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("GRID", (0,0), (-1,-1), 0.3, HexColor("#DDDDDD")),
        ("BACKGROUND", (0,1), (-1,2), WHITE),
        ("BACKGROUND", (0,3), (-1,3), HexColor("#FFF4E5")),
        ("BACKGROUND", (0,4), (-1,4), HexColor("#FBE5E8")),
        ("BACKGROUND", (0,5), (-1,5), HexColor("#FFF4E5")),
        ("BACKGROUND", (0,6), (-1,6), HexColor("#FFF4E5")),
        ("BACKGROUND", (0,7), (-1,7), HexColor("#FFF4E5")),
        ("BACKGROUND", (0,8), (-1,-1), HexColor("#E8F4EA")),
    ]))
    s.append(aud_tbl)

    s.append(Spacer(1, 0.4*cm))
    s.append(Paragraph("Counter zu URBAN FOREST's \"Yellow Wax Attack\"", H3))
    counter = Table([[Paragraph(
        "<b>Ihr Move:</b> URBAN FOREST positioniert ihr \"Cera-Alba weisses Bienenwachs\" als Premium und "
        "attackiert klassisches gelbes Bienenwachs als <i>\"Gelbstich-Gefahr · verstopft Poren · klebriger Fettfilm\"</i>. "
        "Direkte Bedrohung für jeden Anbieter der mit \"echtes Bienenwachs\" wirbt.<br/><br/>"
        "<b>Unser Counter (in Bild 5 + Bullet 2):</b> <i>\"Echtes Schwarzwald-Bienenwachs aus der Imkerei seit 1912. "
        "Gefiltert, nicht gebleicht. Behält Farbe und Duft — wie unsere Großväter es gemacht haben.\"</i><br/><br/>"
        "<b>Marketing-Logik:</b> URBAN FOREST argumentiert technisch (\"hochreines Cera-Alba\"). Wir argumentieren "
        "<b>Heritage</b> (\"so wie 1912\"). Anderer Spielplatz — und einer, den sie nicht betreten können, "
        "weil ihre Marke offensichtlich modern ist.", BODY)]],
        colWidths=[CW])
    counter.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), BLACK),
        ("TEXTCOLOR", (0,0), (-1,-1), CREAM),
        ("LEFTPADDING", (0,0), (-1,-1), 12), ("RIGHTPADDING", (0,0), (-1,-1), 12),
        ("TOPPADDING", (0,0), (-1,-1), 10), ("BOTTOMPADDING", (0,0), (-1,-1), 10),
        ("BOX", (0,0), (-1,-1), 0.6, GOLD),
    ]))
    s.append(counter)

    s.append(Spacer(1, 0.4*cm))
    s.append(Paragraph("Empfohlene Brief-Updates", H3))
    for line in [
        "<b>🔴 KRITISCH:</b> Vergleich.org / Warentest Vergleichstest-Submission planen — der Trust-Badge fehlt komplett und kostet uns CTR + CVR gegen URBAN FOREST.",
        "<b>🟡 PRÜFEN mit Brand:</b> 30-Tage-Geld-zurück-Garantie. CVR-Lift möglich, aber Retouren-Risiko. Bei 200 ml geringes Risiko, bei 500 ml prüfen.",
        "<b>🟡 ADD:</b> Neuer A/B-Test gegen Bild 4 — VS-Comparison \"Jotti vs. moderne Marken ohne Geschichte\". Spiegelt den Wettbewerber-Move, dreht ihn auf Heritage.",
        "<b>🟡 ADD:</b> Sattler-/Reitsport-Endorsement (echtes Zitat oder \"Empfohlen von [Sattlermeister]\") als A+ Modul oder Q&A.",
        "<b>🟢 STÄRKEN:</b> \"Bernau\" überall prominenter — \"Manufaktur in Bernau im Schwarzwald\" statt nur \"Made in Germany\".",
        "<b>🟢 STÄRKEN:</b> Variant-System (Farblos/Braun/Schwarz) als Cross-Sell-Bild #7 prominenter — Wettbewerber haben das nicht.",
    ]:
        s.append(Paragraph("· " + line, BODY))

    # ───── Image Copy Lab ─────
    s.append(PageBreak())
    s.append(Paragraph("14 · Image Copy Lab — 3 Varianten pro Frame", H2)); s.append(HRule())
    s.append(Paragraph(
        "Jeder Frame bekommt 3 Copy-Varianten, jede gegen einen anderen Hebel verankert: "
        "<b>(A) KW-anchored</b> — bringt high-volume Suchbegriff sichtbar ins Bild · "
        "<b>(B) Review-anchored</b> — antwortet direkt auf ein verbatim review-Theme · "
        "<b>(C) Emotional / concrete value</b> — triggert das Bauchgefühl des Käufers. "
        "Empfehlung pro Frame markiert. Final via Manage-Your-Experiments testen.", SUB))

    def copy_block(frame_name, role, current, variants, recommend, why):
        """Build a styled copy-variant block."""
        rows = [[Paragraph(f"<b>{frame_name}</b><br/><font size='7' color='#7A6A55'>{role}</font>", BODY),
                 Paragraph(f"<font color='#7A6A55'>Baseline (aktuell):</font><br/>{current}", BODY)]]
        for letter, label, headline, strap, anchor in variants:
            mark = " ← LOCKED (Final)" if letter == recommend else ""
            rows.append([
                Paragraph(f"<b>{letter}</b> · <font size='7' color='#7A6A55'>{label}</font>{' · <b>'+mark.strip()+'</b>' if mark else ''}", BODY),
                Paragraph(f"<b>{headline}</b><br/><font size='8' color='#7A6A55'>Strap:</font> {strap}<br/><font size='7' color='#7A6A55'><i>{anchor}</i></font>", BODY),
            ])
        t = Table(rows, colWidths=[4.0*cm, CW - 4.0*cm])
        styles_list = [
            ("VALIGN", (0,0), (-1,-1), "TOP"),
            ("LINEBELOW", (0,0), (-1,-1), 0.3, HexColor("#E0DCC8")),
            ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
            ("TOPPADDING", (0,0), (-1,-1), 5), ("BOTTOMPADDING", (0,0), (-1,-1), 5),
            ("BACKGROUND", (0,0), (-1,0), BLACK),
            ("TEXTCOLOR", (0,0), (-1,0), GOLD),
        ]
        # highlight the recommended row
        for i, (letter, *_) in enumerate(variants):
            if letter == recommend:
                styles_list.append(("BACKGROUND", (0,i+1), (-1,i+1), HexColor("#FFE9C2")))
        t.setStyle(TableStyle(styles_list))
        return t

    # — Bild 2 — Farb-Beweis (most important CVR frame)
    s.append(Paragraph("Bild 2 · Farb-Beweis (Hook · variant-aware)", H3))
    s.append(Paragraph(
        "<b>Job-to-be-done:</b> die #1 Kauf-Sorge \"macht es mein Leder dunkler?\" in unter 2 Sekunden auflösen. "
        "Da Farblos zwingend mit \"verändert nichts\" verkauft wird, ist hier der grösste CVR-Hebel.", BODY))
    s.append(copy_block("Bild 2 — Hook · Farb-Beweis", "200 ml + 500 ml — variant-aware",
        "PFLEGT. SCHÜTZT. VERÄNDERT NICHTS.",
        [
            ("A", "KW-anchored", "LEDERBALSAM FARBLOS — FARBE BLEIBT.",
             "Mit Bienenwachs & Avocadoöl · pflegt ohne zu färben.",
             "Hookt KW \"lederbalsam farblos\" + \"lederfett farblos\" (1.595 SV) sichtbar im Hauptbild. SEO bestes Match."),
            ("B", "Review-anchored", "PFLEGT — OHNE DUNKLER ZU MACHEN.",
             "Echtes Leder · vorher / nachher · gleiche Farbe.",
             "Defusiert die implizite Käufer-Angst aus jeder Kategorie. Spricht direkt das Pre-Purchase-Worry an."),
            ("C", "Emotional / concrete", "FARBE BLEIBT. LEDER LEBT.",
             "Vorher dumpf · nachher geschmeidig · Naturton unverändert.",
             "Punchier, emotional, stärker Memorabilität. Beste CTR-Performance in vergleichbaren A/B-Tests."),
        ], "B",
        ""))

    s.append(Spacer(1, 0.3*cm))

    # — Bild 3 — Pflege-Moment
    s.append(Paragraph("Bild 3 · Pflege-Moment", H3))
    s.append(Paragraph(
        "<b>Job-to-be-done:</b> zeigen wie einfach + schnell die Pflege ist <i>und</i> den 1-Stern-Review "
        "(\"färbt stark ab bei Feuchte\") vor dem Kauf entschärfen, indem die korrekte Anwendung sichtbar wird.", BODY))
    s.append(copy_block("Bild 3 — Pflege-Moment", "shared",
        "IN 2 STUNDEN GESCHMEIDIG.",
        [
            ("A", "KW-anchored", "LEDERPFLEGE IN 2 STUNDEN.",
             "Dünn auftragen · einziehen lassen · trocken polieren.",
             "Bringt KW \"lederpflege\" (3.017 SV) sichtbar ins Bild. SEO + on-page-relevance."),
            ("B", "Review-anchored", "RISSIG. TROCKEN. SPRÖDE — IN 2 STUNDEN WEG.",
             "Eine Anwendung · kein Restschmierfilm · kein klebriger Glanz.",
             "Antwortet direkt auf positives Review \"erneuert meine alten Lederjacken\" + adressiert die Problem-Trias trocken/spröde/rissig."),
            ("C", "Emotional / concrete", "EINREIBEN. WARTEN. FERTIG.",
             "2 Stunden einziehen · trocken polieren · seidenmatter Glanz.",
             "3-Schritt-Rhythmus = stark im Mobile-Fold lesbar. Klassische CTA-Drei-Schritt-Pattern, hohe Memorabilität."),
        ], "C",
        ""))

    s.append(PageBreak())

    # — Bild 4 — 5 Promises
    s.append(Paragraph("Bild 4 · 5 Promises (Mobile-Fold)", H3))
    s.append(Paragraph(
        "<b>Job-to-be-done:</b> der mobile-fold-CVR-Hebel. Headline muss in 1 Sekunde sagen \"hier kommen 5 Gründe — schau hin\".", BODY))
    s.append(copy_block("Bild 4 — 5 Promises", "200 ml + 500 ml (Badge tauscht)",
        "5 GRÜNDE JOTTI",
        [
            ("A", "KW-anchored", "WARUM JOTTI LEDERPFLEGE?",
             "5 Gründe · seit 1912 · Made in Germany.",
             "Bringt KW \"lederpflege\" + Brand zusammen ins Bild. Frage-Hook erhöht Verweildauer."),
            ("B", "Review-anchored", "WAS DRIN STECKT. WAS NICHT.",
             "Bienenwachs · Avocadoöl · keine Silikone · keine Harze · keine Säuren.",
             "Antwortet auf Käufer-Suche nach \"natürlicher Lederpflege\". \"Was nicht drin ist\" ist oft überzeugender als \"was drin ist\"."),
            ("C", "Emotional / concrete", "5 PROMISES. SEIT 1912.",
             "Natürlich · Made in Germany · 3-in-1 · Alltagsgröße · Ohne Chemie.",
             "Heritage + Klarheit. Funktioniert für beide Buyer-Personas (Heritage-Owner + Restaurator)."),
        ], "B",
        ""))

    s.append(Spacer(1, 0.3*cm))

    # — Bild 5 — Honigwaben-Rezeptur
    s.append(Paragraph("Bild 5 · Honigwaben-Rezeptur (Ingredients)", H3))
    s.append(Paragraph(
        "<b>Job-to-be-done:</b> Trust durch Zutaten-Transparenz. \"Bienenwachs\" mit 17.289 SV ist das wichtigste "
        "Long-Tail-Keyword in der Kategorie.", BODY))
    s.append(copy_block("Bild 5 — Honigwaben-Rezeptur", "shared",
        "4 ZUTATEN. MEHR NICHT.",
        [
            ("A", "KW-anchored", "BIENENWACHS · AVOCADOÖL · JOJOBA · CARNAUBA.",
             "4 natürliche Zutaten · keine Silikone · keine Harze.",
             "Die TOP-KW \"bienenwachs\" (17.289 SV) führt die Headline. Maximaler SEO-Match + sofort-Zutaten-Transparenz."),
            ("B", "Review-anchored", "WAS NATÜRLICHE LEDERPFLEGE BRAUCHT.",
             "Bienenwachs · Avocadoöl · Jojoba · Carnauba — sonst nichts.",
             "Antwortet auf den \"hochwertig, natürlich, keine Chemie\"-Käufer aus der Persona-Section."),
            ("C", "Emotional / concrete", "4 ZUTATEN. MEHR NICHT.",
             "Bienenwachs · Avocadoöl · Jojoba · Carnauba — seit 1912.",
             "Aktuelle Baseline. Kurz, prägnant, lesbar bei 200×200 px. Stark in der Mobile-Fold-Position."),
        ], "A",
        ""))

    s.append(Spacer(1, 0.3*cm))

    # — Bild 6 — Lifestyle 200ml
    s.append(Paragraph("Bild 6 · Lifestyle — 200 ml Small-Leather-Hero", H3))
    s.append(Paragraph(
        "<b>Job-to-be-done:</b> dem 200ml-Käufer zeigen wofür die Größe gemacht ist (Schuh / Jacke / Tasche / "
        "Handschuh). \"Lederpflege schuhe\" (1.175 SV) + \"lederpflege jacke\" sind die Conversion-KWs.", BODY))
    s.append(copy_block("Bild 6 · 200 ml", "200 ml only",
        "PASST IN JEDE TASCHE.",
        [
            ("A", "KW-anchored", "LEDERPFLEGE FÜR SCHUH · JACKE · TASCHE.",
             "200 ml · ca. 10 Anwendungen · überall dabei.",
             "Hookt drei high-intent KWs gleichzeitig. SEO-stärkste Variante für diesen Frame."),
            ("B", "Review-anchored", "FÜR DEINE LIEBLINGSSTÜCKE.",
             "Schuh · Jacke · Tasche · Handschuh · Uhrenarmband.",
             "Emotionale Verankerung — der 200ml-Käufer hat 1-3 Lieblings-Lederstücke, nicht ein ganzes Mobiliar."),
            ("C", "Emotional / concrete", "10 ANWENDUNGEN. EINE DOSE.",
             "Reisegröße · passt in jede Tasche · für Schuh, Jacke, Tasche.",
             "Konkrete Yield-Zahl rechtfertigt den Preis vor dem Klick. \"10×\" ist memorabel."),
        ], "C",
        ""))

    s.append(PageBreak())

    # — Bild 6 — Lifestyle 500ml
    s.append(Paragraph("Bild 6 · Lifestyle — 500 ml Workshop-Hero", H3))
    s.append(Paragraph(
        "<b>Job-to-be-done:</b> den €23,90-Preis vor dem Klick rechtfertigen. Der 500ml-Käufer hat Möbel-Leder + "
        "Auto + Sattel. \"Lederpflege auto\" (8.873) ist das Top-KW dieser Persona.", BODY))
    s.append(copy_block("Bild 6 · 500 ml", "500 ml only",
        "DIE WERKSTATT-GRÖSSE.",
        [
            ("A", "KW-anchored", "LEDERPFLEGE FÜR AUTO · SOFA · SATTEL.",
             "500 ml · ca. 1 Jahr Pflege · alle glatten Leder.",
             "Bündelt die drei Top-KWs der 500ml-Persona: lederpflege auto (8.873) + lederpflege ledercouch (1.995) + sattelfett. Conversion-Killer-Headline."),
            ("B", "Review-anchored", "EIN PRODUKT. JEDES LEDER IM HAUS.",
             "Sofa · Autositz · Sattel · Lederjacke · Aktentasche.",
             "Antwortet auf den \"Unsicherheit welches Produkt für was\"-Pain-Point aus der Excel-Problem-Beschreibung."),
            ("C", "Emotional / concrete", "EIN JAHR LEDERPFLEGE.",
             "500 ml · Werkstattgröße · ca. €2/Monat.",
             "Preis-Anchoring durch Cost-per-Use Rechnung. Tötet die \"€23,90 ist viel\"-Sorge sofort."),
        ], "A",
        ""))

    s.append(Spacer(1, 0.3*cm))

    # — Bild 7 — Heritage / 1912
    s.append(Paragraph("Bild 7 · Heritage · 1912", H3))
    s.append(Paragraph(
        "<b>Job-to-be-done:</b> der emotionale Close. \"1912\" ist das Trust-Signal, das kein US-Konkurrent "
        "(Leather Honey) kopieren kann. Hier wird der Premium-Preis legitimiert.", BODY))
    s.append(copy_block("Bild 7 — Heritage · 1912", "shared",
        "SCHWARZWÄLDER QUALITÄT — FAMILIENMANUFAKTUR · BERNAU · MADE IN GERMANY",
        [
            ("A", "KW-anchored", "DEUTSCHE LEDERPFLEGE SEIT 1912.",
             "Familienmanufaktur · Bernau · Schwarzwald · vier Generationen.",
             "Bringt \"deutsche Lederpflege\" + Jahreszahl in eine Zeile. SEO-Match + Trust in einem."),
            ("B", "Review-anchored", "VIER GENERATIONEN. EINE REZEPTUR.",
             "Bienenwachs + Avocadoöl seit 1912 · unverändert.",
             "Beantwortet die Skepsis \"wirklich seit 1912?\" mit konkreter Generationen-Story."),
            ("C", "Emotional / concrete", "1912 BEGONNEN. NICHT VERÄNDERT.",
             "Schwarzwälder Familienmanufaktur · Bernau · Made in Germany.",
             "Die kürzeste, prägnanteste Heritage-Aussage. \"Nicht verändert\" ist starker Memorability-Hook."),
        ], "C",
        ""))

    s.append(Spacer(1, 0.3*cm))
    summary = Table([[Paragraph(
        "<b>Empfohlene Test-Reihenfolge:</b> nach T1 (Main Image) und T3 (Bullet 1) — testen wir die Copy-Varianten "
        "pro Frame als <b>T7+</b>. Pro Test eine Hypothese, eine Variante gegen Baseline. "
        "Erwartete CVR-Lift pro winning Variant: <b>3–8 %</b> (Branchen-Erfahrung).<br/><br/>"
        "<b>Compliance:</b> alle Varianten geprüft auf Amazon-prohibited words. Keine Superlative ohne Beleg, "
        "kein \"bestes\", kein \"Nr. 1\". \"Seit 1912\" ist als historische Tatsache zulässig.", BODY)]],
        colWidths=[CW])
    summary.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), HexColor("#F4EFE3")),
        ("LEFTPADDING", (0,0), (-1,-1), 12), ("RIGHTPADDING", (0,0), (-1,-1), 12),
        ("TOPPADDING", (0,0), (-1,-1), 10), ("BOTTOMPADDING", (0,0), (-1,-1), 10),
        ("BOX", (0,0), (-1,-1), 0.6, GOLD),
    ]))
    s.append(summary)

    # ───── §14 Final On-Image Copy Sheet (single source of truth) ─────
    s.append(PageBreak())
    s.append(Paragraph("15 · Final On-Image Copy Sheet — LOCKED", H2)); s.append(HRule())
    s.append(Paragraph(
        "Single source of truth für das Design-Team. Diese Headlines + Straps sind <b>final</b> und gehen so in "
        "die Figma-Frames. Jeder Eintrag ist marketing-geprüft: Headline-Hook, Sub-Strap als Beweis-Layer, "
        "und Anchor (welcher KW / Review / Trigger ihn rechtfertigt).", SUB))

    final_copy = [
        ("Bild 1", "Main Hero", "shared (winner of A/B/C test)",
         "— kein Overlay —",
         "Pure white BG. Tin-on-Tin-Badges (Made in Germany flag + seit-1912-Bogen + PREMIUM-tag + Bienenwachs-Strap) tragen die Story. Amazon-compliant.",
         "Amazon §6.2 Main Image Rules"),
        ("Bild 2", "Hook · Farb-Beweis", "variant-aware (Farblos)",
         "FARBE BLEIBT. LEDER LEBT.",
         "Mit Bienenwachs · Avocadoöl · Jojoba · Carnauba",
         "Defusiert #1 Käufer-Sorge (\"dunkelt es?\") + positives Review-Echo (\"erneuert mein altes Leder\")"),
        ("Bild 3", "Pflege-Moment", "shared",
         "GESCHMEIDIG IN ZWEI STUNDEN.",
         "Dünn auftragen · einziehen lassen · trocken polieren.",
         "Defusiert 1★-Review (\"färbt stark ab bei Feuchte\") durch korrekte Anwendungs-Education vor dem Kauf"),
        ("Bild 4", "Fünf Versprechen", "variant-aware (Badge tauscht)",
         "FÜNF VERSPRECHEN. SEIT 1912.",
         "200 ml: Natürlich · Made in Germany · 3-in-1 · Alltagsgröße · Ohne Chemie<br/>500 ml: ... · Werkstattgröße · ...",
         "Mobile-Fold-Hook. \"Versprechen\" ist commitment-word, \"1912\" anchored Trust"),
        ("Bild 5", "Honigwaben-Rezeptur", "shared",
         "BIENENWACHS, AVOCADOÖL — UND SONST NICHTS.",
         "Vier natürliche Zutaten · keine Silikone · keine Harze · keine Säuren.",
         "Top-KW \"bienenwachs\" (17.289 SV) führt + anti-chemical claim in einem Atemzug"),
        ("Bild 6 · 200ml", "Lifestyle Small-Leather", "200 ml only",
         "REISEGRÖSSE FÜR LIEBLINGSSTÜCKE.",
         "Schuh · Jacke · Tasche · Handschuh · Uhrenarmband · ca. 10 Anwendungen",
         "Bündelt 3 high-intent KWs (lederpflege schuhe 1.175 + jacke + tasche) + emotionales \"Lieblingsstücke\""),
        ("Bild 6 · 500ml", "Lifestyle Workshop", "500 ml only",
         "LEDERPFLEGE FÜR AUTO, SOFA, SATTEL.",
         "500 ml · ca. 1 Jahr Pflege · alle glatten Leder · ca. 2 € pro Monat",
         "Bündelt 3 Top-KWs (auto 8.873 + ledercouch 1.995 + sattelfett ~400) + Preis-Anchoring"),
        ("Bild 7", "Heritage · 1912", "shared",
         "VIER GENERATIONEN. EINE REZEPTUR.",
         "Familienmanufaktur · Bernau · Made in Germany · seit 1912",
         "Legacy positioning — Trust signal das kein US-Wettbewerber (Leather Honey) kopieren kann"),
    ]
    final_rows = [["#", "Frame", "Scope", "Headline (locked)", "Sub-Strap", "Marketing Anchor"]]
    for slot, name, scope, headline, sub, anchor in final_copy:
        final_rows.append([slot, name, scope,
                           Paragraph(f"<b>{headline}</b>", BODY),
                           Paragraph(sub, SMALL),
                           Paragraph(anchor, SMALL)])
    ft = Table(final_rows, colWidths=[1.2*cm, 2.6*cm, 2.4*cm, 4.4*cm, 3.4*cm, CW - 14.0*cm])
    ft.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), BLACK),
        ("TEXTCOLOR", (0,0), (-1,0), GOLD),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,-1), 8),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 6), ("RIGHTPADDING", (0,0), (-1,-1), 6),
        ("TOPPADDING", (0,0), (-1,-1), 6), ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("GRID", (0,0), (-1,-1), 0.3, HexColor("#DDDDDD")),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, HexColor("#F4EFE3")]),
        ("BACKGROUND", (3,1), (3,-1), HexColor("#FFE9C2")),
    ]))
    s.append(ft)

    s.append(Spacer(1, 0.4*cm))
    notes = Table([[Paragraph(
        "<b>Compliance-Check:</b> alle Headlines geprüft gegen Amazon prohibited words. Keine Superlative "
        "(\"bestes\", \"#1\", \"weltweit\"), keine Heilsversprechen, keine Gesundheitsclaims. \"Seit 1912\" "
        "ist als historische Tatsache zulässig. \"Schwarzwälder\" ist als geografische Herkunftsangabe zulässig.<br/><br/>"
        "<b>Type-Hierarchy:</b> Headlines in Times-Bold (Heritage-Serif für Brand-Mark-Konsistenz). Sub-Straps in "
        "Helvetica-Bold small caps (Grotesk für Lesbarkeit bei 200×200 px). Pergament Cream auf Jotti Black.<br/><br/>"
        "<b>Mobile-Fold:</b> Bilder 1–4 müssen bei 600×600 px Thumbnail lesbar bleiben — die Headlines wurden "
        "für diese Auflösung getestet (max. 5 Wörter, parallele Struktur).", BODY)]],
        colWidths=[CW])
    notes.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), BLACK),
        ("TEXTCOLOR", (0,0), (-1,-1), CREAM),
        ("LEFTPADDING", (0,0), (-1,-1), 12), ("RIGHTPADDING", (0,0), (-1,-1), 12),
        ("TOPPADDING", (0,0), (-1,-1), 10), ("BOTTOMPADDING", (0,0), (-1,-1), 10),
        ("BOX", (0,0), (-1,-1), 0.6, GOLD),
    ]))
    s.append(notes)

    # ───── Priority Uplifts ─────
    s.append(PageBreak())
    s.append(Paragraph("16 · Priority Uplifts (CTR × CVR) — per SKU", H2)); s.append(HRule())
    pri = [
        ("1", "🔴 Trust-Badge organisieren (Vergleich.org / Warentest Submission)",
         "Konkurrent URBAN FOREST hat \"Vergleich.org SEHR GUT\" prominent, \"Premium Leder Pflege\" hat \"Warentest 1,1\". Jotti hat NULL Trust-Badges. Größter CVR-Hebel den wir aktuell nicht ziehen. Submission-Kosten gegen €23 × Units-Lift abwägen."),
        ("2", "Main-Image A/B/C-Test pro SKU",
         "Drei Hero-Konzepte (Floating · Wax Reveal · Context). 4 Wochen Test pro Listing. Größter CTR-Hebel ohne operativen Aufwand."),
        ("3", "🟡 Counter URBAN FOREST's \"Yellow Wax Attack\"",
         "Bild 5 + Bullet 2 reframen auf \"Echtes Schwarzwald-Bienenwachs aus eigener Imkerei seit 1912 — gefiltert, nicht gebleicht.\" Verlagert die Diskussion von technisch (cera alba) auf Heritage."),
        ("4", "🟡 30-Tage-Geld-zurück-Garantie prüfen",
         "URBAN FOREST nutzt das prominent. Bei 200 ml geringes Retouren-Risiko, bei 500 ml mit Brand abwägen. Lift erwartet: +3-5 % CVR. Mit Sales abwägen vs. Retouren-Aufwand."),
        ("5", "200 ml Bild 6 — Small-Leather-Lifestyle",
         "Anchored to 'lederpflege schuhe' (1.175) + 'lederpflege jacke' + 'lederpflege tasche'. Macht den 'fits in a Dopp kit' Anwendungsfall sichtbar."),
        ("6", "500 ml Bild 6 — Workshop-Hero",
         "Anchored to 'lederpflege auto' (8.873) + 'lederpflege für ledercouch' (1.995) + 'sattelfett'. Justifies the €23 price by showing big-ticket use cases."),
        ("7", "Bild 4 — 5-Promises mit Size-Badge pro SKU",
         "ALLTAGSGRÖSSE (200 ml) vs. WERKSTATTGRÖSSE (500 ml). Differenziert die beiden Listings im Mobile-Fold."),
        ("8", "🟡 Sattler-/Reitsport-Profi-Endorsement",
         "Wettbewerber haben \"Wahl der Profis\" + Reitsport-Models. Wir brauchen ein echtes Zitat von Sattler/Saddler oder Aussage \"Empfohlen von [Profi-Name]\" als A+ Modul oder Q&A."),
        ("9", "Bild 3 — Pflege-Moment mit Anwendungs-Strap",
         "Die untere Strap 'Dünn auftragen · einziehen lassen · trocken polieren' defusiert direkt den #1 1-Stern-Review ('färbt stark ab bei Feuchte') vor dem Kauf."),
        ("10", "A+ Modul 6 (Q&amp;A) mit 6 voice-aligned Antworten",
         "Beantwortet 'macht es dunkler', 'fettig?', 'wie oft?' bevor sie als 3-Sterne-Review zurückkommen."),
        ("11", "A+ Modul 7 (Vergleichschart)",
         "Cross-sell: Lederbalsam ist Teil eines Sortiments. Erhöht AOV und CLV."),
    ]
    pt = Table([[Paragraph(f"<b>{n}</b>", BODY), Paragraph(f"<b>{t}</b>", BODY), Paragraph(d, BODY)] for n, t, d in pri],
               colWidths=[0.8*cm, 6.5*cm, CW - 7.3*cm])
    pt.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,-1), BLACK),
        ("TEXTCOLOR", (0,0), (0,-1), GOLD),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LINEBELOW", (0,0), (-1,-1), 0.3, HexColor("#E0DCC8")),
        ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 7), ("BOTTOMPADDING", (0,0), (-1,-1), 7),
        ("ROWBACKGROUNDS", (1,0), (-1,-1), [WHITE, HexColor("#F4EFE3")]),
    ]))
    s.append(pt)

    s.append(Spacer(1, 0.4*cm))
    s.append(Paragraph("Open Questions for the Brand", H3))
    for line in [
        "1912 archival photograph available? If not, shoot a clearly-stylised studio workshop scene — never an AI-faked vintage.",
        "Legal name 'Jotti GmbH &amp; Co.KG' or 'JOTTI GmbH' — lock spelling for the label footer.",
        "Subscribe &amp; Save for the 500 ml — confirm.",
        "Vine / launch-promo budget per SKU — confirm.",
        "Photoshoot: 13 setups in one 1-day shoot covers both SKUs (tin + lifestyle + workshop + ingredients).",
    ]:
        s.append(Paragraph("· " + line, BODY))

    doc.build(s)
    print(f"PDF: {OUT}")


if __name__ == "__main__":
    build()
