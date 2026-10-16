---
name: ai4all-chapter-pipeline
description: Runs the full production pipeline for one AI for All chapter, from blueprint to final review, with author checkpoints. Use as /ai4all-chapter-pipeline <chapter-number>.
disable-model-invocation: true
argument-hint: [chapter-number]
---

# Chapter pipeline for chapter $ARGUMENTS

Track progress in docs/status.md (one row per chapter: stage, date, open items). Stop at every AUTHOR CHECKPOINT and wait.

1. **Blueprint** — ai4all-learning-designer → docs/blueprints/. **AUTHOR CHECKPOINT: approve blueprint.**
2. **Draft** — ai4all-chapter-writer, one subsection at a time, Core path first, then Studio and Deep.
3. **Build-outs** — ai4all-diagram-maker for each [FIG], ai4all-lab-designer for the labs, ai4all-case-builder for the opening and main cases, ai4all-assessment-builder for the end-of-chapter package.
4. **Independent checks (subagents, run in parallel)** — fact-checker, subject-expert-reviewer, pedagogy-reviewer, student-reader panel. They must not see each other's reports.
5. **Developmental memo** — ai4all-developmental-editor, merging the subagent findings. **AUTHOR CHECKPOINT: choose which changes to make.**
6. **Revise** — apply the chosen changes; re-run the fact-checker on changed passages.
7. **Copyedit** — ai4all-copyeditor; apply approved mechanical changes.
8. **Voice pass** — ai4all-author-voice Mode B. **AUTHOR CHECKPOINT: author's own voice edit.**
9. **Final review** — ai4all-reviewer; no "must fix" items may remain.
10. **Housekeeping** — update docs/glossary.md, docs/refresh-list.md, docs/ai-use-log.md, figures/index.csv, cases/index.csv; commit with message "Chapter $ARGUMENTS: <stage>".

Report at each checkpoint, in Turkish: what was done, open items, word count against target, and the decision needed.
