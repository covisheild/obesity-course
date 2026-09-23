"""Turn a built booklet into the series PDF: covers, front matter, contents, body, glossary, the
196-book list, back cover.

    python check/pdf/make_pdf.py B0          # after `python check/build.py --subject B0`

`check/build.py --subject <ID>` calls this itself, so the PDF is made on every build. Reads:

    check/_build/<ID>.md         the booklet the build just assembled (body, answers, references)
    check/pdf/series.yml         series-wide text and colours (author, contact, licence, feedback)
    books/<ID>/book.yml          this book's title, version, date, why-this-book, blurb
    map/BOOKS.yml                the 196 books in build order (check/series.py)
    prose/GLOSSARY.md            terms of art; the rows first taught in this book are printed

Writes check/_build/<ID>.pdf (and <ID>-print.html, the exact HTML that was typeset, for
debugging a layout). Engine: WeasyPrint (`pip install weasyprint qrcode`), which needs no TeX.
Fonts are bundled in check/pdf/fonts so every chat's PDF looks the same.

Nothing here changes a word of the book's content. It only lays out what the build produced,
plus front and back matter drawn from the two YAML files above. A book's text is never edited
to make the PDF look better.
"""
import datetime as dt
import hashlib
import html
import math
import os
import random
import re
import subprocess
import sys

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
CHECK = os.path.dirname(HERE)
ROOT = os.path.dirname(CHECK)
BUILD = os.path.join(CHECK, "_build")
sys.path.insert(0, CHECK)

LABELS = {"Definition.": "definition", "In plain terms.": "plain", "Illustration.": "illustration",
          "Where this picture breaks.": "breaks", "Must know points for you.": "mustknow",
          "Practice.": "practice"}


# ---------------------------------------------------------------- inputs

def _yaml(path):
    with open(path, encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def long_date(d):
    if isinstance(d, str):
        d = dt.date.fromisoformat(d)
    return f"{d.day} {d.strftime('%B %Y')}"


def esc(s):
    return html.escape(str(s), quote=True)


def md_inline(text):
    """Series/book YAML text to HTML: paragraphs, **bold**, *italic*. Nothing else is needed."""
    out = []
    for para in re.split(r"\n\s*\n", str(text).strip()):
        p = esc(" ".join(para.split()))
        p = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", p)
        p = re.sub(r"\*(.+?)\*", r"<em>\1</em>", p)
        out.append(f"<p>{p}</p>")
    return "\n".join(out)


def book_list():
    return _yaml(os.path.join(ROOT, "map", "BOOKS.yml"))["books"]


# ---------------------------------------------------------------- colour and covers

def hsl(h, s, l):
    """A hex colour. Hex rather than hsl(): WeasyPrint's SVG renderer ignores hsl() in gradients."""
    import colorsys
    r, g, b = colorsys.hls_to_rgb((h % 360) / 360, l / 100, s / 100)
    return "#{:02x}{:02x}{:02x}".format(round(r * 255), round(g * 255), round(b * 255))


def theme(entry, series):
    hue = series["hues"].get(entry.get("part"), None)
    if hue is None:  # a Part the colour table does not know yet: stable, never a crash
        hue = int(hashlib.md5(entry.get("part", "").encode()).hexdigest(), 16) % 360
        print(f"  [pdf] no hue for part {entry.get('part')!r} in check/pdf/series.yml; using {hue}")
    return {"hue": hue, "ink": hsl(hue, 65, 22), "accent": hsl(hue, 70, 40),
            "accent2": hsl(hue + 40, 75, 45), "tint": hsl(hue, 60, 96), "tint2": hsl(hue, 55, 90),
            "rule": hsl(hue, 45, 80)}


def pattern(entry, hue, w=210, h=297):
    """A generated motif, different for every book and stable across builds (seeded by its id).

    The level picks the family, so the covers of one ladder read as a staircase: dots for the
    ground floor and Introductory, rings for Intermediate, bars for Advanced, arcs for Expert.
    """
    rnd = random.Random(int(hashlib.sha256(entry["id"].encode()).hexdigest(), 16))
    level = entry.get("level", "")
    cols = [hsl(hue, 80, 70), hsl(hue + 40, 85, 65), hsl(hue - 35, 80, 72), hsl(hue + 180, 70, 70)]
    shapes = []
    if level in ("Ground floor", "Introductory"):
        step = 14 if level == "Ground floor" else 16
        for y in range(8, int(h * 0.62), step):
            for x in range(8, w, step):
                if rnd.random() < 0.55:
                    r = rnd.choice([1.2, 2.2, 3.4, 4.6]) * (1.25 if rnd.random() < .12 else 1)
                    shapes.append(f'<circle cx="{x}" cy="{y}" r="{r:.1f}" fill="{rnd.choice(cols)}" '
                                  f'fill-opacity="{rnd.uniform(.35, .95):.2f}"/>')
    elif level == "Intermediate":
        for _ in range(26):
            x, y, r = rnd.uniform(0, w), rnd.uniform(0, h * .6), rnd.uniform(6, 34)
            shapes.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="none" '
                          f'stroke="{rnd.choice(cols)}" stroke-width="{rnd.uniform(.8, 3):.1f}" '
                          f'stroke-opacity="{rnd.uniform(.4, .9):.2f}"/>')
    elif level == "Advanced":
        for i in range(34):
            x = rnd.uniform(-20, w)
            y = rnd.uniform(0, h * .6)
            L = rnd.uniform(20, 90)
            shapes.append(f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{x + L:.1f}" y2="{y - L * .55:.1f}" '
                          f'stroke="{rnd.choice(cols)}" stroke-width="{rnd.uniform(1.5, 6):.1f}" '
                          f'stroke-linecap="round" stroke-opacity="{rnd.uniform(.45, .9):.2f}"/>')
    else:
        cx, cy = rnd.uniform(w * .3, w * .9), rnd.uniform(h * .1, h * .4)
        for i in range(16):
            r = 10 + i * 9
            a0 = rnd.uniform(0, 2 * math.pi)
            a1 = a0 + rnd.uniform(1.2, 4.2)
            x0, y0 = cx + r * math.cos(a0), cy + r * math.sin(a0)
            x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
            large = 1 if (a1 - a0) > math.pi else 0
            shapes.append(f'<path d="M{x0:.1f},{y0:.1f} A{r},{r} 0 {large} 1 {x1:.1f},{y1:.1f}" '
                          f'fill="none" stroke="{rnd.choice(cols)}" stroke-width="{rnd.uniform(1.5, 5):.1f}" '
                          f'stroke-linecap="round" stroke-opacity="{rnd.uniform(.5, .95):.2f}"/>')
    return "\n".join(shapes)


