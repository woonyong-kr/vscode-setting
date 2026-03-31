#!/usr/bin/env python3
from pathlib import Path
import json
import shutil
import subprocess

REPO_ROOT = Path(__file__).resolve().parent.parent
SNAPSHOT_ROOT = REPO_ROOT / "vscode-user"
USER_DIR = Path.home() / "Library/Application Support/Code/User"
PROFILE_NAME = "woonyong"


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
mirror(USER_DIR / "tasks.json", SNAPSHOT_ROOT / "tasks.json")
mirror(USER_DIR / "snippets", SNAPSHOT_ROOT / "snippets")
mirror(profile_dir / "settings.json", repo_profile / "settings.json")
mirror(profile_dir / "tasks.json", repo_profile / "tasks.json")
mirror(profile_dir / "snippets", repo_profile / "snippets")

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
