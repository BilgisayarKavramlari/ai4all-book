"""Chapter 2 experiments: real, reproducible numbers for Figures 2.13 and 2.14.

Dataset: scikit-learn's bundled handwritten-digits dataset (UCI Optical Recognition of Handwritten
Digits test set; 1,797 8x8 images). Run from the repo root:
    python3 figures/scripts/ch02_experiments.py
Writes data/ch02_regimes.csv and data/ch02_overfitting.csv. Library versions and seeds are recorded
in the CSV headers' companion file data/ch02_experiments_meta.txt.
"""
import csv
import os
import platform

import numpy as np
import sklearn
from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA = os.path.join(ROOT, "data")
CLASSES = [3, 5, 8]          # three classes that are easy to confuse, like the lecture's three objects
MINORITY = 8                 # the class reduced in the imbalanced regime
PER_CLASS = 60               # training examples per class in the balanced regime
MINORITY_N = 10              # minority examples in the imbalanced regime
NOISE = 0.20                 # share of training labels flipped in the noisy regime
SEEDS = range(30)


def three_class_data():
    X, y = load_digits(return_X_y=True)
    m = np.isin(y, CLASSES)
    return X[m] / 16.0, y[m]


def run_regime(X, y, regime, seed):
    rng = np.random.default_rng(seed)
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.4, stratify=y, random_state=seed)
    idx = []
    for c in CLASSES:
        ci = np.flatnonzero(ytr == c)
        n = MINORITY_N if (regime == "imbalanced" and c == MINORITY) else PER_CLASS
        idx.extend(rng.choice(ci, size=n, replace=False))
    idx = np.array(idx)
    Xs, ys = Xtr[idx], ytr[idx].copy()
    if regime == "noisy":
        flip = rng.choice(len(ys), size=int(round(NOISE * len(ys))), replace=False)
        for i in flip:
            ys[i] = rng.choice([c for c in CLASSES if c != ys[i]])
    if regime == "systematic":
        # the same share of labels is wrong, but always in one direction: class MINORITY labeled as CLASSES[0]
        src = np.flatnonzero(ys == MINORITY)
        n = int(round(NOISE * len(ys)))
        ys[rng.choice(src, size=min(n, len(src)), replace=False)] = CLASSES[0]
    model = LogisticRegression(max_iter=2000)
    model.fit(Xs, ys)
    pred = model.predict(Xte)
    overall = (pred == yte).mean()
    minority = (pred[yte == MINORITY] == MINORITY).mean()
    return overall, minority


def regimes():
    X, y = three_class_data()
    rows = []
    for regime in ("balanced", "imbalanced", "noisy", "systematic"):
        res = np.array([run_regime(X, y, regime, s) for s in SEEDS])
        rows.append({"regime": regime,
                     "overall_accuracy_pct": round(100 * res[:, 0].mean(), 1),
                     "minority_class_accuracy_pct": round(100 * res[:, 1].mean(), 1),
                     "overall_sd": round(100 * res[:, 0].std(), 1),
                     "minority_sd": round(100 * res[:, 1].std(), 1)})
    with open(os.path.join(DATA, "ch02_regimes.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    return rows


def overfitting():
    X, y = load_digits(return_X_y=True)
    rows = []
    for depth in range(1, 21):
        tr, te = [], []
        for s in range(10):
            Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, stratify=y, random_state=s)
            m = DecisionTreeClassifier(max_depth=depth, random_state=s).fit(Xtr, ytr)
            tr.append(m.score(Xtr, ytr))
            te.append(m.score(Xte, yte))
        rows.append({"max_depth": depth, "train_accuracy_pct": round(100 * np.mean(tr), 1),
                     "test_accuracy_pct": round(100 * np.mean(te), 1)})
    with open(os.path.join(DATA, "ch02_overfitting.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    return rows


if __name__ == "__main__":
    r = regimes()
    o = overfitting()
    with open(os.path.join(DATA, "ch02_experiments_meta.txt"), "w") as fh:
        fh.write(f"python {platform.python_version()} · scikit-learn {sklearn.__version__} · numpy {np.__version__}\n"
                 f"regimes: classes {CLASSES}, minority {MINORITY}, {PER_CLASS}/class, minority {MINORITY_N}, "
                 f"noise {NOISE} (random) and systematic ({NOISE} of all labels, minority->class {CLASSES[0]}), logistic regression, test 40%, {len(SEEDS)} seeds (0-{len(SEEDS)-1})\n"
                 "overfitting: all 10 digit classes, decision tree max_depth 1-20, test 30%, 10 seeds\n")
    for row in r:
        print(row)
    print([(x["max_depth"], x["train_accuracy_pct"], x["test_accuracy_pct"]) for x in o if x["max_depth"] in (1, 3, 5, 8, 10, 15, 20)])
