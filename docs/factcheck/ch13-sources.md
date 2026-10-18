# Chapter 13 — source verification log

Checked 2026-10-18 against primary sources where reachable. Status: ✓ verified (text read) · ◐ partly verified (abstract, listing, search snippet or secondary copy read) · ✗ not reachable. Claim-level verdicts are in `ch13.csv`. Counts: 148 rows — 113 supported, 29 partially supported, 3 unsupported, 2 cannot verify, 1 outdated. The chapter text carries no `[VERIFY]` tag (they were moved to the handoff file); of the 11 open items in `docs/production/handoff/ch13.md`, 6 are resolved (1, 5, 6, 7, 8, 9), 3 are partly resolved (2 Chesney & Citron, 3 CHI items, 4 Ho/Shan/Hönig) and 1 stays open for want of a primary source (10, Arup status). Item 11 (Lab 13.4 consent forms) is an instructor-package task, not a fact-check item.

Access notes: federalregister.gov HTML pages redirect automated fetches to an "unblock" page; the Federal Register API and XML full text were read instead. dl.acm.org, openaccess.thecvf.com, cell.com, congress.gov bill pages, papers.ssrn.com, lawcat.berkeley.edu and weforum.org returned HTTP 403; nhpr.org was not reached (the NHPR story was read on its NEPM republication); npr.org timed out in the fetch tool and was read with curl; Crossref returned HTTP 429 to the fetch tool and was read with curl and a contact header. The Drive connector read Şeker (2015) directly; a second Drive connector call was refused by the permission classifier and was not needed. Search-result snippets are marked ◐.

