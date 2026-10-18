# Case: Medprompt — same model, different context and steps (2023–2024)

Chapter: 6 (Opening Case and main Case Study) · Field: health / medical education benchmarks (research) · Failure label: **2023 result: none on the tree** (a positive benchmark result; no output failure is documented). **2024 reversal: "other" leaf, dashed (inferred)**: a context design (five in-context examples) that lowered accuracy on a newer model; no branch of the tree fits cleanly (editor decision, 2026-10-18) · Outcome: positive (2023), mixed (2024: examples hurt; ensembling still helped)

Student-facing text (Chapter 6) does not use Signature 5; tree labels for students start in Chapter 8 (reading order). The short cases in Chapter 6 name "context loss" in plain words with a forward pointer to Chapter 4, section 4.4.

## Context
MedQA is a public benchmark of four-option multiple-choice questions in the style of the U.S. Medical Licensing Examination. In November 2023, Microsoft researchers studied how far GPT-4 (OpenAI) could be steered on medical benchmarks by prompting alone, without fine-tuning (Nori et al., 2023). In November 2024, a team with the same lead author (Microsoft, with one OpenAI co-author) repeated the exploration with o1-preview, an OpenAI model designed to produce reasoning before its final answer (Nori et al., 2024).

## Timeline
- November 2023: arXiv:2311.16452v1, "Can generalist foundation models outcompete special-purpose tuning? Case study in medicine" (Nori et al., 2023).
- November 6, 2024: arXiv:2411.03590v1, "From Medprompt to o1" (Nori et al., 2024).

## What the AI did (as reported by the authors)
- 2023, MedQA, GPT-4, cumulative steps in the authors' order (Figure 4): zero-shot 81.7% (prior work reported in the paper) → five random solved examples 83.9% → plus GPT-4's self-generated chain-of-thought for the examples 87.3% → examples chosen by k-nearest-neighbor similarity 88.4% → five-run choice-shuffle ensemble with majority vote 90.2%. Figure 6 of the same paper labels the increments +2.2, +3.4, +0.8, +2.1 (the last two differ slightly from Figure 4's printed accuracies); the authors call the ordering subjective. 90.6% with 20 examples and 11 ensemble runs. No fine-tuning; prompting does not change model parameters.
- Self-generated reasoning: GPT-4 wrote chain-of-thought for training questions; samples whose answer did not match the label were discarded. Versus expert-written reasoning with fixed five-shot examples and no ensemble: 86.9% vs. 83.8% (Table 2).
- 2024, o1-preview (zero-shot) 96.0% on MedQA, vs. 90.2% for GPT-4 Turbo with Medprompt (Table 1). Five-shot prompting "resulted in a significant decrease" on MedQA (Figure 5); across benchmarks, few-shot was inconsistent and on average hurt; ensembling gave consistent gains at higher cost (Nori et al., 2024). Exact few-shot accuracies are shown only in figures [not quoted in the book].
- The 2024 paper publishes its prompt templates with placeholders in braces ({examples}, {question}, {answer choices}) (Figure 9).

## What humans did
- Designed the context (example selection, self-generated reasoning) and the workflow (shuffled runs and vote); reported limits: possible memorization or leakage of benchmark items; benchmark scores do not show real-world clinical efficacy; multiple-choice exams do not capture clinical work (Nori et al., 2023).
- 2024: noted that benchmarks such as MedQA are near saturation or their noise ceiling and called for harder benchmarks (Nori et al., 2024).

## Mapped to the Context Layers (Chapter 6)
Prompt layer: in-context examples chosen per question, with self-generated reasoning (context engineering). Outside the context: a workflow of five runs with shuffled options and a vote (section 6.7). Model settings: unchanged.

## Consequences (documented only)
A widely cited demonstration that prompting strategies could raise a general model's benchmark score to the level of specially tuned models in 2023; a 2024 follow-up showing that one of those strategies (few-shot examples) did not transfer to a reasoning model. No clinical deployment is claimed by the authors or by the book.

## A better workflow (AI Work Loop) — for a reader reusing such a design
*Frame:* what is the task, and is a benchmark score evidence for it? *Prompt:* treat the design as a template with a version, a date and the model it was tested on. *Verify:* rerun the test inputs, with and without examples, whenever the model changes. *Decide:* keep only the components that still help. *Disclose:* report the model, date and benchmark limits with any result.

## Questions (4–6)
See the chapter's Case Study Questions 1–5.

## Sources (at least 2, one primary; with access date)
1. Nori, H., Lee, Y. T., Zhang, S., et al. (2023). *Can generalist foundation models outcompete special-purpose tuning? Case study in medicine* (arXiv:2311.16452). https://arxiv.org/abs/2311.16452 (accessed 2026-10-18; PDF v1 read: Table 1, Figures 4 and 6, Table 2, section 5.2, limitations).
2. Nori, H., Usuyama, N., King, N., McKinney, S. M., Fernandes, X., Zhang, S., & Horvitz, E. (2024). *From Medprompt to o1: Exploration of run-time strategies for medical challenge problems and beyond* (arXiv:2411.03590). https://arxiv.org/abs/2411.03590 (accessed 2026-10-18; PDF v1 read: abstract, Table 1, Figures 5–6, Figure 9).
