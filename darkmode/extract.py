import re,html,sys,json,subprocess,os
def get(url):
    return subprocess.run(['curl','-sS','-L',url],capture_output=True,text=True).stdout
def embed_from_page(t):
    # find the escaped doc inside an attribute: starts with &lt;!DOCTYPE or &lt;html
    cands=[]
    for m in re.finditer(r'&lt;!DOCTYPE html',t):
        s=m.start()
        # attribute value ends at next unescaped quote "
        e=t.find('"',s)
        cands.append(html.unescape(t[s:e]))
    if not cands:
        for m in re.finditer(r'&lt;html',t):
            s=m.start(); e=t.find('"',s); cands.append(html.unescape(t[s:e]))
    cands.sort(key=len,reverse=True)
    return cands[0] if cands else None
def nav_links(t,base):
    # published site nav links are in the HTML as href="/view/<site>/<page>"
    site=base.split('/view/')[1].split('/')[0]
    links=sorted(set(re.findall(r'href="(/view/'+re.escape(site)+r'(?:/[^"#?]*)?)"',t)))
    return ['https://sites.google.com'+l for l in links]
if __name__=='__main__':
    base=sys.argv[1]; out=sys.argv[2]; os.makedirs(out,exist_ok=True)
    home=get(base)
    pages=nav_links(home,base)
    if base not in pages: pages.insert(0,base)
    seen=set(); rows=[]
    for p in pages:
        slug=p.rstrip('/').split('/view/')[1].replace('/','__')
        if slug in seen: continue
        seen.add(slug)
        t=home if p==base else get(p)
        e=embed_from_page(t)
        title=re.search(r'<title>(.*?)</title>',t,re.S)
        if e:
            open(f'{out}/{slug}.html','w').write(e)
        rows.append((slug,p,len(e) if e else 0,title.group(1).strip() if title else ''))
    for r in rows: print(r)