def cover_bg(hue):
    """The cover's background, as CSS: WeasyPrint draws CSS gradients reliably, SVG ones not."""
    return (f"background: linear-gradient(160deg, {hsl(hue, 55, 16)} 0%, {hsl(hue + 18, 60, 24)} 55%, "
            f"{hsl(hue + 38, 62, 32)} 100%);")


def cover_svg(entry, hue, w=210, h=297, faint=False):
    """The generated motif over the background, and a darkening towards the foot for the text."""
    shade = hsl(hue, 55, 10)
    bands = "".join(f'<rect y="{h * (.40 + i * .03):.1f}" width="{w}" height="{h:.0f}" fill="{shade}" '
                    f'fill-opacity="0.09"/>' for i in range(10))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}mm" height="{h}mm">'
            f'<g opacity="{0.22 if faint else 1}">{pattern(entry, hue, w, h)}</g>{bands}</svg>')


def qr_svg(url, colour="#ffffff"):
    try:
        import qrcode
        import qrcode.image.svg
    except ImportError:
        return ""
    img = qrcode.make(url, image_factory=qrcode.image.svg.SvgPathImage, box_size=10, border=1)
    s = img.to_string(encoding="unicode")
    s = re.sub(r'<\?xml[^>]*>', "", s)
    return s.replace('fill="#000000"', f'fill="{colour}"').replace("<svg ", '<svg class="qr" ', 1)


# ---------------------------------------------------------------- body

