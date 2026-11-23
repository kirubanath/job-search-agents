#!/usr/bin/env python3
"""Usage: md2gdoc_html.py input.md output.html "Document title"
Converts GitHub-flavoured markdown to one HTML file that Google Drive turns into a clean Google Doc.
Whitespace between tags is flattened everywhere except inside <pre> blocks. Prints the sha256 of the output."""
import sys,re,subprocess,hashlib
src,dst,title=sys.argv[1],sys.argv[2],sys.argv[3]
body=subprocess.run(['pandoc','-f','gfm','-t','html5','--wrap=none','--no-highlight',src],capture_output=True,text=True,check=True).stdout
# Google Docs restarts an ordered list after a nested bullet list, so ordered lists become paragraphs with typed numbers.
from bs4 import BeautifulSoup, NavigableString, Tag
soup=BeautifulSoup(body,'html.parser')
BLOCK={'ul','ol','pre','table','blockquote','p','div'}
def flatten(ol,prefix=''):
    start=int(ol.get('start',1)); new=[]
    for i,li in enumerate([c for c in ol.children if isinstance(c,Tag) and c.name=='li']):
        num=f"{prefix}{start+i}."
        for sub in li.find_all('ol',recursive=False): flatten(sub,prefix=num)
        for pchild in li.find_all('p',recursive=False):
            for sub in pchild.find_all('ol',recursive=False): flatten(sub,prefix=num)
        para=soup.new_tag('p'); para.append(NavigableString(num+' ')); rest=[]; lead=True
        for c in list(li.children):
            c.extract()
            if isinstance(c,Tag) and c.name=='p' and lead and not rest:
                for cc in list(c.children): para.append(cc.extract())
                lead=False
            elif isinstance(c,Tag) and c.name in BLOCK: rest.append(c); lead=False
            elif lead: para.append(c)
            else: rest.append(c)
        new.append(para); new.extend(rest)
    for n in reversed(new): ol.insert_after(n)
    ol.decompose()
while True:
    tops=[o for o in soup.find_all('ol') if not o.find_parent('ol')]
    if not tops: break
    for o in tops: flatten(o)
body=str(soup)
parts=re.split(r'(<pre.*?</pre>)',body,flags=re.S)
out=[]
for p in parts:
    if p.startswith('<pre'): out.append(p)
    else: out.append(re.sub(r'>\s+<','><',p).replace('\n',' '))
html='<!DOCTYPE html><html><head><meta charset="utf-8"><title>%s</title></head><body>%s</body></html>'%(title,''.join(out))
open(dst,'w',encoding='utf-8').write(html)
print(hashlib.sha256(html.encode('utf-8')).hexdigest(), dst)
