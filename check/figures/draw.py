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

**Book 0's figures are frozen as drawn** (the functions below, with Book 0's own two-hue ink).
**Every figure for a later book is drawn from a spec** declared in its record (`figures[].spec`,
checked by `check/figures/figspec.py`) in that book's own colours, by `draw_spec` at the end of
this file:

    python check/figures/draw.py                  # Book 0's figures, unchanged
    python check/figures/draw.py --book S01-R1    # every spec figure in that book's records
    python check/figures/draw.py --book S01-R1 --out <dir>    # somewhere else (a test)

`style_for(book_id)` gives the themed style: the Part hue the book's PDF cover uses
(`check/pdf/series.yml` via `map/BOOKS.yml`), the PDF's own Inter face loaded from
`check/pdf/fonts`, neutral grey axes and grid, WCAG-contrast marks and text on a white ground.
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



# ---------------------------------------------------------------- Part C
#
# Part C is the first Part where a figure is not optional. Its subject is graphs, and a
# section on axes, scale, slope and intercept delivered as prose describes something the
# reader never sees. These six read their numbers out of the ```table blocks of the records
# they appear in, so the picture and the text cannot drift apart.

import re as _re


def table_rows(cid, n=0):
    """The nth ```table block of a record's illustration, as rows of cells."""
    rec = load(cid)
    blocks = _re.findall(r"```table\n(.*?)```", rec["illustration"]["body"], _re.S)
    if n >= len(blocks):
        sys.exit(f"{cid}: no table block {n} - the figure and the record have diverged")
    rows = [_re.split(r" {2,}", l.strip()) for l in blocks[n].strip().split("\n") if l.strip()]
    return rows[0], rows[1:]


def _num(x):
    try:
        return float(str(x).replace(",", ""))
    except ValueError:
        return None


def _frame(ax, xlabel="", ylabel=""):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(RULE)
    ax.tick_params(labelsize=8, length=3, colors=MUTED)
    ax.set_xlabel(xlabel, fontsize=8.5, color=INK)
    ax.set_ylabel(ylabel, fontsize=8.5, color=INK)


def c5_two_scales():
    """The same points on two y-axes. A scale is chosen by whoever drew the figure."""
    head, rows = table_rows("B0-R0-C19", 0)
    xs = [_num(r[0]) for r in rows]
    ys = [_num(r[1]) for r in rows]
    fig, axes = plt.subplots(1, 2, figsize=(6.4, 2.5))
    for ax, top in zip(axes, (max(ys) * 1.1, max(ys) * 5)):
        ax.plot(xs, ys, "o-", color=BLUE, markersize=6, linewidth=1.6,
                markeredgecolor=SURFACE, markeredgewidth=1.4)
        ax.set_ylim(0, top)
        ax.set_xlim(0, max(xs) + 1)
        _frame(ax, head[0], head[1])
    axes[0].set_title("one choice of scale", fontsize=8.5, color=MUTED)
    axes[1].set_title("another, same numbers", fontsize=8.5, color=MUTED)
    fig.tight_layout()
    save(fig, "c5-two-scales.png")


def c5_slope_intercept():
    """Slope read as a rise over a run, and the intercept read off the axis."""
    head, rows = table_rows("B0-R0-C19", 1)
    xs = [_num(r[0]) for r in rows]
    ys = [_num(r[1]) for r in rows]
    fig, ax = plt.subplots(figsize=(6.2, 2.9))
    ax.plot(xs, ys, "-", color=BLUE, linewidth=1.8, zorder=2)
    ax.plot(xs, ys, "o", color=BLUE, markersize=6, markeredgecolor=SURFACE,
            markeredgewidth=1.4, zorder=3)
    a, b = 1, 4
    ya, yb = ys[xs.index(a)], ys[xs.index(b)]
    ax.plot([a, b], [ya, ya], color=ORANGE, linewidth=1.4, zorder=4)
    ax.plot([b, b], [ya, yb], color=ORANGE, linewidth=1.4, zorder=4)
    ax.annotate(f"run = {b - a:g}", ((a + b) / 2, ya), textcoords="offset points",
                xytext=(0, -14), ha="center", fontsize=8.5, color=ORANGE)
    ax.annotate(f"rise = {yb - ya:g}", (b, (ya + yb) / 2), textcoords="offset points",
                xytext=(8, 0), fontsize=8.5, color=ORANGE)
    ax.annotate(f"slope = {(yb - ya) / (b - a):g} {head[1]} per {head[0].split()[0][:-1]}",
                (0.5, 0.92), xycoords="axes fraction", fontsize=8.5, color=INK)
    ax.plot([0], [ys[0]], "o", color=INK, markersize=7, zorder=5)
    ax.annotate(f"intercept {ys[0]:g}", (0, ys[0]), textcoords="offset points",
                xytext=(8, -12), fontsize=8.5, color=INK)
    ax.set_xlim(-0.3, max(xs) + 0.3)
    ax.set_ylim(0, max(ys) * 1.15)
    _frame(ax, head[0], head[1])
    fig.tight_layout()
    save(fig, "c5-slope-intercept.png")


