"""Chapter 18 diagrams (SVG, color + gray). Run from the repo root:
    python3 figures/scripts/ch18_figures.py [figure-id ...]
The data chart F18.13 is in ch18_charts.py (data/ch18_legal_status.csv).

New signature introduced here (book map: "Regulation map (EU, U.S., state)"; reused in Chapters 19, 21, 22):

    regulation_map(highlight=None, notes=None, dashed=None, note=None, title=None)
        Nine boxes: a center "Your AI use · the people it affects" (rounded) and eight sources of rules in
        three labeled bands.
          law (by jurisdiction):  "eu" (EU AI Act and other EU law), "us_federal" (U.S. federal: existing laws),
                                  "us_exec" (U.S. federal: executive policy; labeled "changes often"),
                                  "states" (U.S. states), "city" (cities)
          what you agree to:      "terms" (tool terms of service and licenses), "contract" (client and job contracts)
          your organization:      "org" (course, university, employer policy; rounded = rules people set)
        highlight: a key or a list -> "applies to this use" (dark fill, thick border).
        notes:     {key: short text} replaces that box's sub-text (<= about 40 characters).
        dashed:    keys whose placement is only inferred ("may apply"). Dashed means inferred and nothing else.
        note:      one line under the map (for "As of October 2026 · not legal advice").
        Canvas 800 x MAP_H.

Helper (not a signature): ai_act_tiers(notes=None, as_of="October 2026") — the EU AI Act's four tiers as the
book groups them, plus a box for general-purpose AI models. Dates come from data/ch18_legal_status.csv.

Reused, never redrawn: Signature 1 strip style (chapter map), the failure-to-harm chain
(`from ch04_figures import failure_chain`), the voice and ownership spectrum
(`from ch10_figures import voice_spectrum, spectrum_height`), the open-model layers
(`from ch12_figures import open_layers`), the data-flow map and Signature 10
(`from ch15_figures import data_flow_map, FLOW_H, risk_heat_map, HEAT_H`).
"""
import csv
import os
import sys
from datetime import date

sys.path.insert(0, os.path.dirname(__file__))
from figlib import render, MUTED, INK  # noqa: E402
from ch04_figures import failure_chain  # noqa: E402
from ch10_figures import voice_spectrum, spectrum_height  # noqa: E402
from ch12_figures import open_layers  # noqa: E402
from ch15_figures import data_flow_map, FLOW_H, risk_heat_map, HEAT_H  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LOOP = ["Frame", "Prompt", "Verify", "Decide", "Disclose"]


def _set(x):
    if x is None:
        return set()
    if isinstance(x, str):
        return {x}
    return set(x)


def status():
    """Rows of data/ch18_legal_status.csv keyed by id."""
    with open(os.path.join(ROOT, "data", "ch18_legal_status.csv"), encoding="utf8") as fh:
        rows = list(csv.DictReader(line for line in fh if not line.startswith("#")))
    return {r["id"]: r for r in rows}


def fmt(iso):
    d = date.fromisoformat(iso)
    return d.strftime("%b %-d, %Y")


# ---------------------------------------------------------------- Signature: the Regulation Map
MAP_PARTS = ["eu", "us_federal", "us_exec", "states", "city", "terms", "contract", "org"]
MAP_H = 520
_MAP = {  # key -> (x, y, w, h, label, sub, kind)
    "eu": (18, 76, 146, 100, "EU law", "AI Act and other EU law", "step"),
    "us_federal": (172, 76, 146, 100, "U.S. federal law", "copyright, consumer, civil rights", "step"),
    "us_exec": (326, 76, 146, 100, "U.S. executive", "orders and policy; changes often", "step"),
    "states": (480, 76, 146, 100, "U.S. states", "e.g., Texas TRAIGA", "step"),
    "city": (634, 76, 146, 100, "Cities", "e.g., NYC Local Law 144", "step"),
    "terms": (18, 344, 190, 92, "Terms and licenses", "terms of service; model licenses", "step"),
    "contract": (216, 344, 190, 92, "Contracts", "client and job contracts", "step"),
    "org": (440, 344, 340, 92, "Your organization's policy", "course, university, employer", "human"),
}
_CENTER = (250, 226, 300, 72)


