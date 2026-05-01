#!/bin/bash
# ============================================================
# VS Code 글로벌 세팅 일괄 설치 스크립트
# 사용법: bash ~/workspace/vscode-setting/install.sh
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
echo "║   VS Code 글로벌 세팅 설치 스크립트  ║"
echo "╚══════════════════════════════════════╝"
echo ""

# 0. 기존 설정 백업
if [ -f "$VSCODE_USER_DIR/settings.json" ]; then
    BACKUP="$VSCODE_USER_DIR/settings.backup.$(date +%Y%m%d_%H%M%S).json"
    cp "$VSCODE_USER_DIR/settings.json" "$BACKUP"
    echo "[백업] 기존 settings.json → $BACKUP"
fi

# 1. settings.json 복사
echo ""
echo "[1/4] settings.json 적용..."
mkdir -p "$VSCODE_USER_DIR"
cp "$SCRIPT_DIR/settings.json" "$VSCODE_USER_DIR/settings.json"
echo "  ✓ 완료"

# 2. keybindings.json 복사
echo "[2/4] keybindings.json 적용..."
cp "$SCRIPT_DIR/keybindings.json" "$VSCODE_USER_DIR/keybindings.json"
echo "  ✓ 완료"

# 3. 확장 프로그램 설치
echo "[3/4] 확장 프로그램 설치 (시간이 걸립니다)..."
installed=0
failed=0
while IFS= read -r ext; do
    # 빈 줄, 주석 건너뛰기
    [[ -z "$ext" || "$ext" == \#* ]] && continue
    if $CODE_CMD --install-extension "$ext" --force >/dev/null 2>&1; then
        ((installed++))
    else
        echo "  ⚠ $ext 설치 실패"
        ((failed++))
    fi
done < "$SCRIPT_DIR/extensions.txt"
echo "  ✓ $installed개 설치, $failed개 실패"

# 4. JetBrains Mono 폰트 확인
echo "[4/4] JetBrains Mono 폰트 확인..."
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

echo ""
echo "╔══════════════════════════════════════╗"
echo "║   설치 완료! VS Code를 재시작하세요   ║"
echo "║   Cmd+Shift+P → Reload Window       ║"
echo "╚══════════════════════════════════════╝"
