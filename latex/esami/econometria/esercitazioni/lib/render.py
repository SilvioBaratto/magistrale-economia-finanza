"""Expand the placeholders of the exercise templates and assemble module sources."""

from __future__ import annotations

import os
import re

from .bank import Exercise, Numero
from .config import ROOT

# Deliberately strict: LaTeX is full of "{{" (\frac{{a}}{b}, x_{{i}}) and only
# a dotted id.key or testo:id may ever be read as a placeholder.
PLACEHOLDER_RE = re.compile(
    r"\{\{(?:testo:(?P<tid>[a-z]\w*)"
    r"|(?P<id>[a-z]\w*)\.(?:(?P<kind>tab|fig)\.(?P<name>[A-Za-z_]\w*)"
    r"|(?P<key>[A-Za-z_]\w*)(?P<m>\|m)?))\}\}"
)
# What is left of a placeholder that PLACEHOLDER_RE rejected (a space, a wrong case, a bad suffix).
# Plain LaTeX braces such as \\frac{{a}}{b} never have "name." or "testo:" right after them.
_LEFTOVER_RE = re.compile(r"\{\{\s*(?:testo\s*:|[A-Za-z]\w*\s*\.)")
SECTION_RE = re.compile(r"<!--\s*ex\s+([a-z]\w*)\s*-->\n?(.*?)\n?<!--\s*/ex\s*-->", re.S)
_QUOTE_RE = re.compile(r"^\s*(?:>\s?)*")


class RenderError(ValueError):
    """A placeholder that cannot be resolved, or one that is not allowed where it stands."""


def extract_sections(esercizi_tpl: str) -> dict[str, str]:
    """Return the text of each exercise, keyed by the id in its ``<!-- ex ID -->`` markers.

    Raises:
        RenderError: If two sections share an id.
    """
    sections: dict[str, str] = {}
    for m in SECTION_RE.finditer(esercizi_tpl):
        if m.group(1) in sections:
            raise RenderError(f"sezione duplicata: {m.group(1)}")
        sections[m.group(1)] = m.group(2)
    return sections


def _resolve(m: re.Match, ex: dict[str, Exercise], soluzioni: bool, sezioni: dict[str, str]) -> str:
    if m["tid"]:
        if not soluzioni:
            raise RenderError(f"{{{{testo:{m['tid']}}}}} è ammesso solo nelle soluzioni")
        if m["tid"] not in sezioni:
            raise RenderError(f"sezione dell'esercizio {m['tid']} non trovata")
        return expand(sezioni[m["tid"]], ex, soluzioni=False, sezioni=sezioni)
    if m["id"] not in ex:
        raise RenderError(f"id sconosciuto: {m['id']}")
    e = ex[m["id"]]
    if m["kind"] == "tab":
        if m["name"] not in e.tabelle:
            raise RenderError(f"tabella sconosciuta: {m['id']}.{m['name']}")
        return e.tabelle[m["name"]]
    if m["kind"] == "fig":
        path = e.figure_path.get(m["name"])
        if path is None:
            raise RenderError(f"figura sconosciuta: {m['id']}.{m['name']}")
        if not path.exists():
            raise RenderError(f"figura mancante: {path}")
        return os.path.relpath(path, ROOT)
    key = m["key"]
    if key in e.parametri:
        value = e.parametri[key]
    elif key in e.risposte:
        if not soluzioni:
            raise RenderError(f"risposta nel testo dell'esercizio: {m['id']}.{key}")
        value = e.studente[key]
    else:
        raise RenderError(f"chiave sconosciuta: {m['id']}.{key}")
    if isinstance(value, str):
        return value
    return value.tex() if m["m"] else value.testo()


