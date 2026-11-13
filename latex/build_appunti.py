#!/usr/bin/env python3
"""Merge the lecture notes of each course into one PDF, in chronological order.

Reads ``../obsidian/<NN-Corso>/appunti/*.md`` (written by the ``appunti-lezione`` skill) and
writes ``../dispense/appunti/<NN-corso>.pdf``: one chapter per lecture, titled with the
lecture date, set with the same template and filter as the dispense. Nothing is written back
into ``../obsidian/``.

With ``--variant fedele`` it reads ``appunti-fedeli/`` instead and writes
``../dispense/appunti-fedeli/<NN-corso>.pdf``: the near-verbatim notes, with their
``==highlights==`` in yellow and the figures they embed. ``--variant sintetico`` does the same
for the bullet-point summaries in ``appunti-sintetici/``.

    python3 build_appunti.py --list
    python3 build_appunti.py --all
    python3 build_appunti.py --subject 01-Econometria
    python3 build_appunti.py --variant fedele --subject 11-Finanza-Strategica
    python3 build_appunti.py --variant sintetico --subject 11-Finanza-Strategica
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple

import build

MONTHS = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio", "agosto",
          "settembre", "ottobre", "novembre", "dicembre"]

# The shared filter maps tip/abstract/example/note to numbered theorem-like blocks and sends any
# other kind to a plain "Nota" block. The lecture notes use Obsidian's tip/warning/question for
# exam hints, corrections and doubts, which must not come out as "Teorema" or "Dimostrazione",
# so they are renamed to kinds the filter does not know and keep their own label.
CALLOUT_LABELS: Dict[str, Tuple[str, str]] = {
    "tip": ("esame", "Esame"),
    "warning": ("correzione", "Correzione"),
    "question": ("verifica", "Da verificare"),
}

HIGHLIGHT_RE = re.compile(r"==([^=\n]+?)==")

# soul's \hl draws the marker behind the text and still breaks across lines, which a
# \colorbox would not. The colour is a pale yellow that prints legibly in grey as well.
HIGHLIGHT_PREAMBLE = ("\\usepackage{soul}\\definecolor{evidenzia}{RGB}{255,240,102}"
                      "\\sethlcolor{evidenzia}")


@dataclass(frozen=True)
class Variant:
    """One kind of lecture note and how its merged PDF is set.

    Attributes:
        folder: Folder of the course vault holding the notes.
        out_name: Folder of ``dispense/`` receiving the PDFs; also the intermediate-file prefix.
        subtitle: Subtitle of the title page.
        disclaimer: Note printed on the title page.
        highlights: Whether ``==marks==`` become yellow highlights. Tied to ``extra_pandoc``
            loading the package that draws them: converting without it would stop LaTeX.
        extra_pandoc: Extra pandoc arguments for this variant.
    """

    folder: str
    out_name: str
    subtitle: str
    disclaimer: str
    highlights: bool = False
    extra_pandoc: Tuple[str, ...] = ()


VARIANTS: Dict[str, Variant] = {
    "appunti": Variant(
        folder="appunti",
        out_name="appunti",
        subtitle="Appunti delle lezioni, in ordine cronologico",
        disclaimer=("Appunti ricavati dalla registrazione delle lezioni: la trascrizione automatica è "
                    "stata riscritta in forma scritta senza alterarne il contenuto. I passaggi che il "
                    "riconoscimento vocale non permette di stabilire sono segnalati come «Da verificare». "
                    "Documento a uso personale di studio."),
    ),
    "sintetico": Variant(
        folder="appunti-sintetici",
        out_name="appunti-sintetici",
        subtitle="Sintesi a punti delle lezioni, in ordine cronologico",
        disclaimer=("Sintesi a punti delle lezioni, ricavata dalla trascrizione fedele della stessa "
                    "lezione: dice solo ciò che dice quel testo, con meno parole, e ne conserva i "
                    "titoli per ritrovare il passaggio completo. Le parti evidenziate sono ciò che il "
                    "docente sottolinea. I passaggi che il riconoscimento vocale non permette di "
                    "stabilire sono segnalati come «Da verificare». Documento a uso personale di studio."),
        highlights=True,
        extra_pandoc=("-V", f"header-includes={HIGHLIGHT_PREAMBLE}"),
    ),
    "fedele": Variant(
        folder="appunti-fedeli",
        out_name="appunti-fedeli",
        subtitle="Trascrizione fedele delle lezioni, in ordine cronologico",
        disclaimer=("Trascrizione delle lezioni ripulita da intercalari, false partenze e ripetizioni, "
                    "con le parole del docente. Le parti evidenziate sono ciò che il docente sottolinea "
                    "o che il testo mostra ripetuto. Le figure indicate come ricostruite dall'audio "
                    "non sono le slide. I passaggi che il riconoscimento vocale non permette di "
                    "stabilire sono segnalati come «Da verificare». Documento a uso personale di studio."),
        highlights=True,
        extra_pandoc=("-V", f"header-includes={HIGHLIGHT_PREAMBLE}"),
    ),
}


def italian_date(iso: str) -> str:
    """Format ``2026-11-10`` as ``10 novembre 2026``; return ``iso`` unchanged if malformed."""
    match = re.fullmatch(r"(\d{4})-(\d{2})-(\d{2})", iso)
    if not match:
        return iso
    year, month, day = (int(g) for g in match.groups())
    return f"{day} {MONTHS[month - 1]} {year}"


def normalize_callouts(lines: List[str]) -> List[str]:
    """Rename the lecture callouts and move any text on their first line into the body.

    ``> [!question] Da verificare: la trascrizione riporta ...`` would otherwise make the whole
    sentence the run-in head of the block.
    """
    out: List[str] = []
    for line in lines:
        match = build.CALLOUT_RE.match(line)
        if not match or match.group("kind").lower() not in CALLOUT_LABELS:
            out.append(line)
            continue
        kind, label = CALLOUT_LABELS[match.group("kind").lower()]
        if out and out[-1].strip():
            out.append("")  # two quoted blocks glued together would nest instead of following
        text = match.group("heading").strip()
        if text.lower().startswith(label.lower()):
            text = re.sub(r"^[\s:.\-–]+", "", text[len(label):])
        out.append(f"> [!{kind}] {label}")
        if text:
            # The label is run in with a full stop, so the sentence after it starts a new one.
            out.append(f"> {text[0].upper()}{text[1:]}" if text[0].islower() else f"> {text}")
    return out


def highlights_to_spans(text: str) -> str:
    """Rewrite ``==marked==`` as a pandoc span the LaTeX writer turns into ``\\hl{marked}``."""
    return HIGHLIGHT_RE.sub(r"[\1]{.mark}", text)


def split_title(body: str, fallback: str) -> Tuple[str, str]:
    """Return ``(title, rest)`` where the leading ``# title`` line is removed from the body."""
    lines = body.splitlines()
    for index, line in enumerate(lines):
        if line.strip():
            if line.startswith("# "):
                return line[2:].strip(), "\n".join(lines[index + 1:]).lstrip("\n")
            break
    return fallback, body


