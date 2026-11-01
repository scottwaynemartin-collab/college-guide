const {FILE_URL, HTML_PATH, OUT, FIX} = require('./lib');
const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();
for (const w of [1440,1280,1150,1024,900,390]){
 const p=await b.newPage({viewport:{width:w,height:1000}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto(FILE_URL+'');await p.click('text=Try it with sample data');await p.waitForTimeout(300);
 const r = await p.evaluate(()=>{ const ro=document.querySelector('#rosterCard').getBoundingClientRect(), sd=document.querySelector('.ovside').getBoundingClientRect();
   const rows=[...document.querySelectorAll('.rrow')]; let clipped=0, overflow=0; rows.forEach(rw=>{ if (rw.scrollWidth>rw.clientWidth+1) overflow++; const last=rw.lastElementChild.getBoundingClientRect(); if (last.right>ro.right+1) clipped++; rw.querySelectorAll('.tag,.flag').forEach(t=>{ const tr=t.getBoundingClientRect(); if (tr.right>ro.right+1) clipped++; }); });
   return {rosterW:Math.round(ro.width), sideW:Math.round(sd.width), sideLeft:Math.round(sd.left), rosterRight:Math.round(ro.right), stacked: sd.top>ro.bottom-5, overlap: sd.left<ro.right-1 && !(sd.top>ro.bottom-5), overflow, clipped, rows:rows.length}; });
 console.log(w, JSON.stringify(r), errs.length?errs:'');
 if (w===1440||w===1024) await p.screenshot({path:OUT+`/lay-${w}.png`, clip:{x:0,y:w===1440?560:620,width:w,height:700}});
 await p.close();
}
await b.close();})();
