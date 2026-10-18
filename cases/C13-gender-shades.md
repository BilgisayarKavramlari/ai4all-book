# Case: Gender Shades — Intersectional Error Rates in Commercial Gender Classification (Buolamwini & Gebru, 2018)

Chapter: 16 · Field: computer vision / technology · Failure label: bias (primary, **documented**: leaf "unequal quality across groups or languages"; error rates measured across many matched faces in a published audit) · chain link 2 "checked before use?" **inferred** (no results on existing gender-classification benchmarks in the documentation; internal testing unknown) · link 4: no harm documented in this audit · Outcome: negative (large subgroup gaps), then mixed (the named companies cut the gaps within seven months)

Facts are stated in three attribution tiers (book-wide rule): **confirmed** = the published paper (Buolamwini & Gebru, 2018; full text read 2026-10-18, build/ch16/src/gendershades.txt), its follow-up by one of the authors (Raji & Buolamwini, 2019; full text read), or a company's own statement; **reported** = a named outlet or person; **inferred** = this book's reading.

**Scope rule (book-wide):** Gender Shades tested **gender classification** (labeling a face in a photo as female or male), not face recognition (matching a face to a person). Never write "face recognition" for this audit.

## Context
Microsoft, IBM and Face++ (Megvii) sold gender classification as part of facial-analysis services offered to developers through application programming interfaces (confirmed: paper §4.2). The companies' documentation reported no results on existing gender-classification benchmarks, and none said what data its classifier was trained on; Face++'s terms disclaimed any warranty of accuracy; only IBM returned confidence scores (confirmed: paper §4.2). Two widely used face benchmarks were 79.6% (IJB-A) and 86.2% (Adience) lighter-skinned (confirmed: paper, Table 3).

