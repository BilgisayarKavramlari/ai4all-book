"""Chapter 4 computed toys. Run from the repo root:
    python3 figures/scripts/ch04_experiments.py
Writes data/ch04_recombination.csv, data/ch04_scoring.csv and data/ch04_experiments_meta.txt.

These are TOYS for teaching, not measurements of real large language models.

1. Recombination (F4.4, section 4.2). A word-pair (bigram) model is trained on 12 true sentences of the
   form "<city> is the capital of <country> ." It then generates 1,000 sentences. Every neighboring word
   pair it produces appeared in a true training sentence, yet most sentences are false, because the model
   keeps no record of which country went with which city. A second toy that conditions on the previous
   five words (with back-off to shorter contexts) is asked to complete "<city> is the capital of" for the
   12 training cities and for 4 cities it never saw. It completes every prompt with a fluent country
   name; for the unseen cities none is correct, because the right country never appeared in training.
2. Scoring rules (F4.12, Deep 4.A). Expected score of answering vs. abstaining ("I don't know") at
   confidence p, under (A) right = 1, wrong = 0, abstain = 0 and (B) right = 1, wrong = -3, abstain = 0
   (a penalty of t/(1-t) = 3 for t = 0.75, the rule proposed by Kalai et al., 2025; their v1 text, section 4.2,
   prints "penalty 2" for t = 0.75, an arithmetic slip).
"""
import csv
import os
import platform
import random
from collections import defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA = os.path.join(ROOT, "data")
SEED = 4
N = 1000

TRAIN = [("Nairobi", "Kenya"), ("Lima", "Peru"), ("Ankara", "Türkiye"), ("Hanoi", "Vietnam"),
         ("Ottawa", "Canada"), ("Canberra", "Australia"), ("Dakar", "Senegal"), ("Oslo", "Norway"),
         ("Bogotá", "Colombia"), ("Manila", "the Philippines"), ("Cairo", "Egypt"), ("Tokyo", "Japan")]
UNSEEN = [("Accra", "Ghana"), ("Quito", "Ecuador"), ("Lisbon", "Portugal"), ("Seoul", "South Korea")]
TRUE = dict(TRAIN + UNSEEN)


def tokens(city, country):
    return ["<s>", city, "is", "the", "capital", "of", country, "."]


def train_ngram(sentences, n):
    """counts[context tuple][next word] for every context length 1..n-1"""
    counts = defaultdict(lambda: defaultdict(int))
    for s in sentences:
        for i in range(1, len(s)):
            for k in range(1, n):
                if i - k < 0:
                    break
                counts[tuple(s[i - k:i])][s[i]] += 1
    return counts


def next_word(counts, history, n, rng):
    for k in range(n - 1, 0, -1):          # back off from the longest context to the shortest
        ctx = tuple(history[-k:])
        if ctx in counts:
            words = list(counts[ctx].keys())
            weights = [counts[ctx][w] for w in words]
            return rng.choices(words, weights=weights)[0]
    raise RuntimeError("no context found")


def generate(counts, n, rng, start):
    out = list(start)
    while out[-1] != "." and len(out) < 20:
        out.append(next_word(counts, out, n, rng))
    return out


def main():
    rng = random.Random(SEED)
    sents = [tokens(c, k) for c, k in TRAIN]
    train_pairs = {(s[i], s[i + 1]) for s in sents for i in range(len(s) - 1)}

    rows = []
    # Toy 1: word-pair model, free generation
    bigram = train_ngram(sents, 2)
    n_true = n_pairs_seen = 0
    examples = []
    for _ in range(N):
        s = generate(bigram, 2, rng, ["<s>"])
        city, country = s[1], s[6]
        ok = TRUE.get(city) == country
        n_true += ok
        n_pairs_seen += all((s[i], s[i + 1]) in train_pairs for i in range(len(s) - 1))
        if len(examples) < 3 and not ok:
            examples.append(" ".join(s[1:]))
    rows.append({"condition": "word_pair_free", "label": "Word-pair model, free generation",
                 "n_generated": N, "n_true": n_true, "n_false": N - n_true,
                 "pct_true": round(100 * n_true / N, 1),
                 "pct_all_pairs_seen_in_training": round(100 * n_pairs_seen / N, 1),
                 "example_false": examples[0] if examples else ""})

    # Toy 2: five-word context, cities seen in training vs. never seen
    fivegram = train_ngram(sents, 6)
    for cond, label, cities in (("long_context_seen", "Five-word context, city seen in training", TRAIN),
                                ("long_context_unseen", "Five-word context, city never seen", UNSEEN)):
        n_true = 0
        ex = ""
        for _ in range(N):
            city, _country = rng.choice(cities)
            s = generate(fivegram, 6, rng, ["<s>", city, "is", "the", "capital", "of"])
            ok = TRUE[city] == s[6]
            n_true += ok
            if not ok and not ex:
                ex = " ".join(s[1:])
        rows.append({"condition": cond, "label": label, "n_generated": N, "n_true": n_true,
                     "n_false": N - n_true, "pct_true": round(100 * n_true / N, 1),
                     "pct_all_pairs_seen_in_training": "", "example_false": ex})

    os.makedirs(DATA, exist_ok=True)
    with open(os.path.join(DATA, "ch04_recombination.csv"), "w", newline="", encoding="utf8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    with open(os.path.join(DATA, "ch04_scoring.csv"), "w", newline="", encoding="utf8") as fh:
        w = csv.writer(fh)
        w.writerow(["confidence_p", "rule_A_answer", "rule_A_abstain", "rule_B_answer", "rule_B_abstain"])
        for i in range(0, 21):
            p = i / 20
            w.writerow([f"{p:.2f}", f"{p:.2f}", "0.00", f"{p - 3 * (1 - p):.2f}", "0.00"])

    with open(os.path.join(DATA, "ch04_experiments_meta.txt"), "w", encoding="utf8") as fh:
        fh.write(f"python {platform.python_version()} · standard library only (random, csv)\n")
        fh.write(f"seed {SEED}; N = {N} generations per condition\n")
        fh.write("recombination: 12 training sentences '<city> is the capital of <country> .'; "
                 "word-pair (bigram) model with counts; five-word-context model with back-off to shorter contexts; "
                 "unseen cities: Accra, Quito, Lisbon, Seoul (their countries never appear in training)\n")
        fh.write("scoring: rule A right 1 / wrong 0 / abstain 0; rule B right 1 / wrong -3 / abstain 0 "
                 "(penalty t/(1-t), t = 0.75)\n")
        fh.write("TOYS for teaching; not measurements of real large language models\n")
    for r in rows:
        print(r)


if __name__ == "__main__":
    main()
