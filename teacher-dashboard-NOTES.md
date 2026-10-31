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
- **AP status** (the On track / Watch / Needs help tiles, the roster and the conference page) means one thing only: on pace to pass the AP exam. It is worked out **per class** (APHG, AP World, AP Euro alike) from **one source of truth: AP Classroom unit MC tests and retests** (plus full-length mock MC when present):
  - **Unit MC test** = source AP Classroom, "Unit N" in the name, and "test", "retest", "MC" or "MCQ". A retest counts as its own test, in order.
  - **Raw scores only:** the AP Classroom raw % is used, never a curved Gradebook/TAC copy of the same test. Shown as "raw MC %".
  - **Left out of the math (shown as context only):** Progress Check MCQs, FRQ/SAQ/LEQ/DBQ, and everything from Canvas or the Gradebook.
  - **Settings toggle:** "Count progress checks in AP status" (default off) adds AP Classroom progress-check MCQs back in.
  - **Missing work** counts as 0 only when it's marked missing. Ungraded or blank work is skipped.
  - **Order:** by assignment order.
  - **AP on track:** MC average ≥ 55%, **or** the 2 most recent MC tests are both ≥ 55%.
  - **AP watch:** MC average from 45% to 54.9%, **or** only one of the last 2 MC tests is ≥ 55%.
  - **AP needs help:** MC average below 45%, and neither of the last 2 is ≥ 55%.
  - **No AP data:** no AP Classroom unit MC test yet (not counted as on track).
  - **Each row shows the reason,** for example "AP on track: raw MC avg 58%" or "AP on track: last 2 raw MC 61%, 57% (avg 49%)".
  - **Students in two classes** get a status for each class. The tiles and filters use the student's lowest status.
  - **Settings:** AP on-track % (55), recent MC tests needed (2), AP watch band (10 points).
- **Context only,** never changing AP status: class grades, missing work, dropping, platform gap, AP projection, GPA, attendance, zeros, Power Hour, STAAR, TIA, PSAT/SAT, school watch flags, near-cutoff classes. These show as chips on the roster and in full on the conference page.
- **Conversation starters** (Overview): students with school watch flags or 3+ missing (adjustable).
- **Class-grade cutoff (70):** used for the Power Hour list and the "Below 70" context chip.
- **Dropping:** the average of the last 3 scores is 8 or more points below the average of the earlier scores. It needs 6 or more scores.
- **Platform gap:** platform averages 15 or more points apart. Each platform needs 2 or more scores, and missing work is left out of this check.
- **Retests (retest priority):** AP Classroom unit MC tests (raw %) scored under 80 (the Frisco retest cap). Progress checks, writing, Canvas and Gradebook items are not listed. A test drops off once a same-unit AP Classroom retest is imported, or when ticked. Missing work isn't included. Never treated as tests: "Corrections", "TURN IN HERE", the LockDown Browser test, and "Fill in the Blank Review".
- **Power Hour list:** anyone under 70 in any class, grouped by class period.
- **Assignment types** (used by Compare, the Unit Tracker and AP projection):
  - Writing = SAQ, LEQ, DBQ or FRQ in the name.
  - Progress Check = "progress check" or "PC" in the name.
  - Unit MC test = AP Classroom + "Unit N" + "test", "retest", "MC" or "MCQ" (not a PC, not writing, not a mock).
- **Compare years:** the Progress Check and Unit Test tabs use AP Classroom raw MC only. Each average shows n (students · tests) and a fine-print line naming the source and active filters.
- **Unit Tracker** (conference page): per unit, Test (raw MC %) | Retest | Best | Class avg | PC (not counted, greyed).
- **Units:** taken from "Unit N", "UN", or a topic number such as "Topic Check: 2.3" (Unit 2).
- **AP projection:**
  1. **Unit MC projection** (all year): the weighted average of AP Classroom unit MC tests and retests, raw % (no writing, no progress checks, no mocks). Unit N carries weight 1 + (N − 1) × 0.5.
  2. **Mock projection:** used when assignments named Mock / Practice Exam / Full-length exist. Mock MC = the average of the full-length MC tests. Mock writing = the practice-test FRQ / SAQ / DBQ / LEQ scores. These are combined with the College Board weights (editable in Settings): APHG MC 50 / FRQ 50; AP World and AP Euro MC 40 / SAQ 20 / DBQ 25 / LEQ 15. A missing part is left out and the rest scaled up, with a note such as "(no DBQ yet)".
  3. Once a mock exists it is the headline (badge "Mock"), and the Unit MC projection is shown alongside.
  4. The composite maps to a score: 85+ → 5, 70+ → 4, 55+ → 3, 40+ → 2, otherwise 1. Missing work is left out.
  5. **Compare years:** a "Mock projection vs. actual AP score" grid compares each student's prior-year mock projection with their actual AP score (Profile "Prior AP score" or "AP scores"), showing the exact-match and within-1 rates. A class-level line also compares against the imported College Board AP score summary.
