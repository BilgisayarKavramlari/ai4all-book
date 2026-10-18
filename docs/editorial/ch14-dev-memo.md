# Chapter 14 — developmental memo (2026-10-18)

Inputs: four independent reviews run in parallel without sharing reports (build/ch14/reviews/):
- subject-expert reviewer (Opus); 20 findings, 2 high;
- pedagogy reviewer (Opus); 4 high;
- student-reader panel (Maya / Daniel / Ayşe, Sonnet);
- fact-checker (Sonnet; docs/factcheck/ch14.csv, 149 claims: 118 supported, 26 partially supported, 2 unsupported, 3 cannot verify).

The editor's ten decisions came with the reviews. The author delegated editorial choices (D19), so the editor decides and records them here. Draft v1 is kept at build/ch14/ch14-draft-v1.qmd. Revision v2 is chapters/14-agentic-workflows-and-human-oversight.qmd: 14,399 words; Core sections 5,545 including Check Yourself and 5,170 without, under the 5,400 cap.

## Decisions — accuracy (expert, fact-checker)

| # | Change | Why |
|---|---|---|
| A1 | 14.6 glosses OWASP's term in one clause: "here 'agency' means a system's ability to act through tools, not the way of working in 14.1". The [VERIFY] is removed | Expert S-1 (must-fix); agency ≠ agent rule |
| A2 | The 1,206 / 1,196 record counts are cut from the chapter: eWeek states them without attribution, and they appear to come from the agent's own message. The Opening Case now says "records on business executives and companies". The case file keeps the counts, hedged | Expert S-2 (must-fix); fact-check C11 |
| A3 | The "ALL CAPS" line is tied only to the same remarks about the 4,000-record database ("in the same remarks … not to do this") | Expert S-3 |
| A4 | The freeze now reads: "By July 18 he had told the agent not to change anything without his permission". The F14.2 storyboard shows "Early July" and "By Jul 18" | Fact-check C09, C18; editor decision 6; expert S-19 |
| A5 | The screenshot attribution is split. The Register's hedge ("appear to show") covers "catastrophic error of judgment"; the empty-database detail is attributed to eWeek; "without permission" is cut | Fact-check C12 |
| A6 | Masad's full post was read through the fxtwitter mirror (build/ch14/src/masad_fx.json). The planning/chat-only mode is now attributed to Masad and Abdullahi as "being worked on". Hard gates are now "hard gates if enforced as announced". "In development" is explained as "working in the development setting" | Fact-check C48, C96, C143; expert S-9; panel (Daniel) |
| A7 | C11 gains a secondary tree label, **overconfidence (inferred)**: the agent's output stated with certainty that rollback was impossible, and the restore contradicted it. It is inferred because the screenshots only appear to be Replit output. The case file, F14.17, its long description and D-14.8 are updated to match | Editor decision 7; fact-check note |
| A8 | METR: the first version (March 2025) is named, with Claude 3.7 Sonnet at about 50 min (50%) and about 15 min (80%), "about four times shorter", and 4–6× across models. The result is dated "as of October 2026" (later versions show longer horizons). The tasks were mostly software tasks. METR is kept apart from Ch. 12's study | Expert S-4; fact-check C34, C35 |
| A9 | τ-bench is reframed as inconsistency across tries, not compounding over steps | Expert S-5 |
| A10 | Deep 14.B, the script and the meta file now state simplification (5), independent misses, and the abandon-after-five rule (<0.1% of runs). Core 14.4 gains the reason check points help ("an early error meets several checks…"), so Check Yourself 14.4 Q3 is answerable from Core | Expert S-6; pedagogy; panel |
| A11 | 14.1 now notes that chat tools run short agent loops inside one reply (as of October 2026). The R11 reading guide notes that its prompt chaining and gates are run by code | Expert S-7, S-8 |
| A12 | Hard gate redefined: "cannot run unless a person acts, or cannot run at all" (chapter and glossary row) | Expert S-9 |
| A13 | "Goal reached" is flagged as often the model's own claim, which is a claim to check | Expert S-10; brief rule on self-reports |
| A14 | Summary: "a log and a restore point told the truth" is replaced with the fact-checker's sentence. The Case Study now says "a log the user reads, not the agent's summary" | Fact-check C119 (unsupported); expert S-11 |
| A15 | Operator: dated February 2025, "(merged into ChatGPT's agent mode in July 2025)". "It depended on the agent invoking it" is marked as this book's reading. The Fowler reference is corrected to Feb 7, 2025, with the WaPo URL and the ADN reprint noted | Expert S-12; fact-check C49, C51, C133, C141 |
| A16 | The 93% figure: the classifier is glossed, and the text says it "reviews actions instead of the user, and … also misses some" | Expert S-13 |
| A17 | Chen et al. (short case 2): the label is changed to "closest branch hallucination, inferred", with the reason | Expert S-15 |
| A18 | "Every consequential action…"; the Summary now says "before every action that cannot be undone, especially when other people would bear an error" | Expert S-16, S-17; pedagogy |
| A19 | The Appendix E key for Case Study Question 5 now accepts either answer with reasoning | Expert S-18 |
| A20 | O4's UNESCO tag is corrected to "ethics of AI, Apply" | Fact-check C89 (unsupported) |
| A21 | Feng et al.: the quotation is corrected to "meaningless rubber stamping". Project Vend wording is corrected. Lucía's discount example now points to Chapter 4, and the false "company policy (Chapter 10)" is cut. Anthropic's "stopping conditions … are common". Lab 14.2 uses UTD's Copilot Chat facts (web access, no agents) | Fact-check C77, C102, C68, C69, C24, C91 |
| A22 | References fixed: Kwa et al. (19 authors, ellipsis, Chan; new title); Chen et al. (17 authors); Shavit et al. (Dec 14, 2023); OWASP Gen AI Security Project, *LLM06:2025 Excessive Agency*; AIID full title; Brewster & Chávez full title. All chapter [VERIFY] tags are resolved | Fact-check reference rows; expert S-20 |
| A23 | The book's own computations are renamed "this book's calculation" (p^n) and "this book's simulation" (gates) in the text, figure titles, alt text, scripts, long descriptions and handoff | Brief rule; panel (Daniel) |

