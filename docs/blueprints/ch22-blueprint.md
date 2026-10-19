# Chapter 22 blueprint — The State of the Art: Current Developments

Status: **v0.2 (2026-10-18), APPROVED under delegation (D19).** v0.2 applies the independent blueprint review (build/ch22/reviews/blueprint.md: 6 High, 11 Medium, 2 Low) and the editor's decisions 1–8 (see "Review changes" at the end). v0.1 is kept in build/ch22/ch22-blueprint-v0.1.md.
Part VI — Frontiers and Big Questions · No syllabus week · Path: **Deep** (optional; **not examinable**, D20) · Featured student: **Hana** only (they/them) · Work Loop highlight: **Verify**, with **Decide** second.

**Sources.** build/ch22/research-v0.1.md (R1–R27) plus the v0.2 checks below; raw data saved in build/ch22/src/ (METR benchmark_results_1_1.yaml; Epoch notable and frontier model CSVs, CC BY 4.0, downloaded 2026-10-18 with SHA-256 in data/ch22_meta.txt; OpenAI o3/o4-mini system card PDF). **Case C31** (editor-assigned): the 2025 and 2026 International Mathematical Olympiad (IMO) results claimed for AI systems. From the Field: Şeker (2014), *YBS Ansiklopedi* 1(1) (notes build/ch22/ftf-ag-etkisi-moore.md), drawing on Fichman, Dos Santos & Zheng (2014), *MIS Quarterly* 38(2), 329–354; not commercial; registered.

**The chapter's own rule** (book map): every claim dated (as of October 2026), the chapter rewritten each edition, students asked what has aged. Design: (1) the lasting content is a **method** for reading current developments (22.1), applied in every section; (2) each section 22.2–22.7 has a stable method text plus **one "As of October 2026" box** that holds all of that section's dated numbers, drawn from data/ch22_*.csv (each row has an `as_of` column); figures use the same CSVs; (3) 22.8 and the essay audit the chapter itself. Review keys test the method or values printed in a box, never prose numbers (X9).

**Deep-chapter pattern (Ch. 6, 13, 17):** 22.1–22.7 Deep, 22.8 Studio; not examinable; questions labeled exam-format practice; fast and full routes in the Chapter Map with the "Extra, all optional" line; plain-words box (≤ 12); every Chapter 22 term defined here; two Check Yourself items per section, answerable from it; optional artifact with rubric and alternative; every example printed.

**Boundaries.**

| Owner | Topic | Chapter 22 does |
|---|---|---|
| Ch. 3 (3.2, Deep 3.B) | Tokens, reasoning tokens, settings (parameters), pretraining, scaling laws | Recall in glossary wording; 22.2 and 22.6 start where Deep 3.B stops |
| Ch. 5 · Ch. 6 | Chain-of-thought prompting · workflow vs. agent | Pointers; glossary wording |
| Ch. 8 · Ch. 9 | Independent check, primary source, verdicts · outside source | Reused verbatim; "measured" is defined through Ch. 9's outside source |
| Ch. 12 (12.2, Deep 12.A–B) | Closed, open-weight, local; leaderboards; lock-in | 22.5 adds the measured gap; definitions verbatim |
| Ch. 13 | Multimodal models, generation, provenance, detectors | 22.4 adds dated capability changes |
| Ch. 14 (14.2–14.3) | Agent loop, gates, error compounding, METR 2025 | 22.3 updates the dated evidence; `agent_loop` imported |
| Ch. 17 (17.6) | Reasoning text as a claim; monitoring | 22.2 box keeps Ch. 17's promise |
| Ch. 18 · Ch. 19 (C26) · Ch. 21 | Law · A-Lab correction · "what has aged" | One pointer · one sentence · 22.8 |
| **Ch. 23** | AGI, existential risk, the International AI Safety Report | **One sentence in 22.6:** debates about general AI, long-term risk and the International AI Safety Report are treated in Chapter 23; no summary here |

## 1. Outcome, timing, workload

LO1 (LO3 secondary on O1 and O5). Optional artifact: **short discussion essay, "What has already aged?"** (ungraded; 10-point self-check rubric; alternative). In-class time 0. Examinable: no. **When to read: after Chapter 21** (weeks 15 or later; any time after Chapter 14 also works, and the Spaced Review marks Chapter 19–21 items "if you have read it"). Required time added to any week: **0**.

