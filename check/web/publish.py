"""Publish frozen books to drharshmaheshwari.com. Run by .github/workflows/publish-books.yml.

    python check/web/publish.py check     # prove every key works; build one book; change nothing
    python check/web/publish.py publish   # publish whatever frozen book is not on the site yet

What `publish` does, for every book whose frozen version is on neither the site's `main` nor the
open publisher branch (`books/auto-publish`):

  1. builds its PDF (check/build.py --subject <ID>, the series edition, exactly as a chat would);
  2. uploads the PDF and its figures to R2 (`drhm-files`, under books/obesity-expertise/). A PDF that
     is already there is never replaced: a version's URL is permanent, so is its file;
  3. checks every uploaded file comes back from https://files.drharshmaheshwari.com/;
  4. re-exports every frozen book into the site (check/web/export.py --frozen), commits the result
     to `books/auto-publish` and opens a pull request. Cloudflare builds a Preview of that branch;
  5. writes the Preview's pull request into each book's Notion row (✅ Completed ticked).

While the repository variable PUBLISH_MODE is not `auto`, it stops there: Harsh merges the pull
request after looking at the Preview. With PUBLISH_MODE=auto it merges the pull request itself.

Every run also brings Notion up to date with the live site: a book whose version is on the site's
`main` gets 🌐 On website, Stage = Live, Live URL and Last published.

Keys (repository secrets, never in a chat): R2_ACCOUNT_ID, R2_ACCESS_KEY_ID, R2_SECRET_ACCESS_KEY,
SITE_REPO_TOKEN (push branches and open pull requests on covisheild/drharshmaheshwari), NOTION_TOKEN.
"""
import datetime as dt
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
CHECK = os.path.dirname(HERE)
ROOT = os.path.dirname(CHECK)
sys.path.insert(0, HERE)
sys.path.insert(0, CHECK)

import export  # noqa: E402

SITE_REPO = "covisheild/drharshmaheshwari"
SITE = "https://drharshmaheshwari.com"
BRANCH = "books/auto-publish"
DATA = "src/data/books/obesity-expertise"
BUCKET = "drhm-files"
SOURCES_BUCKET = "drhm-sources"
PREFIX = f"books/{export.SERIES_SLUG}/"
NOTION_DS = "4f06c45f-4d60-4a5f-a16a-0aee045ae757"   # Website Desk · Content Desk
NOTION_VERSION = "2025-09-03"
SITE_DIR = os.environ.get("SITE_DIR", os.path.join(ROOT, "_site"))
SUMMARY = []


def say(line=""):
    print(line, flush=True)
    SUMMARY.append(line)


def env(name):
    v = os.environ.get(name, "").strip()
    if not v:
        raise SystemExit(f"The repository secret {name} is missing or empty.")
    return v


def run(cmd, cwd=None):
    subprocess.run(cmd, cwd=cwd, check=True)


# ---------------------------------------------------------------- what is frozen, what is live

def frozen_books():
    """[(id, version)] frozen in both map/BOOKS.yml and books/<ID>/book.yml, in series order."""
    books = export._yaml(os.path.join(ROOT, "map", "BOOKS.yml"))["books"]
    out = []
    for b in books:
        if b.get("status") != "frozen":
            continue
        meta = export._yaml(os.path.join(ROOT, "books", b["id"], "book.yml"))
        if meta.get("status") == "frozen" and meta.get("version"):
            out.append((b["id"], str(meta["version"])))
    return out


def site_versions(ref):
    """{id: version} of the books exported on a branch of the site, read from a git ref in SITE_DIR."""
    got = {}
    try:
        names = subprocess.run(["git", "ls-tree", "-r", "--name-only", ref, "--", DATA], cwd=SITE_DIR,
                               capture_output=True, text=True, check=True).stdout.split()
    except subprocess.CalledProcessError:
        return got
    for n in names:
        if n.endswith("/book.json"):
            raw = subprocess.run(["git", "show", f"{ref}:{n}"], cwd=SITE_DIR, capture_output=True, text=True, check=True).stdout
            b = json.loads(raw)
            got[b["id"]] = str(b["version"])
    return got


