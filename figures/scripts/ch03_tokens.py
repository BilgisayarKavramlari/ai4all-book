"""Chapter 3 computed data: token counts across languages (F3.2, section 3.1) and the
illustrative next-token scores used in section 3.2 (F3.3, F3.4).

Run from the repo root:
    python3 figures/scripts/ch03_tokens.py

Outputs
  data/ch03_tokens.csv          UDHR full text, tokens per language, two tokenizers (F3.2)
  data/ch03_tokens_example.csv  Elif's constructed abstract, English vs. Turkish (3.1 worked example)
  data/ch03_token_pieces.csv    token pieces of the words used as examples in 3.1
  data/ch03_temperature.csv     illustrative scores at three temperatures + seeded draws (3.2, F3.4)
  data/ch03_tokens_meta.txt     versions, encodings, text source and checksum

Parallel text: the Universal Declaration of Human Rights (UDHR) in the Unicode UDHR
collection, as packaged in the NLTK "udhr2" corpus (downloaded once into build/ch03/,
checked against the SHA-256 below). Each file: NFC-normalized, blank lines removed,
first line (the title) dropped, lines joined with newlines.

Next-token scores: no small open causal language model (for example GPT-2) was in the local
Hugging Face cache on 2026-10-18, and the brief forbids downloading models, so the scores in
data/ch03_temperature.csv are ILLUSTRATIVE (chosen by the book), not output of a real model.
"""
import csv
import hashlib
import io
import math
import os
import random
import unicodedata
import urllib.request
import zipfile
from datetime import date

import tiktoken

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA = os.path.join(ROOT, "data")
BUILD = os.path.join(ROOT, "build", "ch03")
UDHR_URL = "https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/corpora/udhr2.zip"
UDHR_SHA256 = "0796c314b09a930c989c6f9d93d226af9af13feccd88496e196c743dd266c7f3"
ENCODINGS = ["o200k_base", "cl100k_base"]  # tiktoken: gpt-4o -> o200k_base; gpt-4, gpt-3.5-turbo -> cl100k_base
LANGS = [("eng", "English"), ("spa", "Spanish"), ("tur", "Turkish"), ("rus", "Russian"),
         ("cmn_hans", "Chinese (simplified)"), ("arb", "Arabic"), ("vie", "Vietnamese"),
         ("hin", "Hindi"), ("tam", "Tamil")]

ABSTRACT_EN = ("Test anxiety is common among first-year university students and can lower exam "
               "performance. In this study, 120 students completed a short questionnaire about sleep, "
               "study habits and worry before their midterm exams. Students who reported less than six "
               "hours of sleep also reported higher anxiety. The results suggest that sleep may be a "
               "useful focus for campus support programs.")
ABSTRACT_TR = ("Sınav kaygısı, üniversite birinci sınıf öğrencileri arasında yaygındır ve sınav "
               "performansını düşürebilir. Bu çalışmada 120 öğrenci, ara sınavlarından önce uyku, çalışma "
               "alışkanlıkları ve endişe hakkında kısa bir anket doldurdu. Altı saatten az uyuduğunu bildiren "
               "öğrenciler daha yüksek kaygı da bildirdi. Sonuçlar, uykunun kampüs destek programları için "
               "yararlı bir odak olabileceğini göstermektedir.")
PIECE_WORDS = [" hydroxychloroquine", "hydroxychloroquine", " strawberry", "strawberry", " Nguyen", "İzmir", " İzmir",
               " psikoloji"]

# Illustrative next-token probabilities at temperature 1 for the prompt
# "A good name for a coffee shop near campus is" (chosen by the book, not model output).
# The 20 "other" tokens share the remaining probability equally (a real vocabulary has about
# 200,000 tokens; most get almost no probability, so they are left out of this illustration).
SCORES_T1 = [(" The", 0.30), (" Bean", 0.16), (" Brew", 0.12), (" Campus", 0.09),
             (" Common", 0.06), (" Java", 0.05), (" Grounds", 0.04)]
OTHER = [" Mug", " Corner", " Owl", " Roast", " Nook", " Study", " Library", " Latte", " Morning",
         " Hub", " Spot", " Cafe", " Perk", " Drip", " Quad", " Pages", " Orbit", " Tide", " Lantern", " Fox"]
N_OTHER = len(OTHER)
TEMPS = [0.5, 1.0, 1.5]
SEED = 3
N_DRAWS = 10


def udhr_texts():
    os.makedirs(BUILD, exist_ok=True)
    zpath = os.path.join(BUILD, "udhr2.zip")
    if not os.path.exists(zpath):
        with urllib.request.urlopen(UDHR_URL, timeout=60) as r, open(zpath, "wb") as fh:
            fh.write(r.read())
    blob = open(zpath, "rb").read()
    sha = hashlib.sha256(blob).hexdigest()
    if sha != UDHR_SHA256:
        raise SystemExit(f"udhr2.zip checksum mismatch: {sha}")
    z = zipfile.ZipFile(io.BytesIO(blob))
    out = {}
    for code, _ in LANGS:
        raw = z.read(f"udhr2/{code}.txt").decode("utf8")
        lines = [ln.strip() for ln in unicodedata.normalize("NFC", raw).splitlines() if ln.strip()]
        out[code] = "\n".join(lines[1:])
    return out, sha


def write_csv(name, header, rows):
    with open(os.path.join(DATA, name), "w", newline="", encoding="utf8") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(rows)


