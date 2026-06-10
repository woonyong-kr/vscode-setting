$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$UserDir = Join-Path $env:APPDATA "Code\User"

Write-Host "VS Code global settings installer for Windows"
Write-Host ""

function Backup-Path {
    param([string]$Path)

    if (Test-Path -LiteralPath $Path) {
        $stamp = Get-Date -Format "yyyyMMdd_HHmmss"
        $backup = "$Path.backup.$stamp"

        if (Test-Path -LiteralPath $Path -PathType Container) {
            Copy-Item -LiteralPath $Path -Destination $backup -Recurse -Force
        } else {
            Copy-Item -LiteralPath $Path -Destination $backup -Force
        }

        Write-Host "[backup] $Path -> $backup"
    }
}

function Copy-FileSnapshot {
    param(
        [string]$Source,
        [string]$Destination
    )

    if (Test-Path -LiteralPath $Source -PathType Leaf) {
        Backup-Path $Destination
        New-Item -ItemType Directory -Force -Path (Split-Path -Parent $Destination) | Out-Null
        Copy-Item -LiteralPath $Source -Destination $Destination -Force
        Write-Host "  copied $(Split-Path -Leaf $Destination)"
    }
}

function Copy-DirectorySnapshot {
    param(
        [string]$Source,
        [string]$Destination
    )

    if (Test-Path -LiteralPath $Source -PathType Container) {
        Backup-Path $Destination
        New-Item -ItemType Directory -Force -Path (Split-Path -Parent $Destination) | Out-Null
        if (Test-Path -LiteralPath $Destination) {
            Remove-Item -LiteralPath $Destination -Recurse -Force
        }
        Copy-Item -LiteralPath $Source -Destination $Destination -Recurse -Force
        Write-Host "  copied $(Split-Path -Leaf $Destination)"
    }
}

Write-Host "[1/3] Applying VS Code User settings"
New-Item -ItemType Directory -Force -Path $UserDir | Out-Null
Copy-FileSnapshot (Join-Path $ScriptDir "settings.json") (Join-Path $UserDir "settings.json")
Copy-FileSnapshot (Join-Path $ScriptDir "keybindings.json") (Join-Path $UserDir "keybindings.json")
Copy-FileSnapshot (Join-Path $ScriptDir "vscode-user\tasks.json") (Join-Path $UserDir "tasks.json")
Copy-DirectorySnapshot (Join-Path $ScriptDir "vscode-user\snippets") (Join-Path $UserDir "snippets")

Write-Host "[2/3] Installing extensions"
$code = Get-Command code -ErrorAction SilentlyContinue
if ($null -eq $code) {
    Write-Warning "The 'code' command was not found. Install VS Code and add it to PATH, then rerun this script."
} else {
    $installed = 0
    $failed = 0
    $extensionsFile = Join-Path $ScriptDir "extensions.txt"

    foreach ($line in Get-Content -LiteralPath $extensionsFile) {
        $ext = $line.Trim()
        if ([string]::IsNullOrWhiteSpace($ext) -or $ext.StartsWith("#")) {
            continue
        }

        & code --install-extension $ext --force | Out-Null
        if ($LASTEXITCODE -eq 0) {
            $installed += 1
        } else {
            Write-Warning "Failed to install $ext"
            $failed += 1
        }
    }

    Write-Host "  installed: $installed, failed: $failed"
}

Write-Host "[3/3] Font note"
Write-Host "Install JetBrains Mono from https://www.jetbrains.com/lp/mono/ if it is not already installed."
Write-Host ""
Write-Host "Done. Restart VS Code or run Developer: Reload Window."
