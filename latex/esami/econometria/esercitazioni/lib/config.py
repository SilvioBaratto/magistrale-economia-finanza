"""Constants shared by the exercise bank, calibrated on the real exam texts."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LATEX = ROOT.parents[2]
BUILD = LATEX / "build" / "esercitazioni-econometria"

# Digits gretl prints in the exam texts: six for coefficients and standard
# errors, four for the t ratio (see ECON_Sol_2025-01-21.md, first table).
SIG_COEF = 6
SIG_T = 4

# A test statistic closer than this fraction to its critical value makes the
# decision depend on the rounding of the printed table, so the exercise is rejected.
MARGINE_BORDERLINE = 0.15

# Constants a solution may type by hand: textbook critical values and levels.
LINT_DECIMALI_AMMESSI = frozenset(
    {"1,96", "2,58", "1,645", "1,64", "2,57", "0,05", "0,01", "0,10", "0,5", "0,95", "0,99", "0,975"}
)
LINT_INTERI_AMMESSI = frozenset({"100"})
