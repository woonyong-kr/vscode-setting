#!/usr/bin/env python3
from pathlib import Path
import shutil
import sys

REPO_ROOT = Path(__file__).resolve().parent.parent
KEYMAP_NAME = "Codex VSCode"
SOURCE_KEYMAP = REPO_ROOT / "jetbrains" / f"{KEYMAP_NAME}.xml"
JETBRAINS_ROOT = Path.home() / "Library/Application Support/JetBrains"


def ide_config_dirs() -> list[Path]:
    candidates = []
    for path in sorted(JETBRAINS_ROOT.iterdir(), key=lambda p: p.name):
        if not path.is_dir():
            continue
        if not (path / "options").is_dir():
            continue
        if path.name in {"Daemon", "acp-agents", "bl", "consentOptions", "crl"}:
            continue
        candidates.append(path)
    return candidates


def apply_to_config(config_dir: Path) -> None:
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


def main() -> None:
    if sys.platform != "darwin":
        raise SystemExit("This helper currently supports macOS only.")

    targets = ide_config_dirs()
    if not targets:
        raise SystemExit("No JetBrains IDE config directories were found.")

    for config_dir in targets:
        apply_to_config(config_dir)
        print(f"Applied '{KEYMAP_NAME}' to {config_dir.name}.")

    print("Restart JetBrains IDEs to reload the active keymap.")


if __name__ == "__main__":
    main()
