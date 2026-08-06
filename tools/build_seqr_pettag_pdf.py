#!/usr/bin/env python3
"""SeQR Contact — Smart Dog & Cat Tag (2-pack QR pet ID · B0FRN8C6D9)
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

OUT = "/Users/jonask/Desktop/SeQR_Smart_Pet_Tags_Brief.pdf"

# ─── SeQR palette ───────────────────────────────────────────────────
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
COLLAR  = HexColor("#7D2F2A")   # leather collar
COLLAR2 = HexColor("#3E5A6E")   # nylon collar — slate
FUR_BR  = HexColor("#A0734A")   # dog / cat coat — warm brown
FUR_GR  = HexColor("#8C8C8C")   # cat — grey
STEEL   = HexColor("#A8AEB4")   # keyring steel

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
    x = cx - size/2; y = cy - size/2
    c.setFillColor(bg); c.rect(x, y, size, size, fill=1, stroke=0)
    c.setFillColor(color)
    cs = size * 0.27
    for fx, fy in [(x, y + size - cs), (x + size - cs, y + size - cs), (x, y)]:
        c.rect(fx, fy, cs, cs, fill=1, stroke=0)
        c.setFillColor(bg); c.rect(fx + cs*0.18, fy + cs*0.18, cs*0.64, cs*0.64, fill=1, stroke=0)
        c.setFillColor(color); c.rect(fx + cs*0.32, fy + cs*0.32, cs*0.36, cs*0.36, fill=1, stroke=0)
    cell = size / 13
    import random
    rng = random.Random(13)
    for r in range(13):
        for col in range(13):
            if (r < 4 and col < 4) or (r < 4 and col >= 9) or (r >= 9 and col < 4):
                continue
            if rng.random() < 0.42:
                c.rect(x + col*cell, y + r*cell, cell*0.85, cell*0.85, fill=1, stroke=0)


def _draw_pet_tag(c, cx, cy, r=1.4*cm, color=TEAL, with_qr=True, with_ring=True, label=None):
    """Round acrylic pet tag with central QR + optional steel keyring at top."""
    # tag disc
    c.setFillColor(color); c.setStrokeColor(NAVY); c.setLineWidth(0.5)
    c.circle(cx, cy, r, fill=1, stroke=1)
    # subtle inner ring for "acrylic" feel
    c.setStrokeColor(Color(0,0,0,alpha=0.18)); c.setLineWidth(0.4)
    c.circle(cx, cy, r*0.92, fill=0, stroke=1)
    # punched hole at top
    c.setFillColor(WHITE); c.setStrokeColor(NAVY); c.setLineWidth(0.3)
    c.circle(cx, cy + r*0.78, r*0.10, fill=1, stroke=1)
    # steel keyring
    if with_ring:
        c.setStrokeColor(STEEL); c.setLineWidth(1.4)
        c.circle(cx, cy + r*1.05, r*0.20, fill=0, stroke=1)
    # central QR
    if with_qr:
        _draw_qr(c, cx, cy - r*0.05, size=r*1.05, color=NAVY, bg=WHITE)
    # bottom mini label
    if label:
        c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 5)
        c.drawCentredString(cx, cy - r*0.78, label)


def _draw_engraved_tag(c, cx, cy, r=0.9*cm):
    """Traditional engraved metal pet tag with exposed phone number — the 'don't' frame."""
    c.setFillColor(STEEL); c.setStrokeColor(NAVY); c.setLineWidth(0.4)
    c.circle(cx, cy, r, fill=1, stroke=1)
    c.setFillColor(WHITE); c.circle(cx, cy + r*0.72, r*0.13, fill=1, stroke=0)
    c.setFillColor(INK); c.setFont("Helvetica-Bold", 5)
    c.drawCentredString(cx, cy + r*0.20, "MAX")
    c.setFillColor(INK); c.setFont("Helvetica", 4.5)
    c.drawCentredString(cx, cy - r*0.05, "+1 555-")
    c.drawCentredString(cx, cy - r*0.25, "0123-456")


def _draw_collar(c, cx, cy, w=3.8*cm, h=0.7*cm, color=COLLAR, with_tag=True, tag_color=TEAL):
    """Horizontal collar strip with optional dangling tag."""
    # strap
    c.setFillColor(color); c.setStrokeColor(NAVY); c.setLineWidth(0.4)
    c.roundRect(cx - w/2, cy - h/2, w, h, h*0.2, fill=1, stroke=1)
    # stitching
    c.setStrokeColor(Color(1,1,1,alpha=0.4)); c.setLineWidth(0.3)
    c.line(cx - w/2 + 0.1*cm, cy - h*0.35, cx + w/2 - 0.1*cm, cy - h*0.35)
    c.line(cx - w/2 + 0.1*cm, cy + h*0.35, cx + w/2 - 0.1*cm, cy + h*0.35)
    # D-ring
    c.setStrokeColor(STEEL); c.setLineWidth(1.2)
    c.ellipse(cx - 0.18*cm, cy - h*0.8, cx + 0.18*cm, cy - h*0.4, fill=0, stroke=1)
    # dangling tag below D-ring
    if with_tag:
        _draw_pet_tag(c, cx, cy - h*1.4, r=0.55*cm, color=tag_color, with_ring=False)


def _draw_dog(c, cx, cy, w=2.6*cm, h=2.0*cm, color=FUR_BR):
    """Stylised dog silhouette — head + body."""
    # body
    c.setFillColor(color); c.setStrokeColor(NAVY); c.setLineWidth(0.4)
    c.roundRect(cx - w*0.45, cy - h*0.3, w*0.7, h*0.4, 0.1*cm, fill=1, stroke=1)
    # head
    c.circle(cx + w*0.30, cy + h*0.05, h*0.32, fill=1, stroke=1)
    # ear
    c.setFillColor(color)
    p = c.beginPath()
    p.moveTo(cx + w*0.10, cy + h*0.30); p.lineTo(cx + w*0.22, cy + h*0.45); p.lineTo(cx + w*0.28, cy + h*0.20); p.close()
    c.drawPath(p, fill=1, stroke=0)
    # tail
    c.setStrokeColor(NAVY); c.setLineWidth(1.0)
    c.line(cx - w*0.45, cy + h*0.05, cx - w*0.60, cy + h*0.30)
    # legs
    c.setFillColor(color)
    for lx in [-w*0.30, -w*0.05, w*0.10]:
        c.rect(cx + lx, cy - h*0.55, w*0.08, h*0.25, fill=1, stroke=0)
    # eye + nose
    c.setFillColor(NAVY); c.circle(cx + w*0.38, cy + h*0.12, 0.04*cm, fill=1, stroke=0)
    c.circle(cx + w*0.46, cy + h*0.02, 0.05*cm, fill=1, stroke=0)


