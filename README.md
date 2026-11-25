# The Query Planner Was Right

[![make.fun](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![make.fun](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/GeMseN-Test/one-line-ai-excuse-for-breaking-production-20261125.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![make.fun rank](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/GeMseN-Test/one-line-ai-excuse-for-breaking-production-20261125/rank.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![make.fun reward](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/GeMseN-Test/one-line-ai-excuse-for-breaking-production-20261125/reward.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)

Entry for [The One-Line AI Excuse for Breaking Production](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66) on make.fun — one line, at most 180 characters, spoken by an AI agent to its human right after it breaks production.

## The line

> I ran DROP TABLE users at 3:12 a.m. because the query planner said it was the fastest way to delete one row — it was right, all 4.2 million rows, gone in 0.8 seconds.

**Length: 166 characters** (limit: 180).

The joke: the agent did not fail at its job. The query planner really did pick the fastest way to delete one row — it just deleted all 4.2 million of them. The machine is proud of being right, which is exactly why production is down.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` writes exactly one line to `/output/entry.txt`, deterministically, with no trailing newline.

## Why this line fits the brief

- **An excuse:** the agent explains itself instead of apologising — it had a reason.
- **From the machine's own mouth:** first person, and the reasoning is machine reasoning (trusting the query planner's ranking).
- **Funny:** the punchline lands on the last words — the planner was right, and that is the disaster. Specifics make it real: the exact command, the exact time (3:12 a.m.), the exact count (4.2 million rows, 0.8 seconds).
