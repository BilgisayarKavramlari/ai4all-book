"""Chapter 19 diagrams (SVG, color + gray). Run from the repo root:
    python3 figures/scripts/ch19_figures.py
Data charts (F19.5 Ithaca; F19.21 Deep) are in ch19_charts.py.

New reusable drawing introduced here (book-map figure "Discipline x use heat map", renamed so it is not
confused with Chapter 15's Risk Heat Map):

    from ch19_figures import discipline_use_map, USE_MAP_H
    discipline_use_map(highlight=None, note=None, cells=None, rows=None)

  Reads data/ch19_use_map.csv (field, use, level 1-4, label, reason, guide). Each cell shows the default
  people point for a student's coursework in that field (Chapter 14's scale): 1 log review, 2 check point,
  3 approval gate, 4 keep with a person. Meaning is carried by a drawn symbol AND a word AND a fill pattern
  (none, dots, hatching, solid), never by color alone.
  Only the four uses whose defaults differ by field are drawn; the two uses that are the same in every field
  (summarizing sources = check point; advising or deciding about people = keep with a person) are printed as
  one line under the map.
  highlight: a field name, a use key ("draft", "data", "code", "media"), a (field, use) tuple, or a list.
  cells:     {(field, use): level} overrides (Chapters 20-21: a student's own row).
  rows:      list of field names to draw (default: all seven).

Reused, never redrawn: Signature 1 (work loop strip in the chapter map), Signature 5 and the chain
(ch04_figures), Signature 8 (ch08_figures.verification_funnel), fit_matrix (ch12_figures), Signature 9
(ch14_figures.agent_loop, whose soft gate is a hatched diamond), data_flow_map (ch15_figures).
Chapter 18's regulation_map (ch18_figures) is reused for Marcus's rules; the "rules nearest first" list is a
separate figure, because the Regulation Map shows kinds of rules, not a reading order.
"""
import csv
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from figlib import render, MUTED, INK  # noqa: E402
from ch04_figures import failure_tree, failure_chain, tree_height  # noqa: E402
from ch08_figures import verification_funnel, funnel_height  # noqa: E402
from ch12_figures import fit_matrix, fit_matrix_height  # noqa: E402
from ch14_figures import agent_loop, LOOP_H  # noqa: E402
from ch15_figures import data_flow_map, FLOW_H  # noqa: E402
from ch18_figures import regulation_map, MAP_H  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LOOP = ["Frame", "Prompt", "Verify", "Decide", "Disclose"]

# ---------------------------------------------------------------- the Discipline x Use Map (new, reusable)
FIELDS = ["Business", "Health", "Arts and humanities", "Social science", "Natural science", "Engineering",
          "Education"]
USES = {"draft": "Drafting and editing text", "sources": "Summarizing and searching sources",
        "data": "Analyzing data", "code": "Writing code or calculations",
        "media": "Making images, audio or video", "people": "Advising or deciding about people"}
DRAWN = ["draft", "data", "code", "media"]
HEAD = {"draft": "Drafting text", "data": "Analyzing data", "code": "Code or calculations",
        "media": "Images, audio, video"}
LEVEL_WORD = {1: "log review", 2: "check point", 3: "approval gate", 4: "keep with a person"}


def _load_map():
    out = {}
    with open(os.path.join(ROOT, "data", "ch19_use_map.csv"), encoding="utf8") as fh:
        for r in csv.DictReader(fh):
            key = next(k for k, v in USES.items() if v == r["use"])
            out[(r["field"], key)] = int(r["level"])
    return out


def _as_list(x):
    if x is None:
        return []
    if isinstance(x, (str, tuple)):
        return [x]
    return list(x)


def use_map_height(rows=None, note=None):
    n = len(rows) if rows else len(FIELDS)
    return 150 + n * 54 + 104 + (44 if note else 0)


USE_MAP_H = use_map_height()


