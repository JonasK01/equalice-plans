#!/usr/bin/env python3
"""
Export a content brief (markdown) to a styled PDF with EQUALICE branding.
Usage: python3 tools/export_brief_to_pdf.py <input.md> [output.pdf] [--logo path] [--images dir] [--moodboard dir]

Options:
  --logo      Agency logo for cover page
  --images    Directory with product images (*.png, *.jpg) to embed on cover
  --moodboard Directory with reference/inspiration images for moodboard grid
"""

import sys
import re
import os
import glob as globmod

try:
    from fpdf import FPDF
except ImportError:
    print("Missing dependency. Run: pip3 install fpdf2")
    sys.exit(1)


def sanitize_text(text):
    replacements = {
        "\u2014": "--", "\u2013": "-", "\u2018": "'", "\u2019": "'",
        "\u201c": '"', "\u201d": '"', "\u2026": "...", "\u2022": "-",
        "\u2023": ">", "\u00b7": "-", "\u2192": "->", "\u2190": "<-",
        "\u2713": "[x]", "\u2717": "[ ]",
        "\u00e4": "ae", "\u00f6": "oe", "\u00fc": "ue",
        "\u00c4": "Ae", "\u00d6": "Oe", "\u00dc": "Ue", "\u00df": "ss",
    }
    for char, repl in replacements.items():
        text = text.replace(char, repl)
    try:
        text.encode("latin-1")
    except UnicodeEncodeError:
        text = text.encode("latin-1", errors="replace").decode("latin-1")
    return text


# ─── Compact layout constants ────────────────────────────────────
LH = 5            # line height
SP = 1.5          # small space
MP = 3            # medium space
LP = 4            # large space
PL = 18           # page left margin
PR = 18           # page right margin
BX = 22           # bullet x
BTX = 26          # bullet text x


