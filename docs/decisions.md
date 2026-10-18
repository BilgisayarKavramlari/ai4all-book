# Decision log

Decisions made by the author. Proposals become decisions only when the author approves them. Newest first. When this file conflicts with docs/context/ (Drive), this file wins.

## 2026-10-16 — Book decisions (approved by the author)

| # | Topic | Decision | Notes |
|---|---|---|---|
| D1 | License | CC BY-NC-SA 4.0 for the book; a separate written license from the author to OptiWisdom for use in Compass | Dual licensing keeps the open edition unchanged |
| D2 | Title | Keep *AI for All: Career-Ready AI Skills*; keep the subtitle prominent on the cover | Run a U.S. trademark (USPTO) search before the cover is final, because of name similarity with the AI4ALL nonprofit and a UConn course |
| D3 | Publication model | **Start with Draft2Digital**: EPUB 3 ebook and D2D Print paperback (print at cost). Open-web edition later. Second edition: consider a peer-reviewed or open-access publisher | Ebook price (free vs. low price) not decided yet |
| D4 | ISBN | Author's own ISBNs, not D2D's free ISBN; at least three: ebook, print Volume 1, print Volume 2 | Confirm the current price before buying |
| D5 | Volumes | Two print volumes: Volume 1 = Parts I–II (Ch. 1–10, to the midterm); Volume 2 = Parts III–VI (Ch. 11–23) | Each volume has its own ISBN |
| D6 | Certification | Two levels: "AI for All Certified — Foundations" and "— Practitioner"; issued by OptiWisdom, not UTD credit; no UTD logo | |
| D7 | Compass MVP (January 8, 2027) | Part I pages, Chapter 1–4 quizzes and lab pages, interactive versions of three signature diagrams. The tutor-mode assistant comes later in the term | Assistant needs privacy work first (FERPA, KVKK, retention) |
| D8 | Illustration | In-house figure system (Mermaid/SVG, docs/visual-guide.md); a freelance illustrator only for the 12 signature diagrams and the chapter maps; contract by mid-November 2026 | Funded outside any grant (see D10) |
| D9 | Recurring characters | Five recurring students from different majors | The author chooses names, majors and arcs in docs/characters.md before Chapter 1 is drafted |
| D10 | Grant scope | **The book is not part of the course development grant.** The grant has not started; the book is the author's own work and no grant funds are used for it | Supersedes the design guide's grant-ownership question and its "grant-funded tasks" list (illustrator, copyedit, test bank) |

## 2026-10-16 — Design decisions (ai4all-book-designer step 1, approved)

| # | Topic | Decision |
|---|---|---|
| G1 | Trim size and layout | 8.5 × 11 in, single text column with a wide side margin (option O3 in docs/design-options.md) |
| G2 | Fonts | Source Serif 4 (body), Source Sans 3 (headings, callouts, figures), JetBrains Mono (prompts, code); all SIL OFL, embedded |
| G3 | Callout family | R · Rules: elements distinguished by border/line style + icon + label, never by color |
| G4 | Palette | Starting palette F for EPUB: human #1C3D6E · AI #FCE38A · risk #C2410C · verified #4CAF84. In print, meaning is carried by shape and line style; every figure has a hand-checked grayscale render |

## Earlier decisions (from program context)

- 2026-10-16: Book in English first (Turkish adaptation later); no page limit; diagram-heavy; many hands-on labs and cited cases; current-developments and philosophy chapters; "How to Use This Book"; parallel to the Spring 2027 syllabus; end-of-chapter assignment, discussion and review questions.
- 2026-10-16: The digital companion is a project inside OptiWisdom Compass, from chapter exercises to the certification exam. Compass is optional, free and ungraded for UTD students.
- 2026-10-16: Final exams are held on the last class day (CS 2V95: Thursday, May 6, 2027).

## 2026-10-18 — Decisions made by the editor on the author's delegation

The author asked the editor to make suitable choices for open items and to escalate only what cannot be resolved.

