# S58-R1 step 5c, batch r4: holes for the fixer (C19 to C23)

Found by the compression pass (cold reader B, `COLD-READ-GAPS.md`). Each is something the original
does not fill either, an error, or an original sentence that could not come back without raising the
mean sentence length (or, item 12, without tripping a tool conflict). Field names are those of
`<S>-prose.yml`; "Ex" and "Figure" items sit outside the prose files. Quotations are of the final text
(`-final-prose.yml`) or, for exercises and captions, of the record.

## C19

1. **B-19-1, definition.text / Ex 1.** "Or it picks out one element against others drawn in grey."
   Ex 1 asks for "the kind of colour scale each job takes"; the third job has no named scale.
   Close: name what the highlight job uses (one strong colour against grey) in the definition, or
   reword Ex 1 to ask for the scale for the first two jobs only.
2. **B-19-2, definition.text.** "It separates groups that have no order, using a qualitative scale".
   Groups that do have an order (Ex 2's four age groups) are covered nowhere. Close: one sentence
   saying which scale ordered groups take.
3. **B-19-4, must_know[7].point.** "When you review a colleague's map or heat map ... Is there a colour
   bar?" Neither "heat map" nor "colour bar" is defined. Close: a dash-gloss for each at first use.
4. **B-19-6, definition.text.** "a small set of colours that look clearly different from each other
   and equally strong." "Equally strong" is undefined, and lightness is never set against hue, which
   the red-green rule depends on. Close: define strength (saturation) and hue in a clause each.

## C20

5. **B-20-2, definition.text.** "or a 95% confidence interval (CI). When n is 10 or more, it is
   approximately the mean plus or minus 2 SE." A recipe, not a meaning. The original's "A 95% CI is a
   range worked out from the sample so that, if the study were repeated many times, 95 per cent of
   such ranges would contain the true mean of the population." fills it but raised the mean
   sentence length. Close: restore it as two shorter sentences, or after another cut in C20.
6. **B-20-3, Figure caption / definition.text.** "27.7 for an approximate 95% confidence interval (4
   times the standard error, their rule for three values)" against "When n is 10 or more, it is
   approximately the mean plus or minus 2 SE." Nothing covers n from 4 to 9. Close: one sentence
   saying the multiplier falls from about 4 at n = 3 towards 2 by n = 10, with the source.
