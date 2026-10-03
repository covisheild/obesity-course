# S58-R1 change record, version 1.0

For Harsh only. The build renders this file to check/_build/S58-R1-change-record.docx. Nothing
here is printed in the book (Harsh, 28 Sep 2026).

## What this version is
Built from scratch, 2–3 October 2026: Book 9, Scientific writing, visualisation and public
communication · Rung 1. Twenty-three sections, drafted from 28 held sources (plus three extras) after
the source-collection stop, which Harsh released by supplying Kincaid 1975, Cleveland & McGill 1984
and Tufte, and by accepting the public-domain reprint of Flesch 1948. Compressed, cold-read by two
fresh readers, figured, audited, fixed and verified; the built PDF was then read by a fresh reader and
its record-level faults fixed and verified.

## Changes, by section
| Section | Change | Why (defect, reader note, new source) |
| --- | --- | --- |
| 5 · Citing and referencing | New section | Map amendment S58-R1-A02, accepted by Harsh 2 Oct 2026 (coverage gap 4: ICMJE §IV.A.3.g, NLM Citing Medicine) |
| 21 · Making a table that stands alone | New section | Map amendment S58-R1-A01, accepted by Harsh 2 Oct 2026 (coverage gap 1: NMC "tabular presentation", ICMJE §IV.A.3.h, Wilke ch. 22) |
| 11 · Measuring a draft | Reading Ease formula taken from Flesch's own words (.846); Kincaid 1975 used only for the grade-level formula | Kincaid's Table 3 prints ".836", a misprint shown by Flesch 1948 and his worked tables |
| 22 · Making the plot | Taught without a particular tool; a spreadsheet's defaults need heavy changing; plotting code left to the R book | Harsh's decision 2 Oct 2026, following Wilke's Preface |
| All | "with overweight or obesity" in the book's own prose; the survey's indicator keeps its own words when quoted | claude.md §9 (people-first) |
| Map | Five amendments written to `map/AMENDMENTS-v3.1.yml`: S58-R1-A01 (table), S58-R1-A02 (referencing), S58-R2-A01 (poster added to P3), S58-R2-A02 (choosing a journal, cover letter, answering reviewers), S58-R2-A03 (licences and permission for figures) | Harsh accepted all five coverage gaps, 2 Oct 2026 |

## Open decisions for Harsh
- **A contract-change chat for the shared tools.** Four items cannot be fixed inside a book while
  `check/**` is frozen: the reference lists are not in the NLM style section 5 teaches; √, ≈ and the
  superscript minus print blank in tables, captions and every book's Symbols page (one CSS line);
  the figure tool always adds a legend beside direct labels, and for this book's colour its two series
  colours turn the same grey. This book's figures therefore break two of its own rules (sections 18
  and 19), though they read in grey through their labels. Details in `books/S58-R1/HANDOVER.md`.
- **Map line S58-R2 P1** ("most rejected Indian manuscripts are rejected for writing and framing")
  has no source; it needs one at S58-R2's intake, or rewording.
- **Single page reads of NCBI Bookshelf and UCF STARS**, whose terms bar systematic automated
  retrieval; this was not systematic, but it is your call.

## Not taught, and why
Nothing was left out for want of a source. The map's NFHS-based statements are taught from the
NFHS-5 India fact sheet only; the fact sheet prints no confidence intervals, so the book says how sure
one can be only in words. No held source states which abbreviations journals treat as standard, or
names who, which and that as words opening a subordinate clause, so the book does not list them.
