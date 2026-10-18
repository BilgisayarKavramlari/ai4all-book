# Lab 3.2 — Tokens Across Languages

| Field | Value |
|---|---|
| Type | Explore |
| Objectives | O1 (LO1) · tags UNESCO:TECH-U, AI4K12:2 |
| Time | 15 minutes, at home or in Compass (optional) |
| Materials | A free, browser-based tokenizer page (current links in Compass); a paragraph in two languages you know, or the provided translations |

## Steps (tool-neutral)
1. Paste a full paragraph in a language you know other than English (this extends the section 3.1 Your Turn, which used one sentence). Record the token count, the tokenizer's name and the date.
2. Paste its English translation. Record the token count.
3. Divide the first count by the second. Compare your ratio with figure F3.2 (section 3.1).
4. If the page offers a second tokenizer, repeat steps 1–3 and compare.
5. Look at how one long or rare word is split. Then type the same word at the start of the box and after a space, and write down both splits (the pieces can differ).

[COMPASS: ch03-lab2 — tokenizer pages; interactive token explorer]

## Expected observations (instructor notes)
Many languages need more tokens than English for the same sentence; the ratio depends on the tokenizer, and newer tokenizers usually narrow the gap (book measurement: data/ch03_tokens.csv). Short sentences give noisy ratios; a paragraph gives a steadier one. The same word can split differently at the start of a text and after a space (book data: data/ch03_token_pieces.csv).

## Debrief (3–5)
1. What was your ratio, and how does it compare with figure F3.2? (compare)
2. Why might a short sentence give a different ratio from a full document? (explain)
3. What would the ratio mean for cost or for how much text fits in one turn? (apply)

## Deliverable and rubric
Ungraded. Two token counts, the tokenizer name and date, and two sentences of interpretation.

## Accessibility and alternatives
Provided translations on eLearning for students who use only English. A pre-computed table (data/ch03_tokens.csv) for students without access to a tokenizer page; screen-reader friendly.

## Safety and privacy
Paste only public or invented sentences.

## Instructor notes
Book reference values (UDHR, tiktoken 0.8.0): Turkish 1.48× (o200k_base) and 1.98× (cl100k_base); Tamil 2.52× and 9.56×; Spanish 1.23× and 1.48×.
