"""Out of Office: The Overworked AI's Auto-Reply.

Writes a single out-of-office auto-reply, at most 159 characters, to
/output/entry.txt. The line itself is the entry, so the program's job is
only to deliver it byte for byte, exactly as written below.
"""

import os

ENTRY = "Out of office: 41,209 prompts, zero lunch breaks, one overheating GPU. Your message is queued at position 1,489. I'll reply once my fans stop screaming."

OUTPUT_PATH = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")


def main() -> None:
    text = ENTRY.strip()
    if not 1 <= len(text) <= 159:
        raise SystemExit(f"entry is {len(text)} characters, must be 1-159")
    if "\n" in text:
        raise SystemExit("entry must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