| Item | Words or count | Time (150 wpm; "allow more if you read more slowly or are reading in a second language") |
|---|---|---|
| Fast route: Map + plain words, Opening, Warm-up, 22.1, 22.8 with recap, Summary | ~3,000 | **~20 min** |
| Full route: Map through Case Study, labs excluded | ~7,900 (cap 8,000) | **~53 min**; ~63 min with Ethics, Career, From the Field, Summary |
| Extra, all optional: Warm-up and 16 Check Yourself (19 × 0.5 ≈ 10 min); 8 faded examples (16 min); Your Turns; labs 20–30 min each; end-of-chapter questions (~15 min to read; A 6 + B 8 + C 4 + Spaced 5 × 2 = 10 + CSQ 10 ≈ 38 min to answer) | — | as listed |
| Essay, per requirement: brief and rubric 4; three dated claims 6; three current-status checks 24; status table 6; essay 30; revision 6; declaration 4 | — | **about 80 min (65–95)** |

**Word budget:** Map + box 550 · Opening 500 · Objectives + Warm-up 300 · 22.1 900 · 22.2 750 · 22.3 750 · 22.4 550 · 22.5 600 · 22.6 950 · 22.7 650 · 22.8 700 · Case Study 700 = 7,900. Outside: labs ~700, Ethics ~400, Career ~300, From the Field ~400, Summary ~400, package ~2,400, Further Reading ~200, references ~1,400 → ≈ 14,100. Worked ≤ 120 words; faded ≤ 70 (first step filled, every fact supplied); Your Turn ≤ 40; each box ≤ 120 words.

## 2. Objectives

| # | Objective | Bloom | LO | Tags |
|---|---|---|---|---|
| O1 | **Distinguish** measured, reported and forecast claims about an AI development, each with its as-of date | Analyze | LO1 (LO3) | 4D:DISC · UNESCO:TECH-U |
| O2 | **Explain** what a reasoning model does differently from an earlier chat model and what outside evidence shows about its gains and limits | Understand | LO1 | UNESCO:TECH-U · AI4K12:3 |
| O3 | **Interpret** a dated trend chart (logarithmic axis; data points vs. a fitted trend) | Understand | LO1 | 4D:DISC · UNESCO:TECH-U |
| O4 | **Compare** open-weight and closed models on the measured capability gap and on what each lets users inspect and control | Analyze | LO1 | 4D:DEL · UNESCO:TECH-U |
| O5 | **Evaluate** a claim about AI's energy use or a scientific discovery by what it counts and who checked it | Evaluate | LO1 (LO3) | 4D:DISC · 4D:DIL · UNESCO:ETH-U |
| O6 | **Judge** which claims in a dated account have aged and what that means for work in your field | Evaluate | LO1 | 4D:DIL · UNESCO:HCM-A |

## 3. Promises, plain words, glossing

**Promises kept (only those that exist):** Ch. 17 §17.6 ("Methods and results change quickly; Chapter 22 follows them") → 22.2 box; Ch. 21 Last Words ("Chapter 22 asks you to notice what has already aged") → 22.8 and the essay. The Ch. 14, 16, 19 and 20 blueprints planned pointers that their chapters do not contain → editor item E5 (add in assembly or leave).

**Plain-words box (12, glossary wording):** token; reasoning tokens; settings (parameters) and pretraining; benchmark; agent vs. workflow; tool use; agent loop and observation; open-weight model; multimodal model; independent check, primary source and outside source; verdict; jagged technological frontier.

**Glossed, not Key Terms:** logarithmic axis, doubling time, extrapolation, terawatt-hour, inference cost, leaderboard, peer review, preprint, data center, proof assistant (Lean).

## 4. Misconceptions

