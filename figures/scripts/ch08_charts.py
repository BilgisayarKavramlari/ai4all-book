"""Chapter 8 data charts (color + gray SVG). Run from the repo root after ch08_experiments.py:
    python3 figures/scripts/ch08_charts.py
F8.6  published values (data/ch08_citations.csv; Walters & Wilder, 2023)
F8.9  constructed calibration record (data/ch08_calibration_groups.csv; ch08_experiments.py)
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
                     "svg.fonttype": "none"})

STYLE = {
    "color": {"main": "#1C3D6E", "accent": "#FCE38A", "risk": "#C2410C", "ink": "#1D1D1F", "hatch": None,
              "risk_hatch": None, "muted": "#5C5C66"},
    "gray": {"main": "#3A3A3A", "accent": "#FFFFFF", "risk": "#FFFFFF", "ink": "#000000", "hatch": "///",
             "risk_hatch": "xx", "muted": "#444444"},
}


def read(name):
    with open(os.path.join(ROOT, "data", name), encoding="utf8") as fh:
        return list(csv.DictReader(fh))


def save(fig, fid, mode):
    out = os.path.join(ROOT, "figures", "out", mode, f"{fid}.svg")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)


def f8_6(mode):
    s = STYLE[mode]
    rows = read("ch08_citations.csv")
    fig, ax = plt.subplots(figsize=(8.0, 3.9))
    x = [0, 1]
    w = 0.36
    for i, r in enumerate(rows):
        fab = float(r["fabricated_pct"])
        err = float(r["substantive_error_among_real_pct"])
        b1 = ax.bar(x[i] - w / 2, fab, w, color=s["risk"], edgecolor=s["ink"], linewidth=1, hatch=s["risk_hatch"],
                    label="References that did not exist" if i == 0 else None)
        b2 = ax.bar(x[i] + w / 2, err, w, color=s["accent"], edgecolor=s["ink"], linewidth=1, hatch=s["hatch"],
                    label="Real references with substantive errors" if i == 0 else None)
        ax.text(x[i] - w / 2, fab + 2, f"{fab:.0f}%", ha="center", fontsize=12, fontweight="bold", color=s["ink"])
        ax.text(x[i] + w / 2, err + 2, f"{err:.0f}%", ha="center", fontsize=12, fontweight="bold", color=s["ink"])
    ax.set_xticks(x, [r["model"] for r in rows])
    ax.set_ylim(0, 70)
    ax.set_ylabel("Share of references (%)")
    ax.legend(loc="upper right", frameon=False)
    ax.set_title(f"In one 2023 test, GPT-4 invented fewer references than GPT-3.5 "
                 f"({rows[1]['fabricated_pct']}% vs. {rows[0]['fabricated_pct']}%), but not none",
                 loc="left", fontweight="bold", fontsize=12.5, pad=12)
    fig.text(0.01, -0.06, "Source: Walters & Wilder (2023), Scientific Reports. Short literature reviews written by "
             "ChatGPT (GPT-3.5 and GPT-4) on 42 topics;\nerror share is among the references that did exist. "
             "Results for these models on this task, as published; newer tools differ.",
             fontsize=9.5, color=s["ink"])
    save(fig, "f8-06-citations", mode)


def f8_9(mode):
    s = STYLE[mode]
    rows = read("ch08_calibration_groups.csv")
    fig, ax = plt.subplots(figsize=(6.6, 5.0))
    ax.plot([0, 100], [0, 100], linestyle="--", color=s["ink"], linewidth=1.2)
    ax.text(70, 75, "perfect calibration", rotation=37, fontsize=10.5, color=s["muted"], ha="center")
    xs = [float(r["mean_stated_confidence"]) for r in rows]
    ys = [float(r["share_correct_pct"]) for r in rows]
    ax.bar(xs, ys, width=8, color=s["main"], edgecolor=s["ink"], linewidth=1, hatch=s["hatch"], alpha=0.9)
    for xi, yi, r in zip(xs, ys, rows):
        ax.text(xi, yi / 2, f"{int(r['n_correct'])} of\n{int(r['n_items'])}", ha="center", va="center",
                fontsize=11.5, fontweight="bold", color="#FFFFFF" if mode == "color" else s["ink"],
                bbox=None if mode == "color" else dict(facecolor="#FFFFFF", edgecolor="none", pad=1.5))
        ax.annotate("", xy=(xi, xi), xytext=(xi, yi), arrowprops=dict(arrowstyle="->", color=s["risk"]
                    if mode == "color" else s["ink"], lw=1.6))
        ax.plot([xi], [xi], marker="o", color=s["ink"], markersize=5)
    ax.set_xticks(xs, [f"{r['group']}\n(mean {float(r['mean_stated_confidence']):.0f}%)" for r in rows])
    ax.set_xlim(40, 105)
    ax.set_ylim(0, 105)
    ax.set_xlabel("Stated confidence group")
    ax.set_ylabel("Share of answers that were correct (%)")
    top = rows[-1]
    ax.set_title(f"This constructed tool's \"{top['group']} sure\" answers were right\n"
                 f"only {int(top['n_correct'])} times in {int(top['n_items'])}", loc="left", fontweight="bold",
                 fontsize=12.5, pad=10)
    fig.text(0.01, -0.1, "Constructed data for teaching (30 items; data/ch08_calibration_toy.csv), not a real tool.\n"
             "Bars below the dashed diagonal = overconfidence; each arrow runs from the share correct up to the group's mean stated confidence (dot).", fontsize=9.5,
             color=s["ink"])
    save(fig, "f8-09-calibration-toy", mode)


if __name__ == "__main__":
    for mode in ("color", "gray"):
        f8_6(mode)
        f8_9(mode)
    print("rendered f8-06-citations, f8-09-calibration-toy")
