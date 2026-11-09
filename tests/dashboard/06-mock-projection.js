const {FILE_URL, HTML_PATH, OUT, FIX} = require('./lib');
const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1440,height:1000}});
const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('dialog',d=>{errs.push('DIALOG');d.dismiss();});
await p.goto(FILE_URL+'');await p.click('text=Try it with sample data');await p.waitForTimeout(300);
const r=await p.evaluate(()=>{const m=buildModel();const w=m.studs.find(s=>s.cs.some(c=>c.course==='AP World'));const c=w.cs.find(c=>c.course==='AP World');const h=m.studs.find(s=>s.cs.some(c=>c.course==='APHG'));const hc=h.cs.find(c=>c.course==='APHG');
 return {world:projText(c), worldKind:c.proj.kind, aphg:projText(hc), aphgKind:hc.proj.kind, unitHasWriting: hc.unitProj.wrPct};});
console.log(JSON.stringify(r,null,1));
await p.click('aside [data-go=ap]');await p.waitForTimeout(300);await p.screenshot({path:OUT+'/mock-ap.png',fullPage:false});
await p.click('aside [data-go=compare]');await p.click('[data-course="APHG"]');await p.waitForTimeout(300);
console.log(await p.$eval('.card:has(h2:text("Mock projection vs. actual"))',e=>e.innerText.replace(/\n+/g,' | ').slice(0,400)));
await p.screenshot({path:OUT+'/mock-compare.png',fullPage:true});
// writing toggle
await p.click('aside [data-go=options]');await p.click('[data-act=save-settings]');await p.waitForTimeout(200);
console.log('with writing:', await p.evaluate(()=>{const m=buildModel();const h=m.studs.find(s=>s.cs.some(c=>c.course==='APHG'));return projText(h.cs.find(c=>c.course==='APHG'));}));
await p.click('aside [data-go=overview]');await p.click('.rrow');await p.waitForTimeout(200);
console.log(await p.$eval('.fsec:has(h2:text("AP on pace"))',e=>e.innerText.slice(0,300)));
console.log('ERR',errs);await b.close();})();
