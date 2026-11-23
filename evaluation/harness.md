# Cold-start test harness

Each test is one prompt to a fresh chat on the smaller model: this harness text, then the test file for one job, then the paste line. The companies, people and figures in the tests are invented test data. The harness turns a real run into a read-only dry run and asks for a report of everything that was unclear.

```
TEST HARNESS. This part is not from him. It changes the job only where it says so.

This is a dry run. Act exactly as the chat that receives the paste line at the end of this prompt. You have no other knowledge of this project: find the documents by title in the Google Drive folder "{{drive_folder}}" (load the Google Drive, Docs and Sheets tools with ToolSearch) and read them as the paste line says.

Differences from a real run:
1. Write nothing anywhere: no tracker cell, no tab, no Drive file, no document. Wherever a document tells you to write, append, move or delete, record instead in your final report the exact tab, the row (company plus job id), the cell and the text you would have written.
2. Do not use Chrome. Do not start helpers. Web search and web fetch are allowed where the job document allows them.
3. He is not present. Where the document says to wait for his word, the harness tells you what he says.
4. Your final report is the only output. It has two parts. Part 1: everything the chat would have shown him, in order, exactly as it would appear. Part 2, headed "Where the document was unclear": every step where you had to guess, every term that was not defined, every pair of rules that conflicted, every instruction you could not carry out and why, and every place where you were not sure which section of another document to use. Quote the step number each time. If nothing was unclear, say so.
```
