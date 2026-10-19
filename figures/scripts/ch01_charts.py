"""Chapter 1 data charts from data/*.csv (color + gray SVG). Run from the repo root:
    python3 figures/scripts/ch01_charts.py
Only published figures are plotted; see the source column of each CSV.
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
    "color": {"main": "#1C3D6E", "accent": "#4CAF84", "risk": "#C2410C", "ink": "#1D1D1F", "hatch": None},
    "gray": {"main": "#3A3A3A", "accent": "#BDBDBD", "risk": "#FFFFFF", "ink": "#000000", "hatch": "///"},
}


def read(name):
    with open(os.path.join(ROOT, "data", name), encoding="utf8") as fh:
        return list(csv.DictReader(fh))


def save(fig, fid, mode):
    out = os.path.join(ROOT, "figures", "out", mode, f"{fid}.svg")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)


def f1_5(mode):
    s = STYLE[mode]
    rows = read("ch01_support_agents.csv")
    labels = [r["group"] for r in rows]
    vals = [float(r["gain_pct"]) if r["gain_pct"] else None for r in rows]
    fig, ax = plt.subplots(figsize=(8, 3.6))
    y = range(len(rows))
    for i, v in enumerate(vals):
        if v is None:
            ax.text(0.8, i, rows[i]["note"], va="center", ha="left", color=s["ink"], fontsize=11, style="italic",
                    wrap=True)
        else:
            ax.barh(i, v, color=s["main"] if i == 1 else s["accent"], edgecolor=s["ink"], linewidth=1)
            ax.text(v + 0.6, i, f"+{v:g}%", va="center", color=s["ink"], fontsize=12, fontweight="bold")
    ax.set_yticks(list(y), labels)
    ax.set_ylim(len(rows) - 0.4, -0.6)
    ax.set_xlim(0, 40)
    ax.set_xlabel("Change in issues resolved per hour with the AI assistant (%)")
    ax.set_title("Less experienced agents gained the most from the AI assistant", loc="left", fontweight="bold")
    fig.text(0.01, -0.06, "Source: Brynjolfsson, Li & Raymond (2025), Quarterly Journal of Economics, 5,172 agents.",
             fontsize=9.5, color=s["ink"])
    save(fig, "f1-05-support-gains", mode)


def f1_6(mode):
    s = STYLE[mode]
    rows = read("ch01_consultants.csv")
    inside = [r for r in rows if r["panel"] == "inside"]
    outside = [r for r in rows if r["panel"] == "outside"]
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(9, 3.6), gridspec_kw={"width_ratios": [3, 1.3]})
    for i, r in enumerate(inside):
        v = float(r["value"])
        a1.bar(i, v, color=s["accent"], edgecolor=s["ink"])
        a1.text(i, v + 1.2, r["label_value"], ha="center", fontweight="bold", color=s["ink"])
    a1.set_xticks(range(len(inside)), [r["measure"].replace(" ", "\n", 1) for r in inside])
    a1.set_ylim(0, 50)
    a1.set_ylabel("Change vs. control (%)")
    a1.set_title("Inside the frontier (18 tasks, 385 consultants)", loc="left", fontsize=12)
    v = float(outside[0]["value"])
    a2.bar(0, v, color=s["risk"], edgecolor=s["ink"], hatch=s["hatch"], linewidth=1.2)
    a2.text(0, v - 2.5, outside[0]["label_value"], ha="center", va="top", fontweight="bold", color=s["ink"])
    a2.axhline(0, color=s["ink"], linewidth=1)
    a2.set_xticks([0], [outside[0]["measure"]])
    a2.set_ylim(-25, 5)
    a2.set_ylabel("Percentage points")
    a2.set_title("Outside the frontier (1 task, 373)", loc="left", fontsize=12)
    fig.suptitle("Inside the frontier AI help raised quality; outside it, correct answers fell",
                 x=0.01, ha="left", fontweight="bold")
    fig.text(0.01, -0.06, "Source: Dell'Acqua et al. (2023), HBS Working Paper 24-013, 758 BCG consultants. "
             "Quality as rated by human graders ('more than 40%'). Outside: about 84% correct without AI vs. about 60–70% with AI.", fontsize=9.5, color=s["ink"])
    fig.tight_layout()
    save(fig, "f1-06-frontier-results", mode)


if __name__ == "__main__":
    for mode in ("color", "gray"):
        f1_5(mode)
        f1_6(mode)
    print("charts rendered")
