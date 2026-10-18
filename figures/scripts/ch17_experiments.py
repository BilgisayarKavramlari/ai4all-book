"""Chapter 17 computed demos. Constructed data only; not data about any real person, system or tool.

Run from the repo root:
    python3 figures/scripts/ch17_experiments.py
Writes:
  data/ch17_occlusion.csv        Demo A: per-pixel attributions (two models), 12 x 12 grid, long format
  data/ch17_occlusion_summary.csv Demo A: accuracies and per-pixel attribution summaries
  data/ch17_fidelity.csv         Demo B: global surrogate fidelity by tree depth
  data/ch17_stability.csv        Demo B: local-surrogate top feature across 10 seeds, two sample sizes
  data/ch17_counterfactual.csv   Demo B: smallest flip, unconstrained vs actionable features only
  data/ch17_scorecard.csv        Lab 17.3: a constructed points scorecard and 20 applicants (inputs only; key printed)
  data/ch17_baseline_sensitivity.csv  Demo A (v2): background share of the evidence at five fixed baselines
  data/ch17_experiments_meta.txt versions, seeds and every method choice

Methods were fixed before the first run (blueprint v0.2, editor decision 3); results are reported as they come.

Demo A (section 17.3: Sam's replica sorter). 12 x 12 grayscale images of three parts drawn as simple shapes:
bolt = a vertical bar, nut = a square ring, washer = a round ring. Part pixels are bright (1.0); pixel noise
sd 0.08; each shape is shifted by up to 1 pixel. Training set A ("the old photos"): 60 images per part; bolts on
a dark background (0.15), nuts and washers on a light background (0.60), as in Chapter 2. Test set 1: the same
recipe, new images. Test set 2 ("the club workbench"): every part on a mid-gray background (0.40).
Model: multinomial logistic regression on the 144 pixel values (scikit-learn, C = 1.0).
Attribution: one-pixel occlusion. Each pixel in turn is replaced by a FIXED baseline, the mean pixel value of
training set A (one number, the same for every image), and we record the change in the log-odds of the class the
model predicted for the original image: log p/(1-p) before minus after. Positive = the pixel pushed toward the
prediction. Per-pixel summaries (not shares of area): mean |attribution| over background pixels and over part
pixels of a test-1 bolt image, averaged over 30 bolt images.
Log-odds are computed from the model's scores (log-sum-exp), not from rounded probabilities.
Faithfulness check: logistic regression is itself a glass box, so the gap between the predicted class's score and
the runner-up's splits exactly into one term per pixel: (w_c,i - w_k,i) x (x_i - baseline). We report the
correlation between the occlusion map and this exact map, and the share of the positive exact contributions
that comes from background pixels (a share of the model's evidence, not of the image's area).
Retraining (model B): 120 new images per part, every image's background drawn uniformly between 0.10 and 0.70
for every part. Same tests and summaries.

Demo B (sections 17.4-17.5: a constructed micro-loan pre-screen; business example). 2,000 constructed applicants:
income (thousand dollars a year, lognormal, median about 45), debt ratio (0.05-0.80), months at the current job
(0-120), late payments in the last 24 months (Poisson, mean 0.8), age band (1-5; 1 = under 25 ... 5 = 55 and over).
The approval label is drawn from a logistic formula that includes age band ON PURPOSE, so that the demo can show
a counterfactual that changes something a person cannot change. Black box: gradient-boosted trees
(scikit-learn GradientBoostingClassifier, 150 trees, depth 3) trained on 1,500 applicants; 500 held out.
 (1) Global surrogate: decision trees of depth 1-4 fitted to the BLACK BOX's predictions on the training
     applicants (not to the true labels). Fidelity = share of held-out applicants on which surrogate and black box
     give the same decision.
 (2) Local surrogate (LIME-style, written here with NumPy): for one held-out applicant the black box rejects,
     draw n perturbed applicants by adding independent normal noise (sd = each feature's training sd) to the
     standardized features; weight each by exp(-d^2 / w^2) with w = 0.75 * sqrt(5); fit a weighted ridge
     regression (alpha = 1.0) of the black box's approval probability on the standardized features; the top
     feature is the one with the largest |coefficient|. 10 seeds x n in {100, 5000}.
 (3) Counterfactual: smallest change that turns the black box's decision for that applicant into "approve".
     Cost = sum over changed features of |change| / training sd (standardized L1). Search: every single-feature
     change and every pair of feature changes on a grid (income +0..+40k in 1k steps; debt ratio -0..-0.40 in 0.01
     steps; months +0..+48 in 1-month steps; late payments down to 0 in steps of 1; age band any value 1-5).
     "Unconstrained" allows all five features in either direction; "actionable" allows only income up, debt ratio
     down, months up (time) and late payments down (time), never age band.
"""
import csv
import os
import platform

