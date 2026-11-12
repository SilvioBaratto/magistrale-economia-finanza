#!/usr/bin/env python3
"""Merge the lecture notes of each course into one PDF, in chronological order.

Reads ``../obsidian/<NN-Corso>/appunti/*.md`` (written by the ``appunti-lezione`` skill) and
writes ``../dispense/appunti/<NN-corso>.pdf``: one chapter per lecture, titled with the
lecture date, set with the same template and filter as the dispense. Nothing is written back
into ``../obsidian/``.

    python3 build_appunti.py --list
    python3 build_appunti.py --all
    python3 build_appunti.py --subject 01-Econometria
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path
from typing import Dict, List, Tuple

import build

APPUNTI_DIR = "appunti"
OUT_DIR = build.PDFDIR / "appunti"

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

DISCLAIMER = ("Appunti ricavati dalla registrazione delle lezioni: la trascrizione automatica è "
              "stata riscritta in forma scritta senza alterarne il contenuto. I passaggi che il "
              "riconoscimento vocale non permette di stabilire sono segnalati come «Da verificare». "
              "Documento a uso personale di studio.")


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


def split_title(body: str, fallback: str) -> Tuple[str, str]:
    """Return ``(title, rest)`` where the leading ``# title`` line is removed from the body."""
    lines = body.splitlines()
    for index, line in enumerate(lines):
        if line.strip():
            if line.startswith("# "):
                return line[2:].strip(), "\n".join(lines[index + 1:]).lstrip("\n")
            break
    return fallback, body


def chapter(path: Path, slug: str) -> Tuple[str, str]:
    """Convert one lecture note to a pandoc chapter; return ``(sort_key, markdown)``."""
    meta, body = build.split_frontmatter(path.read_text(encoding="utf-8"))
    day = str(meta.get("data", path.stem[:10]))
    title, body = split_title(body, path.stem)
    anchor = f"ch:{slug}-{build.slugify(path.stem)}"

    text = build.fix_glyphs(build.escape_currency(build.resolve_wikilinks(body, {})))
    lines = build.convert_sliderefs(build.convert_callouts(normalize_callouts(text.splitlines())))
    lines = build.namespace_footnotes(lines, anchor)

    heading = build.fix_glyphs(f"Lezione del {italian_date(day)}: {title}")
    return f"{day} {path.name}", "\n".join([f"# {heading} {{#{anchor}}}", ""] + lines + [""])


def discover(vault: Path) -> List[Tuple[Path, List[Path]]]:
    """Return ``(course folder, lecture notes)`` for every course with an ``appunti/`` folder."""
    courses = []
    for folder in sorted(p for p in vault.iterdir() if p.is_dir() and not p.name.startswith(".")):
        notes = sorted((folder / APPUNTI_DIR).glob("*.md")) if (folder / APPUNTI_DIR).is_dir() else []
        if notes:
            courses.append((folder, notes))
    return courses


def build_course(folder: Path, notes: List[Path], toc_depth: int, keep: bool) -> Path:
    """Render the merged PDF of one course and return its path."""
    slug = build.slugify(folder.name)
    chapters = sorted(chapter(note, slug) for note in notes)
    subject = build.load_subject(folder)
    name = subject.title if subject else folder.name[3:].replace("-", " ")
    meta = {
        "title": f"Appunti di {name}",
        "subtitle": "Appunti delle lezioni, in ordine cronologico",
        "author": build.AUTHOR,
        "date": build.DATE,
        "university": build.UNIVERSITY,
        "department": build.DEPARTMENT,
        "degree": build.DEGREE,
        "stats": f"{len(chapters)} " + ("lezione" if len(chapters) == 1 else "lezioni"),
        "disclaimer": DISCLAIMER,
    }
    # The dispense of the same course use ``<slug>`` for their intermediates; a prefix keeps the
    # two builds from overwriting each other's .md and .tex.
    work_slug = f"appunti-{slug}"
    rendered = build.render(work_slug, "\n".join(md for _, md in chapters), meta, toc_depth, keep,
                            pdf_dir=OUT_DIR)
    final = OUT_DIR / f"{slug}.pdf"
    shutil.move(str(rendered), str(final))
    return final


def main() -> int:
    """Parse arguments and build the requested courses."""
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--vault", type=Path, default=build.VAULT)
    parser.add_argument("--subject", action="append", default=[], help="course folder name (repeatable)")
    parser.add_argument("--all", action="store_true", help="build every course that has appunti")
    parser.add_argument("--list", action="store_true", help="list courses and lecture counts")
    parser.add_argument("--toc-depth", type=int, default=1, help="1 = lectures only, 2 = also sections")
    parser.add_argument("--keep", action="store_true", help="keep intermediate .md and LaTeX aux files")
    args = parser.parse_args()

    courses = discover(args.vault)
    if not courses:
        raise SystemExit(f"no appunti/ folder with notes in {args.vault}")
    if args.list:
        for folder, notes in courses:
            print(f"{folder.name:38s} {len(notes):3d} lezioni")
        return 0

    selected = courses if args.all or not args.subject else [
        (f, n) for f, n in courses if f.name in args.subject or build.slugify(f.name) in args.subject
    ]
    if not selected:
        raise SystemExit(f"no course matched {args.subject}")

    for d in (build.BUILD, build.TEXDIR, OUT_DIR):
        d.mkdir(parents=True, exist_ok=True)
    for folder, notes in selected:
        print(f"==> {folder.name} ({len(notes)} lezioni)")
        pdf = build_course(folder, notes, args.toc_depth, args.keep)
        print(f"    {pdf.relative_to(build.ROOT.parent)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
