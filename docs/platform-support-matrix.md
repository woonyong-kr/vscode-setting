# Platform Support Matrix

이 문서는 macOS, Windows, VS Code, Cursor, PyCharm, IntelliJ IDEA를 함께 쓸 때 어떤 기준 파일과 스크립트를 따라야 하는지 정리한다.

## Scope

- OS: macOS, Windows
- Editors and IDEs: VS Code, Cursor, PyCharm, IntelliJ IDEA
- Canonical source: VS Code global settings and keybindings

## Matrix

| Target | Status | Canonical source | Apply path | Notes |
|---|---|---|---|---|
| VS Code on macOS | Primary | `settings.json`, `keybindings.json`, `vscode-user/` | `bash install.sh`, `python3 scripts/apply_to_vscode.py` | 기준 에디터 |
| VS Code on Windows | Primary | `settings.json`, `keybindings.json`, `vscode-user/` | `powershell -ExecutionPolicy Bypass -File .\\install.ps1`, `python scripts/apply_to_vscode.py` | `%APPDATA%\\Code\\User` 적용 |
| Cursor on macOS | Secondary | VS Code canonical files | manual verification + VS Code-compatible settings | CLI와 extension 경로 분리 가능 |
| Cursor on Windows | Secondary | VS Code canonical files | manual verification + VS Code-compatible settings | VS Code 호환이나 별도 상태 확인 필요 |
| PyCharm on macOS | Primary | `jetbrains/Codex VSCode.xml` | `python3 scripts/apply_to_pycharm.py` or `apply_to_jetbrains.py` | active keymap 강제 적용 |
| PyCharm on Windows | Primary | `jetbrains/Codex VSCode.xml` | `python scripts/apply_to_pycharm.py` or `apply_to_jetbrains.py` | `%APPDATA%\\JetBrains\\PyCharm*` 사용 |
| IntelliJ IDEA on macOS | Primary | `jetbrains/Codex VSCode.xml` | `python3 scripts/apply_to_jetbrains.py` | JetBrains 공통 정책 적용 |
| IntelliJ IDEA on Windows | Primary | `jetbrains/Codex VSCode.xml` | `python scripts/apply_to_jetbrains.py` | `%APPDATA%\\JetBrains\\IntelliJIdea*` 사용 |

## Policy

- VS Code는 동작 기준이다.
- Cursor는 VS Code 호환 편집기로 취급하지만, 별도 CLI와 확장 상태를 검증한다.
- PyCharm과 IntelliJ IDEA는 `Codex VSCode` keymap을 공유한다.
- macOS와 Windows 모두에서 OS 단축키는 수정하지 않는다.
- 충돌은 IDE keymap override에서 해결한다.

## Required Validation

- VS Code:
  - `settings.json` 과 `keybindings.json` 이 저장소 기준과 일치하는지 확인
  - `Developer: Reload Window` 후 핵심 키 동작 확인
- JetBrains:
  - `Codex VSCode` 가 active keymap인지 확인
  - keymaps 디렉터리에 XML이 복사되었는지 확인
  - IDE 재시작 후 탭 이동, 북마크, 참조 검색, 디버그 키 확인

## AI Checklist

1. 대상 OS와 IDE를 식별한다.
2. `ai/manifest.json` 에서 해당 apply script를 찾는다.
3. VS Code 기준 의도를 유지한 채 IDE별 액션으로 매핑한다.
4. OS shortcut 변경 없이 적용 가능한지 확인한다.
5. 변경이 있으면 정책 문서와 manifest를 같이 갱신한다.