def c6_three_shapes():
    """Linear, exponential and saturating on one pair of axes, which is how you tell them apart."""
    head, rows = table_rows("B0-R0-C20", 0)
    xs = [_num(r[0]) for r in rows]
    series = [(head[i], [_num(r[i]) for r in rows]) for i in range(1, len(head))]
    fig, ax = plt.subplots(figsize=(6.2, 3.0))
    styles = [(BLUE, "-"), (ORANGE, "-"), (INK, "--")]
    for (name, ys), (colour, ls) in zip(series, styles):
        ax.plot(xs, ys, ls, color=colour, linewidth=1.8, marker="o", markersize=5,
                markeredgecolor=SURFACE, markeredgewidth=1.2, label=name)
        ax.annotate(name, (xs[-1], ys[-1]), textcoords="offset points", xytext=(6, -2),
                    fontsize=8.5, color=colour)
    ax.set_xlim(min(xs) - 0.2, max(xs) + 1.5)
    ax.set_ylim(0, max(max(y) for _, y in series) * 1.15)
    _frame(ax, head[0], "the quantity")
    fig.tight_layout()
    save(fig, "c6-three-shapes.png")


def c7_chords():
    """Averages over shrinking spans, each labelled as the average it is.

    An earlier version of this figure drew the slope across the final month and labelled
    it "steepness at the end". That is an average rate wearing an instantaneous rate's
    name - exactly the confusion this section's diagnostic band exists to catch, drawn as
    if it were the lesson. The table gives readings at whole months and nothing else, so
    an instantaneous rate is not in the data and cannot honestly be drawn from it. What
    the data does support is that the average depends on the span you take it over, which
    is the section's actual claim, so that is what is drawn.
    """
    head, rows = table_rows("B0-R0-C21", 0)
    xs = [_num(r[0]) for r in rows]
    ys = [_num(r[1]) for r in rows]
    fig, ax = plt.subplots(figsize=(6.2, 3.1))
    ax.plot(xs, ys, "-", color=BLUE, linewidth=1.9, zorder=2)
    ax.plot(xs, ys, "o", color=BLUE, markersize=5.5, markeredgecolor=SURFACE,
            markeredgewidth=1.3, zorder=3)
    # All three chords end at the last reading, so they converge there and the two short
    # ones lie almost on the curve. That is not a drawing fault - it is the section's point,
    # that a shorter span gives an average nearer the rate at a moment - but it means the
    # lines cannot be told apart by their paths alone. Each therefore starts at a marked
    # reading and carries its label beside that marker, and each is extended a little past
    # the last reading so the three separate again on the right.
    # Labels go in a key rather than beside each line: the two short spans start within one
    # month of each other and any leader long enough to escape that corner reads as a fourth
    # line on the chart.
    spans = [(0, len(xs) - 1, ORANGE), (len(xs) - 3, len(xs) - 1, INK),
             (len(xs) - 2, len(xs) - 1, ORANGE)]
    over = 0.55
    for k, (a, b, colour) in enumerate(spans):
        rate = (ys[b] - ys[a]) / (xs[b] - xs[a])
        span = xs[b] - xs[a]
        ax.plot([xs[a], xs[b] + over], [ys[a], ys[b] + over * rate], color=colour,
                linewidth=1.6, linestyle=["-", "--", (0, (1, 1.6))][k], zorder=4,
                label=f"over {span:g} month{'s' if span > 1 else ''}: {rate:.2f} a month")
        ax.plot([xs[a]], [ys[a]], "s", color=colour, markersize=5.5,
                markeredgecolor=SURFACE, markeredgewidth=1.2, zorder=5)
    key = ax.legend(loc="lower right", frameon=False, fontsize=8.5,
                    handlelength=2.6, borderaxespad=0.8, labelspacing=0.7)
    for text, (_, _, colour) in zip(key.get_texts(), spans):
        text.set_color(colour)
    ax.annotate("One curve, three averages, all ending at the last reading.\n"
                "Each square marks where its average starts. The span decides the number,\n"
                "and the shorter the span the closer its line lies to the curve.",
                (0.03, 0.95), xycoords="axes fraction", fontsize=8.5, color=INK,
                va="top",
                linespacing=1.4)
    ax.set_xlim(min(xs) - 0.3, max(xs) + over + 0.35)
    ax.set_ylim(0, max(ys) * 1.42)
    _frame(ax, head[0], head[1])
    fig.tight_layout()
    save(fig, "c7-chords.png")


