# Fonts used by the PDF builds

Typst ignores system fonts during the book's PDF builds (`_environment`: TYPST_IGNORE_SYSTEM_FONTS=true) and uses only this folder (`font-paths` in _quarto.yml) plus Quarto's bundled fonts (Font Awesome, New Computer Modern Math, DejaVu Sans Mono). Every file here is unmodified and licensed under the SIL Open Font License 1.1.

| Files | Font | Source |
|---|---|---|
| SourceSans3-{Regular,It,Semibold,SemiboldIt,Bold,BoldIt}.otf | Source Sans 3, static, v3.052R | Adobe official release, https://github.com/adobe-fonts/source-sans/releases/tag/3.052R (OTF-source-sans-3.052R.zip, downloaded 2026-10-22); license in LICENSE-SourceSans3.md |
| SourceSerif4[opsz,wght].ttf, SourceSerif4-Italic[opsz,wght].ttf | Source Serif 4, variable | Copied from the build machine's installed fonts (Google Fonts build of Adobe's Source Serif 4) |
| JetBrainsMono-{Regular,Bold,Italic,BoldItalic}.ttf | JetBrains Mono, static | Copied from the build machine's installed fonts (JetBrains) |
| STIXGeneral*.otf, STIXTwoText*.ttf | STIX fonts (symbol fallback) | Copied from the build machine's system fonts (STIX Fonts project) |

Why static Source Sans 3: with only the variable Source Sans 3 installed, Typst rendered regular-weight figure and chart text as ExtraLight, too faint for black-and-white print.
