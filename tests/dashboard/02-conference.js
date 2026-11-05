const {FILE_URL, HTML_PATH, OUT, FIX} = require('./lib');
const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();
for (const [w,h] of [[1440,1000],[390,844]]){
const p=await b.newPage({viewport:{width:w,height:h}});
const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('dialog',d=>{errs.push('DIALOG');d.dismiss();});
p.on('request',r=>{const u=r.url(); if(!/^(file|data|blob|about):/.test(u)) errs.push('NET '+u);});
await p.goto(FILE_URL+'');await p.click('text=Try it with sample data');await p.waitForTimeout(300);
await p.click('.rrow');await p.waitForTimeout(300);
await p.click('[data-agrate$="|Q1|3"]');await p.waitForTimeout(150);
await p.fill('[data-agency$="|Q1|goal"]','85');await p.fill('[data-agency$="|Q2|goal"]','90');await p.fill('#confNote','Met with parent. Goal: turn in Unit 2 corrections by Friday.');
await p.click('[data-agrate$="|Q2|2"]');await p.waitForTimeout(200);
await p.screenshot({path:OUT+`/${w}-conf.png`,fullPage:false});
const full = await p.evaluate(()=>{ const c=document.querySelector('.conf'); return c.scrollHeight; });
await p.setViewportSize({width:w,height:Math.min(full,9000)}); await p.waitForTimeout(200); await p.screenshot({path:OUT+`/${w}-conf-full.png`}); await p.setViewportSize({width:w,height:h});
await p.click('[data-email]');await p.waitForTimeout(150);await p.keyboard.press('Escape');await p.waitForTimeout(150);
const back = await p.evaluate(()=>!!document.querySelector('.conf'));
const saved = await p.evaluate(()=>{ const k=document.querySelector('#layer').dataset.student; return [DB.agency[k], DB.confNotes[k]]; });
await p.emulateMedia({media:'print'}); await p.screenshot({path:OUT+`/${w}-conf-print.png`}); await p.emulateMedia({media:'screen'});
console.log(w,'back to conf',back,JSON.stringify(saved),'ERR',errs); await p.close();}
await b.close();})();
