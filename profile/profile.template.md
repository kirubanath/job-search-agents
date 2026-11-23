# Profile: the placeholders

Every value that differs from one person to the next is a placeholder in double braces, for example {{home_city}}. This file defines each placeholder once. Fill in your own value, then replace each placeholder in every file of the repository with it (a find and replace across the folder is enough).

The example values are invented. None of them belongs to a real person.

The job documents call the candidate "he" and "him". Change the pronoun everywhere if it does not fit you.

## Who you are

| Placeholder | What goes there | Example (invented) |
|---|---|---|
| {{candidate_name}} | Your full name, as on the resume. | Alex Example |
| {{first_name}} | The name the helpers use for you. | Alex |
| {{email}} | The email address that recruiters get. | alex.example@example.com |
| {{home_city}} | The city you live in and will work from. The documents assume you do not relocate. | Kochi |
| {{years_experience}} | Your total years of work experience, the true figure, as a whole number. | 3 |
| {{degrees}} | Your degrees in one line, so that a helper can judge "5 years with a Bachelor's or 3 with a Master's". | B.E. in Computer Engineering; no Master's |
| {{alumni_groups}} | The schools and former employers whose alumni you ask for referrals, in the order to try them. Each one is also a LinkedIn People page keyword. | Example Institute of Technology, then Example University, then Initech |
| {{current_employer}} | The company you work at now (or left last). The documents never name anything from it beyond its name. | Contoso AI |
| {{previous_employer}} | The employer before that. | Initech |
| {{project_a}} | Your main piece of past work that is a manuscript, not a publication. The documents never call it published. Leave the rules out if you have none. | Project Alpha |
| {{project_b}} | Your second main piece of past work, for example a published paper. | Project Beta |
| {{claims_never_made}} | The skills and kinds of work you have not done and must never claim, as one list. Every job checks its text against it. | RAG in production, vector databases, LangChain or LangGraph, fine-tuning, RLHF, Bedrock or SageMaker |

## Dates

| Placeholder | What goes there | Example (invented) |
|---|---|---|
| {{last_working_day}} | The last day at {{current_employer}}. After it, every text uses the past tense. | 31 January 2027 |
| {{earliest_start}} | The earliest start date that any form or message may give. Never write an earlier one. | 15 February 2027 |
| {{target_start}} | The start date you want. It is asked for at offer stage only, in one sentence. | 1 March 2027 |

## Pay

The pay table in the jobs has four bands and three values. {{pay_high}}, {{pay_mid}} and {{pay_floor}} set the bands. {{pay_target}} is the lower end of the quoted ranges and the "acceptable" line. Write each value with its unit, as you would say it.

| Placeholder | What goes there | Example (invented) |
|---|---|---|
| {{pay_high}} | The top of your target. A band that goes above it gets the "flexible on the split" line. | 30 LPA |
| {{pay_mid}} | A band that includes it gets the "{{pay_mid}} to {{pay_high}}" line. A number-only box with no band gets it. | 26 LPA |
| {{pay_target}} | Fixed pay at or above it is acceptable at any company. It is the lower end of the quoted ranges. | 24 LPA |
| {{pay_floor}} | The private floor. It is never written in any text you send. A stated band below it is out. Between it and {{pay_target}}, you decide after the first call. | 22 LPA |
| {{pay_line_no_band}} | The exact pay line when no band is stated or found. | 24 to 30 LPA fixed, flexible for the right role and hours |
| {{current_pay}} | Your current pay as you state it when asked. It never changes. | 25 LPA fixed |

"In digits" in the tables means the same value written as a plain number for a number-only box, for example 2600000 for 26 LPA.

## Your search

| Placeholder | What goes there | Example (invented) |
|---|---|---|
| {{search_keywords}} | The keywords of your LinkedIn searches, in order. [keyword n] in "Job 1 Search Sites" is item n. | AI engineer; machine learning engineer LLM; forward deployed engineer; ... |
| {{linkedin_geo_id}} | The LinkedIn geoId of {{home_city}}. Run one LinkedIn job search for the city and copy the number after geoId= from the address. | 100000001 |
| {{home_city_slug}} | {{home_city}} as a job site writes it in an address: lower case, hyphens for spaces. | kochi |
| {{naukri_city_slug}} | The city part of a Naukri search address for {{home_city}}. Run one search on Naukri and copy it. | kochi |
| {{target_companies}} | The companies whose careers sites you walk, in order. The first four are walked every run. | Acme AI, Northwind Labs, Globex, Initech |
| {{strict_loop_companies}} | The companies where a failed interview loop bars a new interview for six to twelve months, so that you prepare before a technical round or a timed test. | Globex, Northwind Labs |
| {{excluded_firms}} | The large IT services and outsourcing firms that a helper leaves out without opening the card. | Initech Services, Umbrella Consulting |

## Where things live

| Placeholder | What goes there | Example (invented) |
|---|---|---|
| {{drive_folder}} | The name of the Google Drive folder that holds the documents and the tracker. | Job Search |
| {{tracker_sheet_id}} | The id of the Google Sheet "Job Search Tracker" (the long string in its address between /d/ and /edit). | 1AbCdEfGhIjKlMnOpQrStUvWxYz0123456789abcdEF |
| {{resume_doc}} | The title of the Google Doc that holds your resume. | Resume Alex Example |

## Other documents the jobs name

The jobs also name some documents that this repository does not ship, because they hold only one person's material. Make your own, or remove the steps that open them.

| Document | What it holds |
|---|---|
| "Interview Prep Bank" | Section 1 short-tenure answers; section 2 stories S1 to S12 for interviews; section 3 topics by round; section 4 questions by interviewer; section 5 a company research checklist; section 6 a day-of checklist; section 8 the questions actually asked. |
| "Projects Plan", "ML Basics Plan", "Past Work Study Guide" | Study material for technical rounds, named in table 5.1 of "Job 4 Call Prep". |
| "Application Form Kit" | A page with the form values laid out for copying: personal details, start date, notice and pay, employment, education, skills, publications, short and long answers, job board profiles. |
| "Profile Text" | The resume and profile wording, with a part "Updating later" for the dated tasks of "Job 5 Weekly Review". |
