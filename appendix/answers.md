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
