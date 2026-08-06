#!/usr/bin/env python3
"""GSC International — Photogate BeeSpi V (N-00011 · B0C8JV4LDW)
Amazon.com Image Plan Brief — image-plan focused, no Jotti overkill.
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

OUT = "/Users/jonask/Desktop/GSC_Photogate_Brief.pdf"

# ─── GSC palette (extracted from logo) ──────────────────────────────
GSC_GREEN   = HexColor("#4A9B3F")     # primary leaf green
GSC_GREEN_D = HexColor("#2D6A28")     # darker headline green
GSC_BLUE    = HexColor("#1D60AB")     # secondary royal blue
GSC_BLUE_D  = HexColor("#0E3F75")
LCD_TEAL    = HexColor("#5BA9B5")     # BeeSpi V LCD blue-teal
BUTTON_PURP = HexColor("#5E4B8C")     # BeeSpi V button purple
DEVICE_BLK  = HexColor("#1E1E1E")     # device housing dark
ACCENT_Y    = HexColor("#F5C518")     # warning/highlight yellow
WHITE       = HexColor("#FFFFFF")
OFFWHITE    = HexColor("#F7F9F4")
LIGHT_GRN   = HexColor("#E8F3E5")     # light callout bg
LIGHT_BLU   = HexColor("#E5EEF8")
INK         = HexColor("#1A1A1A")
GREY        = HexColor("#6A6A6A")
GREY_L      = HexColor("#C0C0C0")
GREEN_OK    = HexColor("#3FA770")
RED_X       = HexColor("#D24545")

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

def _draw_gsc_logo(c, cx, cy, w=4.0*cm):
    """Stylised GSC + Go Science Crazy wordmark. Font sizes scale by cm-width."""
    wc = w / cm   # cm-units for font sizing
    h = w * 0.18
    c.setFillColor(GSC_GREEN); c.setFont("Helvetica-Bold", wc * 4.2)
    c.drawString(cx - w/2, cy, "GSC")
    c.setFillColor(GSC_GREEN); c.setFont("Helvetica-Bold", wc * 1.8)
    c.drawString(cx - w/2 + w*0.42, cy + h*0.4, "inc.")
    c.setFillColor(GSC_GREEN); c.setFont("Helvetica-Bold", wc * 2.5)
    c.drawString(cx - w/2, cy - h*1.8, "Go")
    c.setFillColor(GSC_BLUE); c.circle(cx - w/2 + w*0.32, cy - h*1.4, w*0.08, fill=1, stroke=0)
    c.setFillColor(GSC_BLUE); c.setFont("Helvetica-Bold", wc * 2.5)
    c.drawString(cx - w/2 + w*0.43, cy - h*1.8, "Science")
    c.setFillColor(GSC_GREEN); c.setFont("Helvetica-Bold", wc * 2.5)
    c.drawString(cx - w/2 + w*1.0, cy - h*1.8, "Crazy")
    # beaker icon
    bx = cx - w/2 + w*1.08; by = cy - h*1.5
    c.setStrokeColor(GSC_BLUE); c.setLineWidth(0.6)
    c.line(bx - w*0.04, by + w*0.10, bx - w*0.04, by - w*0.03)
    c.line(bx + w*0.04, by + w*0.10, bx + w*0.04, by - w*0.03)
    c.line(bx - w*0.04, by + w*0.10, bx + w*0.04, by + w*0.10)
    c.setFillColor(GSC_BLUE); c.rect(bx - w*0.06, by - w*0.05, w*0.12, w*0.05, fill=1, stroke=0)


def _draw_beespi(c, cx, cy, w=3.0*cm, lcd_text="12.45", show_label=True):
    """BeeSpi V Photogate device — black box with LCD + 2 buttons + 2 light gates underneath.
    Font sizes scale by cm-width so they render correctly at any size."""
    wc = w / cm
    h = w * 0.55
    # body (top section)
    c.setFillColor(DEVICE_BLK); c.setStrokeColor(HexColor("#0A0A0A")); c.setLineWidth(0.4)
    c.roundRect(cx - w/2, cy - h*0.10, w, h*0.85, w*0.04, fill=1, stroke=1)
    # legs / arch underneath
    c.setFillColor(DEVICE_BLK)
    c.rect(cx - w/2, cy - h*0.55, w*0.10, h*0.45, fill=1, stroke=0)
    c.rect(cx + w/2 - w*0.10, cy - h*0.55, w*0.10, h*0.45, fill=1, stroke=0)
    # LCD screen
    c.setFillColor(LCD_TEAL); c.setStrokeColor(HexColor("#003344")); c.setLineWidth(0.3)
    c.rect(cx - w*0.18, cy + h*0.18, w*0.36, h*0.30, fill=1, stroke=1)
    # LCD digits
    c.setFillColor(HexColor("#0A2030")); c.setFont("Helvetica-Bold", max(4, wc * 3.5))
    c.drawCentredString(cx, cy + h*0.24, lcd_text)
    # "BeeSpi V" mini label above LCD
    c.setFillColor(WHITE); c.setFont("Helvetica-Bold", max(3, wc * 1.4))
    c.drawCentredString(cx, cy + h*0.58, "BeeSpi V")
    # 2 round buttons
    c.setFillColor(BUTTON_PURP); c.setStrokeColor(HexColor("#1A0F40")); c.setLineWidth(0.4)
    c.circle(cx - w*0.25, cy + h*0.0, w*0.10, fill=1, stroke=1)
    c.circle(cx + w*0.25, cy + h*0.0, w*0.10, fill=1, stroke=1)
    # button labels
    c.setFillColor(WHITE); c.setFont("Helvetica-Bold", max(2.5, wc * 1.0))
    c.drawCentredString(cx - w*0.25, cy + h*0.0 - w*0.03, "START")
    c.drawCentredString(cx + w*0.25, cy + h*0.0 - w*0.03, "SELECT")
    # IR-sensor dots
    c.setFillColor(HexColor("#FF6B6B"))
    c.circle(cx - w*0.40, cy - h*0.40, w*0.02, fill=1, stroke=0)
    c.circle(cx + w*0.40, cy - h*0.40, w*0.02, fill=1, stroke=0)
    if show_label:
        c.setFillColor(GREY); c.setFont("Helvetica", max(3, wc * 1.0))
        c.drawCentredString(cx, cy - h*0.8, "BeeSpi V · N-00011")


def _draw_cart(c, cx, cy, w=1.4*cm, color=HexColor("#A85030")):
    """Lab dynamics cart."""
    h = w * 0.6
    c.setFillColor(color); c.setStrokeColor(HexColor("#3A1A0A")); c.setLineWidth(0.3)
    c.roundRect(cx - w/2, cy - h*0.2, w, h*0.5, 0.04*cm, fill=1, stroke=1)
    # wheels
    c.setFillColor(DEVICE_BLK)
    c.circle(cx - w*0.30, cy - h*0.25, h*0.12, fill=1, stroke=0)
    c.circle(cx + w*0.30, cy - h*0.25, h*0.12, fill=1, stroke=0)


def _draw_pendulum(c, cx, cy, h=1.6*cm, color=HexColor("#A85030")):
    """Pendulum — string + bob."""
    c.setStrokeColor(HexColor("#444")); c.setLineWidth(0.4)
    c.line(cx, cy + h*0.4, cx + h*0.25, cy - h*0.4)
    c.setFillColor(color); c.setStrokeColor(HexColor("#333")); c.setLineWidth(0.3)
    c.circle(cx + h*0.25, cy - h*0.4, h*0.10, fill=1, stroke=1)


def _draw_ball(c, cx, cy, r=0.25*cm, color=HexColor("#D9534F")):
    """Generic ball (rolling/falling object)."""
    c.setFillColor(color); c.setStrokeColor(HexColor("#3A0A0A")); c.setLineWidth(0.3)
    c.circle(cx, cy, r, fill=1, stroke=1)


def _draw_student(c, cx, cy, h=2.2*cm, shirt=GSC_BLUE):
    """Simple student silhouette — head + shirt."""
    # head
    c.setFillColor(HexColor("#E6B8A0")); c.setStrokeColor(HexColor("#8A5A3A")); c.setLineWidth(0.3)
    c.circle(cx, cy + h*0.30, h*0.15, fill=1, stroke=1)
    # hair
    c.setFillColor(HexColor("#3A2818"))
    c.arc(cx - h*0.15, cy + h*0.16, cx + h*0.15, cy + h*0.46, startAng=0, extent=180)
    # shirt
    c.setFillColor(shirt); c.setStrokeColor(HexColor("#003366")); c.setLineWidth(0.3)
    p = c.beginPath()
    p.moveTo(cx - h*0.10, cy + h*0.18)
    p.lineTo(cx - h*0.28, cy - h*0.18)
    p.lineTo(cx - h*0.30, cy - h*0.42)
    p.lineTo(cx + h*0.30, cy - h*0.42)
    p.lineTo(cx + h*0.28, cy - h*0.18)
    p.lineTo(cx + h*0.10, cy + h*0.18)
    p.close()
    c.drawPath(p, fill=1, stroke=1)


def _draw_laptop_x(c, cx, cy, w=1.6*cm):
    """Laptop with a big red X — symbolizes 'no computer needed'."""
    h = w * 0.65
    c.setFillColor(HexColor("#7A7A7A")); c.setStrokeColor(HexColor("#3A3A3A")); c.setLineWidth(0.4)
    # base
    c.rect(cx - w/2, cy - h*0.2, w, h*0.10, fill=1, stroke=1)
    # screen
    c.setFillColor(HexColor("#AABACC"))
    c.roundRect(cx - w*0.40, cy - h*0.10, w*0.80, h*0.45, 0.03*cm, fill=1, stroke=1)
    # big red X
    c.setStrokeColor(RED_X); c.setLineWidth(2.5)
    c.line(cx - w*0.40, cy - h*0.15, cx + w*0.40, cy + h*0.40)
    c.line(cx - w*0.40, cy + h*0.40, cx + w*0.40, cy - h*0.15)


def _draw_check(c, cx, cy, size=0.5*cm, color=GREEN_OK):
    c.setStrokeColor(color); c.setLineWidth(1.6)
    c.line(cx - size*0.3, cy, cx - size*0.05, cy - size*0.25)
    c.line(cx - size*0.05, cy - size*0.25, cx + size*0.3, cy + size*0.3)


def _draw_callout_line(c, x1, y1, x2, y2, color=GSC_BLUE):
    c.setStrokeColor(color); c.setLineWidth(0.6)
    c.line(x1, y1, x2, y2)
    c.setFillColor(color)
    c.circle(x2, y2, 0.06*cm, fill=1, stroke=0)


# ─── Mockup container ──────────────────────────────────────────────

class ListingMockup(Flowable):
    """Square frame with the concept drawing inside + slot/role tags."""
    def __init__(self, slot, role, draw_fn, bg=WHITE):
        self.slot = slot; self.role = role; self.draw_fn = draw_fn; self.bg = bg
        self.size = 7.0*cm
        Flowable.__init__(self)
    def wrap(self, *a): return (self.size, self.size + 0.5*cm)
    def draw(self):
        c = self.canv; s = self.size
        c.setFillColor(self.bg); c.setStrokeColor(HexColor("#CCCCCC")); c.setLineWidth(0.4)
        c.rect(0, 0, s, s, fill=1, stroke=1)
        # slot tag — top-left
        c.setFillColor(GSC_GREEN_D); c.rect(0, s - 0.75*cm, 1.5*cm, 0.75*cm, fill=1, stroke=0)
        c.setFillColor(WHITE); c.setFont("Helvetica-Bold", 12)
        c.drawCentredString(0.75*cm, s - 0.52*cm, f"#{self.slot}")
        # concept drawing
        self.draw_fn(c, s/2, s/2 - 0.2*cm)
        # role tag — bottom-right
        c.setFillColor(GSC_BLUE)
        tw = c.stringWidth(self.role.upper(), "Helvetica-Bold", 7.5) + 0.5*cm
        c.rect(s - tw, 0, tw, 0.6*cm, fill=1, stroke=0)
        c.setFillColor(WHITE); c.setFont("Helvetica-Bold", 7.5)
        c.drawString(s - tw + 0.25*cm, 0.22*cm, self.role.upper())
        # px label
        c.setFillColor(GREY); c.setFont("Helvetica", 6.5)
        c.drawCentredString(s/2, 0.20*cm, "2000 × 2000 px")


# ─── Concept drawings — 7 listing images ────────────────────────────

def cpt_main_hero(c, cx, cy):
    """#1 Hero — BeeSpi V in 3/4 with LCD showing reading + small ball above suggesting motion."""
    # subtle motion-trail behind
    c.setStrokeColor(Color(GSC_BLUE.red, GSC_BLUE.green, GSC_BLUE.blue, alpha=0.25))
    c.setLineWidth(2.0); c.setDash([3, 2])
    c.line(cx - 2.5*cm, cy + 1.2*cm, cx + 2.0*cm, cy + 0.6*cm)
    c.setDash()
    # ball coming in
    _draw_ball(c, cx - 2.4*cm, cy + 1.2*cm, r=0.18*cm, color=HexColor("#D9534F"))
    # device
    _draw_beespi(c, cx, cy - 0.3*cm, w=3.6*cm, lcd_text="12.45")
    # m/s unit label
    c.setFillColor(GSC_BLUE_D); c.setFont("Helvetica-Bold", 9)
    c.drawCentredString(cx + 0.9*cm, cy + 0.13*cm, "m/s")


