"""Chapter 19 data charts (color + gray SVG). Run from the repo root:
    python3 figures/scripts/ch19_charts.py
F19.5  Ithaca restoration results (data/ch19_ithaca.csv; Assael et al., 2022, Nature 603, Table 1)
F19.21 (Deep 19.A) only if data/ch19_use_by_field.csv exists (source verified at draft time)
Numbers in the chapter are copied from these CSVs.
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
                     "svg.fonttype": "none", "svg.hashsalt": "ch19"})
plt.rcParams["font.sans-serif"] = ["Source Sans 3", "STIXGeneral", "DejaVu Sans"]  # no system-font fallback in print (D29)

STYLE = {
    "color": {"human": "#1C3D6E", "ai": "#FCE38A", "both": "#4CAF84", "ink": "#1D1D1F", "muted": "#5C5C66",
              "hatch": {"human": None, "ai": None, "both": None}},
    "gray": {"human": "#3A3A3A", "ai": "#FFFFFF", "both": "#BDBDBD", "ink": "#000000", "muted": "#444444",
             "hatch": {"human": None, "ai": "///", "both": "..."}},
}


def read(name):
    with open(os.path.join(ROOT, "data", name), encoding="utf8") as fh:
        return list(csv.DictReader(fh))


def save(fig, fid, mode):
    out = os.path.join(ROOT, "figures", "out", mode, f"{fid}.svg")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    fig.savefig(out, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)


def f19_5(mode):
    s = STYLE[mode]
    rows = read("ch19_ithaca.csv")
    keys = ["human", "ai", "both"]
    fig, ax = plt.subplots(figsize=(8.0, 3.3))
    ys = [2, 1, 0]
    for y, r, k in zip(ys, rows, keys):
        v = float(r["top1_accuracy_pct"])
        ax.barh(y, v, height=0.62, color=s[k], edgecolor=s["ink"], linewidth=1.2, hatch=s["hatch"][k])
        ax.text(v + 1.2, y, f"{v:.1f}%", va="center", ha="left", fontsize=12, fontweight="bold", color=s["ink"])
    ax.set_yticks(ys)
    ax.set_yticklabels(["Two experts alone", "Ithaca alone", "Two experts using\nIthaca's top-20 suggestions"])
    ax.set_xlim(0, 100)
    ax.set_xlabel("Top-1 accuracy: the first suggested restoration fully right (%)")
    ax.set_title("With Ithaca's suggestions, the experts were right more often than the model or the experts alone", loc="left", fontweight="bold", fontsize=12, pad=10)
    fig.text(0.01, -0.12, "Source: Assael et al. (2022), Nature 603, 280–283, Table 1. Test texts had characters "
             "hidden on purpose, so the answers were known.\nThe experts were two ancient-history graduate students. "
             "Bars also differ by pattern (print).", fontsize=9.5, color=s["ink"])
    save(fig, "f19-05-ithaca", mode)


def f19_21(mode):
    path = os.path.join(ROOT, "data", "ch19_use_by_field.csv")
    if not os.path.exists(path):
        return False
    s = STYLE[mode]
    rows = read("ch19_use_by_field.csv")
    fig, ax = plt.subplots(figsize=(8.0, 4.0))
    labels = [r["subject"] for r in rows]
    a = [float(r["share_conversations_pct"]) for r in rows]
    b = [float(r["share_degrees_pct"]) for r in rows]
    ys = list(range(len(rows)))[::-1]
    ax.barh([y + 0.2 for y in ys], a, height=0.38, color=s["human"], edgecolor=s["ink"],
            label="Share of student conversations (%)")
    ax.barh([y - 0.2 for y in ys], b, height=0.38, color=s["both"], edgecolor=s["ink"], hatch=s["hatch"]["both"],
            label="Share of U.S. bachelor's degrees (%)")
    for y, v1, v2 in zip(ys, a, b):
        ax.text(v1 + 0.6, y + 0.2, f"{v1:.1f}", va="center", fontsize=10.5, color=s["ink"])
        ax.text(v2 + 0.6, y - 0.2, f"{v2:.1f}", va="center", fontsize=10.5, color=s["ink"])
    ax.set_yticks(ys)
    ax.set_yticklabels(labels)
    ax.set_xlabel("Percent")
    ax.legend(frameon=False, loc="lower right", fontsize=10.5)
    ax.set_title(rows[0]["title"], loc="left", fontweight="bold", fontsize=12, pad=10)
    import textwrap
    fig.text(0.01, -0.16, "\n".join(textwrap.wrap(rows[0]["source"], 140)), fontsize=9.5, color=s["ink"])
    save(fig, "f19-21-use-by-field", mode)
    return True


if __name__ == "__main__":
    for mode in ("color", "gray"):
        f19_5(mode)
        f19_21(mode)
    print("rendered f19-05-ithaca (+ f19-21 if data present)")
