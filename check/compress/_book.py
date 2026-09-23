"""Which book the compression tools are working on, and where its files live.

Shared by prepare.py, restore.py and validate.py. Every tool takes `--subject <ID>`:

    B0        Book 0. Records from check/records/B0, section labels (A1, C7, ...) from the
              Book 0 outline, working folder books/B0/compress/.
    S01-R1    one rung of a subject: the book the series prints. Records from
              check/records/S01, only those whose concept_id starts `S01-R1-`, labelled by
              their own concept_id (S01-R1-C01), working folder books/S01-R1/compress/.

`--out DIR` sends the working folder somewhere else and `--records DIR` reads records from
somewhere else. Both exist for testing - regenerating a committed file into a temp folder and
diffing it is how "Book 0's behaviour is unchanged" is checked rather than asserted.
"""
import os
import re
import sys

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
CHECK = os.path.dirname(HERE)
REPO = os.path.dirname(CHECK)
sys.path.insert(0, CHECK)
import build  # noqa: E402

BOOK_ID = re.compile(r"^(B0|S[0-9]{2}-R[0-9])$")


def take_opts(argv):
    """Pull `--subject X`, `--out D`, `--records D` out of argv; return (opts, rest)."""
    opts, rest, i = {}, [], 0
    while i < len(argv):
        a = argv[i]
        key = a[2:].split("=")[0] if a.startswith("--") else None
        if key in ("subject", "out", "records"):
            if "=" in a:
                opts[key] = a.split("=", 1)[1]
            else:
                opts[key] = argv[i + 1]
                i += 1
        else:
            rest.append(a)
        i += 1
    if "subject" not in opts:
        sys.exit("--subject <ID> is required, e.g. --subject B0 or --subject S01-R1")
    if not BOOK_ID.match(opts["subject"]):
        sys.exit(f"--subject {opts['subject']}: expected B0 or a rung book such as S01-R1 "
                 "(the compression pass runs one book at a time)")
    return opts, rest


class Book:
    def __init__(self, book_id, out=None, records=None):
        self.id = book_id
        self.subject = book_id.split("-")[0]
        self.is_b0 = book_id == "B0"
        self.work = os.path.abspath(out) if out else os.path.join(REPO, "books", book_id, "compress")
        self.records_dir = os.path.abspath(records) if records else \
            os.path.join(CHECK, "records", self.subject)
        self.b0_records_dir = os.path.join(CHECK, "records", "B0") if not records or not self.is_b0 \
            else self.records_dir
        self._outline = None

    @classmethod
    def from_opts(cls, opts):
        return cls(opts["subject"], opts.get("out"), opts.get("records"))

    # ------------------------------------------------------------ records

    def path_of(self, cid):
        """A record's file. Records are named by concept_id; fall back to a scan if not."""
        p = os.path.join(self.records_dir, f"{cid}.yml")
        if os.path.exists(p):
            return p
        for fn in sorted(os.listdir(self.records_dir)):
            if fn.endswith((".yml", ".yaml")):
                with open(os.path.join(self.records_dir, fn), encoding="utf-8") as fh:
                    r = yaml.safe_load(fh) or {}
                if r.get("concept_id") == cid:
                    return os.path.join(self.records_dir, fn)
        sys.exit(f"no record {cid} in {self.records_dir}")

    def load(self, cid):
        with open(self.path_of(cid), encoding="utf-8") as fh:
            return yaml.safe_load(fh)

    def mine(self):
        """[(concept_id, record)] for this book, in reading order."""
        out = []
        if not os.path.isdir(self.records_dir):
            return out
        for fn in sorted(os.listdir(self.records_dir)):
            if not fn.endswith((".yml", ".yaml")):
                continue
            with open(os.path.join(self.records_dir, fn), encoding="utf-8") as fh:
                r = yaml.safe_load(fh) or {}
            cid = r.get("concept_id", "")
            if cid.startswith(f"{self.id}-"):
                out.append((cid, r))
        out.sort(key=lambda t: (t[1].get("rung", 0), t[1].get("sequence", 0), t[0]))
        return out

    # ------------------------------------------------------------ labels

    def outline(self):
        if self._outline is None:
            self._outline = build.load_book0_outline()
        return self._outline

    def b0_labels(self):
        """{record sequence: outline label}, e.g. 15 -> C1. The outline is the one source."""
        return {s["index"]: s["id"] for part in self.outline() for s in part["sections"]}

    def label(self, cid, r):
        """Book 0: the outline label (C7). A rung book: the record's own id (S01-R1-C03)."""
        if self.is_b0:
            return self.b0_labels().get(r.get("sequence"), cid)
        return r.get("concept_id", cid)

    def f(self, name):
        return os.path.join(self.work, name)


def section_of(filename):
    """`A4-pass1-prose.yml` -> A4, `S01-R1-C02-final-prose.yml` -> S01-R1-C02."""
    base = os.path.basename(filename)
    m = re.match(r"^(.+?)-(?:pass1|final|[a-z0-9]+)-prose\.ya?ml$", base)
    if m and m.group(1) != base:
        return m.group(1)
    return base.split("-")[0]
