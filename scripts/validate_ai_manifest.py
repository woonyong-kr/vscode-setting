#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import json
import sys

REPO_ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = REPO_ROOT / "ai" / "manifest.json"


def assert_exists(path_str: str) -> None:
    path = REPO_ROOT / path_str
    if not path.exists():
        raise SystemExit(f"Missing referenced path: {path_str}")


def main() -> None:
    if not MANIFEST_PATH.exists():
        raise SystemExit("Missing ai/manifest.json")

    manifest = json.loads(MANIFEST_PATH.read_text())

    for value in manifest.get("canonical_sources", {}).values():
        assert_exists(value)

    for value in manifest.get("apply_scripts", {}).values():
        assert_exists(value)

    for value in manifest.get("agent_entrypoints", []):
        assert_exists(value)

    for value in manifest.get("installers", {}).values():
        assert_exists(value)

    print("AI manifest validation passed.")


if __name__ == "__main__":
    main()
