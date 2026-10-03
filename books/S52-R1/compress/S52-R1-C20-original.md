# S52-R1-C20 · Does shared code rerun? What studies found

**Definition.** A result is reproducible when the same data, analysed again with the same code, give the same
result. A result is replicated when independent investigators collect new data on the same
question and reach the same answer. Peng (2011) calls replication the ultimate standard for a
scientific claim, and reproducibility a minimum standard for when replication is not possible.
Between no replication and full replication he describes a spectrum: a study is more or less
reproducible depending on what data and code are made available. Reproducing a result does not
show that it is correct.

Running the shared code again without an error, called re-execution, is needed for
reproduction and is not enough for it: code can run and still produce a different result.

Trisovic, Lau, Pasquier and Crosas (2022) measured re-execution at scale. They took 2109
replication packages, the data and code that authors deposit with a published paper, from the
Harvard Dataverse, a website where researchers deposit such files. The packages were published
from 2010 to July 2020 and held 9078 R files.

Each file was run in a clean environment under
three versions of R (3.2, 3.6 and 4.0), with up to one hour per file and five hours per package.
Each was run once as deposited and once after an automatic code cleaning. The cleaning removed
absolute file paths, standardised file encoding and installed the packages the code used. A
file counted as a success if any of the three versions ran it without error. Files that ran out
of time were excluded from the success rate.

Their abstract reports that {{n:trisovic_fail_initial_pct}} of the R files failed to complete without error on first
execution, and {{n:trisovic_fail_cleaned_pct}} after code cleaning. Their results table gives success rates of 25% without
cleaning, 40% with cleaning and 56% for the better of the two runs. The abstract's figures and
the table's are on different bases, and the paper's two 56% figures are different quantities.
Code cleaning fixed every error caused by `setwd()`, and many caused by missing packages.
Errors that remained included packages missing or of an incompatible version, wrong paths and
output folders, and objects that did not exist. Journals with the strictest data-sharing
policies had the highest re-execution rates. Most packages came from the social sciences, and
all from one website.

**In plain terms.** Two words that sound alike mean different things.

**Reproduce** means: take the same data, run the same code, get the same numbers. Someone else can
do it with your project folder in an afternoon.

**Replicate** means: collect new data on the same question and see whether the answer holds. That is
a new study, and it may take years.

Reproducing is the smaller test. It cannot tell you whether the analysis was right, only whether
it was done as described. But a study's data and code make it possible. And it catches the slips
the first section of this book was about.

The first step of reproducing is that the code runs at all. One large study tested that. It took
thousands of R files that researchers had shared with their published papers, and ran each on a
clean computer. Most did not run.

Many of the reasons are ones you have already met in this
book. A script set the working directory to a folder on its author's computer. A package was not
installed, or was the wrong version. A file was in the wrong place.

A script that runs is still not a result reproduced. It may run and print different numbers. So
"the code runs" is the floor, not the finish.

**Figure.** Trisovic and colleagues' results table for R files shared on Harvard Dataverse, 2010 to July 2020: files that ran without error, stopped with an error, or exceeded the time limit. Without code cleaning: 952, 2878 and 3829 of 7659 files. With cleaning: 1472, 2223 and 3719 of 7414. Best of both runs: 1581, 1238 and 5790 of 8609. The table's success rates, 25%, 40% and 56%, leave out the files that ran out of time.

*What the figure shows:* A bar chart with three groups: without code cleaning, with code cleaning, and best of both. Each has three bars: success 952, 1472 and 1581; error 2878, 2223 and 1238; time limit exceeded 3829, 3719 and 5790.

**Must know points for you.**

- One study ran 9078 R files shared with published papers on the Harvard Dataverse, deposited from 2010 to July 2020. Its authors report that {{n:trisovic_fail_initial_pct}} failed to run without an error on first execution. Quote it with that source, sample and date, never as "most research code is broken".
- The error is to think that sharing your code makes your work reproducible. Code that sets the working directory to your own folder stops on its first line on another computer. So does code that loads a package nobody else has.
- Before you quote a percentage from a study, find what it is a share of. The study's 25% success rate leaves out the files that ran out of time; its abstract's {{n:trisovic_fail_initial_pct}} "failed" is on another basis. Quote each with its own words.
- Run your script on a clean computer, or in a fresh R session, before you share it. The study's errors included a folder on the author's computer, a missing package and a missing file. Each shows up the first time someone else runs your code, and is cheapest to find yourself.
- Code that runs is not a result reproduced. Ask for the comparison of the output with the paper's numbers before you accept that a study was reproduced.
- A reproducible analysis can still be wrong. Reproducing it shows it was done as described, not that it was the right analysis. Do not offer reproducibility as evidence that a finding is true.
- Journals with the strictest data-sharing policies had the highest re-execution rates in this study. That is a correlation across a few journals, not a measured effect of the policy. In a committee, offer it as a reason to consider such a policy, not as proof that it works.
- The finding is that most shared R code does not rerun as deposited. Studies of other websites, fields and years that find most files running would overturn it. This study used one website, mostly social science, and code deposited from 2010 to 2020.

**Exercise 1** (critique). A classmate's thesis says, in its methods: "All code is available on request, so the analysis is
fully reproducible." Say what is wrong with the sentence, using this section's evidence, and write
a sentence that would be true.

**Exercise 2** (interpretation). A blog post says: "A Harvard study found only 25% of research code works." Using the results table
in this section, say what the 25% is a share of, what it leaves out, and what the sentence gets
wrong.

**Exercise 3** (retrieval). Without looking back, say what "reproduce" and "replicate" each mean. Then name three reasons the
study in this section found for shared R code failing to run.

**Exercise 4** (teaching). A journalist has three minutes and asks you: "Is it true that most scientists' code doesn't even
run?" Answer without jargon, say how sure you are, and give them one sentence they could quote.