def _draw_cat(c, cx, cy, w=2.0*cm, h=1.8*cm, color=FUR_GR):
    """Stylised sitting cat — head + body + tail curl."""
    # body (sitting)
    c.setFillColor(color); c.setStrokeColor(NAVY); c.setLineWidth(0.4)
    c.ellipse(cx - w*0.30, cy - h*0.5, cx + w*0.30, cy + h*0.05, fill=1, stroke=1)
    # head
    c.circle(cx, cy + h*0.20, h*0.28, fill=1, stroke=1)
    # ears (two triangles)
    for sign in [-1, 1]:
        p = c.beginPath()
        p.moveTo(cx + sign*h*0.18, cy + h*0.30)
        p.lineTo(cx + sign*h*0.10, cy + h*0.55)
        p.lineTo(cx + sign*h*0.25, cy + h*0.40); p.close()
        c.drawPath(p, fill=1, stroke=0)
    # eyes
    c.setFillColor(NAVY)
    c.circle(cx - h*0.08, cy + h*0.22, 0.04*cm, fill=1, stroke=0)
    c.circle(cx + h*0.08, cy + h*0.22, 0.04*cm, fill=1, stroke=0)
    # nose
    c.setFillColor(PINK); c.circle(cx, cy + h*0.12, 0.03*cm, fill=1, stroke=0)
    # whiskers
    c.setStrokeColor(NAVY); c.setLineWidth(0.3)
    c.line(cx - h*0.05, cy + h*0.10, cx - h*0.20, cy + h*0.12)
    c.line(cx + h*0.05, cy + h*0.10, cx + h*0.20, cy + h*0.12)
    # tail curl behind
    c.setStrokeColor(NAVY); c.setLineWidth(1.4); 
    c.arc(cx + w*0.10, cy - h*0.50, cx + w*0.55, cy + h*0.05, startAng=-90, extent=200)


def _draw_phone(c, cx, cy, w=1.4*cm, h=2.4*cm, scanning=False, msg_text=None):
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
        c.setFillColor(TEAL); c.roundRect(cx - w*0.32, cy - h*0.10, w*0.45, h*0.18, 0.06*cm, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.circle(cx - w*0.18, cy - h*0.01, 0.04*cm, fill=1, stroke=0)
        c.circle(cx - w*0.05, cy - h*0.01, 0.04*cm, fill=1, stroke=0)
        c.circle(cx + w*0.08, cy - h*0.01, 0.04*cm, fill=1, stroke=0)


def _draw_check(c, cx, cy, size=0.5*cm, color=GREEN_OK):
    c.setStrokeColor(color); c.setLineWidth(1.6)
    c.line(cx - size*0.3, cy, cx - size*0.05, cy - size*0.25)
    c.line(cx - size*0.05, cy - size*0.25, cx + size*0.3, cy + size*0.3)


def _draw_x(c, cx, cy, size=0.5*cm, color=RED_X):
    c.setStrokeColor(color); c.setLineWidth(1.6)
    c.line(cx - size*0.3, cy - size*0.3, cx + size*0.3, cy + size*0.3)
    c.line(cx - size*0.3, cy + size*0.3, cx + size*0.3, cy - size*0.3)


def _draw_water_drops(c, cx, cy, count=5):
    import random
    rng = random.Random(11)
    for _ in range(count):
        dx = (rng.random() - 0.5) * 1.6*cm
        dy = (rng.random() - 0.5) * 1.0*cm
        c.setFillColor(HexColor("#7AB7E0"))
        c.circle(cx + dx, cy + dy, 0.10*cm, fill=1, stroke=0)


def _draw_paw(c, cx, cy, size=0.4*cm, color=NAVY):
    c.setFillColor(color)
    # main pad
    c.ellipse(cx - size*0.45, cy - size*0.55, cx + size*0.45, cy - size*0.05, fill=1, stroke=0)
    # toe pads
    for (dx, dy) in [(-size*0.45, size*0.05), (size*0.45, size*0.05), (-size*0.20, size*0.40), (size*0.20, size*0.40)]:
        c.circle(cx + dx, cy + dy, size*0.18, fill=1, stroke=0)


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


# ─── Concept drawings — Main Image options ──────────────────────────

def cpt_main_a(c, cx, cy):
    """Pack hero — two round tags side-by-side with steel keyrings."""
    _draw_pet_tag(c, cx - 1.5*cm, cy, r=1.3*cm, color=TEAL, with_ring=True)
    _draw_pet_tag(c, cx + 1.5*cm, cy, r=1.3*cm, color=PINK, with_ring=True)
    c.setFillColor(GREY); c.setFont("Helvetica-Bold", 6.5)
    c.drawCentredString(cx, cy - 2.1*cm, "2-PACK · Teal + Pink")


def cpt_main_b(c, cx, cy):
    """In-use: tag on a dog's collar."""
    _draw_dog(c, cx + 0.5*cm, cy - 0.2*cm, w=3.4*cm, h=2.4*cm, color=FUR_BR)
    # collar across the dog's neck
    _draw_collar(c, cx + 0.6*cm, cy + 0.6*cm, w=2.6*cm, h=0.45*cm, color=COLLAR, tag_color=TEAL)


def cpt_main_c(c, cx, cy):
    """Tag + phone scanning."""
    _draw_pet_tag(c, cx - 1.0*cm, cy + 0.1*cm, r=1.2*cm, color=TEAL, with_ring=True)
    _draw_phone(c, cx + 1.3*cm, cy + 0.1*cm, w=1.4*cm, h=2.6*cm, scanning=True)
    c.setStrokeColor(Color(TEAL.red, TEAL.green, TEAL.blue, alpha=0.4))
    c.setLineWidth(0.6)
    c.line(cx - 0.1*cm, cy + 0.1*cm, cx + 0.8*cm, cy + 0.1*cm)


# ─── Listing image concepts ─────────────────────────────────────────

def cpt_img2(c, cx, cy):
    """Privacy hook — engraved tag (phone exposed) vs SeQR tag."""
    c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(cx, cy + 2.4*cm, "DON'T PUT YOUR NUMBER")
    c.drawCentredString(cx, cy + 2.0*cm, "ON YOUR PET'S COLLAR.")
    # LEFT: engraved metal tag with visible phone number
    _draw_engraved_tag(c, cx - 1.5*cm, cy + 0.2*cm, r=0.95*cm)
    _draw_x(c, cx - 1.5*cm, cy - 1.2*cm, size=0.6*cm)
    # vs
    c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 9)
    c.drawCentredString(cx, cy + 0.2*cm, "vs")
    # RIGHT: SeQR tag
    _draw_pet_tag(c, cx + 1.5*cm, cy + 0.2*cm, r=0.95*cm, color=TEAL, with_ring=False)
    _draw_check(c, cx + 1.5*cm, cy - 1.2*cm, size=0.6*cm)
    c.setFillColor(GREY); c.setFont("Helvetica", 6.5)
    c.drawCentredString(cx, cy - 1.95*cm, "Reachable when it counts. Private the rest of the time.")


def cpt_img3(c, cx, cy):
    """Stick → Scan → Message."""
    c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(cx, cy + 2.4*cm, "ATTACH · SCAN · MESSAGE.")
    panels = [(cx - 2.0*cm, "1", "Attach"),
              (cx,          "2", "Finder scans"),
              (cx + 2.0*cm, "3", "Message you")]
    for x, num, lbl in panels:
        c.setFillColor(TEAL); c.circle(x, cy + 1.2*cm, 0.32*cm, fill=1, stroke=0)
        c.setFillColor(WHITE); c.setFont("Helvetica-Bold", 9)
        c.drawCentredString(x, cy + 1.1*cm, num)
        if num == "1":
            _draw_collar(c, x, cy - 0.1*cm, w=1.6*cm, h=0.35*cm, color=COLLAR, tag_color=TEAL)
        elif num == "2":
            _draw_pet_tag(c, x - 0.5*cm, cy - 0.2*cm, r=0.4*cm, color=TEAL, with_ring=False)
            _draw_phone(c, x + 0.6*cm, cy - 0.2*cm, w=0.7*cm, h=1.2*cm, scanning=True)
        else:
            _draw_phone(c, x, cy - 0.2*cm, w=0.8*cm, h=1.3*cm, scanning=False)
        c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 6.5)
        c.drawCentredString(x, cy - 1.4*cm, lbl.upper())
    c.setFillColor(GREY); c.setFont("Helvetica", 6.5)
    c.drawCentredString(cx, cy - 2.0*cm, "Works on any phone. No app required for finders.")


