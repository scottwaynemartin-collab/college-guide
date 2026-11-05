const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
(async()=>{const b=await chromium.launch({executablePath:'/usr/bin/google-chrome'});
const out={};
for(const f of process.argv.slice(2)){
 const p=await b.newPage({viewport:{width:1280,height:800}});
 p.on('pageerror',e=>console.log('ERR',f,e.message.slice(0,100)));
 await p.goto('file://'+path.resolve(f),{waitUntil:'load'});await p.waitForTimeout(2500);
 const rules=await p.evaluate(()=>{const R=[];const props=['background','background-color','background-image','color','border','border-color','border-top','border-bottom','border-left','border-right','box-shadow','fill','stroke','outline','text-shadow','-webkit-text-fill-color'];
  function walk(list,media){for(const r of list){if(r.cssRules&&r.type!==1){walk(r.cssRules,(media||'')+(r.conditionText?'@'+r.conditionText:''));continue}
   if(r.type!==1)continue;const st=r.style;const d={};for(const k of props){const v=st.getPropertyValue(k);if(v)d[k]=v+(st.getPropertyPriority(k)?' !important':'')}
   // also custom props
   for(let i=0;i<st.length;i++){const k=st[i];if(k.startsWith('--'))d[k]=st.getPropertyValue(k)}
   if(Object.keys(d).length)R.push({sel:r.selectorText,media:media||'',d})}}
  for(const s of document.styleSheets){try{walk(s.cssRules,'')}catch(e){}}return R});
 out[f]=rules;console.log(f,rules.length);await p.close()}
fs.writeFileSync('cssrules.json',JSON.stringify(out));await b.close()})();
