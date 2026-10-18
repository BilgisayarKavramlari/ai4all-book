# Chapter 9 — developmental memo (2026-10-18)

Inputs: four independent reviews run in parallel without sharing reports — subject-expert reviewer (build/ch09/reviews/subject-expert.md, 25 rows), pedagogy reviewer (pedagogy.md, 16 rows + workload appendix), student-reader panel (student-panel.md, Maya / Daniel / Ayşe), fact-checker (fact-check.md; docs/factcheck/ch09.csv, 108 claims: 81 supported, 23 partly supported, 0 unsupported, 4 cannot verify; source log ch09-sources.md). The editor settled conflicts in seven decisions (message of 2026-10-18), applied here. Draft v1 is kept in build/ch09/ch09-draft-v1.qmd; the v1 fact-check CSV in build/ch09/ch09-factcheck-v1.csv.

Result: chapters/09 draft v2. Core 5,297 words (cap 5,300; about 35 minutes at 150 wpm); whole Core package about 7,575 words (about 50 minutes); chapter 12,540 words without references. Week 6 counted per requirement: about 2.2 hours (below). All 29 chapter [VERIFY] tags and the case file's tags are resolved; no [VERIFY] remains in reader-facing text.

## Decisions — accuracy (fact-checker, subject expert; editor decision 4)

| # | Change | Why |
|---|---|---|
| A1 | Opening Case rebuilt in tiers with primary records: contract A$439,142 (AusTender CN4118426); cover dated July 4, published August 14, 2025; first media report *Australian Financial Review*, August 22, 2025 (Karp); final installment A$97,587.11 repaid October 8, 2025 (Senate Hansard); page count removed | Fact-check CV-1–CV-4, V11; expert #13; blueprint rule against a page count |
| A2 | AI disclosure narrowed to the report's own words: a tool chain (Azure OpenAI GPT-4o), licensed by the department and hosted on its Azure tenancy, used in the technical workstream's traceability check (pp. 48, 147); none in the July version; AP's "used in writing the report" attributed as a summary | Fact-check V01, C12; expert #21 |
| A3 | Rudge's certainty hedged as he said it ("either invented by AI or the best-kept secret in his field"); "tokens of legitimacy" glossed; Rudge's check called "going outside the report", not lateral reading | Fact-check C26; expert #8; editor decision 2; panel (Ayşe) |
| A4 | Misquotation described as a passage attributed to a judge in *Amato v Commonwealth* that the reporting said was made up; corrected report describes consent orders; no "failure 3" number assigned | Fact-check C61, C107 |
| A5 | "Advisory, not an audit under AUASB standards" from the report's p. 2; "assurance review" attributed to the department; Deloitte "did not answer AP's question" about AI and the errors | Fact-check V10, C55, C59 |
| A6 | February 2026 update described from the PDF comparison (footnote citations to one book, not findings); three versions named with cover and publication dates; Case Study Q3 key: publisher settles the publication date, cover settles the report's date | Fact-check CV-5, C63; expert #13; panel (Ayşe: Q3 now answerable from the text) |
| A7 | Smith (2006) wording corrected ("flawed process with little evidence that it works ... no obvious alternative"); peer review "is meant to filter" | Expert #3; fact-check C19 |
| A8 | Peters & Chin-Yee: "nearly five times the odds" (vs. *NEJM Journal Watch*); "newer models tended to overgeneralize more (as of 2025)"; F9.9 title "most models … more often than the abstracts did" with the Claude caveat in the source line; Deep 9.B "76% lower odds (odds ratio about 0.24)"; explanations as hypotheses | Expert #4, #6, #7; fact-check C34, C39 |
| A9 | Tow Center: identifying where an excerpt came from; excerpts chosen from Google's top three; one run per tool; "error rates ranged from 37% to 94%" without best/worst labels; F9.12 source line revised; hedging glossed | Expert #9; fact-check C44, C45 |
| A10 | Maynez: 70% includes the human-written reference summaries; ROUGE/BERTScore compare with a reference summary; entailment measures tracked faithfulness better | Expert #10 |
| A11 | GRADE: four levels and start high/low cited to Balshem et al. (2011); five downgrading factors in Guyatt (2008) wording; upgrading mainly for observational evidence, three reasons; "quality" vs. "certainty"; F9.16 redrawn (upgrade arrow from observational studies only) | Expert #11; fact-check V09 |
| A12 | Wineburg & McGrew: "small think-aloud study"; "after a quick scan, often within about half a minute"; SIFT per Caulfield's wording (move 4: "claims, quotes and media to the original context") | Expert #18, #20; fact-check V03, V04, C23, C25 |
| A13 | Goldfish trace: Microsoft Canada consumer survey (2,000 Canadians; 112 brain-activity measurements); hop 4 per Maybin; F9.7 text and alt updated | Fact-check V05, C28, C29 |
| A14 | LK-99 (ordinary pressure; replication by mid-August; Garisto 2023a, 2023b); MLA description-of-output wording; EBU/BBC per the report (led jointly; >2,700 answers; four assistants; "significant sourcing problem" with the report's definition); deep-research announcement dates (Google, OpenAI, Perplexity) with references | Fact-check V02, V07, V08, V12; expert #16, #19 |
| A15 | Reardon short case: shorter wording (removed "150,000 views" and "told *Nature*", which could not be verified); "the lead author disputed the concerns" | Fact-check C65 (cannot verify); editor decision 4 |
| A16 | References fixed: AP → McGuirk (2025); CFO Dive → Alexis (2025) (case file only); Crossref → Hendricks (2023); EBU → Fletcher & Verckist (2025); DOIs added (Breakstone, McGrew, Ho & Bodoff, Wakeling); Caulfield, Maybin, BLS, MLA, Reardon issue; "Retrieved October 18, 2026" on changing pages; Balshem (2011), Garisto (2023a), Google/OpenAI/Perplexity, Karp, AusTender and Hansard added | Fact-check V13–V29, C79, C82, C83 |
| A17 | "M7" removed from student text; APA example dated (2027, February 23); From the Field's Petty & Cacioppo sentence marked "(The book's note …)"; "temperature option", never "setting" | Expert #5, #17; fact-check #9; brief (Chapter 3 terminology) |
| A18 | F9.20 note 3 "public criticism (reported)" instead of "lost trust"; rungs 1–2 "rarely enough" added to the funnel bracket and 9.8 | Expert #22, #23 |

