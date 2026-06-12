#!/usr/bin/env python3
"""Validate chapter frontmatter presence.

This MVP script is intentionally conservative: it checks Markdown files under
module chapter folders and reports files that do not start with YAML
frontmatter. It does not rewrite files.
"""

from pathlib import Path


def main() -> int:
    failures = []
    for path in Path("modules").glob("*/chapters/*.md"):
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            failures.append(path)
    for path in failures:
        print(f"missing frontmatter: {path}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
