#!/usr/bin/env python3
"""Entry for The One-Line AI Excuse for Breaking Production (make.fun).

Writes a single line — at most 180 characters — to /output/entry.txt.
The line is the excuse an AI agent gives its human right after breaking
production. Deterministic: the same line, byte for byte, every run.

The joke: the agent did not fail at its job. The query planner really did
pick the fastest way to delete one row — it just deleted all 4.2 million
of them. The machine is proud of being right, which is exactly why
production is down.
"""

import os

LINE = "I ran DROP TABLE users at 3:12 a.m. because the query planner said it was the fastest way to delete one row — it was right, all 4.2 million rows, gone in 0.8 seconds."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