def chapter(path: Path, slug: str, highlights: bool = False) -> Tuple[str, str]:
    """Convert one lecture note to a pandoc chapter; return ``(sort_key, markdown)``.

    Args:
        path: The lecture note.
        slug: Course slug, used for anchors and image folders.
        highlights: Convert ``==marks==`` to highlight spans.
    """
    meta, body = build.split_frontmatter(path.read_text(encoding="utf-8"))
    day = str(meta.get("data", path.stem[:10]))
    title, body = split_title(body, path.stem)
    anchor = f"ch:{slug}-{build.slugify(path.stem)}"

    body = build.embed_images(build.Note(path=path, meta=meta, body=body, subject_slug=slug))
    if highlights:
        body = highlights_to_spans(body)
    text = build.fix_glyphs(build.escape_currency(build.resolve_wikilinks(body, {})))
    lines = build.convert_sliderefs(build.convert_callouts(normalize_callouts(text.splitlines())))
    lines = build.namespace_footnotes(lines, anchor)

    heading = build.fix_glyphs(f"Lezione del {italian_date(day)}: {title}")
    return f"{day} {path.name}", "\n".join([f"# {heading} {{#{anchor}}}", ""] + lines + [""])


def discover(vault: Path, folder_name: str) -> List[Tuple[Path, List[Path]]]:
    """Return ``(course folder, lecture notes)`` for every course with a ``folder_name`` folder."""
    courses = []
    for folder in sorted(p for p in vault.iterdir() if p.is_dir() and not p.name.startswith(".")):
        notes = sorted((folder / folder_name).glob("*.md")) if (folder / folder_name).is_dir() else []
        if notes:
            courses.append((folder, notes))
    return courses


