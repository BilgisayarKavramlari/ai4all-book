# Chapter 17 — developmental memo (2026-10-18)

Inputs: four independent reviews run in parallel without sharing reports (build/ch17/reviews/): subject-expert reviewer (Opus; 2 High, 9 Medium, 12 Low; reran every simulation byte for byte), pedagogy reviewer (Opus; 4 High, 9 Medium, 9 Low), student-reader panel (Maya / Daniel / Ayşe, Sonnet), fact-checker (Sonnet; docs/factcheck/ch17.csv, 153 rows: 116 supported, 30 partly, 2 unsupported, 1 outdated, 4 cannot verify). Editor decisions 1–9 (coordinator message, 2026-10-18). Chapter revised from v1 to v2; build-outs, figures, handoff and fact-check log updated. Nothing committed.

## Decisions — accuracy (expert, fact-checker; editor decisions 1, 2, 4, 5, 6)

| # | Change | Why |
|---|---|---|
| A1 | **Surrogate fidelity framed with its trivial baseline** (17.5 worked example, three questions, F17.10, Review A9): "a rule that rejects everyone already agrees with the model on 73.4%"; the one-question tree did exactly that (0% of approvals); two questions 82.4% but half of approvals (50%); four 85.2% (64%). Added to ch17_experiments.py and data/ch17_fidelity.csv as extra columns of the same run | Expert High 1; editor 1 |
| A2 | **Occlusion share tied to its baseline** (17.3 Step 2–3, F17.8 title and source line): "measured against an average-gray pixel"; one sentence on baseline sensitivity (13.5% black … 84% light; order can reverse); "the test in Step 1, not the map, settles the question". New data/ch17_baseline_sensitivity.csv | Expert High 2; editor 1 |
| A3 | **Ring-position share computed, not asserted:** 88% of the retrained model's background evidence vs. 18% before (shifted nut/washer ring positions); new column in data/ch17_occlusion_summary.csv | Expert Medium; editor 1 |
| A4 | **Counterfactual numbers exact:** debt ratio 0.285 → 0.276 (−0.009), not "one hundredth"; "a change smaller than the second decimal place could flip it"; a one-band age change also flips the applicant (0.41 → 0.59). F17.9 redrawn with both probabilities | Expert Low/Medium; editor 1, 3 |
| A5 | **Age is not called immutable:** "cannot be changed at all: birthplace, a past bankruptcy; change only with time and not by choice: an age band"; A7 key, CY 17.4 key and F17.9 aligned | Expert Medium; editor 3 |
| A6 | **AP report read** (build/ch17/src/ap_2020.pdf; the earlier file was a 245-byte rejection stub). Confirmed tier now: model since 2013; scorecard points summed into a 0–1 score; top scores to hand checks, the rest automatic; the staff member could not see which indicators produced a score; a high score could delay payment and bring an evidence request; the discrimination conclusion (pp. 14–16, 50). Opening, 17.1, Case Study, F17.2, F17.4, F17.5, F17.19, F17.20 and the case file updated | Fact-check C10, C81, C83; editor 2 |
| A7 | **AP fine sentence** exactly as the fact-checker gives it (Minister of Finance as controller; €2.75 million; decision of November 25, 2021); confirmed; AP (2021) reference added | Fact-check C90; editor 2 |
| A8 | **Inquiry scope** stated per p. 11 (what ministers knew of the harsh fraud approach and why it lasted; nationality-based risk profiles outside its remit); the cabinet's resignation marked reported (Amnesty p. 14) in text and F17.2 | Expert Medium; fact-check C11; editor 2 |
| A9 | **Three readings of the citizenship indicator:** the AP (discriminatory; racial discrimination not sufficiently shown, pp. 48, 50), Amnesty (racial profiling, pp. 18, 20), the government's reply (p. 16) | Fact-check C88; expert; editor 2 |
| A10 | **C-203/22 box:** names Art. 15(1)(h) (the right of access) and "a person subject to automated decision-making"; point 2 covers other people's data as well as trade secrets; the 2017 positions labeled as the pre-2023 debate; Art. 86 stays out (note to Ch. 18 in the handoff); TRAIGA spelled out as a pointer | Expert Medium; editor 4, 6 |
| A11 | **Lapuschkin** described as in the paper (Fisher-vector classifier, PASCAL VOC, source tag in about one in five horse photos, removal test, deep network not fooled) | Fact-check C31; editor 2 |
| A12 | **Chest X-ray faded example:** markers "differed between the data sources"; "performance dropped by about half on images from new hospitals" | Fact-check C37 |
| A13 | **Chen et al.:** "somewhat contrived … multiple-choice questions only, and one kind of behavior, using a hint"; cited as the arXiv paper (arXiv:2505.05410) | Fact-check C58, C121; editor 2 |
| A14 | **Apple Card short:** the NYDFS report itself cited (URL added); "found deficiencies in customer service and transparency, and said that explaining credit terms supports consumer trust"; "opacity still caused confusion and complaints"; "no unlawful discrimination" | Fact-check C95, C96, C136; editor 2 |
| A15 | **Rudin's scope:** "strongest for structured data … her own group has built some for images (Chen et al., 2019)"; key updated | Expert Medium; fact-check C26; editor 5 |
| A16 | **From the Field:** "independently of one another, ignoring how the features relate" (manuscript wording), not "one at a time" | Expert Medium; editor 4 |
| A17 | **Smaller wording fixes:** "the authors, writing in a law journal" (Wachter et al.); "a more transparent model" (not "simpler"); saliency maps also as sensitivity to tiny changes; SHAP shares the difference from an average output; baseline sentence cites Sturmfels et al. (2020); "about 0.004 on average" and method choices; F17.19 tag "(the book's reading)"; Ethics Lens paraphrase per Amnesty pp. 27–28; system cards and the Dutch algorithm register dated and sourced | Expert Low; fact-check C28, C39, C54, C67, C68, C97 |
| A18 | **References:** Chen et al. as the arXiv paper; Korbak et al. in APA 7 form (19 names … Mikulik); ECLIs for both CJEU cases; Regulation 2026/1744 full title; EUR-Lex URLs for the GDPR and the AI Act; Turpin pages; NYDFS URL; Bansal and Poursabzi-Sangdeh pages instead of unconfirmed article numbers; UNESCO (2024); Dakan & Feller in the book-wide form; AP (2020), AP (2021), Government of the Netherlands (n.d.), Sturmfels et al. (2020) added | Fact-check C03, C118–C152; editor 2 |

