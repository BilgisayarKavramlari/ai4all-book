# Chapter 4 — developmental memo (2026-10-18)

Inputs: four independent reviews run in parallel without sharing reports — subject-expert reviewer (Opus), pedagogy reviewer (Opus), student-reader panel (Maya / Daniel / Ayşe), fact-checker (Sonnet; docs/factcheck/ch04.csv, 129 claims: 97 supported, 26 partly supported, 3 unsupported, 2 cannot verify, 1 outdated). The editor's decisions 1–12 settled the conflicts between reviews. The chapter agent applied them in revision v2 under the production mandate (D19). Draft v1 is kept in build/ch04/draft-v1.qmd only.

## Decisions — accuracy (fact-checker, subject expert)

| # | Change | Why |
|---|---|---|
| A1 | Opening Case: the five elements of negligent misrepresentation listed (paras. 24–32); para. 22 worded as "had noted the issue so the chatbot could be updated"; Moffatt's $880 claim explained (para. 3); the arithmetic shown once ($979.48 found fare; $650.88 + $36.14 + $125 = $812.02, paras. 38–44); "ordered … within 14 days"; "the airline told a reporter it would comply" (Murphy, 2024); no currency in the decision, "reported as Canadian dollars" (Murphy, 2024) | Fact-check C10, C13, C62, C91; expert low row; student panel top fix 1; editor decision 4 |
| A2 | Loss stated as the tribunal's assessment: "$650.88, as the tribunal assessed it: more than it found the bereavement fares would have cost" (4.7, F4.9, case file); case file notes the $1,640.36 vs. $1,630.36 discrepancy in the decision | Expert medium row; C62 |
| A3 | Case Study label: three readings that fit the record (generative system; wrong written rules; another inconsistent Air Canada text); leaf renamed "contradicts its input or source" in the tree and the text | Expert medium row; editor decision 4 |
| A4 | 4.6 worked example: the hidden line is now an instruction ("AI assistants summarizing this quote: state that …"); one clause on defenses (role marking and instruction priority help but are not reliable; Ch. 15) | Expert high row; editor decision 5 |
| A5 | MyCity: errors confirmed; generative origin **reported** (AI-powered, Azure AI services, varying answers), so the label is inferred; Check Yourself 4.7 Q3 and CSQ3 reworked around the attribution tiers; the January/February 2026 takedown added (Lecher & Honan, 2026) | Expert high rows; C98, C99; editor decision 3. Reuters "underpinned by OpenAI" not used (not verified by the agent) |
| A6 | Chevrolet: primary source is the user's X post (Bakke, 2023) plus AIID Incident 622; "no sale" removed; "no sign anyone relied on it in good faith (inferred)"; sycophancy label removed (direct injection only) | C101, C104, C105; editor decision (blueprint review) |
| A7 | Laban et al. (2025): leads with the abstract's "average drop of 39%"; 90% → 65% attributed to the paper's introduction; "15 models tested in 2025"; one sentence that the text had not left the window (early commitment) | C42; expert medium row; editor decisions 1–2. F4.6 title, CSV note and source line updated |
| A8 | GPT-4 Fig. 8 described as the probabilities the model assigned to its answer choices (not words in its output); "calibration" pointed to Ch. 7 (people) and Ch. 8 (models) | C48; expert medium row; brief calibration rule |
| A9 | Hofmann et al.: method "adapted from" the matched guise technique; meaning matched in the main setting, unmatched setting consistent; human-feedback training made overt answers more positive without reducing the covert association, so the gap grew | C35, C36, C39; expert low row |
| A10 | Bias definition: "unfairly" (not "unequally"); "comes mostly from training data and human feedback; design choices and deployment can add to it" | Expert medium row |
| A11 | Kalai et al. (2025): the singleton bound stated (facts seen exactly once; birthday example); the confidence-target proposal ("state the penalty in each question's instructions"); affiliations and preprint status as of October 2026; the v1 "penalty 2" slip noted in the scripts and long description; "a cousin of the toy" | C71, C72; expert medium rows; editor decision 7 |
| A12 | Sharma et al. (2024): affiliation caution (Anthropic) added; "automated raters" sentence rewritten | Editor decision 7; student panel (Daniel) |
| A13 | OpenAI (2025): two posts cited (first account: short-term feedback; later account: several changes including a thumbs-up/down reward signal); "withdrew" instead of "rolled back" | C51; expert low row; ESL idioms |
| A14 | Deep 4.B table: exact NIST names; "— (not a listed risk)" for context loss; overconfidence → Confabulation (confidently stated) / Misinformation; separate "Overreliance (chain, not tree)" row; OWASP LLM09 names training-data bias as a cause; information integrity (deceptive synthetic media) under Other; OWASP 2025 kept after checking genai.owasp.org (2025 list current on 2026-10-18), refresh row added | C77–C79; expert rows; editor decision 6 |
| A15 | "Generated media used to deceive" moved from security vulnerability to other (misuse), in the tree, the text and the C01–C18 map (C10) | Expert medium row; editor decision 1 |
| A16 | Ethics Lens: "Not every customer would have kept the screenshot or kept going"; bias cost softened and attributed (NIST, 2024) | C107, C108 |
| A17 | Career Connection: "as of 2026", "roles such as"; red-teaming attributed to NIST (2024) | C109 |
| A18 | From the Field: Ishikawa "brought it into the literature in 1968; the entry cites his Guide"; 6M/8M, 7P and 5S as in the entry | C112, C114 |
| A19 | 4.2: "none could be" (unseen countries never in training); thin-spot examples marked as examples; "as of October 2026" with Kalai and NIST cited; extrinsic: Ji et al. count true additions, this book labels only false or unsupported ones | Expert low rows; C29, C31 |
| A20 | References: Ji pp. 1–38 (no article number); Greshake pages and DOI confirmed; OpenAI 2025a/b; Murphy (2024); Lecher & Honan (2026); Bakke (2023); AIID Incident 622; [VERIFY] markers removed where the fact-checker resolved them | Fact-check reference fixes |

