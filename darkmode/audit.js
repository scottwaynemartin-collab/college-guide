// Render each test page in dark mode, screenshot, and list elements that are still light (bg luminance > .6)
// or have unreadable text (contrast < 3). Usage: node audit.js [--shots] test/a.html test/b.html ...
const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
const files=process.argv.slice(2).filter(a=>!a.startsWith('--'));const shots=process.argv.includes('--shots');const light=process.argv.includes('--light');
fs.mkdirSync('shots',{recursive:true});
(async()=>{const b=await chromium.launch({executablePath:'/usr/bin/google-chrome'});
const report={};
for(const f of files){
 const slug=path.basename(f,'.html');
 for(const [w,h,tag] of [[1280,800,'desk'],[390,780,'phone']]){
  const ctx=await b.newContext({viewport:{width:w,height:h},colorScheme:light?'light':'dark'});const p=await ctx.newPage();
  const errs=[];p.on('pageerror',e=>errs.push(e.message.slice(0,120)));
  await p.goto('file://'+path.resolve(f),{waitUntil:'load'});await p.waitForTimeout(2500);
  const res=await p.evaluate(()=>{
   function lum([r,g,b]){const f=v=>{v/=255;return v<=.03928?v/12.92:((v+.055)/1.055)**2.4};return .2126*f(r)+.7152*f(g)+.0722*f(b)}
   function rgb(s){const m=s&&s.match(/rgba?\(([^)]+)\)/);if(!m)return null;const p=m[1].split(',').map(parseFloat);if(p.length>3&&p[3]===0)return null;return p.slice(0,3)}
   function eff(el){let e=el;while(e){const c=rgb(getComputedStyle(e).backgroundColor);if(c)return c;e=e.parentElement}return [255,255,255]}
   const lightEls={},contrast=[];let n=0;
   for(const el of document.querySelectorAll('body *')){
    const cs=getComputedStyle(el);if(cs.display==='none'||cs.visibility==='hidden')continue;
    const r=el.getBoundingClientRect();if(r.width<24||r.height<12)continue;if(r.bottom<0||r.top>document.documentElement.scrollHeight)continue;
    const bg=rgb(cs.backgroundColor);const bgi=cs.backgroundImage;
    if((bg&&lum(bg)>.6)||(bgi&&bgi!=='none'&&/gradient/.test(bgi)&&/rgb\(2[3-5]\d, ?2[3-5]\d, ?2[3-5]\d\)/.test(bgi))){
      if(el.closest('.dm-tg'))continue;
      const k=(el.tagName.toLowerCase()+(el.className&&typeof el.className==='string'?'.'+el.className.trim().split(/\s+/).slice(0,3).join('.'):''));
      lightEls[k]=(lightEls[k]||0)+1;n++;
    }
    // text contrast: only elements with direct text
    const txt=[...el.childNodes].some(x=>x.nodeType===3&&x.textContent.trim().length>2);
    if(txt){const fg=rgb(cs.color);if(fg){const B=eff(el);const l1=lum(fg),l2=lum(B);const c=(Math.max(l1,l2)+.05)/(Math.min(l1,l2)+.05);
      if(c<3){const k=(el.tagName.toLowerCase()+(el.className&&typeof el.className==='string'?'.'+el.className.trim().split(/\s+/).slice(0,3).join('.'):''));contrast.push([k,c.toFixed(2),cs.color,'on',`rgb(${B.join(',')})`,el.textContent.trim().slice(0,30)])}}}
   }
   const dedup={};for(const c of contrast){dedup[c[0]]=dedup[c[0]]||c}
   return {dark:document.documentElement.classList.contains('dm'),lightCount:n,lightEls,contrast:Object.values(dedup).slice(0,40),toggle:!!document.querySelector('.dm-tg'),bodyBg:getComputedStyle(document.body).backgroundColor,htmlBg:getComputedStyle(document.documentElement).backgroundColor,h:document.documentElement.scrollHeight}});
  res.errors=errs;
  report[slug+':'+tag]=res;
  if(shots)await p.screenshot({path:`shots/${slug}--${tag}${light?'-light':''}.png`,fullPage:false});
  await ctx.close();
 }}
fs.writeFileSync(`audit${light?'-light':''}.json`,JSON.stringify(report,null,1));
for(const [k,v] of Object.entries(report)){console.log(`${k.padEnd(70)} dm=${v.dark} toggle=${v.toggle} light=${v.lightCount} lowContrast=${v.contrast.length} err=${v.errors.length} body=${v.bodyBg}`)}
await b.close()})();
