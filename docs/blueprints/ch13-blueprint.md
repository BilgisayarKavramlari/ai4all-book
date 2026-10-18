# Chapter 13 blueprint — Multimodal AI: Images, Audio and Video

Status: **v0.2 (2026-10-18), APPROVED under delegation (D19); draft v2 changes recorded at the end.** v0.2 applies the independent blueprint review (build/ch13/reviews/blueprint.md: 10 must-fix, 13 should-fix, 2 consider) and the editor's decisions 1–14 (see "Review changes" at the end). v0.1 is kept in build/ch13/ch13-blueprint-v0.1.md.
Part III — Deciding and Building with AI · Syllabus week 10 (read alongside Chapter 12; the syllabus lists "D: Ch. 13" for Tue Mar 30) · Path: **Deep** (optional; not examinable, D20) · Featured student: **Hana** (they/them; only), per docs/characters.md (arc: "studies image generation and deepfakes") · Work Loop highlight: **Verify**, with **Disclose** second.

**Source material.** No session or lab is assigned (week 10 belongs to Chapter 12). Opening case and main Case Study **C10** (editor-assigned): the Arup deepfake video-conference fraud in Hong Kong (2024). Primary record: Hong Kong SAR Government (2024, June 26), *LCQ9: Combating frauds involving deepfake*, text saved in build/ch13/src/lcq9.txt. Reported tier: CNN (Chen & Magramo, 2024, Feb 4; Magramo, 2024, May 16–17), texts in build/ch13/src/cnn_*.txt. From the Field: Şeker (2015), *YBS Ansiklopedi* 2(2), 12–16, read in full (build/ch13/ftf-dijital-varlik.md); not commercial.

**Chapter 6 pattern.** 13.1–13.7 Deep, 13.8 Studio; numbering without "Deep 13.A"; not examinable (D20), and the package says its questions are exam-format practice; fast and full routes timed in the Chapter Map; a "Plain words for this chapter" box re-glosses earlier terms; every Chapter 13 term is defined in this chapter's own text; Check Yourself answerable from each subsection; optional artifact with rubric and alternative; Compass appears as "In Compass (optional): …" notes.

**Boundaries.**

| Topic | Owner | Chapter 13 does |
|---|---|---|
| Multimodal models; generation in plain terms; uses (alt text, captions, transcription, design drafts); provenance and content credentials; watermark limits; why looking and detectors are weak; context before pixels; a verification protocol | **Ch. 13** | Owns |
| Token, context window, next-token prediction | Ch. 3 | One-paragraph recall; Signature 4 imported unchanged (`llm_anatomy(stage="tokens")`); new terms "image token" and "audio token" extend, never change, Ch. 3's text-only "token" |
| Failure types; tree; chain; documented/inferred | Ch. 4 | Fake media made to deceive = tree "other", leaf "misuse, such as fake media made to deceive"; transcript inventions = extrinsic hallucination; `failure_tree`, `failure_chain` imported (CHAIN stages are numbered 1–4 in the figure: 1 output wrong · 2 checked before use? · 3 someone relies · 4 loss; code indices 0–3) |
| Verification method, independent check, primary source, verdicts, stakes | Ch. 8 | Reused word for word; `verification_funnel` imported with media notes |
| Lateral reading, outside source, tracing, SIFT | Ch. 9 | Recalled in Ch. 9's wording; reverse image search taught here as its multimodal extension; tier line styles follow F9.2 (reported = solid + outlet tag; inferred = dashed) |
| AI-text detectors, false positives (Core 10.6), disclosure, process evidence | Ch. 10 | Recalled; "false positive (of a detector)", "disclosure (of AI use)", "process evidence" reused verbatim; media watermark sense-labeled |
| Automation bias; proxy | Ch. 11 | Spaced Review only |
| Data terms; the data gate | Ch. 12 | Used before any upload (Hana; labs) |
| Payment controls, voice-cloning scams, biometrics, family "safe words", nonconsensual imagery in depth | Ch. 15 | Pointers; C10 has one job here; money scenarios limited to Arup plus one faded example |
| Bias in generated images | Ch. 16 | One paragraph (Bianchi et al., 2023) |
| Copyright, likeness, deepfake laws, legal outcomes | Ch. 18 | Pointers; one dated clause each for the robocall outcome, EU AI Act Article 50 and the TAKE IT DOWN Act |

## 1. Outcome link and week 10