def c8_rectangles():
    """A rate held across an interval, times the interval, stacked up: the total is the area."""
    head, rows = table_rows("B0-R0-C22", 0)
    xs = [_num(r[0]) for r in rows]
    rates = [_num(r[1]) for r in rows]
    fig, ax = plt.subplots(figsize=(6.2, 2.9))
    for x, r in zip(xs, rates):
        ax.add_patch(Rectangle((x - 1, 0), 1, r, facecolor=BLUE, alpha=0.22,
                               edgecolor=BLUE, linewidth=1.1))
        ax.annotate(f"{r:g}", (x - 0.5, r), textcoords="offset points", xytext=(0, 4),
                    ha="center", fontsize=8, color=MUTED)
    # The record's prose names "the rate line" and the reader has to be able to see it. Drawn at
    # linewidth=0 it existed in the figure and nowhere on the page. `where` matters once it is
    # visible: each rectangle spans (x-1, x], which is what "pre" draws and "post" shifts by a
    # whole month.
    ax.step([0] + xs, [rates[0]] + rates, where="pre", color=BLUE, linewidth=1.8, zorder=3)
    ax.annotate(f"every rectangle is a rate times one month;\n"
                f"the stack is the total, {sum(rates):g} in all",
                (0.02, 0.80), xycoords="axes fraction", fontsize=8.5, color=INK)
    ax.set_xlim(0, max(xs))
    ax.set_ylim(0, max(rates) * 1.5)
    ax.set_xticks(xs)
    _frame(ax, head[0], head[1])
    fig.tight_layout()
    save(fig, "c8-rectangles.png")


FIGURES.update({"c5-two-scales.png": c5_two_scales,
                "c5-slope-intercept.png": c5_slope_intercept,
                "c6-three-shapes.png": c6_three_shapes,
                "c7-chords.png": c7_chords,
                "c8-rectangles.png": c8_rectangles})
# ---------------------------------------------------------------- F2
#
# F2 is about how a mark carries a number, so its figures are the argument rather than an aid
# to it. Both read Schedule II of the National Food Security Act out of B0-R0-C40's own tables,
# and both keep every printed number correct: what changes between the panels is only how the
# number is drawn. That is the section's claim, so it is the thing the figures must not cheat on.

def _short(label, width=13):
    import textwrap
    return "\n".join(textwrap.wrap(label, width))


