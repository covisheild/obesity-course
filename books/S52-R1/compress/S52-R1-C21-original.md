# S52-R1-C21 · Top to bottom in a fresh session, with one command

**Definition.** Hidden state is anything a script uses that the script itself did not make. It may be an object
left in the workspace by a line typed in the console, a package attached earlier in the session,
or a file made by hand. A script that leans on hidden state runs for the person who has that state
and stops, or gives a different answer, for everyone else.

A script is tested for hidden state by running all of it, from the first line to the last, in a
fresh session. A fresh session is a new R process whose workspace is empty. It has attached no
package beyond R's defaults. The one command for this is `Rscript code/analysis.R`, typed in a terminal
whose working directory is the project root. `Rscript` starts a new R and does not restore a
saved workspace. It runs the file's lines in order and stops at the first error. `source()` also runs a file,
but in the current workspace. So it tests nothing about hidden state unless R has just been
restarted.

A script that passes this test also writes every result it makes into `output/` with code. It
sets the random-number seed with `set.seed()` before any random step. It ends with
`sessionInfo()`, which prints the version of R and of every attached package. Those versions are a record, not a
guarantee: a computer with other versions may still give another result.

**In plain terms.** Here is the trap with a script that works on your computer. While you work, R remembers. Every
object you made, in the script or typed in the console, sits in the workspace. Every package you
loaded stays loaded. Your script can use all of that without saying where it came from. Then a
colleague runs it on their computer, where none of it exists, and it stops.

So test the script the way a stranger would run it. Start a new R with nothing in it, and run
every line from the top. There are two ways to do that.

- In RStudio, restart R (the menu Session, then Restart R), then run the whole script.
- In a terminal, in the project folder, type one command: `Rscript code/analysis.R`. It starts a
  new R, runs the file from the first line to the last, and stops at the first error.

The second way is the one to write in your README, because it is one line anyone can type.

If the script passes, three more habits make its result the same every time.

- It writes every table and figure into `output/` with code. Nothing is copied off the screen.
- If any step is random, `set.seed()` comes first, with a number you choose. The same seed gives
  the same "random" picks on every run.
- Its last line is `sessionInfo()`, which prints the version of R and of each package. That is
  the record of what made the result.

Two tools for later rungs grow out of this. Git keeps a record of every change to the script. You
meet it in the next rung of this subject. renv fixes the package versions, so that another
computer uses the same ones. It comes two rungs up.

**Must know points for you.**

- The error is to think that a script which runs on your computer is a script that runs. Your session may be supplying an object or a package the script never makes. Before you send a script to anyone, run it with `Rscript code/analysis.R` from the project folder. Send it only when it reaches the last line.
- `rm(list = ls())` empties the workspace and leaves every package loaded. `source()` runs a file in the workspace you already have. Neither is a fresh session. Restart R, or use `Rscript`.
- When a script stops with "object not found" on someone else's computer, look for the line that makes that object. If it is missing, the line lived only in your console. Add it to the script, above the line that uses the object.
- Put `set.seed()` with a number you write down before any random step: a random sample of rows to check, a random allocation, a simulation. Without it nobody, including you next month, can get the same picks again.
- End every analysis script with `sessionInfo()`, and keep its printout with the outputs. When a reviewer reruns your work and gets a different number, the version lines are the first place to look.
- A number in your thesis that you typed from the screen has no line of code behind it. Write every table to `output/` with code, and copy numbers into the text from those files. Rung 2 of this subject teaches a document in which the code writes the number itself.
- A trainee says "it runs, I checked". Ask how. If the answer is "I ran it in RStudio", ask them to restart R and run it again in front of you. The test takes one minute, and it is the one their examiner, or their reader, will do.
- One command in a fresh session tests the script against your computer only. It cannot show that a colleague with other package versions gets the same numbers, and it cannot show that the numbers are right. Say "it reruns on my computer", and no more, until someone else has run it.

**Exercise 1** (retrieval). Without looking back, say what "hidden state" is. Name the one command that tests a script for
it. Say why `rm(list = ls())` is not enough.

**Exercise 2** (build). Take the script you have been building through this book. Restart R, or open a terminal in the
project folder, and run it with `Rscript code/analysis.R`. Fix every error in the script, one at
a time, until it reaches the last line. Then make sure that it writes its outputs to `output/`
with code, that any random step follows `set.seed()`, and that it ends with `sessionInfo()`.
Delete `output/` and run the command again. Write the command into your README.

**Exercise 3** (teaching). A journalist has three minutes. A research group has just been told that its published analysis
"does not reproduce". The journalist asks what that usually means, and whether it means the
result is false. Answer them.

**1.** Predict whether these lines print the same three numbers twice, then run them.

```r norun
set.seed(11)
sample(10, 3)
set.seed(11)
sample(10, 3)
```

**2.** Predict what the last line prints, then run all three.

```r norun
height_cm <- c(132, 141, 150)
rm(list = ls())
exists("height_cm")
```

**3.** Predict what the last line prints, then run all three. Does `rm(list = ls())` unload dplyr?

```r norun
library(dplyr)
rm(list = ls())
"package:dplyr" %in% search()
```

**4.** Write a script, `code/analysis.R`, that reads the penguin file from `data-raw/`, counts the rows
of each species, and writes the counts to `output/species_counts.csv`. It must run on a fresh
copy of the project, where `output/` does not exist. Run it with `Rscript`, then show the file it
wrote.

**5.** Write a script that loads readr and dplyr and ends with `sessionInfo()`. Run it with `Rscript`,
and read off the version of dplyr that produced the result. Then get the same version number
with one line of code instead of reading it by eye.

**6.** You want ten penguin rows picked at random, for a colleague to check against the field
notebooks. She must get the same ten when she runs your script. Write the lines that pick ten
row numbers from the penguin file with seed 52. Show that running them twice gives the same ten.

**7.** Meera's script reports the mean body mass of the penguins. Earlier in the same session she had
typed two lines in the console. Here is everything her session ran, and what it printed:

```r
library(readr)
library(dplyr)
penguins_raw <- read_csv(here::here("data-raw", "penguins_raw.csv"),
                         show_col_types = FALSE)
penguins_raw <- penguins_raw |>
  filter(Island == "Biscoe")
```

```output

Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union
```

Her script, `code/analysis.R`, run line by line in that session:

```r
library(dplyr)
penguins_raw |>
  summarise(mean_mass_g = mean(`Body Mass (g)`, na.rm = TRUE))
```

```output
# A tibble: 1 × 1
  mean_mass_g
        <dbl>
1       4716.
```

She writes "mean body mass 4716 g" in her draft. What broke, and what is the right number for
the whole file?

**8.** Ravi checks his script before sending it. In his session the penguin file is already read. He
runs the script with `source()`, sees no error, and tells his guide it is reproducible:

```r
library(readr)
penguins_raw <- read_csv(here::here("data-raw", "penguins_raw.csv"),
                         show_col_types = FALSE)
```

```r file=code/analysis.R
n_rows <- nrow(penguins_raw)
```

```r
source(here::here("code", "analysis.R"))
n_rows
```

```output
[1] 344
```

What is wrong with his check?

**9.** A thesis's methods chapter says: "All analyses were performed in R and are fully reproducible."
The candidate gives you the project folder. Decide what to run to test the sentence, write it
down, and then say what a successful run would still not establish.

**10.** In a department meeting a colleague says: "My script gives the same table every time. I ran it
twice yesterday in RStudio and got the same numbers." His script reads the penguin file and
writes the number of rows of each sex to `output/sex_counts.csv`. Decide what would actually
test his claim, run it, and say what your result does not establish.

