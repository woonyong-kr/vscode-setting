# Environment Manager

이 저장소의 목표는 Woonyong의 VS Code 중심 개발 환경을 다른 macOS 또는 Windows 환경에서 최대한 재현할 수 있게 보관하는 것입니다.

## Daily Sync

Codex 자동화 `개발환경 설정 동기화`가 하루 1회 이상 실행되도록 등록되어 있습니다. 자동화는 로컬 개발 환경을 조사하고 의미 있는 변화가 있으면 저장소 문서와 설정 스냅샷을 갱신한 뒤 커밋하고 푸시합니다.

자동화가 확인하는 범위:

- VS Code User `settings.json`, `keybindings.json`, `tasks.json`, snippets
- `woonyong` VS Code profile 설정, tasks, snippets, profile extensions
- 설치된 VS Code extensions와 버전 스냅샷
- formatter, linter, clang-format, Python, C/C++, JS/TS 관련 컨벤션
- Homebrew, Node.js/npm, Python, Git, Docker 등 개발 도구 상태 중 재현에 필요한 항목
- macOS와 Windows에서 따라 할 수 있는 설치/복원 가이드

## Reproducibility Levels

### Level 1: Team Default

팀원이 가장 쉽게 따라 할 수 있는 기본 복원입니다.

- macOS/Linux: `bash install.sh`
- Windows: `powershell -ExecutionPolicy Bypass -File .\install.ps1`

복원 대상:

- 글로벌 VS Code settings
- 글로벌 keybindings
- 글로벌 tasks
- 글로벌 snippets
- `extensions.txt`의 curated extension 목록
- JetBrains Mono 폰트 안내 또는 설치 시도

### Level 2: Profile Snapshot

`woonyong` 프로필까지 더 가깝게 맞추는 복원입니다. VS Code에서 `woonyong` 프로필을 먼저 생성하거나 선택한 뒤 실행합니다.

```bash
python3 scripts/apply_to_vscode.py
python3 scripts/install_extensions.py
```

복원 대상:

- `vscode-user/` 아래의 User 디렉토리 스냅샷
- `vscode-user/profiles/woonyong/` 아래의 프로필 스냅샷
- 버전이 포함된 extension snapshot

## Exclusions

아래 항목은 의도적으로 커밋하지 않습니다.

- API keys, tokens, passwords, certificates, SSH private keys
- VS Code 또는 extension의 로그인 세션과 계정별 secret storage
- OS keychain, browser profile, cookies
- machine-specific caches, build artifacts, temporary files
- 개인 프로젝트의 민감한 workspace state
- 재현에 필요 없는 절대 경로와 개인 식별 정보

## Platform Notes

macOS 기준 설정에는 Apple Command Line Tools의 clang 경로가 포함되어 있습니다. Windows에서 C/C++를 사용할 때는 MSVC, LLVM, MinGW 중 팀 환경에 맞는 컴파일러를 별도로 설치하고 VS Code의 compiler path를 조정해야 합니다.

키바인딩 문서에서는 macOS의 `Cmd`를 기준으로 설명합니다. Windows에서는 대부분 `Ctrl`로 치환해서 사용합니다.

## Maintenance Rules

- 현재 로컬 환경이 기준이지만, 팀원이 재현하기 어려운 개인 취향이나 임시 설정은 문서화 후 선별합니다.
- 설정 변경은 가능하면 `settings.json`, `keybindings.json`, `extensions.txt`, `vscode-user/` 스냅샷에 함께 반영합니다.
- 문서에는 macOS와 Windows 경로를 같이 남깁니다.
- 커밋 메시지는 `commit-convention` 스킬의 한국어 Conventional Commit 형식을 따릅니다.
- 의미 있는 변경이 없으면 커밋하지 않습니다.
