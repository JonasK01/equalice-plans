#!/usr/bin/env python3
"""JOTTI Lederbalsam (200/500 ml × Farblos / Braun / Schwarz · Amazon.de)
Brand · Moodboard · 3 Main Image Options · 7 Listing Images · A+ Premium · Master Copy.

Rebuilt 2026-05-16 — same layout system as the SeQR briefs, with the Jotti
heritage palette (dark + honeycomb + gold + cream) instead of teal / cream.
"""

import math
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, Color
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (
    Paragraph, Spacer, PageBreak, Table, TableStyle,
    KeepTogether, Frame, BaseDocTemplate, PageTemplate, NextPageTemplate,
)
from reportlab.platypus.flowables import Flowable

OUT = "/Users/jonask/Desktop/Jotti_Lederbalsam_Brief.pdf"

# ─── Jotti palette (matches existing 500 ml labels) ─────────────────
BLACK    = HexColor("#0E0E0E")
CHARCOAL = HexColor("#1B1814")
WALNUT   = HexColor("#3A241A")
AMBER    = HexColor("#C58A3A")     # honeycomb amber
GOLD     = HexColor("#D9B36B")     # accent gold — arches, hairlines, "1912"
CREAM    = HexColor("#EFE6D2")     # pergament
CREAM_DK = HexColor("#E5DEC9")
BEESWAX  = HexColor("#E9C46A")
TAN      = HexColor("#C9985A")     # Farblos chip
BROWN    = HexColor("#6A3A1E")     # Braun chip
ONYX     = HexColor("#0A0A0A")     # Schwarz chip
LEATHER_BR = HexColor("#7A4A2A")
LEATHER_BK = HexColor("#1A1612")
LEATHER_NT = HexColor("#A87A4A")
INK      = HexColor("#111111")
GREY     = HexColor("#7A6A55")
LIGHT    = HexColor("#F5F1E6")
WHITE    = HexColor("#FFFFFF")
GREEN_OK = HexColor("#3FA770")
RED_X    = HexColor("#D24545")
WARN_BG  = HexColor("#FFF4E5")
WARN_BD  = HexColor("#B5390A")

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


# ─── Flowables ──────────────────────────────────────────────────────

class HRule(Flowable):
    def __init__(self, width=None, color=GOLD, thickness=1.2):
        self.width = width or CW; self.color = color; self.thickness = thickness
        Flowable.__init__(self)
    def wrap(self, *a): return (self.width, self.thickness + 6)
    def draw(self):
        self.canv.setStrokeColor(self.color); self.canv.setLineWidth(self.thickness)
        self.canv.line(0, 3, self.width, 3)


class ColorChip(Flowable):
    def __init__(self, color, hex_label, name, w=4.0*cm, h=2.0*cm):
        self.color = color; self.hex_label = hex_label; self.name = name
        self.w = w; self.h = h
        Flowable.__init__(self)
    def wrap(self, *a): return (self.w, self.h + 0.9*cm)
    def draw(self):
        c = self.canv
        c.setFillColor(self.color); c.setStrokeColor(HexColor("#CCCCCC"))
        c.setLineWidth(0.3)
        c.rect(0, 0.9*cm, self.w, self.h, fill=1, stroke=1)
        c.setFillColor(BLACK); c.setFont("Helvetica-Bold", 9)
        c.drawString(0, 0.45*cm, self.name)
        c.setFillColor(GREY); c.setFont("Courier", 8)
        c.drawString(0, 0.15*cm, self.hex_label)


# ─── Drawing helpers ────────────────────────────────────────────────

def _honeycomb(c, cx, cy, radius=1.6*cm, opacity=0.18, color=AMBER):
    """Subtle honeycomb hex pattern centered at (cx, cy)."""
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


def _draw_tin_topdown(c, cx, cy, w=2.6*cm, variant="farblos", show_label=True):
    """Top-down view of the Jotti Lederbalsam tin. Font sizes scale by cm-width."""
    r = w / 2
    w_cm = w / cm   # cm-units for font sizing
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


def _draw_tin_3q(c, cx, cy, w=2.4*cm, variant="farblos"):
    """3/4 angle stylised tin."""
    h = w * 0.4
    c.setFillColor(CHARCOAL); c.setStrokeColor(GOLD); c.setLineWidth(0.4)
    c.roundRect(cx - w/2, cy - h*1.1, w, h*1.2, h*0.1, fill=1, stroke=1)
    c.setFillColor(BLACK); c.setStrokeColor(GOLD)
    c.ellipse(cx - w/2, cy - h*0.2, cx + w/2, cy + h*0.3, fill=1, stroke=1)
    _honeycomb(c, cx, cy + h*0.05, radius=w*0.4, opacity=0.10, color=AMBER)
    c.setFillColor(GOLD); c.setFont("Times-BoldItalic", 5.5)
    c.drawCentredString(cx, cy + h*0.18, "Jotti")
    chip_color = {"farblos": TAN, "braun": BROWN, "schwarz": ONYX}[variant]
    c.setFillColor(chip_color); c.setStrokeColor(GOLD); c.setLineWidth(0.4)
    c.ellipse(cx - w*0.13, cy - h*0.05, cx + w*0.13, cy + h*0.13, fill=1, stroke=1)
    c.setFillColor(CREAM); c.setFont("Helvetica-Bold", 4.5)
    c.drawCentredString(cx, cy - h*0.65, "500 ml")


def _draw_leather_swatch(c, x, y, w, h, color, split="right"):
    """Leather swatch with before/after split. split: 'left' | 'right' | 'full'."""
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


def _draw_workshop(c, cx, cy, w=3.0*cm, h=2.0*cm):
    """Workshop bench with brass scale + three tins + lantern glow."""
    # warm glow
    for i in range(7):
        c.setFillColor(Color(AMBER.red, AMBER.green, AMBER.blue, alpha=0.10 - i*0.012))
        c.circle(cx - w*0.35, cy + h*0.2, h*0.4 + i*0.10*cm, fill=1, stroke=0)
    # bench
    c.setFillColor(WALNUT); c.setStrokeColor(WALNUT); c.setLineWidth(0.3)
    c.rect(cx - w/2, cy - h/2, w, h*0.45, fill=1, stroke=1)
    # brass scale
    c.setFillColor(HexColor("#B58E4A")); c.setStrokeColor(GOLD); c.setLineWidth(0.3)
    c.rect(cx - 0.04*cm, cy - h*0.3, 0.08*cm, h*0.6, fill=1, stroke=0)
    c.rect(cx - w*0.18, cy + h*0.30, w*0.36, 0.05*cm, fill=1, stroke=0)
    c.circle(cx - w*0.18, cy + h*0.20, h*0.10, fill=1, stroke=1)
    c.circle(cx + w*0.18, cy + h*0.20, h*0.10, fill=1, stroke=1)
    # three tins
    for i, var in enumerate(["farblos", "braun", "schwarz"]):
        _draw_tin_topdown(c, cx - w*0.05 + i*w*0.18, cy - h*0.05, w=h*0.32, variant=var, show_label=False)


def _draw_fir(c, cx, cy, h=1.0*cm, color=HexColor("#0A1612")):
    """Single dark Schwarzwald fir silhouette (point-up triangle stack)."""
    c.setFillColor(color)
    p = c.beginPath()
    p.moveTo(cx - h*0.4, cy - h*0.5)
    p.lineTo(cx, cy + h*0.5)
    p.lineTo(cx + h*0.4, cy - h*0.5)
    p.close()
    c.drawPath(p, fill=1, stroke=0)


def _draw_check(c, cx, cy, size=0.5*cm, color=GREEN_OK):
    c.setStrokeColor(color); c.setLineWidth(1.6)
    c.line(cx - size*0.3, cy, cx - size*0.05, cy - size*0.25)
    c.line(cx - size*0.05, cy - size*0.25, cx + size*0.3, cy + size*0.3)


def _draw_x(c, cx, cy, size=0.5*cm, color=RED_X):
    c.setStrokeColor(color); c.setLineWidth(1.6)
    c.line(cx - size*0.3, cy - size*0.3, cx + size*0.3, cy + size*0.3)
    c.line(cx - size*0.3, cy + size*0.3, cx + size*0.3, cy - size*0.3)


# ─── Mockup classes ─────────────────────────────────────────────────

class MainOption(Flowable):
    def __init__(self, letter, name, draw_fn, side_w=8.5*cm):
        self.letter = letter; self.name = name; self.draw_fn = draw_fn
        self.size = 6.5*cm; self.side_w = side_w; self.gap = 0.4*cm
        Flowable.__init__(self)
    def wrap(self, *a): return (self.size + self.gap + self.side_w, self.size + 0.4*cm)
    def draw(self):
        c = self.canv; s = self.size
        c.setFillColor(WHITE); c.setStrokeColor(HexColor("#CCCCCC")); c.setLineWidth(0.4)
        c.rect(0, 0, s, s, fill=1, stroke=1)
        c.setFillColor(BLACK); c.rect(0, s - 0.7*cm, 1.7*cm, 0.7*cm, fill=1, stroke=0)
        c.setFillColor(GOLD); c.setFont("Helvetica-Bold", 11)
        c.drawCentredString(0.85*cm, s - 0.5*cm, f"OPT {self.letter}")
        self.draw_fn(c, s/2, s/2 - 0.3*cm)
        c.setFillColor(GREY); c.setFont("Helvetica", 7)
        c.drawCentredString(s/2, 0.15*cm, "2000 × 2000 px · weisser BG (Amazon)")
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
    def wrap(self, *a): return (self.size + self.gap + self.side_w, self.size + 0.4*cm)
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
    def wrap(self, *a): return (self.bw + self.gap + self.side_w, self.bh + 0.5*cm)
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
        self.draw_fn(c, w/2, h/2 + 0.2*cm)
        c.setFillColor(GOLD); c.rect(0, 0, w, 0.5*cm, fill=1, stroke=0)
        c.setFillColor(BLACK); c.setFont("Helvetica-Bold", 7.5)
        c.drawString(0.2*cm, 0.18*cm, self.title.upper())
        c.setFillColor(BLACK); c.setFont("Helvetica", 6.5)
        c.drawRightString(w - 0.2*cm, 0.18*cm, self.sub)


