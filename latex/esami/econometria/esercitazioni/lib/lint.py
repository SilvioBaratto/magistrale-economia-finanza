"""Reject numbers typed by hand in the exercise and solution templates."""

from __future__ import annotations

import re
from dataclasses import dataclass

from . import config
from .render import PLACEHOLDER_RE

_CODE_RE = re.compile(r"```.*?```", re.S)
_COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
# A comma only continues a number when a digit precedes it: after a LaTeX thin space (\\,)
# it is just spacing and the number that follows is a hand-typed one.
_START = r"(?<![\w}])(?<!\d[.,])"
_DECIMAL_RE = re.compile(_START + r"(\d+)(?:[.,]|\{,\})(\d+)(?!\w)")
_INTEGER_RE = re.compile(_START + r"\d{3,}(?!\w|[.,]\d|\{,\})")
_YEAR_RE = re.compile(r"(?:19|20)\d\d")


@dataclass(frozen=True)
class LintIssue:
    """A number in a template that did not come from a placeholder.

    Attributes:
        line: 1-based line of the template.
        snippet: The offending text as written.
        reason: Why it is reported.
    """

    line: int
    snippet: str
    reason: str


def _blank(m: re.Match) -> str:
    # Keep every newline so the reported line numbers match the template.
    return re.sub(r"[^\n]", " ", m.group(0))


def lint_template(text: str) -> list[LintIssue]:
    """Find numbers that a person, not the exercise code, typed into a template.

    Placeholders, HTML comments and fenced code are skipped. Decimals must be
    one of the textbook constants in ``config``; integers of three or more
    digits (sample sizes, counts) must be placeholders too, except years and
    the allowed constants.

    Args:
        text: Template text.

    Returns:
        One issue per offending number, in order of appearance.
    """
    for pattern in (_CODE_RE, _COMMENT_RE, PLACEHOLDER_RE):
        text = pattern.sub(_blank, text)
    issues = []
    for m in _DECIMAL_RE.finditer(text):
        if f"{m.group(1)},{m.group(2)}" not in config.LINT_DECIMALI_AMMESSI:
            issues.append(LintIssue(text.count("\n", 0, m.start()) + 1, m.group(0), "decimale scritto a mano"))
    for m in _INTEGER_RE.finditer(text):
        if m.group(0) not in config.LINT_INTERI_AMMESSI and not _YEAR_RE.fullmatch(m.group(0)):
            issues.append(LintIssue(text.count("\n", 0, m.start()) + 1, m.group(0), "intero scritto a mano"))
    return sorted(issues, key=lambda i: i.line)
