# S52-R1-C18 · Plotting with the grammar of graphics

**Definition.** `ggplot()`, from the ggplot2 package, starts a plot from a data frame and a set of aesthetic
mappings. An aesthetic mapping, made with `aes()`, says which column of the data controls
which visual property of the marks: position along x, position along y, colour, and others.
A geom is the kind of mark that represents each observation or group, and each `geom_`
function adds one layer of marks. Layers are added to the plot with `+`.

The function `geom_histogram()` divides the x axis into bins and draws a bar whose height is
the count of observations in each bin. Unless told otherwise it uses 30 bins. A value on the
edge between two bins is then counted in the bin to its left. The arguments `binwidth`,
`boundary` and `closed` set the width of the bins, where an edge falls, and which edge a bin
includes.

The function `geom_boxplot()` draws the median and a box from the first to the third
quartile. Its whiskers reach the furthest values within 1.5 times the interquartile range of
the box. Values beyond the whiskers are drawn one by one.

A visual property written inside `aes()` is mapped: it varies with a column. Written outside
`aes()`, as an argument of the geom, it is set: one fixed value for every mark. The function
`facet_wrap()` draws one panel for each value of a column. The function `ggsave()` writes a
plot to a file, at a size you give.

**In plain terms.** Book 0 taught you to read a figure in four steps. What one mark stands for. What each axis
measures, and in what unit. Where each axis starts. Where the numbers came from. Now you make a
figure, and the same four answers are what you write down in code.

A plot in ggplot2 is built from three parts.

**The data**: a data frame, one row per observation, as every section since tidy data has
used.

**The mappings**: which column goes where. Flipper length along the bottom, body mass up the
side, species as colour. You write these inside `aes()`, short for aesthetics, the visual
properties of a mark.

**The geom**: what kind of mark. Points for a scatter plot, bars for a histogram or a count,
boxes for a boxplot.

You join the parts with `+`. Change the geom and the same data, mapped the same way, become a
different picture.

Two traps come up early. Inside `aes()` means "let this vary with a column". Outside it means
"make every mark this". Write `colour = "blue"` inside and ggplot2 treats "blue" as data. And a
histogram's bars depend on bins you did not choose unless you choose them: set their width and
where they start.

Then finish the figure as Book 0 asked: axis titles with units, and a line saying where the data
came from. Save it to `output/` with `ggsave()`, from the script, at a size you write down. Never
export it with the mouse. When the data change, rerun the script and every figure is redrawn
from them.

**Figure.** The counts behind the first illustration's histogram of penguin body mass: bins 500 g wide from 2500 g, each including its left edge. The tallest bin, 3500 to under 4000 g, holds 94 of the 342 penguins with a body mass. The same counts are what the code writes to output/ beside the figure.

*What the figure shows:* A bar chart of eight body-mass bins: 9, 62, 94, 59, 51, 34, 29 and 4 penguins, from 2500 to under 3000 g up to 6000 to under 6500 g.

**Must know points for you.**

- Write a colour or size inside `aes()` only when it should vary with a column. Inside, a fixed value such as "blue" is treated as data. You get the wrong colour, and a legend explaining a value that does not exist.
- Read every message and warning ggplot2 prints. "Removed 2 rows" means your figure shows fewer observations than your data frame holds. Say how many it shows, in the caption.
- The error is to think a histogram shows the shape of the data. It shows the data cut into bins someone chose. Set `binwidth` and `boundary` in the code, try more than one width, and keep the counts per bin in a file.
- A bar chart's value axis starts at zero, because a bar's value is its length. A boxplot or a scatter plot need not, because position carries the value.
- Every axis title names the quantity and its unit, and every figure carries a source line. A figure without them is one a reader cannot check, which Book 0 taught you to refuse.
- Save every figure with `ggsave()` from the script, with its width, height and units written in. A figure exported with the mouse cannot be redrawn when the data change, and nobody can tell which version of the data made it.
- When a trainee's thesis figure looks wrong, ask for the code before the picture. The mapping, the bins and the rows removed are all in the code; none is visible in the image.
- The grammar guarantees that the figure draws your data faithfully. It cannot guarantee that the data are right, that the comparison is fair, or that a pattern means anything. Those questions come before the plot and after it.

**Exercise 1** (calculation). Add to your penguin script a histogram of flipper length. Use bins 10 mm wide starting at
170 mm, each including its left edge. Give it an axis title with its unit, and a source line.
Save it to `output/flipper_histogram.png` at 15 cm by 10 cm. Write the counts per bin to
`output/flipper_histogram_counts.csv`. Say how many penguins the figure shows.

**Exercise 2** (critique). A colleague makes the figures for her thesis by running code in the console. Then she clicks
Export in RStudio's plot pane and chooses "Save as image". She drags the size until it looks
right. After a data correction, she has to remake eleven figures. Say what is wrong
with this way of working and what she should do.