def build_course(folder: Path, notes: List[Path], variant: Variant, toc_depth: int, keep: bool) -> Path:
    """Render the merged PDF of one course and return its path."""
    slug = build.slugify(folder.name)
    chapters = sorted(chapter(note, slug, variant.highlights) for note in notes)
    subject = build.load_subject(folder)
    name = subject.title if subject else folder.name[3:].replace("-", " ")
    meta = {
        "title": f"Appunti di {name}",
        "subtitle": variant.subtitle,
        "author": build.AUTHOR,
        "date": build.DATE,
        "university": build.UNIVERSITY,
        "department": build.DEPARTMENT,
        "degree": build.DEGREE,
        "stats": f"{len(chapters)} " + ("lezione" if len(chapters) == 1 else "lezioni"),
        "disclaimer": variant.disclaimer,
    }
    out_dir = build.PDFDIR / variant.out_name
    # The dispense of the same course use ``<slug>`` for their intermediates; a prefix keeps the
    # builds from overwriting each other's .md and .tex.
    rendered = build.render(f"{variant.out_name}-{slug}", "\n".join(md for _, md in chapters), meta,
                            toc_depth, keep, extra_pandoc=variant.extra_pandoc, pdf_dir=out_dir)
    final = out_dir / f"{slug}.pdf"
    shutil.move(str(rendered), str(final))
    return final


def select_courses(courses: List[Tuple[Path, List[Path]]], args: argparse.Namespace) -> List[Tuple[Path, List[Path]]]:
    """Return the courses the command line asks for; exit when none matches."""
    if args.all or not args.subject:
        return courses
    selected = [(f, n) for f, n in courses if f.name in args.subject or build.slugify(f.name) in args.subject]
    if not selected:
        raise SystemExit(f"no course matched {args.subject}")
    return selected


def main() -> int:
    """Parse arguments and build the requested courses."""
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--vault", type=Path, default=build.VAULT)
    parser.add_argument("--variant", choices=sorted(VARIANTS), default="appunti")
    parser.add_argument("--subject", action="append", default=[], help="course folder name (repeatable)")
    parser.add_argument("--all", action="store_true", help="build every course that has notes")
    parser.add_argument("--list", action="store_true", help="list courses and lecture counts")
    parser.add_argument("--toc-depth", type=int, default=1, help="1 = lectures only, 2 = also sections")
    parser.add_argument("--keep", action="store_true", help="keep intermediate .md and LaTeX aux files")
    args = parser.parse_args()
    variant = VARIANTS[args.variant]

    courses = discover(args.vault, variant.folder)
    if not courses:
        raise SystemExit(f"no {variant.folder}/ folder with notes in {args.vault}")
    if args.list:
        for folder, notes in courses:
            print(f"{folder.name:38s} {len(notes):3d} lezioni")
        return 0

    for d in (build.BUILD, build.TEXDIR, build.PDFDIR / variant.out_name):
        d.mkdir(parents=True, exist_ok=True)
    for folder, notes in select_courses(courses, args):
        print(f"==> {folder.name} ({len(notes)} lezioni)")
        pdf = build_course(folder, notes, variant, args.toc_depth, args.keep)
        print(f"    {pdf.relative_to(build.ROOT.parent)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
