#!/usr/bin/env python3
"""Build a lecture deck (.pptx) for AI for All from a YAML spec.

    python3 tools/build_slides.py slides/specs/ch01.yaml            # build one deck
    python3 tools/build_slides.py slides/specs/ch01.yaml --preview  # + PNG check images
    python3 tools/build_slides.py --template                         # slides/template/*.pptx

The design (16:9, Source Sans 3 / Source Serif 4, the book's palette from
figures/scripts/figlib.py) lives entirely in this file; the spec format and the
speaker-notes standard are documented in slides/README.md.

Run with DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib on macOS (cairosvg needs it
to convert the book's SVG figures).  The build is idempotent: the same spec gives
the same deck, and figure PNGs are reconverted only when their SVG changes.
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

import yaml
from lxml import etree
from PIL import Image, ImageChops, ImageFont
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, MSO_AUTO_SIZE, PP_ALIGN
from pptx.opc.constants import RELATIONSHIP_TYPE as RT
from pptx.oxml.ns import qn
from pptx.util import Emu, Inches, Pt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "figures" / "scripts"))
from figlib import ROLES  # noqa: E402  (palette is shared with the book's figures)

# --------------------------------------------------------------------------- palette
C = ROLES["color"]
NAVY, NAVY_DARK, _ = C["human"]
AI_FILL, AI_STROKE, _ = C["ai"]
RISK, RISK_DARK, _ = C["risk"]
OK, OK_DARK, OK_TEXT = C["verified"]
SOFT, SOFT_STROKE, _ = C["soft"]
INK = "#1D1D1F"
MUTED = "#5C5C66"
WHITE = "#FFFFFF"
PALE = "#D9E1EC"  # light text on navy (contrast 9.6:1)

# role -> (header fill, header text, card border)
ROLE_STYLE = {
    "human": (NAVY, WHITE, NAVY_DARK),
    "ai": (AI_FILL, INK, AI_STROKE),
    "risk": (RISK, WHITE, RISK_DARK),
    "verified": (OK, OK_TEXT, OK_DARK),
    "neutral": (WHITE, INK, "#3A3A3A"),
    "soft": (SOFT, INK, SOFT_STROKE),
}

# --------------------------------------------------------------------------- fonts
FONT_DIRS = [Path.home() / "Library/Fonts", Path("/Library/Fonts"), Path("/System/Library/Fonts/Supplemental")]
SANS = "Source Sans 3"
SERIF = "Source Serif 4"
FONT_FILES = {  # family -> (regular file, italic file); variable fonts, weight set per use
    "Source Sans 3": ("SourceSans3[wght].ttf", "SourceSans3-Italic[wght].ttf"),
    "Source Serif 4": ("SourceSerif4[opsz,wght].ttf", "SourceSerif4-Italic[opsz,wght].ttf"),
    "Arial": ("Arial.ttf", "Arial Italic.ttf"),
    "Georgia": ("Georgia.ttf", "Georgia Italic.ttf"),
}
_font_cache: dict = {}


def _find_font(name: str) -> Path | None:
    for d in FONT_DIRS:
        p = d / name
        if p.exists():
            return p
    return None


def pil_font(family: str, bold=False, italic=False, size=100):
    key = (family, bold, italic, size)
    if key in _font_cache:
        return _font_cache[key]
    files = FONT_FILES.get(family, FONT_FILES["Arial"])
    path = _find_font(files[1] if italic else files[0]) or _find_font(files[0]) or _find_font("Arial.ttf")
    f = ImageFont.truetype(str(path), size)
    try:
        axes = f.get_variation_axes()
        vals = []
        for ax in axes:
            n = ax["name"].decode() if isinstance(ax["name"], bytes) else ax["name"]
            if n.lower().startswith("weight"):
                vals.append(700 if bold else 400)
            elif n.lower().startswith("optical"):
                vals.append(max(ax["minimum"], min(ax["maximum"], 20)))
            else:
                vals.append(ax["default"])
        f.set_variation_by_axes(vals)
    except OSError:
        pass  # static font
    _font_cache[key] = f
    return f


def text_width(s: str, family: str, size: float, bold=False, italic=False) -> float:
    """Width in points."""
    return pil_font(family, bold, italic).getlength(s) * size / 100.0


# --------------------------------------------------------------------------- geometry
SW, SH = 13.333, 7.5          # slide, inches
MX = 0.6                      # side margin
CW = SW - 2 * MX              # content width
TOP = 1.62                    # content top (below title)
BOTTOM = 6.85                 # content bottom (above footer)
LS = 1.18                     # line spacing (multiple of size, exact points)

BODY = 26                     # default body size
BODY_MIN = 24                 # floor for body text students must read
CARD_MIN = 20                 # floor inside cards, tables, step lists
SMALL = 18                    # captions, meta lines
REF_SIZE = 16                 # references only


def E(inches: float) -> Emu:
    return Emu(int(round(inches * 914400)))


def rgb(h: str) -> RGBColor:
    return RGBColor.from_string(h.lstrip("#").upper())


def luminance(h: str) -> float:
    h = h.lstrip("#")
    out = []
    for i in (0, 2, 4):
        c = int(h[i:i + 2], 16) / 255
        out.append(c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * out[0] + 0.7152 * out[1] + 0.0722 * out[2]


def contrast(a: str, b: str) -> float:
    la, lb = sorted([luminance(a), luminance(b)], reverse=True)
    return (la + 0.05) / (lb + 0.05)


# --------------------------------------------------------------------------- build state
@dataclass
class Ctx:
    spec: dict
    prs: Presentation
    warnings: list = field(default_factory=list)
    slide_no: int = 0
    visible: list = field(default_factory=list)   # (slide_no, text) for checks
    notes_all: list = field(default_factory=list)  # (slide_no, notes text)
    minutes: list = field(default_factory=list)    # (session, minutes, slide_no)
    font_sans: str = SANS
    font_serif: str = SERIF

    def warn(self, msg: str):
        self.warnings.append(f"slide {self.slide_no}: {msg}")


# --------------------------------------------------------------------------- inline markup
def parse_runs(s: str, bold=False, italic=False, color=None):
    """'**bold**' and '*italic*' markup -> list of (text, bold, italic, color)."""
    out = []
    pos = 0
    for m in re.finditer(r"\*\*(.+?)\*\*|\*(.+?)\*", s):
        if m.start() > pos:
            out.append((s[pos:m.start()], bold, italic, color))
        if m.group(1) is not None:
            out.append((m.group(1), True, italic, color))
        else:
            out.append((m.group(2), bold, True, color))
        pos = m.end()
    if pos < len(s):
        out.append((s[pos:], bold, italic, color))
    return out


def plain(s: str) -> str:
    return re.sub(r"\*\*(.+?)\*\*|\*(.+?)\*", lambda m: m.group(1) or m.group(2), s)


@dataclass
class Para:
    runs: list                     # (text, bold, italic, color)
    size: float = BODY
    align: str = "l"
    bullet: str | None = None      # '•', '–' or None
    level: int = 0
    space_after: float = 0.35      # in lines of this size
    font: str | None = None


def P(s, size=BODY, bold=False, italic=False, color=None, align="l", bullet=None, level=0,
      space_after=0.35, font=None) -> Para:
    return Para(parse_runs(str(s), bold, italic, color), size, align, bullet, level, space_after, font)


def wrap_para(p: Para, width_pt: float, family: str, scale: float):
    """Greedy wrap; returns number of lines."""
    size = p.size * scale
    indent = bullet_indent(p, size)
    avail = width_pt - indent
    tokens = []
    for text, b, i, _ in p.runs:
        for w in re.split(r"(\s+)", text):
            if w:
                tokens.append((w, b, i))
    lines, cur = 1, 0.0
    for w, b, i in tokens:
        if w.isspace():
            if cur > 0:
                cur += text_width(" ", family, size, b, i)
            continue
        ww = text_width(w, family, size, b, i)
        if cur > 0 and cur + ww > avail:
            lines += 1
            cur = ww
        else:
            cur += ww
        while cur > avail:          # very long word
            lines += 1
            cur -= avail
    return lines


def bullet_indent(p: Para, size: float) -> float:
    if not p.bullet:
        return 0.0
    return size * (0.95 + 1.1 * p.level)


def paras_height(paras, width_pt, family, scale):
    h = 0.0
    for k, p in enumerate(paras):
        size = p.size * scale
        n = wrap_para(p, width_pt, p.font or family, scale)
        h += n * size * LS
        if k < len(paras) - 1:
            h += p.space_after * size
    return h


# --------------------------------------------------------------------------- shapes
SHAPES = {
    "rect": MSO_SHAPE.RECTANGLE,
    "round": MSO_SHAPE.ROUNDED_RECTANGLE,
    "oval": MSO_SHAPE.OVAL,
    "hex": MSO_SHAPE.HEXAGON,
    "chevron": MSO_SHAPE.CHEVRON,
    "pentagon": MSO_SHAPE.PENTAGON,
}


def shape(ctx, slide, x, y, w, h, fill=None, line=None, lw=1.25, kind="rect", dash=False,
          radius=0.12, name=None):
    sp = slide.shapes.add_shape(SHAPES[kind], E(x), E(y), E(w), E(h))
    st = sp._element.find(qn("p:style"))
    if st is not None:
        sp._element.remove(st)
    if fill:
        sp.fill.solid()
        sp.fill.fore_color.rgb = rgb(fill)
    else:
        sp.fill.background()
    if line:
        sp.line.color.rgb = rgb(line)
        sp.line.width = Pt(lw)
        if dash:
            ln = sp.line._get_or_add_ln()
            pd = etree.SubElement(ln, qn("a:prstDash"))
            pd.set("val", "dash")
    else:
        sp.line.fill.background()
    if kind == "round":
        sp.adjustments[0] = min(0.5, radius / max(0.01, min(w, h)))
    if kind == "hex":
        sp.adjustments[0] = 0.18
    if name:
        sp.name = name
    sp.text_frame.text = ""
    return sp


def arrow(ctx, slide, x1, y1, x2, y2, color=INK, lw=1.75):
    c = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, E(x1), E(y1), E(x2), E(y2))
    c.line.color.rgb = rgb(color)
    c.line.width = Pt(lw)
    ln = c.line._get_or_add_ln()
    te = etree.SubElement(ln, qn("a:tailEnd"))
    te.set("type", "triangle")
    te.set("w", "med")
    te.set("len", "med")
    return c


def text(ctx, slide, x, y, w, h, paras, *, sp=None, min_scale=None, anchor="t", bg=WHITE,
         font=None, inset=0.05, name=None, record=True, floor=None):
    """Place paragraphs in a new textbox (or in shape sp); shrink to fit down to the floor.

    floor: smallest allowed font size (pt) for the smallest paragraph; default keeps sizes.
    """
    family = font or ctx.font_sans
    if isinstance(paras, (str, Para)):
        paras = [paras]
    paras = [p if isinstance(p, Para) else P(p) for p in paras]
    width_pt = (w - 2 * inset) * 72
    height_pt = (h - 2 * inset) * 72
    smallest = min(p.size for p in paras)
    lo = (floor / smallest) if floor else (min_scale if min_scale else 1.0)
    lo = min(lo, 1.0)
    scale = 1.0
    while True:
        need = paras_height(paras, width_pt, family, scale)
        if need <= height_pt + 0.5 or scale <= lo + 1e-6:
            break
        scale = max(lo, scale - 0.02)
    if need > height_pt + 0.5:
        first = plain("".join(r[0] for r in paras[0].runs))[:50]
        ctx.warn(f"OVERFLOW ({need:.0f} pt needed, {height_pt:.0f} pt available): '{first}…'")
    if sp is None:
        sp = slide.shapes.add_textbox(E(x), E(y), E(w), E(h))
    if name:
        sp.name = name
    tf = sp.text_frame
    tf.word_wrap = True
    tf.auto_size = MSO_AUTO_SIZE.NONE
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = E(inset)
    tf.vertical_anchor = {"t": MSO_ANCHOR.TOP, "m": MSO_ANCHOR.MIDDLE, "b": MSO_ANCHOR.BOTTOM}[anchor]
    for k, p in enumerate(paras):
        para = tf.paragraphs[0] if k == 0 else tf.add_paragraph()
        size = round(p.size * scale * 2) / 2
        para.alignment = {"l": PP_ALIGN.LEFT, "c": PP_ALIGN.CENTER, "r": PP_ALIGN.RIGHT}[p.align]
        para.line_spacing = Pt(size * LS)
        para.space_after = Pt(p.space_after * size if k < len(paras) - 1 else 0)
        para.space_before = Pt(0)
        if p.bullet:
            ind = bullet_indent(p, size)
            pPr = para._p.get_or_add_pPr()
            pPr.set("marL", str(int(Pt(ind))))
            pPr.set("indent", str(-int(Pt(size * 0.95))))
            bc = etree.SubElement(pPr, qn("a:buClr"))
            etree.SubElement(bc, qn("a:srgbClr")).set("val", NAVY.lstrip("#"))
            etree.SubElement(pPr, qn("a:buSzPct")).set("val", "100000")
            etree.SubElement(pPr, qn("a:buFont")).set("typeface", "Arial")
            etree.SubElement(pPr, qn("a:buChar")).set("char", p.bullet)
        for t, b, i, col in p.runs:
            r = para.add_run()
            r.text = t
            f = r.font
            f.name = p.font or family
            f.size = Pt(size)
            f.bold = bool(b)
            f.italic = bool(i)
            col = col or INK
            f.color.rgb = rgb(col)
            if bg and contrast(col, bg) < 4.5:
                ctx.warn(f"LOW CONTRAST {contrast(col, bg):.1f}:1 ({col} on {bg}) '{t[:30]}'")
        if record:
            ctx.visible.append((ctx.slide_no, plain("".join(r[0] for r in p.runs))))
        if size < 13.5 and record:
            ctx.warn(f"TINY TEXT {size} pt")
    return sp


def set_title(ctx, slide, title, x=MX, y=0.5, w=CW, h=0.95, size=36, color=NAVY, bg=WHITE,
              anchor="t", min_size=28):
    ph = slide.shapes.title
    ph.left, ph.top, ph.width, ph.height = E(x), E(y), E(w), E(h)
    text(ctx, slide, x, y, w, h, [P(title, size=size, bold=True, color=color)], sp=ph,
         font=ctx.font_serif, anchor=anchor, bg=bg, floor=min_size)
    return ph


def kicker(ctx, slide, s, x=MX, y=0.22, w=CW, color=NAVY, bg=WHITE):
    if s:
        text(ctx, slide, x, y, w, 0.36, [P(s.upper(), size=15, bold=True, color=color)], bg=bg,
             record=False)


def picture(ctx, slide, fig_id, x, y, w, h, alt=None, align="c", border=False):
    path, alt0 = figure_png(ctx, fig_id)
    alt = alt or alt0
    if not alt:
        ctx.warn(f"NO ALT TEXT for {fig_id}")
    elif len(alt) > 150:
        ctx.warn(f"alt text for {fig_id} is {len(alt)} characters (book limit 150)")
    with Image.open(path) as im:
        iw, ih = im.size
    r = min(w / iw, h / ih)
    pw, ph = iw * r, ih * r
    px = x + (w - pw) / 2 if align == "c" else x
    py = y + (h - ph) / 2
    pic = slide.shapes.add_picture(str(path), E(px), E(py), E(pw), E(ph))
    pic._element.nvPicPr.cNvPr.set("descr", alt or "")
    pic.name = f"Figure {fig_id}"
    if border:
        pic.line.color.rgb = rgb(SOFT_STROKE)
        pic.line.width = Pt(0.75)
    if pw < 4.0 and ph < 2.5:
        ctx.warn(f"figure {fig_id} placed small ({pw:.1f} x {ph:.1f} in)")
    return pic


def takeaway(ctx, slide, s, y=6.02, h=0.78, x=MX, w=CW):
    shape(ctx, slide, x, y, w, h, fill=SOFT)
    shape(ctx, slide, x, y, 0.12, h, fill=NAVY)
    text(ctx, slide, x + 0.3, y, w - 0.4, h, [P(s, size=24, bold=True)], anchor="m", bg=SOFT,
         floor=20)


def footer(ctx, slide, dark=False):
    d = ctx.spec["deck"]
    col = PALE if dark else MUTED
    bg = NAVY if dark else WHITE
    label = f"AI for All · Ch {d['chapter']} · {d.get('short_title', d['title'])}"
    text(ctx, slide, MX, 7.02, 9.5, 0.36, [P(label, size=12, color=col)], bg=bg, record=False)
    text(ctx, slide, SW - MX - 1.5, 7.02, 1.5, 0.36, [P(str(ctx.slide_no), size=12, color=col, align="r")],
         bg=bg, record=False)


def bullets_paras(items, size=BODY, color=INK):
    out = []
    for it in items or []:
        if isinstance(it, list):
            for sub in it:
                out.append(P(sub, size=size - 2, bullet="–", level=1, color=color))
        else:
            out.append(P(it, size=size, bullet="•", color=color))
    return out


# --------------------------------------------------------------------------- figures
def figure_png(ctx, fig_id: str):
    src_dir = ROOT / "figures" / "out" / "color"
    exact = src_dir / f"{fig_id}.svg"
    if exact.exists():
        svg = exact
    else:
        cands = sorted(src_dir.glob(f"{fig_id}*.svg"))
        if len(cands) != 1:
            raise SystemExit(f"figure id '{fig_id}': {len(cands)} matches in figures/out/color "
                             f"({', '.join(c.stem for c in cands)}); use the full file id")
        svg = cands[0]
    out_dir = ROOT / "slides" / "assets"
    out_dir.mkdir(parents=True, exist_ok=True)
    png = out_dir / f"{svg.stem}.png"
    if not png.exists() or png.stat().st_mtime < svg.stat().st_mtime:
        import cairosvg  # imported lazily: needs DYLD_FALLBACK_LIBRARY_PATH on macOS
        tmp = png.with_suffix(".tmp.png")
        cairosvg.svg2png(url=str(svg), write_to=str(tmp), output_width=2400, background_color="white")
        im = Image.open(tmp).convert("RGB")
        bg = Image.new("RGB", im.size, (255, 255, 255))
        diff = ImageChops.difference(im, bg).convert("L").point(lambda v: 255 if v > 12 else 0)
        box = diff.getbbox()
        if box:
            pad = 24
            box = (max(0, box[0] - pad), max(0, box[1] - pad), min(im.width, box[2] + pad),
                   min(im.height, box[3] + pad))
            im = im.crop(box)
        im.save(png, optimize=True)
        tmp.unlink()
    return png, alt_text(svg.stem)


_alt_cache: dict = {}


def alt_text(file_id: str) -> str | None:
    """Alt text from figures/longdesc/chNN.md (column 'Alt text'), else the chapter's fig-alt."""
    m = re.match(r"f(\d+)-", file_id)
    if not m:
        return None
    ch = int(m.group(1))
    if ch not in _alt_cache:
        table = {}
        ld = ROOT / "figures" / "longdesc" / f"ch{ch:02d}.md"
        if ld.exists():
            cols = None
            for line in ld.read_text(encoding="utf-8").splitlines():
                if not line.startswith("|"):
                    cols = None if not line.strip() else cols
                    continue
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                low = [c.lower() for c in cells]
                if any("file id" in c for c in low) and any(c.startswith("alt text") for c in low):
                    cols = (next(i for i, c in enumerate(low) if "file id" in c),
                            next(i for i, c in enumerate(low) if c.startswith("alt text")))
                    continue
                if cols and not set(line.replace("|", "").strip()) <= set("-: "):
                    ids, alt = cells[cols[0]], cells[cols[1]] if len(cells) > cols[1] else ""
                    for one in re.split(r"[,;/]\s*", ids):
                        one = one.strip().strip("`")
                        mm = re.match(r"^(.*)\((.*)\)(.*)$", one)
                        variants = [mm.group(1) + mm.group(3), mm.group(1) + mm.group(2) + mm.group(3)] if mm else [one]
                        for v in variants:
                            table.setdefault(v, alt)
        for qmd in (ROOT / "chapters").glob(f"{ch:02d}-*.qmd"):
            for mm in re.finditer(r"figures/out/color/([\w-]+)\.svg\)\{[^}]*fig-alt=\"([^\"]+)\"",
                                  qmd.read_text(encoding="utf-8")):
                table.setdefault(mm.group(1), mm.group(2))
        _alt_cache[ch] = table
    return _alt_cache[ch].get(file_id)


