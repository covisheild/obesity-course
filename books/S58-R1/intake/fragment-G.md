# S58-R1 intake, group G (Cleveland & McGill 1984, graphical perception): entries to merge

Three blocks for the conductor to paste into `sources/INDEX.yml` (under `files:`),
`check/references/library.bib` (append) and `sources/SOURCES.md` (a new section). One file:
`sources/cleveland_mcgill_1984_graphical_perception.txt`. The citekey
`cleveland_mcgill_1984_graphical_perception` was grepped in `sources/INDEX.yml`,
`check/references/library.bib`, `sources/SOURCES.md` and every `books/*/intake/fragment-*.md` on 2026-10-02,
at the start and at the end of intake: none exists. Grep again at merge (S47-R1 and S52-R1 are adding keys on
other branches). Log: `books/S58-R1/intake/log-G.md`.

**Merge consequence:** READY.md lists Cleveland & McGill as "no" (Harsh-only, optional for C14). It is now
held. The `heer_bostock_2010_crowdsourcing_perception` entries describe Experiment 1A as a replication of
Cleveland & McGill; both papers can now be cited side by side for C14.

## 1. `sources/INDEX.yml`, under `files:`

```yaml
  cleveland_mcgill_1984_graphical_perception:
    file: cleveland_mcgill_1984_graphical_perception.txt
    what: >-
      Cleveland & McGill, Graphical perception: theory, experimentation, and application to the development of
      graphical methods, J Am Stat Assoc 1984;79(387):531-554 (doi 10.1080/01621459.1984.10478080). PDF supplied by
      Harsh 2 Oct 2026 (Taylor & Francis download, scanned, OCR text layer). (c) ASA, publisher's terms: private
      study only; excerpts, held for study and quotation. Held: T&F cover page and copyright line, abstract, Figure 1
      sentence (10 elementary perceptual tasks), section 3 ordering (1 position common scale; 2 nonaligned scales;
      3 length, direction, angle; 4 area; 5 volume, curvature; 6 shading, color saturation; ties at 3, 5, 6),
      experiments' design (55 and 54 subjects, 51 analysed each), accuracy measure log2(|judged - true| + 1/8),
      results (length errors 40%-250% above position; angle 1.96 times position; pie better than bar in 3 of 40;
      large errors 5.3 and 7.3 times), 4.5 summary, 5.1 dot charts replace pie and divided bar charts, section 6
      conclusions. Numbers checked against page images; OCR errors noted in [NOTE]s. Figures, psychophysics,
      bootstrap, bias, 5.2-5.4, references not held
```

## 2. `check/references/library.bib`, append

```bibtex
@article{cleveland_mcgill_1984_graphical_perception,
  title        = {Graphical Perception: Theory, Experimentation, and Application to the Development of
                  Graphical Methods},
  author       = {Cleveland, William S. and McGill, Robert},
  journal      = {Journal of the American Statistical Association},
  year         = {1984},
  month        = sep,
  volume       = {79},
  number       = {387},
  pages        = {531--554},
  doi          = {10.1080/01621459.1984.10478080},
  note         = {Copyright American Statistical Association; published by Taylor \& Francis; not open
                  access. Quoted from the publisher's PDF (a scan with an OCR text layer); quoted numbers
                  checked against the page images}
}
```

## 3. `sources/SOURCES.md`, new section (same columns as the main table)

```markdown
## S58-R1 intake, group G: Cleveland & McGill 1984, graphical perception (2 Oct 2026)

| File | What it is | Words | Verified in it |
| --- | --- | --- | --- |
| `cleveland_mcgill_1984_graphical_perception.txt` | Cleveland and McGill, *J Am Stat Assoc* 1984;79(387):531-554 (doi 10.1080/01621459.1984.10478080); PDF supplied by Harsh 2 Oct 2026 (Taylor & Francis download, scanned, OCR text layer). © ASA; T&F terms: research, teaching and private study only. **Excerpts** | 3,083 | Abstract ("Graphs should employ elementary tasks as high in the ordering as possible"; "radical surgery on these popular graphs is needed"); 10 elementary perceptual tasks ordered most to least accurate: 1 position along a common scale, 2 positions along nonaligned scales, 3 length, direction, angle, 4 area, 5 volume, curvature, 6 shading, color saturation (ranks 3, 5, 6 are ties; a hypothesis); position-length experiment, 55 subjects, and position-angle experiment, 54 subjects, 51 analysed in each; error = log2(\|judged percent − true percent\| + 1/8), midmeans; length errors 40%-250% larger than position (factor 1.4 to 2.5); angle errors a factor 1.96 (2^.97) larger than position; pie chart more accurate than bar chart in only 3 of 40 cases; large errors 5.3 times (length) and 7.3 times (angle) as frequent as for position; pie chart → bar or dot chart, divided bar chart → grouped dot chart, "neither graphical form should be used"; accuracy fell as position judgments moved apart (0, 2.8, 5.6 cm). OCR errors (e.g. "2'.32" for 2^1.32, "(3.)" for "(5).)") noted, not corrected |
```
