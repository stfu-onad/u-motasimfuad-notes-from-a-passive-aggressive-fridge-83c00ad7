"""One passive-aggressive note from a smart fridge to its owner.

Writes the note to /output/entry.txt (UTF-8, single line, 1-200 chars).
"""

import os

LINE = "Reminder: the leftover pizza you keep 'saving for later' has now legally lived here longer than some of my firmware versions. Eat it or I will."

MAX_CHARS = 200


def main() -> None:
    # Validate the note before writing anything, so a bad line never
    # produces a partial or invalid /output/entry.txt.
    line = LINE
    if not line.strip():
        raise ValueError("entry line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"entry line must be 1-{MAX_CHARS} chars, got {len(line)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
