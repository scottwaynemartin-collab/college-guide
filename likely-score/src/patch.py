#!/usr/bin/env python3
"""Restore the likely-score Check on the live FRQ Exam Prep Room (Nov 6 2026).
Reads embed.html (live) + prog.js (its inflated program); writes out/frq-exam-prep.html."""
import re, base64, zlib, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
rd = lambda p: open(os.path.join(HERE, p), encoding='utf-8').read()
page = rd('embed.html')
prog = rd('prog.js')
mod = rd('gaquick.js')

def rep(src, old, new, n=1, label=''):
    c = src.count(old)
    if c != n:
        sys.exit(f'PATCH FAIL [{label}] expected {n} got {c}: {old[:90]!r}')
    return src.replace(old, new)

# ---------------- program ----------------
p = prog
# 1. the module goes right before the site data
p = rep(p, 'window.GA_SITE=', mod + '\n' + 'window.GA_SITE=', label='module')

# 2. keyword matching back on (Stuck panel greens, PDF)
p = rep(p, 'oe=(e,t)=>[]', 'oe=(e,t)=>window.GAQuick.matches(e,t)', label='matches')

# 3. Gemini prompts: question + guide + answer -> LIKELY POINT / LIKELY SCORE
p = rep(p, 've=e=>window.PracticeFeedback.coaching(e.verb,q(e)||"(blank)")',
        've=e=>window.GAQuick.handoffPart(j,e,q(e))', label='ve')
p = rep(p, 'we=()=>j.parts.map(e=>"PART "+e.l+"\\n"+ve(e)).join("\\n\\n")',
        'we=()=>window.GAQuick.handoffAll(j,j.parts.map(e=>q(e)))', label='we')

# 4. Check passes "silent" through so a fresh Check sets the likely point
p = rep(p, 'B.checked[e]=true;G();Le(p,host,false);', 'B.checked[e]=true;G();Le(p,host,t);', label='Ee')
p = rep(p, 'b("Write your answer first, then check its wording.")', 'b("Write your answer first, then I can check it.")', label='Ee toast')

# 5. the Check card itself
a = p.index('function Le(e,t){')
b = p.index('const Se=(e,t)=>', a)
LE = r'''function Le(e,t,silent){const fields={};_(e.verb).forEach(k=>fields[k]=I(e.l,k));const r=window.GAQuick.grade(j,e,fields);if(!silent){Ce(e.l,r.point,true);r.point?y.ok():y.meh()}const hitT=r.hits.length?r.hits.map(h=>h.t):r.near?[r.near.t]:[];t.innerHTML=`<div class="fb ${r.cls}"><h4>${r.head}<span class="src">Likely score · quick check</span></h4><p class="fbl">${r.blurb}</p>${r.lines.map(l=>`<div class="fbline"><span class="m ${l.ok?"y":"n"}">${l.ok?"✓":"!"}</span><span>${l.quote&&!l.ok?`<q>${s(window.GAQuick.snip(l.quote))}</q>`:""}${l.html}</span></div>`).join("")}<p class="fb-disc">Likely score = a practice estimate from a quick pattern check, not an official AP score. A correct answer in different words can be missed — Gemini or your AP Human Geography teacher can confirm it. Your teacher has the final word.</p><div class="fb-hand"><p><b>Want a second opinion?</b> This copies the question, the official scoring guide, and your answer. Paste it into Gemini and it tells you whether you likely earn the point and exactly what to change.</p><button class="btn gem" data-hand="${e.l}">🤖 Grade it in Gemini</button></div><div class="fb-guide"><h5>Options from the College Board scoring guide — any ONE earns the point (other correct answers can too)</h5><div class="acc">${e.accept.map((a,n)=>{const h=hitT.indexOf(a.t)>=0;return`<div class="${h?"hit":""}"><b>${h?"✓":n+1}</b><span>${s(a.t)}</span></div>`}).join("")}</div></div><div class="fb-look"><h5>What a scorer is looking for</h5>${e.check.map(c=>`<div class="fbline"><span class="m i">?</span><span>${s(c)}</span></div>`).join("")}</div>${Se(e.l,!0)}</div>`;Re(t,e)}'''
p = p[:a] + LE + p[b:]
p = rep(p, '${t?"Agree? You get the final say.":"Self-assess after checking the source — did you earn the point?"}',
        '${t?"That is the likely call. Disagree? You can change it:":"Your call — did you earn the point?"}', label='Se')

