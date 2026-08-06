#!/usr/bin/env python3
"""SeQR Contact — Lost Item Labels (B0D3VQBY8N · 24-pack QR stickers)
Image Plan + A+ Premium PDF brief.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (
    Paragraph, Spacer, PageBreak, Table, TableStyle,
    KeepTogether, Frame, BaseDocTemplate, PageTemplate, NextPageTemplate
)
from reportlab.platypus.flowables import Flowable

OUT = '/Users/jonask/Desktop/SeQR Lost Item Labels — Image Plan.pdf'

# SeQR brand palette (extracted from existing Luggage/KeyTag designs)
TEAL    = HexColor('#1AAEB6')   # Primary
NAVY    = HexColor('#0F2944')   # Headlines, frames
PINK    = HexColor('#E8345C')   # CTA accent (e.g. "Scan to try!")
YELLOW  = HexColor('#F4C040')   # Background accent
SAND    = HexColor('#F2EDE2')   # Soft cream BG
RED_X   = HexColor('#D24545')   # "Wrong way" callout
GREEN_OK= HexColor('#3FA770')   # "Right way" callout
INK     = HexColor('#111111')
GREY    = HexColor('#666666')
LIGHT   = HexColor('#F5F5F5')
WHITE   = HexColor('#FFFFFF')
WARN_BG = HexColor('#FFF4E5')

PAGE_W, PAGE_H = A4
MARGIN_L, MARGIN_R, MARGIN_T, MARGIN_B = 1.6*cm, 1.6*cm, 1.8*cm, 1.6*cm
CONTENT_W = PAGE_W - MARGIN_L - MARGIN_R

styles = getSampleStyleSheet()
H1 = ParagraphStyle('H1', parent=styles['Title'], fontName='Helvetica-Bold',
                    fontSize=26, leading=30, textColor=NAVY, spaceAfter=4, alignment=TA_LEFT)
SUB = ParagraphStyle('SUB', parent=styles['Normal'], fontName='Helvetica',
                     fontSize=11, leading=14, textColor=GREY, spaceAfter=14)
H2 = ParagraphStyle('H2', parent=styles['Heading2'], fontName='Helvetica-Bold',
                    fontSize=18, leading=22, textColor=NAVY, spaceBefore=14, spaceAfter=8)
H3 = ParagraphStyle('H3', parent=styles['Heading3'], fontName='Helvetica-Bold',
                    fontSize=12, leading=15, textColor=INK, spaceBefore=10, spaceAfter=4)
BODY = ParagraphStyle('Body', parent=styles['Normal'], fontName='Helvetica',
                      fontSize=10, leading=14, textColor=INK, spaceAfter=4)
SMALL = ParagraphStyle('Small', parent=BODY, fontSize=9, leading=12, textColor=GREY)
QUOTE = ParagraphStyle('Quote', parent=BODY, fontName='Helvetica-Oblique', textColor=GREY)
LABEL = ParagraphStyle('Label', parent=BODY, fontSize=9, fontName='Helvetica-Bold', textColor=NAVY)


# ---------- Flowables ----------

class HRule(Flowable):
    def __init__(self, width=None, color=TEAL, thickness=1.4):
        self.width = width or CONTENT_W
        self.color = color
        self.thickness = thickness
        Flowable.__init__(self)
    def wrap(self, *a): return (self.width, self.thickness + 6)
    def draw(self):
        self.canv.setStrokeColor(self.color)
        self.canv.setLineWidth(self.thickness)
        self.canv.line(0, 3, self.width, 3)


class ColorChip(Flowable):
    def __init__(self, hex_color, label_top, label_bottom, w=3.6*cm, h=2.0*cm):
        self.color = HexColor(hex_color) if isinstance(hex_color, str) else hex_color
        self.label_top = label_top
        self.label_bottom = label_bottom
        self.w = w; self.h = h
        Flowable.__init__(self)
    def wrap(self, *a): return (self.w, self.h + 0.9*cm)
    def draw(self):
        c = self.canv
        c.setFillColor(self.color)
        c.setStrokeColor(HexColor('#DDDDDD'))
        c.setLineWidth(0.3)
        c.rect(0, 0.9*cm, self.w, self.h, fill=1, stroke=1)
        c.setFillColor(INK); c.setFont('Helvetica-Bold', 9)
        c.drawString(0, 0.45*cm, self.label_top)
        c.setFillColor(GREY); c.setFont('Helvetica', 8)
        c.drawString(0, 0.15*cm, self.label_bottom)


def _wrap_text(canv, text, max_w, font, size, max_lines):
    if not text: return []
    words = text.split(); lines = []; cur = ''
    for w in words:
        trial = (cur + ' ' + w).strip()
        if canv.stringWidth(trial, font, size) > max_w:
            if cur: lines.append(cur)
            cur = w
        else: cur = trial
    if cur: lines.append(cur)
    return lines[:max_lines]


def _draw_sticker_sheet(c, cx, cy, w=2.2*cm, h=2.6*cm, color=TEAL):
    """Draw a stylized sticker SHEET (multiple QR stickers visible)."""
    # Backing paper
    c.setFillColor(WHITE); c.setStrokeColor(NAVY); c.setLineWidth(0.6)
    c.rect(cx - w/2, cy - h/2, w, h, fill=1, stroke=1)
    # Grid of mini QR squares (4x6 = 24 stickers)
    rows, cols = 6, 4
    pad = 0.06*cm
    cell_w = (w - 2*pad - (cols-1)*0.04*cm) / cols
    cell_h = (h - 2*pad - (rows-1)*0.04*cm) / rows
    for r in range(rows):
        for col in range(cols):
            x = cx - w/2 + pad + col*(cell_w + 0.04*cm)
            y = cy - h/2 + pad + r*(cell_h + 0.04*cm)
            c.setFillColor(color)
            c.rect(x, y, cell_w, cell_h, fill=1, stroke=0)
            # Mini QR pattern
            c.setFillColor(WHITE)
            for dx in [0.02, 0.04, 0.06]:
                c.rect(x + dx*cm, y + 0.02*cm, 0.012*cm, 0.012*cm, fill=1, stroke=0)
                c.rect(x + dx*cm, y + cell_h - 0.04*cm, 0.012*cm, 0.012*cm, fill=1, stroke=0)


def _draw_single_sticker(c, cx, cy, w=1.2*cm, h=1.2*cm, color=TEAL, with_label=True):
    """Draw one single QR sticker."""
    c.setFillColor(color); c.setStrokeColor(NAVY); c.setLineWidth(0.4)
    c.roundRect(cx - w/2, cy - h/2, w, h, 0.1*cm, fill=1, stroke=1)
    # QR pattern
    c.setFillColor(WHITE)
    qr_size = w * 0.6
    qr_x = cx - qr_size/2; qr_y = cy - qr_size/2
    c.rect(qr_x, qr_y, qr_size, qr_size, fill=1, stroke=0)
    # 3 corner squares
    c.setFillColor(NAVY)
    cs = qr_size * 0.25
    c.rect(qr_x, qr_y + qr_size - cs, cs, cs, fill=1, stroke=0)
    c.rect(qr_x + qr_size - cs, qr_y + qr_size - cs, cs, cs, fill=1, stroke=0)
    c.rect(qr_x, qr_y, cs, cs, fill=1, stroke=0)
    # noise dots
    for nx, ny in [(0.4, 0.4), (0.55, 0.45), (0.45, 0.6), (0.6, 0.55)]:
        c.rect(qr_x + nx*qr_size, qr_y + ny*qr_size, qr_size*0.1, qr_size*0.1, fill=1, stroke=0)


def _draw_phone(c, cx, cy, w=1.6*cm, h=2.6*cm):
    """Stylized smartphone with a QR scan frame."""
    c.setFillColor(NAVY); c.setStrokeColor(NAVY); c.setLineWidth(0.5)
    c.roundRect(cx - w/2, cy - h/2, w, h, 0.15*cm, fill=1, stroke=1)
    # Screen
    c.setFillColor(WHITE)
    c.roundRect(cx - w/2 + 0.08*cm, cy - h/2 + 0.25*cm, w - 0.16*cm, h - 0.5*cm, 0.05*cm, fill=1, stroke=0)
    # Camera scan frame (teal corners)
    c.setStrokeColor(TEAL); c.setLineWidth(1.2)
    sx = cx - w*0.3; sy = cy - h*0.2; ss = w*0.6
    # 4 corner brackets
    bl = 0.15*cm
    # bottom-left
    c.line(sx, sy, sx + bl, sy)
    c.line(sx, sy, sx, sy + bl)
    # bottom-right
    c.line(sx + ss, sy, sx + ss - bl, sy)
    c.line(sx + ss, sy, sx + ss, sy + bl)
    # top-left
    c.line(sx, sy + ss, sx + bl, sy + ss)
    c.line(sx, sy + ss, sx, sy + ss - bl)
    # top-right
    c.line(sx + ss, sy + ss, sx + ss - bl, sy + ss)
    c.line(sx + ss, sy + ss, sx + ss, sy + ss - bl)


class MainImageOption(Flowable):
    """3 Main Image OPTIONS — concept sketches."""
    def __init__(self, letter, concept_name, composition_desc, ctr_pitch, draw_fn, side_w=8.5*cm):
        self.letter = letter; self.concept = concept_name
        self.desc = composition_desc; self.pitch = ctr_pitch
        self.draw_fn = draw_fn
        self.size = 6.5*cm; self.side_w = side_w; self.gap = 0.4*cm
        self.total_w = self.size + self.gap + self.side_w
        Flowable.__init__(self)
    def wrap(self, *a): return (self.total_w, self.size + 0.5*cm)
    def draw(self):
        c = self.canv; s = self.size
        c.setFillColor(WHITE); c.setStrokeColor(HexColor('#CCCCCC')); c.setLineWidth(0.4)
        c.rect(0, 0, s, s, fill=1, stroke=1)
        c.setFillColor(NAVY); c.rect(0, s - 0.7*cm, 1.3*cm, 0.7*cm, fill=1, stroke=0)
        c.setFillColor(WHITE); c.setFont('Helvetica-Bold', 12)
        c.drawCentredString(0.65*cm, s - 0.5*cm, f'OPT {self.letter}')
        # concept-specific drawing
        self.draw_fn(c, s/2, s/2 - 0.3*cm)
        c.setFillColor(GREY); c.setFont('Helvetica', 7)
        c.drawCentredString(s/2, 0.15*cm, '2000 × 2000 px · Pure white BG')
        c.setFillColor(TEAL)
        tag_w = c.stringWidth(self.concept.upper(), 'Helvetica-Bold', 7) + 0.4*cm
        c.rect(s - tag_w, 0, tag_w, 0.5*cm, fill=1, stroke=0)
        c.setFillColor(WHITE); c.setFont('Helvetica-Bold', 7)
        c.drawString(s - tag_w + 0.2*cm, 0.18*cm, self.concept.upper())


def _draw_opt_a(c, cx, cy):
    """Sticker sheet centered (full pack visible)."""
    _draw_sticker_sheet(c, cx, cy, w=3.4*cm, h=4.0*cm, color=TEAL)


def _draw_opt_b(c, cx, cy):
    """Sticker sheet + single sticker stuck on a phone/water bottle/passport silhouette."""
    # Sticker sheet (smaller, left)
    _draw_sticker_sheet(c, cx - 1.5*cm, cy + 0.2*cm, w=2.2*cm, h=2.6*cm, color=TEAL)
    # Object: passport silhouette
    c.setFillColor(NAVY); c.setStrokeColor(NAVY)
    c.roundRect(cx + 0.3*cm, cy - 1.6*cm, 1.8*cm, 2.4*cm, 0.1*cm, fill=1, stroke=1)
    c.setFillColor(YELLOW); c.setFont('Helvetica-Bold', 6)
    c.drawCentredString(cx + 1.2*cm, cy + 0.4*cm, 'PASSPORT')
    # Sticker on the passport
    _draw_single_sticker(c, cx + 1.2*cm, cy - 0.6*cm, w=0.8*cm, h=0.8*cm, color=PINK)
    # arrow connecting sheet → object
    c.setStrokeColor(TEAL); c.setLineWidth(1.2)
    c.line(cx - 0.3*cm, cy + 0.2*cm, cx + 0.3*cm, cy - 0.1*cm)


def _draw_opt_c(c, cx, cy):
    """Sheet + finder scanning a sticker with a phone."""
    # Sticker sheet (top-left)
    _draw_sticker_sheet(c, cx - 1.4*cm, cy + 0.8*cm, w=1.8*cm, h=2.2*cm, color=TEAL)
    # Single large sticker on a "lost item" surface (book)
    c.setFillColor(SAND); c.setStrokeColor(GREY); c.setLineWidth(0.4)
    c.rect(cx - 0.5*cm, cy - 1.8*cm, 2.0*cm, 1.4*cm, fill=1, stroke=1)
    _draw_single_sticker(c, cx + 0.5*cm, cy - 1.1*cm, w=1.0*cm, h=1.0*cm, color=PINK)
    # Phone scanning it
    _draw_phone(c, cx + 1.7*cm, cy - 1.0*cm, w=1.3*cm, h=2.2*cm)


# ---------- Mockup classes ----------

class ListingImage(Flowable):
    """7 Listing Image mockups."""
    def __init__(self, slot, role, bg, headline, sub, draw_fn=None, side_w=8.5*cm):
        self.slot = slot; self.role = role
        self.bg = HexColor(bg) if isinstance(bg, str) else bg
        self.headline = headline; self.sub = sub
        self.draw_fn = draw_fn
        self.size = 6.5*cm; self.side_w = side_w; self.gap = 0.4*cm
        self.total_w = self.size + self.gap + self.side_w
        Flowable.__init__(self)
    def wrap(self, *a): return (self.total_w, self.size + 0.5*cm)
    def draw(self):
        c = self.canv; s = self.size
        c.setFillColor(self.bg); c.setStrokeColor(HexColor('#CCCCCC')); c.setLineWidth(0.4)
        c.rect(0, 0, s, s, fill=1, stroke=1)
        c.setFillColor(NAVY); c.rect(0, s - 0.7*cm, 1.4*cm, 0.7*cm, fill=1, stroke=0)
        c.setFillColor(WHITE); c.setFont('Helvetica-Bold', 11)
        c.drawCentredString(0.7*cm, s - 0.5*cm, f'#{self.slot}')
        c.setFillColor(GREY); c.setFont('Helvetica', 7)
        c.drawCentredString(s/2, 0.15*cm, '2000 × 2000 px')

        if self.draw_fn:
            self.draw_fn(c, s/2, s/2)

        if self.headline:
            text_color = WHITE if self.bg in (NAVY, TEAL, PINK) else NAVY
            c.setFillColor(text_color)
            c.setFont('Helvetica-Bold', 10)
            lines = _wrap_text(c, self.headline.upper(), s - 0.8*cm, 'Helvetica-Bold', 10, 3)
            y = s - 1.6*cm
            for line in lines:
                c.drawCentredString(s/2, y, line); y -= 12
            if self.sub:
                c.setFont('Helvetica-Oblique', 7.5)
                c.setFillColor(GREY if self.bg in (WHITE, SAND, LIGHT, YELLOW) else WHITE)
                sub_lines = _wrap_text(c, self.sub, s - 0.8*cm, 'Helvetica-Oblique', 7.5, 2)
                yy = y - 4
                for sl in sub_lines:
                    c.drawCentredString(s/2, yy, sl); yy -= 9

        c.setFillColor(TEAL)
        role_w = c.stringWidth(self.role.upper(), 'Helvetica-Bold', 7) + 0.4*cm
        c.rect(s - role_w, 0, role_w, 0.5*cm, fill=1, stroke=0)
        c.setFillColor(WHITE); c.setFont('Helvetica-Bold', 7)
        c.drawString(s - role_w + 0.2*cm, 0.18*cm, self.role.upper())


class APlusMockup(Flowable):
    def __init__(self, slot, mtype, headline, sub, bg=SAND, side_w=7.5*cm):
        self.slot = slot; self.mtype = mtype
        self.headline = headline; self.sub = sub; self.bg = bg
        self.banner_w = 9.5*cm
        self.banner_h = 9.5*cm * (600/1464)
        self.side_w = side_w; self.gap = 0.4*cm
        self.total_w = self.banner_w + self.gap + self.side_w
        Flowable.__init__(self)
    def wrap(self, *a): return (self.total_w, self.banner_h + 0.5*cm)
    def draw(self):
        c = self.canv; w, h = self.banner_w, self.banner_h
        c.setFillColor(self.bg); c.setStrokeColor(HexColor('#CCCCCC')); c.setLineWidth(0.4)
        c.rect(0, 0.5*cm, w, h, fill=1, stroke=1)
        c.setFillColor(NAVY); c.rect(0, 0.5*cm + h - 0.55*cm, 2.6*cm, 0.55*cm, fill=1, stroke=0)
        c.setFillColor(WHITE); c.setFont('Helvetica-Bold', 8)
        c.drawString(0.15*cm, 0.5*cm + h - 0.4*cm, f'MODULE {self.slot}')

        text_color = WHITE if self.bg in (NAVY, TEAL, PINK) else NAVY
        c.setFillColor(text_color); c.setFont('Helvetica-Bold', 11)
        if self.headline:
            lines = _wrap_text(c, self.headline.upper(), w - 1*cm, 'Helvetica-Bold', 11, 2)
            y = 0.5*cm + h/2 + (len(lines)-1)*6 + 0.2*cm
            for line in lines:
                c.drawCentredString(w/2, y, line); y -= 13
            if self.sub:
                c.setFont('Helvetica-Oblique', 8)
                c.setFillColor(GREY if self.bg in (WHITE, SAND, LIGHT, YELLOW) else WHITE)
                sub_lines = _wrap_text(c, self.sub, w - 1*cm, 'Helvetica-Oblique', 8, 1)
                yy = 0.5*cm + h/2 - len(lines)*6 - 4
                for sl in sub_lines:
                    c.drawCentredString(w/2, yy, sl)

        c.setFillColor(TEAL)
        type_w = c.stringWidth(self.mtype.upper(), 'Helvetica-Bold', 7) + 0.3*cm
        c.rect(w - type_w, 0.5*cm, type_w, 0.4*cm, fill=1, stroke=0)
        c.setFillColor(WHITE); c.setFont('Helvetica-Bold', 7)
        c.drawString(w - type_w + 0.15*cm, 0.5*cm + 0.13*cm, self.mtype.upper())
        c.setFillColor(GREY); c.setFont('Helvetica', 6.5)
        c.drawCentredString(w/2, 0.15*cm, '1464 × 600 desktop · 600 × 450 mobile')


# ---------- Page chrome ----------

def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(TEAL); canvas.setLineWidth(2.5)
    canvas.line(MARGIN_L, PAGE_H - 1.0*cm, PAGE_W - MARGIN_R, PAGE_H - 1.0*cm)
    canvas.setFillColor(NAVY); canvas.setFont('Helvetica-Bold', 9)
    canvas.drawString(MARGIN_L, PAGE_H - 0.7*cm, 'SeQR Contact')
    canvas.setFillColor(GREY); canvas.setFont('Helvetica', 8)
    canvas.drawString(MARGIN_L + 1.9*cm, PAGE_H - 0.7*cm, 'Lost Item Labels (24-pack QR Stickers) · Amazon US Brief')
    canvas.setFillColor(GREY); canvas.setFont('Helvetica', 8)
    canvas.drawRightString(PAGE_W - MARGIN_R, PAGE_H - 0.7*cm, f'Page {doc.page}')
    canvas.setStrokeColor(HexColor('#E0DCC8')); canvas.setLineWidth(0.4)
    canvas.line(MARGIN_L, MARGIN_B - 0.4*cm, PAGE_W - MARGIN_R, MARGIN_B - 0.4*cm)
    canvas.setFillColor(GREY); canvas.setFont('Helvetica', 7.5)
    canvas.drawString(MARGIN_L, MARGIN_B - 0.7*cm, 'Prepared by EQUALICE — 2026-05-06 · ASIN B0D3VQBY8N')
    canvas.restoreState()


def cover_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(SAND); canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    canvas.setFillColor(TEAL); canvas.rect(0, PAGE_H - 4*cm, PAGE_W, 4*cm, fill=1, stroke=0)
    canvas.setFillColor(NAVY); canvas.rect(0, PAGE_H - 4.4*cm, PAGE_W, 0.4*cm, fill=1, stroke=0)
    canvas.setFillColor(WHITE); canvas.setFont('Helvetica-Bold', 38)
    canvas.drawString(MARGIN_L, PAGE_H - 2.6*cm, 'SeQR')
    canvas.setFont('Helvetica', 16); canvas.setFillColor(WHITE)
    canvas.drawString(MARGIN_L, PAGE_H - 3.4*cm, 'Lost Item Labels · 24-Pack QR Smart Stickers')
    canvas.setFillColor(NAVY); canvas.setFont('Helvetica-Bold', 22)
    canvas.drawString(MARGIN_L, PAGE_H - 7*cm, 'Amazon US Image Plan')
    canvas.setFillColor(GREY); canvas.setFont('Helvetica', 13)
    canvas.drawString(MARGIN_L, PAGE_H - 7.8*cm, '3 Main Image Options · 7 Listing Images · A+ Premium · CTR Boost')

    y = 5*cm
    canvas.setFillColor(NAVY); canvas.setFont('Helvetica-Bold', 9)
    canvas.drawString(MARGIN_L, y, 'ASIN')
    canvas.drawString(MARGIN_L + 4.5*cm, y, 'CATEGORY')
    canvas.drawString(MARGIN_L + 9*cm, y, 'PACK')
    canvas.drawString(MARGIN_L + 15.2*cm, y, 'DATE')
    canvas.setFillColor(INK); canvas.setFont('Helvetica', 11)
    canvas.drawString(MARGIN_L, y - 0.55*cm, 'B0D3VQBY8N')
    canvas.drawString(MARGIN_L + 4.5*cm, y - 0.55*cm, 'QR Lost & Found')
    canvas.drawString(MARGIN_L + 9*cm, y - 0.55*cm, '24 stickers · 1" × 0.75"')
    canvas.drawString(MARGIN_L + 15.2*cm, y - 0.55*cm, '2026-05-06')

    canvas.setFillColor(NAVY); canvas.rect(0, 0, PAGE_W, 1.4*cm, fill=1, stroke=0)
    canvas.setFillColor(TEAL); canvas.setFont('Helvetica-Bold', 10)
    canvas.drawString(MARGIN_L, 0.5*cm, 'BE FINDABLE BY THE PEOPLE WHO WANT TO HELP YOU.')
    canvas.setFillColor(WHITE); canvas.setFont('Helvetica', 9)
    canvas.drawRightString(PAGE_W - MARGIN_R, 0.5*cm, 'Prepared by EQUALICE')
    canvas.restoreState()


# ---------- Build ----------

def build():
    doc = BaseDocTemplate(OUT, pagesize=A4,
                          leftMargin=MARGIN_L, rightMargin=MARGIN_R,
                          topMargin=MARGIN_T, bottomMargin=MARGIN_B,
                          title='SeQR Lost Item Labels — Image Plan',
                          author='EQUALICE')
    cover_frame = Frame(MARGIN_L, MARGIN_B, CONTENT_W, PAGE_H - MARGIN_T - MARGIN_B,
                        leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, showBoundary=0)
    body_frame = Frame(MARGIN_L, MARGIN_B, CONTENT_W, PAGE_H - MARGIN_T - MARGIN_B,
                       leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, showBoundary=0)
    doc.addPageTemplates([
        PageTemplate(id='Cover', frames=[cover_frame], onPage=cover_page),
        PageTemplate(id='Body', frames=[body_frame], onPage=header_footer),
    ])

    story = []
    # Cover page is drawn entirely by `cover_page` callback. Spacer just gives the frame content.
    story.append(Spacer(1, PAGE_H - MARGIN_T - MARGIN_B - 2))
    story.append(NextPageTemplate('Body'))
    story.append(PageBreak())

    # ============ AT A GLANCE ============
    story.append(Paragraph('At a glance', H2))
    story.append(HRule())
    glance = [
        ['Brand', 'SeQR Contact — privacy-first QR contact tags & labels'],
        ['Product', 'Lost Item Labels — 24-pack of customizable QR code smart stickers · 1" × 0.75"'],
        ['ASIN', 'B0D3VQBY8N · amazon.com'],
        ['Use case', 'Stick on personal items (passports, wallets, water bottles, electronics, kids\' toys, moving boxes). When found, the finder scans the code and can message you privately — no phone number exposed.'],
        ['Hero buyer trigger', '"I lost my [bag / passport / kid\'s lunchbox] last month. I need a way to be reachable that doesn\'t put my phone number on a sticker."'],
        ['Top competitors (from your Excel)', 'Totescan (B07LF3XPLJ) · Mabel\'s Labels · generic QR sticker brands (B0CTS4LG4M, B08997FG26)'],
        ['Brand voice (per brand-voice doc)', 'Warm + practical + plainspoken. Quiet realism. "We\'ve got you" not "submit a ticket". Short sentences. Numbered steps for instructions.'],
    ]
    t = Table([[Paragraph(f'<b>{k}</b>', BODY), Paragraph(v, BODY)] for k, v in glance],
              colWidths=[4.0*cm, CONTENT_W - 4.0*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), SAND),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LINEBELOW', (0,0), (-1,-1), 0.3, HexColor('#E0DCC8')),
        ('LEFTPADDING', (0,0), (-1,-1), 8), ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 6), ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t)

    # ============ COMPLIANCE WARNING — GPS LANGUAGE ============
    story.append(Spacer(1, 0.5*cm))
    warn_box = Table([[Paragraph(
        '<b>⚠ BRAND VOICE COMPLIANCE — GPS / LOCATION LANGUAGE</b><br/><br/>'
        'The current bullet 8 reads: <i>"GPS LOCATION SHARING FOR QUICK RECOVERY … real-time location sharing, ideal for recovering lost tags quickly."</i> '
        'This <b>directly violates the SeQR brand voice doc</b>, which lists as "things we never say": <i>"Real-time GPS tracking", "Track your bag", "Active tracker", "live location"</i>. '
        '<br/><br/>'
        'The actual mechanism — per your brand voice doc — is: <i>"location sharing is manual, finder-initiated, and depends on the finder\'s device."</i> '
        'When a finder scans the sticker, they can <b>optionally</b> share their location with you (a Google Maps link generated from their phone\'s permission). '
        'The owner does not see a live map. The tag is passive. <br/><br/>'
        '<b>Reframed copy used in this brief:</b> <i>"FINDERS CAN SHARE WHERE THEY ARE — Optional. When someone scans your sticker, they can attach a map link so you know where to pick up your item. No live tracking, no battery, no app to install."</i> '
        'This stays compliant with the brand voice and Amazon\'s claim rules and is more accurate to what the product actually does.', BODY)]],
        colWidths=[CONTENT_W])
    warn_box.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), WARN_BG),
        ('BOX', (0,0), (-1,-1), 1.2, HexColor('#B5390A')),
        ('LEFTPADDING', (0,0), (-1,-1), 14), ('RIGHTPADDING', (0,0), (-1,-1), 14),
        ('TOPPADDING', (0,0), (-1,-1), 12), ('BOTTOMPADDING', (0,0), (-1,-1), 12),
    ]))
    story.append(warn_box)

    # ============ BRANDBOOK ============
    story.append(PageBreak())
    story.append(Paragraph('1 · Brandbook (extracted from existing designs + brand voice doc)', H2))
    story.append(HRule())

    story.append(Paragraph('Color palette', H3))
    chips = [
        ColorChip(TEAL, '#1AAEB6', 'Primary — SeQR Teal'),
        ColorChip(NAVY, '#0F2944', 'Headline — Deep Navy'),
        ColorChip(PINK, '#E8345C', 'Accent CTA — Coral Pink'),
        ColorChip(SAND, '#F2EDE2', 'Background — Soft Cream'),
    ]
    story.append(Table([chips], colWidths=[CONTENT_W/4]*4,
                       style=TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),
                                         ('LEFTPADDING',(0,0),(-1,-1),0),
                                         ('RIGHTPADDING',(0,0),(-1,-1),6)])))

    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph('Typography', H3))
    story.append(Paragraph('Sans-serif used in existing Luggage / KeyTag designs: <b>bold rounded sans-serif</b> (close to Avenir Next / Nunito Sans / Manrope) for headlines · regular weight for body. ALL CAPS only for image-overlay headlines and badges.', BODY))

    story.append(Paragraph('Voice rules (verbatim from brand voice doc)', H3))
    voice_rules = [
        'Warm and calm, never dramatic. Losing things is stressful enough.',
        'Practical over clever. Clarity beats wordplay.',
        'Numbered steps for instructions. Plain English everywhere else.',
        'Confident but not preachy. The "superhero" idea is a gentle undercurrent, never a lecture.',
        'Honest about limits. No "never lose anything again". No "real-time GPS tracking". No "guaranteed returns".',
    ]
    for r in voice_rules:
        story.append(Paragraph('• ' + r, BODY))

    story.append(Spacer(1, 0.2*cm))
    sig = Table([[Paragraph(
        '<b>Signature line:</b> <i>"Most people who find your bag want to help you get it back — we just make sure the few who don\'t can\'t use it against you."</i>', BODY)]],
        colWidths=[CONTENT_W])
    sig.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), TEAL),
        ('TEXTCOLOR', (0,0), (-1,-1), WHITE),
        ('LEFTPADDING', (0,0), (-1,-1), 12), ('RIGHTPADDING', (0,0), (-1,-1), 12),
        ('TOPPADDING', (0,0), (-1,-1), 10), ('BOTTOMPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(sig)

    # Visual style notes from existing designs
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph('Visual style (from existing Luggage Tag + KeyTag designs)', H3))
    style_notes = [
        '<b>Cards on cream BG.</b> The KeyTag set uses #F2EDE2 sand background with rounded white cards. Replicate.',
        '<b>Step-by-step format.</b> 3-panel triptych ("If your keys are found... / They scan your tag... / You get them back!") is a proven layout — reuse for stickers.',
        '<b>Red ✕ vs. green ✓ comparisons.</b> Existing "Dead end. Can\'t return." vs. "Scan. Message. Return." pattern is strong — works perfectly for stickers vs. write-on labels.',
        '<b>4-icon trust strip.</b> "Privacy Protection · Instant Scan Alerts · Privacy Messaging · GPS Sharing" footer band — keep, but rename "GPS Sharing" → "Location Sharing" (compliance).',
        '<b>Real-life lifestyle.</b> Coffee shop, hands holding the tag — gritty, real. Continue with passport, water bottle, kid\'s lunchbox lifestyle for stickers.',
        '<b>Scribble accent in pink.</b> "Scan to try!" handwritten arrow in pink (#E8345C) is a recurring CTA element. Reuse on at least one image.',
    ]
    for n in style_notes:
        story.append(Paragraph('• ' + n, BODY))

    # ============ BUYER PSYCHOLOGY ============
    story.append(PageBreak())
    story.append(Paragraph('2 · Buyer Psychology', H2))
    story.append(HRule())
    story.append(Paragraph(
        'The Lost Item Labels buyer is different from the Luggage / Pet / Key buyer. They have <b>many small things</b> they want to protect — passports, water bottles, kids\' lunchboxes, AirPods cases, electronics, moving boxes — and they want one solution that scales. They\'ve thought about writing their phone number on a label and decided against it. They\'ve maybe used Mabel\'s Labels before but those don\'t solve the contact problem. And they don\'t want another tracker subscription.', BODY))
    story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph('Top buying triggers', H3))
    triggers = [
        ('Privacy fear (the SeQR core)', 'Already tried writing a phone number on a luggage tag. Got a spam call. Won\'t do that again.'),
        ('"I have a lot of small things to protect"', '24 stickers solves passport + wallet + water bottle + AirPods + iPad + 2 kids\' lunchboxes + moving boxes — all in one purchase. Bulk math wins.'),
        ('Tracker fatigue', 'Already owns or has tried AirTags / Tile. Knows the battery limit. Knows there\'s no return channel for the finder. Wants the missing piece.'),
        ('"What about my partner / family member?"', 'Multi-user access shows up in every product\'s support inbox. Surface that this works for households (label your kid\'s, your partner\'s, your parent\'s items).'),
        ('Free / no subscription anxiety check', 'Buyer expects a hidden monthly fee somewhere. Reassure clearly.'),
    ]
    t = Table([[Paragraph(f'<b>{k}</b>', BODY), Paragraph(v, BODY)] for k, v in triggers],
              colWidths=[5.0*cm, CONTENT_W - 5.0*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), TEAL),
        ('TEXTCOLOR', (0,0), (0,-1), WHITE),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LINEBELOW', (0,0), (-1,-1), 0.3, HexColor('#E0DCC8')),
        ('LEFTPADDING', (0,0), (-1,-1), 8), ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 7), ('BOTTOMPADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(t)

    story.append(Spacer(1, 0.4*cm))
    story.append(Paragraph('Friction points to defuse', H3))
    frictions = [
        ('"Where is my bag — I thought it tracked it!"', '#1 misconception per the brand voice doc. SeQR is a passive contact channel, not a live map. Set the expectation in image #2 and A+ Module 6 Q&A.'),
        ('"How do I activate 24 stickers?"', 'Buyers worry it\'s 24× the work. The answer: scan ONE sticker on the sheet to bulk-link them all. This is a hidden delight — surface it visually in image #4.'),
        ('"Will the sticker survive the dishwasher / rain / sun?"', 'Real concern for water bottles and outdoor items. Image #5 shows the durability matrix.'),
        ('"Where is the app? It\'s not in the App Store."', 'Recurring support question. SeQR is a Progressive Web App — finders need NO app, owners install via the browser. Address in A+ Q&A.'),
    ]
    t = Table([[Paragraph(f'<b>{k}</b>', BODY), Paragraph(v, BODY)] for k, v in frictions],
              colWidths=[6.0*cm, CONTENT_W - 6.0*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), HexColor('#FBE5E8')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LINEBELOW', (0,0), (-1,-1), 0.3, HexColor('#E0DCC8')),
        ('LEFTPADDING', (0,0), (-1,-1), 8), ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 7), ('BOTTOMPADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(t)

    # ============ MAIN IMAGE — 3 OPTIONS ============
    story.append(PageBreak())
    story.append(Paragraph('3 · Main Image — 3 Options for CTR Test', H2))
    story.append(HRule())
    story.append(Paragraph(
        'Amazon main-image rules: pure white background (#FFFFFF), no overlay text. The 3 options below test 3 different click hooks — pack-density vs. use-context vs. mechanism. '
        'Recommend running them as a Manage Your Experiments A/B/C test for 4 weeks. Whichever wins becomes Image #1 — the other two move to Image #2 / #5 candidates.', BODY))
    story.append(Spacer(1, 0.3*cm))

    options = [
        ('A', 'Pack-Density',
         'The full sticker SHEET (24 stickers visible) centered on pure white, three-quarter angle, slight rim light to make the teal-and-white QR pattern pop. Bottom edge slightly out of frame to suggest there are even more. Subtle contact shadow.',
         'Pack-density hook. The buyer reads "lots of stickers for the price" in 1 second. Best for shoppers comparing 4-pack vs. 24-pack listings — instantly signals value. Lowest-risk baseline. Recommend launch with this.',
         _draw_opt_a),
        ('B', 'Sheet + Item-in-Use',
         'Sticker sheet on the left side of frame. To its right, ONE sticker stuck on a passport (or a water bottle / luggage handle / lunchbox). A subtle teal arrow connects sheet → applied sticker.',
         'Use-context hook. Tells the buyer "this is what you\'ll do with them" before they read the title. Wins for the buyer who isn\'t sure what these are for. Slightly riskier in main-image compliance — Amazon prefers ultra-clean — but proven pattern in the category.',
         _draw_opt_b),
        ('C', 'Sheet + Phone Scanning',
         'Sticker sheet upper-left. Lower-right: one sticker on a kid\'s lunchbox or notebook. A phone is mid-scan over the sticker, with a teal scan-frame visible on the phone screen.',
         'Mechanism hook. Shows the WHOLE thing in one image — sticker + scan + phone. Strongest for the buyer who doesn\'t yet understand SeQR (the #1 misconception per brand voice: "I thought it was like an AirTag"). Highest education ROI per click. Slightly busiest of the three.',
         _draw_opt_c),
    ]
    for letter, name, desc, pitch, draw_fn in options:
        story.append(Paragraph(f'Option {letter} — {name}', H3))
        mockup = MainImageOption(letter, name, desc, pitch, draw_fn)
        side = [
            Paragraph(f'<b>Composition:</b> {desc}', BODY),
            Spacer(1, 0.15*cm),
            Paragraph(f'<b>CTR pitch:</b> <i>{pitch}</i>', QUOTE),
        ]
        side_block = Table([[s] for s in side], colWidths=[CONTENT_W - mockup.size - mockup.gap])
        side_block.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),
                                        ('LEFTPADDING',(0,0),(-1,-1),0),
                                        ('RIGHTPADDING',(0,0),(-1,-1),0)]))
        row = Table([[mockup, side_block]],
                    colWidths=[mockup.size + mockup.gap, CONTENT_W - mockup.size - mockup.gap])
        row.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),
                                 ('LEFTPADDING',(0,0),(-1,-1),0),
                                 ('RIGHTPADDING',(0,0),(-1,-1),0)]))
        story.append(KeepTogether([row]))
        story.append(Spacer(1, 0.4*cm))

    story.append(Spacer(1, 0.2*cm))
    rec_box = Table([[Paragraph(
        '<b>Recommended ship-now sequence:</b> Launch with <b>Option A</b> as Image #1 (lowest-risk, value-density baseline). '
        'In parallel, prepare B and C as variants. Run A/B/C via Amazon Manage Your Experiments for 4 weeks. '
        'Promote the winner to permanent Image #1; the other two become Images #2 / #5 in the gallery — they\'re still strong assets.', BODY)]],
        colWidths=[CONTENT_W])
    rec_box.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), YELLOW),
        ('LEFTPADDING', (0,0), (-1,-1), 12), ('RIGHTPADDING', (0,0), (-1,-1), 12),
        ('TOPPADDING', (0,0), (-1,-1), 10), ('BOTTOMPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(rec_box)

    # ============ 7 LISTING IMAGES ============
    story.append(PageBreak())
    story.append(Paragraph('4 · Seven Listing Images (full set)', H2))
    story.append(HRule())
    story.append(Paragraph('Format for all: 2000 × 2000 px · sRGB · JPG · ≤ 5 MB. The 3 main-image options above feed Slot #1.', SUB))

    images = [
        (1, 'Click trigger', WHITE, '', '',
         'See "Main Image — 3 Options" above. Test A/B/C; ship the winner. Other two go to Slots #2 / #5.',
         'Three CTR concepts staged as a Manage Your Experiments test. Winner becomes the permanent main image.'),
        (2, 'Hook — privacy', NAVY, 'Don\'t put your number on a sticker.',
         'Stick a SeQR code instead. Reachable when it counts. Private the rest of the time.',
         'Split-frame: LEFT a generic write-on label with a (blurred / partially obscured) phone number — desaturated, with a small red ✕. RIGHT a SeQR sticker in teal — saturated, with a small green ✓. Both stuck on the same item (e.g. a lunchbox).',
         'Reverses the buyer\'s #1 fear (phone-number exposure) with the SeQR alternative in one frame. Mirrors the existing "Dead end. Can\'t return." vs. "Scan. Message. Return." layout used on KeyTag.'),
        (3, 'Educate — how it works', SAND, 'They scan. You get a message. You decide what to share.',
         '3 steps. No app required for the finder. Works on any phone.',
         'Three-panel triptych in the existing KeyTag style: (1) Hand placing a SeQR sticker on a passport — caption "Stick it on anything you don\'t want to lose." (2) A finder\'s phone scanning the sticker — caption "Anyone who finds it scans the code." (3) Owner\'s phone showing a chat bubble — caption "You get a message — your number stays private."',
         'Defuses the #1 misconception ("I thought it was like an AirTag") by showing the actual mechanism in 3 steps. Mirrors the existing KeyTag step layout for brand consistency.'),
        (4, 'Versatility — 24 things to protect', SAND, '24 stickers. Endless things to protect.',
         'Tag passports, water bottles, electronics, kids\' toys, moving boxes, gym gear — all from one pack.',
         'Top-down flat lay on warm cream BG. The 24-sticker sheet centered. Around it: 8–10 real items each with a SeQR sticker on them — passport, AirPods case, water bottle, kid\'s lunchbox, gym bag, moving box, iPad, USB stick, water-color set, hard drive, transit card, set of keys.',
         'Solves the "what do I use 24 stickers for?" question instantly. Shows the bulk-math value visually. Justifies the price vs. 4-pack alternatives.'),
        (5, 'Durability — survives real life', WHITE, 'Tear-proof. Waterproof. Dishwasher-safe.',
         '1" × 0.75" stickers built for daily wear, weather, and washing.',
         'Four-quadrant icon grid on white BG. Each quadrant shows one durability test with a small icon: water drop / wash machine / sun / scratch-test. Sticker survives all four. Center: a clean SeQR sticker.',
         'Defuses the #1 sticker objection ("will it stick / survive?"). Builds confidence in long-term value.'),
        (6, 'Bulk activation — the hidden delight', SAND, 'Activate the whole pack in one scan.',
         'One scan to link all 24 stickers to your account. Customize each one later if you want.',
         'Phone hovering over a sticker on the sheet, with a teal scan frame on the screen. Below, a row of 24 sticker icons all turning teal-checked simultaneously, with a connecting curve from the phone scan to the row.',
         'Defuses the "do I have to activate 24 stickers separately?" friction. Surfaces a hidden product delight that buyers don\'t expect.'),
        (7, 'Brand close — privacy + free + global', NAVY, 'Reachable. Private. Free. Forever.',
         'No subscription. No battery. No app required for finders. Works in any country, on any phone.',
         'Wide environmental shot on dark navy BG. SeQR sticker centered with 4 trust badges around it: NO SUBSCRIPTION · NO BATTERY · NO APP REQUIRED FOR FINDERS · WORKS WORLDWIDE. Subtle world-map graphic in the BG, very low opacity.',
         'Closes on the four uncopyable lines. Mirrors the brand voice: "be findable by the people who want to help you, without being findable by everyone else."'),
    ]
    for slot, role, bg, hl, sub, vis, why in images:
        story.append(Paragraph(f'Image {slot} — {role}', H3))
        mockup = ListingImage(slot, role, bg, hl, sub)
        side = []
        if hl: side.append(Paragraph(f'<b>Headline:</b> {hl}', BODY))
        if sub: side.append(Paragraph(f'<b>Subline:</b> {sub}', BODY))
        side.append(Paragraph(f'<b>Visual:</b> {vis}', BODY))
        side.append(Spacer(1, 0.15*cm))
        side.append(Paragraph(f'<i>Why it works:</i> {why}', QUOTE))
        side_block = Table([[s] for s in side], colWidths=[CONTENT_W - mockup.size - mockup.gap])
        side_block.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),
                                        ('LEFTPADDING',(0,0),(-1,-1),0),
                                        ('RIGHTPADDING',(0,0),(-1,-1),0)]))
        row = Table([[mockup, side_block]],
                    colWidths=[mockup.size + mockup.gap, CONTENT_W - mockup.size - mockup.gap])
        row.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),
                                 ('LEFTPADDING',(0,0),(-1,-1),0),
                                 ('RIGHTPADDING',(0,0),(-1,-1),0)]))
        story.append(KeepTogether([row]))
        story.append(Spacer(1, 0.45*cm))

    # ============ A+ MODULES ============
    story.append(PageBreak())
    story.append(Paragraph('5 · A+ Premium Content (7 Modules)', H2))
    story.append(HRule())
    story.append(Paragraph('Variant-agnostic — same A+ ships across every SeQR sticker / label SKU. SKU-specific facts surface in Module 5 (family carousel) and Module 7 (comparison chart).', SUB))

    modules = [
        (1, 'Full Image', 'Be findable by the people who want to help you.',
         'Without being findable by everyone else.',
         TEAL,
         'Hero brand banner. Hands placing a SeQR sticker on a passport, warm cream BG, brand logo top-left. Mobile crop tightens to hands and sticker.'),
        (2, 'Carousel (5 tiles)', 'The SeQR Difference',
         'No phone number · No app for finder · No battery · No subscription · Re-customizable',
         WHITE,
         'Five icon tiles, identical layout: privacy / device / battery / dollar-sign / pencil. One-line headline + one-line body each.'),
        (3, 'Full Image', 'Stick. Scan. Message. Return.',
         '3 steps for any finder, on any phone, anywhere in the world.',
         SAND,
         'Three-panel horizontal layout repeating the Image #3 logic but at A+ banner size. Numbered 1 / 2 / 3 in teal circles.'),
        (4, 'Full Image', 'One pack. Everything you don\'t want to lose.',
         'Passports · water bottles · kids\' toys · electronics · moving boxes · gym gear.',
         NAVY,
         'Wide grid lifestyle shot — multiple items on a wood surface, each with a SeQR sticker. Warm side light, real life.'),
        (5, 'Carousel (5 tiles)', 'The SeQR Family',
         'Lost Item Labels (this) · Iron-on Tags · Luggage Tags · Smart Pet Tags · Smart Keychain',
         WHITE,
         'Same lighting and angle across all 5 tiles. Color-coded teal accent per SKU.'),
        (6, 'Q&A', 'Defuses top objections',
         'Tracking expectation · App location · Free check · Activation · Durability',
         SAND,
         'Five Q&A pairs — see the table below for the full text.'),
        (7, 'Comparison Chart', 'Why SeQR vs. write-on / engraved / AirTag',
         'Privacy · Re-customizable · Battery · App for finder · Subscription · Return channel',
         WHITE,
         'Highlight the SeQR column with subtle teal tint and a navy "RECOMMENDED" ribbon. See the table on the next page.'),
    ]
    for slot, mtype, hl, sub, bg, desc in modules:
        story.append(Paragraph(f'Module {slot} — {mtype}', H3))
        mockup = APlusMockup(slot, mtype, hl, sub, bg)
        side = [
            Paragraph(f'<b>Headline:</b> {hl}', BODY),
            Paragraph(f'<b>Theme:</b> {sub}', BODY),
            Paragraph(f'<b>Visual:</b> {desc}', BODY),
        ]
        side_block = Table([[s] for s in side], colWidths=[CONTENT_W - mockup.banner_w - mockup.gap])
        side_block.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),
                                        ('LEFTPADDING',(0,0),(-1,-1),0),
                                        ('RIGHTPADDING',(0,0),(-1,-1),0)]))
        row = Table([[mockup, side_block]],
                    colWidths=[mockup.banner_w + mockup.gap, CONTENT_W - mockup.banner_w - mockup.gap])
        row.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),
                                 ('LEFTPADDING',(0,0),(-1,-1),0),
                                 ('RIGHTPADDING',(0,0),(-1,-1),0)]))
        story.append(KeepTogether([row]))
        story.append(Spacer(1, 0.4*cm))

    # Q&A + Comparison detail
    story.append(PageBreak())
    story.append(Paragraph('A+ Module 6 — Q&amp;A (full copy, voice-aligned)', H3))
    qa = [
        ('Where is my item — can the app track it?',
         'No. SeQR is a passive contact tag, not a tracker. There is no live map. When someone finds your item and scans the sticker, they can send you a message and — if they choose — share where they are. You decide what to do next.'),
        ('Why is the location showing the wrong place?',
         'The location is shared by the finder\'s phone, not by the sticker. If it\'s wrong, that\'s usually the finder\'s device permissions, not the tag. The map link they send you is theirs to attach or skip.'),
        ('Is it really free? What\'s the catch?',
         'The messaging service is free, no subscription, no monthly fee, no hidden charges. Your one-time purchase covers the stickers. The app is genuinely free to use, forever.'),
        ('How do I activate 24 stickers — do I scan each one?',
         'No. Scan one sticker on the sheet to link the entire pack to your account in seconds. Each sticker is unique, but the activation is bulk. You can customize the message behind any individual sticker later (different message per item if you want).'),
        ('Where is the app? It\'s not in the App Store.',
         'SeQR is a Progressive Web App — install it from your phone\'s browser at app.seqrcontact.com. Finders never need an app — when they scan your sticker, the message page just opens in their phone\'s browser.'),
    ]
    qa_table = Table([[Paragraph(f'<b>Q{i+1}.</b> {q}', BODY), Paragraph(a, BODY)] for i, (q, a) in enumerate(qa)],
                     colWidths=[6.5*cm, CONTENT_W - 6.5*cm])
    qa_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), SAND),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LINEBELOW', (0,0), (-1,-1), 0.3, HexColor('#E0DCC8')),
        ('LEFTPADDING', (0,0), (-1,-1), 10), ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 8), ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(qa_table)

    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph('A+ Module 7 — Comparison Chart', H3))
    comp = [
        ['Feature', 'SeQR Lost\nItem Labels', 'Write-on / engraved\nlabels', 'AirTag / Tile\n(active tracker)', 'Generic QR\nstickers'],
        ['Phone-number-free', 'Yes', 'Usually no (you write it on)', 'N/A', 'Often no'],
        ['Re-customizable after purchase', 'Yes (any time)', 'No (engraved is permanent)', 'N/A', 'Sometimes'],
        ['No battery', 'Yes', 'Yes', 'No (~1 yr)', 'Yes'],
        ['No app required for finder', 'Yes', 'Yes', 'No (ecosystem)', 'Sometimes'],
        ['Built-in messaging platform', 'Yes (private)', 'No', 'No return channel', 'Sometimes (3rd-party)'],
        ['Optional location sharing', 'Yes (finder-initiated)', 'No', 'Live map (different)', 'Sometimes'],
        ['No subscription', 'Yes', 'Yes', 'Mostly yes', 'Varies'],
        ['Works internationally', 'Yes', 'Yes (if # is intl)', 'Limited', 'Sometimes'],
    ]
    comp_table = Table(comp, colWidths=[3.6*cm, 3.4*cm, 3.4*cm, 3.4*cm, 3.0*cm])
    comp_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY),
        ('TEXTCOLOR', (0,0), (-1,0), WHITE),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('BACKGROUND', (1,1), (1,-1), HexColor('#E6F6F7')),
        ('FONTNAME', (1,1), (1,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8.5),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('LEFTPADDING', (0,0), (-1,-1), 5), ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ('TOPPADDING', (0,0), (-1,-1), 5), ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('GRID', (0,0), (-1,-1), 0.3, HexColor('#CCCCCC')),
        ('ROWBACKGROUNDS', (0,1), (0,-1), [WHITE, SAND]),
        ('ROWBACKGROUNDS', (2,1), (-1,-1), [WHITE, SAND]),
    ]))
    story.append(comp_table)

    # ============ MASTER COPY ============
    story.append(PageBreak())
    story.append(Paragraph('6 · Master Copy (paste-ready)', H2))
    story.append(HRule())

    story.append(Paragraph('Title (suggested rewrite, ~199 chars)', H3))
    title_box = Table([[Paragraph(
        '<b>SeQR Lost Item Labels — 24-Pack QR Smart Stickers · Privacy-First Contact Tags for Passports, Water Bottles, Electronics, Kids\' Toys, Moving Boxes · No Phone Number Exposed · No Subscription · Free App</b>', BODY)]],
        colWidths=[CONTENT_W])
    title_box.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), TEAL),
        ('TEXTCOLOR', (0,0), (-1,-1), WHITE),
        ('LEFTPADDING', (0,0), (-1,-1), 12), ('RIGHTPADDING', (0,0), (-1,-1), 12),
        ('TOPPADDING', (0,0), (-1,-1), 8), ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(title_box)

    story.append(Spacer(1, 0.4*cm))
    story.append(Paragraph('Bullets (rewritten in voice — replaces the existing 8 bullets)', H3))
    bullets = [
        ('PHONE NUMBER OFF YOUR STICKER',
         'When someone finds your tagged item and scans the QR code, they reach you through the SeQR app — no phone number, email, or address exposed. Most people who find your stuff want to help. The few who don\'t can\'t use it against you.'),
        ('24 STICKERS FOR EVERYTHING SMALL',
         'Designed for the things AirTags don\'t fit on — passports, wallets, water bottles, AirPods cases, electronics, kids\' lunchboxes, moving boxes, gym gear. 1" × 0.75" each, durable enough to outlast the item itself.'),
        ('TEAR-PROOF, WATERPROOF, DISHWASHER-SAFE',
         'Built for daily use. Tested against rain, washing, dishwasher cycles, scratching, and sun fade. Adheres to plastic, metal, fabric, glass, and curved surfaces.'),
        ('ACTIVATE THE WHOLE PACK IN ONE SCAN',
         'Scan a single sticker on the sheet to link all 24 to your account in seconds. Want a different message per item (e.g. allergy info on your kid\'s lunchbox)? Customize each one individually whenever you like — the QR code never changes.'),
        ('FINDERS DON\'T NEED AN APP',
         'Anyone with a phone camera can scan and message. No download. No account. Works on iPhone, Android, and desktop, anywhere in the world.'),
        ('FINDER CAN OPTIONALLY SHARE WHERE THEY ARE',
         'If a finder wants to send you a Google Maps link of where they picked up your item, they can attach it to their message. No live tracking, no battery, no app — the location only shows up when a finder chooses to share it.'),
        ('FREE FOREVER. NO SUBSCRIPTION.',
         'The messaging app is genuinely free — no monthly fee, no hidden charges. Your one-time purchase covers the whole pack and the service behind it.'),
    ]
    bt = Table([[Paragraph(f'<b>{i+1}. {h}</b>', BODY), Paragraph(b, BODY)] for i, (h, b) in enumerate(bullets)],
               colWidths=[5.8*cm, CONTENT_W - 5.8*cm])
    bt.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), SAND),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LINEBELOW', (0,0), (-1,-1), 0.3, HexColor('#E0DCC8')),
        ('LEFTPADDING', (0,0), (-1,-1), 10), ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 7), ('BOTTOMPADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(bt)

    story.append(Spacer(1, 0.4*cm))
    story.append(Paragraph('Backend search terms (≤ 250 bytes)', H3))
    be = Table([[Paragraph(
        '<font face="Courier" size="8">qr code stickers smart labels lost and found tags storage bin labels moving box labels asset tags property stickers passport label water bottle label kids lunchbox label privacy contact tag no subscription waterproof tear proof dishwasher safe</font>', BODY)]],
        colWidths=[CONTENT_W])
    be.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), HexColor('#F5F5F5')),
        ('LEFTPADDING', (0,0), (-1,-1), 10), ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 8), ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(be)

    story.append(Spacer(1, 0.4*cm))
    story.append(Paragraph('Compliance — what to remove from existing copy', H3))
    for line in [
        '<b>Remove from current bullet 8:</b> "GPS LOCATION SHARING", "real-time location sharing", "lost tag tracking" — these violate the brand voice doc. Replaced with finder-initiated, optional location sharing.',
        'Remove "Use with or instead of a tile tracker, key finder, samsung tracker tags, generic trackers, or air tags / airtag" from bullet 1 — Amazon flags competitor brand names. Reframe as "works alongside trackers" only in A+ comparison, not in bullets.',
        'Remove "android compatible air tags" from bullet 3 — direct AirTag reference, brand-name violation.',
        'Soften "tear-resistant, scratch-proof, fade-resistant, waterproof, and dishwasher-safe" with "tested against" framing if no third-party test exists. Brand voice rule: <i>"Honest about limits."</i>',
        'Avoid "police reports" framing in bullet 5 — too dramatic for the product\'s warmth. Reframe as "for warranty, insurance, or shipping records."',
    ]:
        story.append(Paragraph('• ' + line, BODY))

    # ============ PRIORITY UPLIFTS ============
    story.append(PageBreak())
    story.append(Paragraph('7 · Priority uplifts (CTR × CVR)', H2))
    story.append(HRule())
    pri = [
        ('1', 'Run Main Image A/B/C test (Manage Your Experiments)', 'Three concepts above. 4-week test. Highest CTR lift available without operational change.'),
        ('2', 'Rewrite bullet 8 to remove "GPS / real-time tracking" claim', 'Brand voice violation AND Amazon-flag risk. Replace with finder-initiated optional location share.'),
        ('3', 'Publish A+ Module 6 (Q&A) with the 5 voice-aligned answers', 'Defuses the #1 misconception ("I thought it was an AirTag") and the recurring "is it really free" support question.'),
        ('4', 'Publish A+ Module 7 (Comparison Chart)', 'Makes the price defensible vs. write-on / generic QR / AirTag in one frame.'),
        ('5', 'Add Subscribe & Save (small-pack consumable)', 'Encourages re-purchase by households who use these on every kid / school year / move.'),
        ('6', 'Re-shoot Image #3 (3-step) and #4 (24-item flat lay)', 'Two single most converting images per category-best-in-class data.'),
    ]
    pri_table = Table([[Paragraph(f'<b>{n}</b>', BODY), Paragraph(f'<b>{t}</b>', BODY), Paragraph(d, BODY)] for n, t, d in pri],
                      colWidths=[1*cm, 6.5*cm, CONTENT_W - 7.5*cm])
    pri_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), NAVY),
        ('TEXTCOLOR', (0,0), (0,-1), WHITE),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LINEBELOW', (0,0), (-1,-1), 0.3, HexColor('#E0DCC8')),
        ('LEFTPADDING', (0,0), (-1,-1), 8), ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 7), ('BOTTOMPADDING', (0,0), (-1,-1), 7),
        ('ROWBACKGROUNDS', (1,0), (-1,-1), [WHITE, SAND]),
    ]))
    story.append(pri_table)

    doc.build(story)
    print(f'PDF: {OUT}')


if __name__ == '__main__':
    build()
