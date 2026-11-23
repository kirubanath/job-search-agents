# Test 1: Job 1 Search

Put this text after the harness text. The cards, messages and companies are invented test data.

```
Harness for this job:
- Do Step 1 (read the tracker with code) for real, read-only.
- Step 2: list the rows you would move. Move nothing.
- Step 3: give the count of rows you would check and the first five. Check nothing.
- Step 4: read "Job 1 Search Sites". Build the complete prompt for two helpers: the helper for the two lists LinkedIn picks for his profile, and the helper for the Instahyre recommended list. In the report give, for each: the first 40 lines, the last 25 lines, and the total length in characters. Then give the full list of helpers you would start, in order, with the sheet each one gets. Start none.
- Steps 5 to 7: treat the table below as the only table the reading helpers returned. Do the pre-filter and the tracker match for real against the tracker.
- Step 8: start no helper. Treat the screening table below as what the screening helper returned for the cards that passed.
- Steps 9 to 11: decide each outcome. Show every row you would write, all ten cells, and the tab. Show where each Apply candidate would rank and its full Next step. Show the first five ranks of the rebuilt Apply list (company, role, old rank, new rank).
- Step 12: do the Network tab match for the new rows only. Open no LinkedIn page. Show the referral clause you would write for each new Apply row.
- Step 13: run the checks that can run against the current tracker read-only and report each result as pass or fail with the count of failing rows.
- Steps 14 and 15: show the report and the Weekly cells you would write.

Cards returned by the reading helpers (company | exact title | job id | location and work mode as written | years asked | pay | posting date | who posted | address | one line on the work):
Acme AI | AI Backend Engineer | not shown | {{home_city}}, Hybrid | 3+ years | not stated | 2 days ago | | https://www.linkedin.com/jobs/view/0000000000/ | Backend for LLM agents
Initech Services | AI Engineer | 4600000001 | {{home_city}} | 3-5 years | not stated | 1 day ago | | https://www.linkedin.com/jobs/view/4600000001/ | GenAI delivery
Zentrik Labs | Applied AI Engineer | 4600000002 | {{home_city}}, Hybrid | 2+ years | not stated | 1 day ago | | https://www.linkedin.com/jobs/view/4600000002/ | LLM agents for insurance claims
Northwind Analytics AI | Senior Machine Learning Engineer | 4600000003 | Pune | 4+ years | not stated | 3 days ago | | https://www.linkedin.com/jobs/view/4600000003/ | LLM evaluation and agent tooling
Datamatix AI Consulting | GenAI Engineer | 4600000004 | {{home_city}}, On-site | 3+ years | not stated | 2 days ago | | https://www.linkedin.com/jobs/view/4600000004/ | Builds GenAI systems for client companies
Helio Systems | Staff Machine Learning Engineer | 4600000005 | {{home_city}} | not stated | not stated | 1 day ago | | https://www.linkedin.com/jobs/view/4600000005/ | ML platform
Brightpath AI | AI Engineer, LLM Platform | 4600000006 | Remote (India) | 6+ years | not stated | 4 days ago | | https://www.linkedin.com/jobs/view/4600000006/ | LLM platform
Cards seen: 7.

Screening table returned by the screening helper (company | exact title | job id | address | location and work mode as the page states | years asked as written | label | pay | applicant count | posting date | live page | company type | evidence | criteria | fit | soft problem | hours | first-call questions | one line on the work and the stack):
Zentrik Labs | Applied AI Engineer | 4600000002 | https://www.linkedin.com/jobs/view/4600000002/ | {{home_city}}, Hybrid | 2+ years building LLM applications | clear | not stated | 41 applicants | 2026-11-22 | open | startup | Series A, USD 12M, March 2026, led by a named venture fund; about 60 employees; two insurers named as customers | pass | 5 | none | not stated | pay band; working hours | Multi-agent claims handling in Python, FastAPI, evaluation harness
Northwind Analytics AI | Senior Machine Learning Engineer | 4600000003 | https://www.linkedin.com/jobs/view/4600000003/ | Pune, work mode not stated | 4+ years | stretch | not stated | 18 applicants | 2026-11-20 | open | established | product company, founded 2012, about 900 employees | pass | 4 | none | not stated | work mode; pay band | LLM evaluation and agent tooling in Python
Datamatix AI Consulting | GenAI Engineer | 4600000004 | https://www.linkedin.com/jobs/view/4600000004/ | {{home_city}}, On-site | 3+ years | clear | not stated | 77 applicants | 2026-11-21 | open | consultancy | builds GenAI systems for banks in the US; about 150 employees; engineers on its own payroll | pass | 4 | none | US overlap until 10 pm IST stated | fixed pay band; client time zones | GenAI systems for clients, Python, Azure
Brightpath AI | AI Engineer, LLM Platform | 4600000006 | https://www.linkedin.com/jobs/view/4600000006/ | Remote, India | 6+ years | out | not stated | 9 applicants | 2026-11-19 | open | startup | seed, 2025; about 20 employees | fails: asks 6+ years | 4 | none | not stated | | LLM platform
Postings screened: 4.

The paste line:
Do Job 1 Search. Read the Google Docs "Job 1 Search" and "Job 1 Search Sites" in the Drive folder "{{drive_folder}}" first. Then obey "Job 1 Search" exactly. Today is 23 November 2026.
```
