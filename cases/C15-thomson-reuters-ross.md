# Case: Thomson Reuters v. Ross — Training on Westlaw Headnotes Not Fair Use (2025; affirmed 2026)

Chapter: 18 · Field: law / intellectual property · Failure label: **none on the Failure Taxonomy Tree** (input-side harm: copying works to train a tool; no AI output was wrong) — analyzed on Chapter 15's data-flow map (input → reuse/training) · Outcome: negative for the AI developer (infringement; not fair use, affirmed on appeal)

Facts are stated in three attribution tiers (book-wide rule): **confirmed** = the court record (district memorandum opinion, Feb 11, 2025, read in full: build/ch18/src/ded-ross.txt; Third Circuit opinion, Sept 29, 2026, read in full: build/ch18/src/ca3-ross.txt); **reported** = a named outlet; **inferred** = this book's reading. Every status line is dated and is a row in data/ch18_legal_status.csv. Not legal advice.

## Context
Thomson Reuters owns Westlaw, a legal-research service. Westlaw's editors write headnotes (short summaries of a point of law in a court decision) and organize them in the Key Number System (confirmed). Court opinions themselves are not protected by copyright (confirmed: 3d Cir. op.). ROSS Intelligence was founded by three University of Toronto computer-science students who had used IBM's Watson in a competition; it set out to build an AI legal search engine that answered plain-language questions with passages from judicial opinions (confirmed: 3d Cir. op., pp. 4–5).

## Timeline
- Before training: Ross asked to license Westlaw's content; Thomson Reuters refused because Ross was a competitor (confirmed: trial-court op., p. 3).
- Ross contracted LegalEase, which (with a subcontractor) wrote about 25,000 training memos, each a legal question with four to six court-opinion passages labeled great, good, topical or irrelevant; the memo writers used thousands of Westlaw headnotes to frame the questions (confirmed: 3d Cir. op., pp. 5–6; trial-court op. calls them "Bulk Memos").
- Ross trained its tool on the memos and marketed it against Westlaw at comparable prices; some law firms switched (confirmed: 3d Cir. op., p. 6).
- 2020: Thomson Reuters sues (D. Del. No. 1:20-cv-613) for copyright infringement and tortious interference (confirmed).
- December 11, 2020: Ross announces it will shut down; platform offline January 31, 2021; the litigation continues (reported: Ambrogi, 2020, LawSites).
- 2023: the judge (Bibas, a circuit judge sitting by designation) denies summary judgment on fair use, leaving it for a jury (confirmed: trial-court op. revises 694 F. Supp. 3d 467).
- February 11, 2025: revised ruling. Of 2,830 headnotes compared, actual copying found for 2,243 (p. 12); fair use rejected; factors 1 and 4 for Thomson Reuters, 2 and 3 for Ross (pp. 15–23: factor 1 p. 16, factor 2 p. 20, factor 3 pp. 20–21, factor 4 pp. 21–23, balance p. 23) (confirmed).
- March 18, 2025: Ross moves for certification (D.I. 786). April 4, 2025: two questions certified for interlocutory appeal, originality of headnotes and the Key Number System, and fair use; case stayed (D.I. 799). June 17, 2025: the Third Circuit grants leave (D.I. 805) (confirmed: docket index; questions quoted in 3d Cir. op., p. 7).
- June 11, 2026: argued; September 29, 2026: **affirmed** (Restrepo, Montgomery-Reeves, Bove; opinion by Montgomery-Reeves) (confirmed).
- As of October 2026: Ross asked to extend the rehearing deadline to November 3, 2026 and said it would seek Supreme Court review (reported: LawSites, Oct 2, 2026 (Supreme Court plan); MediaPost, Oct 12, 2026 (extension request)). Remaining claims would return to the trial court after the appeal (inferred: the case was stayed pending the interlocutory appeal, D.I. 799).

## What the AI did
Ross's tool was **not generative**: it returned passages from about ten million existing judicial opinions in response to a question (confirmed: both opinions). No output is alleged to have reproduced headnotes; the outputs were opinion passages (confirmed: trial-court op., factor 3).