# --------------------------------------------------------------------------- notes
NOTE_ORDER = ["say", "background", "questions", "misconceptions", "activity", "book"]


def build_notes(ctx, s: dict) -> str:
    n = s.get("notes") or {}
    if isinstance(n, str):
        n = {"say": n}
    parts = []
    say = (n.get("say") or "").strip()
    wc = len(say.split())
    if not s.get("_reveal_cont"):
        if wc < 80 or wc > 200:
            ctx.warn(f"NOTES 'say' has {wc} words (standard: 80–200)")
    parts.append("SAY\n" + say)
    bg = (n.get("background") or "").strip()
    qs = n.get("questions") or []
    ms = n.get("misconceptions") or []
    if bg or qs or ms:
        block = ["INSTRUCTOR BACKGROUND"]
        if bg:
            block.append(bg)
        if qs:
            block.append("Likely student questions:")
            for q in qs:
                block.append(f"  Q: {q['q'].strip()}\n  A: {q['a'].strip()}")
        if ms:
            block.append("Misconceptions to watch for:")
            for m in ms:
                block.append(f"  {m['m'].strip()}\n  How to address it: {m['fix'].strip()}")
        parts.append("\n".join(block))
    elif not s.get("_reveal_cont") and s["layout"] not in ("title",):
        ctx.warn("NOTES missing 'background'")
    mins = s.get("minutes")
    act = (n.get("activity") or "").strip()
    sess = s.get("_session_label", "")
    tline = "TIMING AND ACTIVITY\n"
    tline += f"{mins:g} min" if isinstance(mins, (int, float)) else "no class time (reference)"
    if sess:
        tline += f" · {sess}"
    if act:
        tline += "\n" + act
    parts.append(tline)
    book = (n.get("book") or "").strip()
    if not book:
        ctx.warn("NOTES missing 'book' pointer")
    parts.append("BOOK\n" + book)
    return "\n\n".join(parts)


