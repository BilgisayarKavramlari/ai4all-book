"""Chapter 16 computed demos: this book's calculations, constructed for teaching; not data about any real system or group.

Run from the repo root:
    python3 figures/scripts/ch16_experiments.py
Writes:
  data/ch16_tradeoff_groups.csv   the constructed population (score bins, counts, share who needed help)
  data/ch16_tradeoff.csv          per-group metrics for every pair of group thresholds
  data/ch16_small_samples.csv     chance of a gap of 20+ points between two versions with NO real difference
  data/ch16_experiments_meta.txt  versions and assumptions

Demo 1 (fairness trade-off; sections 16.3 and Deep 16.A). An early-alert score for "will need
tutoring support" in two constructed groups, A and B, of 1,000 students each. The score is
calibrated in both groups by construction: in every score bin, the share who needed help equals
the score (of the students scored 0.7, 70% needed help, in A and in B). The groups differ only in
how many students fall in each bin, so their base rates differ (A 50%, B 30%). A student is
flagged when the score is at or above the group's threshold. For every pair of thresholds the
script reports, per group: selection rate (share flagged), false-positive rate (share of students
who did not need help who were flagged), false-negative rate or miss rate (share of students who
needed help who were not flagged) and precision (share of flagged students who needed help).
Exact counts; no randomness.

Demo 2 (small samples; section 16.2 and the bias probe). Two versions of a prompt each produce a
"yes" (for example, a stereotyped default) with the same true chance p = 0.5, so there is no real
difference. For n runs per version: (a) the exact binomial chance that the observed shares differ by
at least 20 percentage points; (b) the chance threshold: the smallest gap (in counts and in points)
that chance alone produces less than 1 time in 20 (ALPHA). p = 0.5 gives the widest spread of
chance gaps, so the thresholds are cautious for other true rates. Exact; no randomness.
"""
import csv
import os
import platform
from math import comb

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA = os.path.join(ROOT, "data")

SCORES = [0.1, 0.3, 0.5, 0.7, 0.9]
COUNTS = {"A": [150, 200, 300, 200, 150],   # base rate 50%
          "B": [450, 300, 100, 100, 50]}    # base rate 30%
N_VALUES = [5, 10, 15, 20, 25, 26, 30, 35, 39, 40, 45, 50, 65, 100, 200]
ALPHA = 0.05      # "less than 1 chance in 20"
GAP = 0.20
P_TRUE = 0.5


def group_metrics(group, threshold):
    flagged = tp = pos = 0
    total = sum(COUNTS[group])
    for s, n in zip(SCORES, COUNTS[group]):
        needed = round(s * n)
        pos += needed
        if s >= threshold - 1e-9:
            flagged += n
            tp += needed
    neg = total - pos
    fp = flagged - tp
    fn = pos - tp
    return {
        "group": group, "threshold": threshold, "n": total, "base_rate_pct": round(100 * pos / total, 1),
        "flagged": flagged, "true_pos": tp, "false_pos": fp, "false_neg": fn,
        "selection_rate_pct": round(100 * flagged / total, 1),
        "false_positive_rate_pct": round(100 * fp / neg, 1),
        "miss_rate_pct": round(100 * fn / pos, 1),
        "precision_pct": round(100 * tp / flagged, 1) if flagged else "",
    }


def tradeoff():
    rows = []
    for ta in SCORES:
        for tb in SCORES:
            a, b = group_metrics("A", ta), group_metrics("B", tb)
            row = {"threshold_A": ta, "threshold_B": tb}
            for g in (a, b):
                k = g["group"]
                for key in ["base_rate_pct", "selection_rate_pct", "false_positive_rate_pct",
                            "miss_rate_pct", "precision_pct"]:
                    row[f"{key}_{k}"] = g[key]
            rows.append(row)
    return rows


def binom_pmf(k, n, p):
    return comb(n, k) * p ** k * (1 - p) ** (n - k)


def gap_tail(n):
    """Exact distribution of |k1 - k2| for two Binomial(n, P_TRUE) counts; returns tail(d) = P(|gap| >= d)."""
    pmf = [binom_pmf(k, n, P_TRUE) for k in range(n + 1)]
    dist = [0.0] * (n + 1)
    for k1 in range(n + 1):
        for k2 in range(n + 1):
            dist[abs(k1 - k2)] += pmf[k1] * pmf[k2]
    return lambda d: sum(dist[d:])


def small_samples():
    rows = []
    for n in N_VALUES:
        tail = gap_tail(n)
        d20 = next(d for d in range(n + 1) if d / n >= GAP - 1e-12)
        d_thr = next(d for d in range(n + 1) if tail(d) < ALPHA)
        rows.append({"runs_per_version": n, "true_rate_both": P_TRUE, "gap_points": int(GAP * 100),
                     "pct_chance_gap_or_more": round(100 * tail(d20), 1),
                     "threshold_gap_count": d_thr,
                     "threshold_gap_points": round(100 * d_thr / n, 1),
                     "pct_chance_at_threshold": round(100 * tail(d_thr), 2)})
    return rows


def write(name, rows):
    with open(os.path.join(DATA, name), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


def main():
    groups = []
    for g, counts in COUNTS.items():
        for s, n in zip(SCORES, counts):
            groups.append({"group": g, "score": s, "students": n, "needed_help": round(s * n)})
    write("ch16_tradeoff_groups.csv", groups)
    write("ch16_tradeoff.csv", tradeoff())
    write("ch16_small_samples.csv", small_samples())
    with open(os.path.join(DATA, "ch16_experiments_meta.txt"), "w") as fh:
        fh.write(f"python {platform.python_version()} · standard library only (math.comb); exact, no seeds\n")
        fh.write(f"demo 1: score bins {SCORES}; counts {COUNTS}; calibrated by construction "
                 "(share needing help in a bin = its score); flag if score >= threshold\n")
        fh.write(f"demo 2: true rate {P_TRUE} in both versions; chance of a gap >= {int(GAP*100)} points; "
                 f"threshold = smallest gap with chance < {ALPHA}; runs {N_VALUES}\n")
        fh.write("This book's calculations, constructed for teaching; not data about any real system or group.\n")


if __name__ == "__main__":
    main()