# ---------------------------------------------------------------- R2

def r2():
    import boto3
    from botocore.config import Config
    return boto3.client("s3", endpoint_url=f"https://{env('R2_ACCOUNT_ID')}.r2.cloudflarestorage.com",
                        aws_access_key_id=env("R2_ACCESS_KEY_ID"), aws_secret_access_key=env("R2_SECRET_ACCESS_KEY"),
                        region_name="auto", config=Config(retries={"max_attempts": 4}))


def r2_has(s3, key):
    try:
        return s3.head_object(Bucket=BUCKET, Key=key)
    except s3.exceptions.ClientError as e:
        if e.response.get("Error", {}).get("Code") in ("404", "NoSuchKey", "NotFound"):
            return None
        raise


def public_ok(url, kind):
    """The public file answers 200 with the right kind of content (not R2's 'not found' page)."""
    req = urllib.request.Request(url, method="GET", headers={"Range": "bytes=0-7", "User-Agent": "drhm-publisher"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            head = r.read(8)
    except urllib.error.HTTPError as e:
        return f"{e.code}"
    if kind == "pdf" and not head.startswith(b"%PDF"):
        return "not a PDF"
    if kind == "png" and not head.startswith(b"\x89PNG"):
        return "not a PNG"
    return "ok"


# ---------------------------------------------------------------- GitHub (the site repository)

def gh(method, path, body=None):
    req = urllib.request.Request(f"https://api.github.com{path}", method=method,
                                 data=json.dumps(body).encode() if body is not None else None,
                                 headers={"Authorization": f"Bearer {env('SITE_REPO_TOKEN')}",
                                          "Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28",
                                          "User-Agent": "drhm-publisher"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            raw = r.read()
            return r.status, (json.loads(raw) if raw else {})
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read() or b"{}")


def site_remote():
    return f"https://x-access-token:{env('SITE_REPO_TOKEN')}@github.com/{SITE_REPO}.git"


def clone_site():
    if not os.path.isdir(os.path.join(SITE_DIR, ".git")):
        run(["git", "clone", "--quiet", "--no-tags", site_remote(), SITE_DIR])
    run(["git", "fetch", "--quiet", "origin", "main"], cwd=SITE_DIR)
    subprocess.run(["git", "fetch", "--quiet", "origin", f"{BRANCH}:refs/remotes/origin/{BRANCH}"], cwd=SITE_DIR)


def open_pr():
    st, prs = gh("GET", f"/repos/{SITE_REPO}/pulls?head={SITE_REPO.split('/')[0]}:{BRANCH}&state=open")
    return prs[0] if st == 200 and prs else None


# ---------------------------------------------------------------- Notion

def notion(method, path, body=None):
    req = urllib.request.Request(f"https://api.notion.com/v1{path}", method=method,
                                 data=json.dumps(body).encode() if body is not None else None,
                                 headers={"Authorization": f"Bearer {env('NOTION_TOKEN')}", "Notion-Version": NOTION_VERSION,
                                          "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, json.loads(r.read() or b"{}")
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read() or b"{}")


def notion_rows():
    """{book id: page} for the Content Desk's Book rows of this series."""
    st, res = notion("POST", f"/data_sources/{NOTION_DS}/query",
                     {"filter": {"property": "Type", "select": {"equals": "Book"}}, "page_size": 100})
    if st != 200:
        raise RuntimeError(f"Notion answered {st}: {res.get('message', res)}")
    rows = {}
    for p in res.get("results", []):
        title = "".join(t.get("plain_text", "") for t in p["properties"]["Title"]["title"])
        if not title.startswith("Obesity Expertise · "):
            continue
        rest = title.split("·", 1)[1].strip()
        if rest.startswith("Book 0"):
            rows["B0"] = p
        else:  # "S36 Rung 1: ..."
            parts = rest.split(":")[0].split()
            if len(parts) >= 3 and parts[1] == "Rung":
                rows[f"{parts[0]}-R{parts[2]}"] = p
    return rows


def note(text):
    return {"rich_text": [{"text": {"content": text[:1900]}}]}


def notion_row_title(book_id):
    meta = export._yaml(os.path.join(ROOT, "books", book_id, "book.yml"))
    if book_id == "B0":
        return f"Obesity Expertise · Book 0: {meta['title']}"
    s, r = book_id.split("-R")
    name = meta["title"].replace(f" · Rung {r}", "")
    return f"Obesity Expertise · {s} Rung {r}: {name}"


def notion_mark_published(book_id, version, pr_url):
    rows = notion_rows()
    props = {"✅ Completed": {"checkbox": True},
             "Claude notes": note(f"{dt.date.today():%d %b %Y}: v{version} published by the book publisher: PDF and figures "
                                  f"on R2 (checked). Preview: {pr_url} . Goes live when that pull request is merged; "
                                  "🌐 is ticked then.")}
    if book_id in rows:
        st, res = notion("PATCH", f"/pages/{rows[book_id]['id']}", {"properties": props})
    else:
        props.update({"Title": {"title": [{"text": {"content": notion_row_title(book_id)}}]},
                      "Type": {"select": {"name": "Book"}}, "Section": {"select": {"name": "Books"}},
                      "Audience": {"select": {"name": "Clinicians"}}})
        st, res = notion("POST", "/pages", {"parent": {"type": "data_source_id", "data_source_id": NOTION_DS}, "properties": props})
    if st != 200:
        raise RuntimeError(f"Notion answered {st} for {book_id}: {res.get('message', res)}")


def notion_sync_live(live):
    """Tick 🌐 for every book whose frozen version is on the site's main branch."""
    rows = notion_rows()
    changed = []
    for book_id, version in live.items():
        p = rows.get(book_id)
        if not p:
            continue
        pr = p["properties"]
        url = f"{SITE}{export.SITE_BASE}{export.slug(book_id)}/"
        if pr["🌐 On website"]["checkbox"] and pr["Live URL"].get("url") == url and \
                f"v{version} live" in "".join(t.get("plain_text", "") for t in pr["Claude notes"]["rich_text"]):
            continue
        st, res = notion("PATCH", f"/pages/{p['id']}", {"properties": {
            "🌐 On website": {"checkbox": True}, "✅ Completed": {"checkbox": True}, "Stage": {"select": {"name": "Live"}},
            "Live URL": {"url": url}, "Slug": note(export.slug(book_id)),
            "Last published": {"date": {"start": dt.date.today().isoformat()}},
            "Claude notes": note(f"{dt.date.today():%d %b %Y}: v{version} live at {url} (book publisher).")}})
        if st != 200:
            raise RuntimeError(f"Notion answered {st} for {book_id}: {res.get('message', res)}")
        changed.append(book_id)
    return changed


# ---------------------------------------------------------------- the two modes

def build_pdf(book_id):
    run([sys.executable, os.path.join(CHECK, "build.py"), "--subject", book_id], cwd=ROOT)
    path = os.path.join(CHECK, "_build", f"{book_id}.pdf")
    if not os.path.exists(path):
        raise SystemExit(f"{book_id}: the build made no PDF")
    return path


def check_mode():
    """Use every key once, change nothing anyone can see, and build one book end to end."""
    ok = True
    say("## Publisher check")
    # R2: read both buckets, and prove writing works with a throwaway object in the private bucket.
    try:
        s3 = r2()
        n = s3.list_objects_v2(Bucket=BUCKET, Prefix=PREFIX, MaxKeys=1000).get("KeyCount", 0)
        say(f"- R2 `{BUCKET}`: readable, {n} files under `{PREFIX}`")
        n = s3.list_objects_v2(Bucket=SOURCES_BUCKET, MaxKeys=1000).get("KeyCount", 0)
        say(f"- R2 `{SOURCES_BUCKET}`: readable, {n} files")
        key = "_publisher-check/written-by-github-actions.txt"
        s3.put_object(Bucket=SOURCES_BUCKET, Key=key, Body=b"ok")
        s3.delete_object(Bucket=SOURCES_BUCKET, Key=key)
        say("- R2: can write and delete (tested in the private bucket)")
    except Exception as e:  # noqa: BLE001
        ok = False
        say(f"- **R2 key failed**: {e}")
    # Public files host.
    for f, kind in ((f"{PREFIX}B0-v1.2.pdf", "pdf"), (f"{PREFIX}figures/c5-two-scales.png", "png")):
        r = public_ok(f"{export.FILES}/{f}", kind)
        ok &= r == "ok"
        say(f"- Public file `{f}`: {r}")
    # Site repository: read, then push and delete a throwaway branch.
    try:
        clone_site()
        st, _ = gh("GET", f"/repos/{SITE_REPO}")
        say(f"- Site repository: readable ({st})")
        test = "books/publisher-check"
        run(["git", "push", "--quiet", site_remote(), f"origin/main:refs/heads/{test}"], cwd=SITE_DIR)
        run(["git", "push", "--quiet", site_remote(), f":refs/heads/{test}"], cwd=SITE_DIR)
        say("- Site repository: can push a branch (made and deleted `books/publisher-check`)")
        st, prs = gh("GET", f"/repos/{SITE_REPO}/pulls?state=all&per_page=1")
        say(f"- Site repository: can read pull requests ({st})" if st == 200 else f"- **Site token cannot read pull requests ({st})**")
        ok &= st == 200
    except Exception as e:  # noqa: BLE001
        ok = False
        say(f"- **Site token failed**: {e}")
    # Notion.
    try:
        rows = notion_rows()
        say(f"- Notion: Content Desk readable; {len(rows)} Obesity Expertise book rows ({', '.join(sorted(rows))})")
    except Exception as e:  # noqa: BLE001
        ok = False
        say(f"- **Notion failed**: {e}. Is the integration added to the Website Desk page (••• → Connections)?")
    # What a publish run would do now.
    try:
        main_v, branch_v = site_versions("origin/main"), site_versions(f"origin/{BRANCH}")
        todo = [(b, v) for b, v in frozen_books() if main_v.get(b) != v and branch_v.get(b) != v]
        say(f"- Frozen books: {', '.join(f'{b} v{v}' for b, v in frozen_books())}")
        say(f"- A publish run now would publish: {', '.join(f'{b} v{v}' for b, v in todo) or 'nothing'}")
    except Exception as e:  # noqa: BLE001
        ok = False
        say(f"- **Could not compare with the site**: {e}")
    # One real build, to prove the runner can make a book.
    try:
        pdf = build_pdf("B0")
        out = os.path.join(ROOT, "_check-export")
        run([sys.executable, os.path.join(HERE, "export.py"), "B0", "--out", out, "--figures-out", os.path.join(out, "_fig")])
        say(f"- Built Book 0 here: PDF {os.path.getsize(pdf) / 1e6:.1f} MB; reader export OK")
    except Exception as e:  # noqa: BLE001
        ok = False
        say(f"- **Building Book 0 failed**: {e}")
    say("")
    say("Everything works." if ok else "Something above failed; nothing was published.")
    return ok


def publish_mode():
    clone_site()
    main_v, branch_v = site_versions("origin/main"), site_versions(f"origin/{BRANCH}")
    live = {b: v for b, v in frozen_books() if main_v.get(b) == v}
    todo = [(b, v) for b, v in frozen_books() if main_v.get(b) != v and branch_v.get(b) != v]
    say("## Book publisher")
    try:
        changed = notion_sync_live(live)
        if changed:
            say(f"- Notion: marked live: {', '.join(changed)}")
    except Exception as e:  # noqa: BLE001
        say(f"- Notion could not be updated: {e}")
    if not todo:
        say("- Nothing new to publish.")
        return True

    s3 = r2()
    for book_id, version in todo:
        say(f"### {book_id} v{version}")
        key = f"{PREFIX}{book_id}-v{version}.pdf"
        if r2_has(s3, key):
            say(f"- PDF already on R2 (kept as it is): `{key}`")
        else:
            pdf = build_pdf(book_id)
            s3.upload_file(pdf, BUCKET, key, ExtraArgs={"ContentType": "application/pdf"})
            say(f"- PDF uploaded: `{key}` ({os.path.getsize(pdf) / 1e6:.1f} MB)")

    # Export every frozen book into the site on the publisher branch, then upload any missing figure.
    base = f"origin/{BRANCH}" if branch_v else "origin/main"
    run(["git", "checkout", "--quiet", "-B", BRANCH, base], cwd=SITE_DIR)
    if branch_v:  # keep the branch current with main
        run(["git", "-c", "user.name=Book publisher", "-c", "user.email=contact@drharshmaheshwari.com",
             "merge", "--quiet", "--no-edit", "origin/main"], cwd=SITE_DIR)
    figs = os.path.join(ROOT, "_figures")
    run([sys.executable, os.path.join(HERE, "export.py"), "--frozen", "--out", os.path.join(SITE_DIR, DATA), "--figures-out", figs])
    added = 0
    for f in sorted(os.listdir(figs)):
        key = f"{PREFIX}figures/{f}"
        if not r2_has(s3, key):
            s3.upload_file(os.path.join(figs, f), BUCKET, key, ExtraArgs={"ContentType": "image/png"})
            added += 1
    say(f"- Figures: {added} uploaded, {len(os.listdir(figs)) - added} already on R2")

    # Every file the new books point at must come back from the public address.
    bad = []
    for book_id, version in todo:
        bad += [k for k in [f"{PREFIX}{book_id}-v{version}.pdf"] if public_ok(f"{export.FILES}/{k}", "pdf") != "ok"]
    for f in sorted(os.listdir(figs)):
        if public_ok(f"{export.FILES}/{PREFIX}figures/{f}", "png") != "ok":
            bad.append(f"{PREFIX}figures/{f}")
    if bad:
        say("- **These files do not come back from files.drharshmaheshwari.com; nothing was published:** " + ", ".join(bad))
        return False
    say("- Every PDF and figure answers from files.drharshmaheshwari.com")

    run(["git", "add", "-A", DATA], cwd=SITE_DIR)
    names = ", ".join(f"{b} v{v}" for b, v in todo)
    run(["git", "-c", "user.name=Book publisher", "-c", "user.email=contact@drharshmaheshwari.com",
         "commit", "--quiet", "-m", f"Publish {names}\n\nExported from obesity-course {os.environ.get('GITHUB_SHA', '')[:7]} by the book publisher."],
        cwd=SITE_DIR)
    run(["git", "push", "--quiet", "--force-with-lease", site_remote(), f"{BRANCH}:refs/heads/{BRANCH}"], cwd=SITE_DIR)
    pr = open_pr()
    if not pr:
        body = ("New or updated books from the Obesity Expertise series: " + names + ".\n\n"
                "PDFs and figures are on R2 and every link was checked. Cloudflare builds a Preview of this branch: "
                "open it, look at the new books, and merge this pull request to make them live.\n\n"
                "Made by `check/web/publish.py` in obesity-course.")
        st, pr = gh("POST", f"/repos/{SITE_REPO}/pulls", {"title": f"Publish {names}", "head": BRANCH, "base": "main", "body": body})
        if st not in (200, 201):
            say(f"- **Could not open the pull request ({st})**: {pr.get('message')}")
            return False
    say(f"- Preview pull request: {pr['html_url']}")
    for book_id, version in todo:
        try:
            notion_mark_published(book_id, version, pr["html_url"])
        except Exception as e:  # noqa: BLE001
            say(f"- Notion could not be updated for {book_id}: {e}")
    if os.environ.get("PUBLISH_MODE", "").strip().lower() == "auto":
        st, res = gh("PUT", f"/repos/{SITE_REPO}/pulls/{pr['number']}/merge", {"merge_method": "merge"})
        say("- PUBLISH_MODE=auto: merged, the books go live in a few minutes" if st == 200
            else f"- **PUBLISH_MODE=auto but the merge failed ({st})**: {res.get('message')}")
    else:
        say("- Waiting for Harsh to look at the Preview and merge (PUBLISH_MODE is not `auto`).")
    return True


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "check"
    ok = check_mode() if mode == "check" else publish_mode()
    path = os.environ.get("GITHUB_STEP_SUMMARY")
    if path:
        with open(path, "a", encoding="utf-8") as fh:
            fh.write("\n".join(SUMMARY) + "\n")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
