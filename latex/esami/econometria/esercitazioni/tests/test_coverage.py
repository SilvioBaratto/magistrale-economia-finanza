"""Tests for the coverage matrix against the taxonomy of exam questions."""

import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

from esercitazioni.lib.coverage import load_tassonomia, matrice

TIPI = [
    {"id": "t-ic", "modulo": 2, "origine": "appello", "descrizione": "IC", "occorrenze": ["2025-01-21:D1"]},
    {"id": "t-tcl", "modulo": 0, "origine": "ripasso", "descrizione": "TCL", "occorrenze": []},
]


def _ex(id_, tipo, livello):
    return SimpleNamespace(id=id_, tipo=tipo, livello=livello)


class MatrixTest(unittest.TestCase):
    """Coverage rules of the spec: two per exam type, one at exam level, one per review topic."""

    def test_complete_coverage_has_no_problems(self):
        """Two exercises with one at level 3, plus one review exercise, is enough."""
        _, problems = matrice(TIPI, [_ex("e02_01", "t-ic", 1), _ex("e02_02", "t-ic", 3),
                                     _ex("e00_01", "t-tcl", 1)])
        self.assertEqual(problems, [])

    def test_coverage_flags_under_two(self):
        """An exam type with a single exercise is reported."""
        _, problems = matrice(TIPI, [_ex("e02_01", "t-ic", 3), _ex("e00_01", "t-tcl", 1)])
        self.assertTrue(any("t-ic" in p and "2" in p for p in problems))

    def test_coverage_requires_level3_for_appello_types(self):
        """An exam type without an exam-level exercise is reported."""
        _, problems = matrice(TIPI, [_ex("e02_01", "t-ic", 1), _ex("e02_02", "t-ic", 2),
                                     _ex("e00_01", "t-tcl", 1)])
        self.assertTrue(any("t-ic" in p and "livello 3" in p for p in problems))

    def test_review_topic_needs_one_exercise(self):
        """A review topic with no exercise is reported."""
        _, problems = matrice(TIPI, [_ex("e02_01", "t-ic", 1), _ex("e02_02", "t-ic", 3)])
        self.assertTrue(any("t-tcl" in p for p in problems))

    def test_course_topic_needs_one_exercise(self):
        """A competence the course teaches but the exams never ask needs one exercise only."""
        tipi = TIPI + [{"id": "t-fwl", "modulo": 3, "origine": "corso", "descrizione": "FWL",
                        "occorrenze": []}]
        base = [_ex("e02_01", "t-ic", 1), _ex("e02_02", "t-ic", 3), _ex("e00_01", "t-tcl", 1)]
        _, missing = matrice(tipi, base)
        self.assertTrue(any("t-fwl" in p for p in missing))
        _, covered = matrice(tipi, base + [_ex("e03_01", "t-fwl", 2)])
        self.assertEqual(covered, [])

    def test_exercise_with_several_types_counts_for_each(self):
        """An exercise testing two competences covers both of them."""
        tipi = TIPI + [{"id": "t-b", "modulo": 2, "origine": "appello", "descrizione": "B",
                        "occorrenze": ["2025-01-21:D2"]}]
        both = [_ex("e02_01", ("t-ic", "t-b"), 2), _ex("e02_02", ("t-ic", "t-b"), 3),
                _ex("e00_01", "t-tcl", 1)]
        self.assertEqual(matrice(tipi, both)[1], [])

    def test_unknown_type_is_reported(self):
        """An exercise typed with an id not in the taxonomy is a typo."""
        _, problems = matrice(TIPI, [_ex("e02_01", "t-xx", 1)])
        self.assertTrue(any("t-xx" in p and "e02_01" in p for p in problems))

    def test_table_lists_exercises_per_type(self):
        """The Markdown matrix names each type with the exercises that cover it."""
        table, _ = matrice(TIPI, [_ex("e02_01", "t-ic", 1)])
        self.assertIn("| t-ic |", table)
        self.assertIn("e02_01", table)


class LoadTest(unittest.TestCase):
    """The taxonomy is the first JSON block of its Markdown file."""

    def test_load_tassonomia_reads_json_block(self):
        """Prose around the block is ignored."""
        text = 'Intro\n\n```json\n{"tipi": [{"id": "t-ic", "modulo": 2}]}\n```\n\nFine'
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "TASSONOMIA.md"
            path.write_text(text)
            self.assertEqual(load_tassonomia(path), [{"id": "t-ic", "modulo": 2}])


if __name__ == "__main__":
    unittest.main()
