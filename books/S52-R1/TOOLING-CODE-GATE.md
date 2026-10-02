# Code support and code gate (S52-R1, 2 Oct 2026)

A contract change. Harsh authorised it in the S52-R1 chat on 2 Oct 2026 ("Add code support + code
gate"), under the exception in `PARALLEL.md`. Every change is additive. Records without code
behave exactly as before, and T1 below shows that byte for byte. The S52-R1 conductor commits
this work and reconciles it with S58-R1, which is still in flight. Every file in the list below
is new or touched here.

## What changed, file by file

- **`check/codeblocks.py`** (new). The single parser for code fences, used by every tool:
  - Fences: ```` ```r ````, ```` ```output ```` and ```` ```sh ````.
  - Attributes: `norun`, `error` and `file=<rel/path>`.
  - Functions:
    - `blocks` and `segments` find the code blocks.
    - `strip` blanks code out of a field.
    - `outside` applies a function to everything except code.
    - `pairs` matches each code block with the output block under it, and finds orphans.
    - `unknown_tags` finds fence tags nothing renders.
    - `to_markdown`, `md_outside` and `md_strip` handle the pandoc fences in the assembled booklet.
  - Untagged fences and ```` ```working ````, ```` ```calc ```` and ```` ```table ```` fences are untouched.
- **`check/build.py`**
  - `_prose` works on segments. The notation layer and `_working` run on the prose only. Each
    code block goes to pandoc verbatim as ```` ```{.r} ````, ```` {.bash} ```` or ```` {.output} ````.
  - `_block` puts a label on its own line when the field opens with a code block.
  - A must-know point that holds code keeps its line breaks (`_code_item`).
  - `_notation` parks inline code that carries `^` or `~`. No such span exists in the current
    corpus, so this changes nothing for it.
  - `prose_fields` and `_paragraphs` strip code first. As a result, code is invisible to:
    sentence length, grade, hard words, the hyphen check, banned phrases, forward recall, ids,
    the symbol inventory and the plain-language report.
  - `check_arithmetic` strips code first.
  - The "working block has columns" scan recognises fences that carry attributes, and skips
    r, output and sh blocks.
  - `_ids_to_labels` and the acronym scan skip code.
  - `_caret_check` removes `<pre>` and `<code>` content before counting carets and tildes.
    Prose is checked as before.
  - `check()` ends with `code_gate.build_problems(recs)`, which reports **blocking** problems.
  - How the caret check is enforced: `_caret_check` is not blocking. It prints
    `[notation] …` lines during a render (`--subject`), and `--check` never runs it.
- **`check/reader_checks.py`.** `{{n:key}}` is **never substituted inside code**. It stays as
  typed, and the gate runs it as typed. Reason: code prints verbatim and its output comes from a
  fresh run, so a value pasted in from the registry could not match.
- **`check/notation.py`.** `inventory()` strips code blocks before its old fence regex runs.
- **`check/compress/prepare.py`**
  - A label goes on its own line when the text opens with a code fence.
  - A must-know point that holds code keeps its line breaks.
- **`check/compress/restore.py`.** A fence block is already restored whole. An output block
  now comes back exactly when the r or sh block above it does, and never on its own.
- **`check/compress/validate.py`**
  - New `code_problems` check:
    - A code block in a cut must match the original exactly, line for line.
    - An r or sh block and its output block are kept or cut together.
    - An orphaned output block fails.
  - The survival check compares code blocks exactly, not only after `norm()`.
  - Reports `code blocks N -> M`, each block counted as one unit. Sentences never come from code.
- **`check/pdf/style.css`**
  - New styles: `pre.sourceCode`, which is tinted in the book's hue (`--tint`, `--accent`), and
    `pre.output`, which is white with a faint rule.
  - Code is 8.3pt JetBrains Mono, with `pre-wrap`.
  - Ligatures are switched off. Without that, JetBrains Mono drew `<-` as an arrow and `==` as a
    bar. This was seen on the first page image.
  - A 72-character line fits on one line; tested in WeasyPrint, where 73 characters also fit.
- **`check/code_gate.py`** (new) and **`check/code/run_chunks.R`** (new). The gate itself. Its
  docstring gives the rules. In short:
  - **Sessions.** The prose fields form one session, in print order. Each exercise, practice
    problem and retrieval item is a fresh session.
  - Each session runs in a fresh `Rscript --no-init-file` process, using `evaluate` 0.23.
  - **Scratch project.** Built from `books/<ID>/code.yml`, plus a `.here` file at the root.
  - **Options and environment:**
    - `width = 72`
    - `cli.num_colors = 1`
    - `crayon.enabled = FALSE`
    - `pillar.bold = FALSE`
    - `tibble.width = 72`
    - `rlang_backtrace_on_error = "none"`
    - `LANG` and `LC_ALL` set to `C.UTF-8`, picked from `locale -a`
    - `TZ = UTC`
    - `NO_COLOR = 1`
    - `R_LIBS_USER` left unchanged
  - **sh blocks** run with `bash -c` in the project root, with stdout and stderr together.
    `R_PROFILE_USER` points the child `Rscript` at the same options.
  - **Modes:**
    - `--check`: exit 1 on any failure, with a unified diff.
    - `--write`: edits the raw YAML by line position. It finds the field with
      `yaml.compose`, keeps the literal-block indent and touches nothing else. It refuses unless
      the whole file parses back to the intended record. It backs up to
      `check/_build/code-gate-backup/`.
  - **Cache.** `check/_build/code-cache/`, which is git-ignored. The key covers:
    - the session's steps
    - `code.yml`
    - the hashes of the data files
    - the display root
    - the R and package-version fingerprint
    - the locale
    - the hashes of the gate's own source files
  - `--no-cache` forces a fresh run.
  - If Rscript is missing, every record with code gets a blocking "Rscript not found". Records
    without code get nothing.
- **The driver keeps the reader's global environment clean.** Fixed after the conductor's
  independent test on 2 Oct 2026. At first `run_chunks.R` defined its helpers in
  `globalenv()`, where the chunks also run. That made `library(readr)` print
  "masked _by_ '.GlobalEnv': write_file", and `ls()` would have listed the gate's own
  functions. Now the whole driver sits inside `local({...})`. `evaluate` and `jsonlite` are
  called only with `::`, so neither is attached.
- **`books/S52-R1/code.yml`** (new). Maps `penguins_raw.csv`, `BMX_L.xpt` and `DEMO_L.xpt`
  into `data-raw/`. The `files:` and `display_root:` form is also accepted.
- **Documentation:**
  - `claude.md` §1, after the ```` ```table ```` paragraph: "Code is fenced …". Also one sentence
    added to the blocking-checks list.
  - `PIPELINE.md`: Task 2 drafters run `--write`, then `--check`. Task 3 auditors run
    `--check --no-cache`.
  - `check/SELFCHECK.md`: new item 19a.

## Decisions on the console format

| Case | What the gate writes |
|---|---|
| Printed values, messages | As the console prints them |
| One warning | `Warning message:` then `In <call> : <msg>`, or the message alone when there is no call |
| Several warnings | `Warning messages:` then `1: In …` |
| More than 10 warnings | `There were N warnings …`, as R itself prints it |
| Base error | `Error in <call> : <msg>` or `Error: <msg>` |
| Error with pending warnings | The error, then `In addition: Warning message: …` |
| rlang/cli error (dplyr, readr) | `rlang::cnd_message(e, prefix = TRUE)`: identical to Rscript's text, without the backtrace |

- Warnings are printed after the top-level call that raised them, as the console does.
- R's 75-column line-break rule is reproduced. The constants are 14 for errors, 6 for one
  warning and 10 for several. They were checked against Rscript at the boundary
  (57 characters stay on one line, 58 break).
- evaluate 0.23 reports a top-level call as `eval(expr, envir, enclos)`. The gate treats that
  as no call, which matches the console.

## Remaining differences from a real console

1. The scratch root's path never reaches the page; it is shown as `~/project`. For example,
   `library(here)` prints `here() starts at ~/project`. A reader sees their own path.
2. In an interactive console, an rlang error also prints a line asking the reader to run
   `rlang::last_trace()`. Rscript prints a backtrace instead. The gate prints neither.
3. `Execution halted` is not printed. After an error the session continues to the next block,
   as a console does.
4. Text written with `cat(file = stderr())` is not captured in r blocks, because evaluate does
   not see it. It is captured in sh blocks.
5. Several expressions on one line (`a; b`) form one group, so their warnings print after the
   whole line.
6. In docx, code uses the reference document's own "Source Code" paragraph style and its
   "Verbatim Char" character style (Consolas 11pt). `check/references/reference.docx` was not
   changed, so a 72-character line may wrap in Word.
7. `check/figures/figspec.py` reads record text by itself. A number that appears only in code
   or output would still count as "stated in the text" for a figure spec. This is minor and was
   not changed.

## Tests

The fixtures stayed out of `check/records/`. They were kept in the session's scratch folder:

- `make_fixture.py` builds an S52-R1-C01 record from a copy of S55-R1-C01 with code added.
- `run_build.py` runs `build.main()` with `build.RECORDS` pointed at a scratch copy of
  `check/records` plus the fixture.
- The rendered S52-R1 fixture outputs were deleted from `check/_build/` afterwards.

### T0, before any edit

`python check/build.py --check` printed
`records 126 | clusters 9 | blocking 0 | warnings 214`.

`python check/build.py --subject S55-R1` made the md, html, docx and pdf. Copies were kept,
along with `check_report.md` and the CSV/JSON reports.

### T1, after all edits

The same `--check` line printed: **`records 126 | clusters 9 | blocking 0 | warnings 214`**.

Compared with T0:

- `check_report.md`, `numbers_register.csv`, `review_due.csv` and `retrieval_items.json`:
  byte-identical.
- `S55-R1.md` and `S55-R1.html`: byte-identical.
- `S55-R1.docx`: only `docProps/core.xml` differs, and only in its timestamps.
- PDF: text identical (pdftotext).
- `S55-R1-print.html`: differs only by the new CSS rules, which it embeds. It contains no `<pre>`.
- Render log: identical.

### T2, rendering the fixture

`run_build.py <fixture> --check` gave `blocking 0`. It reported no sentence, symbol,
arithmetic or table warning about code. `run_build.py <fixture> --subject S52-R1` then gave:

- **HTML:** code in `<pre class="sourceCode r">` and output in `<pre class="output">`, verbatim:
  `^`, `~`, `%in%`, `<-`, `|>`, `#` comments, two-space indent and `{{n:not_a_key}}`. No
  `[notation]` line was printed.
- **docx:** 24 paragraphs in style `SourceCode`.
- **PDF:** page images 10 and 11 show monospace text, with literal `<-` and `==` once the
  ligature fix was in.

### T3, the gate

| Case | Result |
|---|---|
| `--write` | Filled 11 output blocks |
| `--check` | Passes |
| One output line edited | `--check` fails with a diff |
| Warning without a call; warning with a call; base errors marked `error` | Correct text |
| rlang error | Correct text |
| tibble print | Correct |
| `norun` | Never runs |
| `file=code/analysis.R` then `Rscript code/analysis.R` | `rows: 344` |
| `here::here("data-raw", "penguins_raw.csv")` | `[1] 344` |
| Exercise session | Fresh: `exists("height")` gives `[1] FALSE` |
| Timing | `--no-cache` 1.6s; cached 0.3s |

**Regression test for the global environment.** A third fixture runs these lines as separate
blocks, and the same lines were also run through a plain Rscript with the same options and
environment:

- `ls()`
- `search()`
- `library(readr)`
- `library(dplyr)`
- `library(ggplot2)`
- `search()` and `ls()` together

The gate's results:

- `ls()` printed `character(0)`, before the library calls and after them.
- `search()` matched plain Rscript, before the library calls and after them.
- `readr` printed nothing; the masking message is gone.
- `dplyr` printed its normal masking message, the same as Rscript.

Compared with the plain Rscript run, the output was identical apart from trailing whitespace
and blank lines at the end of a block, which the gate normalises by design.

After the fix:

- The T3 fixture rerun with `--no-cache` passes, with all 11 outputs unchanged.
- The edited-line test still fails with a diff.
- The negative fixture still reports its 9 failures.
- T1 still prints `records 126 | clusters 9 | blocking 0 | warnings 214`.

A second fixture covered the negative cases:

- an orphan output block
- a `norun` block with an output block (`--write` removes it)
- an unmarked error
- a block marked `error` that does not error
- a silent block with a stale output block (`--write` removes it)
- an unknown attribute

Each was caught. Spot checks against Rscript under the same options matched apart from
trailing spaces: several warnings, a long error that breaks the line, error plus "In addition",
and a dplyr warning.

### T4, the compression tools

Run with `prepare.py extract`, `validate.py` and `restore.py`, all with `--records` and `--out`
pointed at scratch.

| Cut | Result |
|---|---|
| Deletes a sentence, keeps the code | OK |
| Removes an r block and its output whole | OK (`code blocks 22 -> 20`) |
| Alters a line inside a block | FAIL |
| Deletes a line inside a block | FAIL |
| Keeps the r block, drops its output | FAIL |

Restoring by naming words inside the removed block brought back the block and its output. The
field is then identical to the original, and validate's survival check passes.

The S52-R1 records do not exist yet, so nothing was run on real book content. The gate reports
`0 record(s) with code`.
