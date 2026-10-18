# Chapter 5 blueprint — Framing Tasks and Iterating Prompts

Status: v0.2 (2026-10-18), APPROVED under delegation (D19). v0.2 applies the editor's independent blueprint review (19 items, with the editor's bracketed decisions overriding the reviewer; see "Review changes" at the end) and the "Book-wide rules added during production" in docs/production/chapter-brief.md.
Part II — Working with AI · Syllabus week 3 · Path: Core · Featured student: **Lucía** (only featured student, per the rotation; other people are unnamed one-off figures) · Work Loop steps highlighted in the Chapter Map: **Frame and Prompt** (`work_loop(["Frame", "Prompt"])`).

**Source material.** The syllabus's week-3 sessions: Tuesday "Framing a task" (demo: vague prompt versus framed prompt; reading R2 module 2) and Thursday's "Prompt iteration sprint" (a real task, at least four versions, a peer swap test), producing **A3 prompt and iteration log**. Chapter 1's AI Work Loop (Frame and Prompt steps, §1.6). The AI Fluency framework, version 1.1 (Dakan & Feller, 2025b), for the three modalities and the Delegation and Description competencies; its one-page summary (Dakan, Feller & Anthropic, 2025) for the 4D overview only. Paraphrase only; the framework's diagrams are not reproduced. From the Field: the author's 2014 entry on the 5 Whys (registry docs/production/ftf-sources.md).

## 1. Outcome link and week 3

| Item | Value |
|---|---|
| Syllabus outcome | **LO2** (frame a task and improve results through deliberate, documented iteration); LO3 in support (testing a prompt is a verification habit) |
| Studio artifact | **A3 — Prompt and iteration log**, due Monday, February 8, 2027, 11:59 p.m. **Hosted here** (section 5.6 and the Application Assignment; one rubric, one alternative assignment) |
| Reading order | As in the syllabus (no change): R2 module 2 before Tue Feb 2; Chapter 5 before Thu Feb 4 (Deep: Chapter 6). Reading order in weeks 1–5 is Ch. 1 → 2, 3 → 5 (+6) → 7 → 4 + 8, so nothing here depends on Chapter 4 |
| In-class time | **Tue Feb 2:** Opening Case (Klarna, 10 min); concept core = 5.1–5.3; demo "vague versus framed prompt" = the 5.3 worked example run live, twice each; concept check on framing and the ladder. **Thu Feb 4:** Lab 5.1 "Prompt iteration sprint" (5.6) |
| Readings | R2 = Anthropic Academy, *AI Fluency: Framework & Foundations*, module 2, "The AI Fluency Framework" (the course has 10 modules; module 1 = "Introduction to AI Fluency"; docs/refresh-list.md). Modules 4 (Delegation) and 5 (Description) are recommended in Further Reading, not assigned |

### Week 3 workload (out of class), at 150 words per minute

| Item | Time |
|---|---|
| R2 module 2 (two short lessons) | ~15 min [VERIFY length] |
| **Chapter 5 Core + Studio reading** (≤ 4,700 words incl. examples; v1 draft ~4,650) | **≤ 31 min** (longer if English is not your first language) |
| A3 at home after the lab (v4 and second runs, peer swap record, verification, declaration) | 45–60 min |
| **Total** | **~1.5–1.8 h** (syllabus: 1–2 h) |
| Optional: Deep 5.A–5.B, L5.2–L5.3, Chapter 6 (Deep) | 45–90 min |

**Word budget.** Core subsections ~650–950 words, Studio 5.6 ~550; Core + Studio ≤ 4,700 words (raised from 4,200 at drafting; the week stays under 2 h). The chapter reaches ≥ 10,000 words with the Opening Case, Deep sections, Case Study, Ethics Lens, Career Connection, From the Field and the End-of-Chapter Package. Examinable scope = Core sections only (D20).

## 2. Chapter objectives (6; one Bloom verb each)

| # | Objective — after this chapter you will be able to… | Bloom | LO | Framework tags |
|---|---|---|---|---|
| O1 | **Apply** the Frame step to a real task (goal, audience, 3–5 checkable success criteria, limits, what stays with you) | Apply | LO2 | 4D:DEL · 4D:DESC · UNESCO:HCM-A |
| O2 | **Justify** which mode of working with AI (or none) fits each part of a task | Evaluate | LO2 | 4D:DEL · UNESCO:HCM-A |
| O3 | **Construct** a prompt from the parts its task needs (role, task, context, constraints, in-context examples, output format) | Apply | LO2 | 4D:DESC · UNESCO:TECH-A |
| O4 | **Diagnose** a weak output by tracing it to a missing or unclear part of the prompt or frame | Analyze | LO2 | 4D:DESC · 4D:DISC |
| O5 | **Judge** whether the evidence supports "this prompt works" | Evaluate | LO2, LO3 | 4D:DISC · UNESCO:TECH-A |
| O6 | **Produce** A3, a documented prompt and iteration log | Create | LO2, LO4 | 4D:DIL · 4D:DESC |

