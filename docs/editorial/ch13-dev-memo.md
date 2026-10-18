# Chapter 13 — developmental memo (2026-10-18)

Inputs: four independent reviews run in parallel without sharing reports — subject-expert reviewer (Opus; 27 findings, 4 must-fix), pedagogy reviewer (Opus; 18 findings), student-reader panel (Maya / Daniel / Ayşe, Sonnet), fact-checker (Sonnet; docs/factcheck/ch13.csv, 148 claims: 113 supported, 29 partly supported, 3 unsupported, 2 cannot verify, 1 outdated), plus the editor's nine decisions and the newest book-wide rules in the production brief. The author delegated editorial choices (D19), so the chapter agent applied the changes below in draft v2. Draft v1 is kept in build/ch13/ch13-v1-prereview.qmd.

## Decisions — accuracy (fact-checker, subject expert)

| # | Change | Why |
|---|---|---|
| A1 | C10 label kept: tree "other (misuse), documented" plus chain link 2; one sentence in the Case Study that the deepfake is an AI output; Chapter 15 adds the payment-control side | Expert #1; brief rule on input-side harms (Arup labeled on the tree and chain) |
| A2 | TrueMedia: "The authors built the benchmark with TrueMedia.org, a nonprofit deepfake-detection service (closed to the public in January 2025)"; same in F13.12 | Expert #2; fact-check C063 (outdated); editor decision 7 |
| A3 | EU AI Act sentence rewritten: providers mark content machine-readably, deployers disclose deepfakes (Art. 50); "As of October 2026" with August 2, 2026 and the December 2, 2026 transition (Regulation (EU) 2026/1744); reference added | Expert #3; fact-check C097; brief rule |
| A4 | Koenecke denominators: "187 of the 13,140 segments (about 1.4%) … 312 transcriptions … roughly 1% of transcriptions … 38% of those 312"; F13.8 footnote explains the overlap (19 + 13 + 8 > 38) | Expert #4; panel (Daniel); editor decision 7 |
| A5 | Chandra benchmark: user-flagged real and fake media, labeled by the authors; original-test AUCs re-run by the authors; best of 22 anonymized commercial tools; audio result partly credited to labeling; "none was right 90% of the time; the authors estimate trained analysts are right at least that often" | Expert #5–6; panel (Daniel) |
| A6 | Gemini SynthID check (since Nov 2025) added to "a general chat tool is not a detector": a "no" proves nothing about other generators | Expert #7; editor decision 7 |
| A7 | Opening: the government reply's "informant"; CNN cited for the finance employee and the US$ conversion; "pre-recorded" stated by the record, "police believe" for how it was generated; the two accounts described as compatible | Expert #8, #16; fact-check C002, C006 |
| A8 | Police advice quoted fully in 13.8 (head-turn test, a lead at best; identity through conversation; phone check for relatives or friends asking for money; scam-checking tool); the book adds "a call counts only if you place it to a number you already have" | Expert #9 |
| A9 | "A channel the fraudsters did not control" marked as the book's reading (13.7, Summary); Summary now says the later check exposed the fraud "too late" | Expert #10; panel (Daniel); editor decision 7 |
| A10 | DOJ: primary 2026 rule cited (91 FR 20902, April 20, 2026), with April 26, 2027 and 2028; moved into a dated box | Expert #11; fact-check VERIFY 1; pedagogy #16 |
| A11 | Screenshot claim marked as the book's reading, with the C2PA soft-binding caveat; F13.9 "often leaves it behind"; C2PA explainer 2.3 cited | Expert #12, #22; fact-check C046 |
| A12 | 13.2 adds autoregressive and hybrid generators; Carlini "mostly images that appeared many times"; one dated clause on commercial voice cloning (Chapter 15) | Expert #13, #23, #27 |
| A13 | "Much misleading media needs no AI" dated to fact checks collected up to November 2023 | Expert #14 |
| A14 | Robocall "documented" cites the FCC Forfeiture Order FCC 24-104 (Sept 26, 2024), added to references; FCC 24-17 dates (adopted Feb 2, released Feb 8) | Expert #15; fact-check C088, C091 |
| A15 | Patches "about 14 to 32 pixels on a side (16 in the original research)"; "shrunk first if the image is large"; metadata vs. file names attributed exactly | Expert #17–18; fact-check C018, C022 |
| A16 | Mai et al. 73% = speech deepfakes correctly identified (overall 70.35%): text, CSV, F13.11 (now two panels, faces and voices), Lab 13.4 | Fact-check C056; pedagogy #17; panel (Daniel) |
| A17 | Prediction box: 128 faces per participant from a pool of 800 (400 real, 400 generated); "about 11 percentage points (this book's calculation)" | Fact-check C051; panel (Maya) |
| A18 | F13.18 "spread on Twitter that morning"; Pentagon text dated "on the morning of May 22" | Fact-check C085 |
| A19 | From the Field: "publishes news against the business"; Şeker initials "S. E." | Fact-check C101, C142 |
| A20 | Xie et al.: "Be My AI"; Gonzalez Penuela et al. reference corrected; open-weight claim separated from the NIST citation | Fact-check C035, C117, C048 |
| A21 | Arup status: "As of October 2026, we found no public report of an arrest or a recovery in this case" | Expert #21; fact-check C078; editor decision 8 |
| A22 | Police officer no longer named in running text (D-10.8); Greig's quote cut from the chapter (kept in the case file) | Expert #25; editor decision 7 |
| A23 | References: Koenecke pages; Köbis DOI and order; Lovato volume, pages, DOI; Xie and Gonzalez Penuela DOIs; Shan and Ho pages; Hönig URL; Bond (NPR), Bookman (NHPR); Regulation OJ date; W3C edition; DOJ 2024 and 2026; FCC 2024a/b; Google 2025c; League of Minnesota Cities and Nextgov replaced by primary records | Fact-check report |

