"""Tests for the build driver, on a throwaway module in a temporary tree."""

import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path

from esercitazioni import build
from esercitazioni.lib import bank

EX_PY = '''
import statsmodels.api as sm

from esercitazioni.lib.bank import Draft, Numero, Quesito, exercise
from esercitazioni.lib.gretl import ols_table

TITOLO = "Prova"


@exercise("{id}", modulo={modulo}, livello=1, tipo="t-prova")
def make(rng):
    """Return a one-regressor exercise whose answer is the t ratio of x1."""
    x = rng.normal(size=60)
    y = 1 + 0.8 * x + rng.normal(size=60)
    res = sm.OLS(y, sm.add_constant(x)).fit()

    def studente(tab):
        """Read the t ratio from the printed table."""
        return {{"t": Numero(tab["ols"].rows["x1"]["t"], 2)}}

    return Draft(dati=None, parametri={{"n": Numero(60, 0)}},
                 tabelle={{"ols": ols_table(res, labels=["const", "x1"])}},
                 risposte={{"t": Numero(float(res.tvalues[1]), 2)}}, studente=studente,
                 quesiti={{"a": Quesito("t")}})
'''

ESERCIZI = """<!-- ex {id} -->
> [!question] Esercizio 1
> Con n = {{{{{id}.n}}}} osservazioni:
>
> {{{{{id}.tab.ols}}}}
>
> (a) Calcola il rapporto t di x1.
<!-- /ex -->
"""

SOLUZIONI = """{{{{testo:{id}}}}}

> [!success] Risposta
> (a) t = {{{{{id}.t}}}}.
"""


def _write_unit(root: Path, subdir: str, id_: str, modulo: int, esercizi=None, soluzioni=None):
    d = root / subdir
    d.mkdir(parents=True)
    (d / "ex.py").write_text(EX_PY.format(id=id_, modulo=modulo))
    (d / "esercizi.tpl.md").write_text(esercizi or ESERCIZI.format(id=id_))
    (d / "soluzioni.tpl.md").write_text(soluzioni or SOLUZIONI.format(id=id_))


class BuildTestCase(unittest.TestCase):
    """Gives each test its own root and build folders and an empty registry."""

    def setUp(self):
        """Create the temporary tree and silence the driver's console output."""
        bank.clear_registry()
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name) / "esercitazioni"
        self.build = Path(tmp.name) / "build"
        self.root.mkdir()

    def run_main(self, *argv):
        """Run the driver and return its exit status and console output."""
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
            status = build.main(list(argv), root=self.root, build=self.build)
        return status, buf.getvalue()


