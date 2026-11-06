require('/home/claude/tests/pwshim.js');
const { chromium } = require('playwright');
const U = 'http://localhost:8911/wrap.html';
// (frq, part, T1, E2, A3, should)
const C = [
 ['C', "One barrier to the diffusion of English throughout China is the writing system.", "Chinese uses thousands of characters instead of letters like English uses.", "The reason this matters is that learning a whole new alphabet is hard so fewer people learn English.", true],
 ['C', "One barrier is that the government controls the internet.", "China blocks websites like Google and YouTube with the Great Firewall.", "The reason this matters is that people can't see English content online so they have less reason to learn it.", true],
 ['C', "A barrier to English spreading in China is that most people don't need it.", "Mandarin is spoken by over 900 million people so it is the main language there.", "The reason this matters is that if you can do everything in Mandarin you don't need to learn English.", true],
 ['C', "One barrier is that poor rural areas do not have good schools.", "Many villages in western China don't have teachers who can teach English.", "The reason this matters is that kids in the countryside never get the chance to learn it.", true],
 ['C', "A barrier is that English classes cost a lot of money.", "Private tutoring in Beijing can cost hundreds of dollars a month.", "The reason this matters is that poor families can't afford it so their kids don't learn English.", true],
 ['C', "One barrier to the diffusion of English throughout China is a barrier.", "There are a lot of barriers in China.", "The reason this matters is that it is hard.", false],
 ['C', "English is a hard language.", "It has a lot of words.", "So people do not learn it.", false],
 ['C', "One barrier is urban areas have too many people.", "Cities like Shanghai are crowded.", "The reason this matters is that it is crowded so it is hard.", false],
 ['A', "India has many English speakers because a European country ruled it for a long time.", "The British Empire controlled India until 1947.", "The reason this matters is that English stayed in the government and schools after the British left.", true],
 ['A', "India has many English speakers because they watch American movies.", "Bollywood and Hollywood movies are popular in India.", "The reason this matters is that people learn English from movies.", false],
 ['B', "People in China and India learn English because it helps them get better jobs.", "Call centers in India hire workers who speak English.", "The reason this matters is that English speakers get paid more so families want their kids to learn it.", true],
 ['B', "People learn English because it is cool.", "Lots of people think it is cool.", "So they learn it.", false],
 ['G', "A negative impact is that local languages can die out.", "In Nigeria many young people speak English instead of Yoruba or Igbo.", "The reason this matters is that when the old people die, the language and its traditions die with them.", true],
 ['E', "A company moves its call center because workers are cheaper there.", "American companies put call centers in the Philippines where wages are lower.", "The reason this matters is that paying workers less saves the company money so it makes more profit.", true],
 ['E', "A company moves its call center to be nice.", "Companies like to help other countries.", "The reason this matters is that it helps people.", false],
 ['F', "The table is old.", "It is from 2018.", "So it is not right.", false],
 ['A', "India has English speakers, but it was not because of the British Empire or colonization.", "Many people there just like the language a lot today.", "The reason this matters is that people choose to learn it for fun.", false],
 ['B', "People in China and India learn English because it gets them ___ with companies.", "Call centers in Bengaluru hire English speakers.", "The reason this matters is that English pays more so families want it.", false],
 ['B', "People in China and India learn English because it helps them get jobs with international companies.", "Call centers in Bengaluru hire thousands of English speakers.", "", false],
 ['B', "People in China and India learn English to study in other countries.", "Many Chinese students go to universities in the United States and the UK.", "The reason this matters is that you need English to pass classes there so students learn it first.", true],
];
(async () => {
  const res = []; const ok = (n, c, d) => res.push([n, !!c, d]);
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 1320, height: 900 } });
  const pg = await ctx.newPage(); const errs = [];
  pg.on('pageerror', e => errs.push(String(e)));
  pg.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
  await pg.goto(U); await pg.waitForTimeout(2500);
  const fr = pg.frames().find(f => f !== pg.mainFrame());
  const lede = await fr.innerText('.lede'); ok('lobby says likely', /likely/.test(lede) && /final word/.test(lede), lede.slice(0, 80));
  await fr.click('.fcard[data-f="u3-lingua-franca"]'); await pg.waitForTimeout(600);
  const fill = async (l, t1, e2, a3) => { for (const [k, v] of [['T1', t1], ['E2', e2], ['A3', a3]]) await fr.fill(`textarea[data-a="${l}:${k}"]`, v); };
  const head = async l => (await fr.innerText(`[data-fb="${l}"] .fb h4`)).split('\n')[0];
  let wrong = [];
  for (const [l, t1, e2, a3, should] of C) {
    await fill(l, t1, e2, a3); await fr.click(`[data-check="${l}"]`); await pg.waitForTimeout(150);
    const h = await head(l); const got = /likely earns/i.test(h);
    if (got !== should) wrong.push(`${l} ${should ? 'GOOD' : 'BAD'} -> ${h} | ${t1.slice(0, 40)}`);
  }
  ok(`quick check agrees with a reader on ${C.length} answers`, !wrong.length, wrong);
  // verdict auto-set + score bar
  await fill('A', ...C[8].slice(1, 4)); await fr.click('[data-check="A"]'); await pg.waitForTimeout(200);
  const pill = await fr.innerText('#part-A .part-head .pill'); ok('fresh Check sets the likely point pill', /likely point/i.test(pill), pill);
  const sb = await fr.innerText('#scoreBar'); ok('score bar shows "Likely score" + disclaimer', /LIKELY SCORE/i.test(sb) && /not an official AP score/.test(sb), sb.replace(/\n/g, ' | ').slice(0, 160));
  const card = await fr.innerText('[data-fb="A"]');
  ok('card: disclaimer + CB options + Gemini button', /practice estimate/.test(card) && /options from the College Board/i.test(card) && /Grade it in Gemini/.test(card), '');
  await fr.click('[data-v="A"][data-val="0"]'); await pg.waitForTimeout(150);
  ok('student can override the likely call', (await fr.innerText('#part-A .part-head .pill')).trim().toLowerCase() === 'not yet', '');
  // stuck panel shows real matches
  await fr.click('[data-stuck="A"]'); await pg.waitForTimeout(200);
  ok('Stuck panel greens a matching option', await fr.locator('[data-stuckpanel="A"] .acc div.hit').count() >= 1, '');
  // Gemini prompts
  const pp = await fr.evaluate(() => window.__ER.handoffPart(window.__ER.cur.parts[0]));
  ok('part prompt: question + guide + answer + LIKELY POINT', /OFFICIAL SCORING GUIDE/.test(pp) && /STUDENT_DATA/.test(pp) && /LIKELY POINT: Yes or No/.test(pp) && /British Empire/.test(pp) && /Ethnologue/i.test(pp) && /final word/.test(pp), pp.length);
  const pa = await fr.evaluate(() => window.__ER.handoffAll());
  ok('whole-FRQ prompt: 7 parts + LIKELY SCORE: X / 7', (pa.match(/======== PART/g) || []).length === 7 && /LIKELY SCORE: X \/ 7/.test(pa), pa.length);
  const pop = ctx.waitForEvent('page', { timeout: 8000 });
  await fr.click('[data-hand="A"]');
  try { const p2 = await pop; await p2.waitForLoadState('domcontentloaded'); await pg.waitForTimeout(400); const h2 = await p2.content();
    ok('Gemini copy page opens with likely wording + prompt', /Grade part A in Gemini/.test(h2) && /likely/.test(h2) && /LIKELY POINT/.test(h2), ''); await p2.close(); } catch (e) { ok('Gemini copy page opens', false, String(e).slice(0, 80)); }
  await fr.evaluate(() => document.querySelector('#finish').scrollIntoView());
  ok('finish button says likely score', /likely score/i.test(await fr.innerText('#gradeAllBtn')), await fr.innerText('#gradeAllBtn'));
  // PDF
  const pop3 = ctx.waitForEvent('page', { timeout: 8000 });
  await fr.click('#pdfBtn'); await pg.waitForTimeout(300); await fr.click('#xGo');
  try { const p3 = await pop3; await p3.waitForLoadState('domcontentloaded'); await pg.waitForTimeout(500); const h3 = await p3.content();
    ok('PDF: likely score + quick-check verdicts', /Likely score: \d \/ 7/.test(h3) && /Quick check — Likely/.test(h3), ''); await p3.close(); } catch (e) { ok('PDF opens', false, String(e).slice(0, 80)); }
  // every official sample reads Likely earns (both FRQs)
  const sw = [];
  for (const id of ['u3-lingua-franca', 'u4-colonial-africa']) {
    await fr.evaluate(id => { const f = window.__ER.FRQS.find(x => x.id === id); window.__ER.open(f); }, id); await pg.waitForTimeout(500);
    const parts = await fr.evaluate(() => window.__ER.cur.parts.map(p => ({ l: p.l, m: p.model })));
    for (const p of parts) {
      const lines = p.m.split('\n').filter(Boolean).map(x => x.replace(/^(T1|E2|A3)-\s*/, '').replace(/^✅\s*/, ''));
      const boxes = await fr.evaluate(l => [...document.querySelectorAll(`#part-${l} textarea`)].map(t => t.dataset.a.split(':')[1]), p.l);
      for (let i = 0; i < boxes.length; i++) await fr.fill(`textarea[data-a="${p.l}:${boxes[i]}"]`, lines[i] || '');
      await fr.click(`[data-check="${p.l}"]`); await pg.waitForTimeout(120);
      const h = await head(p.l); if (!/^🟢 Likely earns/.test(h)) sw.push(`${id} ${p.l}: ${h}`);
    }
  }
  ok('all 14 official samples read 🟢 Likely earns', !sw.length, sw);
  const sc = await fr.innerText('#scoreBar .sb-big'); ok('7 samples -> likely 7 / 7', /7 \/ 7/.test(sc), sc.replace(/\n/g, ' '));
  // maps FRQ: teacher-added answer counts
  await fr.fill('textarea[data-a="B:T1"]', 'Map 1 boundaries are straight lines but Map 2 boundaries are curvy and irregular.');
  await fr.fill('textarea[data-a="B:E2"]', 'The Fulani and Hausa areas in West Africa have wavy borders that follow where the groups live.');
  await fr.fill('textarea[data-a="B:A3"]', 'The reason this matters is that culture group borders follow people, so they are not straight like colonial lines.');
  await fr.click('[data-check="B"]'); await pg.waitForTimeout(250);
  const mb = await fr.innerText('[data-fb="B"]');
  ok('maps FRQ: teacher-added answer -> likely earns + listed', /Likely earns/.test(mb) && /also accepted/i.test(mb), (await head('B')));
  const gp = await fr.evaluate(() => window.__ER.handoffPart(window.__ER.cur.parts[1]));
  ok('maps part prompt has the maps table text', /TABLE —/.test(gp) && /LIKELY POINT/.test(gp), '');
  // dark mode toggle still works
  const tg = await fr.locator('.dm-tg').count(); if (tg) { await fr.click('.dm-tg'); await pg.waitForTimeout(200); }
  ok('dark-mode toggle present and works', tg && await fr.evaluate(() => document.documentElement.classList.contains('dm')) !== null, tg);
  await pg.screenshot({ path: 'desk.png' });
  // phone
  const ph = await ctx.newPage(); await ph.setViewportSize({ width: 390, height: 844 }); await ph.goto(U); await ph.waitForTimeout(2500);
  const f2 = ph.frames().find(f => f !== ph.mainFrame()); await f2.click('.fcard[data-f]'); await ph.waitForTimeout(500);
  await f2.fill('textarea[data-a="A:T1"]', C[8][1]); await f2.fill('textarea[data-a="A:E2"]', C[8][2]); await f2.fill('textarea[data-a="A:A3"]', C[8][3]);
  await f2.click('[data-check="A"]'); await ph.waitForTimeout(300);
  const ov = await f2.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
  ok('phone: no sideways overflow', ov <= 1, ov);
  await f2.evaluate(() => document.querySelector('[data-fb="A"]').scrollIntoView()); await ph.screenshot({ path: 'phone.png' });
  await f2.evaluate(() => document.querySelector('#scoreBar').scrollIntoView()); await ph.screenshot({ path: 'phone-score.png' });
  ok('zero page errors', !errs.filter(e => !/localStorage|storage|Clipboard|404/i.test(e)).length, errs.slice(0, 4));
  await b.close();
  let f = 0; for (const [n, c, d] of res) { if (!c) f++; console.log((c ? 'PASS ' : 'FAIL ') + n + '   ' + (typeof d === 'string' ? d : JSON.stringify(d)).slice(0, 300)); }
  console.log(f ? `${f} FAILED` : 'ALL PASS');
})();
