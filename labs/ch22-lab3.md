# Lab 22.3 — Read a Log Chart

| Field | Value |
|---|---|
| Type | Studio |
| Objectives | O3 (LO1) · tags 4D:DISC, UNESCO:TECH-U |
| Time | About 20 minutes including reading this sheet and the debrief, at home; optional |
| Materials | The horizon chart in section 22.3 (printed) and the same data as a table below (METR Time Horizon 1.1 raw results, downloaded October 18, 2026) |

## Data table (50% and 80% time horizons, in minutes of skilled-human task time; selected models)
| Model (developer) | Released | 50% horizon | 80% horizon |
|---|---|---|---|
| GPT-4 (OpenAI) | Mar 2023 | 4.0 | 0.9 |
| Claude 3.5 Sonnet (Anthropic) | Jun 2024 | 11.4 | 1.7 |
| o1 (OpenAI) | Dec 2024 | 38.8 | 7.1 |
| Claude 3.7 Sonnet (Anthropic) | Feb 2025 | 60.4 | 12.1 |
| GPT-5 (OpenAI) | Aug 2025 | 203.0 | 38.3 |
| Gemini 3.1 Pro (Google) | Feb 2026 | 384.1 | 89.8 |
| Claude Opus 4.6 (Anthropic) | Feb 2026 | 718.8 | 69.9 |

The chart marks each developer with a different shape (circle = OpenAI, square = Anthropic, triangle = Google); filled = 50% horizon, open = 80%. On the vertical axis, each tick is about four times the one below (1 min, 4 min, 15 min, 1 h, 4 h, 16 h).

## Steps (tool-neutral)
1. **Read two points (5 min).** Find OpenAI's March 2023 point (GPT-4) and its August 2025 point (GPT-5) on the chart; check them against the table.
2. **Doubling time (8 min).** From 4.0 to 203.0 minutes is how many doublings? Hint: keep doubling 4: 8, 16, 32, 64, 128, 256. 203 lies between the fifth doubling (128) and the sixth (256), about two-thirds of the way on a log scale, so about 5.7 doublings (a calculator's log₂(203 ÷ 4) gives 5.67). About how many months per doubling over the 29 months between the two releases?
3. **Data or trend (4 min).** Mark on the chart where the last measured point is. What is everything to its right?

## Expected observations
About 5.7 doublings in 29 months: roughly one doubling every 5 months (about 155 days) for these two points. METR's own fit, about 129 days (a little over 4 months), uses all the leading models since 2023, not two points, and a two-point estimate changes with the points you pick. Points are data; the dotted line is a trend, not data; anything beyond the last point is a forecast. 80% horizons are several times shorter.

Note: METR's first paper (March 2025) gave Claude 3.7 Sonnet a 50% horizon of about 50 minutes; the later data in this table give about 60 minutes for the same model, because METR updated its tasks and method. Different versions of a measurement can give different numbers.

## If it does not work
Use the table only; the chart is optional.

## Debrief (3–5)
1. Why does a straight line on this chart mean steady doubling? (understand)
2. What would make you doubt the next doubling? (evaluate)
3. Which number would you give a manager who wants reliability? (apply)

## Deliverable
Your doubling calculation and one marked chart. Ungraded.

## Accessibility and alternatives
The table replaces the chart for screen-reader users; the chart's long description is in the book's figure descriptions.
