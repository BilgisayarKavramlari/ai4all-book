"""Chapter 10 data and computed charts (color + gray SVG). Run from the repo root:
    python3 figures/scripts/ch10_charts.py
F10.10  published percentages (data/ch10_liang2023.csv; Liang et al., 2023: counts of 91 TOEFL essays derived
        from the paper's 97.8% and 19.8%)
F10.15  computed illustration (Deep 10.A): share of flagged texts that are human-written, from OpenAI's reported
        26% detection and 9% false-positive rates at assumed shares of AI-written text. No randomness. Writes
        data/ch10_detector_baserate.csv.
"""
import csv
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import font_manager  # noqa: E402
from matplotlib.patches import Rectangle  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
for fam in ("Source Sans 3", "Source Sans Pro"):
    if any(fam in f.name for f in font_manager.fontManager.ttflist):
        plt.rcParams["font.family"] = fam
        break
plt.rcParams.update({"font.size": 12, "axes.spines.top": False, "axes.spines.right": False,
                     "svg.fonttype": "none", "svg.hashsalt": "ch10"})
plt.rcParams["font.sans-serif"] = ["Source Sans 3", "STIXGeneral", "DejaVu Sans"]  # no system-font fallback in print (D29)

STYLE = {
    "color": {"main": "#1C3D6E", "mid": "#8FA8CF", "risk": "#C2410C", "ink": "#1D1D1F", "muted": "#5C5C66",
              "risk_hatch": None, "mid_hatch": None},
    "gray": {"main": "#3A3A3A", "mid": "#BDBDBD", "risk": "#FFFFFF", "ink": "#000000", "muted": "#444444",
             "risk_hatch": "xxx", "mid_hatch": None},
}

TPR, FPR = 0.26, 0.09          # OpenAI (2023), as reported: 26% of AI texts flagged; 9% of human texts flagged
SHARES = [0.05, 0.10, 0.25]    # assumed shares of AI-written texts (illustration)


def read(name):
    with open(os.path.join(ROOT, "data", name), encoding="utf8") as fh:
        return list(csv.DictReader(fh))


def save(fig, fid, mode):
    out = os.path.join(ROOT, "figures", "out", mode, f"{fid}.svg")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    fig.savefig(out, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)


def f10_10(mode):
    s = STYLE[mode]
    rows = read("ch10_liang2023.csv")
    counts = [int(r["essays"]) for r in rows]
    assert sum(counts) == 91
    groups = [("all", counts[0]), ("some", counts[1]), ("none", counts[2])]
    fig, ax = plt.subplots(figsize=(8.0, 3.3))
    cols, k = 13, 0
    for kind, n in groups:
        for _ in range(n):
            r, c = divmod(k, cols)
            x, y = c, -r
            if kind == "all":
                ax.add_patch(Rectangle((x, y), 0.86, 0.86, facecolor=s["risk"], edgecolor=s["ink"], lw=1.1,
                                       hatch=s["risk_hatch"]))
            elif kind == "some":
                ax.add_patch(Rectangle((x, y), 0.86, 0.86, facecolor=s["mid"], edgecolor=s["ink"], lw=0.8))
            else:
                ax.add_patch(Rectangle((x, y), 0.86, 0.86, facecolor="#FFFFFF", edgecolor=s["ink"], lw=1.4))
            k += 1
    ax.set_xlim(-0.3, cols + 6.2)
    ax.set_ylim(-6.3, 1.1)
    ax.set_aspect("equal")
    ax.axis("off")
    lx = cols + 0.6
    ax.add_patch(Rectangle((lx, 0), 0.86, 0.86, facecolor=s["risk"], edgecolor=s["ink"], lw=1.1,
                           hatch=s["risk_hatch"]))
    ax.text(lx + 1.2, 0.43, f"flagged by all seven: {counts[0]}", va="center", fontsize=11.5, color=s["ink"])
    ax.add_patch(Rectangle((lx, -1.4), 0.86, 0.86, facecolor=s["mid"], edgecolor=s["ink"], lw=0.8))
    ax.text(lx + 1.2, -0.97, f"by one to six: {counts[1]}", va="center", fontsize=11.5, color=s["ink"])
    ax.add_patch(Rectangle((lx, -2.8), 0.86, 0.86, facecolor="#FFFFFF", edgecolor=s["ink"], lw=1.4))
    ax.text(lx + 1.2, -2.37, f"by none: {counts[2]}", va="center", fontsize=11.5, color=s["ink"])
    ax.text(lx, -4.3, "U.S. eighth-grade essays (88):\nnear-perfectly classified\nas human", fontsize=11,
            color=s["ink"], va="top")
    ax.set_title(f"In a 2023 test, at least one of seven detectors flagged {counts[0] + counts[1]} of 91 essays\n"
                 "written by non-native English speakers for the TOEFL", loc="left", fontweight="bold",
                 fontsize=12.5)
    fig.text(0.01, -0.02, "Each square = one human-written essay. Source: Liang et al. (2023), Patterns: seven "
             "detectors as of early 2023; 91 TOEFL essays from one Chinese\nforum. Counts derived from the paper's "
             "97.8% (at least one detector) and 19.8% (all seven). Average false-positive rate: 61.3%.",
             fontsize=9.5, color=s["ink"])
    save(fig, "f10-10-liang-essays", mode)