class BriefPDF(FPDF):

    C = {
        "black": (35, 35, 35),
        "dark": (50, 50, 50),
        "body": (65, 65, 65),
        "gray": (140, 140, 140),
        "line": (215, 215, 215),
        "bg": (250, 250, 250),
        "white": (255, 255, 255),
        "orange": (242, 140, 0),
        "orange_soft": (255, 248, 235),
        "tbl_head": (45, 45, 45),
        "tbl_alt": (250, 248, 244),
        "green": (39, 174, 96),
    }

    def __init__(self, logo_path=None, images_dir=None, moodboard_dir=None):
        super().__init__()
        self.logo_path = logo_path
        self.images_dir = images_dir
        self.moodboard_dir = moodboard_dir
        self.set_auto_page_break(auto=True, margin=15)
        self.set_margins(PL, 12, PR)
        self.alias_nb_pages()
        # No add_page() here — build_cover or first content call handles it

    def cell(self, w=None, h=None, text="", *args, **kwargs):
        return super().cell(w, h, sanitize_text(str(text)), *args, **kwargs)

    def multi_cell(self, w, h=None, text="", *args, **kwargs):
        return super().multi_cell(w, h, sanitize_text(str(text)), *args, **kwargs)

    def header(self):
        if self.page_no() > 1:
            self.set_draw_color(*self.C["orange"])
            self.set_line_width(0.35)
            self.line(PL, 8, self.w - PR, 8)
            self.set_font("Helvetica", "", 6)
            self.set_text_color(*self.C["gray"])
            self.set_y(9)
            self.cell(0, 4, f"{self.page_no()}/{{nb}}", align="R")
            self.set_y(14)

    def footer(self):
        self.set_y(-10)
        self.set_font("Helvetica", "", 5.5)
        self.set_text_color(*self.C["gray"])
        self.cell(0, 6, "EQUALICE GmbH", align="L")
        self.set_x(PL)
        self.cell(0, 6, f"{self.page_no()}/{{nb}}", align="R")

    # ── Cover ─────────────────────────────────────────────────────

    def build_cover(self, title_text):
        self.add_page()
        if self.logo_path and os.path.isfile(self.logo_path):
            lw = 65
            self.image(self.logo_path, x=(self.w - lw) / 2, y=20, w=lw)
            self.set_y(60)
        else:
            self.set_y(30)

        self.set_font("Helvetica", "B", 18)
        self.set_text_color(*self.C["black"])
        self.multi_cell(0, 9, title_text, align="C")
        self.ln(2)
        bw = 40
        self.set_fill_color(*self.C["orange"])
        self.rect((self.w - bw) / 2, self.get_y(), bw, 1.5, "F")
        self.ln(8)

        # Product images — prioritize files named product_*
        all_imgs = self._find_images(self.images_dir, skip_logos=True)
        product_imgs = [f for f in all_imgs if os.path.basename(f).lower().startswith("product_")]
        if not product_imgs:
            product_imgs = all_imgs
        if product_imgs:
            self._grid_images(product_imgs[:2], img_h=50, gap=5, caption=None)
            self.ln(2)

        self.set_font("Helvetica", "", 7.5)
        self.set_text_color(*self.C["gray"])
        from datetime import date
        self.cell(0, 4, f"Prepared {date.today().strftime('%B %Y')}", align="C")

    # ── Moodboard page ────────────────────────────────────────────

    def build_moodboard(self):
        imgs = self._find_images(self.moodboard_dir)
        if not imgs:
            return
        self.add_page()
        y = self.get_y()
        self.set_fill_color(*self.C["orange"])
        self.rect(PL, y, 2, 7, "F")
        self.set_x(PL + 5)
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(*self.C["black"])
        self.cell(0, 7, "Visual Moodboard & References")
        self.ln(9)
        self.set_font("Helvetica", "", 7)
        self.set_text_color(*self.C["gray"])
        self.cell(0, 3, "Reference imagery for visual direction, styling, and photography tone.")
        self.ln(5)
        self._grid_images(imgs[:6], img_h=58, gap=4, caption=None, cols=2)

    def _find_images(self, directory, skip_logos=False):
        imgs = []
        if not directory or not os.path.isdir(directory):
            return imgs
        for ext in ("*.png", "*.jpg", "*.jpeg"):
            for f in sorted(globmod.glob(os.path.join(directory, ext))):
                bn = os.path.basename(f).lower()
                if skip_logos and ("logo" in bn or "equalice" in bn):
                    continue
                if bn.startswith("preview_"):
                    continue
                imgs.append(f)
        return imgs

    def _grid_images(self, images, img_h=50, gap=5, caption=None, cols=None):
        n = len(images)
        if n == 0:
            return
        if cols is None:
            cols = min(n, 3)
        usable = self.w - PL - PR
        img_w = (usable - gap * (cols - 1)) / cols

        for idx, img_path in enumerate(images):
            col = idx % cols
            if col == 0 and idx > 0:
                self.ln(gap)
            if col == 0 and self.get_y() + img_h > self.h - 20:
                self.add_page()

            x = PL + col * (img_w + gap)
            y = self.get_y()

            # Light card bg
            self.set_fill_color(*self.C["bg"])
            self.set_draw_color(*self.C["line"])
            self.set_line_width(0.2)
            self.rect(x, y, img_w, img_h, "DF")

            try:
                pad = 2
                max_w = img_w - pad * 2
                max_h = img_h - pad * 2
                # Get actual image dimensions to preserve aspect ratio
                from PIL import Image as PILImage
                with PILImage.open(img_path) as pil_img:
                    orig_w, orig_h = pil_img.size
                ratio = orig_w / orig_h
                # Fit within max_w x max_h without stretching
                if ratio > max_w / max_h:
                    # Image is wider — fit to width
                    render_w = max_w
                    render_h = max_w / ratio
                else:
                    # Image is taller — fit to height
                    render_h = max_h
                    render_w = max_h * ratio
                # Center within the card
                cx = x + pad + (max_w - render_w) / 2
                cy = y + pad + (max_h - render_h) / 2
                self.image(img_path, x=cx, y=cy, w=render_w, h=render_h)
            except ImportError:
                # Fallback without PIL: set only width, let fpdf calculate height
                try:
                    self.image(img_path, x=x + pad, y=y + pad, w=img_w - pad * 2)
                except Exception:
                    pass
            except Exception:
                pass

            # After last column, move Y down
            if col == cols - 1 or idx == n - 1:
                self.set_y(y + img_h)

        if caption:
            self.ln(2)
            self.set_font("Helvetica", "I", 7)
            self.set_text_color(*self.C["gray"])
            self.cell(0, 4, caption, align="C")
        self.ln(2)

    # ── Content elements ──────────────────────────────────────────

    def add_title(self, text):
        self.set_font("Helvetica", "B", 14)
        self.set_text_color(*self.C["black"])
        self.multi_cell(0, 7, text)
        self.set_fill_color(*self.C["orange"])
        self.rect(PL, self.get_y() + 0.5, 35, 1, "F")
        self.ln(LP)

    def add_h2(self, text):
        if self.get_y() > self.h - 18:
            self.add_page()
        self.ln(MP)
        y = self.get_y()
        self.set_fill_color(*self.C["orange"])
        self.rect(PL, y, 1.8, 6.5, "F")
        self.set_x(PL + 4)
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(*self.C["black"])
        self.cell(0, 6.5, text)
        self.ln(6.5)
        self.ln(MP)

    def add_h3(self, text):
        if self.get_y() > self.h - 14:
            self.add_page()
        self.ln(SP)
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(*self.C["dark"])
        self.cell(0, 5, text)
        self.ln(5)
        self.set_draw_color(*self.C["line"])
        self.set_line_width(0.1)
        self.line(PL, self.get_y(), PL + 38, self.get_y())
        self.ln(SP + 0.5)

    def add_h4(self, text):
        if self.get_y() > self.h - 12:
            self.add_page()
        y = self.get_y() + 1.5
        self.set_fill_color(*self.C["orange"])
        self.rect(PL, y, 1.2, 1.2, "F")
        self.set_x(PL + 3)
        self.set_font("Helvetica", "B", 8)
        self.set_text_color(*self.C["dark"])
        self.cell(0, LH, text)
        self.ln(LH)
        self.ln(SP)

    def add_body(self, text):
        self.set_font("Helvetica", "", 8)
        self.set_text_color(*self.C["body"])
        self.multi_cell(0, LH, text)
        self.ln(SP)

    def add_bold_label(self, label, value):
        lc = label.rstrip(":") + ":"
        self.set_font("Helvetica", "B", 8)
        self.set_text_color(*self.C["dark"])
        lw = self.get_string_width(lc + " ")
        self.cell(lw, LH, lc + " ")
        self.set_font("Helvetica", "", 8)
        self.set_text_color(*self.C["body"])
        if value:
            tw = self.w - self.get_x() - self.r_margin
            self.multi_cell(tw, LH, value)
        else:
            self.ln(LH)
        self.ln(SP)

    def add_bullet(self, text):
        tw = self.w - BTX - self.r_margin
        clean = re.sub(r"\*\*(.+?)\*\*:?\s*", r"\1: ", text).strip()
        self.set_x(BX)
        self.set_font("Helvetica", "B", 8)
        self.set_text_color(*self.C["orange"])
        self.cell(4, LH, "-")
        self.set_x(BTX)
        self.set_font("Helvetica", "", 8)
        self.set_text_color(*self.C["body"])
        self.multi_cell(tw, LH, clean)
        self.ln(1)

    def add_numbered(self, number, text):
        self.set_x(BX)
        self.set_font("Helvetica", "B", 8)
        self.set_text_color(*self.C["orange"])
        self.cell(5, LH, f"{number}.")
        clean = re.sub(r"\*\*(.+?)\*\*:?\s*", r"\1: ", text).strip()
        self.set_x(BTX + 1)
        tw = self.w - BTX - 1 - self.r_margin
        self.set_font("Helvetica", "", 8)
        self.set_text_color(*self.C["body"])
        self.multi_cell(tw, LH, clean)
        self.ln(1)

    def add_checkbox(self, text, checked=False):
        self.set_x(BX)
        self.set_font("Helvetica", "", 8)
        if checked:
            self.set_text_color(*self.C["green"])
            self.cell(6, LH, "[x]")
        else:
            self.set_text_color(*self.C["gray"])
            self.cell(6, LH, "[ ]")
        self.set_x(BTX + 1)
        tw = self.w - BTX - 1 - self.r_margin
        self.set_text_color(*self.C["body"])
        self.multi_cell(tw, LH, text)
        self.ln(1)

    def add_table(self, headers, rows):
        if not headers:
            return
        pw = self.w - PL - PR
        cw = self._calc_col_widths(headers, rows, pw)

        def draw_hdr():
            self.set_font("Helvetica", "B", 6.5)
            self.set_fill_color(*self.C["tbl_head"])
            self.set_text_color(*self.C["white"])
            for j, h in enumerate(headers):
                self.cell(cw[j], 5.5, h.strip(), border=0, fill=True, align="C")
            self.ln()

        draw_hdr()
        for i, row in enumerate(rows):
            fill = i % 2 == 0
            self.set_fill_color(*(self.C["tbl_alt"] if fill else self.C["white"]))
            self.set_font("Helvetica", "", 6.5)
            self.set_text_color(*self.C["body"])

            max_lines = 1
            for j, ct in enumerate(row):
                w = cw[j] if j < len(cw) else cw[-1]
                sw = self.get_string_width(ct.strip())
                lines = max(1, int(sw / (w - 2)) + 1)
                max_lines = max(max_lines, lines)
            row_h = max(4.5, min(max_lines * 3.2, 28))

            if self.get_y() + row_h > self.h - 14:
                self.add_page()
                draw_hdr()
            y0 = self.get_y()

            x = PL
            for j, ct in enumerate(row):
                w = cw[j] if j < len(cw) else cw[-1]
                self.set_xy(x, y0)
                self.cell(w, row_h, "", border=0, fill=True)
                x += w
            self.set_draw_color(*self.C["line"])
            self.set_line_width(0.06)
            self.line(PL, y0 + row_h, PL + pw, y0 + row_h)

            x = PL
            self.set_text_color(*self.C["body"])
            for j, ct in enumerate(row):
                w = cw[j] if j < len(cw) else cw[-1]
                self.set_xy(x + 1, y0 + 0.5)
                self.set_font("Helvetica", "", 6.5)
                super(BriefPDF, self).multi_cell(w - 2, 3.2, sanitize_text(ct.strip()))
                x += w
            self.set_y(y0 + row_h)
        self.ln(MP)

    def add_code_block(self, text):
        self.set_font("Courier", "", 6.5)
        self.set_text_color(*self.C["body"])
        for line in text.split("\n"):
            if self.get_y() > self.h - 12:
                self.add_page()
            y = self.get_y()
            self.set_fill_color(*self.C["orange"])
            self.rect(PL + 1, y, 0.6, 3.8, "F")
            self.set_fill_color(*self.C["bg"])
            self.set_x(PL + 2.5)
            self.cell(self.w - PL - PR - 2.5, 3.8, " " + line, fill=True)
            self.ln()
        self.ln(SP)

    def add_separator(self):
        pass  # Stripped entirely — h2/h3 provide visual breaks

    def _calc_col_widths(self, headers, rows, total_width):
        n = len(headers)
        if n == 0:
            return []
        maxl = [len(h) for h in headers]
        for row in rows:
            for j, c in enumerate(row):
                if j < len(maxl):
                    maxl[j] = max(maxl[j], min(len(c.strip()), 50))
        s = sum(maxl) or 1
        minw = max(12, total_width / (n * 2))
        ws = [max(minw, (l / s) * total_width) for l in maxl]
        sc = total_width / sum(ws)
        return [w * sc for w in ws]


