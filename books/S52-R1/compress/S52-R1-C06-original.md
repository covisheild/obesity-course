# S52-R1-C06 · Packages: where they come from and which version you have

**Definition.** A package is a collection of R functions, data and documentation that extends what base R,
the set of standard packages installed with R itself, can do. Most packages are distributed
through CRAN, the Comprehensive R Archive Network.

Installing a package, with `install.packages()`, downloads it from a repository such as CRAN
and stores it on the computer. It is done once per computer, and again only to change the
version. Loading a package, with `library()`, makes its functions available in the current R
session. It is done in every session that uses the package, and until it is done, R does not
find the package's functions.

Two attached packages may each have a function of the same name. Then the one attached later
masks the other: a call by that name runs the later one. `library()` prints a message naming
each masked function. The form `package::function()` calls a function from a named package,
whatever is attached, and loads the package if it is not loaded.

The tidyverse is a set of packages designed to work together. `library(tidyverse)` attaches
nine of them at once.

Every package has a version number, read with `packageVersion()`. R itself has one, held in
`R.version.string`. A package's behaviour, and the messages it prints, can change between
versions. The outputs printed in this book come from R {{n:r_version}} and the package
versions listed at the front of the book. Newer versions of R and of these packages exist.

**In plain terms.** The functions you have used so far, `c()`, `mean()` and `round()`, come with R. Thousands
more have been written by other people and shared in packages. A package is a bundle of
functions, with the help pages that explain them and sometimes some data. Most are kept on
CRAN, the Comprehensive R Archive Network, a set of websites from which R downloads them.

Using a package takes two steps, and they happen at different times.

1. **Install it, once per computer.** This downloads the package and stores it on your
   machine. You type it in the console, not in your script:

   ```r norun
   install.packages("dplyr")
   ```

2. **Load it, in every session.** This makes its functions available now. It goes at the top
   of your script:

   ```r norun
   library(dplyr)
   ```

Think of a reference book. Installing buys the book and puts it on your shelf. Loading takes
it down and opens it on the desk. You buy it once. Each new working session starts with a clear
desk, so you open it again.

Some packages share a function name with another package. When that happens, the package you
loaded last wins, and `library()` prints a message saying so. Loading dplyr, for example,
hides another `filter()`, which belongs to stats, a package that comes with R. To be sure
which one you get, write the package name and two colons in front: `dplyr::filter()` or
`stats::filter()`.

The tidyverse is a family of packages built to work together. You can load nine of them with
`library(tidyverse)`. This book loads the ones it needs one at a time, such as `library(readr)`
and `library(dplyr)`. That way the top of every script shows exactly what it uses.

Packages change. Each has a version number, and so does R. The outputs in this book were made
with R {{n:r_version}} and dplyr {{n:dplyr_version}}, and newer versions of both exist. Check
yours with:

```r
R.version.string
packageVersion("dplyr")
```

```output
[1] "R version 4.3.3 (2024-02-29)"
[1] ‘1.1.4’
```

**Must know points for you.**

- The error is to put `install.packages()` in your script. It downloads the package every time the script runs, and it changes the version on whoever runs it. Install once, in the console. Put only `library()` calls in the script, at the top.
- "could not find function" almost always means the package that holds the function is not loaded in this session. Check the `library()` lines at the top of the script before you suspect anything else.
- Read the message that `library()` prints. After `library(dplyr)`, `filter()` means dplyr's. When a call does something you did not expect, ask whether a later package masked the function you meant, and write `package::function()` to be sure.
- Record the version of R and of every package your analysis loads, in the script's output. A methods section that says only "analysed in R" cannot be rerun with confidence.
- When a trainee's output differs from the book's in a message or a detail, have them compare versions with `packageVersion()` before they rewrite their code.
- A version number names a release. It does not pin it: the next person to run `install.packages()` gets whatever version is current that day. Keeping a project on fixed versions needs a separate tool, renv, taught two rungs above this one.

**Exercise 1** (design). You are starting `code/analysis.R`, a script that will read a raw file with readr and
reshape it with dplyr. Write its first lines: the packages it needs and a record of the
versions it ran on. Say why `install.packages()` does not appear in it.

**Exercise 2** (retrieval). Without looking back, say how often you run `install.packages()` and how often you run
`library()`, and where each one goes.

**1.** Write the line you would type in the console to install the package readr. Then write the
line that goes at the top of a script that uses it.

**2.** In a fresh session you load dplyr and then type `filter(...)`. Which package's `filter()`
runs? Write the call you would use to run the other one, and the line that shows you what
dplyr hides when it loads.

**3.** Write the lines that print the version of R you are running and the version of the package
here.

**4.** Without loading any package, count the rows of `penguins_raw.csv` in your project's
`data-raw` folder, and say what one row stands for.

**5.** A colleague's script begins as below and stops at its second line with the error shown.
The script worked for them yesterday. Find what broke.

```r error
raw <- here::here("data-raw", "penguins_raw.csv")
penguins_raw <- read_csv(raw, show_col_types = FALSE)
```

```output
Error in read_csv(raw, show_col_types = FALSE) :
  could not find function "read_csv"
```

**6.** A colleague wants to report the version of dplyr. Their line and its error are below. Find
what broke, and say why the mistake is easy to make.

```r error
packageVersion(dplyr)
```

```output
Error: object 'dplyr' not found
```

**7.** A made-up thesis methods section says: "All analyses were carried out in R." Write the lines
that would record what this sentence leaves out, for an analysis that uses readr and dplyr.
Run them, and say what even your fuller record does not establish.

