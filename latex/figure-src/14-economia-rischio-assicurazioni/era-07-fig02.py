"""ERA 07, slide 22: zero-profit lines of the two types and the three contracts psi_1, psi_2, psi_3."""
from modello_screening import (LABEL_SIZE, LINE_LABEL_STYLE, PI_HIGH, PI_LOW, SYMBOL_SIZE, decorate_axes,
                               mark_contracts, new_plane, plot_full_cover_line, plot_zero_profit_line,
                               save_figure, style)

HEIGHT_RATIO = 0.62
XMAX, YMAX = 8.6, 3.5
# Right end of the zero-profit lines, where their labels start.
ZERO_PROFIT_B_END = 5.6
BOLD_ZERO_PROFIT_LINE_WIDTH = 1.6
# Contracts (B, p) of the chapter's worked example.
CONTRACTS = {r"$\psi_1$": (2.3, 1.7), r"$\psi_2$": (3.2, 1.1), r"$\psi_3$": (3.8, 0.2)}


def main():
    """Render the figure."""
    fig, ax = new_plane(HEIGHT_RATIO, XMAX, YMAX)

    plot_full_cover_line(ax, YMAX)
    plot_zero_profit_line(ax, PI_HIGH, ZERO_PROFIT_B_END, style.DARK, BOLD_ZERO_PROFIT_LINE_WIDTH)
    plot_zero_profit_line(ax, PI_LOW, ZERO_PROFIT_B_END, style.BLUE, BOLD_ZERO_PROFIT_LINE_WIDTH)
    ax.text(YMAX + 0.1, YMAX, "$p=B$", ha="left", va="center", color=style.DARK, fontsize=LABEL_SIZE)
    ax.text(ZERO_PROFIT_B_END + 0.12, PI_HIGH * ZERO_PROFIT_B_END,
            "$p=\\overline{\\pi}B$:\nretta di profitto nullo\ndell’alto rischio",
            ha="left", va="center", color=style.DARK, **LINE_LABEL_STYLE)
    ax.text(ZERO_PROFIT_B_END + 0.12, PI_LOW * ZERO_PROFIT_B_END,
            "$p=\\underline{\\pi}B$:\nretta di profitto nullo\ndel basso rischio",
            ha="left", va="center", color=style.BLUE, **LINE_LABEL_STYLE)

    for label, (b, p) in CONTRACTS.items():
        mark_contracts(ax, b, p)
        ax.text(b + 0.15, p + 0.02, label, ha="left", va="center", fontsize=SYMBOL_SIZE)

    ax.set(xticks=[], yticks=[])
    decorate_axes(ax)

    save_figure(fig, "fig02")


if __name__ == "__main__":
    main()
