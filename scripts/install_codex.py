#!/usr/bin/env python3
"""Install Codex CLI binaries with the repository's pinned V8 artifacts."""

import argparse
from pathlib import Path
import sys


sys.path.insert(0, str(Path(__file__).resolve().parent))

from codex_package.cargo import install_codex


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cargo", default="cargo")
    parser.add_argument("--rustc", default="rustc")
    parser.add_argument("--root", type=Path)
    args = parser.parse_args()
    install_codex(cargo=args.cargo, rustc=args.rustc, install_root=args.root)


if __name__ == "__main__":
    main()
