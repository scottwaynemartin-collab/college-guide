const {FILE_URL, OUT} = require('./lib');
const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const ctx=await b.newContext({viewport:{width:1440,height:1000},permissions:['clipboard-read','clipboard-write']});const p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto(FILE_URL+'');await p.click('text=Try it with sample data');await p.waitForTimeout(300);
// T-TESS distinct students
await p.click('aside [data-go=ttess]'); await p.waitForTimeout(250);
console.log('TT intro:', (await p.textContent('.ttview .phead p')).match(/\(\d+ students\)/)[0], '| distinct', await p.evaluate(()=>Object.values(DB.students).filter(s=>s.classes.length).length));
// filter label ignores STAAR chip
await p.evaluate(()=>{ UI.staar='masters'; render(); }); console.log('TT eyebrow with STAAR filter:', (await p.textContent('.ttview .eyebrow')).trim().slice(0,40)); await p.evaluate(()=>{ UI.staar='all'; render(); });
// groups for two periods same day
await p.evaluate(()=>{ UI.view='overview'; UI.course='APHG'; UI.period='APHG 3B'; render(); }); await p.click('[data-act=make-groups]'); await p.waitForTimeout(150); await p.click('[data-act=groups-copy]'); await p.keyboard.press('Escape');
await p.evaluate(()=>{ UI.period='APHG 4A'; render(); }); await p.click('[data-act=make-groups]'); await p.waitForTimeout(150); await p.click('[data-act=groups-copy]'); await p.keyboard.press('Escape');
console.log('groups logged by class:', JSON.stringify(await p.evaluate(()=>{ const o={}; DB.groups.forEach(g=>g.classes.forEach(c=>o[c]=(o[c]||0)+1)); return o; })));
await p.evaluate(()=>{ UI.course='all'; UI.period='all'; render(); });
// outcomes: a PH draft contact counts as Power Hour
const oc = await p.evaluate(()=>{ const k=Object.keys(DB.students).find(k=>DB.students[k].classes.length && !(DB.drafts[k]||[]).length); const mid = Math.min(...Object.values(DB.assignments).filter(a=>a.at).map(a=>a.at)) + 40*864e5; (DB.contacts[k] ||= []).push({type:'PH draft — Unit 2 test 61', note:'', at: mid}, {type:'Retest message · Unit 2 · Canvas', note:'APHG', at: mid}); save(); const ev = outcomes(buildModel()).filter(e=>e.s.key===k); return ev.map(e=>e.type+':'+e.label).join(' | '); });
console.log('outcomes for that student:', oc);
// parsePartLines
console.log('parsePartLines:', JSON.stringify(await p.evaluate(()=>parsePartLines('Social studies: 1,210 of 1,385\nPanther Creek: approx. 58%\nFrisco ISD - all campuses: 63%\nbad line'))));
// stale phNow no longer excludes
console.log('phNowActive:', await p.evaluate(()=>[phNowActive('Mon, Oct 5 · A Block'), phNowActive('Tue, Nov 3 · A Block'), phNowActive('Fri, Jun 4'), phNowActive('A Block'), phNowActive('')].join(',')));
// drafts: missing latest test listed
const miss = await p.evaluate(()=>{ const k=Object.keys(DB.students).find(k=>DB.students[k].classes[0]==='APHG 3B'); const a=Object.values(DB.assignments).filter(a=>a.source==='Gradebook'&&/Unit 3 Test$/.test(a.name)&&/^APHG/.test(a.name)&&yearOf(a)===curYear())[0]; DB.scores[k][a.id]={p:0,m:true}; if (DB.profiles[k]) delete DB.profiles[k].phNow; save(); return phDraftRows(buildModel(),'test').filter(r=>r.s.key===k).map(r=>r.why).join(','); });
console.log('drafts list for student with missing Unit 3 test:', miss);
// labels from settings
await p.click('aside [data-go=phdraft]'); await p.waitForTimeout(200); console.log('PD tabs:', (await p.textContent('.tabs')).replace(/\s+/g,' '));
// school ID used in prompt even if a Canvas id came first
await p.evaluate(()=>{ Object.values(DB.students).forEach(s=>{ if (s.ids.length) s.ids.unshift('11'); }); save(); render(); });
await p.click('[data-act=pd-prompt]'); await p.waitForTimeout(150); const pr = await p.evaluate(()=>navigator.clipboard.readText()); console.log('prompt first student line:', pr.split('\n').find(l=>/^1\. /.test(l)));
// threshold consistency: 69.6 class avg
const th = await p.evaluate(()=>{ const m=buildModel(); const s=m.studs.find(s=>s.cs.some(c=>c.avg!=null)); const c=s.cs[0]; c.avg=69.6; return [below(69.6,70), below(69.4,70), powerHour({studs:[s]}).length, phDraftRows({studs:[s]},'c70').length].join(','); });
console.log('69.6 vs 70 → below?, 69.4?, power hour list, drafts c70:', th);
// week span
console.log('TT weekly line:', await p.evaluate(()=>{ UI.view='ttess'; render(); return [...document.querySelectorAll('.ttview li')].map(l=>l.textContent).find(t=>/Weekly data refreshes/.test(t)); }));
// default draft day honours the 6 pm deadline (Mon 7:30 pm → not Tuesday)
await p.clock.install({time: new Date('2026-11-02T19:30:00')}); await p.reload(); await p.waitForTimeout(300);
console.log('Mon 7:30 pm default day:', await p.evaluate(()=>defaultDraftDay()), '| Mon 9 am:', await p.evaluate(()=>{ return 'n/a'; }));
await p.clock.setFixedTime(new Date('2026-11-02T09:00:00')); console.log('Mon 9:00 am default day:', await p.evaluate(()=>defaultDraftDay()));
console.log('ERR', errs); await b.close();})();
