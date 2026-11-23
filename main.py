#!/usr/bin/env python3
"""One-Line Laugh Sprint v2 entry writer for make.fun.

Writes the sprint's one-line joke to /output/entry.txt with no trailing
newline. Python 3 standard library only, deterministic, no network access.
"""

from pathlib import Path

ENTRY = "My plants died of neglect, so I bought plastic ones, and now I feel guilty for not watering those too."
# Written to /output/entry.txt with no trailing newline (sprint requirement)
OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