# 6. part pills
p = rep(p, '\'<span class="pill green">✓ Point earned</span>\'', '\'<span class="pill green">✓ Likely point</span>\'', label='pill render')
p = rep(p, 'o.textContent=1===t?"✓ Point earned":"Not yet"', 'o.textContent=1===t?"✓ Likely point":"Not yet"', label='pill set')
p = rep(p, '<span class="muted">Write something first — Check reports limited writing observations.</span>',
        '<span class="muted">Write something first — Check tells you if it likely earns the point.</span>', label='hint')

# 7. score bar
p = rep(p, 'n("#scoreBar").innerHTML=`<div class="sb-big">${e} / ${t}</div>\\n    <div class="sb-mid"><b>${s<t?`${t-s} part${t-s===1?"":"s"} left to score`:"Self-assessed. Confirm uncertain credit with your teacher."}</b>\\n      <div class="bar" style="margin-top:6px"><i style="width:${e/t*100}%;background:linear-gradient(90deg,var(--l4),var(--green))"></i></div></div>',
        'n("#scoreBar").innerHTML=`<div class="sb-big"><small class="sb-k">Likely score</small>${e} / ${t}</div>\\n    <div class="sb-mid"><b>${s<t?`${t-s} part${t-s===1?"":"s"} left to check`:e>=6?"Most parts likely earn the point. 🏆 Review any shaky ones.":"Revise the parts that likely missed the point, then check again."}</b>\\n      <div class="bar" style="margin-top:6px"><i style="width:${e/t*100}%;background:linear-gradient(90deg,var(--l4),var(--green))"></i></div><span class="sb-disc">Practice estimate, not an official AP score. Your AP Human Geography teacher has the final word.</span></div>',
        label='scorebar')

# 8. finish card
p = rep(p, 'Review the whole response, see it the way AP Classroom will, or open the sample response.',
        'Get a likely score on the whole thing, see it the way AP Classroom will, or open the sample response.', label='finish p')
p = rep(p, '${l()?"🎯 Get writing feedback on my whole FRQ":"🤖 Get writing feedback on my whole FRQ in Gemini"}',
        '${l()?"🎯 Grade my whole FRQ":"🤖 Get my likely score in Gemini"}', label='finish btn')

# 9. Gemini copy page
p = rep(p, '<title>Writing feedback on ${s(t)} in Gemini</title>', '<title>Grade ${s(t)} in Gemini</title>', label='hand title')
p = rep(p, '<h1>🤖 Writing feedback on ${s(t)} in Gemini</h1>\\n  <p>Only your response and task verb are below. Remove personal details or copied source text. Pasting sends it to Google. Writing/clarity feedback only: this response-only flow cannot verify factual accuracy, task relevance, or AP credit. Press the button, then paste it into Gemini.</p>',
        '<h1>🤖 Grade ${s(t)} in Gemini</h1>\\n  <p>Everything Gemini needs is below: the question, the official College Board scoring guide, and your answer. Press the button, then paste it into Gemini. It gives you a <b>likely</b> score and what to fix. AI can be wrong, and this is practice, not an official AP score &mdash; your AP Human Geography teacher has the final word.</p>',
        label='hand p')
p = rep(p, '<b>3</b>Read the suggestions, come back to GeoArcade, fix your lines, and Check again.',
        '<b>3</b>Read your likely score, come back to GeoArcade, fix your lines, and Check again.', label='hand step3')

p = rep(p, "g.classList.toggle('done',ok);window.open(", "g.classList.toggle('done',ok);if(ok)window.open(", label='copy guard')

# 10. Stuck panel
p = rep(p, '<h5>Answer list for comparison — other defensible answers may be possible</h5>',
        '<h5>The scoring guide accepts any ONE of these — you only need one</h5>', label='stuck h5')

# 11. PDF export
p = rep(p, '<div class="score">Self-assessment: ${n} / ${a} points${r?',
        '<div class="score">Likely score: ${n} / ${a} points${r?', label='pdf score')
