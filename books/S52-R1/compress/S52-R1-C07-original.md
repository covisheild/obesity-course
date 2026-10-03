# S52-R1-C07 · A project folder, and paths that work on someone else's computer

**Definition.** A project folder is one folder that holds everything for one analysis. In this book it has
three folders inside it and one file at the top. `data-raw/` holds the raw data as it arrived,
and code reads from it but never writes to it. `code/` holds the scripts. `output/` holds every
file the code produces, which can always be made again by running the code. A README at the top
says what the project is and how to rerun it.

A path is the address of a file. An absolute path starts from the top of one computer's disk,
such as `C:/Users/priya/Documents/thesis/data-raw/heights.csv`, so it names a place that exists
on one computer only. A relative path starts from the working directory, the folder R treats as
its current home when it looks for a file or saves one, such as `data-raw/heights.csv`. It works
on any computer where the project folder has the same layout inside.

The function `here()`, from the here package, builds a path from the project root, the top
folder of the project. It finds the root by starting at the working directory and climbing
upwards. It stops at the first folder that holds a marker, such as a file called `.here`, an
RStudio project file or a `.git` folder. The same line of code therefore finds the same file from any
folder inside the project, on any computer.

**In plain terms.** Give every analysis its own folder. Name the folder after the analysis, for example
`penguin_mass` or `school_heights_2026`, with no spaces in the name. Inside it, make three
folders:

```table
| Folder | What goes in it | Who writes to it |
| data-raw/ | the data exactly as it arrived | you, once, when it arrives; never the code |
| code/ | your scripts | you |
| output/ | tables, figures and cleaned files the scripts make | only the scripts |
```

Put a short plain-text file called README at the top. It says what the project is, where the
data came from, and how to run it again.

Now the addresses. A file's address is its path. `C:/Users/priya/Documents/thesis/data-raw/heights.csv`
is the full address on Priya's laptop. On your laptop there is no `C:/Users/priya` folder, so that
address leads nowhere. `data-raw/heights.csv` says "from where I am now, go into data-raw". It
works on any computer, as long as R starts from the top of the project folder.

That last condition is the weak spot. R does not always start from the top. So use `here()`,
which finds the top of the project for you: `here("data-raw", "heights.csv")` gives the full
address on whichever computer runs it.

Two habits follow. Never write a full address from your own computer into a script. And never
start a script with `setwd()`, the function that moves R's current home to a named folder.
Whatever folder you name exists only on your computer.

**Must know points for you.**

- The error is to believe that a script which runs on your computer will run on another. An address that starts with `C:/Users/` or `/home/` names a folder on one computer. Before you send a script, search it for such addresses and replace each one with `here()`.
- Build every file address with `here()`, starting from the project root: `here("data-raw", "file.csv")` to read, `here("output", "table.csv")` to write. The line then works from any folder inside the project.
- A script that starts with `setwd()` and a folder name works only on the computer it was written on. When you receive one, delete that line, open the project folder, and change the paths to `here()`. Do not create the other person's folders on your own disk to make it run.
- No code ever writes into `data-raw/`, and no one edits a raw file there. A correction typed into the raw file cannot be told apart from the original later. The analysis can then no longer be rerun from the data as it arrived. Put the correction in code, and write the corrected file to `output/`.
- Everything in `output/` can be deleted and made again by running the code. If a file there cannot be remade, part of the analysis was done by hand, and that part is the one to find.
- A trainee's script fails on your computer with "does not exist". Look at the address in the failing line before you look at the data, and check whether it names a folder on their computer.
- Name files with no spaces, no brackets and no capital letters used to tell two files apart. `Final data (2).xlsx` and `final data.xlsx` are a quarrel waiting to happen. Rename the copy you keep as raw data once, when it arrives, and record the original name in the README.
- A tidy folder and safe addresses fix only where files are. They do not make an analysis correct, and they do not make it rerun if a package is missing. Do not accept "the paths are relative" as proof that someone else can rerun the work.

