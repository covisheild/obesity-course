# Draft notes · batch b5 · S47-R1-C12, C13, C14

Written 2026-10-02. Build: no blocking item and no warning for any of the three records
(`python check/build.py --check`, filtered to b5). Figures drawn with `check/figures/draw.py --book S47-R1`,
0 problems; each PNG looked at. 109 quotes checked by script: every one is inside a `[TEXT]` block of
its source file (none from a header or `[NOTE]` line).

## Records written

- `check/records/S47/S47-R1-C12.yml`: What a frame is (derivable). Textbook anchor `openstax_amgov_4e`
  §8.4 and chapter 8 Key Terms. Off-type, held and quoted: `koon_2016_framing` (Entman's four functions,
  "as reported by Koon et al."), `pib_2105618` (Dr Devi Shetty's guest message; the PM on agenda).
- `check/records/S47/S47-R1-C13.yml`: The frames obesity is argued in (empirical). `barry_2009_metaphors`,
  `koon_2016_framing`, `summan_2026_foodtax`.
- `check/records/S47/S47-R1-C14.yml`: The frame sets the menu (empirical). `barry_2009_metaphors`,
  `koon_2016_framing`, `pib_2105618`, `fssai_eat_right_india`, `pib_2163555`, `summan_2026_foodtax`.

None is quantitative, so no practice sets. Each has a retrieval exercise and at least one exercise with
`skill_ref: S47-R1-K02`.

## Reference kinds

- Koon 2016 is a scoping review; its own Table 1 contrasts scoping with systematic reviews, so it is
  labelled `primary`, not `systematic_review`. Conductor may prefer otherwise.
- PIB 2105618 (a speech) and the FSSAI page are labelled `primary`; PIB 2163555 is `instrument` as in
  earlier books. These are off-type supporting references on the empirical/derivable records.

## Unsourced, left out, or decided

- **Inventory frames not carried.** "Economic cost" and "protecting children" are not named as obesity
  frames by any held source, so they are not listed as frames. The frames table names only frames a held
  study names (Barry; Saguy and Riley, Kwan, Jenkin via Koon's Appendix).
- **Which frame dominates news or Indian texts**: no held source measures it. C13 says so plainly. Koon
  names three media-framing studies of obesity (Barry 2011, Gollust 2013, Niederdeppe 2014); none held.
- **Gollust 2013 experiment**: not held; C14 states only Barry's associations and Barry's own call for
  experiments.
- **Remedies per frame**: C13 gives cause and responsibility only; the remedy/menu is C14's, to avoid
  doing C14's job twice.
- **Barry copyright**: no table reproduced. Six support/endorsement figures and three R-squared values
  are quoted in prose; the C14 figure plots the three R-squared values the text itself states (not the
  Table 4 row). Conductor to confirm this is within "short quotation".
- **R-squared** is glossed as "the share of differences in support between respondents that the model
  accounted for, 0 none, 1 all", and the model is marked beyond this book.
- **Overton window** named only, not defined (no held source defines it).
- Dr Devi Shetty is introduced only as the PM introduces him ("a very distinguished doctor"). His
  sentence "Majority of the youngsters in India today are obese" (unsourced) is not used.
- §9: Barry's sinful-behaviour wording (with "disgust") is described, never quoted.
- The word "instrument" is used only in its Book 0 legal sense; for a tax, label or rule C14 says
  "measure" (see notes-for-others-b5.md).

## Practice-set sizes

Not applicable: C12, C13, C14 are not quantitative.

## Figures

- C12: `figure_note`. Wanted diagram (not drawable by the tool): one sentence split into four labelled
  parts, problem, cause, judgement, remedy, with arrows from the remedy to "who would have to act"; two
  versions side by side for Letter A and Letter B of the first illustration.
- C13: `s47-r1-c13-koon-issues.png` (Koon's 52 articles by health issue: obesity 3) and
  `s47-r1-c13-summan-interviews.png` (the 18 Indian interviews by group; government 3 is derived 1+1+1,
  `check: sum(y) = 18`).
- C14: `s47-r1-c14-model-share.png` (0.08, 0.11, 0.18; `check: 1 - y[2] = 0.82`).

## Glossary rows (proposed; not added)

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| agenda setting | choosing which issues get attention at all, before any frame is chosen | `S47-R1-C12` |
| episodic frame | telling an issue through one case or event and its details | `S47-R1-C12` |
| frame (of an account) | what an account chooses to keep in and leave out; usually it names a problem, a cause, a judgement and a remedy | `S47-R1-C12` |
| key informant interview | an interview with someone chosen because they know the policy area | `S47-R1-C13` |
| menu (of a frame) | the measures a frame makes easy to say | `S47-R1-C14` |
| priming | when what a reader meets first tilts how they judge what comes next | `S47-R1-C12` |
| R-squared | the share of the differences between people that a statistical model accounts for, from 0 (none) to 1 (all) | `S47-R1-C14` |
| scoping review | a broad review that maps what research exists on a question, without the strict rules and quality checks of a systematic review | `S47-R1-C13` |
| thematic frame | telling an issue through the broad view: the trend over time and what led to it | `S47-R1-C12` |

## Numbers keys proposed (literal values used meanwhile)

| Key | Value | Source | Sections |
| --- | --- | --- | --- |
| `edible_oil_cut_pct` | 10 | `pib_2105618` ("use 10% less oil every month") | C14; likely C15 |
| `barry_n` | 1,009 | `barry_2009_metaphors` | C13, C14; C15 if it uses Barry |
| `barry_toxic_env_important_pct` | 77.5 | `barry_2009_metaphors`, Table 2 | C13; C15 if used |
| `summan_kii_n` | 18 | `summan_2026_foodtax` | C13; C18 if it cites the interviews |

C14 uses the existing `{{n:gst_demerit_rate_pct}}`.
