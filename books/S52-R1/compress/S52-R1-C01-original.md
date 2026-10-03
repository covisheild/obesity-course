# S52-R1-C01 · When data change silently: three documented failures

**Definition.** A silent change is a change to data, or a choice about which data to use, that leaves no
instruction a second person can read and run again, and that nothing on the screen announces.
This section rests on three documented cases.

Gene symbols turned into dates. Ziemann, Eren and El-Osta report that Microsoft Excel, used
with its default settings, converts some gene symbols to dates: SEPT2 becomes "2-Sep" and
MARCH1 becomes "1-Mar".

They screened 35,175 supplementary Excel files from 18 journals published from 2005 to 2015.
They confirmed gene name errors in 987 files from 704 articles, which is {{n:ziemann_affected_pct}} of the 3597 articles whose Excel files held gene lists. They
state that in 2016 no spreadsheet program they named could switch the conversion off for good.
In 2020 the HUGO Gene Nomenclature Committee (HGNC) reported that it had renamed every gene
symbol that Excel turned into a date: SEPT1 is now SEPTIN1, and MARCH1 is now MARCHF1.

A spreadsheet formula and undeclared choices. Herndon, Ash and Pollin replicated, that is
rebuilt, Reinhart and Rogoff's 2010 papers on public debt and economic growth from the authors' working spreadsheet.
They found selective exclusion of available data, coding errors and inappropriate weighting of
summary statistics. One formula averaged rows 30 to 44 instead of rows 30 to 49, which left out
five countries entirely.

The papers' highest category was public debt above 90% of gross domestic product (GDP), a
measure of the size of an economy. The correct count of years in that category was 110. The
chosen exclusions brought it to 96, and the spreadsheet error to 71. Average growth in that
category, recalculated with all the data, was 2.2% a year rather than the published −0.1%. The
authors state that the problems interact. Corrected alone, the spreadsheet error moves the
figure to 1.9%.

Rows lost in transfer. Public Health England (PHE) stated on 4 October 2020 that 15,841
positive test results for coronavirus disease 2019 (COVID-19), from 25 September to 2 October,
had been left out of the reported daily figures. It gave the cause as files that "exceeded the
maximum file size" of the process that loads them into central systems. It does not name the
software.

The three cases differ in cause. What they share is that the change was silent: nothing
announced it, and it came to light only later.

**In plain terms.** Here is the trap with data. A number can change, or a row can go missing, and nothing on the
screen tells you. You see a tidy table and a clean total. The table looks right, so you trust it.

This book starts with three times that happened, each one written up by the people who found
it.

- **A program changed values as the file was opened.** Excel, used with its default settings,
  turned gene names such as SEPT2 into dates such as "2-Sep". About one in five genomics papers
  that came with Excel gene lists carried such errors.
- **A formula covered the wrong rows, and choices went unsaid.** A famous paper on debt and
  growth averaged rows 30 to 44 instead of 30 to 49. Five countries dropped out. Other data had
  been left out on purpose, and the paper never said so.
- **A transfer lost rows.** In England in 2020, 15,841 positive COVID-19 test results did not
  reach the daily figures for up to about a week. Some files were too big for the system that loaded
  them.

The causes differ. The pattern is the same. The change was silent, and it came to light only
later.

So this book follows one rule. You never edit the raw data file. Every change you make to the
data is a line of code, kept in a file, that anyone can read and run again. And you count your
rows before and after each step.

The rule is a response to cases like these, not a law of nature. Code can be wrong too. Its
advantage is that the wrong line is there to be found.

**Figure.** Positive COVID-19 test results left out of England's daily figures, by the day each should have been reported, as Public Health England's statement of 4 October 2020 gives them: 957, 744, 757, 0, 1415, 3049, 4133 and 4786, a total of 15,841. The last three days hold 11,968 of them.

*What the figure shows:* A bar chart of the days from 25 September to 2 October 2020. Results not included: 957, 744, 757, 0, 1415, 3049, 4133 and 4786. The bars rise over the last four days.

**Must know points for you.**

- The error is to believe a table because it looks complete. A converted gene name, a formula that stops at row 44 and a batch of lost rows all produce tidy-looking output. Before you trust a table, compare its row count, or a total, with the count you expected.
- Never edit the raw data file, and never save over it. Make every change in code that reads the raw file and writes a new one. If a value is wrong, the correction is a line someone can read, and the original is still there to compare.
- A choice about which data to leave out is part of the analysis. Write it as a line of code with a comment saying why. Reinhart and Rogoff's exclusions mattered as much as their formula error, and the papers never stated them.
- Do not repeat "a spreadsheet slip caused austerity" or "Excel lost the COVID cases". The replication found the slip alone moved the result from 2.2% to 1.9% a year. The PHE statement names no software. Quote what each source says, and no more.
- About one in five genomics papers with Excel gene lists carried gene names turned into dates. The count was 704 of 3597, in 18 journals from 2005 to 2015. When you open someone else's data file, look for values that have changed type, such as text turned into dates.
- When a trainee says their numbers are right because they checked them on screen, ask how a second person would check them. If the answer is "by redoing it by hand", the work has no record.
- Writing every step in code does not make the steps right. A script can average the wrong rows too. What it changes is that the step is written down, so a reviewer can find the error and you can fix it once and rerun.

**Exercise 1** (retrieval). From memory, name the three documented failures in this section. For each, say in one sentence
what changed or went missing, and how it came to light.

**Exercise 2** (critique). In a made-up department meeting, a senior colleague says: "Our thesis data are in one Excel
file. Residents correct mistakes directly in the cells, so the file is always the cleanest
version. That is good practice."

Using the three cases in this section, say what is lost when corrections are made directly in
the file, and what you would propose instead.

**Exercise 3** (interpretation). A classmate's draft introduction says: "Excel deleted 15,841 COVID-19 cases in England in 2020
because of its row limit." Check this sentence against what PHE's statement says, and rewrite
it so that every part of it is supported.

**Exercise 4** (teaching). A first-year resident has ten minutes and a whiteboard. They say: "My data are small, a few
hundred rows. I can see every cell. Why should I bother with code?" Teach them, using one of the
three cases.

