// Full paperback cover (back + spine + front) on IngramSpark's cover template.
// Template: 9798182962292-Perfect.pdf (Black & White, 50 lb White, Matte, 8.5 x 11 in, 1114 pages).
// Geometry measured from the template (points, origin top-left):
//   page 1512 x 864; bleed artwork x 112.5-1511.6, y 0-810 (19.432 x 11.25 in)
//   trim: back x 121.5-733.5, spine x 733.5-890.6 (2.182 in), front x 890.6-1502.6; y 9-801
//   Ingram's barcode (kept, vector, clipped from the template): about x 585-675, y 705-778
// Build: tools/make-print-cover.sh (Typst -> CMYK PDF/X-1a with Ghostscript). Text is ASCII (D28).

#let navy = rgb("#1C3D6E")
#let navy-deep = rgb("#14304F")
#let gold = rgb("#FCE38A")
#let soft = rgb("#B9C6DA")
#let white = rgb("#FFFFFF")
#let serif = ("Source Serif 4", "STIXGeneral")
#let sans = ("Source Sans 3", "STIXGeneral")

#set page(width: 1512pt, height: 864pt, margin: 0pt)
#set text(font: sans, fill: white, lang: "en")
#set par(justify: false)

// 1. The template is NOT embedded here (Typst would wrap it in a transparency group, which makes
//    Ghostscript rasterize the page). tools/make-print-cover.sh adds it underneath with qpdf after the
//    PDF/X conversion, so its marks and labels outside the artwork stay unaltered.

// 2. Background over the whole bleed area (covers every pink and blue box).
#place(top + left, dx: 112.5pt, dy: 0pt, rect(width: 1399.1pt, height: 810pt, fill: navy, stroke: none))
// Slightly deeper spine band, with 1 pt inside each fold so a small fold shift does not show.
#place(top + left, dx: 734.5pt, dy: 0pt, rect(width: 155.1pt, height: 810pt, fill: navy-deep, stroke: none))

// 3. Front cover: the book's designed cover at trim size (its own background is navy, so the bleed matches).
#place(top + left, dx: 890.6pt, dy: 9pt, image("front.svg", width: 612pt, height: 792pt))

// 4. Spine: reads top to bottom (rotated 90 degrees clockwise), kept inside the safe area.
#place(top + left, dx: 733.5pt, dy: 9pt,
  box(width: 157.1pt, height: 792pt,
    align(center + horizon,
      rotate(90deg, reflow: true,
        box(width: 732pt, height: 140pt,
          grid(columns: (auto, 1fr, auto, 1fr, auto), align: horizon, column-gutter: 0pt,
            [#text(font: serif, size: 40pt, weight: "bold")[AI for All]],
            [],
            [#text(size: 17pt, fill: soft)[Career-Ready AI Skills] #h(22pt) #text(size: 19pt, weight: "semibold")[Sadi Evren Seker]],
            [],
            [#text(size: 13pt, fill: gold, weight: "semibold", tracking: 1.5pt)[OPTIWISDOM]],
          )
        )
      )
    )
  )
)

// 5. Back cover text, inside the safe area (trim x 121.5-733.5; text block 52 pt in from the trim).
#place(top + left, dx: 173.5pt, dy: 72pt,
  block(width: 508pt)[
    #text(size: 11.5pt, fill: gold, weight: "semibold", tracking: 1.8pt)[ARTIFICIAL INTELLIGENCE · CAREERS · AI LITERACY]
    #v(18pt)
    #text(font: serif, size: 36pt, weight: "bold")[Use AI well, \ at school and at work.]
    #v(16pt)
    #set par(leading: 0.66em, spacing: 1.05em)
    #text(size: 14.5pt)[AI tools now draft, summarize, analyze and recommend alongside us. *AI for All* shows students in every major, and working professionals, how to use them well: when to trust an output, how to check it, when a decision must stay with a person, and how to show an employer what you did.]

    #text(size: 14.5pt)[The book is built around one method, the AI Work Loop: *Frame* the task, *Prompt* the tool, *Verify* the output, *Decide* as a person, and *Disclose* your use. Its 23 chapters run from how machine learning and large language models work, and why they fail, to verification, writing, data and decisions, agents, privacy and security, bias, law, and field guides for using AI across disciplines.]
    #v(10pt)
    #text(size: 15pt, weight: "semibold", fill: gold)[Inside]
    #v(2pt)
    #set list(marker: text(fill: gold)[•], indent: 2pt, body-indent: 8pt, spacing: 0.7em)
    #text(size: 14pt)[
      - 75 hands-on labs that work with free tools, many with a no-device route
      - 31 real cases built from documented, dated sources
      - Worked, faded and Your Turn examples in every chapter
      - 14 portfolio assignments that add up to evidence for employers
      - A 464-term glossary, a practice exam and model answers
    ]
    #v(18pt)
    #line(length: 508pt, stroke: 0.6pt + soft)
    #v(12pt)
    #text(size: 12.5pt, fill: soft)[*Sadi Evren Seker* has worked in information technology since 1997 and teaches artificial intelligence and computer science at the university level. He has lived and worked in six countries as an academic, expert and consultant, and is a founder of OptiWisdom.]
  ]
)

// Publisher line, bottom left of the back cover.
#place(top + left, dx: 173.5pt, dy: 742pt,
  block(width: 300pt)[
    #text(size: 12pt, fill: gold, weight: "semibold", tracking: 1.5pt)[OPTIWISDOM] \
    #text(size: 9.5pt, fill: soft)[OptiWisdom LLC · optiwisdom.com]
  ]
)

// 6. EAN-13 barcode for ISBN 979-8-1829-6229-2, drawn as vector bars in 100% black (K only).
//    Module 0.7472 pt (80%), bars x 595.42-666.40 pt, top 714 pt: the same geometry as Ingram's
//    template barcode; the bar pattern was checked module by module against it (95 of 95 match).
#let k100 = cmyk(0%, 0%, 0%, 100%)
#let paper = cmyk(0%, 0%, 0%, 0%)
#let ean = "10101110110010111000100100110010001001001001101010111010010100001101100110110011101001101100101"
#let bx = 595.42pt
#let mw = 0.7472pt
#let guards = (0, 1, 2, 45, 46, 47, 48, 49, 92, 93, 94)
#place(top + left, dx: 579pt, dy: 699pt, rect(width: 102pt, height: 84pt, fill: paper, stroke: none))
#for (i, m) in ean.clusters().enumerate() {
  if m == "1" {
    let h = if guards.contains(i) { 58.5pt } else { 54.2pt }
    place(top + left, dx: bx + mw * i, dy: 714pt, rect(width: mw, height: h, fill: k100, stroke: none))
  }
}
#let digits(x, s) = place(top + left, dx: x, dy: 768.8pt, box(width: mw * 42, align(center, text(font: sans, size: 8pt, fill: k100, tracking: 0.55pt, s))))
#place(top + left, dx: 588.4pt, dy: 768.8pt, text(font: sans, size: 8pt, fill: k100, "9"))
#digits(bx + mw * 3, "798182")
#digits(bx + mw * 50, "962292")
#place(top + left, dx: 583pt, dy: 704.2pt, box(width: 94pt, align(center, text(font: sans, size: 7.4pt, fill: k100)[ISBN 979-8-1829-6229-2])))
