"""Build the Word style template the booklets are rendered against.

Run: python check/references/make_reference_docx.py

Pandoc's default template typesets an indented block as `SourceCode` in a monospace
face. That is correct for a programming manual and wrong for this book, where every
indented block is arithmetic. Before this template existed, 186 paragraphs of Book 0 -
every worked calculation in it - were set as computer source code.

The template defines a `Working` paragraph style for display arithmetic, gives the body
a serif face at a readable measure, and cuts the default paragraph spacing, which was
what produced the gaps between every paragraph. It is generated rather than committed as
a binary blob so that a change to it is reviewable in a diff.
"""
import os, re, shutil, subprocess, sys, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET = os.path.join(HERE, "reference.docx")

# Cambria and Calibri ship with Office on Windows and macOS; the fallbacks cover Linux.
SERIF, SANS = "Cambria", "Calibri"

DOC_DEFAULTS = f'''<w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="{SERIF}" w:hAnsi="{SERIF}" w:eastAsia="{SERIF}" w:cs="{SERIF}"/><w:sz w:val="22"/><w:szCs w:val="22"/><w:lang w:val="en-IN"/></w:rPr></w:rPrDefault><w:pPrDefault><w:pPr><w:spacing w:before="0" w:after="140" w:line="288" w:lineRule="auto"/></w:pPr></w:pPrDefault></w:docDefaults>'''

WORKING = f'''<w:style w:type="paragraph" w:customStyle="1" w:styleId="Working"><w:name w:val="Working"/><w:basedOn w:val="BodyText"/><w:qFormat/><w:pPr><w:spacing w:before="200" w:after="200" w:line="264" w:lineRule="auto"/><w:ind w:left="567"/><w:contextualSpacing w:val="0"/></w:pPr><w:rPr><w:rFonts w:ascii="{SERIF}" w:hAnsi="{SERIF}"/><w:sz w:val="21"/></w:rPr></w:style>'''

# Tables arrive from markdown with no borders at all, which is why they did not read as
# tables. Horizontal rules only: vertical lines make a small table look like a form.
TABLE = '''<w:style w:type="paragraph" w:styleId="Table"><w:name w:val="Table"/><w:basedOn w:val="BodyText"/><w:qFormat/><w:pPr><w:spacing w:before="40" w:after="40" w:line="240" w:lineRule="auto"/></w:pPr><w:rPr><w:sz w:val="20"/></w:rPr></w:style>'''

TABLE_GRID = '''<w:style w:type="table" w:styleId="Table"><w:name w:val="Table"/><w:tblPr><w:tblBorders><w:top w:val="single" w:sz="8" w:space="0" w:color="444444"/><w:bottom w:val="single" w:sz="8" w:space="0" w:color="444444"/><w:insideH w:val="single" w:sz="4" w:space="0" w:color="BBBBBB"/></w:tblBorders><w:tblCellMar><w:top w:w="60" w:type="dxa"/><w:bottom w:w="60" w:type="dxa"/><w:left w:w="100" w:type="dxa"/><w:right w:w="100" w:type="dxa"/></w:tblCellMar></w:tblPr></w:style>'''


def heading(sid, name, size, before, after, color="1A1A1A", sans=True):
    fonts = SANS if sans else SERIF
    return (f'<w:style w:type="paragraph" w:styleId="{sid}"><w:name w:val="{name}"/>'
            f'<w:basedOn w:val="Normal"/><w:next w:val="BodyText"/><w:qFormat/>'
            f'<w:pPr><w:keepNext/><w:spacing w:before="{before}" w:after="{after}" '
            f'w:line="240" w:lineRule="auto"/><w:outlineLvl w:val="{int(sid[-1]) - 1}"/></w:pPr>'
            f'<w:rPr><w:rFonts w:ascii="{fonts}" w:hAnsi="{fonts}"/><w:b/>'
            f'<w:color w:val="{color}"/><w:sz w:val="{size}"/></w:rPr></w:style>')


REPLACEMENTS = [
    ("Heading1", heading("Heading1", "heading 1", 40, 480, 220)),
    ("Heading2", heading("Heading2", "heading 2", 30, 420, 180)),
    ("Heading3", heading("Heading3", "heading 3", 25, 340, 140)),
    ("Heading4", heading("Heading4", "heading 4", 22, 260, 120, color="333333")),
    ("Table", TABLE),
]


def style_block(xml, style_id, wtype=None):
    """Locate one <w:style> element by id, optionally by w:type too."""
    for m in re.finditer(r"<w:style\b[^>]*>", xml):
        tag = m.group(0)
        if f'w:styleId="{style_id}"' not in tag:
            continue
        if wtype and f'w:type="{wtype}"' not in tag:
            continue
        end = xml.index("</w:style>", m.end()) + len("</w:style>")
        return m.start(), end
    return None


def main():
    if not shutil.which("pandoc"):
        sys.exit("pandoc is required to generate the reference document.")
    base = subprocess.run(["pandoc", "--print-default-data-file", "reference.docx"],
                          capture_output=True)
    if base.returncode != 0:
        sys.exit("pandoc could not supply its default reference.docx")
    tmp = TARGET + ".tmp"
    with open(tmp, "wb") as fh:
        fh.write(base.stdout)

    with zipfile.ZipFile(tmp) as z:
        parts = {n: z.read(n) for n in z.namelist()}

    xml = parts["word/styles.xml"].decode("utf-8")
    xml = re.sub(r"<w:docDefaults>.*?</w:docDefaults>", DOC_DEFAULTS, xml, flags=re.S)

    changed = ["docDefaults"]
    for sid, block in REPLACEMENTS:
        span = style_block(xml, sid, "paragraph")
        if span:
            xml = xml[:span[0]] + block + xml[span[1]:]
            changed.append(sid)

    span = style_block(xml, "Table", "table")
    if span:
        xml = xml[:span[0]] + TABLE_GRID + xml[span[1]:]
        changed.append("Table(table)")

    if 'w:styleId="Working"' not in xml:
        xml = xml.replace("</w:styles>", WORKING + "</w:styles>")
        changed.append("Working")

    parts["word/styles.xml"] = xml.encode("utf-8")
    with zipfile.ZipFile(TARGET, "w", zipfile.ZIP_DEFLATED) as z:
        for name, data in parts.items():
            z.writestr(name, data)
    os.remove(tmp)
    print(f"wrote {os.path.relpath(TARGET)} · styles set: {', '.join(changed)}")


if __name__ == "__main__":
    main()
