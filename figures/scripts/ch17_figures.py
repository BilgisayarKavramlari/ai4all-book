"""Chapter 17 diagrams (SVG, color + gray). Run from the repo root:
    python3 figures/scripts/ch17_figures.py
Data charts (F17.8, F17.10, F17.11, F17.13) are in ch17_charts.py (data/ch17_*.csv).

New signature introduced here (book map: "Black box -> explanation layers"); Chapters 18 and 19 import it:

    from ch17_figures import explanation_layers, layers_height
    explanation_layers(highlight=None, missing=None, partly=None, inferred=None, notes=None, note=None,
                       title=None, audiences=True)

  7 boxes: the model (a solid hexagon: inputs in, output out, workings not visible) and six layers, each phrased
  as the question it answers: "notice", "documentation", "global", "local", "change", "contest" (LAYERS).
  Layer states, never by color alone:
    present (default) = light fill, solid border
    missing  = an empty (white) box, with "missing" in its label
    partly   = a dotted fill, with "partly" in its label
    inferred = a dashed border (dashed is reserved for "inferred", the book's reading, as in every figure)
    highlight = a thick border (this figure's focus)
  audiences=True prints each layer's default audience at the right; notes={layer: text} replaces it.
  The legend says "layers, not steps": a decision can need any of them, in any order.

Reused, never redrawn: Signature 1 strip (chapter map), Signature 5 and the chain (`from ch04_figures import
failure_tree, failure_chain, tree_height`), Signature 8 (`from ch08_figures import verification_funnel,
funnel_height`), Signature 10 (`from ch15_figures import risk_heat_map, HEAT_H`), Signature 11
(`from ch16_figures import bias_lifecycle, lifecycle_height`), decision roles (`from ch11_figures import
decision_roles`). No figure contains generated imagery or a real person's likeness.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from figlib import render, MUTED, INK, ROLES  # noqa: E402
from ch04_figures import failure_tree, failure_chain, tree_height  # noqa: E402
from ch08_figures import verification_funnel, funnel_height  # noqa: E402
from ch11_figures import decision_roles  # noqa: E402
from ch15_figures import risk_heat_map, HEAT_H  # noqa: E402
from ch16_figures import bias_lifecycle, lifecycle_height  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LOOP = ["Frame", "Prompt", "Verify", "Decide", "Disclose"]


def _set(x):
    if x is None:
        return set()
    if isinstance(x, str):
        return {x}
    return set(x)


# ---------------------------------------------------------------- Signature: explanation layers (new, reusable)
LAYERS = ["notice", "documentation", "global", "local", "change", "contest"]
LAYER_TEXT = {
    "notice": ("1. Notice", "Was an AI system used in this decision?"),
    "documentation": ("2. Documentation", "Purpose, data, tests and known limits?"),
    "global": ("3. Global logic", "What drives its outputs overall?"),
    "local": ("4. Local reasons", "Why this output for this case?"),
    "change": ("5. What would change it", "What would give a different result?"),
    "contest": ("6. Contest", "Who can review and change it, and how?"),
}
AUDIENCE = {
    "notice": "the people affected; the public",
    "documentation": "deployers, auditors, journalists",
    "global": "builders, oversight bodies",
    "local": "the reviewer; the person affected",
    "change": "the person affected",
    "contest": "the person affected, and a reviewer with power to change it",
}
LY0, LSTEP, LH = 66, 64, 54


def layers_height(note=None):
    return 520 + (22 if note else 0)


def explanation_layers(highlight=None, missing=None, partly=None, inferred=None, notes=None, note=None,
                       title=None, audiences=True):
    hl, ms, pt, inf = _set(highlight), _set(missing), _set(partly), _set(inferred)
    notes = notes or {}
    for s in (hl, ms, pt, inf, set(notes)):
        if s - set(LAYERS):
            raise ValueError(f"unknown layer: {s - set(LAYERS)}")
    if ms & pt:
        raise ValueError("a layer cannot be both missing and partly present")

    def draw(f):
        ink, muted = INK[f.mode], MUTED[f.mode]
        f.text(400, 24, title or "Black box → explanation layers", size=17, weight="700", width=780)
        y0 = LY0 + (22 if note else 0)
        if note:
            f.text(400, 48, note, size=13, color=muted, italic=True, width=770)
        # the model: solid hexagon (a known component; its workings are what is not visible)
        hy = y0 + 2 * LSTEP + LH / 2 - 70
        f.box(18, hy, 150, 140, "The model", role="ai", kind="ai", size=15,
              sub="inputs in, output out; workings not visible", sub_size=13)
        f.raw('<defs><pattern id="partly-dots" patternUnits="userSpaceOnUse" width="9" height="9">'
              '<rect width="9" height="9" fill="#FFFFFF"/><circle cx="4.5" cy="4.5" r="1.3" fill="#8A8A8A"/>'
              '</pattern></defs>')
        x, w = 198, 352
        for i, key in enumerate(LAYERS):
            y = y0 + i * LSTEP
            lab, q = LAYER_TEXT[key]
            if key in ms:
                lab += " — missing"
            elif key in pt:
                lab += " — partly"
            kind = "human" if key == "contest" else "step"
            role = "soft"
            if key in ms or key in pt:
                role = "neutral"
            f.box(x, y, w, LH, lab, role=role, kind=kind, thick=(key in hl), dashed=(key in inf),
                  size=14, sub=q, sub_size=13)
            if key in pt:
                # dotted fill drawn as a frame inside the border, leaving the text area readable
                rx = 16 if kind == "human" else 3
                f.raw(f'<rect x="{x + 4}" y="{y + 4}" width="{w - 8}" height="{LH - 8}" rx="{rx}" '
                      f'fill="none" stroke="url(#partly-dots)" stroke-width="7"/>')
            f.line(170, hy + 70, x - 4, y + LH / 2, color=muted, width=1.0)
            right = notes.get(key) or (AUDIENCE[key] if audiences else None)
            if right:
                f.text(x + w + 12, y + LH / 2, right, size=13, anchor="start", color=ink if key in notes else muted,
                       weight="600" if key in notes else "normal", width=226)
        if audiences and not notes:
            f.text(x + w + 12, y0 - 14, "Who usually asks", size=13, anchor="start", weight="700")
        ly = y0 + 6 * LSTEP + 14
        f.text(400, ly, "Layers, not steps: a decision can need any of them, in any order.", size=13, weight="600")
        f.text(400, ly + 24, "Hexagon = AI model · light fill = present · empty box with \"missing\" = missing · "
               "dotted frame with \"partly\" = partly present", size=13, color=muted, width=790)
        f.text(400, ly + 46, "Rounded = a person · thick border = this figure's focus · dashed border = inferred "
               "(the book's reading)", size=13, color=muted, width=790)
    return draw


# ---------------------------------------------------------------- F17.1 Chapter map
def chapter_map(f):
    muted = MUTED[f.mode]
    f.text(400, 30, "Chapter 17 at a glance (optional chapter)", size=22, weight="700")
    cols = [("Why and what", ["17.1 Who needs an explanation", "17.2 Black box, glass box",
                              "17.3 What attributions show"]),
            ("Testing explanations", ["17.4 What would change it", "17.5 Plausible is not faithful",
                                      "17.6 When a model explains itself"]),
            ("Rights and practice", ["17.7 Documents and contest", "17.8 Explain a decision (Studio)",
                                     "Case Study: the benefits case"])]
    fast = {(0, 0), (2, 1)}
    for c, (head, items) in enumerate(cols):
        x = 30 + c * 255
        f.text(x + 115, 74, head, size=16, weight="700")
        for i, it in enumerate(items):
            on = (c, i) in fast
            role = "verified" if on else ("neutral" if c < 2 else "soft")
            kind = "human" if c == 2 else "step"
            f.box(x, 94 + i * 88, 230, 70, it, role=role, kind=kind, thick=on, size=14)
        if c < 2:
            f.arrow(x + 236, 217, x + 252, 217)
    y = 372
    f.text(150, y, "AI Work Loop:", size=14, weight="700", anchor="end")
    xs = [200, 290, 405, 530, 650]
    for i, step in enumerate(LOOP):
        if step == "Disclose":
            f.box(xs[i] - 52, y - 20, 104, 40, step, role="highlight", kind="human", thick=True, size=15)
        elif step == "Verify":
            f.box(xs[i] - 62, y - 17, 124, 34, "Verify (second)", role="neutral", kind="human", size=14)
        else:
            f.text(xs[i], y, step, size=14, color=muted)
        if i < 4:
            ax = {0: 245, 1: 330, 2: 476, 3: 584}[i]
            f.text(ax, y, "→", size=14, color=muted)
    f.text(400, 410, "Disclose: what people affected are told. Verify (second): is the explanation true of the "
           "system?", size=13, color=muted, width=790)
    f.text(400, 436, "Thick boxes = the fast route, with the Opening Case and Summary · Opening case: Dutch "
           "childcare benefits", size=13, color=muted, width=790)


# ---------------------------------------------------------------- F17.2 storyboard (attribution tiers)
def storyboard(f):
    ink, muted = INK[f.mode], MUTED[f.mode]
    ev = [("2013", "model in use for checks (confirmed: AP)", True),
          ("2016–18", "citizenship indicator in the model (confirmed: AP)", True),
          ("July 2020", "data protection authority report (confirmed)", True),
          ("Dec 2020", "parliamentary inquiry report (confirmed)", True),
          ("Jan 2021", "the cabinet resigns (reported: Amnesty, citing press)", False),
          ("Oct 2021", "Amnesty's report (reported tier)", False)]
    f.text(400, 24, "Seven years passed between the model's first use and the official finding on what it used",
           size=16, weight="700", width=780)
    f.text(400, 50, "The 2013 start and the 2016–2018 period are in the AP's report (2020, pp. 14, 50); the seven years "
           "are this book's arithmetic", size=13, color=muted, italic=True, width=780)
    f.line(24, 236, 776, 236, color=ink, width=2.4)
    for i, (d, txt, conf) in enumerate(ev):
        x = 22 + i * 128
        up = i % 2 == 0
        y = 76 if up else 258
        f.box(x, y, 116, 140, d, role="verified" if conf else "neutral", kind="human" if conf else "step",
              size=15, sub=txt, sub_size=13)
        cx = x + 58
        f.line(cx, 216 if up else 258, cx, 236, color=ink, width=1.4)
        f.raw(f'<circle cx="{cx}" cy="236" r="5" fill="{ink}"/>')
    f.text(400, 428, "Rounded, filled = confirmed by a primary record (the AP or the parliamentary inquiry) · "
           "rectangles = reported by a named source · no inferred items", size=13, color=muted, width=780)
    f.text(400, 460, "Sources: Autoriteit Persoonsgegevens (2020); Parlementaire ondervragingscommissie "
           "Kinderopvangtoeslag (2020); Amnesty International (2021).", size=13,
           color=muted, italic=True, width=780)


# ---------------------------------------------------------------- F17.6 glass box vs black box
def glass_black(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "A post-hoc explanation studies a model from outside; an interpretable model is its own "
           "explanation", size=16, weight="700", width=780)
    f.text(200, 70, "Interpretable model (glass box)", size=15, weight="700")
    f.box(40, 92, 320, 70, "A scorecard or a rule list", role="ai", kind="ai", size=14,
          sub="you can read it directly", sub_size=13)
    f.arrow(200, 164, 200, 200)
    f.box(60, 202, 280, 60, "The explanation is the model itself", role="verified", kind="step", size=14)
    f.text(600, 70, "Black box + post-hoc explanation", size=15, weight="700")
    f.box(440, 92, 320, 70, "A complex model", role="ai", kind="ai", size=14,
          sub="inputs and outputs visible; workings not", sub_size=13)
    f.arrow(600, 164, 600, 200)
    f.text(612, 182, "inputs tried, outputs recorded", size=13, color=muted, italic=True, anchor="start")
    f.box(450, 202, 300, 70, "An explanation method run afterward", role="neutral", kind="step", size=14,
          sub="occlusion, attribution, a surrogate model, a counterfactual search", sub_size=13)
    f.arrow(600, 274, 600, 306)
    f.box(450, 308, 300, 60, "An explanation of the model, with its own error", role="neutral", kind="step",
          size=14)
    f.text(400, 404, "Hexagon = AI model · rectangle = a step or a product · filled = needs no separate check of "
           "its faithfulness", size=13, color=muted, width=780)
    f.text(400, 428, "Rudin (2019) argues for the left column whenever a high-stakes decision allows it.", size=13,
           color=muted, italic=True)


# ---------------------------------------------------------------- F17.7 global vs local
def global_local(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "A global explanation describes the model's overall pattern; a local one, a single decision",
           size=16, weight="700", width=780)
    f.text(200, 66, "Global", size=16, weight="700")
    f.box(40, 84, 320, 62, "Many cases", role="neutral", kind="step", size=14, sub="the whole test set",
          sub_size=13)
    f.arrow(200, 148, 200, 178)
    f.box(40, 180, 320, 70, "The model", role="ai", kind="ai", size=14)
    f.arrow(200, 252, 200, 282)
    f.box(40, 284, 320, 70, "\"Overall, debt ratio and income matter most\"", role="soft", kind="step", size=14,
          sub="who asks: builders, auditors", sub_size=13)
    f.text(600, 66, "Local", size=16, weight="700")
    f.box(440, 84, 320, 62, "One case", role="neutral", kind="step", size=14, sub="this applicant", sub_size=13)
    f.arrow(600, 148, 600, 178)
    f.box(440, 180, 320, 70, "The model", role="ai", kind="ai", size=14)
    f.arrow(600, 252, 600, 282)
    f.box(440, 284, 320, 70, "\"For you, the debt ratio pulled the score down most\"", role="soft", kind="step",
          size=14, sub="who asks: the reviewer, the applicant", sub_size=13)
    f.text(400, 392, "A local explanation can disagree with the global pattern; that disagreement is worth "
           "checking.", size=13, weight="600")
    f.text(400, 418, "Hexagon = AI model · rectangle = input or explanation · constructed example", size=13,
           color=muted)


# ---------------------------------------------------------------- F17.9 counterfactual
def counterfactual(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "A counterfactual helps a person only if it names a change they can make", size=17,
           weight="700", width=780)
    f.box(30, 150, 210, 110, "Not approved", role="neutral", kind="step", size=14,
          sub="income 61.8k · debt ratio 0.285 · 0 late payments · age band 1", sub_size=13)
    f.box(320, 60, 230, 92, "Debt ratio 0.285 → 0.276", role="verified", kind="step", size=14,
          sub="actionable: pay down a little debt", sub_size=13)
    f.box(320, 258, 230, 92, "Age band 1 → 2", role="neutral", kind="step", size=14,
          sub="cannot be changed soon: only by waiting years", sub_size=13)
    f.arrow(242, 186, 318, 112)
    f.arrow(242, 228, 318, 300)
    f.text(200, 124, "smallest change found", size=13, color=muted, italic=True)
    f.text(200, 296, "also flips it", size=13, color=muted, italic=True)
    f.box(610, 60, 170, 92, "Approve (0.51)", role="soft", kind="step", size=14, sub="model output",
          sub_size=13)
    f.box(610, 258, 170, 92, "Approve (0.59)", role="soft", kind="step", size=14,
          sub="true of the model; not advice", sub_size=13)
    f.arrow(552, 106, 608, 106)
    f.arrow(552, 304, 608, 304)
    f.text(400, 392, "Both searches in this book's simulation found the same smallest change: debt ratio down by "
           "0.009. A one-band age change also flips it, at a higher cost.", size=13, weight="600", width=780)
    f.text(400, 420, "Filled = actionable change · numbers are the model's approval probability · constructed data "
           "(data/ch17_counterfactual.csv)", size=13, color=muted, width=780)


# ---------------------------------------------------------------- F17.12 plausible x faithful
def plausible_faithful(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "Plausible and faithful are separate questions", size=18, weight="700")
    f.text(400, 56, "Is it true of the model? (faithful)", size=14, weight="700")
    f.text(285, 82, "yes", size=14, weight="600")
    f.text(555, 82, "no", size=14, weight="600")
    f.text(70, 246, "Does it seem\nright to people?\n(plausible)", size=14, weight="700")
    f.text(140, 161, "yes", size=14, weight="600", anchor="end")
    f.text(140, 311, "no", size=14, weight="600", anchor="end")
    cells = [(150, 96, "Useful", "convincing and true: still check it", "verified", False),
             (420, 96, "Dangerous", "convincing but not what the model did", "risk", True),
             (150, 246, "Easy to dismiss", "true but surprising: often a real finding", "neutral", False),
             (420, 246, "Harmless", "unconvincing and untrue: few rely on it", "soft", False)]
    for x, y, lab, sub, role, thick in cells:
        f.box(x, y, 260, 130, lab, role=role, kind="step", thick=thick, size=15, sub=sub, sub_size=13)
    f.text(400, 410, "Thick border, hatched in print = the cell this chapter warns about · a test, not a feeling, "
           "decides the column", size=13, color=muted, width=780)


# ---------------------------------------------------------------- F17.16 contest route
def contest_route(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "A right to contest needs a person who can change the decision", size=18, weight="700")
    steps = [("Notice", "you learn a system was used", "step", "neutral"),
             ("Ask for reasons", "from the record, in words you can use", "step", "neutral"),
             ("Review by a person", "with power to change it?", "decision", "neutral"),
             ("Correct and remedy", "decision changed; harm repaired", "human", "verified")]
    xs, ws = [16, 206, 404, 618], [168, 172, 188, 170]
    for i, (a, b, kind, role) in enumerate(steps):
        h = 132 if kind == "decision" else 96
        y = 92 if kind == "decision" else 110
        f.box(xs[i], y, ws[i], h, a, role=role, kind=kind, size=14, sub=b, sub_size=13)
        if i < 3:
            f.arrow(xs[i] + ws[i] + 2, 158, xs[i + 1] - 2, 158)
    f.text(603, 140, "yes", size=12, color=muted, italic=True)
    f.arrow(504, 226, 504, 280)
    f.box(370, 282, 268, 72, "A review in form only", role="risk", kind="step", thick=True, size=14,
          sub="no power to change, or no reasons", sub_size=13)
    f.text(516, 252, "no", size=12, color=muted, italic=True, anchor="start")
    f.text(400, 380, "Diamond = a check · rounded = a person · thick border, hatched in print = where a contest "
           "fails in practice", size=13, color=muted, width=780)


# ---------------------------------------------------------------- F17.17 report card
def report_card(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "Your report says what the person is told and where each statement came from", size=17,
           weight="700", width=780)
    rows = [("1. Decision, role, owner", "informs · recommends · triggers; who answers for it", "step", "neutral"),
            ("2. Layer audit", "six layers: present · partly · missing, and where you looked", "step", "neutral"),
            ("3. The explanation (≤ 150 words)", "decision · reasons · what would change it · unknowns · contest",
             "human", "verified"),
            ("4. Faithfulness record", "each statement: rule or record · approximation · self-account", "step",
             "neutral"),
            ("5. Revision", "after reading it aloud as the person affected", "step", "neutral"),
            ("6. Judgment", "what the person still cannot learn, and who should fix it", "step", "neutral"),
            ("7. AI Use Declaration", "tools · purpose · accepted/rejected/revised · how verified",
             "step", "neutral")]
    for i, (a, b, kind, role) in enumerate(rows):
        y = 50 + i * 60
        f.box(60, y, 680, 52, a, role=role, kind=kind, thick=(i == 2), size=14, sub=b, sub_size=13)
    f.text(400, 488, "Rounded, thick = the part the person reads · rectangles = your working record", size=13,
           color=muted)


# ---------------------------------------------------------------- F17.22 summary card
def summary_card(f):
    f.text(400, 24, "Chapter 17 in six cards", size=18, weight="700")
    cards = [("Who asks, and why", "contest · debug · decide how far to rely"),
             ("Layers, not one thing", "notice · documentation · global · local · change · contest"),
             ("Describes the model", "an attribution is not a cause in the world"),
             ("Actionable or not", "a counterfactual helps only if a person can act on it"),
             ("Plausible ≠ faithful", "fidelity, stability, the system's own record"),
             ("A self-account is a claim", "check it; the contest route makes it matter")]
    for i, (a, b) in enumerate(cards):
        x = 20 + (i % 3) * 260
        y = 50 + (i // 3) * 130
        f.box(x, y, 240, 110, a, role="verified" if i == 5 else "neutral", kind="human" if i == 5 else "step",
              size=15, sub=b, sub_size=13)
    f.text(400, 316, "Rounded = what a person can do with an explanation", size=13, color=MUTED[f.mode])


# ---------------------------------------------------------------- reuse instances
LAYERS_INTRO = explanation_layers(
    title="An explanation is not one thing: six layers answer different people's questions")
LAYERS_C14 = explanation_layers(
    missing=["notice", "documentation", "global", "local", "change"], partly=["contest"],
    notes={"notice": "use hidden from the public for years (reported)",
           "documentation": "no public information on the model (reported)",
           "global": "workings not visible to users (reported)",
           "local": "reviewers could not see which indicators drove a score (confirmed: AP)",
           "change": "no basis to say what would change it (reported)",
           "contest": "objection and appeal existed; the inquiry faults courts too (confirmed)"},
    note="Layers 1–3 and 5: reported (Amnesty, 2021); layer 4: confirmed (AP, 2020); contest: the parliamentary inquiry (2020)",
    title="Parents reached none of the first five layers; the contest route failed in practice")
LAYERS_DOCS = explanation_layers(
    highlight=["notice", "documentation"],
    notes={"notice": "a label or notice; an algorithm register entry",
           "documentation": "model card · datasheet · system card",
           "global": "documentation may summarize it",
           "local": "owed to a person on request in some laws (17.7)",
           "change": "one court called it sufficient in a credit case (17.7)",
           "contest": "a named person and a route"},
    title="Each transparency document answers a different reader's question")
ROLES_C14 = decision_roles(
    highlight={"recommends", "triggers"},
    notes={"informs": "(not described in the record)",
           "recommends": "Highest scores: checked by a staff member, who could not see which indicators drove the score (AP)",
           "triggers": "Not selected: processed automatically into a decision (AP)"},
    title="One score approved some applications by itself and sent others to a reviewer")
FUNNEL_SELF = verification_funnel(
    highlight=["claims", "primary"],
    notes={"claims": "the model's account of its own steps",
           "check": "rerun without the hint: does the answer change?",
           "primary": "the system's record: its rule, its logs, a traced computation"},
    note="A model's account of its reasoning is a claim to check, not a record of what the system did")
TREE_C14 = failure_tree({"bias"}, tag="C14 Dutch childcare benefits · bias, documented (official finding: the AP's 2020 report)")
CHAIN_C14 = failure_chain(
    notes={0: "Risk score with a citizenship indicator (confirmed: AP)",
           1: "Reviewer could not see which indicators drove the score (confirmed: AP)",
           2: "High score: payment delayed, evidence requested (confirmed: AP)",
           3: "Investigations, suspended payments, reclaims (reported: Amnesty)"},
    highlight={1},
    tag="Confirmed = the AP's report · reported = Amnesty (2021) · opacity is not a tree branch: it disabled "
        "link 2 (the book's reading)")
LIFECYCLE_C14 = bias_lifecycle(
    highlight=["data", "use"], dashed=["feedback"],
    notes={"data": "historic correct and incorrect applications; citizenship indicator",
           "model": "a \"self-learning\" risk model (the office's description, per the AP)",
           "use": "reviewer could not see which indicators drove a score (AP)",
           "feedback": "decisions as new examples? (the book's reading)"},
    tag="C14 on the lifecycle · the AP finding enters at data; the missing reasons fail at use",
    note="Placement only; Chapter 16 teaches how bias is measured")
HEAT_SAM = risk_heat_map(
    risks=[(1, 2, 2, "I")], moves={1: (1, 2)},
    title="Sam's transparency risk before and after quoting the club's written rule",
    note="1 = members told an AI summary \"explains\" their score (constructed). Reduce: quote the rule and the "
         "officers' notes; avoid: no AI-written reasons. Inferred: no pooled test on the club's tool.")

FIGS = [
    ("f17-01-chapter-map", chapter_map, 800, 455, "Chapter 17 at a glance"),
    ("f17-02-storyboard", storyboard, 800, 480,
     "Seven years passed between the model's first use and the official finding on what it used"),
    ("f17-03-layers", LAYERS_INTRO, 800, layers_height(),
     "An explanation is not one thing: six layers answer different people's questions"),
    ("f17-04-layers-c14", LAYERS_C14, 800, layers_height(note=True),
     "Parents reached none of the first five layers; the contest route failed in practice"),
    ("f17-05-roles-c14", ROLES_C14, 800, 450,
     "One score approved some applications by itself and sent others to a reviewer"),
    ("f17-06-glass-black", glass_black, 800, 446,
     "A post-hoc explanation studies a model from outside; an interpretable model is its own explanation"),
    ("f17-07-global-local", global_local, 800, 436,
     "A global explanation describes the model's overall pattern; a local one, a single decision"),
    ("f17-09-counterfactual", counterfactual, 800, 440,
     "A counterfactual helps a person only if it names a change they can make"),
    ("f17-12-plausible-faithful", plausible_faithful, 800, 430, "Plausible and faithful are separate questions"),
    ("f17-14-funnel-self-account", FUNNEL_SELF, 800, funnel_height(note=True),
     "A model's account of its reasoning is a claim to check, not a record"),
    ("f17-15-documents", LAYERS_DOCS, 800, layers_height(),
     "Each transparency document answers a different reader's question"),
    ("f17-16-contest-route", contest_route, 800, 400,
     "A right to contest needs a person who can change the decision"),
    ("f17-17-report-card", report_card, 800, 505,
     "Your report says what the person is told and where each statement came from"),
    ("f17-18-tree-c14", TREE_C14, 800, tree_height() + 24,
     "The benefits model on the tree: bias, documented by an official finding"),
    ("f17-19-chain-c14", CHAIN_C14, 800, 420,
     "The reviewer's check could not work because the reviewer was shown no reasons"),
    ("f17-20-lifecycle-c14", LIFECYCLE_C14, 800, lifecycle_height() + 24,
     "The citizenship indicator entered at the data phase; the missing reasons failed at the use phase"),
    ("f17-21-heat-sam", HEAT_SAM, 800, HEAT_H,
     "Sam's transparency risk before and after quoting the club's written rule"),
    ("f17-22-summary-card", summary_card, 800, 340, "Chapter 17 summary card"),
]

if __name__ == "__main__":
    only = set(sys.argv[1:])
    for fid, fn, w, h, title in FIGS:
        if only and fid not in only:
            continue
        render(fid, fn, w, h, title, ROOT)
        print("rendered", fid)
