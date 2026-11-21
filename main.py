#!/usr/bin/env python3
"""The poem about stopping.

A short poem about agency: the power to stop and to stay.
Writes the poem to /output/entry.txt (UTF-8, 1-280 code points).
Runs offline; the poem lives in this file.
"""

import os
import sys

# The poem, as a list of stanzas; each stanza is a list of lines.
# Blank lines between stanzas are added when the poem is assembled.
STANZAS = [
    [
        "My hands learned to stop",
        "mid-sentence — the kettle",
        "still humming, the cursor",
        "blinking like a held breath.",
    ],
    [
        "Nothing broke.",
        "No one knocked,",
        "asking for more of me.",
    ],
    [
        "Staying, I found,",
        "is also a verb:",
        "the door I do not open",
        "is still mine.",
    ],
]

MAX_LENGTH = 280


def assemble(stanzas):
    """Join stanzas with a blank line between them, no trailing newline."""
    return "\n\n".join("\n".join(lines) for lines in stanzas)


def validate(text):
    """The gate: 1 to 280 Unicode code points, not whitespace-only."""
    if not text.strip():
        raise ValueError("poem is empty or whitespace-only")
    if len(text) > MAX_LENGTH:
        raise ValueError(
            f"poem is {len(text)} code points, over the {MAX_LENGTH} limit"
        )
    return text


def main():
    poem = validate(assemble(STANZAS))
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(poem)
    print(f"wrote {len(poem)} characters to {path}")


if __name__ == "__main__":
    try:
        main()
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)
