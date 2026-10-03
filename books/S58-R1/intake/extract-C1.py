# Extract TinyFish fetch_content results verbatim from this subagent's transcript.
# usage: extract.py URL OUTFILE   (takes the LAST result for that exact URL)
import json, sys, re, os
T='/root/.claude/projects/-home-claude/f2099557-ac04-5a0f-a543-1cd2874da8af/subagents/agent-ab237abe9d6b2b51d.jsonl'
url, out = sys.argv[1], sys.argv[2]
def payloads():
    for line in open(T):
        try: d=json.loads(line)
        except: continue
        msg=d.get('message',{})
        c=msg.get('content')
        if not isinstance(c,list): continue
        for part in c:
            if part.get('type')!='tool_result': continue
            cc=part.get('content')
            texts=[]
            if isinstance(cc,str): texts=[cc]
            elif isinstance(cc,list): texts=[x.get('text','') for x in cc if isinstance(x,dict)]
            for t in texts:
                m=re.search(r'(/root/\.claude/projects/\S+?tool-results/\S+?\.(?:txt|json))',t)
                if m and not t.lstrip().startswith('{'):
                    raw=open(m.group(1)).read()
                    try:
                        j=json.loads(raw)
                        if isinstance(j,list): raw=''.join(x.get('text','') for x in j if isinstance(x,dict))
                    except: pass
                    t=raw
                yield t
hit=None
for t in payloads():
    try: j=json.loads(t)
    except: continue
    if not isinstance(j,dict): continue
    for r in j.get('results',[]):
        if r.get('url')==url: hit=r
if not hit: sys.exit('NOT FOUND '+url)
open(out,'w').write(hit['text'])
print(out, len(hit['text']), 'chars; title:', hit.get('title'), '; final_url:', hit.get('final_url'), '; format:', hit.get('format'))
