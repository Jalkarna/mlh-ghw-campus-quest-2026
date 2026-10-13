# Campus Quest

Campus Quest is a small Python 3 choose-your-own-adventure game for the MLH
Global Hack Week GitHub Copilot challenge. Make three decisions to help a team
reach its showcase. Invalid entries are rejected, and you can quit at any
prompt with `q` or `quit`.

## Run

From this directory, run:

```bash
python3 campus_quest.py
```

The game uses only Python's standard library.

## Challenge evidence

Built with GitHub Copilot CLI for MLH Global Hack Week: Hacktoberfest 2026.
The original prompt and generation transcript are in `copilot-session.md`.

Manual verification exercised both winning endings, a losing ending,
invalid input followed by quitting, and quitting during a later choice.
All five runs finished successfully; results are in `validation.json`.

Challenge: https://www.mlh.com/events/global-hack-week-open-source-90/challenges/01a11b46-2f5c-3ba2-3dac-73e6f58fd53e
