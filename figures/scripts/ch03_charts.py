"""Chapter 3 data charts (color + gray SVG). Run from the repo root after ch03_tokens.py:
    python3 figures/scripts/ch03_charts.py
F3.2  token counts across languages   <- data/ch03_tokens.csv (computed, tiktoken 0.8.0)
F3.4  temperature                      <- data/ch03_temperature.csv (ILLUSTRATIVE scores)
F3.6  lost in the middle               <- data/ch03_lost_middle.csv (published values, Liu et al., 2024)
F3.13 reversal curse, real celebrities <- data/ch03_reversal.csv (published values, Berglund et al., 2024)
"""
import csv
import os

import numpy as np
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

STYLE = {
    "color": {"main": "#1C3D6E", "accent": "#FCE38A", "risk": "#C2410C", "ink": "#1D1D1F", "hatch": None,
              "muted": "#8A94A3"},
    "gray": {"main": "#3A3A3A", "accent": "#FFFFFF", "risk": "#FFFFFF", "ink": "#000000", "hatch": "///",
             "muted": "#7A7A7A"},
}


def read(name):
    with open(os.path.join(ROOT, "data", name), encoding="utf8") as fh:
        return [r for r in csv.DictReader(fh) if not r[list(r)[0]].startswith("#")]


def save(fig, fid, mode):
    out = os.path.join(ROOT, "figures", "out", mode, f"{fid}.svg")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    fig.savefig(out, bbox_inches="tight")
    if os.environ.get("CH03_PNG"):  # optional preview for layout checks (build/ch03/png)
        prev = os.path.join(ROOT, "build", "ch03", "png", f"{fid}-{mode}.png")
        os.makedirs(os.path.dirname(prev), exist_ok=True)
        fig.savefig(prev, bbox_inches="tight", dpi=90)
    plt.close(fig)


def f3_2(mode):
    s = STYLE[mode]
    rows = read("ch03_tokens.csv")
    names = [r["language"] for r in rows]
    new = [float(r["ratio_to_english_o200k_base"]) for r in rows]
    old = [float(r["ratio_to_english_cl100k_base"]) for r in rows]
    y = np.arange(len(rows))[::-1]
    h = 0.38
    fig, ax = plt.subplots(figsize=(8.6, 5.0))
    ax.barh(y + h / 2, new, h, color=s["main"], edgecolor=s["ink"], linewidth=1,
            label="Newer tokenizer (o200k_base)")
    ax.barh(y - h / 2, old, h, color=s["accent"], edgecolor=s["ink"], linewidth=1, hatch=s["hatch"],
            label="Older tokenizer (cl100k_base)")
    for i in range(len(rows)):
        ax.text(new[i] + 0.12, y[i] + h / 2, f"{new[i]:.1f}×", va="center", fontsize=11.5, color=s["ink"])
        ax.text(old[i] + 0.12, y[i] - h / 2, f"{old[i]:.1f}×", va="center", fontsize=11.5, color=s["ink"],
                fontweight="bold")
    ax.axvline(1.0, color=s["ink"], linewidth=1, linestyle=":")
    ax.set_yticks(y, names)
    ax.set_xlim(0, 10.8)
    ax.set_xlabel("Tokens needed for the same text, relative to English (English = 1.0×)")
    ax.legend(loc="upper right", frameon=False)
    ax.set_title("The same text needs more tokens in many languages than in English; the gap depends on the tokenizer",
                 loc="left", fontweight="bold", fontsize=12.5, pad=12)
    fig.text(0.01, -0.06, "Computed by the book (Oct 2026): full text of the Universal Declaration of Human Rights in each "
             "language, Unicode UDHR collection; tiktoken 0.8.0.", fontsize=9.5, color=s["ink"])
    save(fig, "f3-02-tokens-languages", mode)


def f3_4(mode):
    s = STYLE[mode]
    rows = read("ch03_temperature.csv")
    toks = [r["token"].replace(" other tokens combined", " others\ncombined") for r in rows]
    lo = [float(r["pct_T0.5"]) for r in rows]
    hi = [float(r["pct_T1.5"]) for r in rows]
    x = np.arange(len(rows))
    w = 0.38
    fig, ax = plt.subplots(figsize=(9.6, 4.2))
    ax.bar(x - w / 2, lo, w, color=s["main"], edgecolor=s["ink"], linewidth=1, label="Low temperature (0.5)")
    ax.bar(x + w / 2, hi, w, color=s["accent"], edgecolor=s["ink"], linewidth=1, hatch=s["hatch"],
           label="High temperature (1.5)")
    for i in range(len(rows)):
        ax.text(x[i] - w / 2 - 0.02, lo[i] + 1.2, f"{lo[i]:.0f}%", ha="center", fontsize=10.5, color=s["ink"])
        ax.text(x[i] + w / 2 + 0.02, hi[i] + 1.2, f"{hi[i]:.0f}%", ha="center", fontsize=10.5, color=s["ink"],
                fontweight="bold")
    ax.set_xticks(x, toks)
    ax.set_ylim(0, 72)
    ax.set_ylabel("Chance of being picked next (%)")
    ax.legend(loc="upper right", frameon=False)
    ax.set_title("Temperature changes how often less likely tokens are picked", loc="left", fontweight="bold",
                 fontsize=12.5)
    fig.text(0.01, -0.08, 'Illustrative scores chosen by the book (not real model output) for the next token after '
             '"A good name for a coffee shop near campus is".', fontsize=9.5, color=s["ink"])
    save(fig, "f3-04-temperature", mode)


