# S58-R1-C17 · Honest axes: where an axis starts, what range it shows, and measuring the distortion

**Definition.** The value axis of a figure is the axis its values are read against (`B0-R0-C40`). The axis
start, written s, is the value at which the value axis begins.

The principle of proportional ink, so named by Bergstrom and West, says that a shaded area
must be in proportion to the value it stands for. On an ordinary, linear axis a bar, or an
area shaded down to the axis, therefore starts at zero. On a logarithmic axis a bar stands
for a ratio, and it starts at 1. A point or a line carries its value by position alone. Its
axis may start wherever the data need, and the range it shows is a choice the author makes
and states.

Take two bars with values a and b, a the smaller, drawn up from an axis start s above zero.
Their drawn heights are a − s and b − s, read "a minus s" and "b minus s". The drawn ratio is
(b − s) ÷ (a − s), where ÷ is read "divided by". The data ratio is b ÷ a.

Tufte's Lie Factor (LF) compares a change as the figure draws it with the same change in the
data. Each change is a percentage change: the change divided by the value it started
from, times 100.

```working
LF = (percentage change drawn in the figure) ÷ (percentage change in the data)
```

An LF of 1 draws the change at its true size. Tufte counts an LF above 1.05 or below 0.95 as
substantial distortion. For two bars drawn from an axis start s, the LF comes to a ÷ (a − s),
as the second illustration shows.

Starting a bar chart's axis above zero is called truncating it. Truncation makes readers judge
a difference as more severe. In one set of experiments this held for line charts as well as
bars, held when the axis was drawn as broken, and held when readers reported the numbers
accurately.

**In plain terms.** A bar is a length, and a reader reads a length as a value. Cut the bottom off the bars and the
reader still reads the lengths that are left. A small rise then looks like a leap.

You can measure how big the leap looks. Take the change the figure draws, as a percentage. Divide
it by the change in the data, as a percentage. That is the Lie Factor. Close to 1 is honest, and
Tufte drew the line at 1.05.

Points and lines work differently. A point is read by where it sits, not by how long anything
is. So a line chart may start its axis near the data, as long as the axis says where it starts.
Even then, the range you choose changes how big the change feels. So the caption gives the
change in numbers too.

**Figure.** The Lie Factor of a bar slide of women aged 15-49 with overweight or obesity, 20.6% in NFHS-4 and 24.0% in NFHS-5, against where the value axis starts. It is 20.6 ÷ (20.6 − s): 1.00 from zero, 1.94 from 10, 3.68 from 15, 7.92 from 18 and 34.3 from 20. The dashed line is Tufte's 1.05. The side axis is logarithmic.

*What the figure shows:* A rising curve, drawn on a logarithmic side axis, from 1.00 at an axis start of 0 through 1.94 at 10, 3.68 at 15 and 7.92 at 18, to 34.3 at 20. A dashed horizontal line at 1.05 sits just above the first point.

**Figure.** Women and men aged 15-49 with overweight or obesity, India, NFHS-4 (2015-16) and NFHS-5 (2019-21). Bars from zero: women 20.6% and 24.0%, men 18.9% and 22.9%. The rise is drawn at its true size beside the level.

*What the figure shows:* Paired bars from zero. Women: 20.6 then 24.0. Men: 18.9 then 22.9.

**Figure.** The same four values as points joined by lines, each survey placed at the year its fieldwork ended, 2016 for NFHS-4 and 2021 for NFHS-5. The side axis starts at 18%, not zero: a point carries its value by position, so this is honest when the caption says so. Women rose by 3.4 percentage points, men by 4.0.

*What the figure shows:* Two rising lines on an axis from 18 to 26. Women: 20.6 in 2016 to 24.0 in 2021. Men: 18.9 to 22.9.

**Must know points for you.**

- "Every number on the axis is correct, so the chart cannot mislead" is the error. Readers judge the lengths. In Correll's experiments the exaggeration stayed even when readers reported the numbers accurately. Fix the drawing, not the labels.
- Before you show or accept a bar chart whose axis starts above zero, work out a ÷ (a − s) with the smaller bar. If it is above 1.05, redraw it before anyone discusses the size of the gap.
- A break mark on the axis does not make a truncated bar chart honest. The lengths are unchanged, so the Lie Factor is unchanged, and a break mark did not stop the exaggeration in Correll's second experiment.
- Shading counts as ink. If you fill the area under a line, take the axis down to zero, or leave the line unfilled.
- To show a small change honestly, draw the change itself as bars from zero, or draw points on a stated range near the data. Do not truncate bars to make the change visible.
- Draw a ratio on a logarithmic axis, with bars from 1. Then "twice" and "half" have the same length, pointing opposite ways, as the same fact said two ways should.
- The Lie Factor measures whether a drawn change matches the data. It cannot tell you whether the change matters, and it does not apply to points read by position. The range you pick for a line chart still sets how big the change feels. So state the axis start in the caption, and give the change in numbers.
- When a journalist or a colleague sends you an alarming bar chart, do not repeat its shape. Repeat the change in percentage points and in per cent, with both values.

