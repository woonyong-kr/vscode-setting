#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import json
import os
import platform
import re
import shutil
import subprocess
from datetime import datetime, timezone

REPO_ROOT = Path(__file__).resolve().parent.parent
SNAPSHOT_DIR = REPO_ROOT / "snapshots"


def command_exists(name: str) -> bool:
    return shutil.which(name) is not None


def sanitize_version(command: str, version: str) -> str:
    if command == "pip3":
        match = re.match(r"^(pip [^ ]+) from .+ \((python .+)\)$", version)
        if match:
            return f"{match.group(1)} ({match.group(2)})"
    return version


def capture(cmd: list[str]) -> dict[str, object]:
    try:
        completed = subprocess.run(
            cmd,
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return {"available": False}

    stdout = completed.stdout.strip()
    first_line = stdout.splitlines()[0] if stdout else ""
    return {
        "available": True,
        "command": cmd[0],
        "version": sanitize_version(cmd[0], first_line),
    }


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def write_lines(path: Path, lines: list[str]) -> None:
    content = "\n".join(lines)
    if lines:
        content += "\n"
    write_text(path, content)


def main() -> None:
    shell_name = Path(os.environ.get("SHELL", "")).name or None
    snapshot = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "platform": {
            "system": platform.system(),
            "release": platform.release(),
            "machine": platform.machine(),
        },
        "shell": {
            "default": shell_name,
            "zsh": capture(["zsh", "--version"]) if command_exists("zsh") else {"available": False},
            "bash": capture(["bash", "--version"]) if command_exists("bash") else {"available": False},
            "pwsh": capture(["pwsh", "-Version"]) if command_exists("pwsh") else {"available": False},
        },
        "tools": {
            "code": capture(["code", "--version"]),
            "cursor": capture(["cursor", "--version"]),
            "brew": capture(["brew", "--version"]),
            "node": capture(["node", "--version"]),
            "npm": capture(["npm", "--version"]),
            "pnpm": capture(["pnpm", "--version"]),
            "bun": capture(["bun", "--version"]),
            "uv": capture(["uv", "--version"]),
            "ruff": capture(["ruff", "--version"]),
            "python3": capture(["python3", "--version"]),
            "pip3": capture(["pip3", "--version"]),
            "git": capture(["git", "--version"]),
            "docker": capture(["docker", "--version"]),
            "gh": capture(["gh", "--version"]),
            "direnv": capture(["direnv", "version"]),
            "mise": capture(["mise", "--version"]),
            "volta": capture(["volta", "--version"]),
        },
    }

    write_text(
        SNAPSHOT_DIR / "tool-versions.json",
        json.dumps(snapshot, indent=2) + "\n",
    )

    if command_exists("brew"):
        formulae = subprocess.run(
            ["brew", "list", "--formula"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout.splitlines()
        casks = subprocess.run(
            ["brew", "list", "--cask"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout.splitlines()
        write_lines(SNAPSHOT_DIR / "homebrew-formulae.txt", sorted(formulae))
        write_lines(SNAPSHOT_DIR / "homebrew-casks.txt", sorted(casks))

    if command_exists("npm"):
        raw = subprocess.run(
            ["npm", "-g", "ls", "--depth=0", "--json"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout
        data = json.loads(raw)
        deps = data.get("dependencies", {})
        lines = [f"{name}@{meta['version']}" for name, meta in sorted(deps.items()) if "version" in meta]
        write_lines(SNAPSHOT_DIR / "npm-global-packages.txt", lines)


if __name__ == "__main__":
    main()