# ─── Concept drawings — Main Image options ──────────────────────────

def cpt_main_a(c, cx, cy):
    """Floating Heritage — tin with long warm shadow."""
    c.setFillColor(Color(AMBER.red, AMBER.green, AMBER.blue, alpha=0.20))
    c.ellipse(cx - 1.3*cm, cy - 1.7*cm, cx + 2.4*cm, cy - 1.0*cm, fill=1, stroke=0)
    _draw_tin_3q(c, cx - 0.2*cm, cy + 0.5*cm, w=3.2*cm, variant="farblos")


def cpt_main_b(c, cx, cy):
    """Open Wax Reveal — top-down with lid offset, amber wax visible inside."""
    # tin body (open)
    c.setFillColor(BLACK); c.setStrokeColor(GOLD); c.setLineWidth(0.5)
    c.circle(cx - 0.5*cm, cy, 1.5*cm, fill=1, stroke=1)
    # wax inside
    c.setFillColor(BEESWAX)
    c.circle(cx - 0.5*cm, cy, 1.25*cm, fill=1, stroke=0)
    _honeycomb(c, cx - 0.5*cm, cy, radius=1.1*cm, opacity=0.22, color=AMBER)
    # offset lid
    c.setFillColor(BLACK); c.setStrokeColor(GOLD); c.setLineWidth(0.5)
    c.circle(cx + 1.6*cm, cy - 0.4*cm, 1.0*cm, fill=1, stroke=1)
    _honeycomb(c, cx + 1.6*cm, cy - 0.4*cm, radius=0.85*cm, opacity=0.12, color=AMBER)
    c.setFillColor(GOLD); c.setFont("Times-BoldItalic", 7)
    c.drawCentredString(cx + 1.6*cm, cy - 0.2*cm, "Jotti")
    c.setFillColor(TAN); c.setStrokeColor(GOLD); c.setLineWidth(0.4)
    c.circle(cx + 1.6*cm, cy - 0.55*cm, 0.25*cm, fill=1, stroke=1)


def cpt_main_c(c, cx, cy):
    """Familien-Hero — three tins staggered."""
    for i, var in enumerate(["schwarz", "braun", "farblos"]):
        _draw_tin_3q(c, cx, cy - 0.9*cm + i*0.55*cm, w=2.5*cm - i*0.15*cm, variant=var)


# ─── Listing image concepts ─────────────────────────────────────────

def cpt_img2_variant(c, cx, cy):
    """Variant proof — Farblos by default (the safest representative)."""
    c.setFillColor(CREAM); c.setFont("Times-Bold", 10)
    c.drawCentredString(cx, cy + 2.4*cm, "PFLEGT. SCHÜTZT.")
    c.drawCentredString(cx, cy + 2.0*cm, "VERÄNDERT NICHTS.")
    _draw_leather_swatch(c, cx - 2.0*cm, cy - 0.4*cm, 4.0*cm, 1.5*cm, LEATHER_NT, split="right")
    c.setFillColor(GOLD); c.setFont("Helvetica-Bold", 5.5)
    c.drawCentredString(cx - 1.0*cm, cy - 0.9*cm, "VORHER")
    c.drawCentredString(cx + 1.0*cm, cy - 0.9*cm, "NACHHER")
    _draw_tin_topdown(c, cx + 1.8*cm, cy - 1.8*cm, w=1.3*cm, variant="farblos", show_label=False)
    c.setFillColor(CREAM); c.setFont("Helvetica-Bold", 5.5)
    c.drawCentredString(cx, cy - 2.5*cm, "MIT BIENENWACHS & AVOCADOÖL")


def cpt_img3_moment(c, cx, cy):
    """Pflege-Moment — cinematic hand + sofa arm + open tin."""
    c.setFillColor(CREAM); c.setFont("Times-Bold", 12)
    c.drawCentredString(cx, cy + 2.4*cm, "IN 2 STUNDEN")
    c.drawCentredString(cx, cy + 1.9*cm, "GESCHMEIDIG.")
    # sofa arm
    c.setFillColor(LEATHER_BR); c.setStrokeColor(WALNUT); c.setLineWidth(0.3)
    c.roundRect(cx - 2.4*cm, cy - 1.4*cm, 4.8*cm, 1.5*cm, 0.3*cm, fill=1, stroke=1)
    # warm window glow
    c.setFillColor(Color(AMBER.red, AMBER.green, AMBER.blue, alpha=0.20))
    c.circle(cx + 0.8*cm, cy - 0.6*cm, 1.3*cm, fill=1, stroke=0)
    # open tin in foreground showing wax
    c.setFillColor(BLACK); c.setStrokeColor(GOLD); c.setLineWidth(0.4)
    c.circle(cx - 1.8*cm, cy - 2.0*cm, 0.6*cm, fill=1, stroke=1)
    c.setFillColor(BEESWAX); c.circle(cx - 1.8*cm, cy - 2.0*cm, 0.5*cm, fill=1, stroke=0)
    # hex tag with "1 Anwendung"
    c.setFillColor(GOLD); _hex(c, cx + 1.6*cm, cy + 0.5*cm, 0.40*cm)
    c.setFillColor(BLACK); c.setFont("Helvetica-Bold", 5)
    c.drawCentredString(cx + 1.6*cm, cy + 0.55*cm, "1 ANW.")
    c.drawCentredString(cx + 1.6*cm, cy + 0.42*cm, "2 STD.")


# ─── Key Benefits frame (slot #4) ───────────────────────────────────

def _draw_benefit_icon(c, cx, cy, kind, size=0.42*cm):
    if kind == "natural":
        # honeycomb drop
        c.setFillColor(BEESWAX)
        _hex(c, cx, cy, size*0.45)
        c.setStrokeColor(GOLD); c.setLineWidth(0.4)
        pts = [(cx + size*0.45*math.cos(math.radians(60*i+30)), cy + size*0.45*math.sin(math.radians(60*i+30))) for i in range(6)]
        p = c.beginPath(); p.moveTo(*pts[0])
        for pt in pts[1:]: p.lineTo(*pt)
        p.close(); c.drawPath(p, fill=0, stroke=1)
    elif kind == "germany":
        # DE flag inside hex
        c.setFillColor(BLACK); c.rect(cx - size*0.40, cy + size*0.10, size*0.80, size*0.18, fill=1, stroke=0)
        c.setFillColor(RED_X);  c.rect(cx - size*0.40, cy - size*0.08, size*0.80, size*0.18, fill=1, stroke=0)
        c.setFillColor(YELLOW := HexColor("#F4C040")); c.rect(cx - size*0.40, cy - size*0.26, size*0.80, size*0.18, fill=1, stroke=0)
        c.setStrokeColor(GOLD); c.setLineWidth(0.5)
        c.rect(cx - size*0.40, cy - size*0.26, size*0.80, size*0.54, fill=0, stroke=1)
        c.setFillColor(GOLD); c.setFont("Helvetica-Bold", size*10)
        c.drawCentredString(cx, cy - size*0.55, "1912")
    elif kind == "three_in_one":
        # shield with 3 dots
        c.setFillColor(GOLD); c.setStrokeColor(GOLD)
        p = c.beginPath()
        p.moveTo(cx - size*0.4, cy + size*0.3)
        p.lineTo(cx + size*0.4, cy + size*0.3)
        p.lineTo(cx + size*0.4, cy - size*0.05)
        p.curveTo(cx + size*0.4, cy - size*0.4, cx + size*0.1, cy - size*0.5, cx, cy - size*0.5)
        p.curveTo(cx - size*0.1, cy - size*0.5, cx - size*0.4, cy - size*0.4, cx - size*0.4, cy - size*0.05)
        p.close()
        c.drawPath(p, fill=1, stroke=0)
        c.setFillColor(BLACK)
        for dx in [-size*0.18, 0, size*0.18]:
            c.circle(cx + dx, cy, size*0.05, fill=1, stroke=0)
    elif kind == "universal":
        # 3 leather-good icons (saddle, sofa, shoe)
        c.setFillColor(GOLD)
        c.ellipse(cx - size*0.45, cy + size*0.05, cx - size*0.10, cy + size*0.30, fill=1, stroke=0)  # saddle
        c.rect(cx - size*0.10, cy - size*0.10, size*0.35, size*0.30, fill=1, stroke=0)  # sofa
        c.roundRect(cx + size*0.20, cy - size*0.35, size*0.30, size*0.18, size*0.04, fill=1, stroke=0)  # shoe
    elif kind == "no_chemicals":
        # "Ø chemistry" — beaker with X
        c.setFillColor(GOLD); c.setStrokeColor(GOLD); c.setLineWidth(0.8)
        c.setFillColor(None) if False else None
        c.line(cx - size*0.25, cy + size*0.35, cx + size*0.25, cy + size*0.35)  # top
        c.line(cx - size*0.25, cy + size*0.35, cx - size*0.30, cy - size*0.30)
        c.line(cx + size*0.25, cy + size*0.35, cx + size*0.30, cy - size*0.30)
        c.line(cx - size*0.30, cy - size*0.30, cx + size*0.30, cy - size*0.30)
        # liquid
        c.setFillColor(BEESWAX); c.rect(cx - size*0.27, cy - size*0.30, size*0.54, size*0.30, fill=1, stroke=0)
        # red X
        c.setStrokeColor(RED_X); c.setLineWidth(1.5)
        c.line(cx - size*0.45, cy - size*0.45, cx + size*0.45, cy + size*0.45)


