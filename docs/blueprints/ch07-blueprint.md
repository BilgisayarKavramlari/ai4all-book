# Chapter 7 blueprint — Learning with AI: Tutor, Not Answer Machine

Status: v0.2 (2026-10-18), APPROVED under delegation (D19). v0.2 applies the editor's independent blueprint review (5 must-fix, 11 should-fix, 4 consider; see "Review changes" at the end) and the brief's book-wide production rules (reading order, tree vs. chain, Failure Diary prompt, Ch. 5/6 boundary, D20). Drafting starts only after Chapter 5's figure functions (`prompt_anatomy`, `delegation_ladder`) exist in figures/scripts/ch05_figures.py. **Draft v1 written 2026-10-18** (chapters/07-learning-with-ai-tutor-not-answer-machine.qmd, about 12,000 words; Core + Studio about 4,200); deviations from this blueprint are listed in docs/production/handoff/ch07.md (Decisions) and below.
Part II — Working with AI · Syllabus week 4 · Path: Core (examinable: Core sections only, D20; midterm covers Ch. 1–10) · Featured students: **Elif** (main) and **Marcus** (second), per docs/characters.md · Work Loop step highlighted in the Chapter Map: **Frame** (is the goal here the output or the skill?), with Verify second (a closed-book check verifies your learning, not the tool's answer).

**Source material.** Syllabus week 4: Tue Feb 9 concept session "Tutor or answer machine; the evidence" (R3, R4; demo: answer mode versus Socratic mode) and Thu Feb 11 tutor-mode lab (a new concept from your major plus three closed-book questions) → **A4 tutor-mode dialogue and reflection**, due Mon Feb 15. No Haliç lecture covers this chapter (docs/context/halic/ holds Lectures 2–3 only); it is built from the cited research below. Opening case C04, Bastani et al. (2025), read in full from the PNAS open-access text (PMC12232635) on 2026-10-18. From the Field: the author's 2015 encyclopedia entry on pair programming (read via Drive and tools/drive2md.py; see §5).

**Reading order (brief):** weeks 1–5 read Ch. 1 → 2, 3 → 5 (+6 Deep) → **7** → 4 + 8. Chapter 7 therefore does not depend on Chapter 4: sycophancy and model calibration are defined in Core here in one clause each and pointed forward to Chapters 4 and 8. No Failure Taxonomy Tree figure appears in Chapter 7 (student-facing tree labels start in Chapter 8).

## 1. Outcome link and week 4

| Item | Value |
|---|---|
| Syllabus outcome | **LO4** (distinguish responsible assistance from overreliance, undisclosed outsourcing and academic misconduct); LO3 in a supporting role (checking the tool's explanations against a course source) |
| Studio artifact | **A4 — tutor-mode dialogue and reflection**, due Monday, February 15, 2027, 11:59 p.m. Hosted in this chapter (section 7.6 and the Application Assignment), with its own 10-point rubric and an alternative assignment |
| Reading order within the week | **Before Tue Feb 9:** R3 only (Significance statement + Table 1, the main results; ~10 min). R4's abstract is read and discussed in Tuesday's class (no outside time). **Before Thu Feb 11:** Chapter 7 Core 7.1–7.5 and Studio 7.6, including the pre-lab Your Turn in 7.5 (choose a concept, a source and three keyed questions). This matches the syllabus, which lists Ch. 7 for Thursday; only the R3/R4 scope changes (Author-only item 1) |
| In-class time | **Tue Feb 9:** Opening Case (Bastani et al., 2025; 10 min); concept core = the ideas of 7.1–7.4 (performance vs. learning, retrieval practice, calibration, scaffold vs. crutch) with R4's abstract; demo "answer mode versus Socratic mode" (= the 7.5 worked example run live); ungraded concept check. **Thu Feb 11:** Lab 7.1 "Tutor-mode session" (section 7.6) |
| Readings | **R3** Bastani et al. (2025), PNAS version (open access): Significance statement and Table 1 (decision T1). **R4** Lee et al. (2025), CHI '25: abstract only, covered in class (decision T2) |

### Week 4 workload (out of class), counted honestly

| Item | Time |
|---|---|
| R3 (Significance + Table 1), before Tuesday | ~10 min |
| Chapter 7 Core + Studio reading (≤ 4,200 words incl. worked and faded examples) | 25–30 min (longer for ESL readers) |
| Your Turn items in 7.1–7.4 (four short items, ~2–3 min each) | ~10 min |
| Pre-lab Your Turn in 7.5 (concept, source, three keyed questions, baseline answers with confidence, setup prompt) | ~10 min |
| A4 at home: delayed closed-book check (10), finish annotation started in lab (10–15), verification (10), reflection (20), declaration (5) | 55–60 min |
| **Total** | **~1.8–2.0 h** (syllabus: 1–2 h) |
| Optional: labs L7.2–L7.3, Deep 7.A–7.B (not examinable, D20) | 45–60 min |

**Word budget.** Core 7.1–7.5 ≤ 3,400 words and Studio 7.6 ≤ 800 (≤ 4,200 together, incl. worked and faded examples; each Core subsection ~650–750 words), the same week-budget exception as Chapters 2, 3 and 5. The chapter still reaches ≥ 10,000 words with the Opening Case, Deep sections, Case Study, Ethics Lens, Career Connection, From the Field and the End-of-Chapter Package (estimate ~11,500).

## 2. Chapter objectives (6)

| # | Objective — after this chapter you will be able to… | Bloom | LO | Framework tags |
|---|---|---|---|---|
| O1 | **Explain** why performance while using AI can overstate learning, using the design, measures and limits of the Bastani et al. (2025) experiment | Understand | LO4 | UNESCO:HCM-U |
| O2 | **Explain** how retrieval practice builds lasting learning, with generation and spacing as supporting effects, and why it feels less effective than rereading or receiving answers | Understand | LO4 | UNESCO:HCM-U |
| O3 | **Distinguish** scaffolding from crutch use in an AI dialogue, turn by turn, and justify each label | Analyze | LO4 | 4D:DEL · 4D:DISC |
| O4 | **Set up** a tutor-mode session for a new concept: a setup prompt, an attempt-first rule, a course source with an answer key, and closed-book questions | Apply | LO4, LO2 | 4D:DESC · 4D:DEL |
| O5 | **Judge** how much you learned from a session by comparing predicted and actual closed-book performance, and decide what to change in your study practice | Evaluate | LO4 | UNESCO:HCM-A |
| O6 | **Produce** A4: a tutor-mode dialogue with annotations, an immediate and a delayed closed-book check, verification against a source, a reflection and an AI Use Declaration | Create | LO4 | 4D:DIL · UNESCO:ETH-A |

UNESCO codes follow the ai4all-frameworks table (HCM = human-centred mindset, ETH = ethics of AI). At most three tags per objective.

## 3. Prerequisites and promises kept

From Chapter 1: assistance vs. outsourcing (glossary wording reused verbatim), the three-zone policy, the AI Use Declaration, the test "if you cannot explain, defend or redo the work without the tool, you outsourced it", control group, random assignment, percentage point, the Jagged Frontier Map (F1.7), F1.13 "Working faster is not the same as learning", and the two-sentence preview of Bastani et al. in 1.2. From Chapter 3: fluent text can be false (3.2); retrieval adds documents to the context (3.5; contrast box in 7.2). From Chapter 5 (read in week 3): task frame and success criteria (5.1), the Delegation Ladder and its third question, "is the task meant to build your skill?" with its pointer to Chapter 7 (5.2), Signature 6 Anatomy of a Prompt (5.3), "test inputs" (5.5). Chapter 6 (Deep) is not assumed; no Chapter 6 term is used.

**Promise kept:** Chapter 1 said "You will study this in Chapter 7." Chapter 7 gives the full design, the exact numbers (relative change and percentage points), the mechanism, what students believed, and the limits. **Refinement, not contradiction:** Chapter 1 says the hint-giving version "largely avoided that harm"; Chapter 7 adds that it did not raise exam scores above the control group, and states exactly what the control group did and when the exam took place (the editor fixes Chapter 1's "never had access" / "later exam" wording; handoff).

**Link to Chapter 1, without repeating it (7.4).** One sentence plus a two-row table:

| What happens | What it is under the course policy |
|---|---|
| Crutch turns during permitted study help (the tool produces the answer you were meant to produce while you study) | Permitted study help that **costs you learning**; not misconduct |
| The tool's work is submitted as your own in graded work | **Outsourcing** (Chapter 1's not-acceptable zone) |

The closed-book check puts Chapter 1's "redo it without the tool" test into practice. A4 documents study habits; it is not a confession, and the A4 brief says so.

**Not repeated:** the three zones and the assistance/outsourcing definitions (Ch. 1); prompt anatomy (Ch. 5, reused as Signature 6); context design (Ch. 6); verification method (Ch. 8); writing and voice (Ch. 10; A4's reflection is graded for content and judgment, not prose style).

## 4. Misconceptions (refutation pattern; six)

| # | Misconception | Where confronted |
|---|---|---|
| M1 | "If I scored well while using AI, I learned it." | Opening Case, 7.1 (practice +48% vs. exam 17% lower than control) |
| M2 | "If studying feels easy and smooth, it is working; struggle means I am doing it wrong." | 7.2 (retrieval practice and desirable difficulties, with the caveat that not every difficulty helps) |
| M3 | "I can tell how well I have learned something." | 7.3 (calibration; Roediger & Karpicke's prediction data; Deslauriers et al.; Bastani students' perceptions) |
| M4 | "AI help is either always good for learning or always bad for it." | 7.4, Case Study (different designs and uses, different results; refutation must not create "design is all that matters": the evidence comes from a few studies, subjects and dates) |
| M5a | "Once a tool is in tutor mode, my learning is taken care of." | 7.5 (GPT Tutor matched, but did not beat, the control on the exam; tutor mode is one request away from answer mode) |
| M5b | "If the tutor says my answer is right, it is right." | 7.5 (GPT Tutor's accuracy came from teacher-supplied solutions; a model can agree with a wrong attempt, called sycophancy; score against your course source, not the tool's verdict) |

Elif's starting worry ("using AI to study is cheating") is not a separate misconception; the Chapter 1 link table in 7.4 answers it.

## 5. Concept sequence

**Session question, answered in the Summary:** *Can a chatbot help you learn, or only help you finish?* Hedged answer: both have been observed. In one school, one subject and fall 2023, unrestricted answer access raised practice scores and lowered unaided exam scores; a design that kept students working (hints instead of answers) avoided the harm (Bastani et al., 2025). Two structured tutors produced gains in short studies (Kestin et al., 2025; De Simone et al., 2025). The book's reading: what differed was who recalled and produced the answers, and that is partly under your control.

**Opening Case (450–600 words): the high-school experiment in Türkiye.** A research finding, with model and date in the first paragraph. Fall semester 2023–24, a large high school in Türkiye (the paper's own description; the school is not named in the text), nearly 1,000 students in about fifty 9th–11th-grade classes; classrooms randomly assigned to three arms; four 90-minute review sessions covering about 15% of the semester's math. Each session, in the same 90 minutes: teacher review → assisted practice (the only part that differed) → closed-book, closed-laptop exam whose problems were each paired with a very similar practice problem; both parts counted toward grades. Arms: **GPT Base** (a GPT-4 chat interface built to mimic ChatGPT), **GPT Tutor** (same model and interface; prompt with teacher-written solutions, common mistakes and an instruction to give hints, not answers), **control** (practiced the same problems with course books and notes, no devices). Results: practice +48% (Base) and +127% (Tutor) relative to the control mean; on the exam, Base students scored 17% lower than control (statistically significant) and Tutor students were statistically indistinguishable from control. Students in the Base arm did not perceive that they had learned less. Chapter question: *How can students who did better with the tool end up worse without it, and not notice?* Answered in Core: 7.1 (what was measured, what students did), 7.2 (why), 7.3 (why they did not notice). One line acknowledges Chapter 1's preview.

**Prediction before the evidence (7.2):** "One week before a test. Plan A: read the chapter four times. Plan B: read it once, then test yourself three times. Which plan will you remember more from after a week? Which will *feel* better?" Answered with F7.4 (Roediger & Karpicke, 2006, Experiment 2).

**Contrast boxes (term collisions), modeled on Chapter 3's "two meanings of sampling":**
- **7.2 "Retrieval" and "generation", two meanings each.** *Retrieval practice* (learning): **you** recall information from memory. *Retrieval* (Chapter 3): **the system** adds documents to the model's context. *Generation effect* (learning): **you** produce an answer, and remember it better than one you read. *Generative AI*: **the tool** produces content. The chapter's key test is phrased to fit: **"Who recalled and produced the answer: you or the tool?"**
- **7.3 Two meanings of "calibration".** *Calibration of your confidence*: how well your predicted score matches your actual score. *Calibration of a model*: how well a model's stated confidence matches its accuracy (Chapter 4 explains why it can be poor; Chapter 8 shows how it is checked). Forward pointers only.
- Glossary entries are sense-labeled: "Retrieval practice (learning)", "Generation effect (learning)", "Calibration (of your confidence)".

| # | Subsection | Tag | One new core idea | Examples | Figures |
|---|---|---|---|---|---|
| 7.1 | Practice scores are not learning | Core | **Performance** during practice is not **learning** (a lasting change you can use without the help) (Soderstrom & Bjork, 2015). What students in the Bastani experiment actually did: in the GPT Base arm most conversations asked for the answer or restated the question; tutor users shifted toward attempts and requests for help. **Overreliance** defined. (The error-carryover argument is in the Case Study.) | **Worked:** reading Bastani's Table 1 two ways: relative change (Base +48%, Tutor +127% in practice; Base 17% lower on the exam) and percentage points of the normalized grade (Base +13.7 points on a 28.4-point control mean in practice; Tutor +36.1; Base −5.4 points on a 32.1-point control mean on the exam; Tutor −0.4, not significant). **Faded:** a constructed language-app study, reader decides which result measures learning and what is missing (education). **Your Turn:** a time help raised your performance; the check that would show whether you learned | F7.2 (data), F7.3 (session storyboard), F7.9 (data: message types); reference F1.13 |
| 7.2 | Retrieval practice: the work that builds memory | Core | **Core idea: retrieval practice.** Recalling information from memory strengthens it more than restudying: in Roediger & Karpicke (2006, Exp. 2), rereading won at 5 minutes and testing won after a week, while rereaders predicted they would remember more. Umbrella: **desirable difficulties** (Bjork, 1994; Bjork & Bjork, 2011), with the caveat that a difficulty helps only if you can overcome it with effort. One paragraph on the **generation effect** (Slamecka & Graf, 1978), which feeds 7.4's test. Spacing in two sentences (Cepeda et al., 2006), practiced in 7.6's delayed check. Practice testing and distributed practice rated high utility, rereading and highlighting low (Dunlosky et al., 2013). Contrast box: two meanings of "retrieval" and "generation" | **Worked:** **Elif** turns her bilingual vocabulary notebook (intro-statistics terms) from rereading into self-testing. **Faded:** **Marcus**'s pathophysiology review plan, half converted (textbook material only, no patient data). **Your Turn:** convert one of your study habits | F7.4 (data: Roediger & Karpicke, 2006, Exp. 2), F7.5 (retrieval practice, with generation and spacing beside it) |
| 7.3 | Feeling ready is not being ready | Core | **Metacognition** (Flavell, 1979): judging your own learning; **calibration (of your confidence)**. Ease misleads: Roediger & Karpicke's rereaders predicted better recall; students in an active-learning class learned more but felt they learned less (Deslauriers et al., 2019); Bastani students did not perceive the harm, and GPT Tutor students believed they did better than they did. The fix: **predict, then check**. Contrast box: two meanings of "calibration" | **Worked:** **Marcus** predicts 3/3 on acid–base questions after a smooth AI explanation, scores 1/3 closed-book against the textbook key; what he changes. **Faded:** a partly filled calibration table (business: price elasticity). **Your Turn:** compare your Warm-up confidence ratings with your Warm-up answers | F7.6 (feeling ready vs. being ready) |
| 7.4 | Scaffold or crutch | Core | A **scaffold** supports what you cannot yet do alone and is withdrawn as you improve (Wood, Bruner & Ross, 1976); a **crutch** does the part you needed to learn and stays. The test: **who recalled and produced the answer in this turn, you or the tool?** The same AI reply is a scaffold after your attempt and a crutch with no attempt. Signature 2 from the learner's side: inside the tool's frontier it can do the task for you; outside it, only your own skill catches its errors. **Overreliance** evidence from R4, both directions and labeled as self-report from knowledge workers: higher confidence in AI went with less reported critical thinking, higher self-confidence with more (Lee et al., 2025; 319 workers, 936 examples). Chapter 1 link sentence and two-row table (§3). Chapter 5 link: the ladder's third question ("is the task meant to build your skill?") | **Worked:** a 6-turn **Elif** dialogue on standard deviation vs. standard error (intro statistics; constructed example, labeled), every turn coded S or C with a reason. Before it, Elif's peer-tutoring observation appears as an anecdote only and is followed by the evidence. **Faded:** **Marcus**'s 6-turn dialogue on acid–base balance, 3 turns coded. **Your Turn:** code a provided 5-turn dialogue (music theory: cadences) | F7.7 (**Signature 2 reused**), **F7.8 "Scaffold versus crutch"** (turn-level, book-map figure) |
| 7.5 | Setting up tutor mode | Core | What the evidence-backed designs shared (Bastani GPT Tutor; Kestin et al., 2025): hints instead of answers, accurate reference material supplied to the model, step-by-step structure. What a user can reproduce, mapped onto **Signature 6** (Ch. 5): role (a tutor who responds with questions; **Socratic questioning** defined once: teaching by asking questions that lead you to reason it out), task (help me learn X), context (my course and level, my source), constraints (attempt first; one hint at a time; no full answer unless I ask after two attempts), output format (one question per turn; ask me to explain back). **Limits:** the model can still produce the answer or an error; **answer mode** is one request away; "check my answer" relies on the model judging you, and a model can agree with a wrong attempt (**sycophancy**: agreeing with the user against the evidence; Chapter 4 explains why), so **score against your course source, not the tool's verdict**. Built-in study or learning modes exist in several tools as of October 2026 (dated sentence, at least two providers; steps in Compass) | **Worked:** **Elif**'s answer-mode request turned into a tutor-mode setup, parts labeled on Signature 6 (mirrors Tuesday's demo; constructed, labeled). **Faded:** a chemistry student's setup (limiting reagent) missing the attempt-first constraint and the source. **Your Turn (pre-lab):** your concept, source, three keyed questions, baseline answers with confidence, and your setup | F7.10 (**Signature 6 reused**, tutor-mode parts highlighted) |
| 7.6 | The tutor-mode session (Lab 7.1, A4) | Studio | A session is a small experiment on yourself: **before** (three closed-book questions with keys, baseline answers, confidence) → **during** (tutor dialogue, attempt first) → **right after** (predict, then answer closed-book; score against the key) → **later** (delayed check after ≥ 2 days: spacing) → **reflect** (calibration gap, performance in the dialogue vs. closed-book, immediate vs. delayed, one S turn, one C turn, one change). Honest low scores are valid evidence and do not lower the grade | Marcus's completed one-page record as the worked model; a partly filled annotation sheet as the faded model; the Failure Diary prompt (verification step) | F7.11 (session protocol), F7.12 (A4 annotation and calibration sheet) |
| Deep 7.A | Tutors before chatbots | Deep | One-to-one tutoring has long been studied: Bloom's (1984) "2 sigma" claim; VanLehn's (2011) review found human tutoring (d ≈ 0.79) and step-based computer tutors (d ≈ 0.76) close together, with answer-only feedback weaker; a meta-analysis of tutoring experiments (Nickow et al., 2020). Why step-level feedback matters for AI tutors | — | F7.13 (data from VanLehn, 2011) |
| Deep 7.B | Offloading on purpose | Deep | **Cognitive offloading** (Risko & Gilbert, 2016): using tools to reduce mental work is often sensible (calculators, notes). The question is whether the offloaded skill is the goal, which is the Delegation Ladder's third question (Ch. 5). Pilots and autopilot: the FAA encouraged manual flying practice so skills do not fade (FAA SAFO 13002, 2013, as cited by Bastani et al.) [VERIFY primary] | — | F7.14 (**Signature 7 reused**, `delegation_ladder`) |

Other anatomy parts:

| Part | Plan |
|---|---|
| Case Study (1 main + 2 short) | **Job: judging the strength of evidence across three studies**, not retelling the opening case. **Main (Bastani et al., 2025):** what makes it strong (classroom-level random assignment, preregistered primary outcome, intention-to-treat, independent graders, paired practice/exam problems) and the mechanism evidence, including the **error-carryover argument** (GPT Base answers were correct 51% of the time on "What is the answer?" queries; its errors lowered practice scores but did not carry over to the paired exam problems, which the authors read as students copying rather than learning from the answers); limits as the authors state them (one school, math, fall 2023, GPT-4, short-term outcomes). **Short 1 (Kestin et al., 2025, *Scientific Reports*):** Harvard introductory physics, 194 students, crossover design, two lessons, immediate post-tests; a structured AI tutor (step-by-step solutions in the prompts, problem parts sequenced by the platform) produced median learning gains more than double those of an in-class active-learning lesson, in less time (median 49 min); authors' own limits; their enthusiasm not repeated. **Short 2 (De Simone et al., 2025, World Bank working paper):** six-week program in Nigeria using Microsoft Copilot (GPT-4) for English in first-year senior secondary school; 0.31 SD on the program assessment, 0.23 SD in English [VERIFY design details and status]. **Comparison table:** design, sample, duration, unaided outcome, peer review status, what the study cannot tell you. **Failure label (case file C04):** output failure = hallucination, wrong-calculation leaf (GPT Base's logical and arithmetic errors), **documented**; overreliance is a **use** failure labeled on the failure-to-harm chain (output → no check → student relies → skill not built), not on the tree. No tree figure in Chapter 7 |
| Ethics Lens | Who gets the scaffold? Guarded tutors cost expert labor (two part-time teachers wrote the problem-specific inputs; the authors call the construction labor-intensive), while general tools default to answers. Time pressure pushes students toward the crutch (Marcus between night shifts). The closed-book check as a personal honesty practice, linked to Chapter 1's "work you do not understand" rule (the two-row table, not a new rule). Tutor transcripts contain data about you: no personal or patient data, redact identifiers before submitting (pointer to Ch. 15) |
| Career Connection | Nurse (continuing education and competency checks; Marcus), corporate learning-and-development specialist (designing AI-assisted training that tests unaided skill), software developer onboarding to a new codebase (learning on the job while an assistant writes code), airline pilot (manual-flying practice; Deep 7.B link), teacher or tutor. Descriptive only, no salary or market claims |
| From the Field | Şeker (2015), "Eşli programlama" [Pair programming], *YBS Ansiklopedi* 2(1) [VERIFY page range]: driver and navigator roles that swap at intervals; benefits the article reports, attributed to the article's sources; warning signs it lists (disengagement, "watching the master", silence). **Present-day connection, marked as the book's:** when the AI drives and you only watch, you are in the "watching the master" seat; tutor mode keeps you at the keyboard. Translated and paraphrased from Turkish; not commercial, so no D16 disclosure |
| Summary + Key Terms | Answers the session question (hedged, above); summary card F7.15; "Revisit your Warm-up" with short answers and the calibration comparison |

**Key Terms (Core), proposed:** performance (vs. learning) · learning (durable) · overreliance · retrieval practice (learning) · desirable difficulty · generation effect (learning) · spacing (spaced practice) · metacognition · calibration (of your confidence) · scaffold · crutch · tutor mode · answer mode · Socratic questioning · sycophancy (defined in one clause; Ch. 4 owns it; reuse Ch. 4's wording if the glossary has it at draft time). Deep only: cognitive offloading. Reused word for word: assistance, outsourcing, control group, random assignment, percentage point, fluent.

## 6. Example plan (worked → faded → your turn)

| Skill | Worked | Faded | Your Turn |
|---|---|---|---|
| Performance vs. learning (O1) | Bastani Table 1 in relative change and in percentage points (values in 7.1) | Constructed language-app study with practice and one-week scores; reader marks which result measures learning and what is missing (the "without the app" check) | A time help raised your performance; the check that would show learning |
| Retrieval practice (O2) | Elif's vocabulary notebook: reread plan → self-test plan with spacing (Mon/Wed/Fri) | Marcus's pathophysiology plan: two of four steps converted; reader converts the rest | Convert one of your study habits; say whether it adds retrieval, generation or spacing |
| Calibration (O5) | Marcus: prediction 3/3, closed-book 1/3 against the textbook key; what the gap tells him | Business student's calibration table (price elasticity): predictions filled, reader fills the gaps and the conclusion | Warm-up confidence vs. Warm-up answers |
| Scaffold vs. crutch (O3) | Elif's 6-turn dialogue (standard deviation vs. standard error), every turn coded S/C with a reason (constructed, labeled) | Marcus's 6-turn acid–base dialogue, 3 turns coded | Provided 5-turn music-theory dialogue (cadences): code every turn |
| Tutor-mode setup (O4) | Elif: answer-mode request → tutor-mode setup, labeled on Signature 6 | Chemistry setup (limiting reagent) missing two elements | Pre-lab: your own setup, concept, source and keyed questions |
| A4 session (O6) | Marcus's completed one-page record | Partly filled annotation sheet | Lab 7.1 and A4 |

Fields: psychology/intro statistics (Elif), health (Marcus, textbook-level content only; he never enters patient information and says so), education, business, chemistry (natural science), music (arts and humanities); engineering appears in the Career Connection and a Review B item. No cameo by the other three students. All AI dialogues are labeled "constructed example" unless they carry a real model name and date.

**New character details to log** (handoff): Elif takes an introductory statistics course for her psychology major and self-tests with her bilingual vocabulary notebook; at the peer-tutoring center where she volunteers she has noticed that giving the answer rarely helps (fictional anecdote, followed by evidence, never used as evidence). Marcus studies acid–base balance for a pathophysiology exam between night shifts, using textbook values only.

## 7. Retrieval and spacing

- **Warm-up** (three content questions, each with a 0–100% confidence rating): (1) Students who used an AI chatbot for practice scored higher during practice. Did they score higher on a closed-book exam afterward? (2) One week before a test: reread four times, or read once and test yourself three times? (3) A tool set to "tutor mode" says your answer is correct. Is that enough to count it as correct? The confidence ratings are revisited in 7.3's Your Turn and the Summary.
- **Check Yourself** after 7.1–7.6, 2–3 items each, at least one "why", all answerable from Core.
- **Spaced Review** (4 items, from the chapters read just before in reading order; checked against docs/blueprints/ch05-blueprint.md v-current, recheck against the Ch. 5 text at draft time): Chapter 5 ×2 (what makes a success criterion checkable, 5.1; which rung of the Delegation Ladder fits a task meant to build your skill, and why, 5.2); Chapter 3 ×2 (why fluent text can be false, 3.2; what retrieval changes and what it does not, 3.5). No Chapter 4 (read after Ch. 7) or Chapter 6 (Deep) items.
- **Failure Diary prompt** (brief rule): in Lab 7.1's verification step and A4 item 6: "If the tool's explanation was wrong, or it gave the answer despite your setup, save it for your Failure Diary (Chapter 4)."
- **Spaced forward:** sycophancy and model calibration → Ch. 4; verifying explanations, calibration measurement → Ch. 8; reading with AI → Ch. 9; writing and voice → Ch. 10; task–tool fit and the jagged frontier at work → Ch. 12; privacy of tutor transcripts → Ch. 15; learning in your field → Ch. 19; A4 as a portfolio piece → Ch. 20; personal code of practice → Ch. 21.
- **Built-in spacing:** A4's delayed closed-book check (≥ 2 days after Thursday's lab).

## 8. Alignment matrix

| Objective | Taught | Practiced | Figures | Assessed | Artifact |
|---|---|---|---|---|---|
| O1 | Opening Case, 7.1 | Table 1 worked/faded (relative and points); Case Study | F7.2, F7.3, F7.9 | Review A (incl. one percentage-point item); B1; Case Study Questions | A4 reflection: performance in the dialogue vs. closed-book |
| O2 | 7.2 | Study-plan sequence; L7.2 | F7.4, F7.5 | Review A (incl. one "two meanings of retrieval" item); B2 | A4 reflection: immediate vs. delayed result |
| O3 | 7.4 | Dialogue-coding sequence; Lab 7.1 share and critique | F7.7, F7.8 | Review A; B3; C1 | A4 annotation |
| O4 | 7.5 | Setup sequence; pre-lab Your Turn; L7.3 | F7.10 | Review A; B4 | A4 setup |
| O5 | 7.3, 7.6 | Calibration sequence; Lab 7.1 closed-book step | F7.6, F7.12 | Review A (incl. one "two meanings of calibration" item); B5; C2 | A4 closed-book record and calibration gap |
| O6 | 7.6 | Lab 7.1 | F7.11, F7.12 | Application Assignment (rubric below) | **A4** |

Counts follow the anatomy: Review A 13 (distractors from M1–M5b, no absolute giveaways), B 5, C 3 (should schools default AI tools to tutor mode; calibration and honesty; "AI tutors will replace teachers", using the three studies), Spaced 4, Discussion 5 (≥ 1 ethics, 1 career, 1 interdisciplinary), Case Study Questions 5 (evidence strength), optional Mini-Project (a three-week spaced self-testing log with a tutor-mode setup, feeding the portfolio, Ch. 20). Every item carries O · LO · Bloom; no item tests Deep 7.A–7.B (D20). Odd answers → handoff Appendix E block; even answers → private/ch07-answers-even.md.

## 9. Application Assignment — A4 Tutor-Mode Dialogue and Reflection

**Due:** Monday, February 15, 2027, 11:59 p.m., on eLearning. *(O6 · LO4 · Create)* Prepared before the lab (pre-lab Your Turn in 7.5, ~10 min), started in Thursday's lab (section 7.6), finished at home (~55–60 min). A4 documents how you studied; it is not a confession. Crutch turns during study help are not misconduct (see 7.4).

**What to submit:**

1. **Setup:** the concept (new to you, from your major), the course source with an answer key, and your tutor-mode setup prompt.
2. **Before:** three closed-book questions, preferably your textbook's own end-of-section or practice questions that come with keys; or, if your source has none, questions written from its headings or learning objectives only, with the key looked up in the source *after* your immediate check. Include your baseline answers (or "don't know") and a confidence rating for each.
3. **Dialogue:** the full transcript (copy or export) with tool name and date, at least 10 of your own turns. Use a university-provided tool by default (see docs/syllabus.md, Materials). No personal or confidential data; redact names and identifiers in the exported transcript. The dialogue may be in any language; give an English gloss for each turn you annotate.
4. **Annotation:** at least 6 turns coded S (scaffold: you recalled or produced the answer, or received a hint after an attempt) or C (crutch: the tool recalled or produced what you needed to), each with a one-line reason; mark any factual error you found.
5. **Closed-book record:** answers to your three questions right after the session (in lab) and again at least two days later, each preceded by a confidence prediction, and scored against the key. A teammate may check your in-lab score; self-scoring is allowed if you prefer to keep your answers private.
6. **Verification:** at least two of the tool's explanations checked against your source (not against the tool's own verdict), with any error corrected. If the tool was wrong, or gave the answer despite your setup, save it for your Failure Diary (Chapter 4).
7. **Reflection (300–400 words):** (a) how your performance during the dialogue compared with your closed-book scores; (b) how your immediate and delayed scores compared, and what retrieval or spacing has to do with it; (c) your calibration gap; (d) one S and one C turn by number; (e) one concrete change to your study practice. Null or negative results are acceptable evidence.
8. **AI Use Declaration:** tools, purpose, what you accepted, rejected or revised, how you verified it, and where your own judgment shaped the work.

**Your closed-book scores do not affect your grade.** An honest low score with a clear reflection can earn full marks. AI use during the closed-book checks is not acceptable (the checks play the role of an exam).

**Rubric (10 points)** — follows the course's artifact split (task 3, process evidence 3, verification 2, declaration and judgment 2); process evidence is scored as two separate criteria.

| Criterion (points) | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| **Task (3)** | 3: concept new and from your major; source with a key named; setup with an attempt-first constraint; three keyed questions written or chosen before the session, with baseline and confidence; dialogue of at least 10 of your turns, tool and date given | 2: all parts present, but one is weak (e.g., questions not tied to the source, or setup without an attempt-first constraint) | 1: one required part missing (setup, baseline, keyed questions or a 10-turn dialogue) | 0: two or more required parts missing |
| **Annotation (1.5)** | 1.5: at least 6 turns coded S/C, each reason accurate and specific to the turn | 1: at least 6 turns coded; one or two reasons vague or mislabeled | 0.5: 3–5 turns coded, or most reasons vague | 0: 0–2 coded turns |
| **Closed-book record (1.5)** | 1.5: immediate and delayed answers to all three questions, each with a prior prediction, scored against the key | 1: both checks present; one prediction or one score missing | 0.5: only one of the two checks | 0: no closed-book record |
| **Verification (2)** | 2: at least two explanations checked against the named source; any error corrected and explained | 1.5: two checks; correction present but thin, or source not specific | 1: one check, or checks without a named source | 0: no verification |
| **Declaration and judgment (2)** | 2: all five declaration elements; reflection covers all of (a)–(e) with specifics from your own record | 1.5: all five elements; reflection covers (a)–(e) but one or two are general | 1: two to four declaration elements, or reflection missing two or more of (a)–(e) | 0: 0–1 declaration elements |

**Alternative assignment** (for students who prefer not to use AI tools, or cannot access one). Same protocol with a human or text scaffold: run the session with a classmate or a peer tutor who follows the provided question script, or by self-explaining a worked example from your textbook (Chi et al., 1989); then annotate the **provided dated pair of transcripts** on eLearning (the same concept in answer mode and in tutor mode). Same rubric, read this way: **Task** = setup, keyed questions and your session record; **Annotation** = S/C codes on the provided transcripts (at least 6 turns); **Closed-book record** = unchanged; **Verification** = check two explanations from the provided transcripts against a source; **Declaration and judgment** = unchanged, with (a) comparing your session with the provided answer-mode transcript (the declaration states "no AI tools used" if so).

## 10. Figures (titles state the finding; each serves an objective; ≤ 9 boxes)

| ID | Title | Type | Section | Objective |
|---|---|---|---|---|
| F7.1 | Chapter 7 at a glance (AI Work Loop, Frame highlighted) | Chapter map; imports `work_loop("Frame")` from ch01_figures | Opening | all |
| F7.2 | With unrestricted GPT-4 access, practice scores rose, but exam scores were 17% lower than the control group's | **Data chart** from Bastani et al. (2025) Table 1 (data/ch07_bastani_table1.csv: arm, phase, effect, SE, control mean); bars labeled in percentage points with the relative change beside them; source line | 7.1 | O1 |
| F7.3 | Only the practice part of each session differed; the exam came right after, closed-book for everyone | Session storyboard (teacher review → assisted practice, three arms incl. "books and notes" control → closed-book exam, same 90 minutes) | 7.1, Case Study | O1 |
| F7.9 | Students with the unrestricted tool asked for answers more often than tutor users | **Data chart** from Bastani et al. (2025) text: share of first interactions that restated the question or asked for the answer (very first interaction: Base 56%, Tutor 42%; first interaction on each problem in session 1: Base 67%, Tutor 37%) (data/ch07_bastani_messages.csv) | 7.1 | O1, O3 |
| F7.4 | Rereading won after 5 minutes; testing yourself won after a week | **Data chart** from Roediger & Karpicke (2006) Exp. 2 published values (SSSS 83%/40%, SSST 78%/56%, STTT 71%/61%; predicted-recall ratings 4.8/4.2/4.0 shown as a second panel) (data/ch07_rk2006.csv) | 7.2, 7.3 | O2, O5 |
| F7.5 | Recalling from memory feels harder and lasts longer | Concept diagram: retrieval practice as the main row (what you do, how it feels, what it does), generation and spacing as two smaller rows | 7.2 | O2 |
| F7.6 | Feeling ready and being ready are different | 2 × 2 (feel ready / are ready); risk corner thick border, hatched in gray | 7.3 | O5 |
| F7.7 | Inside the tool's frontier, it can do the task for you; outside it, only your skill catches its errors | **Signature 2 reused**: `from ch01_figures import jagged`; a ch07 wrapper draws jagged(f) unchanged and adds two callouts below the plot (taller canvas); no redraw | 7.4 | O3 |
| F7.8 | **Scaffold versus crutch: the same AI reply builds skill only after your own attempt** — caption "Chapter 1's two paths, turn by turn" | Turn-level comparison, two lanes with the **same** hexagon reply in each: crutch lane = question → (no attempt) → reply → copy; scaffold lane = question → your attempt (rounded) → reply → you redo and explain (rounded); ≤ 9 boxes. New reusable function `scaffold_crutch(highlight=None)` in ch07_figures.py, `highlight` = "scaffold", "crutch" or None, for reuse in Ch. 10, 19 and 21. Does not repeat F1.13's output-level paths | 7.4 | O3 |
| F7.10 | A tutor-mode setup changes the role, the constraints and the output format | **Signature 6 reused**: `from ch05_figures import prompt_anatomy`; `prompt_anatomy(highlight=["role", "constraints", "output format"])` with tutor-mode labels in the caption and text (exact part names checked against ch05_figures.py at draft time) | 7.5 | O4 |
| F7.11 | A tutor-mode session is a small experiment on yourself | Protocol timeline (before → during → right after → later → reflect) | 7.6 | O6 |
| F7.12 | Your calibration gap is the evidence; your score is not the grade | A4 annotation and calibration sheet template | 7.6 | O5, O6 |
| F7.13 | In one review, step-based computer tutors came close to human tutors | **Data chart** from VanLehn (2011) published effect sizes (data/ch07_vanlehn2011.csv) [VERIFY answer-based and substep values] | Deep 7.A | (Deep) |
| F7.14 | When the skill is the goal, stay low on the ladder: think it through with the tool, or without it | **Signature 7 reused**: `from ch05_figures import delegation_ladder`; highlight per the Ch. 5 function's rung names (augmentation, with the "no AI" floor noted in the caption) | Deep 7.B | (Deep) |
| F7.15 | Chapter summary card | Summary card | Summary | all |

15 figures (3 signature reuses: 2, 6, 7; one new reusable function, `scaffold_crutch`) plus F1.13 referenced in 7.1 (not redrawn). Data charts in ch07_charts.py from data/ch07_*.csv with source lines. Interactive in Compass (D7 scope permitting): F7.8 step-through and a calibration self-check [COMPASS].

## 11. Labs (tool-neutral)

**Lab 7.1 Tutor-mode session** — Studio, Thursday Feb 11, in class, 75 minutes (syllabus lab flow), teams of 3–4, individual dialogues and write-ups. University-provided tools by default (docs/syllabus.md, Materials); current tool steps, memory-off and temporary-chat settings and built-in study modes in Compass.

| Minutes | Step |
|---|---|
| Before Thursday (~10, the 7.5 pre-lab Your Turn) | Concept new to you from your major; course source with a key; three closed-book questions (textbook end-of-section or practice questions with keys, or written from headings/objectives only); baseline answers and confidence; setup prompt |
| 0–10 | Briefing: the protocol (F7.11), S/C codes ("who recalled and produced the answer?"), privacy and redaction rule; check your setup against F7.10 |
| 10–35 | Tutor-mode dialogue, individually; attempt before every hint; note turn numbers where you slipped toward answers |
| 35–45 | Devices away. Predict, then answer your three questions closed-book (extended time for students with accommodations; the step can move to the end of the period) |
| 45–55 | Score against the key; optionally swap with a teammate who checks the score against the key; check one tool explanation against the source. Failure Diary prompt |
| 55–70 | Start the annotation individually (code your first 4–6 turns); each team brings one scaffold turn and one crutch turn to the class |
| 70–75 | Exit: one change you will make before the delayed check |

At home by Monday: delayed closed-book check (≥ 2 days later), finish annotation, verification, reflection, declaration (A4). **Make-up route** (absent, or no device in class): run the same protocol at home with self-scoring; same rubric.

Optional home labs: **L7.2 Reread or retrieve?** (15 min + a 2-day check: split a short reading into two halves, reread one, self-test the other, compare) and **L7.3 Answer mode versus tutor mode** (15 min; the same question both ways; record what you did in each, mirroring Tuesday's demo).

Accessibility and alternatives: no-device route (human or text scaffold, alternative assignment); dated sample transcripts on eLearning; screen-reader-friendly annotation and calibration tables; extended time for the closed-book steps; dialogue in any language with English glosses of annotated turns; no personal, confidential or patient data, identifiers redacted.

## 12. Risks and checks

- **Bastani numbers exactly as published** (verified 2026-10-18 from PMC12232635): GPT-4, custom interfaces (Base "mimics" ChatGPT; it is not ChatGPT itself); percentages relative to the control mean, percentage points of the normalized grade stated separately; Tutor's exam effect −0.004, not significant; "nearly 1,000" students; classroom-level random assignment, honors classes excluded; control practiced with books and notes; the exam was the third part of the same session. The school is named only in the acknowledgments, so the chapter uses the paper's description. Spelling: Türkiye in the book's voice; "Turkey" kept in titles and quotations.
- **PNAS correction notice resolved:** 122(34), e2518204122 (Aug 20, 2025) corrects only Osbert Bastani's affiliation; no change to findings. Handoff: refresh-list rows for Chapter 1 can be closed.
- **R3 title:** the syllabus's working-paper title ("Generative AI Can Harm Learning", 2024) differs from the PNAS title; cite the PNAS version. Table 1 is the main-results display (the paper's figures show prompts, error rates and engagement).
- **Positive cases with limits:** Kestin et al. (two lessons, immediate post-tests, solutions supplied to the model); De Simone et al. (working paper; check status and design details).
- **Learning-science claims** cited to primary sources (Roediger & Karpicke, 2006; Slamecka & Graf, 1978; Cepeda et al., 2006; Bjork, 1994; Bjork & Bjork, 2011; Flavell, 1979; Wood et al., 1976; Deslauriers et al., 2019; Soderstrom & Bjork, 2015), with Dunlosky et al. (2013) as the review. No learning-style or similar myths. Lee et al. (2025) is a self-report survey of knowledge workers: association, not effect, and not about students; it measures confidence in AI, not calibration of one's learning, so it sits in 7.4, not 7.3. Kirk-Johnson et al. (2019) dropped from Core (one source per point is enough; Further Reading).
- **Term collisions** handled by the two contrast boxes; Review A has one item on each.
- **Ch. 4 dependency:** sycophancy and model calibration defined in one clause each, pointed forward; no tree figure; C04's label lives in the case file and the Case Study text only.
- **No anthropomorphic verbs:** "the tool returns a question", "the setup instructs the model to …", "the model produces agreement", never "the tutor knows / wants / understands / thinks you are right".
- **Tool neutrality:** no product steps; the dated "study modes exist" sentence cites at least two providers and goes to the refresh list.
- **Characters:** Elif (main), Marcus (no patient data, ever); constructed dialogues labeled; the peer-tutoring observation is an anecdote, never evidence; new details logged.
- **Boundaries:** no re-teaching of the three zones (Ch. 1); prompt anatomy only as a Signature 6 reuse (Ch. 5); no Chapter 6 terms; no verification method beyond "score against your source" (Ch. 8); no writing-voice content (Ch. 10); sycophancy mechanism left to Ch. 4.
- **Conflict of interest:** Compass's planned tutor-mode assistant (D7) is not mentioned in Core; standard Compass placeholders only.
- **Dependency on Chapter 5:** F7.10 and F7.14 import `prompt_anatomy` and `delegation_ladder`; drafting waits for them (editor instruction).

## Decisions taken under delegation (D19)

| # | Decision | Reason |
|---|---|---|
| T1 | R3 is cited in its PNAS 2025 version; before Tuesday students read the Significance statement and Table 1 only (~10 min) | Peer-reviewed and open access; keeps week 4 ≤ 2 h (editor decision, D18 pattern) |
| T2 | R4 = abstract only, read and discussed in Tuesday's class | Week 4 ≤ 2 h (editor decision); the paper's finding is used in 7.4 |
| T3 | Opening Case = Bastani et al. (2025); the school is not named; Chapter 1's preview acknowledged in one line | Book map; promise kept |
| T4 | The main Case Study's job is judging evidence strength across Bastani, Kestin and De Simone | Avoids retelling the opening case (review item 20); keeps M4 refuted without overclaiming |
| T5 | Signature 2 reused by importing `jagged` unchanged and adding callouts in a ch07 wrapper, because ch01's `jagged(f)` has no `highlight` argument and other chapters' files may not be edited | Signature rule; suggest the editor add `highlight` in ch01 for Chapters 12 and 19 |
| T6 | F7.8 is turn-level (same reply after an attempt vs. with none), a new reusable function `scaffold_crutch(highlight)` | Avoids repeating F1.13 (review item 3) |
| T7 | F7.10 reuses Signature 6 (`prompt_anatomy`, list highlight) and F7.14 reuses Signature 7 (`delegation_ladder`) | Signature rule; Ch. 5 functions planned with these names (ch05 blueprint, F5.3, F5.6) |
| T8 | Work Loop highlight = Frame (output or skill?) | The chapter's central decision happens before prompting |
| T9 | A4: closed-book scores are not graded; AI use during the closed-book checks is not acceptable; dialogues may be in any language with English glosses of annotated turns; self-scoring allowed; teammate check optional | Removes the incentive to game the self-test; privacy; supports ESL students |
| T10 | A4 rubric splits process evidence into Annotation 1.5 + Closed-book record 1.5, inside the syllabus's 3/3/2/2 split; reflection descriptors carry O1 and O2 specifics; Declaration Beginning = 0–1 elements | Criteria scored separately; every matrix cell for A4 is assessed |
| T11 | Closed-book questions come from the textbook's keyed end-of-section or practice questions, or from headings/objectives with the key looked up after the immediate check | Students cannot score themselves reliably against questions an AI wrote or answered (review item 5) |
| T12 | Alternative assignment: human/peer or self-explanation scaffold plus annotation of a provided dated transcript pair | Same rubric, no AI required; matches the A2 pattern |
| T13 | From the Field = Şeker (2015) pair-programming entry, facts limited to the entry, present-day connection marked; no disclosure | Only author-written source in the inventory that fits; "watching the master" maps onto crutch use |
| T14 | Spaced Review draws on Chapters 5 and 3 only | Reading order: the chapters read just before; Ch. 4 comes after, Ch. 6 is Deep |
| T15 | Contrast boxes for "retrieval/generation" and "calibration"; sense-labeled glossary entries | Term collisions with Chapters 3, 4 and 8 (review item 2) |
| T16 | M5 split into M5a (learning guaranteed) and M5b (the tutor's verdict is correct); Elif's "cheating" worry handled by the Chapter 1 link table instead of a misconception | Keeps six misconceptions; M5b carries the sycophancy point |
| T17 | Elif's concept is from introductory statistics (standard deviation vs. standard error), not research-methods power | Fits a first-year student |
| T18 | C04 failure label: hallucination → wrong-calculation leaf, documented; overreliance on the failure-to-harm chain; no tree figure in Ch. 7 | Brief's tree-vs.-chain rule; tree labels start in Ch. 8 |
| T19 | Constructed dialogues are labeled; no real model transcript in the chapter | Style sheet §3 (two providers); dated real transcripts go to eLearning |

Book-wide decisions for the handoff `## Decisions` section: T5 (signature reuse without a highlight argument), T6 (new reusable `scaffold_crutch`), T9 (any-language dialogues with English glosses; ungraded self-test scores) and T1 (cite peer-reviewed versions of syllabus readings when they exist).

**Handoff notes for the editor:** (a) case index row C04: title "Bastani et al.: GPT-4 tutors and learning in a high school in Türkiye", primary_source_url https://doi.org/10.1073/pnas.2422633122, secondary the SSRN working paper, failure_type "hallucination (wrong calculation, documented); overreliance (use failure, chain)", outcome mixed, verified_on 2026-10-18; (b) Chapter 1 1.2 wording ("never had access", "later exam") to be fixed by the editor: the control group practiced with books and notes, and the exam was the third part of the same session; (c) close the Chapter 1 refresh-list rows on the PNAS correction; (d) optional `highlight` for ch01 `jagged`.

## Author-only items (collected for the end, not asked now)

1. Live syllabus: R3 → PNAS 2025 version, Significance statement + Table 1; R4 → abstract, discussed in class; week 4 ≈ 1.8–2.0 h.
2. Optional: a real, anonymized moment from the author's teaching where students used AI as a crutch or a scaffold, to supplement From the Field; confirm the pair-programming entry and its page range in *YBS Ansiklopedi* 2(1).
3. Course materials before Feb 11 (instructor preparation): the dated answer-mode/tutor-mode transcript pair and the peer-tutor question script on eLearning.
4. Final voice edit (pipeline step 8).

## Planned references and verification status (checked 2026-10-18)

| Reference | Status |
|---|---|
| Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. (2025). *PNAS, 122*(26), e2422633122. https://doi.org/10.1073/pnas.2422633122 | Verified, full text read (PMC12232635); correction 122(34) e2518204122 read: affiliation only |
| Lee, H.-P., Sarkar, A., Tankelevitch, L., Drosos, I., Rintel, S., Banks, R., & Wilson, N. (2025). CHI '25, Article 1121, 1–22. https://doi.org/10.1145/3706598.3713778 | Verified (Crossref; Microsoft Research abstract: 319 workers, 936 examples, both directions) |
| Roediger, H. L., III, & Karpicke, J. D. (2006). *Psychological Science, 17*(3), 249–255. https://doi.org/10.1111/j.1467-9280.2006.01693.x | Verified, full text read (Exp. 1: 120 students; Exp. 2: 180 students, values above) |
| Slamecka, N. J., & Graf, P. (1978). *JEP: Human Learning and Memory, 4*(6), 592–604. https://doi.org/10.1037/0278-7393.4.6.592 | Verified (Crossref) |
| Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). *Psychological Bulletin, 132*(3), 354–380. https://doi.org/10.1037/0033-2909.132.3.354 | Verified (Crossref) |
| Bjork, R. A. (1994). Memory and metamemory considerations in the training of human beings. In J. Metcalfe & A. Shimamura (Eds.), *Metacognition: Knowing about knowing* (pp. 185–205). MIT Press | Verified (bibliographic details; content via secondary summary) |
| Bjork, E. L., & Bjork, R. A. (2011). Making things hard on yourself, but in a good way. In M. A. Gernsbacher et al. (Eds.), *Psychology and the real world* (pp. 56–64). Worth | Verified (as cited in Bastani et al.); caveat on undesirable difficulties [VERIFY wording] |
| Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). *PSPI, 14*(1), 4–58. https://doi.org/10.1177/1529100612453266 | Verified (Crossref); utility ratings [VERIFY against the paper] |
| Flavell, J. H. (1979). *American Psychologist, 34*(10), 906–911. https://doi.org/10.1037/0003-066X.34.10.906 | Verified (Crossref) |
| Deslauriers, L., McCarty, L. S., Miller, K., Callaghan, K., & Kestin, G. (2019). *PNAS, 116*(39), 19251–19257. https://doi.org/10.1073/pnas.1821936116 | Verified (Crossref); sample and wording [VERIFY] |
| Soderstrom, N. C., & Bjork, R. A. (2015). *Perspectives on Psychological Science, 10*(2), 176–199. https://doi.org/10.1177/1745691615569000 | Verified (Crossref) |
| Wood, D., Bruner, J. S., & Ross, G. (1976). *Journal of Child Psychology and Psychiatry, 17*(2), 89–100. https://doi.org/10.1111/j.1469-7610.1976.tb00381.x | Verified (Crossref) |
| Chi, M. T. H., Bassok, M., Lewis, M. W., Reimann, P., & Glaser, R. (1989). *Cognitive Science, 13*(2), 145–182. https://doi.org/10.1207/s15516709cog1302_1 | Verified (Crossref) |
| Kestin, G., Miller, K., Klales, A., Milbourne, T., & Ponti, G. (2025). *Scientific Reports, 15*, 17458. https://doi.org/10.1038/s41598-025-97652-6 | Verified, full text read (PMC12179260) |
| De Simone, M., Tiberti, F., Barron Rodriguez, M., Manolio, F., Mosuro, W., & Dikoru, E. J. (2025). *From chalkboards to chatbots* (Policy Research Working Paper 11125). World Bank | Verified (abstract read); design details and status [VERIFY] |
| VanLehn, K. (2011). *Educational Psychologist, 46*(4), 197–221. https://doi.org/10.1080/00461520.2011.611369 | Verified (Crossref; 0.79 and 0.76 confirmed); answer-based and substep values [VERIFY] |
| Bloom, B. S. (1984). *Educational Researcher, 13*(6), 4–16. https://doi.org/10.3102/0013189X013006004 | Verified (Crossref) |
| Nickow, A., Oreopoulos, P., & Quan, V. (2020). NBER Working Paper 27476. https://doi.org/10.3386/w27476 | Verified (Crossref); pooled effect size [VERIFY] |
| Risko, E. F., & Gilbert, S. J. (2016). *Trends in Cognitive Sciences, 20*(9), 676–688. https://doi.org/10.1016/j.tics.2016.07.002 | Verified (Crossref) |
| Kirk-Johnson, A., Galla, B. M., & Fraundorf, S. H. (2019). *Cognitive Psychology, 115*, 101237. https://doi.org/10.1016/j.cogpsych.2019.101237 | Verified (Crossref); Further Reading only |
| Federal Aviation Administration. (2013). *Manual flight operations* (SAFO 13002) | Cited via Bastani et al.; [VERIFY primary] |
| Study/learning modes: OpenAI (July 29, 2025), Google Gemini Guided Learning (Aug 6, 2025; TechCrunch verified), Anthropic Claude learning mode (Aug 2025) | Secondary sources verified; [VERIFY primary announcement pages]; refresh list |
| Şeker, Ş. E. (2015). Eşli programlama [Pair programming]. *YBS Ansiklopedi, 2*(1) | Read in full (Drive 1cJo2MG8E97EM4MqzyIaDMUh0GB9x58Ed → build/ch07/fromthefield-esli-programlama.md); [VERIFY page range] |

## Review changes (v0.1 → v0.2)

Must-fix: week 4 brought to ~1.8–2.0 h (R3 = Significance + Table 1; R4 = abstract in class; Core + Studio ≤ 4,200 words; 7.4 dialogues cut to 5–6 turns; Your Turn time and A4 home time counted; annotation started in lab; reading order per day stated, Ch. 7 before Thursday as in the syllabus); contrast boxes for "retrieval/generation" (you vs. the system or tool) and "calibration" (your confidence vs. a model's), key test rephrased as "who recalled and produced the answer: you or the tool?", sense-labeled glossary entries; F7.8 made turn-level (same reply after an attempt vs. with none) with a reusable `scaffold_crutch(highlight)` and the caption "Chapter 1's two paths, turn by turn"; Chapter 1 link as one sentence plus a two-row table, A4 framed as documenting study habits, not misconduct; closed-book questions from keyed textbook questions (or headings/objectives with the key looked up afterward), scoring against the key, self-scoring allowed.
Should-fix: 7.1 worked example in relative change and percentage points, with a Review A item; control group and exam timing described exactly (Chapter 1 fix passed to the editor); F7.9 moved to 7.1 and the error-carryover argument to the Case Study; R4 moved to 7.4 (overreliance, both directions, self-report, knowledge workers); 7.2 centered on retrieval practice, generation one paragraph, spacing brief and practiced in the delayed check; F7.10 reuses Signature 6 with a list highlight and F7.14 reuses Signature 7; Spaced Review checked against the Chapter 5 blueprint and drawn from Chapters 5 and 3; 7.5 adds the sycophancy limit of "check my answer" (score against your source; forward pointer to Ch. 4); rubric reflection descriptors carry O1/O2 specifics, Declaration Beginning = 0–1 elements, teammate check optional; C04 failure label per the tree-vs.-chain rule, no tree figure, handoff index row; figure titles reworded (F7.2, F7.7, F7.9); session answer hedged as requested.
Consider (all applied): 4D:DEL dropped from O1 and 4D:DIL from O5; M5 split into M5a/M5b; Warm-up = three content questions with confidence ratings; lab make-up route with self-scoring, extended time, university-provided tools by default, redaction of exported transcripts, "Socratic questioning" defined once; Elif moved to an intro-statistics concept, her peer-tutoring observation used as anecdote only; the main Case Study given the job of judging evidence strength across three studies.
Brief rules applied: reading order (no Ch. 4 dependency; sycophancy and model calibration defined in one clause and pointed forward), tree vs. chain (C04), Failure Diary prompt (Lab 7.1 verification step and A4 item 6), Ch. 5/6 boundary (no Ch. 6 terms; prompt anatomy only as Signature 6), D20 (no assessment items on Deep 7.A–7.B).

## Draft notes (v1, 2026-10-18)

- Nigeria design verified from the authors' World Bank blog (January 9, 2025): six-week after-school program, June–July 2024, with teacher support, random assignment; gains also on end-of-year exams. Number of schools and students still [VERIFY].
- VanLehn (2011) values verified from the article's table: answer-based 0.31 (165 comparisons), substep-based 0.40 (26), step-based 0.76 (28), human 0.79 (10). Nickow et al. (2020): pooled 0.37 SD; stronger for teacher and paraprofessional tutors (NBER abstract). Deslauriers et al. (2019): 149 students, Harvard introductory physics, crossover, two class meetings in week 12. Bjork & Bjork (2011) caveat verified from the chapter PDF.
- Study modes cited to Malik (2025, TechCrunch), which dates Google's Guided Learning (Aug 6, 2025) and OpenAI's Study Mode (about a week earlier); Anthropic's learning mode not mentioned (no primary source read).
- Kirk-Johnson et al. (2019) moved to Further Reading (one source per point in 7.3).
- F7.1's Work Loop strip highlights Frame and Verify; no separate `work_loop` figure (D-7.f in the handoff).

## Revision v2 (2026-10-18)

Four independent reviews applied with the editor's decisions E1–E9; details and skips in docs/editorial/ch07-dev-memo.md. Changes against this blueprint:
- 7.2 adds a pretesting caveat (Kornell, Hays & Bjork, 2009).
- 7.3 defines one prediction format (summed confidence → predicted score; calibration gap = predicted − actual).
- 7.4 adds coding rules, and its Your Turn is now a self-contained business item (break-even) in place of music.
- A4: check questions stay out of the dialogue; the delayed check uses parallel keyed questions; reflection is 200–300 words; the rubric now has six criteria (Reflection 1.5 + Declaration 0.5).
- The Case Study is read in Tuesday's class, and its job is judging evidence strength across the three studies.
- Nickow et al. is cited in the AERJ 2024 version (about 0.29 SD).
- The Nigeria caveats are added.
- Week 4 comes to about 2.2 h.
