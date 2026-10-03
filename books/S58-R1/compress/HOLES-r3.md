# S58-R1 step 5c: holes, batch r3 (C13 to C18)

These are gaps the restore could not close. In most, the full-length original does not fill the
gap either, or the gap is an error or a contradiction. In four, the original's sentence exists but
could not come back without raising the mean sentence length above the original's (marked
**dropped for the mean**). All are for the fixer, and they go back through the audit.
"Field" is the record field. "Exercise" and "Problem" mean fields the compression pass does not
touch. Gap ids are from `COLD-READ-GAPS.md`.

## C13

**H-13-1** (B-13-1). `illustration.body`, the third rule of the pass.
- As it stands: "Every part is there and nothing is added. The draft passes."
- What is wrong: the second reader's sentence ("Overweight among women of 15 to 49 ...") drops
  "India", but the table fails the first reader for dropping the age range from "about whom".
- What would close it: make "India" survive in the second reader's sentence, or say which parts
  of "about whom" must survive.

**H-13-2** (B-13-2). `illustration.body`, the comparison table.
- As it stands: "| about whom | ... | Indian women | age range lost |" and "| what was found | commoner in
  NFHS-5 than in NFHS-4 | increasing | kept |".
- What is wrong: the reader's "Obesity" for "overweight or obesity" goes unflagged, though C08 forbids
  the swap. "Increasing" is marked kept for a two-survey comparison. There is no rule for "kept".
- What would close it: flag the outcome change in the table, and state in the definition what
  counts as a part kept.

**H-13-3** (B-13-3). `definition.text`, step 4.
- As it stands: "... compared with what, and how far it reaches."
- What is missing: "how far it reaches" is never defined. Only the table shows it means the
  claim's limits.
- What would close it: one sentence defining it, with C03's term if C03 has one.

**H-13-4** (B-13-4). Exercise 2, step 4 (also C11 `must_know`).
- As it stands: "Score each paragraph for readability with one program ..."
- What is missing: no program is named here or in C11, which teaches only hand formulas.
- What would close it: name a freely available tool and the score it reports, or tell the reader
  to use C11's hand formula.

## C14

**H-14-2** (B-14-2). Figure caption. The same issue recurs in C15 and C22.
- As it stands: "Source: NFHS-5 India Fact Sheet, indicators 88 and 89."
- What is missing: the reader is never told that the fact sheet numbers its indicators.
- What would close it: one sentence at the first use, saying how fact-sheet indicators are numbered.

**H-14-3** (B-14-3). Exercise 4.
- As it stands: "... wants to keep all eight NFHS bars in one figure ..."
- What is wrong: the figure has four bars. "Eight" (women and men × urban and rural × two rounds?)
  is never introduced.
- What would close it: say what the eight values are, or change the number to match a figure the reader has seen.

