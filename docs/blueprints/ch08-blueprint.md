# Chapter 8 blueprint — Hallucination, Uncertainty and Verification

Status: v0.2 (2026-10-18), APPROVED under delegation (D19). v0.2 applies the independent blueprint review (build/ch08/reviews/blueprint.md: 4 high, 11 medium, 9 low) and the editor's decisions on it; see "Review changes" at the end. v0.1 is kept in build/ch08/ch08-blueprint-v0.1.md.
Part II — Working with AI · Syllabus week 5 (read for Thu Feb 18, 2027; Chapter 4 is read for Tue Feb 16) · **Reading order** (brief): Ch. 1 → 2, 3 → 5 (+6 Deep) → 7 → 4 + **8** · Path: Core (examinable: Core sections only, D20) · Featured student: **Lucía** (rotation; other people are unnamed one-off figures) · Work Loop step highlighted in the Chapter Map: **Verify**, with **Decide** second.

**Source material.** Syllabus week 5: Tue Feb 16 concept session (Ch. 4; demo: asking for sources on a niche topic) and Thu Feb 18 verification lab "ten claims; the fabricated court citations case" (R6, Ch. 8) → **A5 claim verification table**, due Mon Feb 22. Opening case C05 from the primary record, read on 2026-10-18: *Mata v. Avianca, Inc.*, No. 1:22-cv-01461-PKC (S.D.N.Y.), Opinion and Order on Sanctions, ECF 54, June 22, 2023 (43 pp.), and Opinion and Order, ECF 55, June 22, 2023 (dismissal). From the Field: Şeker (2015), *IEEE Access* (Argument Delphi), Drive 14tfA7WBJODNmUh4Ne5bFSsNQuSPMZPyu, read in full (build/ch08/argument-delphi-2015.md).

**Kept consistent with Chapter 1** (§1.4): a federal judge in New York sanctioned two lawyers and their firm in 2023 for a brief citing decisions ChatGPT had made up, which they kept defending; "You will study that case in Chapter 8." Chapter 1's four-step trace of a statistic and its red flags are recalled, not re-taught.

**Boundaries.** *Chapter 4* explains why failures happen: 8.1 recalls the tree and the two hallucination causes in at most two sentences; 8.4 reuses the pushback test without re-teaching it. *Chapter 3* owns next-token sampling (one-sentence recall). *Chapter 7* owns calibration of your own confidence; Chapter 8 reuses Chapter 7's model-sense clause word for word. *Chapter 9* owns how far a source deserves trust (reliability ladder, lateral reading), reading with AI and **summary fidelity**; Chapter 8 owns verifying claims: detection and verification methods, citation checking, fabricated-citation rates, uncertainty signals, calibration measurement, and the first student-facing tree labels after Chapter 4. **Passage vs. summary line:** Chapter 8 asks whether one passage of a source supports one claim; Chapter 9 asks whether a summary represents a whole source.

## 1. Outcome link and week 5

| Item | Value |
|---|---|
| Syllabus outcome | **LO3** (verify AI-generated claims, sources and outputs, and document remaining uncertainty); LO1 supporting (O5) |
| Studio artifact | **A5 — claim verification table**, due Monday, February 22, 2027, 11:59 p.m., hosted here (8.6 and the Application Assignment) with a 10-point four-level rubric and an alternative assignment |
| Reading order within the week | **Before Thu Feb 18:** save one dated AI output from your field that names at least two sources (pre-lab, ~5 min, stated at the start of the chapter); read Chapter 8 Core 8.1–8.5 and Studio 8.6. The 8.1 and 8.2 Your Turns use that output and **are the first rows of A5** |
| In-class time | **Tue Feb 16:** Chapter 4 (Lab 4.1 labels two demo outputs). **Thu Feb 18:** Lab 8.1 "Ten Claims": briefing with R6 pp. 1–2 read in class and the Mata excerpts; teams check the Tuesday demo's sources; each student checks **three** of their own claims, citations first |
| Readings | **R6** sanctions opinion (ECF 54): pp. 1–2 read in the lab briefing; ¶¶ 11–12, 25–28 and 45 as lab excerpts; full opinion in Further Reading (Decision 6). **R5** (Ch. 4) moves to Further Reading, recommended (editor decision) |

### Week 5 workload (out of class), counted honestly

