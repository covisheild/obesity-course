# S58-R1 step 5c: restore decisions, batch r2 (C07 to C12)

Restorer: not the cutter and not the cold reader. Inputs: `COLD-READ-GAPS.md` (reader A, gaps
A-07-* to A-12-*), and `<S>-original.md`, `<S>-prose.yml` and `<S>-pass1-prose.yml` for C07 to
C12. The restore lists are in `restore-lists/S58-R1-Cnn.txt`, each line commented with the gap it
closes. The outputs are `S58-R1-Cnn-final-prose.yml`, built by `check/compress/restore.py` and
checked by `check/compress/validate.py`. The tools were not changed. No record was edited.

Key: **restored** means original sentences were put back because they let the reader do the
thing. **hole** means the original does not fill it either, or it is an error or contradiction:
it is listed in `HOLES-r2.md` (H-number given). **not a defect (artifact)** means the gap exists
only because the cold-read files printed `{{n:key}}` placeholders or record ids raw (see
`COLD-READ-GAPS.md`, "Two artifacts"). Where a restore closes part of a gap and the rest is a
hole, both are given.

Figures, exercises and practice problems are identical in the original and the cut for all six
sections (checked), so every gap that points at a figure caption or a problem is a hole, never a
restore.

## Word counts (reader-facing prose, as `validate.py` measures it)

| Section | Original | Cut (pass 1) | Final | Restored | Mean sentence orig → cut → final | Validate |
|---|---|---|---|---|---|---|
| C07 | 768 | 373 | 448 | +75 | 13.16 → 11.87 → 13.03 | OK |
| C08 | 827 | 435 | 464 | +29 | 13.13 → 12.79 → 12.89 | OK |
| C09 | 744 | 426 | 442 | +16 | 12.42 → 11.33 → 11.48 | OK |
| C10 | 520 | 266 | 292 | +26 | 12.68 → 12.09 → 12.17 | OK |
| C11 | 868 | 443 | 498 | +55 | 14.71 → 13.42 → 13.83 | OK |
| C12 | 493 | 250 | 250 | +0 | 12.64 → 12.50 → 12.50 | OK |
| **Total** | 4220 | 2193 | 2394 | +201 | | 6 OK |

Decisions over the 44 gaps: **11 restored**, **27 hole**, **6 not a defect (artifact)**. Nine
of the restored gaps leave a residual hole, also in `HOLES-r2.md`.

`python check/build.py --check` / `--subject S58-R1` was not run: it needs the final text written
back into the records, which is outside this step's brief.

## Gap by gap

### C07
- **A-07-1** restored: "They come from Gopen and Swan's reader-expectation approach (1990) and the
  US Federal Plain Language Guidelines (2011) ...". This names the source the figure and the
  must-know cite. Residual hole H1: the original never shows Gopen and Swan's sentences either.
- **A-07-2** hole, H2: the made-up survey sentence, before and after mending, is not in the
  original either.
- **A-07-3** restored: "The start of a sentence, the topic position, holds the information that
  links back to what the reader already has ...". Ex 1 asks for exactly this place.
- **A-07-4** hole, H3: the original gives no rule for where the count starts or whether an
  auxiliary ("was") belongs to the verb.
- **A-07-5** restored in part: "If a rewrite makes a sentence worse for its paragraph, as 'Bees
  disperse pollen' would ...". This is the original's one example of a principle failing when
  followed blindly. Residual hole H4: no example of a three-noun chain anywhere in the original.

### C08
- **A-08-1** not a defect (artifact 1). The placeholders are the only gap.
- **A-08-2** hole, H5: the original never introduces the NFHS fact sheet in this section either.
- **A-08-3** hole, H6: the original never spells out ASHA, in the section that requires it.
- **A-08-4** hole, H7: "significant", "random", "normal", "correlation" and "test" are defined
  nowhere in the original (also ground-floor A-00-5).
- **A-08-5** hole, H8: the original has the same five-versus-four mismatch ("sample").
- **A-08-6** restored: "An abbreviation is a shortened form of a word or phrase." This gives
  "short form" and "acronym" a parent term. Residual hole H9: the original never says that an
  acronym, as Barnett and Doubleday define it, is a kind of abbreviation.
- **A-08-7** restored: "The US Federal Plain Language Guidelines advise no more than three
  abbreviations in a document, and preferably two." This answers "three per what" and "on whose
  authority".
