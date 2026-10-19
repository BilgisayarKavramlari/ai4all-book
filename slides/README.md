# Lecture slides

One PowerPoint deck per chapter for CS 2V95.001 (Spring 2027), built in code from a YAML spec so that every deck shares one design and one speaker-notes standard.

| Path | What it is |
|---|---|
| `tools/build_slides.py` | The design system and the builder (layouts, palette, fonts, checks) |
| `tools/preview_slides.py` | Renders a built deck to PNG check images without Office |
| `slides/specs/chNN.yaml` | The content of one deck (written by a content agent) |
| `slides/out/chNN-<slug>.pptx` | Built deck (do not edit by hand; edit the spec and rebuild) |
| `slides/assets/fN-*.png` | Book figures converted from `figures/out/color/*.svg` (2400 px, trimmed) |
| `slides/template/ai4all-16x9.pptx` | Empty 16:9 file with the theme (fonts, colors) for hand-made extras |
| `slides/template/gallery.yaml` → `layout-gallery.pptx` | One example of every layout |
| `build/slides-check/chNN/` | Preview images (`slide-NN.png`, `sheet-N.png`) and `check-report.txt` |

## Build

```sh
export DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib     # cairosvg needs it on macOS
python3 tools/build_slides.py slides/specs/ch01.yaml --preview
python3 tools/build_slides.py --template                 # template + layout gallery
```

The build is idempotent: the same spec gives the same deck; figure PNGs are reconverted only when their SVG is newer. It prints the slide count, the minutes per session (target 75 for `tue` and `thu`) and a list of warnings. **A deck is finished only when the warning list is empty or every remaining warning is a deliberate, explained exception, and you have looked at every preview image.**

## Design (fixed for the whole book)

- 16:9 (13.333 × 7.5 in). Titles in Source Serif 4 Bold, navy; everything else in Source Sans 3. Both are installed here as variable fonts. On a presenting machine without them, install Source Sans 3 and Source Serif 4 (free, SIL Open Font License; static OTFs work best on Windows), present the PDF export, or rebuild with `--fonts Georgia Arial`.
- Palette from `figures/scripts/figlib.py` (Palette F): navy = human action, yellow = AI component, orange-red = risk (always with a thick border), green = verified, pale blue-gray = soft background. Color never carries meaning alone: every colored card or chip also says its meaning in words; dashed outlines mean "conditional" or "inferred", as in the book's figures. Text contrast is checked automatically (≥ 4.5:1).
- Shape grammar as in the book: rounded box = human step, hexagon = AI component, rectangle = step, dashed = uncertainty or inference.
- Type sizes: body text 24–28 pt (floor 24 for bullets), text in cards, tables and step lists ≥ 18–20 pt, diagram sub-labels ≥ 15 pt, captions 16–18 pt, references 16 pt, footer 12 pt. The builder shrinks text to fit only down to these floors and reports an OVERFLOW otherwise.
- At most about 40 words and six lines below the title. Detail goes into the speaker notes.
- Footer on every slide except the title: "AI for All · Ch N · short title" and the slide number. No university logos or trademarks.
- Accessibility: every slide has a real title placeholder (screen readers), every picture carries the book's alt text (from `figures/longdesc/chNN.md`, column "Alt text"; else the chapter's `fig-alt`), reading order follows layout order, tables have a header row.
- Book figures are used where they stay legible at slide size (charts, the Jagged Frontier Map). Text-dense figures are redrawn natively with the same grammar (`compare`, `matrix`, `lanes`, `loop`) so their labels are ≥ 20 pt; the slide's kicker then names the book figure, and the notes point to it.

## Spec format (`slides/specs/chNN.yaml`)

