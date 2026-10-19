// Project override of Quarto's orange-book typst-show partial.
// Adds: the designed front cover as page 1 (screen PDF only), US Letter paper, the book's
// palette, a copyright block and a chapter-level table of contents.
// Print edition (quarto render --profile print): no cover page, grayscale theme, and no
// element at the page edge, so the interior needs no bleed (IngramSpark, decision D29).

#import "@preview/orange-book:0.7.1": book, part, chapter, appendices

$if(print-edition)$
#let print-edition = true
$else$
#let print-edition = false
// Page 1: the designed cover (cover/cover-front.svg, built by figures/scripts/cover.py).
#page(paper: "us-letter", margin: 0pt, header: none, footer: none, numbering: none)[
  #image("/cover/cover-front.svg", width: 100%, height: 100%, fit: "cover")
]
$endif$
// Grayscale for print, unchanged for screen.
#let ink(c) = if print-edition and type(c) == color { luma(c) } else { c }

// Fonts (design option A, docs/design-options.md; colophon): Source Serif 4 body, Source Sans 3
// headings, JetBrains Mono code. STIX (SIL OFL) covers symbols the main fonts lack (check marks,
// arrows, set signs), so no system font is embedded as a fallback.
#let body-fonts = ("Source Serif 4", "STIX Two Text", "STIXGeneral")
#let heading-fonts = ("Source Sans 3", "STIXGeneral")
#let code-fonts = ("JetBrains Mono", "DejaVu Sans Mono", "STIXGeneral")
#set text(font: body-fonts)

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
  main-color: ink(rgb("#1C3D6E")),
$if(print-edition)$
  heading-style: 1,
  cover-background: none,
$endif$
$if(print-edition)$
  // Print (D29): 10 pt and narrower margins keep the paperback within IngramSpark's page limit;
  // the gutter stays above Ingram's 0.875" minimum for thick books; footer stays >= 0.5" from trim.
  font-size: 10pt,
  margin: (inside: 2.3cm, outside: 2cm, top: 2.5cm, bottom: 2.5cm),
$else$
  font-size: 10.5pt,
$endif$
  first-line-indent: false,
  outline-depth: 1,
  outline-small-depth: 1,
  copyright: [
    *AI for All: Career-Ready AI Skills* \
    Sadi Evren Seker \
    First edition, 2027 (edition 2027.1). Copyright © 2027 Sadi Evren Seker.

    Licensed under Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0): https://creativecommons.org/licenses/by-nc-sa/4.0/

    Publisher: [to be added]. \
    ISBN (paperback): [to be added]. ISBN (EPUB): [to be added].
  ],
$if(quarto.language.crossref-ch-prefix)$
  supplement-chapter: "$quarto.language.crossref-ch-prefix$",
$endif$
)

#set text(font: body-fonts)
#show heading: set text(font: heading-fonts)
#show raw: set text(font: code-fonts)

// Body paragraphs: no first-line indent, so give paragraphs visible spacing.
#set par(spacing: 0.95em, leading: 0.62em)

// Callouts (worked examples, Your Turn, Check Yourself) may break across pages.
// Quarto's default callout is breakable: false, so a box taller than the space left
// on a page overflowed into the footer. Same look; the title stays with the body.
#let callout(body: [], title: "Callout", background_color: rgb("#dddddd"), icon: none, icon_color: black, body_background_color: white) = {
  block(
    breakable: true,
    fill: ink(background_color),
    stroke: (paint: ink(icon_color), thickness: 0.5pt, cap: "round"),
    width: 100%,
    radius: 2pt,
    block(
      inset: 1pt,
      width: 100%,
      below: 0pt,
      sticky: true,
      block(
        fill: ink(background_color),
        width: 100%,
        inset: 8pt)[#if icon != none [#text(ink(icon_color), weight: 900)[#icon] ]#title]) +
      if (body != []) {
        block(
          inset: 1pt,
          width: 100%,
          block(fill: ink(body_background_color), width: 100%, inset: 8pt, body))
      }
  )
}

$if(print-edition)$
// Print edition: part pages without the full-page tinted background (it touched the trim
// edge). Same layout as orange-book's part-style 0 otherwise.
#import "@preview/orange-book:0.7.1": part-change, part-state, part-counter, part-location, main-color-state, part-font-size-state, outline-small-depth-state, outline-small-width-state, appendix-state, my-outline-small, large-text, outline-part, outline-heading1, outline-heading2, outline-heading3
#let part(title) = {
  pagebreak(to: "odd")
  part-change.update(x => true)
  part-state.update(x => title)
  part-counter.step()
  [
    #context{
      let her = here()
      part-location.update(x => her)
    }
    #context{
      let main-color = main-color-state.at(here())
      let part-font-size = part-font-size-state.at(here())
      let outline-small-depth = outline-small-depth-state.at(here())
      let outline-small-width = outline-small-width-state.at(here())
      set par(justify: false)
      place(top+right, text(fill: black, size: large-text, weight: "bold", box(width: 60%, part-state.get())))
      place(top+left, text(fill: main-color, size: part-font-size, weight: "bold", part-counter.display("I")))
      align(bottom+right, my-outline-small(title, appendix-state, part-state, part-location, part-change, part-counter, main-color, textSize1: outline-part, textSize2: outline-heading1, textSize3: outline-heading2, textSize4: outline-heading3, depth: outline-small-depth, width: outline-small-width))
    }
  ]
}
$endif$
