# Chapter 10 — source verification log

Checked 2026-10-18 against primary sources where reachable. Status: ✓ verified (text read) · ◐ partly verified (abstract, archived copy, reproduction or excerpt read) · ✗ not reachable. Claim-level verdicts are in `ch10.csv`. Counts: 130 rows — 106 supported, 20 partially supported, 0 unsupported, 4 cannot verify, 0 outdated. The chapter has 11 `[VERIFY]` tags and the case file 2; 8 and 2 are resolved with replacement text. Three stay open for want of paywalled full text: R8 Figure 1 in the Science version (C02), the Schilke & Reimann "fade" sentence (C79) and the Jiang et al. findings (C103); the Matsuda definition (C24) is a fourth open item without a tag.

Access notes: openai.com, ap.org, science.org, sciencedirect.com, canlii.org, decisions.civilresolutionbc.ca and unesdoc.unesco.org return HTTP 403 to automated fetches; the Internet Archive (web.archive.org) copies below were used instead. The first Drive connector failed to authorize ("Incompatible auth server"); the second Drive connector read Şeker (2016) directly.

| # | Source | What was opened | Status | Note |
|---|---|---|---|---|
| S1 | Perrotta (2023, Feb 17), *The Vanderbilt Hustler* | Live page (raw HTML, text extracted) | ✓ | Byline Rachael Perrotta, Editor-in-Chief; two updates on Feb 17 (7:30 and 9:05 p.m. CST), correction Feb 21. Email dated Feb 16 in the text; the image alt text says Feb. 15, the visible caption says the screenshot was taken Feb. 17. "poor judgment"; spokesperson; classifier's 26%. |
| S2 | Lele (2023, Feb 19), *The Vanderbilt Hustler* | Live page | ✓ | Paraphrases "Peabody's typical process of review for communications"; quotes "were unaware"; does **not** contain "multiple layers of review". Deans step back. |
| S3 | Lele & Faquih (2023, Apr 12), *The Vanderbilt Hustler* | Live page | ✓ | Return April 11; three signers; three killed, five injured; no review outcome. Published headline differs from the chapter's reference title (see C108). |
| S4 | Korn (2023, Feb 22), CNN via KTVZ | Live page | ✓ | Quotes the citation line, "last Friday", "recent Michigan shootings", and Benbow's statement "to CNN" on Tuesday with "multiple layers of review". |
| S5 | Benbow, statement, peabody.vanderbilt.edu/statement.php | Internet Archive capture of 2023-02-21 19:39 UTC | ✓ | Live URL is 404 (2026-10-18) and in a 2024 capture. Undated page. Full text read, with the "multiple layers of review" sentence. The WKRN (Feb 21, 2023) and The Hill pages link to it. |
| S6 | WKRN (2023, Feb 21) | Live page | ✓ | Confirms the statement was posted on the school's website; quotes it. |
| S7 | NPR (2023, Feb 13), "3 students and a suspect are dead after Michigan State University shooting" | Live page | ✓ | Metadata title matches; on-page headline changed Feb 14; 3 killed, 5 injured; 8:18 p.m. ET. |
| S8 | OpenAI (2023), "New AI classifier for indicating AI-written text" | Internet Archive captures of 2023-07-21 and 2024-01-02 | ✓ | 26% / 9% on a "challenge set of English texts"; "As of July 20, 2023, the AI classifier is no longer available due to its low rate of accuracy." |
| S9 | Noy & Zhang (2023b), working paper, Mar 10, 2023 (and Mar 2 version) | PDF read (MIT economics) | ✓ | 444 participants; Figure 1 = time and grades (panels a–d); "68% of treated participants report submitting ChatGPT's initial output without editing it"; treated vs raw ChatGPT output grades. |
| S10 | Noy & Zhang (2023a), *Science* 381(6654) | Crossref abstract; Unpaywall/OpenAlex/Europe PMC checked | ◐ | Full text closed (science.org 403; only the SSRN working paper is open). Abstract: 453 participants, −40% time, +18% quality, inequality down. Fig. 1 content and the 68% figure in the published version **not** checked. |
| S11 | Liu, Mittal, Yang & Bruckman (2022), CHI '22 | Full text (build/ch10/liu-2022-chi.txt) | ✓ | 229 recruited, 147 analyzed, 49 per condition, 10 interviewees; all emails human-written. |
| S12 | Liang et al. (2023), *Patterns* 4(7) 100779 | PMC10382961 full text | ✓ | 7 detectors; 91 TOEFL + 88 U.S. eighth-grade essays; 61.3%; 97.8%; 19.8%; 61.3% → 11.6%; "Elevate the provided text…" on ChatGPT-3.5 Common App essays. |
| S13 | Jiang, Hao, Fauss & Li (2024), *Computers & Education* 217, 105070 | Crossref record; search-engine summary of the abstract; ETS conference transcript | ◐ | ScienceDirect 403; full text closed. Volume resolved. Findings (near-perfect detection; no bias in well-sampled GRE data) unconfirmed from the paper itself. |
| S14 | Weber-Wulff et al. (2023), *IJEI* 19, Art. 26 | Abstract (OpenAlex), Crossref | ◐ | 12 tools + Turnitin + PlagiarismCheck = 14; "neither accurate nor reliable". |
| S15 | Kirchenbauer et al. (2023), ICML, PMLR 202 | PMLR page (abstract, BibTeX) | ◐ | Pages 17061–17084; green-token watermark. Full text not read (Deep section only). |
| S16 | Sadasivan et al. (2023), arXiv:2303.11156 | arXiv API record (v1 Mar 17, 2023; v4 Jan 17, 2025) | ◐ | Abstract of v4 read; authors and title confirmed. |
| S17 | Kruger, Epley, Parker & Ng (2005), *JPSP* 89(6) | PubMed 16393025 abstract; Crossref | ◐ | Five experiments; egocentrism in Studies 4–5. Full text paywalled; percentages not read. |
| S18 | Matsuda (2001), *JSLW* 10(1–2) | Crossref; abstract on ASU Pure | ◐ | Abstract supports §10.6; the definition (cited to p. 40) is not verified. |
| S19 | Doshi & Hauser (2024), *Sci. Adv.* 10(28) | Abstract (OpenAlex), Crossref | ◐ | Findings as stated; open access, full text not needed for the chapter's claims. |
| S20 | Agarwal, Naaman & Vashistha (2025), CHI '25 | arXiv 2409.11360 v3 full text | ✓ | 118 participants (60 India, 58 U.S.); GPT-4o autocomplete; completion time −35% vs −30% (n.s. difference); Americans gained more per accepted suggestion. |
| S21 | Jakesch et al. (2023), CHI '23 | Abstract (OpenAlex), Crossref | ◐ | N = 1,506; judges N = 500. |
| S22 | Hancock, Naaman & Levy (2020), *JCMC* 25(1) | Abstract (OpenAlex), Crossref | ◐ | Definition as paraphrased. |
| S23 | Hohenstein et al. (2023), *Sci. Rep.* 13, 5487 | Abstract (OpenAlex), Crossref | ◐ | Two randomized experiments; findings as stated. |
| S24 | Schilke & Reimann (2025), *OBHDP* 188, 104405 | Abstract (OpenAlex, Semantic Scholar), Crossref; University of Arizona news release (via search) | ◐ | 13 experiments; exposure effect stronger than disclosure effect (abstract). Participant count not in the abstract (">5,000" in the news release; "3,000+" in another summary). "Fade" claim not in the abstract. |
| S25 | Microsoft & LinkedIn (2024), *AI at Work Is Here. Now Comes the Hard Part* | Report page (via fetch tool) | ◐ | 31,000 / 31 markets; Edelman; Feb 15–Mar 28, 2024; published May 8, 2024; 52% of AI users reluctant to admit use for most important tasks. |
| S26 | Barrett (2023, Aug 16), AP, "Standards around generative AI" | Internet Archive captures of 2023-12-30 (blog.ap.org) and 2025-12-20 (ap.org) | ✓ | Same text in both captures. |
| S27 | *Moffatt v. Air Canada*, 2024 BCCRT 149 | Internet Archive PDF capture of 2024-10-13 | ✓ | Paras. 24–32 read; "static page or a chatbot" is para. 27; "no reason why Mr. Moffatt should know…" is para. 29. |
| S28 | AP (2025, Oct 7), via News4JAX | Live page | ✓ | Revised report disclosed Azure OpenAI; Rudge; refund. DEWR (2025b) checked in Chapter 9 (see ch09-sources S4). |
| S29 | Şeker (2016), "Sosyal Müşteri İlişkileri Yönetimi / Social CRM", *YBS Ansiklopedi* 3(3) | Drive file 1WM_8xQ6x5y7m1NGlm5wLki2A59O9LtLO read through the Drive connector; local extract build/ch10/ftf-sosyal-crm.md | ✓ | Four PDF pages; running numbers 38, 39, 40 on pages 2–4, page 1 unnumbered (page range needs a check against the volume's table of contents). Running header wrongly reads "İş Planı (Business Plan)". Facts limited to this file. |
| S30 | UNESCO, *AI competency framework for students* (2024) | Secondary summaries only | ◐ | unesdoc.unesco.org 403. |
| S31 | Crossref records for the 13 DOI-bearing journal and proceedings references | API | ✓ | Authors, title, container, volume, pages and DOI match, except the items listed in `ch10.csv` (Jiang volume; Lele & Faquih title; Perrotta update wording; Microsoft title; Kirchenbauer pages). |
| S32 | Calendar and docs/syllabus.md | Local | ✓ | Mar 8, 2027 (Mon); Mar 11, 2027 (Thu); Feb 13–18 and Apr 11, 2023 weekdays. |

## Not opened (stated so no row is mistaken for a read)

- Noy & Zhang (2023a) full text; Kruger et al. (2005), Matsuda (2001), Jiang et al. (2024) and Schilke & Reimann (2025) full texts; the UNESCO framework PDF.
- Joseph's Feb 17 apology email itself (only the Hustler's quotation of it).
