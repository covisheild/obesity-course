# S52-R1-C04 · Vectors, types and NA

**Definition.** A vector is an ordered set of values that R holds as one object under one name. The
function `c()` combines values into a vector, in the order given.

Every element of a vector has the same type. This book uses three types. Numeric values
are numbers (R keeps two kinds, integer and double, and treats both as numbers). Character
values are text, printed inside quotation marks. Logical values are `TRUE` and `FALSE`.

When values of different types are combined, R converts all of them to the highest type in
the order logical, then numeric, then character. This conversion is called coercion. A
single text value therefore turns a vector of numbers into a vector of text, and functions
that compute on numbers, such as `mean()`, return no number for it.

Arithmetic on vectors is done element by element: the first element with the first, the
second with the second. A single number is repeated to match the length of the longer
vector. A comparison, such as `>` or `==`, returns a logical vector of the same length.

`NA`, for "not available", marks a value that is missing. Almost any arithmetic or
comparison that involves `NA` returns `NA`, because the result cannot be known. The
exception is a logical operation whose answer does not depend on the missing value. The
function `is.na()` returns `TRUE` for each element that is `NA`. The comparison `x == NA`
returns `NA` for every element and finds nothing.

Square brackets after a vector's name pick out elements, by position or by a logical vector
of the same length.

What R prints is a rounded display. The value R stores is held in binary, carries more
digits than it shows, and for most decimal fractions is a close approximation, not the
exact decimal.

**In plain terms.** The last section gave a name to one value at a time. Most data come as many values of the
same kind: the weights of every child in a class, the dates of every clinic visit. In R, a set
of values in a row, kept in order under one name, is a vector. You build one with `c()`, which
stands for combine:

```r
height_cm <- c(152, 160.5, 171)
height_cm
```

```output
[1] 152.0 160.5 171.0
```

The `[1]` at the start of the printed line is not part of the data. It tells you that the
line begins with the first element. In a long vector, each new line starts with the position of
its first value.

A vector holds one type of value. The three you need now are numbers (numeric), text
(character) and `TRUE` or `FALSE` (logical). R shows you which one it holds. Text is printed
inside quotation marks:

```r
sex <- c("female", "male", "female")
sex
```

```output
[1] "female" "male"   "female"
```

Arithmetic works on the whole vector at once, element by element. Divide the heights by 100
and every height turns into metres:

```r
height_cm / 100
```

```output
[1] 1.520 1.605 1.710
```

The 100 was used three times, once for each height. R repeats a single number as often as
the longer vector needs. That is why one line converts a thousand heights as easily as three.

A comparison asks the same question of every element and answers `TRUE` or `FALSE` for each:

```r
height_cm > 155
```

```output
[1] FALSE  TRUE  TRUE
```

Square brackets pick elements out. A number inside them is a position. A logical vector
inside them keeps the elements where it says `TRUE`:

```r
height_cm[2]
height_cm[height_cm > 155]
```

```output
[1] 160.5
[1] 160.5 171.0
```

Two more things will trip you up if nobody tells you, and each has its own example below.
First, if one value in a vector is text, the whole vector becomes text. Second, R writes `NA`
where a value is missing, and `NA` spreads: almost anything you compute from it is also `NA`.

**Figure.** The first ten body masses in the practice file, in kg, as R holds them after dividing by 1000. Penguin 4 has no bar: its value is NA, which is not zero and not small but unknown. Penguins 8 and 10 are the two above 4 kg.

*What the figure shows:* A bar chart of body mass in kilograms for penguins 1 to 10. Nine bars lie between 3.250 and 4.675 kg. There is a gap with no bar at penguin 4, labelled NA.

**Must know points for you.**

