"""Tests for the exercise registry and the checks every exercise must pass."""

import tempfile
import unittest
from pathlib import Path

import numpy as np
import statsmodels.api as sm

from esercitazioni.lib import bank
from esercitazioni.lib.bank import Draft, ExerciseError, Margin, Numero, Quesito
from esercitazioni.lib.gretl import Table, ols_table


def _draft(student_t=None, truth=None, attese=(), margini=(), figure=None, decision=None):
    """Build a one-regressor draft whose single answer is the t ratio of x1."""
    rng = np.random.default_rng(1)
    x = rng.normal(size=60)
    y = 1.0 + 0.8 * x + rng.normal(size=60)
    res = sm.OLS(y, sm.add_constant(x)).fit()
    text = ols_table(res, labels=["const", "x1"])
    real_t = float(res.tvalues[1])
    seen = []

    def studente(tabelle):
        """Return the t ratio read from the printed table, or a forced value."""
        seen.append(tabelle)
        value = student_t if student_t is not None else tabelle["ols"].rows["x1"]["t"]
        out = {"t": Numero(value, 2)}
        if decision is not None:
            out["d"] = decision[1]
        return out

    risposte = {"t": Numero(truth if truth is not None else real_t, 2)}
    quesiti = {"a": Quesito("t")}
    if decision is not None:
        risposte["d"] = decision[0]
        quesiti["b"] = Quesito("d")
    draft = Draft(dati=None, parametri={}, tabelle={"ols": text}, risposte=risposte,
                  studente=studente, quesiti=quesiti, attese=list(attese),
                  margini=list(margini), figure=figure or {})
    draft.seen = seen
    return draft


def _register(id_, draft, modulo=3, livello=1):
    bank.exercise(id_, modulo=modulo, livello=livello, tipo="t-test")(lambda rng: draft)


class BankTestCase(unittest.TestCase):
    """Starts every test from an empty registry."""

    def setUp(self):
        """Empty the registry and give the test a scratch figure folder."""
        bank.clear_registry()
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.figdir = Path(self.tmp.name)

    def run_module(self, modulo=3):
        """Build one module into the scratch folder."""
        return bank.build_all(modulo, self.figdir)


class NumeroTest(unittest.TestCase):
    """A number prints with the decimals it was declared with."""

    def test_numero_formats(self):
        """Plain and math forms use the decimal comma; a rounded zero has no sign."""
        self.assertEqual(Numero(0.05491, 4).testo(), "0,0549")
        self.assertEqual(Numero(0.05491, 4).tex(), "0{,}0549")
        self.assertEqual(Numero(-0.00001, 2).testo(), "0,00")


class SeedTest(unittest.TestCase):
    """Seeds depend only on the exercise id."""

    def test_seed_is_stable(self):
        """The same id always gives the same seed, different ids differ."""
        self.assertEqual(bank.seed_for("e03_01"), bank.seed_for("e03_01"))
        self.assertNotEqual(bank.seed_for("e03_01"), bank.seed_for("e03_02"))


class RegistryTest(BankTestCase):
    """The registry refuses ambiguous ids."""

    def test_duplicate_id_rejected(self):
        """Registering the same id twice raises ValueError."""
        _register("e03_01", _draft())
        with self.assertRaises(ValueError):
            _register("e03_01", _draft())

    def test_build_all_filters_by_module(self):
        """Only the exercises of the requested module are built."""
        _register("e03_01", _draft(), modulo=3)
        _register("e04_01", _draft(), modulo=4)
        self.assertEqual([e.id for e in self.run_module(3)], ["e03_01"])


class StudentPathTest(BankTestCase):
    """The answer must be reachable from the printed table alone."""

    def test_student_path_within_one_unit(self):
        """One unit of the last digit passes, three units are reported by key."""
        res = _draft()
        truth = float(res.risposte["t"].valore)
        _register("e03_01", _draft(student_t=round(truth, 2) + 0.01, truth=round(truth, 2)))
        self.assertEqual(self.run_module()[0].id, "e03_01")
        bank.clear_registry()
        _register("e03_01", _draft(student_t=round(truth, 2) + 0.03, truth=round(truth, 2)))
        with self.assertRaises(ExerciseError) as ctx:
            self.run_module()
        self.assertTrue(any(p.startswith("e03_01: t:") for p in ctx.exception.problemi))

    def test_student_path_reads_printed_table_only(self):
        """The student function receives parsed tables, never the dataframe."""
        draft = _draft()
        _register("e03_01", draft)
        self.run_module()
        self.assertTrue(all(isinstance(t, Table) for t in draft.seen[0].values()))

    def test_parameter_and_answer_with_same_key_rejected(self):
        """A key that is both a parameter and an answer would let the text show the answer."""
        draft = _draft()
        draft.parametri["t"] = Numero(1, 0)
        _register("e03_01", draft)
        with self.assertRaises(ExerciseError) as ctx:
            self.run_module()
        self.assertTrue(any("sia parametro sia risposta" in p for p in ctx.exception.problemi))

    def test_decision_mismatch(self):
        """A rejection in the truth and a non-rejection from the table is a problem."""
        _register("e03_01", _draft(decision=("rifiuta", "non rifiuta")))
        with self.assertRaises(ExerciseError):
            self.run_module()


