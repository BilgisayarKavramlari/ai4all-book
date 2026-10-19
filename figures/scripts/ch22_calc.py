"""This book's calculation for section 22.6 (an illustration, not anyone's measured footprint).
Run from the repo root:  python3 figures/scripts/ch22_calc.py
Deterministic (no random numbers). Writes data/ch22_calc.csv.

Assumptions (printed in the chapter):
  - 30 text prompts a day (the book's choice for a heavy student user).
  - Per-prompt energy from data/ch22_prompt_energy.csv: 0.10 Wh (active chips only) and 0.24 Wh (full stack),
    both Google's 2025 median for its own text prompts; 0.3 Wh (Epoch AI's 2025 estimate for a typical query).
  - "Long reasoning answers": 10 times the full-stack figure (the book's assumption; no source measures it).
  - Laptop: 50 W for one hour = 50 Wh (the book's round number for a typical laptop in use).
"""
import csv
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PROMPTS = 30
LAPTOP_W = 50.0
CASES = [
    ("active chips only (Google, 2025)", 0.10),
    ("full serving stack (Google, 2025)", 0.24),
    ("typical query estimate (Epoch AI, 2025)", 0.30),
    ("long reasoning answers (book's assumption: 10 x 0.24)", 2.40),
]


def main():
    rows = []
    for label, wh in CASES:
        day = PROMPTS * wh
        rows.append({"case": label, "wh_per_prompt": f"{wh:.2f}", "prompts_per_day": PROMPTS,
                     "wh_per_day": f"{day:.1f}", "laptop_minutes_equivalent": f"{day / LAPTOP_W * 60:.0f}"})
    out = os.path.join(ROOT, "data", "ch22_calc.csv")
    with open(out, "w", newline="", encoding="utf8") as fh:
        fh.write("# This book's calculation (figures/scripts/ch22_calc.py): 30 prompts a day; laptop = 50 W. "
                 "Illustration only.\n")
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    for r in rows:
        print(r)


if __name__ == "__main__":
    main()