## Decisions — learning design (pedagogy, student panel)

| # | Change | Why |
|---|---|---|
| P1 | **Workload made honest.** The count now includes the main Case Study, the end items (~18 min) and reading the A11 brief and rubric (~7 min; new brief rule). To fit, each trace card is a step-map row, done-criteria and the step estimate move into lab step 1, a "how I checked" column goes on the lab sheet, and Core is trimmed (~350 words). Total: **132 min ≈ 2.2 h**, stated identically in the chapter time line, the A11 brief, blueprint revision v2 and D-14.6. R11 is recommended everywhere ("about 800 words") | Pedagogy §1 (high); editor decision 1 |
| P2 | **A11 rubric repaired.** Proficient now reads "one or two minor flaws"; the log plan moves to "People points, permissions and log plan"; Dry-run record runs 1.5 / 1 / 0.5 / 0; Verification and revision has four levels, with the 0 rule stated below the table; Defense now covers "outside 100–120 words"; the Declaration can be scored for "no AI tools used" (Ch. 6 rule); "what the approver sees" is restored in O4, item 4 and the rubric; the text states whether a soft-only gate earns credit, and what points look like for a fixed workflow | Pedagogy (high); editor decision 2 |
| P3 | **A11/A13 boundary sentence** added to the brief, with a handoff decision for Chapter 19 (D-14.7). Alternative scenario 1 is replaced with a tutoring center's booking, because the old scenario leaked into the 14.9 faded sheet | Pedagogy; brief rule; editor decision 2 |
| P4 | **Complete short A11 sample printed in 14.9** (a hiking club newsletter: a fixed workflow with a hard gate, a check point and stop points). The 14.9 faded sheet now prints its facts. The Lab 14.2 sample trace and the no-partner route are printed in the chapter | Pedagogy; panel; brief rule (every example printed) |
| P5 | **Lab 14.1:** a 48-card deck dealt per team; a triad rule; a coin flip at soft gates (shows M3; hard gates always hold); an eight-card cap; a tick-box sheet with a swap cue; a lighter briefing (loop labeling dropped) | Pedagogy §2; editor decision 3 |
| P6 | **Review A rebuilt.** The key is the longest option only in A11. Distractors are hedged ("usually", "probably", "likely"), A9's lone hedge is gone, A11's absolute options are rewritten, and every distractor is tied to a named misconception (comment in the package). A8 and A9 are retagged Understand | Pedagogy (high); editor decision 4 |
| P7 | **Self-checking keys.** Appendix E (handoff) now holds keys for every Check Yourself item and faded example, plus the odd answers. The time line ends with the standard sentence | Brief rule; panel |
| P8 | **14.8 worked example** shows two recorded steps with named independent checks. The 14.2 worked trace labels passes 1 and 6 as plan, tool call and observation. The F14.5 title now reads "eight passes; the gate stops the eighth" | Pedagogy; panel |
| P9 | **Sam's thread reconciled.** 14.2 is "Sam's design after a test went wrong (section 14.5 tells that story)". 14.3 states the test data (20 runs; 152 of 160 passes right). The 14.1 pointer now reads "Sam routes any question about money to the treasurer (section 14.4 explains why)" | Panel; editor decision 8 |
| P10 | **Glosses and plain language.** Added: "bears an error" (who would suffer the cost), near miss, rubber stamp, vibe coding (everyday language), code freeze, classifier, DevOps. "Agency" is contrasted with its everyday and psychology meanings. Done-criteria and workflow blueprint are defined in Core (14.8). M6 is now stated in 14.6. The soft-gate wording addresses whether a soft gate is a gate ("Despite the name, it is a request") | Panel (Ayşe, Maya); pedagogy; editor decision 8 |
| P11 | **Faded examples supply the facts.** The 14.3 faded example gives the spreadsheet formula. The 14.7 faded example asks about both the line needing a check and the stop point (Daniel's reading of line 3) | Panel (Maya, Daniel); brief rule |
| P12 | Lab 14.3 now states the formula for a check that catches a share *c* and lists the simplifications (Deep 14.B shortcut) | Panel (Daniel) |

## Not changed (with reason)

- **METR's later horizons:** the expert's "above 16 hours" (METR's chart) is not used, because it was not verified for this text. The chapter says later versions report longer horizons, and the refresh row carries v4's ~110 min for o3 (fact-check C154).
- **τ-bench "newer models score higher":** not stated as a number. The text says results change quickly and points to the lasting lesson (no unverified figure).
- **Anthropic as corporate author of R11:** kept for consistency with Chapters 3, 5 and 6 (fact-check C130, optional).
- **Short case 2 (Chen et al.) stays an optional Deep box,** although Daniel wanted it in Core. Its job is gate design, and Core already carries the 93% figure and Shavit's point. Moving it would raise the week above the cap.
- **Culture-bound examples (eggs, church band, Toyota)** are kept: each is cited or is a fixed character detail. Ayşe's gloss requests are covered by P10.
- **Lab 14.1 pre-lab time (Ayşe: ~40 min):** with the estimate and done-criteria moved into class, the pre-lab is cards only (~13 min at the book's rate). ESL readers are told to expect longer.
- **Segregation of duties citation:** kept as a standard concept without a citation (fact-check C113). NIST SP 800-53 AC-5 is noted for the editor.
- **No model names behind Replit's agent** (provider neutrality; left for a book-wide decision).

## Waiting for the author

1. Live syllabus: R11 is recommended; the A11 wording (no AI tool required, three dry runs, photographed lab sheet, defense 100–120 words); LO6 for Thu Apr 8; the A11/A13 boundary.
2. Approval of the Kanban From the Field (not commercial).
3. The Tuesday Apr 6 demo: tool kind, model and a dated recording.
4. Final voice edit (pipeline step 8). The editor never marks a chapter done.

## Open items (not author)

- Fact-check C67 and C112: pointers to Chapters 17, 18 and 23, which are not drafted yet. Recheck at assembly.
- Fact-check C88: the Compass spreadsheet is not built yet (instructor package).

## Voice pass (Mode B, 2026-10-18)

A light pass using docs/voice/voice-profile.md rules 1–5:
- a "Let's take each system…" walkthrough opening (14.1 worked example);
- "In other words" restatements after the start-simple advice (14.1), the two-way independence caveat (14.3) and the restore-point paragraph (Case Study);
- concrete openings for 14.4 ("a draft, a cart, a customer or a bank account") and 14.6 (the full-access temptation);
- "For example" after the workflow and hard-gate definitions.

No facts, numbers, citations or figure references were changed by the voice pass. The author's final voice edit is still pending.

## Final review (2026-10-18) — applied

The final reviewer (Opus, independent) approved the chapter after 6 must-fixes and 13 should-fixes. All were applied with the reviewer's wording.

- **M1 (Signature 9).** `agent_loop(gate="soft")` now draws a hatched risk diamond labeled "Soft gate: an instruction (may be skipped)", with plain arrows. The legend adds "hatched = a soft gate" only when the gate is soft, and "dashed = may be skipped" is gone. The signature is unchanged. Docstring, D-14.1 and the longdesc are updated.
- **M2.** Dashes that did not mean inferred or reported are removed:
  - F14.1 (optional labs);
  - F14.3 note box;
  - F14.10 divider, arrow and box;
  - F14.15 planted fault.
- **F14.6.** The lines are now solid, told apart by marker shape and a direct label (S11).
- **M3.** F14.19 now marks the dash as "inferred: the authors' suggestion", in the figure and in its alt text.
- **M4.** Lab 14.2 now points to A11 item 4 for the log plan.
- **M5.** The F14.16 rows are renumbered to match the A11 brief.
- **M6.** The sample A11's step map now includes the president's approval gate and a never-touch line, and its reliability note reads "one AI step of six".
- **Should-fixes:**
  - S1: reading-rate wording in the time line.
  - S2: Anthropic sentence grammar.
  - S3: A1's key shortened so A11 is the only key that is the longest option.
  - S4: C11 ALL CAPS and "panicked" attributions.
  - S5: Spaced Review 1 key now reuses Ch. 12's data-class row.
  - S6: "more than five times" in Deep 14.B.
  - S7: OWASP and IT expanded; "CEO's" written out in the alt texts.
  - S8: Sharwood (2025b) is now cited in the Case Study.
  - S9: the Case Study Question 5 key is marked as this book's reading.
  - S10: Appendix E order now matches Ch. 12.
  - S12: the chapter-map second-highlight dash is left to the editor's design pass.
  - S13: D-14.6 states that there is no separate check-and-submit item.
- **Row caps.** Two sections exceed their individual caps, counted without Check Yourself: 14.1 at 684 words (cap 650) and 14.5 at 748 (cap 700). They are accepted because the Core total, 5,170 words, stays under 5,400.
