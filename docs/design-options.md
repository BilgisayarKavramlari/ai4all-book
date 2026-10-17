# Design options (step 1 of ai4all-book-designer) — for the author's decision

Status: decided 2026-10-16 — the author approved the proposals (O3 trim in two volumes, font set A, callout family R, palette F); see docs/decisions.md G1–G4. Next: docs/design-system.md (step 2).

## 1. Trim size and page estimate

Assumptions: 250,000 words (the stated minimum) and about 450 figures; callouts, tables and end-of-chapter formatting add 12% to text pages; fixed pages = 23 chapter openers × 2 + 6 part openers × 2 + 30 front matter + 70 back matter (glossary, answers, case index, index) = 158. Words per full text page assume 10.5–11 pt Source Serif 4 on ~14 pt leading. These are planning estimates, ±15%; a real count comes from the sample spread.

| Option | Layout | Words / text page | Figure area (avg page per figure) | Pages at 250k words | Per volume if 2 | Pages at 350k words |
|---|---|---|---|---|---|---|
| O1 · 7.5 × 9.25 in | Single column, no side margin | ~520 | 0.45 | ~900 | ~450 | ~1,195 |
| O2 · 7.5 × 9.25 in | Single column + narrow side margin for icons and key terms | ~430 | 0.45 | ~1,010 | ~505 | ~1,355 |
| **O3 · 8.5 × 11 in** | Text column + wide side margin (classic textbook) | ~560 | 0.35 | **~815** | **~410** | ~1,080 |
| O4 · 8.5 × 11 in | Two columns | ~750 | 0.30 | ~665 | ~335 | ~870 |
| (reference) 6 × 9 in | Single column | ~400 | 0.55 | ~1,105 | ~555 | ~1,485 |

D2D page limit: sources disagree (FAQ 32–1,050 pages; an older post 64–740). Plan for the conservative 740 per volume and check at upload.

**Proposal: O3 in two volumes.** The wide side margin carries key-term definitions, Compass links/QR codes and Core/Studio/Deep markers without interrupting the text, and wide figures can extend into it. Two volumes stay near 410 pages each at 250k words and near 540 at 350k words, safely under even the conservative limit. Trade-offs: 8.5 × 11 is heavier and costs more per copy than 7.5 × 9.25; two columns (O4) save pages but break up diagrams and are harder to keep accessible. In EPUB the side margin becomes inline asides.

## 2. Volumes

| Option | Content | Pages (O3) | Note |
|---|---|---|---|
| One volume | Whole book | ~815 | Over the conservative 740 limit; no room to grow |
| **Two volumes** | Vol. 1 = Parts I–II (Ch. 1–10, to the midterm); Vol. 2 = Parts III–VI (Ch. 11–23) | ~410 + ~410 | Matches the two halves of the term; each half needs its own ISBN |
| Three volumes | Parts I–II · III–IV · V–VI | ~270 each | Only if the book grows well past 350k words |

## 3. Fonts (SIL Open Font License only, embedded in PDF and EPUB)

| Option | Body | Headings, callouts, figures | Prompts and code | Note |
|---|---|---|---|---|
| **A** | Source Serif 4 | Source Sans 3 | JetBrains Mono | Already installed; optical sizes; full Turkish glyphs (needed for the later Turkish edition); one design family |
| B | Literata | Inter | JetBrains Mono | Literata is tuned for e-reading; Inter is very legible in figures |
| C | Charis SIL | Fira Sans | Fira Mono | Very sturdy in low-resolution print; less modern look |

Proposal: A.

## 4. Callout styles (must be distinguishable in grayscale: icon + border style + label, never color)

Three style families:

| Family | How elements differ | Ink / print risk | Proposal |
|---|---|---|---|
| **R · Rules** | Border and line style (solid, dashed, dotted, thick left rule, double rule, top-and-bottom rules) + icon + label | Low ink; very clear in grayscale | **Proposed** |
| P · Panels | Gray tints (5–20%) + icon + label | Heavier ink; tints can look muddy in print-on-demand | |
| T · Tabs | Identical boxes; only the icon and label tab differ | Simplest; weakest at a glance | |

Element spec under family R (icons from an open icon set such as Lucide or Material Symbols, license to be confirmed):

| Element | Icon | Border / fill | Label |
|---|---|---|---|
| Warm-up | spark | Dotted full box, white | WARM-UP |
| Check Yourself | question mark in circle | 1 pt solid full box, white | CHECK YOURSELF |
| Worked Example | numbered list | 10% gray fill, no border | WORKED EXAMPLE |
| Faded Example | half-filled list | 10% gray fill + dashed outline | FADED EXAMPLE |
| Your Turn | pencil | Dashed full box, white | YOUR TURN |
| Ethics Lens | scales | 3 pt black left rule | ETHICS LENS |
| Career Connection | briefcase | 1 pt rules top and bottom only | CAREER CONNECTION |
| From the Field | map pin | Double left rule | FROM THE FIELD |
| Key Term | key | Side margin, 5% fill | KEY TERM |
| Compass link | compass rose + QR | Side margin, rounded outline | COMPASS |
| Prompt | terminal | JetBrains Mono, 5% fill, 0.5 pt border, header strip "PROMPT · model · date" | PROMPT |
| Deep / Studio markers | — | Margin tab: solid black = DEEP; outlined = STUDIO; Core unmarked | DEEP / STUDIO |

## 5. Grayscale legibility (measured)

D2D Print interiors are black and white, so every color must survive conversion. Measured with CIE L* lightness (sRGB, D65) and WCAG contrast; a lightness difference ΔL* ≥ 20 is the working threshold for two gray tones to read as clearly different.

| Palette (human · AI · risk · verified) | Gray lightness L* | Smallest ΔL* between roles | Result |
|---|---|---|---|
| Okabe–Ito (#0072B2 · #E69F00 · #D55E00 · #009E73) | 46 · 71 · 54 · 58 | 3.6 (risk vs. verified) | Fails: three roles become nearly the same gray |
| Lightness-spaced B (#1B4F8A · #F0B429 · #B3261E · #7FC8A9) | 33 · 77 · 40 · 75 | 1.6 (AI vs. verified) | Fails |
| **Four-step F (#1C3D6E · #FCE38A · #C2410C · #4CAF84)** | 26 · 91 · 46 · 65 | 18.8 | Best found; still just under 20 |

Gray fills for callouts (5–25%) all keep black body text far above the 4.5:1 minimum (11.4:1 at 25%, 18.8:1 at 5%).

Conclusions:

1. Even a palette tuned for lightness gives only about three reliably distinct gray levels. Color can support meaning in the EPUB but cannot carry it in print. The shape grammar (rectangle, diamond, rounded box, hexagon, dashed outline) and line styles must do the work. This is already a rule in docs/visual-guide.md; the measurement shows it is not optional.
2. Use palette F (or a refinement) for EPUB. Light fills (AI, L* 91) need a dark outline on white paper. Text on fills: white on human and risk, black on AI and verified (all above 4.5:1).
3. Render the gray version of every figure ourselves (figures/out/gray/) rather than relying on D2D's automatic conversion, and check each one.

## 6. What the author decides here

Trim (O1–O4), volumes, font set (A–C), callout family (R, P, T), and whether palette F is acceptable as the starting point.
