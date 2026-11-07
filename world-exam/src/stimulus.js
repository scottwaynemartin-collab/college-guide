/* World Compass · AP Practice Exam · stimulus renderer
   Everything here is driven by the JSON stimulus object; nothing is hard-coded per question.
   Supported stimulus.type: passage | pair | image | table | bar (plus the GeoArcade map types, kept for later units).
   Anything else -> "source unavailable" card. render(stim, {glossary:true}) adds the practice-only "Words to know". */
window.PE_STIM = (function () {
  'use strict';
  const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  let uid = 0;
  const nid = () => 'st' + (++uid) + '_' + Math.random().toString(36).slice(2, 6);
  const num = v => (typeof v === 'number' && isFinite(v)) ? v : (parseFloat(v) || 0);
  const fmt = v => Number.isInteger(v) ? v.toLocaleString('en-US') : (+v).toLocaleString('en-US', { maximumFractionDigits: 1 });
  const r1 = v => Math.round(v * 10) / 10;

  function render(stim, opt) {
    if (!stim || typeof stim !== 'object') return unavailable();
    opt = opt || {};
    try {
      switch (stim.type) {
        case 'passage': return passage(stim, opt);
        case 'pair': return pair(stim, opt);
        case 'image': return image(stim, opt);
        case 'table': return table(stim);
        case 'bar': return bar(stim);
        case 'districtMap': return districtMap(stim);
        case 'schematicMap': return schematicMap(stim);
        case 'rings': return rings(stim);
        default: return unavailable(stim.type);
      }
    } catch (e) {
      if (window.console && console.warn) console.warn('stimulus render failed', e);
      return unavailable(stim.type);
    }
  }

  function unavailable(type) {
    return `<figure class="stim unavail" role="note"><div>⚠︎ Source unavailable${type ? ` <span class="muted">(${esc(type)})</span>` : ''}</div><div class="small muted">You can still answer the question. Tell your AP World History teacher which question this is.</div></figure>`;
  }
  const title = t => t ? `<figcaption class="stim-title">${esc(t)}</figcaption>` : '';
  const source = s => s ? `<div class="stim-source">Source: ${esc(s)}</div>` : '';


  /* ---------- text sources (AP World) ---------- */
  // Paragraph text is plain; a "\n" inside a paragraph is a line break (poems). Footnote marks stay inline (e.g. "kaan*").
  const para = t => `<p>${esc(t).replace(/\n/g, '<br>')}</p>`;
  function glossaryHTML(g) {
    if (!g || !g.length) return '';
    return `<details class="gloss"><summary>Words to know <span class="n">${g.length}</span></summary><dl>${g.map(x => `<div><dt>${esc(x.t)}</dt><dd>${esc(x.d)}</dd></div>`).join('')}</dl></details>`;
  }
  function passageBody(s, opt, label) {
    const fns = (s.footnotes || []).map(f => `<div class="fn"><span class="m">${esc(f.mark || '*')}</span>${esc(f.text)}</div>`).join('');
    return `${label ? `<div class="psg-lbl">${esc(label)}</div>` : ''}${s.title ? `<div class="psg-title">${esc(s.title)}</div>` : ''}
      <blockquote class="psg-text${s.verse ? ' verse' : ''}">${(s.paragraphs || []).map(para).join('')}</blockquote>
      ${fns ? `<div class="fns">${fns}</div>` : ''}
      <div class="attr">${s.attribution ? `<span class="who">${esc(s.attribution)}</span>` : ''}${s.translation ? `<span class="tr">${esc(s.translation)}</span>` : ''}</div>
      ${opt.glossary ? glossaryHTML(s.glossary) : ''}`;
  }
  function passage(s, opt) {
    return `<figure class="stim psg" aria-label="Source">${passageBody(s, opt, s.label || '')}</figure>`;
  }
  function pair(s, opt) {
    const items = s.items || [];
    return `<div class="pairset">${items.map((it, i) => `<figure class="stim psg" aria-label="${esc(it.label || 'Source ' + (i + 1))}">${passageBody(it, opt, it.label || ('Source ' + (i + 1)))}</figure>`).join('')}</div>`;
  }
  function image(s, opt) {
    const id = nid();
    const ratio = s.width && s.height ? ` style="aspect-ratio:${num(s.width)}/${num(s.height)}"` : '';
    return `<figure class="stim simg" aria-label="Image source">${s.title ? `<div class="psg-title">${esc(s.title)}</div>` : ''}
      <div class="imgbox"${ratio}><img src="${esc(s.src)}" alt="${esc(s.alt || '')}" loading="lazy" decoding="async" referrerpolicy="no-referrer" onerror="this.closest('.imgbox').classList.add('broken')"><div class="imgfail" role="note"><b>The image didn't load.</b> ${esc(s.description || s.alt || '')}</div></div>
      ${s.caption ? `<p class="icap">${esc(s.caption)}</p>` : ''}
      <div class="attr">${s.attribution ? `<span class="who">${esc(s.attribution)}</span>` : ''}${s.credit ? `<span class="tr">${esc(s.credit)}</span>` : ''}</div>
      ${s.description ? `<details class="gloss"><summary>Image description</summary><p class="idesc" id="${id}">${esc(s.description)}</p></details>` : ''}
      ${opt.glossary ? glossaryHTML(s.glossary) : ''}</figure>`;
  }

  /* ---------- table ---------- */
  function tableHTML(t, caption) {
    const cols = t.columns || [], rows = t.rows || [];
    return `<div class="tscroll"><table class="stab"${caption ? ` aria-label="${esc(caption)}"` : ''}><thead><tr>${cols.map(c => `<th scope="col">${esc(c)}</th>`).join('')}</tr></thead><tbody>${rows.map(r => `<tr>${r.map((c, i) => i === 0 ? `<th scope="row">${esc(c)}</th>` : `<td>${esc(c)}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`;
  }
  function table(s) {
    return `<figure class="stim stim-table">${title(s.title)}${tableHTML(s, s.title)}${s.text ? `<p class="stim-text">${esc(s.text)}</p>` : ''}${s.note ? `<p class="stim-note">${esc(s.note)}</p>` : ''}${source(s.source)}</figure>`;
  }

  /* ---------- grouped bar chart (inline SVG) ---------- */
  function niceStep(raw) {
    const p = Math.pow(10, Math.floor(Math.log10(raw || 1)));
    const f = raw / p;
    const m = f <= 1 ? 1 : f <= 2 ? 2 : f <= 2.5 ? 2.5 : f <= 5 ? 5 : 10;
    return m * p;
  }
  function bar(s) {
    const cats = s.categories || [], series = s.series || [];
    const maxV = Math.max(1, ...series.flatMap(sr => (sr.values || []).map(num)));
    const yMax = num(s.yMax) > 0 ? num(s.yMax) : niceStep(maxV / 5) * 5;
    const W = 640, H = 380, m = { t: 20, r: 18, b: 56, l: 70 };
    const pw = W - m.l - m.r, ph = H - m.t - m.b;
    const step = niceStep(yMax / 5);
    const y = v => m.t + ph - (v / yMax) * ph;
    const gw = pw / Math.max(1, cats.length), n = Math.max(1, series.length);
    const bw = Math.min(58, (gw * 0.72) / n), groupW = bw * n;
    const id = nid(), tid = id + 't', did = id + 'd';
    let grid = '';
    for (let v = 0; v <= yMax + 1e-9; v += step) {
      grid += `<line class="grid" x1="${m.l}" x2="${W - m.r}" y1="${r1(y(v))}" y2="${r1(y(v))}"/><text class="tick" x="${m.l - 9}" y="${r1(y(v) + 4)}" text-anchor="end">${fmt(v)}</text>`;
    }
    let bars = '';
    cats.forEach((c, ci) => {
      const x0 = m.l + ci * gw + (gw - groupW) / 2;
      series.forEach((sr, si) => {
        const v = num((sr.values || [])[ci]);
        const x = x0 + si * bw, h = Math.max(0, ph * (v / yMax));
        bars += `<rect class="bar s${si}" x="${r1(x + 3)}" y="${r1(y(v))}" width="${r1(bw - 6)}" height="${r1(h)}" rx="3"><title>${esc(c)} · ${esc(sr.name)}: ${fmt(v)}</title></rect>`;
        if (si === 1) bars += `<rect x="${r1(x + 3)}" y="${r1(y(v))}" width="${r1(bw - 6)}" height="${r1(h)}" rx="3" fill="url(#${id}h)" pointer-events="none"/>`;
        bars += `<text class="val" x="${r1(x + bw / 2)}" y="${r1(y(v) - 6)}" text-anchor="middle">${fmt(v)}</text>`;
      });
      const cx = r1(m.l + ci * gw + gw / 2), lines = String(c).split('\n');
      bars += `<text class="cat" x="${cx}" y="${H - m.b + 22}" text-anchor="middle">${lines.map((ln, li) => `<tspan x="${cx}" dy="${li ? 15 : 0}">${esc(ln)}</tspan>`).join('')}</text>`;
    });
    const axes = `<line class="axis" x1="${m.l}" x2="${m.l}" y1="${m.t}" y2="${m.t + ph}"/><line class="axis" x1="${m.l}" x2="${W - m.r}" y1="${m.t + ph}" y2="${m.t + ph}"/>`;
    const ylab = s.yLabel ? `<text class="ylab" transform="translate(16 ${r1(m.t + ph / 2)}) rotate(-90)" text-anchor="middle">${esc(s.yLabel)}</text>` : '';
    const legend = `<div class="legend" aria-hidden="true">${series.map((sr, i) => `<span class="lg"><i class="sw s${i}"></i>${esc(sr.name)}</span>`).join('')}</div>`;
    const desc = `Grouped bar chart with ${cats.length} categories and ${series.length} series. ` + cats.map((c, ci) => `${String(c).replace(/\n/g, ' ')}: ` + series.map(sr => `${sr.name} ${fmt(num((sr.values || [])[ci]))}`).join(', ')).join('. ') + '.';
    const srTable = `<div class="sr-only"><table><caption>${esc(s.title || 'Chart data')}</caption><thead><tr><th scope="col">Category</th>${series.map(sr => `<th scope="col">${esc(sr.name)}</th>`).join('')}</tr></thead><tbody>${cats.map((c, ci) => `<tr><th scope="row">${esc(String(c).replace(/\n/g, ' '))}</th>${series.map(sr => `<td>${fmt(num((sr.values || [])[ci]))}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`;
    return `<figure class="stim stim-bar">${title(s.title)}${legend}<div class="chart"><svg viewBox="0 0 ${W} ${H}" role="img" aria-labelledby="${tid} ${did}"><title id="${tid}">${esc(s.title || 'Bar chart')}</title><desc id="${did}">${esc(desc)}</desc><defs><pattern id="${id}h" patternUnits="userSpaceOnUse" width="6" height="6" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="6" stroke="rgba(255,255,255,.55)" stroke-width="2"/></pattern></defs>${grid}${axes}${bars}${ylab}</svg></div>${srTable}${s.text ? `<p class="stim-text">${esc(s.text)}</p>` : ''}${source(s.source)}</figure>`;
  }

  /* ---------- district maps ---------- */
  function districtMap(s) {
    const g = s.grid || {}, R = num(g.rows) || (g.blueShare || []).length, C = num(g.cols) || ((g.blueShare || [])[0] || []).length;
    const bs = g.blueShare || [];
    const cell = 50, pad = 4, W = C * cell + pad * 2, H = R * cell + pad * 2;
    const plans = (s.plans || []).map((p, pi) => {
      const dmap = {};
      (p.districts || []).forEach((d, di) => d.forEach(rc => { dmap[rc[0] + ',' + rc[1]] = di; }));
      let cells = '', borders = '';
      const X = c => pad + c * cell, Y = r => pad + r * cell;
      for (let r = 0; r < R; r++) for (let c = 0; c < C; c++) {
        const v = num((bs[r] || [])[c]);
        const blue = v >= 50;
        cells += `<rect class="pc ${blue ? 'blue' : 'orange'}" x="${X(c)}" y="${Y(r)}" width="${cell}" height="${cell}"/><text class="pval" x="${X(c) + cell / 2}" y="${Y(r) + cell / 2 + 5}" text-anchor="middle">${fmt(v)}</text>`;
        const me = dmap[r + ',' + c];
        const diff = (rr, cc) => rr < 0 || cc < 0 || rr >= R || cc >= C || dmap[rr + ',' + cc] !== me;
        if (diff(r - 1, c)) borders += `<line class="dline" x1="${X(c)}" y1="${Y(r)}" x2="${X(c) + cell}" y2="${Y(r)}"/>`;
        if (diff(r, c - 1)) borders += `<line class="dline" x1="${X(c)}" y1="${Y(r)}" x2="${X(c)}" y2="${Y(r) + cell}"/>`;
        if (diff(r + 1, c)) borders += `<line class="dline" x1="${X(c)}" y1="${Y(r) + cell}" x2="${X(c) + cell}" y2="${Y(r) + cell}"/>`;
        if (diff(r, c + 1)) borders += `<line class="dline" x1="${X(c) + cell}" y1="${Y(r)}" x2="${X(c) + cell}" y2="${Y(r) + cell}"/>`;
      }
      const did = nid();
      const desc = (p.districts || []).map((d, di) => `District ${di + 1}: ` + d.map(rc => `row ${rc[0] + 1} column ${rc[1] + 1} (${fmt(num((bs[rc[0]] || [])[rc[1]]))}% Blue)`).join(', ')).join('. ');
      return `<figure class="dplan"><svg viewBox="0 0 ${W} ${H}" role="img" aria-labelledby="${did}"><title id="${did}">${esc(p.name || 'Plan ' + (pi + 1))}. ${esc(desc)}</title><g>${cells}</g><g>${borders}</g></svg><figcaption>${esc(p.name || 'Plan ' + (pi + 1))}</figcaption></figure>`;
    });
    const legend = `<div class="legend"><span class="lg"><i class="sw pblue"></i>Majority Blue Party (≥ 50)</span><span class="lg"><i class="sw porange"></i>Majority Orange Party (&lt; 50)</span><span class="lg"><i class="sw dline"></i>District boundary</span></div>`;
    return `<figure class="stim stim-dmap dmap">${title(s.title)}${s.note ? `<p class="stim-note">${esc(s.note)}</p>` : ''}<div class="dplans">${plans.join('')}</div>${legend}${s.resultsTable ? `<div class="dresults">${title(s.resultsTable.title)}${tableHTML(s.resultsTable, s.resultsTable.title)}</div>` : ''}${source(s.source)}</figure>`;
  }

  /* ---------- schematic maps ---------- */
  const pts = poly => (poly || []).map(p => `${r1(num(p[0]))},${r1(num(p[1]))}`).join(' ');
  function bbox(poly) {
    const xs = poly.map(p => num(p[0])), ys = poly.map(p => num(p[1]));
    return { x1: Math.min(...xs), y1: Math.min(...ys), x2: Math.max(...xs), y2: Math.max(...ys) };
  }
  const contains = (a, b) => a.x1 <= b.x1 && a.y1 <= b.y1 && a.x2 >= b.x2 && a.y2 >= b.y2 && (a.x2 - a.x1) * (a.y2 - a.y1) > (b.x2 - b.x1) * (b.y2 - b.y1);
  function wrap(text, max) {
    const words = String(text || '').split(/\s+/), lines = []; let cur = '';
    words.forEach(w => { if ((cur + ' ' + w).trim().length > max && cur) { lines.push(cur); cur = w; } else cur = (cur + ' ' + w).trim(); });
    if (cur) lines.push(cur);
    return lines;
  }
  function star(cx, cy, R, r, n) {
    let d = '';
    for (let i = 0; i < n * 2; i++) {
      const a = Math.PI / n * i - Math.PI / 2, rad = i % 2 ? r : R;
      d += (i ? 'L' : 'M') + r1(cx + rad * Math.cos(a)) + ',' + r1(cy + rad * Math.sin(a));
    }
    return d + 'Z';
  }
  function ownerKey(owner) { return String(owner || '').replace(/\s*\(.*$/, '').trim() || 'owner'; }

  function schematicMap(s) {
    const cv = s.canvas || {}, W = num(cv.width) || 800, H = num(cv.height) || 400;
    const feats = Array.isArray(s.features) ? s.features : [];
    const id = nid();
    const L = { claims: '', zones: '', hatchZones: '', land: '', lines: '', markers: '', labels: '', arrows: '', scale: '', brackets: '' };
    const owners = [];
    const ownerIdx = o => { const k = ownerKey(o); let i = owners.indexOf(k); if (i < 0) { owners.push(k); i = owners.length - 1; } return i; };
    const claimShapes = {};
    const zones = feats.filter(f => f.kind === 'zone' && Array.isArray(f.polygon));
    const zb = zones.map(z => bbox(z.polygon));
    const descBits = [];

    feats.forEach((f, fi) => {
      const kind = f.kind;
      if (kind === 'land' && Array.isArray(f.polygon)) {
        const cls = f.style === 'power' ? 'power' : f.style === 'small' ? 'small' : '';
        L.land += `<polygon class="land ${cls}" points="${pts(f.polygon)}"><title>${esc(f.name || 'Land')}</title></polygon>`;
        if (f.labelAt && f.name) {
          const lb = bbox(f.polygon), perChar = f.style === 'power' ? 10.5 : 8.5;
          const lines = wrap(f.name, Math.max(8, Math.floor((lb.x2 - lb.x1 - 8) / perChar)));
          const lh = f.style === 'power' ? 22 : 18, y0 = num(f.labelAt[1]) + 6 - (lines.length - 1) * lh / 2;
          lines.forEach((ln, i) => { L.labels += `<text class="lbl ${f.style === 'power' ? 'big' : ''}" x="${r1(num(f.labelAt[0]))}" y="${r1(y0 + i * lh)}">${esc(ln)}</text>`; });
        }
        descBits.push(f.name);
      } else if (kind === 'territorialSea') {
        const oi = ownerIdx(f.owner);
        let shape = '';
        if (f.circle && f.circle.center) shape = `<circle cx="${r1(num(f.circle.center[0]))}" cy="${r1(num(f.circle.center[1]))}" r="${r1(num(f.circle.radius))}"/>`;
        else if (Array.isArray(f.polygon)) shape = `<polygon points="${pts(f.polygon)}"/>`;
        (claimShapes[oi] = claimShapes[oi] || []).push(shape);
        descBits.push(`${f.owner || 'claim'} territorial sea claim`);
      } else if (kind === 'island' && f.center) {
        const cx = r1(num(f.center[0])), cy = r1(num(f.center[1])), rr = r1(num(f.radius) || 10);
        L.land += `<circle class="island" cx="${cx}" cy="${cy}" r="${rr}"><title>${esc(f.name || 'Island')}</title></circle>`;
        if (f.name) L.labels += `<text class="lbl sm" x="${cx}" y="${r1(cy + rr + 15)}">${esc(f.name)}</text>`;
        descBits.push(f.name);
      } else if (kind === 'zone' && Array.isArray(f.polygon)) {
        const zi = zones.indexOf(f), b = zb[zi];
        const inside = zb.some((o, j) => j !== zi && contains(o, b));
        const holds = zb.some((o, j) => j !== zi && contains(b, o));
        const shade = Math.min(3, zi);
        if (inside) L.hatchZones += `<polygon class="zone hatch" points="${pts(f.polygon)}" fill="url(#${id}zh)"><title>${esc(f.name || 'Zone')}</title></polygon>`;
        else { const poly = `<polygon class="zone z${shade}" points="${pts(f.polygon)}"><title>${esc(f.name || 'Zone')}</title></polygon>`; L.zones = holds ? poly + L.zones : L.zones + poly; }
        if (holds) L.brackets += `<path class="bracket" d="M${r1(b.x1 + 3)},${r1(b.y2 - 16)} v9 H${r1(b.x2 - 3)} v-9"/>`;
        if (f.labelAt) {
          const lx = r1(num(f.labelAt[0])), ly = r1(num(f.labelAt[1]));
          L.labels += `<text class="lbl" x="${lx}" y="${ly}">${esc(f.name || '')}</text>`;
          if (f.sublabel) wrap(f.sublabel, Math.max(10, Math.min(30, Math.floor((b.x2 - b.x1 - 10) / 6.6)))).forEach((ln, i) => { L.labels += `<text class="sub" x="${lx}" y="${ly + 17 + i * 14}">${esc(ln)}</text>`; });
        }
        descBits.push(`${f.name}${f.sublabel ? ' (' + f.sublabel + ')' : ''}`);
      } else if ((kind === 'line' || kind === 'shippingLane') && Array.isArray(f.line)) {
        const dash = f.dashed ? ` stroke-dasharray="${kind === 'shippingLane' ? '14 9' : '7 6'}"` : '';
        L.lines += `<polyline class="${kind === 'shippingLane' ? 'lane' : 'line'}" points="${pts(f.line)}"${dash}><title>${esc(f.name || kind)}</title></polyline>`;
        descBits.push(f.name || kind);
      } else if (kind === 'marker' && Array.isArray(f.points)) {
        f.points.forEach(p => {
          const x = r1(num(p[0])), y = r1(num(p[1]));
          if (f.symbol === 'conflict') L.markers += `<path class="conflict" d="${star(x, y, 11, 5, 8)}"><title>${esc(f.name || 'Conflict')}</title></path>`;
          else if (f.symbol === 'baseN' || f.symbol === 'baseS') L.markers += `<rect class="${f.symbol}" x="${x - 7}" y="${y - 7}" width="14" height="14" rx="2"><title>${esc(f.name || 'Base')}</title></rect>`;
          else if (f.symbol === 'house') L.markers += `<path class="house" d="M${x - 7},${y + 6} V${y - 1} L${x},${y - 7} L${x + 7},${y - 1} V${y + 6} Z"><title>${esc(f.name || 'House')}</title></path>`;
          else L.markers += `<circle class="baseN" cx="${x}" cy="${y}" r="6"><title>${esc(f.name || 'Marker')}</title></circle>`;
        });
        descBits.push(`${f.name || 'markers'} at ${f.points.length} location${f.points.length === 1 ? '' : 's'}`);
      } else if (kind === 'arrow' && f.from && f.to) {
        L.arrows += `<line class="arrow" x1="${r1(num(f.from[0]))}" y1="${r1(num(f.from[1]))}" x2="${r1(num(f.to[0]))}" y2="${r1(num(f.to[1]))}" marker-end="url(#${id}ah)"><title>${esc(f.name || 'Arrow')}</title></line>`;
        descBits.push(f.name || 'arrow');
      } else if (kind === 'scaleBar' && f.from && f.to) {
        const x1 = r1(num(f.from[0])), y1 = r1(num(f.from[1])), x2 = r1(num(f.to[0])), y2 = r1(num(f.to[1]));
        L.scale += `<line class="scale" x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}"/><line class="scale" x1="${x1}" y1="${y1 - 5}" x2="${x1}" y2="${y1 + 5}"/><line class="scale" x1="${x2}" y1="${y2 - 5}" x2="${x2}" y2="${y2 + 5}"/>${f.label ? `<text class="scalelbl" x="${r1((x1 + x2) / 2)}" y="${y1 - 8}">${esc(f.label)}</text>` : ''}`;
      }
    });
    Object.keys(claimShapes).forEach(oi => {
      const i = +oi, cls = i === 0 ? 'a' : 'b';
      L.claims += `<g class="claim ${cls}" opacity="${i === 0 ? '.38' : '.34'}">${claimShapes[oi].join('')}</g>`;
      if (i === 1) L.claims += `<g fill="url(#${id}ch)" opacity=".9">${claimShapes[oi].join('')}</g>`;
    });
    const legend = Array.isArray(s.legend) && s.legend.length ? `<div class="legend">${s.legend.map(item => `<span class="lg">${swatch(item.swatch)}${esc(item.label)}</span>`).join('')}</div>` : '';
    const tid = id + 't', did = id + 'd';
    const desc = (s.description ? s.description + ' ' : '') + 'Map features: ' + descBits.filter(Boolean).join('; ') + '.';
    const svg = `<div class="smap"><svg viewBox="0 0 ${W} ${H}" role="img" aria-labelledby="${tid} ${did}"><title id="${tid}">${esc(s.title || 'Map')}</title><desc id="${did}">${esc(desc)}</desc><defs><pattern id="${id}zh" patternUnits="userSpaceOnUse" width="9" height="9" patternTransform="rotate(45)"><line class="hatchline" x1="0" y1="0" x2="0" y2="9"/></pattern><pattern id="${id}ch" patternUnits="userSpaceOnUse" width="10" height="10" patternTransform="rotate(-45)"><line class="claim-hatch" x1="0" y1="0" x2="0" y2="10"/></pattern><marker id="${id}ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path class="arrowhead" d="M0,0 L10,5 L0,10 z"/></marker></defs><rect class="water" x="0" y="0" width="${W}" height="${H}"/>${L.zones}${L.hatchZones}${L.claims}${L.land}${L.lines}${L.brackets}${L.markers}${L.arrows}${L.labels}${L.scale}</svg></div>`;
    return `<figure class="stim stim-smap">${title(s.title)}${svg}${legend}${s.description ? `<p class="stim-desc">${esc(s.description)}</p>` : ''}${s.note ? `<p class="stim-note">${esc(s.note)}</p>` : ''}${source(s.source)}</figure>`;
  }
  /* ---------- von Thünen-style concentric ring diagram ---------- */
  function rings(s) {
    const rs = Array.isArray(s.rings) ? s.rings : [];
    const W = 640, H = 420, cx = 320, cy = 210, r0 = 46, step = Math.max(28, Math.floor((190 - r0) / Math.max(1, rs.length)));
    const id = nid(), tid = id + 't', did = id + 'd';
    let body = '', labels = '';
    for (let i = rs.length - 1; i >= 0; i--) {
      const R = r0 + step * (i + 1);
      body += `<circle class="ring r${i % 4}" cx="${cx}" cy="${cy}" r="${R}"><title>${esc('Ring ' + (rs[i].label || i + 1))}</title></circle>`;
    }
    rs.forEach((rg, i) => {
      const mid = r0 + step * i + step / 2;
      [[cx + mid, cy], [cx - mid, cy], [cx, cy - mid], [cx, cy + mid]].forEach(([x, y]) => {
        labels += `<text class="rlbl" x="${r1(x)}" y="${r1(y + 6)}">${esc(rg.label || String(i + 1))}</text>`;
      });
    });
    const outerR = r0 + step * rs.length;
    const outer = s.outer ? `<text class="rout" x="${W - 14}" y="${H - 14}" text-anchor="end">${esc(s.outer)}</text><text class="rout" x="14" y="26" text-anchor="start">${esc(s.outer)}</text>` : '';
    const center = `<circle class="rcity" cx="${cx}" cy="${cy}" r="${r0}"/>` + wrap(s.center || 'Market', 10).map((ln, i, a) => `<text class="rcl" x="${cx}" y="${r1(cy + 5 - (a.length - 1) * 8 + i * 16)}">${esc(ln)}</text>`).join('');
    const desc = (s.description ? s.description + ' ' : '') + `Rings from the center outward: ${rs.map((rg, i) => rg.label || i + 1).join(', ')}.`;
    const svg = `<div class="smap rings"><svg viewBox="0 0 ${W} ${H}" role="img" aria-labelledby="${tid} ${did}"><title id="${tid}">${esc(s.title || 'Ring diagram')}</title><desc id="${did}">${esc(desc)}</desc><rect class="rbg" x="0" y="0" width="${W}" height="${H}"/>${body}${center}${labels}${outer}<circle class="rline" cx="${cx}" cy="${cy}" r="${outerR}"/></svg></div>`;
    return `<figure class="stim stim-rings">${title(s.title)}${svg}${s.description ? `<p class="stim-desc">${esc(s.description)}</p>` : ''}${s.note ? `<p class="stim-note">${esc(s.note)}</p>` : ''}${source(s.source)}</figure>`;
  }

  function swatch(key) {
    switch (key) {
      case 'power': case 'small': case 'land': return `<i class="sw ${key}"></i>`;
      case 'conflict': return `<svg viewBox="0 0 22 16" aria-hidden="true"><path class="conflict" d="${star(11, 8, 7.5, 3.5, 8)}" style="fill:var(--conflict);stroke:#fff"/></svg>`;
      case 'baseN': return `<svg viewBox="0 0 22 16" aria-hidden="true"><rect x="5" y="2" width="12" height="12" rx="2" style="fill:var(--base-n)"/></svg>`;
      case 'baseS': return `<svg viewBox="0 0 22 16" aria-hidden="true"><rect x="5" y="2" width="12" height="12" rx="2" style="fill:var(--base-s)"/></svg>`;
      case 'territorialSeaA': return `<svg viewBox="0 0 22 16" aria-hidden="true"><rect width="22" height="16" rx="3" style="fill:var(--stim-water)"/><rect width="22" height="16" rx="3" style="fill:var(--claim-a);opacity:.38"/></svg>`;
      case 'territorialSeaB': return `<svg viewBox="0 0 22 16" aria-hidden="true"><rect width="22" height="16" rx="3" style="fill:var(--stim-water)"/><rect width="22" height="16" rx="3" style="fill:var(--claim-b);opacity:.34"/><path d="M-2,8 L8,-2 M4,18 L18,2 M12,18 L24,6" style="stroke:var(--claim-b);stroke-width:2.2"/></svg>`;
      case 'overlap': return `<svg viewBox="0 0 22 16" aria-hidden="true"><rect width="22" height="16" rx="3" style="fill:var(--stim-water)"/><rect width="22" height="16" rx="3" style="fill:var(--claim-a);opacity:.38"/><rect width="22" height="16" rx="3" style="fill:var(--claim-b);opacity:.34"/><path d="M-2,8 L8,-2 M4,18 L18,2 M12,18 L24,6" style="stroke:var(--claim-b);stroke-width:2.2"/></svg>`;
      case 'lane': return `<svg viewBox="0 0 22 16" aria-hidden="true"><line x1="1" y1="8" x2="21" y2="8" style="stroke:var(--lane);stroke-width:3" stroke-dasharray="6 4"/></svg>`;
      case 'water': return `<svg viewBox="0 0 22 16" aria-hidden="true"><rect width="22" height="16" rx="3" style="fill:var(--stim-water);stroke:var(--stim-land-stroke);stroke-width:1"/></svg>`;
      case 'house': return `<svg viewBox="0 0 22 16" aria-hidden="true"><path class="house" d="M4,15 V8 L11,2 L18,8 V15 Z"/></svg>`;
      case 'road': return `<svg viewBox="0 0 22 16" aria-hidden="true"><line x1="1" y1="8" x2="21" y2="8" style="stroke:var(--ink);stroke-width:2" stroke-dasharray="5 4"/></svg>`;
      default: return `<i class="sw generic"></i>`;
    }
  }

  return { render, esc };
})();
