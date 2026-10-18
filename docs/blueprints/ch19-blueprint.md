# Chapter 19 blueprint — AI Across Disciplines: Field Guides

Status: **v0.2 (2026-10-18), APPROVED under delegation (D19).** v0.2 applies the independent blueprint review (build/ch19/reviews/blueprint.md: 3 High, 10 Medium, 4 Low) and the editor's decisions 1–9; see "v0.2 changes" below, which **wins over any v0.1 row**, as does the drafted chapter. v0.1 kept at build/ch19/ch19-blueprint-v0.1.md.
Part V — AI in Your Field and Your Future · Syllabus week 13 · Path: **Core** (examinable: Core sections only, D20) · Featured students: **Marcus** (main thread: builds and tests a privacy-safe pharmacology study workflow, the A13 worked model) and **all five in the field guides** (Lucía business, Marcus health, Hana arts and humanities, Elif social science and education, Sam engineering) · Work Loop highlight in the Chapter Map: **Frame** (your field defines the task, what "correct" means, what data may go in and which rules apply), with **Disclose** second (the workflow card and the defense say what the workflow is for and where it fails).

## v0.2 changes (review applied; editor decisions 1–9)

| # | Finding (sev.) | Change in v0.2 and the draft |
|---|---|---|
| R1 | §12.5 table vs. "no, even without names" (High) | One sentence under the verbatim table: the table is the **course floor**; a field rule (placement policy, IRB protocol, consent form, HIPAA's de-identification standard, an employer's policy) can still say no. Review A keyed to it. Elif's input = "personal data about other people", plus the consent form |
| R2 | A-Lab "hallucination" (High) | Tree **"other (automated identifications not confirmed on expert re-analysis: 4 of 40)", documented** by the Author Correction; chain link 2 documented only if the Methods or correction say no manual check before publication, else **inferred**; "novel" off the tree (a Disclose issue). F19.17 = `failure_tree(highlight={"other"})`, retitled. Correction facts exactly: online Jan 19, 2026; 36 of 40 confirmed; 4 inconclusive; Zn₂Cr₃FeO₈ removed (training data); "new to the prediction platform, not necessarily new to science"; 57 targets only as stated in the correction (read on PMC) |
| R3 | Health guide on TPMG (High) | **19.F2 rebuilt on C24, Wong et al. (2021):** Michigan Medicine, Dec 2018–Oct 2019; 27,697 patients, 38,455 hospitalizations; sepsis in 2,552 (7%); AUC 0.63 vs. the developer's 0.76–0.83; 67% of sepsis cases missed; alerts on 18% of patients; one-site external validation by a hospital using the model, of the 2018–19 version; Epic disputed the findings (reported); later versions [VERIFY]. Tree **"other (a prediction model below its reported accuracy at a new site)", documented**; chain link 3 alert burden inferred; no documented harm. TPMG scribes = one line from the editor's abstract notes, "reported by the deploying organization". Reposted-PDF numbers deleted from build/ch19/research-health-education.md |
| R4 | Uncounted Check Yourself and faded examples (Med) | **D24 counting:** whole Core package **with Check Yourself answering** + R16 part + pre-lab + A13 at home incl. brief; Review A, Spaced Review, faded examples beyond the first per section and Case Study Questions labeled **final-exam practice**. One number everywhere (§1 rewritten in the draft) |
| R5 | Identical rows and columns; O1 overstated (Med) | Cells revised against each field's rules; the two columns that are the same in every field (summarizing sources = check point; advising or deciding about people = keep with a person) are printed as one line, not drawn; 19.1 says **the use matters more than the field, except where a field's rules raise the floor**; O1 reworded accordingly |
| R6 | Glyphs, gray, name clash (Med) | Renamed **Discipline × Use Map**, function **`discipline_use_map(highlight=None, note=None, cells=None)`**; symbols drawn as SVG shapes (open circle, half-filled circle, diamond, filled square); white marks on the solid fill; 19.1 says it is not Ch. 15's Risk Heat Map (a people point, not likelihood × impact); "coursework default, as of October 2026"; 42-cell longdesc table |
| R7 | Ithaca metric (Med) | **Top-1 accuracy** 25.3 / 61.8 / 71.7% (the top suggestion fully right) on texts with characters hidden on purpose, answers known; CER named in the case file only; affiliations incl. Harvard's Center for Hellenic Studies [VERIFY full list] |
| R8 | Aeneas (Med) | Claim limited to restoration and region |
| R9 | Rubric levels (Med) | Verification 2 / 1.5 / 1 / 0; test runs scored on the three jobs (typical, different, edge); card 0.5 and defense 0.5 with parallel levels; personal or confidential data = **resubmission condition**, not a score |
| R10 | A11/A13 credit (Med) | D-14.7's sentence printed verbatim; A11-derived parts score only if revised for the build; the defense cites one result and one limit from the card |
| R11 | Alternative works backward (Med) | Forward-built: classify the provided inputs typical/different/edge with reasons, add one input and predict its output, check every provided output, write the build forward; peer route for students absent from the lab |
| R12 | Marcus's fairness check (Med) | Marcus records "no group cue enters" (drug tables describe no people); the paired-input lead moves to a faded example that describes people (Elif's tutoring feedback, cue: a name) |
| R13 | Rule dates (Med) | Every rule dated from its issuing page or [VERIFY] in the handoff refresh rows (research note build/ch19/research-field-rules.md) |
| R14 | Tesla, Tutor CoPilot (Low) | "As of October 2026, NHTSA's record shows RQ24-009 open"; Tutor CoPilot = EdWorkingPaper No. 24-1054, "not peer reviewed as of October 2026", "did not show an effect on end-of-year tests" |
| R15 | From the Field (Low) | "About 85% success" (başarı), not "agree"; "early verification authority" marked as the book's reading; D16 question (funded or commercial project) stays Author-only |
| R16 | Bloom (Low) | O2 "Analyze … to determine"; O3 "Apply … to determine" |
| R17 | Guide map; numbering (Low) | One-line map from UTD schools and majors to the nearest guide ("note one difference"); figures renumbered F19.1–F19.21 in the draft |

Case ids (case-ids.md): **C22** Ithaca (Opening) · **C23** Zillow Offers · **C24** Wong et al. (2021) Epic Sepsis Model validation · **C25** silicon samples · **C26** A-Lab (main Case Study) · **C27** Tesla Autopilot recall · **C28** Tutor CoPilot.

**Revision v2 outcome (2026-10-18; supersedes the draft v1 line).** Four reviews applied (dev memo docs/editorial/ch19-dev-memo.md). Core sections 19.1–19.7 = 3,753 words without markup including the faded examples and the written-out build (3,304 without the faded examples); the blueprint's 3,400 cap is exceeded because the student panel asked for a fully written-out build and a complete sample A13. **Week 13 (D24 amended, standard rates) = 132 min (2 h 12 min); 125 min if the workflow describes no people:** Core package ~52 (reading 6,427 words ≈ 42.8 min + 19 Warm-up and Check Yourself items × 0.5) + R16 abstract and Figure 1 ~4 (Figure 2 now recommended) + pre-lab ~12 + A13 at home ~64 (brief 6, build record 5, checks 12, safeguards 8, fairness runs 7, peer record 4, revision and rerun 8, card ≤ 100 words 6, defense 80–100 words 4, declaration 4). All faded examples, Review A–C, the Spaced Review and the Case Study Questions are final-exam practice. A-Lab chain link 2 is **inferred** (editor decision 1). 22 figures (F19.22 reuses Chapter 18's `regulation_map`; F19.8 kept). Health case = C24 (Wong et al., 2021; v2 note Wong et al., 2026).