| Item | Value |
|---|---|
| Outcomes | **LO1** and **LO5** (book-map table); LO3 secondary in 13.6–13.8. The book map's coverage line lists Ch. 13 under LO6: inconsistency reported to the editor (handoff Decisions) |
| Artifact | **Verification protocol — optional, ungraded**; not one of the 13 graded artifacts; 10-point rubric for self-check; alternative assignment; suggested evidence for A12 (Ch. 15) and Ch. 21 |
| In-class time | None required |
| Examinable? | No (D20) |

### Workload (out of class; 150 wpm; longer if English is not your first language)

| Item | Words | Time |
|---|---|---|
| **Fast route** (Chapter Map with plain-words box, Warm-up, Opening Case, 13.7 with recap, 13.8, Summary) | ~3,550 (draft v2) | **~24 min**, optional |
| **Full route** (Chapter Map through the Case Study, labs excluded) | ~8,500 (draft v2; cap 8,500) | **~57 min**, optional; about 66 min with Ethics Lens, Career Connection, From the Field and Summary |
| Labs 13.1–13.4 | — | 15–30 min each, optional |
| Verification protocol, per requirement: brief and rubric ≈ 5; scope and triggers ≈ 10; channels and checks ≈ 10; three test items at ~12–18 each ≈ 36–54; disclosure rule ≈ 5; revision and re-check ≈ 8; declaration ≈ 7 | — | **80–100 min**, optional, weeks 10–12 |

Required week-10 time is unchanged (the chapter is optional).

**Word budget (full route ≤ 8,500):** Map + plain words 550 · Opening 450 · Objectives + Warm-up 300 · 13.1 750 · 13.2 1,050 · 13.3 900 · 13.4 700 · 13.5 550 · 13.6 850 · 13.7 950 · 13.8 750 · Case Study 700. Outside the full route: labs ~750, Ethics ~450, Career ~300, From the Field ~400, Summary ~400, End-of-Chapter Package ~2,300, Further Reading ~200 → total ≥ 12,500 words (≥ 10,000 rule met).

## 2. Objectives (one verb each)

| # | Objective | Bloom | LO | Tags |
|---|---|---|---|---|
| O1 | **Explain** how a multimodal model receives images and sound as tokens and how generators produce new media | Understand | LO1 | UNESCO:TECH-U · AI4K12:1 |
| O2 | **Distinguish** generated or altered media from a record of an event | Analyze | LO1 | 4D:DISC |
| O3 | **Evaluate** a multimodal use in your field by who relies on the output and which check it needs | Evaluate | LO5 | 4D:DIL · 4D:DISC |
| O4 | **Differentiate** what a provenance signal shows when present from what its absence shows | Analyze | LO5 | 4D:DISC · UNESCO:ETH-A |
| O5 | **Assess** whether media can be trusted, using source, channel and context checks before looks or scores | Evaluate | LO5, LO3 | 4D:DISC · 4D:DIL |
| O6 | **Create** a personal verification protocol for media and the requests it carries | Create | LO5 | 4D:DIL · UNESCO:ETH-A |

## 3. Prerequisites, promises, glossing

Recalled (re-glossed in the plain-words box): token, context window, generative model (Ch. 2–3); hallucination, extrinsic hallucination, the tree and chain (Ch. 4); independent check, primary source, verdicts (Ch. 8); lateral reading, outside source (Ch. 9); AI-text detector, false positive, disclosure, process evidence (Ch. 10); data gate (Ch. 12). Hana's 97% detector app is in Ch. 2 §2.5. **Promises kept:** Ch. 8 "Ch. 13 (deepfakes)"; Ch. 9 "verifying images and video → Ch. 13"; Ch. 12 §12.2 pointer. **Glossed at first use, not Key Terms:** patch, pixel, noise, denoising, latent, codec, frame, encoder/decoder, chance level, AUC, stripping, platform label, generation pipeline, hash, signature, phishing.

## 4. Misconceptions (six; refutation pattern)

