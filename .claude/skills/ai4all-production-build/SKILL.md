---
name: ai4all-production-build
description: Builds the AI for All print PDF and EPUB with Quarto, runs EPUBCheck, accessibility and PDF preflight checks, and writes a build report.
---

# AI for All — production build

## Build
1. `quarto render` for each target (print PDF via Typst, EPUB 3; per volume if the book is split).
2. Print uses figures/out/gray/; EPUB uses figures/out/color/.

## Checks (all must pass before a file goes to Draft2Digital)
EPUB
- `epubcheck <file>.epub` → 0 errors (warnings listed in the report).
- `ace <file>.epub -o build/ace-report` (Ace by DAISY) → no serious or critical accessibility violations.
- Every image has alt text; document language set; navigation (TOC, landmarks) present; file under 100 MB.

Print PDF
- Page size equals the chosen trim size; margins match docs/design-system.md.
- `pdffonts` → every font embedded.
- Images grayscale and at least 300 dpi effective at final size (`pdfimages -list`).
- Page count within the current D2D Print limits (verify on D2D at upload time).
- No text outside the safe area; no blank pages except intended ones; running heads and folios correct.
- Visual spot check: render 10 random pages to PNG and look at them.

Content
- No remaining [VERIFY], [CITE], [AQ], [AUTHOR ANECDOTE NEEDED] or [FIG …] markers (grep). List any found and stop.
- Every cross-reference resolves; glossary terms consistent.

## Output
build/report-YYYY-MM-DD.md: file names, sizes, page counts, check results (pass/fail), list of problems with locations. Summarize for the author in Turkish.
