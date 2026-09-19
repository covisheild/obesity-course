# Obesity expertise course

A curriculum built from first principles for one reader: 61 subjects across 18 parts, 195 rungs,
on a 43-section ground floor called Book 0. One concept record per teachable concept; records
assemble into booklets.

**The one rule everything else rests on:** a claim without an opened source is not written down as
a fact.

## Where to start

| Read this | For |
| --- | --- |
| `claude.md` | the contract — how prose is written and what a record must contain. Read in full, always. |
| `PIPELINE.md` | the six steps that take a subject from nothing to released |
| `PARALLEL.md` | how to work in more than one chat without the corpus drifting apart |
| `done/` | the four finished Book 0 sections. They are the standard. |
| `prose/GLOSSARY.md` | terms of art and the plain words they get at first use |

## Layout

```
claude.md              the contract: style sheet + specification
PIPELINE.md            the six pipeline steps, with the prompt for each
PARALLEL.md            working in more than one chat at once
map/                   the frozen subject map — 61 subjects, 195 rungs
check/                 build.py, schema, hard-word list, Book 0 outline
done/                  finished Book 0 concept records
books/<SUBJECT>/       per-subject working directory, one chat at a time
sources/               opened primary sources; append-only
prose/GLOSSARY.md      cross-booklet terminology
plan/                  pilot inventories and verification notes
```

## Build

```bash
python check/build.py --check          # schema, citations, plain-language checks
python check/build.py --subject B0     # assemble a booklet to _build/
```

`check/_build/` is generated and not committed.

## Status

Book 0: 4 of 43 sections written, 1 of those with its source opened and clause-located.
Subjects: 0 of 195 rungs. The binding constraint is not drafting — it is retrieval. Three FSSAI
and Gazette instruments that S48 needs cannot be reached from a sandbox and can be reached from a
browser.