| # | Topic | Decision | Notes |
|---|---|---|---|
| D11 | Recurring characters | Lucía Herrera (accounting), Marcus Bell (nursing), Elif Kaya (psychology, from İzmir), Sam Okafor (mechanical engineering), Hana Nguyen (arts and technology, they/them). Story bible: docs/characters.md. Front-matter section "Meet the Students" tells readers they are fictional composites | Author may revise any detail |
| D12 | Figure 1.3 providers | Keep two real outputs from two models of one provider (Anthropic), labeled as such in the text and caption — a documented exception to style sheet §3 until a second provider's output is added | Swap one panel before print if possible |
| D13 | From the Field, Chapter 1 | Based on the author's published article on AI tools for SMEs (Şeker, 2023), without naming the product, with a conflict-of-interest disclosure | **Approved by the author 2026-10-18** |
| D14 | How This Book Was Written | First draft written from the AI-use log and decisions; declares OptiWisdom interests and that the book is not grant-funded | **Conflict-of-interest statement approved by the author 2026-10-18**; rest of the section pending the author's voice edit |
| D15 | Course policy wording | "Personal or confidential data in public AI tools" appears in the book's not-acceptable zone as "course guidance" | The author should add it to the live syllabus policy |
| D16 | From the Field disclosures, Chapter 2 onward | Use the conflict-of-interest wording approved in "How This Book Was Written" (D14): "I am a founder of OptiWisdom, which develops software for businesses, including AI tools." Chapter 1 keeps its approved D13 wording | Editor decision under delegation (2026-10-18); consistent with the approved D14 statement |
| D17 | Week 2 schedule (Chapter 2) | Chapter 2 is read before Tue Jan 26; Tuesday's 10-minute opening case is the Amazon recruiting tool; Tuesday's ungraded concept check includes 2–3 Chapter 2 items; Thursday's reading is Chapter 3. Applied to the repository's working copy of the syllabus | **Approved by the author 2026-10-18**; the author updates the live syllabus |
| D18 | Chapter 3 blueprint proposals | Reversal curse (Berglund et al., 2024) is the Opening Case and main Case Study; From the Field uses the author's 2024 manuscript on LLM-based modular software development (unpublished; cited as a manuscript); R1 becomes recommended rather than required in week 2 so the week stays near 2 hours | Decided by the editor under D19 (2026-10-18); the author updates the live syllabus |
| D19 | Production mandate | The author asked the editor to finish the whole book without asking him. The editor decides editorial matters, records them here, and collects author-only items (personal anecdotes, final voice edits, live-syllabus changes, money and credentials) for the end. Chapters are produced by chapter agents under docs/production/chapter-brief.md | **Author's instruction, 2026-10-18** |
| D20 | Examinable scope | The midterm covers the Core sections of Chapters 1–10 and the final the Core sections of the whole book; Deep chapters (6, 13, 17, 22, 23) and Deep sections are not examinable. The practice exam and syllabus wording should say "Core sections" | Editor decision under D19 (2026-10-18); the author updates the live syllabus wording |
| D21 | Week-5 workload exception | Week 5 (Chapters 4 and 8, A5) is about 2.4 h out of class after all cuts (R5 recommended, Failure Diary moved to the Mar 12 checkpoint, A5 verifies eight of ten claims). Accepted as a one-week exception rather than cutting the verification skill the course is built on | Editor decision under D19 (2026-10-18); the author may trim further in the live syllabus |

## Chapter-level decisions (from handoffs)