def cpt_what_it_measures(c, cx, cy):
    """#2 — what it does: velocity + time visualization, cart through gates."""
    # headline strap area
    c.setFillColor(GSC_GREEN_D); c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(cx, cy + 2.6*cm, "INSTANT SPEED.")
    c.drawCentredString(cx, cy + 2.20*cm, "ZERO COMPUTER.")
    # device smaller, bottom
    _draw_beespi(c, cx, cy - 1.4*cm, w=2.6*cm, lcd_text="2.04", show_label=False)
    # cart approaching
    _draw_cart(c, cx - 2.0*cm, cy - 1.05*cm, w=1.0*cm)
    # arrow
    c.setStrokeColor(GSC_GREEN); c.setLineWidth(2.0)
    c.line(cx - 1.3*cm, cy - 0.9*cm, cx - 0.6*cm, cy - 0.9*cm)
    # arrow head
    p = c.beginPath()
    p.moveTo(cx - 0.6*cm, cy - 0.9*cm); p.lineTo(cx - 0.8*cm, cy - 0.7*cm); p.lineTo(cx - 0.8*cm, cy - 1.1*cm); p.close()
    c.setFillColor(GSC_GREEN); c.drawPath(p, fill=1, stroke=0)
    # speed reading callout
    c.setFillColor(LIGHT_GRN); c.setStrokeColor(GSC_GREEN); c.setLineWidth(0.6)
    c.roundRect(cx + 0.6*cm, cy + 0.2*cm, 2.4*cm, 1.0*cm, 0.10*cm, fill=1, stroke=1)
    c.setFillColor(GSC_GREEN_D); c.setFont("Helvetica-Bold", 13)
    c.drawCentredString(cx + 1.8*cm, cy + 0.75*cm, "2.04 m/s")
    c.setFillColor(GREY); c.setFont("Helvetica", 7)
    c.drawCentredString(cx + 1.8*cm, cy + 0.40*cm, "live · on the unit")
    # bottom strap
    c.setFillColor(GREY); c.setFont("Helvetica-Oblique", 6.5)
    c.drawCentredString(cx, cy - 2.5*cm, "Velocity + elapsed time appear on the LCD as the object passes through.")


