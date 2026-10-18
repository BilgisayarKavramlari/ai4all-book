# Case: A risk score without reasons — the Dutch childcare-benefits scandal (2013–2021)

Chapter: 17 (only) · Field: government / social services · Failure label: **bias — documented** (official finding: the AP's 2020 report, pp. 14–16, 50, and its 2021 fine decision); chain **link 2 "checked before use?" failed** (the staff member could not see which indicators produced a score: confirmed, AP 2020 p. 15); link 3 reliance (payment delayed, evidence requested: confirmed, AP p. 16); **link 4 harm reported** (Amnesty) · Outcome: negative

Attribution tiers (book-wide rule): **confirmed** = Autoriteit Persoonsgegevens (2020), report z2018-22445 (build/ch17/src/ap_2020.pdf, read in v2), the AP's fine decision of November 25, 2021, and Parlementaire ondervragingscommissie Kinderopvangtoeslag (2020), *Ongekend onrecht* (build/ch17/src/ongekend_onrecht.txt); Dutch texts in the book's translation · **reported** = Amnesty International (2021), *Xenophobic Machines*, English edition (build/ch17/src/amnesty_en.txt; amnesty_xenophobic.pdf is the Dutch translation) · **inferred** = this book's reading, marked. **No individual is named.** The model was one part of a larger failure; the book never says it caused the scandal.

## Context
Parents in the Netherlands who pay for childcare can receive a benefit (*kinderopvangtoeslag*) from the tax administration's benefits office (Belastingdienst/Toeslagen).

## Timeline
- **2013:** after a large fraud case, the responsible state secretary tells staff fraud will be tackled harder; more checks before payment (confirmed, inquiry p. 14). The risk classification model is in use from 2013 (confirmed, AP p. 14).
- **At least March 2016 – October 2018:** nationality used for the model's "Dutch citizenship" indicator; the AP calls this discriminatory and therefore improper processing (confirmed, AP p. 50; inquiry p. 14).
- **July 16, 2020:** the AP's report (confirmed).
- **December 17, 2020:** the inquiry's report, *Ongekend onrecht* ("unprecedented injustice") (confirmed).
- **January 15, 2021:** the cabinet resigns (reported: Amnesty, p. 14, citing government letter and press).
- **October 25, 2021:** Amnesty's report (reported tier).
- **November 25, 2021 (announced December 7):** the AP fines the Minister of Finance, as controller for the tax administration, €2.75 million for unlawfully keeping dual-nationality data and for using nationality in the risk model and in fraud detection, in a discriminatory and improper way (confirmed, AP decision). No appeal found.

## What the AI did
A risk classification model, described by the office as *zelflerend* ("self-learning"), trained on examples of correct and incorrect applications, used several dozen indicators; the trained model produced a scorecard whose indicator values add up to a risk score between 0 and 1 (confirmed, AP pp. 14–15; inquiry p. 14). "Dutch citizenship / not Dutch citizenship" was one indicator; the head of the benefits office stated that non-Dutch citizenship raised the risk but was not enough alone for a high score (AP p. 16).

## What humans did
- Selected applications were checked by hand; applicants could be asked for extra evidence (confirmed, p. 14).
- The 100 highest-scoring applications each month (in principle all above 0.8) went to staff for hand checks; the others continued through the automatic process (confirmed, AP pp. 14–15).
- The staff member could not see on which indicators a score was based; the tax administration itself wrote that the staff member does not know why the system selects a case (confirmed, AP pp. 15–16).
- A high score could delay the advance payment and bring a request for evidence (confirmed, AP p. 16).
- Three readings: the AP found the processing discriminatory but racial discrimination not sufficiently shown (AP pp. 48, 50); Amnesty calls it racial profiling (pp. 18, 20); the government replied to Amnesty that considering citizenship did not mean nationality was a risk factor, and Amnesty rejects that reply (p. 16).

## Consequences (by tier)
- Selection led to suspension of payments and investigations (reported, Amnesty pp. 5, 11).
- "Tens of thousands" of parents and caregivers were falsely accused of fraud (reported, Amnesty p. 5).
- The inquiry's own findings concern the wider practice: the all-or-nothing approach, the group-wise approach and the intent/gross-negligence approach grossly violated the rule-of-law principle of doing justice to individual situations; fundamental principles of the rule of law were violated by the legislature, the executive and the administrative courts (confirmed, pp. 7–8); information from government was extraordinarily limited (p. 9). Its questions did **not** include nationality risk profiles (p. 11).

## Labels (Chapter 4 rules)
- **Tree:** bias — **documented** (an official finding records the indicator applied to applications; D-4.3's "same skew across matched outputs" is met by a rule applied to every application). Figure file f17-18-tree-c14.
- **Chain:** link 1 output (score with a citizenship indicator: confirmed, AP); **link 2 failed** (the staff member could not see which indicators produced the score: confirmed, AP); link 3 reliance (payment delayed, evidence requested: confirmed, AP); **link 4 harm: reported** (Amnesty). The inquiry's harm findings are about the wider practice and are not drawn on the model's chain. Figure file f17-19-chain-c14.
- **Opacity is not a tree branch** (book-wide rule): it is the condition that disabled link 2 and the contest (inferred).
- **Bias Lifecycle:** data (historic examples; citizenship indicator) and use (no reasons) highlighted; model described as "self-learning" (the office's description, recorded by the AP and the inquiry); feedback dashed (the book's reading). Figure file f17-20-lifecycle-c14.
- **Explanation layers (file f17-04-layers-c14):** for the parents, notice, documentation, global logic and what would change it missing (reported, Amnesty); local reasons missing (confirmed for reviewers, AP); contest partly: objections and appeals existed, but the inquiry found the administrative courts helped sustain the rigid practice (confirmed).

## A better workflow (AI Work Loop: Frame → Prompt → Verify → Decide → Disclose)
- **Frame:** decide whether any automated selection is appropriate, and which features are lawful (the AP found nationality unnecessary for the office's task).
- **Verify:** test the score group by group before use (Chapter 16); measure what drives it (global logic); publish a register entry and model card.
- **Decide:** reviewers see the reasons for each score and have power and time to overrule it.
- **Disclose:** tell applicants that a system was used, give reasons from the record, and a route to a person who can change the decision.
- *Inferred, marked:* reasons shown to reviewers would at least have made the citizenship indicator visible; whether they would have changed decisions is unknown.

## Jobs per chapter
Ch. 17 only: Opening (facts, puzzle); 17.1 (audiences, roles); 17.2 (black box, one sentence); 17.7 (no public documentation); Case Study (labels, tiers, dispute, larger failure); Ethics Lens (who gets an explanation). Not used in Chapters 15–16.

## Questions (4–6)
1. Sort five facts into confirmed and reported, with reasons.
2. Label the case on the tree and the chain; why is opacity not a tree branch?
3. Which layer would most have helped the reviewers, and which the parents? (Mark your reading.)
4. State the AP's finding, Amnesty's reading and the government's reply about the indicator; how would you write about the dispute?
5. Compare with the Apple Card short case: discrimination found and not found, opacity in both.

## Sources
Autoriteit Persoonsgegevens. (2020). *Belastingdienst/Toeslagen: De verwerking van de nationaliteit van aanvragers van kinderopvangtoeslag* (z2018-22445). · Autoriteit Persoonsgegevens. (2021, November 25). *Besluit tot boeteoplegging*. · Parlementaire ondervragingscommissie Kinderopvangtoeslag. (2020). *Ongekend onrecht*. Tweede Kamer. · Amnesty International. (2021). *Xenophobic machines* (EUR 35/4686/2021), English edition.