def expand(text: str, ex: dict[str, Exercise], *, soluzioni: bool, sezioni: dict[str, str]) -> str:
    """Replace every placeholder in ``text``.

    Args:
        text: Template text.
        ex: Built exercises by id.
        soluzioni: Whether answers and ``{{testo:id}}`` are allowed; the exercise
            text must never contain an answer.
        sezioni: Exercise sections, for ``{{testo:id}}``.

    Returns:
        The text with numbers, tables and figure paths filled in. A multi-line
        expansion keeps the blockquote marker of the line it sits on, so a table
        inside a callout stays inside it.

    Raises:
        RenderError: On any reference that does not resolve, or a placeholder written
            almost right (extra space, wrong case) that would reach the PDF as literal braces.
    """
    lines = []
    for line in text.split("\n"):
        prefix = _QUOTE_RE.match(line).group(0)
        lines.append(PLACEHOLDER_RE.sub(
            lambda m: _resolve(m, ex, soluzioni, sezioni).replace("\n", "\n" + prefix), line))
    out = "\n".join(lines)
    leftover = _LEFTOVER_RE.search(out)
    if leftover:
        raise RenderError(f"segnaposto non riconosciuto: {out[leftover.start():leftover.start() + 40]!r}")
    return out


def render_module(esercizi_tpl: str, soluzioni_tpl: str, ex: dict[str, Exercise], *,
                  titolo: str) -> tuple[str, str]:
    """Build the exercise and solution sources of one module.

    Each source becomes its own PDF, so each gets title-page fields in its front matter.

    Args:
        esercizi_tpl: Exercise template, one ``<!-- ex ID -->`` section per exercise.
        soluzioni_tpl: Solution template, which repeats each text with ``{{testo:ID}}``.
        ex: Built exercises by id.
        titolo: Title of both title pages, for example ``Modulo 03 — Regressione multipla``.

    Returns:
        The two Markdown sources, with front matter: ``title``, ``subtitle``
        (exercises or solutions) and ``stats`` (exercises, and questions when an
        exercise has several).
    """
    sezioni = extract_sections(esercizi_tpl)
    if list(sezioni) != list(ex):
        senza_testo = [i for i in ex if i not in sezioni]
        senza_esercizio = [i for i in sezioni if i not in ex]
        if senza_testo:
            raise RenderError(f"esercizi registrati senza testo: {senza_testo}")
        if senza_esercizio:
            raise RenderError(f"sezioni senza esercizio registrato: {senza_esercizio}")
        raise RenderError(f"ordine delle sezioni {list(sezioni)} diverso da quello del registro {list(ex)}")
    es_body = expand(SECTION_RE.sub(lambda m: m.group(2), esercizi_tpl), ex,
                     soluzioni=False, sezioni=sezioni)
    sol_body = expand(soluzioni_tpl, ex, soluzioni=True, sezioni=sezioni)
    includes = re.findall(r"\{\{testo:([a-z]\w*)\}\}", soluzioni_tpl)
    for id_ in ex:
        if includes.count(id_) != 1:
            raise RenderError(f"soluzioni: {{{{testo:{id_}}}}} compare {includes.count(id_)} volte, deve comparire una")
    n, domande = len(ex), len(re.findall(r"^> \[!question\]", es_body, re.M))
    stats = f"{n} esercizio" if n == 1 else f"{n} esercizi"
    if domande > n:
        stats += f" · {domande} domande"

    def head(subtitle: str) -> str:
        return f'---\ntitle: "{titolo}"\nsubtitle: "{subtitle}"\nstats: "{stats}"\n---\n\n'

    return (head("Esercizi di preparazione") + es_body,
            head("Soluzioni svolte e commentate") + sol_body)


def answers_json(ex: dict[str, Exercise]) -> dict:
    """Return the student-path answers by question label, for the blind comparison."""
    out: dict[str, dict] = {}
    for id_, e in ex.items():
        out[id_] = {}
        for label, q in e.quesiti.items():
            v = e.studente[q.chiave]
            numeric = isinstance(v, Numero)
            out[id_][label] = {"valore": v.valore if numeric else v,
                               "decimali": v.decimali if numeric else None,
                               "tolleranza": q.tolleranza}
    return out
