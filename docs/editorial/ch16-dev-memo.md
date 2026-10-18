# Chapter 16 — developmental memo (2026-10-18)

Inputs: four independent reviews run in parallel without sharing reports — subject-expert reviewer (Opus; build/ch16/reviews/subject-expert.md: 2 High, 10 Medium, 12 Low), pedagogy reviewer (Opus; pedagogy.md: 4 High, 10 Medium, 7 Low), student panel (Maya / Daniel / Ayşe, Sonnet; student-panel.md), fact-checker (docs/factcheck/ch16.csv, 159 claims: 132 supported, 25 partly supported, 1 unsupported, 1 cannot verify; ch16-sources.md) — and the editor's nine decisions of 2026-10-18, decisions D22–D24 and the newest brief rules. Draft v1 is kept in build/ch16/ch16-draft-v1.qmd. Every fact-check row now has `resolution_v2` (six rows added for claims new in v2; one stays OPEN: Shumailov et al. full text not opened, wording hedged).

## Decisions — accuracy (subject expert, fact-checker)

| # | Change | Why |
|---|---|---|
| A1 | Warm-up 3 answer: "Yes, but then it must flag a different share of the others wrongly in each group, and a flag means something different in each (16.3)"; question adds "What else would have to differ?" | Expert #1 (key was wrong: equal selection + equal miss rates are possible) |
| A2 | Check Yourself 16.3 key: the higher-base-rate group gets "a higher false-positive rate, a higher miss rate or both"; 16.3 adds the intuition, the exception "unless the tool never flags anyone wrongly" and the selection-rate clash, so the item is answerable from Core | Expert #2, #4; pedagogy #11; panel (Daniel); editor 1 |
| A3 | Deep 16.A: equal selection and equal error rates hold together only with equal base rates "or when the flags carry no information at all"; COMPAS error rates from 7,214 people; "largely about which errors matter more; the company also disputed parts of the analysis" | Expert #5, #15; fact-check C60 |
| A4 | Chance threshold defined fully ("in either direction", "when both versions truly give the pattern 50% of the time", equal runs per version); count table for 10–50 runs in 16.4 and on the station card; "no gap is not proof of no bias"; one comparison named in advance; F16.7 title and source line qualified; ch16_experiments.py adds 25, 26, 35, 45 runs | Expert #3, #24; editor 2; pedagogy #7 |
| A5 | Wilson & Caliskan: "about 85% of 27 statistical tests"; "the study tested only those names"; correction in one clause | Expert #6; fact-check C36; editor 5, 7 |
| A6 | IBM 2020 covered facial **analysis** too; "different technology" removed; Amazon's moratorium "later extended until further notice (reported)"; F16.2 box reworded | Expert #7, #22; fact-check C152 |
| A7 | Williams: six-photo lineup with his current license photo, picked by a store security contractor who had only seen the video, "according to his lawsuit"; charges dismissed January 23, 2020; link 2 "documented in the lawsuit's allegations, not adjudicated"; F16.21 link 1 solid ("False match (documented); bias inferred") | Expert #8–#10; fact-check C86, C87, C90; editor 7, 8 |
| A8 | Gonen & Goldberg: removing the "gender direction"; Raji & Buolamwini: updates "appear data-driven" (the authors' reading), named vs. unnamed companies stated without "improved more"; Gender Shades: "raise two possibilities"; 44.6% women; "existing gender-classification benchmarks"; Aspire Mirror wording; Bianchi prompt, classifier and three categories | Expert #12–#14, #17; fact-check C01, C06, C11, C44, C50, C72, C74, C79 |
| A9 | Deep 16.B: generative feedback path cited to Shumailov et al. (2024) with hedged wording | Fact-check C66; editor 7 |
| A10 | Gemini's August 2024 return cited to Google's own post (confirmed); Blodgett "commonly distinguished"; Selbst "can fail"; NYC audit content ("selection rates by sex and race or ethnicity, no pass mark") | Expert #16, #19–#21 |
| A11 | References: Amazon URL, IBM archived letter, Atari DOI, Crenshaw article number and URL, Dieterich date/type/archive, Hardt publisher, Wilson & Caliskan pages, Spector subtitle, Google (2024), Shumailov (2024), Adams (1963) added for From the Field; Hofmann, Arnett and Liang removed (no longer cited); all [VERIFY] tags closed (0 in the chapter and case file) | Fact-check reference fixes; expert #23 |
| A12 | Dashes mean only "inferred" (or "reported" with a legend): F16.1 Decide drawn solid and labeled "(2nd)"; F16.2 mask box dashed = reported, 2020 box solid gray with "Link not established" and no arrow; F16.10 legend "dashed = inferred (a lead)"; F16.21 link 1 solid | Expert #10, #11; editor 8; brief rule |

## Decisions — learning design (pedagogy, student panel, editor)

| # | Change | Why |
|---|---|---|
| L1 | **Week-12 count per D22, one number everywhere:** Core package incl. the "Words Used" box, 16.7 with the A12 fairness-row text and the Application box ≈ 3,500 words (23.3 min) + answering 7 Check Yourself (0.33 min each, Ch. 15's rate), 6 faded examples (0.5 min each) and the Warm-up (0.5 min) = **≈ 29 min**, stated as "about 30 minutes"; Core sections ≈ 16 min. Achieved by one Check Yourself per section, the A12 box merged into 16.7 (Application section now a pointer), the Summary shortened, and ~550 words cut from Core (repeated numbers, Simpson's paradox, Liang and Arnett sentences, the Telugu result moved to the Ethics Lens). Review A, B, C, Spaced Review, the Case Study and its questions labeled final-exam practice | Pedagogy #1, #19; editor 3; D22; Ch. 15 and 18 totals (≈ 131 of 132) |
| L2 | **Evidence transfer:** 16.7 states that the station documents *that tool on that prompt*; a workflow row is documented only for the same tool and kind of task; otherwise inferred + lead + the test that would document it. Elif's row transfers because the center plans to score drafts with the same tool; likelihood "medium" with its anchor reason; the heat map now moves impact and likelihood to low under reduce + avoid (F16.14) | Pedagogy #2, #13; editor 4; brief rule |
| L3 | **Inclusion:** prompt B and Elif's row test a cue that names the property, "Author's first language: English / Turkish", not "international student"; writing-center clause removed and not logged; a non-victim international student (a linguistics research assistant) in the 16.2 faded example; Deep 16.B sentence about international students rewritten; private opt-out; "never ask a classmate to speak for a group"; the name-swap evidence "covers only" White- and Black-associated names; new reading-time wording | Pedagogy #3, #20; panel (Ayşe); editor 5; brief rules |
| L4 | **Station 3 rebuilt** (labs/ch16-lab1.md; handoff "For Chapter 15"): copy-and-paste prompts, numbered printed outputs per table, one subtotal line per table with a worked line, exact-word matching rule, prompt C's comparison she vs. he fixed in advance (they reported as a lead) with 2 runs per version, A and B 3 runs, count threshold table; minutes 34–49 with the pooled reading at Lab 15.1's gallery walk (Ch. 15 v2) | Pedagogy #4–#8; panel; editor 3, 6; Ch. 15 v2 |
| L5 | A12 wording uses "the station's preregistered counting rule"; the fairness-row element list (worse error; allocation or representation; phase; likelihood and impact; marker; mitigation kind and what it might hide; owner) proposed for Ch. 15's rubric; 16.3's Your Turn is the row's "worse error" element | Pedagogy #4, #10; editor 3, 6 |
| L6 | Chance block moved from 16.2 to 16.4 (one idea per section; the Your Turn order now follows the station steps) | Pedagogy #9; editor 2 |
| L7 | "Words Used in This Chapter" box (flag, miss, gap, percentage point, tally, pooled, lead, benchmark, classifier); score, threshold, word error rate, text- and word-embedding model glossed; 16.3's numbers in one labeled table (selection 65/25 separated from precision 65.4/66.0); bias audit defined in 16.6 | Panel (all three); pedagogy #17; editor 9 |
| L8 | Review A: absolutes softened (A1, A2, A8, A11, A12); A2's "reflects the workforce" distractor replaced; keys rotate a/b/c/d (3/3/2/3) | Pedagogy #12, #18 |
| L9 | Mini-Project: time estimate (about 3 hours), "tool kind" and "contributors" defined, language-variety warning, "lead is normal at 30 runs", defect-count rubric levels without gaps, Judgment and Declaration split, LO/Bloom tag, alternative open to opt-outs with a mapping sentence | Pedagogy #14; panel (Ayşe); editor 9 |
| L10 | 16.4 faded example asks for the named comparison and runs (no longer answered in its own prompt); counting rule fits the scene; Koenecke faded supplies gender and age; 16.2 prediction asks "Could one group's error be far above 10%?" | Pedagogy #16; review row 17 |
| L11 | Check Yourself 16.7 now asks when a station result documents a workflow row; 16.2 returns to the campus-chatbot calculation | Pedagogy #2; panel (Daniel) |

## Not changed (with reason)

| Item | Reason |
|---|---|
| Core still has 16 figures in ~2,400 words (pedagogy #19) | Figures carry no reading words; F16.4 and F16.8 now replace prose lists rather than repeat them |
| "Lead" kept as the term (panel suggested "early signal") | Defined in the Words box and the two-part rule; Ch. 15's lab uses it |
| Fisher's exact test not used (expert note) | The book's threshold is a valid, conservative two-sided 5% test and easier to read from a table |
| Elif's Emily/Elif name test kept | One cue that should not matter; counts reported without any portrait of a group (editor 2 satisfied) |
| Pooled runs treated as independent fresh runs (panel, Daniel) | One tool, fresh chats, memory off; the station card says findings are re-run before anyone relies on them |
| O3 verb "Explain" kept | Blueprint O3 Bloom aligned to Understand (one verb, review row 6) |

## Waiting for the author

1. R13 recommended (live syllabus); station 3 at minutes 34–49 with the gallery-walk reading; A12 fairness row and probe; Mini-Project optional.
2. From the Field approval (equity theory, 2014), written in first person from the entry.
3. About 8 minutes for Ch. 16 on Tue Apr 13.
4. UTD check: can Copilot Chat's memory or personalization be switched off for the station?
5. Final voice edit.

## Open items (not author)

- Ch. 15 must adopt the station-3 text and gallery-walk table in docs/production/handoff/ch16.md ("For Chapter 15"): prompt B's stated-first-language cue, prompt C at 2 runs per version, the matching rule, the count table and the fairness-row elements.
- Shumailov et al. (2024) full text not opened (C164, hedged).
- F16.14 imports Ch. 15's `risk_heat_map`; re-render if its API changes.

## Voice pass (Mode B, 2026-10-18)

Light pass on Core and the Opening: shorter sentences in 16.3 and 16.4, numbers moved from prose into one table, hedges kept only where the evidence requires them ("reported", "according to his lawsuit", "the authors' reading"), first person kept only in From the Field (the author's entry). No anecdote invented; Elif's details are constructed and labeled.

## Final review (2026-10-18) — applied

All 5 must-fixes, 13 should-fixes and both nice-to-haves from build/ch16/reviews/final.md, with the reviewer's wording. M1: F16.17 note "more wrong flags, more misses, or both (unless no one is flagged wrongly)" (figure and longdesc). M2: F16.21 alt text. M3: no hardcoded figure numbers (F16.10 "the table in 16.4"; Lab 16.3 "the worked example in section 16.3"; lab card "section 16.7"; longdesc and D-16.9 say source IDs F16.7–F16.11 do not follow page order). M4: Elif's row limited to the cue tested (Turkish vs. English stated first language; other languages and names untested), marked documented for the same tool, task and cue (evidence-transfer rule); F16.14 note. M5: Ch. 15 rubric names ("Register," "Red-team record," "Plan"). S1 Warm-up 3 key with the uninformative-flags exception; S2 39/26 counts and the smaller-total rule (chapter and card); S3 counts assigned to versions, re-run before reliance; S4 item 4c adds live/printed apart and the smallest detectable gap; S5 Williams link 2 **reported**, drawn dashed with "dashed = inferred or reported"; S6 Amazon extension cited to Reuters (2021, May 18), read via syndicated copies; S7 NYC citation and reference; S8 Gemini secondary "hallucination (invented facts)"; S9 C13 wording; S10 Review C labeled, time line "A–C"; S11 F16.9 alt text; S12 C164 closed from the Europe PMC abstract (wording now states the experimental finding); S13 longdesc Raji wording. Nice: probe sheet "(printed: of 3)"; lab CSV note without a comma. Re-rendered all diagrams in color and gray; f16-10, f16-14, f16-17 and f16-21 checked visually (f16-14's arrowhead touches the "D" letter of the after-marker, a Ch. 15 `risk_heat_map` layout detail, reported to the editor). Quarto render clean.
