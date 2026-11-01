const {FILE_URL, HTML_PATH, OUT, FIX} = require('./lib');
const {chromium}=require('playwright');
const csv=`Student,Student ID,Class,Platform,APHG · Unit 1 Progress Check MCQ,APHG · Unit 1 Progress Check FRQ,APHG · Unit 2 Progress Check MCQ,APHG · Unit 2 MC Test,APHG · Unit 2 MC Retest,AP Euro · Unit 1 Progress Check MCQ,AP Euro · Unit 2 Progress Check MCQ
"Case, A",800001,APHG 3B,AP Classroom,50%,10%,52%,60%,58%,,
"Case, B",800002,APHG 3B,AP Classroom,30%,100%,40%,61%,57%,,
"Case, C",800003,APHG 3B,AP Classroom,50%,,48%,46%,,,
"Case, D",800004,APHG 3B,AP Classroom,30%,,35%,60%,40%,,
"Case, E",800005,APHG 3B,AP Classroom,30%,,40%,35%,44%,,
"Case, G",800007,APHG 3B,AP Classroom,70%,,M,,60%,,
"Case, H",800008,APHG 3B,AP Classroom,70%,,,,,30%,35%
"Case, H",800008,AP Euro 1B,AP Classroom,,,,,,30%,35%`;
const canvas=`Student,Student ID,Class,Platform,APHG · Unit 1 Test,APHG · Unit 2 Test
"Case, E",800005,APHG 3B,Canvas,100%,100%
"Case, F",800006,APHG 3B,Canvas,90%,95%`;
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1440,height:1000}});
const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto(FILE_URL+'');await p.click('aside [data-go=import]');
await p.fill('#pasteBox',csv);await p.click('#pasteGo');await p.waitForTimeout(200);
await p.fill('#pasteBox',canvas);await p.click('#pasteGo');await p.waitForTimeout(200);
const out=await p.evaluate(()=>{const m=buildModel();return m.studs.sort((a,b)=>a.name.localeCompare(b.name)).map(s=>s.name+' → '+s.cs.map(c=>`[${c.cls}] ${STATUS[c.ap.status].label}: ${c.ap.reason}`).join(' | ')+'  overall='+s.status);});
console.log(out.join('\n'));
await p.click('aside [data-go=overview]');await p.waitForTimeout(200);
console.log('tiles', await p.$$eval('.tile .tn',x=>x.map(e=>e.textContent).join(',')));
await p.screenshot({path:OUT+'/aprule.png',fullPage:false});
console.log('ERR',errs);await b.close();})();