# ─── Key benefits frame (slot #4) ───────────────────────────────────

def _draw_benefit_icon(c, cx, cy, kind, size=0.42*cm):
    if kind == "privacy":
        c.setFillColor(NAVY); c.roundRect(cx - size*0.5, cy - size*0.45, size, size*0.7, size*0.06, fill=1, stroke=0)
        c.setStrokeColor(NAVY); c.setLineWidth(0.9)
        c.arc(cx - size*0.3, cy + size*0.05, cx + size*0.3, cy + size*0.55, startAng=0, extent=180)
        c.setFillColor(YELLOW); c.circle(cx, cy - size*0.1, size*0.08, fill=1, stroke=0)
    elif kind == "no_fee":
        c.setFillColor(TEAL); c.circle(cx, cy, size*0.45, fill=1, stroke=0)
        c.setFillColor(WHITE); c.setFont("Helvetica-Bold", size*22)
        c.drawCentredString(cx, cy - size*0.15, "$")
        c.setStrokeColor(RED_X); c.setLineWidth(1.4)
        c.line(cx - size*0.5, cy - size*0.5, cx + size*0.5, cy + size*0.5)
    elif kind == "no_app":
        c.setFillColor(NAVY); c.roundRect(cx - size*0.25, cy - size*0.45, size*0.5, size*0.9, size*0.05, fill=1, stroke=0)
        c.setFillColor(WHITE); c.roundRect(cx - size*0.20, cy - size*0.35, size*0.4, size*0.65, size*0.03, fill=1, stroke=0)
        c.setStrokeColor(RED_X); c.setLineWidth(1.2)
        c.line(cx - size*0.20, cy - size*0.25, cx + size*0.20, cy + size*0.25)
        c.line(cx - size*0.20, cy + size*0.25, cx + size*0.20, cy - size*0.25)
    elif kind == "no_battery":
        c.setStrokeColor(NAVY); c.setLineWidth(0.8); c.setFillColor(WHITE)
        c.roundRect(cx - size*0.45, cy - size*0.25, size*0.85, size*0.5, size*0.04, fill=1, stroke=1)
        c.setFillColor(NAVY); c.rect(cx + size*0.40, cy - size*0.12, size*0.08, size*0.24, fill=1, stroke=0)
        c.setStrokeColor(RED_X); c.setLineWidth(1.2)
        c.line(cx - size*0.40, cy - size*0.30, cx + size*0.40, cy + size*0.30)
    elif kind == "world":
        c.setStrokeColor(TEAL); c.setLineWidth(0.8); c.setFillColor(WHITE)
        c.circle(cx, cy, size*0.45, fill=1, stroke=1)
        c.setStrokeColor(TEAL); c.setLineWidth(0.5)
        c.line(cx - size*0.45, cy, cx + size*0.45, cy)
        c.ellipse(cx - size*0.20, cy - size*0.45, cx + size*0.20, cy + size*0.45, fill=0, stroke=1)
        c.setFillColor(PINK); c.circle(cx + size*0.18, cy - size*0.10, size*0.10, fill=1, stroke=0)


def cpt_img4_benefits(c, cx, cy):
    """Key Benefits — 5 badges around the central pet tag."""
    c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(cx, cy + 2.4*cm, "5 REASONS SeQR")
    c.setFillColor(GREY); c.setFont("Helvetica", 7)
    c.drawCentredString(cx, cy + 2.05*cm, "What you get with every pack")
    _draw_pet_tag(c, cx, cy - 0.2*cm, r=0.8*cm, color=TEAL, with_ring=False)
    badges = [
        ( -2.2*cm,  1.3*cm, "privacy",    "PRIVATE\nMESSAGING",    "Phone & email hidden"),
        (  2.2*cm,  1.3*cm, "no_fee",     "NO FEES\nFOREVER",      "No subscription"),
        ( -2.4*cm, -0.4*cm, "no_app",     "NO APP\nFOR FINDERS",   "Any phone, any country"),
        (  2.4*cm, -0.4*cm, "no_battery", "NO BATTERY\nEVER",      "Passive tag, works decades"),
        (  0,      -1.9*cm, "world",      "OPTIONAL\nLOCATION",    "Finder attaches map link"),
    ]
    for dx, dy, kind, label, sub in badges:
        c.setFillColor(WHITE); c.setStrokeColor(TEAL); c.setLineWidth(0.6)
        c.roundRect(cx + dx - 0.95*cm, cy + dy - 0.45*cm, 1.9*cm, 0.9*cm, 0.10*cm, fill=1, stroke=1)
        _draw_benefit_icon(c, cx + dx - 0.65*cm, cy + dy, kind)
        c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 5.5)
        for i, ln in enumerate(label.split("\n")):
            c.drawString(cx + dx - 0.25*cm, cy + dy + 0.18*cm - i*0.18*cm, ln)
        c.setFillColor(GREY); c.setFont("Helvetica", 4.5)
        c.drawString(cx + dx - 0.25*cm, cy + dy - 0.30*cm, sub)


def cpt_img5(c, cx, cy):
    """Durability — addresses the QR-fade / break complaints."""
    c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(cx, cy + 2.4*cm, "BUILT FOR REAL PET LIFE.")
    _draw_pet_tag(c, cx, cy - 0.1*cm, r=0.9*cm, color=TEAL, with_ring=False)
    quads = [(-2.0*cm,  1.5*cm, "WATERPROOF"),
             ( 2.0*cm,  1.5*cm, "SCRATCH-\nRESISTANT"),
             (-2.0*cm, -1.3*cm, "LASER-\nETCHED QR"),
             ( 2.0*cm, -1.3*cm, "LIGHTWEIGHT")]
    for dx, dy, lbl in quads:
        c.setFillColor(SAND); c.setStrokeColor(TEAL); c.setLineWidth(0.5)
        c.circle(cx + dx, cy + dy, 0.42*cm, fill=1, stroke=1)
        if "WATER" in lbl:
            _draw_water_drops(c, cx + dx, cy + dy, count=3)
        elif "SCRATCH" in lbl:
            c.setStrokeColor(NAVY); c.setLineWidth(0.6)
            for i in range(3):
                c.line(cx + dx - 0.18*cm + i*0.10*cm, cy + dy - 0.18*cm,
                       cx + dx - 0.08*cm + i*0.10*cm, cy + dy + 0.18*cm)
        elif "QR" in lbl:
            # tiny QR
            _draw_qr(c, cx + dx, cy + dy, size=0.6*cm)
        else:  # LIGHTWEIGHT — feather
            c.setStrokeColor(NAVY); c.setLineWidth(0.7); 
            c.bezier(cx + dx - 0.20*cm, cy + dy - 0.20*cm,
                     cx + dx - 0.10*cm, cy + dy,
                     cx + dx + 0.05*cm, cy + dy + 0.10*cm,
                     cx + dx + 0.20*cm, cy + dy + 0.20*cm)
            for i in range(4):
                c.line(cx + dx - 0.15*cm + i*0.10*cm, cy + dy - 0.10*cm + i*0.06*cm,
                       cx + dx - 0.05*cm + i*0.10*cm, cy + dy - 0.20*cm + i*0.06*cm)
        c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 5.5)
        lines = lbl.split("\n")
        for i, line in enumerate(lines):
            c.drawCentredString(cx + dx, cy + dy - 0.65*cm - i*0.18*cm, line)


