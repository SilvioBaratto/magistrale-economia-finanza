"""Tests for the comparison between the exercise bank and the blind solver."""

import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path

from esercitazioni.lib.compare_blind import compare, main

BANCO = {"e03_01": {"a": {"valore": 1.23, "decimali": 2, "tolleranza": None},
                    "b": {"valore": "rifiuta", "decimali": None, "tolleranza": None}}}


class CompareTest(unittest.TestCase):
    """The script, not the agent, decides whether the answers agree."""

    def test_one_unit_tolerance(self):
        """One unit of the last digit agrees, three units are a discrepancy."""
        near = compare(BANCO, {"e03_01": {"a": 1.24, "b": "rifiuta"}})
        far = compare(BANCO, {"e03_01": {"a": 1.26, "b": "rifiuta"}})
        self.assertTrue(near.passed)
        self.assertEqual(far.scarti, ["e03_01.a"])

    def test_whole_number_must_match_exactly(self):
        """Degrees of freedom one off are a discrepancy; a non-integer shown without decimals is not."""
        gdl = {"e04_02": {"a": {"valore": 3, "decimali": 0, "tolleranza": None}}}
        self.assertEqual(compare(gdl, {"e04_02": {"a": 4}}).scarti, ["e04_02.a"])
        self.assertTrue(compare(gdl, {"e04_02": {"a": 3}}).passed)
        pct = {"e04_02": {"a": {"valore": 86.4, "decimali": 0, "tolleranza": None}}}
        self.assertTrue(compare(pct, {"e04_02": {"a": 87}}).passed)

    def test_custom_tolerance_overrides(self):
        """An explicit tolerance replaces the one-unit default."""
        banco = {"e03_01": {"a": {"valore": 0.50, "decimali": 2, "tolleranza": 0.1}}}
        self.assertTrue(compare(banco, {"e03_01": {"a": 0.58}}).passed)
        self.assertFalse(compare(banco, {"e03_01": {"a": 0.65}}).passed)

    def test_missing_and_extra_labels(self):
        """Unanswered and unexpected labels are both reported."""
        report = compare(BANCO, {"e03_01": {"a": 1.23, "z": 4.0}})
        self.assertEqual(report.mancanti, ["e03_01.b"])
        self.assertEqual(report.extra, ["e03_01.z"])
        self.assertFalse(report.passed)

    def test_missing_exercise_reports_all_its_labels(self):
        """An exercise the solver skipped entirely is missing every label."""
        self.assertEqual(compare(BANCO, {}).mancanti, ["e03_01.a", "e03_01.b"])

    def test_decision_normalization(self):
        """Case and trailing punctuation do not matter, a negation does."""
        self.assertTrue(compare(BANCO, {"e03_01": {"a": 1.23, "b": "Rifiuta."}}).passed)
        self.assertFalse(compare(BANCO, {"e03_01": {"a": 1.23, "b": "Non rifiuto"}}).passed)

    def test_numbers_given_as_italian_text(self):
        """A solver that writes 1,23 as a string is still read as a number."""
        self.assertTrue(compare(BANCO, {"e03_01": {"a": "1,23", "b": "rifiuta"}}).passed)

    def test_unreadable_number_is_a_discrepancy(self):
        """Text that is not a number is reported, not raised."""
        self.assertEqual(compare(BANCO, {"e03_01": {"a": "circa uno", "b": "rifiuta"}}).scarti,
                         ["e03_01.a"])


class MainTest(unittest.TestCase):
    """The command line reads the bank answers written by the build."""

    def test_main_exit_codes(self):
        """Exit status is 0 when the answers agree and 1 when they do not."""
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            (tmp / "03.json").write_text(json.dumps(BANCO))
            good = tmp / "good.json"
            good.write_text(json.dumps({"e03_01": {"a": 1.23, "b": "rifiuta"}}))
            bad = tmp / "bad.json"
            bad.write_text(json.dumps({"e03_01": {"a": 9.0, "b": "rifiuta"}}))
            with contextlib.redirect_stdout(io.StringIO()) as out:
                self.assertEqual(main(["03", str(good)], answers_dir=tmp), 0)
                self.assertEqual(main(["03", str(bad)], answers_dir=tmp), 1)
            self.assertIn("scarti: e03_01.a", out.getvalue())


if __name__ == "__main__":
    unittest.main()
