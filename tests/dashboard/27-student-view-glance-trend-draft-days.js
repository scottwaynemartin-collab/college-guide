// Student view (privacy, bands, print), At a glance class averages + trend, Power Hour draft days, Overview freshness chips.
// Made-up sample data only.
const {FILE_URL, OUT} = require('./lib');
const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const ctx=await b.newContext({viewport:{width:1440,height:1000},permissions:['clipboard-read','clipboard-write']});const p=await ctx.newPage();
const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>m.type()==='error'&&errs.push(m.text()));
const check=(ok,msg)=>{ if(!ok) errs.push('FAIL '+msg); console.log((ok?'✓ ':'✗ ')+msg); };
await p.goto(FILE_URL);await p.click('text=Try it with sample data');await p.waitForTimeout(300);

// ---------- 1. Student view ----------
// privacy helpers
const h = await p.evaluate(()=>({a:svShare(2,20), b:svShare(18,20), c:svShare(10,20), d:svShare(1,2), e:svCount(2), f:svCount(5), g:svAvg([90,80]), bands:svBands([95,92,91,85,72]).label('70'), blur:svBands([95,92,91,85,84,83,72]).blur, nb:svN(27,true)}));
check(h.a==='fewer than 3' && h.b==='all but fewer than 3' && h.c==='50%' && h.d===null && h.e==='fewer than 3' && h.f==='5' && h.g===null, 'small groups never show a number: '+JSON.stringify(h));
check(h.bands==='fewer than 3' && h.blur===true && h.nb==='≈25', 'a 1-student band reads "fewer than 3" and the rest are rounded so it can\'t be subtracted out');
await p.click('aside [data-go=student]'); await p.waitForTimeout(300);
check((await p.textContent('#top b')).trim()==='Student view' && await p.locator('#q').count()===0, 'top bar: "Student view", no search box');
const priv = await p.evaluate(()=>{ const t=document.body.innerText, ids=Object.values(DB.students).flatMap(s=>s.ids); return {names:Object.values(DB.students).map(s=>s.name).filter(n=>t.includes(n)).length, ids:ids.filter(i=>t.includes(i)).length, tips:document.querySelectorAll('#view [data-tip]').length, links:document.querySelectorAll('#view [data-student],#view [data-report],#view a').length}; });
console.log('names leaked', priv.names); check(priv.ids===0 && priv.tips===0 && priv.links===0, `no IDs, tooltips or student links on the page: ${JSON.stringify(priv)}`);
check(await p.locator('.svstrip .svstat').count()===4, 'top strip has 4 numbers');
const strip = (await p.textContent('.svstrip')).replace(/\s+/g,' '); check(/Class average/.test(strip) && /Unit MC average · raw/.test(strip) && /Unit MC average · scaled/.test(strip) && /On pace for a 3/.test(strip), 'strip: '+strip.slice(0,160));
check(await p.locator('.svsec').nth(0).locator('.svcard').count()===3, 'APHG: one card per unit (3)');
check(await p.locator('.svsec').nth(1).locator('.svcard').count()>=2 && /\/7/.test(await p.textContent('.svsec >> nth=1')), 'writing cards with a rubric average (x/7)');
check(await p.locator('.dbar').count()>=5 && await p.locator('.dbar .med').count()>=5, 'distribution bars with the median marked');
check(await p.locator('.lchart').count()===2, 'trend: two line charts');
const ag = (await p.textContent('.svag')).replace(/\s+/g,' '); check(/Cleared the Agency Pathway/.test(ag) && /Retests completed/.test(ag) && /Average retest gain/.test(ag), 'agency counts: '+ag.slice(0,140));
const takes = await p.locator('.svtake').allTextContents(); check(takes.length===5, `one takeaway per section (${takes.length})`); console.log('  e.g.', takes[1]);
// "first attempt only": the unit raw average ignores retests
const firstOnly = await p.evaluate(()=>{ const d=svData('APHG','all'), u1=d.unitCards[0]; let rt=0; const m=scopedModel('APHG','all'); m.studs.forEach(s=>s.cs.forEach(c=>c.pts.forEach(x=>{ if(isUnitMC(x.a)&&isRetest(x.a)&&unitOf(x.a.name)===1&&!x.m) rt++; }))); return {n:u1.raw.length, rt, students:d.n}; });
check(firstOnly.rt>0 && firstOnly.n<=firstOnly.students, `first attempts only (Unit 1: ${firstOnly.n} first-attempt scores; ${firstOnly.rt} retests left out)`);
// course + period switcher
await p.click('[data-svcourse="AP World"]'); await p.waitForTimeout(200); check(/AP WORLD · ALL PERIODS/i.test(await p.textContent('.svhead h1')), 'course switcher → AP World');
await p.click('[data-svperiod="AP World 1A"]'); await p.waitForTimeout(200); const per = await p.textContent('.svhead h1'); check(/PERIOD 1A/i.test(per), 'period filter → '+per.trim());
const small = await p.evaluate(()=>{ const t=document.querySelector('.sv').innerText; return {few:(t.match(/fewer than 3/g)||[]).length}; }); check(small.few>=1, `small period shows "fewer than 3" (${small.few}×)`);
await p.click('[data-svperiod="all"]'); await p.waitForTimeout(150);
// full screen
await p.click('[data-act=sv-present]'); await p.waitForTimeout(150); check(!(await p.isVisible('aside')) && await p.evaluate(()=>document.body.classList.contains('present')), 'full screen hides the sidebar and top bar');
await p.keyboard.press('/'); await p.keyboard.press('Escape'); await p.waitForTimeout(150); check(await p.isVisible('aside'), 'Esc leaves full screen ("/" does nothing here)');
await p.screenshot({path:OUT+'/student-view.png',fullPage:true});
await p.click('[data-act=theme]'); await p.waitForTimeout(150); await p.screenshot({path:OUT+'/student-view-dark.png',fullPage:true}); await p.click('[data-act=theme]'); await p.waitForTimeout(100);
await p.setViewportSize({width:390,height:900}); await p.waitForTimeout(150); check(await p.evaluate(()=>document.documentElement.scrollWidth)<=390, 'no sideways scroll at phone width'); await p.setViewportSize({width:1440,height:1000});
// print (normal tab) → one page; artifact → printable text with no names
await p.click('[data-svcourse="APHG"]'); await p.waitForTimeout(150);
await p.setViewportSize({width:1000,height:1300}); await p.evaluate(()=>{ window.print=()=>{}; }); await p.click('[data-act=sv-print]'); await p.waitForTimeout(150);
await p.evaluate(()=>document.body.classList.add('printing')); await p.emulateMedia({media:'print'}); await p.pdf({path:OUT+'/student.pdf',format:'Letter',printBackground:true});
await p.emulateMedia({media:'screen'}); await p.evaluate(()=>document.body.classList.remove('printing')); await p.setViewportSize({width:1440,height:1000});
const txt = await p.evaluate(()=>{ const t=svText(svData('APHG','all')); return {t, leak:Object.values(DB.students).some(s=>t.includes(s.name))}; }); check(/UNIT MC TESTS/.test(txt.t) && /AGENCY/.test(txt.t) && !txt.leak, 'printable text version, no names');

