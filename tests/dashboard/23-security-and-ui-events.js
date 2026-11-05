const {FILE_URL, OUT} = require('./lib');
const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1440,height:1000}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto(FILE_URL+'');await p.click('text=Try it with sample data');await p.waitForTimeout(300);
await p.evaluate(()=>{ window.__pw=[]; const k=Object.keys(DB.students).find(k=>DB.students[k].classes.length); DB.students[k].name='Zed <img src=x onerror=__pw.push(1)>'; const a=Object.values(DB.assignments).find(a=>a.source==='AP Classroom'&&yearOf(a)===curYear()); a.name='APHG · Unit 1 MC Test <img src=x onerror=__pw.push(2)>'; DB.settings.scale=[[90,'A'],[80,'B'],[70,'C'],[60,'D'],[0,'<img src=x onerror=__pw.push(3)>']];
  DB.cb.scores.push({course:'APHG', year:'<img src=x onerror=__pw.push(4)>', dist:{5:5,4:5,3:5,2:5,1:5}, n:25, pass:60, mean:3}); save(); render(); });
// hover every tooltip on overview, compare, conference
let hovered=0; const hoverAll = async () => { const els = await p.$$('[data-tip]'); for (const el of els.slice(0,400)) { try { await el.hover({timeout:200, force:true}); hovered++; } catch(_){} } };
await hoverAll();
await p.click('aside [data-go=compare]'); await p.waitForTimeout(200); await hoverAll();
await p.click('aside [data-go=admin]'); await p.waitForTimeout(200); await p.click('aside [data-go=ttess]'); await p.waitForTimeout(200);
await p.click('aside [data-go=overview]'); await p.waitForTimeout(200);
await p.evaluate(()=>openStudent(Object.keys(DB.students).find(k=>/Zed/.test(DB.students[k].name)))); await p.waitForTimeout(300); await hoverAll();
const fired = await p.evaluate(()=>window.__pw); if (fired.length) errs.push('XSS ran: '+fired.join(',')); console.log('XSS fired:', JSON.stringify(await p.evaluate(()=>window.__pw)), '| tooltips hovered', hovered, '| tip sample:', (await p.evaluate(()=>document.getElementById('tip').innerHTML)).slice(0,120));
// '/' ignored with conference open
await p.keyboard.press('/'); console.log('slash with layer open → focus:', await p.evaluate(()=>document.activeElement.id||document.activeElement.tagName));
await p.keyboard.press('Escape'); await p.waitForTimeout(100);
// back button to start page
await p.goto(FILE_URL+''); await p.waitForTimeout(200); await p.click('aside [data-go=retests]'); await p.waitForTimeout(150); await p.goBack(); await p.waitForTimeout(250); console.log('after Back: view =', await p.evaluate(()=>UI.view));
await p.goto(FILE_URL+'#bogus'); await p.waitForTimeout(250); console.log('unknown view →', await p.evaluate(()=>UI.view), await p.locator('aside [aria-current=page]').count());
// backdrop drag doesn't close
await p.click('aside [data-go=options]'); await p.waitForTimeout(150); await p.click('[data-act=backup]'); await p.waitForTimeout(400);
const box = await p.locator('#outText').boundingBox(); await p.mouse.move(box.x+10, box.y+10); await p.mouse.down(); await p.mouse.move(5, 5); await p.mouse.up(); await p.waitForTimeout(100);
const open1 = !!(await p.$('#outText')); if (!open1) errs.push('dialog closed on drag-out'); console.log('dialog open after drag-out:', open1);
await p.mouse.click(5, 300); await p.waitForTimeout(100); console.log('dialog open after backdrop click:', !!(await p.$('#outText')));
console.log('ERR', errs); await b.close();})();
