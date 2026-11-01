const {FILE_URL, HTML_PATH, OUT, FIX} = require('./lib');
const {chromium}=require('playwright');
const H='Student,Student ID,Class,8th STAAR %,8th STAAR Level,AP Exam,Q1 Grade,Q2 Grade (to date),TIA BOY 26-27 %,TIA BOY 26-27 test,Prior AP score (APHG 2026),Prior TIA BOY 25-26 %,Prior TIA EOY 25-26 %,Prior TIA test,Grade level,Q1 Unweighted GPA (all classes),"Q1 Weighted GPA (all classes, est.)",Q1 classes counted,Est. rank band (from Q1 weighted GPA),Est. quartile,Rank cutoffs used,"AP scores (all, from Aware)",PSAT history (total(EBRW/Math)),Best PSAT,SAT history,Best SAT,Q2-to-date Unweighted GPA (all classes),"Q2-to-date Weighted GPA (all classes, est.)",Q2 classes counted,Absences YTD (full-day),Unexcused/unresolved absences,Tardies YTD,Zeros (all classes),Classes below 70 now,Lowest class now,Power Hour drafts,Power Hour no-shows,Power Hour attended,Last Power Hour draft,Power Hour assigned now,Watch flags,Counselor,TIA EOY 26-27 %';
const rows=[
'"Fake, Alpha",900001,APHG 3B,78,Meets,Paid,88,91,62%,TIA BOY APHG,,,,,9,3.71,4.61,7,Top 25%,Q1,"Top10 4.6, Top25 4.3",,1010(500/510),1010,,,3.80,4.70,7,2,0,1,0,0,Geometry 84,0,0,0,,,,Ms. Fake,',
'"Fake, Bravo",900002,AP World 1A,55,Approaches,Unpaid,71,64,40%,TIA BOY World,3,45%,58%,TIA APHG,10,2.9,3.8,7,Bottom 50%,Q3,"Top10 4.6",APHG 3 (2026),930(470/460); 1010(500/510),1010,1100(550/550),1100,2.70,3.55,7,11,4,9,5,2,AP World 64,4,2,2,"Thu, Oct 29","Tue, Nov 3 A Block","Below 70 in 2 classes; 5 zeros; Attendance",Mr. Fake,',
'"Fake, Bravo",900002,AP Euro 1B,55,Approaches,Unpaid,80,77,,,,,,,10,,,,,,,,,,,,,,,,,,,,,,,,,,,,'];
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1440,height:1000}});
const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('dialog',d=>{errs.push('DIALOG');d.dismiss();});
await p.goto(FILE_URL+'');
await p.click('aside [data-go=import]');
await p.fill('#profBox',[H,...rows].join('\n'));await p.click('[data-act=import-profile]');await p.waitForTimeout(300);
const r1=await p.evaluate(()=>({n:Object.keys(DB.students).length, classes:DB.students['bravo fake']?.classes, byClass:DB.profiles['bravo fake']?.byClass, other:DB.profiles['bravo fake']?.other, uw2:DB.profiles['bravo fake']?.uw2, w2:DB.profiles['bravo fake']?.w2, priorTiaBoy:DB.profiles['bravo fake']?.priorTiaBoy, priorTiaEoy:DB.profiles['bravo fake']?.priorTiaEoy, tiaBoyTest:DB.profiles['bravo fake']?.tiaBoyTest, flags:schoolFlags('bravo fake'), msg:document.querySelector('#profileCard .note')?.innerText}));
console.log(JSON.stringify(r1));
// re-import with a change
await p.fill('#profBox',[H, rows[1].replace(',11,4,9,',',12,4,9,')].join('\n'));await p.click('[data-act=import-profile]');await p.waitForTimeout(300);
console.log('reimport', await p.evaluate(()=>[Object.keys(DB.students).length, DB.profiles['bravo fake'].absences, DB.profiles['bravo fake'].byClass['AP Euro 1B'].grade1]));
// sample + filters
await p.click('aside [data-go=options]'); await p.click('[data-act=sample]'); await p.waitForTimeout(150); if (await p.$('#yesBtn')) await p.click('#yesBtn'); await p.waitForTimeout(300);
await p.click('aside [data-go=overview]');
const c0=await p.$$eval('.rrow',x=>x.length);
await p.click('[data-apf=unpaid]'); const c1=await p.$eval('.card .count',e=>e.textContent);
await p.click('[data-apf=all]'); await p.click('[data-quart=Q4]'); const c2=await p.$eval('.card .count',e=>e.textContent);
await p.click('[data-quart=all]'); await p.click('[data-act=flags-only]'); const c3=await p.$eval('.card .count',e=>e.textContent);
await p.click('[data-act=flags-only]');
console.log('roster', c0, 'unpaid', c1, 'Q4', c2, 'flagged', c3);
await p.screenshot({path:OUT+'/spec-overview.png',fullPage:true});
// conference
await p.click('.card:has(h2:text("Watch list")) .gi'); await p.waitForTimeout(250);
await p.fill('[data-agform$="|goal"]','Raise APHG to 85 by end of Q2'); await p.fill('[data-agform$="|steps"]','1. Power Hour Thursdays\n2. Corrections by Friday'); await p.fill('[data-agform$="|checkin"]','2026-11-13');
const k = await p.evaluate(()=>document.querySelector('#layer').dataset.student);
console.log('form', await p.evaluate(k=>JSON.stringify(DB.agency[k].form),k));
await p.screenshot({path:OUT+'/spec-conf.png'});
const hgt = await p.evaluate(()=>document.querySelector('.conf').scrollHeight); await p.setViewportSize({width:1440,height:Math.min(hgt,6000)}); await p.screenshot({path:OUT+'/spec-conf-full.png'});
await p.setViewportSize({width:1000,height:1300}); await p.emulateMedia({media:'print'}); await p.waitForTimeout(200);
await p.pdf({path:OUT+'/spec-conf.pdf',format:'Letter',printBackground:true});
await p.emulateMedia({media:'screen'});
console.log('ERR',errs);await b.close();})();
