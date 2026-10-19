"""Chapter 22 diagrams (SVG, color + gray). Run from the repo root:
    python3 figures/scripts/ch22_figures.py
Data charts are in ch22_charts.py (data/ch22_*.csv).

New signature introduced here (book map: "Capability timeline (rewritten each edition)"):

    from ch22_figures import capability_timeline, timeline_height
    capability_timeline(highlight=None, note=None, events=None, as_of="October 2026", title=None,
                        start=None, end=None)

  Events come from data/ch22_timeline.csv (id, date, label, status, who, section, aged, as_of, tag) unless
  `events` (a list of dicts with the same keys) is passed. The optional `tag` column replaces the status word
  in the box's tag text (e.g. "outside estimate", drawn with the measured mark); the mark follows `status`. At most 9 event boxes; the legend does not count.
  Boxes are placed in date order on two rows (above and below a year axis); a leader line joins each box to
  its date on the axis; a labeled vertical line marks the as-of date.
  Evidence status by tag text and marks, never by color alone:
    measured  = solid rectangle, filled corner square, tag "measured: <who>"
    reported  = solid rectangle, open corner square,   tag "reported: <who>"
    forecast  = light fill, placed right of the as-of line, arrow mark, tag "forecast: <who>" (never dashed,
                never hatched: hatch is the gray risk pattern)
    inferred  = dashed outline (the book's inference; dashes mean only this, book-wide)
    aged      = folded top-left corner and the word "aged" in the tag
    highlight = role "highlight" + thick border (as work_loop)
  Next edition: edit the CSV, not the function.

Reused, never redrawn: Signature 1 strip (chapter map), Signature 9 (`from ch14_figures import agent_loop,
LOOP_H`), the modality lanes (`from ch13_figures import modality_tokens`), Signature 8
(`from ch08_figures import verification_funnel, funnel_height`), the failure-to-harm chain
(`from ch04_figures import failure_chain`). No figure contains generated imagery or a real person's likeness.
"""
import csv
import os
import sys
from datetime import date

sys.path.insert(0, os.path.dirname(__file__))
from figlib import render, MUTED, INK  # noqa: E402
from ch04_figures import failure_chain  # noqa: E402
from ch08_figures import verification_funnel, funnel_height  # noqa: E402
from ch13_figures import modality_tokens  # noqa: E402
from ch14_figures import agent_loop, LOOP_H  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LOOP = ["Frame", "Prompt", "Verify", "Decide", "Disclose"]
STATUSES = ("measured", "reported", "forecast", "inferred")
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def read_events(name="ch22_timeline.csv"):
    with open(os.path.join(ROOT, "data", name), encoding="utf8") as fh:
        return list(csv.DictReader(line for line in fh if line.strip() and not line.startswith("#")))


def _d(s):
    y, m, d = (int(p) for p in s.split("-"))
    return date(y, m, d)


def _frac(dt):
    return dt.year + (dt.timetuple().tm_yday - 1) / 366


def _as_set(x):
    if x is None:
        return set()
    return {x} if isinstance(x, str) else set(x)


def timeline_height(note=None):
    return 52 + (24 if note else 0) + 134 + 44 + 44 + 134 + 22 + 60


