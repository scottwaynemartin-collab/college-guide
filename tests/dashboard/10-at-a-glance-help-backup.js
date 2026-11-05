const {FILE_URL, HTML_PATH, OUT, FIX} = require('./lib');
const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();
const ctx=await b.newContext({viewport:{width:1440,height:1000},permissions:['clipboard-read','clipboard-write']});const p=await ctx.newPage();
const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>m.type()==='error'&&errs.push(m.text()));
await p.goto(FILE_URL+'');await p.click('text=Try it with sample data');await p.waitForTimeout(300);
// help page
await p.click('aside [data-go=help]');await p.waitForTimeout(200); console.log('HELP cards', await p.locator('.card').count(), 'header', (await p.textContent('#top b')).trim());
await p.click('[data-act=copy-chatnote]'); await p.waitForTimeout(150); console.log('CHATNOTE', (await p.evaluate(()=>navigator.clipboard.readText())).split('\n').length, 'lines');
// district import
await p.click('aside [data-go=import]'); await p.waitForTimeout(200);
await p.fill('#pasteBox', 'Course,Year,Campus,Participation %\nAPHG,2026,Panther Creek,71\nAPHG,2026,Lone Star,58\nAPHG,2026,Heritage,64\nAP World,2026,Panther Creek,66\nAP World,2026,Lone Star,49\nAP World,2026,Heritage,55');
await p.click('[data-act=paste]'); await p.waitForTimeout(300); console.log('IMPORT result:', (await p.evaluate(()=>UI.lastResult||'')).slice(0,120), '| district rows', await p.evaluate(()=>DB.cb.district.length));
// at a glance
await p.click('aside [data-go=admin]');await p.waitForTimeout(300);
console.log('ADMIN header', (await p.textContent('#top b')).trim(), '| strip:', (await p.textContent('.adm .strip')).replace(/\s+/g,' '));
console.log('ADMIN charts', await p.locator('.dchart').count(), 'highlighted rows', await p.locator('.drow2.me').count(), (await p.locator('.dchart').first().textContent()).replace(/\s+/g,' ').slice(0,140));
console.log('ADMIN tables', await p.locator('.adm table').count(), '| first proj row:', (await p.locator('.adm table').first().locator('tbody tr').first().textContent()).replace(/\s+/g,' ').slice(0,120));
const names=await p.evaluate(()=>{const t=document.querySelector('.adm').innerText;return Object.values(DB.students).map(s=>s.name).filter(n=>t.includes(n));}); console.log('names leaked', names.length);
await p.click('[data-act=copy-admin]'); await p.waitForTimeout(150); console.log('ADMIN TEXT:\n'+(await p.evaluate(()=>navigator.clipboard.readText())).slice(0,500));
await p.screenshot({path:OUT+'/admin.png',fullPage:true});
await p.setViewportSize({width:1000,height:1300}); await p.evaluate(()=>{ window.print=()=>{}; }); await p.click('[data-act=print-admin]'); await p.waitForTimeout(150);
await p.evaluate(()=>document.body.classList.add('printing')); await p.emulateMedia({media:'print'}); await p.pdf({path:OUT+'/admin.pdf',format:'Letter',printBackground:true});
await p.emulateMedia({media:'screen'}); await p.evaluate(()=>document.body.classList.remove('printing')); await p.setViewportSize({width:1440,height:1000});
// backup compress/restore
await p.click('aside [data-go=options]'); await p.waitForTimeout(200); await p.click('[data-act=backup]'); await p.waitForTimeout(500);
const bk = await p.inputValue('#outText'); console.log('BACKUP', bk.slice(0,5), Math.round(bk.length/1024)+'KB vs json', Math.round((await p.evaluate(()=>JSON.stringify(DB).length))/1024)+'KB', '| title', (await p.textContent('.modal h2')).trim());
await p.keyboard.press('Escape'); await p.waitForTimeout(100);
const before = await p.evaluate(()=>Object.keys(DB.students).length);
await p.click('[data-act=wipe]'); await p.waitForTimeout(100); await p.click('#yesBtn'); await p.waitForTimeout(200);
await p.click('aside [data-go=options]'); await p.waitForTimeout(100); await p.click('[data-act=restore]'); await p.waitForTimeout(100); await p.fill('#restoreText', bk); await p.click('#restoreGo'); await p.waitForTimeout(500);
console.log('RESTORE students', before, '->', await p.evaluate(()=>Object.keys(DB.students).length), '| lastBackup set', await p.evaluate(()=>!!DB.lastBackup), '| settings shows', ((await p.textContent('#view')).match(/Last backup: [^.]+/)||[''])[0]);
await p.evaluate(()=>{ DB.lastBackup = Date.now()-20*864e5; DB.sample=false; save(); }); await p.click('aside [data-go=overview]'); await p.waitForTimeout(200); console.log('REMINDER chip', (await p.locator('.syncs button').textContent().catch(()=>'none')).trim());
// data check item
await p.evaluate(()=>{ const id='AP Classroom:aphg · unit 9 quiz thing'; DB.assignments[id]={id,name:'APHG · Unit 9 Quiz Thing',source:'AP Classroom',order:9999,hidden:false,year:curYear()}; save(); });
await p.click('aside [data-go=import]'); await p.waitForTimeout(200); console.log('DATACHECK', ((await p.textContent('#view')).match(/AP Classroom items not counted[^\n]{0,80}/)||['none'])[0]);
await p.click('aside [data-go=overview]'); await p.waitForTimeout(100); await p.click('[data-act=copy-summary]'); await p.waitForTimeout(150); console.log('SUMMARY line:', (await p.evaluate(()=>navigator.clipboard.readText())).split('\n')[3]);
console.log('ERR', errs); await b.close();})();
