#!/usr/bin/env python3
"""Generate the dark-mode add-on (<style id="dm-css"> + <script id="dm">) per design system.
Input: cssrules.json (collected from the live pages with collect_css.js) + palettes.py.
Output: addons/<ds>.html (snippet to insert before </body>), addons/<ds>.css (for review).
"""
import json, re, colorsys, os
from palettes import DS

R = json.load(open('cssrules.json'))
GROUPS = {
    'ga':   ['live/geoarcade/geoarcade__unit-2.html', 'live/geoarcade/geoarcade.html', 'live/geoarcade/geoarcade__frq-exam-prep.html'],
    'wc':   ['live/ap-world-compass/ap-world-compass__unit-1-the-global-tapestry.html', 'live/ap-world-compass/ap-world-compass.html',
             'live/ap-world-compass/ap-world-compass__saq-checker.html', 'live/ap-world-compass/ap-world-compass__leq-launchpad.html',
             'live/ap-world-compass/ap-world-compass__dbq-dossier.html'],
    'ea':   ['live/ap-euro-atlas/ap-euro-atlas__unit-1-renaissance-and-exploration.html', 'live/ap-euro-atlas/ap-euro-atlas.html',
             'live/ap-euro-atlas/ap-euro-atlas__period-1-the-unmaking-of-christendom.html', 'live/ap-euro-atlas/ap-euro-atlas__the-isms-tracker.html'],
    'eat':  ['live/ap-euro-atlas/ap-euro-atlas__saq-sketchbook.html', 'live/ap-euro-atlas/ap-euro-atlas__leq-atelier.html', 'live/ap-euro-atlas/ap-euro-atlas__dbq-archive.html'],
    'cafe': ['live/ap-euro-atlas/ap-euro-atlas__dbq-cafe.html'],
    'lang': ['live/aplangstudio/aplangstudio.html'],
}

NAMED = {'white': (255, 255, 255), 'black': (0, 0, 0), 'transparent': None, 'inherit': None, 'currentcolor': None, 'none': None}
COLOR_RE = re.compile(r'#(?:[0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{3,4})\b|rgba?\([^)]*\)|hsla?\([^)]*\)|\b(?:white|black)\b', re.I)

def parse(c):
    c = c.strip().lower()
    if c in NAMED: return NAMED[c]
    if c.startswith('#'):
        h = c[1:]
        if len(h) in (3, 4): h = ''.join(x * 2 for x in h)
        try:
            r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
        except ValueError:
            return None
        a = int(h[6:8], 16) / 255 if len(h) == 8 else 1
        return (r, g, b, a) if a < 1 else (r, g, b)
    m = re.match(r'rgba?\(([^)]*)\)', c)
    if m:
        parts = [p.strip() for p in re.split(r'[,/\s]+', m.group(1)) if p.strip()]
        try:
            r, g, b = [float(p.rstrip('%')) * (2.55 if p.endswith('%') else 1) for p in parts[:3]]
        except ValueError:
            return None
        a = 1
        if len(parts) > 3:
            a = float(parts[3].rstrip('%')) / (100 if parts[3].endswith('%') else 1)
        return (int(r), int(g), int(b), a) if a < 1 else (int(r), int(g), int(b))
    return None

def lum(c):
    r, g, b = [x / 255 for x in c[:3]]
    f = lambda v: v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)

def hexs(rgb):
    return '#%02X%02X%02X' % tuple(int(round(x)) for x in rgb[:3])

def darken_surface(c, ds):
    """Light tinted background -> dark tinted background of the same hue."""
    r, g, b = [x / 255 for x in c[:3]]
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    if l > 0.985: return ds['card']
    if l > 0.93: return ds['paper']
    if s < 0.08: return ds['soft_bg']
    nl = 0.16 + (1 - l) * 0.18          # pastels -> ~0.17-0.25
    ns = min(s, 0.45)
    rr, gg, bb = colorsys.hls_to_rgb(h, nl, ns)
    return hexs((rr * 255, gg * 255, bb * 255))