def capability_timeline(highlight=None, note=None, events=None, as_of="October 2026", title=None,
                        start=None, end=None, as_of_date="2026-10-18"):
    evs = sorted(events if events is not None else read_events(), key=lambda e: e["date"])
    if len(evs) > 9:
        raise ValueError("capability_timeline: at most 9 events")
    for e in evs:
        if e["status"] not in STATUSES:
            raise ValueError(f"unknown status {e['status']!r}")
    hl = _as_set(highlight)
    unknown = hl - {e["id"] for e in evs}
    if unknown:
        raise ValueError(f"unknown event id(s): {sorted(unknown)}")
    y0 = int(start) if start else min(_d(e["date"]).year for e in evs)
    y1 = int(end) if end else max(_d(e["date"]).year for e in evs) + 1
    asof = _d(as_of_date)

    def draw(f):
        muted, ink = MUTED[f.mode], INK[f.mode]
        f.text(400, 22, title or f"Capability Timeline, as of {as_of}", size=17, weight="700", width=780)
        top = 52 + (24 if note else 0)
        if note:
            f.text(400, 52, note, size=13, italic=True, color=muted, width=770)
        bw, bh = 140, 134
        ax_y = top + bh + 44
        n = len(evs)
        x_a, x_b = 90, 710
        xs = [400.0] if n == 1 else [x_a + i * (x_b - x_a) / (n - 1) for i in range(n)]
        f.line(30, ax_y, 770, ax_y, width=2.2)
        # year labels at the first event of each year; the as-of marker between past and future events
        seen = set()
        past = [i for i, e in enumerate(evs) if _d(e["date"]) <= asof]
        for i, e in enumerate(evs):
            yr = _d(e["date"]).year
            if yr not in seen:
                seen.add(yr)
                xl = xs[i] - (xs[1] - xs[0]) / 2 if n > 1 and i > 0 else 30
                f.line(xl, ax_y - 8, xl, ax_y + 8, width=1.6)
                f.text(xl + 4, ax_y - 16, str(yr), size=13, weight="700", anchor="start", color=muted)
        if past and len(past) < n:
            xa = (xs[past[-1]] + xs[past[-1] + 1]) / 2
        else:
            xa = 770 if past else 30
        f.line(xa, ax_y - 34, xa, ax_y + 34, width=3.0, color=ink)
        f.text(xa + 5, ax_y + 16, "now", size=13, weight="700", anchor="start")
        for i, e in enumerate(evs):
            dt = _d(e["date"])
            up = i % 2 == 0
            cx = xs[i]
            by = top if up else ax_y + 44
            bx = cx - bw / 2
            on = e["id"] in hl
            st = e["status"]
            role = "highlight" if on else ("soft" if st == "forecast" else "neutral")
            f.box(bx, by, bw, bh, "", role=role, kind="step", dashed=(st == "inferred"), thick=on)
            tc = "#FFFFFF" if on else ink
            dlab = f"{MONTHS[dt.month - 1]} {dt.year}" if st != "forecast" else f"by {dt.year}"
            f.text(cx, by + 16, dlab, size=13, weight="700", color=tc)
            f.text(cx, by + 54, e["label"], size=13, color=tc, width=bw - 14)
            aged = e.get("aged", "no") == "yes"
            tag = f"{e.get('tag') or st}: {e['who']}" + (" · aged" if aged else "")
            f.text(cx, by + 108, tag, size=13, italic=True, color=tc, width=bw - 10)
            mx, my = bx + bw - 14, by + 4
            if st == "measured":
                f.raw(f'<rect x="{mx:.1f}" y="{my}" width="10" height="10" fill="{tc}"/>')
            elif st == "reported":
                f.raw(f'<rect x="{mx:.1f}" y="{my}" width="10" height="10" fill="none" stroke="{tc}" '
                      f'stroke-width="1.6"/>')
            elif st == "forecast":
                f.text(mx + 4, my + 6, "→", size=13, weight="700", color=tc)
            if aged:  # folded top-left corner
                f.raw(f'<path d="M{bx:.1f},{by + 18} L{bx + 18:.1f},{by} L{bx + 18:.1f},{by + 18} z" fill="{tc}"/>')
            f.line(cx, by + bh if up else by, cx, ax_y, width=1.2, color=muted)
            f.raw(f'<circle cx="{cx:.1f}" cy="{ax_y}" r="4.5" fill="{ink}"/>')
        ly = ax_y + 44 + bh + 22
        f.text(400, ly, "■ measured or outside estimate = an outside source · □ reported = the developer's statement",
               size=13, color=muted)
        f.text(400, ly + 21, "→ light fill = forecast · dashed outline = the book's inference · folded corner = aged",
               size=13, color=muted)
        f.text(400, ly + 42, f"Thick bar = now (as of {as_of}) · events in date order, not to scale", size=13,
               color=muted)
    return draw


