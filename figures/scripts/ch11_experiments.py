"""Chapter 11 experiments: reproducible numbers for the missing-value, proxy and decision-matrix demos.

All data are CONSTRUCTED or SIMULATED for teaching; no real people, events or patients.
Run from the repo root:
    python3 figures/scripts/ch11_experiments.py
Writes:
    data/ch11_events.csv              Lucia's constructed volunteer-shift table (true hours kept in a separate column)
    data/ch11_missing_choices.csv     per-event $/volunteer-hour and the "best" event under each missing-value choice
    data/ch11_missing_sim.csv         share of 1,000 simulated datasets in which each choice picks the truly best event,
                                      when blanks fall at random in every event and when they fall only at one
                                      event, mostly on its long shifts
    data/ch11_proxy_sim.csv           simulated selection of the top 3% by a cost proxy vs. by need, as the access gap grows
    data/ch11_matrix.csv              constructed hiring-shortlist decision matrix (candidates A-F)
    data/ch11_matrix_sensitivity.csv  top candidate, margin over second place and shortlist under each scenario
    data/ch11_scenario_a.csv          A9 scenario A' (unsolved): internship candidates G-L for students
    data/ch11_scenario_b.csv          A9 scenario B' (unsolved): three spring fundraisers x five criteria for students
    private/ch11-a9-key.md            instructor key for A' and B' (never committed; private/ is git-ignored)
    data/ch11_experiments_meta.txt    versions, seeds and parameters
    data/ch11_matrix_template.xlsx    spreadsheet template (instructor package): the A-F demo with formulas, and a
                                      blank matrix with fixed-range scaling, "lower is better" reversal and blank flags
"""
import csv
import os
import platform

import numpy as np

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA = os.path.join(ROOT, "data")
EVENTS = ["Bake sale", "Book swap", "Car wash"]