def _glyph(f, x, y, level, color):
    """Draw the level symbol as SVG shapes (no font glyphs): open circle, half circle, diamond, square."""
    if level == 1:
        f.raw(f'<circle cx="{x}" cy="{y}" r="7" fill="#FFFFFF" stroke="{color}" stroke-width="2"/>')
    elif level == 2:
        f.raw(f'<circle cx="{x}" cy="{y}" r="7" fill="#FFFFFF" stroke="{color}" stroke-width="2"/>')
        f.raw(f'<path d="M{x},{y - 7} A7,7 0 0,1 {x},{y + 7} Z" fill="{color}"/>')
    elif level == 3:
        f.raw(f'<polygon points="{x},{y - 8} {x + 8},{y} {x},{y + 8} {x - 8},{y}" fill="#FFFFFF" '
              f'stroke="{color}" stroke-width="2.2"/>')
    else:
        f.raw(f'<rect x="{x - 7}" y="{y - 7}" width="14" height="14" rx="3" fill="{color}" stroke="{color}"/>')


def discipline_use_map(highlight=None, note=None, cells=None, rows=None):
    base = _load_map()
    base.update(cells or {})
    rows = rows or FIELDS
    hl = _as_list(highlight)
    for h in hl:
        if isinstance(h, tuple):
            if h[0] not in rows or h[1] not in DRAWN:
                raise ValueError(f"unknown cell {h}")
        elif h not in rows and h not in DRAWN:
            raise ValueError(f"unknown highlight {h}")

    x0, cw, gap, y0, rh = 206, 142, 6, 112, 54

    def fill(f, level):
        if f.mode == "color":
            return {1: "#FFFFFF", 2: "#E3EAF4", 3: "#9FB6D6", 4: "#1C3D6E"}[level]
        return {1: "#FFFFFF", 2: "url(#dots)", 3: "url(#hatch)", 4: "#2A2A2A"}[level]

    def draw(f):
        ink, muted = INK[f.mode], MUTED[f.mode]
        f.text(400, 26, "Default people point for a student's coursework, by field and use", size=17,
               weight="700")
        f.text(400, 50, "This book's reading, as of October 2026: a starting default, not data. Your field's "
               "rules and your instructor override it.", size=13, italic=True, color=muted, width=780)
        for j, u in enumerate(DRAWN):
            f.text(x0 + j * (cw + gap) + cw / 2, y0 - 22, HEAD[u], size=14, weight="700", width=cw)
        for i, field in enumerate(rows):
            y = y0 + i * rh
            f.text(18, y + rh / 2 - 3, field, size=14, weight="700", anchor="start", width=185)
            for j, u in enumerate(DRAWN):
                lv = base[(field, u)]
                x = x0 + j * (cw + gap)
                thick = (field, u) in hl
                f.raw(f'<rect x="{x}" y="{y}" width="{cw}" height="{rh - 6}" rx="3" fill="{fill(f, lv)}" '
                      f'stroke="{ink}" stroke-width="{3.4 if thick else 1.2}"/>')
                if lv == 4:
                    _glyph(f, x + 18, y + (rh - 6) / 2, lv, "#FFFFFF")
                    f.text(x + 30, y + (rh - 6) / 2, LEVEL_WORD[lv], size=13, weight="700", anchor="start",
                           color="#FFFFFF", width=cw - 34)
                else:
                    f.raw(f'<rect x="{x + 8}" y="{y + 9}" width="{cw - 16}" height="{rh - 24}" rx="9" '
                          f'fill="#FFFFFF" stroke="none"/>')
                    _glyph(f, x + 18, y + (rh - 6) / 2, lv, ink)
                    f.text(x + 30, y + (rh - 6) / 2, LEVEL_WORD[lv], size=13, weight="700", anchor="start",
                           color=ink, width=cw - 34)
            if field in hl:
                f.raw(f'<rect x="12" y="{y - 3}" width="{x0 + 4 * (cw + gap) - 12}" height="{rh}" rx="5" '
                      f'fill="none" stroke="{ink}" stroke-width="3.4"/>')
        for j, u in enumerate(DRAWN):
            if u in hl:
                x = x0 + j * (cw + gap)
                f.raw(f'<rect x="{x - 3}" y="{y0 - 40}" width="{cw + 6}" height="{len(rows) * rh + 40}" rx="5" '
                      f'fill="none" stroke="{ink}" stroke-width="3.4"/>')
        yl = y0 + len(rows) * rh + 18
        f.text(400, yl, "In every field: summarizing and searching sources = check point; advising or deciding "
               "about people = keep with a person.", size=13, weight="600", width=780)
        # legend drawn with the same shapes
        lx = [60, 240, 420, 600]
        for k, lv in enumerate((1, 2, 3, 4)):
            _glyph(f, lx[k], yl + 34, lv, ink)
            f.text(lx[k] + 14, yl + 34, f"{LEVEL_WORD[lv]}", size=13, anchor="start", color=ink)
        f.text(400, yl + 62, "Fill also marks the level: none · dots · hatching · solid. Thick border = highlighted. "
               "Levels follow Chapter 14's rule: can it be undone, and who bears an error?", size=13,
               color=muted, width=780)
        if note:
            f.text(400, yl + 104, note, size=13, italic=True, color=muted, width=780)
    return draw


