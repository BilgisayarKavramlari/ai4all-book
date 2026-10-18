"""Chapter 11 diagrams (SVG, color + gray). Run from the repo root:
    python3 figures/scripts/ch11_figures.py [figure-id ...]
Data charts are in ch11_charts.py (data/ch11_*.csv).

New reusable drawings introduced here (for Chapters 14, 16, 17 and 19):
    proxy_trap(meant, measured, wedge, decision, where=None, note=None, questions=True)
        # the book-map figure "Proxy-variable trap"
    decision_roles(highlight=None, notes=None)      # an AI output informs, recommends or triggers an action
    analysis_audit(highlight=None, center=None)     # six places a hidden choice can change an analysis
    matrix_anatomy(highlight=None)                  # every number in a decision matrix is a choice

Reused, never redrawn: Signature 3 (`from ch02_figures import pipeline`), Signature 8
(`from ch08_figures import verification_funnel, funnel_height`), Signature 5 and the chain
(`from ch04_figures import failure_tree, failure_chain, tree_height`). Signature 11 (Bias Lifecycle) is
introduced in Chapter 16 and is not drawn here.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from figlib import render, MUTED, INK  # noqa: E402
from ch02_figures import pipeline  # noqa: E402
from ch04_figures import failure_tree, failure_chain, tree_height  # noqa: E402
from ch08_figures import verification_funnel, funnel_height  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LOOP = ["Frame", "Prompt", "Verify", "Decide", "Disclose"]


def _set(x):
    if x is None:
        return set()
    if isinstance(x, (str, int)):
        return {x}
    return set(x)


# ---------------------------------------------------------------- proxy_trap (new, reusable)
def proxy_trap(meant, measured, wedge, decision, where=None, note=None, questions=True):
    """The Proxy-variable trap (≤ 7 boxes).

    meant:    (label, sub) what the decision is meant to serve (drawn rounded: a human goal)
    measured: (label, sub) what the data actually record (rectangle)
    wedge:    (label, sub) what separates the two, larger for some people (dashed: the hidden gap)
    decision: (label, sub) what the measure is used to decide
    where:    "the inputs" or "the label": where the proxy sits (printed as a tag)
    note:     one italic line at the bottom (e.g., the case)
    questions: draw the side panel with the three proxy questions
    """
    def draw(f):
        muted = MUTED[f.mode]
        f.text(400, 24, "The proxy-variable trap", size=18, weight="700")
        if where:
            f.text(400, 50, f"Where the proxy sits: {where}", size=14, weight="700")
        w = 480 if questions else 760
        x0 = 20
        bw = 190
        f.box(x0, 80, bw, 96, meant[0], role="human", kind="human", size=15, sub=meant[1], sub_size=13)
        f.box(x0 + w - bw, 80, bw, 96, measured[0], role="neutral", kind="step", size=15, sub=measured[1],
              sub_size=13)
        f.arrow(x0 + w - bw - 3, 128, x0 + bw + 3, 128)
        f.text(x0 + w / 2, 110, "stands in for", size=13, color=muted, italic=True)
        f.box(x0 + 105, 212, w - 210, 88, wedge[0], role="risk", kind="step", dashed=True, thick=True,
              size=15, sub=wedge[1], sub_size=13)
        f.line(x0 + 95, 176, x0 + 130, 212, dashed=True)
        f.line(x0 + w - 95, 176, x0 + w - 130, 212, dashed=True)
        f.box(x0 + w - 230, 336, 230, 84, decision[0], role="neutral", kind="decision", size=14,
              sub=decision[1], sub_size=13)
        f.arrow(x0 + w - 60, 178, x0 + w - 100, 352)
        f.text(x0 + 10, 360, "Prediction can be accurate", size=13, weight="700", anchor="start")
        f.text(x0 + 10, 382, "for the measure and still", size=13, anchor="start")
        f.text(x0 + 10, 402, "wrong for the goal", size=13, anchor="start")
        if questions:
            qx = 530
            f.box(qx, 80, 250, 340, "", role="soft", kind="human")
            f.text(qx + 125, 110, "Three questions", size=15, weight="700")
            qs = ["1. What do we mean?", "2. What do we measure?", "3. For whom is the gap bigger?"]
            for i, q in enumerate(qs):
                f.text(qx + 18, 170 + i * 66, q, size=14, weight="600", anchor="start", width=220)
            f.text(qx + 125, 384, "Ask them of every criterion", size=13, color=muted, italic=True, width=220)
        if note:
            f.text(400, 458, note, size=13, color=muted, italic=True, width=780)
        f.text(400, 500, "Rounded = the goal people care about · rectangle = what is recorded · dashed, thick "
               "(hatched in print) = the hidden gap · diamond = the decision", size=13, color=muted, width=780)
    return draw


OBERMEYER_TRAP = proxy_trap(("Health need", "how sick a patient is"),
                            ("Next year's cost", "what was spent on care"),
                            ("Unequal access to care", "less is spent on Black patients with the same need"),
                            ("Who is flagged", "for a care program"),
                            where="the label (Chapter 2's proxies sat in the inputs)",
                            note="Obermeyer et al. (2019): race was excluded from the inputs; the gap entered "
                                 "through the label. Chapter 16 places this on the Bias Lifecycle.")


# ---------------------------------------------------------------- decision_roles (new, reusable)
ROLES3 = [("informs", "Informs", "a person reads it among other evidence", "neutral"),
          ("recommends", "Recommends", "a person decides whether to follow it", "neutral"),
          ("triggers", "Triggers an action", "no person in between: an automated decision", "risk")]


def decision_roles(highlight=None, notes=None, title="One output, three roles"):
    """An AI output informs, recommends or triggers an action (7 boxes).

    highlight: role keys ("informs", "recommends", "triggers") to mark with a thick border.
    notes:     {role key: one short line} printed under that role (an example).
    """
    hl, notes = _set(highlight), notes or {}

    def draw(f):
        muted = MUTED[f.mode]
        f.text(400, 24, title, size=18, weight="700")
        f.box(290, 50, 220, 60, "An AI output", role="ai", kind="ai", size=15,
              sub="a score, an analysis, a draft", sub_size=13)
        for i, (k, lab, sub, role) in enumerate(ROLES3):
            x = 22 + i * 256
            f.arrow(400, 112, x + 120, 150)
            f.box(x, 152, 240, 92, lab, role=role if k == "triggers" else "neutral", kind="step",
                  thick=k in hl, size=15, sub=sub, sub_size=13)
            if k != "triggers":
                f.arrow(x + 120, 246, x + 120, 282)
                f.box(x + 10, 284, 220, 62, "The decision owner", role="human", kind="human", size=14,
                      sub="decides; answers for it", sub_size=13)
            else:
                f.arrow(x + 120, 246, x + 120, 282)
                f.box(x + 10, 284, 220, 62, "The action happens", role="neutral", kind="step", dashed=True,
                      size=14, sub="answered for afterward", sub_size=13)
            if k in notes:
                f.text(x + 120, 378, notes[k], size=13, weight="600", width=236)
        f.text(400, 430, "Hexagon = AI output · rounded = a person · risk fill (hatched in print) = no person in "
               "between · thick border = a role this example shows", size=13, color=muted, width=780)
    return draw


OBERMEYER_ROLES = decision_roles(
    highlight={"recommends", "triggers"},
    notes={"informs": "e.g., a summary of the patient's record",
           "recommends": "Above the 55th percentile: the doctor is prompted to consider enrollment",
           "triggers": "Above the 97th percentile: flagged for enrollment by the score alone"},
    title="The same score flagged some patients by itself and only advised a doctor about others")


# ---------------------------------------------------------------- F11.4 what you can inspect
def inspect(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "What you can inspect depends on how the AI took part", size=18, weight="700")
    f.box(300, 48, 200, 54, "Your question and data", role="human", kind="human", size=14)
    paths = [("AI feature in a spreadsheet", "fills cells or writes a formula", "The formula",
              "read it; test it on two rows by hand"),
             ("Chat tool that runs code", "writes and runs code on a file you give it", "The code, if you ask",
              "count rows in and out; read each step"),
             ("Chat answer", "produces text about the data or the decision", "Nothing but the answer",
              "recalculate everything you rely on")]
    for i, (h, s, ins, chk) in enumerate(paths):
        x = 20 + i * 262
        f.arrow(400, 104, x + 120, 140)
        f.box(x, 142, 240, 86, h, role="ai", kind="ai", size=14, sub=s, sub_size=13)
        f.arrow(x + 120, 230, x + 120, 262)
        f.box(x, 264, 240, 62, "You can inspect:", role="verified" if i < 2 else "soft", kind="step",
              dashed=(i == 2), size=13, sub=ins, sub_size=14)
        f.text(x + 120, 360, chk, size=13, weight="600", width=236)
    f.text(400, 410, "Chapter 12 names the kinds of tools and compares them; current features are in Compass.",
           size=13, color=muted, italic=True, width=780)
    f.text(400, 436, "Hexagon = AI component · rounded = a person · dashed = little to inspect", size=13,
           color=muted)


# ---------------------------------------------------------------- analysis_audit (new, reusable)
CHECKS = [("rows", "1. Rows in, rows out", "how many records did it use?"),
          ("blanks", "2. Blanks and odd values", "how were they handled? any impossible ones?"),
          ("units", "3. Definitions and units", "net or gross? $ or $000? dates as dates?"),
          ("time", "4. Time window", "does the period match the decision?"),
          ("groups", "5. Totals vs. groups", "does the pattern hold inside each group?"),
          ("code", "6. Formula or code", "show it, read it, rerun it")]


def analysis_audit(highlight=None, center="An AI-generated analysis"):
    """Six places a hidden choice can change an analysis (7 boxes)."""
    hl = _set(highlight)

    def draw(f):
        muted = MUTED[f.mode]
        f.text(400, 24, "Six places a hidden choice can change the answer", size=18, weight="700")
        f.box(290, 196, 220, 74, center, role="ai", kind="ai", size=15, sub="check outside the tool",
              sub_size=13)
        pos = [(20, 56), (290, 56), (560, 56), (20, 330), (290, 330), (560, 330)]
        for (k, lab, sub), (x, y) in zip(CHECKS, pos):
            on = k in hl
            f.box(x, y, 220, 86, lab, role="highlight" if on else "neutral", kind="step", thick=on, size=15,
                  sub=sub, sub_size=13)
            cx = x + 110
            if y < 100:
                f.line(cx, y + 88, 400 if cx == 400 else (330 if cx < 400 else 470), 194, dashed=True)
            else:
                f.line(cx, y - 2, 400 if cx == 400 else (330 if cx < 400 else 470), 272, dashed=True)
        f.text(400, 448, "Each checked number gets a verdict (Chapter 8's scale); the analysis gets a line of "
               "remaining uncertainty.", size=13, color=muted, width=780)
        f.text(400, 474, "Hexagon = AI output · thick dark border = the check an example uses", size=13,
               color=muted)
    return draw


# ---------------------------------------------------------------- matrix_anatomy (new, reusable)
def matrix_anatomy(f):
    muted, ink = MUTED[f.mode], INK[f.mode]
    f.text(400, 24, "Every number in a decision matrix is a choice someone made", size=18, weight="700")
    gx, gy = 110, 64
    cols = ["Skills test", "Interview", "Experience", "Total"]
    weights = ["25", "25", "30", ""]
    rows = [("A", ["88", "4.5", "1 yr", "5.59"]), ("C", ["91", "blank", "2 yrs", "3.83"]),
            ("E", ["65", "3.0", "8 yrs", "7.00"])]
    cw, rh = 100, 46

    def tag(x, y, n):
        f.raw(f'<circle cx="{x}" cy="{y}" r="11" fill="#FFFFFF" stroke="{ink}" stroke-width="1.6"/>')
        f.text(x, y, str(n), size=13, weight="700")

    f.text(gx - 14, gy + 33, "Weight", size=13, weight="700", anchor="end")
    for j, c in enumerate(cols):
        x = gx + j * cw
        f.raw(f'<rect x="{x}" y="{gy}" width="{cw}" height="{rh}" fill="none" stroke="{ink}" stroke-width="1.2"/>')
        f.text(x + cw / 2, gy + 14, c, size=13, weight="700")
        if weights[j]:
            f.text(x + cw / 2, gy + 33, weights[j], size=13)
    for i, (name, vals) in enumerate(rows):
        y = gy + rh * (i + 1)
        f.text(gx - 20, y + rh / 2, name, size=14, weight="700")
        for j, v in enumerate(vals):
            x = gx + j * cw
            blank = v == "blank"
            dash = ' stroke-dasharray="6 4"' if blank else ""
            f.raw(f'<rect x="{x}" y="{y}" width="{cw}" height="{rh}" fill="none" stroke="{ink}" '
                  f'stroke-width="{2.6 if blank else 1.2}"{dash}/>')
            f.text(x + cw / 2, y + rh / 2, v, size=14, weight="700" if j == 3 else "normal", italic=blank)
    tag(gx + 2 * cw + cw / 2, gy - 14, 1)          # criterion
    tag(gx + 2 * cw + cw / 2 + 30, gy + 33, 2)     # weight
    tag(gx + cw + cw - 14, gy + rh * 2 + 14, 3)   # blank
    tag(gx + 3 * cw + cw - 14, gy + rh * 3 + 14, 6)   # total / reason
    calls = [(540, 60, "1  Criterion: a proxy?", "experience stands in for skill"),
             (540, 146, "2  Weight: a judgment", "even equal weights are a choice"),
             (540, 232, "3  Blank: scored how?", "C's interview was not yet held"),
             (20, 330, "4  Scale: what counts as 10?", "fixed ranges or best-to-worst"),
             (280, 330, "5  Margin: how close?", "E leads B by 0.06 of 10"),
             (540, 330, "6  Reason: who decides?", "the owner, with reasons on record")]
    for x, y, h, s in calls:
        f.box(x, y, 240, 72, h, role="soft", kind="human", size=14, sub=s, sub_size=13)
    f.text(400, 432, "Constructed internship shortlist from section 11.5 (three of six candidates shown; "
           "totals on a 0–10 scale).", size=13, color=muted, italic=True, width=780)
    f.text(400, 458, "Numbered circles point to the cells each note describes · dashed cell with thick border = "
           "a blank · rounded = a judgment someone made", size=13, color=muted, width=780)


# ---------------------------------------------------------------- F11.1 Chapter map
def chapter_map(f):
    muted = MUTED[f.mode]
    f.text(400, 30, "Chapter 11 at a glance", size=22, weight="700")
    cols = [("Hidden assumptions", ["11.1 Decision support", "11.2 A blank is a decision",
                                    "11.3 Measure vs. meaning"]),
            ("Checking and deciding", ["11.4 Check an AI analysis", "11.5 Decision matrices",
                                       "11.6 Human judgment"]),
            ("Practice", ["11.7 Lab 11.1 and A9 (Studio)", "Labs 11.2–11.4 (optional)",
                          "Case Study: a health algorithm"])]
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
    xs = [205, 300, 420, 540, 640]
    for i, step in enumerate(LOOP):
        if step == "Decide":
            f.box(xs[i] - 50, y - 20, 100, 40, step, role="highlight", kind="human", thick=True, size=15)
        elif step == "Verify":
            f.box(xs[i] - 50, y - 17, 100, 34, step, role="neutral", kind="human", dashed=True, size=14)
        else:
            f.text(xs[i], y, step, size=14, color=muted)
        if i < 4:
            f.text((xs[i] + xs[i + 1]) / 2 + (8 if i == 1 else 0), y, "→", size=14, color=muted)
    f.text(400, 410, "This chapter strengthens Decide (who owns the decision, and what can an analysis settle?), "
           "then Verify (dashed): recalculate what the decision depends on.", size=13, color=muted, width=780)
    f.text(400, 446, "Opening case: a health algorithm that never received race (Obermeyer et al., 2019)", size=13,
           color=muted)


# ---------------------------------------------------------------- F11.2 storyboard
def storyboard(f):
    muted, ink = MUTED[f.mode], INK[f.mode]
    ev = [("2013–2015", "Scores and health records from one academic hospital (article)", "neutral", "step"),
          ("Analysis", "Researchers compare scores with health; no contact with the maker (article)",
           "neutral", "human"),
          ("Before publication", "The maker replicates the finding on 3.7 million patients (authors' report)",
           "neutral", "step"),
          ("Oct 25, 2019", "Article published in Science (confirmed)", "verified", "step"),
          ("Oct 25, 2019", "New York regulators write to the maker's parent company (confirmed)", "neutral",
           "human"),
          ("Next step", "A health-and-cost label: 84% less bias by one measure (authors' report)",
           "verified", "step")]
    f.line(24, 230, 776, 230, color=ink, width=2.4)
    for i, (d, txt, role, kind) in enumerate(ev):
        x = 14 + i * 129
        y = 34 if i % 2 == 0 else 252
        h = 176
        f.box(x, y, 122, h, "", role=role, kind=kind)
        tc = "#FFFFFF" if (role == "human") else INK[f.mode]
        f.text(x + 61, y + 24, d, size=14, weight="700", width=112, color=tc)
        f.text(x + 61, y + 104, txt, size=13, width=110, color=tc)
        cx = x + 61
        f.line(cx, y + h if i % 2 == 0 else y, cx, 230, color=ink, width=1.4)
        f.raw(f'<circle cx="{cx}" cy="230" r="5" fill="{ink}"/>')
    f.text(400, 462, "Rounded = a person's or an agency's action · green = a published result · article = in the "
           "primary record; authors' report = what the authors state they were told or found", size=13,
           color=muted, width=780)
    f.text(400, 502, "Sources: Obermeyer et al. (2019); NYDFS & NYSDOH (2019). The product's name and the maker's "
           "response are reported in the news; what changed for patients is not on record.", size=13,
           color=muted, italic=True, width=780)


# ---------------------------------------------------------------- F11.14 is matrix_anatomy; F11.18 A9 sheet
def a9_sheet(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "Your audit records the evidence behind every number in the matrix", size=18, weight="700")
    rows = [("1. Decision", "statement · owner · who is affected · reversible?", "human"),
            ("2. AI-drafted matrix", "tool · model · date · prompt", "ai"),
            ("3. Criteria audit", "meant · measured · proxy, for whom? · blanks: can you get the real value?",
             "step"),
            ("4. Recalculation", "top two totals outside the tool · verdict for each", "step"),
            ("5. Two sensitivity tests", "a weight · a blank or criterion → new top, margin, shortlist", "step"),
            ("6. Revised matrix and memo", "recommendation · reasons · review step · what the matrix misses",
             "human"),
            ("7–8. Uncertainty and declaration", "what you could not check · the five declaration elements",
             "step")]
    for i, (h, s, kind) in enumerate(rows):
        y = 48 + i * 58
        role = "ai" if kind == "ai" else ("soft" if kind == "human" else "neutral")
        f.box(30, y, 740, 50, "", role=role, kind="ai" if kind == "ai" else ("human" if kind == "human" else "step"),
              dashed=(i == 6))
        f.text(50, y + 25, h, size=14, weight="700", anchor="start")
        f.text(310, y + 25, s, size=13, anchor="start", width=450)
    f.text(400, 470, "Hexagon = AI output · rounded = your decisions · dashed = what remains uncertain", size=13,
           color=muted)


# ---------------------------------------------------------------- F11.21 summary card
def summary_card(f):
    f.text(400, 26, "Chapter 11 — what you can do now", size=18, weight="700")
    cards = ["Distinguish: informs, recommends, triggers; name the owner",
             "Test a blank: count, ask why, get the real value, then compare",
             "Evaluate a proxy: mean? measure? for whom is the gap bigger?",
             "Verify an analysis: six places; recalculate outside the tool",
             "Stress-test a matrix: margins and shortlists, not only the top",
             "Design a review step that makes disagreement possible"]
    for i, c in enumerate(cards):
        x = 20 + (i % 3) * 258
        y = 50 + (i // 3) * 150
        f.box(x, y, 242, 130, c, role="neutral" if i % 2 else "soft", kind="human", size=14, weight="600")


# ---------------------------------------------------------------- F11.22 why values go missing (Deep)
def mechanisms(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "Why a value is missing decides which fix is safe", size=18, weight="700")
    m = [("Missing completely at random", "MCAR", "a page of the sign-in sheet got wet",
          "deletion loses data but does not tilt the answer"),
         ("Missing at random, given what you know", "MAR", "evening shifts were logged less often, and you know "
          "which shifts were evenings", "a fill that uses the known pattern can work"),
         ("Missing not at random", "MNAR", "the longest shifts went unlogged because they were long",
          "every simple fix can mislead: get the real value")]
    for i, (h, ab, ex, fix) in enumerate(m):
        y = 52 + i * 128
        f.box(20, y, 240, 110, h, role="neutral", kind="step", dashed=(i == 2), thick=(i == 2), size=15,
              sub=ab, sub_size=14)
        f.arrow(262, y + 55, 290, y + 55)
        f.box(292, y, 230, 110, "Example from Lucía's log", role="soft", kind="step", size=13, sub=ex,
              sub_size=13)
        f.arrow(524, y + 55, 552, y + 55)
        f.box(554, y, 226, 110, "What it means", role="verified" if i < 2 else "risk", kind="human", size=13,
              sub=fix, sub_size=13)
    f.text(400, 448, "After Rubin (1976). Dashed, thick = the case where no fill method is safe. Examples are "
           "constructed.", size=13, color=muted, width=780)


# ---------------------------------------------------------------- reused signatures
PIPELINE_LABEL = pipeline((1,), {1: "Label: next year's cost, standing in for health need"})
FUNNEL_ANALYSIS = verification_funnel(highlight="check", tag="An AI-generated analysis",
                                      notes={"check": "Recalculate from the raw data; read the formula or code"})
OBERMEYER_TREE = failure_tree({"bias"}, tag="Case: Obermeyer et al. (2019) · bias, leaf skewed recommendations, "
                              "documented", note="The article measured lower scores for Black patients at equal health")
OBERMEYER_CHAIN = failure_chain(
    notes={0: "Lower scores at equal health (article)",
           1: "Judged on cost accuracy; doctors fixed little",
           2: "Top 3% flagged by the score alone",
           3: "Fewer Black patients flagged (simulated)"},
    highlight={1}, dashed={3},
    tag="Stage 4 is inferred: an estimate from the authors' simulation, with no record of harm to individuals")

FIGS = [
    ("f11-01-chapter-map", chapter_map, 800, 465, "Chapter 11 at a glance"),
    ("f11-02-storyboard", storyboard, 800, 526,
     "The bias came to light only when researchers compared scores with health records"),
    ("f11-03-decision-roles", OBERMEYER_ROLES, 800, 450,
     "The same score flagged some patients by itself and only advised a doctor about others"),
    ("f11-04-inspect", inspect, 800, 450, "What you can inspect depends on how the AI took part"),
    ("f11-07-pipeline-label", PIPELINE_LABEL, 800, 390,
     "The bias entered at the label: the algorithm predicted cost, not need"),
    ("f11-08-proxy-trap", OBERMEYER_TRAP, 800, 530,
     "A proxy fails where the gap between it and the goal differs across groups"),
    ("f11-11-funnel-analysis", FUNNEL_ANALYSIS, 800, funnel_height(tag=True),
     "Checking an AI analysis starts with your own recalculation"),
    ("f11-12-analysis-audit", analysis_audit(), 800, 490, "Six places a hidden choice can change the answer"),
    ("f11-14-matrix-anatomy", matrix_anatomy, 800, 470, "Every number in a decision matrix is a choice someone made"),
    ("f11-18-a9-sheet", a9_sheet, 800, 486, "Your audit records the evidence behind every number in the matrix"),
    ("f11-19-tree-obermeyer", OBERMEYER_TREE, 800, tree_height() + 34, "Obermeyer on the tree: bias, documented"),
    ("f11-20-chain-obermeyer", OBERMEYER_CHAIN, 800, 420,
     "The check measured cost accuracy, not need, and the harm is an estimate"),
    ("f11-21-summary-card", summary_card, 800, 340, "Chapter 11 summary card"),
    ("f11-22-mechanisms", mechanisms, 800, 466, "Why a value is missing decides which fix is safe"),
]

if __name__ == "__main__":
    only = set(sys.argv[1:])
    for fid, fn, w, h, title in FIGS:
        if only and fid not in only:
            continue
        render(fid, fn, w, h, title, ROOT)
        print("rendered", fid)
