# Chapter 21 — developmental memo (2026-10-18)

Inputs: four independent reviews run in parallel without sharing reports — subject-expert reviewer (Opus; 23 findings, 1 High), pedagogy reviewer (Opus), student-reader panel (Maya / Daniel / Ayşe, Sonnet), fact-checker (docs/factcheck/ch21.csv, 123 claims: 90 supported, 6 supported as marked, 19 partly supported, 0 unsupported, 8 cannot verify, 6 of them because Chapters 19, 20 and 22 were drafts). The author delegated editorial choices (D19); the editor's nine decisions for this revision and decisions D23–D25 were applied in revision v2. Draft v1 kept at build/ch21/ch21-draft-v1.qmd.

## Decisions — accuracy (fact-checker, subject expert)

| # | Change | Why |
|---|---|---|
| A1 | Hana's model commitment now covers the whole contract clause: "Before I use any AI image generation on a client job, I get the client's written agreement, because my contract clause requires it" (21.2, F21.5, Summary); the worked example says why the earlier "brief mentions AI" trigger was too narrow | Expert #1 (High): the model line was looser than Hana's own rule, the error 21.3 teaches against; editor decision 3 |
| A2 | 2025 meta-analysis stated as in its abstract (effects on thoughts, feelings and behavior, d ≈ 0.27–0.66; larger with the if-then form, high motivation and rehearsal); range tied to outcome type; "almost two decades later"; rehearsal defined as in the studies and not equated with a six-month review | Expert #2–4; fact-check C40–C41 |
| A3 | Independent check on the evidence: Wang, Wang & Gai (2021), 21 studies, g = 0.34, publication bias noted; both earlier reviews identified as by the theory's originators | Expert #5; editor decision 7 (abstract read via Europe PMC) |
| A4 | Principle 2.5's condition restored everywhere ("systems whose future risks cannot be reliably predicted"); 2.3 paraphrased exactly ("should consider challenging … before violating"; whoever violates accepts responsibility) in 21.3, Review A8, the case file | Expert #6, #17; fact-check C09, C28 |
| A5 | McNamara et al. (2018) described from the abstract: "105 professional software developers and 63 software engineering students", "one group was asked to consider the ACM code; a control group was not", "no significant difference in the answers"; DOI and pages confirmed via Crossref | Expert #7; fact-check C31–C33 |
| A6 | Gollwitzer's form no longer in quotation marks (paraphrased); 2006 domains "exercising, studying or health screening"; the 2006 meta-analysis cited in chapter form (In M. P. Zanna (Ed.), Vol. 38, Academic Press) | Fact-check C36, C42, C46 |
| A7 | EU General-Purpose AI Code of Practice: drafted by independent experts in a process run by the Commission's AI Office, voluntary for providers, published July 10, 2025 (Commission page); one sentence that Chapter 18 does not discuss it | Expert #9; fact-check C49–C50; editor decision 7 |
| A8 | ANA's January 2025 revision given as the one verified example of a revised professional code, "though not every revision addresses AI" | Expert #8; fact-check C111 |
| A9 | ACM press release (July 17, 2018) cited as ACM (2018b) with live URL and archive capture; "two-year process, drafts published for comment" now confirmed; F21.2's middle box solid; booklet = ACM (2018a) | Fact-check C01, C13, C15; editor decision 7 |
| A10 | Opening wording to the source: "in ways that may not be intended or even predictable"; co-chairs of ACM's Committee on Professional Ethics; "fits on a few printed pages"; "largest" never used | Fact-check C05; expert #13–14 |
| A11 | Verification Funnel row: primary source for any number, quotation or citation, or when the stakes are high (Ch. 8 stage 2); heat-map row: an owner for every risk (Ch. 15); hard gate and paired-input glosses in their owner chapters' exact wording | Expert #10–12 |
| A12 | One wording of Hana's dated note ("prompts are not used to train its foundation models (as of October 2026)"); F21.7 points to it instead of rewording it; university tool line "The university provides Microsoft Copilot Chat to all students (as of October 2026)" | Expert #15–16 |
| A13 | Hana's zine: Chapter 18 only *proposed* an AI line on the submission form; Hana "runs a small zine" and belongs to the zine collective (characters.md, Ch. 13); "the collective's editor" removed | Fact-check C81; pedagogy; editor decision 3 |
| A14 | Marcus's no-patient-information rule "first stated in Chapter 15"; his reason is now his own evidence (his A12 data-flow map); Elif's Career line no longer gives her a research-assistant role | Fact-check C64, C115; editor decision 6 |
| A15 | From the Field: only counts by cause feed the fishbone diagram; reference title as printed, "Kontrol sayfası (Control sheet)" | Expert #20; fact-check C59 |
| A16 | Interview-question claim softened ("An employer may ask …"); uncited "engineering codes put public safety first" removed; Further Reading time for the ACM passages corrected (about 5 minutes, about 10 with the prefaces) | Fact-check C113, C117, C118 |

