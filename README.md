# IDE Environment Settings

이 저장소는 "내 개발 환경을 어디서든 Claude나 Codex로 재현하기 위한 레포" 입니다.
VS Code를 canonical source로 두고, Cursor, PyCharm, IntelliJ IDEA, macOS, Windows까지 함께 고려합니다.
현재 공통 단축키는 OS 시스템 단축키를 건드리지 않아도 되는 `macOS-safe` canonical profile을 기준으로 합니다.

## Start Here

- 사람: [docs/environment-manager.md](docs/environment-manager.md)
- AI: [ai/manifest.json](ai/manifest.json), [AGENTS.md](AGENTS.md), [CLAUDE.md](CLAUDE.md)
- 플랫폼/IDE 범위: [docs/platform-support-matrix.md](docs/platform-support-matrix.md)
- 키맵 정책: [docs/ide-keymap-policy.md](docs/ide-keymap-policy.md)
- Python 컨벤션: [docs/conventions/python-google.md](docs/conventions/python-google.md)

---

## Quick Start

### macOS / Linux

```bash
git clone <이 레포 URL> ~/workspace/ide-setting
cd ~/workspace/ide-setting
bash install.sh
```

### Windows

```powershell
git clone <이 레포 URL> $HOME\workspace\ide-setting
cd $HOME\workspace\ide-setting
powershell -ExecutionPolicy Bypass -File .\install.ps1
```

스크립트가 기존 VS Code User 설정을 백업한 뒤 settings, keybindings, tasks, snippets, curated extensions를 복원합니다.

프로필까지 더 가깝게 맞추려면 VS Code에서 `woonyong` 프로필을 만든 뒤 아래를 실행합니다.

```bash
python3 scripts/apply_to_vscode.py
python3 scripts/install_extensions.py
```

JetBrains 계열 IDE에서는 아래 명령으로 공통 키맵을 일괄 적용합니다.

```bash
python3 scripts/apply_to_jetbrains.py
```

운영 원칙과 재현 범위는 [Environment Manager](docs/environment-manager.md)에 정리되어 있습니다.
단축키 유지 규칙은 [IDE Keymap Policy](docs/ide-keymap-policy.md), 플랫폼/IDE 지원 범위는 [Platform Support Matrix](docs/platform-support-matrix.md), Python 컨벤션은 [Python Conventions](docs/conventions/python-google.md)에 정리되어 있습니다.

---

## File Structure

```
ide-setting/
├── AGENTS.md                ← AI/자동화용 환경 적용 규칙
├── CLAUDE.md                ← Claude용 빠른 진입점
├── README.md                ← 이 문서
├── ai/
│   ├── README.md
│   └── manifest.json        ← AI용 machine-readable source of truth
├── install.sh               ← 일괄 설치 스크립트 (macOS/Linux)
├── install.ps1              ← 일괄 설치 스크립트 (Windows)
├── settings.json            ← VS Code 글로벌 settings.json
├── keybindings.json         ← canonical VS Code 단축키 기준
├── extensions.txt           ← 기본 복원용 curated 확장 목록
├── jetbrains/               ← JetBrains 계열 공통 keymap source
├── pintos-clang-format      ← PintOS C 코딩 스타일 (.clang-format)
├── docs/
│   ├── environment-manager.md
│   ├── ide-keymap-policy.md
│   ├── platform-support-matrix.md
│   └── conventions/python-google.md
├── snapshots/               ← 개발 도구/패키지 매니저 상태 스냅샷
├── vscode-user/             ← VS Code User 디렉토리 백업
│   ├── settings.json
│   ├── keybindings.json
│   ├── snippets/            ← 언어별 코드 스니펫
│   └── profiles/woonyong/   ← 프로필별 설정/스니펫
└── scripts/
    ├── apply_to_jetbrains.py
    ├── apply_to_pycharm.py
    ├── apply_to_vscode.py
    ├── export_from_vscode.py
    ├── install_extensions.py
    └── validate_ai_manifest.py
```

---

## Settings Overview

### Theme & Appearance

