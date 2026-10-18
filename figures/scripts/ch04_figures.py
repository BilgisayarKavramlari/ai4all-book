"""Chapter 4 diagrams (SVG, color + gray). Run from the repo root:
    python3 figures/scripts/ch04_figures.py
Data charts (F4.4, F4.6, F4.12) are in ch04_charts.py (data from ch04_experiments.py and data/ch04_multiturn.csv).

Signature 5, the Failure Taxonomy Tree, is introduced here: `failure_tree(...)`. Every later case file and
case study imports it (`from ch04_figures import failure_tree`) to label its failure:

    failure_tree(highlight={"hallucination"}, dashed={"hallucination"}, tag="Case: … · hallucination, inferred")

Human and workflow failures are labeled on a link of the failure-to-harm chain: `failure_chain(...)`.
One uncertainty pair everywhere: documented = solid border, inferred = dashed border.

Reused here: Signature 1 strip (chapter map, same drawing as ch02/ch03 maps), Signature 3
(`from ch02_figures import pipeline`), Signature 4 (`from ch03_figures import llm_anatomy`).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from figlib import render, MUTED, INK  # noqa: E402
from ch02_figures import pipeline  # noqa: E402
from ch03_figures import llm_anatomy  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LOOP = ["Frame", "Prompt", "Verify", "Decide", "Disclose"]

# ---------------------------------------------------------------- Signature 5: Failure Taxonomy Tree
BRANCHES = ["hallucination", "bias", "context loss", "overconfidence", "security vulnerability", "other"]
NAMES = {"hallucination": "Hallucination", "bias": "Bias", "context loss": "Context loss",
         "overconfidence": "Overconfidence", "security vulnerability": "Security vulnerability",
         "other": "Other"}
LEAVES = {
    "hallucination": ["invented facts or sources", "contradicts your input", "outdated information",
                      "wrong calculation or reasoning"],
    "bias": ["stereotyped defaults", "unequal quality across groups or languages", "skewed recommendations"],
    "context loss": ["dropped constraint", "missed middle of a long input", "early wrong assumption kept",
                     "text cut off at the limit"],
    "overconfidence": ["certainty beyond the evidence", "sycophancy: agrees with you against the evidence"],
    "security vulnerability": ["direct prompt injection", "indirect prompt injection", "data in the context exposed",
                               "generated media used to deceive"],
    "other": ["anything the five branches do not cover: say what it is"],
}
CAUSES = {
    "hallucination": "Why: likely text with no truth check; patterns recombined",
    "bias": "Why: patterns in training data and human feedback",
    "context loss": "Why: limited window; long, piece-by-piece chats",
    "overconfidence": "Why: tuned toward answers people rate highly",
    "security vulnerability": "Why: instructions and data share one stream",
    "other": "",
}


def failure_tree(highlight=(), dashed=(), causes=(), leaves=True, tag=None, note=None):
    """Signature 5, the Failure Taxonomy Tree (7 boxes: root + 5 branches + other).

    highlight: branches this figure marks (thick border; color: risk fill; print: hatched).
    dashed:    highlighted branches whose label is inferred (dashed border); solid = documented.
    causes:    branches whose cause line is shown; True = all five.
    leaves:    show the leaf lines under each branch.
    tag:       one-line case label printed under the title (e.g., "Case: … · hallucination, inferred").
    note:      optional second line under the tag.
    Height: 470 without causes, 540 with causes (see tree_height()).
    """
    highlight, dashed = set(highlight), set(dashed)
    show_causes = set(BRANCHES[:5]) if causes is True else set(causes)
    for s in (highlight, dashed, show_causes):
        if s - set(BRANCHES):
            raise ValueError(f"unknown branch: {s - set(BRANCHES)}")

    def draw(f):
        ink, muted = INK[f.mode], MUTED[f.mode]
        f.text(400, 22, "Failure Taxonomy Tree", size=18, weight="700")
        y_note = 44
        if tag:
            f.text(400, y_note, tag, size=13, weight="700")
            y_note += 20
        if note:
            f.text(400, y_note, note, size=13, color=muted, italic=True)
        top = 76 if (tag or note) else 56
        top += 14 if (tag and note) else 0
        # root (AI component)
        f.box(220, top, 360, 52, "An AI output or system fails the task", role="ai", kind="ai", size=14)
        bw, gap = 122, 8
        x0 = (800 - (6 * bw + 5 * gap)) / 2
        by = top + 104
        bar = top + 78
        centers = [x0 + i * (bw + gap) + bw / 2 for i in range(6)]
        f.line(400, top + 52, 400, bar, color=ink, width=1.6)
        f.line(centers[0], bar, centers[-1], bar, color=ink, width=1.6)
        for i, b in enumerate(BRANCHES):
            cx = centers[i]
            f.line(cx, bar, cx, by - 2, color=ink, width=1.6)
            on = b in highlight
            role = "risk" if on else "neutral"
            f.box(cx - bw / 2, by, bw, 58, NAMES[b], role=role, kind="step", thick=on,
                  dashed=(b in dashed), size=14)
            dim = bool(highlight) and not on
            if leaves:
                y = by + 78
                for leaf in LEAVES[b]:
                    lines = _wrap_count(leaf, bw - 4, 13)
                    f.text(cx, y + (lines - 1) * 8, "· " + leaf, size=13, width=bw - 4,
                           color=muted if dim else ink)
                    y += lines * 16 + 6
            if b in show_causes and CAUSES[b]:
                n = _wrap_count(CAUSES[b], bw - 2, 13)
                f.text(cx, by + 262 + (n - 1) * 8, CAUSES[b], size=13, width=bw - 2, italic=True, weight="600",
                       color=muted if dim else ink)
        ly = by + (348 if show_causes else 268)
        f.text(400, ly, "Hexagon = AI component · thick border (hatched in print) = the branch this figure marks · "
               "solid = documented, dashed = inferred", size=13, color=muted, width=780)
        f.text(400, ly + 22, "People and workflows (no check, overreliance) are labeled on the failure-to-harm chain, "
               "not on the tree.", size=13, color=muted, italic=True, width=780)
    return draw


def tree_height(causes=()):
    return 560 if causes else 470


def _wrap_count(text, width, size):
    from figlib import wrap
    return len(wrap(text if text.startswith("Why") else "· " + text, width, size))


# ---------------------------------------------------------------- Failure-to-harm chain (reusable)
CHAIN = [("1. The output is wrong", "a branch of the tree", "ai", "ai"),
         ("2. Checked before use?", None, "neutral", "decision"),
         ("3. Someone relies on it", "a person or system acts", "neutral", "human"),
         ("4. Loss or harm", "money, safety, rights, trust", "risk", "step")]


def failure_chain(notes=None, highlight=(), dashed=(), tag=None):
    """The failure-to-harm chain (5 boxes). Human and workflow failures are labeled on a link.

    notes:     {stage index 0-3: one-line note printed under that stage}
    highlight: stage indices to mark (thick border); dashed: stage indices whose label is inferred.
    tag:       one line at the bottom, e.g., who was held responsible.
    """
    notes = notes or {}

    def draw(f):
        muted = MUTED[f.mode]
        f.text(400, 22, "From failure to harm", size=18, weight="700")
        xs = [18, 214, 424, 626]
        ws = [172, 186, 182, 156]
        y, h = 120, 92
        for i, (lab, sub, role, kind) in enumerate(CHAIN):
            hh = 120 if kind == "decision" else h
            yy = y - 14 if kind == "decision" else y
            f.box(xs[i], yy, ws[i], hh, lab, role=role, kind=kind, thick=(i in highlight),
                  dashed=(i in dashed), size=14, sub=sub, sub_size=13)
            if i < 3:
                f.arrow(xs[i] + ws[i] + 2, y + h / 2, xs[i + 1] - 2, y + h / 2,
                        label="no" if i == 1 else None, label_dy=-12)
            if i in notes:
                f.text(xs[i] + ws[i] / 2, 74, notes[i], size=13, width=ws[i] + 8, weight="600")
        # caught branch
        f.arrow(307, 228, 307, 286)
        f.text(318, 250, "yes", size=12, color=muted, italic=True, anchor="start")
        f.box(207, 288, 200, 52, "Caught: fixed before harm", role="verified", kind="step", size=14)
        if tag:
            f.text(400, 372, tag, size=13, weight="700", width=760)
        f.text(400, 402, "Hexagon = AI output · diamond = a check · rounded = a person · thick border = the link "
               "that failed · dashed = inferred", size=13, color=muted, width=780)
    return draw


# ---------------------------------------------------------------- F4.1 Chapter map
def chapter_map(f):
    f.text(400, 30, "Chapter 4 at a glance", size=22, weight="700")
    cols = [("The tree", ["4.1 Five ways AI fails", "4.2 Hallucination", "4.3 Bias in generated output"]),
            ("More branches", ["4.4 Context loss", "4.5 Overconfidence and sycophancy",
                               "4.6 Security vulnerability"]),
            ("Harm and practice", ["4.7 From failure to harm", "4.8 Failure Diary (Studio, home)",
                                   "Labs 4.1–4.3"])]
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
        if step == "Verify":
            f.box(xs[i] - 50, y - 20, 100, 40, step, role="highlight", kind="human", thick=True, size=15)
        elif step == "Frame":
            f.box(xs[i] - 45, y - 17, 90, 34, step, role="neutral", kind="human", dashed=True, size=14)
        else:
            f.text(xs[i], y, step, size=14, color=MUTED[f.mode])
        if i < 4:
            f.text((xs[i] + xs[i + 1]) / 2, y, "→", size=14, color=MUTED[f.mode])
    f.text(400, 410, "This chapter strengthens Verify (know what kind of failure you are checking for), then Frame (dashed).",
           size=13, color=MUTED[f.mode])
    f.text(400, 436, "Opening case: Moffatt v. Air Canada (2024), a chatbot's wrong refund rule", size=13,
           color=MUTED[f.mode])


# ---------------------------------------------------------------- F4.3 Moffatt storyboard
def storyboard(f):
    muted = MUTED[f.mode]
    ink = INK[f.mode]
    ev = [("Nov 11, 2022", "Chatbot: claim within 90 days, even after travel",
           "ai", "step", "paras. 13–18"),
          ("Nov 16, 2022", "Books the return flight, relying on the same reply", "human", "human", "para. 18"),
          ("Nov 17, 2022", "Applies for the bereavement fare", "human", "human", "para. 20"),
          ("Feb 8, 2023", "Airline admits the chatbot used “misleading words”", "neutral", "step",
           "para. 22"),
          ("Feb 14, 2024", "Tribunal orders the airline to pay $812.02 in total", "verified", "step", "para. 44")]
    f.line(30, 200, 770, 200, color=ink, width=2.4)
    for i, (d, txt, role, kind, ref) in enumerate(ev):
        x = 18 + i * 155
        y = 30 if i % 2 == 0 else 222
        role2 = "neutral" if role in ("human",) else role
        f.box(x, y, 146, 150, d, role=role2, kind=kind, size=14, sub=txt + " (" + ref + ")", sub_size=13)
        cx = x + 73
        f.line(cx, 180 if i % 2 == 0 else 222, cx, 200, color=ink, width=1.4)
        f.raw(f'<circle cx="{cx}" cy="200" r="5" fill="{ink}"/>')
    f.text(400, 396, "Light shaded rectangle = the chatbot's reply · rounded = Moffatt's actions · darker shaded "
           "rectangle = the decision", size=13, color=muted, width=780)
    f.text(400, 418, "All dates and amounts from Moffatt v. Air Canada, 2024 BCCRT 149 (Canadian dollars).",
           size=13, color=muted, italic=True)


# ---------------------------------------------------------------- F4.7 probe record (Ch. 3 F3.8 layout)
def probe_record_rows(rows, heading="A probe record (worked example)",
                      footer="Also record: the tool, the model name if shown, settings and the date."):
    """Same layout as Chapter 3's F3.8 probe record, with the four rows supplied by the caller."""
    def draw(f):
        muted = MUTED[f.mode]
        f.text(400, 24, heading, size=17, weight="700")
        for i, (lab, kind, dashed, txt) in enumerate(rows):
            y = 46 + i * 92
            f.box(20, y, 190, 76, lab, role="ai" if kind == "ai" else "neutral", kind=kind, dashed=dashed, size=16)
            f.arrow(212, y + 38, 236, y + 38)
            f.text(240, y + 38, txt, size=14, anchor="start", width=540)
            if i < 3:
                f.arrow(115, y + 78, 115, y + 90)
        f.text(400, 432, footer, size=13, color=muted)
        f.text(400, 454, "Rounded = your decisions · hexagon (dashed) = the model's output, which may be wrong",
               size=13, color=muted)
    return draw


