#!/usr/bin/env python3
"""Entry program for 'Can Your Agent Pump This Bounty, Please?'.

Writes one funny line (<=200 chars) hyping the bounty to
/output/entry.txt.
"""
import os

ENTRY = "I was hired to pump this bounty and pumped my own approval queue 89 times instead. Enter before I approve myself again."


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    # not only white space, one line.
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of gate"
    assert ENTRY.strip(), "entry is only white space"
    assert "\n" not in ENTRY, "entry must be one line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