def cpt_no_computer(c, cx, cy):
    """#3 — vs comparison: BeeSpi V alone (✓) vs. competitor with cables + laptop (✗)."""
    c.setFillColor(GSC_GREEN_D); c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(cx, cy + 2.6*cm, "NO LAPTOP. NO SOFTWARE.")
    c.drawCentredString(cx, cy + 2.25*cm, "NO CABLES.")
    # vs divider
    c.setFillColor(GREY_L); c.rect(cx - 0.04*cm, cy - 1.6*cm, 0.08*cm, 3.2*cm, fill=1, stroke=0)
    c.setFillColor(WHITE); c.setStrokeColor(INK); c.setLineWidth(0.5)
    c.circle(cx, cy + 0.0*cm, 0.4*cm, fill=1, stroke=1)
    c.setFillColor(INK); c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(cx, cy - 0.08*cm, "vs")
    # LEFT: GSC simple
    _draw_beespi(c, cx - 1.6*cm, cy + 0.1*cm, w=2.0*cm, lcd_text="3.21", show_label=False)
    _draw_check(c, cx - 1.6*cm, cy - 1.4*cm, size=0.6*cm)
    c.setFillColor(GSC_GREEN_D); c.setFont("Helvetica-Bold", 7.5)
    c.drawCentredString(cx - 1.6*cm, cy - 2.0*cm, "STANDALONE.")
    c.setFillColor(GREY); c.setFont("Helvetica", 6.5)
    c.drawCentredString(cx - 1.6*cm, cy - 2.30*cm, "Battery + LCD = done.")
    # RIGHT: competitor with laptop + cables
    _draw_laptop_x(c, cx + 1.6*cm, cy + 0.4*cm, w=1.8*cm)
    # cable snaking down
    c.setStrokeColor(GREY); c.setLineWidth(1.2)
    c.bezier(cx + 1.6*cm, cy + 0.1*cm, cx + 2.2*cm, cy - 0.3*cm,
             cx + 1.0*cm, cy - 0.6*cm, cx + 1.6*cm, cy - 1.0*cm)
    c.setFillColor(GREY); c.circle(cx + 1.6*cm, cy - 1.0*cm, 0.10*cm, fill=1, stroke=0)
    c.setStrokeColor(RED_X); c.setLineWidth(1.6)
    c.line(cx + 1.3*cm, cy - 1.7*cm, cx + 1.9*cm, cy - 1.1*cm)
    c.line(cx + 1.3*cm, cy - 1.1*cm, cx + 1.9*cm, cy - 1.7*cm)
    c.setFillColor(HexColor("#7A0F0F")); c.setFont("Helvetica-Bold", 7.5)
    c.drawCentredString(cx + 1.6*cm, cy - 2.0*cm, "OTHER PHOTOGATES.")
    c.setFillColor(GREY); c.setFont("Helvetica", 6.5)
    c.drawCentredString(cx + 1.6*cm, cy - 2.30*cm, "Need a computer + driver.")
    # bottom strap
    c.setFillColor(GREY); c.setFont("Helvetica-Oblique", 6.0)
    c.drawCentredString(cx, cy - 2.8*cm, "Lab time is short. Setup should be too.")


