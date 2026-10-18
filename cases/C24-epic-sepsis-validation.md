# Case: A hospital tests a widely used sepsis model and finds it below its reported accuracy (2021)

Chapter: 19 (health guide) · Field: health (hospital medicine, clinical decision support) · Failure label: other (a prediction model below its reported accuracy at a new site), documented; chain link 3 alert burden inferred; no documented harm · Outcome: negative

## Context
The Epic Sepsis Model is a proprietary model, built into a widely used electronic health record, that scores hospitalized patients' risk of sepsis. Its developer's internal documentation reported an area under the curve (AUC, a 0.5–1.0 measure of how well a score separates cases from non-cases) of 0.76–0.83. Researchers at Michigan Medicine, a hospital system using the model, validated it independently (Wong et al., 2021).

## Timeline
- Dec 6, 2018 – Oct 20, 2019: study period; 27,697 patients and 38,455 hospitalizations at Michigan Medicine.
- Jun 21, 2021: published online, *JAMA Internal Medicine* 181(8), 1065–1070.

## What the AI did
The model's AUC at the hospitalization level was 0.63 (95% confidence interval 0.62–0.64). Sepsis occurred in 2,552 hospitalizations (7%). At the alert threshold the study used (a score of 6 or more, within the developer's recommended range), the model missed 67% of them (1,709) and alerted in 18% of hospitalizations (6,971) (confirmed).

## What humans did
The hospital ran an external validation: one site, one period, the 2018–19 version of the model. Epic disputed the findings (reported; Reuter, 2021). A second version of the model (2022) was later validated at four health systems: encounter-level AUC 0.82–0.92 by site, with positive predictive values of 0.13–0.26 (Wong et al., 2026; confirmed from the abstract).

## Consequences (documented only)
A published external validation that differs from the developer's reported accuracy. No patient harm is documented in the study.

## A better workflow (AI Work Loop)
Frame: is the developer's accuracy measured on patients like ours? Verify: validate locally before relying on alerts. Decide: clinicians, with alert burden monitored. Disclose: site, period and version on the card.

## Questions (4–6)
1. What does "external validation" add to a developer's reported accuracy?
2. Why is the tree label "other," not hallucination?
3. What would a card for this model list under "tested on"?
4. Why does one site and one period limit the conclusion?

## Sources (at least 2, one primary; with access date)
1. Wong, A., Otles, E., Donnelly, J. P., Krumm, A., McCullough, J., DeTroyer-Cooley, O., Pestrue, J., Phillips, M., Konye, J., Penoza, C., Ghous, M., & Singh, K. (2021). External validation of a widely implemented proprietary sepsis prediction model in hospitalized patients. *JAMA Internal Medicine, 181*(8), 1065–1070. https://doi.org/10.1001/jamainternmed.2021.2626 (read 2026-10-18) — primary.
2. Reuter, E. (2021, June 23). Popular sepsis prediction model works "substantially worse" than claimed, researchers find. *MedCity News*. https://medcitynews.com/2021/06/popular-sepsis-prediction-model-works-substantially-worse-than-claimed-researchers-find (reported; Epic's disagreement).
3. Wong, A., Currey, D., Schwinne, M., et al. (2026). Multicenter prospective validation of an updated proprietary sepsis prediction model. *JAMA Network Open, 9*(2), e260181. https://doi.org/10.1001/jamanetworkopen.2026.0181 (Crossref abstract read 2026-10-18).
