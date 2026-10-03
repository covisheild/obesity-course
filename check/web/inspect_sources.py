"""Prints the structure of the private source files under drhm-sources/<prefix> (default stats/): names,
sizes, kinds, and for documents the heading outline and counts of equations, figures, tables and code.
Never prints body text: this repo's Actions logs are public. Needs R2_ACCOUNT_ID/R2_ACCESS_KEY_ID/R2_SECRET_ACCESS_KEY."""
import collections, io, json, os, re, sys, zipfile
import boto3, pypandoc

prefix = sys.argv[1] if len(sys.argv) > 1 else 'stats/'
s3 = boto3.client('s3', endpoint_url=f"https://{os.environ['R2_ACCOUNT_ID']}.r2.cloudflarestorage.com",
                  aws_access_key_id=os.environ['R2_ACCESS_KEY_ID'], aws_secret_access_key=os.environ['R2_SECRET_ACCESS_KEY'], region_name='auto')
objs = [o for p in s3.get_paginator('list_objects_v2').paginate(Bucket='drhm-sources', Prefix=prefix) for o in p.get('Contents', [])]
print(f'== {len(objs)} objects under drhm-sources/{prefix}')
for o in objs: print(f"  {o['Size']:>12,}  {o['Key']}")

def outline(blocks, depth=0, out=None):
    out = out if out is not None else collections.Counter()
    for b in blocks if isinstance(blocks, list) else []:
        if isinstance(b, dict) and 't' in b:
            out[b['t']] += 1
            if b['t'] == 'Math': out['Math:' + b['c'][0]['t']] += 1
            outline(b.get('c'), depth + 1, out)
        elif isinstance(b, list): outline(b, depth + 1, out)
    return out

def text(inl):
    return ''.join(x['c'] if x['t'] == 'Str' else ' ' if x['t'] in ('Space', 'SoftBreak') else text(x['c']) if x['t'] in ('Emph', 'Strong', 'Span') else '' for x in inl)

def describe_doc(data, ext, name):
    path = f'/tmp/doc.{ext}'; open(path, 'wb').write(data)
    fmt = {'docx': 'docx', 'md': 'markdown', 'tex': 'latex', 'html': 'html', 'odt': 'odt', 'rmd': 'markdown', 'qmd': 'markdown'}[ext]
    ast = json.loads(pypandoc.convert_file(path, 'json', format=fmt))
    c = outline(ast['blocks'])
    print(f'  -- {name}: ' + ', '.join(f'{k} {v}' for k, v in sorted(c.items()) if k in ('Header', 'Para', 'Table', 'Image', 'CodeBlock', 'Code', 'Math:DisplayMath', 'Math:InlineMath', 'BulletList', 'OrderedList', 'Note', 'BlockQuote', 'Div', 'RawBlock', 'RawInline')))
    heads = [(b['c'][0], text(b['c'][2])) for b in ast['blocks'] if b['t'] == 'Header']
    for lvl, h in heads[:120]: print(f"     {'  ' * (lvl - 1)}H{lvl} {h[:90]}")
    if len(heads) > 120: print(f'     ... {len(heads) - 120} more headings')
    styles = collections.Counter(b['c'][0][1][0] for b in ast['blocks'] if b['t'] == 'Div' and b['c'][0][1])
    if styles: print('     div classes:', dict(styles.most_common(20)))
    # Words that mark the book's own block types (Definition, Example...) at the start of paragraphs.
    starts = collections.Counter(re.match(r'\W*(\w+(?: \w+)?)', text(b['c'])).group(1) for b in ast['blocks'] if b['t'] == 'Para' and re.match(r'\W*\w', text(b['c'])))
    print('     common paragraph openings:', [w for w, n in starts.most_common(25) if n >= 5])

DOC = ('docx', 'md', 'tex', 'html', 'odt', 'rmd', 'qmd')
for o in objs:
    key = o['Key']; ext = key.rsplit('.', 1)[-1].lower()
    if ext not in DOC + ('zip',): continue
    data = s3.get_object(Bucket='drhm-sources', Key=key)['Body'].read()
    print(f'\n== {key}')
    if ext == 'zip':
        z = zipfile.ZipFile(io.BytesIO(data))
        kinds = collections.Counter(n.rsplit('.', 1)[-1].lower() if '.' in n.rsplit('/', 1)[-1] else '(dir/none)' for n in z.namelist())
        print('  kinds:', dict(kinds.most_common()))
        tops = collections.Counter('/'.join(n.split('/')[:2]) for n in z.namelist())
        for t, n in sorted(tops.items())[:80]: print(f'  {n:>5}  {t}')
        docs = [n for n in z.namelist() if n.rsplit('.', 1)[-1].lower() in DOC]
        for n in sorted(docs, key=lambda n: -z.getinfo(n).file_size)[:6]:
            try: describe_doc(z.read(n), n.rsplit('.', 1)[-1].lower(), n)
            except Exception as e: print(f'  -- {n}: could not read ({e.__class__.__name__})')
        for n in [n for n in z.namelist() if n.endswith(('.yml', '.yaml', '.json', '.toml'))][:10]:
            print(f'  config {n}: {z.getinfo(n).file_size} bytes; keys:', end=' ')
            try:
                raw = z.read(n).decode(errors='replace')
                print(sorted(json.loads(raw).keys())[:30] if n.endswith('.json') else re.findall(r'^([A-Za-z_][\w-]*):', raw, re.M)[:30])
            except Exception as e: print(e.__class__.__name__)
    else:
        describe_doc(data, ext, key)