<!-- ch03-decisions -->
### Chapter 3
| # | Topic | Decision | Notes |
|---|---|---|---|
| D-ch03-1 | Signature 4 code | `llm_anatomy(stage="complete", highlight=None, note=None)` in figures/scripts/ch03_figures.py; stages "tokens", "scores", "context", "complete"; `highlight` takes a set of parts (context, system, conversation, retrieved, prompt, tokens, model, scores, sampling) and overrides the stage; ≤ 9 boxes. **v2:** the figure now numbers the same four steps as section 3.2 (1 tokens, 2 score, 3 pick, 4 add and repeat); the scores box is unnumbered | Later chapters import it |
| D-ch03-1b | Probe record code | `probe_record(rows=None, title=...)` returns a draw function; `rows` = list of (label, text) pairs; a label containing "Result" is drawn as a dashed hexagon. Default rows unchanged; the footer now says "options used (search on or off)" (terminology decision 1) | For Chapter 4 F4.7 |
| D-ch03-2 | Next-token scores | No small open causal model in the local cache; all next-token scores illustrative, seeded picks recorded | Unchanged |
| D-ch03-3 | Parallel text for token counts | Full UDHR (Unicode UDHR via NLTK udhr2, SHA-256 recorded), nine languages; o200k_base and cl100k_base, named in figure source lines and data only ("a newer / an older tokenizer" in student text) | Editor decision 6 |
| D-ch03-4 | From the Field source | **v2:** cites the published article (Şeker & Nizam-Özoğur, 2026, *Electrica* 26, Article 0033, doi:10.5152/electrica.2026.25033; full text read) with the 2024 manuscript as its earlier version; facts limited to what both say, details only in the manuscript attributed to "the earlier version"; product not named in the text (its name is in the reference title); co-author named; D16 disclosure kept | Author approval requested |
| D-ch03-5 | Figures vs. blueprint | F3.7 cut; F3.11 omitted; F3.13 and F3.3d added; F1.4 reuse kept (pedagogy suggested an in-text reference only; the editor's brief asked for the reuse) | 16 appearances |
| D-ch03-6 | Case failure label | C16 labeled on Signature 5 (primary hallucination, inferred) in the case file and handoff only; the chapter describes the failure in plain words and points to Chapter 4 (book-wide rule; editor decision 6) | Figure import when Chapter 4's `failure_tree` exists |
| D-ch03-7 | Terminology | "settings (parameters)" for learned values; "options" for temperature, search and memory toggles; never "temperature setting" | Editor decision 1 |
| D-ch03-8 | Verdict scale | Section 3.5 examples, Your Turn and Review B3 use the book-wide five verdicts with a pointer to Chapter 8 | Book-wide rule |
<!-- /ch03-decisions -->
<!-- ch04-decisions -->
### Chapter 4
| # | Decision | Notes |
|---|---|---|
| D-4.1 | **Signature 5 API (book-wide).** `failure_tree(highlight=(), dashed=(), causes=(), leaves=True, tag=None, note=None)` in figures/scripts/ch04_figures.py; branches in the visual guide's order plus a plain "other" box (7 boxes); `tree_height(causes)` gives the canvas height (470 without causes, 560 with; add ~34 when both `tag` and `note` are used). Leaves: outdated information and wrong calculation or reasoning under hallucination ("contradicts its input or source" is the intrinsic leaf); sycophancy under overconfidence; **"misuse, such as fake media made to deceive" under other** (moved from security in v2) | Import, never redraw |
| D-4.2 | **Failure-to-harm chain API (book-wide).** `failure_chain(notes=None, highlight=(), dashed=(), tag=None)`: stage 0 output (hexagon), 1 "checked before use?" (diamond), 2 reliance (rounded), 3 loss (risk), plus a "caught" box. Human and workflow failures are labeled on a stage of this chain | Used for every human/workflow failure label |
| D-4.3 | **Defining features for documented labels (book-wide).** Hallucination: shown wrong or unsupported **and** generation confirmed. Bias: the same skew across matched outputs (one output = inferred). Context loss: the information or instruction was confirmed to be in the conversation or input you gave, and the output did not follow it (revised after the final review: a user cannot confirm what a long chat still passes to the model). Overconfidence: expressed certainty (stated %, absolute words, an exact figure for something that varies, a new answer after pushback). Security: instruction-like text in the input that the output followed. A feature that is only **reported** (named outlet) keeps the label inferred; say "reported" in the case text (attribution tiers) | Makes labels gradable (pedagogy #1; subject expert MyCity row) |
| D-4.4 | **Sycophancy stays a leaf of overconfidence**, with one sentence that the literature treats it as its own behavior; a flip under pushback is the sycophancy sign; "its own category" with a reason is accepted on exams | Editor decision 1 |
| D-4.5 | **Moffatt has one job per chapter.** Ch. 4: facts, chain, tree label; Ch. 10 (week 7, R7): disclosure and communication at work; Ch. 18: liability and governance | Avoids redundancy |
| D-4.6 | **Failure Diary:** ungraded in CS 2V95; first version due at the ungraded **portfolio checkpoint, Fri Mar 12, 2027**, counted under the syllabus's "about 5 hours across the term for portfolio assembly"; ~50–60 min by requirement; causes marked documented/inferred (one uncertainty pair); lab probe records count | Editor decisions 9 and final-review M3 (moved from Thu Feb 25 because week 6 already carries Ch. 9 + A6) |
| D-4.7 | **Week 5 workload.** Required out of class: Ch. 4 Core package ~42 min + Ch. 4 Your Turns ~5 min (4.3 and 4.5 Your Turns are recommended and can be done as Lab 4.2 probe 2 or diary entries) + Ch. 8 (~37 min reading and Your Turns + A5 ~45–50 min) ≈ 131 min, within the 2.2 h (132 min) target. R5 stays **recommended** (would add ~15 min). The diary is no longer in week 5 or 6 (D-4.6) | Brief workload rule; final-review M3. The editor tells Chapters 8 and 9 |

**Note for the Chapter 8 agent (what Chapter 8 should only recall, not re-teach):** (1) the Failure Taxonomy Tree and the documented/inferred rule with D-4.3's defining features (import `failure_tree`; Mata v. Avianca: hallucination, invented sources, documented; overconfidence documented only if the opinion records the tool affirming that the cases were real; chain link 2 failed); (2) the causes of hallucination from 4.2 in at most two sentences (likely text with no truth check; recombination, worst for facts seen rarely) and intrinsic vs. extrinsic; (3) the pushback test (4.5) and probe-record format. Chapter 8 owns the Verification Funnel, citation checking, uncertainty signals, calibration measurement, fabricated-citation rates and A5. Chapter 4 mentions model calibration in one sentence (GPT-4, 2023) and points to Chapter 8.

**Note for the Chapter 7 agent:** Chapter 4 section 4.5 opens with "Chapter 7 named sycophancy" and reuses Chapter 7's definition word for word; Spaced Review 2 and 4 rely on Chapter 7's "score against your course source, not the tool's verdict" and on the Bastani labels in Chapter 7's Case Study (hallucination of the wrong-calculation kind; overreliance on the chain). Please keep those wordings.

**Editor requests (other chapters' files):** (a) done: Chapter 3's Deep 3.B pointer already names Chapters 4 and 8; (b) diary lines are present in Chapters 1, 3, 5 and 7 (checked 2026-10-18); Chapter 1's lines say the diary is in section 4.8 ✓; (c) **reference disambiguation:** Chapters 4 and 5 both cite "Şeker (2014)" for two different 2014 entries (fishbone; 5 Whys); the book-level reference list will need 2014a/2014b; (d) Chapters 8 and 9: the Failure Diary's first version now falls at the Mar 12 portfolio checkpoint, not in week 5 or 6.

**Case labels on the tree and chain, C01–C18 (proposals for each case's chapter agent; apply D-4.3 and verify against each case's sources).**

| Id | Case | Tree (primary [+ secondary]) | Chain link | Notes |
|---|---|---|---|---|
| C01 | Support-center study | none on the tree | — | Productivity study; uneven benefit |
| C02 | Amazon recruiting tool | bias, documented (penalized "women's" across résumés) | — | Mechanism (pipeline stages) partly inferred, as in Ch. 2 |
| C03 | Moffatt v. Air Canada | hallucination, inferred | link 2 no accuracy check, documented | This chapter |
| C04 | Bastani et al. | hallucination (wrong calculation), documented | link 3 overreliance, documented | As in Ch. 7's Case Study |
| C05 | Mata v. Avianca | hallucination (invented sources), documented [+ overconfidence, documented if the opinion records the tool affirming the cases; VERIFY] | link 2 no verification, documented | Ch. 8 |
| C06 | Deloitte Australia report | hallucination (invented sources), documented if the firm confirmed generative-AI use; otherwise inferred | link 2 review failed, documented | Ch. 9 |
| C07 | Vanderbilt Peabody email | none on the tree (output not wrong) | inappropriate delegation, documented | Ch. 10 |
| C08 | Obermeyer et al. | bias (proxy label), documented | — | Not generative; Signature 3 also applies |
| C09 | Dell'Acqua et al. (BCG) | hallucination (wrong reasoning), inferred | link 3 overreliance outside the frontier, documented | Ch. 12 |
| C10 | Arup deepfake fraud | **other (misuse: fake media made to deceive)**, documented | link 2 no independent check of the request, documented | Ch. 13, 15 (changed in v2) |
| C11 | Replit agent database deletion | context loss (ignored code-freeze instruction), inferred [+ hallucination if reports confirm misreported state; VERIFY] | link 2 no approval gate, documented | Ch. 14 |
| C12 | Samsung source-code paste | none on the tree | user data leakage (link 3), documented | Ch. 15 |
| C13 | Gender Shades | bias (unequal quality across groups), documented | — | Ch. 16 |
| C14 | Dutch child-benefit scandal | bias, documented | link 2 no meaningful human review / opacity, documented | Ch. 17; not generative |
| C15 | Thomson Reuters v. Ross | other (intellectual property) | — | Ch. 18 |
| C16 | Reversal curse | hallucination (wrong or missing reverse answer), documented | — | Ch. 3 |
| C17 | Medprompt | none on the tree | — | Positive study |
| C18 | Klarna AI assistant | none documented on the tree | inappropriate delegation, documented only if the company's own statements say quality fell [VERIFY] | Ch. 5 |
<!-- /ch04-decisions -->
<!-- ch05-decisions -->
### Chapter 5
| # | Topic | Decision | Notes |
|---|---|---|---|
| D-5.a | Signature 7 (Delegation Ladder) | Order = AI Fluency v1.1 Modality 1–3 over a floor "no AI"; one axis (how hard it is to see and check what the AI contributed before it takes effect) describing each rung's **default**; a design can restore a check before outputs take effect (approval gate, Ch. 14) without changing the rung; ladder, floor and axis labeled as the book's construction. `delegation_ladder(highlight=None, annotate=None, note=None)` | Ch. 12, 14, 21 reuse |
| D-5.b | Signature 6 (Anatomy of a Prompt) | Six parts; "task" always needed (thick border); box label "In-context examples"; Role = voice or perspective, audience goes in context. `prompt_anatomy(highlight=None, note=None)` | Ch. 6, 7, 10, 14 reuse |
| D-5.c | Agency vs. agent | Agency = a way of working (Dakan & Feller, 2025); agent = a system in which the model directs its own steps and tool use (Anthropic, 2024; Ch. 3 wording). Box in 5.2 points to 6.5, 7.5, Ch. 14 | Book-wide rule implemented |
| D-5.d | C01 and C18 | Both agency by the framework's definition; they differ in whether the design kept a human check before each output | Ch. 14 may reuse |
| D-5.e | Week-3 reading R2 | R2 module 2 becomes **recommended** in week 3 so the honest count stays ≤ 2.2 h. Count (150 wpm): Core package ~53 min + Your Turn 5.3 ~5 min (Your Turns 5.1–5.2 are done in Lab 5.1 step 2) + A3 60–70 min = ~2.0–2.15 h; with R2 required, ~2.25–2.4 h | Live-syllabus change: author-only item; precedent D18 |
<!-- /ch05-decisions -->
<!-- ch06-decisions -->
### Chapter 6
| # | Topic | Decision | Notes |
|---|---|---|---|
| D-6.a | Tags in a Deep chapter | 6.1–6.5 and 6.7 tagged Deep; 6.6 Studio; no Core; numbering 6.1–6.7; not examinable (D20); review questions labeled as practice | Model for other Deep chapters |
| D-6.b | Core chapters must not depend on Chapter 6 | Ch. 12, 14, 15, 19 define any Chapter 6 term they use (already in chapter-brief) | Book-wide |
| D-6.c | Context Layers diagram | `context_layers(highlight=None, note=None, side_note=None)` in ch06_figures.py; extends Signature 4's context stage with Ch. 3's labels and two new layers; layer keys "system", "standing", "project", "conversation", "documents", "prompt" | Reusable in Ch. 10, 14, 15 |
| D-6.d | Terminology | "standing instructions" (written "in a tool's options or a project"), "project space", "gap instruction", "prompt template", "placeholder", "prompt version", "prompt library", "prompt chain"; "system prompt" for the provider's layer; "parameters" for learned values and "options" for user controls (Ch. 3/5 rule) | Glossary rows above |
| D-6.e | Medprompt numbers | Text and chart use Figure 4 ("the paper's step-by-step chart"): 81.7 → 83.9 → 87.3 → 88.4 → 90.2; Table 1 / Figure 4 mismatch and Figure 6 increments recorded in data/ch06_medprompt.csv; o1-preview "about 95–96%" | Editor decision 1 |
| D-6.f | Persistent features and agency | Standing instructions / shared projects described as a step toward AI Fluency's agency, not an agent (reusing Ch. 5's box, as Ch. 5 promised "sections 6.5 and 7.5") | Book-wide rule implemented |
| D-6.g | Task placement | "Full task last; optionally one line at the top" attributed to provider guidance (Anthropic; OpenAI GPT-4.1 guide), with Liu et al. stated accurately and "test it" | Editor decision 2 |
<!-- /ch06-decisions -->
<!-- ch08-decisions -->
### Chapter 8
| # | Decision | Notes |
|---|---|---|
| D-8.1 | **Signature 8 API (book-wide).** `verification_funnel(highlight=None, verdict=None, tag=None, note=None, notes=None)` in figures/scripts/ch08_figures.py; `funnel_height(tag, note)`. Stages for `highlight` (a name or a list): "claims", "check" (alias "source"), "primary", "expert", "stop", "verdict", "uncertainty". `verdict` prints one label from `VERDICTS`; `notes` = {stage: short text} beside the rail. 7 boxes. Unchanged in v2 | Import, never redraw (Chapters 9, 10, 11) |
| D-8.2 | **Verdict scale and citation rules (book-wide).** Five verdicts with the v2 meanings (glossary row). Citations: an authoritative record shows the work does not exist, or its details belong to another work → contradicted; any wrong detail that stops a reader from finding the work → contradicted *as cited*, corrected from the record; not found in two indexes no AI tool produced → unsupported, with the indexes named; found but the passage does not support the claim → unsupported (contradicted if it says the opposite). **Checks 1–2 (exists, matches) use an index = stage 1; check 3 (says it) opens the work = stage 2** | Pedagogy #6, #10; expert #16; editor decisions 4–5 |
| D-8.3 | **Definitions owned by Chapter 8 (book-wide):** claim, stakes, verification, independent check, primary source, fabricated citation (failure 1 only), uncertainty signal, consistency check, stated confidence. Chapter 9 reuses them word for word | Hand-off to Chapter 9 |
| D-8.4 | **Passage vs. summary.** Chapter 8 asks whether one passage supports one claim; Chapter 9 asks whether a summary represents a whole source | Ch. 9 boundary |
| D-8.5 | **An AI tool's own "yes" is never a source**; an AI search tool may help find a source, but the verdict rests on the opened source. An index-matching checker (no AI model) does part of stage 1; an AI checker is a signal, not a stage (Deep 8.A) | Mata ¶ 45; expert #5 |
| D-8.6 | **Mata has one job per appearance:** Ch. 1 teaser; Ch. 8 Opening (facts), 8.3 (three checks on "Varghese"), Case Study (labels, stopping stages, workflow), Ethics Lens (costs), Lab 8.1 (excerpts ¶¶ 12, 26, 45). People described by role. **The timing of the lawyer's "is it real?" questions is disputed on the record (¶¶ 46–47) and is always presented that way** | Expert #1; fact-check #5; editor decision 1 |
| D-8.7 | **Calibration wording.** Chapter 8 defines "Calibration (of your own confidence)" as "how closely your confidence in your answers matches how often they are actually correct, across many answers" (Chapter 7's v2 clause) and "Calibration (of a model)" as "how closely a model's stated confidence matches its accuracy". Chapter 7's model clause currently says "how well"; the editor changes it to "how closely" so the two chapters match word for word. A4 and A5 share the idea of a calibration gap; A5's method is in the glossary row | Final review M2; editor decision |
| D-8.8 | **From the Field, Chapter 8:** Şeker (2015), *IEEE Access* 3, 368–380 (Drive 14tfA7WBJODNmUh4Ne5bFSsNQuSPMZPyu). Add to docs/production/ftf-sources.md. The 2014 *YBS Ansiklopedi* Delphi entry (1ffYScBftAW3ttn9JDYoMYRoo7aMppFNY) is not used and remains free | Not commercial; no D16 disclosure |
| D-8.9 | **Overconfidence labeling (book-wide refinement of D-4.3).** Overconfidence needs evidence about expressed certainty (Ch. 4): a percentage, absolute words, an affirmation of reliability, or insistence after a direct question. Before checking, a firm answer is no evidence either way; a plain wrong assertion is hallucination only. A direct question is not a pushback test | Final review M5; editor decision |
| D-8.10 | **Week 5 workload: a documented one-week exception (book decision D21, editor).** A5 lists ten claims but students verify eight; the other two get one line, "not checked" and why. Counted at 150 wpm and by requirement: Chapter 4 ≈ 47 min (its Core package plus Your Turns, D-4.7; its short case 1 is assessed) + Chapter 8 ≈ 96 min (whole Core package 38, pre-lab 5, Your Turns 18, A5 at home 37) ≈ 143 min ≈ **2.4 h**, stated in the chapter's time line | Editor decisions on D-8.10 and final review S1 |

**For the editor:** (a) ftf-sources.md row (D-8.8); (b) Chapter 9: align the "unsupported" wording (glossary note above) and reuse D-8.2's stage mapping for citation checks; label Deloitte (C06) as fabricated citations in one sentence rather than re-teaching the checks; Lab 8.2's record feeds A6; (c) "How This Book Was Written": one sentence that the book's own fact-check uses the same verdict scale; (d) add book decision D21 (week-5 workload exception, D-8.10); (e) Lab 8.1 needs a real dated backup output generated before the term (Instructor package); (f) the live syllabus says the Tuesday demo checks sources "live"; Chapters 4 and 8 move the checking to Thursday (author-only item 1).
<!-- /ch08-decisions -->
<!-- ch07-decisions -->
### Chapter 7
| # | Topic | Decision | Notes |
|---|---|---|---|
| D-7.a | Signature 2 reuse | ch01's `jagged(f)` has no `highlight` argument; Chapter 7 imports it unchanged and adds callouts below the map on a taller canvas (F7.7). Suggest adding `highlight` (and `note`) to `jagged` in ch01_figures.py for Chapters 12 and 19 | Editor to decide; chapter agents may not edit ch01 files |
| D-7.b | New reusable function | `scaffold_crutch(highlight=None | "scaffold" | "crutch", note=None)` in figures/scripts/ch07_figures.py (9 boxes; the same AI reply in two lanes). For reuse in Ch. 10, 19 and 21 | Not a signature diagram; listed so later chapters import rather than redraw |
| D-7.c | Self-assessment artifacts | A4 closed-book scores are not graded; AI use during the closed-book checks is not acceptable; dialogues may be in any language with English glosses of annotated turns (closed-book answers in the course language); self-scoring allowed, teammate check optional; **check questions stay out of the dialogue, and the delayed check uses parallel keyed questions where they exist** | Measurement validity (pedagogy review); pattern for other self-assessment artifacts |
| D-7.d | Syllabus readings, workload and word budget | Cite the peer-reviewed version of a syllabus reading when one exists (R3 → Bastani et al., PNAS 2025); R3 = Significance + Table 1 before Tuesday; R4 = abstract only, discussed in class; the Case Study is read in Tuesday's class; A4 reflection 200–300 words; annotation finished in the lab. **Week 4 counted requirement by requirement: about 2.2 h** (R3 10 + chapter 45 + Your Turns 8 + pre-lab 15 + A4 at home 55 = 133 min), at the editor's ceiling. **Word-budget overrun recorded:** Core 7.1–7.5 is about 4,090 words against ≤ 3,400 (7.4 about 930 and 7.5 about 980 against 650–750 each); Core + Studio about 4,570 against 4,200. The four reviews' required additions (coding rules, pretesting caveat, calibration arithmetic, glosses) outweigh the cuts | Editor updated docs/syllabus.md R3; the live syllabus is the author's |
| D-7.e | Key test and coding rules | Book-wide wording for scaffold vs. crutch: **"Who produced the answer in this turn: you, from your own memory, or the tool?"** (replaces v1–v2 "who recalled and produced …", which let a tool "recall"), plus two rules: a request that sets up your own attempt = S, a request for the answer = C; feedback counts as S only after an attempt at the same question; "OK, thanks" turns are uncoded | Ch. 10, 19, 21 reuse; glossary unaffected (no row for the test itself) |
| D-7.f | Prediction format | One format for self-calibration: a 0–100% confidence rating per question, summed and divided by 100 into a predicted score; calibration gap = predicted − actual, judged on a set, not per question. Same idea as Chapter 8; Chapter 8's per-question form divides by the number of questions (average confidence minus share correct) | Ch. 8 (A5) uses the per-question form |
| D-7.g | A4 rubric | Six criteria within the syllabus's 3/3/2/2 split: Task 3, Annotation 1.5, Closed-book record 1.5, Verification 2, Reflection 1.5, Declaration 0.5; "when a submission fits parts of two levels, give the lower level whose description fully applies" | Pattern for later rubrics that combine reflection and declaration |
| D-7.h | Chapter map | The chapter map's Work Loop strip highlights Frame and Verify; no separate `work_loop` figure | Blueprint said `work_loop("Frame")`; minor deviation |

### Cross-chapter requests for the editor (not edited by the chapter agent)

| File | Change | Why |
|---|---|---|
| chapters/01-why-ai-changes-study-and-work.qmd, about line 199 | "avoided that harm" → "showed no measurable harm on the exam" | Chapter 7 now says GPT Tutor was not measurably different from control (memo A3; final review should-fix 9) |
| chapters/08-*.qmd, about line 268 (and Ch. 8 glossary row) | Own-confidence sense: use Chapter 7's wording exactly, "how closely your confidence in your answers matches how often they are actually correct, across many answers"; keep "how closely a model's stated confidence matches its accuracy" for the model sense | Editor decision on shared calibration wording |
| figures/scripts/ch05_figures.py, `prompt_anatomy` legend | "thick = always needed" → "thick = always needed or highlighted" | F7.10 (and Chapter 6's reuse) highlight parts with a thick border, which the legend does not explain (final review should-fix 7) |
| figures/scripts/ch01_figures.py, `jagged` | Optional `highlight`/`note` arguments | D-7.a |
<!-- /ch07-decisions -->
