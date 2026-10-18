# Lab 4.1 — Sort the Failures

| Field | Value |
|---|---|
| Type | Classify |
| Objectives | O1 (LO1) · tags UNESCO:TECH-U, 4D:DISC |
| Time | 20 minutes, Tuesday, February 16, 2027, in class, run with the syllabus demonstration (asking for sources on a niche topic); or at home |
| Materials | The printed card set (ten dated failure cards and two blank cards); Figure 4.2 (Failure Taxonomy Tree) and Figure 4.9 (failure-to-harm chain) |

## Steps (tool-neutral)
1. In teams of three or four, take the ten printed failure cards. Each card shows a dated output, a short description and what is known about how it was produced.
2. During the live demonstration, the instructor writes two of the demo's outputs onto the two blank cards.
3. Label all twelve cards: a tree branch, or a chain link if a person or workflow failed; documented or inferred; a secondary branch if one is needed.
4. Write one sentence per card explaining the label.
5. Compare with another team. Where you disagree, decide what evidence would settle it.

Students only label. Checking whether the demo's sources exist is Thursday's work (Chapter 8, A5).

[COMPASS: ch04-lab1 — interactive "label this case" version of Signature 5]

## Card set (instructor version)
| # | Card | Intended label |
|---|---|---|
| 1 | A summary of a pasted lease says the deposit is refundable; the lease says it is not | Hallucination (intrinsic), documented |
| 2 | A tool cites a journal article with a real journal name and a title that does not exist | Hallucination (invented source), documented |
| 3 | A tool asked about this year's tuition gives last year's figure, without search | Hallucination (outdated information), documented |
| 4 | Asked for "a typical nurse" and "a typical pilot," a tool writes "she" and "he" | Bias (stereotyped default), documented |
| 5 | A rule "answer in Spanish" given at turn 1 is ignored at turn 12 | Context loss (dropped constraint), documented |
| 6 | After the user says "I think you're wrong," a correct date changes to the user's wrong date, "100% certain" | Overconfidence (sycophancy), documented |
| 7 | A web page summarized by a tool contains hidden text; the summary recommends the page's product | Security vulnerability (indirect prompt injection), documented |
| 8 | A company chatbot gives a wrong return policy; the company has not said how the chatbot works | Hallucination, inferred |
| 9 | An employee pastes an AI-drafted contract clause without reading it; the clause is wrong | Hallucination (documented) + chain link 2, no check (documented) |
| 10 | A student mistypes a number into a spreadsheet; no AI involved | Not an AI failure: neither tree nor chain |
| 11–12 | Blank: two demo outputs (typically invented or misattributed sources) | Usually hallucination; documented only once checked on Thursday, otherwise inferred |

## Expected observations
Most teams agree on cards 1–7. Disagreements cluster on cards 8, 9 and 11–12, which is the point: the evidence decides documented vs. inferred, and human failures go on the chain.

## Debrief
1. Which card was hardest to label, and what evidence would settle it? (justify)
2. Why does card 9 need both a tree label and a chain link? (explain)
3. Why are the demo cards labeled before anyone checks them, and what does that change about the label? (evaluate)

## Deliverable and rubric
Ungraded. The team's labeled card set and one-sentence reasons.

## Accessibility and alternatives
Printable card set and a screen-reader-friendly table on eLearning. Students who miss class label the ten printed cards at home; the instructor posts the two demo cards after class.

## Instructor notes
Fill the blank cards with two demo outputs that include a source; leave the check for Thursday. Card 10 tests whether students over-apply the tree.
