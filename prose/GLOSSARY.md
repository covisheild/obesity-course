# Terms of art, and the plain words they get at first use

Append-only. `claude.md` §10 requires that a term is introduced once and afterwards used in the
same words. The build enforces that inside a booklet; this file is what enforces it across
booklets, which matters as soon as more than one chat is writing. See `PARALLEL.md`.

**Before teaching a term of art, look for it here.** If it is listed, teach it in the plain words
recorded here. If it is not, add the row in the same commit that first teaches it.

Changing an existing row means every booklet that used it must change too. That is a
between-rounds job, never something a chat does mid-book.

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| amendment | a change made to a law after it was passed | B0-R0-C41 |
| consolidated | a copy with all the later changes merged into one text | B0-R0-C41 |
| denominator | the number a percentage is a percentage of | B0-R0-C39 |
| executive | the people who run the country day to day | B0-R0-C43 |
| Gazette | the government's official newspaper of record | B0-R0-C43 |
| inference | the move from the reasons to the conclusion | B0-R0-C42 |
| instrument | the word lawyers use for any of these written things at once | B0-R0-C43 |
| locator | the page, section or clause number that says where to look | B0-R0-C41 |
| notification | an announcement in the Gazette that makes something take effect | B0-R0-C43 |
| precision | how tightly a measurement pins the number down | B0-R0-C39 |
| premise | a reason offered | B0-R0-C42 |
| regulation | a rule written by a body that a statute gave the power to write rules | B0-R0-C41 |
| statute | a law passed by a legislature | B0-R0-C41 |
| unit of observation | what one row of a table stands for | B0-R0-C39 |

Seeded from the terms-of-art table in `check/_build/check_report.md` for the four finished Book 0
sections. Everything after this line was added by a chat that taught the term.

## Added by the Book 0 Part A chat, 2026-09-20

Sections A1 to A8. Same rule: before teaching one of these, use the plain words recorded here.

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| exponent | the small raised number that says how many copies to multiply together | B0-R0-C06 |
| logarithm | the power you have to raise ten to, to get the number | B0-R0-C07 |
| numerator | the number above the line, saying how many of the parts you are holding | B0-R0-C02 |
| order of magnitude | which power of ten a number is nearest to | B0-R0-C08 |
| percentage point | the plain difference between two percentages, as against per cent, which divides | B0-R0-C04 |
| place value | what a digit is worth because of where it sits | B0-R0-C01 |
| proportion | a part out of the whole it came from, never more than one | B0-R0-C05 |
| rate | a count divided by the time, or the number of people, it was counted over | B0-R0-C05 |
| ratio | two quantities of the same kind set side by side by dividing one by the other | B0-R0-C05 |
| scientific notation | a number between one and ten, times a power of ten | B0-R0-C06 |
| significant figures | the digits in a number that carry information about the quantity | B0-R0-C03 |
| square root | the number which, multiplied by itself, gives you the one you started with | B0-R0-C06 |

**Two rows above this section now name the wrong record, and are not changed here.** With Part A
written, document order puts the first use of **denominator** in `B0-R0-C02` and of **precision**
in `B0-R0-C03`, not in `B0-R0-C39`. Changing an existing row is a between-rounds job under
`PARALLEL.md`, so the correction is carried in `books/B0/HANDOVER.md` instead. The plain words
recorded for both were used unchanged.

One note on **denominator**, for whoever makes that correction. The recorded words — "the number a
percentage is a percentage of" — are right for a percentage and do not describe a fraction. A2
teaches it as the number below the line, which is where the reader first meets it, and A4 gives
the recorded words at the point the percentage sense arrives. The row wants both senses when it is
next opened.
