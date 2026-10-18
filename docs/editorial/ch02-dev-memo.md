# Chapter 2 — developmental memo (2026-10-18)

Inputs: four independent reviews run in parallel without sharing reports — subject-expert reviewer (Opus), pedagogy reviewer (Opus), student-reader panel (Maya / Daniel / Ayşe, Sonnet), fact-checker (Sonnet; docs/factcheck/ch02.csv, 89 claims: 54 supported, 27 partly supported, 4 unsupported, 4 cannot verify). The author delegated editorial choices (memory: ai4all-book-delegation), so the editor decided on the changes below and applied them in revision v2. Pre-review draft kept in the session scratchpad only.

## Decisions — accuracy (fact-checker, subject expert)

| # | Change | Why |
|---|---|---|
| A1 | Opening Case, Case Study, C02: "never relied on them alone" attributed to people familiar with the project; Amazon's own statement ("never used by its recruiters to evaluate candidates") added; "two" all-women's colleges; "Amazon edited the programs"; team disbanded by early 2017 | Fact-check C8–C12, C16: misattribution and drift from Reuters |
| A2 | What the label was is marked as the book's reasoning ("Reuters did not report…; if…") in 2.4, Case Study, Summary and F2.4d ("Possibly past hiring decisions") | Fact-check C14–C15; expert must-fix |
| A3 | "No gender column" → "nobody told the model to prefer men"; "a gender field" | Fact-check C13: Reuters does not describe the input fields |
| A4 | Experiment described exactly: logistic regression; 60 per digit, 180 in all; same test examples within each run; test set about balanced; one-direction row = 36 of the 60 eights labeled "3"; column = "Accuracy on the 8s"; mechanism ("most 8s carried the label 3") replaces "partly cancel out"; conclusion limited to "in our experiment" | Expert must-fix ×3; panel (Daniel) |
| A5 | M6 reconciled: most models keep settings, not copies; overfitted settings act almost like memorized answers; LLMs can repeat training text (Carlini et al., 2021); A10 rewritten as "most trained models" | Expert must-fix; pedagogy should-fix |
| A6 | Nested family: "today's generative AI is built almost entirely with deep learning" with a caveat; A12 key reworded | Expert should-fix |
| A7 | Self-supervised learning row in 2.2; 2.6 explains where generative AI's labels come from | Expert should-fix |
| A8 | Labels = human decisions **or recorded outcomes** | Expert should-fix |
| A9 | Proxy presented as a "close cousin" of a shortcut, with the difference (testing in new conditions will not reveal it); proxy added to the diagnosis table, O3 and the Summary | Expert should-fix; panel |
| A10 | Case Study item 1: under-represented group, not class imbalance | Expert should-fix |
| A11 | Deep 2.A: Dartmouth "term appeared in the 1955 proposal"; Deep Blue = search + hand-tuned knowledge, not modern ML; AlphaGo method cited to Silver et al. (2016), Lee Sedol match (March 2016, 4–1) to Silver et al. (2017); Transformer "most of today's LLMs as of 2026" | Fact-check C40, C47, C51; expert |
| A12 | Squire/Lusinchi stated separately (both biases jointly vs. non-response as main cause) | Fact-check C24 |
| A13 | Wald told in 2.3 (selection gap) so Check Yourself 2.3 is answerable; wording "aircraft", not "bombers" | Fact-check C28; panel; pedagogy |
| A14 | "Most errors in the field" → "Many errors in real use"; tax example replaced by a policy illustration; vocabulary "tens or hundreds of thousands" and "scoring then picking" | Fact-check C69, C72; expert |
| A15 | Deep 2.B: "training procedure measures"; **learning rate** named; "billions… some more than a trillion"; F2.14 axis "Squared error (× 1,000)" | Expert consider |
| A16 | Hana's example: the costly error is calling human work AI-made; Liang et al. (2023) on detectors flagging non-native writers | Expert consider; relevant to ESL readers |
| A17 | From the Field: 10% marked as the article's illustration; the 90% trap and "labeling decision" marked as present-day connections; involuntary-churn claim hedged as in the article; reference pages 26–29 + URL | Fact-check C82, From the Field notes |
| A18 | Ethics Lens: ghost work hedged ("often… unpredictable pay and little job security"); fraud labels cover only caught fraud | Fact-check C38; expert |
| A19 | References: Silver 2016 all 20 authors; Silver 2017, Carlini 2021, Liang 2023 added; McCarthy DOI; Krizhevsky URL; OpenAI 2022 title | Fact-check reference fixes |
| A20 | Anthropomorphic wording removed ("safe", "tempted", "does not know", "looks at", "sees", "measures") | Style sheet §1; pedagogy; expert |

## Decisions — learning design (pedagogy, student panel)

