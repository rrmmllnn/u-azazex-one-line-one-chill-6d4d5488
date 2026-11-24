#!/usr/bin/env python3
"""Write one quiet chill to /output/entry.txt.

The scare is domestic and slow: a hand I recognise, a book passed
down the family, and a fresh date where none should exist. No gore,
no creature -- only the sense that the book is still being written in.
"""

from pathlib import Path

# The line is assembled from three movements: the find, the paradox, the sting.
BEATS = (
    "I found my handwriting in my grandmother's recipe book, ",
    "in the margins of dishes she cooked before I was born, ",
    "and the newest note is dated yesterday.",
)

OUT = Path("/output/entry.txt")


def compose() -> str:
    return "".join(BEATS)


def validate(text: str) -> None:
    # The entry must be exactly one line of 1-200 characters.
    single_line = "\n" not in text
    in_range = 1 <= len(text) <= 200
    if not (single_line and in_range):
        raise ValueError(
            f"entry invalid: single_line={single_line}, length={len(text)}"
        )


def main() -> None:
    text = compose()
    validate(text)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
