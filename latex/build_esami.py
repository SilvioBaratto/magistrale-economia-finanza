#!/usr/bin/env python3
"""Render the exam material of every course to PDF.

    python3 build_esami.py --list                                   # courses and sources
    python3 build_esami.py --all                                    # every PDF, every course
    python3 build_esami.py --volume                                 # each course's single volume
    python3 build_esami.py --corso econometria --exam 2023-12-21    # one PDF
    python3 build_esami.py --corso legislazione-bancaria-1 --exam 04
    python3 build_esami.py --all --keep                             # keep LaTeX intermediates

Two kinds of material, one pipeline, the template of the dispense:

- econometria: worked solutions of past written exams, one PDF per sitting;
- legislazione-bancaria-1/-2: question-and-answer tracks for the oral exam,
  one PDF per point of the syllabus.

    esami/<corso>/src/*.md
      -> normalisation (front matter, Obsidian callouts, glyphs)
        -> build/esami-<corso>/<slug>.md
          -> pandoc + filters/esami.lua (exam blocks) + filters/callouts.lua
                    + template/dispensa.latex (+ esami/<corso>/macros.tex)
            -> build/esami-<corso>/<slug>/<slug>.tex -> latexmk -xelatex
              -> ../esami/<corso>/<slug>.pdf

Figures are NOT built here: a course with figures owns
esami/<corso>/figure/<data>/plots.py (this script only checks they exist).
"""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

LATEX = Path(__file__).resolve().parent
REPO = LATEX.parent
TEMPLATE = LATEX / "template" / "dispensa.latex"
# Exam blocks first: their callout kinds mean something else in the dispense.
FILTERS = [LATEX / "filters" / "esami.lua", LATEX / "filters" / "callouts.lua"]

UNIVERSITY = "Università Ca' Foscari Venezia"
DEPARTMENT = "Dipartimento di Economia"
DEGREE = "Economia e Finanza"
AUTHOR = "Silvio Angelo Baratto Roldan"
ACCADEMICO = "2026/2027"


@dataclass(frozen=True)
class Course:
    """What differs between the exam material of two courses.

    Attributes:
        slug: Folder name under esami/ (sources in latex/, PDFs at the root).
        pattern: Glob of the sources in src/.
        coursecode: Code printed on the title page.
        disclaimer: Last line of the title page.
        subtitle: Subtitle of a single PDF whose front matter has none.
        volume: File stem of the single volume.
        volume_title: Title of the single volume.
        volume_subtitle: Subtitle of the single volume.
        parts: Whether the volume gives each source a \\part (exam sittings) or
            just runs their chapters on (syllabus points).
        question_re: Counts the questions of a source, for the title page.
        unit: Name of a source in the volume statistics.
    """

    slug: str
    pattern: str
    coursecode: str
    disclaimer: str
    subtitle: str
    volume: str
    volume_title: str
    volume_subtitle: str
    parts: bool
    question_re: str
    unit: str

    @property
    def sources_dir(self) -> Path:
        return LATEX / "esami" / self.slug

    @property
    def outdir(self) -> Path:
        return REPO / "esami" / self.slug

    @property
    def build_dir(self) -> Path:
        return LATEX / "build" / f"esami-{self.slug}"


def _orale(n: int, points: str) -> Course:
    module = f"mod. {n}"
    return Course(
        slug=f"legislazione-bancaria-{n}",
        pattern=f"LEGB{n}_Orale_*.md",
        coursecode="EM2101",
        disclaimer=("Preparazione personale alla prova orale di Legislazione Bancaria "
                    f"(EM2101, {module}, prof. Alberto Urbani), costruita sul materiale del "
                    "corso e sulle fonti normative. Non è materiale ufficiale del docente."),
        subtitle=points,
        volume=f"LEGB{n}_Orale_Completo",
        volume_title=f"Legislazione Bancaria {n} \u2014 tracce per la prova orale",
        volume_subtitle=points,
        parts=False,
        question_re=r"^##\s+D\d+",
        unit="sezioni",
    )