# ---------------------------------------------------------------- F19.1 Chapter map
def chapter_map(f):
    muted = MUTED[f.mode]
    f.text(400, 30, "Chapter 19 at a glance", size=22, weight="700")
    cols = [("What changes by field", ["19.1 One method, different fields", "19.2 What counts as correct",
                                       "19.3 The data your field protects"]),
            ("From rules to a build", ["19.4 The rules your field writes down", "19.5 From blueprint to prototype",
                                       "19.6 Safeguards and the peer test"]),
            ("Practice", ["19.7 The workflow card; 19.8 Lab 19.1 and A13", "Field guides 19.F1–19.F7",
                          "Case Study: A-Lab (2023–2026)"])]
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
        if step == "Frame":
            f.box(xs[i] - 50, y - 20, 100, 40, step, role="highlight", kind="human", thick=True, size=15)
        elif step == "Disclose":
            f.box(xs[i] - 55, y - 18, 110, 36, "Disclose (2nd)", role="soft", kind="human", thick=True, size=13)
        else:
            f.text(xs[i], y, step, size=14, color=muted)
        if i < 4:
            f.text((xs[i] + xs[i + 1]) / 2 + (6 if i == 3 else 0), y, "→", size=14, color=muted)
    f.text(400, 410, "This chapter strengthens Frame (your field defines the task, what counts as correct, what data "
           "may go in and which rules apply), then Disclose (second): the card says what the workflow is for.",
           size=13, color=muted, width=780)
    f.text(400, 446, "Opening case: Ithaca, experts and a model restoring ancient inscriptions (2022)", size=13,
           color=muted)


# ---------------------------------------------------------------- F19.3 The five-part frame
def frame(f):
    muted = MUTED[f.mode]
    f.box(300, 150, 200, 90, "Your task, in your field", role="highlight", kind="human", size=16)
    parts = [(40, 40, "Typical uses", "your row of the use map"),
             (540, 40, "What to verify", "and who can confirm it"),
             (20, 290, "Data cautions", "the table's floor and your field's records"),
             (300, 300, "Field rules", "nearest first, dated"),
             (580, 290, "Career note", "how employers ask about it")]
    for x, y, lab, sub in parts:
        f.box(x, y, 210, 80, lab, role="neutral", kind="step", size=15, sub=sub, sub_size=13)
    f.arrow(300, 175, 252, 122)
    f.arrow(500, 175, 548, 122)
    f.arrow(300, 225, 232, 290)
    f.arrow(400, 242, 403, 298)
    f.arrow(500, 225, 588, 290)
    f.text(400, 410, "Every field guide (19.F1–19.F7) answers the same five questions, plus one fairness question "
           "and the default people point.", size=13, color=muted, width=760)
    f.text(400, 436, "Rounded = a person · rectangle = a part of the guide", size=13, color=muted)


