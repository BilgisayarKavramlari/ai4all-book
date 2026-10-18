"""Chapter 7 diagrams (SVG, color + gray). Run from the repo root:
    python3 figures/scripts/ch07_figures.py
Data charts (F7.2, F7.4, F7.9, F7.13) are in ch07_charts.py (published values in data/ch07_*.csv).

Signature diagrams reused (imported, never redrawn):
* Signature 2, Jagged Frontier Map: `jagged` from ch01_figures (F7.7 adds two callouts below the unchanged map;
  ch01's `jagged(f)` has no highlight argument).
* Signature 6, Anatomy of a Prompt: `prompt_anatomy` from ch05_figures (F7.10).
* Signature 7, The Delegation Ladder: `delegation_ladder` from ch05_figures (F7.14).

New reusable function introduced here (for Ch. 10, 19 and 21):

    from ch07_figures import scaffold_crutch
    scaffold_crutch(highlight=None | "scaffold" | "crutch", note=None)

It draws one question answered by the same AI reply in two lanes: with no attempt (crutch) and after the
learner's attempt (scaffold). Returns a draw(f) callable for figlib.render(); 9 boxes.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from figlib import render, MUTED, INK  # noqa: E402
from ch01_figures import jagged  # noqa: E402  (Signature 2, reused)
from ch05_figures import prompt_anatomy, delegation_ladder  # noqa: E402  (Signatures 6 and 7, reused)

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LOOP = ["Frame", "Prompt", "Verify", "Decide", "Disclose"]


# ---------------------------------------------------------------- F7.1 Chapter map
def chapter_map(f):
    f.text(400, 30, "Chapter 7 at a glance", size=22, weight="700")
    cols = [("Evidence", ["7.1 Practice scores are not learning", "7.2 Retrieval practice",
                          "7.3 Feeling ready is not being ready"]),
            ("Use", ["7.4 Scaffold or crutch", "7.5 Setting up tutor mode"]),
            ("Do", ["7.6 Lab 7.1: tutor-mode session (Thu, Feb 11)", "A4: tutor-mode dialogue and reflection (due Feb 15)"])]
    for c, (head, items) in enumerate(cols):
        x = 30 + c * 255
        f.text(x + 115, 66, head, size=16, weight="700")
        for i, it in enumerate(items):
            role = "neutral" if c < 2 else ("verified" if i == 1 else "soft")
            kind = "human" if c == 2 else "step"
            f.box(x, 84 + i * 72, 230, 60, it, role=role, kind=kind, size=14)
        if c < 2:
            f.arrow(x + 236, 150, x + 252, 150)
    y = 340
    f.text(150, y, "AI Work Loop:", size=14, weight="700", anchor="end")
    xs = [230, 355, 480, 605, 730]
    for i, step in enumerate(LOOP):
        if step in ("Frame", "Verify"):
            f.box(xs[i] - 52, y - 20, 104, 40, step, role="highlight", kind="human", thick=True, size=15)
        else:
            f.text(xs[i], y, step, size=14, color=MUTED[f.mode])
        if i < 4:
            f.text((xs[i] + xs[i + 1]) / 2 - 2, y, "→", size=14, color=MUTED[f.mode])
    f.text(400, 382, "Frame: is the goal the output or the skill? Verify: check your learning, not only the tool's answer.",
           size=13, color=MUTED[f.mode])
    f.text(400, 408, "Opening case: a high-school math experiment in Türkiye (Bastani et al., 2025)", size=13,
           color=MUTED[f.mode])


# ---------------------------------------------------------------- F7.3 Session storyboard
def storyboard(f):
    f.text(120, 24, "Part 1", size=15, weight="700")
    f.text(410, 24, "Part 2: only this differed", size=15, weight="700")
    f.text(690, 24, "Part 3", size=15, weight="700")
    f.box(20, 120, 200, 110, "Teacher review", role="neutral", kind="human", size=15,
          sub="same for every class", sub_size=13)
    arms = [("Control", "books and notes, no devices", "neutral", "human", False),
            ("GPT Base", "chat built like ChatGPT, asked to act as a tutor", "ai", "ai", False),
            ("GPT Tutor", "hints, not answers; teachers' solutions in its instructions", "ai", "ai", True)]
    for i, (lab, sub, role, kind, thick) in enumerate(arms):
        y = 44 + i * 92
        f.box(290, y, 240, 80, lab, role=role, kind=kind, thick=thick, size=15, sub=sub, sub_size=13)
        f.arrow(222, 175, 288, y + 40)
        f.arrow(532, y + 40, 598, 175)
    f.box(600, 120, 180, 110, "Closed-book exam", role="neutral", kind="step", thick=True, size=15,
          sub="same for all; each problem paired with a practice problem", sub_size=13)
    f.text(400, 336, "Four 90-minute sessions, fall 2023–24; classrooms assigned by a balancing procedure; both parts graded.",
           size=13, color=MUTED[f.mode])
    f.text(400, 358, "Source: Bastani et al. (2025). Hexagon = AI component; rounded = people; thick = the learning measure.",
           size=13, color=MUTED[f.mode])


# ---------------------------------------------------------------- F7.5 Retrieval practice (with generation and spacing)
def retrieval_moves(f):
    heads = [(105, "What you do"), (400, "How it feels"), (655, "What it does")]
    for x, h in heads:
        f.text(x, 26, h, size=15, weight="700")
    rows = [("Retrieve", "recall from memory, then check", "Slower; more mistakes at first",
             "Stronger memory a week later than rereading (Roediger & Karpicke, 2006)", 46, 108, True),
            ("Generate", "produce the answer yourself", "Harder than reading it",
             "Remembered better than what you only read (Slamecka & Graf, 1978)", 172, 84, False),
            ("Space", "spread sessions over days", "You forget a little in between",
             "Beats cramming for later recall (Cepeda et al., 2006)", 274, 84, False)]
    for lab, sub, feels, does, y, h, main in rows:
        f.box(20, y, 170, h, lab, role="highlight" if main else "neutral", kind="human", thick=main,
              size=17 if main else 15, sub=sub, sub_size=13)
        f.box(222, y, 356, h, feels, role="soft", kind="step", size=14, weight="normal")
        f.box(600, y, 180, h, does, role="verified", kind="step", size=13, weight="normal")
        f.arrow(192, y + h / 2, 220, y + h / 2)
        f.arrow(580, y + h / 2, 598, y + h / 2)
    f.text(400, 386, "Retrieval practice is the core habit; generation and spacing support it.", size=13,
           color=MUTED[f.mode])
    f.text(400, 408, "A difficulty helps only if you can meet it with effort (Bjork & Bjork, 2011).", size=13,
           color=MUTED[f.mode])


# ---------------------------------------------------------------- F7.6 Feeling ready vs. being ready
def feel_ready(f):
    x0, y0, w, h = 170, 64, 300, 160
    cells = [("Calibrated", "Feel ready and are ready", "verified", False),
             ("Overconfident", "Feel ready but are not: the risk corner", "risk", True),
             ("Underconfident", "More ready than you think", "neutral", False),
             ("Calibrated", "Not ready, and you know to keep studying", "soft", False)]
    for i, (t, s, role, thick) in enumerate(cells):
        cx = x0 + (i % 2) * w
        cy = y0 + (i // 2) * h
        f.box(cx, cy, w - 10, h - 10, t, role=role, kind="step", thick=thick, size=16, sub=s, sub_size=13)
    f.text(x0 + w / 2 - 5, 44, "Are ready", size=14, weight="700")
    f.text(x0 + w * 1.5 - 5, 44, "Are not ready", size=14, weight="700")
    f.text(95, y0 + h / 2 - 5, "Feel\nready", size=14, weight="700")
    f.text(95, y0 + h * 1.5 - 5, "Do not feel\nready", size=14, weight="700")
    f.text(400, 410, "Predict, then check: the gap between your prediction and your score tells you which cell you are in.",
           size=13, color=MUTED[f.mode])
    f.text(400, 432, "Thick border and hatching mark the risk corner.", size=13, color=MUTED[f.mode])


# ---------------------------------------------------------------- F7.7 Jagged frontier from the learner's side (Signature 2 reuse)
def frontier_learner(f):
    jagged(f)  # Signature 2, unchanged (ch01_figures)
    f.box(40, 500, 350, 92, "● Inside the frontier", role="neutral", kind="step", thick=True, size=15,
          sub="The tool can do the task for you. If the skill is yours to build, this is where the crutch is easiest.",
          sub_size=13)
    f.box(410, 500, 350, 92, "○ Outside the frontier", role="neutral", kind="step", dashed=True, size=15,
          sub="The tool may be wrong. Only your own skill catches the error.", sub_size=13)


# ---------------------------------------------------------------- F7.8 Scaffold versus crutch (new reusable function)
def scaffold_crutch(highlight=None, note=None):
    """Turn-level comparison: the same AI reply with no attempt (crutch) and after an attempt (scaffold).

    highlight: None, "scaffold" or "crutch" (draws a thick frame around that lane).
    note: optional one-line remark printed at the bottom (a later chapter's point).
    """
    if highlight not in (None, "scaffold", "crutch"):
        raise ValueError("highlight must be None, 'scaffold' or 'crutch'")
    xs = [14 + i * 156 for i in range(5)]
    W = 140
    reply = "Same reply: worked steps and the answer"

    def draw(f):
        lanes = [("crutch", "Crutch: no attempt", 76), ("scaffold", "Scaffold: attempt first", 236)]
        for key, title, y in lanes:
            f.text(14, y - 20, title, size=15, weight="700", anchor="start")
            if highlight == key:
                f.raw(f'<rect x="6" y="{y - 40}" width="788" height="140" rx="10" fill="none" '
                      f'stroke="{INK[f.mode]}" stroke-width="3"/>')
        # crutch lane
        y = 76
        f.box(xs[0], y, W, 84, "A practice question", role="neutral", kind="step", size=14)
        f.arrow(xs[0] + W + 2, y + 42, xs[2] - 2, y + 42, dashed=True, label="no attempt", label_dy=-12, size=13)
        f.box(xs[2], y, W, 84, reply, role="ai", kind="ai", size=13)
        f.arrow(xs[2] + W + 2, y + 42, xs[3] - 2, y + 42)
        f.box(xs[3], y, W, 84, "You copy it", role="neutral", kind="human", size=14)
        f.arrow(xs[3] + W + 2, y + 42, xs[4] - 2, y + 42)
        f.box(xs[4], y, W, 84, "Output done; you recalled and produced nothing", role="risk", kind="step",
              thick=True, size=13)
        # scaffold lane
        y = 236
        f.box(xs[0], y, W, 84, "A practice question", role="neutral", kind="step", size=14)
        f.arrow(xs[0] + W + 2, y + 42, xs[1] - 2, y + 42)
        f.box(xs[1], y, W, 84, "You attempt first", role="highlight", kind="human", size=14)
        f.arrow(xs[1] + W + 2, y + 42, xs[2] - 2, y + 42)
        f.box(xs[2], y, W, 84, reply, role="ai", kind="ai", size=13)
        f.arrow(xs[2] + W + 2, y + 42, xs[3] - 2, y + 42)
        f.box(xs[3], y, W, 84, "You compare, redo and explain it back", role="highlight", kind="human", size=13)
        f.arrow(xs[3] + W + 2, y + 42, xs[4] - 2, y + 42)
        f.box(xs[4], y, W, 84, "You recalled and produced: skill built", role="verified", kind="step", size=13)
        f.text(400, 360, "Test for every turn: who recalled and produced the answer, you or the tool?", size=14,
               weight="700")
        f.text(400, 384, "Hexagon = the AI reply (identical in both lanes) · rounded = you · thick border = risk",
               size=13, color=MUTED[f.mode])
        if note:
            f.text(400, 408, note, size=13, italic=True, color=MUTED[f.mode])
    return draw


# ---------------------------------------------------------------- F7.11 Session protocol
def session_protocol(f):
    steps = [("1 · Before", "3 keyed check questions; first answers; confidence", "human", "neutral"),
             ("2 · During", "Tutor-mode dialogue on other problems: attempt first", "ai", "ai"),
             ("3 · Right after", "Devices away: rate, answer, score, calibration gap", "human", "neutral"),
             ("4 · Later", "2+ days: same steps, parallel questions if possible", "human", "neutral"),
             ("5 · Reflect", "Gaps; one S turn, one C turn; one change", "human", "verified")]
    for i, (h, t, kind, role) in enumerate(steps):
        x = 10 + i * 158
        f.text(x + 73, 30, h, size=15, weight="700")
        f.box(x, 50, 146, 150, t, role=role, kind=kind, thick=i in (2, 3), size=13.5, weight="normal")
        if i < 4:
            f.arrow(x + 147, 125, x + 157, 125)
    f.text(400, 232, "Thick border = closed-book checks (no tool, no notes). Hexagon = the AI tool; rounded = you.",
           size=13, color=MUTED[f.mode])
    f.text(400, 256, "Your scores are evidence for your reflection, not your grade.", size=13, color=MUTED[f.mode])


# ---------------------------------------------------------------- F7.12 A4 record sheet
def a4_sheet(f):
    ink = INK[f.mode]
    f.text(400, 22, "A4 record sheet", size=18, weight="700")
    cols = [20, 170, 370, 575, 780]
    heads = ["Check question", "Before: confidence · answer", "Right after: confidence · right?",
             "2+ days later: confidence · right?"]
    top = 44
    rh = 32
    for i, h in enumerate(heads):
        f.text((cols[i] + cols[i + 1]) / 2, top + 16, h, size=13, weight="700")
    rows = ["Q1 (keyed)", "Q2 (keyed)", "Q3 (keyed)", "Predicted score", "Actual score", "Gap (predicted − actual)"]
    for r in range(len(rows) + 2):
        f.line(cols[0], top + r * rh, cols[-1], top + r * rh, color=ink)
    for c in cols:
        f.line(c, top, c, top + (len(rows) + 1) * rh, color=ink)
    for r, lab in enumerate(rows):
        y = top + rh * (r + 1) + 16
        f.text(cols[0] + 8, y, lab, size=13, anchor="start", weight="700" if r >= 3 else "normal")
        for c in range(1, 4):
            if r < 3:
                cell = "___ %  ·  answer" if c == 1 else "___ %  ·  Y / N"
            elif r == 3:
                cell = "sum of % ÷ 100"
            elif r == 4:
                cell = "— " if c == 1 else "___ of 3"
            else:
                cell = "— " if c == 1 else "+ / − ___"
            f.text((cols[c] + cols[c + 1]) / 2, y, cell, size=13, color=MUTED[f.mode])
    cols2 = [20, 110, 220, 620, 780]
    heads2 = ["Turn #", "Code S / C", "Reason: which rule? who recalled and produced it?", "Error found?"]
    top2 = 282
    for i, h in enumerate(heads2):
        f.text((cols2[i] + cols2[i + 1]) / 2, top2 + 16, h, size=13, weight="700")
    for r in range(4):
        f.line(cols2[0], top2 + r * 30, cols2[-1], top2 + r * 30, color=ink)
    for c in cols2:
        f.line(c, top2, c, top2 + 3 * 30, color=ink)
    f.text(400, 396, "Add rows: at least 6 coded turns. Score against your source's key, not the tool's verdict.",
           size=13, color=MUTED[f.mode])
    f.text(400, 418, "Your score does not affect your grade; the record and the reflection do.", size=13,
           color=MUTED[f.mode])


# ---------------------------------------------------------------- F7.15 Summary card
def summary_card(f):
    f.text(400, 26, "Chapter 7: what you can do now", size=18, weight="700")
    cards = ["Performance with help is not learning: check without the tool",
             "Retrieve, generate, space: the effort is the point",
             "Predict, then check: find your calibration gap",
             "Ask of every turn: who recalled and produced it, you or the tool?",
             "Tutor mode: role, attempt-first constraints, one question per turn",
             "A4: a session record, scored against your source"]
    for i, c in enumerate(cards):
        x = 20 + (i % 3) * 258
        y = 50 + (i // 3) * 150
        f.box(x, y, 242, 130, c, role="neutral" if i % 2 else "soft", kind="human", size=14, weight="600")


TUTOR_NOTE = "Tutor mode changes the role, the constraints and the output format; the task stays the same."
LADDER_NOTES = {
    "augmentation": "Tutor mode: you attempt; the tool questions and hints",
    "automation": "Answer mode on a skill you are building: the crutch",
    "none": "Closed-book checks: the skill must show without the tool",
}

FIGS = [
    ("f7-01-chapter-map", chapter_map, 800, 430, "Chapter 7 at a glance"),
    ("f7-03-session-storyboard", storyboard, 800, 372,
     "Only the practice part of each session differed; the exam came right after, closed-book for everyone"),
    ("f7-05-retrieval-moves", retrieval_moves, 800, 422, "Recalling from memory feels harder and lasts longer"),
    ("f7-06-feel-ready", feel_ready, 800, 446, "Feeling ready and being ready are different"),
    ("f7-07-frontier-learner", frontier_learner, 800, 606,
     "Inside the tool's frontier, it can do the task for you; outside it, only your skill catches its errors"),
    ("f7-08-scaffold-crutch", scaffold_crutch(), 800, 400,
     "Scaffold versus crutch: the same AI reply builds skill only after your own attempt"),
    ("f7-10-tutor-anatomy", prompt_anatomy(["role", "constraints", "output format"], note=TUTOR_NOTE), 800, 495,
     "A tutor-mode setup changes the role, the constraints and the output format"),
    ("f7-11-session-protocol", session_protocol, 800, 270, "A tutor-mode session is a small experiment on yourself"),
    ("f7-12-a4-sheet", a4_sheet, 800, 432, "Your calibration gap is the evidence; your score is not the grade"),
    ("f7-14-ladder-skill", delegation_ladder("augmentation", annotate=LADDER_NOTES), 800, 570,
     "When the skill is yours to build, work on the floor or in augmentation, not automation"),
    ("f7-15-summary-card", summary_card, 800, 340, "Chapter 7 summary card"),
]

if __name__ == "__main__":
    for fid, fn, w, h, title in FIGS:
        render(fid, fn, w, h, title, ROOT)
        print("rendered", fid)
