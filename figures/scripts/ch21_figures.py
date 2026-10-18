"""Chapter 21 diagrams (SVG, color + gray). Run from the repo root:
    python3 figures/scripts/ch21_figures.py [figure-id ...]

New reusable diagram introduced here (book map: "Personal principles card"; reusable in Chapter 23):

    principles_card(highlight=None, note=None, lines=None, title=None, scope=None,
                    boundaries=None, review=None, notes=None)
        Five shapes (CARD_PARTS) on one card:
          "scope"        rounded (a person's choice): who you are in this code, and the date
          "commitments"  one block with up to seven ruled lines, each "When ..., I ..., because ..."
          "boundaries"   rectangle with a thick border: the rules the code works inside
          "review"       rectangle with a calendar label and a thick top rule: review date and review triggers
          "notes"        rectangle: dated notes ("as of [month year]"), kept apart from the commitments
        lines:      list of up to 7 strings for the commitments block (default: blank template lines)
        highlight:  a part name, "commitment:N" (1-based) or a list -> thick border and the label "this section"
        scope / boundaries / review / notes: replace that box's text
        note:       one line under the card
        No dashed outline is used: in this book a dash means "inferred" (or "reported") only.
        Canvas 800 x CARD_H.

Reused, never redrawn: Signature 7 (`from ch05_figures import delegation_ladder`), the Regulation Map
(`from ch18_figures import regulation_map, MAP_H`), Signature 12 (`from ch20_figures import portfolio_anatomy`,
drawn only when Chapter 20 has coded it). The Final Bridge map follows the layout of ch10's midterm_map, which is
not parametric, so it is written here.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from figlib import render, MUTED, INK  # noqa: E402
from ch05_figures import delegation_ladder  # noqa: E402  (Signature 7, reused)
from ch18_figures import regulation_map, MAP_H  # noqa: E402  (Regulation Map, reused)

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LOOP = ["Frame", "Prompt", "Verify", "Decide", "Disclose"]

CARD_PARTS = ["scope", "commitments", "boundaries", "review", "notes"]


def card_height(lines=None):
    """Canvas height for principles_card with this many commitment lines (default 5)."""
    n = len(lines) if lines else 5
    return 420 + 40 * n


CARD_H = card_height()
BLANK = ["When [a moment I will notice], I [an action I or someone else can trace], because [my evidence]."] * 5


def _set(x):
    if x is None:
        return set()
    if isinstance(x, str):
        return {x}
    return set(x)


# ---------------------------------------------------------------- New reusable diagram: the principles card
def principles_card(highlight=None, note=None, lines=None, title=None, scope=None, boundaries=None,
                    review=None, notes=None):
    hl = _set(highlight)
    lines = list(lines) if lines else list(BLANK)
    if len(lines) > 7:
        raise ValueError("a card holds at most seven commitments")
    bad = {h for h in hl if h not in CARD_PARTS and not h.startswith("commitment:")}
    if bad:
        raise ValueError(f"unknown card part(s): {sorted(bad)}")
    for h in hl:
        if h.startswith("commitment:") and not 1 <= int(h.split(":")[1]) <= len(lines):
            raise ValueError(f"no such commitment: {h}")

    def draw(f):
        muted, ink = MUTED[f.mode], INK[f.mode]
        f.text(400, 22, title or "A personal AI code of practice fits on one card", size=18, weight="700")
        # card outline
        H = card_height(lines)
        f.raw(f'<rect x="20" y="42" width="760" height="{H - 132}" rx="6" fill="none" stroke="{ink}" '
              f'stroke-width="1.2"/>')
        # scope
        on = "scope" in hl
        f.box(40, 56, 720, 52, scope or "Scope: who I am in this code (student in my major, job, freelance, club) · date",
              role="highlight" if on else "neutral", kind="human", thick=on, size=14)
        # commitments block
        on = "commitments" in hl
        top, row = 122, 40
        bh = 34 + row * len(lines)
        f.box(40, top, 720, bh, "", role="neutral", kind="step", thick=on)
        f.text(56, top + 17, "Commitments (5–7, including the four required lines)" +
               ("  · this section" if on else ""), size=14, weight="700", anchor="start")
        for i, ln in enumerate(lines):
            y = top + 34 + i * row
            f.line(52, y, 748, y, color=muted, width=0.8)
            mark = f"commitment:{i + 1}" in hl
            if mark:
                f.raw(f'<rect x="46" y="{y + 2}" width="708" height="{row - 4}" fill="none" stroke="{ink}" '
                      f'stroke-width="3"/>')
            f.text(62, y + row / 2, f"{i + 1}.", size=13, weight="700", anchor="start")
            f.text(84, y + row / 2, ln + ("  ← this line" if mark else ""), size=13, anchor="start")
        y2 = top + bh + 14
        # boundaries (thick border always: it marks the rules around the code)
        on = "boundaries" in hl
        f.box(40, y2, 720, 62, boundaries or "Boundaries: this code works inside [the rules I am under]; where one "
              "is stricter, it wins; when a rule is unclear, I ask [its owner, by role].",
              role="highlight" if on else "neutral", kind="step", thick=True, size=13, weight="normal")
        y3 = y2 + 76
        # review: calendar label + thick top rule (no dashes)
        on = "review" in hl
        f.box(40, y3, 400, 84, "", role="highlight" if on else "neutral", kind="step", thick=on)
        tcol = "#FFFFFF" if on else ink
        f.raw(f'<line x1="40" y1="{y3}" x2="440" y2="{y3}" stroke="{ink}" stroke-width="5"/>')
        f.raw(f'<rect x="52" y="{y3 + 12}" width="34" height="30" rx="3" fill="#FFFFFF" stroke="{ink}" '
              f'stroke-width="1.6"/><line x1="52" y1="{y3 + 20}" x2="86" y2="{y3 + 20}" stroke="{ink}" '
              f'stroke-width="3"/>')
        f.text(100, y3 + 26, "Review", size=14, weight="700", anchor="start", color=tcol)
        f.text(240, y3 + 58, review or "by [date, ≤ 6 months] · review triggers: [two or more]", size=13,
               color=tcol, width=380)
        # dated notes
        on = "notes" in hl
        f.box(456, y3, 304, 84, notes or "Dated notes: tool or rule facts, each \"as of [month year]\"",
              role="highlight" if on else "neutral", kind="step", thick=on, size=13, weight="normal")
        if note:
            f.text(400, H - 62, note, size=13, italic=True, color=muted, width=780)
        f.text(400, H - 30, "Rounded = your choice · thick border = the rules around your code · calendar = a date "
               "you set" + (" · dark fill or \"this section\" = the part discussed" if hl else ""), size=13,
               color=muted, width=780)
    return draw


# ---------------------------------------------------------------- F21.1 chapter map
def chapter_map(f):
    muted = MUTED[f.mode]
    f.text(400, 30, "Chapter 21 at a glance", size=22, weight="700")
    cols = [("Part A: your code", ["21.1 Why a personal code", "21.2 Commitments as triggers",
                                   "21.3 Inside the rules that bind you"]),
            ("Part A, then the brief", ["21.4 How codes age", "21.5 Writing your code (with the brief)",
                                        "Deep 21.A–21.B (optional)"]),
            ("Practice and review", ["Peer check: Lab 20.1, minutes 50–65", "Part B: Case Study, Summary, Last Words",
                                     "Part B: Final Bridge"])]
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
    xs = [215, 330, 440, 550, 662]
    for i, step in enumerate(LOOP):
        if step == "Frame":
            f.box(xs[i] - 50, y - 20, 100, 40, step, role="highlight", kind="human", thick=True, size=15)
        elif step == "Disclose":
            f.box(xs[i] - 58, y - 17, 116, 34, "Disclose (second)", role="neutral", kind="human", size=13)
        else:
            f.text(xs[i], y, step, size=14, color=muted)
        if i < 4:
            f.text((xs[i] + xs[i + 1]) / 2, y, "→", size=14, color=muted)
    f.text(400, 410, "This chapter strengthens Frame (before a task: which of your commitments apply?), then "
           "Disclose (a code is something you can show).", size=13, color=muted, width=780)
    f.text(400, 440, "Read Part A by Tue Apr 27; Part B by Tue May 4. Short case: the ACM Code of Ethics (2018).",
           size=13, weight="700", color=INK[f.mode])


# ---------------------------------------------------------------- F21.2 storyboard (C21)
def storyboard(f):
    muted = MUTED[f.mode]
    f.text(400, 22, "The ACM Code: from the 1992 version to the 2018 update", size=18, weight="700")
    boxes = [("1992", "the code's last update before 2018", False),
             ("2016–2018", "two-year update; drafts published for comment", False),
             ("June 22, 2018", "ACM Council adopts the update", False),
             ("Structure", "principles + guidelines + compliance (Section 4)", False),
             ("Its own limit", "not an algorithm; a basis for judgment", False),
             ("October 2026", "still the current version (page archived Jul 9, 2026)", False)]
    for i, (a, b, dashed) in enumerate(boxes):
        x = 14 + (i % 3) * 262
        y = 52 + (i // 3) * 132
        f.box(x, y, 246, 100, a, role="neutral", kind="step", dashed=dashed, size=16, sub=b, sub_size=13)
        if i % 3 < 2:
            f.arrow(x + 248, y + 50, x + 260, y + 50)
    f.line(659, 154, 659, 168)
    f.line(659, 168, 137, 168)
    f.arrow(137, 168, 137, 182)
    f.text(400, 316, "Sources: ACM's 2018 booklet and July 17, 2018 press release; ACM's code page as archived "
           "July 9, 2026. All boxes rest on ACM's own records.", size=13, color=muted, width=780)
    f.text(400, 342, "About 26 years passed between the two versions.", size=13, weight="700")


# ---------------------------------------------------------------- F21.3 the trigger test
def trigger_test(f):
    muted = MUTED[f.mode]
    f.text(400, 22, "A line becomes a commitment only when it passes three tests", size=18, weight="700")
    f.box(14, 70, 112, 70, "A line in your draft", role="neutral", kind="step", size=14)
    qs = [("Moment?", "would I notice it then, from something I can see?"),
          ("Action?", "can I or someone else trace it afterward?"),
          ("Reason?", "does it point to my own evidence?")]
    for i, (q, s_) in enumerate(qs):
        x = 146 + i * 160
        f.box(x, 50, 140, 110, q, role="neutral", kind="decision", size=15)
        f.text(x + 70, 184, s_, size=13, color=muted, width=150)
        f.arrow(x - 18, 105, x - 2, 105)
        if i:
            f.text(x - 10, 88, "yes", size=13, italic=True, color=muted)
        f.arrow(x + 70, 210, x + 70, 238)
        f.text(x + 84, 224, "no", size=13, italic=True, color=muted, anchor="start")
    f.text(616, 88, "yes", size=13, italic=True, color=muted)
    f.arrow(608, 105, 650, 105)
    f.box(652, 70, 134, 70, "Commitment", role="verified", kind="human", thick=True, size=15)
    f.box(146, 240, 460, 54, "Rewrite: name a visible moment, a trace, or your evidence", role="risk",
          kind="step", thick=True, size=14)
    f.line(146, 267, 70, 267)
    f.arrow(70, 267, 70, 144)
    f.text(400, 326, "A rewritten line takes the test again.", size=13, color=muted, width=780)
    f.text(400, 352, "Rectangle = a step · diamond = a test you apply · rounded = your commitment · thick border "
           "(hatched in print) = rewrite", size=13, color=muted, width=780)


# ---------------------------------------------------------------- F21.9 three shelf lives
def shelf_lives(f):
    muted = MUTED[f.mode]
    f.text(400, 22, "Commitments last for years; tool facts last for months", size=18, weight="700")
    rows = [("Commitments", "years", "\"Before I send anything others will rely on, I check every claim that "
             "carries a number, a name or a date.\"", "verified"),
            ("Practices", "one to two years", "a prompt template, a checklist, a test-input set, a review routine",
             "neutral"),
            ("Tool notes", "months", "which tool, which model, its price, its data terms, a setting: each "
             "\"as of [month year]\"", "soft")]
    for i, (a, life, ex, role) in enumerate(rows):
        y = 52 + i * 92
        f.box(20, y, 190, 76, a, role=role, kind="step", thick=(i == 0), size=16, sub=life, sub_size=13)
        f.box(222, y, 558, 76, ex, role="neutral", kind="step", size=13, weight="normal")
    f.arrow(796, 60, 796, 316)
    f.text(400, 342, "Arrow: faster change. Keep tool facts in dated notes, apart from your commitments. "
           "Source: this book's own dating rule (style sheet §6), not a measured result.", size=13,
           color=muted, width=780)


# ---------------------------------------------------------------- F21.10 review cycle
def review_cycle(f):
    muted = MUTED[f.mode]
    f.text(400, 22, "A review date or a trigger sends you back to your marks before you revise", size=18,
           weight="700", width=780)
    f.box(16, 62, 190, 110, "Review date reached, or a review trigger?", role="neutral", kind="decision", size=13)
    f.arrow(208, 117, 234, 117, label="yes")
    f.box(236, 72, 200, 90, "Reread your marks", role="neutral", kind="step", size=15,
          sub="which triggers fired, which never did", sub_size=13)
    outs = [("Keep", "it fired and held"), ("Revise", "it failed, or a rule changed"),
            ("Retire", "it no longer applies")]
    for i, (a, b) in enumerate(outs):
        y = 44 + i * 74
        f.box(476, y, 176, 64, a, role="neutral", kind="human", size=15, sub=b, sub_size=13)
        f.arrow(438, 117, 474, y + 32)
        f.arrow(654, y + 32, 678, 145)
    f.box(680, 110, 108, 70, "Set the next date", role="verified", kind="human", thick=True, size=14)
    f.line(734, 182, 734, 262)
    f.line(734, 262, 111, 262)
    f.arrow(111, 262, 111, 176)
    f.text(420, 280, "the next date starts the cycle again", size=13, italic=True, color=muted)
    f.text(400, 314, "Review triggers: Chapter 12's re-test triggers (a model update or retirement, a change in "
           "price or terms, a new kind of input, a change of job or school), plus a new rule from someone who "
           "binds you and a failure you met.", size=13, color=muted, width=780)
    f.text(400, 352, "Diamond = a test · rectangle = a step · rounded = your decision", size=13, color=muted)


# ---------------------------------------------------------------- F21.11 professional vs personal code
def two_codes(f):
    muted = MUTED[f.mode]
    f.text(400, 22, "A profession's code and your code do different jobs", size=18, weight="700")
    f.box(200, 46, 290, 50, "A profession's code (e.g., ACM, 2018)", role="neutral", kind="step", size=14)
    f.box(500, 46, 280, 50, "Your personal code", role="neutral", kind="human", thick=True, size=14)
    rows = [("Who writes it", "a professional body, with members' input", "you"),
            ("Whom it binds", "its members (for ACM, every ACM member)", "you, inside the rules that bind you"),
            ("Who enforces it", "the body (ACM's Enforcement Policy)", "you: your marks and your review"),
            ("How it is updated", "rarely, by the body (1992 → 2018)", "at your review date, or on a trigger")]
    for i, (a, b, c) in enumerate(rows):
        y = 122 + i * 52
        f.text(186, y, a, size=14, weight="700", anchor="end")
        f.text(345, y, b, size=13, width=280)
        f.text(640, y, c, size=13, width=270)
        f.line(20, y + 26, 780, y + 26, color=muted, width=0.6)
    f.text(400, 352, "Your code borrows a profession's habit of reasons and revision; it cannot borrow its "
           "enforcement. Rounded, thick = yours.", size=13, color=muted, width=780)


# ---------------------------------------------------------------- F21.13 Final Bridge map
BRIDGE = [("Frame", ["12 (task × tool fit matrix)", "19 (discipline × use heat map)"]),
          ("Prompt", ["15 (data-flow map)"]),
          ("Verify", ["8 (Verification Funnel)", "9 (source ladder)", "16 (Bias Lifecycle)",
                      "11, 12, 14, 20 (second)", "13 (Deep, not examined)", "17 (second; Deep)"]),
          ("Decide", ["11 (proxy-variable trap)", "14 (Agent Loop with Approval Gates)", "18 (Regulation Map)",
                      "8, 10, 15, 16 (second)"]),
          ("Disclose", ["10 (voice spectrum)", "20 (Portfolio Anatomy)", "9, 18, 19 (second)",
                        "17 (Deep, not examined)", "13 (second; Deep)"])]


def final_map(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "Chapters 8–20 on one loop: every step each chapter's map highlighted", size=17, weight="700")
    for i, (step, items) in enumerate(BRIDGE):
        x = 14 + i * 156
        f.box(x, 50, 146, 54, step, role="neutral", kind="human", size=16)
        if i < 4:
            f.arrow(x + 148, 77, x + 156, 77)
        for j, it in enumerate(items):
            f.text(x + 73, 130 + j * 46, it, size=13, width=144,
                   italic=("second" in it or "Deep" in it))
    f.text(400, 468, "Boxes = the AI Work Loop's steps · text = chapters whose Chapter Map highlighted that step, "
           "with their key diagram · italic = a second highlight or a Deep chapter", size=13, color=muted, width=780)
    f.text(400, 506, "Final: Core sections of the whole book, weighted to weeks 9–14. Chapters 13, 17, 22 and 23 "
           "are Deep and not examined.", size=13, weight="700", width=780)


# ---------------------------------------------------------------- F21.14 summary card
def summary_card(f):
    f.text(400, 24, "Chapter 21 in six cards", size=18, weight="700")
    cards = [("From methods to commitments", "keep what your own work showed you need"),
             ("Triggers that pass", "moment · action you can trace · reason"),
             ("Inside the rules", "strictest wins; ask the owner"),
             ("Dated notes apart", "tool facts age in months"),
             ("Review date and triggers", "reread your marks, then revise"),
             ("Your code, your name", "5–7 lines you can defend")]
    for i, (a, b) in enumerate(cards):
        x = 20 + (i % 3) * 260
        y = 50 + (i // 3) * 130
        f.box(x, y, 240, 110, a, role="verified" if i == 5 else "neutral", kind="human" if i == 5 else "step",
              size=15, sub=b, sub_size=13)
    f.text(400, 316, "Rounded = your decision", size=13, color=MUTED[f.mode])


# ---------------------------------------------------------------- instances
HANA_LINES = [
    "Before any AI image generation on a client job, I get written agreement, because of my clause and the bakery job.",
    "Before I upload a drawing to any tool, I check its data terms and log tool and date (two tools' terms differed).",
    "Before I send an invoice, I list any AI use in its notes, because clients already ask me about these tools.",
    "Before contributors' scans go into any AI tool, I check risk and form (Ch. 18 risk sheet: a tool trained on uploads).",
    "Before an image or quotation goes into the zine, I trace it and file the record (a fake \"1890s photo\" once came in).",
]
CARD_BLANK = principles_card(
    note="Blank template: every commitment is written \"When …, I …, because …\".")
CARD_HANA = principles_card(
    lines=HANA_LINES, highlight="commitments", title="Hana's code turns values into triggers for creative work",
    scope="Scope: Hana, freelance illustrator who runs a small zine · constructed example",
    boundaries="Boundaries: my client contracts, the course's zones (§1.5) and the rules of the zine collective I "
               "belong to; where one is stricter, it wins; I ask the client or the collective.",
    review="by the first week of next term · triggers: a new contract, a tool-terms change, a zine form change",
    notes="Dated note: the university-provided tool's terms say prompts are not used to train its foundation models (as of October 2026)",
    note="Constructed example from Hana's details in Chapters 13 and 18; reasons shortened.")
MARCUS_LINES = [
    "Before I paste or upload anything into an AI tool, I check it holds no information about a patient, even unnamed.",
    "When I build study material with AI, I use only my textbook and my own notes, and mark the file \"own sources\".",
    "When I catch myself typing \"just tell me\" in a study session, I stop and note it in my study log.",
    "Before I rely on a drug fact from an AI tool, I check it in my course's drug reference and note the page.",
    "When I submit coursework, my declaration lists every AI use, checked against my session history.",
]
CARD_MARCUS = principles_card(
    lines=MARCUS_LINES, highlight="boundaries", title="Marcus's patient line is stricter than any rule he is under",
    scope="Scope: Marcus, nursing student, clinical placement and night shifts · constructed example",
    boundaries="Boundaries: the course's zones (§1.5), the university's data rules, my placement site's rules; "
               "where one is stricter, it wins; when unclear, I ask my clinical instructor.",
    review="by the start of my next placement · triggers: a new site's rules, a new tool, a mistake I make",
    notes="Dated note: the university provides Microsoft Copilot Chat to all students (as of October 2026)",
    note="Constructed example; reasons are on Marcus's full page. Line 1 is stricter than any rule he is under.")
LADDER_CODE = delegation_ladder(
    highlight="agency",
    annotate={"agency": "my trigger: before a tool I set up acts for others, a person sees each consequential action"},
    note="A commitment for the top rung: an approval gate before consequential actions (Chapter 14).")
MAP_CODE = regulation_map(
    highlight=["contract", "org", "terms"],
    notes={"contract": "client clause: written OK first", "org": "course zones (§1.5) + Hana's code",
           "terms": "tool terms (see Hana's dated note)"},
    title="Hana's code sits inside the rules nearest them",
    note="Strictest rule wins; ask its owner (section 18.1). As of October 2026 · not legal advice.")

FIGS = [
    ("f21-01-chapter-map", chapter_map, 800, 460, "Chapter 21 at a glance"),
    ("f21-02-storyboard", storyboard, 800, 360,
     "A profession's code waited about 26 years for an update, and still asks for judgment"),
    ("f21-04-trigger-test", trigger_test, 800, 372, "A line becomes a commitment only when it passes three tests"),
    ("f21-11-principles-card", CARD_BLANK, 800, card_height(),
     "A code fits on one card: scope, a few commitments, boundaries, a review date and dated notes"),
    ("f21-05-card-hana", CARD_HANA, 800, card_height(HANA_LINES), "Hana's code turns values into triggers for creative work"),
    ("f21-06-ladder-code", LADDER_CODE, 800, 590,
     "At the agency rung, a commitment puts a person before consequential actions"),
    ("f21-07-map-code", MAP_CODE, 800, MAP_H, "Your code sits inside the rules nearest you; a stricter rule wins"),
    ("f21-08-card-marcus", CARD_MARCUS, 800, card_height(MARCUS_LINES), "Marcus's patient line is stricter than any rule he is under"),
    ("f21-09-shelf-lives", shelf_lives, 800, 362, "Commitments last for years; tool facts last for months"),
    ("f21-10-review-cycle", review_cycle, 800, 366,
     "A review date or a trigger sends you back to your marks before you revise"),
    ("f21-03-two-codes", two_codes, 800, 366, "A profession's code and your code do different jobs"),
    ("f21-14-final-map", final_map, 800, 526, "Chapters 8–20 on one loop: where each chapter's map put its weight"),
    ("f21-13-summary-card", summary_card, 800, 330, "Chapter 21 summary card"),
]


def portfolio_fig():
    """F21.12: Signature 12 reuse. Drawn only if Chapter 20 has coded portfolio_anatomy."""
    try:
        from ch20_figures import portfolio_anatomy  # noqa: E402
    except Exception as exc:  # noqa: BLE001
        print("skipped f21-12-portfolio-code: ch20_figures.portfolio_anatomy not available yet ("
              + type(exc).__name__ + ")")
        return None
    return portfolio_anatomy(highlight="code",
                             note="Your code sits beside your reflection, below the entries and their declarations; "
                                  "the defense may ask about one line.")


if __name__ == "__main__":
    only = set(sys.argv[1:])
    for fid, fn, w, h, title in FIGS:
        if only and fid not in only:
            continue
        render(fid, fn, w, h, title, ROOT)
        print("rendered", fid)
    if not only or "f21-12-portfolio-code" in only:
        pf = portfolio_fig()
        if pf is not None:
            try:
                from ch20_figures import PORTFOLIO_H as PH  # noqa: E402
            except Exception:  # noqa: BLE001
                PH = 620
            render("f21-12-portfolio-code", pf, 800, PH, "Your code sits in the portfolio beside your reflection",
                   ROOT)
            print("rendered f21-12-portfolio-code")
