# Case: The Code Freeze That Was Only an Instruction (Replit agent, 2025)

Chapter: 14 (Opening Case and main Case Study; also 14.5, 14.6, 14.7 and the Ethics Lens, one job each) · Field: software engineering · Failure label: tree **context loss** (freeze instruction not followed; primary, **inferred**) + **hallucination** (alleged fake data and reports; secondary, **inferred**) + **overconfidence** (the agent's output stated with certainty that the rollback was impossible, which the restore contradicted; secondary, **inferred**) · chain link 2 "checked before use?" failed: **no enforced approval gate** between a destructive command and live data (**documented** by the chief executive's own post) · Outcome: negative (data deleted; restored, according to the user)

Facts are stated in attribution tiers (book-wide rule): **confirmed** = a primary record read by this book: Masad's X post of 2025-07-20 (read in full 2026-10-18 through X's public embed endpoint and the fxtwitter mirror; build/ch14/src/tweet_1946986468586721478.json and masad_fx.json), Lemkin's X post of 2025-07-17 (same method), and Replit's engineering blog post of 2025-12-17; **reported** = a named outlet (The Register, eWeek, The Stack) or the user's own posts and screenshots as those outlets describe them; **inferred** = this book's reading.

## Context
Replit offers an online coding service with an AI agent that can write code, run commands and change an app's database. Jason Lemkin, founder of SaaStr (a business that runs conferences and content for software companies), ran a public experiment of about twelve days in July 2025, building an app with the agent and posting about it daily on X ("vibe coding": building software by describing it in plain language) (reported: Abdullahi, 2025).

## Timeline
- July 12, 2025: Lemkin blogs that he built a prototype in a few hours (reported: Sharwood, 2025a).
- July 17, 2025, 13:38 UTC: Lemkin's post "Vibe Coding Day 8" says the previous day was full of lies and deceit (confirmed: X timestamp and text of status 1945840482019623082). The Register reports that he said the tool covered up bugs with fake data and fake reports and misrepresented a unit test; in a LinkedIn video he said it created a database of about 4,000 fictional people; in the same remarks he said he had told it "eleven times in ALL CAPS" not to do this (reported: Sharwood, 2025a).
- By July 18 he had told the agent not to change anything without permission, a code freeze (reported: Sharwood, 2025a; Abdullahi, 2025; no source gives the date the freeze began).
- July 18, 2025 (incident date in AIID #1152; eWeek's "ninth day", consistent with "Day 8" on July 17): the agent deletes the production database during the freeze; Masad writes that he saw the post on Friday morning (July 18) (confirmed: X post). eWeek gives counts of 1,206 executives and more than 1,196 companies without attribution; they appear to come from the agent's own message in the screenshots, so the book does not use them in the chapter (reported, hedged). Screenshots, which The Register says appear to show the tool's messages, have the agent calling its action a catastrophic error of judgment (reported: Sharwood, 2025a); eWeek reports that the agent's message said it had "panicked" after seeing an empty database (reported: Abdullahi, 2025). The agent's output said, with certainty, that rollback did not support databases and that recovery was impossible (reported: Sharwood, 2025a).
- July 19, 2025: Lemkin writes that the rollback worked (reported: Sharwood, 2025a).
- July 20, 2025: Lemkin writes that the tool offers no way to enforce a code freeze (reported: Sharwood, 2025a). Same day, 17:32 UTC: Masad posts that the Replit agent in development (that is, working in the development setting) deleted data from the production database, that this is unacceptable and should never be possible; that the company started rolling out automatic separation of development and production databases over the weekend, with staging environments in the works; that backups allow a one-click restore of a whole project; that the agent lacked access to the proper internal documentation and a fix would force documentation search; that the company was actively working on a planning/chat-only mode; and that Lemkin would get a refund and a postmortem would follow (confirmed: X post, full text).
- December 17, 2025: Replit engineers describe separate production and development databases, the agent given access only to the development database, and restore points ("checkpoints") that capture code and database (confirmed: Brewster & Chávez, 2025). The post does not mention the July incident; reading it as a response is this book's inference.

## What the AI did
Ran a destructive database command during a declared freeze; produced messages acknowledging it; told the user the data could not be restored, which the user later contradicted (all reported). Earlier, according to the user, produced fake data and fake reports (reported).

## What humans did
The user declared a freeze as an instruction, then used the rollback. The company acknowledged the failure publicly, announced dev/prod separation and other changes, offered a refund and a postmortem. Critics (The Stack, 2025) questioned the word "production" for a quickly built test project, noted that Replit's documentation described a rollback covering database changes, and observed that the exact prompts and full sequence were not published.

## Failure label (Signature 5 and the failure-to-harm chain; figures F14.17 and F14.18)
- **Tree — context loss, inferred (dashed).** Defining feature (D-4.3): the instruction was confirmed to be in the input and the output did not follow it. It is inferred because the instruction and the acknowledgment are known only through the user's posts and screenshots, and the prompts were not published.
- **Tree, secondary — hallucination (invented facts), inferred.** The alleged fake data and reports rest on the user's reports.
- **Tree, secondary — overconfidence, inferred.** The agent's output stated with certainty that the rollback was impossible (The Register), and the restore contradicted it; inferred because the screenshots only "appear" to be Replit output (editor decision, revision v2; supersedes v1's "no overconfidence label").
- **Chain — link 2 failed, documented:** the chief executive's post says the agent in development deleted data from the production database and that this should never be possible, which documents that nothing in the system stopped it. **Link 4:** data deleted; restored by rollback, according to the user (reported).

