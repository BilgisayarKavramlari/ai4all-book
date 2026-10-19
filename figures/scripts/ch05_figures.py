"""Chapter 5 diagrams (SVG, color + gray). Run from the repo root:
    python3 figures/scripts/ch05_figures.py
Data charts (F5.10, F5.14) are in ch05_charts.py (published values in data/ch05_*.csv).

Two signature diagrams are introduced here and are imported by later chapters:

    from ch05_figures import prompt_anatomy, delegation_ladder

* Signature 6, Anatomy of a Prompt: `prompt_anatomy(highlight=None, note=None)`.
  Parts: "role", "task", "context", "constraints", "in-context examples", "output format".
  `highlight` is one part name or a list of part names (aliases: "examples", "format").
  Example: prompt_anatomy(highlight="context")  (Ch. 6);  prompt_anatomy(["role", "constraints"])  (Ch. 10).
* Signature 7, The Delegation Ladder: `delegation_ladder(highlight=None, annotate=None, note=None)`.
  Rungs: "none" (the floor: no AI), "automation", "augmentation", "agency".
  `highlight` is one rung or a list; `annotate` maps a rung to a short note printed under it.
  Example: delegation_ladder("agency")  (Ch. 14).

Both functions return a draw(f) callable for figlib.render(). Do not redraw them elsewhere.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from figlib import render, MUTED, INK  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LOOP = ["Frame", "Prompt", "Verify", "Decide", "Disclose"]


def _as_set(x):
    if x is None:
        return set()
    if isinstance(x, str):
        return {x}
    return set(x)


# ---------------------------------------------------------------- Signature 6: Anatomy of a Prompt
PROMPT_PARTS = ["role", "task", "context", "constraints", "in-context examples", "output format"]
_ALIASES = {"examples": "in-context examples", "format": "output format"}


def prompt_anatomy(highlight=None, note=None):
    """Signature 6 (8 shapes): six prompt parts inside 'Your prompt' -> the AI tool -> output.

    highlight: one part name or a list (see PROMPT_PARTS; aliases "examples", "format").
    note: optional one-line remark printed at the bottom (a later chapter's point).
    """
    hl = {_ALIASES.get(p, p) for p in _as_set(highlight)}
    unknown = hl - set(PROMPT_PARTS)
    if unknown:
        raise ValueError(f"unknown prompt part(s): {sorted(unknown)}")

    spec = {
        "role": ("Role", "voice and perspective", (36, 84, 172, 100)),
        "context": ("Context", "what this task needs", (216, 84, 172, 100)),
        "in-context examples": ("In-context examples", "sample input with the output you want",
                                (396, 84, 172, 100)),
        "task": ("Task", "the verb and what it acts on: always needed", (120, 204, 362, 92)),
        "constraints": ("Constraints", "limits and must-nots", (126, 318, 172, 100)),
        "output format": ("Output format", "a shape you can check", (306, 318, 172, 100)),
    }

    def draw(f):
        f.box(20, 46, 564, 388, "", role="soft", kind="step")
        f.text(34, 64, "Your prompt", size=15, weight="700", anchor="start")
        for key in PROMPT_PARTS:
            label, sub, (x, y, w, h) = spec[key]
            on = key in hl
            f.box(x, y, w, h, label, role="highlight" if on else "neutral", kind="human",
                  thick=key == "task", size=15, sub=sub, sub_size=13)
        f.arrow(588, 240, 618, 240)
        f.box(622, 196, 162, 88, "The AI tool", role="ai", kind="ai", size=15,
              sub="receives only what is written", sub_size=13)
        f.arrow(703, 288, 703, 330)
        f.box(632, 334, 142, 84, "Output", role="neutral", kind="step", size=15,
              sub="scored against your criteria", sub_size=13)
        f.text(400, 458, "Rounded boxes = parts you write (thick border = always needed; dark = highlighted here) · hexagon = AI component",
               size=13, color=MUTED[f.mode])
        if note:
            f.text(400, 482, note, size=13, color=MUTED[f.mode], italic=True)
    return draw


# ---------------------------------------------------------------- Signature 7: The Delegation Ladder
RUNGS = ["none", "automation", "augmentation", "agency"]


def delegation_ladder(highlight=None, annotate=None, note=None):
    """Signature 7 (7 shapes): a floor (no AI) and three rungs, each with your part and the AI's part.

    One axis: how hard it is to see and check what the AI contributed before it takes effect.
    highlight: one rung or a list (see RUNGS). annotate: {rung: short note} printed under the rung.
    note: optional one-line remark printed at the bottom.
    """
    hl = _as_set(highlight)
    annotate = annotate or {}
    unknown = (hl | set(annotate)) - set(RUNGS)
    if unknown:
        raise ValueError(f"unknown rung(s): {sorted(unknown)}")

    rows = [  # rung, y, your part (label, sub), AI part
        ("agency", 52, ("3 · Agency", "you configure AI to carry out future tasks for you, including for others"),
         "acts later, without you checking each output"),
        ("augmentation", 172, ("2 · Augmentation", "you and the AI shape the task together, turn by turn"),
         "suggests, drafts and questions inside your thinking"),
        ("automation", 292, ("1 · Automation", "you define the task; the AI carries it out"),
         "produces an output you can check before you use it"),
    ]

    def draw(f):
        # axis
        f.arrow(52, 470, 52, 60, width=2.2)
        f.text(66, 40, "Harder to see and check what the AI contributed before it takes effect",
               size=13, weight="700", anchor="start")
        f.text(66, 512, "Easier to check", size=13, anchor="start", color=MUTED[f.mode])
        # rails
        f.line(84, 46, 84, 488, width=3)
        f.line(784, 46, 784, 488, width=3)
        for rung, y, (lab, sub), ai in rows:
            on = rung in hl
            f.box(100, y, 330, 84, lab, role="highlight" if on else "neutral", kind="human",
                  thick=on, size=16, sub=sub, sub_size=13)
            f.box(446, y + 4, 322, 76, ai, role="ai", kind="ai", thick=on, size=14, weight="600")
            if rung in annotate:
                f.text(434, y + 100, annotate[rung], size=13, italic=True, color=INK[f.mode])
        on = "none" in hl
        f.box(100, 412, 668, 66, "Floor · No AI: you do this part yourself",
              role="highlight" if on else "soft", kind="human", thick=on, size=16,
              sub="always an option", sub_size=13)
        if "none" in annotate:
            f.text(434, 496, annotate["none"], size=13, italic=True, color=INK[f.mode])
        f.text(400, 534, "The ladder, its floor and its axis are this book's arrangement of the AI Fluency "
               "framework's three modalities (Dakan & Feller, 2025).", size=13, color=MUTED[f.mode])
        f.text(400, 554, "The framework ranks none of them; one task often mixes several. A higher rung "
               "is not a better use.", size=13, color=MUTED[f.mode])
        if note:
            f.text(400, 576, note, size=13, italic=True, color=MUTED[f.mode])
    return draw


# ---------------------------------------------------------------- F5.1 Chapter map
def chapter_map(f):
    f.text(400, 30, "Chapter 5 at a glance", size=22, weight="700")
    cols = [("Frame", ["5.1 Frame before you prompt", "5.2 How much to hand over: the Delegation Ladder"]),
            ("Prompt", ["5.3 The anatomy of a prompt", "5.4 Iterate on purpose"]),
            ("Test and do", ["5.5 One result is not evidence", "5.6 Lab 5.1: iteration sprint (in class)",
                             "A3: prompt and iteration log"])]
    for c, (head, items) in enumerate(cols):
        x = 30 + c * 255
        f.text(x + 115, 70, head, size=16, weight="700")
        for i, it in enumerate(items):
            role = "neutral" if c < 2 else ("verified" if i == 2 else "soft")
            kind = "human" if c == 2 else "step"
            f.box(x, 88 + i * 82, 230, 66, it, role=role, kind=kind, size=14)
        if c < 2:
            f.arrow(x + 236, 154, x + 252, 154)
    y = 360
    f.text(150, y, "AI Work Loop:", size=14, weight="700", anchor="end")
    xs = [205, 320, 440, 550, 650]
    for i, step in enumerate(LOOP):
        if step in ("Frame", "Prompt"):
            f.box(xs[i] - 52, y - 20, 104, 40, step, role="highlight", kind="human", thick=True, size=15)
        else:
            f.text(xs[i], y, step, size=14, color=MUTED[f.mode])
        if i < 4:
            f.text((xs[i] + xs[i + 1]) / 2 + 4, y, "→", size=14, color=MUTED[f.mode])
    f.text(400, 400, "This chapter strengthens Frame (what the task is, what good looks like) and Prompt.",
           size=13, color=MUTED[f.mode])
    f.text(400, 426, "Opening case: Klarna's AI assistant, 2024–2025", size=13, color=MUTED[f.mode])


# ---------------------------------------------------------------- F5.2 Task frame card
def frame_card(f):
    f.text(400, 28, "Task frame", size=20, weight="700")
    items = [("Goal", "what the result is for"),
             ("Audience", "who will use it, and what they already know"),
             ("Success criteria", "3–5 checks you can score met, partly or not met"),
             ("Limits", "length, sources, time, data you may not use"),
             ("What stays with you", "decisions, judgments, the final check"),
             ("A rung for each part (added in 5.2)", "no AI, automation, augmentation or agency, part by part")]
    for i, (lab, sub) in enumerate(items):
        x = 40 + (i % 2) * 370
        y = 56 + (i // 2) * 106
        f.box(x, y, 350, 88, lab, role="neutral", kind="human", thick=(lab == "Success criteria"),
              size=16, sub=sub, sub_size=13)
    f.text(400, 392, "Write it before the first prompt; every version is scored against the criteria.",
           size=13, color=MUTED[f.mode])


# ---------------------------------------------------------------- F5.3b Lucía's parts on the ladder
LUCIA_PARTS = {"agency": "Not now: a study-group chatbot for common questions would answer classmates without her",
               "augmentation": "Part 3: why does the example budget confuse readers?",
               "automation": "Part 2: draft the handout text (checked against her criteria)",
               "none": "Part 1: choose what first-year students need; Part 4: final check"}


# ---------------------------------------------------------------- F5.4 Three questions
def three_questions(f):
    qs = [("Can you check the result before it takes effect?",
           "Yes: automation can fit. Not yet: add a check first, or keep the part with you (no AI or augmentation)."),
          ("What would an error cost, and who would bear it?",
           "Low, and only you: any rung can fit. High, or borne by others: no agency without a human check "
           "before the output reaches them (Chapter 14)."),
          ("Is this skill yours to build?",
           "Yes: no AI, or augmentation used as a tutor (Chapter 7). No: let the other two questions decide.")]
    for i, (q, a) in enumerate(qs):
        y = 26 + i * 132
        f.box(24, y, 330, 118, q, role="neutral", kind="decision", size=14)
        f.arrow(358, y + 59, 390, y + 59)
        f.box(394, y + 14, 382, 90, "", role="soft", kind="step")
        f.text(585, y + 59, a, size=13, width=360)
    f.text(400, 432, "Weigh all three together. They are questions to think with, not a formula.",
           size=13, color=MUTED[f.mode])


# ---------------------------------------------------------------- F5.5 Klarna storyboard
def klarna_storyboard(f):
    panels = [("February 2024", "Confirmed (press release): 2.3 million chats in month one, two-thirds of chats, "
               "work equal to 700 full-time staff, satisfaction about the same as with people, more accurate "
               "resolution (its claim) with 25% fewer repeat questions; a person available on request."),
              ("May 2025", "Reported (Bloomberg interview, via other outlets): the chief executive said cost had "
               "been too dominant and quality was lower; customers must always be able to reach a human."),
              ("November 2025", "Reported (CX Dive): the chief executive said the assistant did the work of more than 853 "
               "full-time staff and had saved about $60 million.")]
    for i, (when, txt) in enumerate(panels):
        x = 20 + i * 262
        f.box(x, 40, 236, 250, "", role="neutral", kind="step", thick=(i == 1))
        f.text(x + 118, 64, when, size=16, weight="700")
        f.text(x + 118, 170, txt, size=13, width=210)
        if i < 2:
            f.arrow(x + 240, 165, x + 258, 165)
    f.text(400, 314, "Every figure is the company's own statement; none is an independent measurement.",
           size=13, color=MUTED[f.mode])
    f.text(400, 336, "Sources: Klarna (2024); Fisher (2025); Shibu (2025); Doerer (2025).",
           size=13, color=MUTED[f.mode])


# ---------------------------------------------------------------- F5.7 Lucía v1 vs v2
def lucia_v1_v2(f):
    f.box(20, 30, 250, 200, "", role="soft", kind="step")
    f.text(145, 52, "v1 (first prompt)", size=15, weight="700")
    f.text(145, 120, "Write a one-page handout for first-year students on how to make a monthly budget. "
           "Include one worked example as a table. Use plain language.", size=13, width=222)
    f.text(145, 258, "Missing: the figures that were in her notes.", size=13,
           width=240, italic=True, color=MUTED[f.mode])
    f.box(290, 30, 490, 470, "", role="neutral", kind="step")
    f.text(535, 52, "Final prompt, v5 (parts labeled)", size=15, weight="700")
    lines = [("Task", "Write a one-page handout for first-year students on how to make a monthly budget."),
             ("Context", "Use only these monthly figures: income $1,150; rent $650; groceries $280; phone $45; "
                         "transport $60."),
             ("Constraints", "Use plain language. Refer to tools in general terms, such as \"a spreadsheet or "
                             "a notebook\"; do not name any product, bank or app. Explain every money term in "
                             "everyday words the first time you use it. If costs are higher than income, say so "
                             "and show the gap."),
             ("Output format", "Include one worked example as a table.")]
    y = 80
    for tag, txt in lines:
        n = max(1, len(txt) // 46 + 1)
        h = max(44, 18 * n + 14)
        f.box(302, y, 112, h, tag, role="highlight" if tag == "Context" else "neutral", kind="human",
              thick=(tag == "Task"), size=13)
        f.text(426, y + h / 2, txt, size=13, width=340, anchor="start")
        y += h + 14
    f.text(535, 452, "No role and no in-context examples: this task did not need them.", size=13,
           italic=True, color=MUTED[f.mode])
    f.text(535, 476, "v2 to v5 each added one line (sections 5.4 and 5.5).", size=13,
           italic=True, color=MUTED[f.mode])


# ---------------------------------------------------------------- F5.8 Iteration loop
def iteration_loop(f):
    import math
    steps = ["1. Diagnose the weak output", "2. Trace it to a prompt part (or the frame)",
             "3. Change one thing", "4. Predict the effect", "5. Rerun in a fresh chat, twice",
             "6. Score against the criteria", "7. Log it; keep or revert"]
    cx, cy, rx, ry = 400, 262, 292, 178
    pos = []
    for i in range(7):
        a = -math.pi / 2 + i * 2 * math.pi / 7
        pos.append((cx + rx * math.cos(a), cy + ry * math.sin(a)))
    for i in range(7):
        x1, y1 = pos[i]
        x2, y2 = pos[(i + 1) % 7]
        dx, dy = x2 - x1, y2 - y1
        f.arrow(x1 + dx * 0.36, y1 + dy * 0.36, x1 + dx * 0.64, y1 + dy * 0.64, curve=-14)
    for i, (x, y) in enumerate(pos):
        f.box(x - 92, y - 32, 184, 64, steps[i], role="neutral", kind="step", size=13)
    f.box(cx - 104, cy - 34, 208, 68, "Back to Frame", role="neutral", kind="human", dashed=True, size=14,
          sub="when the trace ends at the task itself", sub_size=13)
    x2, y2 = pos[1]
    f.arrow(x2 - 70, y2 + 30, cx + 90, cy - 30, dashed=True)
    f.text(400, 476, "The Prompt ↔ Verify part of the AI Work Loop. Dashed = taken only when needed.",
           size=13, color=MUTED[f.mode])


# ---------------------------------------------------------------- F5.9 Why-chain
def why_chain(f):
    nodes = [("Weak output", "the example budget's total is wrong; two numbers were invented", "risk", False),
             ("Why?", "no figures were in the prompt, so the output filled in plausible ones", "neutral", False),
             ("Why?", "the frame card said to use the association's figures, but they were never pasted",
              "neutral", False),
             ("Why?", "they were in Lucía's notes, not in the prompt", "neutral", False),
             ("Fix (v2)", "add the figures as context; predict: every number matches", "verified", False)]
    y = 26
    for i, (lab, sub, role, dashed) in enumerate(nodes):
        f.box(40, y, 470, 74, lab, role=role, kind="human" if i == 4 else "step", thick=(i == 0),
              size=15, sub=sub, sub_size=13)
        if i < 4:
            f.arrow(275, y + 76, 275, y + 92)
            if 0 < i:
                f.text(520, y + 37, "checked", size=13, anchor="start", weight="700")
        y += 94
    f.text(520, 26 + 37, "observed in 2 runs", size=13, anchor="start", weight="700")
    f.box(604, 200, 186, 110, "Or is the model just bad at sums?", role="neutral", kind="step", dashed=True,
          size=14, sub="assumed, not checked yet", sub_size=13)
    f.arrow(512, 100, 640, 196, dashed=True)
    f.text(697, 330, "v2 tests it", size=13, italic=True, color=MUTED[f.mode])
    f.text(400, 500, "Solid = a link you checked · dashed = a link you only assumed", size=13,
           color=MUTED[f.mode])


# ---------------------------------------------------------------- F5.11 Test grid
def test_grid(f):
    f.text(400, 24, "Lucía's v4: three test inputs × two runs, five criteria", size=15, weight="700")
    cols = ["Run 1", "Run 2"]
    rows = [("Typical", "the association's figures"), ("Different", "income that changes month to month"),
            ("Edge", "costs higher than income")]
    cells = [[("All 5 met", "verified"), ("All 5 met", "verified")],
             [("All 5 met", "verified"), ("Format partly met: list, not a table", "soft")],
             [("All 5 met", "verified"), ("Numbers not met: invented income line", "risk")]]
    for j, c in enumerate(cols):
        f.text(390 + j * 200, 58, c, size=14, weight="700")
    for i, (r, sub) in enumerate(rows):
        y = 76 + i * 88
        f.text(150, y + 28, r, size=15, weight="700")
        f.text(150, y + 50, sub, size=13, width=200, color=MUTED[f.mode])
        for j in range(2):
            lab, role = cells[i][j]
            f.box(300 + j * 200, y, 180, 70, lab, role=role, kind="step", thick=(role == "risk"), size=13)
    f.box(260, 344, 460, 58, "Verdict: not yet. It fails on the edge input, so v5 adds a rule for budgets "
          "that do not balance.", role="neutral", kind="human", size=13)
    f.text(400, 424, "Shaded = met · light = partly met · hatched with a thick border = not met", size=13,
           color=MUTED[f.mode])


# ---------------------------------------------------------------- F5.12 Peer swap test
def peer_swap(f):
    f.box(20, 40, 170, 80, "Your latest prompt", role="neutral", kind="human", size=14,
          sub="in the lab, v3; no explanation", sub_size=13)
    f.arrow(194, 80, 222, 80)
    f.box(226, 40, 170, 80, "A classmate runs it", role="neutral", kind="human", size=14,
          sub="fresh, temporary chat", sub_size=13)
    f.arrow(400, 80, 428, 80)
    f.box(432, 40, 160, 80, "Output", role="ai", kind="ai", size=15)
    f.arrow(596, 80, 624, 80)
    f.box(628, 40, 152, 80, "Scored against your criteria", role="neutral", kind="human", size=13)
    f.arrow(704, 124, 704, 160)
    f.box(614, 164, 180, 110, "A gap?", role="neutral", kind="decision", size=15)
    f.arrow(614, 219, 474, 219, label="yes")
    f.box(184, 184, 286, 76, "Write what was in your head into the prompt; rerun", role="neutral",
          kind="step", size=14)
    f.arrow(704, 278, 704, 310)
    f.text(716, 294, "no", size=13, italic=True, anchor="start", color=MUTED[f.mode])
    f.box(520, 314, 260, 70, "Evidence the prompt carries its own context", role="verified",
          kind="step", size=14)
    f.text(400, 414, "Rounded = a person · hexagon = AI · diamond = decision", size=13, color=MUTED[f.mode])


# ---------------------------------------------------------------- F5.13 Log template
def log_template(f):
    heads = ["Version", "Part changed", "Prediction", "Run 1", "Run 2", "Keep?"]
    widths = [70, 160, 170, 140, 170, 60]
    rows = [["v2", "Context: pasted the figures", "Every number matches the figures", "5 of 5 met",
             "4 of 5: names a budgeting app", "Keep"],
            ["v3", "Constraint: tools in general terms; no product, bank or app", "No product named; nothing else changes",
             "5 of 5 met", "4 met, 1 partly: a money term unexplained", "Keep"],
            ["Frame", "C3 rewritten after the peer swap", "(no new run; rescore v3)", "C3 partly met",
             "C3 partly met", "Keep"],
            ["Your row", "", "", "", "", ""]]
    x0, y0, rh = 20, 40, 66
    f.box(x0, y0, sum(widths), rh * 5, "", role="neutral", kind="step")
    f.box(x0, y0, sum(widths), rh, "", role="soft", kind="step")
    x = x0
    for k, w in enumerate(widths):
        f.text(x + w / 2, y0 + rh / 2, heads[k], size=13, weight="700", width=w - 8)
        for r in range(4):
            f.text(x + w / 2, y0 + rh * (r + 1) + rh / 2, rows[r][k], size=13, width=w - 8)
        if k:
            f.line(x, y0, x, y0 + rh * 5, width=1)
        x += w
    for r in range(1, 5):
        f.line(x0, y0 + rh * r, x0 + sum(widths), y0 + rh * r, width=1)
    f.text(400, 396, "One change per row, a prediction before the run, scores tied to your criteria.",
           size=13, color=MUTED[f.mode])
    f.text(400, 418, "Constructed example (Lucía's log); the empty row is yours.", size=13, italic=True,
           color=MUTED[f.mode])


# ---------------------------------------------------------------- F5.16 Techniques (Deep 5.A)
def techniques(f):
    techs = [("Step-by-step prompting", "ask for intermediate steps"),
             ("Ask what it needs", "list missing information first"),
             ("Split into steps", "a prompt chain (Chapter 6)")]
    for i, (lab, sub) in enumerate(techs):
        y = 30 + i * 100
        f.box(20, y, 230, 80, lab, role="neutral", kind="step", size=14, sub=sub, sub_size=13)
        f.arrow(254, y + 40, 300, 170)
    f.box(304, 128, 150, 84, "The AI tool", role="ai", kind="ai", size=15)
    f.arrow(458, 170, 488, 170)
    f.box(492, 136, 110, 68, "Output", role="neutral", kind="step", size=15)
    f.arrow(606, 170, 626, 170)
    f.box(630, 100, 160, 140, "Meets your criteria?", role="neutral", kind="decision", size=14)
    f.text(400, 336, "A technique changes how the model is asked; only your criteria say whether the result is good.",
           size=13, color=MUTED[f.mode])


# ---------------------------------------------------------------- F5.15 Summary card
def summary_card(f):
    f.text(400, 26, "Chapter 5: what you can do now", size=18, weight="700")
    cards = ["Frame: goal, audience, 3–5 checkable criteria, limits, what stays with you",
             "Delegate by part: no AI, automation, augmentation or agency, with a reason",
             "Prompt: give the parts the task needs; the task is always one of them",
             "Iterate: trace the weak output, change one thing, predict, rerun, score",
             "Test: repeated runs, typical, different and edge inputs, a peer swap",
             "Log it: A3 shows each change, each prediction and each score"]
    for i, c in enumerate(cards):
        x = 20 + (i % 3) * 258
        y = 50 + (i // 3) * 150
        f.box(x, y, 242, 130, c, role="neutral" if i % 2 else "soft", kind="human", size=14, weight="600")


FIGS = [
    ("f5-01-chapter-map", chapter_map, 800, 445, "Chapter 5 at a glance"),
    ("f5-02-frame-card", frame_card, 800, 410, "A task frame says what good looks like before the first prompt"),
    ("f5-03-delegation-ladder", delegation_ladder(), 800, 570,
     "The higher the rung, the harder it is to check what the AI contributed before it takes effect"),
    ("f5-03b-ladder-lucia", delegation_ladder(annotate=LUCIA_PARTS), 800, 570,
     "One task, several rungs: Lucía places each part of her handout"),
    ("f5-04-three-questions", three_questions, 800, 450,
     "Three questions point to different rungs; they are weighed, not computed"),
    ("f5-05-klarna-storyboard", klarna_storyboard, 800, 350,
     "Klarna's public account moved from efficiency (2024) to quality and a promise of human help (May 2025), then back to AI savings (Nov 2025)"),
    ("f5-06-prompt-anatomy", prompt_anatomy(), 800, 475,
     "A prompt has six parts; the task is the only one you always need"),
    ("f5-07-lucia-v1-v2", lucia_v1_v2, 800, 510, "The framed prompt carries what Lucía knew but had not written down"),
    ("f5-08-iteration-loop", iteration_loop, 800, 492,
     "Iteration is the loop between Prompt and Verify: one change, a prediction, a rerun, a score"),
    ("f5-09-why-chain", why_chain, 800, 515,
     "Asking why more than once traces a weak output back to the prompt, or to the frame"),
    ("f5-11-test-grid", test_grid, 800, 440, "A prompt works when it passes across runs and test inputs, not once"),
    ("f5-12-peer-swap", peer_swap, 800, 430, "A peer swap test shows what was in your head but not in your prompt"),
    ("f5-13-log-template", log_template, 800, 432, "A strong log shows one change, one prediction and one score at a time"),
    ("f5-15-summary-card", summary_card, 800, 340, "Chapter 5 summary card"),
    ("f5-16-techniques", techniques, 800, 360,
     "A technique changes how the model is asked; your criteria still judge the result"),
]

if __name__ == "__main__":
    for fid, fn, w, h, title in FIGS:
        render(fid, fn, w, h, title, ROOT)
        print("rendered", fid)
