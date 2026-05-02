# VS Code Global Settings

어떤 컴퓨터/환경에서든 동일한 VS Code 환경을 복원하기 위한 설정 백업입니다.
IntelliJ에서 넘어온 개발자를 위한 세팅으로, One Dark Pro 테마 + JetBrains Mono 폰트 + IntelliJ 키맵을 기본으로 합니다.

---

## Quick Start

```bash
git clone <이 레포 URL> ~/workspace/vscode-setting
cd ~/workspace/vscode-setting
bash install.sh
```

스크립트가 자동으로 기존 settings.json 백업 후 덮어쓰기합니다.

---

## File Structure

```
vscode-setting/
├── README.md                ← 이 문서
├── install.sh               ← 일괄 설치 스크립트 (macOS/Linux)
├── settings.json            ← VS Code 글로벌 settings.json
├── keybindings.json         ← IntelliJ 스타일 커스텀 단축키
├── extensions.txt           ← 확장 프로그램 전체 목록 (카테고리별)
├── pintos-clang-format      ← PintOS C 코딩 스타일 (.clang-format)
├── vscode-user/             ← VS Code User 디렉토리 백업
│   ├── settings.json
│   ├── snippets/            ← 언어별 코드 스니펫
│   └── profiles/woonyong/   ← 프로필별 설정/스니펫
└── scripts/
    ├── apply_to_vscode.py
    ├── export_from_vscode.py
    └── install_extensions.py
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
| Word Wrap | ON |

### Custom Keybindings (IntelliJ Style)

기본적으로 `k--kato.intellij-idea-keybindings` 익스텐션이 IntelliJ 키맵을 제공하며, 아래는 추가 커스텀 오버라이드입니다.

| 단축키 | 기능 | 카테고리 |
|--------|------|----------|
| `Cmd+[` | Navigate Back | Navigation |
| `Cmd+]` | Navigate Forward | Navigation |
| `Cmd+Shift+[` | Previous Tab | Tab |
| `Cmd+Shift+]` | Next Tab | Tab |
| `Alt+Q` | Close Active Tab | Tab |
| `Shift+Alt+Q` | Close All Tabs | Tab |
| `F5` | Start / Continue Debug | Debug |
| `Shift+F5` | Stop Debug | Debug |
| `F6` | Step Out | Debug |
| `F9` | Toggle Breakpoint | Debug |
| `Shift+F9` | Selection to Watch | Debug |
| `Cmd+F11` | Go to Symbol (All) | Search |
| `Ctrl+Up/Down` | 인덴트 단위 커서 이동 | Navigation |
| `Alt+A` | 괄호 안 내용 선택 | Selection |

### Language-specific Formatters

| Language | Formatter | Tab Size | Indent |
|----------|-----------|----------|--------|
| C / C++ | clang-format (file) | 4 | Tab |
| Python | Black | 4 | Space |
| JS / TS / JSX / TSX | Prettier | 2 | Space |
| HTML / CSS / SCSS | Prettier | 2 | Space |
| JSON / JSONC | Prettier | 2 | Space |

공통 설정: `formatOnSave: true`, `formatOnPaste: true`, `formatOnType: true`, `trimTrailingWhitespace: true`, `insertFinalNewline: true`

### Extensions

`extensions.txt`에 카테고리별로 정리되어 있습니다. 주요 카테고리:

- **Theme/UX**: One Dark Pro, JetBrains Icon Theme, IntelliJ Keybindings
- **Editor Tools**: Code Runner, Error Lens, EditorConfig, Rainbow CSV
- **Navigation/Selection**: Indentation Level Movement, Bracket Select, Project Manager
- **Git**: GitLens, Git Graph, GitHub Actions
- **C/C++**: cpptools, CMake, Makefile Tools
- **Python**: Python, Pylance, Black, Pylint, debugpy
- **Web**: Prettier, ESLint, Tailwind CSS, Astro
- **Markdown**: Markdown All in One, Preview GitHub Styles, Mermaid
- **Remote/Container**: Remote SSH, Dev Containers, Docker
- **AI**: Claude Code
- **Jungle**: Jungle Dev Kit, pintos-test-explorer

### Remote/Container Auto-Apply

`settings.json`에 `remote.SSH.defaultExtensions`와 `dev.containers.defaultExtensions`가 설정되어 있어서, SSH 원격이나 DevContainer에 접속할 때 핵심 익스텐션이 자동 설치됩니다.

---

## PintOS C Coding Style (.clang-format)

`pintos-clang-format` 파일은 PintOS 프로젝트의 GNU 기반 C 코딩 스타일을 정의합니다.
프로젝트 루트에 `.clang-format`으로 복사하고, VS Code의 `editor.formatOnSave: true`와 함께 사용하면 저장 시 자동 포맷팅됩니다.

### 적용 방법

```bash
cp ~/workspace/vscode-setting/pintos-clang-format <프로젝트경로>/.clang-format
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
# settings.json 백업
cp ~/Library/Application\ Support/Code/User/settings.json ~/workspace/vscode-setting/settings.json