# ─── Markdown parser ─────────────────────────────────────────────

def parse_markdown(md_text):
    elements = []
    lines = md_text.split("\n")
    i = 0
    in_code = False
    code_lines = []
    in_table = False
    table_headers = []
    table_rows = []

    while i < len(lines):
        line = lines[i]
        if line.strip().startswith("```"):
            if in_code:
                elements.append(("code", "\n".join(code_lines)))
                code_lines = []
                in_code = False
            else:
                if in_table:
                    elements.append(("table", table_headers, table_rows))
                    in_table, table_headers, table_rows = False, [], []
                in_code = True
            i += 1
            continue
        if in_code:
            code_lines.append(line)
            i += 1
            continue

        if "|" in line and line.strip().startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if all(re.match(r"^[-:]+$", c.strip()) for c in cells if c.strip()):
                i += 1
                continue
            if not in_table:
                in_table = True
                table_headers = cells
            else:
                table_rows.append(cells)
            i += 1
            continue
        else:
            if in_table:
                elements.append(("table", table_headers, table_rows))
                in_table, table_headers, table_rows = False, [], []

        s = line.strip()
        if not s:
            i += 1
            continue
        if s.startswith("#### "):
            elements.append(("h4", s[5:].strip()))
        elif s.startswith("### "):
            elements.append(("h3", s[4:].strip()))
        elif s.startswith("## "):
            elements.append(("h2", s[3:].strip()))
        elif s.startswith("# "):
            elements.append(("h1", s[2:].strip()))
        elif s.startswith("---"):
            elements.append(("separator",))
        elif s.startswith("- [x]"):
            elements.append(("checkbox", s[6:].strip(), True))
        elif s.startswith("- [ ]"):
            elements.append(("checkbox", s[6:].strip(), False))
        elif re.match(r"^\d+\.\s", s):
            m = re.match(r"^(\d+)\.\s(.+)", s)
            elements.append(("numbered", int(m.group(1)), m.group(2)))
        elif s.startswith("- ") or s.startswith("* "):
            elements.append(("bullet", s[2:]))
        elif s.startswith("**") and ":" in s:
            m = re.match(r"\*\*(.+?)\*\*:?\s*(.*)", s)
            if m:
                elements.append(("bold_label", m.group(1).rstrip(":"), m.group(2).strip()))
            else:
                elements.append(("body", s))
        else:
            elements.append(("body", s))
        i += 1

    if in_table:
        elements.append(("table", table_headers, table_rows))
    return elements


