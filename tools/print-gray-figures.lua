-- Print edition (quarto render --profile print): use the grayscale render of every figure.
-- Figures are referenced as ../figures/out/color/<id>.svg; the gray render has the same name
-- under figures/out/gray/ (decision D29; CLAUDE.md "every figure has a color and a grayscale render").
function Image(el)
  el.src = el.src:gsub("figures/out/color/", "figures/out/gray/")
  return el
end
