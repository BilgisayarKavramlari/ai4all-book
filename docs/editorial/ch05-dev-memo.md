# Chapter 5 — developmental memo (2026-10-18)

Inputs: four independent reviews run in parallel without sharing reports: subject-expert reviewer (Opus; 22 items), pedagogy reviewer (Opus; 17 items), student-reader panel (Maya / Daniel / Ayşe, Sonnet), and fact-checker (Sonnet; docs/factcheck/ch05.csv, 111 claims: 84 supported, 19 partially supported, 4 unsupported, 1 outdated, 3 cannot verify). The editor's eight decisions settled conflicts between them. Revision v2 applies them under the author's delegation (D19). The pre-review draft is kept in build/ch05/ch05-v1-prereview.qmd.

## Decisions — accuracy (fact-checker, subject expert)

| # | Change | Why |
|---|---|---|
| A1 | Lucía's version history rebuilt so every logged row is exactly one change: v2 = v1 + pasted figures; v3 = + the products rule (paired with a positive form, "refer to tools in general terms"); a **frame row** (C3 rewritten after the peer swap); v4 = + explain-terms rule; v5 = + gap rule. Section 5.3 now shows v1 and the labeled **final** prompt (v5), "5.4–5.5 show how she got there"; she has no role and no in-context examples, with reasons. F5.7 and F5.13 redrawn; alt texts updated | Fact-check C79 (unsupported); expert #1 and #18; pedagogy must-fix #1; editor decision 1 |
| A2 | "Five of six runs" → "Four of six runs"; longdesc F5.11 "Four cells" | Fact-check C78 |
| A3 | Ladder axis now describes each rung's **default**. 5.2 adds "where the human check sits" and says a design can add an approval gate (Ch. 14) without changing the rung. In the Case Study, "the same rung" became "Both are agency. They differ in whether the design kept a human check before each output." "The check … was removed" became "There was no human check before each answer reached the customer", and the case notes that human agents handled chats throughout | Expert #2 and #14; pedagogy #12; fact-check C28; editor decision 2 |
| A4 | Klarna statements re-cited to the outlets that contain them. "Cost too dominant / lower quality" → Fisher (2025, CX Today, quoting Bloomberg). "Always a human" and fully remote hiring → Shibu (2025, Entrepreneur; author named). "Uber-type" → Fisher; "small pilot" and "still enthusiastic about AI" → Engelking (2025, heise online). November figures → "CX Dive reported that the CEO said…" (Doerer, 2025). "Remained committed to AI" deleted from the Opening Case; the heise-sourced version is in the Case Study timeline | Fact-check C13, C16, C17 (unsupported), C23; expert #3; editor decision 3 |
| A5 | Klarna's 2024 measures listed in full everywhere (volume, speed, cost, repeat questions, a company-reported satisfaction score) in the Opening Case, 5.1 and the Summary. The human option is shown as already offered in 2024. F5.5 retitled ("…from efficiency (2024) to quality and a promise of human help (May 2025), then back to AI savings (Nov 2025)") and its panels labeled confirmed/reported | Fact-check C20, C21; expert #4; pedagogy #6 |
| A6 | Attribution tiers (confirmed / reported / inferred) stated in the Case Study, the case file and F5.5 | Brief (new book-wide rule) |
| A7 | SEC draft registration statement (DRS/A, Jan 24, 2025) added to the Case Study timeline: 60% of chats since launch, no drop in satisfaction per internal surveys. The agent read the EDGAR text directly (filename1.htm) and the filing index (Form DRS/A, filed 2025-01-24) | Editor decision 3 (only if verifiable in EDGAR text) |
| A8 | 5.4 keeps only please vs. order ("made no difference overall … single questions changed a lot"). It adds "two OpenAI models released in 2024" and Meincke 2025c (tips and threats). The measurement lesson moved to 5.5, which defines the strict standard, the majority standard, random guessing (25%) and the 95% interval in Core. It says answers varied even at temperature 0 and adds the authors' caution about other models. The category error ("measuring mattered more than wording") was replaced: "The answers were the same; only the definition of success changed" | Expert #5–7; pedagogy #5; panel (Daniel); editor decision 4 |
| A9 | F5.10 now plots only the two politeness prompts, with the report's own values (points above random, 95% intervals). The reference and unformatted bars were dropped, so no format-line comparison is implied. Title: "Whether a wording 'worked' depended on how strictly success was defined" | Expert #5 (the bars likely lacked the format line). The report's methods say only the prefix changed, so the "(no format line)" label was not confirmed; dropping the cross-comparison avoids the issue |
| A10 | "A 2022 study" → "a study published in 2023" (all places). "Most stopped" → "Many stopped". The "do not say" episode is described as in the paper | Fact-check C43, C59, C61; expert #20 |
| A11 | Brown et al.: "without any change to its parameters, the learned settings from Chapter 2, so no retraining" | Fact-check C44; expert #16 |
| A12 | Zheng scope ("four families of openly released models", "persona in the system prompt"); Sclar scope ("the effect remained in larger and instruction-tuned models"; "a model whose settings Meta released openly") | Expert #17; pedagogy #16 ("open model" glossed) |
| A13 | Role redefined as voice or perspective; audience goes in context (definition, Signature 6 sub-label "voice and perspective", glossary row, faded abstract example) | Expert #8; editor decision 7 |
| A14 | Memory caveat in 5.3 (memory glossed); "fresh, temporary chat" defined in step 5 and in the Hands-on Labs intro (memory off where possible) | Expert #9; panel (Ayşe); editor decisions 4 and 7 |
| A15 | Test leakage: "once you change a prompt to pass an input, that input no longer tests it fairly; add one new input". Lucía adds a $120-textbook month. "Six passes" stated as "evidence for this task, tool and date, not proof" | Expert #10–11; editor decision 4 |
| A16 | Deep 5.B updated as of October 2026 with the January 2026 report (November 2025 data, newer classifier: 52% augmentation, 45% automation on chat; about three-quarters API automation; Appel et al., 2026, read by the agent), and a note that a March 2026 report exists. API-format caveat added. "Same month and method" in text, F5.14 alt text, CSV and chart source line. No trend claim | Expert #12–13; fact-check C71, C72 (outdated); editor decision 5 |
| A17 | Meincke 2025b wording: "a small average gain, smaller for those that already produce steps unasked, … more variable" | Expert #15 |
| A18 | AI Fluency wording: "if, when and how"; "including for other people"; "warns that agency needs a good grasp of what AI can and cannot do"; reference dated December 2025 with the PDF URL; "about ten pages" | Expert #19, #22; fact-check C38, C75 (unsupported) |
| A19 | References: Shibu (Entrepreneur), Fisher (CX Today), Engelking (heise), Klarna Group (DRS/A) and Appel et al. (2026) added. Anthropic n.d.-a / n.d.-b. Google cited as the April 2024 edition via the archived copy (the original URL returns 404). Bloomberg dropped from the reference list (not read; named in text as the interview the outlets reported) | Fact-check C88, C96, C97, C108 |
| A20 | Case file C18: failure-label line broadened ("no specific wrong answers documented in the sources used; one analyst reports complaints about generic answers"); sources and tiers updated | Fact-check C29 |

