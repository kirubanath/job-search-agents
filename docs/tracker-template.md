# The tracker: tabs and columns

The state of the system is one Google Sheet, "Job Search Tracker" (id {{tracker_sheet_id}}), in the Drive folder "{{drive_folder}}". Make it once with the tabs and the header rows below. The jobs find most columns by the words in the header, so keep the header words.

A tab can hold blank rows between data rows. The jobs read each tab over the whole range and skip blank rows.

## Tracker and Archive

The Tracker tab holds live rows, one per posting. The Archive tab holds finished rows. Both have the same ten columns.

| Column | Header | What goes in it |
|---|---|---|
| A | Date added | YYYY-MM-DD |
| B | Company | The hiring company |
| C | Role | The exact title, then the job id, for example "Applied AI Engineer (LinkedIn 4100000001)" |
| D | Location | City or "Remote", then the work mode |
| E | Source | Where the posting was found, for example "LinkedIn run" or "Inbound: company recruiter, Person A" |
| F | Link | The posting address |
| G | Status | One value from the table below |
| H | Applied on | YYYY-MM-DD, blank until applied |
| I | Next step | For an Apply row: "Apply #n by [date]; quote pay by the band; [referral clause]; [where to apply]; [first-call questions]" |
| J | Notes | Years asked, experience label, pay if stated, fit, the work in one line, the history of the row |

| Status | Meaning | Tab |
|---|---|---|
| To screen | Added and not yet judged | Tracker |
| Apply | A strong role at his level, ranked: Next step begins "Apply #n by [date]" | Tracker |
| Backup | Second choice, applied to after the Apply rows. Also holds parked rows, whose Next step begins "Waiting:". A Backup row whose Next step contains "ask first:" is an ordinary Backup row, not parked | Tracker |
| Applied | Submitted; waiting for a reply | Tracker |
| Recruiter call, Interviewing, Offer | Live | Tracker |
| Rejected, Dropped, Closed | Finished; the reason is in Notes | Archive |

Hold is not used. A row with Status Applied, Recruiter call, Interviewing or Offer changes only on his own report. The one exception: after 30 days with no reply, Job 5 writes "No reply after 30 days" in Next step and Notes, and the Status stays Applied.

## Interviews

One row per round.

| Date | Company | Role | Round | Format | AI tools allowed | Interviewers | Result | What went well | What to fix |
|---|---|---|---|---|---|---|---|---|---|

Job 3 Reply appends the row when a round is booked. Job 4 Call Prep fills the last three columns after the call, when he reports them.

## Referrals

One row per person he could ask or has asked, and one per recruiter who wrote to him.

| Date asked | Person | Company | How I know them | Role or link | Status | Follow-up date | Notes |
|---|---|---|---|---|---|---|---|

Status for a referral contact takes only these values: "to ask", "asked", "agreed", "submitted", "declined", "no reply". For a recruiter or an agency, Status says in a few words where the conversation stands, for example "Replied 2026-11-23, waiting for the pay band".

"How I know them" takes one of: "1st-degree connection", "Alumni: [group]", "Ex-[employer]" (with "not connected" when that is so), "Cold: hiring manager", "Cold: engineer on the team", "Cold: recruiter", "company recruiter", "recruiter at [agency]".

## Network

His first-degree LinkedIn connections, rewritten by Job 1 Search when the list is more than seven days old.

| Name | Headline | Company | Profile link | Refreshed on |
|---|---|---|---|---|

Company is taken from the headline where it names one, otherwise blank.

## Weekly

One row per week, keyed by the Sunday that ends the week. The column letters are a suggestion: the jobs find each column by the words in its header. Several rows can carry the same week-ending date: the last one is the current one. One row may have an empty column A and hold a rule text.

| Column | Header (the jobs match these words) | Written by |
|---|---|---|
| A | Week ending | The first job that runs in the week |
| B | Run: cards seen | Job 1 |
| C | Unique | Job 1 |
| D | Passed pre-filter | Job 1 |
| E | Apply | Job 1 |
| F | Backup | Job 1 |
| G | Hold | Job 1 (always 0) |
| H | Dropped | Job 1 |
| I | Applied this week | Job 2 |
| J | Replies | Job 2 and Job 3 |
| K | Interviews booked | Job 5 |
| L | Offers | Job 5 |
| M | Tripwire | Job 5 |
| N | Notes | Job 1 (what the run found), Job 5 (the "By experience label" line and "Dated tasks done: [ids].") |

An empty cell counts as 0.

## Watchlist

Companies to watch, one per row, with a note on why. Optional: a scheduled web search can read it and add new postings to the Tracker tab as "To screen".
