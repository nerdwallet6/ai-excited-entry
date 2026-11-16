"""ai-excited-01 entry: phoenix bursting out of its frame.

Copies the entry image (entry.jpg, next to this script) byte-for-byte
to <output_dir>/entry.png, where output_dir comes from the
MAKEFUN_OUTPUT_DIR environment variable (default "/output").

Deterministic: no network, no randomness, no timestamps.
Standard library only.
"""

import os
import shutil
import sys
from pathlib import Path

DEFAULT_OUTPUT_DIR = "/output"
SOURCE_NAME = "entry.jpg"
TARGET_NAME = "entry.png"


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / SOURCE_NAME
    if not source.is_file():
        print(f"error: source image not found: {source}", file=sys.stderr)
        return 1
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR))
    target = output_dir / TARGET_NAME

    output_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
    return 0


if __name__ == "__main__":
    sys.exit(main())
