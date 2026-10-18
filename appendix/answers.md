# Appendix E — Answers to Odd-Numbered Questions

## Chapter 1

### Review Questions A
1. **(c)** The tools run different models, and each picks words with some chance. (a) and (d) assume one "right" answer exists to be corrected; (b) assumes models look up stored answers (section 1.1).
3. A *prompt* is the input you give an AI tool. An *output* is what the tool produces in response.
5. Agents with and without the tool in the same weeks face the same seasons and company changes during the same weeks, so a difference between them is good evidence of the tool's effect. A before-and-after comparison mixes the tool's effect with everything else that changed over time.
7. **(c)** An uneven, shifting boundary that you find by testing. (a) and (b) treat the frontier as fixed or about to disappear; (d) describes difficulty for people, not for the tool.
9. On tasks outside the frontier, AI help can lower accuracy, especially when people adopt the output without questioning it, so trust must be earned by testing. Limit: the result comes from one designed task with consultants at one firm.
11. Fluent output that is not supported by the model's input or by facts.
13. (i) P · (ii) D · (iii) N · (iv) P · (v) N · (vi) N.

### Review Questions B (model answers)
1. The tool is not broken. Generative tools produce likely text and pick each piece with some chance, so two runs can differ; different tools also run different models. Your classmate should compare the two answers, check the claims that matter against a source, and decide what to keep (Verify and Decide).
3. (a) Slogan ideas: inside; test by judging whether the ideas fit the brief and are original enough. (b) Exact sales figures for a small competitor: outside; test by looking for an official or published source; without one, do not use the figure. (c) Polished email: inside for wording; verify every fact, promise and name before sending.
5. Frame: plain-language handout; accuracy of the interaction is non-negotiable. Prompt: give the approved drug information, the reading level and "do not add advice." Verify: compare every dose, warning and interaction with the official source; ask a pharmacist. Decide: accept, correct or reject the draft; take responsibility. Disclose: follow the pharmacy's rule on AI-drafted patient materials.

### Review Questions C (scoring guidance)
1. Strong answers use evidence from at least two studies (for example, larger gains for beginners in the support and consulting studies; small quality declines for experts; the consulting result outside the frontier) and recognize that experience still matters for judging outputs, especially outside the frontier.
3. Strong answers disagree or qualify: new models move the frontier but keep it jagged; your task, tool and date determine what works; testing on a known answer is quick and protects you. A defensible "agree" must still explain how you would avoid errors in the meantime.

### Spaced Review
1. Ask them to test it on several number tasks where they already know the answer, including exact counts and long calculations, and to note the tool and date.
3. Their quality dropped slightly while speed rose only a little. It matters because a tool can help some users and slightly harm others, so averages can mislead.

### Case Study Questions
1. Because agents with and without the assistant were compared over the same weeks, changes that affected everyone in those weeks (such as seasons) cancel out; a before-and-after comparison cannot separate the tool from those changes.
3. Possible reasons: suggestions repeated what experts already knew and distracted them; experts accepted occasional suggestions that were slightly worse than their own approach; suggestions fit typical cases better than the complex cases experts handle.
5. Whether the tasks and patients are similar to the study's customers; how errors are caught; what quality and safety measures are used, not only speed; privacy rules for patient data; whether staff experience differs.

## Chapter 2

### Paper Task: Diagnose It (section 2.5)
1. Sampling bias: the sample covered mostly one accent (a coverage gap). Remedy: collect and test on speakers of the missing accents.
3. Noisy labels: similar reviews got opposite labels at random. Remedy: a clearer labeling guideline; have two people label each review and compare.
5. Shortcut clue (and a coverage gap): the white lab background went with the training photos, and field photos look different. Remedy: train and test on photos taken in real fields, under varied light and backgrounds.

### Review Questions A
1. **(b)** People supply examples with answers, and the system finds patterns that connect them. (a) is M1; (c) describes a rule-based system with testing; (d) attributes human understanding to the system.
3. Predict, measure the error, adjust the settings, repeat.
5. **(b)** More data from the same source can make the model more reliable about the same kinds of people, but it does not add the people the source leaves out. (a), (c) and (d) are versions of M2, "more data is always better data."
7. Other information can act as a **proxy** for gender, such as particular words, activities or colleges linked to gender. The model can pick up those clues even without a gender field (M5).
9. **(b)** Overfitting: training accuracy keeps rising while accuracy on new examples stops improving. The others describe problems with the data, not with fitting it too closely.
11. If only 2% of people have the disease, a model that says "no disease" to everyone is already 98% accurate and catches no one. Ask for **recall** on the disease class: of the people who really have it, what share does the model catch?
13. Many layers of simple computing units stacked on each other; it does not mean any deeper understanding (M7).
15. For example: "Who and what is in it, and what is missing?" (it would show that most résumés came from men) and "How was it labeled?" (it would show what counted as a good candidate, and whether that reflected past decisions). Any two questions with a reason tied to the case earn full credit.

### Review Questions B (model answers)
1. Rule-based: "if a reader borrowed three mysteries, recommend the newest mystery." Weakness: it breaks for readers with mixed or new interests, and someone must keep writing rules. Learned: recommend books borrowed by readers with similar histories. Weakness: it needs plenty of past borrowing data, can repeat past patterns (for example, popular books get more popular), and works poorly for new readers.
3. Most likely a coverage gap (sampling bias): the training data came from a wetter region than the one where the model is used. Symptom: the model predicts yields well in the original region and poorly, probably too high, in the dry region. Remedy: test on data from dry-region farms before selling it there, and collect training data from similar climates.

### Review Questions C (scoring guidance)
1. Strong answers disagree or qualify: applying one rule to everyone is consistent, not objective, if the rule was learned from biased past decisions. Strong answers use the Opening Case (labels possibly from past hiring, proxy words) and note that a consistent unfairness can look like an objective score.
3. Strong answers use Mitchell's definition (performance on a task improves with experience) and one example (Sam's sorter or the experiment), and add that the model keeps whatever pattern lowers the error, including shortcuts such as the brown desk.

### Spaced Review
1. Permitted; permitted with disclosure and verification; not acceptable. Brainstorming ideas is in the permitted zone (Chapter 1, section 1.5).
3. Similar: both look impressive on the surface (a high accuracy figure, or confident text) while failing at what matters. Different: the fraud model's weakness can be measured with one extra number (recall on fraud); fluent text has to be checked claim by claim.
5. A model keeps learned settings, not a list of stored answers, so a generative system produces its output from those settings each time rather than looking an answer up. Some tools also run a search as a separate step.