def cpt_img4_benefits(c, cx, cy):
    """5 Promises around the tin — promoted to slot #4."""
    c.setFillColor(CREAM); c.setFont("Times-Bold", 11)
    c.drawCentredString(cx, cy + 2.4*cm, "5 GRÜNDE JOTTI")
    c.setFillColor(GREY); c.setFont("Helvetica", 7)
    c.drawCentredString(cx, cy + 2.05*cm, "Was Sie mit jeder Dose bekommen")
    _draw_tin_topdown(c, cx, cy - 0.2*cm, w=1.4*cm, variant="farblos", show_label=False)
    badges = [
        ( -2.2*cm,  1.3*cm, "natural",      "NATÜRLICH",        "Bienenwachs & Avocadoöl"),
        (  2.2*cm,  1.3*cm, "germany",      "MADE IN\nGERMANY", "Familienmanufaktur seit 1912"),
        ( -2.4*cm, -0.4*cm, "three_in_one", "3 IN 1",           "Reinigt · Pflegt · Schützt"),
        (  2.4*cm, -0.4*cm, "universal",    "UNIVERSELL",       "Alle glatten Lederarten"),
        (  0,      -1.9*cm, "no_chemicals", "OHNE CHEMIE",      "Keine Silikone · Harze · Säuren"),
    ]
    for dx, dy, kind, label, sub in badges:
        c.setFillColor(CHARCOAL); c.setStrokeColor(GOLD); c.setLineWidth(0.6)
        c.roundRect(cx + dx - 0.95*cm, cy + dy - 0.45*cm, 1.9*cm, 0.9*cm, 0.10*cm, fill=1, stroke=1)
        _draw_benefit_icon(c, cx + dx - 0.65*cm, cy + dy, kind)
        c.setFillColor(GOLD); c.setFont("Helvetica-Bold", 5.5)
        for i, ln in enumerate(label.split("\n")):
            c.drawString(cx + dx - 0.25*cm, cy + dy + 0.18*cm - i*0.18*cm, ln)
        c.setFillColor(CREAM); c.setFont("Helvetica", 4.5)
        c.drawString(cx + dx - 0.25*cm, cy + dy - 0.30*cm, sub)


def cpt_img5_honeycomb(c, cx, cy):
    """Honigwaben-Rezeptur — 8-hex grid with ingredients."""
    c.setFillColor(CREAM); c.setFont("Times-Bold", 11)
    c.drawCentredString(cx, cy + 2.4*cm, "4 ZUTATEN. MEHR NICHT.")
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
            c.setFillColor(GOLD); c.setFont("Times-Bold", 11)
            c.drawCentredString(x, y - hr*0.30, "1912")
    c.setFillColor(CREAM); c.setFont("Helvetica", 5.5)
    c.drawCentredString(cx, cy - 1.5*cm, "Bienenwachs · Avocadoöl · Jojoba · Carnauba")
    c.setFillColor(GREY); c.setFont("Helvetica-Oblique", 5)
    c.drawCentredString(cx, cy - 1.8*cm, "Keine Silikone · keine Harze · keine Säuren")


def cpt_img6_lifestyle(c, cx, cy):
    """4-quadrant lifestyle grid."""
    c.setFillColor(CREAM); c.setFont("Times-Bold", 10)
    c.drawCentredString(cx, cy + 2.4*cm, "EIN BALSAM. JEDES GLATTE LEDER.")
    quads = [(-1.4*cm,  1.0*cm, "SATTEL",   LEATHER_BR),
             ( 1.4*cm,  1.0*cm, "SOFA",     LEATHER_BR),
             (-1.4*cm, -1.0*cm, "AUTOSITZ", LEATHER_BR),
             ( 1.4*cm, -1.0*cm, "SCHUH",    LEATHER_BK)]
    for dx, dy, lbl, col in quads:
        c.setFillColor(col); c.setStrokeColor(WALNUT); c.setLineWidth(0.3)
        c.rect(cx + dx - 1.1*cm, cy + dy - 0.7*cm, 2.2*cm, 1.4*cm, fill=1, stroke=1)
        c.setFillColor(CREAM); c.setFont("Helvetica-Bold", 6)
        c.drawCentredString(cx + dx, cy + dy - 0.5*cm, lbl)
    # gold cross
    c.setStrokeColor(GOLD); c.setLineWidth(0.8)
    c.line(cx - 2.5*cm, cy, cx + 2.5*cm, cy)
    c.line(cx, cy - 1.7*cm, cx, cy + 1.7*cm)
    # central hex
    c.setFillColor(BLACK); _hex(c, cx, cy, 0.32*cm)
    c.setStrokeColor(GOLD); c.setLineWidth(0.5)
    pts = [(cx + 0.32*cm*math.cos(math.radians(60*i+30)), cy + 0.32*cm*math.sin(math.radians(60*i+30))) for i in range(6)]
    p = c.beginPath(); p.moveTo(*pts[0])
    for pt in pts[1:]: p.lineTo(*pt)
    p.close(); c.drawPath(p, fill=0, stroke=1)
    c.setFillColor(GREY); c.setFont("Helvetica-Oblique", 5)
    c.drawCentredString(cx, cy - 2.3*cm, "Nicht für Nubuk · Velours · Wildleder")


def cpt_img7_heritage(c, cx, cy):
    """1912 hero poster — the year IS the design."""
    c.setFillColor(CREAM); c.setFont("Times-Italic", 7)
    c.drawCentredString(cx, cy + 2.4*cm, "Schwarzwälder Qualität")
    c.setFillColor(GOLD); c.setFont("Times-Bold", 60)
    c.drawCentredString(cx, cy - 0.4*cm, "1912")
    # small tin and fir
    _draw_tin_topdown(c, cx + 1.8*cm, cy - 1.8*cm, w=0.9*cm, variant="farblos", show_label=False)
    _draw_fir(c, cx - 1.8*cm, cy - 1.8*cm, h=0.9*cm)
    c.setFillColor(CREAM); c.setFont("Helvetica-Bold", 5.5)
    c.drawCentredString(cx, cy - 2.5*cm, "FAMILIENMANUFAKTUR · BERNAU · MADE IN GERMANY")


# ─── A+ banner concepts ──────────────────────────────────────────────

def cpt_aplus1(c, cx, cy):
    """Heritage banner — fir silhouettes + glow + wordmark + three tins."""
    # fir silhouettes left
    for i in range(4):
        _draw_fir(c, cx - 4.0*cm + i*0.45*cm, cy - 0.3*cm, h=1.4*cm)
    # lantern glow right
    for i in range(8):
        c.setFillColor(Color(AMBER.red, AMBER.green, AMBER.blue, alpha=0.12 - i*0.014))
        c.circle(cx + 1.8*cm, cy + 0.4*cm, 0.9*cm + i*0.16*cm, fill=1, stroke=0)
    # wordmark
    c.setFillColor(GOLD); c.setFont("Times-BoldItalic", 15)
    c.drawCentredString(cx - 0.5*cm, cy + 0.3*cm, "Jotti")
    c.setFillColor(GOLD); c.setFont("Times-Italic", 7)
    c.drawCentredString(cx - 0.5*cm, cy - 0.05*cm, "Schwarzwälder Qualität · seit 1912")
    # 3 tins right
    for i, var in enumerate(["farblos", "braun", "schwarz"]):
        _draw_tin_3q(c, cx + 2.7*cm + i*0.5*cm, cy - 0.5*cm, w=1.0*cm - i*0.06*cm, variant=var)


def cpt_aplus_carousel(c, cx, cy):
    """5 USP hex tiles."""
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
    c.drawCentredString(cx, cy - 0.9*cm, "Bienenwachs · 1912 · 3-in-1 · Universell · Ohne Chemie")


