# Lab 2.2 — Break It with Data

| Field | Value |
|---|---|
| Type | Break It |
| Objectives | O3 (LO1, LO5) · tags AI4K12:3, 4D:DISC |
| Time | 25 minutes, at home or in Compass (optional, recommended) |
| Materials | The Lab 2.1 tool, training photos and the **same** test photos |

## Steps (tool-neutral)
Retrain the Lab 2.1 model, changing only the training data. Use the same test photos each time and fill in the table.

| Run | Change to the training data | Overall correct | Correct on the changed class |
|---|---|---|---|
| 1 | Balanced, correct labels (Lab 2.1) | | |
| 2 | Imbalanced: keep only 5 photos of one object | | |
| 3 | Scattered errors: move 6 photos of each object into a wrong class, chosen at random (18 of 90 labels wrong) | | |
| 4 | One-directional errors: move 18 photos of one object into one other class (the same 18 wrong labels, all pointing one way) | | |
| 5 | Background: retake the training photos of one object on a new background, and test on the old one | | |

Then compare your table with the table in section 2.4. If you have time, repeat one run to see how much the results change by chance.

[COMPASS: ch02-lab2 — tool steps; post-MVP interactive "try the regimes" version of the label-regimes chart (source ID F2.9)]

## Expected observations
Run 2 lowers the score of the reduced object more than the overall score. Run 3 costs less than Run 4, even though the same number of labels is wrong (in Run 4, most photos of that object carry the wrong label). Run 5 can produce a shortcut: test photos of that object on the old background may fail. Numbers vary with small datasets and different tools; the pattern is what matters.

## Debrief (3–5)
1. Which run hurt the changed class most? Does that match the book's experiment? (compare)
2. Why might one-directional errors be worse than scattered ones? (explain)
3. Which of your runs is most like the recruiting tool in the Opening Case, and why? (analyze)
4. What single number would you report to someone deciding whether to use your model? (justify)

## Deliverable and rubric
Ungraded. The completed observation table and answers to two debrief questions.

## Accessibility and alternatives
Students without a working tool use the provided results table on eLearning (from a run of the same procedure) and answer the debrief. Screen-reader route as in Lab 2.1.

## Safety and privacy
As in Lab 2.1: objects only.

## Instructor notes
Book experiment for reference (data/ch02_regimes.csv, three digit classes, logistic regression, 30 runs): balanced 98.0 / 98.5; imbalanced 91.7 / 77.3; 20% scattered 91.9 / 89.9; 20% one-direction, 36 of the 60 eights labeled "3", 74.7 / 24.3 (overall / accuracy on the 8s). Student numbers will differ.
