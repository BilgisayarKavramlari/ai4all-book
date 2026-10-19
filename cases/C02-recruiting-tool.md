# Case: The Recruiting Tool That Learned the Past (Amazon, 2014–2017; reported 2018)

Chapter: 2 (also 16) · Field: business / human resources · Failure label: under-represented group in the sample; possibly biased labels; proxy features · Outcome: negative (project disbanded)

## Context
Amazon built an experimental tool to score job applicants automatically. The case is known from one investigative Reuters report (Dastin, 2018); the book uses only what that report states, and marks its own reasoning as such.

## Timeline
- 2014: a team begins building a tool to review resumes and score applicants.
- 2015: the company realizes the system is not rating candidates for software-developer and other technical posts in a gender-neutral way.
- Then: Amazon edits the programs to make particular terms neutral; this does not guarantee that the system will not find other ways to sort candidates that could be discriminatory.
- By early 2017: the team is disbanded.
- October 10, 2018: Reuters reports the story (Dastin, 2018).

## What the AI did
Scored applicants from one to five stars. Its models were trained to find patterns in resumes submitted to the company over about ten years; most came from men. It penalized resumes containing the word "women's" (as in "women's chess club captain") and downgraded graduates of two all-women's colleges.

## What humans did
People chose the training data and what the tool would treat as a good candidate. The company found the problem and edited the programs. According to people familiar with the project, recruiters looked at the recommendations but never relied solely on them. Amazon said the tool "was never used by Amazon recruiters to evaluate candidates" (statement in the Reuters.com version).

## Mapped to the Data-to-Prediction Pipeline (source figure F2.4d)
1. Collect data — documented: mostly men's resumes (an under-represented group, not class imbalance in the 2.4 sense).
2. Label — book's reasoning, not reported: if "good candidate" reflected past applications and hiring, the labels could carry past preferences.
3. Train — documented pattern, book's interpretation: words and college names linked to gender acted as proxies.

## Consequences (documented)
The team was disbanded. Reuters reported that a much-watered-down version was used for some tasks and that a new team was formed to try again with a focus on diversity. The record does not show that any candidate was rejected because of the tool; the book makes no such claim.

## A better workflow (AI Work Loop, for the builders)
Frame: define "a good candidate" and ask whether past data measures it. Verify: compare scores group by group before use; search for proxies, not only for a gender field. Decide: keep a human decision with an explainable reason. Disclose: tell applicants when automated scoring is used.

## Questions
See the Chapter 2 Case Study Questions.

## Sources
1. Dastin, J. (2018, October 10). Amazon scraps secret AI recruiting tool that showed bias against women. *Reuters*. https://www.reuters.com/article/us-amazon-com-jobs-automation-insight-idUSKCN1MK08G — primary; Reuters.com blocks automated access, text read via a Reuters.com page printout and syndicated copies (see docs/factcheck/ch02.csv); open once live before print.
2. AI Incident Database, report 611 (Incident 37). https://incidentdatabase.ai/reports/611 — secondary.