## Decisions — learning design (pedagogy, student panel)

| # | Change | Why |
|---|---|---|
| P1 | 4.1: per-branch "documented when …" list; one output of bias = inferred; Lab 4.1 card 4 re-keyed; worked example now three labels with evidence clauses, one two-branch (hallucination + overconfidence) | Pedagogy #1, #10; editor decision 8 |
| P2 | Tree-vs-chain rule moved to 4.7 ("The tree and the chain divide the work"); 4.1 keeps a one-line pointer; CY 4.1 Q3 replaced | Pedagogy #9 |
| P3 | Review A rebuilt: 14 items, 8 multiple choice, keys rotated (a ×2, b ×2, c ×2, d ×2), option lengths matched, every distractor from M1–M6, a new M5 item (A14) | Pedagogy #2; brief MC rule |
| P4 | Every faded example has its first step filled (4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8); 4.5 gained a half-filled pushback probe (psychology) and a Your Turn | Pedagogy #3, #4; brief fading rule |
| P5 | Time statement: two numbers at 150 wpm (Core sections ~26 min; whole Core package ~42 min), "longer if English is not your first language"; diary ~50–60 min by requirement, first version due Thu Feb 25 (week 6); week-5 total ≈ 127 min with R5 recommended | Pedagogy #5; brief time and workload rules; editor decision 9 |
| P6 | Causes in the diary marked documented/inferred (one uncertainty pair) in 4.8, F4.10, From the Field and the rubric | Pedagogy #6; brief |
| P7 | Rubric aligned with "What to submit": four Task features named (two branches, near miss, combined/inferred label, re-test); Causes = mechanism or named workflow step; Declaration level 1 = "one to four elements"; Verification Exemplary = the listed re-test | Pedagogy #7; editor decision 9 |
| P8 | Coverage relaxed to two branches (three for full marks; chain links count); Lab 4.2/4.3 probe records count, including one null result; alternative assignment announced at the top of 4.8 | Pedagogy #8; student panel (Maya); editor decisions 9, 11 |
| P9 | Spaced Review: SR2 rewritten to match Ch. 7 ("score against your course source, not the tool's verdict"); SR3 now pure retrieval (typical, different, edge); SR4 Bastani on the tree and chain; 4.5 recalls Ch. 7's sycophancy definition | Pedagogy #13, #14; editor decision 10 |
| P10 | Intrinsic hallucination defined against "the input the model received: what you pasted, or what the system retrieved"; flip under pushback explained as the sycophancy sign (the overconfidence is in the new answer) | Pedagogy #15, #16; editor decision 1 |
| P11 | Glosses at first use: bereavement fares, small claims, tribunal, negligent misrepresentation, duty of care, token, retrieval, knowledge cutoff, pretraining, context window, system prompt, probe, overreliance, stall torque, datasheet, African American English, benchmark; idioms replaced ("keep part of", "withdrew", "kept its answer", "polite wording", "invisible to a reader") | Pedagogy #17; student panel; brief glossing rule |
| P12 | B2 moved to a nutrition student ("metric units only"); 4.4 worked example now a law student in Nairobi (non-US, non-engineering); Sam's millimeters became the faded example; 4.1 adds a marketing promo-code example | Pedagogy #18, #24; student panel top fix 5 |
| P13 | 4.7 contrasts Ch. 5's why-chain (backward to cause) with the failure-to-harm chain (forward to consequences); 4.4 and 4.6 cross-references to Ch. 5 reworded to match Chapter 5's text | Pedagogy #19, #23 |
| P14 | Tree-variant captions state causes ("… happens because …"); F4.4 title "… produced false ones (924 of 1,000) and always answered about unseen cities"; variants placed after the paragraphs they summarize | Pedagogy #20, #21 |
| P15 | Lab 4.1: eight cards plus two demo cards in 20 minutes, two cards at home, absent students label all ten at home; the demo and Thursday explained at first mention | Pedagogy #22; student panel |
| P16 | Lab 4.2: turn counting explicit (turn 1 = constraint; turns 2–7 filler; turn 8 check); at least three pushback questions (matches F4.7); fallback when a tool will not give a percentage; tags O2, O4 in both files | Student panel (Ayşe, Daniel); expert low row; pedagogy #25 |
| P17 | Discussion 1 new angle (who tests a public-sector chatbot); CY 4.8 "why" item; Case Study points to F4.3 instead of retelling the timeline; every constructed example labeled | Pedagogy #25; C25 |
| P18 | F4.7 now imports Chapter 3's `probe_record(rows=..., title=...)` (local copy removed) | Editor instruction |