def regulation_map(highlight=None, notes=None, dashed=None, note=None, title=None):
    hl, dz, notes = _set(highlight), _set(dashed), dict(notes or {})
    for s in (hl, dz, set(notes)):
        if s - set(MAP_PARTS):
            raise ValueError(f"unknown map part(s): {sorted(s - set(MAP_PARTS))}")
    for k, v in notes.items():
        if len(v) > 44:
            raise ValueError(f"note for {k} too long ({len(v)} chars): {v}")

    def draw(f):
        muted = MUTED[f.mode]
        f.text(400, 20, title or "The Regulation Map: where the rules for an AI use come from", size=18,
               weight="700")
        f.text(18, 56, "Law, by jurisdiction", size=14, weight="700", anchor="start")
        f.text(18, 326, "What you agree to", size=14, weight="700", anchor="start")
        f.text(774, 326, "Your organization's rules", size=14, weight="700", anchor="end")
        cx, cy, cw, ch = _CENTER
        f.box(cx, cy, cw, ch, "Your AI use", role="ai", kind="human", size=16,
              sub="and the people it affects", sub_size=13)
        for k in MAP_PARTS:
            x, y, w, h, lab, sub, kind = _MAP[k]
            on = k in hl
            f.box(x, y, w, h, lab, role="highlight" if on else "neutral", kind=kind, thick=on,
                  dashed=k in dz, size=14, sub=notes.get(k, sub), sub_size=13)
            # arrow to the center: vertical where the box overlaps the center horizontally
            lo, hi = max(x + 20, cx + 30), min(x + w - 20, cx + cw - 30)
            if lo <= hi:
                sx = ex = min(max(x + w / 2, lo), hi)
            else:
                sx = x + w / 2
                ex = min(max(sx, cx + 30), cx + cw - 30)
            if y < cy:
                f.arrow(sx, y + h + 2, ex, cy - 3)
            else:
                f.arrow(sx, y - 2, ex, cy + ch + 3)
        f.text(400, 462, "Every arrow means \"applies to\". Dark, thick border = applies to this use"
               + (" · dashed = may apply (inferred)" if dz else "") + " · rounded = rules people set",
               size=13, color=muted, width=780)
        if note:
            f.text(400, 494, note, size=13, italic=True, color=muted, width=780)
    return draw


# ---------------------------------------------------------------- Helper: EU AI Act tiers
def ai_act_tiers(notes=None, as_of="October 2026"):
    st = status()
    notes = notes or {}
    tiers = [
        ("prohibited", "Prohibited practices", "e.g., inferring emotions from faces or voices at work or school; social scoring",
         f"applies from {fmt(st['aiact_prohibited']['current_date'])}"),
        ("high", "High-risk systems", "e.g., admission, grading, test monitoring, CV screening (Annex III)",
         f"Annex III duties scheduled from {fmt(st['aiact_annex3']['current_date'])}"),
        ("transparency", "Transparency duties", "tell people it is AI; mark generated content; label deepfakes",
         f"applies from {fmt(st['aiact_art50']['current_date'])} (marking: Dec 2, 2026 for systems already on the market)"),
        ("minimal", "Minimal risk", "e.g., spam filters, spell-checkers: no new duties beyond AI literacy", "most uses"),
    ]

    def draw(f):
        muted = MUTED[f.mode]
        f.text(400, 20, f"The EU AI Act's risk tiers (this book's grouping; as of {as_of})", size=18, weight="700")
        widths = [380, 410, 450, 500]
        for i, (k, lab, sub, when) in enumerate(tiers):
            w = widths[i]
            x = 20 + (500 - w) / 2
            y = 48 + i * 96
            role = "risk" if k == "prohibited" else ("neutral" if k != "minimal" else "soft")
            text_sub = notes.get(k, sub)
            f.box(x, y, w, 80, lab, role=role, kind="step", thick=(k == "prohibited"), size=15,
                  sub=text_sub, sub_size=13)
            f.text(x + w + 12, y + 40, when, size=13, weight="600", anchor="start", width=140)
        f.box(636, 346, 144, 96, "General-purpose AI models", role="ai", kind="ai", size=14,
              sub=f"duties from {fmt(st['aiact_gpai']['current_date'])}", sub_size=13)
        f.text(400, 466, "Thick, hatched in print = banned · wider = more uses, fewer duties · hexagon = AI models",
               size=13, color=muted, width=780)
        f.text(400, 490, "Dates: Regulation (EU) 2024/1689, Art. 113, as amended by Regulation (EU) 2026/1744. "
               "Check the current status.", size=13, italic=True, color=muted, width=780)
    return draw


