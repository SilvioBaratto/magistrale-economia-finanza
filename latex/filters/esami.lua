-- Exam-solution callouts -> environments of template/dispensa.latex, for
-- build_esami.py.
--   ::::: {.callout kind="tip" heading="Richiamo"} ... :::::
--
-- Runs BEFORE the general filter (filters/callouts.lua), which
-- sizes tables, sets wide displays and figures: the callout kinds mean
-- something else here (abstract = data, not definition), so they must be
-- consumed before the shared mapping sees them.
--
-- The head is injected as the first inline of the first paragraph, so it
-- stays run-in; \cvhead and \cvproofhead come from the shared template.

local ENV = {
  question = "cvtesto",          -- the exam question, verbatim
  abstract = "cvdati",           -- data, model, regression output
  tip      = "cvteoria",         -- recalled theory
  example  = "cvcalcolo",        -- the working
  success  = "cvrisposta",       -- the answer
  info     = "cvspiegazione",    -- oral tracks: the reasoning behind the answer to give
  warning  = "cvosservazione",   -- side remark
  note     = "cvnota",
}

-- Remarks and notes are accessory: italic head, like a proof's.
local ITALIC_HEAD = { cvosservazione = true, cvnota = true }

local DEFAULT_HEADING = {
  question = "Testo d'esame",
  abstract = "Dati",
  tip      = "Richiamo",
  example  = "Svolgimento",
  success  = "Risposta",
  info     = "Spiegazione",
  warning  = "Osservazione",
  note     = "Nota",
}

local function inline_latex(str)
  local doc = pandoc.read(str, "markdown")
  local tex = pandoc.write(doc, "latex")
  return (tex:gsub("%s+$", ""))
end

local function blocks_latex(blocks)
  local tex = pandoc.write(pandoc.Pandoc(blocks), "latex")
  return (tex:gsub("%s+$", ""))
end

function Div(el)
  if el.classes:includes("callout") then
    local kind = el.attributes["kind"] or "note"
    local env = ENV[kind] or "cvnota"
    local heading = el.attributes["heading"]
    if heading == nil or heading == "" then
      heading = DEFAULT_HEADING[kind] or "Nota"
    end
    heading = heading:gsub("%.%s*$", "")          -- the head macro adds the full stop

    local cmd = ITALIC_HEAD[env] and "cvproofhead" or "cvhead"
    local head = pandoc.RawInline("latex", "\\" .. cmd .. "{" .. inline_latex(heading) .. "}")

    local content = el.content
    local out = pandoc.List()
    out:insert(pandoc.RawBlock("latex", "\\begin{" .. env .. "}"))
    if content[1] and (content[1].t == "Para" or content[1].t == "Plain") then
      table.insert(content[1].content, 1, head)
    else
      out:insert(pandoc.Plain({ head }))
    end
    out:extend(content)
    out:insert(pandoc.RawBlock("latex", "\\end{" .. env .. "}"))
    return out
  end

  if el.classes:includes("chapsource") then
    return pandoc.RawBlock("latex", "\\chapsource{" .. blocks_latex(el.content) .. "}")
  end
end
