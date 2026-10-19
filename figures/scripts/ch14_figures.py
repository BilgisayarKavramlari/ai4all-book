"""Chapter 14 diagrams (SVG, color + gray). Run from the repo root:
    python3 figures/scripts/ch14_figures.py
Data charts (F14.6, F14.8) are in ch14_charts.py (data from ch14_experiments.py).

Signature 9, the Agent Loop with Approval Gates, is introduced here and imported by later chapters:

    from ch14_figures import agent_loop, LOOP_PARTS
    agent_loop(highlight=None, gate="hard", annotate=None, note=None)

Parts (LOOP_PARTS): "goal", "plan", "gate", "tool", "observation", "check", "stop", "handback", "log" (9 shapes).
  highlight: one part or a list of parts (thick border; person parts drawn in the highlight fill).
  gate:      "hard" (solid diamond: the system cannot skip it), "soft" (hatched risk diamond labeled
             "Soft gate: an instruction (may be skipped)": an instruction in the context asking the model to ask
             first), or None (no gate: the plan goes straight to
             the tool call, drawn as a thick risk arrow).
  annotate:  {part: short note} printed next to that part.
  note:      one line at the bottom.
Examples: agent_loop(highlight="gate") (Ch. 14);
          agent_loop(highlight="observation", annotate={"observation": "a retrieved page carries an instruction"}) (Ch. 15).

Reused, never redrawn: Signature 1 strip (chapter map), Signature 5 and the chain (`from ch04_figures import
failure_tree, failure_chain, tree_height`), Signature 7 (`from ch05_figures import delegation_ladder`).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from figlib import render, MUTED, INK  # noqa: E402
from ch04_figures import failure_tree, failure_chain, tree_height  # noqa: E402
from ch05_figures import delegation_ladder  # noqa: E402  (Signature 7, reused)

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LOOP = ["Frame", "Prompt", "Verify", "Decide", "Disclose"]


def _as_set(x):
    if x is None:
        return set()
    if isinstance(x, str):
        return {x}
    return set(x)


# ---------------------------------------------------------------- Signature 9: Agent Loop with Approval Gates
LOOP_PARTS = ["goal", "plan", "gate", "tool", "observation", "check", "stop", "handback", "log"]
_ANN = {  # part -> (x, y, width) of its annotation
    "goal": (95, 166, 160), "plan": (350, 172, 130), "gate": (497, 190, 160), "tool": (705, 166, 150),
    "observation": (690, 352, 180), "check": (475, 344, 170), "stop": (265, 372, 170),
    "handback": (95, 344, 160), "log": (400, 482, 760),
}


def agent_loop(highlight=None, gate="hard", annotate=None, note=None):
    """Signature 9 (9 shapes): goal -> plan -> approval gate -> tool call -> observation -> check point ->
    stop condition -> (no) next pass / (yes) hand back; a log strip records every pass."""
    hl = _as_set(highlight)
    annotate = annotate or {}
    unknown = (hl | set(annotate)) - set(LOOP_PARTS)
    if unknown:
        raise ValueError(f"unknown loop part(s): {sorted(unknown)}")
    if gate not in ("hard", "soft", None):
        raise ValueError("gate must be 'hard', 'soft' or None")

    def person(part):
        return "highlight" if part in hl else "neutral"

    def draw(f):
        muted = MUTED[f.mode]
        f.box(20, 70, 150, 70, "Goal", role=person("goal"), kind="human", thick="goal" in hl, size=16,
              sub="a person sets it", sub_size=13)
        f.box(220, 65, 180, 80, "Plan", role="ai", kind="ai", thick="plan" in hl, size=16,
              sub="the model proposes the next action", sub_size=13)
        f.arrow(172, 105, 218, 105)
        if gate == "hard":
            f.box(425, 45, 145, 120, "Approval gate", role=person("gate"), kind="decision", thick="gate" in hl,
                  size=14)
            f.arrow(402, 105, 423, 105)
            f.arrow(572, 105, 628, 105)
            f.text(600, 84, "yes", size=13, color=muted, italic=True)
        elif gate == "soft":
            f.box(425, 45, 145, 120, "Soft gate: an instruction (may be skipped)", role="risk", kind="decision",
                  thick="gate" in hl, size=13)
            f.arrow(402, 105, 423, 105)
            f.arrow(572, 105, 628, 105)
            f.text(600, 84, "?", size=13, color=muted, italic=True)
        else:
            f.arrow(402, 105, 628, 105, width=3.4, color=None, label="no gate", label_dy=-12, size=13)
        if gate is not None:
            f.arrow(490, 47, 330, 63, curve=26)
            f.text(410, 24, "no, or edited: a new plan", size=13, color=muted, italic=True)
        f.box(630, 65, 150, 80, "Tool call", role="neutral", kind="step", thick="tool" in hl, size=16,
              sub="the system runs it", sub_size=13)
        f.arrow(705, 147, 690, 248)
        f.box(600, 250, 180, 80, "Observation", role="neutral", kind="step", thick="observation" in hl, size=16,
              sub="the result enters the context window", sub_size=13)
        f.arrow(598, 290, 562, 290)
        f.box(390, 255, 170, 70, "Check point", role=person("check"), kind="human", thick="check" in hl,
              size=15, sub="a person inspects a result", sub_size=13)
        f.arrow(388, 290, 352, 290)
        f.box(200, 235, 150, 110, "Stop?", role="neutral", kind="decision", thick="stop" in hl, size=15)
        f.arrow(198, 290, 172, 290, label="yes", label_dy=-12, size=13)
        f.arrow(262, 237, 270, 148, label=None)
        f.text(242, 196, "no: next pass", size=13, color=muted, italic=True, anchor="end")
        f.box(20, 255, 150, 70, "Hand back", role=person("handback"), kind="human", thick="handback" in hl,
              size=15, sub="to a person", sub_size=13)
        f.box(20, 410, 760, 50, "Log: the system records every plan, tool call, observation, approval and stop, "
              "with times", role="soft", kind="step", thick="log" in hl, size=14)
        for part, txt in annotate.items():
            x, y, w = _ANN[part]
            f.text(x, y, txt, size=13, italic=True, weight="600", width=w, color=INK[f.mode])
        if note:
            f.text(400, 506, note, size=13, italic=True, color=muted, width=780)
        legend = "Hexagon = AI · rectangle = the system runs it · diamond = a decision · rounded = a person"
        if gate == "soft":
            legend += " · hatched = a soft gate (an instruction; may be skipped)"
        f.text(400, 530, legend, size=13, color=muted, width=780)
    return draw


LOOP_H = 548


# ---------------------------------------------------------------- F14.1 Chapter map
def chapter_map(f):
    muted = MUTED[f.mode]
    f.text(400, 30, "Chapter 14 at a glance", size=22, weight="700")
    cols = [("How agents work", ["14.1 What makes a system agentic", "14.2 The agent loop",
                                 "14.3 Why errors compound over steps"]),
            ("Where people belong", ["14.4 Reversibility and who bears an error", "14.5 Gates that hold",
                                     "14.6–14.7 Least privilege; logs"]),
            ("Practice", ["14.8 The dry run; 14.9 Lab 14.1 and A11", "Labs 14.2–14.3 (optional)",
                          "Case Study: the code freeze (Replit, 2025)"])]
    for c, (head, items) in enumerate(cols):
        x = 30 + c * 255
        f.text(x + 115, 74, head, size=16, weight="700")
        for i, it in enumerate(items):
            role = "neutral" if c < 2 else ("verified" if i == 0 else "soft")
            kind = "human" if c == 2 else "step"
            f.box(x, 94 + i * 88, 230, 70, it, role=role, kind=kind, size=14)
        if c < 2:
            f.arrow(x + 236, 217, x + 252, 217)
    y = 372
    f.text(150, y, "AI Work Loop:", size=14, weight="700", anchor="end")
    xs = [215, 335, 445, 555, 660]
    for i, step in enumerate(LOOP):
        if step == "Decide":
            f.box(xs[i] - 50, y - 20, 100, 40, step, role="highlight", kind="human", thick=True, size=15)
        elif step == "Verify":
            f.box(xs[i] - 50, y - 17, 100, 34, step, role="neutral", kind="human", dashed=True, size=14)
        else:
            f.text(xs[i], y, step, size=14, color=muted)
        if i < 4:
            f.text((xs[i] + xs[i + 1]) / 2, y, "→", size=14, color=muted)
    f.text(400, 410, "This chapter strengthens Decide (who decides before an action takes effect?), then Verify "
           "(dashed, second): a dry run before anyone relies on it.", size=13, color=muted, width=780)
    f.text(400, 436, "Opening case: an AI coding agent deletes a database during a code freeze (July 2025)",
           size=13, color=muted)


# ---------------------------------------------------------------- F14.2 Storyboard (C11)
def storyboard(f):
    muted = MUTED[f.mode]
    steps = [
        ("Early July", "App built with the agent; posts daily", True, "reported"),
        ("Jul 17", "Post: the day before was full of deceit; fake data alleged", True, "reported"),
        ("By Jul 18", "Freeze: told not to change anything without permission", True, "reported"),
        ("Jul 18", "Database deleted during the freeze", True, "reported"),
        ("Agent's text", "Says the rollback cannot restore the data", True, "reported"),
        ("Jul 19", "User: the rollback worked", True, "reported"),
        ("Jul 20", "CEO's post: dev/prod separation rolling out", False, "confirmed"),
    ]
    xs = [20, 132, 244, 356, 468, 580, 692]
    for i, (when, what, dashed, tier) in enumerate(steps):
        role = "risk" if when == "Jul 18" else ("verified" if tier == "confirmed" else "neutral")
        kind = "ai" if when == "Agent's text" else "step"
        f.text(xs[i] + 50, 70, when, size=13, weight="700")
        f.box(xs[i], 88, 100, 170, what, role=role, kind=kind, dashed=dashed, thick=(when == "Jul 18"), size=13,
              weight="600")
        if i < 6:
            f.arrow(xs[i] + 101, 173, xs[i + 1] - 1, 173)
    f.box(20, 290, 380, 70, "Dec 17, 2025, company blog: the agent gets only the development database "
          "(the post does not mention the incident)", role="verified", kind="step", size=13)
    f.box(420, 290, 360, 70, "What limited the harm: a restore point the agent said would not work",
          role="neutral", kind="step", dashed=True, size=13)
    f.text(400, 392, "Solid = the company's own record (read) · dashed = reported by the user or outlets", size=13,
           color=muted)
    f.text(400, 414, "Thick = the harm · hexagon = text the agent produced", size=13, color=muted)
    f.text(400, 442, "Sources: Masad (2025); Brewster & Chavez (2025); Sharwood (2025a, 2025b); Abdullahi (2025); "
           "AI Incident Database #1152", size=13, color=muted, width=780)


# ---------------------------------------------------------------- F14.3 Four kinds of system (one axis)
def four_kinds(f):
    muted = MUTED[f.mode]
    f.arrow(40, 70, 770, 70, width=2.2)
    f.text(400, 44, "Who fixes the next step?", size=15, weight="700")
    kinds = [("Chat assistant", "you, each turn", "you run each step", "human"),
             ("Prompt chain", "you, in advance", "you run each step", "human"),
             ("Automated workflow", "people, in advance", "software runs each step", "step"),
             ("Agent", "the model, as it goes", "software runs each step", "ai")]
    for i, (k, who, run, kind) in enumerate(kinds):
        x = 30 + i * 190
        f.box(x, 100, 172, 120, k, role="ai" if kind == "ai" else "neutral", kind=kind, size=15,
              sub=who, sub_size=13)
        f.text(x + 86, 244, run, size=13, color=muted, width=170)
    f.box(30, 280, 740, 64, "A separate question: what can it change? Read, write, send, pay (permissions, 14.6). "
          "An approval gate limits that; it does not change the kind of system.", role="soft", kind="step",
          size=13)
    f.text(400, 370, "Agency (a way of working: AI acts for you later) is not a kind of system; any kind above can "
           "be used that way (Chapter 5).", size=13, color=muted, width=780)


# ---------------------------------------------------------------- F14.5 Sam's trace on the loop
SAM_TRACE = agent_loop(
    highlight=["gate"],
    annotate={"plan": "passes 1–7: search, four datasheets, cart, draft", "gate": "pass 8: 'place order, $312' → "
              "treasurer + second officer", "observation": "pass 6: cart total $312",
              "stop": "stop points: over budget line; part not on the list; > 15 passes"},
    note="Sam's current design (constructed). The gate is there because of the test that went wrong in section 14.5.")

# ---------------------------------------------------------------- F14.7 Where a person belongs (2 x 2)
def where_people(f):
    muted = MUTED[f.mode]
    f.text(470, 40, "Who would bear an error?", size=15, weight="700")
    f.text(345, 70, "Only you", size=14, weight="700")
    f.text(615, 70, "Other people", size=14, weight="700")
    f.text(100, 150, "Can be undone", size=14, weight="700", width=150)
    f.text(100, 290, "Cannot easily be undone", size=14, weight="700", width=150)
    f.box(210, 90, 260, 120, "Review the log afterward", role="soft", kind="step", size=15,
          sub="a draft, a cart, a test copy", sub_size=13)
    f.box(480, 90, 260, 120, "Check point before others see it", role="neutral", kind="human", size=15,
          sub="a shared draft, a calendar hold", sub_size=13)
    f.box(210, 230, 260, 120, "Approval gate, or keep the step", role="neutral", kind="human", size=15,
          sub="deleting your own files", sub_size=13)
    f.box(480, 230, 260, 120, "Approval gate before it takes effect", role="highlight", kind="human", thick=True,
          size=15, sub="send, publish, pay, delete shared data", sub_size=13)
    f.text(400, 382, "Read-only actions change nothing: log them. Stop points (limits, errors, surprises) apply in "
           "every cell.", size=13, color=muted, width=760)
    f.text(400, 408, "Rounded = a person acts · thick = the strongest point · the cells are this book's "
           "arrangement, not a rule", size=13, color=muted, width=760)


# ---------------------------------------------------------------- F14.9 Three people points on the loop
PEOPLE_POINTS = agent_loop(
    highlight=["gate", "check", "stop"],
    annotate={"gate": "approve before an action takes effect", "check": "inspect a result before later "
              "steps build on it", "stop": "halt and hand back when a condition is met"},
    note="Three people points: approval gate, check point, stop point.")


# ---------------------------------------------------------------- F14.10 Soft vs. hard gate
def soft_hard(f):
    muted = MUTED[f.mode]
    f.text(200, 34, "Soft gate", size=16, weight="700")
    f.text(600, 34, "Hard gate", size=16, weight="700")
    f.line(400, 50, 400, 380, color=muted)
    f.box(40, 60, 320, 60, "Instruction: \"always ask before ordering\"", role="neutral", kind="step", size=14)
    f.arrow(200, 122, 200, 146)
    f.box(40, 148, 320, 60, "It becomes text in the context window", role="soft", kind="step", size=14)
    f.arrow(200, 210, 200, 234)
    f.box(60, 236, 280, 70, "The model produces the next action", role="ai", kind="ai", size=14)
    f.arrow(200, 308, 200, 332)
    f.box(60, 334, 280, 50, "Action may run without asking", role="risk", kind="step", thick=True,
          size=14)
    f.box(440, 60, 320, 60, "The model proposes an action", role="ai", kind="ai", size=14)
    f.arrow(600, 122, 600, 146)
    f.box(440, 148, 320, 60, "The system pauses: the tool cannot run yet", role="neutral", kind="step", size=14)
    f.arrow(600, 210, 600, 234)
    f.box(470, 236, 260, 90, "A named person approves, edits or rejects", role="highlight", kind="human",
          thick=True, size=14)
    f.arrow(600, 328, 600, 344)
    f.box(470, 346, 260, 40, "Only then does the action run", role="verified", kind="step", size=14)
    f.text(400, 414, "Examples of soft gates in this chapter: a declared code freeze (Opening Case); an agent's "
           "own confirmation step that did not fire (Operator).", size=13, color=muted, width=780)


# ---------------------------------------------------------------- F14.12 Permissions (Marcus)
def permissions(f):
    muted = MUTED[f.mode]
    f.text(400, 30, "Marcus's rehearsal assistant (constructed): what each part may do", size=15, weight="700")
    rows = [("Band calendar", "read: yes · write: no · send: no · pay: no"),
            ("Drafts folder", "read: yes · write: drafts only · send: no · pay: no"),
            ("Band mailing list", "send: reminders only, after his weekly approval · pay: no")]
    for i, (tool, perm) in enumerate(rows):
        y = 60 + i * 86
        f.box(30, y, 230, 70, tool, role="neutral", kind="step", size=15)
        f.text(520, y + 35, perm, size=14, width=470, anchor="middle")
    f.box(30, 322, 740, 64, "Never touches: his email account, anything from his nursing placement, any payment "
          "or room booking", role="risk", kind="step", thick=True, size=14)
    f.text(400, 412, "Least privilege: each part gets only the access its step needs. Thick = a line the assistant "
           "never crosses.", size=13, color=muted, width=780)


# ---------------------------------------------------------------- F14.13 Log vs. the agent's report
def log_vs_report(f):
    muted = MUTED[f.mode]
    f.text(200, 34, "The log (written by the system)", size=15, weight="700")
    f.text(600, 34, "The agent's report (produced by the model)", size=15, weight="700")
    items = ["Time of each pass", "Plan text and tool call", "Observation returned", "Who approved, and when"]
    for i, it in enumerate(items):
        f.box(40, 56 + i * 70, 320, 56, it, role="neutral", kind="step", size=14)
    f.box(440, 56, 320, 266, "More text, predicted from the context window: it can be fluent and wrong. In the "
          "Opening Case, the agent's message said the rollback would not work; the user later said it did.",
          role="ai", kind="ai", size=14)
    f.text(400, 352, "Read the log to learn what happened; treat the agent's summary as a claim to check (Chapter 8).",
           size=13, color=muted, width=780)
    f.text(400, 378, "A log shows what was done, not why the model produced it (Chapter 17).", size=13,
           color=muted, width=780)


# ---------------------------------------------------------------- F14.14 Lucia's review step
def lucia_review(f):
    muted = MUTED[f.mode]
    f.box(20, 150, 130, 80, "AI draft of a reply", role="ai", kind="ai", size=14)
    f.arrow(152, 190, 178, 190)
    f.box(180, 120, 160, 140, "Refund, discount or account change?", role="neutral", kind="decision", size=13)
    f.arrow(260, 120, 260, 70, label=None)
    f.text(272, 96, "yes", size=13, color=muted, italic=True, anchor="start")
    f.box(190, 14, 230, 56, "Approval queue: a support team member approves", role="highlight", kind="human", thick=True,
          size=14)
    f.arrow(342, 190, 388, 190, label="no", label_dy=-12, size=13)
    f.box(390, 155, 160, 70, "Sent and logged", role="neutral", kind="step", size=14)
    f.arrow(552, 190, 578, 190)
    f.box(580, 150, 190, 80, "Weekly sample of 20 sent replies", role="neutral", kind="human", size=14)
    f.arrow(675, 232, 675, 262)
    f.box(590, 264, 170, 110, "Policy error found?", role="neutral", kind="decision", size=13)
    f.arrow(588, 319, 452, 319, label="yes", label_dy=-12, size=13)
    f.box(220, 290, 230, 60, "Pause automatic sending for that category", role="risk", kind="step", thick=True,
          size=14)
    f.text(400, 404, "Lucia's proposal (constructed; no customer data). Thick = a stop point and an approval gate.",
           size=13, color=muted, width=780)


# ---------------------------------------------------------------- F14.15 The dry run
def dry_run(f):
    muted = MUTED[f.mode]
    f.box(20, 40, 200, 70, "Test inputs: typical, edge", role="neutral", kind="step", size=14)
    f.box(20, 130, 200, 70, "One planted fault", role="risk", kind="step", size=14,
          sub="wrong result · missing data · hidden instruction", sub_size=13)
    f.arrow(222, 75, 258, 115)
    f.arrow(222, 165, 258, 130)
    f.box(260, 85, 200, 80, "Side effects off", role="neutral", kind="step", size=14,
          sub="run on paper or in a test copy", sub_size=13)
    f.arrow(462, 125, 488, 125)
    f.box(490, 85, 170, 80, "Record each step", role="neutral", kind="human", size=14,
          sub="right? checked how?", sub_size=13)
    f.arrow(575, 167, 575, 193)
    f.box(500, 195, 150, 110, "Fault caught?", role="neutral", kind="decision", size=14)
    f.arrow(652, 250, 688, 250, label="yes", label_dy=-12, size=13)
    f.box(690, 215, 90, 70, "Keep the design", role="verified", kind="step", size=13)
    f.arrow(575, 307, 575, 333)
    f.text(588, 320, "no", size=13, color=muted, italic=True, anchor="start")
    f.box(250, 335, 530, 60, "Move or add a point · narrow a permission · or use a simpler system (14.1)",
          role="neutral", kind="human", thick=True, size=14)
    f.text(400, 420, "Then rerun the run that failed. One run is a sample, not a reliability estimate (14.3).",
           size=13, color=muted, width=780)


# ---------------------------------------------------------------- F14.16 A11 sheet
def a11_sheet(f):
    muted = MUTED[f.mode]
    f.text(400, 26, "A11 workflow blueprint (one record)", size=17, weight="700")
    rows = [("1 Task, goal and done-criteria", "neutral"),
            ("2 System type and why", "soft"),
            ("3 Step map: 5–10 steps, who or what runs each", "neutral"),
            ("4 Action table: undo? who bears it? people point; permissions; log plan", "neutral"),
            ("5 Dry run: typical, edge, planted fault; per-step record and checks", "neutral"),
            ("6 Revision and rerun", "verified"),
            ("7 Defense for a non-specialist (100–120 words)", "soft"),
            ("8 AI Use Declaration", "soft")]
    for i, (r, role) in enumerate(rows):
        y = 46 + i * 52
        f.box(40, y, 720, 42, r, role=role, kind="step", size=14)
    f.text(400, 476, "Item 3 can be the photographed cards; item 5's typical and planted-fault runs can be the "
           "photographed lab sheet.", size=13, color=muted, width=780)


# ---------------------------------------------------------------- F14.17 / F14.18 C11 labels
C11_TREE = failure_tree(highlight={"context loss", "hallucination", "overconfidence"},
                        dashed={"context loss", "hallucination", "overconfidence"},
                        tag="C11 Replit (2025) · context loss (freeze not followed), inferred",
                        note="Second: hallucination (alleged fake data); overconfidence (certain 'rollback impossible'); inferred")
C11_CHAIN = failure_chain(
    notes={0: "Destructive database command (reported)", 1: "No enforced gate (CEO's post)",
           2: "The system ran it", 3: "Data deleted; restored, per the user"},
    highlight={1}, dashed={0, 3},
    tag="Documented by the company's chief executive: the agent could reach production data")


# ---------------------------------------------------------------- F14.19 A gate that leans toward the draft
def gate_leans(f):
    muted = MUTED[f.mode]
    f.box(30, 90, 200, 100, "Draft reply produced by the model", role="ai", kind="ai", size=14)
    f.arrow(232, 140, 278, 140)
    f.box(280, 80, 240, 120, "A doctor edits every draft", role="neutral", kind="human", dashed=True, size=14,
          sub="edited replies resembled the drafts", sub_size=13)
    f.arrow(522, 140, 568, 140)
    f.box(570, 100, 200, 80, "Reply that would be sent", role="neutral", kind="step", size=14)
    f.text(400, 236, "The gate existed; the authors suggest anchoring and automation bias (dashed = inferred: the "
           "authors' suggestion).", size=13, color=muted, width=760)
    f.text(400, 262, "Chen et al. (2024): six radiation oncologists, simulated messages, GPT-4 drafts, 2023.",
           size=13, color=muted, width=760)


# ---------------------------------------------------------------- F14.20 Summary card
def summary_card(f):
    f.text(400, 26, "Chapter 14 — what you can do now", size=18, weight="700")
    cards = ["Place a system: who fixes the next step, who runs it",
             "Trace a run: plan, tool call, observation, stop",
             "Expect errors to compound; test whole runs",
             "Classify actions; place gates, checks and stops",
             "Prefer hard gates; keep approvals few and real",
             "Give least privilege; keep a log; dry-run with a fault"]
    for i, c in enumerate(cards):
        x = 20 + (i % 3) * 258
        y = 50 + (i // 3) * 150
        f.box(x, y, 242, 130, c, role="neutral" if i % 2 else "soft", kind="human", size=14, weight="600")


LADDER_GATE = delegation_ladder(
    highlight="agency", annotate={"agency": "an approval gate: a person sees each consequential action first"},
    note="The gate restores a check at the agency rung; the rung does not change (Chapter 5).")


# ---------------------------------------------------------------- F14.21 Feng et al. (2025): five user roles
def five_roles(f):
    muted = MUTED[f.mode]
    roles = [("1 Operator", "you direct; the agent helps when asked"),
             ("2 Collaborator", "you and the agent plan and act together"),
             ("3 Consultant", "the agent leads and asks you for direction"),
             ("4 Approver", "the agent acts; you sign off on consequential actions"),
             ("5 Observer", "the agent acts; you watch the log and can switch it off")]
    for i, (r, d) in enumerate(roles):
        y = 40 + i * 70
        f.box(60 + i * 30, y, 560 - i * 30, 58, r, role="highlight" if i == 3 else "neutral", kind="human",
              thick=(i == 3), size=15, sub=d, sub_size=13)
    f.arrow(710, 50, 710, 380, width=2.2)
    f.text(754, 215, "more\nautonomy", size=13, color=muted, italic=True)
    f.text(400, 410, "Paraphrased from Feng, McDonald & Zhang (2025). Thick = the level an approval gate holds a "
           "step at.", size=13, color=muted, width=780)


FIGS = [
    ("f14-01-chapter-map", chapter_map, 800, 455, "Chapter 14 at a glance"),
    ("f14-02-storyboard", storyboard, 800, 470,
     "The freeze was an instruction; the deletion went through, and a restore point limited the damage"),
    ("f14-03-four-kinds", four_kinds, 800, 390,
     "Who fixes the next step, and who runs it, separate four kinds of system"),
    ("f14-04-agent-loop", agent_loop(), 800, LOOP_H,
     "An agent repeats plan, tool call and observation until it stops; the approval gate sits before an action "
     "takes effect"),
    ("f14-05-sam-trace", SAM_TRACE, 800, LOOP_H,
     "Sam's agent runs eight passes; the gate stops the eighth before it spends club money"),
    ("f14-07-where-people", where_people, 800, 425,
     "Whether an action can be undone, and who bears an error, decide where a person belongs"),
    ("f14-09-people-points", PEOPLE_POINTS, 800, LOOP_H,
     "Three people points: approve before, check between, stop when"),
    ("f14-10-soft-hard", soft_hard, 800, 430,
     "An instruction is text the model receives; a hard gate is a step the system cannot skip"),
    ("f14-11-ladder-gate", LADDER_GATE, 800, 590,
     "An approval gate restores a check at the agency rung without changing the rung"),
    ("f14-12-permissions", permissions, 800, 425, "Each part of the workflow gets only the access its step needs"),
    ("f14-13-log-report", log_vs_report, 800, 395,
     "A log records what the system did; the agent's summary is more text from the model"),
    ("f14-14-lucia-review", lucia_review, 800, 420,
     "Lucia's review step sends risky replies to a person and samples the rest"),
    ("f14-15-dry-run", dry_run, 800, 435,
     "A dry run with a planted fault shows which point catches an error before anyone relies on the workflow"),
    ("f14-16-a11-sheet", a11_sheet, 800, 490, "Your blueprint records every step, action, point, permission and test"),
    ("f14-17-tree-c11", C11_TREE, 800, tree_height() + 34,
     "C11 on the tree: context loss, with hallucination and overconfidence second, all inferred"),
    ("f14-18-chain-c11", C11_CHAIN, 800, 420, "No enforced gate stood between the agent's command and the database"),
    ("f14-19-gate-leans", gate_leans, 800, 280, "A gate that exists can still lean toward the draft"),
    ("f14-20-summary-card", summary_card, 800, 340, "Chapter 14 summary card"),
    ("f14-21-five-roles", five_roles, 800, 425,
     "Autonomy is a design choice: five roles for the user, from operator to observer"),
]

if __name__ == "__main__":
    only = set(sys.argv[1:])
    for fid, fn, w, h, title in FIGS:
        if only and fid not in only:
            continue
        render(fid, fn, w, h, title, ROOT)
        print("rendered", fid)
