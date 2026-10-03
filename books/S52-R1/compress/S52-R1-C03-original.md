# S52-R1-C03 · Objects and names

**Definition.** An object is a value R holds in memory under a name. The assignment `name <- value` makes one:
R works out the right-hand side completely, then stores the result under the name on the
left. An assignment prints nothing. Typing the name alone prints the value.

Assigning to a name that already exists replaces its value. The name keeps no link to how the
value was made, so an object worked out from another object does not change when that other
object is later given a new value.

Names are case sensitive: `bmi` and `BMI` are different names. A name may contain letters,
digits, `.` and `_`, and no spaces. It must start with a letter, or with `.` not followed by a
digit.

The objects that exist at a given moment form the workspace, which `ls()` lists and RStudio
shows in its Environment pane. The workspace holds whatever has been run, in any order, in the
current session (R from the moment it starts until it is closed or restarted), whether or not
those lines are in the script.

The tidyverse style guide asks for names in lower case, with words joined by `_` (snake case),
and for `<-` rather than `=` for assignment. R accepts `=` in most places.

"Variable" now has two meanings in this book, and a third comes later. In Book 0's algebra, a
variable is a letter standing for a number. In R, an object's name is often called a variable.
Later, a variable will also mean one column of a table of data.

**In plain terms.** The last section ended with numbers typed straight into each line. This one gives them names.

```r
weight_kg <- 72
```

Read the arrow `<-` as "gets": weight_kg gets 72. R prints nothing. It has stored 72 under the
name `weight_kg`. Type the name, and R prints the value back.

```r
weight_kg
```

```output
[1] 72
```

A name is a label stuck on a value. Three things follow from that.

- **Give the same name a new value, and the old one is gone.** No warning.
- **A name holds a value, not a sum.** If you work out a BMI from `weight_kg` and then change
  `weight_kg`, the BMI stays as it was. It changes only when you run its line again.
- **R reads names exactly.** `Weight_kg` with a capital W is a different name. A name cannot start
  with a digit and cannot hold a space.

The objects you have made so far sit in a list called the workspace. RStudio shows it in the
Environment pane, and `ls()` prints it. That list is not your script. It holds every line you ran
today, in whatever order you ran it, including lines you typed only in the console.

Write names in small letters, with `_` between words, and put the unit in the name:
`height_cm`, `height_m`, `bmi`. Then a line such as `height_m <- height_cm / 100` explains itself.

The word "variable" now means two things. In Book 0's algebra, a variable was a letter standing
for a number. In R, people also call a named object a variable. A third meaning, a column in a
table of data, comes later in the book. The context tells you which is meant.

**Must know points for you.**

- The error is to think a name holds a formula. `bmi <- weight_kg / height_m^2` stores one number. Change the weight afterwards and `bmi` keeps the old answer until you run its line again. After any correction, run the script from the top.
- The workspace is not your script. It holds whatever you ran today, in any order, including lines typed only in the console. Trust a result only after it has come from running the script from the top.
- Assigning to a name that already exists replaces its value without any warning. Give each thing its own name, such as `bmi_visit1` and `bmi_visit2`, rather than reusing `bmi`.
- Put the unit in the name: `height_cm`, `height_m`, `weight_kg`. A line that divides `height_cm` by 100 to make `height_m` can then be checked by reading it.
- "object 'x' not found" usually means a typing slip or a wrong capital letter, or a line that makes `x` was never run. Check the spelling first, then whether the line that creates it has run.
- A good name makes code readable, not correct. `bmi` can still hold the wrong number. Names help a reviewer follow the steps; only checking the values tells you they are right.

**Exercise 1** (retrieval). From memory: you run `bmi <- weight_kg / height_m^2`, then `weight_kg <- 74`. What does `bmi`
hold now, and what must you do to bring it up to date? Then name two things an R name may not
do.

**Exercise 2** (design). A classmate's script reads:

```r
W <- 66
H <- 158
x <- W / (H / 100)^2
x
```

```output
[1] 26.43807
```

Rewrite it so that every name follows this book's style and says what it holds, with its unit.
Add a comment for the step that would puzzle a reader. Check that your version gives the same
answer.

**Exercise 3** (teaching). A first-year resident has ten minutes and a whiteboard. They corrected a participant's height
in the console and say their BMI results are now fixed. Teach them why they may not be.

**1.** What does the last line print?

```r norun
a <- 5
a <- a + 2
a
```

**2.** Which of these names will R accept for an object? Try each one with `<- 1` to check.

`bmi_2024`, `2024_bmi`, `bmi.2024`, `bmi 2024`, `.bmi`, `_bmi`

**3.** Predict what the last line prints, then run the lines to check.

```r norun
x <- 10
y <- x * 2
x <- 3
y
```

**4.** The first penguin in the Palmer file weighed 3750 g. Store that value in an object whose name
gives the unit. Then make a second object holding the weight in kilograms, and print it.

**5.** A made-up adult weighs 81 kg and is 172 cm tall. Write lines that store the weight and the
height as they were recorded, make the height in metres, make the BMI, and print it. Use names
that carry units.

**6.** The second and third penguins in the Palmer file weighed 3800 g and 3250 g. Store each weight in
its own object, make an object holding the difference between them in kilograms, and print it.

**7.** A resident works out BMI for two made-up patients and reports patient A's value. Here is the
script and what it printed.

```r
bmi <- 72 / 1.6^2       # patient A
bmi <- 58 / 1.52^2      # patient B
bmi                     # patient A's BMI, for the report
```

```output
[1] 25.10388
```

They write "Patient A: BMI 25.1 kg/m^2". Find what broke, and say why the wrong answer looks
reasonable.

**8.** This script stops with an error. Find the cause.

```r error
weight_kg <- 60
height_m <- 1.62
weight_kg / Height_m^2
```

```output
Error: object 'Height_m' not found
```

**9.** A line in a made-up thesis reads as follows. "The weight of participant 12 was corrected from 47
kg to 74 kg, a transposition error. The BMI was recalculated." The participant's height is 1.58 m.
Write the lines that record this correction and give both BMIs. Then say what your lines do
not establish.

**10.** A made-up thesis methods section says: "Height was recorded in centimetres and converted to
metres before BMI was calculated." Participant 2's register entry reads: weight 64, height 1.63.
Write the lines the sentence describes for participant 2, with names that carry units. Run
them. Then say what the methods sentence does not establish.

