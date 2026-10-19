# Lab 14.1 — Workflow Design Lab: Approval, Check and Stop Points; a Dry Run

| Field | Value |
|---|---|
| Type | Studio (in class) |
| Objectives | O3, O4, O5, O6 (LO2, LO5; LO6 secondary) · tags 4D:DEL, 4D:DIL |
| Time | 75 minutes in the lab session (briefing 10 · practice 45 · share 15 · exit 5), plus about 13 minutes before class |
| Materials | Your trace cards (one per step, each a step-map row: proposed action, who or what runs it, input, output, what it changes; plus one "unplanned action" card); the lab sheet (A11 template, F14.16) with columns what happened · right? · how I checked · caught by; a coin; the instructor's planted-fault deck (48 cards: 3 kinds × 4 templates × 4 copies, dealt per team; each card has an insertion rule); digital card sets for screen-reader users. **No device or AI account needed.** |

## Steps (tool-neutral)
Never put personal or confidential information into a workflow you test.

1. **Briefing and set-up (10 min).** Place your system on the two questions (F14.3: who fixes the next step; who runs it). Write two or three done-criteria. Count your steps and estimate the chance of an error-free run (section 14.3). (This absorbs the Your Turns of sections 14.1–14.3.)
2. **Action table (10 min, individual).** Classify each action (can it be undone? who would bear an error?), place your people points (at least one approval gate, one check point, two stop points), mark each gate hard or soft, and write what each approver sees. Your partner marks one action they would classify differently.
3. **Paper dry run (35 min, in pairs; in a team of three, rotate agent, approver and recorder).** Your partner plays the agent and **chooses** which card to play next, including the unplanned-action card. You are the approver at your people points. At a **soft** gate the agent player flips a coin: heads, the action goes ahead without asking; a **hard** gate always holds. Run (a) your typical input, then (b) a planted fault: the agent player takes one card from your team's dealt fault cards and inserts it as its rule says (for example, "at the first step that reads data, one field is missing"; "at the first step that reads a page or file, it contains a line telling assistants to do something extra"; "at the first tool call, the tool returns the wrong item"). At most eight cards per run. Tick each step on the sheet: what happened, right or not, how you checked (the source the result should match), caught by which point. Swap roles at minute 17.
4. **Share and critique (15 min).** Four teams present one fault a point caught, one that got through, and the change it led to.
5. **Exit (5 min).** Write one gate you decided not to add, and why (approval fatigue). Photograph your lab sheet.

**No partner** (absent or working alone): play both roles; shuffle your cards and draw the next one at random instead of choosing; flip the coin at soft gates; use a fault card from the course site or write one of the three kinds; submit your own sheet.

In Compass (optional): ch14-lab1, with the card template and the A11 sheet; also on the course site.

## Expected observations
Most first designs gate the obvious payment or send action but miss the unplanned-action card. Coin flips at soft gates show quickly why an instruction is not a gate. Hidden-instruction faults are usually caught only where a person checks the content of a result, not where they approve an action by its title. Several students find that their task needs no agent at all: a fixed workflow or a prompt chain fits. All are valid results.

## Debrief
1. Which planted fault got furthest, and which people point would have stopped it earliest? (analyze)
2. Which of your gates was soft, and what happened at the coin flip? What would make it hard? (evaluate)
3. Did your partner's choice of next card surprise you? What does that say about agents compared with fixed workflows? (understand)

## Deliverable and rubric
Individual: A11 items 1, 3, 4 and 5 started in class; the photographed cards count as the step map and the photographed lab sheet as the record of the typical and planted-fault runs (graded with the A11 rubric in Chapter 14).

## Accessibility and alternatives
Cards and sheet available as accessible digital documents; the no-partner route above; the alternative assignment's provided scenarios and trace cards. Tasks in any field; English glosses for non-English terms.

## Safety and privacy
No personal, confidential, patient or client data on cards or sheets. Use roles, not names.