# ---------------------------------------------------------------- F18.1 Chapter map
def chapter_map(f):
    muted = MUTED[f.mode]
    f.text(400, 30, "Chapter 18 at a glance", size=22, weight="700")
    cols = [("Where rules come from", ["18.1 Layers of rules, nearest first", "18.2 Copyright and training data",
                                       "18.3 Who owns AI output?"]),
            ("Who is responsible", ["18.4 Who is responsible when AI is wrong?", "18.5 Governing AI by risk",
                                           "Deep 18.A–18.C (optional)"]),
            ("Practice", ["18.6 The rules-and-rights risk", "A12: Lab 15.1 step 6, then home", "Mini-Project (optional)"])]
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
    xs = [205, 300, 420, 540, 650]
    for i, step in enumerate(LOOP):
        if step == "Decide":
            f.box(xs[i] - 50, y - 20, 100, 40, step, role="highlight", kind="human", thick=True, size=15)
        elif step == "Disclose":
            f.box(xs[i] - 58, y - 17, 116, 34, "Disclose (second)", role="neutral", kind="human", size=13)
        else:
            f.text(xs[i], y, step, size=14, color=muted)
        if i < 4:
            f.text((xs[i] + xs[i + 1]) / 2, y, "→", size=14, color=muted)
    f.text(400, 410, "This chapter strengthens Decide (which rules apply; is this use allowed?), then Disclose "
           "(telling a client, a registry or the people affected).", size=13, color=muted, width=780)
    f.text(400, 440, "Not legal advice: for a real decision, ask the person or office that owns the rule.",
           size=13, weight="700", color=INK[f.mode])


# ---------------------------------------------------------------- F18.2 storyboard (C15)
def storyboard(f):
    muted = MUTED[f.mode]
    f.text(400, 22, "Thomson Reuters v. Ross: from a refused license to an appeals ruling", size=18, weight="700")
    rows = [[("Ross asks to license Westlaw", "refused: a competitor", False),
             ("Training memos written", "using Westlaw headnotes", False),
             ("Search tool trained", "returns passages of court opinions", False),
             ("Thomson Reuters sues", "2020", False)],
            [("Ross shuts down", "Dec 2020 announcement (reported)", True),
             ("2023 ruling", "fair use left for a jury", False),
             ("Feb 11, 2025", "not fair use (appeal allowed Apr 2025)", False),
             ("Sept 29, 2026", "Third Circuit affirms", False)]]
    bw, bh = 176, 92
    for r, row in enumerate(rows):
        y = 50 + r * 140
        for i, (a, b, rep) in enumerate(row):
            x = 18 + i * 196
            last = (r == 1 and i == 3)
            f.box(x, y, bw, bh, a, role="highlight" if last else "neutral", kind="step", dashed=rep,
                  thick=last, size=14, sub=b, sub_size=13)
            if i < 3:
                f.arrow(x + bw + 2, y + bh / 2, x + 196 - 2, y + bh / 2)
        if r == 0:
            f.arrow(18 + 3 * 196 + bw / 2, y + bh + 2, 18 + bw / 2, y + 140 - 4, curve=24)
    f.text(400, 318, "Solid = court record · dashed = reported by a named outlet · thick = the ruling now in force "
           "(as of October 2026)", size=13, color=muted, width=780)