def f2_baseline():
    """The same six bars from zero and from 400. Length is value only when it starts at zero."""
    head, rows = table_rows("B0-R0-C40", 0)
    # Schedule II's group names are too long to sit under six bars. The short forms are keyed
    # to the record's exact wording, so a changed row stops the drawing rather than letting a
    # stale label sit under a new number.
    short = {"children, 6 months to 3 years": "children\n6 mo–3 yr",
             "children, 3 to 6 years": "children\n3–6 yr",
             "children, 6 months to 6 years, who are malnourished": "malnourished\nchildren",
             "lower primary classes": "lower\nprimary",
             "upper primary classes": "upper\nprimary",
             "pregnant women and lactating mothers": "pregnant and\nlactating"}
    unknown = [r[0] for r in rows if r[0] not in short]
    if unknown:
        sys.exit(f"f2-baseline: no short label for {unknown} - the table in B0-R0-C40 changed")
    names = [short[r[0]] for r in rows]
    vals = [_num(r[-1]) for r in rows]
    if None in vals:
        sys.exit("f2-baseline: a Schedule II value in B0-R0-C40 is not a number")
    lo, hi = min(vals), max(vals)
    # Stacked rather than side by side: six labelled bars need the full width, and one panel
    # above the other puts the two drawings of each bar in the same column for the eye.
    fig, axes = plt.subplots(2, 1, figsize=(6.6, 5.6), sharey=False)
    for ax, floor, title in ((axes[0], 0, "side axis from zero"),
                             (axes[1], 400, "the same bars, side axis from 400")):
        xs = range(len(vals))
        ax.bar(xs, vals, width=0.62, color=BLUE, zorder=2)
        for x, v in zip(xs, vals):
            ax.annotate(f"{v:g}", (x, v), textcoords="offset points", xytext=(0, 3),
                        ha="center", fontsize=7.5, color=MUTED)
        ax.set_ylim(floor, 900)
        ax.set_xticks(list(xs))
        ax.set_xticklabels(names, fontsize=7.4, color=INK, linespacing=1.15)
        _frame(ax, "", "kilocalories per meal")
        ax.set_title(title, fontsize=8.5, color=INK, loc="left")
        drawn = [(v - floor) for v in (hi, lo)]
        # Three significant figures, because the record's text says 1.78: a figure that rounds
        # to 1.8 beside a caption that says 1.78 is two numbers for one fact.
        ax.annotate(f"the {hi:g} bar is drawn {drawn[0] / drawn[1]:.3g} times\nas long as the {lo:g} bar",
                    (0.62, 0.99), xycoords="axes fraction", va="top", fontsize=8,
                    color=ORANGE if floor else INK, linespacing=1.3)
    fig.tight_layout()
    save(fig, "f2-baseline.png")


def f2_area():
    """Two values as bars, then as plates scaled in both directions: area goes as the square."""
    from matplotlib.patches import Circle
    head, rows = table_rows("B0-R0-C40", 1)
    a, b = _num(rows[0][2]), _num(rows[1][2])
    if None in (a, b):
        sys.exit("f2-area: a meal energy in B0-R0-C40 is not a number")
    k = b / a
    fig, (left, right) = plt.subplots(1, 2, figsize=(7.0, 3.3),
                                      gridspec_kw={"width_ratios": [1, 1.35]})
    left.bar([0, 1], [a, b], width=0.55, color=BLUE, zorder=2)
    for x, v in ((0, a), (1, b)):
        left.annotate(f"{v:g}", (x, v), textcoords="offset points", xytext=(0, 3),
                      ha="center", fontsize=8, color=MUTED)
    left.set_xticks([0, 1])
    left.set_xticklabels([_short(rows[0][0]), _short(rows[1][0])], fontsize=7.5)
    left.set_ylim(0, b * 1.25)
    _frame(left, "", "kilocalories per meal")
    left.set_title(f"as bars: {k:.4g} times as tall", fontsize=8.5, color=INK, loc="left")

    # Plates whose diameters are the two values, sitting on one line: the heights match the
    # bars, and the widths come along with them, which is exactly what a picture does.
    unit = 1 / 100
    da, db = a * unit, b * unit
    gap = 0.8
    for cx, d, v in ((da / 2, da, a), (da + gap + db / 2, db, b)):
        right.add_patch(Circle((cx, d / 2), d / 2, facecolor=BLUE, edgecolor=SURFACE,
                               linewidth=1.2, alpha=0.9))
        right.add_patch(Circle((cx, d / 2), d / 2 * 0.72, facecolor="none",
                               edgecolor=SURFACE, linewidth=1.0))
        right.text(cx, d / 2, f"{v:g}", ha="center", va="center", fontsize=9,
                   color=SURFACE, fontweight="bold")
    right.set_xlim(-0.3, da + gap + db + 0.3)
    right.set_ylim(-0.2, db * 1.25)
    right.set_aspect("equal")
    right.axis("off")
    right.set_title(f"as pictures: {k:.4g} times as tall and as wide,\n"
                    f"so {k * k:.3g} times the area", fontsize=8.5, color=ORANGE, loc="left")
    fig.tight_layout()
    save(fig, "f2-area.png")


FIGURES.update({"f2-baseline.png": f2_baseline,
                "f2-area.png": f2_area})


# ---------------------------------------------------------------- Part D
#
# Added by the Book 0 Part D chat, 2026-09-23. Three figures, each showing something the prose
# can only argue: a mean pulled away from a median by one value, a spread of sample means that
# halves when the sample is four times bigger, and two scales whose readings are wrong in two
# different ways. Each reads its numbers out of its record and fails loudly if they have gone.
#
# D4 was expected to carry a dot plot and does not. Its shape lesson is that the same eleven
# values look lopsided or balanced depending on where band edges fall, and the record already
# sets the two bandings side by side as tables. Drawing them again would be a table drawn as a
# picture, which is the A1 failure recorded above.