def body_html(book_id, drop_preamble):
    md_path = os.path.join(BUILD, f"{book_id}.md")
    if not os.path.exists(md_path):
        raise SystemExit(f"no {md_path}: run python check/build.py --subject {book_id} first")
    p = subprocess.run(["pandoc", md_path, "-f", "markdown-yaml_metadata_block", "-t", "html5",
                        "--wrap=none"], capture_output=True, text=True, check=True)
    h = p.stdout
    first_h1 = re.search(r"<h1[^>]*>.*?</h1>", h, re.S)
    if first_h1:
        rest = h[first_h1.end():]
        if drop_preamble:  # the front matter says this, from book.yml; do not print it twice
            m = re.search(r"<h2", rest)
            rest = rest[m.start():] if m else rest
        h = rest
    # the answers appendix is an <h1>: make it a chapter like a Part
    h = re.sub(r"<h1([^>]*)>(.*?)</h1>", r'<h2 class="appendix"\1>\2</h2>', h, flags=re.S)
    # label paragraphs get a class so the page can colour them
    def lab(m):
        cls = LABELS.get(m.group(1).strip())
        if not cls:
            if re.match(r"Exercise \d", m.group(1)):
                cls = "exercise"
            else:
                return m.group(0)
        return f'<p class="lab lab-{cls}"><strong>{m.group(1)}</strong>'
    h = re.sub(r"<p><strong>([^<]{2,40}?)</strong>", lab, h)
    h = re.sub(r'<div (?:data-)?custom-style="Working">', '<div class="working">', h)
    h = h.replace('<figcaption aria-hidden="true">', "<figcaption>")
    return h


def headings(h):
    """[(level, id, text)] for the contents, in document order."""
    out = []
    for m in re.finditer(r'<h([23])[^>]*id="([^"]+)"[^>]*>(.*?)</h\1>', h, re.S):
        text = re.sub(r"<[^>]+>", "", m.group(3))
        out.append((int(m.group(1)), m.group(2), " ".join(html.unescape(text).split())))
    return out


def contents(hs):
    rows, in_appendix = [], False
    for lvl, hid, text in hs:
        if lvl == 2:
            in_appendix = in_appendix or text.lower().startswith("appendix")
            rows.append(f'<li class="toc-part"><a href="#{hid}">{esc(text)}</a></li>')
        elif not in_appendix:
            cls = "toc-ref" if text.lower().startswith("references") else "toc-sec"
            rows.append(f'<li class="{cls}"><a href="#{hid}">{esc(text)}</a></li>')
    rows.append('<li class="toc-part"><a href="#glossary">Glossary</a></li>')
    rows.append('<li class="toc-part"><a href="#series">The series: all 196 books</a></li>')
    return "\n".join(rows)


# ---------------------------------------------------------------- back matter

def glossary_rows(book_id):
    """Rows of prose/GLOSSARY.md first taught in this book, with the record id shown as its
    section label (B0-R0-C36 -> E6) where the book has an outline."""
    path = os.path.join(ROOT, "prose", "GLOSSARY.md")
    if not os.path.exists(path):
        return []
    labels = {}
    try:
        import build
        for part in build.load_book0_outline():
            for s in part["sections"]:
                labels[f"B0-R0-C{s['index']:02d}"] = s["id"]
    except Exception:
        pass
    prefix = "B0-R0-" if book_id == "B0" else f"{book_id}-"
    if book_id != "B0":
        # A rung book prints its sections by number ("3"), as its headings do.
        labels.update({f"{book_id}-C{n:02d}": str(n) for n in range(1, 100)})
    rows = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 3 or cells[0] in ("Term", "---") or set(cells[0]) <= set("-"):
                continue
            ids = re.findall(r"[A-Z]\d+-R\d+-C\d+|[A-Z]\d+-R\d+", cells[2])
            mine = [i for i in ids if i.startswith(prefix)]
            if not mine:
                continue
            where = ", ".join(labels.get(i, i) for i in mine)
            plain = re.sub(r"`?\(?`?([A-Z]\d+-R\d+-C\d+)`?\)?`?",
                           lambda m: f"({labels.get(m.group(1), m.group(1))})", cells[1])
            rows.append((cells[0], plain.replace("`", ""), where))
    rows.sort(key=lambda r: r[0].lower())
    return rows


def series_table(books, current):
    rows, level = [], None
    for b in books:
        if b["level"] != level:
            level = b["level"]
            rows.append(f'<tr class="lvl"><td colspan="3">{esc(level)}</td></tr>')
        cls = ' class="here"' if b["id"] == current else ""
        st = {"frozen": "done", "in progress": "in progress"}.get(b.get("status"), "")
        mark = " ◀ you are here" if b["id"] == current else ""
        rows.append(f'<tr{cls}><td class="n">{b["number"]}</td><td>{esc(b["title"])}'
                    f'<span class="mark">{mark}</span></td><td class="st">{st}</td></tr>')
    return "\n".join(rows)