## What humans did
- Ross sought a license, was refused, and obtained training data built with the competitor's headnotes (confirmed).
- The courts: **trial court** — 2,243 headnotes original and infringed; factor 1 against fair use (commercial, not transformative: same purpose as Westlaw), factor 2 for Ross, factor 3 for Ross (outputs did not show headnotes), factor 4 for Thomson Reuters (substitute; potential market for AI training data), called "the single most important element" (quoting Harper & Row); "only non-generative AI is before me" (paraphrased). **Appeals** — all 2,243 headnotes original, each a copyrightable work; factor 1 against ("minimally transformative, at best" — the chapter's one quotation from this source); factor 2 slightly for; **factor 3 against** (whole headnotes copied; copying unnecessary because the opinions are free) — the one factor the appeals court decided the other way; factor 4 against, without ranking it above the others (Westlaw's market and a rapidly developing market for licensing headnotes as AI training data; Thomson Reuters uses its headnotes to train its own AI products); called the case an ordinary copyright case; footnote 7 distinguishes generative models (Bartz; In re OpenAI) and notes the Justice Department's statement of interest of Sept 1, 2026 in the OpenAI litigation (confirmed). The footnote is a narrowing remark, **not a holding** (this book's reading, consistent with the opinion's text).
- Note: the appeals opinion once says Ross copied "25,000 … headnotes", conflating memos and headnotes; the book uses 2,243 (district finding, affirmed).

## Failure label (input-side rule; the Case Study's data-flow map)
- **Tree:** does not apply — no AI output was wrong (brief's input-side rule; supersedes the Ch. 4 handoff proposal "other (intellectual property)").
- **Data-flow map:** input = memos written from Westlaw headnotes (the copying); reuse = training the tool; output = passages of court opinions, not headnotes. The legal risk can be rated on the Risk Heat Map (Case Study Question).
- **Chain:** not used (the chain describes output errors).

## Consequences (documented only)
Infringement of 2,243 headnotes found on summary judgment; fair use rejected and affirmed; binding in the Third Circuit (Delaware, New Jersey, Pennsylvania, U.S. Virgin Islands), persuasive elsewhere (inferred: standard appellate effect). Ross ceased operating (reported).

## A better workflow (AI Work Loop: Frame → Prompt → Verify → Decide → Disclose)
- **Frame:** what data may we train on, under which license? Record each training source.
- **Verify:** check training data for material copied from a competitor or a refused licensor.
- **Decide:** license, build from free sources (here, the opinions themselves), or do not build.
- **Disclose:** keep a record of data sources that a court, a client or a regulator can inspect (cf. EU AI Act Art. 53 training-content summaries for general-purpose models, a different setting).

## Questions (4–6)
1. Place the case on the data-flow map and explain why the tree does not apply.
2. Why did both courts stress that the tool was not generative, and why is footnote 7 not a holding?
3. How did the two courts reason about factors 3 and 4?
4. What did the appeals ruling settle, whom does it bind, and what did it leave open?
5. Compare with Getty Images v. Stability AI (UK, 2025): the same question under a different law.

## Sources (at least 2, one primary; with access date)
1. *Thomson Reuters Enterprise Centre GmbH v. Ross Intelligence Inc.*, No. 25-2153 (3d Cir. Sept. 29, 2026). https://www2.ca3.uscourts.gov/opinarch/252153p.pdf (full text read 2026-10-18)
2. *Thomson Reuters Enterprise Centre GmbH v. Ross Intelligence Inc.*, No. 1:20-cv-613-SB (D. Del. Feb. 11, 2025) (mem. op., D.I. 770). https://www.ded.uscourts.gov/sites/ded/files/opinions/20-613_5.pdf (full text read 2026-10-18)
3. Ambrogi, R. (2020, Dec 11). Legal research company ROSS to shut down under pressure of Thomson Reuters lawsuit. LawSites. https://www.lawnext.com/2020/12/legal-research-company-ross-to-shut-down-under-pressure-of-thomson-reuters-lawsuit.html; Ambrogi, R. (2026, Oct 2), LawSites (Supreme Court plan) https://www.lawnext.com/2026/10/ross-says-it-will-ask-supreme-court-to-review-3rd-circuit-ruling-for-thomson-reuters-in-copyright-case.html; Davis, W. (2026, Oct 12), MediaPost (extension request) https://www.mediapost.com/publications/article/418680/ai-company-plans-to-seek-new-hearing-in-copyright.html (reported)
4. Jones Day (2025, February). No fair use in AI copyright clash (secondary; earlier index URL)