## Decisions — learning design (pedagogy, student panel; editor decisions 3, 7, 8)

| # | Change | Why |
|---|---|---|
| P1 | **17.2 Your Turn** now practices 17.2's own skill (glass box vs. black box: could the person redo the reasoning?); the classification item moved to 17.4, after global/local and counterfactual/example-based are defined; "glass box" defined in 17.2 | Pedagogy H1, M3; editor 7 |
| P2 | **Report rubric:** five parts throughout (Proficient "all five parts"; Developing "three or four"); the judgment is now submission item 6 with 3 minutes; report "about 75 minutes (65–90)" in the chapter, blueprint note and handoff; own-decision route +15–20 minutes; alternative states who it is for, ~70 minutes, packet under 1,000 words, how "no AI tools used" is scored, sample submission | Pedagogy H2, H3, L8; editor 7 |
| P3 | **17.8 faded key rewritten** from the record only, with one unknown and the contest line marked as not yet published (65 words); Sam's explanation word count corrected to 93 | Pedagogy H4, L4; fact-check C77, C78; editor 7 |
| P4 | **Facts supplied:** Chapter 2's pipeline stages printed in the 17.3 faded example; Chapter 8's verdict scale printed in the 17.6 faded example | Pedagogy M1, M2; editor 7 |
| P5 | **Lab 17.1 is a one-change test** (both versions ask for step-by-step reasoning); Sam's worked example matches. Honest lab times: ~45 / 25 / 25 / 20 minutes including reading and debrief; card extracts ~200 words, scenario cards ~150 | Pedagogy M4, M5; editor 7 |
| P6 | **O2** now covers 17.2: "classify an explanation by its source (the model's own logic or an approximation), scope and kind" | Pedagogy M6; editor 7 |
| P7 | **Review A:** every distractor tied to a named misconception, one hedged distractor per item, A12(a) no longer contradicts the stem; key longest only in A6 and A8; A1, A5, A9, A11 now new instances (similarity score; grammar tool; 90% fidelity vs. a 10% acceptance rate; a dataset document) | Pedagogy M7, L7 |
| P8 | **Lab 17.3 rebuilt:** student file has no points columns (the local explanation is computed); a past record that cannot be changed (bankruptcy before 2020) added; "smallest" = fewest bands; "cost the most points" defined; key in private/ | Pedagogy M8; panel; editor 3 |
| P9 | **Fast route repaired:** includes the Warm-up; the Summary replaces "link 2" with a plain sentence; 17.8 recap is a glossed list defining faithful, plausible, fidelity and the other terms; "faithfulness record" defined in prose before the faded example; five parts mapped to the layers | Panel top fixes 1–3; pedagogy L1, L2, L6; editor 8 |
| P10 | **Second-language glosses:** contest (first page), state secretary, inquiry, regulator, the "confirmed / reported" tiers in 17.1; "question the reason, only the person" rewritten; "overloaded them" rewritten; Lab 17.2 adds "not applicable" for datasheet fields | Panel (Ayşe, Daniel); editor 8 |
| P11 | **CSQ2 retagged O5**; CSQ4 asks for all three readings; CSQ5 says "discrimination found and not found" | Pedagogy L7 |
| P12 | **A12 transparency row:** "about 10 minutes; it replaces the fifth any-lens row, so week 12 gains no time"; evidence-transfer rule stated; Sam's row inferred, naming the test that would document it | Pedagogy L9; brief; editor 2 (earlier) |

## Workload (counted at 150 wpm from the v2 text)

