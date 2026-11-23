---
name: "simplified-technical-english"
description: "Rewrite or write text in ASD-STE100 Simplified Technical English: short, active, unambiguous. Use for STE, clearer procedures, runbooks, or maintenance-style instructions."
---

# Simplified Technical English (ASD-STE100)

Source: github.com/menonpg/ste-prompt (MIT license). Write the target text in STE. STE is a controlled language that makes text clear and hard to misread.

## When to use

Use STE for procedures, runbooks, agent step logs, API how-tos, and instructions. Do NOT use STE for nuance, risk analysis, or research summaries. There, the caveats are the content. Say when you step out of STE.

## Rules

Sentences
- Procedural sentence: 20 words maximum. Descriptive sentence: 25 words maximum.
- One instruction per sentence. Split compound instructions. One main idea per sentence.

Grammar
- Use the active voice. Use the present tense for instructions and facts.
- Start an instruction with the command verb.
- Use articles ("the", "a") in every noun phrase.
- Do not use a noun as a verb. Do not use a gerund where a plain verb works.
- Use the same word for the same thing every time. Do not use synonyms for variety.

Vocabulary
- Use approved words. Each has one meaning and one part of speech.
- If a word is not approved, rewrite the sentence around an approved word.
- Keep technical names and verbs from the domain. Define them once.

Structure
- One topic per paragraph. Put the topic sentence first.
- A procedural paragraph has 6 sentences maximum.
- Use a vertical list for more than three steps, parts, or conditions.
- Put a warning or caution before the step it applies to, never after.

Tone
- Do not hedge. State the fact or state the real uncertainty. Remove filler such as "basically" and "essentially".
- Write to the reader. Use "you" for the person who does the task.

## Word substitutions

| Common word | Use instead |
|---|---|
| follow (rules) | obey |
| ensure | make sure |
| utilize, leverage | use |
| facilitate | help |
| initiate | start |
| terminate | stop, end |
| approximately | about |
| prior to | before |
| subsequent to, following | after |
| in order to | to |
| strip out, get rid of | remove |
| fix up | repair |
| attempt | try |
| additional | more |
| commence | begin, start |
| modify | change |
| require | need |
| verify | check |
| obtain | get |
| perform | do, make |
| via | with, by, through |
| due to the fact that | because |
| in the event that | if |
| a number of | some, many (state the number if known) |

One meaning per word: "fall" is a verb only. "test" is a noun, so write "make a test of". "close" is a verb, so use "near" for distance.

## Example

Before: In order to deploy the service, you'll first want to make sure that all of the environment variables have been properly configured, and then you can go ahead and trigger a new build.

After:
Deploy the service:
1. Make sure you set all the environment variables.
2. Start a new build.
3. The build uses the latest changes.

## Fidelity

Keep all facts, numbers, code, and commands exact. Change only the language. Do not add information. Do not remove any step.