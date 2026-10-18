# Chapter 18 — source verification log

Checked 2026-10-18 against primary sources where reachable, for `chapters/18-intellectual-property-law-and-governance.qmd`, the case file `cases/C15-thomson-reuters-ross.md`, every row of `data/ch18_legal_status.csv`, and the open `[VERIFY]` items in `docs/production/handoff/ch18.md`. Status: ✓ verified (text read) · ◐ partly verified (cited passages, an index entry, a mirror or a fetch-tool reading) · ✗ not reachable. Claim-level verdicts are in `ch18.csv`. Counts: 218 rows — 187 supported, 27 partially supported, 0 unsupported, 4 cannot verify, 0 outdated. The chapter carries 8 `[VERIFY]` tags, the case file 3, the data table 2, and the handoff lists 10 open items; all are resolved with replacement text except two: the American Bar Association URL (the ABA site serves a bot check; the opinion itself was read in a mirror) and the ABA Journal citation in the case file (not located).

Access notes (no bot check was bypassed): americanbar.org returns a Cloudflare "Just a moment" page, so Formal Opinion 512 was read in the MCLE-hosted copy. fcc.gov HTML pages return "Access Denied"; the FCC orders were read at docs.fcc.gov. courtlistener.com docket pages return a CloudFront 403 and its docket-entries API needs a login, so docket events were read from its public search index (RECAP document descriptions) and opinions from storage.courtlistener.com copies. gov.ca.gov (403 to a script), leg.colorado.gov (406 to a script) and ftc.gov (404 to a script) pages were read only through the fetch tool's summary, which is marked ◐. decisions.civilresolutionbc.ca returns 403; the Internet Archive PDF was used. statutes.capitol.texas.gov is script-rendered, so Gov't Code 2054.003 was read on texas.public.law. lprb.mncourts.gov returned 404. The two Drive connectors were not needed: the 2014 encyclopedia entry is on the journal's own website.

