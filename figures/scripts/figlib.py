"""Shared SVG drawing library for AI for All figures.

Implements the book's visual grammar (docs/visual-guide.md, docs/decisions.md G4):
  rectangle = step · diamond = decision · rounded box = human · hexagon = AI component
  dashed outline = uncertainty.  Meaning never by color alone.

Every figure is rendered twice: mode="color" (EPUB/web) and mode="gray" (print).
Gray mode uses distinct lightness steps plus patterns, so roles stay readable in
black-and-white print.
"""
from __future__ import annotations

import html
import math
import os

FONT = "'Source Sans 3', 'Source Sans Pro', STIXGeneral, sans-serif"  # STIX (OFL) for symbols; no system fallback

# role -> (fill, stroke, text) per mode.  Palette F (decisions.md G4).
ROLES = {
    "color": {
        "human":    ("#1C3D6E", "#0F2440", "#FFFFFF"),
        "ai":       ("#FCE38A", "#6B5A12", "#1D1D1F"),
        "risk":     ("#C2410C", "#7A2808", "#FFFFFF"),
        "verified": ("#4CAF84", "#1F5E43", "#0B1F16"),
        "neutral":  ("#FFFFFF", "#3A3A3A", "#1D1D1F"),
        "soft":     ("#EEF2F7", "#8A94A3", "#1D1D1F"),
        "highlight": ("#1C3D6E", "#0F2440", "#FFFFFF"),
    },
    "gray": {
        "human":    ("#3A3A3A", "#000000", "#FFFFFF"),
        "ai":       ("#EDEDED", "#000000", "#000000"),
        "risk":     ("url(#hatch)", "#000000", "#000000"),  # light hatch + bold border in gray
        "verified": ("#BDBDBD", "#000000", "#000000"),
        "neutral":  ("#FFFFFF", "#000000", "#000000"),
        "soft":     ("#F4F4F4", "#7A7A7A", "#000000"),
        "highlight": ("#3A3A3A", "#000000", "#FFFFFF"),
    },
}
INK = {"color": "#1D1D1F", "gray": "#000000"}
MUTED = {"color": "#5C5C66", "gray": "#444444"}
ACCENT = {"color": "#C2410C", "gray": "#000000"}


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def wrap(text: str, width_px: float, size: float) -> list[str]:
    """Greedy wrap using an average glyph width for Source Sans (~0.52 em)."""
    max_chars = max(4, int(width_px / (size * 0.52)))
    out: list[str] = []
    for para in text.split("\n"):
        line = ""
        for word in para.split():
            trial = (line + " " + word).strip()
            if len(trial) <= max_chars:
                line = trial
            else:
                if line:
                    out.append(line)
                line = word
        out.append(line)
    return out


