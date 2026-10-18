"""Chapter 1 diagrams (SVG, color + gray). Run from the repo root:
    python3 figures/scripts/ch01_figures.py
Data charts (F1.5, F1.6) are in ch01_charts.py.
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from figlib import render, MUTED, INK, ROLES  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LOOP = ["Frame", "Prompt", "Verify", "Decide", "Disclose"]
LOOP_SUB = ["What is the task? Should AI be in it?", "Give task, context, limits, format",
            "Check against something other than the tool", "Keep, change or reject; own the result",
            "Say what you used and how"]


# ---------------------------------------------------------------- F1.2 AI Work Loop (signature 1)
def work_loop(highlight=None):
    def draw(f):
        cx, cy, r = 400, 300, 200
        bw, bh = 210, 86
        pos = []
        for i in range(5):
            a = -math.pi / 2 + i * 2 * math.pi / 5
            pos.append((cx + r * math.cos(a), cy + r * math.sin(a)))
        for i in range(5):
            x1, y1 = pos[i]
            x2, y2 = pos[(i + 1) % 5]
            dx, dy = x2 - x1, y2 - y1
            d = math.hypot(dx, dy)
            sx, sy = x1 + dx * 0.30, y1 + dy * 0.30
            ex, ey = x1 + dx * 0.70, y1 + dy * 0.70
            f.arrow(sx, sy, ex, ey, curve=-18)
        for i, (x, y) in enumerate(pos):
            hl = highlight == LOOP[i]
            role = "highlight" if hl else "neutral"
            f.box(x - bw / 2, y - bh / 2, bw, bh, f"{i + 1}. {LOOP[i]}", role=role, kind="human",
                  thick=hl, size=17, sub=LOOP_SUB[i], sub_size=12)
        f.box(cx - 95, cy - 34, 190, 68, "The AI tool", role="ai", kind="ai", size=15,
              sub="produces drafts; you make every decision", sub_size=11)
        f.text(400, 585, "Rounded boxes = human decisions · hexagon = AI component", size=12,
               color=MUTED[f.mode])
    return draw


# ---------------------------------------------------------------- F1.1 Chapter map
def chapter_map(f):
    f.text(400, 32, "Chapter 1 at a glance", size=22, weight="700")
    cols = [("Learn", ["1.1 Same question, different answers", "1.2 What the evidence says",
                       "1.3 The jagged frontier"]),
            ("Judge", ["1.4 Fluent is not the same as correct", "1.5 Your judgment, your responsibility",
                       "1.6 The AI Work Loop"]),
            ("Do", ["Labs 1.1–1.3", "1.7 Your baseline", "A1: AI use baseline and goals (due Jan 25)"])]
    for c, (head, items) in enumerate(cols):
        x = 30 + c * 255
        f.text(x + 115, 78, head, size=16, weight="700")
        for i, it in enumerate(items):
            role = "neutral" if c < 2 else ("verified" if i == 2 else "soft")
            kind = "human" if c == 2 else "step"
            f.box(x, 100 + i * 92, 230, 74, it, role=role, kind=kind, size=14)
        if c < 2:
            f.arrow(x + 236, 237, x + 252, 237)
    f.text(400, 395, "Opening case: 5,172 support agents and an AI assistant (Brynjolfsson et al., 2025)",
           size=13, color=MUTED[f.mode])


# ---------------------------------------------------------------- F1.3 two answers (typeset text)
def two_answers(f):
    a = ("Practice problems by hand instead of just rereading notes. Chemistry is mostly applied skill, "
         "so work through stoichiometry, equilibrium, and gas law problems without looking at the solutions "
         "first. Then check your answers and redo the ones you missed.\n"
         "Make a one-page sheet of key equations, units, and constants, and review it often. Also explain "
         "each reaction type or periodic trend in your own words. Where you can't, you've found a gap to study.\n"
         "Do past exams or old quizzes under timed conditions, showing every step and unit. This builds speed "
         "and gets you used to exam pressure. Afterward, label each mistake as a concept error or a calculation "
         "slip, since they need different fixes.")
    b = ("1. Practice with problems, not just rereading. Work through past exams, textbook problems, and "
         "problem sets without looking at the solution first, then check where you went wrong. Chemistry is a "
         "skill, so stoichiometry, equilibrium, and mechanisms only stick when you do them yourself.\n"
         "2. Use active recall and spaced repetition. Make flashcards for reactions, definitions, periodic "
         "trends, and formulas. Quiz yourself from memory, and review a little each day instead of cramming "
         "the night before.\n"
         "3. Understand the concepts behind the formulas. Be able to explain why something happens, such as "
         "why bond polarity affects solubility. Study with a friend and teach topics to each other. If you can "
         "explain it simply, you know it. Also write out a one-page summary of key equations and concepts "
         "from memory.")
    f.text(400, 28, 'Prompt: "What are three good study strategies for a chemistry exam?"', size=15, weight="700")
    for i, (label, txt) in enumerate([("Answer A · Claude Haiku 5.5 · Oct 17, 2026", a),
                                      ("Answer B · Claude Sonnet 5.5 · Oct 17, 2026", b)]):
        x = 20 + i * 390
        f.box(x, 50, 370, 34, label, role="ai", kind="step", size=13)
        f.raw(f'<rect x="{x}" y="84" width="370" height="345" fill="#FFFFFF" stroke="{INK[f.mode]}" stroke-width="1.2"/>')
        y = 104
        for para in txt.split("\n"):
            from figlib import wrap
            lines = wrap(para, 340, 13)
            for ln in lines:
                f.text(x + 14, y, ln, size=13, anchor="start", weight="normal")
                y += 16.5
            y += 8
    f.text(400, 448, "Same prompt, two models, same day: overlapping advice, different emphasis and form. "
           "Neither states how sure it is.", size=12, color=MUTED[f.mode], italic=True)


# ---------------------------------------------------------------- F1.4 three lanes
def three_lanes(f):
    lanes = [("Search engine", [("Your query", "neutral", "human", False),
                                ("Finds existing documents and ranks links", "neutral", "step", False),
                                ("You choose and read a source", "neutral", "human", False)]),
             ("Generative model", [("Your prompt", "neutral", "human", False),
                                   ("Model writes new text, piece by piece", "ai", "ai", True),
                                   ("You must verify every claim", "risk", "human", False)]),
             ("Search-then-generate tool", [("Your prompt", "neutral", "human", False),
                                            ("Searches, then writes new text with links", "ai", "ai", True),
                                            ("Check each claim against its cited page", "risk", "human", False)])]
    for r, (name, boxes) in enumerate(lanes):
        y = 30 + r * 150
        f.text(20, y + 52, name, size=15, weight="700", anchor="start", width=None)
        for c, (lab, role, kind, dashed) in enumerate(boxes):
            x = 210 + c * 200
            f.box(x, y + 10, 170, 84, lab, role=role, kind=kind, dashed=dashed, size=13)
            if c < 2:
                f.arrow(x + 172, y + 52, x + 198, y + 52)
    f.text(400, 488, "Dashed outline = output may be wrong · hexagon = AI component · rounded = you",
           size=12, color=MUTED[f.mode])


# ---------------------------------------------------------------- F1.7 Jagged frontier map (signature 2)
def jagged(f):
    x0, x1, y0, y1 = 70, 520, 60, 400
    ink = INK[f.mode]
    f.line(x0, y1, x1, y1, color=ink)
    f.line(x0, y0, x0, y1, color=ink)
    f.text((x0 + x1) / 2, y1 + 28, "Tasks, ordered by how hard they look to a person →", size=13)
    f.raw(f'<text x="28" y="{(y0 + y1) / 2}" font-size="13" text-anchor="middle" fill="{ink}" '
          f'transform="rotate(-90 28 {(y0 + y1) / 2})">How hard the task is for the AI tool →</text>')
    pts = [(x0, 300), (115, 270), (150, 330), (195, 220), (235, 280), (280, 190), (320, 300),
           (365, 170), (405, 235), (445, 130), (485, 210), (x1, 120)]
    fill = "#E7F3EC" if f.mode == "color" else "#E6E6E6"
    poly = " ".join(f"{x},{y}" for x, y in pts) + f" {x1},{y1} {x0},{y1}"
    f.raw(f'<polygon points="{poly}" fill="{fill}" stroke="none"/>')
    f.raw(f'<polyline points="{" ".join(f"{x},{y}" for x, y in pts)}" fill="none" stroke="{ink}" '
          f'stroke-width="2.6"/>')
    f.text(300, 375, "Inside the frontier", size=14, weight="700")
    f.text(200, 90, "Outside the frontier", size=14, weight="700")
    tasks = [(100, 345, True, "Rewrite a paragraph in another tone"),
             (150, 245, False, "Exact quotes with page numbers from a book it was not given"),
             (260, 330, True, "Summarize an article you paste in"),
             (300, 150, False, "Exact letter counts in a long text, with no code or calculator feature"),
             (420, 300, True, "Generate many ideas quickly"),
             (470, 105, False, "Facts about a small local organization, without web search")]
    for k, (x, y, inside, _) in enumerate(tasks, 1):
        if inside:
            f.raw(f'<circle cx="{x}" cy="{y}" r="12" fill="{ink}"/>')
            f.text(x, y, str(k), size=13, weight="700", color="#FFFFFF")
        else:
            f.raw(f'<circle cx="{x}" cy="{y}" r="12" fill="#FFFFFF" stroke="{ink}" stroke-width="2.4"/>')
            f.text(x, y, str(k), size=13, weight="700")
    f.text(660, 70, "Example tasks", size=14, weight="700")
    yy = 100
    for k, (_, _, inside, lab) in enumerate(tasks, 1):
        mark = "●" if inside else "○"
        f.text(548, yy, f"{mark} {k}", size=14, weight="700", anchor="start")
        f.text(585, yy, lab, size=13, anchor="start", width=200, line_h=1.15)
        yy += 52
    f.text(400, 470, "● usually inside  ·  ○ usually outside  ·  Illustrative, as of October 2026; "
           "test your own tasks.", size=13, color=MUTED[f.mode], width=760)


# ---------------------------------------------------------------- F1.8 storyboard
def storyboard(f):
    steps = [("Before", "Agents answer customer chats on their own", "neutral", "human"),
             ("Rollout", "The AI assistant reaches agents a few at a time over several months", "ai", "ai"),
             ("Comparison", "Researchers compare agents with and without it, same weeks", "neutral", "step"),
             ("Result", "+15% issues/hour on average; about +30% for newer agents; small quality dip for the most experienced",
              "verified", "step")]
    for i, (h, t, role, kind) in enumerate(steps):
        x = 15 + i * 197
        f.text(x + 87, 30, f"{i + 1}. {h}", size=15, weight="700")
        f.box(x, 50, 175, 150, t, role=role, kind=kind, size=13, weight="normal")
        if i < 3:
            f.arrow(x + 177, 125, x + 195, 125)
    f.text(400, 232, "Source: Brynjolfsson, Li & Raymond (2025), 5,172 agents", size=12, color=MUTED[f.mode])


# ---------------------------------------------------------------- F1.9 2x2
def two_by_two(f):
    x0, y0, w, h = 150, 70, 300, 170
    cells = [("Fluent and correct", "Useful, still verify", "verified", False),
             ("Fluent and wrong", "Dangerous: nothing on the surface warns you", "risk", True),
             ("Halting and correct", "Useful, needs editing", "neutral", False),
             ("Halting and wrong", "Easy to spot and reject", "soft", False)]
    for i, (t, s, role, thick) in enumerate(cells):
        cx = x0 + (i % 2) * w
        cy = y0 + (i // 2) * h
        f.box(cx, cy, w - 10, h - 10, t, role=role, kind="step", thick=thick, size=16, sub=s, sub_size=13)
    f.text(x0 + w / 2 - 5, 50, "Correct", size=14, weight="700")
    f.text(x0 + w * 1.5 - 5, 50, "Wrong", size=14, weight="700")
    f.text(85, y0 + h / 2 - 5, "Sounds\nfluent", size=14, weight="700")
    f.text(85, y0 + h * 1.5 - 5, "Sounds\nhalting", size=14, weight="700")
    f.text(400, 420, "Thick border and hatching mark the risk corner.", size=12, color=MUTED[f.mode])


# ---------------------------------------------------------------- F1.11 three zones
def three_zones(f):
    zones = [("Permitted", "Brainstorming · explanations · study help · feedback on your own draft", "verified", False),
             ("Permitted with disclosure and verification",
              "Drafting · coding support · source synthesis · case and data work", "neutral", True),
             ("Not acceptable", "Undisclosed outsourcing · fabricated sources · unsupported claims · work you do not "
              "understand · AI use in exams · personal or confidential data in public tools", "risk", False)]
    for i, (t, s, role, dashed) in enumerate(zones):
        x = 20 + i * 262
        f.box(x, 40, 240, 210, t, role=role, kind="step", dashed=dashed, size=15, sub=s, sub_size=13)
    f.arrow(282, 285, 282, 252, label=None)
    f.text(282, 305, "Disclose + verify + can explain", size=13, weight="600")
    f.text(544, 285, "Stays off-limits even if disclosed", size=13, weight="600", color=INK[f.mode])
    f.text(400, 345, "Dashed border = acceptable only under conditions", size=12, color=MUTED[f.mode])


# ---------------------------------------------------------------- F1.12 loop walkthrough
def walkthrough(f):
    items = [("Frame", "Goal: solve and keep the customer. Refund decision stays human.", "neutral"),
             ("Prompt", "Draft a polite reply; replacement by express; refund if preferred; under 120 words.", "neutral"),
             ("Verify", "Caught: an invented 20% discount the policy does not allow.", "risk"),
             ("Decide", "Delete the discount, add the order number, send under your name.", "neutral"),
             ("Disclose", "Company rule: reviewed AI drafts need no extra note.", "neutral")]
    for i, (h, t, role) in enumerate(items):
        x = 10 + i * 158
        f.box(x, 40, 146, 56, h, role="highlight" if role == "risk" else "neutral", kind="human",
              thick=role == "risk", size=16)
        f.box(x, 108, 146, 150, t, role=role, kind="step", size=12.5, weight="normal")
        if i < 4:
            f.arrow(x + 147, 68, x + 157, 68)
    f.text(400, 290, "The Verify step catches what the tool invented.", size=12, color=MUTED[f.mode])


# ---------------------------------------------------------------- F1.13 faster vs learning
def faster_vs_learning(f):
    f.box(300, 20, 200, 60, "A course assignment", role="neutral", kind="step", size=15)
    paths = [(60, "The tool produces the answer; you hand it in", "Output delivered", "Skill not built", "risk"),
             (460, "You reason it through; the tool assists", "Output delivered", "Skill built", "verified")]
    for x, a, b, c, role in paths:
        f.box(x, 130, 280, 60, a, role="ai", kind="ai", size=14)
        f.box(x, 225, 280, 56, b, role="neutral", kind="step", size=14)
        f.box(x, 315, 280, 60, c, role=role, kind="human", thick=True, size=15)
        f.arrow(x + 140, 192, x + 140, 223)
        f.arrow(x + 140, 283, x + 140, 313)
    f.arrow(360, 82, 220, 128)
    f.arrow(440, 82, 580, 128)
    f.text(400, 410, "Same output, different result for you. At work the output may be the goal; "
           "in a course, the skill is.", size=12.5, color=MUTED[f.mode], width=740)


# ---------------------------------------------------------------- F1.14 baseline template
def baseline_template(f):
    f.text(400, 26, "A1 — My AI use baseline", size=18, weight="700")
    for i in range(3):
        f.box(20 + i * 258, 50, 242, 140, f"Task {i + 1}",
              role="neutral", kind="step", size=15, sub="What I asked · what came back · what I did", sub_size=12)
    f.box(20, 210, 370, 110, "One documented failure", role="risk", kind="step", size=15,
          sub="The output · why it was wrong · the test that showed it", sub_size=12)
    f.box(410, 210, 370, 110, "Two goals (each tied to an LO)", role="verified", kind="human", size=15,
          sub="Specific · observable · dated", sub_size=12)
    f.box(20, 340, 760, 70, "AI Use Declaration", role="soft", kind="step", dashed=True, size=15,
          sub="Tools · purpose · accepted / rejected / revised · how verified · where my judgment mattered",
          sub_size=12)


# ---------------------------------------------------------------- F1.15 summary card
def summary_card(f):
    f.text(400, 26, "Chapter 1 — what you can do now", size=18, weight="700")
    cards = ["Explain: generation writes likely text, even when it cites sources",
             "Explain: gains from AI at work are real but uneven",
             "Judge: test a task; the frontier is jagged and moves",
             "Judge: fluent is not the same as correct",
             "Judge: assistance vs. outsourcing (three zones)",
             "Apply: Frame → Prompt → Verify → Decide → Disclose"]
    for i, c in enumerate(cards):
        x = 20 + (i % 3) * 258
        y = 50 + (i // 3) * 150
        f.box(x, y, 242, 130, c, role="neutral" if i % 2 else "soft", kind="human", size=14, weight="600")


# ---------------------------------------------------------------- F1.16 staggered rollout
def rollout(f):
    months = 8
    x0, y0, cw, rh = 150, 50, 75, 70
    waves = [("Wave 1 agents", 2), ("Wave 2 agents", 4), ("Wave 3 agents", 6)]
    for m in range(months):
        f.text(x0 + m * cw + cw / 2, 35, f"Month {m + 1}", size=12)
    for r, (name, start) in enumerate(waves):
        y = y0 + r * (rh + 12)
        f.text(140, y + rh / 2, name, size=13, weight="600", anchor="end")
        for m in range(months):
            on = m >= start
            role = "ai" if on else "neutral"
            f.box(x0 + m * cw + 3, y, cw - 6, rh, "AI" if on else "", role=role, kind="step", size=12)
    f.text(400, 330, "Schematic. In month 5, wave 2 has just received the assistant while wave 3 has not: comparing "
           "their changes in the same weeks helps separate the tool's effect, if the groups were on similar paths before.", size=12.5,
           width=740, color=MUTED[f.mode])


FIGS = [
    ("f1-01-chapter-map", chapter_map, 800, 410, "Chapter 1 at a glance"),
    ("f1-02-ai-work-loop", work_loop(), 800, 600, "Every AI-assisted task passes through five human decisions"),
    ("f1-02-ai-work-loop-frame", work_loop("Frame"), 800, 600,
     "Every AI-assisted task passes through five human decisions (Frame highlighted)"),
    ("f1-03-two-answers", two_answers, 800, 465, "The same question can produce different answers that sound equally sure"),
    ("f1-04-three-lanes", three_lanes, 800, 500, "Search points to sources; generation writes new text, even when it cites sources"),
    ("f1-07-jagged-frontier", jagged, 800, 500, "AI capability is uneven across tasks that look equally hard"),
    ("f1-08-storyboard", storyboard, 800, 245, "What happened when the assistant arrived"),
    ("f1-09-fluent-correct", two_by_two, 800, 440, "Sounding right and being right are two different things"),
    ("f1-11-three-zones", three_zones, 800, 360,
     "Disclosure and verification make middle-zone uses acceptable; some uses stay off-limits"),
    ("f1-12-loop-walkthrough", walkthrough, 800, 305, "The AI Work Loop applied to an upset customer's email"),
    ("f1-13-faster-vs-learning", faster_vs_learning, 800, 430, "Working faster with AI is not the same as learning"),
    ("f1-14-baseline-template", baseline_template, 800, 420, "Your baseline: three tasks, one failure, two goals"),
    ("f1-15-summary-card", summary_card, 800, 340, "Chapter 1 summary card"),
    ("f1-16-staggered-rollout", rollout, 800, 350, "A staggered rollout turns a workplace into an experiment"),
]

if __name__ == "__main__":
    for fid, fn, w, h, title in FIGS:
        render(fid, fn, w, h, title, ROOT)
        print("rendered", fid)
