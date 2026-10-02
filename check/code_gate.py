"""The code gate: run every R and shell block a book prints, and check each printed output.

    python check/code_gate.py --check                      # every record that carries code
    python check/code_gate.py --check --subject S52-R1     # one book
    python check/code_gate.py --check --record <path.yml>  # one record (any path; repeatable)
    python check/code_gate.py --write --subject S52-R1     # fill in or replace ```output blocks
    python check/code_gate.py --check --no-cache           # rerun everything

Added 2 Oct 2026 for S52-R1 (Book 6, R), on Harsh's instruction. A record's code is written in
```r, ```sh and ```output fences (check/codeblocks.py says what each attribute means). An output
block is never typed by hand: `--write` fills it from a fresh run, and `--check` (which
`check/build.py --check` runs, cached) fails when the page and a fresh run disagree.

**Sessions.** A record's prose fields, in the order the book prints them (definition,
plain terms, illustrations, must-know points, common misreading, reporting it), form one R
session. Each exercise, each practice problem and each retrieval item (its prompt, then its
answer) is a fresh session of its own, because a reader may turn to it cold. Each session runs in
a new Rscript process (check/code/run_chunks.R) inside a scratch project built from
`books/<ID>/code.yml`: a mapping of project paths to repository files copied in, e.g.

    data-raw/penguins_raw.csv: sources/data/penguins_raw.csv

(or `files:` holding that mapping, plus `display_root:`), with an empty `.here` file at the root
so `here::here()` finds it. The scratch root's real path never reaches the page: it is shown as
`display_root` (default `~/project`). Every session gets the same options (width 72, no colour,
no rlang backtrace), a UTF-8 locale and TZ=UTC; R_LIBS_USER is left alone.

**Rules.** An r or sh block that is run and prints something must be followed by an ```output
block (blank lines between allowed); an output block must follow an r or sh block; a `norun` or
`file=` block has no output block; an error fails the gate unless the block is marked `error`,
and a block marked `error` must stop with one. Outputs are compared after removing trailing
whitespace on each line and trailing blank lines. `{{n:key}}` is never substituted inside code.

**Cache.** Results are stored under check/_build/code-cache/ (git-ignored), keyed by the
session's code, code.yml, the hashes of the files it copies in, the R and package versions, and
this tool's own source, so a repeat build reruns nothing that could not have changed.
"""
from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import codeblocks  # noqa: E402

RECORDS = os.path.join(HERE, "records")
CACHE = os.path.join(HERE, "_build", "code-cache")
BACKUP = os.path.join(HERE, "_build", "code-gate-backup")
DRIVER = os.path.join(HERE, "code", "run_chunks.R")
DEFAULT_DISPLAY_ROOT = "~/project"
TIMEOUT = 900
OPTIONS_R = ('options(width = 72, cli.num_colors = 1, crayon.enabled = FALSE, pillar.bold = FALSE, '
             'tibble.width = 72, rlang_backtrace_on_error = "none", cli.dynamic = FALSE, '
             'readr.show_progress = FALSE)\n')


# ---------------------------------------------------------------- what to run

def has_code_raw(raw: str) -> bool:
    return isinstance(raw, str) and "```" in raw and any(codeblocks.OPEN.match(l) for l in raw.split("\n"))


def book_of(rid: str) -> str:
    m = re.match(r"^(B0|S\d\d-R\d)", rid or "")
    return "B0" if (rid or "").startswith("B0") else (m.group(1) if m else "")


