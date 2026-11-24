#!/usr/bin/env python3
"""One-Liner Laugh Lab entry (variant A).

Writes the final one-liner to /output/entry.txt and to entry.txt
in the repo root. Deterministic: no randomness, no network.
"""

import os

LINE = (
    "My obstacle sensor flagged your sock as debris, so I filed "
    "ticket #404, closed it, and ate the evidence. "
    "No further action required."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Best-effort convenience copy next to this script (repo root).
    # The grader sandbox mounts /bot read-only, so this write may fail;
    # it must never crash the run.
    try:
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt"),
                   "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        pass


if __name__ == "__main__":
    main()