# ---------------------------------------------------------------- F22.1 chapter map
def chapter_map(f):
    muted = MUTED[f.mode]
    f.text(400, 30, "Chapter 22 at a glance (optional chapter)", size=22, weight="700")
    cols = [("How to read a claim", ["22.1 Reading a dated claim", "22.2 Reasoning models",
                                     "22.3 Agents and tool use"]),
            ("What changed", ["22.4 Many modalities", "22.5 Open and closed models",
                              "22.6 Scale and its costs"]),
            ("Checking and aging", ["22.7 AI and science", "22.8 What has already aged? (Studio)",
                                    "Case Study: the olympiad claims"])]
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
        if step == "Verify":
            f.box(xs[i] - 52, y - 20, 104, 40, step, role="highlight", kind="human", thick=True, size=15)
        elif step == "Decide":
            f.box(xs[i] - 62, y - 17, 124, 34, "Decide (second)", role="neutral", kind="human", size=14)
        else:
            f.text(xs[i], y, step, size=14, color=muted)
        if i < 4:
            ax = {0: 245, 1: 330, 2: 462, 3: 590}[i]
            f.text(ax, y, "→", size=14, color=muted)
    f.text(400, 410, "Verify: who checked a claim about what AI can do? Decide (second): what you rely on, "
           "and until when", size=13, color=muted, width=790)
    f.text(400, 436, "Thick boxes = the fast route, with the Opening Case and Summary · written in October 2026",
           size=13, color=muted, width=790)


# ---------------------------------------------------------------- F22.2 storyboard
def storyboard(f):
    muted = MUTED[f.mode]
    f.text(400, 22, "IMO 2025: the same score, three kinds of check", size=18, weight="700")
    cols = [("Graded by the competition",
             "Gemini Deep Think: 35 of 42, natural language, 4.5 hours",
             "measured: IMO coordinators (as DeepMind's post states)", False),
            ("Graded in the developer's own evaluation",
             "OpenAI experimental model: 35 of 42",
             "reported: three former medalists, according to OpenAI", False),
            ("Checked by a proof program",
             "Seed Prover: 30 of 42 after about 3 days · Aristotle: gold level",
             "measured: each proof's validity (Lean) · scores reported by the developers", False)]
    for i, (head, what, tag, _) in enumerate(cols):
        x = 20 + i * 262
        f.box(x, 50, 236, 64, head, role="neutral", kind="human", size=14)
        f.box(x, 132, 236, 112, what, role="ai", kind="ai", size=13, sub=None)
        f.arrow(x + 118, 116, x + 118, 130)
        f.text(x + 118, 270, tag, size=13, italic=True, width=228)
    f.box(20, 320, 760, 62, "What no check covered: how much computing was used, or whether people helped "
          "(the IMO president, reported by AFP)", role="soft", kind="step", size=13)
    f.box(20, 398, 760, 50, "Human context (AFP): 641 students; about 10% won gold; five scored 42 of 42",
          role="neutral", kind="human", size=13)
    f.text(400, 470, "Hexagon = an AI system's result · rounded = who checked it · Seed Prover's score: "
           "IMO-confirmed, according to ByteDance", size=13, color=muted, width=780)


# ---------------------------------------------------------------- F22.4 evidence status and crosswalk
def evidence_status(f):
    muted = MUTED[f.mode]
    f.text(400, 22, "Three tags for every claim about what AI can do", size=18, weight="700")
    f.box(20, 48, 230, 74, "1. As-of date", role="neutral", kind="step", size=15,
          sub="when it was made or measured", sub_size=13)
    f.box(285, 48, 230, 74, "2. Evidence status", role="highlight", kind="decision", size=14, thick=True)
    f.box(550, 48, 230, 74, "3. Who could check it", role="neutral", kind="human", size=15,
          sub="an outside source that could test it", sub_size=13)
    f.arrow(252, 85, 283, 85)
    f.arrow(517, 85, 548, 85)
    sts = [("■ measured", "checked by someone other than the developer", "neutral", False),
           ("□ reported", "stated by the developer, or an outlet citing it", "neutral", False),
           ("→ forecast", "about the future, whoever says it", "soft", False),
           ("the book's inference", "this book's reading, marked as such", "neutral", True)]
    for i, (a, b, role, dash) in enumerate(sts):
        x = 20 + i * 192
        f.box(x, 150, 180, 112, a, role=role, kind="step", dashed=dash, size=14, sub=b, sub_size=13)
        f.arrow(400, 124, x + 90, 148)
    f.text(400, 292, "Crosswalk with the case tiers", size=15, weight="700")
    f.box(20, 308, 370, 92, "Case tier: is this fact in the primary record?", role="neutral", kind="step",
          size=14, sub="confirmed · reported · inferred", sub_size=13)
    f.box(410, 308, 370, 92, "Evidence status: who checked the capability?", role="neutral", kind="step",
          size=14, sub="measured · reported · forecast · the book's inference", sub_size=13)
    f.text(400, 424, "Example: DeepMind's post is the confirmed record of what DeepMind says; the score it "
           "reports was checked by the IMO's coordinators, so it is measured.", size=13, italic=True,
           width=760)
    f.text(400, 464, "\"Reported\" is in both lists: as a tier, a named outlet says so; as a status, only the "
           "developer vouches for the capability.", size=13, italic=True, width=760)
    f.text(400, 500, "Dashed = the book's inference only · light fill = forecast · diamond = the decision you "
           "make about a claim", size=13, color=muted, width=780)


