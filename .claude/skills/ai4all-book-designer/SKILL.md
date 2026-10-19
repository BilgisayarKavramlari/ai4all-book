---
name: ai4all-book-designer
description: Creates and applies the AI for All design system - trim size, page grid, typography, callout boxes, tables and chapter openers - for print PDF and EPUB.
---

# AI for All — book designer

Goal: one design system, two outputs — a print interior PDF (grayscale, for the IngramSpark paperback; decision D29) and a reflowable EPUB 3 (color).

## Step 1 — decisions for the author (do not decide alone)
Present a table with options, trade-offs and an estimated page count for each:
- Trim size: D2D Print offers 5×8, 5.25×8.5, 5.5×8.5, 6×9, 7.5×9.25, 8.5×11 in. For a figure-heavy textbook the realistic candidates are 7.5×9.25 and 8.5×11. Estimate pages from the current word count and figure count.
- Volumes: one or two volumes, given D2D's page limits (check the current limit at upload; sources differ — FAQ 32–1,050 pages, an older post 64–740).
- Fonts: open-licensed (SIL OFL) families only, embedded in the PDF and EPUB. Suggested set: Source Serif 4 (body), Source Sans 3 (headings, callouts, figures), JetBrains Mono (prompts and code).
- Callout styling for recurring elements: Check Yourself, Warm-up, Worked Example, Your Turn, Ethics Lens, Career Connection, From the Field, Key Terms, Compass link, Deep/Studio markers. Each must be distinguishable in grayscale (icon + border style + label), not by color.

## Step 2 — write docs/design-system.md
Page grid (margins with larger gutter, text block width, columns or side margin for notes), baseline and type scale, heading levels, running heads and folios, chapter opener, part opener, table style, figure placement and caption style, list styles, prompt/code block style, callout specs, color palette with grayscale equivalents, EPUB CSS equivalents, accessibility (reading order, real text not images of text, contrast ≥ 4.5:1 in EPUB).

## Step 3 — implement
- Quarto with Typst for the print PDF (template in _extensions/ai4all/ or templates/), CSS for EPUB.
- Build a 6–8 page **sample spread** (chapter opener, body text, every callout type, a table, two figures, end-of-chapter page) as PDF and EPUB, and show it to the author before applying the design to all chapters.

## Step 4 — maintain
Every new element type gets a spec in docs/design-system.md before it is used. Never style one-off elements by hand.
