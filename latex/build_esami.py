#!/usr/bin/env python3
"""Render the worked Econometria exam solutions to PDF.

    python3 build_esami.py --list
    python3 build_esami.py --all
    python3 build_esami.py --exam 2023-12-21
    python3 build_esami.py --volume            # all exams in one PDF
    python3 build_esami.py --all --keep        # keep LaTeX intermediates

Same template and general filter as the dispense (build.py), so both look the
same:

    esami/econometria/src/ECON_Sol_<data>.md
      -> normalisation (front matter, Obsidian callouts, glyphs)
        -> build/esami-econometria/<slug>.md
          -> pandoc + filters/esami.lua (exam blocks)
                    + filters/callouts.lua (tables, displays, figures)
                    + template/dispensa.latex + esami/econometria/macros.tex
            -> build/esami-econometria/<slug>/<slug>.tex
              -> latexmk -xelatex
                -> ../esami/econometria/ECON_Sol_<data>.pdf

Figures are NOT built here: each exam owns esami/econometria/figure/<data>/
plots.py, which regenerates its PDFs (this script only checks they exist).
"""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

LATEX = Path(__file__).resolve().parent
REPO = LATEX.parent
COURSE = LATEX / "esami" / "econometria"       # sources, figures, macros
SRC = COURSE / "src"
OUTDIR = REPO / "esami" / "econometria"        # the PDFs only
BUILD = LATEX / "build" / "esami-econometria"
TEMPLATE = LATEX / "template" / "dispensa.latex"
# Exam blocks first: their callout kinds mean something else in the dispense.
FILTERS = [LATEX / "filters" / "esami.lua", LATEX / "filters" / "callouts.lua"]
MACROS = COURSE / "macros.tex"

UNIVERSITY = "Università Ca' Foscari Venezia"
DEPARTMENT = "Dipartimento di Economia"
DEGREE = "Economia e Finanza"
AUTHOR = "Silvio Angelo Baratto Roldan"
ACCADEMICO = "2026/2027"
DISCLAIMER = ("Svolgimento personale a fini di studio, basato sulla teoria del corso "
              "(Econometria EM0004, prof. Davide Raggi). Non è una soluzione ufficiale.")

FENCE = ":" * 5
CALLOUT_RE = re.compile(r"^>\s*\[!(?P<kind>\w+)\][-+]?\s*(?P<heading>.*)$")
WIKILINK_RE = re.compile(r"\[\[([^\]|]+?)(?:\|([^\]]*?))?\]\]")
FM_KEY_RE = re.compile(r"^(?P<key>[A-Za-z_][\w-]*):\s*(?P<val>.*)$")


# --------------------------------------------------------------- front matter
def split_frontmatter(raw: str) -> tuple[dict, str]:
    if not raw.startswith("---\n"):
        return {}, raw
    end = raw.find("\n---", 4)
    if end == -1:
        return {}, raw
    head, body = raw[4:end], raw[end + 4:]
    meta: dict[str, str] = {}
    for line in head.splitlines():
        if not line.strip() or line.lstrip().startswith("- "):
            continue
        m = FM_KEY_RE.match(line)
        if m:
            val = m.group("val").strip().strip('"').strip("'")
            if val:
                meta[m.group("key")] = val
    return meta, body.lstrip("\n")


