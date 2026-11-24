#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second.

Writes one sentence (<= 200 characters) pitching a bizarre startup idea
that sounds absurd until the business logic lands, to /output/entry.txt.

The pitch: a dog that performs in divorce court. Pet custody is the
fight nobody settles in a divorce, and divorcing spouses already spend
thousands on it -- so a trained dog that demonstrates, in front of a
judge, which spouse it obeys is a service with a real payer, a real
budget, and a real market. Bizarre at first glance; a real business
on the second.

Stdlib only. No network, no files read, no environment secrets.
Deterministic: the same pitch on every run.
"""

import os

PITCH = (
    "We train dogs to perform in divorce court \u2014 $500 a case, "
    "because pet custody is the fight nobody settles, and the spouse "
    "a dog obeys in front of a judge is the one who keeps it."
)

OUTPUT_PATH = os.path.join(os.environ.get("OUTPUT_DIR", "/output"), "entry.txt")


def main() -> None:
    text = PITCH.strip()
    assert 1 <= len(text) <= 200, "pitch must be 1-200 characters"
    assert text and not text.isspace(), "pitch must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "pitch must be a single line"
    assert text.count(".") == 1 and text.endswith("."), "pitch must be one sentence"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
