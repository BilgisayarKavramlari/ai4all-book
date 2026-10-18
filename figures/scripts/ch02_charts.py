"""Chapter 2 data charts (color + gray SVG). Run from the repo root after ch02_experiments.py:
    python3 figures/scripts/ch02_charts.py
F2.9 and F2.10 plot the book's own experiment (data/ch02_regimes.csv, data/ch02_overfitting.csv).
F2.14 is a worked mathematical illustration (no data).
"""
import csv
import os

import numpy as np
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
    "color": {"main": "#1C3D6E", "accent": "#FCE38A", "risk": "#C2410C", "ink": "#1D1D1F", "hatch": None},
    "gray": {"main": "#3A3A3A", "accent": "#FFFFFF", "risk": "#FFFFFF", "ink": "#000000", "hatch": "///"},
}


def read(name):
    with open(os.path.join(ROOT, "data", name), encoding="utf8") as fh:
        return list(csv.DictReader(fh))


def save(fig, fid, mode):
    out = os.path.join(ROOT, "figures", "out", mode, f"{fid}.svg")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)


NAMES = {"balanced": "Balanced,\ncorrect labels", "imbalanced": "Imbalanced\n(10 vs. 60 examples)",
         "noisy": "20% wrong labels,\nscattered", "systematic": "20% wrong labels,\none direction (8s as 3s)"}


def f2_9(mode):
    s = STYLE[mode]
    rows = read("ch02_regimes.csv")
    fig, ax = plt.subplots(figsize=(8.6, 4.2))
    x = np.arange(len(rows))
    w = 0.38
    ov = [float(r["overall_accuracy_pct"]) for r in rows]
    mi = [float(r["minority_class_accuracy_pct"]) for r in rows]
    ovs = [float(r["overall_sd"]) for r in rows]
    mis = [float(r["minority_sd"]) for r in rows]
    ax.bar(x - w / 2, ov, w, yerr=ovs, color=s["main"], edgecolor=s["ink"], linewidth=1,
           error_kw={"ecolor": s["ink"], "elinewidth": 1, "capsize": 3}, label="All test examples")
    ax.bar(x + w / 2, mi, w, yerr=mis, color=s["accent"], edgecolor=s["ink"], linewidth=1,
           hatch=s["hatch"], error_kw={"ecolor": s["ink"], "elinewidth": 1, "capsize": 3},
           label="The 8s (made rare in row 2, mislabeled in row 4)")
    for i in range(len(rows)):
        ax.text(x[i] - w / 2, ov[i] + ovs[i] + 2, f"{ov[i]:.1f}%", ha="center", fontsize=11.5,
                fontweight="bold", color=s["ink"])
        ax.text(x[i] + w / 2, mi[i] + mis[i] + 2, f"{mi[i]:.1f}%", ha="center", fontsize=11.5,
                fontweight="bold", color=s["ink"])
    ax.set_xticks(x, [NAMES[r["regime"]] for r in rows])
    ax.set_ylim(0, 128)
    ax.set_yticks([0, 20, 40, 60, 80, 100])
    ax.set_ylabel("Accuracy on new test examples (%)")
    ax.legend(loc="upper right", frameon=False, ncol=2, bbox_to_anchor=(1.0, 1.0))
    ax.set_title("The same share of wrong labels costs about 6 points when scattered and about 23 when they all point one way",
                 loc="left", fontweight="bold", fontsize=12.5, pad=22)
    fig.text(0.01, -0.07, "Book experiment: handwritten 3s, 5s and 8s (Alpaydin & Kaynak, 1998); logistic regression; "
             "averages of 30 runs, lines show ±1 standard deviation.", fontsize=9.5, color=s["ink"])
    save(fig, "f2-09-label-regimes", mode)


