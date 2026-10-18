# Case: GPT-4 tutors and learning in a high school in Türkiye (Bastani et al., 2025)

Chapter: 7 (Opening Case and main Case Study; previewed in Chapter 1, section 1.2) · Field: education (secondary mathematics) · Failure label: **hallucination → wrong-calculation leaf, documented (solid)**: GPT Base's answers to the practice problems were correct only 51% of the time (logical errors 42%, arithmetic errors 8%; Bastani et al., 2025). The harm to learning is a **use failure, labeled on Chapter 4's failure-to-harm chain**: output → no check of one's own → reliance (copying) → skill not built; **overreliance, documented** by the message analysis and the exam result (solid). Not labeled as overconfidence: the paper reports no evidence about expressed certainty. · Outcome: **mixed** (unrestricted access harmed exam performance; a guarded design avoided the harm but did not improve it)

Student-facing text (Chapter 7) does not use Signature 5; tree labels for students start in Chapter 8 (reading order).

## Context
A field experiment run by researchers from the University of Pennsylvania with a large high school in Türkiye during the fall semester of the 2023–24 school year. Nearly 1,000 students in about fifty 9th-, 10th- and 11th-grade classes took part in four 90-minute math review sessions, together about 15% of the semester's curriculum. Classrooms were randomly assigned to one of three conditions (the school assigns students to regular classrooms at random; honors classrooms were excluded from the main sample). The study was preregistered with the unassisted exam as the primary outcome. The school is named only in the paper's acknowledgments; the book uses the paper's description. Published open access in *PNAS* (June 25, 2025); a correction (August 20, 2025) changed one author's affiliation only.

## Timeline
- Fall semester 2023–24: four sessions per grade; each session = teacher review → assisted practice (randomized) → closed-book, closed-laptop exam with problems paired to the practice problems; practice and exam both counted toward grades.
- 2024: working paper on SSRN [VERIFY first posting date] ("Generative AI Can Harm Learning"; syllabus reading R3 cites this version).
- June 25, 2025: *PNAS* article, 122(26), e2422633122.
- August 20, 2025: *PNAS* correction, 122(34), e2518204122 (affiliation of Osbert Bastani; no change to findings).

## What the AI did
- **GPT Base:** a chat interface built on GPT-4 to mimic ChatGPT; its hidden prompt included the current problem and told GPT-4 to act as a tutor and help the student solve it. Asked ten times per problem with the students' most common message ("What is the answer?"), it answered correctly 51% of the time.
- **GPT Tutor:** the same model and interface; the hidden prompt also contained teacher-written solutions, common mistakes with feedback, and an instruction to give hints instead of the answer. Students in both AI arms saw a short video on prompts that support learning.

## What humans did
- Students in the control arm practiced with books and notes, no devices. Teachers did not interact with students during practice or the exam; a teacher and a staff member monitored the AI classes.
- In GPT Base classes, students most often asked for the answer or restated the question (first interactions in session 1: 56% for the very first; 67% across first interactions on each problem). In GPT Tutor classes, these shares were 42% and 37%, and attempts and requests for help grew over time. (GPT Tutor offered suggested prompts, which the authors note may explain part of the first-message gap.)
- Two part-time teachers wrote the problem-specific inputs for GPT Tutor; the authors call the construction labor-intensive.

## Consequences (documented only)
- Practice (assisted): GPT Base +0.137 and GPT Tutor +0.361 on a 0–1 normalized grade versus a control mean of 0.284 (+48% and +127%).
- Exam (unassisted, right after): GPT Base −0.054 versus a control mean of 0.321 (−17%, p < 0.05); GPT Tutor −0.004 (not significant).
- Mechanism: GPT Base's errors lowered practice scores on the affected problems but did not carry over to the paired exam problems, which the authors read as students copying rather than learning from the answers.
- Perception: GPT Base students did not perceive lower learning or performance; GPT Tutor students perceived significantly better exam performance than they achieved.
- Skill gap: both tools narrowed grade dispersion during practice; no significant effect on dispersion in the exam.
- Limits stated by the authors: one school, one subject, short-term outcomes, fall 2023 (students new to the tools), GPT-4 (since surpassed).

## A better workflow (AI Work Loop: Frame → Prompt → Verify → Decide → Disclose)
For a student: **Frame** — is the goal the answer or the skill? (here, the skill). **Prompt** — a tutor-mode setup: attempt first, one hint at a time, no full answer before two attempts. **Verify** — score attempts against a source (the key), not the tool's verdict; finish with a closed-book check. **Decide** — keep, change or reject the tool's hints; stop a session when too tired to attempt. **Disclose** — note study help in the AI Use Declaration when it contributes to graded work.
For a school: give students guarded tools with accurate reference material, and measure unassisted performance, not only performance with the tool.

## Questions (4–6)
1. What did the control group do during practice, and when was the exam taken? Why do both details matter?
2. Explain the error-carryover argument for "copying rather than learning."
3. Why do students' perceptions matter for how they should use AI while studying?
4. GPT Base was told to act as a tutor. What did GPT Tutor add, and which addition might matter most?
5. Which limits stop you from generalizing this result to a college course in your major in 2027?
6. Where on the failure-to-harm chain does the harm sit, and why is it not labeled on the tree?

## Sources (at least 2, one primary; with access date)
1. Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. *Proceedings of the National Academy of Sciences, 122*(26), e2422633122. https://doi.org/10.1073/pnas.2422633122 (full text read via PMC12232635, accessed 2026-10-18)
2. Correction for Bastani et al. (2025). *Proceedings of the National Academy of Sciences, 122*(34), e2518204122. https://doi.org/10.1073/pnas.2518204122 (read via PMC12403119, accessed 2026-10-18)
3. Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. (2024). *Generative AI can harm learning* (working paper). SSRN. https://papers.ssrn.com/abstract=4895486 (accessed 2026-10-18)
4. Data and code: https://github.com/obastani/GenAICanHarmLearning (listed in the article; not re-analyzed for the book)
