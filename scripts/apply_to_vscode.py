#!/usr/bin/env python3
from pathlib import Path
import json
import shutil
import sys

REPO_ROOT = Path(__file__).resolve().parent.parent
SNAPSHOT_ROOT = REPO_ROOT / 'vscode-user'
USER_DIR = Path.home() / 'Library/Application Support/Code/User'
PROFILE_NAME = 'woonyong'


def find_profile_location() -> str:
    storage_path = USER_DIR / 'globalStorage' / 'storage.json'
    data = json.loads(storage_path.read_text())
    for item in data.get('userDataProfiles', []):
        if item.get('name') == PROFILE_NAME:
            return item['location']
    raise SystemExit(f"Profile '{PROFILE_NAME}' not found. Open VS Code and create/select it once, then rerun.")


def mirror(src: Path, dst: Path) -> None:
    if src.is_dir():
        dst.mkdir(parents=True, exist_ok=True)
        for item in src.iterdir():
            target = dst / item.name
            if item.is_dir():
                mirror(item, target)
            else:
                shutil.copy2(item, target)
    else:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)


profile_location = find_profile_location()
profile_dir = USER_DIR / 'profiles' / profile_location

mirror(SNAPSHOT_ROOT / 'settings.json', USER_DIR / 'settings.json')
mirror(SNAPSHOT_ROOT / 'tasks.json', USER_DIR / 'tasks.json')
mirror(SNAPSHOT_ROOT / 'snippets', USER_DIR / 'snippets')
mirror(SNAPSHOT_ROOT / 'profiles' / PROFILE_NAME / 'settings.json', profile_dir / 'settings.json')
mirror(SNAPSHOT_ROOT / 'profiles' / PROFILE_NAME / 'tasks.json', profile_dir / 'tasks.json')
mirror(SNAPSHOT_ROOT / 'profiles' / PROFILE_NAME / 'snippets', profile_dir / 'snippets')

print('Applied snapshot to VS Code user settings.')
print('Run "Developer: Reload Window" in VS Code if changes are not visible yet.')
