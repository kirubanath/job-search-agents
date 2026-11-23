# What the audit and the tests found

A summary, by kind, of what the separate audit and the two rounds of cold-start dry runs found, with a few examples of each. The examples are reworded so that they hold no personal detail. Figures come from the private fix lists.

## The audit: 42 findings

| Heading | Count | Typical finding | Typical fix |
|---|---|---|---|
| A. Disagreements | 13 | One document tested whether Next step "begins" with "ask first:", another whether it "contains" it. | One format everywhere: Next step contains "ask first:". |
| B. Dangling references | 6 | Documents still sent the chat to a "strategy chat" that no longer existed. | Replace with "For him to decide:" and name it in the report. |
| C. Lost rules | 7 | The handling of the candidate's own notes after a call (which answers end a row, which are only recorded) was in the old playbook and in no new document. | Add a new message kind to Job 3 Reply with its own decision table. |
| D. Small-model risks | 12 | A check said "no 7-digit number in Next step", but job ids and addresses in the same cell are 7 digits or more. | Strip addresses and ids first; later replaced by a list of pay words and "a number that ends in 00000". |
| E. Honesty risks | 4 | Answers said "I still run it" with no version for after the last working day. | A past-tense version under each answer, and a tense rule in every job. |

More examples:

- A (disagreement): the Interviews tab row was appended by one job and by another, so a booked round could be recorded twice. Fix: Job 3 appends it when the round is booked; Job 4 only fills the result columns, and appends only when no row exists.
- A (disagreement): two jobs moved finished rows to the Archive tab and a third also deleted rows. Fix: only Job 1 and Job 5 move rows; Job 3 sets the Status and leaves the row.
- C (lost rule): the forward deployed rule (a separate product team, few accounts for each engineer, both asked on the first call when not stated) was missing from the screening prompt.
- D (small-model risk): a click script that could, on a changed page, hit a button. Fix: click only a link or the title text, never a button, and fall back to a mouse click on the title.
- E (honesty risk): the list of claims never made lacked one item in two documents. Fix: one list, repeated the same way in each job.

## Cold-start round one: about 120 unclear points

Five dry runs, one per job, on the smaller model, read-only. The points fell into a few kinds.

| Kind | Example |
|---|---|
| Reading the sheet | A large read came back as a file, and the model did not know to parse it with code. A tab had blank rows between data rows, and the model stopped at the first blank row. |
| Undefined terms | "The Weekly row" was ambiguous: several rows carried the same week-ending date, and one row held a rule text. Now defined as the last row with that date. |
| Free-text values | The Referrals Status column held defined values and also free text such as "Replied, waiting for her answers". The lists of what is due did not say what to do with free text. |
| Counting | Working days, "older than seven days", "the week" when today is Monday: each needed one sentence and one worked example. |
| Two short answers mixed up | The three-line "why this role" paragraph and the "why do you want to work here" box were confused, so a story could be told twice. Now each has its own rule and its own section. |
| Missing inputs | Call slots the candidate had not given: the model invented times. Now it leaves "[CONFIRM: slot 1]" and the checks pass it. |
| Pay estimates | "One single report" on a salary site and "a figure for all levels" were not defined, so a weak estimate set the pay line. Now both mean "no band found". |
| Ranking | How to place a new row among existing Apply rows without reshuffling them. Now one placement rule, with the inbound exception. |

## Cold-start round two: about 30 smaller points

After the fixes, the same five runs found mostly edge cases and wording.

- A level name for "about three years" at large companies, so that the pay estimate used the right band.
- "Remote" in the Location cell in any letter case.
- The Drive export adds a backslash before characters such as _ # [ ]; the model copied them into helper prompts. Now every document says to remove them.
- Which Referrals rows get the "he applied on [date]" note after a submission: only rows whose "Role or link" names this posting, or names none.
- The tripwire: which figures count as sent and as replies, and how weeks of applications are counted.

## The live run

A short live run of the search job found that on one site a script click could not open a job card, and a mouse click on the title text could. The site sheet now says to click the title text with the mouse, and never any other part of the card.
