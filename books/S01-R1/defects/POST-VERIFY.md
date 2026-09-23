# S01-R1 post-verify check (git diff 12d8bd4 HEAD -- check/records/S01)

Book rebuilt with `python check/build.py --subject S01-R1` (blocking 0) and read in `check/_build/S01-R1.md`.

## Findings

1. **C04 Definition, REE and BMR (build ~l.468-470).** The old text said BMR is REE measured fasting, at rest, in a neutral temperature. That link is now gone. The new text gives REE and BMR as two separate definitions under "three components", and never says how they relate. A reader cannot tell whether BMR is a fourth component, another name for REE, or REE under set conditions. The facts are right: C03's FAO glossary quote and C04's OpenStax quote both give fasting, rest and thermoneutrality. "Also measured in a neutral temperature" also reads awkwardly. Suggested wording: "BMR, from section 3, is REE measured lying down after a fast, in a neutral temperature."
2. **C02 Definition, "The static rule, named in full in section 7" (build l.119-120).** "Named in full" is unclear. Section 7 defines the rule and does not give it a longer name. "defined in section 7" would say it plainly.
3. **C02's new `nist_sp811_pound` citation (reference 10, build l.1403).** The record's `resolved_id` and locator point to the NIST Footnotes page, and that page does hold the quoted exact factor. But the library.bib URL for this key points to the Appendix B.8 page. That page shows only the rounded 4.535 924 E-01. A reader who follows the printed link will not find the exact 0.453 592 37 figure without going on to the Footnotes page. C07 shares this bib entry, so the problem is older than this diff, but the new C02 citation inherits it. Fix: point the URL at `.../nist-guide-si-footnotes` (or print both URLs).

## Checked and found sound

- Pound: "exactly 0.453 592 37 kilogram" matches sources/nist_sp811_pound.txt block 2, "The exact conversion factor is 4.535 923 7 E-01", and the record's quote is verbatim in that file. 3500 / 0.45359237 = 7716.179..., so section 7's 7,716.18 and "about 7,716" are right. The later sums that use 7,716.18 are unchanged. Section 2's "about 7,700 a kilogram (section 7 works that out)" agrees with this.
- C02's 3,500 kcal a pound is backed by the existing hall_2008_ijo quote ("a cumulative energy deficit of 3500 kcal is required to lose 1 pound of body weight"). The "can be traced back ... 87% fat." quote is in sources/hall_2008_ijo.txt block 3. Its subject there is "The origin of this rule", and the book's paraphrase "the rule can be traced back" was worded that way before this diff too. The new deficit and surplus definition agrees with section 7's wording.
- "classic rule" to "static rule": the swap is complete in reader-facing text. "classic" is left only in two reference locators in C02 (l.113, 144), which are not reader prose.
- "metabolisable" to "metabolizable" in C05: the swap is complete.
- C08: `B0-R0-C36` is Book 0 E6, which defines glycogen, so dropping "a form of carbohydrate" / "starch-like fuel" is safe. The caption's "US Federal Trade Commission (FTC)" matches the body's expansion.
- C10: "rise in intake of about 100 kcal a day per kg lost" matches C09 (l.1247, 1278).
- C01: "lean body mass, or lean mass" is fine as a note on usage. Strictly, DXA "lean mass" leaves out bone mineral, but the book uses the terms loosely and says so. Moving the REE gloss ahead of the quote reads acceptably.

## Conductor, 23 Sep 2026

1. Closed: C04 now says BMR is not a fourth part but resting expenditure measured under set conditions.
2. Closed: "named in full in" -> "defined in".
3. Closed: library.bib nist_sp811_pound url now points at the Footnotes page that prints the exact factor.
