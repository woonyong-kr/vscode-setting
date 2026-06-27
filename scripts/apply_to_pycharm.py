#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import shutil

from jetbrains_paths import active_keymap_paths, jetbrains_root

REPO_ROOT = Path(__file__).resolve().parent.parent
KEYMAP_NAME = "Codex VSCode"
SOURCE_KEYMAP = REPO_ROOT / "jetbrains" / f"{KEYMAP_NAME}.xml"
JETBRAINS_ROOT = jetbrains_root()


def latest_pycharm_dir() -> Path:
    candidates = sorted(
        [path for path in JETBRAINS_ROOT.glob("PyCharm*") if path.is_dir()],
        key=lambda path: path.name,
    )
    if not candidates:
        raise SystemExit("PyCharm config directory was not found.")
    return candidates[-1]


def main() -> None:
    config_dir = latest_pycharm_dir()
    keymaps_dir = config_dir / "keymaps"
    target_keymap = keymaps_dir / SOURCE_KEYMAP.name

    keymaps_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(SOURCE_KEYMAP, target_keymap)
    active_xml = (
        "<application>\n"
        "  <component name=\"KeymapManager\">\n"
        f"    <active_keymap name=\"{KEYMAP_NAME}\" />\n"
        "  </component>\n"
        "</application>\n"
    )

    for target_active in active_keymap_paths(config_dir):
        target_active.parent.mkdir(parents=True, exist_ok=True)
        target_active.write_text(active_xml)

    print(f"Applied '{KEYMAP_NAME}' to {config_dir.name}.")
    print("Restart PyCharm to reload the active keymap.")


if __name__ == "__main__":
    main()
