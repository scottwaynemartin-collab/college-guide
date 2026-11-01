const {FILE_URL, HTML_PATH, OUT, FIX} = require('./lib');
const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1440,height:1000}});
const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto(FILE_URL+'');await p.click('aside [data-go=import]');
await p.fill('#pasteBox',`Student,Student ID,Class,8th STAAR %,8th STAAR Level,AP Exam,Q1 Grade,Q2 Grade (to date),TIA BOY 26-27 %,Prior AP score (APHG 2026),Prior TIA BOY/EOY 25-26 %,Grade level,Q1 Unweighted GPA,Q1 Weighted GPA,Est. rank band,Est. quartile
"Test, Alpha",900001,APHG 3B,78,Meets,Paid,88,91,62%,,,9,3.71,4.61,Top 25%,Q1
"Test, Bravo",900002,AP World 1A,55,Approaches,Unpaid,71,68,40%,3,58%,10,2.9,3.8,Bottom 50%,Q3`);
await p.click('#pasteGo');await p.waitForTimeout(300);
console.log(await p.evaluate(()=>JSON.stringify(DB.profiles,null,0)));
await p.click('aside [data-go=overview]');await p.click('.rrow');await p.waitForTimeout(200);
console.log((await p.$eval('.conf',e=>e.innerText)).slice(0,700));
console.log('ERR',errs);await b.close();})();
