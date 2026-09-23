# Source gate · Book 0 Part D (D1–D7)

Checked against `sources/` on 2026-09-23 by the Part D chat. The rule in `claude.md`: a book only
enters the pipeline when its source pack is complete, and a line saying **no** stops the pipeline.

**Every line says yes.** All seven sections are `derivable`, so none of them needs an instrument
before it can be written. What they do need is an anchor that can actually be quoted against — and
for the first time in Book 0 there is one. Parts A to C cite OpenStax books whose table of contents
was opened and whose passages were not, so every definition there carries `claim_located: false`.
Part D's anchor is held as text in `sources/`, so the build can check each quoted sentence.

## The gate

| Needed for | Source | Kind | In `sources/`? | Obtained |
| --- | --- | --- | --- | --- |
| D1–D7 definitions — the textbook anchor | OpenStax *Introductory Statistics 2e* (Illowsky and Dean, 2023; web version updated 7 Jul 2026), sections 1.1, 1.2, 2.3, 2.5, 2.7, 3.1–3.4, 7.1 | textbook | `openstax_intro_stats_2e.txt` | **yes** |
| D7 vocabulary — what *error*, *systematic error*, *random error*, *accuracy*, *trueness*, *precision*, *resolution*, *zero error* mean | JCGM 200:2012, International vocabulary of metrology (VIM3), online edition updated 29 Apr 2017, entries 2.11, 2.13–2.21, 2.53, 4.14, 4.28 | instrument (vocabulary) | `jcgm_vim3.txt` | **yes** |
| D3–D7 real material — a two-way screening table, a mean against a median, a real sample, real measuring instruments | Kiran R, Harshitha, Bhargava M. *Heliyon* 2022;8:e12173, doi:10.1016/j.heliyon.2022.e12173 (PMC9791811), full text with tables | primary | `kiran_2022_muac_nc.txt` | **yes** |
| D1, D2 real material — a coverage ceiling stated as a percentage of a population, and eligibility decided per household | National Food Security Act 2013, s.3(1) and s.3(2) | instrument | `nfsa_2013.txt` | **yes** (already held) |

## How they were obtained, since the route matters to the next chat

Direct downloads from the sandbox fail at the proxy for all three hosts (openstax.org,
jcgm.bipm.org, ebi.ac.uk). The TinyFish `fetch_content` tool reaches all three and returns the page
text whole, with no summarising model in between — which is what makes the copy quotable. WebFetch
does summarise, and was used for one line only: VIM 2.16's one-line definition, which TinyFish's
extractor dropped. That line was asked for verbatim and is short enough to check by eye.

PubMed Central's own HTML page returned empty; the Europe PMC full-text service
(`/europepmc/webservices/rest/PMC<id>/fullTextXML`) returned the paper *with its tables*, which the
PubMed tool's full-text call does not. **That is the route for any open-access paper a later Part
needs**, and it removes most of what `PIPELINE.md` says a session cannot obtain.

## What the anchor does not cover, and where Part D stops because of it

- The normal distribution, confidence intervals and p-values. Section 7.1 is held only for its one
  plain sentence on the square-root law. Everything built on the normal curve belongs to S03.
- Formal probability notation beyond P(A), P(A and B) and P(A | B), each named once.
- Bayes' theorem as a formula. D3 does the reversal with a table and names it; S03 rung 1 owns the
  formula.