## Decisions — learning design (pedagogy, student panel; editor decisions 1, 2, 3, 5, 6)

| # | Change | Why |
|---|---|---|
| P1 | **Source ladder redefined by the source alone** (editor decision 1): 4 = record of this claim (systematic review for "what studies show"); 3 = cites the specific record or records a narrower part; 2 = too vague to find; 1 = no source. Two rules printed in 9.1 and on F9.8b. Every placement recoded: Elif's five items, the supplement site (rung 1 by the citation rule), the 9.6 report, Elif's 9.8 row, A7, all answers. A "rung needed" table added (discussion, essay, number or quotation, decision with stakes) | Expert #1, #2; pedagogy #1; panel (all three) |
| P2 | **Lateral reading feeds the use decision** (editor decision 2): one rule in 9.3 ("rely on it" needs both); gray literature and "who paid" moved to 9.3 (9.1 trimmed); Lab 9.1 step 2 opens the source first, step 5 asks for a changed use decision; Elif's outside-source log uses sources about the newspaper; new Check Yourself 9.3 Q3 and Review A15 | Pedagogy #2, #13 |
| P3 | **Workload per requirement** (editor decision 3): Your Turns of 9.1, 9.2, 9.3, 9.6, 9.7 are A6 items; A6 cut to **three sources**, four outside-source lookups, judgment 100–150 words; Lab 8.2 may supply up to two sources; pre-lab names the summarized source as one of the three; time line states both numbers and "about 15 minutes before the lab and about 65 after it". Count below | Pedagogy #3, #11; panel (A6 "2.5 hours") |
| P4 | Review A rebuilt: 15 items, MC keys rotated 1a · 3d · 5b · 7c · 9a · 11d · 13b · 15c; options parallel in length and hedging (key longest in 0 items); absolutes removed; each distractor tagged to M1–M7 in Appendix E; new O5 MC item (13) and use-decision item (15) | Pedagogy #4, #14; brief MC rules |
| P5 | Faded examples completable from the book with the first step modeled fully: 9.5 (claims and sentences inline, step 1 coded with verdict and drift), 9.6 (claim and four citations inline), 9.8 (constructed source and claim), 9.1, 9.2, 9.3, 9.4, 9.7 (numbered steps, first done); Review B4 inline. Self-check answers for all faded examples in Appendix E | Pedagogy #5, #9; panel (Daniel, Maya) |
| P6 | 9.5 worked example: design stated (survey, not assigned); sentences coded supported / partly supported + broadened / unsupported + cause from correlation, with why not "contradicted"; corrected sentences keep the limits; prediction prompt added before the evidence | Expert #12; pedagogy #6; panel (Daniel) |
| P7 | Verdicts and drift types separated: drift named only when the verdict is not "supported" and one of the four fits; "added content" and "contradiction" dropped as drift types (the verdicts cover them); "omitted key result" checked for the whole summary; Chapter 8 v2's "unsupported" and "cannot verify" meanings copied verbatim | Pedagogy #15, #16; panel (Maya, Ayşe); editor decision 5 |
| P8 | A6 rubric by counts, gapless: outside sources 4 / 3 / 1–2 / 0; verdicts one / two–three / most inaccurate; trace by hops checked; last criterion renamed "References, declaration and judgment", Beginning uses "or"; alternative reading for press releases (release and study with dates) | Pedagogy #7 |
| P9 | Elif's declaration shows all five elements; 9.7 Check Yourself Q3 answerable (reason added: the reader can judge only if they know what the tools did) | Pedagogy #8; panel (Maya) |
| P10 | 9.4 Your Turn added (Lab 9.1 step 4); two 9.8 Check Yourself items; F9.3 cited and placed in 9.1; F9.4 moved to open 9.4; "You can now" list dropped (the card F9.18 carries it) | Pedagogy #9, #12, #14 |
| P11 | Glossing and ESL: abstract, open access, token, context window, hedging, white paper, correlation, Compass, caveat, consent orders, systematic review, meta-analysis, think-aloud; AI, APA, IT, BBC, EBU, LLM, DOI, WHO, GRADE expanded; "installment", "full credit", "English translation or explanation"; Marcus's friend replaces the bandmate; Your Turns no longer ask for "last week / this term" sources | Pedagogy #10; panel (Ayşe, Maya); editor decision 6 |
| P12 | Field rotation kept (psychology, nursing, history, natural science, business, public policy, engineering, art history, marketing in Discussion 3); a primary-source sentence for non-science fields (annual report, survey dataset, interview transcript) | Panel (Maya) |
| P13 | Mode B voice pass (light): "Let's place / follow / trace" in worked examples; "In other words" after peer review and GRADE; sections open with a concrete constraint (9.1, 9.3); no anecdotes added | voice-profile §10 |

