/* GeoArcade · AP Practice Exam · stimulus renderer
   Everything here is driven by the JSON stimulus object; nothing is hard-coded per question.
   Supported stimulus.type: table | bar | line | pyramid | districtMap | schematicMap | rings.
   Anything else -> "stimulus unavailable" card. */
window.PE_STIM = (function () {
  'use strict';
  const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  let uid = 0;
  const nid = () => 'st' + (++uid) + '_' + Math.random().toString(36).slice(2, 6);
  const num = v => (typeof v === 'number' && isFinite(v)) ? v : (parseFloat(v) || 0);
  const fmt = v => Number.isInteger(v) ? v.toLocaleString('en-US') : (+v).toLocaleString('en-US', { maximumFractionDigits: 1 });
  const r1 = v => Math.round(v * 10) / 10;

  function render(stim) {
    if (!stim || typeof stim !== 'object') return unavailable();
    try {
      switch (stim.type) {
        case 'table': return table(stim);
        case 'bar': return bar(stim);
        case 'line': return line(stim);
        case 'pyramid': return pyramid(stim);
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
    return `<figure class="stim unavail" role="note"><div>⚠︎ Stimulus unavailable${type ? ` <span class="muted">(${esc(type)})</span>` : ''}</div><div class="small muted">You can still answer the question. Tell your AP Human Geography teacher which question this is.</div></figure>`;
  }
  const title = t => t ? `<figcaption class="stim-title">${esc(t)}</figcaption>` : '';
  const source = s => s ? `<div class="stim-source">Source: ${esc(s)}</div>` : '';

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
      bars += `<text class="cat" x="${r1(m.l + ci * gw + gw / 2)}" y="${H - m.b + 22}" text-anchor="middle">${esc(c)}</text>`;
    });
    const axes = `<line class="axis" x1="${m.l}" x2="${m.l}" y1="${m.t}" y2="${m.t + ph}"/><line class="axis" x1="${m.l}" x2="${W - m.r}" y1="${m.t + ph}" y2="${m.t + ph}"/>`;
    const ylab = s.yLabel ? `<text class="ylab" transform="translate(16 ${r1(m.t + ph / 2)}) rotate(-90)" text-anchor="middle">${esc(s.yLabel)}</text>` : '';
    const legend = `<div class="legend" aria-hidden="true">${series.map((sr, i) => `<span class="lg"><i class="sw s${i}"></i>${esc(sr.name)}</span>`).join('')}</div>`;
    const desc = `Grouped bar chart with ${cats.length} categories and ${series.length} series. ` + cats.map((c, ci) => `${c}: ` + series.map(sr => `${sr.name} ${fmt(num((sr.values || [])[ci]))}`).join(', ')).join('. ') + '.';
    const srTable = `<div class="sr-only"><table><caption>${esc(s.title || 'Chart data')}</caption><thead><tr><th scope="col">Category</th>${series.map(sr => `<th scope="col">${esc(sr.name)}</th>`).join('')}</tr></thead><tbody>${cats.map((c, ci) => `<tr><th scope="row">${esc(c)}</th>${series.map(sr => `<td>${fmt(num((sr.values || [])[ci]))}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`;
    return `<figure class="stim stim-bar">${title(s.title)}${legend}<div class="chart"><svg viewBox="0 0 ${W} ${H}" role="img" aria-labelledby="${tid} ${did}"><title id="${tid}">${esc(s.title || 'Bar chart')}</title><desc id="${did}">${esc(desc)}</desc><defs><pattern id="${id}h" patternUnits="userSpaceOnUse" width="6" height="6" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="6" stroke="rgba(255,255,255,.55)" stroke-width="2"/></pattern></defs>${grid}${axes}${bars}${ylab}</svg></div>${srTable}${s.text ? `<p class="stim-text">${esc(s.text)}</p>` : ''}${source(s.source)}</figure>`;
  }

  /* ---------- shared helpers for line + pyramid ---------- */
  // Pick a "nice" axis from lo up to at least hi with at most maxTicks steps (steps of 1/2/5 x 10^n first,
  // 2.5 only if nothing else works). If fixedHi is given (author's yMax / xMax) it is kept and the step must land
  // on it. fits(step, k), if given, rejects steps whose tick labels would collide.
  function axisFor(lo, hi, maxTicks, fixedHi, fits) {
    const span = Math.max(1e-9, (fixedHi != null ? fixedHi : hi) - lo);
    const p0 = Math.pow(10, Math.floor(Math.log10(span / maxTicks)) - 1);
    for (const ms of [[1, 2, 5], [1, 2, 2.5, 5]]) {
      const cands = [];
      for (let p = p0; p <= p0 * 1e5; p *= 10) ms.forEach(m => cands.push(+(m * p).toPrecision(6)));
      if (fixedHi != null) {
        const ok = cands.filter(st => { const k = span / st; return k >= 2 - 1e-9 && k <= maxTicks + 1e-9 && Math.abs(k - Math.round(k)) < 1e-6 && (!fits || fits(st, Math.round(k))); });
        if (ok.length) return { lo, hi: fixedHi, step: ok[0] };              // smallest step = most ticks that fit
        continue;
      }
      let best = null;
      cands.forEach(st => {
        const k = Math.ceil((hi - lo) / st - 1e-9); if (k < 1 || k > maxTicks || (fits && !fits(st, k))) return;
        const top = +(lo + k * st).toPrecision(10);
        if (!best || top < best.hi - 1e-9 || (Math.abs(top - best.hi) < 1e-9 && k > best.k)) best = { lo, hi: top, step: st, k };
      });
      if (best) return best;
    }
    const st = niceStep(span / maxTicks);
    return { lo, hi: fixedHi != null ? fixedHi : lo + Math.ceil(span / st) * st, step: st };
  }
  const decOf = st => { const t = String(+(+st).toPrecision(6)); const i = t.indexOf('.'); return i < 0 ? 0 : Math.min(3, t.length - i - 1); };
  const fmtD = (v, d) => (+v).toLocaleString('en-US', { minimumFractionDigits: d, maximumFractionDigits: d });
  const fmt2 = v => (+v).toLocaleString('en-US', { maximumFractionDigits: 2 });
  const ticksOf = ax => { const out = []; for (let k = 0; k < 60; k++) { const v = +(ax.lo + k * ax.step).toPrecision(10); if (v > ax.hi + ax.step * 1e-6) break; out.push(v); } return out; };
  const valOrNull = v => (v == null || v === '' || !isFinite(+v)) ? null : +v;
  const tail = s => `${s.description ? `<p class="stim-desc">${esc(s.description)}</p>` : ''}${s.text ? `<p class="stim-text">${esc(s.text)}</p>` : ''}${s.note ? `<p class="stim-note">${esc(s.note)}</p>` : ''}${source(s.source)}`;

  /* ---------- multi-series line chart (inline SVG) ----------
     Series stay distinguishable without color: each has its own marker shape AND dash pattern
     (blue solid ●, orange dashed ■, teal dotted ▲, ink dash-dot ◆, magenta long-dash ▼).
     Three SVG layouts are emitted (wide 640, medium 480, narrow 360 user units); a container query on the
     figure shows the one that keeps labels legible, so the chart never needs a sideways scroll. */
  const DASH = ['', '9 5', '2.5 4', '12 4 2.5 4', '18 6'];
  function mkPath(k, x, y, r) {
    switch (k % 5) {
      case 1: { const a = r * 0.9; return `M${r1(x - a)},${r1(y - a)}h${r1(2 * a)}v${r1(2 * a)}h${r1(-2 * a)}Z`; }
      case 2: { const a = r * 1.22; return `M${r1(x)},${r1(y - a)}L${r1(x + a * 0.95)},${r1(y + a * 0.62)}L${r1(x - a * 0.95)},${r1(y + a * 0.62)}Z`; }
      case 3: { const a = r * 1.25; return `M${r1(x)},${r1(y - a)}L${r1(x + a)},${r1(y)}L${r1(x)},${r1(y + a)}L${r1(x - a)},${r1(y)}Z`; }
      case 4: { const a = r * 1.22; return `M${r1(x)},${r1(y + a)}L${r1(x + a * 0.95)},${r1(y - a * 0.62)}L${r1(x - a * 0.95)},${r1(y - a * 0.62)}Z`; }
      default: return `M${r1(x - r)},${r1(y)}a${r},${r} 0 1,0 ${2 * r},0a${r},${r} 0 1,0 ${-2 * r},0Z`;
    }
  }
  // wrap that may also break after hyphens ("Lower-middle-income" -> "Lower-middle-" / "income"); no regex lookbehind (old Safari)
  function wrapLabel(text, max) {
    const toks = String(text || '').replace(/-/g, '-\u0001').split(/\s+|\u0001/).filter(Boolean), lines = []; let cur = '';
    toks.forEach(t => { const j = cur ? (cur.endsWith('-') ? cur + t : cur + ' ' + t) : t; if (j.length > max && cur) { lines.push(cur); cur = t; } else cur = j; });
    if (cur) lines.push(cur);
    return lines;
  }
  const dashAttr = si => DASH[si % 5] ? ` stroke-dasharray="${DASH[si % 5]}"` : '';
  function lineSVG(s, cats, series, vals, ax, o) {
    const W = o.W, H = o.H, narrow = o.size === 'nar', id = nid(), tid = id + 't', did = id + 'd';
    const dec = decOf(ax.step), ticks = ticksOf(ax), tl = v => fmtD(v, dec);
    const cw = o.size === 'wid' ? 7.4 : 7.6;                         // rough user units per character at the tick font size
    const maxTL = Math.max(1, ...ticks.map(v => tl(v).length));
    const yTop = narrow && s.yLabel ? wrap(s.yLabel, Math.floor((W - 8) / 7)) : [];
    const m = { t: narrow ? (yTop.length ? 10 + yTop.length * 15 + 8 : 14) : 18, r: narrow ? 16 : 24, l: Math.round((s.yLabel && !narrow ? 30 : 4) + 10 + maxTL * cw), b: 0 };
    const n = cats.length, pad = narrow ? 12 : 18, pw = W - m.l - m.r;
    const X = i => n > 1 ? m.l + pad + i * (pw - 2 * pad) / (n - 1) : m.l + pw / 2;
    const spacing = n > 1 ? (pw - 2 * pad) / (n - 1) : W;
    // room for label i: half the gap to each neighbour, or (at either end) everything out to the chart edge
    const avail = i => (i === 0 ? X(0) - 2 : spacing / 2 - 3) + (i === n - 1 ? W - 2 - X(n - 1) : spacing / 2 - 3);
    let xl = cats.map(c => [c]), every = 1;
    if (cats.some((c, i) => c.length * cw > avail(i))) {
      // long names wrap (up to 3 lines, 4 on phones); years and other unbreakable labels are thinned instead
      const wr = cats.map((c, i) => { const per = Math.max(1, Math.floor(avail(i) / cw)); return { per, w: wrapLabel(c, per) }; });
      if (wr.every(o => o.w.length <= (narrow ? 4 : 3) && o.w.every(l => l.length <= o.per))) xl = wr.map(o => o.w);
      else every = Math.max(1, Math.ceil((Math.max(...cats.map(c => c.length)) * cw + 10) / spacing));
    }
    const xLines = Math.max(1, ...xl.map(a => a.length));
    const xLab = s.xLabel ? wrap(s.xLabel, Math.floor((W - 20) / 7)) : [];
    m.b = 18 + xLines * 15 + (xLab.length ? 6 + xLab.length * 16 : 0);
    const ph = H - m.t - m.b;
    const Y = v => m.t + ph - ((v - ax.lo) / ((ax.hi - ax.lo) || 1)) * ph;
    let g = '';
    ticks.forEach(v => { g += `<line class="grid" x1="${m.l}" x2="${W - m.r}" y1="${r1(Y(v))}" y2="${r1(Y(v))}"/><text class="tick" x="${m.l - 8}" y="${r1(Y(v) + 4.5)}" text-anchor="end">${tl(v)}</text>`; });
    const base = r1(Y(ax.lo));
    g += `<line class="axis" x1="${m.l}" x2="${m.l}" y1="${m.t}" y2="${base}"/><line class="axis" x1="${m.l}" x2="${W - m.r}" y1="${base}" y2="${base}"/>`;
    if (ax.lo < 0 && ax.hi > 0) g += `<line class="axis zero" x1="${m.l}" x2="${W - m.r}" y1="${r1(Y(0))}" y2="${r1(Y(0))}"/>`;
    cats.forEach((c, i) => {
      g += `<line class="axis" x1="${r1(X(i))}" x2="${r1(X(i))}" y1="${base}" y2="${base + 5}"/>`;
      if (i % every !== 0) return;
      const hw = Math.max(...xl[i].map(l => l.length)) * cw / 2, lx = Math.min(Math.max(X(i), hw + 2), W - hw - 2);   // keep edge labels inside the chart
      xl[i].forEach((ln, li) => { g += `<text class="cat" x="${r1(lx)}" y="${r1(base + 21 + li * 15)}" text-anchor="middle">${esc(ln)}</text>`; });
    });
    let lines = '', marks = '';
    series.forEach((sr, si) => {
      const v = vals[si]; let seg = [];
      const flush = () => { if (seg.length > 1) lines += `<polyline class="ln s${si % 5}" points="${seg.join(' ')}"${dashAttr(si)}/>`; seg = []; };
      v.forEach((y, i) => { if (y == null) flush(); else seg.push(`${r1(X(i))},${r1(Y(y))}`); });
      flush();
      v.forEach((y, i) => {
        if (y == null) return;
        marks += `<g class="pt"><title>${esc(cats[i])} · ${esc(sr.name)}: ${fmt2(y)}</title><circle class="hit" cx="${r1(X(i))}" cy="${r1(Y(y))}" r="11"/><path class="mk s${si % 5}" d="${mkPath(si, X(i), Y(y), 5)}"/></g>`;
      });
    });
    let labs = '';
    if (s.yLabel && !narrow) labs += `<text class="ylab" transform="translate(16 ${r1(m.t + ph / 2)}) rotate(-90)" text-anchor="middle">${esc(s.yLabel)}</text>`;
    yTop.forEach((ln, i) => { labs += `<text class="ylab" x="4" y="${14 + i * 15}">${esc(ln)}</text>`; });
    xLab.forEach((ln, i) => { labs += `<text class="xlab" x="${r1(m.l + pw / 2)}" y="${r1(base + 18 + xLines * 15 + 8 + i * 16)}" text-anchor="middle">${esc(ln)}</text>`; });
    return `<svg class="${o.size}" viewBox="0 0 ${W} ${H}" role="img" aria-labelledby="${tid} ${did}"><title id="${tid}">${esc(s.title || 'Line chart')}</title><desc id="${did}">${esc(o.desc)}</desc>${g}${lines}${marks}${labs}</svg>`;
  }
  function line(s) {
    const cats = (s.categories || []).map(String), series = (s.series || []).filter(sr => sr && typeof sr === 'object');
    const vals = series.map(sr => cats.map((_, i) => valOrNull((sr.values || [])[i])));
    const flat = vals.flat().filter(v => v != null);
    const dMax = flat.length ? Math.max(...flat) : 1, dMin = flat.length ? Math.min(...flat) : 0;
    const yMinSet = valOrNull(s.yMin) != null;
    let lo = yMinSet ? +s.yMin : Math.min(0, dMin);
    if (!yMinSet && lo < 0) { const st = niceStep((dMax - lo) / 5); lo = Math.floor(lo / st) * st; }
    const yMaxSet = valOrNull(s.yMax) != null && +s.yMax > lo && +s.yMax >= dMax;   // a yMax below the data is ignored
    const ax = axisFor(lo, Math.max(dMax, lo + 1e-6), 6, yMaxSet ? +s.yMax : null);
    const v2s = v => v == null ? 'no data' : fmt2(v);
    const desc = (s.description ? s.description + ' ' : '') + `Line chart with ${series.length} series${cats.length ? ` from ${cats[0]} to ${cats[cats.length - 1]}` : ''}.${s.yLabel ? ` Vertical axis: ${s.yLabel}, ${fmt2(ax.lo)} to ${fmt2(ax.hi)}.` : ''}${s.xLabel ? ` Horizontal axis: ${s.xLabel}.` : ''} ` + series.map((sr, si) => `${sr.name}: ` + cats.map((c, i) => `${c} ${v2s(vals[si][i])}`).join(', ')).join('. ') + '.';
    const key = si => `<svg class="lkey" viewBox="0 0 36 14" aria-hidden="true"><line class="ln s${si % 5}" x1="2" y1="7" x2="34" y2="7"${dashAttr(si)}/><path class="mk s${si % 5}" d="${mkPath(si, 18, 7, 4.5)}"/></svg>`;
    const legend = `<div class="legend" aria-hidden="true">${series.map((sr, si) => `<span class="lg">${key(si)}${esc(sr.name)}</span>`).join('')}</div>`;
    const srTable = `<div class="sr-only"><table><caption>${esc(s.title || 'Chart data')}</caption><thead><tr><th scope="col">${esc(s.xLabel || 'Category')}</th>${series.map(sr => `<th scope="col">${esc(sr.name)}</th>`).join('')}</tr></thead><tbody>${cats.map((c, i) => `<tr><th scope="row">${esc(c)}</th>${series.map((sr, si) => `<td>${v2s(vals[si][i])}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`;
    const svg = (size, W, H) => `<div class="lc-${size[0]}">${lineSVG(s, cats, series, vals, ax, { W, H, size, desc })}</div>`;
    return `<figure class="stim stim-line">${title(s.title)}${series.length > 1 ? legend : ''}<div class="chart lc">${svg('wid', 640, 360)}${svg('med', 480, 330)}${svg('nar', 360, 310)}</div>${srTable}${tail(s)}</figure>`;
  }

  /* ---------- population pyramid (back-to-back horizontal bars, inline SVG) ----------
     ageGroups are listed youngest first and drawn youngest at the bottom. Male bars run left, female right
     (orange + hatch, the same look as the bar chart's second series), so sex is never color-alone. */
  function pyramid(s) {
    const ages = (s.ageGroups || []).map(String), n = Math.max(1, ages.length);
    const pick = arr => ages.map((_, i) => { const v = valOrNull((arr || [])[i]); return v == null ? null : Math.max(0, v); });
    const male = pick(s.male), female = pick(s.female), pv = v => v == null ? 'no data' : fmt2(v);
    const dMax = Math.max(0.1, ...male.filter(v => v != null), ...female.filter(v => v != null));
    const maxLen = Math.max(3, ...ages.map(a => a.length));
    const W = 340, padX = 16, cw = Math.max(46, Math.round(maxLen * 7.6 + 12));
    const sw = (W - 2 * padX - cw) / 2, L0 = padX + sw, R0 = W - padX - sw;
    // tick labels are plain numbers (the axis title says "Percent of total population"); keep ~2 characters of air between them
    const tlab = v => fmt2(v);
    const fits = (st, k) => { let w = 0; for (let j = 1; j <= k; j++) w = Math.max(w, tlab(st * j).length); return sw / k >= w * 7.8 + 14; };
    const ax = axisFor(0, dMax, 5, num(s.xMax) >= dMax ? num(s.xMax) : null, fits), xMax = ax.hi;   // an xMax below the data is ignored
    const rh = Math.max(16, Math.min(30, 330 / n)), top = 40, ph = rh * ages.length, H = Math.round(top + ph + 52);
    const bh = r1(rh * 0.8), xlen = v => v == null ? 0 : Math.min(sw, (v / xMax) * sw);
    const id = nid(), tid = id + 't', did = id + 'd';
    const rbar = (x, y, w, h, left) => {
      if (w <= 0.05) return '';
      const r = Math.min(3, w / 2, h / 2);
      return left
        ? `M${r1(x + w)},${r1(y)}H${r1(x + r)}Q${r1(x)},${r1(y)} ${r1(x)},${r1(y + r)}V${r1(y + h - r)}Q${r1(x)},${r1(y + h)} ${r1(x + r)},${r1(y + h)}H${r1(x + w)}Z`
        : `M${r1(x)},${r1(y)}H${r1(x + w - r)}Q${r1(x + w)},${r1(y)} ${r1(x + w)},${r1(y + r)}V${r1(y + h - r)}Q${r1(x + w)},${r1(y + h)} ${r1(x + w - r)},${r1(y + h)}H${r1(x)}Z`;
    };
    const unit = '% of total population';
    let g = '', rows = '';
    ticksOf(ax).forEach(v => {
      const a = r1(L0 - xlen(v)), b = r1(R0 + xlen(v)), lab = tlab(v);
      g += `<line class="grid" x1="${a}" x2="${a}" y1="${top}" y2="${top + ph}"/><line class="grid" x1="${b}" x2="${b}" y1="${top}" y2="${top + ph}"/>`;
      g += `<text class="tick" x="${a}" y="${r1(top + ph + 17)}" text-anchor="middle">${lab}</text><text class="tick" x="${b}" y="${r1(top + ph + 17)}" text-anchor="middle">${lab}</text>`;
    });
    g += `<line class="axis" x1="${padX}" x2="${L0}" y1="${top + ph}" y2="${top + ph}"/><line class="axis" x1="${R0}" x2="${W - padX}" y1="${top + ph}" y2="${top + ph}"/>`;
    ages.forEach((a, i) => {
      const y = top + (ages.length - 1 - i) * rh, yb = y + (rh - bh) / 2, wm = xlen(male[i]), wf = xlen(female[i]);
      rows += `<g class="hrow"><title>Male, ages ${esc(a)}: ${male[i] == null ? 'no data' : fmt2(male[i]) + unit}</title><rect class="hit" x="${padX}" y="${r1(y)}" width="${r1(sw)}" height="${r1(rh)}"/><path class="bar s0" d="${rbar(L0 - wm, yb, wm, bh, true)}"/></g>`;
      const fp = rbar(R0, yb, wf, bh, false);
      rows += `<g class="hrow"><title>Female, ages ${esc(a)}: ${female[i] == null ? 'no data' : fmt2(female[i]) + unit}</title><rect class="hit" x="${r1(R0)}" y="${r1(y)}" width="${r1(sw)}" height="${r1(rh)}"/><path class="bar s1" d="${fp}"/>${fp ? `<path d="${fp}" fill="url(#${id}h)" pointer-events="none"/>` : ''}</g>`;
      rows += `<text class="age" x="${r1(W / 2)}" y="${r1(y + rh / 2 + 4.5)}">${esc(a)}</text>`;
    });
    g += `<line class="axis" x1="${r1(L0)}" x2="${r1(L0)}" y1="${top}" y2="${top + ph}"/><line class="axis" x1="${r1(R0)}" x2="${r1(R0)}" y1="${top}" y2="${top + ph}"/>`;
    const hdr = (label, cx, cls) => { const w = 15 + label.length * 8.6, x0 = r1(cx - w / 2); return `<rect class="bar ${cls}" x="${x0}" y="${top - 26}" width="11" height="11" rx="2.5"/>${cls === 's1' ? `<rect x="${x0}" y="${top - 26}" width="11" height="11" rx="2.5" fill="url(#${id}h)"/>` : ''}<text class="hdr" x="${r1(x0 + 16)}" y="${top - 16}">${label}</text>`; };
    const heads = hdr('Male', padX + sw / 2, 's0') + hdr('Female', R0 + sw / 2, 's1') + `<text class="agehdr" x="${r1(W / 2)}" y="${top - 16}">Age</text>`;
    const xl = `<text class="xlab" x="${r1(W / 2)}" y="${H - 8}" text-anchor="middle">${esc(s.xLabel || 'Percent of total population')}</text>`;
    const desc = (s.description ? s.description + ' ' : '') + `Population pyramid. Age groups run from ${ages[0] || ''} at the bottom to ${ages[ages.length - 1] || ''} at the top. Male bars extend left and female bars extend right, in percent of total population. ` + ages.map((a, i) => `${a}: male ${pv(male[i])}${male[i] == null ? '' : '%'}, female ${pv(female[i])}${female[i] == null ? '' : '%'}`).join('; ') + '.';
    const srTable = `<div class="sr-only"><table><caption>${esc(s.title || 'Population pyramid')} (percent of total population)</caption><thead><tr><th scope="col">Age group</th><th scope="col">Male (%)</th><th scope="col">Female (%)</th></tr></thead><tbody>${ages.map((a, i) => `<tr><th scope="row">${esc(a)}</th><td>${pv(male[i])}</td><td>${pv(female[i])}</td></tr>`).join('')}</tbody></table></div>`;
    const svg = `<svg viewBox="0 0 ${W} ${H}" role="img" aria-labelledby="${tid} ${did}"><title id="${tid}">${esc(s.title || 'Population pyramid')}</title><desc id="${did}">${esc(desc)}</desc><defs><pattern id="${id}h" patternUnits="userSpaceOnUse" width="6" height="6" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="6" stroke="rgba(255,255,255,.55)" stroke-width="2"/></pattern></defs>${g}${rows}${heads}${xl}</svg>`;
    return `<figure class="stim stim-pyr">${title(s.title)}<div class="chart pyr">${svg}</div>${srTable}${tail(s)}</figure>`;
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