import random as _random
import statistics as _stats


def _list_after(text, lead):
    """The comma-separated numbers that follow `lead` in a record's prose."""
    m = _re.search(_re.escape(lead) + r"\s*([0-9., ]+?)[.]\s", text)
    if not m:
        sys.exit(f"could not find '{lead}' - the figure and the record have diverged")
    return [float(x) for x in m.group(1).replace(" ", "").split(",") if x]


def _derived(cid, value):
    for n in (load(cid).get("illustration") or {}).get("numbers", []) or []:
        if str(n.get("value")) == value:
            return float(value)
    sys.exit(f"{cid}: number {value} is no longer registered - the figure has diverged")


def d5_mean_median():
    """Six values, one far out. The median stays with the crowd; the mean is pulled after the 40."""
    rec = load("B0-R0-C28")
    xs = _list_after(rec["simplified_explanation"], "Take six numbers:")
    mean, median = sum(xs) / len(xs), _stats.median(xs)
    if (round(mean, 1), median) != (16.7, 13.5):
        sys.exit("B0-R0-C28: mean or median no longer 16.7 and 13.5 - the figure has diverged")
    fig, ax = plt.subplots(figsize=(6.2, 1.9))
    ax.scatter(xs, [0] * len(xs), s=70, color=BLUE, edgecolor=SURFACE, linewidth=1.4, zorder=3)
    for x in xs:
        ax.annotate(f"{x:g}", (x, 0), textcoords="offset points", xytext=(0, -16),
                    ha="center", fontsize=8, color=MUTED)
    for val, name, col, dy in ((median, "median 13.5", INK, 0.62), (mean, "mean 16.7", ORANGE, 0.62)):
        ax.axvline(val, ymin=0.18, ymax=0.82, color=col, linewidth=1.6,
                   linestyle="-" if col == INK else "--")
        ax.annotate(name, (val, dy), xycoords=("data", "axes fraction"), xytext=(4 if col == ORANGE else -4, 12),
                    textcoords="offset points", ha="left" if col == ORANGE else "right",
                    fontsize=8.5, color=INK)
    ax.set_xlim(0, 44)
    ax.set_ylim(-1, 1)
    ax.set_yticks([])
    _frame(ax, "value")
    ax.spines["left"].set_visible(False)
    fig.tight_layout()
    save(fig, "d5-mean-median.png")


def d6_sample_means():
    """5,000 means of samples of 10 against 5,000 of samples of 40, from one eight-number population."""
    rec = load("B0-R0-C29")
    pop = _list_after(rec["illustration"]["body"], "these eight numbers:")
    s10, s40 = _derived("B0-R0-C29", "0.633"), _derived("B0-R0-C29", "0.317")
    # The draw the record's derived fields name: random.seed(110) once, one random.choice per
    # value, the samples of 10 first and the samples of 40 straight after in the same stream.
    _random.seed(110)
    m10 = [sum(_random.choice(pop) for _ in range(10)) / 10 for _ in range(5000)]
    m40 = [sum(_random.choice(pop) for _ in range(40)) / 40 for _ in range(5000)]
    got10, got40 = _stats.pstdev(m10), _stats.pstdev(m40)
    if (round(got10, 3), round(got40, 3)) != (s10, s40):
        sys.exit(f"B0-R0-C29: the draw gives {got10:.3f} and {got40:.3f}, the record says "
                 f"{s10} and {s40} - the figure and the record have diverged")
    bins = [i / 10 for i in range(29, 78, 1)]
    fig, axes = plt.subplots(2, 1, figsize=(6.2, 3.6), sharex=True, sharey=True)
    for ax, ms, n, spread, col in ((axes[0], m10, 10, got10, BLUE), (axes[1], m40, 40, got40, BLUE)):
        ax.hist(ms, bins=bins, color=col, alpha=0.85, edgecolor=SURFACE, linewidth=0.6)
        ax.axvline(5, color=INK, linewidth=1.2)
        ax.annotate(f"5,000 samples of {n}\nspread of their means {spread:.3f}",
                    (0.02, 0.62), xycoords="axes fraction", fontsize=8.5, color=INK)
        ax.set_yticks([])
        _frame(ax)
        ax.spines["left"].set_visible(False)
    axes[0].annotate("population mean 5", (5, 0.92), xycoords=("data", "axes fraction"),
                     xytext=(-6, 0), textcoords="offset points", ha="right", fontsize=8, color=MUTED)
    axes[1].set_xlabel("mean of one sample", fontsize=8.5, color=INK)
    fig.tight_layout()
    save(fig, "d6-sample-means.png")


