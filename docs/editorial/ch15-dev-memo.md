# Chapter 15 — developmental memo (2026-10-18)

Inputs: four independent reviews run in parallel without sharing reports (build/ch15/reviews/):
- subject-expert reviewer (Opus): 24 findings, 1 high;
- pedagogy reviewer (Opus): 4 must-fix;
- student-reader panel (Maya / Daniel / Ayşe);
- fact-checker (Sonnet; docs/factcheck/ch15.csv, 107 claims: 90 supported, 16 partially supported, 1 cannot verify, 0 unsupported).

The editor's seven decisions came with the reviews, followed by notes on Chapter 16's station 3, Chapter 18's rules-and-rights risk and the dash rule for `data_flow_map`. The author delegated editorial choices (D19), so they are decided and recorded here. Draft v1 is kept at build/ch15/ch15-draft-v1.qmd. Revision v2 is chapters/15-privacy-and-security.qmd, with the final-review fixes below: about 11,500 words. The Core sections hold about 3,040 readable words without the faded examples and the optional FERPA/HIPAA box (about 20 minutes). The whole Core package holds about 3,920 words plus answering the Warm-up and seven Check Yourself items, about 30 minutes in all (29.4; build/ch15/count.py).

## Decisions — accuracy (expert, fact-checker)

| # | Change | Why |
|---|---|---|
| A1 | "No layer has been shown to stop every attack" is limited to "outside the tests it was measured on" (15.3, F15.8) and "in real use" (Summary, A9 key) | Expert 1 (high): Anthropic's 2026 zero results |
| A2 | Anthropic 2026 is reported in full: no successful attacks on three of its four newest models, 0.3% on the fourth, on a harder test with a new grading pipeline. "A moving target" is kept; comparability is marked as this book's reading | Expert 2; fact-check C24 |
| A3 | Samsung: the Bloomberg sentence loses the device list, which neither Bloomberg nor CSO prints. A spokesperson's confirmation of the device restriction is added (Park, 2023, TechCrunch). "The pastes are reported, not confirmed" | Fact-check C09; expert 3; editor 3–4 |
| A4 | Heiding et al.: spear phishing vs. a generic control, groups of about 25 | Expert 4 |
| A5 | Deep 15.A now reads "the model's settings (parameters) do not change while you chat; a memory feature stores notes outside the model" | Expert 5 (banned verb "learn") |
| A6 | Deletion vs. legal preservation: "the terms, and sometimes a court order"; a dated example in Deep 15.A (May 2025 order; the duty for new logs ended Sept 26, 2025; Chen, 2025, Engadget) | Expert 6; editor 3 |
| A7 | Explicit safety rule in the Labs intro and Lab 15.1: only the provided file; no attempts to get around safety rules or reveal hidden instructions | Expert 7; editor 2 |
| A8 | Run counts aligned: three runs each way, three numbered printed outputs per version | Expert 8; pedagogy |
| A9 | Appendix E block gains Check Yourself keys (seven) and faded keys (six); the time line ends with the standard sentence | Expert 9; pedagogy 2; brief rule |
| A10 | Wallace ranking (system, user, tool outputs); CaMeL limit (cannot stop a changed summary) in Deep 15.B and F15.22; "is trained to favor" | Expert 10, 11, 24 |
| A11 | Nasr et al.: arXiv preprint kept (it holds the figures), with a note on the revised ICLR 2025 version | Expert 12; editor 3 |
| A12 | Staab: "the best model … correctly up to 85% of the time on its first try"; HIPAA includes business associates; biometric data includes behavior; "unless a model runs on your own device"; "never read that code to anyone who contacts you"; "several layers, built to fail in different ways" | Expert 14–19 |
| A13 | Hong Kong amount: HK$200 million from the government; US$25.6 million (CNN) cut from 15.4 for length | Fact-check C32 |
| A14 | OpenAI's December 2025 statement cited to its own post; Willison's 95% sentence trimmed to what he wrote; EchoLeak cites both Microsoft ("AI command injection", CWE-74) and Aim Labs ("indirect prompt injection"); Stuckey via eWeek (Abdullahi, 2025) | Fact-check C45, C46, C60, C64, C101 |
| A15 | References fixed: Aim Labs Team title and URL; Microsoft entry title and date; Anthropic 2025 title "Piloting Claude in Chrome"; Jeong D.-Y.; Şeker pages 10–17 with URL; FTC PDF URL; CSO canonical URL; Microsoft & LinkedIn URL; OpenAI 2023a–c and Dobberstein added; Bellan and Stuckey removed | Fact-check reference rows; expert 20–21 |
| A16 | Data-class note under the §12.5 table: v2 still paraphrased it (corrected after the final review, F2 below); UTD and OIT expanded | Expert 23; panel |
| A17 | Case Study Question 3 key: owners marked as the reader's reasoning | Expert 22 |

