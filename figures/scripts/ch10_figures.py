"""Chapter 10 diagrams (SVG, color + gray). Run from the repo root:
    python3 figures/scripts/ch10_figures.py
Data and computed charts (F10.10, F10.15) are in ch10_charts.py (data/ch10_liang2023.csv,
data/ch10_detector_baserate.csv).

New reusable drawing introduced here (book-map "Voice and ownership spectrum"; for Chapters 20 and 21):
    voice_spectrum(highlight=None, marks=None, band=None, note=None)

Reused, never redrawn: Signature 6 (`from ch05_figures import prompt_anatomy`), Signature 8
(`from ch08_figures import verification_funnel, funnel_height`), Signature 5 and the chain
(`from ch04_figures import failure_tree, failure_chain, tree_height`). The chapter map and the Midterm Bridge
map use the same Work Loop strip as the Chapter 2–9 maps.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from figlib import render, MUTED, INK, ROLES  # noqa: E402
from ch04_figures import failure_tree, failure_chain, tree_height  # noqa: E402
from ch05_figures import prompt_anatomy  # noqa: E402
from ch08_figures import verification_funnel, funnel_height  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LOOP = ["Frame", "Prompt", "Verify", "Decide", "Disclose"]


def _as_set(x):
    if x is None:
        return set()
    if isinstance(x, (int, str)):
        return {x}
    return set(x)


# ---------------------------------------------------------------- the voice and ownership spectrum (new)
POSITIONS = {  # position: (label, sub, share of wording the tool supplies, as a fraction for the inner bar)
    1: ("1 · Your words only", "no AI", 0.0),
    2: ("2 · AI as reader", "comments; you change it", 0.08),
    3: ("3 · AI as editor", "grammar, rewording or translation", 0.35),
    4: ("4 · AI as co-drafter", "drafts from your points; you rewrite", 0.68),
    5: ("5 · AI as author", "sent as is", 0.95),
}
BANDS = {"own": ("Own words expected", "apology · message after a loss · personal statement · reference letter · "
                 "reflection essay"),
         "accuracy": ("Accuracy and clarity first", "meeting summary · FAQ answer · routine notice · status update")}
P_X0, P_W, P_GAP, P_Y, P_H = 22, 140, 12, 118, 152


def spectrum_height(note=None, marks=None):
    return 506 + (20 if note else 0)


def voice_spectrum(highlight=None, marks=None, band=None, note=None):
    """The voice and ownership spectrum (7 boxes: five positions + two reader bands).

    One axis: the share of the WORDING a tool supplies (not the worth of the message, not who owns it).
    highlight: a position number (1-5) or a list; thick border, dark fill.
    marks:     {(first, last): label} draws a dashed bracket over those positions (an inferred placement),
               e.g. {(4, 5): "Peabody email (2023), inferred"}; a single position may be given as (n, n).
    band:      "own" or "accuracy" to highlight one reader band.
    note:      one-line italic remark under the title.
    Inside each position a small bar shows the tool's share of the wording; the label says it in words,
    so meaning never rests on the bar or on color.
    """
    hl = _as_set(highlight)
    marks = marks or {}
    if hl - set(POSITIONS):
        raise ValueError(f"unknown position(s): {sorted(hl - set(POSITIONS))}")
    if band not in (None, "own", "accuracy"):
        raise ValueError("band must be None, 'own' or 'accuracy'")

    def draw(f):
        ink, muted = INK[f.mode], MUTED[f.mode]
        ai_fill, ai_stroke, _ = ROLES[f.mode]["ai"]
        f.text(400, 24, "The voice and ownership spectrum", size=18, weight="700")
        y0 = 0
        if note:
            f.text(400, 46, note, size=13, italic=True, color=muted, width=760)
            y0 = 20
        # axis
        f.arrow(40, 70 + y0, 760, 70 + y0, width=2.2)
        f.text(40, 52 + y0, "More of the wording supplied by a tool", size=13, weight="700", anchor="start")
        f.text(760, 88 + y0, "so more of your judgment is needed to keep the message yours", size=13,
               anchor="end", color=muted)
        py = P_Y + y0 + (28 if marks else 0)
        xs = {}
        for i, (pos, (lab, sub, share)) in enumerate(POSITIONS.items()):
            x = P_X0 + i * (P_W + P_GAP)
            xs[pos] = x
            on = pos in hl
            role = "highlight" if on else "neutral"
            tc = ROLES[f.mode][role][2]
            f.box(x, py, P_W, P_H, "", role=role, kind="human", thick=on)
            f.text(x + P_W / 2, py + 34, lab, size=14, weight="600", color=tc, width=P_W * 0.86)
            f.text(x + P_W / 2, py + 86, sub, size=13, color=tc, width=P_W * 0.86)
            # inner share bar (outline always drawn; filled part = the tool's share)
            bx, by, bw, bh = x + 14, py + P_H - 20, P_W - 28, 10
            f.raw(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" fill="#FFFFFF" stroke="{ink}" '
                  f'stroke-width="1"/>')
            if share:
                f.raw(f'<rect x="{bx}" y="{by}" width="{bw * share:.1f}" height="{bh}" fill="{ai_fill}" '
                      f'stroke="{ai_stroke}" stroke-width="1"/>')
        # marks: dashed brackets above positions
        for (a, b), lab in marks.items():
            xa, xb = xs[a] - 4, xs[b] + P_W + 4
            yb = py - 12
            f.line(xa, yb, xb, yb, dashed=True, width=2.2)
            f.line(xa, yb, xa, yb + 8, dashed=False, width=2.2)
            f.line(xb, yb, xb, yb + 8, dashed=False, width=2.2)
            f.text((xa + xb) / 2, yb - 12, lab, size=13, weight="700")
        # reader bands
        ty = py + P_H + 34
        f.text(400, ty - 14, "Which position fits depends on what these readers expect:", size=13, color=muted)
        for j, key in enumerate(("own", "accuracy")):
            lab, sub = BANDS[key]
            x = 22 + j * 384
            on = band == key
            f.box(x, ty, 372, 82, lab, role="highlight" if on else "soft", kind="human", thick=on, size=15,
                  sub=sub, sub_size=13)
        f.line(400, ty - 4, 400, ty + 86, dashed=True, width=1.6)
        f.text(400, ty + 112, "Rounded = your decisions · inner bar and label = how much wording the tool "
               "supplies · thick = highlighted · dashed bracket = an inferred placement", size=13,
               color=muted, width=780)
    return draw


# ---------------------------------------------------------------- shared Work Loop strip
def _loop_strip(f, y, main, second, caption):
    muted = MUTED[f.mode]
    f.text(150, y, "AI Work Loop:", size=14, weight="700", anchor="end")
    xs = [205, 300, 420, 540, 640]
    for i, step in enumerate(LOOP):
        if step == main:
            f.box(xs[i] - 50, y - 20, 100, 40, step, role="highlight", kind="human", thick=True, size=15)
        elif step == second:
            f.box(xs[i] - 50, y - 17, 100, 34, step, role="neutral", kind="human", dashed=True, size=14)
        else:
            f.text(xs[i], y, step, size=14, color=muted)
        if i < 4:
            f.text((xs[i] + xs[i + 1]) / 2, y, "→", size=14, color=muted)
    f.text(400, y + 38, caption, size=13, color=muted, width=780)


# ---------------------------------------------------------------- F10.1 chapter map
def chapter_map(f):
    muted = MUTED[f.mode]
    f.text(400, 30, "Chapter 10 at a glance", size=22, weight="700")
    cols = [("Your voice", ["10.1 Voice, ownership, readers", "10.2 The spectrum", "10.3–10.4 Your points first; "
                                                                                   "AI's pull"]),
            ("Judging and disclosing", ["10.5 Keep, rewrite or reject", "10.6 Detectors and process evidence",
                                        "10.7 Disclosure at work"]),
            ("Practice", ["10.8 Lab 10.1 and A7 (Studio)", "Labs 10.2–10.3 (optional)",
                          "Case Study: the Peabody message"])]
    for c, (head, items) in enumerate(cols):
        x = 30 + c * 255
        f.text(x + 115, 74, head, size=16, weight="700")
        for i, it in enumerate(items):
            role = "neutral" if c < 2 else ("verified" if i == 0 else "soft")
            kind = "human" if c == 2 else "step"
            f.box(x, 94 + i * 88, 230, 70, it, role=role, kind=kind, dashed=(c == 2 and i == 1), size=14)
        if c < 2:
            f.arrow(x + 236, 217, x + 252, 217)
    _loop_strip(f, 372, "Disclose", "Decide",
                "This chapter strengthens Disclose (who needs to know how the message was made?), then Decide "
                "(dashed): does each sentence deserve your name?")
    f.text(400, 440, "Opening case: a university office's message after a campus shooting, drafted with ChatGPT "
           "(2023)", size=13, color=muted)


# ---------------------------------------------------------------- F10.2 storyboard (attribution tiers)
def storyboard(f):
    muted, ink = MUTED[f.mode], INK[f.mode]
    ev = [("Feb 13, 2023", "Shooting at Michigan State: three students killed (reported)", "risk", "step"),
          ("Feb 16", "Office emails the Peabody community; last line credits ChatGPT (confirmed)", "ai", "step"),
          ("Feb 17", "Student newspaper reports; the associate dean apologizes (reported)", "neutral", "human"),
          ("Feb 18", "Dean: review layers were skipped; a review opens; two deans step back", "neutral", "human"),
          ("Apr 11", "The two deans return to their roles (reported)", "soft", "step")]
    f.line(24, 200, 776, 200, color=ink, width=2.4)
    for i, (d, txt, role, kind) in enumerate(ev):
        x = 20 + i * 154
        y = 34 if i % 2 == 0 else 222
        f.box(x, y, 144, 146, d, role=role, kind=kind, size=14, sub=txt, sub_size=13)
        cx = x + 72
        f.line(cx, 180 if i % 2 == 0 else 222, cx, 200, color=ink, width=1.4)
        f.raw(f'<circle cx="{cx}" cy="200" r="5" fill="{ink}"/>')
    f.text(400, 396, "Yellow = the AI-drafted message · rounded = people's actions · thick (hatched in print) = "
           "the tragedy · confirmed = the emails as quoted · reported = news reports", size=13, color=muted,
           width=780)
    f.text(400, 440, "Sources: Perrotta (2023); Lele (2023); Lele & Faquih (2023); Korn (2023); NPR (2023). What "
           "readers expected, and how much the office changed the output, are inferred.", size=13,
           color=muted, italic=True, width=780)


# ---------------------------------------------------------------- F10.5 one message, three tones
TONES = [("Formal", "Dear [Coordinator], I am writing to inform you that I am unable to lead Thursday's 4 p.m. "
                    "session, as my examination has been rescheduled. I apologize for the short notice. Would "
                    "Friday at 2 p.m. or Monday at 4 p.m. be suitable? I will notify the students. The materials "
                    "are in the shared folder.",
          "markers: \"I am writing to inform you\" · \"unable\" · \"suitable\""),
         ("Warm", "Hi [Coordinator], I'm so sorry to do this on short notice: my stats exam moved to Thursday at "
                  "4, so I can't lead that session. I completely understand if this causes inconvenience. Could "
                  "we try Friday at 2 or Monday at 4? I'm happy to tell [STUDENTS] myself. Everything is in the "
                  "shared folder.",
          "markers: \"I'm so sorry\" · \"happy to\" · contractions"),
         ("Brief", "Hi [Coordinator], my exam moved, so I can't lead Thursday 4 p.m. Sorry for the late notice. "
                   "Friday 2 p.m. or Monday 4 p.m.? I'll tell the students. Materials are in the shared folder.",
          "markers: short sentences · no extra courtesy")]


def three_tones(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "Elif's five points, three tones (constructed example)", size=17, weight="700")
    for i, (tone, body, markers) in enumerate(TONES):
        x = 20 + i * 258
        f.box(x, 46, 242, 40, tone, role="highlight" if tone == "Warm" else "neutral", kind="step",
              thick=(tone == "Warm"), size=15)
        f.box(x, 92, 242, 250, "", role="ai", kind="step", size=13)
        f.text(x + 121, 216, body, size=13, width=222, weight="normal")
        f.text(x + 121, 370, markers, size=13, width=230, italic=True, color=muted)
    f.text(400, 414, "Yellow cards = tool outputs · the same five points in each · thick = the version Elif chose "
           "to edit (she cut the \"completely understand\" sentence and added her own thanks)", size=13,
           color=muted, width=780)


# ---------------------------------------------------------------- F10.6 pull toward common phrasing
def pull(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "AI suggestions can pull different writers toward the same phrasing", size=17, weight="700")
    writers = [("Writer A", "a specific example from home"), ("Writer B", "a hedge: \"I think\""),
               ("Writer C", "a local turn of phrase"), ("Writer D", "an exact number")]
    for i, (w, sub) in enumerate(writers):
        y = 52 + i * 92
        f.box(20, y, 210, 78, w, role="neutral", kind="human", size=15, sub=sub, sub_size=13)
        f.arrow(232, y + 39, 318, 220)
    f.box(322, 176, 170, 88, "AI suggestions", role="ai", kind="ai", size=15, sub="likely, common wording",
          sub_size=13)
    f.arrow(494, 220, 538, 220)
    f.box(542, 150, 236, 140, "Drafts that sound more alike", role="soft", kind="step", size=15,
          sub="fewer specifics, fewer hedges, more stock phrases", sub_size=13)
    f.text(660, 354, "Studies: stories with AI ideas were more alike (Doshi & Hauser, 2024); autocomplete moved "
           "Indian participants toward Western styles (Agarwal et al., 2025).", size=13, width=250, italic=True,
           color=muted)
    f.text(400, 434, "Rounded = writers · hexagon = AI · grammar checkers were not tested: that they also pull "
           "is this book's inference", size=13, color=muted, width=780)


# ---------------------------------------------------------------- F10.7 keep, rewrite or reject
def keep_rewrite_reject(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "One sentence at a time: keep, rewrite or reject", size=17, weight="700")
    f.box(60, 44, 220, 44, "A sentence in the draft", role="ai", kind="ai", size=14)
    qs = [("True? Facts go through the funnel", "no", "Reject or fix", "tag: accuracy", "risk"),
          ("Says what I mean, in my voice?", "no", "Rewrite", "tag: voice", "neutral"),
          ("Right for this reader?", "no", "Rewrite", "tag: audience and tone", "neutral"),
          ("Can I stand behind it? Safe to share?", "no", "Reject", "tags: commitment, privacy", "risk")]
    f.arrow(170, 90, 170, 104)
    for i, (q, lab, out, tag, role) in enumerate(qs):
        y = 106 + i * 98
        f.box(40, y, 260, 88, q, role="neutral", kind="decision", size=13)
        f.arrow(302, y + 44, 470, y + 44, label=lab, label_dy=-12, size=13)
        f.box(474, y + 14, 300, 60, out, role=role, kind="step", thick=(role == "risk"), size=15, sub=tag,
              sub_size=13)
        if i < 3:
            f.arrow(170, y + 90, 170, y + 104)
            f.text(182, y + 97, "yes", size=13, italic=True, color=muted, anchor="start")
    f.arrow(170, 106 + 3 * 98 + 90, 170, 512)
    f.text(182, 503, "yes", size=13, italic=True, color=muted, anchor="start")
    f.box(60, 514, 220, 40, "Keep", role="verified", kind="step", size=15)
    f.text(560, 534, "Record the code and the tag (annotated draft)", size=13, color=muted, width=420)
    f.text(400, 574, "Diamonds = your decisions · thick (hatched in print) = reject · green = keep", size=13,
           color=muted)


# ---------------------------------------------------------------- F10.9 A7 sheet
def a7_sheet(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "One A7 annotated draft and revision trace", size=17, weight="700")
    fields = [("Context card", "document · reader · purpose · stakes · own words expected? · target position",
               "neutral", False),
              ("v0 (before any AI)", "your notes or first draft, dated", "verified", False),
              ("Prompts", "parts labeled · tool · date · at least one iteration", "neutral", False),
              ("Annotation row", "sentence · K / R / X · tag (voice, accuracy, audience and tone, commitment, "
                                 "privacy) · why", "neutral", False),
              ("Fact-check row", "claim · source opened · verdict on the Chapter 8 scale", "neutral", False),
              ("Trace row", "v0 → v1 → v2 · who or what proposed it · why kept or changed", "neutral", False),
              ("Reflection", "where your voice is · one rejected change · one thing you would not delegate",
               "soft", False),
              ("Declaration", "five elements, with the disclosure decision inside", "soft", True)]
    for i, (h, sub, role, dashed) in enumerate(fields):
        y = 44 + i * 50
        f.box(20, y, 240, 42, h, role=role, kind="human", dashed=dashed, size=14)
        f.text(274, y + 21, sub, size=13, anchor="start", width=510)
    f.text(400, 458, "Rounded = what you write · green = written before any AI · dashed = what you tell your "
           "readers", size=13, color=muted)


# ---------------------------------------------------------------- F10.11 score vs process evidence
def score_vs_process(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "What a detector score can show, and what process evidence shows", size=17, weight="700")
    f.box(30, 52, 340, 66, "A detector score", role="ai", kind="ai", size=16, sub="a number about the text",
          sub_size=13)
    f.box(30, 136, 340, 90, "Rests on how predictable the words are", role="neutral", kind="step", size=14,
          sub="simple, common wording scores as \"AI-like\"", sub_size=13)
    f.box(30, 244, 340, 90, "Cannot show who wrote it, or how", role="risk", kind="step", thick=True, size=14,
          sub="false positives fell hardest on non-native writers in a 2023 test", sub_size=13)
    f.box(430, 52, 340, 66, "Process evidence", role="human", kind="human", size=16,
          sub="a record of how you wrote", sub_size=13)
    f.box(430, 136, 340, 60, "Notes and earlier drafts, dated", role="verified", kind="human", size=14)
    f.box(430, 206, 340, 60, "Version history and revision trace", role="verified", kind="human", size=14)
    f.box(430, 276, 340, 60, "Your declaration, and explaining your choices", role="verified", kind="human",
          size=14)
    f.text(400, 372, "Hexagon = a tool's output · thick (hatched in print) = its limit · rounded green = records "
           "you keep", size=13, color=muted)
    f.text(400, 398, "Sources: Liang et al. (2023); Weber-Wulff et al. (2023); OpenAI (2023, classifier "
           "withdrawn for low accuracy, as reported).", size=13, color=muted, italic=True, width=780)


# ---------------------------------------------------------------- F10.12 disclosure decision
def disclosure(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "Should you disclose AI use in this message?", size=17, weight="700")
    qs = ["Does a rule require it? (course, employer, client, profession)",
          "Do these readers expect your own words?",
          "Would a reasonable reader feel misled later?"]
    for i, q in enumerate(qs):
        y = 48 + i * 112
        f.box(30, y, 300, 100, q, role="neutral", kind="decision", size=13)
        f.arrow(332, y + 50, 420, 160)
        f.text(346, y + (36 if i == 0 else 64), "yes", size=13, italic=True, color=muted, anchor="start")
        if i < 2:
            f.arrow(180, y + 102, 180, y + 110, label=None)
            f.text(196, y + 106, "no", size=13, italic=True, color=muted, anchor="start")
    f.box(424, 92, 352, 136, "Disclose, where readers will see it", role="verified", kind="step", size=15,
          sub="a line in the message · a note to your manager · a project log · the course declaration · a "
              "citation for quoted AI output (Ch. 9)", sub_size=13)
    f.arrow(180, 374, 180, 404)
    f.text(196, 394, "no to all", size=13, italic=True, color=muted, anchor="start")
    f.box(30, 406, 300, 56, "No line needed; keep your record", role="soft", kind="step", size=14)
    f.box(424, 290, 352, 124, "The sender answers either way", role="highlight", kind="human",
          thick=True, size=15, sub="a label tells readers how a message was made, not who checks it (Moffatt, "
                                   "paras. 27–28; this book's reading)", sub_size=13)
    f.text(400, 494, "Diamonds = your decisions · green = disclose · thick = always true", size=13, color=muted)


# ---------------------------------------------------------------- F10.16 AI-mediated communication (Deep)
def ai_mc(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "AI-mediated communication", size=17, weight="700")
    f.box(20, 90, 190, 90, "Sender", role="human", kind="human", size=16, sub="decides what to say",
          sub_size=13)
    f.arrow(212, 135, 290, 135)
    f.box(294, 82, 212, 106, "AI software", role="ai", kind="ai", size=15, sub="changes · adds to · generates",
          sub_size=13)
    f.arrow(508, 135, 586, 135)
    f.box(590, 90, 190, 90, "Receiver", role="human", kind="human", size=16, sub="reads the message",
          sub_size=13)
    f.arrow(684, 184, 116, 184, dashed=True, curve=-60, label="infers the sender's effort and sincerity",
            label_dy=56, size=13)
    f.text(400, 296, "Examples: autocorrect · suggested replies · tone rewriters · drafting assistants", size=13,
           color=muted)
    f.text(400, 322, "Definition after Hancock, Naaman & Levy (2020) · rounded = people · hexagon = AI · dashed = "
           "an inference", size=13, color=muted, width=780)


# ---------------------------------------------------------------- F10.17 Midterm Bridge map
BRIDGE = [("Frame", ["Ch. 1 Work Loop; Jagged Frontier", "Ch. 5 Delegation Ladder", "Ch. 7 scaffold vs. crutch"]),
          ("Prompt", ["Ch. 3 Anatomy of an LLM Response", "Ch. 5 Anatomy of a Prompt",
                      "Ch. 6 context layers (Deep, not examined)"]),
          ("Verify", ["Ch. 2 Data-to-Prediction Pipeline", "Ch. 4 Failure Tree and chain", "Ch. 7 closed-book check",
                      "Ch. 8 Verification Funnel", "Ch. 9 source ladder"]),
          ("Decide", ["Ch. 10 keep, rewrite or reject"]),
          ("Disclose", ["Ch. 10 voice spectrum; disclosure", "Ch. 9 cite what you read (second)"])]


def midterm_map(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "Chapters 1–10 on one loop: the step each chapter's map highlighted", size=17, weight="700")
    for i, (step, items) in enumerate(BRIDGE):
        x = 14 + i * 156
        f.box(x, 50, 146, 54, step, role="highlight" if step in ("Decide", "Disclose") else "neutral",
              kind="human", thick=step in ("Decide", "Disclose"), size=16)
        if i < 4:
            f.arrow(x + 148, 77, x + 156, 77)
        for j, it in enumerate(items):
            f.text(x + 73, 134 + j * 56, it, size=13, width=144, italic=it.endswith("examined)"))
    f.text(400, 432, "Boxes = the AI Work Loop's steps · text = chapters whose Chapter Map highlighted that step, "
           "with their key diagram · thick = this chapter", size=13, color=muted, width=780)
    f.text(400, 470, "Midterm: Core sections of Chapters 1–10. Chapter 6 is Deep and not examined.", size=13,
           weight="700")


# ---------------------------------------------------------------- F10.18 summary card
def summary_card(f):
    f.text(400, 26, "Chapter 10 — what you can do now", size=18, weight="700")
    cards = ["Classify: a writing use on the spectrum, for these readers, in the course's zones",
             "Frame: your points first; name the reader and the tone",
             "Judge: keep, rewrite or reject each sentence, with a tag",
             "Check: facts in the draft through the funnel",
             "Explain: why a detector score is weak; keep process evidence",
             "Decide: disclose where expected; the sender answers either way"]
    for i, c in enumerate(cards):
        x = 20 + (i % 3) * 258
        y = 50 + (i // 3) * 150
        f.box(x, y, 242, 130, c, role="neutral" if i % 2 else "soft", kind="human", size=14, weight="600")


# ---------------------------------------------------------------- reused signatures and case labels
SPECTRUM = voice_spectrum()
SPECTRUM_PEABODY = voice_spectrum(marks={(4, 5): "Peabody email (2023): position 4 or 5, inferred"}, band="own",
                                  note="Readers expected the office's own words (inferred)")
PROMPT_WRITING = prompt_anatomy(highlight=["role", "context", "constraints"],
                                note="For writing: name the reader and the tone; put your own points in the context")
FUNNEL_DRAFT = verification_funnel(highlight=["claims", "check"],
                                   note="Facts in your draft: names, dates, numbers, policies")
PEABODY_CHAIN = failure_chain(
    notes={0: "One wrong detail: \"shootings\" for one (reported)",
           1: "Inappropriate delegation; review skipped (documented)",
           2: "Sent to the Peabody community",
           3: "Hurt and lost trust; deans step back (reported)"},
    highlight={1},
    tag="Peabody email (2023) · primary label: chain link 2, inappropriate delegation and skipped review "
        "(documented by the dean's statement)")
PEABODY_TREE = failure_tree({"hallucination"}, dashed={"hallucination"},
                            tag="Case: Peabody email (2023) · secondary label: hallucination, inferred (dashed)",
                            note="The wrong detail is reported; whether the tool produced it is not on record")

FIGS = [
    ("f10-01-chapter-map", chapter_map, 800, 455, "Chapter 10 at a glance"),
    ("f10-02-storyboard", storyboard, 800, 470,
     "The message disclosed its AI help; the failure was the delegation and the review that did not happen"),
    ("f10-03-voice-spectrum", SPECTRUM, 800, spectrum_height(),
     "The more wording a tool supplies, the more of your judgment the message needs to stay yours"),
    ("f10-03b-spectrum-peabody", SPECTRUM_PEABODY, 800, spectrum_height(note=True) + 28,
     "The Peabody message sat near the far end for readers who expected the office's own words"),
    ("f10-04-prompt-writing", PROMPT_WRITING, 800, 500,
     "For writing, name the reader and the tone, and put your own points in the context"),
    ("f10-05-three-tones", three_tones, 800, 446, "The same five points can arrive in three tones"),
    ("f10-06-pull", pull, 800, 456, "AI suggestions can pull different writers toward the same phrasing"),
    ("f10-07-keep-rewrite-reject", keep_rewrite_reject, 800, 592, "Every sentence earns its place: keep, rewrite "
                                                                   "or reject"),
    ("f10-08-funnel-draft", FUNNEL_DRAFT, 800, funnel_height(note=True),
     "Facts in a draft go through the same funnel as any claim"),
    ("f10-09-a7-sheet", a7_sheet, 800, 476, "Your annotations and trace make your judgment visible"),
    ("f10-11-score-vs-process", score_vs_process, 800, 420,
     "A detector score is a guess about a text; process evidence shows how it was made"),
    ("f10-12-disclosure", disclosure, 800, 512,
     "Disclose when a rule, the reader or fairness asks for it; the sender answers for the message either way"),
    ("f10-13-chain-peabody", PEABODY_CHAIN, 800, 420, "The failure sits on the chain: a delegation nobody reviewed"),
    ("f10-14-tree-peabody", PEABODY_TREE, 800, tree_height() + 34,
     "The one wrong detail is a hallucination only if the tool produced it, which is inferred"),
    ("f10-16-ai-mc", ai_mc, 800, 344, "In AI-mediated communication, software changes the message between two "
                                      "people"),
    ("f10-17-midterm-map", midterm_map, 800, 490, "Chapters 1–10 on one loop: where each chapter's map put its "
                                                  "weight"),
    ("f10-18-summary-card", summary_card, 800, 340, "Chapter 10 summary card"),
]

if __name__ == "__main__":
    only = set(sys.argv[1:])
    for fid, fn, w, h, title in FIGS:
        if only and fid not in only:
            continue
        render(fid, fn, w, h, title, ROOT)
        print("rendered", fid)
