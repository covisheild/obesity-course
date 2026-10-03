# S52-R1-C02 · Installing R and an editor; the console and the script

**Definition.** R is a program that reads instructions written in the R language and carries them out.
RStudio is a separate application, an integrated development environment (IDE), that makes R
easier to use: it gives a script editor, the console, and panes for objects, plots and help
pages. R is installed first, then RStudio. The printed outputs in this book came from R
{{n:r_version}}; newer releases exist.

The console is the pane in which R shows a prompt, `>`, and waits for one instruction. Each
instruction typed there is run once. If it is an expression, its value is printed and then
lost. If the instruction is incomplete, R shows `+` instead of `>` and waits for the rest.

A script is a plain-text file of R code, saved with a name ending in `.R`. Its lines are run in
order, from the top. Together with the data files, the script is the lasting record of an
analysis: from it, every result can be made again.

R does arithmetic with `+` (plus), `-` (minus), `*` (times), `/` (divided by) and `^` (to the
power of). It follows the order Book 0 taught. Brackets come first, then powers, then
multiplication and division, then addition and subtraction, left to right within each pair.

Everything after a `#` on a line is a comment. R ignores it; people read it.

An error message is R's statement that it could not carry out an instruction. It says what it
could not do and, for a line it could not read, where on the line it stopped.

**In plain terms.** You install two programs. R is the one that does the work: you give it an instruction, and it
carries it out. RStudio is the window you work in. Install R first, then RStudio, from their
own websites.

Open RStudio and you see several panes. Two matter today.

**The console** is where R waits for you. It shows a `>` sign. Type `2 + 3` after it and press
Enter. R prints `[1] 5`. The `[1]` only marks the first value on the line; ignore it for now. The
answer is printed once and kept nowhere. If you press Enter on an unfinished line, R shows `+`
and waits for the rest.

**The script** is a plain text file of instructions, one per line, saved with a name ending in
`.R`. Open one from the File menu: New File, then R script. Type your instructions there instead
of in the console. Put the cursor on a line and press Ctrl and Enter together. RStudio sends that
line to the console, and the answer appears there. Select every line and press Ctrl and Enter,
and the whole file runs from the top.

The difference is the whole point of this book. The console is a place to try things. The script
is what you keep. Tomorrow, or in a year, or on your guide's computer, the script makes the same
answers again.

R's arithmetic signs differ from Book 0's in two places. Times is `*`, not ×. Divided by is `/`,
not ÷. Powers are `^`, so 1.6 squared is `1.6^2`. The order of working is the one you already
know: brackets, powers, then times and divide, then plus and minus.

A `#` starts a comment. R skips everything after it on that line. Use comments to say why a line
is there.

When R cannot do what you asked, it prints an error message. Read it word by word. It usually
says exactly what went wrong.

**Must know points for you.**

- The error is to think the console keeps your work. It keeps a list of everything you typed, the wrong lines with the right ones, and nothing says which was which. Type into the console to try something. Put anything you want to keep into the script.
- R's signs are `*` for times, `/` for divided by and `^` for a power. Typing × or ÷ stops R with an error, and typing the letter x as times does too.
- `72 / 1.6 * 1.6` gives 72, not a BMI. R divides and multiplies from left to right. When you mean "divided by a product", put the product in brackets or use a power.
- Write a unit conversion as a line of code, with a comment, rather than doing it in your head and typing the result. A reader can then see that 160 became 1.6 because the register was in centimetres.
- When an answer comes out, check its size against what you expect before you use it. A BMI of 0.003 kg/m^2 or 72 kg/m^2 for an ordinary adult means the code is wrong, however cleanly it ran.
- When a trainee shows you a number from R, ask to see the script, not the console. If there is no script, ask them to write one and run it from the top before you look at the number.

**Exercise 1** (retrieval). Answer from memory, without R open. What does the console show when it is waiting for an
instruction? What does it show when your line is unfinished? Where should a line you want to keep be
written, and why?

**Exercise 2** (build). Start the habit. In RStudio, open a new script. Save it with a name of your choosing that has no
spaces and says what the file is for. In it, write lines that work out, for a made-up
adult who weighs 58 kg and is 152 cm tall:

1. the height in metres;
2. the BMI in kg/m^2.

Give each line a comment saying why it is there. Run the whole script from the top and write
down the two answers.

**Exercise 3** (teaching). A first-year resident has ten minutes and a whiteboard. They have been doing their thesis
calculations in the console "because it is faster". Teach them the difference between the
console and a script, and why it matters for a thesis.

**1.** Write one line of R that works out 45 plus 17 times 2. Before you run it, write down what you
expect it to print.

**2.** Write one line of R that divides 150 by the sum of 20 and 30.

**3.** Predict what each line prints, then run them to check.

```r norun
2^3 * 2
2^(3 * 2)
```

**4.** This book uses a file of {{n:penguins_rows}} rows of penguin measurements from near Palmer Station, Antarctica. The
first penguin in the file weighed 3750 g. Write one line of R that gives its weight in
kilograms, with a comment saying what the line does.

**5.** A made-up adult in a clinic register weighs 81 kg and is 172 cm tall. Write a short script, with
a comment on each line of code, that works out the height in metres and then the BMI in kg/m^2.
Give the BMI to one decimal place in your answer.

**6.** The first three penguins in the Palmer file have flipper lengths of 181, 186 and 195 mm. Write
a line of R that gives their average flipper length in centimetres, with a comment.

**7.** A made-up patient's weight was measured twice at one visit, 71.4 kg and 71.8 kg. A resident
wants the average of the two and writes:

```r
71.4 + 71.8 / 2
```

```output
[1] 107.3
```

They record 107.3 kg in the register. Find what broke, and say why the wrong answer can look
reasonable.

**8.** A resident saves this script and runs every line. R stops with an error. Find the cause.

```r error
# Height in metres
165 / 100
BMI of patient 2
68 / (165 / 100)^2
```

```output
Error: <text>:3:5: unexpected symbol
2: 165 / 100
3: BMI of
       ^
```

**9.** A line from a made-up thesis results chapter reads: "The mean weight of the three participants
in the pilot was 68.3 kg." The three weights in the pilot register are 64.2, 71.5 and 69.1 kg.
Check the sentence in R. Then say what your check does not establish.

**10.** In a made-up lab meeting, someone says this: "The first three penguins in the Palmer file
weighed 3750, 3800 and 3250 g. So the average penguin weighs 3.6 kg." Turn the claim into R, run it,
and say what the result does not establish.