- The error is to believe a column that looks like numbers holds numbers. One text value, such as "71 kg" or "not weighed", turns the whole vector into text, and `mean()` then returns `NA`. Before you compute anything, print the vector and look for quotation marks, or ask `typeof()`.
- `x == NA` never finds a missing value. It returns `NA` for every element. Use `is.na(x)`, and refuse any count of missing values that was made with `==`.
- When a sum or a mean comes back `NA`, R is telling you a value is missing. Do not make the `NA` go away by writing a 0 in its place. Zero is a weight of nothing, and it pulls the mean down. Find out how many values are missing first.
- "NA" typed inside quotation marks is the two letters N and A, not a missing value. `is.na("NA")` is `FALSE`, and the vector it sits in has become text.
- R prints fewer digits than it stores, and stores most decimals only approximately. Never test two decimals with `==`. Report a number to the precision of the measurement behind it, whatever R prints.
- `is.na()` finds only R's own `NA`. Suppose a raw file writes a missing weight as -99 or 999. To R, that is a weight of -99 or 999, and it goes into every mean until you tell R what the code means. A later section shows how to declare such codes when you read the file.
- When a trainee's mean comes back as `NA`, do not fix it for them. Ask them to print the vector and point to the quotation marks or the `NA`. The habit of looking is the thing worth teaching.

**Exercise 1** (critique). A made-up thesis appendix shows this code and says "the mean haemoglobin of the five women
could not be calculated because R gave an error".

```r
hb_g_dl <- c(11.2, 12.5, "9.8*", 13.1, 10.4)
mean(hb_g_dl)
```

```output
[1] NA
Warning message:
In mean.default(hb_g_dl) : argument is not numeric or logical: returning NA
```

Haemoglobin is measured in grams per decilitre (g/dL). Say what actually happened, what the
asterisk probably was, and how the analysis should go on without editing anything by hand.

**Exercise 2** (retrieval). Without looking back, name the three types of vector this section uses. Say which one wins
when they are mixed in `c()`. Then give the line that finds the missing values in a vector `x`.

**1.** Make a vector called `height_cm` holding the heights 98, 102.5 and 110 cm. Then print the
same heights in metres.

**2.** Before running them, say what type of vector each line makes and what it prints. Then run
them and check.

```r norun
c(1, TRUE, "no")
c(0, TRUE, FALSE)
```

**3.** Before running them, say what each line prints.

```r norun
c(2, NA, 5) + 1
c(2, NA, 5) > 3
```

**4.** The column "Flipper Length (mm)" in `penguins_raw.csv` gives flipper lengths in millimetres.
Its first ten values are 181, 186, 195, a missing value, 193, 190, 181, 195, 193 and 190. Make a vector of them with a
name that carries the unit. Print them in centimetres, and say which penguins have a flipper
longer than 190 mm.

**5.** The first ten body masses in `penguins_raw.csv` are 3750, 3800, 3250, a missing value, 3450,
3650, 3625, 4675, 3475 and 4250 g. Print the eighth penguin's body mass in kilograms. Then
print the body masses of the first three penguins in grams.

**6.** Using the same ten body masses, make a vector of only the known body masses, in kilograms,
and count how many there are.

**7.** A colleague wants the tallest child's height from a made-up school register. Their code
and its output are below. They report "the tallest child is 98 cm". Find what broke, and
say why the answer looks reasonable.

```r
height_cm <- c("98", "102", "110")
max(height_cm)
```

```output
[1] "98"
```

**8.** A colleague checks a made-up list of six BMI values, in kg/m^2, for missing entries. Their
code and output are below. They write "no BMI values are missing". Find what broke.

```r
bmi <- c(22.4, 31.0, NA, 27.9, NA, 19.6)
bmi == NA
```

```output
[1] NA NA NA NA NA NA
```

**9.** A colleague marks which of five made-up adults have a BMI of 25 kg/m^2 or more. One BMI was
not recorded. Their code and output are below, and they report "four of the five adults
have a BMI of 25 or more". Find what broke, and say why it looks reasonable.

```r
bmi <- c(22.1, 27.4, "NA", 30.2, 25.8)
bmi >= 25
```

```output
[1] FALSE  TRUE  TRUE  TRUE  TRUE
```

**10.** A made-up draft report says: "Body mass was recorded for all of the first ten penguins in
the practice file." The first ten values of "Body Mass (g)" are as in problem 5. Check the
sentence with code. Then say what your check does not tell you.

**11.** In a made-up meeting, someone says: "Of the first ten penguins in the file, two weighed more
than 4000 g." The first ten body masses are as in problem 5. Check the claim with code, and
then say what the result does not establish.

