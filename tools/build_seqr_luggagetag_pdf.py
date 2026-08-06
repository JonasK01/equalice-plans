#!/usr/bin/env python3
"""SeQR Contact — Smart Luggage Tags (2-pack QR luggage tags · B0DY1L5RPM)
Brand · Moodboard · 3 Main Image Options · 7 Listing Images · A+ Premium · Master Copy.
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

OUT = "/Users/jonask/Desktop/SeQR_Smart_Luggage_Tags_Brief.pdf"

# ─── SeQR palette (matched to the existing KeyTag / Luggage Tag designs) ────
TEAL    = HexColor("#1AAEB6")
NAVY    = HexColor("#0F2944")
PINK    = HexColor("#E8345C")
YELLOW  = HexColor("#F4C040")
SAND    = HexColor("#F2EDE2")
SAND_DK = HexColor("#E5DEC9")
INK     = HexColor("#111111")
GREY    = HexColor("#666666")
LIGHT   = HexColor("#F5F5F5")
WHITE   = HexColor("#FFFFFF")
GREEN_OK= HexColor("#3FA770")
RED_X   = HexColor("#D24545")
WARN_BG = HexColor("#FFF4E5")
WARN_BD = HexColor("#B5390A")
LUG_BR  = HexColor("#34526E")     # luggage shell — slate blue
LUG_BG  = HexColor("#D1B58C")     # luggage shell — tan beige

PAGE_W, PAGE_H = A4
ML, MR, MT, MB = 1.6*cm, 1.6*cm, 1.8*cm, 1.6*cm
CW = PAGE_W - ML - MR

styles = getSampleStyleSheet()
H1   = ParagraphStyle("H1", parent=styles["Title"],   fontName="Helvetica-Bold",fontSize=26,leading=30,textColor=NAVY,spaceAfter=4,alignment=TA_LEFT)
SUB  = ParagraphStyle("SUB", parent=styles["Normal"], fontName="Helvetica",    fontSize=10,leading=13,textColor=GREY,spaceAfter=12)
H2   = ParagraphStyle("H2", parent=styles["Heading2"],fontName="Helvetica-Bold",fontSize=18,leading=22,textColor=NAVY,spaceBefore=12,spaceAfter=6)
H3   = ParagraphStyle("H3", parent=styles["Heading3"],fontName="Helvetica-Bold",fontSize=11,leading=14,textColor=INK,spaceBefore=10,spaceAfter=4)
BODY = ParagraphStyle("Body",parent=styles["Normal"], fontName="Helvetica",    fontSize=9.5,leading=13,textColor=INK,spaceAfter=3)
SMALL= ParagraphStyle("Small",parent=BODY,fontSize=8,leading=11,textColor=GREY)
QUOTE= ParagraphStyle("Quote",parent=BODY,fontName="Helvetica-Oblique",textColor=GREY)


# ─── Flowables ──────────────────────────────────────────────────────

class HRule(Flowable):
    def __init__(self, width=None, color=TEAL, thickness=1.4):
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
        c.setFillColor(self.color); c.setStrokeColor(HexColor("#DDDDDD"))
        c.setLineWidth(0.3)
        c.rect(0, 0.9*cm, self.w, self.h, fill=1, stroke=1)
        c.setFillColor(INK); c.setFont("Helvetica-Bold", 9)
        c.drawString(0, 0.45*cm, self.name)
        c.setFillColor(GREY); c.setFont("Courier", 8)
        c.drawString(0, 0.15*cm, self.hex_label)


# ─── Drawing helpers ────────────────────────────────────────────────

def _draw_qr(c, cx, cy, size=1.0*cm, color=NAVY, bg=WHITE):
    """Stylised QR — 3 corner finders + noise dots."""
    x = cx - size/2; y = cy - size/2
    c.setFillColor(bg)
    c.rect(x, y, size, size, fill=1, stroke=0)
    c.setFillColor(color)
    cs = size * 0.27
    # corner finders (top-left, top-right, bottom-left)
    for fx, fy in [(x, y + size - cs), (x + size - cs, y + size - cs), (x, y)]:
        c.rect(fx, fy, cs, cs, fill=1, stroke=0)
        c.setFillColor(bg)
        c.rect(fx + cs*0.18, fy + cs*0.18, cs*0.64, cs*0.64, fill=1, stroke=0)
        c.setFillColor(color)
        c.rect(fx + cs*0.32, fy + cs*0.32, cs*0.36, cs*0.36, fill=1, stroke=0)
    # noise grid
    cell = size / 13
    import random
    rng = random.Random(7)
    for r in range(13):
        for col in range(13):
            # skip finder regions
            if (r < 4 and col < 4) or (r < 4 and col >= 9) or (r >= 9 and col < 4):
                continue
            if rng.random() < 0.42:
                c.rect(x + col*cell, y + r*cell, cell*0.85, cell*0.85, fill=1, stroke=0)


def _draw_tag(c, cx, cy, w=2.4*cm, h=3.2*cm, color=TEAL, with_qr=True, with_loop=True, label=None):
    """Luggage tag: rounded rect with hole + optional QR + loop strap."""
    # tag body
    c.setFillColor(color); c.setStrokeColor(NAVY); c.setLineWidth(0.5)
    c.roundRect(cx - w/2, cy - h/2, w, h, 0.12*cm, fill=1, stroke=1)
    # top hole
    c.setFillColor(WHITE); c.setStrokeColor(NAVY); c.setLineWidth(0.3)
    c.circle(cx, cy + h/2 - 0.2*cm, 0.10*cm, fill=1, stroke=1)
    # loop strap above hole
    if with_loop:
        c.setStrokeColor(HexColor("#9AA0A6")); c.setLineWidth(0.8)
        c.line(cx, cy + h/2 - 0.15*cm, cx, cy + h/2 + 0.6*cm)
        c.setStrokeColor(HexColor("#9AA0A6")); c.setLineWidth(1.2)
        # carabiner ring
        c.ellipse(cx - 0.15*cm, cy + h/2 + 0.45*cm, cx + 0.15*cm, cy + h/2 + 0.7*cm, fill=0, stroke=1)
    # QR centered
    if with_qr:
        _draw_qr(c, cx, cy + h*0.05, size=min(w, h) * 0.55, color=NAVY, bg=WHITE)
    # bottom label strip
    if label:
        strip_h = 0.36*cm
        c.setFillColor(NAVY)
        c.rect(cx - w/2 + 0.08*cm, cy - h/2 + 0.08*cm, w - 0.16*cm, strip_h, fill=1, stroke=0)
        c.setFillColor(WHITE); c.setFont("Helvetica-Bold", 5.5)
        c.drawCentredString(cx, cy - h/2 + 0.18*cm, label)


def _draw_suitcase(c, cx, cy, w=2.6*cm, h=2.0*cm, color=LUG_BR):
    """Stylised hard-shell suitcase."""
    c.setFillColor(color); c.setStrokeColor(NAVY); c.setLineWidth(0.5)
    c.roundRect(cx - w/2, cy - h/2, w, h, 0.18*cm, fill=1, stroke=1)
    # vertical seam
    c.setStrokeColor(NAVY); c.setLineWidth(0.4)
    c.line(cx, cy - h/2 + 0.1*cm, cx, cy + h/2 - 0.1*cm)
    # handle on top
    c.setStrokeColor(NAVY); c.setLineWidth(0.7)
    c.line(cx - w*0.25, cy + h/2, cx - w*0.25, cy + h/2 + 0.3*cm)
    c.line(cx + w*0.25, cy + h/2, cx + w*0.25, cy + h/2 + 0.3*cm)
    c.line(cx - w*0.25, cy + h/2 + 0.3*cm, cx + w*0.25, cy + h/2 + 0.3*cm)
    # wheels
    c.setFillColor(NAVY)
    c.circle(cx - w*0.32, cy - h/2 - 0.08*cm, 0.08*cm, fill=1, stroke=0)
    c.circle(cx + w*0.32, cy - h/2 - 0.08*cm, 0.08*cm, fill=1, stroke=0)


def _draw_phone(c, cx, cy, w=1.4*cm, h=2.4*cm, scanning=False):
    """Phone with optional scan frame."""
    c.setFillColor(NAVY); c.setStrokeColor(NAVY); c.setLineWidth(0.4)
    c.roundRect(cx - w/2, cy - h/2, w, h, 0.12*cm, fill=1, stroke=1)
    c.setFillColor(WHITE)
    c.roundRect(cx - w/2 + 0.08*cm, cy - h/2 + 0.25*cm, w - 0.16*cm, h - 0.5*cm, 0.05*cm, fill=1, stroke=0)
    if scanning:
        c.setStrokeColor(TEAL); c.setLineWidth(1.2)
        sx = cx - w*0.3; sy = cy - h*0.2; ss = w*0.6
        bl = 0.14*cm
        c.line(sx, sy, sx + bl, sy);                  c.line(sx, sy, sx, sy + bl)
        c.line(sx + ss, sy, sx + ss - bl, sy);        c.line(sx + ss, sy, sx + ss, sy + bl)
        c.line(sx, sy + ss, sx + bl, sy + ss);        c.line(sx, sy + ss, sx, sy + ss - bl)
        c.line(sx + ss, sy + ss, sx + ss - bl, sy + ss); c.line(sx + ss, sy + ss, sx + ss, sy + ss - bl)
    else:
        # speech bubble / message icon
        c.setFillColor(TEAL)
        c.roundRect(cx - w*0.32, cy - h*0.10, w*0.45, h*0.18, 0.06*cm, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.circle(cx - w*0.18, cy - h*0.01, 0.04*cm, fill=1, stroke=0)
        c.circle(cx - w*0.05, cy - h*0.01, 0.04*cm, fill=1, stroke=0)
        c.circle(cx + w*0.08, cy - h*0.01, 0.04*cm, fill=1, stroke=0)


def _draw_water_drops(c, cx, cy, count=5):
    """Small water droplet cluster."""
    import random
    rng = random.Random(11)
    for _ in range(count):
        dx = (rng.random() - 0.5) * 1.6*cm
        dy = (rng.random() - 0.5) * 1.0*cm
        c.setFillColor(HexColor("#7AB7E0"))
        c.circle(cx + dx, cy + dy, 0.10*cm, fill=1, stroke=0)


def _draw_check(c, cx, cy, size=0.5*cm, color=GREEN_OK):
    c.setStrokeColor(color); c.setLineWidth(1.6)
    c.line(cx - size*0.3, cy, cx - size*0.05, cy - size*0.25)
    c.line(cx - size*0.05, cy - size*0.25, cx + size*0.3, cy + size*0.3)


def _draw_x(c, cx, cy, size=0.5*cm, color=RED_X):
    c.setStrokeColor(color); c.setLineWidth(1.6)
    c.line(cx - size*0.3, cy - size*0.3, cx + size*0.3, cy + size*0.3)
    c.line(cx - size*0.3, cy + size*0.3, cx + size*0.3, cy - size*0.3)


def _draw_label_handwritten(c, cx, cy, w=1.6*cm, h=0.8*cm):
    """Paper write-on label with crossed-out phone number."""
    c.setFillColor(SAND); c.setStrokeColor(GREY); c.setLineWidth(0.3)
    c.rect(cx - w/2, cy - h/2, w, h, fill=1, stroke=1)
    # punched hole
    c.setFillColor(WHITE)
    c.circle(cx - w/2 + 0.12*cm, cy + h/2 - 0.12*cm, 0.06*cm, fill=1, stroke=0)
    # squiggly handwritten phone number
    c.setFillColor(INK); c.setFont("Helvetica", 5)
    c.drawCentredString(cx, cy + 0.08*cm, "+1 (555) 0123-")
    c.drawCentredString(cx, cy - 0.10*cm, "Jane Doe")
    # red line through it
    c.setStrokeColor(RED_X); c.setLineWidth(1.0)
    c.line(cx - w*0.35, cy - h*0.1, cx + w*0.35, cy + h*0.15)


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
        c.setFillColor(NAVY); c.rect(0, s - 0.7*cm, 1.7*cm, 0.7*cm, fill=1, stroke=0)
        c.setFillColor(YELLOW); c.setFont("Helvetica-Bold", 11)
        c.drawCentredString(0.85*cm, s - 0.5*cm, f"OPT {self.letter}")
        self.draw_fn(c, s/2, s/2 - 0.3*cm)
        c.setFillColor(GREY); c.setFont("Helvetica", 7)
        c.drawCentredString(s/2, 0.15*cm, "2000 × 2000 px · pure white (Amazon)")
        c.setFillColor(TEAL)
        tw = c.stringWidth(self.name.upper(), "Helvetica-Bold", 7) + 0.4*cm
        c.rect(s - tw, 0, tw, 0.5*cm, fill=1, stroke=0)
        c.setFillColor(WHITE); c.setFont("Helvetica-Bold", 7)
        c.drawString(s - tw + 0.2*cm, 0.18*cm, self.name.upper())


class ListingMockup(Flowable):
    def __init__(self, slot, role, draw_fn, bg=WHITE, side_w=8.5*cm):
        self.slot = slot; self.role = role; self.draw_fn = draw_fn; self.bg = bg
        self.size = 6.5*cm; self.side_w = side_w; self.gap = 0.4*cm
        Flowable.__init__(self)
    def wrap(self, *a): return (self.size + self.gap + self.side_w, self.size + 0.4*cm)
    def draw(self):
        c = self.canv; s = self.size
        c.setFillColor(self.bg); c.setStrokeColor(HexColor("#CCCCCC")); c.setLineWidth(0.4)
        c.rect(0, 0, s, s, fill=1, stroke=1)
        c.setFillColor(NAVY); c.rect(0, s - 0.7*cm, 1.4*cm, 0.7*cm, fill=1, stroke=0)
        c.setFillColor(YELLOW); c.setFont("Helvetica-Bold", 11)
        c.drawCentredString(0.7*cm, s - 0.5*cm, f"#{self.slot}")
        self.draw_fn(c, s/2, s/2)
        c.setFillColor(TEAL)
        tw = c.stringWidth(self.role.upper(), "Helvetica-Bold", 7) + 0.4*cm
        c.rect(s - tw, 0, tw, 0.5*cm, fill=1, stroke=0)
        c.setFillColor(WHITE); c.setFont("Helvetica-Bold", 7)
        c.drawString(s - tw + 0.2*cm, 0.18*cm, self.role.upper())
        c.setFillColor(GREY if self.bg in (WHITE, SAND, LIGHT, YELLOW) else WHITE)
        c.setFont("Helvetica", 6.5)
        c.drawCentredString(s/2, 0.15*cm, "2000 × 2000 px")


class APlusMockup(Flowable):
    def __init__(self, slot, mtype, draw_fn, bg=SAND, side_w=7.0*cm):
        self.slot = slot; self.mtype = mtype; self.draw_fn = draw_fn; self.bg = bg
        self.bw = 10.0*cm; self.bh = self.bw * (600/1464)
        self.side_w = side_w; self.gap = 0.4*cm
        Flowable.__init__(self)
    def wrap(self, *a): return (self.bw + self.gap + self.side_w, self.bh + 0.5*cm)
    def draw(self):
        c = self.canv; w, h = self.bw, self.bh
        c.setFillColor(self.bg); c.setStrokeColor(HexColor("#CCCCCC")); c.setLineWidth(0.4)
        c.rect(0, 0.5*cm, w, h, fill=1, stroke=1)
        c.setFillColor(NAVY); c.rect(0, 0.5*cm + h - 0.55*cm, 2.4*cm, 0.55*cm, fill=1, stroke=0)
        c.setFillColor(WHITE); c.setFont("Helvetica-Bold", 8)
        c.drawString(0.15*cm, 0.5*cm + h - 0.4*cm, f"MODULE {self.slot}")
        self.draw_fn(c, w/2, 0.5*cm + h/2)
        c.setFillColor(TEAL)
        tw = c.stringWidth(self.mtype.upper(), "Helvetica-Bold", 7) + 0.3*cm
        c.rect(w - tw, 0.5*cm, tw, 0.4*cm, fill=1, stroke=0)
        c.setFillColor(WHITE); c.setFont("Helvetica-Bold", 7)
        c.drawString(w - tw + 0.15*cm, 0.5*cm + 0.13*cm, self.mtype.upper())
        c.setFillColor(GREY); c.setFont("Helvetica", 6.5)
        c.drawCentredString(w/2, 0.15*cm, "1464 × 600 desktop · 600 × 450 mobile")


class MoodTile(Flowable):
    def __init__(self, title, sub, draw_fn, w=5.0*cm, h=3.6*cm, bg=SAND):
        self.title = title; self.sub = sub; self.draw_fn = draw_fn
        self.w = w; self.h = h; self.bg = bg
        Flowable.__init__(self)
    def wrap(self, *a): return (self.w, self.h)
    def draw(self):
        c = self.canv; w, h = self.w, self.h
        c.setFillColor(self.bg); c.setStrokeColor(HexColor("#CCCCCC")); c.setLineWidth(0.4)
        c.rect(0, 0, w, h, fill=1, stroke=1)
        self.draw_fn(c, w/2, h/2 + 0.2*cm)
        c.setFillColor(NAVY); c.rect(0, 0, w, 0.5*cm, fill=1, stroke=0)
        c.setFillColor(YELLOW); c.setFont("Helvetica-Bold", 7.5)
        c.drawString(0.2*cm, 0.18*cm, self.title.upper())
        c.setFillColor(WHITE); c.setFont("Helvetica", 6.5)
        c.drawRightString(w - 0.2*cm, 0.18*cm, self.sub)


# ─── Concept drawings ────────────────────────────────────────────────

def cpt_main_a(c, cx, cy):
    """Pack hero — two tags side-by-side."""
    _draw_tag(c, cx - 1.4*cm, cy, w=2.0*cm, h=2.8*cm, color=TEAL, with_loop=True)
    _draw_tag(c, cx + 1.4*cm, cy, w=2.0*cm, h=2.8*cm, color=PINK,  with_loop=True)
    c.setFillColor(GREY); c.setFont("Helvetica-Bold", 6.5)
    c.drawCentredString(cx, cy - 2.1*cm, "2-PACK · Teal + Pink")


def cpt_main_b(c, cx, cy):
    """In-use: tag attached to a suitcase."""
    _draw_suitcase(c, cx + 0.3*cm, cy - 0.2*cm, w=3.4*cm, h=2.6*cm, color=LUG_BR)
    # tag dangling on the handle (left)
    _draw_tag(c, cx - 1.8*cm, cy + 0.5*cm, w=1.4*cm, h=2.0*cm, color=TEAL, with_loop=True)
    # connector arrow
    c.setStrokeColor(TEAL); c.setLineWidth(1.0)
    c.line(cx - 1.05*cm, cy + 0.7*cm, cx - 0.3*cm, cy + 1.2*cm)


def cpt_main_c(c, cx, cy):
    """Tag + phone scanning."""
    _draw_tag(c, cx - 1.0*cm, cy + 0.1*cm, w=1.9*cm, h=2.7*cm, color=TEAL, with_loop=True)
    _draw_phone(c, cx + 1.3*cm, cy + 0.1*cm, w=1.4*cm, h=2.6*cm, scanning=True)
    # subtle scan beam
    c.setStrokeColor(Color(TEAL.red, TEAL.green, TEAL.blue, alpha=0.4))
    c.setLineWidth(0.6)
    c.line(cx - 0.1*cm, cy + 0.5*cm, cx + 0.8*cm, cy + 0.4*cm)


def cpt_img2(c, cx, cy):
    """Privacy hook — write-on label vs SeQR tag."""
    # title bar
    c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(cx, cy + 2.4*cm, "DON'T PUT YOUR NUMBER")
    c.drawCentredString(cx, cy + 2.0*cm, "ON A LUGGAGE TAG.")
    # LEFT: paper write-on label desaturated, red ✕
    _draw_label_handwritten(c, cx - 1.5*cm, cy + 0.2*cm, w=2.0*cm, h=1.2*cm)
    _draw_x(c, cx - 1.5*cm, cy - 1.0*cm, size=0.6*cm)
    # vs divider
    c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 9)
    c.drawCentredString(cx, cy + 0.2*cm, "vs")
    # RIGHT: SeQR tag, green ✓
    _draw_tag(c, cx + 1.5*cm, cy + 0.2*cm, w=1.4*cm, h=1.8*cm, color=TEAL, with_loop=False)
    _draw_check(c, cx + 1.5*cm, cy - 1.0*cm, size=0.6*cm)
    # bottom
    c.setFillColor(GREY); c.setFont("Helvetica", 6.5)
    c.drawCentredString(cx, cy - 1.9*cm, "Reachable when it counts. Private the rest of the time.")


def cpt_img3(c, cx, cy):
    """3 steps: Stick → Scan → Message."""
    c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(cx, cy + 2.4*cm, "STICK · SCAN · MESSAGE.")
    panels = [
        (cx - 2.0*cm, "1", "Attach"),
        (cx,          "2", "Finder scans"),
        (cx + 2.0*cm, "3", "Message you"),
    ]
    for x, num, lbl in panels:
        # circle number
        c.setFillColor(TEAL); c.circle(x, cy + 1.2*cm, 0.32*cm, fill=1, stroke=0)
        c.setFillColor(WHITE); c.setFont("Helvetica-Bold", 9)
        c.drawCentredString(x, cy + 1.1*cm, num)
        # mini illustration per panel
        if num == "1":
            _draw_suitcase(c, x, cy - 0.2*cm, w=1.6*cm, h=1.2*cm)
            _draw_tag(c, x - 0.7*cm, cy + 0.3*cm, w=0.55*cm, h=0.8*cm, color=TEAL, with_loop=False)
        elif num == "2":
            _draw_tag(c, x - 0.5*cm, cy - 0.2*cm, w=0.7*cm, h=1.0*cm, color=TEAL, with_loop=False)
            _draw_phone(c, x + 0.6*cm, cy - 0.2*cm, w=0.7*cm, h=1.2*cm, scanning=True)
        else:
            _draw_phone(c, x, cy - 0.2*cm, w=0.8*cm, h=1.3*cm, scanning=False)
        c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 6.5)
        c.drawCentredString(x, cy - 1.3*cm, lbl.upper())
    # bottom strap
    c.setFillColor(GREY); c.setFont("Helvetica", 6.5)
    c.drawCentredString(cx, cy - 2.0*cm, "Works on any phone. No app required for finders.")


def cpt_img4(c, cx, cy):
    """Versatility — 2-pack tags on multiple travel items."""
    c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(cx, cy + 2.4*cm, "ONE PACK · EVERYTHING YOU TRAVEL WITH.")
    # central pack
    _draw_tag(c, cx - 0.4*cm, cy + 0.2*cm, w=1.0*cm, h=1.4*cm, color=TEAL, with_loop=False)
    _draw_tag(c, cx + 0.4*cm, cy + 0.2*cm, w=1.0*cm, h=1.4*cm, color=PINK, with_loop=False)
    # surrounding items: suitcase, backpack, gym bag, briefcase
    _draw_suitcase(c, cx - 2.2*cm, cy + 1.0*cm, w=1.4*cm, h=1.0*cm, color=LUG_BR)
    _draw_suitcase(c, cx + 2.2*cm, cy + 1.0*cm, w=1.4*cm, h=1.0*cm, color=LUG_BG)
    # backpack silhouette (rounded square)
    c.setFillColor(HexColor("#5A6E80")); c.setStrokeColor(NAVY); c.setLineWidth(0.4)
    c.roundRect(cx - 2.8*cm, cy - 1.3*cm, 1.4*cm, 1.0*cm, 0.2*cm, fill=1, stroke=1)
    c.setFillColor(GREY); c.setFont("Helvetica", 5); c.drawCentredString(cx - 2.1*cm, cy - 1.5*cm, "BACKPACK")
    # briefcase
    c.setFillColor(HexColor("#3E2C1E")); c.setStrokeColor(NAVY); c.setLineWidth(0.4)
    c.roundRect(cx + 1.6*cm, cy - 1.3*cm, 1.4*cm, 0.9*cm, 0.06*cm, fill=1, stroke=1)
    c.setStrokeColor(NAVY); c.setLineWidth(0.5)
    c.line(cx + 2.05*cm, cy - 0.55*cm, cx + 2.25*cm, cy - 0.45*cm)
    c.setFillColor(GREY); c.setFont("Helvetica", 5); c.drawCentredString(cx + 2.3*cm, cy - 1.5*cm, "CARRY-ON")
    c.setFillColor(GREY); c.setFont("Helvetica-Bold", 6)
    c.drawCentredString(cx, cy - 2.0*cm, "Suitcase · Carry-on · Backpack · Briefcase")


def cpt_img5(c, cx, cy):
    """Durability — water + tough + sun icons."""
    c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(cx, cy + 2.4*cm, "BUILT FOR REAL TRAVEL.")
    # center tag
    _draw_tag(c, cx, cy, w=1.6*cm, h=2.2*cm, color=TEAL, with_loop=False)
    # 4 quadrants with icons
    quads = [(-2.0*cm, 1.5*cm, "WATERPROOF"),
             (2.0*cm, 1.5*cm, "TEAR-RESISTANT"),
             (-2.0*cm, -1.3*cm, "UV-STABLE"),
             (2.0*cm, -1.3*cm, "GLOBAL")]
    for dx, dy, lbl in quads:
        c.setFillColor(SAND); c.setStrokeColor(TEAL); c.setLineWidth(0.5)
        c.circle(cx + dx, cy + dy, 0.42*cm, fill=1, stroke=1)
        # icon hint
        if "WATER" in lbl:
            _draw_water_drops(c, cx + dx, cy + dy, count=3)
        elif "TEAR" in lbl:
            c.setStrokeColor(NAVY); c.setLineWidth(0.8)
            c.line(cx + dx - 0.15*cm, cy + dy - 0.10*cm, cx + dx + 0.15*cm, cy + dy + 0.10*cm)
            c.line(cx + dx - 0.15*cm, cy + dy + 0.10*cm, cx + dx + 0.15*cm, cy + dy - 0.10*cm)
        elif "UV" in lbl:
            c.setFillColor(YELLOW); c.circle(cx + dx, cy + dy, 0.18*cm, fill=1, stroke=0)
            c.setStrokeColor(YELLOW); c.setLineWidth(0.6)
            for ang in range(0, 360, 45):
                rad = math.radians(ang)
                c.line(cx + dx + 0.22*cm*math.cos(rad), cy + dy + 0.22*cm*math.sin(rad),
                       cx + dx + 0.32*cm*math.cos(rad), cy + dy + 0.32*cm*math.sin(rad))
        else:  # GLOBAL
            c.setFillColor(TEAL); c.circle(cx + dx, cy + dy, 0.16*cm, fill=1, stroke=0)
            c.setStrokeColor(WHITE); c.setLineWidth(0.4)
            c.line(cx + dx - 0.16*cm, cy + dy, cx + dx + 0.16*cm, cy + dy)
            c.line(cx + dx, cy + dy - 0.16*cm, cx + dx, cy + dy + 0.16*cm)
            c.ellipse(cx + dx - 0.08*cm, cy + dy - 0.16*cm, cx + dx + 0.08*cm, cy + dy + 0.16*cm, fill=0, stroke=1)
        c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 5.5)
        c.drawCentredString(cx + dx, cy + dy - 0.65*cm, lbl)


def cpt_img6(c, cx, cy):
    """Customize + 2-pack — write any details on either tag."""
    c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(cx, cy + 2.4*cm, "TWO TAGS. ANY DETAILS. ANY TIME.")
    # two phone screens showing custom message setup
    _draw_phone(c, cx - 1.4*cm, cy + 0.1*cm, w=1.5*cm, h=2.4*cm, scanning=False)
    _draw_phone(c, cx + 1.4*cm, cy + 0.1*cm, w=1.5*cm, h=2.4*cm, scanning=False)
    # labels
    c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 6)
    c.drawCentredString(cx - 1.4*cm, cy - 1.5*cm, "TAG 1 · Suitcase")
    c.drawCentredString(cx + 1.4*cm, cy - 1.5*cm, "TAG 2 · Carry-on")
    # arrow between phones
    c.setStrokeColor(PINK); c.setLineWidth(1.0)
    c.line(cx - 0.4*cm, cy + 0.1*cm, cx + 0.4*cm, cy + 0.1*cm)
    c.setFillColor(GREY); c.setFont("Helvetica", 6.5)
    c.drawCentredString(cx, cy - 2.0*cm, "Different message per tag. Edit anytime.")


def _draw_benefit_icon(c, cx, cy, kind, size=0.42*cm):
    """One small icon for the benefits frame."""
    if kind == "privacy":
        # padlock
        c.setFillColor(NAVY); c.roundRect(cx - size*0.5, cy - size*0.45, size, size*0.7, size*0.06, fill=1, stroke=0)
        c.setStrokeColor(NAVY); c.setLineWidth(0.9)
        c.arc(cx - size*0.3, cy + size*0.05, cx + size*0.3, cy + size*0.55, startAng=0, extent=180)
        c.setFillColor(YELLOW); c.circle(cx, cy - size*0.1, size*0.08, fill=1, stroke=0)
    elif kind == "no_fee":
        # dollar with slash
        c.setFillColor(TEAL); c.circle(cx, cy, size*0.45, fill=1, stroke=0)
        c.setFillColor(WHITE); c.setFont("Helvetica-Bold", size*22)
        c.drawCentredString(cx, cy - size*0.15, "$")
        c.setStrokeColor(RED_X); c.setLineWidth(1.4)
        c.line(cx - size*0.5, cy - size*0.5, cx + size*0.5, cy + size*0.5)
    elif kind == "no_app":
        # phone with X
        c.setFillColor(NAVY); c.roundRect(cx - size*0.25, cy - size*0.45, size*0.5, size*0.9, size*0.05, fill=1, stroke=0)
        c.setFillColor(WHITE); c.roundRect(cx - size*0.20, cy - size*0.35, size*0.4, size*0.65, size*0.03, fill=1, stroke=0)
        c.setStrokeColor(RED_X); c.setLineWidth(1.2)
        c.line(cx - size*0.20, cy - size*0.25, cx + size*0.20, cy + size*0.25)
        c.line(cx - size*0.20, cy + size*0.25, cx + size*0.20, cy - size*0.25)
    elif kind == "no_battery":
        # battery icon
        c.setStrokeColor(NAVY); c.setLineWidth(0.8); c.setFillColor(WHITE)
        c.roundRect(cx - size*0.45, cy - size*0.25, size*0.85, size*0.5, size*0.04, fill=1, stroke=1)
        c.setFillColor(NAVY); c.rect(cx + size*0.40, cy - size*0.12, size*0.08, size*0.24, fill=1, stroke=0)
        c.setStrokeColor(RED_X); c.setLineWidth(1.2)
        c.line(cx - size*0.40, cy - size*0.30, cx + size*0.40, cy + size*0.30)
    elif kind == "world":
        # globe + map pin
        c.setStrokeColor(TEAL); c.setLineWidth(0.8); c.setFillColor(WHITE)
        c.circle(cx, cy, size*0.45, fill=1, stroke=1)
        c.setStrokeColor(TEAL); c.setLineWidth(0.5)
        c.line(cx - size*0.45, cy, cx + size*0.45, cy)
        c.ellipse(cx - size*0.20, cy - size*0.45, cx + size*0.20, cy + size*0.45, fill=0, stroke=1)
        c.setFillColor(PINK); c.circle(cx + size*0.18, cy - size*0.10, size*0.10, fill=1, stroke=0)


def cpt_img4_benefits(c, cx, cy):
    """Key Benefits — 5 icon badges around the SeQR tag. Promoted to slot #4."""
    # title
    c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(cx, cy + 2.4*cm, "5 REASONS SeQR")
    c.setFillColor(GREY); c.setFont("Helvetica", 7)
    c.drawCentredString(cx, cy + 2.05*cm, "What you get with every pack")
    # center tag (smaller — badges are the hero)
    _draw_tag(c, cx, cy - 0.2*cm, w=1.2*cm, h=1.7*cm, color=TEAL, with_loop=False)
    # 5 badges around the tag (pentagon arrangement)
    badges = [
        ( -2.2*cm,  1.3*cm, "privacy",    "PRIVATE\nMESSAGING",    "Phone & email hidden"),
        (  2.2*cm,  1.3*cm, "no_fee",     "NO FEES\nFOREVER",      "No subscription"),
        ( -2.4*cm, -0.4*cm, "no_app",     "NO APP\nFOR FINDERS",   "Any phone, any country"),
        (  2.4*cm, -0.4*cm, "no_battery", "NO BATTERY\nEVER",      "Passive tag, works decades"),
        (  0,      -1.9*cm, "world",      "OPTIONAL\nLOCATION",    "Finder attaches map link"),
    ]
    for dx, dy, kind, label, sub in badges:
        # badge bg
        c.setFillColor(WHITE); c.setStrokeColor(TEAL); c.setLineWidth(0.6)
        c.roundRect(cx + dx - 0.95*cm, cy + dy - 0.45*cm, 1.9*cm, 0.9*cm, 0.10*cm, fill=1, stroke=1)
        # icon (left)
        _draw_benefit_icon(c, cx + dx - 0.65*cm, cy + dy, kind)
        # label (right)
        c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 5.5)
        lines = label.split("\n")
        for i, ln in enumerate(lines):
            c.drawString(cx + dx - 0.25*cm, cy + dy + 0.18*cm - i*0.18*cm, ln)
        c.setFillColor(GREY); c.setFont("Helvetica", 4.5)
        c.drawString(cx + dx - 0.25*cm, cy + dy - 0.30*cm, sub)


