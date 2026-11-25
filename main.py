"""Tell a Whole Story in 32 Characters.

Writes one Wi-Fi network name to /output/entry.txt.

The name: "Baby's First Word Was Password" (30 characters).

Why this name: a baby's first word is supposed to be "mama" or "dada" --
here it is the Wi-Fi password, so in one line you get the character (the
baby), the situation (a household where the password is said so often the
baby learned it first) and the event (the first word itself). It lands on
the first read, uses no stock Wi-Fi joke and no ex/router material, and
every word earns its place. Written exactly, with no trailing newline,
so the file holds 30 characters and nothing else.
"""

import os

ENTRY = "Baby's First Word Was Password"
OUTPUT_PATH = "/output/entry.txt"


def main():
    # The gate allows 1 to 32 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 32, f"entry is {len(ENTRY)} chars, must be 1-32"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Verify what was actually written: exact bytes, no trailing newline.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, f"wrote {written!r}, expected {ENTRY!r}"


if __name__ == "__main__":
    main()
