# Chapter 5 blueprint — Framing Tasks and Iterating Prompts

Status: v0.1 (2026-10-18), written by the chapter agent under delegation (D19). Awaiting an independent blueprint review; v0.2 will apply it. No chapter text is written until v0.2.
Part II — Working with AI · Syllabus week 3 · Path: Core · Featured student: **Lucía** (main and only featured student, per the rotation in docs/characters.md; other people in examples are unnamed one-off figures) · Work Loop step highlighted in the Chapter Map: **Prompt** (Chapter 1 promised that "Chapter 5 is devoted to this step"), with **Frame** highlighted again at the start of 5.1 by reusing the same drawing (`work_loop("Frame")`).

**Source material.** The syllabus's week-3 sessions: Tuesday "Framing a task" (demo: vague prompt versus framed prompt; reading R2 module 2) and Thursday's "Prompt iteration sprint" (a real task, at least four versions, a peer swap test), producing **A3 prompt and iteration log**. The AI Work Loop's Frame and Prompt steps from Chapter 1 (§1.6). The design guide's chapter line (Anatomy of a Prompt; iteration loop; Signatures 6 and 7) and the AI Fluency framework's three modes of interaction, which Signature 7 is built on (Dakan & Feller, 2025). No Haliç lecture covers this chapter. From the Field: the author's 2014 encyclopedia entry on the 5 Whys method (read on Drive for this blueprint; see §5 and Decisions).

## 1. Outcome link and week 3

