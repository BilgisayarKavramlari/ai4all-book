# Chapter 10 — developmental memo (2026-10-18)

Inputs: four independent reviews run in parallel without sharing reports (build/ch10/reviews/): subject-expert reviewer (Opus; 21 findings, 2 must-fix, 1 must-update), pedagogy reviewer (Opus; 4 must, 14 should, 7 consider), student-reader panel (Maya / Daniel / Ayşe, Sonnet), fact-checker (docs/factcheck/ch10.csv: 130 claims, 106 supported, 20 partly supported, 0 unsupported, 4 cannot verify; sources in docs/factcheck/ch10-sources.md). The author delegated editorial choices (D19); the editor settled conflicts in eight decisions (2026-10-18), and the chapter agent applied them in revision v2. Draft v1 is recoverable from the session; the blueprint v0.1 is archived at build/ch10/blueprint-v0.1.md.

## Decisions — accuracy (fact-checker, subject expert; editor decision 4)

| # | Change | Why |
|---|---|---|
| A1 | **Detector evidence dated and updated** (10.6, Summary key 3, F10.11): the 2023 results are kept with their limits; added that a 2024 study with exam-specific detectors reported no bias (Jiang et al., 2024, *Computers & Education* 217) and that as of 2026 some commercial detectors show near-zero false-positive rates in independent tests while others still fail (Jabarian & Imas, 2025, NBER w34223, verified via abstract and Booth Review); the reason a score is weak evidence is now variability ("accuracy varies by tool, kind of text and time; a single score cannot tell you how likely it is to be wrong about this writer"); F10.11 box: "its error rate for this writer and this text is unknown" | Expert #1, #18; fact-check C50; editor 4 |
| A2 | **Noy & Zhang wording aligned with Chapter 1** ("the study did not separately measure factual accuracy") and the 68% sentence corrected to the group average ("on average, the ChatGPT group's essays scored no higher than raw output") | Expert #2, #3; fact-check C32, C35 |
| A3 | **Deep 10.A mechanism and base rates:** "many detectors, especially early ones, score predictability; others are trained classifiers"; perplexity re-glossed without "surprised"; OpenAI's classifier described as weak (missed 74%) "on a challenge set of English texts"; a far better detector (90%/1%) shown for contrast; the lesson stated as the reviewer put it (share of wrong flags depends on how much writing is AI, which the reader of the score does not know); Weber-Wulff moved here; Vanderbilt's 2023 decision to disable one detector (about 750 of ~75,000 papers at a claimed 1% rate) added and verified on the university's page | Expert #4, #5, #19; pedagogy #21; editor 4 |
| A4 | **Peabody labels and sources:** Benbow quotation re-sourced to her statement (archived 2023-02-21) and Korn (CNN), with Lele (2023) kept for the date and step-back; her separate line on personal connection and empathy paraphrased and used to document the delegation failure; ChatGPT in February 2023 could not know the event (training text before 2022, no web search: book's reading, fact-check V09); tree label recorded as "a wrong detail; AI origin inferred"; F10.2 Feb 18 tagged "(confirmed: her statement)"; F10.13–14 notes updated | Expert #6, #7, #21; fact-check C18; editor 4 |
| A5 | **Moffatt paragraph:** para. 27 (responsible for all information), para. 28 (airline did not explain why customers should double-check one part of its site; the chatbot's answer linked to the correct page, paras. 16–17 per Ch. 4), para. 29 (no reason a customer should know which part was accurate); "The decision does not mention any AI label or describe the chatbot's technology"; Check Yourself 10.7 Q3 and R7 aligned to 27–29 | Expert #10; fact-check C56, C58; panel |
| A6 | **Agarwal et al. corrected** (both groups faster; Americans gained more per suggestion; Indian participants moved toward Western styles) | Fact-check C38 |
| A7 | **Kruger et al.:** "such as sarcasm", no percentages; read-aloud tip kept in the form the secondary source supports (a flat, neutral voice improved senders' judgments in one experiment; BPS Research Digest), not "opposite tone" | Fact-check C29; expert #9; editor 4 (kept, because a source supports the neutral-voice version; full-text confirmation logged as V04) |
| A8 | **Kirchenbauer, Sadasivan, Schilke & Reimann:** "a watermark helps only for text from models whose provider has added one"; "paraphrasing can weaken watermarks and several other kinds of detectors"; "being exposed by someone else cost even more trust than disclosing it yourself" (abstract-supported); the fade sentence unattributed; no participant count | Fact-check C64, C65, C79; expert #11 |
| A9 | **Matsuda:** the "overall effect, chosen deliberately or not" wording kept for Matsuda (2001); the reader-impression aspect attributed to Matsuda & Tardy (2007, *ESP* 26(2), abstract verified) | Expert #8; fact-check C24; editor 4 |
| A10 | **Liu et al. details:** the surprise explained in plain words (researchers expected the opposite); "in the same direction in every condition"; interviewees = ten computer-science students at one university | Expert #12; panel (Maya, Daniel) |
| A11 | **Şeker (2016) connection reworded:** "designed and centralized"; "the central control and worked-out principles the entry describes are what the Peabody message bypassed" | Fact-check C88 |
| A12 | **EDI office** = "whose work is the college's equity and inclusion efforts" | Fact-check C07; editor 4 |
| A13 | **References fixed:** Barrett URL; Jiang volume and DOI; Kirchenbauer PMLR pages and URL; Microsoft & LinkedIn title and date; NPR updated date; OpenAI page read in the archive; Perrotta update dates; Benbow (2023), Jabarian & Imas (2025), Matsuda & Tardy (2007), Vanderbilt University (2023) added; Lele & Faquih cited with the **exact published title** | Fact-check reference rows; editor 4 |
| A14 | **Case file C07:** Feb 14 message "carried no note about ChatGPT"; caption/alt-text dates explained; "about seven and a half weeks"; sources 5–6 resolved | Fact-check C122, C123, C127 |
| A15 | **Fig. 10.6** box: "lost nuances" instead of "fewer hedges" (no study measured hedges); Summary key 2 adds "(none tested grammar checkers)" | Expert #14, #15 |

## Decisions — learning design (pedagogy, student panel; editor decisions 1, 2, 3, 5, 6, 7)

| # | Change | Why |
|---|---|---|
| P1 | **Zone table limited to coursework** (editor 1): two columns (skill-building coursework / other coursework); position 5 in other coursework = "permitted with disclosure and verification, and only if you can explain every sentence and readers would accept it" (no weaker than position 4); "Outside coursework, the zones are not rules: verification always applies, and 10.7's three questions decide disclosure"; "A7 is that explicit permission"; Elif's row 3 relabeled "Not coursework: verified; 10.7's questions give no line"; B1 and B5 keys aligned | Pedagogy #1; panel (Ayşe); editor 1 |
| P2 | **Positions 2 and 3 defined** ("you write every change" vs. "you accept or reject the tool's wording"; "accepted as offered = position 3"); Elif's flyer row "3, grammar only"; A3 stem "accepts three of them as offered" | Panel (Maya, Ayşe); pedagogy #20; editor 6 |
| P3 | **Second-language support** (editor 5): instructor-ask script and what to do if the answer is no (10.2); translation back-check step (10.6) and a translation run in Lab 10.3; one Core sentence on why rewriting to avoid a flag proves nothing (10.6); "Unexpected Score" with hints for every step and a full model in Appendix E; stock-phrase list with the caveat that learned phrases are not wrong (10.4); v0/v2 language and gloss rule in 10.8 and the A7 brief; "plan on up to twice as long" in the time line | Panel (Ayşe top 1); pedagogy #12; editor 5 |
| P4 | **A7 reader-only route defined** (v1 = the tool's comments, coded; trace v0 → comment → v2) in 10.8, the brief, F10.9 and the rubric row; "with a reason" added to item 1; document capped at **300 words**; reflection may be a 2-minute recording; route (b) disclosure asks about acknowledging the person's help | Pedagogy #2, #9, #24; editor 2 |
| P5 | **Rubric levels by counting shortfalls** (one stated rule; Beginning covers "fewer than half coded" and "zero or one declaration element") | Pedagogy #9; editor 2 |
| P6 | **Midterm Bridge:** MB2 pointer → sections 2.3 and 2.5; MB5 replaced (business student, three market reports); MB1 key paraphrased; MB3 key shortened and a distractor lengthened; MB7 pointer 7.2 and 7.4; **retitled "Chapters 1 to 7"** with a line pointing to the Spaced Review and Case Study for Chapters 8–9 (chosen over adding an item, to keep the week's load); F10.17 and its table list every main and second highlight with one stated rule (Ch. 3, 4, 6, 8, 9 seconds added; Ch. 8 under Decide) | Pedagogy #3, #4, #5, #14, #17, #22; editor 3 |
| P7 | **Cross-chapter terms** (editor 6): 10.5 links "keep, rewrite or reject" to Chapter 1's Decide step ("keep, change or reject"); Elif's example re-tagged *voice*/*commitment* (Chapter 9 drift labels removed); "Signature 6" replaced by "the six parts of Chapter 5's anatomy of a prompt" in the chapter and labs; AI and the Verification Funnel glossed at first use in Core; Role vs. Context per Chapter 5 (the reader moves to Context in Elif's prompt; Check Yourself 10.3 Q2 asks for both); O1 verb → **Differentiate** (Understand) | Pedagogy #6, #7, #8, #15, #21; panel (Maya); editor 6 |
| P8 | **Assessment items** (editor 7): A1 (d) and A9 (c) replaced with misconception distractors (M2; M4 "polished with AI tools"); "any/every" absolutes removed (A3, A7); option lengths rebalanced (key longest in one item, A11; keys a2/b3/c2/d2 across Review A and Bridge MC items); Review B3 and B4 swapped so the detector case has a public answer; the club announcement printed in B4 (date moved off spring break); two more refund rows printed in 10.5; Check Yourself 10.6 Q3 asks "why"; faded answers in Appendix E | Pedagogy #10, #13, #14, #23; panel top 2; editor 7 |
| P9 | **One figure per subsection:** new F10.19 reader bands in 10.1 (`reader_bands`) | Pedagogy #18; editor 7 |
| P10 | **Draft markers:** every `[VERIFY]` removed from student-facing text (status in ch10.csv resolution_v2 and the handoff); `[COMPASS: …]` placeholders kept by the book-wide convention | Panel (across personas); editor 7 |
| P11 | **Ghostwriting moved to a short box** in 10.2; cover-letter table cut to seven rows; several long sentences split (Agarwal bullet, Moffatt paragraph) | Pedagogy #19; panel (Ayşe) |
| P12 | **Character consistency:** Elif already holds a scholarship (Ch. 3), so her paragraph is a summer research program statement (logged) | Pedagogy #25 |
| P13 | **One-page label summary** box in the Chapter Summary (positions, bands, codes, tags, questions, process evidence) replaces the "You can now" list | Panel (Ayşe top 4) |
| P14 | **Application essays:** one sentence in Career Connection (check each program's AI rules) | Panel (Daniel) |

## Workload (counted at 150 wpm from the v2 text)

| Item | Basis | Minutes |
|---|---|---|
| Core 10.1–10.7 (with examples, tables, Check Yourself) | 4,980 words | 33 |
| Whole Core package: Core + front block and objectives + Opening Case + 10.8 + Case Study + Summary and label box + Key Terms + Review A + Spaced Review + A7 brief and rubric (main route) | ≈ 9,000 words | 60 |
| R7 (paras. 27–29) + R8 (abstract and two figures) | guides | 8 |
| Your Turn 10.1–10.2 | done in Tuesday's concept check (final review M1) | 0 |
| Pre-lab: context card and v0 | ≥ 80 words or 6 bullets | 15 |
| A7 at home, per requirement (≤ 300-word document: ≤ 9 sentences left to annotate 8; three claims at 4 min each 12; v2 and trace 10; reflection 8; declaration with disclosure 7; assemble 3; rounded) | | 50 |
| **Total** | | **≈ 131 min ≈ 2.2 h** (rule: ≤ 2.2 h = 132 min) |

Not counted: the Lab 10.1 page (read in Thursday's briefing, in class), the alternative-assignment paragraph (read only by students who choose it), labs 10.2–10.3, Deep sections and the Midterm Bridge (used in week 8). After the final review (M1), the 10.1–10.2 Your Turn moved into Tuesday's concept check and the A7 fact check is counted at Chapter 8's rate (4 min per claim): about 131 minutes, stated in the chapter as about 2.2 hours. Second-language readers are told to plan on up to twice as long.

## Not changed (with reason)

| Item | Reason |
|---|---|
| Noy & Zhang "a/b" citation keys (expert #2) | Two different works are cited (the *Science* article and the working paper); Chapter 1 cites only the first, so its key needs no change |
| Expert #13 (post-training "house style" sentence) | Optional; adds a mechanism non-majors do not need; Chapter 3's one-sentence recall suffices |
| Expert #16 (SynthID-Text, Dathathri et al., 2024) | Not verified in this session; the watermark paragraph is Deep and now correctly scoped; candidate for the next edition's refresh |
| Expert #17 (61.3% vs. 61.22%) | The published text says 61.3% (fact-check); kept |
| Panel: a real, dated tool output beside Elif's constructed "after" paragraph (Daniel) | A real output would need a dated run and would age quickly; constructed outputs are labeled per the characters rule. Lab 10.3 gives each student a real, dated comparison of their own |
| Panel: move From the Field out of Core (Daniel) | From the Field is a fixed anatomy part (not Core); its link to the chapter is now stated more concretely (central control and principles; keep-or-rewrite questions) |
| Panel: remove `[COMPASS: …]` placeholders | Book-wide convention (chapter brief); replaced at production |
| Pedagogy #24: audio route for other written parts | Applied only to the reflection; the annotation and trace are inherently written records |
| Liang chart per detector | Per-detector values appear only in the paper's figure; F10.10 uses counts derived from the published percentages (unchanged) |

## Waiting for the author

1. **Course-policy reading** (D-10.2): the coursework table in 10.2, including grammar-only edits, translation of one's own text, position 5 in other coursework, and A7 as the explicit permission for co-drafting.
2. **Live syllabus:** R7/R8 guides; A7 brief (150–300 words); week stated as about 2.2 h; Tuesday's opening slot uses Peabody.
3. **From the Field:** the Social CRM entry, the D16 disclosure, and the page range (headers read 38–40; first page unnumbered).
4. **Library checks** if you wish: Matsuda (2001) p. 40; the *Science* version of Noy & Zhang (figure numbers; whether the 68% figure appears); Kruger et al. (2005) for the neutral-voice condition.
5. Optional first-person anecdote (never constructed) and the final voice edit.

## Voice pass (Mode B, 2026-10-18)

Light pass per voice-profile §10: sections already open with a concrete constraint (10.3, 10.6, 10.7); one "In other words" restatement added after the dense detector paragraph in 10.6; a "For example" added to the From the Field connection; register kept calm and non-hype; no humor, anecdote or opinion added. The author's final voice edit is pending.

## Final review (2026-10-18) — applied

All 7 must-fix and 12 should-fix items from build/ch10/reviews/final.md, with the reviewer's wording: workload recount (Your Turn 10.1–10.2 in Tuesday's class; A7 50 min; ≈ 131 min; handoff time statement fixed); faded 10.2 key (position 5); "links" not "stages" in the F10.13 long description; facts supplied in three faded examples (status update, refund reply, grant paragraph) with matching keys; Kruger sentence reworded to cover both secondary accounts (V04 open, Author-only 5) and V09 resolved as a marked reading; A3 stem and options set in coursework; paras. 16–17 for the chatbot link; Deloitte callback re-sourced (DEWR, 2025; DEWR, 2026, pp. 48, 147; McGuirk, 2025, as in Chapter 9); "its one wrong detail went out uncaught (reported)"; F10.18 "Differentiate" (re-rendered, color and gray); long-description paras. 27–29; Copilot Chat tool wording; Lab 10.3 "20–30 minutes"; "the parts you use" in Lab 10.1; B2 stem supplies the facts; "in its prompt or its paraphrase"; FAQ and LLM expanded; watermark glossary row sense-labeled "(text; Deep)". Nice-to-have applied: v1's full sentence printed in Faded 10.8. Left to the editor's book-wide design pass: gray legends that name colors; the dashed second-highlight convention in chapter maps; the *Moffatt* reference format across chapters.