# ---------------------------------------------------------------- F18.5 four factors
def four_factors(f):
    muted = MUTED[f.mode]
    f.text(400, 22, "Fair use (17 U.S.C. § 107): four factors, weighed together", size=18, weight="700")
    facts = [("1. Purpose", "new purpose? commercial?"), ("2. Nature", "creative or factual?"),
             ("3. Amount", "how much, and was it needed?"), ("4. Market", "does it replace the original?")]
    for i, (a, b) in enumerate(facts):
        x = 22 + i * 192
        f.box(x + 18, 46, 140, 96, a, role="neutral", kind="decision", thick=(i == 3), size=15)
        f.text(x + 88, 158, b, size=13, width=176)
        f.arrow(x + 88, 176, 400 + (i - 1.5) * 40, 214)
    f.box(270, 216, 260, 56, "Weighed together, case by case", role="neutral", kind="step", size=15)
    f.arrow(330, 274, 220, 312)
    f.arrow(470, 274, 580, 312)
    f.box(110, 314, 220, 60, "Fair use: allowed", role="verified", kind="human", size=15)
    f.box(470, 314, 220, 60, "Not fair use: infringement", role="neutral", kind="human", size=15)
    f.text(400, 400, "Diamond = a question the court asks · thick = carries great weight (the trial court in Ross called "
           "it the most important) · rounded = a court's decision", size=13, color=muted, width=780)


# ---------------------------------------------------------------- F18.6 Ross factors, district vs appeal
def ross_factors(f):
    muted = MUTED[f.mode]
    ink = INK[f.mode]
    f.text(400, 22, "Ross's fair-use defense, factor by factor", size=18, weight="700")
    f.text(330, 58, "Trial court (Feb 2025)", size=14, weight="700")
    f.text(610, 58, "Third Circuit (Sept 2026)", size=14, weight="700")
    rows = [("1. Purpose", "against fair use: commercial, not transformative",
             "against: same purpose as Westlaw, \"minimally transformative\""),
            ("2. Nature", "for fair use: headnotes are mostly factual", "slightly for fair use"),
            ("3. Amount", "for fair use: the outputs did not show headnotes",
             "against: whole headnotes copied, and copying was not needed"),
            ("4. Market", "against: a substitute; harms an AI-training-data market",
             "against: harms Westlaw and a developing licensing market")]
    for i, (fac, d, a) in enumerate(rows):
        y = 76 + i * 72
        changed = i == 2
        f.box(18, y, 162, 60, fac, role="highlight" if changed else "neutral", kind="step", thick=changed, size=15)
        f.text(330, y + 30, d, size=13, width=250)
        f.text(610, y + 30, a, size=13, width=270, weight="700" if changed else "normal")
        f.line(190, y + 66, 782, y + 66, color=muted, width=0.8)
    f.raw(f'<rect x="190" y="{76 + 2 * 72 - 4}" width="592" height="68" fill="none" stroke="{ink}" '
          f'stroke-width="2.4"/>')
    f.box(190, 372, 592, 46, "Result in both courts: not fair use for the 2,243 headnotes", role="neutral",
          kind="human", size=15)
    f.text(400, 446, "Thick border = the factor the appeals court decided the other way · rounded = the courts' decision. "
           "The appeals court distinguished generative models in a footnote; that is not a holding.",
           size=13, color=muted, width=780)


# ---------------------------------------------------------------- F18.7 rulings scale
def rulings_scale(f):
    muted = MUTED[f.mode]
    f.text(400, 22, "Where U.S. rulings on AI training landed (as of October 2026)", size=18, weight="700")
    f.arrow(60, 200, 742, 200, width=2.4)
    f.arrow(742, 200, 60, 200, width=2.4)
    f.text(70, 228, "Not fair use", size=15, weight="700", anchor="start")
    f.text(732, 228, "Fair use", size=15, weight="700", anchor="end")
    marks = [(60, 52, "Ross (appeals, 2026)", "non-generative tool competing with Westlaw", True),
             (240, 52, "Bartz: pirated library", "millions of pirated books kept (2025)", False),
             (430, 52, "Kadrey (2025)", "fair use on this record; wrong arguments made", False),
             (600, 52, "Bartz: training", "training on books; scanning bought books", False)]
    for x, y, a, b, thick in marks:
        f.box(x, y - 8, 160, 124, a, role="highlight" if thick else "neutral", kind="human", thick=thick, size=14,
              sub=b, sub_size=13)
    for xc in (140, 320, 510, 680):
        f.line(xc, 170, xc, 192, width=1.6)
    f.text(400, 268, "Ross: an appeals court (binds courts in the Third Circuit). Bartz and Kadrey: trial courts "
           "(bind only their own cases).", size=13, color=muted, width=780)
    f.text(400, 296, "Rounded = a court's decision · thick = appeals court", size=13, color=muted)


