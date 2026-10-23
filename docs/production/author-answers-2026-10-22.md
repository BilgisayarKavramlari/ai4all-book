# Author answers, 2026-10-22 (Chapters 18–19 From the Field; OptiWisdom products)

Pasted by the author in chat on 2026-10-22, in reply to the questions in docs/production/YAZAR_DOLDURMA_LISTESI.md. The pasted text ends mid-sentence in D3 ("at least two non-OptiWisdom"); the editor reads it as "at least two non-OptiWisdom sources in each box" and asks the author to confirm.

Editor notes on conflicts with standing rules:
- B2 asks for the reference title with Turkish letters ("Yazılımların kaynakları"); D28 (the author's rule of 2026-10-19) keeps the book ASCII-only, so the reference stays "Yazilimlarin kaynaklari [Sources of software]" (correct spelling, no "Kaaynaklari").
- D1/D2 name the developer as Bilkav Egitim Danismanlik A.S.; D30 (the author's rule of 2026-10-22) says Bilkav is not named and OptiWisdom is used instead.

---

B1. (a) Keep the disclosure line as written: "Disclosure: I am a founder of OptiWisdom, which develops software for businesses, including AI tools. See 'How This Book Was Written.'"

B2. Approved. The 2014 entry says this in the author's own words: he was once a firm defender of open source and moved away from it because open source had turned into a marketing instrument (old version open, newest version commercial; free software, paid documentation or services; free at first, then very high costs once the customer depends on it). It advises buyers to plan a 5–10-year budget before acquiring software. The author still holds this view today. Frame it as: "In 2014 I wrote … I still hold that view."
Use the correct title in the reference: "Yazılımların kaynakları [Sources of software]". The entry's own running header misspells it "Kaaynakları"; do not copy that.

B3. Pages 5–8 accepted (matched to the issue's contents page; the source .docx has no page numbers). YBS Ansiklopedi, 1(2), October 2014.

B4. Yes. Use this anonymized field story in the author's voice; no company names:
"In the early 2000s, a software company won contracts with many Turkish municipalities by bidding far below market prices. It signed one-year contracts and automated some of the municipalities' most critical services. When a municipality ended the contract, the company refused to hand over the data, the source code, even the passwords, and the system was locked, so the municipality had little choice but to stay. The contracts were written to allow this, and many of these cases ended up in court. In a sense the company had a point: it was working far below market rates. But it spread quickly because software procurement experience was thin and because an elected mayor could approve a cheap deal that showed results in his own term, while the cost landed on the next administration. Municipalities learned, and today I doubt any would sign such a deal without proper terms on data, code and exit."
Add one short sentence that the pattern lives on in other forms (for example, a website built "for free" whose renewal is priced very high and whose contract ties all rights to the developer). Do NOT state as fact that vendors deliberately seed cracked copies; at most, write it as the author's own observation ("I have also seen vendors tolerate unlicensed copies until users depended on them, then start charging"), supported by these verified sources:
- Schlender, B. (1998, July 20). The Bill & Warren Show. Fortune. https://money.cnn.com/magazines/fortune/fortune_archive/1998/07/20/245683/ (Gates: "as long as they're going to steal it, we want them to steal ours. They'll get sort of addicted, and then we'll somehow figure out how to collect sometime in the next decade." Quote at most ~15 words per our rule; paraphrase the rest.)
- Conner, K. R., & Rumelt, R. P. (1991). Software piracy: An analysis of protection strategies. Management Science, 37(2), 125–139. https://doi.org/10.1287/mnsc.37.2.125 (with network effects, leaving software unprotected can raise profits)
- Givon, M., Mahajan, V., & Muller, E. (1995). Software piracy: Estimation of lost sales and the impact on software diffusion. Journal of Marketing, 59(1), 29–37. https://www.jstor.org/stable/1252012 (most users had pirated copies, yet pirates drove most new legal adopters by word of mouth)
- Takeyama, L. N. (1994). The welfare implications of unauthorized reproduction of intellectual property in the presence of demand network externalities. Journal of Industrial Economics, 42(2), 155–166.
- Peitz, M., & Waelbroeck, P. (2006). Piracy of digital products: A critical review of the theoretical literature. Information Economics and Policy, 18(4), 449–476. https://doi.org/10.1016/j.infoecopol.2006.06.005
Optional modern example of "free/legacy use, then charge and audit": Oracle Java SE Universal Subscription (per-employee pricing from January 2023) — IDC (Stewart, 2023-01-30) and The Register (Clark, 2024-06-10; note that some claims come from vendors of Java alternatives).
Optional public-sector source: European Commission (2013). Against lock-in: Building open ICT systems by making better use of standards in public procurement, COM(2013) 455 final.
Run these through the fact-checker and log them in docs/factcheck/.

C1. (b) Publicly funded. The 2016 entry is adapted from a literature-review section the author wrote as a consultant to a TÜBİTAK-supported industrial R&D project, no. 3150106, at a Turkish e-commerce company (consultancy assignment 28 Jan – 28 Jul 2016). The project developed decision-support software comparing external and internal data using big data and sentiment analysis. Disclosure line: "Adapted from a literature review I wrote in 2016 as a consultant to a TÜBİTAK-supported industrial R&D project (no. 3150106) at a Turkish e-commerce company." Do not name the company.

C2. pp. 21–36 is correct (page headers in the published PDF run 22–36; the unnumbered first page is 21). YBS Ansiklopedi, 3(3), September 2016.

C3. (a) Keep the entry's own title: "Duygu analizi (Sentimental analysis)". In our own prose, call the field "sentiment analysis".

C4. Approved. The entry says humans reach about 85% agreement and that about 70% correct classification was then counted as success for software, citing [19] Burn-Murdoch, J. (2013, June). Social media analytics: Are we nearly there yet? The Guardian, Data Store. Present it as a 2013 benchmark, not a current figure. Optional supporting line from the same entry: success rates were lower for less-studied languages such as Turkish than for English.

C5. None.

D1/D2. Product facts (all from company documents; nothing independently verified; no customer names; do not use the word "patented"):
OptiSegment — an AutoML segmentation (clustering) engine. It automates preprocessing, feature engineering and feature elimination, selects among clustering algorithms (e.g., k-means, DBSCAN, agglomerative, spectral) and tunes them, flags anomalous records, and evaluates clusters with internal measures such as silhouette. Input: tabular data via a REST API (CSV/JSON). Output: cluster assignments for records, used as input to later scoring or prediction. Developed by Bilkav Eğitim Danışmanlık A.Ş. with TÜBİTAK 1507 support (project 7190398, July 2019 – December 2020). No documented customer deployment or measured result; planned uses were customer and product segmentation, HR, credit-risk segmentation, CRM and fraud. Teaching hook for Chapter 11: the product's own brochure lists segmentation axes that include "ethnic origin" and "religious, political … beliefs" while claiming it "does not act on prejudice". Use this candidly to show that segment variables are human choices carrying hidden assumptions.
OptiMatcher — an AutoML matching and recommendation engine (product-to-product, person-to-product, behavioral path analysis). Input: a transaction log (visitor ID, time, product, event type) plus an open-ended file of person features such as age, gender and city. Output: ranked recommendations per person or item, a later success metric, and dashboard reports. Developed by Bilkav Eğitim Danışmanlık A.Ş. with TÜBİTAK 1507 support (project 7210248, 2021–2022). Validated on public datasets (HR task-to-staff, call-center customer-to-agent, real-estate and ad matching) and on real e-commerce data. Company-reported result: in an A/B test on a home-textile e-commerce site, run through a marketing-technology partner, OptiMatcher's recommendations converted at about 7% versus about 5% for the site's own recommendations, with responses under 100 ms. Label it "company-reported, not independently verified" and do not name the retailer or partner.
Teaching hook for Chapter 16: the product's documentation uses age, gender and city as recommendation features, and its sample reports read "Most recommendations went to women" and "The most frequent recommendation to men was perfume." Use this candidly: what would we check for bias before such a system decides which loan offer goes to which bank customer (a use case the documentation lists)?

D3. Approved: OptiSegment in Chapter 11; OptiMatcher in Chapter 16; OptiScorer stays in Chapter 12 with a brief mention in Chapter 16. Constraints for each box:
- at most one third of a page (we must stay under the 1,200-page print limit);
- the disclosure line plus the TÜBİTAK support (program and project number);
- at least two non-OptiWisdom [text ends here]
