"""Chapter 9 data charts (color + gray SVG). Run from the repo root:
    python3 figures/scripts/ch09_charts.py
F9.9   published values (data/ch09_peters2025.csv; Peters & Chin-Yee, 2025, Table 2)
F9.12  published values (data/ch09_tow2025.csv; Jazwinska & Chandrasekar, 2025)
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
                     "svg.fonttype": "none", "svg.hashsalt": "ch09"})
plt.rcParams["font.sans-serif"] = ["Source Sans 3", "STIXGeneral", "DejaVu Sans"]  # no system-font fallback in print (D29)

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
    fig.savefig(out, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)


def f9_9(mode):
    s = STYLE[mode]
    rows = read("ch09_peters2025.csv")
    ref = next(r for r in rows if r["model"] == "Original abstracts")
    models = [r for r in rows if r is not ref]
    models.sort(key=lambda r: float(r["pct_generalized"]))
    base = float(ref["pct_generalized"])
    fig, ax = plt.subplots(figsize=(8.0, 4.9))
    ys = range(len(models))
    for y, r in zip(ys, models):
        v = float(r["pct_generalized"])
        over = v > base
        ax.barh(y, v, color=s["risk"] if over else s["main"], edgecolor=s["ink"], linewidth=1,
                hatch=s["risk_hatch"] if over else s["hatch"], height=0.62)
        ax.text(v + 1.2, y, f"{v:.0f}%", va="center", fontsize=11.5, fontweight="bold", color=s["ink"])
    ax.axvline(base, color=s["ink"], linestyle="--", linewidth=1.6)
    ax.set_ylim(-1.3, len(models) - 0.5)
    ax.text(base + 1, -1.0, f"original abstracts: {base:.0f}%", fontsize=11, color=s["ink"],
            ha="left", va="center")
    ax.set_yticks(list(ys), [r["model"] for r in models])
    ax.set_xlim(0, 100)
    ax.set_xlabel("Summaries containing generalized conclusions (%)")
    ax.set_title("In a 2025 test, most models produced generalized conclusions\n"
                 "more often than the abstracts did", loc="left", fontweight="bold", fontsize=12.5, pad=10)
    fig.text(0.01, -0.07, "Source: Peters & Chin-Yee (2025), Royal Society Open Science, Table 2: summaries of 100 "
             "medical abstracts with a simple prompt.\nDashed line = share of the original abstracts with generalized "
             "conclusions. The authors found no significant difference\nfrom the originals for the Claude models. Results for these models and this prompt; newer tools differ.", fontsize=9.5,
             color=s["ink"])
    save(fig, "f9-09-peters-summaries", mode)


def f9_12(mode):
    s = STYLE[mode]
    rows = read("ch09_tow2025.csv")
    tools = [r for r in rows if r["tool"] != "All eight tools"]
    allr = next(r for r in rows if r["tool"] == "All eight tools")
    fig, ax = plt.subplots(figsize=(8.0, 3.8))
    xs = range(len(tools))
    for x, r in zip(xs, tools):
        v = float(r["pct_incorrect"])
        ax.bar(x, v, 0.55, color=s["risk"], edgecolor=s["ink"], linewidth=1, hatch=s["risk_hatch"])
        ax.text(x, v + 2, f"{v:.0f}%", ha="center", fontsize=12, fontweight="bold", color=s["ink"])
    ax.axhline(float(allr["pct_incorrect"]), color=s["ink"], linestyle="--", linewidth=1.6)
    ax.text(-0.3, float(allr["pct_incorrect"]) + 2.5, "all eight tools together: more than 60%",
            fontsize=11, ha="left", color=s["ink"])
    ax.set_xticks(list(xs), [r["tool"] for r in tools])
    ax.set_ylim(0, 105)
    ax.set_ylabel("Queries answered incorrectly (%)")
    ax.set_title("In a February 2025 test, AI search tools gave wrong source details\n"
                 "for 37% to 94% of news excerpts", loc="left", fontweight="bold", fontsize=12.5, pad=10)
    fig.text(0.01, -0.1, "Source: Jazwinska & Chandrasekar (2025), Tow Center, Columbia Journalism Review: 200 news "
             "excerpts per tool, eight tools, one run each.\nThe three tools whose rates the article text reports; "
             "error rates ranged from 37% to 94%. As tested in February 2025.", fontsize=9.5, color=s["ink"])
    save(fig, "f9-12-tow-search", mode)


if __name__ == "__main__":
    for mode in ("color", "gray"):
        f9_9(mode)
        f9_12(mode)
    print("rendered f9-09-peters-summaries, f9-12-tow-search")
