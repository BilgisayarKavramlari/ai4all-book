"""Chapter 14 data charts (color + gray SVG). Run from the repo root, after ch14_experiments.py:
    python3 figures/scripts/ch14_charts.py
F14.6  this book's calculation: chance of an error-free run vs. steps (data/ch14_compounding.csv)
F14.8  this book's simulation: wrong final actions, rework and person checks (data/ch14_gates_sim.csv)
Both are this book's own calculation and simulation, not data about any real agent; assumptions in data/ch14_experiments_meta.txt.
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
                     "svg.fonttype": "none", "svg.hashsalt": "ch14"})

STYLE = {
    "color": {"main": "#1C3D6E", "accent": "#FCE38A", "risk": "#C2410C", "ink": "#1D1D1F", "verified": "#4CAF84",
              "muted": "#5C5C66", "hatch": None, "risk_hatch": None},
    "gray": {"main": "#3A3A3A", "accent": "#EDEDED", "risk": "#FFFFFF", "ink": "#000000", "verified": "#BDBDBD",
             "muted": "#444444", "hatch": "///", "risk_hatch": "xx"},
}


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


def f14_6(mode):
    s = STYLE[mode]
    rows = read("ch14_compounding.csv")
    fig, ax = plt.subplots(figsize=(8.0, 4.2))
    styles = {"0.99": ("o", "99% per step"), "0.95": ("s", "95% per step"), "0.9": ("^", "90% per step")}
    for p, (mk, lab) in styles.items():
        pts = [r for r in rows if r["p_step"] == p]
        xs = [int(r["steps"]) for r in pts]
        ys = [100 * float(r["p_all_correct"]) for r in pts]
        ax.plot(xs, ys, linestyle="-", marker=mk, markevery=3, markersize=7,
                color=s["main"] if p != "0.95" else s["ink"], markerfacecolor="white" if p == "0.9" else None,
                linewidth=2.0)
        ax.text(xs[-1] + 0.4, ys[-1], lab, va="center", ha="left", fontsize=11, fontweight="bold", color=s["ink"])
    for p, n in (("0.95", 20), ("0.99", 20), ("0.9", 10)):
        r = next(r for r in rows if r["p_step"] == p and int(r["steps"]) == n)
        v = 100 * float(r["p_all_correct"])
        ax.annotate(f"{v:.0f}% at {n} steps", (n, v), xytext=(8, -18 if p == "0.99" else 8),
                    textcoords="offset points", fontsize=11.5, fontweight="bold", color=s["ink"])
    ax.set_xlim(1, 37)
    ax.set_xticks([1, 5, 10, 15, 20, 25, 30])
    ax.set_ylim(0, 105)
    ax.set_xlabel("Number of steps in a run")
    ax.set_ylabel("Runs with no error at all (%)")
    ax.set_title("In this book's calculation, at 95% per step only about a third of 20-step runs have no error",
                 loc="left", fontweight="bold", fontsize=12.5, pad=10)
    fig.text(0.01, -0.1, "Computed by this book (figures/scripts/ch14_experiments.py): chance of no error = p × p × … "
             "= p^n, assuming every step goes right\nwith the same chance, independently. A calculation, not data about any "
             "agent: real errors can be correlated (worse) or harmless and fixed (better).", fontsize=9.5,
             color=s["ink"])
    save(fig, "f14-06-compounding", mode)


def f14_8(mode):
    s = STYLE[mode]
    rows = read("ch14_gates_sim.csv")
    order = [("A", "n/a", "No\nperson"), ("B", "0.8", "One gate\nbefore the\nfinal action"),
             ("C", "0.8", "Checks every\n5 steps\n+ the gate")]
    low = {("B", "0.5"), ("C", "0.5")}
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(8.6, 4.2), gridspec_kw={"width_ratios": [1.25, 1]})
    for i, (d, c, lab) in enumerate(order):
        r = next(r for r in rows if r["design"] == d and r["catch_rate"] == c)
        v = float(r["pct_harm"])
        a1.bar(i, v, 0.6, color=s["risk"], edgecolor=s["ink"], linewidth=1.2, hatch=s["risk_hatch"])
        a1.text(i, v + 2, f"{v:.0f}%", ha="center", fontsize=12.5, fontweight="bold", color=s["ink"])
        for dd, cc in low:
            if dd == d:
                r5 = next(r for r in rows if r["design"] == dd and r["catch_rate"] == "0.5")
                v5 = float(r5["pct_harm"])
                a1.plot(i, v5, marker="o", markersize=9, markerfacecolor="white", markeredgecolor=s["ink"],
                        markeredgewidth=1.6)
                a1.text(i + 0.2, v5, f"{v5:.0f}% if half\nthe errors are caught", fontsize=9.5, va="center",
                        color=s["ink"])
    a1.set_xticks(range(3), [o[2] for o in order], fontsize=10.5)
    a1.set_ylim(0, 80)
    a1.set_ylabel("Runs ending in the final action\non a wrong result (%)")
    a1.set_title("Wrong final actions", loc="left", fontweight="bold", fontsize=12)
    labels = ["One gate", "Checks + gate"]
    redo = []
    checks = []
    for d in ("B", "C"):
        r = next(r for r in rows if r["design"] == d and r["catch_rate"] == "0.8")
        redo.append(float(r["mean_steps_redone"]))
        checks.append(float(r["mean_person_checks"]))
    w = 0.36
    for i in range(2):
        a2.bar(i - w / 2, redo[i], w, color=s["accent"], edgecolor=s["ink"], linewidth=1.2,
               hatch="..." if mode == "gray" else None, label="Steps redone" if i == 0 else None)
        a2.bar(i + w / 2, checks[i], w, color=s["main"], edgecolor=s["ink"], linewidth=1.2, hatch=s["hatch"],
               label="Checks by a person" if i == 0 else None)
        a2.text(i - w / 2, redo[i] + 0.2, f"{redo[i]:.1f}", ha="center", fontsize=11.5, fontweight="bold",
                color=s["ink"])
        a2.text(i + w / 2, checks[i] + 0.2, f"{checks[i]:.1f}", ha="center", fontsize=11.5, fontweight="bold",
                color=s["ink"])
    a2.set_xticks(range(2), labels)
    a2.set_ylim(0, 10.5)
    a2.set_ylabel("Average per run")
    a2.legend(frameon=False, loc="upper right", fontsize=10)
    a2.set_title("The cost: rework and checks", loc="left", fontweight="bold", fontsize=12)
    fig.suptitle("In this book's simulation, check points between steps cut wrong final actions and rework, "
                 "at the cost of more of a person's time", x=0.01, ha="left", fontweight="bold", fontsize=12, y=1.04)
    fig.text(0.01, -0.13, "Simulated by this book (figures/scripts/ch14_experiments.py): 20 steps, 95% per step, a "
             "person catching a wrong result 80% of the time (open markers: 50%);\n10 seeds × 20,000 runs. Assumes "
             "independent steps and misses, no false alarms, no approval fatigue, only the final action "
             "irreversible. Not data about any agent.", fontsize=9.5, color=s["ink"])
    fig.tight_layout()
    save(fig, "f14-08-gates-sim", mode)


if __name__ == "__main__":
    for mode in ("color", "gray"):
        f14_6(mode)
        f14_8(mode)
    print("rendered f14-06-compounding, f14-08-gates-sim")
