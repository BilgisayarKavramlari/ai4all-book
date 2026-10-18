# A9 Scenario A′ — Internship Shortlist (one-page brief)

*Constructed scenario for Chapter 11's A9. No real people: candidates are letters. File: data/ch11_scenario_a.csv (on eLearning as a spreadsheet and a screen-reader-friendly table).*

**The decision.** A small accounting firm has one paid spring internship (12–20 hours a week). The office manager must send a **shortlist of three** candidates to the two partners for final interviews by Friday. The partners make the final choice; the office manager owns the shortlist.

**The six candidates and five criteria.**

| Criterion | What the firm recorded | Scale |
|---|---|---|
| Work-sample task | Each candidate reconciled a short sample ledger; two staff members scored it together | 0–100 |
| Structured interview | Same six questions for everyone, scored by the office manager | 1–5 |
| GPA | From the candidate's transcript | 0–4 |
| Hours available per week | From the application form; the firm needs at least 12 | hours |
| Attended a partner university | The firm has hired from two "partner" universities before (1 = yes) | 0 or 1 |

**Why two cells are blank.** Candidate **H** transferred this semester; the transcript from the previous university has not arrived yet (expected next week), so there is no GPA. Candidate **J**'s interview is scheduled for next Tuesday, after the shortlist is due.

**What the firm asked the AI tool.** "Build a decision matrix from this file: scale each criterion to 0–10, propose weights, compute totals and recommend a shortlist of three. Show your scaling rule and how you handled any blanks." (Use this prompt or your own; record the tool, model if shown, and date.)

**Your job (A9).** Audit the matrix the tool produces, as the chapter shows: what each criterion means and measures, whether it is a proxy and for whom the gap is bigger, how each blank was handled and whether the real value can be obtained before Friday; recalculate the top two; run two sensitivity tests; write the memo to the office manager.

**Notes.** The spreadsheet template (data/ch11_matrix_template.xlsx, sheet "Your matrix") does the scaling for you once you enter the ranges and weights. Do not add any real person's data to the file or to a prompt.
