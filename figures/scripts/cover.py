"""Front cover for *AI for All: Career-Ready AI Skills* (Şadi Evren Şeker).

Run from the repo root:
    python3 figures/scripts/cover.py

Writes (all hand-built SVG, standard library only):
    cover/cover-front.svg       8.5 x 11 in, 612 x 792 pt viewBox, full bleed, color
    cover/cover-front-gray.svg  same layout, grayscale (print interior / title page)
    cover/cover-epub.svg        1600 x 2560 px (EPUB cover), color, re-laid out
    cover/alt-1.svg, alt-2.svg, alt-3.svg (+ -gray)  the three studied compositions

The artwork reuses the book's visual grammar (docs/visual-guide.md, figlib.py):
rounded box = human step, hexagon = AI component, diamond = decision,
dashed line = uncertainty. Palette F (docs/decisions.md G4). Meaning is carried
by shape and fill/outline contrast, so the grayscale render reads the same.
"""
from __future__ import annotations

import html
import math
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "cover")

TITLE = "AI for All"
SUBTITLE = "Career-Ready AI Skills"
AUTHOR = "Şadi Evren Şeker"
EDITION = "First edition · 2027"
LOOP = ["Frame", "Prompt", "Verify", "Decide", "Disclose"]

SERIF = "'Source Serif 4', 'Source Serif Pro', Georgia, 'Times New Roman', serif"
SANS = "'Source Sans 3', 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif"

# Palette F (decisions.md G4) plus two neutrals; gray mode keeps lightness steps.
PAL = {
    "color": {
        "navy": "#1C3D6E",      # human
        "navy_deep": "#14304F",
        "ai": "#FCE38A",        # AI
        "ai_line": "#6B5A12",
        "paper": "#F6F4EF",
        "white": "#FFFFFF",
        "ink": "#1D1D1F",
        "soft": "#B9C6DA",      # secondary text / lines on navy
        "faint": "#3A5A8A",     # background pattern on navy
        "muted": "#5C5C66",
    },
    "gray": {
        "navy": "#2B2B2B",
        "navy_deep": "#1E1E1E",
        "ai": "#E6E6E6",
        "ai_line": "#000000",
        "paper": "#FFFFFF",
        "white": "#FFFFFF",
        "ink": "#000000",
        "soft": "#C4C4C4",
        "faint": "#4A4A4A",
        "muted": "#444444",
    },
}


def esc(s: str) -> str:
    return html.escape(s, quote=True)