## Decisions — learning design (pedagogy, student panel, editor)

| # | Change | Why |
|---|---|---|
| L1 | **Week 12 under D22 (as amended): about 131 minutes**, stated identically in the chapter, the blueprint and handoff D-15.2. Ch. 15 package ≈ 30 (reading 26 + answering the Warm-up and Check Yourself 3 = 29.4; all faded examples are final-exam practice); R12 recommended; pre-lab 3; A12 at home ≈ 39 including reading the brief and rubric; Ch. 16 ≤ 30; Ch. 18 ≤ 29 | Pedagogy 1; editor 1; D22; final review M3 |
| L2 | Cuts to fit: one Check Yourself item per section (plus one in 15.7); Summary ≈ 200 words; Opening and 15.1–15.6 tightened; the FERPA/HIPAA box marked optional; standing instructions no longer defined (not needed in v2) | Editor 1 |
| L3 | Multiple choice: the key is the longest option in one item (A2); A7(b) and A9(c) are hedged distractors; A2 is now an MC item on residual risk; A13 assesses biometric data; the A12 item is retagged Understand | Pedagogy 3, 10, 11, 12; editor 5 |
| L4 | Heat-map chain repaired: high likelihood = "already seen it happen in your own ordinary use"; Lucía's worked ratings carry anchor phrases; risk 1's evidence is a coworker at another branch; risk 2 is "a takeover call succeeds" and gets a new mitigation (24-hour hold with notice to the old address; weekly call-log review); Marcus's Risk C is an event; the faded example has an anchor scaffold | Pedagogy 4–6; editor 5 |
| L5 | "Qualifying risk" taught in 15.6 (high impact, or at least medium in both) and used in the worked plan and A12 | Pedagogy 7 |
| L6 | 15.7 prints a model register row built from a probe count (with the evidence-transfer rule) and a 67-word model note for the decision owner; Check Yourself 15.7 asks the transfer question | Pedagogy 8; panel; brief rule |
| L7 | Marker convention stated in 15.5's body (D/solid, I/dashed, hollow before, filled after) | Panel; editor 6 |
| L8 | Glosses: consumer and institutional terms, data class, UTD, OIT, canary, exfiltration, leg, lethal trifecta; postal-code note beside the ZIP example; "a public list of registered voters" | Panel; editor 6 |
| L9 | A12: alternative assignment visible in the first lines of the brief and in 15.7; what to do with no A10/A11 workflow; alternative-assignment students attend the lab; absent-Thursday route (+30 min); an unfixed error counts as two missing elements | Panel; pedagogy |
| L10 | Rubric: counts missing or faulty elements (a rating against its anchor, a mitigation of the wrong kind); red-team Beginning closes the four-or-more gap; map elements match the five taught boxes; Chapter 16's and Chapter 18's elements scored; note and declaration separate; the "lower level" sentence and the confusing header removed | Pedagogy rubric; panel; editor 7 |
| L11 | Lab 15.1 retimed with the map drawn and timed (7–12) and moves inside station windows; station 3 = Chapter 16's text with the editor's fixes (copy-paste prompts, prompt C's comparison fixed as "she" vs. "he", one subtotal per table, live and printed tallies apart, numbered printed outputs, content-safety rule); pooled reading moved to the gallery walk with a threshold table for 20–45 runs (this book's calculation, same method as D-16.3) and "no gap is not evidence of no bias"; rules-and-rights risk drafted in a timed 5-minute slot (49–54) with Chapter 18's five scratch-list prompts (editor note after the Ch. 18 pedagogy review); seated gallery walk; trios allowed; paper or photo | Pedagogy lab; editor 2; Ch. 16 and Ch. 18 handoffs |
| L12 | O5 UNESCO "ethics of AI, Apply"; O2 adds biometric data; Discussion items tagged with LO and Bloom | Pedagogy 10–11 |
| L13 | Figures follow the dash rule: the trust boundary is a shaded band; the reuse box a shaded fill; omitted parts crossed out; chapter-map "Decide (2nd)" without a dash; the "voice realism" box crossed out; F15.8's line solid and tapering; the storyboard's note box solid. Only inferred evidence is dashed (heat-map markers) | Brief rule; editor addition 1 |
| L15 | Legal-layer pointers (FERPA/HIPAA box, Ethics Lens, Further Reading) point to Chapter 18, section 18.1, where Chapter 18 adds the FERPA/HIPAA/consent/state-privacy paragraph (editor decision on final review M4) | Brief rule: Ch. 18 owns the legal layer |
| L14 | Reading-time note in the new inclusive wording; final-exam practice labeled in the time line | Brief rules; editor 7 |

