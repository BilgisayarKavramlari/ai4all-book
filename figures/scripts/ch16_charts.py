"""Chapter 16 data charts (color + gray SVG). Run from the repo root:
    python3 figures/scripts/ch16_charts.py
Published values:
  F16.6  data/ch16_gendershades.csv  (Buolamwini & Gebru, 2018, Table 4)
  F16.11 data/ch16_bianchi2023.csv   (Bianchi et al., 2023)
  F16.14 data/ch16_raji2019.csv      (Buolamwini & Gebru, 2018; Raji & Buolamwini, 2019)
This book's calculations (figures/scripts/ch16_experiments.py; exact, no randomness):
  F16.7  data/ch16_small_samples.csv
  F16.9  data/ch16_tradeoff.csv
"""
import csv
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import font_manager  # noqa: E402
from matplotlib.patches import Patch  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
for fam in ("Source Sans 3", "Source Sans Pro"):
    if any(fam in f.name for f in font_manager.fontManager.ttflist):
        plt.rcParams["font.family"] = fam
        break
plt.rcParams.update({"font.size": 12, "axes.spines.top": False, "axes.spines.right": False,
                     "svg.fonttype": "none", "svg.hashsalt": "ch16"})

STYLE = {
    "color": {"main": "#1C3D6E", "accent": "#FCE38A", "risk": "#C2410C", "ok": "#4CAF84", "ink": "#1D1D1F",
              "hatch": None, "risk_hatch": None, "ok_hatch": None, "muted": "#5C5C66", "light": "#EEF2F7"},
    "gray": {"main": "#3A3A3A", "accent": "#FFFFFF", "risk": "#FFFFFF", "ok": "#BDBDBD", "ink": "#000000",
             "hatch": "///", "risk_hatch": "xx", "ok_hatch": "..", "muted": "#444444", "light": "#FFFFFF"},
}


def read(name):
    with open(os.path.join(ROOT, "data", name), encoding="utf8") as fh:
        return list(csv.DictReader(line for line in fh if not line.startswith("#")))


def save(fig, fid, mode):
    out = os.path.join(ROOT, "figures", "out", mode, f"{fid}.svg")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    fig.savefig(out, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)


def title(ax, text):
    ax.set_title(text, loc="left", fontweight="bold", fontsize=12.5, pad=10)


def source(fig, text, y=-0.08):
    fig.text(0.01, y, text, fontsize=9.5, color="#1D1D1F")


# ---------------------------------------------------------------- F16.6 Gender Shades
def f16_6(mode):
    s = STYLE[mode]
    rows = [r for r in read("ch16_gendershades.csv") if r["metric"] == "error"]
    groups = [("All", "All faces"), ("LighterMale", "Lighter-skinned\nmen"), ("LighterFemale", "Lighter-skinned\nwomen"),
              ("DarkerMale", "Darker-skinned\nmen"), ("DarkerFemale", "Darker-skinned\nwomen")]
    styles = [(s["light"], None, 2.4), (s["ok"], s["ok_hatch"], 1), (s["accent"], None, 1),
              (s["main"], s["hatch"], 1), (s["risk"], s["risk_hatch"], 1)]
    fig, ax = plt.subplots(figsize=(8.0, 4.2))
    w = 0.16
    for ci, r in enumerate(rows):
        for gi, (key, _) in enumerate(groups):
            v = float(r[key])
            x = ci + (gi - 2) * w
            c, h, lw = styles[gi]
            ax.bar(x, v, w, color=c, hatch=h, edgecolor=s["ink"], linewidth=lw)
            ax.text(x, v + 0.6, f"{v:.1f}", ha="center", fontsize=9.5, color=s["ink"])
    ax.set_xticks(range(len(rows)), [r["classifier"] for r in rows], fontsize=11.5)
    ax.set_ylim(0, 40)
    ax.set_ylabel("Error rate (%)")
    ax.legend(handles=[Patch(facecolor=c, hatch=h, edgecolor=s["ink"], linewidth=lw, label=lab)
                       for (c, h, lw), (_, lab) in zip(styles, groups)],
              frameon=False, loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=5, fontsize=9.5)
    title(ax, "Overall error of 6–12% hid error rates of up to 35%\nfor darker-skinned women")
    source(fig, "Source: Buolamwini & Gebru (2018), Table 4: three commercial gender classifiers, April–May 2017, "
           "1,270 faces of parliamentarians.\nError = share of each group labeled with the wrong gender; groups as "
           "the authors labeled skin type (Fitzpatrick scale) and perceived gender.\nThick outline = all faces "
           "together.", y=-0.24)
    save(fig, "f16-06-gendershades", mode)


