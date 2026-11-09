/* Euro Atlas · AP Practice Exam (AP European History) · app
   Screens: home → (practice topics → practice → summary) | (exam intro → exam → score → review)
   Every question belongs to a source set (data.stimuli[q.set]), like the real exam: sets of 3–4.
   Storage is wrapped in try/catch with an in-memory fallback: Google Sites serves the embed from a
   sandboxed origin where localStorage can throw. No window.top navigation. */
(function () {
  'use strict';

  /* ---- switches ---- */
  // Set to false to hide the "Estimated AP score" badge on the score report.
  const SHOW_AP_ESTIMATE = true;
  // Rough estimate only. The College Board does not publish cutoffs; these are the bands many
  // teachers use for a multiple-choice-only practice set. AP European History uses the same
  // section weights as the other AP histories (MC 40%, 55 questions in 55 minutes), so the
  // generic history bands apply.
  const AP_BANDS = [[80, 5], [65, 4], [50, 3], [35, 2], [0, 1]];

  const DATA = (window.PE_DATA && window.PE_DATA.units) || {};
  const STIM = window.PE_STIM;
  const esc = STIM.esc;
  const LETTERS = ['A', 'B', 'C', 'D'];
  // The four chronological periods of the course (Fall 2026 framework), named as on the Euro Atlas period pages.
  const PERIODS = [
    { n: 1, name: 'The Unmaking of Christendom', dates: 'c. 1450 – c. 1648', units: [1, 2] },
    { n: 2, name: 'From Divine Right to the Rights of Man', dates: 'c. 1648 – c. 1815', units: [3, 4, 5] },
    { n: 3, name: 'The Machine, the Nation, and the World', dates: 'c. 1815 – c. 1914', units: [6, 7] },
    { n: 4, name: 'From Total War to Transnational Union', dates: 'c. 1914 – present', units: [8, 9] }
  ];
  // Unit names and exam weightings from the Fall 2026 framework; b = the one-line summary from the Euro Atlas home page.
  const UNITS = [
    { n: 1, t: 'Renaissance and Exploration', w: '10–15%', b: 'Europe stops looking backward at heaven and starts looking outward at the world, and at itself.' },
    { n: 2, t: 'Age of Reformation', w: '10–15%', b: 'One church splits, and Europe spends a century learning that religion and state power cannot be separated.' },
    { n: 3, t: 'Absolutism and Constitutionalism', w: '10–15%', b: 'Two rival answers to one question (who holds sovereignty) and the wars and trade empires that paid for both.' },
    { n: 4, t: 'Scientific, Philosophical, and Political Developments', w: '10–15%', b: 'Europeans learned to trust observation over authority, then turned that habit on government, religion, and daily life.' },
    { n: 5, t: 'Conflict, Crisis, and Reaction in the Late 18th Century', w: '10–15%', b: 'Kings fought over trade and thrones until France handed politics to the nation, and Europe spent a generation reacting.' },
    { n: 6, t: 'Industrialization and Its Effects', w: '10–15%', b: 'Machines made Europe rich, crowded, and furious, and every 19th-century ideology is an answer to that.' },
    { n: 7, t: '19th-Century Perspectives and Political Developments', w: '10–15%', b: 'Nationalism built new states and new empires abroad while Europe quietly lost confidence that truth was objective.' },
    { n: 8, t: '20th-Century Global Conflicts', w: '10–15%', b: 'Industrial power turned Europe’s rivalries into total war, and the ideologies that promised order delivered genocide instead.' },
    { n: 9, t: 'Cold War and Contemporary Europe', w: '10–15%', b: 'Europe lost its empires, split in two, then rebuilt itself as a union still arguing over what Europe means.' }
  ];
  const periodDates = n => (PERIODS.find(p => p.units.includes(n)) || {}).dates || '';
  const SKILLS = { 1: 'Developments & Processes', 2: 'Sourcing & Situation', 3: 'Claims & Evidence', 4: 'Contextualization', 5: 'Making Connections' };
  const unitTitle = n => (DATA[n] && DATA[n].title) || (UNITS.find(u => u.n === n) || {}).t || ('Unit ' + n);
  const unitVars = n => `--uc:var(--u${n});--uc-soft:var(--u${n}-soft);--uc-deep:var(--u${n}-deep);--uc-text:#fff`;

  /* ---- storage (never trust it inside the Sites iframe) ---- */
  const mem = {};
  const store = {
    get(k, d) { try { const v = localStorage.getItem('eape:' + k); if (v != null) return JSON.parse(v); } catch (e) { } return (k in mem) ? mem[k] : d; },
    set(k, v) { mem[k] = v; try { localStorage.setItem('eape:' + k, JSON.stringify(v)); } catch (e) { } },
    del(k) { delete mem[k]; try { localStorage.removeItem('eape:' + k); } catch (e) { } }
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

  /* ---- sources ---- */
  const stimOf = (unit, q) => { const d = DATA[unit] || {}; return (q && q.set && d.stimuli) ? d.stimuli[q.set] || null : null; };
  const NOUN = { passage: 'passage', pair: 'two passages', image: 'image', table: 'table', bar: 'chart', schematicMap: 'map', districtMap: 'maps' };
  // "Questions 4–6 refer to the following passage." computed from where the set sits in the current list.
  function setLabel(list, q, stim) {
    const idx = list.map((o, i) => o.set === q.set ? i + 1 : 0).filter(Boolean);
    const noun = 'the following ' + (NOUN[stim && stim.type] || 'source');
    if (idx.length <= 1) return `Question ${idx[0] || ''} refers to ${noun}.`;
    return `Questions ${idx[0]}–${idx[idx.length - 1]} refer to ${noun}.`;
  }

  /* =================================================================
     shared pieces
     ================================================================= */
  // Euro Atlas mark: a globe inside a laurel wreath (brass on navy)
  const LOGO = `<svg viewBox="0 0 100 100" aria-hidden="true"><g fill="#C9A54F"><path d="M34.6 89.0Q29.7 95.2 22.1 92.6Q27.1 86.4 34.6 89.0ZM24.8 83.3Q18.7 78.1 21.6 70.7Q27.6 75.9 24.8 83.3ZM16.8 75.1Q9.3 77.7 4.3 71.5Q11.9 68.9 16.8 75.1ZM11.5 65.0Q9.1 57.4 15.5 52.7Q17.9 60.3 11.5 65.0ZM9.1 53.9Q1.3 52.1 0.4 44.2Q8.2 46.0 9.1 53.9ZM9.9 42.5Q11.9 34.8 19.9 34.1Q17.8 41.8 9.9 42.5ZM13.8 31.8Q8.1 26.1 11.5 18.9Q17.2 24.6 13.8 31.8ZM20.5 22.5Q26.3 17.1 33.4 20.7Q27.6 26.2 20.5 22.5ZM27.1 17.0Q29.9 9.6 37.9 9.7Q35.0 17.2 27.1 17.0Z"/><path d="M34.6 89.0Q29.7 95.2 22.1 92.6Q27.1 86.4 34.6 89.0ZM24.8 83.3Q18.7 78.1 21.6 70.7Q27.6 75.9 24.8 83.3ZM16.8 75.1Q9.3 77.7 4.3 71.5Q11.9 68.9 16.8 75.1ZM11.5 65.0Q9.1 57.4 15.5 52.7Q17.9 60.3 11.5 65.0ZM9.1 53.9Q1.3 52.1 0.4 44.2Q8.2 46.0 9.1 53.9ZM9.9 42.5Q11.9 34.8 19.9 34.1Q17.8 41.8 9.9 42.5ZM13.8 31.8Q8.1 26.1 11.5 18.9Q17.2 24.6 13.8 31.8ZM20.5 22.5Q26.3 17.1 33.4 20.7Q27.6 26.2 20.5 22.5ZM27.1 17.0Q29.9 9.6 37.9 9.7Q35.0 17.2 27.1 17.0Z" transform="matrix(-1 0 0 1 100 0)"/></g><g fill="none" stroke="#C9A54F" stroke-width="2" stroke-linecap="round"><path d="M40.1 90.8A41 41 0 0 1 28.3 16.2"/><path d="M40.1 90.8A41 41 0 0 1 28.3 16.2" transform="matrix(-1 0 0 1 100 0)"/><path d="M41 92.5Q50 97.5 59 92.5"/></g><circle cx="50" cy="50" r="23" fill="#1A2D52" stroke="#C9A54F" stroke-width="2.6"/><g fill="none" stroke="#E2C782" stroke-width="1.4" opacity=".85"><ellipse cx="50" cy="50" rx="9.5" ry="23"/><path d="M50 27v46M27 50h46M30.5 38.5Q50 43 69.5 38.5M30.5 61.5Q50 66 69.5 61.5"/></g></svg>`;
  const upill = n => `<span class="upill" style="${unitVars(n)}"><i aria-hidden="true"></i>Unit ${n}</span>`;
  function topbar(ctx, acts) {
    return `<header class="bar"><div class="bar-in"><button class="brand" data-act="home" aria-label="Practice Exam, back to start">${LOGO}<span><small>Euro Atlas</small><span class="bt">Practice Exam</span></span></button>${ctx ? `<div class="bar-ctx">${ctx}</div>` : ''}<div class="bar-sp"></div><div class="bar-acts">${acts || ''}</div></div></header>`;
  }
  const metaTag = (unit, q) => {
    const d = DATA[unit] || {}; const topic = (d.topics || []).find(t => t.id === q.topic);
    const sk = String(q.skill || ''); const sn = SKILLS[sk.split('.')[0]];
    return `<div class="tag-meta"><span><b>Topic ${esc(q.topic)}</b>${topic ? ' · ' + esc(topic.name) : ''}</span><span>Skill ${esc(sk)}${sn ? ' · ' + esc(sn) : ''}</span>${q.reasoning ? `<span>${esc(q.reasoning)}</span>` : ''}</div>`;
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
    return `<div class="rows">${ids.map(k => { const r = bySkill[k]; const p = pctOf(r.c, r.t); return `<div class="row"><div class="lbl"><b>${esc(k)}</b>${esc(SKILLS[k] || 'Skill ' + k)}</div><div class="trk" aria-hidden="true"><span class="${barCls(p)}" style="width:${p}%"></span></div><div class="cnt">${r.c}/${r.t}</div></div>`; }).join('')}</div>`;
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
  function stimColumn(label, stimHTML, off, act, setId) {
    return `<aside class="scol ${off ? 'off' : ''}" aria-label="Source"><div class="sticky"><div class="scol-head"><div class="setlabel">${esc(label)}</div><button class="act ghost sm stoggle" data-act="${act}" aria-expanded="${!off}">${off ? 'Show source' : 'Hide source'}</button></div><div class="stimwrap" data-set="${esc(setId || '')}">${stimHTML}</div><p class="hl-tip">Tip: select words in a passage to highlight them. Tap a highlight to remove it.</p></div></aside>`;
  }

  /* =================================================================
     home
     ================================================================= */
  function viewHome() {
    const avail = UNITS.filter(u => DATA[u.n]);
    const pq = avail.reduce((a, u) => a + DATA[u.n].practice.length, 0);
    const xq = avail.reduce((a, u) => a + DATA[u.n].exam.questions.length, 0);
    const ns = avail.reduce((a, u) => a + Object.keys(DATA[u.n].stimuli || {}).length, 0);
    // exam length for the "how it works" panel comes from the banks themselves (25 in 25 unless a bank says otherwise)
    const x0 = avail.length ? DATA[avail[0].n].exam : null;
    const xn = x0 ? x0.questions.length : 25, xm = x0 ? (x0.timeMinutes || 25) : 25;
    const kpi = (v, k) => `<div class="kpi"><span class="v">${v}</span><span class="k">${k}</span></div>`;
    return topbar('', '') + `<header class="hero"><div class="hero-in"><div class="hero-txt"><div class="eyebrow">Euro Atlas · AP® European History</div><h1>Practice <em>Exam</em></h1><p class="sub">Read the source, then answer. Practice by topic with every answer explained, then take a timed exam built like the real one.</p>
        <div class="kpis" aria-label="What's inside">${kpi(avail.length, avail.length === 1 ? 'Unit ready' : 'Units ready')}${kpi(pq, 'Practice questions')}${kpi(xq, 'Exam questions')}${kpi(ns, 'Sources')}</div></div><div class="rose" aria-hidden="true">${LOGO}</div></div></header>
      <main id="main" class="home">
      ${PERIODS.map(per => `<section class="period" aria-label="Period ${per.n}: ${esc(per.name)}"><div class="period-head"><span class="pn" aria-hidden="true">${per.n}</span><div class="ptxt"><div class="eyebrow">Period ${per.n} · ${esc(per.dates)}</div><h2><span class="sr-only">Period ${per.n}: </span>${esc(per.name)}</h2></div><span class="rule" aria-hidden="true"></span></div><div class="ugrid">${per.units.map(n => unitCard(UNITS.find(u => u.n === n))).join('')}</div></section>`).join('')}
      <section class="how" aria-label="How it works">
        <div class="panel"><span class="stepn" aria-hidden="true">1</span><h3>Practice a topic</h3><p>Every question comes with a source, just like the real exam: a primary text, a historian's writing, an image, or data. Answer one question at a time, untimed. Use a hint if you're stuck, and see why the right answer is right and why each wrong one is wrong.</p></div>
        <div class="panel"><span class="stepn" aria-hidden="true">2</span><h3>Take the timed exam</h3><p>${xn} questions in ${xm} minutes${xn === xm ? ", the real exam's one-minute pace" : ''}. Questions come in sets of 3–4 per source, four choices each. Flag questions, cross out choices, jump around, and change answers until you submit.</p></div>
        <div class="panel"><span class="stepn" aria-hidden="true">3</span><h3>Read your report</h3><p>See your score by topic and by historical thinking skill, then review every question with notes on all four choices. Retake it, or bring the ones you missed to your AP European History teacher.</p></div>
      </section>
      <p class="note-line">Questions are original and written in the style of the AP exam; they are not College Board questions. Primary sources are public-domain translations, lightly adapted for length and modern spelling.</p>
    </main><footer class="foot"><span class="ft">Euro Atlas</span>Questions © Scott Martin · <a href="mailto:APandAbroad@gmail.com">APandAbroad@gmail.com</a></footer>`;
  }
  function unitCard(u) {
    const d = DATA[u.n];
    const blurb = (d && d.blurb) || u.b;
    if (!d) return `<article class="ucd soon" style="${unitVars(u.n)}" aria-disabled="true"><span class="tag" aria-hidden="true"></span><div class="uh"><span class="un" aria-hidden="true">${u.n}</span><span class="wt">${esc(u.w)} of exam</span></div><h3><span class="sr-only">Unit ${u.n}: </span>${esc(u.t)}</h3>${blurb ? `<p class="ublurb">${esc(blurb)}</p>` : ''}<span class="soonpill">Coming soon</span></article>`;
    const best = store.get('best:' + u.n), prog = store.get('exam:' + u.n);
    const x = d.exam || {}; const xn = (x.questions || []).length;
    return `<article class="ucd live" style="${unitVars(u.n)}"><span class="tag" aria-hidden="true"></span><div class="uh"><span class="un" aria-hidden="true">${u.n}</span>${prog ? `<span class="resume">⏱ Exam in progress</span>` : (best ? `<span class="best">Best exam <span class="ok">${best.correct}/${best.total}</span> · ${best.pct}%</span>` : `<span class="wt">${esc(u.w)} of exam</span>`)}</div>
      <h3><span class="sr-only">Unit ${u.n}: </span>${esc(d.title || u.t)}</h3>${blurb ? `<p class="ublurb">${esc(blurb)}</p>` : ''}
      <div class="ubtns"><button class="act unit" data-act="ptopics" data-arg="${u.n}"><span>Practice</span><small>${d.practice.length} questions</small></button>
      <button class="act ghost" data-act="xintro" data-arg="${u.n}"><span>${prog ? 'Resume timed exam' : 'Timed Exam'}</span><small>${xn} questions · ${x.timeMinutes || 25} min</small></button></div></article>`;
  }

  /* =================================================================
     practice
     ================================================================= */
  function viewTopics() {
    const unit = S.unit, d = DATA[unit];
    const counts = {}; d.practice.forEach(q => { counts[q.topic] = (counts[q.topic] || 0) + 1; });
    const chip = (id, name, n) => `<button class="tchip" style="${unitVars(unit)}" data-act="p-start" data-arg="${esc(id)}" ${n ? '' : 'disabled'}><span class="id">${esc(id === 'all' ? '★' : id)}</span><span>${esc(name)}</span><span class="n">${n}</span></button>`;
    return topbar(`${upill(unit)}<span class="ellip">Practice</span>`, `<button class="act quiet sm" data-act="home">← All units</button>`) + `<main id="main"><div class="phead" style="${unitVars(unit)}"><div class="eyebrow">Unit ${unit} · ${esc(d.title)}${(d.period || periodDates(unit)) ? ' · ' + esc(d.period || periodDates(unit)) : ''}</div><h2>Practice by topic</h2><p class="muted">Untimed. Read the source, answer one question at a time, and see the answer explained right after you pick. Choose a topic or practice everything.</p>
      <div class="tchips" role="group" aria-label="Topics">${chip('all', 'All topics', d.practice.length)}${(d.topics || []).map(t => chip(t.id, t.name, counts[t.id] || 0)).join('')}</div></div></main>`;
  }
  function startPractice(unit, topic, qs) {
    const d = DATA[unit];
    const list = qs || (topic === 'all' ? d.practice.slice() : d.practice.filter(q => q.topic === topic));
    if (!list.length) return;
    [...stimCache.keys()].forEach(k => { if (k.startsWith('practice:')) stimCache.delete(k); });
    P = { unit, topic, qs: list, i: 0, answers: {}, hints: {}, stimOff: false, label: topic === 'all' ? 'All topics' : (((d.topics || []).find(t => t.id === topic) || {}).name || topic) };
    S.screen = 'practice'; render(); focusQ();
  }
  function viewPractice() {
    const unit = P.unit, q = P.qs[P.i], n = P.qs.length, pick = P.answers[q.id];
    const done = Object.keys(P.answers).length;
    const stim = stimOf(unit, q);
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
        <div class="pnext"><div class="hint">${pick ? '<span class="kbd">Enter</span> or <span class="kbd">→</span> for next' : ''}</div><button class="act primary" data-act="p-next" id="pnext">${P.i + 1 < n ? (P.qs[P.i + 1].set === q.set ? 'Next question (same source) →' : 'Next question →') : 'See my summary →'}</button></div>`;
    }
    const hint = !pick && q.hint ? `<details class="phint" ${P.hints[q.id] ? 'open' : ''} data-hint="${esc(q.id)}"><summary>💡 Need a hint?</summary><p>${esc(q.hint)}</p></details>` : '';
    const stimCol = stim ? stimColumn(setLabel(P.qs, q, stim), STIM.render(stim, { glossary: true }), P.stimOff, 'p-stim', q.set) : '';
    return topbar(`${upill(unit)}<span class="ellip">Practice · ${esc(P.label)}</span>`, `<button class="act quiet sm" data-act="p-topics">Topics</button><button class="act quiet sm" data-act="home">Units</button>`) + `<main id="main" class="pmain" style="${unitVars(unit)}">
      <div class="phead"><div class="prog-row"><span>Question ${P.i + 1} of ${n}</span><div class="prog" role="progressbar" aria-valuemin="0" aria-valuemax="${n}" aria-valuenow="${done}" aria-label="Answered ${done} of ${n}"><span style="width:${(done / n) * 100}%"></span></div><span>${done} answered</span></div></div>
      <div class="xwrap ${stim ? 'has-stim' : ''}">${stimCol}<article class="qcard" id="qcard"><h2 class="qn" id="qhead" tabindex="-1">Question ${P.i + 1}<span class="sr-only"> of ${n}</span></h2><p class="stem">${esc(q.stem)}</p>
      <div class="opts" role="group" aria-label="Answer choices">${opts}</div>${hint}${fb}
      ${pick ? '' : `<div class="pnext"><div class="hint">Press <span class="kbd">A</span>–<span class="kbd">D</span> to answer</div></div>`}</article></div></main>`;
  }
  function burst() {
    if (reducedMotion()) return '';
    const cols = ['#B8923A', '#D4B05E', '#1A2D52', '#3E6B4F', '#8B2A2A', '#6B3A5B'];
    return `<span class="burst" aria-hidden="true">${Array.from({ length: 8 }, (_, i) => { const a = i / 8 * Math.PI * 2, d = 34 + (i % 2) * 10; return `<i style="--dx:${Math.round(Math.cos(a) * d)}px;--dy:${Math.round(Math.sin(a) * d)}px;--c:${cols[i % cols.length]};animation-delay:${i * 15}ms"></i>`; }).join('')}</span>`;
  }
  function viewSummary() {
    const unit = P.unit, r = scoreSet(P.qs, P.answers);
    return topbar(`${upill(unit)}<span class="ellip">Practice · ${esc(P.label)}</span>`, `<button class="act quiet sm" data-act="home">Units</button>`) + `<main id="main" style="${unitVars(unit)}"><div class="score">
      <section class="panel"><div class="sumhead"><div class="eyebrow">Practice set complete</div><div class="big" aria-label="${r.correct} of ${r.total} correct">${r.correct}<small>/${r.total}</small></div><p>${r.pct}% correct · ${esc(P.label)}</p></div>
      <h3>By topic</h3>${topicRows(unit, r.byTopic)}
      <h3 style="margin-top:20px">By skill</h3>${skillRows(r.bySkill)}
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
    const sameSet = P.i + 1 < P.qs.length && P.qs[P.i + 1].set === q.set;
    const keep = sameSet ? saveStimScroll() : null;
    if (P.i + 1 < P.qs.length) { P.i++; render(); restoreStimScroll(keep); focusQ(); scrollToQuestion(sameSet); }
    else { S.screen = 'psummary'; render(); window.scrollTo(0, 0); }
  }
  const focusQ = () => { const h = document.getElementById('qhead'); if (h) h.focus({ preventScroll: true }); };
  // Desktop: source and question sit side by side, so go to the top. Phone (stacked): for the 2nd+ question
  // on the same source, jump straight to the question; the source is still right above it.
  const stacked = () => { try { return window.matchMedia('(max-width: 899px)').matches; } catch (e) { return false; } };
  function scrollToQuestion(sameSet) {
    const h = document.getElementById('qhead');
    if (sameSet && stacked() && h) { const top = h.getBoundingClientRect().top + window.scrollY - 70; window.scrollTo({ top: Math.max(0, top), behavior: 'auto' }); }
    else window.scrollTo({ top: 0, behavior: 'auto' });
  }
  // keep the reader's place in a long passage when moving between questions of the same set
  const saveStimScroll = () => { const s = app.querySelector('.scol .sticky'); return s ? s.scrollTop : null; };
  const restoreStimScroll = v => { if (v == null) return; const s = app.querySelector('.scol .sticky'); if (s) s.scrollTop = v; };

  /* =================================================================
     exam
     ================================================================= */
  function viewIntro() {
    const unit = S.unit, d = DATA[unit], x = d.exam, saved = store.get('exam:' + unit);
    const n = x.questions.length;
    const sets = new Set(x.questions.map(q => q.set)).size;
    return topbar(`${upill(unit)}<span class="ellip">Timed Exam</span>`, `<button class="act quiet sm" data-act="home">← All units</button>`) + `<main id="main"><div class="xintro">
      <div><div class="eyebrow">Unit ${unit} · Timed exam</div><h2>${esc(x.title || d.title)}</h2></div>
      <div class="facts" aria-label="Exam format"><span>${n} questions</span><span>${x.timeMinutes} minutes</span><span>${sets} sources</span><span>4 choices</span><span>no penalty for guessing</span></div>
      <div class="dir"><strong>Directions.</strong> ${esc(x.directions)}</div>
      <ul><li>Each source has its own set of questions. On a computer the source stays on the left while you answer on the right.</li><li>The timer starts when you press Start and keeps running if you leave the page.</li><li>Flag a question to come back to it, and use the ⊘ button to cross out choices you've ruled out.</li><li>You can change any answer until you submit. The exam submits itself when time runs out.</li></ul>
      <div class="acts">${saved ? `<button class="act primary" data-act="x-resume" data-arg="${unit}">Resume exam</button><button class="act ghost" data-act="x-start" data-arg="${unit}">Start over</button>` : `<button class="act primary" data-act="x-start" data-arg="${unit}">Start exam</button>`}</div>
      ${saved ? `<p class="note">You have an exam in progress with ${Object.keys(saved.answers || {}).length} of ${n} answered. Resuming keeps your answers and the original clock.</p>` : ''}
    </div></main>`;
  }
  function startExam(unit, resume) {
    const d = DATA[unit], x = d.exam;
    const saved = resume ? store.get('exam:' + unit) : null;
    const now = Date.now();
    [...stimCache.keys()].forEach(k => { if (k.startsWith('exam:')) stimCache.delete(k); });
    E = { unit, qs: x.questions.slice(), answers: {}, flags: {}, elim: {}, i: 0, startedAt: now, endsAt: now + (x.timeMinutes || 25) * 60000, navOpen: false, confirm: false, stimOff: false, submitted: false, announced: {} };
    if (saved && saved.endsAt) Object.assign(E, { answers: saved.answers || {}, flags: saved.flags || {}, elim: saved.elim || {}, i: Math.min(saved.i || 0, E.qs.length - 1), startedAt: saved.startedAt || now, endsAt: saved.endsAt });
    S.screen = 'exam'; S.unit = unit; persistExam(); render(); window.scrollTo(0, 0); startTimer();
    if (E.endsAt <= Date.now()) submitExam(true);
  }
  const persistExam = () => { if (!E || E.submitted) return; store.set('exam:' + E.unit, { answers: E.answers, flags: E.flags, elim: E.elim, i: E.i, startedAt: E.startedAt, endsAt: E.endsAt }); };
  function timerHTML() {
    const rem = Math.max(0, E.endsAt - Date.now());
    const hid = E.hideTimer && rem > 300000;
    return `<div class="timer ${rem <= 60000 ? 'crit' : rem <= 300000 ? 'warn' : ''} ${hid ? 'hid' : ''}" id="tmr" role="timer" aria-live="polite" aria-atomic="true"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M12 7v5l3.5 2" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg><span class="digits" aria-hidden="true">${mmss(rem)}</span><span class="sr-only" id="tmrsr">${mmss(rem)} remaining</span></div><button class="act quiet sm tmr-tg" data-act="x-timer" aria-pressed="${!!E.hideTimer}">${E.hideTimer ? 'Show' : 'Hide'}</button>`;
  }
  function viewExam() {
    const q = E.qs[E.i], n = E.qs.length, pick = E.answers[q.id], stim = stimOf(E.unit, q), flagged = !!E.flags[q.id];
    const answered = Object.keys(E.answers).length;
    const el = E.elim[q.id] || {};
    const opts = LETTERS.map(L => `<div class="xrow ${el[L] ? 'out' : ''}"><button class="xopt" role="radio" aria-checked="${pick === L}" data-act="x-pick" data-arg="${L}"><span class="ltr" aria-hidden="true">${L}</span><span class="txt"><span class="sr-only">${L}. </span>${esc(q.options[L])}${el[L] ? '<span class="sr-only"> (crossed out)</span>' : ''}</span></button><button class="elim" data-act="x-elim" data-arg="${L}" aria-pressed="${!!el[L]}" aria-label="${el[L] ? 'Undo cross out' : 'Cross out'} choice ${L}" title="${el[L] ? 'Undo' : 'Cross out this choice'}">${el[L] ? 'Undo' : '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M6 18 18 6" stroke="currentColor" stroke-width="2"/></svg>'}</button></div>`).join('');
    const stimCol = stim ? stimColumn(setLabel(E.qs, q, stim), STIM.render(stim, { glossary: true }), E.stimOff, 'x-stim', q.set) : '';
    const nav = E.navOpen ? `<div class="veil" data-act="x-nav-close"><div class="drawer" role="dialog" aria-modal="true" aria-label="Question navigator" data-stop="1"><h3>Questions <button class="act quiet sm" data-act="x-nav-close" aria-label="Close navigator">✕</button></h3>
        <div class="navgrid">${E.qs.map((o, i) => `<button class="navq ${E.answers[o.id] ? 'ans' : ''} ${E.flags[o.id] ? 'flag' : ''} ${i === E.i ? 'cur' : ''}" data-act="x-goto" data-arg="${i}" aria-label="Question ${i + 1}, ${E.answers[o.id] ? 'answered' : 'unanswered'}${E.flags[o.id] ? ', flagged' : ''}${i === E.i ? ', current' : ''}" ${i === E.i ? 'aria-current="true"' : ''}>${i + 1}</button>`).join('')}</div>
        <div class="navkey"><span><i class="ans"></i>Answered (${answered})</span><span><i></i>Unanswered (${n - answered})</span><span><i class="flag"></i>Flagged (${Object.keys(E.flags).length})</span></div>
        <div style="margin-top:auto" class="acts"><button class="act primary wide" data-act="x-submit-ask">Submit exam</button></div></div></div>` : '';
    const unanswered = E.qs.map((o, i) => E.answers[o.id] ? null : i + 1).filter(Boolean);
    const flags = E.qs.map((o, i) => E.flags[o.id] ? i + 1 : null).filter(Boolean);
    const confirm = E.confirm ? `<div class="veil center" data-act="x-confirm-close"><div class="sheet" role="dialog" aria-modal="true" aria-labelledby="cfh" data-stop="1"><h3 id="cfh">Submit your exam?</h3>
        <div class="list">${unanswered.length ? `<div><b>${unanswered.length} unanswered:</b><div class="nums">${unanswered.map(x => `<span>${x}</span>`).join('')}</div></div>` : '<div><b>All questions answered.</b></div>'}${flags.length ? `<div><b>${flags.length} flagged:</b><div class="nums">${flags.map(x => `<span class="f">${x}</span>`).join('')}</div></div>` : ''}<div class="muted small">There is no penalty for guessing. Once you submit you cannot change answers.</div></div>
        <div class="acts end"><button class="act ghost" data-act="x-confirm-close" id="cfback">Keep working</button><button class="act primary" data-act="x-submit">Submit exam</button></div></div></div>` : '';
    return `<header class="xtop"><div class="xtop-in"><div class="who">${upill(E.unit)}<span class="ellip">Timed exam</span></div><div class="qpos"><span class="long">Question ${E.i + 1} of ${n}</span><span class="short" aria-hidden="true">${E.i + 1}<span class="muted">/${n}</span></span></div><div class="bar-sp"></div>${timerHTML()}<button class="act ghost sm" id="navbtn" data-act="x-nav" aria-haspopup="dialog" aria-expanded="${E.navOpen}" aria-label="Questions navigator"><span class="long">Questions</span><svg class="ic short" viewBox="0 0 24 24" aria-hidden="true"><g fill="currentColor"><rect x="3" y="3" width="8" height="8" rx="2"/><rect x="13" y="3" width="8" height="8" rx="2"/><rect x="3" y="13" width="8" height="8" rx="2"/><rect x="13" y="13" width="8" height="8" rx="2"/></g></svg></button><button class="act gold sm" data-act="x-submit-ask">Submit</button></div></header>
      <main id="main"><div class="xwrap ${stim ? 'has-stim' : ''}">${stimCol}<section class="xq" aria-labelledby="qhead"><h2 class="qn" id="qhead" tabindex="-1">Question ${E.i + 1}${flagged ? '<span class="flagged-note"> · ⚑ Flagged</span>' : ''}</h2><p class="stem">${esc(q.stem)}</p>
        <div class="xopts" role="radiogroup" aria-label="Answer choices">${opts}</div>
        <div class="xnav"><button class="act ghost" data-act="x-prev" ${E.i === 0 ? 'disabled' : ''}>← Previous</button><div class="mid"><button class="act ghost sm" data-act="x-flag" aria-pressed="${flagged}">⚑ ${flagged ? 'Flagged' : 'Flag'}</button></div>${E.i + 1 < n ? `<button class="act primary" data-act="x-next">Next →</button>` : `<button class="act primary" data-act="x-submit-ask">Review &amp; submit</button>`}</div></section></div></main>${nav}${confirm}`;
  }
  function xGoto(i) {
    const to = Math.max(0, Math.min(E.qs.length - 1, i));
    const sameSet = E.qs[to].set === E.qs[E.i].set;
    const keep = sameSet ? saveStimScroll() : null;
    E.i = to; E.navOpen = false; persistExam(); render(); restoreStimScroll(keep); focusQ();
    scrollToQuestion(sameSet);
  }
  function xPick(L) {
    const q = E.qs[E.i]; if (!q.options[L]) return;
    E.answers[q.id] = L;
    if (E.elim[q.id] && E.elim[q.id][L]) { delete E.elim[q.id][L]; persistExam(); const keep = saveStimScroll(); render(); restoreStimScroll(keep); const b = document.querySelector(`.xopt[data-arg="${L}"]`); if (b) b.focus({ preventScroll: true }); return; }
    persistExam();
    document.querySelectorAll('.xopt').forEach(b => b.setAttribute('aria-checked', String(b.dataset.arg === L)));
  }
  function xElim(L) {
    const q = E.qs[E.i]; const m = E.elim[q.id] || (E.elim[q.id] = {});
    if (m[L]) delete m[L]; else { m[L] = true; if (E.answers[q.id] === L) delete E.answers[q.id]; }
    persistExam(); const keep = saveStimScroll(); render(); restoreStimScroll(keep);
    const b = document.querySelector(`.elim[data-arg="${L}"]`); if (b) b.focus({ preventScroll: true });
    announce(m[L] ? `Choice ${L} crossed out` : `Choice ${L} restored`);
  }
  function xFlag() {
    const q = E.qs[E.i]; if (E.flags[q.id]) delete E.flags[q.id]; else E.flags[q.id] = true;
    persistExam(); const keep = saveStimScroll(); render(); restoreStimScroll(keep); announce(E.flags[q.id] ? `Question ${E.i + 1} flagged` : `Flag removed from question ${E.i + 1}`);
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
      el.classList.toggle('hid', !!E.hideTimer && rem > 300000);
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
        ${SHOW_AP_ESTIMATE ? `<div class="apbadge" role="note"><span class="l">Estimated AP score</span><span class="n">${ap}</span><span class="d">Rough estimate from your multiple-choice percent. The College Board does not publish cutoffs, and the real exam also scores your essays.</span></div>` : ''}
        <div class="acts center" style="margin-top:20px"><button class="act primary" data-act="x-review" data-arg="all">Review all ${n}</button>${r.missed.length ? `<button class="act ghost" data-act="x-review" data-arg="missed">Missed only (${r.missed.length})</button>` : ''}</div></section>
      <div class="two"><section class="panel"><h3>By topic</h3>${topicRows(unit, r.byTopic)}</section><section class="panel"><h3>By historical thinking skill</h3>${skillRows(r.bySkill)}</section></div>
      <section class="panel"><div class="acts between"><div class="acts"><button class="act ghost" data-act="x-copy">Copy my results</button><button class="act ghost" data-act="x-retake">Retake</button></div><button class="act soft" data-act="home">Back to units</button></div>
        ${S.showCopy ? `<div class="copybox" style="margin-top:14px"><div class="small muted">Copying was blocked here, so select the text below and copy it yourself (Ctrl/Cmd + C).</div><textarea id="copyta" readonly aria-label="Results summary">${esc(resultsText())}</textarea></div>` : ''}</section></div></main>`;
  }
  function resultsText() {
    const r = E.result, d = DATA[E.unit];
    const lines = [`AP European History Practice Exam · Unit ${E.unit}: ${d.title}`, `Score: ${r.correct}/${r.total} (${r.pct}%)${SHOW_AP_ESTIMATE ? ` · Estimated AP score: ${apEstimate(r.pct)} (rough estimate)` : ''}`, `Time used: ${mmss(r.timeUsed)} of ${d.exam.timeMinutes}:00${r.auto ? ' (auto-submitted)' : ''}`, '', 'By topic:'];
    (d.topics || []).forEach(t => { const x = r.byTopic[t.id]; if (x) lines.push(`  ${t.id} ${t.name}: ${x.c}/${x.t}`); });
    lines.push('', 'By skill:');
    Object.keys(r.bySkill).sort().forEach(k => lines.push(`  ${k}. ${SKILLS[k] || 'Skill ' + k}: ${r.bySkill[k].c}/${r.bySkill[k].t}`));
    lines.push('', `Missed: ${r.missed.length ? r.missed.map(q => E.qs.indexOf(q) + 1).join(', ') : 'none'}`, '', 'Euro Atlas · https://sites.google.com/view/ap-euro-atlas');
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
      const st = stimOf(unit, q); let stimHTML = '';
      if (st) {
        const lbl = setLabel(E.qs, q, st);
        if (seenSets[q.set]) stimHTML = `<details class="more"><summary>Show the source again (${esc(lbl.replace(/\s*refers? to.*$/i, ''))})</summary><div class="inner">${STIM.render(st, { glossary: true })}</div></details>`;
        else { stimHTML = `<div class="setlabel">${esc(lbl)}</div>${STIM.render(st, { glossary: true })}`; seenSets[q.set] = true; }
      }
      return `<article class="rv ${state}" id="rv${i + 1}"><header><span class="rn">Question ${i + 1}</span><span class="rvb ${state}">${state === 'ok' ? '✓ Correct' : state === 'bad' ? '✗ Missed' : '– Not answered'}</span>${metaTag(unit, q)}</header>${stimHTML}<p class="stem">${esc(q.stem)}</p>
        <ol class="rvopts" aria-label="Answer choices">${LETTERS.map(L => { const isC = L === q.answer, isP = L === pick; const cls = isC ? 'is-correct' : isP ? 'is-pick' : ''; const mk = isC && isP ? '✓ Your answer · correct' : isC ? '✓ Correct answer' : isP ? '✗ Your answer' : ''; return `<li class="${cls}"><span class="ltr" aria-hidden="true">${L}</span><div><span class="sr-only">${L}. </span>${esc(q.options[L])}${mk ? `<span class="mk">${mk}</span>` : ''}</div></li>`; }).join('')}</ol>
        <div class="fbk ${ok ? 'ok' : 'bad'}"><div class="ico" aria-hidden="true">${ok ? '✓' : '✗'}</div><div class="body"><h4>${ok ? 'Why this is right' : `The answer is ${q.answer}`}</h4><p class="exp">${esc(q.explanation)}</p>
        ${q.rationales ? `<details class="more"><summary>Notes on every choice</summary><div class="inner">${LETTERS.map(L => `<div class="rat ${L === q.answer ? 'correct' : ''}"><span class="ltr" aria-hidden="true">${L}</span><div><b>${L}.</b> ${esc(q.rationales[L] || '')}</div></div>`).join('')}</div></details>` : ''}</div></div></article>`;
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
    const cols = ['#B8923A', '#D4B05E', '#1A2D52', '#8B2A2A', '#3E6B4F', '#6B3A5B'];
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
    keepStim();
    markScrollables();
    if (S.screen === 'exam') {
      if (E.navOpen) { const f = app.querySelector('.drawer .navq.cur') || app.querySelector('.drawer button'); if (f) f.focus(); }
      else if (E.confirm) { const f = document.getElementById('cfback'); if (f) f.focus(); }
    }
  }
  // Keep the same source element while moving between questions of one set, so highlights stay put.
  const stimCache = new Map();
  function keepStim() {
    if (S.screen !== 'exam' && S.screen !== 'practice') return;
    const w = app.querySelector('.stimwrap[data-set]'); if (!w || !w.dataset.set) return;
    const key = S.screen + ':' + w.dataset.set, old = stimCache.get(key);
    if (old && old !== w) w.replaceWith(old); else stimCache.set(key, w);
  }
  /* ---- highlighter (passages only), like Bluebook's highlight tool ---- */
  let hlBtn = null;
  function hlRange() {
    const sel = window.getSelection && window.getSelection();
    if (!sel || sel.rangeCount === 0 || sel.isCollapsed) return null;
    const r = sel.getRangeAt(0);
    const p1 = r.startContainer.parentElement && r.startContainer.parentElement.closest('.psg-text p');
    const p2 = r.endContainer.parentElement && r.endContainer.parentElement.closest('.psg-text p');
    if (!p1 || p1 !== p2 || !app.contains(p1) || !p1.closest('.scol')) return null;
    if (!r.toString().trim()) return null;
    return r;
  }
  function placeHl() {
    const r = hlRange();
    if (!r) { if (hlBtn) hlBtn.hidden = true; return; }
    if (!hlBtn) {
      hlBtn = document.createElement('button'); hlBtn.type = 'button'; hlBtn.className = 'hlbtn'; hlBtn.textContent = '🖍 Highlight';
      hlBtn.addEventListener('mousedown', e => e.preventDefault());
      hlBtn.addEventListener('click', () => { const rr = hlRange(); if (rr) { const m = document.createElement('mark'); m.className = 'hl'; m.title = 'Tap to remove highlight'; m.appendChild(rr.extractContents()); rr.insertNode(m); window.getSelection().removeAllRanges(); announce('Highlighted'); } hlBtn.hidden = true; });
      document.body.appendChild(hlBtn);
    }
    const b = r.getBoundingClientRect();
    hlBtn.hidden = false;
    hlBtn.style.left = Math.max(8, Math.min(innerWidth - 130, b.left + b.width / 2 - 60)) + 'px';
    hlBtn.style.top = Math.max(8, b.top - 46) + 'px';
  }
  document.addEventListener('mouseup', () => setTimeout(placeHl, 0));
  document.addEventListener('touchend', () => setTimeout(placeHl, 250));
  document.addEventListener('selectionchange', () => { if (hlBtn && !hlBtn.hidden && !hlRange()) hlBtn.hidden = true; });
  window.addEventListener('scroll', () => { if (hlBtn) hlBtn.hidden = true; }, true);
  app.addEventListener('click', ev => {
    const m = ev.target.closest && ev.target.closest('mark.hl'); if (!m) return;
    const sel = window.getSelection(); if (sel && !sel.isCollapsed) return;
    const par = m.parentNode; while (m.firstChild) par.insertBefore(m.firstChild, m); m.remove(); par.normalize(); announce('Highlight removed');
  });

  // Charts and tables keep a minimum width so labels stay legible; on phones they scroll sideways.
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
  app.addEventListener('toggle', ev => { const d = ev.target; if (d && d.dataset && d.dataset.hint && P) P.hints[d.dataset.hint] = d.open; }, true);
  const actions = {
    'home': () => { S.screen = 'home'; S.showCopy = false; render(); window.scrollTo(0, 0); },
    'ptopics': arg => { S.unit = +arg; S.screen = 'ptopics'; render(); window.scrollTo(0, 0); },
    'p-start': arg => startPractice(S.unit, arg),
    'p-pick': arg => pPick(arg),
    'p-next': () => pNext(),
    'p-stim': () => { P.stimOff = !P.stimOff; render(); const b = document.querySelector('.stoggle'); if (b) b.focus(); },
    'p-topics': () => { S.unit = P ? P.unit : S.unit; S.screen = 'ptopics'; render(); window.scrollTo(0, 0); },
    'p-missed': () => { const r = scoreSet(P.qs, P.answers); const lbl = P.label; startPractice(P.unit, P.topic, r.missed); P.label = 'Missed questions · ' + lbl; render(); },
    'xintro': arg => { S.unit = +arg; S.screen = 'xintro'; render(); window.scrollTo(0, 0); },
    'x-start': arg => { store.del('exam:' + arg); startExam(+arg, false); },
    'x-resume': arg => startExam(+arg, true),
    'x-pick': arg => xPick(arg),
    'x-elim': arg => xElim(arg),
    'x-prev': () => xGoto(E.i - 1),
    'x-next': () => xGoto(E.i + 1),
    'x-goto': arg => xGoto(+arg),
    'x-flag': () => xFlag(),
    'x-timer': () => { E.hideTimer = !E.hideTimer; const el = document.getElementById('tmr'); if (el) el.classList.toggle('hid', E.hideTimer && E.endsAt - Date.now() > 300000); const b = document.querySelector('.tmr-tg'); if (b) { b.textContent = E.hideTimer ? 'Show' : 'Hide'; b.setAttribute('aria-pressed', String(E.hideTimer)); } },
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