# ---------------------------------------------------------------- glyph fixes
# Symbols go through \ensuremath, never $...$: a generated "$-$" right before a
# digit cannot close, and pandoc pairs the dollars across the paragraph.
TEXT_GLYPHS = {
    "→": r"\ensuremath{\rightarrow}", "⇒": r"\ensuremath{\Rightarrow}", "←": r"\ensuremath{\leftarrow}",
    "⇐": r"\ensuremath{\Leftarrow}", "↔": r"\ensuremath{\leftrightarrow}", "⇔": r"\ensuremath{\Leftrightarrow}",
    "↑": r"\ensuremath{\uparrow}", "↓": r"\ensuremath{\downarrow}",
    "−": r"\ensuremath{-}", "∼": r"\ensuremath{\sim}", "≈": r"\ensuremath{\approx}", "≃": r"\ensuremath{\simeq}",
    "≥": r"\ensuremath{\geq}", "≤": r"\ensuremath{\leq}", "≠": r"\ensuremath{\neq}", "∈": r"\ensuremath{\in}",
    "⋮": r"\ensuremath{\vdots}", "…": r"\ldots{}", "×": r"\ensuremath{\times}",
    "✓": r"\ding{51}", "✗": r"\ding{55}", "●": r"\ensuremath{\bullet}",
    "₀": r"\textsubscript{0}", "₁": r"\textsubscript{1}", "₂": r"\textsubscript{2}",
    "α": r"\ensuremath{\alpha}", "β": r"\ensuremath{\beta}", "γ": r"\ensuremath{\gamma}", "δ": r"\ensuremath{\delta}",
    "ε": r"\ensuremath{\varepsilon}", "λ": r"\ensuremath{\lambda}", "μ": r"\ensuremath{\mu}",
    "ρ": r"\ensuremath{\rho}", "σ": r"\ensuremath{\sigma}", "χ": r"\ensuremath{\chi}", "ω": r"\ensuremath{\omega}",
    "Δ": r"\ensuremath{\Delta}", "Σ": r"\ensuremath{\Sigma}", "Π": r"\ensuremath{\Pi}",
}
MATH_SPAN_RE = re.compile(r"(?<!\\)(\$\$(?:\\.|[^\\])*?\$\$|\$(?:\\.|[^$\\\n])+?\$)", re.DOTALL)


def fix_glyphs(text: str) -> str:
    def convert(chunk: str) -> str:
        for src, dst in TEXT_GLYPHS.items():
            chunk = chunk.replace(src, dst)
        return chunk
    return "".join(part if i % 2 else convert(part)
                   for i, part in enumerate(MATH_SPAN_RE.split(text)))


# ------------------------------------------------------------------- callouts
def convert_callouts(lines: list[str]) -> list[str]:
    out: list[str] = []
    i = 0
    while i < len(lines):
        m = CALLOUT_RE.match(lines[i])
        if not m:
            out.append(lines[i])
            i += 1
            continue
        kind = m.group("kind").lower()
        heading = m.group("heading").strip().replace('"', "'")
        i += 1
        body: list[str] = []
        while i < len(lines) and (lines[i].startswith(">") or lines[i].strip() == ""):
            if lines[i].strip() == "":
                # a blank line ends the callout, unless the same quote continues
                # -- but a new `> [!kind]` header starts a SIBLING callout, and
                # solution files stack them back to back.
                nxt = lines[i + 1] if i + 1 < len(lines) else ""
                if nxt.startswith(">") and not CALLOUT_RE.match(nxt):
                    body.append("")
                    i += 1
                    continue
                break
            if body and CALLOUT_RE.match(lines[i]):
                break            # sibling callout with no blank line between
            stripped = lines[i][1:]
            body.append(stripped[1:] if stripped.startswith(" ") else stripped)
            i += 1
        attrs = f'kind="{kind}"' + (f' heading="{heading}"' if heading else "")
        out += ["", f"{FENCE} {{.callout {attrs}}}"] + convert_callouts(body) + [FENCE, ""]
    return out


def strip_wikilinks(text: str) -> str:
    """Obsidian [[Nota|label]] -> italic label (targets live outside this PDF)."""
    def repl(m: re.Match) -> str:
        return (m.group(2) or m.group(1)).strip()
    return WIKILINK_RE.sub(repl, text)


def normalise(body: str) -> str:
    return "\n".join(convert_callouts(fix_glyphs(strip_wikilinks(body)).splitlines()))