**H-14-4** (B-14-4). `must_know[4].point`. **Dropped for the mean.**
- As it stands: "Do not lift a figure from your paper onto a slide." The reason was restored to the definition.
- What is missing: what to change on the slide. The original has it in a 25-word sentence ("Make
  the slide version again, with fewer elements, thicker lines and bigger text, because it will be
  seen from a distance for a few seconds."), and that sentence raises C14's mean above the original's.
- What would close it: the fixer splits that sentence into two, or accepts it in place of a longer cut.

## C15

**H-15-3** (B-15-3). `definition.text`, and Exercise 1.
- As it stands: "Length, direction and angle share third place, then area." Exercise 1 asks for "the first four places".
- What is wrong: with the tie, it is unclear whether area is fourth or sixth, so Exercise 1 has no
  single answer. No chart in the section shows judging direction.
- What would close it: say whether places are counted by rank or by item, and reword Exercise 1 to
  match. Add one example of a direction judgment, such as a slope.

**H-15-4** (B-15-4). `definition.text`.
- As it stands: "First comes position along a common scale, then positions along scales not lined up."
- What is missing: no example of scales not lined up, such as small multiples with separate axes.
- What would close it: one example sentence.

**H-15-7** (B-15-7). Exercise 3.
- As it stands: "name the shape of the numbers from the table in this section".
- What is wrong: the section has no table. The five shapes are a list in the definition and must-know.
- What would close it: point the exercise at the list, or add the shape-to-mark table.

**H-15-8** (B-15-8). `must_know[6].point`, against C17 `must_know[5]`.
- As it stands: "When the value axis cannot start at zero, as on a logarithmic axis, draw dots, not bars."
  C17 says: "Draw a ratio on a logarithmic axis, with bars from 1."
- What is wrong: the two sections contradict each other.
- What would close it: state the case once. Bars from 1 for ratios, dots otherwise on a log axis,
  or whichever the sources support. Then make both sections agree.

**H-15-9** (B-15-9). Exercise 2.
- As it stands: "stunted 35.5%, wasted 19.3%, underweight 32.1% and overweight 3.4% ... indicators 81, 82, 84 and 85".
- What is missing: stunted, wasted and underweight are never defined. The restored must-know now says
  that the categories overlap.
- What would close it: a one-line gloss of each term in the exercise, or a pointer to where the book defines them.

## C16

**H-16-1** (B-16-1). `definition.text`. **Dropped for the mean.**
- As it stands: "Many different sets of values give the same bar and the same error bar."
- What is missing: what an error bar is. The original's sentence ("It usually adds an error bar for
  the standard deviation, or for the standard error of the mean (`B0-R0-C29`).") says only what it
  stands for. It could not come back with B-16-5's restore without raising the mean. Error bars are
  defined only in C20.
- What would close it: a short definition here ("a line above and below the bar's top, as long as
  ..."), or a pointer forward to C20.

**H-16-2** (B-16-2). Figure captions.
- As it stands: "each ward's standard deviation is 14.3 minutes" and "Ward 1 climbs evenly from 10 to 50 minutes."
- What is missing: the 24 values are only in the figure spec (`check/records/S58/S58-R1-C16.yml`), and
  14.3 is correct for them (sample SD 14.29, 14.28 and 14.25). Ward 1 is not evenly spaced
  (10, 15, 21, 27, 33, 39, 45, 50). Evenly spaced 10 to 50 gives SD 14.0, so the reader cannot
  reconstruct the figure.
- What would close it: list the values in the caption or a table, and say "nearly evenly".

**H-16-3** (B-16-3). The second figure.
- As it stands: "joined in that order" / "against adult number 1 to 8".
- What is wrong: the definition has just defined a strip chart, with one column of dots per group
  and jitter. The only drawn example is a rank plot that joins unrelated people with lines, which
  the must-know reserves for paired measurements.
- What would close it: redraw it as a strip chart (three columns of jittered dots with a mean line).

**H-16-4** (B-16-4). `must_know[2].point`. **Dropped for the mean.**
- As it stands: "A box plot is a summary too."
- What is missing: what a box plot is. The original's definition sentence ("With more values, a box
  plot shows the median, a box around the middle half of the values, and whiskers beyond it, with
  far values drawn as single dots.", 29 words) raises C16's mean above the original's.
- What would close it: split that sentence, or accept it in place of a longer cut.

**H-16-6** (B-16-6). Exercise 1, and `must_know[4].point`.
- As it stands: "Which chart do Weissgerber and colleagues recommend for small groups, and why not a box plot?"
  The must-know reads "A systematic review covered 703 papers ...".
- What is missing: the text never attributes the review, or a recommendation, to Weissgerber and colleagues.
- What would close it: name the review's authors and year where it is described, and state their recommendation.

## C17

**H-17-2** (B-17-2, B-17-4). `definition.text` and `must_know[1].point`.
- As it stands: "work out a ÷ (a − s) with the smaller bar". In the original, the definition also says
  "the LF comes to a ÷ (a − s), as the second illustration shows".
- What is missing: the derivation. No illustration shows it, and it needs dividing fractions, which
  Book 0 does not teach. The drawn and data ratios are defined, but their use is never stated
  (LF = (drawn ratio − 1) ÷ (data ratio − 1)).
- What would close it: a worked derivation from the percentage-change definition through the two
  ratios to a ÷ (a − s), and the cross-reference fixed.

**H-17-3** (B-17-3). `definition.text` and `must_know[1].point`. **An error.**
- As it stands: "a the smaller", with "the change divided by the value it started from".
- What is wrong: the shortcut assumes the smaller bar is the start. For a fall (24.0 to 20.6, axis
  at 20) the LF is 6.0, not 34.3. For urban against rural, nothing says which bar is the start.
- What would close it: state the shortcut for the starting value, or restrict it to rises, and say
  how to choose the start for a comparison of two groups.

**H-17-5** (B-17-5). `definition.text`.
- As it stands: "On a logarithmic axis a bar stands for a ratio, and it starts at 1."
- What is missing: why 1, which is no difference. A ratio below 1 drawn downward is never shown. The
  restored must-know now gives the equal-and-opposite lesson.
- What would close it: one sentence on why 1, and Problem 5's answer or a figure showing a bar below 1.

**H-17-6** (B-17-6). Problems 5 and 10.
- As it stands: "in units of log10".
- What is missing: log10 is never taught or glossed.
- What would close it: a gloss at first use, or a pointer to where Book 0 teaches it.

**H-17-7** (B-17-7). `must_know[3].point`.
- As it stands: "Shading counts as ink."
- What is missing: "ink" is not defined until C18. The principle of proportional ink only implies it.
- What would close it: one sentence in the definition saying what ink means here.

**H-17-11** (B-17-11). Problem 7.
- As it stands: "the 2014 bar uses about 2.7 times as much ink".
- What is missing: the answer assumes equal bar widths and does not say so.
- What would close it: add "with bars of equal width".

## C18

**H-18-2** (B-18-2). `definition.text` and `must_know[4]`, `must_know[5]`. **Dropped for the mean.**
- As it stands: "'Useful junk?' found that cartoon charts ..." and "Holmes charts" (caption).
- What is missing: who Holmes is, and that "Useful junk?" is Bateman and colleagues (2010). The
  original's sentence ("Bateman and colleagues (2010) showed 20 people charts by the graphic artist
  Nigel Holmes, ...", 25 words) raises C18's mean above the original's. Even that sentence never
  ties the title to the authors.
- What would close it: give the full title and authors once, and split the Bateman sentence.

**H-18-3** (B-18-3). `definition.text` and `must_know[2]`.
- As it stands: "Context is non-data ink, and it stays (Wilke)." and "in Wilke's example".
- What is missing: Wilke is never identified (author and book), and C21's "Wilke's rule" depends on it.
- What would close it: the full citation at first use, which is C14 if its restored Wilke line stays.

**H-18-4** (B-18-4). `definition.text` and `must_know[2].point`.
- As it stands: "A 3-D effect on flat data" and "Never draw flat data in 3-D."
- What is missing: "flat data" is undefined. It means values that vary on one dimension only.
- What would close it: a gloss at first use.

**H-18-5** (B-18-5). Exercise 2.
- As it stands: "List what you would change, in the order you would change it".
- What is missing: no order is taught here beyond "Do this before you change anything else". The order arrives in C22.
- What would close it: teach the order here, or drop "in the order" from the exercise.

**H-18-6** (B-18-6). Book-wide; C14 `definition.text` against C18 `definition.text`.
- As it stands: C14 says "journals call it the figure legend" (the caption). C18 says "a legend, the
  key that says which colour is which".
- What is wrong: one word has two meanings, and C20 and C22 use both.
- What would close it: pick one term for the caption and one for the key, and use them throughout.
