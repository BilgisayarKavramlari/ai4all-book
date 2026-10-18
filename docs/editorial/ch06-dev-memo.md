# Chapter 6 — developmental memo (2026-10-18)

Inputs: four independent reviews run in parallel without sharing reports (build/ch06/reviews/): subject-expert reviewer (17 findings: 2 must-fix, 8 should-fix, 3 consider, 4 minor), pedagogy reviewer (13 findings: 3 must-fix, 9 should-fix, 1 consider), student-reader panel (Maya / Daniel / Ayşe; top-5 fixes), fact-checker (docs/factcheck/ch06.csv, 118 claims: 91 supported, 25 partly supported, 0 unsupported, 2 cannot verify; sources in docs/factcheck/ch06-sources.md). The editor settled conflicts in nine decisions; the chapter agent applied them and the rest of the reports under the author's delegation (D19). Pre-review draft: chapter v1 (assembled from build/ch06/part1–5.md).

## Decisions — accuracy (subject expert, fact-checker)

| # | Change | Why |
|---|---|---|
| A1 | Medprompt baseline: "In the paper's step-by-step chart, GPT-4 with a simple prompt and no examples scored 81.7%"; "earlier work"/"prior work" removed from text, chart note and longdesc; the Table 1 (81.4% five-shot) vs. Figure 4 (83.9%) mismatch and the earlier 78.9% recorded in data/ch06_medprompt.csv and C17 | Expert must-fix 1; editor decision 1 |
| A2 | Opening bullets reordered to match the chart (random examples → reasoning → similarity → five runs); the reasoning step now says GPT-4 also wrote its own reasoning before each answer (most of the +3.4) | Expert should-fix 3; pedagogy 7; editor decision 1 |
| A3 | Five runs = "the same question, options in a new order each time and some randomness in each answer, then a vote" (temperature > 0); framed as mainly a workflow, with the note that shuffling also changes the prompt; CSQ1 key accepts that answer | Expert 4; fact-check must-fix 1; editor decision 1 |
| A4 | "Same settings" → "did not retrain the model / change its parameters" everywhere, including the F6.12 title ("without retraining the model (2023)"). "Weights" not used: Chapter 3 uses "weights" for attention weights, and the editor's later addendum fixes "parameters" for learned values | Fact-check must-fix 1; editor decision 1 and addendum |
| A5 | 2024 reversal stated exactly: "the same kind of technique, five solved examples" (question and answer only, Figure 9 template); components tested one at a time; o1-preview "about 95–96%" with the table/chart gap explained; "might have reached" its noise ceiling; JMLE-2024 contamination check added; the "may have confused" reading attributed to the authors | Fact-check must-fix 2, 5, should-fix; expert 3, 13 |
| A6 | Interests: both papers have one OpenAI co-author (McKinney); Microsoft is a major investor in OpenAI and offers its models through its cloud (OpenAI, 2023) — stated as an interest, with "interests do not make findings wrong" | Fact-check must-fix 3; expert 8; editor decision 1 |
| A7 | Task placement rewritten: one rule ("long material first, full task last; optionally one line at the top"), attributed to provider guidance (Anthropic, n.d.: documents first, query last, up to 30% in its tests; OpenAI, n.d., GPT-4.1 guide: instructions before and after, above if once), Liu et al. stated accurately (query repeated before and after helped key-value lookup, barely changed QA), "test it"; Sam's block, recap, faded example, Check Yourself 6.3 Q2 and the A6 key updated | Expert must-fix 2; fact-check must-fix 4; pedagogy 5; editor decision 2 |
| A8 | Shi et al.: 58,052 built, 4,000 tested; base problems solvable by at least one method; "an older OpenAI model, code-davinci-002" (no year); the 6% sentence rewritten as "for only 6 of the 100 problems did the model answer every version correctly"; data/ch06_distraction.csv and F6.4 title/notes updated | Fact-check must-fix 6; expert 15; panel (Daniel); editor decision 3 |
| A9 | "Does not receive these as separate items" replaced: hidden role markers separate provider, user and model turns, and some models are trained to prioritize system instructions (Wallace et al., 2024); inside your own message nothing separates instructions from pasted text | Expert 5; editor decision 4 |
| A10 | Memory: Chapter 3 v2 wording word for word ("saves notes about a user, or draws on past chats…"); training on conversations named as a separate account option (pointer to Ch. 15); routine and Lab 6.4 cover past-chat memory ("turn it off or delete chats") and "check before you delete" | Expert 6, 7; panel; editor decision 5 |
| A11 | System prompts: "at least two providers" (Anthropic since July 2024; xAI since May 2025, Wiggers, 2025); "most products do not" removed (cannot verify); Ethics Lens aligned | Expert 9; fact-check cannot-verify C14; editor decision 5 |
| A12 | Dated box: OpenAI memory test (Feb 2024) and past chats (Apr 2025, Zeff, 2025); Gems announced May 2024, available Aug 2024; UTD wording (Copilot Chat approved for students; CometAI for faculty/staff and student employees via a manager) with a UTD OIT reference; [VERIFY] closed | Expert 10; fact-check should-fix; editor decision 5 |
| A13 | Project files: "for large projects, some products add only the parts of the files that a search finds" | Expert 11 (consider) |
| A14 | Zhao et al.: answers common among the examples (majority label), near the end of the prompt, common in training text; the class-imbalance analogy now cites it | Expert 12 (consider) |
| A15 | "Made the error impossible" → "removed the source of that error; he still checks each price"; "rebuilt and sent at every turn" gains "long chats may be shortened or summarized" | Expert 14, 16; pedagogy 13 |
| A16 | Şeker (2018): pages 10–17 and issue URL ([VERIFY] closed); "Cross Industry Standard Processing – Data Mining" as in the article; Chapman et al. carries the 2000 date; roles "at most of the steps"; "data story tellers" and "data fortune tellers" with the gloss marked as the book's | Fact-check should-fix; editor decision 8 |
| A17 | References: Min et al. DOI; Google title corrected; Anthropic suffixes now 2024a (Projects) and 2024b (agents); new: Anthropic (n.d.), OpenAI (n.d.), OpenAI (2023), Wallace et al. (2024), Wiggers (2025), Zeff (2025), UTD OIT (2026); "widely cited" removed | Fact-check should-fix; cannot-verify C115 |
| A18 | Terminology aligned with Chapters 3 and 5: "parameters" for learned values, "options" for user controls (standing instructions are written "in a tool's options"); glossary wording reused word for word for token, context window, parameter, temperature, memory | Editor addendum |

