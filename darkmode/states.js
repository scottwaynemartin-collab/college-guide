// Deep-state dark-mode QA: drive each tool into its working views, screenshot, and count light elements.
const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
const steps={
 'test/geoarcade__unit-2.html':[
   ['flip','click','.card, .flash, .scene, [data-flip], #card'],
   ['arcade','hash','#arcade'],
   ['arcade-game','click','.game-card button, .game-card, [data-game] button, .gpick button, .games button'],
   ['lab','hash','#lab'],
   ['lab-topic','click','#labNav button'],
 ],
 'test/geoarcade__frq-exam-prep.html':[
   ['open','click','.frq-card button, .frq-card, #frqGrid button, #frqGrid .card'],
   ['scroll','scroll',900],
 ],
 'test/ap-world-compass__saq-checker.html':[
   ['open','click','#frqGrid button, #frqGrid .card, .frq-card'],
   ['scroll','scroll',700],
 ],
 'test/ap-world-compass__unit-1-the-global-tapestry.html':[
   ['flip','click','.vcard, .card'],
   ['quiz','click','.btn.gold, #quizBtn'],
   ['timeline','click','[data-tab=timeline], a[href="#timeline"], button:has-text("Timeline")'],
 ],
 'test/ap-euro-atlas__unit-1-renaissance-and-exploration.html':[
   ['flip','click','.vcard, .card, .term'],
   ['figures','click','button:has-text("Figures"), a:has-text("Figures")'],
   ['timeline','click','button:has-text("Timeline"), a:has-text("Timeline")'],
 ],
 'test/ap-euro-atlas__dbq-archive.html':[
   ['open','click','#frqGrid button, #frqGrid .card, .frq-card'],
   ['scroll','scroll',900],
 ],
 'test/ap-euro-atlas__dbq-cafe.html':[
   ['order','click','button:has-text("Order this DBQ"), .order'],
   ['scroll','scroll',900],
 ],
 'test/aplangstudio.html':[
   ['reading','click','a:has-text("Reading lab"), button:has-text("Reading lab")'],
   ['argument','click','a:has-text("Argument"), button:has-text("Argument")'],
 ],
 'test/ap-euro-atlas__the-isms-tracker.html':[
   ['chip','click','.chip, button'],
   ['scroll','scroll',900],
 ],
};
(async()=>{const b=await chromium.launch({executablePath:'/usr/bin/google-chrome'});
fs.mkdirSync('shots/states',{recursive:true});
for(const [f,list] of Object.entries(steps)){
 const ctx=await b.newContext({viewport:{width:1280,height:800},colorScheme:'dark'});const p=await ctx.newPage();
 const errs=[];p.on('pageerror',e=>errs.push(e.message.slice(0,100)));
 await p.goto('file://'+path.resolve(f));await p.waitForTimeout(2500);
 const slug=path.basename(f,'.html');
 for(const [name,kind,arg] of list){
  try{
   if(kind==='hash'){await p.evaluate(h=>{location.hash=h},arg);}
   else if(kind==='scroll'){await p.evaluate(y=>scrollTo(0,y),arg);}
   else{const loc=p.locator(arg).first();if(await loc.count()){await loc.scrollIntoViewIfNeeded();await loc.click({timeout:3000});}else{console.log('  no match',slug,name);}}
  }catch(e){console.log('  step fail',slug,name,e.message.slice(0,80))}
  await p.waitForTimeout(1200);
  const res=await p.evaluate(()=>{function lum([r,g,b]){const f=v=>{v/=255;return v<=.03928?v/12.92:((v+.055)/1.055)**2.4};return .2126*f(r)+.7152*f(g)+.0722*f(b)}
   function rgb(s){const m=s&&s.match(/rgba?\(([^)]+)\)/);if(!m)return null;const p=m[1].split(',').map(parseFloat);if(p.length>3&&p[3]===0)return null;return p.slice(0,3)}
   const L={};let n=0;const vh=innerHeight;
   for(const el of document.querySelectorAll('body *')){const cs=getComputedStyle(el);if(cs.display==='none'||cs.visibility==='hidden')continue;const r=el.getBoundingClientRect();if(r.width<40||r.height<16||r.bottom<0||r.top>vh)continue;const bg=rgb(cs.backgroundColor);if(bg&&lum(bg)>.6&&!el.closest('.dm-tg')){const k=el.tagName.toLowerCase()+(typeof el.className==='string'&&el.className?'.'+el.className.trim().split(/\s+/).slice(0,3).join('.'):'');L[k]=(L[k]||0)+1;n++}}
   return {n,L}});
  console.log(`${slug} [${name}] light=${res.n} ${JSON.stringify(res.L).slice(0,200)}`);
  await p.screenshot({path:`shots/states/${slug}--${name}.png`});
 }
 if(errs.length)console.log('  errors',slug,errs.slice(0,3));
 await ctx.close();}
await b.close()})();
