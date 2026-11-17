"""Appunti FSTR 2026-11-17: simple and discounted payback of the supermarket case.

Rebuilt from the audio, not the slide. The lecturer describes two lines (blue: payback,
orange: discounted payback) and a dashed line at the initial investment, and states the data
aloud: investment 10 million, FCFO 1.5 million for 10 years, WACC 8%. Intermediate points come
from those parameters; the lecturer's own figure for the last year (10,065,122) is the check.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import style

OUT = str(style.REPO / "obsidian/11-Finanza-Strategica/appunti-fedeli/figure/2026-11-17-fig01.png")

INVESTMENT_MILLIONS = 10.0
ANNUAL_FCFO_MILLIONS = 1.5
WACC = 0.08
HORIZON_YEARS = 10
Y_AXIS_TOP_MILLIONS = 16
# The lecturer calls the second line "gialla o arancio"; the palette has no orange.
ORANGE = "#E08A00"
DASH_WIDTH = 1.0

years = list(range(HORIZON_YEARS + 1))
simple_cumulative = [0.0]
discounted_cumulative = [0.0]
for year in years[1:]:
    simple_cumulative.append(simple_cumulative[-1] + ANNUAL_FCFO_MILLIONS)
    discounted_cumulative.append(
        discounted_cumulative[-1] + ANNUAL_FCFO_MILLIONS / (1 + WACC) ** year)

fig, ax = style.figure()
ax.plot(years, simple_cumulative, color=style.GP_BLUE,
        label="Flussi cumulati (tempo di recupero)")
ax.plot(years, discounted_cumulative, color=ORANGE,
        label="Flussi attualizzati cumulati (tempo di recupero attualizzato)")
ax.axhline(INVESTMENT_MILLIONS, color=style.DARK, linestyle="--", linewidth=DASH_WIDTH,
           label="Investimento iniziale (10 milioni)")

ax.set_xlabel("Anni")
ax.set_ylabel("Milioni di euro")
ax.set_xlim(0, HORIZON_YEARS)
ax.set_ylim(0, Y_AXIS_TOP_MILLIONS)
ax.set_xticks(years)
ax.legend(loc="upper left")

style.save(fig, OUT)