def cpt_img7(c, cx, cy):
    """Brand close — emotional close, tag + Scan to try + signature line."""
    # serif-ish closing headline
    c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(cx, cy + 2.4*cm, "REACHABLE. PRIVATE. FREE.")
    # central tag (larger now — emotional hero)
    _draw_tag(c, cx + 0.4*cm, cy + 0.2*cm, w=2.0*cm, h=2.8*cm, color=TEAL, with_loop=True)
    # handwritten pink "Scan to try!" CTA with arrow pointing to tag
    c.saveState()
    c.translate(cx - 2.0*cm, cy + 1.0*cm)
    c.rotate(-8)
    c.setFillColor(PINK); c.setFont("Helvetica-BoldOblique", 11)
    c.drawString(0, 0, "Scan to try!")
    c.restoreState()
    # curvy arrow pink, towards the tag
    c.setStrokeColor(PINK); c.setLineWidth(1.3)
    c.bezier(cx - 1.2*cm, cy + 0.9*cm, cx - 0.7*cm, cy + 0.4*cm,
             cx - 0.5*cm, cy + 0.7*cm, cx - 0.2*cm, cy + 0.5*cm)
    # arrowhead
    c.setFillColor(PINK)
    p = c.beginPath()
    p.moveTo(cx - 0.18*cm, cy + 0.48*cm); p.lineTo(cx - 0.32*cm, cy + 0.62*cm); p.lineTo(cx - 0.30*cm, cy + 0.40*cm); p.close()
    c.drawPath(p, fill=1, stroke=0)
    # signature line
    c.setFillColor(GREY); c.setFont("Helvetica-Oblique", 6.5)
    c.drawCentredString(cx, cy - 1.7*cm, "Be findable by the people who want to help you.")
    c.setFillColor(GREY); c.setFont("Helvetica-Oblique", 6)
    c.drawCentredString(cx, cy - 2.0*cm, "Without being findable by everyone else.")


