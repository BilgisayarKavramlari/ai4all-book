# Chapter 6 blueprint — Context Engineering and Reusable Workflows

Status: v0.1 (2026-10-18), written by the Chapter 6 agent under delegation (D19). Waiting for the editor's independent blueprint review; v0.2 will apply it. No chapter text is written until v0.2.
Part II — Working with AI · Syllabus week 3 (read alongside Chapter 5) · Path: **Deep** (optional extension; the syllabus lists "D: Ch. 6" for the Thu Feb 4 lab) · Featured student: **Sam** (per the rotation in docs/characters.md; no other recurring character) · Work Loop step highlighted in the Chapter Map: **Prompt** (design what the model receives), with Verify second (test before you reuse).

**Source material.** No Haliç lecture covers this chapter; it is built from the cited research and documentation below. The week-3 concept session (framing a task; vague vs. framed prompt) and Thursday's prompt-iteration sprint belong to Chapter 5; Chapter 6 extends that lab for students who want more. From the Field: the author's 2018 article on CRISP-DM (YBS Ansiklopedi, in Turkish; Drive 1eES0f0OQwHiRuvUB8LVTkhMGi1SddAxY), read in full for this blueprint (see §5 and Decision 6).

**Boundaries with other chapters.** Chapter 3 explains the context window mechanically (tokens, what must fit, "lost in the middle" as a diagnostic). Chapter 5 teaches framing and iterating a single prompt and introduces Signature 6, Anatomy of a Prompt (role, task, context, constraints, examples, output format). **Chapter 6 owns context design**: what to include and leave out, order and labels, in-context examples, documents, standing instructions, project spaces and memory (tool-neutral), reusable prompts and templates, and simple multi-step workflows (prompt chains) run by a person. Chapter 12 owns tool choice (which tool offers which feature); Chapter 14 owns agents (the model chooses its own next steps) and approval gates; Chapter 15 owns privacy, security and prompt injection (what never to paste; Chapter 6 points there in one sentence each time). Chapter 5's blueprint (docs/blueprints/ch05-blueprint.md) did not exist when this was written; see Risk 1.

## 1. Outcome link and week 3

| Item | Value |
|---|---|
| Syllabus outcomes | **LO2** (frame a task and improve results through deliberate, documented iteration); secondary **LO3** (verify outputs: testing a template is verification) |
| Artifact | **Personal prompt library — optional, ungraded.** It is not one of the 13 graded weekly artifacts (A1–A7, A9–A14; docs/syllabus.md). The book offers a 10-point rubric for self-check and instructor feedback, an alternative assignment, and suggests reusing the library in A11 (workflow blueprint, Ch. 14) and A13 (domain workflow prototype, Ch. 19). No syllabus change |
| In-class time | None required. Thu Feb 4 (A3 prompt-iteration sprint, Ch. 5): Lab 6.1 is offered as the "D: Ch. 6" extension for teams that finish early, or at home |
| Readings | None beyond the chapter. Further Reading points ahead to R11 (Anthropic, 2024, assigned in week 11) |

### Week 3 workload (out of class)

| Item | Time |
|---|---|
| Chapter 5 Core reading, R2 module 2, A3 | set by the Chapter 5 blueprint (required) |
| **Chapter 6, fast route** (Chapter Map, 6.1, 6.6, Summary) | ~25 min, optional |
| Chapter 6, full route (6.1–6.7, Case Study) | ~70 min, optional (longer for ESL readers) |
| Lab 6.1 at home (if not done in class) | 30 min, optional |
| Personal prompt library | 60–90 min, optional; can be built across weeks 3–11 |

Because the chapter is optional, it adds nothing to the required 1–2 hours. The Chapter Map says so in its first line.