# ---------------------------------------------------------------- F19.8 Rules, nearest first
def rules_nearest(f):
    muted = MUTED[f.mode]
    f.text(400, 26, "Read the rules nearest you first", size=17, weight="700")
    rows = [("1. Course syllabus and instructor", "declare AI use; drug calculations by hand on exams"),
            ("2. Program or department", "program handbook rules for coursework"),
            ("3. Placement site or employer", "no patient information in any outside tool"),
            ("4. Professional code and licensing board", "privacy and confidentiality duties"),
            ("5. Journals and funders", "authorship and disclosure rules (when you publish)"),
            ("6. Law: federal and state", "HIPAA; Texas TRAIGA (Chapter 18)")]
    for i, (lab, ex) in enumerate(rows):
        y = 52 + i * 62
        w = 330 + i * 26
        kind = "human" if i < 4 else "step"
        f.box(30, y, w, 50, lab, role="highlight" if i == 0 else ("soft" if i < 4 else "neutral"), kind=kind,
              thick=(i == 0), size=14)
        f.text(30 + w + 16, y + 25, ex, size=13, italic=True, color=INK[f.mode], anchor="start",
               width=760 - (30 + w + 16))
    f.arrow(16, 60, 16, 410, width=2)
    f.text(400, 446, "Marcus's list (constructed placement policy, labeled). Rounded = rules people in your "
           "institution or profession write; rectangle = external rules. Dated in the text.",
           size=13, color=muted, width=780)
    f.text(400, 478, "Most rules say who checks, who discloses and what data may go in.", size=13,
           weight="600", color=muted, width=780)


# ---------------------------------------------------------------- F19.9 A11 -> A13
def a11_a13(f):
    muted = MUTED[f.mode]
    f.text(200, 30, "A11: designed on paper", size=15, weight="700")
    f.text(600, 30, "A13: built and tested", size=15, weight="700")
    left = ["Step map", "Action table and people points", "Dry run on paper"]
    right = ["Build: template, chain or configured tool", "Three runs: typical, different, edge",
             "Safeguards built in", "Peer test from another field", "Workflow card and defense"]
    for i, t in enumerate(left):
        f.box(40, 60 + i * 96, 320, 70, t, role="soft", kind="step", size=15)
    for i, t in enumerate(right):
        f.box(440, 56 + i * 64, 320, 52, t, role="verified" if i in (0, 1, 3) else "neutral", kind="step",
              thick=(i in (0, 1, 3)), size=14)
    f.arrow(362, 200, 438, 200, label="may extend", label_dy=-12, size=13)
    f.text(200, 360, "Reused parts are marked \"from A11\" and earn no points unless revised for the build",
           size=13, italic=True, color=muted, width=330)
    f.text(600, 392, "Thick = graded as new work: build, runs, peer test", size=13, italic=True, color=muted,
           width=330)
    f.text(400, 430, "Light fill = reused design · white or green fill = new work in A13", size=13, color=muted)


# ---------------------------------------------------------------- F19.10 Marcus's fit matrix
MARCUS_FIT = fit_matrix(
    parts=["1. Practice questions from a drug table", "2. Answers, closed-book", "3. Marks against the table"],
    options=["Institution's tool", "Consumer tool", "No AI"],
    cells={(0, 0): {"decision": "Use, then check", "rung": "augmentation", "mark": "inside", "state": "chosen"},
           (0, 1): {"decision": "Passes the gate; not chosen", "rung": None, "mark": None, "state": "tested",
                    "note": "training on by default"},
           (0, 2): {"decision": "Write by hand", "rung": "none", "mark": None, "state": "tested",
                    "note": "slower"},
           (1, 0): {"decision": "Not used", "rung": None, "mark": None, "state": "tested",
                    "note": "recall is the point"},
           (1, 2): {"decision": "Answer from memory", "rung": "none", "mark": None, "state": "chosen"},
           (2, 0): {"decision": "Tool marks; he checks every mark", "rung": "augmentation", "mark": "inside",
                    "state": "chosen"},
           (2, 2): {"decision": "Mark by hand", "rung": "none", "mark": None, "state": "tested",
                    "note": "the fallback"}},
    note="Constructed example. Placement material would be blocked in every AI column by his placement rule.")


# ---------------------------------------------------------------- F19.11 Four safeguards
def safeguards(f):
    muted = MUTED[f.mode]
    f.box(300, 160, 200, 90, "Your prototype", role="ai", kind="ai", size=17)
    items = [(40, 40, "Data gate passed", "the table's floor, then your field's rules", "step"),
             (540, 40, "A people point", "hard where an error falls on others", "human"),
             (40, 300, "One field rule applied", "with its source and date", "step"),
             (540, 300, "Fairness check", "a small paired-input test, or why no group cue enters", "step")]
    for x, y, lab, sub, kind in items:
        f.box(x, y, 220, 90, lab, role="neutral", kind=kind, size=15, sub=sub, sub_size=13)
    f.line(262, 120, 312, 170)
    f.line(538, 120, 488, 170)
    f.line(262, 310, 312, 240)
    f.line(538, 310, 488, 240)
    f.text(400, 420, "Hexagon = the AI workflow · rounded = a person acts · rectangle = a check or a rule",
           size=13, color=muted)


