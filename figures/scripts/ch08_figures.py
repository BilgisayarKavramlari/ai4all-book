"""Chapter 8 diagrams (SVG, color + gray). Run from the repo root:
    python3 figures/scripts/ch08_figures.py
Data charts (F8.6, F8.9) are in ch08_charts.py (data/ch08_citations.csv, data/ch08_calibration_toy.csv).

Signature 8, the Verification Funnel, is introduced here: `verification_funnel(...)`. Chapters 9, 10 and 11
import it (`from ch08_figures import verification_funnel`):

    verification_funnel(highlight="primary")                      # one stage marked
    verification_funnel(highlight=["check", "stop"], verdict="contradicted",
                        tag="Case: …", notes={"check": "…", "primary": "…"})

Stages (highlight names): "claims", "check" (alias "source"), "primary", "expert", "stop" (the side rail),
"verdict", "uncertainty". Verdict scale (book-wide): supported · partly supported · unsupported ·
contradicted · cannot verify.

Reused here: Signature 5 (`from ch04_figures import failure_tree, failure_chain, tree_height`).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from figlib import render, MUTED, INK, wrap  # noqa: E402
from ch04_figures import failure_tree, failure_chain, tree_height  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LOOP = ["Frame", "Prompt", "Verify", "Decide", "Disclose"]

# ---------------------------------------------------------------- Signature 8: The Verification Funnel
VERDICTS = ["supported", "partly supported", "unsupported", "contradicted", "cannot verify"]
STAGES = ["claims", "check", "primary", "expert", "stop", "verdict", "uncertainty"]
ALIASES = {"source": "check", "independent": "check", "rail": "stop"}
BANDS = [  # key, label, sub, width, kind
    ("claims", "Claims", "split the output: one statement you might rely on per claim", 540, "step"),
    ("check", "1. Independent check",
     "a source no AI tool produced, with an author or publisher you can name, or redo the calculation yourself",
     476, "step"),
    ("primary", "2. Primary source", "the original record: the study, dataset, law, court record or official page",
     410, "step"),
    ("expert", "3. Expert", "a person with the knowledge and access to judge it; ask for reasons", 344, "human"),
]
CX = 318          # funnel axis
RAIL_X = 640      # the side rail
BAND_H = 66
BAND_GAP = 20


def _norm(highlight):
    if highlight is None:
        return set()
    items = [highlight] if isinstance(highlight, str) else list(highlight)
    out = {ALIASES.get(h, h) for h in items}
    if out - set(STAGES):
        raise ValueError(f"unknown stage: {out - set(STAGES)}")
    return out


def funnel_height(tag=None, note=None):
    """Canvas height for verification_funnel with the same tag/note arguments."""
    return 596 + (22 if tag else 0) + (20 if note else 0)


def verification_funnel(highlight=None, verdict=None, tag=None, note=None, notes=None):
    """Signature 8, The Verification Funnel (7 boxes).

    highlight: one stage name or a list ("claims", "check"/"source", "primary", "expert", "stop",
               "verdict", "uncertainty"); marked by a thick border and dark fill (as work_loop does).
    verdict:   one label from VERDICTS printed in the verdict box; None prints the whole scale.
    tag:       one-line case label under the title.
    note:      one-line italic remark under the tag.
    notes:     {"check"|"primary"|"expert": short text} printed right of the rail beside that stage
               (at most ~60 characters each).
    Canvas: 800 × funnel_height(tag, note).
    """
    hl = _norm(highlight)
    notes = {ALIASES.get(k, k): v for k, v in (notes or {}).items()}
    if verdict is not None and verdict not in VERDICTS:
        raise ValueError(f"verdict must be one of {VERDICTS}")

    def draw(f):
        ink, muted = INK[f.mode], MUTED[f.mode]
        f.text(400, 24, "The Verification Funnel", size=18, weight="700")
        y = 46
        if tag:
            f.text(400, y, tag, size=13, weight="700", width=760)
            y += 22
        if note:
            f.text(400, y, note, size=13, color=muted, italic=True, width=760)
            y += 20
        top = y + 10
        # AI output (hexagon)
        f.box(CX - 110, top, 220, 44, "An AI output", role="ai", kind="ai", size=15)
        f.arrow(CX, top + 46, CX, top + 64)
        # rail label (top right)
        f.text(RAIL_X + 6, top + 18, "Stop when the evidence matches the stakes", size=13, weight="700",
               width=200, color=ink)
        by = top + 66
        ys = {}
        for i, (key, label, sub, w, kind) in enumerate(BANDS):
            on = key in hl
            role = "highlight" if on else ("soft" if key == "claims" else "neutral")
            f.box(CX - w / 2, by, w, BAND_H, label, role=role, kind=kind, thick=on, size=15, sub=sub,
                  sub_size=13)
            ys[key] = by + BAND_H / 2
            if i < len(BANDS) - 1:
                f.arrow(CX, by + BAND_H + 1, CX, by + BAND_H + BAND_GAP - 1)
                lab = "every claim you rely on" if i == 0 else "stakes not yet met"
                f.text(CX + 10, by + BAND_H + BAND_GAP / 2, lab, size=13, color=muted, italic=True,
                       anchor="start")
            if key != "claims":
                x_edge = CX + w / 2
                f.arrow(x_edge + 3, ys[key], RAIL_X - 2, ys[key], width=3.0 if "stop" in hl else 1.8)
            if key in notes:
                f.text(RAIL_X + 14, ys[key], notes[key], size=13, anchor="start", width=146, italic=True,
                       weight="600")
            by += BAND_H + BAND_GAP
        # rail
        rail_top = ys["check"]
        v_y = by + 6
        f.line(RAIL_X, rail_top, RAIL_X, v_y - 30, width=3.4 if "stop" in hl else 2.0)
        f.arrow(RAIL_X, v_y - 31, RAIL_X, v_y - 2, width=3.4 if "stop" in hl else 2.0)
        # verdict and uncertainty
        on = "verdict" in hl
        sub = verdict if verdict else " · ".join(VERDICTS)
        f.box(430, v_y, 350, 74, "Verdict", role="highlight" if on else "verified", kind="step", thick=on,
              size=15, sub=sub, sub_size=13 if verdict is None else 15)
        on_u = "uncertainty" in hl
        f.box(30, v_y, 360, 74, "Remaining uncertainty", role="highlight" if on_u else "soft", kind="step",
              dashed=True, thick=on_u, size=15, sub="what you could not check, and why",
              sub_size=13)
        f.arrow(428, v_y + 37, 393, v_y + 37, dashed=True)
        f.text(400, v_y + 102, "Hexagon = AI output · rectangles = checks you run · rounded = a person · "
               "dashed = uncertainty · thick dark border = the stage this figure marks", size=13, color=muted,
               width=780)
    return draw


# ---------------------------------------------------------------- F8.1 Chapter map
def chapter_map(f):
    muted = MUTED[f.mode]
    f.text(400, 30, "Chapter 8 at a glance", size=22, weight="700")
    cols = [("Checking claims", ["8.1 From an answer to claims", "8.2 The Verification Funnel",
                                 "8.3 Checking citations and quotations"]),
            ("Before and after", ["8.4 Uncertainty signals", "8.5 Measuring calibration",
                                  "Deep 8.A–8.B (optional)"]),
            ("Practice", ["8.6 Lab 8.1 and A5 (Studio)", "Labs 8.2–8.3 (optional)",
                          "Case Study: Mata v. Avianca"])]
    for c, (head, items) in enumerate(cols):
        x = 30 + c * 255
        f.text(x + 115, 74, head, size=16, weight="700")
        for i, it in enumerate(items):
            role = "neutral" if c < 2 else ("verified" if i == 0 else "soft")
            kind = "human" if c == 2 else "step"
            dashed = (c == 1 and i == 2)
            f.box(x, 94 + i * 88, 230, 70, it, role=role, kind=kind, dashed=dashed, size=14)
        if c < 2:
            f.arrow(x + 236, 217, x + 252, 217)
    y = 372
    f.text(150, y, "AI Work Loop:", size=14, weight="700", anchor="end")
    xs = [205, 300, 420, 540, 640]
    for i, step in enumerate(LOOP):
        if step == "Verify":
            f.box(xs[i] - 50, y - 20, 100, 40, step, role="highlight", kind="human", thick=True, size=15)
        elif step == "Decide":
            f.box(xs[i] - 45, y - 17, 90, 34, step, role="neutral", kind="human", dashed=True, size=14)
        else:
            f.text(xs[i], y, step, size=14, color=muted)
        if i < 4:
            f.text((xs[i] + xs[i + 1]) / 2, y, "→", size=14, color=muted)
    f.text(400, 410, "This chapter strengthens Verify (how to check a claim), then Decide (dashed): keep, change "
           "or reject.", size=13, color=muted, width=780)
    f.text(400, 436, "Opening case: Mata v. Avianca (federal court, New York, 2023), six court decisions that did not exist",
           size=13, color=muted)


# ---------------------------------------------------------------- F8.2 Mata storyboard
def storyboard(f):
    muted, ink = MUTED[f.mode], INK[f.mode]
    ev = [("Mar 1, 2023", "Filing cites cases ChatGPT made up (¶¶ 5, 36)", "ai", "ai"),
          ("Mar 15", "Avianca's lawyers cannot find most of the cases (¶ 7)", "neutral", "step"),
          ("Apr 11–12", "Court orders copies of the decisions (¶ 13)", "neutral", "step"),
          ("Apr 25", "Affidavit attaches excerpts of fake “decisions” (¶¶ 20–22)", "risk", "step"),
          ("May 25", "The lawyers begin to admit what happened (p. 2)", "neutral", "human"),
          ("Jun 22, 2023", "Sanctions: $5,000 and letters to the client and judges", "verified", "step")]
    f.line(24, 200, 776, 200, color=ink, width=2.4)
    for i, (d, txt, role, kind) in enumerate(ev):
        x = 14 + i * 129
        y = 34 if i % 2 == 0 else 222
        f.box(x, y, 122, 146, d, role=role, kind=kind, size=14, sub=txt, sub_size=13)
        cx = x + 61
        f.line(cx, 180 if i % 2 == 0 else 222, cx, 200, color=ink, width=1.4)
        f.raw(f'<circle cx="{cx}" cy="200" r="5" fill="{ink}"/>')
    f.text(400, 396, "Hexagon = the AI-produced text · hatched in print, dark orange in color = the filing that "
           "repeated the error · rounded = admission · shaded = the order", size=13, color=muted, width=780)
    f.text(400, 446, "Dates and paragraphs from Mata v. Avianca, Inc. (federal court, New York), court document ECF 54 "
           "(June 22, 2023). The claim itself was dismissed as filed too late (ECF 55).", size=13, color=muted,
           italic=True, width=780)


# ---------------------------------------------------------------- F8.3 claim split (constructed)
CLAIMS = [("1", "The exam has four sections: AUD, BEC, FAR and REG.", "fact", "high"),
          ("2", "Each section lasts four hours.", "number", "medium"),
          ("3", "You need a score of 75 to pass each section.", "number", "high"),
          ("4", "You must pass all four within 18 months.", "number", "high"),
          ("5", "Source: the official exam blueprint.", "citation", "medium"),
          ("6", "Most candidates should start with the hardest section.", "judgment: not checkable", "low")]


def claim_split(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "One paragraph, six claims (constructed example)", size=17, weight="700")
    f.box(20, 44, 760, 92, "", role="ai", kind="ai")
    f.text(400, 90, "“The CPA exam has four sections, AUD, BEC, FAR and REG. Each lasts four hours, and you need "
           "75 to pass each one. You must pass all four within 18 months. Most candidates should start with the "
           "hardest section. Source: the official exam blueprint.”", size=13, italic=True, width=680)
    heads = [("#", 34), ("Claim", 70), ("Type", 520), ("Stakes", 690)]
    for h, x in heads:
        f.text(x, 160, h, size=13, weight="700", anchor="start")
    for i, (n, c, t, s) in enumerate(CLAIMS):
        y = 184 + i * 40
        dashed = "not checkable" in t
        f.box(24, y - 15, 750, 32, "", role="soft" if i % 2 else "neutral", kind="step", dashed=dashed)
        f.text(36, y + 1, n, size=13, weight="700", anchor="start")
        f.text(70, y + 1, c, size=13, anchor="start")
        f.text(520, y + 1, t, size=13, anchor="start", italic=dashed)
        f.text(690, y + 1, s, size=13, anchor="start", weight="700" if s == "high" else "normal")
    f.text(400, 440, "Hexagon = the AI output · each row = one statement you might rely on · dashed row = not "
           "checkable as true or false", size=13, color=muted, width=780)
    f.text(400, 462, "Lucía's overview is a constructed example; section 8.2 checks claim 1.", size=13,
           color=muted, italic=True)


# ---------------------------------------------------------------- F8.5 three ways a citation fails
def three_failures(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "Three ways a citation fails", size=17, weight="700")
    cols = [("1. It does not exist", "Search an index no AI tool produced",
             "“Varghese v. China Southern Airlines”: the federal appeals court's clerk confirmed no such case (¶ 26)"),
            ("2. It points to another work", "Match every detail to the record",
             "Its docket number and Federal Reporter citation belong to two other cases (¶ 28)"),
            ("3. It does not say it", "Open the source and find the passage",
             "Real decisions cited inside it do not contain the quoted words (¶ 29g)")]
    for i, (h, check, ex) in enumerate(cols):
        x = 20 + i * 258
        f.box(x, 46, 244, 64, h, role="risk", kind="step", thick=True, size=15)
        f.arrow(x + 122, 112, x + 122, 132)
        f.box(x, 134, 244, 70, "The check", role="neutral", kind="human", size=14, sub=check, sub_size=13)
        f.text(x + 122, 270, "In Mata: " + ex, size=13, width=230, italic=True)
    f.text(400, 352, "Thick border (hatched in print) = the failure · rounded = the check you run", size=13,
           color=muted)
    f.text(400, 374, "Examples from Mata v. Avianca, ECF 54 (June 22, 2023), Findings of Fact.", size=13,
           color=muted, italic=True)


# ---------------------------------------------------------------- F8.7 three fresh runs (constructed)
def three_runs(f):
    muted, ink = MUTED[f.mode], INK[f.mode]
    f.text(400, 24, "One question, three fresh chats (constructed example)", size=17, weight="700")
    f.box(250, 44, 300, 50, "“How many sections does the CPA exam have?”", role="neutral", kind="human",
          size=14)
    runs = [("Run 1", "Four: AUD, BEC, FAR, REG. “95% sure.”", False),
            ("Run 2", "Four: AUD, BEC, FAR, REG. “95% sure.”", False),
            ("Run 3", "Three core sections plus one discipline section of your choice.", True)]
    for i, (h, txt, diff) in enumerate(runs):
        x = 24 + i * 256
        f.arrow(400, 96, x + 118, 128)
        f.box(x, 130, 236, 104, h, role="ai", kind="ai", size=15, sub=txt, sub_size=13, thick=diff)
    f.box(24, 268, 492, 74, "Runs 1 and 2 agree, and both are outdated", role="neutral", kind="step",
          dashed=True, size=14, sub="agreement is not proof", sub_size=13)
    f.box(534, 268, 242, 74, "Run 3 disagrees", role="risk", kind="step", thick=True, size=14,
          sub="a warning sign: check this claim first", sub_size=13)
    f.line(142, 236, 142, 266, color=ink)
    f.line(398, 236, 398, 266, color=ink)
    f.line(654, 236, 654, 266, color=ink)
    f.text(400, 374, "Hexagons = AI outputs · thick = the run that differs · dashed = an agreement that still "
           "needs checking", size=13, color=muted, width=780)
    f.text(400, 396, "Each run picks its words again with some randomness (Chapter 3). Use a temporary chat or turn memory off.",
           size=13, color=muted, italic=True, width=780)


# ---------------------------------------------------------------- F8.13 A5 template
def a5_template(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "One row of a claim verification table (A5)", size=17, weight="700")
    fields = [("Claim", "one statement you might rely on; checkable or not; type", "neutral", False),
              ("Stakes", "low · medium · high, with a reason", "neutral", False),
              ("Before checking", "your confidence (%) · the tool's stated confidence (%) · any signal", "neutral", False),
              ("Stage reached", "independent check · primary source · expert", "neutral", False),
              ("Source", "link or location; for citations: exists? matches? says it?", "neutral", False),
              ("Verdict", "supported · partly supported · unsupported · contradicted · cannot verify",
               "verified", False),
              ("Remaining uncertainty", "what you could not check, and why", "soft", True),
              ("Corrected statement", "for every claim that is not supported", "neutral", False)]
    for i, (h, sub, role, dashed) in enumerate(fields):
        y = 44 + i * 50
        f.box(20, y, 210, 42, h, role=role, kind="human", dashed=dashed, size=14)
        f.text(244, y + 21, sub, size=13, anchor="start", width=540)
    f.text(400, 458, "Rounded = what you write · shaded = the verdict · dashed = uncertainty · "
           "the tool's own “yes” never counts as a source", size=13, color=muted, width=780)


# ---------------------------------------------------------------- F8.14 two checkers (constructed; Deep 8.A)
def checkers(f):
    import csv
    with open(os.path.join(ROOT, "data", "ch08_checkers.csv"), encoding="utf8") as fh:
        rows = list(csv.DictReader(fh))
    muted = MUTED[f.mode]
    f.text(400, 24, "Two reference checkers on the same 20 references (constructed)", size=17, weight="700")
    for i, r in enumerate(rows):
        x = 30 + i * 380
        tp, fp, fn = int(r["true_pos"]), int(r["false_pos"]), int(r["false_neg"])
        prec = tp / (tp + fp)
        rec = tp / (tp + fn)
        f.box(x, 46, 360, 52, r["checker"], role="ai", kind="ai", size=15)
        f.text(x + 180, 120, f"Flagged {tp + fp} of 20 · fake ones caught: {tp} of {tp + fn}", size=14,
               weight="600")
        f.box(x, 140, 172, 88, "Precision", role="neutral", kind="step", size=15,
              sub=f"{tp} of {tp + fp} flags were fake = {prec:.0%}", sub_size=13)
        f.box(x + 188, 140, 172, 88, "Recall", role="neutral", kind="step", size=15,
              sub=f"caught {tp} of {tp + fn} fakes = {rec:.0%}", sub_size=13)
        f.text(x + 180, 262, r["comment"], size=13, italic=True, width=350)
    f.text(400, 320, "Precision: of what it flagged, the share really fake · Recall: of what was really fake, "
           "the share it flagged (Chapter 2)", size=13, color=muted, width=780)
    f.text(400, 344, "Constructed counts for teaching (data/ch08_checkers.csv); 5 of the 20 references are fake.",
           size=13, color=muted, italic=True)


# ---------------------------------------------------------------- F8.15 summary card
def summary_card(f):
    f.text(400, 26, "Chapter 8 — what you can do now", size=18, weight="700")
    cards = ["Decompose: split an output into claims you might rely on; rank by stakes",
             "Apply the funnel: independent check → primary source → expert; stop at the stakes",
             "Analyze citations: does it exist, does it match, does it say it?",
             "Evaluate signals: disagreement is a warning; agreement and firmness are not proof",
             "Measure calibration: stated confidence vs. share correct, group by group",
             "Produce A5: verdicts, sources, confidence and remaining uncertainty"]
    for i, c in enumerate(cards):
        x = 20 + (i % 3) * 258
        y = 50 + (i // 3) * 150
        f.box(x, y, 242, 130, c, role="neutral" if i % 2 else "soft", kind="human", size=14, weight="600")


# ---------------------------------------------------------------- Case figures (Signature 5, chain, Signature 8)
MATA_TREE = failure_tree({"hallucination", "overconfidence"},
                         tag="Case: Mata v. Avianca (federal court, New York, 2023) · hallucination + overconfidence, both documented",
                         note="Invented cases (¶ 36); asked directly if they were real, the replies said they were (¶¶ 45, 47)")
MATA_CHAIN = failure_chain(
    notes={0: "Six decisions that do not exist (¶ 36)",
           1: "Not checked outside the tool; signer read no authorities (¶¶ 6, 12)",
           2: "Filed with the court; defended after orders (pp. 1–2)",
           3: "$5,000 penalty; letters; time and trust lost"},
    highlight={1},
    tag="Responsibility: the court held the lawyers and their firm responsible for the filing (ECF 54).")
MATA_FUNNEL = verification_funnel(
    highlight=["check", "primary", "verdict"], verdict="contradicted",
    tag="Case: “Varghese v. China Southern Airlines” — flagged at stage 1, contradicted at stage 2",
    notes={"check": "His own search: not found (¶ 12); a second index → unsupported",
           "primary": "The court's records: no such case; citation and docket belong to other cases (¶¶ 26, 28)",
           "expert": "Not needed"})

FIGS = [
    ("f8-04-verification-funnel", verification_funnel(), 800, funnel_height(),
     "Take each claim only as far as its stakes require"),
    ("f8-04d-funnel-mata", MATA_FUNNEL, 800, funnel_height(tag=True),
     "The fake case would have been flagged at stage 1 and contradicted at stage 2"),
    ("f8-04s-funnel-complete", verification_funnel(highlight="verdict",
                                                   note="Every claim you rely on gets at least the independent check"),
     800, funnel_height(note=True), "Every verdict comes with a line of remaining uncertainty"),
    ("f8-01-chapter-map", chapter_map, 800, 455, "Chapter 8 at a glance"),
    ("f8-02-storyboard", storyboard, 800, 478,
     "Six invented cases went from a court filing to a sanctions order in under four months"),
    ("f8-03-claim-split", claim_split, 800, 478,
     "One fluent paragraph held six separate claims to check"),
    ("f8-05-three-failures", three_failures, 800, 390, "A citation can fail in three ways, and each needs a different check"),
    ("f8-07-three-runs", three_runs, 800, 410,
     "Answers that change across fresh runs are a warning sign; answers that agree are not proof"),
    ("f8-11-tree-mata", MATA_TREE, 800, tree_height() + 34,
     "The Mata citations on the tree: invented sources, stated as real"),
    ("f8-12-chain-mata", MATA_CHAIN, 800, 420,
     "The fake cases reached the court because no one checked them outside the tool"),
    ("f8-13-a5-template", a5_template, 800, 478, "A verification table records how far each claim got, not only a verdict"),
    ("f8-14-checkers", checkers, 800, 360,
     "A checker that flags everything catches every fake reference but wastes your time"),
    ("f8-15-summary-card", summary_card, 800, 340, "Chapter 8 summary card"),
]

if __name__ == "__main__":
    only = set(sys.argv[1:])
    for fid, fn, w, h, title in FIGS:
        if only and fid not in only:
            continue
        render(fid, fn, w, h, title, ROOT)
        print("rendered", fid)
