"""Chapter 23 data charts (color + gray SVG). Run from the repo root:
    python3 figures/scripts/ch23_charts.py
Published values only (no simulations):
  f23-07  data/ch23_turing_2026.csv      (Jones & Bergen, 2026, PNAS)
  f23-10  data/ch23_colombatto_2024.csv  (Colombatto & Fleming, 2024)
  f23-16  data/ch23_doshi_hauser.csv     (Doshi & Hauser, 2024)
Titles state findings; every number in a title is read from the CSV at run time.
Meaning never by color alone: bars carry hatching in gray, value labels, and direct labels.
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
                     "svg.fonttype": "none", "svg.hashsalt": "ch23"})

STYLE = {
    "color": {"main": "#1C3D6E", "second": "#FCE38A", "base": "#EEF2F7", "ink": "#1D1D1F", "muted": "#5C5C66",
              "h_main": None, "h_second": None, "h_base": None},
    "gray": {"main": "#3A3A3A", "second": "#FFFFFF", "base": "#DDDDDD", "ink": "#000000", "muted": "#444444",
             "h_main": None, "h_second": "///", "h_base": ".."},
}


def read(name):
    with open(os.path.join(ROOT, "data", name), encoding="utf8") as fh:
        return list(csv.DictReader(line for line in fh if not line.startswith("#") and line.strip()))


def save(fig, fid, mode):
    out = os.path.join(ROOT, "figures", "out", mode, f"{fid}.svg")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    fig.savefig(out, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)


def source(fig, text, y=-0.06):
    fig.text(0.01, y, text, fontsize=10, color="#1D1D1F", wrap=True)


def f23_07(mode):
    s = STYLE[mode]
    rows = read("ch23_turing_2026.csv")
    pct = {(r["system"], r["prompt"]): int(r["judged_human_pct"]) for r in rows}
    top = pct[("GPT-4.5", "persona prompt")]
    lo = sorted(v for (sy, p), v in pct.items() if p == "no persona prompt")
    title = (f"With a persona prompt, one model was judged human {top}% of the time; "
             f"without it, {lo[0]}–{lo[-1]}%")
    fig, ax = plt.subplots(figsize=(8.8, 4.4))
    labels, vals, kinds = [], [], []
    for r in rows:
        short = {"persona prompt": "persona", "no persona prompt": "no persona", "baseline": "baseline"}[r["prompt"]]
        labels.append(f"{r['system'].replace('-405B', '')}\n{short}")
        vals.append(int(r["judged_human_pct"]))
        kinds.append(r["prompt"])
    for i, (v, k) in enumerate(zip(vals, kinds)):
        key = {"persona prompt": "main", "no persona prompt": "second", "baseline": "base"}[k]
        ax.bar(i, v, color=s[key], edgecolor=s["ink"], hatch=s["h_" + key], linewidth=1.0, width=0.66)
        ax.text(i, v + 1.5, f"{v}%", ha="center", va="bottom", fontsize=12, color=s["ink"], fontweight="bold")
    ax.axhline(50, color=s["ink"], linewidth=1.2)
    ax.text(len(vals) - 0.5, 51.5, "50%: chosen as often as the real human", ha="right", va="bottom",
            fontsize=10.5, color=s["ink"])
    ax.set_xticks(range(len(vals)))
    ax.set_xticklabels(labels, fontsize=10.5)
    ax.set_ylabel("Games in which the system was judged human (%)")
    ax.set_ylim(0, 85)
    ax.set_title(title, fontsize=13, fontweight="bold", loc="left")
    source(fig, "Source: Jones & Bergen (2026), PNAS 123(21), abstract. Five-minute, three-party games; two "
                "preregistered studies. Bars are published values, not this book's calculation.")
    save(fig, "f23-07-turing-2026", mode)


def f23_10(mode):
    s = STYLE[mode]
    rows = read("ch23_colombatto_2024.csv")
    some = next(int(r["pct"]) for r in rows if r["answer"].startswith("Some"))
    title = f"{some}% of 300 U.S. adults surveyed in 2023 gave ChatGPT some chance of being conscious"
    fig, ax = plt.subplots(figsize=(8.4, 2.6))
    left = 0
    for r, key in zip(rows, ("base", "main")):
        v = int(r["pct"])
        ax.barh(0, v, left=left, color=s[key], edgecolor=s["ink"], hatch=s["h_" + key], height=0.5)
        tc = "#FFFFFF" if key == "main" else s["ink"]
        short = "Definitely not" if r["answer"].startswith("Definitely") else "Some possibility"
        ax.text(left + v / 2, 0, f"{short}\n{v}%", ha="center", va="center", fontsize=12, color=s["ink"],
                fontweight="bold", bbox=dict(boxstyle="round,pad=0.25", facecolor="#FFFFFF", edgecolor="none"))
        left += v
    ax.set_xlim(0, 100)
    ax.set_yticks([])
    ax.set_xlabel("Share of participants (%)")
    ax.spines["left"].set_visible(False)
    ax.set_title(title, fontsize=13, fontweight="bold", loc="left")
    source(fig, "Source: Colombatto & Fleming (2024), Neuroscience of Consciousness, niae013 (July 2023 survey, "
                "Prolific sample). A measure of public belief, not evidence about ChatGPT.", y=-0.24)
    save(fig, "f23-10-colombatto-2024", mode)


def f23_16(mode):
    s = STYLE[mode]
    rows = read("ch23_doshi_hauser.csv")
    v = {(r["condition"], r["measure"].split(" ")[0]): float(r["change_pct"]) for r in rows}
    title = ("Model ideas raised rated novelty and usefulness and made stories more alike")
    fig, ax = plt.subplots(figsize=(8.4, 4.2))
    groups = ["Novelty", "Usefulness", "Similarity"]
    conds = [("One AI idea", "second"), ("Five AI ideas", "main")]
    for gi, g in enumerate(groups):
        for ci, (c, key) in enumerate(conds):
            x = gi * 3 + ci
            val = v[(c, g)]
            ax.bar(x, val, color=s[key], edgecolor=s["ink"], hatch=s["h_" + key], width=0.9)
            ax.text(x, val + 0.2, f"+{val:.1f}%", ha="center", va="bottom", fontsize=11.5, fontweight="bold",
                    color=s["ink"])
    ax.set_xticks([0.5, 3.5, 6.5])
    ax.set_xticklabels(["Novelty\n(rated, vs. no AI)", "Usefulness\n(rated, vs. no AI)",
                        "Similarity to other stories\n(share of the no-AI range)"], fontsize=10.5)
    ax.set_ylabel("Increase (%)")
    ax.set_ylim(0, 13)
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(facecolor=s[k], edgecolor=s["ink"], hatch=s["h_" + k], label=c) for c, k in conds],
              frameon=False, loc="upper left")
    ax.set_title(title, fontsize=13, fontweight="bold", loc="left")
    source(fig, "Source: Doshi & Hauser (2024), Science Advances 10, eadn5290; 293 writers, 600 evaluators. "
                "Higher similarity = less collective variety. Published values.")
    save(fig, "f23-16-doshi-hauser", mode)


if __name__ == "__main__":
    for mode in ("color", "gray"):
        f23_07(mode)
        f23_10(mode)
        f23_16(mode)
    print("rendered f23-07, f23-10, f23-16")
