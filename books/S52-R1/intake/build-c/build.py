"""S52-R1 intake, group c: build the sources/*.txt files from the raw renders and fetches.

Every [TEXT] block is raw[i:j] of one file in books/S52-R1/intake/raw/, cut by literal anchors.
Header quotes are cut the same way. The manifest (manifest.json) records file, locator and offsets
for verify.py. Run: python3 /home/claude/work/obesity-course/books/S52-R1/intake/build-c/build.py
"""
import json, os, re

ROOT = '/home/claude/work/obesity-course'
RAW = os.path.join(ROOT, 'books/S52-R1/intake/raw')
SRC = os.path.join(ROOT, 'sources')
HERE = os.path.dirname(os.path.abspath(__file__))
DATE = '2026-10-02'
BAR = '=' * 79
MANIFEST = []


def raw(name):
    with open(os.path.join(RAW, name), encoding='utf-8') as fh:
        return fh.read()


def find1(s, a, start=0):
    i = s.find(a, start)
    if i < 0:
        raise SystemExit(f'anchor not found: {a!r}')
    return i


def cut(name, start=None, end=None, start_at=0, include_end=False):
    """raw[i:j]: i at the start anchor (or 0), j at the end anchor (exclusive) or end of file."""
    s = raw(name)
    i = find1(s, start, start_at) if start else 0
    if end is None:
        j = len(s)
    else:
        j = find1(s, end, i + 1)
        if include_end:
            j += len(end)
    return s, i, j


def bullet(name, phrase, marker='\n* ', start_at=0):
    """The whole markdown bullet (top-level '* ' or nested '  + ') that contains phrase."""
    s = raw(name)
    p = find1(s, phrase, start_at)
    i = s.rfind(marker, 0, p) + 1
    ends = [k for k in (s.find('\n* ', p), s.find('\n#', p), s.find(marker, p)) if k > 0]
    j = min(ends)
    return s, i, j


def line(name, prefix):
    s = raw(name)
    i = find1(s, prefix)
    j = s.find('\n', i)
    return s, i, j


def hq(key, name, sij):
    s, i, j = sij
    MANIFEST.append(['HEADER', key, name, None, i, j])
    return s[i:j].rstrip('\n')


class Pack:
    def __init__(self, key):
        self.key, self.parts, self.n = key, [], 0

    def block(self, title, locator, name, sij, note_after=None):
        s, i, j = sij
        text = s[i:j].strip('\n')
        self.n += 1
        MANIFEST.append(['BLOCK', self.key, name, locator, i, j])
        self.parts.append(f'{BAR}\n{self.n}. {title}\n{locator}\n{BAR}\n\n[TEXT]\n{text}\n[END TEXT]\n')
        if note_after:
            self.parts.append(f'[...]\n[NOTE] {note_after}\n')

    def write(self, header):
        path = os.path.join(SRC, self.key + '.txt')
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(header.rstrip('\n') + '\n\n' + '\n'.join(self.parts))
        return path


RULE_LOCAL = """Transcription rule for this file: every line between a [TEXT] and an [END TEXT] line is an exact,
unaltered slice of a raw render made in the book's sandbox and saved under books/S52-R1/intake/raw/, cut
programmatically (raw[i:j]) by books/S52-R1/intake/build-c/build.py and re-checked by verify.py as a
whitespace-normalised substring of that render. Nothing has been paraphrased. Where material is left out,
the omission is marked [...] in place. Lines beginning [NOTE] are this file's own annotation and are NOT
source text. Quoted evidence in this header is cut the same way.

LOCATORS: these are local documents, not web pages, so each block heading carries a locator, not a URL:
  rhelp://<package>@<version>/<Rd name>     the installed help page (what ?topic shows in R)
  rvignette://<package>@<version>/<name>    the installed vignette (what vignette("<name>") shows)
  rfile://<package>@<version>/DESCRIPTION   the installed DESCRIPTION file, byte for byte
The package's website shows the CURRENT version's documentation, which may differ from what is held here.

HOW RENDERED (2026-10-02): R 4.3.3, in a UTF-8 locale, with options(useFancyQuotes = FALSE) so quotation
marks print as straight ASCII ' and "; help pages by tools::Rd2txt(utils:::.getHelpFile(help(topic,
package = pkg)), options = list(underline_titles = FALSE, width = 80)); vignettes from the installed HTML
by xml2 1.3.6, taking h1-h4, p, pre, top-level li and table elements in document order (headings marked
with #, list items with -, code and printed output as in the vignette's own <pre> blocks; images not
held). Script: books/S52-R1/intake/build-c/render.R. Help pages print no output for their Examples: the
code there is shown, not run."""