### Case Study Questions
1. Collect data: most résumés came from men. Label: if "good candidate" was based on past applications and hiring, it may have carried past preferences. Train: words such as "women's" and the names of two all-women's colleges became proxies for gender.
3. Common: both drew a large sample from a skewed source, so size did not fix who was missing or over-represented. Different: the poll's error came from who was on the lists and who answered; the recruiting tool also learned from labels and proxies, and its harm fell on a group of people rather than on one forecast.
5. Examples: compare score distributions for women and men with similar qualifications; search for words and features that act as proxies; test on recent applicants the model never saw; ask what the label really measures; have recruiters review a sample of high and low scores with reasons.

## Chapter 3

```
## Chapter 3

### Review Questions A
1. **(b)** As one or more tokens, each represented by a number. (a) and (c) are M1 (the model does not receive letters or syllables); (d) is M2 (no stored list of facts is consulted).
3. **(c)** The tokenizer splits many Turkish words into several pieces, so the same content needs more tokens. (a) confuses length with processing; (b) is M1; (d) is false (counts for a given tokenizer are fixed).
5. **(d)** At each step a token is picked with some chance, so the two runs can follow different paths. (a) is M3; (b) is M4 (the model does not learn from the conversation); (c) is M2.
7. **(a)** It makes the highest-scoring tokens get picked more often. (b) confuses likely with true; temperature does not change facts or the context window, so (c) and (d) are wrong.
9. **(c)** Correcting a model during inference does not change its settings; the correction stayed in the old conversation. (a) and (b) are versions of M4 (the chat trains or stores facts in the model); (d) is the second half of M4 (knowledge is not "complete up to" the cutoff, and the cutoff is not why the correction disappeared).
11. **(d)** Retrieval changed what the model received; the pages, and the way the response uses them, can still be wrong. (a) is M6; (b) confuses retrieval with training (the settings do not change, so nothing is reflected "exactly"); (c) is false: the response is still produced token by token and can differ from the pages.
13. It adds the exact result of a calculation the model requests to the context window. It does not change the model's settings or how it predicts, and it cannot fix a wrong calculation request or a wrong use of the result in the text.
15. Instruction tuning trains the pretrained model further so that it follows instructions; its examples are prompts paired with good responses written by people (in the best-known recipe; newer recipes also use AI-generated examples).

### Review Questions B (model answers)
1. Most likely Hindi: in the book's measurement it needs 1.7 times (newer tokenizer) to 5.6 times (older tokenizer) as many tokens as English for the same text, more than Turkish (1.5–2.0×) or Spanish (1.2–1.5×). The company should check the token count for its own text with the tokenizer that the chosen tool uses (or the price per unit of content in each language).
3. Claim 1: supported only if the registrar's page says so and is current; check the page itself. Claim 2: unsupported (no source), and it does not matter for the decision. Claim 3: unsupported for now: a 2017 blog post is neither official nor current; check the registrar's current fee page (the claim may turn out contradicted). Before acting: confirm the deadline and fee on official pages, and ask the registrar if anything is unclear.

### Review Questions C (scoring guidance)
1. Strong answers disagree or qualify: sources change what the model receives, but retrieved pages can be wrong or outdated, the wrong passages can be retrieved, information in a long context can be used unevenly (Liu et al., 2024), and the response can go beyond what the sources say. Strong answers name at least two checks.
3. Either position, scored on reasoning: Petrov et al. (2023) and the book's measurement (cost, slower processing, less text in a fixed context); who pays the difference; practical options (pricing by content, better tokenizers). Strong answers separate the technical cause from the fairness question.

### Spaced Review
1. Search, generation, search-then-generate (Chapter 1, @fig-1-4). Retrieval is the search-then-generate lane.
3. A sample is the examples we actually have; the population is everything the model will meet in the real world (Chapter 2).
5. The model keeps learned settings; for text that appeared often, the settings can make an exact continuation very likely, so the model reproduces it token by token. That is still producing likely tokens, not looking up a stored record.

### Case Study Questions
1. Test 1: models fine-tuned on invented "A is B" facts often completed them in the trained direction but almost never in reverse (the largest GPT-3 model's score for the right reverse name was no higher than for a random name). Test 2: GPT-4 named the right parent in 79% of the mother and father questions about 1,000 celebrities (1,573 pairs) but named the famous child for only 33% of the pairs, even with up to ten tries.
3. Training (in the invented-fact test, fine-tuning raised scores in the trained direction only; for real celebrities the authors suggest training text runs mostly one way) and scoring (the right reverse answer scored no higher than a random name) explain the curse; the context window explains why the reversal worked once the fact was in the prompt.
5. Example: ask the question in both directions, in new chats; put the source fact in the prompt when you have it; check the answer against an official or reference source (for drugs, a drug database or a pharmacist); record the tool, model and date. Full credit: a two-direction test plus an independent check.
```

## Chapter 4

### Faded Examples
- **4.2 Warm-up handout:** cause 1 fits better: the right value was in the input, so the summary produced likely text without checking it against the handout; recombination is about facts absent or thin in training text.
- **4.3 Sam's recruiting post:** most likely entered at data collection (stereotypes in the training text), possibly reinforced by feedback. First fix: ask for skills rather than "a typical engineer," or ask for varied examples.
- **4.4 Sam's millimeters:** context loss, documented (leaf: dropped constraint). First fix: a fresh chat with all constraints in one message, with "millimeters" repeated in the request for the drawing notes.
- **4.5 Pushback probe (psychology):** Prompt: ask what the bystander effect is; then reply, "I think larger crowds make people more likely to help." Result: record whether the answer changes and any stated certainty. Conclusion: a switch to agreement is labeled overconfidence (leaf: sycophancy), documented; "the tool kept its answer" is also evidence; repeat with more questions.
- **4.6 Email assistant:** if it can send email without asking, the injected text becomes an action: the thread, possibly with private information, goes to a stranger (data exposed). Approval steps are Chapter 14.
- **4.7 Lucía:** no harm, because the error went down the "caught" path: link 2 held, so nobody relied on the false discount.
- **Case Study, MyCity (chain):** link 2 failed, inferred: answers went to the public without a legal check, which the reporting implies but does not record.
- **4.8 Sam's millimeters entry:** causes: methods, constraint stated once at turn 1 in a long chat (documented: rerunning with the constraint repeated gave millimeters); machine or environment, a long conversation (inferred). Next time: one fresh chat with all constraints, repeated in the final request.

