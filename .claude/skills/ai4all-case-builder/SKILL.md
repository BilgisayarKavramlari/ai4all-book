---
name: ai4all-case-builder
description: Researches and writes a cited real-world case for the AI for All textbook with at least two independent sources, one of them primary.
---

# AI for All — case builder

## Steps
1. Search for the incident or study. Open every page you cite. Prefer court decisions, peer-reviewed papers, official statements and regulator reports. The AI Incident Database is a starting point, not a final source.
2. Fill cases/TEMPLATE.md: Context, Timeline, What the AI did, What humans did, Failure label, Consequences (documented only), A better workflow (AI Work Loop), 4–6 Questions, Sources with access dates.
3. Paraphrase. At most one quotation under 15 words per source.
4. State only documented facts about named people and organizations. No speculation about motives.
5. Balance: keep at least one third of the case library positive or mixed in outcome; say which this case is.
6. Add or update the row in cases/index.csv (id, title, year, chapter, field, failure_type, outcome, primary_source_url, secondary_source_url, verified_on).

## Output
The case file in cases/, the index row, and a one-line note on anything you could not verify.