| Item | Time |
|---|---|
| Chapter 4 share (Core + 4.8; the Failure Diary's first version moves to Feb 25, week 6, by editor decision) | ~35 min |
| Pre-lab: save one dated output from your field | ~5 min |
| **Chapter 8 Core + Studio + Check Yourself** (≤ 3,350 Core words + 8.6 ≤ 450 + ~300 words of Check Yourself, at 150 words per minute) | **~27 min** (longer if English is not your first language) |
| Your Turns 8.1–8.2 = A5 rows (split your output into ten claims; take one through the funnel) | ~10 min |
| A5 at home after the lab: about six claims (≈ 4 min at stage 1; ≈ 6–10 min at the primary source or for a citation), calibration gap (5), corrected statements (5), reflection 100–150 words (8), declaration (5) | ~45–50 min |
| **Required total, week 5** | **~2.0–2.1 h** (target ≤ 2.2 h; syllabus 1–2 h). R5 optional (+15) |

**Core caps:** 8.1 600 · 8.2 750 · 8.3 850 · 8.4 550 · 8.5 600 = 3,350 words. Worked examples ≤ 150 words, faded ≤ 80. Check Yourself sits outside the caps (counted in the reading time). The chapter reaches ≥ 10,000 words through the Opening Case, Deep sections, Case Study, Ethics Lens, Career Connection, From the Field, labs and the End-of-Chapter Package.

## 2. Chapter objectives (6)

| # | Objective — after this chapter you will be able to… | Bloom | LO | Framework tags |
|---|---|---|---|---|
| O1 | **Decompose** an AI output into claims you might rely on, mark each checkable or not, and rank them by what an error would cost | Analyze | LO3 | 4D:DISC · UNESCO:HCM-U |
| O2 | **Apply** the Verification Funnel: take a claim as far as its stakes require (an independent check, the primary source, an expert), give a verdict and record what remains uncertain | Apply | LO3 | 4D:DISC · 4D:DIL |
| O3 | **Analyze** a citation or quotation for the three ways it can fail, using indexes and records no AI tool produced | Analyze | LO3 | 4D:DISC |
| O4 | **Evaluate** what an output's uncertainty signals tell you, by comparing a tool's stated confidence with its results on known-answer items (its calibration) | Evaluate | LO3, LO1 | 4D:DISC · LM:how-works |
| O5 | **Diagnose** a real verification failure: label it on the tree and the failure-to-harm chain (documented or inferred) and name the funnel stage that would have stopped it | Analyze | LO3, LO1 | 4D:DIL · UNESCO:ETH-U |
| O6 | **Produce** A5: a ten-claim verification table with stages, sources, verdicts, both confidence columns, a calibration gap, corrections and an AI Use Declaration | Create | LO3 | 4D:DIL · 4D:DISC |

## 3. Prerequisites and promises kept

From Ch. 1: fluent ≠ correct; red flags; the four-step trace; Verify = "a source, a calculation, your own knowledge, an expert"; fabricated sources unacceptable even when disclosed; hallucination, outdated information, overconfidence (glossary wording). From Ch. 2 (Deep 2.C): precision and recall → Deep 8.A. From Ch. 3: sampling (same prompt, different answers); retrieval adds text but does not change prediction; §3.2 "Chapter 8 shows how to check." From Ch. 5: one result is not evidence. From Ch. 7: calibration (of your confidence), "predict, then check", the two-meanings box, A4's "calibration gap". From Ch. 4 (two days earlier): the tree (leaves "invented facts or sources", "outdated information", "certainty beyond the evidence"), documented/inferred, the chain, the pushback test, "label overconfidence only with evidence about expressed certainty", and Lab 4.1's demo cards. Each recalled in one or two sentences with a pointer.

## 4. Misconceptions (six)

| # | Misconception | Where | Refutation, without creating a new one |
|---|---|---|---|
| M1 | "If most of an answer checks out, the rest is probably right too" | 8.1 | Accuracy varies claim by claim: in a 2023 evaluation, 58% of the separate facts in ChatGPT's biographies of people were supported by a reliable source (Min et al., 2023). Not "most answers are wrong" |
| M2 | "If the output names a source, the claim has been verified" | 8.3 | A named source is a pointer until opened: 55% (GPT-3.5) and 18% (GPT-4) of references in one 2023 test did not exist (Walters & Wilder, 2023). Not "AI references are always fake" |
| M3 | "Asking the tool whether its source is real is a check" | 8.3 | In Mata the lawyer asked; the replies said the cases were real and could be found in legal databases (ECF 54, ¶ 45). A check needs evidence no AI tool produced |
| M4 | "If several runs, or several tools, give the same answer, it is correct" | 8.4 | Disagreement across fresh runs is a warning sign (Manakul et al., 2023); agreement is weaker evidence, because the same patterns can give the same wrong answer. Not "agreement means nothing" |
| M5 | "A tool that says it is 90% sure will be right about 9 times in 10" | 8.5 | Stated confidence clustered at 80–100% (Xiong et al., 2024) and ran ahead of accuracy while still rising with it (Wei et al., 2024). Not "stated confidence is meaningless" |
| M6 | "Verifying means checking every sentence as far as possible" | 8.2 | Checks are proportional to stakes; every claim you rely on gets at least the independent check. Not "low-stakes claims need no check" |

Pushback (8.4): a flip under pushback is a warning sign; holding firm is no evidence either way (in Mata the replies held firm and were wrong, ¶ 45; links to M3).

## 5. Concept sequence

**Session question, answered in the Summary:** *How do you know when an AI output is true enough to use?* Not from the output itself. Signals tell you where to look first; only a check against evidence no AI tool produced tells you whether a claim holds, taken as far as the stakes require, with what remains uncertain written down. How much to trust a source is Chapter 9's question.

**Each appearance of Mata has one job** (Decision 17): Opening Case = the facts; 8.3 = the three citation checks on "Varghese"; Case Study = tree and chain labels, the funnel stage that would have stopped each failure, and a better workflow; Ethics Lens = the costs the court named; Lab 8.1 = excerpts only. F8.2 (timeline) appears once, in the Opening Case.

**Opening Case (450–600 words).** Facts only from ECF 54 and 55. Mata's injury claim (metal serving cart, flight from El Salvador to New York, August 2019; ECF 55 p. 1; ECF 54 ¶ 1); the motion to dismiss as time-barred (¶ 3); March 1, 2023 filing citing decisions (¶ 5); March 15 reply: cases not found (¶ 7); April 11–12 orders (¶ 13); April 25 affidavit with excerpts (¶¶ 20–22); six decisions found not to exist and generated by ChatGPT (¶ 36); the researching lawyer's testimony (¶¶ 11–12) and his questions to ChatGPT (¶ 45); June 22, 2023: bad faith, $5,000 penalty jointly, letters to the client and to each falsely named judge (Conclusion); the same day, the claim dismissed as time-barred in a separate opinion (ECF 55), not because of the fake cases. People by role; one 12-word quotation (p. 1: "nothing inherently improper about using a reliable artificial intelligence tool for assistance"). Close, dated: as of October 2026, a public database (Charlotin, 2026) listed more than 2,000 court decisions addressing hallucinated content in filings [VERIFY count at drafting]. **Chapter question:** "The lawyer asked the tool whether the cases were real, and it said yes. What check would have caught them, and when?" Answered in 8.3 (the checks) and the Case Study (the stage).

**Prediction before the evidence (8.3):** "Out of 100 references GPT-3.5 produced for short literature reviews in 2023, how many do you think did not exist?" Revealed: 55, and 18 for GPT-4 (Walters & Wilder, 2023).

**Definitions fixed here (for Ch. 9 and the glossary).** **Claim:** one statement in an output that you might rely on; marked *checkable* (it can be true or false) or *not checkable as true or false* (a judgment, a recommendation, a prediction). **Independent check:** evidence that no AI tool produced: a source with an author or publisher you can name, or your own recalculation or reasoning from known inputs. **Primary source:** the original record a claim comes from (the study, dataset, law, court record, official page). **Fabricated citation:** a citation to a work that does not exist (failure 1 only). **Verdict scale:** supported · partly supported · unsupported · contradicted · cannot verify.

**Verdict rule for citations (8.3, worked line, one Review A item).** An authoritative record (the court, the publisher, the DOI registry) shows that the work does not exist or that its details belong to another work → **contradicted**. Not found in two indexes that no AI tool produced → **unsupported**, and the uncertainty line names the indexes searched ("not in X or Y; may be unindexed"). Found, but the passage does not support the claim → **unsupported** (or **contradicted** if the passage says the opposite). Found and the passage supports it → **supported**.

| # | Subsection | Tag | One new core idea | Examples (worked ≤ 150, faded ≤ 80 words) | Figures |
|---|---|---|---|---|---|
| 8.1 | From an answer to claims (≤ 600) | Core | Recall (two sentences): Ch. 4 showed that producing likely text involves no truth check and that patterns recombine, so errors sit inside fluent text. **You verify claims, not answers.** Split one fact per claim; mark checkable or not; type (fact, number, citation or quotation, reasoning step; judgment or prediction = not checkable); rank by stakes. Min et al. (2023). M1 | **Worked:** Lucía's constructed CPA-exam overview → six claims, marked and ranked (F8.3). **Faded:** steel yield-strength paragraph, three of five claims split. **Your Turn = A5 rows:** split your pre-lab output into ten claims | F8.3 |
| 8.2 | The Verification Funnel (≤ 750) | Core | **Signature 8.** Stage 1 **independent check** (a source no AI tool produced, with a nameable author or publisher, or redoing the calculation yourself); stage 2 **primary source**; stage 3 **expert** (asked for reasons). Stop when the evidence matches the stakes. Verdicts as a five-row table, one example each. A line of remaining uncertainty. An AI search tool may help *find* a source; the verdict rests on the opened source (Decision 15). One hand-off sentence to Ch. 9. M6 | **Worked:** Lucía's "four sections, including BEC" claim: stage 1 (a review-course page) → stage 2 (the exam administrator's page) → stop; *contradicted*, labeled outdated information; uncertainty line [VERIFY CPA facts]. **Faded:** a nursing student's drug-interaction claim: stages 1–2 filled; reader decides on stage 3 and writes verdict and uncertainty. **Your Turn = A5 row 1** | F8.4 master (caption maps Ch. 1's four steps onto stages 1–2) |
| 8.3 | Checking citations and quotations (≤ 850) | Core | Three ways a citation fails, three checks: (1) **it does not exist** (search an index no AI tool produced); (2) **it points to another work** (match every detail to the record); (3) **it exists but does not say what is claimed** (open it, find the passage). Verdict rule (above). Rates: Walters & Wilder (2023); retrieval-based legal tools still erred on 17–33% of queries (Magesh et al., 2025), one clause. Never the tool's own yes (M3). Passage vs. summary line. One pointer: the Case Study labels the case | **Worked:** "Varghese" through the three checks with the court's findings (¶¶ 26–29). **Faded:** Lucía's Enron and Sarbanes-Oxley paragraph with three references (one checked; reader checks a real article with wrong details and a constructed nonexistent one) [VERIFY the real article]. **Your Turn:** Lab 8.2. M2, M3 | F8.5; F8.6 |
| 8.4 | Uncertainty signals: where to look first (≤ 550) | Core | Signals order your checks; none settles a claim: (1) stated confidence (weak, often too high; 8.5); (2) the **consistency check**: the same question in fresh chats (Ch. 3 recall); disagreement = warning, agreement ≠ proof (Manakul et al., 2023; Farquhar et al., 2024); (3) pushback (Ch. 4's test): a flip = warning, holding firm = no evidence; (4) precise detail about something rare (Ch. 1, Ch. 4). Record signals in A5 *before* checking | **Worked:** what the signals would have shown Lucía *before* she checked: three fresh runs, two repeating the four-section structure at "95%", one different (constructed). **Faded:** a history student's quotation: three agreeing runs at 90%; reader names what the signals justify and the next stage. **Your Turn:** Lab 8.3. M4 | F8.7 three-run panel |
| 8.5 | Measuring calibration (≤ 600) | Core | Ch. 7's model-sense clause verbatim: **calibration (of a model)** = how well a model's stated confidence matches its accuracy. Measure it: known-answer items, stated confidence before checking, groups (50–69, 70–89, 90–100%), each group's share correct vs. its confidence; on a chart, points below the diagonal = overconfidence (glossary term). Published evidence: Xiong et al. (2024); Wei et al. (2024). Ten or twenty items = a rough picture. The **calibration gap**, as in A4, for you and for the tool. One sentence: "I don't know" is a valid answer (Ch. 4 Deep 4.A). M5 | **Worked:** a constructed 30-item record (data/ch08_calibration_toy.csv) and F8.9. **Faded:** Lucía's ten accounting study questions: two groups filled; reader fills one and the conclusion. **Your Turn:** Warm-up 3 revisited; A5 confidence columns | F8.9 |
| 8.6 | The verification lab and A5 (≤ 450) | Studio | One row per claim; what a strong table shows and a weak one looks like; the rows you already wrote in 8.1–8.2 | **Worked:** two of Lucía's completed rows (a citation, a number). **Faded:** a half-filled row. **Your Turn:** Lab 8.1 and A5 | F8.13 |
| Deep 8.A | Judging an automatic checker | Deep | Precision and recall (Ch. 2) for any checker; a model checking itself: verification questions answered separately reduced hallucinations on several tasks (Dhuliawala et al., 2024); revising without outside feedback often did not help on reasoning tasks (Huang et al., 2024). Book's inference: a checker is a signal, not a stage | Constructed reference checkers (data/ch08_checkers.csv) | F8.14 |
| Deep 8.B | How researchers measure calibration | Deep | Reliability diagrams and expected calibration error (Guo et al., 2017); stated confidence vs. answer frequency over repeated samples (Wei et al., 2024; Kadavath et al., 2022); why results age | — | (text; reuses F8.9) |

Other anatomy parts:

| Part | Plan |
|---|---|
| Case Study (1 main + 2 short) | **Main (Mata, C05):** labels on the tree (F8.11: hallucination, leaf "invented facts or sources", documented ¶ 36; overconfidence, leaf "certainty beyond the evidence", documented because, asked directly whether the cases were real, the replies said they were and named databases where they could be found, ¶ 45, which is a statement of certainty about the claim; contrast with Moffatt's plain instructions in Ch. 4) and on the chain (F8.12: link 2 failed, documented ¶¶ 6, 12); the funnel stage that would have stopped each failure (F8.4d: stage 1 for "Varghese", ¶ 12; stage 2 for the borrowed citation and docket, ¶ 28; the signer's own reading, ¶ 6); a better workflow through the Work Loop at the firm's level. **Short 1:** *Kohls v. Ellison* (D. Minn. Jan. 10, 2025, ECF 46): expert declaration with two nonexistent articles and wrong authors for a third, attributed to GPT-4o; declaration excluded; leave to amend denied. Faded labeling (tree given; reader adds chain link and documented/inferred). Lesson: an expert's statement is evidence to check. **Short 2 (non-legal):** the May 2025 syndicated "summer reading list" in two U.S. newspapers that recommended books that do not exist [VERIFY primary reporting, counts and statements]. Label: hallucination, invented facts or sources (documented); chain link 2 (no check by the writer or the publishers), documented if the statements say so |
| Ethics Lens | **Who pays for an unchecked claim?** The court's list of costs (paraphrased, ECF 54 pp. 1–2): the other side's time and money, the court's time, the client's lost chance to argue from real precedent, the reputations of judges falsely named, public trust. Checking is cheap for the writer and expensive downstream. Free verification routes. A fabricated source stays unacceptable even if disclosed (Ch. 1); an honest "cannot verify" is acceptable |
| Career Connection | Paralegal or legal researcher; journalist or fact-checker; reference librarian; auditor or staff accountant (Lucía's path: tracing amounts to source documents; audit standards treat evidence from knowledgeable independent sources as more reliable [VERIFY PCAOB AS 1105]; pointer to Ch. 9); clinical pharmacist; data analyst. Descriptive only |
| From the Field | Şeker (2015), *IEEE Access* 3, 368–380. Facts limited to the paper (classical Delphi: rounds, facilitator, aggregation, feedback; its stated weakness: numbers without arguments; Argument Delphi; the petroleum-price test: more than 100 responses, 63 clean; "first come gets higher attention"; spam handled by moderation and a report button). Present-day connection, marked as the book's: at the expert stage ask for reasons; Delphi-style methods combine disagreeing experts; a consistency check is a numbers-only round. Not commercial; no D16 |
| Summary + Key Terms | Answers the session question; complete funnel with verdict scale (F8.4s); summary card F8.15; Warm-up revisited. **Key Terms (Core):** claim · verification · Verification Funnel · independent check · primary source · verdict (verdict scale) · remaining uncertainty · fabricated citation · uncertainty signal · consistency check · stated confidence · calibration (of a model). Deep: expected calibration error |

## 6. Example plan (worked → faded → your turn)

| Skill | Worked | Faded | Your Turn |
|---|---|---|---|
| Decompose (O1) | Lucía's CPA overview, six claims | Steel paragraph | **A5 rows:** your ten claims |
| Funnel (O2) | Lucía's BEC claim | Drug-interaction claim | **A5 row 1** through the funnel |
| Citations (O3) | "Varghese" (court findings) | Sarbanes-Oxley paragraph | Lab 8.2 |
| Signals (O4) | Lucía's three runs, before checking | History quotation | Lab 8.3 |
| Calibration (O4) | Constructed 30 items, F8.9 | Lucía's ten study questions | Warm-up 3; A5 columns |
| Diagnose (O5) | Mata labels and stopping stages (Case Study) | Kohls (Case Study) | One A5 claim that failed |
| A5 (O6) | Two of Lucía's rows | Half-filled row | Lab 8.1; A5 |

Fields: accounting (Lucía), law (Mata, Kohls), engineering (steel), health (drug interaction), history (quotation), journalism and publishing (reading list), plus each student's field. Every constructed output labeled; real outputs carry model and date. Lucía uses study tasks only (no customer data).

## 7. Retrieval and spacing

- **Warm-up:** (1) A chatbot gives a reference with authors, year, journal and pages. Does that make it likely the paper exists? (2) You ask the same chatbot "Is this source real?" and it says yes. Is that a check? (3) A tool says it is 90% sure of each of ten answers. How many would you expect to be right?
- **Check Yourself** after 8.1–8.6, 2–3 items each, at least one "why", all answerable from Core.
- **Spaced Review** (4): Ch. 4 ×2 (a fabricated reference: which branch and leaf, intrinsic or extrinsic?; why is overconfidence labeled only with evidence about expressed certainty?); Ch. 7 ("two meanings, one habit: predict, then check": what is calibrated in A4, and what in A5?); Ch. 5 (one result is not evidence: why does one agreeing re-run not settle a claim?).
- **Failure Diary link:** an A5 claim that fails can become a diary entry (first version due Feb 25).
- **Spaced forward:** Ch. 9 (funnel reused; the L8.2 record feeds A6's source audit); Ch. 10, 11 (funnel reused); Ch. 12 (verification cost in tool choice); Ch. 13 (deepfakes); Ch. 14 (approval gates); Ch. 18 (liability).

## 8. Alignment matrix

| Objective | Taught | Practiced | Figures | Assessed | Artifact |
|---|---|---|---|---|---|
| O1 | 8.1 | Claim sequence; A5 rows | F8.3 | Review A; B1 | A5 claim columns |
| O2 | 8.2 | Funnel sequence; Lab 8.1 | F8.4 | Review A; B2; C1; C3 | A5 stage, source, verdict, uncertainty |
| O3 | 8.3 | Citation sequence; Lab 8.2 | F8.5, F8.6 | Review A (incl. the verdict rule); B3 | A5 citation rows |
| O4 | 8.4, 8.5 | Signals, calibration; Lab 8.3 | F8.7, F8.9 | Review A; B4; C2 | A5 confidence columns, calibration gap |
| O5 | Case Study (Core recall of Ch. 4 rules) | Mata, Kohls | F8.4d, F8.11, F8.12 | Case Study Questions | A5 failed-claim label |
| O6 | 8.6 | Lab 8.1 | F8.13 | Application Assignment | **A5** |

Note on O5: the labeling rules are Chapter 4 Core; the Case Study applies them. O5 is assessed in Case Study Questions and the A5 label, not in Review A–C. Counts: Review A 13 (distractors from M1–M6; items on the three citation failures, the verdict rule, the verdict scale, reading a calibration chart), B 4, C 3 (C1: should the stopping point depend on who bears the cost of an error? O2; C2: is a tool's stated confidence worth showing users? O4; C3: "verification takes longer than writing it yourself, so AI saves no time" O2), Spaced 4, Discussion 5, Case Study Questions 5, optional Mini-Project. No item tests Deep 8.A–8.B (D20).

## 9. Application Assignment — A5 Claim Verification Table

**Due** Mon Feb 22, 2027, 11:59 p.m. *(O6 · LO3 · Create)* Rows 1–10 started in the 8.1–8.2 Your Turns; three claims checked in Lab 8.1; finished at home (~45–50 min; times per claim given in the brief).

**What to submit:** (1) the output (prompt, full output, tool and date; from your field; naming at least two sources; no personal or confidential data); (2) ten claims, one fact per row, each marked checkable or not, typed, stakes-rated with a reason; at least two citations or quotations and one number; at most two not-checkable claims, with what evidence would bear on them; (3) before checking: your confidence and the tool's stated confidence or signal (ask it, or a three-run consistency check for at least three claims); (4) the check: stage reached (independent check / primary source / expert), source(s) with link or location, and for citations which of the three checks you ran; **at least three claims at the primary source, including every citation**; the tool's own yes never counts; (5) verdict (book scale) and a remaining-uncertainty line for every claim; a corrected statement for every claim not supported; (6) **calibration gap:** of your ≥ 80% claims and of the tool's, how many were supported; one sentence on the gap (a rough picture); (7) one failed claim labeled on the tree, or, if none failed, the claim that came closest with a reason; (8) reflection 100–150 words (best-predicting signal; one stopping-point judgment; what you will check first next time); (9) AI Use Declaration (five elements).

**Rubric (10 points)** — course split (task 3, process evidence 3, verification 2, declaration and judgment 2).

| Criterion (points) | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| **Task (3)** | 3: dated output from your field with prompt and tool; ten one-fact claims, each marked, typed and stakes-rated with reasons; two citations or quotations and one number; at most two not-checkable claims, marked | 2: all parts present; one weak (e.g., two rows hold two facts, or stakes without reasons) | 1: one required part missing (prompt or date, two citations, the number, stakes), or seven to nine claims | 0: two or more parts missing, or fewer than seven claims |
| **Funnel record (1.5)** | 1.5: every claim has a stage, a source no AI tool produced (or a recalculation) with link or location, and a stage fitting its stakes; three or more at the primary source including every citation | 1: exactly one claim without a source, or one stage that does not fit the stakes, or one citation not taken to the primary source | 0.5: two or three claims without sources, or the tool's own answer used as a source once or twice | 0: four or more claims without sources, or the tool's answers used as sources three or more times |
| **Confidence record (1.5)** | 1.5: both confidence columns for all ten claims, recorded before checking; calibration gap computed correctly; one specific sentence on it | 1: both columns for eight or nine claims; gap computed; sentence general | 0.5: both columns for fewer than eight claims, or one column missing, or no gap | 0: no confidence record |
| **Verification (2)** | 2: every verdict follows from the cited evidence and the book's rule; citation checks reported for each citation; specific uncertainty lines; accurate corrected statements for every unsupported claim | 1.5: verdicts follow; one citation check, one uncertainty line or one correction missing | 1: two or more verdicts not supported by the evidence, or citation checks reported only as "found", or corrections missing for two or more claims | 0: verdicts without evidence, or no corrections |
| **Declaration and judgment (2)** | 2: five declaration elements; reflection names the best-predicting signal, one stopping-point judgment and one concrete change, with specifics from the table; the failed claim, or the closest claim with a reason, correctly labeled | 1.5: five elements; reflection covers all three points, one general; or the label imprecise | 1: two to four elements, or reflection missing two points, or no label | 0: zero or one element |

**Alternative assignment:** a dated sample output on eLearning (real output with model and date, ~400 words, ≥ 12 claims incl. three citations and the tool's stated confidence per claim). Choose ten claims; items 2–9 as above (record your own confidence; copy the tool's from the sample). Same rubric; *Task* = your ten claims from the sample.

## 10. Figures (titles state the finding; ≤ 9 boxes; color + gray)

| ID | Title | Type | Section | Objective |
|---|---|---|---|---|
| F8.1 | Chapter 8 at a glance | Chapter map with the Work Loop strip (Verify, Decide second) | Opening | all |
| F8.2 | Six invented cases went from a chatbot to a sanctions order in under four months | Storyboard (dates from ECF 54); Opening only | Opening Case | O5 |
| F8.3 | One fluent paragraph held six separate claims, and only some of them were right | Annotated claim split (constructed) | 8.1 | O1 |
| F8.4 | Take each claim only as far as its stakes require | **Signature 8** `verification_funnel(highlight=None, verdict=None, tag=None, note=None, notes=None)`: hexagon output → Claims → 1 Independent check → 2 Primary source → 3 Expert (rounded); a side rail "stop when the evidence matches the stakes" into Verdict; dashed Remaining uncertainty (7 boxes). Variants: F8.4d (Mata, stopping stages, Case Study), F8.4s (Summary, verdict scale) | 8.2, Case Study, Summary | O2, O5 |
| F8.5 | A citation can fail in three ways, and each needs a different check | Three-column table-figure, Mata examples ¶¶ 26–29 | 8.3 | O3 |
| F8.6 | In one 2023 test, GPT-4 invented fewer references than GPT-3.5, but not none | Bar chart, published values (data/ch08_citations.csv) | 8.3 | O3 |
| F8.7 | Answers that change across fresh runs are a warning sign; answers that agree are not proof | Three-run panel (constructed); caption points to Signature 4 | 8.4 | O4 |
| F8.9 | This constructed tool's "90–100% sure" answers were right only 9 times in 15 | Computed chart (constructed data) with diagonal | 8.5 | O4 |
| F8.11 | The Mata citations on the tree: invented sources, stated as real | `failure_tree({"hallucination", "overconfidence"}, tag=...)` | Case Study | O5 |
| F8.12 | The fake cases reached the court because no one checked them outside the tool | `failure_chain(notes=..., highlight={1}, tag=...)` | Case Study | O5 |
| F8.13 | A verification table records how far each claim got, not only a verdict | A5 template | 8.6 | O6 |
| F8.14 | A checker that flags everything catches every fake reference but wastes your time | Constructed precision/recall comparison | Deep 8.A | (Deep) |
| F8.15 | Chapter summary card | Summary card | Summary | all |

13 figures, 15 renders. Cut: F8.4b and F8.4c (one Signature 8 render per section), F8.8 (redundant table), F8.10 (published calibration values not readable as numbers; the finding stays in the text).

## 11. Labs (tool-neutral)

| Lab | Type | Time | Task | Output |
|---|---|---|---|---|
| **L8.1 Ten Claims** | Studio | Thu Feb 18: briefing 10 · practice 45 · share 15 · exit 5 | Briefing: R6 pp. 1–2 and excerpts ¶¶ 11–12, 25–28, 45. Practice part 1 (15): teams check the Tuesday demo's sources and a provided dated output, citations first. Part 2 (30): each student checks **three** of their own A5 claims, citations first. Share: one verdict that changed at the primary source; a pooled class calibration gap from the shared set. Exit: one claim you could not verify, and the stage that would settle it | Team record; A5 with three checked rows |
| **L8.2 Five References** | Check It | 30 min, home, optional | Ask for five references on a narrow topic in your field; run the three checks on each; keep the record for Chapter 9's source audit (A6) | Five-row citation record |
| **L8.3 Signals versus Truth** | Break It | 35 min, home, optional | Ten provided known-answer questions (field packs); stated confidence for each; three in three fresh chats; score against the key; group and compare | Calibration table + three-sentence conclusion |

Accessibility: dated sample outputs (no-device route); keyed packs with sample outputs; screen-reader tables; free verification routes; no personal data; tell a librarian or instructor when a claim came from an AI tool.

## 12. Risks and checks

- Mata facts only from ECF 54–55; one quotation; roles not names; dismissal separate; no ChatGPT version named; no appeal found (refresh-list).
- Rates with model, year, task, sample; never pooled across studies; F8.6 from one study.
- Calibration wording verbatim from Ch. 7's model-sense clause; metric in Deep only; toy labeled constructed; numbers from data/ch08_*.csv.
- Ch. 4 overlap: recall only; exact leaf names from ch04_figures.LEAVES. Ch. 9 overlap: no ladder, no lateral reading, no summary fidelity, no Deloitte.
- CPA facts verified against primary pages and dated; the constructed reference checked against indexes so that it matches nothing real.
- No anthropomorphic verbs ("the replies said", "the output contains").
- Lucía only; new details logged.

## Decisions taken under delegation (D19)

| # | Decision | Reason |
|---|---|---|
| 1 | Mata facts only from ECF 54–55; people by role; one 12-word quotation | Primary record; teaches roles; quotation rule |
| 2 | Signature 8: four bands, side stop rail, verdict, dashed uncertainty (7 boxes); `verification_funnel(highlight, verdict, tag, note, notes)`; `highlight` takes a name or list | Reuse in Ch. 9–11; no crossing lines |
| 3 | Verdict scale book-wide; the book's own fact-check example goes to "How This Book Was Written" (editor), not 8.2 | One vocabulary; 8.2 cap |
| 4 | Definitions fixed here: claim, independent check (nameable author or publisher, not produced by any AI tool, or recalculation), primary source, fabricated citation (failure 1 only); Ch. 9 ranks sources | Clean hand-off; A5 is due before Ch. 9 |
| 5 | Calibration (of a model) = Ch. 7's clause verbatim; sense-labeled glossary row; A5 "calibration gap" | Terminology consistency (brief) |
| 6 | Workload: R6 pp. 1–2 in the lab briefing; R5 to Further Reading; Your Turns = A5 rows; primary minimum 3; reflection 100–150; lab goal three claims; diary first version Feb 25 (editor) | ≤ 2.2 h |
| 7 | From the Field: Şeker (2015), *IEEE Access*; the 2014 Delphi entry not used | One source per chapter |
| 8 | Short cases: Kohls (2025) and the 2025 summer reading list; Magesh in one clause in 8.3; Chelli in Further Reading | One legal short, one non-legal; no redundant study |
| 9 | C05 labels: hallucination (invented facts or sources, documented ¶ 36) + overconfidence (certainty beyond the evidence, documented ¶ 45, reason stated); chain link 2 (documented ¶¶ 6, 12) | Ch. 4's rule applied with its evidence |
| 10 | Work Loop: Verify, Decide second | Verdict → keep/change/reject |
| 11 | Precision and recall in Deep 8.A | Ch. 2's promise |
| 12 | Calibration chart from a constructed toy | Reproducible; real evidence cited in text |
| 13 | Database count, dated, once | Not isolated; ages fast |
| 14 | A5 on the student's own output; ten claims; two citations; three at primary | Syllabus "ten claims"; LO3 |
| 15 | AI search may find, never verify; the tool's own yes is never a source | Mata ¶ 45 |
| 16 | Lab 8.1 starts from Tuesday's demo cards | Completes the syllabus demo |
| 17 | **One job per Mata appearance** (Opening facts; 8.3 checks; Case Study labels, stopping stages, workflow; Ethics costs; Lab excerpts) | Redundancy, as Ch. 4 D7 |
| 18 | Verdict rule for citations not found (contradicted vs. unsupported) | Most common A5 judgment |
| 19 | Pushback: a flip is a warning; holding firm is no evidence | Mata ¶ 45 |

**For the editor:** (a) ftf-sources.md row (Ch. 8: Şeker 2015); (b) R5 to Ch. 4 Further Reading, Failure Diary date Feb 25 (Ch. 4 files); (c) glossary: "Calibration (of a model)" beside Ch. 7's "Calibration (of your confidence)"; claim, independent check, primary source for Ch. 9; (d) C05 index row (handoff); (e) Ch. 9: `verification_funnel`, the verdict rule, the passage/summary line; Deloitte (C06) labeled with failure 1 in one sentence there; the L8.2 record feeds A6; (f) the fact-check sentence for "How This Book Was Written".

**Author-only items:** (1) live syllabus: R6 read in the lab; R5 recommended only; A5 brief; (2) optional verification story from your own editorial or SME work for From the Field; (3) final voice edit.

## Open [VERIFY] items

1. Walters & Wilder (2023): article number, counts behind the percentages. 2. Magesh et al. (2025): exact range wording. 3. Xiong et al. (2024) and Wei et al. (2024): wording in the published versions. 4. Kadavath, Huang, Dhuliawala, Guo: abstract-level only. 5. CPA facts (AICPA, NASBA, Texas board). 6. Faded-example references. 7. Mata: no appeal; no model version. 8. Kohls: judge and pages. 9. The 2025 reading list: primary reporting. 10. PCAOB AS 1105. 11. Charlotin count. 12. Min et al. (2023) setting.

## Review changes (v0.1 → v0.2)

Workload recounted (rows 1, 16): Your Turns 8.1–8.2 become A5's first rows; R5 to Further Reading; primary-source minimum 3 incl. every citation; reflection 100–150 words; Lab 8.1 goal three checked claims; L8.2 30 min (record kept for A6), L8.3 35 min; Failure Diary first version Feb 25 (editor); total ~2.0–2.1 h. One idea per section (rows 2, 6): 8.3 = three failures + Varghese + Sarbanes-Oxley faded + Walters & Wilder (Magesh one clause, Chelli to Further Reading); labeling, F8.11–F8.12 and Kohls moved to the Case Study; F8.4b–c cut; fact-check sentence out of 8.2; Kohls caveat out of 8.2; verdicts as a table; worked ≤ 150 words; Check Yourself outside the caps. Mata one job per appearance (row 3; Decision 17). Calibration (rows 4, 5): Ch. 7's model-sense clause verbatim; sense-labeled glossary row; Spaced Review "two meanings, one habit: predict, then check"; A5 "calibration gap". Definitions (rows 7–11): claim = a statement you might rely on, marked checkable or not; stage 1 = independent check incl. recalculation, with the nameable-author-or-publisher guard; passage vs. summary line; verdict rule for unfound citations (Decision 18). Ch. 4 consistency (rows 12, 13): overconfidence evidence stated (¶ 45) with Ch. 4's leaf names; pushback flip = warning, holding firm = no evidence. Rubric gaps closed (row 14). Review C remapped; O5 assessed in Case Study Questions (row 15). 8.4 worked example reordered (row 17). F8.7 now a three-run panel (row 18). F8.4 side rail and new title (row 19). Warm-up 3 simplified (row 20). O1 "Decompose" (Analyze), O5 "Diagnose", tags trimmed (row 21). Magesh replaced by a non-legal short case (row 22). Key Terms trimmed; consistency check named; "fabricated" = failure 1 only (row 23). Prediction names GPT-3.5 (row 24). Blueprint shortened from about 10,400 to about 6,000 words.

## Post-draft changes (draft v2, 2026-10-18)

The four independent chapter reviews changed some blueprint details; the chapter and docs/editorial/ch08-dev-memo.md are now authoritative where they differ: Chapter 7's calibration clauses verbatim ("how closely…"); one A5 gap formula; A5 reflection 60–100 words, tool confidence as a stated percentage (one prompt), three-run check optional, row 1 checked in Lab 8.1; Your Turns 8.2–8.5 as two-minute A5 entries; verdict meanings for unsupported and cannot verify sharpened; citation checks 1–2 = stage 1, check 3 = stage 2; Mata's "is it real?" questions presented as undated on the record (¶¶ 46–47); Kohls and the reading list recommended; Lab 8.1 excerpts ¶¶ 12, 26, 45 with a 5-minute buffer; A5 verifies eight of its ten claims; week 5 counted at ≈ 2.3 h, a documented one-week exception (handoff D-8.10, book decision D21).