# --------------------------------------------------------------------------- layouts
def L_title(ctx, slide, s):
    d = ctx.spec["deck"]
    shape(ctx, slide, 0, 0, SW, SH, fill=NAVY)
    shape(ctx, slide, 0, SH - 0.22, SW, 0.22, fill=AI_FILL)
    has_fig = bool(s.get("figure"))
    tw = 7.3 if has_fig else 11.5
    text(ctx, slide, 0.75, 0.75, tw, 0.45, [P("AI for All: Career-Ready AI Skills".upper(), size=18, bold=True,
                                              color=AI_FILL)], bg=NAVY)
    text(ctx, slide, 0.75, 1.3, tw, 0.6, [P(f"Chapter {d['chapter']}", size=28, color=PALE)], bg=NAVY)
    set_title(ctx, slide, s.get("title", d["title"]), x=0.75, y=1.95, w=tw, h=2.0, size=50, color=WHITE,
              bg=NAVY, min_size=36)
    paras = []
    if s.get("subtitle"):
        paras.append(P(s["subtitle"], size=24, color=WHITE, space_after=0.6))
    for m in s.get("meta", []):
        paras.append(P(m, size=20, color=PALE, space_after=0.2))
    text(ctx, slide, 0.75, 4.15, tw, 2.6, paras, bg=NAVY, floor=18)
    if has_fig:
        shape(ctx, slide, 8.35, 0.75, 4.3, 5.85, fill=WHITE, kind="round", radius=0.2)
        picture(ctx, slide, s["figure"], 8.5, 0.9, 4.0, 5.55, alt=s.get("alt"))