# ─── Main ────────────────────────────────────────────────────────

def generate_pdf(md_text, output_path, logo_path=None, images_dir=None, moodboard_dir=None):
    md_text = sanitize_text(md_text)
    elements = parse_markdown(md_text)

    title = "Content Brief"
    content_start = 0
    for idx, el in enumerate(elements):
        if el[0] == "h1":
            title = el[1]
            content_start = idx + 1
            break

    pdf = BriefPDF(logo_path=logo_path, images_dir=images_dir, moodboard_dir=moodboard_dir)
    pdf.build_cover(title)

    # Insert moodboard before content if images exist
    pdf.build_moodboard()

    pdf.add_page()

    for el in elements[content_start:]:
        t = el[0]
        if t == "h1":
            pdf.add_title(el[1])
        elif t == "h2":
            pdf.add_h2(el[1])
        elif t == "h3":
            pdf.add_h3(el[1])
        elif t == "h4":
            pdf.add_h4(el[1])
        elif t == "body":
            pdf.add_body(el[1])
        elif t == "bold_label":
            pdf.add_bold_label(el[1], el[2])
        elif t == "bullet":
            pdf.add_bullet(el[1])
        elif t == "numbered":
            pdf.add_numbered(el[1], el[2])
        elif t == "checkbox":
            pdf.add_checkbox(el[1], el[2])
        elif t == "table":
            pdf.add_table(el[1], el[2])
        elif t == "code":
            pdf.add_code_block(el[1])
        elif t == "separator":
            pdf.add_separator()

    pdf.output(output_path)
    print(f"PDF exported: {output_path}")
    print(f"Pages: {pdf.page_no()}")
    print(f"Size: {os.path.getsize(output_path) / 1024:.1f} KB")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 tools/export_brief_to_pdf.py <input.md> [output.pdf] [--logo path] [--images dir] [--moodboard dir]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = None
    logo_path = None
    images_dir = None
    moodboard_dir = None

    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == "--logo" and i + 1 < len(sys.argv):
            logo_path = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == "--images" and i + 1 < len(sys.argv):
            images_dir = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == "--moodboard" and i + 1 < len(sys.argv):
            moodboard_dir = sys.argv[i + 1]
            i += 2
        elif output_file is None:
            output_file = sys.argv[i]
            i += 1
        else:
            i += 1

    if output_file is None:
        output_file = os.path.splitext(input_file)[0] + ".pdf"

    with open(input_file, "r", encoding="utf-8") as f:
        md_content = f.read()

    generate_pdf(md_content, output_file, logo_path, images_dir, moodboard_dir)
