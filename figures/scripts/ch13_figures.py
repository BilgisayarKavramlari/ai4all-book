"""Chapter 13 diagrams (SVG, color + gray). Run from the repo root:
    python3 figures/scripts/ch13_figures.py
Data charts (F13.8, F13.11, F13.12) are in ch13_charts.py (data/ch13_*.csv).

New reusable drawings introduced here (Chapters 15, 19 and 22 may import them):
    modality_tokens(highlight=None, note=None)                 # text, images and sound become tokens in one window
    generation_pipeline(mode="image"|"voice", highlight=None, note=None)   # book-map figure "Generation pipeline"
    media_checklist(highlight=None, note=None, verdict=None)    # book-map figure "deepfake check list"

Reused, never redrawn: Signature 1 (`from ch01_figures import work_loop`, via the chapter map's loop strip),
Signature 4 (`from ch03_figures import llm_anatomy`), Signature 5 and the chain (`from ch04_figures import
failure_tree, failure_chain, tree_height`), Signature 8 (`from ch08_figures import verification_funnel,
funnel_height, VERDICTS`), the hop chain (`from ch09_figures import hop_chain`).
No figure contains generated imagery or a real person's likeness.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from figlib import render, MUTED, INK  # noqa: E402
from ch03_figures import llm_anatomy  # noqa: E402
from ch04_figures import failure_tree, failure_chain, tree_height  # noqa: E402
from ch08_figures import verification_funnel, funnel_height, VERDICTS  # noqa: E402
from ch09_figures import hop_chain  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LOOP = ["Frame", "Prompt", "Verify", "Decide", "Disclose"]


def _hl(highlight):
    if highlight is None:
        return set()
    return {highlight} if isinstance(highlight, str) else set(highlight)


# ---------------------------------------------------------------- modality_tokens (new, reusable)
MODALITY_LANES = {"text": ("Your words", "split into text tokens"),
                  "image": ("An image", "cut into patches; each patch becomes an image token"),
                  "audio": ("A recording", "cut into short slices; a codec turns each into an audio token")}


def modality_tokens(highlight=None, note=None):
    """Three input lanes (text, image, audio) -> one context window -> model (hexagon) -> output. 8 boxes.

    highlight: lane names ("text", "image", "audio") or "window"/"model" to mark (thick border).
    note:      one-line italic remark under the title.
    """
    hl = _hl(highlight)

    def draw(f):
        muted = MUTED[f.mode]
        f.text(400, 24, "A multimodal model receives images and sound as tokens", size=17, weight="700")
        if note:
            f.text(400, 48, note, size=13, italic=True, color=muted, width=760)
        ys = [80, 186, 292]
        for (key, (lab, sub)), y in zip(MODALITY_LANES.items(), ys):
            on = key in hl
            f.box(20, y, 170, 80, lab, role="highlight" if on else "neutral", kind="human", thick=on, size=15)
            f.box(222, y, 250, 80, sub, role="soft", kind="step", size=13, weight="normal")
            f.arrow(192, y + 40, 220, y + 40)
            f.arrow(474, y + 40, 508, 236 if key != "image" else 226)
        on = "window" in hl
        f.box(510, 140, 130, 172, "One context window", role="highlight" if on else "neutral", kind="step",
              thick=on, size=15, sub="tokens of every kind, side by side", sub_size=13)
        on = "model" in hl
        f.box(664, 186, 120, 80, "Model", role="ai", kind="ai", thick=on, size=15, sub="produces output", sub_size=13)
        f.arrow(642, 226, 662, 226)
        f.text(400, 410, "Rounded = what you provide · rectangle = a processing step · hexagon = AI component",
               size=13, color=muted, width=780)
        f.text(400, 434, "File information (date, place, camera) is not part of the tokens in two providers' tools, but the "
               "file itself still reaches the provider (as of October 2026).", size=13, color=muted, italic=True, width=780)
    return draw


# ---------------------------------------------------------------- generation_pipeline (new, reusable)
PIPE = {
    "image": [("prompt", "Prompt", "words describing the image", "human", "neutral"),
              ("encoder", "Text encoder", "turns the words into numbers", "step", "soft"),
              ("noise", "Random noise", "the starting point", "step", "soft"),
              ("denoise", "Remove a little noise", "repeated many times, steered by the prompt", "ai", "ai"),
              ("decoder", "Decoder", "turns the result into pixels", "step", "soft"),
              ("output", "New image", "plausible for the prompt; no event behind it", "step", "neutral")],
    "voice": [("text", "Text to speak", "what the new speech says", "human", "neutral"),
              ("sample", "A short voice sample", "three seconds of one person, in the 2023 study", "human", "neutral"),
              ("predict", "Predict audio tokens", "one after another, like next tokens", "ai", "ai"),
              ("decoder", "Codec decoder", "turns the tokens into sound", "step", "soft"),
              ("output", "New speech", "in an imitation of that voice", "step", "neutral")],
}


def generation_pipeline(mode="image", highlight=None, note=None):
    """Book-map figure "Generation pipeline". mode "image" (diffusion, 7 boxes incl. training lane) or
    "voice" (audio tokens, 5 boxes). highlight: stage keys of the mode. note: one italic line."""
    stages = PIPE[mode]
    hl = _hl(highlight)
    keys = {k for k, *_ in stages}
    if hl - keys:
        raise ValueError(f"unknown stage: {hl - keys}")

    def draw(f):
        muted = MUTED[f.mode]
        title = ("A generated image is built from noise toward the prompt, not looked up in a record" if mode == "image"
                 else "In 2023 a research system imitated a voice from a three-second sample")
        f.text(400, 24, title, size=17, weight="700", width=780)
        if note:
            f.text(400, 48, note, size=13, italic=True, color=muted, width=760)
        n = len(stages)
        gap = 16
        w = (760 - gap * (n - 1)) / n
        y = 96
        for i, (key, lab, sub, kind, role) in enumerate(stages):
            x = 20 + i * (w + gap)
            on = key in hl
            if on and role != "ai":
                role = "highlight"
            f.box(x, y, w, 132, lab, role=role, kind=kind, thick=on, size=14, sub=sub, sub_size=13)
            if i < n - 1:
                f.arrow(x + w + 1, y + 66, x + w + gap - 1, y + 66, width=2.0)
            if kind == "ai" and mode == "image":
                cx = x + w / 2
                f.arrow(cx + 26, y + 136, cx - 26, y + 136, curve=-26, label=None)
                f.text(cx, y + 172, "loop: many steps", size=13, italic=True, color=muted)
        if mode == "image":
            f.box(170, 300, 460, 64, "Training (earlier): very many images with captions; noise added; settings adjusted "
                  "to predict and remove it", role="soft", kind="step", size=13, weight="normal")
            f.arrow(400, 300, 400, 262)
            f.text(400, 400, "Rounded = what a person provides · hexagon = AI step · gray box = the earlier training stage",
                   size=13, color=muted, width=780)
            f.text(400, 424, "Sources: Ho et al. (2020); Rombach et al. (2022), which works in a compressed (latent) "
                   "version of the image.", size=13, color=muted, italic=True, width=780)
        else:
            f.text(400, 290, "A 2023 research system (Wang et al., 2023), trained on 60,000 hours of English speech; "
                   "not a product.", size=13, color=muted, italic=True, width=780)
            f.text(400, 318, "Rounded = what a person provides · hexagon = AI step", size=13, color=muted, width=780)
    return draw


# ---------------------------------------------------------------- media_checklist (new, reusable)
CHECKS = [("stop", "Stop", "a trigger fired: pause before you act or share", "decision", "neutral"),
          ("source", "1. Source and channel", "who sent it? reach them another way (out-of-band)", "step", "neutral"),
          ("earliest", "2. Earliest version", "reverse image search; where did it first appear?", "step", "neutral"),
          ("outside", "3. Outside sources", "does anyone else report the event?", "step", "neutral"),
          ("signals", "4. Provenance signals", "credential or watermark: present = lead; missing = proves nothing", "step",
           "neutral"),
          ("clues", "5. Content clues", "odd text, shadows, hands: weak leads, checked last", "step", "soft"),
          ("verdict", "Verdict", "", "human", "verified")]


def media_checklist(highlight=None, note=None, verdict=None):
    """Book-map figure "deepfake check list" (7 boxes). highlight: keys of CHECKS. verdict: a VERDICTS label
    printed in the verdict box (default prints the scale)."""
    hl = _hl(highlight)
    keys = {k for k, *_ in CHECKS}
    if hl - keys:
        raise ValueError(f"unknown step: {hl - keys}")
    if verdict is not None and verdict not in VERDICTS:
        raise ValueError(f"unknown verdict: {verdict}")

    def draw(f):
        muted = MUTED[f.mode]
        f.text(400, 24, "Context before pixels: a check list for media", size=17, weight="700")
        if note:
            f.text(400, 48, note, size=13, italic=True, color=muted, width=760)
        top = 70
        f.box(300, top, 200, 84, CHECKS[0][1], role="highlight" if "stop" in hl else "neutral", kind="decision",
              thick="stop" in hl, size=15)
        f.text(620, top + 42, CHECKS[0][2], size=13, italic=True, color=muted, width=220)
        y = top + 104
        for i, (key, lab, sub, kind, role) in enumerate(CHECKS[1:6]):
            on = key in hl
            yy = y + i * 70
            f.box(170, yy, 460, 58, lab, role="highlight" if on else role, kind=kind, thick=on,
                  size=14, sub=sub, sub_size=13)
            f.arrow(400, yy - 12 if i else top + 86, 400, yy - 2)
        vy = y + 5 * 70
        f.arrow(400, vy - 12, 400, vy - 2)
        vtxt = verdict if verdict else " · ".join(VERDICTS)
        f.box(170, vy, 460, 80, "Verdict and remaining uncertainty", role="verified", kind="human",
              thick="verdict" in hl, size=14, sub=vtxt, sub_size=13)
        f.text(400, vy + 106, "Diamond = decision · rectangle = a check · gray box = weak evidence · rounded = your "
               "judgment (Chapter 8's verdict scale)", size=13, color=muted, width=780)
    return draw


def checklist_height(note=None):
    return 720 + (20 if note else 0)


# ---------------------------------------------------------------- F13.1 Chapter map
def chapter_map(f):
    muted = MUTED[f.mode]
    f.text(400, 30, "Chapter 13 at a glance (optional chapter)", size=22, weight="700")
    cols = [("How media is made", ["13.1 Images and sound as tokens", "13.2 How generators build media",
                                   "13.3 Uses, and who checks"]),
            ("Signals and limits", ["13.4 Provenance and credentials", "13.5 Watermarks and labels",
                                    "13.6 Why looks and scores are weak"]),
            ("Checking", ["13.7 Context before pixels", "13.8 Your protocol (Studio)",
                          "Case Study: the fake meeting"])]
    for c, (head, items) in enumerate(cols):
        x = 30 + c * 255
        f.text(x + 115, 74, head, size=16, weight="700")
        for i, it in enumerate(items):
            fast = c == 2 and i < 2
            role = "verified" if fast else ("neutral" if c < 2 else "soft")
            kind = "human" if c == 2 else "step"
            f.box(x, 94 + i * 88, 230, 70, it, role=role, kind=kind, thick=fast, size=14)
        if c < 2:
            f.arrow(x + 236, 217, x + 252, 217)
    y = 372
    f.text(150, y, "AI Work Loop:", size=14, weight="700", anchor="end")
    xs = [205, 300, 420, 540, 640]
    for i, step in enumerate(LOOP):
        if step == "Verify":
            f.box(xs[i] - 50, y - 20, 100, 40, step, role="highlight", kind="human", thick=True, size=15)
        elif step == "Disclose":
            f.box(xs[i] - 50, y - 17, 100, 34, step, role="soft", kind="human", size=14)
        else:
            f.text(xs[i], y, step, size=14, color=muted)
        if i < 4:
            f.text((xs[i] + xs[i + 1]) / 2, y, "→", size=14, color=muted)
    f.text(400, 410, "Verify: what can this picture, voice or video prove? Disclose (second, gray box): say when media you "
           "share was generated or altered.", size=13, color=muted, width=780)
    f.text(400, 436, "Thick boxes = the fast route with the Opening Case and Summary · Opening case: Hong Kong, 2024",
           size=13, color=muted, width=780)


# ---------------------------------------------------------------- F13.2 storyboard (attribution tiers)
def storyboard(f):
    muted, ink = MUTED[f.mode], INK[f.mode]
    ev = [("Email", "phishing email from a fake CFO; first doubted (doubt: reported, CNN)", "risk", "step", False),
          ("Video conference", "pre-recorded; made from public clips and voices, police believe (confirmed)", "risk", "step",
           False),
          ("Instant messages", "meeting ended under a pretext; instructions by messaging (confirmed)", "risk", "step",
           False),
          ("Transfers", "to five local accounts; about HK$200 million (confirmed)", "neutral", "step", False),
          ("Later check", "with head office: fraud found (reported, CNN)", "verified", "human", False)]
    f.text(400, 24, "Every instruction came through a channel the fraudsters controlled", size=17, weight="700")
    f.line(24, 214, 776, 214, color=ink, width=2.4)
    for i, (d, txt, role, kind, dashed) in enumerate(ev):
        x = 18 + i * 154
        y = 48 if i % 2 == 0 else 236
        f.box(x, y, 144, 148, d, role=role, kind=kind, dashed=dashed, size=14, sub=txt, sub_size=13)
        cx = x + 72
        f.line(cx, 196 if i % 2 == 0 else 236, cx, 214, color=ink, width=1.4)
        f.raw(f'<circle cx="{cx}" cy="214" r="5" fill="{ink}"/>')
    f.text(400, 410, "Orange (hatched, thick border in print) = a channel the fraudsters controlled · confirmed = the "
           "government's reply · reported = CNN, citing police", size=13, color=muted, width=780)
    f.text(400, 448, "Sources: Hong Kong SAR Government (2024); Chen & Magramo (2024). Late January 2024; the "
           "company later confirmed it was Arup (Magramo, 2024).", size=13, color=muted, italic=True, width=780)


# ---------------------------------------------------------------- F13.6 camera vs generator
def camera_vs_generator(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "A camera records an event; a generator produces a plausible picture of none", size=17,
           weight="700", width=780)
    f.text(30, 74, "Camera", size=15, weight="700", anchor="start")
    row1 = [("An event", "something happened", "human", "neutral", False),
            ("Light from it", "reaches the lens", "step", "soft", False),
            ("Camera sensor", "records the light", "step", "soft", False),
            ("Photo file", "a record of the event", "step", "verified", False)]
    row2 = [("Prompt + noise", "words and random speckle", "human", "neutral", False),
            ("Generator", "removes noise, steered by the prompt", "ai", "ai", False),
            ("Image file", "plausible for the prompt", "step", "neutral", False),
            ("No event", "nothing behind the picture", "step", "soft", False)]
    for r, (row, y) in enumerate([(row1, 92), (row2, 262)]):
        for i, (lab, sub, kind, role, dashed) in enumerate(row):
            x = 20 + i * 196
            f.box(x, y, 172, 104, lab, role=role, kind=kind, dashed=dashed, size=14, sub=sub, sub_size=13)
            if i < 3:
                f.arrow(x + 174, y + 52, x + 194, y + 52)
    f.text(30, 244, "Generator", size=15, weight="700", anchor="start")
    f.text(400, 406, "Both files can look alike. Only one has an event behind it. Gray box = what is missing.",
           size=13, color=muted, width=780)


# ---------------------------------------------------------------- F13.7 who relies / who checks
def who_checks(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "The person who relies on the output often cannot check it, so the author must", size=17,
           weight="700", width=780)
    rows = [("Alt text", "relies: a screen-reader user · can check: rarely (cannot see the image) · checks: "
             "the author who posts it", "risk"),
            ("Captions", "relies: a viewer who is deaf or hard of hearing · can check: rarely · checks: whoever "
             "publishes the video", "risk"),
            ("Transcript", "relies: a reader of the record · can check: only with the audio · checks: whoever "
             "files it", "soft"),
            ("Design draft", "relies: a client · can check: what they see, not how it was made · checks: the "
             "designer, who discloses", "soft")]
    for i, (lab, sub, role) in enumerate(rows):
        x = 20 + (i % 2) * 390
        y = 56 + (i // 2) * 142
        f.box(x, y, 370, 124, lab, role=role, kind="step", size=15, sub=sub, sub_size=13)
    f.box(170, 352, 460, 56, "The check belongs to whoever publishes the output", role="verified", kind="human",
          size=15)
    f.text(400, 432, "Orange (hatched in print) = the reader can rarely check · rounded = a person's action",
           size=13, color=muted, width=780)


# ---------------------------------------------------------------- F13.9 credential anatomy
def credential(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "A content credential records a file's history, and a screenshot often leaves it behind", size=17,
           weight="700", width=780)
    f.box(30, 70, 220, 92, "Image file", role="neutral", kind="step", size=15, sub="the pixels", sub_size=13)
    f.box(30, 190, 220, 150, "Credential (C2PA)", role="verified", kind="step", size=15,
          sub="signed statements: captured with … · edited with … · generated with …", sub_size=13)
    f.box(280, 150, 180, 92, "Hash binding", role="soft", kind="step", size=14,
          sub="a fingerprint of the pixels; changes show", sub_size=13)
    f.arrow(252, 116, 300, 152)
    f.arrow(252, 262, 300, 236)
    f.box(530, 70, 250, 100, "Shared as the file", role="verified", kind="step", size=14,
          sub="credential kept: a lead about origin", sub_size=13)
    f.box(530, 220, 250, 100, "Screenshot or re-upload", role="soft", kind="step", size=14,
          sub="new file: credential often stripped (unless stored online and linked)", sub_size=13)
    f.arrow(462, 186, 528, 124)
    f.arrow(462, 206, 528, 266)
    f.text(400, 372, "A credential states history as signed by whoever signed it; it cannot say the scene is true "
           "(C2PA, 2026).", size=13, color=muted, width=780)
    f.text(400, 396, "Gray box = stripped or missing · rectangles = parts of the record", size=13, color=muted,
           width=780)


# ---------------------------------------------------------------- F13.10 present vs absent
def present_absent(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "A signal that is present is a lead about origin; a missing signal proves nothing", size=17,
           weight="700", width=780)
    f.text(330, 64, "Present and valid", size=14, weight="700")
    f.text(620, 64, "Missing", size=14, weight="700")
    rows = [("Content credential", "signed history of the file (not truth)"),
            ("Watermark", "the maker's tool produced it"),
            ("Platform label", "the platform or uploader says AI was used")]
    for i, (sig, pres) in enumerate(rows):
        y = 84 + i * 96
        f.box(20, y, 160, 80, sig, role="neutral", kind="step", size=14)
        f.box(210, y, 250, 80, pres, role="verified", kind="step", size=13, weight="normal")
        f.box(490, y, 290, 80, "proves nothing: stripped, never added, or removed", role="soft",
              kind="step", size=13, weight="normal")
    f.text(400, 392, "Green (mid-gray in print) = a lead about where content came from · light gray cells = proves nothing · "
           "a lead still needs the context checks of section 13.7", size=13, color=muted, width=780)


# ---------------------------------------------------------------- F13.15 protocol card
def protocol_card(f):
    muted = MUTED[f.mode]
    f.text(400, 24, "Your protocol decides in advance what you will check before you act", size=17, weight="700")
    steps = [("1. Triggers", "money, files, urgency, a new channel, proof offered, about to publish"),
             ("2. Pause", "no action and no reply in the same channel"),
             ("3. Channel by role", "the number on the contract; the directory"),
             ("4. Checks by stakes", "section 13.7, stop when the stakes allow"),
             ("5. Record", "verdict and what remains uncertain"),
             ("6. Disclose", "when media you share was generated or altered")]
    for i, (lab, sub) in enumerate(steps):
        x = 20 + (i % 3) * 258
        y = 60 + (i // 3) * 150
        kind = "human" if i in (1, 5) else "step"
        f.box(x, y, 242, 128, lab, role="neutral" if i else "highlight", kind=kind,
              thick=(i == 0), size=15, sub=sub, sub_size=13)
        if i % 3 < 2:
            f.arrow(x + 244, y + 64, x + 256, y + 64)
    f.box(140, 370, 520, 52, "Test it on real items, then revise one rule", role="verified", kind="human", size=14)
    f.text(400, 448, "Thick border = where the protocol starts · rounded = your own action · built on the Hong Kong "
           "police advice (2024) and this chapter's evidence", size=13, color=muted, width=780)


# ---------------------------------------------------------------- F13.19 summary card
def summary_card(f):
    f.text(400, 26, "Chapter 13 — what you can do now", size=18, weight="700")
    cards = ["Built, not recorded: a realistic picture or voice records nothing by itself",
             "Who relies, who checks: the author checks alt text, captions and transcripts",
             "Signals: present = a lead about origin; missing = proves nothing; history is not truth",
             "Looks and scores are leads (clues, not conclusions): people near guessing, detectors weak on new media",
             "Context before pixels: source, channel, earliest version, outside sources",
             "Decide in advance: triggers, pause, a channel you trust, then disclose"]
    for i, c in enumerate(cards):
        x = 20 + (i % 3) * 258
        y = 50 + (i // 3) * 150
        f.box(x, y, 242, 130, c, role="neutral" if i % 2 else "soft", kind="human", size=14, weight="600")


# ---------------------------------------------------------------- reused signatures
ANATOMY_TOKENS = llm_anatomy(stage="tokens", note="Recall from Chapter 3")
FUNNEL_MEDIA = verification_funnel(
    highlight=["check", "primary"],
    note="For media: the primary source is the original file, or the person through a channel you trust",
    notes={"check": "earliest version; outside sources", "primary": "original file, or the person via a known channel"})
ARUP_TREE = failure_tree({"other"}, tag="C10 Arup video conference (2024) · other: misuse (fake media made to "
                         "deceive), documented")
ARUP_CHAIN = failure_chain(
    notes={0: "Pre-recorded fake conference (police believe; confirmed)",
           1: "No check with head office before the transfers (reported: CNN)",
           2: "Instructions followed (confirmed)",
           3: "About HK$200 million lost (confirmed)"},
    highlight={1},
    tag="Tiers: confirmed = the government's reply · reported = CNN, citing police · inferred would be dashed")
PENTAGON = hop_chain(
    [("Image posted", "smoke near the Pentagon; look-alike news accounts", "step", "risk", False),
     ("Reposts", "spread on Twitter that morning", "step", "neutral", False),
     ("Brief market dip", "indices recovered", "step", "neutral", False),
     ("Officials' statement", "no explosion or incident", "step", "verified", False),
     ("Context check", "no witnesses, no other images", "human", "verified", False)],
    notes={0: "Maker and intent not documented", 3: "Pentagon Force Protection Agency; county fire department",
           4: "An open-source investigator (Bond, 2023)"},
    heading="Context, not pixels, settled the Pentagon image (May 22, 2023)",
    foot="Source: Bond (2023), NPR. Reported tier throughout; label: other (misuse), inferred.")

FIGS = [
    ("f13-01-chapter-map", chapter_map, 800, 455, "Chapter 13 at a glance"),
    ("f13-02-storyboard", storyboard, 800, 470, "Every instruction came through a channel the fraudsters controlled"),
    ("f13-03a-anatomy-tokens", ANATOMY_TOKENS, 800, 490, "Recall from Chapter 3: text arrives as tokens"),
    ("f13-03b-modality-tokens", modality_tokens(), 800, 450, "Images and sound arrive as tokens too, beside your words"),
    ("f13-04-pipeline-image", generation_pipeline("image"), 800, 440,
     "A generated image is built from noise toward the prompt, not looked up in a record"),
    ("f13-05-pipeline-voice", generation_pipeline("voice", highlight={"sample"}), 800, 336,
     "In 2023 a research system imitated a voice from a three-second sample"),
    ("f13-06-camera-vs-generator", camera_vs_generator, 800, 426,
     "A camera records an event; a generator produces a plausible picture of none"),
    ("f13-07-who-checks", who_checks, 800, 450,
     "The person who relies on the output often cannot check it, so the author must"),
    ("f13-09-credential", credential, 800, 412,
     "A content credential records a file's history, and a screenshot often leaves it behind"),
    ("f13-10-present-absent", present_absent, 800, 412,
     "A signal that is present is a lead about origin; a missing signal proves nothing"),
    ("f13-13-checklist", media_checklist(), 800, checklist_height(),
     "Check the source and the channel first; inspect the pixels last"),
    ("f13-14-funnel-media", FUNNEL_MEDIA, 800, funnel_height(note=True),
     "For media, the primary source is the original file, or the person through a channel you trust"),
    ("f13-15-protocol-card", protocol_card, 800, 470,
     "Your protocol decides in advance what you will check before you act"),
    ("f13-16-tree-arup", ARUP_TREE, 800, tree_height() + 24,
     "Arup on the tree: misuse of fake media to deceive, documented"),
    ("f13-17-chain-arup", ARUP_CHAIN, 800, 420,
     "The loss followed because no check with head office came before the transfers"),
    ("f13-18-pentagon", PENTAGON, 800, 356, "Context, not pixels, settled the Pentagon image"),
    ("f13-19-summary-card", summary_card, 800, 340, "Chapter 13 summary card"),
]

if __name__ == "__main__":
    only = set(sys.argv[1:])
    for fid, fn, w, h, title in FIGS:
        if only and fid not in only:
            continue
        render(fid, fn, w, h, title, ROOT)
        print("rendered", fid)
