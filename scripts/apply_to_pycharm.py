#!/usr/bin/env python3
from pathlib import Path
import shutil
import sys

REPO_ROOT = Path(__file__).resolve().parent.parent
KEYMAP_NAME = "Codex VSCode"
SOURCE_KEYMAP = REPO_ROOT / "jetbrains" / f"{KEYMAP_NAME}.xml"
JETBRAINS_ROOT = Path.home() / "Library/Application Support/JetBrains"


def latest_pycharm_dir() -> Path:
    candidates = sorted(
        [path for path in JETBRAINS_ROOT.glob("PyCharm*") if path.is_dir()],
        key=lambda path: path.name,
    )
    if not candidates:
        raise SystemExit("PyCharm config directory was not found.")
    return candidates[-1]


def main() -> None:
    if sys.platform != "darwin":
        raise SystemExit("This helper currently supports macOS only.")

    config_dir = latest_pycharm_dir()
    keymaps_dir = config_dir / "keymaps"
    options_dir = config_dir / "options" / "mac"
    target_keymap = keymaps_dir / SOURCE_KEYMAP.name
    target_active = options_dir / "keymap.xml"

    keymaps_dir.mkdir(parents=True, exist_ok=True)
    options_dir.mkdir(parents=True, exist_ok=True)

    shutil.copy2(SOURCE_KEYMAP, target_keymap)
    target_active.write_text(
        "<application>\n"
        "  <component name=\"KeymapManager\">\n"
        f"    <active_keymap name=\"{KEYMAP_NAME}\" />\n"
        "  </component>\n"
        "</application>\n"
    )

    print(f"Applied '{KEYMAP_NAME}' to {config_dir.name}.")
    print("Restart PyCharm to reload the active keymap.")


if __name__ == "__main__":
    main()
