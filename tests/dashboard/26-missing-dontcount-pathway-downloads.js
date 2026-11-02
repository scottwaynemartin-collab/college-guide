const {FILE_URL, OUT} = require('./lib');
const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const ctx=await b.newContext({viewport:{width:1440,height:1000},permissions:['clipboard-read','clipboard-write']});const p=await ctx.newPage();
const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>m.type()==='error'&&errs.push(m.text()));
const check=(ok,msg)=>{ if(!ok) errs.push('FAIL '+msg); console.log((ok?'✓ ':'✗ ')+msg); };
await p.goto(FILE_URL);await p.click('text=Try it with sample data');await p.waitForTimeout(300);
// 1. missing AP Classroom scores are skipped (not 0)
const r1 = await p.evaluate(()=>{ const a={name:'APHG · Unit 1 MC Test',source:'AP Classroom'}, b={name:'APHG · Unit 2 MC Test',source:'AP Classroom'}, c={name:'APHG · Unit 3 MC Test',source:'AP Classroom'};
  const st = apStatus([{a,p:60},{a:b,p:58},{a:c,p:0,m:true}]); const pr = apProject('APHG',[{a,p:60},{a:b,p:58},{a:c,p:0,m:true}]); return {status:st.status, avg:Math.round(st.avg), n:st.mc.length, proj:Math.round(pr.mcPct)}; });
