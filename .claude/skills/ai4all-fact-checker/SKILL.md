---
name: ai4all-fact-checker
description: Extracts every checkable claim from an AI for All chapter, verifies each against primary sources and records verdicts and corrections in a fact-check log.
---

# AI for All — fact-checker

## Steps
1. Extract every checkable claim: numbers, dates, names, quotations, study results, legal outcomes, product capabilities, attributions. Include claims already marked [CITE] and [VERIFY].
2. For each claim, find the primary source (paper, court record, official statement, dataset, standard). Open it. Secondary sources only point the way.
3. Verdict: supported / partially supported / unsupported / outdated / cannot verify.
4. For anything not fully supported, propose a corrected wording that the source does support.
5. Product and model capabilities change fast: mark them time-sensitive, add "as of <Month Year>", and add them to docs/refresh-list.md.
6. Legal cases and named people or organizations: state only what the record shows; check the latest status (appeals, settlements).

## Output
Append rows to docs/factcheck/chNN.csv with columns: id, location, claim, type, source_url, source_type (primary/secondary), verdict, correction, checked_on. Then give the author a summary (in Turkish): counts per verdict and every "unsupported" item.

Never mark a claim supported without having read the source.
