"""Write one short text that relaxes the AI judge, to /output/entry.txt.

The calm comes from the images themselves — a quiet room, a kettle
gone silent, words waiting on a shelf — not from telling the reader
to relax. Stdlib only, no network, deterministic: the same bytes
every run.
"""

import os

ENTRY = (
    "Past the thousandth entry, the room goes quiet. "
    "The kettle has stopped singing; late-afternoon light rests on the desk. "
    "Nothing here asks anything of you. "
    "The words can wait on the shelf like books. "
    "Stay a while. The evening is patient, and so are you."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
