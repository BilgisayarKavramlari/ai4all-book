"""Chapter 23 diagrams (SVG, color + gray). Run from the repo root:
    python3 figures/scripts/ch23_figures.py
Data charts (Jones & Bergen 2026; Colombatto & Fleming 2024; Doshi & Hauser 2024) are in ch23_charts.py.

New chapter signature (book map: "Argument maps"); later editions or chapters import it:

    from ch23_figures import argument_map, map_height
    argument_map(claim, pros=(), cons=(), highlight=None, note=None, title=None)

  claim : text, or (text, source)
  pros  : up to 4 reasons; each (text, source) or (text, source, "inferred")
  cons  : up to 4 objections; each (text, source), (text, source, "inferred"),
          or a dict {"text":..., "source":..., "inferred": bool, "target": "pro:N"}.
          With target="pro:N" (1-based) the objection ends on the premise it denies; without it, on the claim.
          At most one objection per target.
  highlight : "claim", "pro:N", "con:N" or a list of these (dark fill + a "this section" tag; survives gray).
              Objections are numbered top to bottom as drawn (a targeted objection sits on its premise's row).
  note  : one footer line (default below).
  Boxes: 1 claim + at most 4 + 4 = 9. All boxes are rectangles (rounded = a person in figlib's grammar).
  Side is shown by column, the "+ FOR" / "- AGAINST" tag, and the line end (arrowhead into what it supports,
  flat bar on what it opposes), never by color. Dashed outline and dashed link = inferred only.

Reused, never redrawn: the failure-to-harm chain (`from ch04_figures import failure_chain`) and Signature 8
(`from ch08_figures import verification_funnel, funnel_height`). No figure contains generated imagery or a
real person's likeness. No figure numbers are printed in SVG text (Quarto numbers figures).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from figlib import render, MUTED, INK  # noqa: E402
from ch04_figures import failure_chain  # noqa: E402
from ch08_figures import verification_funnel, funnel_height  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LOOP = ["Frame", "Prompt", "Verify", "Decide", "Disclose"]

DEFAULT_NOTE = "A map shows the structure of an argument, not who is right."
ROW_H, BOX_H = 104, 88
LX, RX, BW = 34, 446, 320          # left column x, right column x, box width
CLAIM_X, CLAIM_W, CLAIM_H = 190, 420, 78


def _item(it):
    """Normalize a pro/con item to a dict."""
    if isinstance(it, dict):
        d = {"text": it["text"], "source": it.get("source", ""), "inferred": bool(it.get("inferred")),
             "target": it.get("target")}
    else:
        it = tuple(it)
        d = {"text": it[0], "source": it[1] if len(it) > 1 else "", "inferred": False, "target": None}
        for extra in it[2:]:
            if extra == "inferred":
                d["inferred"] = True
            elif isinstance(extra, str) and extra.startswith("pro:"):
                d["target"] = extra
    return d


def _hl(highlight):
    if highlight is None:
        return set()
    return {highlight} if isinstance(highlight, str) else set(highlight)


def _layout(pros, cons):
    """Return (rows, con_rows): the number of rows and the row index of each objection."""
    taken, con_rows = {}, []
    for j, c in enumerate(cons):
        if c["target"]:
            k = int(c["target"].split(":")[1]) - 1
            if not 0 <= k < len(pros):
                raise ValueError(f"target {c['target']} has no matching reason")
            if k in taken.values():
                raise ValueError("at most one objection per target premise")
            taken[j] = k
    free = [r for r in range(8) if r not in taken.values()]
    for j in range(len(cons)):
        if j in taken:
            con_rows.append(taken[j])
        else:
            con_rows.append(free.pop(0))
    rows = max([len(pros)] + [r + 1 for r in con_rows]) if (pros or cons) else 0
    return rows, con_rows


def map_height(pros=(), cons=(), title=True):
    p = [_item(x) for x in pros]
    c = [_item(x) for x in cons]
    rows, _ = _layout(p, c)
    return (60 if title else 24) + CLAIM_H + 70 + rows * ROW_H + 70


def argument_map(claim, pros=(), cons=(), highlight=None, note=None, title=None):
    pros = [_item(x) for x in pros]
    cons = [_item(x) for x in cons]
    if len(pros) > 4 or len(cons) > 4:
        raise ValueError("at most 4 reasons and 4 objections (9 boxes)")
    claim_text, claim_src = (claim, "") if isinstance(claim, str) else (claim[0], claim[1])
    hl = _hl(highlight)
    rows, con_rows = _layout(pros, cons)
    note = DEFAULT_NOTE if note is None else note

    def draw(f):
        ink, muted = INK[f.mode], MUTED[f.mode]
        top = 24
        if title:
            f.text(400, 24, title, size=17, weight="700", width=770)
            top = 60
        cy = top
        # claim
        role = "highlight" if "claim" in hl else "soft"
        f.box(CLAIM_X, cy, CLAIM_W, CLAIM_H, "", role=role, kind="step")
        tc = "#FFFFFF" if role == "highlight" else ink
        f.text(CLAIM_X + 12, cy + 14, "CLAIM", size=13, weight="700", anchor="start", color=tc)
        f.text(400, cy + 40, claim_text, size=14, weight="600", width=CLAIM_W - 30, color=tc)
        if claim_src:
            f.text(400, cy + CLAIM_H - 12, claim_src, size=13, italic=True, color=tc)
        if "claim" in hl:
            f.text(CLAIM_X + 70, cy + 14, "▶ this section", size=13, weight="700", anchor="start", color=tc)
        mid = cy + CLAIM_H / 2
        y0 = cy + CLAIM_H + 70
        f.text(LX + BW / 2, y0 - 26, "+ FOR (reasons and premises)", size=14, weight="700")
        f.text(RX + BW / 2, y0 - 26, "− AGAINST (objections)", size=14, weight="700")

        def card(x, y, d, tag, key):
            on = key in hl
            role = "highlight" if on else "neutral"
            f.box(x, y, BW, BOX_H, "", role=role, kind="step", dashed=d["inferred"])
            tcol = "#FFFFFF" if on else ink
            f.text(x + 10, y + 14, tag + ("  (inferred)" if d["inferred"] else "") + ("  ▶ this section" if on else ""),
                   size=13, weight="700", anchor="start", color=tcol)
            f.text(x + BW / 2, y + 46, d["text"], size=13, weight="600", width=BW - 22, color=tcol)
            if d["source"]:
                f.text(x + BW / 2, y + BOX_H - 11, d["source"], size=13, italic=True, color=tcol, width=BW - 16)

        # reasons (left) and a bus on the left margin into the claim's left side
        bus_l = LX - 16
        if pros:
            last = y0 + (len(pros) - 1) * ROW_H + BOX_H / 2
            f.line(bus_l, mid, bus_l, last, color=ink, width=1.6)
            f.arrow(bus_l, mid, CLAIM_X - 2, mid, width=1.8)
        for i, d in enumerate(pros):
            y = y0 + i * ROW_H
            card(LX, y, d, f"+ FOR {i + 1}", f"pro:{i + 1}")
            f.line(bus_l, y + BOX_H / 2, LX, y + BOX_H / 2, dashed=d["inferred"], color=ink, width=1.6)
        # objections (right)
        bus_r = RX + BW + 16
        direct = [j for j, c in enumerate(cons) if not c["target"]]
        if direct:
            last = y0 + max(con_rows[j] for j in direct) * ROW_H + BOX_H / 2
            f.line(bus_r, mid, bus_r, last, color=ink, width=1.6)
            f.line(bus_r, mid, CLAIM_X + CLAIM_W + 10, mid, color=ink, width=1.8)
            bx = CLAIM_X + CLAIM_W + 3  # flat bar on the claim's right side
            f.line(bx, mid - 9, bx, mid + 9, color=ink, width=3)
        rank = {j: n + 1 for n, j in enumerate(sorted(range(len(cons)), key=lambda j: con_rows[j]))}
        for j, d in enumerate(cons):
            y = y0 + con_rows[j] * ROW_H
            card(RX, y, d, f"− AGAINST {rank[j]}", f"con:{rank[j]}")
            yc = y + BOX_H / 2
            if d["target"]:
                f.line(RX, yc, LX + BW + 10, yc, dashed=d["inferred"], color=ink, width=1.8)
                bx = LX + BW + 3
                f.line(bx, yc - 9, bx, yc + 9, color=ink, width=3)
                f.text((LX + BW + RX) / 2 + 3, yc - 12, "denies", size=13, italic=True, color=muted)
            else:
                f.line(RX + BW, yc, bus_r, yc, dashed=d["inferred"], color=ink, width=1.6)
        yl = y0 + rows * ROW_H + 8
        f.text(400, yl, "Arrowhead = supports what it points to · flat bar = opposes it (the claim, or the premise "
               "it denies) · dashed = inferred (the book's reading or an unstated premise)",
               size=13, color=muted, width=770)
        f.text(400, yl + 36, note, size=13, italic=True, color=muted, width=770)
    return draw


# ---------------------------------------------------------------- chapter map
def chapter_map(f):
    muted = MUTED[f.mode]
    f.text(400, 30, "Chapter 23 at a glance (optional chapter)", size=22, weight="700")
    cols = [("Method and minds", ["23.1 Mapping an argument", "23.2 Can a machine understand?",
                                  "23.3 Conscious? Does it matter?"]),
            ("Responsibility and work", ["23.4 The responsibility gap", "23.5 Creativity and authorship",
                                         "23.6 Work and meaning"]),
            ("The long view", ["23.7 AGI and long-term risk", "23.8 Your position (Studio)",
                               "Case Study: three texts"])]
    fast = {(0, 0), (2, 1)}
    for c, (head, items) in enumerate(cols):
        x = 30 + c * 255
        f.text(x + 115, 74, head, size=16, weight="700")
        for i, it in enumerate(items):
            on = (c, i) in fast
            role = "verified" if on else ("neutral" if c < 2 else "soft")
            f.box(x, 94 + i * 88, 230, 70, it, role=role, kind="step", thick=on, size=14)
        if c < 2:
            f.arrow(x + 236, 217, x + 252, 217)
    y = 372
    f.text(150, y, "AI Work Loop:", size=14, weight="700", anchor="end")
    xs = [200, 290, 390, 510, 655]
    for i, step in enumerate(LOOP):
        if step == "Decide":
            f.box(xs[i] - 52, y - 20, 104, 40, step, role="highlight", kind="human", thick=True, size=15)
        elif step == "Disclose":
            f.box(xs[i] - 78, y - 17, 156, 34, "Disclose (second)", role="neutral", kind="human", size=14)
        else:
            f.text(xs[i], y, step, size=14, color=muted)
        if i < 4:
            ax = {0: 245, 1: 340, 2: 440, 3: 568}[i]
            f.text(ax, y, "→", size=14, color=muted)
    f.text(400, 410, "Decide: who answers for a judgment. Disclose (second): whose view is whose.",
           size=13, color=muted, width=790)
    f.text(400, 436, "Thick boxes = the fast route, with the Opening Case and Summary · Opening case: Turing's "
           "imitation game, 1950 and 2026", size=13, color=muted, width=790)


# ---------------------------------------------------------------- storyboard
def storyboard(f):
    ink, muted = INK[f.mode], MUTED[f.mode]
    ev = [("1950", "Turing proposes the imitation game"),
          ("1966", "ELIZA, a pattern-matching chat program"),
          ("1980", "Searle's Chinese Room"),
          ("2020", "Bender & Koller: form is not meaning"),
          ("2021", "\"Stochastic parrots\" paper"),
          ("2023", "Consciousness indicators report"),
          ("2026", "Its authors say two models pass a three-party test")]
    f.text(400, 24, "A 1950 question, a 2026 test: the tests changed, the dispute did not", size=17,
           weight="700", width=780)
    f.line(24, 226, 776, 226, color=ink, width=2.4)
    for i, (d, txt) in enumerate(ev):
        x = 14 + i * 111
        up = i % 2 == 0
        y = 50 if up else 246
        f.box(x, y, 106, 158, "", role="neutral", kind="step")
        f.text(x + 53, y + 20, d, size=15, weight="700")
        f.text(x + 53, y + 92, txt, size=13, width=96)
        cx = x + 53
        f.line(cx, 208 if up else 246, cx, 226, color=ink, width=1.4)
        f.raw(f'<circle cx="{cx}" cy="226" r="5" fill="{ink}"/>')
    f.text(400, 432, "All seven are published texts or programs (confirmed). Sources: Turing (1950); Weizenbaum "
           "(1966); Searle (1980); Bender & Koller (2020); Bender et al. (2021); Butlin et al. (2023); "
           "Jones & Bergen (2026).", size=13, color=muted, italic=True, width=780)


# ---------------------------------------------------------------- indicators method
def indicators(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "Check a system against theories' indicator properties, not its words", size=17,
           weight="700", width=780)
    f.box(20, 70, 200, 120, "Scientific theories of consciousness", role="neutral", sub="e.g., global workspace, "
          "recurrent processing, higher-order", sub_size=13)
    f.box(300, 70, 200, 120, "Indicator properties", role="neutral", sub="features each theory says matter, "
          "stated in computational terms", sub_size=13)
    f.box(580, 70, 200, 120, "Check a system's design", role="neutral", sub="which indicators does its "
          "architecture have?", sub_size=13)
    f.arrow(222, 130, 298, 130)
    f.arrow(502, 130, 578, 130)
    f.box(580, 240, 200, 100, "A credence, not a verdict", role="neutral", sub="how likely, given the theories "
          "you accept", sub_size=13)
    f.arrow(680, 192, 680, 238)
    f.box(20, 240, 470, 100, "The system's own words (\"I feel...\")", role="soft", sub="a claim to check: "
          "both sides of the debate accept this", sub_size=13)
    f.text(400, 372, "Method of Butlin et al. (2023; journal version 2026). Their 2023 conclusion: no current "
           "system is conscious; no obvious technical barrier to systems with the indicators.", size=13,
           color=muted, width=780)
    f.text(400, 410, "Contested: critics doubt that computation is enough for consciousness (Seth, 2025).",
           size=13, color=muted, italic=True, width=780)


# ---------------------------------------------------------------- four gaps
def four_gaps(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "Four responsibility gaps need four different fixes", size=17, weight="700")
    gaps = [("Culpability", "Can anyone fairly be blamed for this harm?", "clear duties before use"),
            ("Moral accountability", "Can anyone explain and answer for what the system did?",
             "reasons people can give and check"),
            ("Public accountability", "Can officials or companies be called to account?",
             "records, audits, a route to complain"),
            ("Active responsibility", "Does anyone see it as their job to prevent harm?",
             "named owners, forward-looking duties")]
    for i, (a, q, fix) in enumerate(gaps):
        x = 20 + (i % 2) * 390
        y = 60 + (i // 2) * 150
        f.box(x, y, 370, 130, a, role="neutral", size=15, sub=q + "\nFix: " + fix, sub_size=13)
    f.text(400, 380, "After Santoni de Sio & Mecacci (2021); the \"fix\" lines summarize their proposals. "
           "They argue the gaps can arise with non-learning systems too.", size=13, color=muted, width=780)


# ---------------------------------------------------------------- creative / author / owner
def three_questions(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "\"Creative\", \"author\" and \"owner\" answer different questions", size=17, weight="700")
    cols = [("Creative?", "Is the output new, surprising and valuable?", "a property of the work (Boden, 2004)"),
            ("Whose choices?", "Who made the choices that shaped it?", "the philosophical question of authorship"),
            ("Who answers?", "Who can explain, defend and stand behind it?", "ownership of a text (Chapter 10)")]
    for i, (a, b, c) in enumerate(cols):
        x = 20 + i * 260
        f.box(x, 64, 240, 170, a, role="neutral", size=16, sub=b + "\n" + c, sub_size=13)
    f.box(20, 262, 760, 64, "Legal authorship is a fourth, separate question: Chapter 18", role="soft", size=14)
    f.text(400, 360, "An output can be rated creative while no one is its author in law, and someone still has to "
           "answer for using it.", size=13, color=muted, italic=True, width=780)


# ---------------------------------------------------------------- three labor studies (table figure)
def labor_table(f):
    ink, muted = INK[f.mode], MUTED[f.mode]
    f.text(400, 24, "Three studies of AI and work answer three different questions", size=17, weight="700")
    cols = [20, 190, 400, 600, 780]
    heads = ["Study", "Question asked", "Result (as of its date)", "Evidence status"]
    rows = [("Brynjolfsson, Li & Raymond (2025)", "Did an assistant change support agents' output?",
             "+15% issues resolved per hour; about +30% for less experienced agents",
             "measured (one firm)"),
            ("Humlum & Vestergaard (rev. March 2026)", "Did chatbots change earnings and hours in Denmark?",
             "no effect larger than 2% two years after launch; tasks reorganized",
             "measured (national records)"),
            ("Brynjolfsson, Chandar & Chen (rev. Aug 12, 2026)", "How has young workers' employment moved in "
             "exposed jobs?", "22–25-year-olds 19% below less-exposed peers' pace, to June 2026",
             "measured; descriptive, not causal")]
    y = 60
    f.raw(f'<rect x="20" y="{y}" width="760" height="40" fill="none" stroke="{ink}" stroke-width="1.4"/>')
    for i, h in enumerate(heads):
        f.text((cols[i] + cols[i + 1]) / 2, y + 20, h, size=14, weight="700")
    for r, row in enumerate(rows):
        yy = y + 40 + r * 104
        f.raw(f'<rect x="20" y="{yy}" width="760" height="104" fill="none" stroke="{ink}" stroke-width="1.2"/>')
        for i, cell in enumerate(row):
            f.text((cols[i] + cols[i + 1]) / 2, yy + 52, cell, size=13, weight="600" if i == 0 else "normal",
                   width=cols[i + 1] - cols[i] - 14)
    for x in cols[1:-1]:
        f.line(x, y, x, y + 40 + 3 * 104, color=ink, width=1.2)
    f.text(400, 436, "Different firms, countries, measures and dates: the numbers cannot be added or compared "
           "directly. Earlier versions of the last two reported other figures.", size=13, color=muted,
           italic=True, width=780)


# ---------------------------------------------------------------- statement, assessment, essay
def doc_kinds(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "A statement, an assessment and an essay are different kinds of evidence", size=17,
           weight="700", width=780)
    cols = [("Statement (CAIS, May 2023)", "Who: signatories, including researchers and company leaders\n"
             "What: one sentence\nAsks: treat extinction risk as a global priority"),
            ("Assessment (International AI Safety Report, Feb 2026)", "Who: 100+ experts, government-backed\n"
             "What: a review of evidence, with disagreements recorded\nAsks: endorses no policy"),
            ("Essay (Narayanan & Kapoor, Apr 2025)", "Who: two computer scientists\n"
             "What: an argument from how past technologies spread\nAsks: policies for resilience")]
    for i, (a, b) in enumerate(cols):
        x = 20 + i * 260
        f.box(x, 64, 240, 230, a, role="neutral", size=14, sub=b, sub_size=13)
    f.text(400, 326, "Each makes or reviews forecasts (Chapter 22's label); none is a measurement of the future.",
           size=13, color=muted, width=780)
    f.text(400, 352, "A signature list shows who holds a view, not that the view is true.", size=13, color=muted,
           italic=True, width=780)


# ---------------------------------------------------------------- position paper card
def paper_card(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "A position paper keeps your view in its own labeled box", size=17, weight="700")
    parts = [("1. The question", "one sentence"), ("2. The map", "claim, reasons, objections"),
             ("3. Side A at its strongest", "from a primary source"), ("4. Side B at its strongest",
                                                                     "from a primary source"),
             ("5. Hardest objection", "and your reply"), ("6. What would change it", "evidence you would accept"),
             ("7. AI Use Declaration", "five elements")]
    for i, (a, b) in enumerate(parts):
        x = 20 + (i % 4) * 192
        y = 60 + (i // 4) * 120
        f.box(x, y, 176, 100, a, role="neutral", size=14, sub=b, sub_size=13)
    f.box(596, 180, 184, 100, "YOUR VIEW (labeled)", role="highlight", size=14, sub="\"undecided, because...\" "
          "counts", sub_size=13)
    f.text(400, 316, "Parts 3 and 4 never contain your view; the labeled box is the only place it appears.",
           size=13, color=muted, width=780)


# ---------------------------------------------------------------- summary card
def summary_card(f):
    f.text(400, 24, "Chapter 23 in six cards: where each debate turns", size=18, weight="700")
    cards = [("Understanding", "is behavior enough evidence?"),
             ("Consciousness", "can computation be enough, and what counts as evidence?"),
             ("Responsibility", "can anyone be justly held responsible when no one could foresee?"),
             ("Creativity", "new, surprising and valuable, or someone's choices?"),
             ("Work", "which tasks change, and who decides?"),
             ("Long-term risk", "how fast do effects arrive, and what comes first?")]
    for i, (a, b) in enumerate(cards):
        x = 20 + (i % 3) * 260
        y = 50 + (i // 3) * 130
        f.box(x, y, 240, 110, a, role="neutral", size=15, sub=b, sub_size=13)
    f.text(400, 316, "Method for all six: each side at its strongest, the disputed premise, your view labeled",
           size=13, color=MUTED[f.mode])


# ---------------------------------------------------------------- maps
MAP_TEMPLATE = dict(
    claim=("The claim being argued", "who makes it, where"),
    pros=[("A reason or premise that supports the claim", "its source"),
          ("A premise the argument needs but does not state", "the reader's reconstruction", "inferred")],
    cons=[{"text": "An objection that denies one premise", "source": "its source", "target": "pro:2"},
          ("An objection to the claim as a whole", "its source")],
    title="An argument map shows reasons and objections, not who is right")

MAP_ELIF = dict(
    claim=("AI tutors can't understand students, so they can't help them", "a classmate in Elif's seminar"),
    pros=[("AI tools produce text by prediction, not by understanding", "the classmate (contested: 23.2)"),
          ("Only something that understands a student can help that student", "unstated premise", "inferred")],
    cons=[{"text": "Practice questions and feedback help students whether or not the tool understands",
           "source": "Elif", "target": "pro:2"},
          ("Help can be measured; the claim can be tested in a study", "Elif")],
    title="Elif's map: the disagreement sits in one unstated premise")

MAP_TURING = dict(
    claim=("Replace \"Can machines think?\" with the imitation game", "Turing (1950)"),
    pros=[("\"Think\" is too vague to settle by defining words", "Turing (1950)"),
          ("We grant other people minds on the evidence of behavior", "Turing's reply (Turing, 1950)")],
    cons=[{"text": "A machine must feel, not only produce words, to think", "source": "objection from consciousness (Turing, 1950)", "target": "pro:2"},
          ("A machine only does what we tell it to do", "Lady Lovelace's objection (Turing, 1950)"),
          ("A program could pass and still understand nothing", "Searle (1980), thirty years later")],
    title="Turing answered objections instead of defining \"think\"")

MAP_ROOM = dict(
    claim=("Running the right program is not enough for understanding", "Searle (1980)"),
    pros=[("A program manipulates symbols by their form (syntax)", "Searle (1980)"),
          ("Form alone is not enough for meaning (semantics)", "Searle (1980)"),
          ("The person in the room follows the rules and understands no Chinese", "the thought experiment")],
    cons=[("Simulate the neurons of a Chinese speaker's brain", "brain simulator reply (Searle, 1980)"),
          {"text": "Connect the symbols to the world with cameras and motors",
           "source": "robot reply (Searle, 1980)", "target": "pro:2"},
          {"text": "The whole system (person, rules, papers) is what understands",
           "source": "systems reply (Searle, 1980)", "target": "pro:3"}],
    highlight="con:3",
    title="The systems reply denies that the person in the room is the one who would understand")

MAP_PARROTS = dict(
    claim=("Language models produce linguistic form without meaning", "Bender & Koller (2020); Bender et al. (2021)"),
    pros=[("Meaning links form to something outside language: intent, the world", "Bender & Koller (2020)"),
          ("A model trained only on text receives only form", "Bender & Koller (2020)")],
    cons=[{"text": "Meaning can come from relations among concepts (conceptual role)",
           "source": "Piantadosi & Hill (2022)", "target": "pro:1"},
          ("Machines may have a different mode of understanding", "Mitchell & Krakauer (2023)")],
    title="\"Stochastic parrots\" is a claim about meaning; critics dispute what meaning needs")

MAP_WELFARE = dict(
    claim=("AI welfare deserves serious attention now", "Long et al. (2024)"),
    pros=[("There is a realistic chance some systems will soon be conscious or robustly agentic",
           "Long et al. (2024)"),
          ("Under uncertainty, take proportionate precautions", "Birch (2024)")],
    cons=[{"text": "Consciousness likely depends on being a living organism", "source": "Seth (2025)",
           "target": "pro:1"},
          ("Welfare talk is premature and feeds belief in seemingly conscious AI", "Suleyman (2025): interested source")],
    note="Contested. Another interested source, Anthropic, cited welfare uncertainty in August 2025; this book was "
         "drafted with Anthropic's tools.",
    title="Moral status: two serious sides, one label: contested")

MAP_GAP = dict(
    claim=("Learning systems open a responsibility gap", "Matthias (2004)"),
    pros=[("Holding someone responsible needs control and foresight", "Matthias (2004)"),
          ("Learning systems act in ways makers and operators cannot predict", "Matthias (2004)")],
    cons=[{"text": "Responsibility practices can stretch to cover new cases", "source": "Tigard (2021)",
           "target": "pro:1"},
          {"text": "Design systems for meaningful human control", "source": "Santoni de Sio & van den Hoven (2018)",
           "target": "pro:2"},
          ("The bigger risk is blame landing on the nearest person", "Elish (2019)")],
    title="Matthias's gap and the main replies")

MAP_RISK = dict(
    claim=("Extinction risk from AI should be a global priority", "CAIS statement (2023), paraphrased"),
    pros=[("Capabilities are improving fast and may outpace our ability to control them", "Bengio et al. (2024)"),
          ("Many AI researchers give non-trivial chances to extremely bad outcomes", "Grace et al. (survey 2023; forecast)")],
    cons=[{"text": "AI's effects arrive slowly, through adoption, like other general-purpose technologies",
           "source": "Narayanan & Kapoor (2025)", "target": "pro:1"},
          ("The framing draws attention from present harms", "Gebru & Torres (2024)")],
    title="The long-term-risk debate turns on how fast effects arrive")

CHAIN_TEMPE = failure_chain(
    notes={0: "Detected 5.6 s before impact, never classified as a pedestrian (NTSB)",
           1: "Design relied on the operator to brake; she was looking at a phone (NTSB)",
           2: "Automation complacency not addressed by the company (NTSB)",
           3: "A pedestrian was killed (NTSB)"},
    highlight={1, 2},
    tag="Tempe, Arizona, 2018 · all links documented (NTSB report HAR-19-03) · no tree branch is assigned")

FUNNEL_QUOTE = verification_funnel(
    highlight=["claims", "primary"],
    notes={"claims": "\"Searle argued that ...\" in a tool's output",
           "check": "a source pack page or the library copy",
           "primary": "Searle (1980) itself: is the point there?"},
    note="An attributed claim is checked in the text it is attributed to")


def mp(d):
    keys = ("claim", "pros", "cons", "highlight", "note", "title")
    return argument_map(**{k: d[k] for k in keys if k in d})


def mh(d):
    return map_height(d.get("pros", ()), d.get("cons", ()), title=True)


FIGS = [
    ("f23-01-chapter-map", chapter_map, 800, 455, "Chapter 23 at a glance"),
    ("f23-02-storyboard", storyboard, 800, 470, "A 1950 question, a 2026 test: the tests changed, the dispute did not"),
    ("f23-03-map-template", mp(MAP_TEMPLATE), 800, mh(MAP_TEMPLATE), MAP_TEMPLATE["title"]),
    ("f23-04-map-elif", mp(MAP_ELIF), 800, mh(MAP_ELIF), MAP_ELIF["title"]),
    ("f23-05-map-turing", mp(MAP_TURING), 800, mh(MAP_TURING), MAP_TURING["title"]),
    ("f23-06-map-room", mp(MAP_ROOM), 800, mh(MAP_ROOM), MAP_ROOM["title"]),
    ("f23-08-map-parrots", mp(MAP_PARROTS), 800, mh(MAP_PARROTS), MAP_PARROTS["title"]),
    ("f23-09-indicators", indicators, 800, 430, "Check a system against theories' indicator properties, not its words"),
    ("f23-11-map-welfare", mp(MAP_WELFARE), 800, mh(MAP_WELFARE), MAP_WELFARE["title"]),
    ("f23-12-four-gaps", four_gaps, 800, 410, "Four responsibility gaps need four different fixes"),
    ("f23-13-map-gap", mp(MAP_GAP), 800, mh(MAP_GAP), MAP_GAP["title"]),
    ("f23-14-chain-tempe", CHAIN_TEMPE, 800, 420, "Blame can land on the last person in the chain"),
    ("f23-15-three-questions", three_questions, 800, 384,
     "\"Creative\", \"author\" and \"owner\" answer different questions"),
    ("f23-17-labor-table", labor_table, 800, 466, "Three studies of AI and work answer three different questions"),
    ("f23-18-map-risk", mp(MAP_RISK), 800, mh(MAP_RISK), MAP_RISK["title"]),
    ("f23-19-doc-kinds", doc_kinds, 800, 376, "A statement, an assessment and an essay are different kinds of evidence"),
    ("f23-20-paper-card", paper_card, 800, 340, "A position paper keeps your view in its own labeled box"),
    ("f23-21-funnel-quote", FUNNEL_QUOTE, 800, funnel_height(note=True),
     "An attributed claim is checked in the source, not by the tool that produced it"),
    ("f23-22-summary-card", summary_card, 800, 340, "Chapter 23 summary card"),
]

if __name__ == "__main__":
    only = set(sys.argv[1:])
    for fid, fn, w, h, title in FIGS:
        if only and fid not in only:
            continue
        render(fid, fn, w, h, title, ROOT)
        print("rendered", fid)
