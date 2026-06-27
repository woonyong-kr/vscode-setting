# IDE Keymap Policy

이 문서는 여러 IDE를 오가도 손이 바뀌지 않도록, 공통 단축키를 어떻게 유지할지 정리한 기준이다.
현재 공식 프로필은 macOS 시스템 단축키를 바꾸지 않고 사용할 수 있는 `macOS-safe` canonical profile이다.

## Goal

- VS Code를 canonical source로 둔다.
- PyCharm, IntelliJ IDEA, Cursor 등 다른 IDE는 가능한 한 동일한 키와 동일한 사용자 의도를 따른다.
- macOS 시스템 단축키는 수정하지 않는다.
- 충돌이 생기면 OS를 바꾸지 않고 IDE keymap에서 해결한다.

## Canonical Source

- 기준 파일: `keybindings.json`
- JetBrains 적용본: `jetbrains/Codex VSCode.xml`

## Canonical Shortcut Set

| Intent | Canonical key | VS Code command | JetBrains action |
|---|---|---|---|
| Navigate back | `Ctrl+-` | `workbench.action.navigateBack` | `Back` |
| Navigate forward | `Ctrl+Shift+-` | `workbench.action.navigateForward` | `Forward` |
| Previous editor tab | `Ctrl+Alt+Left` | `workbench.action.previousEditor` | `PreviousTab` |
| Next editor tab | `Ctrl+Alt+Right` | `workbench.action.nextEditor` | `NextTab` |
| Close active tab | `Alt+Q` | `workbench.action.closeActiveEditor` | `CloseContent` |
| Close all tabs | `Shift+Alt+Q` | `workbench.action.closeAllEditors` | `CloseAllEditors` |
| Debug start / continue | `Ctrl+Alt+Shift+R` | `workbench.action.debug.start` / `...continue` | `Debug` / `Resume` |
| Debug stop | `Ctrl+Alt+Shift+S` | `workbench.action.debug.stop` | `Stop` |
| Debug step out | `Ctrl+Alt+Shift+O` | `workbench.action.debug.stepOut` | `StepOut` |
| Toggle breakpoint | `Ctrl+Alt+Shift+B` | `editor.debug.action.toggleBreakpoint` | `ToggleLineBreakpoint` |
| Add selection to watch | `Ctrl+Alt+Shift+W` | `editor.debug.action.selectionToWatch` | `XDebugger.AddToWatches` |
| Go to symbol | `Cmd+T` | `workbench.action.showAllSymbols` | `GotoSymbol` |
| Find usages / references | `Ctrl+Alt+F7` | `references-view.findReferences` | `FindUsages` |
| Toggle bookmark | `Ctrl+Alt+M` | `bookmarks.toggle` | `ToggleBookmark` |
| Show bookmarks | `Ctrl+Alt+Shift+M` | `bookmarks.listFromAllFiles` | `ShowBookmarks` |
| Previous bookmark | `Alt+[` | `bookmarks.jumpToPrevious` | `GotoPreviousBookmark` |
| Next bookmark | `Alt+]` | `bookmarks.jumpToNext` | `GotoNextBookmark` |

## Mapping Rules

1. macOS-safe canonical key를 우선 유지한다.
2. IDE 내부 액션 이름이 달라도 사용자 입장에서 같은 동작이면 허용한다.
3. VS Code와 JetBrains 모두에서 어색하지 않은 동작만 공통 키에 올린다.
4. 프로젝트 로컬 키맵보다 사용자 전역 키맵을 우선한다.

## Context-sensitive Shortcuts

아래 키는 "설정이 안 먹은 것"과 "현재 컨텍스트에서 실행할 일이 없는 것"을 구분해서 봐야 한다.

- `Ctrl+-` / `Ctrl+Shift+-`: 네비게이션 히스토리가 있어야 체감된다.
- `Ctrl+Alt+Shift+R/S/O/B/W`: 디버그 세션 또는 디버그 가능한 컨텍스트가 있어야 의미가 있다.
- `Ctrl+Alt+F7`: 참조 제공자(reference provider)가 있는 언어/위치에서만 동작한다.

## Conflict Resolution

### Level 1: Keep the canonical key

- IDE가 지원하고 macOS와 충돌하지 않으면 그대로 유지한다.

### Level 2: Change the IDE key, not the OS

- macOS와 충돌하면 IDE keymap 쪽을 변경한다.
- 가능한 경우 mnemonic이 유지되는 대체 키를 canonical로 승격한다.

### Level 3: Remove inherited conflicts

- JetBrains 부모 keymap에서 올라오는 충돌 shortcut은 custom keymap에서 제거한다.
- 이 저장소는 충돌 제거 규칙까지 포함해 관리한다.

## macOS Notes

- `com.apple.keyboard.fnState = 1` 이면 Function key를 표준 F키로 사용한다.
- 그래도 function-key 계열 충돌은 자주 발생하므로, 현재 canonical keyset은 F-key 의존을 최소화했다.
- 남은 low-level delete/backspace 경고는 텍스트 편집 기본키 영역이라 완전 제거 대상에서 제외할 수 있다.

## JetBrains Policy

- JetBrains 기본 키맵 플러그인을 그대로 쓰지 않고 `Codex VSCode` override를 적용한다.
- 부모 keymap은 `Mac OS X` 를 사용하되, 충돌 shortcut은 custom keymap에서 제거한다.
- 적용 스크립트:

```bash
python3 scripts/apply_to_jetbrains.py
```

## AI Instructions

AI 에이전트가 IDE 설정을 만질 때는 아래 순서를 따른다.

1. `keybindings.json` 을 읽어 canonical key set을 확인한다.
2. 대상 IDE가 지원하는 액션 이름으로 매핑한다.
3. OS 충돌이 있으면 OS를 바꾸지 말고 canonical keyset을 재설계한다.
4. JetBrains 계열은 inherited shortcut 제거까지 같이 갱신한다.
5. 변경 후 적용 스크립트와 문서를 같이 갱신한다.
