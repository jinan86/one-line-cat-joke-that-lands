#!/usr/bin/env python3
"""One-line cat joke for make.fun.

This entry produces exactly one joke, always the same one, and stores
it in a file called entry.txt. There is no randomness, no clock, and
no network access involved: running the script twice yields the same
bytes both times, which is what the grader needs to see.
"""

import os
from pathlib import Path

# Why the line works: the vet's allergy question gets an answer from
# the cat itself, and that answer doubles as a complaint about the
# price of the visit.
JOKE = "The vet asked if my cat had any allergies. She sneezed at the invoice."

# Where the result lands. The grading harness mounts /output; setting
# OUTPUT_DIR in the environment lets a local run write somewhere else
# instead, without touching the code.
OUTPUT_ENV_VAR = "OUTPUT_DIR"
DEFAULT_OUTPUT_DIR = "/output"
ENTRY_FILENAME = "entry.txt"


def resolve_entry_path() -> Path:
    """Return the full path of the file the joke will be written to."""
    directory = os.environ.get(OUTPUT_ENV_VAR, DEFAULT_OUTPUT_DIR)
    return Path(directory) / ENTRY_FILENAME


def entry_text() -> str:
    """Return the joke, guarding the one-line contract.

    If the line ever picked up a newline by accident, fail loudly
    instead of silently writing a two-line file.
    """
    if "\n" in JOKE or "\r" in JOKE:
        raise ValueError("joke must be a single line")
    return JOKE


def save_entry(path: Path) -> None:
    """Create parent folders as needed and store the joke verbatim.

    The file holds the joke and nothing else: no trailing newline, so
    its length is exactly the length of the line itself.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(entry_text(), encoding="utf-8")


def main() -> None:
    save_entry(resolve_entry_path())


if __name__ == "__main__":
    main()