**Word budget.** No Core subsections, so no Core cap. Subsections run ~900–1,400 words (below the anatomy's 1,500–2,500, as in Chapters 2–3) so the full route stays near 70 minutes; the chapter still reaches ≥ 10,000 words with the Opening Case, Case Study, Ethics Lens, Career Connection, From the Field, labs and the End-of-Chapter Package. Planned: Opening 500 · Objectives and Warm-up 300 · 6.1–6.7 ≈ 8,100 · Labs 800 · Case Study 1,000 · Ethics 450 · Career 400 · From the Field 450 · Summary 450 · End-of-Chapter Package 2,200 · Further Reading 250 → ~14,900 words including tables and boxes (≥ 10,000 of running prose).

## 2. Chapter objectives (6)

| # | Objective — after this chapter you will be able to… | Bloom | LO | Framework tags |
|---|---|---|---|---|
| O1 | **Explain** the layers of context a model receives in a chat tool (system prompt, standing instructions, project files and memory, conversation so far, documents, examples, your message) and which of them you control | Understand | LO2 | UNESCO:TECH-U · 4D:DESC |
| O2 | **Construct** the context for a task: select relevant excerpts, label and order them, and decide what to leave out | Apply | LO2 | 4D:DESC · UNESCO:TECH-A |
| O3 | **Judge**, from a test on several inputs, whether in-context examples improved an output, and choose balanced examples | Evaluate | LO2, LO3 | 4D:DISC · 4D:DESC |
| O4 | **Evaluate** what belongs in standing instructions, a project space or memory, and audit what is stored there | Evaluate | LO2 | 4D:DIL · 4D:DESC |
| O5 | **Create** a reusable prompt template with placeholders, test it on at least three inputs (including an edge case), and record it with a version in a personal prompt library | Create | LO2, LO3 | 4D:DESC · 4D:DISC · UNESCO:TECH-C |
| O6 | **Design** a two- or three-step prompt chain with a human check between steps, and explain why it is a workflow, not an agent | Create | LO2 | 4D:DEL · 4D:DESC |

UNESCO level codes follow the ai4all-frameworks skill; no sub-competency numbers are used.

## 3. Prerequisites and promises kept

From Chapter 1: AI Work Loop; same prompt → different answers; verify before you reuse. From Chapter 3: token, context window, system prompt, retrieval, training vs. inference (settings fixed at inference; no learning from your chat), "lost in the middle" (Liu et al., 2024). From Chapter 4: the Failure Taxonomy Tree, including context loss. From Chapter 5: Anatomy of a Prompt (Signature 6), framing, the iteration log (A3). **Promises kept:** Chapter 3 §3.4 says "designing context is Chapter 6"; Chapter 5's "context" and "examples" elements are where this chapter zooms in. Because the chapter is optional, it re-explains in one or two sentences every earlier term it relies on.

## 4. Misconceptions (refutation pattern; six)

| # | Misconception | Where |
|---|---|---|
| M1 | "The model receives only the message I just typed" | Opening Case, 6.1 |
| M2 | "More context is always better: paste the whole document" | 6.2 |
| M3 | "Examples in my prompt teach the model, so more examples always help" (refuted: settings do not change at inference, Ch. 3; examples steer format and pattern within that context only; order and balance matter; for some newer models examples hurt) | 6.4, Case Study |
| M4 | "Memory means the model has learned about me, and what it stored is complete and correct" (hedged: memory is a product feature that stores notes and adds them to later contexts; notes can be wrong, stale or missing) | 6.5 |
| M5 | "A prompt that worked once will work every time, on every input and every model" | 6.6, Case Study |
| M6 | "Once a task is split into steps, it runs itself: a chain is an agent and needs no checks" | 6.7 |

Refutation text states the correct idea first and restates the misconception only once, so it does not create a new one (Chapter 2 lesson).

## 5. Concept sequence

**Session question, answered in the Summary:** *If the model is the same, why do two people get such different results from it?* Answer: much of the difference lies in what the model receives (the context someone builds, the examples they choose, the steps they split the task into) rather than in the model; and whether a design helps must be tested, because the same design can stop working when the input or the model changes.

**Opening Case (450–550 words): Medprompt — same model, different context.** A research finding, stated as such, with model name and date in the first paragraph. In November 2023, Microsoft researchers reported that GPT-4, with no fine-tuning (its settings unchanged), scored 90.2% on the MedQA multiple-choice benchmark (U.S. medical-licensing-style questions) when they changed only what it received and how often it was asked: for each question, five similar solved questions chosen automatically as examples, worked reasoning written for those examples, and five runs with the answer options shuffled, combined by majority vote. A simple five-example prompt scored 81.4% (Nori et al., 2023). Chapter question: *what changed, if not the model?* Limits stated in the case: a multiple-choice benchmark is not clinical practice, and the authors could not rule out that test questions appeared in the training data (Nori et al., 2023). The twist (a year later, the same team found that examples *lowered* the scores of a newer reasoning model; Nori et al., 2024) is held for the Case Study. *Departure from the book map (which lists "From the Field" as the case): the Opening Case slot needs a real, cited event (anatomy part 2), so From the Field moves to its own part 11 (Decision 5).*

**Prediction before the evidence (6.2):** "You add one irrelevant sentence to a school math word problem. Does the model's accuracy go up, stay the same, or go down?" Answered with Shi et al. (2023): for one 2023 model (code-davinci-002) with step-by-step prompting, accuracy fell from 95.0% on the original problems to 72.4% on versions with an irrelevant sentence; an instruction to ignore irrelevant information recovered part of the drop (77.8%) [VERIFY table values against the PDF].

**Second prediction (Case Study):** "Which part of Medprompt do you predict added most: the examples, the worked reasoning, or the shuffle-and-vote?" Answered from the paper's ablation (reasoning +3.4, examples +2.2, shuffle-and-vote +2.2 points on MedQA), with the authors' caveat that the order in which components were added affects these numbers.

| # | Subsection | Tag | One new core idea | Examples | Figures |
|---|---|---|---|---|---|
| 6.1 | What the model actually receives | Deep | The model receives one long input assembled in layers, most of which you did not type in this message: the product's system prompt, your standing instructions, project files and memory, the conversation so far, documents and retrieved text, examples, and your message. *Context engineering* = deciding what goes into that input (term popularized in June 2025: Lütke; Karpathy; via Willison, 2025). The system-prompt layer is real and usually hidden: one provider began publishing its consumer system prompts in August 2024 (Anthropic, 2024a) | **Sam** asks for this week's robotics-club update; the chapter lists every layer the model received (worked); a design student's chat with a style file (faded) | F6.2 Context layers (first build) |
| 6.2 | Choosing what to include | Deep | Relevant, bounded context beats volume: irrelevant material distracts (Shi et al., 2023); long inputs are used unevenly (Liu et al., 2024; Hong et al., 2025); select excerpts, name each one's source and date, and say what to do when the material lacks the answer. One-sentence pointer: what never to paste → Ch. 15 | **Sam** checks units in a lab-report results table: two pages of an 80-page lab manual plus the table, not the whole manual (worked); a history student picks which of five primary-source passages to include (faded); a customer question with a provided policy document (Your Turn, business) | F6.3 excerpts vs. whole document; F6.4 published values (Shi et al., 2023) |
| 6.3 | Labels and order | Deep | Structure changes use: label each part (instructions, material, examples, question) with headings or delimiters; keep instructions separate from material; put the task and key instructions where they are used most reliably (start or end, per Liu et al., 2024, stated as a pattern to test). Small format changes can swing results (Sclar et al., 2024). Pointer: text inside a document can contain instructions → prompt injection, Ch. 15 | **Sam**'s lab-report context rebuilt with labels (worked); reader orders a provided jumbled context (faded) | F6.5 labeled context layout |
| 6.4 | Examples in the context | Deep | An *in-context example* shows the pattern and format you want (few-shot prompting; Brown et al., 2020); it changes the output only within that context, not the model's settings (Ch. 3). Choice, balance and order matter (Lu et al., 2022; Zhao et al., 2021); the format of examples can matter more than whether each label is right (Min et al., 2022, with the counter-finding of Yoo et al., 2022 [VERIFY]); for some newer models examples hurt (Nori et al., 2024): test with and without | Coding open-ended survey answers with three balanced vs. three one-sided examples (social science; constructed outputs, labeled); a teaching assistant chooses three of six candidate feedback examples (education, faded) | F6.6 balanced vs. one-sided examples (illustrative) |
| 6.5 | Standing instructions, projects and memory | Deep | Three persistent features fill context layers automatically: *standing instructions* (custom or project instructions, instructions files), *project spaces* (files attached to every chat in a project), *memory* (notes the product stores and adds to later contexts). They give consistency but are invisible, can go stale, and carry privacy risk (Ch. 15); memory is not training (Ch. 3). Dated box "as of October 2026", at least two providers (OpenAI, 2024; Anthropic, 2024b; Google, 2024), no click paths; current steps in Compass. Routine: review and prune | **Sam**'s standing instruction ("SI units; show every conversion") and a stale memory note ("Sam is on co-op", true only last year) (worked); reader sorts eight items into standing instructions / project file / this chat only / never store (faded); Lab 6.4 (Your Turn) | F6.2 reused with layers 2–3 highlighted (F6.7) |
| 6.6 | Reusable prompts: templates and your library | **Studio** | A prompt becomes reusable when it is *parameterized* (fixed parts + placeholders), *tested* (typical, different and edge inputs, with pass criteria), and *versioned* (number, date, tool and model tested on, what changed). A library entry also says when not to use it. Builds the optional artifact | **Sam** turns his club-update prompt into template v1.0; it fails on a meeting with no decisions; v1.1 adds "if no decisions, say so" (worked); a nursing student's template for summarizing a *public* drug leaflet, test record partly filled (health, faded, no patient data); Lab 6.1 and the library (Your Turn) | F6.8 template anatomy (Signature 6 import with placeholders); F6.9 test record; F6.10 library entry card |
| 6.7 | Simple multi-step workflows | Deep | A *prompt chain* splits a task into fixed steps; each step's output becomes the next step's input; a person checks between steps, so errors surface where they start (Wu et al., 2022). When one prompt is enough. Workflow vs. agent: in a workflow the steps are fixed in advance; in an agent the model chooses its next steps (Anthropic, 2024c); agents and approval gates → Ch. 14 | **Sam**'s three-step chain: extract decisions and action items → Sam checks names and dates against his notes → draft the email (worked); a business report-summary chain with the check step missing: reader adds it (faded); Lab 6.3 (Your Turn) | F6.11 chain with a check; F6.12 workflow vs. agent (contrast; does not draw Signature 9) |

Other anatomy parts:

| Part | Plan |
|---|---|
| Case Study (1 main + 2 short) | **Main: Medprompt, revisited** — traced through Context Layers (examples layer = similar solved questions chosen per question; worked reasoning; repeated runs = a simple workflow); the ablation prediction; the twist: with a newer reasoning model (o1-preview), examples lowered performance, and the model without any of these techniques beat GPT-4 with Medprompt (Nori et al., 2024) [VERIFY numbers]. Lesson: a context design is tied to a model and a date; re-test when either changes. Disclose: authors are Microsoft researchers (the 2024 paper also lists OpenAI authors [VERIFY]); benchmark ≠ clinical use. **Short 1:** example order and balance (Lu et al., 2022; Zhao et al., 2021; GPT-3-era models, stated). **Short 2:** irrelevant and long context (Shi et al., 2023; Hong et al., 2025, an industry technical report from a company that sells retrieval software, labeled as such). Short cases labeled on the Failure Taxonomy Tree (Signature 5, imported from ch04_figures) as *context loss* |
| Ethics Lens | **Invisible instructions.** Standing instructions, memory and system prompts shape outputs that readers of your work never see. Transparency (publishing system prompts as one provider's practice, 2024), accountability for shared templates at work (who answers for a template's wrong reply), and templates that encode a bias (a screening template that repeats Chapter 2's recruiting-tool pattern; pointer to Ch. 16). One line on others' data in context → Ch. 15 |
| Career Connection | Support knowledge-base or operations specialist (reply templates tied to a policy document); paralegal or legal-operations specialist (clause and checklist libraries); marketing content specialist (brand-style standing instructions); quality or manufacturing engineer (standard work instructions become templates; Sam's co-op field); instructional designer or teaching assistant (rubric-based feedback templates). Descriptive only; no salary or demand numbers unless cited |
| From the Field | **The author's CRISP-DM article (Şeker, 2018).** Facts limited to the article: CRISP-DM is a six-step process (business understanding, data understanding, data preparation, modeling, evaluation, deployment) with loops, the most important one returning from evaluation to the start; the article reports that practitioners who use it for long adopt its rule of starting from the business problem, not from "what project can I make from this data?"; it lists roles per step and notes that tools such as SPSS Modeler build the steps in. **Present-day connection, marked as the book's:** a prompt-library entry is a small process standard; its test step plays the role of CRISP-DM's evaluation loop; "start from the task, not the tool". Turkish source, paraphrased, cited with year; original guide cited for the six phases (Chapman et al., 2000). Not commercial: no D16 disclosure needed (see Author-only item 1) |
| Summary + Key Terms | Answers the session question; Context Layers complete as the summary visual (F6.13 card); Key Terms list (§8) |

## 6. Example plan (worked → faded → your turn)

| Skill | Worked | Faded (genuinely partly filled) | Your Turn |
|---|---|---|---|
| Mapping context layers (O1) | Sam's club-update chat: a table of every layer the model received, who set it, whether Sam could see it | A design student's chat inside a project with a brand-style file: three of seven layers filled | Map the layers of your own last AI conversation (layer types only, no content) |
| Selecting and ordering context (O2) | Sam's units check: which two manual pages and why; labels; task placed last | History: five primary-source passages, two already marked include/exclude with reasons; reader decides the other three and the order | Business: a provided policy document and a customer question; build the context (Lab 6.2 extends it) |
| Choosing and testing examples (O3) | Survey coding: three balanced vs. three one-sided examples; constructed outputs labeled as such; what changed | Education: six candidate feedback examples, two chosen with reasons; reader picks the third and predicts its effect | Lab 6.2 step 4: run one task with and without examples on three inputs; judge |
| Persistent features (O4) | Sam's standing instruction and stale memory note; what he keeps, edits, deletes | Eight items, three already sorted into standing instructions / project file / this chat only / never store | Lab 6.4: audit your own standing context (or a provided sample) |
| Template, test, version (O5) | Sam's template v1.0 → edge-case failure → v1.1 with a version note | Nursing student's leaflet-summary template: test record with the typical input done, the edge input left to the reader | Lab 6.1; the personal prompt library |
| Chain with a check (O6) | Sam's three-step chain with his check between steps 1 and 3 | Business report summary: a two-step chain with no check; reader inserts the check and its pass criteria | Lab 6.3 |

Fields: engineering (Sam), arts and design, history, business, social science, education, health (public leaflet; Medprompt). Sam is the only recurring character; others are unnamed one-off figures. Every AI output is labeled "constructed example" or carries model name and date.

## 7. Retrieval and spacing

- **Warm-up (3):** When you type a message in a chat tool, what else might the model receive? If you paste a 50-page document, are all pages used equally well? If examples in your prompt improve today's answer, has the model learned from them?
- **Check Yourself** after 6.1–6.7, 2–3 items each, at least one "why", all answerable from that subsection's own text (there is no Core to fall back on).
- **Spaced Review (two previous chapters, plus one Ch. 3 item):** Ch. 4 (context loss on the Failure Taxonomy Tree; a chatbot answering from the wrong policy, *Moffatt v. Air Canada*, asked as a question about what context it needed, not as a claim about its cause); Ch. 5 (the six parts of Anatomy of a Prompt; what an iteration log records); Ch. 3 (context window; inference does not change settings). Ch. 4 and Ch. 5 items are finalized after those chapters are drafted.
- **Spaced forward:** verification of outputs → Ch. 8; standing instructions for voice and style → Ch. 10; which tools offer which features → Ch. 12; from chains to agents with approval gates → Ch. 14 (A11); what never to paste, memory and prompt injection → Ch. 15; domain workflow → Ch. 19 (A13); library as portfolio evidence → Ch. 20.

## 8. Alignment matrix

| Objective | Taught | Practiced | Figures | Assessed | Artifact |
|---|---|---|---|---|---|
| O1 | 6.1 | Layer-mapping sequence | F6.2 | Review A; B1 | Library entry field "context to attach" |
| O2 | 6.2, 6.3 | Selection and ordering sequences; Lab 6.2 | F6.3–F6.5 | Review A; B2 | Library entries |
| O3 | 6.4 | Examples sequence; Lab 6.2 step 4 | F6.6 | Review A; B3; Case Study Questions | One in-context example per entry |
| O4 | 6.5 | Persistent-features sequence; Lab 6.4 | F6.7 | Review A; C1 | "What never to attach" field |
| O5 | 6.6 | Template sequence; Lab 6.1 | F6.8–F6.10 | B4; Application Assignment | **Personal prompt library** |
| O6 | 6.7 | Chain sequence; Lab 6.3 | F6.11, F6.12 | Review A; B5; C2 | Workflow card in the library |

Counts follow the anatomy (A 10–15, B 3–5, C 2–3, Spaced 3–5, Discussion 4–6 with at least one ethics, one career, one interdisciplinary; Case Study Questions 4–6; optional Mini-Project). Every item carries O · LO · Bloom. Review A distractors come from M1–M6 without absolute giveaways. **The chapter is Deep, so none of it is examinable** (Decision 1); the review questions are exam-format practice, and the package says so in one line. Odd answers → handoff Appendix E block; even → private/ch06-answers-even.md.

**Key Terms (planned; definitions drafted in the handoff, glossary wording reused where it exists):** context engineering · context layer · system prompt (reuse Ch. 3 wording) · standing instructions · project space · memory (product feature) · in-context example · few-shot prompting · prompt template · placeholder · edge case · prompt library · prompt version · prompt chain · workflow (vs. agent). Terms not to reuse with a new meaning: *example* (glossary: one item in a dataset) → always "in-context example"; *test set* (glossary: held-out labeled examples) → "test inputs".

### Application Assignment (optional): Personal Prompt Library

*(O5, O6 · LO2, LO3 · Create)* Ungraded unless an instructor chooses to give feedback; about 60–90 minutes, can grow across the term. **What to build:** 3–5 entries for tasks you really repeat in study or work. Each entry: name and purpose; when to use it and when not to; the template with placeholders; the context to attach (and what never to attach, with a pointer to Ch. 15); one in-context example; a test record on three inputs (typical, different, edge case) with pass criteria and results; version number, date, and the tool and model it was tested on; what changed since the last version. Plus **one workflow card** (a two- or three-step chain with the check you perform between steps). Plus an **AI Use Declaration** (tools, purpose, what you accepted, rejected or revised, how you verified it, and where your judgment mattered) and two sentences on which entry you would *not* reuse without retesting, and why.

**Rubric (10 points; same four criteria and weights as the course artifact rubric)**

| Criterion (points) | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| **Task (3)** | 3: 3–5 entries for real recurring tasks, every field present, and a workflow card | 2: 3–5 entries with one or two fields missing, or no workflow card | 1: one or two entries, or several fields missing in most entries | 0: no usable entry |
| **Process evidence (3)** | 3: every entry tested on typical, different and edge inputs, and at least one revision with what changed and why | 2: most entries tested on three inputs; revisions noted but without reasons | 1: tests on one or two inputs only, or no revision | 0: no test record |
| **Verification (2)** | 2: every test judged against stated pass criteria or a named source; at least one failure recorded honestly | 1.5: checks present, criteria vague | 1: checks for some entries only | 0: no checks |
| **Declaration and judgment (2)** | 2: all five declaration elements and a specific reason for the entry you would not reuse | 1.5: all five elements; general reason | 1: two to four elements, or reason missing | 0: missing |

**Alternative assignment** (for students who prefer not to use AI tools or cannot access persistent features): repair the dated, constructed sample library on eLearning (four flawed entries: no placeholders, a whole document pasted, one-sided examples, a field that asks for personal data). Diagnose each flaw with the chapter's checklist, rewrite three entries, and write a test plan (three inputs and pass criteria) for each, without running a tool. Same rubric, read this way: Task = three repaired entries and a workflow card; Process = diagnoses and test plans; Verification = the criterion or source behind each repair; Declaration and judgment = as above.

**Mini-Project (optional):** a shared library for a club, team or job over three weeks, with versions and a change log; feeds A11 and A13.

## 9. Figures (titles state the finding; each serves an objective; ≤ 9 boxes)

| ID | Title | Type | Section | Objective |
|---|---|---|---|---|
| F6.1 | Chapter 6 at a glance (optional chapter; AI Work Loop, Prompt highlighted) | Chapter map (imports `work_loop` from ch01_figures) | Opening | all |
| F6.2 | The model receives far more than the message you typed | **Context layers**: seven stacked layers (system prompt dashed = not visible to you; standing instructions; project files and memory; conversation so far; documents and retrieved text; examples; your message), with "your message" drawn by importing Chapter 5's Signature 6 function with its context and examples parts highlighted. New reusable function `context_layers(highlight=...)` | 6.1 | O1 |
| F6.3 | Two labeled excerpts serve the task better than an 80-page manual | Concept diagram (whole document vs. selected excerpts with source labels) | 6.2 | O2 |
| F6.4 | One irrelevant sentence lowered a 2023 model's accuracy on math word problems | Data chart from published values (Shi et al., 2023; data/ch06_distraction.csv; model and year in the title) [VERIFY values] | 6.2 | O2 |
| F6.5 | Labels separate instructions from material, and the task sits where it is used most reliably | Annotated layout of a labeled context | 6.3 | O2 |
| F6.6 | One-sided examples pull the outputs toward one label | Illustrative schematic, labeled illustrative | 6.4 | O3 |
| F6.7 | Standing instructions, project files and memory fill layers automatically, so they need upkeep | F6.2 reused, layers 2–3 highlighted | 6.5 | O4 |
| F6.8 | A reusable prompt keeps fixed parts and leaves placeholders for what changes | Template anatomy (Signature 6 import, placeholders marked) | 6.6 | O5 |
| F6.9 | Test a template on a typical, a different and an edge input before you trust it | Test-record template (table-figure) | 6.6 | O5 |
| F6.10 | A library entry records when to use it, what it was tested on, and what changed | Library entry card (the artifact format) | 6.6 | O5 |
| F6.11 | A check between steps catches errors where they start | Sam's three-step chain (rectangle = step, hexagon = AI, rounded = Sam's check, diamond = pass/fix) | 6.7 | O6 |
| F6.12 | In a workflow you fix the steps; in an agent the model chooses them | Two-panel contrast; pointer to Ch. 14 (does not draw Signature 9) | 6.7 | O6 |
| F6.13 | Medprompt raised GPT-4's MedQA score from 81.4% to 90.2% without changing the model (2023) | Data chart from published values (Nori et al., 2023; data/ch06_medprompt.csv), with the ablation as a second panel | Case Study | O3, O5 |
| F6.14 | Chapter summary card | Summary card (complete Context Layers) | Summary | all |

14 figures. Short cases also appear on Signature 5 (imported from ch04_figures) if Chapter 4 exports it in time; otherwise the text names the branch. Interactive in Compass: a context-layer builder and a template tester. **Dependencies:** `ch05_figures.py` (Signature 6) and `ch04_figures.py` (Signature 5) do not exist yet; Chapter 6 imports, never redraws (Risk 1).

## 10. Labs (tool-neutral; current tool steps in Compass)

**Lab 6.1 Template Your Prompt** — Studio · 30 minutes · Thu Feb 4 extension (after the A3 sprint) or at home · individual.

| Minutes | Step |
|---|---|
| 0–5 | Take your best A3 prompt (or the provided one); mark what stays fixed and what changes each time |
| 5–12 | Rewrite it as a template with placeholders; add "when not to use" |
| 12–25 | Run it on three inputs: typical, different, edge case; record result against pass criteria |
| 25–30 | Fix one failure; save as v1.1 with a version note (first library entry) |

**Lab 6.2 Context A/B** — home · 25 minutes. One provided question with (a) no document, (b) the whole provided document with unrelated sections, (c) two labeled excerpts with the task last; compare against a provided answer key; step 4 adds two in-context examples to (c) and judges the change on three inputs.

**Lab 6.3 Two Steps or One?** — home · 25 minutes. Constructed meeting notes with planted errors (a wrong date, a misattributed task): one prompt vs. a two-step chain with your check in between; count the errors each catches.

**Lab 6.4 Audit Your Standing Context** — home · 15 minutes · optional. List what your tool's standing instructions, project files and memory contain (where to find them: Compass); fix or delete one stale or risky item. No-feature route: audit a provided sample memory list.

Accessibility and alternatives: dated sample outputs on eLearning for every lab (opt-out and no-device route: analyze the samples); every lab has a "paste it at the start of a new chat" fallback for free tiers without projects or memory; screen-reader-friendly test-record table; provided texts only; no personal or confidential data (course guidance D15; Ch. 15).

## 11. Risks and checks

1. **Chapter 5 dependency.** Signature 6 is drawn in Chapter 5. Chapter 6 imports its drawing function (name and `highlight` signature to be read from ch05_figures.py) and never redraws it; if the function is not ready at build-out, F6.2 and F6.8 wait and the handoff says so. Once the Chapter 5 blueprint exists, check the boundary on the "context" and "examples" parts (Ch. 5 names them in one prompt; Ch. 6 designs them), the A3 link in Lab 6.1, and the Spaced Review items.
2. **Chapter 3 and 4 dependencies.** Reuse Chapter 3's glossary wording for context window, system prompt, retrieval, inference; import Signature 5 from Chapter 4 if available.
3. **Later Core chapters must not depend on this optional chapter** (Decision 2): Ch. 12, 14, 15 and 19 may point here but define what they need themselves.
4. **Fast-aging product features.** No product names or numbers in running text; one dated "as of October 2026" box with at least two providers; click paths only in Compass; refresh-list rows in the handoff.
5. **Research on older models.** Example-order findings come from GPT-3-era models (2021–2022) and distraction from 2023 models; state model and year; present as patterns to test; Nori et al. (2024) shows a reversal for a newer model.
6. **Interested sources, labeled:** Medprompt (Microsoft authors, OpenAI model; the 2024 paper with OpenAI co-authors [VERIFY]); Chroma's context-rot report (a vendor of retrieval software; not peer reviewed); Anthropic posts (a model provider). Balance: peer-reviewed sources carry every general claim; the book already relies on Anthropic outputs (D12), so vendor posts are used only for definitions and dated practice.
7. **No anthropomorphic verbs.** "In-context learning" appears once as the research term, with the explanation that no settings change; never "the model learns from your examples", "remembers", "pays attention"; use "receives", "uses", "produces", "the product stores a note".
8. **Boundaries:** no tool comparisons (Ch. 12); no loops where the model chooses steps (Ch. 14); privacy, memory risk and prompt injection get one-sentence pointers to Ch. 15, not lessons.
9. **Medical content.** Medprompt is a benchmark result; the chapter says benchmark ≠ clinical practice and never suggests medical use; the nursing example uses a public leaflet, never patient data.
10. **Characters.** Sam only; new details to log (handoff): runs the robotics club's weekly meeting and writes the update email; a lab report with a units table; keeps his prompt library as a plain text file; a stale memory note from his co-op (the co-op is completed, consistent with characters.md). Classmates' names in his notes are replaced with roles before pasting.
11. **Equity of access.** Every lab works on a free tier with the paste-at-start fallback.

## Decisions taken under delegation (D19)

| # | Decision | Reason |
|---|---|---|
| 1 | **Tags in a Deep chapter:** 6.1–6.5 and 6.7 are tagged Deep; 6.6 (templates and the library) is tagged Studio because it is the Thu Feb 4 extension and builds the artifact. No Core subsections; numbering 6.1–6.7 (no "Deep 6.A" sections, since everything is already Deep). Nothing in the chapter is examinable (midterm included, although it covers "Ch. 1–10"); review questions are practice. Check Yourself items are answerable from each subsection's own text | Book map path D; anatomy defines Deep as optional, not examinable; CLAUDE.md requires a tag on every subsection |
| 2 | **Book-wide:** later Core chapters (12, 14, 15, 19) may point to Chapter 6 but must define any Chapter 6 term they need (e.g., prompt chain, standing instructions, memory) themselves | A Core chapter cannot rest on optional reading |
| 3 | Subsections ~900–1,400 words; fast route (~25 min) and full route (~70 min) stated in the Chapter Map | Optional chapter in Chapter 5's week; keeps ≥ 10,000 words |
| 4 | Work Loop highlight: Prompt (Verify second) | The chapter designs what the model receives and tests it before reuse |
| 5 | **Opening Case: Medprompt (Nori et al., 2023)**, returned to in the Case Study with the 2024 reversal; From the Field stays in part 11. Departure from the book map's "From the Field" case entry | The anatomy requires a real, cited event in the Opening Case; From the Field cannot be the opening because it is the author's own writing, not an event |
| 6 | **From the Field: Şeker (2018), CRISP-DM**, facts limited to the article; present-day connections marked. OptiCRM (2022) rejected: it describes the author's company's product (would need the D16 disclosure) and is about AI in business-process software rather than repeatable method | Best fit for "reusable process"; not commercial |
| 7 | Personal prompt library: optional and ungraded, with a 10-point rubric (course artifact criteria and weights) for self-check, an alternative assignment and a Mini-Project; suggested reuse in A11 and A13. No change to the live syllabus | Syllabus lists 13 graded artifacts; the library is not one of them |
| 8 | Lab 6.1 offered as the "D: Ch. 6" extension in the Thu Feb 4 lab or at home; Labs 6.2–6.4 at home | The lab belongs to Chapter 5's A3 sprint |
| 9 | **Terminology:** "in-context example" (never bare "example", which the glossary defines as a dataset item); "test inputs" (not "test set"); "standing instructions" as the tool-neutral name for custom/project instructions and instructions files; "system prompt" only for the provider's layer (Ch. 3 term); "memory" defined as a product feature that stores notes; "prompt chain" for a person-run multi-step workflow; "workflow vs. agent" per Anthropic (2024c) | Avoids clashes with Chapter 2's glossary and with Chapter 14 |
| 10 | **Context Layers** is a reusable secondary diagram (`context_layers(highlight=...)` in ch06_figures.py) built on Signature 6, available for reuse in Ch. 10, 14 and 15; it is not a thirteenth signature diagram | Book map names it as the chapter figure; reuse keeps one visual language |
| 11 | Featured character Sam only; other fields use unnamed one-off figures | Rotation table; avoids crowding |
| 12 | Case file id: **C16 (provisional; the editor assigns)**, cases/C16-medprompt.md | cases/index.csv has no Chapter 6 row; C01–C15 are taken |
| 13 | The term's 2025 origin (Lütke; Karpathy) appears as one dated sentence in 6.1, cited through the original posts and Willison (2025) | Students meet the term at work; dated so it can age |

## Open [VERIFY] items

1. Shi et al. (2023) table values for F6.4 (95.0 → 72.4; 77.8 with instruction; code-davinci-002; 100 base problems): read from ar5iv; confirm against the published PDF.
2. Nori et al. (2024): exact accuracies (o1-preview with and without few-shot; GPT-4 with Medprompt) and whether OpenAI authors are listed.
3. Yoo et al. (2022), "Ground-truth labels matter" (EMNLP 2022): authors and pages, as the counter-finding to Min et al. (2022).
4. Lütke and Karpathy posts: exact dates (status IDs from Willison, 2025; around June 19 and June 25, 2025).
5. Anthropic Projects launch date (June 25, 2024, secondary sources) and Google Gems rollout (August 28, 2024, Google Workspace Updates blog); OpenAI memory (February 13, 2024; expanded April 10, 2025). Re-check all three, and current status, for the "as of October 2026" box.
6. Anthropic system-prompt publication: release-notes page date (coverage August 26, 2024).
7. Şeker (2018) CRISP-DM: page range in YBS Ansiklopedi 5(2) (not printed in the Drive copy).
8. Brown et al. (2020) page range (1877–1901) in NeurIPS 33.
9. Hong et al. (2025): confirm the model list and that the report supports only the general claim used (performance becomes less reliable as input grows); no secondary-blog numbers.

## Author-only items

1. CRISP-DM article affiliation reads "Bilkav Eğitim Danışmanlık". If that is the author's own company, confirm that no disclosure is needed (the article promotes no product; the plan treats it as non-commercial).
2. Nothing else needs the author at the blueprint stage: no anecdote is used, no live-syllabus change is proposed, no commercial disclosure is planned.

## Planned sources and verification status (checked online 2026-10-18)

| Source | Use | Status |
|---|---|---|
| Nori, H., Lee, Y. T., Zhang, S., … Horvitz, E. (2023). *Can generalist foundation models outcompete special-purpose tuning? Case study in medicine* (arXiv:2311.16452) | Opening Case, Case Study, F6.13 | Verified: 81.4% (5-shot simple prompt) → 90.2% (Medprompt, 5 examples, 5-run ensemble); ablation +3.4 / +2.2 / +2.2; no fine-tuning; limits stated |
| Nori, H., et al. (2024). *From Medprompt to o1* (arXiv:2411.03590) | Case Study twist | Verified (abstract): few-shot hinders o1; o1-preview without techniques beats GPT-4 with Medprompt; numbers [VERIFY] |
| Shi, F., Chen, X., Misra, K., Scales, N., Dohan, D., Chi, E., Schärli, N., & Zhou, D. (2023). Large language models can be easily distracted by irrelevant context. *ICML*, PMLR 202, 31210–31227 | 6.2 prediction, F6.4 | Verified; table values [VERIFY] |
| Liu, N. F., et al. (2024). Lost in the middle. *TACL*, 12, 157–173. doi:10.1162/tacl_a_00638 | 6.2, 6.3 | Verified |
| Hong, K., Troynikov, A., & Huber, J. (2025, July 14). *Context rot* (Chroma technical report) | 6.2, Short 2 | Verified (18 models; general finding only) |
| Sclar, M., Choi, Y., Tsvetkov, Y., & Suhr, A. (2024). Quantifying language models' sensitivity to spurious features in prompt design. *ICLR* | 6.3 | Verified (up to 76 accuracy points, LLaMA-2-13B; a maximum, stated as such) |
| Brown, T. B., et al. (2020). Language models are few-shot learners. *NeurIPS 33* | 6.4 | Verified; pages [VERIFY] |
| Lu, Y., Bartolo, M., Moore, A., Riedel, S., & Stenetorp, P. (2022). Fantastically ordered prompts…. *ACL*, 8086–8098. doi:10.18653/v1/2022.acl-long.556 | 6.4, Short 1 | Verified |
| Zhao, Z., Wallace, E., Feng, S., Klein, D., & Singh, S. (2021). Calibrate before use. *ICML*, PMLR 139 | 6.4, Short 1 | Verified (format, examples and order move GPT-3 from near chance to near state of the art) |
| Min, S., et al. (2022). Rethinking the role of demonstrations. *EMNLP*, 11048–11064 | 6.4 | Verified (12 models; labels matter less than format and distribution) |
| Yoo, K. M., et al. (2022). Ground-truth labels matter. *EMNLP* | 6.4 counterpoint | [VERIFY] details |
| Wu, T., Terry, M., & Cai, C. J. (2022). AI chains. *CHI '22*. doi:10.1145/3491102.3517582 | 6.7 | Verified (20-person study; quality, transparency, control) |
| Anthropic (2024c, December 19). *Building effective agents* (R11) | 6.7, F6.12 | Verified (workflows = predefined code paths; agents direct their own steps; prompt chaining with gates) |
| Anthropic (2025, September 29). *Effective context engineering for AI agents* | 6.1 (dated definition), Further Reading | Verified |
| Anthropic (2024a). System prompts, release notes | 6.1, Ethics Lens | Verified via coverage (Willison, 2024-08-26); primary page date [VERIFY] |
| OpenAI (2024, February 13). *Memory and new controls for ChatGPT* | 6.5 dated box | Verified (with 2025 updates on the same page) |
| Anthropic (2024b). *Projects* announcement; Google (2024, August 28). *Customize Gemini with Gems* | 6.5 dated box | Verified via secondary/blog; dates [VERIFY] |
| Willison, S. (2025, June 27). *Context engineering* (links Lütke's and Karpathy's posts) | 6.1 | Verified |
| Schulhoff, S., et al. (2024). *The Prompt Report* (arXiv:2406.06608) | Further Reading (taxonomy; 58 techniques) | Verified |
| Şeker, Ş. E. (2018). CRISP-DM: Endüstriler arası standart işleme – veri madenciliği için. *YBS Ansiklopedi*, 5(2) | From the Field | Read in full (Drive); pages [VERIFY] |
| Chapman, P., Clinton, J., Kerber, R., Khabaza, T., Reinartz, T., Shearer, C., & Wirth, R. (2000). *CRISP-DM 1.0: Step-by-step data mining guide*. SPSS | From the Field (six phases) | Verified (author list, six phases) |