class ModuleBuildTest(BuildTestCase):
    """A module becomes two Markdown sources and an answers file."""

    def test_writes_sources_front_matter_and_answers(self):
        """The module is written with its chapter title and its blind-comparison answers."""
        _write_unit(self.root, "moduli/05-prova", "e99_01", 5)
        status, _ = self.run_main("--modulo", "5")
        self.assertEqual(status, 0)
        sol = (self.build / "src" / "ECON_Soluzioni_05_Prova.md").read_text()
        self.assertIn('title: "Modulo 05 — Prova"', sol)
        self.assertIn('subtitle: "Soluzioni svolte e commentate"', sol)
        self.assertTrue((self.build / "src" / "ECON_Esercizi_05_Prova.md").exists())
        answers = json.loads((self.build / "answers" / "05.json").read_text())
        self.assertEqual(list(answers["e99_01"]), ["a"])

    def test_appello_numbering(self):
        """Appello 1 is file number 8 and its answers are named a01."""
        _write_unit(self.root, "appelli/01", "a01_01", 8)
        status, _ = self.run_main("--appello", "1")
        self.assertEqual(status, 0)
        text = (self.build / "src" / "ECON_Soluzioni_08_Appello-simulato-1.md").read_text()
        self.assertIn('title: "Appello simulato 1"', text)
        self.assertTrue((self.build / "answers" / "a01.json").exists())

    def test_build_is_idempotent(self):
        """Two builds in a row produce identical sources."""
        _write_unit(self.root, "moduli/05-prova", "e99_01", 5)
        self.run_main("--modulo", "5")
        first = (self.build / "src" / "ECON_Soluzioni_05_Prova.md").read_bytes()
        bank.clear_registry()
        self.run_main("--modulo", "5")
        self.assertEqual((self.build / "src" / "ECON_Soluzioni_05_Prova.md").read_bytes(), first)

    def test_sources_with_the_old_names_are_replaced(self):
        """A source written under an earlier naming of the same unit does not linger."""
        _write_unit(self.root, "moduli/05-prova", "e99_01", 5)
        src = self.build / "src"
        src.mkdir(parents=True)
        (src / "ECON_Sol_05.md").write_text("vecchio")
        (src / "ECON_Eserc_05.md").write_text("vecchio")
        (src / "ECON_Esercizi_01_Altro.md").write_text("altro modulo")
        self.assertEqual(self.run_main("--modulo", "5")[0], 0)
        self.assertEqual(sorted(p.name for p in src.iterdir()),
                         ["ECON_Esercizi_01_Altro.md", "ECON_Esercizi_05_Prova.md",
                          "ECON_Soluzioni_05_Prova.md"])

    def test_stale_figures_are_removed(self):
        """A figure left over from an earlier numbering is deleted; other files stay."""
        _write_unit(self.root, "moduli/05-prova", "e99_01", 5)
        figdir = self.root / "moduli" / "05-prova" / "figure"
        figdir.mkdir()
        (figdir / "e99_09_vecchia.pdf").write_text("x")
        (figdir / "note.txt").write_text("x")
        self.assertEqual(self.run_main("--modulo", "5")[0], 0)
        self.assertFalse((figdir / "e99_09_vecchia.pdf").exists())
        self.assertTrue((figdir / "note.txt").exists())

    def test_check_fails_on_unresolved_placeholder(self):
        """A placeholder that does not resolve fails the check and writes nothing."""
        _write_unit(self.root, "moduli/05-prova", "e99_01", 5,
                    soluzioni="{{testo:e99_01}}\n\nt = {{e99_01.zzz}}\n")
        status, out = self.run_main("--modulo", "5", "--check")
        self.assertEqual(status, 1)
        self.assertIn("zzz", out)
        self.assertFalse((self.build / "src").exists())

    def test_check_does_not_write_sources(self):
        """A passing check leaves the render folder untouched."""
        _write_unit(self.root, "moduli/05-prova", "e99_01", 5)
        self.assertEqual(self.run_main("--modulo", "5", "--check")[0], 0)
        self.assertFalse((self.build / "src").exists())

    def test_lint_failure_returns_1(self):
        """A hand-typed decimal in a template fails the build."""
        _write_unit(self.root, "moduli/05-prova", "e99_01", 5,
                    esercizi=ESERCIZI.format(id="e99_01").replace("Calcola", "Calcola, sapendo che 2,51,"))
        status, out = self.run_main("--modulo", "5")
        self.assertEqual(status, 1)
        self.assertIn("2,51", out)


class NumberingTest(BuildTestCase):
    """Appelli take the numbers from 8 on, so a module with such a number is refused."""

    def test_module_numbered_eight_or_more_is_rejected(self):
        """A moduli/08-... folder would collide with the first appello."""
        _write_unit(self.root, "moduli/08-prova", "e08_01", 8)
        status, out = self.run_main("--all")
        self.assertEqual(status, 1)
        self.assertIn("08", out)
        self.assertFalse((self.build / "src").exists())


class DeterminismTest(unittest.TestCase):
    """Figures are tracked, so rebuilding must not change them."""

    def test_pdf_figures_do_not_carry_the_build_time(self):
        """Two figures saved a second apart are byte-identical: no creation date in the PDF."""
        import time

        import matplotlib
        matplotlib.use("pdf")
        import matplotlib.pyplot as plt

        out = []
        for _ in range(2):
            fig, ax = plt.subplots()
            ax.plot([0, 1], [0, 1])
            buf = io.BytesIO()
            fig.savefig(buf, format="pdf")
            plt.close(fig)
            out.append(buf.getvalue())
            time.sleep(1.1)
        self.assertEqual(out[0], out[1])


class BlindPackTest(BuildTestCase):
    """The blind solver gets the exercise text and nothing else."""

    def test_blind_pack_contains_no_answers(self):
        """The pack has the rendered exercise only: no solutions, answers or bank code."""
        _write_unit(self.root, "moduli/05-prova", "e99_01", 5)
        pack = self.build.parent / "pack"
        status, _ = self.run_main("--modulo", "5", "--blind-pack", str(pack))
        self.assertEqual(status, 0)
        files = sorted(p.name for p in pack.rglob("*") if p.is_file())
        self.assertEqual(files, ["esercizi.md"])
        text = (pack / "esercizi.md").read_text()
        self.assertIn("Calcola il rapporto t", text)
        self.assertNotIn("Risposta", text)
        self.assertNotIn("def make", text)


if __name__ == "__main__":
    unittest.main()