def cpt_aplus_restoration(c, cx, cy):
    """Sofa-arm restoration wide banner."""
    c.setFillColor(LEATHER_BR); c.setStrokeColor(WALNUT); c.setLineWidth(0.3)
    c.roundRect(cx - 3.4*cm, cy - 1.0*cm, 6.8*cm, 1.4*cm, 0.3*cm, fill=1, stroke=1)
    # split overlay (left=dry)
    c.setFillColor(Color(0.2,0.2,0.2,alpha=0.55))
    c.rect(cx - 3.4*cm, cy - 1.0*cm, 3.4*cm, 1.4*cm, fill=1, stroke=0)
    # warm glow right
    c.setFillColor(Color(AMBER.red, AMBER.green, AMBER.blue, alpha=0.18))
    c.circle(cx + 1.8*cm, cy + 0.2*cm, 1.5*cm, fill=1, stroke=0)
    # divider
    c.setStrokeColor(GOLD); c.setLineWidth(0.6)
    c.line(cx, cy - 1.0*cm, cx, cy + 0.4*cm)
    # tin
    c.setFillColor(BLACK); c.setStrokeColor(GOLD)
    c.circle(cx - 2.7*cm, cy - 1.4*cm, 0.45*cm, fill=1, stroke=1)
    c.setFillColor(BEESWAX); c.circle(cx - 2.7*cm, cy - 1.4*cm, 0.35*cm, fill=1, stroke=0)
    # headline
    c.setFillColor(CREAM); c.setFont("Times-Bold", 11)
    c.drawCentredString(cx, cy + 1.4*cm, "IN 2 STUNDEN GESCHMEIDIG.")


def cpt_aplus_manufaktur(c, cx, cy):
    """Workshop banner."""
    _draw_workshop(c, cx, cy, w=6.0*cm, h=1.8*cm)
    c.setFillColor(CREAM); c.setFont("Times-Bold", 11)
    c.drawCentredString(cx, cy + 1.4*cm, "EINE REZEPTUR. VIER GENERATIONEN.")


def cpt_aplus_uses(c, cx, cy):
    """Use-case carousel — 5 leather items."""
    labels = ["SOFA", "SCHUH", "SATTEL", "AUTOSITZ", "TASCHE"]
    for i, lbl in enumerate(labels):
        x = cx - 2.2*cm + i*1.1*cm
        c.setFillColor(LEATHER_BR); c.setStrokeColor(GOLD); c.setLineWidth(0.4)
        c.roundRect(x - 0.45*cm, cy - 0.4*cm, 0.9*cm, 0.9*cm, 0.05*cm, fill=1, stroke=1)
        c.setFillColor(CREAM); c.setFont("Helvetica-Bold", 5.5)
        c.drawCentredString(x, cy - 0.7*cm, lbl)


def cpt_aplus_qa(c, cx, cy):
    c.setFillColor(GOLD); c.setFont("Times-Bold", 11)
    c.drawCentredString(cx, cy + 0.9*cm, "HÄUFIGE FRAGEN")
    for i, q in enumerate([
        "Macht Farblos das Leder dunkler?",
        "Geeignet für Wildleder / Nubuk?",
        "Bleibt ein klebriger Film zurück?",
        "Wie oft anwenden?",
        "Wie riecht der Balsam?",
        "Wirklich seit 1912?",
    ]):
        c.setFillColor(CREAM); c.setFont("Helvetica", 6)
        c.drawCentredString(cx, cy + 0.3*cm - i*0.17*cm, "· " + q)


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


# ─── Moodboard tile drawings ─────────────────────────────────────────

def md_workshop(c, cx, cy):
    _draw_workshop(c, cx, cy, w=4.0*cm, h=1.8*cm)


def md_honeycomb(c, cx, cy):
    _honeycomb(c, cx, cy + 0.3*cm, radius=1.6*cm, opacity=0.55, color=AMBER)
    c.setFillColor(BEESWAX); c.rect(cx - 0.5*cm, cy - 0.6*cm, 1.0*cm, 0.55*cm, fill=1, stroke=0)


def md_saddle(c, cx, cy):
    """Brown English saddle silhouette on wooden stand."""
    c.setFillColor(LEATHER_BR); c.setStrokeColor(WALNUT); c.setLineWidth(0.3)
    c.ellipse(cx - 1.5*cm, cy - 0.5*cm, cx + 1.5*cm, cy + 0.7*cm, fill=1, stroke=1)
    # pommel raise
    c.setFillColor(LEATHER_BR)
    c.ellipse(cx - 0.4*cm, cy + 0.4*cm, cx + 0.4*cm, cy + 0.85*cm, fill=1, stroke=1)
    # stand
    c.setFillColor(WALNUT); c.rect(cx - 0.1*cm, cy - 1.0*cm, 0.2*cm, 0.5*cm, fill=1, stroke=0)
    c.rect(cx - 1.0*cm, cy - 1.15*cm, 2.0*cm, 0.12*cm, fill=1, stroke=0)


def md_avocado(c, cx, cy):
    """Avocado halved on dark slate."""
    c.setFillColor(HexColor("#3A2810"))
    c.rect(cx - 1.8*cm, cy - 1.0*cm, 3.6*cm, 2.0*cm, fill=1, stroke=0)
    c.setFillColor(HexColor("#5A7A30"))
    c.ellipse(cx - 0.9*cm, cy - 0.7*cm, cx + 0.9*cm, cy + 0.7*cm, fill=1, stroke=0)
    c.setFillColor(HexColor("#C8D89A"))
    c.ellipse(cx - 0.7*cm, cy - 0.55*cm, cx + 0.7*cm, cy + 0.55*cm, fill=1, stroke=0)
    c.setFillColor(HexColor("#5A3818"))
    c.circle(cx, cy, 0.32*cm, fill=1, stroke=0)


def md_lantern(c, cx, cy):
    """Lantern glow + dark fir silhouettes."""
    for i in range(10):
        c.setFillColor(Color(AMBER.red, AMBER.green, AMBER.blue, alpha=0.12 - i*0.011))
        c.circle(cx + 0.8*cm, cy + 0.3*cm, 0.7*cm + i*0.16*cm, fill=1, stroke=0)
    for i in range(5):
        _draw_fir(c, cx - 1.6*cm + i*0.30*cm, cy, h=1.3*cm)


def md_brass(c, cx, cy):
    """Brass scale on walnut bench."""
    c.setFillColor(WALNUT); c.rect(cx - 1.8*cm, cy - 1.0*cm, 3.6*cm, 0.5*cm, fill=1, stroke=0)
    c.setFillColor(HexColor("#B58E4A")); c.setStrokeColor(GOLD); c.setLineWidth(0.3)
    c.rect(cx - 0.05*cm, cy - 0.4*cm, 0.10*cm, 1.2*cm, fill=1, stroke=0)
    c.rect(cx - 1.1*cm, cy + 0.7*cm, 2.2*cm, 0.08*cm, fill=1, stroke=0)
    c.circle(cx - 1.1*cm, cy + 0.55*cm, 0.32*cm, fill=1, stroke=1)
    c.circle(cx + 1.1*cm, cy + 0.55*cm, 0.32*cm, fill=1, stroke=1)


def md_palette(c, cx, cy):
    """Brand color swatches in a row."""
    cols = [BLACK, AMBER, GOLD, CREAM, BROWN, ONYX]
    for i, col in enumerate(cols):
        x = cx - 2.0*cm + i*0.7*cm
        c.setFillColor(col); c.setStrokeColor(HexColor("#CCCCCC")); c.setLineWidth(0.3)
        c.rect(x - 0.30*cm, cy - 0.5*cm, 0.60*cm, 1.0*cm, fill=1, stroke=1)


# ─── Page chrome ─────────────────────────────────────────────────────

def cover_page(canvas, doc):
    canvas.saveState()
    # full black bg
    canvas.setFillColor(BLACK); canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    # subtle honeycomb relief background
    _honeycomb(canvas, PAGE_W*0.75, PAGE_H*0.55, radius=9*cm, opacity=0.08, color=AMBER)
    _honeycomb(canvas, PAGE_W*0.15, PAGE_H*0.25, radius=5*cm, opacity=0.06, color=AMBER)
    # top gold band
    canvas.setFillColor(GOLD); canvas.rect(0, PAGE_H - 0.5*cm, PAGE_W, 0.5*cm, fill=1, stroke=0)
    # wordmark area
    canvas.setFillColor(GOLD); canvas.setFont("Times-BoldItalic", 56)
    canvas.drawString(ML, PAGE_H - 4.5*cm, "Jotti")
    canvas.setFillColor(GOLD); canvas.setFont("Times-Italic", 13)
    canvas.drawString(ML, PAGE_H - 5.2*cm, "Schwarzwälder Qualität · seit 1912")
    # title block
    canvas.setFillColor(CREAM); canvas.setFont("Times-Bold", 34)
    canvas.drawString(ML, PAGE_H - 8.4*cm, "Lederbalsam")
    canvas.setFillColor(CREAM); canvas.setFont("Helvetica", 14)
    canvas.drawString(ML, PAGE_H - 9.2*cm, "200 ml · 500 ml · Farblos · Braun · Schwarz")
    canvas.setStrokeColor(GOLD); canvas.setLineWidth(0.5)
    canvas.line(ML, PAGE_H - 10.0*cm, ML + 8*cm, PAGE_H - 10.0*cm)
    canvas.setFillColor(GOLD); canvas.setFont("Helvetica-Bold", 14)
    canvas.drawString(ML, PAGE_H - 10.9*cm, "Amazon.de — Content Brief")
    canvas.setFillColor(CREAM); canvas.setFont("Helvetica", 11)
    canvas.drawString(ML, PAGE_H - 11.5*cm, "Brandbook · Moodboard · 7 Listing-Bilder · A+ Premium · Master Copy")

    # meta row (cream labels, cream values, navy strap not used — gold instead)
    y = 4.5*cm
    fields = [("MARKE", "Jotti GmbH"), ("MARKT", "Amazon.de"), ("SKUs", "6 (3 Farben × 2 Größen)"), ("DATUM", "2026-05-16")]
    for i, (k, v) in enumerate(fields):
        x = ML + i * 4.4*cm
        canvas.setFillColor(GOLD); canvas.setFont("Helvetica-Bold", 8)
        canvas.drawString(x, y, k)
        canvas.setFillColor(CREAM); canvas.setFont("Helvetica", 11)
        canvas.drawString(x, y - 0.55*cm, v)

    # sample tins — fill cream/black middle space
    _draw_tin_topdown(canvas, PAGE_W - MR - 5.5*cm, PAGE_H - 11.0*cm, w=3.4*cm, variant="farblos", show_label=True)
    _draw_tin_topdown(canvas, PAGE_W - MR - 2.3*cm, PAGE_H - 11.5*cm, w=3.4*cm, variant="braun",   show_label=True)
    _draw_tin_topdown(canvas, PAGE_W - MR - 3.9*cm, PAGE_H - 14.0*cm, w=3.4*cm, variant="schwarz", show_label=True)
    # tagline
    canvas.setFillColor(GOLD); canvas.setFont("Helvetica-Oblique", 10)
    canvas.drawString(ML, PAGE_H - 15.0*cm, "Drei Farben. Zwei Größen. Eine Rezeptur.")

    # bottom strap
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
    canvas.drawString(ML + 1.5*cm, PAGE_H - 0.7*cm, "Lederbalsam — Amazon.de Content Brief")
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


