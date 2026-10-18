# Case: Tesla's Autopilot recall and the gap between expectations and capability (2023–2024)

Chapter: 19 (engineering guide) · Field: engineering (automotive safety) · Failure label: tree not applicable (no AI output was wrong; the defect is in the design of the human's controls); chain link 2 controls insufficient (documented, recall report); link 3 overreliance (documented, NHTSA) · Outcome: negative

## Context
Autopilot combines adaptive cruise control with Autosteer, a driver-assistance feature at SAE Level 2: the driver must supervise at all times. NHTSA's Office of Defects Investigation opened a preliminary evaluation (PE21-020) on Aug 13, 2021 and upgraded it to an engineering analysis (EA22-002) on Jun 8, 2022 (confirmed).

## Timeline
- Dec 5, 2023: Tesla decides to recall, while not concurring with the agency's analysis.
- Dec 12, 2023: recall 23V-838 filed: 2,031,220 vehicles (Model S 2012–2023, Model X 2016–2023, Model 3 2017–2023, Model Y 2020–2023).
- Apr 25, 2024: EA22-002 closed; recall query RQ24-009 opened on the remedy's adequacy.
- As of October 2026, NHTSA's record shows RQ24-009 open (no closing document found).

## What the AI did
Not a single wrong output. The recall report says that, in certain circumstances, Autosteer's controls may not be sufficient to prevent driver misuse (confirmed).

## What humans did
The remedy was a free over-the-air software update with more prominent alerts, extra checks and eventual suspension for repeated misuse (confirmed).

## Consequences (documented only)
NHTSA analyzed 956 crashes, 467 in scope, including 13 crashes with fatalities (14 deaths), and described a critical safety gap between drivers' expectations and the system's capabilities (EA22-002 closing resume; confirmed). RQ24-009 cites post-remedy crashes and remedy parts that drivers can opt into or reverse (confirmed).

## A better workflow (AI Work Loop)
Frame: what must the human do? Verify: test the human's role, not only the software. Decide: enforce engagement (a hard gate), not only warn. Disclose: state limits where drivers will see them.

## Questions (4–6)
1. Why does the tree not apply here, and where does the chain apply?
2. Which part of the remedy is a soft gate, and which a hard one?
3. What does "a gap between expectations and capability" mean for a student's workflow card?
4. Why must the RQ24-009 status always carry a date?

## Sources (at least 2, one primary; with access date)
1. Tesla, Inc. (2023, December 12). *Part 573 safety recall report 23V-838*. NHTSA. https://static.nhtsa.gov/odi/rcl/2023/RCLRPT-23V838-8276.PDF (read 2026-10-18) — primary.
2. National Highway Traffic Safety Administration, Office of Defects Investigation. (2024a, April 25). *ODI resume EA22-002 (closing)*. https://static.nhtsa.gov/odi/inv/2022/INCLA-EA22002-14498.pdf (read 2026-10-18).
3. National Highway Traffic Safety Administration, Office of Defects Investigation. (2024b, April 25). *ODI resume RQ24-009 (opening)*. https://static.nhtsa.gov/odi/inv/2024/INOA-RQ24009-12046.pdf (read 2026-10-18).
