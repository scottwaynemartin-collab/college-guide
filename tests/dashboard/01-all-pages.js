const {FILE_URL, HTML_PATH, OUT, FIX} = require('./lib');
const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();
for (const [w,h] of [[1440,1000],[390,844]]){
 const p=await b.newPage({viewport:{width:w,height:h}});
 const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>m.type()==='error'&&errs.push(m.text()));
 p.on('dialog',d=>{errs.push('DIALOG '+d.type());d.dismiss();});
 p.on('request',r=>{const u=r.url(); if(!/^(file|data|blob|about):/.test(u)) errs.push('NET '+u);});
 await p.goto(FILE_URL+'');await p.waitForTimeout(300);
 await p.screenshot({path:OUT+`/${w}-welcome.png`});
 await p.click('text=Try it with sample data');await p.waitForTimeout(300);
 await p.screenshot({path:OUT+`/${w}-overview.png`,fullPage:true});
 const go=async v=>{ if(w<800){ await p.click('[data-act=menu]'); await p.waitForTimeout(250);} await p.click(`aside [data-go=${v}]`); await p.waitForTimeout(250); };
 for (const v of ['retests','power','missing','compare','ap','assignments','import','options']){ await go(v); await p.screenshot({path:OUT+`/${w}-${v}.png`,fullPage:true}); }
 await go('compare'); await p.click('[data-course="APHG"]'); await p.selectOption('#cmpStu',{index:3}); await p.waitForTimeout(200); await p.screenshot({path:OUT+`/${w}-compare-aphg.png`,fullPage:true});
 await go('overview'); await p.click('[data-status="help"]'); await p.waitForTimeout(150);
 await p.click('.rrow'); await p.waitForTimeout(250); await p.screenshot({path:OUT+`/${w}-drawer.png`});
 await p.keyboard.press('Escape');
 await go('options'); await p.click('[data-act=wipe]'); await p.waitForTimeout(150); await p.screenshot({path:OUT+`/${w}-confirm.png`}); await p.click('#layer [data-close].btn:not(.x)');
 await p.click('[data-act=backup]'); await p.waitForTimeout(150); const bl=await p.evaluate(()=>document.querySelector('#outText').value.length); await p.keyboard.press('Escape');
 console.log(w,'backup chars',bl,'ERR',errs);
 await p.close();}
await b.close();})();