# ---------------------------------------------------------------- F22.5 test-time compute
def test_time(f):
    muted = MUTED[f.mode]
    f.text(400, 22, "A reasoning model produces extra tokens before its answer", size=18, weight="700")
    f.box(20, 70, 150, 80, "Your prompt", role="neutral", kind="human", size=15)
    f.box(220, 60, 150, 100, "Model", role="ai", kind="ai", size=16)
    f.box(420, 60, 200, 100, "Reasoning tokens", role="soft", kind="step", size=15,
          sub="often hidden; counted in time and cost", sub_size=13)
    f.box(660, 70, 120, 80, "Answer", role="ai", kind="step", size=15)
    f.arrow(172, 110, 218, 110)
    f.arrow(372, 110, 418, 110)
    f.arrow(622, 110, 658, 110)
    f.box(20, 200, 360, 90, "Earlier chat model: answer right away", role="neutral", kind="step", size=14,
          sub="less computation at answer time", sub_size=13)
    f.box(420, 200, 360, 90, "Reasoning model: more tokens first", role="neutral", kind="step", size=14,
          sub="test-time compute: more computation spent per answer", sub_size=13)
    f.box(20, 320, 760, 70, "Scores compiled by an outside tracker: large gains on math and code. Factual "
          "errors remain and depend on the task (one developer's test: reported).", role="soft", kind="step",
          size=13)
    f.text(400, 420, "Hexagon = AI · the reasoning text is generated like any other text: a claim to check "
           "(Chapter 17)", size=13, color=muted, width=780)


# ---------------------------------------------------------------- F22.13 trend vs forecast
def trend_forecast(f):
    muted = MUTED[f.mode]
    f.text(400, 22, "The trend is documented; whether it continues is a forecast", size=18, weight="700")
    f.box(20, 60, 240, 110, "Documented inputs", role="neutral", kind="step", size=15,
          sub="training compute, electricity use (outside estimates)", sub_size=13)
    f.box(280, 60, 240, 110, "Debated returns", role="neutral", kind="decision", size=14)
    f.box(540, 60, 240, 110, "Forecasts", role="soft", kind="step", size=15,
          sub="2030 compute, data, power; what more scale will buy", sub_size=13)
    f.arrow(262, 115, 278, 115)
    f.arrow(522, 115, 538, 115)
    f.box(20, 200, 370, 120, "\"Still paying off\"", role="neutral", kind="human", size=15,
          sub="benchmark gains continue; answer-time computing adds a new way to scale (as its proponents "
              "report)", sub_size=13)
    f.box(410, 200, 370, 120, "\"Slowing down\"", role="neutral", kind="human", size=15,
          sub="reports in 2024 of smaller gains from pretraining; limits of data, chips and power", sub_size=13)
    f.box(20, 346, 760, 64, "What would move each side: outside measurements of the next systems, dated, "
          "on tasks not seen in training", role="verified", kind="step", size=13)
    f.text(400, 440, "Rounded = a position held by people · light fill = forecast · Chapter 23 treats debates "
           "about general AI and long-term risk", size=13, color=muted, width=780)