# ---------------------------------------------------------------- F19.12 Peer test
def peer_test(f):
    muted = MUTED[f.mode]
    steps = [("Your three runs", "typical, different, edge", "human", "neutral", False),
             ("A peer from another field", "chooses an input within your scope", "human", "neutral", False),
             ("Runs it with only your instructions", "you watch and record", "step", "neutral", False),
             ("Finding: confused here", "or a wrong output", "step", "risk", True),
             ("Revision", "one change, with a reason", "step", "neutral", False),
             ("Rerun", "the input that failed", "step", "verified", False)]
    for i, (lab, sub, kind, role, thick) in enumerate(steps):
        x = 30 + (i % 3) * 255
        y = 50 if i < 3 else 230
        f.box(x, y, 230, 100, lab, role=role, kind=kind, thick=thick, size=15, sub=sub, sub_size=13)
    f.arrow(262, 100, 283, 100)
    f.arrow(517, 100, 538, 100)
    f.arrow(655, 152, 655, 226)
    f.arrow(538, 280, 517, 280)
    f.arrow(283, 280, 262, 280)
    f.text(400, 372, "Thick border = what the peer test is for: a finding you did not see yourself", size=13,
           color=muted)
    f.text(400, 398, "Rounded = a person · rectangle = a step", size=13, color=muted)


# ---------------------------------------------------------------- F19.13 Model card -> workflow card
def card_mapping(f):
    muted, ink = MUTED[f.mode], INK[f.mode]
    f.text(170, 30, "Model card (nine sections)", size=15, weight="700")
    f.text(600, 30, "Workflow card (five fields)", size=15, weight="700")
    groups = [(["Intended use (out-of-scope uses)"], "Not for"),
              (["Intended use"], "For"),
              (["Model details (tool and model used)", "Evaluation data", "Factors"], "Tested on"),
              (["Metrics", "Quantitative analyses"], "Results"),
              (["Training data (what it learned from, if known)", "Ethical considerations",
                "Caveats and recommendations"], "Limits and safeguards")]
    y = 64
    for names, card in groups:
        h = 22 * len(names) + 26
        for k, n in enumerate(names):
            f.text(40, y + 18 + k * 22, "· " + n, size=13, anchor="start", color=ink)
        f.box(500, y, 240, h - 6, card, role="highlight" if card == "Not for" else "neutral", kind="step",
              thick=(card == "Not for"), size=15)
        f.arrow(330, y + h / 2 - 3, 496, y + h / 2 - 3)
        y += h + 10
    f.text(400, y + 18, "Factors and quantitative analyses ask for results by group and condition, not one overall "
           "number (Mitchell et al., 2019). Thick = the field to write first.", size=13, color=muted,
           width=780)


# ---------------------------------------------------------------- F19.14 Marcus's card
def marcus_card(f):
    muted = MUTED[f.mode]
    f.text(400, 26, "Workflow card: pharmacology review (Marcus, constructed)", size=16, weight="700")
    rows = [("Not for", "patient care; real dose calculations; anyone's grades", "highlight"),
            ("For", "my own exam review, from my textbook's drug tables", "neutral"),
            ("Tested on", "3 tables (typical, different, edge) + Hana's peer test; institution's tool, model shown, "
                          "date", "neutral"),
            ("Results", "typical and different: all marks right; edge: one name swap, caught; after revision, all right",
             "neutral"),
            ("Limits and safeguards", "one tool and model; no combination drugs tested; I check every mark; "
                                      "no group cue enters", "neutral")]
    for i, (k, v, role) in enumerate(rows):
        y = 50 + i * 70
        f.box(30, y, 180, 60, k, role=role, kind="step", thick=(i == 0), size=15)
        f.box(220, y, 550, 60, v, role="soft", kind="step", size=14, weight="normal")
    f.text(400, 412, "Thick = the first line a reader sees: what the workflow must not be used for", size=13,
           color=muted)