**Exercise 1** (retrieval). From memory: what does the Lie Factor divide by what? What value means the drawing is honest,
and from what value does Tufte call it substantial distortion? What does it come to for two
bars drawn from an axis start s?

**Exercise 2** (design). Take one result from the manuscript or thesis section you are rewriting for this book. Plan
its figure's value axis.

Write down four things. The mark you will use, and why. Where the value axis starts, and the
range it shows. If you use bars, the Lie Factor of that start. The sentence of the caption that
tells the reader where the axis starts and how big the change is in numbers.

**1.** Two bars stand for 40 and 50. The value axis starts at 30. Work out the height each bar is
drawn above the axis start, the drawn ratio and the data ratio.

**2.** Two bars stand for 40 and 50, and the value axis starts at 30. Work out the percentage change
in the data, the percentage change in the drawing, and the Lie Factor.

**3.** A value rises from 10 to 20. An infographic shows each value as a picture, and doubles the
picture's height and its width for the second value. Work out how many times larger the second
picture's area is, and the Lie Factor if readers judge by area.

**4.** Two bars stand for 60 and 66. On the page, the second bar is three times as tall as the first.
Where does the value axis start?

**5.** Two ratios, 2 and 0.5, are drawn as bars on a logarithmic axis. Work out each bar's length, in
units of log10, when the bars start at 1. Then work them out when the bars start at 0.1.

**6.** In NFHS-4 (2015-16), {{n:nfhs4_men_ow_ob_pct}}% of men aged 15-49 in India had overweight or obesity. In NFHS-5
(2019-21) it was {{n:nfhs5_men_ow_ob_pct}}%. A slide draws the two as bars on an axis starting at 18%. Work out the
drawn heights, the drawn ratio, the data ratio and the Lie Factor.

**7.** Bergstrom and West describe a bar chart of jobs in Tennessee. The value for 2014 is about 1.08
times the value for 2010, but the 2014 bar uses about 2.7 times as much ink. Work out the Lie
Factor. Then work out where the axis started, as a fraction of the 2010 value.

**8.** In NFHS-5, {{n:nfhs5_women_ow_ob_urban_pct}}% of urban women aged 15-49 and {{n:nfhs5_women_ow_ob_rural_pct}}% of rural women had overweight or
obesity.
A slide draws the two as bars on an axis starting at 15%. Work out the Lie Factor of the
comparison.

**9.** You want one figure for the change in overweight or obesity in adults aged 15-49 between NFHS-4 and
NFHS-5. Women went from {{n:nfhs4_women_ow_ob_pct}}% to {{n:nfhs5_women_ow_ob_pct}}%, and men from {{n:nfhs4_men_ow_ob_pct}}% to {{n:nfhs5_men_ow_ob_pct}}%. You choose points joined
by lines.
Choose the value axis's range, say why, and say what would happen if a colleague drew bars on
the same axis.

**10.** In NFHS-5, {{n:nfhs5_men_ow_ob_urban_pct}}% of urban men aged 15-49 and {{n:nfhs5_men_ow_ob_rural_pct}}% of rural men had overweight or obesity.
For women the two figures were {{n:nfhs5_women_ow_ob_urban_pct}}% and {{n:nfhs5_women_ow_ob_rural_pct}}%. Draw the urban-to-rural ratio for women and for men
as bars on a logarithmic axis. Work out each ratio and each bar's length in units of log10, and
the ratio of the two lengths.

**11.** Here is a worked answer. Find the step that broke.

```working
women overweight or obese: 20.6% in NFHS-4, 24.0% in NFHS-5
bars drawn from an axis start of 20
drawn heights: 0.6 and 4.0
drawn ratio: 4.0 divided by 0.6 = 6.67
data ratio: 24.0 divided by 20.6 = 1.165
Lie Factor: 6.67 divided by 1.165 = 5.73
```

**12.** Here is a worked answer. Find the step that broke.

```working
the slide: bars for 20.6% and 24.0% on an axis from 20, Lie Factor 34.3
the fix: a zig-zag break mark added to the axis and to both bars
the axis numbers are correct, and the break tells the reader the axis was cut
so readers now read the values, not the lengths: the Lie Factor is 1
```

**13.** Correll and colleagues reproduce a bar chart shown on Fox News. Their caption says the second
bar is 6 times taller than the first. It goes on: "even though there is only a 4.6% increase in
tax rate (ratio of 1.13 to 1)". A colleague says: "So the chart made a 4.6% rise look like a 500% rise."

Decide what to compute, compute it, and say what the chart's critics cannot claim from it.

**14.** A district officer presents NFHS results with a bar slide and says: "Look at this. Overweight
and obesity in men almost doubled between the two surveys."

Decide what to compute, compute it, and say what the claim and the slide do not establish.

