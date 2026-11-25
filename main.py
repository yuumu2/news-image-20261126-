"""Copy entry_image.jpg next to main.py byte for byte to entry.png.
Use MAKEFUN_OUTPUT_DIR, or /output if unset, and create the directory if needed.
"""

import os
import shutil
import sys
from pathlib import Path


def main():
    source = Path(__file__).resolve().with_name("entry_image.jpg")
    try:
        image = source.open("rb")
    except FileNotFoundError:
        print(f"Error: required image is missing: {source}", file=sys.stderr)
        return 1

    with image:
        output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
        output_dir.mkdir(parents=True, exist_ok=True)
        destination = output_dir / "entry.png"
        with destination.open("wb") as output:
            shutil.copyfileobj(image, output)
            bytes_copied = output.tell()
    print(f"Copied {bytes_copied} bytes to {destination}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