```yaml
deck:
  chapter: 3
  slug: inside-large-language-models          # file name: slides/out/ch03-<slug>.pptx
  title: Inside Large Language Models
  short_title: Inside Large Language Models   # footer
  week: 2
  sessions:
    tue: {label: "Tue, Jan 26, 2027 · concept session", minutes: 75}
    thu: {label: "Thu, Jan 28, 2027 · practice lab", minutes: 75}
    after: {label: "reference slides (not presented)"}
  sources:                                    # files the number check reads
    - chapters/03-inside-large-language-models.qmd
    - labs/ch03-lab1.md
    - docs/syllabus.md
    - figures/longdesc/ch03.md
    - appendix/answers.md
slides:
  - layout: concept
    session: tue          # carried forward until changed: tue | thu | after
    minutes: 3            # class time for this slide (summed per session)
    kicker: "§3.2 · ..."  # small line above the title (optional)
    title: "..."
    ...layout fields...
    notes: {say: ..., background: ..., questions: [...], misconceptions: [...], activity: ..., book: ...}
```

Inline markup in any text field: `**bold**`, `*italic*`. Use curly quotes inside text to avoid YAML escaping.

### Fields common to all layouts

`layout`, `title`, `kicker`, `session`, `minutes`, `notes`, `takeaway` (one-sentence bar at the bottom, where the layout supports it), `figure` (book file id such as `f3-04` or the full id `f3-04-context-window`; a prefix must match exactly one SVG in `figures/out/color/`), `alt` (overrides the book's alt text; ≤ 150 characters), `size` (base text size for that slide; in `compare` it applies to every column without its own `size`), `max_words` (raises the word-count warning threshold for this slide only; use it only for a deliberate exception and say why in a YAML comment above the slide, as `ch01.yaml` does for its side-by-side answers and its five-step worked example).

`deck.draft: true` switches off the notes checks, the session-minute targets and asset pruning (used by `slides/template/gallery.yaml`; never leave it on in a chapter deck).

### Layouts

| Layout | Use | Fields |
|---|---|---|
| `title` | First slide | `subtitle`, `meta` (list of lines), `figure` (optional, on a white card) |
| `session_plan` | Week plan | `columns`: [{`heading`, `sub`, `blocks`: [{`min`, `label`, `detail`}]}] |
| `objectives` | Objectives O1–On in plain words; also the summary | `items`: [{`code`, `text`}] (≤ 6), `intro`, `takeaway` |
| `section` | Divider for each Core subsection (and Thursday) | `number` ("3.2", "Thu"), `tag` (Core/Studio/Deep/Lab), `idea` (one sentence), `meta` ("Book §3.2 · …") |
| `concept` | Bullets, optional figure, optional flow strip | `bullets` (nested list = sub-bullets), `figure`, `figure_side` (right/left), `figure_width` ("auto" or 0–1), `flow`: [{`label`, `kind`: human/ai/step, `role`, `dashed`}], `takeaway` |
| `figure` | One book figure, large | `figure`, `caption`, `takeaway` |
| `compare` | Two or three cards side by side | `columns`: [{`heading`, `role`: human/ai/risk/verified/neutral/soft, `dashed`, `text`, `bullets`, `size`}], `header_height`, `takeaway` |
| `matrix` | 2 × 2 grid (or n × m) | `col_headers`, `row_headers`, `cells` [[{`title`, `text`, `role`}]] (cell title 24 pt, text 20 pt, floor 16), optional `bullets` at left, `takeaway` |
| `lanes` | Rows of flows (e.g., tool types, pipelines) | `rows`: [{`label`, `nodes`: [flow nodes, each may carry `size`]}], `label_width` (inches, default 2.7), `caption` (italic line under the rows), `takeaway` |
| `loop` | Signature diagram 1, AI Work Loop, drawn natively (five rounded human steps around the AI hexagon, wording of `f1-02`) | `highlight` (step or list: drawn dark with a thick border), `step_notes` {Step: text} (replaces a step's sub-label; 15 pt, keep it to about six words), `bullets` (left 40 %), `takeaway` |
| `timeline` | Case story | `events`: [{`label`, `text`, `role`, `tier`: confirmed/reported/inferred}] (3–5), `takeaway` |
| `worked` | Worked example, revealed step by step | `context`, `steps`: [{`label`, `text`}], `reveal`: [2, 5] (steps visible on each slide), `result` (shown on the last reveal), `figure`, `notes_reveal`: one notes block per reveal (each may carry `minutes`) |
| `quiz` | Quick check; the answer slide is generated next | `question`, `options` (MC) or none (open), `answer` (letter, or a list of labels per option for sorting items), `option_tags`, `legend`, `model_answer` (open), `instruction`, `explanation`, `notes` (question slide), `answer_notes`, `answer_minutes`, `title_prefix`. An open question (no `options`) is shown large on a soft card; on the answer slide the question repeats small above the options or the model answer |
| `tps` | Think · pair · share | `prompt` (string or list), `phases`: [{`name`, `min`, `text`}] |
| `lab` | Lab briefing | `goal`, `steps`: [{`text`, `min`}], `side`: [{`heading`, `text`, `role`}] (deliverable, privacy rule, no-device route) |
| `assignment` | Weekly artifact | `due`, `parts`, `rubric`: [{`criterion`, `points`, `full`}], `rubric_title`, `note` |
| `key_terms` | Key terms | `terms` (mark optional ones "(Deep)"), `note` |
| `exit_ticket` | Exit ticket | `questions` (≤ 3), `instruction` |
| `deep` | At most one optional "Going deeper" slide | as `concept`; adds the badge "Going deeper · optional · not on exams" |
| `references` | Sources cited on slides and in notes | `refs` (APA short form), `per_slide` |

### Builder helpers (for whoever extends `tools/build_slides.py`)

New layouts are functions `L_name(ctx, slide, s)` registered in `LAYOUTS`; keep every new field optional so older specs still build. Shared helpers: `text()` (fits text down to a floor and records it for the word, contrast and number checks; pass `record=False` for decoration), `shape()` (book shape grammar: `rect`, `round`, `hex`, `oval`; `dash=True` for conditional or inferred), `to_back()` (puts a full-slide background behind the title placeholder so the title stays first in reading order), `flow()` (a row of nodes with arrows; used by `concept` and `lanes`), `work_loop()` (the AI Work Loop; used by `loop`), `table()`, `picture()` (adds alt text and warns when a figure is placed small) and `takeaway()`. `reflow()` turns YAML block text into notes paragraphs. After saving, `normalize_zip()` fixes the zip timestamps (same spec, same bytes) and `prune_assets()` deletes this chapter's PNGs in `slides/assets/` that no spec names any more.

## Speaker notes standard

Every slide has notes in English, written in the book's terms, built from these fields (the builder assembles them under fixed headings: SAY · INSTRUCTOR BACKGROUND · TIMING AND ACTIVITY · BOOK):

1. **`say`** — what to say: 80–200 words of talking points the instructor can speak almost as written. Use the book's definitions and examples, address students as "you", no anthropomorphic verbs for models ("produces", "generates", not "knows", "thinks").
2. **`background`** — instructor background: the facts behind the slide with source and year, exact study details (sample, measure, limits), dates of anything time-sensitive ("as of October 2026"), and the attribution tier of each case fact exactly as the chapter states it (confirmed = primary record; reported = a named outlet or person, including the authors' own interpretation; inferred = the book's reading). Plus, where useful:
   - **`questions`** — likely student questions with good answers (`q`, `a`);
   - **`misconceptions`** — from the chapter blueprint's misconception list (M1…Mn), each with how to address it (`m`, `fix`).
3. **`minutes`** (slide field) and **`activity`** — class time and instructions for any activity (who does what, for how long, how to debrief).
4. **`book`** — pointer to the passage: "§3.2", "Worked Example '…'", "Check Yourself 3.2", "@fig-3-4", "Lab 3.1", "Appendix E".

Rules: no invented facts. Every number, date and quotation must come from the chapter (which is fact-checked), its labs, the syllabus, the figure long descriptions or Appendix E; the builder's number check flags any number it cannot find in `deck.sources`. Paraphrase; quote at most a few words. Keep the chapter's hedges ("about", "suggests", "consistent with"). Where two book files disagree, follow the chapter text and say so in the background. Answers to even-numbered review items are instructor-only (private/); never show them on a slide.

## Warnings the builder prints

| Warning | Fix |
|---|---|
| `OVERFLOW` / `TABLE OVERFLOW` / `KEY TERMS overflow` | Shorten the text or split the slide (never lower a floor) |
| `N words on slide below the title` (> 50, or the slide's `max_words`) | Cut to about 40 words; move detail to the notes. Kicker, footer and "coming next" placeholders are not counted; `references`, `assignment`, `session_plan`, `lab`, `key_terms`, `title`, `objectives`, `quiz`, `loop` and `lanes` are exempt |
| `NOTES 'say' has N words` | Keep talking points to 80–200 words |
| `NOTES missing 'background'` / `'book' pointer` | Add them |
| `NUMBER NOT IN SOURCES` | Use the chapter's number, or remove it; add a source file to `deck.sources` only if it is a book file |
| `LOW CONTRAST`, `TINY TEXT`, `NO ALT TEXT`, `alt text … characters` | Fix the color, size or alt text |
| `figure … placed small` | Use the `figure` layout, or redraw natively |
| `session tue: N min <-- target 75` | Adjust `minutes` so each session is about 75 |

## Visual check

`--preview` writes `build/slides-check/chNN/slide-NN.png` (1600 × 900), contact sheets `sheet-N.png` (12 slides each) and `check-report.txt` (text that does not fit its box, also outlined in red on the image). The preview uses the same fonts and wrapping as the builder; PowerPoint's own wrapping can differ by a word, so leave a little room. Look at every sheet, and open single slides for figures. (PowerPoint and Keynote could not be scripted here without permission dialogs; if they can be on another machine, a PDF export is a useful second check.)

## Instructions for a chapter content agent

1. Read: this README; `slides/specs/ch01.yaml` (the pilot, the quality bar); your chapter `chapters/NN-*.qmd` in full; `docs/blueprints/chNN-blueprint.md` (objectives, misconceptions M1…); `labs/chNN-lab*.md`; `figures/longdesc/chNN.md`; your week in `docs/syllabus.md` (dates, readings, artifact, due date); your chapter's block in `appendix/answers.md` (odd answers only); `docs/production/instructor-package.md` (your chapter's assets); `docs/production/chapter-brief.md` (book-wide rules).
2. Write only `slides/specs/chNN.yaml`. Do not edit chapters, figures, figure scripts, `tools/` or `_quarto.yml`.
3. Structure (adapt to the chapter and its week; for shared weeks, split the 75 minutes as the syllabus and decisions D22/D23 say): `title` → `session_plan` (Tue + Thu, minutes from the syllabus flow: opening case 10 · concept core 35 · demonstration 20 · concept check 10; lab briefing 10 · group practice 45 · share and critique 15 · exit step 5) → `objectives` (O1–On in plain words, ≤ 12 words each) → Opening Case as a `timeline` (with attribution tiers) and its figure → for each Core subsection: a `section` divider, 1–3 content slides using the chapter's figures (signature diagrams where the chapter uses them; `loop` with the chapter's highlighted step), and a `quiz` from that section's Check Yourself or an odd-numbered review item (answer on the next slide) → at least one `worked` example revealed over 2–3 slides → "Before Thursday" → Thursday `section` divider, warm-up `quiz`, `lab` briefing (goal, steps with minutes, deliverable, privacy rule, no-device route from the lab sheet), the week's `assignment` (brief, rubric summary, due date from the syllabus), a work-time slide, `tps` share-and-critique → summary (`objectives` layout with takeaway) → `key_terms` → `exit_ticket` → optional one `deep` → `references` (APA short form, from the chapter's reference list, for every source cited on slides or in notes). Aim for 30–45 slides; a deck that runs a little over because of quiz answer slides is acceptable.
4. Notes on every slide per the standard above. Use the chapter's misconception list. Mark every case fact's tier as the chapter does. Tool neutrality: no click paths; Compass is optional, free and ungraded.
5. Build with `--preview`, clear every warning (or justify it in a YAML comment), and look at every contact sheet and at single slides with figures. Fix overflow, tiny text, small figures (switch to `figure` or a native layout), and crowded slides.
6. Report: slide count, minutes per session, remaining warnings with reasons, any conflicts found between book files, and anything only the author can supply.