**Source material.** Week 13: Tue Apr 20, 2027 "Designing for your own discipline. Demo: an end-to-end example workflow" (R16, Ch. 19); Thu Apr 22 "Discipline sprint: test with three inputs, safeguards, peer test" → **A13 domain workflow prototype**, due Mon Apr 26 (LO6). R16 = Mitchell et al. (2019), *Model cards for model reporting* (arXiv v2 read in full). Seven field cases researched from primary records on 2026-10-18 (build/ch19/research-*.md; health case from the editor's abstract notes, build/sources/nejm-catalyst-ambient-scribes.md). From the Field: the author's 2016 *YBS Ansiklopedi* entry on sentiment analysis ("Duygu Analizi"), read in full via the Google Drive connector (build/ch19/ftf-duygu-analizi.md); unassigned in ftf-sources.md.

**The job left for Chapter 19.** Chapters 12, 14, 15, 16 and 18 built the tools (fit matrix and data gate; blueprint, gates and dry run; data-flow map; paired-input test; regulation map) and promised their use per field in A13; Ch. 17 asked for a Core model-card definition. Chapter 19's job is **application, not new machinery**: the method is the same in every field and four things change; a field decides what counts as correct and who can say so; which data never goes in; which written rules apply, nearest first; a working prototype is tested on three inputs; safeguards and a peer test from outside the field; a card that states what the workflow is for and not for.

**Boundaries.**

| Topic | Owner | Chapter 19 does |
|---|---|---|
| Field guides; Discipline × use heat map; verification authority; field data cautions and rules as design inputs; prototypes; peer test; workflow card; A13 | **Ch. 19** | Owns |
| Independent check, verdict scale (Ch. 8); task–tool fit, data class, data gate, fit matrix, §12.5 table (Ch. 12) | Ch. 8, 12 | Glossary wording; **§12.5 table verbatim** (19.3); `verification_funnel`, `fit_matrix` reused |
| Workflow, approval gate, check point, stop point, hard/soft gate, test inputs, planted fault, dry run, workflow blueprint | Ch. 14 | Glossary wording; no gate theory re-taught; `agent_loop` reused (engineering guide) |
| Prompt template, prompt chain, standing instructions (Deep Ch. 6) | Ch. 6 | **Defined again in 19.5 with glossary wording** |
| Data-flow map, de-identification, data minimization, constructed case, risk owner | Ch. 15 | Wording reused; `data_flow_map` reused (19.3); no defenses re-taught |
| Paired-input test, disaggregated evaluation, lead vs. finding | Ch. 16 | Wording reused (19.6); one small check per prototype |
| Model card (Deep Ch. 17) | Ch. 17 | **Defined in 19.7 with Ch. 17's proposed wording:** "A short document published with a model that states what it is for and not for, how it was evaluated, including results by group where relevant, and its known limits (after Mitchell et al., 2019)." |
| Synthetic media, deepfake (Deep Ch. 13) | Ch. 13 | Defined with Ch. 13 handoff wording where used (19.F3, 19.F7) |
| Copyright, liability, FERPA, HIPAA, TRAIGA | Ch. 18 | `regulation_map` per field; one clause per law; dated "As of October 2026" |

## 1. Outcome link and week 13

| Item | Value |
|---|---|
| Outcomes | **LO6** primary (design an AI-assisted workflow for a task in your field and defend it to a non-specialist; evidence "domain workflow prototype"); LO5 (privacy, fairness, transparency, oversight: O2, O3, O6), LO2 (documented revision: O5), LO3 (verification by the field's standard: O2) secondary |
| Artifact | **A13 — domain workflow prototype**, due Mon Apr 26, 2027, 11:59 p.m.; hosted here (19.8, Application Assignment), 10-point rubric and an alternative |
| In class | Tue: opening case (Ithaca), concept core, demo mirrored by 19.5's worked example, concept check. Thu: Lab 19.1 |
| Readings | Chapter 19. **R16 required in part: the abstract, Figure 1 (summary of the nine card sections) and Figure 2 (example card, smiling-face classifier), ~900 words** [VERIFY Figure 2 count at draft; research counts: abstract ~265, Figure 1 ~230, Figures 2–3 together ~820]. Rest of R16 (~5,450 words body) recommended (Q8) |

### Week 13 workload (out of class; 150 wpm)

| Item | Words or count | Time |
|---|---|---|
| **Core sections** 19.1–19.7 with Check Yourself | ≤ 3,400 | **~23 min** |
| **Whole Core package:** + Opening (~420) + Warm-up (~90) + Studio 19.8 (≤ 350) + **two field guides, yours and one other** (2 × ≤ 430) + main Case Study (≤ 400) + Summary (~300) | ~5,820 | **~39 min** |
| R16 required part | ~900 (technical) | ~7 min |
| Review A (12) + Spaced Review (5) | ~850 + answering | ~13 min |
| Your Turns | absorbed (19.1–19.4 → pre-lab; 19.5–19.6 → lab; 19.7 → A13) | 0 |
| **Pre-lab:** field answers for one task (authority, data class and gate, one rule with source) + three test inputs written out | 1 task, 3 inputs | ~12 min |
| **A13 at home, per requirement (§9):** brief and rubric (~750 words) 5 · finish build record 5 · independent checks on the three lab runs 12 · safeguards table incl. fairness check (2 × 3 runs or a reason) 8 · peer-test record 4 · revision and rerun 8 · card 7 · defense 5 · declaration 4 | — | **~58 min** |
| **Total** | 39 + 7 + 13 + 12 + 58 | **129 min ≈ 2.15 h** (cap 132). All of R16 would add ~30 min (→ ~2.6 h), so the rest is recommended. The time line uses the new note: "about N minutes at a steady pace (150 words a minute); allow more if you read more slowly or are reading in a second language" — Core ~23, package ~39, week ~2 h 10 min — and ends with the Appendix E sentence |

**Word budget.** Core cap **3,400** incl. Check Yourself (Q2): 19.1 520 · 19.2 480 · 19.3 480 · 19.4 440 · 19.5 520 · 19.6 480 · 19.7 480. Worked ≤ 120 words; faded ≤ 70 with the first step filled; Your Turn ≤ 35. Studio 19.8 ≤ 350; seven guides ≤ 430 each incl. a ~130-word case. Estimated total ~13,000 words.

## 2. Chapter objectives (6)

| # | Objective — after this chapter you will be able to… | Bloom | LO | Tags |
|---|---|---|---|---|
| O1 | **Explain** why the same AI use needs different oversight in different fields, using the heat map and the four things that change | Understand | LO6 (LO5) | 4D:DISC · UNESCO:ETH-U |
| O2 | **Identify**, for a task in your field, what counts as correct, who can confirm it, and which data must never go into an AI tool | Analyze | LO6, LO3 (LO5) | 4D:DIL · 4D:DISC |
| O3 | **Locate** the written rules that apply to an AI use in your field, nearest first, and state what each requires | Apply | LO5, LO6 | 4D:DIL · UNESCO:ETH-A |
| O4 | **Build** a working prototype of a domain workflow and test it on three inputs with safeguards built in | Create | LO6, LO2 | 4D:DEL · 4D:DESC · UNESCO:DES-A |
| O5 | **Evaluate** a prototype with a peer test from outside your field, and revise it on the evidence | Evaluate | LO6 (LO2) | 4D:DISC · 4D:DIL |
| O6 | **Write** a workflow card (for, not for, tested on, results, limits) and **defend** the design to a non-specialist | Create | LO6 (LO5) | 4D:DESC · 4D:DIL · UNESCO:DES-A |

## 3. Prerequisites, promises, glossing

**Reused (glossary wording):** jagged technological frontier; independent check, primary source, verdict scale; task–tool fit, data class, data gate, fit matrix; workflow, approval gate, check point, stop point, hard/soft gate, test inputs, planted fault, dry run, workflow blueprint; de-identification, data minimization, constructed case, risk owner; paired-input test, disaggregated evaluation, lead; Ch. 18's three layers.

**Promises kept:** Ch. 6, 7, 9, 11 ("… in your field → Ch. 19": 19.5, F7, 19.2, F1); Ch. 12 `fit_matrix` (F19.11); Ch. 14 A13 and `agent_loop` (19.5, F19.F6); Ch. 15 `data_flow_map` (F19.7); Ch. 16 bias checks (19.6); Ch. 17 model card (19.7); Ch. 18 `regulation_map` (F19.8).

**Glossing at first use:** every new term in §5 plus epigraphy, inscription, protected health information, education record, responsible charge, vehicle recall, over-the-air update, X-ray diffraction, author correction, feeling thermometer, randomized controlled trial, write-down, ambient AI scribe, sentiment analysis, domain dependency.

**Not repeated:** gate theory and compounding (Ch. 14); defenses (Ch. 15); fairness definitions (Ch. 16); legal analysis (Ch. 18); explanation methods (Ch. 17).

## 4. Misconceptions (six; refutation pattern)

| # | Misconception | Where confronted · refutation check |
|---|---|---|
| M1 | "AI skills are the same in every field: a good prompt and a careful check work anywhere." | 19.1, F19.2, From the Field (domain dependency) · must not create "nothing transfers": the Work Loop, gates and three test inputs are shared |
| M2 | "If the output looks right to me, it is right for my field." | 19.2 (verification authority; Ithaca's trained evaluators; A-Lab settled by manual re-analysis and a correction) · must not create "students cannot verify anything" |
| M3 | "If I remove the names, any data from my field is safe to use." | 19.3 (de-identification is a start; health, student, participant and client records carry their own rules) · must not create "never use real data": public data, own work and constructed cases pass |
| M4 | "If there is no AI law for my field, there are no rules for AI in it." | 19.4 (codes, boards, journals, funders, employers, courses; nearest first) · must not create "AI is banned in regulated fields": rules mostly say who checks, who discloses, what data goes in |
| M5 | "If it worked on my test, it works; my own tests are enough." | 19.5–19.6 (three inputs; a peer from outside; Bisbee et al.: same prompt, different results months apart) · must not create "testing is pointless" |
| M6 | "Writing down limits makes the work look weak; a working prototype is finished." | 19.7 (R16: intended and out-of-scope uses come first; A-Lab's one word "novel") · must not create "a card makes a workflow safe": a card informs, gates protect |

## 5. Concept sequence

**Session question, answered in the Summary:** *What changes when you bring AI into your own field, and how do you show that your workflow is ready to use?* Answer (hedged): the method stays — frame, prompt, verify, decide, disclose — but four things change: what counts as correct and who can confirm it, which data your field protects, which written rules apply, and who bears an error. Read your field's guide, place your use on the heat map, build the smallest workflow that does the job, test it on three inputs with safeguards built in, have someone outside your field run it, revise, and write a card saying what it is for, what it was tested on and where it fails. "Ready" means ready for the uses on the card.

**Opening Case (350–420 words): "Seventy-two percent" (Ithaca, 2022; C?? proposed).** Facts and puzzle only. In March 2022, a DeepMind-led team [VERIFY affiliations] described Ithaca, a deep neural network trained on 78,608 ancient Greek **inscriptions** (texts cut in stone) from the Packard Humanities Institute's database, which suggests missing letters, a place of origin and a date (Assael et al., 2022; confirmed, Table 1). On damaged texts, two ancient-history graduate students trained in **epigraphy** restored 25% of the missing characters correctly alone; Ithaca alone 62%; the two using Ithaca's top-20 suggestions 72%. Places: 71% of 84 regions; dates within about 30 years on average (median 3). The authors call it an assistive tool. Say "two expert evaluators". **Puzzle:** *If the model alone beat the experts so widely, why did the authors keep historians in charge — and why did the pair beat both?* Answered in 19.2, 19.6 and the Summary.

**One job per appearance.** Ithaca: Opening · 19.2 (experts chose among ranked suggestions; the field decides what a restoration is worth) · Summary. A-Lab: one clause in 19.2 and 19.7 · Case Study · CSQ. Bisbee et al.: one clause in 19.6 · social-science guide. Every other case: its guide only.

| # | Subsection (cap) | Tag | One core idea | Examples (worked ≤ 120 · faded ≤ 70) | Figures |
|---|---|---|---|---|---|
| 19.1 | One method, different fields (520) | Core | **The Work Loop is the same everywhere; four things change: what counts as correct (and who says so), protected data, written rules, who bears an error.** A **field guide** answers these plus typical uses and a career note (19.F1–F7). **Discipline × use heat map** (new signature): 7 fields × 6 uses (drafting and editing text; summarizing and searching sources; analyzing data; code or calculations; images, audio, video; advising or deciding about people); each cell shows the **default people point** for a student's work on Ch. 14's scale *log review · check point · approval gate · keep with a person*, by F14.7's rule (can it be undone × who bears an error). Always labeled **this book's reading, a default your field's rules and your instructor override**. One sentence: the heat map is about oversight, not tool quality (frontier, Ch. 12 wording). M1 | **Worked:** Marcus's row: textbook study summary = check point; dose calculation = approval gate (he recomputes by formula and uses the course key); anything about a real patient = keep with a person (he never enters patient information). **Faded (business):** Lucía's row; "draft a customer reply in the company's approved tool = check point" filled; reader places "analyze the association's budget data" and "choose scholarship recipients". **Your Turn → pre-lab:** your cell, one reason | F19.2, F19.3, F19.4 |
| 19.2 | What counts as correct, and who can say so (480) | Core | **Each field has its own evidence for "correct", and some checks need a qualified person.** **Verification authority** (new term): the source or person a field accepts as able to confirm a result — a primary record, a standard, a replication, a licensed professional, a trained specialist. Independent check and primary source recalled (Ch. 8 wording); verdict scale used. Ithaca's second job; A-Lab in one clause. Name the authority before you build; plan which checks you can do yourself. M2 | **Worked:** Hana's zine caption: an AI summary of a 1920s newspaper page gives a date; authority = the page and the archive's catalog record; verdict *contradicted*; corrected and the archive noted. **Faded (engineering):** Sam's datasheet summary gives a motor's rated speed; authority filled (the manufacturer's dated datasheet); reader names the check and verdict. **Your Turn → pre-lab** | F19.5, F19.6 |
| 19.3 | The data your field protects (480) | Core | **Your field decides which data never goes in, and the data gate comes before any test.** Data class and gate recalled; **§12.5 table reproduced verbatim with its note**. Field records, one gloss each: health information (HIPAA), education records (FERPA), research-participant data under **informed consent** and an **IRB** protocol [VERIFY UTD IRB guidance on AI tools], client files, unpublished results and code. Ch. 15: de-identification is a start; data minimization and the constructed case are the habits. M3 | **Worked:** Marcus's inputs: textbook drug tables and his own notes, university-provided tool → pass; anything from placement → no, even without names. **Faded (social science):** Elif's research-methods survey answers; class filled (participant data; consent form keeps responses with the course team); reader decides the gate and the input change that passes it. **Your Turn → pre-lab** | F19.7 |
| 19.4 | The rules your field writes down (440) | Core | **Find the written rules that apply, nearest first, and record what each requires.** Ch. 18's layers via `regulation_map`. Nearest first: syllabus and instructor (cite §10.2), program, placement or employer, professional code and licensing board (**licensure**, **scope of practice**), journals and funders, law. Dated examples [VERIFY each on the issuing body's page]: NIH NOT-OD-23-149 (2023) bars peer reviewers from generative AI; ICMJE: AI tools cannot be authors, use disclosed; Texas TRAIGA's health-care disclosure (Ch. 18). Most rules say **who checks, who discloses and what data may go in**. M4 | **Worked:** Marcus's list: syllabus (declare AI use; drug calculations by hand on exams); placement policy (no patient information in outside tools; constructed program policy, labeled); HIPAA (pointer); professional code's privacy duty [VERIFY ANA wording]. **Faded (education):** Elif's tutoring center; first rule filled (tutors do not give graded answers; constructed); reader adds FERPA and the syllabus. **Your Turn → pre-lab** | F19.8 |
| 19.5 | From blueprint to working prototype (520) | Core | **A prototype is the smallest working version of a workflow, built so it can be run, checked and changed.** **Prototype** (new term). Builds (tool-neutral): a **prompt template** (glossary wording), a **prompt chain** (glossary wording), a tool with **standing instructions** (glossary wording) and chosen files, a spreadsheet AI feature, or an automated workflow in a sandbox. The build answers the guide: inputs pass the gate; each output has a named check; at least one people point; side effects off. **Test inputs** (typical, different, edge) taken from the field's own hard cases. `fit_matrix` per part; "no AI" stays a valid cell. A13 may extend A11: the step map is reused **without credit**; build, runs and peer test are new. M5 | **Worked (mirrors the demo):** Marcus's three-step chain in the university-provided tool: (1) 10 practice questions from a pasted drug table; (2) he answers closed-book (Ch. 7); (3) the tool marks his answers against the table and he checks every mark (check point). Inputs: one drug class; a table with US and metric units; two look-alike drug names. Edge run swaps the names; caught at the check point (constructed). **Faded (natural science):** a chemistry major's lab-report checker; step 1 filled; reader writes the three inputs. **Your Turn → Lab 19.1** | F19.10, F19.11 |
| 19.6 | Safeguards and the peer test (480) | Core | **Someone who did not build the workflow, from outside your field, finds what your own tests miss.** **Peer test** (new term): a person from another field runs your prototype on an input of their choosing within its stated scope, with only your instructions, and records where it confused them or failed. Four safeguards: gate passed; one people point, hard where an error falls on others; one field rule applied; one **fairness check** when people are described — a small paired-input test (Ch. 16 wording; at this size a lead, not a finding), naming the cue changed, or one line on why no group cue enters. Bisbee et al. in one clause (same prompt, significantly different results three months apart) → the card records model and date. M5 | **Worked:** Hana peer-tests Marcus's workflow and cannot tell why answers were marked wrong (abbreviations); he adds a plain "why" line. Fairness: one constructed vignette run with two patient names (the cue: the name), 3 runs each, same key; recorded as a lead (constructed). **Faded (business):** Sam peer-tests Lucía's reconciliation-practice workflow; his first finding filled; reader writes her revision. **Your Turn → Lab 19.1** | F19.12, F19.13 |
| 19.7 | Say what it is for: the workflow card (480) | Core | **A workflow is ready only for the uses its card states.** **Model card** defined (Ch. 17 wording, R16); R16's nine sections named once (model details, intended use, factors, metrics, evaluation data, training data, quantitative analyses, ethical considerations, caveats and recommendations); its point in one sentence: report results by group and condition, not one overall number. **Workflow card** (new term): five fields — *for* · *not for* · *tested on* (inputs, peer test, tool kind, model if shown, date) · *results* (per input, with the check) · *limits and safeguards*. "If you read all of R16…" for more. A-Lab in one clause: one word, "novel", carried the claim. M6 | **Worked:** Marcus's card (≤ 120 words): for his own exam review from textbook tables; not for patient care, real doses or anyone's grades; tested on three tables and Hana's peer test, date; results 10/10, 10/10, 9/10 with one caught swap; limits: one tool and model, no combination drugs; check point at every mark. **Faded (engineering):** Sam's card; *for* and *not for* filled; reader writes *tested on* and *limits*. **Your Turn → A13** | F19.14, F19.15 |
| 19.8 | Discipline sprint (Lab 19.1, A13) (350) | Studio | A13 as one record, in §9's order; full-mark results as in §9 | Marcus's A13 page (worked); a partly filled sheet **printed in the chapter** (faded) | F19.16 |
| 19.F1–F7 | Field guides (430 each) | Studio (reference) | Five-part frame plus a fairness question, a featured student and one short case (§5b). Read yours and one other; not examinable as content (Q3) | §5b | F19.F6 |
| Deep 19.A | Who uses AI in which fields (as of 2026) | Deep | Usage by field, dated (e.g., Anthropic's 2025 education report [VERIFY]); one company's data is not a sample; adoption is not fit | — | F19.21 |
| Deep 19.B | Model cards in practice | Deep | What published cards omit (Liang et al., 2024 [VERIFY]); the rest of R16 | — | — |

### 5b. Field guides and cases (seven cases, "C?? proposed"; C22–C28 are reserved for them in case-ids.md; the editor assigns)

Defaults below are the heat-map rows (data/ch19_heatmap.csv), order: drafting · sources · data · code · media · people. L = log review, C = check point, G = approval gate, P = keep with a person.

| Guide · student | Row | Verify / authority · data cautions · rules (nearest first; each [VERIFY] at draft) | Short case (≤ 130 words; tiers; labels) |
|---|---|---|---|
| **19.F1 Business** · Lucía | C · C · G · C · C · P | Ledgers, source documents, audit trail, a forecast's stated conditions, a CPA for opinions · client and customer data, employer confidential data · employer policy; AICPA confidentiality rule; FTC actions on deceptive AI claims (2024); TRAIGA pointer | **Zillow Offers (2021).** From Feb 2021, Zillow said, its Zestimate — which it described as using AI, including a deep-learning network — became the *initial* cash offer for a limited subset of homes in 20+ markets (Zillow, 2021a; confirmed). On Nov 2, 2021 it announced a wind-down: it had been unable to forecast home prices accurately, missing in both directions; it wrote down about $304 million of inventory in Q3, expected $240–265 million more in Q4 losses and would cut about 25% of staff (Zillow, 2021b, 2021c; confirmed). Zillow did not blame an algorithm; that framing is the press's (**inferred**). AP's "$340 million" conflicts with the filing; use $304M. **Verify:** the conditions a forecast was built on. Labels: tree "other: a forecast used outside its conditions", inferred; chain link 2 inferred, link 4 loss documented |
| **19.F2 Health** · Marcus | G · C · G · G · G · P | Guidelines, drug references, the patient record, the licensed clinician · protected health information (HIPAA), placement rules, even de-identified cases · course and placement policy; approved-tools list; HIPAA; TRAIGA health-care disclosure (Jan 1, 2026); Texas SB 1188 (2025) | **Ambient AI scribes at The Permanente Medical Group (2023–2025).** Facts only from the two abstracts the editor read; **reported by the deploying organization** (commentaries by its own staff, not independent trials — said in the text). In October 2023 the group enabled an **ambient AI scribe** (transcribes a visit through a smartphone microphone and drafts the note; audio not kept) for 10,000 physicians and staff; in 10 weeks 3,442 physicians used it in up to 303,266 encounters; notes are drafts for physicians' editing; the authors caution about accuracy (Tierney et al., 2024). After a year: over 2.5 million uses, more than 15,700 hours of documentation time estimated saved, and a call for analysis across clinical scenarios and patient groups (Tierney et al., 2025). The abstract's "1,794 working days" is not used (it does not match 15,700 ÷ 8). **Verify:** who evaluated the tool; the signing clinician checks each note. Labels: tree none documented; chain link 2 = physician editing of every draft (design, reported). Alternate (independent study): Wong et al. (2021) sepsis-model validation (AUC 0.63 vs. the developer's 0.76–0.83; confirmed) |
| **19.F3 Arts and humanities** · Hana | C · C · C · L · G · P | Primary source, archive record, editions, process evidence, a trained specialist · unpublished manuscripts, archive permissions, other artists' work, client files · course policy; archive terms; client contract (Ch. 18); MLA/Chicago AI citation guidance; copyright (Ch. 18). **Synthetic media** and **deepfake** defined with Ch. 13 wording | The Opening Case is this guide's case; one sentence on its sequel **Aeneas** (2025, Latin inscriptions; historians with the tool outperformed humans and the model alone; Assael et al., 2025, abstract; confirmed). **Verify:** the specialist chooses among ranked suggestions. Labels: none on the tree (positive result) |
| **19.F4 Social science** · Elif | C · C · G · C · C · P | Data, codebook, replication, preregistration, IRB protocol, methods advisor · participant data under consent; small groups that re-identify · course and lab rules; IRB and the Common Rule (45 CFR 46); APA journal AI policy; AAPOR guidance | **Silicon samples (2023–2024).** Argyle et al. (2023) reported that GPT-3, given respondents' backstories from the American National Election Studies (ANES), reproduced subgroup patterns closely enough to call it "algorithmic fidelity" (confirmed). Bisbee et al. (2024) gave ChatGPT 3.5 Turbo personas of 2016 and 2020 ANES respondents and asked for 0–100 **feeling-thermometer** ratings of 11 groups: averages were close, spreads far smaller; 48% of regression coefficients differed significantly from the survey's, a third of those with the opposite sign; small wording changes shifted results; identical prompts in April, June and July 2023 gave significantly different results (confirmed). **Verify:** variation and reproducibility, not only averages. Labels: tree bias (a skew across matched outputs: too little variation), documented; the authors' word "overconfidence" quoted as theirs, not a tree label |
| **19.F5 Natural science** · unnamed chemistry major | C · C · G · C · P · P | Replication, raw data, instrument records, peer review, lab supervisor · unpublished results, notebooks, collaborators' data · lab rules; journal AI-text and AI-image policies (Science, Nature families); funder data rules | Points to the main Case Study (A-Lab); no second case (one job per appearance) |
| **19.F6 Engineering** · Sam | C · C · G · C · C · P | Standards, datasheets, tests and measurement, a licensed engineer in **responsible charge** · employer and client designs, export-controlled technical data, source code (Ch. 15) · course and club rules; employer policy; Texas engineering board sealing rule; NSPE Code; product-safety regulators | **Tesla Autopilot recall (2023–2024).** On Dec 12, 2023, Tesla filed a recall of 2,031,220 vehicles because Autosteer's controls "may not be sufficient to prevent driver misuse"; the remedy was a free **over-the-air** update; Tesla recalled while not agreeing with the agency's analysis (Tesla, 2023; confirmed). NHTSA's closing report (Apr 25, 2024) analyzed 467 crashes, 13 with fatalities (14 deaths), and described a critical safety gap between drivers' expectations and the system's capabilities; the same day it opened a query on whether the remedy was adequate (NHTSA, 2024a, 2024b; confirmed). The query's status as of October 2026 [VERIFY]; never called closed. **Verify:** that the human's role in an automated system is designed and tested. Labels: tree not applicable (a control-design weakness, no wrong output); chain link 2 controls insufficient (documented, recall), link 3 overreliance (documented, NHTSA). F19.F6 shows Sam's datasheet step on `agent_loop` |
| **19.F7 Education** · Elif (peer tutor) | C · C · G · L · C · P | Curriculum standard, answer key, the teacher, learning evidence (Ch. 7) · education records (FERPA), minors' data, student work · center and course rules; school policy; FERPA; COPPA; U.S. Dept. of Education guidance (2023) | **Tutor CoPilot (2024–2025).** A preregistered **randomized controlled trial** of chat tutoring in grades 3–6 in one Southern U.S. district (Mar 27–May 17, 2024): tutors were randomized; the tool showed the tutor three GPT-4 suggested replies to edit or ignore, and students never saw it. Students of tutors with the tool were 4 percentage points more likely to master the topic on an exit ticket (62% → 66%); with lower-rated tutors, 9 points (56% → 65%); no significant effect on end-of-year tests; about $20 per tutor per year; the authors note suggestions that missed the grade level and disclose an author's part-time work with the provider (Wang et al., 2025, working paper; confirmed; latest version's sample: ~900 tutors randomized, 783 tutoring, 1,013 students). **Verify:** learning, not only answers, and who saw the AI's words. Labels: none on the tree; chain: the tutor is the gate (design, documented). Peer-review status [VERIFY] |

Each guide ends with one descriptive career note (no salary or market claims). Elif appears in two guides in her established roles; the natural-science guide uses an unnamed one-off because no recurring student majors in a natural science (Q6).

### 5c. Main Case Study: "Novel, then corrected" (A-Lab, 2023–2026; C?? proposed)

| Tier | Statement | Source |
|---|---|---|
| Confirmed | *Nature* (online Nov 29, 2023): an autonomous lab in which robots made inorganic powders from recipes proposed by models trained on the literature, with results read by automated analysis of **X-ray diffraction** patterns; over 17 days it "realized 41 novel compounds from a set of 58 targets" (original abstract) | Szymanski et al. (2023) |
| Confirmed | A peer-reviewed critique (*PRX Energy*, Mar 7, 2024; preprint Jan 8) argued that automated analysis of the patterns was not yet reliable and that many predicted ordered compounds were known disordered forms; it concluded no new materials had been discovered in that work | Leeman et al. (2024) [VERIFY full text; its abstract counts 43] |
| Reported | A critic said the paper should be retracted; the lead author said the critique had errors and the team would respond in the peer-reviewed literature | The Register (2024, Jan 31); Chemistry World (2024, Jan 16) [VERIFY bylines] |
| Confirmed | Author Correction (online Jan 19, 2026): title now "…synthesis of inorganic materials"; one target removed because it was in the training data (58 → 57); manual re-analysis confirmed 36 of 40 reported successes, 4 excluded as inconclusive; "novel" had meant new to the prediction platform, not necessarily to science; unnamed correspondents thanked | Szymanski et al. (2026) |
| Inferred | The field's own verification authority — expert re-analysis, peer-reviewed critique, a journal correction — settled what the automated analysis could not; the word "novel" carried the claim | "This book reads…" |

**Plan (≤ 400 words, counted).** Four-line timeline (F19.17); **corrected, not retracted**. **Labels:** tree **hallucination** (output not supported by the evidence: 4 of 40 identifications unconfirmed), **documented** by the correction; the "novel" wording is a verification and disclosure issue, not a branch; chain link 2 "checked before use?" — results reported before expert re-analysis of every pattern, documented by the correction's own re-analysis; link 4 none beyond a corrected record. Fallback "other: contested analysis" if reviewers judge the label too strong (Q11).

**Other anatomy parts.**

| Part | Plan |
|---|---|
| Ethics Lens | **Who carries the risk when AI enters a field?** Patients, students, participants, clients and drivers often did not choose the tool; responsibility stays with the named or licensed person (Ch. 18); benefits are uneven across languages (From the Field, marked as the entry's 2016 claim) |
| Career Connection | One occupation per guide (auditor, clinical informatics, archivist, survey researcher, research technician, test engineer, instructional designer), each with "a question an employer may ask about your A13"; descriptive only; bridge to Ch. 20 |
| From the Field | Şeker, Ş. E. (2016). Duygu analizi (Sentimental analysis). *YBS Ansiklopedi, 3*(3), 22–36 (Drive 1L9GhfySDnmUNN4BdK1BMzkexUSQ02IzR; pages from the running heads; Cilt 3 Sayı 3, Eylül 2016). **Facts limited to the entry:** sentiment analysis classifies the feeling a text expresses, first as positive, negative or neutral; hard problems include sarcasm and implicit sentiment, negation, several entities in one sentence, and **domain dependency** — the same words mean different things in different domains (its example: a film whose plot moves unpredictably is praised; a car that moves unpredictably is faulted); method choice depends on the application (fast statistical methods for streaming social-media data); success rates were lower for Turkish than for English in the studies it cites; citing a 2013 newspaper piece, it reports that people agree on sentiment about 85% of the time and that 70% then counted as success for software. **Present-day connections, marked:** domain dependency is why field guides exist (the book's own examples, labeled: "a positive test result" in medicine); people's agreement rate works as an early verification authority. The entry mentions an unnamed project: no D16 unless the author says it was commercial (Author-only 2). A third-party table it reprints is not reproduced |
| Summary + Key Terms | Session answer; card F19.20; Warm-up revisit; return to Ithaca. **New Core terms:** Discipline × use heat map · field guide · verification authority · prototype · peer test · workflow card · model card · informed consent · institutional review board (IRB) · licensure · scope of practice. **Reused verbatim:** see §3, plus prompt template, prompt chain, standing instructions, synthetic media, deepfake |

## 6. Example plan (worked → faded → your turn)

| Skill | Worked | Faded (first step filled) | Your Turn |
|---|---|---|---|
| Reading a heat-map row (O1) | Marcus | Lucía | Pre-lab |
| Verification authority (O2) | Hana's caption date | Sam's rated speed | Pre-lab |
| Data cautions and gate (O2) | Marcus's inputs | Elif's survey answers | Pre-lab |
| Field rules, nearest first (O3) | Marcus's list | Elif's tutoring center | Pre-lab |
| Build and three inputs (O4) | Marcus's chain | Chemistry lab-report checker | Lab 19.1 |
| Safeguards and peer test (O5) | Hana tests Marcus; fairness lead | Sam tests Lucía | Lab 19.1 |
| Workflow card (O6) | Marcus's card | Sam's card | A13 |

All worked and faded examples printed; each faded example supplies the facts its next step needs. AI outputs labeled "constructed example" unless a model and date are given; tools by kind.

**New character details to log** (handoff), all constructed and consistent with characters.md and the Ch. 12–16 logs: **Marcus** — pharmacology review chain from textbook drug tables in the university-provided tool, every mark checked by him; look-alike-name edge input; two-name fairness lead; card excludes patient care and real doses. **Hana** — checks an AI summary's date against the archive record (zine history issue); peer-tests Marcus. **Elif** — survey answers kept with the course team under the consent form; tutoring-center rule against giving graded answers. **Sam** — datasheet rated-speed check; card for his datasheet step (new build extending A11); peer-tests Lucía. **Lucía** — heat-map row; reconciliation-practice workflow for coursework.

## 7. Retrieval and spacing

- **Warm-up** (third with confidence 0–100%): (1) Would you check an AI summary the same way in nursing and in history? Why? (2) You remove all names from survey answers. May they go into any AI tool? (3) Your workflow worked on your own test. Is it ready for others?
- **Check Yourself** after 19.1–19.8, two items each, at least one "why", answerable from Core; model answers in Appendix E.
- **Spaced Review** (5): Ch. 15 ×2 (Marcus's input on the data-flow map; who owns a residual risk), Ch. 16 (why one output is a lead), Ch. 18 (which rule layer you meet first), Ch. 14 (hard vs. soft gate in a prototype). Checked against the written chapters at draft time.
- **Spaced forward:** A13 → Ch. 20; heat-map row as personal rules → Ch. 21 (`discipline_heatmap` reused); field news → Ch. 22.

## 8. Alignment matrix and package

| Obj. | Taught | Practiced | Figures | Assessed | Artifact |
|---|---|---|---|---|---|
| O1 | 19.1 | Heat-map sequence; guides | F19.2–4 | A; B1 | A13 cell |
| O2 | 19.2, 19.3 | Authority, data sequences | F19.5–7 | A; B2; CSQ | Field answers, gate |
| O3 | 19.4 | Rules sequence | F19.8 | A; B3 | Rule row |
| O4 | 19.5, 19.8 | Build sequence; Lab 19.1 | F19.10–11, F19.16 | A; B4 | **Build and runs** |
| O5 | 19.6 | Peer-test sequence; lab | F19.12–13 | A; C1 | Peer test, revision |
| O6 | 19.7 | Card sequence | F19.14–15 | A; C2; CSQ | Card, defense |

**Review A 12** (keys rotated (a)–(d); correct option longest in at most two; distractors from M1–M6, no absolute giveaways): four things that change; reading a cell; verification authority; §12.5 row for de-identified data; de-identification vs. field rules; nearest rule first; A11/A13 credit; three test inputs; purpose of a peer test; a paired-input lead; model card definition; the *not for* field. **B 4:** B1 a city-planning intern summarizes public comments on a zoning change (place the use; authority; comments may name people); B2 an agriculture student's pest-photo workflow (three inputs; the extension specialist as authority); B3 a music-education major's practice feedback for middle-school students (FERPA, minors, rules, gate); B4 a journalism student's interview transcription (consent, checking against the recording, what the card excludes). **C 2:** C1 "AI literacy is the same in every field, so field guides are unnecessary" (O1, O5); C2 "If a licensed professional reviews every output, the field's risks are handled" (O3, O6; approval fatigue, Ch. 14). **Spaced 5. Discussion 5** (ethics: who bears errors without choosing the tool; career: a cited posting or professional-body page on AI in your field; interdisciplinary: two fields' verification authorities, cited; language: does your field's tool work as well in another language you know; one cell you would change). **Case Study Questions 5** (place A-Lab facts in tiers; label tree and chain; what "novel" claimed and what the correction changed; who had the authority to settle it; write *not for* and *limits* lines for the automated analysis step). **Mini-Project (optional):** three-week "field watch", one dated rule, case or posting per week placed on your row; feeds Ch. 20–21. Items tagged O · LO · Bloom; Appendix E gets odd answers plus all Check Yourself and faded-example answers; even → private/.

## 9. Application Assignment — A13 Domain Workflow Prototype

**Due:** Mon Apr 26, 2027, 11:59 p.m., eLearning. *(O4–O6 · LO6; LO5, LO2 · Create)* About 12 minutes before Thursday's lab and about 60 after. **A13 may extend your A11 blueprint; reused parts are marked "from A11" and earn no points. A13 is graded only on what is new — the build, the runs and the peer test — with the checks, safeguards, card and defense that belong to them.** Use a university-provided tool such as Microsoft Copilot Chat (as of October 2026) or a free tier whose terms pass your data gate; side effects off or simulated; no personal, confidential, patient, student or client data.

**Submit:**
1. **Task and field answers (≤ 150 words):** a recurring task from your major or intended career; goal and done-criteria; verification authority; data class and gate (§12.5); one written rule, its source and what it requires; your heat-map cell and whether you agree.
2. **The build**, written out so someone else could run it (template, chain, configured tool with standing instructions and files, or other); tool kind, model if shown, date; reused parts marked.
3. **Three runs** (typical, different, edge; lab runs count): output, the independent check against your field's authority, verdict.
4. **Safeguards table:** data gate; at least one people point (type, hard or soft, role); the rule applied; one fairness check (paired-input, 2 × 3 runs, cue named, recorded as a lead) or one sentence on why no group cue enters.
5. **Peer test:** a classmate from another field ran it on an input of their choosing within scope; what they did; what confused them or failed.
6. **Revision:** one change from a run or the peer test, and a rerun of the failed input.
7. **Workflow card (≤ 150 words):** for · not for · tested on · results · limits and safeguards.
8. **Defense for a non-specialist (100–120 words):** why it fits its stated use and where a person stays.
9. **AI Use Declaration:** tools, purpose, accepted/rejected/revised, how verified, where your judgment shaped the work.

Full-mark results include "a fixed template is enough", "this step stays with a person", "the edge input failed and the card now excludes it". Tool steps in Compass only.

**Rubric (10 points;** course split task 3, process 3, verification 2, declaration and judgment 2; process scored as two criteria).

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| **Build and field design (3)** | 3: a rerunnable build with tool kind and date; field answers complete (authority, class and gate, one cited rule, cell); safeguards complete (gate, people point with role, rule, fairness check or reason); no personal or confidential data | 2: one field answer or safeguard missing or uncited, or one detail needed to rerun missing | 1: build not rerunnable from the record, or two answers or safeguards missing | 0: no working build, or personal or confidential data used |
| **Test runs (1.5)** | 1.5: three runs recorded with output and date | 1: two | 0.5: one | 0: none |
| **Peer test (1.5)** | 1.5: peer from another field, own input within scope; what they did and what failed recorded; linked to a revision | 1: recorded but not linked to a change, or a same-field peer | 0.5: a comment without a run | 0: none |
| **Verification and revision (2)** | 2: every run has a named independent check and verdict; one revision with rerun | 1.5: one run unchecked, or rerun missing | 1: checks mostly missing, or no revision | 0.5: revision without checks; 0: neither |
| **Card and defense (1)** | 1: five fields, specific *not for*; 100–120-word defense a non-specialist follows | 0.75: one thin field or one unexplained term | 0.5: two fields missing, or defense unclear or over length | 0: neither |
| **Declaration (1)** | 1: five elements | 0.75: four | 0.5: two or three | 0: zero or one |

**Alternative assignment** (no AI tool wanted, no passable data gate, or unshareable data): one of **seven provided field scenarios** (one per guide) with provided inputs and **provided dated outputs** (model and date, two per input). The student writes the build that would produce them, checks each output against the field's authority, designs the safeguards, has a peer from another field work through the scenario and record confusions, revises the build and writes the card. Same rubric: "Build" = the written build and field answers; "Test runs" = the provided outputs recorded per input; the rest unchanged.

## 10. Figures (titles state findings; ≤ 9 boxes for diagrams; dashes mean only inferred or reported)

| ID | Title | Type | § | Obj. |
|---|---|---|---|---|
| F19.1 | Chapter 19 at a glance | `work_loop(highlight=["Frame", "Disclose"])` (ch01) | Map | all |
| F19.2 | In this book's reading, the same use needs more oversight where an error falls on other people | **New signature `discipline_heatmap(highlight=None, note=None, cells=None)`** in ch19_figures.py from data/ch19_heatmap.csv (field, use, level 1–4, reason, guide). Chart, 7 × 6 cells; each cell a **symbol and a word** (○ log · ◔ check · ◑ gate · ● person) plus a gray-safe fill (none, dots, hatch, solid); `highlight` = field, use, `(field, use)` or a list (thick border); `cells` overrides a row (Ch. 20–21); source line "This book's reading of the field guides; a default, not data" | 19.1 | O1 |
| F19.3 | Every field guide answers the same five questions | Concept, 6 boxes | 19.1 | O1 |
| F19.4 | Marcus's row runs from a check point for study notes to "keep with a person" for patients | `discipline_heatmap(highlight="health")` | 19.1 | O1 |
| F19.5 | In your field, someone has the authority to say "correct" | `verification_funnel(highlight="expert", notes=…)` (ch08) | 19.2 | O2 |
| F19.6 | The experts with Ithaca's suggestions restored more text than the model or the experts alone | Data chart, data/ch19_ithaca.csv (25.3 / 61.8 / 71.7; Assael et al., 2022, Table 1) | Opening, 19.2 | O2 |
| F19.7 | Marcus's input stays on his side: textbook tables in, placement data never | `data_flow_map(highlight="input", annotate=…, note=…)` (ch15) | 19.3 | O2 |
| F19.8 | The rules nearest you come first: course, program, placement, then law | `regulation_map(highlight=["org", "us_existing"], notes=…, note="As of October 2026")` (ch18) | 19.4 | O3 |
| F19.10 | A13 reuses A11's design and adds a build, runs and a peer test | Two lanes, ≤ 8 boxes, "reused, no credit" vs. "new, graded" labels | 19.5 | O4 |
| F19.11 | Each part of Marcus's workflow gets its own fit decision; the consumer tool is blocked for placement material | `fit_matrix(…)` (ch12): 3 parts × university tool / consumer tool / no AI | 19.5 | O4 |
| F19.12 | Four safeguards travel with every prototype | Concept, ≤ 6 boxes | 19.6 | O5 |
| F19.13 | A peer from another field finds what the builder's tests miss | Process, ≤ 6 boxes; the finding has a risk border and the label "confused here" (no dash) | 19.6 | O5 |
| F19.14 | A workflow card keeps the model card's core: what it is for, what it was tested on, where it fails | Mapping, ≤ 9 boxes: R16's nine sections → five card fields | 19.7 | O6 |
| F19.15 | Marcus's card says "not for patient care" before it says what works | Card figure | 19.7 | O6 |
| F19.16 | Your A13 records field answers, build, runs, peer test and card | A13 sheet | 19.8 | O4–O6 |
| F19.17 | "Novel" was claimed, challenged and corrected through the field's own channels | Storyboard, ≤ 6 boxes; solid = primary record, dashed = reported (legend says so) | Case | O2, O6 |
| F19.18 | The A-Lab case on the tree: unconfirmed identifications, documented by the correction | `failure_tree(highlight={"hallucination"}, tag=…)` (ch04) | Case | O2 |
| F19.19 | Results were reported before experts re-checked every pattern | `failure_chain(highlight=[1], notes=…)` (ch04) | Case | O2 |
| F19.20 | Chapter summary card | Summary card | Summary | all |
| F19.21 | (Deep) Students' AI conversations are not spread evenly across fields | Data chart, data/ch19_use_by_field.csv [VERIFY source] | Deep 19.A | — |
| F19.F6 | Sam's datasheet step on the agent loop: read-only tool, a check point before the cart | `agent_loop(highlight=["tool", "check"], annotate=…)` (ch14) | 19.F6 | O4 |

20 figures; Compass: heat map with a "my row" editor.

## 11. Labs (tool-neutral)

**Lab 19.1 Discipline sprint** — Thu Apr 22, 75 min, mixed-field teams of 3–4, individual records; university-provided tool or the provided outputs (no-device route).

| Minutes | Step |
|---|---|
| Before (~12) | Pre-lab: field answers, three inputs |
| 0–10 | Briefing: F19.3, F19.2, F19.12; peer-test rules (within scope, no personal data, record, do not fix) |
| 10–35 | Build and run three inputs; record output, tool kind, model if shown, date |
| 35–55 | Peer test in cross-field pairs; the builder watches and records |
| 55–70 | Share: place cells on a class heat-map poster; discuss one cell where fields disagreed |
| 70–75 | Exit: one change, and what the card will exclude |

**Optional:** L19.2 Read a real model card (20 min; two providers' cards; which of R16's nine sections each fills). L19.3 Cross-field swap (20 min; a classmate's prototype on an input from your field, outside its scope). Accessibility: provided outputs, screen-reader-friendly templates, any input language with English glosses.

## 12. Risks and checks

- **The heat map is a judgment, not data:** labeled so everywhere; a reason per cell in the CSV; levels follow F14.7's rule; students may disagree.
- **Exact attribution:** as stated in each case row (§5b–5c).
- **Workload** ~2.15 h by count; never a lower number; five guides optional.
- **Field rules** dated "as of October 2026", each [VERIFY] on the issuing body's page, all to the refresh list; Ch. 18 owns legal analysis.
- **No patient, student or client data** anywhere; Deep-chapter terms defined in Core where used.
- **Signatures:** all reused functions exist except `regulation_map` (ch18, import when written); `discipline_heatmap` written once.

## Decisions taken under delegation (D19)

| # | Decision | Reason |
|---|---|---|
| Q1 | Highlight **Frame**, Disclose second | Field defines the task; the card discloses scope |
| Q2 | Seven Core sections; **Core cap 3,400** incl. Check Yourself | Week budget with a prototype at home |
| Q3 | **Field guides = Studio reference**; read yours and one other; not examinable as content | Fair to every major (D20); honest workload |
| Q4 | **`discipline_heatmap`** = default people point (Ch. 14 scale) per field × use; book's reading; symbol + word + pattern | Book map; reuses F14.7's rule; never color alone |
| Q5 | Opening Ithaca; main Case Study A-Lab; five cases in guides; natural-science guide points to the Case Study | One job per appearance |
| Q6 | Marcus main thread; all five in guides; unnamed chemistry major for natural science | Rotation table |
| Q7 | New terms verification authority, prototype, peer test, workflow card; model card in Core with Ch. 17 wording | Deep-term rule; R16 in week 13 |
| Q8 | **R16 required in part** (abstract, Figures 1–2, ~900 words) | Section 4 alone is ~2,670 words; full paper → ~2.6 h |
| Q9 | **A13 graded only on new work**; A11 parts marked, no credit; rubric 3 / 1.5 + 1.5 / 2 / 1 + 1 | Brief rule; course split |
| Q11 | A-Lab: hallucination (4 of 40 unconfirmed) and chain link 2, documented by the correction; fallback "other" | Ch. 4 defining features |
| Q12 | TPMG scribes from abstracts only, tier "reported by the deploying organization"; Wong et al. (2021) as alternate | Editor's access note; never imply independent evaluation |
| Q13 | From the Field = Şeker (2016) sentiment-analysis entry; no D16 unless the author says the project was commercial | Unassigned; "domain dependency" is the chapter's idea |

Book-wide (handoff `## Decisions`): Q3, Q4, Q7, Q9.

**For the editor:** (a) assign ids from C22–C28 to the seven cases: Ithaca (2022), Zillow Offers (2021), TPMG ambient scribes (2023–2025), silicon samples (2023–2024), A-Lab (2023–2026), Tesla Autopilot recall (2023–2024), Tutor CoPilot (2024–2025); (b) ftf-sources.md row: Ch. 19, Duygu Analizi (2016), 1L9GhfySDnmUNN4BdK1BMzkexUSQ02IzR; with Ch. 10's Social CRM (same issue) book-level references need 2016a/b; (c) `regulation_map` not yet written (ch18); (d) refresh-list: every field rule, RQ24-009 status, Aeneas, Tutor CoPilot peer review, university tool access, Deep 19.A data; (e) log the three research subagents' web use in docs/ai-use-log.md (shared file); (f) visual-guide.md lists Signature 2 (jagged) as reused in Ch. 19: not reused; the heat map takes its place; (g) bot-blocked or paywalled pages (not retried): catalyst.nejm.org (editor's notes used), journals.aps.org (PRX Energy full text, 403), nature.com (login wall; PMC copies read), cnbc.com (403).

## Author-only items (collected for the end)

1. **Live syllabus:** R16 required in part; A13 wording (graded on new build, runs, peer test; may extend A11); Lab 19.1 flow; LO tags.
2. **From the Field:** approve the 2016 entry with present-day connections marked; say whether its "project" was commercial (then D16). Optional: a real, anonymized moment where a model built for one sector failed in another; never written for him.
3. **Tuesday demo (Apr 20):** which end-to-end workflow, so 19.5 mirrors it; a dated recording for Compass.
4. **Instructor package by Apr 20–22:** seven guide one-pagers; seven provided scenarios with dated outputs; A13 and card templates; peer-test card; class heat-map poster.
5. Final voice edit.

## Planned references and verification status (2026-10-18)

Full records and read status are in build/ch19/research-*.md and build/sources/nejm-catalyst-ambient-scribes.md. **Read:** Mitchell et al. (2019, arXiv v2; [VERIFY] ACM pages 220–229); Assael et al. (2022, PMC); Szymanski et al. (2023) and its Author Correction (2026, PMC); Argyle et al. (2023); Bisbee et al. (2024; [VERIFY] issue); Zillow (2021a–c, SEC EDGAR) and Veiga (2021, AP); Tesla (2023) recall report and NHTSA (2024a, 2024b) resumes; Wong et al. (2021); Wang et al. (2025, EdWorkingPaper 24-1054, all versions); Pearce et al. (2022); Şeker (2016, Drive). **Partly read:** Assael et al. (2025, repository abstract); Leeman et al. (2024, Crossref abstract; APS 403); Tierney et al. (2024, 2025, abstracts only, editor). **To verify at draft:** all field rules in §5b and 19.4; RQ24-009 status; Tutor CoPilot peer review; Deep 19.A–B sources (Anthropic education report, 2025; Liang et al., 2024); press bylines (The Register, Chemistry World).
