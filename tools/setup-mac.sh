#!/usr/bin/env bash
# AI for All textbook — local toolchain for macOS (Homebrew required: https://brew.sh)
# Run from the repository root:  bash tools/setup-mac.sh
set -u

step() { printf "\n==> %s\n" "$1"; }
try()  { "$@" || echo "   !! failed: $* (continue; fix later)"; }

step "Homebrew packages"
try brew install git gh node poppler qpdf epubcheck vale
try brew install --cask quarto            # Quarto bundles Pandoc and Typst
# If the cask installer cannot ask for a password, install without sudo into ~/Applications:
#   pkgutil --expand-full "$(ls /opt/homebrew/Caskroom/quarto/*/quarto-*-macos.pkg | tail -1)" /tmp/quarto-pkg
#   cp -R /tmp/quarto-pkg/quarto-core.pkg/Payload ~/Applications/quarto && ln -sf ~/Applications/quarto/bin/quarto ~/.local/bin/quarto

step "Node tools"
try npm install -g @mermaid-js/mermaid-cli   # mmdc: Mermaid -> SVG/PNG/PDF
try npm install -g @daisy/ace                # Ace by DAISY: EPUB accessibility checker

step "Python tools for data charts"
try python3 -m pip install --user matplotlib pandas

step "Open-licensed fonts (SIL OFL)"
try brew install --cask font-source-serif-4 font-source-sans-3 font-jetbrains-mono

step "Prose linter styles"
try vale sync

step "Versions"
for c in git gh quarto mmdc epubcheck ace vale pdffonts; do
  printf "%-10s " "$c"; command -v "$c" >/dev/null && echo ok || echo MISSING
done
quarto check || true