# ─── Build ──────────────────────────────────────────────────────────

def build():
    doc = BaseDocTemplate(OUT, pagesize=A4,
                          leftMargin=ML, rightMargin=MR,
                          topMargin=MT, bottomMargin=MB,
                          title="Jotti Lederbalsam — Amazon.de Content Brief",
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

    # ───── 1 · Auf einen Blick ─────
    s.append(Paragraph("Auf einen Blick", H2)); s.append(HRule())
    glance = [
        ["Marke", "Jotti GmbH — Familienmanufaktur in Bernau, Schwarzwald. Gegründet 1912."],
        ["Produkt", "Lederbalsam (Wachs) — Bienenwachs · Avocadoöl · Jojoba · Carnauba. Hard-Tin/Dose."],
        ["SKU-Matrix", "3 Farben (Farblos · Braun · Schwarz) × 2 Größen (200 ml · 500 ml) = 6 Varianten."],
        ["Marktplatz", "Amazon.de · Kategorie: Lederpflege"],
        ["Top-Wettbewerber", "Leather Honey · Collonil · Sonax · Furniture Clinic · Tapir"],
        ["Hauptkeywords (DE)", "lederpflege auto (8.873) · lederpflege (3.017) · auto lederpflege (2.648) · lederbalsam (1.198) · lederpflege schuhe (1.175)"],
        ["Käufer-Trigger", '"Mein Ledersofa / Autositz / Sattel / meine Lederjacke wird trocken oder verblasst. Ich will etwas Natürliches, das nicht klebt und keine Chemie ist."'],
        ["Hero-USP", "Schwarzwälder Familienmanufaktur seit 1912 · Bienenwachs & Avocadoöl · ohne aggressive Chemie."],
    ]
    t = Table([[Paragraph(f"<b>{k}</b>", BODY), Paragraph(v, BODY)] for k, v in glance],
              colWidths=[3.8*cm, CW - 3.8*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,-1), HexColor("#F4EFE3")),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LINEBELOW", (0,0), (-1,-1), 0.3, HexColor("#E0DCC8")),
        ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 6), ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ]))
    s.append(t)

    # strategic lead
    s.append(Spacer(1, 0.5*cm))
    strat = Table([[Paragraph(
        "<b>Strategischer Lead.</b> Im SERP gewinnt Jotti den Klick durch eine <b>dunkle, mit Honigwabe versehene Dose</b> in einer Kategorie voller weißer/gelber Konkurrenz. "
        "Auf der Produktseite gewinnt Jotti den Conversion durch <b>variantengenaue Farb-Beweise</b> auf echtem Leder (Bild 2), den <b>2-Stunden Pflege-Moment</b> (Bild 3), "
        "das <b>5-Promises-Frame</b> in der Mobile-Fold (Bild 4) und das <b>1912-Heritage-Statement</b> (Bild 7).", BODY)]],
        colWidths=[CW])
    strat.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), BLACK),
        ("TEXTCOLOR", (0,0), (-1,-1), CREAM),
        ("LEFTPADDING", (0,0), (-1,-1), 14), ("RIGHTPADDING", (0,0), (-1,-1), 14),
        ("TOPPADDING", (0,0), (-1,-1), 10), ("BOTTOMPADDING", (0,0), (-1,-1), 10),
        ("BOX", (0,0), (-1,-1), 0.8, GOLD),
    ]))
    s.append(strat)

    # ───── 2 · Brandbook ─────
    s.append(PageBreak())
    s.append(Paragraph("1 · Brandbook", H2)); s.append(HRule())
    s.append(Paragraph(
        "Visuelle Grundlage: die bestehenden 500 ml-Labels (Farblos · Braun · Schwarz). "
        "Dunkles Schwarz mit Honigwaben-Relief, warmes Cream als Typo-Farbe, Gold als einziges Highlight-Metall. "
        "Die Forest-Green-Idee aus der ersten Briefing-PDF ist geparkt — wir halten die Linie der bereits produzierten Labels.", BODY))

    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("Farbpalette", H3))
    row1 = [ColorChip(BLACK, "#0E0E0E", "Jotti Black"),
            ColorChip(CHARCOAL,"#1B1814", "Wax Charcoal"),
            ColorChip(AMBER, "#C58A3A", "Honig Amber"),
            ColorChip(GOLD,  "#D9B36B", "Jotti Gold")]
    row2 = [ColorChip(CREAM, "#EFE6D2", "Pergament"),
            ColorChip(TAN,   "#C9985A", "Natur Tan · Farblos"),
            ColorChip(BROWN, "#6A3A1E", "Sattel Braun · Braun"),
            ColorChip(ONYX,  "#0A0A0A", "Onyx · Schwarz")]
    s.append(Table([row1], colWidths=[CW/4]*4,
                   style=TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),
                                     ("LEFTPADDING",(0,0),(-1,-1),0),
                                     ("RIGHTPADDING",(0,0),(-1,-1),6)])))
    s.append(Table([row2], colWidths=[CW/4]*4,
                   style=TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),
                                     ("LEFTPADDING",(0,0),(-1,-1),0),
                                     ("RIGHTPADDING",(0,0),(-1,-1),6)])))

    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph("Typografie", H3))
    typo = [
        ["Display / Brand", "Trajan Pro · Cormorant Garamond Bold (chiselled serif, gleich dem Label-Wordmark)"],
        ["Jotti Wordmark",  "Locked SVG — Script-Serif mit gold gebogener \"seit 1912\"-Inschrift"],
        ["Headlines",       "Recoleta SemiBold · GT Sectra (Heritage-Display-Serif)"],
        ["Body / Bullets",  "Söhne · Inter (Grotesk-Sans, cream auf schwarz)"],
        ["Cap-Strap",       "Body-Sans, small caps, +160 Tracking — nur für \"SCHWARZWÄLDER QUALITÄT · SEIT 1912\""],
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
    s.append(Paragraph("Voice / Markenton", H3))
    for r in [
        "Premium Deutsche Tradition. Honig-Wärme trifft Werkstatt-Präzision.",
        "Ruhig und sachlich. Wir verkaufen nicht laut — wir verkaufen alt.",
        "Konkret statt schwülstig. Statt \"hochwertig\" → \"seit 1912\". Statt \"premium\" → \"Bienenwachs &amp; Avocadoöl\".",
        "Drei Worte sind besser als zehn. Foto trägt 80 %, Text 20 %.",
        "Nie eco-wellness. Nie Discount. Nie SaaS-Minimalismus. Nie Pure White Background (außer Amazon-Pflicht bei Main Image).",
    ]:
        s.append(Paragraph("· " + r, BODY))

    sig = Table([[Paragraph(
        '<b>Signatur:</b> <i>"Schwarzwälder Lederpflege. Seit 1912. Bienenwachs &amp; Avocadoöl — mehr braucht es nicht."</i>', BODY)]],
        colWidths=[CW])
    sig.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), BLACK),
        ("TEXTCOLOR", (0,0), (-1,-1), GOLD),
        ("LEFTPADDING", (0,0), (-1,-1), 12), ("RIGHTPADDING", (0,0), (-1,-1), 12),
        ("TOPPADDING", (0,0), (-1,-1), 10), ("BOTTOMPADDING", (0,0), (-1,-1), 10),
    ]))
    s.append(Spacer(1, 0.2*cm)); s.append(sig)

    # ───── 3 · Moodboard ─────
    s.append(PageBreak())
    s.append(Paragraph("2 · Moodboard", H2)); s.append(HRule())
    s.append(Paragraph(
        "Stimmung: <b>Eine Schwarzwald-Werkstatt bei Nacht, beleuchtet von einer Laterne.</b> "
        "Warmes Seitenlicht. Dunkles Walnussholz. Werkzeuge, Messing, gut gepflegtes Leder. "
        "Wie ein Standbild aus einer Dokumentation über eine Familienwerkstatt, die sich seit 1912 nicht verändert hat — "
        "Hermès-Werkstatt meets feine Honig-Marke, nicht Apotheke.", BODY))
    s.append(Spacer(1, 0.3*cm))

    md_w = (CW - 0.4*cm) / 3
    md_h = 3.6*cm
    row1 = Table([[
        MoodTile("Werkstatt bei Nacht", "Walnuss · Messing · Leder", md_workshop, w=md_w, h=md_h, bg=BLACK),
        MoodTile("Honigwaben", "Signature Pattern", md_honeycomb, w=md_w, h=md_h, bg=CHARCOAL),
        MoodTile("Brauner Sattel", "Hauptlifestyle-Objekt", md_saddle, w=md_w, h=md_h, bg=CHARCOAL),
    ]], colWidths=[md_w]*3)
    row1.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),
                              ("LEFTPADDING",(0,0),(-1,-1),0), ("RIGHTPADDING",(0,0),(-1,-1),5)]))
    s.append(row1)
    s.append(Spacer(1, 0.2*cm))
    row2 = Table([[
        MoodTile("Avocado auf Schiefer", "Zutat-Stillleben", md_avocado, w=md_w, h=md_h, bg=CHARCOAL),
        MoodTile("Laternenlicht & Tanne", "Schwarzwald-Atmosphäre", md_lantern, w=md_w, h=md_h, bg=BLACK),
        MoodTile("Messingwaage", "Apotheker-Präzision", md_brass, w=md_w, h=md_h, bg=BLACK),
    ]], colWidths=[md_w]*3)
    row2.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),
                              ("LEFTPADDING",(0,0),(-1,-1),0), ("RIGHTPADDING",(0,0),(-1,-1),5)]))
    s.append(row2)
    s.append(Spacer(1, 0.2*cm))
    # palette tile alone
    row3 = Table([[
        MoodTile("Brand-Palette", "Black · Amber · Gold · Cream", md_palette, w=md_w, h=md_h, bg=CREAM),
    ]], colWidths=[md_w])
    row3.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),
                              ("LEFTPADDING",(0,0),(-1,-1),0), ("RIGHTPADDING",(0,0),(-1,-1),0)]))
    s.append(row3)

    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("Setdesign — Props-Liste", H3))
    props = [
        ("Hauptobjekte", "Brauner Sattel · Chesterfield Sofa-Arm · Oldtimer-Lederinnenraum · Brogues · Reitstiefel · abgewetzte Aktentasche"),
        ("Zutaten-Props", "Bienenwachs-Block (warm-amber) · Avocado auf dunkler Schiefer · kleiner Bernsteinglas-Flakon Öl · dunkler Tannenzweig"),
        ("Werkstatt-Props", "Messingwaage · Lederbund-Kontorbuch · alte Handwerkzeuge · Walnussholz-Bank · Pergament-Tuch · Honigtropfer"),
        ("Licht", "Eine warme Lichtquelle (~3200 K) von oben links, schmaler Lichtkegel. Subtile Vignette zu den Ecken."),
        ("Personen", "Nur Hände — ältere, leicht gezeichnete männliche Hände mit Canvas-/Wollhemd-Manschette. Keine Gesichter."),
        ("No-Gos", "Edelstahl · Glas · Plastik · helles Tageslicht · Pärchen-auf-Sofa-Klischees · AI-Lederfaktur"),
    ]
    pt = Table([[Paragraph(f"<b>{k}</b>", BODY), Paragraph(v, BODY)] for k, v in props],
               colWidths=[3.4*cm, CW - 3.4*cm])
    pt.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,-1), HexColor("#F4EFE3")),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LINEBELOW", (0,0), (-1,-1), 0.3, HexColor("#E0DCC8")),
        ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 5), ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ]))
    s.append(pt)

    # ───── 4 · Käuferpsychologie ─────
    s.append(PageBreak())
    s.append(Paragraph("3 · Käuferpsychologie", H2)); s.append(HRule())
    s.append(Paragraph("Drei überlappende Käufergruppen auf Amazon.de:", BODY))

    personas = [
        ("Der Heritage-Besitzer (45–65)",
         "Besitzt ein €3.000-Ledersofa, eine Glashütte mit Lederband, eine Aktentasche im Hermès-Stil, einen Mercedes E mit Ledersitzen. Will kein billiges Wundermittel — will ein ernsthaftes deutsches Produkt, das sein Vater hätte verwenden können."),
        ("Der Reiter / die Reiterin (25–55, ~70 % weiblich)",
         "Besitzt Sättel, Trensen, Reitstiefel. Lederpflege ist Routine, nicht Luxus. Kauft 500 ml als Nachfüllgröße. Liest Inhaltsstoffe — Angst vor allem, was teures Lederzeug austrocknet oder verfärbt."),
        ("Der Restaurator (30–50)",
         "Hat ein spezifisches Problem — eine verblasste Lederjacke, ein rissiger Autositz, ein ausgetrocknetes Sofakissen. Hat \"lederpflege auto\" oder \"lederbalsam schwarz\" gesucht. Will Sicherheit, dass *dieser* die Farbe wiederherstellt, ohne klebrig zu werden."),
    ]
    pt = Table([[Paragraph(f"<b>{k}</b>", BODY), Paragraph(v, BODY)] for k, v in personas],
               colWidths=[5.0*cm, CW - 5.0*cm])
    pt.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,-1), BLACK),
        ("TEXTCOLOR", (0,0), (0,-1), GOLD),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LINEBELOW", (0,0), (-1,-1), 0.3, HexColor("#E0DCC8")),
        ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 7), ("BOTTOMPADDING", (0,0), (-1,-1), 7),
    ]))
    s.append(pt)

    s.append(Spacer(1, 0.4*cm))
    s.append(Paragraph("Kauf-Einwände — und wo wir sie töten", H3))
    obj = [
        ("\"Macht es mein Leder dunkler?\"", "Bild 2 — Farb-Beweis variantenspezifisch auf echtem Leder."),
        ("\"Funktioniert es gegen Risse?\"", "Bild 3 — der 2-Stunden-Pflege-Moment auf echtem Sofa-Arm."),
        ("\"Ist es fettig oder klebrig?\"", "Bullet 5 + A+ Q&A: \"seidenmatter Glanz, 2 Std., kein Restschmierfilm\"."),
        ("\"Riecht es nach Chemie?\"", "Bild 5 + Q&A: \"dezent natürlich nach Bienenwachs. Nicht parfümiert.\""),
        ("\"Ist deutsche Manufakturqualität echt?\"", "Bild 7 + Modul 4: das große \"1912\" als zentrales Trust-Statement."),
        ("\"Verfärbt es bei Nässe?\" (1★-Review)", "Bullet 5 + Q&A: korrekte Anwendung — dünn auftragen, 2 h einziehen lassen, polieren."),
        ("\"500 ml zu viel / 200 ml zu wenig?\"", "Bild 7 — Größenvergleich mit Anwendungs-Yield."),
    ]
    ot = Table([[Paragraph(f"<b>{k}</b>", BODY), Paragraph(v, BODY)] for k, v in obj],
               colWidths=[6.0*cm, CW - 6.0*cm])
    ot.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,-1), HexColor("#F4EFE3")),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LINEBELOW", (0,0), (-1,-1), 0.3, HexColor("#E0DCC8")),
        ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 6), ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ]))
    s.append(ot)

    # ───── 5 · Main Image 3 Options ─────
    s.append(PageBreak())
    s.append(Paragraph("4 · Main Image — 3 Optionen für CTR-Test", H2)); s.append(HRule())
    s.append(Paragraph(
        "Amazon Hauptbild-Regeln: pure white Background (#FFFFFF), Produkt füllt ≥ 85 % der Fläche, kein Overlay-Text. "
        "Drei Konzepte testen Premium-Heritage, Open-Tin-Reveal und Familien-Range. 4-Wochen A/B/C-Test via Manage Your Experiments — "
        "Sieger wird Bild #1, andere rutschen auf #2 / #6.", BODY))
    s.append(Spacer(1, 0.3*cm))

    options = [
        ("A", "Floating Heritage",
         "Die Dose schwebt im 3/4-Winkel mit langem, weichen amber-goldenen Schatten — wie ein Museums-Katalogfoto. Kein Prop. Kein Overlay-Text.",
         "Premium-Watch-Catalogue-Energie. Liest sofort als 'edles deutsches Erbstück'. Sicherste Launch-Option.",
         cpt_main_a),
        ("B", "Wax Reveal",
         "Top-Down mit Deckel leicht daneben — die Bernstein-Bienenwachs-Oberfläche im Inneren wird sichtbar. Honigwaben-Relief im Wachs.",
         "Einzigartig in der Kategorie: jeder Konkurrent zeigt geschlossene Dosen. Macht den Zutaten-Beweis im SERP sichtbar.",
         cpt_main_b),
        ("C", "Familien-Hero",
         "Drei Dosen (Farblos · Braun · Schwarz) gestaffelt im 3/4-Winkel — kommuniziert sofort 'das ist eine Familie von 3 Farben'.",
         "Cross-sell auf den ersten Pixel. Effektiv für Käufer, die zwischen Varianten unentschlossen sind.",
         cpt_main_c),
    ]
    for letter, name, desc, pitch, fn in options:
        s.append(Paragraph(f"Option {letter} — {name}", H3))
        m = MainOption(letter, name, fn)
        side = _side([
            Paragraph(f"<b>Komposition:</b> {desc}", BODY),
            Spacer(1, 0.1*cm),
            Paragraph(f"<i>CTR-Hebel:</i> {pitch}", QUOTE),
        ], CW - m.size - m.gap)
        row = Table([[m, side]], colWidths=[m.size + m.gap, CW - m.size - m.gap])
        row.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),
                                 ("LEFTPADDING",(0,0),(-1,-1),0), ("RIGHTPADDING",(0,0),(-1,-1),0)]))
        s.append(KeepTogether([row])); s.append(Spacer(1, 0.35*cm))

    rec = Table([[Paragraph(
        "<b>Empfehlung:</b> Launch mit <b>Option A (Floating Heritage)</b> als sicherer Baseline. Parallel B und C als Challenger vorbereiten. "
        "4-Wochen A/B/C-Test. Sieger wird permanentes Bild #1; die anderen werden Slot #2 oder #6.", BODY)]],
        colWidths=[CW])
    rec.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), GOLD),
        ("LEFTPADDING", (0,0), (-1,-1), 12), ("RIGHTPADDING", (0,0), (-1,-1), 12),
        ("TOPPADDING", (0,0), (-1,-1), 10), ("BOTTOMPADDING", (0,0), (-1,-1), 10),
    ]))
    s.append(rec)

    # ───── 6 · 7 Listing Images ─────
    s.append(PageBreak())
    s.append(Paragraph("5 · Sieben Listing-Bilder (Galerie)", H2)); s.append(HRule())
    s.append(Paragraph(
        "Format: 2000 × 2000 px · sRGB · JPG · ≤ 5 MB. Reuse-Policy: Bilder 3–7 sind shared (alle 6 SKUs); 1, 2 sind variant-aware. "
        "Layout-Regel: Foto trägt 80 %, Copy max. 12 Wörter pro Frame. Eine Hero-Element pro Frame.", SUB))

    listings = [
        (1, "Click Trigger",
         "(kein Overlay — Sieger von A/B/C oben)",
         "Siehe Main-Image-Optionen oben. A/B/C-Test, Sieger wird permanent.",
         cpt_main_a, WHITE),
        (2, "Hook · Farb-Beweis",
         "Farblos: Pflegt. Schützt. Verändert nichts.  ·  Braun: Bringt Braun zurück.  ·  Schwarz: Belebt tiefes Schwarz.",
         "Echtes Lederobjekt halbiert — eine Hälfte konditioniert, eine Hälfte stumpf. Variant-spezifische Headline. Killt die #1 Kauf-Sorge ('macht es dunkler?'). Wichtigster CVR-Frame.",
         cpt_img2_variant, BLACK),
        (3, "Pflege-Moment",
         "In 2 Stunden geschmeidig.",
         "Cinematic Einzelaufnahme: ältere Hand mit Pergament-Tuch auf braunem Sofa-Arm. Offene Dose im Vordergrund, Wachs glänzt. Warmes Fensterlicht.",
         cpt_img3_moment, BLACK),
        (4, "5 Promises",
         "5 Gründe Jotti.",
         "Promoted in Slot #4 (Mobile-Fold). Fünf Badges um die Dose: NATÜRLICH · MADE IN GERMANY · 3-IN-1 · UNIVERSELL · OHNE CHEMIE. Im Mobile-Carousel sichtbar.",
         cpt_img4_benefits, BLACK),
        (5, "Honigwaben-Rezeptur",
         "4 Zutaten. Mehr nicht.",
         "Honigwaben-Hexagon-Gitter als Layout — 6 Hexagons. Bienenwachs · Avocadoöl · Jojoba · Carnauba im eigenen Hex. Brand-Signature-Frame.",
         cpt_img5_honeycomb, BLACK),
        (6, "Universal-Anwendung",
         "Ein Balsam. Jedes glatte Leder.",
         "4-Quadranten-Grid: Sattel · Sofa · Autositz · Schuh. Disclaimer unten: 'Nicht für Nubuk · Velours · Wildleder'.",
         cpt_img6_lifestyle, BLACK),
        (7, "Heritage · 1912",
         "Familienmanufaktur · Bernau · Made in Germany.",
         "1912 als 80 % der Canvas in Gold-Display-Serif. Tannenzweig + kleine Dose unten. Wie ein Museumsplakat, kein Infografik-Layout.",
         cpt_img7_heritage, BLACK),
    ]
    for slot, role, headline, why, fn, bg in listings:
        s.append(Paragraph(f"Bild {slot} — {role}", H3))
        m = ListingMockup(slot, role, fn, bg=bg)
        side = _side([
            Paragraph(f"<b>Headline:</b> {headline}", BODY),
            Spacer(1, 0.1*cm),
            Paragraph(f"<i>Konzept &amp; Wirkung:</i> {why}", QUOTE),
        ], CW - m.size - m.gap)
        row = Table([[m, side]], colWidths=[m.size + m.gap, CW - m.size - m.gap])
        row.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),
                                 ("LEFTPADDING",(0,0),(-1,-1),0), ("RIGHTPADDING",(0,0),(-1,-1),0)]))
        s.append(KeepTogether([row])); s.append(Spacer(1, 0.30*cm))

    # ───── 7 · A+ Premium ─────
    s.append(PageBreak())
    s.append(Paragraph("6 · A+ Premium Content (7 Module)", H2)); s.append(HRule())
    s.append(Paragraph("Parent-Level — gilt für alle 6 SKUs. Komplett auf Deutsch, gestrafft.", SUB))

    modules = [
        (1, "Full Image", "Schwarzwälder Lederpflege seit 1912.",
         "Familienmanufaktur · Bernau", cpt_aplus1, BLACK),
        (2, "Karussell (5)", "5 Gründe Jotti — Bienenwachs · 1912 · 3-in-1 · Universell · Ohne Chemie",
         "5 Hex-Kacheln mit gold Linien-Icons", cpt_aplus_carousel, BLACK),
        (3, "Full Image", "In 2 Stunden geschmeidig.",
         "Eine Anwendung. Kein Fettfilm. Kein klebriger Rückstand.", cpt_aplus_restoration, BLACK),
        (4, "Full Image", "Eine Rezeptur. Vier Generationen.",
         "Seit 1912 in Bernau im Schwarzwald. Gleiche Rezeptur. Gleicher Anspruch.", cpt_aplus_manufaktur, BLACK),
        (5, "Karussell (5)", "Sofa · Schuh · Sattel · Autositz · Tasche",
         "Use-Case-Karussell — Rembrandt-belichtete Lifestyle-Aufnahmen", cpt_aplus_uses, BLACK),
        (6, "Q&A", "6 häufige Fragen — voice-aligned",
         "Farbe · Wildleder · Rückstand · Häufigkeit · Duft · 1912-Echtheit", cpt_aplus_qa, BLACK),
        (7, "Vergleichschart", "Jotti Range im Vergleich",
         "Lederbalsam vs. flüssig vs. Wachs vs. Polster vs. Imprägnierer vs. Reiniger", cpt_aplus_compare, BLACK),
    ]
    for slot, mtype, hl, sub, fn, bg in modules:
        s.append(Paragraph(f"Modul {slot} — {mtype}", H3))
        m = APlusMockup(slot, mtype, fn, bg=bg)
        side = _side([
            Paragraph(f"<b>Headline:</b> {hl}", BODY),
            Paragraph(f"<b>Body / Thema:</b> {sub}", BODY),
        ], CW - m.bw - m.gap)
        row = Table([[m, side]], colWidths=[m.bw + m.gap, CW - m.bw - m.gap])
        row.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),
                                 ("LEFTPADDING",(0,0),(-1,-1),0), ("RIGHTPADDING",(0,0),(-1,-1),0)]))
        s.append(KeepTogether([row])); s.append(Spacer(1, 0.30*cm))

    # ───── 8 · Q&A + Comparison ─────
    s.append(PageBreak())
    s.append(Paragraph("Modul 6 — Q&amp;A (vollständig)", H3))
    qa = [
        ("Macht Farblos mein Leder dunkler?",
         "Nein. Farblos ist farblos formuliert — pflegt, macht geschmeidig und schützt, ohne den Farbton zu verändern. Wählen Sie Braun oder Schwarz nur, um eine verblasste Farbe aufzufrischen."),
        ("Geeignet für Nubuk, Velours oder Alcantara?",
         "Nein. Jotti Lederbalsam ist ausschließlich für glattes und strukturiertes Leder. Auf Nubuk, Velours, Alcantara oder Wildleder würde der Wachs-Öl-Balsam die Faser flach legen — dafür gibt es spezielle Bürstenpflege."),
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

    s.append(Spacer(1, 0.4*cm))
    s.append(Paragraph("Modul 7 — Vergleichschart", H3))
    comp = [
        ["Merkmal", "Lederbalsam\n(dieses)", "Lederpflege\nflüssig", "Möbel-\npflege Wachs", "Polster-\nspray", "Imprägnierer", "Leder-\nreiniger"],
        ["Produkttyp", "Wachs-Öl-Balsam", "Flüssig", "Möbelwachs", "Spray", "Imprägnierspray", "Flüssigreiniger"],
        ["Ideal für", "Pflege + Schutz glattes Leder", "Tägliche Tiefenpflege", "Holzmöbel", "Stoff & Textil", "Wasser- & Schmutzschutz", "Anhaftende Schmutz"],
        ["Anwendung", "Sofa · Sattel · Schuh · Auto", "Alle glatten Leder", "Tische · Schränke", "Sofa · Sitze (Stoff)", "Leder · Schuhe", "Vor der Pflege"],
        ["Größe", "200 / 500 ml", "500 ml", "200 / 500 ml", "500 ml", "500 ml", "500 ml"],
        ["Hauptzutaten", "Bienenwachs · Avocado · Jojoba · Carnauba", "Natürliche Öle", "Bienenwachs · Carnauba", "Pflanzliche Tenside", "Fluorcarbon-frei", "Milde Tenside"],
        ["Made in Germany", "✓ seit 1912", "✓ seit 1912", "✓ seit 1912", "✓ seit 1912", "✓ seit 1912", "✓ seit 1912"],
    ]
    comp_tbl = Table(comp, colWidths=[2.8*cm] + [(CW - 2.8*cm)/6]*6)
    comp_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), BLACK),
        ("TEXTCOLOR", (0,0), (-1,0), GOLD),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("BACKGROUND", (1,1), (1,-1), HexColor("#F4EFE3")),
        ("FONTNAME", (1,1), (1,-1), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,-1), 7),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("LEFTPADDING", (0,0), (-1,-1), 4), ("RIGHTPADDING", (0,0), (-1,-1), 4),
        ("TOPPADDING", (0,0), (-1,-1), 4), ("BOTTOMPADDING", (0,0), (-1,-1), 4),
        ("GRID", (0,0), (-1,-1), 0.3, HexColor("#DDDDDD")),
    ]))
    s.append(comp_tbl)

    # ───── 9 · Master Copy ─────
    s.append(PageBreak())
    s.append(Paragraph("7 · Master Copy (paste-ready, Deutsch)", H2)); s.append(HRule())

    s.append(Paragraph("Titel — variantengenau (max. 200 Zeichen)", H3))
    titles = [
        ("Farblos 500 ml", "Jotti Lederbalsam Farblos 500 ml – Premium Lederpflege mit Bienenwachs &amp; Avocadoöl für Schuhe, Jacken, Taschen, Sofa, Autositze, Sattel – Made in Germany seit 1912"),
        ("Braun 500 ml",   "Jotti Lederbalsam Braun 500 ml – Premium Lederpflege mit Bienenwachs für braune Schuhe, Sofa, Autositze, Sattel, Lederjacken – Farbauffrischend – Made in Germany seit 1912"),
        ("Schwarz 500 ml", "Jotti Lederbalsam Schwarz 500 ml – Premium Lederpflege mit Bienenwachs für schwarze Schuhe, Lederjacken, Sofa, Autositze, Sattel – Farbauffrischend – Made in Germany seit 1912"),
        ("200 ml Größen",   "Identische Struktur — '500 ml' → '200 ml' tauschen und 'Reisegröße' / 'Alltagsgröße' als Differenzierer ergänzen."),
    ]
    tt = Table([[Paragraph(f"<b>{k}</b>", BODY), Paragraph(v, BODY)] for k, v in titles],
               colWidths=[3.5*cm, CW - 3.5*cm])
    tt.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,-1), BLACK),
        ("TEXTCOLOR", (0,0), (0,-1), GOLD),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LINEBELOW", (0,0), (-1,-1), 0.3, HexColor("#E0DCC8")),
        ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 6), ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ]))
    s.append(tt)

    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("Bullets — 5 × ~240 Zeichen", H3))
    bullets = [
        ("PREMIUM LEDERPFLEGE SEIT 1912",
         "Hochwertiger Lederbalsam aus deutscher Familienmanufaktur im Schwarzwald. Pflegt, nährt und schützt alle glatten Lederarten mit der unveränderten Rezeptur unserer Manufaktur seit 113 Jahren."),
        ("NATÜRLICHE REZEPTUR · BIENENWACHS &amp; AVOCADOÖL",
         "Jojoba, Carnaubawachs und Lanolin ziehen tief ins Leder ein, füllen feine Risse und versiegeln die Oberfläche – ohne Silikone, Harze, Säuren oder künstliche Farbstoffe."),
        ("3-IN-1: REINIGT · PFLEGT · SCHÜTZT",
         "Ein Produkt statt drei. Reinigung, Pflege und Imprägnierung in einem Arbeitsgang. Spart Zeit, Geld und Schrankplatz. Wasser- und schmutzabweisend nach nur einer Anwendung."),
        ("UNIVERSELL EINSETZBAR",
         "Geeignet für Lederjacken, Lederschuhe, Ledertaschen, Sattelzeug, Ledersofas, Autositze und mehr. Erhältlich in Farblos (erhält die Naturfarbe), Braun und Schwarz (farbauffrischend)."),
        ("EINFACHE ANWENDUNG · 2 STUNDEN · KEIN RESTSCHMIERFILM",
         "Dünn mit Tuch oder Schwamm auftragen, ca. 2 Stunden einziehen lassen, bei Bedarf nachpolieren. Seidenmatter Glanz, dezenter Bienenwachs-Duft. Nicht für Nubuk-, Velours- oder Wildleder."),
    ]
    bt = Table([[Paragraph(f"<b>{i+1}. {h}</b>", BODY), Paragraph(b, BODY)] for i, (h, b) in enumerate(bullets)],
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
    s.append(Paragraph("Backend Search Terms (max. 450 Bytes)", H3))
    be = Table([[Paragraph(
        '<font face="Courier" size="8">bienenwachs lederpflege auto für ledercouch sofa tasche jacke lederbalsam farblos lederfett ledercreme '
        'neutral leather honey conditioner sattelfett sattelseife schuhcreme lederreiniger ledersitze pflege motorradkombi reiten pferd glattleder '
        'kunstleder couch möbel autositz aktentasche stiefel reitstiefel handtasche oldtimer chesterfield deutsche manufaktur schwarzwald</font>', BODY)]],
        colWidths=[CW])
    be.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), HexColor("#F5F5F5")),
        ("LEFTPADDING", (0,0), (-1,-1), 10), ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 7), ("BOTTOMPADDING", (0,0), (-1,-1), 7),
    ]))
    s.append(be)

    # ───── 10 · Priority Uplifts ─────
    s.append(PageBreak())
    s.append(Paragraph("8 · Priority Uplifts (CTR × CVR)", H2)); s.append(HRule())
    pri = [
        ("1", "Main-Image A/B/C-Test (Manage Your Experiments)",
         "Drei Hero-Konzepte oben (Floating · Wax Reveal · Familien-Hero). 4 Wochen Test. Größter CTR-Hebel ohne operativen Aufwand."),
        ("2", "Bild 2 — variantengenauer Farb-Beweis",
         "Echtes Lederobjekt halbiert, eine Hälfte konditioniert. Killt die #1 Kauf-Sorge ('macht es dunkler?'). Wichtigster CVR-Frame."),
        ("3", "Bild 4 — 5-Promises in der Mobile-Fold",
         "Natürlich · Made in Germany · 3-in-1 · Universell · Ohne Chemie. Beantwortet die 5 wichtigsten Käuferfragen vor dem Scroll-Drop."),
        ("4", "A+ Modul 6 (Q&A) mit 6 voice-aligned Antworten",
         "Defusiert: 'macht es dunkler', 'fettig?', 'wie oft?', 'wirklich von 1912?'. Senkt Retouren und negative Reviews."),
        ("5", "A+ Modul 7 (Vergleichschart) — Jotti Range",
         "Cross-sell: Lederbalsam ist Teil eines Sortiments. Erhöht AOV und CLV."),
        ("6", "Variant-Aware Bild 7 (1912 Heritage Poster)",
         "Das 1912 als Hero-Element. Closing-Trust-Signal — niemand in der Kategorie kann das kopieren."),
        ("7", "Subscribe &amp; Save für 500 ml prüfen",
         "Sattler und Reiter als Repeat-Buyer-Segment — S&S funktioniert. Mit Brand bestätigen."),
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
    s.append(Paragraph("Offene Punkte für die Brand", H3))
    for line in [
        "Archivfoto aus 1912 vorhanden? Wenn nein: Studio-Mockup einer Werkstatt-Szene shooten (klar gestyled, nie AI-Fake-Vintage).",
        "Legal-Name 'Jotti GmbH &amp; Co.KG' oder 'JOTTI GmbH' — Schreibweise locken für Label-Footer.",
        "Subscribe &amp; Save für 500 ml — mit Brand klären.",
        "Vine / Launch-Promo Budget — mit Brand klären.",
        "Variant-Photoshoot: 13 Setups in einem 1-Tag-Shoot (alle 6 SKUs Hero + 3 Lifestyle + Werkstatt + Zutaten).",
    ]:
        s.append(Paragraph("· " + line, BODY))

    doc.build(s)
    print(f"PDF: {OUT}")


if __name__ == "__main__":
    build()
