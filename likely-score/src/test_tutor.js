require('/home/claude/tests/pwshim.js');
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const ctx = await b.newContext({ viewport: { width: 1300, height: 900 } });
  let fails = 0; const ok = (n, c, d = '') => { if (!c) fails++; console.log((c ? 'PASS ' : 'FAIL ') + n + ' ' + String(d).slice(0, 300)); };
  const pg = await ctx.newPage(); const errs = []; pg.on('pageerror', e => errs.push(String(e)));
  await pg.goto('http://localhost:8913/wrapu.html?/frq-tutor.html'); await pg.waitForTimeout(2500);
  const fr = pg.frames().find(f => f !== pg.mainFrame());
  const n = await fr.evaluate(() => (typeof F2 !== 'undefined' ? F2 : (typeof L2 !== 'undefined' ? L2 : [])).length);
  const total = await fr.locator('[data-a="start"]').count();
  let pass = 0, bad = [];
  for (let k = 0; k < total; k++) {
    await fr.evaluate(() => { const h = document.querySelector('[data-a="home"]'); h && h.click(); });
    await pg.waitForTimeout(150);
    await fr.locator('[data-a="start"]').nth(k).click(); await pg.waitForTimeout(250);
    const r = await fr.evaluate(() => {
      const out = [];
      for (let i = 0; i < S.f.p.length; i++) {
        const st = S.p[i]; st.a = 'T1- A test answer. E2- In 2020, Brazil grew. A3- The reason this matters is that jobs pull people.';
        st.ck = 1; st.c = 5; st.g = S.f.p[i].r.i.map(r => r[1].test(st.a)); st.box = st.g.slice();
        const t = gemPrompt(i);
        out.push([S.f.t, L(i), /LIKELY POINT: Yes or No/.test(t), /WHAT EARNS THE POINT/.test(t), /jobs pull people/.test(t), S.f.stim ? /THE STIMULUS/.test(t) : true, t.length]);
      }
      return out;
    });
    for (const x of r) { if (x[2] && x[3] && x[4] && x[5]) pass++; else bad.push(x); }
  }
  ok(`Gemini prompt built for every part of all ${total} FRQs (${pass} parts)`, total >= 16 && !bad.length, JSON.stringify(bad.slice(0, 3)));
  // render a check card and click the Gemini button
  await fr.evaluate(() => { const st = S.p[0]; S.k = 1; render(1); });
  await fr.evaluate(() => { S.p[0].a = 'Kestria is in Stage 2 because its fertility is high.'; S.p[0].ck = 1; S.p[0].c = 5; S.p[0].box = S.f.p[0].r.i.map(() => true); S.p[0].g = S.p[0].box.slice(); render(1); });
  await pg.waitForTimeout(300);
  const panel = await fr.evaluate(() => document.querySelector('.verdict') ? document.querySelector('.verdict').textContent + ' || ' + [...document.querySelectorAll('.note')].map(n => n.textContent).join(' | ') : 'none');
  ok('check card says Likely + disclaimer', /Likely earns the point/.test(panel) && /official AP score/.test(panel), panel);
  const pop = ctx.waitForEvent('page', { timeout: 8000 });
  await fr.click('[data-a="gem"]');
  let txt = ''; try { const p2 = await pop; await p2.waitForLoadState('domcontentloaded'); await pg.waitForTimeout(300); txt = await p2.$eval('#t', t => t.value); await p2.screenshot({ path: 'gem.png' }); await p2.close(); } catch (e) { txt = 'ERR ' + e; }
  ok('Gemini copy page opens with the prompt', /LIKELY POINT/.test(txt) && /STUDENT_DATA/.test(txt) && /Kestria is in Stage 2/.test(txt), txt.slice(0, 120));
  
  await fr.evaluate(() => document.querySelector('.verdict').scrollIntoView({ block: 'center' })); await pg.screenshot({ path: 'check.png' });
  await fr.evaluate(() => { S.k = S.f.p.length + 1; render(1); }); await pg.waitForTimeout(300);
  const pop5 = ctx.waitForEvent('page', { timeout: 8000 });
  await fr.click('[data-a="gemall"]');
  let t5 = ''; try { const p5 = await pop5; await p5.waitForLoadState('domcontentloaded'); await pg.waitForTimeout(300); t5 = await p5.$eval('#t', t => t.value); await p5.close(); } catch (e) { t5 = 'ERR ' + e; }
  const np = await fr.evaluate(() => S.f.p.length);
  ok('whole-FRQ prompt: LIKELY SCORE + every part + STUDENT_DATA', new RegExp('LIKELY SCORE: X / ' + np).test(t5) && (t5.match(/======== PART/g) || []).length === np && /STUDENT_DATA/.test(t5) && /Kestria is in Stage 2/.test(t5), t5.slice(0, 200));
  await pg.screenshot({ path: 'done.png' });
  ok('no page errors', !errs.length, errs[0] || '');
  await b.close(); console.log(fails ? fails + ' FAILED' : 'ALL PASS');
})();