# ─── A+ concept drawings ─────────────────────────────────────────────

def cpt_aplus1(c, cx, cy):
    """Heritage banner — pack on luggage."""
    _draw_suitcase(c, cx + 2.0*cm, cy - 0.2*cm, w=3.0*cm, h=2.2*cm, color=LUG_BR)
    _draw_tag(c, cx - 2.5*cm, cy + 0.5*cm, w=1.4*cm, h=2.0*cm, color=TEAL, with_loop=True)
    c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 13)
    c.drawCentredString(cx - 0.5*cm, cy + 0.6*cm, "BE FINDABLE")
    c.setFillColor(NAVY); c.setFont("Helvetica", 8)
    c.drawCentredString(cx - 0.5*cm, cy + 0.0*cm, "by the people who want to help you.")
    c.setFillColor(GREY); c.setFont("Helvetica-Oblique", 7)
    c.drawCentredString(cx - 0.5*cm, cy - 0.4*cm, "Without being findable by everyone else.")


def cpt_aplus_carousel(c, cx, cy):
    """5 USP tiles."""
    for i in range(5):
        x = cx - 2.2*cm + i*1.1*cm
        c.setFillColor(WHITE); c.setStrokeColor(TEAL); c.setLineWidth(0.5)
        c.roundRect(x - 0.5*cm, cy - 0.5*cm, 1.0*cm, 1.0*cm, 0.06*cm, fill=1, stroke=1)
        c.setFillColor(TEAL); c.setFont("Helvetica-Bold", 8)
        c.drawCentredString(x, cy + 0.1*cm, str(i+1))
    c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 8)
    c.drawCentredString(cx, cy + 1.1*cm, "5 REASONS SeQR")
    c.setFillColor(GREY); c.setFont("Helvetica", 6.5)
    c.drawCentredString(cx, cy - 0.9*cm, "Privacy · No app · No battery · No fee · Customize")