# ------------------------------------------------------------------ 1. Lucia's events (constructed)
# (event, shift, true_hours, proceeds, hours_logged?)  proceeds in dollars, net of costs
SHIFTS = [
    ("Bake sale", 1, 8, 144, True), ("Bake sale", 2, 9, 162, True), ("Bake sale", 3, 10, 180, True),
    ("Bake sale", 4, 8, 144, True), ("Bake sale", 5, 9, 162, True), ("Bake sale", 6, 10, 180, True),
    ("Book swap", 1, 6, 150, True), ("Book swap", 2, 7, 168, True), ("Book swap", 3, 14, 210, False),
    ("Book swap", 4, 6, 144, True), ("Book swap", 5, 13, 195, False), ("Book swap", 6, 8, 192, True),
    ("Car wash", 1, 10, 225, True), ("Car wash", 2, 10, 225, True),
    ("Car wash", 3, 11, 248, True), ("Car wash", 4, 9, 202, True),
    ("Car wash", 5, 10, 225, True), ("Car wash", 6, 10, 225, True),
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
            w.writerow([c] + [f"{r[e]:.2f}" for e in EVENTS] + [best])
            print(f"  {c:62s}", "  ".join(f"{r[e]:6.1f}" for e in EVENTS), "->", best)


# ------------------------------------------------------------------ 2. simulation over many datasets
SIM_N, SIM_SEED, SHIFTS_PER_EVENT, MISSING_SHARE = 1000, 11, 8, 0.25


def simulate(mechanism, rng):
    """mechanism "spread": blanks at random in every event (each shift 25%).
    mechanism "one_event": blanks only at the book swap, more often on its long shifts."""
    rows = []
    base_rate = {"Bake sale": rng.normal(18, 2), "Book swap": rng.normal(20, 2), "Car wash": rng.normal(21, 2)}
    for ev in EVENTS:
        hours = np.clip(rng.normal(9, 3, SHIFTS_PER_EVENT), 3, 16).round()
        # longer shifts earn less per hour (traffic fades late in the day)
        rate = base_rate[ev] * (1.15 - 0.03 * (hours - 9))
        proceeds = (rate * hours * rng.normal(1, 0.08, SHIFTS_PER_EVENT)).round()
        if mechanism == "spread":
            miss = rng.random(SHIFTS_PER_EVENT) < MISSING_SHARE
        elif ev == "Book swap":  # the longer the shift, the likelier it went unlogged
            p = np.clip(2 * MISSING_SHARE * (hours - 3) / 6, 0, 0.9)
            miss = rng.random(SHIFTS_PER_EVENT) < p
        else:
            miss = np.zeros(SHIFTS_PER_EVENT, dtype=bool)
        for h, pr, m in zip(hours, proceeds, miss):
            rows.append((ev, float(h), float(pr), None if m else float(h)))
    return rows


def simulation():
    rng = np.random.default_rng(SIM_SEED)
    res = {mech: np.zeros(len(CHOICES)) for mech in ("spread", "one_event")}
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
        w.writerow(["choice", "share right: blanks at random in every event",
                    "share right: blanks only at one event, mostly its long shifts"])
        for i in range(1, len(CHOICES)):
            w.writerow([CHOICES[i], f"{res['spread'][i] / SIM_N:.3f}", f"{res['one_event'][i] / SIM_N:.3f}"])
            print(f"  {CHOICES[i]:62s} spread {res['spread'][i] / SIM_N:.3f}  one event {res['one_event'][i] / SIM_N:.3f}")


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
        out.append([name, "/".join(map(str, wts)), ranked[0], f"{sc[ranked[0]] - sc[ranked[1]]:.2f}",
                    " ".join(ranked[:3])] + [f"{sc[k]:.2f}" if k in sc else "" for k in CANDIDATES])
        print(f"  {name:66s} top {ranked[0]} (+{sc[ranked[0]] - sc[ranked[1]]:.2f})  shortlist {' '.join(ranked[:3])}")
    with open(os.path.join(DATA, "ch11_matrix_sensitivity.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["scenario", "weights (test/interview/experience/GPA/referral)", "top candidate",
                    "margin over second (0-10 scale)", "shortlist of three"] + [f"score {k}" for k in CANDIDATES])
        w.writerows(out)
    on_list = {k: sum(k in r[4].split() for r in out) for k in CANDIDATES}
    print("  shortlist appearances across", len(out), "scenarios:", on_list)


# ------------------------------------------------------------------ 5. A9 scenario files (unsolved for students)
A_CRIT = ["Work-sample task (0-100)", "Structured interview (1-5)", "GPA (0-4)",
          "Hours available per week", "Attended a partner university (1 = yes)"]
A_RANGES = [(0, 100), (1, 5), (0, 4), (0, 20), (0, 1)]
A_CANDS = {"G": [78, 4.0, 3.2, 15, 1], "H": [90, 4.5, None, 12, 0],      # H: transfer student, no GPA here yet
           "I": [70, 3.5, 3.7, 20, 1], "J": [85, None, 3.4, 15, 0],      # J: interview not yet held
           "K": [74, 4.0, 3.0, 18, 1], "L": [82, 3.5, 3.5, 10, 0]}
A_TRY = [("Even-looking weights 30/25/20/10/15, blanks = lowest", [30, 25, 20, 10, 15], "zero"),
         ("Same weights, blanks = mean of others", [30, 25, 20, 10, 15], "mean"),
         ("Partner-university flag removed, its 15 to the work sample", [45, 25, 20, 10, 0], "mean"),
         ("Equal weights, blanks = mean", [20, 20, 20, 20, 20], "mean")]
B_CRIT = ["Expected net proceeds ($)", "Volunteer hours needed (lower is better)",
          "Weather risk (1 low - 3 high; lower is better)", "Members who said they would help (survey)",
          "Fit with the association's mission (board rating 1-5)"]
B_OPTS = {"Trivia night": [620, 40, 1, 9, 3], "Plant sale": [None, 30, 3, 6, 4],  # new event: no history
          "Graduation photo booth": [900, 55, 2, None, 4]}                       # survey did not ask about it
B_BETTER_LOW = [False, True, True, False, False]
B_TRY = [("Weights 35/20/15/15/15, blanks = worst", [35, 20, 15, 15, 15], "zero"),
         ("Same weights, blanks = mean of others", [35, 20, 15, 15, 15], "mean"),
         ("Proceeds 20, mission 30", [20, 20, 15, 15, 30], "mean"),
         ("Equal weights, blanks = mean", [20, 20, 20, 20, 20], "mean")]


def generic_scores(opts, wts, ranges, missing, better_low=None):
    cols = list(zip(*opts.values()))
    out = {}
    for name, vals in opts.items():
        tot = 0.0
        for j, v in enumerate(vals):
            lo, hi = ranges[j]
            present = [c for c in cols[j] if c is not None]
            if v is None:
                v = float(np.mean(present)) if missing == "mean" else (hi if better_low and better_low[j] else lo)
            x = (v - lo) / (hi - lo)
            if better_low and better_low[j]:
                x = 1 - x
            tot += wts[j] / 100 * x * 10
        out[name] = tot
    return out


def scenarios():
    with open(os.path.join(DATA, "ch11_scenario_a.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["candidate"] + A_CRIT)
        for k, v in A_CANDS.items():
            w.writerow([k] + ["" if x is None else x for x in v])
    with open(os.path.join(DATA, "ch11_scenario_b.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["option"] + B_CRIT)
        for k, v in B_OPTS.items():
            w.writerow([k] + ["" if x is None else x for x in v])
    b_ranges = []
    for j in range(len(B_CRIT)):
        present = [v[j] for v in B_OPTS.values() if v[j] is not None]
        b_ranges.append({0: (0, 1000), 1: (0, 60), 2: (1, 3), 3: (0, 12), 4: (1, 5)}[j])
    lines = ["# Chapter 11 — A9 scenario key (instructor only; generated by figures/scripts/ch11_experiments.py)", "",
             "Scaling: each criterion to 0-10 by fixed ranges; weighted sum; one illustrative set of tests. "
             "Students may choose other defensible weights and scales; grade the audit, not the ranking.", ""]
    for label, opts, crit, ranges, tries, bl in [("A' internship shortlist (G-L)", A_CANDS, A_CRIT, A_RANGES, A_TRY, None),
                                                 ("B' spring fundraiser", B_OPTS, B_CRIT, b_ranges, B_TRY, B_BETTER_LOW)]:
        lines += [f"## {label}", "", "| Test | Ranking (score) | Top margin |", "|---|---|---|"]
        for name, wts, miss in tries:
            sc = generic_scores(opts, wts, ranges, miss, bl)
            r = sorted(sc, key=sc.get, reverse=True)
            lines.append(f"| {name} | {', '.join(f'{k} {sc[k]:.2f}' for k in r)} | {sc[r[0]] - sc[r[1]]:.2f} |")
            print(f"  {label[:3]} {name:62s} -> {r[0]} (+{sc[r[0]] - sc[r[1]]:.2f}) | {' '.join(r)}")
        lines.append("")
    lines += ["Hidden assumptions students should find:",
              "- A': H's blank GPA (transfer student) and J's blank interview (not yet held) — scoring a blank as the lowest "
              "value penalizes the candidate for the firm's own missing step; the fix is to get the value (hold the "
              "interview; ask for the transcript), not to pick a fill. The partner-university flag is a proxy (for "
              "preparation or fit) that tracks where someone studied; GPA scales differ across universities.",
              "- A': candidate L offers 10 hours a week, but the firm needs at least 12. That is an eligibility rule, "
              "not a weighted criterion: a matrix that scores hours on a scale lets L trade hours for other strengths; "
              "students should screen L out (or ask L) before scoring.",
              "- B': the plant sale has no proceeds history (new event) and the photo booth was not on the survey; the "
              "survey count comes from 14 of about 60 members (a sample that volunteered). 'Lower is better' criteria "
              "must be reversed; an AI-drafted matrix that adds raw hours or weather scores is a check-6 (formula) error.",
              "", "## Observations moved from Lab 11.1 (instructor only)",
              "In A', the partner-university flag can decide the top spot: removing it moves H from fourth or fifth "
              "to first in the illustrative tests above. Both blanks have reasons the firm controls (an interview not "
              "yet held, a transcript not yet received), so the right move is to get the values, not to pick a fill. "
              "In B', once blanks are handled with the mean the margins are small (0.08 and 0.13 on the 0-10 scale in "
              "two of four tests). The survey count comes from 14 of about 60 members, a self-selected sample. Matrices "
              "that do not reverse the two 'lower is better' criteria rank the options on the wrong basis."]
    os.makedirs(os.path.join(ROOT, "private"), exist_ok=True)
    with open(os.path.join(ROOT, "private", "ch11-a9-key.md"), "w") as f:
        f.write("\n".join(lines) + "\n")


def xlsx_template():
    """Spreadsheet template: scaled score = (value - low) / (high - low) x 10; "lower is better" = 10 - that;
    a blank shows BLANK and blocks the total until you decide how to handle it."""
    try:
        from openpyxl import Workbook
    except ImportError:
        print("  openpyxl not installed: template skipped")
        return
    from openpyxl.utils import get_column_letter as L
    wb = Workbook()

    def sheet(ws, names, crit, ranges, lower, weights, values):
        n = len(crit)
        ws["A1"] = "Decision matrix: fixed-range scaling to 0-10; weights in percent (must sum to 100)"
        ws["A3"], ws["A4"], ws["A5"], ws["A6"] = "Criterion", "Low end of scale", "High end of scale", "Lower is better? (yes/no)"
        ws["A7"] = "Weight (%)"
        for j in range(n):
            c = L(j + 2)
            ws[f"{c}3"], ws[f"{c}4"], ws[f"{c}5"] = crit[j], ranges[j][0], ranges[j][1]
            ws[f"{c}6"], ws[f"{c}7"] = "yes" if lower[j] else "no", weights[j]
        ws[f"{L(n + 2)}7"] = f"=SUM(B7:{L(n + 1)}7)"
        ws["A9"] = "Option"
        for j in range(n):
            ws[f"{L(j + 2)}9"] = crit[j] + " (raw)"
            ws[f"{L(n + j + 2)}9"] = crit[j] + " (scaled 0-10)"
        ws[f"{L(2 * n + 2)}9"] = "Weighted total (0-10)"
        for i, name in enumerate(names):
            r = 10 + i
            ws[f"A{r}"] = name
            for j in range(n):
                v = values[i][j] if values else None
                if v is not None:
                    ws[f"{L(j + 2)}{r}"] = v
                raw, c = f"{L(j + 2)}{r}", L(j + 2)
                ws[f"{L(n + j + 2)}{r}"] = (f'=IF(ISBLANK({raw}),"BLANK",IF(${c}$6="yes",10-({raw}-${c}$4)/(${c}$5-${c}$4)*10,'
                                            f'({raw}-${c}$4)/(${c}$5-${c}$4)*10))')
            sc = f"{L(n + 2)}{r}:{L(2 * n + 1)}{r}"
            ws[f"{L(2 * n + 2)}{r}"] = (f'=IF(COUNTIF({sc},"BLANK")>0,"decide how to handle the blank",'
                                        f'SUMPRODUCT({sc},$B$7:${L(n + 1)}$7)/100)')

    ws = wb.active
    ws.title = "Chapter demo A-F"
    sheet(ws, list(CANDIDATES), CRITERIA, RANGES, [False] * 5, AI_WEIGHTS, list(CANDIDATES.values()))
    ws2 = wb.create_sheet("Your matrix")
    sheet(ws2, [f"Option {k}" for k in "123456"], [f"Criterion {k}" for k in "12345"], [(0, 10)] * 5, [False] * 5,
          [20] * 5, None)
    wb.save(os.path.join(DATA, "ch11_matrix_template.xlsx"))


if __name__ == "__main__":
    print("1. Lucia's events ($ per volunteer hour)")
    lucia_table()
    print("2. Simulation")
    simulation()
    print("3. Proxy simulation")
    proxy_sim()
    print("4. Decision matrix")
    matrix()
    print("5. A9 scenario files (key -> private/ch11-a9-key.md)")
    scenarios()
    print("6. Spreadsheet template")
    xlsx_template()
    with open(os.path.join(DATA, "ch11_experiments_meta.txt"), "w") as f:
        f.write(f"python {platform.python_version()} · numpy {np.__version__}\n")
        f.write("events: constructed 18-shift table; Book swap shifts 3 and 5 (14 h, 13 h) unlogged; "
                "rates = total proceeds / total hours per event\n")
        f.write(f"missing-value simulation: {SIM_N} datasets per mechanism, seed {SIM_SEED}, "
                f"{SHIFTS_PER_EVENT} shifts per event, missing share {MISSING_SHARE}; condition 'spread' = each shift "
                f"blank with probability {MISSING_SHARE} in every event; condition 'one_event' = blanks only at the book "
                "swap, probability 2 x 0.25 x (hours - 3) / 6 capped at 0.9; long shifts earn less per hour\n")
        f.write(f"proxy simulation: population {POP}, group B share {SHARE_B}, top {TOP:.0%} selected, "
                f"need ~ lognormal(0, 0.6), cost = need x access x lognormal(0, 0.3), seeds 1000-1049; "
                "mechanism only, not Obermeyer et al.'s data\n")
        f.write("decision matrix: constructed candidates A-F; each criterion scaled to 0-10 by fixed ranges, "
                "weighted sum; scenarios as in ch11_matrix_sensitivity.csv\n")
