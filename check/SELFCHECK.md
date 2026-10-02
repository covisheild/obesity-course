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

4b. **Every headline number says what it does not mean.** For each quantitative claim a reader
   might carry away, one sentence names its nearest overreach: an association read as an effect, a
   value used outside the range it was fitted or measured on, a result for one population read as
   true for another. (Added 28 Sep 2026 from the statistics book, whose analysis journeys end with
   "what the result does not mean"; the course's two outside-reader escapes, Book 1 C08 and Book 2
   C12, were both overreach.)

## Consistency

5. **The record never does what it says cannot be done.** If the section refuses a claim (a rate
   from two points, energy matched from steady weight), no answer, analogy or exercise makes it.
6. **One number, one value, throughout a calculation.** Do not use 4186 in one line and 4184 in
   the next.
6a. **A number reused across sections comes from the registry.** Write `{{n:key}}` and add the key to
   `books/<ID>/numbers.yml` (value, meaning, how it was obtained); another book's number is
   `{{n:S01-R1/key}}`. Never retype it. (28 Sep 2026: the statistics book printed r = 0.82 and
   R² = 0.62 for one regression, and one survey with 20 and with 25 households per village.)
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
14a. **Every symbol too.** A sign, Greek letter or mark (x̄, p̂, Σ, ≈, subscripts) is explained in words
    where it is first used, and has a row in `check/notation.yml` (the build warns otherwise; the
    PDF's *Symbols used in this book* page is built from it). Mathematics beyond the book's stated
    `prerequisites` is taught where it appears or marked "beyond this book".
14b. **Nothing depends on an optional part.** If a book ever adds a software, spreadsheet or tool box,
    it is labelled optional, no prose relies on its output (the number is stated in the text), and a
    question that needs the tool is marked optional.

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

## Words that never reach a reader

20. **No filler and no authoring vocabulary.** No "This completes…", no internal names for the
    book's structure, no "it can be shown" without the showing. The build blocks the phrases in
    `check/banned_phrases.yml`; add one when an audit finds the same filler twice.
21. **No version history in the book.** "What's new", change lists and requests about versions go to
    `books/<ID>/CHANGE-RECORD.md` for Harsh, never into `book.yml` text or a record (Harsh, 28 Sep 2026).
22. **"Recall" only points back.** A later section is named with a one-clause gloss, never recalled.
    The build blocks a recall of a later record id.

## Rendering

19. Exponents as `10^7`, logarithms as `log10`, no markup; no repository path (`sources/…`,
    `check/…`) anywhere a reader will see it, including `.bib` notes.
19a. **Code runs as printed.** Every ```` ```r ```` / ```` ```sh ```` block is fenced, every
    ```` ```output ```` block was written by `python check/code_gate.py --write`, never typed, and
    `python check/code_gate.py --check --subject <ID>` passes.