def cpt_aplus3(c, cx, cy):
    """3 steps wide banner."""
    for i, lbl in enumerate(["1 Stick", "2 Scan", "3 Message"]):
        x = cx - 3.0*cm + i*3.0*cm
        c.setFillColor(TEAL); c.circle(x, cy + 0.5*cm, 0.3*cm, fill=1, stroke=0)
        c.setFillColor(WHITE); c.setFont("Helvetica-Bold", 8)
        c.drawCentredString(x, cy + 0.4*cm, lbl[0])
        c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 8)
        c.drawCentredString(x, cy - 0.1*cm, lbl[1:].strip().upper())
    c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 9)
    c.drawCentredString(cx, cy + 1.1*cm, "HOW SeQR WORKS")


def cpt_aplus4(c, cx, cy):
    """Lifestyle hero — wide travel scene."""
    _draw_suitcase(c, cx - 2.5*cm, cy - 0.2*cm, w=1.8*cm, h=1.3*cm, color=LUG_BR)
    _draw_suitcase(c, cx + 2.4*cm, cy - 0.2*cm, w=1.8*cm, h=1.3*cm, color=LUG_BG)
    _draw_tag(c, cx, cy + 0.2*cm, w=1.2*cm, h=1.7*cm, color=TEAL, with_loop=True)
    c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(cx, cy + 1.2*cm, "ONE PACK · EVERY TRIP")


def cpt_aplus_uses(c, cx, cy):
    """Use-case carousel."""
    labels = ["SUITCASE", "BACKPACK", "CARRY-ON", "DUFFEL", "GYM BAG"]
    for i, lbl in enumerate(labels):
        x = cx - 2.2*cm + i*1.1*cm
        c.setFillColor(LUG_BR); c.setStrokeColor(NAVY); c.setLineWidth(0.4)
        c.roundRect(x - 0.4*cm, cy - 0.45*cm, 0.8*cm, 0.9*cm, 0.05*cm, fill=1, stroke=1)
        c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 5.5)
        c.drawCentredString(x, cy - 0.75*cm, lbl)


def cpt_aplus_qa(c, cx, cy):
    """Q&A list."""
    c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(cx, cy + 0.9*cm, "FREQUENTLY ASKED")
    for i, q in enumerate([
        "Does it track in real time?",
        "Is it really free?",
        "Does the finder need an app?",
        "Is it waterproof?",
        "How do I activate 2 tags?",
    ]):
        c.setFillColor(NAVY); c.setFont("Helvetica", 6.5)
        c.drawCentredString(cx, cy + 0.3*cm - i*0.20*cm, "· " + q)


def cpt_aplus_compare(c, cx, cy):
    """Comparison chart."""
    cols = ["SeQR", "Write-on", "Engraved", "AirTag", "Generic QR"]
    w = 1.7*cm
    for i, col in enumerate(cols):
        x = cx - 4.3*cm + i*w
        c.setFillColor(TEAL if i == 0 else WHITE); c.setStrokeColor(NAVY); c.setLineWidth(0.4)
        c.rect(x, cy - 0.8*cm, w - 0.05*cm, 1.4*cm, fill=1, stroke=1)
        if i == 0:
            _draw_tag(c, x + w/2, cy + 0.1*cm, w=0.7*cm, h=1.0*cm, color=NAVY, with_loop=False)
        else:
            c.setFillColor(GREY); c.setFont("Helvetica", 5.5)
            c.drawCentredString(x + w/2, cy + 0.1*cm, "—")
        c.setFillColor(WHITE if i == 0 else NAVY); c.setFont("Helvetica-Bold", 5.5)
        c.drawCentredString(x + w/2, cy - 0.55*cm, col)