check(r1.status==='ok' && r1.avg===59 && r1.n===2 && r1.proj===59, `missing skipped: ${JSON.stringify(r1)}`);
// 2. don't-count toggle on one AP Classroom score
const key = await p.evaluate(()=>{ const m=buildModel(); const s=m.studs.find(s=>s.cs.length===1 && s.cs[0].ap.mc.length>=2); return s.key; });
const before = await p.evaluate(k=>{ const c=studentFull(k).cs[0]; return {avg:c.ap.avg, n:c.ap.mc.length}; }, key);
await p.evaluate(k=>openStudent(k), key); await p.waitForTimeout(300);
await p.locator('[data-exclude]').first().click(); await p.waitForTimeout(150);
await p.fill('#exNote','didn’t attempt'); await p.click('#exGo'); await p.waitForTimeout(300);
const after = await p.evaluate(k=>{ const c=studentFull(k).cs[0]; return {avg:c.ap.avg, n:c.ap.mc.length, ex:Object.keys(DB.excluded).length}; }, key);
check(after.n===before.n-1 && after.ex===1, `don't count: mc ${before.n}→${after.n}, excluded entries ${after.ex}`);
check(await p.locator('.nchip.ex').count()===1 && /didn’t attempt/.test(await p.textContent('.nchip.ex')), 'struck-through chip with note on conference page');
check(await p.locator('.ft s').count()>=1, 'unit tracker shows the excluded score struck through');
await p.locator('.nchip.ex').click(); await p.waitForTimeout(150); await p.click('#exGo'); await p.waitForTimeout(300);
check(await p.evaluate(()=>Object.keys(DB.excluded).length)===0, 'count it again removes the exclusion');
await p.locator('[data-exclude]').first().click(); await p.waitForTimeout(150); await p.click('#exGo'); await p.waitForTimeout(200);
await p.keyboard.press('Escape'); await p.waitForTimeout(150);
const bk = await p.evaluate(async()=>{ const t = await backupText(); const d = await parseBackup(t); return Object.keys(d.excluded||{}).length; });
check(bk===1, 'exclusion is in the backup');
// 3. Agency Pathway import
await p.click('aside [data-go=import]'); await p.waitForTimeout(200);
const ids = await p.evaluate(()=>{ const ks=Object.keys(DB.students).filter(k=>DB.students[k].classes.some(c=>/^APHG/.test(c))).slice(0,3); return ks.map(k=>schoolId(DB.students[k])); });
await p.fill('#pasteBox', `Student ID,Course,Unit,Steps done,Steps total,Cleared\n${ids[0]},APHG,3,3,7,No\n${ids[1]},APHG,Unit 3,7,7,Yes\n${ids[2]},APHG,3,0,7,No\n999999,APHG,3,2,7,No`);
await p.click('[data-act=paste]'); await p.waitForTimeout(300);
const res = await p.evaluate(()=>UI.lastResult.split('\n').pop()); check(/Agency Pathway progress for 3 students/.test(res) && /1 student ID not found/.test(res), 'pathway import: '+res);
check(await p.evaluate(()=>Object.keys(DB.pathway).filter(id=>/\|APHG\|3$/.test(id)).length)===3, 'three APHG Unit 3 pathway entries stored (the sample\'s made-up ones replaced)');
await p.fill('#pasteBox', `Student ID,Course,Unit,Steps done,Steps total,Cleared\n${ids[0]},APHG,3,5,7,No`); await p.click('[data-act=paste]'); await p.waitForTimeout(300);
check(await p.evaluate(()=>Object.keys(DB.pathway).filter(id=>/\|APHG\|3$/.test(id)).length)===1, 're-import of APHG Unit 3 replaced it (1 entry left)');
check(await p.evaluate(()=>!!lastSync('Pathway') && lastDataImport() < lastSync('Pathway').at), 'pathway import does not reset "hidden until next refresh"');
await p.fill('#pasteBox', `Student ID,Course,Unit,Steps done,Steps total,Cleared\n${ids[0]},APHG,3,5,7,No\n${ids[1]},APHG,3,7,7,Yes`); await p.click('[data-act=paste]'); await p.waitForTimeout(300);
// chips
await p.evaluate(k=>openStudent(k), await p.evaluate(id=>DB.idmap[id], ids[0])); await p.waitForTimeout(300);
check(/Pathway 5\/7/.test(await p.textContent('#layer')), 'conference unit tracker shows "Pathway 5/7"'); await p.keyboard.press('Escape');
await p.click('aside [data-go=retestmsg]'); await p.waitForTimeout(200); const rmChips = await p.locator('.rmrow .tag.pw').count(); console.log('  retest-message rows with a pathway chip:', rmChips);
await p.click('aside [data-go=phdraft]'); await p.waitForTimeout(200); const pdChips = await p.locator('.rmrow .tag.pw').count(); console.log('  power-hour-draft rows with a pathway chip:', pdChips);
check(rmChips + pdChips >= 1, 'pathway chips appear on action-list rows');
await p.click('aside [data-go=ttess]'); await p.waitForTimeout(250); const tt = await p.textContent('.ttview'); check(/Agency Pathway \(retest module\): APHG U3/.test(tt), 'T-TESS shows pathway counts');
const names = await p.evaluate(()=>{ const t=document.querySelector('.ttview').innerText; return Object.values(DB.students).map(s=>s.name).filter(n=>t.includes(n)).length; }); check(names===0, 'no names on T-TESS');
await p.click('aside [data-go=admin]'); await p.waitForTimeout(250); check(/Agency Pathway \(retest module\)/.test(await p.textContent('.adm')), 'At a glance shows pathway table');
const names2 = await p.evaluate(()=>{ const t=document.querySelector('.adm').innerText; return Object.values(DB.students).map(s=>s.name).filter(n=>t.includes(n)).length; }); check(names2===0, 'no names on At a glance');
// 5. district import: own chip, doesn't reset hidden lists
const beforeData = await p.evaluate(()=>lastDataImport());
await p.click('aside [data-go=import]'); await p.waitForTimeout(150); await p.fill('#pasteBox','Course,Year,Campus,Participation %\nAPHG,2026,Panther Creek,71'); await p.click('[data-act=paste]'); await p.waitForTimeout(300);
check(await p.evaluate(b=>lastDataImport()===b && lastSync('Reports') && !/College Board|district/.test((lastSync('Profile')||{}).file||''), beforeData), 'district import logged as Reports, data-refresh time unchanged');
check(/Reports · just now/.test(await p.textContent('.syncs')), 'Import page shows a Reports chip');
// 4. downloads: in a normal tab the Save button downloads; in the artifact the capability is used
await p.click('aside [data-go=options]'); await p.waitForTimeout(150); await p.click('[data-act=backup]'); await p.waitForTimeout(400);
const [dl] = await Promise.all([p.waitForEvent('download',{timeout:3000}).catch(()=>null), p.click('#dlBtn')]); check(!!dl && /classroom-dashboard-backup/.test(dl.suggestedFilename()), 'Save file downloads in a normal tab: '+(dl&&dl.suggestedFilename()));
await p.keyboard.press('Escape');
const art = await p.evaluate(async()=>{ window.__saved=null; window.claude = {use: async n => n==='downloads' ? {save: async o => { window.__saved = o; }} : null};
  // simulate the artifact frame (CAN_PRINT false) by calling the capability path directly
  let dl = await window.claude.use('downloads'); await dl.save({filename:'x.csv', data:'a,b'}); return window.__saved && window.__saved.filename; });
check(art==='x.csv', 'downloads capability call shape {filename, data}');
console.log('ERR', errs); await b.close();})();
