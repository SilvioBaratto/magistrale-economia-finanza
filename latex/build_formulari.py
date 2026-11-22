#!/usr/bin/env python3
"""Build the PDFs of the formularies in ``../Formulari/``.

Each ``Formulario_<Corso>.md`` becomes ``Formulario_<Corso>.pdf`` in the same folder, set with
the template and filters of ``build_esami.py``. The front matter of a source (``title``,
``subtitle``, ``coursecode``, ``disclaimer``) fills its title page.

    python3 build_formulari.py --list
    python3 build_formulari.py --all
    python3 build_formulari.py --only Econometria
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path

import build_esami

FORMULARI = build_esami.REPO / "Formulari"
PATTERN = "Formulario_*.md"
TOC_DEPTH = 2

# A regular expression that cannot match: the title page would otherwise print a count of exam
# questions, and a formulary has none.
NO_QUESTIONS = r"(?!)"


@dataclass(frozen=True)
class FormulariCourse(build_esami.Course):
    """The formularies, which keep their sources and their PDFs in one folder.

    ``build_esami.Course`` looks for sources under ``latex/esami/<slug>/`` and writes PDFs under
    ``esami/<slug>/``; the formularies live together in ``Formulari/`` instead.
    """

    @property
    def sources_dir(self) -> Path:
        return FORMULARI

    @property
    def src_dir(self) -> Path:
        return FORMULARI

    @property
    def outdir(self) -> Path:
        return FORMULARI


COURSE = FormulariCourse(
    slug="formulari",
    pattern=PATTERN,
    coursecode="",
    disclaimer="",
    subtitle="",
    volume=None,
    volume_title="",
    volume_subtitle="",
    parts=False,
    question_re=NO_QUESTIONS,
    unit="",
    dated=False,
)


def main(argv: list[str] | None = None) -> int:
    """Run the command line.

    Args:
        argv: Arguments without the program name; ``sys.argv`` when omitted.

    Returns:
        The exit status: 0 on success, 1 when ``--only`` matches no source.
    """
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--list", action="store_true", help="list the sources and whether a PDF exists")
    ap.add_argument("--all", action="store_true", help="build every formulary")
    ap.add_argument("--only", metavar="KEY",
                    help="build the formularies whose file name contains KEY, ignoring case")
    ap.add_argument("--keep", action="store_true", help="keep the LaTeX intermediates")
    args = ap.parse_args(argv)

    todo = build_esami.sources(COURSE)
    if args.only:
        todo = [p for p in todo if args.only.lower() in p.stem.lower()]

    if args.list or not (args.all or args.only):
        for p in todo:
            has_pdf = (COURSE.outdir / f"{p.stem}.pdf").exists()
            print(f"{p.stem:36s} pdf:{'si' if has_pdf else 'no'}")
        return 0
    if not todo:
        print(f"no formulary matches {args.only!r}", file=sys.stderr)
        return 1

    for p in todo:
        print(f"==> {p.stem}")
        meta, body = COURSE.load(p)
        out = build_esami.render(COURSE, p.stem, body, meta, TOC_DEPTH, args.keep)
        print(f"    {out.relative_to(build_esami.REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