# ---------------------------------------------------------------- F18.8 layers of Hana's menu cover
def menu_layers(f):
    muted = MUTED[f.mode]
    f.text(400, 22, "Hana's menu cover: what copyright can protect, layer by layer", size=18, weight="700")
    f.box(40, 52, 470, 70, "The owner's generated draft", role="soft", kind="ai", size=15,
          sub="layout reference only · not protected: no human author", sub_size=13)
    f.box(40, 140, 470, 70, "Hana's hand-drawn illustration", role="human", kind="human", size=15,
          sub="Hana's own expression · protected", sub_size=13)
    f.box(40, 228, 470, 70, "The owner's arrangement of text and pictures", role="neutral", kind="human", size=15,
          sub="at most thin protection, as an arrangement", sub_size=13)
    f.box(550, 140, 220, 158, "The bakery's logo, as a brand", role="neutral", kind="step", size=15,
          sub="trademark: protects the bakery's brand in trade; its artwork may also have copyright", sub_size=13)
    f.text(400, 330, "Hexagon = AI output · rounded = made by people · the layout idea itself is not protected "
           "(ideas never are)", size=13, color=muted, width=780)
    f.text(400, 356, "Source: U.S. Copyright Office (2025), Part 2; this book's application to a constructed case",
           size=13, italic=True, color=muted, width=780)


# ---------------------------------------------------------------- F18.10 roles
def roles(f):
    muted = MUTED[f.mode]
    f.text(400, 22, "Who is responsible for an AI system: roles and duties", size=18, weight="700")
    items = [("Provider", "builds and documents it; designs for oversight"),
             ("Deployer", "uses it in its work; checks it; tells people"),
             ("User", "checks the output before relying on it"),
             ("People affected", "customers, applicants, patients, students")]
    for i, (a, b) in enumerate(items):
        x = 18 + i * 196
        f.box(x, 60, 176, 120, a, role="human" if i < 3 else "neutral", kind="human", size=15, sub=b, sub_size=13)
        if i < 3:
            f.arrow(x + 178, 115, x + 194, 115)
    f.box(40, 214, 210, 76, "The model", role="ai", kind="ai", size=15, sub="has no duties: not a legal person",
          sub_size=13)
    f.arrow(146, 212, 106, 182)
    f.text(560, 252, "Terms: provider (developer, in Texas TRAIGA) and deployer (EU AI Act). "
           "Which role carries which duty depends on the law that applies.", size=13, color=muted, width=420)
    f.text(400, 316, "Rounded = people and organizations · hexagon = AI component · duties and good practice "
           "(this book's reading)", size=13, color=muted, width=780)