# ─── Moodboard tile drawings ─────────────────────────────────────────

def md_airport(c, cx, cy):
    """Airport scene — wave of suitcases."""
    for i, col in enumerate([LUG_BR, LUG_BG, LUG_BR, LUG_BG]):
        _draw_suitcase(c, cx - 1.5*cm + i*1.0*cm, cy - 0.4*cm + (i%2)*0.2*cm, w=0.9*cm, h=0.7*cm, color=col)

def md_qr(c, cx, cy):
    """Large QR + small tag."""
    _draw_qr(c, cx, cy + 0.3*cm, size=1.8*cm, color=NAVY, bg=WHITE)
    _draw_tag(c, cx, cy - 1.0*cm, w=1.2*cm, h=0.6*cm, color=TEAL, with_qr=False, with_loop=False, label="SeQR")

def md_handheld(c, cx, cy):
    """Hand holding tag."""
    # hand silhouette
    c.setFillColor(HexColor("#E8B89C"))
    c.roundRect(cx - 0.4*cm, cy - 1.0*cm, 0.8*cm, 1.2*cm, 0.1*cm, fill=1, stroke=0)
    # fingers
    for fx in [-0.25*cm, -0.05*cm, 0.15*cm, 0.35*cm]:
        c.roundRect(cx + fx, cy - 0.2*cm, 0.12*cm, 0.6*cm, 0.05*cm, fill=1, stroke=0)
    # tag held
    _draw_tag(c, cx, cy + 0.5*cm, w=1.0*cm, h=1.4*cm, color=TEAL, with_loop=False)

def md_water(c, cx, cy):
    """Tag in water spray."""
    _draw_water_drops(c, cx, cy + 0.4*cm, count=10)
    _draw_tag(c, cx, cy - 0.3*cm, w=1.2*cm, h=1.6*cm, color=TEAL, with_loop=False)

def md_privacy(c, cx, cy):
    """Privacy lock + crossed-out phone."""
    # padlock
    c.setFillColor(NAVY); c.setStrokeColor(NAVY); c.setLineWidth(0.5)
    c.roundRect(cx - 0.5*cm, cy - 0.5*cm, 1.0*cm, 0.8*cm, 0.05*cm, fill=1, stroke=1)
    c.setFillColor(YELLOW); c.circle(cx, cy - 0.1*cm, 0.10*cm, fill=1, stroke=0)
    c.setStrokeColor(NAVY); c.setLineWidth(0.8)
    c.arc(cx - 0.3*cm, cy + 0.3*cm, cx + 0.3*cm, cy + 0.9*cm, startAng=0, extent=180)
    # crossed phone number
    c.setFillColor(GREY); c.setFont("Helvetica", 6)
    c.drawCentredString(cx, cy - 1.1*cm, "+1 555-0123")
    c.setStrokeColor(RED_X); c.setLineWidth(1.0)
    c.line(cx - 0.8*cm, cy - 1.05*cm, cx + 0.8*cm, cy - 0.95*cm)

def md_palette(c, cx, cy):
    """Brand color swatches."""
    cols = [TEAL, NAVY, PINK, YELLOW, SAND]
    for i, col in enumerate(cols):
        x = cx - 1.6*cm + i*0.8*cm
        c.setFillColor(col); c.setStrokeColor(HexColor("#CCCCCC")); c.setLineWidth(0.3)
        c.rect(x - 0.32*cm, cy - 0.4*cm, 0.65*cm, 0.9*cm, fill=1, stroke=1)


# ─── Page chrome ─────────────────────────────────────────────────────

