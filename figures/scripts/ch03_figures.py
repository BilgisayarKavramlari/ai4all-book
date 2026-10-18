"""Chapter 3 diagrams (SVG, color + gray). Run from the repo root:
    python3 figures/scripts/ch03_figures.py
Data charts (F3.2, F3.4, F3.6, F3.13) are in ch03_charts.py (data from ch03_tokens.py).
F1.4 (three lanes) is reused in section 3.5 from figures/out/{color,gray}/f1-04-three-lanes.svg (not redrawn).

Signature 4, Anatomy of an LLM Response, is introduced here. The reusable drawing function is `llm_anatomy(stage=..., highlight=...)`. Later chapters (4, 8, 9) import it
(`from ch03_figures import llm_anatomy`) and pass a stage, or a set of parts to highlight.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from figlib import render, MUTED, INK, ROLES  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LOOP = ["Frame", "Prompt", "Verify", "Decide", "Disclose"]

# Illustrative scores shown inside Signature 4 (same values as data/ch03_temperature.csv, T = 1.0)
SIG4_SCORES = [("The", 30), ("Bean", 16), ("Brew", 12), ("Campus", 9), ("Common", 6)]
SIG4_TOKENS = "A | good | name | for |\na | coffee | shop | near |\ncampus | is"  # o200k_base pieces


# ---------------------------------------------------------------- Signature 4: Anatomy of an LLM Response
PARTS = {"context", "system", "conversation", "retrieved", "prompt", "tokens", "model", "scores", "sampling"}
STAGES = {"tokens": {"tokens"}, "scores": {"model", "scores", "sampling"}, "context": {"context"},
          "complete": set()}


def llm_anatomy(stage="complete", highlight=None, note=None):
    """Signature 4, Anatomy of an LLM Response (at most 9 boxes).

    stage: "tokens" (step 1), "scores" (steps 2-4: scoring and sampling), "context" (the context
           window), or "complete" (nothing highlighted: Chapter Summary and later chapters).
    highlight: optional set of parts that replaces the stage's highlight; parts are
           context, system, conversation, retrieved, prompt, tokens, model, scores, sampling.
           Example: llm_anatomy(highlight={"retrieved"}) marks the retrieved-text slot (section 3.5).
    note: optional one-line remark printed under the title (e.g., a later chapter's point).
    """
    parts = set(highlight) if highlight is not None else STAGES[stage]
    if parts - PARTS:
        raise ValueError(f"unknown parts: {parts - PARTS}")
    short = {"tokens": "tok", "sampling": "sample", "context": "ctx", "retrieved": "retr",
             "system": "sys", "conversation": "conv", "prompt": "you"}
    hl = {short.get(p, p) for p in parts}

    def draw(f):
        ink, muted = INK[f.mode], MUTED[f.mode]
        f.text(400, 24, "Anatomy of an LLM response", size=18, weight="700")
        if note:
            f.text(400, 44, note, size=13, color=muted, italic=True)
        # --- context window frame (box 1 of 9)
        thick_ctx = "ctx" in hl
        fill, stroke, _ = ROLES[f.mode]["soft"]
        f.raw(f'<rect x="20" y="56" width="262" height="364" rx="6" fill="{fill}" stroke="{ink}" '
              f'stroke-width="{3.4 if thick_ctx else 1.6}"/>')
        if thick_ctx:
            hf, hs, ht = ROLES[f.mode]["highlight"]
            f.raw(f'<rect x="20" y="56" width="262" height="50" rx="6" fill="{hf}" stroke="{ink}" stroke-width="3.4"/>')
            f.text(151, 72, "Context window", size=15, weight="700", color=ht)
            f.text(151, 92, "everything the model receives this turn", size=13, color=ht)
        else:
            f.text(151, 72, "Context window", size=15, weight="700")
            f.text(151, 92, "everything the model receives this turn", size=13)
        inner = [("System prompt", "set by the tool's maker", "step", "neutral", "sys"),
                 ("Conversation so far", "earlier prompts and responses", "step", "neutral", "conv"),
                 ("Pasted or retrieved text", "documents, search results", "step", "neutral", "retr"),
                 ("Your prompt", "the newest message", "human", "neutral", "you")]
        for i, (lab, sub, kind, role, key) in enumerate(inner):
            on = key in hl if key else False
            f.box(36, 116 + i * 66, 230, 56, lab, role="highlight" if on else role, kind=kind, thick=on,
                  size=14, sub=sub, sub_size=13)
        f.text(151, 398, "+ each token the model adds", size=13, italic=True)
        # --- 1. tokens
        on = "tok" in hl
        f.box(318, 60, 210, 120, "1. Text becomes tokens", role="highlight" if on else "neutral", kind="step",
              thick=on, size=14, sub=SIG4_TOKENS, sub_size=13)
        f.arrow(284, 120, 316, 120)
        # --- 2. model
        on = "model" in hl
        f.box(566, 60, 214, 120, "2. The model scores every possible next token",
              role="highlight" if on else "ai", kind="ai", thick=on, size=14,
              sub="settings fixed after training", sub_size=13)
        f.arrow(530, 120, 564, 120)
        # --- 3. scores (bars inside)
        on = "scores" in hl
        sfill, _, _ = ROLES[f.mode]["neutral"]
        f.raw(f'<rect x="566" y="216" width="214" height="204" rx="3" fill="{sfill}" stroke="{ink}" '
              f'stroke-width="{3.4 if on else 1.6}"/>')
        if on:
            hf, _, ht = ROLES[f.mode]["highlight"]
            f.raw(f'<rect x="566" y="216" width="214" height="34" rx="3" fill="{hf}" stroke="{ink}" stroke-width="3.4"/>')
            f.text(673, 233, "Scores for the next token", size=14, weight="700", color=ht)
        else:
            f.text(673, 233, "Scores for the next token", size=14, weight="700")
        afill, astroke, _ = ROLES[f.mode]["ai"]
        for i, (tok, pct) in enumerate(SIG4_SCORES):
            y = 268 + i * 25
            f.text(580, y, tok, size=13, anchor="start")
            f.raw(f'<rect x="644" y="{y - 8}" width="{pct * 3}" height="16" fill="{afill}" stroke="{astroke}" '
                  f'stroke-width="1"/>')
            f.text(650 + pct * 3, y, f"{pct}%", size=13, anchor="start")
        f.text(673, 394, "… thousands more, most near 0%", size=13, italic=True)
        f.arrow(673, 182, 673, 214)
        # --- 4. sampling (dashed: chance is involved)
        on = "sample" in hl
        f.box(318, 252, 210, 120, "3. Pick one token (sampling)", role="highlight" if on else "neutral",
              kind="step", dashed=True, thick=on, size=14,
              sub="the temperature option sets how often less likely tokens win", sub_size=13)
        f.arrow(564, 312, 530, 312)
        # --- 5. loop back into the context
        f.arrow(316, 352, 286, 380)
        f.text(423, 396, "4. Add the token to the context; repeat", size=13, weight="700")
        f.text(423, 414, "until the response is finished", size=13)
        f.text(400, 452, "Hexagon = AI component · dashed = chance involved · rounded = you · "
               "dark or thick = this section's step", size=13, color=muted, width=780)
        f.text(400, 476, "Scores are illustrative; token pieces from a newer OpenAI tokenizer (o200k_base).", size=13,
               color=muted, italic=True)
    return draw


# ---------------------------------------------------------------- F3.1 Chapter map
def chapter_map(f):
    f.text(400, 30, "Chapter 3 at a glance", size=22, weight="700")
    cols = [("How it works", ["3.1 Words become tokens", "3.2 Predicting the next token",
                              "3.3 Training, then inference"]),
            ("What it receives", ["3.4 The context window", "3.5 Retrieval and tools (and what agents are)"]),
            ("Do", ["3.6 Probe the model: Lab 3.1 (Thu, Jan 28)", "A2 Part 2: at least 5 Chapter 3 terms (due Feb 1)"])]
    for c, (head, items) in enumerate(cols):
        x = 30 + c * 255
        f.text(x + 115, 74, head, size=16, weight="700")
        for i, it in enumerate(items):
            role = "neutral" if c < 2 else ("verified" if i == 1 else "soft")
            kind = "human" if c == 2 else "step"
            f.box(x, 94 + i * 88, 230, 70, it, role=role, kind=kind, size=14)
        if c < 2:
            f.arrow(x + 236, 217, x + 252, 217)
    y = 372
    f.text(150, y, "AI Work Loop:", size=14, weight="700", anchor="end")
    xs = [205, 300, 420, 540, 640]
    for i, step in enumerate(LOOP):
        if step == "Prompt":
            f.box(xs[i] - 50, y - 20, 100, 40, step, role="highlight", kind="human", thick=True, size=15)
        elif step == "Verify":
            f.box(xs[i] - 45, y - 17, 90, 34, step, role="neutral", kind="human", dashed=True, size=14)
        else:
            f.text(xs[i], y, step, size=14, color=MUTED[f.mode])
        if i < 4:
            f.text((xs[i] + xs[i + 1]) / 2, y, "→", size=14, color=MUTED[f.mode])
    f.text(400, 410, "This chapter strengthens Prompt (know what the model actually receives), then Verify (dashed).",
           size=13, color=MUTED[f.mode])
    f.text(400, 436, "Opening case: the reversal curse (Berglund et al., 2024)", size=13, color=MUTED[f.mode])


# ---------------------------------------------------------------- F3.5 training, then inference
def train_infer(f):
    ink, muted = INK[f.mode], MUTED[f.mode]
    f.text(20, 26, "Training (before you use the tool): the settings change", size=15, weight="700", anchor="start")
    steps = [("Pretraining", "predict the next token in huge amounts of text (self-supervised)", "step"),
             ("Instruction tuning", "examples of prompts and good responses", "step"),
             ("Learning from human feedback", "people rank responses; a scoring model is trained on them", "human")]
    for i, (h, s, kind) in enumerate(steps):
        x = 20 + i * 260
        f.box(x, 44, 240, 118, h, role="neutral", kind=kind, size=14, sub=s, sub_size=13)
        if i < 2:
            f.arrow(x + 242, 103, x + 258, 103)
    f.text(20, 200, "Inference (each time you use it):", size=15, weight="700", anchor="start")
    f.text(20, 220, "the settings only get used", size=15, weight="700", anchor="start")
    f.box(20, 244, 200, 76, "Your prompt", role="neutral", kind="human", size=15)
    f.arrow(222, 282, 278, 282)
    f.box(280, 236, 240, 92, "The model", role="ai", kind="ai", size=15, sub="settings fixed (frozen)",
          sub_size=13)
    f.arrow(522, 282, 578, 282)
    f.box(580, 244, 200, 76, "Response", role="neutral", kind="step", dashed=True, size=15,
          sub="likely text; may be out of date", sub_size=13)
    f.arrow(650, 166, 470, 234)
    f.text(520, 190, "settings frozen when training ends", size=13, anchor="end", italic=True, color=muted)
    # timeline with knowledge cutoff
    y = 392
    f.line(40, y, 520, y, color=ink, width=3)
    f.line(520, y, 760, y, color=ink, width=2, dashed=True)
    f.raw(f'<polygon points="760,{y - 6} 772,{y} 760,{y + 6}" fill="{ink}"/>')
    f.text(280, y - 20, "Text written before the cutoff: can shape the settings", size=13)
    f.text(642, y - 20, "Later events: not in the settings", size=13)
    f.line(520, y - 34, 520, y + 26, color=ink, width=2.4, dashed=True)
    f.text(520, y + 40, "Knowledge cutoff", size=14, weight="700")
    f.text(776, y + 40, "time", size=13, anchor="end", italic=True, color=muted)
    f.text(400, 466, "Hexagon = AI component · rounded = human input · dashed = may be wrong or out of date",
           size=13, color=muted)


# ---------------------------------------------------------------- F3.8 probe record
PROBE_ROWS = [("1. Prediction",
               "The model will miscount the letter r in “strawberry”, because it receives tokens, not letters."),
              ("2. Prompt",
               "“How many times does the letter r appear in the word strawberry? Answer with a number.”"),
              ("3. Result",
               "Constructed example: “3”. Correct. Asked to spell the word letter by letter first: also 3."),
              ("4. Conclusion",
               "My prediction was wrong for this tool on this date. One correct answer does not show the tool "
               "counts letters reliably; I would test five more words.")]


def probe_record(rows=None, title="A probe record (worked example)"):
    """Four-part probe record. rows: optional list of (label, text) pairs replacing the default worked
    content (Chapter 4 reuses it for F4.7). A row whose label contains "Result" is drawn as the model's
    output (dashed hexagon); the others are human decisions (rounded). Default output unchanged."""
    rows = rows or PROBE_ROWS

    def draw(f):
        muted = MUTED[f.mode]
        f.text(400, 24, title, size=17, weight="700")
        for i, (lab, txt) in enumerate(rows):
            is_ai = "result" in lab.lower()
            y = 46 + i * 92
            f.box(20, y, 190, 76, lab, role="ai" if is_ai else "neutral", kind="ai" if is_ai else "human",
                  dashed=is_ai, size=16)
            f.arrow(212, y + 38, 236, y + 38)
            f.text(240, y + 38, txt, size=14, anchor="start", width=540)
            if i < len(rows) - 1:
                f.arrow(115, y + 78, 115, y + 90)
        f.text(400, 432, "Also record: the tool, the model name if shown, the options used (search on or off) and the date.",
               size=13, color=muted)
        f.text(400, 454, "Rounded = your decisions · hexagon (dashed) = the model's output, which may be wrong", size=13,
               color=muted)
    return draw


# ---------------------------------------------------------------- F3.9 mini concept map
def mini_map(f):
    muted = MUTED[f.mode]
    bw, bh = 220, 56
    f.text(150, 28, "Chapter 3 term", size=15, weight="700")
    f.text(650, 28, "Chapter 2 term", size=15, weight="700")
    links = [("Pretraining", "is a kind of", "Self-supervised learning"),
             ("Next-token prediction", "uses the real next token as its", "Label"),
             ("Knowledge cutoff", "marks the end of the", "Training data"),
             ("Context window", "is rebuilt at every step of", "Inference")]
    for k, (a, lab, b) in enumerate(links):
        y = 80 + k * 84
        f.box(150 - bw / 2, y - bh / 2, bw, bh, a, role="neutral", kind="human", size=15)
        f.box(650 - bw / 2, y - bh / 2, bw, bh, b, role="soft", kind="human", size=15)
        f.arrow(262, y, 538, y)
        f.text(400, y - 16, lab, size=14, italic=True, weight="600")
    f.text(400, 410, "Read each link as a sentence: “Pretraining is a kind of self-supervised learning.”", size=14)
    f.text(400, 436, "White = Chapter 3 terms · shaded = Chapter 2 terms · italic labels = the relationship", size=13,
           color=muted)


# ---------------------------------------------------------------- F3.10 attention (Deep 3.A)
def attention(f):
    """Decoder-only (causal) attention: a token draws only on tokens before it. Illustration only."""
    muted = MUTED[f.mode]
    words_tpl = ["The", "trophy", "doesn't", "fit", "in", "the", "brown", "suitcase", "because", "it's", "too"]
    sents = [("big.", "trophy", "suitcase", 140), ("small.", "suitcase", "trophy", 320)]
    f.text(400, 24, "Attention lets each token draw on the tokens before it", size=16, weight="700")
    for last, strong, weak, y in sents:
        words = words_tpl + [last]
        xs, x = [], 24
        for w in words:
            wpx = len(w) * 8.6 + 16
            xs.append(x + wpx / 2)
            x += wpx
        for w, cx in zip(words, xs):
            bold = w in (strong, last, "it's")
            f.text(cx, y, w, size=15, weight="700" if bold else "normal")
        src = xs[-1]
        f.arrow(src, y - 14, xs[words.index(strong)], y - 14, curve=110, width=3.4)      # above the words
        f.arrow(src, y + 14, xs[words.index(weak)], y + 14, curve=-80, width=1.2, dashed=True)  # below
        ly = y + 50 if strong == "trophy" else y - 50
        f.text(30, ly, f"strong link: “{strong}” · weak link: “{weak}”", size=13, anchor="start", color=muted)
    f.text(400, 408, "Arrows start at the later word: each token can draw only on the tokens before it.", size=14)
    f.text(400, 434, "Thick arrow = strong link · thin dashed arrow = weak link · illustration, not measured values",
           size=13, color=muted)


# ---------------------------------------------------------------- F3.12 summary card
def summary_card(f):
    f.text(400, 26, "Chapter 3 — what you can do now", size=18, weight="700")
    cards = ["Tokens: text becomes numbered pieces; the same text costs more in some languages",
             "Prediction: score every possible next token, pick one, add it, repeat",
             "Training vs. inference: settings fixed after training; a knowledge cutoff; your chat does not retrain it",
             "Context window: everything received this turn; the middle of a long input can be missed",
             "Retrieval and tools: change what the model receives, not how it predicts; check what they add",
             "Probe: prediction → prompt → result → conclusion; any result is evidence"]
    for i, c in enumerate(cards):
        x = 20 + (i % 3) * 258
        y = 50 + (i // 3) * 150
        f.box(x, y, 242, 130, c, role="neutral" if i % 2 else "soft", kind="human", size=14, weight="600")


FIGS = [
    ("f3-01-chapter-map", chapter_map, 800, 455, "Chapter 3 at a glance"),
    ("f3-03a-anatomy-tokens", llm_anatomy("tokens"), 800, 490, "Step 1: text becomes tokens"),
    ("f3-03b-anatomy-scores", llm_anatomy("scores"), 800, 490,
     "Steps 2 to 4: the model scores every possible next token and one is picked"),
    ("f3-03c-anatomy-context", llm_anatomy("context"), 800, 490,
     "The context window holds everything the model receives in one turn"),
    ("f3-03d-anatomy-retrieval", llm_anatomy(highlight={"retrieved"}), 800, 490,
     "Retrieval adds text to the context; it does not change how the model predicts"),
    ("f3-03-anatomy", llm_anatomy("complete"), 800, 490,
     "A response is built one token at a time from scores over every possible next token"),
    ("f3-05-train-infer", train_infer, 800, 480,
     "Training changes the settings; inference only uses them, so knowledge stops at the cutoff"),
    ("f3-08-probe-record", probe_record(), 800, 470, "A probe turns a guess about a model into evidence"),
    ("f3-09-mini-map", mini_map, 800, 450, "Each new term attaches to a Chapter 2 term with a true sentence"),
    ("f3-10-attention", attention, 800, 450, "Attention lets each token draw on the tokens before it"),
    ("f3-12-summary-card", summary_card, 800, 340, "Chapter 3 summary card"),
]

if __name__ == "__main__":
    for fid, fn, w, h, title in FIGS:
        render(fid, fn, w, h, title, ROOT)
        print("rendered", fid)