## Decisions — learning design (pedagogy, student panel)

| # | Change | Why |
|---|---|---|
| L1 | Fast route self-standing: the recap moved to the top of 13.7 and now defines deepfake, content credential and watermark; the plain-words box adds deepfake, content credential, watermark, lead, tree and chain, stopping rule, disclosure and process evidence; Hana and "zine" introduced at 13.7; the Warm-up is part of the fast route; the artifact states it assumes 13.4–13.5 or the recap | Pedagogy #1, #9; panel top 1; editor decision 1 |
| L2 | One absent-signal wording everywhere: "a missing signal proves nothing" (text, F13.10, F13.13, F13.19, keys, rubric) | Pedagogy #10; editor decision 2 |
| L3 | Book-wide definitions: deepfake narrowed to synthetic media of a real person or event; cheap fake "without generative AI"; handoff glossary rows updated verbatim | Pedagogy #8; editor decision 2 |
| L4 | Honest times: fast ~24 min, full ~57 min (~66 with extras); end-of-chapter questions listed as extra; artifact 80–100 min with the brief, disclosure rule and re-check timed; week-10 advice "this week if you have time, otherwise week 11" | Pedagogy time table and #2; panel; editor decision 3 |
| L5 | Lab times: Lab 13.2 35 min (10-minute version: one item); Lab 13.4 gets a real 10-minute version (five clips); Lab 13.1 data gate 5 min and the audio extension timed separately | Pedagogy #18; panel (Ayşe); editor decision 3 |
| L6 | Every faded example and B4 supplies its facts (poster size and labels; mockup parts; caption phrases; three photos' signals; renders' label position; vendor reports no false-positive rate; voice message details; club's posting facts; B4's three findings); the 13.7 faded prompt states the control in plain words | Pedagogy #3–4; brief rule; editor decision 4 |
| L7 | Reason for naming channels by role (numbers change; a written list can be copied or faked) | Panel (Daniel, Maya); editor decision 4 |
| L8 | Second worked example in 13.7 ends *supported* (a 1920s archive photo checked through the archive's own site) | Pedagogy #11; editor decision 6 |
| L9 | A2, A6 and A10 distractors rebuilt from named misconceptions (M1, M4, M3); A5 and A7 turned into reasoning items; CSQ1 says the accounts differ in detail; CSQ5 key limited to this case; Spaced Review 4 features "a designer", not Hana | Pedagogy #12–15; editor decision 6 |
| L10 | Lab 13.2 and the artifact items: public-domain originals with no people; dated search-result sheets for generated items; P2 is a fictional, non-local place (Port Calder), eLearning only, with a visible "COURSE SAMPLE: GENERATED" band and credentials; P2 key rewritten | Pedagogy #5–6; editor decision 5 |
| L11 | Privacy: the file and its location data still reach the provider (13.1); Lab 13.1 excludes the student's home; Hana removes location data before uploading | Pedagogy #7; editor decision 5 |
| L12 | Plain-language pass: pretext → "with an excuse"; "set that doubt aside" → "stopped doubting"; glosses for zine, mural, accounts payable, controller, robocall, open-weight, benchmark, guardrails, memorization, spectrogram, calibration (Lab 13.4), automation bias and proxy (Spaced Review); RTHK spelled out | Panel top 3; pedagogy #9; editor decision 9 |
| L13 | Statistics density cut: diary study as one number with its scale; detector dataset as "over 100 hours of video and audio and about 2,000 images"; faces vs. speech separated in F13.11 | Panel top 4; pedagogy #16–17; editor decision 9 |
| L14 | How to take a frame from a video (13.7 step 2); what the artifact's "item of your own" is checked against (an item whose origin you can prove) | Panel top 5; editor decision 9 |
| L15 | Appendix E block now holds keys for every Check Yourself item and every faded example, plus the standard time-line sentence | Brief (self-checking keys rule) |

## Not changed (with reason)

| Item | Reason |
|---|---|
| C10 labeling (expert #1 option to follow the input-side rule) | The brief now states that Arup is labeled on the tree and chain because the deepfake is an AI output |
| Lovato et al. split percentages (expert #24) | The AIhub figures were not confirmed in the paper; the text reports the abstract's findings and hedges ("one survey is not every artist") |
| WEF wording for Arup's CIO | The page was never read (403); framing rests on CNN's reported statement |
| Dated box on image tokens | Kept with two providers (style sheet §3); refresh row |
| Fast route length (~24 min, above the v1 18 min) | The editor asked for a self-standing route; the added Warm-up, recap and glosses are required for that |

## Workload (W1)

Fast route ~3,550 words (~24 min); full route ~8,500 words (~57 min); with Ethics Lens, Career, From the Field and Summary ~66 min (150 wpm; longer if English is not your first language). End-of-chapter package ~2,200 words (~15 min to read). Labs 15–35 min each; artifact 80–100 min. Everything is optional: week 10's required time (Chapter 12) is unchanged.

## Waiting for the author

1. From the Field: confirm the 2015 entry (non-commercial); optional anonymized anecdote.
2. Final voice edit.
3. No live-syllabus change.

## Voice pass (Mode B, 2026-10-18)

Light pass per voice-profile §10: sections 13.1 and 13.2 now open with a concrete breadth sentence; "For example" added after the abstract rules in 13.2, 13.3, 13.4 and 13.7 (fields: engineering, history, accessibility, journalism, finance); "In other words" restatements after the dense paragraphs in 13.1 and 13.5; "Let's take …" walkthroughs in three worked examples. No humor, anecdotes or opinions were added.

## Render and figures

Figures re-rendered in color and gray (figures/scripts/ch13_figures.py, ch13_charts.py) and checked visually from previews (build/ch13/png). Quarto rendered the chapter to HTML (build/ch13/render/ch13.html): 20 images, no unresolved cross-references.

## Final review (applied, 2026-10-18)

All 6 must-fix, 14 should-fix and 4 nice-to-have items from build/ch13/reviews/final.md, with the editor's decisions (a)–(e):
- **M1** recap's deepfake definition now verbatim. **M2 / (a)** own figures use dashes only for inferred: F13.1 (Disclose second, gray box), F13.4, F13.6, F13.9, F13.10, F13.13 now use labeled gray fills; legends, alt text and long descriptions updated; guessing lines in F13.11 and F13.12 thin solid gray. Imported Ch. 3/8/9 legends left for the design pass. **M3** handoff D-13.9 times = 24 / 57 / 66 min. **M4** inclusive reading-time wording. **M5** brief and rubric 5 min (artifact parts add to 81–99, "80–100" holds). **M6** TrueMedia.org (2025) cited; autoregressive sentence cites Yu et al. (2022, Parti; author list checked on arXiv), hybrid claim dropped; commercial voice-cloning claim replaced by a pointer to Chapter 15 (decision d).
- **S1 / (e)** Deepfake-Eval-2024 named where the study is introduced. **S2–S4** plain-words box and recap use the glossary wording (independent check, content credentials, watermark (media)); data gate marked "adapted"; alt text glossed in the recap. **S5** From the Field wording ("the entry called sentimental, and its examples concern reputation"; "someone with bad intentions"). **S6** case file citations and "police believe". **S7 / (b)** one neutral band on every provided item ("COURSE SAMPLE — may be real or generated"), status only in the key. **S8** alternative packet = P1, P2 and one further case, none from Lab 13.2 (instructor package row added). **S9** A2 (d) reworded. **S10** "few tools support it" marked as the book's reading. **S11** dated box retitled "credentials in one maker's phones". **S12** F13.4 and F13.5 titles state the finding. **S13** guessing lines solid gray. **S14** blueprint times, C2PA year in the even key, handoff label and ordering fixed.
- **Nice to have:** "have applied since"; consent exception for Lab 13.4 clips; "language-model" in an alt text; "59.0%".
- To keep the full route at its cap, two sentences were cut (the Whisper training-hours sentence with its reference, and the Chapter 10 watermark recall) and the Opening's navigation sentence shortened. Counts: fast ~3,600 words (~24 min), full ~8,500 (~57 min), ~66 min with extras. Figures re-rendered in color and gray and checked; Quarto HTML render: 20 images, no unresolved cross-references.