## Week 6 workload, counted per requirement (150 wpm; longer if English is not your first language)

| Item | Basis | Minutes |
|---|---|---|
| Core sections 9.1–9.7 | 5,297 words | 35 |
| Rest of the Core package: Opening Case, Warm-up, 9.8, Case Study, Summary | ~2,280 words | 15 (50 in all) |
| Your Turns | all are A6 items | 0 extra |
| Before the lab: question, purpose, claim (3); find two sources, or take them from Lab 8.2 (7); run and record the summary (5) | — | 15 |
| A6 after the lab: third source (5); open each source and locate the claim (3 × 2.5); outside-source log (4 lookups × 3); type, status, two rungs, use decision (3 × 3); finish the summary check and corrected summary (8); trace write-up (5); references (4 × 1.5); judgment 100–150 words (8); declaration (4) | — | ~65 |
| **Total** | | **~130 min ≈ 2.2 h** (brief limit 2.2 h; syllabus 1–2 h) |

## Not changed (with reason)

- **Opening Case kept in the AP's quotation "tokens of legitimacy"** (one quotation under 15 words, now glossed): it carries the Ethics Lens point.
- **F9.4 stays a separate figure from F9.7** (pedagogy #15 suggested an instance relation): both are drawn by the same `hop_chain()` function, F9.4 shows the general path and F9.7 one trace; 9.2 refers forward to it.
- **[COMPASS: …] placeholders** stay (book convention until the Compass MVP); Compass is now glossed at first use.
- **Deep 9.A keeps GRADE** although Daniel wanted it in Core: Core is at its cap, and the ladder/strength distinction is stated in Core (9.1).
- **The From the Field connection** stays one paragraph (panel: "link is one final paragraph"): facts are limited to the entry; a longer link would be the book's invention.
- **F9.12 stays at three tools**: per-tool values for the other five are not in the article text (fact-check S11).
- **Summary sentence about citations** now distinguishes support (2023) from source identification (2025) (panel, Daniel) — changed, listed here because the panel's broader request to add data on research-report tools cannot be met: no published evaluation of those tools was used, and the four checks are presented as the book's method.

## Waiting for the author

1. **Live syllabus:** the lab title says "five sources"; A6 is now three sources (the lab's team pack has four). Week 6 has no R reading (confirm).
2. **From the Field:** confirm the ELM entry (YBS Ansiklopedi 1(1), 15–16, September 2014) and the book's note on Petty & Cacioppo (1986 vs. the entry's 1980); an optional first-person note on that is yours to write.
3. **Optional:** a real, anonymized case of a report whose references nobody had opened.
4. **Final voice edit** (pipeline step 8) — the editor never marks a chapter "done".

## Final review (build/ch09/reviews/final.md) — applied 2026-10-18

All 4 must-fix and 12 should-fix items applied as worded; nice-to-have wording and serial-comma fixes applied (Chapter 3 temperature wording, F9.1 label, F9.4 legend and the "social post" hop, Lab 9.2 "name and front-page heading", A$ gloss, arXiv scope, two serial commas). Not applied (not pure wording): 9.1/9.3 section lengths and objective/Bloom retagging of CSQ 2 and 4, Spaced Review 1 and the Lab 9.3 debrief.

| # | Change |
|---|---|
| M1 | Rule added to 9.5 step 3: a sentence that turns a reported link into a cause is **unsupported** (drift: cause from correlation, plus broadened claim if widened). Rekeyed: Review A10 and B4 sentence 1 (private); D-9.3 updated |
| M2 | Rung 4 = "the record of this claim": 9.8 sentence, F9.8b bracket "Funnel stage 2: the record of this claim", D-9.1 |
| M3 | Failure-to-harm chain uses "link" everywhere (chapter, C06, handoff case row); D-9.9 book-wide rule |
| M4 | BBC expanded at first use (9.4), *NEJM* expanded, ROUGE expanded |
| S1–S12 | Four-day-week rungs and blog support; M8 ("a document has one type, whatever the claim") and M9 ("who is behind a source changes its rung") added to blueprint §4 and the answer headers, distractors retagged; Elif's status and F9.15 statuses; 9.6 Your Turn; link 2 documented and solid (F9.20, alt text, longdesc, C06); citation rule includes "a narrower part … same population and outcome" and "a second source, with its own rung"; F9.16 "biases that would hide the effect"; Lab 9.2 key on eLearning (also in Compass) and in the instructor package; C48 and C52 closed in resolution_v2; rubric gaps closed (Task 1, Trace 0.5, Verification 0); Appendix E pointer in the time paragraph; goldfish walk-through labeled constructed |

Re-rendered (color and gray) and checked visually: F9.1, F9.4, F9.7, F9.8b, F9.15, F9.16, F9.20.
