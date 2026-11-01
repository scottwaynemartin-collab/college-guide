const {FILE_URL, HTML_PATH, OUT, FIX} = require('./lib');
const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1440,height:1000}});
const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('dialog',d=>{errs.push('DIALOG');d.dismiss();});
await p.addInitScript(()=>{
  const d=new Date(); d.setHours(12); do { d.setDate(d.getDate()+1);} while(d.getDay()!==2);
  const day=d.toLocaleDateString('en-US',{weekday:'short',month:'short',day:'numeric'});
  const tabs={'A-D Swenson':[['ID Number','LAST NAME','FIRST NAME','E','G1','G2','Wed, X',day]],'E-K Morgan':[['ID Number','L','F','E','G1','G2',day]],'L-Rh Frederick':[['ID Number','L','F','E','G1','G2',day]],'Ri-Z Istre':[['ID Number','L','F','E','G1','G2',day]]};
  const t=Object.keys(tabs); for(let i=0;i<52;i++){ const tab=tabs[t[i%4]], row=Array(tab[0].length).fill(''); row[0]=String(410200+i); if(i%7===0) row[tab[0].length-1]='Smith, Jo B200 A Block'; tab.push(row); }
  window.__writes=[];
  const L=s=>{let n=0;for(const c of s)n=n*26+c.charCodeAt(0)-64;return n-1;};
  window.claude={use:async n=> n==='mcp'?{callTool:async(srv,tool,inp)=>{ const m=inp.range.match(/^'(.+)'!(.+)$/), tab=tabs[m[1]], r=m[2];
    if(tool==='update_values'){ const mm=r.match(/^([A-Z]+)(\d+)$/); tab[+mm[2]-1][L(mm[1])]=inp.values[0][0]; window.__writes.push(inp.range+'='+inp.values[0][0]); return {payload:{updatedCells:1}}; }
    if(r==='1:1') return {payload:{values:[tab[0]]}};
    const c=L(r.split(':')[0]); return {payload:JSON.stringify({values:tab.map(row=>[row[c]])})}; }}:null};
});
await p.goto(FILE_URL+'');await p.click('text=Try it with sample data');await p.waitForTimeout(300);
await p.click('aside [data-go=power]');await p.waitForTimeout(300);
await p.click('[data-act=draft-check]');await p.waitForTimeout(800);
console.log(await p.$$eval('.dprev .dstat',x=>x.map(e=>e.textContent).join(', ')));
await p.screenshot({path:OUT+'/draft.png',fullPage:false});
await p.click('[data-act=draft-write]');await p.waitForTimeout(200);await p.waitForTimeout(800);
console.log(await p.evaluate(()=>window.__writes));
console.log(await p.$$eval('.dprev .dstat',x=>x.map(e=>e.textContent).join(', ')));
console.log('ERR',errs);await b.close();})();