VIGNETTE_NOTE = 'Vignette text continues in the installed vignette; sections not needed by S52-R1 are not held.'


def rdocs():
    meta = json.load(open(os.path.join(HERE, 'pkgmeta.json'), encoding='utf-8'))
    tmap = {}
    for row in raw('rdocs_s52r1-topic-map.csv').splitlines()[1:]:
        p, t, rd, rf = [x.strip('"') for x in row.split(',')]
        tmap.setdefault(p, []).append((t, rd, rf))
    extras = {('base', 'round'), ('base', 'library'), ('utils', 'packageVersion'),
              ('utils', 'install.packages'), ('stats', 'median'), ('stats', 'sd'), ('stats', 'quantile'),
              ('stats', 'IQR'), ('dplyr', 'across'), ('dplyr', 'n_distinct'), ('dplyr', 'rename'),
              ('dplyr', 'desc'), ('dplyr', 'n')}
    vign = {
        'dplyr': [('dplyr', '# Introduction to dplyr', '## Patterns of operations',
                   'Introduction to dplyr: the introduction, "Data: starwars", "Single table verbs" (the pipe; filter, arrange, slice, select, mutate, relocate, summarise; commonalities) and "Combining functions with %>%", whole',
                   'Omitted: the vignette\'s closing section "Patterns of operations" (selecting and mutating operations).'),
                  ('two-table', '# Two-table verbs', '## Set operations',
                   'Two-table verbs: the introduction, "Mutating joins" (how tables are matched, types of join, observations) and "Filtering joins", whole',
                   'Omitted: "Set operations" and "Multiple-table verbs".')],
        'tidyr': [('tidy-data', '# Tidy data', '## Tidying messy datasets',
                   'Tidy data: the introduction, "Data tidying" and "Defining tidy data" (data structure, data semantics, the three rules), whole',
                   None),
                  ('tidy-data', '## Tidying messy datasets', '### Variables are stored in both rows and columns',
                   'Tidy data: "Tidying messy datasets" with its first two cases, "Column headers are values, not variable names" and "Multiple variables stored in one column", whole',
                   'Omitted: the cases "Variables are stored in both rows and columns", "Multiple types in one table", "One type in multiple tables".'),
                  ('pivot', '# Pivoting', '### Numeric data in column names',
                   'Pivoting: "Introduction", "Longer" and its first case "String data in column names", whole',
                   'Omitted: the remaining pivot_longer() cases (numeric data and many variables in column names, multiple observations per row).'),
                  ('pivot', '## Wider', '### Aggregation',
                   'Pivoting: "Wider" and its first case "Capture-recapture data", whole',
                   'Omitted: the rest of the vignette (aggregation, names from several variables, tidy census, implicit missing values, unused columns, contact list, longer-then-wider, manual specs).')],
        'readr': [('readr', '# Introduction to readr', None,
                   'Introduction to readr: whole (vector parsers, column specification, rectangular parsers, overriding the defaults, available column specifications, output)', None)],
        'forcats': [('forcats', '# Introduction to forcats', None,
                     'Introduction to forcats: whole (ordering by frequency, NAs in levels and values, combining levels, ordering by another variable, manual reordering)', None)],
    }
    titles = {'base': 'The R Base Package', 'utils': 'The R Utils Package', 'stats': 'The R Stats Package'}
    vers_raw = 'rdocs_s52r1-versions.txt'
    out = {}
    for p in ['base', 'utils', 'stats', 'dplyr', 'tidyr', 'readr', 'readxl', 'haven', 'ggplot2', 'forcats',
              'lubridate', 'stringr', 'here']:
        key = f'rdocs_s52r1_{p}'
        pk = Pack(key)
        desc = f'rdocs_s52r1_{p}-DESCRIPTION.txt'
        ver_line = hq(key, vers_raw, line(vers_raw, f'{p} '))
        version = ver_line.split()[1]
        lic_line = hq(key, desc, line(desc, 'License:'))
        title_line = hq(key, desc, line(desc, 'Title:'))
        order = {}
        for t, rd, rf in tmap[p]:
            order.setdefault((rd, rf), []).append(t)
        held = [(ts, rd, rf) for (rd, rf), ts in order.items()]
        for ts, rd, rf in held:
            tag = ', '.join(f'{p}::{x}' + (' [extra]' if (p, x) in extras else '') for x in ts)
            pk.block(f'{tag} — help page "{rd}" ({p} {version}), whole', f'rhelp://{p}@{version}/{rd}', rf, cut(rf))
        for v, a, b, title, note in vign.get(p, []):
            rf = f'rdocs_s52r1_{p}-vignette-{v}.txt'
            pk.block(f'vignette("{v}", package = "{p}") {version} — {title}', f'rvignette://{p}@{version}/{v}', rf,
                     cut(rf, a, b), note_after=note)
        pk.block(f'DESCRIPTION file of {p} {version}, whole (title, authors, licence, version, publication date)',
                 f'rfile://{p}@{version}/DESCRIPTION', desc, cut(desc))
        if p in meta:
            m = meta[p]
            aut = m['aut'] if isinstance(m['aut'], list) else [m['aut']]
            cit = (f"{'; '.join(aut)}. {p}: {m['title']}. R package version {version}, published on CRAN "
                   f"{m['date'][:10]}. Help pages as installed.")
            lic = (f'LICENCE: the installed DESCRIPTION file states\n  "{lic_line}"\n'
                   f'The LICENSE file it names is not present in the installed package (system.file("LICENSE",\n'
                   f'package = "{p}") returns ""), so its year and copyright-holder lines were not read.')
            if p == 'lubridate':
                lic = f'LICENCE: the installed DESCRIPTION file states\n  "{lic_line}"\n(GNU General Public License, version 2 or later).'
            web = m['url'].split(',')[0].strip()
        else:
            cit = f'R Core Team. {titles[p]}, part of R 4.3.3 (2024-02-29). Help pages as installed.'
            gpl = hq(key, vers_raw, cut(vers_raw, 'R is free software', 'GNU General Public License versions 2 or 3.', include_end=True))
            lic = (f'LICENCE: the installed DESCRIPTION file states\n  "{lic_line}"\nand R itself, asked with R --version, states:\n'
                   + '\n'.join('  ' + x for x in gpl.splitlines()))
            web = 'none (base R documentation ships with R itself; R-project.org hosts the current release only)'
        topics_held = '; '.join(f"{', '.join(ts)} (Rd \"{rd}\")" for ts, rd, rf in held)
        vheld = ''.join(f'\n  - vignette "{v}": {title}' for v, a, b, title, note in vign.get(p, []))
        xnote = (" Pages marked [extra] were not in the intake brief's list and were added because S52-R1's\ninventory uses them (C05, C06, C11-C13, C16, C19)." if any((p, x) in extras for ts, _, _ in held for x in ts) else '')
        lnote = ("\n[NOTE] lubridate's vignette is not held: the installed package has no rendered vignette (vignette(\"lubridate\")\nfinds no HTML)." if p == 'lubridate' else '')
        header = f"""{p.upper()} {version} — VERSION-MATCHED HELP PAGES FROM THE BOOK'S R 4.3.3 SANDBOX
VERBATIM SOURCE PACK (EXCERPTS)
============================================================

{RULE_LOCAL}

CITATION: {cit}
PACKAGE TITLE (from DESCRIPTION): "{title_line}"
VERSION read with packageVersion() on {DATE}: "{ver_line}"
{lic}

WHAT THIS FILE HOLDS: these help pages, each whole (description, usage, arguments, details, value, examples
as code): {topics_held}.{(' Vignette sections, each whole as marked:' + vheld) if vheld else ''}
The DESCRIPTION file, whole.{xnote} Every other help page and vignette of the package is NOT held.{lnote}

VERSION WARNING: this is the documentation of the version the book's outputs were made with. Newer versions
exist (see `tidyverse_news_s52r1` for what changed in dplyr, tidyr, readr and ggplot2). A reader on a newer
version may see different text in ?topic. Current online reference (orientation only, not this text): {web}
"""
        out[key] = (pk.write(header), pk.n, [ts for ts, _, _ in held])
    return out