| # | Source | What was opened | Status | Note |
|---|---|---|---|---|
| S1 | *Thomson Reuters Enterprise Centre GmbH v. Ross Intelligence Inc.*, No. 25-2153 (3d Cir. Sept. 29, 2026) | www2.ca3.uscourts.gov PDF, 28 pages, full text | ✓ | Panel Restrepo, Montgomery-Reeves (author), Bove; argued June 11, 2026. Headed "Opinion of the Court", no "not precedential" legend. n.7 (generative models; DOJ statement of Sept. 1, 2026); p. 22 "25,000 ... headnotes" slip vs. 2,243 on pp. 7, n.3. |
| S2 | *Thomson Reuters v. Ross*, No. 1:20-cv-613-SB (D. Del. Feb. 11, 2025), mem. op. | ded.uscourts.gov PDF, full text | ✓ | License refusal is on p. 3 (case file says p. 2); 2,243 finding p. 12; fair use pp. 15–23; "only non-generative AI is before me" p. 19. |
| S3 | D. Del. 1:20-cv-613 and 3d Cir. Nos. 25-8018 / 25-2153 docket entries | CourtListener RECAP search index (entry descriptions) | ◐ | Complaint D.I. 1 (2020-05-06); D.I. 770–772 (2025-02-11); Ross's § 1292(b) motion D.I. 786 (2025-03-18); certification order and stay D.I. 799 (2025-04-04); memorandum D.I. 804 (2025-05-23); 3d Cir. leave granted D.I. 805 (2025-06-17). Docket HTML blocked. |
| S4 | Ambrogi (2020, Dec. 11), LawSites, "Legal research company ROSS to shut down under pressure of Thomson Reuters' lawsuit" | Page source and fetch tool | ✓ | Title and published time 2020-12-11 read; platform unavailable "as of January 31, 2021". |
| S5 | Ambrogi (2026, Sept. 30; Oct. 12), LawSites; Davis (2026, Oct. 12–13), MediaPost | Fetch tool | ◐ | Opinion first issued under seal, then released; Ross will seek en banc and Supreme Court review; Ross asked to move the rehearing deadline from Oct. 13 to Nov. 3. No remand statement found. |
| S6 | *Bartz v. Anthropic PBC*, order on fair use (N.D. Cal. June 23, 2025, Dkt 231) | CourtListener RECAP PDF, 32 pages | ◐ | Introduction, holdings (p. 9), facts (pp. 1–2, 11) read; rest searched by keyword. Order text says "No. C 24-05417 WHA"; header now 4:24-cv-05417-AMO. |
| S7 | *Bartz*, final approval order (July 20, 2026, Dkt 680) | CourtListener RECAP PDF | ◐ | 482,460 works, ~$3,000 per work, $1.5 billion, final approval and judgment; 54 objections; read by keyword (pp. 1, 4 and release terms). |
| S8 | *Bartz* notices of appeal, Dkt 682, 683, 687, and index of Dkt 676–690 | RECAP PDFs (682, 683) and index | ◐ | 682 and 683 are fee-related (Ninth Cir. Nos. 26-5391, 26-5455); 687 is an objector's request, not read. |
| S9 | Authors Guild (2026, July 21), final-approval post; other news | Fetch tool | ◐ | 54 objections; no payout date. |
| S10 | *Kadrey v. Meta Platforms*, order of June 25, 2025 (N.D. Cal., Dkt 598) | CourtListener RECAP PDF, 40 pages | ◐ | Pages 1–5 and keyword passages read (thirteen authors; "wrong arguments"; market dilution). |
| S11 | *Kadrey* docket entries Dkt 741–873 | CourtListener RECAP search index | ◐ | Interlocutory-appeal motion denied July 8, 2026 (Dkt 767); schedule reset Sept. 16, 2026 (Dkt 839); earlier entry set a Feb. 25, 2027 hearing. |
| S12 | *Getty Images (US) Inc & Ors v Stability AI Ltd* [2025] EWHC 2863 (Ch) (4 Nov 2025) | National Archives HTML, full text extracted | ◐ | Paras. 1–9, 18, 590, 599–600, 757–758 read; the 630,000-character judgment was searched, not read through. |
| S13 | Same, [2025] EWHC 3343 (Ch) (16 Dec 2025), consequentials | National Archives HTML | ✓ | Permission to appeal on the secondary-infringement point; Stability refused permission on trade marks. |
| S14 | *Thaler v. Perlmutter*, No. 23-5233 (D.C. Cir. Mar. 18, 2025) | cadc.uscourts.gov PDF | ◐ | Opening and holding read. 130 F.4th 1039 from CourtListener index. |
| S15 | Supreme Court docket No. 25-449 | supremecourt.gov docket page | ✓ | Petition filed Oct. 9, 2025; "Petition DENIED" Mar. 2, 2026. |
| S16 | U.S. Copyright Office (2025), *Copyright and AI, Part 2* | copyright.gov PDF | ◐ | Table of contents and Executive Summary (pp. i–iii) read. |
| S17 | copyright.gov/ai | Live page | ✓ | Part 2 published Jan. 29, 2025; Part 3 pre-publication May 9, 2025; 88 Fed. Reg. 16,190. |
| S18 | 88 Fed. Reg. 16190 (Mar. 16, 2023) | federalregister.gov raw text | ◐ | "More than de minimis ... should be explicitly excluded." |
| S19 | 17 U.S.C. §§ 102, 106, 107, 401; 15 U.S.C. § 1127; 42 U.S.C. § 2000e-2(k); 28 U.S.C. § 41 | govinfo.gov (2023 edition) | ✓ | Sections as quoted in `ch18.csv`. |
| S20 | 37 C.F.R. § 202.1 | eCFR API (2026-10-01) | ✓ | (a) words and short phrases, slogans. |
| S21 | Regulation (EU) 2024/1689 (OJ L, 12.7.2024) | `build/ch18/src/aiact.txt` (OJ text) | ◐ | Arts. 2, 3(60), 4, 5(1)(c)(f), 14, 26, 50, 53, 113 and Annex III 3–4 read; "tier" does not occur. |
| S22 | Regulation (EU) 2026/1744 (OJ L, 24.7.2026) | EUR-Lex HTML | ◐ | Title, Art. 4 rewrite, Art. 5(1)(ba)–(bb) and (1a), Art. 111(4), amended Art. 113, entry into force (third day) read; recitals skimmed. |
| S23 | European Commission, AI Act regulatory-framework page | digital-strategy.ec.europa.eu | ✓ | "AI Act does not introduce rules for AI that is deemed minimal or no risk ... spam filters". |
| S24 | Directive (EU) 2019/790 | EUR-Lex HTML | ◐ | Art. 4(1)–(3); OJ L 130, 17.5.2019, pp. 92–125 from the ELI page. |
| S25 | EO 14281 and EO 14365 (Federal Register full text); EO 14179 (metadata) | federalregister.gov API and raw text | ◐ | EO 14281 = 90 FR 17537; EO 14365 secs. 3–4; EO 14179 = 90 FR 8741 (title and date only). No later revocation found. |
| S26 | Senate roll-call vote 363, 119th Cong., 1st sess. | senate.gov vote_menu XML | ✓ | July 1, 2025, Blackburn Amdt. 2814 to H.R. 1: 99–1, agreed to. |
| S27 | Pub. L. 119-12 (TAKE IT DOWN Act) | govinfo.gov | ✓ | Secs. 2–3; 48 hours; one-year platform deadline; FTC enforcement. |
| S28 | FTC press release "FTC Begins Enforcing the TAKE IT DOWN Act" and business blog (May 19, 2026) | Fetch tool | ◐ | Direct requests to ftc.gov returned 404. |
| S29 | FCC 24-17 and FCC 24-104 | docs.fcc.gov PDFs | ◐ | Openings and key paragraphs read. |
| S30 | Bookman (2025, June 13), NHPR | nhpr.org live page and fetch tool | ✓ | Byline Todd Bookman; acquitted on all counts. |
| S31 | Texas H.B. 149 and S.B. 1964, enrolled | capitol.texas.gov HTML | ✓ | Secs. 552.001, .051, .052, .056, .057, .105; effective Jan. 1, 2026 / Sept. 1, 2025; § 2054.707; no higher-education carve-out in SB 1964. |
| S32 | Tex. Gov't Code § 2054.003(13) | texas.public.law mirror | ◐ | "including a university system or institution of higher education". Official site script-rendered. |
| S33 | Colorado SB26-189 | leg.colorado.gov via fetch tool | ◐ | Signed May 14, 2026; repeals and reenacts SB 24-205; duties from Jan. 1, 2027. |
| S34 | *X.AI LLC v. Weiser*, No. 1:26-cv-01515 (D. Colo.) | CourtListener RECAP index | ◐ | United States as intervenor plaintiff Apr. 24, 2026. |
| S35 | NYC DCWP, AEDT page | nyc.gov live page | ✓ | Enforcement from July 5, 2023. The Local Law text itself was not opened. |
| S36 | NY State Comptroller, Report 2024-N-6 (Dec. 2025) | osc.ny.gov PDF | ✓ | Highlights and findings read; 32 vs. 22 companies inconsistency; 9 of 12 test calls misrouted. |
| S37 | *Moffatt v. Air Canada*, 2024 BCCRT 149 | Internet Archive PDF (2024-10-13) | ✓ | Paras. 1–35. |
| S38 | *Mata v. Avianca*, ECF 54 (S.D.N.Y. June 22, 2023) | CourtListener PDF | ◐ | Introduction and sanction (jointly and severally, $5,000). Reporter cite via *Kohls v. Ellison* ECF 46 (scratch copy). |
| S39 | LG München I, 42 O 14139/24 (Nov. 11, 2025) | justiz.bayern.de press release; gesetze-bayern.de full text | ◐ | Leitsätze, tenor and press release read; appeal OLG München 6 U 3662/25 e. |
| S40 | Japan Copyright Act (Act No. 48 of 1970), Art. 30-4 | japaneselawtranslation.go.jp; CRIC PDF (2020) | ✓ | Official translation, last version Act No. 52 of 2021. |
| S41 | Open Source Initiative, *Open Source AI Definition 1.0* | opensource.org live page | ✓ | Published 2024-10-28. |
| S42 | Llama 3.1 Community License | raw.githubusercontent.com | ✓ | 700 million MAU term; acceptable-use policy. |
| S43 | Microsoft Learn, Customer Copyright Commitment Required Mitigations | learn.microsoft.com | ✓ | Page updated 2026-07-13. |
| S44 | ABA Formal Opinion 512 (July 29, 2024) | MCLE mirror PDF | ◐ | Opening and competence sections read; americanbar.org blocked by Cloudflare. |
| S45 | UTDSP5017; UTDBP3096 | policy.utdallas.edu | ✓ | Issued 2025-03-24; titles confirmed. |
| S46 | UT Dallas OIT, "Microsoft Copilot available to campus" (Jan. 15, 2025) | Fetch tool | ◐ | Free to students; not approved for confidential data. |
| S47 | Şeker (2014), *YBS Ansiklopedi* 1(2), 5–8 | ybsansiklopedi.com issue page and PDF | ✓ | Contents list pages 5–8; PDF headed "Yazılımların Kaynakları"; criteria list not attributed to Laudon & Laudon. |
| S48 | Laudon & Laudon, *Management Information Systems* (12th ed.) | Open Library record | ◐ | Dated 2012. |
| S49 | Illinois P.A. 103-0804; NY governor's RAISE release; Utah SB 149 enrolled; California SB 53 | ilga.gov, governor.ny.gov, le.utah.gov pages; gov.ca.gov 403 | ◐ | Existence and dates only. |
| S50 | Law-firm alerts on EO 14281 and on *Ross* as the first appellate AI-training ruling | Web search summaries | ◐ | Secondary; used for "reported" statements only. |
| S51 | Chapters 1, 4, 8, 10, 12, 13, 15, 16 | Local files | ✓ | Cross-references; the "three zones" are in Chapter 1, not 10.2. |
| S52 | `build/ch18/count.py` | Run locally | ✓ | Core body 2,886 words; package 4,109; total 10,758. |

## Not opened (stated so no row is mistaken for a read)

- americanbar.org (bot check); fcc.gov and gov.ca.gov HTML pages; courtlistener.com docket pages; the ABA Journal piece cited in the case file.
- The full text of Getty [2025] EWHC 2863 (beyond the cited paragraphs), *Kadrey* (beyond pp. 1–5), *Bartz* Dkt 244 and 437, and the DOJ statement of interest itself (docket entry and the Third Circuit's n.7 only).
- The 2023 *Ross* opinion (694 F. Supp. 3d 467); Colorado SB 25B-004; the New York City Local Law 144 text; any provider terms other than Microsoft's CCC page and the Llama license; the UNESCO competency framework and AI Fluency documents.
