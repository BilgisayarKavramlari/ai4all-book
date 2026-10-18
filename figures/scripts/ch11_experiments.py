"""Chapter 11 experiments: reproducible numbers for the missing-value, proxy and decision-matrix demos.

All data are CONSTRUCTED or SIMULATED for teaching; no real people, events or patients.
Run from the repo root:
    python3 figures/scripts/ch11_experiments.py
Writes:
    data/ch11_events.csv              Lucía's constructed volunteer-shift table (true hours kept in a separate column)
    data/ch11_missing_choices.csv     per-event $/volunteer-hour and the "best" event under each missing-value choice
    data/ch11_missing_sim.csv         share of 1,000 simulated datasets in which each choice picks the truly best event,
                                      when blanks are random (MCAR) and when long shifts go unlogged (MNAR)
    data/ch11_proxy_sim.csv           simulated selection of the top 3% by a cost proxy vs. by need, as the access gap grows
    data/ch11_matrix.csv              constructed hiring-shortlist decision matrix (candidates A-F)
    data/ch11_matrix_sensitivity.csv  top candidate and shortlist under weight and missing-value changes
    data/ch11_experiments_meta.txt    versions, seeds and parameters
"""
import csv
import os
import platform

import numpy as np

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA = os.path.join(ROOT, "data")
EVENTS = ["Bake sale", "Book swap", "Budget workshop"]

# ------------------------------------------------------------------ 1. Lucía's events (constructed)
# (event, shift, true_hours, proceeds, hours_logged?)  proceeds in dollars, net of costs
SHIFTS = [
    ("Bake sale", 1, 8, 144, True), ("Bake sale", 2, 9, 162, True), ("Bake sale", 3, 10, 180, True),
    ("Bake sale", 4, 8, 144, True), ("Bake sale", 5, 9, 162, True), ("Bake sale", 6, 10, 180, True),
    ("Book swap", 1, 6, 150, True), ("Book swap", 2, 7, 168, True), ("Book swap", 3, 14, 210, False),
    ("Book swap", 4, 6, 144, True), ("Book swap", 5, 13, 195, False), ("Book swap", 6, 8, 192, True),
    ("Budget workshop", 1, 10, 225, True), ("Budget workshop", 2, 10, 225, True),
    ("Budget workshop", 3, 11, 248, True), ("Budget workshop", 4, 9, 202, True),
    ("Budget workshop", 5, 10, 225, True), ("Budget workshop", 6, 10, 225, True),
]
CHOICES = ["true hours (known only in this demo)", "blank = 0 (total proceeds / total logged hours)",
           "drop rows with a blank (listwise deletion)", "fill with the mean of all logged shifts",
           "fill with the event's own mean", "copy the previous shift (last observation carried forward)"]


def rates(rows, choice):
    """rows: list of (event, true_hours, proceeds, logged_hours or None) in shift order."""
    logged_all = [h for _, _, _, h in rows if h is not None]
    out = {}
    for ev in EVENTS:
        r = [x for x in rows if x[0] == ev]
        if choice == 0:
            hrs, pro = sum(x[1] for x in r), sum(x[2] for x in r)
        elif choice == 1:
            hrs, pro = sum(x[3] or 0 for x in r), sum(x[2] for x in r)
        elif choice == 2:
            kept = [x for x in r if x[3] is not None]
            hrs, pro = sum(x[3] for x in kept), sum(x[2] for x in kept)
        elif choice == 3:
            m = np.mean(logged_all)
            hrs, pro = sum(x[3] if x[3] is not None else m for x in r), sum(x[2] for x in r)
        elif choice == 4:
            ev_logged = [x[3] for x in r if x[3] is not None]
            m = np.mean(ev_logged) if ev_logged else np.mean(logged_all)
            hrs, pro = sum(x[3] if x[3] is not None else m for x in r), sum(x[2] for x in r)
        else:
            prev, hrs = None, 0.0
            for x in r:
                h = x[3] if x[3] is not None else (prev if prev is not None else np.mean(logged_all))
                hrs += h
                prev = h
            pro = sum(x[2] for x in r)
        out[ev] = pro / hrs if hrs else float("nan")
    return out