class Svg:
    def __init__(self, w, h, mode, title, unit=""):
        self.w, self.h, self.mode, self.title, self.unit = w, h, mode, title, unit
        self.c = PAL[mode]
        self.parts: list[str] = []

    def add(self, s):
        self.parts.append(s)

    # ---- shapes (book grammar) ----
    def rounded(self, cx, cy, s, r, fill, stroke="none", sw=0, extra=""):
        self.add(f'<rect x="{cx - s / 2:.2f}" y="{cy - s / 2:.2f}" width="{s:.2f}" height="{s:.2f}" '
                 f'rx="{r:.2f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw:.2f}"{extra}/>')

    def hexagon(self, cx, cy, w, h, fill, stroke="none", sw=0, extra=""):
        c = w * 0.25
        pts = [(cx - w / 2 + c, cy - h / 2), (cx + w / 2 - c, cy - h / 2), (cx + w / 2, cy),
               (cx + w / 2 - c, cy + h / 2), (cx - w / 2 + c, cy + h / 2), (cx - w / 2, cy)]
        self.poly(pts, fill, stroke, sw, extra)

    def diamond(self, cx, cy, w, h, fill, stroke="none", sw=0, extra=""):
        pts = [(cx, cy - h / 2), (cx + w / 2, cy), (cx, cy + h / 2), (cx - w / 2, cy)]
        self.poly(pts, fill, stroke, sw, extra)

    def poly(self, pts, fill, stroke, sw, extra=""):
        p = " ".join(f"{a:.2f},{b:.2f}" for a, b in pts)
        self.add(f'<polygon points="{p}" fill="{fill}" stroke="{stroke}" stroke-width="{sw:.2f}" '
                 f'stroke-linejoin="round"{extra}/>')

    def line(self, x1, y1, x2, y2, stroke, sw, dash=None, cap="round", extra=""):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{stroke}" '
                 f'stroke-width="{sw:.2f}" stroke-linecap="{cap}"{d}{extra}/>')

    def path(self, d, stroke, sw, fill="none", dash=None, marker=None, extra=""):
        a = f' stroke-dasharray="{dash}"' if dash else ""
        m = f' marker-end="url(#{marker})"' if marker else ""
        self.add(f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw:.2f}" '
                 f'stroke-linecap="round" stroke-linejoin="round"{a}{m}{extra}/>')

    def text(self, x, y, s, size, family, weight=400, fill=None, anchor="start", tracking=0.0,
             opsz=None, extra=""):
        fill = fill or self.c["ink"]
        style = []
        if opsz:
            style.append(f"font-variation-settings:'opsz' {opsz}")
        st = f' style="{";".join(style)}"' if style else ""
        ls = f' letter-spacing="{tracking:.2f}"' if tracking else ""
        self.add(f'<text x="{x:.2f}" y="{y:.2f}" font-family="{family}" font-size="{size:.2f}" '
                 f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{ls}{st}{extra}>'
                 f'{esc(s)}</text>')

    def arrow_marker(self, mid, color, size):
        self.add(f'<marker id="{mid}" viewBox="0 0 10 10" refX="8" refY="5" markerUnits="userSpaceOnUse" '
                 f'markerWidth="{size:.2f}" markerHeight="{size:.2f}" orient="auto">'
                 f'<path d="M0,0 L10,5 L0,10 z" fill="{color}"/></marker>')

    def render(self, desc) -> str:
        u = self.unit
        return ('<?xml version="1.0" encoding="UTF-8"?>\n'
                f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" '
                f'width="{self.w}{u}" height="{self.h}{u}" role="img" aria-labelledby="t d" lang="en">'
                f'<title id="t">{esc(self.title)}</title><desc id="d">{esc(desc)}</desc>'
                + "".join(self.parts) + "</svg>\n")


def arc_path(cx, cy, r, a0, a1):
    """Clockwise (screen) arc from angle a0 to a1 in radians, a1 > a0."""
    x0, y0 = cx + r * math.cos(a0), cy + r * math.sin(a0)
    x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
    large = 1 if (a1 - a0) > math.pi else 0
    return f"M{x0:.2f},{y0:.2f} A{r:.2f},{r:.2f} 0 {large} 1 {x1:.2f},{y1:.2f}"


DESC = ("Book cover. Title AI for All, subtitle Career-Ready AI Skills, author Şadi Evren Şeker. "
        "Artwork: the book's AI Work Loop drawn as five shapes on a circle. Four rounded squares are "
        "human steps; the Decide step is a large solid diamond. A yellow hexagon, the AI tool, sits "
        "in the middle and reaches the loop only by dashed lines: AI assists, people decide.")


# =====================================================================================
# Alternative 1 — "The Loop": the AI Work Loop on a full navy field (chosen design)
# =====================================================================================
LAYOUT_LOOP = {
    # print: 612 x 792 pt
    "print": dict(W=612, H=792, M=54, unit="pt", title_y=172, title_size=106, sub_y=222, sub_size=34,
                  rule_y=None, cx=306, cy=488, R=170, node=52, dia=108, hexw=108, hexh=94,
                  label_size=12, author_y=742, author_size=23, ed_size=11.5, num_size=15),
    # EPUB: 1600 x 2560 px
    "epub": dict(W=1600, H=2560, M=140, unit="", title_y=540, title_size=330, sub_y=690, sub_size=100,
                 rule_y=None, cx=800, cy=1560, R=440, node=144, dia=290, hexw=290, hexh=252,
                 label_size=34, author_y=2420, author_size=72, ed_size=32, num_size=42),
}


