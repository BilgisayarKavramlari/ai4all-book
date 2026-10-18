# Chapter 6 blueprint — Context Engineering and Reusable Workflows

Status: v0.2 (2026-10-18), APPROVED under delegation (D19). v0.2 applies the editor's independent review (5 must-fix, 11 should-fix, 5 consider; see "Review changes" at the end). Drafted 2026-10-18 (chapter v1); drafting-stage changes ("system prompt" kept as Ch. 3's layer name; Medprompt numbers from Figure 4; context loss = Ch. 4 §4.4; full route ~60 min) are listed in docs/production/handoff/ch06.md, Notes for the editor.
Part II — Working with AI · Syllabus week 3 (read alongside Chapter 5) · Path: **Deep** (optional extension; the syllabus lists "D: Ch. 6" for the Thu Feb 4 lab) · Featured student: **Sam** (per the rotation in docs/characters.md; no other recurring character) · Work Loop step highlighted in the Chapter Map: **Prompt** (design what the model receives), with Verify second (test before you reuse).

**Source material.** No Haliç lecture covers this chapter; it is built from the cited research and documentation below. The week-3 concept session (framing a task; vague vs. framed prompt) and Thursday's prompt-iteration sprint belong to Chapter 5; Chapter 6 extends them for students who want more. From the Field: the author's 2018 article on CRISP-DM (YBS Ansiklopedi, in Turkish; Drive 1eES0f0OQwHiRuvUB8LVTkhMGi1SddAxY), read in full for this blueprint (see §5 and Decision 6).

**Boundaries with other chapters.**

| Chapter | Owns | Chapter 6's relation |
|---|---|---|
| 3 (week 2) | The context window mechanically (system instructions, conversation so far, pasted or retrieved text, your prompt must fit); "lost in the middle" as a diagnostic; Signature 4 | Recalled in one paragraph; Context Layers extends Signature 4's context stage |
| 5 (week 3, Core) | Framing and iterating a **single prompt**; Signature 6 (role, task, context, constraints, in-context examples, output format); defines "in-context example" in its Core text with one illustration (Chapter 6 reuses the definition word for word); owns Sclar et al. (2024) on prompt-format sensitivity; owns the "agency ≠ agent" box; "test inputs" (typical, different, edge); repeated runs; peer swap test; A3 | Chapter 5 ends at single-prompt iteration; **Chapter 6 starts at reuse across inputs.** Chapter 6 owns choosing, balancing, ordering and testing in-context examples with and without; it uses Chapter 5's "test inputs" and its three input types word for word (editor decision, review item 11) |
| 4 (week 5) | Failure Taxonomy Tree; context loss (§4.3); prompt injection mechanism (§4.6) | Read **after** Chapter 6: forward pointers only, no dependencies. "Context loss" is defined in one sentence where used |
| 12 | Tool choice (which tool offers which feature) | No tool comparisons |
| 14 | Agents (the model chooses its next steps), software workflows, approval gates | 6.7 stops at person-run chains |
| 15 | Privacy, security, prompt-injection defenses, what never to paste | One-sentence pointers: injection → "Ch. 4 §4.6 (mechanism); Ch. 15 (defenses)" |

## 1. Outcome link and week 3

| Item | Value |
|---|---|
| Syllabus outcomes | **LO2** (frame a task and improve results through deliberate, documented iteration); secondary **LO3** (verify outputs: testing a template is verification) |
| Artifact | **Personal prompt library — optional, ungraded.** It is not one of the 13 graded weekly artifacts (A1–A7, A9–A14; docs/syllabus.md). The book offers a 10-point rubric for self-check and instructor feedback, an alternative assignment, and suggests reusing the library in A11 (workflow blueprint, Ch. 14) and A13 (domain workflow prototype, Ch. 19). No syllabus change |
| In-class time | None required. Thu Feb 4 is filled by Chapter 5's A3 sprint; **Lab 6.1 is a home lab first**, done in class only by a team that finishes the sprint early |
| Readings | None beyond the chapter. Further Reading points ahead to R11 (Anthropic, 2024c, assigned in week 11) |
| Examinable? | **No** (D20: the midterm covers the Core sections of Chapters 1–10; Deep chapters and Deep sections are not examinable) |

### Week 3 workload (out of class)

| Item | Time |
|---|---|
| Chapter 5 Core reading, R2 module 2, A3 | set by the Chapter 5 blueprint (required) |
| **Chapter 6, fast route** (Chapter Map, 6.1, 6.6 with its recap box, Summary) | ~20 min at 150 words per minute, optional (longer if English is not your first language) |
| Chapter 6, full route (6.1–6.7, Case Study) | ~65 min at 150 words per minute, optional (longer if English is not your first language) |
| Lab 6.1 at home | 30 min, optional |
| Personal prompt library (at least 3 entries) | **2–3 h across weeks 3–11**, optional |

Because the chapter is optional, it adds nothing to the required 1–2 hours. The Chapter Map says so in its first line.

