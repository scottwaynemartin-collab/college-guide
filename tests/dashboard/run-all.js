#!/usr/bin/env node
// Runs every dashboard test in headless Chromium (Playwright) and reports pass/fail.
// Usage:  node tests/dashboard/run-all.js            (all tests)
//         node tests/dashboard/run-all.js 07 10      (only tests whose file name starts with 07 or 10)
// A test fails if it exits non-zero, times out, prints a non-empty "ERR [...]" (page errors / console errors),
// or reports leaked student names. Printouts are checked for page count with pdfinfo when it is installed.
const {spawnSync, execFileSync} = require('child_process'), fs = require('fs'), path = require('path');
const dir = __dirname, {OUT} = require('./lib');
const only = process.argv.slice(2);
const files = fs.readdirSync(dir).filter(f => /^\d\d-.*\.js$/.test(f) && (!only.length || only.some(o => f.startsWith(o)))).sort();
const onePage = ['r3b.pdf', 'spec-conf.pdf', 'ttess2.pdf', 'admin.pdf'];
let failed = 0;
for (const f of files){
  const t0 = Date.now(), r = spawnSync(process.execPath, [path.join(dir, f)], {cwd: dir, encoding: 'utf8', timeout: 240000});
  const out = (r.stdout || '') + (r.stderr || ''), why = [];
  if (r.error) why.push(r.error.code === 'ETIMEDOUT' ? 'timed out' : r.error.message);
  if (r.status) why.push('exit ' + r.status);
  if (/ERR \[\s*['"{]/.test(out)) why.push('page/console errors: ' + (out.match(/ERR \[[^\]]*\]/) || [''])[0].slice(0, 200));
  if (/names leaked:? [1-9]/.test(out)) why.push('student names leaked');
  if (/TimeoutError/.test(out)) why.push((out.match(/waiting for [^\n]+/) || ['TimeoutError'])[0]);
  console.log(`${why.length ? '✗' : '✓'} ${f}  (${((Date.now()-t0)/1000).toFixed(1)}s)${why.length ? '\n    ' + why.join('\n    ') : ''}`);
  if (why.length) failed++;
}
let pdfinfo = true; try { execFileSync('pdfinfo', ['-v'], {stdio: 'ignore'}); } catch(_) { pdfinfo = false; }
if (pdfinfo) for (const p of onePage){ const fp = path.join(OUT, p); if (!fs.existsSync(fp)) continue;
  const pages = +((execFileSync('pdfinfo', [fp], {encoding: 'utf8'}).match(/Pages:\s+(\d+)/) || [])[1]);
  const ok = pages === 1; if (!ok) failed++; console.log(`${ok ? '✓' : '✗'} print ${p}: ${pages} page${pages === 1 ? '' : 's'}`); }
console.log(failed ? `\n${failed} problem(s)` : '\nAll dashboard tests passed');
process.exit(failed ? 1 : 0);