COURSES = {c.slug: c for c in (
    Course(
        slug="econometria",
        pattern="ECON_Sol_*.md",
        coursecode="EM0004",
        disclaimer=("Svolgimento personale a fini di studio, basato sulla teoria del corso "
                    "(Econometria EM0004, prof. Davide Raggi). Non è una soluzione ufficiale."),
        subtitle="Soluzione svolta e commentata",
        volume="ECON_Soluzioni_Raccolta",
        volume_title="Econometria \u2014 soluzioni dei temi d\u2019esame",
        volume_subtitle="Sette appelli svolti, con derivazioni e grafici",
        parts=True,
        question_re=r"^## ",
        unit="appelli",
    ),
    _orale(1, "Punti 1\u20137 del programma (prova intermedia)"),
    _orale(2, "Punti 8\u201311 del programma (seconda prova)"),
)}

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
    "≡": r"\ensuremath{\equiv}", "▪": r"\ensuremath{\bullet}",
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


def count_questions(course: Course, body: str) -> int:
    return len(re.findall(course.question_re, body, re.M))


def render(course: Course, slug: str, body: str, meta: dict[str, str],
           toc_depth: int, keep: bool) -> Path:
    """Compile one Markdown body to ``esami/<corso>/<slug>.pdf``.

    Args:
        course: The course the material belongs to.
        slug: Output file stem.
        body: Markdown without front matter.
        meta: Title-page fields; missing ones fall back to the course's.
        toc_depth: Depth of the table of contents.
        keep: Keep the LaTeX intermediates.

    Returns:
        The written PDF.
    """
    gaps = [r for r in figure_refs(body) if not (course.sources_dir / r).exists()]
    if gaps:
        print(f"    ! figure mancanti: {', '.join(gaps)}", file=sys.stderr)

    aux = course.build_dir / slug
    aux.mkdir(parents=True, exist_ok=True)
    flat = course.build_dir / f"{slug}.md"
    flat.write_text(normalise(body), encoding="utf-8")
    tex = aux / f"{slug}.tex"

    n = count_questions(course, body)
    doc_meta = {
        "title": meta.get("title", slug),
        "subtitle": meta.get("subtitle", course.subtitle),
        "author": AUTHOR,
        "date": meta.get("date", ACCADEMICO),
        "university": UNIVERSITY,
        "department": DEPARTMENT,
        "degree": DEGREE,
        "coursecode": meta.get("coursecode", course.coursecode),
        "stats": meta.get("stats", f"{n} domande d\u2019esame" if n else ""),
        "disclaimer": course.disclaimer,
        "graphicspath": f"{course.sources_dir}/",
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
        "--top-level-division=chapter",
        "--toc", f"--toc-depth={toc_depth}",
        "--wrap=preserve",
        f"--resource-path={course.sources_dir}",
        "-V", f"toc-depth={max(toc_depth - 1, 0)}",
        "-o", str(tex),
    ]
    macros = course.sources_dir / "macros.tex"
    if macros.is_file():
        cmd += ["--include-in-header", str(macros)]
    for key, value in doc_meta.items():
        if value:
            cmd += ["-M", f"{key}={value}"]
    run(cmd)

    run(["latexmk", "-xelatex", "-interaction=nonstopmode", "-file-line-error",
         "-halt-on-error", f"-outdir={aux}", tex.name], cwd=aux)

    course.outdir.mkdir(parents=True, exist_ok=True)
    dst = course.outdir / f"{slug}.pdf"
    shutil.copy2(aux / f"{slug}.pdf", dst)
    if not keep:
        flat.unlink(missing_ok=True)
        for junk in aux.iterdir():
            if junk.suffix not in {".tex"}:
                junk.unlink(missing_ok=True) if junk.is_file() else shutil.rmtree(junk, True)
    return dst


# --------------------------------------------------------------- single volume
LABEL_RE = re.compile(r"\\(label|eqref|ref|autoref)\{([^}]+)\}")
# Footnotes are local to a file: two sources that both use [^1] collide, and
# pandoc drops one with "Duplicate note reference".
FOOTNOTE_RE = re.compile(r"\[\^([^\]\s]+)\]")
IMGID_RE = re.compile(r"\{#([A-Za-z][\w:.-]*)([^}]*)\}")


