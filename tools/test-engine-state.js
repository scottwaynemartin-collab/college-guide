#!/usr/bin/env node
// Checks that the tutor engine still follows the state machine written down in tools/ENGINE-STATE.md.
// It drives the built all-in-one file (frq-tutor.html) by clicking, the way a student would, and reads
// S and localStorage after each move. Run `python3 build.py` first.
// Usage: node tools/test-engine-state.js
const fs = require('fs'), path = require('path'), http = require('http');
const { chromium } = require('playwright');
const ROOT = path.join(__dirname, '..'), FILE = path.join(ROOT, 'frq-tutor.html');
if (!fs.existsSync(FILE)) { console.error('frq-tutor.html not built yet: run python3 build.py'); process.exit(2); }

(async () => {
  const srv = http.createServer((q, r) => { r.setHeader('content-type', 'text/html; charset=utf-8'); r.end(fs.readFileSync(FILE)); });
  await new Promise(res => srv.listen(0, '127.0.0.1', res));
  const url = `http://127.0.0.1:${srv.address().port}/frq-tutor.html`;
  const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: 1200, height: 900 } });
  const errs = []; pg.on('pageerror', e => errs.push(String(e)));
  let fails = 0; const ok = (n, c, d = '') => { if (!c) fails++; console.log((c ? 'PASS ' : 'FAIL ') + n + (c ? '' : '  ' + String(d).slice(0, 300))); };
  const click = async sel => { await pg.click(sel); await pg.waitForTimeout(60); };
  const st = (i = 0) => pg.evaluate(i => { const p = S.p[i]; return { k: S.k, max: S.max, vis: S.vis, cb: S.cb, c: p.c, st: p.st, ck: p.ck, done: p.done, ok: p.ok, a: p.a, w: p.w || 0, box: p.box.length }; }, i);
  const saved = () => pg.evaluate(() => JSON.parse(localStorage.getItem('geoarcade-frq:' + S.f.t) || 'null'));

  await pg.goto(url); await pg.waitForTimeout(400);
  ok('home screen is S.k = -1', (await pg.evaluate(() => S.k)) === -1);

  // start -> stimulus screen, every part fresh
  await click('[data-a="start"]');
  let s = await st();
  const n = await pg.evaluate(() => S.f.p.length);
  const fresh = await pg.evaluate(() => S.p.every(p => p.c === 0 && p.st === 1 && !p.ck && !p.done && !p.ok && p.a === ''));
  ok('start: S.k = 0 and every part is on card 0, unchecked', s.k === 0 && fresh, JSON.stringify(s));

  // progress bar can jump to a part; go() records max and vis
  await click('[data-a="go"][data-k="1"]');
  s = await st();
  ok('go(1): Part A shown, max and vis recorded', s.k === 1 && s.max === 1 && s.vis[1] === 1 && s.c === 0, JSON.stringify(s));

  // cards 0-4 are free; card 5 is locked until checked
  const locked = await pg.evaluate(() => document.querySelector('.sb[data-c="5"]').disabled);
  ok('card 5 (Check) is disabled before check', locked === true);
  await click('.sb[data-c="1"]'); ok('card 1 (Verb) reachable', (await st()).c === 1);
  await click('.sb[data-c="3"]'); ok('card 3 (Think) reachable', (await st()).c === 3);

  // Think: each "Next step" reveals one more step until "Start writing" appears
  const steps = await pg.evaluate(() => S.f.p[0].s.length);
  for (let k = 1; k < steps; k++) await click('[data-a="step"]');
  s = await st();
  const startWriting = await pg.evaluate(() => !document.querySelector('[data-a="step"]') && !!document.querySelector('.btn.c[data-a="card"][data-c="4"]'));
  ok('Think: st counts to the last step, then offers Start writing', s.st === steps && startWriting, JSON.stringify({ st: s.st, steps, startWriting }));
  await click('.btn.c[data-a="card"][data-c="4"]'); ok('Start writing lands on card 4', (await st()).c === 4);

  // typing updates S.p[i].a and the save, without checking
  await pg.fill('#ans', 'A first draft with a ___ blank.'); await pg.waitForTimeout(60);
  s = await st(); let sv = await saved();
  ok('typing updates the answer and the save', s.a === 'A first draft with a ___ blank.' && sv && sv.p[0].a === s.a && !s.ck, JSON.stringify({ a: s.a, saved: sv && sv.p[0].a }));

  // check with blanks: warning, stay on Write
  await click('[data-a="check"]'); s = await st();
  ok('check with ___ blanks: w=1, stays on card 4, not checked', s.w === 1 && s.c === 4 && s.ck === 0, JSON.stringify(s));

  // check with a too-short answer: stay
  await pg.fill('#ans', 'x'); await click('[data-a="check"]'); s = await st();
  ok('check with a one-letter answer: stays on card 4', s.c === 4 && s.ck === 0, JSON.stringify(s));

  // check with a real (wrong) answer: ck=1, card 5, box sized to the rubric
  const lines = await pg.evaluate(() => S.f.p[0].r.i.length);
  await pg.fill('#ans', 'zzqx vrbl plonk zzqx.'); await click('[data-a="check"]'); s = await st();
  const unlocked = await pg.evaluate(() => !document.querySelector('.sb[data-c="5"]').disabled);
  ok('check: ck=1, card 5, box has one slot per rubric line, Check tab unlocked', s.ck === 1 && s.c === 5 && s.box === lines && unlocked, JSON.stringify(s));
  ok('check does not count as done', s.done === 0 && s.ok === 0);

  // revise: back to Write, unchecked, answer kept
  await click('[data-a="rev"]'); s = await st();
  ok('rev: card 4, ck=0, done=0, answer kept', s.c === 4 && s.ck === 0 && s.done === 0 && s.a === 'zzqx vrbl plonk zzqx.', JSON.stringify(s));

  // check again, then Next: done=1, ok frozen from earned(), move to Part B
  await click('[data-a="check"]');
  const earnedNow = await pg.evaluate(() => earned(0));
  await click('[data-a="next"]'); s = await st();
  ok('next: done=1, ok = earned(i), go(i+2) shows Part B', s.done === 1 && s.ok === earnedNow && s.k === 2, JSON.stringify({ ...s, earnedNow }));
  ok('score counts done && ok only', (await pg.evaluate(() => score())) === (earnedNow ? 1 : 0));

  // results screen; nonsense answer should be a miss, so Retry appears
  await click(`[data-a="go"][data-k="${n + 1}"]`);
  const hasRetry = await pg.evaluate(() => !!document.querySelector('[data-a="retry"]'));
  ok('results (S.k = n+1) offers Retry when a done part was missed', (await pg.evaluate(() => S.k)) === n + 1 && (hasRetry === !earnedNow), JSON.stringify({ hasRetry, earnedNow }));
  if (hasRetry) {
    await click('[data-a="retry"]'); s = await st();
    ok('retry: the missed part goes back to Write, unchecked, and is shown', s.k === 1 && s.c === 4 && s.ck === 0 && s.done === 0, JSON.stringify(s));
  }

  // persistence: exact save shape, and a reload restores the screen and the part
  sv = await saved();
  ok('save holds exactly {k,max,vis,p,nt,cb}', JSON.stringify(Object.keys(sv).sort()) === JSON.stringify(['cb', 'k', 'max', 'nt', 'p', 'vis']), JSON.stringify(Object.keys(sv)));
  const partKeys = ['a', 'box', 'c', 'cf', 'ck', 'done', 'h', 'ok', 'q', 'st'];
  ok('each saved part has the documented fields', sv.p.every(p => partKeys.every(k => k in p)), JSON.stringify(Object.keys(sv.p[0])));
  const before = await st();
  await pg.reload(); await pg.waitForTimeout(400); await click('[data-a="start"]'); s = await st();
  ok('reload + start restores S.k and the part', s.k === before.k && s.c === before.c && s.a === before.a && s.ck === before.ck, JSON.stringify({ before, after: s }));

  // the shape guard: a save with the wrong number of parts is ignored
  await pg.evaluate(() => { const v = JSON.parse(localStorage.getItem('geoarcade-frq:' + S.f.t)); v.p.pop(); localStorage.setItem('geoarcade-frq:' + S.f.t, JSON.stringify(v)); });
  await pg.reload(); await pg.waitForTimeout(400); await click('[data-a="start"]'); s = await st();
  ok('loadSave ignores a save whose part count differs (fresh start)', s.k === 0 && s.a === '' && s.c === 0, JSON.stringify(s));

  // restart needs two taps; the second wipes the save
  await pg.fill('#ans', '').catch(() => {});
  await click('[data-a="go"][data-k="1"]'); await click('.sb[data-c="4"]'); await pg.fill('#ans', 'keep me?'); await pg.waitForTimeout(60);
  await click(`[data-a="go"][data-k="${n + 1}"]`);
  await click('[data-a="restart"]');
  const armed = await pg.evaluate(() => S.rc === 1 && S.p[0].a === 'keep me?');
  ok('restart: first tap only arms the confirm, nothing erased', armed);
  await click('[data-a="restart"]'); s = await st();
  const gone = await pg.evaluate(() => S.p.every(p => p.a === '' && !p.done));
  ok('restart: second tap wipes answers and starts at the stimulus', s.k === 0 && gone, JSON.stringify(s));

  ok('no page errors', !errs.length, errs[0] || '');
  await b.close(); srv.close();
  console.log(fails ? fails + ' FAILED' : 'ALL PASS'); process.exit(fails ? 1 : 0);
})().catch(e => { console.error(e); process.exit(1); });
