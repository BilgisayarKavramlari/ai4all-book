# Case: Medprompt — same model, different context and steps (2023–2024)

Chapter: 6 (Opening Case and main Case Study) · Field: health / medical education benchmarks (research) · Failure label: **2023 result: none on the tree** (a positive benchmark result; no output failure is documented). **2024 reversal: "other" leaf, dashed (inferred)**: a context design (five in-context examples) that lowered accuracy on a newer model; no branch of the tree fits cleanly (editor decision, 2026-10-18) · Outcome: positive (2023), mixed (2024: examples hurt; ensembling still helped)

Student-facing text (Chapter 6) does not use Signature 5; tree labels for students start in Chapter 8 (reading order). Short case 2 in Chapter 6 names "context loss" in plain words with a forward pointer to Chapter 4, section 4.4.

Attribution tiers: all facts below are **confirmed** from the two papers (primary records) unless marked **reported** (named outlet or person) or **inferred** (this book's reading).

## Context
MedQA is a public benchmark of four-option multiple-choice questions in the style of the U.S. Medical Licensing Examination. In November 2023, Microsoft researchers studied how far GPT-4 (OpenAI) could be steered on medical benchmarks by prompting alone, without fine-tuning (Nori et al., 2023). In November 2024, a team with the same lead author repeated the exploration with o1-preview, an OpenAI model designed to produce reasoning before its final answer (Nori et al., 2024). Both papers list one co-author at OpenAI (Scott Mayer McKinney); the other authors are at Microsoft.

## Timeline
- November 2023: arXiv:2311.16452v1, "Can generalist foundation models outcompete special-purpose tuning? Case study in medicine" (Nori et al., 2023).
- November 6, 2024: arXiv:2411.03590v1, "From Medprompt to o1" (Nori et al., 2024).

## What the AI did (as reported by the authors)
- 2023, MedQA, GPT-4, cumulative steps in the authors' order (Figure 4, the step-by-step chart): simple prompt, no examples 81.7% → five random solved examples 83.9% → plus GPT-4's self-generated chain-of-thought for the examples 87.3% (with these examples, GPT-4 also wrote its own reasoning before each answer; the previous step answered with a single token) → examples chosen by k-nearest-neighbor similarity 88.4% → five-run choice-shuffle ensemble (sampling at temperature > 0) with majority vote 90.2%. Figure 6 labels the increments +2.2, +3.4, +0.8, +2.1 (the last two differ slightly from Figure 4's printed accuracies); the authors call the ordering subjective. 90.6% with 20 examples and 11 ensemble runs. No fine-tuning; prompting does not change model parameters.
- Internal mismatch, not reconciled in the paper: Table 1 lists GPT-4 five-shot at 81.4% (from earlier work), while Figure 4 lists random five-shot at 83.9%; the earlier study reported 78.9% zero-shot. The book uses Figure 4 and says "in the paper's step-by-step chart".
- Self-generated reasoning: GPT-4 wrote chain-of-thought for training questions; samples whose answer did not match the label were discarded. Versus expert-written reasoning with fixed five-shot examples and no ensemble: 86.9% vs. 83.8% (Table 2).
- 2024: o1-preview (zero-shot) 96.0% on MedQA in Table 1, vs. 90.2% for the Medprompt column (Table 1 labels it GPT-4 Turbo; the 90.2% is the 2023 GPT-4 result); Figure 5 shows about 94.9% for the minimal prompt and about 95.7% at best, so the book says "about 95–96%". Components were tested one at a time. Five-shot prompting (question and answer only, Figure 9 template, random or kNN-selected) "resulted in a significant decrease" on MedQA (Figure 5); across benchmarks, few-shot was inconsistent and on average hurt; ensembling gave consistent gains at higher cost. The authors suggest the examples "may have confused" the model. A Japanese licensing exam given after the model's knowledge cutoff (JMLE-2024) was used to address contamination.
- The 2024 paper publishes its prompt templates with placeholders in braces ({examples}, {question}, {answer choices}) (Figure 9).

## What humans did
- Designed the context (example selection, self-generated reasoning) and the workflow (shuffled runs and vote); reported limits: possible memorization or leakage of benchmark items; benchmark scores do not show real-world clinical efficacy; multiple-choice exams do not capture clinical work (Nori et al., 2023).
- 2024: noted that MedQA "might have reached" its noise ceiling and that benchmarks are near saturation; called for harder benchmarks (Nori et al., 2024).

## Interests
Microsoft is a major investor in OpenAI and offers OpenAI's models through its cloud service (OpenAI, 2023, "OpenAI and Microsoft extend partnership"; confirmed for the investment and Azure OpenAI Service). Both papers study OpenAI models; each lists one OpenAI co-author. Reading the results as these authors' benchmark results, not general facts about medicine, is **inferred** (the book's reading).

## Mapped to the Context Layers (Chapter 6)
Prompt layer: in-context examples chosen per question, with self-generated reasoning (context engineering). Mainly a workflow: five runs with shuffled options (which also changes the prompt) and a vote (section 6.7). Model settings: unchanged.

## Consequences (documented only)
A demonstration that prompting strategies could raise a general model's benchmark score to the level of specially tuned models in 2023; a 2024 follow-up showing that one of those strategies (few-shot examples) did not transfer to a reasoning model. No clinical deployment is claimed by the authors or by the book.

## A better workflow (AI Work Loop) — for a reader reusing such a design
*Frame:* what is the task, and is a benchmark score evidence for it? *Prompt:* treat the design as a template with a version, a date and the model it was tested on. *Verify:* rerun the test inputs, with and without examples, whenever the model changes. *Decide:* keep only the components that still help. *Disclose:* report the model, date and benchmark limits with any result.

## Questions (4–6)
See the chapter's Case Study Questions 1–5.

## Sources (at least 2, one primary; with access date)
1. Nori, H., Lee, Y. T., Zhang, S., et al. (2023). *Can generalist foundation models outcompete special-purpose tuning? Case study in medicine* (arXiv:2311.16452). https://arxiv.org/abs/2311.16452 (accessed 2026-10-18; PDF v1 read: Table 1, Figures 4 and 6, Table 2, sections 4.3–4.4 and 5.2, limitations).
2. Nori, H., Usuyama, N., King, N., McKinney, S. M., Fernandes, X., Zhang, S., & Horvitz, E. (2024). *From Medprompt to o1: Exploration of run-time strategies for medical challenge problems and beyond* (arXiv:2411.03590). https://arxiv.org/abs/2411.03590 (accessed 2026-10-18; PDF v1 read: abstract, Table 1, Figures 5–6, Figure 9).
3. OpenAI. (2023, January 23). *OpenAI and Microsoft extend partnership*. https://openai.com/index/openai-and-microsoft-extend-partnership (interests).
