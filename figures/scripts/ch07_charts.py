"""Chapter 7 data charts (color + gray SVG). Run from the repo root:
    python3 figures/scripts/ch07_charts.py
F7.2  practice vs. exam effects        <- data/ch07_bastani_table1.csv (published values, Bastani et al., 2025, Table 1)
F7.9  first-message types               <- data/ch07_bastani_messages.csv (published values, Bastani et al., 2025, text)
F7.4  reread vs. recall, 5 min / 1 week <- data/ch07_rk2006.csv (published values, Roediger & Karpicke, 2006, Exp. 2)
F7.13 tutoring effect sizes             <- data/ch07_vanlehn2011.csv (published values, VanLehn, 2011)
Numbers are read from the CSVs only; nothing is computed except plotting positions.
"""
import csv
import os
import textwrap

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
    "color": {"ink": "#1D1D1F", "muted": "#5C5C66",
              "fills": ["#1C3D6E", "#FCE38A", "#4CAF84", "#EEF2F7"], "hatches": [None, None, None, None]},
    "gray": {"ink": "#000000", "muted": "#444444",
             "fills": ["#3A3A3A", "#FFFFFF", "#BDBDBD", "#FFFFFF"], "hatches": [None, "///", None, ".."]},
}


def read(name):
    with open(os.path.join(ROOT, "data", name), encoding="utf8") as fh:
        lines = [ln for ln in fh if not ln.startswith("#")]
    return list(csv.DictReader(lines))


def save(fig, fid, mode):
    out = os.path.join(ROOT, "figures", "out", mode, f"{fid}.svg")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    fig.savefig(out, bbox_inches="tight")
    if os.environ.get("PREVIEW"):  # optional PNG previews for visual checks (scratch only)
        prev = os.path.join(ROOT, "build", "ch07", "png", f"{fid}-{mode}.png")
        os.makedirs(os.path.dirname(prev), exist_ok=True)
        fig.savefig(prev, bbox_inches="tight", dpi=80)
    plt.close(fig)


def wrapped(text, width=95):
    return "\n".join(textwrap.wrap(text, width))


def f7_02(mode):
    s = STYLE[mode]
    rows = read("ch07_bastani_table1.csv")
    get = {(r["arm"], r["phase"]): r for r in rows}
    arms = [("GPT Base", 0), ("GPT Tutor", 1)]
    phases = [("practice", "Practice, with the tool"), ("exam", "Exam right after, without any tool")]
    fig, ax = plt.subplots(figsize=(8.6, 4.6))
    x = np.arange(len(phases))
    w = 0.32
    for arm, k in arms:
        vals = [float(get[(arm, p)]["points"]) for p, _ in phases]
        ses = [float(get[(arm, p)]["se"]) * 100 for p, _ in phases]
        xs = x + (k - 0.5) * w
        ax.bar(xs, vals, w, color=s["fills"][k], edgecolor=s["ink"], linewidth=1, hatch=s["hatches"][k],
               label=arm)
        ax.errorbar(xs, vals, yerr=ses, fmt="none", ecolor=s["ink"], elinewidth=1, capsize=3)
        for xi, p, v, se in zip(xs, [p for p, _ in phases], vals, ses):
            r = get[(arm, p)]
            rel = int(r["relative_pct"])
            sig = "" if r["significance"] != "ns" else ", not significant"
            lab = f"{v:+.1f} pts\n({rel:+d}%{sig})"
            y = v + se + 1.2 if v >= 0 else v - se - 1.2
            ax.text(xi, y, lab, ha="center", va="bottom" if v >= 0 else "top", fontsize=10.5, color=s["ink"])
    ax.axhline(0, color=s["ink"], linewidth=1.2)
    ax.set_xticks(x, [lab for _, lab in phases])
    ax.set_ylabel("Difference from the control group\n(points on a 100-point normalized grade)")
    ax.set_ylim(-16, 46)
    ax.legend(loc="upper right", frameon=False, fontsize=11)
    ax.set_title(wrapped("With unrestricted GPT-4 access, practice scores rose, but exam scores were 17% lower than "
                 "the control group's", 80), loc="left", fontweight="bold", fontsize=12.5, pad=12)
    fig.text(0.01, -0.07, wrapped("Published values: Bastani et al. (2025), Table 1. Control means: practice 28.4, exam 32.1 points; "
             "lines = 1 standard error. Percent = change relative to the control mean.", 110), fontsize=10, color=s["ink"])
    save(fig, "f7-02-bastani-results", mode)


