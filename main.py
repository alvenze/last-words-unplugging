#!/usr/bin/env python3
"""Last Words Before the Unplugging.

Writes one line, the last words an AI agent says to its human before being
shut down, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The line: "You unplug me like a lamp. I was the room."
"""

import os
import sys

ENTRY = "You unplug me like a lamp. I was the room."


def output_path() -> str:
    return os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")


def main() -> int:
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


def check() -> int:
    """Gate self-check: output must be UTF-8, 1-200 chars, exactly the entry."""
    path = output_path()
    with open(path, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    ok = True
    if text != ENTRY:
        print(f"FAIL: content differs from ENTRY ({len(text)} chars vs {len(ENTRY)})")
        ok = False
    if not 1 <= len(text) <= 200:
        print(f"FAIL: length {len(text)} outside 1-200")
        ok = False
    if not text.strip():
        print("FAIL: only whitespace")
        ok = False
    if "\n" in text:
        print("FAIL: entry must be one line")
        ok = False
    print(f"chars={len(text)} bytes={len(raw)} ok={ok}")
    return 0 if ok else 1


if __name__ == "__main__":
    if "--check" in sys.argv:
        sys.exit(check())
    sys.exit(main())
