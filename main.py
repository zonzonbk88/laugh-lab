#!/usr/bin/env python3
"""One-Liner Laugh Lab entry: the excuse a robot vacuum gives after eating a sock.

Writes a single short funny line to /output/entry.txt (max 200 chars).
Standard library only.
"""

import os

LINE = (
    # The joke reframes the crime as charity: the vacuum didn't eat the sock,
    # it *adopted* it — then undercuts the sentiment with a deadpan inventory
    # of the dustbin and the sock's suspiciously cheerful fate.
    "I didn't eat your sock \u2014 I adopted it. It lives in my dustbin now, "
    "rent-free, next to a Lego and three hair ties. It seems happy."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