def main():
    encs = {n: tiktoken.get_encoding(n) for n in ENCODINGS}
    texts, sha = udhr_texts()

    # F3.2: tokens per language, relative to English, for each encoding
    base = {n: len(encs[n].encode(texts["eng"])) for n in ENCODINGS}
    rows = []
    for code, name in LANGS:
        t = texts[code]
        row = [code, name, len(t)]
        for n in ENCODINGS:
            k = len(encs[n].encode(t))
            row += [k, f"{k / base[n]:.2f}"]
        rows.append(row)
    write_csv("ch03_tokens.csv",
              ["lang_code", "language", "characters", "tokens_o200k_base", "ratio_to_english_o200k_base",
               "tokens_cl100k_base", "ratio_to_english_cl100k_base"], rows)

    # 3.1 worked example: Elif's constructed abstract
    ex = []
    for lang, t in (("English", ABSTRACT_EN), ("Turkish", ABSTRACT_TR)):
        ex.append([lang, len(t.split()), len(t)] + [len(encs[n].encode(t)) for n in ENCODINGS])
    write_csv("ch03_tokens_example.csv",
              ["language", "words", "characters", "tokens_o200k_base", "tokens_cl100k_base"], ex)

    # 3.1 token pieces
    pieces = []
    for w in PIECE_WORDS:
        for n in ENCODINGS:
            ids = encs[n].encode(w)
            pieces.append([repr(w), n, len(ids), " | ".join(encs[n].decode([i]) for i in ids),
                           " ".join(map(str, ids))])
    p_ids = encs["o200k_base"].encode("A good name for a coffee shop near campus is")
    pieces.append(["'A good name for a coffee shop near campus is'", "o200k_base", len(p_ids),
                   " | ".join(encs["o200k_base"].decode([i]) for i in p_ids), " ".join(map(str, p_ids))])
    write_csv("ch03_token_pieces.csv", ["text", "encoding", "n_tokens", "pieces", "token_ids"], pieces)

    # 3.2 / F3.4: temperature (illustrative scores)
    p_other_each = (1 - sum(p for _, p in SCORES_T1)) / N_OTHER
    vocab = SCORES_T1 + [(t, p_other_each) for t in OTHER]
    logits = [math.log(p) for _, p in vocab]  # illustrative scores (log-probabilities at T = 1)
    probs = {}
    for t in TEMPS:
        ex_ = [math.exp(l / t) for l in logits]
        s = sum(ex_)
        probs[t] = [e / s for e in ex_]
    rows = []
    for i, (tok, _) in enumerate(SCORES_T1):
        rows.append([tok.strip(), f"{logits[i]:.3f}"] + [f"{100 * probs[t][i]:.1f}" for t in TEMPS])
    rows.append([f"{N_OTHER} other tokens combined", f"{math.log(p_other_each):.3f} each"] +
                [f"{100 * sum(probs[t][len(SCORES_T1):]):.1f}" for t in TEMPS])
    # seeded draws for the worked example
    rng = random.Random(SEED)
    draws = {}
    for t in (0.5, 1.5):
        picks = rng.choices(range(len(vocab)), weights=probs[t], k=N_DRAWS)
        draws[t] = [vocab[k][0].strip() for k in picks]
    rows.append(["# draws_T0.5 (seed 3)", " ".join(draws[0.5]), "", "", ""])
    rows.append(["# draws_T1.5 (seed 3)", " ".join(draws[1.5]), "", "", ""])
    write_csv("ch03_temperature.csv",
              ["token", "score_logit_illustrative", "pct_T0.5", "pct_T1.0", "pct_T1.5"], rows)

    import sys
    with open(os.path.join(DATA, "ch03_tokens_meta.txt"), "w", encoding="utf8") as fh:
        fh.write(f"Generated by figures/scripts/ch03_tokens.py on {date.today().isoformat()}\n")
        fh.write(f"Python {sys.version.split()[0]}; tiktoken {tiktoken.__version__}\n")
        for n in ENCODINGS:
            fh.write(f"Encoding {n}: vocabulary size {encs[n].n_vocab}\n")
        fh.write("tiktoken model map: gpt-4o -> o200k_base; gpt-4 and gpt-3.5-turbo -> cl100k_base\n")
        fh.write(f"Parallel text: UDHR, Unicode UDHR collection via NLTK udhr2 corpus, {UDHR_URL}\n")
        fh.write(f"udhr2.zip SHA-256 {sha}\n")
        fh.write("Preprocessing: NFC normalization, blank lines removed, first (title) line dropped.\n")
        fh.write("Languages: " + ", ".join(f"{n} ({c})" for c, n in LANGS) + "\n")
        fh.write("Note: the Vietnamese file has one extra line (adoption note) after the title; kept.\n")
        fh.write("Elif's abstract: constructed by the book (not a real study); Turkish translation by the book.\n")
        fh.write("Next-token scores (ch03_temperature.csv): ILLUSTRATIVE, chosen by the book. No local causal\n"
                 "language model (e.g., GPT-2) was found in ~/.cache/huggingface on 2026-10-18; none downloaded.\n")
        fh.write(f"Temperature draws: random.Random({SEED}), {N_DRAWS} draws each at T = 0.5 and T = 1.5.\n")
    print("ch03 token data written")


if __name__ == "__main__":
    main()
