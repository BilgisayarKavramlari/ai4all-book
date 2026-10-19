"""Chapter 20 data charts (color + gray SVG). Run from the repo root:
    python3 figures/scripts/ch20_charts.py
F20.3  NACE perception gap: students' vs. employers' ratings of recent graduates' proficiency (data/ch20_nace_gap.csv)
F20.5  WEF Future of Jobs 2025: jobs employers expect created, displaced and net, 2025-2030 (data/ch20_wef2025.csv)
Values copied from the publishers' pages; sources and caveats in data/ch20_sources_meta.txt.
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
                     "svg.fonttype": "none", "svg.hashsalt": "ch20"})
plt.rcParams["font.sans-serif"] = ["Source Sans 3", "STIXGeneral", "DejaVu Sans"]  # no system-font fallback in print (D29)

STYLE = {
    "color": {"main": "#1C3D6E", "accent": "#FCE38A", "risk": "#C2410C", "ink": "#1D1D1F", "muted": "#5C5C66",
              "light": "#EEF2F7", "hatch": None},
    "gray": {"main": "#3A3A3A", "accent": "#EDEDED", "risk": "#FFFFFF", "ink": "#000000", "muted": "#444444",
             "light": "#F4F4F4", "hatch": "///"},
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


def f20_3(mode):
    s = STYLE[mode]
    rows = sorted(read("ch20_nace_gap.csv"), key=lambda r: float(r["gap_points"]))
    fig, ax = plt.subplots(figsize=(8.0, 4.8))
    for i, r in enumerate(rows):
        st, em = float(r["students_proficiency"]), float(r["employers_proficiency"])
        ax.plot([em, st], [i, i], color=s["muted"], linewidth=2.0, zorder=1)
        ax.scatter([st], [i], marker="o", s=70, color=s["main"], zorder=3,
                   label="Students (rating recent graduates)" if i == 0 else None)
        ax.scatter([em], [i], marker="s", s=70, facecolor="white", edgecolor=s["ink"], linewidth=1.8, zorder=3,
                   label="Employers" if i == 0 else None)
        gap = float(r["gap_points"])
        xr = max(st, em) + 2.0
        ax.text(xr, i, f"{gap:+.1f} points", va="center", ha="left", fontsize=11, color=s["ink"],
                fontweight="bold" if abs(gap) >= 24 else "normal")
    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels([r["competency"] for r in rows], fontsize=12)
    ax.set_xlim(20, 112)
    ax.set_xticks(range(20, 101, 10))
    ax.set_xlabel('% rating recent graduates "very" or "extremely" proficient', fontsize=12)
    ax.set_title("Employers rated new graduates' proficiency 25 to 35 points lower than students did\n"
                 "in four competencies", fontsize=13, loc="left", color=s["ink"])
    ax.legend(loc="lower left", frameon=False, fontsize=11)
    ax.grid(axis="x", color=s["light"], linewidth=1)
    fig.text(0.0, -0.06, "Source: Gray (2025), NACE, Figure 1: 2024 Student Survey (Mar-May 2024; 20,482 students, "
             "group shown not stated)\nand Job Outlook 2025 (Aug-Sep 2024; 237 employers). Different people, "
             "not a matched comparison. Gap = students minus employers.", fontsize=10, color=s["muted"])
    save(fig, "f20-03-nace-gap", mode)


def f20_5(mode):
    s = STYLE[mode]
    rows = read("ch20_wef2025.csv")
    labels = ["Created", "Displaced", "Net growth"]
    vals = [int(r["millions"]) for r in rows]
    pct = [int(r["share_of_formal_employment_pct"]) for r in rows]
    fig, ax = plt.subplots(figsize=(8.0, 4.0))
    fills = [s["main"], s["risk"] if mode == "color" else "white", s["accent"]]
    hatches = [None, "///" if mode == "gray" else None, None]
    bars = ax.bar(labels, vals, color=fills, edgecolor=s["ink"], linewidth=1.4, width=0.55)
    for b, h in zip(bars, hatches):
        if h:
            b.set_hatch(h)
    for b, v, p in zip(bars, vals, pct):
        ax.text(b.get_x() + b.get_width() / 2, v + 4, f"{v} million\n({p}% of covered jobs)", ha="center",
                va="bottom", fontsize=11, color=s["ink"], fontweight="bold")
    ax.set_ylim(0, 215)
    ax.set_ylabel("Millions of jobs, 2025-2030 (all trends)", fontsize=12)
    ax.set_title("From employers' expectations, the WEF estimates more jobs created than displaced\nby 2030, "
                 "across all trends, with churn of 22%", fontsize=13, loc="left", color=s["ink"])
    fig.text(0.0, -0.12, "Source: World Economic Forum (2025), Future of Jobs Report 2025, pp. 5-6, 25, 97, 99. The WEF's estimates from "
             "employers' expectations (over 1,000 employers,\nsurvey May-September 2024; a p. 99 note says May-August), applied to "
             "about 1.18 billion employees in covered roles. All trends combined, not AI alone:\nthe report links about 11 million "
             "created and 9 million displaced to AI and information processing (p. 25).", fontsize=10, color=s["muted"])
    save(fig, "f20-05-wef-jobs", mode)


if __name__ == "__main__":
    for mode in ("color", "gray"):
        f20_3(mode)
        f20_5(mode)
    print("rendered f20-03-nace-gap, f20-05-wef-jobs")
