"""Exercise registry and the checks every exercise passes before it is rendered."""

from __future__ import annotations

import math
import zlib
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Literal, Union

import numpy as np

from . import config
from .gretl import Table, parse_table

Decisione = Literal["rifiuta", "non rifiuta", "sì", "no"]

# Beyond one unit of the last printed digit the student's rounding, not the
# exercise, would decide whether an answer is right; the epsilon absorbs float noise.
_EPS = 1e-9


@dataclass(frozen=True)
class Numero:
    """A number together with the decimals it is shown with.

    Attributes:
        valore: The value, at full precision unless it comes from a printed table.
        decimali: Decimals shown in the text; also sets the answer tolerance.
    """

    valore: float
    decimali: int

    def _fixed(self) -> str:
        text = f"{self.valore:.{self.decimali}f}"
        # A value that rounds to zero must not keep its sign ("-0,00").
        return text.lstrip("-") if float(text) == 0 else text

    def testo(self) -> str:
        """Return the number for running text, with a decimal comma."""
        return self._fixed().replace(".", ",")

    def tex(self) -> str:
        """Return the number for math mode, where the comma needs braces."""
        return self._fixed().replace(".", "{,}")


Risposta = Union[Numero, str]


@dataclass(frozen=True)
class Quesito:
    """A labelled question of the exercise text whose answer is checked blind.

    Attributes:
        chiave: Key of the answer in ``Draft.risposte``.
        tolleranza: Absolute tolerance; ``None`` means one unit of the last digit.
    """

    chiave: str
    tolleranza: float | None = None


@dataclass(frozen=True)
class Margin:
    """A test statistic that must stay clear of its critical value.

    Attributes:
        stat: Observed statistic.
        crit: Critical value it is compared with.
        rel: Fraction of ``crit`` the statistic must stay away from it.
    """

    stat: float
    crit: float
    rel: float = config.MARGINE_BORDERLINE


@dataclass
class Draft:
    """What an exercise function returns before the checks run.

    Attributes:
        dati: The synthetic dataset, kept for the figures.
        parametri: Numbers the student sees in the text (n, level, hypothesised value).
        tabelle: Printed tables by name, in Markdown.
        risposte: Truth computed from the data.
        studente: Recomputes the answers from the parsed printed tables only.
        quesiti: Question label in the text to the answer it asks for.
        attese: Predicates on ``risposte`` that pin the story of the exercise.
        margini: Statistics that must not be borderline.
        figure: Figure name to a function that writes the PDF at a given path.
    """

    dati: Any
    parametri: dict[str, Numero]
    tabelle: dict[str, str]
    risposte: dict[str, Risposta]
    studente: Callable[[dict[str, Table]], dict[str, Risposta]]
    quesiti: dict[str, Quesito]
    attese: list[Callable[[dict[str, Risposta]], bool]] = field(default_factory=list)
    margini: list[Margin] = field(default_factory=list)
    figure: dict[str, Callable[[Path], None]] = field(default_factory=dict)


@dataclass
class Exercise:
    """A built exercise: its metadata, its draft and the student-path answers.

    Attributes:
        id: Unique identifier, also the prefix of its figure files.
        modulo: Module number (an appello ``N`` uses ``7 + N``).
        livello: 1 base, 2 intermediate, 3 exam level.
        tipo: Question type from the taxonomy, or a tuple of them when the
            exercise tests several competences.
        punti: Points the question would be worth in an exam.
        draft: The draft the exercise function returned.
        studente: Answers recomputed from the printed tables.
        figure_path: Figure name to the file written for it.
    """

    id: str
    modulo: int
    livello: int
    tipo: str | tuple[str, ...]
    punti: int
    draft: Draft
    studente: dict[str, Risposta]
    figure_path: dict[str, Path] = field(default_factory=dict)

    @property
    def parametri(self) -> dict[str, Numero]:
        """Numbers visible to the student."""
        return self.draft.parametri

    @property
    def tabelle(self) -> dict[str, str]:
        """Printed tables by name."""
        return self.draft.tabelle

    @property
    def risposte(self) -> dict[str, Risposta]:
        """Truth computed from the data."""
        return self.draft.risposte

    @property
    def quesiti(self) -> dict[str, Quesito]:
        """Labelled questions of the text."""
        return self.draft.quesiti


class ExerciseError(Exception):
    """Raised when a module has exercises that fail their checks.

    Attributes:
        problemi: One line per problem, prefixed with the exercise id.
    """

    def __init__(self, problemi: list[str]):
        super().__init__("\n".join(problemi))
        self.problemi = problemi


@dataclass(frozen=True)
class _Entry:
    id: str
    modulo: int
    livello: int
    tipo: str | tuple[str, ...]
    punti: int
    fn: Callable[[np.random.Generator], Draft]


_REGISTRY: dict[str, _Entry] = {}


def unit_tolerance(valore: float, decimali: int) -> float:
    """Return the default tolerance of an answer: one unit of its last shown digit.

    A whole number shown with no decimals (degrees of freedom, a lag order, a count)
    has tolerance zero: being one off is the classic mistake, not a rounding.
    """
    if decimali == 0 and float(valore).is_integer():
        return 0.0
    return 10.0 ** -decimali


