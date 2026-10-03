# S58-R1-C18 · Decoration that does no work

**Definition.** Tufte divides the ink on a figure into two kinds. Data-ink is the ink that changes when the
data change: the bars, the points, the line. Everything else is non-data ink: frames, grid
lines, background fills, shadows. The data-ink ratio is the data-ink divided by all the ink
used to print the figure.

```working
data-ink ratio = data-ink ÷ total ink used to print the figure
               = 1 − (share of the ink that can be erased without losing any data)
```

Tufte's rule is to maximise this ratio "within reason": erase non-data ink, and erase
data-ink that repeats what other ink already shows. He gives no one-sentence definition of
chartjunk. He introduces it as decoration that "does not tell the viewer anything new".

In this book, decoration is any element that tells the reader nothing about the data or about
how to read them. A 3-D effect on flat data, a shadow, a coloured background behind a single
plot, a frame round the whole figure and a dark grid are decoration. Axis titles, tick labels
and a light grid or reference line are context. So is a direct label: a group's name written
beside its data, in place of a legend, the key that says which colour is which. Context is
non-data ink, and it stays (Wilke).

One experiment measured the cost of decoration. Bateman and colleagues (2010) showed 20 people
charts by the graphic artist Nigel Holmes, built around cartoon pictures, and plain versions of
the same charts. While the charts were on screen, people described the decorated ones as
accurately as the plain ones. Two to three weeks later, the 10 people tested then remembered
the decorated charts better. The paper reports t-tests, not the size of the difference in
score points. Viewing time was not limited, and the task was to describe the chart aloud.

What would overturn the working rule here: studies of figures read for exact values, under time
pressure, or in a scientific paper, finding that decoration costs nothing in accuracy and adds
no bias.

**In plain terms.** Every mark on a figure either tells the reader something or gets in the way. The bars and points
tell. So do the axis titles and the labels: without them the bars mean nothing. A 3-D tilt, a
shadow, a coloured background or a thick grid tells nothing, and some of them bend the data.

So ask one question of each mark: what does this tell the reader? If the answer is "nothing",
delete it. Then stop before you delete the labels.

There is one real argument for decoration. In one small study, cartoon charts were remembered
better weeks later, and were described no worse. That is a reason to think about a poster, not
a licence for a 3-D bar in a paper.

**Figure.** Bateman and colleagues (2010): share of on-screen time spent looking at each part of the chart. Holmes charts, built into cartoon pictures: 40% on data alone, 27% on data drawn as part of a picture, 13% on picture alone, 20% elsewhere. Plain charts: 78% on data, 22% elsewhere. 20 students, untimed viewing.

*What the figure shows:* Paired bars for four parts of the screen. Holmes charts: data alone 40, data in a picture 27, picture alone 13, elsewhere 20. Plain charts: data 78, data in a picture 0, picture alone 0, elsewhere 22.

**Must know points for you.**

- "The cleanest figure is the one with the least ink" is the error. Tufte's rule is to maximise the data-ink ratio "within reason". Delete the axis title or the labels and the bars mean nothing. Delete decoration; keep context.
- Ask one question of every element of a figure: what does it tell the reader about the data, or about how to read them? If nothing, delete it. Do this before you change anything else.
- Never draw flat data in 3-D. The third dimension carries no data and it bends the bars: in Wilke's example, 322 first-class passengers read as fewer than 300.
- Use direct labels: write each line's or group's name beside its data, and delete the legend. The reader then reads the figure without moving the eye back and forth.
- "Useful junk?" found that cartoon charts were described no worse, and were remembered better two to three weeks later. That was 20 students, with no time limit. It does not show that decoration is harmless when a reader needs exact values, and the authors say so. A picture tied to the message may suit a poster. Keep it out of a paper's figure.
- A picture on a chart carries an opinion. In Bateman's study readers found the designer's "value message" more often in the decorated charts. On a public chart, choose a picture only if you are willing to say its message out loud.
- Removing decoration cannot fix a dishonest axis. A plain bar chart that starts above zero is still wrong. Check the axis as well as the ink.
- When a trainee brings you a chart straight from a spreadsheet, do not redraw it for them. Have them delete one element at a time, and ask after each whether the reader lost anything.

**Exercise 1** (retrieval). From memory: what is data-ink, what is the data-ink ratio, and what two words does Tufte attach
to his rule to maximise it? Name two elements that are not data-ink but should stay.

**Exercise 2** (critique). A made-up district report has a figure for six blocks. It shows the share of children under 5
weighed last month at the anganwadi, the village child-care centre. The figure has:

- 3-D cylinders in six colours, with a shadow under each;
- a legend matching the colours to block names;
- a dark grid every 5%;
- a picture of a weighing scale behind the bars;
- no axis title;
- a value axis running from 60% to 100%.

List what you would change, in the order you would change it, and say why for each.

**Exercise 3** (teaching). A first-year resident has read the abstract of "Useful junk?" and says: "So chartjunk is fine
now. Decorated charts are remembered better." You have ten minutes and a whiteboard. Say what
you would teach.