def L_session_plan(ctx, slide, s):
    set_title(ctx, slide, s["title"])
    cols = s["columns"]
    n = len(cols)
    gap = 0.3
    cw = (CW - gap * (n - 1)) / n
    for i, col in enumerate(cols):
        x = MX + i * (cw + gap)
        y0, y1 = TOP, BOTTOM
        shape(ctx, slide, x, y0, cw, y1 - y0, fill=WHITE, line=SOFT_STROKE, kind="round", radius=0.15)
        shape(ctx, slide, x, y0, cw, 1.0, fill=NAVY, kind="rect")
        text(ctx, slide, x + 0.2, y0 + 0.05, cw - 0.4, 0.9,
             [P(col["heading"], size=24, bold=True, color=WHITE, space_after=0.1),
              P(col.get("sub", ""), size=18, color=PALE)], bg=NAVY, anchor="m", floor=16)
        blocks = col["blocks"]
        total = sum(float(b.get("min", 0)) for b in blocks) or 1
        # proportional strip (decorative; minutes are also written as text)
        bx = x + 0.2
        bw = cw - 0.4
        cur = bx
        for k, b in enumerate(blocks):
            ww = bw * float(b.get("min", 0)) / total
            shape(ctx, slide, cur, y0 + 1.15, max(0.02, ww - 0.03), 0.16,
                  fill=[NAVY, AI_FILL, OK, SOFT_STROKE, RISK, PALE][k % 6])
            cur += ww
        top = y0 + 1.45
        rh = (y1 - 0.15 - top) / len(blocks)
        for k, b in enumerate(blocks):
            yy = top + k * rh
            shape(ctx, slide, x + 0.2, yy + 0.08, 1.15, min(0.5, rh - 0.12), fill=SOFT, line=NAVY, lw=1,
                  kind="round", radius=0.12)
            text(ctx, slide, x + 0.2, yy + 0.08, 1.15, min(0.5, rh - 0.12),
                 [P(f"{b.get('min', '')} min", size=17, bold=True, color=NAVY, align="c")], anchor="m",
                 bg=SOFT, inset=0.02, floor=14)
            paras = [P(b["label"], size=21, bold=True, space_after=0.05)]
            if b.get("detail"):
                paras.append(P(b["detail"], size=17, color=MUTED))
            text(ctx, slide, x + 1.5, yy, cw - 1.7, rh, paras, anchor="t", floor=15)


