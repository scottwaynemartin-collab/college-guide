const {FILE_URL, HTML_PATH, OUT, FIX} = require('./lib');
const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:390,height:844}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto(FILE_URL+'');await p.waitForTimeout(200);
console.log('welcome header:', (await p.textContent('#top b')).trim());
await p.click('[data-act=menu]');await p.click('aside [data-go=options]');await p.waitForTimeout(200);console.log('settings header:', (await p.textContent('#top b')).trim());
await p.click('[data-act=menu]');await p.click('aside [data-go=import]');await p.waitForTimeout(200);console.log('import header:', (await p.textContent('#top b')).trim());
console.log('ERR',errs);await b.close();})();
