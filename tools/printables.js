#!/usr/bin/env node
// Builds printable PDFs for every FRQ in src/frqs/:
//   print/<name>-student.pdf  stimulus, questions, labeled answer space
//   print/<name>-key.pdf      scoring guide with model answers and common mistakes
//   print/ALL-teacher-keys.pdf every key in one file
// Usage: node tools/printables.js            (all FRQs)
//        node tools/printables.js u3-english-global
const fs = require('fs'), path = require('path');
const { chromium } = require('playwright');

const ROOT = path.join(__dirname, '..');
const OUT = path.join(ROOT, 'print');
const only = process.argv[2];

function load(file) {
  const BG = {}, FRQ = [];
  new Function('addBG', 'addFRQ', fs.readFileSync(file, 'utf8'))(o => Object.assign(BG, o), f => FRQ.push(f));
  return FRQ[0];
}
const esc = t => String(t).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const L = i => String.fromCharCode(65 + i);

const CSS = `
@page{size:letter;margin:0.6in 0.65in}
:root{--ln:#999;--yl:#000;--cy:#000;--mg:#000;--gr:#000;--dim:#444;--ink:#000;--pn:#fff;--pn2:#f2f2f2}
*{box-sizing:border-box}
body{font:11.5pt/1.45 "Helvetica Neue",Arial,sans-serif;color:#000;margin:0}
h1{font-size:17pt;margin:0 0 2px}
h2{font-size:12.5pt;margin:18px 0 6px;border-bottom:2px solid #000;padding-bottom:2px}
.meta{font-size:9.5pt;color:#333;margin-bottom:10px}
.namebox{display:flex;gap:18px;font-size:10pt;margin:6px 0 12px}
.namebox span{flex:1;border-bottom:1px solid #000;padding-top:12px}
.dir{border:1.5px solid #000;padding:8px 10px;font-size:10pt;margin-bottom:12px}
.stim{border:1.5px solid #000;padding:10px;margin:8px 0 14px}
.stim svg,.stim table,.passage,.legend{break-inside:avoid}
.stim h4{break-after:avoid}
.stim h3{font-size:11pt;margin:0 0 6px}
.stim h4{color:#000!important;font-size:10.5pt;margin:12px 0 4px!important}
.stim svg{display:block;max-width:100%;height:auto;max-height:4.6in;margin:0 auto}
.passage{background:#fff!important;color:#000!important;border:1px solid #666!important;font-size:10.5pt!important;padding:8px 10px!important}
.tbl{overflow:visible}
table{border-collapse:collapse;width:100%;font-size:9.5pt;margin:4px 0}
th,td{border:1px solid #000;padding:4px 5px;text-align:center}
th{background:#e8e8e8}
td:first-child{text-align:left;font-weight:bold}
.legend{display:flex;flex-wrap:wrap;gap:4px 12px;font-size:9pt;margin-top:6px}
.legend i{display:inline-block;width:11px;height:11px;border:1px solid #000;margin-right:4px;vertical-align:-1px}
.src{font-size:8.5pt;font-style:italic;color:#333;margin:6px 0 0}
.q{break-inside:avoid;margin:12px 0}
.q .h{font-weight:bold}
.q .h b{display:inline-block;min-width:22px}
.verb{font-size:8.5pt;border:1px solid #000;padding:0 4px;margin-left:6px;vertical-align:1px;text-transform:uppercase;letter-spacing:.04em}
.lines{margin-top:6px}
.ln{display:flex;align-items:flex-end;gap:6px;margin-top:4px}
.ln .lab{font-weight:bold;font-size:9.5pt;width:28px}
.ln .rule{flex:1;border-bottom:1px solid #777;height:22px}
.key .q{border:1.5px solid #000;padding:8px 10px}
.key .rb{margin:6px 0 4px;padding-left:18px}
.key .rb li{margin:2px 0}
.key .mo{background:#f2f2f2;padding:6px 8px;margin:6px 0}
.key .lab2{font-size:8.5pt;font-weight:bold;text-transform:uppercase;letter-spacing:.05em;color:#333;display:block}
.key .wk{font-size:10pt;margin:4px 0 0}
.foot{margin-top:16px;font-size:8.5pt;color:#555;border-top:1px solid #999;padding-top:4px}
.pb{break-before:page}
`;

