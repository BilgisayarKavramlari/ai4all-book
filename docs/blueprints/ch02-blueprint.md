# Chapter 2 blueprint — How Machines Learn from Data

Status: v0.2 APPROVED by the author (2026-10-18). Chapter revision v2 (2026-10-18) moved the diagnosis table and paper task to the end of 2.5, cut F2.6, widened the A2 Chapter 2 pool to the Core Key Terms and added an A2 alternative assignment (docs/editorial/ch02-dev-memo.md). v0.2 applies an independent pedagogy review (5 must-fix, 15 should-fix) and the results of the book's own experiment. No chapter text is written until this blueprint is approved.
Part I — Understanding AI · Syllabus week 2 (shared with Chapter 3) · Path: Core · Featured student: Sam (Lucía and Hana in short examples) · Work Loop step highlighted in the Chapter Map: **Verify** (question the data behind an output).

**Author's source material.** The chapter follows the author's own English lectures at Haliç University — Lecture 2 "Concept Architecture" and Lecture 3 "Data: source, sampling, labelling and quality" (docs/context/halic/, internal): the session question answered at the end, a prediction before the evidence, build-then-break, the Amazon case, roles along the data pipeline. The lectures' "illustrative results" are replaced by **real, reproducible results** from the book's experiment (figures/scripts/ch02_experiments.py; data/ch02_*.csv).

## 1. Outcome link and week 2

| Item | Value |
|---|---|
| Syllabus outcomes | **LO1** (how AI systems work in outline and why they fail), **LO3** (judging reported performance), **LO5** (data responsibility) |
| Studio artifact | **A2 — 15-term concept map with worked definitions**, due Monday, February 1, 2027. The brief is hosted in this chapter (section 2.7, Part 1: at least 7 Chapter 2 terms) and completed with Chapter 3 terms |
| Reading order (proposal to the author) | Read Chapter 2 **before Tuesday, January 26** (it supplies the learning vocabulary for the concept session), and Chapter 3 before Thursday's "Probe the model" lab |
| In-class time (proposal to the author) | Tuesday's 10-minute opening case = the Amazon recruiting tool; 2–3 Chapter 2 items in Tuesday's ungraded concept check |
| Labs | Thursday's lab belongs to Chapter 3. Chapter 2's build-and-break labs are home/Compass labs (optional, recommended); a **paper task** at the end of 2.5 (Core, ungraded) gives every student the build-and-break reasoning without a tool |
| Readings | R1 Wolfram (2023): only the sections on "what is a model" and "neural nets" (~15 minutes) [VERIFY section titles]; the Gebru et al. excerpt is dropped (the datasheet questions are in the text) |

### Week 2 workload (out of class)

