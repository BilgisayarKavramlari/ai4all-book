# Case: The Chatbot That Promised a Refund (*Moffatt v. Air Canada*, 2024 BCCRT 149)

Chapter: 4 (also 10, 18) · Field: customer service / law · Failure label: hallucination (primary, **inferred**: the record does not describe the chatbot's technology) · chain link 2 "checked before use?" failed (**documented**, para. 28) · Outcome: negative for the airline (ordered to pay $812.02 CAD)

All facts below come from the decision (Civil Resolution Tribunal of British Columbia, issued February 14, 2024, Tribunal Member Christopher C. Rivers), read in full on 2026-10-18. Paragraph numbers refer to the decision. The decision uses they/them for Jake Moffatt; so does the book.

## Context
Air Canada offers reduced fares to passengers traveling because of the death of an immediate family member (para. 13). Its website included a support chatbot. Air Canada gave no information about the nature of its chatbot; the tribunal described a chatbot generally as an automated system that answers a website user's prompts (para. 14). The parties agreed Moffatt was not chatting with an employee (para. 14).

## Timeline
- November 11, 2022: Moffatt's grandmother dies in Ontario; the same day Moffatt asks the chatbot about bereavement fares and saves a screenshot (paras. 13–15); books a one-way Vancouver–Toronto flight departing November 12 for $794.98 (para. 18); a phone representative quotes about $380 per flight as the bereavement fare (para. 19).
- November 16, 2022: books the return flight, departing November 18, for $845.38 (para. 18).
- November 17, 2022: first application for the bereavement fare (para. 20).
- December 2022 – February 2023: emails seeking a partial refund (para. 20).
- February 5, 2023: Moffatt sends the chatbot screenshot and confirms the refund form and death certificate were provided (para. 21).
- February 8, 2023: an Air Canada representative admits the chatbot provided "misleading words," points to the linked policy page, and says the chatbot will be updated (para. 22).
- February 14, 2024: decision issued.

## What the AI did
In reply to a question about bereavement fares, the chatbot said that a passenger who needed to travel immediately or had already traveled could submit the ticket for a reduced bereavement rate within 90 days of the ticket's issue date, using the Ticket Refund Application form (para. 15). The words "bereavement fares" in the reply linked to the airline's "Bereavement travel" page, which said the policy does not apply to requests made after travel is completed (paras. 16–17).

## What humans did
Moffatt relied on the reply, booked at full fare, applied within 90 days and pursued the refund (paras. 18–21, 30). Air Canada did not grant the partial refund, offered a $200 coupon that Moffatt did not accept (para. 41), and argued before the tribunal that it could not be held liable for information provided by its chatbot, that Moffatt had not followed the proper procedure, and that its tariff protected it, without filing the tariff text (paras. 4, 27, 31).

## Failure label (Signature 5 and the failure-to-harm chain; source figures F4.11 and F4.9)
- **Tree — hallucination, inferred** (leaf: contradicts the source the system linked to). The reply was wrong (documented), but the record does not show it was generated (para. 14). If it was a generative system working from the policy page, this was an intrinsic hallucination; if it followed written rules, the error was in the rules.
- **No overconfidence label.** The reply gave plain instructions; there is no evidence of expressed certainty (no stated probability, no "guaranteed", no pushback).
- **Chain — link 2 failed, documented:** the tribunal found Air Canada did not take reasonable care to ensure its chatbot was accurate (para. 28). Link 3, reliance, was found reasonable (para. 29). Link 4, loss: $650.88 (para. 40).

## Consequences (documented only)
Finding of negligent misrepresentation (paras. 24–32). Order: $650.88 damages, $36.14 pre-judgment interest, $125 tribunal fees; $812.02 total within 14 days (para. 44). The tribunal rejected the airline's argument that the chatbot was effectively a separate entity responsible for its own actions, holding that the airline is responsible for all information on its website, whether from a static page or a chatbot (para. 27), and noted the airline did not explain why customers should double-check one part of its website against another (para. 28). Scope: one small-claims decision in British Columbia; not a general rule of law. No later review or appeal was found as of 2026-10-18 [VERIFY].

## A better workflow (AI Work Loop, for the organization)
Frame: decide which policy questions a chatbot may answer and which go to a person. Verify: test every policy answer against the policy page with known-answer questions before launch and after each policy change. Decide: where the chatbot and the page disagree, the page wins and the chatbot is corrected. Disclose: tell customers what the chatbot is and where the binding policy lives (whether a disclaimer changes responsibility was not before the tribunal; Chapter 18).

## Each appearance in the book has one job (Decision 7, ch04 blueprint)
Chapter 4: facts (Opening Case), failure-to-harm chain (4.7), tree label and better workflow (Case Study). Chapter 10 (week 7, reading R7): disclosure and communication at work. Chapter 18: liability and governance.

## Questions
See the Chapter 4 Case Study Questions.

## Sources (accessed 2026-10-18)
1. *Moffatt v. Air Canada*, 2024 BCCRT 149. Civil Resolution Tribunal, British Columbia, February 14, 2024. https://decisions.civilresolutionbc.ca/crt/crtd/en/525448/1/document.do — primary (decision PDF, read in full). Also indexed on CanLII (2024bccrt149), which blocks automated access.
2. Mondaq (2024). Airline ordered to compensate a B.C. man because its chatbot provided inaccurate information. https://www.mondaq.com/canada/new-technology/1427926/airline-ordered-to-compensate-a-bc-man-because-its-chatbot-provided-inaccurate-information — secondary.

## Short cases used with this case (Appendix G only; no case id)
- New York City MyCity business chatbot (2024): Lecher, C. (2024, March 29). NYC's AI chatbot tells businesses to break the law. *The Markup*. Label: hallucination, documented; chain link 2 (no legal review), inferred.
- Chevrolet of Watsonville chatbot, "$1 SUV" (December 2023): AI Incident Database entity page (secondary) [VERIFY primary report]. Label: security vulnerability, direct prompt injection, documented.
