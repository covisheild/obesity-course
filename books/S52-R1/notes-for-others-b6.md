# Notes for other batches and the conductor, from b6 (C16-C18)

Nothing in another batch's record was edited. `books/S52-R1/numbers.yml` gained one key, `demo_rows`
(11933, DEMO_L rows), placed after `bmx_cols`.

| Section | What | Why |
| --- | --- | --- |
| C09 (b3) | C09 practice level 6 prints "11933 rows" of DEMO_L in prose. The key `demo_rows` now exists. | Switch the prose number to `{{n:demo_rows}}` (SELFCHECK 6a). |
| C13 (b5) | C16 teaches `n()` against `sum(!is.na(x))` beside a mean, and that `na.rm = TRUE` leaves values out silently. It points back to "the section on missing values" for counting and reporting them. | If C13 already teaches the `n()` vs values-used distinction, the reconcile step can shorten C16's first illustration. |
| C14 (b5) | C16 calls `count()` "met in the section on categories" and shows it equals `group_by()` + `summarise(n = n())` and returns an ungrouped result. | C14 should introduce `count()` (it does, from a grep); keep the name "section on categories" or tell me the title to use. |
| C19 (b7) | C17 illustration 2 finds a duplicated key (patient 102) with `count(id) |> filter(n > 1)` and says the duplicate "is removed by a line of code, with a comment saying why, which a later section of this book teaches". C17 also uses `relationship = "one-to-one"` / `"many-to-one"` as a stopping check on joins. | C19 discharges the dedup promise; it may also mention `relationship` as a check that stops the script. |
| C19, C22 (b7, b8) | C17 joins BMX_L to DEMO_L with `left_join(..., by = "SEQN", relationship = "one-to-one")`, keeps 8860 rows, and shows the 3073 DEMO_L-only rows all have RIDSTATR 1. Adults 20+ by RIAGENDR: 2720 men / 3344 women; BMI present 2680 / 3290; mean 29.3 / 30.3; median 28.1 / 28.7 kg/m^2 (unweighted). | Reuse the same join line and numbers; if any of these four BMI figures is printed in prose again, register keys. |
| C21, C22 (b8) | C16-C18 write outputs with `dir.create(here::here("output"), showWarnings = FALSE)` before `write_csv()` / `ggsave()`, because the gate's scratch project has no `output/`. C18 links this to ggplot2 3.5.0 (`ggsave()` no longer makes folders). Files written: `output/mass_by_species.csv`, `output/mass_histogram_counts.csv`, `output/mass_flipper.png` (and practice files). | C22's script can use the same idiom and file names. |
| C21 (b8) | C18 says a histogram left on default bins can redraw differently on ggplot2 4.x (quoting the 4.0.0 news). | A natural example for C21's "package versions change outputs" point. |
| conductor | Plots print no text, so the gate checks C18's plotting code only through warnings ("Removed 2 rows ...") and companion `count()`/`summarise()` output. A broken plot that errors is still caught. | Known limit of the gate for a plotting section; the auditor may want to render C18's plots once. |