def cpt_img6(c, cx, cy):
    """Versatility · 2-pack · 2 messages — for dog + cat household."""
    c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(cx, cy + 2.4*cm, "TWO TAGS. TWO PETS. ANY DETAILS.")
    # central 2-pack
    _draw_pet_tag(c, cx - 0.7*cm, cy + 0.3*cm, r=0.7*cm, color=TEAL, with_ring=False)
    _draw_pet_tag(c, cx + 0.7*cm, cy + 0.3*cm, r=0.7*cm, color=PINK, with_ring=False)
    # dog and cat below
    _draw_dog(c, cx - 1.7*cm, cy - 1.4*cm, w=1.8*cm, h=1.2*cm, color=FUR_BR)
    _draw_cat(c, cx + 1.7*cm, cy - 1.4*cm, w=1.4*cm, h=1.2*cm, color=FUR_GR)
    # labels
    c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 6)
    c.drawCentredString(cx - 1.6*cm, cy - 2.3*cm, "Tag 1 · Max")
    c.drawCentredString(cx + 1.6*cm, cy - 2.3*cm, "Tag 2 · Luna")
    # pink arrow between tags
    c.setStrokeColor(PINK); c.setLineWidth(1.0)
    c.line(cx - 0.2*cm, cy + 0.3*cm, cx + 0.2*cm, cy + 0.3*cm)


def cpt_img7(c, cx, cy):
    """Emotional brand close — tag + Scan to try."""
    c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(cx, cy + 2.4*cm, "REACHABLE. PRIVATE. FREE.")
    # central tag (larger — hero)
    _draw_pet_tag(c, cx + 0.4*cm, cy + 0.2*cm, r=1.3*cm, color=TEAL, with_ring=True)
    # paw print in negative space
    _draw_paw(c, cx - 1.8*cm, cy - 0.4*cm, size=0.7*cm, color=Color(NAVY.red, NAVY.green, NAVY.blue, alpha=0.12))
    # "Scan to try!" handwritten in pink
    c.saveState()
    c.translate(cx - 2.0*cm, cy + 1.0*cm)
    c.rotate(-8)
    c.setFillColor(PINK); c.setFont("Helvetica-BoldOblique", 11)
    c.drawString(0, 0, "Scan to try!")
    c.restoreState()
    c.setStrokeColor(PINK); c.setLineWidth(1.3)
    c.bezier(cx - 1.2*cm, cy + 0.9*cm, cx - 0.7*cm, cy + 0.4*cm,
             cx - 0.5*cm, cy + 0.7*cm, cx - 0.2*cm, cy + 0.5*cm)
    c.setFillColor(PINK)
    p = c.beginPath()
    p.moveTo(cx - 0.18*cm, cy + 0.48*cm); p.lineTo(cx - 0.32*cm, cy + 0.62*cm); p.lineTo(cx - 0.30*cm, cy + 0.40*cm); p.close()
    c.drawPath(p, fill=1, stroke=0)
    # signature line
    c.setFillColor(GREY); c.setFont("Helvetica-Oblique", 6.5)
    c.drawCentredString(cx, cy - 1.7*cm, "Be findable by the people who want to help your pet home.")
    c.setFillColor(GREY); c.setFont("Helvetica-Oblique", 6)
    c.drawCentredString(cx, cy - 2.0*cm, "Without being findable by everyone else.")


# ─── A+ banner concepts ──────────────────────────────────────────────

def cpt_aplus1(c, cx, cy):
    """Heritage banner — dog with collar + tag."""
    _draw_dog(c, cx + 2.2*cm, cy - 0.3*cm, w=2.6*cm, h=2.0*cm, color=FUR_BR)
    _draw_collar(c, cx + 2.3*cm, cy + 0.5*cm, w=1.8*cm, h=0.35*cm, color=COLLAR, tag_color=TEAL)
    _draw_pet_tag(c, cx - 2.5*cm, cy + 0.2*cm, r=1.0*cm, color=TEAL, with_ring=True)
    c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 13)
    c.drawCentredString(cx - 0.5*cm, cy + 0.6*cm, "BE FINDABLE")
    c.setFillColor(NAVY); c.setFont("Helvetica", 8)
    c.drawCentredString(cx - 0.5*cm, cy + 0.0*cm, "by the people who want to bring them home.")


def cpt_aplus_carousel(c, cx, cy):
    for i in range(5):
        x = cx - 2.2*cm + i*1.1*cm
        c.setFillColor(WHITE); c.setStrokeColor(TEAL); c.setLineWidth(0.5)
        c.roundRect(x - 0.5*cm, cy - 0.5*cm, 1.0*cm, 1.0*cm, 0.06*cm, fill=1, stroke=1)
        c.setFillColor(TEAL); c.setFont("Helvetica-Bold", 8)
        c.drawCentredString(x, cy + 0.1*cm, str(i+1))
    c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 8)
    c.drawCentredString(cx, cy + 1.1*cm, "5 REASONS SeQR")
    c.setFillColor(GREY); c.setFont("Helvetica", 6.5)
    c.drawCentredString(cx, cy - 0.9*cm, "Privacy · No fees · No app · No battery · Customize")


def cpt_aplus3(c, cx, cy):
    for i, lbl in enumerate(["1 Attach", "2 Scan", "3 Message"]):
        x = cx - 3.0*cm + i*3.0*cm
        c.setFillColor(TEAL); c.circle(x, cy + 0.5*cm, 0.3*cm, fill=1, stroke=0)
        c.setFillColor(WHITE); c.setFont("Helvetica-Bold", 8)
        c.drawCentredString(x, cy + 0.4*cm, lbl[0])
        c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 8)
        c.drawCentredString(x, cy - 0.1*cm, lbl[1:].strip().upper())
    c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 9)
    c.drawCentredString(cx, cy + 1.1*cm, "HOW SeQR WORKS")


def cpt_aplus4(c, cx, cy):
    """Dog + cat side-by-side hero."""
    _draw_dog(c, cx - 2.0*cm, cy - 0.2*cm, w=2.4*cm, h=1.6*cm, color=FUR_BR)
    _draw_cat(c, cx + 2.0*cm, cy - 0.2*cm, w=1.6*cm, h=1.4*cm, color=FUR_GR)
    _draw_pet_tag(c, cx, cy + 0.2*cm, r=0.8*cm, color=TEAL, with_ring=False)
    c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(cx, cy + 1.2*cm, "DOGS · CATS · ANY PET")


def cpt_aplus_uses(c, cx, cy):
    """Use-case carousel."""
    labels = ["COLLAR", "HARNESS", "CARRIER", "LEASH", "KEYRING"]
    for i, lbl in enumerate(labels):
        x = cx - 2.2*cm + i*1.1*cm
        c.setFillColor(COLLAR); c.setStrokeColor(NAVY); c.setLineWidth(0.4)
        c.roundRect(x - 0.4*cm, cy - 0.35*cm, 0.8*cm, 0.7*cm, 0.05*cm, fill=1, stroke=1)
        _draw_pet_tag(c, x, cy - 0.65*cm, r=0.18*cm, color=TEAL, with_ring=False, with_qr=False)
        c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 5.5)
        c.drawCentredString(x, cy - 1.0*cm, lbl)


def cpt_aplus_qa(c, cx, cy):
    c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(cx, cy + 0.9*cm, "FREQUENTLY ASKED")
    for i, q in enumerate([
        "Does it track in real time?",
        "Will the QR rub off?",
        "Does the finder need an app?",
        "Is it really free?",
        "Will it survive water and play?",
    ]):
        c.setFillColor(NAVY); c.setFont("Helvetica", 6.5)
        c.drawCentredString(cx, cy + 0.3*cm - i*0.20*cm, "· " + q)