def news():
    key = 'tidyverse_news_s52r1'
    pk = Pack(key)
    U = {p: f'https://{p}.tidyverse.org/news/' for p in ['ggplot2', 'dplyr', 'readr', 'tidyr']}
    R = {p: f'tidyverse_news_s52r1-{p}.txt' for p in U}
    g, d, r, t = R['ggplot2'], R['dplyr'], R['readr'], R['tidyr']
    pk.block('ggplot2 4.0.3, whole entry (geom_boxplot() gains quantile.type, default 7)', U['ggplot2'], g,
             cut(g, '## ggplot2 4.0.3', '## ggplot2 4.0.2'),
             note_after='Omitted: ggplot2 4.0.2 (one internal change) and all of 4.0.1 except the bullet below.')
    pk.block('ggplot2 4.0.1 (CRAN release 2025-11-14), bug fix: stat_bin(boundary) was ignored', U['ggplot2'], g,
             bullet(g, 'was ignored (#6682)'),
             note_after='Omitted: the other 4.0.1 bug fixes and improvements.')
    pk.block('ggplot2 4.0.0 (CRAN release 2025-09-11): heading, "Breaking changes" and "Lifecycle changes", whole', U['ggplot2'], g,
             cut(g, '## ggplot2 4.0.0', '#### Improvements'),
             note_after='Omitted: the 4.0.0 "Improvements" (themes, scales, coords, layers, other), bug fixes and developer-facing changes, except the bullet below.')
    pk.block("ggplot2 4.0.0, Improvements > Other: a variable's label attribute used as default label", U['ggplot2'], g,
             bullet(g, 'An attempt is made to use a variable'),
             note_after='Omitted: everything else in 4.0.0 and all of 3.5.2 (infrastructure for extension packages) and 3.5.1 (regression fixes).')
    pk.block('ggplot2 3.5.0 (CRAN release 2024-02-23): heading, summary and "Breaking changes", whole', U['ggplot2'], g,
             cut(g, '## ggplot2 3.5.0', '### New features'),
             note_after='Omitted: 3.5.0 "New features" (guide system, coord_radial, patterns) and most improvements and bug fixes, except the three bullets below.')
    pk.block('ggplot2 3.5.0, Improvements: geom_boxplot() gains an outliers argument', U['ggplot2'], g,
             bullet(g, 'argument to switch outliers on or off'))
    pk.block('ggplot2 3.5.0, Improvements: facet_grid()/facet_wrap() gain an axes argument', U['ggplot2'], g,
             bullet(g, 'controls the display of axes at interior panel positions'))
    pk.block('ggplot2 3.5.0, Bug fixes: ggsave() and directory creation (new create.dir argument)', U['ggplot2'], g,
             bullet(g, 'no longer sometimes creates new directories'),
             note_after='Omitted: the rest of 3.5.0. Entries for 3.4.4 and earlier (the installed version and before) are not held.')
    pk.block('dplyr 1.2.0 (CRAN release 2026-02-03): heading and the first new feature, filter_out()', U['dplyr'], d,
             cut(d, '## dplyr 1.2.0', '* New\n\n  ```\n  when_any()'),
             note_after='Omitted: when_any()/when_all().')
    pk.block('dplyr 1.2.0, New features: case_when() becomes one of a family of four (replace_when(), recode_values(), replace_values())', U['dplyr'], d,
             bullet(d, 'is now part of a family of 4 related functions'))
    pk.block('dplyr 1.2.0, New features: case_when() gains .unmatched', U['dplyr'], d,
             bullet(d, 'rather than providing a'),
             note_after='Omitted: speed of if_else()/case_when()/coalesce(), between(ptype), rbind() for rowwise_df.')
    pk.block('dplyr 1.2.0, "Lifecycle changes": "Newly stable" and "Newly deprecated", whole', U['dplyr'], d,
             cut(d, '### Lifecycle changes', '#### Other deprecation advancements'),
             note_after='Omitted: the list of long-deprecated functions now defunct, warning or removed, except the item below (none of the others is in the book\'s function list).')
    pk.block('dplyr 1.2.0, now defunct: returning more or less than 1 row per group in summarise()', U['dplyr'], d,
             bullet(d, 'Returning more or less than 1 row per group', marker='\n  + '),
             note_after='Omitted: other defunct, warning and removed items; minor improvements except the three below.')
    pk.block('dplyr 1.2.0, Minor improvements: base pipe in the documentation', U['dplyr'], d,
             bullet(d, 'The base pipe is now used throughout the documentation (#7711)'))
    pk.block('dplyr 1.2.0, Minor improvements: the .groups message from summarise()', U['dplyr'], d,
             bullet(d, 'message emitted by'))
    pk.block('dplyr 1.2.0, Minor improvements: R >= 4.1.0 required', U['dplyr'], d,
             bullet(d, 'R >=4.1.0 is now required, in line with the tidyverse standard of supporting the previous 5 minor releases of R (#7711)'),
             note_after='Entries for dplyr 1.1.4 (the installed version) and earlier are not held.')
    pk.block('readr 2.2.0, whole entry (removed deprecated functions; literal data must be wrapped in I())', U['readr'], r,
             cut(r, '## readr 2.2.0', '## readr 2.1.6'))
    pk.block('readr 2.1.6 (CRAN release 2025-11-14), whole entry', U['readr'], r,
             cut(r, '## readr 2.1.6', '## readr 2.1.5'),
             note_after='Entries for readr 2.1.5 (the installed version) and earlier are not held.')
    pk.block('tidyr 1.3.2 (CRAN release 2025-12-19), whole entry', U['tidyr'], t,
             cut(t, '## tidyr 1.3.2', '## tidyr 1.3.0'),
             note_after='The page lists no entry headed tidyr 1.3.1 (the installed version): after 1.3.2 it goes to 1.3.0. Entries for 1.3.0 and earlier are not held.')
    gq = hq(key, g, bullet(g, 'Update the ggplot2 licence to an MIT license'))
    rq = hq(key, r, cut(r, 'We are systematically re-licensing', 'now released under the MIT license.', include_end=True))
    head = {p: hq(key, R[p], line(R[p], f'## {p} ')) for p in U}
    header = f"""TIDYVERSE CHANGELOGS (ggplot2, dplyr, readr, tidyr) — ENTRIES AFTER THE BOOK'S INSTALLED VERSIONS
VERBATIM SOURCE PACK (EXCERPTS)
============================================================

Transcription rule for this file: every line between a [TEXT] and an [END TEXT] line is an exact,
unaltered slice of the text returned by the TinyFish fetch_content tool (markdown) for the URL in that
block's heading, saved unchanged under books/S52-R1/intake/raw/ and cut programmatically (raw[i:j]) by
books/S52-R1/intake/build-c/build.py; verify.py re-checks each as a whitespace-normalised substring of the
saved fetch. The markdown conversion puts each inline code name (`filter()`) in its own fenced block on
separate lines; that is how the fetch returned it and it is kept. Where material is left out, the omission
is marked [...] in place. Lines beginning [NOTE] are this file's own annotation and are NOT source text.

CITATION: the changelog (NEWS) pages of the package websites, each built from the package's NEWS.md:
  ggplot2 {U['ggplot2']}   dplyr {U['dplyr']}
  readr {U['readr']}       tidyr {U['tidyr']}
URL FETCHED: those four URLs, TinyFish fetch_content, markdown, ttl 0 (live), {DATE}.

NEWEST ENTRY ON EACH PAGE on {DATE} (cut from the fetch): "{head['ggplot2']}"; "{head['dplyr']}";
"{head['readr']}"; "{head['tidyr']}". [NOTE] Task 1 (READY.md) recorded dplyr 1.2.1 as the newest
heading; the page fetched here has no 1.2.1 entry, its newest heading is 1.2.0. readr 2.2.0 carries no
"CRAN release" date line on the page.

INSTALLED VERSIONS (the book's): ggplot2 3.4.4, dplyr 1.1.4, readr 2.1.5, tidyr 1.3.1 (packageVersion(),
see the rdocs_s52r1_* files). Only entries for LATER versions are held.

LICENCE: none is stated on the four pages. The text is the package's NEWS.md, part of the package source;
the installed DESCRIPTION files (rdocs_s52r1_* files) give "License: MIT + file LICENSE" for all four. The
pages themselves record the relicensing, e.g. ggplot2: "{gq.strip()}" and readr: "{rq}"

SELECTION RULE (intake brief): only entries about behaviour a beginner's code in S52-R1 could meet — a
changed default, a new function or argument replacing a pattern the book teaches, or the deprecation or
removal of something in the book's function list (filter, select, mutate, summarise, group_by, arrange,
count, if_else, case_when, left_join, anti_join; pivot_longer, pivot_wider, drop_na; read_csv, problems;
ggplot, aes, geom_histogram, geom_boxplot, ggsave, facet_wrap) — plus each version's heading and summary
where the block starts at it. Whole version entries are held for readr 2.2.0, readr 2.1.6, tidyr 1.3.2
and ggplot2 4.0.3, because they are short. Everything else is omitted and marked.

WHAT THIS FILE DOES NOT SAY: it does not say which of these changes alters any output printed in S52-R1.
That is found only by running the book's code on the newer versions, which this sandbox cannot install.
"""
    return pk.write(header), pk.n