def lighten_text(c, ds):
    r, g, b = [x / 255 for x in c[:3]]
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    if s < 0.12:
        return ds['ink']
    nl = max(0.72, 1 - l * 0.6)
    rr, gg, bb = colorsys.hls_to_rgb(h, nl, min(s, 0.8))
    return hexs((rr * 255, gg * 255, bb * 255))

def lighten_border(c, ds):
    r, g, b = [x / 255 for x in c[:3]]
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    if s < 0.15: return ds['line']
    rr, gg, bb = colorsys.hls_to_rgb(h, 0.32, min(s, 0.5))
    return hexs((rr * 255, gg * 255, bb * 255))

def is_light(c): return c is not None and len(c) == 3 and lum(c) > 0.62
def is_dark(c): return c is not None and len(c) == 3 and lum(c) < 0.18

def rewrite_value(v, ds, mode):
    """Replace hardcoded colors inside a value (handles gradients)."""
    changed = False
    def rep(m):
        nonlocal changed
        c = parse(m.group(0))
        if c is None: return m.group(0)
        if mode == 'bg' and is_light(c):
            changed = True; return darken_surface(c, ds)
        if mode == 'bg' and len(c) == 4 and lum(c) > 0.62 and c[3] >= 0.35:
            changed = True; pr = ds['paper_rgb']; return 'rgba(%d,%d,%d,%.2f)' % (pr[0], pr[1], pr[2], min(0.97, c[3] + 0.1))
        if mode == 'text' and is_dark(c):
            changed = True; return lighten_text(c, ds)
        if mode == 'border' and is_light(c):
            changed = True; return lighten_border(c, ds)
        return m.group(0)
    out = COLOR_RE.sub(rep, v)
    return (out, changed)

BG_PROPS = ('background', 'background-color', 'background-image')
TEXT_PROPS = ('color', '-webkit-text-fill-color')
BORDER_PROPS = ('border', 'border-color', 'border-top', 'border-bottom', 'border-left', 'border-right', 'outline')

def prefix_selector(sel):
    parts = []
    for s in re.split(r',(?![^()]*\))', sel):
        s = s.strip()
        if not s: continue
        if s in (':root', 'html'):
            parts.append('html.dm')
        elif s.startswith('html'):
            parts.append('html.dm' + s[4:])
        elif s.startswith(':root'):
            parts.append('html.dm' + s[5:])
        else:
            parts.append(':where(html.dm) ' + s)
    return ','.join(parts)

def bg_kind(d, ds, root):
    """Classify a rule's background: 'none' | 'light' | 'var-surface' | 'var-accent' | 'solid' """
    v = ' '.join(d.get(p, '') for p in BG_PROPS).strip()
    if not v: return 'none'
    vars_ = re.findall(r'var\((--[\w-]+)', v)
    if vars_:
        for t in vars_:
            rv = root.get(t, '')
            m = COLOR_RE.search(rv) if rv else None
            if m and is_light(parse(m.group(0))):
                return 'var-surface'
            if t in ('--card', '--surface', '--paper', '--paper-2', '--bg', '--bg-2', '--surface-2', '--white', '--soft', '--marbre', '--creme', '--craie', '--cream', '--cream-warm', '--bg-alt'):
                return 'var-surface'
        return 'var-accent'
    cols = [parse(m) for m in COLOR_RE.findall(v)]
    cols = [c for c in cols if c]
    if not cols: return 'none'
    if all(is_light(c) for c in cols): return 'light'
    return 'solid'

