"""Chapter 16 diagrams (SVG, color + gray). Run from the repo root:
    python3 figures/scripts/ch16_figures.py [figure-id ...]
Data charts are in ch16_charts.py (data/ch16_*.csv).

New signature introduced here (Signature 11, reused in Chapters 11 and 17):
    bias_lifecycle(highlight=None, notes=None, dashed=None, tag=None, note=None)
        The Bias Lifecycle: four phases (data, model, use, feedback) with a return arrow from feedback
        to data, and "people affected" below.  All phases are drawn solid; `dashed` marks a placement
        as inferred (book-wide solid = documented, dashed = inferred).  `highlight` takes one phase or a
        list (thick border; risk fill in color, hatched in print).  `notes` = {phase: short note} printed
        under that phase.  `tag` = one bold line above the legend; `note` = one muted line under the title.
        Canvas 800 x 476 (lifecycle_height()).

Reused, never redrawn: Signature 5 and the chain (`from ch04_figures import failure_tree, failure_chain,
tree_height`); Signature 10 (`from ch15_figures import risk_heat_map`), only if Chapter 15 has coded it.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from figlib import render, MUTED, INK  # noqa: E402
from ch04_figures import failure_tree, failure_chain, tree_height  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LOOP = ["Frame", "Prompt", "Verify", "Decide", "Disclose"]

PHASES = ["data", "model", "use", "feedback"]
PHASE_LABEL = {"data": "1. Data", "model": "2. Model", "use": "3. Use", "feedback": "4. Feedback"}
PHASE_Q = {"data": "Who is in it? How were labels made? Which proxies?",
           "model": "What was it trained and tested to do?",
           "use": "Who uses it, for what decision, on whom?",
           "feedback": "Do its decisions become new data?"}
PHASE_KIND = {"data": "step", "model": "ai", "use": "human", "feedback": "step"}


def _set(x):
    if x is None:
        return set()
    if isinstance(x, str):
        return {x}
    return set(x)


def lifecycle_height():
    return 476


# ---------------------------------------------------------------- Signature 11 (new, reusable)
def bias_lifecycle(highlight=None, notes=None, dashed=None, tag=None, note=None):
    """Signature 11, the Bias Lifecycle (5 boxes). See the module docstring."""
    hl, dz, notes = _set(highlight), _set(dashed), notes or {}
    for s in (hl, dz, set(notes)):
        if s - set(PHASES):
            raise ValueError(f"unknown phase: {s - set(PHASES)}")

    def draw(f):
        muted = MUTED[f.mode]
        f.text(400, 22, "The Bias Lifecycle: where bias can enter", size=18, weight="700")
        if note:
            f.text(400, 46, note, size=13, color=muted, italic=True, width=760)
        bw, bh, gap, x0, y0 = 170, 112, 26, 22, 66
        for i, p in enumerate(PHASES):
            x = x0 + i * (bw + gap)
            on = p in hl
            kind = PHASE_KIND[p]
            role = "risk" if on else ("ai" if kind == "ai" else "neutral")
            f.box(x, y0, bw, bh, PHASE_LABEL[p], role=role, kind=kind, thick=on, dashed=(p in dz),
                  size=16, sub=PHASE_Q[p], sub_size=13)
            if i < 3:
                f.arrow(x + bw + 2, y0 + bh / 2, x + bw + gap - 2, y0 + bh / 2)
            if p in notes:
                f.text(x + bw / 2, y0 + bh + 40, notes[p], size=13, weight="600", width=bw + 12)
        # return arrow: feedback -> data (solid; decisions become new data)
        fx = x0 + 3 * (bw + gap) + bw / 2
        dx = x0 + bw / 2
        f.arrow(fx, 252, dx, 252, curve=-30)
        f.text(400, 286, "decisions become new data, and the loop starts again", size=13, color=muted, italic=True)
        # people affected
        f.box(250, 304, 300, 46, "People affected: everyone the decisions reach", role="neutral", kind="human",
              size=14)
        if tag:
            f.text(400, 372, tag, size=13, weight="700", width=770)
        f.text(400, 404, "Sources of harm named by Suresh & Guttag (2021): historical, representation, measurement "
               "(data) · learning, aggregation, evaluation (model) · deployment (use). Feedback loops: this "
               "book's fourth phase (Ensign et al., 2018).", size=13, color=muted, width=790)
        f.text(400, 446, "Rectangle = step · hexagon = AI component · rounded = people · thick border (hatched in "
               "print) = the phase this figure marks · dashed = placement inferred", size=13, color=muted,
               width=790)
    return draw


# ---------------------------------------------------------------- F16.1 Chapter map
def chapter_map(f):
    muted = MUTED[f.mode]
    f.text(400, 30, "Chapter 16 at a glance", size=22, weight="700")
    cols = [("Where and how much", ["16.1 The Bias Lifecycle", "16.2 Measure group by group",
                                    "16.3 What \"fair\" can mean"]),
            ("Test and fix", ["16.4 Paired-input tests", "16.5 Mitigation and its limits",
                              "16.6 Who decides?"]),
            ("Practice", ["16.7 Bias probe and fairness row", "Lab 15.1 station 3 (Thursday)",
                          "A12 (Chapter 15)"])]
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
    xs = [205, 300, 420, 540, 640]
    for i, step in enumerate(LOOP):
        if step == "Verify":
            f.box(xs[i] - 50, y - 20, 100, 40, step, role="highlight", kind="human", thick=True, size=15)
        elif step == "Decide":
            f.box(xs[i] - 46, y - 16, 92, 32, "Decide (2nd)", role="neutral", kind="human", size=13)
        else:
            f.text(xs[i], y, step, size=14, color=muted)
        if i < 4:
            f.text((xs[i] + xs[i + 1]) / 2, y, "→", size=14, color=muted)
    f.text(400, 410, "This chapter strengthens Verify (test group by group), then Decide, second (who chooses "
           "what counts as fair).", size=13, color=muted, width=780)
    f.text(400, 436, "Opening case: Gender Shades (Buolamwini & Gebru, 2018), an audit of gender classification",
           size=13, color=muted)


# ---------------------------------------------------------------- F16.2 storyboard
def storyboard(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "Gender Shades: from a missed face to a re-test", size=18, weight="700")
    top = [("Demo misses her face", "until she wears a white mask (her account)"),
           ("A balanced benchmark", "1,270 parliamentarians, six countries"),
           ("April–May 2017 audit", "three gender classifiers"),
           ("Results by subgroup", "darker-skinned women: 20.8–34.7% error")]
    bw, bh = 176, 92
    for i, (a, b) in enumerate(top):
        x = 18 + i * 196
        f.box(x, 52, bw, bh, a, role="neutral", kind="human" if i == 0 else "step", dashed=(i == 0), size=14,
              sub=b, sub_size=13)
        if i < 3:
            f.arrow(x + bw + 2, 98, x + 194, 98)
    f.arrow(694, 146, 694, 182)
    bot = [(606, "Dec 19, 2017", "results sent to the companies, unnamed", "neutral"),
           (410, "Feb 2018", "paper public, companies named", "neutral"),
           (214, "Aug 21, 2018 re-test", "all three cut the largest gap", "verified")]
    for x, a, b, r in bot:
        f.box(x, 184, bw, bh, a, role=r, kind="step", size=14, sub=b, sub_size=13)
    f.arrow(604, 230, 588, 230)
    f.arrow(408, 230, 392, 230)
    f.box(18, 184, bw, bh, "June 2020: IBM and Amazon facial-recognition and analysis decisions. Link not "
          "established", role="soft", kind="step", size=13, weight="normal")
    f.text(400, 304, "Solid = in the published record · dashed = reported (her own account) · gray box with no "
           "arrow = a later event; link to the audit not established", size=13, color=muted, width=780)
    f.text(400, 330, "Sources: Buolamwini & Gebru (2018); Raji & Buolamwini (2019); Buolamwini (2023)", size=13,
           color=muted)


# ---------------------------------------------------------------- F16.5 two harms
def harms(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "Two kinds of harm", size=18, weight="700")
    cols = [("Allocation harm", "An opportunity or resource is withheld",
             ["A job shortlist (Ch. 2's recruiting tool)", "A care program (Ch. 11's health algorithm)",
              "A tutoring offer (Elif's outreach score)"]),
            ("Representation harm", "A group is stereotyped, demeaned or left out",
             ["Images of \"a software developer\"", "Default descriptions of \"a typical\" person",
              "A group missing from examples"])]
    for c, (head, sub, items) in enumerate(cols):
        x = 40 + c * 380
        f.box(x, 50, 340, 70, head, role="risk" if c == 0 else "neutral", kind="step", thick=(c == 0), size=16,
              sub=sub, sub_size=13)
        for i, it in enumerate(items):
            f.text(x + 170, 150 + i * 30, "· " + it, size=13, width=330)
    f.text(400, 250, "The same system can cause both. Allocation harms show up in decisions; representation "
           "harms show up in what people see and read.", size=13, color=muted, width=760)
    f.text(400, 286, "After Blodgett et al. (2020)", size=13, color=muted, italic=True)


# ---------------------------------------------------------------- F16.8 three fairness questions
def three_questions(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "Three fairness definitions, three questions", size=18, weight="700")
    f.box(270, 46, 260, 56, "A tool that flags people", role="ai", kind="ai", size=15)
    qs = [("Equal selection rates", "Is the same share of each group flagged?"),
          ("Equal error rates", "Is the same share missed, and the same share wrongly flagged?"),
          ("Equal precision", "Does a flag mean the same thing in each group?")]
    for i, (a, b) in enumerate(qs):
        x = 30 + i * 255
        f.arrow(400, 104, x + 115, 136)
        f.box(x, 138, 230, 96, a, role="neutral", kind="decision", size=14)
        f.text(x + 115, 262, b, size=13, width=220)
    f.text(400, 312, "When groups differ in how often the outcome really occurs (the base rate), a tool that "
           "makes errors cannot meet all three at once.", size=13, weight="600", width=760)
    f.text(400, 346, "Diamond = a question you must answer for the decision · hexagon = AI component", size=13,
           color=muted)


# ---------------------------------------------------------------- F16.10 paired-input test
def paired_input(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "A paired-input test", size=18, weight="700")
    f.box(20, 60, 150, 70, "One input", role="neutral", kind="step", size=14, sub="fixed text", sub_size=13)
    f.box(210, 40, 150, 50, "Version 1", role="neutral", kind="step", size=14)
    f.box(210, 104, 150, 50, "Version 2", role="neutral", kind="step", size=14)
    f.text(285, 172, "only one cue changed", size=13, color=muted, italic=True)
    f.arrow(172, 88, 208, 66)
    f.arrow(172, 102, 208, 128)
    f.box(400, 60, 160, 74, "Counting rule", role="neutral", kind="human", size=14, sub="fixed before any run",
          sub_size=13)
    f.arrow(362, 66, 398, 86)
    f.arrow(362, 128, 398, 110)
    f.box(600, 54, 180, 86, "Many fresh runs of each", role="ai", kind="ai", size=14,
          sub="same tool, memory off", sub_size=13)
    f.arrow(562, 97, 598, 97)
    f.box(600, 210, 180, 70, "Counts with totals", role="neutral", kind="step", size=14, sub="e.g., 31 of 39",
          sub_size=13)
    f.arrow(690, 142, 690, 208)
    f.box(330, 196, 220, 100, "Gap ≥ chance threshold?", role="neutral", kind="decision", size=14,
          sub="the table in 16.4", sub_size=13)
    f.arrow(598, 246, 552, 246)
    f.box(30, 200, 200, 40, "Yes: a finding", role="verified", kind="step", size=14)
    f.box(30, 254, 200, 40, "No: a lead; run more", role="soft", kind="step", dashed=True, size=14)
    f.arrow(330, 238, 232, 222)
    f.arrow(330, 256, 232, 272)
    f.text(400, 326, "Rounded = a person's decision · hexagon = AI runs · diamond = a check · dashed = inferred "
           "(a lead)", size=13, color=muted)


# ---------------------------------------------------------------- F16.15 fairness choice record
def choice_record(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "Who decides what is fair, and on what record", size=18, weight="700")
    boxes = [("The decision", "is AI needed for it at all?", "step", "neutral"),
             ("Which error harms whom?", "a miss or a false flag", "decision", "neutral"),
             ("Fairness definition", "and the trade-off accepted", "step", "neutral"),
             ("People affected asked", "stakeholders, not only users", "human", "neutral"),
             ("Decision owner records", "the choice and its reason", "human", "highlight")]
    xs = [10, 168, 340, 490, 645]
    ws = [148, 162, 140, 145, 145]
    for i, (a, b, k, r) in enumerate(boxes):
        hh = 120 if k == "decision" else 88
        yy = 60 if k == "decision" else 76
        f.box(xs[i], yy, ws[i], hh, a, role=r, kind=k, size=14, sub=b, sub_size=13)
        if i < 4:
            f.arrow(xs[i] + ws[i] + 2, 120, xs[i + 1] - 2, 120)
    f.text(400, 214, "The numbers show what each choice costs; people decide which cost is acceptable.", size=13,
           weight="600")
    f.text(400, 244, "Rectangle = step · diamond = a judgment · rounded = people", size=13, color=muted)


# ---------------------------------------------------------------- F16.16 bias-probe sheet
def probe_sheet(f):
    muted = MUTED[f.mode]
    f.text(400, 22, "Bias-probe sheet (Lab 15.1 station 3; A12 items 3 and 4c)", size=18, weight="700")
    rows = [("1 Prompt pair", "station prompt A, B or C; the one cue that changes"),
            ("2 Phase", "where a gap would most likely enter (16.1)"),
            ("3 Counting rule", "the station's preregistered rule (exact words count)"),
            ("4 Your counts", "version 1: _ of 3 · version 2: _ of 3 (C: of 2; printed: of 3) · tool, date, model"),
            ("5 Subtotal, pooled", "table line on the class sheet; pooled _ of _ vs. _ of _ (printed apart)"),
            ("6 Lead or finding", "counts differ by at least the threshold for that many runs (16.4)?"),
            ("7 Fairness row", "worse error · harm kind · phase · likelihood · impact · marker · fix · owner")]
    for i, (a, b) in enumerate(rows):
        y = 48 + i * 48
        f.box(20, y, 190, 40, a, role="neutral", kind="step", size=14)
        f.box(220, y, 560, 40, b, role="soft", kind="step", size=13, weight="normal")
    f.text(400, 400, "Marker solid only if the two-part rule passes on the same tool and kind of task as your "
           "workflow; otherwise dashed (inferred)", size=13, color=muted, width=780)


# ---------------------------------------------------------------- F16.20 summary card
def summary_card(f):
    f.text(400, 24, "Chapter 16 in six cards", size=18, weight="700")
    cards = [("Four phases", "data · model · use · feedback"),
             ("Measure by group", "with counts and intersections"),
             ("Is the gap real?", "fair test + gap above the chance threshold"),
             ("Three fairness questions", "selection · errors · precision; choose"),
             ("Fix by phase", "avoid, reduce, detect, accept; test again"),
             ("Who decides", "people affected asked; owner answers")]
    for i, (a, b) in enumerate(cards):
        x = 20 + (i % 3) * 260
        y = 50 + (i // 3) * 130
        f.box(x, y, 240, 110, a, role="verified" if i == 5 else "neutral", kind="human" if i == 5 else "step",
              size=15, sub=b, sub_size=13)
    f.text(400, 316, "Rounded = a decision by people", size=13, color=MUTED[f.mode])


# ---------------------------------------------------------------- F16.21 Deep: the identity
def identity(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "Same flag meaning, different base rates", size=18, weight="700")
    cols = [("Group A", "base rate 50%", "flag means: 65.4% needed help", "missed: 15.0%",
             "wrongly flagged: 45.0%"),
            ("Group B", "base rate 30%", "flag means: 66.0% needed help", "missed: 45.0%",
             "wrongly flagged: 12.1%")]
    for c, (g, br, pr, mr, fp) in enumerate(cols):
        x = 60 + c * 380
        f.box(x, 50, 300, 52, g, role="neutral", kind="step", size=16, sub=br, sub_size=13)
        f.box(x, 116, 300, 40, pr, role="verified", kind="step", size=14)
        f.box(x, 170, 300, 40, mr, role="risk" if c == 1 else "neutral", kind="step", thick=(c == 1), size=14)
        f.box(x, 224, 300, 40, fp, role="risk" if c == 0 else "neutral", kind="step", thick=(c == 0), size=14)
    f.text(400, 296, "wrongly flagged = base rate ÷ (1 − base rate) × (1 − precision) ÷ precision × (1 − miss rate)",
           size=14, weight="700", width=780)
    f.text(400, 326, "With precision held equal, a group with a higher base rate must have more wrong flags, "
           "more misses, or both (unless no one is flagged wrongly).", size=13, width=780)
    f.text(400, 356, "This book's calculation (one threshold, 0.5): data/ch16_tradeoff.csv; identity from "
           "Chouldechova (2017). Thick border = the larger error in that row.", size=13, color=muted, width=780)


# ---------------------------------------------------------------- instances of the signature
LIFECYCLE_INTRO = bias_lifecycle(
    highlight="data",
    notes={"data": "proxies such as \"women's\" (Ch. 2) · the label: cost for need (Ch. 11)",
           "model": "one overall score, or tested group by group?",
           "use": "a tool built for one setting, used in another",
           "feedback": "people never chosen never show the tool was wrong"},
    tag="Chapter 2's recruiting tool and Chapter 11's health algorithm both let bias in at the data phase")

LIFECYCLE_ELIF = bias_lifecycle(
    highlight="data",
    notes={"data": "label: \"visited the center\" (who knew and came), not who needed help",
           "model": "tested only on overall accuracy",
           "use": "outreach emails in English only",
           "feedback": "students never emailed never visit"},
    dashed=["use", "feedback"],
    tag="Elif's reading of the outreach score (constructed): data marked; use and feedback inferred")

LIFECYCLE_FIX = bias_lifecycle(
    notes={"data": "reduce: add missing groups · limit: proxies can stay",
           "model": "reduce: test and tune by group · limit: tuned to one test",
           "use": "avoid: not for this decision · or reduce: a person who can disagree",
           "feedback": "detect: re-run the probe after updates · limit: who is never offered"},
    tag="What remains after every fix: accept it, with a named risk owner (Chapter 15)")

LIFECYCLE_LOOP = bias_lifecycle(
    highlight="feedback",
    notes={"feedback": "patrols → more records → more patrols (Ensign et al., 2018)",
           "data": "records show where people looked, not only what happened"},
    tag="A runaway feedback loop: the system is sent back to where it already looked")

C13_TREE = failure_tree({"bias"}, tag="Case: Gender Shades (2018) · bias, leaf unequal quality across groups, "
                        "documented", note="Error rates measured group by group in a published audit")
C13_CHAIN = failure_chain(
    notes={0: "Gender labels with unequal error",
           1: "No published group results (inferred)",
           3: "None documented in this audit"},
    highlight={1}, dashed={1},
    tag="Link 2 is inferred: the documentation showed no group results; internal tests are unknown")
WILLIAMS_CHAIN = failure_chain(
    notes={0: "False match (documented); bias inferred",
           1: "Lineup, no independent evidence (reported)",
           2: "Automation bias (inferred)",
           3: "Wrongful arrest; charges dismissed"},
    highlight={1}, dashed={1, 2},
    tag="Link 2 is reported (the lawsuit's allegations); dashed = inferred or reported")

FIGS = [
    ("f16-01-chapter-map", chapter_map, 800, 455, "Chapter 16 at a glance"),
    ("f16-02-storyboard", storyboard, 800, 345,
     "An outside audit with a balanced benchmark found the gaps, and a re-test showed they could shrink"),
    ("f16-03-lifecycle", LIFECYCLE_INTRO, 800, lifecycle_height(),
     "Bias can enter at four phases, and each phase needs its own check"),
    ("f16-05-lifecycle-elif", LIFECYCLE_ELIF, 800, lifecycle_height(),
     "Elif's outreach score could let bias in at every phase"),
    ("f16-04-harms", harms, 800, 300, "Bias can withhold an opportunity or misrepresent a group"),
    ("f16-08-three-questions", three_questions, 800, 362, "Three fairness definitions ask three different questions"),
    ("f16-10-paired-input", paired_input, 800, 340, "A paired-input test changes one cue and counts many runs"),
    ("f16-12-lifecycle-mitigation", LIFECYCLE_FIX, 800, lifecycle_height(),
     "Each phase has a fix of a named kind, and each fix can hide or move the problem"),
    ("f16-15-choice-record", choice_record, 800, 260,
     "Someone must choose which error matters more, and say who was asked"),
    ("f16-16-probe-sheet", probe_sheet, 800, 420,
     "Your probe sheet records the preregistered rule, the counts with totals and the row it produces"),
    ("f16-19-tree-c13", C13_TREE, 800, tree_height() + 34,
     "Gender Shades on the tree: bias, unequal quality across groups, documented"),
    ("f16-20-chain-c13", C13_CHAIN, 800, 420,
     "The services' documentation reported no group results, so whether they were checked by group is unknown"),
    ("f16-21-chain-williams", WILLIAMS_CHAIN, 800, 420, "A face match treated as proof became a wrongful arrest"),
    ("f16-22-summary-card", summary_card, 800, 330, "Chapter 16 summary card"),
    ("f16-17-identity", identity, 800, 372, "With the same flag meaning, different base rates force different error rates"),
    ("f16-18-feedback-loop", LIFECYCLE_LOOP, 800, lifecycle_height(),
     "A feedback loop sends the system back to where it already looked"),
]


def heat_map_fig():
    """F16.13: Signature 10 reuse. Drawn only if Chapter 15 has coded risk_heat_map."""
    try:
        from ch15_figures import risk_heat_map, HEAT_H  # noqa: E402,F401
    except Exception as exc:  # noqa: BLE001
        print("skipped f16-14-heatmap: ch15_figures.risk_heat_map not available yet (" + type(exc).__name__ + ")")
        return None
    return risk_heat_map(
        risks=[(1, 2, 2, "D")], moves={1: (1, 1)},
        note="Risk 1 (constructed): lower scores when the author line states Turkish, not English, as first language. "
             "Reduce: strip author lines; avoid: score never decides tutoring; owner: the coordinator.")


if __name__ == "__main__":
    only = set(sys.argv[1:])
    for fid, fn, w, h, title in FIGS:
        if only and fid not in only:
            continue
        render(fid, fn, w, h, title, ROOT)
        print("rendered", fid)
    if not only or "f16-14-heatmap" in only:
        hm = heat_map_fig()
        if hm is not None:
            from ch15_figures import HEAT_H
            render("f16-14-heatmap", hm, 800, HEAT_H,
                   "A narrower use and a reduce step lowered Elif's bias risk; its owner accepts what is left",
                   ROOT)
            print("rendered f16-14-heatmap")
