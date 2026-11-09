const {FILE_URL, HTML_PATH, OUT, FIX} = require('./lib');
const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const ctx=await b.newContext({viewport:{width:1440,height:1000},permissions:['clipboard-read','clipboard-write']});const p=await ctx.newPage();
const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>m.type()==='error'&&errs.push(m.text()));p.on('dialog',d=>{errs.push('DIALOG');d.dismiss();});
await p.goto(FILE_URL+'');await p.click('text=Try it with sample data');await p.waitForTimeout(300);
await p.click('.rrow');await p.waitForTimeout(200);
await p.fill('[data-agform$="|goal"]','Raise APHG to 85');await p.click('[data-confheld]');await p.waitForTimeout(150);
await p.click('[data-contact$="|Counselor referral"]');await p.waitForTimeout(150);
await p.click('[data-email]');await p.waitForTimeout(100);await p.keyboard.press('Escape');await p.waitForTimeout(100);await p.keyboard.press('Escape');
await p.click('aside [data-go=ttess]');await p.waitForTimeout(300);
console.log(await p.$eval('.ttview',e=>e.innerText.slice(0,2500)));
const names=await p.evaluate(()=>{const t=document.querySelector('.ttview').innerText;return Object.values(DB.students).map(s=>s.name).filter(n=>t.includes(n));});
console.log('names leaked:',names.length, 'rows', await p.$$eval('.ttr',x=>x.length), 'scope chips', await p.$$eval('[data-course]',x=>x.length));
await p.screenshot({path:OUT+'/ttess2.png',fullPage:true});
// scoped
await p.click('[data-course="APHG"]'); await p.waitForTimeout(200); console.log('APHG intro:', (await p.$eval('.ttview .phead p',e=>e.innerText)).slice(0,120));
// links
await p.click('.ttgo[data-anchor=radarCard]'); await p.waitForTimeout(300); console.log('after link view=', await p.evaluate(()=>UI.view), 'course', await p.evaluate(()=>UI.course), 'radar exists', !!(await p.$('#radarCard')));
await p.click('aside [data-go=ttess]');await p.waitForTimeout(200); await p.click('.ttgo[data-act=make-groups]'); await p.waitForTimeout(200); console.log('groups modal', await p.$$eval('.gcard',x=>x.length)); await p.keyboard.press('Escape');
await p.click('[data-act=copy-ttess]'); await p.waitForTimeout(200); const clip=await p.evaluate(()=>navigator.clipboard.readText()); console.log('CLIP', clip.split('\n').length, 'lines;', clip.slice(0,200));
// printable text in artifact mode
await p.setViewportSize({width:1000,height:1300});
await p.evaluate(()=>{ window.print=()=>{}; }); await p.click('[data-act=print-ttess]'); await p.waitForTimeout(150);
console.log('printArea?', (await p.evaluate(()=>document.getElementById('printArea').innerHTML.length)));
await p.evaluate(()=>document.body.classList.add('printing')); await p.emulateMedia({media:'print'}); await p.pdf({path:OUT+'/ttess2.pdf',format:'Letter',printBackground:true});
// settings card gone
await p.emulateMedia({media:'screen'}); await p.evaluate(()=>document.body.classList.remove('printing')); await p.click('aside [data-go=options]'); await p.waitForTimeout(200); console.log('settings has ttess card:', (await p.$eval('#view',e=>e.innerText)).includes('T-TESS summary'));
console.log('ERR',errs);await b.close();})();
