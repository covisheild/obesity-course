# Drafter's self-check

Run this on your own records before handing back. Every item is a kind of defect that audits of
Parts A to F found more than once. The build catches some things mechanically; everything below is
what it does not catch. An auditor will still check all of it — this list exists so that the audit
finds little, because a defect fixed at draft time costs a fraction of one fixed after an audit.

When an audit marks a defect **recurring** and it is not on this list, add it here.

## Support

1. **Each quote carries the claim it is cited for**, not merely a nearby one. The commonest
   serious defect: a quote genuinely in the source, made to stand behind something it does not
   say. Read the quote alone and ask whether it says your sentence.
2. **A quote cited for a number states that number.** A table of contents or a heading does not.
3. **Every figure about the world has a citekey** — in prose, in practice prompts and in practice
   answers alike — and appears in `illustration.numbers` where it is an illustration's number.
   A made-up figure is said to be made up in the sentence that introduces it, and the count is
   right ("both figures are made up" when there are two).
4. **No conclusion the source does not license**, especially a policy conclusion, and nothing that
   pre-empts what a later section establishes.
4a. **A rate or a fitted equation is used only where it was measured or fitted.** A per-kg figure
   from one body size multiplied out to a very different one, or an equation fitted on one range of
   weights applied outside it, is a model assumption, not arithmetic: say so in the sentence, or
   bound the answer another way. (Added 24 Sep 2026: Book 1 scaled a 55 kg woman's 36 kcal/kg a day
   to 140 kg and reached the wrong verdict; every arithmetic and quote gate passed.)

## Consistency

5. **The record never does what it says cannot be done.** If the section refuses a claim (a rate
   from two points, energy matched from steady weight), no answer, analogy or exercise makes it.
6. **One number, one value, throughout a calculation.** Do not use 4186 in one line and 4184 in
   the next.
7. **One term for one thing, across sections.** Check `prose/GLOSSARY.md` and the earlier
   sections your record depends on before naming anything; do not rename what they named.
8. **Pointers are right.** "The last section" is the section immediately before this one in the
   outline. Any section you mention is in `concept_deps`.

## Teaching

9. **Derivations do not skip.** Every step a reader must take is on the page.
10. **Worked answers are recomputed in Python**, every line, and each answer answers the question
    that was asked, at the precision it asked for.
11. **Must-know points are about the reader's behaviour.** None has the section as its subject;
    a `boundary` point names a limit of the technique.
12. **§9 language** on weight and the people who have it.
13. **Bounds keep their direction.** Anything worked out from a ceiling ("up to") by taking 1 minus
    it is a floor, and a bound for a whole population is no bound for a subgroup. Say which it is
    in the sentence. Found in two sections of Part D by the compression pass (C24, C25).
14. **Every term is explained at or before its first use**, in prose, exercises and practice prompts
    alike, in this section or an earlier one. The compression pass found undefined terms in most
    sections of Parts D to F.

## Figures

15. **Every section has a figure or a `figure_note`** saying in one line why a figure would teach
     nothing the prose does not. A quantitative section's figure draws its worked relationship.
16. **Every figure is a `spec` in the record**, drawn by `python check/figures/draw.py --book <ID>`;
     none is drawn by hand and no number is typed into a script. Its data come from the record's own
     table where there is one.
17. **Every number the figure plots or prints is in the prose**, or under `derived` with the
     arithmetic that gives it; the caption and alt text count. Every line it draws is a `fit` that
     passes through the plotted points, and every total or ratio it shows is a `check` that holds.
     The build blocks on each of these, and on a PNG older than its spec.
18. **Look at the PNG.** Recompute what it shows in Python, and read it as a reader would: the
     same numbers and units as the text, bars from zero, no label over the data.

## Rendering

19. Exponents as `10^7`, logarithms as `log10`, no markup; no repository path (`sources/…`,
    `check/…`) anywhere a reader will see it, including `.bib` notes.
