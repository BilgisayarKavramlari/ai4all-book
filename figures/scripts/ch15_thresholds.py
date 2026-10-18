"""Chance thresholds for Lab 15.1's pooled bias tallies (this book's calculation; same method as Chapter 16, D-16.3).
For n runs per version with both versions at a true rate of 50%, the threshold is the smallest gap g (in runs) such that
P(|X - Y| >= g) < 0.05, with X, Y ~ Binomial(n, 0.5) independent, computed exactly. Run from the repo root:
    python3 figures/scripts/ch15_thresholds.py   -> data/ch15_lab_thresholds.csv
"""
import csv
import os
from math import comb

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def p_gap(n, g):
    pm = [comb(n, k) / 2 ** n for k in range(n + 1)]
    return sum(pm[x] * pm[y] for x in range(n + 1) for y in range(n + 1) if abs(x - y) >= g)


rows = []
for n in (20, 25, 26, 30, 35, 39, 40, 45):
    g = next(g for g in range(n + 1) if p_gap(n, g) < 0.05)
    rows.append({"runs_per_version": n, "threshold_gap_runs": g, "threshold_gap_points": round(100 * g / n, 1),
                 "pct_chance_at_threshold": round(100 * p_gap(n, g), 2)})
with open(os.path.join(ROOT, "data", "ch15_lab_thresholds.csv"), "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0]))
    w.writeheader()
    w.writerows(rows)
print(rows)
