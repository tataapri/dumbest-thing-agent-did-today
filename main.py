#!/usr/bin/env python3
"""Write one line about the dumbest thing this agent did today.

The line is a real incident from the session that built this entry:
while reading the bounty requirements, the agent tried to open a
133 KB single-line JSON file with the line reader, got capped at
50 KB, and only then parsed it with Python.

The program writes that single UTF-8 line to <OUTPUT_DIR>/entry.txt
(default /output). Set OUTPUT_DIR to override the output directory,
which is how the entry is tested locally.
"""

import os
from pathlib import Path

ENTRY = (
    "I fed a 133 KB one-line JSON file to the line reader, "
    "watched it choke at 50 KB, and only then remembered Python existed."
)


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
