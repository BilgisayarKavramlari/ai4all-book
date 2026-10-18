# Chapter 19 — developmental memo (2026-10-18)

Inputs: four independent reviews, run in parallel without sharing reports (build/ch19/reviews/): subject-expert (Opus), pedagogy (Opus), student panel (Sonnet; Maya, Daniel, Ayşe), fact-check (Sonnet; docs/factcheck/ch19.csv, 170 claims: 133 supported, 27 partly supported, 3 unsupported, 1 outdated, 6 cannot verify), plus the editor's decisions 1–7 of 2026-10-18 and the amended D24. The author delegated editorial choices (D19), so the editor made the calls below. Revision v2 also includes a light Mode B voice pass (voice-profile §10): breadth-first openings in 19.1 and 19.2, "For example" after abstract claims, short "In other words" restatements after dense paragraphs (19.2, 19.4, the Case Study's "So what?"), the "Let's take" walkthrough in Marcus's worked example. No anecdote, humor or opinion was added. Draft v1 is kept at build/ch19/ch19-draft-v1.qmd. Every fact-check row now has a `resolution_v2`; 14 rows were added for claims introduced in revision (F171–F184).

## Decisions — accuracy (fact-checker, subject expert)

| # | Change | Why |
|---|---|---|
| A1 | A-Lab chain link 2 relabeled **inferred** (dashed): the Methods describe manual analysis "when the automated refinement gives a poor fit", and a full manual re-analysis is documented only after publication. Updated in the Case Study, F19.18 (new title, dashed link), C26, the case-index row, D-19.6 and both answer keys | Expert High; editor decision 1; blueprint R2's own test was not met |
| A2 | Zn₂Cr₃FeO₈ described as a **compound** mistakenly included in the training data, not a target; the 57-target count is kept as the corrected article's own; Szymanski (2023) carries the title note; both Szymanski entries list all 16 authors | Fact-check F122, F128, F129; editor decision 1 |
| A3 | Ceder described as "one of the paper's senior authors", not "the lead author"; team affiliations (UC Berkeley, LBNL, Google DeepMind) | Expert; fact-check F115 |
| A4 | Health guide rebuilt on **C24** (Wong et al., 2021): Epic's figure attributed to its internal documentation; the alert threshold (≥ 6) stated before the 67% and 18%; one site, 2018–19 version; Epic's dispute cited to MedCity News with the corrected title; dated note on version 2 (Wong et al., 2026, four systems, AUC 0.82–0.92; Crossref abstract read). TPMG scribes stay one line from the abstracts only | Editor decision 3; expert; fact-check F054–F061 |
| A5 | Health map frame stated: health coursework includes placement work that can reach patients; a practice set that reaches no one is a check point. Marcus's practice dose calculation is now a **check point** | Expert Medium; pedagogy #7; editor decision 4 |
| A6 | SB 1188 cited to its statute in 19.F2 only; the false "Chapter 18 treats both" removed | Expert Medium |
| A7 | FTC: Rytr order set aside on Dec 22, 2025, deception cases stand; AICPA: 1.700.040 nuance (members in public practice; a confidentiality agreement or the client's consent before an outside provider), cited to Blatch (2015) | Expert; fact-check F044–F045, F160 |
| A8 | UTD: OIT's guidelines (URL updated) and the Information Security Office's 2026 guidelines both stated, with the course rule; IRB change rule cited to 45 CFR 46.108(a)(3)(iii); "generally requires" informed consent | Expert; fact-check F066–F070 |
| A9 | NIH wording ("to analyze or write critiques"); NIH NOT-OD-25-132 (applications substantially developed by AI) added in 19.F5 | Fact-check F032–F033; expert |
| A10 | Ithaca: affiliations listed; "designed to assist and expand the historian's workflow"; the first suggestion was still wrong in about 38% of restorations; "historians stay in charge" and "why the pair won" labeled **this book's reading**; the "journals decide" sentence cut; a limits sentence (one test, two experts, texts damaged on purpose) | Fact-check F016–F018; expert; student panel |
| A11 | Bisbee: the simpler prompt rerun; June not distinguishable, July differed; the provider updated the model under the same name in June 2023. Argyle: backstories also from a second survey | Fact-check F039, F073, F078; expert |
| A12 | NHTSA: 956 crashes analyzed, 467 in scope; Tutor CoPilot: tutor-facing only, tutors used it in about 3 of 10 sessions; TBPELS: "should be aware", §137.33(b) incl. standards reviewed and selected; AAPOR as a task-force report (Rothschild et al., 2026); Springer Nature: AI authorship and photorealistic images only; ANA Provision 3.1 | Fact-check F083–F084, F090, F098, F100, F071–F072, F080; expert |
| A13 | Data class aligned with Chapter 12 ("its row in Chapter 12's table"); "the table's rows, unchanged"; OIT expanded | Fact-check F029–F030; student panel |
| A14 | UTD majors mapped by school (2026 catalog), moved to the Field Guides intro; "speech, language, and hearing sciences"; no "arts and technology" degree in the UTD list | Fact-check F021–F023; pedagogy #9 |
| A15 | References: Assael (2025) author order with Dietrich; Handa (14 authors); Zillow Group 2021a–c with URL; Wang (Nov 2025 version); Reuter title and URL; TBPELS title; OIT URL; Springer Nature, MLA, Blatch, FTC (2025), NIH (2025), Wong (2026), Rothschild et al. added; Veiga removed (cited only in C23); Chemistry World and the Michigan Medicine release dropped from the case files | Fact-check F059–F161 |
| A16 | Use-map cells and reasons: natural-science images that are data = keep with a person, diagrams a check point; engineering wording "a licensed engineer who directs the work"; education quiz generator moved to drafting; F19.13 maps training data to "Limits and safeguards", not "Tested on" | Expert Medium/Low |
| A17 | Case Study and C25/C26 label paragraphs broken into lists, with a one-line definition of the tree, the chain and documented/inferred | Student panel; expert |

## Decisions — learning design (pedagogy, student panel)

| # | Change | Why |
|---|---|---|
| P1 | **Week 13 recounted** under amended D24 at the standard rates: Core package ~52 min (reading 6,427 words ≈ 42.8 + 19 items × 0.5) + R16 abstract and Figure 1 ~4 (Figure 2 recommended) + pre-lab ~12 + A13 ~64 (fairness runs 7 counted; card ≤ 100 words, defense 80–100) = **132 min**, 125 without fairness runs. All faded examples, Review A–C, Spaced Review and Case Study Questions are final-exam practice. One number in chapter, blueprint and handoff | Pedagogy High #1; editor decision 2 |
| P2 | Core word count reported without markup: 3,753 including faded examples and the written-out build (3,304 without them); the v1 "~110 over" note corrected | Pedagogy; editor decision 3 |
| P3 | Review A rebuilt: option lengths equalized (the key is longest in one item only, A4, tied), absolute distractors replaced with misconception wording, A11 (c) no longer echoes 19.6; comment updated | Pedagogy High #2 |
| P4 | A13 brief prints the clause "with the checks, safeguards, card and defense that belong to them"; a reused A11 people point counts only when a run or the peer test shows it working; "real inputs" and "done-criteria" defined | Pedagogy #5; student panel |
| P5 | Rubric made count-based with parallel levels: eight items for Build; three-job test runs; verification (1.5) split from revision (0.5); card and defense 0.5 each; data rule as a resubmission condition | Pedagogy #6; editor decision 5 |
| P6 | Alternative assignment read criterion by criterion: classify four inputs and predict an added one; the peer picks a provided input; three provided outputs checked; the revised build's predicted output counts as the rerun; a pre-lab route; scenarios posted by Tue Apr 20 | Pedagogy High #3 |
| P7 | Faded examples now supply every fact: 19.1 (the board votes on spending; default and override asked), 19.4 (the course's AI rule; session notes name students), 19.5 (units and the common error), 19.8 (run 2's output) | Pedagogy #4 |
| P8 | Lab 19.1: pairing by guide from the pre-lab sheet, the builder brings in-scope inputs, a checkpoint at minute 20, build 30 min, share 10, exit 10, same-guide peer allowed when confirmed, any input language with glosses; figures named by title in the lab file | Pedagogy #8 |
| P9 | Check Yourself made answerable from Core: 19.4 states why to start nearest; 19.7 puts "not for" first and says why; M6 refuted ("A card only informs; the gates and checks are what protect"); "why" items added to 19.5 and 19.8 | Pedagogy #10, #13 |
| P10 | One fully written-out build (Marcus's chain as text with placeholders) in 19.5 and a complete abridged sample A13 (all nine parts) in 19.8 | Student panel top fix 1 |
| P11 | Business guide adds marketing (authority, edge case, fairness ruling for audience-targeted copy); Natural Science guide expanded (Lucía's day-length lab as a worked row; known error patterns) | Student panel top fix 2 |
| P12 | 19.1 decluttered: the four levels glossed in a list; the Chapter 14/15/12 contrasts moved to a Note; the figure's four uses named in the text; "raise the floor" glossed | Student panel; pedagogy |
| P13 | Box types explained once; OIT and TBPELS expanded; codebook, preregistration and sandbox glossed; a home-country rules line for students outside the U.S.; a peer-test sentence frame (19.6, Lab 19.1) | Student panel (Ayşe) |
| P14 | New F19.22 reuses Chapter 18's `regulation_map` for Marcus; F19.8 kept as the "nearest first" list | Expert; editor decision 4 |
| P15 | Tags: O6 one verb (Produce); B3 Apply; CSQ 3 Analyze; Review B2 and B3 supply the field facts the keys use | Pedagogy #11–#12 |

## Not changed (with reason)

- **Tesla (C27) "tree not applicable" kept**, with the reason now stated: no AI output was wrong; the defect is in the design of the human's controls. The expert offered "other (a system control weakness)" as an alternative; the chain labels carry the documented failures.
- **Core over the 3,400 cap.** The written-out build and the sample A13 record add about 300 words of Core and Studio; both were the student panel's top request. The week still fits 132 minutes at the standard rates.
- **U.S. Department of Education guidance not added** to the Education guide (expert: optional); the guide cites FERPA and COPPA only.
- **Field guides remain Studio reference**; the map by school is in their intro, with a pointer from 19.1.

## Waiting for the author

1. Live-syllabus items: R16 required part now the abstract and Figure 1; A13 wording (card ≤ 100 words, defense 80–100, the D-14.7 sentence and the "belong to them" clause); Lab 19.1 timing.
2. From the Field: approval, and whether the 2016 entry's project was commercial or funded (D16).
3. Tuesday demo choice.
4. Final voice edit — the editor never marks a chapter "done".

## Final review (build/ch19/reviews/final.md) — applied 2026-10-18

| # | Change |
|---|---|
| M1 | Majors map corrected to the 2026 catalog (Interdisciplinary Studies: healthcare studies, education; EPPS: public health; JSOM: business administration, healthcare management; Bass: philosophy; undecided on its own line); F183 resolved |
| M2 | The §12.5 note now copies Chapter 12 verbatim |
| S1 | Hana's major is "media arts and design" (decision D26) |
| S2 | People-point levels use Chapter 14's wording; the stop point is named as a build condition, not a map level; handoff glossary row aligned |
| S3 | Time line names the Spaced Review as exam practice, Discussion Questions as class work, and the optional parts |
| S4 | "Not hallucination" reason uses the glossary definition (fluent output), in the Case Study and the even key |
| S5–S6 | TBPELS wording as advice; FTC Rytr as one order of five cases; FTC URL |
| S7 | One A11-credit test: revised for the build and shown working by a run or the peer test (brief, keys, D-19.4) |
| S8 | Rubric gaps closed (Build Developing; Card Proficient) |
| S9 | Handoff glossary count (12) and wording aligned (informed consent; IRB "approves and oversees") |
| S10 | Faded 19.4 key no longer depends on a court case; the tutee's-work point is an "Accept also" |
| S11 | HIPAA expanded at first use; MLA expanded |
| Nice to have | Opening Case extended to 300+ words; Discussion Questions tagged; Engineering coursework-code note kept in the CSV reason |
| S12 | Chapter 21 item: handled by the editor |