**Exercise 1** (retrieval). Without looking back, write the line that reads a file called `heights.csv` from the project's
`data-raw` folder so that it works on any computer. Say why a line starting with `setwd()`
does not belong above it.

**Exercise 2** (design). You are starting a thesis analysis of weight and height measured in a school health camp. The
camp team will give you one CSV file, a plain-text table, exported from their data-entry form.
Lay out the project folder. Give it a name, and list the folders and the files you expect in
each. Say which folders your code may write to. Then write the one line that reads the camp file.

**Exercise 3** (teaching). A first-year resident has ten minutes and a whiteboard. Her script ran on her laptop and
stopped on yours with "does not exist". Teach her why, and what to change.

**1.** The project root is `~/project`. Write the `here()` call that gives the address of a file
called `heights.csv` inside `data-raw`, and run it.

**2.** Say whether each address is absolute or relative.

a. `C:/Users/ravi/Documents/thesis/data.csv`
b. `data-raw/camp_export.csv`
c. `/home/ravi/thesis/output/table1.csv`
d. `output/figures/bmi_histogram.png`
e. `D:/MD thesis/final.xlsx`

**3.** The project root is `~/project`. Predict what this line prints, then run it. Does running it
create a folder called `figures`?

```r norun
here::here("output", "figures", "bmi_histogram.png")
```

**4.** Read `penguins_raw.csv` from the project's `data-raw` folder, building the address with
`here()`. Give its number of rows and columns with `dim()`.

**5.** Where does each of these files belong in the project folder: `data-raw/`, `code/`, `output/`,
or the top?

a. `penguins_raw.csv`, exactly as downloaded
b. `analysis.R`
c. `species_counts.csv`, written by your script
d. `mass_histogram.png`, saved by your script
e. `README`
f. a copy of `penguins_raw.csv` in which you corrected one value by hand

**6.** In the project, make the `output` folder from code, check that it now exists, and list the
folders at the top of the project.

**7.** A colleague's script begins like this. Run it. Find the line that broke, and say why it
looked reasonable to the person who wrote it.

```r error
library(readr)
setwd("C:/Users/priya/Documents/thesis")
penguins_raw <- read_csv("data-raw/penguins_raw.csv", show_col_types = FALSE)
```

```output
Error in setwd("C:/Users/priya/Documents/thesis") :
  cannot change working directory
```

**8.** A resident wants a quick test run on fewer rows. Her script keeps the first 300 rows and saves
them. She runs it twice. Run the two runs below. Find the line that broke, and say why nothing
looked wrong on the first run.

```r
library(readr)
library(here)
# first run
penguins_raw <- read_csv(here("data-raw", "penguins_raw.csv"), show_col_types = FALSE)
nrow(penguins_raw)
penguins_test <- head(penguins_raw, 300)
write_csv(penguins_test, here("data-raw", "penguins_raw.csv"))
# second run, the same lines again
penguins_raw <- read_csv(here("data-raw", "penguins_raw.csv"), show_col_types = FALSE)
nrow(penguins_raw)
```

```output
here() starts at ~/project
[1] 344
[1] 300
```

**9.** Your guide says at a meeting: "Send me the project folder. If it runs on your laptop, it will
run on mine."

Test the second half of that claim before you send anything. The project holds this script:

```r file=code/count_rows.R
library(readr)
penguins_raw <- read_csv(here::here("data-raw", "penguins_raw.csv"), show_col_types = FALSE)
nrow(penguins_raw)
```

Then say what your test does not establish.

**10.** A co-author writes: "Just email me the cleaned file. I don't need your code. The cleaned file
is the result."

The project's script reads the raw penguin file and writes a file with the rows that have a
body mass recorded to `output/penguins_with_mass.csv`. Show that the cleaned file is
disposable: delete it, remake it from code, and check that the remade file is identical to the
first. Then say what this does not establish.

