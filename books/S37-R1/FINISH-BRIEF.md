# Finishing brief · S37-R1 drafts (the chat stopped mid-draft on 24 Sep)

Your batch's records already exist in `check/records/S37/`, written by an earlier drafter of the same
batch who was stopped during its self-check, before writing its notes. Do not start again: **finish
them.** Follow `books/S37-R1/DRAFT-BRIEF.md` (read it whole, with everything it tells you to read), then:

1. Read your records whole. Complete anything unfinished (a missing field, a stub, a drill set that
   does not reach both ends of the ladder, a figure without a spec or `figure_note`).
2. **Withdrawn sources (25 Sep):** `eca_1955` and `food_corporations_act_1964` are no longer held
   (India Code's terms forbid automated access). Any claim resting on them is re-sourced from a held
   file (e.g. `dfpd_pds`, `fci_about`, the PIB releases) or cut, and the references removed. Do not
   cite them even with `opened: false`.
3. Do the whole self-check in DRAFT-BRIEF.md: `python check/build.py --check` blocking zero for your
   records; every practice answer and `working` number recomputed in Python; every quote found in its
   file and stating its number; each SELFCHECK item including 4a; figures pass `draw.py --book S37-R1`.
4. Write `books/S37-R1/draft-notes-<batch>.md` as DRAFT-BRIEF.md says (records, anything unsourced,
   why each practice-set size, figures wanted, glossary rows).

Do not commit. Return at most 150 words.