# ---------------------------------------------------------------- F16.7 small samples
def f16_7(mode):
    s = STYLE[mode]
    rows = [r for r in read("ch16_small_samples.csv") if int(r["runs_per_version"]) in (10, 15, 20, 25, 30, 35, 40, 45, 50, 100)]
    n = [r["runs_per_version"] for r in rows]
    chance = [float(r["pct_chance_gap_or_more"]) for r in rows]
    thr = [float(r["threshold_gap_points"]) for r in rows]
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(10.0, 3.9))
    a1.bar(range(len(n)), chance, 0.62, color=s["risk"], hatch=s["risk_hatch"], edgecolor=s["ink"], linewidth=1)
    for i, v in enumerate(chance):
        a1.text(i, v + 1.2, f"{v:.1f}", ha="center", fontsize=9.5, color=s["ink"])
    a1.set_xticks(range(len(n)), n)
    a1.set_xlabel("Runs per version")
    a1.set_ylabel("Chance of a gap of 20+ points (%)")
    a1.set_ylim(0, 60)
    title(a1, "Both versions truly at 50%: a 20-point\ngap is common when runs are few")
    a2.bar(range(len(n)), thr, 0.62, color=s["main"], hatch=s["hatch"], edgecolor=s["ink"], linewidth=1)
    for i, v in enumerate(thr):
        a2.text(i, v + 1.2, f"{v:g}", ha="center", fontsize=9.5, color=s["ink"])
    a2.set_xticks(range(len(n)), n)
    a2.set_xlabel("Runs per version")
    a2.set_ylabel("Chance threshold (percentage points)")
    a2.set_ylim(0, 60)
    title(a2, "The gap a finding needs\nshrinks as runs grow")
    fig.subplots_adjust(wspace=0.38)
    source(fig, "This book's calculation (figures/scripts/ch16_experiments.py; exact binomial; data/ch16_small_samples.csv): "
           "both versions truly give a \"yes\" 50% of the time,\nequal runs per version. Chance threshold = the smallest gap, in either direction, that chance alone reaches "
           "less than 1 time in 20. A calculation, not data about any tool.", y=-0.1)
    save(fig, "f16-07-small-samples", mode)


# ---------------------------------------------------------------- F16.9 trade-off
def f16_9(mode):
    s = STYLE[mode]
    rows = {(r["threshold_A"], r["threshold_B"]): r for r in read("ch16_tradeoff.csv")}
    designs = [(("0.5", "0.5"), "One threshold for both groups (0.5)"),
               (("0.5", "0.3"), "Group B's threshold lowered to 0.3")]
    metrics = [("miss_rate_pct", "Missed\n(miss rate)"), ("false_positive_rate_pct", "Wrongly flagged\n(false-positive rate)"),
               ("precision_pct", "Flag means\n(precision)")]
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 3.9), sharey=True)
    w = 0.36
    for ax, (key, name) in zip(axes, designs):
        r = rows[key]
        for mi, (m, lab) in enumerate(metrics):
            a, b = float(r[f"{m}_A"]), float(r[f"{m}_B"])
            ax.bar(mi - w / 2, a, w, color=s["main"], hatch=s["hatch"], edgecolor=s["ink"], linewidth=1)
            ax.bar(mi + w / 2, b, w, color=s["accent"], edgecolor=s["ink"], linewidth=1)
            ax.text(mi - w / 2, a + 1.5, f"{a:.1f}", ha="center", fontsize=9.5, color=s["ink"])
            ax.text(mi + w / 2, b + 1.5, f"{b:.1f}", ha="center", fontsize=9.5, color=s["ink"])
        ax.set_xticks(range(3), [lab for _, lab in metrics], fontsize=9.8)
        ax.set_ylim(0, 80)
        title(ax, name)
    axes[0].set_ylabel("Percent")
    fig.legend(handles=[Patch(facecolor=s["main"], hatch=s["hatch"], edgecolor=s["ink"], label="Group A (base rate 50%)"),
                        Patch(facecolor=s["accent"], edgecolor=s["ink"], label="Group B (base rate 30%)")],
               frameon=False, loc="upper center", bbox_to_anchor=(0.5, 0.0), ncol=2, fontsize=10)
    fig.suptitle("Equalizing the miss rates made a flag mean less in one group", x=0.01, ha="left",
                 fontweight="bold", fontsize=12.5, y=1.04)
    source(fig, "This book's calculation (figures/scripts/ch16_experiments.py; data/ch16_tradeoff.csv): two constructed "
           "groups of 1,000 students; scores built\nto mean the same in both groups. Exact counts. A calculation for "
           "teaching, not data about any tool or group.", y=-0.17)
    save(fig, "f16-09-tradeoff", mode)


