# Chapter 8 — developmental memo (2026-10-18)

Inputs: four independent reviews run in parallel without sharing reports — subject-expert reviewer (Opus; 20 findings, verdict "revise before release (minor)"), pedagogy reviewer (Opus; 21 findings, 6 high), student-reader panel (Maya / Daniel / Ayşe, Sonnet), fact-checker (Sonnet; docs/factcheck/ch08.csv, 139 claims: 108 supported, 25 partly supported, 1 unsupported, 1 outdated, 4 cannot verify), plus the editor's nine decisions settling conflicts between them. The author delegated editorial choices (D19), so the chapter agent applied the changes below in draft v2. Draft v1 is kept in build/ch08/ch08-draft-v1.qmd.

## Decisions — accuracy (fact-checker, subject expert)

| # | Change | Why |
|---|---|---|
| A1 | The lawyer's questions to ChatGPT ("Is Varghese a real case") are no longer placed before the filing. Opening Case: "At some point he also asked… His own accounts of when he asked differ, and the court found them inconsistent (¶¶ 46–47)". Puzzle reworded: "When the lawyer asked the tool whether the cases were real, it said yes." Same treatment in 8.3, the Case Study, C05 and the keys | Expert #1 (high); fact-check #5; editor decision 1. The record leaves the timing disputed |
| A2 | The replies named Westlaw, LexisNexis and the Federal Reporter (each glossed), not "standard legal research databases"; "the Federal Reporter" replaces "the official reporter" | Fact-check #5, #10 |
| A3 | "Searched for 'Varghese', could not find it, and cited it anyway (¶ 12)": "on a free case-law website" removed from text, figure F8.4d and C05 | Fact-check #4 |
| A4 | "Most of the cases" (¶ 7), "response to that motion" (¶ 5), "ECF 55, pp. 1–2" (filing date on p. 2); F8.2 retitled "from a court filing to a sanctions order" (the output's date is not in the record) | Fact-check #1–3, #6 |
| A5 | Ethics Lens: "took the lawyer seconds" → "a few prompts (¶ 39)" | Fact-check (the one unsupported claim) |
| A6 | Case Study: ¶ 23(a) for the March 1 filing (the signer read none of the cases) and ¶ 23(b) for the April 25 affidavit; the AI-produced excerpts are a **warning signal** that should have triggered stage 1, not a stage-1 check | Expert #2; pedagogy #12; editor decision 4 |
| A7 | Stage mapping and the two-index rule applied to the case: one empty search *flags* "Varghese"; a second index makes it unsupported; stage 2 (the court's records, the Federal Reporter citation and docket) makes it contradicted. The clerk's confirmation moved from "expert" to stage 2 in F8.4d; stage 3 "not needed" | Expert #3, #15; pedagogy #6; editor decision 4 |
| A8 | Min et al. (2023): checked "against Wikipedia"; "not supported" is not the same as false; facts later in an answer and about less famous people were supported less often; "tells you little about the fourth sentence" marked as the book's reading; 8.4 signal 4 cites the same finding | Expert #4; fact-check #7; editor decision 7 |
| A9 | Deep 8.A distinguishes index-matching checkers (no AI model; part of stage 1) from AI checkers (a signal, not a stage) | Expert #5 |
| A10 | Consistency check caveats: temporary chat or memory off; web search can return the same wrong page; Farquhar et al. catch answers that vary, not repeated errors; the "same wrong answer" point is labeled as weaker evidence rather than stated as a finding | Expert #6; fact-check #15 |
| A11 | 8.5: Xiong's five models were tested in 2023; SimpleQA's questions were chosen to be hard for GPT-4 and its plots cover four OpenAI models; one sentence on post-training miscalibration (OpenAI, 2023, recalled from Ch. 4). Deep 8.B: Kadavath's good calibration was mostly before chat training; ECE depends on binning and is noisy at 30 answers; calibration ≠ usefulness; weighted average "about 31 points"; the opposite size trend for language models noted | Expert #7, #10–13; editor decision 3 |
| A12 | "Newer tools often do better, though not always": OpenAI's April 2025 system card (o3 33%, o4-mini 48% vs. o1 16% on PersonQA) | Expert #8; editor decision 7 |
| A13 | NASBA defined and described as running the exam together with the AICPA (both expanded); AUD/FAR/REG named and cited to the TSBPA scoring page; AUD, BEC, FAR, REG spelled out | Expert #14; fact-check #8; panel |
| A14 | 22 TAC § 511.80 cited as amended effective June 3, 2026 (30-month section credit unchanged) | Fact-check (outdated) |
| A15 | Kohls: errors "apparently" from GPT-4o (p. 3); the court did not fault the use of AI, only the unchecked citations (pp. 8–9); leave to amend "denied as moot", with *moot* glossed; the leftover blank removed (moved to Case Study Question 4) | Expert #20; fact-check #12 |
| A16 | Reading list: the *Inquirer* ran "a 56-page summer supplement" from the same company (reported); "would have flagged the invented titles", marked as the book's inference; attribution tiers used | Expert #19; fact-check #13; brief (attribution tiers) |
| A17 | From the Field: "first come gets higher attention" presented as a design problem the paper described (Sec. V.B), not a measured result; no "far more often"; the box opens with its link to the expert stage | Fact-check #14; panel |
| A18 | Charlotin scope: "filings that relied, or were alleged to rely, on AI-generated content that was false" | Expert #18 |
| A19 | 8.6 claim 5 now has its own verdict: contradicted (failure 3: the blueprints describe the new structure); the [VERIFY] resolved (AICPA & CIMA blueprints, editions effective Jan 1, 2026 and 2027) | Expert #17; pedagogy #9; panel top 1; fact-check #11 |
| A20 | "Any wrong detail that stops a reader from finding the work makes it contradicted *as cited*" (8.3), so the Enron faded key is unambiguous | Expert #16 |
| A21 | References: Bell and Mihalopoulos titles corrected; AICPA FAQ title and date; PCAOB URL; Ji et al. (2023), OpenAI (2023), OpenAI (2025), TSBPA and AICPA Blueprints added; Magesh issue number | Fact-check #16 |
| A22 | Career Connection softened ("often", "help people", no tool-specific claims); PCAOB expanded | Fact-check (cannot verify) |

## Decisions — learning design (pedagogy, student panel)

| # | Change | Why |
|---|---|---|
| P1 | Calibration aligned with Chapter 7: "Calibration (of your own confidence)… how closely your confidence in your answers matches how often they are actually correct, across many answers" (the last clause added in the final-review pass, FR2); "Calibration (of a model)… how closely a model's stated confidence matches its accuracy". Spaced Review "two meanings, one habit: predict, then check" | Pedagogy #2 (high); editor decision 3 |
| P2 | One A5 gap formula (8.5, A5 item 6, glossary): average confidence of claims rated 80% or higher minus the share of them supported, leaving out not-checkable and cannot-verify rows and counting "partly supported" as not supported; "if fewer than two qualify, say so". The tool must give a stated percentage (one prompt for all ten). Modeled in 8.6 (Lucía's 36-point gap); the 8.5 faded table now has an "average stated" column and a blank gap; the 8.6 faded row has a blank tool gap | Pedagogy #4 (high); expert #9; panel top 3; editor decision 3 |
| P3 | Overconfidence label for Mata kept documented, with the reason stated: before checking, a firm answer is no evidence either way; after the record showed the cases false, the flat assertion when asked directly is certainty beyond the evidence (¶¶ 45, 47). 8.4 no longer calls ¶ 45 pushback; the pushback test is glossed (it challenges an answer you know is correct) and, on an unchecked claim, a flip is a warning while holding firm is no evidence | Pedagogy #3, #16 (high); fact-check #9; editor decision 2 |
| P4 | Citation checks mapped to stages in 8.3: checks 1–2 use an index (stage 1); check 3 opens the work (stage 2). Verdict meanings sharpened: unsupported = "no evidence for it at the stage you reached: nothing found, or the source does not say it"; cannot verify = "the evidence exists or may exist, but you cannot reach it" | Pedagogy #6, #10 (high); editor decision 4 |
| P5 | Review A rotated (keys c, a, d, c, d, a, b across the multiple-choice items) and distractors tied to misconceptions; a new M5 item (A13); A11 turned into a scenario. v2 still had four items whose key was the longest option, one absolute (A13(d)) and one distractor with no misconception (A9(b)); fixed in the final-review pass (FR3) | Pedagogy #5, #19 (high); brief (multiple-choice rule); editor decision 6 |
| P6 | A5 rubric rewritten: each criterion lists its requirements and the levels count shortfalls (all / one / two / three or more), so the levels are parallel and have no gaps; the O5 label is scored under Verification; the declaration and reflection are scored together under Declaration and judgment | Pedagogy #15; editor decision 6 |
| P7 | Your Turn 8.1 asks for both confidences (the tool's in one prompt) and the saved transcript; Your Turns 8.2–8.5 each produce a two-minute A5 entry (stage plan, check 1 on one citation, signals column, 80% marks). Row 1 is checked in Lab 8.1 Part 2, not at home | Pedagogy #7, #8; editor decisions 5–6 |
| P8 | Pre-lab: "about 250 words, one number or date, two sources"; save the transcript; an eLearning sample route for students without a tool; six field samples for the alternative assignment | Pedagogy #14, #21; panel; editor decision 6 |
| P9 | Time statement: two numbers (Core sections ≈ 24 min; whole Core package ≈ 38 min), Your Turns ≈ 18 min, A5 at home ≈ 37 min estimated item by item; reflection 60–100 words; three-run check optional; Kohls and the reading list marked recommended; R5 in Further Reading. **Week 5 counts at ≈ 2.4 h, a documented one-week exception (W1, D-8.10); A5 verifies eight of its ten claims** | Pedagogy #1 (high); panel; brief (time and workload rules); editor decision 5 |
| P10 | Lab 8.1: briefing excerpts cut to ¶¶ 12, 26, 45 on a glossed handout; team check 10 min; a 5-minute buffer; the lab-checked claims count toward the primary-source minimum. Lab 8.3 aligned with its file (own predictions, temporary chats, gap method). Lab types "Check It"/"Break It" explained | Pedagogy #13, #20; panel; editor decision 5 |
| P11 | Glosses at first use: docket, ECF, ¶, sanctions, bad faith, gatekeepers, Westlaw/LexisNexis, Federal Reporter, retrieval, misgrounded, benchmark, stakes (now a Key Term), moot, pushback test, A4, Pub. L. No., ksi/MPa/ASTM, AUD/BEC/FAR/REG, NASBA, AICPA, PCAOB; "Signature 4" removed from the caption; "the fourth sentence" | Pedagogy #11; panel top 2; brief (glossing rule); editor decision 8 |
| P12 | Examples: a marketing example (market share) and a non-US example (Statistics Canada; a university's fee page in another country) in Core; Check Yourself 8.1 Q2 gives the expected count (four) | Panel; editor decision 8 |
| P13 | Warm-up 1 reworded ("Does that show that the paper exists?"); the Summary answer gives both rates (55% GPT-3.5, 18% GPT-4) | Panel top 4; editor decision 8 |
| P14 | Prediction moved into a "Predict" callout; F8.3 retitled "One fluent paragraph held six separate claims to check" and its six claims listed in the text; the faded quotation example has its first step filled; Check Yourself 8.6 has a "why" item | Pedagogy #17–19; brief (faded rule) |
| P15 | Spaced Review: one Chapter 4 item replaced by a Chapter 3 item (retrieval can still yield an unsupported claim) | Pedagogy #21 |
| P16 | Opening Case opens with the hook (fake decisions), then a two-line guide to the record, then the procedure | Panel (Maya) |
| P17 | Faded-example answers published in Appendix E | Panel (Daniel); editor decision 8 |

## Not changed (with reason)

- **F8.5 kept next to the numbered list in 8.3** (pedagogy #17 suggested letting the figure replace the list). The list carries the checks and the stage mapping in accessible text; the figure carries the Mata examples. Both are short.
- **Mata stays the opening case despite its legal background** (panel, Ayşe). It is the syllabus's R6 case; v2 adds a guide to the record and glosses every legal term instead.
- **The CPA exam stays Lucía's running example** (panel, Maya). It follows her fixed details (saving for the CPA exam); the marketing and non-US examples were added instead of replacing it.
- **Overconfidence label kept "documented", not changed to "inferred"** (pedagogy #3 offered either): the editor chose documented with the stated reason (decision 2).
- **Lab 8.1's provided output is still a placeholder** (panel). It must be a real, dated output generated shortly before the term; it is listed in the Instructor package.
- **Ten claims kept** in A5's list (syllabus: "ten claims"); eight are verified (editor decision on D-8.10); see W1.

## Workload (W1)

Counted at 150 words per minute and by requirement. The editor's decision on D-8.10: A5 lists ten claims but students verify eight (the other two get one line, "not checked" and why); Chapter 4 stays unchanged (its short case 1 is assessed). Chapter 4 ≈ 47 min (its whole Core package plus its Your Turns, as its D-4.7 counts; the Failure Diary moved to the Mar 12 checkpoint; R5 recommended). Chapter 8 ≈ 96 min: whole Core package 38, pre-lab 5, Your Turns 18 (all A5 work), A5 at home 37. **Week 5 ≈ 143 min ≈ 2.4 h**, recorded as a documented one-week exception (handoff D-8.10; book decision D21, updated by the editor) and stated in the chapter's time line.

## Waiting for the author

1. Live-syllabus wording for week 5: R6 read in the lab briefing; R5 recommended; the A5 brief; the Tuesday demo's "checking them live" (Chapters 4 and 8 move the checking to Thursday).
2. Live-syllabus note for A5: ten claims listed, eight verified; week 5 about 2.4 h (D21).
3. Optional From the Field addition from your own editorial or SME work (never constructed).
4. Final voice edit (pipeline step 8); the agent never marks a chapter "done".

## Voice pass (Mode B, 2026-10-18)

Light pass with docs/voice/voice-profile.md rules 1–4: a breadth opening for 8.1 ("Whatever your field…") and for the Ethics Lens ("Every field that publishes claims…"); the constraint-first opening of 8.2 kept; "Let's take…" walkthroughs in the 8.1 and 8.4 worked examples; "For example" with two fields in 8.2's primary-source paragraph (a news story about a study; a university's fee page abroad); "In other words" restatements after the stakes list (8.1) and the consistency-check paragraph (8.4). No facts, numbers, citations, headings or figure references were changed by the voice pass. The author's final voice edit is still pending.

## Final review (applied, 2026-10-18)

The final reviewer (Opus, independent; build/ch08/reviews/final.md) found 5 must-fix, 12 should-fix and 6 nice-to-have items. All applied, with the editor's decisions:

| # | Change | Review item |
|---|---|---|
| FR1 | docs/factcheck/ch08.csv: `resolution_v2` column added to every row (resolved wording or "OPEN: reason") and rows added for the claims new in v2 | M1 |
| FR2 | Own-confidence calibration quoted with ", across many answers" (Chapter 7's v2 clause); model sense kept as "how closely…"; the editor changes Chapter 7's model clause from "how well" to "how closely" (handoff D-8.7) | M2; editor decision |
| FR3 | Review A: A5, A7, A10 keys shortened so the key is no longer the longest option (A2 alone remains, within the rule); A13(d) without an absolute; A9(b) now M2 (a link is a pointer); Appendix E and private keys and rationales updated | M3 |
| FR4 | F8.13 legend "shaded = the verdict"; re-rendered in color and gray | M4 |
| FR5 | Mata's overconfidence evidence restated with the reviewer's wording (an affirmation of reliability and, as reported, insistence after a direct question; a plain wrong answer would be hallucination only) in the Case Study, C05 and the keys; D-8.9 reworded | M5; editor decision |
| FR6 | Week 5 stated as about 2.4 h (Chapter 4 counted at 47 min with its Your Turns); diary date corrected to the Mar 12 checkpoint | S1; editor decision |
| FR7 | 8.5: the OpenAI (2023) result described as GPT-4's internal answer probabilities, not stated confidence | S2 |
| FR8 | 8.5 adds the "not checked" exclusion and one sentence contrasting A4's and A5's arithmetic; the merged calibration-gap glossary row in the handoff ("same idea", per the editor) | S3; editor decision |
| FR9 | Glosses: AUD/BEC/FAR/REG expanded at first use (8.1); ECF expanded; "frequently asked questions page"; "affidavit (a sworn written statement)"; hallucination and outdated information glossed with the glossary wording at first use; figures say "the federal appeals court's clerk" and "(federal court, New York, 2023)"; alt text and longdesc updated to match | S4 |
| FR10 | Pre-lab names Microsoft Copilot Chat (as of October 2026) as the university-provided tool | S5 |
| FR11 | Opening Case cut below 600 words: the Charlotin paragraph moved to the Ethics Lens; the "check every fact" sentence deleted | S6 |
| FR12 | Labs refer to figures by title, not source IDs; Lab 8.3's unsourced sentence replaced with a dated, cited one; Lab 8.1 step 3 "if they reach the primary source" | S7, S11; nice-to-have |
| FR13 | 8.6: "Of her ten A5 claims (the six above plus four from the rest of the output)…" | S8 |
| FR14 | Bell attributed as chief executive of Chicago Public Media, which owns the newspaper | S9 |
| FR15 | Memo rows P5 and P14 corrected | S10 |
| FR16 | Appendix E headings "(model answers)" and "(scoring guidance)"; faded-example block first | S12 |
| FR17 | Nice-to-haves: "asks the tool to state its confidence"; A3, A14 and Check Yourself 8.3 Q2 reworded so they no longer duplicate each other; small trims in 8.1 and 8.5; NASBA and PCAOB spelled out as group authors in the references | Nice-to-have |

Not changed: chart fonts below 13 px in the matplotlib charts (book-wide production item, as in Chapter 2; left to the editor). "AICPA & CIMA" kept as the group author because that is how the publisher names itself on the pages cited. 8.1 and 8.2 remain about 3–5% over their caps by this agent's count (headings and box titles included); no further cut without losing a required gloss.
