# Chapter 1 — developmental memo (2026-10-17)

Inputs: four independent reviews run in parallel without sharing reports — subject-expert reviewer, pedagogy reviewer, student-reader panel (Maya / Daniel / Ayşe), fact-checker (docs/factcheck/ch01.csv). The author asked for a finished chapter, so the editor decided on the changes below and applied them in revision v2. Items only the author can supply are listed at the end.

## Decisions — accuracy and currency (subject expert, fact-checker)

| # | Change | Why |
|---|---|---|
| A1 | 1.1: two reasons answers differ — sampling within one tool; different models, data and hidden instructions across tools | Chance alone explained only half of the demo |
| A2 | 1.1: autocomplete analogy holds for the basic step (predict what comes next) and breaks on scale and instruction tuning | Old wording contradicted "producer of likely text" |
| A3 | 1.1: many search engines now show an AI summary above links — that summary belongs in the third lane | Product reality, late 2026 |
| A4 | 1.1: "usually new wording, but it can repeat training passages almost word for word"; table cells "No human author" | Memorization; "Nobody" was glib |
| A5 | 1.2: assistant was trained on past chats with top performers' chats weighted more; expert explanation labeled as the researchers' hypothesis | QJE 2025, Section II |
| A6 | "Real or realistic work tasks" (not "real workplaces") wherever the three studies are summarized | Only the support study was real work |
| A7 | Opening + Case: customer satisfaction (NPS) did not change significantly; "moderately rare problems" stated precisely; ignoring routine suggestions labeled as our inference | QJE 2025 |
| A8 | Deep 1.A: parallel-trends assumption; managers chose onboarding order; terms corrected (staggered design, difference-in-differences analysis); randomization balances "on average" | Methods accuracy |
| A9 | 1.3 table updated: exact counting / long calculations without a calculator or code feature; recent events "when the tool does not search"; "choosing for you" moved to Frame | Late-2026 model capability |
| A10 | 1.4: outdated information also comes from skipped or stale searches; overconfidence partly from tuning toward answers people rate highly | Mechanism |
| A11 | Deep 1.B: Article 4 as amended in 2026 (support the development of AI literacy; no guaranteed level) with the original 2025 wording for context — per fact-check | Law changed in July 2026 |
| A12 | Anthropomorphic verbs removed ("read", "looked", "does the thinking", "colleague", "keeps track", "hides behind") | Style sheet §1 |

## Decisions — learning design (pedagogy reviewer, student panel)

| # | Change | Why |
|---|---|---|
| P1 | Objectives numbered O1–O6 with framework tags; O1 restored in full; every end-of-chapter item tagged O-ID · LO · Bloom | Traceability |
| P2 | 1.7 gets a plain-language box listing LO1–LO7, so A1 goals can be tied to them | Students could not complete A1 |
| P3 | Reading time stated honestly in the Chapter Map (about 35–50 minutes for Core, more with Your Turns); map title "Chapter 1 at a glance" | "20 minutes" was wrong |
| P4 | "Fluent" defined in 1.4; the opening's "English fluency" finding reworded as improved English writing | Two meanings confused ESL readers |
| P5 | 1.5 policy: where drafting ends and outsourcing begins (if the assignment's purpose is the thinking or writing itself, AI drafting it is outsourcing unless the instructor allows it); whether permitted-zone uses go in the declaration (list them briefly); confidential and personal data in public tools added to "not acceptable" | Gap and contradiction found by all three panels |
| P6 | Baseline reconciled: A1 records current habits plus a first structured run in Lab 1.2; non-users have a stated path in 1.7; graded for completeness and quality of process, never for how much or how "acceptably" AI was used before | Contradiction between "not judged" and a graded artifact |
| P7 | 1.3 Your Turn and Lab 1.2 use the same three tasks; Lab 1.2 group share made optional to fit 45 minutes | Two different task lists |
| P8 | 1.2 restructured: pattern signaled first; worked example right after Study 1 / F1.5; faded example with the same three steps after Study 2; non-essential numbers moved to the table; control group, random assignment and percentage points glossed; one Core sentence on why the staggered rollout supports a causal reading; Bastani comparison group stated | Cognitive load, contiguity, causal question in Core |
| P9 | 1.3 worked example changes one variable only (same task, essay pasted vs. not pasted); faded example keeps the Task / Test / Verdict structure with a partly filled test ("which gallon?") | Worked example modeled a flawed test |
| P10 | 1.4: concrete worked trace of the remote-work statistic (per fact-check); explicit red flags ("exactly", "regardless", an organization you cannot find) | Step 2 was vague; students need cues |
| P11 | M2 refutation added (newer models do not "handle everything"); Summary keeps "likely reason" hedging; Warm-up revisited in the Summary | Refutation pattern; consistency |
| P12 | Box types separated: Check Yourself (tip), Your Turn (important), worked and faded examples (note); a line in 1.1 says Your Turns are practice, not graded, and where answers live | Signaling; "are these required?" |
| P13 | Language pass for ESL readers: idioms replaced ("oracle", "traps", "decoration", "rescue", "bites"); 1.1 definitions split one idea at a time; "piece" = word or part of a word; "Fortune 500", "brief", "sanctioned" glossed | Ayşe |
| P14 | End-of-chapter package rebuilt: Review A as transfer items (not copies of Check Yourself), new M4 and M5 items, matching with six uses, A9 replaced with an interpretation item; B4 tightened with a scoring guide; C1 retagged O2, new C3 for O3; interleaved Spaced Review with a new case; Discussion 1 retagged; Case Study Q1 now answerable from Core | Item-writing rules (Haladyna et al., 2002) |
| P15 | A1 rubric: four levels (Exemplary / Proficient / Developing / Beginning) with descriptors; declaration and goals scored separately inside the 2-point criterion; alternative pathway mapped to each criterion | Assessment-builder rule |
| P16 | Names and pronouns varied; one positive arts use added; a psychology research example added | Inclusion; Ayşe |
| P17 | Answer keys: odd answers → appendix/answers.md; even answers → private/ | Assessment-builder rule |

## Not changed (with reason)

- Forward references to later chapters: kept but reduced in Core; they are part of how the book connects.
- Figure 1.4 and the 1.1 table both kept: the figure shows the process; the table is reduced to "what you must still check".

## Waiting for the author

1. Five recurring students (docs/characters.md, decision D9) — [CHARACTER] placeholders remain.
2. From the Field story — [AUTHOR ANECDOTE NEEDED] remains.
3. Final voice edit (pipeline step 8) — the chapter is never marked "done" by the editor.
4. Optional: replace one Figure 1.3 panel with a second provider's output (both current panels are Anthropic models, labeled as such).