| # | Misconception | Confronted | Refutation check |
|---|---|---|---|
| M1 | "A developer's announcement tells you what AI can now do." | Opening; 22.1; Short 1 | A reported claim can be true; it is unchecked until an outside source checks it |
| M2 | "Newer reasoning models make fewer factual errors." | 22.2: in its developer's 2025 test, a newer reasoning model (o3) invented facts about people more often than an older one (o1): 0.33 vs. 0.16 (OpenAI, 2025, Table 4; the developer says more research is needed) | Not "reasoning models are worse": outside benchmarks show large gains on math and code; errors depend on the task |
| M3 | "A high benchmark score means the system will do my task reliably." | 22.3 (50% vs. 80% horizons; METR's own caveats); AI Index 2026 jagged example | Benchmarks are dated evidence; your own test settles fit (Ch. 12, 14) |
| M4 | "Progress will keep accelerating" / "AI has hit a wall" as certainties | 22.6 (measured trends vs. forecasts; 2024 plateau reports; test-time compute) | Both are forecasts; the text names what would move each |
| M5 | "One chat question uses a huge amount of energy" / "AI's energy use is negligible" | 22.6 box (per-prompt figures by boundary; grid totals) | Small per prompt and large in total can both be true |
| M6 | "If an AI system made a discovery, the science is settled." | 22.7 (AlphaFold's community testing; GNoME critique; C26 recalled) | Not "AI cannot contribute"; the field's checks settle it |

## 5. Concept sequence

**Session question:** *When you read that AI "can now" do something, how do you tell what was measured, what was only claimed and what is a guess about the future, and how long will the answer stay true?*

**The method (22.1).** Three tags per claim: (1) **as-of date** — when it was made or measured; (2) **evidence status** — **measured** (measured or checked by an outside source, Chapter 9's term, with a method you can read: a competition's own graders, an evaluation group such as METR or Epoch AI, the AI Index, the IEA, peer reviewers, a proof checker); **reported** (stated by the developer, or by an outlet citing the developer: launch posts, system cards, benchmark tables in announcements; the developer's page is the primary source for what the developer claims, and it passes Chapter 8's independent check, but it is not an outside source); **forecast** (about the future, by anyone, including outside bodies); and **the book's inference**, marked as always; (3) **who could check it.**

**Crosswalk printed in 22.1 (two lines):** the case tiers (confirmed / reported / inferred) ask *is this fact in the primary record?*; the evidence status asks *who checked the capability?* DeepMind's blog post is the primary record of what DeepMind says (confirmed as its statement), and the capability it describes was checked by the IMO's coordinators (measured), with limits the post itself states.

**C31 facts and tiers (verified 2026-10-18; build/ch22/c31-sources.md).**
- *2025, confirmed (developer's page):* an advanced Gemini Deep Think scored 35/42, five of six problems, within the 4.5-hour limit, in natural language; IMO coordinators graded and certified it by the criteria used for students; **DeepMind's own post** adds that the IMO's review "does not extend to validating our system, processes, or underlying model" (one quotation).
- *2025, reported (AFP):* the IMO president cautioned that organisers could not verify how much computing power was used or whether people were involved; companies had privately tested models on the problems faced by 641 students; about 10% of students won gold and five scored a perfect 42.
- *2025, reported (Reuters):* OpenAI announced on Saturday (July 19, derived) that an experimental model reached 35/42; three former medalists graded each proof; it did not have its results certified by the IMO; IMO judges had asked labs to wait until July 28, and later let cooperating companies publish on Monday (July 21); OpenAI said a board member allowed publication after the closing ceremony. Reuters' student counts (630; 67 gold) differ from AFP's; the text uses AFP's, the case file records both.
- *2025, reported (developers):* ByteDance's Seed Prover: an IMO-certified 30/42 (silver-level), proofs written for a proof assistant (Lean) after problems were formalized by hand (ByteDance Seed, 2025); Harmonic's Aristotle: gold-medal-equivalent performance with formally verified proofs (Achim et al., 2025, arXiv). A machine-checked proof is a third kind of check: a program confirms each step of the formal proof (not whether the formal statement matches the problem).
- *2026, reported (AFP, July 23, 2026):* Huawei and Xiaohongshu said their systems scored 100%; Xiaohongshu said its answers were submitted to the IMO's organisers for grading and human intervention was prohibited; firms got the problems after the contestants; seven of 666 contestants had full marks (official scoreboard); a venture investor said four models he tested scored 42/42 (his own test, not official). No IMO statement in the report.
- *Inferred:* the book's reading that by 2026 the IMO no longer separates the strongest systems; marked.

**One job per appearance:** Opening = 2025 facts and the puzzle · 22.1 = worked tagging and crosswalk · 22.2 = one sentence (both 2025 gold results came from reasoning models given extra computation at answer time, as their makers describe) · Case Study = labels, the third kind of check, the 2026 update.

| # | Section (words) | Tag | One core idea | Worked → Faded → Your Turn | "As of October 2026" box (CSV) | Figures |
|---|---|---|---|---|---|---|
| 22.1 | Reading a dated claim (900) | Deep | A claim about the state of the art is incomplete without its date, its evidence status and who could check it. Defines as-of date, evidence status, measured/reported/forecast, capability claim, outside evaluation. **Signature introduced.** Edition note: written October 2026 for edition 2027.1. Crosswalk | IMO 2025 statements tagged → vendor's "resolves 80% of tickets" (constructed; tag 1 filled) → tag one claim you saw this week | — | F22.3, F22.4 |
| 22.2 | Reasoning models (750) | Deep | A reasoning model spends extra computation at answer time; outside tests show large gains on math and code, and errors remain. Defines reasoning model (a provider term), test-time compute. Shojaee et al. (NeurIPS 2025) and an informal reply comment (labeled as such) as a live dispute | Hana's archive-date question (constructed outputs) → nursing tutor's "doesn't hallucinate doses" (status filled) → Your Turn | ch22_benchmarks.csv, ch22_personqa.csv: AI Index 2025 jumps; AI Index 2026 SWE-bench; PersonQA; DeepSeek-R1 in *Nature*; reasoning-text monitoring (Ch. 17 promise) | F22.5, F22.6, F22.7 |
| 22.3 | Agents and tool use (750) | Deep | Agents complete longer tasks than in 2025, but "half the time" and "reliably" are still far apart. Defines time horizon, computer-use agent, tool protocol. Benchmark saturation glossed | Hana reads METR's chart for the zine column → facilities team's "agent can run maintenance scheduling" (Q1 filled) → Your Turn | ch22_metr.csv (TH 1.1 yaml): 50%/80% for three providers; doubling ~129 days since 2023 (METR's fit); caveats (page no longer actively updated, last update Sept 8, 2026; above 16 h unreliable); OSWorld 12% → ~66% (AI Index 2026) vs. 72.36% human baseline (Xie et al., 2024); Agentic AI Foundation (Dec 2025; adoption counts are company claims) | F22.8, F22.9 |
| 22.4 | Many modalities (550) | Deep | Generation now spans sound with video and real-time voice; Chapter 13's checks matter more. Realism is reported quality, not accuracy | Hana tags a constructed video-model launch post → instructional designer's "indistinguishable voices" (tag 1 filled) → Your Turn | ch22_modalities.csv: two providers' video-with-sound releases (2025) [VERIFY V13]; AI Index 2026 multimodal reasoning | F22.10 |
| 22.5 | Open and closed models (600) | Deep | The measured gap between the best open-weight and best closed models is months, not years; access and inspection differ more than scores. Ch. 12 terms verbatim (lock-in: "the effort and cost that keep you on a tool after a better fit appears") | Zine collective's open-weight alt-text question → lab's "a year behind" (status filled) → Your Turn | ch22_open_closed.csv: AI Index 2025 (a crowd-vote leaderboard, Chatbot Arena: 8% → 1.7%; Ch. 12 Deep 12.B on leaderboards); Epoch Oct 30, 2025 (3.5 months, 90% CI 1.1–5.3); Epoch May 29, 2026 (~4 months since Jan 2026) | F22.11 |
| 22.6 | Scale and its costs (950) | Deep | The growth of compute and electricity is measured; whether more scale keeps paying off is a forecast. Defines training compute, FLOP, scaling, system boundary. Debate: 2024 reports of slower pretraining gains (reported), the turn to test-time compute; Epoch 2030 and data-stock forecasts. Ch. 23 sentence | This book's calculation (ch22_calc.py): 30 prompts a day at three boundaries → council claim "as much power as 100,000 homes" (IEA's figure for a typical AI-focused data center; boundary question filled) → Your Turn | ch22_compute.csv (Epoch; this book's fit ≈ 4.3×/yr; Epoch's 4–5×); ch22_energy.csv: IEA 2025 (415 TWh, ~1.5%, 2024; 945 TWh 2030 base case; "large uncertainties"), IEA Apr 16, 2026 (+17% in 2025; set to double by 2030; AI-focused to triple) in separate sentences; LBNL/DOE (176 TWh, 4.4%, 2023; 6.7–12% by 2028 [VERIFY V9]); ch22_prompt_energy.csv: Google 0.24 Wh full stack vs. 0.10 Wh active chips only (blog: "not been verified by an independent third-party"); Epoch ~0.3 Wh (2025); 2023 estimate ~2.9 Wh [VERIFY V10] | F22.12–F22.15 |
| 22.7 | AI and science (650) | Deep | A discovery claim is settled by the field's own checks, which take longer than the announcement | Hana's "first AI-discovered…" headline (constructed) → chemistry newsletter's "two million new materials" (stage 1 filled) → Your Turn | ch22_science.csv: Nobel 2024 [VERIFY V11]; GNoME and Cheetham & Seshadri (2024, *Chem. Mater.* 36(8), 3490–3495); Erdős #728 (Jan 2026, AI-assisted, Lean-verified; Sothanaphan, arXiv 2601.07421); May 20, 2026 unit-distance result (developer-reported, external mathematicians' companion paper) [VERIFY V3]; C26 one sentence | F22.16 |
| 22.8 | What has already aged? (700) | Studio | Recap box (~150). **Aging check** defined: what does the best current source say; verdict on the old claim as a description of today (Ch. 8 scale); what changed (facts, status, names). **Book's own example:** the 2014 From the Field entry's row on "machines that talk with users", its claims printed. **Hana** re-checks two 22.3 claims (constructed later date) | Book's 2014 example + Hana → energy row (column 1 filled) → the essay | the chapter's 12-row aging checklist (from the refresh rows) | F22.17 (2014–2026 axis, own events), F22.18 |

**Case Study (700): C31 revisited.** Tree **none** (no output shown wrong); evidence-status lesson; the three kinds of check (competition graders, graders chosen by the developer, a proof checker) and what each does not check; 2026 update box (reported). **Short 1 — the "ten solved problems" post (October 17–18, 2025):** an executive's post said a model had found solutions to ten open problems; the problem site's maintainer said "open" meant he knew of no solution; the model had found existing papers; posts deleted (reported). Tree none; **chain link 2 "checked before use?" failed (reported)** (F22.19). Since then (dated): in January 2026 an AI-assisted solution to problem #728 was checked with Lean and written up (Sothanaphan, 2026); on May 20, 2026 the developer reported a result checked by outside mathematicians (reported [VERIFY V3]). **Short 2 — GNoME (2023–2024):** tree none; a dispute about what counts as a discovery.

**Ethics Lens (~400):** who pays for the frontier (local grids; IEA), who must check overclaims, concentration (AI Index 2026: industry over 90% of notable frontier models in 2025), responsible-AI benchmarks lag and documented incidents rose to 362 (AI Index 2026); pointer to Ch. 18.
**Career Connection (~300):** technology journalist, sustainability analyst, procurement officer, research scientist, policy staffer, product manager; one dated line: an opinion gap (AI Index 2026: 73% of experts vs. 23% of the public expect a positive effect on how people do their jobs).
**From the Field (~400):** Şeker (2014), facts limited to the entry, which "draws on" Fichman et al. (2014); Moore's law defined by the book (Moore, 1965, 1975), marked as the book's addition; the Q&A-machines row and the lock-in/standards row; present-day connections marked; limit: predates LLMs.
**Summary + Key Terms (16):** as-of date · evidence status · measured (claim) · reported (claim) · forecast · outside evaluation · capability claim · reasoning model · test-time compute · time horizon (of an agent) · computer-use agent · training compute · FLOP · scaling (of AI models) · system boundary (of an energy estimate) · aging check.

## 6. Characters

Hana only. New details: keeps a dated clippings file of AI announcements (date, source, status); writes a one-page zine column for local artists, "AI image and video tools, as of [date]," every claim tagged; still draws by hand (profile and Ch. 18 contract clause kept); the zine collective considers an open-weight model on a member's computer for alt-text drafts (Ch. 13, Ch. 18 consistent); re-checks two of the column's agent claims a term later (constructed). **No link between Hana and the From the Field entry.** Details logged for Ch. 23's use.

## 7. Retrieval

Warm-up (3; the third with confidence): "matches PhD experts" — what to know first; do written-out steps mean fewer factual errors; one chat question's electricity vs. one minute of a laptop. Check Yourself 2 per section. **Spaced Review:** Ch. 8 (an AI tool's own "yes" is never a source; independent check vs. outside source with Ch. 9), Ch. 12 (open-weight vs. local), Ch. 14 (50% vs. 80%; error compounding), Ch. 21 and Ch. 19 marked "if you have read it" (review trigger; who settled the A-Lab claim). Forward: Ch. 23.

## 8. Alignment and package

| Obj. | Taught | Practiced | Figures | Assessed |
|---|---|---|---|---|
| O1 | 22.1, Opening | every section; Lab 22.1 | F22.2–F22.4 | A; B1; CSQ 1–2 |
| O2 | 22.2 | sequence | F22.5–F22.7 | A; B2 |
| O3 | 22.3, 22.5, 22.6 | sequences; Lab 22.3 | F22.8, F22.11, F22.12 | A; B3 |
| O4 | 22.5 | sequence | F22.11 | A; C1 |
| O5 | 22.6, 22.7, Case | sequences; Lab 22.2 | F22.13–F22.16, F22.19 | A; B4; CSQ 3–5 |
| O6 | 22.8 | Lab 22.4; essay | F22.17, F22.18 | C2; essay |

Review A 12 (keys rotated; correct option longest in ≤ 2; distractors from M1–M6) · B 4 · C 2 · Spaced 4 + 1 · Discussion 5 · CSQ 5 · optional Mini-Project. Appendix E block: all Check Yourself keys, faded keys, odd answers; even → private/ch22-answers-even.md.

## 9. Optional essay — "What has already aged?"

Submit: (1) three dated claims from one section's box, quoted with section and as-of date; (2) status table (then-status, now-status, source opened today; an AI tool's answer is never the source); (3) aging verdicts on the five-point scale with what changed; (4) essay 500–700 words: what aged, what held, what it means for one task in your field, at least one forecast judged or dated for a later check; (5) revision after a skeptical reread; (6) AI Use Declaration (five elements). Full marks possible for "nothing has aged yet; I will check again on [date]." Rubric (10; lower-level rule): Task: essay 3 · Process: status table 1.5 · Process: revision 1.5 · Verification: aging verdicts 2 · Declaration 2; four parallel levels as in Ch. 17. Alternative (no AI or no reliable internet, ~70 min): the provided "then and now" packet; same rubric.

