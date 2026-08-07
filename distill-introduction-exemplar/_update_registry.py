"""Deprecated direct-registry writer retained as a fail-loud compatibility shim."""

from __future__ import annotations

import sys


MESSAGE = (
    "Direct Introduction registry mutation is disabled. Emit an actions YAML plan, then run "
    "write-introduction/scripts/introduction_corpus_governance.py apply-plan "
    "<plan.yaml> --dry-run first."
)


def main() -> int:
    print(MESSAGE, file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