def cpt_aplus_compare(c, cx, cy):
    cols = ["SeQR", "Engraved", "AirTag", "GPS Coll.", "Other QR"]
    w = 1.7*cm
    for i, col in enumerate(cols):
        x = cx - 4.3*cm + i*w
        c.setFillColor(TEAL if i == 0 else WHITE); c.setStrokeColor(NAVY); c.setLineWidth(0.4)
        c.rect(x, cy - 0.8*cm, w - 0.05*cm, 1.4*cm, fill=1, stroke=1)
        if i == 0:
            _draw_pet_tag(c, x + w/2, cy + 0.1*cm, r=0.4*cm, color=NAVY, with_ring=False, with_qr=False)
        else:
            c.setFillColor(GREY); c.setFont("Helvetica", 5.5)
            c.drawCentredString(x + w/2, cy + 0.1*cm, "—")
        c.setFillColor(WHITE if i == 0 else NAVY); c.setFont("Helvetica-Bold", 5.5)
        c.drawCentredString(x + w/2, cy - 0.55*cm, col)


# ─── Moodboard tile drawings ─────────────────────────────────────────

def md_park(c, cx, cy):
    """Park scene — dog on leash with tag."""
    _draw_dog(c, cx + 0.3*cm, cy - 0.2*cm, w=2.2*cm, h=1.6*cm, color=FUR_BR)
    _draw_collar(c, cx + 0.4*cm, cy + 0.4*cm, w=1.6*cm, h=0.3*cm, color=COLLAR, tag_color=TEAL)
    # leash going off-frame
    c.setStrokeColor(NAVY); c.setLineWidth(0.8)
    c.line(cx + 0.4*cm, cy + 0.4*cm, cx - 1.8*cm, cy + 1.2*cm)


def md_qr(c, cx, cy):
    _draw_qr(c, cx, cy + 0.3*cm, size=1.8*cm, color=NAVY, bg=WHITE)
    _draw_pet_tag(c, cx, cy - 1.0*cm, r=0.5*cm, color=TEAL, with_ring=False, with_qr=False, label="SeQR")


def md_dogcat(c, cx, cy):
    _draw_dog(c, cx - 1.0*cm, cy, w=1.8*cm, h=1.4*cm, color=FUR_BR)
    _draw_cat(c, cx + 1.2*cm, cy - 0.1*cm, w=1.2*cm, h=1.2*cm, color=FUR_GR)


def md_water(c, cx, cy):
    _draw_water_drops(c, cx, cy + 0.4*cm, count=12)
    _draw_pet_tag(c, cx, cy - 0.3*cm, r=0.8*cm, color=TEAL, with_ring=False)


def md_privacy(c, cx, cy):
    """Padlock + exposed phone crossed out."""
    c.setFillColor(NAVY); c.setStrokeColor(NAVY); c.setLineWidth(0.5)
    c.roundRect(cx - 0.5*cm, cy - 0.5*cm, 1.0*cm, 0.8*cm, 0.05*cm, fill=1, stroke=1)
    c.setFillColor(YELLOW); c.circle(cx, cy - 0.1*cm, 0.10*cm, fill=1, stroke=0)
    c.setStrokeColor(NAVY); c.setLineWidth(0.8)
    c.arc(cx - 0.3*cm, cy + 0.3*cm, cx + 0.3*cm, cy + 0.9*cm, startAng=0, extent=180)
    c.setFillColor(GREY); c.setFont("Helvetica", 6)
    c.drawCentredString(cx, cy - 1.1*cm, "+1 555-0123")
    c.setStrokeColor(RED_X); c.setLineWidth(1.0)
    c.line(cx - 0.8*cm, cy - 1.05*cm, cx + 0.8*cm, cy - 0.95*cm)


def md_palette(c, cx, cy):
    cols = [TEAL, NAVY, PINK, YELLOW, SAND]
    for i, col in enumerate(cols):
        x = cx - 1.6*cm + i*0.8*cm
        c.setFillColor(col); c.setStrokeColor(HexColor("#CCCCCC")); c.setLineWidth(0.3)
        c.rect(x - 0.32*cm, cy - 0.4*cm, 0.65*cm, 0.9*cm, fill=1, stroke=1)


# ─── Page chrome ─────────────────────────────────────────────────────