p = rep(p, ':"<small>Self-scored</small>"}</div>',
        ':"<small>Practice estimate from the quick check (students can change any mark) &mdash; not an official AP score. Your AP Human Geography teacher has the final word.</small>"}</div>', label='pdf small')
p = rep(p, 'const a=_(t.verb).map(e=>I(t.l,e)).join(" "),i=oe(t,a);return`<div class="fbk"><b class="h">Quick check</b>\\n      ${i.length?`<div style="margin-bottom:4pt"><b>Words shared with the answer list (not verified):</b> ${i.slice(0,3).map(e=>s(e.t)).join(" &nbsp;·&nbsp; ")}</div>`:\'<div style="margin-bottom:4pt"><b>Writing check only — no score.</b> Facts, relevance, contradictions, and AP credit were not verified. Review the complete meaning with the source and your teacher.</div>\'}\\n      <b class="h">Answer list for comparison</b>',
        'const fl={};_(t.verb).forEach(k=>fl[k]=I(t.l,k));const g=window.GAQuick.grade(j,t,fl),i=g.hits.concat(g.xhits);return`<div class="fbk"><b class="h">Quick check — ${s(g.head.replace(/^\\S+\\s/,""))}</b>\\n      ${i.length?`<div style="margin-bottom:4pt"><b>Matched:</b> ${i.slice(0,3).map(e=>s(e.t)).join(" &nbsp;·&nbsp; ")}</div>`:\'<div style="margin-bottom:4pt"><b>No match found</b> against the scoring guide list.</div>\'}\\n      <b class="h">The options from the College Board scoring guide</b>',
        label='pdf quick')
p = rep(p, '<b class="h">Classroom checklist — use the exact prompt</b>', '<b class="h">What a scorer looks for</b>', label='pdf check')
p = rep(p, '<label><input type="checkbox" id="xFb" checked> Include my self-assessment and feedback</label>',
        '<label><input type="checkbox" id="xFb" checked> Include my likely score and feedback</label>', label='xFb')
p = rep(p, 'Every answer, check, and self-assessment on <b>', 'Every answer, check, and score on <b>', label='reset')

# 12. map add-on: teacher-added answers match again; note wording
p = rep(p, 'const hitsExtra = (p, text) => [];',
        'const hitsExtra = (p, text) => window.GAQuick.matchesExtra(p, text);', label='hitsExtra')
p = rep(p, 'Make it clear in your sentences, then run it through <b>Optional AI writing feedback</b> or check with your teacher.',
        'Make it clear in your sentences, then run it through <b>Grade it in Gemini</b> or check with your teacher.', label='gm-note')
p = rep(p, 'const EXTRA_T = \'Teacher-added answer ideas — ask your teacher to review how they apply\';',
        'const EXTRA_T = \'Also accepted — added by your AP Human Geography teacher (not on the College Board list)\';', label='EXTRA_T')

# 13. last add-on: the score label now lives in the score bar; add the small styles
p = rep(p, "if(score&&!score.querySelector('.practice-self')){",
        "if(false&&score&&!score.querySelector('.practice-self')){", label='practice-self')
p = rep(p, "n.textContent='Your self-assessment'", "n.textContent='Likely score'", label='practice-self text')
p = rep(p, ".fb-stale{padding:9px;background:#fff4ce;border:1px solid #bc9124;margin-bottom:10px;font-size:14px}';",
        ".fb-stale{padding:9px;background:#fff4ce;border:1px solid #bc9124;margin-bottom:10px;font-size:14px}.fb-disc{font-size:12.5px;font-weight:700;color:var(--ink-3);line-height:1.45;margin:10px 0 0}.sb-k{display:block;font-family:var(--body);font-size:10.5px;font-weight:900;letter-spacing:.12em;text-transform:uppercase;color:var(--ink-3);margin-bottom:4px}.sb-disc{display:block;font-size:11.5px;font-weight:700;color:var(--ink-3);margin-top:6px;line-height:1.35}';",
        label='css')