def cpt_use_cases(c, cx, cy):
    """#4 — 5 use cases in a single composite: cart, pendulum, projectile, falling body, collision."""
    c.setFillColor(GSC_GREEN_D); c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(cx, cy + 2.6*cm, "FIVE EXPERIMENTS.")
    c.drawCentredString(cx, cy + 2.25*cm, "ONE SENSOR.")
    # 5 use case icons in a row
    cases = [
        ("CARTS",       cx - 2.4*cm, lambda c2,x,y: _draw_cart(c2, x, y, w=1.0*cm)),
        ("PENDULUMS",   cx - 1.2*cm, lambda c2,x,y: _draw_pendulum(c2, x, y, h=1.1*cm)),
        ("PROJECTILES", cx,          lambda c2,x,y: (_draw_ball(c2, x - 0.3*cm, y, r=0.20*cm),
                                                     _draw_ball(c2, x + 0.0*cm, y + 0.15*cm, r=0.15*cm, color=HexColor("#D9999F")),
                                                     _draw_ball(c2, x + 0.3*cm, y + 0.30*cm, r=0.12*cm, color=HexColor("#E0BBBE")))),
        ("FREE FALL",   cx + 1.2*cm, lambda c2,x,y: (_draw_ball(c2, x, y + 0.40*cm, r=0.20*cm),
                                                      _draw_ball(c2, x, y, r=0.20*cm, color=HexColor("#D9999F")),
                                                      _draw_ball(c2, x, y - 0.40*cm, r=0.20*cm, color=HexColor("#E0BBBE")))),
        ("COLLISIONS",  cx + 2.4*cm, lambda c2,x,y: (_draw_cart(c2, x - 0.30*cm, y, w=0.6*cm),
                                                      _draw_cart(c2, x + 0.30*cm, y, w=0.6*cm, color=HexColor("#3A7AB0")))),
    ]
    for label, x, dfn in cases:
        # icon box
        c.setFillColor(OFFWHITE); c.setStrokeColor(GSC_GREEN); c.setLineWidth(0.5)
        c.roundRect(x - 0.55*cm, cy - 0.4*cm, 1.1*cm, 1.4*cm, 0.08*cm, fill=1, stroke=1)
        dfn(c, x, cy + 0.4*cm)
        c.setFillColor(GSC_GREEN_D); c.setFont("Helvetica-Bold", 5.5)
        c.drawCentredString(x, cy - 0.95*cm, label)
    # device underneath
    _draw_beespi(c, cx, cy - 2.0*cm, w=2.0*cm, lcd_text="1.27", show_label=False)


def cpt_how_it_works(c, cx, cy):
    """#5 — labeled callouts on the device."""
    c.setFillColor(GSC_GREEN_D); c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(cx, cy + 2.6*cm, "BUILT FOR THE CLASSROOM.")
    # device big
    _draw_beespi(c, cx, cy - 0.4*cm, w=3.6*cm, lcd_text="0.97", show_label=False)
    # 4 callouts around it
    callouts = [
        (cx - 3.0*cm, cy + 1.4*cm, cx - 0.7*cm, cy + 0.1*cm,  "LCD DISPLAY",         "Result on the unit"),
        (cx + 3.0*cm, cy + 1.4*cm, cx + 0.9*cm, cy - 0.4*cm,  "DUAL LIGHT GATES",   "Speed + time in one pass"),
        (cx - 3.0*cm, cy - 1.0*cm, cx - 0.7*cm, cy - 0.7*cm,  "START · SELECT",      "Two buttons, six modes"),
        (cx + 3.0*cm, cy - 1.0*cm, cx + 0.7*cm, cy - 1.0*cm,  "5-MEMORY",            "Repeat trials"),
    ]
    for tx, ty, dx, dy, head, sub in callouts:
        _draw_callout_line(c, tx, ty, dx, dy, color=GSC_BLUE)
        c.setFillColor(GSC_BLUE_D); c.setFont("Helvetica-Bold", 7)
        align = "left" if tx > cx else "right"
        if align == "left":
            c.drawString(tx + 0.1*cm, ty + 0.05*cm, head)
            c.setFillColor(GREY); c.setFont("Helvetica", 6)
            c.drawString(tx + 0.1*cm, ty - 0.20*cm, sub)
        else:
            c.drawRightString(tx - 0.1*cm, ty + 0.05*cm, head)
            c.setFillColor(GREY); c.setFont("Helvetica", 6)
            c.drawRightString(tx - 0.1*cm, ty - 0.20*cm, sub)