def cover_page(canvas, doc):
    canvas.saveState()
    # SAND background
    canvas.setFillColor(SAND); canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    # Top teal band
    canvas.setFillColor(TEAL); canvas.rect(0, PAGE_H - 4*cm, PAGE_W, 4*cm, fill=1, stroke=0)
    canvas.setFillColor(NAVY); canvas.rect(0, PAGE_H - 4.4*cm, PAGE_W, 0.4*cm, fill=1, stroke=0)
    canvas.setFillColor(WHITE); canvas.setFont("Helvetica-Bold", 38)
    canvas.drawString(ML, PAGE_H - 2.6*cm, "SeQR")
    canvas.setFont("Helvetica", 16); canvas.setFillColor(WHITE)
    canvas.drawString(ML, PAGE_H - 3.4*cm, "Smart Luggage Tags · 2-Pack · QR-Code Travel ID")
    canvas.setFillColor(NAVY); canvas.setFont("Helvetica-Bold", 22)
    canvas.drawString(ML, PAGE_H - 7*cm, "Amazon US Image Plan")
    canvas.setFillColor(GREY); canvas.setFont("Helvetica", 13)
    canvas.drawString(ML, PAGE_H - 7.8*cm, "3 Main Image Options · 7 Listing Images · A+ Premium · Master Copy")

    # Meta row
    y = 5.0*cm
    fields = [("ASIN", "B0DY1L5RPM"), ("CATEGORY", "QR Luggage Tags"), ("PACK", "2 tags · 1 metal loop"), ("DATE", "2026-05-16")]
    for i, (k, v) in enumerate(fields):
        x = ML + i * 4.4*cm
        canvas.setFillColor(NAVY); canvas.setFont("Helvetica-Bold", 8)
        canvas.drawString(x, y, k)
        canvas.setFillColor(INK); canvas.setFont("Helvetica", 11)
        canvas.drawString(x, y - 0.55*cm, v)

    # Sample tags — fill the middle cream space, well clear of the meta row
    _draw_tag(canvas, PAGE_W - MR - 5.5*cm, PAGE_H - 12.5*cm, w=3.4*cm, h=4.8*cm, color=TEAL, with_loop=True)
    _draw_tag(canvas, PAGE_W - MR - 2.0*cm, PAGE_H - 13.0*cm, w=3.4*cm, h=4.8*cm, color=PINK, with_loop=True)
    # Tagline near the tags
    canvas.setFillColor(GREY); canvas.setFont("Helvetica-Oblique", 10)
    canvas.drawString(ML, PAGE_H - 14.5*cm, "Two tags. Any details. Any time.")

    # Bottom strap
    canvas.setFillColor(NAVY); canvas.rect(0, 0, PAGE_W, 1.4*cm, fill=1, stroke=0)
    canvas.setFillColor(TEAL); canvas.setFont("Helvetica-Bold", 10)
    canvas.drawString(ML, 0.5*cm, "BE FINDABLE BY THE PEOPLE WHO WANT TO HELP YOU.")
    canvas.setFillColor(WHITE); canvas.setFont("Helvetica", 9)
    canvas.drawRightString(PAGE_W - MR, 0.5*cm, "Prepared by EQUALICE")
    canvas.restoreState()


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(TEAL); canvas.setLineWidth(2.5)
    canvas.line(ML, PAGE_H - 1.0*cm, PAGE_W - MR, PAGE_H - 1.0*cm)
    canvas.setFillColor(NAVY); canvas.setFont("Helvetica-Bold", 9)
    canvas.drawString(ML, PAGE_H - 0.7*cm, "SeQR Contact")
    canvas.setFillColor(GREY); canvas.setFont("Helvetica", 8)
    canvas.drawString(ML + 1.9*cm, PAGE_H - 0.7*cm, "Smart Luggage Tags (2-Pack QR) · Amazon US Brief")
    canvas.setFillColor(GREY); canvas.setFont("Helvetica", 8)
    canvas.drawRightString(PAGE_W - MR, PAGE_H - 0.7*cm, f"Page {doc.page}")
    canvas.setStrokeColor(HexColor("#E0DCC8")); canvas.setLineWidth(0.4)
    canvas.line(ML, MB - 0.4*cm, PAGE_W - MR, MB - 0.4*cm)
    canvas.setFillColor(GREY); canvas.setFont("Helvetica", 7.5)
    canvas.drawString(ML, MB - 0.7*cm, "Prepared by EQUALICE — 2026-05-16 · ASIN B0DY1L5RPM")
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
                          title="SeQR Smart Luggage Tags — Image Plan",
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

    # ───── At a glance ─────
    s.append(Paragraph("At a glance", H2)); s.append(HRule())
    glance = [
        ["Brand", "SeQR Contact — privacy-first QR contact tags & labels."],
        ["Product", "Smart Luggage Tags — 2-pack QR-code luggage IDs with reinforced acrylic/metal loop. Waterproof, durable, no app for finders."],
        ["ASIN", "B0DY1L5RPM · amazon.com"],
        ["Use case", "Frequent business + leisure travel; family travel; backpacks, suitcases, carry-ons, gym bags, instrument cases. Finder scans QR → messages the owner via SeQR without exposing phone/email/address."],
        ["Hero buyer trigger", '"My checked bag got lost in Frankfurt and the airline could not reach me. The handwritten name tag had nothing useful and exposed too much."'],
        ["Top competitors (Excel)", "Dynotag · Retag · Cloud-Tag · ReboundTag · iTag · Lucid Tag · generic-QR multi-packs"],
        ["Top keywords (US, SV)", "luggage tags for suitcases tsa approved (6020) · luggage identifiers for suitcases (2534) · smart luggage tags (1676) · baggage tags for air travel (1617) · itag (1617) · lucid tag (1170) · luggage tags 3 pack (539)"],
        ["Brand voice", 'Warm + practical + plainspoken. "We\'ve got you" — not "submit a ticket". Numbered steps for instructions. Honest about limits.'],
    ]
    t = Table([[Paragraph(f"<b>{k}</b>", BODY), Paragraph(v, BODY)] for k, v in glance],
              colWidths=[3.8*cm, CW - 3.8*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,-1), SAND),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LINEBELOW", (0,0), (-1,-1), 0.3, HexColor("#E0DCC8")),
        ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 6), ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ]))
    s.append(t)

    # ───── Compliance warning ─────
    s.append(Spacer(1, 0.5*cm))
    warn = Table([[Paragraph(
        '<b>⚠ BRAND-VOICE COMPLIANCE — GPS / "REAL-TIME" LANGUAGE</b><br/><br/>'
        'The Excel\'s USP list and bullet 2 of the current draft contain <i>"GPS location sharing via QR code"</i> and <i>"real-time GPS sharing"</i>. '
        'These <b>directly violate the SeQR Brand Voice doc</b>, which lists as "things we never say": <i>"Real-time GPS tracking", "Track your bag", "Active tracker", "live location"</i>. '
        'The tag does not track. It does not have a battery. It does not pulse a location.<br/><br/>'
        'What it actually does (per the Brand Voice doc): a finder who scans the QR code can <b>optionally</b> share their current location with you (a Google Maps link from <i>their</i> phone\'s permission), '
        'attached to a private message. The owner does not see a live map. The tag is passive.<br/><br/>'
        '<b>Reframed for this brief:</b> <i>"FINDERS CAN SHARE WHERE THEY ARE — Optional. When a finder scans your tag, they can attach a map link so you know where to pick up your bag. No live tracking, no battery, no app to install."</i> '
        'Compliant with the brand voice, with Amazon\'s claim rules, and more accurate to what the product actually does.', BODY)]],
        colWidths=[CW])
    warn.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), WARN_BG),
        ("BOX", (0,0), (-1,-1), 1.2, WARN_BD),
        ("LEFTPADDING", (0,0), (-1,-1), 14), ("RIGHTPADDING", (0,0), (-1,-1), 14),
        ("TOPPADDING", (0,0), (-1,-1), 12), ("BOTTOMPADDING", (0,0), (-1,-1), 12),
    ]))
    s.append(warn)

    # ───── Brandbook ─────
    s.append(PageBreak())
    s.append(Paragraph("1 · Brandbook (extracted from existing KeyTag & Luggage Tag designs + brand-voice doc)", H2))
    s.append(HRule())

    s.append(Paragraph("Color palette", H3))
    chips = [
        ColorChip(TEAL,   "#1AAEB6", "Primary · SeQR Teal"),
        ColorChip(NAVY,   "#0F2944", "Headline · Deep Navy"),
        ColorChip(PINK,   "#E8345C", "Accent CTA · Coral Pink"),
        ColorChip(SAND,   "#F2EDE2", "Background · Soft Cream"),
    ]
    s.append(Table([chips], colWidths=[CW/4]*4,
                   style=TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),
                                     ("LEFTPADDING",(0,0),(-1,-1),0),
                                     ("RIGHTPADDING",(0,0),(-1,-1),6)])))

    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph("Typography", H3))
    s.append(Paragraph(
        'Sans-serif used in existing Luggage / KeyTag designs: <b>bold rounded sans-serif</b> '
        '(close to Avenir Next / Nunito Sans / Manrope) for headlines · regular weight for body. '
        'ALL CAPS only for image-overlay headlines and badges. Pink (#E8345C) handwritten "Scan to try!" '
        'as a recurring CTA element.', BODY))

    s.append(Paragraph("Voice rules (verbatim from brand-voice doc)", H3))
    for r in [
        "Warm and calm, never dramatic. Lost luggage is stressful enough.",
        "Practical over clever. Clarity beats wordplay.",
        "Numbered steps for instructions. Plain English everywhere else.",
        "Confident but not preachy. The \"superhero\" idea is a gentle undercurrent, never a lecture.",
        "Honest about limits. No \"never lose anything again\". No \"real-time GPS tracking\". No \"guaranteed returns\".",
    ]:
        s.append(Paragraph("· " + r, BODY))

    s.append(Spacer(1, 0.2*cm))
    sig = Table([[Paragraph(
        '<b>Signature line:</b> <i>"Most people who find your bag want to help you get it back — we just make sure '
        'the few who don\'t can\'t use it against you."</i>', BODY)]],
        colWidths=[CW])
    sig.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), TEAL),
        ("TEXTCOLOR", (0,0), (-1,-1), WHITE),
        ("LEFTPADDING", (0,0), (-1,-1), 12), ("RIGHTPADDING", (0,0), (-1,-1), 12),
        ("TOPPADDING", (0,0), (-1,-1), 10), ("BOTTOMPADDING", (0,0), (-1,-1), 10),
    ]))
    s.append(sig)

    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("Visual style (extracted from existing Luggage Tag PNGs)", H3))
    for n in [
        '<b>Soft cream BG, rounded white cards.</b> #F2EDE2 with white panels — replicate from KeyTag set.',
        '<b>3-panel triptychs.</b> "Step by Step" is a proven layout — keep for "Stick · Scan · Message".',
        '<b>Red ✕ vs. green ✓ comparison frames.</b> "Don\'t expose yourself" pattern is strong — keep for write-on vs. SeQR.',
        '<b>4-icon trust strip.</b> "Privacy · Instant alerts · Private messaging · Location sharing" — keep, but rename "GPS" → "Location" (compliance).',
        '<b>Lifestyle context.</b> Hand holding the tag, tag on a suitcase, tag in water (durability) — all already shot. Reuse for the new image set.',
        '<b>Handwritten pink "Scan to try!"</b> CTA arrow is a recurring element. Keep on at least one image.',
    ]:
        s.append(Paragraph("· " + n, BODY))

    # ───── Moodboard ─────
    s.append(PageBreak())
    s.append(Paragraph("2 · Moodboard", H2)); s.append(HRule())
    s.append(Paragraph(
        "Mood: <b>warm, practical, real-life travel.</b> Soft natural light. Hands. Hard-shell suitcases. "
        "Real airport / hotel / coffee-shop atmosphere — not stock-photo perfection. Pink handwritten cues "
        "for one moment of delight. Teal as the brand's hero color; navy for trust; sand for backgrounds.", BODY))
    s.append(Spacer(1, 0.3*cm))

    md_w = (CW - 0.4*cm) / 3
    md_h = 3.6*cm
    row1 = Table([[
        MoodTile("Airport conveyor", "Real-life travel", md_airport, w=md_w, h=md_h, bg=SAND),
        MoodTile("QR + Tag", "Brand signature object", md_qr, w=md_w, h=md_h, bg=WHITE),
        MoodTile("Hand-held tag", "Reuse 'In Hand' PNG", md_handheld, w=md_w, h=md_h, bg=SAND),
    ]], colWidths=[md_w]*3)
    row1.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),
                              ("LEFTPADDING",(0,0),(-1,-1),0), ("RIGHTPADDING",(0,0),(-1,-1),5)]))
    s.append(row1)
    s.append(Spacer(1, 0.2*cm))
    row2 = Table([[
        MoodTile("Tag in water", "Durability claim", md_water, w=md_w, h=md_h, bg=HexColor("#E5EFF6")),
        MoodTile("Privacy lock", "Brand promise", md_privacy, w=md_w, h=md_h, bg=SAND),
        MoodTile("Brand palette", "Teal · Navy · Pink · Sand", md_palette, w=md_w, h=md_h, bg=WHITE),
    ]], colWidths=[md_w]*3)
    row2.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),
                              ("LEFTPADDING",(0,0),(-1,-1),0), ("RIGHTPADDING",(0,0),(-1,-1),5)]))
    s.append(row2)

    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("Set design — props & shots to source", H3))
    props = [
        ("Hero objects", "Hard-shell suitcase (slate blue) · canvas weekender bag · leather briefcase · backpack with name tag visible"),
        ("Lifestyle scenes", "Airport conveyor at golden hour · hotel-room luggage rack · cobblestone street in Europe · cab trunk loaded"),
        ("Props", "Boarding pass strapped to handle · passport peeking out · keychain ring · handwritten paper label (for the 'don't' comparison)"),
        ("People", "Hands only — diverse, warm. Cuff of a travel-shirt or sweater visible. No celebrity stock-model gloss."),
        ("Light", "Soft natural — airport window light, golden-hour exterior, warm hotel lamp. Avoid harsh flash."),
        ("No-Gos", "Posed family-laughing-at-airport stock · plastic-perfect models · futuristic tech aesthetic · 'GPS map' imagery (compliance)"),
    ]
    pt = Table([[Paragraph(f"<b>{k}</b>", BODY), Paragraph(v, BODY)] for k, v in props],
               colWidths=[3.4*cm, CW - 3.4*cm])
    pt.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,-1), SAND),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LINEBELOW", (0,0), (-1,-1), 0.3, HexColor("#E0DCC8")),
        ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 5), ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ]))
    s.append(pt)

    # ───── Buyer Psychology ─────
    s.append(PageBreak())
    s.append(Paragraph("3 · Buyer Psychology", H2)); s.append(HRule())
    s.append(Paragraph(
        "The Smart Luggage Tag buyer is more focused than the Lost-Item-Labels buyer. They have <b>one specific fear</b> — "
        "their checked or carry-on luggage going missing — and they want a way to be reachable that does not write their phone number "
        "on the side of a suitcase. Many have already tried AirTags and want a complementary, return-channel solution.", BODY))
    s.append(Spacer(1, 0.3*cm))

    s.append(Paragraph("Top buying triggers", H3))
    triggers = [
        ("Privacy fear (the SeQR core)", "Already wrote a phone number on a tag once. Got spam. Now refuses. \"Don't expose yourself\" frame is the strongest hook."),
        ("Recent or anticipated trip", "Heading abroad. Just had luggage delayed in Madrid. Wants something better than the airline's paper tag."),
        ("AirTag complement", "Already owns an AirTag. Knows it tells *them* where the bag is — but does not tell the *finder* who to call. SeQR fills the gap."),
        ("Family travel", "Travelling with kids. Multiple bags. Wants two tags so each adult can have a backup on their own bag."),
        ("No subscription anxiety", "Has been burned by tracker apps with hidden monthly fees. Wants a one-time-purchase that just works."),
    ]
    t = Table([[Paragraph(f"<b>{k}</b>", BODY), Paragraph(v, BODY)] for k, v in triggers],
              colWidths=[5.0*cm, CW - 5.0*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,-1), TEAL),
        ("TEXTCOLOR", (0,0), (0,-1), WHITE),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LINEBELOW", (0,0), (-1,-1), 0.3, HexColor("#E0DCC8")),
        ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 7), ("BOTTOMPADDING", (0,0), (-1,-1), 7),
    ]))
    s.append(t)

    s.append(Spacer(1, 0.4*cm))
    s.append(Paragraph("Friction points to defuse (from the bad-review column)", H3))
    fr = [
        ("\"Where is my bag — I thought it tracked it!\"", "#1 misconception. SeQR is a passive contact tag, not a tracker. There is no live map. Defuse in Image #2 and A+ Q&A."),
        ("\"The wire/loop broke after one trip\"", "Real complaint in reviews — luggage tag loops bend or snap under airport handling. Show the metal-reinforced loop in Image #5 + bullet 3. Consider upgrading the included loop."),
        ("\"GPS isn't real-time\"", "Buyer expected an AirTag and got a contact tag. Reframe BEFORE purchase — Image #3 (mechanism) and Q&A. Removes false expectation."),
        ("\"Recovery depends on the finder cooperating\"", "True. Reframe positively: \"Most people who find your bag want to help you.\" Brand-voice signature line addresses this head-on."),
        ("\"Where is the app? It's not in the App Store.\"", "SeQR is a Progressive Web App. Finders need no app — owners install via the browser. Address in Q&A."),
    ]
    t = Table([[Paragraph(f"<b>{k}</b>", BODY), Paragraph(v, BODY)] for k, v in fr],
              colWidths=[6.0*cm, CW - 6.0*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,-1), HexColor("#FBE5E8")),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LINEBELOW", (0,0), (-1,-1), 0.3, HexColor("#E0DCC8")),
        ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 7), ("BOTTOMPADDING", (0,0), (-1,-1), 7),
    ]))
    s.append(t)

    # ───── Main Image — 3 Options ─────
    s.append(PageBreak())
    s.append(Paragraph("4 · Main Image — 3 Options for CTR Test", H2)); s.append(HRule())
    s.append(Paragraph(
        "Amazon main-image rules: pure white background, product fills ≥ 85 % of frame, no overlay text. "
        "Three concepts test pack-shot, in-use, and mechanism. Recommend Manage Your Experiments A/B/C test for 4 weeks. "
        "Winner becomes Image #1; the other two move to slots #2 / #6.", BODY))
    s.append(Spacer(1, 0.3*cm))

    options = [
        ("A", "Pack-Shot",
         "Both tags (Teal + Pink) side-by-side, three-quarter angle, slight rim light to make the QR pattern pop. The metal loop catches a single highlight.",
         "Pack-density hook. Reads \"2 tags · clean · premium\" in 1 second. Lowest-risk baseline for launch.",
         cpt_main_a),
        ("B", "In-Use on Luggage",
         "A SeQR tag dangling from a hard-shell suitcase handle, three-quarter angle. Tag is the clear hero; suitcase is supportive context.",
         "Use-context hook. Tells the buyer \"this is what you do with them\" before they read the title. Strongest for the first-time category buyer.",
         cpt_main_b),
        ("C", "Tag + Phone Scan",
         "A SeQR tag with a phone hovering over it, scan frame visible on the screen. Shows the whole mechanism in one image.",
         "Mechanism hook. Defuses the #1 misconception (\"I thought it was an AirTag\") before the click. Highest education ROI.",
         cpt_main_c),
    ]
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
        s.append(KeepTogether([row])); s.append(Spacer(1, 0.4*cm))

    rec = Table([[Paragraph(
        "<b>Recommended:</b> Launch with <b>Option A (Pack-Shot)</b> as Image #1 — safest baseline, communicates the 2-pack value. "
        "Prepare B and C as challengers. 4-week A/B/C test via Manage Your Experiments. Winner becomes permanent #1; the other two slot into #2 / #6.", BODY)]],
        colWidths=[CW])
    rec.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), YELLOW),
        ("LEFTPADDING", (0,0), (-1,-1), 12), ("RIGHTPADDING", (0,0), (-1,-1), 12),
        ("TOPPADDING", (0,0), (-1,-1), 10), ("BOTTOMPADDING", (0,0), (-1,-1), 10),
    ]))
    s.append(rec)

    # ───── 7 Listing Images ─────
    s.append(PageBreak())
    s.append(Paragraph("5 · Seven Listing Images (full set)", H2)); s.append(HRule())
    s.append(Paragraph("Format: 2000 × 2000 px · sRGB · JPG · ≤ 5 MB. The 3 main-image options above feed Slot #1.", SUB))

    listings = [
        (1, "Click trigger",
         "(no overlay — winner of A/B/C above)",
         "See Main Image — 3 Options above. Test A/B/C; ship the winner.",
         lambda c, cx, cy: cpt_main_a(c, cx, cy),
         WHITE),
        (2, "Hook · privacy",
         "Don't put your number on a luggage tag.",
         "Split-frame: LEFT a paper write-on label with a (visible / risky) phone number — small red ✕. RIGHT a SeQR tag in teal — small green ✓. Mirrors the existing \"Don't Expose Yourself\" KeyTag layout.",
         cpt_img2,
         SAND),
        (3, "Educate · how it works",
         "Stick · Scan · Message.",
         "Three-panel triptych: (1) Hand attaching SeQR to a suitcase handle. (2) A finder's phone scanning the tag. (3) The owner's phone showing a chat bubble. 3 steps, no GPS imagery.",
         cpt_img3,
         WHITE),
        (4, "Key benefits · 5 promises",
         "5 reasons SeQR.",
         "Promoted from slot #7 per client feedback. Five icon badges around the central tag: Private messaging · No fees forever · No app for finders · No battery ever · Optional location sharing (finder-attached map link, not real-time GPS). Lives in the mobile-visible carousel position. The client's \"GPS love\" is included here as one badge — compliant phrasing, not its own frame.",
         cpt_img4_benefits,
         WHITE),
        (5, "Trust · built for travel",
         "Waterproof. Tear-resistant. UV-stable. Global.",
         "Central tag with four trust badges: water-drop, tear-test, UV-sun, world. Directly defuses the loop-break and water complaints from the reviews. Reinforced metal loop visible in the photograph.",
         cpt_img5,
         WHITE),
        (6, "Versatility · 2-pack · 2 messages",
         "Two tags. Every kind of bag. Any details. Any time.",
         "Central 2-pack flanked by four travel items: suitcase, carry-on, backpack, briefcase. A pink arrow between two phones at the bottom shows \"different message per tag\". Combines old #4 (versatility) and #6 (customize) into one frame.",
         cpt_img4,
         SAND),
        (7, "Brand close",
         "Reachable. Private. Free. — Scan to try.",
         "Tighter close shot: the tag, the pink handwritten \"Scan to try!\" CTA, and the signature line. Since the four badges have moved to image #4, this slot becomes the emotional close — \"Be findable by the people who want to help you.\"",
         cpt_img7,
         WHITE),
    ]
    for slot, role, headline, why, fn, bg in listings:
        s.append(Paragraph(f"Image {slot} — {role}", H3))
        m = ListingMockup(slot, role, fn, bg=bg)
        side = _side([
            Paragraph(f"<b>Headline:</b> {headline}", BODY),
            Spacer(1, 0.1*cm),
            Paragraph(f"<i>Why it works:</i> {why}", QUOTE),
        ], CW - m.size - m.gap)
        row = Table([[m, side]], colWidths=[m.size + m.gap, CW - m.size - m.gap])
        row.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),
                                 ("LEFTPADDING",(0,0),(-1,-1),0), ("RIGHTPADDING",(0,0),(-1,-1),0)]))
        s.append(KeepTogether([row])); s.append(Spacer(1, 0.35*cm))

    # ───── A+ ─────
    s.append(PageBreak())
    s.append(Paragraph("6 · A+ Premium Content (7 Modules)", H2)); s.append(HRule())
    s.append(Paragraph("Parent-level — same A+ across SeQR luggage tag SKUs.", SUB))

    modules = [
        (1, "Full Image", "Be findable by the people who want to help you.",
         "Without being findable by everyone else.", cpt_aplus1, SAND),
        (2, "Carousel (5)", "The SeQR Difference",
         "No phone number · No app for finder · No battery · No subscription · Re-customizable", cpt_aplus_carousel, WHITE),
        (3, "Full Image", "Stick. Scan. Message. Return.",
         "3 steps. Any phone. Any country. No app required for finders.", cpt_aplus3, SAND),
        (4, "Full Image", "One pack. Every trip.",
         "Suitcase + carry-on covered in seconds. Two tags, two messages, one purchase.", cpt_aplus4, NAVY),
        (5, "Carousel (5)", "What you can tag",
         "Suitcase · Backpack · Carry-on · Duffel · Gym bag", cpt_aplus_uses, WHITE),
        (6, "Q&A", "Defuses top objections",
         "Real-time tracking · Free check · App question · Waterproofing · 2-tag activation", cpt_aplus_qa, SAND),
        (7, "Comparison", "SeQR vs. write-on / engraved / AirTag / generic QR",
         "Privacy · Re-customize · Battery · App-for-finder · Subscription · Return channel", cpt_aplus_compare, WHITE),
    ]
    for slot, mtype, hl, sub, fn, bg in modules:
        s.append(Paragraph(f"Module {slot} — {mtype}", H3))
        m = APlusMockup(slot, mtype, fn, bg=bg)
        side = _side([
            Paragraph(f"<b>Headline:</b> {hl}", BODY),
            Paragraph(f"<b>Theme:</b> {sub}", BODY),
        ], CW - m.bw - m.gap)
        row = Table([[m, side]], colWidths=[m.bw + m.gap, CW - m.bw - m.gap])
        row.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),
                                 ("LEFTPADDING",(0,0),(-1,-1),0), ("RIGHTPADDING",(0,0),(-1,-1),0)]))
        s.append(KeepTogether([row])); s.append(Spacer(1, 0.35*cm))

    # ───── Q&A + Comparison ─────
    s.append(PageBreak())
    s.append(Paragraph("Module 6 — Q&amp;A (full copy, voice-aligned)", H3))
    qa = [
        ("Does this track my bag in real time?",
         "No. SeQR is a passive contact tag, not a tracker. There is no live map and no battery. "
         "When someone finds your bag and scans the QR code, they can send you a private message — "
         "and, if they choose, attach a map link of where they are. You decide what to do next."),
        ("Is it really free? What's the catch?",
         "The messaging service is free. No subscription, no monthly fee, no hidden charges. "
         "Your one-time purchase covers the two tags and the service behind them."),
        ("Does the finder need to download an app?",
         "No. When a finder scans your tag with any phone camera, the message page just opens in their browser. "
         "Owners install SeQR as a Progressive Web App from <i>app.seqrcontact.com</i> — also no App Store download required."),
        ("Is it really waterproof?",
         "Yes. The hard-plastic body and printed QR survive rain, snow, and the wash that happens to checked luggage. "
         "We do not recommend full submersion for extended periods."),
        ("How do I activate the two tags?",
         "Scan one of the tags to link the pack to your account. The second tag links automatically. "
         "Each tag can carry a different message — useful when you want one for your suitcase and one for your carry-on."),
        ("Can I use it on my pet's collar?",
         "No — these tags are sized for luggage, not pets. For pet collars, see SeQR Smart Pet Tags."),
    ]
    qa_tbl = Table([[Paragraph(f"<b>Q{i+1}.</b> {q}", BODY), Paragraph(a, BODY)] for i, (q, a) in enumerate(qa)],
                   colWidths=[6.0*cm, CW - 6.0*cm])
    qa_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,-1), SAND),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LINEBELOW", (0,0), (-1,-1), 0.3, HexColor("#E0DCC8")),
        ("LEFTPADDING", (0,0), (-1,-1), 10), ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 7), ("BOTTOMPADDING", (0,0), (-1,-1), 7),
    ]))
    s.append(qa_tbl)

    s.append(Spacer(1, 0.4*cm))
    s.append(Paragraph("Module 7 — Comparison Chart", H3))
    comp = [
        ["Feature", "SeQR Smart\nLuggage Tags", "Write-on\nor engraved", "AirTag / Tile\n(active tracker)", "Generic QR\nluggage tags"],
        ["Phone-number-free", "Yes", "Usually no", "N/A", "Often no"],
        ["Re-customizable after purchase", "Yes (any time)", "No", "N/A", "Sometimes"],
        ["No battery", "Yes", "Yes", "No (~1 yr)", "Yes"],
        ["No app required for finder", "Yes", "Yes", "No (ecosystem)", "Sometimes"],
        ["Built-in private messaging", "Yes", "No", "No return channel", "Sometimes (3rd-party)"],
        ["Optional location sharing", "Yes (finder-initiated)", "No", "Live map (different)", "Sometimes"],
        ["No subscription", "Yes", "Yes", "Mostly yes", "Varies"],
        ["Works internationally", "Yes", "Yes (if # is intl)", "Limited", "Sometimes"],
    ]
    comp_tbl = Table(comp, colWidths=[3.6*cm, 3.4*cm, 3.4*cm, 3.4*cm, 3.0*cm])
    comp_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), NAVY),
        ("TEXTCOLOR", (0,0), (-1,0), WHITE),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("BACKGROUND", (1,1), (1,-1), HexColor("#E6F6F7")),
        ("FONTNAME", (1,1), (1,-1), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,-1), 8.5),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("LEFTPADDING", (0,0), (-1,-1), 5), ("RIGHTPADDING", (0,0), (-1,-1), 5),
        ("TOPPADDING", (0,0), (-1,-1), 5), ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("GRID", (0,0), (-1,-1), 0.3, HexColor("#CCCCCC")),
        ("ROWBACKGROUNDS", (0,1), (0,-1), [WHITE, SAND]),
        ("ROWBACKGROUNDS", (2,1), (-1,-1), [WHITE, SAND]),
    ]))
    s.append(comp_tbl)

    # ───── Master Copy ─────
    s.append(PageBreak())
    s.append(Paragraph("7 · Master Copy (paste-ready)", H2)); s.append(HRule())

    s.append(Paragraph("Title (suggested rewrite, ~199 chars)", H3))
    title_box = Table([[Paragraph(
        "<b>SeQR Smart Luggage Tags — 2-Pack QR Code Travel ID for Suitcases, Carry-Ons, Backpacks "
        "· Privacy-First Contact Tag for Air Travel · No Phone Number Exposed · Waterproof · No App for Finders · No Subscription</b>", BODY)]],
        colWidths=[CW])
    title_box.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), TEAL),
        ("TEXTCOLOR", (0,0), (-1,-1), WHITE),
        ("LEFTPADDING", (0,0), (-1,-1), 12), ("RIGHTPADDING", (0,0), (-1,-1), 12),
        ("TOPPADDING", (0,0), (-1,-1), 8), ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ]))
    s.append(title_box)

    s.append(Spacer(1, 0.4*cm))
    s.append(Paragraph("Bullets (rewritten in voice — replaces the existing 5 bullets)", H3))
    bullets = [
        ("PHONE NUMBER OFF YOUR LUGGAGE",
         "When someone finds your bag and scans the QR code, they reach you through the SeQR app — no phone number, email, or address exposed. Most people who find your bag want to help you. The few who don't can't use it against you."),
        ("TWO TAGS · ONE PURCHASE",
         "Tag your suitcase and your carry-on. Or your bag and your travel partner's. Each tag carries its own message — write \"Allergy: nuts\" on the kids' carry-on, \"Insurance: policy #...\" on the checked bag. Edit any time."),
        ("BUILT FOR ACTUAL TRAVEL",
         "Hard-plastic body, waterproof, UV-stable, with a reinforced metal loop that survives airport handling. Tested against rain, snow, baggage carousels, and global travel — not just a desk."),
        ("FINDERS DON'T NEED AN APP",
         "Anyone with a phone camera scans and messages. No download. No account. Works on iPhone, Android, and desktop, in any country."),
        ("FINDERS CAN SHARE WHERE THEY ARE — OPTIONAL",
         "When a finder scans your tag, they can attach a Google Maps link of where they picked up your bag. No live tracking. No battery. No app to install. The location only shows up when the finder chooses to share it."),
    ]
    bt = Table([[Paragraph(f"<b>{i+1}. {h}</b>", BODY), Paragraph(b, BODY)] for i, (h, b) in enumerate(bullets)],
               colWidths=[5.8*cm, CW - 5.8*cm])
    bt.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,-1), SAND),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LINEBELOW", (0,0), (-1,-1), 0.3, HexColor("#E0DCC8")),
        ("LEFTPADDING", (0,0), (-1,-1), 10), ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 7), ("BOTTOMPADDING", (0,0), (-1,-1), 7),
    ]))
    s.append(bt)

    s.append(Spacer(1, 0.4*cm))
    s.append(Paragraph("Backend search terms (≤ 250 bytes)", H3))
    be = Table([[Paragraph(
        '<font face="Courier" size="8">qr luggage tag suitcase tsa approved smart baggage air travel name identifiers '
        'custom waterproof lost found locator electronic trackable rebound itag lucid cloud digital privacy carry on '
        'backpack briefcase 2 pack 3 pack family business international vacation cruise checked bag</font>', BODY)]],
        colWidths=[CW])
    be.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), HexColor("#F5F5F5")),
        ("LEFTPADDING", (0,0), (-1,-1), 10), ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 8), ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ]))
    s.append(be)

    s.append(Spacer(1, 0.4*cm))
    s.append(Paragraph("Compliance — what to remove from existing copy", H3))
    for line in [
        "<b>Remove from current bullet 2:</b> <i>\"share GPS locations\"</i> — replace with <i>\"share a map link\"</i> and clarify finder-initiated, optional. Real-time / GPS language is a brand-voice violation.",
        "<b>Remove from USP list:</b> <i>\"GPS location sharing via QR code\"</i> and <i>\"real-time GPS sharing\"</i> — same violation. Replaced in the bullets and Q&A above.",
        "Soften <i>\"tear-resistant, waterproof\"</i> with <i>\"tested against rain, snow, airport handling\"</i> if no third-party test exists. Brand voice rule: <i>\"Honest about limits.\"</i>",
        "Remove competitor brand names from bullets (\"AirTag\", \"Tile\", \"Samsung tags\") — Amazon flags these. Keep brand comparison only in A+ Module 7 chart, where compliant.",
        "Address the loop-break complaint with a real spec line in bullet 3 (\"reinforced metal loop\") rather than a marketing claim.",
    ]:
        s.append(Paragraph("· " + line, BODY))

    # ───── Priority uplifts ─────
    s.append(PageBreak())
    s.append(Paragraph("8 · Priority uplifts (CTR × CVR)", H2)); s.append(HRule())
    pri = [
        ("1", "Rewrite the GPS / real-time language out of bullet 2 + USPs",
         "Brand-voice violation AND a buyer-expectation mismatch (one of the top bad-review themes). Highest single-fix on conversion + reviews."),
        ("2", "Run Main Image A/B/C test (Manage Your Experiments)",
         "Three concepts above (Pack-shot · In-Use · Phone-Scan). 4-week test. Largest CTR lift available."),
        ("3", "Publish A+ Module 6 (Q&A) with 6 voice-aligned answers",
         "Defuses the \"is it really free\", \"does it track\", and \"app where?\" support questions before they become a 3-star review."),
        ("4", "Publish A+ Module 7 (Comparison Chart)",
         "Makes the price defensible vs. write-on / engraved / AirTag / generic QR in one frame. Justifies the 2-pack premium."),
        ("5", "Address loop durability in bullet 3 + Image #5",
         "Loop-break complaint is the #1 negative-review pattern. Specify reinforced metal loop; show it visually in Image #5."),
        ("6", "Consider a 3-pack SKU",
         "Top keyword \"luggage tags 3 pack\" has 539 SV with strong intent. 3-pack expands family-travel and gift use-cases."),
        ("7", "Add Subscribe & Save (gift / family / corporate)",
         "Bulk orders for corporate gifting and frequent-traveler households. Increases AOV + LTV."),
    ]
    pri_table = Table([[Paragraph(f"<b>{n}</b>", BODY), Paragraph(f"<b>{t}</b>", BODY), Paragraph(d, BODY)] for n, t, d in pri],
                      colWidths=[1*cm, 6.5*cm, CW - 7.5*cm])
    pri_table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,-1), NAVY),
        ("TEXTCOLOR", (0,0), (0,-1), WHITE),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LINEBELOW", (0,0), (-1,-1), 0.3, HexColor("#E0DCC8")),
        ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 7), ("BOTTOMPADDING", (0,0), (-1,-1), 7),
        ("ROWBACKGROUNDS", (1,0), (-1,-1), [WHITE, SAND]),
    ]))
    s.append(pri_table)

    doc.build(s)
    print(f"PDF: {OUT}")


if __name__ == "__main__":
    build()
