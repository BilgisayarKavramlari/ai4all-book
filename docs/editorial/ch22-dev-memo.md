# Chapter 22 — developmental memo (2026-10-18)

Inputs: four independent reviews run in parallel without sharing reports — subject-expert reviewer (Opus; 28 findings, 4 High), pedagogy reviewer (Opus; 18 findings, 4 High), student-reader panel (Maya / Daniel / Ayşe, Sonnet), fact-checker (Sonnet; docs/factcheck/ch22.csv, 105 claims: 64 supported, 37 partly supported, 1 unsupported, 3 cannot verify). The author delegated editorial choices (D19); the editor's ten Stage 5 decisions (build/ch22/editor-decisions-stage5.md) and the independence rules (D27) were applied in revision v2. The chapter agent who drafted v1 handed over at Stage 5; this revision was done by a new chapter agent. Draft v1 kept at build/ch22/ch22-draft-v1.qmd; v1 build-outs at build/ch22/v1-buildouts/. Fact-check log closed with a `resolution_v2` column and 13 new rows (C106–C118) for claims added in revision.

## Decisions — independence and editor rulings

| # | Change | Why |
|---|---|---|
| E1 | D27 applied: "at the end of the course", "No week of the course requires this chapter", "university-provided tool such as Microsoft Copilot Chat", "Answer key after the deadline on eLearning", "eLearning" packets, "graded weekly assignments" and the Apr 28 portfolio link removed; lab rule uses "a tool your institution provides or approves (for example, an enterprise chat assistant with data protection) or a free tier"; LOs are "the book's learning outcome"; essay says "if your course uses the portfolio … before it is due" | Editor decision 0; D27 |
| E2 | Hana stated as "a media arts and design student who runs a small zine" at first appearance in 22.2 and again in 22.8 (the fast route meets Hana there); they/them throughout | Editor decisions 0 and 10; D26; pedagogy #17 |
| E3 | One fast-route box in 22.1, "As of October 2026: five claims you will meet again" (METR horizon, open–closed gap, IEA 2025/2030, Google per-prompt figure with this book's laptop arithmetic, 2026 olympiad), each tagged | Editor decision 6; panel fix 1 |
| E4 | The Case Study's "Since then" 2026 box moved into 22.8 as a worked aging check ("A claim you can check yourself: the olympiad, a year later"), with a verdict (partly supported), what changed (the facts, as reported) and a next check (an IMO statement or the 2027 olympiad); the Case Study points to it | Editor decisions 6 and 9; panel (Daniel: student-checkable companion to the 2014 entry) |
| E5 | Visible "[VERIFY: OpenAI's own page refused automated access]" removed; Sora 2 cited to Lanz (2025), Decrypt | Editor decision 6; panel; fact-check C43 |

## Decisions — accuracy (fact-checker, subject expert)

| # | Change | Why |
|---|---|---|
| A1 | OpenAI's graders: "According to OpenAI, three former IMO medalists graded each proof (Wei, 2025, as reproduced by Willison, 2025)"; "Only Google had entered the competition, so the IMO did not grade or certify OpenAI's proofs (Davies, 2025)"; Reuters (CP24 copy) kept only for the July 28 request and the permission to publish; "chosen by the company" removed from the Opening, Worked Example A, Case Study, F22.2, keys | Expert #10; fact-check C05–C08, C97; editor decision 3. The CP24 copy has no score or graders; Euronews read for the entry fact |
| A2 | Seed Prover: "ByteDance said the IMO had confirmed" 30/42, "about three days" of search, problems formalized by hand; Aristotle's score is Harmonic's report; F22.2 tag "measured: each proof's validity (Lean) · scores reported by the developers" | Expert #9; fact-check C15, C84, C90 |
| A3 | AGENTS.md: "a standard file of written instructions for coding agents (not a way to reach tools)"; only MCP is a tool protocol; goose named | Expert #4 (High); fact-check C33 |
| A4 | "Measured" vocabulary repaired: *reported (compiled)* for AI Index scores (22.2, 22.3, 22.4 boxes; F22.5, F22.7 source lines); *outside estimate* defined once in 22.1 and used for Epoch 0.3 Wh, IEA and LBNL figures and Epoch's compute data; Chatbot Arena gap "measured: the leaderboard's votes, compiled by the AI Index"; METR page notice, Nobel and peer review take case tiers ("Confirmed: …") | Expert #5, #6, #23; pedagogy #4; panel (Daniel); editor decision 2 |
| A5 | Epoch 0.3 Wh: "other assumptions give about 0.1 to 4 Wh, and a long input of about 10,000 tokens about 2.5 Wh"; "Neither is wrong" replaced by Google's own framing ("says the narrower one substantially underestimates the real footprint"); the 10× case placed inside Epoch's range | Expert #6; fact-check C65, C66, C68; Epoch page re-read |
| A6 | PersonQA: o3 also more accurate (0.59 vs 0.47) because it makes more claims; "one test of one kind of question"; F22.6 title "more often accurate and more often wrong"; box adds the GPT-5 system card (Aug 13, 2025: far fewer factual errors than o3 on the developer's own tests, partly graded by another model), read in the card itself before printing | Expert #7; pedagogy #10; fact-check C23–C24; editor decision 4 |
| A7 | DeepSeek: R1-Zero (reinforcement learning only) distinguished from the released R1 (small set of written examples, further stages) | Expert #8; fact-check C20; editor decision 5 |
| A8 | "Rose fast once reasoning models arrived" → "in 2024, the year reasoning models arrived; that is a matter of timing, not a measured cause"; reasoning-model attribution of the olympiad results as the makers describe them | Expert #15; fact-check C12, C22 |
| A9 | IEA 2026: 485 TWh (2025) and about 950 TWh (2030, ~3%), AI-focused +50%; per-task efficiency sentence; accelerated servers ~30%/yr vs 9% replaces "fastest-growing part"; F22.14 rebuilt on the 2026 edition with title "about 485 TWh in 2025; … about twice that by 2030"; LBNL 325–580 TWh stated as 2028 totals "as reported by DOE and LBNL" | Expert #1, #20, #22; fact-check C58–C63; editor decisions 1 and 3; IEA executive summary read 2026-10-18 |
| A10 | 22.8 energy faded example rebuilt: a 2025 news story's 945 TWh, today's source the 2026 report (485/950 supplied); key "supported (partly supported accepted with a reason); facts only slightly changed; still a forecast; next edition" | Expert #1 (High); pedagogy #6; editor decisions 1 and 9 |
| A11 | Voices faded example prints Chapter 13's fact (listeners caught about 73% of speech deepfakes made with older methods; Mai et al., 2023); key rebuilt on it | Expert #2 (High); pedagogy #2 (High); fact-check C46; editor decision 1 |
| A12 | 22.3 faded key Q2: eight-hour tasks succeed about half the time at an 8-hour 50% horizon; four-in-five success holds for tasks several times shorter (about one to one and a half hours in the box) | Expert #3 (High); pedagogy #1 (High); editor decision 1 |
| A13 | METR: values named as Time Horizon 1.1 raw file (page text quotes older estimates); Opus 4.6 range about 5–60 h; Mythos (17 h) on its own line, not counted; fit "about 129 days (range 104–158), leaving out estimates above 16 hours"; F22.8 label "METR's fit … this book's recalculation agrees"; F22.3 milestone replaced (Opus 4.6, 12 h) | Expert #13, #14, #27; fact-check C16, C36–C38 |
| A14 | Open–closed: "Both say … months, not years" replaced (only Epoch measures time; the AI Index figure is a score gap as of February 2025); Epoch "as of October 30, 2025" with its caution that the gap likely looks larger than it is; Emberson (2025) as author | Fact-check C48, C51, C100; panel (Daniel); editor decision 3 |
| A15 | Epoch's 4–5× "for frontier models"; compute values labeled outside estimates; F22.13 "documented inputs" and title "The trend is documented; …" | Fact-check C53; editor decision 3 |
| A16 | May 20, 2026 result: "Reported by the developer; checked by nine outside mathematicians in a preprint (Alon et al., 2026), not yet peer-reviewed"; Short case 1 notes the problem list's maintainer is a co-author | Expert #12; fact-check C78; editor decision 3 |
| A17 | GNoME "2.2 million crystal structures predicted to be stable"; Cheetham & Seshadri "examined the claims" (not "a sample"); Decoder "mostly deleted", dated Oct 18, 2025 | Fact-check C73, C75, C91; editor decision 3 |
| A18 | Case Study: the IMO president's caution attributed to the organizers only; "this book adds that the other two kinds of check do not cover these questions either" | Pedagogy #12 |
| A19 | Lawsen: "a comment posted on arXiv … and later corrected by its author" | Expert #19; fact-check C26 |
| A20 | 2026 olympiad: "100%, which is a perfect 42"; the investor's test "informal, with no published method, so not measured"; counts kept attributed to AFP | Expert #25; fact-check C85, C87–C88 |
| A21 | Career Connection: Pew Research Center surveys (2024), AI experts vs U.S. adults, 20-year outlook (Pew report read 2026-10-18); "a measured fact about opinions; the opinions themselves are forecasts" | Expert #16; fact-check C95 |
| A22 | Ethics Lens: "developers' reporting of responsible-AI test results is patchy compared with their reporting of capability tests" | Fact-check C93 |
| A23 | Monitoring line in the 22.2 box now dated and sourced (Korbak et al., 2025, "new and fragile opportunity"), with the absence of later change marked as this book's reading; keeps Ch. 17's promise | Expert #26; fact-check C29 |
| A24 | References: Achim, Best, Bietti et al.; Hu & Tong (Nov 15, 2024, URL); Emberson (2025); Merchant 624(7990); Shehabi DOI 10.71468/P1WC7Q; Shojaee arXiv:2506.06941; Decoder Oct 18, 2025; added Alon et al. (2026), Davies (2025), Korbak et al. (2025), Kwa et al. (2025), Lanz (2025), Mai et al. (2023), OpenAI (2025b), Pew (2025), IEA (2026b), Wei (2025, escaped handle), Willison (2025); OpenAI (2025a) and IEA (2026a) relettered | Fact-check C25, C98–C103; expert #18; editor decision 3 |
| A25 | Warm-up answer 3: "a few seconds to under a minute of a 50-watt laptop" for a short prompt; "several watt-hours, a few minutes" for long inputs or answers | Fact-check C70 |

## Decisions — learning design (pedagogy, student panel)

| # | Change | Why |
|---|---|---|
| P1 | "Trace first" rule in 22.1 (a claim that names no source has no status yet); 22.4, 22.5 and 22.6 faded done steps and keys use it; the 22.5 done step no longer calls someone else's claim "the book's reading" | Pedagogy #3 (High); editor decision 2 |
| P2 | Evidence status simplified ("says who has checked it so far …; it does not say whether the claim is true"); "measured" no longer circular ("tested, run or checked by someone other than the developer") | Pedagogy #16; panel (Ayşe) |
| P3 | Crosswalk box: tiers "since Chapter 5" (was 9); warns that *reported* means different things in the two lists, with OpenAI's claim as reported in both senses; same line added to F22.4 | Pedagogy #5; panel (Maya); editor decision 2 |
| P4 | 22.8: three kinds of change only ("the facts" now covers a changed policy; Hana's Claim 2 = the facts); "contradicted" defined as "no longer true as a description of today, not wrong when written"; reason for the next check stated (answers CY 22.8 Q2); the 2014 example ends with a next check | Pedagogy #6; panel (Daniel); editor decision 9 |
| P5 | Fast-route recap rewritten as a glossary of the skipped sections' words (reasoning model, time horizon 50%/80%, realism, open-weight, Wh/TWh, system boundary, the field's checks), so it no longer repeats the Summary; TWh glossed in the 22.8 faded example | Pedagogy #13; panel fix 1; editor decision 6 |
| P6 | Note under the aged timeline explains the October 2025 and 2030 boxes the fast reader has not met; thick boxes now match the three claims re-checked in 22.8; F22.17 title "four had aged" | Panel; fact-check C83; editor decision 3 |
| P7 | 22.7: "four steps" (announcement, paper, data, field) in text, worked and faded examples; "stage" kept for the Verification Funnel only | Pedagogy #14; book-wide rule |
| P8 | Alt-text worked example: local running keeps scans off outside services, but the form permits only printing and posting, so it must first tell contributors (Hana's Ch. 21 risk line); trial only on scans whose artists said yes | Pedagogy #11; characters log (Ch. 18, Ch. 21) |
| P9 | Glosses added: system card, replication, NeurIPS, arXiv, crowd-vote leaderboard, AI Work Loop steps on page 1, SWE-bench Verified; idioms "keep the score in proportion" and "bind" (22.6) replaced; dates added to the 22.2 and 22.7 faded examples | Pedagogy #16; panel (Ayşe) |
| P10 | Worked 22.6 conclusion limited to what it shows ("with the same 30 prompts, the boundary and the kind of answer move one person's daily figure from about 4 to about 86 minutes") | Panel (Daniel) |
| P11 | Essay: rubric gaps closed (Task: "all but one" / "two or more missing"; status table: two complete + one element missing / any other partial; Verification: one or two complete, or two or more gaps; Declaration: one or more general; a true "no AI tools used" is complete); brief and rubric both say "source opened today (a primary source where one exists)"; time about 90 minutes counted per requirement (verdicts now counted); rubric framed for self-assessment or optional instructor feedback; alternative 400–600 words for readers without reliable internet or current sources, same rubric with two named changes | Pedagogy #7–9; panel; editor decision 8 |
| P12 | Time line recounted: fast route about 27 min, full route about 66 min (73 with Ethics, Career, From the Field, Summary); end-of-chapter items about 8 min to read and 45–50 min to answer at the standard rates | Pedagogy #9; brief (honest counts) |
| P13 | Labs: 22.1 handles the shared date and prints answer notes in the sheet; 22.2 prints the boundary table and Epoch's stated boundary (Epoch page re-read) with answer notes; 22.3 adds a doubling hint, ×4 chart ticks, provider shapes, and explains 155 vs 129 days and 50 vs 60 minutes; 22.4 rows match the boxes ("geometry result"), 30 minutes, offline packet; all repo paths and eLearning removed; chapter lab blurbs tagged O · LO · Bloom | Pedagogy #18; panel fix 3; editor decision 7 |
| P14 | Review A12 stem "checked by an outside test" (not the tier word "confirmed"); O2 tagged AI4K12 Learning, as in the blueprint; CSQ 4 points to 22.8; "within days" now printed (22.8 note) for the CSQ 5 key | Pedagogy #15 |
| P15 | Light Mode B voice pass (voice profile §10): "In other words" restatements after the two variants, the boundary paragraph and the aging-check definition; "Let's take one heavy user" in the calculation; no anecdotes or opinions added | Brief step 5 |

## Not changed (with reasons)

| Suggestion | Decision | Reason |
|---|---|---|
| Rename "reported" in one of the two label lists (panel) | Not renamed | Both words are fixed book-wide (case tiers from Ch. 5; evidence status in the brief); the chapter now warns about the double meaning in text, box and F22.4 |
| Replace the author's 2014 entry as the first aging example (panel, Daniel) | Kept, with a student-checkable companion | From the Field is registered for this chapter (X10); the 2026 olympiad check follows it, so readers have one example they can open themselves |
| Cut the essay to two claims (panel) | Not cut | Three claims keep the status table meaningful; the time is now stated honestly (about 90 minutes) instead |
| Official IMO 2025/2026 counts (expert #11) | Kept attributed to AFP | imo-official.org year pages return "page does not exist"; listed for the editor to read in Chrome |
| Print GPT-5 hallucination numbers | Not printed | One sentence without numbers is enough for the aging point; the card's figures depend on an LLM grader and would age fast |
| Trim the chapter back to the 7,900-word budget | Partly | Redundant sentences cut in 22.1, but the review-required additions (≈1,600 words) stay; the chapter is optional and the counts are stated (D-22.9) |
| Ch. 13 cross-chapter terms, Ch. 23's "measured" wording, pointers from Ch. 14/16/19/20/21 | Not edited here | Other chapters' files; recorded in the handoff for the assembly pass |
| METR data licence | Not resolved | The page states none; the chapter quotes values only and the CSV keeps its [VERIFY] note for the editor |
| Failure-chain highlight style in F22.19 (harm box drawn thick by Ch. 4's function) | Not changed | `failure_chain` is Chapter 4's signature function; reuse without redrawing is the rule |

## Waiting for the author

1. From the Field: approve the use of Şeker (2014) and confirm its page range (printed 8–12 vs file name 9–12).
2. Final voice edit of the chapter.

## For the editor (not the author)

Read in Chrome before print: LBNL-2001637 PDF (2028 totals wording), the IMO's official 2025 and 2026 results, optionally OpenAI's unit-distance and Sora 2 pages. Renders: all 20 figures re-rendered in color and gray and checked visually (PNG proofs in build/ch22/png/); `quarto render chapters/22-*.qmd --to html` completed with no warnings.
