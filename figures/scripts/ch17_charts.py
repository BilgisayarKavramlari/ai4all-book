"""Chapter 17 data charts (color + gray SVG). Run from the repo root after ch17_experiments.py:
    python3 figures/scripts/ch17_charts.py
This book's simulations (figures/scripts/ch17_experiments.py; constructed data; seeds in data/ch17_experiments_meta.txt):
  F17.8  data/ch17_occlusion.csv, data/ch17_occlusion_summary.csv   (Sam's replica sorter)
  F17.10 data/ch17_fidelity.csv                                      (global surrogate fidelity)
  F17.11 data/ch17_stability.csv                                     (local surrogate top feature across reruns)
Published values:
  F17.13 data/ch17_cot_faithfulness.csv                              (Chen et al., 2025)
Every title is written from the CSV values at run time.
"""
import csv
import os
from collections import Counter

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib import font_manager  # noqa: E402
from matplotlib.patches import Patch, Rectangle  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
for fam in ("Source Sans 3", "Source Sans Pro"):
    if any(fam in f.name for f in font_manager.fontManager.ttflist):
        plt.rcParams["font.family"] = fam
        break
plt.rcParams.update({"font.size": 12, "axes.spines.top": False, "axes.spines.right": False,
                     "svg.fonttype": "none", "svg.hashsalt": "ch17"})

STYLE = {
    "color": {"main": "#1C3D6E", "accent": "#FCE38A", "risk": "#C2410C", "ok": "#4CAF84", "ink": "#1D1D1F",
              "hatch": None, "risk_hatch": None, "muted": "#5C5C66", "cmap": "YlOrBr"},
    "gray": {"main": "#3A3A3A", "accent": "#FFFFFF", "risk": "#FFFFFF", "ok": "#BDBDBD", "ink": "#000000",
             "hatch": "///", "risk_hatch": "xx", "muted": "#444444", "cmap": "Greys"},
}
FEAT = {"income_k": "Income", "debt_ratio": "Debt ratio", "months_employed": "Months at job",
        "late_payments": "Late payments", "age_band": "Age band"}


def read(name):
    with open(os.path.join(ROOT, "data", name), encoding="utf8") as fh:
        return list(csv.DictReader(line for line in fh if not line.startswith("#") and line.strip()))


def save(fig, fid, mode):
    out = os.path.join(ROOT, "figures", "out", mode, f"{fid}.svg")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    fig.savefig(out, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)


def source(fig, text, y=-0.08):
    fig.text(0.01, y, text, fontsize=9.5, color="#1D1D1F")


def summary():
    return {r["model"]: r for r in read("ch17_occlusion_summary.csv")}