## Decisions — learning design (pedagogy, student panel)

| # | Change | Why |
|---|---|---|
| P1 | All seven multiple-choice items rebuilt: keys rotated (A2 d, A4 a, A7 c, A9 b, A10 d, A12 a, A14 c), option lengths matched, absolutes removed, every distractor tied to M1–M6; both answer files rewritten | Pedagogy must-fix 1; brief MC rule; editor decision 6 |
| P2 | Lab 6.3 rebuilt: no context-loss label for errors that were in the notes; question "in the notes, or introduced by the output?"; Version 1 gets an equal-time (5-minute) check of the final email, so the lab tests where a check belongs; Failure Diary line kept without a label | Pedagogy must-fix 2; editor decision 6 |
| P3 | Library rubric: gaps closed (Tests "most entries on fewer than three", Declaration "missing, or one element"), one dimension per level, "real recurring tasks" at every level, a failure required in Revision only (a hardened edge input counts), the with-and-without examples run scored under Tests, the workflow card's check and criterion scored under Task | Pedagogy must-fix 3; editor decision 6 |
| P4 | Alternative assignment: rationale "prefer not to, or cannot, run AI tools"; adds a workflow-card task for the 6.7 report-summary chain and a "no AI tools used" declaration; its own level descriptors for every criterion | Pedagogy 4; editor decision 6 |
| P5 | Fast route made self-contained: exact contents stated; recap box adds the Medprompt reversal, "examples do not carry over to a new chat" and what a workflow is; the Opening Case no longer promises an answer "by the end of 6.4"; Warm-up 3 reworded so the fast route answers it | Panel top fix 1; pedagogy 8; editor decision 7 |
| P6 | Time statement: two honest numbers at 150 wpm (fast ≈ 25 min; full through the Case Study ≈ 65 min, ≈ 75 with the remaining parts), with week-3 advice (fast route now, rest before week 11); library time counted per requirement (2.5–3 h) | Pedagogy 9; panel; fact-check C11; brief time rule |
| P7 | 6.1 trimmed: naming table moved to 6.5; term history cut to one dated sentence; one sentence per layer; a "Two lists of six" box separates the six layers from Chapter 5's six prompt parts | Pedagogy 8; panel (Maya); editor decision 7 |
| P8 | "Plain words for this chapter" box (token, context window, parameters and options, benchmark, zero-shot, majority vote, edge input, placeholder, version, agent vs. agency); idioms replaced (backfires, slipped, spoil, tilt, swing, worth their tokens, however convenient); "co-op" explained; dates as "21 October"; A3/A11/A13/R11/LO2 spelled out at use | Panel (Ayşe, Daniel) top fix 5; brief glossing rule; editor decision 7 |
| P9 | Text, figure and examples agree: F6.9 highlights only context (examples fixed if a test shows they help); F6.10 matches the 6.6 text (2 of 3, criterion (b); the v1.1 line); Sam's template puts notes first and the task last | Pedagogy 6; panel problem 2 |
| P10 | Faded examples fixed: TA example keeps two and asks for the third; leaflet criteria no longer conflict (warnings only, copied); primary sources ordered by date with type labels; design-student example made answerable; answers to all faded examples added to the Appendix E block | Panel top fix 3; pedagogy 13 |
| P11 | Your Turn 6.2 self-contained (a three-section policy in the box); Your Turn 6.3 "run each twice, limit the conclusion" | Panel; pedagogy 11 |
| P12 | Labs: Lab 6.1 adds a pass-criteria step (book and lab file now match); Lab 6.2 inputs labeled typical/different/edge, 40 minutes; every lab has a 10-minute version; Lab 6.4 "check before you delete" and a past-chat route | Panel top fix 4; pedagogy 11; editor decision 7 |
| P13 | Case Study prediction changed to the fallback ("what GPT-4 received, or how it was run?"; +6.7 vs. +1.8 under Figure 4, robust under Figure 6); the Figure 6 increments moved to the chart note and CSV; short cases each end with a task | Pedagogy 7, 13 |
| P14 | Item tags: A10, A12 Apply; B5 Create; A1 now a matching item, A5 and A11 application items; C3 now an O6 item (chains); the system-prompt question moved to Discussion; Spaced Review 3 items + 2 Chapter 5 interleaving items | Pedagogy 12 |
| P15 | Check Yourself 6.1 Q3 and 6.3 Q1 reworded (no anthropomorphic "the model needs labels to tell"); "Sam prefers SI units" replaced (units theme excluded) | Pedagogy 13 |
| P16 | Handoff: Instructor package section (9th) listing every promised asset with "needed by Thu Feb 4, 2027"; refresh rows include the fact-checker's time-sensitive list | Pedagogy 10; brief |