7. **B-20-4, must_know[7].point.** "Bars on the same group measured at different times cannot show
   whether the group changed (Cumming's Rule 8)." The rule number means nothing to the reader, and
   the per-person interval is never shown. Close: cite Cumming, Fidler and Vaux (2007) by name and
   drop "Rule 8", or give a three-person example of the change interval.
8. **B-20-6, Ex 3.** "Error bars represent variation. *p<0.05." The P value and the asterisk
   convention are taught nowhere (A-00-5 also). Close: a one-line gloss of the convention in the
   exercise, or a pointer to where P values are taught.

## C21

9. **B-21-2, simplified_explanation / must_know[7].point.** "Numbers line up on the right and keep the
   same number of decimal places." against "Give each value the digits it needs, and line the column
   up on the decimal point." No rule for which wins. Close: say right alignment holds when the
   decimal places are the same, and decimal-point alignment when they differ.
10. **B-21-4, Ex 2.** "measured in grams per decilitre (g/dl)". Litre and deci- are not taught (floor
    test 2). Close: one clause, "a decilitre is a tenth of a litre", with litre glossed.
11. **B-21-5, definition.text.** "Explanations, exclusions and nonstandard abbreviations go in
    footnotes". Nothing says which abbreviations are standard. Close: name the authority (the
    journal's list) or give two examples of each.

## C22

12. **B-22-5, illustration.body / caption.** "Here: between NFHS-4 and NFHS-5, the share with anaemia
    rose in every group." and the caption's "in every group the India fact sheet reports". (a) The
    reader cannot tell the claim covers the rows left out of the table. The original's "The fact
    sheet's rows for non-pregnant and pregnant women rose too. They are left out because the row for
    all women contains them, ..." fills it, but restoring it brings back the Lie Factor working block
    without its introduction (tool conflict, `RESTORE-DECISIONS-r4.md`). (b) A rise of 29.2 to 31.1 is
    called a rise with no way, taught anywhere, to check it against sampling variation. Close: (a)
    restore once the tool is fixed; (b) a sentence saying the claim is descriptive and the confidence
    intervals in the full NFHS report are where to check it, or soften "rose" for the small rises.
13. **B-22-1, Ex 1 / illustration.body.** "list the nine decisions for making a figure" against the
    worked sheet's ten rows, one of them "data". Close: drop the data row into the claim row, or say
    the sheet records the data as well as the nine decisions.
14. **B-22-2, illustration.body (sheet) / section 18.** "legend names the rounds" against section 18's
    "delete the legend" and the sheet's own "each round named over the first pair". Close: choose one;
    direct labels fit section 18 and step 6.
15. **B-22-6 and B-22-3, illustration.body / caption.** "Bars show the per cent anaemic, by each
    group's own haemoglobin cut-off". The restored rows give 11.0 g/dl for children and 13.0 for men;
    the women's cut-offs (non-pregnant 12.0, pregnant 11.0, in C21 Ex 2 only in part) are given
    nowhere. Also "save a vector graphic, such as a pdf ... a png where a bitmap is required, and
    never a jpeg": pdf, png and jpeg are never named as kinds of file. Close: one clause for the
    women's cut-offs from the fact sheet's footnote 22; a dash-gloss saying png and jpeg are bitmaps
    and pdf can hold a vector graphic.

## C23

16. **B-23-1, Figure caption.** "the diary 61.6, the claim draft 79.7, after the cut 86.7". The three
    drafts are never shown; the section has no worked journey. Close: an illustration carrying the
    finding through the nine steps, with the three drafts.
17. **B-23-3, must_know[6].point.** "Format each kind of source from its own chapter of Citing
    Medicine." Only the journal-article format was taught. The original's "A fact sheet read online is
    not a journal article: it follows the chapter on titles on the Internet." raised the mean sentence
    length and was not restored. Close: restore it, and show one formatted Internet entry.
18. **B-23-4, Ex 3.** "say how sure you are". No tool for uncertainty is taught, and the NFHS sample
    size appears only as a placeholder. Close: tie it to the CI of item 5, or reword the exercise.
19. **B-23-6, simplified_explanation (error).** "The result is the share of Indian adults with
    overweight or obesity in two national surveys." Drops the 15-49 range, and 15-17-year-olds are not
    adults (also sections 14 and 17). Close: "Indian women and men aged 15 to 49".
20. **B-23-7, Ex 2.** "Obesity in Indian women up 17%" needs 20.6 and 24.0, carried from section 17;
    the section never prints the finding's numbers. Close: print the two figures in the plain terms or
    the illustration of item 16.

## Symbols (reader B's list, as it touches C19 to C23)

21. **C20 Ex 2, C21 must_know[3].point and Ex 3, C21 Ex 2, C22 rows.** "±" is glossed once (earlier)
    and "<" never. Close: gloss each at first use in these sections ("plus or minus", "below").
22. **C20 definition.text and Ex 2.** "the standard error of the mean (SE)" against "SEM is the
    standard error of the mean". Two abbreviations for one term, against section 08's one-term rule.
    Close: use SE throughout and say journals also write SEM.
23. **C20, C21, C22.** "title" means the caption's opening (C20), text across the drawing (C22) and the
    table heading (C21). Close: say once that a figure's title sits in its caption and a table's above
    the table.
24. **C19 definition.text / section 18.** "Colour that does none of these jobs is ornament." against
    section 18's "decoration". Close: one term in both.
25. **C20 Ex 3 / C22 illustration.body.** "a side axis titled 'BMI'" against "the value axis". Close:
    one term, glossed once.
