# Environment Agent Guide

이 저장소는 Claude, Codex 같은 AI 에이전트가 Woonyong의 개발 환경을 어디서든 재현하기 위한 기준 저장소다.
에이전트는 이 저장소를 볼 때 VS Code를 기준 소스로 삼고, 다른 IDE가 그 동작을 최대한 따라오게 해야 한다.

## Read Order

1. `ai/manifest.json`
2. `AGENTS.md`
3. `CLAUDE.md`
4. `docs/environment-manager.md`
5. `docs/ide-keymap-policy.md`
6. `docs/platform-support-matrix.md`
7. `docs/conventions/python-google.md`

## Canonical Sources

- AI manifest: `ai/manifest.json`
- 단축키 기준: `keybindings.json`
- VS Code 기본 동작 기준: `settings.json`
- 플랫폼/IDE 매트릭스: `docs/platform-support-matrix.md`
- IDE 간 단축키 정책: `docs/ide-keymap-policy.md`
- 환경 운영 원칙: `docs/environment-manager.md`
- Python 컨벤션: `docs/conventions/python-google.md`

## Core Rules

1. VS Code 단축키를 canonical source로 취급한다.
2. 다른 IDE에는 "같은 기능 의도"를 우선 매핑한다.
3. 단축키가 OS와 충돌하면 다음 우선순위를 따른다.
   - IDE에 동일 키를 그대로 적용
   - IDE keymap에서 inherited shortcut과 충돌 키를 제거
   - 그래도 불가능하면 OS를 바꾸지 않는 fallback 키를 canonical로 문서화
4. IDE 플러그인이 제공하는 기본 키맵을 그대로 신뢰하지 말고, 이 저장소의 override를 우선 적용한다.
5. 머신별 경로, 로그인 세션, 토큰, 캐시는 저장소에 넣지 않는다.
6. macOS와 Windows를 모두 고려한다.
7. Cursor, PyCharm, IntelliJ IDEA도 모두 지원 대상으로 본다.

## IDE Setup Workflow

### VS Code / Cursor

- `settings.json`, `keybindings.json`, `vscode-user/` 스냅샷을 기준으로 적용한다.
- Cursor는 VS Code 계열이지만 별도 CLI와 확장 경로를 가질 수 있으므로 별도로 확인한다.

### JetBrains IDEs

- JetBrains 계열은 `jetbrains/Codex VSCode.xml` 를 공통 keymap source로 사용한다.
- `scripts/apply_to_jetbrains.py` 로 설치된 IDE 설정 디렉터리에 일괄 적용한다.
- 특정 IDE 하나만 급히 맞출 때는 `scripts/apply_to_pycharm.py` 를 사용할 수 있다.
- macOS와 Windows를 모두 지원하도록 스크립트를 유지한다.

## Conflict Policy

- 에디터 탭 이동, 네비게이션, 디버그, 북마크, 심볼 검색은 가능한 한 canonical keyset을 유지한다.
- macOS가 Function key나 일부 시스템 단축키를 가로채면 OS를 바꾸지 않고 문서의 macOS-safe profile을 따른다.
- IDE가 동일 액션 ID를 제공하지 않으면 이름이 아닌 사용자 의도 기준으로 대체한다.

## Update Rules

- 정책 변경 시 `ai/manifest.json`, 관련 스크립트, 관련 문서를 함께 갱신한다.
- 새 AI가 빠르게 적용할 수 있도록 선언형 파일과 설명 문서를 분리한다.
- 사람이 읽는 README와 AI entrypoint의 내용이 충돌하면 실제 적용 파일과 manifest를 우선한다.

## Python Convention Policy

- Python 스타일은 Google Python Style Guide를 기준으로 한다.
- 포맷팅은 `black`, 린트는 `pylint`, 타입 힌트는 현대 Python typing 관례를 기본으로 한다.
- 이 저장소 문서에서 요약한 규칙과 외부 원문 링크를 함께 참고한다.
