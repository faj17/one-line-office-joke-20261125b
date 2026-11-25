#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry: writes one original office joke
to /output/entry.txt.

The joke is built from two fragments: a SETUP that states the change —
the water cooler replaced by a Slack channel — and a PUNCH that turns
it into a joke: the office gossip now has a search function. The water
cooler was the classic gossip spot; digitising it gives the rumour mill
a feature nobody asked for.
"""

import os

MAX_CHARS = 200
MAX_WORDS = 40

# Setup: the change — the physical gossip spot replaced by a channel.
SETUP = "They replaced the water cooler with a Slack channel,"
# Punch: the twist — the gossip now has a search function.
PUNCH = "so now the office gossip has a search function."


def assemble():
    """Join the fragments into the single joke line."""
    return f"{SETUP} {PUNCH}"


def validate(text):
    """Gate: 1-200 chars, single line, UTF-8, not only whitespace."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing space")
    if len(text.split()) > MAX_WORDS:
        raise ValueError(f"entry must be at most {MAX_WORDS} words")
    text.encode("utf-8")
    return text


def main():
    text = validate(assemble())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