import numpy as np
import sklearn
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA = os.path.join(ROOT, "data")
N = 12
CLASSES = ["bolt", "nut", "washer"]


# ---------------------------------------------------------------- Demo A
def shape_mask(kind, dx, dy):
    m = np.zeros((N, N), dtype=bool)
    if kind == "bolt":
        m[2 + dy:10 + dy, 5 + dx:7 + dx] = True
    elif kind == "nut":
        m[3 + dy:9 + dy, 3 + dx:9 + dx] = True
        m[5 + dy:7 + dy, 5 + dx:7 + dx] = False
    else:  # washer: round ring
        yy, xx = np.mgrid[0:N, 0:N]
        r = np.sqrt((yy - (5.5 + dy)) ** 2 + (xx - (5.5 + dx)) ** 2)
        m = (r >= 1.6) & (r <= 3.4)
    return m


def make_images(rng, per_class, bg_rule):
    X, y, masks = [], [], []
    for c, kind in enumerate(CLASSES):
        for _ in range(per_class):
            dx, dy = rng.integers(-1, 2, size=2)
            m = shape_mask(kind, dx, dy)
            bg = bg_rule(kind, rng)
            img = np.full((N, N), bg) + rng.normal(0, 0.08, (N, N))
            img[m] = 1.0 + rng.normal(0, 0.08, m.sum())
            X.append(img.ravel())
            y.append(c)
            masks.append(m.ravel())
    return np.array(X), np.array(y), np.array(masks)


def old_bg(kind, rng):
    return 0.15 if kind == "bolt" else 0.60


def gray_bg(kind, rng):
    return 0.40


def mixed_bg(kind, rng):
    return rng.uniform(0.10, 0.70)


def log_odds(p):
    p = np.clip(p, 1e-12, 1 - 1e-12)
    return np.log(p / (1 - p))


def class_log_odds(model, X, c):
    """log p_c / (1 - p_c), computed from the model's scores (logsumexp), so it does not round off near p = 1."""
    S = model.decision_function(X)
    others = np.delete(S, c, axis=1)
    m = others.max(axis=1, keepdims=True)
    lse = m[:, 0] + np.log(np.exp(others - m).sum(axis=1))
    return S[:, c] - lse


def occlusion(model, x, baseline):
    c = int(model.predict(x[None])[0])
    base = class_log_odds(model, x[None], c)[0]
    Xo = np.repeat(x[None], x.size, axis=0)
    Xo[np.arange(x.size), np.arange(x.size)] = baseline
    return base - class_log_odds(model, Xo, c), c


def exact_map(model, x, baseline, c):
    """Glass-box check: the predicted class's score minus the runner-up's, split exactly into one term per pixel."""
    S = model.decision_function(x[None])[0]
    k = int(np.argsort(-S)[1])
    w = model.coef_[c] - model.coef_[k]
    return w * (x - baseline)