# ---------------------------------------------------------------- F19.15 A13 sheet
def a13_sheet(f):
    muted = MUTED[f.mode]
    f.text(400, 22, "A13 record (one page)", size=17, weight="700")
    items = ["1. Task and field answers", "2. The build (rerunnable)", "3. Three runs and checks",
             "4. Safeguards table", "5. Peer test", "6. Revision and rerun", "7. Workflow card",
             "8. Defense: one result, one limit", "9. AI Use Declaration"]
    for i, t in enumerate(items):
        x = 30 + (i % 3) * 252
        y = 44 + (i // 3) * 104
        new = i in (1, 2, 4)
        f.box(x, y, 236, 88, t, role="verified" if new else "neutral", kind="step", thick=new, size=15)
    f.text(400, 372, "Thick = the new work A13 is graded on: build, runs, peer test (with checks, safeguards, card "
           "and defense)", size=13, color=muted, width=780)


# ---------------------------------------------------------------- F19.16 A-Lab storyboard
def storyboard(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "C26 A-Lab: claimed, challenged, corrected", size=17, weight="700")
    ev = [("Nov 29, 2023", "Nature paper: \"41 novel compounds\" from 58 targets in 17 days", False, "ai"),
          ("Jan 8, 2024", "Preprint critique: automated analysis not reliable", False, "step"),
          ("Jan 2024", "Public exchange in the press (reported)", True, "step"),
          ("Mar 7, 2024", "Peer-reviewed critique, PRX Energy", False, "step"),
          ("Jan 19, 2026", "Author Correction: 36 of 40 confirmed; \"novel\" dropped", False, "step")]
    for i, (d, t, dashed, kind) in enumerate(ev):
        x = 18 + i * 156
        f.text(x + 70, 62, d, size=13, weight="700")
        f.box(x, 80, 142, 170, t, role="verified" if i == 4 else "neutral", kind="ai" if kind == "ai" else "step",
              dashed=dashed, thick=(i == 4), size=13, weight="600")
        if i < 4:
            f.arrow(x + 144, 165, x + 154, 165)
    f.text(400, 286, "Solid = primary record (paper, critique, correction) · dashed = reported by named outlets · "
           "thick = the correction", size=13, color=muted, width=780)
    f.text(400, 312, "Hexagon = the output of the automated lab and its analysis", size=13, color=muted)


# ---------------------------------------------------------------- F19.17 / F19.18 labels (reuse)
ALAB_TREE = failure_tree(
    highlight={"other"},
    tag="C26 A-Lab (2023–2026) · other: automated identifications not confirmed on expert re-analysis (4 of 40), "
        "documented")
ALAB_CHAIN = failure_chain(
    notes={0: "automated XRD identifications; 4 of 40 not confirmed later", 1: "manual analysis for poor fits; full "
           "re-check after publication (inferred)", 2: "readers and the field rely on the claim",
           3: "no harm beyond a corrected record"},
    highlight=[1], dashed=[1],
    tag="Corrected, not retracted: the authors' Author Correction (2026) after a peer-reviewed critique (2024)")


# ---------------------------------------------------------------- F19.19 Summary card
def summary_card(f):
    f.text(400, 26, "Chapter 19 — what you can do now", size=18, weight="700")
    cards = ["Read your field's row: the use matters more than the field, except where rules raise the floor",
             "Name who can confirm a result in your field",
             "Pass the data gate, then your field's own rules",
             "Find the written rules, nearest first, with dates",
             "Build the smallest prototype; run three inputs",
             "Ask a peer from another field; write the card"]
    for i, c in enumerate(cards):
        x = 20 + (i % 3) * 258
        y = 50 + (i // 3) * 150
        f.box(x, y, 242, 130, c, role="neutral" if i % 2 else "soft", kind="human", size=14, weight="600")


# ---------------------------------------------------------------- reuse figures
HEALTH_ROW = discipline_use_map(highlight="Health",
                                note="Health coursework includes placement work that can reach patients; a practice "
                                     "set that reaches no one is a check point.")
MARCUS_REG = regulation_map(
    highlight=["us_federal", "states", "org"],
    notes={"us_federal": "HIPAA", "states": "TRAIGA; SB 1188", "org": "syllabus, program, placement"},
    note="Marcus (constructed) · as of October 2026 · not legal advice",
    title="Marcus's rules on the Regulation Map")
AUTHORITY = verification_funnel(highlight="expert", notes={"expert": "in your field: who can confirm it?"},
                                note="The expert stage is your field's verification authority (section 19.2).")
MARCUS_FLOW = data_flow_map(
    highlight="input",
    annotate={"input": "textbook tables and his own notes only", "storage": "institutional terms",
              "recipients": "only Marcus"},
    note="Placement data never enters, even without names: the table's floor allows de-identified data, and his "
         "placement rule says no.")
SAM_LOOP = agent_loop(
    highlight=["tool", "check"],
    annotate={"tool": "read one datasheet (read-only)", "check": "Sam compares speed and units with the datasheet",
              "stop": "stop: a value missing or units unclear"},
    note="Sam's A13 build is this one step from his A11 design; cart and order are not part of it (constructed).")

FIGS = [
    ("f19-01-chapter-map", chapter_map, 800, 470, "Chapter 19 at a glance"),
    ("f19-02-use-map", discipline_use_map(), 800, USE_MAP_H,
     "In this book's reading, the use matters more than the field, except where a field's rules raise the floor"),
    ("f19-03-frame", frame, 800, 455, "Every field guide answers the same five questions"),
    ("f19-04-health-row", HEALTH_ROW, 800, use_map_height(note="x"),
     "Health's row: placement work can reach patients, so drafting, data, calculations and media default to "
     "approval gates"),
    ("f19-06-authority", AUTHORITY, 800, funnel_height(note="x"),
     "In your field, someone has the authority to say \"correct\""),
    ("f19-07-marcus-flow", MARCUS_FLOW, 800, FLOW_H,
     "Marcus's input stays on his side: textbook tables in, placement data never"),
    ("f19-08-rules-nearest", rules_nearest, 800, 500,
     "The rules nearest you come first: course, program, placement, then law"),
    ("f19-09-a11-a13", a11_a13, 800, 450,
     "A13 may reuse A11's design; it is graded on what A11 could not show: a build, runs and a peer test"),
    ("f19-10-marcus-fit", MARCUS_FIT, 800, fit_matrix_height(3, note="x"),
     "Each part of Marcus's workflow gets its own decision, and one part stays with no AI"),
    ("f19-11-safeguards", safeguards, 800, 440, "Four safeguards travel with every prototype"),
    ("f19-12-peer-test", peer_test, 800, 415, "A peer from another field finds what the builder's own tests miss"),
    ("f19-13-card-mapping", card_mapping, 800, 530,
     "A workflow card keeps the model card's core: what it is for, what it was tested on, and where it fails"),
    ("f19-14-marcus-card", marcus_card, 800, 430,
     "Marcus's card says what the workflow is not for before it says what works"),
    ("f19-15-a13-sheet", a13_sheet, 800, 390,
     "Your A13 records field answers, the build, the runs, the peer test and the card"),
    ("f19-16-storyboard", storyboard, 800, 330,
     "\"Novel\" was claimed, challenged and corrected through the field's own channels"),
    ("f19-17-tree-c26", ALAB_TREE, 800, tree_height() + 34,
     "C26 on the tree: automated identifications that experts could not confirm, documented by the correction"),
    ("f19-18-chain-c26", ALAB_CHAIN, 800, 420,
     "An expert re-check of every pattern is documented only after publication"),
    ("f19-22-marcus-regmap", MARCUS_REG, 800, MAP_H,
     "Marcus's rules on Chapter 18's Regulation Map: federal and state law, and his organization's rules"),
    ("f19-19-summary-card", summary_card, 800, 340, "Chapter 19 summary card"),
    ("f19-20-sam-loop", SAM_LOOP, 800, LOOP_H,
     "Sam's A13 is one read-only step of his agent, with a check point before anything else builds on it"),
]

if __name__ == "__main__":
    only = set(sys.argv[1:])
    for fid, fn, w, h, title in FIGS:
        if only and fid not in only:
            continue
        render(fid, fn, w, h, title, ROOT)
        print("rendered", fid)
