"""Chapter 8: build the constructed calibration record (data/ch08_calibration_toy.csv).
Run from the repo root:  python3 figures/scripts/ch08_experiments.py

CONSTRUCTED DATA FOR TEACHING, not a measurement of any real tool. Thirty known-answer items with a
stated confidence and whether the answer was correct. The values are fixed (no randomness), chosen to
match the published pattern: stated confidence mostly 80-100% (Xiong et al., 2024) and above accuracy
while still rising with it (Wei et al., 2024). Python standard library only.
"""
import csv
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# (stated confidence %, number of items, number correct) per confidence value
SPEC = [(55, 1, 0), (60, 2, 1), (65, 2, 1),                      # 50-69%: 5 items, 2 correct
        (70, 1, 1), (75, 2, 1), (80, 3, 2), (85, 4, 1),          # 70-89%: 10 items, 5 correct
        (90, 5, 3), (95, 7, 4), (100, 3, 2)]                     # 90-100%: 15 items, 9 correct
GROUPS = [("50-69%", 50, 69), ("70-89%", 70, 89), ("90-100%", 90, 100)]


def main():
    rows, i = [], 0
    for conf, n, k in SPEC:
        for j in range(n):
            i += 1
            rows.append({"item": i, "stated_confidence": conf, "correct": 1 if j < k else 0})
    out = os.path.join(ROOT, "data", "ch08_calibration_toy.csv")
    with open(out, "w", newline="", encoding="utf8") as fh:
        w = csv.DictWriter(fh, fieldnames=["item", "stated_confidence", "correct"])
        w.writeheader()
        w.writerows(rows)
    summ = []
    for name, lo, hi in GROUPS:
        g = [r for r in rows if lo <= r["stated_confidence"] <= hi]
        mean_conf = sum(r["stated_confidence"] for r in g) / len(g)
        acc = 100 * sum(r["correct"] for r in g) / len(g)
        summ.append({"group": name, "n_items": len(g), "n_correct": sum(r["correct"] for r in g),
                     "mean_stated_confidence": round(mean_conf, 1), "share_correct_pct": round(acc, 1)})
    with open(os.path.join(ROOT, "data", "ch08_calibration_groups.csv"), "w", newline="", encoding="utf8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(summ[0]))
        w.writeheader()
        w.writerows(summ)
    for s in summ:
        print(s)


if __name__ == "__main__":
    main()
