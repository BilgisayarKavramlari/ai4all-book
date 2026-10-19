#!/usr/bin/env python3
"""Render a .pptx made by tools/build_slides.py to PNG check images (no Office needed).

    python3 tools/preview_slides.py slides/out/ch01-*.pptx [outdir]

This is a checking tool, not a general PowerPoint renderer: it understands the
shapes build_slides.py writes (rectangles, rounded rectangles, ovals, hexagons,
connectors with arrowheads, text boxes, pictures, tables) and draws them with the
same fonts and the same line-wrapping metrics. Text that does not fit its box is
outlined in red, and every such case is listed in check-report.txt. Output:
slide-NN.png (1600 x 900) and contact sheets sheet-N.png (12 slides each).
"""
from __future__ import annotations

import io
import re
import sys
from pathlib import Path

from PIL import Image, ImageDraw
from pptx import Presentation
from pptx.oxml.ns import qn

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_slides import pil_font  # noqa: E402

PXW = 1600
A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"


def _hex(el, default=None):
    if el is None:
        return default
    c = el.find(A + "srgbClr")
    if c is not None:
        return "#" + c.get("val")
    return default


class R:
    def __init__(self, prs):
        self.k = PXW / prs.slide_width  # px per EMU
        self.h = int(round(prs.slide_height * self.k))
        self.ppt = self.k * 12700        # px per point
        self.problems: list[str] = []

    def px(self, emu):
        return emu * self.k

    # ------------------------------------------------------------------ geometry
    def draw_geom(self, img, d, x, y, w, h, prst, adj, fill, line, lw, dash):
        box = [x, y, x + w, y + h]
        lwp = max(1, int(round(lw * self.ppt))) if line else 0
        if prst == "roundRect":
            r = (adj if adj is not None else 0.16667) * min(w, h)
            d.rounded_rectangle(box, radius=r, fill=fill, outline=None if dash else line, width=lwp)
        elif prst == "ellipse":
            d.ellipse(box, fill=fill, outline=None if dash else line, width=lwp)
        elif prst == "hexagon":
            o = (adj if adj is not None else 0.25) * min(w, h)
            pts = [(x + o, y), (x + w - o, y), (x + w, y + h / 2), (x + w - o, y + h), (x + o, y + h), (x, y + h / 2)]
            d.polygon(pts, fill=fill)
            if line and not dash:
                d.line(pts + [pts[0]], fill=line, width=lwp, joint="curve")
        else:
            d.rectangle(box, fill=fill, outline=None if dash else line, width=lwp)
        if line and dash:
            self.dashed_rect(d, box, line, lwp)

    def dashed_rect(self, d, box, color, width, seg=12, gap=8):
        x0, y0, x1, y1 = box
        for (ax, ay, bx, by) in [(x0, y0, x1, y0), (x1, y0, x1, y1), (x1, y1, x0, y1), (x0, y1, x0, y0)]:
            length = abs(bx - ax) + abs(by - ay)
            n = int(length // (seg + gap)) + 1
            for i in range(n):
                t0 = i * (seg + gap) / max(length, 1)
                t1 = min(1, (i * (seg + gap) + seg) / max(length, 1))
                d.line([ax + (bx - ax) * t0, ay + (by - ay) * t0, ax + (bx - ax) * t1, ay + (by - ay) * t1],
                       fill=color, width=width)

    # ------------------------------------------------------------------ text
    def layout_text(self, txBody, width_px):
        """Returns list of paragraphs: dict(lines=[[(text,font,color)]], line_h, space_after, align, bullet, x0)."""
        out = []
        for p in txBody.findall(A + "p"):
            pPr = p.find(A + "pPr")
            algn = pPr.get("algn", "l") if pPr is not None else "l"
            marL = int(pPr.get("marL", 0)) if pPr is not None else 0
            indent = int(pPr.get("indent", 0)) if pPr is not None else 0
            lnspc = spcaft = None
            bullet = None
            if pPr is not None:
                ls = pPr.find(A + "lnSpc/" + A + "spcPts")
                if ls is not None:
                    lnspc = int(ls.get("val")) / 100
                sa = pPr.find(A + "spcAft/" + A + "spcPts")
                if sa is not None:
                    spcaft = int(sa.get("val")) / 100
                bu = pPr.find(A + "buChar")
                if bu is not None:
                    bullet = bu.get("char")
            runs = []
            maxsz = 0
            for r in p.findall(A + "r"):
                rPr = r.find(A + "rPr")
                sz = int(rPr.get("sz", 1800)) / 100 if rPr is not None else 18
                maxsz = max(maxsz, sz)
                b = rPr is not None and rPr.get("b") == "1"
                i = rPr is not None and rPr.get("i") == "1"
                lat = rPr.find(A + "latin") if rPr is not None else None
                fam = lat.get("typeface") if lat is not None else "Source Sans 3"
                col = _hex(rPr.find(A + "solidFill") if rPr is not None else None, "#000000")
                t = r.find(A + "t").text or ""
                runs.append((t, fam, b, i, sz, col))
            if not runs:
                out.append(dict(lines=[], line_h=(lnspc or 18) * self.ppt, space_after=(spcaft or 0) * self.ppt,
                                align=algn, bullet=None, x0=0, sz=maxsz or 18))
                continue
            x0 = self.px(marL)
            avail = width_px - x0
            lines = [[]]
            cur = 0.0
            for t, fam, b, i, sz, col in runs:
                f = pil_font(fam, b, i, max(1, int(round(sz * self.ppt))))
                for tok in re.split(r"(\s+)", t):
                    if not tok:
                        continue
                    if tok.isspace():
                        if cur > 0:
                            w = f.getlength(" ")
                            lines[-1].append((" ", f, col))
                            cur += w
                        continue
                    w = f.getlength(tok)
                    if cur > 0 and cur + w > avail:
                        while lines[-1] and lines[-1][-1][0] == " ":
                            lines[-1].pop()
                        lines.append([])
                        cur = 0
                    lines[-1].append((tok, f, col))
                    cur += w
            line_h = (lnspc or maxsz * 1.2) * self.ppt
            out.append(dict(lines=lines, line_h=line_h, space_after=(spcaft or 0) * self.ppt, align=algn,
                            bullet=bullet, x0=x0, bx=self.px(marL + indent), sz=maxsz,
                            bcol=_hex(pPr.find(A + "buClr") if pPr is not None else None, "#000000")))
        return out

    def draw_text(self, img, d, txBody, x, y, w, h, label):
        bp = txBody.find(A + "bodyPr")
        li = int(bp.get("lIns", 91440)) if bp is not None else 91440
        ri = int(bp.get("rIns", 91440)) if bp is not None else 91440
        ti = int(bp.get("tIns", 45720)) if bp is not None else 45720
        bi = int(bp.get("bIns", 45720)) if bp is not None else 45720
        anchor = bp.get("anchor", "t") if bp is not None else "t"
        ix, iy = x + self.px(li), y + self.px(ti)
        iw, ih = w - self.px(li) - self.px(ri), h - self.px(ti) - self.px(bi)
        paras = self.layout_text(txBody, iw)
        if not any(p["lines"] for p in paras):
            return
        total = 0.0
        for k, p in enumerate(paras):
            total += len(p["lines"]) * p["line_h"] + (p["space_after"] if k < len(paras) - 1 else 0)
        if anchor == "ctr":
            cy = iy + (ih - total) / 2
        elif anchor == "b":
            cy = iy + ih - total
        else:
            cy = iy
        if total > ih + 2:
            self.problems.append(f"{label}: text needs {total:.0f}px, box has {ih:.0f}px")
            self.dashed_rect(d, [x, y, x + w, y + h], "#FF0000", 3)
        for k, p in enumerate(paras):
            for n, line in enumerate(p["lines"]):
                lw = sum(f.getlength(t) for t, f, _ in line)
                if p["align"] == "ctr":
                    lx = ix + p["x0"] + (iw - p["x0"] - lw) / 2
                elif p["align"] == "r":
                    lx = ix + iw - lw
                else:
                    lx = ix + p["x0"]
                base = cy + p["line_h"] * 0.5 + p["sz"] * self.ppt * 0.36
                if n == 0 and p["bullet"]:
                    f0 = line[0][1] if line else None
                    if f0:
                        d.text((ix + p["bx"], base), p["bullet"], font=f0, fill=p["bcol"], anchor="ls")
                for t, f, col in line:
                    d.text((lx, base), t, font=f, fill=col, anchor="ls")
                    lx += f.getlength(t)
                cy += p["line_h"]
            if k < len(paras) - 1:
                cy += p["space_after"]

    # ------------------------------------------------------------------ slide
    def render(self, slide, n):
        img = Image.new("RGB", (PXW, self.h), "white")
        d = ImageDraw.Draw(img)
        for shp in slide.shapes:
            el = shp._element
            x, y = self.px(shp.left or 0), self.px(shp.top or 0)
            w, h = self.px(shp.width or 0), self.px(shp.height or 0)
            label = f"slide {n} '{shp.name}'"
            tag = el.tag.split("}")[1]
            if tag == "pic":
                im = Image.open(io.BytesIO(shp.image.blob)).convert("RGB")
                img.paste(im.resize((max(1, int(w)), max(1, int(h))), Image.LANCZOS), (int(x), int(y)))
                continue
            if tag == "cxnSp":
                ln = el.find(".//" + A + "ln")
                col = _hex(ln.find(A + "solidFill"), "#000000") if ln is not None else "#000000"
                lw = int(ln.get("w", 12700)) / 12700 if ln is not None else 1
                bx, by = self.px(shp.begin_x), self.px(shp.begin_y)
                ex, ey = self.px(shp.end_x), self.px(shp.end_y)
                d.line([bx, by, ex, ey], fill=col, width=max(1, int(lw * self.ppt)))
                if ln is not None and ln.find(A + "tailEnd") is not None:
                    import math
                    ang = math.atan2(ey - by, ex - bx)
                    s = 8 + lw * 3
                    pts = [(ex, ey), (ex - s * math.cos(ang - 0.45), ey - s * math.sin(ang - 0.45)),
                           (ex - s * math.cos(ang + 0.45), ey - s * math.sin(ang + 0.45))]
                    d.polygon(pts, fill=col)
                continue
            if tag == "graphicFrame" and shp.has_table:
                tbl = shp.table
                cy = y
                for r, row in enumerate(tbl.rows):
                    rh = self.px(row.height)
                    cx = x
                    for c, col in enumerate(tbl.columns):
                        cw = self.px(col.width)
                        cell = tbl.cell(r, c)
                        tcPr = cell._tc.find(A + "tcPr")
                        fill = _hex(tcPr.find(A + "solidFill"), None) if tcPr is not None else None
                        d.rectangle([cx, cy, cx + cw, cy + rh], fill=fill, outline="#8A94A3", width=1)
                        self.draw_text(img, d, cell._tc.find(A + "txBody"), cx, cy, cw, rh, f"{label} cell {r},{c}")
                        cx += cw
                    cy += rh
                if cy - y > h + 2:
                    self.problems.append(f"{label}: table taller than frame")
                continue
            if tag != "sp":
                continue
            spPr = el.find(qn("p:spPr"))
            prst, adj, fill, line, lw, dash = "rect", None, None, None, 0, False
            if spPr is not None:
                g = spPr.find(A + "prstGeom")
                if g is not None:
                    prst = g.get("prst")
                    gd = g.find(A + "avLst/" + A + "gd")
                    if gd is not None:
                        m = re.search(r"val (\d+)", gd.get("fmla", ""))
                        if m:
                            adj = int(m.group(1)) / 100000
                fill = _hex(spPr.find(A + "solidFill"), None)
                ln = spPr.find(A + "ln")
                if ln is not None and ln.find(A + "noFill") is None:
                    line = _hex(ln.find(A + "solidFill"), None)
                    lw = int(ln.get("w", 12700)) / 12700
                    dash = ln.find(A + "prstDash") is not None
            if fill or line:
                self.draw_geom(img, d, x, y, w, h, prst, adj, fill, line, lw, dash)
            tx = el.find(qn("p:txBody"))
            if tx is not None:
                self.draw_text(img, d, tx, x, y, w, h, label)
        return img


def render_deck(pptx: Path, outdir: Path):
    outdir.mkdir(parents=True, exist_ok=True)
    for old in outdir.glob("*.png"):
        old.unlink()
    prs = Presentation(str(pptx))
    r = R(prs)
    thumbs = []
    for n, slide in enumerate(prs.slides, 1):
        img = r.render(slide, n)
        img.save(outdir / f"slide-{n:02d}.png")
        th = img.resize((400, int(400 * img.height / img.width)), Image.LANCZOS)
        thumbs.append(th)
    per = 12
    for s in range(0, len(thumbs), per):
        group = thumbs[s:s + per]
        cols = 3
        rows = -(-len(group) // cols)
        tw, th_ = 400, thumbs[0].height
        sheet = Image.new("RGB", (cols * (tw + 16) + 16, rows * (th_ + 40) + 16), "#9AA3AF")
        dd = ImageDraw.Draw(sheet)
        f = pil_font("Source Sans 3", True, False, 20)
        for k, th in enumerate(group):
            cx = 16 + (k % cols) * (tw + 16)
            cy = 16 + (k // cols) * (th_ + 40)
            sheet.paste(th, (cx, cy + 24))
            dd.text((cx, cy), f"{s + k + 1}", font=f, fill="#111111")
        sheet.save(outdir / f"sheet-{s // per + 1}.png")
    rep = outdir / "check-report.txt"
    rep.write_text("\n".join(r.problems) + ("\n" if r.problems else "no overflow found\n"), encoding="utf-8")
    if r.problems:
        print(f"preview: {len(r.problems)} overflow problem(s) — see {rep}")
    return r.problems


if __name__ == "__main__":
    p = Path(sys.argv[1])
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("build/slides-check") / p.stem
    render_deck(p, out)
