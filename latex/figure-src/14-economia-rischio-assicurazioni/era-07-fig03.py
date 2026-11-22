"""ERA 07, slide 23: separating equilibrium, contracts psi_h^c and psi_l (bar) with curves u_h^c and u_l (bar)."""
import numpy as np

from modello_screening import (CURVE_LINE_WIDTH, GUIDE_LINE_STYLE, LABEL_SIZE, LINE_LABEL_STYLE, LOSS, PI_HIGH,
                               PI_LOW, SYMBOL_SIZE, TICK_LENGTH, decorate_axes, indemnity_on_curve, leader_line,
                               mark_contracts, new_plane, plot_full_cover_line, plot_zero_profit_line,
                               save_figure, separating_contract, style)

HEIGHT_RATIO = 0.68
XMAX, YMAX = 8.9, 4.4
FULL_COVER_END = 4.1
ZERO_PROFIT_B_END = 6.6
CURVE_SAMPLES = 400
# Premium at which each curve stops. With u = ln the high-risk curve is almost straight near psi_h^c and
# hides the zero-profit line it touches there, so it stops just past psi_h^c (p = 3.0) and the line goes on alone.
HIGH_CURVE_P_END = 3.08
LOW_CURVE_P_END = 1.22
# Premium at which u_h^c is labelled: low enough that the curve is clearly apart from the zero-profit line.
HIGH_CURVE_LABEL_P = 1.5
PSI_LOW_LABEL_XY = (2.15, 0.62)


def draw_reference_lines(ax):
    """Draw the line p = B and the zero-profit lines of the two types, with their labels.

    Args:
        ax: Axes of the (B, p) plane.
    """
    plot_full_cover_line(ax, FULL_COVER_END)
    ax.text(FULL_COVER_END + 0.1, FULL_COVER_END, "$p=B$", ha="left", va="center", fontsize=LABEL_SIZE)
    plot_zero_profit_line(ax, PI_HIGH, ZERO_PROFIT_B_END, style.DARK)
    plot_zero_profit_line(ax, PI_LOW, ZERO_PROFIT_B_END, style.BLUE)
    ax.text(ZERO_PROFIT_B_END + 0.1, PI_HIGH * ZERO_PROFIT_B_END + 0.12, "retta di profitto\nnullo dell’alto\nrischio",
            ha="left", va="bottom", **LINE_LABEL_STYLE)
    ax.text(ZERO_PROFIT_B_END + 0.1, PI_LOW * ZERO_PROFIT_B_END - 0.08, "retta di profitto\nnullo del basso\nrischio",
            ha="left", va="top", color=style.BLUE, **LINE_LABEL_STYLE)


def draw_indifference_curves(ax, contract):
    """Draw the curves u_h^c and u_l (bar) with their labels.

    Args:
        ax: Axes of the (B, p) plane.
        contract: The separating equilibrium that fixes the utility level of each curve.
    """
    p_high = np.linspace(0, HIGH_CURVE_P_END, CURVE_SAMPLES)
    p_low = np.linspace(0, LOW_CURVE_P_END, CURVE_SAMPLES)
    b_high = indemnity_on_curve(PI_HIGH, contract.u_high_c, p_high)
    b_low = indemnity_on_curve(PI_LOW, contract.u_low_bar, p_low)
    ax.plot(b_high, p_high, color=style.DARK, lw=CURVE_LINE_WIDTH)
    ax.plot(b_low, p_low, color=style.BLUE, lw=CURVE_LINE_WIDTH)
    b_label = indemnity_on_curve(PI_HIGH, contract.u_high_c, HIGH_CURVE_LABEL_P)
    ax.text(b_label + 0.15, HIGH_CURVE_LABEL_P, "$u_h^c$", ha="left", va="center", fontsize=SYMBOL_SIZE)
    ax.text(b_low[-1] + 0.1, p_low[-1], r"$\overline{u}_l$", ha="left", va="center", color=style.BLUE,
            fontsize=SYMBOL_SIZE)


def draw_contracts(ax, contract):
    """Mark psi_h^c and psi_l (bar), with the guide from psi_h^c to the B axis.

    Args:
        ax: Axes of the (B, p) plane.
        contract: The separating equilibrium that fixes the two contracts.
    """
    p_high_full = PI_HIGH * LOSS
    ax.plot([LOSS, LOSS], [0, p_high_full], **GUIDE_LINE_STYLE)
    mark_contracts(ax, [LOSS, contract.b_bar], [p_high_full, contract.p_bar])
    ax.annotate(r"$\psi_h^c$", xy=(LOSS, p_high_full), xytext=(6, -6), textcoords="offset points",
                ha="left", va="top", fontsize=SYMBOL_SIZE)
    ax.annotate(r"$\overline{\psi}_l$", xy=(contract.b_bar, contract.p_bar), xytext=PSI_LOW_LABEL_XY,
                textcoords="data", ha="left", va="center", fontsize=SYMBOL_SIZE,
                arrowprops=leader_line(shrink_a=3, shrink_b=3))


def main():
    """Render the figure."""
    contract = separating_contract()
    fig, ax = new_plane(HEIGHT_RATIO, XMAX, YMAX)

    draw_reference_lines(ax)
    draw_indifference_curves(ax, contract)
    draw_contracts(ax, contract)

    ax.set_xticks([LOSS], ["$L$"])
    ax.set_yticks([])
    ax.tick_params(length=TICK_LENGTH, labelsize=LABEL_SIZE)
    decorate_axes(ax)

    save_figure(fig, "fig03")


if __name__ == "__main__":
    main()
