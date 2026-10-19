# Lab 22.2 — Trace an Energy Number

| Field | Value |
|---|---|
| Type | Check It |
| Objectives | O5 (LO1, LO3) · tags 4D:DISC, UNESCO:ETH-U |
| Time | About 30 minutes including reading this sheet and the debrief, at home; optional |
| Materials | The three figures below with their stated boundaries (section 22.6 box, as of October 2026); the printed boundary table |

## The three figures (as of October 2026)
- **A.** 0.10 Wh per median text prompt to Google's Gemini apps, counting the active AI chips only (Google, August 2025; reported). Google calls this narrower figure a substantial underestimate of the real footprint.
- **B.** 0.24 Wh per median text prompt to the same apps, counting the full serving system: the active chips, the host computer and memory, idle machines kept ready, and data-center overhead such as cooling and power conversion (Google, August 2025; reported; the blog says the figures were not verified by an independent third party).
- **C.** About 0.3 Wh per typical query to another provider's model (Epoch AI, February 2025; outside estimate from stated assumptions). What it counts: the computing chips' running time for an assumed model size and an answer of about 500 tokens, with a power figure per chip that includes the overhead of servers and data centers; it does not count idle machines separately, training or making the hardware. Other assumptions give about 0.1 to 4 Wh.

## Boundary table (fill in: yes, no, partly or not stated)

| Figure | Active chips | Host computer and memory | Idle capacity | Cooling and building power | Training | Making the hardware |
|---|---|---|---|---|---|---|
| A (0.10 Wh) | | | | | | |
| B (0.24 Wh) | | | | | | |
| C (0.3 Wh) | | | | | | |

## Steps (tool-neutral)
1. **Boundary table (12 min).** Fill each cell from the descriptions above.
2. **Explain (8 min).** In three sentences, explain why the figures differ. Use the words boundary, model and year.
3. **One more (5 min).** Take one energy or water claim about AI from the news (or, offline, the council speaker's "100,000 homes" from section 22.6). Can you fill its row? If not, which column is missing?

## Expected observations
No figure counts training or making the hardware. A and B differ only by boundary (same developer, same year, same kind of prompt). C is for a different provider's model, rests on stated assumptions, and folds server and data-center overhead into its power figure, so it counts roughly what B counts but for a different system.

## If it does not work
If a source does not say what it counts, write "not stated": that is a finding.

## Debrief (3–5)
1. Which figure would you quote to answer "how much energy does my question use"? (evaluate)
2. Which figure would a grid planner need instead? (analyze)
3. What one disclosure would make news claims comparable? (create)

## Deliverable
The completed boundary table and three sentences. Ungraded.

## Answer notes (read after you finish)
A: chips yes; everything else no. B: chips, host, idle capacity, cooling and power yes; training and hardware no. C: chips yes; host, cooling and power partly (inside the power figure); idle capacity not counted separately; training and hardware no.

## Accessibility and alternatives
Table available as plain text; no chart reading required; no internet needed for steps 1–2.