# ---------------------------------------------------------------- assembly

def make(book_id):
    series = _yaml(os.path.join(HERE, "series.yml"))
    meta = _yaml(os.path.join(ROOT, "books", book_id, "book.yml"))
    books = book_list()
    entry = next((b for b in books if b["id"] == book_id), None)
    if entry is None:
        raise SystemExit(f"{book_id} is not in map/BOOKS.yml")
    for k in ("version", "last_updated", "title"):
        if not meta.get(k):
            raise SystemExit(f"books/{book_id}/book.yml has no {k}")
    t = theme(entry, series)
    n, total = entry["number"], len(books)
    title = meta["title"]
    number_label = f"Book {n}"
    version, updated = str(meta["version"]), long_date(meta["last_updated"])
    fmt = {"email": series["email"], "website": series["website"], "number": n, "version": version}
    idx = books.index(entry)
    pos = f"{idx + 1}{'th' if 10 <= (idx + 1) % 100 <= 20 else {1: 'st', 2: 'nd', 3: 'rd'}.get((idx + 1) % 10, 'th')}"
    prev_b = books[idx - 1] if idx > 0 else None
    next_b = books[idx + 1] if idx + 1 < len(books) else None

    body = body_html(book_id, drop_preamble=bool(meta.get("why")))
    hs = headings(body)
    gl = glossary_rows(book_id)
    css = open(os.path.join(HERE, "style.css"), encoding="utf-8").read()
    css = (css.replace("--INK--", t["ink"]).replace("--ACCENT--", t["accent"])
              .replace("--ACCENT2--", t["accent2"]).replace("--TINT--", t["tint"])
              .replace("--TINT2--", t["tint2"]).replace("--RULE--", t["rule"])
              .replace("--PAGE--", series.get("page_size", "A4")))
    fonts = f'<link rel="stylesheet" href="file://{os.path.join(HERE, "fonts", "fonts.css")}">'
    level_line = meta.get("cover_line") or (f'{entry["level"]} · {entry["part"]}' if n else "")
    url = f'https://{series["website"]}'

    front = f"""
<section class="cover" style="{cover_bg(t['hue'])}">{cover_svg(entry, t['hue'])}
  <div class="cover-top"><div class="cover-series">{esc(series['series_title'])}</div>
    <div class="cover-series-sub">{esc(series['series_subtitle'])}</div></div>
  <div class="cover-main">
    <div class="booknum">{esc(number_label)}<span>{pos} of {total} in the series</span></div>
    <h1 class="cover-title">{esc(title)}</h1>
    <div class="cover-subtitle">{esc(meta.get('subtitle', ''))}</div>
    <div class="cover-level">{esc(level_line)}</div>
  </div>
  <div class="cover-foot"><div class="author">{esc(series['author'])}</div>
    <div class="role">{esc(series['author_role'])}</div>
    <div class="site">{esc(series['website'])} · version {esc(version)}</div></div>
</section>

<section class="titlepage">
  <div class="tp-series">{esc(series['series_title'])} · {esc(number_label)}</div>
  <h1 class="tp-title">{esc(title)}</h1>
  <div class="tp-subtitle">{esc(meta.get('subtitle', ''))}</div>
  <div class="tp-author">{esc(series['author'])}</div>
  <div class="tp-role">{esc(series['author_role'])}</div>
  <div class="tp-contact">{esc(series['email'])} · {esc(series['website'])}</div>
</section>

<section class="colophon">
  <table class="facts">
    <tr><th>Series</th><td>{esc(series['series_title'])}: {esc(series['series_subtitle'])}</td></tr>
    <tr><th>Book</th><td>{esc(number_label)}, {esc(title)} ({pos} of {total} in the series)</td></tr>
    <tr><th>Version</th><td>{esc(version)}</td></tr>
    <tr><th>Last updated</th><td>{esc(updated)}</td></tr>
    <tr><th>Author</th><td>{esc(series['author'])}, {esc(series['author_role'])}</td></tr>
    <tr><th>Contact</th><td>{esc(series['email'])}</td></tr>
    <tr><th>Newest version</th><td>{esc(series['website'])}</td></tr>
  </table>
  <p class="copy">© {series['copyright_year']} {esc(series['author'].replace('Dr. ', ''))}.</p>
  {md_inline(series['licence'])}
  {md_inline(series['third_party'])}
  <h4>How this book was made</h4>{md_inline(series['how_made'])}
  <h4>Not advice</h4>{md_inline(series['disclaimer'])}
</section>

<section class="intro">
  <h2 class="front" id="introduction">Introduction</h2>
  <h3 class="front">Why this book exists</h3>{md_inline(meta.get('why', ''))}
  <h3 class="front">How to read it</h3>{md_inline(meta.get('how_to_read', ''))}{md_inline(series['how_to_read'])}
  <h3 class="front">How to send feedback</h3>{md_inline(series['feedback'].format(**fmt))}
  <div class="whereis">
    <div class="whereis-h">Where this book sits</div>
    <div>{esc(number_label)} of the series' {total} books (Book 0 and 195 rung books).
      {('Before it: Book ' + str(prev_b['number']) + ', ' + esc(prev_b['title']) + '.') if prev_b else 'It is the first.'}
      {('After it: Book ' + str(next_b['number']) + ', ' + esc(next_b['title']) + '.') if next_b else ''}
      The full list is at the back.</div>
  </div>
</section>

<section class="toc">
  <h2 class="front" id="contents">Contents</h2>
  <ul>{contents(hs)}</ul>
</section>
"""
    gl_html = "\n".join(f"<tr><td class='term'>{esc(a)}</td><td>{esc(b)}</td><td class='where'>{esc(c)}</td></tr>"
                        for a, b, c in gl)
    back = f"""
<section class="glossary">
  <h2 class="back" id="glossary">Glossary</h2>
  <p class="note">Every term of art this book teaches, in the plain words it gets where it is first
  used, and the section that teaches it.</p>
  <table class="gloss"><thead><tr><th>Term</th><th>Plain words</th><th>Section</th></tr></thead>
  <tbody>{gl_html}</tbody></table>
</section>

<section class="series-list">
  <h2 class="back" id="series">The series: all {total} books</h2>
  <p class="note">In build order: Book 0 first, then every Introductory rung, then every
  Intermediate rung, and so on; within a level, a subject comes after the subjects it depends on.
  "done" means that book's version 1 is finished. This is Book {n}.</p>
  <table class="series"><tbody>{series_table(books, book_id)}</tbody></table>
</section>

<section class="backcover" style="{cover_bg(t['hue'] + 20)}">{cover_svg({**entry, 'id': entry['id'] + '-back'}, t['hue'], faint=True)}
  <div class="bc-inner">
    <div class="bc-series">{esc(series['series_title'])} · {esc(number_label)}</div>
    <div class="bc-title">{esc(title)}</div>
    {md_inline(meta.get('back_blurb', ''))}
    <div class="bc-where">{esc(number_label)} of the series' {total} books, free to read at {esc(series['website'])}.</div>
    <div class="bc-bottom">
      <div class="bc-qr">{qr_svg(url)}</div>
      <div class="bc-meta"><div class="author">{esc(series['author'])}</div>
        <div>{esc(series['author_role'])}</div><div>{esc(series['email'])}</div>
        <div>{esc(series['website'])}</div><div>Version {esc(version)} · {esc(updated)}</div>
        <div class="lic">CC BY-NC-SA 4.0 · free to share, not to sell</div></div>
    </div>
  </div>
</section>
"""
    doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>{esc(series['series_title'])} · {esc(number_label)} · {esc(title)}</title>
<meta name="author" content="{esc(series['author'])}">
<meta name="description" content="{esc(meta.get('subtitle', ''))}">
<meta name="keywords" content="obesity, {esc(entry.get('part', ''))}">
<meta name="dcterms.created" content="{meta['last_updated']}">
{fonts}<style>{css}</style></head>
<body><div class="runtitle">{esc(number_label)} · {esc(title)}</div>
{front}<main class="book">{body}</main>{back}</body></html>"""
    html_path = os.path.join(BUILD, f"{book_id}-print.html")
    with open(html_path, "w", encoding="utf-8") as fh:
        fh.write(doc)
    from weasyprint import HTML
    pdf_path = os.path.join(BUILD, f"{book_id}.pdf")
    HTML(filename=html_path, base_url=BUILD).write_pdf(pdf_path)
    return pdf_path


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    for bid in sys.argv[1:]:
        print(f"  {bid}: {os.path.relpath(make(bid), ROOT)}")


if __name__ == "__main__":
    main()
