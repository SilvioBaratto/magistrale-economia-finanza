"""Check the exercises against the taxonomy of exam question types."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Iterable

_JSON_BLOCK = re.compile(r"```json\n(.*?)\n```", re.S)


def load_tassonomia(path: Path) -> list[dict]:
    """Return the question types listed in the first JSON block of ``TASSONOMIA.md``.

    Each type has ``id``, ``modulo``, ``origine``, ``descrizione`` and
    ``occorrenze``. ``origine`` is ``appello`` (asked in the past exams),
    ``ripasso`` (one of the statistics reviews) or ``corso`` (taught by the
    notes or the official 2024-01-16 solution but never asked in the 70 questions).
    """
    block = _JSON_BLOCK.search(path.read_text(encoding="utf-8"))
    if block is None:
        raise ValueError(f"{path}: nessun blocco json")
    return json.loads(block.group(1))["tipi"]


def matrice(tipi: list[dict], esercizi: Iterable) -> tuple[str, list[str]]:
    """Build the coverage matrix and the list of rules it breaks.

    Args:
        tipi: Question types from :func:`load_tassonomia`.
        esercizi: Objects with ``id``, ``livello`` and ``tipo``, which is a type id
            or a tuple of them: an exercise testing two competences covers both.

    Returns:
        A Markdown table (type, module, origin, count, levels, exercises) and the
        problems: an exam type (``appello``) with fewer than two exercises or none
        at level 3, a ``ripasso`` or ``corso`` topic with none, an exercise typed
        with an id the taxonomy lacks.
    """
    by_type: dict[str, list] = {t["id"]: [] for t in tipi}
    problems = []
    for e in esercizi:
        for tipo in (e.tipo,) if isinstance(e.tipo, str) else e.tipo:
            if tipo in by_type:
                by_type[tipo].append(e)
            else:
                problems.append(f"tipo sconosciuto {tipo} nell'esercizio {e.id}")
    rows = ["| tipo | modulo | origine | n | livelli | esercizi |", "|---|---|---|---|---|---|"]
    for t in tipi:
        found = by_type[t["id"]]
        levels = sorted({e.livello for e in found})
        rows.append(f"| {t['id']} | {t['modulo']} | {t['origine']} | {len(found)} | "
                    f"{','.join(map(str, levels))} | {', '.join(e.id for e in found)} |")
        if t["origine"] != "appello":
            if not found:
                problems.append(f"{t['id']}: nessun esercizio per questo argomento ({t['origine']})")
        else:
            if len(found) < 2:
                problems.append(f"{t['id']}: {len(found)} esercizi, ne servono almeno 2")
            if 3 not in levels:
                problems.append(f"{t['id']}: manca un esercizio di livello 3")
    return "\n".join(rows), problems
