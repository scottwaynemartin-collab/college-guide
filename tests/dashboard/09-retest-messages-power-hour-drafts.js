const {FILE_URL, HTML_PATH, OUT, FIX} = require('./lib');
const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();
const ctx=await b.newContext({viewport:{width:1440,height:1000},permissions:['clipboard-read','clipboard-write']});const p=await ctx.newPage();
const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>m.type()==='error'&&errs.push(m.text()));
await p.goto(FILE_URL+'');await p.click('text=Try it with sample data');await p.waitForTimeout(300);
// retest messages: below 80
await p.click('aside [data-go=retestmsg]');await p.waitForTimeout(200);
console.log('RM strip:', (await p.textContent('.strip')).replace(/\s+/g,' '));
console.log('RM intro:', (await p.textContent('.phead p')).slice(0,120));
console.log('RM optional rows:', await p.locator('.rmopt').count(), '| checked:', await p.locator('[data-rm]:checked').count());
await p.locator('.rmg').first().locator('[data-act=rm-copy]').click(); await p.waitForTimeout(150);
const clip=await p.evaluate(()=>navigator.clipboard.readText()); console.log('RM msg wording:', /below 80/.test(clip)?'below 80 ✓':'WRONG', /70 or below/.test(clip)?'still has 70!':'');
const g0=p.locator('.rmg').first(); const nBefore=await g0.locator('[data-rm]:checked').count();
await g0.locator('[data-act=rm-sent]').click(); await p.waitForTimeout(200);
await p.locator('.rmg').first().locator('[data-act=rm-sent]').click().catch(()=>{}); await p.waitForTimeout(200);
console.log('RM contacts logged (dedupe check):', await p.evaluate(()=>Object.values(DB.contacts).flat().filter(c=>/^Retest message/.test(c.type)).length), 'for', nBefore, 'selected');
// PH drafts page
await p.click('aside [data-go=phdraft]');await p.waitForTimeout(200);
console.log('PD strip:', (await p.textContent('.strip')).replace(/\s+/g,' '));
console.log('PD first row:', (await p.locator('.rmrow').first().textContent()).replace(/\s+/g,' ').slice(0,160));
const excl = await p.evaluate(()=>Object.values(DB.profiles).filter(pr=>pr.phNow).length); console.log('profiles with phNow:', excl);
for (const k of ['c70','c80']){ await p.click(`[data-pdlist=${k}]`); await p.waitForTimeout(200); console.log(k, (await p.textContent('.strip')).replace(/\s+/g,' ').slice(0,90)); }
await p.click('[data-pdlist=test]'); await p.waitForTimeout(200);
await p.click('[data-act=pd-roster]'); await p.waitForTimeout(150); const ro=await p.evaluate(()=>navigator.clipboard.readText()); console.log('ROSTER lines', ro.split('\n').length, '|', ro.split('\n')[0]);
await p.click('[data-act=pd-prompt]'); await p.waitForTimeout(150); console.log('PROMPT:\n'+(await p.evaluate(()=>navigator.clipboard.readText())).slice(0,420));
const sel = await p.locator('[data-pd]:checked').count(); const uniq = await p.evaluate(()=>new Set((UI.pdRows||[]).map(r=>r.s.key)).size);
await p.click('[data-act=pd-drafted]'); await p.waitForTimeout(250);
console.log('after Mark drafted: lines', sel, 'unique students', uniq, 'contacts logged', await p.evaluate(()=>Object.values(DB.contacts).flat().filter(c=>/^PH draft/.test(c.type)).length), '| strip:', (await p.textContent('.strip')).replace(/\s+/g,' ').slice(0,120));
console.log('sample contact:', await p.evaluate(()=>Object.values(DB.contacts).flat().filter(c=>/^PH draft/.test(c.type))[0]));
await p.click('[data-act=pd-drafted]').catch(()=>{}); await p.waitForTimeout(150);
// settings
await p.click('aside [data-go=options]'); await p.waitForTimeout(200); console.log('SET cut', await p.inputValue('#setRmCut'), 'msg2 field present:', await p.locator('#setRetestMsg2').count(), 'msg has below 80:', /below 80/.test(await p.inputValue('#setRetestMsg')));
await p.click('[data-act=save-settings]'); await p.waitForTimeout(200);
await p.screenshot({path:OUT+'/pd.png'});
console.log('ERR', errs); await b.close();})();
