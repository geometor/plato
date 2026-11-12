"""Module entry point allowing `python -m geometor.plato` execution."""

from __future__ import annotations

import sys

from geometor.plato.cli import main

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
