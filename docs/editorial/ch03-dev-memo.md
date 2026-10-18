# Chapter 3 — developmental memo (2026-10-18)

Inputs: four independent reviews run in parallel without sharing reports. These were a subject-expert reviewer (Opus; 18 findings: 2 High, 5 Medium, 11 Low), a pedagogy reviewer (Opus; 3 must-fix, 10 should-fix, 10 consider), a student-reader panel (Maya / Daniel / Ayşe; simulated personas) and a fact-checker (Sonnet). The fact-checker's results are in docs/factcheck/ch03.csv and ch03-sources.md: 100 claims, of which 76 supported, 17 partly supported, 1 unsupported and 6 cannot verify. The editor's 18 decisions settled conflicts between reviewers, and the chapter agent applied them in revision v2. The pre-review draft is kept in build/ch03/ch03-v1-prereview.qmd (scratch, not committed). Book-wide rules re-read before revising: docs/production/chapter-brief.md, "Book-wide rules added during production" (reading rate, agency ≠ agent, verdict scale, calibration, tree vs. chain, Failure Diary prompts, D20).

## Decisions — accuracy (fact-checker, subject expert)

| # | Change | Why |
|---|---|---|
| A1 | Opening Case and Case Study: "GPT-4 named the right parent in 79% of the mother and father questions, which gave 1,573 child–parent pairs"; "turned all 1,573 pairs around"; "even with up to ten tries per question, … only 33%"; Llama-1 models showed the same gap | Fact-check must-fix 1–2 (C11, C12, C22); expert #7, #12; editor decision 5 |
| A2 | The student-facing [VERIFY] on 33%/28% replaced by "The paper gives 33% in its text and 28% in a figure note; this book uses 33%"; case file and data/ch03_reversal.csv record footnote 11 and the Figure 5 note | Fact-check must-fix 2 (C13, C25); editor decision 5 |
| A3 | "three sets of 30" invented facts; "the largest GPT-3 model often completed the facts in the trained direction" (96.7% / 50.0% in the case file); "GPT-4 (2023)" without "later" and without a snapshot number | Fact-check C05, C07, C21, C23; expert #12 |
| A4 | The explanation is hedged everywhere as the authors' suggestion (Opening Case, 3.3, Case Study, Summary). One plain sentence explains why training is directional ("the model always scores what comes after the text before it"). The privacy-tuning factor is placed next to the observation that untuned Llama-1 models showed the same gap | Fact-check must-fix 3 (C27); expert #12; panel (Daniel); editor decision 5 |
| A5 | "A person who knows one direction usually knows the other" → "We tend to expect that anyone who can answer one direction can answer the other" | Fact-check C16 (cannot verify) |
| A6 | 3.1 cross-reference: "The Ethics Lens and Short case 2 return to…" (section 3.4 does not discuss languages) | Fact-check must-fix 4 (C41) |
| A7 | Deep 3.A rewritten for causal (decoder-only) attention: a token draws on the tokens **before it**; the link is formed at "big"/"small". F3.10 redrawn with arrows starting at "big"/"small" and pointing back to "trophy"/"suitcase". Levesque sentence quoted exactly ("The trophy doesn't fit in the brown suitcase because it's too big") | Expert High #1, #15; fact-check C63; editor decision 4 |
| A8 | Privacy caveat added to 3.3 and echoed in the Warm-up answer. Some providers may use conversations to train **future** versions, depending on account and options (as of 2026; details in Compass); this can change a later model, never the current one. Chapter 15 pointer added. Anthropic dates appear only in the refresh-list row, marked [VERIFY]; the chapter cites no provider | Expert High #2; editor decision 2 |
| A9 | Training stages updated. The chapter now gives Ouyang et al. (2022) as "the best-known recipe": a scoring model is trained on people's rankings. One sentence notes that newer recipes also use AI-generated examples and feedback (Bai et al., 2022, verified on arXiv). "usually" → "often". F3.5's human-feedback box updated | Expert #3; fact-check C52; editor decision 3 |
| A10 | Reasoning tokens: one sentence in 3.2 (made the same way; count toward context and cost; OpenAI, 2024, n.d.). Probe 1 records whether the tool showed a reasoning step. Deep 3.B adds one dated sentence on later training stages and reasoning tokens | Expert #4, #16; editor decision 3 |
| A11 | Memory wording: "saves notes about you, or draws on past chats". The corrected AI definition in 3.6 now says "the model itself keeps nothing between turns; the system resends the conversation, and a memory feature, if on, adds saved notes or passages from past chats" | Expert #6; editor decision 3 |
| A12 | Token splits depend on what precedes them. "İzmir" is 3 pieces at the start of a text and 2 after a space. "hydroxychloroquine" is 4 pieces after a space and 5 at the start or in quotation marks. data/ch03_token_pieces.csv now holds both cases | Expert #8; editor decision 14 |
| A13 | Short case 2 adds that ratios vary with the text (Petrov's FLORES 3× for Arabic vs. the book's UDHR measurement, 2.6×) | Expert #17; editor decision 14 |
| A14 | Cheng et al.: "from one data source to another" (not "topic to topic"). Toolformer: "a calculator, a calendar or a search engine; code interpreters work the same way". Kaplan: "some trends … each tenfold increase cut the error by about the same percentage". "Most of today's … (as of 2026)". Fu et al. called "a 2024 preprint". Pretraining described without "hides" | Fact-check C54, C59, C61, C65; expert #16, #18 |
| A15 | Context window = "the space for everything the model receives in one turn"; the response counts toward it; tool results and memory notes go into the same window. The closed-book score is explained ("answering from its training alone") | Expert #9; panel (Daniel) |
| A16 | Scores: "the scores are then turned into a probability distribution"; they reflect training text "and, after later training stages, what people rated as good". Temperature is offered by "many developer tools, and some apps" | Expert #10, #11 |
| A17 | From the Field rebuilt on the published article: Şeker & Nizam-Özoğur (2026), *Electrica* 26, Article 0033, doi:10.5152/electrica.2026.25033 (journal page and full-text PDF read). The 2024 manuscript is cited as its earlier version, and facts are limited to what both say. Details found only in the manuscript are attributed to "the earlier version": incorrect method signatures, libraries "not actually used", and the link to the context window. Figures: 30–40% less development time and about 30% fewer errors, with the article's own limitation (based on the developer's reflections). Co-author named; product not named in the text; D16 disclosure kept | Fact-check C70, C75; editor decision 17 |
| A18 | data/ch03_lost_middle.csv and the F3.6 source line cite arXiv:2307.03172v3, App. G.2, Table 6. References add URLs for Vaswani and Carlini, Bai et al. (2022, all 51 authors checked; APA 19 + last), OpenAI (2024) and OpenAI (n.d.). Cheng's proceedings title is reduced to what is printed | Fact-check reference fixes; expert #14 |
| A19 | Opening Case: "millions of people" → "many people" (Case Study context) | Fact-check C18 |
| A20 | "settings" is used only for learned values (said once in 3.3: Chapter 2's parameters). Temperature, search and memory toggles are "options" everywhere (3.2, 3.6, F3.3 subtitle, F3.8 footer, labs) | Expert #5; panel top-1; editor decision 1 |

## Decisions — learning design (pedagogy, student panel)

| # | Change | Why |
|---|---|---|
| P1 | The Case Study no longer shows Signature 5 labels to students. "What kind of failure?" describes the failure in plain words and points to Chapter 4. The tree label stays only in cases/C16 and the handoff. "Signature 4/5", "Failure label", "Primary branch", o200k/cl100k removed from student text ("a newer / an older tokenizer"; technical names kept in figure source lines) | Pedagogy must-fix 1; book-wide rule; panel; editor decision 6 |
| P2 | "Save one surprising probe result for your Failure Diary (Chapter 4)" added to the Lab 3.1 exit step, in the chapter and the lab file | Pedagogy must-fix 2; book-wide rule; editor decision 7 |
| P3 | Spaced Review: the answer is removed from item 1's stem. A pure Chapter 2 recall item is added (sample vs. population), making five items | Pedagogy must-fix 3, should-fix 4; Ch. 2 memo P6; editor decision 8 |
| P4 | 3.2 numbers the four steps (split, score, pick, add and repeat). F3.3 is renumbered to match (the scores box is unnumbered). Review A4, Check Yourself 3.2, the Summary and the coffee-shop worked example use the same steps | Pedagogy should-fix 10; panel (Maya); editor decision 10 |
| P5 | 3.6 changes. The faded box is partly filled: the first link and half of the temperature correction are done, and the remaining links are Chapter 3 → Chapter 2 pairs. The worked correction cites sections 3.3 and 3.4 plus a new-chat check instead of probe 3. A written version of the F3.8 record is added. The A2 split is restated (15 terms; ≥ 7 Ch. 2; ≥ 5 Ch. 3; one corrected AI definition for the whole A2), with "Bring your Part 1 draft to Thursday's lab" | Pedagogy should-fix 5, 6, 8, consider 22; panel (A2 ambiguities); editor decision 9 |
| P6 | F3.9 redrawn so that all four links are Chapter 3 → Chapter 2 pairs (pretraining–self-supervised learning, next-token prediction–label, cutoff–training data, context window–inference). New title: "Each new term attaches to a Chapter 2 term with a true sentence" | Panel; pedagogy consider 22; editor decision 9 |
| P7 | Application Assignment: the steps are split into per-term steps and whole-map steps. A "hardest link" sentences step is added and tied to the lab exit step. "Term pool" is glossed | Pedagogy should-fix 8; panel (Ayşe) |
| P8 | Hana's Step 4: "asks for a supporting quotation, then searches the document for it; a quotation that is not in the document counts as a miss" | Pedagogy should-fix 7; editor decision 11 |
| P9 | Lab 3.1: teams of three skip probe 2 (not probe 4). A 3-minute debrief slot is added. No-Compass steps for a fresh or temporary chat and switching memory off are added. Tuesday's demonstration is mentioned in the chapter's time paragraph. An optional reversal extension uses a less famous pair from a provided list. The lab file's expected observations and extra debrief questions are marked as instructor notes, and debrief Q3 no longer assumes a reversal probe. O3 is added to the lab's tags | Pedagogy should-fix 11, consider 18; panel; expert #13; editor decisions 5, 12 |
| P10 | Review A: distractors 1(c)(d), 3(b) and 9(a)(b)(d) rebuilt from M1, M2 and M4. A14 is replaced by an item on what the context window does **not** hold. A new A15 covers instruction tuning | Pedagogy should-fix 12–13; editor decision 13 |
| P11 | Time statement: Core sections about 25–30 minutes (3,894 prose words ≈ 26 min at 150 wpm). The whole Core package is about 45 minutes, and longer for readers whose first language is not English | Pedagogy consider 20; panel; book-wide reading rate; editor decision 15 |
| P12 | ESL wording: "packs suffixes", "bought a similar improvement", "draws", "jigsaw" (explained), GPA and "W" glossed, "Llama-1" introduced as "Meta's openly released Llama-1". "scores" = "chances" stated once. The twenty other tokens in the coffee example and the source of " Fox"/" Perk" are explained. AI4K12 is described as in Chapter 2 | Pedagogy consider 21; panel (Ayşe, Maya) |
| P13 | M6 gets an explicit refutation sentence at the start of 3.5. The worked and faded retrieval examples, the Your Turn and B3 use the book's five-verdict scale with a pointer to Chapter 8 | Pedagogy consider 16; book-wide verdict scale |
| P14 | Your Turn 3.2 now prepares the lab (two prompts to test in probe 2 or Lab 3.3) rather than repeating it. Lab 3.2 is a paragraph-length, two-tokenizer extension of the 3.1 Your Turn, including a start-of-text vs. after-a-space split | Pedagogy consider 17 |
| P15 | C3 and Discussion 1 retagged LO1 (LO5 is not in the objectives) | Pedagogy consider 19 |
| P16 | Core trimmed to stay within budget after the additions. One 3.2 paragraph that 3.3 now covers was cut, along with shorter Opening Case and 3.4 sentences. Prose word counts: 3.1 881, 3.2 780, 3.3 846, 3.4 646, 3.5 741; Opening Case + 3.1–3.5 = 4,345 (≤ 4,500) | Blueprint budget; caps on 3.2 and 3.5 (800) |
| P17 | `probe_record` now takes `rows=None` (a list of (label, text) pairs) so that Chapter 4 can reuse it for F4.7. The default rows are unchanged. The footer word changed from "settings" to "options" per decision 1 | Editor request |

## Not changed (with reason)

- **F1.4 reuse in 3.5** (pedagogy consider 15: redundant with F3.3d and the table). Kept, because the brief asked that F1.4 be reused with a new caption. It links the search-then-generate lane from Chapter 1 to the retrieval slot in Signature 4.
- **3.3 load** (pedagogy consider 14). The training stages are now two sentences, as suggested. "Memory" stays inline rather than in a separate note, because the privacy caveat (decision 2) belongs next to it.
- **Hana's county history and From the Field** (panel: less relevant to non-CS readers). Kept. Hana's example is the blueprint's arts/humanities field, and From the Field is a required anatomy part. The coffee-shop, scholarship and support-thread examples cover business and everyday contexts.
- **Greedy decoding can still vary** (expert #11, second half). Not added. The source (an industry blog, Sept 2025) was not verified, and the detail is beyond week 2.
- **Optional page numbers for Hoffmann and Ouyang** (fact-checker). Not added, because they come from citing papers rather than the proceedings pages.
- **[COMPASS: …] placeholders** (panel: raw tags). They stay until the Compass MVP, as in Chapters 1–2. The no-Compass steps students need are now in the text.
- **Lucía's one-paragraph faded example** stays, as the editor decided (decision 16).
- **Rubric gaps in the shared A2 rubric** (pedagogy should-fix 9). The editor closed them in Chapter 2; Chapter 3 has no rubric of its own.

## Voice pass (Mode B, 2026-10-18)

This was a light pass using voice-profile §10 rules 1–4:
- a breadth opening for 3.1 (long words across fields) and for 3.4 (a student's reading, an analyst's report);
- an "In other words" restatement in 3.5 ("search and tools change the input, not the machine");
- a "Let's take" walkthrough opening in Hana's worked example.

No facts, numbers, citations, headings or figure references changed in the voice pass. The author's final voice edit is still pending.

## Waiting for the author

1. **From the Field.** Approve citing the published *Electrica* article, which you co-authored with Hatice Nizam-Özoğur, with the 2024 manuscript as its earlier version. The questions are:
   - Does the D16 disclosure apply (is Kolay.ai an OptiWisdom product)?
   - May the text name your co-author?
   - May the product stay unnamed in the text although its name appears in the reference title?
   - Which article/page form should the reference use?
   - May the article's 30–40% and 30% figures be printed with its own caveat?
2. **Character detail:** Elif holds an international student scholarship with a GPA requirement.
3. **Final voice edit** (pipeline step 8). The editor never marks a chapter "done".
4. **Live syllabus:** R1 is recommended rather than required in week 2 (D18).

## Final review (applied, 2026-10-18)

The independent final review (build/ch03/reviews/final.md) found 2 must-fix, 14 should-fix and 7 nice-to-have items. All were applied, with the editor's decisions on S10, S11 and S14:

- **M1:** the Levesque et al. (2012) reference now has no page range and links to the AAAI KR 2012 paper page. No [VERIFY] remains in the chapter.
- **M2:** the handoff has a ninth section, "Instructor package", listing every promised asset with its due date (Jan 26 and Jan 28, 2027).
- **S1:** section 3.5 defines the five verdicts with Chapter 8's wording. The old forum post is now "unsupported for now", and the arithmetic claim is "supported for the arithmetic". The same changes are made in Appendix E B3 and the even answers.
- **S2:** the time statement now reads "about 50 minutes to read the whole Core package … plus time to answer them"; the handoff count matches.
- **S3:** "as of October 2026" is used throughout.
- **S4:** the comment about the untuned Llama-1 models is marked as the book's own inference.
- **S5:** the Deep 3.A rationale for causal attention is corrected.
- **S6:** F3.10's in-figure title states the finding (re-rendered in color and gray).
- **S7:** From the Field no longer uses an anthropomorphic verb.
- **S8:** the claim about gains since 2024 is attributed to OpenAI.
- **S9:** distractors A10(d) and A11(b) are lengthened and hedged so the key is no longer the longest option; the rationales are updated.
- **S10:** the F1.4 caption uses `@fig-1-4`, in the chapter, longdesc and Appendix E.
- **S11:** a "Changed definitions" row for memory is in the handoff; the editor syncs Chapter 6.
- **S12:** the chapter's definition of "probability distribution" now matches the glossary.
- **S13:** the case-index CSV row is correctly quoted.
- **S14:** the Long & Magerko tag is dropped from O1 because the paper could not be reached to confirm the theme name; the uncited reference is removed, and so is the matching tag in the Lab 3.1 file.
- **Nice to have:**
  - "at the start of a text" replaces "inside quotation marks";
  - the pool note now says why inference counts;
  - the repeated "the largest GPT-3 model" is replaced with "it";
  - the "it's" link is marked "not shown";
  - the C16 privacy note now says the book names neither the celebrity nor the parent;
  - Lucía's thread is about an account email address, not a delivery address;
  - Elif's "thinks in Turkish" is logged in the characters rows.

Script note: the editor asked for a duplicated `summary_card`, `FIGS` and main block to be removed from figures/scripts/ch03_figures.py. The current file has only one copy of each (checked with grep), so nothing was removed. All renders were regenerated from that single copy. All 16 captions and alt texts are identical in the chapter and figures/longdesc/ch03.md.