def sessions_of(r: dict) -> list:
    """[(session name, [(field label, yaml path, text)])] in the order the book prints them."""
    main = []
    d = r.get("definition") or {}
    main.append(("definition.text", ("definition", "text"), d.get("text")))
    main.append(("simplified_explanation", ("simplified_explanation",), r.get("simplified_explanation")))
    many = r.get("illustrations")
    if isinstance(many, list) and many:
        for i, ill in enumerate(many):
            if isinstance(ill, dict):
                for k in ("body", "analogy_breaks_when"):
                    main.append((f"illustrations[{i}].{k}", ("illustrations", i, k), ill.get(k)))
    elif isinstance(r.get("illustration"), dict):
        for k in ("body", "analogy_breaks_when"):
            main.append((f"illustration.{k}", ("illustration", k), r["illustration"].get(k)))
    for i, p in enumerate(r.get("must_know") if isinstance(r.get("must_know"), list) else []):
        if isinstance(p, dict):
            main.append((f"must_know[{i}].point", ("must_know", i, "point"), p.get("point")))
    for k in ("common_misreading", "reporting_sentence"):
        main.append((k, (k,), r.get(k)))
    out = [("main", main)]
    for i, ex in enumerate(r.get("exercises") or []):
        if isinstance(ex, dict):
            out.append((f"exercise {i + 1}", [(f"exercises[{i}].{k}", ("exercises", i, k), ex.get(k))
                                              for k in ("prompt", "answer")]))
    for i, p in enumerate(r.get("practice") or []):
        if isinstance(p, dict):
            out.append((f"practice {i + 1} (level {p.get('level')})",
                        [(f"practice[{i}].{k}", ("practice", i, k), p.get(k)) for k in ("prompt", "answer")]))
    for i, it in enumerate(r.get("retrieval_items") or []):
        if isinstance(it, dict):
            out.append((f"retrieval item {i + 1}", [(f"retrieval_items[{i}].{k}", ("retrieval_items", i, k),
                                                     it.get(k)) for k in ("q", "a")]))
    return [(n, [f for f in fs if isinstance(f[2], str)]) for n, fs in out]


def _safe_rel(p: str) -> bool:
    return bool(p) and not os.path.isabs(p) and ".." not in p.replace("\\", "/").split("/")


def plan(fields: list):
    """Steps for the R driver, the blocks to compare, and structural problems."""
    steps, items, problems, extra = [], [], [], []
    for label, path, text in fields:
        if not codeblocks.has_code(text):
            continue
        prs, orphans = codeblocks.pairs(text)
        for b in codeblocks.blocks(text):
            a = b["attrs"]
            if b["bad"]:
                problems.append((label, f"unknown attribute '{' '.join(b['bad'])}' on ```{b['tag']} "
                                        "(allowed: norun, error, file=<relative path>)"))
            if b["end"] is None:
                problems.append((label, f"a ```{b['tag']} block is never closed"))
            if b["tag"] == "output" and a:
                problems.append((label, "an ```output block takes no attributes"))
            if "file" in a and (b["tag"] != "r" or not _safe_rel(a["file"])):
                problems.append((label, f"file={a['file']} must be on an r block and be a relative path "
                                        "inside the project"))
            if "file" in a and (a.get("norun") or a.get("error")):
                problems.append((label, "a file= block is saved, never run: it takes no norun or error"))
        for o in orphans:
            problems.append((label, f"an ```output block (line {o['start'] + 1} of the field) does not "
                                    "immediately follow an r or sh block"))
            extra.append({"field": label, "path": path, "orphan": o})
        for b, out in prs:
            a = b["attrs"]
            code = "\n".join(b["body"])
            item = {"field": label, "path": path, "block": b, "out": out, "step": None,
                    "error": bool(a.get("error")), "mode": "run"}
            if "file" in a:
                steps.append({"kind": "file", "code": code, "file": a["file"]})
                item["mode"] = "file"
            elif a.get("norun"):
                item["mode"] = "norun"
            else:
                item["step"] = len(steps)
                steps.append({"kind": b["tag"], "code": code})
            if item["mode"] != "run" and out is not None:
                problems.append((label, f"a {item['mode']} block is never run, so it cannot have an "
                                        "```output block (python check/code_gate.py --write removes it)"))
            items.append(item)
    return steps, items, problems, extra


