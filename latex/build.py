#!/usr/bin/env python3
"""Build professional LaTeX/PDF dispense from the Obsidian vault.

One PDF per subject (folder of ../obsidian), plus an optional combined volume.

    python3 build.py --list
    python3 build.py --all
    python3 build.py --subject 01-Econometria
    python3 build.py --all --combined

Pipeline: Obsidian markdown -> normalized markdown -> pandoc (+lua filter,
custom template) -> XeLaTeX (latexmk) -> PDF.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VAULT = (ROOT.parent / "obsidian").resolve()
BUILD = ROOT / "build"
TEXDIR = ROOT / "tex"
IMGDIR = TEXDIR / "img"
# The PDFs leave latex/: the repository keeps sources here, outputs beside it.
PDFDIR = ROOT.parent / "dispense"
TEMPLATE = ROOT / "template" / "dispensa.latex"
FILTER = ROOT / "filters" / "callouts.lua"

UNIVERSITY = "Universit\u00e0 Ca' Foscari Venezia"
DEPARTMENT = "Dipartimento di Economia"
DEGREE = "Economia e Finanza"
AUTHOR = "Silvio Angelo Baratto Roldan"
DATE = "2026/2027"
DISCLAIMER = ("Appunti rielaborati dal materiale didattico ufficiale del corso. "
              "Documento a uso personale di studio.")

FENCE = ":" * 5

CALLOUT_RE = re.compile(r"^>\s*\[!(?P<kind>\w+)\][-+]?\s*(?P<heading>.*)$")
WIKILINK_RE = re.compile(r"\[\[([^\]|]+?)(?:\|([^\]]*?))?\]\]")
SLIDEREF_RE = re.compile(r"^\*\(((?:slide|pagina)[^)]*)\)\*\s*$", re.IGNORECASE)
FM_KEY_RE = re.compile(r"^(?P<key>[A-Za-z_][\w-]*):\s*(?P<val>.*)$")


# --------------------------------------------------------------------------- utils
def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def split_frontmatter(raw: str) -> tuple[dict, str]:
    """Minimal YAML front-matter reader (scalars + simple list items)."""
    if not raw.startswith("---\n"):
        return {}, raw
    end = raw.find("\n---", 3)
    if end == -1:
        return {}, raw
    head = raw[4:end]
    body = raw[end + 4:].lstrip("\n")
    meta: dict = {}
    current_list_key: str | None = None
    for line in head.splitlines():
        if not line.strip():
            continue
        if line.lstrip().startswith("- ") and current_list_key:
            meta.setdefault(current_list_key, []).append(line.lstrip()[2:].strip())
            continue
        m = FM_KEY_RE.match(line)
        if not m:
            continue
        key, val = m.group("key"), m.group("val").strip()
        if val == "":
            current_list_key = key
            meta.setdefault(key, [])
        else:
            current_list_key = None
            meta[key] = val.strip('"').strip("'")
    return meta, body


# --------------------------------------------------------------------------- model
@dataclass
class Note:
    path: Path
    meta: dict
    body: str
    subject_slug: str

    @property
    def stem(self) -> str:
        return self.path.stem

    @property
    def title(self) -> str:
        return self.meta.get("title") or self.stem

    @property
    def anchor(self) -> str:
        return f"ch:{self.subject_slug}-{slugify(self.stem)}"

    @property
    def is_index(self) -> bool:
        return "tipo/indice" in self.meta.get("tags", [])


@dataclass
class Subject:
    folder: Path
    hub: Note
    chapters: list[Note] = field(default_factory=list)

    @property
    def slug(self) -> str:
        return slugify(self.folder.name)

    @property
    def title(self) -> str:
        return self.hub.title

    @property
    def total_slides(self) -> int:
        total = 0
        for note in self.chapters:
            try:
                total += int(note.meta.get("pages", 0))
            except (TypeError, ValueError):
                pass
        return total


# --------------------------------------------------------------------------- loading
def load_subject(folder: Path) -> Subject | None:
    subject_slug = slugify(folder.name)
    notes: list[Note] = []
    for path in sorted(folder.glob("*.md")):
        meta, body = split_frontmatter(path.read_text(encoding="utf-8"))
        notes.append(Note(path=path, meta=meta, body=body, subject_slug=subject_slug))
    if not notes:
        return None

    hub = next((n for n in notes if n.is_index), None)
    if hub is None:
        hub = notes[0]

    by_stem = {n.stem: n for n in notes}
    ordered: list[Note] = []
    for target, _label in WIKILINK_RE.findall(hub.body):
        note = by_stem.get(target.strip())
        if note and note is not hub and note not in ordered:
            ordered.append(note)
    for note in notes:  # orphans not listed in the hub index
        if note is not hub and note not in ordered:
            ordered.append(note)

    return Subject(folder=folder, hub=hub, chapters=ordered)


def discover(vault: Path) -> list[Subject]:
    subjects = []
    for folder in sorted(p for p in vault.iterdir() if p.is_dir() and not p.name.startswith(".")):
        subject = load_subject(folder)
        if subject:
            subjects.append(subject)
    return subjects


# --------------------------------------------------------------------------- transform
# Glyphs missing from the text font (TeX Gyre Pagella): rewrite them, but only
# outside math spans, where unicode-math already handles them. Symbols go through
# \ensuremath, never $...$: a generated "$-$" right before a digit ("−97.000")
# cannot close, and pandoc pairs the dollars across the rest of the paragraph.
MATH_GLYPHS = {
    "\u2192": r"\rightarrow", "\u2794": r"\rightarrow", "\u21d2": r"\Rightarrow",
    "\u2194": r"\leftrightarrow", "\u2191": r"\uparrow", "\u2193": r"\downarrow",
    "\u21d1": r"\Uparrow", "\u21d3": r"\Downarrow",
    "\u2212": "-", "\u223c": r"\sim", "\u2248": r"\approx",
    "\u2265": r"\geq", "\u2264": r"\leq", "\u2208": r"\in", "\u22ee": r"\vdots",
    "\u25cf": r"\bullet",
    "\u03b1": r"\alpha", "\u03b2": r"\beta", "\u03b5": r"\varepsilon",
    "\u03bb": r"\lambda", "\u03bc": r"\mu", "\u03c1": r"\rho", "\u03c3": r"\sigma",
    "\u0394": r"\Delta", "\u03a0": r"\Pi",
}
TEXT_GLYPHS = {
    **{src: rf"\ensuremath{{{dst}}}" for src, dst in MATH_GLYPHS.items()},
    "\u2713": r"\ding{51}", "\u2717": r"\ding{55}",
    "\u25a0": r"\ding{110}", "\u25b2": r"\ding{115}",
    "\u2080": r"\textsubscript{0}", "\u2081": r"\textsubscript{1}", "\u2082": r"\textsubscript{2}",
}

# A currency dollar opens a math span that pandoc closes at the next dollar on
# the page, swallowing table cells on the way. "$29.68" is currency when its
# line holds no dollar that could close it before a cell border; "($)" always
# is. A closer needs a non-space before it and no digit after (pandoc's rule),
# and "($ USD" is currency too, never the end of a formula.
CURRENCY_RE = re.compile(r"(?<![\\$])\$(?=\d)")
CLOSER_RE = re.compile(r"(?<=[^\s\\(])\$(?!\d)")


def escape_currency(text: str) -> str:
    def escape_line(line: str) -> str:
        line = line.replace("($)", r"(\$)")
        # Outside a table row a "|" is an absolute value, not a cell border.
        table_row = line.lstrip("> ").startswith("|")
        cut = []
        for m in CURRENCY_RE.finditer(line):
            close = CLOSER_RE.search(line, m.end() + 1)
            if close is None or (table_row and "|" in line[m.end():close.start()]):
                cut.append(m.start())
        for pos in reversed(cut):
            line = line[:pos] + "\\" + line[pos:]
        return line

    out, in_fence = [], False
    for line in text.split("\n"):
        if line.lstrip("> ").startswith("```"):
            in_fence = not in_fence
        out.append(line if in_fence else escape_line(line))
    return "\n".join(out)


MATH_SPAN_RE = re.compile(r"(?<!\\)(\$\$(?:\\.|[^\\])*?\$\$|\$(?:\\.|[^$\\\n])+?\$)", re.DOTALL)

# Accented Latin letters have no math glyph and unicode-math falls back to a
# legacy font that lacks them too. A word holding one is a label (R_{liquidità}),
# so it is set as text.
LATIN = "A-Za-z\u00c0-\u00d6\u00d8-\u00f6\u00f8-\u024f"
ACCENTED_WORD_RE = re.compile(
    rf"(?<![\\{LATIN}])[{LATIN}]*[\u00c0-\u00d6\u00d8-\u00f6\u00f8-\u024f][{LATIN}]*")

# decimalcomma reads "1,5" as a decimal and "1, 5" as a list. Notes that write
# decimals as "0{,}30" use the bare comma as a separator, and so do runs such as
# "1,2,3" or "1,2,\ldots" and integer tuples such as N(0,1) or (1,0)': those
# commas get the space that marks them. A tuple part like "01" is a decimal
# fraction, as in S_0(1,01).
DIGIT_COMMA_RE = re.compile(r"(?<=\d),(?=\d)")
NUMBER_LIST_RE = re.compile(r"\b\d+(?:,\d+){2,}\b|\b\d+,\d+(?=,\s*\\[lc]?dots)")
INTEGER_TUPLE_RE = re.compile(r"\(-?\d+(?:,-?\d+)+\)")


def separate(match: re.Match) -> str:
    return match.group(0).replace(",", ", ")


def separate_tuple(match: re.Match) -> str:
    parts = match.group(0)[1:-1].split(",")[1:]
    if any(re.match(r"-?0\d", part) for part in parts):
        return match.group(0)
    return separate(match)


def fix_math(span: str) -> str:
    span = ACCENTED_WORD_RE.sub(r"\\text{\g<0>}", span)
    if "{,}" in span:
        return DIGIT_COMMA_RE.sub(", ", span)
    span = INTEGER_TUPLE_RE.sub(separate_tuple, span)
    return NUMBER_LIST_RE.sub(separate, span)


def fix_glyphs(text: str) -> str:
    def convert(chunk: str) -> str:
        for src, dst in TEXT_GLYPHS.items():
            chunk = chunk.replace(src, dst)
        return chunk
    return "".join(fix_math(part) if i % 2 else convert(part)
                   for i, part in enumerate(MATH_SPAN_RE.split(text)))


def convert_callouts(lines: list[str]) -> list[str]:
    """Obsidian callouts -> pandoc fenced divs (recursive for nested ones)."""
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
                # blank line ends the callout unless the quote continues after it
                if i + 1 < len(lines) and lines[i + 1].startswith(">"):
                    body.append("")
                    i += 1
                    continue
                break
            stripped = lines[i][1:]
            body.append(stripped[1:] if stripped.startswith(" ") else stripped)
            i += 1
        attrs = f'kind="{kind}"' + (f' heading="{heading}"' if heading else "")
        out.append("")
        out.append(f"{FENCE} {{.callout {attrs}}}")
        out.extend(convert_callouts(body))
        out.append(FENCE)
        out.append("")
    return out


def convert_sliderefs(lines: list[str]) -> list[str]:
    out: list[str] = []
    for line in lines:
        m = SLIDEREF_RE.match(line)
        if m:
            out.extend(["", f"{FENCE} {{.slideref}}", f"({m.group(1)})", FENCE, ""])
        else:
            out.append(line)
    return out


def resolve_wikilinks(text: str, anchors: dict[str, str]) -> str:
    def repl(m: re.Match) -> str:
        target = m.group(1).strip()
        label = (m.group(2) or target).strip()
        anchor = anchors.get(target)
        if anchor:
            return f"[{label}](#{anchor})"
        return label
    return WIKILINK_RE.sub(repl, text)


IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)\)")
EMBED_RE = re.compile(r"!\[\[([^\]|]+?\.(?:png|jpe?g|pdf))(?:\|[^\]]*)?\]\]", re.IGNORECASE)


def embed_images(note: Note) -> str:
    """Copy the images a note embeds next to the .tex and point its links there.

    LaTeX runs in tex/, away from the vault, and the vault path holds spaces
    that \\includegraphics does not take; the copies get plain names. Obsidian
    embeds (``![[fig.png]]``) are found by file name under the note's folder,
    as Obsidian resolves them. A missing image is dropped with a warning
    rather than stopping LaTeX.

    Args:
        note: The note whose body is rewritten.

    Returns:
        The body with every local image pointing into ``tex/img/``.
    """
    def place(src: Path, alt: str) -> str:
        # A PNG kept for Obsidian may have a vector twin: LaTeX takes the PDF.
        if src.suffix.lower() == ".png" and src.with_suffix(".pdf").is_file():
            src = src.with_suffix(".pdf")
        if not src.is_file():
            print(f"    ! immagine mancante in {note.path.name}: {src}", file=sys.stderr)
            return ""
        dest = IMGDIR / note.subject_slug / f"{slugify(note.stem)}-{slugify(src.stem)}{src.suffix.lower()}"
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
        return f"![{alt}]({dest.relative_to(TEXDIR).as_posix()})"

    def markdown_image(m: re.Match) -> str:
        if re.match(r"[a-z]+://", m.group(2)):
            return m.group(0)
        return place(note.path.parent / m.group(2), m.group(1))

    def obsidian_embed(m: re.Match) -> str:
        hits = sorted(note.path.parent.rglob(Path(m.group(1)).name))
        return place(hits[0] if hits else note.path.parent / m.group(1), "")

    return IMAGE_RE.sub(markdown_image, EMBED_RE.sub(obsidian_embed, note.body))


FOOTNOTE_RE = re.compile(r"\[\^([^\]\s]+)\]")


def namespace_footnotes(lines: list[str], anchor: str) -> list[str]:
    """Prefix every footnote label with the chapter anchor.

    All chapters land in one .md, so two chapters both using `[^1]` collide and
    pandoc drops one ("Duplicate note reference"). Labels are chapter-local by
    nature, so scoping them to the anchor is enough. Fenced code is left alone.
    """
    out: list[str] = []
    in_fence = False
    for line in lines:
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            out.append(line)
            continue
        out.append(line if in_fence else FOOTNOTE_RE.sub(rf"[^{anchor}-\1]", line))
    return out


def chapter_markdown(note: Note, anchors: dict[str, str], with_source: bool) -> str:
    body = fix_glyphs(escape_currency(resolve_wikilinks(embed_images(note), anchors)))
    lines = convert_sliderefs(convert_callouts(body.splitlines()))
    lines = namespace_footnotes(lines, note.anchor)
    parts = [f"# {fix_glyphs(note.title)} {{#{note.anchor}}}", ""]
    if with_source and note.meta.get("source"):
        src = note.meta["source"].replace("_", r"\_")
        pages = note.meta.get("pages")
        unit = "pagine" if "_Appunti_" in note.meta["source"] else "slide"
        tail = f" \u2014 {pages} {unit}" if pages else ""
        parts += ["", f"{FENCE} {{.chapsource}}", f"Fonte: *{src}*{tail}", FENCE, ""]
    parts += lines + [""]
    return "\n".join(parts)


def subject_markdown(subject: Subject, anchors: dict[str, str], with_source: bool) -> str:
    return "\n".join(chapter_markdown(n, anchors, with_source) for n in subject.chapters)


def build_anchor_map(subjects: list[Subject]) -> dict[str, str]:
    """stem/title -> anchor, for every non-index note in the vault."""
    anchors: dict[str, str] = {}
    for subject in subjects:
        for note in subject.chapters:
            anchors[note.stem] = note.anchor
            anchors.setdefault(note.title, note.anchor)
    return anchors


# --------------------------------------------------------------------------- render
def run(cmd: list[str], cwd: Path | None = None) -> None:
    proc = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if proc.returncode != 0:
        sys.stderr.write(proc.stdout[-8000:])
        sys.stderr.write(proc.stderr[-8000:])
        raise SystemExit(f"command failed ({proc.returncode}): {' '.join(cmd[:3])} ...")
    if proc.stderr.strip():
        for line in proc.stderr.strip().splitlines():
            if "warning" in line.lower() or "Missing" in line:
                print(f"    ! {line}", file=sys.stderr)


def render(slug: str, markdown: str, meta: dict[str, str], toc_depth: int, keep: bool) -> Path:
    md_path = BUILD / f"{slug}.md"
    tex_path = TEXDIR / f"{slug}.tex"
    md_path.write_text(markdown, encoding="utf-8")

    cmd = [
        "pandoc", str(md_path),
        "--from", "markdown+fenced_divs+header_attributes+tex_math_dollars+pipe_tables+raw_tex"
                    "+autolink_bare_uris-implicit_figures",
        "--to", "latex",
        "--standalone",
        "--template", str(TEMPLATE),
        "--lua-filter", str(FILTER),
        "--top-level-division=chapter",
        "--toc", f"--toc-depth={toc_depth}",
        "--wrap=preserve",
        # report class: chapter=0, section=1 -> shift the user-facing depth
        "-V", f"toc-depth={max(toc_depth - 1, 0)}",
        "-o", str(tex_path),
    ]
    for key, value in meta.items():
        cmd += ["-M", f"{key}={value}"]
    run(cmd)

    aux = TEXDIR / f".aux-{slug}"
    aux.mkdir(exist_ok=True)
    run(["latexmk", "-xelatex", "-interaction=nonstopmode", "-file-line-error",
         "-halt-on-error", f"-outdir={aux}", tex_path.name], cwd=TEXDIR)

    pdf_src = aux / f"{slug}.pdf"
    pdf_dst = PDFDIR / f"{slug}.pdf"
    shutil.copy2(pdf_src, pdf_dst)
    if not keep:
        shutil.rmtree(aux, ignore_errors=True)
        md_path.unlink(missing_ok=True)
    return pdf_dst


def subject_meta(subject: Subject) -> dict[str, str]:
    stats = f"{len(subject.chapters)} capitoli"
    if subject.total_slides:
        stats += f" \u00b7 {subject.total_slides} slide di riferimento"
    return {
        "title": subject.title,
        "subtitle": "Dispensa del corso",
        "author": AUTHOR,
        "date": DATE,
        "university": UNIVERSITY,
        "department": DEPARTMENT,
        "degree": DEGREE,
        "stats": stats,
        "disclaimer": DISCLAIMER,
    }


# --------------------------------------------------------------------------- cli
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--vault", type=Path, default=VAULT, help="Obsidian vault root")
    ap.add_argument("--subject", action="append", default=[], help="folder name (repeatable)")
    ap.add_argument("--all", action="store_true", help="build every subject")
    ap.add_argument("--combined", action="store_true", help="also build one volume with all subjects")
    ap.add_argument("--list", action="store_true", help="list subjects and chapter counts")
    ap.add_argument("--toc-depth", type=int, default=1,
                    help="1 = solo capitoli (default), 2 = anche le sezioni")
    ap.add_argument("--no-sources", action="store_true", help="omit the source-file line under each chapter")
    ap.add_argument("--keep", action="store_true", help="keep intermediate .md and LaTeX aux files")
    args = ap.parse_args()

    for d in (BUILD, TEXDIR, PDFDIR):
        d.mkdir(exist_ok=True)

    subjects = discover(args.vault)
    if not subjects:
        raise SystemExit(f"no subjects found in {args.vault}")

    if args.list:
        for s in subjects:
            print(f"{s.folder.name:38s} {len(s.chapters):3d} capitoli  ({s.title})")
        return 0

    anchors = build_anchor_map(subjects)
    with_source = not args.no_sources

    selected = subjects if args.all or not args.subject else [
        s for s in subjects if s.folder.name in args.subject or s.slug in args.subject
    ]
    if not selected:
        raise SystemExit(f"no subject matched {args.subject}")

    for subject in selected:
        print(f"==> {subject.title} ({len(subject.chapters)} capitoli)")
        pdf = render(subject.slug, subject_markdown(subject, anchors, with_source),
                     subject_meta(subject), args.toc_depth, args.keep)
        print(f"    {pdf.relative_to(ROOT.parent)}")

    if args.combined:
        print("==> Volume unico")
        chunks = []
        for subject in subjects:
            chunks.append(f"\\part{{{subject.title}}}\n")
            chunks.append(subject_markdown(subject, anchors, with_source))
        meta = {
            "title": "Economia e Finanza",
            "subtitle": "Dispense complete del corso di laurea magistrale",
            "author": AUTHOR, "date": DATE,
            "university": UNIVERSITY, "department": DEPARTMENT, "degree": DEGREE,
            "stats": f"{len(subjects)} insegnamenti \u00b7 "
                     f"{sum(len(s.chapters) for s in subjects)} capitoli",
            "disclaimer": DISCLAIMER,
        }
        pdf = render("00-dispense-complete", "\n".join(chunks), meta, args.toc_depth, args.keep)
        print(f"    {pdf.relative_to(ROOT.parent)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
