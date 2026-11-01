#!/usr/bin/env node
// Checks one FRQ data file (src/frqs/*.js) before it is built into the tutor.
// Usage: node tools/validate.js src/frqs/u3-english-global.js
const fs = require('fs'), path = require('path');
const file = process.argv[2];
if (!file) { console.error('usage: node tools/validate.js src/frqs/<file>.js'); process.exit(2); }

// Shared pop-outs that live in src/engine.html and any FRQ may reference.
const SHARED = ['frq', 'tea', 'readmap', 'readtable', 'raj', 'scale'];
const BG = {}, FRQ = [];
const addBG = o => Object.assign(BG, o), addFRQ = f => FRQ.push(f);
new Function('addBG', 'addFRQ', fs.readFileSync(file, 'utf8'))(addBG, addFRQ);

const errs = [], warn = [];
const need = (o, k, where) => { if (o[k] === undefined || o[k] === '' ) errs.push(`${where}: missing "${k}"`); };
if (FRQ.length !== 1) errs.push(`expected exactly one addFRQ(), found ${FRQ.length}`);
const f = FRQ[0] || { p: [] };
['k', 't', 'd', 'u', 'intro', 'bg', 'nt', 'm', 'p'].forEach(k => need(f, k, 'FRQ'));
if (f.stim) need(f, 'st', 'FRQ');
const FMTS = ['No stimulus (like Question 1)', 'One stimulus (like Question 2)', 'Two stimuli (like Question 3)'];
if (f.fmt && !FMTS.includes(f.fmt)) errs.push(`fmt must be one of: ${FMTS.join(' | ')}`);
if (f.fmt === FMTS[0] && f.stim) errs.push('a no-stimulus FRQ must have stim:""');
if (f.fmt === FMTS[2] && !f.two) errs.push('a two-stimulus FRQ must set two:1');
if (f.fmt !== FMTS[0] && !f.stim) errs.push('missing "stim" (or set fmt to the no-stimulus format)');
if (f.nt && f.nt.length !== 3) errs.push(`need 3 "What do you notice?" prompts, found ${f.nt.length}`);
if (f.p.length !== 7) errs.push(`need 7 parts, found ${f.p.length}`);
const bgKeys = k => { if (!BG[k] && !SHARED.includes(k)) errs.push(`unknown background key "${k}"`); };
(f.bg || []).forEach(bgKeys);
Object.values(BG).forEach(b => { if (!b.t || !b.s || b.s.length < 3 || b.s.length > 5) errs.push(`background "${b.t}" needs 3-5 sentences`); });

f.p.forEach((p, i) => {
  const L = String.fromCharCode(65 + i), w = `Part ${L}`;
  ['v', 'q', 'sk', 's', 'r', 'mo', 'b', 'th', 'co', 'kq', 'ml', 'wk', 'mw', 'fr', 'qc'].forEach(k => need(p, k, w));
  if (!['Identify', 'Describe', 'Explain'].includes(p.v)) errs.push(`${w}: verb must be Identify/Describe/Explain`);
  const steps = p.v === 'Identify' ? 2 : 3;
  if (p.s && p.s.length !== steps) errs.push(`${w}: ${p.v} needs ${steps} thinking steps, found ${p.s.length}`);
  (p.s || []).forEach((s, j) => { if (!Array.isArray(s[1]) || s[1].length < 1 || s[1].length > 2) errs.push(`${w} step ${j + 1}: needs 1 or 2 hints`); });
  if (p.r) {
    if (!['any', 'all'].includes(p.r.m)) errs.push(`${w}: rubric mode must be "any" or "all"`);
    (p.r.i || []).forEach((r, j) => {
      if (!(r[1] instanceof RegExp)) errs.push(`${w} rubric ${j + 1}: second item must be a regex`);
      if (!r[2]) errs.push(`${w} rubric ${j + 1}: missing fix-it tip`);
    });
    const hits = (p.r.i || []).map(r => r[1] instanceof RegExp && r[1].test(p.mo || ''));
    const ok = p.r.m === 'any' ? hits.some(Boolean) : hits.every(Boolean);
    if (!ok) errs.push(`${w}: the model answer does NOT earn its own point (rubric hits: ${hits.join(',')})`);
    if (p.wk && p.r.m === 'all' && (p.r.i || []).every(r => r[1] instanceof RegExp && r[1].test(p.wk[0]))) warn.push(`${w}: the weak answer would pass the rubric`);
  }
  if (p.v !== 'Identify' && p.mo && !/T1-/.test(p.mo)) warn.push(`${w}: model answer not labeled T1-/E2-/A3-`);
  (p.b || []).forEach(bgKeys);
  if (p.ml && (!p.ml[1] || p.ml[1].length < 3 || !p.ml[2] || p.ml[2].length < 2)) errs.push(`${w}: mini-lesson needs 3+ sentences and 2+ key words`);
  if (p.fr && !/___/.test(p.fr)) errs.push(`${w}: sentence frame needs blanks (___)`);
  if (p.qc) {
    if (!p.qc[1] || p.qc[1].length !== 3 || p.qc[2] !== 0 || !p.qc[3]) errs.push(`${w}: quick check needs [question, [correct, wrong, wrong], 0, explanation]`);
  }
  if ((p.q || '').length > 260) warn.push(`${w}: question is long (${p.q.length} chars)`);
});
const kb = fs.statSync(file).size / 1024;
console.log(`${path.basename(file)}: ${f.p.length} parts, ${Object.keys(BG).length} pop-outs, ${kb.toFixed(1)} KB`);
warn.forEach(w => console.log('  warn:', w));
errs.forEach(e => console.log('  ERROR:', e));
process.exit(errs.length ? 1 : 0);