**Word budget.** No Core subsections, so no Core cap. Subsections run ~900–1,400 words (below the anatomy's 1,500–2,500, as in Chapters 2–3) so the full route stays near 65 minutes at the book-wide rate of 150 words per minute (fast route ≈ 3,100 words ≈ 20 min; full route ≈ 9,800 words including the Opening and Case Study ≈ 65 min). Planned: Opening 500 · Objectives and Warm-up 300 · 6.1–6.7 ≈ 8,100 (including the 150-word recap box in 6.6) · Labs 800 · Case Study 1,000 · Ethics 450 · Career 400 · From the Field 450 · Summary 450 · End-of-Chapter Package 2,200 · Further Reading 250 → ~14,900 words including tables and boxes (≥ 10,000 of running prose).

## 2. Chapter objectives (6; one Bloom verb each)

| # | Objective — after this chapter you will be able to… | Bloom | LO | Framework tags |
|---|---|---|---|---|
| O1 | **Explain** the layers of context a model receives in a chat tool and which of them you control | Understand | LO2 | UNESCO:TECH-U · 4D:DESC |
| O2 | **Construct** the context for a task from selected, labeled and ordered material | Apply | LO2 | 4D:DESC · UNESCO:TECH-A |
| O3 | **Judge**, from a with-and-without test on several test inputs, whether in-context examples improve an output | Evaluate | LO2, LO3 | 4D:DISC · 4D:DESC |
| O4 | **Evaluate** which information belongs in standing instructions, a project space, memory, or only the current chat | Evaluate | LO2 | 4D:DIL · 4D:DESC |
| O5 | **Create** a reusable prompt template with placeholders for a task you repeat | Create | LO2 | 4D:DESC · UNESCO:TECH-C |
| O6 | **Design** a two- or three-step prompt chain with a human check between steps | Create | LO2 | 4D:DEL · UNESCO:DES-A |

Testing on test inputs, versioning and the library record are assessed through the rubric (§8), not stated as extra verbs. UNESCO level codes follow the ai4all-frameworks skill; no sub-competency numbers are used.

## 3. Prerequisites and promises kept

From Chapter 1: AI Work Loop; same prompt → different answers. From Chapter 2: label, class imbalance, test set (contrasted with "test inputs"). From Chapter 3: token, context window, system instructions/system prompt, retrieval, training vs. inference (settings fixed at inference; no learning from your chat), "lost in the middle" (Liu et al., 2024). From Chapter 5 (same week): Signature 6, in-context examples (defined there), test inputs (typical, different, edge), repeated runs, the iteration log (A3). **Promises kept:** Chapter 3 §3.4 says "designing context is Chapter 6"; Chapter 5 §5.3 says the same. Because the chapter is optional, it re-explains in one or two sentences every earlier term it relies on. Nothing from Chapter 4 is assumed.

### Naming table (in 6.1 and 6.5)

| What products call it (examples, as of October 2026) | This book's term |
|---|---|
| System prompt, system message, developer instructions | **system instructions** (Ch. 3 wording; Key Term "system prompt" reused from Ch. 3's glossary entry) |
| Custom instructions, personalization, project instructions, saved info, instructions files (for example AGENTS.md-style files) | **standing instructions** |
| Projects, notebooks, workspaces, custom assistants with uploaded files | **project space** |
| Memory, saved memories, chat history reference | **memory** (a product feature that stores notes and adds them to later contexts) |
| Few-shot examples, demonstrations, exemplars | **in-context examples** (Ch. 5 term) |
| Prompt chaining, multi-step prompting | **prompt chain** |

Product names in the left column appear only in this table and in the dated box; the running text uses the right column.

## 4. Misconceptions (refutation pattern; six)

| # | Misconception | Where |
|---|---|---|
| M1 | "The model receives only the message I just typed" | Opening Case, 6.1 |
| M2 | "More context is always better: paste the whole document" | 6.2 |
| M3 | "In-context examples teach the model, so more examples always help" (refuted: settings do not change at inference, Ch. 3; examples steer format and pattern within that context only; balance and order matter; for some newer models examples lowered scores) | 6.4, Case Study |
| M4 | "Memory means the model has learned about me, and what it stored is complete and correct" (hedged: memory is a product feature that stores notes and adds them to later contexts; notes can be wrong, stale or missing) | 6.5 |
| M5 | "A prompt that worked once will work every time, on every input and every model" | 6.6, Case Study |
| M6 | "Once a task is split into steps, it runs itself: a chain needs no checks" | 6.7 |

Refutation text states the correct idea first and restates the misconception only once, so it does not create a new one (Chapter 2 lesson).

## 5. Concept sequence

**Session question, answered in the Summary:** *If the model is the same, why do two people get such different results from it?* Answer: much of the difference lies in what the model receives (the context someone builds, the examples they choose) and in how the task is run (the steps, the repeats, the checks), rather than in the model; and whether a design helps must be tested, because the same design can stop working when the input or the model changes.

**Opening Case (450–550 words): Medprompt — same model, different context and steps.** A research finding, stated as such, with model name and date in the first paragraph. In November 2023, Microsoft researchers reported that GPT-4, **without any change to its settings** (no fine-tuning), scored 90.2% on MedQA, a multiple-choice benchmark of U.S. medical-licensing-style questions (Nori et al., 2023). The starting point was GPT-4 with five fixed examples, as reported in earlier work: 81.4% (Nori et al., 2023, Table 1). They changed two kinds of thing. **What the model received:** for each question, five similar solved questions chosen automatically as in-context examples, each with step-by-step reasoning that **GPT-4 had written itself** (kept only where its answer matched the correct one). **How the task was run:** five runs with the answer options shuffled each time, combined by majority vote, a simple workflow. Chapter question: *what changed, if not the model?* Limits stated in the case: a multiple-choice benchmark is not clinical practice, and the authors could not rule out that test questions appeared in the training data (Nori et al., 2023). The twist (a year later, the same team found that examples lowered the scores of a newer reasoning model; Nori et al., 2024) is held for the Case Study. The Chapter Map links the case to 6.4 (examples) and 6.7 (workflows). *Departure from the book map (which lists "From the Field" as the case): the Opening Case slot needs a real, cited event (anatomy part 2), so From the Field moves to its own part 11 (Decision 5).*

**Medprompt component numbers [VERIFY before drafting].** The paper's text gives three increments from its ablation (Figure 6): step-by-step reasoning +3.4, examples +2.2, shuffle-and-vote +2.2 points. These sum to 89.2%, not 90.2%, so the figure contains a step or a baseline the text does not state, and the authors call the order of the ablation subjective. Before drafting, read Figure 6 in the PDF and record in data/ch06_medprompt.csv: the starting point (zero-shot or five-shot), every step in order, and the accuracy after each. The Case Study prediction and its answer key are written only from that table. If Figure 6 cannot be read exactly, the prediction is reworded to "which kind of change (what the model received, or how the task was run) do you predict mattered more?" and answered qualitatively.

**Prediction before the evidence (6.2):** "You add one irrelevant sentence to a school math word problem. Does the model's accuracy go up, stay the same, or go down?" Answered with Shi et al. (2023): for code-davinci-002 (released 2022, tested in 2023) with step-by-step prompting, accuracy was 95.0% on 100 original problems and 72.4% on versions with one irrelevant sentence added; an instruction to ignore irrelevant information recovered part of the drop (77.8%) [VERIFY table values against the PDF]. Chapter 5 §5.3 mentions this study in one clause; Chapter 6 gives the numbers.

| # | Subsection | Tag | One new core idea | Examples | Figures |
|---|---|---|---|---|---|
| 6.1 | What the model actually receives | Deep | Recall (one paragraph): Chapter 3's context window holds system instructions, the conversation so far, pasted or retrieved text and your prompt. New: two more layers can be filled **before you type**: your **standing instructions** and your **project files and memory notes**. *Context engineering* = deciding what goes into all of these (term popularized in June 2025: Lütke; Karpathy; via Willison, 2025). **How the layers relate to the prompt anatomy:** Signature 6 describes one layer, your message; its "context" part is the material you choose to add (it may travel in your message, a project file or a document layer), and its "in-context examples" part lives in your message or in a template; the other layers are added by the tool or by persistent features. The system-instructions layer is real and usually hidden: one provider began publishing its consumer system prompts in 2024 (Anthropic, 2024a). Naming table (§3) | **Sam** asks for this week's robotics-club update; the chapter lists every layer the model received, who set it, whether Sam could see it (worked); a design student's chat in a project with a brand-style file (faded) | F6.2 Signature 4 context stage (reuse); F6.3 Context Layers |
| 6.2 | Choosing what to include | Deep | Relevant, bounded context beats volume: irrelevant material distracts (Shi et al., 2023); long inputs are used unevenly (Liu et al., 2024; Hong et al., 2025, labeled as an industry report); select excerpts, name each one's source and date, and say what to do when the material lacks the answer. One-sentence pointer: what never to paste → Ch. 15 | **Sam** drafts a parts-order request for the robotics club: from a 120-page supplier catalog and the club's budget rules, he selects two catalog pages and the one budget rule that applies (worked; constructed documents); a history student picks which of five primary-source passages to include (faded); a customer question with a provided policy document (Your Turn, business) | F6.4 published values (Shi et al., 2023); F6.5 Context Layers, documents layer highlighted |
| 6.3 | Labels and order | Deep | Structure changes use: label each part (instructions, material, in-context examples, question) with headings or delimiters; keep instructions separate from material; put the task and key instructions where they are used most reliably (start or end, per Liu et al., 2024, stated as a pattern to test). Small format changes can swing results: one sentence pointing back to Chapter 5's discussion of Sclar et al. (2024), not retaught. Pointer: text inside a document can act as an instruction → "Ch. 4 §4.6 (mechanism); Ch. 15 (defenses)" | **Sam**'s parts-order context rebuilt with labels and the task last (worked); reader orders a provided jumbled context (faded) | F6.6 before/after: whole catalog vs. two labeled excerpts with the task last (merges v0.1 F6.3 and F6.5) |
| 6.4 | Choosing and testing in-context examples | Deep | Three claims only: (1) in-context examples steer the format and pattern of the output, within that context and without changing the model's settings (Brown et al., 2020; Ch. 3); (2) their balance and order matter (Lu et al., 2022; Zhao et al., 2021; GPT-3-era models, stated); (3) so test with and without examples on the same test inputs, because for some newer models examples lowered scores (Nori et al., 2024). Link to Ch. 2: one-sided examples act like class imbalance in miniature | Coding open-ended survey answers with three balanced vs. three one-sided examples (social science; constructed outputs, labeled); a teaching assistant chooses three of six candidate feedback examples (education, faded) | F6.7 balanced vs. one-sided examples (illustrative, labeled) |
| 6.5 | Standing instructions, projects and memory | Deep | Three persistent features fill context layers automatically: standing instructions, project spaces, memory. They give consistency but are invisible, can go stale, and carry privacy risk (Ch. 15); memory is not training (Ch. 3). Dated box "as of October 2026": at least two providers (OpenAI, 2024; Anthropic, 2024b; Google, 2024) **and the university-provided tools named in the syllabus (Microsoft Copilot, CometAI)** [VERIFY which of these features the UTD license offers]; no click paths; current steps in Compass. Routine: review and prune | **Sam**'s standing instruction ("Write for first-year club members: plain words; every task gets an owner and a due date") and a stale memory note ("Sam is on co-op", true only last year) (worked); reader sorts eight items into standing instructions / project file / this chat only / never store (faded); Lab 6.4 (Your Turn) | F6.8 Context Layers, standing-instructions and project/memory layers highlighted |
| 6.6 | Reusable prompts: templates and your library | **Studio** | **Recap box (~150 words) for fast-route readers:** one line each from 6.2–6.5 (select, label and order, examples tested with and without, what belongs in persistent features). New idea: a prompt becomes reusable when it is *parameterized* (fixed parts + placeholders), *re-tested across inputs* (Chapter 5's typical, different and edge test inputs, now for a template that will meet inputs you have not seen) and *versioned* (number, date, tool and model tested on, what changed); a library entry also says when not to use it. Re-test when the model changes (Case Study). Builds the optional artifact | **Sam** turns his club-update prompt into template v1.0; it fails on the edge case (a meeting with no decisions); v1.1 adds "if no decisions were made, say so" (worked); a nursing student's template for summarizing a *public* drug leaflet, test record with the typical input done and the different and edge inputs left to the reader (health, faded, no patient data); Lab 6.1 and the library (Your Turn) | F6.9 template anatomy (Signature 6 import, placeholders marked, callout mapping its context and in-context-examples parts to layers); F6.10 library entry card with its test record |
| 6.7 | Simple multi-step workflows | Deep | A *prompt chain* splits a task into fixed steps; each step's output becomes the next step's input; a person checks between steps, so errors surface where they start (Wu et al., 2022: 20-participant study). When one prompt is enough. One sentence: a workflow can also repeat one step and compare the results (Medprompt's shuffle-and-vote). Workflow vs. agent, **adapted from Anthropic (2024c)**, which defines workflows as predefined code paths: in this book's person-run chains the steps are fixed in advance and you run them; in an agent the model chooses its next steps. **Reuses Chapter 5's "agency ≠ agent" box** (AI Fluency's agency mode, Dakan & Feller, is not the same as an agent) in one recalled sentence, not a new box. Software workflows, agents and approval gates → Ch. 14 | **Sam**'s three-step chain: extract decisions and action items → Sam checks names and dates against his notes → draft the email (worked); a business report-summary chain with the check step missing: reader adds it and its pass criteria (faded); Lab 6.3 (Your Turn) | F6.11 chain with a check (no workflow-vs-agent figure; the contrast is a two-row text table) |

Other anatomy parts:

| Part | Plan |
|---|---|
| Case Study (1 main + 2 short) | **Main: Medprompt, revisited** (cases/C17-medprompt.md) — traced on Context Layers: the examples layer (similar solved questions chosen per question, with reasoning GPT-4 wrote itself) and, separately, the workflow (five shuffled runs and a vote). The component prediction is answered only from the verified Figure 6 table (see above). The twist: with a newer reasoning model (o1-preview), examples lowered performance, and that model without these techniques scored higher than GPT-4 with Medprompt (Nori et al., 2024) [VERIFY numbers]. Lesson: a context design belongs to a model and a date; re-test when either changes. Disclose: authors are Microsoft researchers (the 2024 paper's author list to be checked for OpenAI co-authors [VERIFY]); benchmark ≠ clinical use. **Short 1:** example balance and order (Lu et al., 2022; Zhao et al., 2021). **Short 2:** irrelevant and long context (Shi et al., 2023; Hong et al., 2025, an industry technical report from a company that sells retrieval software, labeled as such). Short cases name their failure in plain words: *context loss*, defined in one sentence ("information the model received is not used, or is used wrongly, in the output"), with a forward pointer to Ch. 4 §4.3. **Failure label line in C17 (Ch. 4 convention):** 2023 result: "none on the tree" (a positive result); 2024 reversal: "other" leaf, dashed (inferred): a context design that lowered accuracy on a newer model |
| Ethics Lens | **Invisible instructions** (supports O4). Standing instructions, memory and system instructions shape outputs that readers of your work never see. Transparency (publishing system prompts as one provider's practice since 2024), accountability for shared templates at work (who answers for a template's wrong reply), and templates that encode a bias (a screening template that repeats Chapter 2's recruiting-tool pattern; pointer to Ch. 16). A discussion question asks which of your standing instructions you would disclose in an AI Use Declaration. One line on others' data in context → Ch. 15 |
| Career Connection | Support knowledge-base or operations specialist (reply templates tied to a policy document); paralegal or legal-operations specialist (clause and checklist libraries); marketing content specialist (brand-style standing instructions); quality or manufacturing engineer (standard work instructions become templates; Sam's co-op field); instructional designer or teaching assistant (rubric-based feedback templates). Descriptive only; no salary or demand numbers unless cited |
| From the Field | **The author's CRISP-DM article (Şeker, 2018).** Facts limited to the article: CRISP-DM is a six-step process (business understanding, data understanding, data preparation, modeling, evaluation, deployment) with loops, the most important one returning from evaluation to the start; the article reports that practitioners who use it for long adopt its rule of starting from the business problem, not from "what project can I make from this data?"; it lists roles per step and notes that tools such as SPSS Modeler build the steps in. **Present-day connection, marked as the book's:** a prompt-library entry is a small process standard; its test step plays the role of CRISP-DM's evaluation loop; "start from the task, not the tool". Turkish source, paraphrased, cited with year; original guide cited for the six phases (Chapman et al., 2000). Not commercial: no D16 disclosure planned (see Author-only items). An optional author anecdote from a CRISP-DM project would strengthen it; never invented |
| Summary + Key Terms | Answers the session question; the complete Context Layers diagram on the summary card (F6.14); Key Terms (§8) |

## 6. Example plan (worked → faded → your turn)

| Skill | Worked | Faded (genuinely partly filled) | Your Turn |
|---|---|---|---|
| Mapping context layers (O1) | Sam's club-update chat: a table of every layer the model received, who set it, whether Sam could see it | A design student's chat inside a project with a brand-style file: three of six layers filled | Map the layers of your own last AI conversation (layer types only, no content) |
| Selecting and ordering context (O2) | Sam's parts-order request: which two catalog pages and which budget rule, and why; labels; task placed last | History: five primary-source passages, two already marked include/exclude with reasons; reader decides the other three and the order | Business: a provided policy document and a customer question; build the context (Lab 6.2 extends it) |
| Choosing and testing examples (O3) | Survey coding: three balanced vs. three one-sided examples; constructed outputs labeled as such; what changed | Education: six candidate feedback examples, two chosen with reasons; reader picks the third and predicts its effect | Lab 6.2 step 4: one task with and without examples on three test inputs; judge |
| Persistent features (O4) | Sam's standing instruction and stale memory note; what he keeps, edits, deletes | Eight items, three already sorted into standing instructions / project file / this chat only / never store | Lab 6.4: audit your own standing context (or a provided sample) |
| Template (O5) | Sam's template v1.0 → edge-case failure → v1.1 with a version note | Nursing student's leaflet-summary template: typical input tested, different and edge inputs left to the reader | Lab 6.1; the personal prompt library |
| Chain with a check (O6) | Sam's three-step chain with his check between steps 1 and 3 | Business report summary: a two-step chain with no check; reader inserts the check and its pass criteria | Lab 6.3 |

Fields: engineering (Sam), arts and design, history, business, social science, education, health (public leaflet; Medprompt). Sam is the only recurring character; others are unnamed one-off figures. Every AI output is labeled "constructed example" or carries model name and date. Sam's examples avoid the units theme already used in Chapters 1 and 4.

## 7. Retrieval and spacing

- **Warm-up (3):** When you type a message in a chat tool, what else might the model receive? If you paste a 50-page document, are all pages used equally well? If examples in your prompt improve today's answer, has the model learned from them?
- **Check Yourself** after 6.1–6.7, 2–3 items each, at least one "why", all answerable from that subsection's own text (there is no Core to fall back on).
- **Spaced Review (Chapters 3 and 2, the two chapters read before; 4 items):** Ch. 3: what must fit in the context window, and what "lost in the middle" predicts about a long pasted document; Ch. 3: why an example in today's prompt does not change tomorrow's answers (inference does not change settings); Ch. 2: how one-sided in-context examples resemble class imbalance; Ch. 2: why "test inputs" are not a "test set".
- **Interleaving with Chapter 5 (same week; 1–2 items, labeled "Chapter 5 this week"):** which Signature 6 part each context layer feeds; what a template adds to a prompt that already passed Chapter 5's test inputs. Finalized after Chapter 5 is drafted.
- **Spaced forward:** context loss over many turns → Ch. 4 §4.3; prompt injection → Ch. 4 §4.6 and Ch. 15; verification of outputs → Ch. 8; standing instructions for voice and style → Ch. 10; which tools offer which features → Ch. 12; from chains to agents with approval gates → Ch. 14 (A11); what never to paste and memory risk → Ch. 15; domain workflow → Ch. 19 (A13); library as portfolio evidence → Ch. 20.

## 8. Alignment matrix

| Objective | Taught | Practiced | Figures | Assessed | Artifact |
|---|---|---|---|---|---|
| O1 | 6.1 | Layer-mapping sequence | F6.2, F6.3 | Review A; B1 | Entry field "context to attach" |
| O2 | 6.2, 6.3 | Selection and ordering sequences; Lab 6.2 | F6.4–F6.6 | Review A; B2 | Library entries |
| O3 | 6.4, Case Study | Examples sequence; Lab 6.2 step 4 | F6.7, F6.12, F6.13 | Review A; B3; Case Study Questions | Entry field "in-context examples: used / not used, and the test that decided" |
| O4 | 6.5, Ethics Lens | Persistent-features sequence; Lab 6.4 | F6.8 | Review A; C1; Discussion (ethics) | Entry field "what never to attach" |
| O5 | 6.6 | Template sequence; Lab 6.1 | F6.9, F6.10 | B4; Application Assignment | **Personal prompt library** |
| O6 | 6.7 | Chain sequence; Lab 6.3 | F6.11 | Review A; B5; C2 | Workflow card in the library |

Counts follow the anatomy (A 10–15, B 3–5, C 2–3, Spaced 4 + 1–2 interleaving, Discussion 4–6 with at least one ethics, one career, one interdisciplinary; Case Study Questions 4–6; optional Mini-Project). Every item carries O · LO · Bloom. Review A distractors come from M1–M6 without absolute giveaways. **Nothing in this chapter is examinable (D20)**; the review questions are exam-format practice, and the package says so in one line. Odd answers → handoff Appendix E block; even → private/ch06-answers-even.md.

**Key Terms (planned; definitions drafted in the handoff, glossary wording reused where it exists):** context engineering · context layer · system prompt (Ch. 3 entry, reused) · standing instructions · project space · memory (product feature) · in-context example (Ch. 5 definition, reused word for word) · prompt template · placeholder · edge case (reuse Ch. 5 wording if it defines one) · prompt library · prompt version · prompt chain · workflow (vs. agent; adapted from Anthropic, 2024c). Never reused with a new meaning: *example* (Ch. 2: one item in a dataset); *test set* (Ch. 2) → "test inputs" (Ch. 5).

### Application Assignment (optional): Personal Prompt Library

*(O5, O6 · LO2, LO3 · Create)* Ungraded unless an instructor chooses to give feedback; **about 2–3 hours across weeks 3–11**. **What to build:** at least **3 entries** for tasks you really repeat in study or work. Each entry: name and purpose; when to use it and when not to; the template with placeholders; the context to attach (and what never to attach, with a pointer to Ch. 15); **in-context examples: used / not used, and the test that decided**; a test record on three test inputs (typical, different, edge) with pass criteria and results; version number, date, and the tool and model it was tested on; what changed since the last version. Plus **one workflow card** (a two- or three-step chain with the check you perform between steps). Plus an **AI Use Declaration** (tools, purpose, what you accepted, rejected or revised, how you verified it, and where your judgment mattered) and two sentences on which entry you would *not* reuse without retesting, and why.

**Rubric (10 points; the course artifact rubric's four criteria and weights, with process evidence split into tests and revision; each level differs from the one above on one dimension)**

| Criterion (points) | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| **Task (3)** | 3: at least 3 entries for real recurring tasks, every field complete, and a workflow card | 2: at least 3 entries, every field complete; workflow card missing or incomplete | 1: at least 3 entries, but some fields missing | 0: fewer than 3 entries |
| **Process: tests (1.5)** | 1.5: every entry tested on a typical, a different and an edge input | 1: every entry tested on three inputs, but one entry lacks an edge input | 0.5: some entries tested on fewer than three inputs | 0: no test record |
| **Process: revision (1.5)** | 1.5: at least one entry revised after a failed test, with what changed and why, and the earlier test inputs re-run | 1: a revision with what changed and why; earlier inputs not re-run | 0.5: a revision noted without a reason | 0: no revision |
| **Verification (2)** | 2: every test judged against stated pass criteria or a named source, and at least one failure recorded | 1.5: every test judged; criteria vague in some | 1: only some tests judged | 0: no judgments |
| **Declaration and judgment (2)** | 2: all five declaration elements and a specific reason for the entry you would not reuse | 1.5: all five elements; general reason | 1: two to four elements | 0: missing |

**Alternative assignment** (for students who prefer not to use AI tools or cannot access persistent features): repair the dated, constructed sample library on eLearning (four flawed entries: no placeholders, a whole document pasted, one-sided examples, a field that asks for personal data). Diagnose each flaw with the chapter's checklist, rewrite three entries, and write a test plan (three test inputs and pass criteria) for each, without running a tool. Same rubric, read this way: Task = three repaired entries and a workflow card; Process: tests = the test plans; Process: revision = the diagnoses and what each rewrite changes; Verification = the criterion or source behind each repair; Declaration and judgment = as above.

**Mini-Project (optional):** a shared library for a club, team or job over three weeks, with versions and a change log; feeds A11 and A13.

## 9. Figures (titles state the finding; each serves an objective; ≤ 9 boxes)

**Context Layers (new reusable diagram).** `context_layers(highlight=None, note=None)` in figures/scripts/ch06_figures.py **extends Signature 4's context stage**: it imports `llm_anatomy` and the context-window conventions from ch03_figures.py (same frame, same box style, Chapter 3's labels and subtitles for its four layers) and adds two layers, standing instructions and project files and memory notes. **7 boxes:** the context-window frame + system instructions (dashed: usually not visible to you) + standing instructions + project files and memory notes + conversation so far + documents and retrieved text + your message. It does not redraw the scoring half of Signature 4, and Signature 6 is not nested inside it (no double counting of context and examples). `highlight` takes layer names; the stage variants below make up the figure count. Signature 6 appears only in F6.9, with a callout mapping its parts to layers.

| ID | Title | Type | Section | Objective |
|---|---|---|---|---|
| F6.1 | Chapter 6 at a glance (optional chapter; AI Work Loop, Prompt highlighted; the opening case linked to 6.4 and 6.7) | Chapter map (imports `work_loop` from ch01_figures) | Opening | all |
| F6.2 | Everything the model receives this turn shares one context window | **Signature 4 reuse**: `llm_anatomy(stage="context", note="Recall from Chapter 3")` | 6.1 | O1 |
| F6.3 | Two more layers can fill the window before you type | **Context Layers**, complete, the two new layers highlighted | 6.1 | O1 |
| F6.4 | One irrelevant sentence lowered a 2022 model's accuracy on math word problems (tested 2023) | Data chart from published values (Shi et al., 2023; data/ch06_distraction.csv) [VERIFY values] | 6.2 | O2 |
| F6.5 | The documents you add are the layer you control most directly | Context Layers variant, documents layer highlighted | 6.2 | O2 |
| F6.6 | Two labeled excerpts with the task last replace a 120-page catalog | Before/after layout (merges v0.1 F6.3 and F6.5) | 6.3 | O2 |
| F6.7 | One-sided examples pull the outputs toward one label | Illustrative schematic, labeled illustrative | 6.4 | O3 |
| F6.8 | Standing instructions, project files and memory fill layers automatically, so they need upkeep | Context Layers variant, those two layers highlighted | 6.5 | O4 |
| F6.9 | A template keeps the prompt's fixed parts and leaves placeholders for what changes | Signature 6 import (`prompt_anatomy`), placeholders marked; callout: its context part → document/project layers, its in-context-examples part → your message | 6.6 | O5 |
| F6.10 | A library entry records when to use it, what it was tested on, and what changed | Library entry card with its test record (merges v0.1 F6.9 and F6.10) | 6.6 | O5 |
| F6.11 | A check between steps catches errors where they start | Sam's three-step chain (rectangle = step, hexagon = AI, rounded = Sam's check, diamond = pass/fix); ≤ 7 boxes | 6.7 | O6 |
| F6.12 | Medprompt raised GPT-4's MedQA score from 81.4% to 90.2% without changing the model's settings (2023) | Data chart from published values (Nori et al., 2023; data/ch06_medprompt.csv); ablation panel only after Figure 6 is verified | Case Study | O3 |
| F6.13 | Medprompt changed what the model received and how often it was asked | Context Layers variant: your-message layer (examples) highlighted, plus a "five runs, then a vote" workflow note outside the frame | Case Study | O3 |
| F6.14 | Chapter summary card | Summary card (complete Context Layers) | Summary | all |

14 figures (v0.1 F6.12 workflow-vs-agent dropped; the contrast is a text table in 6.7). No dependency on Chapter 4's Signature 5. Interactive in Compass: a context-layer builder and a template tester. **Dependencies:** `llm_anatomy` (ch03_figures.py, exists); `prompt_anatomy` (ch05_figures.py, being built). Chapter 6 imports, never redraws (Risk 1).

## 10. Labs (tool-neutral; current tool steps in Compass)

**Lab 6.1 Template Your Prompt** — Studio · 30 minutes · **at home first** (Thursday Feb 4 belongs to the A3 sprint; a team that finishes early may start it in class) · individual.

| Minutes | Step |
|---|---|
| 0–5 | Take your final A3 prompt (or the provided one); mark what stays fixed and what changes each time |
| 5–12 | Rewrite it as a template with placeholders; add "when not to use" |
| 12–25 | Run it on three test inputs it has not met before (typical, different, edge); record each result against pass criteria |
| 25–30 | Fix one failure; re-run the earlier inputs; save as v1.1 with a version note (first library entry) |

**Lab 6.2 Context A/B** — home · 25 minutes. **Three provided questions, each with an answer key**, each asked with (a) no document, (b) the whole provided document with unrelated sections, (c) two labeled excerpts with the task last; score each answer against the key. Step 4 adds two in-context examples to (c) and judges the change on the same three questions (with and without).

**Lab 6.3 Two Steps or One?** — home · 25 minutes. Constructed meeting notes with planted errors (a wrong date, a misattributed task): one prompt vs. a two-step chain with your check in between; count the errors each catches.

**Lab 6.4 Audit Your Standing Context** — home · 15 minutes · optional. Look at what your tool's standing instructions, project files and memory hold (where to find them: Compass); fix or delete one stale or risky item. **What you record or submit: item types and the action taken** (e.g., "memory note about my job — deleted, outdated"), **never the contents.** No-feature route: audit a provided sample memory list.

Accessibility and alternatives: dated sample outputs on eLearning for every lab (opt-out and no-device route: analyze the samples); every lab has a "paste it at the start of a new chat" fallback for free tiers without projects or memory; screen-reader-friendly test-record table; provided texts only; no personal or confidential data (course guidance D15; Ch. 15).

## 11. Risks and checks

1. **Chapter 5 dependency.** `prompt_anatomy(highlight=…)` (ch05_figures.py) is needed for F6.9; drafting of 6.6 waits for it; no redraw. Chapter 5's blueprint (v0.x) defines in-context examples and test inputs in Core; Chapter 6 reuses its glossary wording and must not re-teach its single-prompt iteration. Check Chapter 5's final term for the examples part ("in-context examples", per the editor's decision) before drafting.
2. **Chapter 3 dependency.** `llm_anatomy` exists; `context_layers` must reuse its labels ("System prompt — set by the tool's maker" etc.) exactly, or the editor decides the wording. Reuse Chapter 3's glossary wording for context window, system prompt, retrieval, inference once its handoff lands.
3. **No Chapter 4 dependency** (Chapter 4 is read in week 5): forward pointers only.
4. **Later Core chapters must not depend on this optional chapter** (Decision 2).
5. **Medprompt numbers** (Figure 6) and Shi et al. table values are verified before any chart or prediction key is written.
6. **Fast-aging product features.** No product names or numbers in running text; one dated "as of October 2026" box with at least two providers plus the university tools; click paths only in Compass; refresh-list rows in the handoff.
7. **Research on older models.** Example-order findings come from GPT-3-era models (2021–2022) and distraction from a 2022 model tested in 2023; state model and year; present as patterns to test; Nori et al. (2024) shows a reversal for a newer model.
8. **Interested sources, labeled:** Medprompt (Microsoft authors, OpenAI model); Chroma's context-rot report (a vendor of retrieval software; not peer reviewed); Anthropic posts (a model provider). Peer-reviewed sources carry every general claim; vendor posts are used only for definitions and dated practice; the workflow/agent line is "adapted from" Anthropic, not quoted as a standard.
9. **No anthropomorphic verbs.** "In-context learning" appears at most once as the research term, with the explanation that no settings change; never "the model learns from your examples", "remembers", "pays attention"; use "receives", "uses", "produces", "the product stores a note".
10. **Boundaries:** no tool comparisons (Ch. 12); no loops where the model chooses steps (Ch. 14); privacy, memory risk and injection get one-sentence pointers (Ch. 4 §4.6; Ch. 15).
11. **Medical content.** Medprompt is a benchmark result; benchmark ≠ clinical practice; the nursing example uses a public leaflet, never patient data.
12. **Characters.** Sam only; new details to log (handoff): runs the robotics club's weekly meeting and writes the update email for members; drafts the club's parts orders within the club's budget rules (consistent with Ch. 4's vendor-quote example); keeps his prompt library as a plain text file; a stale memory note from his completed co-op. Classmates' names in his notes are replaced with roles before pasting. No units example (already used in Ch. 1 and Ch. 4).
13. **Equity of access.** Every lab works on a free tier with the paste-at-start fallback.

## Decisions taken under delegation (D19)

| # | Decision | Reason |
|---|---|---|
| 1 | **Tags in a Deep chapter:** 6.1–6.5 and 6.7 are Deep; 6.6 (templates and the library) is Studio because it builds the artifact and is the lab's extension. No Core subsections; numbering 6.1–6.7 (no "Deep 6.A"). Not examinable, per D20 (midterm = Core sections of Chapters 1–10); review questions are practice. Check Yourself items are answerable from each subsection's own text | Book map path D; anatomy defines Deep as optional; CLAUDE.md requires a tag on every subsection; D20 |
| 2 | **Book-wide:** later Core chapters (12, 14, 15, 19) may point to Chapter 6 but must define any Chapter 6 term they need (e.g., prompt chain, standing instructions, memory) themselves | A Core chapter cannot rest on optional reading |
| 3 | Subsections ~900–1,400 words; fast route (~20 min, with a recap box in 6.6) and full route (~65 min), both at 150 words per minute with "longer if English is not your first language" stated in the Chapter Map | Optional chapter in Chapter 5's week; keeps ≥ 10,000 words |
| 4 | Work Loop highlight: Prompt (Verify second) | The chapter designs what the model receives and tests it before reuse |
| 5 | **Opening Case: Medprompt (Nori et al., 2023)**, returned to in the Case Study with the 2024 reversal; From the Field stays in part 11. Departure from the book map's case entry | The anatomy requires a real, cited event in the Opening Case |
| 6 | **From the Field: Şeker (2018), CRISP-DM**, facts limited to the article; present-day connections marked. OptiCRM (2022) rejected: it describes the author's company's product (would need D16) and is about AI in business-process software rather than repeatable method | Best fit for "reusable process"; not commercial |
| 7 | Personal prompt library: optional and ungraded, at least 3 entries, 2–3 h across weeks 3–11; 10-point rubric (course criteria and weights; process evidence split into tests and revision); alternative assignment; Mini-Project; suggested reuse in A11 and A13. No change to the live syllabus | Syllabus lists 13 graded artifacts; the library is not one of them |
| 8 | Lab 6.1 is a home lab first (in class only for a team that finishes the A3 sprint early); Labs 6.2–6.4 at home; Lab 6.4 records item types and actions, never contents | Thursday belongs to Chapter 5's sprint; privacy |
| 9 | **Terminology:** naming table in §3; "system instructions" (Ch. 3 wording) for the provider's layer, Key Term "system prompt" reused from Ch. 3; "standing instructions"; "project space"; "memory" = a product feature that stores notes; "in-context example" (Ch. 5 definition, word for word) and "test inputs" with the labels typical, different, edge reused from Ch. 5; "prompt chain"; workflow vs. agent "adapted from Anthropic (2024c)" | One definition per term; no clash with Ch. 2, 3, 5, 14 |
| 10 | **Context Layers** = `context_layers(highlight=…)` in ch06_figures.py, an extension of Signature 4's context stage (imports `llm_anatomy` conventions), 7 boxes, reusable in Ch. 10, 14 and 15; not a thirteenth signature diagram. Signature 6 appears only in F6.9 | Density limit (≤ 9 boxes); no redraw of Signature 4; no double counting |
| 11 | Featured character Sam only; other fields use unnamed one-off figures; Sam's tasks avoid the units theme | Rotation table; variety across chapters |
| 12 | Case file id: **C17** (registry), cases/C17-medprompt.md, with a Failure label line (2023: none on the tree; 2024 reversal: "other", dashed = inferred) | Editor's case registry; Ch. 4 labeling convention |
| 13 | The term's 2025 origin (Lütke; Karpathy) appears as one dated sentence in 6.1, cited through the original posts and Willison (2025) | Students meet the term at work; dated so it can age |
| 14 | Min et al. (2022) and Yoo et al. (2022) move to Further Reading; 6.4 keeps three claims | One core idea; the label debate is advanced |
| 15 | No workflow-vs-agent figure; Signature 7 (`delegation_ladder`, Ch. 5) is not reused, because a person-run chain does not map cleanly onto one rung; Chapter 5's "agency ≠ agent" box is recalled in one sentence in 6.7 | Avoids a misleading mapping and Signature 9 territory; one owner per shared idea |
| 16 | **Book-wide rules applied (chapter-brief, production additions):** time estimates at 150 words per minute with "longer if English is not your first language"; Sclar et al. (2024) owned by Ch. 5 (6.3 points back); "in-context example" defined by Ch. 5; test-input labels typical, different, edge; no Ch. 4 dependency; C17's failure label is a case-file line only (student-facing tree labels start in Ch. 8) | Consistency across chapters |

## Open [VERIFY] items

1. **Medprompt Figure 6 (Nori et al., 2023):** starting point and every ablation step with its accuracy (the text's +3.4, +2.2, +2.2 sum to 89.2%, not 90.2%). Blocks the Case Study prediction key and F6.12's second panel.
2. Shi et al. (2023) table values for F6.4 (95.0 → 72.4; 77.8 with the instruction; code-davinci-002; 100 base problems): read from ar5iv; confirm against the published PDF.
3. Nori et al. (2024): exact accuracies (o1-preview with and without few-shot; GPT-4 with Medprompt) and the full author list (OpenAI co-authors?).
4. Yoo et al. (2022), "Ground-truth labels matter" (EMNLP 2022): authors and pages (Further Reading).
5. Lütke's and Karpathy's posts: exact dates (status IDs in Willison, 2025; around June 19 and June 25, 2025).
6. Dated box: Anthropic Projects (June 25, 2024, secondary sources), Google Gems (August 28, 2024), OpenAI memory (February 13, 2024; expanded April 10, 2025), and **which features Microsoft Copilot and CometAI offer under the UTD license**, all as of October 2026. What CometAI is, exactly, to be confirmed from UTD pages.
7. Anthropic system-prompt publication: release-notes page date (coverage August 26, 2024).
8. Şeker (2018) CRISP-DM: page range in YBS Ansiklopedi 5(2) (not printed in the Drive copy).
9. Brown et al. (2020) page range (1877–1901) in NeurIPS 33.
10. Hong et al. (2025): confirm the model list; only the general claim is used (performance becomes less reliable as input grows).

## Author-only items

1. The CRISP-DM article's affiliation reads "Bilkav Eğitim Danışmanlık". If that is the author's own company, confirm that no disclosure is needed (the article promotes no product; the plan treats it as non-commercial).
2. Optional: a short anecdote from a CRISP-DM project the author ran, for From the Field. Without it the section stays within the article; nothing is invented.
3. No live-syllabus change is proposed.

## Planned sources and verification status (checked online 2026-10-18)

| Source | Use | Status |
|---|---|---|
| Nori, H., Lee, Y. T., Zhang, S., … Horvitz, E. (2023). *Can generalist foundation models outcompete special-purpose tuning? Case study in medicine* (arXiv:2311.16452) | Opening Case, Case Study, F6.12, F6.13 | Verified: 81.4% (GPT-4, five examples, from earlier work, Table 1) → 90.2% (Medprompt: 5 similar examples, self-written reasoning, 5-run shuffle ensemble); no fine-tuning; limits stated. Ablation steps [VERIFY Figure 6] |
| Nori, H., et al. (2024). *From Medprompt to o1* (arXiv:2411.03590) | Case Study twist | Verified (abstract): few-shot hinders o1; o1-preview without techniques beats GPT-4 with Medprompt; numbers and authors [VERIFY] |
| Shi, F., Chen, X., Misra, K., Scales, N., Dohan, D., Chi, E., Schärli, N., & Zhou, D. (2023). Large language models can be easily distracted by irrelevant context. *ICML*, PMLR 202, 31210–31227 | 6.2 prediction, F6.4 | Verified; table values [VERIFY] |
| Liu, N. F., et al. (2024). Lost in the middle. *TACL*, 12, 157–173. doi:10.1162/tacl_a_00638 | 6.2, 6.3 | Verified |
| Hong, K., Troynikov, A., & Huber, J. (2025, July 14). *Context rot* (Chroma technical report) | 6.2, Short 2 | Verified (18 models; general finding only) |
| Sclar, M., Choi, Y., Tsvetkov, Y., & Suhr, A. (2024). Quantifying language models' sensitivity to spurious features in prompt design. *ICLR* | 6.3 pointer back to Ch. 5 (owned there) | Verified |
| Brown, T. B., et al. (2020). Language models are few-shot learners. *NeurIPS 33* | 6.4 | Verified; pages [VERIFY] |
| Lu, Y., Bartolo, M., Moore, A., Riedel, S., & Stenetorp, P. (2022). Fantastically ordered prompts…. *ACL*, 8086–8098. doi:10.18653/v1/2022.acl-long.556 | 6.4, Short 1 | Verified |
| Zhao, Z., Wallace, E., Feng, S., Klein, D., & Singh, S. (2021). Calibrate before use. *ICML*, PMLR 139 | 6.4, Short 1 | Verified |
| Min, S., et al. (2022). Rethinking the role of demonstrations. *EMNLP*, 11048–11064 | Further Reading | Verified |
| Yoo, K. M., et al. (2022). Ground-truth labels matter. *EMNLP* | Further Reading | [VERIFY] details |
| Wu, T., Terry, M., & Cai, C. J. (2022). AI chains. *CHI '22*. doi:10.1145/3491102.3517582 | 6.7 | Verified (20-person study; quality, transparency, control) |
| Anthropic (2024c, December 19). *Building effective agents* (R11) | 6.7 | Verified (workflows = predefined code paths; agents direct their own steps; prompt chaining with gates) |
| Anthropic (2025, September 29). *Effective context engineering for AI agents* | 6.1 (dated definition), Further Reading | Verified |
| Anthropic (2024a). System prompts, release notes | 6.1, Ethics Lens | Verified via coverage (Willison, 2024-08-26); primary page date [VERIFY] |
| OpenAI (2024, February 13). *Memory and new controls for ChatGPT* | 6.5 dated box | Verified (with 2025 updates on the same page) |
| Anthropic (2024b). *Projects* announcement; Google (2024, August 28). *Customize Gemini with Gems* | 6.5 dated box | Verified via secondary sources and the Workspace blog; dates [VERIFY] |
| Microsoft Copilot; CometAI (university-provided tools) | 6.5 dated box | [VERIFY] features under the UTD license |
| Willison, S. (2025, June 27). *Context engineering* (links Lütke's and Karpathy's posts) | 6.1 | Verified |
| Schulhoff, S., et al. (2024). *The Prompt Report* (arXiv:2406.06608) | Further Reading | Verified |
| Şeker, Ş. E. (2018). CRISP-DM: Endüstriler arası standart işleme – veri madenciliği için. *YBS Ansiklopedi*, 5(2) | From the Field | Read in full (Drive); pages [VERIFY] |
| Chapman, P., Clinton, J., Kerber, R., Khabaza, T., Reinartz, T., Shearer, C., & Wirth, R. (2000). *CRISP-DM 1.0: Step-by-step data mining guide*. SPSS | From the Field (six phases) | Verified (author list, six phases) |

## Review changes (v0.1 → v0.2)

Must-fix: (1) all Chapter 4 dependencies removed: Spaced Review now from Chapters 3 and 2 with Chapter 5 as interleaving; Moffatt and the Failure Taxonomy Tree dropped from the plan; "context loss" defined in one sentence with a pointer to Ch. 4 §4.3; injection pointers read "Ch. 4 §4.6 (mechanism); Ch. 15 (defenses)". (2) Context Layers rebuilt as an extension of Signature 4's context stage (`llm_anatomy` imported), 7 boxes, Signature 6 no longer nested; Signature 6 shown only in F6.9 with a callout mapping its parts to layers; 6.1 explains how layers relate to the prompt anatomy. (3) Case id C17 (cases/C17-medprompt.md). (4) Medprompt: starting point stated (five examples, 81.4%, from earlier work), self-written reasoning stated, shuffle-and-vote framed as a workflow (6.7, F6.13), ablation steps marked [VERIFY] with a fallback prediction, F6.12 title says "without changing the model's settings". (5) Library field now "in-context examples: used / not used, and the test that decided".
Should-fix: one Bloom verb per objective, testing and versioning moved to the rubric, UNESCO:DES-A for O6 (6); 6.4 cut to three claims, Min and Yoo to Further Reading (7); workflow vs. agent "adapted from Anthropic (2024c)", Ch. 14 owns software workflows and gates (8); workflow-vs-agent figure dropped (9); F6.3 + F6.5 merged into F6.6, the test record merged into the library card, titles state findings, F6.4 "a 2022 model (tested 2023)", count made up with Context Layers variants (10); Ch. 5 boundary per the editor's decision, "in-context examples" and "test inputs" reused (11); Sam's 6.2/6.3 task is now a club parts order, his standing instruction is about audience, not units (12); library time 2–3 h, minimum 3 entries, rubric levels differing on one dimension, tests and revision scored separately (13); 150-word recap box in 6.6 for the fast route (14); Lab 6.1 home first, Lab 6.2 with three questions and answer keys, Lab 6.4 records item types and actions only (15); dated box includes Microsoft Copilot and CometAI with [VERIFY] on the UTD license (16).
Consider: naming table added, Ch. 3's "system instructions" wording reused (17); From the Field stays CRISP-DM, optional anecdote and affiliation added to Author-only items (18); C17 failure label line added (19); D20 recorded (20); Chapter Map links the opening case to 6.4 and 6.7, Ethics Lens used for O4 (21).

Editor's additional notes (applied in v0.2): reading times recomputed at 150 words per minute (fast route ~20 min, full route ~65 min) with "longer if English is not your first language"; test-input labels changed to typical, different, edge throughout (labs, rubric, faded example); "in-context example" reused word for word from Ch. 5; Sclar et al. (2024) reduced to a pointer back to Ch. 5; Chapter 5's "agency ≠ agent" box recalled in 6.7; figure imports confirmed as `prompt_anatomy(highlight=...)` and `delegation_ladder(highlight=...)` from ch05_figures.py (only `prompt_anatomy` is used); C17's failure label stays a case-file line with documented/inferred marking; no student-facing tree labels in Ch. 6.
