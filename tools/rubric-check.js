#!/usr/bin/env node
// Tests how well each FRQ's keyword rubric guesses real student answers.
// Test answers live in tools/rubric-tests/<frq-name>.json as:
//   { "A": [ { "a": "student answer", "ok": true }, ... ], "B": [...], ... }
// "ok" is what a fair AP reader would award. The tutor's guess is "earned"
// when every rubric item matches (or any one item, for "any" rubrics),
// exactly as the tutor pre-ticks the checklist.
// Usage: node tools/rubric-check.js u3-english-global      (one FRQ)
//        node tools/rubric-check.js                        (every FRQ with tests)
const fs = require('fs'), path = require('path');
const ROOT = path.join(__dirname, '..');

function load(name) {
  const BG = {}, FRQ = [];
  new Function('addBG', 'addFRQ', fs.readFileSync(path.join(ROOT, 'src/frqs', name + '.js'), 'utf8'))(o => Object.assign(BG, o), f => FRQ.push(f));
  return FRQ[0];
}

function check(name) {
  const tf = path.join(ROOT, 'tools/rubric-tests', name + '.json');
  if (!fs.existsSync(tf)) return null;
  const f = load(name), tests = JSON.parse(fs.readFileSync(tf, 'utf8'));
  let total = 0, wrong = 0;
  const lines = [];
  f.p.forEach((p, i) => {
    const L = String.fromCharCode(65 + i);
    (tests[L] || []).forEach(t => {
      const hits = p.r.i.map(r => r[1].test(t.a));
      const guess = p.r.m === 'any' ? hits.some(Boolean) : hits.every(Boolean);
      total++;
      if (guess !== t.ok) {
        wrong++;
        lines.push(`  ${L} ${t.ok ? 'MISSED (should earn)' : 'FALSE PASS (should not earn)'}  items=[${hits.map(h => h ? 'y' : 'n').join('')}]  "${t.a}"`);
      }
    });
  });
  console.log(`${name}: ${total - wrong}/${total} guesses correct`);
  lines.forEach(l => console.log(l));
  return { total, wrong };
}

const only = process.argv[2];
const names = only ? [only] : fs.readdirSync(path.join(ROOT, 'tools/rubric-tests')).filter(n => n.endsWith('.json')).map(n => n.replace(/\.json$/, '')).sort();
let T = 0, W = 0;
for (const n of names) { const r = check(n); if (r) { T += r.total; W += r.wrong; } }
if (!only && names.length > 1) console.log(`\nALL: ${T - W}/${T} correct (${T ? Math.round(100 * (T - W) / T) : 0}%)`);
process.exit(W ? 1 : 0);
