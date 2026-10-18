"""Chapter 6 diagrams (SVG, color + gray). Run from the repo root:
    python3 figures/scripts/ch06_figures.py
Data charts (F6.4, F6.12) are in ch06_charts.py (published values in data/ch06_*.csv).

Reused signatures (imported, never redrawn):
  * Signature 1, AI Work Loop: work_loop (ch01_figures) is not drawn in full here; the chapter map uses the
    same five-step strip as Chapters 2 and 5.
  * Signature 4, Anatomy of an LLM Response: `llm_anatomy` from ch03_figures (F6.2).
  * Signature 6, Anatomy of a Prompt: `prompt_anatomy` from ch05_figures (F6.9).

New reusable diagram introduced here (not one of the 12 signatures):

    from ch06_figures import context_layers

* Context Layers: `context_layers(highlight=None, note=None, side_note=None)`. It extends the context-window
  stage of Signature 4: the same frame and Chapter 3's four layers with Chapter 3's wording, plus two layers
  that persistent features fill (standing instructions; project files and memory notes). 8 shapes:
  frame + 6 layers + the model hexagon.
  Layer names for `highlight` (one name or a list): "system", "standing", "project", "conversation",
  "documents", "prompt". `note` prints a line under the title; `side_note` prints up to three short lines
  under the model hexagon (used for the Medprompt variant).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from figlib import render, MUTED, INK, ROLES  # noqa: E402
from ch03_figures import llm_anatomy  # noqa: E402  (Signature 4, reused)
from ch05_figures import prompt_anatomy  # noqa: E402  (Signature 6, reused)

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LOOP = ["Frame", "Prompt", "Verify", "Decide", "Disclose"]


def _as_set(x):
    if x is None:
        return set()
    if isinstance(x, str):
        return {x}
    return set(x)


# ---------------------------------------------------------------- Context Layers (extends Signature 4)
# (key, label, subtitle, who sets it, new in Ch. 6?)  Ch. 3 labels and subtitles kept word for word.
LAYERS = [
    ("system", "System prompt", "set by the tool's maker", "the provider; usually unseen", False),
    ("standing", "Standing instructions", "your rules for every chat in a scope", "you, once, in options or a project", True),
    ("project", "Project files and memory notes", "added automatically", "you, or the product", True),
    ("conversation", "Conversation so far", "earlier prompts and responses", "you and the model, earlier", False),
    ("documents", "Pasted or retrieved text", "documents, search results", "you, or a search tool", False),
    ("prompt", "Your prompt", "the newest message", "you, now", False),
]
LAYER_KEYS = [k for k, *_ in LAYERS]


def context_layers(highlight=None, note=None, side_note=None):
    hl = _as_set(highlight)
    unknown = hl - set(LAYER_KEYS)
    if unknown:
        raise ValueError(f"unknown layer(s): {sorted(unknown)}")

    def draw(f):
        ink, muted = INK[f.mode], MUTED[f.mode]
        f.text(400, 24, "Context layers", size=18, weight="700")
        if note:
            f.text(400, 46, note, size=13, color=muted, italic=True, width=760)
        fill, _, _ = ROLES[f.mode]["soft"]
        f.raw(f'<rect x="20" y="62" width="540" height="458" rx="6" fill="{fill}" stroke="{ink}" stroke-width="1.6"/>')
        f.text(36, 82, "Context window", size=15, weight="700", anchor="start")
        f.text(36, 102, "everything the model receives this turn", size=13, anchor="start")
        f.text(420, 102, "Who sets it", size=13, weight="700")
        for i, (key, lab, sub, who, new) in enumerate(LAYERS):
            y = 116 + i * 66
            on = key in hl
            kind = "human" if key == "prompt" else "step"
            f.box(36, y, 290, 56, lab, role="highlight" if on else "neutral", kind=kind, thick=on,
                  dashed=(key == "system"), size=14, sub=sub, sub_size=13)
            f.text(420, y + 20, who, size=13, width=210)
            if new:
                f.text(420, y + 42, "(new in Chapter 6)", size=13, italic=True, color=muted)
        f.arrow(562, 291, 600, 291)
        f.box(604, 240, 176, 102, "The model", role="ai", kind="ai", size=15,
              sub="receives all layers as one input", sub_size=13)
        if side_note:
            for j, ln in enumerate(side_note[:3]):
                f.text(692, 378 + j * 40, ln, size=13, width=180, weight="600" if j == 0 else "normal")
        f.text(400, 544, "Dashed = usually not visible to you · rounded = you, now · hexagon = AI component · "
               "dark or thick = this section's layer", size=13, color=muted, width=780)
        f.text(400, 566, "Chapter 3's four layers, with two that persistent features fill before you type.",
               size=13, color=muted, italic=True)
    return draw


# ---------------------------------------------------------------- F6.1 Chapter map
def chapter_map(f):
    muted = MUTED[f.mode]
    f.text(400, 26, "Chapter 6 at a glance", size=22, weight="700")
    f.text(400, 52, "Optional (Deep) chapter, read with Chapter 5 · not examinable · fast route about 25 minutes",
           size=13, color=muted)
    cols = [("What the model receives", ["6.1 Context layers", "6.2 Choosing what to include",
                                         "6.3 Labels and order"]),
            ("Steering and keeping", ["6.4 In-context examples, tested", "6.5 Standing instructions, projects, memory"]),
            ("Reuse", ["6.6 Templates and your library (Studio)", "6.7 Prompt chains with a check",
                       "Personal prompt library (optional)"])]
    for c, (head, items) in enumerate(cols):
        x = 24 + c * 258
        f.text(x + 116, 86, head, size=16, weight="700")
        for i, it in enumerate(items):
            role = "soft" if c == 2 and i == 2 else "neutral"
            kind = "human" if c == 2 else "step"
            f.box(x, 104 + i * 82, 232, 66, it, role=role, kind=kind, size=14)
        if c < 2:
            f.arrow(x + 238, 220, x + 254, 220)
    f.text(400, 372, "Opening case: Medprompt (2023) — same model, different context (6.2–6.4) and steps (6.7)",
           size=13, color=muted)
    y = 412
    f.text(150, y, "AI Work Loop:", size=14, weight="700", anchor="end")
    xs = [205, 300, 420, 540, 640]
    for i, step in enumerate(LOOP):
        if step == "Prompt":
            f.box(xs[i] - 50, y - 20, 100, 40, step, role="highlight", kind="human", thick=True, size=15)
        else:
            f.text(xs[i], y, step, size=14, color=muted, weight="700" if step == "Verify" else "normal")
        if i < 4:
            f.text((xs[i] + xs[i + 1]) / 2, y, "→", size=14, color=muted)
    f.text(400, 450, "This chapter strengthens Prompt (design what the model receives), then Verify (test before reuse).",
           size=13, color=muted)


# ---------------------------------------------------------------- F6.6 catalog before / after
def catalog_before_after(f):
    muted = MUTED[f.mode]
    f.text(200, 28, "Before: everything pasted", size=16, weight="700")
    f.text(600, 28, "After: selected, labeled, task last", size=16, weight="700")
    f.line(400, 46, 400, 470, dashed=True, color=muted)
    f.box(30, 56, 340, 54, "Draft a parts order for the club", role="neutral", kind="human", size=14,
          sub="task first, with no criteria", sub_size=13)
    f.box(30, 128, 340, 190, "Supplier catalog, all 120 pages", role="risk", kind="step", thick=True, size=15,
          sub="motors, wheels, sensors, tools, clothing, returns policy, 2026 and 2027 price lists mixed",
          sub_size=13)
    f.box(30, 336, 340, 74, "Club budget rules, all 8 pages", role="neutral", kind="step", size=14,
          sub="travel, food, parts, fundraising", sub_size=13)
    f.text(200, 440, "The rule that applies is on page 6.", size=13, color=muted, italic=True)
    f.text(200, 462, "Two price lists disagree.", size=13, color=muted, italic=True)
    rows = [("TASK IN BRIEF", "a parts order for the club (details at the end)", "step"),
            ("INSTRUCTIONS", "Use only the material below; if a part is missing, say so", "step"),
            ("CATALOG p. 14 · 2027 price list", "drive motors (four models)", "step"),
            ("CATALOG p. 52 · 2027 price list", "wheels and hubs", "step"),
            ("BUDGET RULE 3 · Jan 2027", "parts orders over $250 need two officers", "step"),
            ("TASK (full, last)", "Draft an order for two motors and four wheels; list total and who must approve", "human")]
    for i, (lab, sub, kind) in enumerate(rows):
        f.box(430, 56 + i * 70, 340, 62, lab, role="verified" if i in (2, 3, 4) else "neutral", kind=kind,
              thick=(i == 5), size=14, sub=sub, sub_size=13)
    f.text(400, 494, "Thick border (orange in color, hatched in print) = material the task does not need · "
           "shaded = labeled excerpts with source and date · rounded = your task", size=13, color=muted, width=780)
    f.text(400, 516, "Constructed example: catalog, prices and rules are invented for teaching.", size=13,
           color=muted, italic=True)


# ---------------------------------------------------------------- F6.7 balanced vs one-sided examples
def balanced_examples(f):
    muted = MUTED[f.mode]
    panels = [("Balanced in-context examples", ["\"Loved the workshop\" → positive",
                                               "\"Too long, hard to follow\" → negative",
                                               "\"Useful, but the room was cold\" → mixed"],
               "New answers coded across all three labels", "verified"),
              ("One-sided in-context examples", ["\"Loved the workshop\" → positive",
                                                "\"Great speakers\" → positive",
                                                "\"Really helpful\" → positive"],
               "New answers pulled toward \"positive\", even mixed ones", "risk")]
    for p, (head, exs, result, role) in enumerate(panels):
        x = 24 + p * 392
        f.text(x + 172, 30, head, size=16, weight="700")
        for i, e in enumerate(exs):
            f.box(x, 52 + i * 70, 344, 56, e, role="neutral", kind="step", size=14)
        f.arrow(x + 172, 262, x + 172, 290)
        f.box(x + 8, 294, 328, 82, result, role=role, kind="step", thick=(role == "risk"), size=14,
              sub="(illustrative pattern, not a measured result)", sub_size=13)
    f.text(400, 404, "Coding open-ended survey answers. Balance and order of examples changed outputs in "
           "published tests (Zhao et al., 2021; Lu et al., 2022).", size=13, color=muted, width=770)
    f.text(400, 434, "Thick border (orange in color, hatched in print) = the pattern to avoid · shaded = the pattern to aim for", size=13, color=muted)


# ---------------------------------------------------------------- F6.9 template anatomy (Signature 6 reused)
def template_anatomy(f):
    sig6 = prompt_anatomy(highlight="context",
                          note="Shown as a template: the highlighted part becomes a {placeholder} you fill each time.")
    sig6(f)
    muted = MUTED[f.mode]
    f.line(20, 504, 780, 504, color=muted)
    f.text(400, 526, "Where the parts land in the context layers", size=15, weight="700")
    notes = ["Context → pasted text, project files or the prompt itself (6.2, 6.5)",
             "In-context examples → a fixed part of the template, kept only if a with-and-without test shows they help (6.4)",
             "Task, constraints, format → the fixed part of the template (6.6)"]
    for i, n in enumerate(notes):
        f.text(400, 554 + i * 24, n, size=13, color=INK[f.mode])


# ---------------------------------------------------------------- F6.10 library entry card
def library_card(f):
    ink, muted = INK[f.mode], MUTED[f.mode]
    f.box(20, 16, 760, 548, "", role="soft", kind="step")
    f.text(40, 40, "Library entry: Club update email · v1.1 · 2027-02-03", size=16, weight="700", anchor="start")
    fields = [("Purpose", "Turn my meeting notes into the weekly update for members"),
              ("Use when / not when", "Weekly meeting notes · not for budget or safety decisions"),
              ("Template", "{NOTES} + {DATE} first, then the fixed task, audience, format"),
              ("Context to attach", "My notes, names replaced by roles · never members' contact details"),
              ("In-context examples", "Not used: the test with and without showed no gain"),
              ("Tested on", "Tool and model name, date (in the file)"),
              ("What changed", "v1.1 adds: If no decisions were made, write \"No decisions this week.\"")]
    for i, (k, v) in enumerate(fields):
        y = 72 + i * 32
        f.text(40, y, k, size=13, weight="700", anchor="start")
        f.text(220, y, v, size=13, anchor="start")
    f.line(36, 302, 764, 302, color=muted)
    f.text(40, 324, "Test record", size=14, weight="700", anchor="start")
    cols = [40, 150, 470, 640]
    heads = ["Input", "What it was", "Pass criteria met?", "Action"]
    for c, h in zip(cols, heads):
        f.text(c, 352, h, size=13, weight="700", anchor="start")
    rows = [("Typical", "Normal meeting, 3 decisions", "3 of 3", "keep"),
            ("Different", "Two meetings merged", "3 of 3", "keep"),
            ("Edge (v1.0)", "No decisions; draft invented one", "2 of 3: (b) failed", "fix → v1.1"),
            ("Edge (v1.1)", "Same notes, rerun", "3 of 3", "keep")]
    for r, row in enumerate(rows):
        y = 382 + r * 32
        f.line(36, y - 16, 764, y - 16, color=muted, width=0.8)
        for c, val in zip(cols, row):
            f.text(c, y, val, size=13, anchor="start", weight="700" if (r == 2 and c == 470) else "normal")
    f.text(400, 532, "Pass criteria: every decision in the notes appears · nothing appears that is not in the notes · "
           "each task has an owner and a date", size=13, color=muted, width=740)
    f.text(400, 584, "Constructed example (Sam's library). Earlier inputs are rerun after every change.", size=13,
           color=muted, italic=True)


# ---------------------------------------------------------------- F6.11 chain with a check
def chain_check(f):
    muted = MUTED[f.mode]
    f.box(20, 70, 150, 92, "Meeting notes", role="neutral", kind="step", size=14,
          sub="names replaced by roles", sub_size=13)
    f.arrow(172, 116, 196, 116)
    f.box(200, 64, 170, 104, "Step 1: extract decisions and action items", role="ai", kind="ai", size=14)
    f.arrow(372, 116, 396, 116)
    f.box(400, 60, 180, 112, "Sam checks names, dates and owners against his notes", role="neutral",
          kind="human", thick=True, size=14)
    f.arrow(582, 116, 606, 116)
    f.box(610, 56, 170, 120, "All correct?", role="neutral", kind="decision", size=14)
    f.arrow(695, 178, 695, 236)
    f.text(712, 207, "yes", size=13, anchor="start", italic=True)
    f.arrow(640, 150, 500, 174, curve=0, dashed=True)
    f.text(560, 196, "no: fix the list", size=13, italic=True)
    f.box(610, 240, 170, 104, "Step 2: draft the update email", role="ai", kind="ai", size=14)
    f.arrow(608, 292, 512, 292)
    f.box(330, 246, 180, 92, "Sam reads, edits and sends", role="neutral", kind="human", size=14)
    f.text(400, 390, "Each step's output becomes the next step's input; the check sits where errors start.",
           size=14, weight="600")
    f.text(400, 420, "Rectangle = material · hexagon = AI step · rounded = Sam (thick = the check) · "
           "diamond = decision · dashed = loop back", size=13, color=muted, width=780)
    f.text(400, 444, "Constructed example. You fix the steps and run them; the model does not choose them.",
           size=13, color=muted, italic=True)


# ---------------------------------------------------------------- F6.14 summary card
def summary_card(f):
    f.text(400, 26, "Chapter 6 — what you can do now", size=18, weight="700")
    cards = ["Layers: the model receives more than your message; list who set each layer",
             "Select: relevant, labeled excerpts with source and date beat whole documents",
             "Examples: balance them, and keep them only if a with-and-without test shows they help",
             "Persistent context: review standing instructions, project files and memory; prune",
             "Templates: fixed parts + placeholders, tested on typical, different and edge inputs, versioned",
             "Chains: fixed steps you run, with your check where errors start"]
    for i, c in enumerate(cards):
        x = 20 + (i % 3) * 258
        y = 50 + (i // 3) * 150
        f.box(x, y, 242, 130, c, role="neutral" if i % 2 else "soft", kind="human", size=14, weight="600")


FIGS = [
    ("f6-01-chapter-map", chapter_map, 800, 470, "Chapter 6 at a glance"),
    ("f6-02-anatomy-context", llm_anatomy("context", note="Recall from Chapter 3"), 800, 490,
     "Everything the model receives this turn shares one context window"),
    ("f6-03-context-layers", context_layers(note="Chapter 3's four layers plus two that are filled before you type"),
     800, 580,
     "Two more layers can fill the window before you type"),
    ("f6-05-layers-documents", context_layers(highlight="documents",
                                              note="The layer you control most directly"), 800, 580,
     "The documents you add are the layer you control most directly"),
    ("f6-06-catalog-before-after", catalog_before_after, 800, 530,
     "Two labeled excerpts with the task last replace a 120-page catalog"),
    ("f6-07-balanced-examples", balanced_examples, 800, 450, "One-sided examples pull the outputs toward one label"),
    ("f6-08-layers-persistent", context_layers(highlight=["standing", "project"],
                                               note="Filled automatically, so they need upkeep"), 800, 580,
     "Standing instructions, project files and memory fill layers automatically, so they need upkeep"),
    ("f6-09-template-anatomy", template_anatomy, 800, 640,
     "A template keeps the prompt's fixed parts and leaves placeholders for what changes"),
    ("f6-10-library-card", library_card, 800, 600,
     "A library entry records when to use it, what it was tested on, and what changed"),
    ("f6-11-chain-check", chain_check, 800, 460, "A check between steps catches errors where they start"),
    ("f6-13-layers-medprompt", context_layers(highlight="prompt",
                                              note="Medprompt (2023): what GPT-4 received, and how often it was asked",
                                              side_note=["Plus a workflow:", "5 runs, answer options shuffled",
                                                         "majority vote"]), 800, 580,
     "Medprompt changed what the model received and how often it was asked"),
    ("f6-14-summary-card", summary_card, 800, 340, "Chapter 6 summary card"),
]

if __name__ == "__main__":
    for fid, fn, w, h, title in FIGS:
        render(fid, fn, w, h, title, ROOT)
        print("rendered", fid)