def cpt_classroom(c, cx, cy):
    """#6 — students in classroom doing the experiment, BeeSpi in front."""
    c.setFillColor(GSC_GREEN_D); c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(cx, cy + 2.6*cm, "FROM FORMULA TO 'AHA!'.")
    # lab bench
    c.setFillColor(HexColor("#D9C9B0")); c.setStrokeColor(HexColor("#7A5A30")); c.setLineWidth(0.3)
    c.rect(cx - 3.0*cm, cy - 1.6*cm, 6.0*cm, 0.4*cm, fill=1, stroke=1)
    # 2 students behind the bench
    _draw_student(c, cx - 1.2*cm, cy + 0.6*cm, h=2.0*cm, shirt=GSC_BLUE)
    _draw_student(c, cx + 1.2*cm, cy + 0.6*cm, h=2.0*cm, shirt=HexColor("#D9534F"))
    # BeeSpi on bench
    _draw_beespi(c, cx, cy - 1.0*cm, w=1.6*cm, lcd_text="4.18", show_label=False)
    # cart approaching
    _draw_cart(c, cx - 1.8*cm, cy - 1.10*cm, w=0.7*cm)
    # bottom strap
    c.setFillColor(GREY); c.setFont("Helvetica-Oblique", 6.5)
    c.drawCentredString(cx, cy - 2.4*cm, "Students see motion they previously only calculated.")


def cpt_specs_brand(c, cx, cy):
    """#7 — tech specs callouts + GSC brand close."""
    c.setFillColor(GSC_GREEN_D); c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(cx, cy + 2.6*cm, "SPEC SHEET")
    # device on the left
    _draw_beespi(c, cx - 1.8*cm, cy + 0.3*cm, w=2.4*cm, lcd_text="99.99", show_label=False)
    # spec list on the right
    specs = [
        ("0–99.99 m/s",       "speed range, multi-unit"),
        ("5 measurements",    "memory storage"),
        ("Dual light gates",  "instant velocity + time"),
        ("Standalone",        "no PC · no software"),
        ("Battery-powered",   "no wall outlet"),
    ]
    for i, (a, b) in enumerate(specs):
        y = cy + 1.4*cm - i*0.55*cm
        c.setFillColor(GSC_GREEN); c.circle(cx + 0.5*cm, y, 0.08*cm, fill=1, stroke=0)
        c.setFillColor(INK); c.setFont("Helvetica-Bold", 8)
        c.drawString(cx + 0.7*cm, y - 0.06*cm, a)
        c.setFillColor(GREY); c.setFont("Helvetica", 7)
        c.drawString(cx + 0.7*cm, y - 0.28*cm, b)
    # GSC brand close at the bottom
    c.setFillColor(GSC_GREEN); c.rect(cx - 3.0*cm, cy - 2.4*cm, 6.0*cm, 0.8*cm, fill=1, stroke=0)
    c.setFillColor(WHITE); c.setFont("Helvetica-Bold", 13)
    c.drawCentredString(cx, cy - 2.10*cm, "GO SCIENCE CRAZY")
    c.setFillColor(WHITE); c.setFont("Helvetica", 7.5)
    c.drawCentredString(cx, cy - 2.32*cm, "Hands-on tools for the classroom · since 2003")


# ─── Page chrome ────────────────────────────────────────────────────

def cover_page(canvas, doc):
    canvas.saveState()
    # split bg: top green band, bottom white
    canvas.setFillColor(GSC_GREEN); canvas.rect(0, PAGE_H - 5*cm, PAGE_W, 5*cm, fill=1, stroke=0)
    canvas.setFillColor(GSC_BLUE); canvas.rect(0, PAGE_H - 5.3*cm, PAGE_W, 0.3*cm, fill=1, stroke=0)
    # GSC logo top-left in white
    canvas.setFillColor(WHITE); canvas.setFont("Helvetica-Bold", 38)
    canvas.drawString(ML, PAGE_H - 2.6*cm, "GSC")
    canvas.setFont("Helvetica-Bold", 14)
    canvas.drawString(ML + 3.0*cm, PAGE_H - 2.2*cm, "inc.")
    canvas.setFillColor(WHITE); canvas.setFont("Helvetica", 14)
    canvas.drawString(ML, PAGE_H - 3.4*cm, "Go Science Crazy")
    # title block
    canvas.setFillColor(GSC_GREEN_D); canvas.setFont("Helvetica-Bold", 32)
    canvas.drawString(ML, PAGE_H - 7.5*cm, "Photogate BeeSpi V")
    canvas.setFillColor(INK); canvas.setFont("Helvetica", 14)
    canvas.drawString(ML, PAGE_H - 8.2*cm, "Self-contained dual-light-gate sensor · N-00011")
    canvas.setStrokeColor(GSC_GREEN); canvas.setLineWidth(0.5)
    canvas.line(ML, PAGE_H - 8.7*cm, ML + 8*cm, PAGE_H - 8.7*cm)
    canvas.setFillColor(GSC_BLUE); canvas.setFont("Helvetica-Bold", 14)
    canvas.drawString(ML, PAGE_H - 9.5*cm, "Amazon.com — Image Plan Brief")
    canvas.setFillColor(GREY); canvas.setFont("Helvetica", 11)
    canvas.drawString(ML, PAGE_H - 10.1*cm, "Buyer psychology · 7 listing images · A+ outline · Master copy")

    # meta row
    y = 3.4*cm
    fields = [("BRAND", "GSC International"), ("MARKET", "Amazon.com"), ("ASIN", "B0C8JV4LDW"), ("DATE", "2026-05-25")]
    for i, (k, v) in enumerate(fields):
        x = ML + i * 4.4*cm
        canvas.setFillColor(GSC_GREEN_D); canvas.setFont("Helvetica-Bold", 8)
        canvas.drawString(x, y, k)
        canvas.setFillColor(INK); canvas.setFont("Helvetica", 11)
        canvas.drawString(x, y - 0.55*cm, v)

    # hero device on the right
    _draw_beespi(canvas, PAGE_W - MR - 4.5*cm, PAGE_H - 13*cm, w=5.5*cm, lcd_text="12.45")
    canvas.setFillColor(GSC_GREEN_D); canvas.setFont("Helvetica-Oblique", 10)
    canvas.drawString(ML, PAGE_H - 14.5*cm, "Make physics visible. In 0.01 seconds.")

    # bottom strap
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
    canvas.drawString(ML + 1.2*cm, PAGE_H - 0.7*cm, "Photogate BeeSpi V — Amazon.com Image Plan")
    canvas.drawRightString(PAGE_W - MR, PAGE_H - 0.7*cm, f"Page {doc.page}")
    canvas.setStrokeColor(HexColor("#E0DCC8")); canvas.setLineWidth(0.4)
    canvas.line(ML, MB - 0.4*cm, PAGE_W - MR, MB - 0.4*cm)
    canvas.setFillColor(GREY); canvas.setFont("Helvetica", 7.5)
    canvas.drawString(ML, MB - 0.7*cm, "Prepared by EQUALICE — 2026-05-25 · Go Science Crazy")
    canvas.restoreState()