function head(f, kind) {
  return `<h1>${esc(f.t)}</h1><div class="meta">AP Human Geography · ${esc(f.u)} · ${esc(f.fmt || '')} · ${f.p.length} points · ${kind} · GeoArcade FRQ Tutor</div>`;
}
function stim(f) {
  if (!f.stim) return `<div class="dir"><b>No stimulus.</b> ${esc(f.intro)}</div>`;
  return `<p style="margin:0 0 4px">${esc(f.intro)}</p><div class="stim"><h3>${esc(f.st)}</h3>${f.stim}</div>`;
}
const DIRECTIONS = `<div class="dir"><b>Directions:</b> Answer all parts of the question. Respond in complete sentences; an outline or bulleted list is not acceptable. Label each part (A, B, C…). For Describe and Explain parts, write it out with <b>T1-</b> (your reason in general words), <b>E2-</b> (the specific proof), and <b>A3-</b> (why it matters).</div>`;

function student(f) {
  const qs = f.p.map((p, i) => {
    const lines = (p.v === 'Identify' || p.v === 'Define')
      ? `<div class="ln"><span class="lab"></span><span class="rule"></span></div><div class="ln"><span class="lab"></span><span class="rule"></span></div>`
      : ['T1-', '', 'E2-', '', 'A3-', ''].map(l => `<div class="ln"><span class="lab">${l}</span><span class="rule"></span></div>`).join('');
    return `<div class="q"><div class="h"><b>${L(i)}.</b>${esc(p.q)}<span class="verb">${p.v}</span></div><div class="lines">${lines}</div></div>`;
  }).join('');
  return `${head(f, 'Student handout')}<div class="namebox"><span>Name</span><span>Date</span><span>Period</span></div>${DIRECTIONS}${stim(f)}${qs}
<div class="foot">Practice FRQ. ${f.k && /Class FRQ/.test(f.k) ? 'Publicly released question.' : 'Original question; places and data may be fictional.'} Try it with step-by-step help on GeoArcade.</div>`;
}

function key(f) {
  const qs = f.p.map((p, i) => `<div class="q"><div class="h"><b>${L(i)}.</b>${esc(p.q)}<span class="verb">${p.v}</span></div>
<span class="lab2" style="margin-top:6px">Earns the point if the answer ${p.r.m === 'any' ? 'does ANY ONE of these' : 'does ALL of these'}:</span>
<ul class="rb">${p.r.i.map(r => `<li>${esc(r[0])}</li>`).join('')}</ul>
<div class="mo"><span class="lab2">Model answer</span>${esc(p.mo).replace(/ (E2-|A3-) /g, '<br><b>$1</b> ').replace(/^T1- /, '<b>T1-</b> ')}</div>
<p class="wk"><b>Common mistake:</b> “${esc(p.wk[0])}” ${esc(p.wk[1])}</p>
<p class="wk"><b>Why the model works:</b> ${esc(p.mw)}</p></div>`).join('');
  return `<div class="key">${head(f, 'Teacher key')}${stim(f)}${qs}<div class="foot">Scoring guide written for the GeoArcade FRQ Tutor. Award each part independently, 1 point each.</div></div>`;
}

const page = body => `<!DOCTYPE html><html><head><meta charset="utf-8"><style>${CSS}</style></head><body>${body}</body></html>`;

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const files = fs.readdirSync(path.join(ROOT, 'src/frqs')).filter(n => n.endsWith('.js')).sort()
    .filter(n => !only || n === only + '.js');
  const browser = await chromium.launch();
  const pg = await browser.newPage();
  const keys = [];
  for (const n of files) {
    const f = load(path.join(ROOT, 'src/frqs', n)), base = n.replace(/\.js$/, '');
    for (const [kind, html] of [['student', student(f)], ['key', key(f)]]) {
      await pg.setContent(page(html), { waitUntil: 'load' });
      await pg.pdf({ path: path.join(OUT, `${base}-${kind}.pdf`), format: 'Letter', printBackground: true, margin: { top: '0.6in', bottom: '0.6in', left: '0.65in', right: '0.65in' } });
    }
    keys.push(key(f));
    console.log('printed', base);
  }
  if (!only) {
    await pg.setContent(page(keys.join('<div class="pb"></div>')), { waitUntil: 'load' });
    await pg.pdf({ path: path.join(OUT, 'ALL-teacher-keys.pdf'), format: 'Letter', printBackground: true, margin: { top: '0.6in', bottom: '0.6in', left: '0.65in', right: '0.65in' } });
    console.log('printed ALL-teacher-keys');
  }
  await browser.close();
})();