| # | Source | What was opened | Status | Note |
|---|---|---|---|---|
| S1 | Hong Kong SAR Government (2024, Jun 26), LCQ9 | build/ch13/src/lcq9.txt (full reply) | ✓ | Issued HKT 11:05. Says "informant", not "employee"; no company, role or office; no US dollar figure. HK$200 million; five accounts; "end-January 2024" report; "Police believed" pre-recorded, generated from downloaded public clips and voices; ended meeting "under some pretext"; instant messaging; "still under Police investigation". Four police verification methods incl. Scameter and 18222. Also a May 20, 2024 second case (about HK$4 million) and a 2023 face-swap loan syndicate (nine arrests), not used in the chapter. |
| S2 | Chen & Magramo (2024, Feb 4), CNN | build/ch13/src/cnn_6504a3.txt | ✓ | Published and updated Feb 4, 2024, 2:31 AM ET. Briefing "on Friday" (Feb 2). Chan quoted via RTHK; first doubt and why set aside attributed to Chan; "discovered when the employee later checked" is CNN's own narration. US$25.6 million attributed to the officer. Also six arrests in a separate identity-card scheme (not this case). |
| S3 | Magramo (2024, May 16; updated May 17), CNN | build/ch13/src/cnn_7ed3fc.txt | ✓ | Spokesperson statement "on Friday" (May 17); "fake voices and images were used"; "none of our internal systems were compromised"; 15 transactions per RTHK; Rob Greig quote; Arup notified police "in January". Browser-tab title differs from the on-page headline. |
| S4 | WEF interview with Arup's CIO (2025) | weforum.org page | ✗ | HTTP 403 (build/ch13/src/wef.html). Not used in the chapter. |
| S5 | Arup case status (arrest, recovery) | Web searches, 2026 | ✗ | No primary source found: no Hong Kong Police press release, court record or Arup statement after June 2024; only secondary case-study pages, which report no arrest or recovery. See C078. |
| S6 | NIST AI 100-4 (Nov 2024) | build/ch13/src/nist.txt (full text) | ✓ | Metadata stripping (including for privacy); watermark robustness and removal; "method-specific detectors"; false positives "extremely damaging". No statement about screenshots or about open-weight models specifically. |
| S7 | C2PA Explainer v2.2 | spec.c2pa.org | ✓ | s.6.1 signing and hash; s.7.2.2 "cannot tell you whether the digital content is true, accurate or factual"; s.7.2.3 metadata can be removed; durable credentials. |
| S8 | Microsoft (2021, Feb 22), C2PA announcement | Live page | ✓ | Founding members Adobe, Arm, BBC, Intel, Microsoft, Truepic. |
| S9 | Google (2025a), Pixel / C2PA | Live page | ✓ | Dated Sept 10, 2025; "first to have Content Credentials built in across every photo created by Pixel Camera"; JPEG captures. |
| S10 | Google (2025b), SynthID Detector | Live page | ✓ | Dated May 20, 2025; "over 10 billion pieces"; early-tester portal and waitlist. |
| S11 | Anthropic, Vision docs | platform.claude.com page (full) | ✓ | 28×28 patches; ⌈w/28⌉×⌈h/28⌉; 1000×1000 = 1,296; two resolution tiers; "does not parse or receive any metadata"; cannot determine whether an image is AI-generated. Model names in the page's examples are current to Oct 2026 and will change. |
| S12 | OpenAI, Images and vision | developers.openai.com page (summary of fetch) | ◐ | 32px patches on newer models, 512px tiles on older; "doesn't process original file names or metadata". Page title not visible in the fetch. |
| S13 | Dosovitskiy et al. (2021) | arXiv abstract | ◐ | 16×16 patches ("16x16 words"); ICLR camera-ready; full text not opened. |
| S14 | Ho et al. (2020) | arXiv abstract; NeurIPS listing | ◐ | Pages 6840–6851 from secondary listings; the NeurIPS page gives none. |
| S15 | Rombach et al. (2022) | arXiv abstract; search listing | ◐ | CVF page 403; pages 10684–10695 from listings. |
| S16 | Wang et al. (2023), VALL-E | arXiv abstract; PDF p. 1 | ✓ | 3-second prompt; 60K hours; Microsoft affiliation. |
| S17 | Carlini et al. (2023) | USENIX page (abstract) | ◐ | "over a thousand training examples"; pages 5253–5270. |
| S18 | Bianchi et al. (2023) | arXiv abstract; Crossref | ◐ | Stereotypes with and without identity words; mitigation ineffective; pp. 1493–1504. |
| S19 | Radford et al. (2023) | PMLR page (abstract) | ◐ | 680,000 hours; pp. 28492–28518. |
| S20 | W3C WCAG 2.2 | TR page (first 100,000 characters); WAI "new in 2.2" | ✓ | SC 1.1.1 wording; Recommendation 5 Oct 2023; TR page edition 12 Dec 2024. |
| S21 | DOJ (2024), final rule, 89 FR 31320 | Federal Register API and full-text XML | ✓ | RIN 1190-AA79; WCAG 2.1 Level AA; effective June 24, 2024; public universities discussed. |
| S22 | DOJ (2026), interim final rule, 91 FR 20902 | Federal Register API; LMC page; search results | ✓ | Document 2026-07663; April 20, 2026; RIN 1190-AA82; 50,000+ entities April 26, 2027; smaller entities April 26, 2028; comments to June 22, 2026. |
| S23 | Gonzalez Penuela et al. (2024), CHI '24 | arXiv abstract; Crossref | ◐ | 16 participants, 2.76/5, 2.43/4; author order Gonzalez Penuela, Collins, Bennett, Azenkot; pp. 1–21. ACM page 403. |
| S24 | Xie et al. (2025), CHI '25 | arXiv HTML v1 (first 100,000 of 137,000 characters); Crossref | ◐ | 14 participants; quotes on unexpected information, independence, hallucination, verification; DOI 10.1145/3706598.3714210; pp. 1–17. "Widely used" not in the paper. |
| S25 | Koenecke et al. (2024), FAccT '24 | build/ch13/src/koenecke.txt (full); Crossref | ✓ | 13,140; 187; 312; 19/13/8/38; 1.4%; Dec 2023 retest 12/187; pp. 1672–1681. |
| S26 | Nightingale & Farid (2022), PNAS | PMC full text | ✓ | 315 / 48.2% (CI 47.1–49.2); 219 / 59.0% (CI 57.7–60.4); 223 / trust 4.82 vs 4.48 (7.7%); 128 of 800 faces. |
| S27 | Mai et al. (2023), PLOS ONE | Europe PMC full text | ✓ | 529 (Prolific); 73% = fakes identified (1,841/2,522); real 67.78%; overall 70.35%; 50 sentences, 100 clips in total, 20 per participant; "older approach" caveat; training +3.8 points. |
| S28 | Köbis et al. (2021), iScience | Europe PMC full text | ✓ | N = 210; 16 videos; accuracy 57.6% (SD 11.6); bias toward authentic; overconfidence. cell.com 403. |
| S29 | Groh et al. (2022), PNAS | Europe PMC full text | ✓ | 15,016 participants; humans ≈ model; crowd means 74–86%. |
| S30 | Chandra et al. (2025), arXiv:2503.02857v5 | build/ch13/src/chandra.txt (full) | ✓ | Tables 1, 3, 5; section 3.1 (TrueMedia.org "was a non-profit application"); 90% lower-bound estimate. |
| S31 | TrueMedia.org, "Shutting down" (2025, Jan 7) | Live page; GeekWire (search snippet) | ◐ | Hosted service closed after Jan 13, 2025; open-source release Jan 27, 2025 (snippet); Georgetown revival (GeekWire snippet, not checked). |
| S32 | Paris & Donovan (2019) | Data & Society page | ✓ | Sept 18, 2019; cheap fake definition. |
| S33 | Dufour et al. (2024), AMMeBa | arXiv abstract and PDF text | ✓ | Context manipulation majority at end of data collection (Nov 18, 2023); AI content "rare until Spring of 2023". |
| S34 | NPR (Bond, 2023, May 22) | Live page (curl) | ✓ | Joint PFPA/Arlington statement; Waters quote; stock dip; blue-check accounts incl. a fake Bloomberg account and RT. No timing for reposts. |
| S35 | Johnson (2024, Feb 6), CyberScoop | Live page | ✓ | YouMail, Nomorobo, Industry Traceback Group; Life Corporation, Lingo Telecom; ElevenLabs link unconfirmed by NH authorities. |
| S36 | FCC 24-17, Declaratory Ruling | docs.fcc.gov PDF | ✓ | Adopted Feb 2, released Feb 8, 2024; CG Docket No. 23-362; TCPA "artificial or prerecorded voice" covers current AI voice generation. |
| S37 | FCC 24-104, Forfeiture Order (Kramer) | docs.fcc.gov PDF | ✓ | Adopted Sept 26, released Sept 30, 2024; $6,000,000; Truth in Caller ID Act; "deepfake generative AI voice message". |
| S38 | Nextgov (DiMolfetta, 2024, Sept 26) | Live page | ✓ | Headline, byline, date. |
| S39 | NHPR (Bookman, 2025, Jun 13), via NEPM | Republication | ✓ | Exact headline; Belknap County jury; not guilty on all charges. |
| S40 | TAKE IT DOWN Act, Pub. L. 119-12 | congress.gov public-law text; WilmerHale alert | ✓ | Approved May 19, 2025; 48-hour removal; one-year implementation. WilmerHale (Jun 15, 2026) confirms May 19, 2026 and FTC enforcement. |
| S41 | Regulation (EU) 2024/1689, Art. 50, Art. 113 | EUR-Lex full text | ✓ | Art. 50(2) marking; 50(4) deepfake disclosure; applies from 2 Aug 2026. |
| S42 | Regulation (EU) 2026/1744 (Digital Omnibus on AI) | EUR-Lex (recitals; operative text truncated) | ◐ | Adopted 8 July 2026; published 24 July 2026; four-month transition for Art. 50(2) marking of systems already on the market; Art. 50 date unchanged. |
| S43 | Lovato et al. (2024), AIES | AAAI OJS page (abstract); Crossref | ◐ | 459 artists; vol. 7(1), pp. 905–916. |
| S44 | Shan et al. (2023), Glaze | USENIX page | ◐ | "more than 1000 artists"; pp. 2187–2204. |
| S45 | Hönig et al. (2025) | arXiv abstract | ◐ | Upscaling defeats protections. |
| S46 | Chesney & Citron (2019) | CLR journal page (full text); UT page; search | ◐ | Vol. 107, December 2019; first page 1753; liar's dividend section; issue number and last page not confirmed. |
| S47 | Şeker (2015), YBS Ansiklopedi 2(2) | Drive file 1lXos207zGxsCOkXfVYoFcRGPlpb4bbzO (full) | ✓ | Byline "Sadi Evren SEKER"; sections 1, 1.2–1.4 match the chapter; no AI content. |
| S48 | Crossref records for 9 DOI-bearing references (Koenecke, Bianchi, Nightingale, Mai, Köbis, Groh, Gonzalez Penuela, Xie, Lovato) | API | ✓ | Authors, titles, venues, pages and DOIs checked; differences listed in `ch13.csv` (Gonzalez; Koenecke pages; Köbis DOI; Lovato volume/pages; Xie DOI). |
| S49 | Dakan & Feller (2025) | Search results only | ✗ | PDF not opened. |
| S50 | Chapter text, calendar, cross-references | Local | ✓ | Reading times recomputed from word counts; Ch. 2 §2.5, Ch. 4 "other" branch, Ch. 8 verdicts, Ch. 9 lateral reading, Ch. 10 §10.6–10.7 and Ch. 12 data gate exist as cited; data/ch13_*.csv all match their sources except the labeling issue in C056; figure SVG text checked, one unsupported hop (C085). |

## Not opened (stated so no row is mistaken for a read)

- Dakan & Feller (2025); the WEF interview; Hong Kong Police Force press releases and court records on the Arup case.
- ACM article pages for Gonzalez Penuela et al. and Xie et al. (403), so ACM article numbers are unconfirmed.
- Full texts of Dosovitskiy et al., Ho et al., Rombach et al., Carlini et al., Bianchi et al., Radford et al., Lovato et al., Shan et al. and Hönig et al. (abstracts or listings only); Xie et al. read to about 73% of its length.
- The operative text of Regulation (EU) 2026/1744; the California Law Review table of contents (issue number, last page).
