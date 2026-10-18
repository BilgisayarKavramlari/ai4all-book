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
