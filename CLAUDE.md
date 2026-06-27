# Claude Environment Guide

이 저장소는 Claude, Codex 같은 AI 에이전트가 Woonyong의 개발 환경을 재구성하기 위한 기준 저장소다.

Claude가 이 저장소를 다룰 때는 아래 순서로 읽는다.

1. `ai/manifest.json`
2. `AGENTS.md`
3. `docs/environment-manager.md`
4. `docs/ide-keymap-policy.md`
5. `docs/platform-support-matrix.md`
6. `docs/conventions/python-google.md`

핵심 원칙:

- 이 저장소의 목적은 "내 환경을 어디서든 AI로 재현"하는 것이다.
- VS Code는 editor behavior의 canonical source다.
- PyCharm, IntelliJ IDEA, Cursor는 VS Code의 의도와 keymap policy를 따라간다.
- macOS와 Windows를 모두 고려한다.
- OS 시스템 단축키는 변경하지 않는다.
- 머신별 비밀정보, 로그인 세션, 캐시, 개인 절대경로는 커밋하지 않는다.

실행 우선순위:

- VS Code 계열 적용: `settings.json`, `keybindings.json`, `vscode-user/`, `scripts/apply_to_vscode.py`
- JetBrains 계열 적용: `jetbrains/Codex VSCode.xml`, `scripts/apply_to_jetbrains.py`
- 환경 스냅샷 갱신: `scripts/export_environment_snapshot.py`
- 무결성 검증: `scripts/validate_ai_manifest.py`

Claude는 문서 요약보다 실제 적용 파일과 스크립트 동작을 우선 신뢰한다.
