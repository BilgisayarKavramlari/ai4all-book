# Case: A video conference built from public clips — the Arup deepfake fraud (2024)

Chapter: 13 (and 15) · Field: finance / corporate security · Failure label: **other — misuse, such as fake media made to deceive (documented)**; chain link 2 "checked before use?" failed (transfers followed the instructions: confirmed; no check with head office before them: reported) · Outcome: negative

Attribution tiers (book-wide rule): **confirmed** = Hong Kong SAR Government (2024), the written reply to the Legislative Council (text: build/ch13/src/lcq9.txt) · **reported** = Chen & Magramo (2024) and Magramo (2024), citing the police briefing, RTHK, or the company · **inferred** = this book's reading, marked. The record says "police believe" for the generation of the conference; that wording is kept.

## Context
A finance employee at the Hong Kong office of a multinational company (later confirmed by the company as Arup, a British engineering and design firm) received a phishing email from someone posing as the chief financial officer of the head office in the United Kingdom, inviting the employee to a group video conference about confidential transactions (confirmed).

## Timeline
- **January 2024:** the transfers and the report to the police; the police received the case in late January (confirmed). The company says it notified the police in January (reported, Magramo, 2024).
- **Friday, February 2, 2024 (date derived from CNN's "Friday"):** police briefing; a senior police superintendent told Radio Television Hong Kong (RTHK), as reported by CNN, that everyone the worker saw in the multi-person video conference was fake (reported, Chen & Magramo, 2024).
- **May 16–17, 2024:** Arup confirms to CNN that it was the company (reported, Magramo, 2024).
- **June 26, 2024:** the Secretary for Security's written reply to the Legislative Council describes the case (confirmed).
- **As of October 2026:** we found no public report of an arrest or a recovery in this case (refresh list).

## What the AI did
The video conference was pre-recorded (confirmed); after investigating, the police believe it was generated from downloaded public online video clips and voices of the impersonated officer; there was no real interaction between the employee and the fraudster (confirmed). The record does not name the tools or describe how the clips were edited.

## What humans did
- The employee first suspected the message was phishing because it spoke of a secret transaction, then set the doubt aside after the call because the people looked and sounded like colleagues he recognized (reported, Chen & Magramo, 2024, citing police).
- As instructed, the employee authorized transfers to five local bank accounts (confirmed); 15 transactions (reported, RTHK via Magramo, 2024).
- After giving the instruction, the fraudster ended the meeting under some pretext and continued the payment instructions by instant messaging (confirmed).
- The fraud was "only discovered when the employee later checked with the corporation's head office" (reported, CNN's narration; Chen & Magramo, 2024).

## Consequences (documented only)
- Loss of about HK$200 million (about US$25.6 million) (confirmed; conversion reported).
- Arup: "Our financial stability and business operations were not affected and none of our internal systems were compromised" (reported, Magramo, 2024).
- The case was still under police investigation in June 2024 (confirmed).

## Labels (Chapter 4 rules)
- **Tree:** other — "misuse, such as fake media made to deceive," **documented** (the record states that the police believe the conference was generated from public clips and voices of the impersonated officer). Not hallucination: the media did what its makers intended.
- **Chain:** link 2 "checked before use?" failed (links are numbered 1–4: output wrong, checked before use?, someone relies, loss). Documented that the transfers followed the instructions (confirmed); "no check with head office before the transfers" is reported (CNN). Link 4 loss confirmed. Figure: F13.17 (tiers: confirmed solid, reported solid with outlet tag, inferred dashed — none here).

## Two accounts, one event (a tiers lesson)
February reports describe a video conference with several people on screen; the June government reply adds that it was pre-recorded, with no real interaction. The accounts are compatible; the later one is narrower and more exact. Use the primary record for what it states; mark the rest "reported."

## A better workflow (AI Work Loop: Frame → Prompt → Verify → Decide → Disclose)
- **Frame:** a money request that is urgent, secret or arrives on a new channel is a trigger (Chapter 13 §13.8).
- **Verify:** confirm through a channel the requester does not control (an out-of-band check: the directory number, the head office directly). The police advice in the record: ask the person to move on camera, test identity through the content of the conversation, verify money requests by phone, use Scameter (confirmed).
- **Decide:** no transfer until the check is done; dual authorization for large transfers (controls: Chapter 15).
- *Inferred, marked:* this book reads the later check with head office as a channel the fraudsters did not control, and the case as one where the same check before the first transfer would likely have exposed the fraud. The police advice also includes a looking test (ask the person to turn their head on camera), which this book treats as a lead at best, and a phone check for money requests from relatives or friends; a call counts only if placed to a number you already have.

## Jobs per chapter
Ch. 13: facts, how the media was made (police belief), the channel, the protocol, labels, the two accounts. **Ch. 15:** payment controls, dual authorization, security training, voice-cloning scams, the police's separate report of deepfakes used to fool facial recognition with stolen identity cards (reported, Chen & Magramo, 2024).

## Questions (4–6)
1. What do the first reports and the government's reply each say about the meeting (they differ in detail, not in substance), and how should you write about it today?
2. Label the case on the tree and the chain, marking confirmed and reported facts.
3. Which single rule of a verification protocol would most likely have stopped the transfers? (Mark your answer as your reading.)
4. Why was a video call more convincing than the email, if the call could be built from public clips?
5. What does "none of our internal systems were compromised" tell you about where the failure sat?

## Sources (at least 2, one primary; with access date)
1. Hong Kong SAR Government. (2024, June 26). *LCQ9: Combating frauds involving deepfake* [Press release]. https://www.info.gov.hk/gia/general/202406/26/P2024062600192.htm (accessed 2026-10-18; text saved in build/ch13/src/lcq9.txt).
2. Chen, H., & Magramo, K. (2024, February 4). Finance worker pays out $25 million after video call with deepfake 'chief financial officer'. *CNN*. https://edition.cnn.com/2024/02/04/asia/deepfake-cfo-scam-hong-kong-intl-hnk/index.html (accessed 2026-10-18).
3. Magramo, K. (2024, May 16; updated May 17). British engineering giant Arup revealed as $25 million deepfake scam victim. *CNN*. https://edition.cnn.com/2024/05/16/tech/arup-deepfake-scam-loss-hong-kong-intl-hnk/index.html (accessed 2026-10-18).
Not used (not read): the WEF interview with Arup's CIO (page returned 403); the *Financial Times* report that first named Arup.
