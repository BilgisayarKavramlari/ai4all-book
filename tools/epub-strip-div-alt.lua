-- EPUB only: Quarto copies fig-alt onto the figure's wrapper <div> as an "alt" attribute,
-- which EPUBCheck rejects (RSC-005: attribute "alt" not allowed here). The <img> keeps its alt.
function Div(el)
  if el.attributes["alt"] ~= nil then
    el.attributes["alt"] = nil
    return el
  end
end
