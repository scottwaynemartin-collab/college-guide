# The tutor's state machine

`src/engine.html` has one state object, `S`. Every view is drawn from it by `render()`, and
`render()` saves it to `localStorage` each time. Nothing else holds state. This page writes
down the states and the legal moves between them, which the code only implies.

The same facts are in a `//` comment block above `let S=` in the engine. `build.py` strips
those lines, so the embeds do not grow. `node tools/test-engine-state.js` checks that the
engine still follows this page.

## Screens (`S.k`)

| `S.k` | Screen | Drawn by |
|---|---|---|
| `-1` | Home: the FRQ menu | `home()` |
| `0` | Stimulus (or warm-up when the FRQ has no stimulus) | `stimV()` |
| `1 … n` | Part A … (part index is `S.k - 1`) | `partV(S.k-1)` |
| `n+1` | Results | `doneV()` |

`go(k)` sets `S.k`, raises `S.max`, marks `S.vis[k]`. The progress bar can jump to any
screen at any time; nothing is locked at this level.

Other top-level fields: `S.f` the current FRQ, `S.fi` its index, `S.cb` combo (points earned
in a row, reset by a miss), `S.rc` set when "Start over" was tapped once and awaits a second
tap, `S.nt` the "What do you notice?" prompts, `S.bo` the boss round on the results screen.

## A part (`S.p[i]`)

Each part walks through the six `CARDS`:

```
0 Ask  ->  1 Verb  ->  2 Learn  ->  3 Think  ->  4 Write  ->  5 Check
```

| Field | Meaning |
|---|---|
| `c` | Current card, 0–5 |
| `st` | Next Think step to reveal (starts at 1); `h` marks revealed hints as `"step-hint": 1` |
| `q` | Quick-check pick on the Learn card, `null` until answered |
| `a` | Answer text, updated live from the textarea |
| `w` | 1 while the "fill in the ___ blanks" warning shows |
| `cf` | Confidence pick, `null`, 0, 1 or 2 |
| `ck` | 1 once the answer has been checked. This is what unlocks card 5 |
| `g` | Per-rubric-line regex matches, set by `check` |
| `box` | What the student ticked on the Check card, seeded from `g` |
| `done` | 1 once the student pressed Next or See results on the Check card |
| `ok` | `earned(i)` frozen at that moment. Scoring counts `done && ok` |

### Legal moves

| Action (`data-a`) | From | Effect |
|---|---|---|
| `card` | any card | Jump to cards 0–4. The card 5 button is disabled until `ck=1` |
| `step` | Think | `st++`, reveals the next step |
| `hint` | Think | marks one hint revealed |
| `mcq` | Learn | records the quick-check pick |
| `check` | Write | answer has `___` → `w=1`, stay. Too short → stay. Else `ck=1`, `c=5`, `g` and `box` from the rubric |
| `box` | Check | toggles one tick |
| `rev` | Check | back to Write: `c=4`, `ck=0`, `done=0`. The answer is kept |
| `next` | Check | `done=1`, `ok=earned(i)`, combo updated, `go(i+2)` (the next part, or results) |
| `retry` | Results | first part with `done && !ok` goes back to Write (`c=4`, `ck=0`, `done=0`) and is shown |
| `restart` | Results | first tap sets `S.rc`; second tap wipes the save and starts the FRQ fresh |

The one real gate is **card 5 needs `ck=1`**, and only `check` sets it. Everything else is
free navigation.

## Persistence

`save()` writes `{k, max, vis, p, nt, cb}` under `localStorage['geoarcade-frq:' + FRQ title]`
on every render. `start()` restores it unless `fresh` is set.

`loadSave()` accepts a save only when `p.length` equals the FRQ's part count. So:

- changing the number of parts in an FRQ resets saved progress for it (by design);
- renaming or reshaping the fields in `S.p[i]` **silently breaks saved student work**
  unless `loadSave()` is also taught to migrate the old shape. Treat the field list above
  as a storage format, not just variable names.
