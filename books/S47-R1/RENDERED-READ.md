# S47-R1 rendered-page cold read (PIPELINE Step 5b, second pass)

Source: `check/_build/S47-R1.pdf`, 173 pages. Read as a reader with only the book in hand.
Pages examined (≈130): 1–34, 44–64, 68–76, 81–110, 116–119, 140–173.
Checked in full: sections 1–6 (early), section 11 (tracing who decides), section 18 (one-page note), the appendix, glossary, series list and back cover.
No symbol was drawn as a box. No repository path or record id (S47-R1-C.., B0-R0-C..) is printed anywhere I read. No heading or label is left alone at the foot of a page.

## 1. Stray markup

| Page | What | Quote | Why it is a fault |
|---|---|---|---|
| 151, 152, 157, 158, 159, 160, 162, 163, 166 | Raw pipe/grid-table source printed as running text in the practice answers (sec 11 items 1, 2, 4, 6; sec 15 items 1–6, 10; sec 17 items 1, 2, 4, 5; sec 18 Ex 4) | "1. +———+————+ \| Part \| In the provision \| +———+ … \| body \| the Board \|" | The table was never rendered. The answers can't be read, and these are the answers the practice sets send the reader to. (p159 item 8 renders correctly, so the input is inconsistent.) |
Fixed: every practice/exercise answer that opened with a table (C11 pr1, 2, 4, 6; C15 pr1–6, 10; C17 pr1, 2, 4, 5; C18 Ex 4) now opens with a short lead line, so the label no longer lands on the grid rule.
| 57 | Stray pipe character in a table cell | "section 4 lists every entry a canteen rule touches \|" | Leftover table-cell markup. |
Fixed: the cross-reference inside the C11 table cell (which shrank after the grid was drawn and broke its alignment) is now the section's title in words: the section "Union, State or local: whose subject is it" lists every entry.
| 165–166 | A Markdown bullet list run together into one paragraph, with literal hyphens | "- Line 1: "The government should ban" is a demand … - Line 2: no instrument … - Lines 3 and 4: …" | Unrendered list markup. Eleven separate faults merge into one block. |
Fixed: C18 Ex 3 answer opens with "Line by line:", so the bullets render as a list.

## 2. Lines running off the page

| Page | What | Quote | Why |
|---|---|---|---|
| 151 | Grid rule in sec 11 practice answer 4 runs past the right margin to the page edge | "+==========+======…" | Text runs off the page, on top of the markup fault above. |
Fixed: same cause as the raw-grid fault above (C11 pr4); lead line added, grid now parsed as a table.
| 152 | Same, in answer 6 | "+=====…=====" | Same. |
Fixed: same cause (C11 pr6); lead line added.
| 163 | Same, in sec 17 practice answers 4 and 5 | "+=========+=============+=====…" | Same. |
Fixed: same cause (C17 pr4, pr5); lead lines added.

## 3. Tables too narrow or broken