The skills behind each verb (one change at a time with a prediction; repeated runs, typical/different/edge test inputs and the peer swap; rung per part) are success criteria in the rubric and the sequences, not extra objective verbs. Framework terms stay in English; the three modalities and Delegation's "Goal and Task Awareness" sub-competency (breaking a task into AI, human and collaborative parts; Dakan & Feller, 2025b) are named once in Core.

## 3. Prerequisites and promises kept

From Chapter 1: prompt, output, AI Work Loop, jagged frontier, assistance vs. outsourcing, AI Use Declaration, the support-center study. From Chapter 3: token, context window, system prompt, sampling (why the same prompt gives different answers), temperature, knowledge cutoff, no learning from your chat, memory as a product feature, agent (one paragraph). From Chapter 2: example (a dataset item) and test set, contrasted with "in-context example" and "test inputs".
**Promises kept:** Ch. 1 §1.6 ("Chapter 5 is devoted to this step"); Ch. 3 §3.4 (designing context is Ch. 6, so 5.3 introduces context as one prompt part only).
**Boundary with Chapter 6 (book-wide rule):** Chapter 5 ends at single-prompt iteration; Chapter 6 starts at reuse across inputs. Ch. 5 defines **in-context example** in Core with one illustration; Ch. 6 owns choosing, balancing, ordering and testing them, context layers, standing instructions, memory and prompt chains. Both use **test inputs: typical, different, edge**. Ch. 5 owns Sclar et al. (2024).

## 4. Misconceptions (refutation pattern; six)

| # | Misconception | Where | Refutation evidence |
|---|---|---|---|
| M1 | "Good results come from magic words: say *please*, give an order, offer a tip, or tell it it is an expert" | 5.3 (role), 5.4 | Meincke et al. (2025a): *please* vs. *I order you* on 198 questions × 100 runs; Meincke et al. (2025c): tips and threats generally no significant effect; Zheng et al. (2024): personas did not improve accuracy on 2,410 factual questions. Two-sided: formatting alone moved accuracy by up to 76 points in one 2023 test (Sclar et al., 2024), so the lesson is "test, don't trust tricks", not "wording never matters" |
| M2 | "You can skip framing and just start typing; the tool will work out what you want" | 5.1, 5.5 | Zamfirescu-Pereira et al. (2023): participants expected the system to understand instructions as a person would and were surprised by the results; the peer swap test (5.5) shows what was in your head but not in the prompt |
| M3 | "What is in my head reaches the tool" (Ch. 3 recall: only the context reaches the model) | 5.3, 5.5 | Ch. 3 §3.4; peer swap result in the worked example |
| M4 | "More detail is always better, and every prompt needs all six parts" | 5.3 | Google (2024): not every prompt needs every part; irrelevant information lowered accuracy in a published test (Shi et al., 2023; numbers in Ch. 6) |
| M5 | "If it worked once, the prompt works; if it failed once, the tool cannot do it" | 5.5 | Zamfirescu-Pereira et al. (2023): overgeneralizing from single successes and failures; Meincke et al. (2025a): the same prompt varied across 100 runs even at temperature 0 |
| M6 | "Handing more to AI (a higher rung) is the more advanced, better use" | 5.2, Opening Case, Case Study | The framework presents no hierarchy and says interactions often mix modalities (Dakan & Feller, 2025b); Klarna's CEO later said cost had weighed too heavily and promised customers a human option (second-hand, via Bloomberg, 2025 [VERIFY]) |

## 5. Concept sequence

**Session question, answered in the Summary:** *Is getting good results from AI mainly a matter of finding the right words?* Answer: mostly no. Results depend first on framing (what the task is, what good looks like, which parts to hand over and how), then on giving the tool what the task needs, then on testing deliberately. Wording does matter, in ways that are hard to predict, which is why you test rather than trust a trick.

**Opening Case (450–550 words): Klarna's AI assistant, 2024–2025.** Every figure is attributed as Klarna's own: on February 27, 2024, the company said its assistant (built with OpenAI) had 2.3 million conversations in its first month, two-thirds of its customer-service chats, work it put at the equivalent of 700 full-time agents; resolution time under 2 minutes instead of 11; satisfaction on par with human agents; 25% fewer repeat inquiries; an estimated $40 million profit improvement in 2024; customers could still choose a human (Klarna, 2024). The case frames the question: **"By the measures Klarna chose, it worked. Were they the right measures?"** In May 2025, according to Bloomberg's interview as reported by other outlets, CEO Sebastian Siemiatkowski said cost had been too dominant a factor and the result was lower quality, and that customers would always be able to reach a person (Bloomberg, 2025; Entrepreneur, 2025) [VERIFY wording against Bloomberg]. No layoff or headcount claims. The Case Study adds the November 2025 earnings-call statements (CX Dive, 2025). Explanation in Core: 5.1 (success criteria decide what "working" means; "this book reads…") and 5.2 (where the human check sits).

**Prediction before the evidence (start of 5.4):** "*Please answer the following question* vs. *I order you to answer the following question*: over 198 hard science questions asked 100 times each, which scores higher?" Answered with Meincke et al. (2025a) and F5.10.

