-- Converts the fenced divs produced by build.py into LaTeX, and sizes tables.
--   ::::: {.callout kind="abstract" heading="Definizione"} ... :::::
--   ::::: {.slideref} (slide 3) :::::
--   ::::: {.chapsource} Fonte: ... :::::
--
-- The callout head is not an environment argument: it is injected as the
-- first inline of the first paragraph, so it stays run-in instead of taking
-- a line of its own. The environments in template/dispensa.latex only set
-- vertical space and step the counter.

local ENV = {
  abstract = "cvdefinizione",
  tip      = "cvteorema",
  example  = "cvesempio",
  note     = "cvdimostrazione",
}

local DEFAULT_HEADING = {
  abstract = "Definizione",
  tip      = "Teorema",
  example  = "Esempio",
  note     = "Dimostrazione",
}

local NUMBERED = { cvdefinizione = true, cvteorema = true, cvesempio = true }
local ITALIC_HEAD = { cvdimostrazione = true, cvnota = true }

local function inline_latex(str)
  local doc = pandoc.read(str, "markdown")
  local tex = pandoc.write(doc, "latex")
  return (tex:gsub("%s+$", ""))
end

local function blocks_latex(blocks)
  local tex = pandoc.write(pandoc.Pandoc(blocks), "latex")
  return (tex:gsub("%s+$", ""))
end

local function is_paragraph(block)
  return block and (block.t == "Para" or block.t == "Plain")
end

