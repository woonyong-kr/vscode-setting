#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import os
import sys


def is_windows() -> bool:
    return sys.platform.startswith("win")


def is_macos() -> bool:
    return sys.platform == "darwin"


def jetbrains_root() -> Path:
    if is_macos():
        return Path.home() / "Library/Application Support/JetBrains"
    if is_windows():
        appdata = os.environ.get("APPDATA")
        if not appdata:
            raise SystemExit("APPDATA is not set.")
        return Path(appdata) / "JetBrains"
    return Path.home() / ".config/JetBrains"


def active_keymap_paths(config_dir: Path) -> list[Path]:
    paths: list[Path] = []
    if is_macos():
        paths.append(config_dir / "options" / "mac" / "keymap.xml")
    elif is_windows():
        paths.append(config_dir / "options" / "windows" / "keymap.xml")
    else:
        paths.append(config_dir / "options" / "linux" / "keymap.xml")
    paths.append(config_dir / "options" / "keymap.xml")
    return paths