def namespace_references(body: str, key: str) -> str:
    """Prefix labels, references, figure ids and footnotes with a source key.

    The sources are written independently and reuse the same names
    (``eq:d01-derivata``, ``fig:d03``, ``[^1]``): concatenated without a
    prefix, LaTeX reports "multiply defined" and references land in the wrong
    source.
    """
    pre = re.sub(r"[^A-Za-z0-9]", "", key)
    body = LABEL_RE.sub(lambda m: f"\\{m.group(1)}{{{pre}:{m.group(2)}}}", body)
    body = IMGID_RE.sub(lambda m: f"{{#{pre}:{m.group(1)}{m.group(2)}}}", body)
    return FOOTNOTE_RE.sub(rf"[^{pre}-\1]", body)


def volume_markdown(course: Course) -> tuple[str, dict[str, str]]:
    """Join every source of a course into one document.

    Returns:
        The Markdown body and its title-page fields.
    """
    pieces, questions, figures = [], 0, 0
    paths = sources(course)
    for md in paths:
        meta, body = split_frontmatter(md.read_text(encoding="utf-8"))
        questions += count_questions(course, body)
        figures += len(figure_refs(body))
        body = namespace_references(body, md.stem)
        if course.parts:
            title = meta.get("title", md.stem).replace("Econometria \u2014 esame del ", "Esame del ")
            body = f"\\part{{{title}}}\n\n" + body
        pieces.append(body)
    stats = f"{len(paths)} {course.unit} \u00b7 {questions} domande"
    if figures:
        stats += f" \u00b7 {figures} figure"
    meta = {"title": course.volume_title, "subtitle": course.volume_subtitle, "stats": stats}
    return "\n\n".join(pieces), meta


# ------------------------------------------------------------------------ cli
def sources(course: Course) -> list[Path]:
    return sorted((course.sources_dir / "src").glob(course.pattern))


def list_course(course: Course) -> None:
    print(f"{course.slug}:")
    for p in sources(course):
        _meta, body = split_frontmatter(p.read_text(encoding="utf-8"))
        pdf = course.outdir / f"{p.stem}.pdf"
        print(f"  {p.stem:52s} {len(body.splitlines()):5d} righe  "
              f"{count_questions(course, body):3d} domande  {len(figure_refs(body)):2d} figure  "
              f"pdf:{'si' if pdf.exists() else 'no'}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--corso", action="append", choices=sorted(COURSES),
                    help="limita a un corso (ripetibile); di default tutti")
    ap.add_argument("--list", action="store_true", help="elenca i sorgenti e i PDF")
    ap.add_argument("--all", action="store_true", help="compila ogni sorgente")
    ap.add_argument("--exam", metavar="CHIAVE",
                    help="compila i sorgenti il cui nome contiene CHIAVE (es. 2023-12-21, 04)")
    ap.add_argument("--volume", action="store_true", help="compila anche il volume unico")
    ap.add_argument("--toc-depth", type=int, default=2)
    ap.add_argument("--keep", action="store_true", help="conserva i file .tex intermedi")
    args = ap.parse_args()

    courses = [COURSES[c] for c in args.corso] if args.corso else list(COURSES.values())
    if args.list or not (args.all or args.exam or args.volume):
        for course in courses:
            list_course(course)
        return 0

    built = 0
    for course in courses:
        todo = sources(course) if args.all else (
            [p for p in sources(course) if args.exam in p.stem] if args.exam else [])
        for p in todo:
            print(f"==> {p.stem}")
            meta, body = split_frontmatter(p.read_text(encoding="utf-8"))
            out = render(course, p.stem, body, meta, args.toc_depth, args.keep)
            print(f"    {out.relative_to(REPO)}")
            built += 1
        if args.volume and sources(course):
            print(f"==> {course.volume}")
            body, meta = volume_markdown(course)
            depth = max(args.toc_depth, 3) if course.parts else args.toc_depth
            out = render(course, course.volume, body, meta, depth, args.keep)
            print(f"    {out.relative_to(REPO)}")
            built += 1
    if not built:
        print(f"nessun sorgente corrisponde a {args.exam!r}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
