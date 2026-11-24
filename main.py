"""Last Text at One Percent — entry for make.fun.

Writes the phone's final text message to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Pure Python stdlib, deterministic, no network.
"""

import os

LINE = (
    "before i go: your screen time was 11 hours a day and i never told "
    "anyone. delete my search history. tell my charger i loved her."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
