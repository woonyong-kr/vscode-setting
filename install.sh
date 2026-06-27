#!/bin/bash
# ============================================================
# IDE 공통 세팅 일괄 설치 스크립트
# 사용법: bash ~/workspace/ide-setting/install.sh
# 새 컴퓨터/환경에서 이 스크립트 하나로 동일 세팅 복원
# ============================================================

set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# macOS / Linux 분기
if [[ "$OSTYPE" == "darwin"* ]]; then
    VSCODE_USER_DIR="$HOME/Library/Application Support/Code/User"
    CODE_CMD="code"
else
    VSCODE_USER_DIR="$HOME/.config/Code/User"
    CODE_CMD="code"
fi

echo "╔══════════════════════════════════════╗"
echo "║    IDE 공통 세팅 설치 스크립트      ║"
echo "╚══════════════════════════════════════╝"
echo ""

backup_path() {
    local target="$1"
    if [ -e "$target" ]; then
        local backup="$target.backup.$(date +%Y%m%d_%H%M%S)"
        if [ -d "$target" ]; then
            cp -R "$target" "$backup"
        else
            cp "$target" "$backup"
        fi
        echo "[백업] $target → $backup"
    fi
}

copy_file() {
    local src="$1"
    local dst="$2"
    if [ -f "$src" ]; then
        backup_path "$dst"
        mkdir -p "$(dirname "$dst")"
        cp "$src" "$dst"
        echo "  ✓ $(basename "$dst") 적용"
    fi
}

copy_dir() {
    local src="$1"
    local dst="$2"
    if [ -d "$src" ]; then
        backup_path "$dst"
        mkdir -p "$(dirname "$dst")"
        rm -rf "$dst"
        cp -R "$src" "$dst"
        echo "  ✓ $(basename "$dst") 적용"
    fi
}

# 1. User 설정 파일 복원
echo ""
echo "[1/4] VS Code User 설정 적용..."
mkdir -p "$VSCODE_USER_DIR"
copy_file "$SCRIPT_DIR/settings.json" "$VSCODE_USER_DIR/settings.json"
copy_file "$SCRIPT_DIR/keybindings.json" "$VSCODE_USER_DIR/keybindings.json"
copy_file "$SCRIPT_DIR/vscode-user/tasks.json" "$VSCODE_USER_DIR/tasks.json"
copy_dir "$SCRIPT_DIR/vscode-user/snippets" "$VSCODE_USER_DIR/snippets"

# 2. 확장 프로그램 설치
echo "[2/4] 확장 프로그램 설치 (시간이 걸립니다)..."
installed=0
failed=0
if ! command -v "$CODE_CMD" >/dev/null 2>&1; then
    echo "  ⚠ code 명령을 찾을 수 없습니다. VS Code에서 Shell Command: Install 'code' command in PATH 실행 후 다시 시도하세요."
else
    while IFS= read -r ext; do
        # 빈 줄, 주석 건너뛰기
        [[ -z "$ext" || "$ext" == \#* ]] && continue
        if $CODE_CMD --install-extension "$ext" --force >/dev/null 2>&1; then
            installed=$((installed + 1))
        else
            echo "  ⚠ $ext 설치 실패"
            failed=$((failed + 1))
        fi
    done < "$SCRIPT_DIR/extensions.txt"
    echo "  ✓ $installed개 설치, $failed개 실패"
fi

# 3. JetBrains Mono 폰트 확인
echo "[3/4] JetBrains Mono 폰트 확인..."
if fc-list 2>/dev/null | grep -qi "JetBrains Mono"; then
    echo "  ✓ 이미 설치됨"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    echo "  → brew로 설치 시도..."
    brew install --cask font-jetbrains-mono 2>/dev/null || \
        echo "  ⚠ brew로 설치 실패. https://www.jetbrains.com/lp/mono/ 에서 수동 설치"
else
    echo "  → apt로 설치 시도..."
    sudo apt-get install -y fonts-jetbrains-mono 2>/dev/null || \
        echo "  ⚠ 수동 설치 필요: https://www.jetbrains.com/lp/mono/"
fi

# 4. 프로필 스냅샷 안내
echo "[4/4] 프로필 스냅샷 안내..."
echo "  → woonyong 프로필까지 맞추려면 VS Code에서 프로필을 만든 뒤 아래 명령을 실행하세요."
echo "     python3 scripts/apply_to_vscode.py && python3 scripts/install_extensions.py"

echo ""
echo "╔══════════════════════════════════════╗"
echo "║   설치 완료! VS Code를 재시작하세요   ║"
echo "║   Cmd+Shift+P → Reload Window       ║"
echo "╚══════════════════════════════════════╝"
