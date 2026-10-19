# Case: Two gold medals, three kinds of grading: AI at the International Mathematical Olympiad (2025–2026)

Chapter: 22 · Field: mathematics / AI evaluation · Failure label: none on the tree (no output shown wrong; an evidence-status case). Short case 1: chain link 2 "checked before use?" failed (reported) · Outcome: mixed (strong results; uneven checking)

Attribution tiers (book-wide): confirmed (primary record) · reported (named outlet or person) · inferred (the book's reading). Evidence status (Chapter 22): measured (checked by an outside source) · reported (the developer) · forecast · the book's inference. Source notes: build/ch22/c31-sources.md.

## Context
The International Mathematical Olympiad (IMO) is an annual competition for students under 20: six proof problems over two days, 4.5 hours a day. In 2025 several AI developers tested systems on the problems; the IMO coordinated with some of them for the first time (reported, Reuters, 2025).

## Timeline
- **Sat July 19, 2025** (date derived from Reuters' "Saturday"): OpenAI announces that an experimental reasoning model scored 35/42 on the 2025 problems, graded by three former IMO medalists; not certified by the IMO (reported: Reuters).
- **Mon July 21, 2025:** Google DeepMind announces that an advanced Gemini Deep Think scored 35/42, five of six problems, in natural language within the time limit; IMO coordinators graded and certified the proofs (confirmed: DeepMind's post; capability measured). DeepMind's post states the IMO's review does not extend to validating its system, processes or model.
- **July 22, 2025:** AFP reports the IMO president's caution that organizers could not verify the computing used or whether people were involved; 641 students from 112 countries, about 10% gold, five perfect scores (reported: AFP). Reuters gives 630 students and 67 gold medals (reported; counts differ).
- **July 23, 2025:** ByteDance reports an IMO-certified 30/42 (silver-level) for Seed Prover, which writes proofs in Lean after the problems were formalized by hand (reported: developer).
- **Oct 2025:** Harmonic's preprint reports gold-medal-equivalent performance with formally verified proofs (reported: developer).
- **July 23, 2026:** AFP reports that Huawei and Xiaohongshu said their systems scored 100% at IMO 2026 in Shanghai; Xiaohongshu said its answers were submitted to the IMO's organizers for grading; 7 of 666 students had full marks; a venture investor reported 42/42 for four models in his own test (reported: AFP).

## What the AI did
Produced written proofs for olympiad problems: in natural language (Gemini Deep Think; OpenAI's model) or in a proof assistant's formal language (Seed Prover; Aristotle). Both natural-language systems were reasoning models using large answer-time computation, as their makers describe them.

## What humans did
Coordinators graded certified entries by the student criteria; a developer selected its own graders; humans formalized problem statements for the Lean systems; journalists reported the claims with different degrees of attribution.

## Consequences (documented only)
No harm. Public claims of "gold" appeared under different kinds of checking. By 2026 the competition no longer separated the strongest systems (the book's inference, marked in the chapter).

## A better workflow (AI Work Loop: Frame → Prompt → Verify → Decide → Disclose)
Verify: tag each claim with its as-of date, evidence status and who could check it; Decide: cite the certified result as measured and the self-graded one as reported; Disclose: say what no check covered (computing, human involvement, the formalization step).

## Short case 1: "Ten open problems solved" (October 2025)
An executive's post said a model had found solutions to ten open Erdős problems; the problem list's maintainer said "open" meant he knew of no solution; the model had found existing papers; posts deleted (reported: The Decoder). Tree: none (the literature search was useful). Chain: link 2 "checked before use?" failed: the claim was published before anyone checked what "open" meant (reported). Since then: Erdős #728 resolved with an AI-assisted, Lean-checked proof (Sothanaphan, 2026, arXiv:2601.07421); a May 20, 2026 developer report of a disproof of a 1946 conjecture with outside mathematicians' companion paper (reported; openai.com not read).

## Short case 2: GNoME (2023–2024)
Merchant et al. (2023, *Nature* 624, 80–85): 2.2 million structures below the earlier stability line; 736 already made independently. Cheetham & Seshadri (2024, *Chem. Mater.* 36(8), 3490–3495): "scant evidence" of compounds that are novel, credible and useful at once; methods promising. Tree: none; a dispute about what counts as a discovery.

## Questions (4–6)
1. For each kind of check, what did it check and what did it leave out?
2. Write one honest sentence each about the two 35/42 results.
3. Why is the main case "none" on the tree while Short case 1 has a chain label?
4. What has aged since July 2025, and is it a change of facts, status or names?
5. Which claim in the two short cases was settled quickly, and why?

## Sources (at least 2, one primary; with access date)
1. Google DeepMind (2025, July 21), blog post (primary for DeepMind's claim) — accessed 2026-10-18.
2. Reuters (2025, July 21), via CP24 — accessed 2026-10-18.
3. Agence France-Presse (2025, July 22), via Citizen Digital — accessed 2026-10-18.
4. ByteDance Seed (2025, July 23), blog post — search excerpt of the official page, 2026-10-18.
5. Achim et al. (2025), arXiv:2510.01346 — accessed 2026-10-18.
6. Agence France-Presse (2026, July 23), via The Standard — accessed 2026-10-18.
7. The Decoder (2025, October); Sothanaphan (2026), arXiv:2601.07421; Merchant et al. (2023); Cheetham & Seshadri (2024) — accessed 2026-10-18.
