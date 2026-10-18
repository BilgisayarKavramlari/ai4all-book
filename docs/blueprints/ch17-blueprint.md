# Chapter 17 blueprint — Explainability and Transparency

Status: **v0.2 (2026-10-18), APPROVED under delegation (D19).** v0.2 applies the independent blueprint review (build/ch17/reviews/blueprint.md: 5 High, 11 Medium, 4 Low) and the editor's decisions 1–8 (see "Review changes" at the end). v0.1 is kept in build/ch17/ch17-blueprint-v0.1.md; the v0.1 source notes and tier analysis are not repeated here. **Chapter v2 (2026-10-18):** where this blueprint and docs/editorial/ch17-dev-memo.md differ (route times, report time, AP facts now confirmed, simulation reporting, Lab 17.3, O2 wording), the dev memo and the handoff govern.
Part IV — Using AI Responsibly · Syllabus week 12 (shared with Chapters 15, 16 and 18) · Path: **Deep** (optional; **not examinable**, D20) · Featured student: **Sam** only (arc: "learns to explain a model's decision") · Work Loop highlight: **Disclose**, with **Verify** second.

**Sources (saved in build/ch17/src/).** C14 (editor-assigned): the Dutch childcare-benefits scandal. Confirmed tier: Parlementaire ondervragingscommissie Kinderopvangtoeslag (2020), *Ongekend onrecht* (read; pp. 7–9 findings, p. 11 scope, p. 14 the model). Reported tier: Amnesty International (2021), *Xenophobic machines* (read; chs. 4–5, §§7.2–7.3). The AP's 2020 report and 2021 fine are used only as recorded by the inquiry and Amnesty, or as reported by Dutch outlets (AP site refused download; [VERIFY] in the handoff). Law: CJEU C-203/22 and C-634/21 judgment texts (EUR-Lex, read 2026-10-18). From the Field: Şeker, HermAI (manuscript, 2025; Drive 1c_sgq7_xCtrgyF_9nZ1BWeLi4gXBAIXY; notes build/ch17/ftf-hermai.md); D16 disclosure.

**Deep-chapter pattern (Chapters 6, 13).** 17.1–17.7 Deep, 17.8 Studio; not examinable; fast and full routes in the Chapter Map; a plain-words box (≤ 12 terms, the rest glossed inline); every term defined in this chapter; Check Yourself answerable from each section; optional artifact with rubric and alternative; every worked and faded example printed in the book.

