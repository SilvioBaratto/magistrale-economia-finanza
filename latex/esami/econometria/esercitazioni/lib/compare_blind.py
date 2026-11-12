"""Compare the answers of a blind solver with the answers of the exercise bank."""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

from . import config
from .bank import unit_tolerance

_EPS = 1e-9


@dataclass
class Report:
    """The outcome of a comparison, one list of ``<id>.<label>`` per kind of finding.

    Attributes:
        ok: Answers that agree.
        scarti: Answers that disagree or cannot be read.
        mancanti: Questions the solver did not answer.
        extra: Answers to questions the bank does not have.
    """

    ok: list[str] = field(default_factory=list)
    scarti: list[str] = field(default_factory=list)
    mancanti: list[str] = field(default_factory=list)
    extra: list[str] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        """Whether the two sets of answers agree completely."""
        return not (self.scarti or self.mancanti or self.extra)


def _number(value) -> float:
    if isinstance(value, str):
        value = value.replace(",", ".")
    return float(value)


def _decision(value) -> str:
    return re.sub(r"[^\w ]", "", str(value).lower()).strip()


def compare(banco: dict, cieco: dict) -> Report:
    """Compare the blind solver's answers with the bank's.

    Args:
        banco: ``{id: {label: {"valore", "decimali", "tolleranza"}}}``, the
            student-path answers written by the build.
        cieco: ``{id: {label: value}}`` from the solver. Numbers may be written
            with a decimal comma; decisions are compared ignoring case and punctuation.

    Returns:
        A :class:`Report`. A number agrees within its tolerance, which defaults
        to one unit of the last printed digit and to zero for a whole number shown without decimals.
    """
    report = Report()
    for id_, labels in banco.items():
        given = cieco.get(id_, {})
        for label, spec in labels.items():
            key = f"{id_}.{label}"
            if label not in given:
                report.mancanti.append(key)
                continue
            if spec["decimali"] is None:
                agree = _decision(given[label]) == _decision(spec["valore"])
            else:
                tol = spec["tolleranza"]
                tol = (unit_tolerance(spec["valore"], spec["decimali"]) if tol is None else tol) + _EPS
                try:
                    agree = abs(_number(given[label]) - spec["valore"]) <= tol
                except (TypeError, ValueError):
                    agree = False
            (report.ok if agree else report.scarti).append(key)
    for id_, labels in cieco.items():
        for label in labels:
            if label not in banco.get(id_, {}):
                report.extra.append(f"{id_}.{label}")
    return report


def main(argv: list[str], *, answers_dir: Path | None = None) -> int:
    """Run the comparison from the command line.

    Args:
        argv: ``[NN, cieco.json]`` where ``NN`` names the bank answers file.
        answers_dir: Folder with the bank answers; defaults to the build folder.

    Returns:
        0 when the answers agree, 1 otherwise.
    """
    name, blind_path = argv
    folder = answers_dir or config.BUILD / "answers"
    banco = json.loads((folder / f"{name}.json").read_text(encoding="utf-8"))
    cieco = json.loads(Path(blind_path).read_text(encoding="utf-8"))
    report = compare(banco, cieco)
    print(f"ok: {len(report.ok)}")
    for kind in ("scarti", "mancanti", "extra"):
        for key in getattr(report, kind):
            print(f"{kind}: {key}")
    return 0 if report.passed else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
