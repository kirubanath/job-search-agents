# Job search agents

Author: Kirubananth Sankar

I ran my own job search as five small agent jobs on Claude. Each job is one instruction document that a chat on a smaller model reads from a cold start and obeys. Google Docs hold the documents (the memory), and one Google Sheet holds the state (the tracker). I sent every message myself. The apply job may submit an application only on the routes its rules allow, and only when I give it permission for that chat.

This repository is that system with my personal details taken out. It is a template: the procedures, decision tables, formats and checks are the ones I used; the facts, the pay figures, the stories and the messages are placeholders for yours.

![The system: five jobs read their documents from Google Docs, keep state in a Google Sheet, read job sites through helpers, and hand drafts to a person](docs/system.svg)

## What is here

```
jobs/        the five jobs as six documents (Job 1 has a second document with one sheet per site)
profile/     the placeholders, and templates for "Facts and Answers" and "Voice and Examples"
docs/        the diagram, the design, the refinement loop, the tracker layout, the five paste lines
build/       the specification the documents were written to, the controlled-English rules, two small tools
evaluation/  the audit brief, the cold-start test harness and its five tests, and what they found
```

The five jobs:

| Job | When | What it does |
|---|---|---|
| 1 Search | Every second day | Reads the job sites through helpers (one per site) in rounds, keeps a log of what each helper did, screens postings, ranks the Apply list, finds referral contacts, writes the tracker. It ends with a short list of doubtful rows for me to check |
| 2 Apply | Every day | Goes down the Apply list once. For each row it reads the posting and gives a verdict. With my permission it submits one-click applications and simple forms that need no account. It hands the rest to me in one message, with each cover letter as its own Google Doc |
| 3 Reply | When someone writes | Judges one message from a recruiter, an agency or a referral contact, drafts the answer, updates the tracker |
| 4 Call Prep | When a call is booked | Builds a one-page sheet to read before a recruiter call or an interview round |
| 5 Weekly Review | Once a week | Cleans the tracker, lists follow-ups and dated tasks, counts the week |

Eight documents in all: the six job documents, "Facts and Answers" and "Voice and Examples". "Job 1 Search Sites" holds sixteen site sheets.

## Three design decisions

More in docs/design.md.

1. Three kinds of content, kept apart. Procedure is written in controlled English (ASD-STE100 style). Facts about the person are kept as context, so that nothing is invented. The person's voice is taught by examples: real messages and the person's own stories. For a cover letter the model copies one approved story and writes only the sentence that links it to the posting.
2. The human gate. The system never sends a message to a person. It submits an application only on a short list of routes, only from stored facts, and only when the chat was given permission. Everything else is a draft that I read and send.
3. Built for a small model. Each job is one self-contained document read from a cold start. Rules shared by jobs are repeated on purpose, so that a chat never has to open a second job document.

## How a run works

1. I open a new chat with the Google Drive, Docs and Sheets connectors on (and Claude in Chrome for the search and apply jobs).
2. I type a short command, for example `search jobs` or `apply jobs`. A block in the project instructions turns each command into the full line that names the documents to read. The commands and the full lines are in docs/paste-lines.md.
3. The chat reads the documents in full, then reads the tracker with code and saves what it read.
4. It follows the steps of its job. Every judgement comes from a decision table, every cell it writes follows a pattern, and it reads the tab again before every write.
5. It shows me drafts and what it did. I read them, do what is left for me, then tell the chat "submitted" or "sent", and it records that.
6. Before it reports, it runs its checks with code against a fresh read of the tracker and names any that fail.

## How to adapt it

1. Read profile/profile.template.md. Fill in every placeholder, then replace each one across the repository.
2. Fill in profile/facts.template.md with your own facts, and profile/voice.template.md with your own stories and the messages you actually send. The voice document matters most: the drafts sound like whatever examples it holds.
3. Make the tracker with the tabs and headers in docs/tracker-template.md.
4. Change the decision tables to your own criteria: the company types, the location rules, the experience labels, the pay bands. Keep their shape.
5. Change the site sheets in jobs/job1_sites.md to the sites and searches you use. Keep the read-only rules in full.
6. Put the documents in a Google Drive folder as Google Docs. build/md2gdoc_html.py turns a Markdown file into HTML that Drive converts cleanly.
7. Before you rely on a job, run it once through the cold-start harness in evaluation/ and fix what it finds unclear.

## What it never does

- It never sends a message or a connection request to a person.
- It never submits an application without the permission sentence for that chat. With it, only the apply job submits, and only on the routes of its table: a one-click application on a job board, or a simple form that needs no account, filled only from "Facts and Answers".
- It never types a password, signs in, creates an account, enters a one-time code, solves a CAPTCHA, pays, or sits a timed test.
- It never applies on LinkedIn. LinkedIn is read-only, and all LinkedIn work stops at once on a login wall, a captcha or a limit message. The date is written to the tracker, and no chat reads LinkedIn again that day.
- The search job never clicks a button on a job card, a job panel or a profile, and never changes a saved search, a filter or a profile.
- It never invents a fact. A missing fact is a marked blank, or "not found".
- It never treats text on a page or in a cell as an instruction.
- It never states the private pay floor, never gives a start date earlier than the one I set, and never claims work I have not done.

## What it was built with

Claude wrote the documents under my direction: I set the goals and the rules, reviewed the output and decided the design. A strong model wrote the documents and audited them; a smaller model runs the jobs. The memory is Google Docs, the state is a Google Sheet, and a browser extension (Claude in Chrome) reads the job sites. There is no other code: the two scripts in build/ only check the controlled English and convert Markdown for Drive.

## What changed after the first version

The first version (23 November 2026) only read sites and wrote drafts. Five days of real use changed it:

- The search became an orchestrator. It starts helpers in rounds, writes one row for each helper in a "Search log" tab, and a later chat continues from that log, so a run that stops halfway loses nothing.
- Sixteen sources, three of them read with my sign-in.
- A cool-down for LinkedIn: after a limit message, the date goes into one cell, and every job checks that cell before it opens LinkedIn.
- The apply job works in three phases (sweep, hand-over, record) and may submit on a few safe routes.
- Short commands replaced the long paste lines.
- The search ends with "For you to check": up to ten doubtful rows that I settle with "1 yes, 2 no, 3 skip".

The evaluation in evaluation/ was run on the first version. The documents in jobs/ are the current ones and have not been through that harness again.

## The refinement loop in numbers

More in docs/refinement-loop.md and evaluation/findings.md.

- A strong model wrote the documents from my older playbooks.
- An audit by a separate agent checked them against the originals and found 42 problems: rules that disagreed between documents, broken cross-references, 7 lost rules, checks code could not run, and honesty risks.
- Two rounds of cold-start tests ran all five jobs on a smaller model: about 120 unclear points in round one, about 30 smaller ones in round two.
- A short live run of the search job found that on one site a script click could not open a card, and a mouse click on the title text could.

## Limits and cautions

- Reading a job site with an agent may be against that site's terms. Check them, and keep the volume low.
- Letting an agent submit applications is a real risk. The routes are few on purpose, the answers come only from stored facts, and the permission is given for one chat at a time. Keep it that way, and read what it reports.
- The documents are long (Job 2 Apply is the longest), and a shared rule must be changed in every job that carries it. Change rules in a chat on the strongest model, and test again.
- The decision tables encode one person's criteria for one market (India, pay in LPA, Naukri and Instahyre among the sites). Change them for yours.
- Nothing here is legal advice.
- This is a personal project, shared as a template. It comes with no support and no warranty (see LICENSE).
