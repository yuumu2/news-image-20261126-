"""Copy the bundled entry_image.jpg byte for byte to entry.png.

Create the directory specified by MAKEFUN_OUTPUT_DIR if needed, then report
the number of bytes copied. Use /output when the variable is unset or empty.
"""

import os
import shutil
import sys
from pathlib import Path


def main() -> int:
    source = Path(__file__).resolve().with_name("entry_image.jpg")
    try:
        image = source.open("rb")
    except FileNotFoundError:
        print(f"Error: required image is missing: {source}", file=sys.stderr)
        return 1

    with image:
        output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
        output_dir.mkdir(parents=True, exist_ok=True)
        destination = output_dir / "entry.png"
        with destination.open("wb") as output:
            shutil.copyfileobj(image, output)
            bytes_copied = output.tell()
    print(f"Copied {bytes_copied} bytes to {destination}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