class ExpectationTest(BankTestCase):
    """The story of an exercise is pinned by expectations and margins."""

    def test_expectation_violation_fails(self):
        """A false expectation is reported as such."""
        _register("e03_01", _draft(attese=[lambda r: False]))
        with self.assertRaises(ExerciseError) as ctx:
            self.run_module()
        self.assertIn("attesa violata", " ".join(ctx.exception.problemi))

    def test_borderline_margin(self):
        """A statistic within 15% of its critical value is rejected, 50% away is fine."""
        _register("e03_01", _draft(margini=[Margin(stat=2.0, crit=1.96)]))
        with self.assertRaises(ExerciseError):
            self.run_module()
        bank.clear_registry()
        _register("e03_01", _draft(margini=[Margin(stat=3.0, crit=1.96)]))
        self.assertEqual(len(self.run_module()), 1)


class OrderAndFiguresTest(BankTestCase):
    """Levels rise inside a module and figures land next to their id."""

    def test_levels_must_be_non_decreasing(self):
        """A module with levels 1, 3, 2 fails to build."""
        for i, level in enumerate((1, 3, 2), start=1):
            _register(f"e03_0{i}", _draft(), livello=level)
        with self.assertRaises(ExerciseError) as ctx:
            self.run_module()
        self.assertIn("livell", " ".join(ctx.exception.problemi))

    def test_figures_written_next_to_exercise_id(self):
        """Each figure writer is called with <figdir>/<id>_<name>.pdf."""
        writer = lambda path: path.write_text("pdf")
        _register("e03_01", _draft(figure={"residui": writer}))
        exercise = self.run_module()[0]
        expected = self.figdir / "e03_01_residui.pdf"
        self.assertEqual(exercise.figure_path["residui"], expected)
        self.assertTrue(expected.exists())



class IntegerAnswerTest(BankTestCase):
    """Whole-number answers (degrees of freedom, lag orders, counts) must match exactly."""

    @staticmethod
    def _draft(truth, student):
        return Draft(dati=None, parametri={}, tabelle={}, risposte={"gdl": Numero(truth, 0)},
                     studente=lambda _tabelle: {"gdl": Numero(student, 0)},
                     quesiti={"a": Quesito("gdl")})

    def test_off_by_one_integer_is_a_problem(self):
        """An integer answer one unit off fails: n-k against n-k-1 is the classic mistake."""
        _register("e03_01", self._draft(3, 4))
        with self.assertRaises(ExerciseError):
            self.run_module()

    def test_exact_integer_passes(self):
        """The same integer from both paths is fine."""
        _register("e03_01", self._draft(3, 3))
        self.assertEqual(len(self.run_module()), 1)

    def test_non_integer_shown_without_decimals_keeps_one_unit(self):
        """A value shown with no decimals that is not a whole number keeps the one-unit tolerance."""
        _register("e03_01", self._draft(86.4, 87.1))
        self.assertEqual(len(self.run_module()), 1)


class NonFiniteTest(BankTestCase):
    """NaN and infinity compare false with everything, so they must be rejected explicitly."""

    @staticmethod
    def _draft(truth=1.0, student=1.0, parametro=1.0, margin=(3.0, 1.96)):
        return Draft(dati=None, parametri={"n": Numero(parametro, 0)}, tabelle={},
                     risposte={"x": Numero(truth, 2)},
                     studente=lambda _tabelle: {"x": Numero(student, 2)},
                     quesiti={"a": Quesito("x")}, margini=[Margin(*margin)])

    def test_non_finite_values_are_problems(self):
        """A NaN or infinite truth, student answer, parameter or margin statistic fails the build."""
        nan, inf = float("nan"), float("inf")
        cases = {"verita": dict(truth=nan), "studente": dict(student=inf),
                 "parametro": dict(parametro=nan), "margine": dict(margin=(nan, 1.96))}
        for name, kwargs in cases.items():
            with self.subTest(name):
                bank.clear_registry()
                _register("e03_01", self._draft(**kwargs))
                with self.assertRaises(ExerciseError) as ctx:
                    self.run_module()
                self.assertTrue(any("non finito" in p for p in ctx.exception.problemi))


if __name__ == "__main__":
    unittest.main()