- **Overview:**
  - Status tiles (On Track / Watch / Needs Help / AP exam unpaid); tapping one filters the roster.
  - Roster, and "Grab these kids" with reason tags and last parent contact.
  - Action lists.
  - Charts: assignment averages, platform freshness, periods side by side, biggest changes, STAAR vs. now, heatmap.
  - A weekly summary to copy.
- **Retests:** grouped by student or by test, with a tick box when a retest is done.
- **Power Hour:** the list, plus **Draft in the Tutorials sheet**:
  1. Reads the ID column, the header row and the chosen day's column from each alphabet tab (default day: next Tuesday or Wednesday; Thursday is duty).
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
- **Settings:** rules, which overview cards show, back up, restore, sample data, erase.
- **T-TESS** (sidebar tab): see "T-TESS tab" below.
  - **1.2 Data & Assessment:** data sources in use; reteach units (class AP Classroom unit MC average below the on-track %); retest priority (students one retest from on track).
  - **1.3 Knowledge of Students:** % with a full profile (8th STAAR, TIA BOY and GPA on file); prior AP on file.
  - **1.4 / 2.4 Activities / Differentiation:** reteach groups (units with 2+ students under the on-track %); Power Hour drafts and attended.
  - **2.1 / 3.3 Achieving Expectations / Classroom Culture:** % with an Agency goal; check-ins whose date has passed; % of quarter grade goals met.
  - **2.3 Communication:** parent contacts by type; parent emails drafted.
  - **2.5 Monitor & Adjust:** average AP Classroom MC change after a Power Hour draft (assignments imported after the first draft vs. before); average retest gain (MC retest vs. the same-unit original); weeks with a data refresh.
  - **3.1 Routines:** conferences marked "held", per grading period (approximate dates in `CONFIG.gradingPeriods`).
  - **4.2 Goal Setting (SLO: APHG):** % AP on track now vs. at the first MC test; TIA BOY → EOY growth; last year's AP results (typed in on the page) vs. % projected 3+.
  - **4.4 School Community:** counselor and co-teacher referrals logged.
  - **Tracked from the day the page was added:** "Mark conference held", referral buttons, parent-email drafts and assignment arrival dates.

## Added in this round (conference, overview, T-TESS, retest messages)
- **Conference page:**
  - Rank cells use the imported column labels, e.g. "Q1 snapshot rank band (vs past cutoffs)".
  - "Close to next letter" shows in Attendance & all classes.
  - The Agency form has AP skill strength, AP skill gap and Next step.
  - **Conference prep card** at the top gives 3 talking points worked out from the data:
    1. Raw MC trend: up or down in a row, or the latest unit MC test missing.
    2. Classes under 70: from the profile, or from the dashboard when my class is lower.
    3. Power Hour no-shows, or missing work when there's no Power Hour data.
    - Amber/red marks a concern. The card prints, compact and black & white.
  - **Growth tracker** (screen only): a line chart of every AP Classroom unit MC score in order, with R marking a retest. Beside it: TIA BOY → EOY this year, last year's TIA, and last year's AP score.
  - The Unit Tracker shows "Retest message sent: date" under a unit when one was logged.
- **Overview:**
  - **Reteach radar:** the 5 weakest units per course, using each student's latest AP Classroom unit MC attempt. Students below the on-track % are listed under each unit.
  - **Make groups:** reteach groups by each student's weakest unit, 4–5 per group (snake-dealt so group MC averages balance). Buckets of 1–3 fold into the student's next-weakest unit. You can copy or print the groups; each copy or print is logged for T-TESS.
  - **Retest priority:** watch / needs-help students whose next retest at ≥ 55% would flip them to AP on track. Each row shows the lowest score that flips them, and the list is sorted by it. The retest is added as its own test, as in the status rule.
  - **Intervention → outcome:** for each Power Hour draft, contact and retest, the next unit MC score vs. the previous one. The hero line shows "After Power Hour: avg MC ±X pts".
  - Test dates come from when each assignment first arrived in the dashboard, since imports carry no due dates.
- **AP projection, Benchmarks card:** this year's projected mean and % 3+ next to last year's line from Settings (default "Martin 2026: mean 4.05, 92.5% 3+" for APHG and "mean 3.51, 70% 3+" for AP World). Our class, school, Texas and global lines come from the AP score summary.
  - Optional score-summary columns: "School mean", "School % 3+", "Texas mean", "Texas % 3+" (a lone "School mean" still counts as ours).
