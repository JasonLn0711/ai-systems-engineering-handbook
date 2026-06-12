#!/usr/bin/env python3
"""Print the current reading-path source file."""

from pathlib import Path


def main() -> int:
    path = Path("master-knowledge-base/03-learning-paths.md")
    print(path.read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
