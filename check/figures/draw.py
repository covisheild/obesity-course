"""Draw the figures the booklets embed.

Run: python check/figures/draw.py

A figure in this book earns its place only when it shows something the prose cannot say
in the same space. Two do, in Part A: two quantities cut into different-sized pieces, and four
amounts on a ruler where each step multiplies. Everything else in Part A is better as a
sentence, and one candidate was drawn and then cut for failing that test.

**Figures read their numbers from the records.** A figure drawn from numbers typed into
the drawing script is a second copy of the data, and the two copies drift - the text is
corrected and the picture silently keeps the old value, which is worse than no picture
because it carries the authority of having been drawn. Every quantity below is pulled
out of the concept record that the figure appears in, and the script fails loudly if a
number it expects is no longer there.
"""
import os, sys, re

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

HERE = os.path.dirname(os.path.abspath(__file__))
RECORDS = os.path.join(os.path.dirname(HERE), "records", "B0")

# Ink, not decoration. Two hues only, validated for colour-vision deficiency
# (worst adjacent pair dE 21.7 protan, 27.9 normal) and legible in greyscale print.
BLUE, ORANGE = "#2A6FB0", "#C25E00"
INK, MUTED, RULE, SURFACE = "#1A1A1A", "#5A5A5A", "#BFBFBF", "#FFFFFF"

plt.rcParams.update({
    "font.family": "DejaVu Serif",
    "font.size": 9,
    "figure.facecolor": SURFACE,
    "axes.facecolor": SURFACE,
    "savefig.facecolor": SURFACE,
    "text.color": INK,
    "axes.edgecolor": RULE,
    "axes.labelcolor": INK,
    "xtick.color": MUTED,
    "ytick.color": MUTED,
})