def d7_two_scales():
    """Twenty readings from each of two scales against a weight known to be 60.0 kilograms."""
    rec = load("B0-R0-C30")
    blocks = _re.findall(r"```table\n(.*?)```", rec["illustration"]["body"], _re.S)
    scales = {}
    for b in blocks:
        lines = [l.strip() for l in b.strip().split("\n") if l.strip()]
        m = _re.match(r"scale ([AB]) readings", lines[0])
        if m:
            scales[m.group(1)] = [float(v) for l in lines[1:] for v in l.split()]
    if sorted(scales) != ["A", "B"] or any(len(v) != 20 for v in scales.values()):
        sys.exit("B0-R0-C30: two tables of twenty readings not found - the figure has diverged")
    if "exactly 60.0 kilograms" not in rec["illustration"]["body"]:
        sys.exit("B0-R0-C30: the 60.0 kilogram weight is gone - the figure has diverged")
    true = 60.0
    fig, ax = plt.subplots(figsize=(6.2, 2.6))
    for y, key, col, label in ((1, "A", ORANGE, "scale A"), (0, "B", BLUE, "scale B")):
        vals = scales[key]
        counts = {}
        for v in vals:
            k = round(v, 1)
            counts[k] = counts.get(k, 0) + 1
            ax.scatter(k, y + (counts[k] - 1) * 0.045, s=22, color=col, edgecolor=SURFACE,
                       linewidth=0.8, zorder=3)
        mean = sum(vals) / len(vals)
        ax.plot([mean, mean], [y - 0.14, y - 0.04], color=INK, linewidth=1.6)
        ax.annotate(f"{label}: average {mean:g}", (58.45, y + 0.02), fontsize=8.5, color=INK,
                    va="bottom")
    ax.axvline(true, color=MUTED, linewidth=1.0, linestyle="--")
    ax.annotate("true weight 60.0", (true, -0.22), xytext=(4, 0), textcoords="offset points",
                fontsize=8, color=MUTED)
    ax.annotate("short black mark: each scale's average", (58.45, 1.72), fontsize=8, color=MUTED)
    ax.set_xlim(58.4, 61.0)
    ax.set_ylim(-0.3, 1.85)
    ax.set_yticks([])
    _frame(ax, "reading (kg)")
    ax.spines["left"].set_visible(False)
    fig.tight_layout()
    save(fig, "d7-two-scales.png")


FIGURES.update({"d5-mean-median.png": d5_mean_median,
                "d6-sample-means.png": d6_sample_means,
                "d7-two-scales.png": d7_two_scales})


# ---------------------------------------------------------------- every later book: from a spec
#
# Added 23 September 2026 on Harsh's standing instruction: more figures, in each book's own colours,
# every one mathematically correct and matching the numbers in its text. The spec is the only copy
# of the data (`check/figures/figspec.py`); this function draws exactly what it declares and writes
# the spec's fingerprint beside the PNG, and `check/build.py --check` blocks when the two part.

import json as _json
sys.path.insert(0, HERE)
import figspec  # noqa: E402

FONT_CACHE = os.path.join(os.path.dirname(HERE), "_build", "fonts")   # gitignored
PDF_FONTS = os.path.join(os.path.dirname(HERE), "pdf", "fonts")


def _pdf_font(family="Inter"):
    """Register the PDF's bundled face with matplotlib; return its family name, or None.

    The bundle is WOFF, which matplotlib's FreeType cannot open, so each face is unpacked once to
    TTF in check/_build/fonts (fontTools). Without fontTools the figure falls back to DejaVu Sans
    and says so: a different face, never a failed drawing.
    """
    from matplotlib import font_manager as fm
    stem = family.lower().replace(" ", "-")
    try:
        from fontTools.ttLib import TTFont
    except ImportError:
        print("  [figures] fontTools not installed (pip install fonttools) - using DejaVu Sans")
        return None
    os.makedirs(FONT_CACHE, exist_ok=True)
    ok = False
    for weight in ("400", "600", "700"):
        src = os.path.join(PDF_FONTS, f"{stem}-latin-{weight}-normal.woff")
        if not os.path.exists(src):
            continue
        dst = os.path.join(FONT_CACHE, f"{stem}-latin-{weight}.ttf")
        if not os.path.exists(dst):
            f = TTFont(src)
            f.flavor = None
            f.save(dst)
        fm.fontManager.addfont(dst)
        ok = True
    return family if ok else None


