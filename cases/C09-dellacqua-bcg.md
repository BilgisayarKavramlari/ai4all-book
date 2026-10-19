# Case: Consultants at the Jagged Frontier (Dell'Acqua et al., BCG, 2023)

Chapter: 12 (opening case and main Case Study; also Chapter 1 §1.2–1.3 and Chapter 11's reading guide) · Field: management consulting · Failure label: hallucination, leaf "contradicts its input or source" or "wrong calculation or reasoning" (either accepted; primary, **inferred**: the paper says the task was designed so GPT-4 would err, and does not report the outputs each consultant saw) · chain link 2 "checked before use?" failed and link 3 "someone relies on it": overreliance, **documented by the authors' statement** (Chapter 11: automation bias) · Outcome: mixed

Facts are stated in attribution tiers (book-wide rule): **confirmed** = the 2023 Harvard Business School working paper (HBS WP 24-013, full text read 2026-10-18) or the 2026 *Organization Science* abstract (Crossref record); **reported** = a named secondary source; **inferred** = this book's reading. The journal body was not read (paywalled); numbers come from the working paper.

## Context
Boston Consulting Group (BCG) is a global management consulting firm. In 2023, researchers from Harvard Business School, the Wharton School, MIT, Warwick Business School and BCG ran a preregistered experiment with 758 of BCG's individual-contributor consultants, about 7% of that group (confirmed). The study introduced the image of a "jagged technological frontier": AI raises performance on some tasks and lowers it on others that look equally hard.

## Timeline
- End of April 2023: the version of GPT-4 used by every consultant with AI, through a company platform built on the provider's API, with the provider's default system prompt and temperature (confirmed: WP p. 8).
- 2023: the experiment; each consultant first does a baseline task without AI, then is randomly assigned to no AI, GPT-4, or GPT-4 plus a prompt-engineering overview (videos and documents) (confirmed).
- September 2023: working paper released (HBS WP 24-013; SSRN 4573321) (confirmed).
- December 2025: a follow-up working paper on three modes of working with AI on the same task (HBS WP 26-036) (reported: HBS AI Institute summary, December 29, 2025; the authors' Fortune piece, January 30, 2026).
- March 2026: peer-reviewed version in *Organization Science* 37(2), 403–423 (confirmed: Crossref).

## What the AI did
Inside the frontier (385 consultants; 18 creative and analytical subtasks, such as ideas for a new shoe, market segmentation and a press release), the tool's outputs were good enough that consultants with AI completed more tasks (12.2%), worked faster (25.1%) and received quality ratings more than 40% higher (confirmed: WP abstract). On the outside task (373 consultants), the authors write that the interview notes led to a conclusion contrasting with what AI would give when prompted with the exercise instructions, the data and the interviews; the task was designed so that GPT-4 would err (confirmed: WP pp. 8, 13–14). The outputs each consultant received are not reported (hence "inferred" on the tree).

## What humans did
- Correctness on the outside task: about 84.4% without AI; about 70.5% with GPT-4; about 59.9% with GPT-4 plus the overview (confirmed: WP Table 4, col. 1: control mean 0.844, coefficients −0.139 and −0.245; text: "24 percentage points versus 13"). The gap between the two AI groups is significant only at the 10% level (F-test p = 0.082–0.095; WP p. 14); the gaps from no AI are significant at 1%.
- Time on the outside task: the AI groups finished faster (more than 11 minutes, 30%, for the overview group; more than 6 minutes, 18%, for GPT-4 alone) (confirmed: WP p. 14).
- Recommendation quality (1–10, two sets of human graders: BCG consultants not in the experiment and business-school students): +1.47 (25.1%) and +1.05 (17.9%) over the control mean, and higher whether the answer was right or wrong (confirmed: WP Table 6, Figure 8).
- Retainment (copying the tool's output into answers) was measured only in the creative, inside-frontier experiment, where the overview increased it and it went with higher scores (confirmed: WP p. 10, Appendix C). On the outside task, the authors state that consultants who did worse tended to adopt the output and question it less (confirmed as the authors' statement: WP p. 17; not a measurement).
- Among consultants who were correct with AI, the authors describe **centaurs** (dividing work between themselves and the tool) and **cyborgs** (integrating with the tool at the subtask level) (confirmed: WP pp. 15–16). The follow-up (244 consultants) adds **self-automators** (handing over whole workflows with little review); in the authors' own summaries, about 60% worked as cyborgs, 27% as self-automators and 14% as centaurs, and centaurs were the most accurate (reported: Randazzo et al., 2025, via the HBS AI Institute; Candelon et al., 2026). The working paper itself was not opened (403).
- Ideas on the creative task were less varied with AI; 100 simulated sessions of the tool alone were the most similar (confirmed: WP p. 12, Appendix D).

## Failure label (Signature 5 and the failure-to-harm chain; figures F12.18 and F12.19)
- **Tree — hallucination, inferred (dashed); either leaf accepted:** "contradicts its input or source" (the interview notes held the decisive information) or "wrong calculation or reasoning" (the authors say only that the task was designed so GPT-4 would err in its analysis). The paper does not report individual outputs. (Editor decision, revision v2.)
- **Chain — link 2 failed and link 3, documented by the authors' statement:** those who did worse questioned the output less; Chapter 11 calls this automation bias. **Link 4:** wrong recommendations in an experiment; no real-world harm.
- **No overconfidence label:** no evidence about expressed certainty.

## Consequences (documented only)
A widely cited result; the "jagged frontier" image entered the vocabulary of AI at work. No real-world harm (an experiment).

## A better workflow (AI Work Loop)
Frame: split the task into parts and predict, per part, which side of the tool's frontier it falls on. Prompt: ask the tool to work through the interview notes and state what in them could change the answer (whether this helps is a question for a test, not an assumption). Verify: score correctness separately from polish, against the interview notes (an independent check). Decide: keep the recommendation itself on the floor or in augmentation; use the tool for parts inside its frontier, as the centaurs did. Disclose: record in the deliverable which parts the tool drafted.

## Each appearance in the book has one job
Chapter 1: headline numbers and the frontier image. Chapter 11: the outside task (recommended reading, with a reading guide). Chapter 12 Opening: the two new findings (the overview group was correct least often, with the 10% caveat; quality rated higher regardless of correctness) and the puzzle. 12.1: a prompting overview did not move this tool's frontier on this task (10% caveat; one task, one model). 12.6: score correctness and polish separately (F12.10). Case Study: how successful consultants split the work, mapped onto the fit matrix and ladder; limits; WP vs. journal wording; labels.

## Limits (this book's reading of the design the authors report)
One firm; GPT-4 as of April 2023; tasks designed by the researchers; one outside task, selected to be outside. The journal abstract says "19% less likely"; the working paper says "19 percentage points" (the average of 13.9 and 24.5 points from 84.4%, about a 23% relative drop) (Case Study Question 4). The journal's full text was not read; check it before print.

## Questions
See the Chapter 12 Case Study Questions.

## Sources
1. Dell'Acqua, F., McFowland, E., III, Mollick, E., Lifshitz-Assaf, H., Kellogg, K. C., Rajendran, S., Krayer, L., Candelon, F., & Lakhani, K. R. (2023). *Navigating the jagged technological frontier* (HBS Working Paper No. 24-013). https://ssrn.com/abstract=4573321 (PDF via mitsloan.mit.edu; accessed 2026-10-18).
2. Dell'Acqua, F., et al. (2026). *Organization Science, 37*(2), 403–423. https://doi.org/10.1287/orsc.2025.21838 (Crossref record and abstract; accessed 2026-10-18).
3. Randazzo, S., Lifshitz, H., Kellogg, K. C., Dell'Acqua, F., Mollick, E., Candelon, F., & Lakhani, K. R. (2025). *Cyborgs, centaurs and self-automators* (HBS Working Paper No. 26-036); summary: https://aiinstitute.hbs.edu/the-three-ways-professionals-work-with-ai-which-one-are-you/ (accessed 2026-10-18).
4. Candelon, F., Kellogg, K. C., Lifshitz, H., & Randazzo, S. (2026, January 30). Are you a cyborg, a centaur, or a self-automator? *Fortune*. https://fortune.com/2026/01/30/ai-business-humans-in-the-loop-cyborg-centaur-or-self-automator/
