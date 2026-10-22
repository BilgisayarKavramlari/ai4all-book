#!/usr/bin/env bash
# Convert the print interior (quarto render --profile print --to typst -> _book-print/AI-for-All.pdf)
# to PDF/X-1a:2001 in grayscale for IngramSpark (decision D29). Needs Ghostscript (brew install ghostscript).
# Link annotations are dropped (not allowed in PDF/X; a printed page has no links).
# Usage (from the repo root): tools/make-print-pdfx.sh [input.pdf] [output.pdf]
set -euo pipefail
IN="${1:-_book-print/AI-for-All.pdf}"
OUT="${2:-_book-print/AI-for-All-interior-PDFX1a.pdf}"
DEF="tools/pdfx/PDFX_def_ai4all.ps"
# IngramSpark wants an even page count: add one blank page at the end if needed.
N=$(qpdf --show-npages "$IN")
if [ $((N % 2)) -eq 1 ]; then
  BLANK="$(mktemp -d)/blank.pdf"
  gs -q -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -dDEVICEWIDTHPOINTS=612 -dDEVICEHEIGHTPOINTS=792 -dFIXEDMEDIA \
     -sOutputFile="$BLANK" -c showpage
  EVEN="$(dirname "$BLANK")/even.pdf"
  qpdf "$IN" --pages "$IN" "$BLANK" -- "$EVEN"
  IN="$EVEN"
  echo "added a blank last page ($N -> $((N + 1)) pages)"
fi
gs -dPDFX=1 -dBATCH -dNOPAUSE -dNOSAFER -dQUIET \
   -sDEVICE=pdfwrite -dCompatibilityLevel=1.3 \
   -sColorConversionStrategy=Gray -sProcessColorModel=DeviceGray \
   -dPDFSETTINGS=/prepress -dEmbedAllFonts=true -dSubsetFonts=true \
   -dAutoRotatePages=/None -dPreserveAnnots=false \
   -dDownsampleGrayImages=false -dDownsampleColorImages=false -dDownsampleMonoImages=false \
   -sOutputFile="$OUT.tmp.pdf" "$DEF" "$IN"
python3 tools/pdfx/add_trimbox.py "$OUT.tmp.pdf" "$OUT"
rm -f "$OUT.tmp.pdf"
echo "wrote $OUT"
