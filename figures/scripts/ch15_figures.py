"""Chapter 15 diagrams (SVG, color + gray). Run from the repo root:
    python3 figures/scripts/ch15_figures.py
The data chart f15-06-reid is in ch15_charts.py (data/ch15_reid.csv).

Two reusable functions are introduced here and imported by later chapters (16, 17, 18, 19):

Signature 10, the Risk Heat Map:
    from ch15_figures import risk_heat_map, HEAT_H
    risk_heat_map(risks=None, moves=None, highlight=None, note=None, band=True, title=None)
  A 3 x 3 grid (9 cells): x = likelihood (1 low, 2 medium, 3 high), y = impact (1 low, 2 medium, 3 high).
  Every cell is labeled in words; cells share one neutral fill (no likelihood x impact shading).
  band=True draws the high-impact row as a labeled band: "High impact: mitigate or name an owner".
  risks:  list of (id, likelihood, impact, evidence) with evidence "D" (documented) or "I" (inferred).
          Evidence = letter beside the marker + outline (solid D, dashed I). At most 7 markers.
  moves:  {id: (likelihood_after, impact_after)}. Before-markers are hollow; after-markers are filled;
          an arrow joins them. Without moves, every marker is hollow (a current rating).
  highlight: a cell (l, i) or a list of cells (thick cell border).
  note:   one line under the legend.
  title:  optional heading drawn above the grid (default None; added in v2, backward compatible).
Legends name shapes and lines, never colors (gray edition).

The data-flow map (book-map figure "data-flow map"):
    from ch15_figures import data_flow_map, FLOW_PARTS, FLOW_H
    data_flow_map(highlight=None, annotate=None, boundary=True, omit=None, note=None)
  Parts (FLOW_PARTS, 9 shapes): "you", "input", "connectors", "tool", "storage", "seen by", "reuse", "output",
  "recipients". highlight: one part or a list (thick border, risk role). annotate: {part: short note}.
  boundary: the trust boundary as a shaded vertical band (no dash: dashes mean only "inferred").
  omit: parts drawn greyed and crossed out with "(not under these
  terms)", so an absence stays visible. note: one line at the bottom.

Reused, never redrawn: Signature 1 strip (chapter map), Signature 5 (`from ch04_figures import failure_tree,
tree_height`), Signature 9 (`from ch14_figures import agent_loop, LOOP_H`).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from figlib import render, MUTED, INK  # noqa: E402
from ch04_figures import failure_tree, tree_height  # noqa: E402  (Signature 5, reused)
from ch14_figures import agent_loop, LOOP_H  # noqa: E402  (Signature 9, reused)

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LOOP = ["Frame", "Prompt", "Verify", "Decide", "Disclose"]
LEVEL = {1: "low", 2: "medium", 3: "high"}
BAND_FILL = {"color": "#FBE3D6", "gray": "url(#hatch)"}


def _as_set(x):
    if x is None:
        return set()
    if isinstance(x, (str, tuple)):
        return {x}
    return set(x)


# ---------------------------------------------------------------- Signature 10: Risk Heat Map
X0, Y0, CW, CH = 170, 92, 180, 92  # grid origin and cell size
HEAT_H = 520


def _cell_xy(l, i):
    """Top-left of the cell for likelihood l (1-3, left to right) and impact i (1-3, bottom to top)."""
    return X0 + (l - 1) * CW, Y0 + (3 - i) * CH


def risk_heat_map(risks=None, moves=None, highlight=None, note=None, band=True, title=None):
    risks = list(risks or [])
    moves = moves or {}
    hl = _as_set(highlight)
    if len(risks) > 7:
        raise ValueError("at most 7 markers per heat map")
    ids = {r[0] for r in risks}
    if set(moves) - ids:
        raise ValueError("moves refer to unknown risk ids")

    def draw(f):
        ink, muted = INK[f.mode], MUTED[f.mode]
        if title:
            f.text(400, 24, title, size=17, weight="700", width=780)
        # band fill first, so cell labels stay on top
        if band:
            bx, by = _cell_xy(1, 3)
            f.raw(f'<rect x="{bx}" y="{by}" width="{3 * CW}" height="{CH}" fill="{BAND_FILL[f.mode]}" stroke="none"/>')
        # cells
        for l in (1, 2, 3):
            for i in (1, 2, 3):
                x, y = _cell_xy(l, i)
                thick = (l, i) in hl
                fill = "none" if (band and i == 3) else "#FFFFFF"
                f.raw(f'<rect x="{x}" y="{y}" width="{CW}" height="{CH}" fill="{fill}" stroke="{ink}" '
                      f'stroke-width="{3 if thick else 1.2}"/>')
                if band and i == 3:
                    f.raw(f'<rect x="{x + CW / 2 - 52}" y="{y + 6}" width="104" height="18" fill="#FFFFFF"/>')
                f.text(x + CW / 2, y + 15, f"{LEVEL[l]} · {LEVEL[i]}", size=13, color=muted)
        if band:
            x, y = _cell_xy(1, 3)
            f.raw(f'<rect x="{x - 4}" y="{y - 4}" width="{3 * CW + 8}" height="{CH + 8}" fill="none" '
                  f'stroke="{ink}" stroke-width="3.2"/>')
            f.text(X0 + 1.5 * CW, Y0 - 22, "High-impact band: mitigate, or name an owner who accepts the risk",
                   size=14, weight="700")
        # axes
        for i in (1, 2, 3):
            _, y = _cell_xy(1, i)
            f.text(X0 - 14, y + CH / 2, LEVEL[i].capitalize(), size=14, weight="600", anchor="end")
        for l in (1, 2, 3):
            x, _ = _cell_xy(l, 1)
            f.text(x + CW / 2, Y0 + 3 * CH + 18, LEVEL[l].capitalize(), size=14, weight="600")
        f.text(X0 + 1.5 * CW, Y0 + 3 * CH + 44, "Likelihood →", size=15, weight="700")
        f.text(60, Y0 + 1.5 * CH, "Impact ↑", size=15, weight="700")
        # marker positions: every token (a before-marker or an after-marker) gets its own slot in its cell;
        # odd ids sit higher and even ids lower, so arrows between neighbouring cells do not cross markers
        tokens = [(r[0], "b", r[1], r[2]) for r in risks] + [(rid, "a", la, ia) for rid, (la, ia) in moves.items()]
        cells = {}
        for tok in tokens:
            cells.setdefault((tok[2], tok[3]), []).append(tok)
        movers = sorted(moves)
        pos = {}
        for (l, i), toks in cells.items():
            x, y = _cell_xy(l, i)
            toks.sort(key=lambda t: (t[0], t[1]))
            n = len(toks)
            for k, (rid, kind, _, _) in enumerate(toks):
                px = x + CW * (k + 1) / (n + 1)
                if not moves:
                    dy = 0
                elif rid in moves:
                    dy = -15 if movers.index(rid) % 2 == 0 else 13
                else:
                    dy = 14
                pos[(rid, kind)] = (px, y + 60 + dy)
        before = {rid: pos[(rid, "b")] for rid in ids}
        after = {rid: pos[(rid, "a")] for rid in moves}
        ev = {r[0]: r[3] for r in risks}

        def marker(x, y, rid, filled):
            dash = ' stroke-dasharray="5 3"' if ev[rid] == "I" else ""
            fill = ink if filled else "#FFFFFF"
            tc = "#FFFFFF" if filled else ink
            f.raw(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="19" fill="#FFFFFF" stroke="none"/>')
            f.raw(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="15" fill="{fill}" stroke="{ink}" stroke-width="2.2"{dash}/>')
            f.text(x, y, str(rid), size=14, weight="700", color=tc)
            f.raw(f'<rect x="{x + 15:.1f}" y="{y - 21:.1f}" width="14" height="16" fill="#FFFFFF"/>')
            f.text(x + 22, y - 13, ev[rid], size=13, weight="700")

        for rid, (ax, ay) in after.items():
            bx, by = before[rid]
            dx, dy = ax - bx, ay - by
            d = (dx * dx + dy * dy) ** 0.5 or 1
            f.raw(f'<line x1="{bx + dx / d * 24:.1f}" y1="{by + dy / d * 24:.1f}" x2="{ax - dx / d * 24:.1f}" '
                  f'y2="{ay - dy / d * 24:.1f}" stroke="#FFFFFF" stroke-width="6"/>')
            f.arrow(bx + dx / d * 18, by + dy / d * 18, ax - dx / d * 20, ay - dy / d * 20, width=2.2)
        for rid, (x, y) in before.items():
            marker(x, y, rid, filled=False)
        for rid, (x, y) in after.items():
            marker(x, y, rid, filled=True)
        ly = Y0 + 3 * CH + 76
        legend = "Cell = likelihood · impact · circle = one risk · D, solid outline = documented · " \
                 "I, dashed outline = inferred"
        if moves:
            legend2 = "Hollow = rating before mitigation · filled = after · arrow = the change"
        else:
            legend2 = "Hollow = the current rating, before any mitigation"
        f.text(400, ly, legend, size=13, color=muted, width=780)
        f.text(400, ly + 22, legend2, size=13, color=muted, width=780)
        if note:
            f.text(400, ly + 48, note, size=13, italic=True, color=muted, width=780)
    return draw


# ---------------------------------------------------------------- Data-flow map
FLOW_PARTS = ["you", "input", "connectors", "tool", "storage", "seen by", "reuse", "output", "recipients"]
FLOW_H = 510
_FLOW = {  # part -> (x, y, w, h, label, sub, kind, role)
    "you": (20, 190, 110, 80, "You", "or your team", "human", "neutral"),
    "input": (150, 190, 140, 80, "Input", "typed, pasted, uploaded", "step", "neutral"),
    "connectors": (340, 62, 170, 70, "Connectors", "other apps it reads or sends to", "step", "neutral"),
    "tool": (330, 185, 190, 90, "AI tool", "the model, at the provider", "ai", "ai"),
    "output": (548, 190, 110, 80, "Output", "the response", "step", "neutral"),
    "recipients": (676, 185, 108, 90, "Recipients", "anyone it is forwarded to", "human", "neutral"),
    "storage": (330, 330, 140, 86, "Storage", "history, memory, logs, backups", "step", "neutral"),
    "seen by": (488, 330, 150, 86, "Seen by", "reviewers, admins, people with a link", "human", "neutral"),
    "reuse": (656, 330, 128, 86, "Reuse", "training future models?", "step", "neutral"),
}
_FLOW_ANN = {  # part -> (x, y, width) for annotations
    "you": (75, 300, 130), "input": (220, 300, 150), "connectors": (640, 97, 230),
    "tool": (425, 160, 220), "output": (603, 304, 130), "recipients": (730, 304, 120),
    "storage": (400, 434, 180), "seen by": (563, 434, 150), "reuse": (720, 434, 140),
}


def data_flow_map(highlight=None, annotate=None, boundary=True, omit=None, note=None):
    hl = _as_set(highlight)
    annotate = annotate or {}
    om = _as_set(omit)
    unknown = (hl | set(annotate) | om) - set(FLOW_PARTS)
    if unknown:
        raise ValueError(f"unknown flow part(s): {sorted(unknown)}")

    def draw(f):
        muted = MUTED[f.mode]
        for part in FLOW_PARTS:
            x, y, w, h, lab, sub, kind, role = _FLOW[part]
            dashed = False
            if part in om:
                f.box(x, y, w, h, lab, role="soft", kind=kind, size=15,
                      sub="(not under these terms)", sub_size=13)
                f.line(x + 6, y + 6, x + w - 6, y + h - 6, color=muted, width=1.2)
                continue
            if part in hl:
                role = "risk"
            if part == "reuse" and part not in hl:
                role = "soft"
            f.box(x, y, w, h, lab, role=role, kind=kind, dashed=dashed, thick=part in hl, size=15,
                  sub=sub, sub_size=13)
        # flow arrows
        f.arrow(132, 230, 148, 230)
        f.arrow(292, 230, 330, 230)
        f.arrow(520, 230, 546, 230)
        f.arrow(660, 230, 674, 230)
        f.arrow(425, 134, 425, 183)
        f.arrow(445, 183, 445, 134)
        f.arrow(405, 277, 405, 328)
        f.arrow(472, 373, 486, 373)
        f.arrow(640, 373, 654, 373)
        if boundary:
            f.raw(f'<rect x="306" y="46" width="12" height="400" fill="{"#D9DEE6" if f.mode == "color" else "#BDBDBD"}" stroke="none"/>')
            f.text(312, 28, "Trust boundary", size=14, weight="700")
            f.text(302, 50, "← your side", size=13, italic=True, color=muted, anchor="end")
            f.text(322, 50, "someone else's rules →", size=13, italic=True, color=muted, anchor="start")
        for part, txt in annotate.items():
            x, y, w = _FLOW_ANN[part]
            f.text(x, y, txt, size=13, italic=True, weight="600", width=w, color=INK[f.mode])
        if note:
            f.text(400, 472, note, size=13, italic=True, color=muted, width=780)
        f.text(400, 496, "Rounded = people · hexagon = AI · rectangle = a place data goes · shaded box = depends on the "
               "terms · shaded band = trust boundary · thick = the risk", size=13, color=muted, width=790)
    return draw


# ---------------------------------------------------------------- figure f15-01 Chapter map
def chapter_map(f):
    muted = MUTED[f.mode]
    f.text(400, 30, "Chapter 15 at a glance", size=22, weight="700")
    cols = [("Privacy", ["15.1 Every prompt is a data transfer", "15.2 Personal data: names are not enough"]),
            ("Security", ["15.3 Prompt injection: defense in depth", "15.4 Check the channel, not the voice"]),
            ("Risk", ["15.5 The Risk Heat Map", "15.6 Mitigate, then re-rate"])]
    for c, (head, items) in enumerate(cols):
        x = 30 + c * 255
        f.text(x + 115, 74, head, size=16, weight="700")
        for i, it in enumerate(items):
            f.box(x, 94 + i * 88, 230, 70, it, role="neutral", kind="step", size=14)
        if c < 2:
            f.arrow(x + 236, 173, x + 252, 173)
    f.box(30, 280, 740, 50, "15.7 Red-team lab (Lab 15.1) and A12, the responsible AI risk review",
          role="verified", kind="human", size=14)
    y = 372
    f.text(150, y, "AI Work Loop:", size=14, weight="700", anchor="end")
    xs = [215, 335, 445, 555, 660]
    for i, step in enumerate(LOOP):
        if step == "Prompt":
            f.box(xs[i] - 50, y - 20, 100, 40, step, role="highlight", kind="human", thick=True, size=15)
        elif step == "Decide":
            f.box(xs[i] - 50, y - 17, 100, 34, step + " (2nd)", role="soft", kind="human", size=13)
        else:
            f.text(xs[i], y, step, size=14, color=muted)
        if i < 4:
            f.text((xs[i] + xs[i + 1]) / 2, y, "→", size=14, color=muted)
    f.text(400, 410, "This chapter strengthens Prompt (what you send decides your privacy), then Decide (second): "
           "which risks to reduce, and who owns the rest.", size=13, color=muted, width=780)
    f.text(400, 440, "Opening case: engineers paste source code and a meeting transcript into a chat tool (2023)",
           size=13, color=muted)


# ---------------------------------------------------------------- figure f15-02 Storyboard (C12)
def storyboard(f):
    muted = MUTED[f.mode]
    steps = [("Mar 11, 2023", "Chip division allows a chat tool; staff told to take care"),
             ("Paste 1", "Source code of a chip-data program, to fix an error"),
             ("Paste 2", "Source code of a yield and defect program, to optimize it"),
             ("Paste 3", "A meeting recording turned into text, to draft minutes"),
             ("Notice", "Once sent, stored on outside servers; cannot be retrieved"),
             ("Emergency rule", "Uploads limited to 1,024 bytes per question"),
             ("May 2, 2023", "Generative AI restricted on company devices (confirmed)")]
    xs = [20, 132, 244, 356, 468, 580, 692]
    for i, (when, what) in enumerate(steps):
        risk = when.startswith("Paste")
        f.text(xs[i] + 50, 66, when, size=13, weight="700")
        f.box(xs[i], 84, 100, 176, what, role="risk" if risk else "neutral", kind="step", thick=risk, size=13)
        if i < 6:
            f.arrow(xs[i] + 101, 172, xs[i + 1] - 1, 172)
    f.text(212, 284, "Mar 30: The Economist Korea reports the three pastes", size=13, italic=True, color=muted)
    f.text(630, 284, "Bloomberg, citing the memo", size=13, italic=True, color=muted)
    f.box(20, 306, 760, 58, "No public Samsung statement confirms the pastes. The Economist Korea places them "
          "in March; Bloomberg's account of the memo says the leak happened in April.",
          role="soft", kind="step", size=13)
    f.text(400, 392, "Boxes are reported by named outlets; the May restriction was confirmed by a spokesperson · thick = a paste", size=13,
           color=muted)
    f.text(400, 416, "Sources: Jeong (2023, The Economist Korea); Gurman (2023, Bloomberg) via Sharma (2023); Park (2023, TechCrunch)",
           size=13, color=muted, width=780)


# ---------------------------------------------------------------- figure f15-03–f15-05 data-flow maps
FLOW_BASIC = data_flow_map(note="Ask of every box: what is here, for how long, and under whose rules?")
FLOW_SAMSUNG = data_flow_map(
    highlight=["input", "storage"],
    annotate={"input": "source code; a meeting transcript", "storage": "outside servers; could not be retrieved (reported)", "reuse": "depended on the account's terms"},
    note="This book reads the pastes as made under consumer terms; the reports do not say which account was used.")
FLOW_TERMS = data_flow_map(
    highlight=["seen by"],
    annotate={"reuse": "institutional terms: often no training", "seen by": "institutional: your school's or "
              "employer's admins", "storage": "kept for the period the contract sets",
              "input": "the same input travels the same way"},
    note="Institutional terms change the reuse and seen-by boxes; the data still crosses the boundary.")
FLOW_ECHOLEAK = data_flow_map(
    highlight=["input", "output"],
    annotate={"input": "an email from outside, with hidden instructions",
              "connectors": "the user's mail and files, retrieved to answer",
              "output": "a link or image address that could carry data out"},
    note="C19 (2025): the assistant retrieved the attacker's email with the user's own data. Fixed by the vendor.")
FLOW_LINKS = data_flow_map(
    highlight=["seen by"],
    annotate={"seen by": "anyone using a search engine, once a shared chat was made findable",
              "recipients": "people with the link"},
    note="C20 (2025): an opt-in sharing option widened who could see a chat. The option was removed.")


# ---------------------------------------------------------------- figure f15-07 Marcus's constructed case
def constructed_case(f):
    muted = MUTED[f.mode]
    heads = [("Kept: what the task needs", "verified"), ("Left out: what could point to a person", "risk"),
             ("Built from the textbook", "neutral")]
    items = [["Condition and its signs", "The care steps to practice"],
             ["Unit, bed, date of the shift", "Exact age; a rare detail"],
             ["A constructed patient with textbook values", "Labeled 'constructed case'"]]
    for c, ((h, role), its) in enumerate(zip(heads, items)):
        x = 20 + c * 262
        f.text(x + 120, 40, h, size=15, weight="700", width=250)
        for k, it in enumerate(its):
            f.box(x, 70 + k * 100, 240, 80, it, role=role, kind="step", thick=(role == "risk"), size=14)
    f.text(400, 300, "Marcus sends no detail from his placement, with or without a name.", size=14, weight="600")
    f.text(400, 330, "Thick border = left out · thin border = kept or built", size=13, color=muted)


# ---------------------------------------------------------------- figure f15-08 Defense in depth
def layers(f):
    muted = MUTED[f.mode]
    names = [("Label untrusted content", "keep material apart from instructions"),
             ("Trained priority", "the model favors the provider's and developer's instructions"),
             ("Filters", "classifiers flag likely injections"),
             ("Least privilege", "the tool can reach only what its step needs"),
             ("Approval gate", "a person approves before an action takes effect"),
             ("Log", "a record the system writes, reviewed later")]
    for i, (n, s) in enumerate(names):
        x = 20 + i * 128
        f.box(x, 90, 116, 190, n, role="human" if n == "Approval gate" else "neutral",
              kind="human" if n == "Approval gate" else "step", size=14, sub=s, sub_size=13)
    f.text(60, 60, "Injected text", size=13, weight="700")
    for i in range(6):
        x = 20 + i * 128
        f.line(x - 8 if i else 6, 316, x + 120, 316, width=4.2 - i * 0.65)
    f.arrow(770, 316, 790, 316, width=1.2)
    f.box(20, 340, 760, 50, "Each layer lets less through; none has been shown to stop every attack outside its tests (as of October 2026)",
          role="soft", kind="step", size=14)
    f.text(400, 420, "Line under the layers = injected text getting through · thinner = less gets through · rounded = a person",
           size=13, color=muted)


LOOP_INJECTION = agent_loop(
    highlight="observation", annotate={"observation": "a retrieved page carries an instruction"},
    note="Constructed example: a browsing agent compares two public pages; the next tool call acts with the agent's "
         "permissions.")


# ---------------------------------------------------------------- figure f15-10 Three legs
def three_legs(f):
    muted = MUTED[f.mode]
    f.box(300, 160, 200, 90, "One AI system", role="ai", kind="ai", size=16)
    legs = [(40, 40, "Private data", "it can read your mail, files or records"),
            (560, 40, "Untrusted content", "it receives text a stranger can write"),
            (300, 320, "A way to send data out", "it can send messages or load links")]
    for x, y, lab, sub in legs:
        f.box(x, y, 200, 90, lab, role="risk", kind="step", thick=True, size=15, sub=sub, sub_size=13)
    f.arrow(240, 110, 312, 168)
    f.arrow(560, 110, 488, 168)
    f.arrow(400, 252, 400, 318)
    f.text(400, 440, "Remove any one leg and this route for stealing data closes. Injected text can still change "
           "the outputs, so they still need a check.", size=14, weight="600", width=760)
    f.text(400, 482, "After Willison (2025), who calls the combination the lethal trifecta · thick = a leg",
           size=13, color=muted)


# ---------------------------------------------------------------- figure f15-12 Channel check
def channel_check(f):
    muted = MUTED[f.mode]
    f.box(20, 120, 140, 90, "A request", role="neutral", kind="step", size=15, sub="money, logins or data",
          sub_size=13)
    f.box(185, 120, 120, 90, "Pause", role="human", kind="human", size=15, sub="urgency is a cue", sub_size=13)
    f.box(330, 105, 150, 120, "Confirmed out of band?", role="neutral", kind="decision", size=14)
    f.box(505, 120, 140, 90, "Second approver", role="human", kind="human", size=14, sub="dual authorization",
          sub_size=13)
    f.box(660, 120, 120, 90, "Act", role="verified", kind="step", size=15)
    f.arrow(162, 165, 183, 165)
    f.arrow(307, 165, 328, 165)
    f.arrow(482, 165, 503, 165, label="yes", label_dy=-12, size=13)
    f.arrow(647, 165, 658, 165)
    f.arrow(405, 227, 405, 290, label=None)
    f.text(420, 255, "no", size=13, italic=True, color=muted, anchor="start")
    f.box(320, 292, 170, 60, "Stop; report it", role="risk", kind="step", thick=True, size=14)
    f.box(20, 40, 300, 54, "How real the voice or face seems", role="soft", kind="step", size=14)
    f.line(24, 44, 316, 90, color=MUTED[f.mode], width=1.4)
    f.text(470, 66, "not a check: a voice or a face can be generated", size=13, italic=True, color=muted)
    f.text(400, 400, "Out of band = through a channel you already have: the number on file, the directory, in "
           "person · crossed out = set aside", size=13, color=muted, width=780)


# ---------------------------------------------------------------- figure f15-13 Lucía's account-change rule
def account_change(f):
    muted = MUTED[f.mode]
    f.box(20, 130, 150, 90, "Caller asks to change the account email", role="neutral", kind="step", size=14)
    f.box(195, 130, 150, 90, "Code sent to the email already on file", role="neutral", kind="step", size=14)
    f.box(370, 110, 150, 130, "Code confirmed?", role="neutral", kind="decision", size=14)
    f.box(545, 60, 150, 80, "Second agent", role="human", kind="human", size=14,
          sub="approves login or payment changes", sub_size=13)
    f.box(545, 210, 150, 80, "No change; call logged", role="risk", kind="step", thick=True, size=14)
    f.box(715, 70, 70, 60, "Change", role="verified", kind="step", size=14)
    f.arrow(172, 175, 193, 175)
    f.arrow(347, 175, 368, 175)
    f.arrow(500, 150, 543, 110, label="yes", label_dy=-12, size=13)
    f.arrow(500, 200, 543, 245, label="no", label_dy=14, size=13)
    f.arrow(697, 100, 713, 100)
    f.text(400, 330, "Nothing changes on a call alone (constructed example).", size=14, weight="600")
    f.text(400, 360, "Rounded = a person · diamond = a check · thick = the safe default", size=13, color=muted)


# ---------------------------------------------------------------- Heat maps (f15-14 to f15-18, f15-23)
HEAT_EMPTY = risk_heat_map(note="Anchors in full: section 15.5.")
LUCIA = [(1, 2, 3, "D"), (2, 2, 3, "D"), (3, 2, 2, "I"), (4, 1, 2, "I"), (5, 1, 2, "D")]
HEAT_LUCIA = risk_heat_map(risks=LUCIA, note="Constructed example. Risks 1–5 are listed in section 15.5.")
HEAT_MOVES = risk_heat_map(risks=LUCIA, moves={1: (1, 3), 2: (1, 3), 3: (1, 2)},
                           note="Risks 1 and 2 stay in the band, so the team lead owns them; risk 3's owner is Lucía.")
HEAT_SAMSUNG = risk_heat_map(risks=[(1, 3, 3, "D")], moves={1: (1, 3)},
                             note="1 = confidential data pasted into an outside tool. Data already sent did not move.")
HEAT_SAME_CELL = risk_heat_map(risks=[(1, 2, 3, "I"), (2, 2, 3, "I")],
                               note="1 = a mislabeled reply to one customer · 2 = every customer's record exposed. "
                                    "Same cell, very different harm.")


# ---------------------------------------------------------------- figure f15-17 Mitigation ladder
def ladder(f):
    muted = MUTED[f.mode]
    rungs = [("Avoid", "do not send it, connect it or use the feature"),
             ("Reduce", "minimize, use placeholders or an institutional tool, narrow access, add a gate"),
             ("Detect", "logs, reviews, a planted fake value"),
             ("Accept", "the risk that remains, in writing")]
    for i, (r, s) in enumerate(rungs):
        x = 20 + i * 150
        f.box(x, 90, 138, 170, r, role="neutral", kind="step", size=16, sub=s, sub_size=13)
        if i < 3:
            f.arrow(x + 140, 175, x + 148, 175)
    f.box(630, 110, 150, 130, "Risk owner", role="human", kind="human", size=16,
          sub="a named person for every row", sub_size=13)
    f.arrow(620, 175, 628, 175)
    f.text(400, 300, "Every mitigation moves a risk on the heat map; then rate it again.", size=14, weight="600")
    f.text(400, 330, "Rounded = a person · the four kinds are the only words this book uses for mitigation",
           size=13, color=muted)


# ---------------------------------------------------------------- figure f15-19 A12 sheet
def a12_sheet(f):
    muted = MUTED[f.mode]
    f.text(400, 26, "A12 responsible AI risk review (one record)", size=17, weight="700")
    rows = [("1 Scope: workflow, decision owner, data classes", "neutral"),
            ("2 Data-flow map with the trust boundary (drawn in the lab)", "neutral"),
            ("3 Register: five risks (four drafted in the lab: privacy, security, fairness, rules and rights)", "neutral"),
            ("4 Red-team record: injection 3 runs each way, canary trace, bias probe", "soft"),
            ("5 Heat map: hollow before (lab), filled after (home), arrows", "neutral"),
            ("6 Plan for each qualifying risk: kind, change, owner, new rating", "verified"),
            ("7 Note for the decision owner (60–80 words)", "soft"),
            ("8 AI Use Declaration", "soft")]
    for i, (r, role) in enumerate(rows):
        y = 46 + i * 52
        f.box(40, y, 720, 42, r, role=role, kind="step", size=14)
    f.text(400, 476, "Fake data only. Real personal, confidential, patient or client data: returned for resubmission.",
           size=13, color=muted)


# ---------------------------------------------------------------- figure f15-21 Summary card
def summary_card(f):
    f.text(400, 26, "Chapter 15 — what you can do now", size=18, weight="700")
    cards = ["Trace a prompt on the data-flow map",
             "Minimize: names are not the only identifiers",
             "Assume inputs can carry instructions; layer defenses",
             "Remove a leg of the risky combination",
             "Check the channel, not the voice; two approvers",
             "Rate with evidence; mitigate; name an owner"]
    for i, c in enumerate(cards):
        x = 20 + (i % 3) * 258
        y = 50 + (i // 3) * 150
        f.box(x, y, 242, 130, c, role="neutral" if i % 2 else "soft", kind="human", size=14, weight="600")


# ---------------------------------------------------------------- figure f15-22 Three families of defense (Deep)
def defense_families(f):
    muted = MUTED[f.mode]
    cols = [("Train", "the model is trained to favor privileged instructions", "attacks still succeed, less often"),
            ("Detect", "classifiers flag likely injections", "new attacks can slip past a filter"),
            ("Design", "the plan comes only from the user's request; tools' data cannot steer it",
             "fewer tasks completed; a summary can still be changed")]
    for c, (h, what, gap) in enumerate(cols):
        x = 20 + c * 262
        f.box(x, 50, 240, 70, h, role="neutral", kind="step", size=17)
        f.box(x, 140, 240, 100, what, role="neutral", kind="step", size=14)
        f.box(x, 260, 240, 90, "Leaves open: " + gap, role="risk", kind="step", thick=True, size=14)
    f.text(400, 390, "Thick = what each family leaves open (Deep 15.B)", size=13, color=muted)


TREE_ECHOLEAK = failure_tree(highlight={"security vulnerability"},
                             tag="C19 EchoLeak (2025) · security vulnerability, indirect prompt injection, documented",
                             note="Record: CVE-2025-32711; fixed by the vendor; no known exploitation")


FIGS = [
    ("f15-01-chapter-map", chapter_map, 800, 460, "Chapter 15 at a glance"),
    ("f15-02-storyboard", storyboard, 800, 432,
     "Three ordinary work requests sent confidential data outside the company, and none could be taken back"),
    ("f15-03-data-flow-map", FLOW_BASIC, 800, FLOW_H,
     "Every prompt is a transfer: trace what goes in, where it is kept, who sees it, whether it is reused and "
     "where the output goes"),
    ("f15-04-flow-samsung", FLOW_SAMSUNG, 800, FLOW_H,
     "Samsung's pastes crossed the boundary into storage the company did not control"),
    ("f15-05-flow-terms", FLOW_TERMS, 800, FLOW_H,
     "Institutional terms change who may reuse and see an input, not where it travels"),
    ("f15-07-constructed-case", constructed_case, 800, 350, "Marcus sends a constructed case, not a de-identified "
                                                            "real one"),
    ("f15-08-layers", layers, 800, 440,
     "Each layer of defense against prompt injection reduces the risk; none removes it"),
    ("f15-09-loop-injection", LOOP_INJECTION, 800, LOOP_H,
     "When an observation carries an instruction, it reaches the next plan with the agent's permissions"),
    ("f15-10-three-legs", three_legs, 800, 500,
     "Private data, untrusted content and a way to send data out: remove any one and this route for stealing data "
     "closes"),
    ("f15-12-channel-check", channel_check, 800, 420,
     "Check the channel and get a second approver; how real a voice sounds is not a check"),
    ("f15-13-account-change", account_change, 800, 380, "Lucía's team changes nothing on a call alone"),
    ("f15-14-heat-map", HEAT_EMPTY, 800, HEAT_H,
     "Rate each risk by likelihood and impact, and mark what the rating rests on"),
    ("f15-15-heat-lucia", HEAT_LUCIA, 800, HEAT_H,
     "Two of Lucía's five risks sit in the high-impact band, so both need a mitigation or an owner"),
    ("f15-16-heat-moves", HEAT_MOVES, 800, HEAT_H,
     "Mitigations lowered the likelihood of Lucía's two high-impact risks, but their impact stayed high, so each "
     "has an owner"),
    ("f15-17-ladder", ladder, 800, 350,
     "Four ways to answer a risk: avoid it, reduce it, detect it, or accept it, each with a named owner"),
    ("f15-18-heat-samsung", HEAT_SAMSUNG, 800, HEAT_H,
     "Samsung's measures lowered the chance of a new paste; none could recall what was already sent"),
    ("f15-19-a12-sheet", a12_sheet, 800, 490,
     "Your review records the flow, the risks, the tests, the fixes and who owns what remains"),
    ("f15-21-summary-card", summary_card, 800, 340, "Chapter 15 summary card"),
    ("f15-22-defense-families", defense_families, 800, 410,
     "Train, detect or design: each family of injection defense leaves a gap"),
    ("f15-23-same-cell", HEAT_SAME_CELL, 800, HEAT_H, "Two risks in the same cell can differ greatly in expected harm"),
    ("f15-24-tree-echoleak", TREE_ECHOLEAK, 800, tree_height() + 34,
     "EchoLeak on the tree: security vulnerability, documented"),
    ("f15-25-flow-echoleak", FLOW_ECHOLEAK, 800, FLOW_H,
     "In EchoLeak, an email from outside entered the assistant's retrieved content, and an outbound link could "
     "carry data out"),
    ("f15-26-flow-links", FLOW_LINKS, 800, FLOW_H,
     "A sharing option widened the seen-by box to anyone with a search engine"),
]

if __name__ == "__main__":
    only = set(sys.argv[1:])
    for fid, fn, w, h, title in FIGS:
        if only and fid not in only:
            continue
        render(fid, fn, w, h, title, ROOT)
        print("rendered", fid)