| Page | What | Quote | Why |
|---|---|---|---|
| 14 | First column too narrow, so words break mid-word | "prop / ose", "advis / e", "deci / de" | Table too narrow. The key words of the section are broken. |
Renderer/series: column widths are set by the renderer.
| 15 | Same | "propo / se", "advis / e", "decid / e" | Same. |
Renderer/series: column widths are set by the renderer.
| 18 | Header cell broken | "Run / g" | Same. |
Renderer/series: column widths are set by the renderer.
| 22 | Header and cells broken | "entr / y", "Concurr / ent", "33( / b)" | Same. An entry number is split across lines. |
Renderer/series: column widths are set by the renderer.
| 94 | Header and cells broken | "Ma / rk", "campai / gning", "informi / ng", "no / ne" | Same. |
Renderer/series: column widths are set by the renderer.
| 100 | Header broken | "Lin / e" | Same. |
Renderer/series: column widths are set by the renderer.
| 102 | Header broken over three lines | "Li / n / e" | Same. |
Renderer/series: column widths are set by the renderer.
| 19 | Ordered-list numbering inside a table renders every row as "1." | Stage column: "1. / 1. / 1." while the text says "stages (b) and (c)" | The reader can't match the rows to (a), (b) and (c). |
Fixed: C03 Stage cells now read "Stage (a)", "Stage (b)", "Stage (c)", matching the prose.
| 92 | Same | "1. Selective evidence / 1. Uncertainty changed / 1. A value written as a finding / 1. An interest not declared" | The text then says "Mark 3", "Mark 2", "mark 4", but every row reads 1. |
Fixed: C17 cells now read "Mark 1: Selective evidence" … "Mark 4: An interest not declared".
| 96 | Same | "1. Selective evid-ence … 1. An interest not declared" | Same. |
Fixed: same edit in C17's second table.
| 10–11 | Table breaks after the header and one row. The continuation on p11 has no header | p10: header + "agenda setting: the problem"; p11 starts "agenda setting: the options" with no header | Table broken across its header. |
Renderer/series: header not repeated after a page break.
| 51–52 | Actor table continues on p52 without its header | "CSOs such as BPNI and NAPi \| pushes …" | Same. |
Renderer/series: header not repeated after a page break.
| 83–84 | One row orphaned on p84 without a header | "left out \| who pays the higher price …" | Same. |
Renderer/series: header not repeated after a page break.
| 160–161 | One row orphaned on p161 without a header | "the ban can be enforced in every canteen \| partly …" | Same. |
Renderer/series: header not repeated after a page break.

## 4. Missing content and broken cross-references

| Page | What | Quote | Why |
|---|---|---|---|
| 167 | The glossary is empty: a header row and nothing under it | "Term \| Plain words \| Section" (no rows) | p5 promises "The glossary lists every term of art". The page has nothing on it. |
Renderer/series: the PDF was built before the glossary merge.
| 5 | Points to a Symbols page that does not exist (not in contents p7, not between pp 6–8) | "The **Symbols used in this book** page lists every sign and Greek letter" | Cross-reference to something not there. |
Renderer/series: series front-matter text.
| 5 | Points to per-Part reference lists. The book has one rung and one reference list | "The references for each Part follow that Part." | Not true of this book. |
Renderer/series: series front-matter text.
| 108 | "above" points three pages back | "Take the finished note above." | The note is on p105. "Above" sends the reader up the page to Exercise 3. |
Fixed: C18 Ex 4 now says "Take the finished note in this section's second illustration."
| 141 | Boilerplate about "outstanding" entries. No entry is marked outstanding | "An entry marked outstanding has not yet been checked … the reasoning is a derivation you can check with a calculator" | Refers to nothing in the list. It also contradicts "there are no calculations" (p5). |
Renderer/series: the "outstanding" note is renderer boilerplate.
| 30 | Figure appears before Illustration 1. Its caption points forward | "(the second illustration works these figures)" | The figure is two pages from the text that uses it. Figures have no numbers, so the text can't point back to them. |
Fixed: C06 caption drops "(the second illustration works these figures)"; it already carries every figure it shows. Placement is the renderer's.
| 101 | Two figures before the draft their caption depends on | "Line 4 of the failed draft, for drinks with added sugar or flavour." | The failed draft first appears on p102. The reader meets the caption before its referent. |
Fixed: C18 caption now opens "Drinks with added sugar or flavour, before and after the 2025 GST reform." with no reference to the draft. Placement is the renderer's.
| 93 | Captions refer to a draft not yet shown | "The made-up paragraph of the department's note …"; "Mark 2 in the first draft." | The first draft appears on p94. |
Fixed: C17 captions now open "A made-up paragraph of a department's note on a sugary-drinks tax, sentence by sentence, in a first draft and a rewrite." and "Mark 2, uncertainty changed, in a made-up draft note."
| 57 | Source note cites ref [129], which is "The Constitution of India … figures quoted in the text" | "Figures quoted in this illustration are from [129]." | The illustration quotes the FSS Act and no figures. [129] is also the catch-all used for PRS figures on p32. A reader who looks it up finds nothing to match. |
Rejected: the note is generated by the renderer from the illustration's `numbers`, which cite the Constitution for the list-entry numbers it quotes (Union List entry 52, Concurrent List entry 25, State List entry 6); on p32 [129] is cited for the Money Bill's fourteen days, beside [128] for the PRS figures. The wording "figures quoted in the text" is the renderer's.
| 9, 13, 17, 21, 25, 29, 34, 44, 50, 55, 64, 68, 75, 81, 88, 92, 100 | Each definition ends in a block of 15–60 citation numbers attached to one sentence | p55: "[239, 240, … 77, 266, … 300]"; p100: "[422, 53, 251, 253, 437, …]" | The reader can't tell which source supports which claim. Out-of-order runs (p29 "107, 88, 90, 108") look like errors. |
Renderer/series: citation marks are generated per definition by the renderer.

