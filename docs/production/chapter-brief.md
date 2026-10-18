# Chapter production brief (for chapter agents)

Mandate (2026-10-18): the author asked the editor to finish the whole book without asking him (decision D19). Chapter agents work under that delegation: make the editorial choices yourself, record them, and list anything only the author can supply. Chapters 1 and 2 are the quality bar; Chapter 2 is the closest model (same pipeline, same files).

## Read first (every agent)

CLAUDE.md (non-negotiable rules) · docs/chapter-anatomy.md · docs/style-sheet.md · docs/visual-guide.md · docs/decisions.md · docs/book-map.md · docs/syllabus.md (your week, LO list, artifact) · docs/characters.md (rotation table and fixed details; **Hana uses they/them**) · cases/index.csv (your chapter's case) · docs/voice/voice-profile.md · docs/glossary.md (reuse existing definitions word for word).

Model files from Chapter 2: docs/blueprints/ch02-blueprint.md, docs/blueprints/ch03-blueprint.md (v0.2 format), chapters/02-how-machines-learn-from-data.qmd, docs/editorial/ch02-dev-memo.md (**the list of mistakes the Chapter 2 draft made — do not repeat them**), labs/ch02-lab*.md, cases/C02-recruiting-tool.md, figures/longdesc/ch02.md, figures/scripts/ch02_figures.py, figures/scripts/ch02_charts.py, figures/scripts/figlib.py, appendix/answers.md (Chapter 2 part), private/ch02-answers-even.md.

## Pipeline per chapter (NN = two-digit chapter number)

1. **Blueprint** → docs/blueprints/chNN-blueprint.md in the Chapter 3 v0.2 format: outcome link and week, workload, 4–6 objectives (Bloom · LO · framework tags), misconceptions (3–6), concept sequence (5–8 subsections tagged Core/Studio/Deep, one core idea each), example plan (worked → faded → your turn per skill), retrieval and spacing, alignment matrix, the syllabus artifact with a 10-point four-level rubric and an alternative assignment (if the artifact is hosted here), figures (titles state findings), labs, risks, "Decisions taken under delegation". Then an independent blueprint review is run and applied (v0.2). The blueprint counts as approved under D19.
2. **Draft** → chapters/NN-*.qmd (keep the existing file name and the first heading line with its {#sec-chNN} id). Full anatomy, ≥ 10,000 words, Core within the blueprint's word budget. Plus figures, labs, case file, answers, long descriptions (step 3).
3. **Build-outs:** figures/scripts/chNN_figures.py (+ chNN_charts.py for data charts from data/chNN_*.csv), rendered to figures/out/{color,gray}/fN-*.svg by running the scripts; labs/chNN-labK.md; cases/CXX-*.md (your case id from cases/index.csv); figures/longdesc/chNN.md; private/chNN-answers-even.md; **docs/production/handoff/chNN.md** (see below).
4. **Four independent reviews** run in parallel by the editor (subject expert, pedagogy, student panel, fact-checker → docs/factcheck/chNN.csv + chNN-sources.md). You do not see each other's reports until the editor passes them to you.
5. **Revision**: apply the reviews, write docs/editorial/chNN-dev-memo.md (Chapter 2 format: decisions table with reasons, "not changed" with reasons, "waiting for the author"), and a light Mode B voice pass (voice-profile §10; never invent anecdotes).
6. **Final review** by an independent reviewer; the editor passes you its must-fixes; fix them.
7. The editor renders, checks figures visually, merges handoff files and commits. **Agents never commit, push, edit shared files or edit other chapters.**

## Files you may write

Only your own chapter's files: chapters/NN-*.qmd, docs/blueprints/chNN-blueprint.md, docs/editorial/chNN-dev-memo.md, figures/scripts/chNN_*.py, figures/out/{color,gray}/fN-*.svg, figures/longdesc/chNN.md, data/chNN_*, labs/chNN-*.md, cases/CXX-*.md, private/chNN-answers-even.md, docs/production/handoff/chNN.md, and scratch files under build/chNN/. **Do not edit** figlib.py, other chapters' files, docs/glossary.md, docs/characters.md, docs/decisions.md, docs/status.md, docs/refresh-list.md, docs/ai-use-log.md, figures/index.csv, cases/index.csv, appendix/answers.md, _quarto.yml — put what they need in your handoff file.

## Handoff file (docs/production/handoff/chNN.md)

Sections, in this order, each ready to paste:
1. `## Glossary rows` — `| Term | Definition | Türkçe |` rows for new Key Terms (reuse existing glossary wording for terms already there; list changed definitions separately with a reason).
2. `## Characters log rows` — `| 2026-MM-DD | Ch. NN | Name | Detail |`.
3. `## Figure index rows` — CSV rows in figures/index.csv format.
4. `## Case index row` — the updated CSV row for your case id.
5. `## Refresh-list rows` — time-sensitive claims.
6. `## Decisions` — D-style rows for decisions taken under delegation that affect the whole book.
7. `## Appendix E (odd answers)` — a `## Chapter NN` block in the appendix/answers.md format.
8. `## Author-only items` — things only the author can supply (personal anecdotes, approvals of commercial disclosures, money, credentials).

## Writing rules that the Chapter 2 reviews enforced

- Every factual claim has a source and year; paraphrase; at most one quotation under 15 words per source; **attribute statements exactly** (who said it: the company, unnamed sources, the authors); mark the book's own inferences as such ("this book reads…", "if…").
- Experiments, studies and numbers described exactly (sample, what was measured, model and date); conclusions limited to what the evidence shows.
- No anthropomorphic verbs for models ("looks at", "reads", "thinks", "knows", "learns that", "is tempted", "safe"): use "receives", "scores", "produces", "the training procedure adjusts".
- Define every acronym and term at first use **in Core**; every Check Yourself answerable from Core; refutation text must not create a new misconception.
- One core idea per subsection; worked → faded (genuinely partly filled) → Your Turn for every skill in the blueprint.
- Review A distractors from the misconceptions, without absolute giveaways ("always", "never", "immune"); tags O · LO · Bloom correct; odd answers in the handoff file, even answers in private/.
- Rubrics: four parallel levels without gaps, criteria scored separately, declaration elements listed (tools, purpose, accepted/rejected/revised, how verified, your judgment); an alternative assignment for the artifact.
- Cross-references follow docs/book-map.md exactly (check chapter numbers and titles).
- Characters per the rotation; log every new fixed detail; never contradict characters.md; they/them for Hana.
- From the Field: only from the author's own writing (docs/voice/ybs-inventory.md lists Drive IDs; read the file with the Google Drive connector and tools/drive2md.py), facts limited to the source, present-day connections marked as such; disclosure for anything commercial uses D16 wording. If nothing fits, write `[FROM THE FIELD: author case needed]` and list it under Author-only items — **never invent**.
- Tool neutrality: no click paths; current tools live in Compass ([COMPASS: …] placeholders).
- Dated content: "as of October 2026"; anything that will age goes to the handoff refresh-list rows.
- American spelling; house style without a serial comma in simple lists (match Chapter 2).

## Figures

- figlib.py grammar: rect = step, rounded = human, hexagon = AI, diamond = decision, dashed = uncertainty; risk = thick border (hatched in gray); ≤ 9 boxes; minimum font 13 px; title states the finding; every figure in color and gray.
- **Signature diagrams are reused by importing the drawing function from the chapter that introduced them** (e.g., `from ch02_figures import pipeline`), never redrawn differently. New signatures (see visual-guide.md table) are written as reusable functions with a `highlight` argument.
- Data charts only from data/chNN_*.csv with a source line; numbers in text copied from the CSV; computed experiments are reproducible scripts with seeds and versions recorded.
- Alt text ≤ 150 characters, identical in the chapter and in figures/longdesc/chNN.md; long descriptions for complex figures; the longdesc table is keyed by source ID (FN.k) and file id.
- Check layouts by reading the SVG coordinates carefully (overlaps, text outside boxes, labels on lines); the editor also checks renders visually.

## Report back

End each stage with a short report: files written, word counts (Core / total), figure count, open [VERIFY] items, author-only items, and anything the editor must decide.