// ---------- 2. At a glance ----------
await p.click('aside [data-go=admin]'); await p.waitForTimeout(250);
const th = await p.locator('.adm table').first().locator('th').allTextContents(); check(th.includes('Class avg'), 'course table has a Class avg column: '+th.join('|'));
const avgCells = await p.evaluate(()=>[...document.querySelector('.adm table').querySelectorAll('tbody tr')].map(tr=>tr.children[1].textContent.trim())); check(avgCells.length>=6 && avgCells.every(v=>/^\d+%$/.test(v)), 'class average per course and per period: '+avgCells.join(' '));
check(/Trend over time/.test(await p.textContent('.adm')) && await p.locator('.adm .lchart path').count()===3, 'trend: one line per course');
const tr0 = await p.evaluate(()=>({n:DB.trend.length, days:new Set(DB.trend.map(t=>t.date)).size, keys:Object.keys(DB.trend[DB.trend.length-1]).sort().join(',')}));
check(tr0.days===6 && /avg/.test(tr0.keys) && /help/.test(tr0.keys) && /ok/.test(tr0.keys) && /paid/.test(tr0.keys) && /watch/.test(tr0.keys), 'snapshots {date, course, on-track %, watch, help, paid %, class average}: '+tr0.keys);
await p.click('aside [data-go=import]'); await p.waitForTimeout(150);
const sid = await p.evaluate(()=>schoolId(Object.values(DB.students).find(s=>s.classes.includes('APHG 3B'))));
await p.fill('#pasteBox', `Student,Student ID,Class,Platform,APHG · Unit 4 MC Test\n"Test, Sample",${sid},APHG 3B,AP Classroom,40%`); await p.click('[data-act=paste]'); await p.waitForTimeout(300);
const tr1 = await p.evaluate(d0=>({n:DB.trend.length, today:DB.trend.filter(t=>t.date===isoDay(new Date())).length}), tr0); check(tr1.today===3 && tr1.n===tr0.n, `an import replaces today's snapshot (${tr1.today} courses today, ${tr1.n} total)`);
const n1 = await p.evaluate(()=>{ DB.trend = DB.trend.filter(t=>t.date!==isoDay(new Date())); return DB.trend.length; });
await p.fill('#pasteBox', `Student,Student ID,Class,Platform,APHG · Unit 4 MC Test\n"Test, Sample",${sid},APHG 3B,AP Classroom,45%`); await p.click('[data-act=paste]'); await p.waitForTimeout(300); check(await p.evaluate(()=>DB.trend.length)===n1+3, 'each import day adds one point per course');