| Route | Words | Time stated |
|---|---|---|
| Fast route (page, Opening, Warm-up, 17.1, 17.8 with recap, Summary) | ~3,350 | about 22 minutes |
| Full route (page through Case Study) | ~9,180 | about 61 minutes |
| Full route with Ethics, Career, From the Field, Summary | ~10,500 | about 70 minutes |
| Labs | — | about 45 / 25 / 25 / 20 minutes, optional |
| Report | — | about 75 minutes (65–90), optional |

The editor's note asked for "about 57 minutes" for the full route; the v2 text counts to about 61, because the accuracy fixes added words (AP facts, baselines, the three readings). The chapter states the counted number, never a lower one. Week-12 required time added: 0 (D22).

## Not changed (with reason)

| Item | Reason |
|---|---|
| Example word caps exceeded (pedagogy L5: Sam's sorter ~250 words) | The worked example now carries the baseline caveat and the ring-position number that the expert required; trimming them would reintroduce the plausible-but-unfaithful framing. The route total is stated honestly |
| "Partly" encoded as a dotted frame, not hatch (expert Low) | Dotted is labeled and is not a dash; hatch is reserved for risk in the book's grammar |
| Optional 2026 clause on hint acknowledgment (expert Low, arXiv 2603.22582) | Not verified in this pass; the dated box already says methods and results change |
| Dashes in imported F17.5 (`decision_roles`) and F17.14 (`verification_funnel`) | Imported signatures are not redrawn; listed for the editor's design pass (editor decision 9) |
| Lee & See (2004) paraphrase (fact-check C14, cannot verify) | Labeled "after Lee & See"; the final review can confirm the phrase |
| Page ranges for Lundberg & Lee and Wachter et al. 2018 (C133, C150) | Commonly cited ranges; not confirmed by an API; kept and logged OPEN |
| Recorded read-aloud as an alternative response mode (pedagogy note) | Left to the instructor; the report's read-aloud step already allows it |

## Waiting for the author

1. HermAI: approval with D16; founder wording (C105); publication status; whether the book may note the manuscript's example counterfactual (author-only item 1).
2. Live syllabus week 12: "Ch. 15, 16, 18 (D: Ch. 17)" (C02).
3. Final voice edit.

## Voice pass (Mode B, 2026-10-18)

Light pass per voice-profile §10: breadth openers added to 17.3 ("Builders, auditors and the people affected …") and 17.5 ("In medicine, lending and hiring …") and 17.7 ("Hospitals, lenders, city halls and AI providers …"); "For example" before the Lapuschkin case; "In other words" restatements in 17.1 and 17.3. No anecdote, humor or opinion added. The author's From the Field section keeps his first-person framing and the D16 disclosure.

## Build-outs updated

figures/scripts/ch17_experiments.py (v2 reports; meta file), ch17_charts.py (F17.8, F17.10), ch17_figures.py (F17.2, F17.4, F17.5 notes, F17.9, F17.19, F17.20); all 22 figures re-rendered in color and gray and checked visually from gray previews; labs/ch17-lab1–4.md; cases/C14-dutch-childcare-benefits.md; figures/longdesc/ch17.md; private/ch17-answers-even.md (keys, scorecard key); docs/production/handoff/ch17.md (Appendix E, decisions, refresh rows, author items, instructor package); docs/factcheck/ch17.csv (`resolution_v2` for all 153 rows; 8 new rows C154–C161; 7 OPEN). Quarto render of the chapter (standalone copy, HTML): 22 figures, 0 unresolved cross-references, no warnings.

## Final review (2026-10-18) — applied

All 3 must-fixes, 16 should-fixes and 5 nice-to-haves from build/ch17/reviews/final.md applied with the reviewer's wording: Opening title "A Score Without Reasons" (and the case file title); "used several dozen indicators" (chapter and case file); the Summary's parents sentence marked as this book's reading; F17.18 tag and alt cite the AP's 2020 report; case file "Consequences (by tier)", "self-learning" attribution, file ids; F17.17 adds item 6 (judgment) and renumbers the declaration; F17.22 without step arrows; Lab 17.1 "about 45 minutes" (lab, chapter, D-17.8, this memo); recap's fidelity definition limited to surrogates; alternative assignment "surrogate-based explanation"; TRAIGA no longer cited as a source; Molnar (2022) added; reference list sorted; hermai's PyPI version moved to the present-day connections; Appendix E CSQ5 and A9 wording; D-17.4 −0.009; Sam's sorter "had come to rely on" and "is trained to"; lab intro punctuation; A04 key tie (income or months); F17.13 note "somewhat contrived"; fact-check C107, C108, C152 updated; C14, C133, C150 closed as accepted at final review (4 OPEN remain: C02, C105 author-only; C76 by design; C80 refresh row); "(reported)" on the Amnesty transparency sentence; "See 'How This Book Was Written.'" after the D16 line; Warm-up and Check Yourself answering time added to the time line (about 5 fast, 14 full). F17.13, F17.17, F17.18, F17.22 re-rendered in color and gray and checked; Quarto render clean.
