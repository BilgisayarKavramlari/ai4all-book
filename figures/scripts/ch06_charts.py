"""Chapter 6 data charts (color + gray SVG). Run from the repo root:
    python3 figures/scripts/ch06_charts.py
F6.4 irrelevant context  <- data/ch06_distraction.csv (published values, Shi et al., 2023, Tables 2-3)
F6.12 Medprompt steps    <- data/ch06_medprompt.csv  (published values, Nori et al., 2023, Figure 4)
Numbers are read from the CSVs only; nothing is computed except plotting positions and step differences.
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
    "color": {"ink": "#1D1D1F", "fills": ["#1C3D6E", "#C2410C", "#FCE38A", "#4CAF84", "#EEF2F7"],
              "hatches": [None, None, None, None, None]},
    "gray": {"ink": "#000000", "fills": ["#3A3A3A", "#FFFFFF", "#EDEDED", "#BDBDBD", "#FFFFFF"],
             "hatches": [None, "///", None, None, ".."]},
}


def read(name):
    with open(os.path.join(ROOT, "data", name), encoding="utf8") as fh:
        lines = [ln for ln in fh if not ln.startswith("#")]
    return list(csv.DictReader(lines))


def save(fig, fid, mode):
    out = os.path.join(ROOT, "figures", "out", mode, f"{fid}.svg")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)


def f6_04(mode):
    s = STYLE[mode]
    rows = read("ch06_distraction.csv")
    vals = [float(r["accuracy"]) for r in rows]
    labels = ["Original problems\n(100 base problems)", "Same problems +\none irrelevant sentence",
              "+ instruction to ignore\nirrelevant information"]
    fills = [s["fills"][0], s["fills"][1], s["fills"][2]]
    hatches = [s["hatches"][0], s["hatches"][1], s["hatches"][2]]
    fig, ax = plt.subplots(figsize=(8.6, 4.2))
    x = np.arange(len(rows))
    for xi, v, fc, h in zip(x, vals, fills, hatches):
        ax.bar(xi, v, 0.55, color=fc, edgecolor=s["ink"], linewidth=1.2, hatch=h)
        ax.text(xi, v + 1.5, f"{v:.1f}%", ha="center", va="bottom", fontsize=13, fontweight="bold", color=s["ink"])
    ax.set_xticks(x, labels)
    ax.set_ylim(0, 105)
    ax.set_ylabel("Accuracy (%)")
    ax.set_title("One irrelevant sentence lowered an older model's accuracy\non math word problems (tested 2023)",
                 loc="left", fontweight="bold", fontsize=12.5, pad=12)
    fig.text(0.01, -0.2, "Published values: Shi et al. (2023), Tables 2 and 3. Model code-davinci-002, step-by-step\n"
             "(chain-of-thought) prompting. Middle and right bars: 4,000 problems (GSM-IC-4K), each a base\n"
             "problem with one irrelevant sentence added (from 58,052 built). Hatched bar in print = the distracted condition.",
             fontsize=10, color=s["ink"])
    save(fig, "f6-04-distraction-chart", mode)


def f6_12(mode):
    s = STYLE[mode]
    rows = read("ch06_medprompt.csv")
    vals = [float(r["accuracy"]) for r in rows]
    labels = ["No examples\n(zero-shot)", "+ five random\nsolved\nquestions", "+ reasoning\nGPT-4 wrote\nfor them",
              "Examples\nchosen by\nsimilarity", "+ five\nshuffled\nruns, vote"]
    fig, ax = plt.subplots(figsize=(8.8, 4.6))
    x = np.arange(len(rows))
    fills = [s["fills"][4], s["fills"][2], s["fills"][2], s["fills"][2], s["fills"][3]]
    hatches = [s["hatches"][4], None, None, None, None]
    for i, (xi, v) in enumerate(zip(x, vals)):
        ax.bar(xi, v, 0.6, color=fills[i], edgecolor=s["ink"], linewidth=1.2, hatch=hatches[i])
        ax.text(xi, v + 0.25, f"{v:.1f}%", ha="center", va="bottom", fontsize=12.5, fontweight="bold",
                color=s["ink"])
        if i > 0:
            ax.text(xi, 79.6, f"{v - vals[i - 1]:+.1f}", ha="center", va="bottom", fontsize=11, color=s["ink"])
    ax.set_xticks(x, labels)
    ax.set_ylim(79, 92)
    ax.set_ylabel("MedQA accuracy (%) — axis starts at 79")
    ax.set_title("Medprompt raised GPT-4's MedQA score from 81.7% to 90.2%\nwithout retraining the model (2023)",
                 loc="left", fontweight="bold", fontsize=12.5, pad=12)
    fig.text(0.01, -0.26, "Published values: Nori et al. (2023), Figure 4 (the paper's step-by-step chart; first bar: simple prompt, no examples).\n"
             "Steps are cumulative in the authors' order, which they call subjective; the paper's Figure 6\n"
             "gives slightly different sizes for the last two steps (+0.8, +2.1). Small numbers = change from the bar before.",
             fontsize=10, color=s["ink"])
    save(fig, "f6-12-medprompt-chart", mode)


if __name__ == "__main__":
    for mode in ("color", "gray"):
        f6_04(mode)
        f6_12(mode)
    print("rendered f6-04-distraction-chart, f6-12-medprompt-chart")
