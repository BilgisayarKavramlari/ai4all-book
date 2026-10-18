# Front matter — figure captions, alt text and long descriptions

Print uses figures/out/gray/<id>.svg; EPUB and web use figures/out/color/<id>.svg. Source: figures/scripts/front_figures.py (imports figures/scripts/figlib.py). Used in front/visual-guide.qmd ("A Visual Guide to This Book").

| Source ID | File id | Caption (≤ 25 words) | Alt text (≤ 150 characters) |
|---|---|---|---|
| F0.1 | f0-01-legend | Shape tells you who or what acts; line and fill tell you how sure, how risky and where to look. | Legend. Shapes: rectangle step, rounded box person, hexagon AI, diamond decision. Dashed inferred, thick risk, filled verified or highlighted. |

## Long descriptions (complex figures)

**F0.1 — Legend of the book's diagram language.** Two columns separated by a thin vertical line, each with four rows; every row shows one sample box on the left and its meaning on the right. Left column, headed "Shape: who or what acts": a plain rectangle labeled "Step" (a step or stage in a process); a rectangle with rounded corners labeled "Person" (a person acts or decides); a six-sided hexagon labeled "AI tool", filled light yellow in color and very light gray in print (an AI component produces something); a diamond labeled "Choice?" (a decision point with more than one way out). Right column, headed "Line and fill: how sure, how risky": a rectangle with a dashed outline labeled "Inferred" (inferred, this book's reading; never anything else); a rectangle with a thick border labeled "Risk", filled orange in color and hatched with fine diagonal lines in print (a risk or warning); a rectangle labeled "Checked", filled green in color and mid-gray in print (verified information, always labeled); a rectangle with a dark fill, thick border and white text labeled "This step" (the part this figure is about). Below both columns, a solid arrow pointing right, explained as "what comes next, or what feeds what." A closing line in italics: every meaning is carried by shape, line or label, so it survives the gray print edition.
