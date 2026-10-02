# Source intake log · S58-R1 · group T (Tufte: Lie Factor, graphical integrity, data-ink, chartjunk)

One pass, 2 Oct 2026. Source supplied by Harsh by hand (not fetched): four PDFs split from one 208-page scan,
in `/root/.claude/uploads/f2099557-ac04-5a0f-a543-1cd2874da8af/` (`664e5786-1_SplittRare_*`, PDF pp. 1-50;
`abae68c0-51_*`, 51-100; `4701cb92-101_*`, 101-150; `5949e965-151_*`, 151-208). File names end
`Anna_s_Archive.pdf`: the copy comes from a shadow library; the scan inside is an Internet Archive
digitisation (2023, item bwb_T2-EQU-551). The source file's header says so plainly and holds only short
excerpts, privately, for study and quotation.

Method: `pdftotext -layout` per PDF, saved unchanged as `raw/T-tufte_2001-part<1-4>-pdftotext.txt`.
`intake/build-T.py` cuts each passage as `raw[i:j]` between whitespace-flexible anchors (as `build-K.py`),
refuses any passage that crosses a page break, writes `sources/tufte_1983_visual_display.txt`, then re-reads
the file from disk and tests every [TEXT] passage as a whitespace-normalised substring of the raw named in its
block. OCR errors were NOT corrected in passages; each is given its true reading in a [NOTE]. Nothing committed;
INDEX.yml, library.bib and SOURCES.md untouched (entries in `fragment-T.md`).

**Verbatim check: 30 of 30. Filed: 1 source, 2,225 words of passages.**

| Source | Obtained from | Passages | Check | Licence as stated | Citekey |
| --- | --- | --- | --- | --- | --- |
| Tufte, *The Visual Display of Quantitative Information*, Graphics Press, Cheshire CT, **1st ed. 1983**, tenth printing March 1990 | PDFs supplied by Harsh (Anna's Archive, a shadow library; Internet Archive scan bwb_T2-EQU-551); OCR text layer | 30 (14 blocks) | 30/30 | Copyright page: "Copyright © 1983 by Edward R. Tufte / Published by Graphics Press ... ALL RIGHTS RESERVED" | `tufte_1983_visual_display` |

## Edition: NOT the 2001 second edition

The task named the 2nd edition (2001). The copyright page (PDF p. 8, checked on the image) reads "Copyright ©
1983 by Edward R. Tufte ... Tenth printing, March 1990": this is the first edition. The citekey is therefore
`tufte_1983_visual_display`, not the task's `tufte_2001_visual_display`. The 2nd edition is commonly said to
keep the first edition's pagination for these chapters (e.g. Lie Factor on p. 57), but that was not checked.
**Needs Harsh/conductor:** cite as 1983 (what is held), or check the page numbers in a 2001 copy before citing 2001.

## Book pages held, and page images checked

Book page = PDF page − 4 throughout. Every page from which a passage is held was rendered with
`pdftoppm -r 80` (into the scratchpad as `T-pdf<N>-*.png`) and read against its passage:

| Book page | PDF page | Held |
| --- | --- | --- |
| front matter | 5, 8 | scan provenance leaf; copyright page (edition, printing) |
| 56 | 60 | first two integrity principles (proportional representation; labelling) |
| 57 | 61 | Lie Factor definition, the 1.05/.95 range, log LF, fuel-economy data change 53% |
| 58 | 62 | lines 0.6 and 5.3 in., 783%, Lie Factor 14.8 |
| 60, 61 | 64, 65 | design variation; "Show data variation, not design variation"; OPEC scales, 15.1 |
| 70, 71 | 74, 75 | areas varying in two dimensions; barrels 9.4 / 59.4; dimensions principle |
| 77 | 81 | the six principles of graphical integrity |
| 93, 94 | 97, 98 | data-ink defined; data-ink ratio; 10-20 percent non-data-ink example |
| 96, 97, 100 | 100, 101, 104 | maximize the data-ink ratio; erase non-data-ink; redundant data-ink; erase redundant data-ink |
| 105 | 109 | the five principles |
| 107 | 111 | chartjunk introduced |
| 112, 113, 116 | 116, 117, 120 | the grid; "Dark grid lines are chartjunk"; gray grid; the duck |
| 121 | 125 | chartjunk conclusion; "Forgo chartjunk" |

## As printed (read from the page images)

- **Lie Factor** (p. 57; display fraction, garbled in the text layer, so transcribed in a [NOTE]):
  Lie Factor = size of effect shown in graphic / size of effect in data.
- **Range:** "Lie Factors greater than 1.05 or less than .95 indicate substantial distortion, far beyond minor
  inaccuracies in plotting." (p. 57; clean in the text layer.)
- **Worked example:** (27.5 − 18.0)/18.0 × 100 = 53%; (5.3 − 0.6)/0.6 × 100 = 783%; Lie Factor = 783/53 = 14.8.
- **Data-ink ratio** (p. 93, display fraction, transcribed in a [NOTE]): data-ink / total ink used to print the
  graphic = proportion of a graphic's ink devoted to the non-redundant display of data-information = 1.0 −
  proportion of a graphic that can be erased without loss of data-information.
- **Chartjunk** has no one-line definition in the book: p. 107 introduces it as decoration that is "all
  non-data-ink or redundant data-ink, and it is often chartjunk". A book must not quote a definition the
  text does not give.

## OCR errors found in held passages (true readings in the file's [NOTE]s)

p. 57 "Lie Factor =" garbled to "TSE CC Oe ee oe"; "1007 = 53%" for "× 100 = 53%"; p. 58 "X< 100:= 783%" for
"× 100 = 783%"; "Lie Factor = 7 ... 59" for "783/53"; minus signs read as dashes (pp. 57-58); p. 93 fraction bar
as "————__________"; p. 96 "sometiines", "nuinber"; p. 61 em dash for en dash ("January—March 1979"); p. 70
stray ">"; scan leaf "owb_T2-EQU-551" for "bwb_T2-EQU-551". 11 in held passages. Outside them: the p. 96 bar label
"659" for "35.9" (skipped by a [...]) and the p. 107 chapter number "§" for "5". None in the Lie Factor range
sentence, the six principles, or the five data-ink principles.

## Not held

All figures; chapters 1, 3, 6-9 and the epilogue; the rest of ch. 2, 4 and 5 (listed in the file header);
notes and index. One p. 71 paragraph was skipped because the barrel figure's text is interleaved with it.
