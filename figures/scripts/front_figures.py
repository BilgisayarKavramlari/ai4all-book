"""Front-matter figures (SVG, color + gray). Run from the repo root:
    python3 figures/scripts/front_figures.py

F0.1 — the legend of the book's diagram language ("A Visual Guide to This Book").
Uses only figlib.py primitives, so the legend shows exactly what the chapter figures draw:
rectangle = step · rounded box = human · hexagon = AI component · diamond = decision ·
dashed outline = inferred · thick border (hatched in print) = risk · dark fill = highlighted step.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from figlib import render, MUTED, INK  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# (label inside the shape, kind, role, dashed, thick, explanation)
SHAPES = [
    ("Step", "step", "neutral", False, False,
     "Rectangle: a step or stage in a process"),
    ("Person", "human", "neutral", False, False,
     "Rounded box: a person acts or decides"),
    ("AI tool", "ai", "ai", False, False,
     "Hexagon: an AI component produces something"),
    ("Choice?", "decision", "neutral", False, False,
     "Diamond: a decision point with more than one way out"),
]
LINES = [
    ("Inferred", "step", "neutral", True, False,
     "Dashed outline: inferred, this book's reading; never anything else"),
    ("Risk", "step", "risk", False, True,
     "Thick border (hatched in print): a risk or warning"),
    ("Checked", "step", "verified", False, False,
     "Green fill (mid-gray in print), labeled: verified information"),
    ("This step", "step", "highlight", False, True,
     "Dark fill, light text: the part this figure is about"),
]


def legend(f):
    ink, muted = INK[f.mode], MUTED[f.mode]
    f.text(200, 34, "Shape: who or what acts", size=16, weight="700")
    f.text(600, 34, "Line and fill: how sure, how risky", size=16, weight="700")
    f.line(400, 60, 400, 470, color=muted, width=1)
    for col, items in ((0, SHAPES), (1, LINES)):
        x0 = 24 + col * 400
        for i, (lab, kind, role, dashed, thick, expl) in enumerate(items):
            y = 70 + i * 100
            h = 76 if kind == "decision" else 64
            yy = y + (76 - h) / 2
            f.box(x0, yy, 140, h, lab, role=role, kind=kind, dashed=dashed, thick=thick, size=14)
            f.text(x0 + 160, y + 38, expl, size=14, anchor="start", width=205, color=ink)
    # arrow row: one legend item drawn as a line, not a box
    f.arrow(60, 500, 170, 500)
    f.text(190, 500, "Solid arrow: what comes next, or what feeds what", size=14, anchor="start",
           width=560, color=ink)
    f.text(400, 538, "Every meaning is carried by shape, line or label, so it survives the gray print edition.",
           size=13, color=muted, italic=True)


FIGS = [
    ("f0-01-legend", legend, 800, 560,
     "Shape tells you who or what acts; line and fill tell you how sure, how risky and where to look"),
]

if __name__ == "__main__":
    for fid, fn, w, h, title in FIGS:
        render(fid, fn, w, h, title, ROOT)
        print("rendered", fid)