**Agency is not an agent (box in 5.2, two lines).** In the AI Fluency framework, *agency* is a way of working: you configure AI to carry out future tasks on your behalf, often for others (Dakan & Feller, 2025b). An *agent* is a kind of system in which the model chooses its own steps and tool calls (adapted from Anthropic, 2024). A configured course chatbot is agency without being an agent. Reused in 6.5, 7.5 and Ch. 14.

**Two meanings (contrast box in 5.3):** *example* (Ch. 2: one item in a dataset) vs. **in-context example** (a sample input with its desired output, placed in the prompt to show the pattern); *context window* (Ch. 3: everything the model receives in one turn) vs. **context** as a prompt part.

| # | Subsection | Tag | One new core idea | Examples (worked → faded → Your Turn) | Figures |
|---|---|---|---|---|---|
| 5.1 | Frame Before You Prompt | Core | A **task frame**: goal, audience, 3–5 checkable **success criteria**, limits, what stays with you; written before the first prompt, because every version is scored against it; providers' own guides start here (Anthropic, n.d.; OpenAI, n.d.; Google, 2024). Opening-case explanation (measures) | **Worked:** Lucía is asked by the accounting students' association to make a one-page "budget basics" handout for a first-year workshop; vague wish → frame card (public, constructed figures only). **Faded:** a biology student's lab-safety summary for a new lab group (goal and audience given; reader writes criteria and limits). **Your Turn:** frame one task from your major | F5.1b `work_loop(["Frame","Prompt"])`; F5.2 frame card |
| 5.2 | How Much to Hand Over: The Delegation Ladder | Core | **Signature 7.** The framework's three modalities, paraphrased from v1.1: **automation** (AI carries out a task you define), **augmentation** (you and AI define and carry out the task together, turn by turn), **agency** (you configure AI to carry out future tasks on your behalf, often for others). Order = the framework's Modality 1–3 numbering. **This book** draws them as a ladder over a floor ("no AI"), with **one axis**: how hard it is to see and check what the AI contributed **before it takes effect**. The framework presents no hierarchy and notes that interactions often mix modalities; a higher rung is not a better use. **Rung per part:** the framework's Goal and Task Awareness = splitting a task into AI, human and collaborative parts. Box: agency is not an agent | **Worked:** Lucía's handout split into parts on rungs: choosing what first-year students need (no AI), drafting definitions (automation, checked against her textbook), working out why her example budget confuses readers (augmentation), and, separately, a study-group FAQ chatbot she might configure from the course's public FAQ (agency: it answers classmates when she is not there). **Faded:** a history student's archive-visit report: two parts placed; reader places two. **Your Turn:** split one of your tasks into parts and place each | F5.3 Signature 7; F5.4 three questions |
| 5.3 | The Anatomy of a Prompt | Core | **Signature 6.** Six parts: **role**, **task**, **context**, **constraints**, **in-context examples**, **output format**; the task is the one part always needed (Google, 2024). Role sets voice, audience, vocabulary, not accuracy (Zheng et al., 2024). Context = what this task needs that the tool cannot otherwise receive (Ch. 6 designs it). Constraints = limits and must-nots; a "do not" instruction is still text the model receives (in one 2022 study a prompt telling a chatbot not to say a phrase was followed by that phrase; Zamfirescu-Pereira et al., 2023). **In-context example** defined with one illustration (Brown et al., 2020); choosing and testing them → Ch. 6. Output format = the shape you can check. More is not always better (Shi et al., 2023, no numbers). Contrast box | **Worked:** Lucía's v1 ("Make a budget handout for freshmen") → six-part v2, parts labeled, in-context examples left out and why (constructed outputs, labeled). **Faded:** an engineering lab-report abstract prompt with task, context and role filled; reader adds constraints and format. **Your Turn:** label the parts of a prompt you used this week; cross out one you did not need | F5.6 Signature 6; F5.7 Lucía's v1 vs. v2 |
| 5.4 | Iterate on Purpose | Core | **Iteration**: diagnose → trace to a part (or to the frame) → change **one** thing → predict → rerun → score against the criteria → log → keep or revert. Why: runs differ (Ch. 3) and wording effects are real but unpredictable (Sclar et al., 2024; Meincke et al., 2025a). Rerun in a fresh chat for a clean test; follow-ups in the same chat keep earlier turns in the context (Ch. 3). Ask "why?" more than once: if the trace ends at the frame, reframe instead of rewording; sometimes the answer is not to use AI. Drawn as the Work Loop's Prompt ↔ Verify cycle | **Prediction** answered. **Worked:** Lucía's log rows v2 → v4. **Faded:** a museum exhibit-label prompt (arts) with two rows filled; reader writes row 3. **Your Turn:** Lab 5.1 | F5.8 iteration loop; F5.9 why-chain; F5.10 data chart |
| 5.5 | One Result Is Not Evidence | Core | "Works" = meets the criteria across **repeated runs** and **test inputs** (typical, different, edge); rerun earlier inputs after each change (a fix can break an earlier fix); the **peer swap test**. Evidence: Zamfirescu-Pereira et al. (2023), described exactly (10 participants, mostly STEM professionals and graduate students, GPT-3 text-davinci-002, 2022, a cooking-assistant chatbot; authors say not representative). "Test inputs", not "test set" (Ch. 2), with the analogy. Failure Diary line in the Your Turn | **Worked:** Lucía's v4 on three test inputs × two runs; peer swap with an unnamed classmate reveals "freshmen" meant different things (no ages, no budget period; fix: audience and period in the context). **Faded:** a sociology survey-question rewrite with three provided outputs; reader judges "it works" and names the missing test. **Your Turn:** Lab 5.1 + "Save this for your Failure Diary (Chapter 4)" | F5.11 test grid; F5.12 peer swap |
| 5.6 | The Iteration Sprint (A3) | Studio | What a strong log shows (one change, a prediction, a score per version; a keep/revert decision) and what a weak log looks like (four rewordings, no criteria); v1 = the first prompt written from your frame card | Condensed sample log (Lucía's) with notes keyed to the rubric; faded: a partial log to finish | F5.13 log template |
| Deep 5.A | Techniques Beyond the Six Parts | Deep | Step-by-step prompting (chain of thought; Wei et al., 2022) and its smaller benefit for newer reasoning models (Meincke et al., 2025b); asking the tool what it needs before it answers; the field's map of 58 text techniques (Schulhoff et al., 2024). Prompt chains: one-sentence pointer to Ch. 6 (6.7) | — | — |
| Deep 5.B | How People Actually Delegate | Deep | One provider's August 2025 data, one classifier: automation patterns in about half of chat conversations (49%) vs. 77% of business API traffic (Appel et al., 2025); earlier split (57% augmentation, 43% automation; Handa et al., 2025) mentioned without a trend claim because the classifier changed. Definitions differ from the AI Fluency modalities; one provider | — | F5.14 |

Other anatomy parts:

| Part | Plan |
|---|---|
| Case Study (1 main + 2 short) | **Main (cases/C18-klarna-assistant.md):** Klarna, revisited. By the framework's definition, Klarna's assistant is **agency** (the company configured AI to answer future customers on its behalf), and so, from the company's side, was Chapter 1's support tool. The real contrast is **where the human check sits**: in Ch. 1 an agent reviewed each suggestion before the customer saw it; at Klarna the customer received the answer directly, with an option to ask for a person (pointer to Ch. 14's approval gates). Measures chosen vs. measures later named; company claims vs. independent evidence; November 2025: the CEO said the assistant did the work of more than 853 full-time agents and had saved about $60 million (company statements, CX Dive, 2025), while an analyst quoted there said Klarna had over-pivoted to cost containment. **Short 1:** "Why Johnny Can't Prompt" (Zamfirescu-Pereira et al., 2023) through the iteration loop. **Short 2:** "Small changes, big swings" (Sclar et al., 2024; Meincke et al., 2025a): what "it works" means depends on how you measure. No Signature 5 in student text |
| Ethics Lens | Who carries the cost of a badly framed delegation (customers who cannot reach a person, workers whose work is redefined, the person who signs the output); success criteria carry values (speed and cost vs. quality and choice); telling people when they deal with AI (pointer to Ch. 17–18, no legal claims); what goes into a prompt (Ch. 15; D15 course guidance) |
| Career Connection | Marketing/communications specialist (a creative brief is a prompt anatomy); accountant or auditor (framing an analysis request, keeping the judgment); teacher (practice items with constraints and a key to check); software tester / quality analyst (test inputs, a fix that breaks an earlier fix); nurse educator (patient materials with must-not constraints); operations manager (deciding which parts of a process to automate and where the human check sits). Descriptive only |
| From the Field | **Şeker (2014a), 5 Whys entry**, facts limited to the entry: the method; the car example; the criticisms it reports from Toyota's then global purchasing head Teruyuki Minoura (stays at symptoms; cannot go beyond what the investigator and respondents know; "why" questions can lead the wrong way; not repeatable across people and times; focus can scatter); the refinement (confirm each answer before the next "why"). **Present-day connections, marked as the book's:** "why does this task exist?" is the Frame step; "cannot go beyond what you know" applies to a frame; "not repeatable" is why 5.5 reruns a prompt; "confirm each answer first" is one change at a time. No fishbone (Chapter 4's source). No commercial disclosure. Optional author anecdote (Author-only) |
| Summary + Key Terms | Answers the session question two-sidedly; Signatures 6 and 7 as the summary visual; Warm-up revisited |

**Key Terms (Core):** task frame · success criteria · Delegation Ladder · automation · augmentation · agency (mode of working with AI) · anatomy of a prompt · role (prompt part) · task (prompt part) · context (prompt part) · constraint · in-context example · output format · iteration · iteration log · test inputs · peer swap test. Reused word for word: prompt, output, AI Work Loop, AI Use Declaration, example (Ch. 2), context window (Ch. 3), agent (Ch. 3). "In-context example" is defined here and reused word for word by Ch. 6.

## 6. Example plan

| Skill | Worked | Faded (genuinely partly filled) | Your Turn |
|---|---|---|---|
| Framing (O1) | Lucía's budget-basics handout: vague wish → frame card | Biology lab-safety summary: goal, audience given; reader writes 3 criteria and 1 limit | Frame a task from your major |
| Rung per part (O2) | Lucía's handout split into four parts on rungs + the FAQ chatbot as agency | History archive-visit report: two parts placed; reader places two | Split one of your tasks and place each part |
| Anatomy (O3) | Lucía's v1 → v2, parts labeled, examples left out with a reason | Engineering abstract: role, task, context given; reader adds constraints and format | Label a prompt you used this week; remove one unneeded part |
| Diagnosing (O4) | Lucía's log rows v2 → v4 with why-chains | Museum exhibit label: two rows filled; reader writes row 3 | Lab 5.1 |
| Judging evidence (O5) | Lucía's v4 on typical, different and edge inputs × 2 runs + peer swap | Survey-question rewrite: three outputs; reader judges and names the missing test | Lab 5.1 peer swap; Failure Diary line |
| A3 (O6) | Condensed sample log with rubric notes | Partial log: frame card and v1–v2 given | A3 |

Fields: business/accounting (Lucía), natural science (biology), history, engineering, arts, social science, health (Career Connection, Review B), education (Review B). No customer-service examples outside the Klarna case. Lucía's figures are constructed or public; no employer data (her job appears only as context she does not use). Outputs labeled "constructed example" or with model name and date.

## 7. Retrieval and spacing

- **Warm-up:** Have you reworded a prompt until it "worked"? How did you know? Does *please* change the answer? Will the same prompt give the same good answer again?
- **Check Yourself** after 5.1–5.6, 2–3 items each, at least one "why", answerable from Core.
- **Spaced Review (Chapters 3 and 2, read just before; plus Chapter 1):** why the same prompt gives different answers (Ch. 3); what is in the context window (Ch. 3); why a correction in your chat does not change the model (Ch. 3); example vs. in-context example and test set vs. test inputs (Ch. 2); the Work Loop steps (Ch. 1). No Chapter 4 items.
- **Forward:** Ch. 6 (context, in-context examples, reuse, prompt chains); Ch. 7 (tutor use; agency box); Ch. 8 (verification); Ch. 10 (voice); Ch. 12 (tool fit; Signature 7); Ch. 14 (agents, approval gates; Signatures 6 and 7); Ch. 15 (privacy); Ch. 21 (Signature 7). Failure Diary (Ch. 4, week 5).

## 8. Alignment matrix

| Objective | Taught | Practiced | Figures | Assessed | Artifact |
|---|---|---|---|---|---|
| O1 | 5.1 | Framing sequence; Lab 5.1 step 1 | F5.2 | Review A; B1 | A3 frame card |
| O2 | 5.2 | Rung-per-part sequence; L5.2 | F5.3, F5.4 | Review A; B2; C1; Case Study Questions | A3 frame card (rung per part) |
| O3 | 5.3 | Anatomy sequence; Lab 5.1 step 2 | F5.6, F5.7 | Review A; B3 | A3 versions |
| O4 | 5.4 | Diagnosis sequence; Lab 5.1 step 3; L5.3 | F5.8, F5.9, F5.10 | Review A; B3; B4 | A3 version table |
| O5 | 5.5 | Evidence sequence; Lab 5.1 step 4; L5.3 | F5.11, F5.12 | Review A; B4; C2 | A3 test and peer swap record |
| O6 | 5.6 | Partial log | F5.13 | Application Assignment | **A3** |

Review A 12–14 (distractors from M1–M6, no absolute giveaways; one item on example vs. in-context example), B 4, C 2–3, Spaced 4, Discussion 5, Case Study Questions 5, optional Mini-Project (one recurring task, three weeks of frame cards and log entries). Every item carries O · LO · Bloom. Odd answers → handoff; even → private/ch05-answers-even.md.

## 9. Application Assignment: A3 — Prompt and Iteration Log

**Due** Monday, February 8, 2027, 11:59 p.m. *(O6 · LO2, LO4 · Create)* Started in Thursday's lab; v1–v3 in class, v4 and second runs at home (45–60 min).

**Task:** a real task from your major, a job or daily life; **no personal or confidential data** (yours or anyone else's; course guidance), and no data from an employer unless you use the employer's approved tool under its rules. Task bank on eLearning.

**Submit:** (1) **Frame card**: goal, audience, 3–5 checkable criteria, limits, what stays with you, and **a rung for each part** of the task with one reason. (2) **At least four versions**: v1 = the first prompt you write from your frame card; each later version makes one named change (prompt part, or the frame) with a prediction. (3) **Test record**: every version run at least twice in a fresh, temporary chat; the final version on three test inputs (typical, different, edge); each output scored met / partly / not met per criterion; outputs or excerpts saved with tool name and date. (4) **Peer swap test**: a classmate runs your final prompt in a fresh chat without explanation and scores it against your criteria; what was missing; what you changed. (5) **Verification note**: each claim or number you relied on in the final output and how you checked it. (6) **Reflection** (3–5 sentences): the most and least useful change; when and why you stopped. (7) **AI Use Declaration**: tools, purpose, what you accepted, rejected or revised, how you verified it, where your judgment shaped the result.

**Rubric (10 points)** — syllabus split (task 3, process evidence 3, verification 2, declaration and judgment 2), process evidence scored as two criteria.

| Criterion (points) | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| **Task and frame (3)** | 3: real task; all frame elements; 3–5 checkable criteria; a rung per part, each with a reason | 2: all elements, but one or two criteria cannot be checked, or rung reasons are generic | 1: two or more elements missing, or criteria vague throughout | 0: no frame card |
| **Versions and changes (1.5)** | 1.5: at least four versions; each later version makes one named change with a prediction | 1: four versions; one or two change several things at once or lack a prediction | 0.5: two or three versions, or changes not named | 0: one version |
| **Testing evidence (1.5)** | 1.5: every version run twice; final version on typical, different and edge inputs; every output scored against the criteria | 1: most versions run twice and scored; final version on one or two inputs | 0.5: single runs, or scores not tied to the criteria | 0: no test record |
| **Verification (2)** | 2: peer swap recorded with what it revealed and what changed; every relied-on claim checked with a named method | 1.5: peer swap recorded; most claims checked | 1: peer swap or claim checks missing | 0: neither |
| **Declaration and judgment (2)** | 2: all five declaration elements; reflection names the most and least useful change with reasons and a stopping decision | 1.5: all five elements; general reflection | 1: two to four elements, or no reflection | 0: missing |

**Alternative assignment (iteration audit):** for students who prefer not to use AI tools, lack a device, or for whom the peer swap is a barrier. Analyze the dated log on eLearning (six versions of one prompt with real outputs, model names and dates): write your own frame card with a rung per part; label each change (one change or several); score every output against your criteria; choose a version and write v7 with a prediction; a classmate or the instructor reads v7 without explanation and lists what they would need to ask. Same rubric: Task and frame = your frame card; Versions = your labeling + v7; Testing = your scoring; Verification = the reader test + claim checks on your chosen version; Declaration = as above ("no AI tools used" where true).

## 10. Figures (titles state findings; ≤ 9 boxes; color + gray)

| ID | File id | Title | Type | Section | Obj. |
|---|---|---|---|---|---|
| F5.1 | f5-01-chapter-map | Chapter 5 at a glance | Chapter map, Frame and Prompt highlighted | Opening | all |
| F5.1b | f5-01b-work-loop | Framing and prompting are the first two of five decisions you make | `work_loop(["Frame","Prompt"])` imported | 5.1 | O1 |
| F5.2 | f5-02-frame-card | A task frame says what good looks like before the first prompt | Template card | 5.1 | O1 |
| F5.3 | f5-03-delegation-ladder | The higher the rung, the harder it is to check what the AI contributed before it takes effect | **Signature 7**, `delegation_ladder(highlight=None)` (str or list; parts none, automation, augmentation, agency) | 5.2, Summary | O2 |
| F5.3b | f5-03b-ladder-lucia | One task, several rungs: Lucía places each part of her handout | Signature 7 with per-part annotations | 5.2 | O2 |
| F5.4 | f5-04-three-questions | Three questions point to different rungs; they are weighed, not computed | Three questions, each with the rungs it points to | 5.2 | O2 |
| F5.5 | f5-05-klarna-storyboard | Klarna's public account moved from speed and cost (2024) to a guaranteed human option (2025) | Dated storyboard, figures attributed | Opening Case | O2 |
| F5.6 | f5-06-prompt-anatomy | A prompt has six parts; the task is the only one you always need | **Signature 6**, `prompt_anatomy(highlight=None)` (str or list); caption glosses "in-context examples" | 5.3, Summary | O3 |
| F5.7 | f5-07-lucia-v1-v2 | The framed prompt carries what Lucía knew but had not written down | Annotated prompt pair | 5.3 | O3 |
| F5.8 | f5-08-iteration-loop | Iteration is the loop between Prompt and Verify: one change, a prediction, a rerun, a score | Process diagram | 5.4 | O4 |
| F5.9 | f5-09-why-chain | Asking "why?" more than once traces a weak output back to the prompt, or to the frame | 5 Whys-style chain, each link marked checked or assumed (solid/dashed) | 5.4 | O4 |
| F5.10 | f5-10-wording-chart | How strictly answers were scored mattered more than "please" or "I order you" (GPT-4o, 2025) | Data chart of the report's own values: percentage points above random guessing with 95% CIs, four prompts × two standards (Meincke et al., 2025a, Supplementary Table 2), data/ch05_wording.csv | 5.4 | O4, O5 |
| F5.11 | f5-11-test-grid | A prompt works when it passes across runs and test inputs, not once | Test grid template | 5.5 | O5 |
| F5.12 | f5-12-peer-swap | A peer swap test shows what was in your head but not in your prompt | Flow | 5.5 | O5 |
| F5.13 | f5-13-log-template | A strong log shows one change, one prediction and one score at a time | Log template | 5.6 | O6 |
| F5.14 | f5-14-delegation-data | In one provider's August 2025 data, automation patterns were far more common in business API traffic than in chat | Data chart, same classifier only (Appel et al., 2025), data/ch05_delegation.csv | Deep 5.B | (Deep) |
| F5.15 | f5-15-summary-card | Chapter 5 summary card | Summary card | Summary | all |

Signature functions live in figures/scripts/ch05_figures.py and are imported by Chapters 6, 7, 10, 12, 14 and 21 (`from ch05_figures import prompt_anatomy, delegation_ladder`). Charts in ch05_charts.py from data/ch05_*.csv with source lines. Compass (after the MVP): a prompt builder (Signature 6) and a rung chooser (Signature 7) [COMPASS].

## 11. Labs (tool-neutral)

**Lab 5.1 Prompt iteration sprint** (Studio, Thursday, 75 min; teams of 3–4; individual A3).

| Minutes | Step |
|---|---|
| 0–10 | Briefing: log template; swap pairs; task bank for students without a task |
| 10–20 | Step 1 (individual): frame card with a rung per part; a teammate checks each criterion can be checked |
| 20–40 | Steps 2–3: v1 from the frame card, then v2 and v3 with one change each, one run each in a fresh, temporary chat, scored (second runs and v4 at home) |
| 40–55 | Step 4 (pairs): peer swap on v3 |
| 55–70 | Share and critique: the change that mattered most and one that did not |
| 70–75 | Exit: "My prompt works for … but I have not tested …" |

No "memory" term in the lab; "a fresh, temporary chat" where the tool allows it [COMPASS: settings by tool]. Accessibility: dated sample outputs (no-device and opt-out route = the alternative's audit); screen-reader-friendly log template; no personal or confidential data.

Optional home labs: **L5.2 Same task, two rungs** (Compare, 20 min: one task as automation and as augmentation; what you learned, how much checking each needed). **L5.3 Test a magic phrase** (Break It, 25 min: a popular trick, five runs with and without, two test inputs, conclusion limited to your test; one line: "Save this for your Failure Diary (Chapter 4)" if it fails).

## 12. Risks and checks

- **Klarna:** company figures attributed as claims, never stated as fact; CEO statements second-hand (Bloomberg via Entrepreneur, CX Dive) [VERIFY]; press release says two-thirds (one outlet says 75%); no layoff claims; the measures reading marked as the book's; refresh-list entry. Failure label in C18: none on the tree; workflow issue (where the human check sits) on a link of Chapter 4's failure-to-harm chain, inferred (dashed); not in student text before Chapter 8.
- **Zamfirescu-Pereira et al. (2023):** exact description; "do not say X" belongs to that model and setup.
- **Meincke et al. (2025a):** two 2024 models; one hard multiple-choice benchmark; temperature 0; the polite and commanding prompts also replaced the baseline wording; F5.10 plots the report's own values (differences from random guessing with CIs).
- **Zheng et al. (2024):** cite the published Findings of EMNLP title (arXiv v1 reported the opposite).
- **Sclar et al. (2024):** "up to 76 accuracy points", LLaMA-2-13B, few-shot, a maximum.
- **Economic Index:** one provider; one classifier per comparison; definitions differ from the framework's.
- **AI Fluency:** v1.1 (CC BY-SA 4.0) for definitions, the one-pager (CC BY-NC-SA 4.0) for the 4D summary; ladder, floor and axis labeled as the book's construction; "when and how" (v1.1 Delegation) vs. "whether, when and how" (one-pager); diagrams not reproduced.
- **Boundaries:** Ch. 6 (context layers, in-context examples beyond the definition, prompt chains, memory), Ch. 3 (mechanism one-line recalls), Ch. 12 (tool choice), Ch. 14 (agents, approval gates), Ch. 8 (verification method), Ch. 4 (no Signature 5).
- **Anthropomorphism:** "the model receives", "the output follows"; never "understands", "ignores", "tries".
- **Privacy:** constructed or public data; no employer data.
- **Characters:** Lucía only; new details logged (accounting students' association handout; considers a study-group FAQ chatbot).

## Decisions taken under delegation

| # | Decision | Reason |
|---|---|---|
| D-5.1 | Opening Case and main Case Study = Klarna (C18, editor-assigned); short cases = Zamfirescu-Pereira et al. (2023) and prompt sensitivity (Sclar et al., 2024; Meincke et al., 2025a) | Real, dated, primary-sourced; poses the measures question; contrasts with Ch. 1 on where the human check sits |
| D-5.2 | From the Field = the 5 Whys entry (registry); F5.9 is a why-chain, not a fishbone (Ch. 4's source); no disclosure | Editor decision (review item 5); no commercial interest |
| D-5.3 | No live-syllabus change; R2 module 2 = "The AI Fluency Framework" | Workload ≤ 2 h; numbering per docs/refresh-list.md |
| D-5.4 | Signature 7: framework's Modality 1–3 order; one axis (how hard to see and check what the AI contributed before it takes effect); floor "no AI"; ladder labeled as the book's construction | Review item 1; consistent with book map and visual guide |
| D-5.5 | Signature 6: six parts, task always needed; box label "In-context examples" (book-wide term) with a caption gloss; `highlight` accepts str or list | Review item 7 and the brief's Ch. 5/6 rule |
| D-5.6 | Rung per part in examples, frame card and rubric | Review item 2; framework's Goal and Task Awareness |
| D-5.7 | Lucía's main thread = a public budget-basics handout, not her employer's tickets | Review items 10 and 18 (privacy; field variety) |
| D-5.8 | F5.10 plots the report's own differences from random guessing with CIs; F5.14 compares one classifier only, no trend claim | Review item 15 |
| D-5.9 | Spaced Review from Chapters 3, 2 and 1; no Chapter 4 dependency | Reading order (brief) |
| D-5.10 | A3 rubric as above; peer swap under Verification; v1 from the frame card | Review items 9, 14 |

## Open [VERIFY] items

1. Bloomberg (May 8, 2025) wording (paywalled; via Entrepreneur, May 9, 2025, and CX Dive, Nov 20, 2025).
2. R2 module 2 length.
3. Şeker (2014a) page range in *YBS Ansiklopedi* 1(4) (printed line "pp. 5–6").
4. Google (2024) edition/date of *Prompting guide 101*.
5. Anthropic (2024) "Building effective agents" wording for the agent definition (adapted).

## Author-only items

1. Optional: a personal anecdote about framing a problem before solving it, for From the Field (never invented).
2. Optional live-syllabus note: R2 modules 4–5 (Delegation, Description) fit week 3 better than module 2.
3. Final voice edit.

## Review changes (v0.1 → v0.2)

(1) Signature 7 rebuilt on one axis (checkability before effect), Modality 1–3 order kept, no-hierarchy and mixing caveats, ladder and floor labeled as the book's; v1.1 cited for definitions, the one-pager for the 4D summary; R2 module 2 settled. (2) Rung per part added to examples, frame card and rubric. (3) F5.4 rebuilt: each question points to rungs; skill-building → no AI or tutor-style augmentation (Ch. 7); not a formula. (4) Klarna and Ch. 1's tool re-mapped as agency; contrast = where the human check sits; "agency is not an agent" box. (5) [Editor] From the Field stays the 5 Whys; F5.9 is a why-chain; no fishbone. (6) Case id C18; failure label line per the tree-vs-chain rule; no Signature 5 in student text. (7) "In-context example" defined in Core with one illustration; no separate "examples (in a prompt)" entry; caption gloss. (8) Prompt chains dropped from Deep 5.A; Shi et al. without numbers; test inputs "typical, different, edge". (9) Lab: "fresh, temporary chat"; v1–v3 in class, v4 at home. (10) Lucía uses public, constructed data, not employer tickets. (11) Opening Case asks whether Klarna's measures were the right ones; claims attributed; CEO words second-hand; no layoff claims; November 2025 statements added. (12) M2 refuted with Zamfirescu-Pereira et al. and the peer swap; Klarna kept for M6. (13) Reading time at 150 wpm; Core + Studio ≤ 4,700 words (~31 min); week ≤ 2 h; ESL note. (14) v1 = first prompt from the frame card. (15) F5.10 plots reported values; F5.14 one classifier only. (16) One Bloom verb per objective. (17) Chapter Map highlights Frame and Prompt. (18) Customer-service examples confined to the Klarna case. (19) Failure Diary line in the 5.5 Your Turn and L5.3.

## Revision notes after the chapter reviews (stage 5, 2026-10-18)

The chapter (v2) departs from this blueprint as recorded in docs/editorial/ch05-dev-memo.md:

- R2 module 2 is recommended, not required, in week 3 (D-5.e). The honest count is about 32 min for the Core sections, 53 min for the Core package and 60–70 min for A3.
- F5.1b removed; F5.10 moved to 5.5 (the measurement lesson) and reduced to please vs. order; F5.13 moved to 5.6.
- Lucía's log is one change per row; the final prompt (v5) is shown in 5.3. Klarna statements are re-cited with attribution tiers, and the SEC DRS/A (Jan 2025) has been added.
- The A3 rubric gaps are closed. The alternative assignment has its own rubric. The in-lab peer swap counts. The final version runs once on each of a different and an edge input.
- Role is now defined as voice or perspective (audience goes in context). The ladder axis describes each rung's default, and an approval gate does not change the rung.

**Final review (v3) departure, recorded:** Core + Studio is about 5,300 words by section count (5.2 ~1,070 and 5.5 ~1,050 exceed the ~950 ceiling), above the 4,700 cap. 5.5 was tightened in v3, but the cap is not reached. The week-3 count still stays ≤ 2.2 h: Core package ~53 min + Your Turn 5.3 ~5 min (the 5.1–5.2 Your Turns are done in Lab 5.1 step 2) + A3 60–70 min ≈ 2.0–2.15 h, with R2 recommended (D-5.e). Per the editor's rule, the overage is recorded rather than cut further.