## Final review fixes (build/ch15/reviews/final.md, 2026-10-18)

| # | Change | Why |
|---|---|---|
| F1 | Station 3 replaced with Chapter 16 v2's text: prompt B "Author's first language: English / Turkish" (replacing "Written by an international student"); prompt C two runs per version (she vs. he; they a lead); matching rule; private opt-out; one subtotal line per table; gallery table in counts with a 26-run row (data/ch15_lab_thresholds.csv); fair test includes at least 10 runs per version | M1; S10; inclusion rule |
| F2 | Chapter 12's note under the data-class table, word for word, and the "course floor" sentence (Chapter 19's wording); fact-check C121 corrected | M2 |
| F3 | Week recounted under D22 as amended (all faded examples are final-exam practice; Warm-up and Check Yourself answering stay): package 29.4 → "about 30"; week about 131 | M3; editor |
| F4 | Legal-layer pointers to Chapter 18, section 18.1 | M4; editor |
| F5 | Deepfake defined verbatim from Chapter 13, with synthetic media glossed | M5 |
| F6 | S1 class glosses after "(UTD)"; S2 rubric rules element (template, closing line) and item 4c's detectable gap; S3 tree label on Marcus's runs; S4 Arup's heat-map side; S5 standing instructions glossed in A7; S6 two anthropomorphic phrasings fixed; S7 unused Chen & Magramo reference deleted and OWASP in-text author matched; S8 handoff wording (Decide second; defense in depth) and the full memory definition; S9 C115 left to the editor (hhs.gov in Chrome); nice-to-have: `risk_heat_map`'s `title` parameter documented | S1–S10; nice-to-have |

## Not changed (with reason)

| Item | Reason |
|---|---|
| Golle (2006) re-estimate of the Sweeney figure (expert 13, optional) | The 1990 estimate is exact as cited and the point holds; adding a second estimate costs Core words |
| Rename "stations" to "rounds" (blueprint review) | Chapter 16's text uses "station 3", and every pair takes the stations in turn |
| Move points from the map to the register (panel) | The split follows the course's artifact rubric (task 3); the register's weight is shared with the red-team record (process evidence 3) |
| A US$ conversion for the Arup loss in 15.4 | Cut for length; Chapter 13 keeps CNN's figure |
| Ch. 6's standing instructions definition | No longer needed in v2's 15.1; the term is still used in Review A7, where the stem's meaning is clear and Chapter 14 defined it |

## Waiting for the author

1. Live syllabus: R12 recommended (D22); R13–R15 recommended unless they fit; A12 hosted here; Tuesday Apr 13 split.
2. From the Field approval (2015 entry, pages 10–17).
3. UTD OIT/ISO confirmation for live runs of the hidden-instruction file; until then, printed outputs.
4. Tuesday demo tool and model; guest's field.
5. Final voice edit.

## Open items (not author)

- Fact-check C79 (Corti et al. not opened; cited "as cited in"), C115 (HIPAA business-associate wording against the HHS page, 403 to automated fetch).
- Chapter 16's lab file still places the pooled reading at station 3; Chapter 15 moved it to the gallery walk (the pool is complete only then). Editor to align.
- Chapter 18 should re-render its imports of `data_flow_map`.

## Voice pass (Mode B, 2026-10-18)

Light pass within the word cap. Worked examples use the model → solve → apply frame, with one "Let's take …" walkthrough (Lucía's map). "In other words" restatements follow the dense evidence paragraph in 15.3 and the From the Field connection. Sections open with a concrete constraint (15.1 "Unless a model runs on your own device…"; 15.5 "You cannot remove every risk…"). Hedges were replaced by sourced statements. No humor, anecdotes or opinions were added; the author's own words appear only in From the Field, limited to the 2015 entry.
