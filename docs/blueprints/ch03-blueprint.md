# Chapter 3 blueprint — Inside Large Language Models

Status: v0.2 (2026-10-18), awaiting the author's approval. v0.2 applies an independent pedagogy review (6 must-fix, 11 should-fix; see "Review changes" at the end). No chapter text is written until this blueprint is approved.
Part I — Understanding AI · Syllabus week 2 (shared with Chapter 2) · Path: Core · Featured students: **Elif** (main) and **Hana** (they/them; short examples), per docs/characters.md · Work Loop step highlighted in the Chapter Map: **Prompt** (know what the model actually receives), with Verify second.

**Source material.** The syllabus's week-2 concept session (tokens, training and inference, context window, retrieval, tools, agents; demo: tokenizer and repeated sampling) and Thursday's "Probe the model" lab. Reading R1: Wolfram (2023). No Haliç lecture covers this chapter; it is built from the cited research below. From the Field: candidate source is the author's 2024 English paper on large language models (Drive 1yPpN_rmplzKfjhJs7yXyE8YTBATr0_db), to be read before drafting; never constructed (see Proposals).

## 1. Outcome link and week 2

| Item | Value |
|---|---|
| Syllabus outcomes | **LO1** (how generative and agentic systems work in outline and why they fail), **LO3** (verifying outputs) |
| Studio artifact | **A2 — 15-term concept map**, due Monday, February 1, 2027. A2 lives in Chapter 2 (section 2.7 and its Application Assignment, one rubric). **Part 1** = at least 7 Chapter 2 terms, at home. **Part 2** = at least 5 Chapter 3 terms with worked definitions, links to Chapter 2 terms and verification, started in Thursday's lab (section 3.6). Chapter 3's Application Assignment points to Chapter 2's brief and rubric, adds Part 2 guidance and has no second rubric |
| In-class time | Tue Jan 26, second half of the concept session (first half: Chapter 2's opening case, D17); demo: tokenizer and repeated sampling. Thu Jan 28: Lab 3.1 "Probe the model" (section 3.6) |
| Readings | R1 Wolfram (2023): Chapter 2 assigns "what is a model" and "neural nets"; Chapter 3 assigns the opening section on producing text one word at a time [VERIFY section title]; together ~15 minutes |

### Week 2 workload (out of class), both chapters

| Item | Time |
|---|---|
| Chapter 2 Core reading + paper task | 30 + 15 min |
| **Chapter 3 Core reading** (≤ 4,500 Core words incl. examples) | **25–30 min** |
| R1, selected sections | ~15 min |
| A2 Parts 1 and 2 at home (15 worked definitions, verification, declaration) | 45–60 min |
| **Total** | **~2.2–2.5 h** (syllabus: 1–2 h) — see Proposal 3 |

**Week-2 word-budget exception** (as in Chapter 2): Core subsections ~600–800 words; 3.2 and 3.5 are capped at 800. The chapter still reaches ≥ 10,000 words with the Opening Case, Deep sections, Case Study, Ethics Lens, Career Connection, From the Field and the End-of-Chapter Package.

## 2. Chapter objectives (5)

| # | Objective — after this chapter you will be able to… | Bloom | LO | Framework tags |
|---|---|---|---|---|
| O1 | **Explain** how a large language model produces a response: text becomes tokens, the model scores every possible next token, one is sampled, and the loop repeats inside a context window | Understand | LO1 | UNESCO:TECH-U · AI4K12:2 · LM:how-works |
| O2 | **Explain** the difference between training and inference, and its consequences: a knowledge cutoff, and no learning from your conversation | Understand | LO1 | UNESCO:TECH-U · AI4K12:3 · 4D:DEL |
| O3 | **Judge** what a retrieval- or tool-assisted answer still requires you to check | Evaluate | LO1, LO3 | 4D:DISC · UNESCO:TECH-U |
| O4 | **Test** a model's behavior with a simple probe (prediction, prompt, result, conclusion) and record the evidence | Apply | LO1, LO3 | 4D:DISC |
| O5 | **Complete** A2: at least 5 Chapter 3 terms with worked definitions, labeled links to Chapter 2 terms, and verification (including one corrected AI definition) | Create | LO1 | UNESCO:TECH-U |

## 3. Prerequisites and promises kept

From Chapter 1: generative AI system, prompt, output, "producer of likely text", same prompt → different answers, the three lanes (search, generation, search-then-generate). From Chapter 2: model as learned settings (parameters), self-supervised learning, training vs. inference, generative AI ⊃ large language model, memorization caveat (Carlini et al., 2021). **Promises kept:** the next-token mechanism behind "likely text" (Ch. 1 §1.1), why two runs differ (sampling), and why some tools cite sources (retrieval).

## 4. Misconceptions (refutation pattern; six)

| # | Misconception | Where |
|---|---|---|
| M1 | "The model reads words and letters the way I do" | 3.1 |
| M2 | "The model looks up the answer in a database of facts" (Ch. 1 M1) | Opening Case, 3.2 |
| M3 | "The same prompt should always give the same answer; a different answer means an error" | 3.2 |
| M4 | "It learns from my conversation, and its knowledge is complete up to its cutoff" (hedged: some products store notes, a separate feature; not training) | 3.3 |
| M5 | "If it fits in the context window, the model uses all of it equally well" | 3.4 |
| M6 | "If the tool searched the web or my files, the answer is correct" (mechanism level only: retrieved text can be wrong, outdated or misread; checking citations is Ch. 8–9) | 3.5 |

Agent anthropomorphism is left to Chapter 14.

## 5. Concept sequence

**Session question, answered in the Summary:** *Does a language model know things, or does it predict text?* Answer: mechanically, it predicts text, one token at a time; what looks like knowledge comes from patterns in its training text, its context and its tools. Whether that adds up to "knowing" is debated (Chapter 23).

**Opening Case (400–600 words): the reversal curse** — a research finding, stated as such, with model names and dates in the first paragraph. Researchers fine-tuned models on made-up facts of the form "A is B" and found they could not answer "B is A" (Berglund et al., 2024). In a second test with real people, a widely used chat model (2023) named a celebrity's parent far more often than it named that parent's famous child [VERIFY model, numbers; the parent is named only as in the paper, or anonymized]. Chapter question: if the model "knows" one direction, why not the other? **The explanation sits in Core:** 3.2 (prediction follows patterns in text) and 3.3 (training text mostly states such facts in one direction). A line tells students: "If your tool answers both directions, that is evidence too: newer models and search change the result." *Departure from the book map ("lab-centered") flagged in Proposal 1.*

**Prediction before the evidence:** "Which costs more tokens: an English sentence or the same sentence in Turkish (or your other language)?" Answered in 3.1 with a **computed figure** from a named open tokenizer (version recorded; data/ch03_tokens.csv), consistent with the published pattern (Petrov et al., 2023).

**Two meanings of "sampling."** A contrast box in 3.2: *sampling* in Chapter 2 (choosing which examples go into a dataset) vs. *sampling* here (picking the next token from the scores). A pool note and a Review A item reinforce it.

| # | Subsection | Tag | One new core idea | Examples | Figures |
|---|---|---|---|---|---|
| 3.1 | Words become tokens | Core | Text is split into tokens (words, parts of words, symbols); the model works with token numbers, not letters; consequences: letter counting, rare names, length limits and cost, and different costs across languages | **Elif** compares token counts for an English and a Turkish psychology abstract; a drug name splits into odd pieces (health, unnamed) | F3.2 computed; F3.3 Signature 4, stage 1 (tokens) |
| 3.2 | Predicting the next token | Core | The model scores every possible next token; one is sampled; the loop repeats; a "temperature" setting changes how often less likely tokens are picked (one paragraph); why answers differ; why fluent text can be false; two meanings of sampling | An open completion with real spread ("A good name for a coffee shop near campus is …"; illustrative scores); repeated-sampling demo; reversal-curse explanation | F3.3 stage 2 (scores, sampling); F3.4 (scores at two temperatures, merged) |
| 3.3 | Training, then inference | Core | Pretraining on large text (self-supervised next-token prediction, Ch. 2) → instruction tuning and learning from human feedback (two sentences; Ouyang et al., 2022); at inference the settings are fixed; knowledge cutoff; not learning from your chat | A question about last week's news (everyday); why facts written one way are learned one way | F3.5 (training stages → frozen settings → inference, with cutoff; merges the old F3.6/F3.7) |
| 3.4 | The context window | Core | Everything the model receives in one turn (system instructions, conversation so far, pasted or retrieved text, your prompt) must fit; information in the middle of a long context is used less reliably. **Diagnostic only:** predict which parts of a long input are likely to be missed, then check. Designing context is Chapter 6 | **Hana** asks about a long public-domain historical document (arts/humanities); a constructed, anonymized support thread for Lucía with a one-line privacy caution and a pointer to Ch. 15 | F3.3 stage 3 (context); F3.6 drawn from published values in Liu et al. (2024), model and year in the title |
| 3.5 | Retrieval and tools (and what agents are) | Core | Retrieval adds documents to the context; tools let the system run code, a calculator or other software; neither changes how the model predicts, both change what it receives; what still needs checking. Agents: one paragraph (a system that repeats model → tool → result steps toward a goal) with a pointer to Chapter 14 | The same question answered plainly, with search, and with a calculator tool | Reuse F1.4 (three lanes) with a new caption; F3.7 "what each adds / what you still check" table-figure only if not redundant with the text table (decide in drafting) |
| 3.6 | Probe the model (A2 Part 2) | Studio | A probe = prediction, prompt, result, conclusion; a "the model got it right" result is valid evidence; turning probe findings into worked definitions and labeled links | Students' own probes in Thursday's lab | F3.8 (probe record template), F3.9 (mini-map linking Ch. 3 to Ch. 2 terms) |
| Deep 3.A | Attention in plain words | Deep | Transformers let each token's representation draw on other tokens in the context (Vaswani et al., 2017) | Pronoun reference ("the trophy didn't fit in the suitcase because it was too big") | F3.10 |
| Deep 3.B | Why scale changed things | Deep | Prediction error fell in a predictable way as models, data and compute grew (Kaplan et al., 2020; Hoffmann et al., 2022) [VERIFY]; a two-sentence pointer to Chapter 8 for why confident errors persist | — | F3.11 (drawn from published values, or omitted) |

Other anatomy parts:

| Part | Plan |
|---|---|
| Case Study (1 main + 2 short) | **Main:** the reversal curse (Berglund et al., 2024), traced through Signature 4. **Short 1:** "Lost in the middle" (Liu et al., 2024). **Short 2:** tokenizers cost some languages several times more tokens for the same text (Petrov et al., 2023) |
| Ethics Lens | Language fairness: token cost and quality across languages (Elif); whose text trained the model, and consent (pointer to Ch. 18) |
| Career Connection | Customer-support knowledge-base manager (retrieval), technical writer (instructions and context), localization specialist (tokens and languages), data analyst using code tools; descriptive only |
| From the Field | The author's 2024 English LLM paper, facts limited to the paper, or the author's own case; disclosure per D16 if commercial (Proposal 2) |
| Summary + Key Terms | Answers the session question (hedged); Signature 4 complete as the summary visual |

## 6. Example plan (worked → faded → your turn)

| Skill | Worked | Faded | Your Turn |
|---|---|---|---|
| Tokens (O1) | Elif's abstract: English vs. Turkish token counts; what follows for cost and length limits | A long product or drug name split into tokens: reader predicts why letter counting can fail | Count tokens for a sentence in your language with any tokenizer page |
| Next-token sampling (O1) | Coffee-shop completion: illustrative score table; two samples at two temperatures | Reader completes the next step for a different open prompt | Ask one open question 5 times; describe what changes and what stays |
| Training vs. inference (O2) | Why a model may not know last week's news, and what a search tool changes | Reader decides which of three questions need current information | List three questions in your field that need current information |
| Context, diagnostic (O1) | Hana's long document: predict which facts in the middle are likely to be missed; check | Reader predicts misses for a provided long text | (Lab 3.1, probe 3) |
| Retrieval and tools (O3) | One answer with two retrieved sources: which claims the sources support, which they do not, what the calculator tool fixed | Partly marked answer: reader completes the marking | A provided retrieved answer with sources: mark supported, unsupported, unclear |
| Probing (O4) | A complete probe record | Partly filled probe record | Lab 3.1 |
| A2 Part 2 (O5) | One Chapter 3 worked definition ("token"), two labeled links to Chapter 2 terms ("pretraining *is a kind of* self-supervised learning"), and one AI definition corrected using a probe result | Reader labels 3 links and corrects one provided AI definition | A2 Part 2 |

Fields: psychology, history/arts, business, health (drug names), everyday, languages. No Sam cameo; Lucía only in the constructed thread.

## 7. Retrieval and spacing

- Warm-up: three questions (Does a model read letters? Does it remember your chat tomorrow? If a tool searched the web, is its answer correct?).
- Check Yourself after 3.1–3.6, 2–3 items each, at least one "why", **all answerable from Core** (dev-memo A13 lesson).
- Spaced Review: Chapter 1 (same prompt, different answers; fluent vs. correct; three lanes) and Chapter 2 (labels; self-supervised learning; memorization caveat; sample vs. sampling).
- Spaced forward: context design → Ch. 6; confident errors → Ch. 8; citation checking → Ch. 8–9; tool ecosystem → Ch. 12; agents → Ch. 14; privacy of pasted context → Ch. 15; "does it know?" → Ch. 23.

## 8. Alignment matrix

| Objective | Taught | Practiced | Figures | Assessed | Artifact |
|---|---|---|---|---|---|
| O1 | 3.1, 3.2, 3.4 | Token, sampling and context sequences; Lab 3.1 probes 1–3 | F3.2–F3.4, F3.6 | Review A; B1 | A2 terms |
| O2 | 3.3 | Training-vs-inference sequence; Lab 3.1 probe 4 | F3.5 | Review A; B2 | A2 links |
| O3 | 3.5 | Retrieval/tools sequence (incl. Your Turn); Lab 3.1 probe 4 | F1.4 reuse | B3; C1; Case Study Questions | — |
| O4 | 3.6 | Lab 3.1 | F3.8 | B4 | Probe record |
| O5 | 3.6 | A2 Part 2 sequence | F3.9 | Application Assignment (points to Ch. 2 rubric) | **A2** |

Counts follow the anatomy (A 10–15, B 3–5, C 2–3, Spaced 3–5, Discussion 4–6, Case Study Questions 4–6, optional Mini-Project); every item carries O · LO · Bloom; Review A distractors from M1–M6, plus one item on the two meanings of sampling. Odd answers → Appendix E; even → private/.

**A2 Chapter 3 term pool:** token · tokenizer · next-token prediction · probability distribution · sampling (of tokens) · temperature · pretraining · instruction tuning · human feedback · knowledge cutoff · context window · system prompt · retrieval · tool use · agent. Any Chapter 3 Core Key Term also counts; a term in both pools (e.g., inference) counts once. Pool note: use one sense per term ("sample" in Chapter 2 is not "sampling" here). The eLearning alternative glossary must include Chapter 3 pool terms.

## 9. Figures (titles state the finding; each serves an objective; ≤ 9 boxes)

| ID | Title | Type | Section | Objective |
|---|---|---|---|---|
| F3.1 | Chapter 3 at a glance (AI Work Loop, Prompt highlighted) | Chapter map | Opening | all |
| F3.2 | The same text costs different numbers of tokens in different languages | **Computed chart** (named open tokenizer; data/ch03_tokens.csv) | 3.1 | O1 |
| F3.3 | A response is built one token at a time from scores over every possible next token | **Signature 4: Anatomy of an LLM Response**, built in stages: tokens (3.1), scores and sampling (3.2), context window (3.4); complete version in the Summary; ≤ 9 boxes | 3.1, 3.2, 3.4, Summary | O1 |
| F3.4 | Temperature changes how often less likely tokens are picked | Computed from illustrative scores at two temperatures (labeled illustrative) | 3.2 | O1 |
| F3.5 | Training changes the settings; inference only uses them, so knowledge stops at the cutoff | Stages + frozen settings + cutoff | 3.3 | O2 |
| F3.6 | Information in the middle of a long context was used less reliably (2023 models) | Line chart drawn from published values (Liu et al., 2024), model and year in the title | 3.4 | O1 |
| F1.4 (reuse) | Search points to sources; generation writes new text | Chapter 1 three lanes, new caption | 3.5 | O3 |
| F3.7 | (optional) What retrieval and tools add, and what you still check | Decide in drafting; cut if it repeats the text table | 3.5 | O3 |
| F3.8 | A probe turns a guess about a model into evidence | Probe record template | 3.6 | O4 |
| F3.9 | Chapter 3 terms link to Chapter 2 terms | Mini concept map | 3.6 | O5 |
| F3.10 | Attention lets each token draw on the others | Schematic | Deep 3.A | (Deep) |
| F3.11 | Prediction error fell steadily as models and data grew | Drawn from published values [VERIFY], or omitted | Deep 3.B | (Deep) |
| F3.12 | Chapter summary card | Summary card | Summary | all |

12 figures plus Signature 4 stage variants. Cut from v0.1: agent loop (Signature 9 belongs to Ch. 14), separate score bar chart (merged into F3.4), separate training/inference contrast (merged into F3.5), separate context diagram (now a Signature 4 stage). Interactive in Compass (MVP scope, D7): Signature 4 and a token explorer.

## 10. Labs (tool-neutral)

**Lab 3.1 Probe the model** — Studio, Thursday in class, 45 minutes, teams of 3–4, individual write-up.

| Minutes | Step |
|---|---|
| 0–5 | Briefing; each team member takes one probe (jigsaw); teams of 3 skip probe 4 or share it |
| 5–20 | Each student runs their probe: write the prediction, run the prompt, record the result and conclusion |
| 20–30 | Team pools the four probe records and agrees on one sentence per probe |
| 30–43 | Each student, individually, writes at least 3 worked definitions and labeled links for A2 Part 2 from the probes |
| 43–45 | Exit: one link you are unsure of |

Probes (tool-neutral; current tool steps, memory-off and temporary-chat settings in Compass):
1. **Tokens:** count letters in a long word or name; then ask for a spelled-out or code-based count. "The model got it right" is a valid result; the book explains why it may.
2. **Sampling:** one open prompt from your own field, five times in new chats; mark what stays and what changes (extends Tuesday's demo).
3. **Context:** a provided long public-domain text with one fact placed at the start, middle and end; ask about each.
4. **Cutoff and search:** questions about provided dated events (not the model's self-reported cutoff), with and without search where the tool allows it.

Output: the team's probe records (shared) and each student's A2 Part 2 draft (individual).

Optional home labs: **L3.2 Tokens across languages** (15 min; compare one sentence in two languages on a free tokenizer page) and **L3.3 Same prompt, five answers** (15 min).

Accessibility and alternatives: dated sample outputs on eLearning for every probe (opt-out and no-device route: analyze the samples instead of running prompts); a paper version of the sampling probe (draw tokens from a provided score table with dice); a screen-reader-friendly probe record table; no personal or confidential data in prompts.

## 11. Risks and checks

- Reversal curse: separate the synthetic-fact result from the celebrity test; state model and date; protect the private family member's name (use the paper's framing or anonymize); refresh-list entry because newer models may answer both directions.
- Token counts depend on the tokenizer and version: name both, date the figure.
- "Lost in the middle" was measured on 2023 models: present as a documented pattern to test, not a law; F3.6 title carries model year.
- Context-window sizes and memory features change quickly: no product numbers in Core; dated examples only in Compass.
- No anthropomorphic verbs: "the model scores", "the system retrieves", never "thinks", "reads", "remembers".
- Characters: Elif (main), Hana (they/them); log new details in docs/characters.md.
- Workload: Core ≤ 4,500 words; week-2 total flagged to the author (Proposal 3).
- Boundaries: no context design (Ch. 6), no confident-error mechanism beyond a pointer (Ch. 8), no citation-checking method (Ch. 8–9), agents one paragraph (Ch. 14).

## Proposals that need the author

1. **Opening case:** the book map lists Chapter 3 as "lab-centered (token and probability explorer)" without a named case. Approve the reversal curse (Berglund et al., 2024) as the Opening Case and main Case Study.
2. **From the Field:** confirm that your 2024 English LLM paper may be the source (or name another piece or case of yours), and whether a commercial-interest disclosure applies.
3. **Week-2 workload:** with A2 realistically at 45–60 minutes, week 2 comes to about 2.2–2.5 hours outside class (syllabus: 1–2 h). Option: make R1 optional in week 2 (it stays in Further Reading), which brings the week to about 2 hours. This changes the live syllabus, so it is your call.

## Review changes (v0.1 → v0.2)

Lab 3.1 redesigned as a timed jigsaw with individual A2 write-up; A2 Part 1 moved to home time (Chapter 2 text updated); O5 aligned with the full A2 rubric (definitions, links, verification, corrected AI definition) and Part 1/Part 2 named in both chapters; "two meanings of sampling" added; agents cut to one paragraph, agent-loop figure and agent misconception moved to Ch. 14, confident-error Deep section reduced to a pointer to Ch. 8, 3.4 made diagnostic (context design stays in Ch. 6), session answer hedged (Ch. 23); Core capped at 4,500 words, temperature and RLHF shortened, cameos dropped, misconceptions cut to six; figures merged and Signature 4 built in stages; Bloom levels and framework tags corrected, O3 recast as an Evaluate objective with a Your Turn; opening case dated, its explanation moved into Core, departure from the book map flagged; Lucía's thread constructed and anonymized, Hana's document public domain; probes accept null results and use provided texts and dated events, with opt-out and screen-reader routes; R1 section named; health example added.
