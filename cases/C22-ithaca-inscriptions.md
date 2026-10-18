# Case: Ithaca, experts and a model restoring ancient Greek inscriptions (2022)

Chapter: 19 (Opening Case; arts and humanities guide) · Field: arts and humanities (epigraphy, ancient history) · Failure label: none on the tree (positive research result) · Outcome: positive

## Context
Many ancient Greek inscriptions are damaged; epigraphers restore missing letters and attribute texts to places and dates. A team from DeepMind, Ca' Foscari University of Venice, Harvard's Center for Hellenic Studies, the Athens University of Economics and Business and the University of Oxford built Ithaca, a deep neural network for the three tasks (Assael et al., 2022; affiliations confirmed in Europe PMC).

## Timeline
- Aug 16, 2021: manuscript received by *Nature*; accepted Jan 19, 2022.
- Mar 9, 2022: published, *Nature* 603, 280–283 (open access).
- Jul 23, 2025: a sequel, Aeneas, for Latin inscriptions, published online (Assael et al., 2025).

## What the AI did
Ithaca was trained on 78,608 inscriptions processed from the Packard Humanities Institute's searchable Greek inscriptions database. On test texts with characters hidden on purpose (answers known), it produced ranked restorations, a region (84 possible) and a date. Top-1 restoration accuracy alone: 61.8%. Region: 70.8% top-1. Dates: within about 30 years on average, median 3 (confirmed; the methods section gives 28.7 years).

## What humans did
Two ancient-history graduate students with epigraphic training restored the texts alone (top-1 accuracy 25.3%) and then with Ithaca's top-20 suggestions (71.7%) (Table 1; confirmed). The authors describe Ithaca as designed to assist and expand the historian's workflow, and present its restorations as plausible suggestions, never as certain. Its first suggestion was wrong in about 38% of restorations. That historians should stay in charge, and why the pair beat both, is this book's reading; the paper reports the result without testing the reason.

## Consequences (documented only)
A published method and an open tool; the 2025 sequel reports that historians using Aeneas outperformed humans and the model alone on restoration and geographic attribution (abstract; on dating the model alone did better).

## A better workflow (AI Work Loop)
Frame: restoration as ranked candidates for an expert. Prompt: the damaged text. Verify: an epigrapher chooses, using the field's evidence. Decide: the expert, not the model. Disclose: publish the method and its accuracy by task.

## Questions (4–6)
1. Why is top-1 accuracy a strict measure, and what does it leave out?
2. Who is the verification authority in epigraphy?
3. Why might the pair beat both the model and the experts alone?
4. What would a workflow card for Ithaca list as "not for"?

## Sources (at least 2, one primary; with access date)
1. Assael, Y., Sommerschield, T., Shillingford, B., Bordbar, M., Pavlopoulos, J., Chatzipanagiotou, M., Androutsopoulos, I., Prag, J., & de Freitas, N. (2022). Restoring and attributing ancient texts using deep neural networks. *Nature, 603*, 280–283. https://doi.org/10.1038/s41586-022-04448-z (PMC8907065; read 2026-10-18) — primary.
2. Assael, Y., Sommerschield, T., Cooley, A., Shillingford, B., Pavlopoulos, J., Suresh, P., Herms, B., Grayston, J., Maynard, B., Dietrich, N., Wulgaert, R., Prag, J., Mullen, A., & Mohamed, S. (2025). Contextualizing ancient texts with generative neural networks. *Nature, 645*, 141–147. https://doi.org/10.1038/s41586-025-09292-5 (repository abstract read 2026-10-18).