| # | Misconception | Confronted |
|---|---|---|
| M1 | "A model that receives my photo or recording gets all of it, as I do, so its descriptions and transcripts are faithful." | 13.1 (resized patches; providers say file metadata is not processed); 13.3 (Koenecke et al., 2024). Check: not "useless": users report real benefits (Xie et al., 2025; Gonzalez et al., 2024) |
| M2 | "A realistic image, voice or video is evidence that what it shows happened." | 13.2; Opening; Short 1. Check: must not create M6 |
| M3 | "If I look and listen carefully, I will notice a fake." | 13.6 prediction (48.2%; 59.0%), Mai et al. (73%), Köbis et al. (overconfidence). Check: crowds matched a model (Groh et al., 2022); context checks still work |
| M4 | "A detector tool, or a chatbot, can settle whether media is fake." | 13.6 (Chandra et al., 2025 Table 3: AUC 0.43–0.63 on 2024 media vs. 0.87–1.00 on original tests; NIST, 2024 false positives; a provider's own documentation). Check: a score is a lead |
| M5 | "No label, watermark or credential means it is real; a credential means it is true." | 13.4–13.5 (C2PA explainer; NIST). Check: a valid credential is strong evidence of origin |
| M6 | "Anything could be fake, so checking is pointless." | 13.7 (Dufour et al., 2024; context checks settle many cases), Ethics Lens (liar's dividend) |

## 5. Concept sequence

**Session question:** *If seeing and hearing are no longer proof, how do you decide what to believe, and what to act on?* Hedged answer in the Summary (media is a claim; check source, channel, earliest version and outside sources first; signals present = lead, absent = nothing; looks and scores last; confirm requests by a channel you trust; decide triggers in advance).

**C10 tiers (state the tier for every fact not in the primary record; keep "police believe" with confirmed items).**

| Tier | Statement | Source |
|---|---|---|
| Confirmed (government record) | In end-January 2024 police received the case; the informant received a phishing email from a fraudster impersonating the CFO of the UK head office and was invited to a group video conference about confidential transactions; as instructed, authorized transfers to five local accounts; lost about HK$200 million; police **believe** the pre-recorded conference was generated from downloaded public video clips and voices of the impersonated officer, so there was no interaction; **after giving the instruction, the fraudster ended the meeting under some pretext and continued the payment instructions by instant messaging**; under investigation; three deepfake cases to May 31, 2024; police advice (head movements on camera, test identity through the conversation's content, verify money requests by phone, Scameter, helpline 18222) | LCQ9 (2024) |
| Reported (CNN, citing the police briefing) | The worker grew suspicious of a message purportedly from the UK-based CFO and first suspected phishing because it mentioned a secret transaction; set doubts aside after the call because the others looked and sounded like colleagues; HK$200 million ≈ US$25.6 million; "The scam involving the fake CFO was only discovered when the employee later checked with the corporation's head office" (CNN's narration); Senior Superintendent Baron Chan Shun-ching told RTHK that everyone the worker saw was fake (as reported by CNN); the briefing was on "Friday" (the date, February 2, 2024, is derived, not printed) | CNN (2024, Feb 4) |
| Reported (CNN, company statements) | Arup confirmed it was the company and notified police in January; "fake voices and images were used"; "Our financial stability and business operations were not affected and none of our internal systems were compromised"; 15 transactions (RTHK, citing police); Rob Greig, global CIO: attacks including invoice fraud, phishing scams, WhatsApp voice spoofing and deepfakes rising "sharply" | CNN (2024, May 16–17) |
| Not used | WEF interview wording (page not read: 403); FT naming (not read) | — |
| Inferred (the book's reading, marked) | That a call to a known number before the first transfer would likely have exposed the fraud | "This book reads…" |

The two accounts (first reports of a multi-person video conference; the government's "pre-recorded … no interaction") are taught as a tiers lesson. Status of arrests or recovery: none found in reliable sources as of October 2026 (refresh list).

**Opening Case (≤ 450 words):** facts and puzzle (why did a video call overcome a doubt an email had raised, and what check would have worked when looking did not?).

**One job per appearance of C10:** Opening = facts, puzzle · 13.2 = public clips were the raw material (one sentence) · 13.7 = the instructions came only through channels the fraudsters controlled · 13.8 = the protocol's out-of-band rule draws on the police advice · Case Study = labels, the two accounts, what the record shows and does not · Ch. 15 = controls, training, voice-cloning scams, biometric ID spoofing (handoff note).

**Prediction (13.6):** "People judged 128 faces, half real photos and half made by a 2020 generator. What share did they get right? After training?" → 48.2% (315 participants); 59.0% (219) (Nightingale & Farid, 2022).

| # | Subsection (words) | Tag | One core idea | Examples | Figures |
|---|---|---|---|---|---|
| 13.1 | Many kinds of input, one kind of model (750) | Deep | **Multimodal model** and **modality** defined; images become **image tokens** (patches; Dosovitskiy et al., 2021), sound becomes **audio tokens** (Wang et al., 2023); all share the context window. Dated box (two providers, as of October 2026): one counts a token per 28 × 28-pixel patch (1,000 × 1,000 ≈ 1,296 tokens) and shrinks large images; another uses 32 × 32 patches on newer models; both say their models do not process file names or metadata (Anthropic, n.d.; OpenAI, n.d.). M1 | **Worked:** Hana checks the tool's data terms first (Ch. 12 data gate: whether uploads may be used for training; they use the university-provided tool and switch off training where offered), then asks for a description of a scan of their hand-drawn 1920s streetcar; what the model received and what the description got wrong (route number lost after resizing; constructed). **Faded (health):** a nursing student's photo of a public anatomy poster, first item filled. **Your Turn (≤ 40 words)** | F13.3a (Signature 4 reuse, tokens stage), F13.3b (`modality_tokens`, new) |
| 13.2 | How generators make images, sound and video (1,050) | Deep | **A generated image is built, not retrieved.** **Diffusion model** (plain: noise removed step by step, guided by the prompt; Ho et al., 2020; Rombach et al., 2022); voice from a three-second sample (Wang et al., 2023); video as consistent frames (one sentence). **Definitions (book-wide):** synthetic media, deepfake, voice cloning. Memorization rare but real (Carlini et al., 2023); stereotyped outputs (Bianchi et al., 2023; → Ch. 16). Camera vs. generator (M2). C10 in one sentence. Hana's reasons for testing once stated | **Worked:** Hana's one test on a non-client prompt (no artist's style named; none of their own work uploaded), to understand what clients and zine readers ask about. **Faded (business):** marketing mockup, first part marked. **Your Turn** | F13.4 (`generation_pipeline("image")`), F13.5 (`generation_pipeline("voice")`), F13.6 (camera vs. generator) |
| 13.3 | Uses that help, and who checks them (900) | Deep | **The person who relies on the output often cannot check it, so the author must.** Alt text (WCAG SC 1.1.1: text alternative "that serves the equivalent purpose", Level A; W3C, 2023); legal basis for public universities: the 2024 DOJ ADA Title II rule adopting WCAG 2.1 AA, compliance extended in April 2026 to April 2027 for large entities (dated; reported via law-firm summaries; Federal Register citation in references); benefits and users' views (Gonzalez et al., 2024: 16 blind and low-vision participants, uses including avoiding dangerous objects, satisfaction 2.76/5, trust 2.43/4; Xie et al., 2025: users of one app reported discovering unnoticed details and more independence, and checked errors with their own knowledge or sighted helpers); harms (Koenecke et al., 2024: 187 of 13,140 segments reliably produced invented text; 1.4% of transcriptions; 38% of 312 hallucinated transcriptions harmful; more often for people with aphasia; 12 of 187 still in Dec 2023; much of the true transcription highly accurate). Person-first language | **Worked:** Hana's alt text (purpose first, draft, claim check). **Faded (education):** TA's lecture captions, check 1 done. **Your Turn** | F13.7 (who relies / who checks), F13.8 (data: Koenecke harm categories) |
| 13.4 | Provenance: where a file came from (700) | Deep | **Provenance**, **metadata**, **content credentials** (C2PA, founded 2021; signed statements bound by a hash; records history, not truth: C2PA explainer). Stripping on sharing (NIST, 2024); screenshots. Dated box: one phone maker's camera app attaches credentials to every photo (Google, 2025). M5 (first half). From the Field link | **Worked:** Hana credentials a scan; the screenshot a classmate shares has none. **Faded (journalism):** three photos, first verdict filled. **Your Turn** | F13.9 (credential anatomy) |
| 13.5 | Watermarks and labels (550) | Deep | **Watermark (media)** defined (sense-labeled; Ch. 10's text watermark recalled); exists only where a maker added it; can be weakened by edits; open-weight models need not add one (NIST, 2024); one provider's detector portal (Google, 2025). Platform labels depend on signals or the uploader. Two-sided rule (M5). (Glaze/Hönig moved to the Ethics Lens) | **Worked:** the zine collective's rule: every applicant, Hana included, submits process evidence (sketch photos, scans of pages), because no signal can show hand-made origin. **Faded (engineering):** labeled renders, first question answered. **Your Turn** | F13.10 (present vs. absent) |
| 13.6 | Why looking and detector scores are weak (850) | Deep | **Looks and scores are leads, not verdicts.** Human studies (Nightingale & Farid; Mai et al.; Köbis et al.; Groh et al.); **deepfake detector** defined; Chandra et al. (2025, v5) Table 3 absolute AUC (0.5 = guessing): 0.43–0.63 on Deepfake-Eval-2024 vs. 0.87–1.00 on original test data; best commercial AUC 0.79 video, 0.93 audio, 0.90 image (Table 5), none at 90% accuracy; false positives (NIST, 2024; Ch. 10 §10.6); a provider's documentation says its model cannot determine whether an image is AI-generated (Anthropic, n.d.). Hana's 97% app (Ch. 2 §2.5) recalled. M3, M4 | **Worked:** prediction box and Hana's re-reading of the 97% app claim. **Faded (social science):** a survey researcher reads a detector vendor's accuracy claim; first question filled. **Your Turn** | F13.11 (data: human detection), F13.12 (data: detector AUC, absolute) |
| 13.7 | Context before pixels (950) | Deep | **Check the source, the channel and the context before the pixels.** **Out-of-band check**, **reverse image search**, outside sources, earliest version; definitions (book-wide): **social engineering**, **cheap fake** (Paris & Donovan, 2019); Dufour et al. (2024): context manipulations a majority of fact-checked media misinformation through November 2023, generated images rising from spring 2023. Check list (book-map figure). C10's channel paragraph. Funnel recalled with media notes. M6 | **Worked:** Hana's "1890s photograph": earliest copy is a 2025 post whose poster labeled it as made with an image generator (positive evidence) → contradicted as an 1890s photograph. **Faded (accounting; the one money item):** an accounts-payable clerk's voice message, step 1 filled. **Your Turn** | F13.13 (`media_checklist`), F13.14 (Signature 8 reuse) |
| 13.8 | Your verification protocol (750) | **Studio** | Recap box (~150 words; fast route). **Verification protocol** defined: triggers, pause, out-of-band channels by role, checks by stakes, record, disclosure; built on the police advice and the chapter's evidence | **Worked (media evidence):** a classmate's video "proving" the city painted over a downtown mural last week; Hana's protocol: source, earliest version (a 2019 upload of a different wall), outside sources (city notice, local news) → a real clip, miscaptioned: a cheap fake; verdict contradicted for the claim. **Faded:** a club social-media manager's protocol, triggers filled. **Your Turn** = the optional artifact | F13.15 (protocol card) |

Other parts: **Case Study** (700): C10 revisited (labels; two accounts; what the record shows and does not; CNN's "none of our internal systems were compromised"; the book's reading marked). Tree: other (misuse), documented. Chain: stage 2 "Checked before use?" failed: note "no check with head office before the transfers (reported)", drawn dashed per the F9.2 convention only where inferred — here solid with an outlet tag "(reported: CNN)"; stage 4 loss confirmed. **Short 1** Pentagon image (2023; NPR): context settled it; tree other (misuse), inferred. **Short 2** NH robocall (2024): how the audio was traced (Industry Traceback Group and two robocall-blocking firms helped investigators trace the calls to a Texas company; researchers attributed the voice to one AI tool, which the state could not confirm; Johnson, 2024) and the FCC's ruling that AI voices are "artificial" (FCC, 2024); legal outcome for the consultant in one dated clause, pointer to Ch. 18. **Ethics Lens:** content note; people depicted (TAKE IT DOWN Act, one dated sentence); artists (Lovato et al., 2024: 459 artists, majority favor disclosure of training works and reject model makers' ownership of outputs, views on usefulness mixed; Glaze user study; protections later shown to be defeated by simple edits, method not named; what artists can still do: contracts, disclosure, credentials, collective rules); liar's dividend (Chesney & Citron, 2019); EU AI Act Article 50 (dated). **Career:** fact-checker, accessibility specialist or captioner, illustrator or designer, paralegal (media evidence), archivist, medical scribe. **From the Field:** as v0.1 (facts limited to the 2015 entry; connections marked). **Summary + Key Terms** (22): modality · multimodal model · image token · audio token · diffusion model · synthetic media · deepfake · voice cloning · alt text · closed captions · transcription (speech recognition) · provenance · metadata · content credentials · watermark (media) · deepfake detector · reverse image search · out-of-band check · social engineering · cheap fake · liar's dividend · verification protocol.

## 6. Example plan

Every skill has worked → faded (first step filled) → Your Turn (≤ 40 words) as in §5. Fields: arts and history (Hana), health, business, education, journalism, engineering, social science, accounting (one money item), student organizations. No identifiable real person in any example or lab item; outputs labeled constructed.

**New character details (handoff):** Hana's zine has a web page with alt text; history issue with a hand-drawn 1920s Dallas streetcar; checks a tool's data terms and training option before uploading their drawings; tested a text-to-image tool once on a non-client prompt and still does not use generation in their own illustrations; credentials scans of their drawings; received an AI-generated "1890s photograph" from a reader; belongs to a small zine collective whose rule asks every applicant, Hana included, for process evidence; keeps a written verification protocol; checked a mural clip before citing it.

## 7. Retrieval and spacing

Warm-up (3; the third with confidence): what a model receives from a photo; a video clip offered as proof of an event: one check not about how real it looks; no label = more likely real? **Spaced Review** (Ch. 11 ×2: automation bias with a detector score; a realistic look as a proxy for "real" — checked against the Ch. 11 blueprint; Ch. 10 ×2 from Core: false positives for second-language writers, §10.6; Hana's disclosure to a client, §10.7) + 1 interleaving item (Ch. 12 data gate). **Spaced forward:** Ch. 15 (controls, voice cloning, safe words, biometrics), 16, 18, 19, 21, 22, 23.

## 8. Alignment and package

| Obj. | Taught | Practiced | Figures | Assessed |
|---|---|---|---|---|
| O1 | 13.1–13.2 | sequences | F13.3a–F13.5 | A; B1 |
| O2 | 13.2, Opening, Short 1 | sequence | F13.6 | A; C1 |
| O3 | 13.3 | sequence; Lab 13.1 | F13.7, F13.8 | A; B2 |
| O4 | 13.4–13.5 | sequences; Lab 13.3 | F13.9, F13.10 | A; B3 |
| O5 | 13.6–13.7, Case | sequences; Labs 13.2, 13.4 | F13.11–F13.14, F13.16–F13.18 | A; B4; C2; CSQ |
| O6 | 13.8 | artifact | F13.15 | optional artifact |

Review A 12 (keys rotated; correct option longest in ≤ 2 items) · B 4 (B4 = a media-evidence case: a video offered as proof in a community dispute) · C 2 · Spaced 4 + 1 · Discussion 5 · CSQ 5 (all answerable from the chapter; robocall CSQ asks how the calls were traced) · optional Mini-Project. Odd answers → handoff Appendix E; even → private/ch13-answers-even.md. **Artifact test-item keys** (two provided items, not used in Lab 13.2) → Appendix E block ("read after writing your record") and the instructor package.

## 9. Optional artifact — Verification Protocol

As v0.1 §9 with these changes: 65–90 min; scope situations must include at least one media-evidence situation (a recording or image offered as proof, an image to cite, a files request); test items contain no identifiable people; the student's own item contains no person's face or voice; channels by role; rubric unchanged (3 / 1.5 + 1.5 / 2 / 2), parallel levels; alternative = the provided no-tool case packet (reusing the Lab 13.2 packet format).

## 10. Figures (19 entries, 20 files; no generative imagery)

New reusable functions in figures/scripts/ch13_figures.py: `modality_tokens(highlight=None, note=None)`, `generation_pipeline(mode="image"|"voice", highlight=None, note=None)`, `media_checklist(highlight=None, note=None, verdict=None)`. Imports unchanged: `work_loop` (ch01), `llm_anatomy` (ch03), `failure_tree`, `failure_chain`, `tree_height` (ch04), `verification_funnel`, `funnel_height` (ch08), `hop_chain` (ch09). Charts in ch13_charts.py from data/ch13_*.csv.

| ID | File | Title (states the finding) | Section |
|---|---|---|---|
| F13.1 | f13-01-chapter-map | Chapter 13 at a glance | Opening |
| F13.2 | f13-02-storyboard | Every instruction came through a channel the fraudsters controlled | Opening |
| F13.3a | f13-03a-anatomy-tokens | Recall from Chapter 3: text arrives as tokens | 13.1 |
| F13.3b | f13-03b-modality-tokens | Images and sound arrive as tokens too, beside your words | 13.1 |
| F13.4 | f13-04-pipeline-image | A generated image is built from noise toward the prompt, not looked up in a record | 13.2 |
| F13.5 | f13-05-pipeline-voice | In 2023 a research system imitated a voice from a three-second sample | 13.2 |
| F13.6 | f13-06-camera-vs-generator | A camera records an event; a generator produces a plausible picture of none | 13.2 |
| F13.7 | f13-07-who-checks | The person who relies on the output often cannot check it, so the author must | 13.3 |
| F13.8 | f13-08-whisper-harms | In a 2023 test, 38% of transcripts with invented text contained harmful inventions | 13.3 |
| F13.9 | f13-09-credential | A content credential records a file's history, and a screenshot leaves it behind | 13.4 |
| F13.10 | f13-10-present-absent | A signal that is present is a lead about origin; an absent signal shows nothing | 13.5 |
| F13.11 | f13-11-human-detection | People judging faces did about as well as guessing; training helped a little | 13.6 |
| F13.12 | f13-12-detector-auc | Detectors that scored 0.87–1.00 on their own test data scored 0.43–0.63 on 2024 deepfakes | 13.6 |
| F13.13 | f13-13-checklist | Check the source and the channel first; inspect the pixels last | 13.7 |
| F13.14 | f13-14-funnel-media | For media, the primary source is the original file, or the person through a channel you trust | 13.7 |
| F13.15 | f13-15-protocol-card | Your protocol decides in advance what you will check before you act | 13.8 |
| F13.16 | f13-16-tree-arup | Arup on the tree: misuse of fake media to deceive, documented | Case |
| F13.17 | f13-17-chain-arup | The loss followed because no check with head office came before the transfers | Case |
| F13.18 | f13-18-pentagon | Context, not pixels, settled the Pentagon image | Case |
| F13.19 | f13-19-summary-card | Chapter 13 summary card | Summary |

## 11. Labs (optional, home; In Compass (optional): steps)

Rules for all labs: no identifiable people in any item, including your own; run the data gate (Ch. 12) before any upload; provided materials made for the course.
- **Lab 13.1 Describe It, Then Check** (25 min): your own drawing, chart or object photo (no people) or a provided image; data gate; your alt text first; tool's draft; claim check. Audio extension uses a provided clip recorded for the course by a consenting speaker.
- **Lab 13.2 Trace an Image** (30 min): four provided dated items without people (buildings, landscapes, objects): authentic, miscaptioned, generated, edited; check list; answer key after.
- **Lab 13.3 Read the Credentials** (20 min): provided credentialed file; inspect; screenshot; inspect again; one image of your own (no people).
- **Lab 13.4 The Ear Test** (15 min): ten provided clips recorded for the course by consenting speakers, with synthetic versions made with their written consent (instructor package; replaces the v0.1 research-dataset plan); confidence first, then score; non-audio route (transcript and spectrogram pairs) or skip.

## 12. Risks and checks

1. Tiers exactly as §5; no WEF or FT wording; "police believe" kept; derived date marked.
2. Numbers exactly as published (Koenecke denominators; Chandra absolute AUC with version v5; Nightingale & Farid; Mai; Gonzalez; Xie).
3. Harm avoidance: no bypass or removal method named; no generated likeness of real people; nonconsensual imagery as a category with a content note.
4. Artists: range of positions, hedged prevalence (Lovato et al. is one survey of 459 artists), what artists can still do; Hana's reasons stated; they/them.
5. Dated content in boxes naming two or more providers; unverified items dropped (platform test, OpenAI watermark adoption, video tools box).
6. Ch. 15 / Ch. 18 boundaries as in the table.
7. No visible [VERIFY] in student text unless unresolved; status in the handoff and the fact-check log.
8. Stray environment dump: build/ch13 contains none; the editor should delete appmap.log and docs/appmap.log (security note, review item 10).

## Decisions taken under delegation (D19)

T1–T17 from v0.1 stand, amended: **T1** 8 subsections (13.1–13.7 Deep, 13.8 Studio); fast route = Map, Opening, 13.7, 13.8 + recap, Summary. **T4** chain stage numbers follow the figure (stage 2 failed, stage 4 loss); stage 2's "no check with head office before the transfers" is reported (CNN), drawn solid with an outlet tag (F9.2 convention). **T5** LCQ9 text saved; the meeting's ending "under some pretext" is now confirmed (record) and used as such. **T11** unchanged. **T12** artifact 65–90 min; keys in Appendix E. **T13** Hana runs the data gate before uploads; the collective's process-evidence rule applies to every applicant. **T14** robocall case recast around tracing. New: **T18** definitions of deepfake, synthetic media, voice cloning (13.2), social engineering and cheap fake (13.7) are book-wide; Ch. 15/16/18/19 copy them verbatim. **T19** detector chart uses absolute AUC from Table 3 (v5). **T20** Lab 13.4 uses clips made for the course with consent. **T21** "safe word" advice moved to the Ch. 15 handoff note.

## Author-only items

1. From the Field: confirm the 2015 entry (non-commercial). Optional anonymized anecdote; never written for you.
2. No live-syllabus change.
3. Final voice edit.

## Review changes (v0.1 → v0.2)

Must-fix: (1) workload recounted and cut (full route ≤ 8,500 words; drafted ~7,350 words, ~50 min; fast ~18 min); (2) 13.6 split into 13.6 / 13.7 / 13.8; (3) deepfake, synthetic media, voice cloning defined in 13.2, social engineering and cheap fake in 13.7; (4) "had to end quickly" deleted; the record's own "ended the meeting under some pretext" used instead (confirmed); (5) Chan → RTHK as reported by CNN; derived date marked; CNN's discovery wording; Greig's "WhatsApp voice spoofing" read and used; (6) chain stage numbers fixed; F9.2 line convention; "police believe" kept; (7) WEF wording dropped; framing on CNN's "none of our internal systems were compromised"; (8) no bypass method; no identifiable people in any item; data gate before uploads; Lab 13.4 clips made for the course with consent; (9) F13.12 uses absolute AUC values (Table 3, v5); (10) LCQ9 text saved; appmap note to the editor.
Should-fix: (11) fast route rebuilt; (12) Shan/Hönig and Chesney & Citron once each, in the Ethics Lens; (13) money items cut to Arup + one faded example; Hana's protocol test is a media-evidence case; safe word → Ch. 15; (14) robocall recast around tracing; legal outcome one dated clause; (15) one verb per objective; O1 tags UNESCO:TECH-U · AI4K12:1; book-map LO note; (16) accessibility benefits and users' views added; WCAG wording and legal basis corrected; Koenecke denominators; person-first; (17) Hana's data gate; collective rule for all applicants; Hana's reasons; (18) artists' range of positions hedged with Lovato et al.; what artists can still do; (19) token chart cut, dated box kept; chatbot-as-detector claim generalized with one cited example; (20) 13.7 verdict rests on positive evidence; (21) faded examples with first steps; Your Turns ≤ 40 words; (22) `llm_anatomy` imported unchanged; new `modality_tokens()`; (23) Spaced Review from Core 10.6; keys location; 65–90 min.
Consider: (24) seven terms moved to glosses; (25) unverified dated items dropped; content note added.

## Post-draft changes (draft v2, 2026-10-18)

Applied after the four chapter reviews and the editor's decisions 1–9 (full list: docs/editorial/ch13-dev-memo.md). Changes that override this blueprint: **fast route** = Map with plain-words box, Warm-up, Opening, 13.7 (now opening with the recap of 13.2–13.6), 13.8, Summary (~3,550 words, ~24 min); **full route** ~8,500 words (~57 min; ~66 with Ethics Lens, Career, From the Field, Summary); **artifact** 80–100 min; week-10 advice "this week if you have time, otherwise week 11". **Definitions:** deepfake = synthetic media that realistically shows a real person, or a real event, saying, doing or happening in a way that did not happen; cheap fake = media manipulated without generative AI; one rule wording everywhere: "a missing signal proves nothing". **Examples:** a second worked example in 13.7 ends *supported* (archive photo); faded examples and B4 supply every fact; the 13.7 faded prompt no longer depends on Ch. 15. **C10:** the two accounts are compatible; "pre-recorded" is stated by the record, "police believe" attaches to how it was generated; the police officer is not named in running text (D-10.8); the later check with head office as "a channel the fraudsters did not control" is the book's reading. **Evidence updates:** TrueMedia.org (closed to the public January 2025); Chandra benchmark description (user-flagged real and fake media; 22 anonymized commercial tools; audio-labeling caveat); Gemini SynthID check (Nov 2025); C2PA 2.3 and soft bindings; DOJ 91 FR 20902; EU AI Act Article 50 with the Dec 2, 2026 transition (Regulation (EU) 2026/1744); FCC 24-104 for the robocall label; Koenecke denominators; Mai et al. 73% = deepfakes identified (F13.11 split into faces and voices panels). **Labs:** Lab 13.2 uses public-domain originals and dated search-result sheets; generated items are fictional, non-local, eLearning-only and banded; Lab 13.4 has a five-clip 10-minute version.
