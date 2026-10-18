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

## Book-wide rules added during production

- **Case ids** are assigned by the editor (registry: docs/production/case-ids.md). Use the id given in your prompt; never pick one yourself.
- **Deep Chapter 6 terms:** Core chapters (12, 14, 15, 19) may point to Chapter 6 but must define any Chapter 6 term they use (context layers, in-context example, standing instructions, memory, prompt chain) in their own Core text.
- **Terminology fixed by Chapter 6:** "in-context example" (never a bare "example", which the glossary defines as a dataset item); "test inputs" (not "test set") for prompts tried on a template; "standing instructions" for a user's persistent instructions; "system prompt" only for the provider's or developer's layer; "memory" = a product feature that stores notes; "prompt chain" = a person-run multi-step workflow; workflow vs. agent per Anthropic (2024).
- **Failure labels (from Chapter 4):** every case file and case study labels its failure on Signature 5 (Failure Taxonomy Tree: hallucination, bias, context loss, overconfidence, security vulnerability; outdated information and wrong calculation are leaves of hallucination; sycophancy is a leaf of overconfidence), with a primary and optional secondary branch, each marked documented (solid) or inferred (dashed). Import `failure_tree` from figures/scripts/ch04_figures.py.
- **Boundaries:** Chapter 4 explains why failures happen; Chapter 8 owns detection and verification methods (fabricated-citation rates, calibration measurement); Chapters 15, 16, 18 and 10 own security, fairness, liability and disclosure respectively.
- **work_loop(highlight)** in ch01_figures.py accepts one step name or a list of step names.
- **Chapter 5/6 boundary:** Chapter 5 (Core) labels the prompt part "in-context examples", defines it in Core with one illustration; Chapter 6 (Deep) owns choosing, balancing, ordering and testing them. Both use "test inputs". Chapter 5 ends at single-prompt iteration; Chapter 6 starts at reuse across inputs.
- **Examinable scope (D20):** Core sections only; Deep chapters 6, 13, 17, 22, 23 and all Deep sections are not examinable.
- **Reading order differs from chapter order** (syllabus): weeks 1–5 read Ch. 1 → 2, 3 → 5 (+6 Deep) → 7 → 4 + 8. Chapters 5, 6 and 7 must not depend on Chapter 4; Spaced Review draws on the chapters read just before in reading order. Student-facing Failure Taxonomy Tree labels start in Chapter 8.
- **Tree vs. chain:** the Failure Taxonomy Tree labels output and system failures; human and workflow failures (overreliance, no approval gate, inappropriate delegation, data leakage by a user) are labeled on a link of Chapter 4's failure-to-harm chain. One uncertainty pair everywhere: documented / inferred (solid / dashed). Label overconfidence only with evidence about expressed certainty.
- **Failure Diary prompts:** Chapters 3, 5 and 7 each add one line in a lab or Your Turn: "Save this for your Failure Diary (Chapter 4)" — so students arrive in week 5 with entries.
- **Reading rate:** estimate Core reading time at 150 words per minute, and add "longer if English is not your first language". Use the same rate in every chapter.
- **Agency ≠ agent:** the AI Fluency framework's "agency" mode (configuring AI to act on your behalf, Dakan & Feller v1.1) is not the same as an "agent" (a system in which the model chooses its own steps and tool calls; adapted from Anthropic, 2024). Chapter 5 introduces the distinction in a short box; Chapters 6, 7 and 14 reuse it.
- **Shared terms owned by one chapter:** "in-context example" is defined in Chapter 5 Core and reused word for word in Chapter 6; Sclar et al. (2024) prompt sensitivity is owned by Chapter 5 (Chapter 6 points back); test-input labels in both chapters are "typical, different, edge".
- **Verdict scale (from Chapter 8), used book-wide:** supported · partly supported · unsupported · contradicted · cannot verify. Signature 8 is `verification_funnel(highlight, verdict, tag, note)` in figures/scripts/ch08_figures.py. Chapter 8 defines "independent source" and "primary source"; Chapter 9 owns the reliability ladder, lateral reading and summary fidelity. An AI tool's own "yes" is never a source.
- **Calibration:** one glossary term, sense-labeled ("calibration (of your own confidence)" from Chapter 7; a model's calibration from Chapter 8), definitions reused word for word.
- **Time statements:** give two honest numbers at 150 wpm: Core sections (body) and the whole Core package (body + Studio + case + summary + end-of-chapter items students are expected to do), plus "longer if English is not your first language". Assignment home time is estimated per requirement (count runs, sources, annotations), not guessed. Glossing rule: every technical, legal or idiomatic term gets a plain gloss at first use in each chapter, even if an earlier chapter defined it.
- **Chapter 9/10 boundary:** Chapter 9 owns reference-list citation of sources and of AI output (APA 2025 guidance); Chapter 10 owns disclosure of AI use in prose and at work. "Outside source" (Chapter 9) = not written or paid for by whoever is behind the page being checked; it complements Chapter 8's "independent source".
- **Attribution tiers for cases:** confirmed (primary record) · reported (named outlet or person) · inferred (the book's reading). State the tier whenever a case fact is not in the primary record.
- **Multiple-choice items:** rotate keys across (a)–(d) roughly evenly; the key is never systematically the longest or the only hedged option; every distractor comes from a named misconception. Faded examples always have at least the first step filled in.
- **Instructor-package dependencies:** add a `## Instructor package` section (9th) to your handoff listing every asset the chapter promises on eLearning or in Compass (dated sample outputs with model and date, card sets, provided texts, templates, accessible versions), with the date it is needed by (the lab's session date).
- **Weekly workload target:** out-of-class time per week ≤ 2.2 h (syllabus 1–2 h), counted honestly (reading at 150 wpm, Your Turns, assignment by requirement). If over, cut or make readings recommended and record the decision; never state a lower number than the count.
- **Midterm Bridge (Chapter 10):** a review figure plus exam-format items on the Core sections of Chapters 1–9, separate from Spaced Review; offered to Appendix D's practice exam.
