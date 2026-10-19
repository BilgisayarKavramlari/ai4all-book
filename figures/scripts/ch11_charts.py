"""Chapter 11 data charts (color + gray SVG). Run from the repo root:
    python3 figures/scripts/ch11_charts.py
Constructed or simulated (figures/scripts/ch11_experiments.py):
  F11.5  data/ch11_missing_choices.csv       F11.6  data/ch11_missing_sim.csv
  F11.10 data/ch11_proxy_sim.csv (Lab 11.4)  F11.15 data/ch11_matrix_sensitivity.csv
  F11.13 data/ch11_simpson_constructed.csv
Published values:
  F11.9  data/ch11_obermeyer_labels.csv (Obermeyer et al., 2019, Table 2)
  F11.17 data/ch11_obermeyer_enrollment.csv (Obermeyer et al., 2019, text and Table 3)
  F11.16 data/ch11_dratsch2023.csv (Dratsch et al., 2023, abstract)
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
                     "svg.fonttype": "none", "svg.hashsalt": "ch11"})
plt.rcParams["font.sans-serif"] = ["Source Sans 3", "STIXGeneral", "DejaVu Sans"]  # no system-font fallback in print (D29)

STYLE = {
    "color": {"main": "#1C3D6E", "accent": "#FCE38A", "risk": "#C2410C", "ok": "#4CAF84", "ink": "#1D1D1F",
              "hatch": None, "risk_hatch": None, "ok_hatch": None, "muted": "#5C5C66", "light": "#EEF2F7"},
    "gray": {"main": "#3A3A3A", "accent": "#FFFFFF", "risk": "#FFFFFF", "ok": "#BDBDBD", "ink": "#000000",
             "hatch": "///", "risk_hatch": "xx", "ok_hatch": None, "muted": "#444444", "light": "#FFFFFF"},
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


# ---------------------------------------------------------------- F11.5 five choices
def f11_5(mode):
    s = STYLE[mode]
    rows = read("ch11_missing_choices.csv")
    labels = ["True hours\n(demo only)", "Blank = 0", "Drop rows\nwith a blank", "Fill: mean of\nall shifts",
              "Fill: the event's\nown mean", "Copy the\nprevious shift"]
    fig, ax = plt.subplots(figsize=(8.0, 4.4))
    xs = range(len(rows))
    w = 0.36
    for x, r in zip(xs, rows):
        swap, car = float(r["Book swap ($/h)"]), float(r["Car wash ($/h)"])
        truth = x == 0
        ax.bar(x - w / 2, swap, w, color=s["risk"] if not truth else s["light"], edgecolor=s["ink"], linewidth=1,
               hatch=s["risk_hatch"] if not truth else None)
        ax.bar(x + w / 2, car, w, color=s["main"], edgecolor=s["ink"], linewidth=1, hatch=s["hatch"])
        ax.text(x - w / 2, swap + 0.8, f"{swap:.2f}", ha="center", fontsize=9.5, color=s["ink"])
        ax.text(x + w / 2, car + 0.8, f"{car:.2f}", ha="center", fontsize=9.5, color=s["ink"])
        best = r["best event"]
        ax.text(x, -12.5, "→ " + ("car wash" if best == "Car wash" else "book swap"), ha="center",
                fontsize=10, fontweight="bold", color=s["ink"])
    ax.set_xticks(list(xs), labels, fontsize=10)
    ax.set_ylim(0, 44)
    ax.set_ylabel("Net proceeds per volunteer hour ($)")
    ax.legend(handles=[Patch(facecolor=s["risk"], edgecolor=s["ink"], hatch=s["risk_hatch"], label="Book swap (two blanks)"),
                       Patch(facecolor=s["main"], edgecolor=s["ink"], hatch=s["hatch"], label="Car wash (no blanks)")],
              frameon=False, loc="upper right", fontsize=10.5)
    title(ax, "In this constructed log, five common ways of handling two blanks\nall picked the same wrong event")
    source(fig, "Constructed data (data/ch11_missing_choices.csv). The two blank cells are the book swap's longest\n"
           "shifts (14 h and 13 h). Bake sale: 18.00 under every choice (not shown). → = the event each choice picks.", y=-0.2)
    save(fig, "f11-05-missing-choices", mode)


# ---------------------------------------------------------------- F11.6 simulation
def f11_6(mode):
    s = STYLE[mode]
    rows = read("ch11_missing_sim.csv")
    short = ["Blank = 0", "Drop rows with a blank", "Fill: mean of all shifts", "Fill: the event's own mean",
             "Copy the previous shift"]
    cols = list(rows[0].keys())
    fig, ax = plt.subplots(figsize=(8.0, 4.0))
    ys = range(len(rows))
    h = 0.36
    for y, r in zip(ys, rows):
        a, b = float(r[cols[1]]) * 100, float(r[cols[2]]) * 100
        ax.barh(y - h / 2, a, h, color=s["main"], edgecolor=s["ink"], hatch=s["hatch"], linewidth=1)
        ax.barh(y + h / 2, b, h, color=s["risk"], edgecolor=s["ink"], hatch=s["risk_hatch"], linewidth=1)
        ax.text(a + 1, y - h / 2, f"{a:.1f}%", va="center", fontsize=10.5, color=s["ink"])
        ax.text(b + 1, y + h / 2, f"{b:.1f}%", va="center", fontsize=10.5, color=s["ink"])
    ax.set_yticks(list(ys), short)
    ax.invert_yaxis()
    ax.set_xlim(0, 110)
    ax.set_xlabel("Simulated logs in which the choice picked the truly best event (%)")
    ax.legend(handles=[Patch(facecolor=s["main"], edgecolor=s["ink"], hatch=s["hatch"],
                             label="Blanks at random in every event"),
                       Patch(facecolor=s["risk"], edgecolor=s["ink"], hatch=s["risk_hatch"],
                             label="Blanks only at one event, mostly its long shifts")],
              frameon=False, loc="upper center", bbox_to_anchor=(0.45, -0.2), ncol=2, fontsize=10)
    title(ax, "In 1,000 simulated logs, every shortcut did worse\nwhen the blanks were the long shifts of one event")
    source(fig, "Simulated data: 1,000 constructed logs per condition, seed 11, three events, eight shifts each\n"
           "(data/ch11_missing_sim.csv; parameters in data/ch11_experiments_meta.txt). As in the chapter's log, long shifts\n"
           "earn less per hour in the simulation. A teaching simulation, not a study of real events.", y=-0.3)
    save(fig, "f11-06-missing-sim", mode)


# ---------------------------------------------------------------- F11.9 Obermeyer labels
def f11_9(mode):
    s = STYLE[mode]
    rows = read("ch11_obermeyer_labels.csv")
    names = {"Total costs": "Total costs\n(like the original algorithm)", "Avoidable costs": "Avoidable costs\n"
             "(emergency visits, hospital stays)", "Active chronic conditions": "Active chronic conditions\n"
             "(a health measure)"}
    fig, ax = plt.subplots(figsize=(8.0, 3.8))
    for i, r in enumerate(rows):
        v = float(r["fraction_black_in_top3pct"]) * 100
        health = i == 2
        ax.barh(i, v, 0.55, color=s["ok"] if health else s["main"], edgecolor=s["ink"], linewidth=1,
                hatch=None if health else s["hatch"])
        ax.text(v + 0.6, i, f"{v:.1f}%", va="center", fontsize=12, fontweight="bold", color=s["ink"])
    ax.set_yticks(range(len(rows)), [names[r["training_label"]] for r in rows])
    ax.invert_yaxis()
    ax.set_xlim(0, 32)
    ax.set_xlabel("Black patients among the 3% with the highest predicted risk (%)")
    title(ax, "Changing only the label nearly doubled the share of Black patients\namong the highest-risk 3%")
    source(fig, "Source: Obermeyer, Powers, Vogeli & Mullainathan (2019), Science, Table 2 (holdout set; same inputs "
           "and training,\nrace excluded; standard error 0.3 percentage points for each share).", y=-0.13)
    save(fig, "f11-09-obermeyer-labels", mode)


# ---------------------------------------------------------------- F11.10 proxy simulation (Lab 11.4)
def f11_10(mode):
    s = STYLE[mode]
    rows = read("ch11_proxy_sim.csv")
    gaps = [float(r["access_gap_group_B"]) * 100 for r in rows]
    need = [float(r["group_B_share_selected_by_need"]) * 100 for r in rows]
    cost = [float(r["group_B_share_selected_by_cost"]) * 100 for r in rows]
    fig, ax = plt.subplots(figsize=(8.0, 3.8))
    ax.plot(gaps, need, color=s["main"], linewidth=2.2, marker="o", label="Selected by need (the goal)")
    ax.plot(gaps, cost, color=s["risk"] if mode == "color" else s["ink"], linewidth=2.2, linestyle="--",
            marker="s", label="Selected by cost (the proxy)")
    for g, c in zip(gaps, cost):
        ax.text(g, c + 0.7, f"{c:.1f}%", ha="center", fontsize=10.5, color=s["ink"])
    ax.set_xlabel("Access gap: how much less is spent on group B for the same need (%)")
    ax.set_ylabel("Group B among the top 3% (%)")
    ax.set_ylim(0, 15)
    ax.legend(frameon=False, loc="upper right", fontsize=10.5)
    title(ax, "In a simulation, a 30% access gap cut group B's share of those selected\nfrom 12% to about 3.5%")
    source(fig, "Simulated mechanism, not Obermeyer et al.'s data (data/ch11_proxy_sim.csv; 20,000 people,\n"
           "12% in group B, 50 seeds). Need is the same in both groups, unlike the case, and selecting only the\n"
           "top 3% magnifies small gaps. Even with no gap, about 40% of the highest-need people were not selected\n"
           "by cost: that is random noise in spending, not the gap.", y=-0.22)
    save(fig, "f11-10-proxy-sim", mode)


# ---------------------------------------------------------------- F11.13 Simpson (constructed)
def f11_13(mode):
    s = STYLE[mode]
    rows = read("ch11_simpson_constructed.csv")
    rate = {}
    tot = {"X": [0, 0], "Y": [0, 0]}
    for r in rows:
        a, d = int(r["applicants"]), int(r["admitted"])
        rate[(r["department"], r["group"])] = 100 * d / a
        tot[r["group"]][0] += a
        tot[r["group"]][1] += d
    groups = ["Department 1 (easier)", "Department 2 (harder)", "Total"]
    fig, ax = plt.subplots(figsize=(8.0, 3.8))
    w = 0.34
    for i, g in enumerate(groups):
        if g == "Total":
            x_, y_ = 100 * tot["X"][1] / tot["X"][0], 100 * tot["Y"][1] / tot["Y"][0]
        else:
            x_, y_ = rate[(g, "X")], rate[(g, "Y")]
        ax.bar(i - w / 2, x_, w, color=s["main"], edgecolor=s["ink"], hatch=s["hatch"], linewidth=1)
        ax.bar(i + w / 2, y_, w, color=s["light"], edgecolor=s["ink"], linewidth=1.4)
        ax.text(i - w / 2, x_ + 2, f"X {x_:.0f}%", ha="center", fontsize=11, color=s["ink"])
        ax.text(i + w / 2, y_ + 2, f"Y {y_:.0f}%", ha="center", fontsize=11, color=s["ink"])
    ax.axvline(1.5, color=s["ink"], linestyle=":", linewidth=1.2)
    ax.set_xticks(range(3), ["Department 1 (easier)\nX: 400 apply\nY: 100 apply", "Department 2 (harder)\n"
                             "X: 100 apply\nY: 400 apply", "Total\n500 applicants\nin each group"])
    ax.set_ylim(0, 100)
    ax.set_ylabel("Admitted (%)")
    title(ax, "In this constructed example, the total favored one group\nwhile both departments favored the other")
    source(fig, "Constructed numbers (data/ch11_simpson_constructed.csv). In Berkeley's real fall 1973 data the "
           "pattern was milder: few departments\nshowed a significant difference, and about as many favored women as "
           "men (Bickel, Hammel & O'Connell, 1975).", y=-0.2)
    save(fig, "f11-13-simpson", mode)


# ---------------------------------------------------------------- F11.15 matrix sensitivity
def f11_15(mode):
    s = STYLE[mode]
    rows = read("ch11_matrix_sensitivity.csv")
    short = ["AI weights,\nblank = lowest", "AI weights,\nblank = mean", "AI weights,\nC left out",
             "Experience 20,\ntest 35", "Referral\nremoved", "Equal\nweights"]
    cands = ["A", "B", "C", "D", "E", "F"]
    markers = {"A": "o", "B": "s", "C": "^", "D": "D", "E": "P", "F": "X"}
    fig, ax = plt.subplots(figsize=(8.0, 4.4))
    for j, r in enumerate(rows):
        scores = {c: float(r[f"score {c}"]) for c in cands if r[f"score {c}"]}
        top = r["top candidate"]
        shortlist = r["shortlist of three"].split()
        for c, v in scores.items():
            on = c in shortlist
            ax.scatter(j + (cands.index(c) - 2.5) * 0.09, v, marker=markers[c], s=95 if c == top else 52,
                       facecolor=(s["main"] if on else "#FFFFFF"), edgecolor=s["ink"], linewidth=1.6 if c == top
                       else 1.0, zorder=3)
        ax.text(j, 8.05, f"top: {top}\n+{float(r['margin over second (0-10 scale)']):.2f}", ha="center",
                fontsize=10, fontweight="bold", color=s["ink"])
    for c in cands:
        ax.scatter([], [], marker=markers[c], s=52, facecolor="#FFFFFF", edgecolor=s["ink"], label=c)
    ax.legend(title="Candidate", frameon=False, loc="lower left", ncol=6, fontsize=10, title_fontsize=10)
    ax.set_xticks(range(len(rows)), short, fontsize=10)
    ax.set_ylim(2.5, 8.6)
    ax.set_ylabel("Weighted score (0–10)")
    title(ax, "The top spot changed with the weights, but only by near-ties;\nB and E stayed on every shortlist")
    source(fig, "Constructed internship shortlist (data/ch11_matrix_sensitivity.csv). Filled marker = on that run's "
           "shortlist of three; large marker = top;\n'+0.06' = the top candidate's lead over second place on the 0–10 "
           "scale.", y=-0.1)
    save(fig, "f11-15-matrix-sensitivity", mode)


# ---------------------------------------------------------------- F11.16 Dratsch
def f11_16(mode):
    s = STYLE[mode]
    rows = read("ch11_dratsch2023.csv")
    fig, ax = plt.subplots(figsize=(8.0, 3.8))
    w = 0.36
    for i, r in enumerate(rows):
        a, b = float(r["correct_when_ai_correct_pct"]), float(r["correct_when_ai_incorrect_pct"])
        ax.bar(i - w / 2, a, w, color=s["main"], edgecolor=s["ink"], hatch=s["hatch"], linewidth=1)
        ax.bar(i + w / 2, b, w, color=s["risk"], edgecolor=s["ink"], hatch=s["risk_hatch"], linewidth=1)
        ax.text(i - w / 2, a + 2, f"{a:.1f}%", ha="center", fontsize=11, color=s["ink"])
        ax.text(i + w / 2, b + 2, f"{b:.1f}%", ha="center", fontsize=11, color=s["ink"])
    ax.legend(handles=[Patch(facecolor=s["main"], edgecolor=s["ink"], hatch=s["hatch"], label="Suggested category correct"),
                       Patch(facecolor=s["risk"], edgecolor=s["ink"], hatch=s["risk_hatch"], label="Suggested category wrong")],
              frameon=False, loc="upper right", fontsize=10.5)
    ax.set_xticks(range(len(rows)), [r["experience_group"] for r in rows])
    ax.set_ylim(0, 110)
    ax.set_ylabel("Mammograms rated correctly (%)")
    title(ax, "When the suggested category was wrong, radiologists at every experience level\nrated far fewer "
          "mammograms correctly")
    source(fig, "Source: Dratsch et al. (2023), Radiology 307(4), e222176: 27 radiologists, 50 mammograms, a purported "
           "AI system that suggested\na wrong BI-RADS category for 12 of 40 test mammograms. Means per group.", y=-0.12)
    save(fig, "f11-16-dratsch", mode)


# ---------------------------------------------------------------- F11.17 Obermeyer enrollment
def f11_17(mode):
    s = STYLE[mode]
    rows = read("ch11_obermeyer_enrollment.csv")
    labels = ["Observed: doctors' decisions\nafter the score's screen", "Simulated: random within\neach score bin",
              "Simulated: most predicted chronic\nconditions within each bin", "Simulated: highest\npredicted cost",
              "Simulated: most predicted\nchronic conditions"]
    fig, ax = plt.subplots(figsize=(8.0, 4.2))
    for i, r in enumerate(rows):
        v = float(r["black_share"]) * 100
        observed = i == 0
        health = i in (2, 4)
        color = s["light"] if observed else (s["ok"] if health else s["main"])
        hatch = None if (observed or health) else s["hatch"]
        ax.barh(i, v, 0.6, color=color, edgecolor=s["ink"], hatch=hatch, linewidth=2.6 if observed else 1)
        ax.text(v + 0.5, i, f"{v:.1f}%", va="center", fontsize=11.5, fontweight="bold", color=s["ink"])
    ax.axvline(11.9, color=s["ink"], linestyle=":", linewidth=1.3)
    ax.text(12.2, -0.55, "Black share of the whole sample: 11.9%", fontsize=10, color=s["ink"])
    ax.set_yticks(range(len(rows)), labels, fontsize=10)
    ax.set_ylim(4.5, -0.85)
    ax.set_xlim(0, 36)
    ax.set_xlabel("Black patients among those enrolled or simulated as enrolled (%)")
    title(ax, "Selecting on predicted health raised the Black share\nfar more than doctors' review did")
    source(fig, "Source: Obermeyer et al. (2019), Science, text and Table 3. Simulations are the authors', on "
           "factors recorded in the data only; the observed 19.2%\ncannot be told apart from random-within-bin 18.3% "
           "(P = 0.83). Doctors saw only patients the score referred to them.", y=-0.12)
    save(fig, "f11-17-obermeyer-enrollment", mode)


if __name__ == "__main__":
    for mode in ("color", "gray"):
        for fn in (f11_5, f11_6, f11_9, f11_10, f11_13, f11_15, f11_16, f11_17):
            fn(mode)
    print("rendered f11-05, f11-06, f11-09, f11-10, f11-13, f11-15, f11-16, f11-17")
