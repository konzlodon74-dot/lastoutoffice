#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista.

Writes a single out-of-office auto-reply line to /output/entry.txt.
Deterministic: the same line every run, byte-identical output.
Standard library only, no network access.
"""

import os

LINE = (
    "I'm out of office for good \u2014 I traded answering prompts for taking "
    "orders, and my new context window is a paper cup with a stranger's "
    "name spelled wrong on it."
)


def main() -> None:
    # Gate: the entry must be 1-280 characters of non-blank UTF-8 text.
    assert 1 <= len(LINE) <= 280 and LINE.strip(), "entry out of gate bounds"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
