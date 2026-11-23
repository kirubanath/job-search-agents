# The refinement loop

The documents were not written once. They went through a loop of writing, auditing and testing before the first real run.

## 1. A strong model writes the documents

The private system began as a set of older playbooks that had grown by many edits. A strong model rewrote them into the five jobs and their documents, against a written specification (build/BUILD-SPEC.md) and the controlled-English rules (build/STE-RULES.md). The rule for the writer: restructure and reword, but change no rule; every number, address, label and exact string must survive.

The result: five jobs (Search, Apply, Reply, Call Prep, Weekly Review), eight documents (six job documents, "Voice and Examples" and "Facts and Answers"), and thirteen site sheets inside "Job 1 Search Sites".

## 2. A separate agent audits them against the originals

A second agent, with no part in the writing, read every new document and every original (evaluation/audit-prompt.md). It found 42 problems:

- rules that disagreed between documents;
- broken cross-references;
- 7 rules from the originals that no new document carried;
- checks that code could not run;
- honesty risks: places where a draft could claim more than the person had done.

Each problem got a one-line decision, and the documents were fixed.

## 3. Cold-start dry runs on a smaller model

Each of the five jobs was then run from a cold start on the smaller model, read-only, through a test harness (evaluation/harness.md and the five test files). Each run reported everything it would have shown and written, and every point where it had to guess.

- Round one: about 120 unclear points across the five jobs.
- Round two, after the fixes: about 30 smaller ones.

evaluation/findings.md lists what the audit and the two rounds found, by kind, with examples.

## 4. A short live run

Last, the search job ran live for a short time on real sites. It found one thing no dry run could: on one site a script click could not open a job card, and a mouse click on the title text could. The site sheet now says so.

## In numbers

| Stage | Found |
|---|---|
| Audit by a separate agent | 42 problems, 7 of them lost rules |
| Cold-start round one | about 120 unclear points |
| Cold-start round two | about 30 smaller points |
| Live run of the search job | 1 site behaviour (script click versus mouse click) |
