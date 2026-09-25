# Cutter brief · S55-R1 (Task 5, step 5a)

Repository `/home/claude/obesity-course`. Do not commit, push, or edit any record or any file not
named here. Read `claude.md` §11, §11a and §12. Read `books/S55-R1/compress/<SECTION>-original.md`
(the section as the reader meets it) and `books/S55-R1/compress/<SECTION>-prose.yml` (the prose
fields, which are all you may touch).

Write a deliberately aggressive compression of that section to
`books/S55-R1/compress/<SECTION>-pass1-prose.yml` (same fields, same YAML shape as `-prose.yml`).
Aim at roughly half the reader-facing word count. A later step will test your output with a cold
reader and restore whatever turns out to be load-bearing, so cut hard and let the test catch your
mistakes. Do not be cautious.

Remove words by deleting whole sentences and whole paragraphs. Never fuse two sentences into one.
Never push a second idea into a sentence that had one. Never edit a kept sentence. Keep every
heading in order even where almost nothing survives under it. Keep the second person and the
physical instructions. Add nothing. The exercises and practice problems are not in the prose file
and stay word for word.

Then run `python check/compress/validate.py --subject S55-R1 <SECTION>-pass1-prose.yml` until it
passes (deletion only, sentences verbatim, mean and longest sentence not risen — if it fails, fix
your cut, never the tool), and `python check/compress/prepare.py --subject S55-R1 assemble <SECTION>`.

Append to `books/S55-R1/compress/LEAST-SURE-<SECTION>.md` the one cut you were least sure about
(under eighty words). Return at most 60 words: words before → after, validate result.

**Batches:** you may be given two or three sections; do each in turn exactly as above, with its own
LEAST-SURE file. Scratch files go in `/home/claude/scratch-cut-<your batch>/`, never a shared name.
