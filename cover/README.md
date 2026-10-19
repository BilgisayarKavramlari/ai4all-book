# Cover: *AI for All: Career-Ready AI Skills*

## Concept
- The artwork is the book's first signature diagram, the AI Work Loop (Frame, Prompt, Verify, Decide, Disclose), drawn in the book's shape grammar on a navy field.
- The four human steps are outlined rounded squares. **Decide** is the only solid shape: a large white diamond with a dotted halo.
- The AI tool is a yellow hexagon in a darker inner disc. It reaches the loop only through dotted lines to Prompt and Verify, which says that AI output stays uncertain until a person checks it.
- Message: people decide, AI assists. There are no robots, brains, circuits or photos, and the meaning comes from shape and solid versus outline, not hue.
- Readers meet the same drawing again in Chapter 1 (f1-02) and at every chapter opening, so the cover is part of the book's visual language, not decoration.

## Files
| File | What it is |
|---|---|
| `cover-front.svg` | Print/PDF front cover, 8.5 × 11 in, 612 × 792 pt viewBox, full bleed, color |
| `cover-front-gray.svg` | The same layout in grayscale (print interior or title page) |
| `cover-epub.svg` | EPUB cover, 1600 × 2560 px (1 : 1.6), re-laid out for the taller page |
| `alt-1.svg` … `alt-3.svg` (+ `-gray`) | The three compositions studied; alt-1 was chosen |

## Colors (palette F, docs/decisions.md G4)
Color: navy (human) `#1C3D6E` · inner disc `#14304F` · AI yellow `#FCE38A` · white `#FFFFFF` · secondary text `#B9C6DA`.
Gray: field `#2B2B2B` · disc `#1E1E1E` · AI hexagon `#E6E6E6` with a black outline · white `#FFFFFF` · secondary `#C4C4C4`.

## Fonts (decision G2; installed and SIL OFL)
Title: Source Serif 4 Bold (opsz 60). Subtitle, author, labels: Source Sans 3 SemiBold/Bold. The text stays live SVG text with fallbacks (Source Serif Pro/Georgia; Source Sans Pro/Helvetica Neue/Arial). Before final print, convert the text to outlines or embed the fonts in the PDF.

## Why alt-1
- **alt-1 "The Loop" (chosen):** it reuses a diagram readers will learn, and the human decision is the clear focal point. It also holds up best at thumbnail size: the title reads at 100 px wide, and the shapes read in grayscale.
- **alt-2 "Many drafts, one decision":** AI hexagons converge on a navy diamond. The idea is clear, but the many thin lines look busy, the lower third is empty, and the light hexagons lose contrast when small.
- **alt-3 "Pattern":** a grid of faint shapes with one lit loop. It is strong as a graphic, but the square loop on a grid looks like a circuit board, which is the cliche this cover avoids.

## Regenerate
```
python3 figures/scripts/cover.py      # from the repo root; standard library only
```
Layout values are in `LAYOUT_LOOP` (print and EPUB). Text sits at least 0.5 in from the trim edge; the small step labels sit at least 0.65 in from it. Trim size is not final, so if it changes, add a new layout entry instead of scaling. The title, the subtitle prominence (decision D2) and the USPTO check are still open; nothing here is final until the author approves the cover.
