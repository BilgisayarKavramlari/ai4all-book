# Case: The Paste That Could Not Be Taken Back (Samsung, 2023)

Chapter: 15 (Opening Case and main Case Study; also 15.1, 15.6 and the Ethics Lens, one job each) · Field: engineering / corporate · Failure label: **none on the tree (input-side harm); data-flow map** (input crossed the trust boundary into a provider's storage) and **Risk Heat Map** (high likelihood, high impact before the measures) · Outcome: negative (loss of control over confidential data; no disclosure to anyone else is reported)

Facts are stated in attribution tiers (book-wide rule): **confirmed** = a company statement on the record: a Samsung spokesperson confirmed to TechCrunch on May 2, 2023 that the company was temporarily restricting generative AI on company devices, and did not comment on the leak (Park, 2023); nothing else is confirmed (an official told *The Economist* Korea the pastes were an internal matter it could not confirm); **reported** = a named outlet: *The Economist* Korea (Jeong, 2023, read in Korean via translation on 2026-10-18) and Bloomberg (Gurman, 2023, paywalled; read through its summary and CSO Online's account, Sharma, 2023; also The Register, Dobberstein, 2023); **inferred** = this book's reading.

## Context
Samsung Electronics' Device Solutions (semiconductor) division had restricted a popular AI chat tool and lifted the restriction on March 11, 2023, telling staff to be careful with internal information and not to enter personal content; the Device eXperience (mobile and appliances) division still banned it (reported: Jeong, 2023).

## Timeline
- March 11, 2023: the semiconductor division allows the chat tool (reported: Jeong, 2023).
- Within 20 days: three cases found (reported: Jeong, 2023). (A) An employee pastes the full source code of a program that downloads data from a semiconductor equipment-measurement database, to fix an error. (B) An employee pastes source code of a program that identifies equipment affecting yield and defects, asking for optimization. (C) An employee records a meeting on a phone, converts it to text with a speech-to-text app and pastes the text to draft minutes.
- The company's internal notice: once entered, content is sent to and stored on outside servers and cannot be retrieved; emergency limit of 1,024 bytes per question; investigation and possible discipline; an in-house AI service under consideration; warning that access could be blocked (reported: Jeong, 2023).
- March 30, 2023: *The Economist* Korea publishes the report.
- April 2023: an internal survey; 65% of respondents saw a security risk in such services (reported: Sharma, 2023, citing Bloomberg).
- May 2, 2023: Bloomberg reports a memo to staff in one of Samsung's biggest divisions restricting generative AI tools, after engineers accidentally leaked internal source code by uploading it, "earlier in April" according to the memo; data sent to such services is stored on outside servers, hard to retrieve and delete, and could be disclosed to other users; staff asked not to upload company information from personal devices, with dismissal possible (reported: Gurman, 2023; Sharma, 2023). TheWrap (2023) adds internal networks and company-owned devices (reported). The same day, a Samsung spokesperson confirmed to TechCrunch that generative AI was temporarily restricted on company devices (confirmed: Park, 2023).
- **Discrepancy:** March (Jeong) vs. April (the memo as reported). Not resolved by the available record.

## What the AI did
Nothing wrong is reported. The tool received the pastes and, presumably, answered the requests; no output is described.

## What humans did
Three employees pasted confidential material into an outside tool to do ordinary work faster (inferred: no intent to leak is reported). The company counted the cases, warned staff, limited input size, considered an in-house tool and later restricted generative AI on company devices.

## Labels (book-wide input-side rule)
The Failure Taxonomy Tree does not apply: no output was wrong. On the **data-flow map** (F15.4), the input crossed the trust boundary into the provider's storage; this book reads the pastes as made under consumer terms, but the reports do not say which account type was used (inferred). On the **heat map** (F15.18), before the measures: high likelihood (three cases in under three weeks; documented by the company's count as reported) and high impact (trade secrets outside the company's control). The measures lowered the likelihood of new pastes; they could not lower the impact of the pastes already made.

## Consequences (documented only)
Company measures as reported (input limit, warnings, device restriction, in-house tools). No report shows that the code reached any other user.

## A better workflow (AI Work Loop: Frame → Prompt → Verify → Decide → Disclose)
**Frame:** which part of the task needs the tool? **Prompt:** apply the data gate before pasting (company source code is confidential; section 12.5); send a minimal, de-identified description of the error instead of the whole program, or use an approved tool under the company's contract. **Decide:** the company approves a tool and writes the rule before lifting a ban; a technical block on uploading confidential files (data loss prevention). **Disclose:** report a mistaken paste at once so the company can act.

## Each appearance in the book has one job
Opening = facts and puzzle · 15.1 = the flow crossed the boundary; the notice's reason · 15.6 = the measures classified (reduce: limit, in-house tool, warnings; avoid: device restriction; owners are the reader's reasoning, the reports name none) · Case Study = map, heat map, discrepancy, what each party could change · Ethics Lens = workers without a safe route.

## Questions (5)
See the chapter's Case Study Questions 1–5.

## Sources (accessed 2026-10-18)
1. Jeong, D.-Y. (2023, March 30). [Exclusive] Concerns become reality: Samsung Electronics sees misuse as soon as it lifts its ChatGPT ban [in Korean]. *The Economist* (Korea). https://economist.co.kr/article/view/ecn202303300057 (earliest report; reporter 정두용; the site romanizes the byline Jeong Du-yong)
2. Gurman, M. (2023, May 2). Samsung bans staff's AI use after spotting ChatGPT data leak. *Bloomberg*. https://www.bloomberg.com/news/articles/2023-05-02/samsung-bans-chatgpt-and-other-generative-ai-use-by-staff-after-leak (paywalled; summary read)
3. Sharma, S. (2023, May 2). Samsung bans staff AI use over data leak concerns. *CSO Online*. https://www.csoonline.com/article/575215/samsung-bans-staff-ai-use-over-data-leak-concerns.html
3a. Park, K. (2023, May 2). Samsung bans use of generative AI tools like ChatGPT after April internal data leak. *TechCrunch*. https://techcrunch.com/2023/05/02/samsung-bans-use-of-generative-ai-tools-like-chatgpt-after-april-internal-data-leak/
3b. TheWrap. (2023, May 2). Samsung cracks down on staff use of AI, citing security risks.
4. Dobberstein, L. (2023, April 6). Samsung reportedly leaked its own secrets through ChatGPT. *The Register*. https://www.theregister.com/2023/04/06/samsung_reportedly_leaked_its_own
5. OpenAI. (2023, March 1). *Introducing ChatGPT and Whisper APIs* (API data not used for training by default). OpenAI. (2023, April 25). *New ways to manage your data in ChatGPT* (chat history off). Both read in Internet Archive captures by the fact-checker.