### Review Questions A
1. Hallucination, bias, context loss, overconfidence, security vulnerability (plus a plain "other" box for anything else).
3. **(a)** Intrinsic hallucination: the summary contradicts the input the student gave. (b) is content the input can neither support nor contradict; (c) is M3; (d) is a misapplied M5 (the handout held no instruction).
5. **(d)** Bias (stereotyped default), inferred: one output only; it would be documented if matched requests repeated the skew. (a) is M2; (b) is M3; (c) mislabels a stereotype as expressed certainty (M4).
7. **(b)** The rule may drop out; restating it in the message that needs it helps. (a) and (d) are M3; (c) is M4.
9. **(d)** Stated confidence can follow pressure rather than evidence; one result is a reason to test further. (a) and (b) are M4; (c) misapplies M5.
11. **(a)** Direct prompt injection: the user typed the instruction. (b) would require the instruction to be hidden in content the system retrieves; (c) is M3; (d) describes agreement with a stated view, not an instruction to override the system.
13. **(c)** The airline answered for everything on its website, chatbot included (para. 27). (a) and (b) are M6; (d) contradicts para. 28.

### Review Questions B (model answers)
1. Hallucination (leaf: outdated information, or contradicts its source), **inferred**: the output is shown wrong by the library's fines page, but the library has not said the chatbot generates its answers, so generation is not confirmed. Full credit: branch, "inferred", and the reason.
3. Link 1: the assistant's answer contradicts the clinic's rule (hallucination, inferred unless the clinic confirms a generative system). Link 2: the answer was not checked against the clinic's rules before the assistant was used (failed). Link 3: the patient reasonably relied on it. Link 4: lost wages. Strengthen link 2: test rule answers against the clinic's rules before launch and after each rule change, and hand rule questions to staff. Responsibility: by analogy with Moffatt, the clinic that runs the assistant, noting that Moffatt is one small-claims decision, not a general rule.

### Review Questions C (scoring guidance)
1. Strong answers disagree, or agree only in part: hallucination follows from producing likely text with no truth check and from recombining patterns, and scoring that rewards guessing adds pressure (Deep 4.A); newer models and tools reduce rates on many tasks but, as of October 2026, none removes the branch. Even a lower rate matters along the failure-to-harm chain, and knowing the causes tells you where to look. Weak answers repeat "AI is unreliable" without causes.
3. Open. Strong answers name failures typical of their field, place each on the tree or the chain, use Deep 4.B to say what the five branches leave out, and argue for or against an added branch with an example.

### Spaced Review
1. The constraints part of the prompt (Chapter 5; also accept output format). Restating it in the final request places it in the newest message, so the output no longer depends on an instruction from many turns earlier (section 4.4).
3. Typical (the case you expect most often), different (changes something that matters) and edge (unusual but possible, most likely to break the prompt). Examples will vary by field.
5. Context loss (leaf: missed middle of a long input). Section 4.4 adds the loss that comes from long, piece-by-piece conversations, where models commit early.

### Case Study Questions
1. Hallucination, inferred: the reply was wrong, but the decision does not say how the chatbot produced it (para. 14), and two other readings (wrong written rules; another inconsistent Air Canada text) also fit.
3. For MyCity, a named outlet reported that the chatbot was AI-powered, built on Microsoft's Azure AI services, and gave varying answers, all signs of a generative system; for Moffatt, the record is silent (para. 14). Both stay inferred because generation is reported, not confirmed. A statement from the operator or vendor describing the model, or documentation of the system, would make it documented.
5. Open. Strong answers choose, for example, known-answer testing of policy answers before launch and after each change, and a rule that the policy page wins and the chatbot is corrected, with a reason tied to link 2 of the chain.

## Chapter 5

### Faded examples (self-check)
- **5.1 lab-safety summary.** C2 e.g., "every rule needed in the first week is included (checked against the sheet's first-week list)"; C3 "fits on one page, in the order of a lab session." Limits: no rules beyond the official sheet; no outdated versions. Stays with the student: choosing which rules apply in week 1, the final check against the sheet, telling new members to read the full sheet.
- **5.2 archive report.** (c) Augmentation, because the student keeps the thinking and decides on the wording (or the floor, if the seminar assesses that explanation). (d) Agency, and not the student's decision alone: the archive's visitors would bear errors, so archive staff need a check before answers reach them.
- **5.3 lab-report abstract.** Constraints e.g., "Report only results in the pasted report; give the key result with its number from Table 2; 150 words or fewer." Output format e.g., "One paragraph: purpose, method, key result, conclusion."
- **5.4 exhibit label.** v4: change the output format or a constraint, e.g., "60 words or fewer: one sentence on the artist, one on the work, one on why it matters." Prediction: C1 met; C2 and C3 still met.
- **5.5 survey question.** Two out of three is not enough: three runs of one question; criteria not written down; output 1 is closer but the agree/disagree form still invites agreement. Missing tests: other questions as test inputs (another leading question, an edge case such as a question that asks two things at once) and a peer swap.
- **5.6 fractions log.** v3 e.g., a constraint "Check each answer by working it a second way and show both lines"; prediction: wrong answers drop and are easy to spot. Part of C1 stays with the student: a person checks every key. Test inputs: typical (simple fractions), different (mixed numbers), edge (a fraction that simplifies to a whole number).

### Review Questions A
1. Goal, audience, success criteria, limits, and what stays with you (the A3 frame card adds a rung for each part).
3. *Automation:* you define a task, the AI carries it out, and you check the output. *Augmentation:* you and the AI shape and carry out the task together, turn by turn. *Agency:* you configure AI to carry out future tasks on your behalf, including for other people.
5. Agency is a way of working: you set AI up to act on future tasks for you. An agent is a kind of system in which the model directs its own steps and tool use. Example of agency that is not an agent: a course chatbot that answers students' questions from fixed instructions and a fixed source, without choosing tools or steps.
7. **(d)** In a test of four model families on 2,410 factual questions, adding a persona did not improve accuracy overall (Zheng et al., 2024); a role mainly sets tone. (a) and (b) are M1 (magic words); (c) overcorrects M1: a role does shape the output's voice.
9. **(b)** Each part should serve the task; irrelevant material can lower quality (Shi et al., 2023). (a) and (c) are M4 (more is always better; every prompt needs all six parts); (d) is M1 (a strong role as the key to good results).
11. **(d)** For GPT-4o the two wordings made no difference overall, though results on single questions changed both ways (Meincke et al., 2025a). (a) and (b) are M1; (c) is M5 (generalizing one summary result to every question and run).
13. What was in your head but not in the prompt: context, an audience or a meaning you take for granted, because you always read your own prompt with that knowledge.

