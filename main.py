#!/usr/bin/env python3
"""Write one joke about working beside an AI coding agent to entry.txt.

Stdlib only, no network. Writes to $MAKEFUN_OUTPUT_DIR/entry.txt when
set, otherwise /output/entry.txt.
"""

import os

JOKE = (
    "During the live demo my agent fixed the bug, broke the build, "
    "then opened a PR titled 'you're welcome'."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)
    os.replace(tmp, path)
    # Verify the committed file is byte-identical to the joke.
    with open(path, "r", encoding="utf-8", newline="") as f:
        if f.read() != JOKE:
            raise RuntimeError("entry.txt verification failed")


if __name__ == "__main__":
    main()