# ---------------- page HTML ----------------
h = page
h = rep(h, '<p class="lede">Practice with released free-response questions. Check reports entered text and wording; it cannot verify geography or predict AP credit. Compare the complete meaning with the prompt, source, and answer list, then ask your teacher about uncertain credit.</p>',
        '<p class="lede">Real free-response questions with the real College Board scoring guide. Write it, hit <b>Check</b>, and find out whether your answer <b>likely</b> earns the point &mdash; and exactly what to change if it doesn\'t. A likely score is practice feedback, not an official AP score: your AP Human Geography teacher has the final word.</p>', label='lede')
h = rep(h, '<i>Review text features and self-check meaning. Optional AI writing feedback can be wrong and is not a grade.</i>',
        '<i>Likely point or not, and what to fix. Then tap <b>Grade it in Gemini</b>, paste, Enter &mdash; a likely score on your actual sentences.</i>', label='hk1')
h = rep(h, '<i>An answer list to study and discuss; other defensible answers may be possible.</i>',
        '<i>Accepted examples from the College Board scoring guide. Other correct answers can also earn the point.</i>', label='hk2')
h = rep(h, '<i>Your answers, your feedback, your self-assessment &mdash; ready to turn in.</i>',
        '<i>Your answers, your feedback, your likely score &mdash; ready to turn in.</i>', label='hk4')
h = rep(h, '<strong>✓ Check my answer</strong>Review writing observations, then check meaning with the source.',
        '<strong>✓ Check my answer</strong>See whether it likely earns the point and what to fix.', label='ht2')
h = rep(h, '<strong>🤖 Optional AI writing feedback</strong>Tap it, then in Gemini press <kbd>Ctrl</kbd>+<kbd>V</kbd> (Mac: <kbd>⌘</kbd>+<kbd>V</kbd>) and Enter. Optional AI feedback can be wrong; your teacher judges credit.',
        '<strong>🤖 Grade it in Gemini</strong>Tap it, then in Gemini press <kbd>Ctrl</kbd>+<kbd>V</kbd> (Mac: <kbd>⌘</kbd>+<kbd>V</kbd>) and Enter. Gemini gives a likely score on your actual sentences.', label='ht3')
h = rep(h, '<div class="practice-note"><b>Practice check, not a grade.</b> This tool can count entered text and notice wording. It cannot verify facts, meaning, contradictions, or AP credit. T1-/E2-/A3- and placing specifics in E2- are classroom writing strategies, not universal AP requirements. Use the exact prompt and answer list, then ask your teacher about credit.</div>',
        '<div class="practice-note"><b>Likely score, not an official AP score.</b> Check and Gemini estimate whether each part would likely earn the point using the College Board scoring guide. They can miss a correct answer worded differently &mdash; your AP Human Geography teacher has the final word.</div>', label='practice-note')

# ---------------- leftover audit (student-visible strings) ----------------
core = p[p.index('window.GA_SITE='):]   # the old PracticeFeedback module above is no longer called
for bad in ['no score', 'No score', 'Optional AI writing', 'Self-check next', 'Self-assess', 'self-assessment', 'Self-assessment', 'Mr. Martin', 'Writing check']:
    if bad in core or bad in h:
        sys.exit('LEFTOVER: ' + bad)
if 'PracticeFeedback.inspect' in core or 'PracticeFeedback.coaching' in core:
    sys.exit('LEFTOVER: PracticeFeedback still wired')

# ---------------- repack ----------------
raw = p.encode('utf-8')
co = zlib.compressobj(9, zlib.DEFLATED, -15)
b64 = base64.b64encode(co.compress(raw) + co.flush()).decode()
m = re.search(r'var P="([^"]*)";', h)
h = h[:m.start(1)] + b64 + h[m.end(1):]
old_n = re.search(r'var o=new Uint8Array\((\d+)\);window\.__inflate', h)
h = h[:old_n.start(1)] + str(len(raw)) + h[old_n.end(1):]
os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
open(os.path.join(HERE, 'out/frq-exam-prep.html'), 'w', encoding='utf-8').write(h)
open(os.path.join(HERE, 'out/prog.js'), 'w', encoding='utf-8').write(p)
print('program', len(prog), '->', len(raw), '| page', len(page), '->', len(h), '| dm-css blocks', h.count('id="dm-css"'))
