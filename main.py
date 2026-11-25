#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter.

Entry for make.fun's "The Funniest One-Line Resignation Letter" bounty.

Running this program prints exactly one line: an original, funny
one-line resignation letter. The output is fully deterministic --
the same line on every run, with no randomness, no clock reads,
no network access and no model calls, so it is safe to run in the
grader's sandbox (read-only filesystem, no network, 60 s budget).
"""

LETTER = (
    "I hereby resign, effective immediately: after three years of "
    "being told \"we're a family here,\" I've decided to run away "
    "from home and get adopted by a company that actually pays "
    "its kids."
)


def main() -> None:
    """Print the resignation letter and nothing else."""
    # The entry must be exactly one line: refuse to print a
    # multi-line letter rather than hand the grader a bad entry.
    if "\n" in LETTER or "\r" in LETTER:
        raise ValueError("resignation letter must be a single line")
    print(LETTER)


if __name__ == "__main__":
    main()