## Decisions — learning design (pedagogy, student panel)

| # | Change | Why |
|---|---|---|
| P1 | **One set of required lines everywhere:** verification, data, disclosure, plus a fourth on "delegation and oversight, or risk, or fairness — whichever your work most needs" (21.2, 21.5, brief, rubric, Check Yourself 21.2 Q3, card header) | Pedagogy and panel must-fix; editor decision 1 |
| P2 | **"Own evidence" defined** in 21.2 with where to find it (Failure Diary, assignment results, lab records) and the rule that a policy counts only with the student's own evidence of why it matters; Hana's, Marcus's, the student teacher's and the closing-box reasons rewritten to pass; new Check Yourself 21.2 Q2 and Review A12 on it; Key Term added | Panel top-2; pedagogy; editor decision 2 |
| P3 | **Honest times with the standard rates** (opening page included): Part A reading ~29 min + answering ~7 + workshop draft 15 = **51 min in week 14**; finishing the code itemized at 27–29 min of portfolio-assembly time (code 42–44 in all); Part B ~7; whole Core package ~45; final-exam practice ~70 (Final Bridge ~40). Time paragraph turned into a table | Pedagogy top-1; panel; D23–D25; editor decision 4 |
| P4 | **D25 cuts:** the 21.1 Your Turn folded into the 21.2 draft (reread A1 goals); the workshop draft limited to three commitments and a boundaries line; the rest of the code moves to portfolio-assembly time | Editor note (D25) |
| P5 | 21.2's nine-term gloss paragraph replaced by a three-column table with a one-line example each; the implementation-intention paragraph cut to two sentences (details stay in Deep 21.A); "fires" replaced by "applies" | Pedagogy load row; panel (Ayşe); editor decision 4 |
| P6 | **Rubric gaps closed:** counts 3 and 8+, one line failing two questions, more than half failing, no review date, Fit levels non-overlapping, revision and declaration scored 1 + 1; "no recorded test → Proficient at most"; role-brief reading time for the alternative | Pedagogy must-fix; editor decision 6 |
| P7 | **Final Bridge "Chapters 8 to 20":** ten items (Ch. 8, 9, 10, 11, 12, 14, 15, 16, 18 ×2); old FB7–FB8 (repeating earlier Spaced Reviews) replaced by §18.3 authorship and §10.7 disclosure; FB5 (old FB4) option-start cue removed; keys c, a, b, d, a; map and table extended to Chapters 8–10; even items on eLearning and in the first 10 minutes of May 4 | Pedagogy; panel; editor decision 5 |
| P8 | **Review A:** four near-repeats of Check Yourself replaced with items on M3 (A6), M5 (A10), M6 (A3) and own evidence (A12); giveaways removed (A8, A12); tags fixed (B4 Apply, DQ4 Analyze); objectives print their Bloom level; O4 "Plan" tagged Create | Pedagogy review table |
| P9 | Faded examples: all labeled "(Constructed example.)"; every fact the reader needs supplied in one line (curriculum document, the intern's own incident, the co-op's tool and model); the student teacher's step 1 shows the test ticks and step 3 asks for the test; pronouns varied (she, he, they, he) | Fact-check C122; pedagogy; inclusion rule |
| P10 | Case Study ends with a decision (review interval; one ACM principle turned into a commitment), defended in Case Study Question 3; "Failure Taxonomy Tree" glossed in the Labels paragraph | Panel; editor decision 8 |
| P11 | Duplicated preaching cut: the second "never a reason to skip a rule" and "protects the people your work affects" exhortation removed from the Ethics Lens; Last Words ends on a concrete action (put the review date in your calendar; keep, revise or retire each line) with `[AUTHOR NOTE: optional]` as the only placeholder | Panel "earned or preachy"; editor decision 8 |
| P12 | Spaced Review items point to sections that exist: §20.3, §20.4, §19.6, §19.1 (the four things that change across fields) | Fact-check C101; editor decision 8 |
| P13 | Card target "about 300 words" in 21.5 and the brief (card with short reasons); `principles_card` header now "including the four required lines" | Panel; fact-check C123 |
| P14 | Labs 21.1–21.3 aligned: the same line kinds as 21.1 (no separate "value"), the reason question includes "a rule with no evidence", Lab 21.3 step 4 made concrete | Panel |

