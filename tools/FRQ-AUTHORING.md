# Writing an FRQ for the GeoArcade FRQ Tutor

Each FRQ is one file in `src/frqs/`. Copy `u3-english-global.js` as your template: it has every field filled in, in the house voice. Read it fully before writing.

## Who this is for

A 9th/10th grader in AP Human Geography who may be confused or unmotivated. The tutor should feel like a patient private tutor sitting next to them: it anticipates what the kid is thinking, teaches every piece of content they need (so they never have to Google), and walks them through writing step by step. Warm, plain, specific. Never condescending. No jargon without a definition.

## Hard rules

- **Original content only.** Do not copy College Board questions, stimuli, or wording. Write a fresh scenario. Fictional countries/cities are fine for data tables (say so in the source line); real places are fine for history and examples.
- **Accurate.** Every fact in lessons and pop-outs must be true and standard AP Human Geography content (AMSCO / CED). When unsure, leave it out.
- **7 parts, A–G, 1 point each**, in this order of difficulty: usually A Identify, then a mix of Describe and Explain, with F or G about a limitation of the data/scale or a broader connection. At least one part must say "Using the [table/map/diagram]…".
- **Task verbs:** `Identify` (name it), `Describe` (what it is/looks like, with evidence), `Explain` (how/why, cause → effect).
- **TEA labels.** Describe/Explain parts have exactly 3 thinking steps (T1 Topic, E2 Evidence, A3 Analysis). Identify parts have exactly 2 steps. Each step has 1–2 hints that get progressively more specific; the last hint can nearly hand them the answer.
- **Model answers** for Describe/Explain are written in the class format: `T1- …reason in general words. E2- …specific proof. A3- …why it matters.` Identify model answers are one phrase or sentence. The model answer must earn the point under its own rubric regex.
- **Rubric regexes** are JavaScript regex literals, case-insensitive (`/…/i`), generous with synonyms a kid might use, and the fix-it tip (third item) says exactly what to add in one sentence. `m:"all"` means every item is needed (use for Describe/Explain); `m:"any"` means one of them is enough (use for Identify).
- **Weak answer** (`wk`) is something a real student would plausibly write that misses the point; the explanation says precisely why. It should NOT pass the rubric.
- **Sentence frame** (`fr`) uses `___` blanks and mirrors the T1-/E2-/A3- shape for Describe/Explain.
- **Quick check** (`qc`): `[question, [correct, wrong, wrong], 0, one-sentence explanation]`. The correct answer is always first in the array (the tutor shuffles).
- **Mini-lesson** (`ml`): `[title, [3–5 short sentences teaching exactly what this part needs], [[term, kid-friendly definition], …]]` with 2–3 terms.
- **Pop-outs** (`addBG`): 3–5 short sentences each, teaching background a kid would otherwise Google. Give each a unique key (check it doesn't collide with the shared keys below or another FRQ file). Reference them in the FRQ's `bg` (shown on the stimulus screen) and each part's `b`.
- **Shared pop-out keys you may reference without defining:** `frq`, `tea`, `readmap`, `readtable`, `raj`, `scale`.
- **Stimulus** (`stim`): HTML string. Tables use the `.tbl > table` markup from the template. Diagrams/maps are inline SVG with `viewBox`, `role="img"`, and a full `aria-label` describing it; keep SVG under ~4 KB, use the tutor's palette (dark navy background `#0a1d3a`/`#24304f`, cyan `#22e5ff`, yellow `#ffd23f`, pink `#ff3fa4`, green `#3ddc84`, text `#fff`/`#ffe7a6`, font `Chakra Petch,sans-serif`). Add a `<p class="src">` source/notes line and a `.legend` if needed.
- **Notice prompts** (`nt`): exactly 3 `[question, tutor's take]` pairs that make the kid look closely before any question appears.
- **Top-level fields:** `k` (card label, e.g. `"Practice FRQ · Data table"`), `t` (short catchy title), `d` (one-line description), `u` (e.g. `"Unit 5"`), `st` (stimulus title), `intro` (1–2 sentences), `stim`, `bg`, `nt`, `m` (minutes, use 20), `p` (parts).
- **Per-part fields:** `v, q, sk` (skill name for the results screen), `s` (steps), `r` (rubric), `mo` (model), `b` (pop-out keys), `th` (what a confused kid is thinking, in quotes), `co` (tutor's warm reply), `kq` (the question in plain words), `ml`, `wk`, `mw` (why the model works), `fr`, `qc`.
- **Size:** aim for 22–30 KB per file.

## Check your work

```
node tools/validate.js src/frqs/<your-file>.js
```

Fix every ERROR. Then build and open it:

```
python3 build.py
```