| Item | Time |
|---|---|
| Chapter 2 Core reading (~4,800 Core words incl. examples) | 25–30 min |
| Chapter 3 Core reading | 30 min (to be confirmed in the Chapter 3 blueprint) |
| R1, selected sections | ~15 min |
| Paper Task in 2.5 (Core, ungraded) | ~15 min |
| A2 at home (terms are drafted in Thursday's lab) | ~30 min |
| **Total** | **~2 h** (syllabus: 1–2 h) |
| Optional: labs L2.1–L2.3, Deep sections | 60–90 min |

**Documented week-2 exception (word budget).** Core subsections are ~650–800 words, below the anatomy's 1,500–2,500, because week 2 carries two chapters. Worked and faded examples sit inside the Core word count. The chapter still reaches ≥ 10,000 words with the Opening Case, Deep sections, Case Study, Ethics Lens, Career Connection, From the Field and the End-of-Chapter Package.

## 2. Chapter objectives (5)

| # | Objective — after this chapter you will be able to… | Bloom | LO | Framework tags |
|---|---|---|---|---|
| O1 | **Classify** a system as rule-based or learned from examples, and place generative AI and language models within the family of machine-learning approaches | Understand | LO1 | UNESCO:TECH-U · AI4K12:3 · LM:how-works |
| O2 | **Explain** how a supervised model learns: predict, measure the error, adjust its settings, repeat | Understand | LO1 | AI4K12:3 · UNESCO:TECH-U |
| O3 | **Diagnose** a data problem — sampling bias, noisy labels, biased labels, class imbalance, or a shortcut (proxy) clue — from its symptoms, and name a remedy, including documenting the data | Analyze | LO1, LO5 | AI4K12:3 · 4D:DISC |
| O4 | **Judge** whether a model's reported performance can be trusted, using held-out testing, overfitting and the minority-class score | Evaluate | LO3 | 4D:DISC |
| O5 | **Produce** a concept map of 15 core terms with labeled links and worked definitions (A2) | Create | LO1 | UNESCO:TECH-U |

## 3. Prerequisites and promises kept from Chapter 1

From Chapter 1: generative AI system, prompt, output, model (informal); jagged frontier; fluent vs. correct; AI Work Loop. **Chapter 2 keeps two Chapter 1 promises:** it gives "model" its formal definition (a set of learned settings that maps an input to an output, 2.2), and it adds a hedged elaboration of the jagged frontier (unevenness partly tracks what the training sample covered, 2.3). No programming or statistics needed.

## 4. Misconceptions (refutation pattern)

| # | Misconception | Where |
|---|---|---|
| M1 | "AI follows rules that programmers wrote" | 2.1 |
| M2 | "More data is always better data" (the 1936 poll) | 2.3 |
| M3 | "A few wrong labels don't matter" — or "all label errors are the same" (scattered vs. one-directional errors) | 2.4 |
| M4 | "High test accuracy means the model is right for the right reasons" (99.9% trap, shortcuts, overfitting) | 2.4, 2.5 |
| M5 | "Removing the sensitive column removes the bias" (proxies in the Amazon case) | Opening Case, 2.3 |
| M6 | "The model stores its training examples and looks answers up" (links to Ch. 1 M1; memorization vs. generalization) | 2.5 |
| M7 | "Deep learning and generative AI are a different, mysterious kind of thing" | 2.6 |

## 5. Concept sequence

**Session question (Lecture 2), answered in the Summary through Mitchell's operational definition of learning:** *Does the machine really learn, or does it just find the shortest path to the right answer?*

**Prediction before the evidence (Lecture 3), options written after running the experiment:** "One fifth of the training labels are wrong. How much accuracy does the model lose: about 5, about 15, or more than 20 points?" Answer in 2.4: *it depends on how they are wrong* — in the book's experiment (data/ch02_regimes.csv; three digit classes, logistic regression, 30 runs), 20% **scattered** wrong labels cost about 6 points (98.0% → 91.9%); the same 20% wrong **in one direction** cost about 23 points (→ 74.7%), and the affected class fell from 98.5% to 24.3%. Imbalance alone (10 vs. 60 examples) left overall accuracy at 91.7% but cut the minority class to 77.3%. A note tells students their own lab numbers will differ and why.

**Opening Case (400–600 words): the recruiting tool that learned the past.** From 2014, an Amazon team built a tool to score applicants from one to five stars, trained on about ten years of résumés, most from men. It learned to penalize résumés containing "women's" and graduates of some all-women's colleges; edits to neutralize specific terms did not guarantee fairness; the project was abandoned; Amazon said recruiters never relied on it alone (Dastin, 2018) [VERIFY every detail against the Reuters article]. Chapter question: there was no gender column — where did the model learn it from? Returns in 2.3 (proxy) and 2.4 (biased labels).

| # | Subsection | Tag | One new core idea | Examples | Figures |
|---|---|---|---|---|---|
| 2.1 | Writing rules or learning them | Core | People write rules, or people supply examples with answers and the machine finds the rule; Mitchell's (1997) task–performance–experience definition | Spam filter (everyday); **Lucía**'s support-ticket routing rules at work (business) | F2.2 |
| 2.2 | How a model learns | Core | The supervised learning loop; **model** formally defined; the Data-to-Prediction Pipeline as the chapter's skeleton. A small, non-examined reference table of learning and task types | **Sam** trains a classifier to sort robotics-club parts (engineering) | F2.3, **F2.4 Signature 3** |
| 2.3 | A model learns its sample | Core | The gap between population and sample (coverage, non-response, selection); big ≠ representative; **proxy** as a core term; hedged link to the jagged frontier | 1936 *Literary Digest* poll with Squire's (1988) correction; Amazon returns: no gender column, but proxies | F2.5, F2.4 (sampling stage highlighted) |
| 2.4 | Labels and balance | Core | **Noisy** (random) vs. **biased** (systematic, historical) labels; class imbalance and the 99.9% trap; the prediction answered with the experiment; **required paper "break it" task** (predict, read F2.9, diagnose) | Fraud detection (finance); Amazon labels = past hiring decisions | F2.4 (labeling stage highlighted), F2.6, **F2.9 computed** |
| 2.5 | Right for the wrong reasons | Core | Shortcut clues; held-out test set; overfitting (memorizing vs. generalizing); the minority-class score as the one extra number | **Sam**'s classifier learned the desk, not the part (Geirhos et al., 2020); memorizing last year's exam (study); **Hana** questions a "97% accurate" art-style detector (arts) | F2.7, **F2.10 computed** |
| 2.6 | Where generative AI fits | Core | Nested family: AI ⊃ machine learning ⊃ deep learning ⊃ generative AI ⊃ large language models; "deep" = many layers. Bridge to Chapter 3 (the next-token mechanism is taught there) | Pen vs. mug classifier vs. "draw me a cat" (Lecture 2) | F2.11 |
| 2.7 | Map the terms (A2) | Studio | How to build a concept map: terms, labeled links, worked definitions; A2 Part 1 drafted in Thursday's lab | Students' own maps | F2.12 |
| Deep 2.A | Why now? Three waves of AI | Deep | Dartmouth 1956; expert systems; 2012 image-recognition leap; 2017 Transformer; 2022 public generative AI; data, compute and algorithms maturing together | History | F2.13 |
| Deep 2.B | One learning step, with numbers | Deep | Error reduced by small adjustments (one-parameter gradient descent) | Mathematics (links to Appendix F) | F2.14 |
| Deep 2.C | Two families of models; precision and recall | Deep | Discriminative vs. generative models; precision and recall beyond the minority-class score (full treatment in Ch. 8) | Fraud, medical screening | — |

Removed from Core (review): Wald's survivorship reasoning → a Check Yourself item and Case Study short case; time drift → Chapter 11; precision/recall → Deep 2.C and Chapter 8; "next-token generation" figure → Chapter 3's Signature 4.

Other anatomy parts:

| Part | Plan |
|---|---|
| Case Study (1 main + 2 short) | **Main:** Amazon recruiting tool (cases/C02) — data → labels → pattern → result, labeled on Signature 3: biased labels + imbalance + proxy shortcut. **Short 1:** 1936 *Literary Digest* poll. **Short 2:** Wald and the missing aircraft (Mangel & Samaniego, 1984) |
| Ethics Lens | Invisible labeling labor [VERIFY source, e.g., Gray & Suri, 2019]; when past decisions should not become future rules |
| Career Connection | Roles along the data pipeline (Lecture 3): data engineer, data steward, annotation specialist, chief data officer; plus data analyst and ML engineer. Descriptive only |
| From the Field | From the author's published "Müşteri Kayıp Analizi" (YBS Ansiklopedi, 2016): customer-churn data is naturally imbalanced — facts limited to the article; disclosure as in D13 if commercial |
| Summary + Key Terms | Answers the session question with Mitchell's definition: performance on a task improves with experience — *and* the model takes the shortest path the data allows |

## 6. Example plan (worked → faded → your turn)

| Skill | Worked | Faded | Your Turn |
|---|---|---|---|
| Rules vs. learned (O1) | Spam filter: three rules and why they fail; the same task as examples + answers | Lucía's ticket routing: reader writes two rules and names their failure | A task from your major: rules or examples? |
| The learning loop (O2) | Sam's classifier, one round: predict "nut", answer "bolt", error, adjust | Reader completes a loop for a house-price model (regression) | Draw the loop for a task in your major |
| Diagnose a data problem (O3) | Fraud model with 99.9% accuracy that catches no fraud (imbalance) | Hospital no-show predictor trained at one clinic (sampling) — reader names symptom and check | **Interleaved mixed set:** five scenarios incl. one with two problems at once (Amazon-like) and one non-example (imbalance handled correctly) |
| Judge reported performance (O4) | "97% accurate" art-style detector: which test set, which classes, minority-class score? | A résumé-screener claim — reader writes three questions | A real claim from the news, or one from the book's dated claim bank (fallback) |
| Concept map (O5) | A 5-term mini-map with labeled links ("is trained on", "produces") and one worked definition | Reader labels 3 links | A2 |

Fields: business, engineering, finance, health, arts, real estate, everyday, study — 8.

## 7. Retrieval and spacing

- Warm-up: three questions (Does AI follow rules someone wrote? Is more data always better? If a model is 99% accurate, is it good?).
- Check Yourself after 2.1–2.7: 2–3 items each, at least one "why"; 2.3 includes a Wald survivorship item.
- **Spaced Review applying Chapter 1 to Chapter 2:** e.g., apply Verify to the "97% accurate" claim; is the 99.9% fraud model "fluent but wrong"?; which Work Loop step would have caught the Amazon problem?; generation vs. retrieval in the light of "the model does not store its examples."
- Spaced forward: proxies → Ch. 11; biased labels → Ch. 16; evaluation → Ch. 8; nested family → Ch. 3.

## 8. Alignment matrix

| Objective | Taught | Practiced | Figures | Assessed | Artifact |
|---|---|---|---|---|---|
| O1 | 2.1, 2.6 | Rules-vs-examples sequence | F2.2, F2.11 | Review A; B1 | A2 terms |
| O2 | 2.2 | Learning-loop sequence; L2.1 | F2.3, F2.4 | Review A; B2 | A2 links |
| O3 | 2.3, 2.4 | Diagnosis sequence; **required paper task**; L2.2, L2.3 | F2.5, F2.6, F2.9 | B3; Case Study Questions; C1 | — |
| O4 | 2.5 | Performance-claim sequence | F2.7, F2.10 | Review A; B4; C2 | — |
| O5 | 2.7 | Concept-map sequence | F2.12 | Application Assignment | **A2** |

Review A distractors are built from M1–M7; counts follow the anatomy (A 10–15, B 3–5, C 2–3, Spaced 3–5, Discussion 4–6, Case Study Questions 4–6); every item carries O · LO · Bloom. Odd answers for the O3 and O4 sequences go to Appendix E.

**A2 (10 points, four levels):** task 3 (15 correct terms from the term pool, ≥7 from Ch. 2 and ≥5 from Ch. 3); process evidence 3 (**labeled links** forming correct propositions, and worked definitions in your own words with one example each); verification 2 (each definition checked against the glossary or a cited source, and **one AI-generated definition corrected — your own, or a provided dated one**); declaration and judgment 2. Two formats offered to everyone: a drawn map, or a structured table of terms and labeled links.

**Term pool.** Chapter 2: rule-based system, machine learning, training data, feature, label, model, supervised learning, error, sample, population, proxy, class imbalance, overfitting, test set, deep learning. Chapter 3: set in the Chapter 3 blueprint (token, context window, training vs. inference, …).

## 9. Figures (titles state the finding; each serves an objective)

| ID | Title | Type | Section | Objective |
|---|---|---|---|---|
| F2.1 | Chapter 2 at a glance (with the AI Work Loop, Verify highlighted) | Chapter map | Opening | all |
| F2.2 | In machine learning, people supply the answers and the machine finds the rule | Two-lane comparison | 2.1 | O1 |
| F2.3 | Learning is many small corrections toward less error | Loop diagram | 2.2 | O2 |
| F2.4 | Every prediction inherits the choices made in collecting and labeling its data | **Signature 3: Data-to-Prediction Pipeline** (master; reused with a highlighted stage in 2.3, 2.4 and the Case Study) | 2.2 | O2, O3 |
| F2.5 | A model learns its sample, not the world | Population vs. sample with three gaps | 2.3 | O3 |
| F2.6 | — (cut in chapter revision v2: duplicated the diagnosis table; the table is kept) | | | |
| F2.7 | A model can score well for the wrong reason | Shortcut schematic (Sam's desk) | 2.5 | O4 |
| F2.8 | — (cut; mechanism shown in Ch. 3 Signature 4) | | | |
| F2.9 | The same share of wrong labels costs 6 points when scattered and 23 when they all point one way | **Computed data chart** (four regimes) | 2.4 | O3 |
| F2.10 | When a model starts memorizing, training accuracy keeps rising but test accuracy levels off (100% vs. about 84%) | **Computed data chart** (decision-tree depth 1–20, digits) | 2.5 | O4 |
| F2.11 | Generative AI is a branch of machine learning, not a different kind of thing | Nested diagram | 2.6 | O1 |
| F2.12 | A concept map is a set of labeled links between terms | Mini-map example | 2.7 | O5 |
| F2.13 | Three waves of AI, and why now | Timeline | Deep 2.A | (Deep) |
| F2.14 | One parameter, one error curve, one step downhill | Computed chart | Deep 2.B | (Deep) |
| F2.15 | Chapter summary card | Summary card | Summary | all |

15 figures. Interactive in Compass (MVP scope, D7): F2.4 (Signature 3). The interactive "try the regimes" version of F2.9 is post-MVP.

## 10. Labs (home or Compass; optional, recommended; tool-neutral)

| Lab | Type | Time | Task | Output |
|---|---|---|---|---|
| L2.1 Train a classifier | Build | 25 min | Train a three-class classifier on photos of three everyday objects with a free no-code tool; test on new photos | Model + observation note |
| L2.2 Break it with data | Break It | 25 min | Retrain: balanced, imbalanced, 20% scattered wrong labels, 20% one-directional wrong labels; then change the background; same test photos; record overall and minority-class results. Note: "Your numbers will differ from the book's; small datasets and different tools vary." | Observation table (Lecture 3) |
| L2.3 Datasheet | Audit | 20 min | Six datasheet questions for your L2.1 dataset, plus "Where did my photos go, and who can see them?" | Datasheet draft |

Accessibility and alternatives: a paper version of L2.1–L2.2 (sorting printed cards by rules vs. by examples, with a provided results table); a screen-reader route using a provided tabular dataset in an accessible spreadsheet; no photos of people; no personal data.

## 11. Risks and checks

- Amazon: verify every detail against Reuters (Dastin, 2018); report Amazon's statement; avoid overstating use in hiring.
- 1936 poll: textbook account plus its correction (Squire, 1988; Lusinchi, 2012).
- Wald: Mangel & Samaniego (1984); no reproduction of the popular aircraft image.
- Invisible labor: needs a solid source.
- Deep 2.A dates: verify each.
- Computed figures: numbers in the text are copied from data/ch02_*.csv only; script, seed and library versions in data/ch02_experiments_meta.txt.
- Characters: Sam (main), Lucía (support-ticket routing — consistent with her job), Hana (art-style detector); log new details in docs/characters.md.

## Proposals that need the author (live syllabus)

1. List Chapter 2 as the reading before Tuesday, January 26.
2. Use Tuesday's opening-case slot for the Amazon case and add 2–3 Chapter 2 items to the concept check.
