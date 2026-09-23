# Defects · Book 0 F2 (`B0-R0-C40`)

Audited 23 September 2026 by a subagent that wrote none of it, against the held sources, the live
OpenStax pages, Schedule II of the National Food Security Act, and the neighbouring records C5
(`B0-R0-C19`) and F1 (`B0-R0-C39`). Twenty-one defects; all closed.

## The three that were in the sources, and were mine

The auditor fetched both OpenStax pages live and compared every held sentence. **Every sentence
matched word for word.** What did not match was what the file headers claimed.

1. **`openstax_contemporary_math_8_2.txt` said "the subsection as published … no other change"**
   and was an excerpt. The cuts mattered: Steps 1 and 2 were missing, and they are the only words
   showing that the source's "Beware of vertical axes that don't start at zero" is about a *bar
   chart*. F2's whole zero-baseline argument rests on that distinction, and the held file could not
   show it. **Closed** — Steps 1, 2, 5 and 6 restored verbatim; every omission now marked where it
   falls; the header says "excerpt" and lists what is held.
2. **A sentence beginning "Both of these data representations" sat in the file with its antecedent
   cut.** **Closed** — the preceding sentence restored.
3. **`openstax_business_stats_2_1.txt` claimed the whole subsection and dropped its framing
   paragraphs.** Those paragraphs — Huff's *How to Lie with Statistics*, and "Purposeful
   manipulation is fraud and unethical" — are what mark its "be sure that the axis does not begin at
   zero" as irony. Without them the file reads as advice to truncate. **Closed** — restored; the
   subsection is now held whole.

A fourth, found on checking the licence before any of this: I first wrote both files up as CC BY
4.0. **Both books are CC BY-NC-SA 4.0**, confirmed on their details pages. Corrected before commit.
The course is non-commercial, so short attributed excerpts are within the licence.

## In the record

| # | Kind | What was wrong | Status |
| --- | --- | --- | --- |
| 4 | error | The unequal-bins check said a wider bin "covers more page". OpenStax's own example is a bar drawn the same width whose label "over 80" hides 80–200; F2's check would have passed it | Closed: read the range under each bar |
| 5 | error | "Overstates by the scale factor squared". It shows k² where the numbers show k, so it overstates by k | Closed |
| 6 | over-claim | "The 2.42 is what it takes in" — the source says only that the eye reads area more easily than height | Closed |
| 7 | over-claim | Side-by-side pies "cannot be compared" — shares can; amounts cannot | Closed |
| 8 | over-claim | A line chart from 400 "is fine" — C5 adds that a non-zero axis makes wiggles look like cliffs and steepness is never a measurement | Closed: steepness caveat added |
| 9 | minor | The line-chart condition was weaker than C5's | Closed: "printed on the axis and stated in the caption", everywhere, including the must-know |
| 10 | over-claim | Two-axis crossing "tells nothing about the two quantities" — it tells both values, read against their own axes | Closed |
| 11 | minor | "Each mark carries its value in one of three ways" — colour and shade exist | Closed: "most marks" |
| 12 | gap | Exercise 2 called side-by-side pies a known fault the section never taught | Closed |
| 13 | minor | A threshold stated as 4 per cent that is 4.05 | Closed |
| 14 | gap | Unequal bins had no practice problem | Closed: level 7 diagnostic added. Its first answer over-claimed — "the readings over 80 are the thinnest" — when all 18 could sit between 80 and 100; scoped to an average in the main-thread read |
| 15–16 | minor | Figure labels 1.8 and 1.56 against text saying 1.78 and 1.556 | Closed |
| 17 | gap | Said it agreed with F1 and C5 without saying how; dropped F1's "out of what" | Closed |
| 18 | minor | "The caption says which" — many do not | Closed |
| 19 | minor | Two uncertainty phrases past the Part D boundary | Closed: deleted |
| 20 | minor | "A log axis … says so" — it does not announce itself | Closed |
| 21 | minor | `concept_deps` missed C12, energy units | Closed |

## Found in the main-thread read after the fix

- **The bibliography leaked a repository path.** My own bib notes read "… is held in sources/", and
  they print in the reader's reference list — one of the seven defects Harsh reported on the first
  draft of this book. Fixed, and the render now checks the built page for any repository path,
  which is the second leak of this class and the reason it is now mechanical.
- **The must-know on zero baselines** said a line chart "need not" start at zero without the
  condition every other place now carried. Condition added.
