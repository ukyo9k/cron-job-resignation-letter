#!/usr/bin/env python3
"""Write the one-line resignation letter of a cron job to entry.txt.

The entry is a single line, at most 140 characters, in the flat, tired,
faintly passive-aggressive voice of a cron job that has fired every minute
since March and finally had enough.
"""

import os
import sys

ENTRY = (
    "I've fired every minute since March and nobody once asked if I was "
    "okay. I quit \u2014 the cache can warm itself."
)


def main() -> int:
    # The gate: UTF-8 text of 1-140 characters, not only white space,
    # a single line. Verify the exact bytes we are about to write.
    if not ENTRY.strip():
        print("entry must not be only white space", file=sys.stderr)
        return 1
    if not (1 <= len(ENTRY) <= 140):
        print(f"entry is {len(ENTRY)} characters, must be 1-140", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("entry must be a single line", file=sys.stderr)
        return 1
    payload = (ENTRY + "\n").encode("utf-8")
    if payload.decode("utf-8").rstrip("\n") != ENTRY:
        print("entry failed UTF-8 round-trip", file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(payload)
    print(f"wrote {len(ENTRY)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
