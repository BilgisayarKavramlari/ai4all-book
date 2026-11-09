#!/usr/bin/env bash
# Build the full paperback cover (back + spine + front) for IngramSpark (decision D29/D30):
# publishing/print-cover/cover.typ on Ingram's template (publishing/print-cover/template.pdf, a copy of
# publishing/9798182962292-Perfect.pdf), then CMYK PDF/X-1a:2001 with Ghostscript.
# Usage (from the repo root): tools/make-print-cover.sh
set -euo pipefail
cd publishing/print-cover
TYPST_IGNORE_SYSTEM_FONTS=true quarto typst compile --font-path ../../fonts cover.typ cover-rgb.pdf
cd ../..
OUT=build/out/AI-for-All-cover-PDFX1a.pdf   # outside _book-print, which each print render empties
mkdir -p build/out
gs -dPDFX=1 -dBATCH -dNOPAUSE -dNOSAFER -dQUIET \
   -sDEVICE=pdfwrite -dCompatibilityLevel=1.3 \
   -sColorConversionStrategy=CMYK -sProcessColorModel=DeviceCMYK \
   -dPDFSETTINGS=/prepress -dEmbedAllFonts=true -dSubsetFonts=true \
   -dAutoRotatePages=/None -dPreserveAnnots=false \
   -dDownsampleColorImages=false -dDownsampleGrayImages=false -dDownsampleMonoImages=false \
   -sOutputFile="$OUT.tmp.pdf" tools/pdfx/PDFX_def_ai4all.ps publishing/print-cover/cover-rgb.pdf
# Ingram's template (CMYK, PDF 1.3) underneath: its marks and labels outside the artwork stay as delivered;
# the artwork covers every pink and blue box.
qpdf --force-version=1.3 "$OUT.tmp.pdf" --underlay publishing/print-cover/template.pdf -- "$OUT.under.pdf"
python3 tools/pdfx/add_trimbox.py "$OUT.under.pdf" "$OUT"
rm -f "$OUT.tmp.pdf" "$OUT.under.pdf"
echo "wrote $OUT"
