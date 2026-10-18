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