# --------------------------------------------------------------------- render
def run(cmd: list[str], cwd: Path | None = None) -> None:
    proc = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if proc.returncode != 0:
        sys.stderr.write(proc.stdout[-8000:])
        sys.stderr.write(proc.stderr[-8000:])
        raise SystemExit(f"command failed ({proc.returncode}): {' '.join(cmd[:3])} ...")
    for line in proc.stderr.strip().splitlines():
        if "warning" in line.lower() or "Missing" in line:
            print(f"    ! {line}", file=sys.stderr)


# A caption may itself contain "]", so anchor on the "](path)" tail instead of
# trying to match balanced brackets in the alt text.
IMG_RE = re.compile(r"!\[.*\]\((?P<path>[^)\s]+)", re.MULTILINE)


def figure_refs(body: str) -> list[str]:
    return IMG_RE.findall(body)


def missing_figures(body: str) -> list[str]:
    return [r for r in figure_refs(body) if not (COURSE / r).exists()]


def render(md_path: Path, toc_depth: int, keep: bool,
           corpo: str | None = None, meta_extra: dict | None = None) -> Path:
    if corpo is None:
        meta, body = split_frontmatter(md_path.read_text(encoding="utf-8"))
    else:
        meta, body = dict(meta_extra or {}), corpo
    slug = md_path.stem

    gaps = missing_figures(body)
    if gaps:
        print(f"    ! figure mancanti: {', '.join(gaps)}", file=sys.stderr)

    aux = BUILD / slug
    aux.mkdir(parents=True, exist_ok=True)
    flat = BUILD / f"{slug}.md"
    flat.write_text(normalise(body), encoding="utf-8")
    tex = aux / f"{slug}.tex"

    doc_meta = {
        "title": meta.get("title", slug),
        "subtitle": meta.get("subtitle", "Soluzione svolta e commentata"),
        "author": AUTHOR,
        "date": meta.get("date", ACCADEMICO),
        "university": UNIVERSITY,
        "department": DEPARTMENT,
        "degree": DEGREE,
        "coursecode": meta.get("coursecode", "EM0004"),
        "stats": meta.get("stats", ""),
        "disclaimer": DISCLAIMER,
        "graphicspath": f"{COURSE}/",
    }

    cmd = [
        "pandoc", str(flat),
        "--from", "markdown+fenced_divs+header_attributes+tex_math_dollars"
                  "+pipe_tables+raw_tex+footnotes+tex_math_single_backslash"
                  "+link_attributes+implicit_figures",
        "--to", "latex",
        "--standalone",
        "--template", str(TEMPLATE),
        *[arg for f in FILTERS for arg in ("--lua-filter", str(f))],
        "--include-in-header", str(MACROS),
        "--top-level-division=chapter",
        "--toc", f"--toc-depth={toc_depth}",
        "--wrap=preserve",
        f"--resource-path={COURSE}",
        "-V", f"toc-depth={max(toc_depth - 1, 0)}",
        "-o", str(tex),
    ]
    for key, value in doc_meta.items():
        if value:
            cmd += ["-M", f"{key}={value}"]
    run(cmd)

    run(["latexmk", "-xelatex", "-interaction=nonstopmode", "-file-line-error",
         "-halt-on-error", f"-outdir={aux}", tex.name], cwd=aux)

    OUTDIR.mkdir(parents=True, exist_ok=True)
    dst = OUTDIR / f"{slug}.pdf"
    shutil.copy2(aux / f"{slug}.pdf", dst)
    if not keep:
        flat.unlink(missing_ok=True)
        for junk in aux.iterdir():
            if junk.suffix not in {".tex"}:
                junk.unlink(missing_ok=True) if junk.is_file() else shutil.rmtree(junk, True)
    return dst



# --------------------------------------------------------------- volume unico
LABEL_RE = re.compile(r"\\(label|eqref|ref|autoref)\{([^}]+)\}")
# Le note a pie' di pagina sono locali al file: due appelli che usano [^1]
# collidono, e pandoc ne scarta una con "Duplicate note reference".
FOOTNOTE_RE = re.compile(r"\[\^([^\]\s]+)\]")
IMGID_RE = re.compile(r"\{#([A-Za-z][\w:.-]*)([^}]*)\}")


