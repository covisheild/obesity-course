# S52-R1-C22 · One dataset, end to end

**Definition.** An end-to-end analysis takes one question from raw data to its final table and figure in a
single script that another person can run.

Real work does it in this order. Write the question. Obtain the raw files, read their terms of
use, and record their checksums. Write the data dictionary from the source's documentation. Set
up the project folder.

Then write the script,
which reads, checks, joins, cleans, derives, summarises, plots, writes its outputs to `output/`
and prints the versions that made them. Write the README, whose rerun line is the one command.
Last, a fresh session, or a second person, runs that command and gets the same outputs.

The analysis is reproducible in this book's sense when the outputs come back the same from the
raw files with that one command. That says the result can be checked. It does not say the
result is right, or that it describes any population beyond the rows in the file.

**In plain terms.** This section puts the whole book into one piece of work, in the order you would really do it.

1. **The question.** One sentence, saying who, what is measured, and how it is summarised.
2. **The data.** Download the raw files. Read the terms that come with them. Record each file's
   checksum.
3. **The dictionary.** One row per variable you will use: its name in the file, its meaning, its
   unit, its codes, and where you found them.
4. **The project folder.** `data-raw/` for the files as they arrived, `code/` for the script,
   `output/` for what the script makes.
5. **The script.** Read, check, join, clean, work out new columns, summarise, plot, write the
   outputs, print the versions. Every step is a line of code.
6. **The README.** What the project is, where the data came from, and the one command that
   reruns it.
7. **The rerun.** Delete the outputs and run the command from nothing. The same table and the
   same figure must come back.
8. **What it does not show.** Say it, next to the result.

The data here are real: the body measures and the demographics of the people examined in an
American national survey, NHANES, in 2021 to 2023. The method is the same for a thesis dataset
from Raipur.

**Figure.** The first quartile, median and third quartile of measured BMI in 2680 men and 3249 women aged 20 and over, not pregnant, examined in NHANES 2021–2023. The medians are close, 28.1 and 28.7 kg/m^2; the women's third quartile, 34.7 kg/m^2, is higher than the men's, 32.4 kg/m^2. Unweighted: these values describe the participants, not the United States.

*What the figure shows:* A chart of points for two groups at 25, 50 and 75 per cent. Male: 24.9, 28.1, 32.4 kg/m^2. Female: 24.4, 28.7, 34.7 kg/m^2. The female points start lower and end higher.

**Must know points for you.**

- Write the question before you open the data, and write who it is about. "Adults aged 20 and over examined in this survey cycle, not pregnant" decides every filter in the script. Without it, each filter becomes a choice made after seeing the numbers.
- The error is to trust a filter because it ran without a warning. `filter(RIDEXPRG != 1)` ran silently and dropped 4971 adults instead of 41, because a missing value is neither equal nor unequal to 1. Before each filter, write down how many rows you expect it to keep, and check.
- Record each raw file's checksum in the README on the day it arrives, and the terms it came with. Someone who questions your result months later can confirm in one line that they hold the same file. They can also see whether they may use it.
- Put a printed row count after every step that can add or drop rows, and a `stopifnot()` where you know the right count. The log of counts is the first thing an examiner, or you next year, reads to see what the script did.
- Any summary of an NHANES file without its sample weights describes the participants in the file. Write "unweighted" beside it, and never present it as the figure for the United States, still less for India.
- The gate is one command from raw data to the same outputs. When you hand a project on, or ask for one, the first test is that command in a fresh session. Ask for it before you read a single result.
- Reproducible means the result can be checked, not that it is right. A wrong cut-point or a wrong filter reruns perfectly. Rerunning shows that the script is complete; only reading it shows whether it asks the right question.

**Exercise 1** (retrieval). Without looking back, list the steps of an end-to-end analysis in the order real work runs
them. Then say what the gate to the next rung is.

**Exercise 2** (build). Build the rung's target with a dataset of your own. It may be a thesis dataset, or a department
register you have permission to use. It may be the NHANES files of this section, with a question
of your own.

Write the question in one sentence. Put the raw files in `data-raw/` and record their
checksums and terms. Write the data dictionary.

Write `code/analysis.R` so that it reads,
checks, cleans, summarises and plots, writes one table and one figure to `output/`, and ends
with `sessionInfo()`. Write the README. Then delete `output/`, run `Rscript code/analysis.R`
in a fresh session, and give the project folder to a colleague to run the same command.

**Exercise 3** (critique). A colleague sends you the project for her thesis chapter. The README says: "Run the scripts in
code/ in order." `code/` holds `clean.R` and `analysis.R`. The first line of `clean.R` is
`data <- read_excel("C:/Users/anita/Desktop/final data (2).xlsx")`. Its last line is
`write_xlsx(data, "C:/Users/anita/Desktop/final data (2).xlsx")`. Her chapter reports "mean
BMI 24.6 kg/m^2 (n = 412)". Find each thing that stops this project from passing the gate, and
say what each one would cost her.

**Exercise 4** (teaching). A health secretary asks why the department's analysts should hand over every analysis as a
project folder that reruns with one command. Answer on one page. Put the answer first, then the
reasons, with no methods section.

