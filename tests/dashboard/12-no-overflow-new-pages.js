const {FILE_URL, HTML_PATH, OUT, FIX} = require('./lib');
const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();
for (const w of [1440,900,390]){
 const p=await b.newPage({viewport:{width:w,height:1000}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto(FILE_URL+'');await p.click('text=Try it with sample data');await p.waitForTimeout(300);
 await p.evaluate(()=>{ DB.cb.district=[{course:'APHG',year:'2026',campus:'Panther Creek',pct:71},{course:'APHG',year:'2026',campus:'A Very Long Campus Name High School',pct:58},{course:'AP World',year:'2026',campus:'Panther Creek',pct:66},{course:'AP World',year:'2026',campus:'Heritage',pct:55}]; save(); });
 const measure = async (label) => { const r = await p.evaluate(()=>{ const root=document.querySelector('#view'); const cards=[...root.querySelectorAll('.card,.dchart,.strip,.stat,table')]; let over=[]; cards.forEach(c=>{ if (c.scrollWidth>c.clientWidth+1) over.push((c.className||c.tagName).toString().slice(0,20)); });
   return {docOver: document.documentElement.scrollWidth > document.documentElement.clientWidth+1, over: over.slice(0,5)}; }); console.log(w, label, JSON.stringify(r)); };
 const go=async v=>{ if(w<=820){ await p.click('[data-act=menu]'); await p.waitForTimeout(250);} await p.click(`aside [data-go=${v}]`); await p.waitForTimeout(300); };
 for (const v of ['admin','phdraft','help','ttess','retestmsg']){ await go(v); await measure(v); if (w===390 && v==='admin') await p.screenshot({path:OUT+'/admin-390.png', fullPage:true}); }
 if (errs.length) console.log('ERR', errs); await p.close();
}
await b.close();})();
