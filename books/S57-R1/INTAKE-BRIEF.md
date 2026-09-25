# Source intake brief · S57-R1 (for intake subagents)

You file sources for S57-R1 to the intake checklist in `PIPELINE.md` ("Before anything: the source gate",
"The intake checklist") and `claude.md` §7b and §8 (read those three sections only). Model the method on
`books/S02-R1/INTAKE.md` (read its first 40 lines): fetch with `mcp__TinyFish__fetch_content` (load it with
ToolSearch "select:mcp__TinyFish__fetch_content"); PubMed tools (`mcp__PubMed__*`) may be used to confirm
identifiers and to get PMC full text. TinyFish can return a PDF's text layer (OpenIntro was taken that way)
— try it before declaring a PDF unobtainable. PMC open-access XML is also at
https://pmc-oa-opendata.s3.amazonaws.com/PMC<id>.1/PMC<id>.1.xml. Never use curl/wget/Python HTTP.
Never store WebFetch output. Never paraphrase into a source file: every stored passage is cut by script
from the saved raw fetch text (`raw[i:j]`) and re-checked as a whitespace-normalised substring of it.

For each source in your group:
1. Fetch; save the raw result under `books/S57-R1/intake/raw/<citekey>-*.txt` (your own names only).
2. Write `sources/<citekey>.txt`: an honest header (what it is, URL fetched, date, licence quoted from the
   work's own page, exactly which parts are held, every omission marked `[...]` with a `[NOTE]`), then the
   passages. Keep the passages the inventory's concepts need (see `books/S57-R1/INVENTORY.md` and
   `books/S57-R1/READY.md`): results with their numbers, definitions, the key tables in text form.
   Whole relevant sections are better than fragments; skip reference lists.
3. Citekey: new and unique — `grep` it in `sources/INDEX.yml` and `check/references/library.bib`; use a
   form like `roediger_karpicke_2006`. Two other book chats (S36-R1 qualitative methods, S37-R1 food
   policy) are adding sources on unpublished branches, so prefer specific keys (author_year_topic).
4. Do NOT edit `sources/INDEX.yml`, `check/references/library.bib` or `sources/SOURCES.md` yourself
   (three intake agents run at once). Instead write your entries into your own fragment file
   `books/S57-R1/intake/fragment-<group>.md` with three fenced blocks: the INDEX.yml `files:` entries
   (same shape as existing ones, `what:` naming exactly what is held), the .bib entries (same shape as
   existing; `note` gives licence and identifiers; NO repository path anywhere in the entry), and the
   SOURCES.md lines (look at the file's existing format first).
5. Verbatim check by script for every passage; record passages and pass counts.
6. Write `books/S57-R1/intake/log-<group>.md`: one table row per source (source, URL, passages, check
   n/n, licence as stated, citekey) and, for anything NOT obtained, why and what exact file/URL Harsh
   would need to download. If a source is unobtainable but an open substitute carries the same claim
   (e.g. a PMC review restating the numbers), you may file the substitute and say so.
Do not commit. Reply ≤150 words: obtained n/m, citekeys, what needs Harsh, your log path.