def style_for(book_id):
    """(palette, rcParams) for a book's figures: pal, rc = style_for(id); with plt.rc_context(rc): ..."""
    pal = figspec.palette_for(book_id)
    face = _pdf_font("Inter")
    rc = {
        "font.family": [face, "DejaVu Sans"] if face else ["DejaVu Sans"],
        "font.size": 8.5, "axes.titlesize": 9, "axes.labelsize": 8.5,
        "xtick.labelsize": 8, "ytick.labelsize": 8, "legend.fontsize": 8,
        "figure.facecolor": pal["surface"], "axes.facecolor": pal["surface"],
        "savefig.facecolor": pal["surface"],
        "text.color": pal["ink"], "axes.labelcolor": pal["ink"], "axes.titlecolor": pal["ink"],
        "axes.edgecolor": pal["axis"], "axes.linewidth": 0.8,
        "axes.spines.top": False, "axes.spines.right": False,
        "axes.grid": True, "axes.grid.axis": "y", "grid.color": pal["grid"], "grid.linewidth": 0.6,
        "axes.axisbelow": True,
        "xtick.color": pal["axis"], "ytick.color": pal["axis"],
        "xtick.labelcolor": pal["muted"], "ytick.labelcolor": pal["muted"],
        "xtick.major.width": 0.8, "ytick.major.width": 0.8, "xtick.major.size": 3, "ytick.major.size": 3,
        "lines.linewidth": 1.8, "lines.markersize": 5.5, "patch.linewidth": 0.8,
        "legend.frameon": False,
        "axes.prop_cycle": matplotlib.cycler(color=[pal["primary"], pal["secondary"], pal["tertiary"]]),
    }
    return pal, rc


