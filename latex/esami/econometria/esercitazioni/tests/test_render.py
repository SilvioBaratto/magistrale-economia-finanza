"""Tests for placeholder expansion and module assembly."""

import os
import tempfile
import unittest
from pathlib import Path

from esercitazioni.lib import render
from esercitazioni.lib.bank import Draft, Exercise, Numero, Quesito
from esercitazioni.lib.render import RenderError

TABLE = "| | coefficiente |\n|---|---|\n| x | $1{,}5$ |"


def _ex(figure_path=None, id_="e03_01"):
    """Build an exercise whose t ratio is 5.1234 in truth and 5.12 for the student."""
    draft = Draft(
        dati=None,
        parametri={"n": Numero(50, 0), "kappa": Numero(0.15, 2)},
        tabelle={"ols": TABLE},
        risposte={"t": Numero(5.1234, 2), "d": "rifiuta"},
        studente=lambda tabelle: {},
        quesiti={"a": Quesito("t"), "b": Quesito("d", tolleranza=0.5)},
    )
    return Exercise(id_, 3, 1, "t-test", 3, draft,
                    {"t": Numero(5.12, 2), "d": "rifiuta"}, figure_path or {})


def _expand(text, solutions=False, sections=None, figure_path=None):
    return render.expand(text, {"e03_01": _ex(figure_path)}, soluzioni=solutions,
                         sezioni=sections or {})


class PlaceholderTest(unittest.TestCase):
    """Numbers enter the text only through placeholders."""

    def test_plain_and_math_forms(self):
        """The plain form uses a comma, the |m form wraps it for math mode."""
        self.assertEqual(_expand("kappa = {{e03_01.kappa}}"), "kappa = 0,15")
        self.assertEqual(_expand("$\\kappa = {{e03_01.kappa|m}}$"), "$\\kappa = 0{,}15$")

    def test_latex_braces_untouched(self):
        """Double braces that are not placeholders pass through unchanged."""
        text = r"$\frac{{a}}{b} x_{{i}}$"
        self.assertEqual(_expand(text), text)

    def test_unknown_id_key_figure_raise(self):
        """A reference to something that does not exist fails, naming it."""
        for text, name in (("{{e99_01.n}}", "e99_01"), ("{{e03_01.zzz}}", "zzz"),
                           ("{{e03_01.fig.residui}}", "residui"), ("{{e03_01.tab.nope}}", "nope")):
            with self.subTest(text=text), self.assertRaisesRegex(RenderError, name):
                _expand(text)

    def test_missing_figure_file_raises(self):
        """A figure registered but not written to disk fails the build."""
        with self.assertRaisesRegex(RenderError, "mancante"):
            _expand("{{e03_01.fig.residui}}", figure_path={"residui": Path("/nonexistent/x.pdf")})

    def test_figure_path_is_relative_to_the_sources(self):
        """A figure placeholder expands to a path relative to the esercitazioni folder."""
        with tempfile.NamedTemporaryFile(suffix=".pdf") as f:
            out = _expand("{{e03_01.fig.residui}}", figure_path={"residui": Path(f.name)})
        self.assertEqual(out, os.path.relpath(f.name, render.ROOT))

    def test_answer_in_exercise_text_raises(self):
        """An answer cannot appear in the exercise text, only in the solution."""
        with self.assertRaisesRegex(RenderError, "risposta"):
            _expand("t = {{e03_01.t}}", solutions=False)

    def test_solutions_use_student_values(self):
        """The solution prints the student-path value, not the full-precision truth."""
        self.assertEqual(_expand("{{e03_01.t}}", solutions=True), "5,12")
        self.assertEqual(_expand("{{e03_01.d}}", solutions=True), "rifiuta")

    def test_parameters_allowed_in_exercise_text(self):
        """Numbers the student is given may appear in the exercise text."""
        self.assertEqual(_expand("n = {{e03_01.n}}"), "n = 50")

    def test_table_in_blockquote_prefixes_each_line(self):
        """A multi-line table inside a callout keeps the quote marker on every line."""
        out = _expand("> {{e03_01.tab.ols}}")
        self.assertTrue(all(line.startswith(">") for line in out.splitlines()))
        self.assertEqual(len(out.splitlines()), 3)