## Decisions — learning design (pedagogy, student panel)

| # | Change | Why |
|---|---|---|
| P1 | A3 rubric gaps closed exactly as proposed: Developing for task = "one or more elements missing"; Versions Developing adds "most rows change several things or lack predictions"; Testing Proficient uses "or"; Declaration Beginning = "missing, or only one element" | Pedagogy must-fix #2; editor decision 6 |
| P2 | Alternative assignment rewritten as seven steps (including "propose typical, different and edge inputs for v7 and say what result would show it works") with **its own four-level rubric table** | Pedagogy #8; editor decision 6 |
| P3 | The in-lab peer swap on v3 counts for A3. Re-swapping the final prompt is optional. The same wording is used in the chapter's Lab 5.1, the A3 brief and labs/ch05-lab1.md | Pedagogy must-fix #3; panel (Ayşe); editor decision 6 |
| P4 | Required runs reduced: final version one run each on a different and an edge input (the usual input counts as typical). The A3 home time is counted from the requirements (7 runs, about 7 outputs scored, writing): **60–70 minutes**. "How many runs are enough?" paragraph added to 5.6; "two runs is a minimum … evidence, not proof" in A3 item 3 | Pedagogy #4; panel top fixes 1 and 4; editor decision 4 and 6 |
| P5 | Honest time statement with two numbers at 150 wpm: Core sections ~32 min; whole Core package ~53 min; A3 60–70 min. **R2 module 2 made recommended for week 3** so that the honest count stays ≤ 2.2 h (≈ 1.9–2.05 h); recorded as handoff decision D-5.e and an author-only live-syllabus item | Brief (time statements; weekly workload ≤ 2.2 h); pedagogy #4; panel |
| P6 | Verification scaffold for week 3 in A3 item 5 and the lab file: recompute every total; compare facts with the source you supplied, textbook or course notes; Chapter 8 adds methods | Pedagogy #10 |
| P7 | Review A distractors rewritten from misconceptions without "always/never": A7(c) "A role has no effect … at all"; A11(c) "the same on every single question"; A9(c) "all six parts"; A9(d) a context misreading; A14(b) "a typical input run a second time". Keys rotated (a: A2, A10; b: A9, A12; c: A4, A14; d: A7, A11); answers in the handoff and private file updated | Pedagogy #7; brief (MC key rotation) |
| P8 | Labs retimed: L5.2 = 30 min with "a reading you have already read"; L5.3 = 12 runs, 40 min, class pooling | Pedagogy #11; panel (Daniel) |
| P9 | "Rung" and "floor" introduced in 5.1 before first use (the sixth frame-card box is marked "added in 5.2"). "Where the human check sits" explained in 5.2, as the Opening Case promises. "Agents" glossed as human staff in the Opening Case. "Agency" vs. a marketing agency glossed | Panel top fix 2; pedagogy #13; editor decision 7 |
| P10 | Glossing and plain English: "buy now, pay later", benchmark, net pay, withholdings, alternator, open model, temperature, memory, interval. Idioms replaced: "on par" → "about the same as", "errands" → "problems", "swung widely" → "changed a lot", "opportunistically" → "by trial and error, without a plan", "over-pivoted" → "leaned too far toward cutting costs", "earns its place" removed | Brief (glossing rule); pedagogy #16; panel (Ayşe) |
| P11 | Hints added to all six faded examples; full self-check answers in Appendix E (handoff) | Panel top fix 5; editor decision 7 |
| P12 | Check Yourself 5.2 Q1 now practices Justify (place a part and give the reason). CY 5.4 Q2 asks what the test found; the strictness question moved to CY 5.5 Q2. CY 5.6 Q1 de-ambiguated | Pedagogy #5, #14; panel (Ayşe) |
| P13 | F5.1b removed (it repeated the Chapter Map). The Summary shows the summary card and one signature (F5.6). F5.13 moved to 5.6 so the Studio section has its own figure | Pedagogy #15 |
| P14 | 5.4 Your Turn adds a no-lab route ("write v1–v2 from your 5.1 frame card now"); 5.5 worked example says how a test input enters the prompt (replace the figures in the context line) | Pedagogy #17 |
| P15 | Handoff gains the 9th section "Instructor package": log template and accessible version, task bank, dated six-version sample log, L5.2 and L5.3 samples and scoring sheet, Compass steps, each with the date needed | Pedagogy #9; brief; editor |