# ---------------------------------------------------------------- F17.8 occlusion maps
def f17_8(mode):
    s = STYLE[mode]
    rows = read("ch17_occlusion.csv")
    sm = summary()
    a, b = sm["A_old_photos"], sm["B_mixed_backgrounds"]
    fig, axes = plt.subplots(1, 2, figsize=(8.4, 4.3))
    fig.subplots_adjust(wspace=0.35)
    names = [("A_old_photos", "Old model (dark-desk bolts)"),
             ("B_mixed_backgrounds", "Retrained (mixed backgrounds)")]
    vmax = max(max(0.0, float(r["occlusion_logodds"])) for r in rows)
    for ax, (key, lab) in zip(axes, names):
        grid = np.zeros((12, 12)); part = np.zeros((12, 12), dtype=bool)
        for r in rows:
            if r["model"] == key:
                grid[int(r["row"]), int(r["col"])] = max(0.0, float(r["occlusion_logodds"]))
                part[int(r["row"]), int(r["col"])] = r["is_part_pixel"] == "1"
        ax.imshow(grid, cmap=s["cmap"], vmin=0, vmax=vmax)
        for (i, j), p in np.ndenumerate(part):
            if p:
                ax.add_patch(Rectangle((j - 0.5, i - 0.5), 1, 1, fill=False, edgecolor=s["ink"], linewidth=1.6))
        ax.set_xticks([]); ax.set_yticks([])
        for sp in ax.spines.values():
            sp.set_visible(True)
        r = sm[key]
        ax.set_title(lab + f"\nbackground share of evidence: "
                     f"{float(r['pct_of_positive_exact_contribution_from_background']):.0f}%\n"
                     f"gray-bench bolts sorted right: {float(r['test2_acc_bolt']) * 100:.0f}%",
                     fontsize=10.5, loc="left")
    fig.suptitle(f"Measured against an average-gray pixel, background pixels supplied "
                 f"{float(a['pct_of_positive_exact_contribution_from_background']):.0f}% of the old model's\nevidence "
                 f"for \"bolt\"; after retraining, "
                 f"{float(b['pct_of_positive_exact_contribution_from_background']):.0f}%, and the gray-bench errors "
                 f"were gone", x=0.01, ha="left", fontweight="bold", fontsize=12.5, y=1.08)
    sens = read("ch17_baseline_sensitivity.csv")
    old = [float(r["pct_of_positive_exact_contribution_from_background"]) for r in sens if r["model"] == "A_old_photos"]
    source(fig, "This book's simulation (figures/scripts/ch17_experiments.py; data/ch17_occlusion*.csv): constructed "
           "12 x 12 images, not Sam's real photos. Darker = the pixel pushed harder\ntoward \"bolt\" (one-pixel "
           "occlusion against a fixed average-gray pixel, change in log-odds). Outlined squares = the bolt's pixels. "
           f"For this glass-box model the map\nmatched the exact contributions (correlation "
           f"{float(a['mean_corr_occlusion_vs_exact']):.2f} and {float(b['mean_corr_occlusion_vs_exact']):.2f}). "
           f"Against other baselines the old model's share runs from {min(old):.1f}% to {max(old):.0f}% "
           "(data/ch17_baseline_sensitivity.csv).", y=-0.12)
    save(fig, "f17-08-occlusion", mode)


# ---------------------------------------------------------------- F17.10 fidelity
def f17_10(mode):
    s = STYLE[mode]
    rows = read("ch17_fidelity.csv")
    d = [int(r["tree_depth"]) for r in rows]
    v = [float(r["fidelity_pct_heldout"]) for r in rows]
    fig, ax = plt.subplots(figsize=(7.6, 3.6))
    ax.bar(range(len(d)), v, 0.6, color=s["main"], hatch=s["hatch"], edgecolor=s["ink"], linewidth=1)
    for i, x in enumerate(v):
        ax.text(i, x + 1.5, f"{x:.1f}%", ha="center", fontsize=10.5, color=s["ink"])
    ax.set_xticks(range(len(d)), [f"{k} question{'s' if k > 1 else ''}\n(depth {k})\napprovals\nmatched: "
                                  f"{float(r['pct_of_model_approvals_matched']):.0f}%" for k, r in zip(d, rows)],
                  fontsize=10.5)
    ax.set_ylim(0, 100)
    ax.set_ylabel("Agreement with the model (%)")
    two = v[d.index(2)]
    base = float(rows[0]["always_reject_agreement_pct"])
    ax.axhline(base, color=s["ink"], linewidth=1.2)
    ax.set_xlim(-0.6, len(d) + 0.9)
    ax.text(len(d) - 0.45, base + 3, f"a rule that\nrejects everyone:\n{base:.1f}%", ha="left", va="bottom",
            fontsize=10, color=s["ink"])
    ax.set_title(f"A rule that rejects everyone already agrees with the loan model on {base:.1f}% of new cases;\n"
                 f"a two-question summary reaches {two:.1f}% and matches only half of its approvals",
                 loc="left", fontweight="bold", fontsize=12.5, pad=10)
    source(fig, "This book's simulation (figures/scripts/ch17_experiments.py; data/ch17_fidelity.csv): constructed "
           "applicants; decision trees fitted to the model's own\ndecisions; fidelity = share of 500 held-out "
           "applicants on which tree and model agree. A simulation, not data about any lender.", y=-0.3)
    save(fig, "f17-10-fidelity", mode)


