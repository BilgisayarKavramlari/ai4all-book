"""Chapter 2 diagrams (SVG, color + gray). Run from the repo root:
    python3 figures/scripts/ch02_figures.py
Data charts (F2.9, F2.10, F2.14) are in ch02_charts.py.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from figlib import render, MUTED, INK  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LOOP = ["Frame", "Prompt", "Verify", "Decide", "Disclose"]


# ---------------------------------------------------------------- F2.1 Chapter map
def chapter_map(f):
    f.text(400, 30, "Chapter 2 at a glance", size=22, weight="700")
    cols = [("Learn", ["2.1 Writing rules or learning them", "2.2 How a model learns",
                       "2.6 Where generative AI fits"]),
            ("Diagnose", ["2.3 A model learns its sample", "2.4 Labels and balance",
                          "2.5 Right for the wrong reasons"]),
            ("Do", ["2.7 A2: concept map of 15 terms", "Labs 2.1–2.3 (optional)"])]
    for c, (head, items) in enumerate(cols):
        x = 30 + c * 255
        f.text(x + 115, 74, head, size=16, weight="700")
        for i, it in enumerate(items):
            role = "neutral" if c < 2 else ("verified" if i == 0 else "soft")
            kind = "human" if c == 2 else "step"
            f.box(x, 94 + i * 88, 230, 70, it, role=role, kind=kind, size=14)
        if c < 2:
            f.arrow(x + 236, 217, x + 252, 217)
    # AI Work Loop strip, Verify highlighted
    y = 372
    f.text(150, y, "AI Work Loop:", size=14, weight="700", anchor="end")
    xs = [205, 300, 420, 540, 640]
    for i, step in enumerate(LOOP):
        if step == "Verify":
            f.box(xs[i] - 50, y - 20, 100, 40, step, role="highlight", kind="human", thick=True, size=15)
        else:
            f.text(xs[i], y, step, size=14, color=MUTED[f.mode])
        if i < 4:
            f.text((xs[i] + xs[i + 1]) / 2, y, "→", size=14, color=MUTED[f.mode])
    f.text(400, 410, "This chapter strengthens Verify: question the data behind an output.", size=13,
           color=MUTED[f.mode])
    f.text(400, 436, "Opening case: the recruiting tool that learned the past (Dastin, 2018)", size=13,
           color=MUTED[f.mode])


# ---------------------------------------------------------------- F2.2 rules vs examples
def rules_vs_examples(f):
    lanes = [("Classical programming", [("Data", "neutral", "step"), ("Rules", "human", "human")],
              ("Computer applies the rules", "neutral", "step"), ("Answers", "neutral", "step")),
             ("Machine learning", [("Data", "neutral", "step"), ("Answers (labels)", "human", "human")],
              ("Learning algorithm finds patterns", "ai", "ai"), ("Rules (learned patterns)", "ai", "step"))]
    for r, (name, ins, mid, out) in enumerate(lanes):
        y = 40 + r * 165
        f.text(20, y + 12, name, size=16, weight="700", anchor="start")
        for k, (lab, role, kind) in enumerate(ins):
            f.box(30, y + 30 + k * 60, 170, 50, lab, role=role, kind=kind, size=14)
            f.arrow(202, y + 55 + k * 60, 290, y + 85)
        f.box(295, y + 45, 220, 80, mid[0], role=mid[1], kind=mid[2], size=14)
        f.arrow(517, y + 85, 575, y + 85)
        f.box(580, y + 55, 190, 60, out[0], role=out[1], kind=out[2], size=14,
              thick=(r == 1))
    f.text(400, 385, "Rounded = supplied by people · hexagon = AI component · thick border = what the machine produces",
           size=13, color=MUTED[f.mode], width=760)


# ---------------------------------------------------------------- F2.3 learning loop
def learning_loop(f):
    pos = [(400, 70), (650, 230), (400, 390), (150, 230)]
    steps = [("1. Predict", 'The model guesses: "nut"', "ai", "ai"),
             ("2. Measure the error", 'The label says "bolt": wrong, and by how much', "neutral", "step"),
             ("3. Adjust", "Settings shift slightly toward the right answer", "neutral", "step"),
             ("4. Repeat", "Next example, thousands of times", "neutral", "step")]
    bw, bh = 250, 92
    for i, (x, y) in enumerate(pos):
        nx, ny = pos[(i + 1) % 4]
        # arrows between box edges
        if i == 0:
            f.arrow(x + bw / 2 + 4, y + 10, nx - 30, ny - bh / 2 - 6, curve=-30)
        elif i == 1:
            f.arrow(x - 30, y + bh / 2 + 6, nx + bw / 2 + 4, ny - 10, curve=-30)
        elif i == 2:
            f.arrow(x - bw / 2 - 4, y - 10, nx + 30, ny + bh / 2 + 6, curve=-30)
        else:
            f.arrow(x + 30, y - bh / 2 - 6, nx - bw / 2 - 4, ny + 10, curve=-30)
    for (x, y), (h, s, role, kind) in zip(pos, steps):
        f.box(x - bw / 2, y - bh / 2, bw, bh, h, role=role, kind=kind, size=16, sub=s, sub_size=13)
    f.text(400, 222, "Each round:", size=14, weight="700")
    f.text(400, 246, "a little less error", size=14)
    f.text(400, 470, "Hexagon = the model's output · rectangles = steps of the training procedure",
           size=13, color=MUTED[f.mode])


# ---------------------------------------------------------------- F2.4 Signature 3: Data-to-Prediction Pipeline
STAGES = [("1. Collect data", "Which examples? From whom?", "step"),
          ("2. Label", "Who decides the answers? By which guideline?", "human"),
          ("3. Train", "Which model? How long?", "ai"),
          ("4. Predict", "On which new cases?", "ai")]


def pipeline(highlight=(), notes=None):
    """highlight: indices of stages (0-3, 4 = feedback) to mark as the problem stage."""
    notes = notes or {}

    def draw(f):
        bw, bh, gap = 170, 110, 26
        x0, y0 = 22, 70
        f.text(400, 28, "The Data-to-Prediction Pipeline", size=18, weight="700")
        for i, (h, s, kind) in enumerate(STAGES):
            x = x0 + i * (bw + gap)
            hl = i in highlight
            role = "risk" if hl else ("ai" if kind == "ai" else "neutral")
            f.box(x, y0, bw, bh, h, role=role, kind="human" if kind == "human" else kind,
                  thick=hl, size=16, sub=s, sub_size=13)
            if i < 3:
                f.arrow(x + bw + 2, y0 + bh / 2, x + bw + gap - 2, y0 + bh / 2)
            if i in notes:
                f.text(x + bw / 2, y0 + bh + 34, notes[i], size=13, weight="700", width=bw + 10)
        # feedback stage
        hl = 4 in highlight
        fx, fy, fw, fh = 230, 270, 340, 64
        f.box(fx, fy, fw, fh, "5. Feedback", role="risk" if hl else "soft", kind="step", dashed=True,
              thick=hl, size=15, sub="Decisions based on predictions become new data", sub_size=13)
        last = x0 + 3 * (bw + gap) + bw / 2
        f.arrow(last, y0 + bh + (60 if 3 in notes else 4), fx + fw + 4, fy + fh / 2, curve=-40)
        f.arrow(fx - 4, fy + fh / 2, x0 + bw / 2, y0 + bh + (60 if 0 in notes else 4), curve=-40)
        legend = "Rounded = human decision · hexagon = AI component · dashed = loop back into the data"
        if highlight:
            legend = "Hatched/colored with thick border = where the problem enters · " + legend
        f.text(400, 372, legend, size=13, color=MUTED[f.mode], width=770)
    return draw


# ---------------------------------------------------------------- F2.5 population vs sample
def population_sample(f):
    ink = INK[f.mode]
    f.box(20, 40, 760, 300, "", role="soft", kind="human")
    f.text(40, 64, "Population: everything the model will meet in the real world", size=15, weight="700",
           anchor="start")
    # population symbols: three groups (shape, not color, carries meaning)
    import random
    rnd = random.Random(7)
    for _ in range(120):
        x, y = rnd.uniform(50, 750), rnd.uniform(90, 325)
        if 300 < x < 520 and 120 < y < 300:
            continue
        shape = rnd.choice(["c", "t", "s"])
        if shape == "c":
            f.raw(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="5" fill="none" stroke="{ink}" stroke-width="1.4"/>')
        elif shape == "t":
            f.raw(f'<polygon points="{x:.0f},{y - 6:.0f} {x + 6:.0f},{y + 5:.0f} {x - 6:.0f},{y + 5:.0f}" '
                  f'fill="none" stroke="{ink}" stroke-width="1.4"/>')
        else:
            f.raw(f'<rect x="{x - 5:.0f}" y="{y - 5:.0f}" width="10" height="10" fill="none" stroke="{ink}" '
                  f'stroke-width="1.4"/>')
    # the sample: mostly circles
    f.raw(f'<rect x="300" y="120" width="220" height="180" rx="14" fill="#FFFFFF" stroke="{ink}" '
          f'stroke-width="2.6" stroke-dasharray="8 5"/>')
    f.text(410, 140, "Sample: the examples we have", size=14, weight="700")
    for k in range(18):
        x, y = 325 + (k % 6) * 34, 175 + (k // 6) * 38
        if k in (5, 11):
            f.raw(f'<rect x="{x - 5}" y="{y - 5}" width="10" height="10" fill="{ink}"/>')
        else:
            f.raw(f'<circle cx="{x}" cy="{y}" r="6" fill="{ink}"/>')
    f.text(410, 285, "mostly one kind", size=13, italic=True)
    gaps = [(120, "Coverage gap", "never sampled (no triangles in the sample)"),
            (400, "Non-response", "asked, but did not answer"),
            (680, "Selection", "entered only by meeting a condition")]
    for x, h, s in gaps:
        f.text(x, 372, h, size=15, weight="700")
        f.text(x, 396, s, size=13, width=230)
    f.text(400, 440, "Filled shapes = in the sample · outlines = in the world, not in the sample", size=13,
           color=MUTED[f.mode])


# ---------------------------------------------------------------- F2.6 symptoms
def symptoms(f):
    rows = [("Works in testing, fails in the field", "Sampling bias", "Test on the group that was missing"),
            ("Unstable, contradictory predictions", "Noisy labels", "Label twice and compare"),
            ("Consistently unfair to one group", "Biased labels", "Ask what the label really measures"),
            ("High overall accuracy, small class missed", "Class imbalance", "Score the small class separately"),
            ("Success that collapses when conditions change", "Shortcut clue", "Vary the conditions and retest")]
    f.text(130, 30, "Symptom you see", size=15, weight="700")
    f.text(400, 30, "Likely problem", size=15, weight="700")
    f.text(660, 30, "First check", size=15, weight="700")
    for i, (sym, prob, chk) in enumerate(rows):
        y = 60 + i * 76
        f.text(130, y + 30, sym, size=14, width=230)
        f.arrow(255, y + 30, 312, y + 30)
        f.box(318, y + 6, 164, 48, prob, role="risk" if prob == "Biased labels" else "neutral",
              kind="decision" if False else "step", thick=prob == "Biased labels", size=15)
        f.arrow(486, y + 30, 540, y + 30)
        f.text(660, y + 30, chk, size=14, width=220)
        if i < 4:
            f.line(20, y + 68, 780, y + 68, color=MUTED[f.mode], width=0.6)
    f.text(400, 448, "Thick border: the problem our experiment showed to be the most damaging (section 2.4).",
           size=13, color=MUTED[f.mode])


# ---------------------------------------------------------------- F2.7 shortcut
def shortcut(f):
    f.text(150, 28, "Training photos", size=16, weight="700")
    f.box(20, 48, 260, 70, "Bolts, photographed on a brown desk", role="neutral", kind="step", size=14)
    f.box(20, 132, 260, 70, "Nuts and washers, photographed on a white table", role="soft", kind="step",
          size=14)
    f.arrow(284, 83, 338, 118)
    f.arrow(284, 167, 338, 134)
    f.text(470, 28, "What the model learned", size=16, weight="700")
    f.box(342, 82, 256, 86, '"Brown background = bolt"', role="ai", kind="ai", dashed=True, size=15,
          sub="an easier rule than the shape", sub_size=13)
    f.text(470, 196, "Testing on photos from the same desk and table: almost all correct", size=13,
           width=300, color=MUTED[f.mode])
    f.arrow(470, 222, 470, 262)
    f.text(470, 250, "", size=13)
    f.box(320, 268, 300, 80, 'At the club workbench (new background): a nut is called "bolt"', role="risk",
          kind="step", thick=True, size=14)
    f.text(710, 296, "Predictions", size=15, weight="700")
    f.text(710, 318, "collapse", size=15, weight="700")
    f.text(400, 390, "Dashed = a rule nobody intended · thick border = the failure", size=13,
           color=MUTED[f.mode])


# ---------------------------------------------------------------- F2.11 nested family
def nested(f):
    levels = [("Artificial intelligence", "Systems that do tasks we associate with intelligence · e.g., a rule-based expert system"),
              ("Machine learning", "Learns rules from data · e.g., a credit-scoring model"),
              ("Deep learning", "Many layers of simple units · e.g., photo recognition"),
              ("Generative AI", "Produces new content · e.g., an image generator"),
              ("Large language models", "Generate text · e.g., today's chat tools")]
    fills = {"color": ["#FFFFFF", "#EEF2F7", "#D5DFEC", "#FCE38A", "#F7D24D"],
             "gray": ["#FFFFFF", "#F2F2F2", "#E0E0E0", "#CFCFCF", "#BDBDBD"]}
    ink = INK[f.mode]
    for i, (h, s) in enumerate(levels):
        x, y = 20 + i * 40, 20 + i * 74
        w, hgt = 760 - i * 80, 440 - i * 86
        dash = ' stroke-dasharray="7 5"' if i >= 3 else ""
        f.raw(f'<rect x="{x}" y="{y}" width="{w}" height="{hgt}" rx="16" fill="{fills[f.mode][i]}" '
              f'stroke="{ink}" stroke-width="{2.4 if i == 3 else 1.6}"{dash}/>')
        f.text(x + 18, y + 24, h, size=16, weight="700", anchor="start")
        f.text(x + 18, y + 48, s, size=13, anchor="start")
    f.text(400, 478, "Each box sits inside the one around it. Dashed = generates content; same learning loop, much larger scale.",
           size=13, color=MUTED[f.mode], width=770)


# ---------------------------------------------------------------- F2.12 concept map
def concept_map(f):
    nodes = {"data": (130, 90, "Training data"), "labels": (130, 300, "Labels"),
             "model": (400, 90, "Model"), "pred": (670, 90, "Predictions"), "test": (670, 300, "Test set")}
    bw, bh = 170, 56
    links = [("data", "labels", "is paired with", (130, 146), (130, 272), -14, 0),
             ("model", "data", "is trained on", (315, 90), (216, 90), 0, -18),
             ("model", "pred", "produces", (486, 90), (584, 90), 0, -18),
             ("test", "pred", "checks", (670, 272), (670, 120), -14, 0),
             ("test", "data", "must not overlap with", (585, 290), (200, 120), 0, 0)]
    for _, _, lab, (x1, y1), (x2, y2), dx, dy in links:
        f.arrow(x1, y1, x2, y2)
    for k, (x, y, lab) in nodes.items():
        f.box(x - bw / 2, y - bh / 2, bw, bh, lab, role="neutral", kind="human", size=16)
    # link labels placed clear of lines
    f.text(70, 210, "is paired with", size=14, italic=True, weight="600", anchor="middle", width=110)
    f.text(265, 64, "is trained on", size=14, italic=True, weight="600")
    f.text(535, 64, "produces", size=14, italic=True, weight="600")
    f.text(730, 196, "checks", size=14, italic=True, weight="600")
    f.text(350, 250, "must not overlap with", size=14, italic=True, weight="600")
    f.text(400, 372, "Read each link as a sentence: “A model is trained on training data.”", size=14)
    f.text(400, 400, "Rounded boxes = terms · italic arrow labels = the relationship", size=13,
           color=MUTED[f.mode])


# ---------------------------------------------------------------- F2.13 timeline
def timeline(f):
    ink = INK[f.mode]
    y = 150
    events = ["1956 Dartmouth workshop (term used in its 1955 proposal)", "1980s expert systems",
              "1997 Deep Blue beats the world chess champion",
              "2012 a deep network leaps ahead in image recognition", "2016 AlphaGo beats a top Go player",
              "2017 the Transformer", "2022 ChatGPT released to the public"]
    xs = [70 + i * 110 for i in range(7)]
    f.line(30, y, 770, y, color=ink, width=2)
    for i, (x, lab) in enumerate(zip(xs, events)):
        f.raw(f'<circle cx="{x}" cy="{y}" r="7" fill="{ink}"/>')
        if i % 2 == 0:
            f.line(x, y - 8, x, y - 34, color=ink, width=1)
            f.text(x, y - 66, lab, size=13, width=140)
        else:
            f.line(x, y + 8, x, y + 34, color=ink, width=1)
            f.text(x, y + 66, lab, size=13, width=140)
    bands = [(20, 290, "Wave 1: rules, logic, early learning"), (300, 620, "Wave 2: deep learning"),
             (630, 780, "Wave 3: generative")]
    fills = {"color": ["#EEF2F7", "#D5DFEC", "#FCE38A"], "gray": ["#F4F4F4", "#D6D6D6", "#ADADAD"]}
    for i, (a, b, lab) in enumerate(bands):
        f.raw(f'<rect x="{a}" y="262" width="{b - a}" height="36" fill="{fills[f.mode][i]}" '
              f'stroke="{ink}" stroke-width="1"/>')
        f.text((a + b) / 2, 280, lab, size=14, weight="700")
    f.text(400, 316, "Events evenly spaced, not to scale", size=13, italic=True, color=MUTED[f.mode])
    f.text(40, 350, "Why now? Three things matured together:", size=15, weight="700", anchor="start")
    for i, (h, s) in enumerate([("Data", "huge amounts of digital text and images"),
                                ("Compute", "cheap parallel processing on graphics chips and computer clusters"),
                                ("Algorithms", "training methods for very large networks")]):
        f.box(30 + i * 252, 368, 236, 84, h, role="neutral", kind="step", size=15, sub=s, sub_size=13)


# ---------------------------------------------------------------- F2.15 summary card
def summary_card(f):
    f.text(400, 26, "Chapter 2 — what you can do now", size=18, weight="700")
    cards = ["Classify: rules written by people, or patterns learned from examples",
             "Explain: predict → measure the error → adjust → repeat",
             "Diagnose: who is in the sample, and who is missing?",
             "Diagnose: noisy vs. biased labels; always score the small class",
             "Judge: tested on new examples, in real conditions, for every class?",
             "Place: AI ⊃ machine learning ⊃ deep learning ⊃ generative AI ⊃ large language models"]
    for i, c in enumerate(cards):
        x = 20 + (i % 3) * 258
        y = 50 + (i // 3) * 150
        f.box(x, y, 242, 130, c, role="neutral" if i % 2 else "soft", kind="human", size=14, weight="600")


FIGS = [
    ("f2-01-chapter-map", chapter_map, 800, 455, "Chapter 2 at a glance"),
    ("f2-02-rules-vs-examples", rules_vs_examples, 800, 400,
     "In machine learning, people supply the answers and the machine finds the rule"),
    ("f2-03-learning-loop", learning_loop, 800, 490, "Learning is many small corrections toward less error"),
    ("f2-04-pipeline", pipeline(), 800, 390,
     "Every prediction inherits the choices made in collecting and labeling its data"),
    ("f2-04b-pipeline-sampling", pipeline((0,), {0: "Who is in the sample?"}), 800, 390,
     "The sampling stage: every later stage inherits who was in the sample"),
    ("f2-04c-pipeline-labels", pipeline((1,), {1: "Human decisions or recorded outcomes, often from the past"}), 800, 390,
     "The labeling stage: a label is a human decision"),
    ("f2-04d-pipeline-case", pipeline((0, 1, 2), {0: "Mostly résumés from men", 1: "Possibly past hiring decisions",
                                                  2: "Proxy words such as “women's”"}), 800, 390,
     "The recruiting tool: problems at three stages of the pipeline"),
    ("f2-05-population-sample", population_sample, 800, 460, "A model learns its sample, not the world"),
    ("f2-07-shortcut", shortcut, 800, 410, "A model can score well for the wrong reason"),
    ("f2-11-nested-family", nested, 800, 495,
     "Generative AI is a branch of machine learning, not a different kind of thing"),
    ("f2-12-concept-map", concept_map, 800, 420, "A concept map is a set of labeled links between terms"),
    ("f2-13-timeline", timeline, 800, 465, "Old ideas became practical when data, computing power and algorithms matured together"),
    ("f2-15-summary-card", summary_card, 800, 340, "Chapter 2 summary card"),
]

if __name__ == "__main__":
    for fid, fn, w, h, title in FIGS:
        render(fid, fn, w, h, title, ROOT)
        print("rendered", fid)
