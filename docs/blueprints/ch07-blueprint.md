# Chapter 7 blueprint — Learning with AI: Tutor, Not Answer Machine

Status: v0.1 (2026-10-18), written under delegation (D19); awaiting the editor's independent blueprint review (v0.2). No chapter text is written until v0.2 is applied.
Part II — Working with AI · Syllabus week 4 · Path: Core (examinable; midterm covers Ch. 1–10) · Featured students: **Elif** (main) and **Marcus** (second), per docs/characters.md · Work Loop step highlighted in the Chapter Map: **Frame** (is the goal here the output or the skill?), with Verify second (a closed-book check verifies your learning, not the tool's answer).

**Source material.** Syllabus week 4: Tue Feb 9 concept session "Tutor or answer machine; the evidence" (R3, R4; demo: answer mode versus Socratic mode) and Thu Feb 11 tutor-mode lab (a new concept from your major plus three closed-book questions) → **A4 tutor-mode dialogue and reflection**, due Mon Feb 15. No Haliç lecture covers this chapter (docs/context/halic/ holds Lectures 2–3 only); it is built from the cited research below. Opening case C04, Bastani et al. (2025), read in full from the PNAS open-access text (PMC12232635) on 2026-10-18. From the Field: the author's 2015 encyclopedia entry on pair programming (read via Drive and tools/drive2md.py; see §11).

## 1. Outcome link and week 4

| Item | Value |
|---|---|
| Syllabus outcome | **LO4** (distinguish responsible assistance from overreliance, undisclosed outsourcing and academic misconduct); LO3 in a supporting role (checking the tool's explanations against a source) |
| Studio artifact | **A4 — tutor-mode dialogue and reflection**, due Monday, February 15, 2027, 11:59 p.m. Hosted in this chapter (section 7.6 and the Application Assignment), with its own 10-point rubric and an alternative assignment |
| In-class time | Tue Feb 9: 10-minute opening case (Bastani et al., 2025), concept core, demo "answer mode versus Socratic mode" (the book's 7.5 worked example mirrors it), ungraded concept check. Thu Feb 11: Lab 7.1 "Tutor-mode session" (section 7.6) |
| Readings | **R3** Bastani et al. (2025), PNAS version (open access), sections Significance, introduction, Main Results and "Potential Mechanism" (~20 min). The syllabus lists the 2024 working paper; the book cites the peer-reviewed version (decision T1). **R4** Lee et al. (2025), CHI '25: abstract, introduction and the summary of findings only (~10–15 min; decision T2) |

### Week 4 workload (out of class)

| Item | Time |
|---|---|
| Chapter 7 Core + Studio reading (≤ 4,900 words incl. examples) | 30–35 min (longer for ESL readers) |
| R3 selected sections | ~20 min |
| R4 selected sections | ~10–15 min |
| Pre-lab task (choose a concept and a course source, write three closed-book questions and baseline answers with confidence) | ~10 min |
| A4 at home (delayed closed-book check, annotation, reflection, declaration) | 45–55 min |
| **Total** | **~2.0–2.3 h** (syllabus: 1–2 h; see decision T2 and Author-only item 1) |
| Optional: labs L7.2–L7.3, Deep 7.A–7.B | 45–60 min |

**Word budget.** Week 4 carries one chapter, so Core subsections run ~700–900 words (below the anatomy's 1,500–2,500, as in Chapters 2–3) to keep the week near two hours. The chapter reaches ≥ 10,000 words with the Opening Case, Deep sections, Case Study, Ethics Lens, Career Connection, From the Field and the End-of-Chapter Package (estimate ~12,000).

## 2. Chapter objectives (6)

| # | Objective — after this chapter you will be able to… | Bloom | LO | Framework tags |
|---|---|---|---|---|
| O1 | **Explain** why performance while using AI can overstate learning, using the design, measures and limits of the Bastani et al. (2025) experiment | Understand | LO4 | UNESCO:HCM-U · 4D:DEL |
| O2 | **Explain** how retrieval practice, generation and spacing build lasting learning, and why they feel less effective than rereading or receiving answers | Understand | LO4 | UNESCO:HCM-U |
| O3 | **Distinguish** scaffolding from crutch use in an AI dialogue, turn by turn, and justify each label | Analyze | LO4 | 4D:DEL · 4D:DISC |
| O4 | **Set up** a tutor-mode session for a new concept: a setup prompt, an attempt-first rule, a course source to check against and closed-book questions | Apply | LO4, LO2 | 4D:DESC · 4D:DEL |
| O5 | **Judge** how much you learned from a session by comparing predicted and actual closed-book performance, and decide what to change in your study practice | Evaluate | LO4 | 4D:DIL · UNESCO:HCM-A |
| O6 | **Produce** A4: a tutor-mode dialogue with annotations, an immediate and a delayed closed-book check, verification, a reflection and an AI Use Declaration | Create | LO4 | 4D:DIL · UNESCO:ETH-A |

UNESCO codes follow the ai4all-frameworks table (HCM = human-centred mindset, ETH = ethics of AI). At most three tags per objective.

## 3. Prerequisites and promises kept

From Chapter 1: assistance vs. outsourcing (glossary wording reused verbatim), the three-zone policy, the AI Use Declaration, the test "if you cannot explain, defend or redo the work without the tool, you outsourced it", control group, random assignment, percentage point, the Jagged Frontier Map (F1.7), F1.13 "Working faster is not the same as learning", and the two-sentence preview of Bastani et al. in 1.2. From Chapter 3: fluent text can be false (3.2); a model's output comes from scores over tokens, not a stored answer. From Chapter 5 (week 3): framing a task and iterating prompts (the Ch. 5 text is not written yet; Ch. 7 refers to it only at book-map level and the drafter checks the wording against Ch. 5 before finalizing).

**Promise kept:** Chapter 1 said "You will study this in Chapter 7." Chapter 7 gives the full design, the exact numbers, the mechanism, what students believed, and the limits. **Refinement, not contradiction:** Chapter 1 says the hint-giving version "largely avoided that harm"; Chapter 7 adds that it did not raise exam scores above the control group.

**Not repeated:** Chapter 7 does not re-teach the three zones or the assistance/outsourcing definitions; it operationalizes Chapter 1's "can you redo it without the tool?" test as a closed-book check. Writing and voice belong to Chapter 10 (A4's reflection is graded for content and judgment, not prose style); prompt anatomy belongs to Chapter 5; verification method belongs to Chapter 8.

## 4. Misconceptions (refutation pattern; six)

| # | Misconception | Where confronted |
|---|---|---|
| M1 | "If I scored well while using AI, I learned it." | Opening Case, 7.1 (practice +48% vs. exam −17%) |
| M2 | "If studying feels easy and smooth, it is working; struggle means I am doing it wrong." | 7.2 (desirable difficulties; with the caveat that not every difficulty helps) |
| M3 | "I can tell how well I have learned something." | 7.3 (calibration; Roediger & Karpicke's prediction data; Bastani students' perceptions) |
| M4 | "AI help is either always good for learning or always bad for it." | 7.4, Case Study (same model family, different designs and uses, different results) |
| M5 | "Once a tool is in tutor mode, my learning is taken care of and its explanations are correct." | 7.5 (GPT Tutor matched, but did not beat, the control on the exam; its accuracy came from teacher-supplied solutions; tutor mode is one request away from answer mode) |
| M6 | "Using AI to study is cheating." (Elif's starting worry) | 7.4, briefly, with a pointer to Chapter 1: study help is permitted; the question this chapter asks is whether it builds the skill |

Refutation check for the drafter: M4's refutation must not create "design is all that matters"; the text says the evidence comes from a few studies, subjects and dates.

## 5. Concept sequence

**Session question, answered in the Summary:** *Can a chatbot help you learn, or only help you finish?* Answer (hedged): both have been observed. In one school, one subject and fall 2023, unrestricted answer access raised practice scores and lowered unaided exam scores, while a design that withheld answers and gave hints avoided the harm (Bastani et al., 2025). Structured tutors that kept students doing the work produced gains in two other studies (Kestin et al., 2025; De Simone et al., 2025). Across these studies, what differed was who did the retrieving and generating (this book's reading of the evidence), and that is partly under your control.

**Opening Case (450–600 words): the high-school experiment in Türkiye.** Stated as a research finding with model and date in the first paragraph. Fall 2023–24, a large high school in Türkiye (the paper's description; the school is not named in the text), nearly 1,000 students in about fifty 9th–11th-grade classes; classrooms randomly assigned to three arms; four 90-minute review sessions covering about 15% of the semester's math. Each session: teacher review → assisted practice (the only part that differed) → closed-book, closed-laptop exam with problems paired to the practice problems; both parts counted toward grades. Arms: **GPT Base** (a GPT-4 chat interface built to mimic ChatGPT), **GPT Tutor** (same model and interface; prompt with teacher-written solutions, common mistakes, and an instruction to give hints, not answers), control (books and notes). Results: practice +48% (Base) and +127% (Tutor) relative to control; exam −17% for Base (statistically significant); Tutor indistinguishable from control. Students in the Base arm did not perceive that they learned less. Puzzle for the chapter: *How can students who did better with the tool end up worse without it, and not notice?* The explanation sits in Core (7.1 mechanism, 7.2 why, 7.3 why they did not notice). Chapter 1's two sentences are acknowledged in one line ("Chapter 1 gave you the headline; here is the experiment").

**Prediction before the evidence (7.2):** "You have one week before a test. Plan A: read the chapter four times. Plan B: read it once, then test yourself three times. Which plan will you remember more from after a week? Which one will *feel* better?" Answered with F7.4 (Roediger & Karpicke, 2006, Experiment 2).

| # | Subsection | Tag | One new core idea | Examples | Figures |
|---|---|---|---|---|---|
| 7.1 | Practice scores are not learning | Core | **Performance** during practice is not **learning** (a lasting change you can use without the help) (Soderstrom & Bjork, 2015). Bastani's mechanism: in the GPT Base arm most conversations asked for answers; errors in GPT Base answers (correct only 51% of the time on "What is the answer?" queries) lowered practice scores but did not carry over to the exam, which the authors read as students copying rather than learning. Overreliance defined | Worked: reading Bastani's Table 1 (what each number measured). Faded: a constructed language-app study, reader decides which result measures learning (education) | F7.2 (data), F7.3 (session storyboard); reference F1.13 |
| 7.2 | The work that builds memory | Core | Learning comes from effortful work you do yourself: **retrieval practice** (Roediger & Karpicke, 2006), the **generation effect** (Slamecka & Graf, 1978) and **spacing** (Cepeda et al., 2006), under the umbrella of **desirable difficulties** (Bjork, 1994; Bjork & Bjork, 2011); practice testing and distributed practice rated high utility, rereading and highlighting low (Dunlosky et al., 2013). Caveat: a difficulty helps only if you can overcome it with effort (Bjork & Bjork, 2011) | Worked: **Elif** turns her bilingual vocabulary notebook from rereading into self-testing (psychology terms). Faded: **Marcus**'s pharmacology review plan, partly converted (health; textbook material, no patient data). Your Turn: convert one of your own study habits | F7.4 (data: Roediger & Karpicke, 2006, Exp. 2), F7.5 (retrieve, generate, space) |
| 7.3 | Feeling ready is not being ready | Core | **Metacognition** (Flavell, 1979): judging your own learning; **calibration** = how well your confidence matches your results. Ease and fluency mislead: restudiers predicted better recall (Roediger & Karpicke, 2006); students in an active-learning class learned more but felt they learned less (Deslauriers et al., 2019); effort is misread as poor learning (Kirk-Johnson et al., 2019); Bastani students did not perceive the harm. R4: knowledge workers who reported more confidence in AI also reported less critical thinking (self-report survey, 319 workers, 936 examples; Lee et al., 2025). The fix: **predict, then check** | Worked: **Marcus** predicts 3/3 on acid–base questions after a smooth AI explanation, scores 1/3 closed-book; what he changes. Faded: a partly filled calibration table (business: price elasticity). Your Turn: the Warm-up calibration | F7.6 (feeling ready vs. being ready 2 × 2) |
| 7.4 | Scaffold or crutch | Core | A **scaffold** supports what you cannot yet do alone and is removed as you improve (Wood, Bruner & Ross, 1976); a **crutch** does the part you needed to learn and stays. Test: *who did the retrieving and generating in this turn?* The same AI reply can be either, depending on whether you attempted first. Signature 2 seen from the learner's side: inside the tool's frontier it can do the task for you (highest crutch risk); outside it the tool may be wrong and only your own skill catches the error. Links Chapter 1's assistance/outsourcing in one sentence, without repeating it (M6 here) | Worked: an annotated 8-turn **Elif** dialogue on statistical power (constructed example, labeled), each turn coded S or C. Faded: **Marcus**'s dialogue on acid–base balance, half coded. Your Turn: code a provided dialogue (music theory: cadences) | F7.7 (**Signature 2 reused**), **F7.8 "Scaffold versus crutch"** (book-map figure), F7.9 (data: Bastani message types) |
| 7.5 | Setting up tutor mode | Core | What the evidence-backed designs shared (Bastani GPT Tutor; Kestin et al., 2025): hints instead of answers, accurate reference material supplied to the model, step-by-step structure, attempt first, check and explain back. What a user can reproduce: a **tutor-mode** setup (questions and hints, wait for my attempt, do not reveal the answer unless I ask after two attempts, check my answer against my source, ask me to explain back). Limits: the model can still produce the answer or an error; **answer mode** is one request away; keep the course source open. Built-in study or learning modes exist in several tools as of October 2026 (dated sentence; steps in Compass). Framing method → Ch. 5; verification method → Ch. 8 | Worked: **Elif**'s answer-mode request turned into a tutor-mode setup (mirrors Tuesday's demo; constructed, labeled). Faded: a chemistry student's setup (limiting reagent) with two elements missing. Your Turn: write a setup for a concept in your major (used in Lab 7.1) | F7.10 (what a tutor-mode setup asks for) |
| 7.6 | The tutor-mode session (Lab 7.1, A4) | Studio | A session is a small experiment on yourself: **before** (three closed-book questions from a course source, baseline answers, confidence) → **during** (tutor dialogue, attempt first) → **right after** (closed-book answers, prediction first) → **later** (delayed check after ≥ 2 days, spacing) → **reflect** (calibration gap, one scaffold turn, one crutch turn, one change). Honest low scores are valid evidence and do not lower the grade | Students' own sessions in Thursday's lab; Marcus's completed calibration record as the worked model; a partly filled annotation sheet as the faded model | F7.11 (session protocol), F7.12 (A4 annotation and calibration sheet) |
| Deep 7.A | Tutors before chatbots | Deep | One-to-one tutoring has long been studied: Bloom's (1984) "2 sigma" claim; VanLehn's (2011) review found human tutoring (d ≈ 0.79) and step-based computer tutors (d ≈ 0.76) close together, and answer-only feedback weaker; a meta-analysis of tutoring experiments (Nickow et al., 2020). Why step-level feedback matters for AI tutors | — | F7.13 (data from VanLehn, 2011) |
| Deep 7.B | Offloading on purpose | Deep | **Cognitive offloading** (Risko & Gilbert, 2016): using tools to reduce mental work is often sensible (calculators, notes). The question is whether the offloaded skill is the goal. Pilots and autopilot: the FAA encouraged manual flying practice so skills do not fade (FAA SAFO 13002, 2013, as cited by Bastani et al.) [VERIFY primary] | — | F7.14 (decision: is the skill the goal?) |

Other anatomy parts:

| Part | Plan |
|---|---|
| Case Study (1 main + 2 short) | **Main:** Bastani et al. (2025) traced through F7.8: design, what was measured, mechanism, what students believed, how strong the evidence is (classroom-level random assignment, preregistered primary outcome, intention-to-treat, independent graders) and its limits as the authors state them (one school, math, fall 2023, GPT-4, short-term outcomes). **Short 1 (positive):** Kestin et al. (2025), *Scientific Reports*: Harvard introductory physics, 194 students, crossover design, two lessons; a structured AI tutor (step-by-step solutions in the prompts, sequenced problem parts) produced median learning gains more than double those of an in-class active-learning lesson, in less time (median 49 min); limits stated by the authors. **Short 2 (positive, working paper):** De Simone et al. (2025), World Bank: six-week program in Nigeria using Microsoft Copilot (GPT-4) for English learning in first-year senior secondary school; 0.31 SD on the program assessment, 0.23 SD in English [VERIFY design details: after-school sessions guided by teachers; sample size; publication status as of Oct 2026]. Comparison table: tool, who designed the interaction, what students did, unaided outcome |
| Ethics Lens | Who gets the scaffold? Guarded tutors cost expert labor (Bastani: two part-time teachers wrote the problem-specific inputs; "labor-intensive" in the authors' word), while free tools default to answers. Time pressure pushes students toward the crutch (Marcus between night shifts). Honesty with yourself: the closed-book check as a personal integrity practice, linked to Chapter 1's "work you do not understand" rule. Tutor transcripts contain data about you; no personal or patient data in prompts (pointer to Ch. 15) |
| Career Connection | Nurse (continuing education and competency checks; Marcus), corporate learning-and-development specialist (designing AI-assisted training that tests unaided skill), software developer onboarding to a new codebase (learning on the job while an assistant writes code), airline pilot (manual-flying practice; Deep 7.B link), teacher or tutor. Descriptive only, no salary or market claims |
| From the Field | Şeker (2015), "Eşli programlama" [Pair programming], *YBS Ansiklopedi* 2(1) [VERIFY page range]: driver and navigator roles that swap at intervals; benefits the article reports (with the article's sources); warning signs it lists (disengagement, "watching the master", silence). **Present-day connection, marked as such:** when the AI drives and you only watch, you are in the "watching the master" seat; tutor mode keeps you at the keyboard. No commercial interest, so no D16 disclosure |
| Summary + Key Terms | Answers the session question (hedged, above); summary card F7.15; "Revisit your Warm-up" with short answers |

## 6. Example plan (worked → faded → your turn)

| Skill | Worked | Faded | Your Turn |
|---|---|---|---|
| Performance vs. learning (O1) | Bastani Table 1: practice +0.137 / +0.361 vs. exam −0.054 / −0.004 (normalized grades; control means 0.284 and 0.321); what each measured and why the exam is the learning measure | Constructed language-app study with practice and one-week scores; reader marks which result measures learning and what is missing (the "without the app" condition) | Describe a time help raised your performance; design the check that would show whether you learned |
| Desirable difficulties (O2) | Elif's vocabulary notebook: reread plan → self-test plan with spacing (Mon/Wed/Fri) | Marcus's pharmacology plan: two of four steps converted, reader converts the rest | Convert one of your study habits; say which of retrieve, generate or space it adds |
| Calibration (O5) | Marcus: prediction 3/3, closed-book 1/3, what the gap tells him and what he changes | Business student's calibration table (price elasticity), predictions filled, reader fills the gaps and the conclusion | Warm-up revisited: compare your Warm-up confidence with the Check Yourself results |
| Scaffold vs. crutch (O3) | Elif's 8-turn dialogue on statistical power, every turn coded S/C with a reason (constructed, labeled) | Marcus's acid–base dialogue, 4 of 8 turns coded | Provided music-theory dialogue (cadences): code every turn |
| Tutor-mode setup (O4) | Elif: answer-mode request → tutor-mode setup with all five elements | Chemistry student's setup (limiting reagent) missing the attempt-first rule and the source | Your own setup for a concept in your major (Lab 7.1) |
| A4 session (O6) | Marcus's completed calibration and annotation record (one page) | Partly filled A4 annotation sheet | Lab 7.1 and A4 |

Fields: psychology (Elif), health (Marcus, textbook-level content only; he never enters patient information and says so), education, business, chemistry (natural science), music (arts and humanities); engineering appears in the Career Connection and a Review B item. No cameo by the other three students. All AI dialogues are labeled "constructed example" unless they carry a real model name and date.

**New character details to log** (handoff): Elif takes a research-methods course and is learning statistical power; she self-tests with her bilingual vocabulary notebook; at the peer-tutoring center she volunteers at, she has seen that giving the answer rarely helps (fictional, not a factual claim). Marcus studies acid–base balance for a pathophysiology exam between night shifts; he uses textbook values only.

## 7. Retrieval and spacing

- **Warm-up** (three items, with a confidence rating each): (1) If you score well on homework done with AI help, will you score as well on a closed-book exam? (2) One week before a test: reread four times, or read once and test yourself three times? (3) How sure are you of your answers to 1 and 2 (0–100%)? The third item seeds 7.3's calibration.
- **Check Yourself** after 7.1–7.6, 2–3 items each, at least one "why", all answerable from Core.
- **Spaced Review** (4 items): Chapter 5 ×2 (framing a task; why iterate) [checked against the Ch. 5 text at draft time], Chapter 3 ×1 (fluent text can be false, and why), Chapter 1 ×1 (the "redo it without the tool" test). Chapter 4 is read in week 5 and Chapter 6 is Deep, so neither is used.
- **Spaced forward:** prompt anatomy → Ch. 5; verifying explanations → Ch. 8; reading with AI and source fidelity → Ch. 9; writing and voice → Ch. 10; task–tool fit and the jagged frontier at work → Ch. 12; privacy of tutor transcripts → Ch. 15; learning in your field → Ch. 19; A4 as a portfolio piece → Ch. 20; personal code of practice → Ch. 21.
- **Built-in spacing:** A4's delayed closed-book check (≥ 2 days after Thursday's lab) is itself spaced retrieval.

## 8. Alignment matrix

| Objective | Taught | Practiced | Figures | Assessed | Artifact |
|---|---|---|---|---|---|
| O1 | Opening Case, 7.1 | Table 1 worked/faded; Case Study | F7.2, F7.3 | Review A; B1; Case Study Questions | A4 reflection (performance vs. learning) |
| O2 | 7.2 | Study-plan sequence; L7.2 | F7.4, F7.5 | Review A; B2 | A4 delayed check |
| O3 | 7.4 | Dialogue-coding sequence; Lab 7.1 share and critique | F7.7, F7.8, F7.9 | Review A; B3; C1 | A4 annotation |
| O4 | 7.5 | Setup sequence; Lab 7.1; L7.3 | F7.10 | Review A; B4 | A4 setup prompt |
| O5 | 7.3, 7.6 | Calibration sequence; Lab 7.1 closed-book step | F7.6, F7.12 | B5; C2 | A4 calibration record |
| O6 | 7.6 | Lab 7.1 | F7.11, F7.12 | Application Assignment (rubric below) | **A4** |

Counts follow the anatomy: Review A 12 (distractors from M1–M6, no absolute giveaways), B 5, C 3 (one on whether schools should default AI tools to tutor mode, one on calibration and honesty, one taking a position on "AI tutors will replace teachers" using the three studies), Spaced 4, Discussion 5 (≥ 1 ethics, 1 career, 1 interdisciplinary), Case Study Questions 5, optional Mini-Project (a three-week spaced self-testing log with an AI tutor, feeding the portfolio, Ch. 20). Every item carries O · LO · Bloom. Odd answers → handoff Appendix E block; even answers → private/ch07-answers-even.md.

## 9. Application Assignment — A4 Tutor-Mode Dialogue and Reflection

**Due:** Monday, February 15, 2027, 11:59 p.m., on eLearning. *(O6 · LO4 · Create)* Started in Thursday's lab (section 7.6); expect about 10 minutes before the lab and 45–55 minutes after it.

**What to submit:**

1. **Setup:** the concept (new to you, from your major), the course source you will check against (textbook section, lecture notes or an assigned reading), and your tutor-mode setup prompt.
2. **Before:** three closed-book questions written from the source before the session (at least one "why" or "how" question and one application question), your baseline answers (or "don't know") and a confidence rating for each.
3. **Dialogue:** the full transcript (copy or export), at least 10 of your own turns, with tool name and date. No personal or confidential data. The dialogue may be in any language; give an English gloss for each turn you annotate.
4. **Annotation:** at least 6 turns coded S (scaffold: you retrieved, generated or explained, or received a hint after an attempt) or C (crutch: the tool did thinking you needed to do), each with a one-line reason; mark any factual error you found.
5. **Closed-book record:** answers to your three questions right after the session (in lab) and again at least two days later, each preceded by a confidence prediction, and scored against your source (the in-lab score checked by a teammate).
6. **Verification:** at least two of the tool's explanations checked against your source, with any error corrected.
7. **Reflection (300–400 words):** your calibration gap; one scaffold and one crutch turn by turn number; what you will change; whether this session helped more or less than your usual way of studying. Null or negative results are acceptable evidence.
8. **AI Use Declaration:** tools, purpose, what you accepted, rejected or revised, how you verified it, and where your own judgment shaped the work.

**Your closed-book scores do not affect your grade.** An honest low score with a clear reflection can earn full marks. AI use during the closed-book checks is not acceptable (the checks play the role of an exam).

**Rubric (10 points)** — follows the course's artifact split (task 3, process evidence 3, verification 2, declaration and judgment 2); process evidence is scored as two separate criteria.

| Criterion (points) | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| **Task (3)** | 3: concept new and from your major; named source; setup prompt with attempt-first rule; three pre-written questions with baseline and confidence; dialogue of at least 10 of your turns, tool and date given | 2: all parts present, but one is weak (e.g., questions not tied to the source, or setup without an attempt-first rule) | 1: one required part missing (setup, baseline or a 10-turn dialogue) | 0: two or more required parts missing |
| **Annotation (1.5)** | 1.5: at least 6 turns coded S/C, each reason accurate and specific to the turn | 1: at least 6 turns coded; one or two reasons vague or mislabeled | 0.5: 3–5 turns coded, or most reasons vague | 0: fewer than 3 coded turns |
| **Closed-book record (1.5)** | 1.5: immediate and delayed answers to all three questions, each with a prior prediction, scored against the source | 1: both checks present; one prediction or one score missing | 0.5: only one of the two checks | 0: no closed-book record |
| **Verification (2)** | 2: at least two explanations checked against the named source; any error corrected and explained | 1.5: two checks; correction present but thin, or source not specific | 1: one check, or checks without a named source | 0: no verification |
| **Declaration and judgment (2)** | 2: all five declaration elements; reflection names the calibration gap, one S and one C turn by number, and one concrete change | 1.5: all five elements; reflection general or missing one of the three specifics | 1: two to four elements, or reflection missing two specifics | 0: missing |

**Alternative assignment** (for students who prefer not to use AI tools, or cannot access one). Same protocol with a human or text scaffold: run the session with a classmate or a peer tutor who follows the provided question script, or by self-explaining a worked example from your textbook (Chi et al., 1989); then annotate the **provided dated pair of transcripts** on eLearning (the same concept in answer mode and in tutor mode). Same rubric, read this way: **Task** = setup, questions and your session record; **Annotation** = S/C codes on the provided transcripts (at least 6 turns); **Closed-book record** = unchanged; **Verification** = check two explanations from the provided transcripts against a source; **Declaration and judgment** = unchanged (the declaration states "no AI tools used" if so).

## 10. Figures (titles state the finding; each serves an objective; ≤ 9 boxes)

| ID | Title | Type | Section | Objective |
|---|---|---|---|---|
| F7.1 | Chapter 7 at a glance (AI Work Loop, Frame highlighted) | Chapter map; imports `work_loop("Frame")` from ch01_figures | Opening | all |
| F7.2 | With unrestricted GPT-4 access, practice scores rose but exam scores fell | **Data chart** from Bastani et al. (2025) Table 1 (data/ch07_bastani_table1.csv: arm, phase, effect, SE, control mean); source line | 7.1 | O1 |
| F7.3 | Only the practice part of each session differed; the exam was closed-book for everyone | Session storyboard (review → assisted practice, three arms → closed-book exam) | 7.1, Case Study | O1 |
| F7.4 | Rereading won after 5 minutes; testing yourself won after a week | **Data chart** from Roediger & Karpicke (2006) Exp. 2 published values (SSSS 83%/40%, SSST 78%/56%, STTT 71%/61%; predicted-recall ratings 4.8/4.2/4.0) (data/ch07_rk2006.csv) | 7.2, 7.3 | O2, O5 |
| F7.5 | Retrieving, generating and spacing feel harder and last longer | Concept diagram (three moves: what you do, how it feels, what it does) | 7.2 | O2 |
| F7.6 | Feeling ready and being ready are different | 2 × 2 (feel ready / are ready); risk corner thick border | 7.3 | O5 |
| F7.7 | Inside the tool's frontier, it can do your learning for you; outside it, only your skill catches its errors | **Signature 2 (Jagged Frontier Map) reused**: `from ch01_figures import jagged`; ch07 wrapper draws jagged(f) unchanged and adds two callouts below the plot (canvas taller); no redraw | 7.4 | O3 |
| F7.8 | **Scaffold versus crutch: the same question builds skill only when you do the retrieving and generating** | Two paths from one question (crutch: ask → answer → copy → output delivered, skill unchanged; scaffold: attempt → hint/question → you generate → check → explain back → skill built); ≤ 9 boxes; caption ties back to F7.7 | 7.4 | O3 |
| F7.9 | Students with the unrestricted tool mostly asked for answers; tutor users shifted toward attempts | **Data chart** from Bastani et al. (2025) text: share of first interactions that repeated the question or asked for the answer (first problem: Base 56%, Tutor 42%; all problems in session 1: Base 67%, Tutor 37%) (data/ch07_bastani_messages.csv) | 7.4 | O3 |
| F7.10 | A tutor-mode setup asks for questions, hints and checks, not answers | Checklist card (five elements). Not a Signature 6 variant: Chapter 5's prompt-anatomy function does not exist yet; if it exists at draft time, use it with a highlight instead | 7.5 | O4 |
| F7.11 | A tutor-mode session is a small experiment on yourself | Protocol timeline (before → during → right after → later → reflect) | 7.6 | O6 |
| F7.12 | Your calibration gap is the evidence; your score is not the grade | A4 annotation and calibration sheet template | 7.6 | O5, O6 |
| F7.13 | In one review, step-based computer tutors came close to human tutors | **Data chart** from VanLehn (2011) published effect sizes (data/ch07_vanlehn2011.csv) [VERIFY answer-based and substep values] | Deep 7.A | (Deep) |
| F7.14 | Offloading is fine when the skill is not the goal | Decision tree (diamond: is this skill the goal of the task?) | Deep 7.B | (Deep) |
| F7.15 | Chapter summary card | Summary card | Summary | all |

15 figures plus F1.13 referenced in 7.1 (not redrawn). Interactive in Compass (D7 scope permitting): F7.8 step-through and a calibration self-check.

## 11. Labs (tool-neutral)

**Lab 7.1 Tutor-mode session** — Studio, Thursday Feb 11, in class, 75 minutes (syllabus lab flow), teams of 3–4, individual dialogues and write-ups.

| Minutes | Step |
|---|---|
| Before Thursday (~10) | Choose a concept new to you from your major and a course source; write three closed-book questions from the source; write baseline answers and confidence |
| 0–10 | Briefing: the protocol (F7.11), S/C codes, privacy rule; check your setup prompt against F7.10 |
| 10–35 | Tutor-mode dialogue, individually; attempt before every hint; note the turn numbers where you slipped toward answers |
| 35–45 | Devices away. Predict, then answer your three questions closed-book |
| 45–55 | Swap with a teammate: score each other's answers against the source; check one tool explanation together |
| 55–70 | Share and critique: each team brings one scaffold turn and one crutch turn to the class |
| 70–75 | Exit: one change you will make before the delayed check |

At home by Monday: delayed closed-book check (≥ 2 days later), annotation, verification, reflection, declaration (A4).

Optional home labs: **L7.2 Reread or retrieve?** (15 min + a 2-day check: split a short reading into two halves, reread one, self-test the other, compare) and **L7.3 Answer mode versus tutor mode** (15 min; the same question both ways; record what you did in each, mirroring Tuesday's demo).

Accessibility and alternatives: no-device route (human or text scaffold, alternative assignment); dated sample transcripts on eLearning; screen-reader-friendly annotation and calibration tables; dialogue in any language with English glosses of annotated turns; no personal, confidential or patient data; tool settings (memory off, temporary chat, built-in study modes) in Compass only.

## 12. Risks and checks

- **Bastani numbers exactly as published** (verified 2026-10-18 from PMC12232635): GPT-4, custom interfaces (Base "mimics" ChatGPT; it is not ChatGPT itself); percentages relative to the control mean; Tutor's exam effect −0.004, not significant; "nearly 1,000" students; classroom-level random assignment, honors classes excluded; the perception finding stated as the authors report it. The school is named only in the acknowledgments, so the chapter uses the paper's description. Spelling: Türkiye in the book's voice; the paper's "Turkey" kept in quotations and titles.
- **PNAS correction notice resolved:** 122(34), e2518204122 (Aug 20, 2025) corrects only Osbert Bastani's affiliation; no change to findings. Handoff: refresh-list rows 14 and 21 can be closed; Chapter 1's open item is cleared.
- **R3 title:** the syllabus's working-paper title ("Generative AI Can Harm Learning", 2024) differs from the PNAS title; cite the PNAS version.
- **Positive cases with limits:** Kestin et al. (two lessons, immediate post-tests, solutions supplied to the model, authors' own enthusiasm not repeated); De Simone et al. (working paper; check status and design details).
- **Learning-science claims** cited to primary sources (Roediger & Karpicke, 2006; Slamecka & Graf, 1978; Cepeda et al., 2006; Bjork, 1994; Bjork & Bjork, 2011; Flavell, 1979; Wood et al., 1976; Deslauriers et al., 2019; Kirk-Johnson et al., 2019; Soderstrom & Bjork, 2015), with Dunlosky et al. (2013) as the review. No "learning styles", no "10% of the brain"-type myths. Lee et al. (2025) is a self-report survey of knowledge workers: correlation, not effect, and not about students.
- **No anthropomorphic verbs:** "the tool returns a question", "the setup instructs the model to …", never "the tutor knows / wants / understands you".
- **Tool neutrality:** no product steps; the dated "study modes exist" sentence cites at least two providers and goes to the refresh list.
- **Characters:** Elif (main), Marcus (no patient data, ever); constructed dialogues labeled; new details logged.
- **Boundaries:** no re-teaching of the three zones (Ch. 1); no prompt anatomy (Ch. 5); no verification method beyond "check against your source" (Ch. 8); no writing-voice content (Ch. 10).
- **Conflict of interest:** Compass's planned tutor-mode assistant (D7) is not mentioned in Core; standard Compass placeholders only.

## Decisions taken under delegation (D19)

| # | Decision | Reason |
|---|---|---|
| T1 | R3 is cited and assigned in its PNAS 2025 version (open access), selected sections | Peer-reviewed, freely available; the working paper title in the syllabus is outdated |
| T2 | R4 limited to abstract, introduction and summary of findings (~10–15 min) | Keeps week 4 near two hours (syllabus 1–2 h); the full CHI paper is 22 pages |
| T3 | Opening Case and main Case Study = Bastani et al. (2025), as in the book map; school not named; full design given here, Chapter 1's preview acknowledged in one line | Book map; promise kept; avoid repeating Ch. 1 |
| T4 | Two positive short cases (Kestin et al., 2025; De Simone et al., 2025) | case index marks C04 "mixed"; the chapter must not read as "AI harms learning" (M4) |
| T5 | Signature 2 reused by importing `jagged` unchanged and adding callouts in a ch07 wrapper (taller canvas), because ch01's `jagged(f)` has no `highlight` argument and other chapters' files may not be edited | Signature rule (import, never redraw); suggest the editor add a `highlight` parameter in ch01 for Chapters 12 and 19 |
| T6 | "Scaffold versus crutch" is F7.8, paired with the Signature 2 reuse F7.7 | Book-map figure; 9-box limit; the jagged map alone cannot show who does the thinking |
| T7 | F7.10 is a standalone checklist, not a Signature 6 variant | Chapter 5's prompt-anatomy function does not exist yet; switch if it exists at draft time |
| T8 | Work Loop highlight = Frame (output or skill?) | The chapter's central decision happens before prompting |
| T9 | A4: closed-book scores are not graded; AI use during the closed-book checks is not acceptable; dialogues may be in any language with English glosses of annotated turns | Removes the incentive to cheat the self-test; supports ESL students (Elif) without changing the grading language |
| T10 | A4 rubric splits process evidence into Annotation 1.5 + Closed-book record 1.5, within the syllabus's 3/3/2/2 split | Same pattern as A2 in Chapter 2; criteria scored separately |
| T11 | Alternative assignment: human/peer or self-explanation scaffold plus annotation of a provided dated transcript pair | Same rubric, no AI required; matches the A2 alternative pattern |
| T12 | From the Field = Şeker (2015) pair-programming entry, facts limited to the entry, present-day connection marked; no disclosure (non-commercial) | Only author-written source in the inventory that fits; "watching the master" maps onto crutch use |
| T13 | Spaced Review draws on Chapters 5, 3 and 1, not 4 (read in week 5) or 6 (Deep) | Students have not read Chapter 4 by week 4 |
| T14 | Constructed dialogues are labeled; no real model transcript in the chapter | Style sheet §3 needs two providers for product examples; dated real transcripts go to eLearning for the alternative assignment |

Book-wide decisions for the handoff `## Decisions` section: T5 (signature reuse without a highlight argument), T9 (any-language dialogues with English glosses in artifacts) and T1 (cite peer-reviewed versions of syllabus readings when they exist).

## Author-only items (collected for the end, not asked now)

1. Live syllabus: R3 → PNAS 2025 version; R4 selected sections; week-4 total ~2.0–2.3 h.
2. Optional: a real, anonymized moment from the author's teaching where students used AI as a crutch or a scaffold, to replace or supplement From the Field; confirm the pair-programming entry as the source and its page range in *YBS Ansiklopedi* 2(1).
3. Course materials before Feb 11 (instructor preparation): the dated answer-mode/tutor-mode transcript pair and the peer-tutor question script on eLearning.
4. Final voice edit (pipeline step 8).

## Planned references and verification status (checked 2026-10-18)

| Reference | Status |
|---|---|
| Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. (2025). *PNAS, 122*(26), e2422633122. https://doi.org/10.1073/pnas.2422633122 | Verified, full text read (PMC12232635); correction 122(34) e2518204122 read: affiliation only |
| Lee, H.-P., Sarkar, A., Tankelevitch, L., Drosos, I., Rintel, S., Banks, R., & Wilson, N. (2025). CHI '25, Article 1121, 1–22. https://doi.org/10.1145/3706598.3713778 | Verified (Crossref; Microsoft Research abstract: 319 workers, 936 examples) |
| Roediger, H. L., III, & Karpicke, J. D. (2006). *Psychological Science, 17*(3), 249–255. https://doi.org/10.1111/j.1467-9280.2006.01693.x | Verified, full text read (Exp. 1: 120 students; Exp. 2: 180 students, values above) |
| Slamecka, N. J., & Graf, P. (1978). *JEP: Human Learning and Memory, 4*(6), 592–604. https://doi.org/10.1037/0278-7393.4.6.592 | Verified (Crossref) |
| Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). *Psychological Bulletin, 132*(3), 354–380. https://doi.org/10.1037/0033-2909.132.3.354 | Verified (Crossref) |
| Bjork, R. A. (1994). Memory and metamemory considerations in the training of human beings. In J. Metcalfe & A. Shimamura (Eds.), *Metacognition: Knowing about knowing* (pp. 185–205). MIT Press | Verified (bibliographic details; content via secondary summary) |
| Bjork, E. L., & Bjork, R. A. (2011). Making things hard on yourself, but in a good way. In M. A. Gernsbacher et al. (Eds.), *Psychology and the real world* (pp. 56–64). Worth | Verified (as cited in Bastani et al.); caveat on undesirable difficulties [VERIFY wording in the chapter] |
| Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). *PSPI, 14*(1), 4–58. https://doi.org/10.1177/1529100612453266 | Verified (Crossref); utility ratings from memory of the paper [VERIFY] |
| Flavell, J. H. (1979). *American Psychologist, 34*(10), 906–911. https://doi.org/10.1037/0003-066X.34.10.906 | Verified (Crossref) |
| Deslauriers, L., McCarty, L. S., Miller, K., Callaghan, K., & Kestin, G. (2019). *PNAS, 116*(39), 19251–19257. https://doi.org/10.1073/pnas.1821936116 | Verified (Crossref); findings [VERIFY sample and wording] |
| Kirk-Johnson, A., Galla, B. M., & Fraundorf, S. H. (2019). *Cognitive Psychology, 115*, 101237. https://doi.org/10.1016/j.cogpsych.2019.101237 | Verified (Crossref); findings [VERIFY] |
| Soderstrom, N. C., & Bjork, R. A. (2015). *Perspectives on Psychological Science, 10*(2), 176–199. https://doi.org/10.1177/1745691615569000 | Verified (Crossref) |
| Wood, D., Bruner, J. S., & Ross, G. (1976). *Journal of Child Psychology and Psychiatry, 17*(2), 89–100. https://doi.org/10.1111/j.1469-7610.1976.tb00381.x | Verified (Crossref) |
| Chi, M. T. H., Bassok, M., Lewis, M. W., Reimann, P., & Glaser, R. (1989). *Cognitive Science, 13*(2), 145–182. https://doi.org/10.1207/s15516709cog1302_1 | Verified (Crossref) |
| Kestin, G., Miller, K., Klales, A., Milbourne, T., & Ponti, G. (2025). *Scientific Reports, 15*, 17458. https://doi.org/10.1038/s41598-025-97652-6 | Verified, full text read (PMC12179260) |
| De Simone, M., Tiberti, F., Barron Rodriguez, M., Manolio, F., Mosuro, W., & Dikoru, E. J. (2025). *From chalkboards to chatbots* (Policy Research Working Paper 11125). World Bank | Verified (abstract read); design details and status [VERIFY] |
| VanLehn, K. (2011). *Educational Psychologist, 46*(4), 197–221. https://doi.org/10.1080/00461520.2011.611369 | Verified (Crossref; 0.79 and 0.76 confirmed); answer-based and substep values [VERIFY] |
| Bloom, B. S. (1984). *Educational Researcher, 13*(6), 4–16. https://doi.org/10.3102/0013189X013006004 | Verified (Crossref) |
| Nickow, A., Oreopoulos, P., & Quan, V. (2020). NBER Working Paper 27476. https://doi.org/10.3386/w27476 | Verified (Crossref); pooled effect size [VERIFY] |
| Risko, E. F., & Gilbert, S. J. (2016). *Trends in Cognitive Sciences, 20*(9), 676–688. https://doi.org/10.1016/j.tics.2016.07.002 | Verified (Crossref) |
| Federal Aviation Administration. (2013). *Manual flight operations* (SAFO 13002) | Cited via Bastani et al.; [VERIFY primary] |
| Study/learning modes: OpenAI (July 29, 2025), Google Gemini Guided Learning (Aug 6, 2025; TechCrunch verified), Anthropic Claude learning mode (Aug 2025) | Secondary sources verified; [VERIFY primary announcement pages]; refresh list |
| Şeker, Ş. E. (2015). Eşli programlama [Pair programming]. *YBS Ansiklopedi, 2*(1) | Read in full (Drive 1cJo2MG8E97EM4MqzyIaDMUh0GB9x58Ed → build/ch07/fromthefield-esli-programlama.md); [VERIFY page range] |