def base_rates():
    rows = []
    for p in SHARES:
        ai_flag = TPR * p * 1000
        hu_flag = FPR * (1 - p) * 1000
        rows.append({"assumed_share_ai": f"{p:.2f}", "ai_texts_per_1000": f"{p * 1000:.0f}",
                     "ai_flagged": f"{ai_flag:.1f}", "human_flagged": f"{hu_flag:.1f}",
                     "share_of_flags_human": f"{hu_flag / (ai_flag + hu_flag):.3f}",
                     "rates": "TPR 0.26, FPR 0.09 (OpenAI, 2023, as reported)"})
    out = os.path.join(ROOT, "data", "ch10_detector_baserate.csv")
    with open(out, "w", newline="", encoding="utf8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    return rows


def f10_15(mode, rows):
    s = STYLE[mode]
    fig, ax = plt.subplots(figsize=(8.0, 3.6))
    labels = [f"{float(r['assumed_share_ai']):.0%} of texts\nAI-written" for r in rows]
    vals = [float(r["share_of_flags_human"]) * 100 for r in rows]
    ys = range(len(rows))
    for y, v in zip(ys, vals):
        ax.barh(y, v, color=s["main"], edgecolor=s["ink"], height=0.6)
        ax.text(v + 1.2, y, f"{v:.0f}%", va="center", fontsize=11.5, fontweight="bold", color=s["ink"])
    ax.set_yticks(list(ys), labels)
    ax.invert_yaxis()
    ax.set_xlim(0, 100)
    ax.axvline(50, color=s["ink"], linestyle="--", linewidth=1.2)
    ax.set_xlabel("Flagged texts that were written by a person (%)")
    ax.set_title("In this illustration, most flagged texts are human-written\nwhen most writing is human",
                 loc="left", fontweight="bold", fontsize=12.5)
    fig.text(0.01, -0.12, "Computed illustration, not a study: detection 26% and false positives 9%, the rates OpenAI "
             "reported for its own weak 2023 classifier on a challenge set\n(withdrawn July 2023); assumed shares of AI-written text. "
             "Dashed line = half of all flags. Data: data/ch10_detector_baserate.csv.", fontsize=9.5,
             color=s["ink"])
    save(fig, "f10-15-base-rates", mode)


if __name__ == "__main__":
    rows = base_rates()
    for mode in ("color", "gray"):
        f10_10(mode)
        f10_15(mode, rows)
    print("rendered f10-10, f10-15; wrote data/ch10_detector_baserate.csv")