def seed_for(id: str) -> int:
    """Return the fixed seed of an exercise, so a rebuild reproduces its data."""
    return zlib.crc32(id.encode())


def exercise(id: str, *, modulo: int, livello: int, tipo: str | tuple[str, ...], punti: int = 3):
    """Register a function ``f(rng) -> Draft`` as an exercise.

    Args:
        id: Unique identifier, lowercase with digits and underscores.
        modulo: Module number (an appello ``N`` uses ``7 + N``).
        livello: 1 base, 2 intermediate, 3 exam level.
        tipo: Question type from the taxonomy, or a tuple of them for an
            exercise that tests several competences.
        punti: Points the question would be worth.

    Raises:
        ValueError: If ``id`` is already registered or ``livello`` is not 1-3.
    """
    if livello not in (1, 2, 3):
        raise ValueError(f"{id}: livello {livello} non valido")

    def register(fn):
        """Store ``fn`` under ``id`` and return it unchanged."""
        if id in _REGISTRY:
            raise ValueError(f"id duplicato: {id}")
        _REGISTRY[id] = _Entry(id, modulo, livello, tipo, punti, fn)
        return fn

    return register


def clear_registry() -> None:
    """Empty the registry, for tests and for modules that are loaded twice."""
    _REGISTRY.clear()


def verify(ex: Exercise) -> list[str]:
    """Check one built exercise against its own truth, expectations and margins.

    Args:
        ex: The exercise with its student-path answers already computed.

    Returns:
        One line per problem; empty when the exercise is sound.
    """
    draft, problems = ex.draft, []
    # NaN and infinity compare false with everything, so no tolerance or margin test would ever fire.
    for where, values in (("parametro", draft.parametri), ("verità", draft.risposte),
                          ("percorso studente", ex.studente)):
        for key, value in values.items():
            if isinstance(value, Numero) and not math.isfinite(value.valore):
                problems.append(f"{key}: valore non finito nel {where}")
    for m in draft.margini:
        if not (math.isfinite(m.stat) and math.isfinite(m.crit)):
            problems.append(f"margine con valore non finito: stat={m.stat}, crit={m.crit}")
    # The renderer reads parameters first, so a shared key would hide the answer
    # in the solution and leak it into the exercise text.
    for key in sorted(set(draft.parametri) & set(draft.risposte)):
        problems.append(f"{key}: chiave sia parametro sia risposta")
    for key, truth in draft.risposte.items():
        if key not in ex.studente:
            problems.append(f"{key}: manca nel percorso studente")
            continue
        got = ex.studente[key]
        if isinstance(truth, Numero):
            if not isinstance(got, Numero):
                problems.append(f"{key}: il percorso studente non è un numero")
            elif abs(got.valore - truth.valore) > unit_tolerance(truth.valore, truth.decimali) + _EPS:
                problems.append(f"{key}: percorso studente {got.valore} lontano dalla verità "
                                f"{truth.valore} (tolleranza {unit_tolerance(truth.valore, truth.decimali)})")
        elif got != truth:
            problems.append(f"{key}: decisione dello studente {got!r} diversa dalla verità {truth!r}")
    for label, quesito in draft.quesiti.items():
        if quesito.chiave not in draft.risposte:
            problems.append(f"quesito {label}: la risposta {quesito.chiave} non esiste")
    for i, check in enumerate(draft.attese):
        if not check(draft.risposte):
            problems.append(f"attesa violata: {getattr(check, '__name__', i)}")
    for m in draft.margini:
        if abs(abs(m.stat) - abs(m.crit)) < m.rel * abs(m.crit):
            problems.append(f"esito borderline: |{m.stat}| troppo vicino al valore critico {m.crit}")
    return problems


def build_all(modulo: int, figdir: Path) -> list[Exercise]:
    """Build, verify and draw every registered exercise of one module.

    Args:
        modulo: Module number to build.
        figdir: Folder for the figures, written as ``<id>_<name>.pdf``.

    Returns:
        The exercises in registration order.

    Raises:
        ExerciseError: With every problem found; no figure is written then.
    """
    built, problems = [], []
    for entry in (e for e in _REGISTRY.values() if e.modulo == modulo):
        draft = entry.fn(np.random.default_rng(seed_for(entry.id)))
        tables = {name: parse_table(text) for name, text in draft.tabelle.items()}
        ex = Exercise(entry.id, entry.modulo, entry.livello, entry.tipo, entry.punti,
                      draft, draft.studente(tables))
        problems += [f"{entry.id}: {p}" for p in verify(ex)]
        built.append(ex)
    levels = [e.livello for e in built]
    if levels != sorted(levels):
        problems.append(f"modulo {modulo}: livelli non in ordine crescente {levels}")
    if problems:
        raise ExerciseError(problems)
    for ex in built:
        figdir.mkdir(parents=True, exist_ok=True)
        for name, write in ex.draft.figure.items():
            ex.figure_path[name] = figdir / f"{ex.id}_{name}.pdf"
            write(ex.figure_path[name])
    return built
