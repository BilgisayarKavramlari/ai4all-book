# Lab 16.3 — The Trade-off Calculator (Deep)

| Field | Value |
|---|---|
| Type | Explore (optional, Deep, not examinable) |
| Objectives | O3 (LO5) · tags 4D:DISC |
| Time | 15 minutes |
| Materials | data/ch16_tradeoff_groups.csv (this book's calculation: two constructed groups of 1,000 students with score bins 0.1–0.9 built so that a score means the same in both groups); a spreadsheet; template in Compass (optional) |

## Steps (tool-neutral)
1. For each group, a student is flagged if the score is at or above the group's threshold. For a threshold, add up the students flagged and the students flagged who needed help.
2. Compute, for each group: selection rate, miss rate, false-positive rate and precision.
3. Start with both thresholds at 0.5 and check your results against the worked example in section 16.3 (miss 15.0 and 45.0; false positives 45.0 and 12.1; precision 65.4 and 66.0).
4. Change one group's threshold at a time (0.1, 0.3, 0.5, 0.7, 0.9). Try to make all four measures equal across groups.
5. Write one sentence on why it fails, using Deep 16.A's formula.

## Expected observations
No pair of thresholds makes all four measures equal (data/ch16_tradeoff.csv lists all 25 pairs). Equal miss rates come with unequal precision (0.5/0.3: precision 65.4 vs. 46.4); equal-looking precision comes with unequal error rates (0.5/0.5).

## Debrief
1. Which pair would you choose for a tutoring outreach email, and why? (evaluate)
2. Would your choice change for a decision that withholds something, such as a scholarship? (evaluate)

## Deliverable and rubric
None (optional practice).

## Accessibility and alternatives
The 25 results are precomputed in data/ch16_tradeoff.csv for students who prefer to read rather than calculate.

## Safety and privacy
Constructed data only.
