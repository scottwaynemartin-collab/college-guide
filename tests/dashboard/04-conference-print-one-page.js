const {FILE_URL, HTML_PATH, OUT, FIX} = require('./lib');
const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1440,height:1000}});
await p.goto(FILE_URL+'');await p.click('text=Try it with sample data');await p.waitForTimeout(300);
await p.click('.rrow');await p.waitForTimeout(200);
for (const [sel,v] of [['goal','Raise APHG to 85 by the end of Q2 by turning in all corrections'],['steps','1. Power Hour Thursdays\n2. Corrections by Friday\n3. Redo DBQ thesis'],['nextStep','Redo U2 DBQ thesis'],['support','Check in each Thursday'],['skillStrength','sourcing'],['skillGap','evidence, reasoning']]) await p.fill(`[data-agform$="|${sel}"]`,v);
await p.fill('[data-agform$="|checkin"]','2026-11-13'); await p.fill('#confNote','Met with parent; agreed on Thursday Power Hour and weekly email update.');
for (const q of [1,2]) { await p.click(`[data-agrate$="|Q${q}|3"]`); await p.waitForTimeout(100); await p.fill(`[data-agency$="|Q${q}|goal"]`,'85'); await p.fill(`[data-agency$="|Q${q}|next"]`,'Turn in corrections'); }
await p.setViewportSize({width:1000,height:1300});await p.emulateMedia({media:'print'});await p.pdf({path:OUT+'/r3b.pdf',format:'Letter',printBackground:true});await b.close();})();