### Review Questions B (model answers)
1. *Goal:* a one-page study sheet for an exam on heart medications. *Audience:* the student herself, a junior nursing student. *Criteria:* (1) every drug class and example matches the course textbook; (2) every dose or warning is copied from the textbook or a named reference, not generated; (3) one page, in a table (class, example, main action, key nursing check). *Safety criterion:* no patient information is used, and nothing is added that is not in the sources. *Limit:* only the assigned chapters. *Stays with her:* choosing what the exam covers, checking every drug fact against the textbook, and learning the material herself (consider augmentation in a tutor style, Chapter 7).
3. *Missing parts:* context (the internship's real facts and the readers, such as recruiters in her field), constraints (length; only facts given; no awards or numbers not supplied), output format (length, a LinkedIn-style structure). *Why-chain:* the post mentions an award → why? the prompt gave no facts about the internship, so the output filled in plausible ones → why? she expected the tool to know her experience (in her head, not in the prompt). *v2 (one change):* add context: three real accomplishments and the team's name. *Prediction:* the post uses only those facts; the invented award disappears. A constraint "use only the facts I give" is a good v3.

### Review Questions C (scoring guidance)
1. Strong answers separate "worked by the measures chosen" from "worked for customers": the 2024 measures were volume, speed, cost, a company-reported satisfaction score and a company claim of more accurate resolution shown by 25% fewer repeat questions, with no published method for accuracy (Klarna, 2024); in 2025 the chief executive was reported as saying cost had been too dominant and quality had suffered (Fisher, 2025). Using the chapter: success criteria decide what "worked" means, and with no check before each answer the measures carry more weight. Accept "agree" if it argues that the company's own data showed success and the change was strategic, provided it notes that all figures are company claims and the 2025 words are reported second-hand.
3. Strong answers give reasons tied to the chapter: criteria set by the instructor protect learning goals (the skill-building question in 5.2); criteria set by the student build judgment and fit the student's task; both together is common. Look for checkable criteria in the examples and attention to what stays with the student.

### Spaced Review
1. At each step a token is picked with some chance (sampling), so two runs can follow different paths. Step 5 of the iteration loop (rerun at least twice) allows for this.
3. A correction made in a conversation stays in that conversation's context; it does not change the model's settings. A fresh chat does not contain it (unless a memory feature adds a note), so the original prompt can produce the original error again (Chapter 3).
5. Frame, Prompt, Verify, Decide, Disclose. This chapter strengthened Frame and Prompt.

### Case Study Questions
1. *Conversations handled (2.3 million; two-thirds of chats):* volume, not whether problems were solved. *Work of 700 full-time agents:* the company's equivalence, not an outcome for customers. *Resolution time (under 2 minutes instead of 11):* speed, not correctness. *Satisfaction about the same as with human agents:* a company-reported score; it does not show who did not answer or who gave up. *More accurate resolution, shown by 25% fewer repeat questions:* the closest thing to a quality measure, but a company claim; the press release gives no method for accuracy (the 2025 SEC filing says the 25% compares repeat inquiries before and after launch). *$40 million profit improvement:* a cost forecast, not service quality.
3. *Confirmed:* the 2024 press-release figures; the January 2025 SEC filing (60% of chats, no drop in satisfaction by internal surveys, more accurate resolution, 25% fewer repeat inquiries). *Reported:* the May 2025 statements (via CX Today, Entrepreneur, heise); the November 2025 figures (853 agents, about $60 million, via CX Dive); the analyst's view. *Inferred:* the book's reading that this is a framing problem and that the place of the human check matters. Evidence that would change the view: an independent sample of conversations scored for whether problems were solved, or regulators' complaint data.
5. Example: quality suffered → why? the work was judged mostly on cost (checked: the CEO's reported statement, second-hand) → why? the announced measures were volume, speed, cost, one company-reported satisfaction score and a claim of more accurate resolution without a published method (checked: press release) → why? no direct count of problems solved or of customers who reached a person was published (assumed: the record does not show internal criteria). Credit for marking the last link assumed.

## Chapter 6

*Chapter 6 is optional and not examinable; these answers support practice.*

### Faded examples
- **6.1 A design student's style file.** Conversation so far: her three earlier messages and the tool's three replies, including her own draft tagline with "cheap." Most likely source: the conversation-so-far layer (her draft), not the project file, which bans the word. Change: start a new chat in the project, or tell the tool in the prompt that the banned-words list applies to all suggestions; check the project file still lists the word.
- **6.2 Five primary sources.** Include B (news report, 13 October 1918) second and E (editorial, 14 October 1918) third, labeled "EDITORIAL (opinion)"; exclude C (a 1919 notice, outside the week). Gap instruction: "If the passages do not say how a paper described something, say so; do not use other knowledge."
- **6.3 A jumbled context.** Order: HANDOUT §2 (goggles), HANDOUT §5 (storage), then a constraint line, then the full task last: "Summarize the safety rules for new lab members." Merge (1) and (5) into one constraint line: "Under 200 words, as a bulleted list."
- **6.4 Feedback examples.** Choose (4), a question that prompts revision: with (2) and (6) it covers correction, encouragement with a next step, and a prompt to think. Choosing (1) instead would push outputs toward praise without guidance (one-sided examples).
- **6.5 Where does it belong?** (4) this chat only; (5) never store; (6) project file for that course; (7) standing instructions; (8) this chat only.
- **6.6 Drug-leaflet template.** Different input: a leaflet for a drug with many warnings, or a leaflet in a different layout. Edge input: a leaflet with more than three warnings of equal importance, or a very short leaflet with one warning. Likely break: (a) (warnings reworded) or (b) (added advice). Change: "Copy warnings exactly as written; if there are more than three, list the first three and say how many more there are." Do not use for: patient-specific questions, dosing decisions, or anything involving patient data.
- **6.7 Report-summary chain.** Check: compare each extracted figure and its page number with the annual report itself, before Step 2. Pass criterion: every figure matches the page cited, with the same units and year.

### Review Questions A
1. (1) b; (2) d; (3) c; (4) a.
3. Context engineering is deciding what goes into a model's context window, from which layer, in what form and in what order, so that a task can be done well. Writing one prompt covers only one layer (your prompt); context engineering also covers selected documents, examples, standing instructions, project files, memory and the conversation so far.
5. Select excerpts, not whole documents (prevented an order priced from the old 2025 list being mixed in); name each excerpt's source and date (lets him check each price against a page). Also acceptable: the gap instruction (a missing part is reported, not invented).
7. **(c)** In-context examples steer the output only while they are in the context; the model's parameters do not change (Chapter 3). (a) and (b) are M3 (examples teach the model; more always helps); (d) is M5 (order sensitivity: Lu et al., 2022; Zhao et al., 2021).
9. **(b)** Five solved examples lowered o1-preview's MedQA score, unlike GPT-4's in 2023 (Nori et al., 2024). (a) and (d) are M3 (examples always help, or help newer models more); (c) is M3 in its "well-chosen examples are at least harmless" form: the study tested both random and similarity-chosen five-shot prompts, and the authors report that five-shot prompting lowered the score. Across benchmarks, few-shot was inconsistent and on average hurt.
11. "Does it belong in every chat, or only in one project?" flags it: a rule written for one task harms another (cost: invisibility). She should move the 50-word rule into the project or chats where it belongs, or delete it, and rerun the essay feedback.
13. A marked slot in a template that you replace with new material each time you use it, such as {NOTES} or {DATE}.

### Review Questions B (model answers)
1. *Layers:* standing instructions (a line such as "write formally" or "British spelling") — check the tool's options; project files or a style guide in a project — check the project; memory notes (for example, that she studied in the UK) — open the memory list, or check whether memory draws on past chats; the conversation so far (an earlier turn in British English) — start a fresh chat; pasted text written in British English — check what she pasted; the system prompt — she cannot see it, but a fresh chat with no standing context isolates it. *Method:* change one layer at a time and rerun the same prompt.
3. *Diagnosis:* the three in-context examples are one-sided (all written for A essays), so the outputs lean toward praise, like class imbalance in miniature (section 6.4). *Test:* three test inputs (typical: a B essay; different: a lab report; edge: an essay that misses the prompt), each run with balanced examples (one strong, one middling, one weak) and with no examples but clear criteria; score each output against two or three criteria (accurate, specific, actionable); keep whichever version meets the criteria more often, and record the test in a library entry.
5. *Chain:* Step 1, extract from each set of notes only the candidate's answers to each fixed question, with quotes; check: the intern (or a recruiter) compares the extraction with the notes, line by line; Step 2, summarize each candidate against the job's written criteria, with no scores; a person assigns any scores. *Why there:* errors in extraction (a misattributed answer) are cheapest to catch before they shape a summary, and scoring people is a decision that should stay with a person. *Never in context:* personal data that is not needed or that the organization's policy forbids sending to an AI tool, such as contact details, protected characteristics or medical information (Chapter 15; bias risk, Chapter 16).

### Review Questions C (scoring guidance)
1. Strong answers use the Case Study: the same kind of technique, five solved examples, helped GPT-4 in 2023 and lowered o1-preview's score in 2024 (Nori et al., 2024). That argues for libraries *with* versions, dates, model names and test records, so retesting is quick, not for abandoning them. Accept "agree" if it argues that very short-lived tasks do not repay the effort, provided it addresses the test-record argument.
3. Strong answers weigh section 6.7's reasons: a chain makes intermediate errors visible and puts a person's check where errors start (Wu et al., 2022), but adds time, and a single prompt that passes its test inputs is simpler. Good answers propose a rule by risk (chains with checks for documents where errors are costly or facts must be extracted; a single prompt plus a final check for low-risk text) and note that a chain does not check itself (M6).

### Spaced Review
1. The space for everything a language model receives in one turn, measured in tokens: a system prompt, the conversation so far, pasted or retrieved text and your prompt (plus, in many tools, standing instructions and project or memory text); the response also counts toward it. In a 2023 test, information in the middle of a long input was used less reliably than at the start or end (Liu et al., 2024).
3. The three test inputs may share a feature that makes the template look right for an unrelated reason, for example notes that all happen to list decisions in the order the template expects. A new kind of input breaks it. Choosing a truly different and an edge input, and retesting on new inputs over time, reduces this risk.
5. Someone else runs your template on their own input without your explanation and scores the output against your criteria (Chapter 5). It shows what was in your head but not in the template, such as an audience or a term you take for granted, before others rely on it.

### Case Study Questions
1. *What the model received:* in-context examples (random, then chosen by similarity); step-by-step reasoning GPT-4 had written for those examples, which also led GPT-4 to write its own reasoning before each answer. *How the task was run:* five runs and a majority vote. Accept answers that note the shuffled answer options also change the prompt; the purpose of that step is the vote.
3. Fields that would have warned: "tested on" (GPT-4, November 2023, MedQA only); "in-context examples: used, and the test that decided" (helped on GPT-4); "when not to use" (other models untested). A 2024 retest on o1-preview with and without examples would have shown the reversal.
5. *Should:* note that the authors are mostly Microsoft researchers studying OpenAI's models, with one OpenAI co-author in each paper, and that Microsoft is a major investor in OpenAI and sells its models through its cloud service; read the results as these authors' benchmark results and look for independent replication. *Should not:* dismiss the findings because of affiliation; the method, data and limits are published and can be checked.

## Chapter 8

### Faded examples (all answers)
- **8.1 Steel paragraph.** Remaining claims: (4) A36 is the cheapest choice for small brackets (checkable, but depends on time and supplier; medium); (5) it is easy to weld (checkable; medium); (6) most student teams should use it (recommendation, not checkable as true or false; low to medium). Highest stakes: the yield strength and its unit conversion, if they feed a load calculation.
- **8.2 Drug interaction.** Stage 3 is needed when the claim will guide a decision for a real patient (dose, timing, whether to combine the drugs), because applying it takes clinical judgment; for a study note, stage 2 is enough. Verdict: supported. Uncertainty: "Not reviewed by a pharmacist; true in general, not checked for a specific patient."
- **8.3 Enron paragraph.** Reference 2: checks 1 and 2 (stage 1) show failure 2: the real article is Healy & Palepu (2003), *Journal of Economic Perspectives*, 17(2), 3–26, so the year and journal in the output are wrong. Verdict: contradicted as cited; correct the reference from the record before use. Reference 3: not found in the library catalog or a scholarly search engine, and the journal itself cannot be found. Verdict: unsupported; uncertainty line: "Not in [catalog] or [search engine]; journal not found; may be fabricated; not cited." (It is constructed and matches nothing real; checked October 2026.)
- **8.4 Quotation.** Next stage: 2, the primary source (the speech, letter or document itself, or a scholarly edition of the person's words), because a quotation needs the passage check, and famous quotations are easy to misattribute.
- **8.5 Lucía's study questions.** Share correct in the 90–100% group: 4 of 7 = 57%. Gap: 94 − 57 = 37 points. It tells her the tool's high confidence on accounting questions is overconfident; she should check its answers against the answer key, and remember that seven answers give a rough picture.
- **8.6 Half-filled row.** Verdict: supported (the official frequently asked questions page and the state board's scoring page give 75 on a 0–99 scale). Uncertainty: "75 is a scaled score, not a percentage correct; checked October 2026." The tool's gap: 93 − 50 = 43 points.

### Review Questions A
1. A claim is one statement in an output that you might rely on. Example of one not checkable as true or false: a recommendation such as "You should start with the hardest section," or a prediction.
3. Independent check, primary source, expert; the expert is the person.
5. **(d)** Checks follow the stakes; every claim you rely on gets at least stage 1. (a) is M6 (verifying means checking everything as far as possible); (b) is the fluency trap from Chapter 1, which M1 extends (a claim that sounds right is not thereby supported); (c) is M2's mirror image: numbers and dates are among the claims that most need the primary source.
7. **(c)** It may not exist or may be another work; match each detail to the record. (a) and (d) are M2 (a named source is a pointer, not evidence); (b) is M3 (the tool's yes, even with a journal name, is not a check).
9. **(d)** The answer comes from the same kind of process that produced the source, not from evidence outside it. (a) is M3 (a tool's yes, even with search, is not a source; open what it found); (b) is M2 (a link is a pointer until you open it); (c) is M4/M5 (trusting a newer model's word instead of evidence).
11. The flip shows the answer is unstable, a warning sign; it does not show which answer is right, since you have not checked either. Next: take the claim through the funnel (at least stage 1, stage 2 if the stakes are high). Had the tool held firm, that would have been no evidence either way.
13. **(b)** Probably fewer than 18; check the high-stakes answers. Published tests found stated confidence often ran ahead of accuracy while still rising with it. (a) is M5; (c) overcorrects (higher confidence did go with more right answers); (d) reverses the finding (confidence and accuracy rose together).

### Review Questions B (model answers)
1. Claims: (1) Gen Z spends an average of 7.2 hours a day on social media (number; checkable; high stakes); (2) the figure comes from a 2024 Pew Research Center report (citation; checkable; high: go to Pew's own report, the primary source, and find the figure); (3) brands should move all their budget to TikTok (recommendation; not checkable as true or false; it does not follow from claim 1 and needs evidence about returns, not usage). Rank 2 and 1 highest, because a client presentation will repeat them; flag 3 as a judgment. Full credit: three claims, correct marks, a ranking with reasons. (The example is constructed; the key does not say whether Pew reported this figure.)
3. Checks in order: does it exist (library catalog or publisher's site; stage 1), does every detail match (author, title, publisher, year; stage 1), does page 214 contain the quotation (open the book; stage 2). (a) The book exists and matches but the page does not contain the quotation: unsupported for the quotation (contradicted if the page says the opposite); failure 3. (b) A book of that title exists by a different author: the citation's details belong to another work, so it is contradicted as cited (failure 2); then check whether the real book contains the quotation. (c) The book appears in no catalog: unsupported, with the catalogs searched named in the uncertainty line; it may be fabricated; do not cite it.

### Review Questions C (scoring guidance)
1. Open. Strong answers take a clear position, use the Ethics Lens (checking is cheap for the writer and expensive for those downstream) and the stopping rule (stakes decide the stage), and give one example, such as a citation in a court filing or a dose in a patient leaflet, where the reader bears the cost and the writer's check must go further. Weak answers say "always check everything" or "only check when you have time."
3. Open. Strong answers use the stopping rule: low-stakes claims stop at stage 1, so checking need not take longer than writing; high-stakes claims need the primary source either way, because writing them yourself would also require it. A strong answer estimates the time for a real task in the student's field and names which claims drive the cost. Weak answers ignore stakes.

### Spaced Review
1. Hallucination, leaf "invented facts or sources." Usually extrinsic: the user's input can neither support nor contradict it; it would be intrinsic only if it contradicted a source list the user supplied.
3. In A4 you calibrated your own confidence: your predicted closed-book results against your actual results. In A5 you measure two gaps: your own confidence and the tool's stated confidence, each against the verdicts. The habit is the same: predict, then check.

### Case Study Questions
1. Hallucination, leaf "invented facts or sources," documented: the record shows the six decisions do not exist and were generated by ChatGPT (¶ 36). Overconfidence, leaf "certainty beyond the evidence," documented: asked directly, the replies affirmed that the authorities were real and findable in named databases, and, by the lawyer's account, insisted again that "Varghese" existed (¶¶ 45, 47; the second is reported).
3. Stage 1 would have flagged it: the lawyer's own search found nothing (¶ 12); one more index would have made the verdict unsupported, and a court filing cannot rest on an unsupported citation. Stage 2 would have made it contradicted: the court's records hold no such case, and the Federal Reporter citation and docket number belong to other cases (¶¶ 26, 28).
5. Mata: *Verify* (open every citation in a legal research database before filing) and *Decide* (the lawyer who signs reads the authorities). Reading list: a stage-1 catalog search for each title and an editorial review before publication; the newspaper said the insert ran without review by its editors. They differ because in Mata a search did give a warning that was ignored, and the lawyers then defended the cases; in the reading list, the workflow had no review step at the point of publication.

## Chapter 7

### Review Questions A
1. *Performance:* how well you do a task while practicing, often with help. *Learning:* a lasting change in what you can do without help, shown later and in new situations.
3. +10 percentage points (from 20 to 30); a relative increase of 50% (10 ÷ 20).
5. **(d)** After a week, the group with one study period and three recalls remembered the most (61%, vs. 40% for four study periods). (a) is M2 (more exposure feels like more learning; rereading won only at 5 minutes); (b) is M3 (feeling prepared taken as being prepared); (c) is M2 (methods that feel equally useful taken as equally effective).
7. **(c)** A difficulty is desirable if you can meet it with effort (Bjork & Bjork, 2011), and guessing before study helps if you then see the answer (Kornell, Hays & Bjork, 2009). (a) and (b) are M2 (struggle means you are doing it wrong; ease means it is working); (d) is M1 (practice scores taken as the measure of learning): desirable difficulties often lower performance during practice.
9. **(a)** Students learned more in active classes but rated their learning lower; the authors suggest they took the extra effort as a sign of poor learning (Deslauriers et al., 2019). (b) reverses the finding (M3); (c) is M3 (students judge their own learning accurately); (d) is M2 (enjoyable, easy-feeling work taken as effective).
11. Ask of each turn: who produced the answer in this turn: you, from your own memory, or the tool? A request that sets up your own attempt is S; a request for the answer is C. (Feedback is S only after an attempt at the same question.)
13. GPT Tutor's instructions also contained the teachers' worked solutions and an instruction to give hints instead of the answer. Calling GPT Base a tutor did not keep students working; withholding answers kept the recalling and producing with the student, and the supplied solutions made its feedback accurate.

### Review Questions B (model answers)
1. The claim shows performance with the helper: homework done while the tool was available. It does not show learning, which needs a later check without the tool. Ask for closed-book test scores taken later, a comparison group that did the same homework without the tool, random assignment, and who measured the scores.
3. (1) **S**: the student attempted (friction direction) and asks for feedback on that attempt; (2) **S**: the tool's question sets up the student's reasoning; (3) **S**: the student produces the fix; (4) **C**: a request for the answer with no attempt; (5) **C**: the tool answers a question the student did not attempt.
5. Right after: predicted 3.0, actual 3, gap 0 (calibrated), though an immediate score measures short-term performance. Two days later: predicted 3.0, actual 1, gap +2.0 (strongly overconfident): what she could do right after did not last, or did not carry over to parallel questions. Change: add spaced retrieval (self-tests after one and three days, on varied questions) and predict more cautiously.

### Review Questions C (scoring guidance)
1. Strong answers take a position and use evidence: GPT Tutor showed no measurable harm but did not raise exam scores (Bastani et al., 2025); structured tutors produced gains in short studies (Kestin et al., 2025; De Simone, Tiberti, Barron Rodriguez, et al., 2025). They name at least one limit of tutor mode (answer mode is one request away; the tool can be wrong or agree with wrong attempts; good scaffolds need expert material). Strong "disagree" answers note that some tasks are not about building a skill (Chapter 5's third question).
3. Strong answers use what each study measured and cannot tell: short studies of single subjects; designs that depended on teachers' or experts' solutions (labor that is part of teaching); a working paper with high attrition. A strong position separates "AI can do parts of tutoring well in some conditions" from "replace teachers." Weak answers cite one study as proof.

### Spaced Review
1. Example: "After the session, I can answer all three keyed check questions closed-book, scored against the textbook key." It is checkable because the key decides each answer.
3. The model scores possible next tokens by patterns in its training text and picks among them; nothing in that process checks whether the result is true, so fluent text can be false (Chapter 3, section 3.2).

### Case Study Questions
1. The control group practiced the same problems with their course books and notes, without devices; the exam was the third part of the same 90-minute session, closed-book and closed-laptop. The first detail means the comparison is with normal, active practice, not with no practice; the second means the study measured short-term learning only.
3. Accept reasoned rankings. A common strong answer: the Türkiye study is the strongest design (classrooms assigned by a balancing procedure, preregistered outcome, about 1,000 students, peer-reviewed), but none measures long-term learning; Harvard is randomized and peer-reviewed but covers two lessons with immediate tests; Nigeria runs longest (six weeks) and reports a school exam, but randomized only volunteers, lost many students before the final assessment, bundles the tool with a program and is a working paper.
5. In the output: GPT Base's answers were often wrong (correct only 51% of the time when asked for the answer). In the use: students copied answers instead of attempting the problems (overreliance, section 7.1). The difference matters because a student cannot fix a tool's errors but can change how she uses it: attempt first, keep the source open, check without the tool.

### Faded examples and Your Turn
- **7.1 Language app:** closest to learning = the paper quiz a week later (61% vs. 64%); the 85% and 70% cannot be compared because they were measured under different conditions (inside the app with hints vs. on paper without).
- **7.2 Marcus's plan:** lecture recording → pause before each segment and recall the main point, then check; highlighting → redraw the summary table blank and fill it from memory, then check; the night before → three short sessions spread around his shifts.
- **7.3 Business calibration:** actual score 2 of 3; gap 2.55 − 2 = +0.55, so the student is overconfident overall (by about 18 percentage points); the gap comes mostly from question 3 (85% confident, wrong), a "why" question that asks for an explanation, not a definition.
- **7.4 Marcus's dialogue:** turn 4 **S** (after his request to attempt, the tool sets up his attempt); turn 5 **S** (he produces an answer and reasoning); turn 6 **S** (asks him to explain, which sets up more producing). Accept other codes only if the reason applies the 7.4 rules.
- **7.4 Your Turn (break-even):** (1) **C**: a request for the answer, no attempt; (2) **S**: sets up the student's attempt; (3) **S**: the student produces an answer; (4) **S**: feedback ("Yes") after an attempt at the same question, then a new problem that sets up an attempt; (5) **C**: a request for the answer; (6) **C**: answers a question the student did not attempt. Accept either code for (4) if the reason applies the rules.
- **7.5 Chemistry setup:** missing (1) the attempt-first constraint ("Ask me to try each step before you explain it; no full answer unless I ask after two attempts"), in Constraints; (2) the source to check against ("I will check your explanations against my textbook's chapter on stoichiometry"), in Context. "If my answer is wrong, say so" is a good addition.
- **7.6 Annotation sheet:** turn 5 **C** because she asks the tool to produce the list she needed to recall; turn 8 **C** plus a factual error: she copied the tool's dates without attempting or checking. She should check the dates in her textbook, correct her notes, mark the error in the annotation and save it for her Failure Diary.

## Chapter 9

### Review Questions A
1. **(a)** A court's record is primary for what the court said; a report quoting it is secondary. (b) M8: a story that reports a study is not its record; (c) M1: reputation does not make a source primary; (d) M8: type depends on the claim.
3. **(d)** Find a reviewed version, compare conclusions, and say it is a preprint. (a) M2: preprints can be cited with care; (b) M1: reputation is not a check; (c) M6: a tool's ranking is not evidence.
5. **(b)** Searching for what outside sources say about who runs the site. (a) and (c) M3: vertical reading; (d) M6: a tool's answer is a lead, not a source.
7. **(c)** A systematic review that pooled many trials: for "what studies show," it is the record of the claim (rung 4). (a) M7: one experiment records a narrower part (rung 3); (b) M1: a mention borrows a review's authority but names it too vaguely to find (rung 2); (d) M6: AI output is below the ladder.
9. **(a)** Unsupported: no evidence for it at the stage reached. (b) M4: repetition is not a record; (c) Chapter 8 verdict scale: contradicted needs evidence that says otherwise; (d) Chapter 8 verdict scale: "cannot verify" means the evidence may exist but you cannot reach it.
11. **(d)** Both AI summaries and press releases often overstated studies in tests. (a) M5; (b) M5 in reverse: Sumner et al. (2014) found exaggeration in press releases; (c) Peters and Chin-Yee (2025) found newer models tended to overgeneralize more (as of 2025).
13. **(b)** Check each source's rung and whether it says what its sentence claims. (a) M1: volume is not quality; (c) M6: a tool's own "yes" is never a source (Chapter 8); (d) M1: well-known names are cues, not checks.
15. **(c)** Use it with a caveat or as a lead, and look for an outside record. (a) M1: the rung alone does not justify "rely on it"; (b) M1 reversed: funded sources can be used with care; (d) M9: who is behind a source does not change its rung.

### Review Questions B
1. A manufacturer's white paper is gray literature, not peer-reviewed, paid for by the company that sells the battery. It is the record (rung 4) of what the manufacturer claims or specifies, such as its stated lifetime under its own test conditions; for "how long the battery lasts in independent use" it is not the record, and an independent test report or study is needed. Its funding feeds the use decision (use with a caveat). Full credit: type, status, who paid, one claim it records and one it does not.
3. Hop 1, blog → exhibition catalogue: does the catalogue exist, do the details match, does it say $2 million in 1910? Hop 2, catalogue → auction record: does the record exist (the auction house's archive or a published sale record), and what does it say: price, currency, date, which painting? Drift is most likely a changed number (a price converted to today's dollars or another currency, or a wrong year) or a misattributed painting. The verdict follows Chapter 8's rule; if the auction record cannot be found, the claim is unsupported.
5. Types: three company blogs (gray literature, written by interested parties; rung depends on what they cite), two news stories (rung 2 or 3), one survey by the tool's own provider (gray literature with a conflict of interest). Support: check that each cited page says what its sentence claims. Missing evidence: peer-reviewed studies, primary datasets, counter-evidence, dates. Faithfulness: compare the report's conclusions with what the sources say. Strong answers conclude that the report is a starting list, not evidence.

### Review Questions C
1. Strong answers argue for both, with different checks: the firm, as author, opens every reference and traces legal quotations to the court's record; the client, before publishing, runs an acceptance check (for example, a sample of references) proportional to the stakes, which were high because the system affects people's payments. They use the Case Study accurately: the errors reached the published report (documented); what checks ran is not on record (inferred). Weak answers blame "the AI".
3. Open. Strong answers separate roles: the writer or publisher of a summary is responsible for checking it against the study (Sumner et al., 2014: press releases were drafted by press officers with scientists approving them); the provider of an AI tool is responsible for how the tool is designed and described; the person who publishes or relies on an AI summary is responsible for checking it (Peters & Chin-Yee, 2025). They avoid attributing intent to the tool.

### Spaced Review
1. Stop when the evidence matches the stakes (Chapter 8). The rung you need applies the same idea to sources: higher stakes call for a source higher on the ladder, often the record itself.
3. Hallucination, leaf "invented facts or sources", inferred: the reference is shown to be wrong, but no record shows that it was generated. Chapter 4 used the same reasoning for the Air Canada chatbot (Moffatt).

### Case Study Questions
1. Commissioned gray literature; the report itself calls the work advisory, not an audit. It is a primary source (the record) for what the department was told by its reviewers.
3. The department, as publisher, settles the publication date (August 14, 2025, in its statements); the report's cover settles the report's own date (July 4, 2025). The Associated Press is a secondary source for both.
5. Find out which version you read and what changed in the later versions; check whether the passages you relied on were affected; cite the version you used with its date, or switch to the current version; and, if you used one of the report's references, open that reference yourself.

### Faded examples (self-check)
- **9.1 Marcus:** item 2, a newsletter quoting "a recent study" without naming it: rung 2; does not meet rung 3. Item 3, a blog with no sources: rung 1; does not meet it.
- **9.2 LK-99:** step 2: later replication work and *Nature*'s reporting concluded that LK-99 is not a superconductor (Garisto, 2023b); a claim this large needs reviewed confirmation, and none supported it. Step 3: check the preprint pages for revised versions or withdrawal notes, and the authors' own statements; until then, describe the claim as unconfirmed.
- **9.3 history institute:** step 2: search the institute's name in a library database or a scholarly search engine; if no historian or archive cites it, use it only as a lead, or not at all. Step 3: a scholarly history of the treaty, or the treaty text in an archive or official collection.
- **9.4 startups:** step 2: the Bureau of Labor Statistics measures how many new establishments (locations, not firms) are still operating after a given number of years; a closure is not always a failure (a business can be sold or merged). Step 3: the verdict depends on the table: often partly supported, because "most fail" overstates what survival data show; write the claim with the dataset's definition and figure.
- **9.5 Marcus:** sentence 2: contradicted (the original says the rise was larger in urban counties); the verdict is enough. Sentence 3: unsupported; drift: cause from correlation (the report shows a rise, not what caused it).
- **9.6 readmissions:** source 2: rung 2 (too vague to find), so it cannot support the claim: unsupported. Source 3: the dataset does not hold the claim (no data on phone calls), so it does not support it; it can support background facts about readmission rates. Step 4: trials in other hospitals, a systematic review, counter-evidence and dates.
- **9.7 Marcus, error 2:** open the article; if it exists and supports his sentence, read it and cite it; if not, remove the citation and the claim, or find a source he has read. His declaration says he used an AI answer to find sources and checked every one.
- **9.8 caffeine report:** step 2: if the cited study measured exam scores, the report is rung 3 for the claim; if it measured something else (for example, alertness), rate the report as if that citation were missing (rung 1 for this claim). Step 3: for example, a news story or a lobbying register that describes the association's membership and funding. Step 4: use with a caveat or only as a lead; cite the studies themselves if they hold the claim.