- **Compare years:** "% AP on track by month" for the course, using the same rule as of each month's end, by arrival date.
- **Retest messages** (sidebar under Action lists; a button on every Overview / class page):
  - **Who:** students whose most recent **Gradebook (TAC) unit test** (curved) is **below 80** and who have no retest for that unit (any platform), and no ticked retest. Grouped by class and unit, all checked.
  - The threshold is in Settings ("Retest message if TAC unit test is below"). Setting it lower than the retest cap (80) brings back an optional second tier (cutoff–79, unchecked) with its own message.
  - **Copy for Canvas:** the names, one per line, plus the message. With more than one student it copies one personalized message per student, separated by "----".
  - **Mark sent:** logs "Retest message · Unit N · Canvas" in the contact log (once per student per unit per day) and hides the student for that unit until the next import.
  - **Copy prompt for Claude:** names + IDs, the unit and the message, ready for Claude in Chrome to send.
  - The message says "below 80" and includes: "I'll usually draft you for A Block. If A Block doesn't work, you can come during B Block instead — any day except Wednesday B Block or Thursday A Block, when I have duty." Editable in Settings.
- **Power Hour drafts** (sidebar under Action lists): three lists, one tab each:
  - **Below 80 on latest test:** latest TAC unit test *or retest* (whichever is later) under 80.
  - **Below 70 in class** and **Below 80 in class:** current class grade.
  - One line per student per class, grouped by class period: name, period, ID, the triggering score, last Power Hour draft (profile "Last Power Hour", else the last draft from this dashboard), no-shows. Students with a profile "Power Hour assigned now" value are left out (listed in a footnote).
  - **Copy roster** (name · ID · period, one per line), **Copy prompt for Claude** (sheet ID, the draft day, the dropdown value "Martin, Scott B106 A Block" — drafts are always A Block, never Wednesday B Block or Thursday A Block (duty); default draft day is the next Tuesday or Wednesday, never Thursday, and the prompt names the date — and the list with reasons), **Mark drafted** (logs "PH draft — Unit 3 test 72" or "PH draft — class grade 68" once per student, with the draft day as the note, and hides them until the next import).
  - A student on several lines (two classes) is logged once per action; a second press the same day doesn't log again.
- **T-TESS tab** (sidebar, under Insights; replaces the Settings-page version). Written for an administrator who has never seen the dashboard:
  - A date-stamped intro paragraph: what the dashboard is, what feeds it, that it refreshes weekly.
  - One table row per dimension (1.2, 1.3, 1.4/2.4, 2.1/3.3, 2.3, 2.5, 3.1, 4.2, 4.4): Dimension · What this dashboard shows (live numbers) · Where to see it (a link that jumps to the page or card, keeping the current course/period filter). A plain-English sentence sits under each row.
  - No student names anywhere. Numbers are totals for the classes in the current filter (All courses by default; pick a course or period chip to scope it).
  - Bottom: "Not covered here — see the separate T-TESS dashboard: 1.1, 2.2, 3.2, 4.1, 4.3." Footer: "Student-level data available on request."
  - Print (one page) and Copy text. In the artifact, Print opens a printable text version.
  - 4.2 shows last year's results per course from the AP score summary, else the Settings benchmark line, next to this year's projected % 3+.

## Added: At a glance, Help, backup, district participation
- **At a glance** (sidebar, under Insights): one printable page for an administrator, always every class regardless of the course chips, no student names.
  - Tiles: % on pace for a 3+ (headline AP projection ≥ 3 ÷ students with a projection), % AP exam paid, students drafted to Power Hour (profile drafts, dashboard drafts or PH-draft contacts), total drafts and attended.
  - Table 1: on pace for a 3+ per course and per class period, with last year's result (score summary, else the Settings benchmark) and "AP on track now".
  - Table 2: AP exam participation per course and class: paid ÷ enrolled, unpaid shown; students come from the Student Profile "AP Exam" column.
  - **School-wide social studies participation**: lines entered in Settings → At a glance inputs ("Label: paid of total" or "Label: 71%").
  - **AP exam participation by campus**: one small chart per course from the **District participation** import (`Course,Year,Campus,Participation %`, pasted on the Import page). Latest year per course; sorted; the campus matching Settings → School is highlighted; a dashed line marks the district average. A Settings text list is the fallback if nothing is imported.
  - Copy text, Print (one page).
- **Help & rules** (sidebar footer): where the numbers come from, the AP status rule, one line per page, import naming rules, phone/other-computer steps, privacy. "Copy instructions for the import chat" copies the note for the chat that loads data.
- **Backup:** compressed (gzip, prefix `CDZ1:`, about 4–5× smaller) so it fits in a note or email; Restore accepts both compressed and plain JSON. Settings shows the last backup date; the Overview shows a reminder chip when real data hasn't been backed up for 14 days.
- **Data check:** new item "AP Classroom items not counted in AP status" lists AP Classroom assignments that lack "Unit N" or "test/MC" in the name (progress checks and writing excluded by design).
- **Weekly summary:** adds retest messages to send, the Power Hour draft list count, and "After Power Hour: avg MC ±X".
- **Top bar** shows the page name on the welcome screen, Help, T-TESS and At a glance instead of the course chips.

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
- Progress checks no longer appear in Retests; only AP Classroom unit MC tests do.
- If the other chat imports only the Gradebook copy of a unit test (curved), it won't count. The AP Classroom raw score must be imported with "Unit N" in the name.