| 항목 | 설정 |
|------|------|
| Color Theme | One Dark Pro (IntelliJ Darcula 유사) |
| Icon Theme | JetBrains Icon Theme |
| Font | JetBrains Mono 14px, ligatures ON |
| Line Height | 1.6 |
| Minimap | OFF |
| Bracket Colorization | ON |
| Sticky Scroll | ON |
| Cursor Animation | Smooth |
| Line Highlight | All |
| Word Wrap | OFF |

### Custom Keybindings (Canonical Cross-IDE)

VS Code의 `keybindings.json` 을 canonical source로 사용합니다. 다른 IDE는 이 키와 사용자 의도를 따라오게 맞춥니다.

| 단축키 | 기능 | 카테고리 |
|--------|------|----------|
| `Ctrl+-` | Navigate Back | Navigation |
| `Ctrl+Shift+-` | Navigate Forward | Navigation |
| `Ctrl+Alt+Left` | Previous Tab | Tab |
| `Ctrl+Alt+Right` | Next Tab | Tab |
| `Alt+Q` | Close Active Tab | Tab |
| `Shift+Alt+Q` | Close All Tabs | Tab |
| `Ctrl+Alt+Shift+R` | Start / Continue Debug | Debug |
| `Ctrl+Alt+Shift+S` | Stop Debug | Debug |
| `Ctrl+Alt+Shift+O` | Step Out | Debug |
| `Ctrl+Alt+Shift+B` | Toggle Breakpoint | Debug |
| `Ctrl+Alt+Shift+W` | Selection to Watch | Debug |
| `Cmd+T` | Go to Symbol (All) | Search |
| `Ctrl+Alt+F7` | Find References / Find Usages | Search |
| `Ctrl+Up/Down` | 인덴트 단위 커서 이동 | Navigation |
| `Alt+A` | 괄호 안 내용 선택 | Selection |

JetBrains 계열 IDE는 `jetbrains/Codex VSCode.xml` 로 같은 단축키를 따라오게 합니다.

충돌 처리 원칙:

- canonical keyset은 저장소에서 관리합니다.
- macOS와 충돌하면 OS를 바꾸지 않고 IDE keymap을 재설계합니다.
- 완전 동일 키가 불가능하면 fallback 키를 canonical로 승격하고 문서에 명시합니다.

### Language-specific Formatters

| Language | Formatter | Tab Size | Indent |
|----------|-----------|----------|--------|
| C / C++ | clang-format (file) | 4 | Tab |
| Python | Ruff | 4 | Space |
| JS / TS / JSX / TSX | Prettier | 2 | Space |
| HTML / CSS / SCSS | Prettier | 2 | Space |
| JSON / JSONC | Prettier | 2 | Space |

공통 설정: `formatOnSave: true`, `formatOnPaste: true`, `formatOnType: true`, `trimTrailingWhitespace: true`, `insertFinalNewline: true`

### Python Convention

Python 코드는 Google Python Style Guide를 기준으로 합니다.

- formatter/linter: `ruff`
- Python 전역 환경에서는 줄 길이 제한으로 인한 자동 줄바꿈을 강제하지 않음
- naming/docstring/import 정책: [Python Conventions](docs/conventions/python-google.md) 참고

### Extensions

`extensions.txt`는 새 머신 기본 복원용 curated 목록이고, 실제 이 머신에 설치된 전체 버전 스냅샷은 `vscode-user/extensions-global.txt`에 있습니다. 주요 curated 카테고리:

- **Theme/UX**: One Dark Pro, JetBrains Icon Theme, IntelliJ Keybindings
- **Editor Tools**: Code Runner, Error Lens, EditorConfig, Spell Checker, Rainbow CSV
- **Navigation/Selection**: Indentation Level Movement, Bracket Select, Project Manager
- **Git**: GitLens, Git Graph, GitHub Actions
- **C/C++**: cpptools, CMake, Makefile Tools
- **Python**: Python, Pylance, Ruff, debugpy
- **Web**: Prettier, ESLint, Tailwind CSS, Astro
- **Markdown**: Markdown All in One, Preview GitHub Styles, Mermaid
- **Remote/Container**: Remote SSH, Dev Containers, Docker
- **Diagram**: Draw.io Integration
- **AI**: Claude Code, OpenAI ChatGPT

### Remote/Container Auto-Apply