local function callout(el)
  local kind = el.attributes["kind"] or "note"
  local env = ENV[kind] or "cvnota"
  local heading = el.attributes["heading"]
  if heading == nil or heading == "" then
    heading = DEFAULT_HEADING[kind] or "Nota"
  end
  heading = inline_latex((heading:gsub("%.%s*$", "")))
  if NUMBERED[env] then
    heading = heading .. "~\\the" .. env
  end
  local cmd = ITALIC_HEAD[env] and "cvproofhead" or "cvhead"
  local head = pandoc.RawInline("latex", "\\" .. cmd .. "{" .. heading .. "}")

  local content = el.content
  local out = pandoc.List({ pandoc.RawBlock("latex", "\\begin{" .. env .. "}") })
  if is_paragraph(content[1]) then
    content[1].content:insert(1, head)
  else
    out:insert(pandoc.Plain({ head }))
  end
  out:extend(content)
  if env == "cvdimostrazione" then
    if is_paragraph(out[#out]) then
      out[#out].content:insert(pandoc.RawInline("latex", "\\cvqed"))
    else
      out:insert(pandoc.RawBlock("latex", "\\cvqed"))
    end
  end
  out:insert(pandoc.RawBlock("latex", "\\end{" .. env .. "}"))
  return out
end

-- Table sizing --------------------------------------------------------------
-- Pipe tables whose source lines exceed --columns get relative widths from
-- the dashes of the separator row, which Obsidian writes all alike: every
-- column comes out equal, numeric columns waste space and text columns
-- overflow. Widths are recomputed from the content with the CSS automatic
-- table layout: a column gets at least its longest word (min-content) and
-- the spare room is shared in proportion to max-content minus min-content.

-- Widths are counted in average prose characters of \small Latin Modern
-- (10 pt in the 11 pt class): the 160 mm measure holds ~106 of them,
-- measured, and each column also pays two default \tabcolsep of 6 pt, ~2.8
-- characters. Tied to template/dispensa.latex. Cells run to capitals and
-- digits, wider than that average, so they are weighted: an underestimate
-- overflows, an overestimate only wraps a little earlier.
local LINE_CHARS = 106
local COLSEP_CHARS = 2.8
-- \LTleft and \LTright let a table shrink into each margin by 10 mm,
-- ~13 characters in all. Smaller sizes hold more characters than \small.
local MARGIN_CHARS = 13
local SMALLER_SIZES = {
  { cmd = "\\footnotesize", gain = 10 / 9 },
  { cmd = "\\scriptsize", gain = 10 / 8 },
}

-- Advance widths over the prose average, rounded up.
local WIDE = { m = 1.9, w = 1.75, M = 2.0, W = 2.2 }
local NARROW = { i = 0.65, j = 0.65, l = 0.65, t = 0.8, f = 0.8, r = 0.85, [" "] = 0.6 }

local function glyph_width(ch)
  if WIDE[ch] then return WIDE[ch] end
  if NARROW[ch] then return NARROW[ch] end
  if ch:match("^%u$") then return 1.55 end
  if ch:match("^%d$") then return 1.15 end
  return 1.1
end

local function text_width(text)
  local w = 0
  for ch in text:gmatch(utf8.charpattern) do
    w = w + glyph_width(ch)
  end
  return w
end

local function math_chars(tex)
  return text_width((tex:gsub("\\[%a]+", "x"):gsub("[ \t\r\n{}%^_&\\]", "")))
end

local function cell_text(cell)
  local function as_width(text) return pandoc.Str(string.rep("x", math.ceil(math_chars(text)))) end
  return pandoc.utils.stringify(cell.contents:walk({
    Math = function(m) return as_width(m.text) end,
    RawInline = function(r) return as_width(r.text) end,
  }))
end

local function measure(text)
  local longest = 0
  for word in text:gmatch("[^ \t\r\n]+") do
    longest = math.max(longest, text_width(word))
  end
  return longest + 1.5, text_width(text) + 1.5
end

local function each_row(tbl, fn)
  for _, row in ipairs(tbl.head.rows) do fn(row) end
  for _, body in ipairs(tbl.bodies) do
    for _, row in ipairs(body.head) do fn(row) end
    for _, row in ipairs(body.body) do fn(row) end
  end
  for _, row in ipairs(tbl.foot.rows) do fn(row) end
end

local function is_simple(tbl)
  local simple = true
  each_row(tbl, function(row)
    for _, cell in ipairs(row.cells) do
      if #cell.contents > 1 or (cell.contents[1] and cell.contents[1].t ~= "Plain") then
        simple = false
      end
    end
  end)
  return simple
end

-- Column widths as fractions of the measure (pandoc multiplies them by
-- \linewidth less the column gaps), or nil when even the longest words do
-- not fit in `room`. `line` is the measure in the same characters.
local function layout(minw, maxw, line, room)
  local n, summin, summax = #minw, 0, 0
  for j = 1, n do summin, summax = summin + minw[j], summax + maxw[j] end
  if summin > room then return nil end
  local widths = {}
  if summax <= room then
    for j = 1, n do widths[j] = maxw[j] / line end
  else
    local share = (room - summin) / (summax - summin)
    for j = 1, n do widths[j] = (minw[j] + (maxw[j] - minw[j]) * share) / line end
  end
  return widths
end

function Table(tbl)
  local n = #tbl.colspecs
  local minw, maxw = {}, {}
  for j = 1, n do minw[j], maxw[j] = 1, 1 end
  each_row(tbl, function(row)
    local j = 1
    for _, cell in ipairs(row.cells) do
      if cell.col_span == 1 and j <= n then
        local lo, hi = measure(cell_text(cell))
        minw[j] = math.max(minw[j], lo)
        maxw[j] = math.max(maxw[j], hi)
      end
      j = j + cell.col_span
    end
  end)

  local line = LINE_CHARS - COLSEP_CHARS * n
  local summax = 0
  for j = 1, n do summax = summax + maxw[j] end

  -- Prefer wrapping inside the measure, then the margins, then smaller sizes.
  local widths, size
  if summax <= line and is_simple(tbl) then
    widths = {}   -- natural l/c/r columns: LaTeX measures them exactly
  else
    widths = layout(minw, maxw, line, line)
          or layout(minw, maxw, line, line + MARGIN_CHARS)
    for _, smaller in ipairs(SMALLER_SIZES) do
      if widths then break end
      size = smaller
      widths = layout(minw, maxw, line * smaller.gain, (line + MARGIN_CHARS) * smaller.gain)
    end
    if not widths then
      -- Nothing fits: spread the overflow evenly instead of on one column.
      local summin = 0
      for j = 1, n do summin = summin + minw[j] end
      widths = {}
      for j = 1, n do widths[j] = minw[j] / summin * (line + MARGIN_CHARS) / line end
    end
  end

  for j = 1, n do
    tbl.colspecs[j] = { tbl.colspecs[j][1], widths[j] }
  end
  if size then
    return {
      pandoc.RawBlock("latex", "\\begingroup\\let\\cvtablesize" .. size.cmd),
      tbl,
      pandoc.RawBlock("latex", "\\endgroup"),
    }
  end
  return tbl
end

-- A long unbroken code token (a hash, an address) has no breakpoint and
-- overruns the measure: let it break between any two characters.
function Code(c)
  if #c.text > 24 and c.text:match("^%w+$") then
    return pandoc.RawInline("latex", "\\texttt{\\seqsplit{" .. c.text .. "}}")
  end
end

-- Display math --------------------------------------------------------------
-- \cvdisplay typesets its argument twice (measure, then set), so a \tag is
-- passed apart and set once; anything that labels or unnumbers is left to
-- plain \[...\].
local SINGLE_PASS_ONLY = { "\\label", "\\notag", "\\nonumber" }

function Math(m)
  if m.mathtype ~= "DisplayMath" then return nil end
  for _, cmd in ipairs(SINGLE_PASS_ONLY) do
    if m.text:find(cmd, 1, true) then return nil end
  end
  local tag = ""
  local body = m.text:gsub("\\tag%*?%s*%b{}", function(t) tag = t; return "" end)
  return pandoc.RawInline("latex", "\\cvdisplay[" .. tag .. "]{" .. body .. "}")
end

-- Figures -------------------------------------------------------------------
-- A paragraph that is only an image becomes a centred figure. Not a float:
-- in these notes the "Figura N -- ..." paragraph that follows describes it,
-- so it must stay where it is. The alt text, when present, says how a chart
-- was rebuilt and is set under it.
local function lone_image(inlines)
  local image
  for _, el in ipairs(inlines) do
    if el.t == "Image" then
      if image then return nil end
      image = el
    elseif el.t ~= "Space" and el.t ~= "SoftBreak" then
      return nil
    end
  end
  return image
end

function Para(p)
  local image = lone_image(p.content)
  if not image then return nil end
  local note = blocks_latex({ pandoc.Plain(image.caption) })
  return pandoc.RawBlock("latex", "\\cvfigure{" .. image.src .. "}{" .. note .. "}")
end

-- Divs and block lists ------------------------------------------------------
function Div(el)
  if el.classes:includes("callout") then
    return callout(el)
  end
  if el.classes:includes("chapsource") then
    return pandoc.RawBlock("latex", "\\chapsource{" .. blocks_latex(el.content) .. "}")
  end
end

-- A slide reference closes the passage it cites: it goes flush right on the
-- last line of the preceding paragraph rather than costing a line of its own.
-- Runs after Div, so callouts are already spliced into the surrounding list.
function Blocks(blocks)
  local out = pandoc.List()
  for _, block in ipairs(blocks) do
    if block.t == "Div" and block.classes:includes("slideref") then
      local mark = "\\slideref{" .. blocks_latex(block.content) .. "}"
      if is_paragraph(out[#out]) then
        out[#out].content:insert(pandoc.RawInline("latex", mark))
      else
        out:insert(pandoc.RawBlock("latex", mark))
      end
    else
      out:insert(block)
    end
  end
  return out
end
