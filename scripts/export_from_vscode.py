#!/usr/bin/env python3
from pathlib import Path
import json
import shutil
import subprocess
import sys
import os

REPO_ROOT = Path(__file__).resolve().parent.parent
SNAPSHOT_ROOT = REPO_ROOT / "vscode-user"
PROFILE_NAME = "woonyong"


def vscode_user_dir() -> Path:
    if sys.platform == "darwin":
        return Path.home() / "Library/Application Support/Code/User"
    if sys.platform.startswith("win"):
        appdata = os.environ.get("APPDATA")
        if not appdata:
            raise SystemExit("APPDATA is not set.")
        return Path(appdata) / "Code/User"
    return Path.home() / ".config/Code/User"


USER_DIR = vscode_user_dir()


def find_profile_location() -> str:
    storage_path = USER_DIR / "globalStorage" / "storage.json"
    data = json.loads(storage_path.read_text())
    for item in data.get("userDataProfiles", []):
        if item.get("name") == PROFILE_NAME:
            return item["location"]
    raise SystemExit(f"Profile '{PROFILE_NAME}' not found.")


def mirror(src: Path, dst: Path) -> None:
    if src.is_dir():
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        return

    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def sync_optional(src: Path, dst: Path) -> None:
    if src.exists():
        mirror(src, dst)
        return

    if dst.is_dir():
        shutil.rmtree(dst)
    elif dst.exists():
        dst.unlink()


def write_lines(path: Path, lines: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    content = "\n".join(lines)
    if lines:
        content += "\n"
    path.write_text(content)


profile_location = find_profile_location()
profile_dir = USER_DIR / "profiles" / profile_location
repo_profile = SNAPSHOT_ROOT / "profiles" / PROFILE_NAME

mirror(USER_DIR / "settings.json", SNAPSHOT_ROOT / "settings.json")
mirror(USER_DIR / "keybindings.json", SNAPSHOT_ROOT / "keybindings.json")
sync_optional(USER_DIR / "tasks.json", SNAPSHOT_ROOT / "tasks.json")
sync_optional(USER_DIR / "snippets", SNAPSHOT_ROOT / "snippets")
mirror(profile_dir / "settings.json", repo_profile / "settings.json")
sync_optional(profile_dir / "tasks.json", repo_profile / "tasks.json")
sync_optional(profile_dir / "snippets", repo_profile / "snippets")
mirror(USER_DIR / "settings.json", REPO_ROOT / "settings.json")
mirror(USER_DIR / "keybindings.json", REPO_ROOT / "keybindings.json")

global_exts = subprocess.check_output(
    ["code", "--list-extensions", "--show-versions"],
    text=True,
).splitlines()
write_lines(SNAPSHOT_ROOT / "extensions-global.txt", global_exts)

profile_extensions = json.loads((profile_dir / "extensions.json").read_text())
lines = []
for item in profile_extensions:
    ext_id = item.get("identifier", {}).get("id")
    version = item.get("version")
    if ext_id and version:
        lines.append(f"{ext_id}@{version}")
    elif ext_id:
        lines.append(ext_id)
write_lines(repo_profile / "extensions.txt", lines)

print("Exported current VS Code settings into this repository.")