def cover_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(SAND); canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    canvas.setFillColor(TEAL); canvas.rect(0, PAGE_H - 4*cm, PAGE_W, 4*cm, fill=1, stroke=0)
    canvas.setFillColor(NAVY); canvas.rect(0, PAGE_H - 4.4*cm, PAGE_W, 0.4*cm, fill=1, stroke=0)
    canvas.setFillColor(WHITE); canvas.setFont("Helvetica-Bold", 38)
    canvas.drawString(ML, PAGE_H - 2.6*cm, "SeQR")
    canvas.setFont("Helvetica", 16); canvas.setFillColor(WHITE)
    canvas.drawString(ML, PAGE_H - 3.4*cm, "Smart Dog & Cat Tag · 2-Pack · Privacy QR Pet ID")
    canvas.setFillColor(NAVY); canvas.setFont("Helvetica-Bold", 22)
    canvas.drawString(ML, PAGE_H - 7*cm, "Amazon US Image Plan")
    canvas.setFillColor(GREY); canvas.setFont("Helvetica", 13)
    canvas.drawString(ML, PAGE_H - 7.8*cm, "3 Main Image Options · 7 Listing Images · A+ Premium · Master Copy")

    # Meta row
    y = 5.0*cm
    fields = [("ASIN", "B0FRN8C6D9"), ("CATEGORY", "QR Pet ID Tags"), ("PACK", "2 tags · 2 steel rings"), ("DATE", "2026-05-16")]
    for i, (k, v) in enumerate(fields):
        x = ML + i * 4.4*cm
        canvas.setFillColor(NAVY); canvas.setFont("Helvetica-Bold", 8)
        canvas.drawString(x, y, k)
        canvas.setFillColor(INK); canvas.setFont("Helvetica", 11)
        canvas.drawString(x, y - 0.55*cm, v)

    # Sample tags — fill middle cream space
    _draw_pet_tag(canvas, PAGE_W - MR - 6.0*cm, PAGE_H - 12.0*cm, r=1.9*cm, color=TEAL, with_ring=True)
    _draw_pet_tag(canvas, PAGE_W - MR - 2.2*cm, PAGE_H - 12.5*cm, r=1.9*cm, color=PINK, with_ring=True)
    # Tagline
    canvas.setFillColor(GREY); canvas.setFont("Helvetica-Oblique", 10)
    canvas.drawString(ML, PAGE_H - 14.5*cm, "Two tags. Two pets. Any details. Any time.")

    # Bottom strap
    canvas.setFillColor(NAVY); canvas.rect(0, 0, PAGE_W, 1.4*cm, fill=1, stroke=0)
    canvas.setFillColor(TEAL); canvas.setFont("Helvetica-Bold", 10)
    canvas.drawString(ML, 0.5*cm, "BE FINDABLE BY THE PEOPLE WHO WANT TO BRING THEM HOME.")
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
    canvas.drawString(ML + 1.9*cm, PAGE_H - 0.7*cm, "Smart Dog & Cat Tag (2-Pack QR) · Amazon US Brief")
    canvas.setFillColor(GREY); canvas.setFont("Helvetica", 8)
    canvas.drawRightString(PAGE_W - MR, PAGE_H - 0.7*cm, f"Page {doc.page}")
    canvas.setStrokeColor(HexColor("#E0DCC8")); canvas.setLineWidth(0.4)
    canvas.line(ML, MB - 0.4*cm, PAGE_W - MR, MB - 0.4*cm)
    canvas.setFillColor(GREY); canvas.setFont("Helvetica", 7.5)
    canvas.drawString(ML, MB - 0.7*cm, "Prepared by EQUALICE — 2026-05-16 · ASIN B0FRN8C6D9")
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
                          title="SeQR Smart Dog & Cat Tag — Image Plan",
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
        ["Brand", "SeQR Contact — privacy-first QR contact tags."],
        ["Product", "Smart Dog & Cat Tag — 2-pack round acrylic QR pet ID with steel keyring. Waterproof, scratch-resistant, no app for finders."],
        ["ASIN", "B0FRN8C6D9 · amazon.com"],
        ["Use case", "Pet owners (dog + cat households) who want their pet reachable without exposing their own phone number on a collar. When the pet is found, the finder scans the QR → messages the owner privately through SeQR."],
        ["Hero buyer trigger", '"My dog slipped his leash at the park last month. The engraved tag still had my old number. I need something I can update."'],
        ["Top competitors", "Pet Dwelling QR Tag · GoTag · Pawscout · Byte Tag · Whistle ID Tag · generic etched dog tags"],
        ["Top keywords (US, SV)", "dog name tag (12,284) · dog id tags (11,932) · custom dog tag (4,136) · dog tags for pets (2,553) · dog id tag (2,200) · pet id tags for dogs (2,197) · pet id tag (1,865)"],
        ["Brand voice", 'Warm + practical + plainspoken. "We\'ve got you" — not "submit a ticket". Numbered steps. Honest about limits. The pet community looks out for each other.'],
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
        '<b>⚠ BRAND-VOICE COMPLIANCE — "REAL-TIME" / TRACKER LANGUAGE</b><br/><br/>'
        'The current Excel USP list and bullet 3 read <i>"Instant real-time alerts when scanned"</i> and <i>"REAL-TIME ALERTS"</i>. '
        'The brand-voice doc lists as things-we-never-say: <i>"Real-time GPS tracking"</i>, <i>"Track your bag"</i>, <i>"Active tracker"</i>, <i>"live location"</i>. '
        '"Real-time alerts" is borderline — it reinforces the buyer misconception (see bad-review #5: <i>"Confusion/frustration that it doesn\'t provide real-time location tracking"</i>). <br/><br/>'
        '<b>Reframed here:</b> <i>"INSTANT SCAN ALERTS"</i> or <i>"YOU\'RE NOTIFIED THE MOMENT YOUR PET\'S TAG IS SCANNED"</i> — accurate, no tracker connotation.<br/><br/>'
        '<b>GPS location:</b> bullets 3 + 5 say <i>"share GPS location"</i> / <i>"view the GPS location"</i>. Per brand voice, location sharing is <b>finder-initiated, optional, manual</b> — not GPS. '
        'Reframe as <i>"FINDER CAN ATTACH A MAP LINK"</i>. No live tracking, no battery, no app.', BODY)]],
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
    s.append(Paragraph("1 · Brandbook (extracted from existing SeQR designs + brand-voice doc)", H2))
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
        'Bold rounded sans-serif (close to Avenir Next / Nunito Sans / Manrope) for headlines · regular weight for body. '
        'ALL CAPS for image-overlay headlines and badges only. Pink (#E8345C) handwritten "Scan to try!" '
        'as the recurring CTA element.', BODY))

    s.append(Paragraph("Voice rules (verbatim from brand-voice doc)", H3))
    for r in [
        "Warm and calm, never dramatic. A lost pet is stressful enough.",
        "Practical over clever. Clarity beats wordplay.",
        "Numbered steps for instructions. Plain English everywhere else.",
        "Confident but not preachy. The community-helper undercurrent is gentle, never a lecture.",
        "Honest about limits. No \"never lose your pet again\". No \"real-time GPS tracking\". No \"guaranteed return\".",
    ]:
        s.append(Paragraph("· " + r, BODY))

    s.append(Spacer(1, 0.2*cm))
    sig = Table([[Paragraph(
        '<b>Signature line:</b> <i>"Most people who find your dog or cat want to bring them home — '
        'we just make sure the few who don\'t can\'t use your number against you."</i>', BODY)]],
        colWidths=[CW])
    sig.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), TEAL),
        ("TEXTCOLOR", (0,0), (-1,-1), WHITE),
        ("LEFTPADDING", (0,0), (-1,-1), 12), ("RIGHTPADDING", (0,0), (-1,-1), 12),
        ("TOPPADDING", (0,0), (-1,-1), 10), ("BOTTOMPADDING", (0,0), (-1,-1), 10),
    ]))
    s.append(sig)

    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("Visual style", H3))
    for n in [
        '<b>Soft cream BG, rounded white cards.</b> #F2EDE2 with white panels — replicate from KeyTag set.',
        '<b>Step-by-step triptychs.</b> "Attach · Scan · Message" mirrors the proven KeyTag step layout.',
        '<b>Red ✕ vs. green ✓ comparisons.</b> Engraved-tag-with-phone vs. SeQR — strong privacy hook.',
        '<b>Real pet lifestyle.</b> Dog at the park, cat on a windowsill, kid clipping the tag onto a collar. Avoid stock-perfect golden-retriever-on-white.',
        '<b>Handwritten pink "Scan to try!"</b> CTA arrow on the final close.',
    ]:
        s.append(Paragraph("· " + n, BODY))

    # ───── Moodboard ─────
    s.append(PageBreak())
    s.append(Paragraph("2 · Moodboard", H2)); s.append(HRule())
    s.append(Paragraph(
        "Mood: <b>warm, lived-in, real pet life.</b> Soft natural light. Hands clipping a collar. Dogs at the park, cats on windowsills. "
        "The pet community looks out for each other — and SeQR is the privacy-respecting tool for that. Teal as hero color; navy for trust; "
        "pink for delight; sand for ground.", BODY))
    s.append(Spacer(1, 0.3*cm))

    md_w = (CW - 0.4*cm) / 3
    md_h = 3.6*cm
    row1 = Table([[
        MoodTile("Dog at the park", "Real-life pet moments", md_park, w=md_w, h=md_h, bg=SAND),
        MoodTile("QR + Tag", "Signature object", md_qr, w=md_w, h=md_h, bg=WHITE),
        MoodTile("Dog + Cat", "2-pack households", md_dogcat, w=md_w, h=md_h, bg=SAND),
    ]], colWidths=[md_w]*3)
    row1.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),
                              ("LEFTPADDING",(0,0),(-1,-1),0), ("RIGHTPADDING",(0,0),(-1,-1),5)]))
    s.append(row1)
    s.append(Spacer(1, 0.2*cm))
    row2 = Table([[
        MoodTile("Tag in water", "Survives bath + rain", md_water, w=md_w, h=md_h, bg=HexColor("#E5EFF6")),
        MoodTile("Privacy lock", "Brand promise", md_privacy, w=md_w, h=md_h, bg=SAND),
        MoodTile("Brand palette", "Teal · Navy · Pink · Sand", md_palette, w=md_w, h=md_h, bg=WHITE),
    ]], colWidths=[md_w]*3)
    row2.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),
                              ("LEFTPADDING",(0,0),(-1,-1),0), ("RIGHTPADDING",(0,0),(-1,-1),5)]))
    s.append(row2)

    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("Set design — props & shots to source", H3))
    props = [
        ("Hero objects", "Round acrylic SeQR tag (Teal + Pink) · leather collar · nylon harness · steel keyring · cat carrier"),
        ("Lifestyle scenes", "Dog at the park on a leash · cat on a sunny windowsill · kid clipping a tag onto a small-dog collar · vet-table moment with multiple tags"),
        ("Props", "Old engraved metal tag with visible phone number (for the 'don't' comparison) · paw-print background pattern · grooming brush · pet bowl"),
        ("People", "Hands only. Diverse, warm. Cuffs of weekend wear visible. No celebrity-dog-influencer aesthetic."),
        ("Light", "Soft natural — morning park light, golden hour, warm kitchen lamp. Never harsh studio flash."),
        ("No-Gos", "Posed family with golden retriever on white background · GPS-map / tracker imagery (compliance) · luxury pet stock photography"),
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
        "The Smart Dog & Cat Tag buyer is emotionally loaded. They love their pet, they have already imagined losing them, "
        "and they have a specific complaint about engraved tags — the phone number is permanent and public. "
        "Many also own an AirTag and are looking for the *return channel* the AirTag does not provide.", BODY))
    s.append(Spacer(1, 0.3*cm))

    s.append(Paragraph("Top buying triggers", H3))
    triggers = [
        ("Privacy fear (the SeQR core)", "Engraved tag has their phone number visible. Got a spam call or scary message once. Wants a private alternative."),
        ("Recent scare", "Pet got out, came back, or didn't. The scare made them want better contact-on-collar than a static engraving."),
        ("Multi-pet household", "Dog AND cat (or two dogs). The 2-pack maps perfectly — one tag each, different message per pet."),
        ("AirTag complement", "Already owns an AirTag for the dog. Knows it tells *them* where the dog is — but does not tell the *finder* who to call. SeQR fills that gap."),
        ("Updatability", "Moved house, changed phone number, switched vets. Wants info that updates without buying a new tag."),
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
        ("\"The QR fades or rubs off\"", "#1 negative-review theme. Address head-on: laser-etched (not printed), waterproof acrylic, scratch-resistant. Show in Image #5 + bullet 3 + Q&A."),
        ("\"It's not a GPS tracker\"", "Buyer expected an AirTag and got a contact tag. Reframe BEFORE purchase — Image #3 (mechanism) + Q&A. \"Real-time\" wording must be removed (see compliance warning)."),
        ("\"Tags break / deform\"", "Real complaint. Specify acrylic thickness + steel keyring in bullet 3 and Image #5."),
        ("\"Confusing setup\"", "Show 3-step setup explicitly. \"Scan one of the tags to link the pack — no app required.\""),
        ("\"Need an app (Ring?)\"", "SeQR is a PWA. Finders need no app. Owners install via browser. Address in Q&A."),
        ("\"QR less effective than printed contact info\"", "Counter with the privacy argument — printed info is permanent AND public. Privacy hook in Image #2 owns this."),
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
        "Three concepts test pack-shot, in-use on a dog, and mechanism. Recommend Manage Your Experiments A/B/C test for 4 weeks. "
        "Winner becomes Image #1; the other two move to slots #2 / #6.", BODY))
    s.append(Spacer(1, 0.3*cm))

    options = [
        ("A", "Pack-Shot",
         "Both round acrylic tags (Teal + Pink) side-by-side with steel keyrings visible. Three-quarter angle, slight rim light to catch the QR.",
         "Pack-density hook. Reads \"2 tags · premium · clean\" instantly. Lowest-risk launch baseline.",
         cpt_main_a),
        ("B", "In-Use on Dog Collar",
         "SeQR tag attached to a leather collar, on or near a dog. The tag is the hero; the dog gives emotional context.",
         "Use-context hook. Emotionally loaded — buyer sees their own dog. Strongest for first-time category buyer.",
         cpt_main_b),
        ("C", "Tag + Phone Scan",
         "SeQR tag with a phone hovering over it, scan-frame visible. Shows the whole mechanism in one image.",
         "Mechanism hook. Defuses the #1 misconception (\"I thought it was an AirTag\") before the click.",
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
        "<b>Recommended:</b> Launch with <b>Option B (In-Use on Dog Collar)</b> as Image #1 — emotionally loaded, pet imagery wins on emotion-driven categories. "
        "Prepare A and C as challengers. 4-week A/B/C test via Manage Your Experiments. Winner becomes permanent #1; the other two slot into #2 / #6.", BODY)]],
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
         lambda c, cx, cy: cpt_main_b(c, cx, cy),
         WHITE),
        (2, "Hook · privacy",
         "Don't put your number on your pet's collar.",
         "Split-frame: LEFT a traditional engraved metal tag with a visible phone number — small red ✕. RIGHT a SeQR tag in teal — small green ✓. Same composition the existing KeyTag \"Don't Expose Yourself\" frame uses.",
         cpt_img2,
         SAND),
        (3, "Educate · how it works",
         "Attach · Scan · Message.",
         "Three-panel triptych: (1) Tag clipped to a collar. (2) A finder's phone scanning the tag. (3) The owner's phone showing a chat bubble. 3 steps, no GPS imagery.",
         cpt_img3,
         WHITE),
        (4, "Key benefits · 5 promises",
         "5 reasons SeQR.",
         "Promoted to mobile-visible slot #4. Five icon badges around the central tag: Private messaging · No fees forever · No app for finders · No battery ever · Optional location sharing (finder-attached map link, not real-time GPS). Compliant phrasing throughout.",
         cpt_img4_benefits,
         WHITE),
        (5, "Trust · built for pet life",
         "Waterproof. Scratch-resistant. Laser-etched. Lightweight.",
         "Central tag with four trust badges: water-drop, scratch-test, etched-QR, feather (lightweight). Directly defuses the \"QR fades / tag breaks\" complaints from the reviews.",
         cpt_img5,
         WHITE),
        (6, "Versatility · 2-pack · 2 pets",
         "Two tags. Two pets. Any details. Any time.",
         "Central 2-pack with a dog and cat below — labelled \"Tag 1 · Max\" and \"Tag 2 · Luna\". Highlights different message per tag for multi-pet households. Combines old #4 (versatility) and #6 (customize).",
         cpt_img6,
         SAND),
        (7, "Brand close",
         "Reachable. Private. Free. — Scan to try.",
         "Tighter close: the tag, the pink handwritten \"Scan to try!\" CTA, and the signature line tuned for pets: \"Be findable by the people who want to bring them home.\" A faint paw print sits in negative space.",
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
    s.append(Paragraph("Parent-level — same A+ across SeQR pet tag SKUs.", SUB))

    modules = [
        (1, "Full Image", "Be findable by the people who want to bring them home.",
         "Without being findable by everyone else.", cpt_aplus1, SAND),
        (2, "Carousel (5)", "5 reasons SeQR",
         "Privacy · No fees · No app for finder · No battery · Optional location", cpt_aplus_carousel, WHITE),
        (3, "Full Image", "Attach. Scan. Message. Reunite.",
         "3 steps. Any phone. Any country. No app required for finders.", cpt_aplus3, SAND),
        (4, "Full Image", "Dogs. Cats. Every kind of pet.",
         "Two tags, two pets, two messages. One purchase.", cpt_aplus4, NAVY),
        (5, "Carousel (5)", "Wear anywhere",
         "Collar · Harness · Carrier · Leash · Keyring", cpt_aplus_uses, WHITE),
        (6, "Q&A", "Defuses top objections",
         "Real-time question · QR durability · App-for-finder · Free check · Waterproofing", cpt_aplus_qa, SAND),
        (7, "Comparison", "SeQR vs. engraved / AirTag / GPS collar / generic QR",
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
        ("Does the tag track my pet in real time?",
         "No. SeQR is a passive contact tag, not a tracker. There is no live map and no battery. "
         "When someone finds your pet and scans the QR code, they can send you a private message — and, if they choose, "
         "attach a map link of where they are. You decide what to do next."),
        ("Will the QR code rub off or fade?",
         "No. The QR is laser-etched into waterproof acrylic — not printed. It survives baths, rain, mud, and rough play. "
         "We tested it through three years of simulated daily wear with no loss of scannability."),
        ("Does the finder need to download an app?",
         "No. Anyone with a phone camera can scan and message. No App Store download. No account. "
         "Owners install SeQR as a Progressive Web App from <i>app.seqrcontact.com</i> — no App Store download required either."),
        ("Is it really free? What's the catch?",
         "The messaging service is free. No subscription, no monthly fee, no hidden charges. "
         "Your one-time purchase covers two tags and the service behind them — forever."),
        ("How do I activate the two tags?",
         "Scan one of the tags to link the pack to your account. The second tag links automatically. "
         "Each tag carries its own profile — useful when you have one dog and one cat, or two dogs with different medical notes."),
        ("Can I update the information after I buy?",
         "Yes — any time. Add a new emergency contact, change your phone number, update medical info, attach vet records. "
         "The QR code itself never changes; the profile behind it does."),
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
        ["Feature", "SeQR Smart\nPet Tag", "Engraved\nmetal tag", "AirTag / Tile\n(active tracker)", "GPS collar\n(subscription)", "Generic QR\npet tags"],
        ["Phone-number-free", "Yes", "Usually no", "N/A", "Yes", "Often no"],
        ["Re-customizable after purchase", "Yes (any time)", "No (permanent)", "N/A", "Limited", "Sometimes"],
        ["No battery", "Yes", "Yes", "No (~1 yr)", "No (recharge)", "Yes"],
        ["No app required for finder", "Yes", "Yes", "No (ecosystem)", "No (varies)", "Sometimes"],
        ["Built-in private messaging", "Yes", "No", "No return channel", "Sometimes", "Sometimes (3rd-party)"],
        ["Optional location sharing", "Yes (finder-initiated)", "No", "Live map (different)", "Live map (different)", "Sometimes"],
        ["No subscription", "Yes", "Yes", "Mostly yes", "No (monthly)", "Varies"],
        ["Works internationally", "Yes", "Yes (if # is intl)", "Limited", "Varies", "Sometimes"],
    ]
    comp_tbl = Table(comp, colWidths=[3.2*cm, 2.9*cm, 2.7*cm, 2.7*cm, 2.7*cm, 2.6*cm])
    comp_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), NAVY),
        ("TEXTCOLOR", (0,0), (-1,0), WHITE),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("BACKGROUND", (1,1), (1,-1), HexColor("#E6F6F7")),
        ("FONTNAME", (1,1), (1,-1), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,-1), 7.5),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("LEFTPADDING", (0,0), (-1,-1), 4), ("RIGHTPADDING", (0,0), (-1,-1), 4),
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
        "<b>SeQR Smart Dog &amp; Cat Tag — 2-Pack QR Code Pet ID for Dogs and Cats · Privacy-First Contact Tag · "
        "Waterproof Laser-Etched Acrylic · No Phone Number Exposed · No App for Finders · No Subscription · Customizable</b>", BODY)]],
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
        ("PHONE NUMBER OFF YOUR PET'S COLLAR",
         "When someone finds your dog or cat and scans the QR code, they reach you through the SeQR app — no phone number, email, or address on the tag. "
         "Most people who find your pet want to bring them home. The few who don't can't use your number against you."),
        ("TWO TAGS · TWO PETS · ONE PURCHASE",
         "Tag your dog and your cat. Or two dogs. Different name, different message, different medical notes — each tag carries its own profile. "
         "Update the info anytime — the QR code itself never changes."),
        ("LASER-ETCHED · NOT PRINTED",
         "The QR code is laser-etched into waterproof acrylic — not printed and not screen-printed. It survives baths, rain, mud, dog parks, and rough play. "
         "Steel keyring included; tested across three years of simulated daily wear with no loss of scannability."),
        ("FINDERS DON'T NEED AN APP",
         "Anyone with a phone camera scans the QR code and reaches you. No download. No account. "
         "Works on iPhone, Android, and desktop, in any country your pet might wander into."),
        ("INSTANT SCAN ALERTS · OPTIONAL LOCATION",
         "When someone scans your tag, you're notified the moment it happens. If the finder chooses, they can also attach a map link of where they are — "
         "so you know exactly where to come. No live tracking, no battery, no app — the location only shows up when the finder shares it."),
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
        '<font face="Courier" size="8">dog tag qr code id smart pet identification custom name personalized collar identity cat profile '
        'scan alert acrylic dogtag nametag customizable trackable contact notification waterproof placa identificacion perro '
        'multiple pets vet medical info no subscription free privacy</font>', BODY)]],
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
        "<b>Remove from bullet 3:</b> <i>\"REAL-TIME ALERTS\"</i> → reframe as <i>\"INSTANT SCAN ALERTS\"</i> or <i>\"YOU'RE NOTIFIED THE MOMENT YOUR PET'S TAG IS SCANNED\"</i>. \"Real-time\" reinforces the tracker misconception.",
        "<b>Remove from bullets 3 + 5:</b> <i>\"share GPS location\"</i> and <i>\"view the GPS location they share\"</i> → reframe as <i>\"share a map link\"</i> / <i>\"attach a map link\"</i>. Finder-initiated, optional. Not GPS.",
        "<b>Remove from USP list:</b> <i>\"Instant real-time alerts when scanned\"</i> → <i>\"Instant scan alerts\"</i>.",
        "Soften <i>\"durable\" / \"scratch-resistant\"</i> with the specific spec (acrylic thickness, steel keyring) — brand voice rule: <i>\"Honest about limits.\"</i>",
        "Do not name competitor brands in bullets (\"AirTag\", \"Tile\", \"Ring\"). Keep brand comparison only in A+ Module 7 chart, where compliant.",
    ]:
        s.append(Paragraph("· " + line, BODY))

    # ───── Priority uplifts ─────
    s.append(PageBreak())
    s.append(Paragraph("8 · Priority uplifts (CTR × CVR)", H2)); s.append(HRule())
    pri = [
        ("1", "Rewrite \"real-time\" + \"GPS\" out of bullets 3 + 5 + USPs",
         "Brand-voice violation AND directly causes the #5 negative-review theme (\"not a real-time tracker\"). Highest single-fix on conversion + reviews."),
        ("2", "Run Main Image A/B/C test (recommend B as launch)",
         "Pack-shot vs. dog-with-collar vs. tag-with-phone-scan. 4-week test. Largest CTR lift available."),
        ("3", "Address QR durability head-on in bullet 3 + Image #5",
         "QR-fade is the #1 negative review. Specify laser-etched + waterproof acrylic + steel keyring. Show the laser-etched QR visually."),
        ("4", "Publish A+ Module 6 (Q&A) with 6 voice-aligned answers",
         "Covers \"does it track\", \"will the QR fade\", \"is it free\", \"do finders need an app\". Pre-empts 3-star reviews."),
        ("5", "Publish A+ Module 7 (Comparison Chart)",
         "Makes the price defensible vs. engraved / AirTag / GPS-collar / generic-QR in one frame."),
        ("6", "Lean into multi-pet households in copy + imagery",
         "\"Tag 1 · Max  ·  Tag 2 · Luna\" — the dog+cat angle is underused in current draft and is the natural fit for 2-pack."),
        ("7", "Add Subscribe & Save (free pet-tag re-issue program)",
         "Encourage repeat-purchase as families add pets / move / change vets. Increases AOV + LTV."),
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
