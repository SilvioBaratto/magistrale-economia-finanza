"""Tests for the gretl-style regression table printer and parser."""

import unittest

import numpy as np
import statsmodels.api as sm

from esercitazioni.lib import config
from esercitazioni.lib.gretl import fmt_p, fmt_sig, ols_table, parse_table, parse_vif, vif_table

EXAM_ROW = "| crime | $-0{,}0127792$ | $0{,}00248715$ | $-5{,}138$ | 3,99e-07 |"
HEADER = "| | coefficiente | errore std. | rapporto $t$ | p-value |\n|---|---|---|---|---|\n"


def _fit(seed: int = 0, n: int = 50):
    rng = np.random.default_rng(seed)
    x = rng.normal(size=(n, 2))
    y = 1.0 + 0.5 * x[:, 0] - 0.3 * x[:, 1] + rng.normal(size=n)
    return sm.OLS(y, sm.add_constant(x)).fit()


class FmtTest(unittest.TestCase):
    """Number formatting follows the rows printed in the real exam texts."""

    def test_fmt_sig_matches_exam_rows(self):
        """Significant-figure formatting reproduces three real exam cells."""
        self.assertEqual(fmt_sig(-0.0127792, 6), "-0,0127792")
        self.assertEqual(fmt_sig(88.52, 4), "88,52")
        self.assertEqual(fmt_sig(12.1767, 6), "12,1767")

    def test_fmt_p(self):
        """P-values use four decimals, or scientific notation below 1e-4."""
        self.assertEqual(fmt_p(0.0007), "0,0007")
        self.assertEqual(fmt_p(0.011), "0,0110")
        self.assertEqual(fmt_p(3.99e-07), "3,99e-07")

    def test_tiny_coefficient_never_prints_negative_zero(self):
        """A tiny negative coefficient is never rounded to a signed zero."""
        self.assertNotIn("0,0000", fmt_sig(-0.00000004, config.SIG_COEF))


class ParseTest(unittest.TestCase):
    """The parser reads what the exam texts print."""

    def test_parse_real_exam_row(self):
        """A row copied from the 2025-01-21 exam parses to its printed values."""
        row = parse_table(HEADER + EXAM_ROW).rows["crime"]
        self.assertEqual(row["coef"], -0.0127792)
        self.assertEqual(row["se"], 0.00248715)
        self.assertEqual(row["t"], -5.138)
        self.assertEqual(row["p"], 3.99e-07)

    def test_parse_zero_p_value(self):
        """A p-value printed as 0,0000 parses to zero."""
        text = HEADER + "| zona2 | $11{,}8342$ | $0{,}132916$ | $89{,}04$ | 0,0000 |"
        self.assertEqual(parse_table(text).rows["zona2"]["p"], 0.0)

    def test_stats_line(self):
        """The line under the table gives back the sample size."""
        text = ols_table(_fit(), labels=["const", "x1", "x2"])
        self.assertEqual(parse_table(text).stats["n"], 50)


class RoundTripTest(unittest.TestCase):
    """Printing then parsing keeps exactly the printed precision."""

    def test_roundtrip_precision(self):
        """Coefficients, errors and t ratios come back rounded, never more precise."""
        res = _fit()
        labels = ["const", "x1", "x2"]
        table = parse_table(ols_table(res, labels=labels))
        for i, name in enumerate(labels):
            row = table.rows[name]
            self.assertEqual(row["coef"], float(f"{res.params[i]:.{config.SIG_COEF}g}"))
            self.assertEqual(row["se"], float(f"{res.bse[i]:.{config.SIG_COEF}g}"))
            self.assertEqual(row["t"], float(f"{res.tvalues[i]:.{config.SIG_T}g}"))

    def test_default_labels_come_from_the_model(self):
        """Without explicit labels the row names are the model's regressor names."""
        self.assertEqual(set(parse_table(ols_table(_fit())).rows), {"const", "x1", "x2"})


class NoPValueTest(unittest.TestCase):
    """Dickey-Fuller regressions are printed without the misleading t-based p-value."""

    def test_table_without_p_value_column(self):
        """The p-value column and the p cells are dropped; the other columns parse back."""
        text = ols_table(_fit(), labels=["const", "x1", "x2"], p=False)
        self.assertNotIn("p-value", text)
        row = parse_table(text).rows["x1"]
        self.assertEqual(set(row), {"coef", "se", "t"})
        self.assertEqual(parse_table(text).stats["n"], 50)

    def test_default_keeps_the_p_value_column(self):
        """Without the option the table is unchanged."""
        self.assertIn("p-value", ols_table(_fit(), labels=["const", "x1", "x2"]))


class VifTest(unittest.TestCase):
    """The VIF table of the exam texts, printed and read back."""

    def test_vif_table_format(self):
        """Three decimals and a decimal comma, one row per regressor."""
        text = vif_table({"reddito": 12.3456, "famiglia": 1.2})
        self.assertIn("| reddito | 12,346 |", text)
        self.assertIn("| famiglia | 1,200 |", text)

    def test_vif_roundtrip_at_printed_precision(self):
        """Reading the table back gives the three-decimal values, not the originals."""
        self.assertEqual(parse_vif(vif_table({"reddito": 12.3456})), {"reddito": 12.346})

    def test_parse_table_ignores_the_vif_table(self):
        """A two-column table is not mistaken for a regression table."""
        self.assertEqual(parse_table(vif_table({"x": 2.0})).rows, {})


if __name__ == "__main__":
    unittest.main()