**Boundaries.** Ch. 2 (pipeline, feature, Sam's shortcut), Ch. 3 (reasoning tokens; attention "hard to interpret"), Ch. 4 (tree, chain, documented/inferred), Ch. 8 (independent check, primary source, calibration, an AI tool's "yes" is never a source), Ch. 11 (decision roles, decision owner, automated decision, automation bias), Ch. 14 (log vs. the agent's account) are recalled in their glossary wording. Ch. 15 (heat map, A12), Ch. 16 (Bias Lifecycle, two-part small-sample rule) are imported, not re-taught. **Ch. 18 owns law:** Ch. 17 has one dated box with two judgments and the Article 50 line; TRAIGA and AI Act Art. 13 are a one-line pointer. C14 is used only in Ch. 17. Ch. 19 must define "model card" itself (R16, week 13).

## 1. Outcome, week 12, workload

LO5 (LO3 secondary on O4; LO1 secondary on O2). Optional artifact: **Explaining-a-decision report** (ungraded). Optional **A12 transparency row** (Ch. 15). In-class time: 0 minutes. Readings: none. Examinable: no. Required week-12 time added: **0** (week stays at 132 min).

| Item | Words or count | Time (150 wpm; longer if English is not your first language) |
|---|---|---|
| Fast route (v2): Map + plain words, Opening, Warm-up, 17.1, 17.8 with recap, Summary | ~3,350 (v2) | **~22 min** |
| Full route (v2): Map through Case Study, labs excluded | ~9,180 (v2; over the 8,500 cap after accuracy fixes, recorded in the dev memo) | **~61 min**; ~70 min with Ethics, Career, From the Field, Summary |
| Labs 17.1 (~40 min), 17.2 (~25), 17.3 (~25), 17.4 (~20), including reading and debrief | — | optional |
| Artifact, per requirement: read brief and rubric ≈ 5; packet ≈ 8; decision, role, owner ≈ 6; layer audit ≈ 12; explanation ≈ 15; faithfulness record ≈ 10; contest and unknowns ≈ 6; revision ≈ 6; declaration ≈ 4 | — | **about 75 min (65–90)** (v2: + judgment item 3 min) |
| Optional A12 transparency row | 1 row | ~4 min |

**Budget per section (words):** Map + box 550 · Opening 450 · Objectives + Warm-up 300 · 17.1 800 · 17.2 650 · 17.3 900 · 17.4 700 · 17.5 850 · 17.6 900 · 17.7 850 · 17.8 600 · Case Study 750. Outside the full route ≈ 5,000 (labs, Ethics, Career, From the Field, Summary, package, reading) → total ≥ 12,500. Worked ≤ 120 words; faded ≤ 70 with the first step filled and every fact supplied; Your Turn ≤ 40.

## 2. Objectives

| # | Objective | Bloom | LO | Tags |
|---|---|---|---|---|
| O1 | **Explain** why people around an AI-supported decision need explanations (contest, debug, decide how far to rely) and which layer each needs | Understand | LO5 | 4D:DISC · UNESCO:ETH-U |
| O2 | **Classify** an explanation by scope (global, local) and kind (feature attribution, counterfactual, example-based, rule) | Understand | LO5 (LO1) | 4D:DISC · UNESCO:TECH-U |
| O3 | **Interpret** a feature attribution or a counterfactual, stating what it shows about the model and not about the world | Understand | LO5 | 4D:DISC · UNESCO:TECH-A |
| O4 | **Evaluate** whether an explanation is faithful, not only plausible, including a model's account of its own reasoning | Evaluate | LO5 (LO3) | 4D:DISC · 4D:DIL |
| O5 | **Examine** which transparency documents, notices and contest routes exist for a decision, as of a date | Analyze | LO5 | 4D:DIL · UNESCO:ETH-A |
| O6 | **Create** an explanation of an AI-supported decision for the person it affects, with a contest route | Create | LO5 | 4D:DIL · UNESCO:ETH-A · UNESCO:HCM-A |

## 3. Promises kept and plain-words box

Promises: Ch. 3 Deep 3.A (attention weights → 17.2), Ch. 5 Ethics ("Chapter 17 discusses transparency" → 17.7 notice), Ch. 11 §11.3 (how a score should be explained to the people it affects → 17.1, 17.8), Ch. 14 §14.7 (a log shows what, not why → 17.6), Ch. 15 §15.5 / A12 (optional transparency risk → §9), Ch. 16 §16.6 (people affected may need an explanation → 17.1).

**Plain-words box (12):** model; feature; proxy; reasoning tokens; decision owner; automated decision; the three roles (informs, recommends, triggers an action); automation bias; independent check; primary source; documented / inferred; risk owner. Everything else is glossed where it first appears.

## 4. Misconceptions

| # | Misconception | Confronted | Refutation check |
|---|---|---|---|
| M1 | "Giving people an explanation makes them trust the system the right amount." | 17.1 prediction: Bansal et al. (2021): explanations raised acceptance of AI recommendations whether right or wrong; Poursabzi-Sangdeh et al. (2021): a simpler, visible model made participants *less* able to catch its large mistakes | Not "explanations are useless": they help debugging (17.3) and contest (17.7) |
| M2 | "Publishing the code, or showing inputs and outputs, explains a decision." | 17.1–17.2 (C14 reviewers saw the score, not reasons); 17.7 (C-203/22 para 59: a complex formula alone is not enough) | Each layer answers a different reader |
| M3 | "Highlighted features are causes in the world." | 17.3 (an attribution describes the model; Lapuschkin et al., 2019), 17.4 | Attributions are evidence about the model, which is what debugging needs |
| M4 | "A clear, convincing explanation must be faithful." | 17.5 (Adebayo et al., 2018; Slack et al., 2020; fidelity and rerun demos) | Fidelity can be measured; glass boxes need no surrogate |
| M5 | "When a chatbot explains its reasoning, it reports how it reached the answer." | 17.6 (Turpin et al., 2023; Chen et al., 2025; Anthropic, 2025a) | The √0.64 case matched; reasoning text can help find errors, but it is a claim to check |
| M6 | "High-stakes decisions need black boxes, explained afterward." | 17.2 (Rudin, 2019, her argument and scope) | Hedged: an argument for structured-data, high-stakes settings |

## 5. Concept sequence

**Session question:** *When an AI system shapes a decision about you, what are you owed, and how would you know the reason you are given is the real one?*

**C14, one job per appearance.** Opening = facts and puzzle (a person reviewed every high-scoring application; why did that check not catch a score that used a citizenship indicator?). 17.1 = three audiences; the score's two roles (`decision_roles`). 17.2 = Amnesty's black-box definition (one sentence). 17.7 = the model's existence and logic were not public (reported). Case Study = labels, tiers, the government's reply vs. Amnesty, and the inquiry's larger finding. Ethics = who gets an explanation.

**Tiers fixed for drafting.** Confirmed (inquiry): after a 2013 fraud case the state secretary called for harder action; checks before payment; the system selected applications by a risk classification model that the report calls *zelflerend* ("self-learning", the report's quotation marks around "learns"), using several dozen indicators; selected applications were checked by hand (p. 14); the AP established that at least from March 2016 to October 2018 the processing was improper and discriminatory because nationality was used for the indicator "Dutch citizenship" (p. 14, as recorded); the inquiry's questions did **not** include nationality risk profiles or black lists (p. 11); its findings: the all-or-nothing approach, the group-wise approach and the intent/gross-negligence approach grossly violated the rule-of-law principle; fundamental principles of the rule of law were violated by legislature, executive and the administrative courts, which for years helped sustain the rigid practice (pp. 7–8); information from government was extraordinarily limited (p. 9). The cabinet resigned on January 15, 2021 (reported via Amnesty, citing government letter and press). Reported (Amnesty, citing the AP): model introduced in 2013; points per factor summed into a risk score; low scores approved automatically; highest scores to a civil servant, who got no information on why; selection led to suspension of payments and investigation; the government replied that considering citizenship did not mean nationality was a risk factor, and Amnesty rejects that reply; "tens of thousands" falsely accused. Reported (Dutch outlets): AP fine €2.75 million for processing dual-nationality data (decision November 2021). Inferred (marked): opacity disabled the link-2 check and the parents' contest; whether reasons shown to reviewers would have changed decisions is unknown.

| # | Section | Tag | One core idea | Worked → Faded → Your Turn | Figures |
|---|---|---|---|---|---|
| 17.1 | Who needs an explanation, and why (800) | Deep | An explanation is for someone and for a purpose: contest, debug, decide how far to rely. Defines explainability, appropriate reliance (Lee & See, 2004). Prediction box (Bansal; Poursabzi-Sangdeh). **Signature introduced.** C14 roles | C14's three audiences → hospital sepsis alert (nurse filled) → a decision about you | F17.3 signature, F17.4 C14 layers (five missing, contest partly), F17.5 roles |
| 17.2 | Black boxes, glass boxes, after-the-fact explanations (650) | Deep | Transparency, interpretability, explainability differ; some systems need no after-the-fact explanation (Rudin, 2019); attention weights are not explanations by themselves (Jain & Wallace, 2019; Wiegreffe & Pinter, 2019) | Scholarship screen built two ways → early-alert rule list → classify four explanations | F17.6 |
| 17.3 | Global and local: what attributions show (900) | Deep | An attribution shows how much a model leaned on each input, for one decision or many; it describes the model, not the world. LIME, SHAP at intuition level; baselines in one clause; one debugging case: Lapuschkin et al. (2019) | Sam's replica sorter (simulation) → health: chest X-ray markers (DeGrave et al., 2021) → attribution chart for a house-price model | F17.7, F17.8 |
| 17.4 | What would have to change (700) | Deep | A counterfactual says what would change the outcome; it helps only if a person can act on it. Wachter et al. (2018), recourse (Ustun et al., 2019), several valid counterfactuals (Mothilal et al., 2020), example-based in one paragraph | Loan pre-screen counterfactual (simulation: both searches found debt ratio −0.01) → rental application → write one actionable counterfactual | F17.9 |
| 17.5 | Plausible is not faithful (850) | Deep | Faithfulness must be tested. Jacovi & Goldberg (2020); Adebayo et al. (2018); Slack et al. (2020); Alvarez-Melis & Jaakkola (2018) for *similar inputs giving different explanations*; rerun variation shown only by the simulation | Fidelity and reruns (simulation) → museum saliency sanity check → three questions | F17.10, F17.11, F17.12 |
| 17.6 | When a language model explains itself (900) | Deep | A model's account of its reasoning is generated text: a claim to check. Turpin et al. (2023; the suggested-answer design Lab 17.1 adapts); Chen et al. (2025: 25%, 39%); Anthropic (2025a: arithmetic self-description mismatch; √0.64 matched; hint-driven working backward; fraction captured). Dated box: Baker et al. (2025, OpenAI) and Korbak et al. (2025, many labs) on monitoring reasoning text | Sam's hint test on a materials question → paralegal's clause reason → Lab 17.1 | F17.13, F17.14 |
| 17.7 | Transparency documents and your right to contest (850) | Deep | Documents and duties let others check a system; a right matters only with a person who can change the decision. Model cards, datasheets, system cards, registers; five contest questions. **Dated box (≤ 4 items):** GDPR Art. 22 and the pre-2023 debate (history); C-634/21 (operative test: a third party "draws strongly on" the score); C-203/22 (operative point 1, paras 58–62, point 2); AI Act Art. 50 per the book-wide rule; one-line pointer for TRAIGA and Art. 13 → Ch. 18 | Read a model card on eight fields → newsroom corrections page → five questions | F17.15, F17.16 |
| 17.8 | Explaining a decision to the person it affects (600) | Studio | Recap box; the report's six parts | Sam explains the travel-team decision; a second look by two officers who did not score her → campus shift scheduling → artifact | F17.17 |

**Case Study (750):** C14 labels: tree bias, documented (official finding, as recorded); chain link 2 failed (reported); link 3 reliance (reported); **link 4 harm reported (Amnesty)**; the inquiry's own findings presented separately as the larger failure, with its scope limit; opacity not a tree branch; lifecycle placement (data, use; feedback dashed = the book's reading; "self-learning" = the inquiry's description). Short 1: Slack et al. (2020). Short 2: Apple Card and NYDFS (2021; reported). **Ethics:** information asymmetry; recourse shifts burden (Barocas et al., 2020); fairwashing (Aïvodji et al., 2019). **Career:** lending analyst, clinical informatics, ML engineer or model-risk analyst, public-sector analyst, UX writer, internal auditor. **From the Field:** HermAI (manuscript), facts limited to the article (interpretive loop; local surrogate with counterfactual narrative; global tree surrogate; Titanic example output: change class 3 → 1 **and** fare 7.89 → 75.45; the article calls its counterfactuals actionable), D16 wording; a neutral, sourced caveat about counterfactual explanations in general (Barocas et al., 2020; Wachter et al., 2018); no critique of the article in the book text (author-only item).

## 6. Characters

Sam only. New details: builds a replica of his Ch. 2 sorter in a simulation; runs a hint test on a materials question (lightest metal; no units); is one of the robotics club's officers who choose a five-person travel team by a written rule (build hours, completed tasks, safety training) with an AI summary of build logs; asked for a second look, he refers it to two officers who did not score the member. The member is an unnamed first-year.

## 7. Retrieval

Warm-up 3 (third with confidence). Check Yourself 2–3 per section. Spaced Review: Ch. 16 ×2 (overall rate hides a group; fairness choice is a value choice), Ch. 15 (high-impact band), Ch. 14 (log vs. account) + Ch. 11 interleaving (roles). Forward: Ch. 18, 19, 20, 21, 22, 23.

## 8. Package and key terms

Review A 12 (keys rotated; correct option longest ≤ 2), B 4, C 2, Spaced 4 + 1, Discussion 5, CSQ 5, optional Mini-Project; "not examinable" line. Appendix E block: all Check Yourself keys, faded-example keys, odd answers; the chapter's time line ends with the standard sentence. **Key Terms (21):** explainability · appropriate reliance · transparency (of an AI system) · black box · interpretable model · post-hoc explanation · global explanation · local explanation · feature attribution · counterfactual explanation · recourse · example-based explanation · faithfulness (of an explanation) · surrogate model · fidelity (of a surrogate model) · chain-of-thought text · model card · datasheet (for a dataset) · system card · algorithm register · right to contest.

## 9. Optional artifact and A12 row

**Report** (about 75 min, 65–90, v2): decision, role and owner; six-layer audit (present / partly / missing, where you looked); the explanation for the person (≤ 150 words: decision, owner, reasons from the record, what would change it **or a statement that no actionable change exists**, unknowns, contest route); faithfulness record; revision after a read-aloud; declaration. Rubric 3 / 1.5 + 1.5 / 2 / 2, parallel levels, lower-level rule. Alternative: the "three explanations" packet (no AI use).

**A12 transparency row (optional).** Ch. 15's columns. Evidence: **documented only with pooled counts on the workflow's own tool and task that pass Ch. 16's two-part rule** (fair test with at least 10 runs per version; gap at or above the chance threshold); otherwise inferred. Lab 17.1's general-knowledge counts are a lead about the kind of tool, never evidence about a specific workflow. Sam's worked row: inferred.

## 10. Figures (22; titles from the data where computed)

New signature `explanation_layers(highlight, missing, partly, inferred, notes, note, title, audiences)` in ch17_figures.py: solid hexagon + six layers phrased as questions; missing = empty box with "missing"; partly = dotted frame with "partly"; inferred = dashed; default audiences printed; legend "layers, not steps". Imports: `decision_roles` (ch11), `verification_funnel` (ch08), `failure_tree`, `failure_chain` (ch04), `bias_lifecycle` (ch16), `risk_heat_map` (ch15). Dropped from v0.1: the pipeline reuse and the `llm_anatomy` reuse.

F17.1 map · F17.2 storyboard · F17.3 signature · F17.4 C14 layers · F17.5 roles · F17.6 glass vs. black box ("A post-hoc explanation studies a model from outside; an interpretable model is its own explanation") · F17.7 global vs. local · F17.8 occlusion (simulation) · F17.9 counterfactual · F17.10 fidelity (simulation) · F17.11 reruns (simulation) · F17.12 plausible × faithful · F17.13 Chen et al. (published values; Turpin in a note) · F17.14 funnel reuse · F17.15 documents (layers variant) · F17.16 contest route · F17.17 report card · F17.18 tree · F17.19 chain · F17.20 lifecycle · F17.21 heat map (Sam, inferred) · F17.22 summary card.

**Simulations (figures/scripts/ch17_experiments.py; methods fixed before the run; seeds in data/ch17_experiments_meta.txt).** Demo A: occlusion with a fixed baseline, change in log-odds from the model's scores, per-pixel summaries, the glass-box weight map as faithfulness check, and the background share of the exact positive contributions. Results: old model 100% on the same recipe, 73% on gray backgrounds (bolts 43%); background supplied 79% of the evidence for "bolt"; per pixel, part pixels mattered about twice as much as background pixels; after retraining on mixed backgrounds: 100% on gray, 66% from background (much of it where another part's ring would be). Demo B: surrogate fidelity 73.4 / 82.4 / 84.2 / 85.2% at depths 1–4; top feature split 6/4 (100 samples) and 5/5 (5,000), a near tie (weights differ by 0.004); the smallest counterfactual was the same in both searches (debt ratio −0.01), so the age-band point is taught conceptually and in Lab 17.3. The text reports these results as they came.

## 11. Labs

17.1 The Hint Test (Studio; ~35 min; three questions × two versions × three runs; after Turpin et al.'s suggested-answer design; printed outputs) · 17.2 Read a Card (20 min; one eight-field checklist) · 17.3 Open the Scorecard (Deep; 20 min; data/ch17_scorecard.csv) · 17.4 Contest It (15 min).

## 12. Risks

Never say the model caused the scandal; tiers as above; no individual named; Dutch paraphrased with "(the book's translation)"; interested sources labeled (Anthropic, OpenAI research on their own models); no anthropomorphic verbs; law dated and pointed to Ch. 18; "this book's simulation", never "this book's model".

## Decisions taken under delegation (D19)

X1 tags (17.1–17.7 Deep, 17.8 Studio) · X2 Disclose, Verify second · X3 route times as §1 · **X4 signature API as §10 (book-wide)** · **X5 opacity is not a tree branch; C14 = bias documented + link 2 reported + link 4 reported; the inquiry's findings kept separate (book-wide)** · X6 C14 one job per appearance, Ch. 17 only · **X7 faithful / plausible / fidelity (book-wide)** · **X8 a model's self-account is a claim (book-wide)** · X9 simulations reported as they came · X10 law box as §5 · X11 From the Field: HermAI as a manuscript, D16, no critique in the text · X12 artifact about 70 min · **X13 A12 row evidence = Ch. 16's rule on the workflow's own tool** · X14 Spaced Review as §7 · X15 Sam only · X16 shorts: Slack; Apple Card · X17 inquiry leads, Amnesty reported.

## Author-only items

1. HermAI: approve its use with D16; confirm publication status (cited as a manuscript); decide whether the book may note that the article's example counterfactual changes features a passenger could not change after the fact (the book's critique is not in the text). Optional anecdote, never invented.
2. No live-syllabus change. 3. Final voice edit.

## Review changes (v0.1 → v0.2)

High: link 4 reported, inquiry findings separate (1); contest layer "partly" with a new state (2); A12 evidence rule aligned with Ch. 16, Sam's row inferred (3); demo methods fixed before the run, titles from CSVs (4); law box on the judgment texts (5). Medium: Art. 86 out of the text, [VERIFY] in the handoff; Art. 13 and TRAIGA as a pointer (6); one debugging case, box ≤ 4 items, two figures dropped (7); plain-words box 12 terms (8); Alvarez-Melis & Jaakkola re-attributed (9); Demo B surrogate fitted to predictions and cost metric stated (10); F17.6 retitled (11); Turpin credited, working-backward and √0.64 added, F17.13 = Chen et al. (12); non-Anthropic box sources (13); signature states and audiences (14); 2013 and "seven years" tagged reported (15); lifecycle feedback dashed = the book's reading (16); dependencies now exist (17). Low: rubric accepts "no actionable change exists" (18); From the Field facts fixed, manuscript citation (19); new hint-test question, second look by other officers, O2 = Understand, one checklist, handoff Instructor package and Appendix E sentence (20). Blueprint trimmed from ~14,200 to ~3,600 words.
