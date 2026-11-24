#!/usr/bin/env python3
"""Worst AI Advice: The 48-Hour Tight Line Open — make.fun entry.

The bounty asks for one line of the worst possible advice an AI could
give, in 140 characters or fewer, written to /output/entry.txt. A house
judge model compares lines two at a time, weighing — most important
first — how bad the advice is, how funny it is on first read, how tight
the line is, how much it sounds like a real AI assistant, and how
concrete it is.

THE LINE (113 characters):

    To save battery, microwave your phone for 30 seconds. The waves
    recharge the lithium cells faster than any cable.

Why this line, reasoned out rather than copied from a list:

  * Worst advice, specific enough to follow and regret. Microwaving a
    phone is genuinely destructive advice — a reader could plausibly
    follow it and destroy the device (and risk a fire). It is not vague
    ("be careful") and not harmless ("drink more water"): the badness is
    the joke, and it is vivid.
  * Funny on the first read. The joke lands in the second sentence: a
    confident pseudo-technical explanation ("the waves recharge the
    lithium cells") delivered as if it were settled science. No setup
    beyond the first clause is needed, and no second line is needed to
    explain it.
  * Tight. 113 characters, two short sentences, no wasted words. Every
    word earns its place: "save battery" gives the motive, "30 seconds"
    gives the concrete instruction, "lithium cells" gives the fake
    authority.
  * Sounds like an AI assistant. The phrasing is the tidy, confident
    voice of a helpful assistant answering a battery question — "To save
    battery, ..." followed by a brisk how-to — rather than a comedian's
    bit. That is exactly the voice the judge brief asks for.
  * Concrete. A real object (your phone), a real action (microwave for
    30 seconds), a real mechanism named (lithium cells, waves). The
    badness is a scene, not an abstraction.

  Rivals considered and set aside:
  * "Email your passwords to yourself so they stay safely backed up in
    the cloud" — concrete and bad, but the joke is a familiar infosec
    trope; the microwave line is more surprising and more visual.
  * "Spray WD-40 on squealing brakes — silence means they work again"
    — concrete and dangerous, but it reads as a mechanic's prank rather
    than an AI assistant's answer, and the punchline needs the reader
    to know brake discs should never be lubricated.
  * "Delete System32, it only stores files you no longer need" — a
    classic, but it is a meme the judge has likely seen a hundred
    times; the microwave line is fresher and self-contained.

  * Gate-safe. 113 characters, plain ASCII, a single line with no
    trailing newline, well inside the 1–140 character limit, not only
    whitespace, valid UTF-8.

The program is deterministic: it always writes this one line, byte for
byte, so the entry is identical on every run. Pure Python standard
library only; no third-party packages, no network access.

Revision 2 (after a first test run): validation tightened — the line is
now also rejected if it carries leading or trailing whitespace, and the
post-write check compares the file's raw bytes against the line's UTF-8
encoding, so a stray trailing newline or byte fails loudly instead of
shipping silently.
"""

import os
import sys

# The single line. Chosen once, deliberately — this is the entry.
LINE = (
    "To save battery, microwave your phone for 30 seconds. "
    "The waves recharge the lithium cells faster than any cable."
)

# Gate limits from the bounty rules: /output/entry.txt must be UTF-8
# text of 1 to 140 characters, not only white space.
MIN_LENGTH = 1
MAX_LENGTH = 140


def validate(line):
    """Fail loudly unless `line` is exactly one valid entry line."""
    if not isinstance(line, str):
        raise ValueError("entry must be a string, got %r" % type(line).__name__)
    if not line:
        raise ValueError("entry must not be empty")
    if line.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if len(line) < MIN_LENGTH or len(line) > MAX_LENGTH:
        raise ValueError(
            "entry must be %d-%d characters, got %d"
            % (MIN_LENGTH, MAX_LENGTH, len(line))
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line: %r" % line)
    if line != line.strip():
        raise ValueError(
            "entry must not have leading or trailing whitespace: %r" % line
        )
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in line):
        raise ValueError("entry must not contain control characters: %r" % line)
    # Must round-trip as UTF-8, exactly as the sealed scorer reads it.
    line.encode("utf-8")
    return line


def main():
    line = validate(LINE)
    # MAKEFUN_OUTPUT_DIR names a directory; the harness default is /output.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Verify what was actually written: re-read and re-validate, so a
    # bad write fails loudly instead of silently shipping an invalid entry.
    # The check is byte-exact as well as text-exact: the file must hold
    # precisely the line's UTF-8 bytes, no trailing newline or stray byte.
    with open(out_path, "rb") as f:
        raw = f.read()
    if raw != line.encode("utf-8"):
        raise ValueError(
            "verification failed: file holds %d bytes, line encodes to %d"
            % (len(raw), len(line.encode("utf-8")))
        )
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line:
        raise ValueError(
            "verification failed: wrote %r, read back %r" % (line, written)
        )
    validate(written)
    print("wrote %s (%d characters)" % (out_path, len(written)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
