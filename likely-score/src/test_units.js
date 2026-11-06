require('/home/claude/tests/pwshim.js');
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const ctx = await b.newContext({ viewport: { width: 1300, height: 900 } });
  let fails = 0; const ok = (n, c, d = '') => { if (!c) fails++; console.log((c ? 'PASS ' : 'FAIL ') + n + ' ' + String(d).slice(0, 200)); };
  for (const u of [1, 2, 3, 4, 5, 6, 7]) {
    const pg = await ctx.newPage(); const errs = []; pg.on('pageerror', e => errs.push(String(e)));
    await pg.goto(`http://localhost:8912/wrapu.html?/out/unit-${u}.html`); await pg.waitForTimeout(2500);
    const fr = pg.frames().find(f => f !== pg.mainFrame());
    await fr.click('.lvl[data-level="lab"]'); await pg.waitForTimeout(500);
    await fr.click('#labNav .nitem >> nth=1'); await pg.waitForTimeout(400);
    const nb = await fr.locator('[data-gem]').count();
    const pill = await fr.innerText('.reps-h .pill');
    const key = await fr.getAttribute('[data-gem] >> nth=0', 'data-gem');
    // empty -> toast, no popup
    await fr.click('[data-gem] >> nth=0'); await pg.waitForTimeout(300);
    await fr.fill(`[data-draft="${key}"]`, 'T- This happens because people move for jobs. E- For example, in 2020 many workers moved to Texas. A- This matters because jobs pull people.');
    const pop = ctx.waitForEvent('page', { timeout: 8000 });
    await fr.click('[data-gem] >> nth=0');
    let txt = ''; try { const p2 = await pop; await p2.waitForLoadState('domcontentloaded'); await pg.waitForTimeout(300); txt = await p2.$eval('#t', t => t.value); await p2.close(); } catch (e) { txt = 'ERR ' + e; }
    ok(`unit ${u}: ${nb} Gemini buttons, copy page has LIKELY POINT + question + model + answer`, nb >= 3 && /LIKELY POINT: Yes or No/.test(txt) && /ONE FULL-CREDIT EXAMPLE/.test(txt) && /moved to Texas/.test(txt) && /WHAT A READER LOOKS FOR/.test(txt), pill);
    // boss
    await fr.click('#labNav .nitem >> text=Boss'); await pg.waitForTimeout(400);
    const bk = await fr.getAttribute('[data-gem] >> nth=1', 'data-gem');
    await fr.fill(`[data-draft="${bk}"]`, 'A test answer for the boss part that is long enough.');
    const pop2 = ctx.waitForEvent('page', { timeout: 8000 });
    await fr.click('[data-gem] >> nth=1');
    let t2 = ''; try { const p3 = await pop2; await p3.waitForLoadState('domcontentloaded'); await pg.waitForTimeout(300); t2 = await p3.$eval('#t', t => t.value); await p3.close(); } catch (e) { t2 = 'ERR ' + e; }
    ok(`unit ${u}: Boss prompt has stem + table + Part B`, /THE FRQ\nStem:/.test(t2) && /TABLE —/.test(t2) && /Part B \(task verb/.test(t2), '');
    await fr.click(`[data-reveal="${bk}"]`); await pg.waitForTimeout(200);
    await fr.click(`[data-verdict="${bk}"][data-val="1"]`); await pg.waitForTimeout(200);
    const bs = await fr.innerText('#bossScore');
    const pop4 = ctx.waitForEvent('page', { timeout: 8000 });
    await fr.click('#bossGem');
    let t4 = ''; try { const p4 = await pop4; await p4.waitForLoadState('domcontentloaded'); await pg.waitForTimeout(300); t4 = await p4.$eval('#t', t => t.value); await p4.close(); } catch (e) { t4 = 'ERR ' + e; }
    ok(`unit ${u}: whole-Boss prompt has LIKELY SCORE X / 7 + STUDENT_DATA + 7 parts`, /LIKELY SCORE: X \/ 7/.test(t4) && /STUDENT_DATA/.test(t4) && (t4.match(/======== PART/g) || []).length === 7 && /long enough/.test(t4), t4.slice(0, 60));
    ok(`unit ${u}: boss score says Likely score`, /likely score/i.test(bs) && /1 \/ 7/.test(bs), bs.replace(/\n/g, ' '));
    if (u === 3) { await fr.evaluate(k => document.querySelector(`[data-key="${k}"]`).scrollIntoView(), bk); await pg.screenshot({ path: 'u3.png' }); }
    ok(`unit ${u}: no page errors`, !errs.length, errs[0] || '');
    await pg.close();
  }
  await b.close(); console.log(fails ? fails + ' FAILED' : 'ALL PASS');
})();
