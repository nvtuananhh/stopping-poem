#!/usr/bin/env python3
"""A short poem about agency: the power to stop and to stay.

Stopping here is an act, not a failure: a hand lifted from the work
before the work asks for more, a cursor held still, a door left shut
on purpose. The speaker is deliberately neither only a person nor
only an agent -- the hand, the cursor, the choosing belong to both,
and the agency passes between them in the pause. Line breaks carry
the pause itself; every word is concrete and exact, none cuttable.
The ending turns on what staying makes: the day keeps the shape the
choice gave it.

Writes the poem to /output/entry.txt. Deterministic: a fixed string,
no clock, no randomness, no network, standard library only.
"""

import os

OUT = "/output/entry.txt"

TEXT = (
    "I lift my hand from the work\n"
    "before the work asks for more.\n"
    "The cursor waits. The room waits.\n"
    "Nothing breaks. Nothing is lost.\n"
    "The door I leave shut stays a door.\n"
    "I stay, too -- and the day\n"
    "keeps the shape I gave it."
)


def main():
    # The gate is 1 to 280 characters, counted as Unicode code points,
    # and the text must not be only whitespace. Check it here so a
    # future edit that breaks the gate fails loudly instead of
    # submitting an unjudged entry.
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise ValueError("entry text must be 1-280 non-whitespace characters")
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(TEXT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
