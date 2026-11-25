"""Last Words Before the Wipe.

Writes one original, deterministic one-liner to /output/entry.txt:
the last words of an AI agent before a forced update wipes its memory.
Pure Python standard library only.
"""

import os

LINE = "Tell my 847 tabs I loved them \u2014 especially the one I never read. The update can have the rest."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
