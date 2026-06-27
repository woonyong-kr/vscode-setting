#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import shutil

from jetbrains_paths import active_keymap_paths, jetbrains_root

REPO_ROOT = Path(__file__).resolve().parent.parent
KEYMAP_NAME = "Codex VSCode"
SOURCE_KEYMAP = REPO_ROOT / "jetbrains" / f"{KEYMAP_NAME}.xml"
JETBRAINS_ROOT = jetbrains_root()


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


def main() -> None:
    targets = ide_config_dirs()
    if not targets:
        raise SystemExit("No JetBrains IDE config directories were found.")

    for config_dir in targets:
        apply_to_config(config_dir)
        print(f"Applied '{KEYMAP_NAME}' to {config_dir.name}.")

    print("Restart JetBrains IDEs to reload the active keymap.")


if __name__ == "__main__":
    main()
