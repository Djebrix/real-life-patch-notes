#!/usr/bin/env python3
"""Real Life Patch Notes: The Comedy Changelog.

One-line patch note for the 3 a.m. embarrassing-memory replay bug:
the brain replays your worst moment from 2011 with no skip button.
Writes it to /output/entry.txt (or $ENTRY_OUTPUT_DIR/entry.txt).
Standard library only, deterministic.
"""

import os

TEXT = (
    "v2.1.7: fixed a bug where the brain replayed your most embarrassing "
    "moment from 2011 at 3 a.m. with no skip button and full surround sound."
)


def main() -> None:
    text = TEXT.strip()
    assert 1 <= len(text) <= 160, f"patch note must be 1-160 chars, got {len(text)}"
    assert text.strip(), "patch note must not be whitespace-only"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