def draw_spec(rec, fig_entry, out_dir=HERE, book_id=None):
    """Draw one figure from its record's spec, and write <file>.spec.json with the spec's hash."""
    book_id = book_id or figspec.book_of(rec)
    res = figspec.resolve(rec, fig_entry)
    pal, rc = style_for(book_id)
    colours = [pal["primary"], pal["secondary"], pal["tertiary"]]
    styles, markers = ["-", "-", "--"], ["o", "s", "^"]
    with plt.rc_context(rc):
        fig, ax = plt.subplots(figsize=tuple(res["size"]))
        n = len(res["series"])
        # `bands`: a shaded horizontal range behind the data, edged by thin dashed lines, keyed in
        # the legend. Its bounds pass the same number-in-text check as a plotted point.
        for b in res.get("bands") or []:
            ax.axhspan(b["y0"], b["y1"], facecolor=pal["fill"], edgecolor="none", zorder=1,
                       label=b["label"] or None)
            for yv in (b["y0"], b["y1"]):
                ax.axhline(yv, color=pal["muted"], linewidth=0.8, linestyle=(0, (3, 2)), zorder=1)
        if res["kind"] == "bar":
            pos = list(range(len(res["x_raw"]))) if res["x"] is None else res["x"]
            step = min((b - a for a, b in zip(pos, pos[1:])), default=1) if res["x"] else 1
            width = 0.7 * step / n
            for i, s in enumerate(res["series"]):
                off = (i - (n - 1) / 2) * width
                bars = ax.bar([p + off for p in pos], s["y"], width=width * 0.92,
                              color=colours[i % 3], label=s["name"], zorder=2)
                if res["value_labels"]:
                    for b, raw in zip(bars, s["y_raw"]):
                        ax.annotate(raw, (b.get_x() + b.get_width() / 2, b.get_height()),
                                    textcoords="offset points", xytext=(0, 3), ha="center",
                                    fontsize=7.5, color=pal["muted"])
            if res["x"] is None:
                ax.set_xticks(pos)
                ax.set_xticklabels(res["x_raw"])
            ax.set_ylim(bottom=0)
        else:
            # A series with a drawn relation is shown as points on that line, not joined up, so the
            # reader sees the stated rule and the data it was checked against as two things.
            fitted = {r.get("series") or res["series"][0]["name"] for r in res["relations"]
                      if r.get("fit") and r.get("draw")}
            for i, s in enumerate(res["series"]):
                c = colours[i % 3]
                joined = res["kind"] == "line" and s["name"] not in fitted
                if res["kind"] == "step":
                    ax.step(res["x"], s["y"], where="post", color=c, linestyle=styles[i % 3],
                            label=s["name"])
                # `marker: none` on a series: a bare line, for a fitted slope rather than observations.
                mk = "none" if s.get("marker") == "none" else markers[i % 3]
                ax.plot(res["x"], s["y"], linestyle=styles[i % 3] if joined or mk == "none" else "none",
                        marker=mk, color=c, markeredgecolor=pal["surface"],
                        markeredgewidth=1.2, label=None if res["kind"] == "step" else s["name"],
                        zorder=3)
                if res["value_labels"]:
                    for xv, yv, raw in zip(res["x"], s["y"], s["y_raw"]):
                        ax.annotate(raw, (xv, yv), textcoords="offset points", xytext=(0, 6),
                                    ha="center", fontsize=7.5, color=pal["muted"])
        names = figspec._names(res)
        for rel in res["relations"]:
            if rel.get("fit") and rel.get("draw") and res["x"] is not None:
                rhs = str(rel["fit"]).partition("=")[2]
                lo, hi = min(res["x"]), max(res["x"])
                xs = [lo + (hi - lo) * k / 100 for k in range(101)]
                ys = [figspec.evaluate(rhs, {**names, "x": xv}) for xv in xs]
                ax.plot(xs, ys, color=pal["secondary"], linewidth=1.3, linestyle=(0, (4, 2)),
                        label=rel.get("label") or rel["fit"], zorder=2)
        for lab in res["labels"]:
            if lab.get("at"):
                ax.annotate(lab["text"], tuple(lab["at"]), textcoords="offset points",
                            xytext=tuple(lab.get("offset", (6, 6))), fontsize=8, color=pal["ink"])
        if res["y_scale"] == "log":
            ax.set_yscale("log")
        if res["y_range"]:
            ax.set_ylim(*[float(v) for v in res["y_range"]])
        ax.set_xlabel(res["x_label"])
        ax.set_ylabel(res["y_label"])
        if res["title"]:
            ax.set_title(res["title"], loc="left")
        if n > 1 or any(r.get("draw") for r in res["relations"]) or \
                any(b["label"] for b in res.get("bands") or []):
            ax.legend(loc="best")
        fig.tight_layout()
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, fig_entry["file"])
        fig.savefig(path, dpi=220, bbox_inches="tight", pad_inches=0.12)
        plt.close(fig)
    with open(figspec.sidecar(out_dir, fig_entry["file"]), "w", encoding="utf-8") as fh:
        _json.dump({"hash": figspec.spec_hash(rec, fig_entry, book_id), "record": rec.get("concept_id"),
                    "book": book_id, "drawn_by": "check/figures/draw.py"}, fh, indent=1)
        fh.write("\n")
    print(f"  wrote {path} ({book_id} palette, hue {pal['hue']})")
    return path


def draw_book(book_id, out_dir=HERE):
    """Check, then draw, every spec figure in a book's records. A figure that fails its check is not drawn."""
    import yaml
    folder = os.path.join(os.path.dirname(HERE), "records", book_id.split("-")[0])
    bad, n = [], 0
    for fn in sorted(os.listdir(folder)):
        if not fn.endswith((".yml", ".yaml")):
            continue
        with open(os.path.join(folder, fn), encoding="utf-8") as fh:
            rec = yaml.safe_load(fh) or {}
        if figspec.book_of(rec) != book_id:
            continue
        for f in rec.get("figures") or []:
            if not isinstance(f, dict) or not f.get("spec"):
                continue
            probs = figspec.verify(rec, f)
            if probs:
                bad += [f"{rec.get('concept_id')}: {p}" for p in probs]
                continue
            draw_spec(rec, f, out_dir, book_id)
            n += 1
    for b in bad:
        print("  NOT DRAWN", b)
    print(f"{book_id}: {n} figure(s) drawn, {len(bad)} problem(s)")
    return 1 if bad else 0


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--book", help="draw every spec figure in this book's records (e.g. S01-R1)")
    ap.add_argument("--out", default=HERE, help="where to write (default check/figures)")
    a = ap.parse_args()
    sys.exit(draw_book(a.book, a.out) if a.book else main())