## Not changed (with reason)

- **"(no format line)" label on the politeness bars** (expert #5): not applied. The report's methods say only the prefix changed, so the label could not be confirmed. Instead F5.10 compares only the two politeness prompts with each other.
- **Klarna kept as Opening Case** despite the panel's "irrelevant once she has the point" (Maya). It carries O2 and the measures question, and customer-service examples elsewhere were already removed (blueprint D-5.7).
- **US dollar amounts in Lucía's example** (Ayşe): kept. The audience is UT Dallas students, and the figures are labeled constructed. The point is arithmetic and wording, not living costs.
- **The car example in From the Field** (Maya, Daniel: "a stretch"): kept. It is the author's own example, and From the Field must stay within the source's facts.
- **Reading time "55–60 min for Core"** (panel's estimate): the panel counted the case, the summary and the end-of-chapter items. The new two-number statement (32 min for the Core sections; 53 min for the Core package) uses the brief's definition and the agent's word count.
- **A3 "2–3 hours"** (Maya): requirements reduced and counted instead (60–70 min); see P4.
- **Sifted as a source** (expert #3): not added. The fact-checker did not open it; the same statements are covered by CX Today, heise and Entrepreneur, which were read.
- **February 2026 "two-tier model" coverage** (expert #14; fact-check): not used, because it is unverified. It is listed in the refresh rows.
- **Şeker (2014) page range [VERIFY]**: left for the author (author-only item 3).

## Waiting for the author

1. Live syllabus: R2 module 2 recommended (not required) in week 3, so the week stays ≤ 2.2 h (D-5.e). Optional: modules 4–5 instead.
2. Şeker (2014) page range (pp. 5–6 vs. p. 5).
3. Optional personal anecdote for From the Field.
4. Final voice edit (pipeline step 8). The editor never marks a chapter "done".

## Voice pass (Mode B, 2026-10-18)

A light pass with docs/voice/voice-profile.md rules 1–4:

- A breadth opening for 5.1 (lab report, marketing post, lesson plan, budget).
- A "Let's take…" walkthrough at the start of the 5.4 worked example.
- Two "In other words" restatements: 5.1, success criteria decide what "worked" means; 5.5, evidence, not proof.

No facts, numbers, citations, headings or figure references were changed in this pass.