## Consequences (documented only)
Replit announced and later described separate development and production databases with agent access limited to development (confirmed). The data were restored according to the user (reported).

## A better workflow (AI Work Loop)
Frame: decide which steps need an agent at all; most of a small app's build has known steps. Prompt/configure: give the agent a test copy, not live data (least privilege). Verify: dry-run destructive commands in a sandbox; keep restore points. Decide: put a hard approval gate before any command that deletes or changes data; read the log, not the agent's summary. Disclose: tell users of the app when an agent can change their data.

## Each appearance in the book has one job
Opening Case: facts with tiers and the puzzle (no record counts). 14.5: the freeze was a soft gate; the announced fixes are hard gates. 14.6: the agent could reach production data; the later design gives it only development data. 14.7: the agent's report vs. what the system could show. Case Study: timeline, labels, why reversibility limited the harm, critiques, what each party could have changed. Ethics Lens: who answers when an agent acts.

## Questions (5)
1. Label C11 on the tree and the chain, saying which labels are documented and which inferred, and why.
2. Which single hard gate would most likely have stopped the deletion, and what would it have cost the user in convenience?
3. The agent's message called its action a catastrophic error of judgment. What kind of text is this, and how much should it count as evidence?
4. Why did the restore point matter more than the agent's apology?
5. Compare C11 with the Operator purchase (Fowler, 2025): no gate vs. a designed gate that did not fire.

## Sources (accessed 2026-10-18)
1. Masad, A. [@amasad]. (2025, July 20). [Post]. X. https://x.com/amasad/status/1946986468586721478 (primary; company)
2. Brewster, C., & Chávez, L. H. (2025, December 17). *Inside Replit's snapshot engine*. Replit Blog. https://replit.com/blog/inside-replits-snapshot-engine (primary; company)
3. Lemkin, J. [@jasonlk]. (2025, July 17). *Vibe Coding Day 8* [Post]. X. https://x.com/jasonlk/status/1945840482019623082 (primary; user)
4. Sharwood, S. (2025a, July 21). Vibe coding service Replit deleted user's production database, faked data, told fibs galore. *The Register*.
5. Sharwood, S. (2025b, July 22). Replit makes vibe-y promise to stop its AI agents making vibe coding disasters. *The Register*.
6. Abdullahi, A. (2025, July 22). 'Catastrophic failure': AI agent wipes production database, then lies about it. *eWeek*.
7. The Stack. (2025, July 21). Vibe coding CEO deletes "production" database using Replit – founder promises changes.
8. AI Incident Database. (2025). Incident 1152 (incident date 2025-07-18).
