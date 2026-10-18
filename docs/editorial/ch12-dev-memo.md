# Chapter 12 — developmental memo (2026-10-18)

Inputs: four independent reviews run in parallel without sharing reports — subject-expert reviewer (Opus; 1 must, 19 should, 5 consider), pedagogy reviewer (Opus; 3 must, 13 should, 3 consider), student-reader panel (Maya / Daniel / Ayşe, Sonnet), fact-checker (Sonnet; docs/factcheck/ch12.csv, 90 claims: 65 supported, 20 partly supported, 1 unsupported, 3 cannot verify, 1 outdated; `resolution_v2` added to every row and 9 rows added for claims new in revision). The editor's eleven decisions of 2026-10-18 were applied as given. Draft v1 is kept in build/ch12/v1/.

## Decisions — accuracy (fact-checker, subject expert)

| # | Change | Why |
|---|---|---|
| A1 | "Skill with a tool does not move its frontier" → **"A prompting overview did not move this tool's frontier on this task"**, with the 10%-significance caveat and the one-task, one-model limit beside it, in the Opening, 12.1, the Summary, Review A2 and Check Yourself 12.1 Q2; "training made them better users" → "the overview raised scores and copying inside the frontier"; a sentence that prompting is part of fit and might change the result (only a test shows it) | Expert must-fix #1–2; fact-check C07; panel (Maya, Daniel); editor decision 1 |
| A2 | Case Study "Limits, as the authors state them" → "this book's reading of the design the authors report" (chapter and C09) | Expert #3; C17 |
| A3 | Tree label accepts either leaf ("contradicts its input or source" or "wrong calculation or reasoning"), inferred; F12.18 tag updated; Case Q3 key accepts both with reasons | Expert #4; editor decision 1 |
| A4 | "The trap": the authors expected AI prompted with the instructions, the data **and the interviews** to reach the contrasting answer; Case Question 1 replaced; even answers rechecked | C11, C12 (unsupported); editor decision 1 |
| A5 | 19 points vs. 19%: replacement paragraph (19 points from 84% ≈ 23% relative drop) | C19; editor decision 1 |
| A6 | Chen et al.: "think step by step" prompt, the authors' behavior-change reading, 51% ≈ guessing, dated version labels; F12.14 labeled "50% = guessing"; one narrow task not generalized | Expert #5; C46; panel (Daniel) |
| A7 | Fair bake-off: fresh chats **with memory and standing instructions off**; both terms defined in 12.6's Core text (Ch. 6 is Deep) | Expert #6; editor decision 11 |
| A8 | Peng: 95 recruited, 70 finished, plausible range 21%–89%; "was the tool given at random?" added to the five questions | Expert #7, #21 |
| A9 | Deep 12.B: Cui et al. named GitHub Copilot, 2022–23, pull requests, the parent company among the firms (HTML-comment VERIFY for the published text); Humlum labor paper retitled "Still Waters, Rapid Currents" (2026) with the 2% bound; LMArena's May 9, 2025 response | Expert #8, #10, #16; C49, C51, C53 |
| A10 | Ethics Lens: Danish survey fielded Nov 2023–Jan 2024; "in the same occupation" | Expert #9; C61 |
| A11 | Closed models "used only through a service, its developer's or a partner's; whose terms cover you depends on who runs the tool" | Expert #11 |
| A12 | Open-weight examples filled: Meta Llama 3.1 (Jul 23, 2024), OpenAI gpt-oss (Aug 5, 2025); OSI 1.0 dated Oct 28, 2024, "information about the data, not necessarily the data itself", "substantially equivalent"; "cannot fully see or rebuild" | Expert #12, #13, #24; C26, C47, C48 |
| A13 | Short case 2 made symmetric: OpenAI (2026, Jan 29) confirmed as primary; API exit Jan 14, 2027 (announced Oct 14, 2026) "as of October 2026"; Anthropic "Claude Opus 3"; Bastian dropped | Expert #14; C58 (outdated), C60; editor decision 9 |
| A14 | Short case 1: vendor responses at the reported tier (Ambrogi, 2024; Magesh et al., 2025), and "a tool used outside its intended scope is a fit question too" | Expert #15; C56 |
| A15 | From the Field: "late 1990s and early 2000s"; the lens adds that the vendor's own tests are not the customer's independent check and that each central update is a re-test trigger for the business | Expert #17; C64 |
| A16 | R10 cited as the QJE 2025 version everywhere (38% confirmed there; section VI.A); "about 1,600 with the tool" (WP count, check in QJE) | Expert #19; C31, C32 |
| A17 | Randazzo et al. per the authors' summaries: 244 consultants; about 60% cyborgs, 27% self-automators, 14% centaurs; centaurs most accurate (reported; Candelon et al., 2026 added); F12.17 shows the shares | Expert #20; C15, C86; editor decision 9 |
| A18 | OpenAI data terms replaced with the fact-checker's sentence (feedback exception; business, education and API services); Anthropic "new or resumed chats"; Microsoft unchanged | C41, C84; expert #23 |
| A19 | References fixed: Anthropic title, Becker "Barnes, B.", Brynjolfsson QJE, Humlum (two papers, new title), Magesh 22(2), Singh NeurIPS 2025, OSI date, OpenAI items; added Ambrogi, Candelon, LMArena, Meta, OpenAI 2026 and n.d.-a/-b/-c, UTDBP3096 | Fact-check reference fixes; C90 |
| A20 | METR "snapshot" (the book's word) → "caution against generalizing beyond early-2025 tools in this setting" | C37 |
| A21 | Mild absolutes softened ("cannot settle", "often where", "cannot fully see or rebuild"); "hardware you or your institution control" in F12.5 | Expert #24–25 |

## Decisions — learning design (pedagogy, student panel)

| # | Change | Why |
|---|---|---|
| P1 | Opening retitled "A Study You Met in Chapter 1"; R9 conditional ("If you read R9, recommended in Chapter 11…"); the chapter is fully understandable without R9; Case Study no longer assumes it | Pedagogy must #1; brief rule (recommended readings never assumed); editor decision 2 |
| P2 | **Data classes aligned with UTD's policy** (UTDBP3096: Public, Controlled, Confidential Data, verified 2026-10-18); a data-class → terms table (consumer / institutional) marked as the book's reading of course guidance; FERPA and HIPAA each glossed in one plain clause; the Worked Example contradiction resolved (no personal data about others in consumer tools; institutional only if the part needs it; Sam uses placeholders); F12.9 updated. Table offered to Chapter 15 verbatim (handoff D-12.8) | Panel top 2; pedagogy #5; C44; editor decision 3 |
| P3 | Matrix made teachable: four fit decisions and the rung levels as short lists (floor, automation, augmentation, agency); every cell = decision · rung · reason, matching F12.12 (`fit_matrix` gains `note` and `once`); Chapter 11's sensitivity check in its own sense (change one choice); "predicted" only for untested cells, "tested once" for single runs; floor, rung, lead and edge input glossed | Pedagogy #6–7; panel top 4; editor decision 4 |
| P4 | Second worked bake-off on a judgment task (marketing caption) with checkable criteria and **polish anchors 1 rough · 3 usable after edits · 5 ready to send**; Sam's engineering example simplified to one unit conversion (41 oz-in ≈ 0.29 N·m, the same motor as his Chapter 4 diary entry) with stall torque and datasheet glossed | Panel top 1; pedagogy #17–18; editor decision 5 |
| P5 | Faded examples 12.3, 12.4, 12.6, 12.7 (and 12.1, 12.5, 12.8, 12.9) now supply every fact the next step needs; 12.9 prints the first rows of the partly filled sheet (a biology abstract) | Pedagogy #4, #16; panel top 3; brief rule; editor decision 5 |
| P6 | Check Yourself: one application item per box where possible; "Check Yourself: Short Answers" block added after the Summary for self-checking; CY 12.3 Q2 names "the two coding studies" among three; CY 12.9 added | Panel; pedagogy #16; editor decision 5 |
| P7 | Career Connection rows added for marketing, psychology and biology; IT expanded | Panel; editor decision 5 |
| P8 | Review A rewritten: no absolute distractors; A8 no longer cues "data gate"; new scenarios replace Check Yourself repeats; A3 domain-tool item and A10 lock-in item added; A11 tagged Understand; keys rotate a2 b2 c2 d2; the correct option is the longest in two items (A3, A8); items 5, 7, 10, 13 marked optional practice | Pedagogy #8–9; brief MC rules; editor decision 6 |
| P9 | Review B: B1 moved to a museum and asks for the two differences that matter most (Differentiate); pronouns varied (he, they); C1 makes the Ethics Lens optional support; CSQ5 marked optional | Pedagogy #14, #19 |
| P10 | **A10 rewritten:** three routes (two tools; one tool and no AI; provided outputs, using the provided task in every column), all able to earn full marks; 6 runs; edge repeat optional; baseline estimated; polish anchors; five Declaration elements listed; count-based levels; "Matrix and trigger (1)" and "Judgment and declaration (1)" split; a gate-breaking decision caps "Cost and data gate" at 0.5; alternative assignment = Route C with own no-AI column | Pedagogy must #3, #10; panel top 5; editor decision 7 |
| P11 | **Workload recounted per requirement (D-12.9, final):** Core 36 min; whole Core package 48 min (the Case Study read together in Tuesday's class); required Review A items 1, 2, 3, 6, 8, 11 and Spaced 1–2 ≈ 10 min; pre-lab 13 min; A10 after the lab 60 min including its brief and rubric; total ≈ 131 min (2.2 h). The v2 figure of 132 min undercounted (final review M2); see the final-review section below. Cuts that made it fit: Core prose tightened (~600 words), Sam's tool table shortened, the data-terms box condensed, Summary's "You can now" list folded, Review A items 5/7/10/13 optional, A10 edge repeat optional and baseline estimated, judgment 100–120 words | Pedagogy must #2; editor decision 8 |
| P12 | Glosses at first use: system prompt, temperature, token, license, free tier, jigsaw, centaur, cyborg, stall torque, datasheet, edge input, floor, rung, lead; independent check and automation bias in their Chapters 8 and 11 wording verbatim; "the task the tool could not do" → "the task outside the tool's frontier"; "It's free is the most common reason" → "a common reason" | Pedagogy #11–13, #15; panel |
| P13 | Spaced Review checked against the written Chapters 10 and 11; item 2 asks for Chapter 11's three proxy questions (Analyze); stale "re-check" notes removed | Pedagogy checks |
| P14 | Visible [VERIFY] and [COMPASS: …] markers removed from student-facing text; Compass appears only as "In Compass (optional) and on eLearning: …" notes; the one open check sits in an HTML comment | Panel cross-cutting #1; editor decision 10 |
| P15 | Lab 12.1: routes, polish anchors, fresh chats with memory off, edge input may finish at home, jigsaw glossed; Lab 12.2: honest time (20 min with cards, up to an hour with full pages); Lab 12.3: two runs per input | Pedagogy #17; panel |
| P16 | "Stage" → "link" for the failure-to-harm chain (chapter, F12.19, C09, handoff) | Brief rule (links vs. stages) |

## Not changed (with reason)

- **D16 disclosure ("I am a founder of OptiWisdom…")** kept word for word although the fact-check notes "founder" is not in the entry: it is the approved D14/D16 disclosure wording, not a claim from the entry. Compass disclosure is handled once in the front matter (editor decision 10), so the expert's option to add Compass to the line (#18) was not taken.
- **Kwa et al. (2025), METR time horizons** (expert #22, consider): not added; it would need careful caveats and the week is at its cap.
- **OpenAI court preservation order** (expert #23, optional): not added; Chapter 15 owns retention risks.
- **"Snapshot"-style paraphrases elsewhere** are attributed as the book's reading.
- **Optional 10%-level note on quality among wrong answers** (C06): not added; the chapter's point (quality rose while correctness fell) stands on the main tables.
- **Chapter 6 (Deep) pointer** for a full prompt library dropped from 12.8; the two Chapter 6 terms used (standing instructions, memory) are defined in 12.6's Core text.
- **Eight Core sections** kept (the anatomy's maximum); each holds one owned topic.

## Waiting for the author

1. Live syllabus: R10 recommended; the Materials line naming CometAI; A10 routes; week ≈ 2.2 h.
2. Approval of the OptiScorer From the Field (commercial), framed as a 2020 vendor argument.
3. Confirmation of the §12.5 data-class table as course guidance (extends D15).
4. Library access to the *Organization Science* full text and Randazzo et al. (2025).
5. Guest practitioner (Tue Mar 30): whether to mention the session.
6. Final voice edit (pipeline step 8) — the editor never marks a chapter "done".

## Voice pass (Mode B, 2026-10-18)

Light pass with docs/voice/voice-profile.md rules 1–4: "In other words" restatements after the verification-cost paragraph (12.4) and the drift evidence (12.8); a "Let's take…" opening for the caption bake-off (12.6); breadth opening kept in 12.2; calm, sourced register throughout. No facts, numbers, citations, headings or figure references changed by the voice pass. The author's final voice edit is still pending.

## Final review (2026-10-18) — applied

The final reviewer (Opus, independent) found 5 must-fix and 11 should-fix items; all applied with the reviewer's wording, plus the editor's decisions (a)–(f).

- **M1:** Check Yourself keys (each with its §) and faded-example keys moved into the handoff Appendix E block; the in-chapter key block removed; the standard Appendix E sentence added to the chapter's time paragraph.
- **M2 / editor (a):** one honest number everywhere (chapter time paragraph, blueprint, D-12.9, P11): **about 131 minutes (2.2 h)**: Core 36; package 48 (Case Study read together in Tuesday's class, as in Ch. 11); required Review A items 1, 2, 3, 6, 8, 11 and Spaced 1–2 ≈ 10; pre-lab 13; A10 after the lab 60 including about 7 to read its brief and rubric. Review A items 4, 9, 12 and Spaced 3–4 made optional; A10 judgment 80–100 words. "Case Study in Tuesday's class" is an Author-only live-syllabus item.
- **M3 / editor (b):** Core body recounted at **5,392 words** after the reviewer's ten cuts and three small extra trims (12.3 "The lesson is not…", 12.7 trigger clause, 12.8 retirement clause).
- **M4 / editor (c):** the data-class note under the §12.5 table and in D-12.8, verbatim.
- **M5:** rubric "all five elements".
- **S1–S11:** privacy wording in the labs, chapter and A10; Sam's matrix cells (Tool B blocked for the contact list, not tested with placeholders; No AI marked predicted); Agency in the glossary sense; faded 12.2 terms fact; memory's last clause; glosses (underlying models, homogenization, hallucination, the tree and the chain); fact-check rows C45, C92, C94, C97; figure text (F12.7 "Results for early-2025 tools in this setting", "confidence interval"; F12.10 "working paper, Figure 8"; F12.2/F12.10 "Harvard Business School"); handoff F12.17 row and A9 (d); APA first citation "(The University of Texas at Dallas, Office of Information Technology [OIT], n.d.-a)", then "(OIT, n.d.-b)"; From the Field "nearly every project was coded from scratch", "three periods", and "my company built" removed (not in the entry; Author-only item 2).
- **Editor (f):** no [VERIFY] left in the chapter; C97 closed against the open February 2025 draft of Cui et al.; C94 stays on the handoff open list.
- Figures F12.2, F12.7, F12.10 and F12.16 re-rendered in color and gray and checked visually.
