# Case: Can a language model stand in for survey respondents? Silicon samples (2023–2024)

Chapter: 19 (social science guide) · Field: social science (political science, survey research) · Failure label: bias (a skew across matched outputs: too little variation), documented · Outcome: mixed

## Context
Argyle et al. (2023) proposed "silicon samples": GPT-3, given first-person backstories built from real respondents in the American National Election Studies (ANES) and the "Pigeonholing Partisans" survey, produced answers whose subgroup patterns closely matched the survey's; they called the property "algorithmic fidelity" (confirmed).

## Timeline
- Feb 21, 2023: Argyle et al. online, *Political Analysis* 31(3), 337–351.
- April, June and July 2023: Bisbee et al. reran a simpler version of their main prompt; June was not distinguishable from April, July differed substantially.
- May 17, 2024: Bisbee et al. online, *Political Analysis* 32, 401–416 (open access).

## What the AI did
In Bisbee et al., ChatGPT 3.5 Turbo adopted personas from 2016 and 2020 ANES respondents and gave 0–100 feeling-thermometer ratings of 11 groups. Averages were close to the survey's, but answers varied far less; 48% of regression coefficients differed significantly from the survey's, and about a third of those had the opposite sign; small wording changes shifted the results; a simpler version of the main prompt, rerun in July 2023, gave substantially different results from April's, after the provider updated the model under the same name in June (confirmed).

## What humans did
The researchers compared synthetic and real data side by side and published the comparison; they warned about reproducibility with closed models.

## Consequences (documented only)
A published warning: the authors raise serious concerns about the quality, reliability and reproducibility of synthetic survey data (Bisbee et al., 2024).

## A better workflow (AI Work Loop)
Frame: what would synthetic data be used for? Verify: compare spreads and relationships, not only averages, with real data. Decide: no conclusions about people from synthetic answers alone. Disclose: model version and dates on the card.

## Questions (4–6)
1. Why is "the averages match" not enough?
2. Why is the bias label documented here?
3. Why does the authors' word "overconfidence" not become a tree label (Chapter 4)?
4. What should a social-science workflow card record about the model and dates?

## Sources (at least 2, one primary; with access date)
1. Bisbee, J., Clinton, J. D., Dorff, C., Kenkel, B., & Larson, J. M. (2024). Synthetic replacements for human survey data? The perils of large language models. *Political Analysis, 32*, 401–416. https://doi.org/10.1017/pan.2024.5 (read 2026-10-18) — primary.
2. Argyle, L. P., Busby, E. C., Fulda, N., Gubler, J. R., Rytting, C., & Wingate, D. (2023). Out of one, many: Using language models to simulate human samples. *Political Analysis, 31*(3), 337–351. https://doi.org/10.1017/pan.2023.2 (read 2026-10-18).
