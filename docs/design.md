# Design

Three decisions shape the whole system. Each one came from a way that a model on its own tends to fail at this kind of work.

## 1. Three kinds of content, kept apart

Every job reads three kinds of content, and each kind is written in its own way and lives in its own place.

| Kind | Where it lives | How it is written | Why |
|---|---|---|---|
| Procedure | The six job documents in jobs/ | Controlled English in the style of ASD-STE100 (build/STE-RULES.md): one instruction in each sentence, a command verb first, one word for one thing, a table for every decision | A small model obeys a short, literal sentence. It drifts on a long or hedged one. |
| Facts about the person | profile/facts.template.md, and the facts sections at the top of each job | Plain lists and tables: dates, pay bands, years in each skill, what he has never done | The model writes from context, so nothing is invented. A missing fact becomes a marked blank, never a guess. |
| The person's voice | profile/voice.template.md | Natural English, taught by examples: real messages the person sent and the person's own stories | Rules alone make text sound written by a model. Examples make it sound like the person. |

The voice is never written in controlled English, and the procedure is never written in the person's voice. Mixing them was the source of most early problems: rules got softened into prose, and letters picked up the flat tone of a procedure.

For a cover letter the model does not write a story. It copies one approved story word for word and writes only the one or two sentences that link the story to the posting (the bridge). That is the part a model can do well from the posting text. Everything else is the person's own wording, approved once.

## 2. The human gate

No job sends a message or a connection request to a person. The person sends every message himself.

Applications have a narrow gate. Only the apply job may submit, and only when all of these are true:

- the person gave the permission sentence for this chat;
- the route is on the job's own table: a one-click application on a job board, or a simple form that needs no account;
- every value in the form comes from "Facts and Answers";
- nothing on the way asks for a password, a sign-in, a new account, a one-time code, a CAPTCHA, a payment or a timed test.

Any other row is handed back in one message, with the reason and with the prepared text. LinkedIn is read-only in every job. The tracker records what was submitted and by whom.

This keeps three things true:

- every message that goes out is one the person chose and read;
- an application that the chat submits holds only facts that the person approved once;
- an account, a credential or a test is never touched.

The first version had a wider gate: it submitted nothing. The gate was narrowed after the drafts had been checked by hand for some days, and only for the routes where a wrong answer is unlikely and cheap.

## 3. Built for a small model

Each job is one self-contained document read in full from a cold start. A chat on a smaller model gets one paste line (docs/paste-lines.md), opens the documents it names, and needs nothing else.

What that means in practice:

- Every document has the same eight sections: this job, rules you must never break, words used in this document, steps, decision tables, exact formats, checks before you report, when something is not covered.
- Rules shared by several jobs are repeated in each one on purpose. A cross-reference to another job document is not allowed, because the chat would have to open it and might not.
- Every judgement is a table: condition in the first column, outcome in the next.
- Every cell the job writes has a pattern and one filled example.
- Every check can be run with code against a fresh read of the tracker, and states what "pass" is.
- State that must survive a chat lives in the tracker, never in the chat. The search writes one row for each helper in the "Search log" tab, so a new chat continues a run from the log. One cell of that tab holds the date of a LinkedIn limit message, and every job reads it before it opens LinkedIn.
- When a case is not covered, the job takes the cautious outcome, keeps the row, puts the open question first, and names the case in its report. It never stops to ask when the person is not there.

The cost is length: the documents are long, and a change to a shared rule must be made in every job that carries it. The gain is that a cheaper model runs each job the same way every time.
