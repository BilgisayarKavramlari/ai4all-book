# Chapter 7 — developmental memo (2026-10-18)

Inputs: four independent reviews run in parallel without sharing reports (build/ch07/reviews/):
- subject-expert reviewer (Opus; 3 major, 5 moderate, 9 minor);
- pedagogy reviewer (Opus; 5 high, 5 medium, 7 low);
- student-reader panel (Maya, Daniel, Ayşe);
- fact-checker (Sonnet; docs/factcheck/ch07.csv, 96 claims: 69 supported, 22 partly supported, 0 unsupported, 1 outdated, 4 cannot verify; sources in ch07-sources.md).

The editor settled the conflicts in nine decisions (numbered E1–E9 below). Under the author's delegation (D19), the chapter agent applied them in revision v2. The pre-review draft is in git (commit b938cf3).

## Decisions: accuracy (fact-checker, subject expert; editor E1)

| # | Change | Why |
|---|---|---|
| A1 | Randomization stated exactly: the school places students in classrooms at random; the researchers assigned whole classrooms to conditions with a procedure that balanced observable characteristics (honors classes excluded). Applied in the Opening Case, the Case Study and its table, F7.3 and C04 | Fact-check C07, C18 (footnote # of the paper); E1 |
| A2 | "A team led by researchers at the University of Pennsylvania" | Fact-check C01: two authors are not at Penn |
| A3 | Opening Case and Summary: GPT Tutor "not measurably different" / "no measurable harm", instead of "about the same" / "avoided the harm"; "statistically significant" glossed at first use | Student panel (Daniel): not significant is not equal; pedagogy row 8 |
| A4 | Roediger & Karpicke: "four 5-minute study periods (about 14 read-throughs)", three periods + one recall, one period (about 3 read-throughs) + three recalls. F7.4 labels and data/ch07_rk2006.csv relabeled; "Restudiers predicted the best recall" | Fact-check C32 (Table 1: 14.2/10.3/3.4 readings); E1 |
| A5 | Pretesting caveat in 7.2: a difficulty you cannot meet is "a problem that needs knowledge you do not have yet, with no answer or feedback afterward"; guessing before study helps if the answer follows (Kornell, Hays & Bjork, 2009, verified on Crossref and Europe PMC); "one reason A4 starts with questions." Check Yourself 7.2 Q3 reworded | Subject expert #1 (major): v1 contradicted pretesting research and A4's own design; fact-check C38 |
| A6 | Nickow et al. replaced by the peer-reviewed AERJ 2024 article: about 0.29 SD across 89 randomized experiments, largest with teachers or paraprofessionals | Subject expert #2; fact-check C67 (outdated) |
| A7 | Nigeria study rewritten. **Design:** nine public schools in Benin City; twelve 90-minute after-school sessions with teacher support; randomization among the roughly half of students who volunteered; the control group had no extra program. **Results:** English 0.23 SD (the main outcome); the 0.31 SD total includes AI and digital-skills content taught only to participants; regular end-of-year exam about 0.21 SD. **Limits:** 1,328 randomized, 759 assessed, more missing among controls. **Citation:** "updated December 2025"; blog and working paper disambiguated in-text (Barron Rodriguez vs. Mosuro) | Subject expert #3 (major); fact-check C55–C62; E1 |
| A8 | Case Study synthesis: "all three used GPT-4-class models; what differed was what students were set up to do"; new table row "Compared with"; outcome cells marked as not directly comparable | Subject expert #4: the model was never varied |
| A9 | Summary mechanism hedged: "the most likely reason, consistent with the authors' evidence that students copied …"; "one likely reason they did not notice …" | Subject expert #5; student panel (Daniel) |
| A10 | Error-carryover argument: "If wrong answers had misled students, the errors should have hurt the paired exam problems too, but the researchers found no evidence that they did"; moved from 7.1 to the Case Study | Fact-check C21; subject expert #11; pedagogy (E1) |
| A11 | GPT Base errors described as mostly flawed solution logic (42%), some arithmetic (8%), in the Case Study and C04; "when asked for the answer … 51%" in 7.4 | Subject expert #12, #14 |
| A12 | Authors' limits in their words ("fall 2023, when generative AI was still new; GPT-4, since improved on by newer models"); Kestin's comparator named as active learning ("median gains more than double active learning's, immediate test") | Subject expert #13, #15 |
| A13 | Lee et al.: task-level confidence ("in tasks where they were more confident that AI could do the work …"); moved to 7.4 (overreliance), both directions, self-report | Fact-check C47; E1/editor item 9 from the pedagogy review |
| A14 | Deep 7.A: VanLehn "computer scientist"; Bloom's tutoring "combined with mastery learning, so the 2-sigma effect cannot be credited to tutoring alone"; finer-grained systems "did not do reliably better"; answer-handing tools "give even less than the weakest systems …, which at least responded to the student's own answer" | Fact-check C64, C65; subject expert #9, #10 |
| A15 | FAA SAFO 13002 read in the primary source: "so that manual-flying knowledge and skills do not degrade"; reference with issuing office, date (January 4, 2013) and URL; [VERIFY] markers removed | Fact-check C69, C70 |
| A16 | Study modes from primary announcements: Claude (April 2025 education accounts; August 2025 all users), ChatGPT (July 29, 2025), Gemini (August 6, 2025); "none had been tested in a published experiment on learning," as far as the book could find in October 2026. ChatGPT's menu change goes to the refresh list | Subject expert #8; fact-check C71–C73; E1 |
| A17 | Şeker (2015) reference completed (*YBS Ansiklopedi* 2(1), 19–21, issue URL). "Watching the master" now reads "asserts that mastery" | Fact-check C79 and S30 |
| A18 | Smaller fixes: "repeated the question text" (C12); "Which values are outside their normal ranges?" (subject expert #16); "GPT Base raised the first number" (subject expert #17); "three researchers" for Wood, Bruner & Ross (C75); preregistration explained without an unverified "before the study" claim (C19) | Fact-check; subject expert |

## Decisions: learning design (pedagogy, student panel; editor E2–E9)

| # | Change | Why |
|---|---|---|
| P1 | **A4 validity.** Check questions stay out of the dialogue (students practice on neighboring problems); the delayed check uses parallel keyed questions where they exist; students do not look at the key before the immediate check. Added to the Task descriptor, 7.5's Your Turn, 7.6, Lab 7.1 and A4 item 3. The record is called "a signal about you, not proof of what works" (three questions, no comparison) | Pedagogy row 2 (high); subject expert #7; student panel (Daniel); E2 |
| P2 | **One prediction format** everywhere. A 0–100% confidence rating per question; the ratings are summed and divided by 100 to give a predicted score. Calibration gap = predicted − actual, judged on a set. Defined in the 7.3 and 7.6 text, not only in F7.12. The faded table is in aggregate form; the Warm-up Your Turn, Marcus's two examples, F7.12, Lab 7.1, A4 item 5, Review A14 and B5 all use the same format. The model sense quotes Chapter 8's wording | Pedagogy row 5; subject expert #6; student panel cross-cutting 1; E3 |
| P3 | **S/C coding rules** in 7.4. A request that sets up your own attempt = S; a request for the answer = C. Feedback is S only after an attempt at the same question. "OK, thanks" turns are uncoded. Elif's dialogue gains a labeled borderline row. The music Your Turn is replaced by a self-contained business dialogue (break-even). Keys accept either code if the reason applies the rules | Pedagogy row 4; student panel (Ayşe, Maya); E4 |
| P4 | **Rubric.** "Declaration and judgment" split into Reflection 1.5 and Declaration 0.5, each with four levels. Rule: "when a submission fits parts of two levels, give the lower level whose description fully applies." Level gaps filled (Task: one missing or two weak; Closed-book: two or more elements missing; Annotation: three or more vague reasons) | Pedagogy row 6; student panel (rubric weight); E5 |
| P5 | **Workload.** Two reading numbers (31 min for 7.1–7.6, 45 min for the required package) and the week counted by requirement (about 2.2 h). Reflection cut to 200–300 words; the Case Study is read in Tuesday's class; annotation is finished in the lab (20 min; briefing 5 min). Core and Studio trimmed by about 800 words, cutting the frontier paragraph, the Kestin details in 7.5 and repeated steps in 7.6 | Pedagogy row 3, row 9; student panel; E6 |
| P6 | **Reading order.** Review A4 is now "Why is overreliance something people do, not a property of the output?"; CSQ5 asks "output or use?". The Case Study's tree/chain label is replaced by "two kinds of problem," with a pointer to Chapter 4. The leaf label stays only in C04 | Pedagogy row 7; brief reading-order rule; E7 |
| P7 | **Multiple-choice keys rotated** (A2 a, A5 d, A7 c, A9 a, A10 b, A12 d). Distractors carry reason clauses of similar length drawn from M1–M5b. New A14 (calibration gap arithmetic). Appendix E and private/ updated | Pedagogy row 1; E8 |
| P8 | **Glosses at first use:** statistically significant, randomly assigned ("in other words, the groups were alike on average"), standard error (sentence after F7.2), crutch (in 7.1, before 7.4), SD and effect size, median, peer-reviewed vs. working paper, preregistered, crossover, *PNAS*, agile, statics, free-body diagram, limiting reagent, periodization, keyed questions. "Junior" → "third-year" | Pedagogy row 8; student panel; E8 |
| P9 | **ESL wording.** Idioms replaced: "slid toward", "dodge", "the pull", "drifts off", "rewards the crutch", "the word was not enough". A language line added (dialogue in any language or simple English; closed-book answers in the course language). The scaffold image glossed ("like the frame around a building under construction") | Student panel (Ayşe); E8 |
| P10 | **Access and fields.** "A course you are taking this term" replaces "your major". A humanities keyed-question example (study-guide items keyed to a page) added. Marketing analyst and physician rows added to the Career table. A one-line link sentence opens From the Field. The Career row no longer points Core readers to Deep 7.B | Pedagogy row 11; student panel (Maya, Daniel); E8 |
| P11 | **Faded examples.** Chemistry: the Context is filled with the student's level, and the reader finds the two missing elements. History turn 8 states her action (copies the dates without checking) so the item has one key | Pedagogy rows 12, 13 |
| P12 | **Labs.** Lab 7.2: chapter and file aligned; a counting rule (list each half's main ideas first); no checking of half B (so neither half gets extra study); the prediction comes before the two-day check; the note now says week 5. Lab 7.3: two questions of similar difficulty, tutor mode first, 20 minutes. Lab 7.1: timings 5/25/10/10/20/5; missed-lab route by Friday so the delayed check fits before the deadline | Pedagogy row 15; student panel (Daniel, cross-cutting 2); E8 |
| P13 | **A4 brief.** Reflection (a) defines performance during the dialogue (how many attempts were right before a hint); (b) asks "what that suggests about how much stuck" (not a spacing effect); verification covers "explanations, hints or verdicts"; the alternative assignment's (d) uses the provided transcripts and has a time estimate (about 70 minutes) | Subject expert #7; student panel cross-cutting 3; pedagogy row 10 |
| P14 | **Tags and placement.** Review C1 retagged O4 · LO4; C2 reframed for O5 (calibration gap vs. practice score); Discussion 1's LO5 dropped; F7.3 placed right after the three-part list; the Chapter 1 test quoted exactly | Pedagogy rows 14, 16, 17 |
| P15 | **Handoff.** New ninth section "Instructor package": transcript pair and Case Study handout by Tue Feb 9; peer-tutor script, A4 template and keyed-question guidance by Thu Feb 11. Refresh rows include the fact-checker's table. Glossary gains "Calibration gap" and "Keyed questions". Appendix E includes faded-example answers | Pedagogy row 10; brief; E9 |

## Not changed (with reason)

- **Core length.** Core and Studio are about 4,600 words, against the blueprint's 4,200. The coding rules, the pretesting caveat, the calibration arithmetic and the glosses the reviews asked for outweigh the cuts. The week stays at about 2.2 h because the Case Study moved to class. Recorded in handoff D-7.d.
- **F7.7 (Jagged Frontier Map) keeps Chapter 1's tasks.** The student panel suggested relabeling them with study tasks. A signature diagram is reused unchanged (signature rule); the two callouts underneath carry the learning point.
- **[COMPASS: …] placeholders, framework codes in the objectives, and per-set numbering of end-of-chapter items** are book-wide conventions (Chapters 1–5). The chapter-at-a-glance paragraph now says "odd-numbered items in each set".
- **Elif's peer-tutoring observation kept**, presented as an anecdote followed by evidence (consider item 19; characters.md fixed detail).
- **Pre-lab and home times** are stated as 15 and 55 minutes, not the student panel's 20–30 and 90. The panel's estimates assumed a 300–400-word reflection, annotation done at home and finding a keyed source unaided; all three are now addressed (200–300 words, annotation in the lab, keyed-question guidance in the instructor package).
- **Acid–base normal ranges are not printed** (fact-check C90): the fact-checker saw them only in a snippet. The examples rely on the student's textbook ranges.
- **Flavell (1979), Chi et al. (1989), Wood, Bruner & Ross (1976)** could not be read in full (fact-check C42, C74, C75). The citations are bibliographically correct and the sentences are standard, cautious paraphrases. They stay on the refresh list for a pre-print check.
- **Bastani SI Appendix** (session dates, cluster detail) is not reachable. The text avoids claims that depend on it.

## Waiting for the author

1. Live syllabus, week 4: R3 → the PNAS 2025 version (Significance statement + Table 1); R4 → the abstract, discussed in class; the Case Study read in Tuesday's class. The editor updates the repository's docs/syllabus.md.
2. Optional: an anonymized teaching moment for From the Field (the source entry is confirmed: *YBS Ansiklopedi* 2(1), 19–21).
3. Final voice edit (pipeline step 8). The editor never marks a chapter "done".

## Voice pass (Mode B, 2026-10-18)

A light pass with docs/voice/voice-profile.md rules 1–4:
- **Breadth openings** for the chapter-at-a-glance paragraph (nursing, marketing, history), 7.2 (drug classes, accounting rules, dates of a war) and From the Field (programmers had a version of this question).
- **"In other words" restatements** after the randomization paragraph and in 7.3's "predict, then check".
- **A "For example" with numbers** right after the calibration definition (40% + 30% + 50%).
- **"Teachers, sports coaches and employers"** as a cross-field opening in 7.1.

No facts, numbers, citations, headings or figure references were changed in the voice pass. The author's final voice edit is still pending.