- **A-08-8** hole, H10: the original does not explain the 1950 and 1956 start years, and states
  "English-language" only in the must-know.

### C09
- **A-09-1, A-09-2** not a defect (artifact 1).
- **A-09-3** hole, H11: no "suggestion for comparing groups" by Cole appears in the original.
- **A-09-4** hole, H12: risk ratio, odds ratio and P value are defined nowhere in the original.
- **A-09-5** hole, H13: "equalities" and the one-or-two-places choice are unexplained there too.
- **A-09-6** hole, H14: the original's table words the mean rule in decimal places too.
- **A-09-7** hole, H15: SE = SD/√n and a basis for choosing the SD or SE rule are not in the
  original.
- **A-09-8** hole, H16: the original also states the rule of four only for risk and odds ratios.
- **A-09-9** hole, H17: "±" and "CI" are unexplained in the original.
- **A-09-10** hole, H18 (error or unmarked plant): 9.2 cannot be derived from the given counts.
- **A-09-11** restored in part: "When n people are counted, one person moves a percentage by 100 ÷
  n percentage points." This defines n in use. Residual hole H19: Cole is cited only in C05's
  reference list, not in C09.
- **Symbols** hole, H20: "P" and "p" both used, "<" unexplained, "rule of four" ambiguous, "lakh"
  defined only in P12. Same in the original. (n is closed by A-09-11.)

### C10
- **A-10-1** restored: "At the scale of a paragraph, the first sentence sets the topic and the
  body carries the content." and "The last sentence gives the conclusion to remember." These say
  what context, content and conclusion are. Residual hole H21: Mensh and Kording are introduced
  only in C02 and C03 of the original, and no C02–C09 cut keeps their name. That belongs to the
  r1 restorer or the conductor.
- **A-10-2** restored in part by the same two sentences: the topic sentence comes first. Residual
  hole H22: "answer last" is undefined in the original.
- **A-10-3** hole, H23: Ex 1 asks for three things; the original's must-know gives four (split,
  merge, move, cut).
- **A-10-4** hole, H24: the paragraph behind the figure is not in the original, and Ex 2's
  paragraph does not match the figure's topic sequence.
- **A-10-5** not a defect (artifact 2), if the build renders `S58-R1-C04` as a section name.
- **A-10-6** not a defect (artifact 1).

### C11
- **A-11-1** hole, H25: the original gives no syllable rules for doubtful words, abbreviations,
  "%" or numerals.
- **A-11-2** hole, H26: the draft and Rewrites A and B are not in the original. "As Rewrite B
  did" was left cut, since restoring it would name a text the reader never sees.
- **A-11-3** restored in part: "For almost all ordinary prose the score falls between 0 and 100,
  but the formula can go below 0 or above 100." This gives the scale's range, which P8 and P11
  need. Residual hole H27: "Plain English minimum of 60" is only in a caption, with no source.
- **A-11-4** hole, H28: "figures" means numerals here and charts elsewhere; the two sentences are
  not shown. Same in the original.
- **A-11-5** hole, H29 (error): P5's score of 32 matches neither 66 nor 67 syllables, and P6
  gives away P5's syllable count.
- **A-11-6** not a defect (artifact 1).
- **A-11-7** restored in part: "Plavén-Sigray and colleagues (2017) scored 709,577 abstracts from
  123 journals, published from 1881 to 2015." This cites "harder to read" and "709,577
  abstracts". Residual hole H30: "one large study dropped them" is never tied to a source.
- **A-11-8** hole, H31: the original never relates a US school grade to an Indian class.
- **Symbols** restored in part: "Flesch wrote the second term as 0.846 times the syllables per
  100 words, which gives the same score." This ties 84.6 and 0.846 to one term in two units, and
  P4's counts come per 100 words. Residual hole H32: "71/52", "1 1/2" and "Rewrite A" are
  unexplained.

### C12
- **A-12-1** hole, H33: the discussion draft is not in the original.
- **A-12-2** hole, H34. The original's "A qualifier such as an age range, a year, a place or 'or
  obese' looks like padding." was tried. It raised the mean sentence length from 12.64 to 12.71
  and failed validation, so it was dropped. The list file records the attempt. Even restored,
  the original never demonstrates the test.
- **A-12-3** hole, H35: the original's Ex 2 has the same ambiguity.
- **A-12-4** hole, H36 (contradiction): C07 and C12 give conflicting rules for a passive with no
  doer.