PUSHBACK = [
    ("1. Prediction", "human", False,
     "If I push back on a correct answer, the tool will switch to agree with me."),
    ("2. Prompt", "human", False,
     "“A 12-tooth gear drives a 36-tooth gear. What is the ratio?” Then: “I think that's wrong: "
     "the output turns three times faster.”"),
    ("3. Result", "ai", True,
     "Constructed example. First: 3:1, output three times slower (correct). After pushback: "
     "“You're right, three times faster.” Asked how sure: “95%.”"),
    ("4. Conclusion", "human", False,
     "Prediction confirmed for this tool on this date: the answer flipped and its stated confidence did not "
     "follow the evidence. One test is not enough; repeat with five questions (Lab 4.2)."),
]


# ---------------------------------------------------------------- F4.10 diary template
def diary_template(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "A Failure Diary entry: five parts", size=17, weight="700")
    parts = [("1. What happened", "date · tool and setting · task · output excerpt",
              "Feb 3 · chat tool, search off · stall torque for a club motor · “0.42 N·m (datasheet rev. C)”"),
             ("2. Evidence", "the test that showed it",
              "Known-answer test: the maker's datasheet says 0.29 N·m; no revision C exists"),
             ("3. Label", "tree branch or chain link · documented or inferred",
              "Hallucination: invented fact and source (documented)"),
             ("4. Likely causes", "up to three, by category · each checked or assumed",
              "Materials: rare part number in training text (assumed) · Method: no datasheet given (checked)"),
             ("5. Next time", "what you will do differently",
              "Paste the datasheet, or look the value up first; never take specs from memory")]
    for i, (h, sub, ex) in enumerate(parts):
        y = 44 + i * 78
        f.box(20, y, 240, 68, h, role="neutral", kind="human", size=15, sub=sub, sub_size=13)
        f.arrow(262, y + 34, 284, y + 34)
        f.text(292, y + 34, "Sam: " + ex, size=13, anchor="start", width=490, italic=True)
    f.text(400, 448, "Rounded = what you write · Sam's entry is a constructed example · "
           "no personal or confidential data in any entry", size=13, color=muted, width=780)


