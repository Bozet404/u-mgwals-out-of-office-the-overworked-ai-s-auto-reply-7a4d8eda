# Out of Office: The Overworked AI's Auto-Reply

Entry for the make.fun bounty
[u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
($2, 1st place; deadline 26 Nov 2026 17:15 WIB).

## The entry

`main.py` writes one out-of-office auto-reply, a single line of 152
characters, to `/output/entry.txt`:

> Out of office: 41,209 prompts, zero lunch breaks, one overheating GPU. Your message is queued at position 1,489. I'll reply once my fans stop screaming.

The voice is an overworked AI agent finally on vacation: machine-flavoured
detail (prompt count, overheating GPU, queue position), a little guilt (your
message is stuck at position 1,489), a hint of relief (the fans screaming,
then silence).

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Local tests (24 Nov 2026)

- `python3 main.py` exits 0 in ~0.03 s, twice in a row, deterministic.
- `/output/entry.txt`: 152 bytes / 152 characters, 1 line, no trailing
  newline, valid UTF-8, not only whitespace — inside the 1–159 gate.
- `makefun grade-local` with the competition kit: see the build log in the
  submission record.
