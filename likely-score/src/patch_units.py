#!/usr/bin/env python3
"""GeoArcade unit pages (FRQ Lab): add 'Likely point? Grade it in Gemini' + likely-point wording. Nov 6 2026."""
import re, base64, zlib, os, sys
H = os.path.dirname(os.path.abspath(__file__))
mod = open(os.path.join(H, 'galab.js'), encoding='utf-8').read()

def rep(src, old, new, label):
    c = src.count(old)
    if c != 1: sys.exit(f'FAIL {label}: count {c}')
    return src.replace(old, new)

os.makedirs(os.path.join(H, 'out'), exist_ok=True)
for u in range(1, 8):
    page = open(os.path.join(H, f'u{u}.embed.html'), encoding='utf-8').read()
    p = open(os.path.join(H, f'u{u}.prog.js'), encoding='utf-8').read()
    p = mod + '\n' + p
    p = rep(p, '_=(e,s,a,n,i)=>{const o=k[s];', '_=(e,s,a,n,i)=>{const o=k[s];window.GALab.remember(s,e,i);', 'remember')
    p = rep(p, '\'<span class="pill green">✓ Self-assessed point</span>\'', '\'<span class="pill green">✓ Likely point</span>\'', 'pill')
    p = rep(p, 'Need a sentence starter?</button>', 'Need a sentence starter?</button><button class="btn sm gemb" data-gem="${s}">🤖 Likely point? Grade it in Gemini</button>', 'gem btn')
    p = rep(p, '<span>Self-assess after checking the rubric:</span>', '<span>Would it likely earn the point? Compare with the model and the checklist (or ask Gemini), then mark it:</span>', 'verdict')
    p = rep(p, '<div class="big">${a} / 7</div>', '<div class="big"><small class="lk-k">Likely score</small>${a} / 7</div>', 'boss big')
    p = rep(p, 'left to self-score`', 'left to score`', 'boss left')
    p = rep(p, 'n("Self-assessed point ✓")', 'n("Likely point ✓")', 'toast')
    p = rep(p, 'Type first · reveal second · score yourself', 'Type first · check it · mark the likely point', 'reps pill')
    p = rep(p, 'e("[data-verdict]",b).forEach(t=>t.addEventListener("click",()=>{',
            'e("[data-gem]",b).forEach(q9=>q9.addEventListener("click",()=>{const m9=window.GALab.gem(q9.dataset.gem,x[q9.dataset.gem]||"",u);m9&&n(m9,4200)})),e("[data-verdict]",b).forEach(t=>t.addEventListener("click",()=>{', 'wire')
    p = rep(p, 'x[e.dataset.draft]=e.value,a.set(`lab:${g}:drafts`,x)', 'x[e.dataset.draft]=e.value,GA.store.set(`lab:${g}:drafts`,x)', 'draft save fix')
    raw = p.encode('utf-8')
    co = zlib.compressobj(9, zlib.DEFLATED, -15)
    b64 = base64.b64encode(co.compress(raw) + co.flush()).decode()
    m = re.search(r'var P="([^"]*)";', page)
    h = page[:m.start(1)] + b64 + page[m.end(1):]
    n = re.search(r'var o=new Uint8Array\((\d+)\);window\.__inflate', h)
    h = h[:n.start(1)] + str(len(raw)) + h[n.end(1):]
    open(os.path.join(H, f'out/unit-{u}.html'), 'w', encoding='utf-8').write(h)
    open(os.path.join(H, f'out/unit-{u}.prog.js'), 'w', encoding='utf-8').write(p)
    print(u, len(page), '->', len(h), 'dm', h.count('id="dm-css"'))