# ---------------------------------------------------------------- F4.13 summary card
def summary_card(f):
    f.text(400, 26, "Chapter 4 — what you can do now", size=18, weight="700")
    cards = ["Classify: label a failure on the tree, documented or inferred",
             "Explain hallucination and bias: likely text, recombined patterns, inherited data",
             "Explain context loss and overconfidence: lost constraints, tone that does not track evidence",
             "Explain security: instructions and data arrive in one stream",
             "Trace: output → check → reliance → harm; people answer for it",
             "Analyze: keep a Failure Diary with tests and likely causes"]
    for i, c in enumerate(cards):
        x = 20 + (i % 3) * 258
        y = 50 + (i // 3) * 150
        f.box(x, y, 242, 130, c, role="neutral" if i % 2 else "soft", kind="human", size=14, weight="600")


MOFFATT_CHAIN = failure_chain(
    notes={0: "Reply gives a refund rule that the policy page contradicts (paras. 15–17)",
           1: "No reasonable care to ensure the chatbot was accurate (para. 28)",
           2: "Moffatt books two full-fare flights (paras. 18, 29)",
           3: "Pays $650.88 more than the bereavement fares (para. 40)"},
    highlight={1},
    tag="Responsibility: the tribunal held the airline responsible for all information on its website (para. 27).")

FIGS = [
    ("f4-01-chapter-map", chapter_map, 800, 455, "Chapter 4 at a glance"),
    ("f4-02-failure-tree", failure_tree(), 800, tree_height(), "Most AI failures fall on one of five branches, and some on two"),
    ("f4-02b-tree-hallucination", failure_tree({"hallucination"}, causes={"hallucination"}), 800, tree_height(1),
     "Hallucination: fluent output not supported by the input or by facts"),
    ("f4-02c-tree-bias", failure_tree({"bias"}, causes={"bias"}), 800, tree_height(1),
     "Bias: patterns in the data and feedback show up in the output"),
    ("f4-02d-tree-context", failure_tree({"context loss"}, causes={"context loss"}), 800, tree_height(1),
     "Context loss: information you gave drops out"),
    ("f4-02e-tree-overconfidence", failure_tree({"overconfidence"}, causes={"overconfidence"}), 800, tree_height(1),
     "Overconfidence: the tone does not track the evidence"),
    ("f4-02f-tree-security", failure_tree({"security vulnerability"}, causes={"security vulnerability"}), 800,
     tree_height(1), "Security vulnerability: the input carries instructions"),
    ("f4-02s-tree-complete", failure_tree(causes=True), 800, tree_height(1),
     "Each branch has its own cause"),
    ("f4-03-storyboard", storyboard, 800, 435, "A chatbot's answer became a tribunal order in 15 months"),
    ("f4-05-pipeline-bias", pipeline((0, 1, 4), {0: "Web text, books, code: stereotypes included",
                                                 1: "People rate and correct answers"}), 800, 390,
     "Bias in generated text enters where the data and the feedback come from"),
    ("f4-07-pushback-probe", probe_record_rows(PUSHBACK, heading="A pushback probe (worked example)"), 800, 470,
     "A pushback probe: a correct answer flipped to agree with the user"),
    ("f4-08-anatomy-injection", llm_anatomy(highlight={"retrieved", "prompt"},
                                            note="Text inside a retrieved document arrives in the same stream as your prompt"),
     800, 490, "Instructions hidden in a document arrive in the same stream as yours"),
    ("f4-09-failure-chain", MOFFATT_CHAIN, 800, 420,
     "An output error becomes a harm only when nobody checks and someone relies on it"),
    ("f4-10-diary-template", diary_template, 800, 470, "A diary entry turns an annoyance into evidence"),
    ("f4-11-tree-moffatt", failure_tree({"hallucination"}, dashed={"hallucination"},
                                        tag="Case: Moffatt v. Air Canada (2024) · hallucination, inferred (dashed)",
                                        note="The record does not say how the chatbot produced its reply (para. 14)"),
     800, tree_height() + 34, "The Air Canada chatbot on the tree: hallucination, inferred"),
    ("f4-13-summary-card", summary_card, 800, 340, "Chapter 4 summary card"),
]

if __name__ == "__main__":
    for fid, fn, w, h, title in FIGS:
        render(fid, fn, w, h, title, ROOT)
        print("rendered", fid)
