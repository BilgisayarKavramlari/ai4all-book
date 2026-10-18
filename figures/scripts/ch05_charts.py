"""Chapter 5 data charts (color + gray SVG). Run from the repo root:
    python3 figures/scripts/ch05_charts.py
F5.10 wording and scoring standard <- data/ch05_wording.csv (published values, Meincke et al., 2025a, Suppl. Table 2)
F5.14 automation patterns by traffic <- data/ch05_delegation.csv (published values, Appel et al., 2025)
Numbers are read from the CSVs only; nothing is computed except plotting positions.
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
    "color": {"main": "#1C3D6E", "accent": "#FCE38A", "ink": "#1D1D1F", "muted": "#8A94A3",
              "fills": ["#1C3D6E", "#FCE38A", "#4CAF84", "#EEF2F7"], "hatches": [None, None, None, None]},
    "gray": {"main": "#3A3A3A", "accent": "#FFFFFF", "ink": "#000000", "muted": "#7A7A7A",
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
    plt.close(fig)


PROMPTS = [("formatted", "Reference wording\n(with format line)"), ("unformatted", "Format line\nremoved"),
           ("order", "\"I order you\nto answer…\""), ("please", "\"Please\nanswer…\"")]
STANDARDS = [("all100", "Correct in all 100 of 100 runs"), ("majority", "Correct in most runs (51 or more)")]


def f5_10(mode):
    s = STYLE[mode]
    rows = [r for r in read("ch05_wording.csv") if r["model"] == "GPT-4o"]
    get = {(r["prompt"], r["standard"]): r for r in rows}
    fig, ax = plt.subplots(figsize=(8.6, 4.8))
    x = np.arange(len(STANDARDS))
    w = 0.19
    for k, (p, lab) in enumerate(PROMPTS):
        vals = [float(get[(p, st)]["pp_above_random"]) for st, _ in STANDARDS]
        lo = [float(get[(p, st)]["ci_low"]) for st, _ in STANDARDS]
        hi = [float(get[(p, st)]["ci_high"]) for st, _ in STANDARDS]
        xs = x + (k - 1.5) * w
        err = [np.array(vals) - np.array(lo), np.array(hi) - np.array(vals)]
        ax.bar(xs, vals, w, color=s["fills"][k], edgecolor=s["ink"], linewidth=1, hatch=s["hatches"][k],
               label=lab.replace("\n", " "))
        ax.errorbar(xs, vals, yerr=err, fmt="none", ecolor=s["ink"], elinewidth=1, capsize=3)
        for xi, v, h in zip(xs, vals, hi):
            ax.text(xi, h + 0.8, f"{v:+.1f}", ha="center", va="bottom", fontsize=10.5, color=s["ink"])
    ax.axhline(0, color=s["ink"], linewidth=1.2)
    ax.set_xticks(x, [lab for _, lab in STANDARDS])
    ax.set_ylabel("Points above random guessing (0 = 25%)\nbars: estimate · lines: 95% interval")
    ax.set_ylim(-14, 36)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), frameon=False, fontsize=10.5, ncol=4)
    ax.set_title("How strictly answers were scored mattered more than \"please\" or \"I order you\" (GPT-4o, 2025)",
                 loc="left", fontweight="bold", fontsize=12.5, pad=12)
    fig.text(0.01, -0.13, "Published values: Meincke et al. (2025a), Supplementary Table 2. 198 GPQA Diamond questions, "
             "each asked 100 times per prompt at temperature 0; model gpt-4o-2024-08-06.", fontsize=10, color=s["ink"])
    save(fig, "f5-10-wording-chart", mode)


def f5_14(mode):
    s = STYLE[mode]
    rows = read("ch05_delegation.csv")
    names = ["Chat conversations\n(Claude.ai)", "Business software traffic\n(first-party API)"]
    vals = [float(r["automation_pct"]) for r in rows]
    fig, ax = plt.subplots(figsize=(8.6, 3.2))
    y = np.arange(len(rows))[::-1]
    ax.barh(y, vals, 0.5, color=[s["fills"][0], s["fills"][1]], edgecolor=s["ink"], linewidth=1,
            hatch=[None, s["hatches"][1]] if mode == "gray" else None)
    for yi, v in zip(y, vals):
        ax.text(v + 1.5, yi, f"{v:.0f}%", va="center", fontsize=12, color=s["ink"], fontweight="bold")
    ax.set_yticks(y, names)
    ax.set_xlim(0, 100)
    ax.set_xlabel("Share of conversations or transcripts showing automation patterns (%)")
    ax.set_title("In one provider's August 2025 data, automation patterns were far more common in business API "
                 "traffic than in chat", loc="left", fontweight="bold", fontsize=12.5, pad=12)
    fig.text(0.01, -0.16, "Published values: Appel et al. (2025), Anthropic Economic Index, September 2025 report; same "
             "month and classifier (Claude Sonnet 4). The provider's own definitions, not the AI Fluency modalities.",
             fontsize=10, color=s["ink"])
    save(fig, "f5-14-delegation-data", mode)


if __name__ == "__main__":
    for mode in ("color", "gray"):
        f5_10(mode)
        f5_14(mode)
    print("rendered f5-10-wording-chart, f5-14-delegation-data")
