const {FILE_URL, OUT} = require('./lib');
const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1300,height:900}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto(FILE_URL+'');await p.waitForTimeout(200);
console.log('parseScore', JSON.stringify(await p.evaluate(()=>['12/15 pts','12/15 (80%)','8.5 of 10','-/10','—/10','85 (B)','85%','M','EX','-','0','91.333333','7/0'].map(v=>[v,parseScore(v, v==='85 (B)'?100:null)]))));
console.log('matchSource', await p.evaluate(()=>['TAC','Teacher Access Center','College Board','Canvas','AP Classroom','Gradebook','ap','zzz'].map(v=>v+'→'+matchSource(v)).join(', ')));
console.log('isProfile spatial', await p.evaluate(()=>isProfile([['Student','Student ID','Class','APHG · Unit 1 Spatial Concepts Quiz','APHG · Unit 1 MC Test']])), '| real profile', await p.evaluate(()=>isProfile([['Student','Student ID','Class','TIA BOY 26-27 %','Q1 Weighted GPA']])), await p.evaluate(()=>isProfile([['Student ID','8th STAAR %','AP Exam']])));
console.log('nameKey', await p.evaluate(()=>[nameKey('Ramírez, José'), nameKey('Jose Ramirez'), nameKey('Garcia-Lopez, Ana'), nameKey('李 小龙')].join(' | ')));
// same-name students and accents via import
await p.click('aside [data-go=import]'); await p.waitForTimeout(200);
const paste = async (txt, year) => { await p.fill('#pasteBox', txt); if (year) await p.fill('#pasteYear', year); await p.click('[data-act=paste]'); await p.waitForTimeout(300); };
await paste('Student,Student ID,Class,Platform,APHG · Unit 1 MC Test\n"Hernandez, Jose",50001,APHG 3B,AP Classroom,95\n"Hernandez, Jose",50002,AP World 1A,AP Classroom,40\n"Ramírez, José",50003,APHG 3B,Gradebook,80\n"Reyes, Ava Marie",50004,APHG 3B,Gradebook,77');
await paste('Student,Student ID,Class,Platform,APHG · Unit 2 MC Test\nJose Ramirez,,APHG 3B,AP Classroom,70\nAva Reyes,,APHG 3B,AP Classroom,66');
console.log('students', JSON.stringify(await p.evaluate(()=>Object.entries(DB.students).map(([k,s])=>[k,s.name,s.ids.join('/'),s.classes.join('/'),Object.keys(DB.scores[k]||{}).length]))));
// Spatial grade CSV without platform → grades, not profile
await paste('Student,Student ID,Class,APHG · Unit 1 Spatial Concepts Quiz\n"Hernandez, Jose",50001,APHG 3B,88');
console.log('spatial routed:', await p.evaluate(()=>UI.lastResult.split('\n').pop()));
// Canvas with Notes and 0-point column
await paste('Student,ID,SIS User ID,SIS Login ID,Section,Unit 1 Quiz (101),Notes,Bonus (103),Final Grade Reflection (1006),Current Score\n    Points Possible,,,,,20,,0,10,(read only)\n"Hernandez, Jose",11,50001,jh,APHG 3B,18,called 9/12,3,9,90');
console.log('canvas assigns:', await p.evaluate(()=>Object.values(DB.assignments).filter(a=>a.source==='Canvas').map(a=>a.name).join(', ')));
// year rollover: set currentYear to next year via settings and reload
const before = await p.evaluate(()=>({cur:curYear(), cls:DB.students['jose hernandez'].classes.join('/'), cy:DB.students['jose hernandez'].cy}));
await p.evaluate(()=>{ DB.settings.currentYear='2027-28'; save(); }); await p.reload(); await p.waitForTimeout(300);
const after = await p.evaluate(()=>({cur:curYear(), cls:DB.students['jose hernandez'].classes.join('/'), past:JSON.stringify(DB.students['jose hernandez'].past)}));
await p.evaluate(()=>{ DB.settings.currentYear=''; save(); }); await p.reload(); await p.waitForTimeout(300);
const back = await p.evaluate(()=>({cur:curYear(), cls:DB.students['jose hernandez'].classes.join('/'), past:JSON.stringify(DB.students['jose hernandez'].past||{})}));
console.log('rollover', JSON.stringify(before), '→', JSON.stringify(after), '→ back', JSON.stringify(back));
// old backup without cb.district → restore → at a glance works
await p.evaluate(()=>{ const d=JSON.parse(JSON.stringify(DB)); d.cb={scores:[],ipr:[]}; delete d.groups; window.__old=JSON.stringify(d); });
await p.click('aside [data-go=options]'); await p.waitForTimeout(150); await p.click('[data-act=restore]'); await p.waitForTimeout(100);
await p.evaluate(()=>{ document.getElementById('restoreText').value = window.__old; }); await p.click('#restoreGo'); await p.waitForTimeout(400);
await p.click('aside [data-go=admin]'); await p.waitForTimeout(300); console.log('after old restore, at a glance renders:', !!(await p.$('.adm')), 'district array', await p.evaluate(()=>Array.isArray(DB.cb.district)));
// wipe removes undo
await p.click('aside [data-go=options]'); await p.waitForTimeout(150); await p.click('[data-act=wipe]'); await p.waitForTimeout(100); await p.click('#yesBtn'); await p.waitForTimeout(200);
console.log('undo after wipe:', await p.evaluate(()=>localStorage.getItem('classroomDashboard.v1.undo')));
// quota: simulate full storage
await p.evaluate(()=>{ const orig = Storage.prototype.setItem; Storage.prototype.setItem = function(k,v){ if (k==='classroomDashboard.v1') throw new DOMException('full','QuotaExceededError'); return orig.call(this,k,v); }; save(); });
console.log('warn banner:', await p.evaluate(()=>document.getElementById('saveWarn')?.innerText.slice(0,60)));
const st = await p.evaluate(()=>1); console.log('ERR', errs); await b.close();})();
