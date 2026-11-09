const {FILE_URL, HTML_PATH, OUT, FIX} = require('./lib');
const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1440,height:1000}});
const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto(FILE_URL+'');await p.click('aside [data-go=import]');
const H='Student,Student ID,Class,Absences YTD (full-day),Unexcused/unresolved absences,Tardies YTD,Zeros (all classes),Classes below 70 now,Lowest class now,Power Hour drafts,Power Hour no-shows,Power Hour attended,Last Power Hour draft,Power Hour assigned now,Watch flags,Counselor';
await p.fill('#profBox',H+'\n"Fake, Delta",900010,APHG 4A,6,2,3,4,1,Chemistry 66,3,1,2,"Tue, Oct 27","Thu, Nov 5 A Block","Zeros; Below 70 in a class",Ms. Example');await p.click('[data-act=import-profile]');await p.waitForTimeout(200);
// re-import with blanks: values should stay
await p.fill('#profBox',H+'\n"Fake, Delta",900010,APHG 4A,7,,,,,,,,,,,');await p.click('[data-act=import-profile]');await p.waitForTimeout(200);
const k=await p.evaluate(()=>DB.idmap['900010']);
console.log(await p.evaluate(k=>JSON.stringify(DB.profiles[k]),k));
await p.evaluate(k=>openStudent(k,true),k);await p.waitForTimeout(200);
const t=await p.$eval('.conf',e=>e.innerText);
console.log(['Counselor: Ms. Example','ATTENDANCE & ALL CLASSES','POWER HOUR','Zeros','Below 70 in a class','Chemistry 66','Thu, Nov 5 A Block','7'].map(x=>x+':'+t.includes(x)).join(' | '));
console.log('scores', await p.evaluate(k=>Object.keys(DB.scores[k]||{}).length,k), 'ERR',errs);await b.close();})();