class Fig:
    def __init__(self, w: int, h: int, mode: str, title: str):
        self.w, self.h, self.mode, self.title = w, h, mode, title
        self.parts: list[str] = []

    # ---------- primitives ----------
    def text(self, x, y, s, size=14, weight="normal", anchor="middle", color=None,
             italic=False, width=None, line_h=1.22):
        color = color or INK[self.mode]
        size = max(size, 13)  # 13 px ≈ 8.2 pt when the 800-px canvas prints 7 in wide
        lines = wrap(s, width, size) if width else s.split("\n")
        y0 = y - (len(lines) - 1) * size * line_h / 2
        style = "font-style:italic;" if italic else ""
        for i, ln in enumerate(lines):
            self.parts.append(
                f'<text x="{x:.1f}" y="{y0 + i * size * line_h:.1f}" font-size="{size}" '
                f'font-weight="{weight}" text-anchor="{anchor}" dominant-baseline="middle" '
                f'fill="{color}" style="{style}">{esc(ln)}</text>')

    def _style(self, role, dashed=False, thick=False):
        fill, stroke, tcolor = ROLES[self.mode][role]
        sw = 3 if (thick or (role == "risk" and self.mode == "gray")) else 1.6
        dash = ' stroke-dasharray="7 5"' if dashed else ""
        return fill, f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{dash}', tcolor

    def box(self, x, y, w, h, label, role="neutral", kind="step", dashed=False,
            thick=False, size=14, weight="600", sub=None, sub_size=12):
        """kind: step (rect) | human (rounded) | ai (hexagon) | decision (diamond)."""
        _, st, tc = self._style(role, dashed, thick)
        if kind == "human":
            self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" {st}/>')
        elif kind == "ai":
            c = min(18, w * 0.12)
            pts = [(x + c, y), (x + w - c, y), (x + w, y + h / 2), (x + w - c, y + h),
                   (x + c, y + h), (x, y + h / 2)]
            self.parts.append(f'<polygon points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in pts)}" {st}/>')
        elif kind == "decision":
            pts = [(x + w / 2, y), (x + w, y + h / 2), (x + w / 2, y + h), (x, y + h / 2)]
            self.parts.append(f'<polygon points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in pts)}" {st}/>')
        else:
            self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" {st}/>')
        pad = 0.62 if kind == "decision" else 0.86
        if sub:
            self.text(x + w / 2, y + h * 0.34, label, size=size, weight=weight, color=tc, width=w * pad)
            self.text(x + w / 2, y + h * 0.70, sub, size=sub_size, weight="normal", color=tc, width=w * pad)
        else:
            self.text(x + w / 2, y + h / 2, label, size=size, weight=weight, color=tc, width=w * pad)

    def arrow(self, x1, y1, x2, y2, dashed=False, label=None, color=None, width=1.8,
              label_dy=-10, curve=0.0, size=12):
        color = color or INK[self.mode]
        dash = ' stroke-dasharray="6 4"' if dashed else ""
        if curve:
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            nx, ny = -(y2 - y1), (x2 - x1)
            n = math.hypot(nx, ny) or 1
            cx, cy = mx + curve * nx / n, my + curve * ny / n
            d = f"M{x1:.1f},{y1:.1f} Q{cx:.1f},{cy:.1f} {x2:.1f},{y2:.1f}"
        else:
            d = f"M{x1:.1f},{y1:.1f} L{x2:.1f},{y2:.1f}"
        self.parts.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}"{dash} '
                          f'marker-end="url(#arrow-{self.mode})"/>')
        if label:
            self.text((x1 + x2) / 2, (y1 + y2) / 2 + label_dy, label, size=size, color=MUTED[self.mode],
                      italic=True)

    def line(self, x1, y1, x2, y2, dashed=False, color=None, width=1.4):
        color = color or INK[self.mode]
        dash = ' stroke-dasharray="6 4"' if dashed else ""
        self.parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" '
                          f'stroke-width="{width}"{dash}/>')

    def raw(self, s: str):
        self.parts.append(s)

    # ---------- output ----------
    def svg(self) -> str:
        ink = INK[self.mode]
        defs = (f'<defs><marker id="arrow-{self.mode}" viewBox="0 0 10 10" refX="9" refY="5" '
                f'markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
                f'<path d="M0,0 L10,5 L0,10 z" fill="{ink}"/></marker>'
                '<pattern id="hatch" patternUnits="userSpaceOnUse" width="8" height="8" '
                'patternTransform="rotate(45)"><rect width="8" height="8" fill="#FFFFFF"/>'
                '<line x1="0" y1="0" x2="0" y2="8" stroke="#9A9A9A" stroke-width="1.3"/></pattern>'
                '<pattern id="dots" patternUnits="userSpaceOnUse" width="7" height="7">'
                '<rect width="7" height="7" fill="#FFFFFF"/><circle cx="3.5" cy="3.5" r="1.2" fill="#000"/></pattern>'
                '</defs>')
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" '
                f'width="{self.w}" height="{self.h}" role="img" font-family="{FONT}">'
                f'<title>{esc(self.title)}</title>{defs}'
                f'<rect width="{self.w}" height="{self.h}" fill="#FFFFFF"/>'
                + "".join(self.parts) + "</svg>")


def render(fig_id: str, draw, w: int, h: int, title: str, root: str):
    """draw(fig) builds the figure; writes color and gray SVGs."""
    for mode in ("color", "gray"):
        f = Fig(w, h, mode, title)
        draw(f)
        out = os.path.join(root, "figures", "out", mode, f"{fig_id}.svg")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", encoding="utf8") as fh:
            fh.write(f.svg())