def lucia_table():
    rows = [(e, h, p, h if logged else None) for e, _, h, p, logged in SHIFTS]
    with open(os.path.join(DATA, "ch11_events.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["event", "shift", "proceeds_usd", "hours_logged", "true_hours_demo_only"])
        for e, s, h, p, logged in SHIFTS:
            w.writerow([e, s, p, h if logged else "", h])
    with open(os.path.join(DATA, "ch11_missing_choices.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["choice"] + [f"{e} ($/h)" for e in EVENTS] + ["best event"])
        for i, c in enumerate(CHOICES):
            r = rates(rows, i)
            best = max(r, key=r.get)
            w.writerow([c] + [f"{r[e]:.1f}" for e in EVENTS] + [best])
            print(f"  {c:62s}", "  ".join(f"{r[e]:6.1f}" for e in EVENTS), "->", best)


# ------------------------------------------------------------------ 2. simulation over many datasets
SIM_N, SIM_SEED, SHIFTS_PER_EVENT, MISSING_SHARE = 1000, 11, 8, 0.25


def simulate(mechanism, rng):
    rows = []
    base_rate = {"Bake sale": rng.normal(18, 2), "Book swap": rng.normal(20, 2), "Budget workshop": rng.normal(21, 2)}
    for ev in EVENTS:
        hours = np.clip(rng.normal(9, 3, SHIFTS_PER_EVENT), 3, 16).round()
        # longer shifts earn less per hour (traffic fades late in the day)
        rate = base_rate[ev] * (1.15 - 0.03 * (hours - 9))
        proceeds = (rate * hours * rng.normal(1, 0.08, SHIFTS_PER_EVENT)).round()
        if mechanism == "MCAR":
            miss = rng.random(SHIFTS_PER_EVENT) < MISSING_SHARE
        else:  # MNAR: the longer the shift, the likelier it went unlogged
            p = np.clip(MISSING_SHARE * (hours - 3) / 6, 0, 0.9)
            miss = rng.random(SHIFTS_PER_EVENT) < p
        for h, pr, m in zip(hours, proceeds, miss):
            rows.append((ev, float(h), float(pr), None if m else float(h)))
    return rows


def simulation():
    rng = np.random.default_rng(SIM_SEED)
    res = {mech: np.zeros(len(CHOICES)) for mech in ("MCAR", "MNAR")}
    for mech in res:
        for _ in range(SIM_N):
            rows = simulate(mech, rng)
            truth = rates(rows, 0)
            best = max(truth, key=truth.get)
            for i in range(1, len(CHOICES)):
                r = rates(rows, i)
                res[mech][i] += max(r, key=r.get) == best
    with open(os.path.join(DATA, "ch11_missing_sim.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["choice", "share right when blanks are random (MCAR)", "share right when long shifts go unlogged (MNAR)"])
        for i in range(1, len(CHOICES)):
            w.writerow([CHOICES[i], f"{res['MCAR'][i] / SIM_N:.3f}", f"{res['MNAR'][i] / SIM_N:.3f}"])
            print(f"  {CHOICES[i]:62s} MCAR {res['MCAR'][i] / SIM_N:.3f}  MNAR {res['MNAR'][i] / SIM_N:.3f}")


# ------------------------------------------------------------------ 3. proxy simulation (mechanism only)
POP, SHARE_B, TOP, PROXY_SEEDS = 20000, 0.12, 0.03, range(50)
GAPS = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]


def proxy_sim():
    rows = []
    for gap in GAPS:
        b_cost, b_need, missed = [], [], []
        for s in PROXY_SEEDS:
            rng = np.random.default_rng(1000 + s)
            group_b = rng.random(POP) < SHARE_B
            need = rng.lognormal(0, 0.6, POP)                   # same distribution of need in both groups
            access = np.where(group_b, 1 - gap, 1.0)             # group B gets less care for the same need
            cost = need * access * rng.lognormal(0, 0.3, POP)    # spending = need x access x noise
            k = int(TOP * POP)
            by_cost = np.argsort(-cost)[:k]
            by_need = np.argsort(-need)[:k]
            b_cost.append(group_b[by_cost].mean())
            b_need.append(group_b[by_need].mean())
            missed.append(1 - len(set(by_cost) & set(by_need)) / k)
        rows.append([gap, np.mean(b_need), np.mean(b_cost), np.mean(missed)])
        print(f"  gap {gap:.1f}: group B share by need {np.mean(b_need):.3f}, by cost {np.mean(b_cost):.3f}, "
              f"top-need people not selected by cost {np.mean(missed):.3f}")
    with open(os.path.join(DATA, "ch11_proxy_sim.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["access_gap_group_B", "group_B_share_selected_by_need", "group_B_share_selected_by_cost",
                    "share_of_highest_need_not_selected_by_cost"])
        for r in rows:
            w.writerow([f"{r[0]:.1f}"] + [f"{v:.3f}" for v in r[1:]])


# ------------------------------------------------------------------ 4. decision matrix (constructed)
CRITERIA = ["Skills test (0-100)", "Structured interview (1-5)", "Years of experience",
            "GPA (0-4)", "Employee referral (1 = yes)"]
AI_WEIGHTS = [25, 25, 30, 10, 10]          # weights proposed in the constructed AI output
CANDIDATES = {                              # None = not yet recorded
    "A": [88, 4.5, 1, 3.6, 0],
    "B": [72, 3.5, 6, 3.1, 1],
    "C": [91, None, 2, 3.8, 0],             # interview not yet held
    "D": [80, 4.0, 3, 3.3, 1],
    "E": [65, 3.0, 8, 2.9, 1],
    "F": [84, 4.5, 2, 3.4, 0],
}
RANGES = [(0, 100), (1, 5), (0, 10), (0, 4), (0, 1)]   # scaling: (value - lo) / (hi - lo) * 10


def score(vals, weights, missing="zero"):
    tot = 0.0
    for v, wgt, (lo, hi), col in zip(vals, weights, RANGES, range(len(weights))):
        if v is None:
            if missing == "zero":
                v = lo
            elif missing == "mean":
                others = [c[col] for c in CANDIDATES.values() if c[col] is not None]
                v = float(np.mean(others))
            else:
                return None
        tot += wgt / 100 * (v - lo) / (hi - lo) * 10
    return tot


def matrix():
    with open(os.path.join(DATA, "ch11_matrix.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["candidate"] + CRITERIA)
        for k, v in CANDIDATES.items():
            w.writerow([k] + ["" if x is None else x for x in v])
    scen = [("AI weights, blank interview = lowest score", AI_WEIGHTS, "zero"),
            ("AI weights, blank interview = mean of others", AI_WEIGHTS, "mean"),
            ("AI weights, candidate C left out until interviewed", AI_WEIGHTS, "drop"),
            ("Experience 20, test 35 (others unchanged), blank = mean", [35, 25, 20, 10, 10], "mean"),
            ("Referral removed, its 10 points to the interview, blank = mean", [25, 35, 30, 10, 0], "mean"),
            ("Equal weights (20 each), blank = mean", [20, 20, 20, 20, 20], "mean")]
    out = []
    for name, wts, miss in scen:
        sc = {k: score(v, wts, miss) for k, v in CANDIDATES.items()}
        sc = {k: s for k, s in sc.items() if s is not None}
        ranked = sorted(sc, key=sc.get, reverse=True)
        out.append([name, "/".join(map(str, wts)), ranked[0], " ".join(ranked[:3]),
                    " ".join(f"{k}={sc[k]:.2f}" for k in ranked)])
        print(f"  {name:66s} top {ranked[0]}  shortlist {' '.join(ranked[:3])}  | {out[-1][-1]}")
    with open(os.path.join(DATA, "ch11_matrix_sensitivity.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["scenario", "weights (test/interview/experience/GPA/referral)", "top candidate",
                    "shortlist of three", "scores (0-10)"])
        w.writerows(out)


if __name__ == "__main__":
    print("1. Lucía's events ($ per volunteer hour)")
    lucia_table()
    print("2. Simulation")
    simulation()
    print("3. Proxy simulation")
    proxy_sim()
    print("4. Decision matrix")
    matrix()
    with open(os.path.join(DATA, "ch11_experiments_meta.txt"), "w") as f:
        f.write(f"python {platform.python_version()} · numpy {np.__version__}\n")
        f.write("events: constructed 18-shift table; Book swap shifts 3 and 5 (14 h, 13 h) unlogged; "
                "rates = total proceeds / total hours per event\n")
        f.write(f"missing-value simulation: {SIM_N} datasets per mechanism, seed {SIM_SEED}, "
                f"{SHIFTS_PER_EVENT} shifts per event, missing share {MISSING_SHARE}; MNAR probability rises with "
                "shift length; long shifts earn less per hour\n")
        f.write(f"proxy simulation: population {POP}, group B share {SHARE_B}, top {TOP:.0%} selected, "
                f"need ~ lognormal(0, 0.6), cost = need x access x lognormal(0, 0.3), seeds 1000-1049; "
                "mechanism only, not Obermeyer et al.'s data\n")
        f.write("decision matrix: constructed candidates A-F; each criterion scaled to 0-10 by fixed ranges, "
                "weighted sum; scenarios as in ch11_matrix_sensitivity.csv\n")