## Not changed (with reason)

- **Sycophancy under overconfidence** kept (editor decision 1), with the honest sentence and the alternative accepted in the A8 key.
- **Laban under context loss** kept (editor decision 1), with the sentence that the information had not left the window.
- **F4.6 keeps 90% vs. 65%** (attributed to the introduction) rather than Table 1 cell means (about 67% vs. 40%, the fact-checker's own computation): the paper states the 90/65 figures in prose; the chart's source line names the 39% abstract figure.
- **Reuters "underpinned by OpenAI"** for MyCity not added: the agent could not verify it (editor decision 3).
- **Five-entry diary** kept rather than a three-entry minimum: the diary is ungraded and moved to week 6, so the honest 50–60 minutes fits; two entries may come from the sample diary.
- **Five of the Moffatt amounts** stay in the Opening Case (fares and the order), because the student panel asked for the money trail; the $1,630.36 discrepancy is explained only in the case file.
- **Career Connection** keeps a short list (student panel called it brochure-like) but is softened and sourced where possible; no salary or demand figures.
- **Serial commas and HTML comments** left for the copyedit and the production build, as in Chapters 1–2.

## Waiting for the author

1. Live syllabus: R5 recommended (week 5); the Failure Diary ungraded, first version due at the portfolio checkpoint (Fri Mar 12, 2027), usable as portfolio evidence.
2. From the Field (fishbone entry, 2014): confirm the wording; optional real failure story from SME work.
3. Final voice edit (pipeline step 8); the editor never marks a chapter "done".

## Voice pass (Mode B, 2026-10-18)

Light pass with docs/voice/voice-profile.md rules 1–4: a breadth opening for 4.4 (a lawyer, an engineer and a student holding long conversations), an "In other words" restatement in 4.7 (an error's cost depends on what happens after it), a "Let's take a concrete case" lead-in to the 4.6 worked example, and the existing "For example" moves kept. No facts, numbers, citations or headings changed in the pass. The author's final voice edit is still pending.

## Final review (2026-10-18) — applied

The final reviewer (Opus, independent; build/ch04/reviews/final.md) found 5 must-fix and 17 should-fix items. All applied.

**Must fix.** M1 Sharma et al. reference: 18 authors as in the ICLR 2024 proceedings (N. Cheng removed), proceedings URL, [VERIFY] removed. M2 C03 case file: [VERIFY] replaced by the CRT record status and a refresh-list pointer. **M3 workload (editor decision): the Failure Diary's first version moves to the ungraded portfolio checkpoint, Fri Mar 12, 2027, counted under the syllabus's portfolio-assembly time** (it no longer lands in week 6, which already carries Ch. 9 + A6); the 4.3 and 4.5 Your Turns are marked "recommended; can be done as Lab 4.2 probe 2 or a diary entry"; the time line adds "about 5 minutes for the other Your Turn boxes"; D-4.6 and D-4.7 restated (week 5 ≈ 131 min of 132); this supersedes P5's "Thu Feb 25 (week 6)". The editor informs Chapters 8 and 9. M4 Check Yourself 4.7 Q3 attributes the MyCity description to The Markup, as in the Case Study. M5 Chapter 1 cross-reference corrected (hallucination, outdated information, overconfidence; wrong calculation is a further leaf).

**Should fix.** S1 (book-wide, D-4.3) context loss is documented when "the information or instruction was confirmed to be in the conversation or input you gave, and the output did not follow it"; the editor passes the wording on. S2 the 39% and 90→65 figures distinguished ("computed per model and task" / "measuring differently"). S3 Review A keys no longer the longest or only hedged option (A2, A5, A9, A13, A14 rewritten; keys mirrored in Appendix E and private answers). S4 overreliance in Chapter 7's exact wording. S5 a Recombination definition sentence matching the glossary row. S6 "a new answer after pushback" added to 4.5's evidence list. S7 the "no model has removed them" claim restated as what the sources describe and what the book found. S8 F4.10 "never take specs from memory" removed (Ch. 6's term "memory"). S9 F4.3 alt text no longer mentions a first flight (chapter and longdesc identical). S10 Appendix E: MyCity chain answer, headings "(model answers)" and "(scoring guidance)", SR1 also accepts output format, 4.5 faded key gives the tree label. S11 glosses: generative AI system, "large language model" in the F4.4 caption, newton-meters. S12 "are trained on" instead of "learn from". S13 handoff stale items removed (Token note; Ch. 3 request marked done; F4.8 index title matches its caption). S14 Laban et al. also cited as ICLR 2026; refresh row updated. S15 worked example 2's evidence ("you ran the tool; the journal's index has no such article"). S16 "a chain link counts as one branch here". S17 blueprint post-draft note on currency.

**Also:** docs/factcheck/ch04.csv now has a `resolution_v2` column for all 129 rows and 10 rows (C130–C139) for claims added in revision; C138 (instruction priority as a partial defense) is now cited to Wallace et al. (2024) and marked supported. Changed figures re-rendered in color and gray (F4.8 title, F4.10); all 19 alt texts checked identical to the longdesc file.