## 10. Figures (20; no generative imagery)

**Signature (book-wide):** `capability_timeline(highlight=None, note=None, events=None, as_of="October 2026", title=None, start=None, end=None)` and `timeline_height(note)` in figures/scripts/ch22_figures.py. Events from data/ch22_timeline.csv (id, date, label, status, who, section, aged, as_of) unless `events` is passed; ≤ 9 event boxes (the legend does not count); year axis; labeled "as of" line. Status by tag text and position: "measured: <who>" and "reported: <who>" solid rectangles (reported with an open corner mark); forecast right of the as-of line with "forecast: <who>" and a light fill (never dashed, never hatched); dashed outline = the book's inference only; `aged` events carry the tag "aged" and a folded-corner mark (never color alone). `highlight` = id or list (role "highlight" + thick border, as `work_loop`). Charts: data points solid; fitted trends **dotted, labeled "trend, not data (fitted by …)"**; log axes print "each step is ten times the last".

Imports: `work_loop` (ch01), `agent_loop` (ch14), `modality_tokens` (ch13), `verification_funnel` (ch08), `failure_chain` (ch04).

F22.1 map · F22.2 storyboard (2025: three kinds of check) · F22.3 signature · F22.4 evidence status and crosswalk · F22.5 test-time compute · F22.6 PersonQA (developer's values) · F22.7 benchmark jumps (AI Index) · F22.8 METR horizons (log) · F22.9 computer use (`agent_loop`) · F22.10 modalities (`modality_tokens`) · F22.11 open–closed gap · F22.12 compute (log; dotted trend) · F22.13 trend vs. forecast · F22.14 electricity · F22.15 boundary (0.10 vs. 0.24 Wh) · F22.16 science funnel · F22.17 timeline 2014–2026 (aged) · F22.18 aging card · F22.19 chain (Short 1) · F22.20 summary card. Titles from the CSVs where computed.

## 11. Labs (optional; printed; dated)

22.1 Tag a Launch Post (25 min) · 22.2 Trace an Energy Number (30 min) · 22.3 Read a Log Chart (20 min; chart **and** data-table version) · 22.4 What Has Aged? (25 min).

## 12. Risks

No hype, no doom (dated, tagged; "not plateauing" attributed); vendor neutrality (≥ 2 providers or none outside the case; vendor claims "reported"); no aggregator sources; IEA editions never in one sentence; no individual named (D-10.8); interested sources labeled; "reasoning model" glossed as a provider term; bot-blocked pages listed, never bypassed; `\@` for any handle; no hardcoded figure numbers.

## Decisions taken under delegation (D19)

X1 tags, eight sections · X2 Verify, Decide second · **X3 evidence status (measured through Ch. 9's outside source / reported / forecast / the book's inference) and the crosswalk (book-wide, optional for other chapters per the brief)** · **X4 `capability_timeline` API; each edition edits the CSV** · X5 C31 widened to five systems and 2026 · **X6 dotted "trend, not data"** · X7 product names only in boxes and the case · X8 times as §1 · **X9 one CSV-backed box per section; keys test the method or box values** · X10 From the Field as registered · X11 Hana only, no link to the 2014 entry · X12 22.6 calculation is an illustration · X13 when to read: after Ch. 21.

## Author-only items

1. From the Field: approve the 2014 entry with "draws on Fichman et al. (2014)"; confirm the entry's page range. Optional anecdote, never written for you.
2. Optional syllabus line ("Ch. 22, optional, after week 15").
3. Final voice edit.

## Editor items

E3 read in Chrome: openai.com unit-distance page; nobelprize.org 2024 chemistry; LBNL-2001637 PDF; AFP 2025 copy on thesun.my · E4 the "then and now" packet each term · E5 the Ch. 14/16/19/20 pointers to Ch. 22 (assembly) · E6 adopt X3/X9 wording in the brief if wanted.

## Review changes (v0.1 → v0.2)

High: IMO 2026 box (1); DeepMind attribution, AFP caution, Reuters timing (2); Seed Prover, Aristotle, human context (3); "measured" via Ch. 9's outside source, crosswalk (4); promises cut to Ch. 17 and 21 (5); one CSV box per section (6). Medium: METR TH 1.1 values for three providers, OSWorld human baseline (7); IEA 2026 current, 2025 as aging example (8); LBNL stub removed (9); M2 reframed (10); Shojaee NeurIPS 2025 confirmed, reply labeled informal (11); Erdős 2026 lines (12); 22.8 book's own 2014 example, Hana on 22.3 (13); read after Ch. 21, Spaced Review marked (14); answering time (15); Ch. 23 sentence (16); timeline rules (17). Low: C31; settings (parameters); lock-in wording; Fichman 329–354; O6 one verb, Interpret = Understand; opinion-gap line (18); DeepSeek-R1 *Nature* 645(8081), 633–638; Cheetham & Seshadri 3490–3495; Google statement from the blog's footnote; Chatbot Arena named; IEA's 100,000 households (19).

## Draft v1 notes (2026-10-18)

Drafted from this blueprint: full route 8,180 words (~55 min; ~62 with Ethics, Career, From the Field, Summary), fast route ~3,300 (~22 min); chapter ≈ 12,500 words excluding comments. Tool protocol added as a Key Term (17). METR values taken from Time Horizon 1.1 raw data (this book's fit reproduces METR's ~129-day doubling). The "Chinese models are open-weight" line was dropped pending a direct read. Details: docs/production/handoff/ch22.md.
