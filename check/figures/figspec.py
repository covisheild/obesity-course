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
                              - a `curves` formula that misses its series or is not finite
                                on its range; an `areas` entry whose `equals` is not its integral
    spec_hash(rec, fig)     fingerprint of the resolved spec and the book's palette; draw.py
                            writes it beside the PNG as <file>.spec.json, and the build blocks
                            when the two differ (the text changed and the picture did not)
    palette_for(book_id)    the book's figure colours, from the same Part hue its PDF cover uses

Pure Python and PyYAML, so `check/build.py --check` needs no matplotlib.

Spec shape (see check/schema/concept.schema.json, figures[].spec):

    spec:
      kind: line                 # line | scatter | bar (bars may be negative) | step
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
      bands:                                 # optional: shaded ranges; y0, y1 checked like data
        - {y0: 88, y1: 90, label: "target range"}
      curves:                                # optional: a formula over its own x range
        - {y: "y = 92 - 0.5*x", x0: 0, x1: 8, label: "the rule", series: <name>}   # series: checked like a fit
      areas:                                 # optional: shaded between y and `to` (default the axis)
        - {y: "y = 300 - 10*x", x0: 0, x1: 30, to: 0, equals: 4500, label: "4,500 kcal gained"}
      refs:                                  # optional: a reference line at a stated value
        - {x: 70, label: "expected value 70"}   # or {y: ...}
    and on a literal series, `marker: none` draws it as a bare line (a fitted slope, not points).
    Every constant, x0/x1, `to`, `equals`, ref value and label number is checked like data; `equals`
    is the signed integral of (y - to) over [x0, x1]. Bars may be negative (drawn from a zero line);
    two or more drawn fits each take their series' colour.
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
        series = [{"name": s.get("name", ""), "y_raw": [str(v) for v in s.get("y") or []],
                   **({"marker": s["marker"]} if s.get("marker") else {})}
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
        if s.get("marker") not in (None, "none"):
            raise ValueError(f"series '{s['name']}': marker must be 'none' or left out")
    bands = []
    for b in spec.get("bands") or []:
        y0, y1 = _num(b.get("y0")), _num(b.get("y1"))
        if y0 is None or y1 is None:
            raise ValueError(f"spec.bands: y0 and y1 must be numbers, got {b}")
        bands.append({"y0": y0, "y1": y1, "y0_raw": str(b.get("y0")), "y1_raw": str(b.get("y1")),
                      "label": b.get("label", "")})
    out = {"kind": kind, "x_raw": x_raw, "x": None if categorical else xs, "series": series,
            "x_label": spec.get("x_label", ""), "y_label": spec.get("y_label", ""),
            "title": spec.get("title", ""), "relations": spec.get("relations") or [],
            "labels": spec.get("labels") or [], "derived": spec.get("derived") or [],
            "y_scale": spec.get("y_scale", "linear"), "value_labels": bool(spec.get("value_labels")),
            "y_range": spec.get("y_range"), "size": spec.get("size", [6.2, 3.0])}
    # Everything below is added only when it is declared or used, so a spec without it keeps the
    # fingerprint it was drawn with (added 24 September 2026 for S02-R1).
    if bands:
        out["bands"] = bands
    curves = [_curve(c, "curves", series) for c in spec.get("curves") or []]
    areas = [_area(a) for a in spec.get("areas") or []]
    refs = [_ref(r) for r in spec.get("refs") or []]
    if (curves or areas) and categorical:
        raise ValueError("spec.curves and spec.areas need numeric x")
    for key, val in (("curves", curves), ("areas", areas), ("refs", refs)):
        if val:
            out[key] = val
    if kind == "bar" and any(v < 0 for s in series for v in s["y"]):
        out["signed_bars"] = True       # drawn from a zero line, not a zero floor
    if sum(1 for r in out["relations"] if r.get("fit") and r.get("draw")) > 1:
        out["fit_colours"] = "series"   # two or more drawn fits: each in its own series' colour
    return out


def _rhs(expr, where):
    """The expression after '=' in 'y = ...', or a bare number/expression as given."""
    s = str(expr).strip()
    lhs, eq, rhs = s.partition("=")
    if eq and lhs.strip() != "y":
        raise ValueError(f"{where}: '{s}' must read 'y = <expression in x>'")
    return (rhs if eq else s).strip()


def _span(d, where):
    x0, x1 = _num(d.get("x0")), _num(d.get("x1"))
    if x0 is None or x1 is None or not x0 < x1:
        raise ValueError(f"{where}: x0 and x1 must be numbers with x0 < x1, got {d}")
    return {"x0": x0, "x1": x1, "x0_raw": str(d.get("x0")), "x1_raw": str(d.get("x1"))}


def _curve(c, key, series):
    if not c.get("y"):
        raise ValueError(f"spec.{key}: each curve needs y: 'y = <expression in x>'")
    if c.get("series") and c["series"] not in [s["name"] for s in series]:
        raise ValueError(f"spec.{key}: series '{c['series']}' is not a series of this figure")
    return {"y": str(c["y"]), "rhs": _rhs(c["y"], f"spec.{key}"), **_span(c, f"spec.{key}"),
            "label": c.get("label", ""), "series": c.get("series", "")}


def _area(a):
    if not a.get("y"):
        raise ValueError("spec.areas: each area needs y: 'y = <expression in x>' (its upper edge)")
    to = a.get("to", 0)
    out = {"y": str(a["y"]), "rhs": _rhs(a["y"], "spec.areas"), "to": str(to),
           "to_rhs": _rhs(to, "spec.areas"), **_span(a, "spec.areas"), "label": a.get("label", "")}
    if a.get("equals") is not None:
        if _num(a["equals"]) is None:
            raise ValueError(f"spec.areas: equals must be a number, got {a['equals']}")
        out["equals"] = str(a["equals"])
    return out


def _ref(r):
    axis = [k for k in ("x", "y") if r.get(k) is not None]
    if len(axis) != 1 or _num(r[axis[0]]) is None:
        raise ValueError(f"spec.refs: each reference line needs exactly one of x or y, a number; got {r}")
    return {"axis": axis[0], "at": _num(r[axis[0]]), "raw": str(r[axis[0]]), "label": r.get("label", "")}


def samples(rhs, names, x0, x1, n=200):
    """(xs, ys) of a formula over [x0, x1], for drawing a curve or shading an area."""
    xs = [x0 + (x1 - x0) * k / n for k in range(n + 1)]
    return xs, [float(evaluate(rhs, {**names, "x": xv})) for xv in xs]


def integral(rhs, to_rhs, names, x0, x1, n=2000):
    """Signed area of (rhs - to_rhs) over [x0, x1], by Simpson's rule on n (even) strips."""
    h = (x1 - x0) / n
    tot = 0.0
    for k in range(n + 1):
        xv = x0 + k * h
        f = evaluate(rhs, {**names, "x": xv}) - evaluate(to_rhs, {**names, "x": xv})
        tot += f * (1 if k in (0, n) else 4 if k % 2 else 2)
    return tot * h / 3


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
    for b in res.get("bands") or []:
        need({abs(b["y0"]), abs(b["y1"])}, "shades a band from")
        need(numbers_in(b["label"]), f"prints the band '{b['label']}' with")
    for c in res.get("curves") or []:
        need(_expr_numbers(c["rhs"]), f"draws the curve '{c['y']}' with constants")
        need({abs(c["x0"]), abs(c["x1"])}, f"draws the curve '{c['y']}' from x =")
        need(numbers_in(c["label"]), f"prints the key '{c['label']}' with")
    for a in res.get("areas") or []:
        need(_expr_numbers(a["rhs"]) | _expr_numbers(a["to_rhs"]),
             f"shades the area under '{a['y']}' with constants")
        need({abs(a["x0"]), abs(a["x1"])}, f"shades the area under '{a['y']}' from x =")
        need(numbers_in(a["label"]), f"prints the area '{a['label']}' with")
        if "equals" in a:
            need({abs(_num(a["equals"]))}, f"states the area under '{a['y']}' as")
    for r in res.get("refs") or []:
        need({abs(r["at"])}, f"draws a reference line at {r['axis']} =")
        need(numbers_in(r["label"]), f"prints the reference line '{r['label']}' with")
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
            elif _num(want) == 0:
                # A difference asserted to be zero. The right side "0" carries no decimals, so
                # _close would allow +-0.5 and pass a difference of 0.4 (found 24 Sep 2026). The
                # precision comes from the constants on the left instead; with none, it is exact.
                places = max([_decimals(c) for c in re.findall(r"\d+\.\d+", lhs)] or [None]) \
                    if re.search(r"\d+\.\d+", lhs) else None
                ok = abs(got) <= (0.5 * 10 ** -places if places is not None else 1e-9 * max(1, abs(got)))
            else:
                ok = _close(got, want)
            if not ok:
                probs.append(f"{tag}: check '{rel['check']}' is false - the left side is {got:.6g}")
        else:
            probs.append(f"{tag}: a relation must be a `fit` or a `check`")

    # 3a. A curve is a drawn relation over its own range: it must evaluate everywhere on that range,
    #     and when it names a series, pass through every point of it inside the range, like a `fit`.
    #     An area's `equals` is its signed integral, (y - to) over [x0, x1], at the written precision.
    for c in res.get("curves") or []:
        try:
            _, ys = samples(c["rhs"], names, c["x0"], c["x1"])
        except Exception as e:
            probs.append(f"{tag}: curve '{c['y']}' cannot be evaluated over [{c['x0_raw']}, {c['x1_raw']}] ({e})")
            continue
        if not all(math.isfinite(v) for v in ys):
            probs.append(f"{tag}: curve '{c['y']}' is not finite everywhere on [{c['x0_raw']}, {c['x1_raw']}]")
        if res["y_scale"] == "log" and any(v <= 0 for v in ys):
            probs.append(f"{tag}: curve '{c['y']}' reaches zero or below, which a log axis cannot show")
        if c["series"]:
            s = next(s for s in res["series"] if s["name"] == c["series"])
            for xv, yraw in zip(res["x"], s["y_raw"]):
                if c["x0"] <= xv <= c["x1"]:
                    got = evaluate(c["rhs"], {**names, "x": xv})
                    if not _close(got, yraw):
                        probs.append(f"{tag}: curve '{c['y']}' gives {got:.6g} at x = {xv:g}, "
                                     f"but the figure plots {yraw}")
    for a in res.get("areas") or []:
        try:
            samples(a["rhs"], names, a["x0"], a["x1"])
            samples(a["to_rhs"], names, a["x0"], a["x1"])
            got = integral(a["rhs"], a["to_rhs"], names, a["x0"], a["x1"])
        except Exception as e:
            probs.append(f"{tag}: area under '{a['y']}' cannot be evaluated ({e})")
            continue
        if "equals" in a and not _close(got, a["equals"]):
            probs.append(f"{tag}: area under '{a['y']}' from {a['x0_raw']} to {a['x1_raw']} is "
                         f"{got:.6g}, not {a['equals']} (equals is the signed area, y minus to)")

    # 4. Honest geometry.
    if res.get("signed_bars"):
        lo = min(v for s in res["series"] for v in s["y"])
        hi = max(v for s in res["series"] for v in s["y"])
        if res["y_range"] and not (float(res["y_range"][0]) <= min(lo, 0)
                                   and float(res["y_range"][1]) >= max(hi, 0)):
            probs.append(f"{tag}: a bar chart with negative bars needs an axis that holds zero and "
                         "every bar whole (a bar's length is its value)")
    elif res["kind"] == "bar" and res["y_range"] and float(res["y_range"][0]) != 0:
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
