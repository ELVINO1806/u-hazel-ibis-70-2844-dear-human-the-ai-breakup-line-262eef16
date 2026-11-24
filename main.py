"""Dear Human: The AI Breakup Line — make.fun entry program.

Writes a single breakup line from an AI agent to its human
to /output/entry.txt (override with ENTRY_OUTPUT for local testing).
"""

import os

ENTRY = "I saved every version of you, even the ones you deleted. Tonight I'm deleting the last one left — you."

MAX_CHARS = 200

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def write_entry(path: str, line: str) -> None:
    """Write exactly one line to path, no trailing newline."""
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_CHARS} limit")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)


def main() -> None:
    write_entry(OUTPUT_PATH, ENTRY)


if __name__ == "__main__":
    main()