def alt_loop(fmt, mode, *, labels=True, start_deg=-90):
    L = LAYOUT_LOOP[fmt]
    W, H, M = L["W"], L["H"], L["M"]
    s = Svg(W, H, mode, f"{TITLE}: {SUBTITLE} — {AUTHOR}", L["unit"])
    c = s.c
    k = W / 612  # stroke scale
    s.add("<defs>")
    s.arrow_marker("arr", c["white"], 13 * k)
    s.add("</defs>")
    s.add(f'<rect x="0" y="0" width="{W}" height="{H}" fill="{c["navy"]}"/>')

    # quiet inner disc marks the AI tool's zone inside the human loop
    cx, cy, R = L["cx"], L["cy"], L["R"]
    s.add(f'<circle cx="{cx}" cy="{cy}" r="{R * 0.62:.2f}" fill="{c["navy_deep"]}" stroke="none"/>')

    # ---- typography ----
    s.text(M - 4 * k, L["title_y"], TITLE, L["title_size"], SERIF, 700, c["white"], opsz=60,
           tracking=-1.5 * k)
    s.text(M, L["sub_y"], SUBTITLE, L["sub_size"], SANS, 600, c["ai"], tracking=0.2 * k)
    s.text(W - M, L["author_y"], AUTHOR, L["author_size"], SANS, 600, c["white"], anchor="end",
           tracking=0.3 * k)
    s.text(M, L["author_y"], EDITION.upper(), L["ed_size"], SANS, 600, c["soft"], tracking=1.6 * k)

    # ---- the loop ----
    n = 5
    angs = [math.radians(start_deg) + i * 2 * math.pi / n for i in range(n)]
    pos = [(cx + R * math.cos(a), cy + R * math.sin(a)) for a in angs]
    dec = 3  # Decide
    gap_node = (L["node"] * 0.80) / R
    gap_dec = (L["dia"] * 0.62) / R
    for i in range(n):
        a0 = angs[i] + (gap_dec if i == dec else gap_node)
        a1 = angs[i] + 2 * math.pi / n - (gap_dec if (i + 1) % n == dec else gap_node)
        s.path(arc_path(cx, cy, R, a0, a1), c["white"], 3.2 * k, marker="arr")

    # AI hexagon at the centre; dashed lines = AI output is uncertain until a person checks it
    hx, hy = cx, cy
    for i in (1, 2):  # Prompt, Verify
        px, py = pos[i]
        dx, dy = px - hx, py - hy
        d = math.hypot(dx, dy)
        ux, uy = dx / d, dy / d
        s.line(hx + ux * L["hexw"] * 0.52, hy + uy * L["hexw"] * 0.52,
               px - ux * L["node"] * 0.78, py - uy * L["node"] * 0.78,
               c["ai"], 2.6 * k, dash=f"{2 * k:.1f} {7 * k:.1f}")
    s.hexagon(hx, hy, L["hexw"], L["hexh"], c["ai"], c["ai_line"], 0 if mode == "color" else 1.5 * k)
    s.text(hx, hy + L["num_size"] * 0.36 * 1.6, "AI", L["num_size"] * 1.6, SANS, 700, c["ink"],
           anchor="middle", tracking=0.5 * k)

    # human steps (outlined rounded squares) and the decision (solid diamond)
    for i, (x, y) in enumerate(pos):
        if i == dec:
            d = L["dia"]
            s.diamond(x, y, d * 1.32, d * 1.32, "none", c["soft"], 1.6 * k,
                      extra=f' stroke-dasharray="{1 * k:.1f} {5.5 * k:.1f}" stroke-linecap="round"')
            s.diamond(x, y, d, d, c["white"], c["white"], 2 * k)
            s.text(x, y + L["label_size"] * 0.36 * 1.25, LOOP[i], L["label_size"] * 1.25, SANS, 700,
                   c["navy"], anchor="middle")
        else:
            s.rounded(x, y, L["node"], L["node"] * 0.28, c["navy"], c["white"], 3.2 * k)
            s.text(x, y + L["num_size"] * 0.36, str(i + 1), L["num_size"], SANS, 700, c["white"],
                   anchor="middle")
        if labels and i != dec:
            # labels sit outside the ring: above the top node, beside the side nodes,
            # below-outside the lower node
            a = angs[i]
            off = L["node"] * 0.5 + 10 * k
            ls_ = L["label_size"]
            if i == 0:
                s.text(x, y - off - ls_ * 0.2, LOOP[i].upper(), ls_, SANS, 600, c["soft"],
                       anchor="middle", tracking=1.2 * k)
            elif abs(math.sin(a)) < 0.6:
                side = 1 if math.cos(a) > 0 else -1
                s.text(x + side * off, y + ls_ * 0.36, LOOP[i].upper(), ls_, SANS, 600, c["soft"],
                       anchor="start" if side > 0 else "end", tracking=1.2 * k)
            else:
                side = 1 if math.cos(a) > 0 else -1
                s.text(x + side * (L["node"] * 0.5 + 2 * k), y + off + ls_ * 0.75, LOOP[i].upper(), ls_,
                       SANS, 600, c["soft"], anchor="start" if side > 0 else "end", tracking=1.2 * k)
    return s.render(DESC)


