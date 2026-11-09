/* GeoArcade · AP Practice Exam · app
   Screens: home → (practice topics → practice → summary) | (exam intro → exam → score → review)
   Storage is wrapped in try/catch with an in-memory fallback: Google Sites serves the embed from a
   sandboxed origin where localStorage can throw. No network calls, no window.top navigation. */
(function () {
  'use strict';

  /* ---- switches ---- */
  // Set to false to hide the "Estimated AP score" badge on the score report.
  const SHOW_AP_ESTIMATE = true;
  // Rough estimate only. The College Board does not publish cutoffs; these bands are the ones many
  // teachers use for a multiple-choice-only practice set.
  const AP_BANDS = [[80, 5], [65, 4], [50, 3], [35, 2], [0, 1]];

  const DATA = (window.PE_DATA && window.PE_DATA.units) || {};
  const STIM = window.PE_STIM;
  const esc = STIM.esc;
  const LETTERS = ['A', 'B', 'C', 'D', 'E'];
  const UNITS = [
    { n: 1, t: 'Thinking Geographically' }, { n: 2, t: 'Population and Migration' }, { n: 3, t: 'Cultural Patterns and Processes' },
    { n: 4, t: 'Political Patterns and Processes' }, { n: 5, t: 'Agriculture and Rural Land Use' }, { n: 6, t: 'Cities and Urban Land Use' },
    { n: 7, t: 'Industrial and Economic Development' }
  ];
  const SKILLS = { 1: 'Concepts & Processes', 2: 'Spatial Relationships', 3: 'Data Analysis', 4: 'Visual/Source Analysis', 5: 'Scale Analysis' };
  const unitTitle = n => (DATA[n] && DATA[n].title) || (UNITS.find(u => u.n === n) || {}).t || ('Unit ' + n);
  const unitVars = n => `--uc:var(--u${n});--uc-soft:var(--u${n}-soft);--uc-deep:var(--u${n}-deep);--uc-text:${n === 4 ? 'var(--ink)' : '#fff'}`;

  /* ---- storage (never trust it inside the Sites iframe) ---- */
  const mem = {};
  const store = {
    get(k, d) { try { const v = localStorage.getItem('pe:' + k); if (v != null) return JSON.parse(v); } catch (e) { } return (k in mem) ? mem[k] : d; },
    set(k, v) { mem[k] = v; try { localStorage.setItem('pe:' + k, JSON.stringify(v)); } catch (e) { } },
    del(k) { delete mem[k]; try { localStorage.removeItem('pe:' + k); } catch (e) { } }
  };

  /* ---- environment ---- */
  let embedded = false;
  try { embedded = window.self !== window.top; } catch (e) { embedded = true; }
  if (embedded) document.documentElement.classList.add('embedded');
  const reducedMotion = () => { try { return window.matchMedia('(prefers-reduced-motion: reduce)').matches; } catch (e) { return false; } };

  /* ---- state ---- */
  let S = { screen: 'home' };   // home | ptopics | practice | psummary | xintro | exam | xscore | xreview
  let P = null;                 // practice session
  let E = null;                 // exam session
  let timerId = null;
  const app = document.getElementById('app');
  const live = document.getElementById('live');

  const announce = msg => { if (!live) return; live.textContent = ''; setTimeout(() => { live.textContent = msg; }, 30); };
  function toast(msg) {
    const t = document.createElement('div'); t.className = 'toastmsg'; t.setAttribute('role', 'status'); t.textContent = msg;
    document.body.appendChild(t); setTimeout(() => t.remove(), 1900);
  }
  const mmss = ms => { const s = Math.max(0, Math.ceil(ms / 1000)); return Math.floor(s / 60) + ':' + String(s % 60).padStart(2, '0'); };
  const pctOf = (c, t) => t ? Math.round(100 * c / t) : 0;
  const barCls = p => p >= 75 ? '' : p >= 50 ? 'mid' : 'low';

  /* =================================================================
     shared pieces
     ================================================================= */
  const LOGO = `<svg viewBox="0 0 40 40" aria-hidden="true"><defs><linearGradient id="gA" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2F6FED"/><stop offset=".55" stop-color="#7C3AED"/><stop offset="1" stop-color="#FF6A3D"/></linearGradient></defs><rect width="40" height="40" rx="11" fill="url(#gA)"/><circle cx="19" cy="20" r="10.5" fill="none" stroke="#fff" stroke-width="2.4"/><ellipse cx="19" cy="20" rx="4.4" ry="10.5" fill="none" stroke="#fff" stroke-width="1.8" opacity=".9"/><path d="M8.6 20h20.8M10.4 14.6h17.2M10.4 25.4h17.2" stroke="#fff" stroke-width="1.5" fill="none" opacity=".8"/><circle cx="30.5" cy="29.5" r="6.2" fill="#FFC83D" stroke="#fff" stroke-width="1.6"/><path d="M28.9 26.7v5.6l4.4-2.8z" fill="#1F1B3A"/></svg>`;
  const upill = n => `<span class="upill" style="${unitVars(n)}"><i aria-hidden="true"></i>Unit ${n}</span>`;
  function topbar(ctx, acts) {
    return `<header class="bar"><div class="bar-in"><button class="brand" data-act="home" aria-label="Practice Exam, back to start">${LOGO}<span><small>GeoArcade</small><span class="bt">Practice Exam</span></span></button>${ctx ? `<div class="bar-ctx">${ctx}</div>` : ''}<div class="bar-sp"></div><div class="bar-acts">${acts || ''}</div></div></header>`;
  }
  const metaTag = (unit, q) => {
    const d = DATA[unit] || {}; const topic = (d.topics || []).find(t => t.id === q.topic);
    return `<div class="tag-meta"><span><b>Topic ${esc(q.topic)}</b>${topic ? ' · ' + esc(topic.name) : ''}</span><span>Skill ${esc(q.skill || '')}</span>${q.difficulty ? `<span>${esc(q.difficulty)}</span>` : ''}</div>`;
  };
  function topicRows(unit, byTopic) {
    const d = DATA[unit] || {};
    const ids = (d.topics || []).map(t => t.id).filter(id => byTopic[id]);
    Object.keys(byTopic).forEach(id => { if (!ids.includes(id)) ids.push(id); });
    return `<div class="rows">${ids.map(id => {
      const t = (d.topics || []).find(x => x.id === id) || { name: '' }; const r = byTopic[id]; const p = pctOf(r.c, r.t);
      return `<div class="row"><div class="lbl"><b>${esc(id)}</b>${esc(t.name)}</div><div class="trk" aria-hidden="true"><span class="${barCls(p)}" style="width:${p}%"></span></div><div class="cnt">${r.c}/${r.t}</div></div>`;
    }).join('')}</div>`;
  }
  function skillRows(bySkill) {
    const ids = Object.keys(bySkill).sort();
    return `<div class="rows">${ids.map(k => { const r = bySkill[k]; const p = pctOf(r.c, r.t); return `<div class="row"><div class="lbl"><b>${esc(k)}.x</b>${esc(SKILLS[k] || 'Skill ' + k)}</div><div class="trk" aria-hidden="true"><span class="${barCls(p)}" style="width:${p}%"></span></div><div class="cnt">${r.c}/${r.t}</div></div>`; }).join('')}</div>`;
  }
  function scoreSet(qs, answers) {
    let correct = 0; const byTopic = {}, bySkill = {}, missed = [];
    qs.forEach(q => {
      const ok = answers[q.id] === q.answer; if (ok) correct++; else missed.push(q);
      const t = byTopic[q.topic] || (byTopic[q.topic] = { c: 0, t: 0 }); t.t++; if (ok) t.c++;
      const k = String(q.skill || '?').split('.')[0]; const s = bySkill[k] || (bySkill[k] = { c: 0, t: 0 }); s.t++; if (ok) s.c++;
    });
    return { correct, total: qs.length, pct: pctOf(correct, qs.length), byTopic, bySkill, missed };
  }
  const apEstimate = pct => (AP_BANDS.find(b => pct >= b[0]) || [0, 1])[1];

  /* =================================================================
     home
     ================================================================= */
  function viewHome() {
    const avail = UNITS.filter(u => DATA[u.n]);
    const pq = avail.reduce((a, u) => a + DATA[u.n].practice.length, 0);
    const xq = avail.reduce((a, u) => a + DATA[u.n].exam.questions.length, 0);
    const kpi = (v, k) => `<div class="kpi"><span class="v">${v}</span><span class="k">${k}</span></div>`;
    return topbar('', '') + `<main id="main">
      <section class="hero"><div class="eyebrow">GeoArcade · AP® Human Geography</div><h1><span class="gl">Practice Exam</span></h1><p class="sub">Practice by topic, then take a timed exam built like the real one.</p>
        <div class="kpis" aria-label="What's inside">${kpi(avail.length, avail.length === 1 ? 'Unit available' : 'Units available')}${kpi(pq, 'Practice questions')}${kpi(xq, 'Exam questions')}</div></section>
      <section class="ugrid" aria-label="Units">${UNITS.map(unitCard).join('')}</section>
      <section class="how" aria-label="How it works">
        <div class="panel"><span class="stepn" aria-hidden="true">1</span><h3>Practice a topic</h3><p>Pick a unit and a topic. Answer one question at a time, untimed. Every answer comes with a plain-English explanation and a line on why each wrong choice is wrong.</p></div>
        <div class="panel"><span class="stepn" aria-hidden="true">2</span><h3>Take the timed exam</h3><p>25 questions in 25 minutes, five choices each, with stimulus sets just like AP Classroom. Flag questions, jump around, change answers until you submit.</p></div>
        <div class="panel"><span class="stepn" aria-hidden="true">3</span><h3>Read your report</h3><p>See your score by topic and by skill, review every question with College Board–style notes on each choice, then retake it or bring questions to your AP Human Geography teacher.</p></div>
      </section>
      <p class="note-line">Questions are original and written in the style of the AP exam; they are not College Board questions.</p>
    </main><footer class="foot">Questions © Scott Martin · <a href="mailto:APandAbroad@gmail.com">APandAbroad@gmail.com</a></footer>`;
  }
  function unitCard(u) {
    const d = DATA[u.n];
    if (!d) return `<article class="ucd soon" style="${unitVars(u.n)}" aria-disabled="true"><div class="uh"><span class="un">${u.n}</span></div><h3>${esc(u.t)}</h3><span class="soonpill">Coming soon</span></article>`;
    const best = store.get('best:' + u.n), prog = store.get('exam:' + u.n);
    const x = d.exam || {}; const xn = (x.questions || []).length;
    return `<article class="ucd live" style="${unitVars(u.n)}"><div class="uh"><span class="un" aria-hidden="true">${u.n}</span>${prog ? `<span class="resume">⏱ Exam in progress</span>` : (best ? `<span class="best">Best exam <span class="ok">${best.correct}/${best.total}</span> · ${best.pct}%</span>` : '')}</div>
      <h3><span class="sr-only">Unit ${u.n}: </span>${esc(d.title || u.t)}</h3>
      <div class="ubtns"><button class="act unit" data-act="ptopics" data-arg="${u.n}"><span>Practice</span><small>${d.practice.length} questions</small></button>
      <button class="act ghost" data-act="xintro" data-arg="${u.n}"><span>${prog ? 'Resume timed exam' : 'Timed Exam'}</span><small>${xn} questions · ${x.timeMinutes || 25} min</small></button></div></article>`;
  }

  /* =================================================================
     practice
     ================================================================= */
  function viewTopics() {
    const unit = S.unit, d = DATA[unit];
    const counts = {}; d.practice.forEach(q => { counts[q.topic] = (counts[q.topic] || 0) + 1; });
    const chip = (id, name, n, pressed) => `<button class="tchip" style="${unitVars(unit)}" data-act="p-start" data-arg="${esc(id)}" aria-pressed="${pressed}" ${n ? '' : 'disabled'}><span class="id">${esc(id)}</span><span>${esc(name)}</span><span class="n">${n}</span></button>`;
    return topbar(`${upill(unit)}<span class="ellip">Practice</span>`, `<button class="act quiet sm" data-act="home">← Back to units</button>`) + `<main id="main"><div class="phead" style="${unitVars(unit)}"><div class="eyebrow">Unit ${unit} · ${esc(d.title)}</div><h2>Practice by topic</h2><p class="muted">Untimed. One question at a time, with the answer explained right after you pick. Choose a topic or practice everything.</p>
      <div class="tchips" role="group" aria-label="Topics">${chip('all', 'All topics', d.practice.length, 'false')}${(d.topics || []).map(t => chip(t.id, t.name, counts[t.id] || 0, 'false')).join('')}</div></div></main>`;
  }
  function startPractice(unit, topic, qs) {
    const d = DATA[unit];
    const list = qs || (topic === 'all' ? d.practice.slice() : d.practice.filter(q => q.topic === topic));
    if (!list.length) return;
    P = { unit, topic, qs: list, i: 0, answers: {}, label: topic === 'all' ? 'All topics' : (((d.topics || []).find(t => t.id === topic) || {}).name || topic) };
    S.screen = 'practice'; render(); focusQ();
  }
  function viewPractice() {
    const unit = P.unit, q = P.qs[P.i], n = P.qs.length, pick = P.answers[q.id];
    const done = Object.keys(P.answers).length;
    const opts = LETTERS.map(L => {
      let cls = 'opt', mk = '';
      if (pick) { if (L === q.answer) { cls += ' ok'; mk = '✓ Correct answer'; } else if (L === pick) { cls += ' bad'; mk = '✗ Your answer'; } else cls += ' dim'; }
      return `<button class="${cls}" data-act="p-pick" data-arg="${L}" ${pick ? 'disabled' : ''} aria-label="${L}: ${esc(q.options[L])}${pick ? (L === q.answer ? ' (correct answer)' : L === pick ? ' (your answer)' : '') : ''}"><span class="ltr" aria-hidden="true">${L}</span><span class="txt">${esc(q.options[L])}</span><span class="mk" aria-hidden="true">${mk}</span></button>`;
    }).join('');
    let fb = '';
    if (pick) {
      const ok = pick === q.answer;
      const others = LETTERS.filter(L => L !== q.answer && L !== pick && q.whyNot && q.whyNot[L]);
      fb = `<div class="fbk ${ok ? 'ok' : 'bad'}" role="status"><div class="ico ${ok ? 'pop' : ''}" aria-hidden="true">${ok ? '✓' : '✗'}${ok ? burst() : ''}</div><div class="body"><h4>${ok ? ['Correct!', 'Nice work!', 'You got it!', 'Exactly right!'][P.i % 4] : `Not quite. The answer is ${q.answer}.`}</h4><p class="exp">${esc(q.explanation)}</p>
        ${!ok && q.whyNot && q.whyNot[pick] ? `<div class="whynot"><b>You picked ${pick}.</b> ${esc(q.whyNot[pick])}</div>` : ''}
        ${others.length ? `<details class="more"><summary>Show why each other answer is wrong</summary><div class="inner">${others.map(L => `<div class="wn"><span class="ltr" aria-hidden="true">${L}</span><div><b>${L}.</b> ${esc(q.whyNot[L])}</div></div>`).join('')}</div></details>` : ''}
        <div style="margin-top:12px">${metaTag(unit, q)}</div></div></div>
        <div class="pnext"><div class="hint"><span class="kbd">Enter</span> or <span class="kbd">→</span> for next</div><button class="act primary" data-act="p-next" id="pnext">${P.i + 1 < n ? 'Next question →' : 'See my summary →'}</button></div>`;
    }
    return topbar(`${upill(unit)}<span class="ellip">Practice · ${esc(P.label)}</span>`, `<button class="act quiet sm" data-act="p-topics">Topics</button><button class="act quiet sm" data-act="home">Units</button>`) + `<main id="main" style="${unitVars(unit)}">
      <div class="phead"><div class="prog-row"><span>Question ${P.i + 1} of ${n}</span><div class="prog" role="progressbar" aria-valuemin="0" aria-valuemax="${n}" aria-valuenow="${done}" aria-label="Answered ${done} of ${n}"><span style="width:${(done / n) * 100}%"></span></div><span>${done} answered</span></div></div>
      <article class="qcard" id="qcard"><h2 class="qn" id="qhead" tabindex="-1">Question ${P.i + 1}<span class="sr-only"> of ${n}</span></h2>${q.stimulus ? STIM.render(q.stimulus) : ''}<p class="stem">${esc(q.stem)}</p>
      <div class="opts" role="group" aria-label="Answer choices">${opts}</div>${fb}
      ${pick ? '' : `<div class="pnext"><div class="hint">Press <span class="kbd">A</span>–<span class="kbd">E</span> to answer</div></div>`}</article></main>`;
  }
  function burst() {
    if (reducedMotion()) return '';
    const cols = ['var(--l1)', 'var(--l2)', 'var(--l3)', 'var(--sun)', 'var(--pink)', 'var(--mint)'];
    return `<span class="burst" aria-hidden="true">${Array.from({ length: 8 }, (_, i) => { const a = i / 8 * Math.PI * 2, d = 34 + (i % 2) * 10; return `<i style="--dx:${Math.round(Math.cos(a) * d)}px;--dy:${Math.round(Math.sin(a) * d)}px;--c:${cols[i % cols.length]};animation-delay:${i * 15}ms"></i>`; }).join('')}</span>`;
  }
  function viewSummary() {
    const unit = P.unit, r = scoreSet(P.qs, P.answers);
    return topbar(`${upill(unit)}<span class="ellip">Practice · ${esc(P.label)}</span>`, `<button class="act quiet sm" data-act="home">Units</button>`) + `<main id="main" style="${unitVars(unit)}"><div class="score">
      <section class="panel"><div class="sumhead"><div class="eyebrow">Practice set complete</div><div class="big" aria-label="${r.correct} of ${r.total} correct">${r.correct}<small>/${r.total}</small></div><p>${r.pct}% correct · ${esc(P.label)}</p></div>
      <h3>By topic</h3>${topicRows(unit, r.byTopic)}
      <div class="acts center" style="margin-top:22px">${r.missed.length ? `<button class="act primary" data-act="p-missed">Try the ones I missed (${r.missed.length})</button>` : `<span class="rvb ok">✓ Nothing missed. Perfect set!</span>`}<button class="act ghost" data-act="p-topics">Back to topics</button><button class="act ghost" data-act="home">Back to units</button></div></section></div></main>`;
  }
  function pPick(L) {
    const q = P.qs[P.i]; if (P.answers[q.id] || !q.options[L]) return;
    P.answers[q.id] = L; render();
    const ok = L === q.answer;
    announce(ok ? `Correct. ${q.explanation}` : `Not quite. The answer is ${q.answer}. ${q.explanation}`);
    const nb = document.getElementById('pnext'); if (nb) nb.focus({ preventScroll: true });
  }
  function pNext() {
    const q = P.qs[P.i]; if (!P.answers[q.id]) return;
    if (P.i + 1 < P.qs.length) { P.i++; render(); focusQ(); window.scrollTo({ top: 0, behavior: reducedMotion() ? 'auto' : 'smooth' }); }
    else { S.screen = 'psummary'; render(); window.scrollTo(0, 0); }
  }
  const focusQ = () => { const h = document.getElementById('qhead'); if (h) h.focus({ preventScroll: true }); };

  /* =================================================================
     exam
     ================================================================= */
  function viewIntro() {
    const unit = S.unit, d = DATA[unit], x = d.exam, saved = store.get('exam:' + unit);
    const n = x.questions.length;
    return topbar(`${upill(unit)}<span class="ellip">Timed Exam</span>`, `<button class="act quiet sm" data-act="home">← Back to units</button>`) + `<main id="main"><div class="xintro">
      <div><div class="eyebrow">Unit ${unit} · Timed exam</div><h2>${esc(x.title || d.title)}</h2></div>
      <div class="facts" aria-label="Exam format"><span>${n} questions</span><span>${x.timeMinutes} minutes</span><span>5 choices</span><span>no penalty for guessing</span></div>
      <div class="dir"><strong>Directions.</strong> ${esc(x.directions)}</div>
      <ul><li>The timer starts when you press Start and keeps running if you leave the page.</li><li>Flag a question to come back to it. The question navigator shows what is answered, unanswered, and flagged.</li><li>You can change any answer until you submit. The exam submits itself when time runs out.</li></ul>
      <div class="acts">${saved ? `<button class="act primary" data-act="x-resume" data-arg="${unit}">Resume exam</button><button class="act ghost" data-act="x-start" data-arg="${unit}">Start over</button>` : `<button class="act primary" data-act="x-start" data-arg="${unit}">Start exam</button>`}</div>
      ${saved ? `<p class="note">You have an exam in progress with ${Object.keys(saved.answers || {}).length} of ${n} answered. Resuming keeps your answers and the original clock.</p>` : ''}
    </div></main>`;
  }
  function startExam(unit, resume) {
    const d = DATA[unit], x = d.exam;
    const saved = resume ? store.get('exam:' + unit) : null;
    const now = Date.now();
    E = { unit, qs: x.questions.slice(), answers: {}, flags: {}, i: 0, startedAt: now, endsAt: now + (x.timeMinutes || 25) * 60000, navOpen: false, confirm: false, stimOff: false, submitted: false, announced: {} };
    if (saved && saved.endsAt) Object.assign(E, { answers: saved.answers || {}, flags: saved.flags || {}, i: Math.min(saved.i || 0, E.qs.length - 1), startedAt: saved.startedAt || now, endsAt: saved.endsAt });
    S.screen = 'exam'; S.unit = unit; persistExam(); render(); window.scrollTo(0, 0); startTimer();
    if (E.endsAt <= Date.now()) submitExam(true);
  }
  const persistExam = () => { if (!E || E.submitted) return; store.set('exam:' + E.unit, { answers: E.answers, flags: E.flags, i: E.i, startedAt: E.startedAt, endsAt: E.endsAt }); };
  function stimFor(qs, q) {
    if (q.stimulus) return { stim: q.stimulus, label: q.setLabel || '' };
    if (q.set) { const first = qs.find(o => o.set === q.set && o.stimulus); if (first) return { stim: first.stimulus, label: first.setLabel || q.setLabel || '' }; }
    return null;
  }
  function timerHTML() {
    const rem = Math.max(0, E.endsAt - Date.now());
    return `<div class="timer ${rem <= 60000 ? 'crit' : rem <= 300000 ? 'warn' : ''}" id="tmr" role="timer" aria-live="polite" aria-atomic="true"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M12 7v5l3.5 2" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg><span class="digits" aria-hidden="true">${mmss(rem)}</span><span class="sr-only" id="tmrsr">${mmss(rem)} remaining</span></div>`;
  }
  function viewExam() {
    const q = E.qs[E.i], n = E.qs.length, pick = E.answers[q.id], st = stimFor(E.qs, q), flagged = !!E.flags[q.id];
    const answered = Object.keys(E.answers).length;
    const opts = LETTERS.map(L => `<button class="xopt" role="radio" aria-checked="${pick === L}" data-act="x-pick" data-arg="${L}"><span class="ltr" aria-hidden="true">${L}</span><span class="txt"><span class="sr-only">${L}. </span>${esc(q.options[L])}</span></button>`).join('');
    const stimCol = st ? `<aside class="scol ${E.stimOff ? 'off' : ''}" aria-label="Stimulus"><div class="sticky">${st.label ? `<div class="setlabel">${esc(st.label)}</div>` : ''}<button class="act ghost sm stoggle" data-act="x-stim" aria-expanded="${!E.stimOff}">${E.stimOff ? 'Show stimulus' : 'Hide stimulus'}</button><div class="stimwrap">${STIM.render(st.stim)}</div></div></aside>` : '';
    const nav = E.navOpen ? `<div class="veil" data-act="x-nav-close"><div class="drawer" role="dialog" aria-modal="true" aria-label="Question navigator" data-stop="1"><h3>Questions <button class="act quiet sm" data-act="x-nav-close" aria-label="Close navigator">✕</button></h3>
        <div class="navgrid">${E.qs.map((o, i) => `<button class="navq ${E.answers[o.id] ? 'ans' : ''} ${E.flags[o.id] ? 'flag' : ''} ${i === E.i ? 'cur' : ''}" data-act="x-goto" data-arg="${i}" aria-label="Question ${i + 1}, ${E.answers[o.id] ? 'answered' : 'unanswered'}${E.flags[o.id] ? ', flagged' : ''}${i === E.i ? ', current' : ''}" ${i === E.i ? 'aria-current="true"' : ''}>${i + 1}</button>`).join('')}</div>
        <div class="navkey"><span><i class="ans"></i>Answered (${answered})</span><span><i></i>Unanswered (${n - answered})</span><span><i class="flag"></i>Flagged (${Object.keys(E.flags).length})</span></div>
        <div style="margin-top:auto" class="acts"><button class="act primary wide" data-act="x-submit-ask">Submit exam</button></div></div></div>` : '';
    const unanswered = E.qs.map((o, i) => E.answers[o.id] ? null : i + 1).filter(Boolean);
    const flags = E.qs.map((o, i) => E.flags[o.id] ? i + 1 : null).filter(Boolean);
    const confirm = E.confirm ? `<div class="veil center" data-act="x-confirm-close"><div class="sheet" role="dialog" aria-modal="true" aria-labelledby="cfh" data-stop="1"><h3 id="cfh">Submit your exam?</h3>
        <div class="list">${unanswered.length ? `<div><b>${unanswered.length} unanswered:</b><div class="nums">${unanswered.map(x => `<span>${x}</span>`).join('')}</div></div>` : '<div><b>All questions answered.</b></div>'}${flags.length ? `<div><b>${flags.length} flagged:</b><div class="nums">${flags.map(x => `<span class="f">${x}</span>`).join('')}</div></div>` : ''}<div class="muted small">There is no penalty for guessing. Once you submit you cannot change answers.</div></div>
        <div class="acts end"><button class="act ghost" data-act="x-confirm-close" id="cfback">Keep working</button><button class="act primary" data-act="x-submit">Submit exam</button></div></div></div>` : '';
    return `<header class="xtop"><div class="xtop-in"><div class="who">${upill(E.unit)}<span class="ellip">Timed exam</span></div><div class="qpos"><span class="long">Question ${E.i + 1} of ${n}</span><span class="short" aria-hidden="true">${E.i + 1}<span class="muted">/${n}</span></span></div><div class="bar-sp"></div>${timerHTML()}<button class="act ghost sm" id="navbtn" data-act="x-nav" aria-haspopup="dialog" aria-expanded="${E.navOpen}" aria-label="Questions navigator"><span class="long">Questions</span><svg class="ic short" viewBox="0 0 24 24" aria-hidden="true"><g fill="currentColor"><rect x="3" y="3" width="8" height="8" rx="2"/><rect x="13" y="3" width="8" height="8" rx="2"/><rect x="3" y="13" width="8" height="8" rx="2"/><rect x="13" y="13" width="8" height="8" rx="2"/></g></svg></button><button class="act primary sm" data-act="x-submit-ask">Submit</button></div></header>
      <main id="main"><div class="xwrap ${st ? 'has-stim' : ''}">${stimCol}<section class="xq" aria-labelledby="qhead"><h2 class="qn" id="qhead" tabindex="-1">Question ${E.i + 1}${flagged ? '<span class="flagged-note"> · ⚑ Flagged</span>' : ''}</h2><p class="stem">${esc(q.stem)}</p>
        <div class="xopts" role="radiogroup" aria-label="Answer choices">${opts}</div>
        <div class="xnav"><button class="act ghost" data-act="x-prev" ${E.i === 0 ? 'disabled' : ''}>← Previous</button><div class="mid"><button class="act ghost sm" data-act="x-flag" aria-pressed="${flagged}">⚑ ${flagged ? 'Flagged' : 'Flag'}</button></div>${E.i + 1 < n ? `<button class="act primary" data-act="x-next">Next →</button>` : `<button class="act primary" data-act="x-submit-ask">Review &amp; submit</button>`}</div></section></div></main>${nav}${confirm}`;
  }
  function xGoto(i) {
    E.i = Math.max(0, Math.min(E.qs.length - 1, i)); E.navOpen = false; persistExam(); render(); focusQ();
    window.scrollTo({ top: 0, behavior: 'auto' });
  }
  function xPick(L) {
    const q = E.qs[E.i]; if (!q.options[L]) return;
    E.answers[q.id] = L; persistExam();
    document.querySelectorAll('.xopt').forEach(b => b.setAttribute('aria-checked', String(b.dataset.arg === L)));
  }
  function xFlag() {
    const q = E.qs[E.i]; if (E.flags[q.id]) delete E.flags[q.id]; else E.flags[q.id] = true;
    persistExam(); render(); announce(E.flags[q.id] ? `Question ${E.i + 1} flagged` : `Flag removed from question ${E.i + 1}`);
    const b = document.querySelector('[data-act="x-flag"]'); if (b) b.focus({ preventScroll: true });
  }
  function startTimer() { stopTimer(); timerId = setInterval(tick, 250); tick(); }
  function stopTimer() { if (timerId) clearInterval(timerId); timerId = null; }
  function tick() {
    if (!E || E.submitted) { stopTimer(); return; }
    const rem = Math.max(0, E.endsAt - Date.now());
    const el = document.getElementById('tmr');
    if (el) {
      const d = el.querySelector('.digits'); if (d) d.textContent = mmss(rem);
      el.classList.toggle('warn', rem <= 300000 && rem > 60000); el.classList.toggle('crit', rem <= 60000);
      const mins = Math.ceil(rem / 60000);
      [10, 5, 2, 1].forEach(m => { if (mins <= m && !E.announced[m]) { E.announced[m] = true; const sr = el.querySelector('#tmrsr'); if (sr) sr.textContent = `${m} minute${m === 1 ? '' : 's'} remaining`; } });
    }
    if (rem <= 0) submitExam(true);
  }
  function submitExam(auto) {
    if (!E || E.submitted) return;
    stopTimer(); E.submitted = true; E.confirm = false; E.navOpen = false;
    const r = scoreSet(E.qs, E.answers);
    r.timeUsed = Math.min(E.endsAt - E.startedAt, Date.now() - E.startedAt); r.auto = !!auto; r.when = Date.now();
    E.result = r; store.del('exam:' + E.unit);
    const best = store.get('best:' + E.unit);
    if (!best || r.correct > best.correct) store.set('best:' + E.unit, { correct: r.correct, total: r.total, pct: r.pct, when: r.when });
    S.screen = 'xscore'; S.showCopy = false; render(); window.scrollTo(0, 0);
    announce(auto ? `Time is up. Your exam was submitted. You scored ${r.correct} out of ${r.total}.` : `Exam submitted. You scored ${r.correct} out of ${r.total}.`);
    if (r.pct >= 50) confetti();
  }
  function viewScore() {
    const r = E.result, unit = E.unit, d = DATA[unit], n = r.total;
    const ap = apEstimate(r.pct);
    const bestNow = store.get('best:' + unit);
    return topbar(`${upill(unit)}<span class="ellip">Score report</span>`, `<button class="act quiet sm" data-act="home">Units</button>`) + `<main id="main"><div class="score">
      <section class="score-hero"><div class="eyebrow">${esc(d.exam.title || d.title)}</div><div class="big" aria-label="${r.correct} out of ${n}">${r.correct}<small>/${n}</small></div><div class="pct">${r.pct}% correct</div><div class="sub">${r.auto ? 'Time ran out and the exam submitted itself · ' : ''}Time used ${mmss(r.timeUsed)} of ${d.exam.timeMinutes}:00${bestNow && bestNow.correct === r.correct && bestNow.when === r.when ? ' · New best for this unit' : ''}</div>
        ${SHOW_AP_ESTIMATE ? `<div class="apbadge" role="note"><span class="l">Estimated AP score</span><span class="n">${ap}</span><span class="d">Rough estimate from your percent — the College Board does not publish cutoffs.</span></div>` : ''}
        <div class="acts center" style="margin-top:20px"><button class="act primary" data-act="x-review" data-arg="all">Review all ${n}</button>${r.missed.length ? `<button class="act ghost" data-act="x-review" data-arg="missed">Missed only (${r.missed.length})</button>` : ''}</div></section>
      <div class="two"><section class="panel"><h3>By topic</h3>${topicRows(unit, r.byTopic)}</section><section class="panel"><h3>By skill category</h3>${skillRows(r.bySkill)}</section></div>
      <section class="panel"><div class="acts between"><div class="acts"><button class="act ghost" data-act="x-copy">Copy my results</button><button class="act ghost" data-act="x-retake">Retake</button></div><button class="act soft" data-act="home">Back to units</button></div>
        ${S.showCopy ? `<div class="copybox" style="margin-top:14px"><div class="small muted">Copying was blocked here, so select the text below and copy it yourself (Ctrl/Cmd + C).</div><textarea id="copyta" readonly aria-label="Results summary">${esc(resultsText())}</textarea></div>` : ''}</section></div></main>`;
  }
  function resultsText() {
    const r = E.result, d = DATA[E.unit];
    const lines = [`GeoArcade Practice Exam · Unit ${E.unit}: ${d.title}`, `Score: ${r.correct}/${r.total} (${r.pct}%)${SHOW_AP_ESTIMATE ? ` · Estimated AP score: ${apEstimate(r.pct)} (rough estimate)` : ''}`, `Time used: ${mmss(r.timeUsed)} of ${d.exam.timeMinutes}:00${r.auto ? ' (auto-submitted)' : ''}`, '', 'By topic:'];
    (d.topics || []).forEach(t => { const x = r.byTopic[t.id]; if (x) lines.push(`  ${t.id} ${t.name}: ${x.c}/${x.t}`); });
    lines.push('', 'By skill:');
    Object.keys(r.bySkill).sort().forEach(k => lines.push(`  ${SKILLS[k] || 'Skill ' + k} (${k}.x): ${r.bySkill[k].c}/${r.bySkill[k].t}`));
    lines.push('', `Missed: ${r.missed.length ? r.missed.map(q => q.n || E.qs.indexOf(q) + 1).join(', ') : 'none'}`, '', 'GeoArcade · sites.google.com/view/geoarcade');
    return lines.join('\n');
  }
  async function copyResults() {
    const text = resultsText();
    try {
      if (!navigator.clipboard || !navigator.clipboard.writeText) throw new Error('no clipboard');
      await navigator.clipboard.writeText(text); toast('Results copied');
    } catch (e) {
      S.showCopy = true; render();
      const ta = document.getElementById('copyta'); if (ta) { ta.focus(); ta.select(); }
    }
  }
  function viewReview() {
    const r = E.result, unit = E.unit, f = S.rvFilter || 'all';
    const list = E.qs.map((q, i) => ({ q, i })).filter(o => f === 'all' || E.answers[o.q.id] !== o.q.answer);
    const seenSets = {};
    const items = list.map(({ q, i }) => {
      const pick = E.answers[q.id], ok = pick === q.answer, state = !pick ? 'skip' : ok ? 'ok' : 'bad';
      const st = stimFor(E.qs, q); let stimHTML = '';
      if (st) {
        if (q.set && seenSets[q.set]) stimHTML = `<details class="more"><summary>Show the shared stimulus${st.label ? ` (${esc(st.label.replace(/\s*refer to.*$/i, ''))})` : ''}</summary><div class="inner">${STIM.render(st.stim)}</div></details>`;
        else { stimHTML = `${st.label ? `<div class="setlabel">${esc(st.label)}</div>` : ''}${STIM.render(st.stim)}`; if (q.set) seenSets[q.set] = true; }
      }
      return `<article class="rv ${state}" id="rv${i + 1}"><header><span class="rn">Question ${i + 1}</span><span class="rvb ${state}">${state === 'ok' ? '✓ Correct' : state === 'bad' ? '✗ Missed' : '– Not answered'}</span>${metaTag(unit, q)}</header>${stimHTML}<p class="stem">${esc(q.stem)}</p>
        <ol class="rvopts" aria-label="Answer choices">${LETTERS.map(L => { const isC = L === q.answer, isP = L === pick; const cls = isC ? 'is-correct' : isP ? 'is-pick' : ''; const mk = isC && isP ? '✓ Your answer · correct' : isC ? '✓ Correct answer' : isP ? '✗ Your answer' : ''; return `<li class="${cls}"><span class="ltr" aria-hidden="true">${L}</span><div><span class="sr-only">${L}. </span>${esc(q.options[L])}${mk ? `<span class="mk">${mk}</span>` : ''}</div></li>`; }).join('')}</ol>
        <div class="fbk ${ok ? 'ok' : 'bad'}"><div class="ico" aria-hidden="true">${ok ? '✓' : '✗'}</div><div class="body"><h4>${ok ? 'Why this is right' : `The answer is ${q.answer}`}</h4><p class="exp">${esc(q.explanation)}</p>
        ${q.rationales ? `<details class="more"><summary>College Board–style notes on every choice</summary><div class="inner">${LETTERS.map(L => `<div class="rat ${L === q.answer ? 'correct' : ''}"><span class="ltr" aria-hidden="true">${L}</span><div><b>${L}.</b> ${esc(q.rationales[L] || '')}</div></div>`).join('')}</div></details>` : ''}</div></div></article>`;
    }).join('');
    return topbar(`${upill(unit)}<span class="ellip">Review</span>`, `<button class="act quiet sm" data-act="x-back-score">← Score report</button>`) + `<main id="main"><div class="review"><div class="rvhead"><h2>Review · ${r.correct}/${r.total}</h2><div class="seg" role="group" aria-label="Filter"><button data-act="x-review-filter" data-arg="all" aria-pressed="${f === 'all'}">All ${r.total}</button><button data-act="x-review-filter" data-arg="missed" aria-pressed="${f === 'missed'}">Missed only (${r.missed.length})</button></div></div>
      ${items || `<div class="empty">Nothing missed. Every answer was correct.</div>`}
      <div class="acts center"><button class="act ghost" data-act="x-back-score">← Score report</button><button class="act ghost" data-act="x-retake">Retake</button><button class="act soft" data-act="home">Back to units</button></div></div></main>`;
  }

  /* ---- celebration (score report only; practice uses a tiny CSS burst) ---- */
  function confetti() {
    if (reducedMotion()) return;
    let cv = document.getElementById('confetti');
    if (!cv) { cv = document.createElement('canvas'); cv.id = 'confetti'; cv.setAttribute('aria-hidden', 'true'); document.body.appendChild(cv); }
    const ctx = cv.getContext('2d'); if (!ctx) return;
    cv.width = innerWidth; cv.height = innerHeight;
    const cols = ['#FF6A3D', '#2F6FED', '#7C3AED', '#FFC83D', '#0D9488', '#EC4899'];
    const ps = Array.from({ length: 110 }, () => ({ x: innerWidth / 2 + 240 * (Math.random() - .5), y: innerHeight * .3, vx: 13 * (Math.random() - .5), vy: -11 * Math.random() - 4, g: .3 + .2 * Math.random(), r: 4 + 5 * Math.random(), c: cols[Math.random() * cols.length | 0], a: 6.28 * Math.random(), va: .3 * (Math.random() - .5) }));
    const t0 = performance.now();
    (function frame(t) {
      const k = (t - t0) / 1700; ctx.clearRect(0, 0, cv.width, cv.height);
      if (k >= 1) { cv.remove(); return; }
      ps.forEach(p => { p.vy += p.g; p.x += p.vx; p.y += p.vy; p.a += p.va; ctx.save(); ctx.globalAlpha = Math.max(0, 1 - k * k); ctx.translate(p.x, p.y); ctx.rotate(p.a); ctx.fillStyle = p.c; ctx.fillRect(-p.r / 2, -p.r / 2, p.r, p.r * .6); ctx.restore(); });
      requestAnimationFrame(frame);
    })(t0);
  }

  /* =================================================================
     render + events
     ================================================================= */
  function view() {
    switch (S.screen) {
      case 'ptopics': return viewTopics();
      case 'practice': return viewPractice();
      case 'psummary': return viewSummary();
      case 'xintro': return viewIntro();
      case 'exam': return viewExam();
      case 'xscore': return viewScore();
      case 'xreview': return viewReview();
      default: return viewHome();
    }
  }
  function render() {
    document.body.classList.toggle('exam', /^x|^exam$/.test(S.screen));
    document.body.classList.toggle('practice', /^p/.test(S.screen));
    app.innerHTML = view();
    markScrollables();
    if (S.screen === 'exam') {
      if (E.navOpen) { const f = app.querySelector('.drawer .navq.cur') || app.querySelector('.drawer button'); if (f) f.focus(); }
      else if (E.confirm) { const f = document.getElementById('cfback'); if (f) f.focus(); }
    }
  }
  // Charts and maps keep a minimum width so their labels stay legible; on phones they scroll sideways.
  // Add a small hint above any that actually overflow (checked after render and on resize).
  function markScrollables() {
    app.querySelectorAll('.scrollhint').forEach(h => h.remove());
    app.querySelectorAll('.chart, .smap, .tscroll').forEach(el => {
      if (el.scrollWidth > el.clientWidth + 4) {
        const h = document.createElement('div'); h.className = 'scrollhint'; h.textContent = 'Swipe sideways to see the whole ' + (el.classList.contains('chart') ? 'chart' : el.classList.contains('smap') ? 'map' : 'table');
        el.parentNode.insertBefore(h, el);
      }
    });
  }
  let rsz = null;
  window.addEventListener('resize', () => { clearTimeout(rsz); rsz = setTimeout(markScrollables, 150); });
  const actions = {
    'home': () => { S.screen = 'home'; S.showCopy = false; render(); window.scrollTo(0, 0); },
    'ptopics': arg => { S.unit = +arg; S.screen = 'ptopics'; render(); window.scrollTo(0, 0); },
    'p-start': arg => startPractice(S.unit, arg),
    'p-pick': arg => pPick(arg),
    'p-next': () => pNext(),
    'p-topics': () => { S.unit = P ? P.unit : S.unit; S.screen = 'ptopics'; render(); window.scrollTo(0, 0); },
    'p-missed': () => { const r = scoreSet(P.qs, P.answers); startPractice(P.unit, P.topic, r.missed); P.label = 'Missed questions · ' + P.label; render(); },
    'xintro': arg => { S.unit = +arg; S.screen = 'xintro'; render(); window.scrollTo(0, 0); },
    'x-start': arg => { store.del('exam:' + arg); startExam(+arg, false); },
    'x-resume': arg => startExam(+arg, true),
    'x-pick': arg => xPick(arg),
    'x-prev': () => xGoto(E.i - 1),
    'x-next': () => xGoto(E.i + 1),
    'x-goto': arg => xGoto(+arg),
    'x-flag': () => xFlag(),
    'x-stim': () => { E.stimOff = !E.stimOff; render(); const b = document.querySelector('.stoggle'); if (b) b.focus(); },
    'x-nav': () => { E.navOpen = true; E.confirm = false; render(); },
    'x-nav-close': (arg, el, ev) => { if (ev && ev.target.closest('[data-stop]') && !ev.target.closest('[data-act="x-nav-close"]')) return; E.navOpen = false; render(); const b = document.getElementById('navbtn'); if (b) b.focus(); },
    'x-submit-ask': () => { E.confirm = true; E.navOpen = false; render(); },
    'x-confirm-close': (arg, el, ev) => { if (ev && ev.target.closest('[data-stop]') && !ev.target.closest('[data-act="x-confirm-close"]')) return; E.confirm = false; render(); const b = document.querySelector('[data-act="x-submit-ask"]'); if (b) b.focus(); },
    'x-submit': () => submitExam(false),
    'x-review': arg => { S.rvFilter = arg || 'all'; S.screen = 'xreview'; render(); window.scrollTo(0, 0); },
    'x-review-filter': arg => { S.rvFilter = arg; render(); },
    'x-back-score': () => { S.screen = 'xscore'; render(); window.scrollTo(0, 0); },
    'x-copy': () => copyResults(),
    'x-retake': () => startExam(E.unit, false)
  };
  app.addEventListener('click', ev => {
    const el = ev.target.closest('[data-act]'); if (!el || el.disabled) return;
    const fn = actions[el.dataset.act]; if (fn) fn(el.dataset.arg, el, ev);
  });
  document.addEventListener('keydown', ev => {
    if (ev.defaultPrevented || ev.metaKey || ev.ctrlKey || ev.altKey) return;
    const tag = (ev.target && ev.target.tagName || '').toLowerCase();
    if (tag === 'textarea' || tag === 'input' || tag === 'select') return;
    const k = ev.key, L = k.length === 1 ? k.toUpperCase() : '';
    if (k === 'Escape' && E && S.screen === 'exam' && (E.navOpen || E.confirm)) { actions[E.navOpen ? 'x-nav-close' : 'x-confirm-close'](); return; }
    if (S.screen === 'practice' && P) {
      const q = P.qs[P.i];
      if (LETTERS.includes(L) && !P.answers[q.id]) { ev.preventDefault(); pPick(L); }
      else if (P.answers[q.id] && (k === 'ArrowRight' || L === 'N' || (k === 'Enter' && tag !== 'button' && tag !== 'summary' && tag !== 'a'))) { ev.preventDefault(); pNext(); }
    } else if (S.screen === 'exam' && E && !E.navOpen && !E.confirm) {
      if (LETTERS.includes(L)) { ev.preventDefault(); xPick(L); }
      else if (k === 'ArrowRight' && E.i + 1 < E.qs.length) { ev.preventDefault(); xGoto(E.i + 1); }
      else if (k === 'ArrowLeft' && E.i > 0) { ev.preventDefault(); xGoto(E.i - 1); }
      else if (L === 'F' && tag !== 'button') { ev.preventDefault(); xFlag(); }
    }
  });
  document.addEventListener('visibilitychange', () => { if (!document.hidden && E && !E.submitted && S.screen === 'exam') tick(); });
  window.addEventListener('pagehide', () => persistExam());

  // test hooks (used by the headless test run; harmless in production)
  window.PE = { state: () => ({ S, P, E }), setRemaining(sec) { if (E && !E.submitted) { E.endsAt = Date.now() + sec * 1000; persistExam(); tick(); } }, store };

  render();
})();
