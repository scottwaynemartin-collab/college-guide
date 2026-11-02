# Classroom Dashboard tests

Headless Chromium checks for `teacher-dashboard.html`, using the built-in **made-up sample data** only. Never add real student data here.

```
node tests/dashboard/run-all.js          # everything (~2–3 minutes)
node tests/dashboard/run-all.js 07 10    # only tests starting with 07 or 10
```

Needs Playwright with Chromium (`require('playwright')`). Screenshots and PDFs go to `tests/dashboard/out/` (git-ignored).
A test fails on a non-zero exit, a timeout, any page/console error (`ERR [...]` non-empty) or leaked student names on the no-name pages.
The runner also checks the conference, T-TESS, At a glance and Student view printouts are one page each (when `pdfinfo` is installed).

| Test | Covers |
|---|---|
| 01 | Every page at 1440 and 390 px, backup size |
| 02–04 | Conference page, profile fields, one-page print |
| 05–06 | AP status rule cases, unit/mock projection |
| 07 | T-TESS tab: no names, scoping, links, print |
| 08–09 | Prep card, reteach radar, retest messages, Power Hour drafts (copy, prompt, mark once) |
| 10 | At a glance, district participation import, Help, compressed backup/restore, data check |
| 11–13 | No horizontal overflow or overlapping cards; roster + side panel columns |
| 14 | Power Hour drafting into the Tutorials sheet (mock connector) |
| 15–21 | College Board, profile, unknown layouts, column picker, standard CSV imports |
| 22 | Top-bar page labels |
| 23–26 | Tooltip/UI-event safety, import edge cases, action-page fixes, missing / don't-count / Pathway / downloads |
| 27 | Student view (no names, small-group rules, bands, print), At a glance class averages + trend, Power Hour draft days, Overview chips |