def namespace_riferimenti(body: str, slug: str) -> str:
    """Prefissa etichette e rimandi con lo slug dell'appello.

    I sette svolgimenti nascono indipendenti e riusano gli stessi nomi
    (`eq:d01-derivata`, `fig:d03`): concatenandoli senza prefisso LaTeX
    emette "multiply defined" e i rimandi puntano all'appello sbagliato.
    """
    pre = slug.replace("-", "")
    body = LABEL_RE.sub(lambda m: f"\\{m.group(1)}{{{pre}:{m.group(2)}}}", body)
    body = IMGID_RE.sub(lambda m: f"{{#{pre}:{m.group(1)}{m.group(2)}}}", body)
    body = FOOTNOTE_RE.sub(rf"[^{pre}-\1]", body)
    return body


def volume_markdown() -> tuple[str, dict]:
    """Un solo documento: una parte per appello, sezioni e numerazione continue."""
    pezzi, n_dom, n_fig = [], 0, 0
    for md in sources():
        meta, body = split_frontmatter(md.read_text(encoding="utf-8"))
        slug = md.stem.replace("ECON_Sol_", "")
        n_dom += len(re.findall(r"^## ", body, re.M))
        n_fig += len(figure_refs(body))
        titolo = meta.get("title", slug).replace("Econometria — esame del ", "Esame del ")
        pezzi.append(f"\\part{{{titolo}}}\n\n" + namespace_riferimenti(body, slug))
    meta = {
        "title": "Econometria \u2014 soluzioni dei temi d\u2019esame",
        "subtitle": "Sette appelli svolti, con derivazioni e grafici",
        "stats": f"{len(sources())} appelli \u00b7 {n_dom} domande \u00b7 {n_fig} figure",
    }
    return "\n\n".join(pezzi), meta


# ------------------------------------------------------------------------ cli
def sources() -> list[Path]:
    return sorted(SRC.glob("ECON_Sol_*.md"))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--list", action="store_true", help="elenca le soluzioni disponibili")
    ap.add_argument("--all", action="store_true", help="compila ogni soluzione")
    ap.add_argument("--exam", metavar="DATA", help="compila una sola soluzione (es. 2023-12-21)")
    ap.add_argument("--toc-depth", type=int, default=2)
    ap.add_argument("--keep", action="store_true", help="conserva i file .tex intermedi")
    ap.add_argument("--volume", action="store_true",
                    help="compone i sette appelli in un solo PDF")
    args = ap.parse_args()

    found = sources()
    if args.list or not (args.all or args.exam or args.volume):
        if not found:
            print("nessuna soluzione in src/")
            return 0
        for p in found:
            meta, body = split_frontmatter(p.read_text(encoding="utf-8"))
            n_fig = len(figure_refs(body))
            pdf = OUTDIR / f"{p.stem}.pdf"
            print(f"  {p.stem:26s} {len(body.splitlines()):5d} righe  "
                  f"{n_fig:2d} figure  pdf:{'si' if pdf.exists() else 'no'}")
        return 0

    if args.volume:
        BUILD.mkdir(parents=True, exist_ok=True)
        corpo, meta = volume_markdown()
        print("==> ECON_Soluzioni_Raccolta")
        out = render(SRC / "ECON_Soluzioni_Raccolta.md", max(args.toc_depth, 3),
                     args.keep, corpo=corpo, meta_extra=meta)
        print(f"    {out.name}")
        return 0

    todo = found if args.all else [p for p in found if args.exam in p.stem]
    if not todo:
        print(f"nessuna soluzione corrisponde a {args.exam!r}", file=sys.stderr)
        return 1

    BUILD.mkdir(parents=True, exist_ok=True)
    for p in todo:
        print(f"==> {p.stem}")
        out = render(p, args.toc_depth, args.keep)
        print(f"    {out.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
