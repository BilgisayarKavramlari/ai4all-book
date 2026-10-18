"""Chapter 9 diagrams (SVG, color + gray). Run from the repo root:
    python3 figures/scripts/ch09_figures.py
Data charts (F9.9, F9.12) are in ch09_charts.py (data/ch09_peters2025.csv, data/ch09_tow2025.csv).

New reusable drawings introduced here (for Chapters 10, 11 and 19):
    source_ladder(highlight=None, needed=None, note=None)   # the source ladder (book-map "Source reliability ladder")
    hop_chain(hops, dashed_arrows=(), notes=None, heading=None, foot=None)   # a claim retold hop by hop

Reused, never redrawn: Signature 8 (`from ch08_figures import verification_funnel`), Signature 4
(`from ch03_figures import llm_anatomy`), Signature 5 and the chain (`from ch04_figures import failure_tree,
failure_chain, tree_height`).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from figlib import render, MUTED, INK  # noqa: E402
from ch03_figures import llm_anatomy  # noqa: E402
from ch04_figures import failure_tree, failure_chain, tree_height  # noqa: E402
from ch08_figures import verification_funnel, funnel_height  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LOOP = ["Frame", "Prompt", "Verify", "Decide", "Disclose"]


# ---------------------------------------------------------------- the source ladder (new, reusable)
RUNGS = {  # rung: (label, sub)
    4: ("4. Is the record itself", "the study, dataset, law, court record or official page that holds the claim"),
    3: ("3. Cites the record specifically", "you can open the record and check it: a review, a textbook, a referenced report"),
    2: ("2. Reports the claim and names a source", "that you have not checked yet: a news story, a press release"),
    1: ("1. States the claim, no traceable origin", "an unsourced page, a social post, a quotation with no reference"),
}
L_X, L_W, R_H, R_GAP, L_TOP = 160, 390, 70, 12, 60


def ladder_height(note=None):
    return 530 + (20 if note else 0)


def source_ladder(highlight=None, needed=None, note=None):
    """The source ladder (5 boxes): four rungs and a dashed area below the ladder for AI output.

    highlight: a rung number (1-4) or a list of rungs to mark (thick border, dark fill).
    needed:    a rung number; draws the "rung your purpose needs" arrow at the left.
    note:      one-line italic remark under the title (e.g., a worked placement).
    The rung measures how directly a source records ONE claim (checkability), not the strength of a body
    of evidence. Rungs 1-3 sit in funnel stage 1 (independent check), rung 4 in stage 2 (primary source).
    """
    hl = set([highlight] if isinstance(highlight, int) else (highlight or []))

    def draw(f):
        ink, muted = INK[f.mode], MUTED[f.mode]
        f.text(400, 24, "The source ladder: how directly does this source record the claim?", size=17,
               weight="700", width=780)
        top = L_TOP + (20 if note else 0)
        if note:
            f.text(400, 48, note, size=13, italic=True, color=muted, width=760)
        ys = {}
        for i, r in enumerate((4, 3, 2, 1)):
            y = top + i * (R_H + R_GAP)
            ys[r] = y
            on = r in hl
            f.box(L_X, y, L_W, R_H, RUNGS[r][0], role="highlight" if on else ("verified" if r == 4 else "neutral"),
                  kind="step", thick=on, size=15, sub=RUNGS[r][1], sub_size=13)
        bottom = ys[1] + R_H
        # rails
        f.line(L_X - 10, top - 10, L_X - 10, bottom + 10, color=ink, width=3)
        f.line(L_X + L_W + 10, top - 10, L_X + L_W + 10, bottom + 10, color=ink, width=3)
        # below the ladder: AI output
        ay = bottom + 26
        f.box(L_X, ay, L_W, 62, "Below the ladder: AI output", role="ai", kind="ai", dashed=True, size=15,
              sub="a lead to sources, not evidence (except of what the tool produced)", sub_size=13)
        # brackets to the funnel
        bx = L_X + L_W + 32
        for (y1, y2, lab) in ((ys[4], ys[4] + R_H, "Funnel stage 2: primary source (Chapter 8)"),
                              (ys[3], ys[1] + R_H, "Funnel stage 1: independent check (Chapter 8), if the author or publisher can be named")):
            f.line(bx, y1 + 4, bx, y2 - 4, color=ink, width=2)
            f.line(bx - 8, y1 + 4, bx, y1 + 4, color=ink, width=2)
            f.line(bx - 8, y2 - 4, bx, y2 - 4, color=ink, width=2)
            f.text(bx + 12, (y1 + y2) / 2, lab, size=13, anchor="start", width=190, weight="600")
        # rung needed
        if needed:
            yc = ys[needed] + R_H / 2
            f.arrow(18, yc, L_X - 16, yc, width=3.2)
            f.text(70, yc - 30, "Rung your purpose needs", size=13, weight="700", width=128)
        f.text(400, ay + 92, "Pick the rung your purpose and stakes need. The ladder measures how checkable a "
               "source is for one claim, not the strength of a body of evidence (Deep 9.A).", size=13,
               color=muted, italic=True, width=700)
        f.text(400, ay + 128, "Rectangles = sources on the rungs · green = the record itself · dashed hexagon = "
               "not on the ladder · thick dark border = the rung this figure marks · arrow = the rung you need",
               size=13, color=muted, width=700)
    return draw


# ---------------------------------------------------------------- hop chain (new, reusable)
def hop_chain(hops, dashed_arrows=(), notes=None, heading=None, foot=None):
    """A claim retold hop by hop (at most 6 hops, left to right).

    hops:          list of (label, sub, kind, role, dashed) with kind in step/human/ai and role a figlib role.
    dashed_arrows: indices i of arrows (hop i -> hop i+1) drawn dashed: drift documented or likely there.
    notes:         {hop index: short italic text printed under that hop}.
    heading:       title line; foot: italic source line.
    """
    notes = notes or {}

    def draw(f):
        muted = MUTED[f.mode]
        f.text(400, 24, heading or "", size=17, weight="700", width=780)
        n = len(hops)
        gap = 18
        w = (760 - gap * (n - 1)) / n
        for i, (lab, sub, kind, role, dashed) in enumerate(hops):
            x = 20 + i * (w + gap)
            f.box(x, 56, w, 132, lab, role=role, kind=kind, dashed=dashed, size=14, sub=sub, sub_size=13)
            if i < n - 1:
                f.arrow(x + w + 1, 122, x + w + gap - 1, 122, dashed=i in dashed_arrows, width=2.2)
            if i in notes:
                f.text(x + w / 2, 236, notes[i], size=13, italic=True, width=w + 6)
        f.text(400, 306, "Rectangles = sources written by people · hexagon = AI output · dashed box = no record "
               "found · dashed arrow = drift documented at that step", size=13, color=muted, width=780)
        if foot:
            f.text(400, 336, foot, size=13, color=muted, italic=True, width=780)
    return draw


RETELLINGS = hop_chain(
    [("Study", "the record of what was done and found", "step", "verified", False),
     ("Preprint", "posted before peer review", "step", "neutral", False),
     ("Journal article", "after peer review", "step", "neutral", False),
     ("Press release", "written for the media", "step", "neutral", False),
     ("News story", "written by a journalist", "step", "neutral", False),
     ("AI summary", "new text generated from a source", "ai", "ai", False)],
    dashed_arrows=(2, 4),
    notes={3: "Exaggeration documented in many (Sumner et al., 2014)",
           5: "Broader claims documented (Peters & Chin-Yee, 2025)"},
    heading="Each retelling of a study is a chance for a caveat to drop",
    foot="Not every claim travels every step; check status (9.2) and trace back (9.4).")

GOLDFISH = hop_chain(
    [("AI answer", "“shorter than a goldfish's”; no source given", "ai", "ai", False),
     ("News articles", "many repeat the claim; cite a 2015 report", "step", "neutral", False),
     ("Marketing report", "Microsoft Canada, 2015; credits a statistics website", "step", "neutral", False),
     ("Statistics website", "gives no study; did not answer requests", "step", "neutral", False),
     ("No study found", "dead end: verdict unsupported", "step", "soft", True)],
    notes={0: "Below the ladder: a lead", 1: "Exists; names its source", 2: "Exists; not the origin",
           3: "Source material not provided", 4: "Write what the trail shows"},
    heading="Following the goldfish claim upstream showed that it had no origin",
    foot="Elif's trace (constructed walk-through of a documented trail; Maybin, 2017).")


# ---------------------------------------------------------------- F9.1 Chapter map
def chapter_map(f):
    muted = MUTED[f.mode]
    f.text(400, 30, "Chapter 9 at a glance", size=22, weight="700")
    cols = [("Judging sources", ["9.1–9.2 Types and status", "9.3 Read laterally", "9.4 Trace upstream"]),
            ("Reading with AI", ["9.5 Summary fidelity", "9.6 AI search and reports", "9.7 Cite what you read"]),
            ("Practice", ["9.8 Lab 9.1 and A6 (Studio)", "Labs 9.2–9.3 (optional)",
                          "Case Study: the Deloitte report"])]
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
        if step == "Verify":
            f.box(xs[i] - 50, y - 20, 100, 40, step, role="highlight", kind="human", thick=True, size=15)
        elif step == "Disclose":
            f.box(xs[i] - 50, y - 17, 100, 34, step, role="neutral", kind="human", dashed=True, size=14)
        else:
            f.text(xs[i], y, step, size=14, color=muted)
        if i < 4:
            f.text((xs[i] + xs[i + 1]) / 2, y, "→", size=14, color=muted)
    f.text(400, 410, "This chapter strengthens Verify (how directly does a source record the claim?), then "
           "Disclose (dashed): cite what you read.", size=13, color=muted, width=780)
    f.text(400, 436, "Opening case: a government report whose references did not hold up (Australia, 2025)",
           size=13, color=muted)


# ---------------------------------------------------------------- F9.2 storyboard (attribution tiers)
def storyboard(f):
    muted, ink = MUTED[f.mode], INK[f.mode]
    ev = [("Dec 2024–Jun 2025", "Deloitte conducts the review (confirmed)", "neutral", "step"),
          ("Aug 14, 2025", "The department publishes the report (confirmed)", "neutral", "step"),
          ("From Aug 2025", "An outside reader reports errors to the media (reported)", "neutral", "human"),
          ("Oct 3, 2025", "Corrected version released; AI use disclosed (confirmed; disclosure reported)",
           "verified", "step"),
          ("Oct 2025", "Final instalment repaid: just over A$97,000 (reported)", "neutral", "step"),
          ("Feb 3, 2026", "Report updated again to address corrections (confirmed)", "verified", "step")]
    f.line(24, 200, 776, 200, color=ink, width=2.4)
    for i, (d, txt, role, kind) in enumerate(ev):
        x = 14 + i * 129
        y = 34 if i % 2 == 0 else 222
        f.box(x, y, 122, 146, d, role=role, kind=kind, size=14, sub=txt, sub_size=13)
        cx = x + 61
        f.line(cx, 180 if i % 2 == 0 else 222, cx, 200, color=ink, width=1.4)
        f.raw(f'<circle cx="{cx}" cy="200" r="5" fill="{ink}"/>')
    f.text(400, 396, "Rounded = a person's action · green = a correction published · confirmed = the department's "
           "own pages · reported = news reports", size=13, color=muted, width=780)
    f.text(400, 440, "Sources: DEWR (2025a, 2025b, 2026); Associated Press (2025); CFO Dive (2025). Whether the AI "
           "tool produced the errors is not on record.", size=13, color=muted, italic=True, width=780)


# ---------------------------------------------------------------- F9.3 source types for one claim
def source_types(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "Source types: what each is good evidence for", size=17, weight="700")
    cols = [("Primary", "the record itself: a study, dataset, law, court record, official page",
             "Good evidence for: what was done, found or decided"),
            ("Secondary", "reports on or interprets primary sources: a review, a textbook, a news story",
             "Good evidence for: what the records add up to, if it cites them"),
            ("Tertiary", "collects and condenses: an encyclopedia, an index, a study guide",
             "Good evidence for: background and where to look next")]
    for i, (h, sub, good) in enumerate(cols):
        x = 20 + i * 260
        f.box(x, 46, 240, 100, h, role="verified" if i == 0 else "neutral", kind="step", size=16, sub=sub,
              sub_size=13)
        f.arrow(x + 120, 148, x + 120, 168)
        f.box(x, 170, 240, 80, good, role="soft", kind="human", size=13, weight="600")
    f.box(20, 290, 500, 84, "Type depends on the claim: the Deloitte report", role="neutral", kind="step",
          size=14, sub="primary for “what the department was told”; secondary for “what the court "
          "said” (the judgment is the record)", sub_size=13)
    f.box(540, 290, 240, 84, "AI output", role="ai", kind="ai", dashed=True, size=15,
          sub="not a source of evidence: a lead", sub_size=13)
    f.text(400, 398, "Gray literature (reports by governments, firms, charities and consultancies) can be any of "
           "the three types; ask who paid for it.", size=13, color=muted, italic=True, width=780)
    f.text(400, 424, "Green = the record itself · rounded = what you can use it for · dashed hexagon = not a source",
           size=13, color=muted)


# ---------------------------------------------------------------- F9.6 vertical vs lateral reading
def lateral(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "Vertical and lateral reading of the same website", size=17, weight="700")
    f.box(14, 168, 150, 92, "An unfamiliar website", role="neutral", kind="step", size=15)
    rows = [(70, [("Stay on the page", "read it carefully", "neutral"),
                  ("Judge it by its looks", "logos, About page, .org, references", "neutral"),
                  ("Often taken in", "historians and students in the study", "risk")]),
            (282, [("Leave within seconds", "open new tabs", "neutral"),
                   ("Ask outside sources", "who is behind it, and who pays?", "neutral"),
                   ("Return with evidence", "fact-checkers: faster, more accurate", "verified")])]
    labels = ["Vertical reading", "Lateral reading"]
    for r, (y, boxes) in enumerate(rows):
        f.text(500, y - 14 if r == 0 else y + 110, labels[r], size=14, weight="700")
        f.arrow(166, 214, 204, y + 46, width=2.0)
        for i, (h, sub, role) in enumerate(boxes):
            x = 206 + i * 196
            f.box(x, y, 176, 92, h, role=role, kind="human", thick=(role == "risk"), size=14, sub=sub,
                  sub_size=13)
            if i < 2:
                f.arrow(x + 178, y + 46, x + 194, y + 46)
    f.text(400, 428, "Rounded = what the reader does · thick (hatched in print) = the risk · green = the better "
           "result", size=13, color=muted)
    f.text(400, 452, "After Wineburg & McGrew (2019): 10 fact-checkers, 10 historians, 25 undergraduates.",
           size=13, color=muted, italic=True)


# ---------------------------------------------------------------- F9.13 research report
def research_report(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "A research report brings more sources, not better ones", size=17, weight="700")
    f.box(20, 50, 200, 80, "Your question", role="neutral", kind="human", size=15)
    f.arrow(222, 90, 286, 90)
    f.box(288, 50, 230, 80, "Many searches", role="ai", kind="ai", size=15, sub="many pages retrieved", sub_size=13)
    f.arrow(520, 90, 576, 90)
    f.box(578, 50, 202, 80, "A long report", role="ai", kind="ai", size=15, sub="dozens of citations", sub_size=13)
    f.line(679, 132, 679, 160)
    f.line(110, 160, 679, 160)
    checks = [("1. Types", "which rungs, for which claims?"), ("2. Support", "does each page say it?"),
              ("3. Missing evidence", "dates, counter-evidence, primary sources"),
              ("4. Faithfulness", "does the synthesis match its sources?")]
    for i, (h, sub) in enumerate(checks):
        x = 20 + i * 195
        f.arrow(x + 90, 160, x + 90, 186)
        f.box(x, 188, 180, 96, h, role="neutral", kind="human", size=15, sub=sub, sub_size=13)
    f.arrow(400, 286, 400, 320)
    f.box(200, 322, 400, 70, "Remaining uncertainty", role="soft", kind="step", dashed=True, size=15,
          sub="what you could not check, and why", sub_size=13)
    f.text(400, 420, "Hexagons = AI steps · rounded = checks you run · dashed = uncertainty", size=13, color=muted)


# ---------------------------------------------------------------- F9.14 what to cite
def what_to_cite(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "What goes in your reference list", size=17, weight="700")
    f.box(40, 48, 270, 136, "Did you open and read the source?", role="neutral", kind="decision", size=14)
    f.arrow(312, 116, 368, 116, label="no", label_dy=-12, size=13)
    f.box(370, 80, 400, 72, "Do not cite it", role="risk", kind="step", thick=True, size=15,
          sub="read it first, or drop the claim", sub_size=13)
    f.arrow(175, 186, 175, 222, label="yes", label_dy=0, size=13)
    f.box(40, 224, 270, 136, "Are you quoting or paraphrasing AI output itself?", role="neutral",
          kind="decision", size=14)
    f.arrow(312, 292, 368, 240, label="no", label_dy=-8, size=13)
    f.box(370, 206, 400, 70, "Cite the source you read", role="verified", kind="step", size=15,
          sub="not the tool that found it", sub_size=13)
    f.arrow(312, 292, 368, 340, label="yes", label_dy=12, size=13)
    f.box(370, 306, 400, 74, "Cite the source, and cite the AI chat", role="verified", kind="step", size=15,
          sub="APA 2025: company, date, chat title, [Generative AI chat], tool, link", sub_size=13)
    f.box(40, 404, 730, 52, "In this course, declare AI use either way (AI Use Declaration, Chapter 1)",
          role="neutral", kind="human", size=14)
    f.text(400, 484, "Diamonds = decisions · thick (hatched in print) = do not · green = cite · rounded = your "
           "declaration", size=13, color=muted)


# ---------------------------------------------------------------- F9.15 A6 sheet
def a6_sheet(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "One A6 source reliability review", size=17, weight="700")
    fields = [("Question, purpose, claim", "the claim you most need to support", "neutral", False),
              ("Source: type and status", "primary/secondary/tertiary; peer-reviewed, preprint, corrected", "neutral",
               False),
              ("Outside-source log", "who is behind it, according to sources it did not write or pay for",
               "neutral", False),
              ("Rung for the claim · rung needed", "with a one-sentence justification", "verified", False),
              ("Use decision", "rely · use with a caveat · only as a lead · do not use", "neutral", False),
              ("Trace", "at least two hops or a dead end; three checks per hop; verdict", "neutral", False),
              ("Fidelity check", "each summary sentence: passage, verdict, drift type", "neutral", False),
              ("References · judgment · declaration", "what you relied on, and what remains uncertain", "soft", True)]
    for i, (h, sub, role, dashed) in enumerate(fields):
        y = 44 + i * 50
        f.box(20, y, 260, 42, h, role=role, kind="human", dashed=dashed, size=14)
        f.text(294, y + 21, sub, size=13, anchor="start", width=490)
    f.text(400, 458, "Rounded = what you write · green = the rung judgment · dashed = remaining uncertainty",
           size=13, color=muted)


# ---------------------------------------------------------------- F9.16 GRADE (Deep)
def grade(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "Rating certainty in a body of evidence (GRADE, simplified)", size=17, weight="700")
    f.box(20, 60, 220, 74, "Randomized trials", role="neutral", kind="step", size=15, sub="start high",
          sub_size=13)
    f.box(20, 160, 220, 74, "Observational studies", role="neutral", kind="step", size=15, sub="start low",
          sub_size=13)
    f.arrow(242, 97, 300, 140)
    f.arrow(242, 197, 300, 160)
    f.box(302, 110, 196, 80, "Certainty rating", role="neutral", kind="human", size=15)
    f.box(530, 46, 250, 104, "Move down", role="risk", kind="step", thick=True, size=15,
          sub="risk of bias, inconsistency, indirectness, imprecision, publication bias", sub_size=13)
    f.box(530, 168, 250, 70, "Move up", role="verified", kind="step", size=15, sub="for example, a very large effect",
          sub_size=13)
    f.arrow(500, 136, 528, 100)
    f.arrow(500, 166, 528, 200)
    f.arrow(400, 192, 400, 276)
    f.box(150, 278, 500, 62, "High · Moderate · Low · Very low", role="soft", kind="step", size=15)
    f.text(400, 372, "Thick (hatched in print) = reasons to lower certainty · green = reasons to raise it",
           size=13, color=muted)
    f.text(400, 396, "Simplified from Guyatt et al. (2008).", size=13, color=muted, italic=True)


# ---------------------------------------------------------------- F9.18 summary card
def summary_card(f):
    f.text(400, 26, "Chapter 9 — what you can do now", size=18, weight="700")
    cards = ["Differentiate: type and status of a source, for one claim",
             "Evaluate: read laterally with outside sources",
             "Place: the rung for the claim, and the rung you need",
             "Trace: follow a claim upstream; name the drift",
             "Judge: check a summary sentence by sentence",
             "Critique AI research reports; cite what you read and declare AI use"]
    for i, c in enumerate(cards):
        x = 20 + (i % 3) * 258
        y = 50 + (i // 3) * 150
        f.box(x, y, 242, 130, c, role="neutral" if i % 2 else "soft", kind="human", size=14, weight="600")


# ---------------------------------------------------------------- reused signatures
FUNNEL_LADDER = verification_funnel(highlight=["check", "primary"],
                                    note="Chapter 9 asks how directly a source at these stages records the claim")
ANATOMY_SUMMARY = llm_anatomy(highlight={"retrieved", "sampling"},
                              note="The summary is new text produced from the pasted original")
DELOITTE_TREE = failure_tree({"hallucination"}, dashed={"hallucination"},
                             tag="Case: Deloitte–DEWR review (2025) · hallucination, inferred (dashed)",
                             note="Incorrect references are confirmed; no record shows they were generated")
DELOITTE_CHAIN = failure_chain(
    notes={0: "Incorrect references reached the published report (confirmed)",
           1: "Two checkpoints, firm and department; what ran is unknown (inferred)",
           2: "Published by the department; recommendations stand (reported)",
           3: "Corrections, partial refund, lost trust (reported)"},
    highlight={1}, dashed={1},
    tag="Tiers: confirmed = the department's pages · reported = news reports · inferred = this book's reading")

FIGS = [
    ("f9-01-chapter-map", chapter_map, 800, 455, "Chapter 9 at a glance"),
    ("f9-02-storyboard", storyboard, 800, 470, "An outside reader, not the firm or the department, reported the errors"),
    ("f9-03-source-types", source_types, 800, 446, "The same document can be primary for one claim and secondary for another"),
    ("f9-04-retellings", RETELLINGS, 800, 356, "Each retelling of a study is a chance for a caveat to drop"),
    ("f9-06-lateral-reading", lateral, 800, 474, "Fact-checkers learned more about a site by leaving it"),
    ("f9-07-goldfish-trace", GOLDFISH, 800, 356, "Following a claim upstream showed that it had no origin"),
    ("f9-08a-funnel-ladder", FUNNEL_LADDER, 800, funnel_height(note=True),
     "The source ladder works inside the funnel's first two stages"),
    ("f9-08b-source-ladder", source_ladder(), 800, ladder_height(),
     "A source's rung depends on how directly it records the claim you need"),
    ("f9-11-anatomy-summary", ANATOMY_SUMMARY, 800, 490, "A summary is generated from the original, not cut out of it"),
    ("f9-13-research-report", research_report, 800, 440, "A research report brings more sources, not better ones"),
    ("f9-14-what-to-cite", what_to_cite, 800, 500, "Cite the source you read, not the tool that found it"),
    ("f9-15-a6-sheet", a6_sheet, 800, 476, "Your review records the evidence behind every rating"),
    ("f9-16-grade", grade, 800, 414, "Certainty in a body of evidence starts from study design and moves up or down"),
    ("f9-18-summary-card", summary_card, 800, 340, "Chapter 9 summary card"),
    ("f9-19-tree-deloitte", DELOITTE_TREE, 800, tree_height() + 34, "Deloitte on the tree: hallucination, inferred"),
    ("f9-20-chain-deloitte", DELOITTE_CHAIN, 800, 420,
     "The errors reached the published report; what checks ran is not on record"),
]

if __name__ == "__main__":
    only = set(sys.argv[1:])
    for fid, fn, w, h, title in FIGS:
        if only and fid not in only:
            continue
        render(fid, fn, w, h, title, ROOT)
        print("rendered", fid)
