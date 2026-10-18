"""Chapter 14 experiment: how errors compound over the steps of an agent run, and what check
points and an approval gate change. A constructed model, not data about any real agent.

Run from the repo root:
    python3 figures/scripts/ch14_experiments.py
Writes data/ch14_compounding.csv (closed form), data/ch14_gates_sim.csv (simulation) and
data/ch14_experiments_meta.txt (versions, seeds, assumptions).

Model (stated in the chapter as assumptions, not findings):
  * A run has N steps, each producing a correct result with probability p, independently.
  * Errors propagate: once a step is wrong, everything built on it is wrong until a person
    catches it and the work is redone from the wrong step.
  * A person's check catches a wrong result with probability c (the same at every check).
  * The run ends with one irreversible action (send, pay, delete). If it runs on a wrong
    result, that is counted as a harm.
  * When a check catches an error, the steps from the error onward are redone (each redo can
    fail again with probability 1 - p); a run is given up after MAX_PASSES caught passes and
    counted as "stopped" (no harm, task not done).
Designs compared:
  A  no person in the loop: the irreversible action runs at the end.
  B  one approval gate, just before the irreversible action.
  C  check points every K steps, plus the approval gate before the irreversible action.
"""
import csv
import os
import platform

import numpy as np

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA = os.path.join(ROOT, "data")

P_VALUES = [0.90, 0.95, 0.99]
N_MAX = 30
N = 20            # steps in the simulated run
P = 0.95          # per-step chance of a correct result in the simulation
C_VALUES = [0.5, 0.8]   # chance a person's check catches a wrong result
K = 5             # steps between check points in design C
MAX_PASSES = 5
RUNS = 20000
SEEDS = range(10)


def closed_form():
    rows = []
    for p in P_VALUES:
        for n in range(1, N_MAX + 1):
            rows.append({"p_step": p, "steps": n, "p_all_correct": round(p ** n, 4)})
    return rows


def simulate_run(rng, design, c):
    """Return (outcome, steps_redone, checks) for one run. outcome: correct | harm | stopped."""
    checkpoints = set(range(K, N, K)) if design == "C" else set()
    step = 0            # steps completed so far
    first_error = None  # index of the first wrong step in the current work, or None
    redone = 0
    checks = 0
    passes = 0
    while True:
        while step < N:
            step += 1
            if first_error is None and rng.random() > P:
                first_error = step
            if step in checkpoints:
                checks += 1
                if first_error is not None and rng.random() < c:
                    passes += 1
                    if passes > MAX_PASSES:
                        return "stopped", redone, checks
                    redone += step - first_error + 1
                    step = first_error - 1
                    first_error = None
        if design == "A":
            return ("correct" if first_error is None else "harm"), redone, checks
        checks += 1  # the approval gate before the irreversible action
        if first_error is not None and rng.random() < c:
            passes += 1
            if passes > MAX_PASSES:
                return "stopped", redone, checks
            redone += step - first_error + 1
            step = first_error - 1
            first_error = None
            continue
        return ("correct" if first_error is None else "harm"), redone, checks


def simulation():
    rows = []
    for c in C_VALUES:
        for design in ["A", "B", "C"]:
            if design == "A" and c != C_VALUES[0]:
                continue
            res = {"correct": [], "harm": [], "stopped": [], "redone": [], "checks": []}
            for seed in SEEDS:
                rng = np.random.default_rng(seed)
                out = [simulate_run(rng, design, c) for _ in range(RUNS)]
                for key in ["correct", "harm", "stopped"]:
                    res[key].append(np.mean([o[0] == key for o in out]))
                res["redone"].append(np.mean([o[1] for o in out]))
                res["checks"].append(np.mean([o[2] for o in out]))
            rows.append({
                "design": design,
                "catch_rate": "n/a" if design == "A" else c,
                "steps": N, "p_step": P, "check_every": K if design == "C" else "n/a",
                "pct_correct": round(100 * np.mean(res["correct"]), 1),
                "pct_harm": round(100 * np.mean(res["harm"]), 1),
                "pct_harm_sd_across_seeds": round(100 * np.std(res["harm"]), 2),
                "pct_stopped": round(100 * np.mean(res["stopped"]), 2),
                "mean_steps_redone": round(float(np.mean(res["redone"])), 2),
                "mean_person_checks": round(float(np.mean(res["checks"])), 2),
            })
    return rows


def write(name, rows):
    path = os.path.join(DATA, name)
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    return path


if __name__ == "__main__":
    write("ch14_compounding.csv", closed_form())
    sim = simulation()
    write("ch14_gates_sim.csv", sim)
    with open(os.path.join(DATA, "ch14_experiments_meta.txt"), "w") as fh:
        fh.write(f"python {platform.python_version()} · numpy {np.__version__}\n")
        fh.write(f"closed form: p in {P_VALUES}, steps 1-{N_MAX}, P(all correct) = p^n (independent steps)\n")
        fh.write(f"simulation: N={N}, p={P}, catch rates {C_VALUES}, check every {K} steps (design C), "
                 f"max {MAX_PASSES} caught passes, {RUNS} runs x seeds {list(SEEDS)}; numpy default_rng\n")
        fh.write("assumptions: independent step errors; errors propagate until caught; same catch rate at "
                 "every check; caught work redone from the first wrong step. A constructed model, not data "
                 "about any real agent.\n")
    for r in sim:
        print(r)