# ---------------------------------------------------------------- F17.11 stability
def f17_11(mode):
    s = STYLE[mode]
    rows = read("ch17_stability.csv")
    sizes = sorted({int(r["n_samples"]) for r in rows})
    feats = ["debt_ratio", "income_k"]
    fig, ax = plt.subplots(figsize=(7.6, 3.6))
    w = 0.36
    styles = [(s["main"], s["hatch"]), (s["accent"], None)]
    for fi, f in enumerate(feats):
        counts = [Counter(r["top1"] for r in rows if int(r["n_samples"]) == n)[f] for n in sizes]
        for i, c in enumerate(counts):
            ax.bar(i + (fi - 0.5) * w, c, w, color=styles[fi][0], hatch=styles[fi][1], edgecolor=s["ink"], linewidth=1)
            ax.text(i + (fi - 0.5) * w, c + 0.2, str(c), ha="center", fontsize=10.5, color=s["ink"])
    ax.set_xticks(range(len(sizes)), [f"{n:,} perturbed samples per run" for n in sizes])
    ax.set_ylim(0, 10.5)
    ax.set_ylabel("Runs (of 10) naming it first")
    ax.legend(handles=[Patch(facecolor=styles[i][0], hatch=styles[i][1], edgecolor=s["ink"], label=FEAT[f])
                       for i, f in enumerate(feats)], frameon=False, loc="upper right", fontsize=10)
    big = [r for r in rows if int(r["n_samples"]) == max(sizes)]
    gap = np.mean([abs(abs(float(r["coef_income_k"])) - abs(float(r["coef_debt_ratio"]))) for r in big])
    ax.set_title("Rerun 10 times, the same explanation method switched its top feature\nat both sample sizes",
                 loc="left", fontweight="bold", fontsize=12.5, pad=10)
    source(fig, "This book's simulation (figures/scripts/ch17_experiments.py; data/ch17_stability.csv): one "
           "constructed applicant; a LIME-style local surrogate, seeds 1704-1713.\nWith 5,000 samples the two "
           f"weights differed by {gap:.3f} on average: a near tie that a ranking hides.", y=-0.12)
    save(fig, "f17-11-stability", mode)


# ---------------------------------------------------------------- F17.13 published CoT faithfulness
def f17_13(mode):
    s = STYLE[mode]
    rows = read("ch17_cot_faithfulness.csv")
    avg = [r for r in rows if r["hint_type"].startswith("average")]
    fig, ax = plt.subplots(figsize=(7.6, 2.8))
    for i, r in enumerate(avg):
        v = float(r["pct_mentioned_hint"])
        ax.barh(i, v, 0.5, color=s["main"] if i == 0 else s["accent"], hatch=s["hatch"] if i == 0 else None,
                edgecolor=s["ink"], linewidth=1)
        ax.text(v + 1.5, i, f"{v:.0f}%", va="center", fontsize=11.5, fontweight="bold", color=s["ink"])
    ax.set_yticks(range(len(avg)), [r["model"] for r in avg])
    ax.invert_yaxis()
    ax.set_xlim(0, 100)
    ax.set_xlabel("Cases in which the reasoning text mentioned the hint the model used (%)")
    lo, hi = min(float(r["pct_mentioned_hint"]) for r in avg), max(float(r["pct_mentioned_hint"]) for r in avg)
    ax.set_title(f"In 2025 tests, two reasoning models mentioned a hint they had used in only {lo:.0f}–{hi:.0f}% "
                 f"of cases", loc="left", fontweight="bold", fontsize=12.5, pad=10)
    source(fig, "Source: Chen et al. (2025), Anthropic research on its own and another provider's model; averages "
           "across hint types; multiple-choice tests with planted hints.\nThe authors call the setting somewhat "
           "contrived. Earlier: Turpin et al. (2023) found explanations that did not mention a bias that changed "
           "the answers.", y=-0.2)
    save(fig, "f17-13-cot-results", mode)


if __name__ == "__main__":
    for mode in ("color", "gray"):
        f17_8(mode)
        f17_10(mode)
        f17_11(mode)
        f17_13(mode)
    print("charts done")