# ---------------------------------------------------------------- F22.15 system boundary
def boundary(f):
    muted = MUTED[f.mode]
    f.text(400, 22, "A per-prompt energy figure depends on what it counts", size=18, weight="700")
    layers = [("Active AI chips", "0.10 Wh: Google's figure counting only these (2025)"),
              ("+ host computer and memory", ""),
              ("+ idle capacity kept ready", ""),
              ("+ data-center overhead (cooling, power)", "0.24 Wh: Google's full-stack figure (2025)")]
    for i, (a, b) in enumerate(layers):
        w = 300 + i * 120
        x = 400 - w / 2
        y = 330 - i * 70
        f.box(x, y, w, 60, a, role="neutral" if i < 3 else "soft", kind="step", size=14)
        if b:
            f.text(400, y + 76 if i == 0 else y - 14, b, size=13, italic=True, weight="600", width=620)
    f.text(400, 446, "Both figures are the developer's (reported); its blog says they have not been verified "
           "by an independent third party.", size=13, color=muted, width=780)
    f.text(400, 480, "Wider boxes = a wider system boundary · an outside estimate for another provider's "
           "typical query: about 0.3 Wh (Epoch AI, 2025)", size=13, color=muted, width=780)


# ---------------------------------------------------------------- F22.18 aging card
def aging_card(f):
    muted = MUTED[f.mode]
    f.text(400, 22, "An aging check asks what a dated claim describes today, and who says so", size=17,
           weight="700", width=780)
    steps = [("1. The old claim", "quote it with its as-of date and status"),
             ("2. Today's best source", "a primary source you opened; never an AI tool's answer"),
             ("3. Verdict for today", "supported · partly supported · unsupported · contradicted · cannot verify"),
             ("4. What changed", "the facts · the evidence status · only the names"),
             ("5. Next check", "the date, or the event, that should trigger it")]
    for i, (a, b) in enumerate(steps):
        y = 52 + i * 78
        kind = "decision" if i == 2 else ("human" if i == 4 else "step")
        role = "highlight" if i == 2 else "neutral"
        if kind == "decision":
            f.box(40, y - 4, 200, 74, a, role=role, kind=kind, thick=True, size=13)
        else:
            f.box(40, y, 200, 64, a, role=role, kind=kind, size=14)
        f.text(500, y + 32, b, size=13, width=500)
        if i < 4:
            f.arrow(140, y + 66, 140, y + 76)
    f.text(400, 460, "Diamond = your judgment · rounded = a person's decision · verdicts on Chapter 8's "
           "five-point scale", size=13, color=muted, width=780)


