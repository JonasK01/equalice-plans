#!/usr/bin/env python3
"""Render the CHEKKO Sesame Oil brief as a properly designed PDF with visual image mockups."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.units import cm, mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    KeepTogether, Image, Frame, BaseDocTemplate, PageTemplate
)
from reportlab.platypus.flowables import Flowable
from reportlab.pdfgen.canvas import Canvas
import os

OUT = '/Users/jonask/Desktop/CHEKKO Sesame Oil Brief.pdf'

# CHEKKO brand palette
GOLD   = HexColor('#EFC522')
MAROON = HexColor('#65161A')
CREAM  = HexColor('#F7F0DD')
ROAST  = HexColor('#3A2A1F')
INK    = HexColor('#111111')
GREY   = HexColor('#666666')
LIGHT  = HexColor('#F5F0E6')
WHITE  = HexColor('#FFFFFF')

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
BODY_BOLD = ParagraphStyle('BodyBold', parent=BODY, fontName='Helvetica-Bold')
SMALL = ParagraphStyle('Small', parent=BODY, fontSize=9, leading=12, textColor=GREY)
QUOTE = ParagraphStyle('Quote', parent=BODY, fontName='Helvetica-Oblique', textColor=GREY)
CAPTION = ParagraphStyle('Caption', parent=BODY, fontSize=8, leading=10, textColor=GREY, alignment=TA_CENTER)
LABEL = ParagraphStyle('Label', parent=BODY, fontSize=9, fontName='Helvetica-Bold', textColor=MAROON)


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
    """Color swatch with HEX label below."""
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
        # Color block
        c.setFillColor(self.color)
        c.setStrokeColor(HexColor('#DDDDDD'))
        c.setLineWidth(0.3)
        c.rect(0, 0.9*cm, self.w, self.h, fill=1, stroke=1)
        # Label
        c.setFillColor(INK)
        c.setFont('Helvetica-Bold', 9)
        c.drawString(0, 0.45*cm, self.label_top)
        c.setFillColor(GREY)
        c.setFont('Helvetica', 8)
        c.drawString(0, 0.15*cm, self.label_bottom)


class ImageMockup(Flowable):
    """A 2000x2000 listing image mockup, drawn at scale on the page."""
    def __init__(self, slot_num, role, bg_hex, headline, sub, visual_desc, side_w=8.5*cm):
        self.slot = slot_num
        self.role = role
        self.bg = HexColor(bg_hex) if isinstance(bg_hex, str) else bg_hex
        self.headline = headline
        self.sub = sub
        self.visual = visual_desc
        # Mockup is square (the listing image), with side panel for description
        self.mockup_size = 6.5*cm
        self.side_w = side_w
        self.gap = 0.4*cm
        self.total_w = self.mockup_size + self.gap + self.side_w
        Flowable.__init__(self)

    def wrap(self, *args):
        return (self.total_w, self.mockup_size + 0.5*cm)

    def draw(self):
        c = self.canv
        s = self.mockup_size
        # === Mockup square ===
        # BG
        c.setFillColor(self.bg)
        c.setStrokeColor(HexColor('#CCCCCC'))
        c.setLineWidth(0.4)
        c.rect(0, 0, s, s, fill=1, stroke=1)
        # Slot number tag (top-left)
        c.setFillColor(MAROON)
        c.rect(0, s - 0.7*cm, 1.4*cm, 0.7*cm, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont('Helvetica-Bold', 11)
        c.drawCentredString(0.7*cm, s - 0.5*cm, f'#{self.slot}')
        # 2000x2000 dim caption (bottom)
        c.setFillColor(GREY)
        c.setFont('Helvetica', 7)
        c.drawCentredString(s/2, 0.15*cm, '2000 × 2000 px')
        # Headline preview inside the mockup (faked)
        if self.headline:
            text_color = MAROON if self.bg in (CREAM, WHITE, LIGHT) else WHITE
            c.setFillColor(text_color)
            c.setFont('Helvetica-Bold', 10)
            # Wrap headline into max 3 lines
            words = self.headline.upper().split()
            lines = []
            cur = ''
            for w in words:
                trial = (cur + ' ' + w).strip()
                if c.stringWidth(trial, 'Helvetica-Bold', 10) > s - 0.8*cm:
                    if cur: lines.append(cur)
                    cur = w
                else:
                    cur = trial
            if cur: lines.append(cur)
            lines = lines[:3]
            y = s/2 + (len(lines)-1) * 6
            for line in lines:
                c.drawCentredString(s/2, y, line)
                y -= 12
            # Sub
            if self.sub:
                c.setFont('Helvetica-Oblique', 7.5)
                sub_lines = []
                cur = ''
                for w in self.sub.split():
                    trial = (cur + ' ' + w).strip()
                    if c.stringWidth(trial, 'Helvetica-Oblique', 7.5) > s - 0.8*cm:
                        if cur: sub_lines.append(cur)
                        cur = w
                    else:
                        cur = trial
                if cur: sub_lines.append(cur)
                sub_lines = sub_lines[:2]
                yy = s/2 - len(lines)*6 - 8
                for sl in sub_lines:
                    c.drawCentredString(s/2, yy, sl)
                    yy -= 9
        else:
            # No-overlay marker
            c.setFillColor(GREY)
            c.setFont('Helvetica-Oblique', 8)
            c.drawCentredString(s/2, s/2, '(hero — no overlay)')

        # Role tag at bottom-right
        c.setFillColor(GOLD)
        role_w = c.stringWidth(self.role.upper(), 'Helvetica-Bold', 7) + 0.4*cm
        c.rect(s - role_w, 0, role_w, 0.5*cm, fill=1, stroke=0)
        c.setFillColor(INK)
        c.setFont('Helvetica-Bold', 7)
        c.drawString(s - role_w + 0.2*cm, 0.18*cm, self.role.upper())


class APlusMockup(Flowable):
    """A 1464x600 A+ banner mockup, drawn at scale."""
    def __init__(self, slot_num, module_type, headline, sub, theme_color=CREAM, side_w=7.5*cm):
        self.slot = slot_num
        self.module_type = module_type
        self.headline = headline
        self.sub = sub
        self.bg = theme_color
        self.banner_w = 9.5*cm
        self.banner_h = 9.5*cm * (600/1464)  # ~3.9cm
        self.side_w = side_w
        self.gap = 0.4*cm
        self.total_w = self.banner_w + self.gap + self.side_w
        Flowable.__init__(self)

    def wrap(self, *args):
        return (self.total_w, self.banner_h + 0.5*cm)

    def draw(self):
        c = self.canv
        w, h = self.banner_w, self.banner_h
        # BG
        c.setFillColor(self.bg)
        c.setStrokeColor(HexColor('#CCCCCC'))
        c.setLineWidth(0.4)
        c.rect(0, 0.5*cm, w, h, fill=1, stroke=1)
        # Module tag
        c.setFillColor(MAROON)
        c.rect(0, 0.5*cm + h - 0.55*cm, 2.6*cm, 0.55*cm, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont('Helvetica-Bold', 8)
        c.drawString(0.15*cm, 0.5*cm + h - 0.4*cm, f'MODULE {self.slot}')
        # Headline (centered)
        text_color = MAROON if self.bg in (CREAM, WHITE, LIGHT) else WHITE
        c.setFillColor(text_color)
        c.setFont('Helvetica-Bold', 11)
        if self.headline:
            words = self.headline.upper().split()
            lines = []
            cur = ''
            for word in words:
                trial = (cur + ' ' + word).strip()
                if c.stringWidth(trial, 'Helvetica-Bold', 11) > w - 1*cm:
                    if cur: lines.append(cur)
                    cur = word
                else:
                    cur = trial
            if cur: lines.append(cur)
            lines = lines[:2]
            y = 0.5*cm + h/2 + (len(lines)-1)*6 + 0.2*cm
            for line in lines:
                c.drawCentredString(w/2, y, line)
                y -= 13
            if self.sub:
                c.setFont('Helvetica-Oblique', 8)
                c.setFillColor(GREY if self.bg in (CREAM, WHITE, LIGHT) else WHITE)
                sub_lines = []
                cur = ''
                for word in self.sub.split():
                    trial = (cur + ' ' + word).strip()
                    if c.stringWidth(trial, 'Helvetica-Oblique', 8) > w - 1*cm:
                        if cur: sub_lines.append(cur)
                        cur = word
                    else:
                        cur = trial
                if cur: sub_lines.append(cur)
                sub_lines = sub_lines[:1]
                yy = 0.5*cm + h/2 - len(lines)*6 - 4
                for sl in sub_lines:
                    c.drawCentredString(w/2, yy, sl)
        # Type tag bottom
        c.setFillColor(GOLD)
        type_w = c.stringWidth(self.module_type.upper(), 'Helvetica-Bold', 7) + 0.3*cm
        c.rect(w - type_w, 0.5*cm, type_w, 0.4*cm, fill=1, stroke=0)
        c.setFillColor(INK)
        c.setFont('Helvetica-Bold', 7)
        c.drawString(w - type_w + 0.15*cm, 0.5*cm + 0.13*cm, self.module_type.upper())
        # Dim caption
        c.setFillColor(GREY)
        c.setFont('Helvetica', 6.5)
        c.drawCentredString(w/2, 0.15*cm, '1464 × 600 px desktop · 600 × 450 mobile')


def header_footer(canvas, doc):
    """Brand header and page footer on every page."""
    canvas.saveState()
    # Top hairline
    canvas.setStrokeColor(GOLD)
    canvas.setLineWidth(2.5)
    canvas.line(MARGIN_L, PAGE_H - 1.0*cm, PAGE_W - MARGIN_R, PAGE_H - 1.0*cm)
    # Brand mark left
    canvas.setFillColor(MAROON)
    canvas.setFont('Helvetica-Bold', 9)
    canvas.drawString(MARGIN_L, PAGE_H - 0.7*cm, 'CHEKKO')
    canvas.setFillColor(GREY)
    canvas.setFont('Helvetica', 8)
    canvas.drawString(MARGIN_L + 1.6*cm, PAGE_H - 0.7*cm, 'Cold-Pressed Sesame Oil 1 L · Amazon US Brief')
    # Page number right
    canvas.setFillColor(GREY)
    canvas.setFont('Helvetica', 8)
    canvas.drawRightString(PAGE_W - MARGIN_R, PAGE_H - 0.7*cm, f'Page {doc.page}')
    # Footer
    canvas.setStrokeColor(HexColor('#E0DCC8'))
    canvas.setLineWidth(0.4)
    canvas.line(MARGIN_L, MARGIN_B - 0.4*cm, PAGE_W - MARGIN_R, MARGIN_B - 0.4*cm)
    canvas.setFillColor(GREY)
    canvas.setFont('Helvetica', 7.5)
    canvas.drawString(MARGIN_L, MARGIN_B - 0.7*cm, 'Prepared by EQUALICE — 2026-05-05 · ASIN B079K4D69K')
    canvas.restoreState()


def cover_page(canvas, doc):
    """Cover page custom design."""
    canvas.saveState()
    # Cream wash
    canvas.setFillColor(CREAM)
    canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    # Gold band top
    canvas.setFillColor(GOLD)
    canvas.rect(0, PAGE_H - 4*cm, PAGE_W, 4*cm, fill=1, stroke=0)
    # Maroon strip
    canvas.setFillColor(MAROON)
    canvas.rect(0, PAGE_H - 4.4*cm, PAGE_W, 0.4*cm, fill=1, stroke=0)
    # Title
    canvas.setFillColor(MAROON)
    canvas.setFont('Helvetica-Bold', 38)
    canvas.drawString(MARGIN_L, PAGE_H - 2.6*cm, 'CHEKKO')
    canvas.setFont('Helvetica', 16)
    canvas.setFillColor(INK)
    canvas.drawString(MARGIN_L, PAGE_H - 3.4*cm, 'Cold-Pressed Sesame Oil 1 L')
    # Subtitle
    canvas.setFillColor(MAROON)
    canvas.setFont('Helvetica-Bold', 22)
    canvas.drawString(MARGIN_L, PAGE_H - 7*cm, 'Amazon US Listing Brief')
    canvas.setFillColor(GREY)
    canvas.setFont('Helvetica', 13)
    canvas.drawString(MARGIN_L, PAGE_H - 7.8*cm, 'Image Plan · A+ Premium · Moodboard')
    # Meta block bottom
    y = 5*cm
    canvas.setFillColor(MAROON)
    canvas.setFont('Helvetica-Bold', 9)
    canvas.drawString(MARGIN_L, y, 'HERO ASIN')
    canvas.drawString(MARGIN_L + 5*cm, y, 'MARKETPLACE')
    canvas.drawString(MARGIN_L + 10*cm, y, 'PACK')
    canvas.drawString(MARGIN_L + 14*cm, y, 'DATE')
    canvas.setFillColor(INK)
    canvas.setFont('Helvetica', 11)
    canvas.drawString(MARGIN_L, y - 0.55*cm, 'B079K4D69K')
    canvas.drawString(MARGIN_L + 5*cm, y - 0.55*cm, 'amazon.com')
    canvas.drawString(MARGIN_L + 10*cm, y - 0.55*cm, '1 L · 33 Fl Oz tin')
    canvas.drawString(MARGIN_L + 14*cm, y - 0.55*cm, '2026-05-05')
    # Bottom strip
    canvas.setFillColor(MAROON)
    canvas.rect(0, 0, PAGE_W, 1.4*cm, fill=1, stroke=0)
    canvas.setFillColor(GOLD)
    canvas.setFont('Helvetica-Bold', 10)
    canvas.drawString(MARGIN_L, 0.5*cm, 'PRESSED SLOW. POURED PROUD.')
    canvas.setFillColor(WHITE)
    canvas.setFont('Helvetica', 9)
    canvas.drawRightString(PAGE_W - MARGIN_R, 0.5*cm, 'Prepared by EQUALICE')
    canvas.restoreState()


# ---------- Build the document ----------
def build():
    doc = BaseDocTemplate(OUT, pagesize=A4,
                          leftMargin=MARGIN_L, rightMargin=MARGIN_R,
                          topMargin=MARGIN_T, bottomMargin=MARGIN_B,
                          title='CHEKKO Cold-Pressed Sesame Oil 1 L — Amazon US Brief',
                          author='EQUALICE')

    cover_frame = Frame(MARGIN_L, MARGIN_B, CONTENT_W, PAGE_H - MARGIN_T - MARGIN_B,
                        leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0,
                        showBoundary=0)
    body_frame = Frame(MARGIN_L, MARGIN_B, CONTENT_W, PAGE_H - MARGIN_T - MARGIN_B,
                       leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0,
                       showBoundary=0)

    cover_template = PageTemplate(id='Cover', frames=[cover_frame], onPage=cover_page)
    body_template = PageTemplate(id='Body', frames=[body_frame], onPage=header_footer)

    doc.addPageTemplates([cover_template, body_template])

    story = []
    # === COVER (template handles drawing; just push page) ===
    story.append(Spacer(1, 1))
    story.append(PageBreak())
    # Switch to body template
    story.append(NextPageTemplate('Body'))
    story.append(PageBreak())

    # ============ SECTION 1: AT A GLANCE ============
    story.append(Paragraph('At a glance', H2))
    story.append(HRule())
    glance = [
        ['Brand', 'CHEKKO — heritage Indian cold-pressed oils (Agamahil family, 40+ years)'],
        ['Hero product', 'Cold-Pressed Sesame Oil · 1 L (33 Fl Oz) plastic-free tin'],
        ['Hero ASIN', 'B079K4D69K'],
        ['Current rank', 'BSR #79 in Sesame Oils · 4.3★'],
        ['Strategic shift', 'Culinary-only → culinary + Ayurvedic / multi-use (the bigger search pocket)'],
        ['Brand DNA', 'Heritage · cold-pressed · plastic-free tin · traceable · multi-use'],
        ['No-gos', 'No plastic packaging or plastic-looking elements · no funky / loud / playful styling · no over-processed imagery'],
    ]
    t = Table([[Paragraph(f'<b>{k}</b>', BODY), Paragraph(v, BODY)] for k, v in glance],
              colWidths=[3.6*cm, CONTENT_W - 3.6*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), CREAM),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LINEBELOW', (0,0), (-1,-1), 0.3, HexColor('#E0DCC8')),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t)

    # ============ SECTION 2: BRANDBOOK ============
    story.append(Spacer(1, 0.6*cm))
    story.append(Paragraph('1 · Brandbook', H2))
    story.append(HRule())
    story.append(Paragraph('Identity', H3))
    story.append(Paragraph('<b>Brand:</b> CHEKKO', BODY))
    story.append(Paragraph('<b>Voice:</b> Calm, grounded, ancestral. <i>"Pressed slow. Poured proud."</i>', BODY))
    story.append(Paragraph('<b>Personality:</b> Modern + Luxurious + Creative/Original (per onboarding)', BODY))

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
        'Real ingredients (sesame seeds, oil, ceramic, wood, linen).',
        'Hands only — no faces unless explicit lifestyle shoot.',
        'Warm side-light. Avoid hard ringlight or cold studio.',
        '<b>NEVER</b> plastic bottles, plastic dispensers, or plastic-looking surfaces in frame.',
        'Stock photos allowed; product can be photoshopped in if it looks real.',
    ]:
        story.append(Paragraph('• ' + line, BODY))

    story.append(Paragraph('Creative freedom', H3))
    story.append(Paragraph('<b>4 / 5</b> — push the design, but stay anchored to brand files.', BODY))

    # ============ SECTION 3: BUYER PSYCHOLOGY ============
    story.append(PageBreak())
    story.append(Paragraph('2 · Buyer Psychology', H2))
    story.append(HRule())
    story.append(Paragraph(
        'The Indian / South Asian US household wants the heritage cold-pressed oil their parents used, in a US-friendly format. '
        'The wellness-curious Western buyer wants a clean, multi-use natural oil with traceable origin and non-plastic packaging — '
        'they oil-pull, they Abhyanga, they distrust supermarket oils. '
        'CHEKKO\'s brand DNA fits both — but the current listing copy only speaks to the cooking buyer.', BODY))
    story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph('Top three buying triggers', H3))
    triggers = [
        ('Quality fear', 'Distrust of refined oils, hexane extraction, anti-foaming agents.'),
        ('Heritage / authenticity', '"The oil my grandmother cooked with" — strong for Indian diaspora; rising for Western buyers seeking ancestral methods.'),
        ('Plastic fatigue', 'Growing distaste for plastic in food. Tin is a brand-aligned rare differentiator.'),
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
    story.append(Paragraph('Top three friction points to defuse', H3))
    frictions = [
        ('Tin shipping damage', 'Visually show the reinforced packaging in image #6.'),
        ('Foaming = bad oil', 'Explain in A+ Q&A: cold-pressed oils naturally foam; refined oils suppress with anti-foam agents.'),
        ('Sticker shock', 'Justify with cold-press yield (1 kg seeds → ~0.4 L oil) + traceable origin + multi-use + tin.'),
    ]
    t = Table([[Paragraph(f'<b>{k}</b>', BODY), Paragraph(v, BODY)] for k, v in frictions],
              colWidths=[4.5*cm, CONTENT_W - 4.5*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), HexColor('#F8E5E5')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LINEBELOW', (0,0), (-1,-1), 0.3, HexColor('#E0DCC8')),
        ('LEFTPADDING', (0,0), (-1,-1), 8), ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 6), ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t)

    # ============ SECTION 4: MOODBOARD ============
    story.append(PageBreak())
    story.append(Paragraph('3 · Moodboard', H2))
    story.append(HRule())

    story.append(Paragraph('Overall direction', H3))
    story.append(Paragraph(
        '<b>Warm. Heritage. Ancestral. Modern luxury without gloss.</b> A heirloom-cookbook aesthetic '
        'lit by golden hour through a kitchen window. The oil itself is the hero — pour shots, drop shots, '
        'rim-light on the tin.', BODY))

    # Mood swatches large
    story.append(Spacer(1, 0.4*cm))
    story.append(Paragraph('Dominant tones', H3))
    big_chips = [
        ColorChip(GOLD, '#EFC522', 'Golden Yellow', w=3.6*cm, h=2.6*cm),
        ColorChip(CREAM, '#F7F0DD', 'Warm Cream', w=3.6*cm, h=2.6*cm),
        ColorChip(MAROON, '#65161A', 'Deep Maroon', w=3.6*cm, h=2.6*cm),
        ColorChip(ROAST, '#3A2A1F', 'Roasted Brown', w=3.6*cm, h=2.6*cm),
    ]
    bc = Table([big_chips], colWidths=[CONTENT_W/4]*4)
    bc.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),
                            ('LEFTPADDING',(0,0),(-1,-1),0), ('RIGHTPADDING',(0,0),(-1,-1),6)]))
    story.append(bc)

    story.append(Spacer(1, 0.4*cm))
    story.append(Paragraph('Five lifestyle scenes', H3))
    scenes = [
        ('1. The pour', 'Slow stream of golden oil falling into a small ceramic bowl, held in a hand. Black ceramic, weathered wood, natural light.'),
        ('2. The press', 'Stone or wooden ghani (traditional cold-press) in a clean Indian-craft workshop. Sun-shaft, dust motes, no machinery glow.'),
        ('3. The kitchen', 'A finished plate (dosa, stir-fry, dressed salad) with the open Chekko tin and a small glass dispenser jug. Linen, wood, ceramic. No stainless, no plastic.'),
        ('4. The body', 'Golden oil dropping into an open palm. Implied Abhyanga (Ayurvedic massage) or hair oiling. Bare wood floor, warm light, folded cotton towel.'),
        ('5. The family table', 'Multigenerational hand pouring oil at a sun-lit family table. Warm, candle-light feel. Recipe card or bowl of seeds in soft focus.'),
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

    # Props
    story.append(Spacer(1, 0.5*cm))
    yes_no = Table([
        [Paragraph('<b>PROPS ALLOWED</b>', LABEL), Paragraph('<b>PROPS NEVER ALLOWED</b>', LABEL)],
        [Paragraph('Sesame seeds (raw + toasted) · ceramic bowls (matte black, terracotta) · weathered wood · linen · cast iron · woven baskets · cotton towels · glass jars · dried herbs · fresh garlic / ginger / scallion · cooked Indian and Asian dishes', BODY),
         Paragraph('Plastic bottles · plastic measuring cups · plastic-looking dispensers · stainless-steel modern minimalism · white Scandi marble · "diverse-family-laughing" stock · anything that reads "supermarket"', BODY)],
    ], colWidths=[CONTENT_W/2 - 0.2*cm, CONTENT_W/2 - 0.2*cm])
    yes_no.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), HexColor('#E8F5E9')),
        ('BACKGROUND', (1,0), (1,-1), HexColor('#FFEBEE')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 10), ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 8), ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('BOX', (0,0), (-1,-1), 0.3, HexColor('#CCCCCC')),
    ]))
    story.append(yes_no)

    # ============ SECTION 5: 7 LISTING IMAGES ============
    story.append(PageBreak())
    story.append(Paragraph('4 · Seven Listing Images', H2))
    story.append(HRule())
    story.append(Paragraph('Format for all: 2000 × 2000 px · sRGB · JPG · ≤ 5 MB', SUB))

    images = [
        (1, 'Click trigger', WHITE, '', '',
         'The 1L Chekko sesame oil tin centered, three-quarter elevated angle, label fully readable, warm rim light to make the gold label glow against white. Tight crop ~85% frame height. No graphics, no overlay (Amazon main-image policy).',
         'A warm-lit tin with a glowing gold label cuts through a search grid full of clear plastic bottles. Buyers immediately read "premium tin packaging" before they read the label.'),
        (2, 'Hook', CREAM, 'Cold-pressed. Never refined.', 'No heat, no chemicals, no hidden additives.',
         'Macro: a hand cradles raw sesame seeds beside the tin while a slow stream of golden oil pours into a small black ceramic bowl. Backdrop: weathered wood. No plastic anywhere.',
         'Reverses the buyer\'s #1 fear (refined oils with hexane and anti-foaming agents) with a single visual that promises the opposite.'),
        (3, 'Educate', CREAM, 'From seed to tin — 3 steps, zero shortcuts.', 'Hand-selected seeds · cold-pressed · sealed in tin',
         'Three illustrated steps along the frame in a warm earthy line-illustration style with Chekko gold accents: hand-selected sesame seeds → cold-pressed at low temperature in a stone ghani → sealed fresh in a plastic-free tin.',
         'Owns the cold-pressed claim with a visible production story. Justifies the premium price and reinforces the heritage angle.'),
        (4, 'Desire', GOLD, 'Everyday cooking. Extraordinary depth.', 'Mild and nutty — built for stir-fry, marinades, dressings, Indian and Asian classics.',
         'Cinematic top-down: a plated Indian / Asian dish in a dark ceramic bowl, the open Chekko tin and a small glass dispenser jug beside it, scattered toasted sesame seeds. Warm side light. Wood and linen. No plastic, no stainless.',
         'Places the buyer in their own kitchen and makes the oil the protagonist. Sells the experience of the meal, not the tin.'),
        (5, 'Trust + Cross-sell', CREAM, 'One oil. Three traditions.', 'Cook · Anoint · Nourish — used in Indian kitchens and Ayurvedic rituals for over a thousand years.',
         'Triptych on warm cream. LEFT: cooking pour over a hot wok. CENTER: golden oil dropping into a hand for Abhyanga / scalp massage. RIGHT: oil pulling / morning ritual. Hands only, no faces.',
         'The strategic image. Captures the wellness search pocket without losing the cooking buyer — the frame says "you can do all three."'),
        (6, 'Trust', WHITE, 'Sealed in tin. Never plastic.', 'Light and air destroy delicate cold-pressed oils. Our food-grade tin keeps every drop the way it was pressed.',
         'Centered tin surrounded by 4 trust badges (NON-GMO · NO ADDITIVES · TRACEABLE SOURCING · PLASTIC-FREE TIN) and a subtle fold-out diagram of the protected double-seal of the tin.',
         'Defuses two objections in one frame: the plastic-fatigue trigger and the "tin damaged in shipping" concern by visibly showing how the seal protects the oil.'),
        (7, 'Close', ROAST, 'Made the way your grandmother made it.', 'Family-rooted · Cold-pressed · Plastic-free',
         'Wide environmental shot: multigenerational hand pouring Chekko oil at a sun-lit family table set with home-cooked food. Warm, candle-light feel. Optional faint family vignette in background.',
         'Closes on identity. The buyer doesn\'t just buy oil — they buy a small act of care for their household.'),
    ]

    for slot, role, bg, hl, sub, vis, why in images:
        # Title row
        title_text = f"Image {slot} — {role}"
        story.append(Paragraph(title_text, H3))
        # Mockup + side description
        mockup = ImageMockup(slot, role, bg, hl, sub, vis)
        side = []
        if hl:
            side.append(Paragraph(f'<b>Headline:</b> {hl}', BODY))
        if sub:
            side.append(Paragraph(f'<b>Subline:</b> {sub}', BODY))
        side.append(Paragraph(f'<b>Visual:</b> {vis}', BODY))
        side.append(Spacer(1, 0.15*cm))
        side.append(Paragraph(f'<i>Why it works:</i> {why}', QUOTE))
        side_block = Table([[s] for s in side], colWidths=[CONTENT_W - mockup.mockup_size - mockup.gap])
        side_block.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),
                                        ('LEFTPADDING',(0,0),(-1,-1),0),
                                        ('RIGHTPADDING',(0,0),(-1,-1),0),
                                        ('TOPPADDING',(0,0),(-1,-1),0),
                                        ('BOTTOMPADDING',(0,0),(-1,-1),3)]))
        row = Table([[mockup, side_block]], colWidths=[mockup.mockup_size + mockup.gap, CONTENT_W - mockup.mockup_size - mockup.gap])
        row.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),
                                 ('LEFTPADDING',(0,0),(-1,-1),0),
                                 ('RIGHTPADDING',(0,0),(-1,-1),0),
                                 ('TOPPADDING',(0,0),(-1,-1),0),
                                 ('BOTTOMPADDING',(0,0),(-1,-1),0)]))
        story.append(KeepTogether([row]))
        story.append(Spacer(1, 0.45*cm))

    # ============ SECTION 6: A+ MODULES ============
    story.append(PageBreak())
    story.append(Paragraph('5 · A+ Premium Content (7 Modules)', H2))
    story.append(HRule())
    story.append(Paragraph('Variant-agnostic — same A+ ships across every Chekko oil SKU. Variant-specific facts surface in Module 5 (family carousel) and Module 7 (comparison chart).', SUB))

    modules = [
        (1, 'Full Image', 'Pressed slow. Poured proud.',
         'Heritage cold-pressed cooking and wellness oils — sealed in plastic-free tin.',
         CREAM,
         'Cinematic golden-hour shot of a stone ghani press in a clean Indian-craft workshop, with the Chekko tin in the foreground.'),
        (2, 'Carousel (5 tiles)', 'The Chekko Difference',
         'Cold-pressed · Never refined · Traceable sourcing · Plastic-free tin · Multi-use family',
         GOLD,
         'Five tiles, identical lighting and composition: macro of seeds + drop · vial of unrefined vs refined · sesame field · tin cross-section · cooking + body + ritual icons.'),
        (3, 'Full Image', 'Seed → Stone → Tin.',
         'Three steps. Zero shortcuts. The way Indian families have made oil for centuries — now in a kitchen-ready format.',
         CREAM,
         'Three-step horizontal layout: hand-selected seeds → stone ghani press → sealed tin. Earthy palette.'),
        (4, 'Full Image', 'Cook. Anoint. Nourish.',
         'Used in Indian kitchens and Ayurvedic rituals for over a thousand years — and ready for yours.',
         ROAST,
         'Triptych within one banner: LEFT cooking on stovetop · CENTER scalp oil being poured · RIGHT oil pulling at sunrise. Warm earth tones throughout.'),
        (5, 'Carousel (5 tiles)', 'The Chekko Family',
         'Sesame · Groundnut · Coconut · Mustard / Kachi Ghani · Multi-pack',
         GOLD,
         'Same lighting and composition across all tiles. Color-coded label band per oil. Footer: "Explore the full Chekko family of cold-pressed heritage oils."'),
        (6, 'Q&A', 'Defuses top objections',
         'Foaming · Toasted vs cold-pressed · Skin & hair use · Why tin?',
         CREAM,
         'Four Q&A pairs — see the table below for the full text.'),
        (7, 'Comparison Chart', 'Make the price make sense',
         'Chekko vs refined supermarket · vs toasted · vs generic carrier sesame',
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
        side_block.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),
                                        ('LEFTPADDING',(0,0),(-1,-1),0),
                                        ('RIGHTPADDING',(0,0),(-1,-1),0),
                                        ('TOPPADDING',(0,0),(-1,-1),0),
                                        ('BOTTOMPADDING',(0,0),(-1,-1),3)]))
        row = Table([[mockup, side_block]], colWidths=[mockup.banner_w + mockup.gap, CONTENT_W - mockup.banner_w - mockup.gap])
        row.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),
                                 ('LEFTPADDING',(0,0),(-1,-1),0),
                                 ('RIGHTPADDING',(0,0),(-1,-1),0),
                                 ('TOPPADDING',(0,0),(-1,-1),0),
                                 ('BOTTOMPADDING',(0,0),(-1,-1),0)]))
        story.append(KeepTogether([row]))
        story.append(Spacer(1, 0.4*cm))

    # Q&A details
    story.append(PageBreak())
    story.append(Paragraph('A+ Module 6 — Premium Q&A (full copy)', H3))
    qa = [
        ('Why does the oil sometimes foam?',
         'Light foam is normal in fresh cold-pressed sesame oil. Refined oils suppress it with anti-foaming agents — we don\'t.'),
        ('Is this the same as toasted sesame oil?',
         'No. Chekko is light cold-pressed sesame oil for everyday cooking. Toasted sesame oil is roasted and used as a finishing oil — we recommend keeping both for full-flavor Asian cuisine.'),
        ('Can I use it on skin and hair?',
         'Yes. Sesame oil is one of the foundational oils in Ayurveda for body massage (Abhyanga), scalp oiling, and oil pulling.'),
        ('Why a tin and not a bottle?',
         'Light, oxygen and plastic leaching all degrade delicate cold-pressed oils. Our food-grade tin protects flavor, freshness, and your body.'),
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

    # Comparison chart
    story.append(Spacer(1, 0.6*cm))
    story.append(Paragraph('A+ Module 7 — Premium Comparison Chart', H3))
    comp = [
        ['Feature', 'Chekko\nCold-Pressed Sesame', 'Refined supermarket sesame', 'Toasted sesame\n(different product)', 'Generic carrier\nsesame'],
        ['Extraction', 'Cold-pressed (low-temp)', 'Refined, often hexane', 'Roasted then pressed', 'Often expeller'],
        ['Heat during extraction', 'None', 'Yes', 'Yes', 'Sometimes'],
        ['Anti-foaming additives', 'None', 'Often', 'None', 'Often'],
        ['Packaging', 'Tin (plastic-free)', 'Plastic', 'Plastic / glass', 'Plastic'],
        ['Single-origin / traceable', 'Yes', 'Rarely', 'Rarely', 'Rarely'],
        ['Use cases', 'Cook · Body · Hair · Ritual', 'Cook only', 'Finish-cook only', 'Body / hair only'],
        ['Made in', 'India, ancestral methods', 'Various', 'Various', 'Various'],
    ]
    comp_table = Table(comp, colWidths=[3.4*cm, 3.6*cm, 3.4*cm, 3.4*cm, 3.0*cm])
    comp_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), MAROON),
        ('TEXTCOLOR', (0,0), (-1,0), WHITE),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('BACKGROUND', (1,1), (1,-1), HexColor('#FFF8DC')),  # Chekko column highlight
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

    # ============ SECTION 7: MASTER COPY ============
    story.append(PageBreak())
    story.append(Paragraph('6 · Master Copy (paste-ready)', H2))
    story.append(HRule())
    story.append(Paragraph('Title (~199 chars)', H3))
    title_box = Table([[Paragraph(
        '<b>CHEKKO Cold-Pressed Sesame Oil 1 Liter (33 Fl Oz) Tin — Pure Single-Origin Sesame Seed Oil for Cooking, '
        'Stir-Fry &amp; Asian Recipes · Traditionally Pressed · Plastic-Free Tin · Multi-Use</b>', BODY)]],
        colWidths=[CONTENT_W])
    title_box.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), GOLD),
        ('LEFTPADDING', (0,0), (-1,-1), 12), ('RIGHTPADDING', (0,0), (-1,-1), 12),
        ('TOPPADDING', (0,0), (-1,-1), 8), ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(title_box)

    story.append(Spacer(1, 0.4*cm))
    story.append(Paragraph('Bullets', H3))
    bullets = [
        ('COLD-PRESSED, NEVER REFINED',
         'Chekko sesame oil is slowly extracted from hand-selected sesame seeds at low temperature, with no heat, no solvents, no bleaching, and no anti-foaming agents. The seed, simply pressed.'),
        ('RICH, NUTTY, EVERYDAY KITCHEN OIL',
         'Mild, golden, and aromatic. Designed for everyday Indian and Asian cooking — stir-fries, marinades, dressings, sautéing, finishing, and traditional family recipes.'),
        ('ONE OIL, THREE TRADITIONS',
         'Cook with it, anoint with it, nourish with it. Sesame oil has been a foundational Indian and Ayurvedic oil for body massage (Abhyanga), scalp oiling, and oil pulling for over a thousand years.'),
        ('SEALED FRESH IN PLASTIC-FREE TIN',
         'Cold-pressed oils are delicate. Our food-grade tin shields the oil from light, oxygen, and plastic — keeping aroma, flavor, and nutrients exactly the way they were pressed.'),
        ('TRACEABLE SOURCING, FAMILY-ROOTED',
         'Made by Chekko from single-origin sesame, with a transparent path from field to tin. Non-GMO, no additives, no fillers — simply the way oil was made before factories.'),
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
        '<font face="Courier" size="8">sesame seed oil cold pressed organic unrefined cooking stir fry asian indian til gingelly virgin pure tin plastic free non gmo for skin hair body massage abhyanga oil pulling ayurvedic single origin</font>', BODY)]],
        colWidths=[CONTENT_W])
    be.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), HexColor('#F5F5F5')),
        ('LEFTPADDING', (0,0), (-1,-1), 10), ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 8), ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(be)

    # Compliance
    story.append(Spacer(1, 0.4*cm))
    story.append(Paragraph('Compliance notes', H3))
    for line in [
        'No competitor brand names (Kadoya, Hemani, Dr Adorable, Handcraft Blends, Spectrum, Eden, Ottavio, La Tourangelle).',
        'No health / medical claims (avoid "cures", "boosts immunity"). Use "traditionally used for", or describe the practice (Abhyanga / oil pulling) rather than the medical outcome.',
        '"Organic" / "Non-GMO" only if certified — otherwise use "natural" / "no additives".',
        'Avoid "best", "#1", "ultimate".',
    ]:
        story.append(Paragraph('• ' + line, BODY))

    doc.build(story)
    print(f'PDF: {OUT}')

if __name__ == '__main__':
    from reportlab.platypus import NextPageTemplate
    build()