def demo_a():
    rng = np.random.default_rng(1702)
    Xa, ya, ma = make_images(rng, 60, old_bg)
    X1, y1, m1 = make_images(rng, 30, old_bg)
    X2, y2, m2 = make_images(rng, 30, gray_bg)
    Xb, yb, _ = make_images(rng, 120, mixed_bg)          # model B: 120 photos per part, mixed backgrounds
    baseline = float(Xa.mean())
    rows, summ, sens = [], [], []
    for name, Xtr, ytr in [("A_old_photos", Xa, ya), ("B_mixed_backgrounds", Xb, yb)]:
        model = LogisticRegression(C=1.0, max_iter=5000)
        model.fit(Xtr, ytr)
        acc1 = float((model.predict(X1) == y1).mean())
        acc2 = float((model.predict(X2) == y2).mean())
        # per-class accuracy on test 2
        per2 = {CLASSES[c]: float((model.predict(X2[y2 == c]) == c).mean()) for c in range(3)}
        bolts = np.where(y1 == 0)[0]
        bg_vals, part_vals, corrs, shares, rings = [], [], [], [], []
        # ring positions: every pixel where a nut's or washer's ring can appear in these images (shifts of up to 1 px)
        ring = np.zeros((N, N), dtype=bool)
        for ddx in (-1, 0, 1):
            for ddy in (-1, 0, 1):
                ring |= shape_mask("nut", ddx, ddy) | shape_mask("washer", ddx, ddy)
        ring = ring.ravel()
        for k, i in enumerate(bolts):
            a, c = occlusion(model, X1[i], baseline)
            e = exact_map(model, X1[i], baseline, c)
            part = m1[i]
            bg_vals.append(np.abs(a[~part]).mean())
            part_vals.append(np.abs(a[part]).mean())
            corrs.append(np.corrcoef(a, e)[0, 1])
            pos = e.clip(min=0)
            shares.append(pos[~part].sum() / pos.sum())
            bgpos = pos * (~part)
            rings.append(bgpos[ring & ~part].sum() / bgpos.sum())
            if k == 0:
                for p in range(N * N):
                    rows.append([name, p // N, p % N, round(float(a[p]), 4), round(float(e[p]), 4),
                                 int(part[p])])
        summ.append([name, len(ytr), round(acc1, 3), round(acc2, 3),
                     round(per2["bolt"], 3), round(per2["nut"], 3), round(per2["washer"], 3),
                     round(float(np.mean(bg_vals)), 4), round(float(np.mean(part_vals)), 4),
                     round(float(np.mean(bg_vals) / np.mean(part_vals)), 2),
                     round(float(np.mean(corrs)), 3), round(float(np.min(corrs)), 3),
                     round(float(np.mean(shares)) * 100, 1),
                     round(float(np.mean(rings)) * 100, 1)])
        # v2 (reviewers' request; method unchanged): the background share at other fixed baselines
        for b in (0.0, 0.15, 0.40, round(baseline, 4), 0.60):
            sh = []
            for i in bolts:
                c = int(model.predict(X1[i][None])[0])
                e = exact_map(model, X1[i], b, c).clip(min=0)
                sh.append(e[~m1[i]].sum() / e.sum())
            sens.append([name, b, round(float(np.mean(sh)) * 100, 1)])
    with open(os.path.join(DATA, "ch17_occlusion.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["model", "row", "col", "occlusion_logodds", "exact_logodds", "is_part_pixel"])
        w.writerows(rows)
    with open(os.path.join(DATA, "ch17_occlusion_summary.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["model", "train_images", "acc_test1_same_recipe", "acc_test2_gray_workbench",
                    "test2_acc_bolt", "test2_acc_nut", "test2_acc_washer",
                    "mean_abs_attr_per_background_pixel", "mean_abs_attr_per_part_pixel",
                    "background_to_part_ratio_per_pixel", "mean_corr_occlusion_vs_exact", "min_corr",
                    "pct_of_positive_exact_contribution_from_background",
                    "pct_of_background_evidence_in_ring_positions"])
        w.writerows(summ)
    with open(os.path.join(DATA, "ch17_baseline_sensitivity.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["model", "baseline_pixel_value", "pct_of_positive_exact_contribution_from_background"])
        w.writerows(sens)
    return summ, baseline


# ---------------------------------------------------------------- Demo B
FEATS = ["income_k", "debt_ratio", "months_employed", "late_payments", "age_band"]


def make_applicants(rng, n):
    income = np.exp(rng.normal(np.log(45), 0.4, n))
    debt = np.clip(rng.normal(0.35, 0.15, n), 0.05, 0.80)
    months = np.clip(rng.gamma(2.0, 18.0, n), 0, 120)
    late = rng.poisson(0.8, n)
    age = rng.integers(1, 6, n)
    z = (-0.5 + 0.045 * (income - 45) - 6.0 * (debt - 0.35) + 0.015 * (months - 36)
         - 0.9 * late + 0.45 * (age - 3))
    p = 1 / (1 + np.exp(-z))
    y = (rng.uniform(size=n) < p).astype(int)
    X = np.column_stack([income, debt, months, late, age]).astype(float)
    return X, y


def lime_local(bb, x, mu, sd, n, seed):
    rng = np.random.default_rng(seed)
    xs = (x - mu) / sd
    Z = xs + rng.normal(0, 1, (n, xs.size))
    Xp = Z * sd + mu
    f = bb.predict_proba(Xp)[:, 1]
    d = np.sqrt(((Z - xs) ** 2).sum(axis=1))
    width = 0.75 * np.sqrt(xs.size)
    wts = np.exp(-(d ** 2) / width ** 2)
    A = np.column_stack([np.ones(n), Z])
    Wm = np.diag(wts) if n <= 200 else None
    reg = np.eye(A.shape[1]) * 1.0
    reg[0, 0] = 0.0
    if Wm is not None:
        beta = np.linalg.solve(A.T @ Wm @ A + reg, A.T @ Wm @ f)
    else:
        Aw = A * wts[:, None]
        beta = np.linalg.solve(A.T @ Aw + reg, Aw.T @ f)
    coefs = beta[1:]
    return coefs


def counterfactual(bb, x, sd, actionable):
    grids = {
        0: [x[0] + d for d in range(0, 41)],
        1: [round(x[1] - d / 100, 2) for d in range(0, 41) if x[1] - d / 100 >= 0.0],
        2: [x[2] + d for d in range(0, 49)],
        3: [x[3] - d for d in range(0, int(x[3]) + 1)],
        4: [1, 2, 3, 4, 5],
    }
    if not actionable:
        grids[0] = [x[0] + d for d in range(-40, 41) if x[0] + d > 5]
        grids[1] = [round(v, 2) for v in np.arange(0.05, 0.81, 0.01)]
        grids[2] = [max(0, x[2] + d) for d in range(-48, 49)]
        grids[3] = list(range(0, 6))
    feats = [0, 1, 2, 3] if actionable else [0, 1, 2, 3, 4]
    best = None
    cands = []
    for i in feats:
        for v in grids[i]:
            z = x.copy(); z[i] = v
            cands.append(z)
    for a in range(len(feats)):
        for b in range(a + 1, len(feats)):
            i, j = feats[a], feats[b]
            for v in grids[i][::2]:
                for u in grids[j][::2]:
                    z = x.copy(); z[i] = v; z[j] = u
                    cands.append(z)
    C = np.array(cands)
    pred = bb.predict(C)
    cost = (np.abs(C - x) / sd).sum(axis=1)
    ok = np.where(pred == 1)[0]
    if ok.size == 0:
        return None
    k = ok[np.argmin(cost[ok])]
    return C[k], float(cost[k])


def demo_b():
    rng = np.random.default_rng(1703)
    X, y = make_applicants(rng, 2000)
    Xtr, ytr, Xte, yte = X[:1500], y[:1500], X[1500:], y[1500:]
    bb = GradientBoostingClassifier(n_estimators=150, max_depth=3, random_state=1703)
    bb.fit(Xtr, ytr)
    bb_acc = float((bb.predict(Xte) == yte).mean())
    ptr, pte = bb.predict(Xtr), bb.predict(Xte)
    fid = []
    for depth in (1, 2, 3, 4):
        t = DecisionTreeClassifier(max_depth=depth, random_state=1703).fit(Xtr, ptr)
        agree = float((t.predict(Xte) == pte).mean())
        root = FEATS[t.tree_.feature[0]]
        tp = t.predict(Xte)
        matched = float(((tp == 1) & (pte == 1)).sum() / max(1, (pte == 1).sum()))
        fid.append([depth, 2 ** depth, round(agree * 100, 1), root, round(float((pte == 0).mean()) * 100, 1),
                    round(matched * 100, 1)])
    with open(os.path.join(DATA, "ch17_fidelity.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["tree_depth", "max_leaves", "fidelity_pct_heldout", "first_split_feature",
                    "always_reject_agreement_pct", "pct_of_model_approvals_matched"])
        w.writerows(fid)
    mu, sd = Xtr.mean(axis=0), Xtr.std(axis=0)
    # applicant to explain: the first held-out applicant the black box rejects with approval prob in 0.30-0.45
    probs = bb.predict_proba(Xte)[:, 1]
    idx = int(np.where((probs > 0.30) & (probs < 0.45))[0][0])
    x = Xte[idx].copy()
    stab = []
    for n in (100, 5000):
        for s in range(1704, 1714):
            coefs = lime_local(bb, x, mu, sd, n, s)
            order = np.argsort(-np.abs(coefs))
            stab.append([n, s, FEATS[order[0]], FEATS[order[1]], FEATS[order[2]]] +
                        [round(float(c), 4) for c in coefs])
    with open(os.path.join(DATA, "ch17_stability.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["n_samples", "seed", "top1", "top2", "top3"] + ["coef_" + f for f in FEATS])
        w.writerows(stab)
    cf_rows = []
    for label, act in (("unconstrained", False), ("actionable_only", True)):
        res = counterfactual(bb, x, sd, act)
        z, cost = res
        changes = "; ".join(f"{FEATS[i]} {x[i]:.2f} -> {z[i]:.2f}" for i in range(5) if abs(z[i] - x[i]) > 1e-9)
        cf_rows.append([label, changes, round(cost, 3), round(float(bb.predict_proba(z[None])[0, 1]), 3)])
    with open(os.path.join(DATA, "ch17_counterfactual.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["search", "applicant_before"] + FEATS + ["approval_prob_before"])
        w.writerow(["applicant", ""] + [round(float(v), 2) for v in x] + [round(float(probs[idx]), 3)])
        w.writerow([])
        w.writerow(["search", "changes", "cost_standardized_L1", "approval_prob_after"])
        w.writerows(cf_rows)
        # v2 (reviewers' request; search method unchanged): exact debt-ratio threshold and a one-band age change
        d = 0.0
        while d < 0.4:
            z = x.copy(); z[1] = x[1] - d
            if bb.predict(z[None])[0] == 1:
                break
            d = round(d + 0.001, 3)
        za = x.copy(); za[4] = x[4] + 1
        w.writerow([])
        w.writerow(["check", "value"])
        w.writerow(["debt_ratio_exact", round(float(x[1]), 4)])
        w.writerow(["smallest_debt_ratio_decrease_that_flips_0.001_steps", d])
        w.writerow(["debt_ratio_at_flip", round(float(x[1] - d), 4)])
        w.writerow(["approval_prob_if_age_band_plus_1", round(float(bb.predict_proba(za[None])[0, 1]), 3)])
    return bb_acc, fid, x, float(probs[idx]), stab, cf_rows


# ---------------------------------------------------------------- Lab 17.3 scorecard
def scorecard():
    """Lab 17.3 (v2). Student file: inputs and decision only (no points), so the local explanation is computed,
    not copied. The points key goes to private/ch17-answers-even.md. 'Bankruptcy before 2020' is a past record the
    applicant cannot change."""
    rng = np.random.default_rng(1714)
    rows, key = [], []
    for k in range(1, 21):
        income = int(rng.integers(18, 90))
        debt = round(float(rng.uniform(0.1, 0.7)), 2)
        months = int(rng.integers(0, 96))
        late = int(rng.poisson(0.8))
        bankrupt = "yes" if rng.uniform() < 0.2 else "no"
        pts_inc = 30 if income >= 60 else (20 if income >= 40 else 10)
        pts_debt = 30 if debt < 0.30 else (15 if debt < 0.45 else 0)
        pts_mon = 20 if months >= 24 else (10 if months >= 12 else 0)
        pts_late = 20 if late == 0 else (10 if late == 1 else 0)
        pts_bk = 10 if bankrupt == "no" else 0
        total = pts_inc + pts_debt + pts_mon + pts_late + pts_bk
        dec = "approve" if total >= 70 else "refer to a person"
        rows.append([f"A{k:02d}", income, debt, months, late, bankrupt, dec])
        key.append([f"A{k:02d}", pts_inc, pts_debt, pts_mon, pts_late, pts_bk, total, dec])
    with open(os.path.join(DATA, "ch17_scorecard.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["# Constructed points scorecard (Lab 17.3). Income (thousand $/yr): >=60 -> 30 points, 40-59 -> 20,"
                    " <40 -> 10. Debt ratio: <0.30 -> 30, 0.30-0.44 -> 15, >=0.45 -> 0. Months at job: >=24 -> 20,"
                    " 12-23 -> 10, <12 -> 0. Late payments (24 months): 0 -> 20, 1 -> 10, 2+ -> 0. Bankruptcy on"
                    " record before 2020: no -> 10, yes -> 0. Total >= 70 -> approve; otherwise refer to a person."])
        w.writerow(["applicant", "income_k", "debt_ratio", "months_employed", "late_payments",
                    "bankruptcy_before_2020", "decision"])
        w.writerows(rows)
    return key


if __name__ == "__main__":
    os.makedirs(DATA, exist_ok=True)
    summ, baseline = demo_a()
    bb_acc, fid, x, p0, stab, cf = demo_b()
    sc = scorecard()
    print("scorecard key:")
    for r in sc:
        print(r)
    with open(os.path.join(DATA, "ch17_experiments_meta.txt"), "w") as fh:
        fh.write(f"Python {platform.python_version()}; NumPy {np.__version__}; scikit-learn {sklearn.__version__}\n")
        fh.write("Seeds: Demo A numpy default_rng(1702); Demo B default_rng(1703), GradientBoosting random_state=1703,"
                 " local-surrogate seeds 1704-1713; scorecard default_rng(1714)\n")
        fh.write(f"Demo A fixed occlusion baseline (training-set mean pixel value): {baseline:.4f}\n")
        fh.write(f"Demo B black-box held-out accuracy against the constructed labels: {bb_acc:.3f}\n")
        fh.write("Implementation note: the first run computed log-odds from probabilities clipped at 1e-12, which rounded "
                 "saturated images to zero change; log-odds are now computed from the model's scores (same method, "
                 "no rounding). No other change was made after seeing results.\n")
        fh.write("Results that differ from the blueprint's expectation are reported as they came (Demo A per-pixel "
                 "measures; Demo B counterfactual): see docs/production/handoff/ch17.md.\n")
        fh.write("Revision v2 (reviewers' request): added the ring-position share, the baseline-sensitivity table, the "
                 "always-reject agreement and approvals matched for each surrogate, the exact debt-ratio flip point "
                 "and a one-band age change. These are extra reports of the same models; no method was changed.\n")
        fh.write("All data are constructed. See the module docstring for every method choice.\n")
    print("Demo A:", summ)
    print("Demo B acc", bb_acc, "fidelity", fid)
    print("applicant", x, "p", p0)
    from collections import Counter
    for n in (100, 5000):
        c = Counter(r[2] for r in stab if r[0] == n)
        print(n, c)
    print(cf)
