"""Chapter 15 data chart (color + gray SVG). Run from the repo root:
    python3 figures/scripts/ch15_charts.py
F15.6  Sweeney (2000): share of the 1990 U.S. population likely unique on three demographic fields
       (data/ch15_reid.csv; values copied from the paper; "likely unique" is the paper's estimate from
       census summary tables, not a count of identified people).
"""
import csv
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import font_manager  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
for fam in ("Source Sans 3", "Source Sans Pro"):
    if any(fam in f.name for f in font_manager.fontManager.ttflist):
        plt.rcParams["font.family"] = fam
        break
plt.rcParams.update({"font.size": 12, "axes.spines.top": False, "axes.spines.right": False,
                     "svg.fonttype": "none", "svg.hashsalt": "ch15"})
STYLE = {"color": {"main": "#1C3D6E", "ink": "#1D1D1F", "muted": "#5C5C66", "hatch": None},
         "gray": {"main": "#3A3A3A", "ink": "#000000", "muted": "#444444", "hatch": None}}


def read(name):
    with open(os.path.join(ROOT, "data", name), encoding="utf8") as fh:
        return list(csv.DictReader(fh))


def save(fig, fid, mode):
    if os.environ.get("PREVIEW_DIR"):
        fig.savefig(os.path.join(os.environ["PREVIEW_DIR"], f"{fid}-{mode}.png"), bbox_inches="tight", dpi=80)
    out = os.path.join(ROOT, "figures", "out", mode, f"{fid}.svg")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    fig.savefig(out, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)


def f15_6(mode):
    s = STYLE[mode]
    rows = read("ch15_reid.csv")
    labels = [r["geography"] for r in rows][::-1]
    vals = [float(r["share_likely_unique_pct"]) for r in rows][::-1]
    fig, ax = plt.subplots(figsize=(8.0, 3.4))
    bars = ax.barh(labels, vals, color=s["main"], height=0.55)
    for b, v in zip(bars, vals):
        ax.text(v + 1.5, b.get_y() + b.get_height() / 2, f"{v:.0f}%", va="center", fontsize=13,
                fontweight="bold", color=s["ink"])
    ax.set_xlim(0, 100)
    ax.set_xlabel("Share of the U.S. population likely unique on these three facts (%)", color=s["ink"])
    ax.tick_params(colors=s["ink"], labelsize=12)
    fig.text(0.01, -0.04, "Source: Sweeney (2000), estimates from 1990 U.S. Census summary data "
             "(87% = about 216 of 248 million people). Not a count of people identified.", fontsize=11,
             color=s["muted"])
    save(fig, "f15-06-reid", mode)


if __name__ == "__main__":
    for mode in ("color", "gray"):
        f15_6(mode)
    print("rendered f15-06-reid")
