"""Chapter 12 diagrams (SVG, color + gray). Run from the repo root:
    python3 figures/scripts/ch12_figures.py
Data charts (F12.7, F12.10, F12.14) are in ch12_charts.py (data/ch12_*.csv).

New reusable drawing introduced here (for Chapter 19's field guides):
    fit_matrix(parts, options, cells, highlight=None, note=None)   # the book-map "Task x tool fit matrix"

Reused, never redrawn: Signature 2 (`from ch01_figures import jagged`; ch01's `jagged(f)` has no highlight
argument, so F12.3 adds callouts below it, as Chapter 7 did), Signature 7 (`from ch05_figures import
delegation_ladder, RUNGS`), Signature 5 and the chain (`from ch04_figures import failure_tree, failure_chain,
tree_height`).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from figlib import render, MUTED, INK  # noqa: E402
from ch01_figures import jagged  # noqa: E402  (Signature 2, reused)
from ch04_figures import failure_tree, failure_chain, tree_height  # noqa: E402
from ch05_figures import delegation_ladder, RUNGS  # noqa: E402  (Signature 7, reused)

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LOOP = ["Frame", "Prompt", "Verify", "Decide", "Disclose"]


# ---------------------------------------------------------------- the fit matrix (new, reusable)
STATES = ("tested", "predicted", "blocked", "chosen")
RUNG_NAMES = {"none": "floor", "automation": "automation", "augmentation": "augmentation",
              "agency": "agency", None: ""}


def fit_matrix_height(n_parts=3, note=None):
    return 150 + n_parts * 112 + (24 if note else 0)


def fit_matrix(parts, options, cells, highlight=None, note=None):
    """The book-map figure "Task x tool fit matrix" (Signature 2 marks + Signature 7 rungs).

    parts:   up to 3 row labels (parts of a task).
    options: up to 3 column labels (tools, and usually "No AI").
    cells:   {(row, col): {"decision": str, "rung": one of RUNGS or None, "mark": "inside" | "outside" | None,
              "state": "tested" | "predicted" | "blocked" | "chosen", optional "note": short reason,
              optional "once": True for a cell tested in one run only}}  -> at most 9 cell boxes.
    highlight: optional set of (row, col) to draw thick (in addition to "chosen" cells).
    Grammar: chosen = verified fill, thick; blocked (data gate) = risk fill (hatched in gray), thick;
    predicted = dashed outline (uncertainty); tested = plain outline.
    """
    if len(parts) > 3 or len(options) > 3:
        raise ValueError("fit_matrix draws at most 3 parts x 3 options (9 boxes)")
    highlight = set(highlight or ())
    for key, c in cells.items():
        if c.get("state", "tested") not in STATES:
            raise ValueError(f"unknown state in cell {key}: {c.get('state')}")
        if c.get("rung") not in list(RUNGS) + [None]:
            raise ValueError(f"unknown rung in cell {key}: {c.get('rung')}")

    x0, cw, gap, y0, ch = 200, 186, 12, 84, 100

    def draw(f):
        muted = MUTED[f.mode]
        for j, opt in enumerate(options):
            f.text(x0 + j * (cw + gap) + cw / 2, y0 - 22, opt, size=15, weight="700", width=cw)
        for i, part in enumerate(parts):
            y = y0 + i * (ch + gap)
            f.text(20, y + ch / 2, part, size=14, weight="700", anchor="start", width=170)
            for j in range(len(options)):
                c = cells.get((i, j))
                if not c:
                    continue
                st = c.get("state", "tested")
                role = {"chosen": "verified", "blocked": "risk"}.get(st, "neutral")
                thick = st in ("chosen", "blocked") or (i, j) in highlight
                mark = {"inside": "● inside", "outside": "○ outside", None: ""}[c.get("mark")]
                rung = RUNG_NAMES[c.get("rung")]
                sub = " · ".join(t for t in (rung, mark, c.get("note"), "tested once" if c.get("once") else None) if t)
                f.box(x0 + j * (cw + gap), y, cw, ch, c["decision"], role=role, kind="step",
                      dashed=(st == "predicted"), thick=thick, size=14, sub=sub or None, sub_size=13)
        yl = y0 + len(parts) * (ch + gap) + 18
        f.text(400, yl, "Thick, filled = chosen · thick with risk fill (hatched in print) = blocked by the data gate · "
               "dashed = predicted, not tested", size=13, color=muted, width=780)
        f.text(400, yl + 24, "● inside / ○ outside the tool's frontier (Signature 2) · rung on the Delegation Ladder "
               "(Signature 7)", size=13, color=muted, width=780)
        if note:
            f.text(400, yl + 48, note, size=13, italic=True, color=muted, width=780)
    return draw


# ---------------------------------------------------------------- F12.1 Chapter map
def chapter_map(f):
    muted = MUTED[f.mode]
    f.text(400, 30, "Chapter 12 at a glance", size=22, weight="700")
    cols = [("What a tool is", ["12.1 Fit: a task and a tool together", "12.2 Kinds of tools",
                                "12.3 What studies of tool effects show"]),
            ("Testing and deciding", ["12.4–12.5 Total cost and the data gate", "12.6 A fair bake-off",
                                      "12.7–12.8 Fit matrix and re-testing"]),
            ("Practice", ["12.9 Lab 12.1 and A10 (Studio)", "Labs 12.2–12.3 (optional)",
                          "Case Study: the BCG consultants"])]
    for c, (head, items) in enumerate(cols):
        x = 30 + c * 255
        f.text(x + 115, 74, head, size=16, weight="700")
        for i, it in enumerate(items):
            role = "neutral" if c < 2 else ("verified" if i == 0 else "soft")
            kind = "human" if c == 2 else "step"
            f.box(x, 94 + i * 88, 230, 70, it, role=role, kind=kind, dashed=(c == 2 and i == 1), size=14)
        if c < 2:
            f.arrow(x + 236, 217, x + 252, 217)
    y = 372
    f.text(150, y, "AI Work Loop:", size=14, weight="700", anchor="end")
    xs = [215, 335, 445, 555, 660]
    for i, step in enumerate(LOOP):
        if step == "Frame":
            f.box(xs[i] - 50, y - 20, 100, 40, step, role="highlight", kind="human", thick=True, size=15)
        elif step == "Verify":
            f.box(xs[i] - 50, y - 17, 100, 34, step, role="neutral", kind="human", dashed=True, size=14)
        else:
            f.text(xs[i], y, step, size=14, color=muted)
        if i < 4:
            f.text((xs[i] + xs[i + 1]) / 2, y, "→", size=14, color=muted)
    f.text(400, 410, "This chapter strengthens Frame (which tool, if any, fits this part?), then Verify (dashed): "
           "test the fit before you rely on it.", size=13, color=muted, width=780)
    f.text(400, 436, "Opening case: consultants who used one tool on many tasks (BCG, 2023), revisited", size=13,
           color=muted)


# ---------------------------------------------------------------- F12.2 BCG design
def design(f):
    muted = MUTED[f.mode]
    f.box(20, 150, 150, 80, "Baseline task", role="neutral", kind="step", size=15, sub="no AI · all 758")
    f.arrow(172, 190, 202, 190)
    f.box(204, 130, 130, 120, "Random assignment", role="neutral", kind="decision", size=14)
    groups = [("No AI", "human", "neutral"), ("GPT-4", "ai", "ai"), ("GPT-4 + prompting overview", "ai", "ai")]
    for i, (lab, kind, role) in enumerate(groups):
        y = 60 + i * 95
        f.box(370, y, 180, 70, lab, role=role, kind=kind, size=14)
        f.arrow(334, 190, 368, y + 35)
    f.box(590, 70, 190, 90, "Inside the frontier", role="neutral", kind="step", size=14,
          sub="18 subtasks · 385 consultants")
    f.box(590, 220, 190, 90, "Outside the frontier", role="neutral", kind="step", thick=True, size=14,
          sub="one task · 373 consultants")
    f.arrow(552, 190, 588, 115)
    f.arrow(552, 190, 588, 265)
    f.box(250, 360, 300, 64, "Measured: correctness · rated quality · time", role="verified", kind="step", size=14)
    f.arrow(685, 312, 552, 392)
    f.text(400, 450, "Everyone with AI: the same model (GPT-4, end of April 2023) with the provider's default options.",
           size=13, color=muted, width=780)
    f.text(400, 474, "Source: Dell'Acqua et al. (2023), Harvard Business School Working Paper 24-013; Organization Science (2026).",
           size=13, color=muted)


# ---------------------------------------------------------------- F12.3 Jagged frontier, one part and two tools
def frontier_two_tools(f):
    jagged(f)  # Signature 2, unchanged (ch01_figures)
    f.text(400, 500, "Sam's unit conversion, 41 oz-in to N·m: the same part, two tools (constructed example)", size=14,
           weight="700")
    f.box(40, 518, 350, 92, "Tool A, no calculation: ○ outside", role="neutral", kind="step", dashed=True,
          size=14, sub="Gave 2.9 N·m, ten times too large; the right answer is about 0.29 N·m",
          sub_size=13)
    f.box(410, 518, 350, 92, "Tool B, runs code: ● inside", role="neutral", kind="step", thick=True,
          size=14, sub="Matched his hand calculation on one known-answer test; one run, so test more",
          sub_size=13)


# ---------------------------------------------------------------- F12.5 Tool anatomy (no flow arrows; Ch. 15 owns data flows)
def tool_anatomy(f):
    muted = MUTED[f.mode]
    f.box(310, 190, 180, 90, "Model", role="ai", kind="ai", size=18, sub="settings (parameters)", sub_size=13)
    f.box(220, 30, 360, 100, "What it receives", role="neutral", kind="step", size=15,
          sub="your prompt · files you upload · your mail and documents · web pages it retrieves", sub_size=13)
    f.box(20, 180, 250, 110, "What it can do", role="neutral", kind="step", size=15,
          sub="produce text · search · run code · act for you (Chapter 14)", sub_size=13)
    f.box(530, 180, 250, 110, "Where it runs", role="neutral", kind="step", size=15,
          sub="provider's service · institution's license · hardware you or your institution control", sub_size=13)
    f.box(220, 340, 360, 100, "Whose terms cover your input", role="neutral", kind="step", thick=True, size=15,
          sub="used for training? · kept how long, seen by whom? · consumer or institutional contract",
          sub_size=13)
    for (x1, y1, x2, y2) in [(400, 130, 400, 190), (270, 235, 310, 235), (490, 235, 530, 235), (400, 280, 400, 340)]:
        f.line(x1, y1, x2, y2, width=1.6)
    f.text(400, 470, "Two tools built on the same model can differ in all four. Thick border: the part that decides the "
           "data gate (section 12.5).", size=13, color=muted, width=780)


# ---------------------------------------------------------------- F12.8 Total cost of use
def cost(f):
    muted, ink = MUTED[f.mode], INK[f.mode]
    f.text(250, 30, "What you see", size=15, weight="700")
    f.box(60, 50, 180, 60, "Price", role="neutral", kind="step", size=15)
    f.box(260, 50, 180, 60, "Usage limits", role="neutral", kind="step", size=15)
    f.line(20, 140, 500, 140, width=2.4, color=ink)
    f.text(250, 164, "What you also pay", size=15, weight="700")
    below = [("Checking time", "verification cost: often the largest", True),
             ("Learning time", "prompts, options, quirks", False),
             ("Data you give up", "under its data terms (12.5)", False),
             ("Switching cost", "lock-in (12.8)", False)]
    for i, (lab, sub, thick) in enumerate(below):
        x = 40 + (i % 2) * 230
        y = 186 + (i // 2) * 106
        f.box(x, y, 210, 90, lab, role="risk" if thick else "neutral", kind="step", thick=thick, size=15,
              sub=sub, sub_size=13)
    f.box(560, 150, 220, 150, "No-AI baseline", role="human", kind="human", size=16,
          sub="the time the part takes you without a tool, done to your criteria", sub_size=13)
    f.arrow(555, 225, 490, 225, label="compare", label_dy=-12, size=13)
    f.text(400, 420, "Total cost of use = everything above and below the line. Thick border: the cost students most "
           "often leave out.", size=13, color=muted, width=780)


# ---------------------------------------------------------------- F12.9 The data gate
def data_gate(f):
    muted = MUTED[f.mode]
    f.box(20, 130, 200, 170, "Data class of the input", role="neutral", kind="step", size=15,
          sub="Public · internal or confidential · restricted or legally protected; also: personal data about others; your own work",
          sub_size=13)
    f.arrow(222, 215, 248, 215)
    f.box(250, 140, 210, 150, "Do the tool's data terms allow this class?", role="neutral", kind="decision", size=14)
    f.arrow(460, 215, 558, 215, label="yes", label_dy=-12, size=13)
    f.box(560, 170, 220, 90, "Pass: now test quality", role="verified", kind="step", size=15,
          sub="the bake-off (12.6)", sub_size=13)
    f.arrow(355, 290, 355, 318, label=None)
    f.text(368, 304, "no", size=13, color=muted, italic=True, anchor="start")
    f.box(260, 320, 190, 130, "Can you change the input?", role="neutral", kind="decision", size=14)
    f.text(30, 360, "For example: remove names,", size=13, color=muted, anchor="start")
    f.text(30, 380, "use placeholders, leave out", size=13, color=muted, anchor="start")
    f.text(30, 400, "confidential details", size=13, color=muted, anchor="start")
    f.arrow(450, 385, 640, 262)
    f.text(560, 340, "yes", size=13, color=muted, italic=True)
    f.arrow(355, 450, 355, 476)
    f.text(368, 463, "no", size=13, color=muted, italic=True, anchor="start")
    f.box(220, 478, 270, 64, "Blocked for this part, whatever its quality", role="risk", kind="step", thick=True,
          size=14)
    f.text(530, 470, "Three questions about the terms:", size=13, weight="700", anchor="start")
    f.text(530, 492, "1 training · 2 retention and access", size=13, color=muted, anchor="start")
    f.text(530, 512, "3 consumer or institutional contract", size=13, color=muted, anchor="start")


# ---------------------------------------------------------------- F12.11 A fair bake-off
def bake_off(f):
    muted = MUTED[f.mode]
    same = [("Same frame and criteria", 20), ("Same prompt, word for word", 200),
            ("Same test inputs: typical · different · edge", 380)]
    for lab, x in same:
        f.box(x, 40, 165, 80, lab, role="neutral", kind="step", size=14)
    f.arrow(186, 80, 198, 80)
    f.arrow(366, 80, 378, 80)
    f.text(640, 80, "Only the tool changes", size=15, weight="700")
    opts = [("Tool A", "fresh chat, memory off; tool, model, date", "ai", "ai", 60),
            ("Tool B", "fresh chat, memory off; tool, model, date", "ai", "ai", 300),
            ("No AI", "you, timed", "human", "human", 540)]
    for lab, sub, role, kind, x in opts:
        f.box(x, 180, 200, 80, lab, role=role, kind=kind, size=15, sub=sub, sub_size=13)
        f.arrow(462, 122, x + 100, 178)
    f.box(150, 320, 500, 70, "Score separately: correctness (independent check) · polish 1–5 · time incl. checking",
          role="verified", kind="step", size=14)
    for x in (160, 400, 640):
        f.arrow(x, 262, 400 + (x - 400) * 0.6, 318)
    f.box(280, 420, 240, 56, "Verdict per input, not per tool", role="neutral", kind="step", thick=True, size=14)
    f.arrow(400, 392, 400, 418)
    f.text(400, 500, "The edge input matters most: it is where a tool is most likely to produce something that was not "
           "there.", size=13, color=muted, width=780)


# ---------------------------------------------------------------- F12.12 Sam's fit matrix (fit_matrix instance)
SAM_PARTS = ["Sponsor thank-you emails", "Datasheet summaries", "Torque calculation"]
SAM_OPTIONS = ["Tool A (institutional)", "Tool B (consumer)", "No AI"]
SAM_CELLS = {
    (0, 0): {"decision": "Use with a check", "rung": "automation", "mark": "inside", "state": "chosen"},
    (0, 1): {"decision": "Do not use: blocked", "rung": None, "mark": None, "state": "blocked",
             "note": "personal data"},
    (0, 2): {"decision": "Do not use", "rung": "none", "mark": None, "state": "predicted", "note": "slower"},
    (1, 0): {"decision": "Use, check every unit", "rung": "automation", "mark": "inside", "state": "chosen"},
    (1, 1): {"decision": "Only as a lead", "rung": "automation", "mark": "outside", "state": "tested"},
    (1, 2): {"decision": "Do not use", "rung": "none", "mark": None, "state": "tested", "note": "10 min each"},
    (2, 0): {"decision": "Do not use", "rung": None, "mark": "outside", "state": "tested"},
    (2, 1): {"decision": "Use with a check", "rung": "automation", "mark": "inside", "state": "tested",
             "once": True},
    (2, 2): {"decision": "Use", "rung": "none", "mark": None, "state": "chosen", "note": "fastest"},
}
SAM_MATRIX = fit_matrix(SAM_PARTS, SAM_OPTIONS, SAM_CELLS,
                        note="Constructed example. Re-test when either tool changes its model or terms, or a new "
                             "datasheet format arrives.")

# ---------------------------------------------------------------- F12.13 Signature 7 reused
SAM_LADDER = delegation_ladder(highlight=["none", "automation"],
                               annotate={"automation": "Sam: sponsor emails; datasheet summaries (check every unit)",
                                         "none": "Sam: torque calculation, in his own spreadsheet"},
                               note="Chapter 12: each part of a task gets its own rung, and sometimes the floor")


# ---------------------------------------------------------------- F12.15 Portability and re-test triggers
def portability(f):
    muted = MUTED[f.mode]
    f.text(200, 30, "Keep in your own files", size=16, weight="700")
    f.text(600, 30, "Stays with the tool unless you copy it", size=16, weight="700")
    keep = ["Task frames and success criteria", "Prompts and test inputs", "Outputs you need, exported"]
    stay = ["Chat history", "Standing instructions and memory", "Access tied to a school or job"]
    for i, (k, s) in enumerate(zip(keep, stay)):
        y = 50 + i * 82
        f.box(40, y, 320, 66, k, role="verified", kind="human", size=15)
        f.box(440, y, 320, 66, s, role="neutral", kind="step", dashed=True, size=15)
    f.box(40, 320, 720, 90, "Re-test triggers", role="neutral", kind="step", thick=True, size=16,
          sub="a model update or retirement · a change in price or terms · a new kind of input · a new job or school",
          sub_size=14)
    f.text(400, 440, "Rounded = what you control · dashed = what you can lose when a tool changes or your access ends",
           size=13, color=muted, width=780)


# ---------------------------------------------------------------- F12.16 A10 sheet
def a10_sheet(f):
    muted = MUTED[f.mode]
    rows = [("1 Task", "parts · predictions per tool · frame and criteria · data class"),
            ("2 Tools", "kind · how the model is reached · model · date"),
            ("3 Data gate", "three questions per tool, cited · pass, changed input, or blocked"),
            ("4 Runs", "route A, B or C · same prompt · typical, different, edge · fresh chats"),
            ("5 Scores", "correctness (independent check) · polish 1–5 · time incl. checking"),
            ("6 Cost row", "price form · limits · checking time · no-AI baseline (estimate)"),
            ("7 Fit matrix", "decision · rung · reason per cell · predicted / tested once · re-test trigger"),
            ("8 Judgment", "80–100 words, one comparison with a 12.3 study · declaration, five elements")]
    for i, (lab, sub) in enumerate(rows):
        y = 20 + i * 56
        f.box(20, y, 160, 46, lab, role="human" if i in (0, 7) else "neutral",
              kind="human" if i in (0, 7) else "step", size=15, thick=(i == 2))
        f.text(200, y + 23, sub, size=14, anchor="start", width=580)
    f.text(400, 482, "Thick border: the gate comes before any quality score.", size=13, color=muted)


# ---------------------------------------------------------------- F12.17 Three ways of working (no shares)
def three_modes(f):
    muted = MUTED[f.mode]
    modes = [("Centaurs, about 14%", "divide the work: decide which parts go to the tool, keep the rest",
              "≈ a fit matrix in practice", "neutral", False, False),
             ("Cyborgs, about 60%", "work with the tool turn by turn, down to sentences and subtasks",
              "≈ augmentation", "neutral", False, False),
             ("Self-automators, about 27%", "hand over the whole task in one or two exchanges, with little review",
              "≈ automation without its check", "risk", True, True)]
    for i, (lab, sub, mapping, role, thick, dashed) in enumerate(modes):
        x = 20 + i * 260
        f.box(x, 40, 240, 170, lab, role=role, kind="human", thick=thick, size=17, sub=sub, sub_size=14)
        f.text(x + 120, 240, mapping, size=14, weight="700", italic=True)
    f.text(400, 300, "Centaurs and cyborgs: Dell'Acqua et al. (2023). Self-automators and shares (244 consultants): "
           "Randazzo et al. (2025), as summarized by the authors.", size=13, color=muted, width=780)
    f.text(400, 346, "Mapping onto the Delegation Ladder (italic) is this book's reading. Thick border: the pattern "
           "with the least review.", size=13, color=muted, width=780)


# ---------------------------------------------------------------- F12.20 Summary card
def summary_card(f):
    f.text(400, 26, "Chapter 12 — what you can do now", size=18, weight="700")
    cards = ["Describe a tool: what it receives, can do, where it runs, whose terms",
             "Read a study by its setting, measure, users and date",
             "Count the total cost, against a no-AI baseline",
             "Pass the data gate before any quality test",
             "Run a fair bake-off: correctness, polish and time apart",
             "Decide cell by cell, with a rung; re-test when things change"]
    for i, c in enumerate(cards):
        x = 20 + (i % 3) * 258
        y = 50 + (i // 3) * 150
        f.box(x, y, 242, 130, c, role="neutral" if i % 2 else "soft", kind="human", size=14, weight="600")


# ---------------------------------------------------------------- F12.21 Open weights vs. open source
def open_layers(f):
    muted = MUTED[f.mode]
    layers = [("Parameters (weights)", "what you download and run", "ai", "ai"),
              ("Code to train and run the system", None, "neutral", "step"),
              ("Information about the training data", "enough to build a similar system", "neutral", "step")]
    for i, (lab, sub, role, kind) in enumerate(layers):
        y = 40 + i * 92
        f.box(170, y, 380, 76, lab, role=role, kind=kind, size=15, sub=sub, sub_size=13)
    f.box(580, 40, 200, 260, "License terms", role="neutral", kind="step", dashed=True, size=15,
          sub="what you may do: use, study, change, share; some licenses limit uses", sub_size=13)
    f.line(158, 40, 158, 116, width=3)
    f.text(146, 70, "open-weight", size=13, weight="700", anchor="end")
    f.text(146, 90, "release", size=13, weight="700", anchor="end")
    f.line(50, 40, 50, 300, width=3)
    f.text(62, 210, "open source", size=13, weight="700", anchor="start")
    f.text(62, 230, "AI (OSI):", size=13, weight="700", anchor="start")
    f.text(62, 250, "all three", size=13, weight="700", anchor="start")
    f.text(400, 330, "Open-weight release: the top layer, under a license. Open Source AI Definition (OSI, 2024): all three "
           "layers, under terms that allow use, study, change and sharing.", size=13, color=muted, width=760)


# ---------------------------------------------------------------- reused signatures (Case Study)
BCG_TREE = failure_tree({"hallucination"}, dashed={"hallucination"},
                        tag="Case: BCG outside task (2023) · hallucination (contradicts its input, or wrong reasoning), "
                            "inferred (dashed)",
                        note="The task was designed so the tool would err; the paper does not report each "
                             "consultant's outputs")
BCG_CHAIN = failure_chain(
    notes={0: "Answer went against the interview notes (inferred)",
           1: "Less questioning (authors' statement)",
           2: "Wrong recommendation submitted",
           3: "An experiment: no real-world harm"},
    highlight={1, 2}, dashed={0},
    tag="Links 2 and 3 documented by the authors' statement; Chapter 11 calls this pattern automation bias")

FIGS = [
    ("f12-01-chapter-map", chapter_map, 800, 455, "Chapter 12 at a glance"),
    ("f12-02-design", design, 800, 490,
     "Everyone with AI had the same tool and default options; only the task and the training differed"),
    ("f12-03-frontier-two-tools", frontier_two_tools, 800, 624,
     "One part, two tools: a calculation can sit outside one tool's frontier and inside another's"),
    ("f12-05-tool-anatomy", tool_anatomy, 800, 490,
     "A tool is a model plus what it receives, what it can do, where it runs and whose terms cover it"),
    ("f12-08-cost", cost, 800, 440, "The price is the smallest part of what a tool costs you"),
    ("f12-09-data-gate", data_gate, 800, 548, "Data terms are a gate: a tool that fails it is out, whatever its quality"),
    ("f12-11-bake-off", bake_off, 800, 520, "A fair bake-off changes only the tool"),
    ("f12-12-fit-matrix", SAM_MATRIX, 800, fit_matrix_height(3, note=True),
     "One workflow, different fits: each part gets its own tool, or none"),
    ("f12-13-ladder-sam", SAM_LADDER, 800, 590, "Fit includes how you use the tool: Sam's parts on the ladder"),
    ("f12-15-portability", portability, 800, 460,
     "Keep what you built outside any one tool, and re-test when something changes"),
    ("f12-16-a10-sheet", a10_sheet, 800, 500, "Your matrix records the evidence behind every fit decision"),
    ("f12-17-three-modes", three_modes, 800, 380,
     "Consultants who solved the hard task split the work with the tool in different ways"),
    ("f12-18-tree-bcg", BCG_TREE, 800, tree_height() + 34, "BCG on the tree: hallucination that contradicts its input, inferred"),
    ("f12-19-chain-bcg", BCG_CHAIN, 800, 420,
     "Wrong outputs became wrong recommendations where people adopted them with less questioning"),
    ("f12-20-summary-card", summary_card, 800, 340, "Chapter 12 summary card"),
    ("f12-21-open-layers", open_layers, 800, 370,
     "Open weights let you run a model; open source also lets you study how it was made"),
]

if __name__ == "__main__":
    only = set(sys.argv[1:])
    for fid, fn, w, h, title in FIGS:
        if only and fid not in only:
            continue
        render(fid, fn, w, h, title, ROOT)
        print("rendered", fid)
