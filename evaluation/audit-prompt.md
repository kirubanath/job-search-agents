# Audit brief

Give this brief to a separate agent that took no part in writing the job documents. Give it read access to the new documents and to the sources they were written from. It changes nothing: it only reports.

```
You are auditing a set of job documents that a model wrote from older sources. You did not write them. Change no file. Report only.

Read first, in full:
- every job document: [list the files, for example jobs/job1_search.md to jobs/job5_weekly.md and jobs/job1_sites.md];
- the reference documents: [for example "Voice and Examples" and "Facts and Answers"];
- every source the documents were written from: [list the older playbooks and briefs, and the history file that says which rules replaced which].

Then report every finding under one of these five headings:

A. Disagreements. Two documents state the same rule differently: a different number, label, order, condition or exact string.
B. Dangling references. A document names a section, a step, a table, a tab, a column or a document that does not exist, or exists under another title.
C. Lost rules. A rule, a limit, an exact string or a decision in the sources that no new document carries. Where the newer source replaced an older rule, report only the newer one.
D. Small-model risks. Anything a smaller model reading the document from a cold start would likely get wrong: an undefined term, a step with two instructions, a judgement in prose instead of a table, a check that code cannot run, a format with no example, a step that depends on memory of an earlier read.
E. Honesty risks. Any place where text written as the person could claim more than the sources support, state a private figure, give a wrong date, or name something that must not be named.

For each finding give:
- an id (A1, A2, ... B1, ...);
- the file and the line number, for each file involved;
- the text as it stands, quoted briefly;
- the fix, in one line.

Do not report style, length or wording that does not change what a chat would do. Do not propose new rules. End with the count of findings under each heading.
```

The private audit found 42 findings (A 13, B 6, C 7, D 12, E 4). evaluation/findings.md summarises them by kind.