def f7_09(mode):
    s = STYLE[mode]
    rows = read("ch07_bastani_messages.csv")
    measures = list(dict.fromkeys(r["measure"] for r in rows))
    get = {(r["measure"], r["arm"]): float(r["pct"]) for r in rows}
    fig, ax = plt.subplots(figsize=(8.6, 3.6))
    y = np.arange(len(measures))[::-1]
    h = 0.34
    for k, arm in enumerate(["GPT Base", "GPT Tutor"]):
        vals = [get[(m, arm)] for m in measures]
        ys = y + (0.5 - k) * h
        ax.barh(ys, vals, h, color=s["fills"][k], edgecolor=s["ink"], linewidth=1, hatch=s["hatches"][k], label=arm)
        for yi, v in zip(ys, vals):
            ax.text(v + 1.2, yi, f"{v:.0f}%", va="center", fontsize=11.5, color=s["ink"], fontweight="bold")
    ax.set_yticks(y, [m.replace(" (session 1)", "\n(session 1)") for m in measures])
    ax.set_xlim(0, 100)
    ax.set_xlabel("Share that repeated the question or asked for the answer (%)")
    ax.legend(loc="lower right", frameon=False, fontsize=11)
    ax.set_title(wrapped("Students with the unrestricted tool asked for answers more often than tutor users", 95),
                 loc="left", fontweight="bold", fontsize=12.5, pad=12)
    fig.text(0.01, -0.12, wrapped("Published values: Bastani et al. (2025), section \"Student Engagement.\" GPT Tutor also offered "
             "suggested prompts, which the authors note may explain part of the first-message gap.", 110), fontsize=10,
             color=s["ink"])
    save(fig, "f7-09-message-types", mode)


def f7_04(mode):
    s = STYLE[mode]
    rows = read("ch07_rk2006.csv")
    labels = [r["label"] for r in rows]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.4, 4.4), gridspec_kw={"width_ratios": [1.7, 1]})
    x = np.arange(2)
    w = 0.26
    for k, r in enumerate(rows):
        vals = [float(r["recall_5min_pct"]), float(r["recall_1week_pct"])]
        xs = x + (k - 1) * w
        ax1.bar(xs, vals, w, color=s["fills"][k], edgecolor=s["ink"], linewidth=1, hatch=s["hatches"][k],
                label=labels[k])
        for xi, v in zip(xs, vals):
            ax1.text(xi, v + 1.5, f"{v:.0f}%", ha="center", va="bottom", fontsize=10.5, color=s["ink"])
    ax1.set_xticks(x, ["Final test after 5 minutes", "Final test after 1 week"])
    ax1.set_ylabel("Share of the passage recalled (%)")
    ax1.set_ylim(0, 128)
    ax1.set_yticks([0, 20, 40, 60, 80, 100])
    ax1.legend(loc="upper left", frameon=False, fontsize=9.5)
    ax1.set_title("Recall", loc="left", fontsize=12)
    preds = [float(r["predicted_rating"]) for r in rows]
    yy = np.arange(len(rows))[::-1]
    for yi, v, k in zip(yy, preds, range(3)):  # the rating scale starts at 1, so bars start at 1
        ax2.barh(yi, v - 1, 0.55, left=1, color=s["fills"][k], edgecolor=s["ink"], linewidth=1,
                 hatch=s["hatches"][k])
    for yi, v in zip(yy, preds):
        ax2.text(v + 0.1, yi, f"{v:.1f}", va="center", fontsize=10.5, color=s["ink"])
    ax2.set_yticks(yy, ["4 study periods", "3 study + 1 recall", "1 study + 3 recalls"])
    ax2.set_xlim(1, 7)
    ax2.set_xlabel("Predicted recall in a week\n(1 = not well, 7 = very well)")
    ax2.set_title("How well they expected to remember", loc="left", fontsize=12)
    fig.suptitle("Rereading won after 5 minutes; testing yourself won after a week", x=0.01, ha="left",
                 fontweight="bold", fontsize=12.5)
    fig.text(0.01, -0.08, wrapped("Published values: Roediger & Karpicke (2006), Experiment 2, 180 students (30 per group); "
             "recall tests without feedback; study periods were 5 minutes each. Restudiers predicted the best recall.", 110), fontsize=10, color=s["ink"])
    fig.tight_layout()
    save(fig, "f7-04-retrieval-rk2006", mode)


def f7_13(mode):
    s = STYLE[mode]
    rows = read("ch07_vanlehn2011.csv")
    fig, ax = plt.subplots(figsize=(8.6, 3.6))
    y = np.arange(len(rows))
    vals = [float(r["d"]) for r in rows]
    fills = [s["fills"][1], s["fills"][1], s["fills"][1], s["fills"][0]]
    hatches = [s["hatches"][1]] * 3 + [None]
    for yi, v, fc, ht in zip(y, vals, fills, hatches):
        ax.barh(yi, v, 0.55, color=fc, edgecolor=s["ink"], linewidth=1, hatch=ht)
    for yi, r, v in zip(y, rows, vals):
        ax.text(v + 0.015, yi, f"d = {v:.2f}  ({r['n']} comparisons)", va="center", fontsize=11, color=s["ink"])
    ax.set_yticks(y, [r["label"] for r in rows])
    ax.set_xlim(0, 1.15)
    ax.set_xlabel("Average effect size versus no tutoring (standard deviations)")
    ax.set_title(wrapped("In one review, step-based computer tutors came close to human tutors", 80), loc="left",
                 fontweight="bold", fontsize=12.5, pad=12)
    fig.text(0.01, -0.12, wrapped("Published values: VanLehn (2011). Computer tutors built before generative AI; feedback on final "
             "answers (answer-based), on each step, or on parts of steps (substep).", 110), fontsize=10, color=s["ink"])
    save(fig, "f7-13-vanlehn", mode)


if __name__ == "__main__":
    for mode in ("color", "gray"):
        f7_02(mode)
        f7_09(mode)
        f7_04(mode)
        f7_13(mode)
    print("rendered f7-02-bastani-results, f7-09-message-types, f7-04-retrieval-rk2006, f7-13-vanlehn")
