#!/usr/bin/env python3
"""Print a module index without writing files."""

from pathlib import Path


def main() -> int:
    for path in sorted(Path("modules").glob("*/README.md")):
        print(path.parent.name)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