// ---------- 3. Power Hour drafts: draft day ----------
await p.click('aside [data-go=phdraft]'); await p.waitForTimeout(250);
const dd = await p.evaluate(()=>{ const v=document.querySelector('#pdDate').value, d=fromISO(v); return {v, dow:d.getDay()}; }); check([2,3].includes(dd.dow), 'draft day defaults to the next Tue/Wed: '+dd.v);
const days = await p.evaluate(()=>{ const out={}; const d=new Date(); d.setHours(12,0,0,0); for(let i=1;i<15;i++){ d.setDate(d.getDate()+1); const k=d.getDay(); if(!out[k]) out[k]=isoDay(d); } return out; });
await p.evaluate(v=>{ const el=document.querySelector('#pdDate'); el.value=v; el.dispatchEvent(new Event('change',{bubbles:true})); }, days[4]); await p.waitForTimeout(200);
check(await p.inputValue('#pdDate')!==days[4] && /duty/.test(await p.textContent('#toast')), 'Thursday is refused');
// group 1 → Wednesday
const firstCls = await p.evaluate(()=>UI.pdRows[0].cls);
await p.click('[data-act=pd-sel][data-on="0"]:not([data-cls])'); await p.waitForTimeout(150);
await p.click(`[data-act=pd-sel][data-on="1"][data-cls="${firstCls}"]`); await p.waitForTimeout(150);
await p.evaluate(v=>{ const el=document.querySelector('#pdDate'); el.value=v; el.dispatchEvent(new Event('change',{bubbles:true})); }, days[3]); await p.waitForTimeout(200);
check(await p.locator('[data-pd]:checked').count()>0 && await p.locator('[data-pd]:not(:checked)').count()>0, 'ticks survive changing the day');
const g1 = await p.locator('[data-pd]:checked').count();
await p.click('[data-act=pd-drafted]'); await p.waitForTimeout(250);
// group 2 → Tuesday
await p.click('[data-act=pd-sel][data-on="1"]:not([data-cls])'); await p.waitForTimeout(150);
await p.evaluate(v=>{ const el=document.querySelector('#pdDate'); el.value=v; el.dispatchEvent(new Event('change',{bubbles:true})); }, days[2]); await p.waitForTimeout(200);
await p.click('[data-act=pd-drafted]'); await p.waitForTimeout(250);
const logged = await p.evaluate(()=>{ const c=Object.values(DB.contacts).flat().filter(x=>/^PH draft/.test(x.type)); const by={}; c.forEach(x=>by[x.day]=(by[x.day]||0)+1); return by; });
console.log('  logged by day', JSON.stringify(logged), 'group 1 lines', g1);
check(logged[days[3]]>0 && logged[days[2]]>0, 'two groups logged for their own days (Wed and Tue)');
check(await p.locator('#pdLog .pdlog').count()===2, 'Logged drafts card shows both days');
// an older entry logged with the wrong day (note only, no stored day) → move the whole group
await p.evaluate(()=>{ const ks=Object.keys(DB.students).filter(k=>DB.students[k].classes.length).slice(-3); ks.forEach(k=>(DB.contacts[k] ||= []).push({type:'PH draft — class grade 65', note:'Tue, Nov 3', at:Date.now()-864e5})); save(); render(); });
const legacyISO = await p.evaluate(()=>draftISO({note:'Tue, Nov 3', at:Date.now()}));
const grp = p.locator('#pdLog .pdlog', {hasText: 'Tue, Nov 3'}); check(await grp.count()===1, 'older entries are grouped by the day in their note: '+legacyISO);
const wed2 = await p.evaluate(()=>isoDay(new Date(fromISO(draftISO({note:'Tue, Nov 3', at:Date.now()})).getTime()+864e5)));
await grp.locator('[data-pdmove]').fill(wed2); await grp.locator('[data-act=pd-move]').click(); await p.waitForTimeout(250);
const moved = await p.evaluate(w=>Object.values(DB.contacts).flat().filter(x=>x.note && /Wed/.test(x.note) && x.day===w && /class grade 65/.test(x.type)).length, wed2);
check(moved===3, `moved 3 drafts from Tue, Nov 3 to ${wed2}`);
// conference contact log: edit one draft's date
const k1 = await p.evaluate(w=>Object.keys(DB.contacts).find(k=>(DB.contacts[k]||[]).some(x=>x.day===w)), wed2);
await p.evaluate(k=>openStudent(k), k1); await p.waitForTimeout(250);
check(/for .*Wed/.test(await p.textContent('#layer .notes')), 'contact log shows the draft day');
await p.locator('[data-editdraft]').first().click(); await p.waitForTimeout(150);
await p.fill('#dlDate', days[2]); await p.click('#dlGo'); await p.waitForTimeout(250);
check(await p.evaluate(([k,d])=>(DB.contacts[k]||[]).some(x=>/^PH draft/.test(x.type) && x.day===d), [k1, days[2]]) && await p.locator('#layer .conf').count()===1, 'edit date in the contact log saves it and returns to the conference page');
await p.keyboard.press('Escape'); await p.waitForTimeout(100);

// ---------- 4. Overview freshness chips ----------
await p.click('aside [data-go=import]'); await p.waitForTimeout(150);
await p.fill('#pasteBox','Course,Year,Campus,Participation %\nAPHG,2026,Panther Creek,71'); await p.click('[data-act=paste]'); await p.waitForTimeout(250);
await p.fill('#pasteBox', `Student ID,Course,Unit,Steps done,Steps total,Cleared\n${sid},APHG,4,2,7,No`); await p.click('[data-act=paste]'); await p.waitForTimeout(250);
await p.click('aside [data-go=overview]'); await p.waitForTimeout(250);
const chips = (await p.textContent('.hero .syncs')).replace(/\s+/g,' '); check(/Profile ·/.test(chips) && /Reports ·/.test(chips) && /Pathway ·/.test(chips), 'Overview header shows Profile, Reports and Pathway chips: '+chips.slice(0,200));
console.log('ERR', errs); await b.close();})();
