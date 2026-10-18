// Project override of Quarto's orange-book typst-show partial.
// Adds: the designed front cover as page 1, US Letter paper, the book's
// palette, a copyright block and a chapter-level table of contents.
// Placeholder values (paper, font size) change when docs/design-system.md is written.

#import "@preview/orange-book:0.7.1": book, part, chapter, appendices

// Page 1: the designed cover (cover/cover-front.svg, built by figures/scripts/cover.py).
#page(paper: "us-letter", margin: 0pt, header: none, footer: none, numbering: none)[
  #image("/cover/cover-front.svg", width: 100%, height: 100%, fit: "cover")
]

#show: book.with(
$if(title)$
  title: [$title$],
$endif$
$if(subtitle)$
  subtitle: [$subtitle$],
$endif$
$if(by-author)$
  author: "$for(by-author)$$it.name.literal$$sep$, $endfor$",
$endif$
$if(date)$
  date: "$date$",
$endif$
$if(lang)$
  lang: "$lang$",
$endif$
  paper-size: "us-letter",
  main-color: rgb("#1C3D6E"),
  font-size: 10.5pt,
  first-line-indent: false,
  outline-depth: 1,
  copyright: [
    *AI for All: Career-Ready AI Skills* \
    Şadi Evren Şeker \
    Edition 2027.1 (working draft, #datetime.today().display("[month repr:long] [day], [year]")) — not for distribution.

    Licensed under Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0).

    This is a production draft. Chapters marked as awaiting the author's voice edit are not final.
  ],
$if(quarto.language.crossref-ch-prefix)$
  supplement-chapter: "$quarto.language.crossref-ch-prefix$",
$endif$
)

// Body paragraphs: no first-line indent, so give paragraphs visible spacing.
#set par(spacing: 0.95em, leading: 0.62em)