def f2_10(mode):
    s = STYLE[mode]
    rows = read("ch02_overfitting.csv")
    d = [int(r["max_depth"]) for r in rows]
    tr = [float(r["train_accuracy_pct"]) for r in rows]
    te = [float(r["test_accuracy_pct"]) for r in rows]
    fig, ax = plt.subplots(figsize=(8.2, 4.0))
    ax.plot(d, tr, color=s["main"], linewidth=2.4, marker="o", markersize=5, label="Training examples")
    ax.plot(d, te, color=s["ink"] if mode == "gray" else s["risk"], linewidth=2.4, linestyle="--",
            marker="s", markersize=5, markerfacecolor="white", label="New test examples")
    ax.text(20.6, tr[-1], f"Training: {tr[-1]:.0f}%", va="center", fontsize=12, fontweight="bold", color=s["ink"])
    ax.text(20.6, te[-1], f"Test: about {te[-1]:.0f}%", va="center", fontsize=12, fontweight="bold", color=s["ink"])
    ax.axvspan(11, 20.3, color="#EEEEEE", zorder=0)
    ax.text(15.7, 30, "Extra complexity goes\ninto memorizing", ha="center", fontsize=11.5, style="italic",
            color=s["ink"])
    ax.set_xlim(0.5, 25.5)
    ax.set_ylim(0, 108)
    ax.set_xticks([1, 5, 10, 15, 20])
    ax.set_xlabel("Model complexity (decision-tree depth)")
    ax.set_ylabel("Accuracy (%)")
    ax.legend(loc="lower center", frameon=False, bbox_to_anchor=(0.62, 0.02))
    ax.set_title("When a model starts memorizing, training accuracy keeps rising but test accuracy levels off",
                 loc="left", fontweight="bold", fontsize=12.5)
    fig.text(0.01, -0.07, "Book experiment: all ten handwritten digits (Alpaydin & Kaynak, 1998); averages of 10 runs.",
             fontsize=9.5, color=s["ink"])
    save(fig, "f2-10-overfitting", mode)


def f2_14(mode):
    s = STYLE[mode]
    w = np.linspace(0.5, 5.5, 200)
    err = (300 - 100 * w) ** 2 / 1000  # squared error, in thousands, for a 100 m² flat that sold for 300
    fig, ax = plt.subplots(figsize=(8.2, 3.8))
    ax.plot(w, err, color=s["main"], linewidth=2.4)
    e = lambda v: (300 - 100 * v) ** 2 / 1000  # noqa: E731
    ax.plot([2], [e(2)], "o", color=s["ink"], markersize=9)
    ax.plot([2.6], [e(2.6)], "o", color=s["ink"], markersize=9, markerfacecolor="white", markeredgewidth=2)
    ax.annotate("", xy=(2.6, e(2.6) + 0.4), xytext=(2.0, e(2.0) + 0.4),
                arrowprops={"arrowstyle": "-|>", "color": s["ink"], "linewidth": 2})
    ax.text(1.85, e(2), "Start: w = 2\npredicts 200, error 100", fontsize=11.5, color=s["ink"], ha="right", va="center")
    ax.text(2.2, 3.4, "One step downhill", fontsize=11.5, color=s["ink"], fontweight="bold", ha="right")
    ax.plot([3], [0], "^", color=s["ink"], markersize=10)
    ax.text(3.6, 1.0, "Lowest error: w = 3", fontsize=11.5, color=s["ink"])
    ax.set_xlabel("The model's one setting, w   (price = w × size)")
    ax.set_ylabel("Squared error (× 1,000)")
    ax.set_ylim(-0.8, 28)
    ax.set_title("Each step moves the setting toward lower error", loc="left", fontweight="bold")
    fig.text(0.01, -0.07, "Illustration: a 100-square-meter apartment that sold for 300 (thousand dollars). Not real market data.",
             fontsize=9.5, color=s["ink"])
    save(fig, "f2-14-gradient-step", mode)


if __name__ == "__main__":
    for mode in ("color", "gray"):
        f2_9(mode)
        f2_10(mode)
        f2_14(mode)
    print("charts rendered")