`settings.json`에 `remote.SSH.defaultExtensions`와 `dev.containers.defaultExtensions`가 설정되어 있어서, SSH 원격이나 DevContainer에 접속할 때 핵심 익스텐션이 자동 설치됩니다.

### Markdown Mermaid Preview

Markdown UML은 ` ```mermaid ` fenced block으로 작성합니다. VS Code에서는 `bierner.markdown-mermaid` 확장으로 Markdown Preview에서 렌더링합니다.

프로젝트의 `.vscode/extensions.json`은 추천 목록이며 자동 설치가 아닙니다. 미리보기에서 Mermaid가 코드 블록으로만 보이면 `code --install-extension bierner.markdown-mermaid`를 실행하거나 Extensions 패널에서 설치하세요.

Cursor를 쓰는 경우 `cursor` CLI와 확장 설치 상태를 별도로 확인해야 합니다. 현재 기준 이 머신은 `cursor` CLI가 PATH에 없고 `code` CLI만 확인됩니다.

계속 안 보이면 Mermaid block을 SVG로 export해서 `![UML](./diagram.svg)`로 연결합니다. 자세한 절차는 [Environment Manager](docs/environment-manager.md)의 Markdown UML and Mermaid Preview 섹션을 참고하세요.

---

## PintOS C Coding Style (.clang-format)

`pintos-clang-format` 파일은 PintOS 프로젝트의 GNU 기반 C 코딩 스타일을 정의합니다.
프로젝트 루트에 `.clang-format`으로 복사하고, VS Code의 `editor.formatOnSave: true`와 함께 사용하면 저장 시 자동 포맷팅됩니다.

### 적용 방법

```bash
cp ~/workspace/ide-setting/pintos-clang-format <프로젝트경로>/.clang-format
```

### 규칙 상세

| 규칙 | 설정값 | 설명 | 예시 |
|------|--------|------|------|
| Base Style | GNU | GNU 코딩 컨벤션 기반 | - |
| Indent | Tab (4칸) | 탭 문자 사용, 너비 4 | `\tint x;` |
| Continuation Indent | 8칸 | 줄 이어쓰기 시 8칸 들여쓰기 | - |
| Column Limit | 79 | 한 줄 최대 79자 | - |
| Return Type | 별도 줄 | 최상위 함수의 반환형이 별도 줄 | `int\nfunc (void)` |
| Brace Style | K&R (same line) | 여는 `{`는 같은 줄, `else`도 `}` 뒤 같은 줄 | `if (x) {` |
| Space Before Parens | Always | 함수명과 괄호 사이 공백 | `func (arg)` |
| Cast Space | After | C 스타일 캐스트 뒤 공백 | `(int) x` |
| Pointer Alignment | Right (변수 쪽) | 포인터 `*`가 변수에 붙음 | `int *ptr` |
| Short Functions | Never | 짧은 함수도 한 줄로 안 씀 | - |
| Short If/Loop | Never | 짧은 if/loop도 한 줄로 안 씀 | - |
| Case Indent | switch와 동일 | case 라벨 별도 들여쓰기 없음 | - |
| Max Empty Lines | 1 | 연속 빈 줄 최대 1줄 | - |
| Sort Includes | OFF | include 순서 변경 안 함 | - |
| Trailing Comments | 1칸 | 주석 앞 공백 1칸 | `x = 1; // comment` |
| Macro Alignment | ON | 매크로 정의 정렬 | - |

### 포맷팅 전/후 예시

```c
// Before
int *func(int a,int b){
    if(a>b){
        return a;
    } else {
        return b;
    }
}

// After (.clang-format 적용)
int *
func (int a, int b) {
    if (a > b) {
        return a;
    } else {
        return b;
    }
}
```

---

## Backup & Update

### 현재 설정 내보내기

```bash
python3 scripts/export_from_vscode.py
```

이 명령은 글로벌 settings/keybindings/tasks/snippets, `woonyong` 프로필 스냅샷, 설치된 extension snapshot을 저장소에 반영합니다.

개발 도구와 패키지 매니저 상태까지 갱신하려면 아래도 함께 실행합니다.

```bash
python3 scripts/export_environment_snapshot.py
```

이 명령은 `snapshots/tool-versions.json`, `snapshots/homebrew-formulae.txt`, `snapshots/homebrew-casks.txt`, `snapshots/npm-global-packages.txt`를 갱신합니다.

JetBrains 계열 IDE keymap을 다시 적용하려면:

```bash
python3 scripts/apply_to_jetbrains.py
```

### 다른 컴퓨터에 적용

macOS/Linux:

```bash
git clone <레포URL> ~/workspace/ide-setting
cd ~/workspace/ide-setting
bash install.sh
```

Windows:

```powershell
git clone <레포URL> $HOME\workspace\ide-setting
cd $HOME\workspace\ide-setting
powershell -ExecutionPolicy Bypass -File .\install.ps1
```

---

## AI Setup Prompts

아래 프롬프트를 AI 코딩 어시스턴트(Claude, ChatGPT 등)에 붙여넣으면, 이 레포의 세팅을 자동으로 적용합니다.

### Prompt 1: Full Setup (전체 설치)

모든 세팅(테마, 키바인딩, 익스텐션, 포맷터, 폰트)을 한번에 적용합니다.

````
내 IDE 환경을 아래 세팅으로 전체 설정해줘. 기준 저장소는 ide-setting 이고, OS는 [macOS/Linux/Windows] 이야.

1. 테마/외관:
   - Color Theme: One Dark Pro (zhuangtongfa.material-theme)
   - Icon Theme: JetBrains Icon Theme (chadalen.vscode-jetbrains-icon-theme)
   - Font: JetBrains Mono 14px, ligatures ON, lineHeight 1.6
   - minimap OFF, bracketPairColorization ON, stickyScroll ON
   - cursorSmoothCaretAnimation ON, renderLineHighlight "all", wordWrap OFF

2. 키바인딩 (macOS-safe canonical):
   - VS Code keybindings.json을 canonical source로 사용
   - 커스텀 오버라이드:
     - Ctrl+- / Ctrl+Shift+- → Navigate Back/Forward
     - Ctrl+Alt+Left / Ctrl+Alt+Right → Previous/Next Tab
     - Alt+Q / Shift+Alt+Q → Close Tab / Close All Tabs
     - Ctrl+Alt+Shift+R → Start/Continue Debug
     - Ctrl+Alt+Shift+S → Stop Debug
     - Ctrl+Alt+Shift+O → Step Out
     - Ctrl+Alt+Shift+B → Toggle Breakpoint
     - Ctrl+Alt+Shift+W → Add Selection to Watch
     - Cmd+T → Go to Symbol
     - Ctrl+Alt+F7 → Find References / Find Usages
     - Ctrl+Alt+M / Ctrl+Alt+Shift+M → Toggle Bookmark / Show Bookmarks
     - Alt+[ / Alt+] → Previous / Next Bookmark
   - macOS 시스템 단축키는 수정하지 말고 IDE keymap에서 충돌을 해결

3. 포맷터:
   - formatOnSave: true, formatOnPaste: true, formatOnType: true
   - trimTrailingWhitespace: true, insertFinalNewline: true
   - C/C++: clang-format (style: file), tabSize 4, tab 문자
   - Python: Black, tabSize 4, space
   - JS/TS/HTML/CSS/JSON: Prettier, tabSize 2, space
   - ESLint: singleQuote, semi, 80 columns, trailing comma

4. 확장 프로그램 (전체 설치):
   zhuangtongfa.material-theme, chadalen.vscode-jetbrains-icon-theme,
   k--kato.intellij-idea-keybindings, formulahendry.code-runner,
   editorconfig.editorconfig, usernamehw.errorlens,
   kaiwood.indentation-level-movement, chunsen.bracket-select,
   alefragnani.project-manager, eamodio.gitlens, mhutchie.git-graph,
   ms-vscode.cpptools, ms-vscode.cpptools-extension-pack,
   ms-vscode.makefile-tools, ms-python.python, ms-python.vscode-pylance,
   charliermarsh.ruff, esbenp.prettier-vscode,
   dbaeumer.vscode-eslint, yzhang.markdown-all-in-one,
   bierner.markdown-preview-github-styles, bierner.markdown-mermaid,
   davidanson.vscode-markdownlint, ms-azuretools.vscode-docker,
   ms-vscode-remote.remote-containers, ms-vscode-remote.remote-ssh,
   tomoki1207.pdf, mechatroner.rainbow-csv, anthropic.claude-code

5. Remote/Container 자동 전파:
   - settings.json에 remote.SSH.defaultExtensions, dev.containers.defaultExtensions 배열로
     핵심 익스텐션 ID 추가 (원격 접속 시 자동 설치)

6. JetBrains Mono 폰트 설치:
   - macOS: brew install --cask font-jetbrains-mono
   - Linux: apt install fonts-jetbrains-mono 또는 GitHub Release에서 다운로드
   - Windows: https://www.jetbrains.com/lp/mono/ 에서 다운로드 후 설치

위 내용을 settings.json, keybindings.json에 반영하고 확장 프로그램을 설치해줘.
JetBrains IDE가 있으면 jetbrains/Codex VSCode.xml 기준으로 같은 의도의 키맵도 함께 맞춰줘.
````

### Prompt 2: Selective Setup (선택적 설치)

아래 프롬프트에서 필요한 항목만 골라서 사용합니다. `[적용]` / `[제외]` 표시를 변경하세요.

````
내 IDE 환경을 아래에서 선택한 항목만 설정해줘. 기준 저장소는 ide-setting 이고, OS는 [macOS/Linux/Windows] 이야.
[적용] 또는 [제외]로 표시된 항목을 확인하고, [적용]인 것만 반영해줘.

## 테마/외관
[적용] Color Theme: One Dark Pro
[적용] Icon Theme: JetBrains Icon Theme
[적용] Font: JetBrains Mono 14px, ligatures ON, lineHeight 1.6
[적용] minimap OFF, bracketPairColorization ON, stickyScroll ON

## 키바인딩
[적용] canonical keybindings.json 기준 커스텀 단축키
[적용] macOS 시스템 단축키를 바꾸지 않는 JetBrains override

## 포맷터
[적용] formatOnSave + trimTrailingWhitespace + insertFinalNewline
[적용] C/C++: clang-format (file), tab 4
[적용] Python: Black, space 4
[적용] JS/TS: Prettier, space 2
[적용] ESLint rules (semi, singleQuote, indent 2)

## 익스텐션 카테고리
[적용] Theme/UX (One Dark Pro, JetBrains Icons, IntelliJ Keys)
[적용] Editor Tools (Code Runner, Error Lens, EditorConfig)
[적용] Navigation/Selection (Indentation Level Movement, Bracket Select, Project Manager)
[적용] Git (GitLens, Git Graph)
[적용] C/C++ (cpptools, Makefile Tools)
[적용] Python (Python, Pylance, Ruff)
[적용] Web (Prettier, ESLint, Tailwind)
[적용] Markdown (All in One, Preview GitHub Styles, Mermaid, Markdownlint)
[적용] Remote/Container (SSH, Dev Containers, Docker)
[적용] AI (Claude Code)

## Remote 자동 전파
[적용] remote.SSH.defaultExtensions 설정
[적용] dev.containers.defaultExtensions 설정

## 폰트 설치
[적용] JetBrains Mono 폰트 설치

---
예시: 테마만 빼고 전부 적용하려면 테마/외관의 Color Theme, Icon Theme을 [제외]로 변경.
예시: 키바인딩만 적용하려면 키바인딩 섹션만 [적용], 나머지 전부 [제외]로 변경.

[적용]으로 표시된 항목만 settings.json, keybindings.json에 반영하고
해당 확장 프로그램을 설치해줘.
JetBrains IDE가 있으면 jetbrains/Codex VSCode.xml 기준 keymap도 같이 맞춰줘.
````

---

## Windows Notes

Windows에서는 `install.ps1`을 우선 사용합니다. 수동으로 확인할 때는 경로가 다릅니다.

| 항목 | 경로 |
|------|------|
| settings.json | `%APPDATA%\Code\User\settings.json` |
| keybindings.json | `%APPDATA%\Code\User\keybindings.json` |
| 익스텐션 설치 | `code --install-extension <id>` (동일) |
| 폰트 | [JetBrains Mono](https://www.jetbrains.com/lp/mono/) 다운로드 후 우클릭 → 설치 |

키바인딩에서 `Cmd` → `Ctrl`로 대체하세요.