def gen(ds_name):
    ds = DS[ds_name]
    rules, seen, root = [], set(), {}
    for f in GROUPS[ds_name]:
        for r in R[f]:
            key = (r['sel'], r['media'], json.dumps(r['d'], sort_keys=True))
            if key in seen: continue
            seen.add(key)
            if r['sel'] == ':root':
                for p, v in r['d'].items():
                    if p.startswith('--'): root.setdefault(p, v.strip())
            rules.append(r)
    tokens = dict(ds['tokens'])
    out = []
    # 1. token overrides + custom toggle tokens
    tg = ds['toggle']
    tok_css = ';'.join(f'{k}:{v}' for k, v in tokens.items())
    out.append(f"html.dm{{color-scheme:dark;{tok_css};--dm-card:{ds['card']};--dm-ink:{ds['ink']};--dm-line:{ds['line']};--dm-tg-bg:{tg['bg']};--dm-tg-fg:{tg['fg']};--dm-tg-b:{tg['border']};--dm-tg-font:{tg['font']}}}")
    flip = set(ds.get('flip_text', []))
    # any token that goes from dark (light mode) to light (dark mode) is a text token: pin its background/border uses
    for t, nv in tokens.items():
        ov = root.get(t, '')
        oc = parse(COLOR_RE.search(ov).group(0)) if ov and COLOR_RE.search(ov) else None
        nc = parse(nv) if nv.startswith('#') else None
        if oc and nc and lum(oc) < 0.25 and lum(nc) > 0.35:
            flip.add(t)
    pins = ds.get('text_pins', {}) or {}
    keep = set(ds.get('keep_text', []))
    keepv = ds.get('keep_text_value', {}) or {}
    # 2. per-rule overrides
    by_media = {}
    for r in rules:
        sel, media, d = r['sel'], r['media'], r['d']
        if sel == ':root': continue
        decl = {}
        kind = bg_kind(d, ds, root)
        for p, v in d.items():
            if p.startswith('--'): continue
            imp = v.endswith('!important')
            vv = v.replace('!important', '').strip()
            vars_ = re.findall(r'var\((--[\w-]+)', vv)
            if p in BG_PROPS:
                # pin flipped text tokens used as backgrounds
                for t in vars_:
                    if t in flip and t in root:
                        decl[p] = vv.replace(f'var({t})', root[t])
                nv, ch = rewrite_value(decl.get(p, vv), ds, 'bg')
                if ch: decl[p] = nv
            elif p in TEXT_PROPS:
                for t in vars_:
                    if t in pins and pins[t] and kind in ('none', 'light', 'var-surface'):
                        decl[p] = vv.replace(f'var({t})', pins[t])
                    if t in keep:
                        decl[p] = vv.replace(f'var({t})', keepv.get(t, root.get(t, vv)))
                if p not in decl and not vars_:
                    c = parse(vv)
                    if c is not None and is_dark(c) and kind in ('none', 'light', 'var-surface'):
                        decl[p] = lighten_text(c, ds)
            elif p in BORDER_PROPS:
                for t in vars_:
                    if t in flip and t in root:
                        decl[p] = vv.replace(f'var({t})', root[t])
                nv, ch = rewrite_value(decl.get(p, vv), ds, 'border')
                if ch: decl[p] = nv
            elif p in ('fill', 'stroke'):
                c = parse(vv)
                if c is not None and is_dark(c) and not vars_:
                    decl[p] = lighten_text(c, ds)
            elif p == 'box-shadow':
                # light "inset 0 0 0 Npx #fff" rings -> dark
                nv, ch = rewrite_value(vv, ds, 'bg')
                if ch: decl[p] = nv
        if decl:
            body = ';'.join(f'{k}:{v}' for k, v in decl.items())
            by_media.setdefault(media, []).append(f'{prefix_selector(sel)}{{{body}}}')
    for media, lst in by_media.items():
        css = '\n'.join(lst)
        if media:
            # media string like "@(max-width: 820px)" possibly nested "@a@b"
            conds = [m for m in media.split('@') if m]
            for c in reversed(conds):
                css = f'@media {c}{{\n{css}\n}}'
        out.append(css)
    if os.path.exists(f'manual/{ds_name}.css'):
        out.append(open(f'manual/{ds_name}.css').read())
    out.append(open('toggle.css').read())
    css = '\n'.join(out)
    os.makedirs('addons', exist_ok=True)
    open(f'addons/{ds_name}.css', 'w').write(css)
    js = open('engine.js').read()
    snippet = f'<style id="dm-css">\n{css}\n</style>\n<script id="dm">\n{js}\n</script>\n'
    open(f'addons/{ds_name}.html', 'w').write(snippet)
    return len(css), len(snippet)

if __name__ == '__main__':
    for k in DS:
        print(k, gen(k))
