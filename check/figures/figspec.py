"""Figure specs: the data a figure draws, declared in the record, and the checks that tie it to the text.

A figure in a subject book is never drawn by hand and never from numbers typed into a script. Its
record carries a `spec` under the figure's entry in `figures:`, and `check/figures/draw.py` draws
the picture from that spec alone. This module is the part both sides share:

    resolve(rec, fig)       the spec with its data filled in (from the record's own ```table blocks
                            when it says `from_table`), as plain numbers and strings
    verify(rec, fig)        list of problems, each one blocking in check/build.py:
                              - a number the figure plots or prints (data, labels, caption, axis
                                titles, relation constants) that the record's reader-facing text
                                does not state and no declared `derived` entry works out
                              - a `derived` entry whose arithmetic does not give its value
                              - a `fit` relation (y = a + b*x ...) that a plotted point breaks
                              - a `check` identity (a total, a ratio) that does not hold
                              - a bar chart whose bars do not start at zero
    spec_hash(rec, fig)     fingerprint of the resolved spec and the book's palette; draw.py
                            writes it beside the PNG as <file>.spec.json, and the build blocks
                            when the two differ (the text changed and the picture did not)
    palette_for(book_id)    the book's figure colours, from the same Part hue its PDF cover uses

Pure Python and PyYAML, so `check/build.py --check` needs no matplotlib.

Spec shape (see check/schema/concept.schema.json, figures[].spec):

    spec:
      kind: line                 # line | scatter | bar | step
      x_label: weeks
      y_label: weight (kg)
      from_table: {block: 0, x: 0, y: [1]}   # or literal  x: [...]  series: [{name, y: [...]}]
      relations:
        - fit: "y = 92 - 0.5*x"  # every point of the series must satisfy it; draw: true draws it
        - check: "y[0] - y[-1] = 4"
      labels:
        - {text: "0.5 kg a week", at: [4, 90]}
      derived:
        - {value: "4", from: "92 - 88"}      # a printed number the prose does not state
"""
import ast
import hashlib
import json
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CHECK = os.path.dirname(HERE)
ROOT = os.path.dirname(CHECK)
SPEC_VERSION = 1   # bump when the drawing of an unchanged spec changes, so every figure redraws


# ---------------------------------------------------------------- the book's colours

def _hsl(h, s, l):
    import colorsys
    r, g, b = colorsys.hls_to_rgb((h % 360) / 360, l / 100, s / 100)
    return "#{:02x}{:02x}{:02x}".format(round(r * 255), round(g * 255), round(b * 255))


