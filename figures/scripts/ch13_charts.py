"""Chapter 13 data charts (color + gray SVG). Run from the repo root:
    python3 figures/scripts/ch13_charts.py
F13.8   published values (data/ch13_koenecke2024.csv; Koenecke et al., 2024, Results)
F13.11  published values (data/ch13_human_detection.csv; Nightingale & Farid, 2022; Mai et al., 2023)
F13.12  published values (data/ch13_deepfake_eval.csv; Chandra et al., 2025, arXiv v5, Table 3)
Numbers in the chapter text are copied from these CSVs. Sources: data/ch13_SOURCES.txt.
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
                     "svg.fonttype": "none", "svg.hashsalt": "ch13"})

STYLE = {
    "color": {"main": "#1C3D6E", "accent": "#FCE38A", "risk": "#C2410C", "ink": "#1D1D1F", "hatch": None,
              "risk_hatch": None, "light": "#EEF2F7"},
    "gray": {"main": "#3A3A3A", "accent": "#FFFFFF", "risk": "#FFFFFF", "ink": "#000000", "hatch": "///",
             "risk_hatch": "xx", "light": "#FFFFFF"},
}


def read(name):
    with open(os.path.join(ROOT, "data", name), encoding="utf8") as fh:
        return list(csv.DictReader(fh))


def save(fig, fid, mode):
    out = os.path.join(ROOT, "figures", "out", mode, f"{fid}.svg")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    fig.savefig(out, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)


def f13_8(mode):
    s = STYLE[mode]
    rows = read("ch13_koenecke2024.csv")
    fig, ax = plt.subplots(figsize=(8.0, 3.6))
    ys = list(range(len(rows)))[::-1]
    for y, r in zip(ys, rows):
        v = float(r["pct_of_312_hallucinated_transcriptions"])
        total = r["category"].startswith("At least")
        ax.barh(y, v, height=0.6, color=s["risk"] if total else s["main"], edgecolor=s["ink"], linewidth=1,
                hatch=s["risk_hatch"] if total else s["hatch"])
        ax.text(v + 0.8, y, f"{v:.0f}%", va="center", fontsize=12, fontweight="bold", color=s["ink"])
    ax.set_yticks(ys, [r["category"] for r in rows])
    ax.set_xlim(0, 50)
    ax.set_xlabel("Share of the 312 transcriptions that contained invented text (%)")
    ax.set_title("In a 2023 test, 38% of transcripts with invented text\ncontained harmful inventions",
                 loc="left", fontweight="bold", fontsize=12.5, pad=10)
    fig.text(0.01, -0.24, "Source: Koenecke et al. (2024), FAccT '24. 13,140 short speech segments (AphasiaBank), run twice "
             "through a public speech-recognition\nservice in April and May 2023: 187 segments (about 1.4%) reliably "
             "produced invented text; 312 transcriptions contained it (roughly 1%).\nCategories overlap, so 19 + 13 + 8 "
             "is more than 38. In December 2023, after updates, 12 of the 187 segments still did.", fontsize=9.5,
             color=s["ink"])
    save(fig, "f13-08-whisper-harms", mode)


def f13_11(mode):
    s = STYLE[mode]
    rows = read("ch13_human_detection.csv")
    faces = [r for r in rows if r["task"].startswith("Faces")]
    speech = [r for r in rows if r["task"].startswith("Speech")]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.0, 3.9), gridspec_kw={"width_ratios": [2, 1]})
    for ax, group, ylab in ((ax1, faces, "Faces judged correctly (%)"),
                            (ax2, speech, "Deepfake clips identified (%)")):
        xs = range(len(group))
        for x, r in zip(xs, group):
            v = float(r["pct"])
            ax.bar(x, v, 0.55, color=s["main"], edgecolor=s["ink"], linewidth=1, hatch=s["hatch"])
            ax.text(x, v + 4, f"{v:.1f}%" if ax is ax1 else f"{v:g}%", ha="center", va="bottom", fontsize=12, fontweight="bold", color=s["ink"])
        ax.set_xticks(list(xs), [f"{r['task']}\nn = {int(r['participants'])}" for r in group], fontsize=10)
        ax.set_ylim(0, 100)
        ax.set_ylabel(ylab, fontsize=10.5)
        ax.set_xlim(-0.6, len(group) - 0.4)
    ax1.axhline(50, color="#8A8A8A", linestyle="-", linewidth=1.1, label="guessing: 50% (gray line)")
    ax1.legend(loc="upper left", frameon=False, fontsize=10.5)
    ax1.set_title("Faces: Nightingale & Farid (2022)", fontsize=11, loc="left")
    ax2.set_title("Voices: Mai et al. (2023)", fontsize=11, loc="left")
    fig.suptitle("People judging faces did about as well as guessing; training helped a little",
                 x=0.01, ha="left", fontweight="bold", fontsize=12.5)
    fig.text(0.01, -0.12, "Different studies, tasks and measures: compare each bar with its own panel, not across panels. "
             "Faces: real vs. generated (StyleGAN2).\nVoices: share of deepfake clips correctly identified in English and "
             "Mandarin (overall accuracy on real and fake clips: 70.35%).", fontsize=9.5, color=s["ink"])
    fig.tight_layout()
    save(fig, "f13-11-human-detection", mode)


def f13_12(mode):
    s = STYLE[mode]
    rows = read("ch13_deepfake_eval.csv")
    fig, ax = plt.subplots(figsize=(8.0, 4.2))
    xs = list(range(len(rows)))
    w = 0.38
    for x, r in zip(xs, rows):
        o = float(r["auc_original_test"])
        n = float(r["auc_deepfake_eval_2024"])
        ax.bar(x - w / 2, o, w, color=s["light"], edgecolor=s["ink"], linewidth=1)
        ax.bar(x + w / 2, n, w, color=s["risk"], edgecolor=s["ink"], linewidth=1, hatch=s["risk_hatch"])
        ax.text(x + w / 2, n + 0.02, f"{n:.2f}", ha="center", fontsize=9.5, color=s["ink"])
    ax.axhline(0.5, color="#8A8A8A", linestyle="-", linewidth=1.1)
    ax.set_xticks(xs, [f"{r['model']}\n({r['modality'].lower()})" for r in rows], fontsize=9.5)
    ax.set_ylim(0, 1.1)
    ax.set_ylabel("AUC (area under the curve)")
    ax.legend(handles=[plt.Rectangle((0, 0), 1, 1, facecolor=s["light"], edgecolor=s["ink"]),
                       plt.Rectangle((0, 0), 1, 1, facecolor=s["risk"], edgecolor=s["ink"], hatch=s["risk_hatch"]),
                       plt.Line2D([0], [0], color="#8A8A8A", linestyle="-", linewidth=1.1)],
              labels=["original test data (re-run)", "media flagged in 2024", "0.5 = guessing (gray line)"], loc="upper left",
              bbox_to_anchor=(0, 1.08), ncol=3, frameon=False, fontsize=9.5)
    ax.set_title("Detectors that scored 0.87–1.00 on their own test data\nscored 0.43–0.63 on 2024 media",
                 loc="left", fontweight="bold", fontsize=12.5, pad=24)
    fig.text(0.01, -0.17, "Source: Chandra et al. (2025), Deepfake-Eval-2024, arXiv:2503.02857 version 5 (May 2026), "
             "Table 3: nine open-source detectors, off the shelf, on real and fake\nmedia users flagged in 2024. The best "
             "of 22 anonymized commercial tools scored 0.79 (video), 0.93 (audio; the authors partly credit their audio "
             "labeling)\nand 0.90 (images) (Table 5). The authors built the benchmark with TrueMedia.org, a nonprofit "
             "deepfake-detection service (closed to the public in January 2025; TrueMedia.org, 2025).", fontsize=9.5, color=s["ink"])
    save(fig, "f13-12-detector-auc", mode)


if __name__ == "__main__":
    for mode in ("color", "gray"):
        f13_8(mode)
        f13_11(mode)
        f13_12(mode)
    print("rendered f13-08-whisper-harms, f13-11-human-detection, f13-12-detector-auc")
