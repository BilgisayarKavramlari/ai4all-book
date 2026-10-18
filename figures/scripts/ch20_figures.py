"""Chapter 20 diagrams (SVG, color + gray). Run from the repo root:
    python3 figures/scripts/ch20_figures.py
Data charts (F20.3 NACE gap, F20.5 WEF jobs) are in ch20_charts.py (data/ch20_*.csv).

Signature 12, Portfolio Anatomy, is introduced here and imported by later chapters:

    from ch20_figures import portfolio_anatomy, PORTFOLIO_PARTS, PORTFOLIO_H
    portfolio_anatomy(highlight=None, note=None)

Parts (PORTFOLIO_PARTS, 9 shapes): "narrative", "map", "artifact", "trace", "verification", "declaration",
"reflection", "code", "defense". The four entry parts sit under one bracket ("each of six entries"), drawn as a
line, not a tenth box.
  highlight: one part or a list; highlighted parts use figlib's "highlight" fill and get the label
             "this section" (meaning survives the gray render without relying on a thick border).
  note:      one line under the figure.
Examples: portfolio_anatomy() (F20.7); portfolio_anatomy(highlight=["artifact", "trace", "verification"]) (F20.9);
          portfolio_anatomy(highlight="code", note="your code sits beside your declaration") (Ch. 21).

Reused, never redrawn: the voice and ownership spectrum (`from ch10_figures import voice_spectrum`).
Dashed outlines in this chapter mean only "reported" (news coverage, as opposed to a company's own page);
each figure that uses them says so in its legend.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from figlib import render, MUTED, INK, ROLES  # noqa: E402
from ch10_figures import voice_spectrum, spectrum_height  # noqa: E402  (reused)

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LOOP = ["Frame", "Prompt", "Verify", "Decide", "Disclose"]


def _as_set(x):
    if x is None:
        return set()
    if isinstance(x, str):
        return {x}
    return set(x)


# ---------------------------------------------------------------- Signature 12: Portfolio Anatomy
PORTFOLIO_PARTS = ["narrative", "map", "artifact", "trace", "verification", "declaration", "reflection", "code",
                   "defense"]
PORTFOLIO_H = 600
_P = {  # part: (x, y, w, h, label, sub, kind)
    "narrative": (250, 58, 300, 62, "Career narrative", "three claims to one named reader", "human"),
    "map": (250, 146, 300, 66, "Evidence map", "artifact · outcome · competency · trail", "step"),
    "artifact": (22, 262, 178, 92, "Artifact", "as submitted, then revised", "step"),
    "trace": (214, 262, 178, 92, "Revision trace", "before → after: what changed and why", "step"),
    "verification": (406, 262, 178, 92, "Verification trail", "checks, verdicts, what stays uncertain", "step"),
    "declaration": (598, 262, 180, 92, "AI Use Declaration", "the AI's part · your part", "step"),
    "reflection": (110, 398, 270, 62, "Reflection", "what changed in your practice since A1", "human"),
    "code": (420, 398, 270, 62, "Code of practice", "your commitments (Chapter 21)", "human"),
    "defense": (250, 498, 300, 62, "Oral defense", "3 + 2 minutes, live", "human"),
}


def portfolio_anatomy(highlight=None, note=None):
    """Signature 12 (9 shapes): narrative -> evidence map -> entries (artifact, revision trace, verification
    trail, declaration) -> reflection and code of practice -> oral defense."""
    hl = _as_set(highlight)
    unknown = hl - set(PORTFOLIO_PARTS)
    if unknown:
        raise ValueError(f"unknown portfolio part(s): {sorted(unknown)}")

    def draw(f):
        muted = MUTED[f.mode]
        f.text(400, 26, "Portfolio Anatomy: a narrative backed by entries, each carrying its own evidence",
               size=16, weight="700", width=780)
        for part in PORTFOLIO_PARTS:
            x, y, w, h, lab, sub, kind = _P[part]
            on = part in hl
            role = "highlight" if on else ("soft" if kind == "step" else "neutral")
            f.box(x, y, w, h, lab, role=role, kind=kind, size=15, sub=sub, sub_size=13)
            if on:
                f.text(x + w / 2, y - 9, "this section", size=13, weight="700", italic=True)
        # arrows (placed off-center so none crosses a "this section" label)
        f.arrow(290, 122, 290, 144)
        # bracket over the four entry parts (a line, not a box)
        by = 240
        f.line(22, by, 778, by, width=2.0)
        f.line(22, by, 22, by + 10, width=2.0)
        f.line(778, by, 778, by + 10, width=2.0)
        f.text(600, by - 12, "each of at least six entries (one of them A13)", size=13, weight="600",
               color=INK[f.mode])
        f.arrow(400, 214, 400, 238)
        f.arrow(180, 356, 180, 396)
        f.arrow(640, 356, 640, 396)
        f.arrow(245, 462, 330, 496)
        f.arrow(555, 462, 470, 496)
        f.text(612, 486, "live, no tool", size=13, italic=True, color=muted)
        y = 580
        if note:
            f.text(400, 574, note, size=13, italic=True, color=muted, width=780)
            y = 594
        f.text(400, y, "Rounded = your judgment in your own words · rectangle = a record a reader can check",
               size=13, color=muted, width=780)
    return draw


# ---------------------------------------------------------------- F20.1 Chapter map
def chapter_map(f):
    muted = MUTED[f.mode]
    f.text(400, 30, "Chapter 20 at a glance", size=22, weight="700")
    cols = [("What readers look for", ["20.1 Competencies and evidence", "20.2 Labor-market claims",
                                       "20.3 Portfolio Anatomy"]),
            ("Building the evidence", ["20.4 Revision evidence", "20.5 Honest entries", "20.6 Privacy"]),
            ("Presenting it", ["20.7 Narrative · 20.8 Defense", "20.9 Workshop, A14 and the portfolio"])]
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
    xs = [205, 315, 435, 560, 690]
    for i, step in enumerate(LOOP):
        if step == "Disclose":
            f.box(xs[i] - 55, y - 20, 110, 40, step, role="highlight", kind="human", size=15)
        elif step == "Verify":
            f.text(xs[i], y, "Verify", size=15, weight="700")
            f.text(xs[i], y + 20, "(second)", size=13, italic=True, color=muted)
        else:
            f.text(xs[i], y, step, size=14, color=muted)
        if i < 4:
            f.text((xs[i] + xs[i + 1]) / 2, y, "→", size=14, color=muted)
    f.text(400, 420, "This chapter strengthens Disclose (say what the AI did and what you did, to a reader outside "
           "the course), then Verify: every claim in a portfolio points to a check.", size=13, color=muted,
           width=780)
    f.text(400, 452, "Opening case: an AI company's rules for its own job applicants (2025)", size=13, color=muted)


# ---------------------------------------------------------------- F20.2 Storyboard (C29)
def storyboard(f):
    muted = MUTED[f.mode]
    top = [("Feb 2025", "Job postings ask applicants not to use AI assistants in the application", True),
           ("May 2025", "The rule reported again", True),
           ("Jul 10, 2025", "The company publishes guidance by hiring stage", False),
           ("Jul 21, 2025", "Fortune quotes the head of talent's LinkedIn post: the approach is intentional", True)]
    xs = [20, 215, 410, 605]
    for i, (when, what, rep) in enumerate(top):
        role = "verified" if not rep else "neutral"
        f.text(xs[i] + 87, 70, when, size=14, weight="700")
        f.box(xs[i], 84, 175, 96, what, role=role, kind="step", dashed=rep, size=13, weight="normal")
        if i < 3:
            f.arrow(xs[i] + 177, 132, xs[i + 1] - 2, 132)
    f.text(400, 30, "From \"no AI\" to \"your first draft, AI to refine, none in live interviews\"", size=16,
           weight="700", width=780)
    stages = [("Application materials", "write your own first draft, then refine; never invent experience"),
              ("Take-home tasks", "no AI unless the company says it is allowed"),
              ("Live interviews", "no AI unless the company indicates otherwise")]
    for j, (lab, sub) in enumerate(stages):
        x = 40 + j * 250
        f.box(x, 250, 225, 100, lab, role="verified", kind="step", size=14, sub=sub, sub_size=13)
        f.arrow(497, 182, x + 112, 248, curve=0)
    f.text(400, 382, "Solid = the company's own page · dashed = reported in news coverage (Fortune, 2025)",
           size=13, color=muted, width=780)


# ---------------------------------------------------------------- F20.4 LO × NACE map (A14 brief)
NACE = ["Career and self-development", "Communication", "Critical thinking", "Equity and inclusion",
        "Leadership", "Professionalism", "Teamwork", "Technology"]
LOS = ["LO1", "LO2", "LO3", "LO4", "LO5", "LO6", "LO7"]
MAPCELLS = {
    ("Career and self-development", "LO4"): "A4", ("Career and self-development", "LO7"): "A1, A14",
    ("Communication", "LO2"): "A3", ("Communication", "LO4"): "A7", ("Communication", "LO6"): "A13",
    ("Communication", "LO7"): "A14",
    ("Critical thinking", "LO1"): "A2", ("Critical thinking", "LO2"): "A3", ("Critical thinking", "LO3"): "A5, A6, A9",
    ("Equity and inclusion", "LO5"): "A12",
    ("Leadership", "LO5"): "A11", ("Leadership", "LO6"): "A13",
    ("Professionalism", "LO4"): "A7", ("Professionalism", "LO5"): "A12",
    ("Teamwork", "LO2"): "A3 (swap)", ("Teamwork", "LO6"): "A13 (peer test)",
    ("Technology", "LO1"): "A2", ("Technology", "LO2"): "A10", ("Technology", "LO5"): "A10, A12",
}


def lo_nace_map(f):
    muted, ink = MUTED[f.mode], INK[f.mode]
    f.text(400, 24, "Each course outcome gives evidence for at least one NACE competency", size=16, weight="700")
    x0, y0, cw, rh, lw = 230, 70, 79, 40, 220
    for j, lo in enumerate(LOS):
        f.text(x0 + j * cw + cw / 2, y0 - 14, lo, size=14, weight="700")
    for i, comp in enumerate(NACE):
        y = y0 + i * rh
        f.text(x0 - 10, y + rh / 2, comp, size=13, anchor="end", weight="600")
        f.line(x0 - lw + 8, y, x0 + 7 * cw, y, color=muted, width=0.8)
        for j, lo in enumerate(LOS):
            val = MAPCELLS.get((comp, lo))
            if val:
                f.text(x0 + j * cw + cw / 2, y + rh / 2, val, size=13, weight="700", color=ink, width=cw - 4)
    f.line(x0 - lw + 8, y0 + 8 * rh, x0 + 7 * cw, y0 + 8 * rh, color=muted, width=0.8)
    for j in range(8):
        f.line(x0 + j * cw, y0, x0 + j * cw, y0 + 8 * rh, color=muted, width=0.8)
    f.text(400, y0 + 8 * rh + 26, "Cells name the artifacts (A1–A14) that can give that evidence. The book's "
           "mapping, not NACE's; NACE lists equity and inclusion as under review (October 2026).",
           size=13, color=muted, width=780)


# ---------------------------------------------------------------- F20.6 Anatomy of a labor-market claim
def claim_anatomy(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "A labor-market number is a forecast by named respondents at a date", size=16, weight="700")
    f.box(270, 176, 260, 84, "\"170 million new jobs by 2030\"", role="soft", kind="step", size=15,
          sub="the number as you met it", sub_size=13)
    top = [(10, "Who said it?", "the WEF, from employers' 2024 answers"),
           (207, "Whom did they ask?", "over 1,000 employers, not workers"),
           (404, "When?", "survey May–September 2024"),
           (601, "What caused it?", "all trends combined, not AI alone")]
    for x, lab, sub in top:
        f.box(x, 56, 189, 92, lab, role="neutral", kind="human", size=14, sub=sub, sub_size=13)
        f.arrow(x + 95, 150, 400 + (x + 95 - 400) * 0.4, 174)
    bot = [(110, "What was measured?", "expectations and plans, not outcomes"),
           (305, "Forecast or count?", "an estimate for 2025–2030"),
           (500, "Gross or net?", "gross; 92 million displaced, net 78 million")]
    for x, lab, sub in bot:
        f.box(x, 300, 190, 92, lab, role="neutral", kind="human", size=14, sub=sub, sub_size=13)
        f.arrow(x + 95, 298, 400 + (x + 95 - 400) * 0.4, 262)
    f.text(400, 420, "Rounded = a question you ask · rectangle = the claim. Answers from WEF (2025), pp. 5, 25, 97.",
           size=13, color=muted)


# ---------------------------------------------------------------- F20.8 Lucía's evidence map
LUCIA_ROWS = [
    ("A1", "LO4, LO7", "Career and self-development", "Baseline: AI for speed; two goals", "as is"),
    ("A5", "LO3", "Critical thinking", "Six claims sorted; three contradicted", "as is"),
    ("A9", "LO3, LO5", "Critical thinking", "Two unlogged shifts reversed the result", "volunteer names removed"),
    ("A11", "LO2, LO5", "Technology", "Review step: queue, weekly sample, pause rule", "described only; permission recorded"),
    ("A12", "LO5", "Professionalism", "Five risks rated; owners where needed", "described only; permission recorded"),
    ("A13", "LO6", "Communication", "Reconciliation practice; peer-tested", "classmate's inputs replaced"),
]


def lucia_map(f):
    muted, ink = MUTED[f.mode], INK[f.mode]
    f.text(400, 24, "Lucía's map: which competency each entry shows, and where the proof is", size=16,
           weight="700")
    heads = ["Artifact", "Outcome", "NACE competency", "Evidence (one line)", "Privacy status"]
    xs = [20, 95, 185, 385, 640]
    ws = [70, 85, 195, 250, 140]
    y0, rh = 56, 46
    for x, w, h in zip(xs, ws, heads):
        f.text(x + 4, y0 + 14, h, size=13, weight="700", anchor="start")
    for i, row in enumerate(LUCIA_ROWS):
        y = y0 + 30 + i * rh
        f.line(20, y, 780, y, color=muted, width=0.8)
        for k, (x, w, val) in enumerate(zip(xs, ws, row)):
            f.text(x + 4, y + rh / 2, val, size=13, anchor="start", weight="700" if k == 0 else "normal",
                   color=ink, width=w - 8)
    f.line(20, y0 + 30 + 6 * rh, 780, y0 + 30 + 6 * rh, color=muted, width=0.8)
    f.text(400, y0 + 30 + 6 * rh + 24, "Constructed example. A3 stays as supporting evidence; A10 is left out "
           "because two rows used her employer's ticket categories.", size=13, color=muted, width=780)


# ---------------------------------------------------------------- F20.10 Revision entry (Lucía's A5)
def revision_entry(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "A revision entry keeps the original and records why it changed", size=16, weight="700")
    rows = [("Before (as submitted)", "Claim 3, \"75 to pass\": supported, 75%. No source named.", "soft"),
            ("After", "Supported: the exam's FAQ page and the state board's scoring page. 75 is a scaled score "
                      "on a 0–99 scale, not a percentage correct. Checked October 2026.", "neutral"),
            ("What changed", "Corrected (the unit) and strengthened (a named source)", "neutral"),
            ("Why", "Instructor feedback: \"Which page says 75?\"", "neutral"),
            ("Trail", "Two rows: the FAQ page and the board's page, with dates; uncertainty: rules change", "verified")]
    y = 52
    for lab, txt, role in rows:
        f.box(20, y, 190, 60, lab, role="neutral", kind="human", size=14)
        f.box(222, y, 558, 60, txt, role=role, kind="step", size=13, weight="normal")
        y += 72
    f.text(400, y + 10, "Constructed example (Lucía's A5, Chapter 8). Rounded = the entry's fields · rectangle = "
           "what she wrote", size=13, color=muted, width=780)


# ---------------------------------------------------------------- F20.11 Entry anatomy
def entry_anatomy(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "An honest entry puts the AI's part and your part side by side", size=16, weight="700")
    f.box(200, 50, 400, 60, "Situation and task", role="neutral", kind="step", size=15,
          sub="what had to be done, for whom", sub_size=13)
    f.box(60, 150, 300, 90, "What the AI did", role="ai", kind="ai", size=15,
          sub="the tool produced: totals and a recommendation", sub_size=13)
    f.box(440, 150, 300, 90, "What you did", role="neutral", kind="human", size=15,
          sub="you checked every row against the sign-in sheets", sub_size=13)
    f.box(200, 280, 400, 56, "How you checked", role="verified", kind="step", size=15,
          sub="an independent check you can name", sub_size=13)
    f.box(60, 370, 300, 56, "Result", role="neutral", kind="step", size=15, sub="what happened, with numbers",
          sub_size=13)
    f.box(440, 370, 300, 56, "Limit", role="neutral", kind="step", size=15, sub="what you could not check",
          sub_size=13)
    f.arrow(320, 112, 230, 148)
    f.arrow(480, 112, 570, 148)
    f.arrow(210, 242, 330, 278)
    f.arrow(590, 242, 470, 278)
    f.arrow(330, 338, 230, 368)
    f.arrow(470, 338, 570, 368)
    f.text(400, 456, "Hexagon = AI · rounded = you · rectangle = a record. Example: Lucía's A9 entry (constructed).",
           size=13, color=muted, width=780)


# ---------------------------------------------------------------- F20.13 Privacy check
def privacy_check(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "Every item passes a data-class check again for its new readers", size=16, weight="700")
    f.box(300, 46, 200, 50, "An item for your portfolio", role="neutral", kind="step", size=14)
    f.arrow(400, 98, 400, 118)
    f.box(300, 120, 200, 110, "Whose information is in it?", role="neutral", kind="decision", size=14)
    f.arrow(502, 175, 588, 175, label="only yours", label_dy=-12, size=13)
    f.box(590, 140, 190, 70, "Keep it", role="verified", kind="step", size=14, sub="check its data class anyway",
          sub_size=13)
    f.arrow(298, 175, 212, 175, label="protected", label_dy=-12, size=13)
    f.box(20, 132, 190, 86, "Remove it", role="risk", kind="step", size=14,
          sub="patients', participants' or clients' confidential data", sub_size=13)
    f.arrow(400, 232, 400, 268)
    f.text(412, 250, "classmates', an employer's, or a client's work", size=13, italic=True, color=muted, anchor="start")
    f.box(300, 270, 200, 110, "Written permission from its owner?", role="neutral", kind="decision", size=13)
    f.arrow(502, 325, 588, 325, label="yes", label_dy=-12, size=13)
    f.box(590, 290, 190, 70, "Keep, permission noted", role="verified", kind="step", size=14)
    f.arrow(400, 382, 400, 412)
    f.text(412, 396, "no", size=13, italic=True, color=muted, anchor="start")
    f.box(270, 414, 260, 70, "Replace with placeholders, or describe the method only", role="neutral", kind="step",
          size=13)
    f.text(400, 512, "Data classes from Chapter 12. Diamond = a decision · rectangle = an action · thick or hatched "
           "border = remove", size=13, color=muted, width=780)


# ---------------------------------------------------------------- F20.14 Narrative structure
def narrative(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "Every claim in a narrative points to an artifact", size=16, weight="700")
    f.box(250, 50, 300, 60, "One named reader", role="neutral", kind="human", size=15,
          sub="a recruiter at an accounting firm", sub_size=13)
    claims = [("Claim 1", "I check before I send"), ("Claim 2", "I find the hidden assumption"),
              ("Claim 3", "I design a review step")]
    ents = ["A5 entry", "A9 entry", "A11 and A12 entries"]
    for i, ((lab, sub), e) in enumerate(zip(claims, ents)):
        x = 30 + i * 255
        f.box(x, 150, 230, 70, lab, role="neutral", kind="step", size=14, sub=sub, sub_size=13)
        f.box(x, 260, 230, 56, e, role="verified", kind="step", size=14)
        f.arrow(x + 115, 222, x + 115, 258)
        f.arrow(400, 112, x + 115, 148)
    f.box(250, 356, 300, 56, "What I am learning next", role="neutral", kind="human", size=14,
          sub="the CPA path", sub_size=13)
    f.text(400, 440, "Lucía's narrative (constructed). Rounded = her own words · rectangle = a claim or its evidence",
           size=13, color=muted, width=780)


# ---------------------------------------------------------------- F20.15 Defense timeline
def defense_timeline(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "In five minutes, show one decision chain and answer from your evidence", size=16,
           weight="700")
    x0, scale = 30, 144  # px per minute
    segs = [(0, 0.5, "Narrative sentence", "neutral"), (0.5, 2.0, "One entry as a decision chain", "neutral"),
            (2.0, 3.0, "One revision and its check", "neutral"), (3.0, 5.0, "Questions (2 minutes)", "soft")]
    for a, b, lab, role in segs:
        f.box(x0 + a * scale, 80, (b - a) * scale - 4, 70, lab, role=role, kind="human" if role == "soft" else "step",
              size=13)
    for m in range(6):
        f.line(x0 + m * scale, 158, x0 + m * scale, 170, width=1.4)
        f.text(x0 + m * scale, 184, f"{m}:00", size=13)
    f.text(400, 222, "No AI tool and no script; one index card and your portfolio open. A time limit, not a pace.", size=13, color=muted)


# ---------------------------------------------------------------- F20.16 Decision chain
def decision_chain(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "\"What did the AI do and what did you do?\" has a five-link answer", size=16, weight="700")
    links = [("You asked for", "the task and frame", "human"),
             ("The AI produced", "a draft, totals, a suggestion", "ai"),
             ("You kept, changed or rejected", "and why", "decision"),
             ("You checked", "how, against what", "step"),
             ("Who decided", "you, or the decision owner", "human")]
    x = 14
    for i, (lab, sub, kind) in enumerate(links):
        role = "ai" if kind == "ai" else ("verified" if kind == "step" else "neutral")
        w = 136
        h = 110 if kind == "decision" else 90
        y = 60 if kind == "decision" else 70
        f.box(x, y, w, h, lab, role=role, kind=kind, size=13, sub=None if kind == "decision" else sub, sub_size=13)
        if kind == "decision":
            f.text(x + w / 2, 186, sub, size=13, italic=True, color=muted)
        if i < 4:
            f.arrow(x + w + 2, 115, x + w + 20, 115)
        x += w + 22
    f.text(400, 216, "Hexagon = AI · diamond = your decision · rounded = a person · rectangle = a check", size=13,
           color=muted)


# ---------------------------------------------------------------- F20.17 A14 sheet
def a14_sheet(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "Your A14 sheet: map, entry, narrative, declaration", size=16, weight="700")
    parts = [("1 · Evidence map (at least 6 rows)", "artifact · outcome · competency and a behavior in your words "
              "· what you revised and why · where the trail is · privacy status or permission recorded"),
             ("2 · One portfolio entry (80–100 words)", "situation and task · what you did · what the AI did · "
              "how you checked · result · limit"),
             ("3 · Career narrative (150–200 words)", "one reader named by role · three claims, each pointing to a map row · "
              "one change after peer review, noted"),
             ("4 · AI Use Declaration and judgment", "tools · purpose · accepted, rejected or revised · how verified · "
              "your judgment (or \"no AI tools used\") · one sentence on a choice you made, and why")]
    y = 50
    for lab, sub in parts:
        f.box(30, y, 740, 84, lab, role="neutral", kind="step", size=15, sub=sub, sub_size=13)
        y += 96
    f.text(400, y + 8, "Due with the portfolio, Wed Apr 28, 11:59 p.m. Bring drafts of parts 1–3 to Tuesday's workshop.",
           size=13, color=muted)


# ---------------------------------------------------------------- F20.18 Employer rules by stage (C29)
RULES = [
    ("Anthropic (company page, July 2025)", False,
     ["Your own first draft; AI to refine; never invent experience", "No AI unless the company says it is allowed",
      "No AI in live interviews unless indicated"]),
    ("Amazon (reported, Feb 2025)", True,
     [None, None, "Generative AI in interviews may disqualify, unless explicitly permitted"]),
    ("Goldman Sachs (reported, June 2025)", True,
     [None, None, "Interviews (HireVue): no outside sources, incl. ChatGPT; all campus applicants"]),
]


def employer_rules(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "All three employers' rules, as published or reported, keep AI tools out of interviews", size=16,
           weight="700", width=780)
    heads = ["Application materials", "Take-home tasks", "Interviews"]
    x0, cw, y0, rh = 200, 196, 70, 104
    for j, h in enumerate(heads):
        f.text(x0 + j * cw + cw / 2, y0 - 14, h, size=14, weight="700")
    for i, (name, rep, cells) in enumerate(RULES):
        y = y0 + i * rh
        f.text(x0 - 10, y + rh / 2 - 4, name, size=13, weight="700", anchor="end", width=170)
        for j, c in enumerate(cells):
            if c is None:
                f.box(x0 + j * cw + 4, y + 6, cw - 10, rh - 14, "no rule reported", role="soft", kind="step",
                      size=13, weight="normal")
            else:
                f.box(x0 + j * cw + 4, y + 6, cw - 10, rh - 14, c, role="neutral", kind="step", dashed=rep,
                      size=13, weight="normal")
    f.text(400, y0 + 3 * rh + 22, "Solid = the company's own page · dashed = reported in news coverage · light fill "
           "with label = no rule reported. Three firms only: not evidence of what employers in general do.", size=13, color=muted, width=780)


# ---------------------------------------------------------------- F20.19 How the WEF numbers are made (Deep)
def wef_method(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "The WEF's job numbers scale employers' answers up to about 1.2 billion jobs", size=16,
           weight="700", width=780)
    steps = [("Survey answers", "over 1,000 employers, May–September 2024"),
             ("Expected % changes", "per role and industry, 2025–2030"),
             ("Jobs data", "ILO employee counts: about 1.18 billion in covered roles"),
             ("Millions of jobs", "170 created · 92 displaced"),
             ("Net and churn", "net 78 million (7%) · churn 22% · all trends, not AI alone")]
    x = 14
    for i, (lab, sub) in enumerate(steps):
        f.box(x, 66, 144, 124, lab, role="neutral", kind="step", size=14, sub=sub, sub_size=13)
        if i < 4:
            f.arrow(x + 146, 125, x + 158, 125)
        x += 158
    f.text(400, 214, "Each step adds an assumption: who answered (large firms), how roles are matched, which jobs are covered.",
           size=13, color=muted, width=780)


FIGS = [
    ("f20-01-chapter-map", chapter_map, 800, 470, "Chapter 20 at a glance"),
    ("f20-02-storyboard", storyboard, 800, 400, "From no AI to your first draft, AI to refine, none in interviews"),
    ("f20-04-lo-nace-map", lo_nace_map, 800, 440, "Each course outcome gives evidence for at least one NACE competency"),
    ("f20-06-claim-anatomy", claim_anatomy, 800, 430, "A labor-market number is a forecast by named respondents at a date"),
    ("f20-07-portfolio-anatomy", portfolio_anatomy(), 800, PORTFOLIO_H, "Portfolio Anatomy"),
    ("f20-08-lucia-map", lucia_map, 800, 400, "Lucía's evidence map"),
    ("f20-09-revision-evidence", portfolio_anatomy(highlight=["artifact", "trace", "verification"]), 800, PORTFOLIO_H,
     "Revision evidence: the before, the after, the reason and the check"),
    ("f20-10-revision-entry", revision_entry, 800, 440, "A revision entry keeps the original and records why it changed"),
    ("f20-11-entry-anatomy", entry_anatomy, 800, 470, "An honest entry puts the AI's part and your part side by side"),
    ("f20-12-spectrum", voice_spectrum(highlight=[1, 2], band="own",
                                       note="Career narrative: your words only or AI as reader (this chapter's advice)"),
     800, spectrum_height(note=True), "Portfolio prose belongs near your words only"),
    ("f20-13-privacy-check", privacy_check, 800, 530, "Every item passes a data-class check again for its new readers"),
    ("f20-14-narrative", narrative, 800, 456, "Every claim in a narrative points to an artifact"),
    ("f20-15-defense-timeline", defense_timeline, 800, 240, "In five minutes, show one decision chain"),
    ("f20-16-decision-chain", decision_chain, 800, 232, "The five-link answer"),
    ("f20-17-a14-sheet", a14_sheet, 800, 450, "Your A14 sheet"),
    ("f20-18-employer-rules", employer_rules, 800, 420, "All three employers' rules keep AI tools out of interviews"),
    ("f20-19-wef-method", wef_method, 800, 232, "How the WEF numbers are made"),
    ("f20-20-summary-card", portfolio_anatomy(note="Narrative 20.7 · map 20.1, 20.3 · entries 20.4–20.6 · "
                                                    "reflection 20.3 · code Chapter 21 · defense 20.8"),
     800, PORTFOLIO_H + 14, "Chapter 20 summary card"),
]

if __name__ == "__main__":
    only = set(sys.argv[1:])
    for fid, fn, w, h, title in FIGS:
        if only and fid not in only:
            continue
        render(fid, fn, w, h, title, ROOT)
        print("rendered", fid)