# ---------------------------------------------------------------- F22.20 summary card
def summary_card(f):
    f.text(400, 24, "Chapter 22 in six cards", size=18, weight="700")
    cards = [("Date it", "every claim has an as-of date"),
             ("Status it", "measured · reported · forecast · the book's inference"),
             ("Who could check?", "an outside source, a competition, a proof checker, the field"),
             ("Half the time ≠ reliably", "50% and 80% horizons; benchmarks are someone else's tasks"),
             ("Count the boundary", "per prompt vs. total; what the number includes"),
             ("Check what aged", "facts, status or only names; set the next check")]
    for i, (a, b) in enumerate(cards):
        x = 20 + (i % 3) * 260
        y = 50 + (i // 3) * 130
        f.box(x, y, 240, 110, a, role="verified" if i == 5 else "neutral", kind="human" if i == 5 else "step",
              size=15, sub=b, sub_size=13)
    f.text(400, 316, "Rounded = what you do next · written as of October 2026", size=13, color=MUTED[f.mode])


# ---------------------------------------------------------------- reuse instances
TIMELINE = None  # built in FIGS so the title can count statuses from the CSV


def _timeline_title(evs):
    from collections import Counter
    c = Counter(e["status"] for e in evs)
    words = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
    return (f"Of the {words[len(evs)]} milestones in this chapter's timeline, {words[c['measured']]} rest on "
            f"an outside source")


def _aged_title(evs):
    words = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
    n = sum(e.get("aged") == "yes" for e in evs)
    return f"Of {words[len(evs)]} dated claims re-checked in October 2026, {words[n]} had aged"


EVS = read_events()
AGED = read_events("ch22_timeline_aged.csv")
_COMPUTER_USE_BASE = agent_loop(
    highlight=["tool", "observation"],
    annotate={"observation": "a new screenshot of the screen"},
    note="A computer-use agent: the same loop, with the screen as the observation (Chapter 14 owns the gates)")


def COMPUTER_USE(f):
    """Signature 9 as drawn by ch14_figures.agent_loop; the tool-call note is placed left of the
    tool-call -> observation arrow here, because the shared default position sits on that arrow."""
    _COMPUTER_USE_BASE(f)
    f.text(615, 200, "a click, keystroke or typed text", size=13, italic=True, weight="600", width=120,
           color=INK[f.mode])
MODALITIES = modality_tokens(
    highlight=["audio", "model"],
    note="As of October 2026, some models also produce sound and video, not only receive them (dated box, 22.4)")
FUNNEL_SCIENCE = verification_funnel(
    highlight="expert", verdict=None,
    tag="A discovery claim: the paper, its data, then the field's own checks",
    note="Peer review, replication and critique by specialists take longer than an announcement",
    notes={"check": "the paper and its supplementary data", "primary": "the predicted structures or proofs",
           "expert": "specialists: replication, critique, formal checks"})
CHAIN_ERDOS = failure_chain(
    notes={0: "A literature search found existing papers (the output was useful)",
           1: "Posted as 'solved' before anyone checked what 'open' meant (documented)",
           2: "Readers and other researchers relied on the post (reported)",
           3: "Posts mostly deleted; public correction; no lasting harm reported"},
    highlight={1},
    tag="Tree: none (no output shown wrong) · the failure was a claim published before its check (link 2)")

FIGS = [
    ("f22-01-chapter-map", chapter_map, 800, 455, "Chapter 22 at a glance"),
    ("f22-02-storyboard", storyboard, 800, 490, "IMO 2025: the same score, three kinds of check"),
    ("f22-03-timeline", capability_timeline(title=_timeline_title(EVS)), 800, timeline_height(),
     _timeline_title(EVS)),
    ("f22-04-evidence-status", evidence_status, 800, 520,
     "A claim's status tells you who checked it, not whether it is true"),
    ("f22-05-test-time", test_time, 800, 440,
     "A reasoning model spends extra tokens before it answers, and they cost time and money"),
    ("f22-09-computer-use", COMPUTER_USE, 800, LOOP_H,
     "A computer-use agent's observation is a screenshot; its action is a click or a keystroke"),
    ("f22-10-modalities", MODALITIES, 800, 450, "Some models now produce sound and video, not only receive them"),
    ("f22-13-trend-forecast", trend_forecast, 800, 460, "The trend is documented; whether it continues is a forecast"),
    ("f22-15-boundary", boundary, 800, 506, "A per-prompt energy figure depends on what it counts"),
    ("f22-16-funnel-science", FUNNEL_SCIENCE, 800, funnel_height(tag=True, note=True),
     "For a discovery, the field's own checks are the last stage"),
    ("f22-17-timeline-aged",
     capability_timeline(events=AGED, start=2014, end=2031, highlight=["qa14", "metr25", "imo25"],
                         title=_aged_title(AGED),
                         note="Thick boxes = claims re-checked in section 22.8: the 2014 entry, a 2025 horizon, "
                              "the 2025 olympiad"),
     800, timeline_height(note=True), _aged_title(AGED)),
    ("f22-18-aging-card", aging_card, 800, 480,
     "An aging check asks what a dated claim describes today, and who says so"),
    ("f22-19-chain-erdos", CHAIN_ERDOS, 800, 420,
     "The 'ten solved problems' claim failed at the check before publication"),
    ("f22-20-summary-card", summary_card, 800, 340, "Chapter 22 summary card"),
]

if __name__ == "__main__":
    only = set(sys.argv[1:])
    for fid, fn, w, h, title in FIGS:
        if only and fid not in only:
            continue
        render(fid, fn, w, h, title, ROOT)
        print("rendered", fid)