| Item | Value |
|---|---|
| Syllabus outcome | **LO2** (frame a task for an AI system and improve results through deliberate, documented iteration); LO3 in support (testing whether a prompt works is a verification habit) |
| Studio artifact | **A3 — Prompt and iteration log**, due Monday, February 8, 2027, 11:59 p.m. **Hosted in this chapter** (section 5.6 and the Application Assignment, one rubric, one alternative assignment) |
| Reading order | As in the syllabus, unchanged: R2 module 2 before Tuesday, Feb 2; Chapter 5 before Thursday's lab, Feb 4 (Deep: Chapter 6). No live-syllabus change is needed (see Decisions, D-5.3) |
| In-class time | **Tue Feb 2:** Opening Case (Klarna, 10 min); concept core = 5.1–5.3 (frame, delegation ladder, anatomy); demo "vague versus framed prompt" = the 5.3 worked example run live, twice each (repeat runs recall Ch. 3); concept check on framing and the ladder. **Thu Feb 4:** Lab 5.1 "Prompt iteration sprint" (section 5.6) |
| Readings | R2: Anthropic Academy, *AI Fluency: Framework & Foundations*, "module 2" [VERIFY which lessons the syllabus means: the course's published outline has unnumbered blocks — Delegation, Description, a prompting deep dive, Discernment — so "module 2" is read here as the Delegation and Description lessons]. Chapter 5 cites the framework document itself (Dakan & Feller, 2025), not the course |

### Week 3 workload (out of class)

| Item | Time |
|---|---|
| R2, Delegation and Description lessons (Tuesday) | ~20–30 min [VERIFY lesson length] |
| **Chapter 5 Core + Studio reading** (≤ 4,500 words incl. examples) | **25–30 min** |
| A3 at home after Thursday's lab (finish versions, peer swap record, verification, declaration) | 45–60 min |
| **Total** | **~1.6–2.0 h** (syllabus: 1–2 h) |
| Optional: Deep 5.A–5.B, labs L5.2–L5.3, Chapter 6 (Deep) | 45–90 min |

**Word budget.** Core subsections ~700–850 words each and Studio 5.6 ~650, for ≤ 4,500 words of Core + Studio (the same week-budget exception as Chapters 2 and 3, because week 3 also carries R2 and A3). The chapter still reaches ≥ 10,000 words with the Opening Case, Deep sections, Case Study, Ethics Lens, Career Connection, From the Field and the End-of-Chapter Package.

## 2. Chapter objectives (6)

| # | Objective — after this chapter you will be able to… | Bloom | LO | Framework tags |
|---|---|---|---|---|
| O1 | **Apply** the Frame step to a real task: state the goal, the audience, three to five checkable success criteria, the limits, and what stays with you | Apply | LO2 | 4D:DEL · 4D:DESC · UNESCO:HCM-A |
| O2 | **Justify** how much of a task to hand to AI (automation, augmentation or agency, or none), using what an error would cost, whether you can check the result, and whether the task is meant to build your own skill | Evaluate | LO2 | 4D:DEL · UNESCO:HCM-A |
| O3 | **Construct** a prompt from the six parts (role, task, context, constraints, examples, output format), explain what each part contributes, and leave out parts the task does not need | Apply | LO2 | 4D:DESC · UNESCO:TECH-A |
| O4 | **Diagnose** a weak output by tracing it to a missing or unclear part of the prompt, and revise with one deliberate change at a time, recording a prediction and the result | Analyze | LO2 | 4D:DESC · 4D:DISC |
| O5 | **Judge** whether a prompt really works, using repeated runs, several test inputs and a peer swap test, instead of one good or bad result | Evaluate | LO2, LO3 | 4D:DISC · UNESCO:TECH-A |
| O6 | **Produce** A3: a task frame, at least four documented prompt versions, a peer swap test, verification of the final output and an AI Use Declaration | Create | LO2, LO4 | 4D:DIL · 4D:DESC |

Framework terms (Delegation, Description, Discernment, Diligence) stay in English (style sheet §2) and are named once in Core with the citation (Dakan & Feller, 2025).

## 3. Prerequisites and promises kept

From Chapter 1: prompt, output, the AI Work Loop (Frame → Prompt → Verify → Decide → Disclose), the jagged frontier, assistance versus outsourcing, the AI Use Declaration, the support-center study (an assistant that suggested replies to human agents). From Chapter 3: tokens, the context window ("everything the model receives in one turn"), next-token sampling and why the same prompt gives different answers, system prompt, knowledge cutoff, "it does not learn from your chat". From Chapter 2: test set (used here only as an analogy; see the terminology note in 5.5).
**Promises kept:** Chapter 1 §1.6 says the Prompt step "is devoted" to Chapter 5; Chapter 3 §3.4 says designing context belongs to Chapter 6 — this chapter introduces *context as one prompt part* (what this task needs that the tool cannot get otherwise) and stops there.
**Not assumed:** Chapter 4 (failure taxonomy) is read in week 5 per the syllabus, after this chapter, so nothing here depends on Signature 5; forward pointers only.

## 4. Misconceptions (refutation pattern; six)

| # | Misconception | Where | Refutation evidence |
|---|---|---|---|
| M1 | "Good results come from magic words: say *please*, threaten it, or tell it it is a world-class expert" | 5.3 (role), 5.4 | Meincke et al. (2025a): *Please* vs. *I order you* made no overall difference on 198 questions run 100 times each; Meincke et al. (2025c): tipping or threatening generally no significant effect; Zheng et al. (2024): personas in system prompts did not improve accuracy on 2,410 factual questions. Refutation must not create "wording never matters" (see M1 note below) |
| M2 | "You can skip framing and just start typing; the tool will work out what you want" | 5.1, Opening Case | Klarna's CEO later named cost as a "too predominant" evaluation factor (Bloomberg, 2025, via secondary reports [VERIFY wording]); providers' own guides start from success criteria (Anthropic, n.d.-a; OpenAI, n.d.) |
| M3 | "The tool understands what I meant, the way a colleague would; what is in my head reaches it" | 5.3, 5.5 (peer swap) | Zamfirescu-Pereira et al. (2023): participants' human-to-human expectations were a main barrier; Ch. 3 recall: the model receives only what is in the context |
| M4 | "More detail is always better, and every prompt needs all six parts" | 5.3 | Google (2024): not every prompt needs every part; Shi et al. (2023): irrelevant information in a problem lowered accuracy |
| M5 | "If it worked once, the prompt works; if it failed once, the tool cannot do it" | 5.5 | Zamfirescu-Pereira et al. (2023): participants overgeneralized from single successes and single failures; Meincke et al. (2025a): same prompt, 100 runs, varied answers even at temperature 0 |
| M6 | "Handing more to AI (a higher rung) is the more advanced, better use" | 5.2, Case Study | The rung follows the task, the cost of error and checkability; Klarna's 2025 move to guarantee a human option; Ch. 1 support-center study (suggestions to agents) |

**M1 note.** The evidence is two-sided and must be taught that way: wording and format *can* change results a lot (up to 76 accuracy points from formatting alone in one 2023 test of LLaMA-2-13B; Sclar et al., 2024), but which change helps is hard to predict and often differs question by question (Meincke et al., 2025a). The lesson is "test, don't trust tricks", not "wording is irrelevant".

## 5. Concept sequence

**Session question, answered in the Summary:** *Is getting good results from AI mainly a matter of finding the right words?* Answer: mostly no. Results depend first on framing (what the task is, what good looks like, how much to hand over), then on giving the tool what the task needs (the six parts), and then on testing deliberately. Specific wordings do matter, but in ways that are hard to predict, which is why you test rather than trust a trick.

**Opening Case (450–550 words): Klarna's AI assistant, 2024–2025** — a real event, attributed exactly. On February 27, 2024, the payments company Klarna said its AI assistant (built with OpenAI) had handled 2.3 million conversations in its first month, two-thirds of its customer-service chats, doing work it put at the equivalent of 700 full-time agents, with resolution time down from 11 minutes to under 2, customer satisfaction on par with human agents, 25% fewer repeat inquiries and an estimated $40 million profit improvement for 2024; customers could still choose a human agent (Klarna, 2024). All are **company figures, not independent measurements**, and the text says so. In May 2025, CEO Sebastian Siemiatkowski told Bloomberg that the cost-cutting push had gone too far, that cost had been too dominant a factor in evaluating it and the result was lower quality, and that Klarna would recruit people so customers could always reach a human, using a flexible remote "Uber-type" model; the company remained committed to AI (Bloomberg, 2025, as reported by Entrepreneur, 2025 [VERIFY exact wording against the Bloomberg article]). **Chapter question:** *The assistant did what it was set up to do. Was it set up to do the right thing?* The explanation sits in Core: 5.1 (success criteria decide what "working" means — this book reads the CEO's statement as a framing problem; Klarna has not used that word) and 5.2 (which rung the work was placed on). A line tells students the story is still developing ("as of October 2026"; refresh list).

**Prediction before the evidence (start of 5.4):** "Two prompts differ only in the first words: *Please answer the following question* and *I order you to answer the following question.* Over 198 hard science questions, asked 100 times each, which gets more right?" Answered in 5.4 with the published result (Meincke et al., 2025a) and F5.10.

**Two meanings of "example" and "context."** A contrast box in 5.3: *example* in Chapter 2 (one item in a dataset) vs. *examples* as a prompt part (sample inputs and outputs you include to show the pattern you want); *context window* in Chapter 3 (everything the model receives in one turn) vs. *context* as a prompt part (the background this task needs). A Review A item reinforces it.

