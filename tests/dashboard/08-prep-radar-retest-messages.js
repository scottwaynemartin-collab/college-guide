const {FILE_URL, HTML_PATH, OUT, FIX} = require('./lib');
const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();
for (const [w,h] of [[1440,1000],[390,844]]){
 const ctx=await b.newContext({viewport:{width:w,height:h}, permissions:['clipboard-read','clipboard-write']}); const p=await ctx.newPage();
 const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>m.type()==='error'&&errs.push(m.text()));
 await p.goto(FILE_URL+'');await p.waitForTimeout(300);
 await p.click('text=Try it with sample data');await p.waitForTimeout(300);
 await p.screenshot({path:OUT+`/p6-${w}-overview.png`,fullPage:true});
 const go=async v=>{ if(w<800){ await p.click('[data-act=menu]'); await p.waitForTimeout(250);} await p.click(`aside [data-go=${v}]`); await p.waitForTimeout(250); };
 if (w>800){
  console.log('HERO', await p.textContent('.hero p'));
  console.log('OUTCOME', (await p.textContent('.orows')).replace(/\s+/g,' '));
  console.log('RADAR', (await p.locator('.rdr').first().textContent()).replace(/\s+/g,' ').slice(0,200), '| rows', await p.locator('.rrow').count());
  console.log('PRIO', await p.locator('.card:has(h2:text("Retest priority")) .gi').count(), (await p.locator('.card:has(h2:text("Retest priority")) .gi').first().textContent().catch(()=>'' )).replace(/\s+/g,' ').slice(0,200));
  await p.click('[data-act=make-groups]'); await p.waitForTimeout(200); await p.screenshot({path:OUT+`/p6-groups.png`});
  console.log('GROUPS', await p.locator('.gcard').count(), (await p.locator('.gcard').first().textContent()).replace(/\s+/g,' '));
  const sizes = await p.$$eval('.gcard', els=>els.map(e=>e.querySelectorAll('.gm').length)); console.log('SIZES', sizes.join(','));
  await p.click('[data-act=groups-copy]'); await p.waitForTimeout(200); console.log('CLIP groups', (await p.evaluate(()=>navigator.clipboard.readText())).slice(0,160));
  await p.keyboard.press('Escape');
  await p.click('[data-act=outcomes]'); await p.waitForTimeout(200); console.log('OUT rows', await p.locator('.modal tbody tr').count()); await p.screenshot({path:OUT+`/p6-outcomes.png`}); await p.keyboard.press('Escape');
 }
 await go('retestmsg'); await p.screenshot({path:OUT+`/p6-${w}-retestmsg.png`,fullPage:true});
 console.log('RM strip', (await p.textContent('.strip')).replace(/\s+/g,' '));
 const g0 = p.locator('.rmg').first();
 console.log('RM g0', (await g0.locator('h2').textContent()), 'checked', await g0.locator('[data-rm]:checked').count(), 'unchecked', await g0.locator('[data-rm]:not(:checked)').count());
 if (w>800){
  await g0.locator('[data-act=rm-copy]').click(); await p.waitForTimeout(200); console.log('CLIP canvas\n'+(await p.evaluate(()=>navigator.clipboard.readText())).slice(0,700));
  await g0.locator('[data-act=rm-prompt]').click(); await p.waitForTimeout(200); console.log('CLIP prompt\n'+(await p.evaluate(()=>navigator.clipboard.readText())).slice(0,600));
  const name = (await g0.locator('[data-rm]:checked').first().locator('xpath=..').textContent()).trim();
  const before = await p.locator('[data-rm]:checked').count();
  await g0.locator('[data-act=rm-sent]').click(); await p.waitForTimeout(300);
  console.log('after sent checked', before, '->', await p.locator('[data-rm]:checked').count(), '| hidden stat', (await p.textContent('.strip')).replace(/\s+/g,' '));
  const key = await p.evaluate(n=>Object.entries(DB.students).find(([k,s])=>s.name===n)[0], name);
  console.log('contact', JSON.stringify(await p.evaluate(k=>DB.contacts[k].slice(-1)[0].type, key)));
  await p.evaluate(k=>openStudent(k), key); await p.waitForTimeout(300);
  console.log('PREP', (await p.textContent('.tps')).replace(/\s+/g,' '));
  console.log('RMSENT', await p.locator('.rmsent').allTextContents());
  console.log('GROWTH', await p.locator('.growth svg circle').count(), (await p.textContent('.growth .cells')).replace(/\s+/g,' '));
  await p.screenshot({path:OUT+`/p6-conf.png`,fullPage:false}); await p.keyboard.press('Escape');
  await go('compare'); console.log('MONTH', (await p.textContent('.mbars')).replace(/\s+/g,' '));
  await go('ap'); console.log('BENCH', (await p.locator('.card:has(h2:text("Benchmarks"))').first().textContent()).replace(/\s+/g,' ').slice(0,300));
  await p.screenshot({path:OUT+`/p6-ap.png`,fullPage:true});
  await go('options'); console.log('SET', await p.inputValue('#setRmCut'), (await p.inputValue('#setRetestMsg')).match(/below 80/)?'msg ok':'msg BAD', await p.inputValue('#setB_APHG'));
  await p.goto(FILE_URL+'#ttess'); await p.waitForTimeout(400);
  const tt = await p.textContent('.ttview'); console.log('TT', ['Retest priority','Reteach groups made','Retest messages sent','student data on request'].map(k=>k+':'+(tt.match(new RegExp(k+'[^·]{0,60}'))||[''])[0]).join(' | '));
 }
 console.log(w, 'ERR', JSON.stringify(errs));
 await ctx.close();
}
await b.close();})();