def _lum(hexc):
    c = [int(hexc[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    c = [v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4 for v in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def contrast(a, b="#ffffff"):
    la, lb = sorted((_lum(a), _lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def _at_least(h, s, l, ratio):
    """The colour at hue h, darkened until it reaches `ratio` against white."""
    while l > 5 and contrast(_hsl(h, s, l)) < ratio:
        l -= 1
    return _hsl(h, s, l)


def book_part(book_id):
    """The map Part a book belongs to, from map/BOOKS.yml (the list the PDF cover reads)."""
    import yaml
    with open(os.path.join(ROOT, "map", "BOOKS.yml"), encoding="utf-8") as fh:
        books = yaml.safe_load(fh)["books"]
    entry = next((b for b in books if b["id"] == book_id), None)
    if entry is None:
        sid = book_id.split("-")[0]           # a subject id: take its first rung's Part
        entry = next((b for b in books if b.get("subject") == sid), None)
    if entry is None:
        raise SystemExit(f"figures: {book_id} is not in map/BOOKS.yml")
    return entry


def palette_for(book_id):
    """Figure colours for a book, from the Part hue in check/pdf/series.yml.

    The cover and the running heads use the same hue (check/pdf/make_pdf.py `theme`), so a book's
    figures sit in its own colour family. Marks and text are darkened until they pass WCAG contrast
    on the white page: 4.5:1 for anything carrying text, 3:1 for lines and markers. The second
    series takes a hue 150 degrees round the wheel and a different lightness, so two series part
    in colour, in greyscale and for the common colour-vision deficiencies; the third is the book's
    dark ink, drawn dashed. Axes and grid are neutral greys, never the book's hue.
    """
    import yaml
    sys.path.insert(0, os.path.join(CHECK, "pdf"))
    import make_pdf
    with open(os.path.join(CHECK, "pdf", "series.yml"), encoding="utf-8") as fh:
        series = yaml.safe_load(fh)
    t = make_pdf.theme(book_part(book_id), series)
    h = t["hue"]
    return {
        "book": book_id, "hue": h,
        "primary": _at_least(h, 70, 42, 4.5),         # the data, and labels about it
        "secondary": _at_least(h + 150, 75, 34, 4.5),  # a second series or the drawn relation
        "tertiary": t["ink"],                          # a third series, dashed
        "fill": _hsl(h, 60, 90),                       # areas and bars behind a line
        "ink": "#1d2327",                              # titles and annotations (style.css --text)
        "muted": "#5b6770",                            # tick labels (style.css --muted)
        "axis": "#8a9097",                             # spines and ticks: 3:1 on white
        "grid": "#e4e7ea",                             # decorative only
        "surface": "#ffffff",
    }


# ---------------------------------------------------------------- the record's own text

_WORDS = {w: i for i, w in enumerate(
    "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen "
    "fifteen sixteen seventeen eighteen nineteen twenty".split())}
_WORDS.update({"thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80,
               "ninety": 90, "hundred": 100, "thousand": 1000, "half": 0.5, "quarter": 0.25,
               "twice": 2, "double": 2, "once": 1})
_NUM = re.compile(r"(?<![\w.])\d[\d,]*(?:\.\d+)?|(?<![\w\d])\.\d+")


def reader_text(rec):
    """Every field a reader reads, except the figure's own caption (which is checked against this)."""
    parts = [(rec.get("definition") or {}).get("text"), rec.get("simplified_explanation")]
    ills = list(rec.get("illustrations") or [])
    if rec.get("illustration"):
        ills.insert(0, rec["illustration"])
    for ill in ills:
        if isinstance(ill, dict):
            parts += [ill.get("body"), ill.get("analogy_breaks_when")]
    for m in rec.get("must_know") or []:
        if isinstance(m, dict):
            parts.append(m.get("point"))
    for ex in (rec.get("exercises") or []) + (rec.get("practice") or []):
        if isinstance(ex, dict):
            parts += [ex.get("prompt"), ex.get("answer")]
    return "\n".join(str(p) for p in parts if p)


def _strip_notation(s):
    """Exponents and log bases are notation, not numbers the figure states: 10^7, kg/m^2, log10."""
    s = re.sub(r"\^\s*\(?-?[\d.]+\)?", "", str(s))
    return re.sub(r"\blog\s?(10|2)\b", "log", s)


def numbers_in(text):
    """The numbers a piece of text states, as floats (absolute values; signs are words here)."""
    text = _strip_notation(text)
    out = set()
    for m in _NUM.finditer(text):
        raw = m.group(0).rstrip(",")
        try:
            out.add(abs(float(raw.replace(",", ""))))
        except ValueError:
            pass
    for w in re.findall(r"[a-z]+", text.lower()):
        if w in _WORDS:
            out.add(float(_WORDS[w]))
    return out


def _decimals(raw):
    s = str(raw)
    m = re.search(r"\.(\d+)", s)
    return len(m.group(1)) if m else 0


def _num(raw):
    try:
        return float(str(raw).replace(",", "").replace("−", "-").strip())
    except ValueError:
        return None


# ---------------------------------------------------------------- resolving a spec

def _tables(rec):
    bodies = []
    ills = list(rec.get("illustrations") or [])
    if rec.get("illustration"):
        ills.insert(0, rec["illustration"])
    for ill in ills:
        if isinstance(ill, dict):
            bodies.append(ill.get("body") or "")
    blocks = re.findall(r"```table\n(.*?)```", "\n".join(bodies), re.S)
    out = []
    for b in blocks:
        rows = []
        for line in b.strip().split("\n"):
            if not line.strip():
                continue
            if "|" in line:
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
            else:
                cells = re.split(r" {2,}", line.strip())
            rows.append(cells)
        out.append(rows)
    return out


def resolve(rec, fig):
    """The spec as data: {'kind', 'x', 'x_raw', 'series': [{'name','y','y_raw'}], ...}.

    Raises ValueError with a reader-sized message when the spec cannot be resolved.
    """
    spec = dict(fig.get("spec") or {})
    kind = spec.get("kind", "line")
    if kind not in ("line", "scatter", "bar", "step"):
        raise ValueError(f"spec.kind '{kind}' is not line, scatter, bar or step")
    ft = spec.get("from_table")
    if ft:
        tabs = _tables(rec)
        n = int(ft.get("block", 0))
        if n >= len(tabs):
            raise ValueError(f"spec.from_table.block {n}: the record has {len(tabs)} ```table block(s)")
        head, rows = tabs[n][0], tabs[n][1:]
        xc, ycs = int(ft.get("x", 0)), ft.get("y", [1])
        ycs = [ycs] if isinstance(ycs, int) else list(ycs)
        try:
            x_raw = [r[xc] for r in rows]
            series = [{"name": head[c], "y_raw": [r[c] for r in rows]} for c in ycs]
        except IndexError:
            raise ValueError(f"spec.from_table: a row of table {n} is shorter than the columns named")
        spec.setdefault("x_label", head[xc])
        if len(series) == 1:
            spec.setdefault("y_label", head[ycs[0]])
    else:
        x_raw = [str(v) for v in (spec.get("x") or [])]
        series = [{"name": s.get("name", ""), "y_raw": [str(v) for v in s.get("y") or []]}
                  for s in spec.get("series") or []]
    if not x_raw or not series:
        raise ValueError("spec has no data: give from_table, or x and series")
    xs = [_num(v) for v in x_raw]
    categorical = any(v is None for v in xs)
    if categorical and kind != "bar":
        raise ValueError(f"spec.kind {kind} needs numeric x; got {x_raw}")
    for s in series:
        if len(s["y_raw"]) != len(x_raw):
            raise ValueError(f"series '{s['name']}' has {len(s['y_raw'])} values for {len(x_raw)} x values")
        s["y"] = [_num(v) for v in s["y_raw"]]
        if None in s["y"]:
            raise ValueError(f"series '{s['name']}' has a value that is not a number: {s['y_raw']}")
    return {"kind": kind, "x_raw": x_raw, "x": None if categorical else xs, "series": series,
            "x_label": spec.get("x_label", ""), "y_label": spec.get("y_label", ""),
            "title": spec.get("title", ""), "relations": spec.get("relations") or [],
            "labels": spec.get("labels") or [], "derived": spec.get("derived") or [],
            "y_scale": spec.get("y_scale", "linear"), "value_labels": bool(spec.get("value_labels")),
            "y_range": spec.get("y_range"), "size": spec.get("size", [6.2, 3.0])}


# ---------------------------------------------------------------- safe arithmetic

_FUNCS = {"sum": sum, "min": min, "max": max, "len": len, "abs": abs, "round": round,
          "sqrt": math.sqrt, "log10": math.log10, "log": math.log, "exp": math.exp,
          "mean": lambda v: sum(v) / len(v)}
_OK = (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Constant, ast.Name, ast.Load, ast.Call,
       ast.Subscript, ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow, ast.USub, ast.UAdd, ast.Mod,
       ast.Slice)


def evaluate(expr, names):
    tree = ast.parse(str(expr).strip().replace("^", "**").replace("−", "-").replace("×", "*"), mode="eval")
    for node in ast.walk(tree):
        if not isinstance(node, _OK):
            raise ValueError(f"'{expr}': {type(node).__name__} is not allowed")
        if isinstance(node, ast.Name) and node.id not in names and node.id not in _FUNCS:
            raise ValueError(f"'{expr}': unknown name '{node.id}'")
    return eval(compile(tree, "<spec>", "eval"), {"__builtins__": {}}, {**_FUNCS, **names})  # noqa: S307


def _names(res):
    n = {"x": res["x"] or []}
    for i, s in enumerate(res["series"], 1):
        n[f"y{i}"] = s["y"]
    n["y"] = res["series"][0]["y"]
    return n


def _close(got, want_raw):
    places = _decimals(want_raw)
    want = _num(want_raw)
    tol = 0.5 * 10 ** -places + 1e-9 + abs(want) * 1e-9
    return abs(got - want) <= tol


def _expr_numbers(expr):
    """Constants written into a relation, minus the ones that are notation (the 2 in x^2)."""
    return numbers_in(re.sub(r"\b(y|x)\d\b", "", str(expr)))


# ---------------------------------------------------------------- the check

def verify(rec, fig):
    """Problems with one figure's spec, each a sentence. Empty means the figure is tied to the text."""
    try:
        res = resolve(rec, fig)
    except ValueError as e:
        return [f"figure '{fig.get('file')}': {e}"]
    tag = f"figure '{fig.get('file')}'"
    probs = []
    text_nums = numbers_in(reader_text(rec))
    names = _names(res)

    # 1. Derived numbers must be worked out correctly, from numbers the text states.
    allowed = set(text_nums)
    for d in res["derived"]:
        raw = str(d.get("value", ""))
        try:
            got = evaluate(d.get("from", ""), names)
        except Exception as e:
            probs.append(f"{tag}: derived {raw} cannot be evaluated ({e})")
            continue
        if _num(raw) is None or not _close(got, raw):
            probs.append(f"{tag}: derived {raw} = {d.get('from')} actually gives {got:.6g}")
            continue
        missing = sorted(v for v in _expr_numbers(d.get("from", "")) if v not in allowed)
        if missing:
            probs.append(f"{tag}: derived {raw} is worked from {missing}, which the text does not state")
        allowed.add(abs(_num(raw)))

    # 2. Every number plotted or printed must be stated or derived.
    def need(values, where):
        bad = sorted({v for v in values if v not in allowed})
        if bad:
            probs.append(f"{tag}: {where} {', '.join(f'{v:g}' for v in bad)} not stated in the "
                         "record's text - state it there, or add a `derived` entry saying how it is worked out")

    if res["x"] is not None:
        need({abs(v) for v in res["x"]}, "plots x =")
    else:
        need(set().union(*(numbers_in(c) for c in res["x_raw"])), "labels categories with")
    for s in res["series"]:
        need({abs(v) for v in s["y"]}, f"plots {s['name'] or 'series'} =")
        need(numbers_in(s["name"]), "names a series with")
    for lab in res["labels"]:
        need(numbers_in(lab.get("text", "")), f"prints '{lab.get('text', '')}' with")
    for rel in res["relations"]:
        need(numbers_in(rel.get("label", "")), f"prints the key '{rel.get('label', '')}' with")
    for key in ("x_label", "y_label", "title"):
        need(numbers_in(res[key]), f"prints its {key.replace('_', ' ')} with")
    need(numbers_in(fig.get("caption", "")), "caption states")
    need(numbers_in(fig.get("alt", "")), "alt text states")

    # 3. Every relation the figure draws or asserts must hold.
    for rel in res["relations"]:
        if "fit" in rel:
            lhs, _, rhs = str(rel["fit"]).partition("=")
            target = next((s for s in res["series"] if s["name"] == rel.get("series")), res["series"][0])
            if res["x"] is None:
                probs.append(f"{tag}: fit '{rel['fit']}' needs numeric x")
                continue
            need(_expr_numbers(rhs), f"draws the relation '{rel['fit']}' with constants")
            for xv, yv, yraw in zip(res["x"], target["y"], target["y_raw"]):
                try:
                    got = evaluate(rhs, {**names, "x": xv})
                except Exception as e:
                    probs.append(f"{tag}: fit '{rel['fit']}' cannot be evaluated ({e})")
                    break
                if not _close(got, yraw):
                    probs.append(f"{tag}: fit '{rel['fit']}' gives {got:.6g} at x = {xv:g}, "
                                 f"but the figure plots {yraw}")
        elif "check" in rel:
            lhs, eq, rhs = str(rel["check"]).rpartition("=")
            if not eq:
                probs.append(f"{tag}: check '{rel['check']}' has no '='")
                continue
            need(_expr_numbers(rhs), f"asserts '{rel['check']}' with")
            try:
                got, want = evaluate(lhs, names), rhs.strip()
            except Exception as e:
                probs.append(f"{tag}: check '{rel['check']}' cannot be evaluated ({e})")
                continue
            if _num(want) is None:
                try:
                    ok = abs(got - evaluate(want, names)) <= 1e-9 * max(1, abs(got))
                except Exception as e:
                    probs.append(f"{tag}: check '{rel['check']}' cannot be evaluated ({e})")
                    continue
            else:
                ok = _close(got, want)
            if not ok:
                probs.append(f"{tag}: check '{rel['check']}' is false - the left side is {got:.6g}")
        else:
            probs.append(f"{tag}: a relation must be a `fit` or a `check`")

    # 4. Honest geometry.
    if res["kind"] == "bar" and res["y_range"] and float(res["y_range"][0]) != 0:
        probs.append(f"{tag}: a bar chart's axis must start at zero (a bar's length is its value)")
    if res["y_scale"] == "log" and any(v <= 0 for s in res["series"] for v in s["y"]):
        probs.append(f"{tag}: a log axis cannot show a value at or below zero")
    return probs


# ---------------------------------------------------------------- freshness

def spec_hash(rec, fig, book_id):
    res = resolve(rec, fig)
    blob = json.dumps({"v": SPEC_VERSION, "spec": res, "palette": palette_for(book_id)},
                      sort_keys=True, default=str)
    return hashlib.sha256(blob.encode()).hexdigest()


def sidecar(fig_dir, file):
    return os.path.join(fig_dir, os.path.splitext(file)[0] + ".spec.json")


def stale(rec, fig, book_id, fig_dir):
    """None if the PNG was drawn from this spec, else why not."""
    path = sidecar(fig_dir, fig["file"])
    if not os.path.exists(path):
        return "has no .spec.json beside it, so nothing shows it was drawn from this spec"
    try:
        with open(path, encoding="utf-8") as fh:
            got = json.load(fh).get("hash")
        want = spec_hash(rec, fig, book_id)
    except (ValueError, OSError) as e:
        return f"cannot be checked ({e})"
    if got != want:
        return "was drawn from an older spec or older text - the picture no longer matches the record"
    return None


def book_of(rec):
    return "B0" if rec.get("subject") == "B0" else f"{rec.get('subject')}-R{rec.get('rung')}"
