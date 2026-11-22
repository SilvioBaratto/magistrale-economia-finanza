"""ERA 02, slide 7: the Machina triangle with a compound lottery on the segment between two lotteries."""
from modello_triangolo import (LABEL_SIZE, compound_lottery, draw_axes, draw_triangle, label_vertices,
                               mark_points, new_triangle_plane, save_figure, style)

# Lotteries L^a, L^b and weight alpha are an arbitrary example: the slide has no data.
LOTTERY_A = (0.15, 0.55)
LOTTERY_B = (0.60, 0.15)
ALPHA = 0.4

SEGMENT_WIDTH = 1.6
VERTEX_TEXTS = ("$L_1=(1,0)$", "$L_2=(0,0)$", "$L_3=(0,1)$")
# Mathtext "{,}" prints the decimal comma without the space that a bare comma gets.
ALPHA_TEXT = str(ALPHA).replace(".", "{,}")
FORMULA_TEXT = f"$L=\\alpha L^a+(1-\\alpha)L^b$\n$\\alpha={ALPHA_TEXT}$"
FORMULA_XY = (0.66, 0.78)
FORMULA_LINE_SPACING = 1.4
# Offset in points and alignment of the labels of L^a, L^b and L, set so that none touches the segment:
# L^a and L^b sit beyond the ends of the segment, L under it.
LABEL_A = dict(xytext=(-5, 4), ha="right", va="bottom")
LABEL_B = dict(xytext=(6, 4), ha="left", va="bottom")
LABEL_MIX = dict(xytext=(-5, -4), ha="right", va="top")


def label_lottery(ax, text, point, placement):
    """Write the symbol of a lottery next to its dot.

    Args:
        ax: Axes of the (p1, p3) plane.
        text: Mathtext symbol, for example ``$L^a$``.
        point: Coordinates ``(p1, p3)`` of the lottery.
        placement: Offset, horizontal and vertical alignment of the label.
    """
    ax.annotate(text, xy=point, textcoords="offset points", fontsize=LABEL_SIZE, **placement)


def main():
    """Render the figure."""
    mixture = compound_lottery(ALPHA, LOTTERY_A, LOTTERY_B)

    fig, ax = new_triangle_plane()
    draw_triangle(ax)
    draw_axes(ax)
    label_vertices(ax, VERTEX_TEXTS)

    ax.plot(*zip(LOTTERY_A, LOTTERY_B), color=style.DARK, lw=SEGMENT_WIDTH)
    mark_points(ax, [LOTTERY_A, LOTTERY_B, mixture])
    label_lottery(ax, "$L^a$", LOTTERY_A, LABEL_A)
    label_lottery(ax, "$L^b$", LOTTERY_B, LABEL_B)
    label_lottery(ax, "$L$", mixture, LABEL_MIX)
    ax.text(*FORMULA_XY, FORMULA_TEXT, ha="left", va="center", fontsize=LABEL_SIZE,
            linespacing=FORMULA_LINE_SPACING)

    save_figure(fig, "fig01")


if __name__ == "__main__":
    main()
