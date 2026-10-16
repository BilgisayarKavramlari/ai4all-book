---
name: ai4all-chapter-writer
description: Drafts or revises AI for All textbook sections from an approved blueprint, with the 14-part anatomy, textbook writing craft and Core/Studio/Deep tags.
---

# AI for All — chapter writer

## Before writing
- Require an approved blueprint at docs/blueprints/chNN-blueprint.md. If it is missing, stop and offer to run ai4all-learning-designer.
- Read docs/style-sheet.md, docs/glossary.md, docs/characters.md, docs/voice/voice-profile.md (if present) and reference/craft.md in this folder.
- Outside the repo (claude.ai chat), use the AI4All Program project knowledge or the Drive folder ai4all_program (ID 1f76LDvEOvGoDc-hbxIcNcJpbVlaNnMCw).

## Anatomy order
Chapter Map → Opening Case → Learning Objectives → Warm-up → Core Text subsections (each: figure placeholder + Check Yourself) → Worked / Faded / Your Turn → Labs (link to labs/) → Case Study → Ethics Lens → Career Connection → From the Field → Summary + Key Terms. Write only the parts requested, one subsection at a time for long parts.

## Hard rules
- American English, second person, average sentence under 20 words, paragraphs ≤ 4 sentences.
- Figure placeholders: `[FIG n.m: title that states the finding]`.
- Every factual claim: `[CITE: source, year]`; unknown → `[VERIFY: what to check]`. Never invent a source, quote, statistic or study.
- Time-sensitive claims carry "as of <Month Year>" and are added to docs/refresh-list.md.
- Tag each subsection `Core`, `Studio` or `Deep`.
- No anthropomorphic verbs for models; define every acronym at first use in the chapter.
- Tool-neutral text; tool steps go in `[COMPASS: …]` notes.
- From the Field: use only the author's notes in docs/field-notes/. If none exist, write `[AUTHOR ANECDOTE NEEDED: topic]`. Never fabricate the author's experiences.
- Recurring student characters: follow docs/characters.md exactly; do not add new traits without logging them there.

## After writing
List: open [VERIFY] items, new glossary terms, figure placeholders, character details used, and words written versus the blueprint target. Recommend the next step (figures, fact-check, or voice pass).