**Exercise 3** (teaching). A journalist has three minutes. She has a bar chart from a press release. One district's bar for
"adults screened" looks five times another's, and the axis starts at 9,000.
Explain what she should ask for, without jargon.

**Exercise 4** (retrieval). Without looking back, name the three parts of a ggplot2 plot, and two choices that change a
histogram's bars without changing the data.

**1.** In this line, name the data, each aesthetic mapping, and the geom.

```r norun
ggplot(clinic, aes(x = age_years, y = bmi)) + geom_point()
```

**2.** In each line, say whether the colour is mapped or set, and what the points will look like.

```r norun
ggplot(clinic, aes(x = age_years, y = bmi, colour = sex)) + geom_point()
ggplot(clinic, aes(x = age_years, y = bmi)) + geom_point(colour = "darkgreen")
```

**3.** Five made-up values: 1.2, 1.8, 2.1, 2.9 and 3.0. A histogram uses `binwidth = 1` and
`boundary = 1`, with ggplot2's default for which edge a bin includes. How many values go in the
bin from 1 to 2, and how many in the bin from 2 to 3? Then answer again with `closed = "left"`.

**4.** Read the penguin file.

```r
library(readr)
library(dplyr)
library(ggplot2)

penguins_raw <- read_csv(
  here::here("data-raw", "penguins_raw.csv"),
  show_col_types = FALSE
)
```

```output

Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union
```

Draw a boxplot of body mass by island, with axis titles. Then give the median and the quartiles
the boxes are drawn from, with the number of body masses behind each box.

**5.** Read the penguin file.

```r
library(readr)
library(dplyr)
library(ggplot2)

penguins_raw <- read_csv(
  here::here("data-raw", "penguins_raw.csv"),
  show_col_types = FALSE
)
```

```output

Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union
```

Draw a scatter plot of culmen depth against culmen length, one panel per species. The culmen is
the ridge of the bill. Give axis titles that carry units, and a source line. Save it to
`output/culmen.png` at 18 cm by 8 cm, and show that the file exists.

**6.** Read the penguin file.

```r
library(readr)
library(dplyr)
library(ggplot2)

penguins_raw <- read_csv(
  here::here("data-raw", "penguins_raw.csv"),
  show_col_types = FALSE
)
```

```output

Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union
```

Draw a bar chart of the number of rows for each value of `Sex`, with axis titles. Give the
heights of the bars, and say what the third bar is.

**7.** A colleague wants all points dark red, and writes:

```r norun
ggplot(penguins_raw, aes(x = `Flipper Length (mm)`, y = `Body Mass (g)`, colour = "darkred")) +
  geom_point()
```

The points come out pinkish red, and a legend says "darkred". She decides her version of R
"cannot show dark red". Find what broke.

**8.** You and a colleague run the same script on the same penguin file. Your histogram of body mass,
made with `geom_histogram()` and no other arguments, has a different shape from hers. You have
ggplot2 {{n:ggplot2_version}}; she has 4.0.3. She concludes one of the two data files must be corrupt. Say what
is more likely, and how to make the two figures agree.

**9.** A colleague used to the pipe writes:

```r
library(readr)
library(ggplot2)

penguins_raw <- read_csv(
  here::here("data-raw", "penguins_raw.csv"),
  show_col_types = FALSE
)
```

```r error
ggplot(penguins_raw, aes(x = `Flipper Length (mm)`, y = `Body Mass (g)`)) |>
  geom_point()
```

```output
Error in `geom_point()`:
! `mapping` must be created by `aes()`
ℹ Did you use `%>%` or `|>` instead of `+`?
```

Read the error. Say what broke and fix it.

**10.** A made-up thesis figure caption says: "Figure 3. Body mass of all {{n:penguins_rows}} penguins, by species." The
code was:

```r
library(readr)
library(ggplot2)

penguins_raw <- read_csv(
  here::here("data-raw", "penguins_raw.csv"),
  show_col_types = FALSE
)

ggplot(penguins_raw, aes(x = Species, y = `Body Mass (g)`)) +
  geom_boxplot()
```

```output
Warning message:
Removed 2 rows containing non-finite values (`stat_boxplot()`).
```

Find what is wrong with the caption, using only what R printed.

**11.** A made-up draft says: "As Figure 1 shows, most penguins weigh between 3.5 and 4 kg." Draw the
histogram that would back the claim, and count the penguins in that range. Say whether the
claim holds, and what the figure does not establish.

**12.** A made-up district officer says: "Give me one figure comparing BMI in men and women from that
American survey, for my slides." Make it from the joined NHANES files for adults aged 20 or
over, save it to `output/`, and say what the figure does not establish.

