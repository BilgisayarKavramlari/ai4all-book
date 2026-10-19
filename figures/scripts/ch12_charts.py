"""Chapter 12 data charts (color + gray SVG). Run from the repo root:
    python3 figures/scripts/ch12_charts.py
F12.7   published values (data/ch12_metr2025.csv; Becker et al., 2025)
F12.10  published values (data/ch12_bcg_outside.csv; Dell'Acqua et al., 2023, WP Tables 4 and 6, col. 1)
F12.14  published values (data/ch12_chen2024.csv; Chen, Zaharia & Zou, 2024)
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
                     "svg.fonttype": "none", "svg.hashsalt": "ch12"})
plt.rcParams["font.sans-serif"] = ["Source Sans 3", "STIXGeneral", "DejaVu Sans"]  # no system-font fallback in print (D29)

STYLE = {
    "color": {"main": "#1C3D6E", "accent": "#FCE38A", "risk": "#C2410C", "ink": "#1D1D1F", "hatch": None,
              "risk_hatch": None, "muted": "#5C5C66", "light": "#EEF2F7"},
    "gray": {"main": "#3A3A3A", "accent": "#FFFFFF", "risk": "#FFFFFF", "ink": "#000000", "hatch": "///",
             "risk_hatch": "xx", "muted": "#444444", "light": "#FFFFFF"},
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


def f12_7(mode):
    """METR (2025): forecast and belief vs. measured change in time per task."""
    s = STYLE[mode]
    rows = read("ch12_metr2025.csv")
    fig, ax = plt.subplots(figsize=(8.0, 3.9))
    ys = list(range(len(rows)))[::-1]
    for y, r in zip(ys, rows):
        v = float(r["value_pct_time_change"])
        measured = r["measure"] == "Measured"
        ax.barh(y, v, 0.55, color=s["risk"] if measured else s["light"], edgecolor=s["ink"], linewidth=1.2,
                hatch=s["risk_hatch"] if measured else ("..." if mode == "gray" else None),
                linestyle="-" if measured else "--")
        ax.text(v + 1.2 if v > 0 else 1.2, y, r["label"], va="center", ha="left",
                fontsize=11.5, fontweight="bold", color=s["ink"])
    ax.axvline(0, color=s["ink"], linewidth=1.4)
    ax.set_yticks(ys, [r["measure"] for r in rows])
    ax.set_xlim(-60, 60)
    ax.set_xlabel("Change in time per task with AI allowed (%): left = faster, right = slower")
    ax.set_title("Developers expected AI to speed them up and felt faster;\nmeasured, their tasks took longer",
                 loc="left", fontweight="bold", fontsize=12.5, pad=10)
    fig.text(0.01, -0.12, "Source: Becker, Rush, Barnes & Rein (2025), METR: 16 experienced open-source developers, "
             "246 tasks, February–June 2025;\ntasks randomly assigned to AI allowed or not. Dashed bars = what "
             "developers expected or believed; solid = measured. Results for early-2025 tools in this setting.",
             fontsize=9.5, color=s["ink"])
    save(fig, "f12-07-metr", mode)


def f12_10(mode):
    """BCG outside task: rated quality up, correctness down (WP Tables 6 and 4, col. 1)."""
    s = STYLE[mode]
    rows = read("ch12_bcg_outside.csv")
    ai = [r for r in rows if r["condition"] != "No AI (control)"]
    ctrl = next(r for r in rows if r["condition"] == "No AI (control)")
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(8.4, 3.9))
    xs = range(len(ai))
    for x, r in zip(xs, ai):
        q = float(r["quality_change_pct_vs_control"])
        a1.bar(x, q, 0.55, color=s["main"], edgecolor=s["ink"], linewidth=1, hatch=s["hatch"])
        a1.text(x, q + 1, f"+{q:.1f}%", ha="center", fontsize=12, fontweight="bold", color=s["ink"])
        d = float(r["diff_pp_vs_control"])
        a2.bar(x, d, 0.55, color=s["risk"], edgecolor=s["ink"], linewidth=1, hatch=s["risk_hatch"])
        a2.text(x, d - 2.6, f"{d:.1f} points", ha="center", fontsize=12, fontweight="bold", color=s["ink"])
    for ax in (a1, a2):
        ax.set_xticks(list(xs), [r["condition"] for r in ai])
        ax.axhline(0, color=s["ink"], linewidth=1.2)
    a1.set_ylim(0, 32)
    a1.set_ylabel("Rated quality vs. no AI (%)")
    a1.set_title("Rated quality: up", loc="left", fontweight="bold", fontsize=12)
    a2.set_ylim(-32, 0)
    a2.set_ylabel("Correct answers vs. no AI\n(percentage points)")
    a2.set_title(f"Correct answers: down (no AI: {float(ctrl['correct_pct']):.1f}%)", loc="left",
                 fontweight="bold", fontsize=12)
    fig.suptitle("On the task outside the frontier, rated quality rose with AI while correct answers fell",
                 x=0.01, ha="left", fontweight="bold", fontsize=12.5, y=1.04)
    fig.text(0.01, -0.1, "Source: Dell'Acqua et al. (2023), Harvard Business School Working Paper 24-013, Table 6 col. 1 (recommendation "
             "quality, 1–10 scale, two sets of human graders)\nand Table 4 col. 1 (correctness); 373 consultants, "
             "GPT-4 as of April 2023. Quality rose for right and wrong answers alike (working paper, Figure 8).",
             fontsize=9.5, color=s["ink"])
    fig.tight_layout()
    save(fig, "f12-10-quality-correctness", mode)


def f12_14(mode):
    """Chen, Zaharia & Zou (2024): prime vs. composite accuracy, March vs. June 2023."""
    s = STYLE[mode]
    rows = read("ch12_chen2024.csv")
    models = ["GPT-4", "GPT-3.5"]
    fig, ax = plt.subplots(figsize=(8.0, 3.9))
    w = 0.34
    for i, m in enumerate(models):
        mar = float(next(r for r in rows if r["model"] == m and r["month"] == "March 2023")["accuracy_pct"])
        jun = float(next(r for r in rows if r["model"] == m and r["month"] == "June 2023")["accuracy_pct"])
        ax.bar(i - w / 2, mar, w, color=s["light"], edgecolor=s["ink"], linewidth=1.2,
               hatch="..." if mode == "gray" else None, label="March 2023" if i == 0 else None)
        ax.bar(i + w / 2, jun, w, color=s["main"], edgecolor=s["ink"], linewidth=1.2, hatch=s["hatch"],
               label="June 2023" if i == 0 else None)
        ax.text(i - w / 2, mar + 2, f"{mar:.0f}%", ha="center", fontsize=12, fontweight="bold", color=s["ink"])
        ax.text(i + w / 2, jun + 2, f"{jun:.0f}%", ha="center", fontsize=12, fontweight="bold", color=s["ink"])
    ax.axhline(50, color=s["ink"], linestyle="--", linewidth=1.3)
    ax.text(0.5, 53, "50% = guessing", fontsize=10.5, ha="center", va="bottom", color=s["ink"])
    ax.set_xticks([0, 1], models)
    ax.set_ylim(0, 118)
    ax.set_yticks([0, 20, 40, 60, 80, 100])
    ax.set_ylabel("Correct on prime vs. composite (%)")
    ax.legend(frameon=False, loc="upper center", ncol=2)
    ax.set_title("The same named model scored about 84% in March 2023 and 51% in June", loc="left",
                 fontweight="bold", fontsize=12.5, pad=10)
    fig.text(0.01, -0.1, "Source: Chen, Zaharia & Zou (2024), Harvard Data Science Review: 1,000 numbers (500 prime, "
             "500 composite), a \"think step by step\" prompt,\nMarch and June 2023 versions of each named model. Half the numbers were "
             "prime, so 50% is what guessing scores. Results for these versions and this task only.", fontsize=9.5, color=s["ink"])
    save(fig, "f12-14-drift", mode)


if __name__ == "__main__":
    for mode in ("color", "gray"):
        f12_7(mode)
        f12_10(mode)
        f12_14(mode)
    print("rendered f12-07-metr, f12-10-quality-correctness, f12-14-drift")
