# Lab 17.3 — Open the Scorecard

| Field | Value |
|---|---|
| Type | Deep |
| Objectives | O2, O3 (LO5) · tags 4D:DISC, UNESCO:TECH-A |
| Time | About 25 minutes including reading this sheet and the debrief, at home; optional |
| Materials | data/ch17_scorecard.csv (a constructed points scorecard and 20 constructed applicants; the rules are in the file's first line; the points are **not** in the file, so you compute them), opened in any spreadsheet. No AI tool needed |

## Steps
1. **Read the rule (3 min).** Five rules give points: income, debt ratio, months at the job, late payments in the last 24 months, and a bankruptcy on record before 2020. A total of 70 or more approves; otherwise "refer to a person."
2. **A local explanation (6 min).** Pick a referred applicant (for example A04). Compute each rule's points and the total. This is a glass-box explanation: it is the model's own logic, not an approximation.
3. **A global pattern (6 min).** For each referred applicant, find how many points each rule cost them: that rule's maximum minus the points they got. Which rule cost referred applicants the most points in total?
4. **Counterfactuals (7 min).** For your applicant, find the smallest **actionable** change that reaches 70, where "smallest" means the fewest bands moved. Then find a change that would also reach 70 but that the applicant cannot make, because it concerns a past record. Explain why it is not recourse.

## Expected observations
Every referred applicant can be explained exactly. The smallest actionable change is usually one band in debt ratio or months at the job, or one fewer late payment over time. Removing a past bankruptcy would also approve some applicants, but no one can change the past: a true counterfactual that is not recourse. Compare with section 17.4, where the explanation of a black box came from a search.

## If it does not work
If the spreadsheet will not open, the file is plain text: read it in any editor.

## Debrief (3–5)
1. What can you say about this scorecard that you could not say about the black box in 17.4? (analyze)
2. Should a scorecard use a past record a person cannot change? Which question would Chapter 16 ask first? (evaluate)
3. Which counterfactuals here are actionable only over time? (apply)

## Deliverable and rubric
The local explanation, the global count and the two counterfactuals. Ungraded. The points key is in the instructor package.

## Accessibility and alternatives
The file is plain CSV, screen-reader friendly; a printed table is in the instructor package.
