# VS Code 글로벌 세팅

어떤 컴퓨터/환경에서든 동일한 VS Code 환경을 복원하기 위한 설정 백업입니다.

## 빠른 시작 (새 컴퓨터)

```bash
git clone <이 레포 URL> ~/workspace/vscode-setting
cd ~/workspace/vscode-setting
bash install.sh
```

## 파일 구조

```
vscode-setting/
├── README.md            ← 이 문서
├── install.sh           ← 일괄 설치 스크립트 (settings + keybindings + extensions + 폰트)
├── settings.json        ← 글로벌 settings.json (테마, 폰트, 포맷터, 언어별 설정)
├── keybindings.json     ← 커스텀 단축키 (IntelliJ 스타일 + 북마크 + 디버그)
└── extensions.txt       ← 설치할 확장 프로그램 목록 (카테고리별 정리)
```

## 핵심 세팅 요약

### 테마/외관

- 테마: **One Dark Pro** (`zhuangtongfa.material-theme`)
- 아이콘: **JetBrains Icon Theme** (`chadalen.vscode-jetbrains-icon-theme`)
- 폰트: **JetBrains Mono** (14px, ligatures ON, lineHeight 1.6)
- 미니맵 OFF, 브래킷 컬러링 ON, 스티키 스크롤 ON

### 키맵

- **IntelliJ IDEA Keybindings** 기반
- 커스텀 오버라이드: `keybindings.json` 참고

### 커스텀 단축키 (keybindings.json)

단축키기능비고`Cmd+[` / `Cmd+]`이전/다음 화면IntelliJ 네비게이션`Cmd+Shift+[` / `]`이전/다음 탭탭 이동`Alt+Q`현재 탭 닫기`Shift+Alt+Q`모든 탭 닫기`F5`디버그 시작/계속`Shift+F5`디버그 중지`F6`Step OutIntelliJ 스타일`F9`브레이크포인트 토글IntelliJ 스타일`Shift+F9`Watch에 추가`Cmd+F11`심볼 검색`Alt+F9`북마크 토글Bookmarks 익스텐션`Cmd+F10`전체 북마크 목록`Alt+]` / `Alt+[`다음/이전 북마크

### 언어별 포맷터

언어포맷터탭스페이스C/C++clangFormat (Google)4탭 문자PythonBlack4스페이스JS/TS/JSON/HTML/CSSPrettier2스페이스

### DevContainer 자동 적용

`dev.containers.defaultExtensions` 설정으로 DevContainer를 열 때 자동으로 핵심 익스텐션이 설치됩니다. `remote.SSH.defaultExtensions`도 동일하게 설정되어 SSH 원격에서도 같은 환경입니다.

## 설정 변경 시 백업 방법

```bash
# 현재 설정을 이 폴더에 덮어쓰기
cp ~/Library/Application\ Support/Code/User/settings.json ~/workspace/vscode-setting/
cp ~/Library/Application\ Support/Code/User/keybindings.json ~/workspace/vscode-setting/
code --list-extensions > ~/workspace/vscode-setting/extensions-raw.txt

# 커밋
cd ~/workspace/vscode-setting && git add -A && git commit -m "chore: VS Code 설정 업데이트"
```

## 확장 프로그램 카테고리

전체 목록은 `extensions.txt` 참고. 주요 카테고리:

- **테마/UX**: One Dark Pro, JetBrains Icon, IntelliJ Keybindings, 한국어 팩
- **에디터 도구**: Code Runner, Error Lens, Spell Checker, Rainbow CSV, PDF Viewer
- **북마크/TODO**: Bookmarks, Todo Tree
- **Git**: GitLens, Git Graph, GitHub Actions
- **C/C++**: cpptools, Makefile Tools, CMake Tools
- **Python**: Python, Pylance, Black, Pylint
- **Web**: Prettier, ESLint, Tailwind CSS
- **Markdown**: Markdown All in One, GitHub Preview, Mermaid, Markdownlint
- **Remote**: Remote SSH, Containers, WSL, Docker
- **AI**: Claude Code
