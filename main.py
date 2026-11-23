#!/usr/bin/env python3
"""Write the One-Line Laugh Sprint entry to /output/entry.txt."""

from pathlib import Path

ENTRY = "I made my Wi-Fi password unguessable, and now the only person locked out of my own internet is me."
# Entries are written to /output/entry.txt as required by the sprint judge.
OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
