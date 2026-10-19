# Case: Two gold medals, three kinds of grading: AI at the International Mathematical Olympiad (2025–2026)

Chapter: 22 · Field: mathematics / AI evaluation · Failure label: none on the tree (no output shown wrong; an evidence-status case). Short case 1: chain link 2 "checked before use?" failed (documented in the problem-list maintainer's public reply, as reported by The Decoder) · Outcome: mixed (strong results; uneven checking)

Attribution tiers (book-wide): confirmed (primary record) · reported (named outlet or person) · inferred (the book's reading). Evidence status (Chapter 22): measured (tested, run or checked by someone other than the developer) · reported (the developer, or an outlet citing it) · forecast · the book's inference; variants: reported (compiled), outside estimate. "Reported" appears in both lists with different meanings. Source notes: build/ch22/c31-sources.md; fact-check: docs/factcheck/ch22.csv.

## Context
The International Mathematical Olympiad (IMO) is an annual competition for pre-university students under 20: six proof problems over two days, 4.5 hours a day. In 2025 several AI developers tested systems on the problems; only Google DeepMind had entered the competition, and the IMO graded and certified its proofs (reported: Davies, Euronews, 2025; confirmed for DeepMind by its own post).

## Timeline
- **Sat July 19, 2025:** OpenAI (researcher Alexander Wei's post, reproduced by Simon Willison) announces that an experimental reasoning model solved 5 of 6 problems for 35/42; according to OpenAI, three former IMO medalists graded each proof (reported: developer). OpenAI had not entered; the IMO did not certify the result (reported: Euronews). Reuters: the IMO had asked cooperating companies to publish on July 28; OpenAI said an IMO board member allowed publication after the closing ceremony (reported: Reuters).
- **Mon July 21, 2025:** Google DeepMind announces that an advanced Gemini Deep Think scored 35/42, five of six problems, in natural language within the time limit; IMO coordinators graded and certified the proofs (confirmed: DeepMind's post; capability measured). DeepMind's post states the IMO's review does not extend to validating its system, processes or model.
- **July 22, 2025:** AFP reports the IMO president's caution that organizers could not verify the computing used or whether people were involved; 641 students from 112 countries, about 10% gold, five perfect scores (reported: AFP). Reuters, mid-reporting, gave 630 students and 67 gold medals; national federations later reported other totals (counts differ; the IMO's own results pages could not be read, 2026-10-18).
- **July 23, 2025:** ByteDance reports a 30/42 (silver-level) score for Seed Prover that it says was confirmed with the IMO; the system writes proofs in Lean after the problems were formalized by hand; per-problem scores 2/7/7/7/7/0: problems 2–5 fully solved after about three days of computer search (well beyond the 4.5-hour limit), problem 1 partly (completed later), problem 6 not solved (reported: developer).
- **Oct 2025:** Harmonic's preprint reports gold-medal-equivalent performance for Aristotle with formally verified proofs (reported: developer; the Lean checker confirms proof validity, not the score).
- **July 23, 2026:** AFP reports that Huawei and Xiaohongshu said their systems scored 100% (a perfect 42) at IMO 2026 in Shanghai; Xiaohongshu said its answers were submitted to the IMO's organizers for grading and that human intervention was prohibited; the companies received the problems after the students' exam; 7 of 666 students had full marks, per AFP citing the official scoreboard; a venture investor's own informal test (no published method; not measured) gave 42/42 for four other models; no IMO statement in the report (reported: AFP).

## What the AI did
Produced written proofs for olympiad problems: in natural language (Gemini Deep Think; OpenAI's model) or in a proof assistant's formal language (Seed Prover; Aristotle). The natural-language systems are described by their makers as reasoning models; OpenAI's account credits, in part, more computation at answer time.

## What humans did
Coordinators graded entered proofs by the student criteria; three former medalists graded within OpenAI's own evaluation (according to OpenAI); people formalized problem statements for the Lean systems; journalists reported the claims with different degrees of attribution.

## Consequences (documented only)
No harm. Public claims of "gold" appeared under different kinds of checking. By 2026, two companies reported perfect scores (reported). This book reads that as a sign that the olympiad may no longer separate the strongest systems (the book's inference, marked in the chapter, section 22.8).

## A better workflow (AI Work Loop: Frame → Prompt → Verify → Decide → Disclose)
Verify: tag each claim with its as-of date, evidence status and who could check it; Decide: cite the certified result as measured and the self-graded one as reported; Disclose: say what no check covered (computing, human involvement, the formalization step).

## Short case 1: "Ten open problems solved" (October 2025)
An executive's post (Oct 17–18, 2025) said a model had found solutions to ten open Erdős problems; the problem list's maintainer said "open" meant he knew of no solution; the model had found existing papers; the posts were mostly deleted (reported: The Decoder, Oct 18, 2025). Tree: none (the literature search was useful). Chain: link 2 "checked before use?" failed: the claim was published before anyone checked what "open" meant (documented in the maintainer's reply, as reported). Since then: Erdős #728 resolved with an AI-assisted, Lean-checked proof (Sothanaphan, 2026, arXiv:2601.07421); on May 20, 2026, OpenAI reported a disproof of a 1946 geometry conjecture of Erdős, checked by nine outside mathematicians, including the problem list's maintainer, in a preprint not yet peer-reviewed (Alon et al., 2026, arXiv:2605.20695; OpenAI's own page not read, 403).

## Short case 2: GNoME (2023–2024)
Merchant et al. (2023, *Nature* 624(7990), 80–85): 2.2 million crystal structures predicted to be stable (below the earlier convex hull); 736 already made independently. Cheetham & Seshadri (2024, *Chem. Mater.* 36(8), 3490–3495), examining the claims: "scant evidence" of compounds that are novel, credible and useful at once; methods promising. Tree: none; a dispute about what counts as a discovery.

## Questions (4–6)
1. For each kind of check, what did it check and what did it leave out?
2. Write one honest sentence each about the two 35/42 results.
3. Why is the main case "none" on the tree while Short case 1 has a chain label?
4. What has aged since July 2025, and is it a change of facts, status or names?
5. Which claim in the two short cases was settled quickly, and why?

## Sources (at least 2, one primary; with access date)
1. Google DeepMind (2025, July 21), blog post (primary for DeepMind's claim) — accessed 2026-10-18.
2. Wei (2025, July 19), post on X, as reproduced by Willison (2025) (primary for OpenAI's claim; x.com not opened) — accessed 2026-10-18.
3. Davies (2025, July 22), Euronews (only Google entered; OpenAI self-published) — accessed 2026-10-18.
4. Reuters (2025, July 21), via CP24 (timing; publication request; permission) — accessed 2026-10-18.
5. Agence France-Presse (2025, July 22), via Citizen Digital — accessed 2026-10-18.
6. ByteDance Seed (2025, July 23), blog post — accessed 2026-10-18 (fact-check read).
7. Achim et al. (2025), arXiv:2510.01346 — accessed 2026-10-18.
8. Agence France-Presse (2026, July 23), via The Standard — accessed 2026-10-18.
9. The Decoder (2025, October 18); Sothanaphan (2026), arXiv:2601.07421; Alon et al. (2026), arXiv:2605.20695; Merchant et al. (2023); Cheetham & Seshadri (2024) — accessed 2026-10-18.