class AssemblyTest(unittest.TestCase):
    """Modules are assembled from the two templates."""

    ES = "<!-- ex e03_01 -->\nCalcola t, n = {{e03_01.n}}.\n<!-- /ex -->\n"
    SOL = "{{testo:e03_01}}\n\nRisposta: {{e03_01.t}}\n"

    def test_extract_sections(self):
        """Exercise sections are found by their markers."""
        self.assertEqual(render.extract_sections(self.ES), {"e03_01": "Calcola t, n = {{e03_01.n}}."})

    def test_testo_include_in_solutions(self):
        """The solution repeats the expanded text of the exercise."""
        _, sol = render.render_module(self.ES, self.SOL, {"e03_01": _ex()},
                                      titolo="Modulo 03 — Prova")
        self.assertIn("Calcola t, n = 50.", sol)
        self.assertIn("Risposta: 5,12", sol)

    def test_markers_removed_from_exercise_pdf_source(self):
        """The exercise source has no section markers and its own title page fields."""
        es, _ = render.render_module(self.ES, self.SOL, {"e03_01": _ex()},
                                     titolo="Modulo 03 — Prova")
        self.assertNotIn("<!--", es)
        self.assertTrue(es.startswith(
            '---\ntitle: "Modulo 03 — Prova"\nsubtitle: "Esercizi di preparazione"\n'
            'stats: "1 esercizio"\n---\n'))

    def test_solutions_have_their_own_subtitle(self):
        """The solution source says so on its title page."""
        _, sol = render.render_module(self.ES, self.SOL, {"e03_01": _ex()},
                                      titolo="Modulo 03 — Prova")
        self.assertIn('subtitle: "Soluzioni svolte e commentate"', sol.split("---\n")[1])

    def test_stats_count_exercises_and_questions(self):
        """Several question callouts in one exercise are counted as questions."""
        es = ("<!-- ex e03_01 -->\n> [!question] A\n> uno\n\n> [!question] B\n> due\n<!-- /ex -->\n")
        out, _ = render.render_module(es, "{{testo:e03_01}}", {"e03_01": _ex()}, titolo="T")
        self.assertIn('stats: "1 esercizio · 2 domande"', out)

    def test_unknown_testo_raises(self):
        """Including an exercise that has no section fails."""
        with self.assertRaisesRegex(RenderError, "e03_09"):
            render.render_module(self.ES, "{{testo:e03_09}}", {"e03_01": _ex()},
                                 titolo="T")

    def test_deterministic(self):
        """Rendering twice gives identical text."""
        args = (self.ES, self.SOL, {"e03_01": _ex()})
        kw = dict(titolo="T")
        self.assertEqual(render.render_module(*args, **kw), render.render_module(*args, **kw))


class AnswersJsonTest(unittest.TestCase):
    """The blind comparison reads the student-path values by question label."""

    def test_answers_json_shape(self):
        """Each labelled question maps to its value, decimals and tolerance."""
        data = render.answers_json({"e03_01": _ex()})
        self.assertEqual(data["e03_01"]["a"], {"valore": 5.12, "decimali": 2, "tolleranza": None})
        self.assertEqual(data["e03_01"]["b"], {"valore": "rifiuta", "decimali": None, "tolleranza": 0.5})



class MalformedPlaceholderTest(unittest.TestCase):
    """A placeholder written slightly wrong must fail, not reach the PDF as literal braces."""

    def test_near_miss_placeholders_raise(self):
        """Spaces, a wrong case, a bad suffix or a dash in the key are all reported."""
        for text in ("{{ e03_01.n }}", "{{e03_01.n |m}}", "{{e03_01.n|M}}", "{{testo: e03_01}}",
                     "{{E03_01.n}}", "{{e03_01.ic-lo}}", "{{e03_01.tab.ols|m}}"):
            with self.subTest(text=text), self.assertRaisesRegex(RenderError, "non riconosciuto"):
                _expand(text)


class RegistryAgreementTest(unittest.TestCase):
    """The registered exercises, the sections of the exercise text and the includes agree."""

    ES2 = ("<!-- ex e03_01 -->\nUno {{e03_01.n}}.\n<!-- /ex -->\n"
           "<!-- ex e03_02 -->\nDue {{e03_02.n}}.\n<!-- /ex -->\n")
    SOL2 = "{{testo:e03_01}}\n\n{{testo:e03_02}}\n"

    def _both(self):
        return {"e03_01": _ex(), "e03_02": _ex(id_="e03_02")}

    def test_matching_registry_renders(self):
        """Two exercises, two sections, two includes in the same order is fine."""
        render.render_module(self.ES2, self.SOL2, self._both(), titolo="T")

    def test_registered_exercise_without_a_section_raises(self):
        """An exercise in the registry that has no text would be counted but never shown."""
        only_first = "<!-- ex e03_01 -->\nUno.\n<!-- /ex -->\n"
        with self.assertRaisesRegex(RenderError, "e03_02"):
            render.render_module(only_first, "{{testo:e03_01}}", self._both(), titolo="T")

    def test_exercise_without_testo_include_raises(self):
        """A solution file that never includes an exercise leaves it without a solution."""
        with self.assertRaisesRegex(RenderError, "e03_02"):
            render.render_module(self.ES2, "{{testo:e03_01}}", self._both(), titolo="T")

    def test_sections_in_another_order_raise(self):
        """The level order is checked on the registry, so the printed order must be the same."""
        swapped = ("<!-- ex e03_02 -->\nDue.\n<!-- /ex -->\n<!-- ex e03_01 -->\nUno.\n<!-- /ex -->\n")
        with self.assertRaisesRegex(RenderError, "ordine"):
            render.render_module(swapped, self.SOL2, self._both(), titolo="T")


if __name__ == "__main__":
    unittest.main()