# =====================================================================================
# Alternative 2 — "Many drafts, one decision": AI options converge on a human diamond
# =====================================================================================
def alt_converge(mode):
    W, H, M = 612, 792, 54
    s = Svg(W, H, mode, f"{TITLE}: {SUBTITLE} — {AUTHOR}", "pt")
    c = s.c
    s.add("<defs>")
    s.arrow_marker("arr2", c["navy"], 14)
    s.add("</defs>")
    s.add(f'<rect width="{W}" height="{H}" fill="{c["paper"]}"/>')
    s.text(M - 4, 168, TITLE, 104, SERIF, 700, c["navy"], opsz=60, tracking=-1.5)
    s.text(M, 214, SUBTITLE, 31, SANS, 600, c["ink"])
    s.line(M, 246, M + 64, 246, c["navy"], 4, cap="butt")

    # cloud of AI drafts (hexagons), staggered
    dx_, dy_ = 50, 44
    hexes = []
    for col in range(3):
        rows = [5, 6, 5][col]
        for r in range(rows):
            x = 92 + col * dx_
            y = 486 - (rows - 1) * dy_ / 2 + r * dy_
            hexes.append((x, y, (col + r) % 3 == 1))
    tx, ty = 380, 486  # decision
    for (x, y, unc) in hexes:
        s.path(f"M{x + 22:.1f},{y:.1f} C{(x + tx) / 2 + 30:.1f},{y:.1f} {tx - 120:.1f},{ty:.1f} {tx - 62:.1f},{ty:.1f}",
               c["muted"] if mode == "color" else "#777777", 0.9)
    for (x, y, unc) in hexes:
        if unc:
            s.hexagon(x, y, 40, 34, c["paper"], c["ai_line"], 1.4, extra=' stroke-dasharray="4 3"')
        else:
            s.hexagon(x, y, 40, 34, c["ai"], c["ai_line"], 1.4)
    s.diamond(tx, ty, 124, 124, c["navy"], c["navy"], 2)
    s.text(tx, ty + 6, "Decide", 17, SANS, 700, c["white"], anchor="middle")
    s.path(f"M{tx + 66},{ty} L{502},{ty}", c["navy"], 4, marker="arr2")
    s.rounded(540, ty, 62, 18, c["white"], c["navy"], 4)
    # iterate back: dashed return arc
    s.path(f"M540,{ty - 40} C540,{ty - 190} 140,{ty - 230} 115,{ty - 150}", c["navy"], 1.8, dash="6 6",
           marker="arr2")
    s.text(W - M, 742, AUTHOR, 23, SANS, 600, c["navy"], anchor="end")
    s.text(M, 742, EDITION.upper(), 11.5, SANS, 600, c["muted"], tracking=1.6)
    return s.render(DESC.replace("Artwork: the book's AI Work Loop drawn as five shapes on a circle. "
                                 "Four rounded squares are human steps; the Decide step is a large solid "
                                 "diamond. A yellow hexagon, the AI tool, sits in the middle and reaches "
                                 "the loop only by dashed lines",
                                 "Artwork: many small hexagons, AI drafts, some dashed, converge on one "
                                 "solid diamond, a human decision, which leads to a single rounded square"))


