# Publishing books to drharshmaheshwari.com

No chat publishes books by hand and no chat holds a key. When a book is frozen and merged to `main`,
GitHub Actions (`.github/workflows/publish-books.yml` → `check/web/publish.py`):

1. builds the PDF and uploads it with the book's figures to R2 (`drhm-files`, `books/obesity-expertise/`),
   never replacing a PDF that is already there;
2. checks every file comes back from `https://files.drharshmaheshwari.com/`;
3. exports every frozen book into the website and opens a pull request from `books/auto-publish`.
   Cloudflare builds a Preview of that branch;
4. ticks ✅ Completed in the book's Notion row and writes the pull request link in Claude notes.

Harsh opens the Preview and merges the pull request. Within six hours the next scheduled run marks the book
🌐 On website, Stage = Live, with Live URL and Last published, in Notion.

**Going automatic.** After about five books have gone through the Preview without problems: repository
Settings → Secrets and variables → Actions → Variables → New repository variable `PUBLISH_MODE` = `auto`.
The publisher then merges its own pull request once every check has passed. Delete the variable to go back.

**Keys** (Settings → Secrets and variables → Actions → Repository secrets): `R2_ACCOUNT_ID`,
`R2_ACCESS_KEY_ID`, `R2_SECRET_ACCESS_KEY` (R2 token: Object Read & Write on `drhm-files` and `drhm-sources`),
`SITE_REPO_TOKEN` (fine-grained token on `covisheild/drharshmaheshwari` only: Contents and Pull requests,
read and write; it expires, so renew it before its date), `NOTION_TOKEN` (internal integration, added to the
Website Desk page under ••• → Connections).

**When something fails** the run shows a red ✗ under the Actions tab, and its summary says which step and
which file. Nothing reaches the site unless every check passed. Run it by hand: Actions → Publish books →
Run workflow → `check` (uses every key, builds Book 0, changes nothing) or `publish`.