def penguins():
    key = 'horst_2020_palmerpenguins'
    pk = Pack(key)
    facts = 'horst_2020_palmerpenguins-facts.txt'
    desc = 'horst_2020_palmerpenguins-DESCRIPTION.txt'
    cran = 'horst_2020_palmerpenguins-cran.txt'
    U = 'https://cran.r-project.org/package=palmerpenguins'
    f_all = hq(key, facts, cut(facts))
    lic = hq(key, desc, line(desc, 'License:'))
    cran_lic = hq(key, cran, cut(cran, 'License:', 'URL:'))
    pk.block('Help page "penguins_raw" (palmerpenguins 0.1.1), whole: the 17 variables and the data sources',
             'rhelp://palmerpenguins@0.1.1/penguins_raw', 'horst_2020_palmerpenguins-help-penguins_raw.txt',
             cut('horst_2020_palmerpenguins-help-penguins_raw.txt'))
    pk.block('DESCRIPTION file of palmerpenguins 0.1.1, whole', 'rfile://palmerpenguins@0.1.1/DESCRIPTION', desc, cut(desc))
    pk.block('citation("palmerpenguins"), as printed by R 4.3.3 (text and BibTeX)', 'rcitation://palmerpenguins@0.1.1',
             'horst_2020_palmerpenguins-citation.txt', cut('horst_2020_palmerpenguins-citation.txt'))
    pk.block('CRAN package page, palmerpenguins, whole as extracted', U, cran, cut(cran))
    # header line and first two data rows of the CSV itself
    csvname = '../../../../sources/data/penguins_raw.csv'
    s = open(os.path.join(SRC, 'data/penguins_raw.csv'), encoding='utf-8').read()
    j = 0
    for _ in range(3):
        j = s.find('\n', j) + 1
    MANIFEST.append(['BLOCK', key, csvname, 'sources/data/penguins_raw.csv', 0, j])
    pk.n += 1
    pk.parts.append(f'{BAR}\n{pk.n}. sources/data/penguins_raw.csv: header line and first two data rows\n'
                    f'file://sources/data/penguins_raw.csv\n{BAR}\n\n[TEXT]\n{s[:j].strip(chr(10))}\n[END TEXT]\n'
                    f'[...]\n[NOTE] The other 342 data rows are in sources/data/penguins_raw.csv itself.\n')
    header = f"""PALMERPENGUINS 0.1.1 — penguins_raw.csv (THE BOOK'S DATASET) AND ITS DOCUMENTATION
VERBATIM SOURCE PACK
============================================================

Transcription rule for this file: every line between a [TEXT] and an [END TEXT] line is an exact,
unaltered slice of a raw file saved under books/S52-R1/intake/raw/ (a render or file from the installed
package, or the TinyFish fetch of the CRAN page for the URL in the block heading), cut programmatically
(raw[i:j]) by books/S52-R1/intake/build-c/build.py and re-checked by verify.py. Locators rhelp://, rfile://
and rcitation:// are local documents (see the rdocs_s52r1_* files for the scheme); file:// is the CSV held
in this folder. Lines beginning [NOTE] are this file's own annotation and are NOT source text.

CITATION: Horst AM, Hill AP, Gorman KB. palmerpenguins: Palmer Archipelago (Antarctica) penguin data.
R package version 0.1.1 (CRAN, published 2022-08-15). doi:10.5281/zenodo.3960218.
https://allisonhorst.github.io/palmerpenguins/. [NOTE] The package's own citation() (block 3) gives
year 2020 and "R package version 0.1.0"; the installed and CRAN version is 0.1.1. The data themselves come
from Palmer Station Antarctica LTER and K. Gorman (Environmental Data Initiative, 2020) and were first
published in Gorman, Williams and Fraser 2014, PLoS ONE 9(3):e90081 (block 1, Source).

THE DATA FILE HELD: sources/data/penguins_raw.csv, copied byte for byte on {DATE} from the installed
package's system.file("extdata", "penguins_raw.csv", package = "palmerpenguins") by
books/S52-R1/intake/build-c/penguins.R. Task 1 (READY.md) found the same MD5 for
https://raw.githubusercontent.com/allisonhorst/palmerpenguins/main/inst/extdata/penguins_raw.csv.
FACTS RECORDED BY SCRIPT (penguins.R output, cut whole from its saved output; read with readr 2.1.5,
default na = c("", "NA")):
{chr(10).join('  ' + x for x in f_all.splitlines())}

LICENCE: the installed DESCRIPTION states "{lic}". The CRAN page (block 4), fetched {DATE}, states
"{' '.join(cran_lic.split())}" (between the License and URL fields).
[NOTE] The text of the CC0 deed itself was not fetched; this file states only what the two pages say.

WHAT THIS FILE HOLDS: the penguins_raw help page, the DESCRIPTION, citation() output, the CRAN page and the
CSV's first three lines, each whole as marked. The penguins (cleaned) dataset and its help page are not held.
"""
    return pk.write(header), pk.n


if __name__ == '__main__':
    res = rdocs()
    for k, (path, n, ts) in res.items():
        print(k, n, 'blocks')
    print(news())
    print(penguins())
    json.dump(MANIFEST, open(os.path.join(HERE, 'manifest.json'), 'w'), indent=0)