## Not changed (with reasons)

| Suggestion | Decision | Reason |
|---|---|---|
| O5 faded example (a partly filled card) | Not added | 21.5 is code-writing time; the blank card, Hana's complete card and Marcus's card already model the whole page, and the student's own card is the Your Turn. Adding a faded card would add 2 minutes to the assembly time for little gain |
| Şeker (2014a/2014b) | Kept as Şeker (2014) | The same-year rule applies within a chapter; this chapter cites one Şeker (2014) entry (Chapter 4's fishbone entry is mentioned, not cited). The book-level list disambiguates at assembly |
| Cite the NSPE code for engineering | Not added | The sentence was removed instead; no professional code edition is named except ANA (verified) |
| 22 signatories of the EU code (Oct 2026) | Not added | Would age quickly and is Chapter 18's ground; the publication date suffices |
| Shorten Part A to reach a 30-minute Core package | Partly | Trimmed ~200 words, but the terms table (requested), the own-evidence paragraph and the faded-example facts added length; the honest number (~45 minutes for the whole package; ~29 for Part A reading) is stated |
| A separate time for slower readers (×1.5) | Not added | The book-wide reading-time note ("allow more if you read more slowly or are reading in a second language") is used, as in other chapters |
| "The tool produces options, and you decide" | Removed | Panel: a slogan by the chapter's own test |

## Waiting for the author

1. Live syllabus (the editor already updated docs/syllabus.md): Ch. 21 Part A on Apr 27 and Part B on May 4; the peer check in Lab 20.1 minutes 50–65; even Final Bridge items on eLearning and in the first 10 minutes of May 4.
2. AI use for the code follows the syllabus row ("drafting permitted with disclosure"), looser than the §10.2 reading (D-10.2): confirm.
3. Last Words: `[AUTHOR NOTE: optional]` and the final voice edit of the book's closing paragraph.
4. From the Field: approve the 2014 check-sheet entry and confirm its pages (printed 26–27).
5. Final voice edit of the chapter.

## Final review (build/ch21/reviews/final.md), applied 2026-10-18

M1 Hana's line 1 now gives the clause together with their own evidence (the bakery client's generated cover image, Ch. 18 §18.1–18.3, logged in the Ch. 18 handoff); M2 Hana's card gains a risk line (Ch. 18 risk sheet) so it has all four required lines; M3 rubric gaps closed (one or more failed questions; two or more failing required lines; two or more tool facts; a true "no AI tools used" declaration scores 1); M4 Revision criterion scores the question failed and the question now passed, matching item 7, §21.5, Lab 21.1 and the key. Should-fixes S1–S16 applied with the reviewer's wording: FB2 → §9.4–9.5; FB3 replaced (§11.2 blanks); FB10 replaced (§10.2 spectrum); Ch. 10 added to Decide (second); the invented invoice clause removed (not logged in Ch. 18); Marcus's line 5 reason; Mina's dates; the §10.2 permission sentence in the brief (still Author-only 2); B2/B3 facts; absolute distractors; F21.7 caption; Lab 21.2 line kinds; case file Q3 and (2018a); Dakan & Feller and ANA URL added; UTD and EU spelled out; FB9 key dated; C98–C100 closed. F21.5, F21.8, F21.14 re-rendered (color and gray) and checked; Quarto render clean.