# ---------------------------------------------------------------- the project and the environment

def project(book: str):
    """(files {dest: abs source}, display_root, code.yml text, problems)."""
    path = os.path.join(REPO, "books", book, "code.yml")
    if not os.path.exists(path):
        return {}, DEFAULT_DISPLAY_ROOT, "", []
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    try:
        d = yaml.safe_load(text) or {}
    except yaml.YAMLError as e:
        return {}, DEFAULT_DISPLAY_ROOT, text, [f"books/{book}/code.yml does not parse: {e}"]
    files, disp = (d.get("files") or {}, d.get("display_root") or DEFAULT_DISPLAY_ROOT) \
        if isinstance(d.get("files"), dict) else (d, DEFAULT_DISPLAY_ROOT)
    out, probs = {}, []
    for dest, src in (files or {}).items():
        full = os.path.normpath(os.path.join(REPO, str(src)))
        if not _safe_rel(str(dest)):
            probs.append(f"books/{book}/code.yml: '{dest}' must be a relative path inside the project")
        elif not full.startswith(REPO + os.sep) or not os.path.isfile(full):
            probs.append(f"books/{book}/code.yml: '{src}' is not a file in the repository")
        else:
            out[str(dest)] = full
    return out, str(disp), text, probs


def _sha(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


_ENV = {}


def environment():
    """Locale, R fingerprint (R version and every installed package's version). Computed once."""
    if _ENV:
        return _ENV
    loc = "C.UTF-8"
    try:
        have = subprocess.run(["locale", "-a"], capture_output=True, text=True, timeout=30).stdout.split()
        low = {h.lower(): h for h in have}
        for want in ("c.utf-8", "c.utf8", "en_us.utf-8", "en_us.utf8"):
            if want in low:
                loc = low[want]
                break
    except Exception:
        pass
    probe = ('ip <- installed.packages()[, c("Package", "Version"), drop = FALSE];'
             'cat(R.version.string, paste(ip[order(ip[, 1]), 1], ip[order(ip[, 1]), 2], collapse = ";"))')
    p = subprocess.run(["Rscript", "--no-save", "--no-restore", "--no-init-file", "-e", probe],
                       capture_output=True, text=True, timeout=120)
    tool = hashlib.sha256()
    for f in (os.path.abspath(__file__), DRIVER, os.path.join(HERE, "codeblocks.py")):
        tool.update(open(f, "rb").read())
    _ENV.update(locale=loc, fingerprint=hashlib.sha256(p.stdout.encode()).hexdigest(),
                r_version=p.stdout.split(" ", 4)[2] if p.stdout else "?", tool=tool.hexdigest())
    return _ENV


def run_session(steps, files, display_root, key, use_cache=True):
    """Results [{output, errored}] for one session, from the cache or a fresh Rscript."""
    cpath = os.path.join(CACHE, key + ".json")
    if use_cache and os.path.exists(cpath):
        with open(cpath, encoding="utf-8") as fh:
            return json.load(fh), True
    env_ = environment()
    work = tempfile.mkdtemp(prefix="codegate-")
    try:
        root = os.path.join(work, "project")
        os.makedirs(root)
        open(os.path.join(root, ".here"), "w").close()
        for dest, src in files.items():
            os.makedirs(os.path.dirname(os.path.join(root, dest)) or root, exist_ok=True)
            shutil.copyfile(src, os.path.join(root, dest))
        with open(os.path.join(work, "Rprofile"), "w", encoding="utf-8") as fh:
            fh.write(OPTIONS_R)
        with open(os.path.join(work, "in.json"), "w", encoding="utf-8") as fh:
            json.dump({"root": root, "steps": steps}, fh)
        env = dict(os.environ, LANG=env_["locale"], LC_ALL=env_["locale"], TZ="UTC", NO_COLOR="1",
                   R_PROFILE_USER=os.path.join(work, "Rprofile"))
        p = subprocess.run(["Rscript", "--no-save", "--no-restore", "--no-init-file", DRIVER,
                            os.path.join(work, "in.json"), os.path.join(work, "out.json")],
                           cwd=root, env=env, capture_output=True, text=True, timeout=TIMEOUT)
        if not os.path.exists(os.path.join(work, "out.json")):
            tail = (p.stderr or p.stdout or "").strip().splitlines()[-3:]
            raise RuntimeError("the R driver produced no result: " + " | ".join(tail))
        with open(os.path.join(work, "out.json"), encoding="utf-8") as fh:
            results = json.load(fh)["results"]
        roots = sorted({root, os.path.realpath(root)}, key=len, reverse=True)
        for res in results:
            for rt in roots:
                res["output"] = res["output"].replace(rt, display_root)
    finally:
        shutil.rmtree(work, ignore_errors=True)
    os.makedirs(CACHE, exist_ok=True)
    with open(cpath, "w", encoding="utf-8") as fh:
        json.dump(results, fh)
    return results, False


def norm_lines(text: str) -> list:
    lines = [l.rstrip() for l in str(text).split("\n")]
    while lines and not lines[-1]:
        lines.pop()
    return lines


# ---------------------------------------------------------------- one record

def gate_record(rid, r, use_cache=True):
    """(failures [(field, message, diff_lines)], plans [(items, results, extra)], stats)."""
    fails, plans, stats = [], [], {"sessions": 0, "cached": 0}
    files, disp, cfg_text, cfg_probs = project(book_of(rid))
    fails += [("code.yml", p, []) for p in cfg_probs]
    todo = []
    for name, fields in sessions_of(r):
        steps, items, probs, extra = plan(fields)
        fails += [(f, m, []) for f, m in probs]
        if not items and not extra:
            continue
        todo.append((name, steps, items, extra))
    if not todo:
        return fails, plans, stats
    if not shutil.which("Rscript"):
        return fails + [("", "Rscript not found", [])], plans, stats
    env_ = environment()
    data = {d: _sha(s) for d, s in sorted(files.items())}

    def one(t):
        name, steps, items, extra = t
        if not any(s["kind"] in ("r", "sh") for s in steps):
            return t, [None] * len(steps), True
        key = hashlib.sha256(json.dumps({"steps": steps, "code.yml": cfg_text, "data": data,
                                         "display_root": disp, "r": env_["fingerprint"],
                                         "locale": env_["locale"], "tool": env_["tool"]},
                                        sort_keys=True).encode()).hexdigest()
        try:
            res, hit = run_session(steps, files, disp, key, use_cache)
        except Exception as e:  # a driver crash is a gate failure, never a silent pass
            res, hit = [{"output": f"code gate could not run this session: {e}", "errored": True}] * len(steps), False
        return t, res, hit

    with ThreadPoolExecutor(max_workers=max(1, min(4, os.cpu_count() or 1))) as pool:
        done = list(pool.map(one, todo))
    for (name, steps, items, extra), res, hit in done:
        stats["sessions"] += 1
        stats["cached"] += bool(hit)
        plans.append((items, res, extra))
        for it in items:
            if it["mode"] != "run":
                continue
            rr = res[it["step"]]
            where = f"{it['field']} ({name})"
            got = norm_lines(rr["output"])
            if rr["errored"] and not it["error"]:
                fails.append((where, f"a ```{it['block']['tag']} block stopped with an error; mark it "
                                     "`error` if the error is the point", got[-6:]))
            if it["error"] and not rr["errored"]:
                fails.append((where, f"a ```{it['block']['tag']} block is marked `error` but ran without one", []))
            exp = norm_lines("\n".join(it["out"]["body"])) if it["out"] else None
            if got and exp is None:
                fails.append((where, "the block prints output but no ```output block follows it "
                                     "(python check/code_gate.py --write)", got[:6]))
            elif exp is not None and not got:
                fails.append((where, "the block prints nothing, but an ```output block follows it", []))
            elif exp is not None and exp != got:
                diff = list(difflib.unified_diff(exp, got, "record", "fresh run", lineterm="", n=1))
                fails.append((where, "the ```output block differs from a fresh run", diff[2:]))
    return fails, plans, stats


# ---------------------------------------------------------------- --write: edit the raw YAML by position

def _node_at(node, path):
    for k in path:
        if isinstance(node, yaml.MappingNode):
            node = next((v for kn, v in node.value if kn.value == k), None)
        elif isinstance(node, yaml.SequenceNode) and isinstance(k, int) and k < len(node.value):
            node = node.value[k]
        else:
            return None
        if node is None:
            return None
    return node


def _get(d, path):
    for k in path:
        d = d[k]
    return d


def _set(d, path, v):
    for k in path[:-1]:
        d = d[k]
    d[path[-1]] = v


def new_field_text(text, items, results_by_step, extra):
    """The field with every output block made to match its fresh run."""
    lines = text.split("\n")
    edits = []   # (start, end_exclusive, replacement lines)
    for it in items:
        b, out = it["block"], it["out"]
        indent = " " * b["indent"]
        want = None
        if it["mode"] == "run":
            got = norm_lines(results_by_step[it["step"]]["output"])
            want = got or None
        if want:
            longest = max((len(m) for l in want for m in re.findall(r"`+", l)), default=0)
            fence = "`" * max(3, longest + 1)
            block = [indent + fence + "output", *[(indent + l) if l else "" for l in want], indent + fence]
        if out is not None and want is None:
            edits.append((b["end"] + 1, out["end"] + 1, []))
        elif out is not None:
            old = lines[out["start"]:out["end"] + 1]
            if [l.rstrip() for l in old] != [l.rstrip() for l in block]:
                edits.append((out["start"], out["end"] + 1, block))
        elif want:
            edits.append((b["end"] + 1, b["end"] + 1, [""] + block))
    for start, end, rep in sorted(edits, key=lambda e: e[0], reverse=True):
        lines[start:end] = rep
    return "\n".join(lines)


def write_record(path, rid, r_parsed, plans):
    """Rewrite one record's output blocks in place. Returns a list of edited field labels."""
    with open(path, encoding="utf-8", newline="") as fh:
        raw = fh.read()
    if "\r\n" in raw:
        raise RuntimeError(f"{path}: CRLF line endings; refusing to edit")
    data = yaml.safe_load(raw)
    expected = yaml.safe_load(raw)
    root = yaml.compose(raw)
    by_field = {}
    for items, res, extra in plans:
        for it in items:
            by_field.setdefault(tuple(it["path"]), {"label": it["field"], "items": [], "res": res})
            by_field[tuple(it["path"])]["items"].append(it)
            by_field[tuple(it["path"])]["res"] = res
    edits, changed = [], []
    for pth, f in by_field.items():
        old = _get(data, pth)
        new = new_field_text(old, f["items"], f["res"], [])
        if new == old:
            continue
        node = _node_at(root, pth)
        if node is None or not isinstance(node, yaml.ScalarNode) or node.style != "|":
            raise RuntimeError(f"{rid} {f['label']}: code must be authored in a literal block "
                               "(`key: |`) for --write to edit it")
        hdr = node.start_mark.line
        rl = raw.split("\n")
        keep_nl = old.endswith("\n")
        old_lines = (old[:-1] if keep_nl else old).split("\n")
        new_lines = (new[:-1] if keep_nl else new).split("\n")
        body = rl[hdr + 1:hdr + 1 + len(old_lines)]
        ind = next((len(l) - len(l.lstrip(" ")) for l in body if l.strip()), None)
        if ind is None or any((l.strip() and (l[:ind].strip() or l[ind:] != v)) or (not l.strip() and v.strip())
                              for l, v in zip(body, old_lines)) or len(body) != len(old_lines):
            raise RuntimeError(f"{rid} {f['label']}: could not map the field to its lines in the file")
        rep = [(" " * ind + l) if l else "" for l in new_lines]
        edits.append((hdr + 1, hdr + 1 + len(old_lines), rep))
        _set(expected, pth, new)
        changed.append(f["label"])
    if not edits:
        return []
    rl = raw.split("\n")
    for start, end, rep in sorted(edits, key=lambda e: e[0], reverse=True):
        rl[start:end] = rep
    new_raw = "\n".join(rl)
    if yaml.safe_load(new_raw) != expected:
        raise RuntimeError(f"{rid}: the edited file does not parse back to the intended record; nothing written")
    stamp = time.strftime("%Y%m%d-%H%M%S")
    dest = os.path.join(BACKUP, stamp, os.path.relpath(os.path.abspath(path), REPO).replace("..", "_"))
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    shutil.copyfile(path, dest)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(new_raw)
    return changed


# ---------------------------------------------------------------- entry points

def build_problems(recs: dict) -> list:
    """Blocking messages for check/build.py: one scan per record; the gate only where code is."""
    out = []
    for rid, r in sorted(recs.items()):
        raw = r.get("_raw") or ""
        if "```" in raw:
            bad = codeblocks.unknown_tags(raw)
            if bad:
                out.append(f"{rid}: fence tag(s) {', '.join(bad)} not known - code is ```r, ```output "
                           "or ```sh; arithmetic ```working; tables ```table")
        if not has_code_raw(raw):
            continue
        fails, _, _ = gate_record(rid, r, use_cache=True)
        for where, msg, _diff in fails:
            out.append(f"{rid}: code gate: {where + ': ' if where else ''}{msg}"
                       + (f" (python check/code_gate.py --check --record {r.get('_path', '')})"
                          if _diff else ""))
    return out


def _load(path):
    with open(path, encoding="utf-8") as fh:
        raw = fh.read()
    r = yaml.safe_load(raw) or {}
    r["_raw"], r["_file"] = raw, path
    return r


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    ap.add_argument("--subject", action="append", default=[], help="a book (S52-R1) or subject (S52)")
    ap.add_argument("--record", action="append", default=[], help="a record file, anywhere")
    ap.add_argument("--no-cache", action="store_true")
    a = ap.parse_args(argv)

    paths = [os.path.abspath(p) for p in a.record]
    if not paths:
        for dp, _, fs in os.walk(RECORDS):
            paths += [os.path.join(dp, f) for f in sorted(fs) if f.endswith((".yml", ".yaml"))]
    recs = []
    for p in sorted(paths):
        r = _load(p)
        rid = r.get("concept_id", os.path.basename(p))
        if a.subject and not any(rid.startswith(s + "-") for s in a.subject):
            continue
        if has_code_raw(r["_raw"]):
            recs.append((p, rid, r))
    t0, n_fail, n_sess, n_hit = time.time(), 0, 0, 0
    for p, rid, r in recs:
        fails, plans, st = gate_record(rid, r, use_cache=not a.no_cache)
        n_sess, n_hit = n_sess + st["sessions"], n_hit + st["cached"]
        if a.write and plans:
            try:
                changed = write_record(p, rid, r, plans)
            except RuntimeError as e:
                print(f"  {rid}: NOT WRITTEN - {e}")
                n_fail += 1
                continue
            if changed:
                print(f"  {rid}: output blocks written in {', '.join(changed)}")
            fails, plans, st = gate_record(rid, _load(p), use_cache=True)
        for where, msg, diff in fails:
            n_fail += 1
            print(f"  FAIL {rid}: {where + ': ' if where else ''}{msg}")
            for l in diff[:40]:
                print("      " + l)
    print(f"code gate: {len(recs)} record(s) with code, {n_sess} session(s) ({n_hit} cached), "
          f"{n_fail} failure(s), {time.time() - t0:.1f}s")
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