| # | Subsection | Tag | One new core idea | Examples | Figures |
|---|---|---|---|---|---|
| 5.1 | Frame before you prompt | Core | A **task frame** turns a vague wish into a task you can check: goal, audience, 3–5 checkable **success criteria**, limits, and what stays with you; write the criteria *before* the first prompt, because they are what every later version is scored against; three providers' guides say the same (Anthropic, n.d.-a; OpenAI, n.d.; Google, 2024). Opening-case explanation (success criteria) | **Worked:** Lucía's team lead asks for "a summary of this week's tickets"; she reframes it (goal: the three most common reasons for refund requests; audience: team lead, 2 minutes to read; criteria; uses exported category counts, never customer messages — one-line privacy pointer to Ch. 15). **Faded:** framing a study task for an accounting course (goal and audience filled; reader writes criteria and limits). **Your Turn:** frame one task from your major | F1.2 reuse `work_loop("Frame")`; F5.2 task frame card |
| 5.2 | How much to hand over: the Delegation Ladder | Core | **Signature 7.** Three ways of working with AI from the AI Fluency framework — **automation** (AI carries out a specific task on your instructions), **augmentation** (you and AI think together), **agency** (you set AI up to carry out future tasks on your behalf) (Dakan & Feller, 2025, paraphrased) — arranged by this book as a ladder: the higher the rung, the further the AI's part reaches and the harder it is to see and check what it contributed. The floor is "no AI". Choosing a rung: can you check the result, what does an error cost and who bears it, is the task meant to build your skill (pointer to Ch. 7). Agency: one paragraph and a pointer to Ch. 14. Delegation (4D) named here | **Worked:** Lucía places three work tasks on the ladder (a routine "where is my order?" reply draft = automation with review; brainstorming why refund requests rose = augmentation; an auto-tagging assistant for incoming tickets = agency, which is not her decision alone and needs approval points, Ch. 14). **Faded:** a nursing student's three tasks (one placed, with the rule that patient information never goes into an AI tool; reader places two). **Your Turn:** place three of your tasks, with one reason each. Ch. 1 support center vs. Klarna as the two-rung contrast (one paragraph; full treatment in the Case Study) | F5.3 Signature 7; F5.4 choosing a rung |
| 5.3 | The anatomy of a prompt | Core | **Signature 6.** Six parts: **role**, **task**, **context**, **constraints**, **examples**, **output format**. The task (a clear verb and object) is the one part you always need; the others are added when the task needs them (Google, 2024). What each contributes: role sets audience, voice and vocabulary, but persona prompts did not make answers more accurate in a large test (Zheng et al., 2024); context = what this task needs that the tool cannot otherwise receive (designing context is Ch. 6); constraints = limits and must-nots (with the caution that a "do not" instruction is still text the model receives, and in one study a prompt saying not to say a phrase was followed by the phrase; Zamfirescu-Pereira et al., 2023); examples = show the pattern (in-context examples, Brown et al., 2020; few participants in the 2023 study used them); output format = the shape you can check. More is not always better: irrelevant detail can lower quality (Shi et al., 2023). Contrast box: two meanings of "example" and "context". Description (4D) named here | **Worked:** Lucía's v1 ("Summarize these tickets") rebuilt as a six-part prompt, each part labeled, with one part deliberately left out and why; run twice (constructed example, or real outputs with model names and dates). **Faded:** an engineering lab-report abstract prompt with task, context and role filled; reader adds constraints, an example and the format. **Your Turn:** label the parts of a prompt you used this week and cross out one you did not need | F5.6 Signature 6; F5.7 Lucía's v1 vs. v2, annotated |
| 5.4 | Iterate on purpose | Core | **Iteration** = diagnose the weak output, trace it to a part of the prompt, change **one** thing, predict the effect, rerun, score against the success criteria, log it, keep or revert. Why iterate at all: outputs vary between runs (Ch. 3) and wording effects are real but hard to predict (Sclar et al., 2024; Meincke et al., 2025a). Two ways to iterate: revise the prompt and rerun in a fresh chat (a clean test) or follow up in the same chat (fast, but earlier turns stay in the context, Ch. 3). When to stop rewording and go back to Frame (the task, not the words, is the problem) or decide not to use AI. The iteration loop is drawn as the Prompt ↔ Verify cycle inside the Work Loop, not as a new framework | **Prediction** (please vs. I order) answered here. **Worked:** Lucía's log rows v2 → v4 (symptom, traced part, one change, prediction, result on two runs). **Faded:** a museum exhibit-label prompt (arts/humanities) with two log rows filled; reader writes the next row. **Your Turn:** in Lab 5.1 | F5.8 iteration loop; F5.9 tracing a weak output (fishbone); F5.10 computed chart from published values |
| 5.5 | One result is not evidence | Core | A prompt "works" only when it meets the criteria across **repeated runs** and **several test inputs** (a typical one, a hard one, an edge case); after each change, rerun the earlier inputs to catch a fix that breaks an earlier fix; the **peer swap test** (someone else runs your final prompt in a fresh chat, without your explanation, and scores it against your criteria) shows what was in your head but not in the prompt. Evidence: non-experts in a 2022 lab study iterated opportunistically, stopped after one success, gave up after one failure, and rarely rechecked earlier problems (Zamfirescu-Pereira et al., 2023: 10 participants, GPT-3 text-davinci-002, a cooking-assistant chatbot; participants skewed toward STEM professionals and graduate students). Terminology note: "test inputs" here, not "test set" (Ch. 2's held-back labeled examples), with the analogy stated | **Worked:** Lucía's v4 on three weeks of category counts × two runs, then a peer swap with an unnamed classmate, who gets a summary in the wrong time frame because "this week" was in Lucía's head (the fix: dates in the context). **Faded:** a provided prompt with three outputs (social science: a survey-question rewrite); reader decides whether the evidence supports "it works" and what test is missing. **Your Turn:** Lab 5.1 | F5.11 test grid; F5.12 peer swap test |
| 5.6 | The iteration sprint (A3) | Studio | Turning 5.1–5.5 into a log: frame card, version table, test record, peer swap record, verification note, declaration. What a strong log shows (one change per version, predictions, scores against criteria, a decision to keep or revert), and what a weak one looks like (four rewordings with no criteria) | A complete sample log (Lucía's, condensed) with marginal notes keyed to the rubric | F5.13 A3 log template |
| Deep 5.A | Techniques beyond the six parts | Deep | Step-by-step prompting (chain-of-thought; Wei et al., 2022) and its decreasing value for newer reasoning models (Meincke et al., 2025b); splitting a task into a chain of smaller prompts; asking the tool to list what it needs before answering; the field's own map of 58 techniques (Schulhoff et al., 2024). Tool-neutral; no product settings | — | (none, or one schematic if needed) |
| Deep 5.B | How people actually delegate | Deep | One provider's published data on its own users: in Claude.ai conversations from late 2024 to early 2025, 57% were classified as augmentation and 43% as automation (Handa et al., 2025); by August 2025, automation-style use was about half (49% with the newer classifier, 45% with the older), and 77% of business API traffic showed automation patterns (Appel et al., 2025). Caveats in the text: one provider, its own classifier, and **definitions that differ from the AI Fluency modes used in 5.2** | — | F5.14 data chart (data/ch05_delegation.csv) |

Other anatomy parts:

| Part | Plan |
|---|---|
| Case Study (1 main + 2 short) | **Main:** Klarna, revisited on the Delegation Ladder and through the Frame step, side by side with Chapter 1's support center (suggested replies to agents = augmentation; answers to customers = automation with a human option): what each counted as success, who checked the output, what the 2025 statement changed. Company claims vs. independent evidence made explicit. **Short 1:** "Why Johnny Can't Prompt" (Zamfirescu-Pereira et al., 2023), traced through the iteration loop: where each observed habit breaks the loop. **Short 2:** "Small changes, big swings": prompt-format sensitivity (Sclar et al., 2024) and the 100-run benchmark design (Meincke et al., 2025a) — what "it works" means depends on how you measure |
| Ethics Lens | Who carries the cost of a badly framed delegation? Customers who cannot reach a person, workers whose jobs are redefined, and the person who signs the output (Ch. 1 responsibility). Success criteria carry values (speed and cost vs. quality and choice). Telling people when they are dealing with AI: pointer to Ch. 17–18 (no legal claims in Core). Privacy of what goes into a prompt: pointer to Ch. 15; course guidance on personal or confidential data (D15) |
| Career Connection | Customer-support team lead (deciding what to automate and how to review it); accountant or auditor (framing an analysis request, keeping the judgment); marketing or communications specialist (a creative brief is a prompt anatomy); teacher (generating practice items with constraints and an answer key to check); software tester / quality analyst (test inputs and "a fix that breaks an earlier fix" are everyday ideas); nurse educator (patient materials with must-not constraints). Descriptive only, no salary or job-growth figures |
| From the Field | **The author's 2014 encyclopedia entry on the 5 Whys** (Şeker, 2014a), facts limited to the entry: the method (ask "why" about a problem five times in a row), the entry's car example (a car that will not start, traced through a flat battery and a charging part past its service life to a missed maintenance step), the criticisms it reports from Toyota's then global purchasing head Teruyuki Minoura (stays at symptoms, cannot go beyond what the investigator and respondents know, "why" questions can lead the wrong way, results are not repeatable across people and times, focus can scatter), and the refinement it describes (confirm each answer before asking the next "why"). One sentence notes that the entry links the method to fishbone diagrams, the subject of a companion entry (Şeker, 2014b). **Present-day connections, marked as such:** asking "why does this task exist?" before prompting is the Frame step; "cannot go beyond what you know" applies to a frame as much as to an answer; "not repeatable" is why 5.5 runs a prompt more than once; "confirm each answer first" is one-change-at-a-time iteration. No commercial disclosure (no product or commercial interest involved; see Decisions). Optional: a personal industry anecdote only if the author supplies one (Author-only items) |
| Summary + Key Terms | Answers the session question (hedged, two-sided on wording); Signature 6 and Signature 7 side by side as the summary visual; Warm-up revisited with short answers |

**Key Terms (Core), proposed:** task frame · success criteria · Delegation Ladder · automation · augmentation · agency (mode of AI use) · anatomy of a prompt · role (in a prompt) · task (in a prompt) · context (in a prompt) · constraint · examples (in a prompt; few-shot examples) · output format · iteration · iteration log · test inputs · peer swap test. Reused word for word from the glossary: prompt, output, AI Work Loop, AI Use Declaration, assistance, outsourcing, example (Ch. 2 sense, in the contrast box only). Definitions go to the handoff file; "context (in a prompt)" is worded so Chapter 6 can extend it without a second definition.

## 6. Example plan (worked → faded → your turn)

| Skill | Worked | Faded (genuinely partly filled) | Your Turn |
|---|---|---|---|
| Framing (O1) | Lucía's weekly ticket summary: vague request → full frame card | Accounting study task: goal and audience given; reader writes 3 criteria and 1 limit | Frame a task from your major (frame card) |
| Choosing a rung (O2) | Lucía's three work tasks placed with reasons | Nursing student's three tasks: one placed and justified; reader places two | Place three of your tasks, one reason each |
| Anatomy (O3) | Lucía's v1 → six-part v2, parts labeled, one part deliberately omitted | Engineering lab-report abstract: role, task, context given; reader adds constraints, an example, a format | Label the parts of a prompt you used this week; remove one unneeded part |
| Diagnosing and revising (O4) | Lucía's log rows v2 → v4 (symptom → traced part → one change → prediction → result) | Museum exhibit label: two rows filled; reader writes row 3 | Lab 5.1 |
| Testing (O5) | Lucía's v4 on three inputs × two runs + peer swap result and fix | Survey-question rewrite: three provided outputs; reader judges the claim "it works" and names the missing test | Lab 5.1 (peer swap) |
| A3 (O6) | Condensed sample log with rubric notes (5.6) | A partial log for the reader to finish (frame card and v1–v2 given) | A3 |

Fields: business and accounting (Lucía), health (nursing student), engineering (lab report), arts and humanities (exhibit label), social science (survey question), education (Career Connection and Review B). All AI outputs are labeled "constructed example" or carry the model name and date (style sheet §5). Lucía's details stay within characters.md: part-time customer support, accounting major, saving for the CPA exam (the faded accounting task may be CPA study); new details are logged in the handoff file.

## 7. Retrieval and spacing

- **Warm-up** (three questions): Have you ever reworded a prompt until it "worked"? How did you know it worked? Does saying *please* to a chatbot change the answer? If a tool gives you a good answer once, will the same prompt give it again?
- **Check Yourself** after 5.1–5.6, 2–3 items each, at least one "why" each, **all answerable from Core**.
- **Spaced Review** (4): Chapter 3 (why the same prompt gives different answers; what is inside the context window; the model does not learn from your chat) and Chapter 1 (the five Work Loop steps; one frontier item). One Chapter 2 item on the two meanings of "example". No Chapter 4 items (read in week 5).
- **Spaced forward:** context design and prompt libraries → Ch. 6; tutor mode and learning vs. outsourcing → Ch. 7; verifying claims in outputs → Ch. 8; voice in AI-assisted writing → Ch. 10; tool choice → Ch. 12 (Signature 7 reused); agents and approval gates → Ch. 14 (Signature 7 "agency" highlighted; Signature 6 reused); privacy of prompt content → Ch. 15; personal code of practice → Ch. 21 (Signature 7 reused).

## 8. Alignment matrix

| Objective | Taught | Practiced | Figures | Assessed | Artifact |
|---|---|---|---|---|---|
| O1 | 5.1 | Framing sequence; Lab 5.1 step 1 | F5.2 | Review A; B1 | A3 frame card |
| O2 | 5.2 | Rung sequence; L5.2 | F5.3, F5.4 | Review A; B2; C1; Case Study Questions | A3 frame card (rung + reason) |
| O3 | 5.3 | Anatomy sequence; Lab 5.1 step 2 | F5.6, F5.7 | Review A; B3 | A3 versions |
| O4 | 5.4 | Iteration sequence; Lab 5.1 step 3; L5.3 | F5.8, F5.9, F5.10 | Review A; B3; B4 | A3 version table |
| O5 | 5.5 | Testing sequence; Lab 5.1 step 4; L5.3 | F5.11, F5.12 | Review A; B4; C2 | A3 test and peer swap record |
| O6 | 5.6 | Partial-log faded example | F5.13 | Application Assignment (rubric below) | **A3** |

Counts follow the anatomy: Review A 12–14 (distractors from M1–M6, no absolute giveaways; one item on the two meanings of "example"/"context"), B 4, C 2–3, Spaced 4, Discussion 5 (one ethics, one career, one interdisciplinary), Case Study Questions 5, optional Mini-Project. Every item carries O · LO · Bloom. Odd answers → handoff (Appendix E block); even → private/ch05-answers-even.md.

**Mini-Project (optional):** follow one recurring task (weekly or more often) for three weeks: a frame card, the rung you chose, and an iteration-log entry each time; at the end, say whether the rung or the criteria changed and why. Feeds the term portfolio (revision evidence, Ch. 20).

## 9. Application Assignment: A3 — Prompt and Iteration Log (hosted here)

**Due:** Monday, February 8, 2027, 11:59 p.m., on eLearning. *(O6 · LO2, LO4 · Create)* Started in Thursday's lab (section 5.6); about 45–60 minutes at home to finish.

**Task choice.** A real task from your major, a job or daily life that you would actually use AI for, with **no personal or confidential data** (yours or anyone else's; course guidance). If you cannot think of one, use a task from the eLearning task bank.

**What to submit:**

1. **Frame card:** goal, audience, 3–5 checkable success criteria, limits, what stays with you, and the rung you chose (automation, augmentation, agency or none) with one sentence of justification.
2. **At least four prompt versions.** v1 is your honest first attempt, written before reading your criteria back. Each later version makes **one deliberate change**, names the prompt part it changes (role, task, context, constraints, examples, output format), and states a prediction.
3. **Test record:** each version run at least twice; the final version on at least two different test inputs; each output scored against your criteria (met / partly / not met). Save the outputs or excerpts with the tool name and date.
4. **Peer swap test:** a classmate runs your final prompt in a fresh chat without your explanation and scores the output against your criteria; record what they got, what was missing from the prompt, and what you changed (if anything).
5. **Verification note:** for the final output, list each factual claim or number you relied on and how you checked it (or why the task had none).
6. **Reflection (3–5 sentences):** which change mattered most and why; one change that did not help; when you stopped and why.
7. **AI Use Declaration** with all five elements: tools, purpose, what you accepted, rejected or revised, how you verified it, and where your judgment shaped the result.

**Rubric (10 points)** — the syllabus split (task 3, process evidence 3, verification 2, declaration and judgment 2), with process evidence scored as two separate criteria.

| Criterion (points) | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| **Task and frame (3)** | 3: real task; frame card complete with 3–5 checkable criteria; rung chosen and justified by cost of error, checkability or learning | 2: frame card complete, but one or two criteria cannot be checked, or the rung reason is generic | 1: frame card missing two or more elements, or criteria are vague throughout | 0: no frame card |
| **Versions and changes (1.5)** | 1.5: at least four versions; each later version makes one named change with a prediction | 1: four versions; one or two versions change several things at once or lack a prediction | 0.5: two or three versions, or changes not named | 0: one version only |
| **Testing evidence (1.5)** | 1.5: every version run at least twice; final version on at least two inputs; every output scored against the criteria | 1: most versions run twice and scored; final version on one input only | 0.5: single runs, or scoring not tied to the criteria | 0: no test record |
| **Verification (2)** | 2: peer swap test recorded with what it revealed and what changed; every relied-on claim in the final output checked with a named method | 1.5: peer swap recorded; most claims checked | 1: peer swap or claim checks missing | 0: neither |
| **Declaration and judgment (2)** | 2: all five declaration elements; reflection names the most and least useful change with reasons and a stopping decision | 1.5: all five elements; general reflection | 1: two to four elements, or reflection missing | 0: missing |

**Formats.** A table (version, part changed, prediction, run 1, run 2, scores, keep/revert) or the eLearning template; screenshots are optional, saved text is enough. Compass offers the same template (optional, ungraded) [COMPASS: A3 template].

**Alternative assignment** (for students who prefer not to use AI tools, have no suitable device, or for whom the peer swap is a barrier). **Iteration audit:** analyze the dated iteration log provided on eLearning (six versions of one prompt with real outputs, model names and dates). Write your own frame card for its task; label each change by prompt part and say whether it was one change or several; score every output against your criteria; choose the version you would use and write a v7 with a prediction; instead of a peer swap, a classmate (or the instructor in office hours) reads your v7 without explanation and lists what they would need to ask. Same rubric, read this way:

- **Task and frame:** your frame card for the provided task, with a justified rung.
- **Versions and changes:** your labeling of the six changes plus your v7.
- **Testing evidence:** your scoring of every provided output against your criteria.
- **Verification:** the reader test of v7 and a check of the claims in the version you chose.
- **Declaration and judgment:** as above (declare "no AI tools used" where true).

## 10. Figures (titles state the finding; each serves an objective; ≤ 9 boxes)

| ID | Title | Type | Section | Objective |
|---|---|---|---|---|
| F5.1 | Chapter 5 at a glance (AI Work Loop, Prompt highlighted) | Chapter map; `work_loop("Prompt")` imported from ch01_figures | Opening | all |
| F1.2 (reuse) | Every AI-assisted task starts with a decision you make before any prompt | `work_loop("Frame")`, new caption | 5.1 | O1 |
| F5.2 | A task frame says what good looks like before the first prompt | Template card: goal, audience, criteria, limits, stays with you, rung (6 boxes) | 5.1 | O1 |
| F5.3 | The higher the rung, the harder it is to see and check what the AI contributed | **Signature 7: The Delegation Ladder** — floor "no AI", rungs automation, augmentation, agency; human role per rung (rounded boxes), AI part (hexagons); new reusable function `delegation_ladder(highlight=None)` | 5.2 | O2 |
| F5.4 | Three questions decide the rung: can you check it, what does an error cost, is the skill yours to build? | Decision flow (3 diamonds, ≤ 8 boxes) | 5.2 | O2 |
| F5.5 | Klarna's public account moved from speed and cost (2024) to quality and a human option (2025) | Case storyboard, dated, figures attributed to Klarna | Opening Case / Case Study | O2 |
| F5.6 | A prompt has six parts; the task is the only one you always need | **Signature 6: Anatomy of a Prompt** — task box thick and central, five optional parts around it (7 boxes); new reusable function `prompt_anatomy(highlight=None)`, `highlight` accepts one part name or a list (Ch. 6 highlights context, Ch. 10 role and constraints, Ch. 14 constraints and output format) | 5.3, Summary | O3 |
| F5.7 | The framed prompt carries what Lucía knew but had not written down | Annotated prompt pair (v1 vs. v2), parts labeled by shape and label, not color | 5.3 | O3 |
| F5.8 | Iteration is the loop between Prompt and Verify: one change, a prediction, a rerun, a score | Process diagram drawn as the Work Loop's inner Prompt ↔ Verify cycle, with an exit back to Frame (≤ 8 boxes) | 5.4 | O4 |
| F5.9 | A weak output can be traced back along the six parts of the prompt | Fishbone (cause-and-effect) diagram: head = weak output, six bones = six parts, one symptom per bone (7 boxes); links to From the Field | 5.4 | O4 |
| F5.10 | "Please" and "I order you" scored the same; small wording changes moved the strictest score (GPT-4o, 2025) | **Data chart from published values**: GPT-4o, GPQA Diamond (198 questions × 100 runs, temperature 0), four prompt conditions × two standards ("correct in 100 of 100 runs", "correct in a majority of runs"); values = 25% random baseline + reported risk difference (Meincke et al., 2025a, Supplementary Table 2), data/ch05_wording.csv, source line [VERIFY derivation against the report's Figure 1] | 5.4 | O4, O5 |
| F5.11 | A prompt works when it passes across runs and inputs, not once | Test grid template: 3 inputs × 2 runs × criteria, pass/partly/fail by symbol (✓ ◐ ✗), illustrative | 5.5 | O5 |
| F5.12 | A peer swap test shows what was in your head but not in your prompt | Flow: your prompt → peer, fresh chat, no explanation → output scored against your criteria → gap found → context added (≤ 6 boxes) | 5.5 | O5 |
| F5.13 | A strong log shows one change, one prediction and one score at a time | A3 iteration log template (table-figure; also on eLearning) | 5.6 | O6 |
| F5.14 | On one provider's chat service, automation-style use grew to about half in eight months (late 2024 to Aug 2025) | Data chart from published values (Handa et al., 2025; Appel et al., 2025), data/ch05_delegation.csv; caption notes the provider's own definitions and classifier | Deep 5.B | (Deep) |
| F5.15 | Chapter summary card | Summary card with Signatures 6 and 7 | Summary | all |

15 figures plus two reuses. Signature functions live in figures/scripts/ch05_figures.py and are imported by later chapters (`from ch05_figures import prompt_anatomy, delegation_ladder`). Data charts in ch05_charts.py from data/ch05_*.csv with source lines. Interactive in Compass (after the MVP): Signature 6 as a prompt builder and Signature 7 as a rung chooser [COMPASS].

## 11. Labs (tool-neutral)

**Lab 5.1 Prompt iteration sprint** — Studio, Thursday in class (75 minutes), teams of 3–4, individual A3.

| Minutes | Step |
|---|---|
| 0–10 | Briefing: the log template; pairs assigned for the peer swap; task-bank option for students without a task |
| 10–20 | Step 1 (individual): frame card, criteria and rung (O1, O2); a teammate checks that each criterion can be checked |
| 20–40 | Steps 2–3 (individual, team helps diagnose): v1, then v2–v4 with one change each, two runs each, scored (O3, O4) |
| 40–55 | Step 4 (pairs): peer swap test — run each other's final prompt in a fresh chat, score against the owner's criteria, report the gap (O5) |
| 55–70 | Share and critique: each team shows the single change that mattered most and one that did not |
| 70–75 | Exit: one sentence — "My prompt works for … but I have not tested …" |

Accessibility and alternatives: dated sample outputs on eLearning for every step (opt-out and no-device route = the alternative assignment's audit, started in class); screen-reader-friendly log template; memory and history features off or a temporary chat where the tool allows it, so earlier chats do not leak into the test [COMPASS: settings by tool]; no personal or confidential data in prompts.

**Optional home labs:**
- **L5.2 Same task, two rungs** (Compare · 20 min): do one study or work task once as automation ("produce it") and once as augmentation ("think it through with me"); compare what you learned and how much checking each needed (O2). No agency setups.
- **L5.3 Test a magic phrase** (Break It · 25 min): pick one popular prompting "trick"; run the prompt with and without it, five runs each, on two inputs, scored against criteria; conclusion limited to your test (O4, O5; M1).

## 12. Risks and checks

- **Klarna:** every figure attributed to Klarna (2024) as company-reported; CEO statements attributed to Bloomberg (2025) and paraphrased, with at most one short quotation; Bloomberg is paywalled — confirm wording against the article or a second outlet that quotes it [VERIFY]; secondary outlets misreport the share (one says 75%; the press release says two-thirds) — use the press release; the "framing problem" reading is marked as the book's; refresh-list entry (later Klarna statements may change the story).
- **Zamfirescu-Pereira et al. (2023):** describe exactly — 10 participants, mostly STEM professionals and graduate students (the authors say not representative), GPT-3 text-davinci-002 in 2022, a chatbot-design task; the "do not say X" observation is from that model and setup, not a general law.
- **Meincke et al. (2025a):** two 2024 models (GPT-4o, GPT-4o mini), one hard multiple-choice benchmark; the polite and commanding prompts also replaced the baseline wording, so state what was compared; F5.10 values are derived (baseline + difference) and labeled as such.
- **Zheng et al. (2024):** cite the published Findings of EMNLP title; the arXiv v1 under the earlier title reported the opposite and was revised — do not cite v1.
- **Sclar et al. (2024):** "up to 76 accuracy points" was measured on LLaMA-2-13B in few-shot classification-style tasks; say so.
- **Economic Index (Deep 5.B):** one provider's data on its own users; classifier changed between reports; its automation/augmentation definitions are not the AI Fluency definitions used in Signature 7 — say so in the caption and text; D12-style single-provider note.
- **Delegation Ladder:** the AI Fluency framework presents three modes, not a ladder; the ordering and the "harder to check" axis are this book's construction and are labeled as such. Agency kept to one paragraph (Ch. 14).
- **Boundaries:** no context layering, system-prompt design, custom instructions or prompt libraries (Ch. 6); no token or sampling mechanism beyond one-line recalls (Ch. 3); no tool or product comparison (Ch. 12); no claim checking method beyond "list and check what you rely on" (Ch. 8).
- **Anthropomorphism:** "the model receives", "the output follows", never "it understands what you mean", "it ignores", "it tries"; M3's refutation is phrased mechanically ("only what is in the context reaches the model").
- **Tool neutrality:** no product names in Core except where a cited study names its model; prompt boxes with outputs carry model name and date; settings in Compass.
- **Privacy:** Lucía works from category counts, never customer messages; A3 forbids personal or confidential data.
- **Characters:** Lucía only; the peer-swap partner and other people are unnamed; log new details (handoff).

## Decisions taken under delegation

| # | Decision | Reason |
|---|---|---|
| D-5.1 | **Opening Case and main Case Study = Klarna's AI assistant (2024–2025)**, with "Why Johnny Can't Prompt" (Zamfirescu-Pereira et al., 2023) and prompt-sensitivity studies (Sclar et al., 2024; Meincke et al., 2025a) as the two short cases. The book map's "From the Field (author case)" stays in the From the Field slot | The book map names no real case for Ch. 5 and cases/index.csv has none. Klarna is a real, dated, primary-sourced event that poses the chapter's framing question, sits in Lucía's field (customer support), and contrasts directly with Chapter 1's support-center study (suggestions to agents vs. answers to customers), which gives spaced retrieval and a two-rung example for Signature 7. The Johnny study is the stronger evidence for iteration but is a 10-person lab study, better as Core evidence and a short case than as the opening event. New case id for cases/index.csv (proposed C16) in the handoff |
| D-5.2 | **From the Field = the author's 2014 encyclopedia entry on the 5 Whys** (Şeker, 2014a), with a one-sentence link to his fishbone entry (Şeker, 2014b); both read on Drive (IDs 1DrAi2SG_C_WyYCC5xminYeMS0uoMl7zJ, 1qol4-fEJ33S84uOaeesMR3ntDsYnnVpw). No commercial disclosure | Chapter 2 set the precedent of an encyclopedia entry with marked present-day connections. The 5 Whys is about finding the real problem before solving it (framing), and the entry's own criticisms and refinement map onto iteration and repeat testing without stretching the source. The 2024 LLM manuscript was not used because D18 assigns it to Chapter 3 (it could serve Ch. 6 or 14). No product or commercial interest is involved, so the D16 disclosure does not apply |
| D-5.3 | **No live-syllabus change for week 3.** Ch. 5 stays the Thursday reading; Tuesday's concept session uses the Opening Case and 5.1–5.3 material; R2 stays the Tuesday reading | Unlike week 2 (D17), nothing in the week depends on reading the chapter before Tuesday; the estimated workload (~1.6–2.0 h) is inside the syllabus's 1–2 h, so no author decision is needed |
| D-5.4 | **Signature 7 keeps the book-map order** (automation → augmentation → agency) and defines the vertical axis as "how far the AI's part reaches, and how hard it is to see and check what it contributed", with a floor "no AI". The text says the framework itself presents three modes, not a ladder, and that a higher rung is not a better use (M6) | Keeps the visual guide, book map and front-matter preview consistent. A plain "autonomy" axis would put augmentation below automation; the "reach and checkability" axis supports the book map's order and fits every later reuse (Ch. 12 fit, Ch. 14 agency gates, Ch. 21 code of practice). Flagged for the independent review |
| D-5.5 | **Signature 6 = six parts with "task" as the only required part**; `prompt_anatomy(highlight=…)` accepts a part name or a list | Matches the visual guide's six parts and the providers' guidance that not every prompt needs every part; list highlighting is needed by Ch. 10 and Ch. 14 |
| D-5.6 | **Chapter Map highlights Prompt only**; Frame is shown by reusing `work_loop("Frame")` at the start of 5.1 | `work_loop()` in ch01_figures.py accepts one step; agents may not edit Chapter 1's script. The handoff will ask the editor whether to add list highlighting to `work_loop()` for chapters that strengthen two steps |
| D-5.7 | **Terminology:** "examples (in a prompt)" and "context (in a prompt)" are separate glossary entries from Ch. 2's "example" and Ch. 3's "context window", taught in a contrast box; "test inputs" instead of "test set" in 5.5 | One definition per term (style sheet §2); avoids the two-meanings confusion the Ch. 3 review found with "sampling" |
| D-5.8 | **Spaced Review draws on Chapters 3, 1 and 2, not Chapter 4** | Chapter 4 is read in week 5 per the syllabus, after this chapter |
| D-5.9 | **A3 rubric** keeps the syllabus split and scores process evidence as two criteria (versions and changes 1.5; testing evidence 1.5); the peer swap is scored under Verification | Same structure as A2 (Ch. 2); the syllabus names the peer swap as a lab requirement, and its purpose is to test whether the prompt carries its context, which is a verification act |
| D-5.10 | **Deep 5.B uses one provider's published usage data** (Anthropic Economic Index) with explicit single-provider and different-definition caveats | It is the only large published dataset on automation vs. augmentation in real use; neutrality is kept by labeling, as in D12 |

## Open [VERIFY] items

1. Bloomberg (May 8, 2025): exact wording of Siemiatkowski's statements (paywalled; currently confirmed through Entrepreneur, May 9, 2025, and the Bloomberg subtitle).
2. R2 "module 2": which lessons of the Anthropic Academy course the syllabus means, and their length.
3. F5.10 values: derivation (25% + risk difference from Supplementary Table 2) against the report's Figure 1 proportions.
4. Handa et al. (2025): exact data dates for the 57% / 43% split (reported as December 2024–January 2025 conversations in the September 2025 report's V1 label).
5. Şeker (2014a, 2014b): true page ranges in YBS Ansiklopedi 1(4), December 2014 (the printed citation lines disagree: "Kasım 2014, pp. 5–6"; "pp. 2–4" vs. "pp. 2–6"; inventory warns these lines are often wrong).
6. Google (2024) *Prompting guide 101*: confirm edition/date and the four-areas wording in the original PDF (secondary summaries consistent).
7. OpenAI and Anthropic prompt-engineering pages: record access dates (living documents; both checked October 18, 2026) and cite as n.d. with retrieval date.

## Verified for this blueprint (October 18, 2026)

Klarna press release, Feb 27, 2024 (klarna.com: figures above) · Bloomberg headline and subtitle, May 8, 2025, and Entrepreneur report, May 9, 2025 · Dakan & Feller (2025), *The AI Fluency Framework* (Anthropic-hosted PDF; three modes and 4D definitions; © 2025 Rick Dakan, Joseph Feller and Anthropic, CC BY-NC-SA 4.0) · Zamfirescu-Pereira, Wong, Hartmann & Yang (2023), CHI '23, doi:10.1145/3544548.3581388 (full text read: 10 participants, text-davinci-002, findings above) · Sclar, Choi, Tsvetkov & Suhr (2024), ICLR 2024, arXiv:2310.11324 · Meincke, Mollick, Mollick & Shapiro (2025a), Prompting Science Report 1, arXiv:2503.04818 (full text read: GPT-4o and GPT-4o mini, GPQA Diamond 198 questions, 100 runs each, temperature 0, conditions and tables) · Meincke et al. (2025b), Report 2, arXiv:2506.07142 · Meincke et al. (2025c), Report 3, arXiv:2508.00614 · Zheng, Pei, Logeswaran, Lee & Jurgens (2024), Findings of EMNLP 2024, pp. 15126–15154 · Shi et al. (2023), ICML 2023, PMLR 202 · Brown et al. (2020), NeurIPS 2020 · Wei et al. (2022), NeurIPS 2022 · Schulhoff et al. (2024), arXiv:2406.06608 · Handa et al. (2025), arXiv:2503.04761 · Appel, McCrory, Tamkin et al. (2025), Anthropic Economic Index report, Sept 15, 2025 · Anthropic (n.d.-a), "Prompt engineering overview" (success criteria and tests first) · OpenAI (n.d.), "Prompt engineering" guide (few-shot examples, evals while iterating) · Google (2024), *Gemini for Google Workspace: Prompting guide 101* (persona, task, context, format) · Şeker (2014a, 2014b), read on Drive.

## Author-only items

1. Optional: a short personal anecdote from industry or teaching about framing a problem before solving it (5 Whys or otherwise), for From the Field. The section works without it; never invented.
2. Final voice edit (pipeline step 8).