# keybindings.json 백업
cp ~/Library/Application\ Support/Code/User/keybindings.json ~/workspace/vscode-setting/keybindings.json

# 현재 설치된 확장 목록 내보내기
code --list-extensions > ~/workspace/vscode-setting/extensions.txt
```

### 다른 컴퓨터에 적용

```bash
git clone <레포URL> ~/workspace/vscode-setting
cd ~/workspace/vscode-setting
bash install.sh
```

---

## AI Setup Prompts

아래 프롬프트를 AI 코딩 어시스턴트(Claude, ChatGPT 등)에 붙여넣으면, 이 레포의 세팅을 자동으로 적용합니다.

### Prompt 1: Full Setup (전체 설치)

모든 세팅(테마, 키바인딩, 익스텐션, 포맷터, 폰트)을 한번에 적용합니다.

````
내 VS Code를 아래 세팅으로 전체 설정해줘. OS는 [macOS/Linux/Windows] 이야.

1. 테마/외관:
   - Color Theme: One Dark Pro (zhuangtongfa.material-theme)
   - Icon Theme: JetBrains Icon Theme (chadalen.vscode-jetbrains-icon-theme)
   - Font: JetBrains Mono 14px, ligatures ON, lineHeight 1.6
   - minimap OFF, bracketPairColorization ON, stickyScroll ON
   - cursorSmoothCaretAnimation ON, renderLineHighlight "all", wordWrap ON

2. 키바인딩 (IntelliJ 스타일):
   - 기본: IntelliJ IDEA Keybindings 익스텐션 (k--kato.intellij-idea-keybindings)
   - 커스텀 오버라이드 (keybindings.json에 추가):
     - Cmd+[ / Cmd+] → Navigate Back/Forward
     - Cmd+Shift+[ / Cmd+Shift+] → Previous/Next Tab
     - Alt+Q → Close Tab, Shift+Alt+Q → Close All Tabs
     - F5 → Start/Continue Debug, Shift+F5 → Stop
     - F6 → Step Out, F9 → Toggle Breakpoint, Shift+F9 → Watch
     - Cmd+F11 → Go to Symbol
     - Ctrl+Up/Down → 인덴트 단위 커서 이동 (Indentation Level Movement)
     - Alt+A → 괄호 안 내용 선택 (Bracket Select)

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
   ms-python.black-formatter, ms-python.pylint, esbenp.prettier-vscode,
   dbaeumer.vscode-eslint, yzhang.markdown-all-in-one,
   bierner.markdown-preview-github-styles, ms-azuretools.vscode-docker,
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
````

### Prompt 2: Selective Setup (선택적 설치)

아래 프롬프트에서 필요한 항목만 골라서 사용합니다. `[적용]` / `[제외]` 표시를 변경하세요.

````
내 VS Code를 아래에서 선택한 항목만 설정해줘. OS는 [macOS/Linux/Windows] 이야.
[적용] 또는 [제외]로 표시된 항목을 확인하고, [적용]인 것만 반영해줘.

## 테마/외관
[적용] Color Theme: One Dark Pro
[적용] Icon Theme: JetBrains Icon Theme
[적용] Font: JetBrains Mono 14px, ligatures ON, lineHeight 1.6
[적용] minimap OFF, bracketPairColorization ON, stickyScroll ON

## 키바인딩
[적용] IntelliJ IDEA Keybindings 익스텐션
[적용] 커스텀 단축키 (Navigate, Tab, Debug, Bookmark)

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
[적용] Python (Python, Pylance, Black, Pylint)
[적용] Web (Prettier, ESLint, Tailwind)
[적용] Markdown (All in One, Preview GitHub Styles)
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
````

---

## Windows Notes

Windows에서는 경로가 다릅니다.

| 항목 | 경로 |
|------|------|
| settings.json | `%APPDATA%\Code\User\settings.json` |
| keybindings.json | `%APPDATA%\Code\User\keybindings.json` |
| 익스텐션 설치 | `code --install-extension <id>` (동일) |
| 폰트 | [JetBrains Mono](https://www.jetbrains.com/lp/mono/) 다운로드 후 우클릭 → 설치 |

키바인딩에서 `Cmd` → `Ctrl`로 대체하세요.
