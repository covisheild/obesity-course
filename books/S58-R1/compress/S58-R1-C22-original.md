# S58-R1-C22 · Making the plot: from a table of numbers to a finished figure

**Definition.** Making a figure is a sequence of decisions, taken in a fixed order, which any program can be
made to carry out. The first four decide the figure's content. They are the one claim it makes,
the mark that suits the shape of the data, and the range of the value axis. The fourth is the
words on it, with each axis titled and given its unit. The next two decide its design: every default the
program applied is checked and changed where it does not serve the claim, and colour is given
a job or removed. Then the caption is written. Last, the figure is saved in the format and at
the size the journal asks for, and checked at the size it will be printed and in grey.

Wilke separates content from design in the same way. Content is the data shown, the mapping
of data to marks, the scales, the axis ranges and the type of plot. Design is the colours,
fonts, symbol sizes and the placement of legends, ticks and titles.

A default is a setting a program uses when you have not chosen one. Defaults are made to suit
any plot, so they suit no particular plot well.

In this book, a figure sheet is the written list of the decisions for one figure, kept beside
the data. It lets you, or anyone else, draw the same figure again from the same numbers.

An image is saved either as a bitmap, a grid of coloured dots called pixels, or as a vector
graphic, which stores the shapes themselves and is redrawn at any size without losing
sharpness.

**In plain terms.** A program will draw a chart from your numbers in one click. That chart is the program's
guess, made for every chart at once. Almost every choice in it needs changing for yours.

So decide first, then draw. Write your decisions down in order. Start with the one thing the
figure says, the kind of mark, and where the axis starts and ends. Then the words on the axes,
which defaults to change, and what colour is for. Last, the caption and how to save it. Then
make the program do exactly that.

Keep that list. When a number changes, or a reviewer asks for a change, you can draw the
figure again in minutes and get the same result.

**Illustration.** Here is the trap with the chart a program offers first. It looks finished. Take a real set
of numbers and see.

Open the *National Family Health Survey (NFHS-5), 2019-21: India Fact Sheet* at
https://dhsprogram.com/pubs/pdf/OF43/India_National_Fact_Sheet.pdf. Search for anaemic.
Haemoglobin is the oxygen-carrying protein of the blood, measured in grams per decilitre
(g/dl). The fact sheet counts a person as anaemic when it is below a cut-off for their group. Five
of its rows are these.

> 92. Children age 6-59 months who are anaemic (<11.0 g/dl)22 (%) 64.2 68.3 67.1 58.6

> 95. All women age 15-49 years who are anaemic22 (%) 53.8 58.5 57.0 53.1

> 96. All women age 15-19 years who are anaemic22 (%) 56.5 60.2 59.1 54.1

> 97. Men age 15-49 years who are anaemic (<13.0 g/dl)22 (%) 20.4 27.4 25.0 22.7

> 98. Men age 15-19 years who are anaemic (<13.0 g/dl)22 (%) 25.0 33.9 31.1 29.2

The four columns are NFHS-5 (2019-21) urban, rural and total, then NFHS-4 (2015-16) total, as
in the overweight rows you have used all through this book. Take the two totals for each
group into a table of your own.

```table
| group | NFHS-4, 2015-16 (%) | NFHS-5, 2019-21 (%) |
| children 6-59 months | 58.6 | 67.1 |
| women 15-19 | 54.1 | 59.1 |
| women 15-49 | 53.1 | 57.0 |
| men 15-19 | 29.2 | 31.1 |
| men 15-49 | 22.7 | 25.0 |
```

Now suppose you select the table and ask your program for a column chart. The draft below is
described, not copied from any one program, but each of its faults is common.

It has a title
across the top, "Chart 1". A legend in a box says "Series1" and "Series2". The value axis
starts at 20. The text is small and grey. The bars are red and green. A dark grid line runs
every 5 points. It saves as a jpeg.

Do not start fixing what you see. Start from the top of the list, and write each decision
down as you take it.