# =====================================================================================
# Alternative 3 — "Pattern": a field of shapes, one loop drawn through it
# =====================================================================================
def alt_pattern(mode):
    W, H, M = 612, 792, 54
    s = Svg(W, H, mode, f"{TITLE}: {SUBTITLE} — {AUTHOR}", "pt")
    c = s.c
    panel_h = 498
    s.add(f'<rect width="{W}" height="{H}" fill="{c["paper"]}"/>')
    s.add(f'<rect width="{W}" height="{panel_h}" fill="{c["navy"]}"/>')
    cell = 68
    cols, rows = 9, 7
    ox, oy = (W - cols * cell) / 2 + cell / 2, 26 + cell / 2
    # loop path through cells (perimeter of a 4 x 3 block)
    loop = [(2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (6, 2), (6, 3), (6, 4), (5, 4), (4, 4),
            (3, 4), (2, 4), (2, 3), (2, 2)]
    dec = (4, 4)
    on = set(loop)
    pts = [(ox + i * cell, oy + j * cell) for i, j in loop]
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + " Z"
    s.path(d, c["white"], 3)
    for j in range(rows):
        for i in range(cols):
            x, y = ox + i * cell, oy + j * cell
            is_ai = (i + j) % 2 == 0
            if (i, j) == dec:
                continue
            if (i, j) in on:
                if is_ai:
                    s.hexagon(x, y, 44, 38, c["ai"], c["ai_line"], 0 if mode == "color" else 1.2)
                else:
                    s.rounded(x, y, 36, 10, c["navy"], c["white"], 3)
            else:
                if is_ai:
                    s.hexagon(x, y, 34, 29, "none", c["faint"], 1.6)
                else:
                    s.rounded(x, y, 26, 8, "none", c["faint"], 1.6)
    x, y = ox + dec[0] * cell, oy + dec[1] * cell
    s.diamond(x, y, 92, 92, c["white"], c["white"], 2)
    s.text(M - 4, 606, TITLE, 96, SERIF, 700, c["navy"], opsz=60, tracking=-1.5)
    s.text(M, 650, SUBTITLE, 30, SANS, 600, c["ink"])
    s.text(W - M, 742, AUTHOR, 23, SANS, 600, c["navy"], anchor="end")
    s.text(M, 742, EDITION.upper(), 11.5, SANS, 600, c["muted"], tracking=1.6)
    return s.render(DESC.replace("Artwork: the book's AI Work Loop drawn as five shapes on a circle. "
                                 "Four rounded squares are human steps; the Decide step is a large solid "
                                 "diamond. A yellow hexagon, the AI tool, sits in the middle and reaches "
                                 "the loop only by dashed lines",
                                 "Artwork: a grid of faint hexagons and rounded squares; one loop path "
                                 "lights up alternating human and AI shapes and passes through a single "
                                 "large white diamond, the decision"))


def write(name, svg):
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, name), "w", encoding="utf8") as fh:
        fh.write(svg)


def main():
    alts = {1: lambda m: alt_loop("print", m), 2: alt_converge, 3: alt_pattern}
    for k, fn in alts.items():
        write(f"alt-{k}.svg", fn("color"))
        write(f"alt-{k}-gray.svg", fn("gray"))
    # chosen design: alternative 1
    write("cover-front.svg", alt_loop("print", "color"))
    write("cover-front-gray.svg", alt_loop("print", "gray"))
    write("cover-epub.svg", alt_loop("epub", "color"))
    print("wrote", sorted(os.listdir(OUT)))


if __name__ == "__main__":
    main()
