# S52-R1-C10 · The data dictionary and the README

**Definition.** A data dictionary is a separate file, laid out as a table, that explains every variable in one
data file. It has one row per variable. Its columns give the variable's exact name as it appears
in the data file, a plain label and what the variable means. They also give its unit, its type,
the values it is allowed to take or its expected range, how a missing value is written, and
where each entry came from. It is written once, before any cleaning, from the documentation of whoever made the data,
and each entry is then checked against the file.

A README is a short plain-text file at the top of the project folder. It gives the project's
title and what it is for. It says where the raw data came from, which version, and on what
terms, and where the data dictionary is. It gives the one command that reruns the analysis, and
the folder to run it from. It says what each output file is, and whom to contact.

A project shared in a public repository adds two more files beside the README. A LICENSE says on
what terms others may reuse the code and data. A CITATION says how to cite the project.

**In plain terms.** Book 0 taught four questions to ask of any table before reading a number. What does one row stand
for? What does each column report? In what unit? Where did the numbers come from? A data
dictionary is those answers, written down once, for every column of your raw file, so nobody has to
guess them again.

It is itself a small table, one row per column of the data. For each column it says:

- the exact name, letter for letter, as it is in the file;
- what the column means, in plain words;
- its unit;
- its type: number, text or date;
- the values it may take, or the range you expect;
- how a missing value is written;
- where you got each of these facts.

Write it before you clean anything, from the documents that came with the data. Then check it
against the file in code. The documents describe what the data's makers meant. The file is what
they delivered, and the two do not always agree.

A README is the note on the front of the project folder. It is a plain-text file that anyone can
open. It says what the project is, and where the raw data came from and on what terms. It gives
the one command that reruns everything, and says what each output is. Someone who has never met you should be able to
read it and rerun your analysis. That someone is often you, a year later.

A project put online for others has two more files beside the README. A LICENSE says what others
may do with it. A CITATION says how to cite it. Both belong to the next level of this subject.

**Must know points for you.**

- The error is to think the documentation describes the file. It describes what the data's makers meant to deliver. Check every entry of your dictionary against the file in code: the names, the values, and whether an ID is really one per row.
- Write the variable name in the dictionary exactly as the file has it, letter for letter, with its spaces and brackets. A name copied from the documentation can differ, and code written from it will fail.
- Write the dictionary before you clean. Every cleaning step needs it: which code means missing, which unit a column is in, which values are allowed. A dictionary written after cleaning describes your cleaned data and hides what the raw file held.
- Record how missing values are written in the raw file, for each column if they differ: blank, `NA`, -99, "not recorded". That one cell decides what you tell `read_csv()` and whether a -99 ends up inside a mean.
- Never fill an "expected range" cell with the smallest and largest values in your own file. A range taken from the data can never flag an error in the data. Leave it blank and say why, until a source or a protocol gives the range.
- Write the README's rerun line as the exact command. If you cannot, because some step is done by hand, you have found the step that makes your analysis unrepeatable. Move it into code.
- When a trainee hands you a thesis dataset, ask for its dictionary before you look at a single number. If there is none, ask them to write one row: one variable, its unit, its missing code, and where they got each. Most of what will go wrong shows up in that row.
- A dictionary and a README describe the data and how to rerun the analysis. They do not make either one right. A dictionary can faithfully describe a column full of errors.

**Exercise 1** (design). A made-up thesis dataset, `school_heights.csv`, has these columns: `child_id`, `school`, `sex`
(coded 1 and 2), `dob`, `visit_date`, `height_cm` (to 0.1 cm), `weight_kg` (to 0.1 kg). The
data-entry operator typed -99 wherever a measurement was not taken. The study protocol says
`sex` is 1 for boys and 2 for girls, and gives no expected ranges. Write the data dictionary.

**Exercise 2** (critique). A colleague's project folder has this README, in full: "Analysis code for my thesis. Run the
scripts in order. Data from the department." Name what is missing, and say what each gap would
cost the next person.

**Exercise 3** (retrieval). Without looking back, list what a data dictionary records for each variable, and what a README
says.

**Exercise 4** (teaching). A health secretary asks, on one page: "Why should a district survey's data come with a data
dictionary? We have the data."