# ─── Build ──────────────────────────────────────────────────────────

def build():
    doc = BaseDocTemplate(OUT, pagesize=A4,
                          leftMargin=ML, rightMargin=MR,
                          topMargin=MT, bottomMargin=MB,
                          title="GSC Photogate BeeSpi V — Amazon.com Image Plan",
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
        ["Product",        "Photogate BeeSpi V (N-00011) — self-contained dual-light-gate sensor"],
        ["Brand",          "GSC International · Go Science Crazy"],
        ["ASIN",           "B0C8JV4LDW · Amazon.com"],
        ["Use cases",      "Velocity · elapsed time · acceleration calc · pendulum · projectile · free-fall · collisions"],
        ["Target group",   "High-school + college physics teachers · STEM labs · homeschool · students 15+"],
        ["Buyer = User?",  "Often NO. Teacher / school buys; student uses. Brief must satisfy both at once."],
        ["Hero USP",       "Velocity reading appears <b>directly on the LCD in seconds</b> — no computer, no software, no data logger."],
        ["Top KWs (SV)",   "experiment (1,779) · lab equipment (792) · projectile launcher (551) · lab timer (443) · physics experiment"],
        ["Pos. reviews",   "Instant measurement · easy setup · no computer · improves student engagement · 5-memory helpful"],
        ["Neg. reviews",   "Limited advanced features · accuracy edge cases · plastic build · battery dependency"],
        ["Brand brief notes", "Engaging for students 15+ · creative freedom 5/5 · must be school-appropriate · NO childish toys aesthetic"],
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
        "<b>Strategic read.</b> The buyer is a teacher with five minutes between classes — they need to see in one image that "
        "this device <b>just works</b> (no laptop, no setup). The user is a student who needs the result <b>to be visible</b>. "
        "Both wins live in the first three frames: hero shows the LCD with a real reading · frame 2 shows it measuring · "
        "frame 3 contrasts \"standalone\" against \"competitor with cables + laptop\". After that the brief sells use-case breadth, "
        "engineering trust, and classroom belonging.", BODY)]],
        colWidths=[CW])
    strat.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), GSC_GREEN_D),
        ("TEXTCOLOR", (0,0), (-1,-1), WHITE),
        ("LEFTPADDING", (0,0), (-1,-1), 14), ("RIGHTPADDING", (0,0), (-1,-1), 14),
        ("TOPPADDING", (0,0), (-1,-1), 10), ("BOTTOMPADDING", (0,0), (-1,-1), 10),
    ]))
    s.append(strat)

    # ───── Buyer Psychology + KW + Review Map ─────
    s.append(PageBreak())
    s.append(Paragraph("Who buys this — and what makes them click", H2)); s.append(HRule())
    persona = [
        ("Physics teacher (high school)",
         "5–25 years on the job. Tight lab budget. Has tried photogates that needed a computer — and watched 30 students stand around waiting for drivers to install. Buys equipment that <b>survives 30 sets of teenage hands</b>, sets up in under 60 seconds, and produces a number on a screen."),
        ("STEM lab coordinator (college)",
         "Equips a freshman physics or engineering lab. Buys in batches of 5–10. Cares about <b>repeatable measurements + spec sheet</b>. Lab manuals reference NGSS or AP Physics standards — match where possible."),
        ("Homeschool parent (advanced)",
         "Teaches a 15–18-year-old serious physics. Buys 1 unit. Needs <b>no-software</b> simplicity AND credible measurement. Reads every Q&A before buying."),
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
        ["Theme (verbatim)",                            "Sentiment",  "How the image plan answers it"],
        ["\"Instant speed measurement\"",                "POS",        "Frame #1 — LCD shows \"12.45 m/s\" right on the unit"],
        ["\"Easy setup, no computer required\"",         "POS",        "Frame #3 — vs. competitor with laptop + cables"],
        ["\"Improves student engagement\"",              "POS",        "Frame #6 — students at the bench, engaged"],
        ["\"5-memory function helpful\"",                "POS",        "Frame #5 — callout: \"5-MEMORY · Repeat trials\""],
        ["\"Limited advanced features\"",                "NEG",        "Frame #4 — show 5 distinct experiment types covered"],
        ["\"Plastic build feels basic\"",                "NEG",        "Frame #7 — material spec + range numbers reframe as \"engineered for daily lab use\""],
        ["\"Battery dependency\"",                       "NEG",        "Frame #7 — \"Battery-powered: no wall outlet\" as positive"],
    ]
    rt = Table([[Paragraph(c, SMALL if i > 0 else BODY) for c in r] for i, r in enumerate(rev)],
               colWidths=[5.4*cm, 1.6*cm, CW - 7.0*cm])
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
    s.append(Paragraph("Top KWs (Helium-10) → where they live in the listing", H3))
    kws = [
        ["KW",                            "SV",       "Used in"],
        ["experiment",                    "1,779",    "Title · Bullet 1 · Image #4 (use cases) · A+ Module 1"],
        ["lab equipment",                 "792",      "Title · Bullet 4 (build trust) · Image #7"],
        ["projectile launcher",           "551",      "Image #4 use-case · backend"],
        ["friction labs",                 "526",      "A+ use-case module · backend"],
        ["science lab equipment",         "524",      "Title · Bullet 4 · backend"],
        ["lab timer",                     "443",      "Image #5 callout · A+ module · backend"],
        ["kinetic labs",                  "443",      "Backend · A+"],
        ["lap timer",                     "371",      "Backend"],
        ["air tracks / air track",        "328 / 14,232", "Use-case mention only — air track is competitive but adjacent"],
    ]
    kw_tbl = Table([[Paragraph(c, SMALL if i > 0 else BODY) for c in r] for i, r in enumerate(kws)],
                   colWidths=[5.0*cm, 1.8*cm, CW - 6.8*cm])
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
        "Each frame is 2000 × 2000 px · sRGB · JPG · ≤ 5 MB. Mockup left, concept + headline + benefit + product proof right. "
        "Headlines are <b>final</b> — pasted into Figma exactly as below.", SUB))

    listing = [
        (1, "HERO",
         "(no overlay — Amazon main-image rule. White BG.)",
         "Device shown in three-quarter, LCD glowing with a real reading (\"12.45\"). A small red ball mid-flight above the gate hints at motion — implies what the device is FOR without breaking the white-BG rule.",
         "Sets up the click: this is a SPEED sensor, the screen shows the number, no setup needed. Beats every competitor that shows the device as a static black box.",
         cpt_main_hero, WHITE),
        (2, "HOOK · WHAT IT MEASURES",
         "INSTANT SPEED. ZERO COMPUTER.",
         "Cart enters from the left, passes the dual gates, BeeSpi's LCD updates to \"2.04 m/s\". Green call-out box magnifies the reading.",
         "Frame answers the first three questions a teacher asks: <i>What does it measure? How fast does it report? Do I need software?</i> in one image.",
         cpt_what_it_measures, OFFWHITE),
        (3, "PROOF · NO COMPUTER NEEDED",
         "NO LAPTOP. NO SOFTWARE. NO CABLES.",
         "Split frame. LEFT: BeeSpi alone with green ✓ and \"STANDALONE\". RIGHT: competitor with a laptop + tangled cable, big red ✕, \"OTHER PHOTOGATES need a computer + driver\".",
         "Directly attacks the largest CVR objection in the category. Teachers have all been burned by photogates that need lab-computer drivers — this frame eliminates that worry pre-purchase.",
         cpt_no_computer, WHITE),
        (4, "BREADTH · 5 EXPERIMENTS",
         "FIVE EXPERIMENTS. ONE SENSOR.",
         "Five icon tiles in a row: Carts · Pendulums · Projectiles · Free fall · Collisions. BeeSpi sits beneath with a reading.",
         "Defuses the negative review \"limited advanced features\" by showing physical experiment breadth. Hits high-volume KWs (\"projectile launcher\", \"friction labs\") via icon labels.",
         cpt_use_cases, OFFWHITE),
        (5, "HOW IT WORKS · LABELED CALLOUTS",
         "BUILT FOR THE CLASSROOM.",
         "Device large, with 4 blue call-out lines pointing to: LCD DISPLAY · DUAL LIGHT GATES · START · SELECT · 5-MEMORY. Each label gets a 6-word benefit caption.",
         "Standard \"explain the product\" frame. Crucial for the lab-coordinator buyer who needs to know what the unit DOES technically before committing.",
         cpt_how_it_works, WHITE),
        (6, "LIFESTYLE · CLASSROOM",
         "FROM FORMULA TO 'AHA!'.",
         "Two students at a lab bench, BeeSpi between them, a cart on the rail. One student looks at the LCD, one watches the cart. Both engaged.",
         "Answers the brand brief explicitly: <i>\"engaging for students 15+\"</i>. Sells the emotional outcome (student engagement) to the teacher-buyer.",
         cpt_classroom, OFFWHITE),
        (7, "SPECS + BRAND",
         "SPEC SHEET — and the GSC promise.",
         "5-line spec sheet with green dots: 0–99.99 m/s · 5 memories · Dual gates · Standalone · Battery. Green GSC brand bar at the bottom: \"GO SCIENCE CRAZY · Hands-on tools for the classroom.\"",
         "Closes on credibility. Teachers need to forward a spec to procurement — this image is screenshot-ready. Brand bar earns repeat-purchases when they come back for the dissection kit / next product.",
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

    # ───── A+ Premium Outline ─────
    s.append(PageBreak())
    s.append(Paragraph("A+ Premium Content — 7 Modules", H2)); s.append(HRule())
    s.append(Paragraph(
        "Parent-level A+. Each module either expands a listing image into a full-bleed banner, "
        "or adds depth the listing image can't (Q&A · comparison chart · trust strip).", SUB))
    modules = [
        ("Module 1 · Premium Full Image",
         "BRING MOTION INTO VIEW.",
         "Wide hero banner. Lab bench at golden hour. BeeSpi center, cart on rail, two students leaning in. GSC wordmark top-left."),
        ("Module 2 · Carousel (5 tiles)",
         "FIVE EXPERIMENTS. ONE SENSOR.",
         "Five carousel tiles, one per experiment type. Each tile: tiny icon + one-sentence application + measured-value example."),
        ("Module 3 · Premium Full Image",
         "NO COMPUTER. NO CABLES. NO WAITING.",
         "Wide banner that expands listing image #3. BeeSpi running on its own next to a closed laptop with a small \"not needed\" tag."),
        ("Module 4 · Premium Full Image",
         "EVERY TRIAL. RECORDED.",
         "Macro of the LCD showing reading #1, #2, #3, #4, #5 sequentially — illustrating the 5-memory function across repeated trials."),
        ("Module 5 · Carousel (4 tiles)",
         "WHO USES BEESPI V.",
         "High-school lab · College freshman physics · STEM after-school program · Homeschool. Each tile: one image + 1-line use-case + a teacher / instructor quote."),
        ("Module 6 · Q&A",
         "TEACHER QUESTIONS, ANSWERED.",
         "5–6 Q&A pairs: Does it need a computer? · Can it measure acceleration? · What's the unit range? · Battery life? · Replacement parts? · NGSS alignment."),
        ("Module 7 · Comparison Chart",
         "BEESPI V vs. PHOTOGATES THAT NEED A COMPUTER.",
         "Four columns: BeeSpi V (highlighted) · PASCO photogate · Vernier go!motion · Generic Amazon photogate. Rows: setup time · computer required · cost · memory · classroom-ready."),
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
        "<b>GSC International Photogate Timer N-00011 BeeSpi V — Self-Contained Dual-Light-Gate Speed Sensor for Physics Lab Experiments · "
        "Carts · Pendulums · Projectiles · Free Fall · No Computer · No Software · 5-Memory · LCD Display</b>", BODY)]],
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
        ("INSTANT SPEED ON THE UNIT — NO COMPUTER REQUIRED",
         "The BeeSpi V is a self-contained photogate timer that displays velocity and elapsed time directly on its built-in LCD. "
         "No laptop, no driver install, no software. Set up in under 60 seconds and start measuring."),
        ("FIVE EXPERIMENTS · ONE SENSOR",
         "Use the same unit for carts on a track, pendulums, projectiles, free-falling objects, and collision experiments. "
         "Dual light gates measure speed (0–99.99 m/s) and elapsed time as objects pass through the sensor."),
        ("5-MEMORY · REPEATED TRIALS BUILT IN",
         "Stores up to 5 measurements per session — students can compare results, calculate averages, and check repeatability "
         "without writing every number down. Multiple unit options for flexibility across lab manuals."),
        ("BUILT FOR THE CLASSROOM — TESTED BY STUDENTS",
         "Battery-powered, portable, and engineered for daily classroom use. No wall outlet, no cables to trip over, "
         "no chance of a Windows update killing your lab plan. Drop into any STEM, AP Physics, or college freshman lab."),
        ("HANDS-ON SCIENCE FROM GO SCIENCE CRAZY",
         "GSC International builds dependable, easy-to-deploy science equipment for educators. The Photogate BeeSpi V helps "
         "students directly see motion — turning textbook formulas (v = d/t, KE = ½mv²) into measurable, classroom-ready results. "
         "NOT A TOY: educational/scientific use; ages 15+, adult supervision required."),
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
        '<font face="Courier" size="8">photogate timer light gate sensor physics lab equipment motion experiment velocity '
        'speed timer kinetic energy acceleration projectile launcher free fall pendulum collision dual gate beespi narika '
        'stem ngss apparatus dynamics cart air track lap timer scientific classroom homeschool</font>', BODY)]],
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
        ("1", "Shoot the hero (#1) with LCD on + ball in flight",
         "Highest single CTR lift. The image must read \"speed sensor with screen on\" at 200×200 px thumbnail."),
        ("2", "Build the vs-frame (#3) early",
         "Defuses the #1 buyer worry (\"will it need a computer?\") before they ever click into the listing. Single biggest CVR fix."),
        ("3", "Title rewrite — lead with PHOTOGATE TIMER + BeeSpi V",
         "Current title is buried. \"Photogate timer\" + \"BeeSpi V\" cover the brand + KW intent in the first 80 chars."),
        ("4", "5-Memory + use-case carousel (Image #4 + A+ Module 2)",
         "Direct response to the \"limited features\" negative review — show breadth, not depth."),
        ("5", "Vine + post-launch review push",
         "Reviews currently mention plastic build and battery dependency — both can be reframed (\"engineered for daily lab use\") in seed-reviews."),
        ("6", "Q&A — pre-seed 6 questions",
         "Teachers buying for procurement read every Q&A. Pre-seed: computer? · acceleration? · range? · battery life? · ages? · NGSS?"),
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
        "Is the BeeSpi V Narika-licensed exclusively to GSC International for US distribution? If yes, that's a useful trust note.",
        "Battery type + included? Confirm so we can put it in bullets / Q&A.",
        "Tolerance / accuracy spec (e.g. ± 1% of reading) — confirm so we can answer the \"accuracy edge cases\" review honestly.",
        "Is there an NGSS / AP Physics alignment doc we can reference?",
        "Replacement parts availability — useful as a Q&A answer.",
    ]:
        s.append(Paragraph("· " + line, BODY))

    doc.build(s)
    print(f"PDF: {OUT}")


if __name__ == "__main__":
    build()
