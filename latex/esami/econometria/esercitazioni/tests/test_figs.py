"""Test that the exam figure style is reachable from the exercise bank."""

import contextlib
import io
import tempfile
import unittest
from pathlib import Path

from esercitazioni.lib.figs import use_style


class UseStyleTest(unittest.TestCase):
    """The bank draws with the same style as the seven exam solutions."""

    def test_style_saves_a_pdf(self):
        """The returned module exposes the palette and writes a vector PDF."""
        es = use_style()
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots()
        ax.plot([0, 1], [0, 1], color=es.BLUE)
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "x.pdf"
            with contextlib.redirect_stdout(io.StringIO()):
                es.save(fig, out)
            self.assertTrue(out.read_bytes().startswith(b"%PDF"))


if __name__ == "__main__":
    unittest.main()