# ---------------------------------------------------------------- F18.16 risk sheet
def risk_sheet(f):
    muted = MUTED[f.mode]
    ink = INK[f.mode]
    f.text(400, 22, "The rules-and-rights risk (one A12 risk, Chapter 15's template)", size=18, weight="700")
    rows = [("1 Scratch list", "prompts a–e on the data-flow map: terms, syllabus, data classes, policies, one law"),
            ("2 Choose", "the rule with the highest stakes; name its layer"),
            ("3 The risk", "risk of breaking [a named rule] or of [a named person] losing [a named right]"),
            ("4 Evidence", "D: the rule's own text opened, section cited · I: give the reason"),
            ("5 Who is harmed", "rights holder · person in the data · person affected · you or your organization"),
            ("6 Rating", "likelihood · impact (Chapter 15's anchors)"),
            ("7 Mitigation", "avoid · reduce · detect · accept, with the risk owner by role"),
            ("8 Whom to ask", "the rule's owner, by role, and your question"),
            ("9 Last line", "\"This records which rules to check and whom to ask; it is not a legal opinion.\"")]
    top, rh = 46, 44
    f.raw(f'<rect x="18" y="{top}" width="764" height="{rh * len(rows)}" fill="none" stroke="{ink}" '
          f'stroke-width="1.8"/>')
    for i, (a, b) in enumerate(rows):
        y = top + i * rh
        if i:
            f.line(18, y, 782, y, color=muted, width=0.8)
        f.text(30, y + rh / 2, a, size=14, weight="700", anchor="start")
        f.text(200, y + rh / 2, b, size=13, anchor="start")
    f.line(190, top, 190, top + rh * len(rows), color=muted, width=0.8)
    f.text(400, top + rh * len(rows) + 22, "Drafted in Lab 15.1, step 6; finished at home", size=13, italic=True,
           color=muted, width=780)


