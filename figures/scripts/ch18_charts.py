"""Chapter 18 data chart (color + gray SVG). Run from the repo root:
    python3 figures/scripts/ch18_charts.py
Published dates (not computed):
  F18.13  data/ch18_legal_status.csv, rows with group "aiact" (Regulation (EU) 2024/1689, Art. 113, as amended by
          Regulation (EU) 2026/1744). The same table feeds the dated box in section 18.5 and the refresh list.
"""
import csv
import os
from datetime import date

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import matplotlib.dates as mdates  # noqa: E402
from matplotlib import font_manager  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
for fam in ("Source Sans 3", "Source Sans Pro"):
    if any(fam in f.name for f in font_manager.fontManager.ttflist):
        plt.rcParams["font.family"] = fam
        break
plt.rcParams.update({"font.size": 12, "axes.spines.top": False, "axes.spines.right": False,
                     "svg.fonttype": "none", "svg.hashsalt": "ch18"})
plt.rcParams["font.sans-serif"] = ["Source Sans 3", "STIXGeneral", "DejaVu Sans"]  # no system-font fallback in print (D29)

STYLE = {
    "color": {"main": "#1C3D6E", "risk": "#C2410C", "ink": "#1D1D1F", "muted": "#5C5C66"},
    "gray": {"main": "#3A3A3A", "risk": "#000000", "ink": "#000000", "muted": "#444444"},
}
LABELS = {
    "aiact_prohibited": "Prohibited practices;\nAI literacy",
    "aiact_gpai": "General-purpose\nAI models",
    "aiact_art50": "Transparency (Art. 50)",
    "aiact_annex3": "High-risk: Annex III uses\n(education, employment …)",
    "aiact_annex1": "High-risk: AI in products\n(Annex I)",
}


def read():
    with open(os.path.join(ROOT, "data", "ch18_legal_status.csv"), encoding="utf8") as fh:
        return list(csv.DictReader(line for line in fh if not line.startswith("#")))


def f18_13(mode):
    s = STYLE[mode]
    rows = [r for r in read() if r["group"] == "aiact"]
    fig, ax = plt.subplots(figsize=(8.4, 3.9))
    for i, r in enumerate(rows):
        y = len(rows) - 1 - i
        o, c = date.fromisoformat(r["original_date"]), date.fromisoformat(r["current_date"])
        if o == c:
            ax.plot([o], [y], "o", ms=9, color=s["main"], markeredgecolor=s["ink"])
            ax.text(mdates.date2num(o) + 25, y, f"{o:%b %-d, %Y} (unchanged)", va="center", fontsize=10,
                    color=s["ink"])
        else:
            ax.plot([o], [y], "o", ms=9, markerfacecolor="white", markeredgecolor=s["ink"], markeredgewidth=1.6)
            ax.annotate("", xy=(c, y), xytext=(o, y),
                        arrowprops=dict(arrowstyle="-|>", color=s["risk"], lw=2.2, shrinkA=6, shrinkB=6))
            ax.plot([c], [y], "s", ms=9, color=s["risk"], markeredgecolor=s["ink"])
            ax.text(mdates.date2num(c) + 25, y, f"{o:%b %Y} → {c:%b %-d, %Y}", va="center", fontsize=10,
                    color=s["ink"], fontweight="bold")
    ax.set_yticks(range(len(rows)), [LABELS[r["id"]] for r in reversed(rows)], fontsize=10.5)
    ax.set_xlim(date(2024, 10, 1), date(2030, 12, 31))
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.axvline(date(2026, 10, 18), color=s["muted"], lw=0.8)
    ax.text(date(2026, 10, 18), len(rows) - 0.45, "October 2026", ha="center", fontsize=9.5, color=s["muted"])
    ax.set_ylim(-0.6, len(rows) - 0.2)
    ax.legend(handles=[Line2D([], [], marker="o", ls="", ms=8, color=s["main"], label="date unchanged"),
                       Line2D([], [], marker="o", ls="", ms=8, markerfacecolor="white", markeredgecolor=s["ink"],
                              label="original date"),
                       Line2D([], [], marker="s", ls="", ms=8, color=s["risk"], label="date after the 2026 amendment")],
              frameon=False, loc="upper center", bbox_to_anchor=(0.5, -0.1), ncol=3, fontsize=9.5)
    ax.set_title("Regulation 2026/1744 moved the high-risk dates; the other dates stayed", loc="left",
                 fontweight="bold", fontsize=12.5, pad=10)
    fig.text(0.01, -0.12, "Source: Regulation (EU) 2024/1689, Art. 113; Regulation (EU) 2026/1744 (OJ L, 24.7.2026). "
             "Dates as published, read October 2026 (data/ch18_legal_status.csv).\nShape and arrow carry the meaning "
             "(circle = original or unchanged, square = moved). Check the current status.", fontsize=9.5,
             color="#1D1D1F")
    out = os.path.join(ROOT, "figures", "out", mode, "f18-13-aiact-dates.svg")
    fig.savefig(out, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)


if __name__ == "__main__":
    for m in ("color", "gray"):
        f18_13(m)
    print("rendered f18-13-aiact-dates")