## 5. Text that contradicts itself

| Page | What | Quote | Why |
|---|---|---|---|
| 5 vs 5, 19, 46, 95, 104, 141 | Says there are no calculations, then asks for a calculator and promises derivations. Arithmetic blocks follow | "there are no calculations" / "Keep a calculator beside you … Worked derivations can be skimmed" | Contradicts itself on one page, and with the later date and percentage arithmetic. |
Renderer/series: series front-matter text.
| 5 vs whole book | Says most sections carry a practice set | "in most sections, a graded practice set" | Only sections 11, 15 and 17 (3 of 18) have one. |
Renderer/series: series front-matter text.
| 3, 173 vs 19 and every "Checked" line | Date mismatch | Copyright and back cover: "1 October 2026"; p19: "This book is written on 2 October 2026"; sections: "Checked against the sources as they stood on 2026-10-02" | The book says it was last updated before it was checked. |
Renderer/series: copyright and back-cover dates are the renderer's; the record's 2 October 2026 is the checking date.
| 168 | Series list marks this book unfinished | "5 Policy process … ◀ you are here \| in progress" | This is version 1.0, released. |
Renderer/series: series list status.
| 7/100 vs 165 | Section 18 title differs between body and appendix | "18 · Worked journey: A one-page note on one Indian proposal" vs "18 · A one-page note on one Indian proposal" | Titles don't match. |
Renderer/series: the "Worked journey:" prefix is added by the renderer.

## 6. Abbreviations not spelled out

| Page | What | Quote | Why |
|---|---|---|---|
| 168–172 | "HTA" never expanded | "Health financing, HTA and pharmaceutical access in India" | Abbreviation the reader may not know. |
Renderer/series: HTA is in another book's title in the series list.
| 30, 32 | "PRS" never expanded | "PRS Legislative Research" | Minor: it is an organisation name, but the reader isn't told. |
Rejected: "PRS Legislative Research" is the organisation's name, not an abbreviation the book uses; no held source expands "PRS", and C06 already says what it is ("an independent, not-for-profit group").

## 7. Layout faults (other)

| Page | What | Quote | Why |
|---|---|---|---|
| 142, 143, 144, 145, 147, 150 | Appendix answers to multi-part exercises: the answer to item 1 runs inline after the label, then the list restarts at 1, so items 2–4 print as 1–3. The list text is also larger than the paragraph text | p142 Ex 2: "1. Not yet a policy …" then "1. Wrong as stated … 2. The conclusion does not follow … 3. A description of a programme" | The reader matches the wrong answer to each question. Exercise 2 on p12 has four items, and the answers number 1, 1, 2, 3. |
Fixed: every exercise answer that opened with a list (C01 Ex 2, Ex 4; C04 Ex 1; C05 Ex 1; C06 Ex 1; C10 Ex 2; C11 Ex 1) now opens with a lead line, so the list numbers 1, 2, 3, 4.
| 151, 157, 162 | Practice answers start with no "Practice" label, straight after the exercise answers | "Quotable sentence: … / 1. +———+…" | The reader can't tell where exercise answers end and practice answers begin. |
Renderer/series: the appendix has no Practice label.
| 34, 81, 88, 92, 100 | "IN PLAIN TERMS" label sits inside the shaded Definition box | p34: "…bye-laws… [130 … 154] IN PLAIN TERMS. Parliament passes an Act." | Plain-terms text looks like part of the formal definition. Elsewhere it sits outside the box. |
Renderer/series: placement of the plain-terms label.
| 10, 26, 30, 32, 45, 47, 109, 110, 116, 140 | Hyphens added to URLs at line breaks | "https://nhsrcin-dia.org/…Nation-al%20Health…", "(ht-tps://www.pib…", "https://le-gislative.gov.in", "https://prsindia.org/art-icles…", "https://taxin-formation.cbic…/sec-tion9", "https://cab-sec.gov.in", "https://egaz-ette.gov.in" | A reader who types the URL from print gets a wrong address. The text tells the reader to "open" these sources. |
Renderer/series: URL hyphenation at line breaks.

