"""Chapter 4 data charts (color + gray SVG). Run from the repo root after ch04_experiments.py:
    python3 figures/scripts/ch04_charts.py
F4.4  computed toy (data/ch04_recombination.csv)
F4.6  published values (data/ch04_multiturn.csv; Laban et al., 2025)
F4.12 computed scoring rules (data/ch04_scoring.csv), Deep 4.A
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
plt.rcParams["font.sans-serif"] = ["Source Sans 3", "STIXGeneral", "DejaVu Sans"]  # no system-font fallback in print (D29)

STYLE = {
    "color": {"main": "#1C3D6E", "accent": "#FCE38A", "risk": "#C2410C", "ink": "#1D1D1F", "hatch": None,
              "risk_hatch": None},
    "gray": {"main": "#3A3A3A", "accent": "#FFFFFF", "risk": "#FFFFFF", "ink": "#000000", "hatch": "///",
             "risk_hatch": "xx"},
}


def read(name):
    with open(os.path.join(ROOT, "data", name), encoding="utf8") as fh:
        return list(csv.DictReader(fh))


def save(fig, fid, mode):
    out = os.path.join(ROOT, "figures", "out", mode, f"{fid}.svg")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)


LABELS = {"word_pair_free": "Word-pair model,\nfree generation",
          "long_context_seen": "Five-word context,\ncity seen in training",
          "long_context_unseen": "Five-word context,\ncity never seen"}


def f4_4(mode):
    s = STYLE[mode]
    rows = read("ch04_recombination.csv")
    first = rows[0]
    fig, ax = plt.subplots(figsize=(8.6, 3.9))
    y = list(range(len(rows)))[::-1]
    for yi, r in zip(y, rows):
        t, f_ = int(r["n_true"]), int(r["n_false"])
        ax.barh(yi, t, color=s["main"], edgecolor=s["ink"], linewidth=1, label="True sentences" if yi == y[0] else None)
        ax.barh(yi, f_, left=t, color=s["risk"], edgecolor=s["ink"], linewidth=1, hatch=s["risk_hatch"],
                label="False sentences" if yi == y[0] else None)
        ax.text(1010, yi, f"{t:,} true · {f_:,} false", va="center", fontsize=11.5, fontweight="bold",
                color=s["ink"])
    ax.set_yticks(y, [LABELS[r["condition"]] for r in rows])
    ax.set_xlim(0, 1450)
    ax.set_xticks([0, 250, 500, 750, 1000])
    ax.set_xlabel("Sentences produced (1,000 per condition)")
    ax.legend(loc="upper center", bbox_to_anchor=(0.45, -0.2), ncol=2, frameon=False)
    ax.set_title(f"A toy model trained only on true sentences still produced false ones "
                 f"({int(first['n_false']):,} of {int(first['n_generated']):,}),\nand always answered about cities it had never seen",
                 loc="left", fontweight="bold", fontsize=12.5, pad=14)
    fig.text(0.01, -0.2, "Toy counting models (word-pair and five-word context), not LLMs. Trained on 12 true sentences \"<city> is the capital of "
             "<country>.\" Book's own computation (seed 4; figures/scripts/ch04_experiments.py).",
             fontsize=9.5, color=s["ink"])
    save(fig, "f4-04-recombination", mode)


def f4_6(mode):
    s = STYLE[mode]
    rows = read("ch04_multiturn.csv")
    fig, ax = plt.subplots(figsize=(7.6, 3.6))
    vals = [float(r["avg_performance_pct"]) for r in rows]
    names = ["Whole task in\none message", "Task revealed piece\nby piece over turns"]
    bars = ax.bar([0, 1], vals, width=0.55, color=[s["main"], s["risk"]], edgecolor=s["ink"], linewidth=1)
    bars[1].set_hatch(s["risk_hatch"])
    for i, v in enumerate(vals):
        ax.text(i, v + 3, f"about {v:.0f}%", ha="center", fontsize=12, fontweight="bold", color=s["ink"])
    ax.set_xticks([0, 1], names)
    ax.set_ylim(0, 110)
    ax.set_yticks([0, 20, 40, 60, 80, 100])
    ax.set_ylabel("Average performance (%)")
    ax.set_title("In the paper's introduction, average scores fell from about 90% to about 65%\nwhen tasks arrived piece by piece (15 models tested in 2025)",
                 loc="left", fontweight="bold", fontsize=12.5, pad=14)
    fig.text(0.01, -0.1, "Published values: Laban et al. (2025), introduction; simulated conversations, 15 models, six tasks. "
             "The abstract reports an average drop of 39%, computed differently.", fontsize=9.5, color=s["ink"])
    save(fig, "f4-06-multiturn", mode)


def f4_12(mode):
    s = STYLE[mode]
    rows = read("ch04_scoring.csv")
    p = [float(r["confidence_p"]) for r in rows]
    a = [float(r["rule_A_answer"]) for r in rows]
    b = [float(r["rule_B_answer"]) for r in rows]
    fig, ax = plt.subplots(figsize=(8.0, 4.0))
    ax.plot(p, a, color=s["main"], linewidth=2.6, label="Rule A: wrong = 0. Answering never scores below abstaining")
    ax.plot(p, b, color=s["ink"], linewidth=2.2, linestyle="--",
            label="Rule B: wrong = −3. Answering pays only above 75% confidence")
    ax.axhline(0, color=s["ink"], linewidth=1.2, linestyle=":")
    ax.text(0.04, -0.28, "\"I don't know\" scores 0 under both rules", fontsize=11, color=s["ink"])
    ax.axvline(0.75, color=s["ink"], linewidth=0.8, linestyle=":")
    ax.set_xlabel("Chance that the answer is right (confidence)")
    ax.set_ylabel("Expected score for answering")
    ax.set_ylim(-3.2, 1.3)
    ax.legend(loc="lower right", frameon=False, fontsize=10.5)
    # Penalty t/(1-t) = 3 at t = 0.75. Kalai et al. (2025, v1, section 4.2) print "penalty 2" for t = 0.75,
    # an arithmetic slip; the book uses the formula's value, 3.
    ax.set_title("When a wrong answer costs nothing, guessing never scores worse than \"I don't know\"",
                 loc="left", fontweight="bold", fontsize=12.5, pad=14)
    fig.text(0.01, -0.08, "Computed illustration (data/ch04_scoring.csv); scoring idea discussed by Kalai et al. (2025).",
             fontsize=9.5, color=s["ink"])
    save(fig, "f4-12-scoring-rules", mode)


if __name__ == "__main__":
    for mode in ("color", "gray"):
        f4_4(mode)
        f4_6(mode)
        f4_12(mode)
    print("rendered f4-04, f4-06, f4-12")
