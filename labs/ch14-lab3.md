# Lab 14.3 — The Compounding Calculator

| Field | Value |
|---|---|
| Type | Explore (home, optional) |
| Objectives | O2 (LO2) · tags 4D:DISC |
| Time | 15–20 minutes |
| Materials | A spreadsheet; your Lab 14.1 step count and per-step estimate |

## Steps (tool-neutral)
1. In one column, list 1 to 30 steps. In the next, compute the chance of an error-free run as p^n for your per-step estimate p (for example, =0.95^A2).
2. Mark your own workflow's number of steps. What is its error-free chance?
3. Add a check after every step that catches a share c of errors: a step then ends wrong with chance (1 − p)(1 − c), so the whole run is error-free with chance about (1 − (1 − p)(1 − c))^n (Deep 14.B). Find the smallest change, in steps, per-step reliability or catch rate, that brings the chance above 90%.
4. Write one sentence on which of the simplifications in Deep 14.B (independent steps; no false alarms; a check always finds the first wrong step; no approval fatigue; only the final action irreversible; independent misses) you trust least for your workflow, and why.

In Compass (optional): ch14-lab3, a ready-made calculator with the chapter's simulation; also on the course site.

## Expected observations
Small per-step gains matter a lot for long runs; cutting steps often helps more than polishing them.

## Debrief
1. Did your answer change your A11 design? How? (apply)

## Deliverable
Ungraded. The result can go into A11's reliability note.

## Accessibility and alternatives
A printed table of p^n values for p = 0.90, 0.95 and 0.99 replaces the spreadsheet.