## 8. Sentences I had to read twice

| Page | Quote | Why |
|---|---|---|
| 13 | "The releases name no power for this decision; the next section shows where to look." | Inside the definition, before any release has been mentioned. |
Fixed: C02 now reads "The government's press releases on this approval name no power for it; the next section shows where to look."
| 21 | "trade in the food industry's products also falls under Concurrent List entry 33(a)" | Every other mention, and the table on p22, uses 33(b). 33(a) is never quoted or explained. |
Fixed: 33(a) is right (it covers "the products of any industry" Parliament has declared under Union control); C04 now says so: "Concurrent List entry 33(a), the products of a declared industry."
| 34 | "Under that Act it then goes before Parliament (a State rule, before the State Legislature)…" | "That Act" could be the General Clauses Act or the FSS Act. |
Fixed: C07 now reads "Under the Food Safety and Standards Act it then goes before Parliament, which can change it or cancel it. A State rule goes before the State Legislature."
| 57 | "section 4 lists every entry a canteen rule touches" | Book section 4, or section 4 of an Act? The cell sits among FSS Act section numbers. |
Fixed: see the stray-pipe fault; the cell now names the section by its title.
| 57 | "The next subject, on India's regulatory architecture, owns the map of food regulators." | "Subject" is an internal course term. The reader doesn't know it means another book. |
Fixed: C11 now reads "The book in this series on India's regulatory architecture maps the food regulators."
| 58 | "Tobacco control is the main precedent the next level of this subject studies." | Same internal jargon ("level", "subject"). Also on p50, p53 ("the next level of this subject") and p59 ("for the subject on implementation"). |
Fixed: "a later book in this series" in C10 (twice), C11 and C14 ("Rung 2 of this subject"); C11 also "for the book in this series on implementation" and "a question for a later book".
| 62 | "section 7 read this preamble for its dates. Now work backwards through the trace." | Starts lower-case. Reads as a broken fragment (probably meant "Section 7 read…"). |
Fixed: C11 pr6 now reads "You read this preamble for its dates in section 7."
| 68 | "The largest held measurement is a United States survey …" / "The studies held for this book, that is, the ones it has opened and read" | "Held" is used in a private sense. It recurs as "held Indian evidence" and "No held study". |
Fixed: C13 now reads "The studies this book has opened and read name these…", "The largest measurement among them", "The Indian evidence among them", "None of them measures".
| 89 | "The course has not read the study" | "The course" is used where the book says "this book" everywhere else. |
Fixed: C16 now reads "This book has not read the study".
| 99 (and 164) | "Our survey of students at one college, described in section 2, proves …" | "Section 2" is a section of the made-up note, but in this book it reads as book section 2. |
Fixed: C17 practice item now says "section 2 of this note" in the quoted sentence, the worked line and the fix.

## Counts

- Stray markup: 3 entries (11 pages)
- Lines running off the page: 3
- Tables too narrow or broken: 14
- Missing content or broken cross-references: 10 (one is a citation-block pattern across 17 pages)
- Contradictions: 5
- Abbreviations not spelled out: 2
- Other layout: 4 (the URL one covers 10 pages)
- Read-twice sentences: 10
- Symbols drawn as boxes: 0. Repository paths or record ids: 0. Stranded headings: 0.

## Three worst

1. Raw grid-table markup in the practice answers (pp 151–166). It can't be read, and some lines run off the page.
2. The glossary is empty (p167), though p5 promises it.
3. Appendix answer numbering is off by one for multi-part exercises (pp 142–150), so answers are matched to the wrong items. A close fourth: the Symbols page that p5 points to does not exist.
