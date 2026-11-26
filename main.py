"""Funniest Cat Voicemail Greeting.

The program writes one voicemail greeting, as recorded by the cat
himself, to the output directory. The cat has taken the phone, the
charger, the plant and one sock hostage, and the greeting is his
ransom note: leave a message after the beep, and a treat by the
door, if the caller wants any of it back.
"""

import os
import sys

GREETING = "You've reached Chairman Meow. Your charger, plant and sock are mine. Leave a message — and a treat — to get them back."

MAX_CHARS = 120


def describe_greeting(text):
    """Summarise the greeting for the run log.

    Counts characters (what the gate measures) and UTF-8 bytes
    (what the file holds), and rejects any control character that
    would not survive the trip to the judge. The em dash in the
    greeting is one character but three bytes, so the two counts
    are deliberately reported side by side.
    """
    encoded = text.encode("utf-8")
    for char in text:
        if ord(char) < 32 and char not in ("\t",):
            raise ValueError("greeting holds a control character: U+%04X" % ord(char))
    return "{} characters, {} UTF-8 bytes".format(len(text), len(encoded))


def validate_greeting(text):
    """Refuse to write a greeting the house gate would reject.

    The gate takes a single line of UTF-8 text, 1 to 120 characters,
    not only whitespace. A greeting outside that never reaches the
    judge, so fail here instead of shipping a dead entry.
    """
    if not isinstance(text, str):
        raise TypeError("greeting must be text")
    if not text.strip():
        raise ValueError("greeting must not be only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "greeting is {} characters, over the {} limit".format(
                len(text), MAX_CHARS
            )
        )
    if "\n" in text or "\r" in text:
        raise ValueError("greeting must be a single line")
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    line = validate_greeting(GREETING)
    summary = describe_greeting(line)
    target = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(line)
    print("wrote {} ({})".format(target, summary))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