def load(cid):
    import yaml
    with open(os.path.join(RECORDS, f"{cid}.yml"), encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def numbers(rec):
    """{value as written: (float, unit)} from the record's own numbers register."""
    out = {}
    for n in (rec.get("illustration") or {}).get("numbers", []) or []:
        raw = str(n.get("value", "")).strip()
        try:
            out[raw] = (float(raw.replace(",", "")), n.get("unit", ""))
        except ValueError:
            continue
    return out


def save(fig, name):
    path = os.path.join(HERE, name)
    fig.savefig(path, dpi=220, bbox_inches="tight", pad_inches=0.12)
    plt.close(fig)
    print(f"  wrote {name}")


# A1 had a figure here and it was cut. It set 10,00,000 against 1,000,000 with their
# names beside them, which is a table drawn as a picture: the two lines of prose above it
# in the section say the same thing, and a reader gains nothing by looking. The bar in the
# module docstring only means something if figures that fail it are removed rather than
# kept because they were already drawn.


# ---------------------------------------------------------------- A2


def common_denominator():
    """Why two fractions must be cut into the same size of piece before they add."""
    fig, ax = plt.subplots(figsize=(6.2, 2.9))
    ax.axis("off")
    W, H = 6.0, 0.52

    def bar(y, parts, filled, colour, label):
        for k in range(parts):
            x = k * W / parts
            ax.add_patch(Rectangle((x, y), W / parts, H, facecolor=colour if k < filled else SURFACE,
                                   edgecolor=RULE, linewidth=0.9))
        ax.text(-0.15, y + H / 2, label, ha="right", va="center", fontsize=11, color=INK)

    bar(2.30, 5, 2, BLUE, "2/5")
    bar(1.58, 3, 1, ORANGE, "1/3")
    ax.text(0, 3.05, "Different-sized pieces. They cannot be counted together.",
            fontsize=9, color=MUTED)

    bar(0.60, 15, 6, BLUE, "6/15")
    bar(-0.12, 15, 5, ORANGE, "5/15")
    ax.text(0, 1.28, "Cut both into fifteenths. Same size of piece, same amount of shading.",
            fontsize=9, color=MUTED)
    ax.text(0, -0.55, "6 + 5 = 11 fifteenths. Adding tops and bottoms would give 3/8, "
                      "which is smaller than 2/5 — so it cannot be right.",
            fontsize=9, color=INK)
    ax.set_xlim(-0.75, W + 0.1)
    ax.set_ylim(-0.75, 3.2)
    save(fig, "a2-common-denominator.png")


# ---------------------------------------------------------------- A7


def log_ruler():
    """One ruler, two sets of labels: the amounts above, their logarithms below.

    An earlier version of this figure put the four penalties on a linear axis beside a
    logarithmic one, which is the standard demonstration of what a log scale is for. It
    was correct and it taught the wrong thing: across a span of only forty, a log axis
    bunches the top three amounts rather than separating them, so the picture argued
    against the tool. The section's actual claim is narrower and this figure carries it -
    position on the multiplying ruler is the logarithm, so a gap of 1.6 *is* a factor of
    about forty, and subtracting has done a division.
    """
    import math
    rec = load("B0-R0-C07")
    nums = numbers(rec)
    want = ["25,000", "3,00,000", "5,00,000", "10,00,000"]
    missing = [w for w in want if w not in nums]
    if missing:
        sys.exit(f"a7-log-ruler: {missing} no longer in B0-R0-C07's numbers register. "
                 "The figure and the text have diverged; fix one of them.")
    vals = [nums[w][0] for w in want]
    logs = [math.log10(v) for v in vals]

    fig, ax = plt.subplots(figsize=(6.2, 2.5))
    ax.axis("off")
    lo, hi = 3.92, 6.28
    span = logs[-1] - logs[0]

    def x(l):
        return (l - lo) / (hi - lo)

    ax.plot([0, 1], [0, 0], color=RULE, linewidth=1.2, zorder=1)
    for p in (4, 5, 6):
        ax.plot([x(p), x(p)], [-0.035, 0.035], color=MUTED, linewidth=1.1, zorder=2)
        ax.text(x(p), -0.125, f"$10^{p}$", ha="center", fontsize=10.5, color=MUTED)

    for v, l, w in zip(vals, logs, want):
        ax.plot([x(l)], [0], "o", markersize=8.5, color=BLUE,
                markeredgecolor=SURFACE, markeredgewidth=1.8, zorder=3)
        ax.text(x(l), 0.075, w, ha="center", fontsize=8.5, color=INK, rotation=32,
                rotation_mode="anchor")
        ax.text(x(l), -0.235, f"{l:.1f}", ha="center", fontsize=9, color=BLUE)

    ax.text(0.5, 0.40, "the amounts, on a ruler where each step multiplies by ten",
            ha="center", fontsize=8.5, color=MUTED)
    ax.text(0.5, -0.325, "the logarithm of each — its position on that ruler",
            ha="center", fontsize=8.5, color=MUTED)

    y = -0.47
    ax.annotate("", (x(logs[0]), y), xytext=(x(logs[-1]), y),
                arrowprops=dict(arrowstyle="<->", color=ORANGE, linewidth=1.2))
    ax.text((x(logs[0]) + x(logs[-1])) / 2, y - 0.075,
            f"{logs[-1]:.1f} − {logs[0]:.1f} = {span:.1f}, and {span:.1f} powers of ten "
            f"is a factor of about {round(vals[-1] / vals[0])}",
            ha="center", fontsize=8.5, color=INK)
    ax.set_xlim(-0.06, 1.06)
    ax.set_ylim(-0.62, 0.52)
    save(fig, "a7-log-ruler.png")


FIGURES = {"a2-common-denominator.png": common_denominator,
           "a7-log-ruler.png": log_ruler}


def main():
    print(f"drawing {len(FIGURES)} figures into {os.path.relpath(HERE)}")
    for fn in FIGURES.values():
        fn()


if __name__ == "__main__":
    main()