**1. The claim.** Cover the chart and write the one sentence it should make. Here: between
NFHS-4 and NFHS-5, the share with anaemia rose in every group. Check it against the table,
group by group, in percentage points.

```working
67.1 minus 58.6 = 8.5
59.1 minus 54.1 = 5.0
57.0 minus 53.1 = 3.9
31.1 minus 29.2 = 1.9
25.0 minus 22.7 = 2.3
```

Every difference is above zero, so the claim holds. The fact sheet's rows for non-pregnant
and pregnant women rose too. They are left out because the row for all women contains them,
and they would not weaken the claim. Rows that would weaken it stay in.

**2. The mark.** The shape of the data is amounts for a set of groups, at two times. That
takes bars, or dots where the bars would end, on one shared axis (`S58-R1-C15`). Put each
group's two bars side by side, because the claim compares the two rounds within a group.

**3. The axis.** Bars start at zero, so the starting point of 20 goes. See what it was doing
to the men aged 15-49, the smallest pair. Work out the Lie Factor (LF) of `S58-R1-C17` with
the smaller bar, a ÷ (a − s).

```working
22.7 minus 20 = 2.7
22.7 divided by 2.7 = 8.407407407
```

The draft drew their rise about 8.4 times its true size. From zero, the Lie Factor is 1.

**4. The words.** Title the value axis with the quantity and its unit: "anaemic (%)". The
group names go under their bars, with ages in years. Delete "Chart 1": the finding goes in the
caption, not across the drawing.

**5. The defaults.** Go through the rest one at a time and ask of each what it tells the
reader (`S58-R1-C18`). The legend's "Series1" and "Series2" become "NFHS-4, 2015-16" and
"NFHS-5, 2019-21". The dark grid goes, or becomes faint. Make the small grey text larger and
darker. Wilke's verdict on defaults is the reason: "nearly all plot libraries and graphing
softwares have poor defaults".

**6. Colour.** Its job here is to separate two rounds. Red against green fails in grey and for
a reader with colour-vision deficiency (`S58-R1-C19`). Choose two colours that differ clearly
in lightness. Then make sure colour does not carry the difference alone. Keep the earlier
round on the left in every pair, and write each round's name over the first pair of bars.

**7. The caption.** Finding first, then what the bars are, who, when, and the source
(`S58-R1-C20`). The fact sheet gives no counts, so say so.

**8. Saving.** Read the journal's instructions on file type and size first. ICMJE notes that
most submission systems give "detailed instructions on the quality of images". Where it is
left to you, save a vector graphic, such as a pdf, for print. Use a png where a bitmap is
required. Never use a jpeg for a chart: Wilke says to avoid it for "images containing line
drawings or text".

Keep the original. A jpeg made from it cannot be turned back into it.

**9. The checks.** Shrink the figure on screen to about {{n:figure_check_width_low_cm}} to {{n:figure_check_width_high_cm}} cm wide, the size of one column
of a printed page, and read every label (`S58-R1-C20`).

Print it, or view it, in grey, and look
at it through a colour-vision-deficiency simulator. Two bars that look alike in grey need
another difference.

Here is the figure sheet you have written, decision by decision.

```table
| step | decision for this figure |
| claim | anaemia rose between NFHS-4 and NFHS-5 in every group the fact sheet reports |
| data | five rows of the NFHS-5 India fact sheet, NFHS-4 and NFHS-5 totals; pregnant and non-pregnant women left out, contained in all women |
| mark | bars, the two rounds side by side within each group |
| axis | value axis from 0 to 80, titled "anaemic (%)" |
| words | groups under the bars with ages in years; no title on the drawing |
| defaults changed | legend names the rounds; faint grid; larger, darker text |
| colour | two colours that differ in lightness; NFHS-4 always on the left; each round named over the first pair |
| caption | finding first; what the bars show; ages; no counts in the source; source and indicator numbers |
| saving | the journal's format and size; otherwise pdf, and png where a bitmap is required |
| checks | read at {{n:figure_check_width_low_cm}} cm wide; in grey; through a simulator |
```