| # | Change | Why |
|---|---|---|
| P1 | Diagnosis synthesis moved to the end of 2.5 ("Putting it together"): six-problem table (proxy row added), datasheet remedy, and the **Paper Task** (Core, ~15 min, ungraded; answers for odd items in Appendix E); its predict-after-evidence step removed (the prediction stays at the start of 2.4); "one or more problems, or none"; shortcut scenario added; 2.4 now carries labels + imbalance only | Pedagogy must-fix + should-fix; panel top-2 |
| P2 | F2.6 cut: it duplicated the table (redundancy principle); table kept because it is accessible and searchable | Pedagogy should-fix |
| P3 | Defined in Core: feature, class, error, training data = training set, parameter, worked definition; "rules = patterns stored in settings"; why steps are small; recall named in 2.4 | Panel top-1; pedagogy must-fix (A2 pool) |
| P4 | A2: pool = Chapter 2 Core Key Terms (any Core Key Term counts); overlap rule (counts once); every term linked, ≥14 links; rubric split into Links 1.5 + Definitions 1.5 with parallel levels; five declaration elements listed; integrity issues left to course policy; **alternative assignment** (audit a dated AI glossary) with the same rubric read another way; time estimate; "the glossary" → "the chapter's own definition or a cited source" | Pedagogy must-fix ×2; panel |
| P5 | Review A: shortcut item (A14) and datasheet item (A15) added; distractors in A1, A5, A10, A12 rewritten from M1–M7 without absolute giveaways; B3 new context (crop yields); several Bloom/objective tags corrected | Pedagogy should-fix |
| P6 | Spaced Review: one pure Chapter 1 retrieval item; answer removed from the stem of the generation item | Pedagogy should-fix |
| P7 | Lucía's faded example now has one rule and its failure filled in; résumé faded example has Q1 filled in | Renkl (2014) fading |
| P8 | Time statement: ~30 min reading (longer for ESL readers) + ~15 min paper task; box types explained once | Panel; pedagogy |
| P9 | Feedback stage of the pipeline explained in 2.2; loop vs. decision trees reconciled (2.2, 2.5) | Pedagogy consider; expert consider |
| P10 | Warm-up revisit gives the short answers | Corrective feedback |
| P11 | ESL wording: "opens the box", "brittle", "landslide", "flash of insight", "carried the same tilt", "shortest path" replaced; Landon described as "the challenger"; bolts/nuts/washers glossed | Panel (Ayşe); pedagogy |
| P12 | 2.7 worked definition fixed (test set = photos held back, not the workbench); F2.13 and F2.14 captions state findings | Pedagogy consider |
| P13 | Lab 2.2 runs specified in numbers matching the book's experiment (18 of 90 labels); background run defined; "repeat one run" added; Lab 2.3 privacy step uses settings/help pages instead of legal terms | Panel (Daniel, Ayşe) |
| P14 | Case Study and Case Study Question 1 use the figure's stage names (Collect data / Label / Train); CSQ2 and CSQ3 reworded to match what Reuters reports | Pedagogy should-fix; expert |

## Not changed (with reason)

- The Amazon case appears in the Opening Case, 2.3 and the Case Study: the Opening Case poses the puzzle, 2.3 answers it, the Case Study maps it to the pipeline. Kept; 2.4 now refers to it only through the hedged label example.
- Overfitting chart (test accuracy levels off rather than falls): kept as real data; the text now says a growing gap is the warning sign and that test accuracy sometimes falls.
- No tool named in the labs (tool-neutrality rule); Compass pages carry current tools.
- [COMPASS: …] placeholders stay until the Compass MVP, as in Chapter 1.

## Waiting for the author

1. Live-syllabus proposals from the blueprint: list Chapter 2 before Tue Jan 26; Amazon case in Tuesday's opening slot; 2–3 Chapter 2 concept-check items (the Paper Task now says it prepares students for "the week's concept check").
2. Final voice edit (pipeline step 8) — the editor never marks a chapter "done".
3. Dependency: A2 (due Feb 1) needs the Chapter 3 term pool — set in the Chapter 3 blueprint (editor's next task, not the author's).

## Final review (2026-10-18) — applied

The final reviewer (Opus, independent) found 16 must-fix and 19 should-fix items. Applied: remaining fact-check partial findings (C03 opening wording, C05 "male dominance across the tech industry", C17 workforce context, C21 "largest polls" removed, C24 short case 1), "trillion" removed, wolves/huskies item made explicitly hypothetical, **Hana's pronouns corrected to they/them**, chapter cross-references (Ch. 16 bias and fairness, Ch. 11 data work, Ch. 18 governance), AI and AI4K12 defined at first use, remaining anthropomorphic verbs, citations for the symbolic wave (Russell & Norvig, 2021) and for layers and "why now" (Goodfellow et al., 2016), lab files synced with the chapter, disclosure aligned with the approved front-matter statement (D16), Reuters' watered-down version and new team added, Opening Case expanded, two Further Reading items, glossary synced, longdesc keyed by source ID, all alt texts ≤ 150 characters and identical to the longdesc table, "flat" → "apartment", F2.9 title "about 6 / about 23", F2.13 Dartmouth label, F2.15 "large language models", Paper Task item 6 keyed as a non-example, optional Mini-Project added, blueprint line updated. v2 additions sent to the fact-checker (docs/factcheck/ch02.csv, resolution_v2 column).

Not applied (with reason): serial commas outside the listed lines (style sheet is silent; Chapter 1 mostly omits; left to the copyedit at production); HTML comments (stripped by the production build, as in Chapter 1); framework references in the Learning Objectives (same treatment as Chapter 1; to be added for all chapters together); Appendix F (does not exist yet; tracked in docs/status.md).
