# Chapter 19 — source verification log

Checked 2026-10-18 against primary sources where reachable (chapter `chapters/19-ai-across-disciplines-field-guides.qmd`, cases C22–C28, `data/ch19_*.csv`, handoff `[VERIFY]` items). Status: ✓ verified (text read) · ◐ partly verified (abstract, archived copy, preprint, reproduction or secondary copy read) · ✗ not reachable. Claim-level verdicts are in `ch19.csv` (ids F001–F170; "F" is used so they do not collide with case ids C22–C28). Counts: 170 rows — 133 supported, 27 partially supported, 3 unsupported, 1 outdated, 6 cannot verify. The chapter text has 0 `[VERIFY]` tags; the case files have 2 (C22 affiliation list: resolved; C24 later versions: resolved), the handoff has 7 tagged items plus the two status checks requested (see the last section).

Access notes: science.org, ed.gov and hhs.gov return HTTP 403, nhtsa.gov pages answer "Access Denied" (Akamai) and apa.org returns an empty challenge page; none was pursued; official alternates used instead (Internet Archive captures, NHTSA's static.nhtsa.gov documents and bulk data, PMC, Crossref, PubMed). jamanetwork.com, journals.aps.org, catalyst.nejm.org, michiganmedicine.org, midas.umich.edu, si.umich.edu and ihpi.umich.edu returned 403. pub.aicpa.org (the official Code) serves a login/JavaScript shell. The Texas Secretary of State rules site has moved (texreg.sos.state.tx.us shows a move notice). ftc.gov answered HTTP 404 to curl with a browser user agent but served the page through the fetch tool. No attempt was made to get past any bot check. The TPMG ambient-scribe line was checked only against `build/sources/nejm-catalyst-ambient-scribes.md`; no NEJM Catalyst page or third-party repost was opened.

| # | Source | What was opened | Status | Note |
|---|---|---|---|---|
| S1 | Assael et al. (2022), *Nature* 603:280–283 | Full text via PMC8907065 | ✓ | Received Aug 16, 2021; accepted Jan 19, 2022; published Mar 9, 2022. Table 1: experts 25.3% top-1 (CER 59.6); Ithaca 61.8% (CER 26.3; top-20 78.3); experts + Ithaca 71.7% (CER 18.3); region 70.8% top-1 of 84; dates 29.3 years (median 3; Methods 28.7). I.PHI 78,608 of PHI's 178,551. Evaluators: two graduate students of ancient history, 7 years' training. "Designed to assist and expand the historian's workflow"; no "replacement" wording. Affiliations: DeepMind, Ca' Foscari Venice, Harvard CHS, Athens UEB, Oxford. |
| S2 | Assael et al. (2025), *Nature* 645:141–147 (Aeneas) | nature.com full text; PubMed 40702185; Crossref | ✓ | Online Jul 23, 2025. Abstract: paired historians outperform humans and AI alone on restoration and geographic attribution; dating 13-year distance. Latin inscriptions. Author list differs from the chapter's reference (14 authors incl. N. Dietrich). |
| S3 | Zillow (2021a), press release, Feb 25, 2021 | q4cdn PDF | ✓ | "More than 20 cities"; "limited subset of homes"; AI "including ... a deep-learning neural network". |
| S4 | Zillow Group (2021b), Q3 2021 shareholder letter (8-K Ex. 99.3) | SEC page | ✓ | "unable to accurately forecast future home prices at different times in both directions"; $304 million write-down; 9,680 bought, 3,032 sold, 9,790 in inventory; ~25% workforce cut; footnote 1 on the suspension two weeks earlier. No use of the word "algorithm". |
| S5 | Zillow Group (2021c), Q3 results release (8-K Ex. 99.1) | SEC page | ✓ | $304 million; $240–265 million Q4 losses; wind down; "unpredictability in forecasting home prices". |
| S6 | Veiga (2021, Nov 2), AP | Syndicated copy at newschannel9.com | ◐ | Byline Alex Veiga; "about $340 million" (conflicts with the filing's $304 million); headline spells "layoff". Not cited in the chapter text. |
| S7 | Wong et al. (2021), *JAMA Intern Med* 181(8):1065–1070 | Full text via PMC8218233; PubMed 34152373; Crossref | ✓ | All figures match: 38,455 hospitalizations, 27,697 patients, Dec 6, 2018 – Oct 20, 2019; AUC 0.63; 2,552 (7%); 1,709 missed (67%); 6,971 alerts (18%); Epic's 0.76–0.83 from internal documentation; single center. Online Jun 21, 2021. |
| S8 | Reuter (2021, Jun 23), MedCity News | Live page | ✓ | Real title: "Popular sepsis prediction model works 'substantially worse' than claimed, researchers find"; byline Elise Reuter; Epic's response quoted. The chapter's title is wrong. |
| S9 | Michigan Medicine (2021) news release | — | ✗ | 403 (also ihpi.umich.edu, midas.umich.edu, si.umich.edu). Not needed for the chapter's claims. |
| S10 | Wong et al. (2026), *JAMA Netw Open* 9(2):e260181 | PubMed 41758510 abstract | ◐ | Multicenter validation of Epic Sepsis Model version 2 (Aug 31, 2023 – Mar 11, 2025). Resolves C24 "[VERIFY] later versions". |
| S11 | Tierney et al. (2024; 2025), *NEJM Catalyst* | `build/sources/nejm-catalyst-ambient-scribes.md` (editor's notes); Crossref metadata | ◐ | Notes only; pages paywalled/403 and not opened. Authors, volume/issue and dates match Crossref (5(3) Feb 21, 2024; 6(5) Apr 16, 2025). |
| S12 | Argyle et al. (2023), *Political Analysis* 31(3):337–351 | Cambridge abstract and reference list; arXiv:2209.06899 v1 full text | ◐ | Published text not available on the page; preprint read. ANES 2012/2016/2020 plus "Pigeonholing Partisans" data. |
| S13 | Bisbee et al. (2024), *Political Analysis* 32(4):401–416 | Full text (open access) | ✓ | 11 groups, 0–100 thermometers, 2016 and 2020 ANES, ChatGPT 3.5 Turbo; 48% of coefficients differ, 32% flip sign; April/June/July 2023 runs of "a simpler version of our main prompt"; June not distinguishable from April by placebo test, July substantially different. |
| S14 | Szymanski et al. (2023), *Nature* 624:86–91 | PMC10700133 (corrected text); Internet Archive capture of 2023-11-29 (original) | ✓ | Original abstract: "realized 41 novel compounds from a set of 58 targets"; original title "...of novel materials". Methods: manual analysis "when the automated refinement gives a poor fit". Crossref/Nature now show the corrected title. |
| S15 | Szymanski et al. (2026), Author Correction, *Nature* 650:E1 | Full text via PMC12872444 | ✓ | 36 of 40 confirmed, 4 inconclusive; one compound (Zn2Cr3FeO8) removed; "new to the prediction platform, not necessarily new to science"; re-analysis peer-reviewed post-publication. Nature article page (Oct 18, 2026) shows no retraction. |
| S16 | Leeman et al. (2024), *PRX Energy* 3:011002 | Crossref abstract | ◐ | 43 products; "no new materials"; "Automated Rietveld analysis ... not yet reliable"; two thirds likely known disordered versions. APS full text 403. ChemRxiv preprint created Jan 7, 2024 (Crossref). |
| S17 | Quach (2024, Jan 31), The Register | Live page | ✓ | Palgrave: "should be retracted"; Ceder: "not peer reviewed ... multiple errors". |
| S18 | Tesla (2023), Part 573 report 23V-838 | static.nhtsa.gov PDF | ✓ | 2,031,220; Dec 12, 2023; "may not be sufficient to prevent driver misuse"; OTA remedy; "While not concurring"; chronology PE21-020 Aug 13, 2021, EA22-002 Jun 8, 2022, decision Dec 5, 2023. |
| S19 | NHTSA ODI (2024a), EA22002 closing resume | static.nhtsa.gov PDF | ✓ | 956 crashes analyzed, 467 remaining in scope, 13 fatal crashes / 14 deaths; "critical safety gap". |
| S20 | NHTSA ODI (2024b), RQ24009 opening resume | static.nhtsa.gov PDF | ✓ | Opened Apr 25, 2024; post-remedy crashes; opt-in and reversible remedy part. |
| S21 | NHTSA ODI investigations flat file | static.nhtsa.gov/odi/ffdd/inv/FLAT_INV.zip (Last-Modified Oct 18, 2026) | ✓ | RQ24009: open date 20240425, close date empty. nhtsa.gov record page 403 (not pursued). |
| S22 | Wang et al. (2025), EdWorkingPaper 24-1054; arXiv:2410.03017 v3 | edworkingpapers.com page and PDFs (cover "No. 24-1054"; Nov 2025 version); arXiv v3 PDF; Research Square page; Crossref, OpenAlex | ✓ | Figures match both the Nov 2025 EdWP and arXiv v3 (783 tutors, 1,013 students, 62→66%, 56→65%, $20, tutor-facing only, ~29% of treatment sessions used the tool). Page's suggested citation says "24-1056". No journal version found. Research Square: "not peer reviewed by a journal". |
| S23 | Handa et al. (2025, Apr 8), Anthropic Education Report | Live page | ✓ | 574,740; 18-day window; 36.8% in the key findings, 38.6% in the body; business 8.9 vs 18.6; health 5.5 vs 13.1; humanities 6.4 vs 12.5; natural sciences 15.2 vs 9.2; 14 authors in BibTeX. Chart image not read. |
| S24 | Liang et al. (2024), *Nat Mach Intell* 6:744–753; arXiv:2402.05160 | nature.com abstract (paywalled preview); arXiv full text | ◐ | Abstract matches the chapter; 15.4% and 17.4% from the arXiv text; journal full text not read. |
| S25 | Mitchell et al. (2019), FAT* '19 | arXiv:1810.03993 full text; Crossref | ✓ | Nine sections; Figure 1 summary; Figure 2 smile detector; Figure 3 toxicity detector; pp. 220–229. |
| S26 | NIH NOT-OD-23-149 (Jun 23, 2023) | Live page | ✓ | Prohibits reviewers' use of generative AI "for analyzing and formulating peer review critiques"; "violate NIH's peer review confidentiality requirements". |
| S27 | ICMJE Recommendations | Live pages (home, Section V.A) | ✓ | "Updated January 2026"; chatbots "should not be listed as authors"; disclosure required. |
| S28 | Texas H.B. 149 (TRAIGA) and S.B. 1188 | capitol.texas.gov enrolled texts | ✓ | Sec. 552.051(f) health-care disclosure; effective Jan 1, 2026. Sec. 183.005 review and disclosure; effective Sept 1, 2025. |
| S29 | TBPELS letter, Nov 14, 2024 (Request No. 71) | PDF | ✓ | "should be aware" (not "must understand"); responsibility for sealed work; competence rule 137.59; data rule 137.61. |
| S30 | 22 TAC §137.33 | Cornell LII copy | ◐ | Texas SOS site moved; LII text: seal own or directly supervised work, and reviewed/selected standards. |
| S31 | NSPE Code of Ethics | Live page | ✓ | II.2.b wording; "As Revised July 2019". |
| S32 | ANA 2025 Code of Ethics, Provision 3 | codeofethics.ana.org pages; nursingworld.org product page; ANA news release (fetch tool) | ✓ | 3.1 Privacy and Confidentiality. News release dated Jan 29, 2025; no approval date or body. Errata/reprint noted. |
| S33 | AICPA Code 1.700.001 | Journal of Accountancy (Mar 1, 2015) via fetch tool; official site pub.aicpa.org | ◐ | Official site: login/JS shell. JofA quotes the rule and exceptions. |
| S34 | FTC press release, Sept 25, 2024 | Fetch tool | ✓ | "Operation AI Comply". |
| S35 | AAPOR task force report (May 2026) | PDF (full text); announcement page | ✓ | Required disclosures: tasks AI was used for, number of human respondents, validation and human oversight. Report disclaimer: authors' opinions, not necessarily the Executive Council's. Announcement dated 05/08/2026. |
| S36 | Springer Nature AI policy | Live page (Oct 18, 2026); Internet Archive captures 2025-03-16 to 2026-10-10 | ◐ | Undated. Current text is a risk-assessment framework with "Assigning authorship or accountability to AI systems" and "Creating photorealistic images (deepfakes)" as not permitted; older text in captures through 2026-05-15 (no LLM authorship; AI images/videos not permitted with exceptions). |
| S37 | Science journals' editorial policies | Internet Archive capture 2026-06-14 (live page 403) | ◐ | Undated. AI tools may not be authors; disclosure; AI-generated images and multimedia not permitted without editors' permission. |
| S38 | MLA Style Center | Live pages | ✓ | Updated post "Published 13 August 2025"; the March 2023 post points to it. |
| S39 | COPPA Rule, 90 FR 16918 (Apr 22, 2025) | govinfo PDF | ✓ | Effective Jun 23, 2025; compliance Apr 22, 2026 (safe-harbor items earlier). |
| S40 | UTDBP3096 | policy.utdallas.edu | ✓ | Three classes: Confidential, Controlled, Public. |
| S41 | UT Dallas OIT "Initial Guidelines for Gen AI" | Live page at the redirected URL; Wayback CDX | ✓ | "No FERPA or HIPAA information may be used in Generative AI tools." Undated; cited URL 301-redirects to /about/oit-ai-studio/initial-guidelines/. Old URL first archived 2026-02-04. |
| S42 | UT Dallas OIT AI Studio page | Live page | ✓ | Microsoft Copilot Chat "approved AI browser-based chat solution for UTD staff, faculty, and students". |
| S43 | UT Dallas Office of Human Subjects Protections pages | Live pages (main, obtaining approval, forms and checklists, policies, guidance) | ✓ | No AI guidance found. |
| S44 | 45 CFR 46.116 and 46.108 | eCFR (46.116); govinfo CFR 2023 PDF (46.108) | ✓ | 46.116(a)(1) consent; 46.108(a)(3)(iii) changes need IRB approval first. |
| S45 | UT Dallas 2022/2024/2026 undergraduate catalogs | catalog.utdallas.edu | ✓ | Healthcare Studies BS; Speech, Language, and Hearing Sciences BS (no speech-language pathology major); no "Arts and Technology" degree. |
| S46 | Şeker (2016), *YBS Ansiklopedi* 3(3) | Drive extract `build/ch19/ftf-duygu-analizi.md` | ✓ | Sections 2.1, 2.2, 2.7, 2.8; 85%/70% with reference [19] (Guardian, June 2013); Eylül 2016. |
| S47 | Crossref records for the 11 DOI-bearing references | API | ✓ | Authors, title, container, volume, pages, DOI match, except Aeneas authors, the 2023 A-Lab title (now corrected) and as listed in `ch19.csv`. |
| S48 | docs/syllabus.md; chapters 8, 12, 14, 15, 16, 18; data/ch19_*.csv; handoff file | Local | ✓ | Dates, table text, definitions and CSV values checked. |

## Handoff `[VERIFY]` items (docs/production/handoff/ch19.md)

| Item | Result |
|---|---|
| ANA Code approval date | Not published on ANA pages; release date Jan 29, 2025 (news release). Chapter prints only "2025": no change; drop the tag. |
| AICPA Code site | Official site unreadable (login shell). Rule text via Journal of Accountancy (2015). Open. |
| Springer Nature page date | None printed; policy text changed between 2026-05-15 and 2026-10-10 captures. |
| Science policy page | Read in the 2026-06-14 Internet Archive capture; undated. |
| UTD OIT page date | None printed; URL moved (update reference). |
| UTD IRB guidance on AI | None found on OHSP pages. |
| NHTSA RQ24-009, October 2026 | Open per NHTSA's ODI flat file (modified Oct 18, 2026). |
| Tutor CoPilot peer review | No journal version found; still a working paper/preprint. |
| Epic Sepsis Model later versions (C24) | Version 2 exists (2022); validated in JAMA Netw Open, Feb 2026. |

## Not opened (stated so no row is mistaken for a read)

- NEJM Catalyst pages (Tierney et al., 2024, 2025); journal full texts of Liang et al. (2024), Argyle et al. (2023, published version), Leeman et al. (2024); the official AICPA Code; nhtsa.gov record pages; science.org live pages.
- Chemistry World (Jan 16, 2024) article named in `cases/C26`; Michigan Medicine's 2021 news release named in `cases/C24`.
- The Guardian (2013) article behind Şeker's 85%/70%; the Texas SOS rule text; chart image in the Anthropic report.
