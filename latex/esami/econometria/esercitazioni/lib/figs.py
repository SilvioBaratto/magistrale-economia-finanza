"""Access to the plotting style shared with the seven exam solutions."""

from __future__ import annotations

import importlib
import sys

from . import config

_FIGURE_DIR = config.ROOT.parent / "figure"


def use_style():
    """Install the house plotting style and return the ``econstyle`` module.

    ``econstyle`` lives next to the exam figures and is not a package, so its
    folder is put on ``sys.path`` instead of being copied.

    Returns:
        The module, with the palette (``BLUE``, ``RED``...) and the primitives
        (``dist_test``, ``ci_line``, ``acf_pacf``...).
    """
    if str(_FIGURE_DIR) not in sys.path:
        sys.path.insert(0, str(_FIGURE_DIR))
    es = importlib.import_module("econstyle")
    es.use()
    return es