The figure that results is drawn below. The program you used does not appear anywhere on the
sheet. That is the point: any program that will take these decisions can draw it again.

**Where this picture breaks.** The sheet makes the figure repeatable only as far as you wrote it down. A change you make by
dragging a label with the mouse and forget to record is lost the next time. Wilke's answer is
to have a program draw the figure from the data by code every time, so nothing is done by
hand. Writing that code is taught in the course's book on R and reproducibility.

These rows are national totals for India. Each group has its own cut-off for haemoglobin, so
the bars compare shares, not haemoglobin levels. The fact sheet's own footnote warns that its
capillary-blood results "need not be compared with other surveys using venous blood".

**Figure.** Between NFHS-4 (2015-16) and NFHS-5 (2019-21), the share with anaemia rose in every group the India fact sheet reports. Bars show the per cent anaemic, by each group's own haemoglobin cut-off; ages in years. Counts are not given in the source. Source: NFHS-5 India Fact Sheet, indicators 92 and 95 to 98.

*What the figure shows:* Five pairs of bars from zero, NFHS-4 on the left of each pair and NFHS-5 on the right, named over the first pair: children 6-59 months 58.6 and 67.1; women 15-19 54.1 and 59.1; women 15-49 53.1 and 57.0; men 15-19 29.2 and 31.1; men 15-49 22.7 and 25.0. In every pair the NFHS-5 bar is taller.

**Must know points for you.**

- Write the figure's decisions down before you open the program, in order: claim, mark, axis, words, defaults, colour, caption, saving, checks. Then make the program carry them out. If you start by fixing what the first chart shows, you fix what you happen to notice.
- "The program drew it, so it is a neutral picture of the numbers" is the error. Every setting you did not choose was chosen for any chart at all. Rougier and colleagues: defaults are "good enough for any plot but they are best for none". Check each one, the axis start first.
- A spreadsheet will do only if you change nearly every default. Wilke does not recommend Excel for figures at all, because everything in it is done by hand and cannot be repeated exactly. If a spreadsheet is what you have, keep a figure sheet beside the file, and record every change as you make it.
- Never finish a figure by hand in a drawing program and leave no record. Wilke: "the moment you manually edit a figure, your final figure becomes irreproducible." When a reviewer asks for one changed number, every hand edit has to be done again, and some will be forgotten.
- Read the journal's instructions for figures before you save. Where they leave it to you, save a vector graphic such as a pdf for print. Use a png where a bitmap is required, and never a jpeg for a chart. Keep the original: a pdf saved as a jpeg cannot be turned back.
- Check the figure at the size it will be printed, not at the size of your screen. ICMJE asks that every letter and number stay "legible when the figure is reduced for publication". Shrink it to one column's width, then view it in grey and through a simulator.
- When a trainee shows you a chart, ask for the figure sheet before you look at the chart. If there is none, have them write the claim first. Most of the faults you would have marked follow from a missing first line.
- The procedure makes sure each decision is taken on purpose. It cannot tell you whether the numbers are right or the claim is true. A perfectly made figure of a wrong table is a wrong figure, so check the data against their source before step 1.

**Exercise 1** (retrieval). From memory: list the nine decisions for making a figure, in order. Which four decide what
the figure shows, and which come after?

**Exercise 2** (critique). A colleague hands you the figure sheet below for a figure in her thesis. It is invented. Say
what is wrong with each line you would change, and what you would write instead.

```table
| step | decision |
| claim | anaemia in NFHS-5 |
| mark | 3-D columns, the program's first offer |
| axis | the program's own range, which starts at 50 |
| words | title on top: "Anaemia"; axis untitled |
| colour | red for women, green for men |
| saving | jpeg, so the file is small |
```

**Exercise 3** (design). Take the figure you are drawing for your build section. Write its figure sheet, all nine
lines, before you open any program. Then draw it, and note every place where you had to change
something the sheet did not mention. Add those to the sheet.

**Exercise 4** (teaching). A first-year resident says: "I only have a spreadsheet, and my guide says it is fine. Why
should I bother with all these steps?" Ten minutes, with a whiteboard.

