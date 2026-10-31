# Classroom Dashboard: how it works

These notes cover `teacher-dashboard.html`, so a reviewer (or future you) can check that it does what it should.

## What it is
- **One HTML file.** No build step and no libraries.
- **Two ways to run it.** As a private claude.ai artifact, or opened directly in Chrome.
- **Private storage.** Data stays in the browser's `localStorage` under the key `classroomDashboard.v1`.
- **No network calls,** with one exception: Power Hour drafting goes through the viewer's own Google Sheets connector, and only when you click **Check sheet** or **Draft**.

## Data in
Everything comes in through **Import data**: paste text, or drop CSV files.

| Kind | Header | Notes |
|---|---|---|
| **Grades** | `Student,Student ID,Class,Platform,<assignment>,…` | Class = course + period (`APHG 3B`). Prefix assignments with the course (`APHG · Unit 2 Test`). Platform = `Canvas`, `AP Classroom`, or `Gradebook` (Gradebook is TAC). Optional `School Year` column. |
| **Student Profile (CSV)** | `Student, Student ID, Class, 8th STAAR %, 8th STAAR Level, AP Exam, Q1 Grade, Q2 Grade (to date), TIA BOY 26-27 %, TIA BOY 26-27 test, Prior AP score (APHG 2026), Prior TIA BOY 25-26 %, Prior TIA EOY 25-26 %, Prior TIA test, Grade level, Q1 Unweighted GPA (all classes), Q1 Weighted GPA (all classes, est.), Q1 classes counted, Est. rank band (from Q1 weighted GPA), Est. quartile, Rank cutoffs used, AP scores (all, from Aware), PSAT history (total(EBRW/Math)), Best PSAT, SAT history, Best SAT, Q2-to-date Unweighted GPA (all classes), Q2-to-date Weighted GPA (all classes, est.), Q2 classes counted, Absences YTD (full-day), Unexcused/unresolved absences, Tardies YTD, Zeros (all classes), Classes below 70 now, Lowest class now, Power Hour drafts, Power Hour no-shows, Power Hour attended, Last Power Hour draft, Power Hour assigned now, Watch flags` | Imported from its own card, "Student Profile (CSV)", on the Import page. Each header is mapped explicitly (`PROFILE_FIELDS`). One row per student per class, matched on Student ID; Q1–Q4 class grades are stored per class. Re-importing updates and never duplicates, and blank cells keep the earlier value. Unknown columns are kept and shown under "Other profile fields". Never counted in averages. |
| **College Board reports** | AP score summary: `Course, Year, Score 5, Score 4, Score 3, Score 2, Score 1 [, Mean, Global mean, Global % 3+]`. Instructional Planning Report: `Course, Year, Section, Item, Our %, Global % [, Students]`. | Pasted into the main paste box. Year = exam year (2026 → school year 2025-26). Re-importing replaces the same course + year. Shown on Compare and used in T-TESS 4.2 (last year's results vs. projection; items 5+ points below or above global) and 1.2 (data sources). |
| **Canvas export** | "Export Entire Gradebook" CSV | Detected automatically. Sections become classes, and the "Points Possible" row is used as "out of". |
| **Anything else** | any | A one-time column picker. The layout is remembered for files with the same header. |

**Score formats:**
- `18/20` → 90%.
- `85%` → 85%.
- A plain number → percent, or divided by "out of" when one is set.
- `M` / `missing` → 0% and flagged missing.
- `EX` → excused, not counted.
- Blank → not graded.
- A score of 0 also counts as missing.

**Matching students:** by Student ID first, then by normalized name. `Last, First` and `First Last` are treated as the same.

**School years:** assignments carry a year. Only the current year (August–July, for example 2026-27) counts anywhere on the dashboard. Older years appear only in **Compare years**, and last year's students never appear on the current roster.

## The rules (all adjustable in Settings)
- **AP status** (the On track / Watch / Needs help tiles, the roster and the conference page) means one thing only: on pace to pass the AP exam. It is worked out **per class** (APHG, AP World, AP Euro alike) from **AP Classroom multiple-choice scores only**:
  - **Counted:** progress-check MCQs, and MC unit tests and retests. A retest counts as its own test.
  - **Left out:** FRQ, SAQ, LEQ and DBQ, and everything from Canvas or the Gradebook.
  - **Missing work** counts as 0 only when it's marked missing. Ungraded or blank work is skipped.
  - **Order:** by assignment order.
  - **AP on track:** MC average ≥ 55%, **or** the 2 most recent MC tests are both ≥ 55%.
  - **AP watch:** MC average from 45% to 54.9%, **or** only one of the last 2 MC tests is ≥ 55%.
  - **AP needs help:** MC average below 45%, and neither of the last 2 is ≥ 55%.
  - **No AP data:** no AP Classroom MC yet (not counted as on track).
  - **Each row shows the reason,** for example "AP on track: MC avg 58%" or "AP on track: last 2 MC 61%, 57% (avg 49%)".
  - **Students in two classes** get a status for each class. The tiles and filters use the student's lowest status.
  - **Settings:** AP on-track % (55), recent MC tests needed (2), AP watch band (10 points).
- **Context only,** never changing AP status: class grades, missing work, dropping, platform gap, AP projection, GPA, attendance, zeros, Power Hour, STAAR, TIA, PSAT/SAT, school watch flags, near-cutoff classes. These show as chips on the roster and in full on the conference page.
- **Conversation starters** (Overview): students with school watch flags or 3+ missing (adjustable).
- **Class-grade cutoff (70):** used for the Power Hour list and the "Below 70" context chip.
- **Dropping:** the average of the last 3 scores is 8 or more points below the average of the earlier scores. It needs 6 or more scores.
- **Platform gap:** platform averages 15 or more points apart. Each platform needs 2 or more scores, and missing work is left out of this check.
- **Retests:** tests and progress checks scored under 80 (the Frisco retest cap). Missing work isn't included. Never treated as tests: "Corrections", "TURN IN HERE", the LockDown Browser test, and "Fill in the Blank Review".
- **Power Hour list:** anyone under 70 in any class, grouped by class period.
- **Assignment types** (used by Compare, the Unit Tracker and AP projection):
  - Writing = SAQ, LEQ, DBQ or FRQ in the name.
  - Progress Check = "progress check" in the name, except vocabulary ones.
  - Unit Test = "test", "retest", "MC" or "MCQ".
- **Units:** taken from "Unit N", "UN", or a topic number such as "Topic Check: 2.3" (Unit 2).
- **AP projection:**
  1. **Unit MC projection** (all year): the weighted average of AP Classroom multiple-choice scores (not writing, not mocks). Unit N carries weight 1 + (N − 1) × 0.5. Writing is ignored unless "Include unit writing" is turned on in Settings.
  2. **Mock projection:** used when assignments named Mock / Practice Exam / Full-length exist. Mock MC = the average of the full-length MC tests. Mock writing = the practice-test FRQ / SAQ / DBQ / LEQ scores. These are combined with the College Board weights (editable in Settings): APHG MC 50 / FRQ 50; AP World and AP Euro MC 40 / SAQ 20 / DBQ 25 / LEQ 15. A missing part is left out and the rest scaled up, with a note such as "(no DBQ yet)".
  3. Once a mock exists it is the headline (badge "Mock"), and the Unit MC projection is shown alongside.
  4. The composite maps to a score: 85+ → 5, 70+ → 4, 55+ → 3, 40+ → 2, otherwise 1. Missing work is left out.
  5. **Compare years:** a "Mock projection vs. actual AP score" grid compares each student's prior-year mock projection with their actual AP score (Profile "Prior AP score" or "AP scores"), showing the exact-match and within-1 rates.
- **Overview:**
  - Status tiles (On Track / Watch / Needs Help / AP exam unpaid); tapping one filters the roster.
  - Roster, and "Grab these kids" with reason tags and last parent contact.
  - Action lists.
  - Charts: assignment averages, platform freshness, periods side by side, biggest changes, STAAR vs. now, heatmap.
  - A weekly summary to copy.
- **Retests:** grouped by student or by test, with a tick box when a retest is done.
- **Power Hour:** the list, plus **Draft in the Tutorials sheet**:
  1. Reads the ID column, the header row and the chosen day's column from each alphabet tab.
  2. Writes `Martin, Scott B106 <A Block|B Block|Advisory>` into empty cells only.
  3. Skips cells another teacher already filled.
  4. Warns after the 6 pm deadline the day before.
- **Missing work:** a board by class period, plus the most-missed assignments.
- **Compare years:**
  - Class average per unit for each type, this year against earlier years, with missing work left out.
  - Optional overlay of one student.
- **AP projection:** the distribution per class, with 1–2s flagged.
- **Filters:** class and period, 8th STAAR level, AP exam (paid / unpaid / opted out), estimated quartile, and has-flags.
- **Watch list card:** students with school watch flags or dashboard flags, sortable by number of flags. A school flag that already covers a dashboard flag (for example "Below 70 in a class") isn't counted twice.
- **Classes side by side:** per class, the average, status mix and missing work, plus profile averages: 8th STAAR, TIA BOY, GPA (Q2-to-date weighted, otherwise Q1) and absences.
- **Conference view** (click any student):
  - Header: name, ID, grade, classes, AP exam paid or unpaid, and watch flags as chips.
  - Grades & GPA: my-class Q1 and Q2, and all-class unweighted and weighted GPA Q1 vs. Q2-to-date with up/down arrows. Rank band and quartile, with the cutoffs used in small text.
  - Tests: 8th STAAR, TIA BOY/EOY this year vs. last year, prior AP and all AP scores, PSAT and SAT history with a small trend line, and AP Classroom progress checks.
  - Attendance & all classes: absences, unexcused, tardies, zeros, classes below 70, lowest class. Amber or red when high. Counselor shows in the header. The optional column "Classes just under a cutoff now" shows as "Close to next letter".
  - Power Hour: drafts, no-shows, attended, last draft, assigned now.
  - Agency conferencing goals: goal, action steps, check-in date, next step, support, AP skill strength / gap, notes, and per-quarter rating 1–4 with grade goal vs. actual. All saved per student. Blank fields are left off the printout.
  - Rank band and quartile boxes use the imported column names (for example "Q1 snapshot rank band (vs past cutoffs)").
  - Print / Save as PDF: a one-page summary in black and white.
  - Baseline, Academic Snapshot.
  - Agency 1–4 and grade goal vs. actual per quarter (saved).
  - Unit Tracker per class.
  - Every platform side by side with trend lines.
  - Missing work, parent contact log, and conference notes (saved).
  - Prev and Next buttons; the ← and → keys also work.
- **Import:** the Claude in Chrome prompt, paste box, file drop, school year, **Data check**, import history, and **Undo last import** (one level).
- **Settings:** rules, which overview cards show, back up, restore, sample data, erase, and **T-TESS summary**.
- **T-TESS summary** (Settings → Open T-TESS summary): one printable page per class with counts only (no student names), a date stamp, and "Evidence from Classroom Dashboard, student data on request." Organized by dimension:
  - **1.2 Data & Assessment:** data sources in use; reteach topics (units where the class AP Classroom MC average is below the on-track %); retest priority count.
  - **1.3 Knowledge of Students:** % with a full profile (8th STAAR, TIA BOY and GPA on file); prior AP on file.
  - **1.4 / 2.4 Activities / Differentiation:** reteach groups (units with 2+ students under the on-track %); Power Hour drafts and attended.
  - **2.1 / 3.3 Achieving Expectations / Classroom Culture:** % with an Agency goal; check-ins whose date has passed; % of quarter grade goals met.
  - **2.3 Communication:** parent contacts by type; parent emails drafted.
  - **2.5 Monitor & Adjust:** average AP Classroom MC change after a Power Hour draft (assignments imported after the first draft vs. before); average retest gain (MC retest vs. the same-unit original); weeks with a data refresh.
  - **3.1 Routines:** conferences marked "held", per grading period (approximate dates in `CONFIG.gradingPeriods`).
  - **4.2 Goal Setting (SLO: APHG):** % AP on track now vs. at the first MC test; TIA BOY → EOY growth; last year's AP results (typed in on the page) vs. % projected 3+.
  - **4.4 School Community:** counselor and co-teacher referrals logged.
  - **Tracked from the day the page was added:** "Mark conference held", referral buttons, parent-email drafts and assignment arrival dates.

## Artifact limits (by design)
The claude.ai artifact frame blocks several browser features, so the page works around them:
- **Pop-ups (`confirm`, `prompt`, `alert`):** replaced with dialogs built into the page.
- **File downloads:** backup and export open a box with a **Copy all** button.
- **Printing:** **Print** becomes a copyable text view. Printing works normally when the file is opened directly in Chrome.
- **Reserved link name:** claude.ai reserves `#settings`, so the Settings view uses `#options`.

## Worth checking
1. Do the status, retest and AP-projection rules match how the teacher thinks about students?
2. Is the AP projection weighting (recency, and the MC/writing split per course) sensible?
3. Spot-check one student's average by hand against Canvas, AP Classroom and TAC.
4. After a real import, look at **Data check** for ID mismatches and unrecognized prefixes.
5. Accessibility: keyboard use, contrast, and screen-reader labels.

## Known limits
- Data lives in one browser. Use **Back up…** in Settings to move it.
- **Undo last import** keeps only one step.
- Power Hour drafting has been tested against a mock of the sheet layout, not yet against the live sheet.
- Vocabulary Progress Checks still appear in Retests when under 80. Whether they should is the teacher's call.
