#!/usr/bin/env python3
from pathlib import Path
import subprocess

REPO_ROOT = Path(__file__).resolve().parent.parent
SNAPSHOT_ROOT = REPO_ROOT / 'vscode-user'
PROFILE_NAME = 'woonyong'


def install(lines, profile=None):
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        cmd = ['code']
        if profile:
            cmd += ['--profile', profile]
        cmd += ['--install-extension', line]
        subprocess.run(cmd, check=True)


global_lines = (SNAPSHOT_ROOT / 'extensions-global.txt').read_text().splitlines()
profile_lines = (SNAPSHOT_ROOT / 'profiles' / PROFILE_NAME / 'extensions.txt').read_text().splitlines()

install(global_lines)
install(profile_lines, profile=PROFILE_NAME)

print('Installed extensions from snapshot.')