## Not changed (with reason)

- **Opening Case and main Case Study both use Medprompt.** The Opening poses the puzzle; the Case Study answers it with numbers and the 2024 reversal (same pattern as Chapters 2–3).
- **Chapter length (~15,100 words, about 1,000 more than v1).** The reviews asked for glosses, a self-contained fast route, alternative descriptors and answers; the fast route stays at about 25 minutes, and the full route is optional.
- **Daniel's request for real numbers in the survey-coding example.** It stays a constructed teaching example, now labeled "not measured evidence"; the chapter's measured evidence comes from the cited studies and the student's own with-and-without test.
- **Student panel: lab sample sizes are anecdotal.** Kept small on purpose (labs are practice); each lab asks for conclusions limited to the test, and Lab 6.2's debrief asks what ten questions would change.
- **No screenshot of a real settings page (Ayşe).** Tool neutrality (style sheet §3); the names box in 6.5 maps product names to the book's terms, and Compass carries current screens.
- **"Context loss" in Short case 2.** Kept as a forward pointer with Chapter 4's exact definition ("In week 5, Chapter 4 … will call this"), not as a Failure Taxonomy label; Lab 6.3's label was removed (P2).
- **Spaced Review from Chapters 3 and 2 only (plus Chapter 5 interleaving).** Reading order puts Chapter 4 after Chapter 6.
- **Further Reading keeps Min et al. and Yoo et al.** as a Deep pointer, now described as "qualified" rather than "disagree" (fact-check C80).

## Waiting for the author

1. CRISP-DM article affiliation ("Bilkav Eğitim Danışmanlık"): confirm no disclosure is needed.
2. Optional: a CRISP-DM project anecdote for From the Field (never invented).
3. Live syllabus: CometAI is listed as a student tool, but UTD OIT pages restrict it to faculty, staff and student employees via a manager; Copilot Chat is approved for students.
4. Final voice edit (pipeline step 8); the editor never marks a chapter "done".

## Voice pass (Mode B, 2026-10-18)

Light pass with docs/voice/voice-profile.md §10 rules 1–4: a breadth opening for 6.2 (a nursing student, an engineer and a history student each pasting a large source), two "In other words" restatements (6.2 habits; 6.7 two shapes of workflow), a two-field "For example" after the opening claim of 6.5 (marketing and nursing students), and a "Let's take …" walkthrough for Sam's template in 6.6. No facts, numbers, citations, headings or figure references changed. The author's final voice edit is still pending.