## Timeline
- 2015–2016: as a graduate student at the MIT Media Lab working on an art project ("Aspire Mirror", proposed October 2015, which projects quotes and faces onto a viewer's reflection), Buolamwini found that face-tracking software did not detect her face until she put on a white mask (reported: her own account, Buolamwini, 2023; NPR *Fresh Air*, November 28, 2023).
- 2017: the authors build the **Pilot Parliaments Benchmark (PPB)**: 1,270 official photos of parliamentarians from Rwanda, Senegal, South Africa, Iceland, Finland and Sweden, chosen for gender parity in their parliaments; skin type labeled on the six-point Fitzpatrick scale, with the definitive labels by a board-certified surgical dermatologist, grouped as lighter (I–III) and darker (IV–VI); perceived gender labeled from names, titles and photos; 44.6% women, 55.4% men (confirmed: paper §3.3–3.5, Tables 1–3). Subgroups: darker women 21.3%, darker men 25.0%, lighter women 23.3%, lighter men 30.3% (confirmed: Table 2).
- April–May 2017: the audit of the three services (confirmed: paper §4).
- December 19, 2017: the paper, without company names, sent to the three companies (confirmed: Raji & Buolamwini, 2019).
- February 9, 2018: first public mention in *The New York Times* (reported: Raji & Buolamwini, 2019, citing Lohr, 2018); February 24, 2018: paper presented at the FAT* conference with company names (confirmed: Raji & Buolamwini, 2019).
- Within seven months of receiving the results (IBM after 66 days, Microsoft 189, Face++ 190): all three companies release new API versions; IBM and Microsoft reference the study in their update releases (confirmed as reported in Raji & Buolamwini, 2019; company statements cited there).
- August 21, 2018: re-test on the same benchmark, adding Amazon and Kairos (confirmed: Raji & Buolamwini, 2019).
- June 2020, amid nationwide protests: IBM writes to members of Congress that it no longer offers general-purpose facial recognition **or analysis** software (June 8; the analysis part covers the kind of feature the audit tested); Amazon announces a one-year moratorium on police use of its face-recognition service (June 10), extended until further notice in May 2021 (reported) (confirmed as company statements: IBM THINKPolicy letter, archived; aboutamazon.com). **Not causally linked by this book**: the audit's influence on either decision is not established.

## What the AI did
Overall accuracy (true positive rate): Microsoft 93.7%, Face++ 90.0%, IBM 87.9%. Error rates for darker-skinned women: 20.8%, 34.5%, 34.7%. Best-classified group: lighter-skinned men for Microsoft (0.0%) and IBM (0.3%); darker-skinned men for Face++ (0.7%). All three performed better on men than women (gap 8.1–20.6 points) and on lighter than darker faces (11.8–19.2 points). Darker-skinned women were 21.3% of the faces and 61.0–72.4% of each classifier's errors (confirmed: paper §4.1, §4.4, Table 4). The South African subset, with the most consistent image quality, showed the same pattern (confirmed: Table 5).

## What humans did
- The auditors chose skin type rather than race because race labels differ across places and appearance varies within categories (confirmed: paper §3.1); used binary perceived-gender labels to match the services, noting that this does not capture gender identity (confirmed: §3.4); disclosed results to the companies before publication (confirmed: Raji & Buolamwini, 2019).
- The companies released updates, which the follow-up study judged to "appear to be data-driven" (the authors' reading of IBM's and Microsoft's statements); the August 2018 re-test found darker-skinned women's error at 1.52% (Microsoft), 4.1% (Face++) and 16.97% (IBM), reductions of 17.7–30.4 points, and overall error reductions of 5.72–8.3 points; Amazon 31.37% and Kairos 22.50% for that group (confirmed: Raji & Buolamwini, 2019, Tables 1–2).
- The follow-up's authors caution that models may have been tuned to the one benchmark (confirmed).

## Why the gaps arose (tiers)
- The paper raises possibilities rather than naming causes: darker skin "may" be correlated with facial features or gender displays underrepresented in training data, and default camera settings are often tuned to expose lighter skin better (citing Roth, 2009) (confirmed as the authors' discussion, §4.5–4.7).
- The authors conclude that image characteristics did not fully account for the gaps, from the South African subset (confirmed).
- **This book's reading (inferred):** training data in which some faces are underrepresented, and imaging conditions, are possible contributors; neither is shown as the cause, and the companies did not disclose their training data.

## Failure label (Signature 5 and the failure-to-harm chain; the tree and chain figures in the chapter's Case Study)
- **Tree — bias, leaf "unequal quality across groups or languages", documented (solid).** The defining feature (D-4.3: the same skew across matched outputs) is met: error rates measured over hundreds of faces per subgroup.
- **Chain — link 1 documented; link 2 "Checked before use?" inferred (dashed):** the public documentation showed no group results (confirmed), but whether the companies tested by group internally is unknown; **link 3 and link 4:** no reliance or harm documented in this audit. Harms of face *recognition* in use belong to other cases (Chapter 16, Short case 2).

## Consequences (documented only)
Published subgroup results; updated services from all three named companies within seven months with much smaller gaps on this benchmark; wide citation of the study in later policy discussion (reported: Raji & Buolamwini, 2019, list letters from shareholders, civil-rights groups and a U.S. senator that cite the work).

## A better workflow (AI Work Loop: Frame → Prompt → Verify → Decide → Disclose)
- **Frame:** for whom must the tool work? Name the groups and intersections before testing.
- **Verify:** test group by group on a benchmark with enough people in every subgroup; report each group's size; apply the two-part rule to gaps.
- **Decide:** choose which errors matter most for the use (16.3, 16.6); decide not to use the feature for decisions about people if gaps cannot be closed.
- **Disclose:** publish subgroup results and training-data composition (the paper's own recommendation on transparency and accountability, §4.7).

## Questions (4–6)
1. Label the case on the tree and the chain, with documented or inferred and a reason for each.
2. Why is gender classification not face recognition, and why does the difference matter for claims?
3. Which three features of the method made the results hard to dismiss?
4. What could the August 2018 re-test show, and what could it not show?
5. Compare the case with the Williams arrest (Short case 2): where on the Bias Lifecycle did each problem become visible?

## Sources (at least 2, one primary; with access date)
1. Buolamwini, J., & Gebru, T. (2018). Gender shades: Intersectional accuracy disparities in commercial gender classification. *PMLR 81*, 77–91. https://proceedings.mlr.press/v81/buolamwini18a.html (full text read 2026-10-18)
2. Raji, I. D., & Buolamwini, J. (2019). Actionable auditing. *AIES '19*, 429–435. https://doi.org/10.1145/3306618.3314244 (full text read 2026-10-18 via the MIT Media Lab PDF)
3. Buolamwini, J. (2023, October 31). *Unmasking AI*. Random House (her account; reported tier); NPR *Fresh Air* interview (2023, November 28)
4. IBM (2020, June 8), letter to Congress, IBM THINKPolicy blog (Internet Archive capture of 2022-04-23); Amazon (2020, June 10), https://www.aboutamazon.com/news/policy-news-views/we-are-implementing-a-one-year-moratorium-on-police-use-of-rekognition (both read by the fact-checker 2026-10-18)