def L_objectives(ctx, slide, s):
    kicker(ctx, slide, s.get("kicker"))
    set_title(ctx, slide, s["title"])
    items = s["items"]
    y = TOP
    if s.get("intro"):
        text(ctx, slide, MX, y, CW, 0.5, [P(s["intro"], size=22, color=MUTED)], floor=20)
        y += 0.6
    ncol = 2 if len(items) > 3 else 1
    nrow = -(-len(items) // ncol)
    gap = 0.25
    cw = (CW - gap * (ncol - 1)) / ncol
    rh = (BOTTOM - y - gap * (nrow - 1)) / nrow
    for k, it in enumerate(items):
        r, c = (k % nrow, k // nrow)
        x = MX + c * (cw + gap)
        yy = y + r * (rh + gap)
        shape(ctx, slide, x, yy, cw, rh, fill=WHITE, line=SOFT_STROKE, kind="round", radius=0.12)
        d = min(0.8, rh - 0.3)
        shape(ctx, slide, x + 0.2, yy + (rh - d) / 2, d, d, fill=NAVY, kind="oval")
        text(ctx, slide, x + 0.2, yy + (rh - d) / 2, d, d, [P(it["code"], size=20, bold=True, color=WHITE, align="c")],
             anchor="m", bg=NAVY, inset=0.0)
        text(ctx, slide, x + 0.4 + d, yy + 0.05, cw - d - 0.6, rh - 0.1, [P(it["text"], size=24)], anchor="m",
             floor=CARD_MIN)


def L_section(ctx, slide, s):
    shape(ctx, slide, 0, 0, SW, SH, fill=SOFT)
    shape(ctx, slide, 0, 0, 4.4, SH, fill=NAVY)
    text(ctx, slide, 0.3, 1.9, 3.8, 1.9, [P(str(s.get("number", "")), size=88, bold=True, color=AI_FILL, align="c",
                                          font=ctx.font_serif)], anchor="m", bg=NAVY, floor=48)
    if s.get("tag"):
        shape(ctx, slide, 1.35, 4.0, 1.7, 0.55, line=WHITE, lw=1.5, kind="round", radius=0.27)
        text(ctx, slide, 1.35, 4.0, 1.7, 0.55, [P(s["tag"], size=20, bold=True, color=WHITE, align="c")],
             anchor="m", bg=NAVY, inset=0.0)
    set_title(ctx, slide, s["title"], x=5.0, y=1.7, w=7.7, h=1.9, size=44, bg=SOFT, anchor="b", min_size=34)
    paras = []
    if s.get("idea"):
        paras.append(P(s["idea"], size=28, space_after=0.8))
    if s.get("meta"):
        paras.append(P(s["meta"], size=20, color=MUTED))
    text(ctx, slide, 5.0, 3.8, 7.7, 2.6, paras, bg=SOFT, floor=24)


def L_concept(ctx, slide, s, badge=None):
    kicker(ctx, slide, s.get("kicker"))
    set_title(ctx, slide, s["title"])
    if badge or s.get("badge"):
        b = badge or s["badge"]
        bw = min(6.0, 0.6 + len(b) * 0.115)
        shape(ctx, slide, SW - MX - bw, 0.18, bw, 0.42, fill=AI_FILL, line=AI_STROKE, kind="round", radius=0.2)
        text(ctx, slide, SW - MX - bw, 0.18, bw, 0.42, [P(b, size=15, bold=True, align="c")], anchor="m",
             bg=AI_FILL, inset=0.02, record=False)
    bottom = 5.85 if s.get("takeaway") else BOTTOM
    if s.get("flow"):
        fh = s.get("flow_height", 1.25)
        flow(ctx, slide, s["flow"], MX, bottom - fh, CW, fh)
        bottom -= fh + 0.25
    fig = s.get("figure")
    bl = bullets_paras(s.get("bullets"), size=s.get("size", BODY))
    if fig:
        frac = s.get("figure_width", 0.55)
        fw = CW * frac
        tw = CW - fw - 0.35
        if s.get("figure_side", "right") == "right":
            tx, fx = MX, MX + tw + 0.35
        else:
            fx, tx = MX, MX + fw + 0.35
        if bl:
            text(ctx, slide, tx, TOP, tw, bottom - TOP, bl, floor=BODY_MIN - 2)
        picture(ctx, slide, fig, fx, TOP, fw, bottom - TOP, alt=s.get("alt"))
    elif bl:
        text(ctx, slide, MX, TOP, CW, bottom - TOP, bl, floor=BODY_MIN)
    if s.get("takeaway"):
        takeaway(ctx, slide, s["takeaway"])


def flow(ctx, slide, nodes, x, y, w, h):
    """A row of book-grammar boxes joined by arrows: kind human (rounded), ai (hexagon), step (rect).
    role picks the palette; dashed=True marks uncertainty (as in the book's figures)."""
    n = len(nodes)
    gap = 0.6
    bw = (w - gap * (n - 1)) / n
    for k, nd in enumerate(nodes):
        nd = nd if isinstance(nd, dict) else {"label": nd}
        kind = {"human": "round", "ai": "hex", "step": "rect"}[nd.get("kind", "step")]
        role = nd.get("role", "ai" if kind == "hex" else ("human" if nd.get("kind") == "human" else "neutral"))
        hf, ht, border = ROLE_STYLE[role]
        bx = x + k * (bw + gap)
        shape(ctx, slide, bx, y, bw, h, fill=hf, line=border, lw=1.75, kind=kind, dash=nd.get("dashed", False),
              radius=0.18)
        pad = 0.35 if kind == "hex" else 0.15
        text(ctx, slide, bx + pad, y, bw - 2 * pad, h, [P(nd["label"], size=nd.get("size", 22), bold=True, color=ht,
                                                       align="c")], anchor="m", bg=hf, floor=18)
        if k < n - 1:
            arrow(ctx, slide, bx + bw + 0.06, y + h / 2, bx + bw + gap - 0.06, y + h / 2, color=INK, lw=2.25)


def L_deep(ctx, slide, s):
    L_concept(ctx, slide, s, badge=s.get("badge", "Going deeper · optional · not on exams"))


def L_figure(ctx, slide, s):
    kicker(ctx, slide, s.get("kicker"))
    set_title(ctx, slide, s["title"])
    bottom = 5.85 if s.get("takeaway") else BOTTOM
    if s.get("caption"):
        bottom -= 0.45
        text(ctx, slide, MX, bottom + 0.05, CW, 0.4, [P(s["caption"], size=16, italic=True, color=MUTED, align="c")],
             floor=14)
    picture(ctx, slide, s["figure"], MX, TOP, CW, bottom - TOP, alt=s.get("alt"))
    if s.get("takeaway"):
        takeaway(ctx, slide, s["takeaway"])


def L_compare(ctx, slide, s):
    kicker(ctx, slide, s.get("kicker"))
    set_title(ctx, slide, s["title"])
    cols = s["columns"]
    n = len(cols)
    gap = 0.3
    cw = (CW - gap * (n - 1)) / n
    bottom = 5.8 if s.get("takeaway") else BOTTOM
    hh = s.get("header_height", 0.85)
    for i, col in enumerate(cols):
        x = MX + i * (cw + gap)
        role = col.get("role", "neutral")
        hf, ht, border = ROLE_STYLE[role]
        thick = role == "risk"
        dashed = bool(col.get("dashed"))
        shape(ctx, slide, x, TOP, cw, bottom - TOP, fill=WHITE, line=border, lw=3 if thick else 1.5, dash=dashed)
        shape(ctx, slide, x, TOP, cw, hh, fill=hf, line=border, lw=3 if thick else 1.5, dash=dashed)
        text(ctx, slide, x + 0.15, TOP, cw - 0.3, hh, [P(col["heading"], size=24, bold=True, color=ht, align="c")],
             anchor="m", bg=hf, floor=18)
        paras = bullets_paras(col.get("bullets"), size=col.get("size", 24))
        if col.get("text"):
            paras = [P(col["text"], size=col.get("size", 24))] + paras
        text(ctx, slide, x + 0.2, TOP + hh + 0.15, cw - 0.4, bottom - TOP - hh - 0.25, paras, floor=CARD_MIN)
    if s.get("takeaway"):
        takeaway(ctx, slide, s["takeaway"])


def L_worked(ctx, slide, s):
    kicker(ctx, slide, s.get("kicker"))
    set_title(ctx, slide, s["title"])
    shown = s["_shown"]
    steps = s["steps"]
    final = shown >= len(steps)
    y = TOP
    if s.get("context"):
        text(ctx, slide, MX, y - 0.05, CW, 0.55, [P(s["context"], size=20, italic=True, color=MUTED)], floor=18)
        y += 0.55
    bottom = 5.85 if (final and s.get("result")) else BOTTOM
    fig = s.get("figure") if (final or s.get("figure_always")) else None
    sw_ = CW * (0.52 if fig else 1.0)
    n = len(steps)
    gap = 0.12
    rh = (bottom - y - gap * (n - 1)) / n
    for k, st in enumerate(steps):
        yy = y + k * (rh + gap)
        if k < shown:
            newest = (k == shown - 1) and not final
            fill = SOFT if newest else WHITE
            shape(ctx, slide, MX, yy, sw_, rh, fill=fill, line=NAVY if newest else SOFT_STROKE,
                  lw=3 if newest else 1.25, kind="round", radius=0.1)
            d = min(0.55, rh - 0.16)
            shape(ctx, slide, MX + 0.15, yy + (rh - d) / 2, d, d, fill=NAVY, kind="oval")
            text(ctx, slide, MX + 0.15, yy + (rh - d) / 2, d, d, [P(str(k + 1), size=20, bold=True, color=WHITE,
                                                                     align="c")], anchor="m", bg=NAVY, inset=0)
            runs = [P(f"**{st['label']}** — {st['text']}" if st.get("text") else f"**{st['label']}**", size=24)]
            text(ctx, slide, MX + 0.3 + d, yy, sw_ - d - 0.45, rh, runs, anchor="m", bg=fill, floor=CARD_MIN)
        else:
            shape(ctx, slide, MX, yy, sw_, rh, fill=SOFT, kind="round", radius=0.1)
            text(ctx, slide, MX + 0.3, yy, sw_ - 0.4, rh,
                 [P(f"Step {k + 1} · {st['label']} — coming next", size=20, color=MUTED)], anchor="m", bg=SOFT)
    if fig:
        picture(ctx, slide, fig, MX + sw_ + 0.3, y, CW - sw_ - 0.3, bottom - y, alt=s.get("alt"))
    if final and s.get("result"):
        takeaway(ctx, slide, s["result"])


def L_quiz(ctx, slide, s):
    ans = s.get("_answer", False)
    kicker(ctx, slide, s.get("kicker", "Quick check"))
    set_title(ctx, slide, s.get("answer_title", "Answer") + (": " + s["title"] if s.get("title") else "")
              if ans else s.get("title_prefix", "Quick check") + (": " + s["title"] if s.get("title") else ""))
    y = TOP
    qsize = 26 if ans else 30
    qh = 1.3 if not ans else 1.0
    text(ctx, slide, MX, y, CW, qh, [P(s["question"], size=qsize, bold=not ans, color=INK if not ans else MUTED)],
         floor=22)
    y += qh + 0.1
    opts = s.get("options") or []
    key = s.get("answer")
    bottom = BOTTOM - (0.95 if (ans and s.get("explanation")) or (not ans and s.get("instruction")) else 0)
    if opts:
        gap = 0.12
        rh = min(1.0, (bottom - y - gap * (len(opts) - 1)) / len(opts))
        letters = "abcdefgh"
        for k, o in enumerate(opts):
            yy = y + k * (rh + gap)
            label = None
            correct = False
            if ans:
                if isinstance(key, list):
                    label = str(key[k])
                else:
                    correct = (letters[k] == str(key).strip("() ").lower())
                    label = "Correct" if correct else None
            fill = SOFT if correct else WHITE
            shape(ctx, slide, MX, yy, CW, rh, fill=fill, line=NAVY if correct else SOFT_STROKE,
                  lw=3.5 if correct else 1.25, kind="round", radius=0.1)
            tag = s.get("option_tags", None)
            lt = tag[k] if tag else f"({letters[k]})"
            col = MUTED if (ans and not correct and not isinstance(key, list)) else INK
            text(ctx, slide, MX + 0.2, yy, 0.9, rh, [P(lt, size=24, bold=True, color=NAVY)], anchor="m", bg=fill)
            lab_w = (text_width(label, ctx.font_sans, 18, True) / 72 + 0.45) if label else 0
            lw_ = lab_w + 0.25 if label else 0
            text(ctx, slide, MX + 1.1, yy, CW - 1.3 - lw_, rh, [P(o, size=24, color=col)], anchor="m", bg=fill,
                 floor=CARD_MIN)
            if label:
                lx = MX + CW - 0.2 - lab_w
                shape(ctx, slide, lx, yy + (rh - 0.5) / 2, lab_w, 0.5, fill=NAVY, kind="round", radius=0.2)
                text(ctx, slide, lx, yy + (rh - 0.5) / 2, lab_w, 0.5,
                     [P(label, size=18, bold=True, color=WHITE, align="c")], anchor="m", bg=NAVY, inset=0.02)
    elif ans:
        shape(ctx, slide, MX, y, CW, bottom - y, fill=SOFT, line=NAVY, lw=2, kind="round", radius=0.12)
        text(ctx, slide, MX + 0.3, y + 0.1, CW - 0.6, bottom - y - 0.2,
             [P("Model answer", size=20, bold=True, color=NAVY, space_after=0.3)] + [P(a, size=26) for a in
                                                                                  ([s["model_answer"]] if isinstance(s.get("model_answer"), str) else s.get("model_answer", []))],
             anchor="m", bg=SOFT, floor=CARD_MIN)
    if ans and s.get("explanation"):
        takeaway(ctx, slide, s["explanation"], y=BOTTOM - 0.85, h=0.85)
    if not ans and s.get("instruction"):
        text(ctx, slide, MX, BOTTOM - 0.8, CW, 0.7, [P(s["instruction"], size=22, italic=True, color=MUTED)],
             anchor="m", floor=18)
    if s.get("legend") and ans:
        text(ctx, slide, MX, 0.2, CW, 0.38, [P(s["legend"], size=15, color=MUTED, align="r")], record=False)


def L_tps(ctx, slide, s):
    kicker(ctx, slide, s.get("kicker", "Think · Pair · Share"))
    set_title(ctx, slide, s["title"])
    y = TOP
    ph = 2.05
    shape(ctx, slide, MX, y, CW, ph, fill=SOFT, kind="round", radius=0.15)
    shape(ctx, slide, MX, y, 0.12, ph, fill=NAVY)
    pr = s["prompt"] if isinstance(s["prompt"], list) else [s["prompt"]]
    text(ctx, slide, MX + 0.35, y, CW - 0.6, ph, [P(p, size=28, bold=(i == 0), space_after=0.25) for i, p in enumerate(pr)],
         anchor="m", bg=SOFT, floor=22)
    phases = s.get("phases") or [{"name": "Think", "min": 1, "text": "On your own, in writing"},
                                 {"name": "Pair", "min": 2, "text": "Compare with a neighbor"},
                                 {"name": "Share", "min": 2, "text": "A few pairs report out"}]
    n = len(phases)
    gap = 0.55
    bw = (CW - gap * (n - 1)) / n
    yy = y + ph + 0.35
    bh = BOTTOM - yy
    for k, p_ in enumerate(phases):
        x = MX + k * (bw + gap)
        shape(ctx, slide, x, yy, bw, bh, fill=WHITE, line=NAVY, lw=2, kind="round", radius=0.2)
        text(ctx, slide, x + 0.2, yy + 0.1, bw - 0.4, bh - 0.2,
             [P(f"{p_['name']} · {p_['min']} min", size=26, bold=True, color=NAVY, align="c", space_after=0.25),
              P(p_.get("text", ""), size=22, align="c")], anchor="m", floor=CARD_MIN)
        if k < n - 1:
            arrow(ctx, slide, x + bw + 0.08, yy + bh / 2, x + bw + gap - 0.08, yy + bh / 2, color=NAVY, lw=2.5)


def L_timeline(ctx, slide, s):
    kicker(ctx, slide, s.get("kicker"))
    set_title(ctx, slide, s["title"])
    ev = s["events"]
    n = len(ev)
    bottom = 5.85 if s.get("takeaway") else BOTTOM
    ly = TOP + 0.95
    shape(ctx, slide, MX + 0.2, ly - 0.03, CW - 0.4, 0.06, fill=NAVY)
    gap = 0.25
    cw = (CW - gap * (n - 1)) / n
    for k, e in enumerate(ev):
        x = MX + k * (cw + gap)
        cx = x + cw / 2
        text(ctx, slide, x, TOP - 0.05, cw, 0.62, [P(e["label"], size=22, bold=True, color=NAVY, align="c")],
             anchor="b", floor=18)
        d = 0.5
        shape(ctx, slide, cx - d / 2, ly - d / 2, d, d, fill=NAVY, line=WHITE, lw=2, kind="oval")
        text(ctx, slide, cx - d / 2, ly - d / 2, d, d, [P(str(k + 1), size=18, bold=True, color=WHITE, align="c")],
             anchor="m", bg=NAVY, inset=0)
        tier = e.get("tier")
        cy = ly + 0.45
        tier_h = 0.5 if tier else 0
        ch = bottom - cy - tier_h - (0.1 if tier else 0)
        role = e.get("role", "neutral")
        hf, _, border = ROLE_STYLE[role]
        fill = hf if role in ("ai", "verified", "soft") else WHITE
        tc = OK_TEXT if role == "verified" else INK
        shape(ctx, slide, x, cy, cw, ch, fill=fill, line=border, lw=1.5, kind="hex" if role == "ai" else "round",
              radius=0.12)
        text(ctx, slide, x + (0.35 if role == "ai" else 0.15), cy + 0.08, cw - (0.7 if role == "ai" else 0.3), ch - 0.16,
             [P(e["text"], size=22, align="c", color=tc)], anchor="m", bg=fill, floor=CARD_MIN - 2)
        if tier:
            tw_ = min(cw, 0.45 + len(tier) * 0.105)
            tx = cx - tw_ / 2
            shape(ctx, slide, tx, bottom - 0.45, tw_, 0.42, fill=WHITE, line=NAVY if tier != "inferred" else MUTED,
                  lw=1.25, kind="round", radius=0.2, dash=(tier == "inferred"))
            text(ctx, slide, tx, bottom - 0.45, tw_, 0.42, [P(tier, size=15, color=NAVY, align="c")], anchor="m",
                 inset=0.02, record=False)
    if s.get("takeaway"):
        takeaway(ctx, slide, s["takeaway"])


def L_lab(ctx, slide, s):
    kicker(ctx, slide, s.get("kicker"))
    set_title(ctx, slide, s["title"])
    y = TOP
    if s.get("goal"):
        text(ctx, slide, MX, y - 0.05, CW, 0.6, [P(f"**Goal:** {s['goal']}", size=24)], floor=20)
        y += 0.65
    side = s.get("side") or []
    lw_ = CW * (0.6 if side else 1.0)
    steps = s["steps"]
    n = len(steps)
    gap = 0.1
    rh = (BOTTOM - y - gap * (n - 1)) / n
    for k, st in enumerate(steps):
        st = st if isinstance(st, dict) else {"text": st}
        yy = y + k * (rh + gap)
        shape(ctx, slide, MX, yy, lw_, rh, fill=WHITE, line=SOFT_STROKE, kind="round", radius=0.08)
        d = min(0.46, rh - 0.1)
        shape(ctx, slide, MX + 0.12, yy + (rh - d) / 2, d, d, fill=NAVY, kind="oval")
        text(ctx, slide, MX + 0.12, yy + (rh - d) / 2, d, d, [P(str(k + 1), size=17, bold=True, color=WHITE, align="c")],
             anchor="m", bg=NAVY, inset=0)
        mw = 1.05 if st.get("min") else 0
        text(ctx, slide, MX + 0.25 + d, yy, lw_ - d - 0.4 - mw, rh, [P(st["text"], size=21)], anchor="m",
             floor=CARD_MIN - 2)
        if mw:
            text(ctx, slide, MX + lw_ - mw - 0.1, yy, mw, rh, [P(f"{st['min']} min", size=17, bold=True, color=NAVY,
                                                                 align="r")], anchor="m", inset=0.02)
    if side:
        sx = MX + lw_ + 0.3
        swd = CW - lw_ - 0.3
        sg = 0.15
        heights = []
        for c in side:
            heights.append(paras_height([P(c["heading"], size=20, bold=True), P(c["text"], size=20)],
                                        (swd - 0.4) * 72, ctx.font_sans, 1.0) / 72 + 0.45)
        total = sum(heights) + sg * (len(side) - 1)
        avail = BOTTOM - y
        scale = avail / total
        yy = y
        for c, hh in zip(side, heights):
            hh *= scale
            role = c.get("role", "soft")
            hf, ht, border = ROLE_STYLE[role]
            shape(ctx, slide, sx, yy, swd, hh, fill=hf if role in ("soft", "ai") else WHITE, line=border,
                  lw=3 if role == "risk" else 1.25, kind="round", radius=0.1)
            bgc = hf if role in ("soft", "ai") else WHITE
            text(ctx, slide, sx + 0.18, yy + 0.08, swd - 0.36, hh - 0.16,
                 [P(c["heading"], size=20, bold=True, color=NAVY if bgc != AI_FILL else INK, space_after=0.2),
                  P(c["text"], size=20)], anchor="m", bg=bgc, floor=17)
            yy += hh + sg


def L_assignment(ctx, slide, s):
    kicker(ctx, slide, s.get("kicker"))
    set_title(ctx, slide, s["title"], w=CW)
    due = s.get("due")
    y = TOP
    if due:
        shape(ctx, slide, MX, y - 0.05, CW, 0.55, fill=AI_FILL, line=AI_STROKE, kind="round", radius=0.15)
        text(ctx, slide, MX + 0.2, y - 0.05, CW - 0.4, 0.55, [P(f"**Due:** {due}", size=22)], anchor="m", bg=AI_FILL)
        y += 0.7
    lw_ = CW * 0.47
    parts = s.get("parts", [])
    text(ctx, slide, MX, y, lw_, 0.45, [P("What to submit", size=22, bold=True, color=NAVY)])
    paras = [P(f"**{k + 1}.** {p}", size=21, space_after=0.35) for k, p in enumerate(parts)]
    bottom = BOTTOM - (0.6 if s.get("note") else 0)
    text(ctx, slide, MX, y + 0.5, lw_, bottom - y - 0.5, paras, floor=CARD_MIN - 2)
    rub = s.get("rubric") or []
    if rub:
        tx = MX + lw_ + 0.35
        tw = CW - lw_ - 0.35
        text(ctx, slide, tx, y, tw, 0.45, [P(s.get("rubric_title", "Rubric"), size=22, bold=True, color=NAVY)])
        table(ctx, slide, tx, y + 0.5, tw, bottom - y - 0.5,
              [["Criterion", "Pts", "Full credit"]] + [[r["criterion"], str(r["points"]), r["full"]] for r in rub],
              col_frac=[0.27, 0.11, 0.62], size=17)
    if s.get("note"):
        text(ctx, slide, MX, BOTTOM - 0.5, CW, 0.5, [P(s["note"], size=17, italic=True, color=MUTED)], anchor="m",
             floor=15)


def table(ctx, slide, x, y, w, h, rows, col_frac, size=18, min_size=15):
    nr, nc = len(rows), len(rows[0])
    widths = [w * f for f in col_frac]
    sz = size
    while True:
        heights = []
        for r in rows:
            hmax = 0
            for c, cell in enumerate(r):
                hh = paras_height([P(cell, size=sz)], (widths[c] - 0.16) * 72, ctx.font_sans, 1.0) / 72 + 0.14
                hmax = max(hmax, hh)
            heights.append(hmax)
        if sum(heights) <= h or sz <= min_size:
            break
        sz -= 0.5
    if sum(heights) > h:
        ctx.warn(f"TABLE OVERFLOW ({sum(heights):.2f} in > {h:.2f} in)")
    gf = slide.shapes.add_table(nr, nc, E(x), E(y), E(w), E(sum(heights)))
    tbl = gf.table
    tblPr = tbl._tbl.tblPr
    for attr in ("bandRow", "firstRow"):
        tblPr.set(attr, "1")
    sid = tblPr.find(qn("a:tableStyleId"))
    if sid is not None:
        sid.text = "{5940675A-B579-460E-94D1-54222C63F5DA}"  # 'No Style, Table Grid'
    for c in range(nc):
        tbl.columns[c].width = E(widths[c])
    for r in range(nr):
        tbl.rows[r].height = E(heights[r])
        for c in range(nc):
            cell = tbl.cell(r, c)
            cell.margin_left = cell.margin_right = E(0.08)
            cell.margin_top = cell.margin_bottom = E(0.05)
            head = r == 0
            fill = NAVY if head else (SOFT if r % 2 == 0 else WHITE)
            cell.fill.solid()
            cell.fill.fore_color.rgb = rgb(fill)
            tf = cell.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.line_spacing = Pt(sz * LS)
            for t, b, i, _ in parse_runs(rows[r][c], bold=head or c == 0):
                run = p.add_run()
                run.text = t
                run.font.name = ctx.font_sans
                run.font.size = Pt(sz)
                run.font.bold = b
                run.font.italic = i
                run.font.color.rgb = rgb(WHITE if head else INK)
            ctx.visible.append((ctx.slide_no, plain(rows[r][c])))
    return gf


def L_key_terms(ctx, slide, s):
    kicker(ctx, slide, s.get("kicker"))
    set_title(ctx, slide, s["title"])
    terms = s["terms"]
    size = s.get("size", 22)
    bottom = BOTTOM - (0.6 if s.get("note") else 0)
    while True:
        x, y = MX, TOP
        h = size * 0.0275 + 0.3
        place = []
        for t in terms:
            w = text_width(plain(t), ctx.font_sans, size, True) / 72 + 0.5
            if x + w > MX + CW:
                x = MX
                y += h + 0.18
            place.append((t, x, y, w))
            x += w + 0.18
        if y + h <= bottom or size <= 18:
            break
        size -= 1
    if y + h > bottom:
        ctx.warn("KEY TERMS overflow")
    for t, x, y, w in place:
        deep = "(Deep)" in t
        shape(ctx, slide, x, y, w, h, fill=WHITE if deep else SOFT, line=MUTED if deep else NAVY, lw=1.25,
              kind="round", radius=h / 2, dash=False)
        text(ctx, slide, x, y, w, h, [P(t, size=size, bold=not deep, color=NAVY if not deep else MUTED, align="c")],
             anchor="m", bg=SOFT if not deep else WHITE, inset=0.02)
    if s.get("note"):
        text(ctx, slide, MX, BOTTOM - 0.5, CW, 0.5, [P(s["note"], size=18, italic=True, color=MUTED)], anchor="m")


def L_exit_ticket(ctx, slide, s):
    kicker(ctx, slide, s.get("kicker", "Exit ticket"))
    set_title(ctx, slide, s.get("title", "Exit ticket"))
    qs = s["questions"]
    bottom = BOTTOM - (0.95 if s.get("instruction") else 0)
    n = len(qs)
    gap = 0.2
    rh = (bottom - TOP - gap * (n - 1)) / n
    for k, q in enumerate(qs):
        yy = TOP + k * (rh + gap)
        shape(ctx, slide, MX, yy, CW, rh, fill=WHITE, line=NAVY, lw=1.75, kind="round", radius=0.12)
        d = min(0.65, rh - 0.2)
        shape(ctx, slide, MX + 0.2, yy + (rh - d) / 2, d, d, fill=NAVY, kind="oval")
        text(ctx, slide, MX + 0.2, yy + (rh - d) / 2, d, d, [P(str(k + 1), size=22, bold=True, color=WHITE, align="c")],
             anchor="m", bg=NAVY, inset=0)
        text(ctx, slide, MX + 0.45 + d, yy, CW - d - 0.65, rh, [P(q, size=26)], anchor="m", floor=BODY_MIN - 2)
    if s.get("instruction"):
        takeaway(ctx, slide, s["instruction"], y=BOTTOM - 0.8, h=0.8)


def L_references(ctx, slide, s):
    set_title(ctx, slide, s["title"])
    paras = []
    for r in s["_refs"]:
        p = P(r, size=REF_SIZE, space_after=0.5)
        paras.append(p)
    sp = text(ctx, slide, MX, TOP, CW, BOTTOM - TOP, paras)
    for para in sp.text_frame.paragraphs:  # hanging indent
        pPr = para._p.get_or_add_pPr()
        pPr.set("marL", str(int(Pt(28))))
        pPr.set("indent", str(-int(Pt(28))))


LAYOUTS = {
    "title": L_title, "session_plan": L_session_plan, "objectives": L_objectives, "section": L_section,
    "concept": L_concept, "figure": L_figure, "compare": L_compare, "worked": L_worked, "quiz": L_quiz,
    "tps": L_tps, "timeline": L_timeline, "lab": L_lab, "assignment": L_assignment, "key_terms": L_key_terms,
    "exit_ticket": L_exit_ticket, "references": L_references, "deep": L_deep,
}
WORD_LIMIT_EXEMPT = {"references", "assignment", "session_plan", "lab", "key_terms", "title", "objectives"}


# --------------------------------------------------------------------------- expansion
def expand(spec) -> list[dict]:
    """Turn spec slides into concrete slides (reveals, quiz answers, reference pages)."""
    out = []
    session = None
    sessions = spec["deck"].get("sessions", {})
    for s in spec["slides"]:
        s = dict(s)
        if s.get("session"):
            session = s["session"]
        s["_session"] = session
        lab = sessions.get(session, {}).get("label", session or "")
        s["_session_label"] = lab
        lay = s["layout"]
        if lay == "worked":
            reveal = s.get("reveal") or [len(s["steps"])]
            notes_list = s.get("notes_reveal") or []
            for k, nshow in enumerate(reveal):
                t = dict(s)
                t["_shown"] = nshow
                if k < len(notes_list):
                    t["notes"] = notes_list[k]
                    t["minutes"] = notes_list[k].get("minutes", s.get("minutes"))
                elif k > 0:
                    t["notes"] = {"say": f"(Continued from the previous slide.)", "book": s["notes"].get("book", "")}
                    t["_reveal_cont"] = True
                    t["minutes"] = 0
                out.append(t)
        elif lay == "quiz":
            q = dict(s)
            out.append(q)
            a = dict(s)
            a["_answer"] = True
            a["notes"] = s.get("answer_notes") or {"say": "", "book": s.get("notes", {}).get("book", "")}
            a["minutes"] = s.get("answer_minutes", 1)
            out.append(a)
        elif lay == "references":
            refs = list(s["refs"])
            per = s.get("per_slide", 7)
            pages = [refs[i:i + per] for i in range(0, len(refs), per)]
            for k, pg in enumerate(pages):
                t = dict(s)
                t["_refs"] = pg
                if len(pages) > 1:
                    t["title"] = f"{s.get('title', 'References')} ({k + 1} of {len(pages)})"
                if k > 0:
                    t["_reveal_cont"] = True
                    t["notes"] = {"say": "(References continued.)", "book": s["notes"].get("book", "")}
                out.append(t)
        else:
            out.append(s)
    return out


# --------------------------------------------------------------------------- theme
THEME_FONTS = ("Source Serif 4", "Source Sans 3")


def apply_theme(prs, serif, sans):
    master = prs.slide_master
    theme = master.part.part_related_by(RT.THEME)
    xml = theme.blob.decode("utf-8")
    xml = re.sub(r'(<a:majorFont>\s*<a:latin typeface=")[^"]*', r"\g<1>" + serif, xml)
    xml = re.sub(r'(<a:minorFont>\s*<a:latin typeface=")[^"]*', r"\g<1>" + sans, xml)
    colors = {"dk1": INK, "lt1": WHITE, "dk2": NAVY, "lt2": SOFT, "accent1": NAVY, "accent2": RISK,
              "accent3": OK, "accent4": AI_FILL, "accent5": MUTED, "accent6": NAVY_DARK}
    for k, v in colors.items():
        xml = re.sub(rf"(<a:{k}>)\s*<a:(?:srgbClr|sysClr)[^>]*/>", rf'\1<a:srgbClr val="{v.lstrip("#")}"/>', xml)
    xml = re.sub(r'name="Office Theme"', 'name="AI for All"', xml)
    theme._blob = xml.encode("utf-8")


def new_presentation(ctx_fonts=(SERIF, SANS)):
    prs = Presentation()
    prs.slide_width = E(SW)
    prs.slide_height = E(SH)
    apply_theme(prs, *ctx_fonts)
    return prs


# --------------------------------------------------------------------------- checks
NUM_RE = re.compile(r"(?<![\w§.])[−\-+]?\d[\d,]*(?:\.\d+)?\s?%?")


def number_check(ctx, slides_text, sources_text):
    """Warn about numbers on slides or in notes that do not occur in the source files."""
    norm_src = sources_text.replace("−", "-").replace(" ", "").replace(" ", " ")
    nums_src = set(m.group(0).replace(" ", "").lstrip("+-") for m in NUM_RE.finditer(norm_src))
    flagged = {}
    for sn, t in slides_text:
        t = t.replace("−", "-")
        for m in NUM_RE.finditer(t):
            tok = m.group(0).replace(" ", "").lstrip("+-")
            after = t[m.end():m.end() + 8].lower()
            if re.match(r"\s*(min|minute|slide|of\b)", after):
                continue
            base = tok.rstrip("%")
            try:
                val = float(base.replace(",", ""))
            except ValueError:
                continue
            if "%" not in tok and "," not in tok and "." not in tok and val <= 20:
                continue
            if tok in nums_src or base in nums_src or base.replace(",", "") in nums_src:
                continue
            flagged.setdefault(tok, set()).add(sn)
    for tok, sl in sorted(flagged.items()):
        ctx.warnings.append(f"NUMBER NOT IN SOURCES: '{tok}' on slides {sorted(sl)}")


# --------------------------------------------------------------------------- main build
def build(spec_path: Path, preview=False, out=None, fonts=None, quiet=False):
    spec = yaml.safe_load(spec_path.read_text(encoding="utf-8"))
    d = spec["deck"]
    serif, sans = fonts or (SERIF, SANS)
    prs = new_presentation((serif, sans))
    ctx = Ctx(spec=spec, prs=prs, font_sans=sans, font_serif=serif)
    layout = prs.slide_layouts[5]  # 'Title Only': every slide gets a real title (screen readers)
    slides = expand(spec)
    for s in slides:
        ctx.slide_no += 1
        slide = prs.slides.add_slide(layout)
        fn = LAYOUTS.get(s["layout"])
        if not fn:
            raise SystemExit(f"unknown layout '{s['layout']}' (slide {ctx.slide_no})")
        before = len(ctx.visible)
        fn(ctx, slide, s)
        dark = s["layout"] == "title"
        if s["layout"] != "title":
            footer(ctx, slide, dark=False)
        words = sum(len(t.split()) for sn, t in ctx.visible[before:] if sn == ctx.slide_no)
        if s["layout"] not in WORD_LIMIT_EXEMPT and words > 50:
            ctx.warn(f"{words} words on slide (guide: about 40)")
        notes = build_notes(ctx, s)
        slide.notes_slide.notes_text_frame.text = notes
        ctx.notes_all.append((ctx.slide_no, notes))
        if isinstance(s.get("minutes"), (int, float)):
            ctx.minutes.append((s.get("_session"), float(s["minutes"]), ctx.slide_no))
    # checks
    src_text = ""
    for f in d.get("sources", []):
        p = ROOT / f
        if p.exists():
            src_text += p.read_text(encoding="utf-8") + "\n"
        else:
            ctx.warnings.append(f"source file not found: {f}")
    if src_text:
        number_check(ctx, ctx.visible + ctx.notes_all, src_text)
    cp = prs.core_properties
    cp.title = f"AI for All · Chapter {d['chapter']}: {d['title']}"
    cp.author = d.get("author", "Şadi Evren Şeker")
    cp.subject = "Lecture slides"
    cp.keywords = "AI for All; lecture; slides"
    cp.revision = 1
    import datetime as _dt
    stamp = _dt.datetime(2026, 1, 1)
    cp.created = cp.modified = stamp
    cp.last_modified_by = "tools/build_slides.py"
    out = out or ROOT / "slides" / "out" / f"ch{int(d['chapter']):02d}-{d['slug']}.pptx"
    out.parent.mkdir(parents=True, exist_ok=True)
    prs.save(out)
    # report
    tot = {}
    for sess, m, _ in ctx.minutes:
        tot[sess] = tot.get(sess, 0) + m
    print(f"wrote {out.relative_to(ROOT)} · {len(prs.slides)} slides")
    for k, v in tot.items():
        target = d.get("sessions", {}).get(k, {}).get("minutes")
        flag = "" if not target or abs(v - target) <= 2 else f"  <-- target {target}"
        print(f"  session {k}: {v:g} min{flag}")
    if ctx.warnings:
        print(f"{len(ctx.warnings)} warning(s):")
        for w in ctx.warnings:
            print("  -", w)
    else:
        print("no warnings")
    if preview:
        sys.path.insert(0, str(ROOT / "tools"))
        from preview_slides import render_deck
        outdir = ROOT / "build" / "slides-check" / f"ch{int(d['chapter']):02d}"
        render_deck(out, outdir)
        print(f"preview images in {outdir.relative_to(ROOT)}")
    return ctx


def build_template():
    """slides/template/ai4all-16x9.pptx (theme only) and the layout gallery deck."""
    tdir = ROOT / "slides" / "template"
    tdir.mkdir(parents=True, exist_ok=True)
    prs = new_presentation()
    prs.save(tdir / "ai4all-16x9.pptx")
    print(f"wrote {(tdir / 'ai4all-16x9.pptx').relative_to(ROOT)}")
    g = tdir / "gallery.yaml"
    if g.exists():
        build(g, out=tdir / "layout-gallery.pptx")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("spec", nargs="?", help="slides/specs/chNN.yaml")
    ap.add_argument("--preview", action="store_true", help="render PNG check images to build/slides-check/chNN/")
    ap.add_argument("--template", action="store_true", help="build slides/template/ files")
    ap.add_argument("--fonts", nargs=2, metavar=("SERIF", "SANS"),
                    help="override fonts, e.g. --fonts Georgia Arial for machines without Source fonts")
    a = ap.parse_args()
    if a.template:
        build_template()
    if a.spec:
        build(Path(a.spec).resolve(), preview=a.preview, fonts=tuple(a.fonts) if a.fonts else None)
    if not a.spec and not a.template:
        ap.print_help()


if __name__ == "__main__":
    main()