# ---------------------------------------------------------------- F18.21 summary card
def summary_card(f):
    f.text(400, 24, "Chapter 18 in six cards", size=18, weight="700")
    cards = [("Layers, nearest first", "law · agreements · your organization"),
             ("Training data", "four factors; the facts decide"),
             ("AI output", "only human authors; disclose AI parts"),
             ("When AI is wrong", "deployers and users are responsible (this book's reading)"),
             ("Risk tiers and dated rules", "EU tiers; U.S. laws, states, cities"),
             ("One rules-and-rights risk", "rule, its text, whom to ask")]
    for i, (a, b) in enumerate(cards):
        x = 20 + (i % 3) * 260
        y = 50 + (i // 3) * 130
        f.box(x, y, 240, 110, a, role="verified" if i == 5 else "neutral", kind="human" if i == 5 else "step",
              size=15, sub=b, sub_size=13)
    f.text(400, 316, "Rounded = your decision · not legal advice", size=13, color=MUTED[f.mode])


# ---------------------------------------------------------------- reuses
MAP_INTRO = regulation_map(note="As of October 2026 · not legal advice · the boxes are kinds of rules, not a ranking")
MAP_HANA = regulation_map(
    highlight=["us_federal", "contract", "org"],
    notes={"us_federal": "copyright: who owns the art?", "contract": "Hana's AI clause",
           "org": "Hana's rule: tell the client first"},
    note="Constructed example. Texas: no AI-specific rule found for this job (this book's reading, as of October 2026)")
MAP_US = regulation_map(
    highlight=["us_federal", "us_exec", "states", "city"],
    notes={"us_federal": "no comprehensive AI statute", "us_exec": "EO 14179; EO 14365 (Dec 2025)",
           "states": "TRAIGA from Jan 1, 2026", "city": "LL144 since July 5, 2023"},
    title="The U.S. rules for AI in one map (as of October 2026)",
    note="Colorado's 2024 act was replaced before it took effect; new duties scheduled from Jan 1, 2027. "
         "Check the current status.")
MAP_FAKES = regulation_map(
    highlight=["eu", "us_federal", "states"],
    notes={"eu": "Art. 50 labels; new bans", "us_federal": "TAKE IT DOWN Act; FCC ruling",
           "states": "TRAIGA: sexual deepfakes"},
    title="Rules on fakes and labels (as of October 2026)",
    note="These rules protect the people depicted and voters; they do not decide whether training was lawful.")
SPECTRUM = voice_spectrum(marks={(1, 2): "yours: protected", (3, 4): "only your own parts protected",
                                 (5, 5): "no human author"},
                          note="Copyright mapping: this book's reading of USCO (2025), not a legal test")
RETAIL_CHAIN = failure_chain(
    notes={0: "assistant states a 60-day return window", 1: "policy answers never checked",
           2: "customer returns on day 45", 3: "refund refused; dispute"},
    highlight={1},
    tag="Who is responsible: the shop, as deployer (this book's reading, from Moffatt, 2024). Constructed example.")
TIERS = ai_act_tiers()
FLOW_RULES = data_flow_map(
    annotate={"input": "whose work? which data class?",
              "storage": "retention terms; FERPA or HIPAA (18.1)", "reuse": "training terms",
              "output": "who owns it? a label?", "recipients": "hiring or notice rules"},
    note="At the tool: its terms and license. List rules at each box; write the highest-stakes one as a risk.")
HEAT_ZINE = risk_heat_map(
    risks=[(1, 2, 2, "D")], moves={1: (1, 2)},
    note="Risk 1 (constructed): contributors losing their right to decide how copies of their drawings are used. "
         "Reduce: a no-training tool and an AI line on the form; owner: Hana, as editor.")
FLOW_C15 = data_flow_map(
    highlight=["input", "reuse"], boundary=False,
    annotate={"you": "Ross (and its memo writers)", "input": "memos written from Westlaw headnotes",
              "reuse": "training the tool", "output": "passages of court opinions, not headnotes"},
    note="Input-side harm: the copying sits at the input; no output was wrong, so the tree does not apply.")

FIGS = [
    ("f18-01-chapter-map", chapter_map, 800, 460, "Chapter 18 at a glance"),
    ("f18-02-storyboard", storyboard, 800, 340,
     "Training memos built from a competitor's headnotes led to the first appeals ruling on AI training and fair use"),
    ("f18-03-regulation-map", MAP_INTRO, 800, MAP_H, "Every AI use sits under several layers of rules at once"),
    ("f18-04-map-hana", MAP_HANA, 800, MAP_H, "Hana's menu job touches copyright, a contract and Hana's own rule"),
    ("f18-05-four-factors", four_factors, 800, 420, "Fair use is weighed factor by factor, and market harm carries great weight"),
    ("f18-06-ross-factors", ross_factors, 800, 470,
     "On appeal, the result held but the court decided factor 3 the other way"),
    ("f18-07-rulings-scale", rulings_scale, 800, 316,
     "U.S. courts answered differently on training because the facts differed"),
    ("f18-08-menu-layers", menu_layers, 800, 374,
     "In Hana's menu cover, copyright covers Hana's drawing, not the generated draft"),
    ("f18-09-spectrum-copyright", SPECTRUM, 800, spectrum_height(note=True, marks=True),
     "The more of the wording a tool supplies, the less of it copyright protects for you"),
    ("f18-10-roles", roles, 800, 336, "Each role has its own duty, and none passes to the model"),
    ("f18-11-chain-retail", RETAIL_CHAIN, 800, 420,
     "The shop that deployed the assistant is responsible for its wrong return window"),
    ("f18-12-ai-act-tiers", TIERS, 800, 506, "The EU AI Act sets duties by risk, and most uses carry none"),
    ("f18-14-map-us", MAP_US, 800, MAP_H,
     "In the United States, AI rules come from existing laws, a few states and a city, and changing federal policy"),
    ("f18-15-flow-rules", FLOW_RULES, 800, FLOW_H, "Walk the data-flow map and list the rules that may apply at each box"),
    ("f18-16-risk-sheet", risk_sheet, 800, 470,
     "Your rules-and-rights risk names one rule, its layer and its evidence, and whom to ask"),
    ("f18-17-heat-zine", HEAT_ZINE, 800, HEAT_H, "A no-training tool and a new line on the form moved the zine's risk down"),
    ("f18-18-open-layers", open_layers, 800, 370,
     "Open is a license question: weights, code, data information and terms can each be open or closed"),
    ("f18-19-map-fakes", MAP_FAKES, 800, MAP_H,
     "Laws on fakes protect the people depicted and voters; they do not settle training"),
    ("f18-20-flow-c15", FLOW_C15, 800, FLOW_H, "C15's copying sits at the input; no output was wrong"),
    ("f18-21-summary-card", summary_card, 800, 330, "Chapter 18 summary card"),
]

if __name__ == "__main__":
    only = set(sys.argv[1:])
    for fid, fn, w, h, title in FIGS:
        if only and fid not in only:
            continue
        render(fid, fn, w, h, title, ROOT)
        print("rendered", fid)
