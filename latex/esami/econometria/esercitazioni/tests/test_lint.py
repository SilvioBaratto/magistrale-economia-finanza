"""Tests for the lint that keeps hand-typed numbers out of the templates."""

import unittest

from esercitazioni.lib.lint import lint_template


class DecimalTest(unittest.TestCase):
    """Decimals must come from a placeholder, apart from textbook constants."""

    def test_hand_typed_decimal_flagged(self):
        """A decimal typed by hand is reported with its line and the offending text."""
        issues = lint_template("riga uno\nt = 2,51")
        self.assertEqual([(i.line, i.snippet) for i in issues], [(2, "2,51")])

    def test_dot_decimal_flagged(self):
        """The dot form is caught too."""
        self.assertEqual(len(lint_template("t = 2.51")), 1)

    def test_math_comma_form_flagged(self):
        """The math form with braced comma is caught."""
        self.assertEqual(len(lint_template("$t = 2{,}51$")), 1)

    def test_placeholder_not_flagged(self):
        """A number that comes through a placeholder is fine."""
        self.assertEqual(lint_template("t = {{e03_01.t}} e $\\kappa={{e03_01.kappa|m}}$"), [])

    def test_allowed_constants(self):
        """Textbook critical values and levels may be typed, in either spelling."""
        self.assertEqual(lint_template("1,96 e 0,05 e $1{,}96$ e 100 e 1,64 e 2,57"), [])


class IntegerTest(unittest.TestCase):
    """Large integers are sample sizes and counts, which are parameters too."""

    def test_integer_sample_size_flagged(self):
        """A three-digit integer such as a sample size is reported."""
        self.assertEqual([i.snippet for i in lint_template("n = 506 aree")], ["506"])

    def test_years_and_small_integers_not_flagged(self):
        """Years and integers under 100 are structural."""
        self.assertEqual(lint_template("appello del 21 gennaio 2025, 3 punti, 95%"), [])


class StrippingTest(unittest.TestCase):
    """Comments and code blocks are not prose."""

    def test_comments_and_code_ignored_but_lines_kept(self):
        """Numbers in HTML comments or code fences are skipped without shifting line numbers."""
        text = "<!-- ex e03_01 -->\n```\nx = 2,51\n```\nt = 7,77\n"
        self.assertEqual([(i.line, i.snippet) for i in lint_template(text)], [(5, "7,77")])



class ThinSpaceTest(unittest.TestCase):
    """A thin space (backslash comma) is not a decimal separator, so numbers after it count."""

    def test_numbers_after_a_thin_space_are_flagged(self):
        """Hand-typed numbers right after \\, are reported, one per number."""
        self.assertEqual(len(lint_template("$t=\\,2{,}51$")), 1)
        self.assertEqual(len(lint_template("$\\,506$")), 1)
        self.assertEqual(len(lint_template("$[0{,}12;\\,0{,}34]$")), 2)

    def test_allowed_constants_after_a_thin_space_pass(self):
        """The allowed constants stay allowed there too."""
        self.assertEqual(lint_template("$\\pm\\,1{,}96$ e $\\,0{,}05$"), [])


if __name__ == "__main__":
    unittest.main()
