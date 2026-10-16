---
name: ai4all-diagram-maker
description: Turns AI for All figure placeholders into Mermaid or SVG sources and renders color (EPUB/web) and grayscale (print) versions with caption and alt text.
---

# AI for All — diagram maker

The print edition (Draft2Digital Print) has black-and-white interiors. Every figure therefore ships in two renders: color for EPUB and web, grayscale for print. Design for grayscale first.

## Inputs
docs/visual-guide.md and docs/design-system.md (palette, shape grammar, fonts, sizes), the chapter text around `[FIG n.m: …]`.

## Design rules
- At most 9 boxes; the title states the finding.
- Meaning is carried by shape, line style (solid/dashed/dotted), pattern, labels and position — never by color alone.
- Color palette must keep distinct luminance steps so the grayscale render stays readable (check contrast between adjacent fills).
- Minimum text size at final print size: 8 pt; same font family as the book's sans-serif.
- Width fits the text block of the chosen trim size; full-page figures only when unavoidable.
- Signature diagrams reuse masters in figures/src/signature/; change only the highlighted step.
- Data charts are generated from data/*.csv by script (Python/matplotlib or Vega-Lite), never drawn by hand.
- No generated images for diagrams or anything meant to depict real people, products or logos.

## Steps
1. Choose the type: concept map, process, architecture, decision tree, 2×2, timeline, data chart, storyboard.
2. Write the source: figures/src/chNN-fig-m.mmd (Mermaid), .svg, or a script in figures/scripts/.
3. Render: `mmdc` (mermaid-cli) or the script → figures/out/color/ (SVG + PNG) and figures/out/gray/ (vector PDF or SVG; PNG fallback at 300 dpi or more at final size).
4. View both renders yourself (open the PNG). Fix overlaps, clipped labels and low-contrast fills.
5. Write caption (≤25 words), alt text (≤150 characters) and, for complex figures, a long description in figures/longdesc/.
6. Replace the placeholder in the chapter with the figure include, caption and alt text; log the figure in figures/index.csv (id, chapter, title, type, source, status).