def f3_6(mode):
    s = STYLE[mode]
    rows = read("ch03_lost_middle.csv")
    fig, ax = plt.subplots(figsize=(8.4, 4.2))
    styles = {"GPT-3.5-Turbo (0613)": ("-", "o", s["main"]), "Claude-1.3": ("--", "s", s["ink"] if mode == "gray" else s["risk"])}
    for model, (ls, mk, col) in styles.items():
        rr = [r for r in rows if r["model"] == model]
        pos = [int(r["answer_position"]) for r in rr]
        acc = [float(r["accuracy_pct"]) for r in rr]
        cb = float(rr[0]["closed_book_pct"])
        ax.plot(pos, acc, linestyle=ls, marker=mk, color=col, linewidth=2.4, markersize=6,
                markerfacecolor="white" if mk == "s" else col, label=model)
        ax.text(20.6, acc[-1], f"{model.split(' (')[0]}", va="center", fontsize=11, color=s["ink"],
                fontweight="bold")
        ax.axhline(cb, xmax=20.3 / 27, color=col, linewidth=1, linestyle=":")
        ax.text(20.6, cb, f"no documents: {cb:.1f}%", va="center", fontsize=10.5, color=s["ink"],
                style="italic")
    ax.annotate("Answer in the middle:\nlowest accuracy", xy=(10, 53.8), xytext=(11.5, 70),
                fontsize=11, color=s["ink"], arrowprops={"arrowstyle": "->", "color": s["ink"]})
    ax.set_xlim(0, 27)
    ax.set_ylim(40, 80)
    ax.set_xticks([1, 5, 10, 15, 20])
    ax.set_xlabel("Position of the document that contains the answer (out of 20 documents)")
    ax.set_ylabel("Questions answered correctly (%)")
    ax.legend(loc="upper center", frameon=False, ncol=2, bbox_to_anchor=(0.5, 1.0))
    ax.set_title("Information in the middle of a long context was used less reliably (2023 models)",
                 loc="left", fontweight="bold", fontsize=12.5, pad=22)
    fig.text(0.01, -0.07, "Published values: Liu et al. (2024; arXiv v3, App. G.2), question answering with 20 retrieved documents. "
             "Dotted lines: the same questions asked with no documents (closed book).", fontsize=9.5, color=s["ink"])
    save(fig, "f3-06-lost-middle", mode)


def f3_13(mode):
    s = STYLE[mode]
    rows = read("ch03_reversal.csv")
    labels = ["Celebrity → parent\n(mother and father questions)", "Parent → celebrity\n(\"Name a child of [parent]\")"]
    vals = [float(r["accuracy_pct"]) for r in rows]
    fig, ax = plt.subplots(figsize=(7.6, 3.4))
    y = [1, 0]
    ax.barh(y[0], vals[0], 0.5, color=s["main"], edgecolor=s["ink"], linewidth=1)
    ax.barh(y[1], vals[1], 0.5, color=s["accent"], edgecolor=s["ink"], linewidth=1, hatch=s["hatch"])
    for yy, v in zip(y, vals):
        ax.text(v + 1.5, yy, f"{v:.0f}%", va="center", fontsize=12.5, fontweight="bold", color=s["ink"])
    ax.set_yticks(y, labels)
    ax.set_xlim(0, 100)
    ax.set_xlabel("Questions answered correctly (%)")
    ax.set_title("GPT-4 named a celebrity's parent far more often than the parent's famous child (2023)",
                 loc="left", fontweight="bold", fontsize=12.5)
    fig.text(0.01, -0.14, "Published values: Berglund et al. (2024), section 2.2; 1,573 celebrity–parent pairs; the child direction "
             "counted as correct if any of ten tries was right.",
             fontsize=9.5, color=s["ink"])
    save(fig, "f3-13-reversal-real", mode)


if __name__ == "__main__":
    for mode in ("color", "gray"):
        f3_2(mode)
        f3_4(mode)
        f3_6(mode)
        f3_13(mode)
    print("ch03 charts rendered")