# ---------------------------------------------------------------- F16.11 Bianchi
def f16_11(mode):
    s = STYLE[mode]
    rows = read("ch16_bianchi2023.csv")
    fig, ax = plt.subplots(figsize=(8.0, 2.6))
    for i, r in enumerate(rows):
        v = float(r["pct_white"])
        gen = i == 0
        ax.barh(i, v, 0.55, color=s["risk"] if gen else s["main"], hatch=s["risk_hatch"] if gen else s["hatch"],
                edgecolor=s["ink"], linewidth=1)
        ax.text(v + 1, i, f"{v:.0f}%", va="center", fontsize=11.5, fontweight="bold", color=s["ink"])
    ax.set_yticks(range(len(rows)), [r["group"] for r in rows], fontsize=10.5)
    ax.invert_yaxis()
    ax.set_xlim(0, 110)
    ax.set_xlabel("Shown as, or identifying as, White (%)")
    title(ax, "An image generator showed software developers as White\nfar more often than the U.S. workforce is")
    source(fig, "Source: Bianchi et al. (2023): prompt \"software developer\", Stable Diffusion, 100 images; race "
           "assigned by an automated classifier,\nso the 99% is itself a model's judgment. Workforce share: U.S. Bureau "
           "of Labor Statistics (2021), as cited by the authors.", y=-0.3)
    save(fig, "f16-11-bianchi", mode)


# ---------------------------------------------------------------- F16.14 Raji & Buolamwini
def f16_14(mode):
    s = STYLE[mode]
    rows = read("ch16_raji2019.csv")
    fig, ax = plt.subplots(figsize=(8.0, 3.8))
    w = 0.36
    for i, r in enumerate(rows):
        aug = float(r["aug_2018"])
        if r["may_2017"]:
            may = float(r["may_2017"])
            ax.bar(i - w / 2, may, w, color=s["risk"], hatch=s["risk_hatch"], edgecolor=s["ink"], linewidth=1)
            ax.text(i - w / 2, may + 0.8, f"{may:g}", ha="center", fontsize=9.5, color=s["ink"])
        else:
            ax.text(i - w / 2, 1.2, "not\naudited", ha="center", fontsize=9, color=s["ink"])
        ax.bar(i + w / 2, aug, w, color=s["main"], hatch=s["hatch"], edgecolor=s["ink"], linewidth=1)
        ax.text(i + w / 2, aug + 0.8, f"{aug:g}", ha="center", fontsize=9.5, color=s["ink"])
    ax.set_xticks(range(len(rows)), [r["company"] + ("\n(named in 2018)" if r["named_in_2018_paper"] == "yes"
                                                     else "\n(not named)") for r in rows], fontsize=10)
    ax.set_ylim(0, 40)
    ax.set_ylabel("Error for darker-skinned women (%)")
    ax.legend(handles=[Patch(facecolor=s["risk"], hatch=s["risk_hatch"], edgecolor=s["ink"], label="May 2017 (original audit)"),
                       Patch(facecolor=s["main"], hatch=s["hatch"], edgecolor=s["ink"], label="August 2018 (re-test)")],
              frameon=False, loc="upper right", fontsize=10)
    title(ax, "After a public audit, the three named companies cut darker-skinned\nwomen's error sharply; two others lagged")
    source(fig, "Sources: Buolamwini & Gebru (2018), Table 4; Raji & Buolamwini (2019), Table 1 (re-test August 21, "
           "2018, same benchmark).\nThe authors caution that models may have been tuned to this one benchmark.", y=-0.16)
    save(fig, "f16-13-raji", mode)


if __name__ == "__main__":
    for mode in ("color", "gray"):
        for fn in (f16_6, f16_7, f16_9, f16_11, f16_14):
            fn(mode)
    print("rendered f16-06, f16-07, f16-09, f16-11, f16-13")
