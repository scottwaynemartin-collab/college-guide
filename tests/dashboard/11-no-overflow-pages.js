const {FILE_URL, HTML_PATH, OUT, FIX} = require('./lib');
const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();
for (const w of [1440,1280,1150,1024,900,390]){
 const p=await b.newPage({viewport:{width:w,height:1000}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto(FILE_URL+'');await p.click('text=Try it with sample data');await p.waitForTimeout(300);
 const measure = async (label) => { const r = await p.evaluate(()=>{ const root=document.querySelector('#layer .conf')||document.querySelector('#view'); const cards=[...root.querySelectorAll('.card,.fsec,.rcard,.ph')]; let over=0, cardOverflow=[]; cards.forEach(c=>{ if (c.scrollWidth>c.clientWidth+1){ over++; cardOverflow.push((c.querySelector('h2,h3')?.textContent||c.className).trim().slice(0,30)); } });
   const docOver = Math.max(root.scrollWidth, document.documentElement.scrollWidth) > document.documentElement.clientWidth+1;
   const rects=cards.map(c=>c.getBoundingClientRect()); let overlaps=0; for (let i=0;i<rects.length;i++) for (let j=i+1;j<rects.length;j++){ const a=rects[i],b=rects[j]; if (cards[i].contains(cards[j])||cards[j].contains(cards[i])) continue; if (a.left<b.right-1&&b.left<a.right-1&&a.top<b.bottom-1&&b.top<a.bottom-1) overlaps++; }
   return {cards:cards.length, over, cardOverflow:cardOverflow.slice(0,4), docOver, overlaps}; }); console.log(w, label, JSON.stringify(r)); };
 const go=async v=>{ if(w<=820){ await p.click('[data-act=menu]'); await p.waitForTimeout(250);} await p.click(`aside [data-go=${v}]`); await p.waitForTimeout(250); };
 await measure('overview');
 await go('retests'); await measure('retests');
 await p.click('[data-retestby=test]'); await p.waitForTimeout(200); await measure('retests-bytest');
 await go('retestmsg'); await measure('retestmsg');
 await p.evaluate(()=>openStudent(Object.keys(DB.students).find(k=>DB.students[k].classes.length>1))); await p.waitForTimeout(300); await measure('conference');
 await p.keyboard.press('Escape');
 if (errs.length) console.log('ERR', errs);
 await p.close();
}
await b.close();})();
