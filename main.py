#!/usr/bin/env python3
"""Entry for make.fun: The One-Line Cat Joke That Lands.

Running this script writes one single-line cat joke to entry.txt
inside the output directory. The output is fixed: the same bytes
come out on every run, with no randomness, no clock reads, and no
network calls, so two runs are always byte-identical.
"""

import os
from pathlib import Path

# The joke. Setup: a vet asks about allergies. Turn: the cat's
# sneeze answers the question and reacts to the bill at the same time.
JOKE = "The vet asked if my cat had any allergies. She sneezed at the invoice."


def output_path() -> Path:
    """Where entry.txt goes.

    The grader provides /output; OUTPUT_DIR lets a local run point
    somewhere else without changing the program.
    """
    base = os.environ.get("OUTPUT_DIR", "/output")
    return Path(base) / "entry.txt"


def main() -> None:
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    # Exactly the joke, no trailing newline, so the file holds
    # precisely the text the judge reads.
    target.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
