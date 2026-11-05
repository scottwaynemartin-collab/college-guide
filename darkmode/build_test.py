#!/usr/bin/env python3
"""Insert the right add-on before </body> of every live page -> test/<slug>.html (and out/<slug>.html = final embed code)."""
import os, glob, re, json
os.makedirs('test', exist_ok=True); os.makedirs('out', exist_ok=True)

def ds_for(slug):
    if slug.startswith('geoarcade'):
        if 'frq-tutor' in slug: return None       # already a dark design
        return 'ga'
    if slug.startswith('ap-world-compass'): return 'wc'
    if slug.startswith('ap-euro-atlas'):
        if 'dbq-cafe' in slug: return 'cafe'
        if any(k in slug for k in ('saq-sketchbook', 'leq-atelier', 'dbq-archive')): return 'eat'
        return 'ea'
    if slug.startswith('aplangstudio'): return 'lang'
    return None

MARK = '<style id="dm-css">'
manifest = []
for f in sorted(glob.glob('live/*/*.html')):
    slug = os.path.basename(f)[:-5]
    if slug.endswith('__home'): continue           # duplicate of the site root
    ds = ds_for(slug)
    if not ds: continue
    t = open(f, encoding='utf-8').read()
    if MARK in t:
        # replace an older add-on
        t = re.sub(r'<style id="dm-css">.*?</script>\n?', '', t, flags=re.S)
    add = open(f'addons/{ds}.html', encoding='utf-8').read()
    i = t.rfind('</body>')
    assert i > 0, slug
    new = t[:i] + add + t[i:]
    open(f'test/{slug}.html', 'w', encoding='utf-8').write(new)
    open(f'out/{slug}.html', 'w', encoding='utf-8').write(new)
    manifest.append(dict(slug=slug, ds=ds, live_len=len(t), new_len=len(new), site=f.split('/')[1]))
json.dump(manifest, open('manifest.json', 'w'), indent=1)
print(len(manifest), 'pages built')
for m in manifest: print(f"{m['slug'][:60]:60s} {m['ds']:5s} {m['live_len']:7d} -> {m['new_len']:7d}")
