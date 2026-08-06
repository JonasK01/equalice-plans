#!/usr/bin/env python3
"""Render the CHEKKO Peanut Oil brief as a properly designed PDF — full plan."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    KeepTogether, Frame, BaseDocTemplate, PageTemplate, NextPageTemplate
)
from reportlab.platypus.flowables import Flowable

OUT = '/Users/jonask/Desktop/CHEKKO Peanut Oil Brief.pdf'

# CHEKKO brand palette
GOLD   = HexColor('#EFC522')
MAROON = HexColor('#65161A')
CREAM  = HexColor('#F7F0DD')
ROAST  = HexColor('#3A2A1F')
INK    = HexColor('#111111')
GREY   = HexColor('#666666')
LIGHT  = HexColor('#F5F0E6')
WHITE  = HexColor('#FFFFFF')
RED_TINT  = HexColor('#F8E5E5')
GREEN_TINT = HexColor('#E8F5E9')
WARN_BG = HexColor('#FFF4E5')

PAGE_W, PAGE_H = A4
MARGIN_L, MARGIN_R, MARGIN_T, MARGIN_B = 1.6*cm, 1.6*cm, 1.8*cm, 1.6*cm
CONTENT_W = PAGE_W - MARGIN_L - MARGIN_R

# ---------- Styles ----------
styles = getSampleStyleSheet()
H1 = ParagraphStyle('H1', parent=styles['Title'], fontName='Helvetica-Bold',
                    fontSize=26, leading=30, textColor=MAROON, spaceAfter=4, alignment=TA_LEFT)
SUB = ParagraphStyle('SUB', parent=styles['Normal'], fontName='Helvetica',
                     fontSize=11, leading=14, textColor=GREY, spaceAfter=14)
H2 = ParagraphStyle('H2', parent=styles['Heading2'], fontName='Helvetica-Bold',
                    fontSize=18, leading=22, textColor=MAROON, spaceBefore=14, spaceAfter=8)
H3 = ParagraphStyle('H3', parent=styles['Heading3'], fontName='Helvetica-Bold',
                    fontSize=12, leading=15, textColor=INK, spaceBefore=10, spaceAfter=4)
BODY = ParagraphStyle('Body', parent=styles['Normal'], fontName='Helvetica',
                      fontSize=10, leading=14, textColor=INK, spaceAfter=4)
SMALL = ParagraphStyle('Small', parent=BODY, fontSize=9, leading=12, textColor=GREY)
QUOTE = ParagraphStyle('Quote', parent=BODY, fontName='Helvetica-Oblique', textColor=GREY)
LABEL = ParagraphStyle('Label', parent=BODY, fontSize=9, fontName='Helvetica-Bold', textColor=MAROON)
WARN = ParagraphStyle('Warn', parent=BODY, fontName='Helvetica-Bold', textColor=HexColor('#B5390A'))


# ---------- Custom flowables ----------

class HRule(Flowable):
    def __init__(self, width=None, color=GOLD, thickness=1.4):
        self.width = width or CONTENT_W
        self.color = color
        self.thickness = thickness
        Flowable.__init__(self)
    def wrap(self, *args):
        return (self.width, self.thickness + 6)
    def draw(self):
        self.canv.setStrokeColor(self.color)
        self.canv.setLineWidth(self.thickness)
        self.canv.line(0, 3, self.width, 3)


class ColorChip(Flowable):
    def __init__(self, hex_color, label_top, label_bottom, w=3.6*cm, h=2.0*cm):
        self.color = HexColor(hex_color) if isinstance(hex_color, str) else hex_color
        self.label_top = label_top
        self.label_bottom = label_bottom
        self.w = w
        self.h = h
        Flowable.__init__(self)
    def wrap(self, *args):
        return (self.w, self.h + 0.9*cm)
    def draw(self):
        c = self.canv
        c.setFillColor(self.color)
        c.setStrokeColor(HexColor('#DDDDDD'))
        c.setLineWidth(0.3)
        c.rect(0, 0.9*cm, self.w, self.h, fill=1, stroke=1)
        c.setFillColor(INK)
        c.setFont('Helvetica-Bold', 9)
        c.drawString(0, 0.45*cm, self.label_top)
        c.setFillColor(GREY)
        c.setFont('Helvetica', 8)
        c.drawString(0, 0.15*cm, self.label_bottom)


def _wrap_text(canv, text, max_w, font, size, max_lines):
    """Word-wrap text to fit max_w; returns up to max_lines lines."""
    if not text:
        return []
    words = text.split()
    lines = []
    cur = ''
    for w in words:
        trial = (cur + ' ' + w).strip()
        if canv.stringWidth(trial, font, size) > max_w:
            if cur:
                lines.append(cur)
            cur = w
        else:
            cur = trial
    if cur:
        lines.append(cur)
    return lines[:max_lines]


class MainImageOption(Flowable):
    """A 2000x2000 main-image OPTION mockup with composition sketch."""
    def __init__(self, letter, concept_name, composition_desc, ctr_pitch, side_w=8.5*cm):
        self.letter = letter
        self.concept = concept_name
        self.desc = composition_desc
        self.pitch = ctr_pitch
        self.size = 6.5*cm
        self.side_w = side_w
        self.gap = 0.4*cm
        self.total_w = self.size + self.gap + self.side_w
        Flowable.__init__(self)

    def wrap(self, *args):
        return (self.total_w, self.size + 0.5*cm)

    def draw(self):
        c = self.canv
        s = self.size
        # Pure white BG (Amazon main-image rule)
        c.setFillColor(WHITE)
        c.setStrokeColor(HexColor('#CCCCCC'))
        c.setLineWidth(0.4)
        c.rect(0, 0, s, s, fill=1, stroke=1)
        # Letter tag
        c.setFillColor(MAROON)
        c.rect(0, s - 0.7*cm, 1.3*cm, 0.7*cm, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont('Helvetica-Bold', 12)
        c.drawCentredString(0.65*cm, s - 0.5*cm, f'OPT {self.letter}')

        # Composition sketch: simplified shapes per option
        cx, cy = s/2, s/2 - 0.3*cm
        if self.letter == 'A':
            # Tin solo, tall
            self._draw_tin(c, cx, cy, w=2.4*cm, h=2.8*cm)
        elif self.letter == 'B':
            # Tin slightly left + golden oil pour into a small bowl on the right
            self._draw_tin(c, cx - 1.2*cm, cy, w=2.0*cm, h=2.4*cm)
            # Pour ribbon
            c.setFillColor(GOLD)
            c.setStrokeColor(GOLD)
            for i in range(8):
                xx = cx + 0.3*cm + i*0.05*cm
                yy = cy + 1.0*cm - i*0.18*cm
                c.circle(xx, yy, 0.05*cm, fill=1, stroke=0)
            # Small ceramic bowl
            c.setFillColor(HexColor('#2C2C2C'))
            c.setStrokeColor(HexColor('#1A1A1A'))
            c.ellipse(cx + 0.6*cm, cy - 1.4*cm, cx + 2.2*cm, cy - 0.7*cm, fill=1, stroke=1)
            # Oil pool inside bowl
            c.setFillColor(GOLD)
            c.ellipse(cx + 0.75*cm, cy - 1.2*cm, cx + 2.05*cm, cy - 0.85*cm, fill=1, stroke=0)
        elif self.letter == 'C':
            # Tin centered + pile of groundnuts at base
            self._draw_tin(c, cx, cy + 0.3*cm, w=2.4*cm, h=2.6*cm)
            # Groundnut pile
            c.setFillColor(HexColor('#C19A6B'))
            for offs in [(-1.6,0.0),(-1.2,0.1),(-0.8,0.0),(0.8,0.0),(1.2,0.05),(1.6,0.0),
                         (-0.4,0.1),(0.4,0.05),(0,0.15),(-1.0,-0.1)]:
                ox, oy = offs
                c.ellipse(cx + ox*cm - 0.18*cm, cy - 1.6*cm + oy*cm,
                          cx + ox*cm + 0.18*cm, cy - 1.4*cm + oy*cm + 0.12*cm,
                          fill=1, stroke=0)
            # One shelled half on top
            c.setFillColor(HexColor('#E8C58A'))
            c.ellipse(cx - 0.15*cm, cy - 1.45*cm, cx + 0.15*cm, cy - 1.30*cm, fill=1, stroke=0)

        # Dim caption
        c.setFillColor(GREY)
        c.setFont('Helvetica', 7)
        c.drawCentredString(s/2, 0.15*cm, '2000 × 2000 px · Pure white BG')
        # Concept tag bottom-right
        c.setFillColor(GOLD)
        tag_w = c.stringWidth(self.concept.upper(), 'Helvetica-Bold', 7) + 0.4*cm
        c.rect(s - tag_w, 0, tag_w, 0.5*cm, fill=1, stroke=0)
        c.setFillColor(INK)
        c.setFont('Helvetica-Bold', 7)
        c.drawString(s - tag_w + 0.2*cm, 0.18*cm, self.concept.upper())

    def _draw_tin(self, c, cx, cy, w, h):
        """Draw a stylized CHEKKO tin in maroon + gold."""
        # Tin body (gold)
        c.setFillColor(GOLD)
        c.setStrokeColor(MAROON)
        c.setLineWidth(0.5)
        c.rect(cx - w/2, cy - h/2, w, h, fill=1, stroke=1)
        # Top cap (maroon)
        c.setFillColor(MAROON)
        c.rect(cx - w/2, cy + h/2 - 0.35*cm, w, 0.35*cm, fill=1, stroke=0)
        # Spout
        c.setFillColor(HexColor('#222222'))
        c.rect(cx + w/2 - 0.55*cm, cy + h/2, 0.3*cm, 0.25*cm, fill=1, stroke=0)
        # Label area (cream)
        c.setFillColor(CREAM)
        c.rect(cx - w/2 + 0.18*cm, cy - h/3, w - 0.36*cm, h*0.55, fill=1, stroke=0)
        # CHEKKO text on label
        c.setFillColor(MAROON)
        c.setFont('Helvetica-Bold', 8)
        c.drawCentredString(cx, cy + h*0.10, 'CHEKKO')
        c.setFont('Helvetica', 5)
        c.setFillColor(INK)
        c.drawCentredString(cx, cy + h*0.02, 'COLD-PRESSED')
        c.drawCentredString(cx, cy - h*0.04, 'PEANUT OIL')
        c.setFont('Helvetica-Bold', 5.5)
        c.setFillColor(MAROON)
        c.drawCentredString(cx, cy - h*0.20, '5 L · 169 FL OZ')


class ImageMockup(Flowable):
    """A 2000x2000 listing image mockup."""
    def __init__(self, slot_num, role, bg_hex, headline, sub, side_w=8.5*cm):
        self.slot = slot_num
        self.role = role
        self.bg = HexColor(bg_hex) if isinstance(bg_hex, str) else bg_hex
        self.headline = headline
        self.sub = sub
        self.size = 6.5*cm
        self.side_w = side_w
        self.gap = 0.4*cm
        self.total_w = self.size + self.gap + self.side_w
        Flowable.__init__(self)

    def wrap(self, *args):
        return (self.total_w, self.size + 0.5*cm)

    def draw(self):
        c = self.canv
        s = self.size
        c.setFillColor(self.bg)
        c.setStrokeColor(HexColor('#CCCCCC'))
        c.setLineWidth(0.4)
        c.rect(0, 0, s, s, fill=1, stroke=1)
        c.setFillColor(MAROON)
        c.rect(0, s - 0.7*cm, 1.4*cm, 0.7*cm, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont('Helvetica-Bold', 11)
        c.drawCentredString(0.7*cm, s - 0.5*cm, f'#{self.slot}')
        c.setFillColor(GREY)
        c.setFont('Helvetica', 7)
        c.drawCentredString(s/2, 0.15*cm, '2000 × 2000 px')

        if self.headline:
            text_color = MAROON if self.bg in (CREAM, WHITE, LIGHT, GOLD) else WHITE
            c.setFillColor(text_color)
            c.setFont('Helvetica-Bold', 10)
            lines = _wrap_text(c, self.headline.upper(), s - 0.8*cm, 'Helvetica-Bold', 10, 3)
            y = s/2 + (len(lines)-1) * 6
            for line in lines:
                c.drawCentredString(s/2, y, line)
                y -= 12
            if self.sub:
                c.setFont('Helvetica-Oblique', 7.5)
                c.setFillColor(GREY if self.bg in (CREAM, WHITE, LIGHT, GOLD) else WHITE)
                sub_lines = _wrap_text(c, self.sub, s - 0.8*cm, 'Helvetica-Oblique', 7.5, 2)
                yy = s/2 - len(lines)*6 - 8
                for sl in sub_lines:
                    c.drawCentredString(s/2, yy, sl)
                    yy -= 9
        else:
            c.setFillColor(GREY)
            c.setFont('Helvetica-Oblique', 8)
            c.drawCentredString(s/2, s/2, '(see options A/B/C)')

        c.setFillColor(GOLD)
        role_w = c.stringWidth(self.role.upper(), 'Helvetica-Bold', 7) + 0.4*cm
        c.rect(s - role_w, 0, role_w, 0.5*cm, fill=1, stroke=0)
        c.setFillColor(INK)
        c.setFont('Helvetica-Bold', 7)
        c.drawString(s - role_w + 0.2*cm, 0.18*cm, self.role.upper())


class APlusMockup(Flowable):
    """A 1464x600 A+ banner mockup."""
    def __init__(self, slot_num, module_type, headline, sub, theme_color=CREAM, side_w=7.5*cm):
        self.slot = slot_num
        self.module_type = module_type
        self.headline = headline
        self.sub = sub
        self.bg = theme_color
        self.banner_w = 9.5*cm
        self.banner_h = 9.5*cm * (600/1464)
        self.side_w = side_w
        self.gap = 0.4*cm
        self.total_w = self.banner_w + self.gap + self.side_w
        Flowable.__init__(self)

    def wrap(self, *args):
        return (self.total_w, self.banner_h + 0.5*cm)

    def draw(self):
        c = self.canv
        w, h = self.banner_w, self.banner_h
        c.setFillColor(self.bg)
        c.setStrokeColor(HexColor('#CCCCCC'))
        c.setLineWidth(0.4)
        c.rect(0, 0.5*cm, w, h, fill=1, stroke=1)
        c.setFillColor(MAROON)
        c.rect(0, 0.5*cm + h - 0.55*cm, 2.6*cm, 0.55*cm, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont('Helvetica-Bold', 8)
        c.drawString(0.15*cm, 0.5*cm + h - 0.4*cm, f'MODULE {self.slot}')

        text_color = MAROON if self.bg in (CREAM, WHITE, LIGHT, GOLD) else WHITE
        c.setFillColor(text_color)
        c.setFont('Helvetica-Bold', 11)
        if self.headline:
            lines = _wrap_text(c, self.headline.upper(), w - 1*cm, 'Helvetica-Bold', 11, 2)
            y = 0.5*cm + h/2 + (len(lines)-1)*6 + 0.2*cm
            for line in lines:
                c.drawCentredString(w/2, y, line)
                y -= 13
            if self.sub:
                c.setFont('Helvetica-Oblique', 8)
                c.setFillColor(GREY if self.bg in (CREAM, WHITE, LIGHT, GOLD) else WHITE)
                sub_lines = _wrap_text(c, self.sub, w - 1*cm, 'Helvetica-Oblique', 8, 1)
                yy = 0.5*cm + h/2 - len(lines)*6 - 4
                for sl in sub_lines:
                    c.drawCentredString(w/2, yy, sl)

        c.setFillColor(GOLD)
        type_w = c.stringWidth(self.module_type.upper(), 'Helvetica-Bold', 7) + 0.3*cm
        c.rect(w - type_w, 0.5*cm, type_w, 0.4*cm, fill=1, stroke=0)
        c.setFillColor(INK)
        c.setFont('Helvetica-Bold', 7)
        c.drawString(w - type_w + 0.15*cm, 0.5*cm + 0.13*cm, self.module_type.upper())
        c.setFillColor(GREY)
        c.setFont('Helvetica', 6.5)
        c.drawCentredString(w/2, 0.15*cm, '1464 × 600 px desktop · 600 × 450 mobile')


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(GOLD)
    canvas.setLineWidth(2.5)
    canvas.line(MARGIN_L, PAGE_H - 1.0*cm, PAGE_W - MARGIN_R, PAGE_H - 1.0*cm)
    canvas.setFillColor(MAROON)
    canvas.setFont('Helvetica-Bold', 9)
    canvas.drawString(MARGIN_L, PAGE_H - 0.7*cm, 'CHEKKO')
    canvas.setFillColor(GREY)
    canvas.setFont('Helvetica', 8)
    canvas.drawString(MARGIN_L + 1.6*cm, PAGE_H - 0.7*cm, 'Cold-Pressed Peanut Oil 1 L + 5 L · Amazon US Brief')
    canvas.setFillColor(GREY)
    canvas.setFont('Helvetica', 8)
    canvas.drawRightString(PAGE_W - MARGIN_R, PAGE_H - 0.7*cm, f'Page {doc.page}')
    canvas.setStrokeColor(HexColor('#E0DCC8'))
    canvas.setLineWidth(0.4)
    canvas.line(MARGIN_L, MARGIN_B - 0.4*cm, PAGE_W - MARGIN_R, MARGIN_B - 0.4*cm)
    canvas.setFillColor(GREY)
    canvas.setFont('Helvetica', 7.5)
    canvas.drawString(MARGIN_L, MARGIN_B - 0.7*cm, 'Prepared by EQUALICE — 2026-05-05 · Hero ASIN B08WHJNW3V (5 L) · Sister B079JT6NBP (1 L)')
    canvas.restoreState()


def cover_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(CREAM)
    canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    canvas.setFillColor(GOLD)
    canvas.rect(0, PAGE_H - 4*cm, PAGE_W, 4*cm, fill=1, stroke=0)
    canvas.setFillColor(MAROON)
    canvas.rect(0, PAGE_H - 4.4*cm, PAGE_W, 0.4*cm, fill=1, stroke=0)
    canvas.setFillColor(MAROON)
    canvas.setFont('Helvetica-Bold', 38)
    canvas.drawString(MARGIN_L, PAGE_H - 2.6*cm, 'CHEKKO')
    canvas.setFont('Helvetica', 16)
    canvas.setFillColor(INK)
    canvas.drawString(MARGIN_L, PAGE_H - 3.4*cm, 'Cold-Pressed Peanut Oil · 1 L + 5 L')
    canvas.setFillColor(MAROON)
    canvas.setFont('Helvetica-Bold', 22)
    canvas.drawString(MARGIN_L, PAGE_H - 7*cm, 'Amazon US Listing Brief')
    canvas.setFillColor(GREY)
    canvas.setFont('Helvetica', 13)
    canvas.drawString(MARGIN_L, PAGE_H - 7.8*cm, 'Image Plan · A+ Premium · Moodboard · CTR Boost')
    y = 5*cm
    canvas.setFillColor(MAROON)
    canvas.setFont('Helvetica-Bold', 9)
    canvas.drawString(MARGIN_L, y, 'HERO ASIN (5 L)')
    canvas.drawString(MARGIN_L + 5*cm, y, 'SISTER (1 L)')
    canvas.drawString(MARGIN_L + 10*cm, y, 'MARKETPLACE')
    canvas.drawString(MARGIN_L + 14*cm, y, 'DATE')
    canvas.setFillColor(INK)
    canvas.setFont('Helvetica', 11)
    canvas.drawString(MARGIN_L, y - 0.55*cm, 'B08WHJNW3V · BSR #5')
    canvas.drawString(MARGIN_L + 5*cm, y - 0.55*cm, 'B079JT6NBP · BSR #26')
    canvas.drawString(MARGIN_L + 10*cm, y - 0.55*cm, 'amazon.com')
    canvas.drawString(MARGIN_L + 14*cm, y - 0.55*cm, '2026-05-05')
    canvas.setFillColor(MAROON)
    canvas.rect(0, 0, PAGE_W, 1.4*cm, fill=1, stroke=0)
    canvas.setFillColor(GOLD)
    canvas.setFont('Helvetica-Bold', 10)
    canvas.drawString(MARGIN_L, 0.5*cm, 'PRESSED SLOW. POURED PROUD. — 40+ YEARS OF AGAMAHIL HERITAGE.')
    canvas.setFillColor(WHITE)
    canvas.setFont('Helvetica', 9)
    canvas.drawRightString(PAGE_W - MARGIN_R, 0.5*cm, 'Prepared by EQUALICE')
    canvas.restoreState()


# ---------- Build the document ----------
def build():
    doc = BaseDocTemplate(OUT, pagesize=A4,
                          leftMargin=MARGIN_L, rightMargin=MARGIN_R,
                          topMargin=MARGIN_T, bottomMargin=MARGIN_B,
                          title='CHEKKO Cold-Pressed Peanut Oil 1 L + 5 L — Amazon US Brief',
                          author='EQUALICE')

    cover_frame = Frame(MARGIN_L, MARGIN_B, CONTENT_W, PAGE_H - MARGIN_T - MARGIN_B,
                        leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, showBoundary=0)
    body_frame = Frame(MARGIN_L, MARGIN_B, CONTENT_W, PAGE_H - MARGIN_T - MARGIN_B,
                       leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, showBoundary=0)
    cover_template = PageTemplate(id='Cover', frames=[cover_frame], onPage=cover_page)
    body_template = PageTemplate(id='Body', frames=[body_frame], onPage=header_footer)
    doc.addPageTemplates([cover_template, body_template])

    story = []
    story.append(Spacer(1, 1))
    story.append(PageBreak())
    story.append(NextPageTemplate('Body'))
    story.append(PageBreak())

    # ============ AT A GLANCE ============
    story.append(Paragraph('At a glance', H2))
    story.append(HRule())
    glance = [
        ['Brand', 'CHEKKO — heritage Indian wood-pressed cooking oils (Agamahil family, 40+ years)'],
        ['Product', '100% Pure Cold-Pressed Peanut Oil (Groundnut Oil) — wood-pressed via chekku / ganuga / lakdi ghani method · unrefined · plastic-free tin'],
        ['Hero variant', '5 L (169 Fl Oz) — ASIN B08WHJNW3V — currently #5 in Peanut Oils · 4.4★ (bestseller)'],
        ['Sister variant', '1 L (33 Fl Oz) — ASIN B079JT6NBP — currently #26 in Peanut Oils · 4.4★'],
        ['Strategic position', 'Defend the #5 slot vs. Gramiyaa (only other heritage cold-pressed competitor) AND steal commodity-oil buyers (Amazon Grocery, PLANTERS, Lou Ana) on the "no anti-foam chemicals" hook.'],
        ['CRITICAL compliance', '⚠ Never claim "allergy-safe" or "allergen-free." Cold-pressed peanut oil contains natural peanut proteins. Only refined peanut oil is generally considered allergy-safe. Q&A frames this transparently.'],
        ['Operational fixes flagged in reviews', '(1) Tin spout / opening UX — multiple buyers love the oil but flag the spout. (2) FBA shipping damage — dented tins arriving in padded envelopes.'],
    ]
    t = Table([[Paragraph(f'<b>{k}</b>', BODY), Paragraph(v, BODY)] for k, v in glance],
              colWidths=[4.0*cm, CONTENT_W - 4.0*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), CREAM),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LINEBELOW', (0,0), (-1,-1), 0.3, HexColor('#E0DCC8')),
        ('LEFTPADDING', (0,0), (-1,-1), 8), ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 6), ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t)

    # ============ BRANDBOOK ============
    story.append(Spacer(1, 0.6*cm))
    story.append(Paragraph('1 · Brandbook', H2))
    story.append(HRule())
    story.append(Paragraph('Identity', H3))
    story.append(Paragraph('<b>Brand:</b> CHEKKO', BODY))
    story.append(Paragraph('<b>Voice:</b> Calm, grounded, ancestral. <i>"Pressed slow. Poured proud."</i>', BODY))
    story.append(Paragraph('<b>Personality:</b> Modern + Luxurious + Creative/Original (per onboarding)', BODY))
    story.append(Paragraph('<b>Heritage line:</b> 40+ years of Agamahil family oil-making heritage', BODY))

    story.append(Paragraph('Color palette', H3))
    chips = [
        ColorChip(GOLD, '#EFC522', 'Primary — Golden Yellow'),
        ColorChip(MAROON, '#65161A', 'Accent — Deep Maroon'),
        ColorChip(INK, '#000000', 'Text — Black'),
        ColorChip(CREAM, '#F7F0DD', 'Mood — Warm Cream'),
    ]
    chip_table = Table([chips], colWidths=[CONTENT_W/4]*4)
    chip_table.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'),
                                    ('LEFTPADDING', (0,0), (-1,-1), 0),
                                    ('RIGHTPADDING', (0,0), (-1,-1), 6)]))
    story.append(chip_table)

    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph('Typography', H3))
    story.append(Paragraph('Sans-serif family from onboarding: <b>Minion Variable Concept · Inter · Myriad Pro · Open Sans</b>', BODY))
    story.append(Paragraph('Image headlines 72–96 pt, semibold, all-caps where dramatic · A+ headlines 60–80 pt · Body 16–22 pt · line-height 1.4–1.5', BODY))

    story.append(Paragraph('Photography rules', H3))
    for line in [
        'Real ingredients (groundnuts, oil, ceramic, wood, linen, cast iron).',
        'Hands only — no faces unless explicit lifestyle shoot.',
        'Warm side-light. Avoid hard ringlight or cold studio.',
        '<b>NEVER</b> plastic bottles, plastic dispensers, or plastic-looking surfaces in frame.',
        'Stock photos allowed; product can be photoshopped in if it looks real.',
    ]:
        story.append(Paragraph('• ' + line, BODY))

    story.append(Paragraph('Creative freedom', H3))
    story.append(Paragraph('<b>4 / 5</b> — push the design, but stay anchored to brand files.', BODY))

    # ============ KEYWORDS + COMPETITORS ============
    story.append(PageBreak())
    story.append(Paragraph('2 · Keywords & Competitors (from your Excel + live data)', H2))
    story.append(HRule())

    story.append(Paragraph('Top-priority keywords', H3))
    kws = [
        ('peanut oil', 'Root term · ~50–80k/mo', 'Title position #1 candidate'),
        ('peanut oil for deep frying', 'Very High · ~3,200/mo', 'Title — peanut oil = deep frying in US shopper mind'),
        ('peanut oil for cooking', 'High · ~1,200/mo', 'Bullets / A+'),
        ('cold pressed peanut oil', 'High · ~570/mo', 'CHEKKO\'s strongest single-claim term — own this'),
        ('peanut oil cold pressed', 'High · ~560/mo', 'Alt-phrase for backend'),
        ('cold pressed peanut oil for cooking', 'Medium · ~500/mo', 'Tightest match to CHEKKO positioning'),
        ('groundnut oil', 'High · ~455/mo', 'Title — Indian/diaspora credibility signal'),
        ('peanut oil for turkey fryer', 'High · ~350/mo', 'Q4 seasonal — Bullet 3 + A+ Module 4'),
        ('unrefined peanut oil', 'Medium · ~260/mo', 'Title'),
        ('peanut oil 1 gallon', 'Medium-High · ~550/mo', 'A+ Module 5 variant carousel'),
        ('wood pressed groundnut oil', 'Lower · niche', 'Title + Bullet 2 — direct CHEKKO method'),
        ('chekku oil · ganuga oil · kachi ghani', 'Lower · brand-aligned', 'Backend — Indian method terms'),
    ]
    kw_table = Table([['Keyword phrase', 'Volume tier', 'Use where']] +
                     [[Paragraph(k, BODY), Paragraph(v, SMALL), Paragraph(u, BODY)] for k, v, u in kws],
                     colWidths=[6.5*cm, 4.5*cm, CONTENT_W - 11*cm])
    kw_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), MAROON),
        ('TEXTCOLOR', (0,0), (-1,0), WHITE),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 9),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 7), ('RIGHTPADDING', (0,0), (-1,-1), 7),
        ('TOPPADDING', (0,0), (-1,-1), 5), ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('GRID', (0,0), (-1,-1), 0.3, HexColor('#CCCCCC')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [WHITE, CREAM]),
    ]))
    story.append(kw_table)

    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph('Competitive landscape (live BSR · 2026-05)', H3))
    comps = [
        ['Brand', 'ASIN', 'Rating', 'BSR', 'Pack', 'How to beat them'],
        ['CHEKKO 5 L (HERO)', 'B08WHJNW3V', '4.4★', '#5', '5 L tin', '— defend & widen lead'],
        ['CHEKKO 1 L', 'B079JT6NBP', '4.4★', '#26', '1 L tin', 'trial-size; major headroom'],
        ['Amazon Grocery', 'B07SRJ8S14', '4.7★', '#1', '128 fl oz plastic', 'beat on ingredients (no anti-foam)'],
        ['PLANTERS', 'B00I8GK544', '4.7★', '#2', '24 oz', 'beat on heritage + cold-pressed'],
        ['365 Whole Foods', 'B074H6BYQ3', '4.7★', '#3', '8.4 fl oz roasted', 'different product (roasted) — complementary'],
        ['Gramiyaa cold-pressed 5 L', 'B0F8KLB9QM', '4.3★', '#12', '5 L plastic-look', 'DIRECT comp — beat on tin + family backstory + photography'],
    ]
    comp_table = Table([[Paragraph(f'<b>{c}</b>' if i==0 else c, BODY) for c in row] for i, row in enumerate(comps)],
                       colWidths=[3.6*cm, 2.6*cm, 1.5*cm, 1.4*cm, 3.0*cm, CONTENT_W - 12.1*cm])
    comp_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), MAROON),
        ('TEXTCOLOR', (0,0), (-1,0), WHITE),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 5), ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ('TOPPADDING', (0,0), (-1,-1), 5), ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('GRID', (0,0), (-1,-1), 0.3, HexColor('#CCCCCC')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [WHITE, CREAM]),
        ('BACKGROUND', (0,1), (-1,1), HexColor('#FFF8DC')),  # CHEKKO 5L row
    ]))
    story.append(comp_table)

    story.append(Spacer(1, 0.4*cm))
    gap_box = Table([[Paragraph(
        '<b>KEY GAP:</b> CHEKKO is the only listing combining (a) heritage cold-pressed, (b) traceable Indian wood-press method, '
        '(c) plastic-free tin packaging, (d) 40+ year family business backstory in a polished, modern brand. '
        'Gramiyaa shares (a)+(b) but loses on tin and brand polish. <b>Defend hard, then steal commodity buyers</b> '
        'with the "no anti-foam chemicals" hook.', BODY)]], colWidths=[CONTENT_W])
    gap_box.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), GOLD),
        ('LEFTPADDING', (0,0), (-1,-1), 12), ('RIGHTPADDING', (0,0), (-1,-1), 12),
        ('TOPPADDING', (0,0), (-1,-1), 10), ('BOTTOMPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(gap_box)

    # ============ BUYER PSYCHOLOGY ============
    story.append(PageBreak())
    story.append(Paragraph('3 · Buyer Psychology', H2))
    story.append(HRule())
    story.append(Paragraph(
        'The Indian / South Asian US household wants the cold-pressed groundnut oil their parents used at home, '
        'in a US-friendly bulk format — daily tempering, pickling, deep frying. The clean-ingredient US home cook '
        'has read about anti-foaming chemicals and refined-oil shortcuts and wants a traceable cooking oil. '
        'The Q4 turkey-fryer buyer is currently using Lou Ana / PLANTERS — a massive seasonal pocket convertible '
        'if "premium" doesn\'t break the "fries great" promise.', BODY))
    story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph('Top buying triggers', H3))
    triggers = [
        ('Distrust of refined oils', 'Anti-foaming agents, hexane, bleaching. The "no chemicals, no shortcuts" message converts. (Verbatim in commodity reviews: "doesn\'t have a chemical that reduces foam".)'),
        ('Heritage / wood-press authenticity', '"Made the way oil was made before factories." Strong for Indian diaspora; rising for Western buyers seeking pre-industrial methods.'),
        ('Plastic fatigue', 'Both commodity (Amazon Grocery) and direct competitor (Gramiyaa) reviews mention wanting glass/non-plastic. CHEKKO tin = differentiator.'),
        ('Bulk-size value (5 L)', 'For frequent fryers and Indian families cooking daily, bulk cold-pressed oil is hard to find. CHEKKO 5L owns this.'),
    ]
    t = Table([[Paragraph(f'<b>{k}</b>', BODY), Paragraph(v, BODY)] for k, v in triggers],
              colWidths=[4.5*cm, CONTENT_W - 4.5*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), GOLD),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LINEBELOW', (0,0), (-1,-1), 0.3, HexColor('#E0DCC8')),
        ('LEFTPADDING', (0,0), (-1,-1), 8), ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 6), ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t)

    story.append(Spacer(1, 0.4*cm))
    story.append(Paragraph('Friction points to defuse', H3))
    frictions = [
        ('Tin spout / opening UX', 'Multiple buyers love the oil but flag the spout. Reframe in image #6 + ops fix.'),
        ('FBA shipping damage', '"Metal can arrived in a padded envelope, badly dented." Coordinate with FBA packaging team.'),
        ('Sticker shock vs. commodity', 'CHEKKO 5L costs 2-3× Amazon Grocery 1 gallon. Justify with cold-press yield + heritage + no chemicals + tin.'),
        ('Allergy concern (cold-pressed vs refined)', 'Refined peanut oil is allergy-safe; cold-pressed retains allergens. NEVER claim allergy safety. Q&A frames transparently.'),
        ('Foaming on first heat', 'Cold-pressed oils naturally foam; refined ones suppress with anti-foam. Address in A+ Q&A.'),
    ]
    t = Table([[Paragraph(f'<b>{k}</b>', BODY), Paragraph(v, BODY)] for k, v in frictions],
              colWidths=[5.0*cm, CONTENT_W - 5.0*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), RED_TINT),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LINEBELOW', (0,0), (-1,-1), 0.3, HexColor('#E0DCC8')),
        ('LEFTPADDING', (0,0), (-1,-1), 8), ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 6), ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t)

    # ============ ALLERGY COMPLIANCE WARNING (LARGE) ============
    story.append(Spacer(1, 0.5*cm))
    warn_box = Table([[Paragraph(
        '<b>⚠ COMPLIANCE WARNING — PEANUT OIL ALLERGY</b><br/><br/>'
        'Cold-pressed peanut oil contains natural peanut proteins. <b>Only refined peanut oil is generally considered allergy-safe.</b> '
        'CHEKKO is cold-pressed and unrefined — NEVER claim "allergy-safe", "allergen-free", or "safe for peanut allergies" anywhere in title, bullets, images, or A+. '
        'The Q&A in A+ Module 6 addresses this honestly.', BODY)]], colWidths=[CONTENT_W])
    warn_box.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), WARN_BG),
        ('BOX', (0,0), (-1,-1), 1.2, HexColor('#B5390A')),
        ('LEFTPADDING', (0,0), (-1,-1), 14), ('RIGHTPADDING', (0,0), (-1,-1), 14),
        ('TOPPADDING', (0,0), (-1,-1), 12), ('BOTTOMPADDING', (0,0), (-1,-1), 12),
    ]))
    story.append(warn_box)

    # ============ MOODBOARD ============
    story.append(PageBreak())
    story.append(Paragraph('4 · Moodboard', H2))
    story.append(HRule())
    story.append(Paragraph('Overall direction', H3))
    story.append(Paragraph(
        '<b>Warm. Heritage. Honest.</b> A heirloom-cookbook aesthetic lit by golden hour through a kitchen window. '
        'The oil is the hero — pours, drops, rim-light on the tin, the visible labor of the wood press.', BODY))

    story.append(Spacer(1, 0.4*cm))
    story.append(Paragraph('Dominant tones', H3))
    big_chips = [
        ColorChip(GOLD, '#EFC522', 'Golden Yellow', w=3.6*cm, h=2.6*cm),
        ColorChip(CREAM, '#F7F0DD', 'Warm Cream', w=3.6*cm, h=2.6*cm),
        ColorChip(MAROON, '#65161A', 'Deep Maroon', w=3.6*cm, h=2.6*cm),
        ColorChip(ROAST, '#3A2A1F', 'Roasted Brown', w=3.6*cm, h=2.6*cm),
    ]
    bc = Table([big_chips], colWidths=[CONTENT_W/4]*4)
    bc.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'),
                            ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 6)]))
    story.append(bc)

    story.append(Spacer(1, 0.4*cm))
    story.append(Paragraph('Five lifestyle scenes', H3))
    scenes = [
        ('1. The press', 'Wooden chekku / ganuga press in a sunlit Indian-craft workshop, dust motes, no machinery glow. CHEKKO tin in foreground.'),
        ('2. The pour', 'Slow stream of golden oil falling into a small black ceramic bowl, held in a hand. Wooden surface, linen napkin.'),
        ('3. The fry', 'Golden oil bubbling around a turkey leg / chicken pieces in a heavy cast-iron pot. Steam, golden light, wood handles.'),
        ('4. The temper', 'Whole spices popping in a steel kadai, oil shimmering, gas flame underneath. Indian kitchen.'),
        ('5. The family table', 'Multigenerational hand pouring CHEKKO oil at a sun-lit table set with home-cooked food. Warm, candle-light feel.'),
    ]
    t = Table([[Paragraph(f'<b>{k}</b>', BODY), Paragraph(v, BODY)] for k, v in scenes],
              colWidths=[4.2*cm, CONTENT_W - 4.2*cm])
    t.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LINEBELOW', (0,0), (-1,-1), 0.3, HexColor('#E0DCC8')),
        ('LEFTPADDING', (0,0), (-1,-1), 8), ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 7), ('BOTTOMPADDING', (0,0), (-1,-1), 7),
        ('ROWBACKGROUNDS', (0,0), (-1,-1), [WHITE, CREAM]),
    ]))
    story.append(t)

    story.append(Spacer(1, 0.5*cm))
    yes_no = Table([
        [Paragraph('<b>PROPS ALLOWED</b>', LABEL), Paragraph('<b>PROPS NEVER ALLOWED</b>', LABEL)],
        [Paragraph('Raw groundnuts (in shell + shelled) · ceramic bowls (matte black, terracotta) · weathered wood · linen · cast-iron tawa &amp; kadai · cotton towels · glass jars · dried red chillies · curry leaves · mustard seeds · fresh garlic / ginger · finished Indian / American comfort food', BODY),
         Paragraph('Plastic bottles · plastic measuring cups · plastic-looking dispensers · stainless-steel modern minimalism · marble Scandi-counter aesthetic · stock "diverse-family-laughing" lifestyle · anything that reads "supermarket commodity"', BODY)],
    ], colWidths=[CONTENT_W/2 - 0.2*cm, CONTENT_W/2 - 0.2*cm])
    yes_no.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), GREEN_TINT),
        ('BACKGROUND', (1,0), (1,-1), RED_TINT),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 10), ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 8), ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('BOX', (0,0), (-1,-1), 0.3, HexColor('#CCCCCC')),
    ]))
    story.append(yes_no)

    # ============ MAIN IMAGE OPTIONS — A/B/C ============
    story.append(PageBreak())
    story.append(Paragraph('5 · Main Image — 3 Options for CTR Test', H2))
    story.append(HRule())
    story.append(Paragraph(
        'Amazon main-image rules require pure white BG (#FFFFFF) and no overlay text. '
        'Three concepts below — different hooks, all compliant. Recommend running them as a Manage Your Experiments A/B/C test for 4 weeks; '
        'whichever wins on click-through becomes Image #1, the other two become Images #5 / #6 candidates.', BODY))
    story.append(Spacer(1, 0.4*cm))

    options = [
        ('A', 'Hero Tin Solo',
         'CHEKKO 5L tin centered, three-quarter elevated angle, label fully readable, subtle warm rim light to make the gold label glow against pure white. ~85% of frame height. Subtle contact shadow.',
         'Premium-credibility hook. Reads "premium tin packaging" instantly at thumbnail size. Best CTR vs. plastic-bottle competitors. Low risk, broad appeal — recommended baseline.'),
        ('B', 'Tin + Hand-Pour',
         'CHEKKO 5L tin slightly off-center-left. To its right, a small black ceramic dispenser jug or bowl with a slow, viscous golden stream of oil pouring into it. Hand visible at the edge holding the jug.',
         'Sensory hook — shows the oil itself (the product inside the tin). Wins for the "cold-pressed quality" buyer who is comparing. Slightly riskier in compliance (Amazon prefers very clean main images) but strong for ingredient-conscious search.'),
        ('C', 'Tin + Groundnut Pile',
         'CHEKKO 5L tin centered. At the base of the tin, a small pile of raw in-shell groundnuts plus one shelled half-peanut placed on top of the pile. Subtle warm rim light.',
         'Heritage / authenticity hook. Signals "real ingredient" before the buyer reads any text. Strongest pull for Indian diaspora search ("groundnut oil") and the "what is this actually made of" Western buyer. May read slightly busier at thumbnail.'),
    ]
    for letter, name, desc, pitch in options:
        story.append(Paragraph(f'Option {letter} — {name}', H3))
        mockup = MainImageOption(letter, name, desc, pitch)
        side = [
            Paragraph(f'<b>Composition:</b> {desc}', BODY),
            Spacer(1, 0.15*cm),
            Paragraph(f'<b>CTR pitch:</b> <i>{pitch}</i>', QUOTE),
        ]
        side_block = Table([[s] for s in side], colWidths=[CONTENT_W - mockup.size - mockup.gap])
        side_block.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'),
                                        ('LEFTPADDING', (0,0), (-1,-1), 0),
                                        ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
        row = Table([[mockup, side_block]], colWidths=[mockup.size + mockup.gap, CONTENT_W - mockup.size - mockup.gap])
        row.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'),
                                 ('LEFTPADDING', (0,0), (-1,-1), 0),
                                 ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
        story.append(KeepTogether([row]))
        story.append(Spacer(1, 0.4*cm))

    story.append(Spacer(1, 0.2*cm))
    rec_box = Table([[Paragraph(
        '<b>Recommended ship-now sequence:</b> Launch with <b>Option A</b> as Image #1 (lowest-risk baseline). '
        'In parallel, prepare B + C as variants. Run A/B/C test via Amazon Manage Your Experiments for 4 weeks. '
        'Promote the winner to permanent Image #1; reuse the other two as supplementary product shots elsewhere in the gallery.', BODY)]],
        colWidths=[CONTENT_W])
    rec_box.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), GOLD),
        ('LEFTPADDING', (0,0), (-1,-1), 12), ('RIGHTPADDING', (0,0), (-1,-1), 12),
        ('TOPPADDING', (0,0), (-1,-1), 10), ('BOTTOMPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(rec_box)

    # ============ 7 LISTING IMAGES ============
    story.append(PageBreak())
    story.append(Paragraph('6 · Seven Listing Images (full set)', H2))
    story.append(HRule())
    story.append(Paragraph('Format for all: 2000 × 2000 px · sRGB · JPG · ≤ 5 MB. The 1 L variant uses an identical 7-image suite, only the hero tin swap to 1 L tin. Image #5 is identical across both variants.', SUB))

    images = [
        (1, 'Click trigger', WHITE, '', '',
         'See "Main Image — 3 Options" above. Test A/B/C; ship the winner.',
         'Three CTR concepts staged as Manage Your Experiments test. Winner becomes the permanent main image.'),
        (2, 'Hook', CREAM, 'Cold-pressed. Never refined.', 'No heat. No solvents. No anti-foam chemicals. Just the seed.',
         'Macro: hands holding raw groundnuts beside the tin, with a slow stream of golden oil pouring into a small black ceramic bowl. Backdrop: weathered wood. No plastic anywhere.',
         'Reverses the buyer\'s #1 fear about refined oils. The "no anti-foam chemicals" line is verbatim from commodity-oil reviews where buyers praise the absence of additives.'),
        (3, 'Educate', CREAM, 'From seed to tin — the wood-press way.', 'Hand-selected groundnuts · wood-pressed · sealed in tin',
         'Three illustrated steps in a warm earthy line-illustration style with CHEKKO gold accents: hand-selected groundnuts → wood-pressed in chekku / ganuga / lakdi ghani → sealed in plastic-free tin.',
         'Owns the heritage cold-press claim. Justifies the price premium and reinforces what no commodity competitor can credibly claim.'),
        (4, 'Desire', GOLD, 'Built for deep frying. Perfect for daily cooking.', 'High smoke point for turkey fry, stir fry, roasting and crisp South Indian classics.',
         'Cinematic shot of golden oil bubbling around a turkey leg or chicken pieces in a heavy cast-iron pot, OR a top-down of a tempered Indian dish (dal tadka, dosa, vada) with the open tin and a small ceramic dispenser jug.',
         'Captures the Q4 turkey-fryer pocket AND the daily Indian cooking pocket in one frame.'),
        (5, 'Clarify + Cross-sell', CREAM, 'Two sizes. One standard.', '1 Liter for daily cooking · 5 Liter for families and frequent frying. Same heritage cold-pressed oil.',
         'Both Chekko Peanut Oil tins side by side: 1L on left, 5L on right (slightly larger). Clean lighting, identical angle, color-coded label band reinforcing variant size.',
         'Solves wrong-size returns and triples basket math. (Identical image used in both 1L and 5L listings.)'),
        (6, 'Trust + defuse spout/shipping', WHITE, 'Sealed in tin. Protected for your kitchen.', 'Light and oxygen destroy delicate cold-pressed oils. Our food-grade tin keeps every drop the way it was pressed — and travels protected.',
         'Centered tin with 4 trust badges: NON-GMO · NO ADDITIVES · WOOD-PRESSED · PLASTIC-FREE TIN. Below: subtle fold-out diagram showing the reinforced seal of the tin protecting from light, oxygen, and shipping impact.',
         'Defuses two real review-driven objections (dented shipping + spout UX) by visibly showing the protection story. Pair with operational spout fix.'),
        (7, 'Close', ROAST, '40+ years of honest oil.', 'Family-rooted · Wood-pressed · Plastic-free tin',
         'Wide environmental shot: a multigenerational hand pouring CHEKKO oil at a sun-lit family table. Sun-filled, golden, candle-warm. Optional faint family-archive vignette in BG.',
         'Closes on identity. The buyer doesn\'t just buy oil — they buy a continuation of a family craft that has been made the same way for 40+ years.'),
    ]

    for slot, role, bg, hl, sub, vis, why in images:
        title_text = f"Image {slot} — {role}"
        story.append(Paragraph(title_text, H3))
        mockup = ImageMockup(slot, role, bg, hl, sub)
        side = []
        if hl:
            side.append(Paragraph(f'<b>Headline:</b> {hl}', BODY))
        if sub:
            side.append(Paragraph(f'<b>Subline:</b> {sub}', BODY))
        side.append(Paragraph(f'<b>Visual:</b> {vis}', BODY))
        side.append(Spacer(1, 0.15*cm))
        side.append(Paragraph(f'<i>Why it works:</i> {why}', QUOTE))
        side_block = Table([[s] for s in side], colWidths=[CONTENT_W - mockup.size - mockup.gap])
        side_block.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'),
                                        ('LEFTPADDING', (0,0), (-1,-1), 0),
                                        ('RIGHTPADDING', (0,0), (-1,-1), 0),
                                        ('TOPPADDING', (0,0), (-1,-1), 0),
                                        ('BOTTOMPADDING', (0,0), (-1,-1), 3)]))
        row = Table([[mockup, side_block]], colWidths=[mockup.size + mockup.gap, CONTENT_W - mockup.size - mockup.gap])
        row.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'),
                                 ('LEFTPADDING', (0,0), (-1,-1), 0),
                                 ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
        story.append(KeepTogether([row]))
        story.append(Spacer(1, 0.45*cm))

    # ============ A+ MODULES ============
    story.append(PageBreak())
    story.append(Paragraph('7 · A+ Premium Content (7 Modules)', H2))
    story.append(HRule())
    story.append(Paragraph('Variant-agnostic — same A+ ships across both 1L + 5L. Banner heroes use the 5L tin (or both tins together) — never a single-variant frame that would confuse the other listing.', SUB))

    modules = [
        (1, 'Full Image', 'Pressed slow. Poured proud.',
         'Heritage cold-pressed cooking oils — sealed in plastic-free tin. 40+ years of Agamahil family craft.',
         CREAM,
         'Cinematic golden-hour shot of a wooden chekku / ganuga press in operation in a clean Indian-craft workshop. CHEKKO 5L tin in foreground, 1L tin slightly behind.'),
        (2, 'Carousel (5 tiles)', 'The Chekko Difference',
         'Cold-pressed · Never refined · Traceable sourcing · Plastic-free tin · Two sizes',
         GOLD,
         '5 tiles, identical lighting and composition: macro of seeds + drop · vial of unrefined vs refined · groundnut field · tin cross-section · 1L+5L tins.'),
        (3, 'Full Image', 'Seed → Wood-press → Tin.',
         'Three steps. Zero shortcuts. The way Indian families have made oil for centuries — now in a kitchen-ready format.',
         CREAM,
         'Three-step horizontal layout: hand-selected groundnuts → wood-pressed in chekku / ganuga → sealed in tin. Earthy palette.'),
        (4, 'Full Image', 'Deep fry. Temper. Sauté. Roast.',
         'High smoke point for high-heat cooking — cold-pressed clarity for everyday meals.',
         ROAST,
         'Triptych within one banner: LEFT golden oil bubbling in a deep-fry pot with chicken or turkey · CENTER tempering whole spices in a steel kadai · RIGHT pouring oil onto a hot cast-iron tawa for dosa.'),
        (5, 'Carousel (5 tiles)', 'The Chekko Family',
         'Peanut · Sesame · Coconut · Mustard / Kachi Ghani · Sunflower or Castor',
         GOLD,
         'Same lighting and composition across all tiles. Color-coded label band per oil. Footer: "Explore the full Chekko family of cold-pressed heritage oils."'),
        (6, 'Q&A', 'Defuses top objections',
         'Price · Allergy honesty · Foaming · Why tin?',
         CREAM,
         'Four Q&A pairs — see the table below for the full text.'),
        (7, 'Comparison Chart', 'Make the price make sense',
         'Chekko vs refined supermarket · vs roasted · vs generic cold-pressed',
         CREAM,
         'Highlight Chekko column with subtle gold tint and a maroon RECOMMENDED ribbon. See the table on the next page.'),
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
        side_block.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'),
                                        ('LEFTPADDING', (0,0), (-1,-1), 0),
                                        ('RIGHTPADDING', (0,0), (-1,-1), 0),
                                        ('TOPPADDING', (0,0), (-1,-1), 0),
                                        ('BOTTOMPADDING', (0,0), (-1,-1), 3)]))
        row = Table([[mockup, side_block]], colWidths=[mockup.banner_w + mockup.gap, CONTENT_W - mockup.banner_w - mockup.gap])
        row.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'),
                                 ('LEFTPADDING', (0,0), (-1,-1), 0),
                                 ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
        story.append(KeepTogether([row]))
        story.append(Spacer(1, 0.4*cm))

    # ============ Q&A + COMPARISON CHART ============
    story.append(PageBreak())
    story.append(Paragraph('A+ Module 6 — Premium Q&amp;A (full copy)', H3))
    qa = [
        ('Why is Chekko more expensive than supermarket peanut oil?',
         'Cold-pressed extraction yields about 40% of the oil that refined extraction does, and we use no chemicals to push more out. You are paying for the seed, the slow press, and the tin — nothing else.'),
        ('Is this allergy-safe for someone with a peanut allergy?',
         '<b>No.</b> Refined peanut oil is generally considered allergy-safe because the proteins are processed out. Chekko is cold-pressed and unrefined — it retains natural peanut compounds. If anyone in your home has a peanut allergy, choose a refined peanut oil.'),
        ('Why does it foam when I first heat it?',
         'Light foam is normal in fresh cold-pressed oil. Refined oils suppress it with anti-foaming agents — we don\'t.'),
        ('Why a tin and not a plastic bottle?',
         'Light, oxygen, and plastic leaching all degrade delicate cold-pressed oils. Our food-grade tin protects flavor, freshness, and your kitchen.'),
    ]
    qa_table = Table([[Paragraph(f'<b>Q{i+1}.</b> {q}', BODY), Paragraph(a, BODY)] for i, (q, a) in enumerate(qa)],
                     colWidths=[6.5*cm, CONTENT_W - 6.5*cm])
    qa_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), CREAM),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LINEBELOW', (0,0), (-1,-1), 0.3, HexColor('#E0DCC8')),
        ('LEFTPADDING', (0,0), (-1,-1), 10), ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 8), ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(qa_table)

    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph('A+ Module 7 — Premium Comparison Chart', H3))
    comp = [
        ['Feature', 'Chekko\nCold-Pressed Peanut', 'Refined supermarket peanut', 'Roasted peanut\n(different product)', 'Generic cold-pressed peanut'],
        ['Extraction', 'Wood-pressed cold', 'Refined high-temp', 'Roasted then pressed', 'Often expeller'],
        ['Anti-foaming additives', 'None', 'Often', 'None', 'Often'],
        ['Solvents / hexane', 'None', 'Sometimes', 'None', 'Sometimes'],
        ['Packaging', 'Tin (plastic-free)', 'Plastic', 'Plastic / glass', 'Often plastic'],
        ['Single-origin / traceable', 'Yes', 'Rarely', 'Rarely', 'Rarely'],
        ['Heritage method', 'Wood-press chekku/ganuga', 'Industrial', 'Various', 'Various'],
        ['Use cases', 'Deep fry · Temper · Sauté · Roast', 'Deep fry', 'Finish-cook only', 'Cook'],
    ]
    comp_table = Table(comp, colWidths=[3.4*cm, 3.6*cm, 3.4*cm, 3.4*cm, 3.0*cm])
    comp_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), MAROON),
        ('TEXTCOLOR', (0,0), (-1,0), WHITE),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('BACKGROUND', (1,1), (1,-1), HexColor('#FFF8DC')),
        ('FONTNAME', (1,1), (1,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8.5),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('LEFTPADDING', (0,0), (-1,-1), 5), ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ('TOPPADDING', (0,0), (-1,-1), 5), ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('GRID', (0,0), (-1,-1), 0.3, HexColor('#CCCCCC')),
        ('ROWBACKGROUNDS', (0,1), (0,-1), [WHITE, CREAM]),
        ('ROWBACKGROUNDS', (2,1), (-1,-1), [WHITE, CREAM]),
    ]))
    story.append(comp_table)

    # ============ MASTER COPY ============
    story.append(PageBreak())
    story.append(Paragraph('8 · Master Copy (paste-ready)', H2))
    story.append(HRule())

    story.append(Paragraph('Title — 1 L (~199 chars)', H3))
    title_box_1L = Table([[Paragraph(
        '<b>Chekko Cold-Pressed Peanut Oil 1 L (33 Fl Oz) Tin — 100% Pure Wood-Pressed Groundnut Oil · Unrefined for Deep Frying, Stir-Fry &amp; Daily Cooking · Non-GMO · Plastic-Free · 40+ Year Heritage</b>', BODY)]],
        colWidths=[CONTENT_W])
    title_box_1L.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), GOLD),
        ('LEFTPADDING', (0,0), (-1,-1), 12), ('RIGHTPADDING', (0,0), (-1,-1), 12),
        ('TOPPADDING', (0,0), (-1,-1), 8), ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(title_box_1L)

    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph('Title — 5 L (~199 chars)', H3))
    title_box_5L = Table([[Paragraph(
        '<b>Chekko Cold-Pressed Peanut Oil 5 L (169 Fl Oz) Bulk Tin — 100% Pure Wood-Pressed Groundnut Oil · Unrefined for Turkey Fry, Deep Frying &amp; Family Cooking · Non-GMO · Plastic-Free · 40+ Year Heritage</b>', BODY)]],
        colWidths=[CONTENT_W])
    title_box_5L.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), GOLD),
        ('LEFTPADDING', (0,0), (-1,-1), 12), ('RIGHTPADDING', (0,0), (-1,-1), 12),
        ('TOPPADDING', (0,0), (-1,-1), 8), ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(title_box_5L)

    story.append(Spacer(1, 0.4*cm))
    story.append(Paragraph('Bullets (shared across both variants)', H3))
    bullets = [
        ('UNCOMPROMISED PURITY',
         'Chekko peanut oil is cold-pressed from carefully selected Non-GMO groundnuts with no additives, no fillers, and no anti-foaming chemicals. A clean, unrefined cooking oil for families who care about every ingredient.'),
        ('TRADITIONAL WOOD PRESSING',
         'Slowly extracted using the heritage chekku / ganuga / lakdi ghani wood-press method, this groundnut oil preserves natural aroma, mild nutty taste, and nutrients for Indian, South Indian, Asian, and everyday cooking.'),
        ('BUILT FOR HIGH-HEAT COOKING',
         'A naturally high smoke point makes this peanut oil ideal for deep frying turkey, frying chicken, stir-fry, pan-frying, roasting, grilling, baking, and crisp tempering on cast iron.'),
        ('SEALED FRESH IN PLASTIC-FREE TIN',
         'Cold-pressed oils are delicate. Our food-grade tin shields the oil from light, oxygen, and plastic — keeping aroma, flavor, and nutrients exactly the way they were pressed. Choose 1 L for daily cooking or 5 L for families and frequent frying.'),
        ('BUILT ON TRUST, NOT SHORTCUTS',
         'Backed by 40+ years of Agamahil family oil-making heritage, Chekko is made with disciplined care for households who believe honest meals start with honest oil.'),
    ]
    bt = Table([[Paragraph(f'<b>{i+1}. {h}</b>', BODY), Paragraph(b, BODY)] for i, (h, b) in enumerate(bullets)],
               colWidths=[5.8*cm, CONTENT_W - 5.8*cm])
    bt.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), CREAM),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LINEBELOW', (0,0), (-1,-1), 0.3, HexColor('#E0DCC8')),
        ('LEFTPADDING', (0,0), (-1,-1), 10), ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 7), ('BOTTOMPADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(bt)

    story.append(Spacer(1, 0.4*cm))
    story.append(Paragraph('Backend search terms (≤ 250 bytes — Grocery)', H3))
    be = Table([[Paragraph(
        '<font face="Courier" size="8">peanut oil cold pressed wood pressed groundnut oil for deep frying turkey fryer cooking unrefined natural high heat smoke point chekku ganuga lakdi ghani kachi non gmo tin no additives indian asian south indian</font>', BODY)]],
        colWidths=[CONTENT_W])
    be.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), HexColor('#F5F5F5')),
        ('LEFTPADDING', (0,0), (-1,-1), 10), ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 8), ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(be)

    story.append(Spacer(1, 0.4*cm))
    story.append(Paragraph('Compliance notes', H3))
    for line in [
        '<b>NEVER</b> claim "allergy-safe" or "allergen-free" — cold-pressed peanut oil retains natural allergens.',
        'No competitor brand names (Lou Ana, Louana, PLANTERS, Amazon, Whole Foods, Gramiyaa).',
        'No health/medical claims — describe the cooking practice, not the medical outcome.',
        '"Non-GMO" only if certified or supported. If not, soften to "natural" / "no additives".',
        '"40+ years of Agamahil heritage" — confirm exact wording with the client.',
        'Avoid "best", "#1", "ultimate".',
    ]:
        story.append(Paragraph('• ' + line, BODY))

    # ============ PRIORITY UPLIFTS ============
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph('9 · Priority uplifts (CTR × CVR)', H2))
    story.append(HRule())
    pri = [
        ('1', 'Operational: redesign tin spout + improve FBA shipping protection', 'Single biggest lever on the rating — multiple buyers love the oil but flag the spout. Lifts past 4.5★.'),
        ('2', 'Publish A+ Module 7 Comparison Chart', 'Defuses sticker shock vs. Amazon Grocery / PLANTERS commodity oils.'),
        ('3', 'Publish A+ Module 6 Q&A (incl. allergy honesty)', 'Defuses the four biggest buying objections at once.'),
        ('4', 'Run Main Image A/B/C test (Manage Your Experiments)', 'Highest CTR lift available without operational change.'),
        ('5', 'Enable Subscribe & Save + launch coupon', 'Grocery LTV + CTR badge density.'),
        ('6', 'Publish A+ Module 1 heritage banner (chekku/ganuga press shoot)', 'One shoot powers both 1L + 5L A+ + future Coconut / Mustard / Sunflower listings.'),
    ]
    pri_table = Table([[Paragraph(f'<b>{n}</b>', BODY), Paragraph(f'<b>{t}</b>', BODY), Paragraph(d, BODY)] for n, t, d in pri],
                      colWidths=[1*cm, 6.5*cm, CONTENT_W - 7.5*cm])
    pri_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), MAROON),
        ('TEXTCOLOR', (0,0), (0,-1), WHITE),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LINEBELOW', (0,0), (-1,-1), 0.3, HexColor('#E0DCC8')),
        ('LEFTPADDING', (0,0), (-1,-1), 8), ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 7), ('BOTTOMPADDING', (0,0), (-1,-1), 7),
        ('ROWBACKGROUNDS', (1,0), (-1,-1), [WHITE, CREAM]),
    ]))
    story.append(pri_table)

    doc.build(story)
    print(f'PDF: {OUT}')

if __name__ == '__main__':
    build()
