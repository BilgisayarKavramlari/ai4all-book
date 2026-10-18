# Case: The Reversal Curse — models trained on "A is B" fail on "B is A" (2023; published 2024)

Chapter: 3 (Opening Case and main Case Study) · Field: AI research / general knowledge · Failure label (Signature 5): primary **hallucination**, inferred (dashed); no secondary branch · Outcome: research finding (no harm reported)

## Context
By 2023, many people were asking chat tools based on large language models factual questions. Seven researchers tested whether a model trained on a statement in one direction ("A is B") can answer the reverse question ("B is A"). The case is known from the paper itself (Berglund et al., 2024); the book uses only what the paper states and marks its own reasoning as such.

## Timeline
- June 28, 2023: access date of the list of the top 1,000 celebrities (a film database) used in the second test.
- September 21, 2023: first arXiv version (2309.12288); revised versions to May 26, 2024 (v4).
- 2024: published in the proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024).

## What the AI did
- **Test 1 (invented facts).** GPT-3 base models (350 million to 175 billion parameters) were fine-tuned on invented "name is description" facts (three subsets of 30 base facts; the main text says 30 facts), each paraphrased 30 times (for example, a made-up person is the director of a made-up film). In the trained direction, GPT-3-175B scored 96.7% (description → name) and 50.0% (name → description) exact match (Table 1). In the reverse direction, the largest GPT-3 model scored 0.0% and 0.1% exact-match accuracy in the two reverse tests; the likelihood of the correct name was not significantly higher than that of a random name. A Llama-7b sweep is reported in an appendix.
- **Test 2 (real celebrities).** For the top 1,000 IMDb celebrities, GPT-4 was asked for each one's mother and father; it identified the parent 79% of the time, giving 1,573 child–parent pairs (1,573 is about 79% of 2,000 questions; the paper does not state 2,000). All 1,573 pairs were reversed ("Name a child of [parent]"). GPT-4 was correct 33% of the time, counting a success if any of 10 tries named the celebrity (footnote 11). The note to Figure 5 gives 28% without explanation; the book uses the text's 33%. GPT-3.5-turbo and Llama-1 base models were also much better at the parent direction (values only in Figure 5). The paper gives no GPT-4 snapshot name or query date; the book prints "GPT-4 (2023)".
- **Limit.** When "A is B" appears in the prompt (in context), models can answer "B is A"; with 3-shot prompting GPT-3 models reached 96.67–100% on reversed facts (appendix B.6).

## What humans did
The researchers designed both tests, used invented facts so that no model could have seen them in pretraining, compared the likelihood of the right name with random names, and released their code (https://github.com/lukasberglund/reversal_curse). No product decision or harm is involved.

## Mapped to Signature 4 (Anatomy of an LLM Response; figure F3.3)
- **Training (section 3.3):** in test 1, fine-tuning raised scores for continuations in the trained direction only. For the real-world test, the authors hypothesize that pretraining data contains fewer examples in which the parent precedes the celebrity (paper, section 1.1; section 4.1 notes that mentions are long-tailed). They also raise a separate possibility: GPT-4 may have been tuned to avoid revealing information about individuals and may over-apply this to parent questions (section 2.2). Untuned Llama-1 base models showed the same gap, which weakens that explanation. The general explanation in the chapter is the book's simplified reading.
- **Scores (section 3.2):** at inference, the score for the right name in the reverse direction was no higher than for a random name (test 1).
- **Context window (section 3.4):** with the fact in the prompt, the reversal works.

## Failure label (Signature 5; figure to be imported from figures/scripts/ch04_figures.py `failure_tree` once Chapter 4 exists)
- Primary: hallucination — **inferred (dashed)**. Documented: failures to give the correct answer in the reverse direction. Inferred by the book: that a share of the wrong answers were fluent invented names rather than non-answers (the paper does not break this down).
- Secondary: none.
- **Student-facing:** per the book-wide rule (tree labels start in Chapter 8; Chapter 3 is read before Chapter 4), the chapter describes the failure in plain words and points to Chapter 4. Chapter 4 or 8 may reuse this label.

## Consequences (documented only)
A research result, not an incident. No harm to any person was reported. The models tested were those available in 2023; newer models and tools that search may behave differently (refresh-list entry). The paper's best-known example is now widely repeated online, so a correct answer from a current tool may come from new training text; the lab uses less famous pairs.

## A better workflow (AI Work Loop)
Frame: a reverse lookup ("whose son is this person?", "which drug has this brand name?") is a task where a model may fail even when it succeeds in the other direction. Prompt: if you have the source fact, put it in the prompt. Verify: ask in both directions and check against a reliable source. Decide: rely only on the checked answer. Disclose: note the tool and how you checked.

## Questions
See the Chapter 3 Case Study Questions (five items).

## Privacy note
The paper's best-known example names a celebrity's mother, a private person. The book names neither her nor the celebrity.

## Sources
1. Berglund, L., Tong, M., Kaufmann, M., Balesni, M., Stickland, A. C., Korbak, T., & Evans, O. (2024). The reversal curse: LLMs trained on "A is B" fail to learn "B is A". ICLR 2024. https://proceedings.iclr.cc/paper_files/paper/2024/hash/5178b2f2d7c44aa390c0777dc77b3f0c-Abstract-Conference.html — primary; read via arXiv abstract and HTML v4 (https://arxiv.org/abs/2309.12288, https://arxiv.org/html/2309.12288v4), accessed 2026-10-18.
2. ICLR 2024 poster page, https://iclr.cc/virtual/2024/poster/19033 — venue confirmation, accessed 2026-10-18.
